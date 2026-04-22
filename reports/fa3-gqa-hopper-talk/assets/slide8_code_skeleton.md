# Slide 8 Code Skeleton

This page should show that the FA3-style Hopper structure is already explicit in
our TileLang code skeleton, before discussing later optimizations such as
reorder or anchor.

## What This Slide Should Highlight

- `Register budgeting`
  - producer gives registers back with `T.dec_max_nreg(24)`
  - consumers claim them with `T.inc_max_nreg(240)`
- `TMA movement`
  - producer waits on `k_empty / v_empty`
  - then issues `T.tma_copy(...)`
  - then publishes `k_full / v_full`
- `WGMMA compute`
  - consumers use `T.wgmma_gemm(...)` for both `QK` and `PV`
- `Barrier / handoff`
  - `T.barrier_wait(...)`
  - `T.call_extern(... "tl::barrier_arrive_named", ...)`
  - `T.sync_threads(barrier_id=..., arrive_count=256)`
- `Fence / wait`
  - `T.wait_wgmma(1)` gates softmax-side consumption
  - `T.wait_wgmma(0)` gates output-side completion
  - `T.warpgroup_fence_operand(...)` marks accumulator handoff to scalar code

## Suggested On-Slide Structure

- Left: one code snippet
- Right: 4-5 short callouts
- Do not show the whole kernel
- Only keep the structural backbone
- Important: the real kernel is still `1 producer + 2 consumers`
- On slide, we show `producer + WG1` in detail, and explain that `WG2` is the symmetric second consumer

## Curated Snippet

Source:
- [\_test_ws_fa3_v2_threadbind_opt.py](/home/ga/TileOPs/_test_ws_fa3_v2_threadbind_opt.py:171)

```python
# FA3/Hopper 的 tile 内执行模型：
# - Producer 主要负责 TMA 搬运 K/V
# - Consumer 主要负责 WGMMA 计算 QK / PV
# - ping-pong 的目标不是“换一种写法”，而是把数据搬运、
#   QK、softmax-side work、PV 组织成可重叠的 steady state
#
# FA3-style register reallocation:
# - Producer 主动让出寄存器，换取两个 consumer 更大的计算窗口
# - 这不是局部微调，而是 warp-specialized schedule 的资源再分配
#   Producer dec:  128 * (168 - 24)  = 18432 regs released
#   Consumer inc:  256 * (240 - 168) = 18432 regs claimed

tx = T.get_thread_binding()

if tx < 128:
    # Producer WG:
    # - 只负责把 K/V 通过 TMA 喂进 shared memory
    # - full / empty barrier 管理双缓冲 slot 的“可读”和“可复用”
    T.dec_max_nreg(24)
    for n_idx in T.Pipelined(loop_range, num_stages=0):
        # 先等消费者把 K buffer 归还，再重用这一拍的 K slot
        T.barrier_wait(k_empty, (n_idx + 1) % 2)
        # ^ 等上一轮 consumer 对这块 K buffer 的使用完全结束
        #   然后 producer 才能把新的 K tile 搬进来

        T.tma_copy(k[..., head_kv, :], k_smem_0 if n_idx % 2 == 0 else k_smem_1, barrier=k_full)
        # ^ 发起一次 TMA：把当前拍 K tile 从 GMEM 搬到 SMEM
        #   这一步对应 Slide 5 里 producer lane 的 K movement

        T.barrier_arrive(k_full)
        # ^ 发布 k_full：告诉 consumer 这一拍的 K tile 已 ready
        #   consumer 后面才能安全开始 QK

        if n_idx > 0:
            # V 同理：empty 表示上一拍消费者已经释放了该 buffer
            T.barrier_wait(v_empty, n_idx % 2)
            # ^ 等上一拍 PV 对 V buffer 的消费结束，然后复用这块 V slot

            T.tma_copy(v[..., head_kv, :], v_smem_0 if (n_idx - 1) % 2 == 0 else v_smem_1, barrier=v_full)
            # ^ 发起一次 TMA：把上一拍 PV 需要的 V tile 搬进来
            #   K 和 V 的 producer wave 在 steady state 中错开推进

            T.barrier_arrive(v_full)
            # ^ 发布 v_full：告诉 consumer 对应的 V tile 已 ready

elif tx < 256:
    # Consumer WG1:
    # - 负责 QK / PV 两段 WGMMA
    # - 通过 named barrier 和另一组 consumer 交替接力
    # - 这就是 Slide 5 里的 ping-pong consumer structure
    T.inc_max_nreg(240)
    T.call_extern("handle", "tl::barrier_arrive_named", 1, 256)
    # ^ bootstrap 阶段先在 named barrier 1 上 arrive 一次
    #   这样后面的第一次 bar.sync(1, 256) 才能由 WG1/WG2 一起凑满 256
    T.clear(acc_o_1)
    T.clear(ls_1)
    T.fill(sm_1, -T.infinity(accum_dtype))
    T.clear(acc_s_1)

    for n_idx in T.Pipelined(loop_range, num_stages=0):
        # k_full 保证当前拍的 K tile 已经就绪
        # named barrier 保证 WG1 / WG2 的调度接力节奏
        T.barrier_wait(k_full, n_idx % 2)
        # ^ 等 producer 把当前拍 K tile 准备好
        #   没有这个条件，QK 不能开始

        T.sync_threads(barrier_id=1, arrive_count=256)
        # ^ 等 named barrier 满足 256 个到达
        #   表示 WG1 / WG2 在这一拍的调度接力已经对齐

        # 第一段主计算：QK
        T.wgmma_gemm(q_shared_1, k_smem_0 if n_idx % 2 == 0 else k_smem_1,
                     acc_s_1, transpose_B=True, policy=T.GemmWarpPolicy.FullRow)
        # ^ 发起 QK 这段 WGMMA
        #   这是 consumer 的第一段 Tensor Core 主计算

        if n_idx > 0:
            # 第二段主计算：PV
            # 在 steady state 里，QK 和上一拍的 V consumption 会交叠推进
            T.barrier_wait(v_full, (n_idx - 1) % 2)
            # ^ 等上一拍对应的 V tile ready，之后才能进入 PV

            T.wgmma_gemm(acc_s_cast_1, v_smem_0 if (n_idx - 1) % 2 == 0 else v_smem_1,
                         acc_o_1, policy=T.GemmWarpPolicy.FullRow)
            # ^ 发起 PV 这段 WGMMA
            #   与当前拍的 QK 和 softmax-side work 共同构成 steady-state overlap

        # 释放另一组 consumer，形成 ping-pong handoff
        T.call_extern("handle", "tl::barrier_arrive_named", 2, 256)
        # ^ WG1 在这一拍关键计算发出后，release WG2
        #   这样另一组 consumer 才能接着推进下一拍

        # wait<1> + acc_s fence:
        # - 表示 QK 这段 async WGMMA 已经到达 softmax 可消费阶段
        # - 这对应 Slide 5 里“softmax-side work”进入的位置
        T.wait_wgmma(1)
        # ^ 等到只剩 1 组未完成的 async WGMMA
        #   此时 acc_s 已经可以进入 softmax-side 标量路径

        T.warpgroup_fence_operand(acc_s_1, num_regs=64)
        # ^ 给 acc_s 加 fence：把 Tensor Core accumulator
        #   变成后续 softmax 可以安全读取的 operand

        T.barrier_arrive(k_empty)
        # ^ 发布 k_empty：告诉 producer 这一拍的 K buffer 可以回收重用

        softmax_1(acc_s_1, sm_1, smp_1, ss_1, ssum_1, ls_1)
        # ^ 执行 online softmax / rescale 相关标量工作
        #   这就是 Slide 5 里与 GEMM 重叠的 softmax-side work

        # wait<0> + acc_o fence:
        # - 表示 PV 结果已经稳定
        # - 后续才能安全释放 V buffer，或者进入 output-side 路径
        T.wait_wgmma(0)
        # ^ 等相关 async WGMMA 全部完成
        #   到这里 acc_o 才是稳定可消费的输出累加值

        T.warpgroup_fence_operand(acc_o_1, num_regs=64)
        # ^ 给 acc_o 加 fence：output-side 路径之后才能安全读取它

        T.barrier_arrive(v_empty)
        # ^ 发布 v_empty：告诉 producer 这一拍的 V buffer 可以释放
        #   下一轮 TMA 才能安全复用它

else:
    # Consumer WG2:
    # - 是第二个对称的 consumer
    # - 与 WG1 交替接力，形成完整的 1 producer + 2 consumers ping-pong
    # - 代码结构与 WG1 基本对称，区别主要在 barrier_id 和处理的 half tile
    ...
```

## Why The Snippet Only Expands WG1

- 真正的 kernel 结构始终是 `1 producer + 2 consumers`
- 这里不把 WG2 全量展开，只是因为它和 WG1 基本对称
- Slide 上如果把两个 consumer 都完整贴出来，代码密度会过高，反而不利于讲清主线
- 更好的讲法是：
  - 左侧代码详细展开 `producer + WG1`
  - 右侧 callout 明确补一句：`WG2` 是对称的第二个 consumer
  - 口头说明 `WG1/WG2` 通过 named barrier 交替接力

## Suggested Callouts

- `Register split`: producer and consumers do not keep the same register budget.
- `TMA producer path`: buffer reuse is guarded by `empty`, data-ready is published through `full`.
- `Two-consumer structure`: WG1 and WG2 are symmetric consumers; the snippet expands only one side.
- `WGMMA consumer path`: both `QK` and `PV` are explicit warpgroup GEMMs.
- `Named barrier handoff`: WG1/WG2 release each other in steady state.
- `Wait + fence`: async GEMM completion is separated from later softmax / output consumption.

## Why These Chinese Comments Help

- They connect Slide 5's schedule language directly to the code.
- They tell the audience what each primitive is *for*, not just what it is called.
- They make the page readable even for people who do not know TileLang syntax well.

## If You Need To Cut The Snippet Down Further

- Keep all lines containing:
  - `dec_max_nreg / inc_max_nreg`
  - `barrier_wait(...)`
  - `tma_copy(...)`
  - `wgmma_gemm(...)`
  - `barrier_arrive_named(...)`
  - `wait_wgmma(...)`
  - `warpgroup_fence_operand(...)`
  - `barrier_arrive(k_empty / v_empty)`
- Remove:
  - `if n_idx % 2 == 0 else ...` branch detail
  - causal mask detail
  - final output writeback detail

## Supporting References

- Producer path: [\_test_ws_fa3_v2_threadbind_opt.py](/home/ga/TileOPs/_test_ws_fa3_v2_threadbind_opt.py:179)
- WG1 path: [\_test_ws_fa3_v2_threadbind_opt.py](/home/ga/TileOPs/_test_ws_fa3_v2_threadbind_opt.py:234)
- WG2 path: [\_test_ws_fa3_v2_threadbind_opt.py](/home/ga/TileOPs/_test_ws_fa3_v2_threadbind_opt.py:342)
