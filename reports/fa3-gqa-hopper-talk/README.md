# FA3 on Hopper and Our GQA Kernel

从硬件原语、执行模型，到我们在 TileLang 中的实现

---

## 1. Why GQA Deserves Its Own Discussion

**核心观点**

`GQA` 不是简单的 “MHA 少几个 KV heads”，它首先改变了 workload structure。

**要点**

- 多个 `Q heads` 共享同一个 `KV head`
- 这会显著改变 `KV` footprint
- 也会改变后续 kernel 优化的重点

---

## 2. What Hopper Changes for Attention Kernels

**核心观点**

Hopper 改变的不是“峰值算力数字”，而是高性能 attention kernel 的设计空间。

**要点**

- `WGMMA`：Hopper 把 Tensor Core 主计算提升到 warpgroup 粒度。一个 warpgroup 由 `4 warps / 128 threads` 组成，协同 issue `wgmma.mma_async`，这比旧的 warp-level `mma.sync` 更适合大 tile 和深流水。
- `TMA`：Hopper 新增了专门的数据搬运硬件。单线程提交 tensor descriptor 和 block coordinates 之后，多维地址生成与 `GMEM <-> SMEM` 搬运由硬件完成，并通过 `mbarrier` / async barrier 通知完成。
- `WGMMA` 解决的是 compute roofline，`TMA` 解决的是 feed roofline。`TMA` 本身不会提高 HBM 峰值带宽，但会显著降低地址生成、copy loop 和线程占用开销，提高有效带宽利用率。
- 对我们关心的 dense `BF16/FP16` Tensor Core 路径，`H100/H200 SXM` 的理论峰值约为 `989 TFLOPS`；官方给出的带 sparsity 标称是 `1,979 TFLOPS`。`H200` 还提供 `4.8 TB/s` 的 `HBM3e` 带宽。
- 因此，attention kernel 的核心问题不再只是“算对”，而是能否让 `WGMMA` 持续有活干，并让 `TMA`、barrier 和寄存器分配不成为瓶颈。

---

## 3. What FA2 Already Got Right, and What It Left on the Table

**核心观点**

`FA2` 已经有正确的算法基础，但还不是围绕 Hopper async execution model 写的。

**要点**

- `FA2` 已经有 IO-aware FlashAttention formulation
- `FA2` 已经支持 `MQA/GQA`
- `FA2` 通过 indexing 避免复制 `K/V`
- 但 `FA2` 没有把 kernel 重写成 Hopper-native 的执行模型

---

## 4. FA3's Hopper-Specific Intra-Tile Redesign

**核心观点**

`FA3` 主要重写的是 tile 内执行模型：围绕 `WGMMA`、`TMA` 和 `ping-pong` pipeline 重新组织 kernel。

![Slide 5 Figure](figures/slide5_fa3_hopper_intra_tile.png)

**要点**

- `WGMMA`：Hopper 的 warpgroup-level Tensor Core 原语
- `TMA`：Hopper 的异步 GMEM -> SMEM 搬运原语
- `pipeline GEMM` 是目标：让 `TMA + QK + softmax-side work + PV` 重叠推进
- `ping-pong` 是组织方式：`1 producer + 2 consumers` 在 steady state 里交替接力

**这一页最重要的是依赖关系**

- `K` 的 `TMA` 先完成，consumer 才能开始当前拍的 `QK`
- `QK` 发出之后，不需要等整个 tile 都算完，另一组 consumer 就可以被 release，开始接下一拍
- softmax-side work 要等 `QK` 到达可消费阶段，也就是 `wait<1> + acc_s fence` 之后才能开始
- `PV` 还额外依赖对应的 `V tile ready`，所以它要等 `v_full`
- `V buffer` 只有在 `PV` 真正完成，也就是 `wait<0> + acc_o fence` 之后，才能通过 `v_empty` 归还给 producer
- `K buffer` 的释放更早，在 `QK` 对应结果已经进入 softmax-side 路径后，就可以通过 `k_empty` 提前归还

**把它按一拍 steady state 展开，可以读成：**

1. producer 等 `k_empty`，然后搬下一拍 `K`
2. `k_full` 发布后，当前 consumer 开始 `QK`
3. `QK` 发出后，named barrier release 另一组 consumer
4. 当前 consumer 等 `wait<1>`，然后进入 softmax-side work
5. 与此同时，如果上一拍的 `V` 已 ready，则当前拍可以发 `PV`
6. `PV` 完成并经过 `wait<0>` 后，`V buffer` 才能通过 `v_empty` 释放
7. producer 看到 `k_empty / v_empty` 后，再推进后续 `TMA`

**所以真正的 overlap 不是“所有步骤同时做”，而是：**

- producer 在搬下一拍 `K/V`
- 一个 consumer 在做当前拍 `QK`
- 另一个 consumer 在做上一拍相关的 softmax-side work / `PV`

这三类工作被 barrier 和 fence 精确地错开，而不是简单串行。

**一个关键数字**

- `FA2` 在 `H100` 上大约只有 `35%` utilization
- `FA3` 的意义就在于把这部分 Hopper execution gap 补上

---

## 5. GQA Semantics and Decode Optimizations

**核心观点**

对 decode 而言，`FA3` 既有通用优化，也有建立在 `GQA` 结构上的附加优化。

![Slide 6 Figure](figures/slide6_fa3_gqa_packing.png)

**左边：语义结构**

- `GQA` 中多个 `Q heads` 共享一个 `KV head`
- 这只是 shared-KV semantics，本身还不是硬件优化

**右边上半部分：通用 decode 优化**

- `KV split / Flash Decoding`
- 这是 decode 的通用优化
- `MHA` 也能使用

**右边下半部分：GQA-specific 优化**

- `GQA packing`
- 当 `Q` 太短时，单个 query head 很难把 tile 填满
- `MQA/GQA` 可以把共享同一 `KV head` 的多个 query heads 一起 pack 起来

**结论**

- `KV split` 解决的是 decode 并行度问题
- `GQA packing` 解决的是短 `Q` 下 tile 利用率问题

---

## 6. How We Realize FA3 in TileLang

**核心观点**

我们的实现把 `FA3` 落成了三个层次：`shared-KV` 语义、decode 期工作切分、tile 内执行层，而且这三层在 `FA3` 与 `TileLang` 里是一一对应的。

| 层次 | 这一层回答什么问题 | FA3 中怎么实现 | FA3 原语 / 机制 | TileLang 中的实现 |
| --- | --- | --- | --- | --- |
| Shared-KV semantics | “谁和谁共享同一个 `KV head`？” | `GQA/MQA` 通过 head indexing 保留 shared-KV，不复制 `K/V` | head remap / tensor indexing / grouped head layout | head mapping / grouped work decomposition |
| Decode-side work partition | “decode 时这些工作怎么切、怎么分派？” | `KV split / Flash Decoding` + `GQA packing` heuristic | split-KV launch / partial reduction / `pack_gqa` reshape | persistent outer scheduling / dispatch policy |
| Intra-tile engine | “一个 tile 内部怎么把硬件吃满？” | `TMA + WGMMA + ping-pong + wait/fence` | `TMA`, `mbarrier`, `WGMMA`, `wait_group`, named barrier | `T.tma_copy` / `T.wgmma_gemm` / barrier / `T.wait_wgmma` / fence |

**结论**

`TileLang` 不是只支持某个原语，而是能把 `FA3` 这三层结构都显式表达出来。

---

## 7. Code Skeleton: Registers, TMA, WGMMA, and Fences

**核心观点**

代码骨架已经把 `FA3/Hopper` 的关键结构写出来了：寄存器再分配、`TMA`、`WGMMA`、barrier handoff、`wait/fence`。

```python
tx = T.get_thread_binding()

if tx < 128:
    # Producer WG
    T.dec_max_nreg(24)
    for n_idx in T.Pipelined(loop_range, num_stages=0):
        T.barrier_wait(k_empty, (n_idx + 1) % 2)   # 等 K buffer 可复用
        T.tma_copy(..., barrier=k_full)            # 发起 K 的 TMA
        T.barrier_arrive(k_full)                   # 发布 K ready

        if n_idx > 0:
            T.barrier_wait(v_empty, n_idx % 2)     # 等 V buffer 可复用
            T.tma_copy(..., barrier=v_full)        # 发起 V 的 TMA
            T.barrier_arrive(v_full)               # 发布 V ready

elif tx < 256:
    # Consumer WG1
    T.inc_max_nreg(240)
    T.call_extern("handle", "tl::barrier_arrive_named", 1, 256)

    for n_idx in T.Pipelined(loop_range, num_stages=0):
        T.barrier_wait(k_full, n_idx % 2)          # 等 K tile ready
        T.sync_threads(barrier_id=1, arrive_count=256)

        T.wgmma_gemm(...)                          # QK

        if n_idx > 0:
            T.barrier_wait(v_full, (n_idx - 1) % 2)
            T.wgmma_gemm(...)                      # PV

        T.call_extern("handle", "tl::barrier_arrive_named", 2, 256)
        T.wait_wgmma(1)                            # QK 可进入 softmax-side
        T.warpgroup_fence_operand(acc_s_1, num_regs=64)
        T.barrier_arrive(k_empty)                  # K buffer 可回收
        softmax_1(...)
        T.wait_wgmma(0)                            # PV 完成
        T.warpgroup_fence_operand(acc_o_1, num_regs=64)
        T.barrier_arrive(v_empty)                  # V buffer 可回收

else:
    # Consumer WG2
    # 与 WG1 对称，形成 1 producer + 2 consumers 的 ping-pong
    ...
```

**这段代码对应的结构**

- producer 和 consumer 的寄存器预算不一样
- `TMA` 和 `WGMMA` 是显式的
- `wait/fence` 不是装饰，而是 async pipeline 的边界
- 真实结构始终是 `1 producer + 2 consumers`
- 这里代码只详细展开了 `producer + WG1`，`WG2` 是与 `WG1` 对称的第二个 consumer

完整注释版素材见：
- [slide8_code_skeleton.md](assets/slide8_code_skeleton.md)

---

## 8. Takeaways

**最重要的结论**

这部分最重要的不是某个孤立 trick，而是一整套对齐关系：workload structure、decode policy 和 Hopper execution model 必须一起对齐。

**请记住这四点**

1. `GQA` 先改变 workload structure：shared-KV semantics
2. `FA3` 再重写 Hopper 上的执行模型：`TMA + WGMMA + ping-pong`
3. decode 上有两层优化：通用的 `KV split`，以及 `MQA/GQA` 上附加的 `GQA packing`
4. `TileLang` 能把这整套结构显式写出来，这也是后续 locality、register-flow 和 scheduling 优化的基础

---

## 9. Transition to Our Optimizations

到这里，应该已经能分清三件事：

- 哪些是语义
- 哪些是 decode policy
- 哪些是 Hopper execution machinery

这也是后面继续讲我们自己的优化工作时，不会丢主线的原因。

---

## References

**Figure references**

- Slide 5 figure (`slide5_fa3_hopper_intra_tile.png`)
  - 基于我们自己的 Hopper WS kernel 实现与时间线整理绘制
  - 对应代码骨架见 [\_test_ws_fa3_v2_threadbind_opt.py](/home/ga/TileOPs/_test_ws_fa3_v2_threadbind_opt.py)
- Slide 6 left panel
  - Ainslie et al., *GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints*, Figure 2
  - Paper: https://arxiv.org/abs/2305.13245
- Slide 6 right panel, upper half (`KV split / Flash Decoding`)
  - Tri Dao, *FlashAttention-3* GTC slides, p.17
  - Slides: /home/ga/TileOPs/experiments/ws_kernel_evolution/notes/fa3_gqa_hopper_talk/assets/external/gtc/fa3_gtc.pdf
- Slide 6 right panel, lower half (`GQA packing`)
  - Tri Dao, *FlashAttention-3* GTC slides, p.18
  - Slides: /home/ga/TileOPs/experiments/ws_kernel_evolution/notes/fa3_gqa_hopper_talk/assets/external/gtc/fa3_gtc.pdf

**Paper and hardware references**

- Dao, *FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning*
  - https://tridao.me/publications/flash2/flash2.pdf
- Shah et al., *FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision*
  - https://tridao.me/publications/flash3/flash3.pdf
- NVIDIA Hopper architecture overview / technical blog
  - https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/
- NVIDIA H100 product page
  - https://www.nvidia.com/en-eu/data-center/h100/
- NVIDIA H200 product page
  - https://www.nvidia.com/es-la/data-center/h200/
