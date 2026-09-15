........................................................................ [  8%]
........................................................................ [ 17%]
........................................................................ [ 26%]
........................................................................ [ 35%]
........................................................................ [ 44%]
.......................FFFFFF........................................... [ 53%]
........................................................................ [ 62%]
........................................................................ [ 71%]
........................................................................ [ 80%]
........................................................................ [ 89%]
.....................FFFF............................................... [ 98%]
.............                                                            [100%]Benchmark report saved to profile_run.log

=================================== FAILURES ===================================
_______________ test_fp8_lighting_indexer_bench[default-config] ________________

seq_len = 4096, heads = 32, index_dim = 64, seq_len_kv = 8192
clean_logits = True, config = None, tune = False

    @pytest.mark.parametrize(
        "seq_len, heads, index_dim, seq_len_kv, clean_logits, config, tune",
        _FP8_LIGHTING_INDEXER_BENCH_PARAMS,
    )
    def test_fp8_lighting_indexer_bench(seq_len: int, heads: int, index_dim: int, seq_len_kv: int,
                                        clean_logits: bool, config: Optional[dict],
                                        tune: bool) -> None:
        test = Fp8LightingIndexerTest(seq_len, heads, index_dim, seq_len_kv, clean_logits, config)
        bm = Fp8LightingIndexerBenchmark(test)
>       inputs = test.gen_inputs()
                 ^^^^^^^^^^^^^^^^^

benchmarks/ops/bench_fp8_lighting_indexer.py:50: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <tests.ops.test_fp8_lighting_indexer.Fp8LightingIndexerTest object at 0x7f2d97b2a950>
params = None

    def gen_inputs(
            self,
            params=None
    ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
        IndexQ = torch.randn(
            self.batch,
            self.seq_len,
            self.heads,
            self.index_dim,
            device='cuda',
            dtype=torch.bfloat16)
>       IndexK = torch.randn(
            self.batch,
            self.seq_len_kv,
            self.kv_group,
            self.index_dim,
            device='cuda',
            dtype=torch.bfloat16)
E       TypeError: randn(): argument 'size' failed to unpack the object at pos 3 with error "type must be tuple of ints,but got NoneType"

tests/ops/test_fp8_lighting_indexer.py:170: TypeError
__________________ test_fp8_lighting_indexer_bench[mid-shape] __________________

seq_len = 2048, heads = 16, index_dim = 64, seq_len_kv = 4096
clean_logits = True, config = None, tune = False

    @pytest.mark.parametrize(
        "seq_len, heads, index_dim, seq_len_kv, clean_logits, config, tune",
        _FP8_LIGHTING_INDEXER_BENCH_PARAMS,
    )
    def test_fp8_lighting_indexer_bench(seq_len: int, heads: int, index_dim: int, seq_len_kv: int,
                                        clean_logits: bool, config: Optional[dict],
                                        tune: bool) -> None:
        test = Fp8LightingIndexerTest(seq_len, heads, index_dim, seq_len_kv, clean_logits, config)
        bm = Fp8LightingIndexerBenchmark(test)
>       inputs = test.gen_inputs()
                 ^^^^^^^^^^^^^^^^^

benchmarks/ops/bench_fp8_lighting_indexer.py:50: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <tests.ops.test_fp8_lighting_indexer.Fp8LightingIndexerTest object at 0x7f387f6d3950>
params = None

    def gen_inputs(
            self,
            params=None
    ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
>       IndexQ = torch.randn(
            self.batch,
            self.seq_len,
            self.heads,
            self.index_dim,
            device='cuda',
            dtype=torch.bfloat16)
E       torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 16.00 GiB. GPU 0 has a total capacity of 140.06 GiB of which 3.12 GiB is free. Process 2444524 has 136.94 GiB memory in use. Of the allocated memory 128.03 GiB is allocated by PyTorch, and 216.00 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)

tests/ops/test_fp8_lighting_indexer.py:163: OutOfMemoryError
____________________ test_fp8_quant_bench[mainstream-fp16] _____________________

seq_len_kv = 8192, index_dim = 64, in_dtype = torch.float16, tune = True

    @pytest.mark.parametrize("seq_len_kv, index_dim, in_dtype, tune", _FP8_QUANT_BENCH_PARAMS)
    def test_fp8_quant_bench(seq_len_kv: int, index_dim: int, in_dtype: torch.dtype,
                             tune: bool) -> None:
>       test = Fp8QuantTest(seq_len_kv, index_dim, in_dtype)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       TypeError: Fp8QuantTest.__init__() missing 2 required positional arguments: 'index_dim' and 'in_dtype'

benchmarks/ops/bench_fp8_quant.py:34: TypeError
____________________ test_fp8_quant_bench[mainstream-bf16] _____________________

seq_len_kv = 8192, index_dim = 64, in_dtype = torch.bfloat16, tune = True

    @pytest.mark.parametrize("seq_len_kv, index_dim, in_dtype, tune", _FP8_QUANT_BENCH_PARAMS)
    def test_fp8_quant_bench(seq_len_kv: int, index_dim: int, in_dtype: torch.dtype,
                             tune: bool) -> None:
>       test = Fp8QuantTest(seq_len_kv, index_dim, in_dtype)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       TypeError: Fp8QuantTest.__init__() missing 2 required positional arguments: 'index_dim' and 'in_dtype'

benchmarks/ops/bench_fp8_quant.py:34: TypeError
______________________ test_fp8_quant_bench[wider-index] _______________________

seq_len_kv = 4096, index_dim = 128, in_dtype = torch.float32, tune = True

    @pytest.mark.parametrize("seq_len_kv, index_dim, in_dtype, tune", _FP8_QUANT_BENCH_PARAMS)
    def test_fp8_quant_bench(seq_len_kv: int, index_dim: int, in_dtype: torch.dtype,
                             tune: bool) -> None:
>       test = Fp8QuantTest(seq_len_kv, index_dim, in_dtype)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       TypeError: Fp8QuantTest.__init__() missing 2 required positional arguments: 'index_dim' and 'in_dtype'

benchmarks/ops/bench_fp8_quant.py:34: TypeError
_____________________ test_fp8_quant_bench[long-sequence] ______________________

seq_len_kv = 16384, index_dim = 32, in_dtype = torch.float32, tune = True

    @pytest.mark.parametrize("seq_len_kv, index_dim, in_dtype, tune", _FP8_QUANT_BENCH_PARAMS)
    def test_fp8_quant_bench(seq_len_kv: int, index_dim: int, in_dtype: torch.dtype,
                             tune: bool) -> None:
>       test = Fp8QuantTest(seq_len_kv, index_dim, in_dtype)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       TypeError: Fp8QuantTest.__init__() missing 2 required positional arguments: 'index_dim' and 'in_dtype'

benchmarks/ops/bench_fp8_quant.py:34: TypeError
___________________ test_topk_selector_bench[base-topk1024] ____________________

batch = 64, seq_len = 32768, topk = 1024, in_dtype_str = 'float32'
out_dtype_str = 'int32', tune = True

    @pytest.mark.parametrize(
        "batch, seq_len, topk, in_dtype_str, out_dtype_str, tune",
        _TOPK_SELECTOR_BENCH_PARAMS,
    )
    def test_topk_selector_bench(batch: int, seq_len: int, topk: int, in_dtype_str: str,
                                  out_dtype_str: str, tune: bool) -> None:
        in_dtype = str2dtype[in_dtype_str]
        out_dtype = str2dtype[out_dtype_str]
>       test = TopkSelectorTest(batch, seq_len, topk, in_dtype, out_dtype)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       TypeError: TopkSelectorTest.__init__() missing 2 required positional arguments: 'in_dtype' and 'out_dtype'

benchmarks/ops/bench_topk_selector.py:42: TypeError
___________________ test_topk_selector_bench[base-topk2048] ____________________

batch = 64, seq_len = 32768, topk = 2048, in_dtype_str = 'float32'
out_dtype_str = 'int32', tune = True

    @pytest.mark.parametrize(
        "batch, seq_len, topk, in_dtype_str, out_dtype_str, tune",
        _TOPK_SELECTOR_BENCH_PARAMS,
    )
    def test_topk_selector_bench(batch: int, seq_len: int, topk: int, in_dtype_str: str,
                                  out_dtype_str: str, tune: bool) -> None:
        in_dtype = str2dtype[in_dtype_str]
        out_dtype = str2dtype[out_dtype_str]
>       test = TopkSelectorTest(batch, seq_len, topk, in_dtype, out_dtype)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       TypeError: TopkSelectorTest.__init__() missing 2 required positional arguments: 'in_dtype' and 'out_dtype'

benchmarks/ops/bench_topk_selector.py:42: TypeError
________________ test_topk_selector_bench[large-batch-topk1024] ________________

batch = 128, seq_len = 65536, topk = 1024, in_dtype_str = 'float32'
out_dtype_str = 'int32', tune = True

    @pytest.mark.parametrize(
        "batch, seq_len, topk, in_dtype_str, out_dtype_str, tune",
        _TOPK_SELECTOR_BENCH_PARAMS,
    )
    def test_topk_selector_bench(batch: int, seq_len: int, topk: int, in_dtype_str: str,
                                  out_dtype_str: str, tune: bool) -> None:
        in_dtype = str2dtype[in_dtype_str]
        out_dtype = str2dtype[out_dtype_str]
>       test = TopkSelectorTest(batch, seq_len, topk, in_dtype, out_dtype)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       TypeError: TopkSelectorTest.__init__() missing 2 required positional arguments: 'in_dtype' and 'out_dtype'

benchmarks/ops/bench_topk_selector.py:42: TypeError
________________ test_topk_selector_bench[large-batch-topk2048] ________________

batch = 128, seq_len = 65536, topk = 2048, in_dtype_str = 'float32'
out_dtype_str = 'int32', tune = True

    @pytest.mark.parametrize(
        "batch, seq_len, topk, in_dtype_str, out_dtype_str, tune",
        _TOPK_SELECTOR_BENCH_PARAMS,
    )
    def test_topk_selector_bench(batch: int, seq_len: int, topk: int, in_dtype_str: str,
                                  out_dtype_str: str, tune: bool) -> None:
        in_dtype = str2dtype[in_dtype_str]
        out_dtype = str2dtype[out_dtype_str]
>       test = TopkSelectorTest(batch, seq_len, topk, in_dtype, out_dtype)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       TypeError: TopkSelectorTest.__init__() missing 2 required positional arguments: 'in_dtype' and 'out_dtype'

benchmarks/ops/bench_topk_selector.py:42: TypeError
=============================== warnings summary ===============================
benchmarks/ops/bench_activation.py: 93 warnings
benchmarks/ops/bench_ada_layer_norm.py: 16 warnings
benchmarks/ops/bench_argreduce.py: 12 warnings
benchmarks/ops/bench_batch_norm.py: 12 warnings
benchmarks/ops/bench_binary_arith.py: 65 warnings
benchmarks/ops/bench_binary_elementwise.py: 107 warnings
benchmarks/ops/bench_binary_strategy.py: 18 warnings
benchmarks/ops/bench_cumulative.py: 12 warnings
benchmarks/ops/bench_deepseek_dsa_decode.py: 4 warnings
benchmarks/ops/bench_deepseek_mla_decode.py: 4 warnings
benchmarks/ops/bench_deepseek_nsa_cmp_fwd.py: 4 warnings
benchmarks/ops/bench_deepseek_nsa_fwd.py: 6 warnings
benchmarks/ops/bench_deepseek_nsa_topk.py: 6 warnings
benchmarks/ops/bench_dropout.py: 9 warnings
benchmarks/ops/bench_elementwise_fp8.py: 24 warnings
benchmarks/ops/bench_engram_bwd.py: 4 warnings
benchmarks/ops/bench_engram_decode.py: 6 warnings
benchmarks/ops/bench_engram_fwd.py: 8 warnings
benchmarks/ops/bench_fft.py: 10 warnings
benchmarks/ops/bench_fft_lut.py: 21 warnings
benchmarks/ops/bench_fused_add_layer_norm.py: 8 warnings
benchmarks/ops/bench_fused_add_rmsnorm.py: 8 warnings
benchmarks/ops/bench_gated_deltanet_decode.py: 13 warnings
benchmarks/ops/bench_gated_deltanet_vs_fla.py: 64 warnings
benchmarks/ops/bench_gemm.py: 6 warnings
benchmarks/ops/bench_gla.py: 24 warnings
benchmarks/ops/bench_gla_decode.py: 16 warnings
benchmarks/ops/bench_gqa.py: 6 warnings
benchmarks/ops/bench_gqa_decode.py: 6 warnings
benchmarks/ops/bench_gqa_decode_paged.py: 8 warnings
benchmarks/ops/bench_gqa_sliding_window_fwd.py: 5 warnings
benchmarks/ops/bench_gqa_sliding_window_varlen_fwd.py: 5 warnings
benchmarks/ops/bench_group_norm.py: 8 warnings
benchmarks/ops/bench_grouped_gemm.py: 16 warnings
benchmarks/ops/bench_independent_elementwise.py: 132 warnings
benchmarks/ops/bench_instance_norm.py: 8 warnings
benchmarks/ops/bench_layer_norm.py: 8 warnings
benchmarks/ops/bench_logical_reduce.py: 30 warnings
benchmarks/ops/bench_mean_pooling.py: 8 warnings
benchmarks/ops/bench_mha.py: 6 warnings
benchmarks/ops/bench_mha_decode.py: 6 warnings
benchmarks/ops/bench_mha_decode_paged.py: 8 warnings
benchmarks/ops/bench_mhc_post.py: 6 warnings
benchmarks/ops/bench_mhc_pre.py: 6 warnings
benchmarks/ops/bench_moe_permute_align.py: 10 warnings
benchmarks/ops/bench_reduce.py: 20 warnings
benchmarks/ops/bench_rms_norm.py: 8 warnings
benchmarks/ops/bench_rope.py: 9 warnings
benchmarks/ops/bench_softmax.py: 24 warnings
benchmarks/ops/bench_unary_elementwise.py: 21 warnings
benchmarks/ops/bench_unary_strategy.py: 27 warnings
benchmarks/ops/bench_vector_norm.py: 24 warnings
  /home/ci-runner/workdir/_tool/tileops_benchmarks_venv_db4a9af2f48857c5/lib/python3.11/site-packages/torch/profiler/profiler.py:509: UserWarning: Profiler won't be using warmup, this can skew profiler results
    warn("Profiler won't be using warmup, this can skew profiler results")

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ============================
FAILED benchmarks/ops/bench_fp8_lighting_indexer.py::test_fp8_lighting_indexer_bench[default-config] - TypeError: randn(): argument 'size' failed to unpack the object at pos 3 with error "type must be tuple of ints,but got NoneType"
FAILED benchmarks/ops/bench_fp8_lighting_indexer.py::test_fp8_lighting_indexer_bench[mid-shape] - torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 16.00 GiB. GPU 0 has a total capacity of 140.06 GiB of which 3.12 GiB is free. Process 2444524 has 136.94 GiB memory in use. Of the allocated memory 128.03 GiB is allocated by PyTorch, and 216.00 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)
FAILED benchmarks/ops/bench_fp8_quant.py::test_fp8_quant_bench[mainstream-fp16] - TypeError: Fp8QuantTest.__init__() missing 2 required positional arguments: 'index_dim' and 'in_dtype'
FAILED benchmarks/ops/bench_fp8_quant.py::test_fp8_quant_bench[mainstream-bf16] - TypeError: Fp8QuantTest.__init__() missing 2 required positional arguments: 'index_dim' and 'in_dtype'
FAILED benchmarks/ops/bench_fp8_quant.py::test_fp8_quant_bench[wider-index] - TypeError: Fp8QuantTest.__init__() missing 2 required positional arguments: 'index_dim' and 'in_dtype'
FAILED benchmarks/ops/bench_fp8_quant.py::test_fp8_quant_bench[long-sequence] - TypeError: Fp8QuantTest.__init__() missing 2 required positional arguments: 'index_dim' and 'in_dtype'
FAILED benchmarks/ops/bench_topk_selector.py::test_topk_selector_bench[base-topk1024] - TypeError: TopkSelectorTest.__init__() missing 2 required positional arguments: 'in_dtype' and 'out_dtype'
FAILED benchmarks/ops/bench_topk_selector.py::test_topk_selector_bench[base-topk2048] - TypeError: TopkSelectorTest.__init__() missing 2 required positional arguments: 'in_dtype' and 'out_dtype'
FAILED benchmarks/ops/bench_topk_selector.py::test_topk_selector_bench[large-batch-topk1024] - TypeError: TopkSelectorTest.__init__() missing 2 required positional arguments: 'in_dtype' and 'out_dtype'
FAILED benchmarks/ops/bench_topk_selector.py::test_topk_selector_bench[large-batch-topk2048] - TypeError: TopkSelectorTest.__init__() missing 2 required positional arguments: 'in_dtype' and 'out_dtype'
10 failed, 795 passed, 995 warnings in 3414.81s (0:56:54)

===== profile_run.log summary =====
# TileOPs Benchmark Report
Generated: 2026-03-18 20:30:31

## Environment

- **Torch version**: 2.9.1+cu128
- **CUDA version (torch)**: 12.8
- **GPU model**: NVIDIA H200
- **Driver version**: 575.57.08

## r2_small_tensor_unary

### tileops

| n_total | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| 4096 | torch.float16 | 0.00 | 0.00 | 0.01 |

### baseline

| n_total | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| 4096 | torch.float16 | 0.00 | 0.00 | 0.01 |

## r3_jit_cost

### relu_jit

| n_total | cold_ms | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| 1000 | 20.98 | 0.00 | 0.00 | 0.00 |
| 2000 | 20.48 | 0.00 | 0.00 | 0.00 |
| 4000 | 20.7 | 0.00 | 0.00 | 0.01 |
| 8000 | 20.51 | 0.00 | 0.00 | 0.02 |
| 16000 | 20.67 | 0.00 | 0.01 | 0.03 |
| 32000 | 21.14 | 0.00 | 0.02 | 0.06 |
| 64000 | 20.69 | 0.00 | 0.03 | 0.12 |
| 128000 | 20.27 | 0.00 | 0.06 | 0.23 |
| 256000 | 21.44 | 0.00 | 0.11 | 0.45 |
| 512000 | 20.71 | 0.00 | 0.19 | 0.77 |

## r4_strategy_unary

### relu_direct

| n_total | size_label | dtype | strategy | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 4096 | 4K | torch.float16 | direct | 0.00 | 0.00 | 0.01 |
| 4096 | 4K | torch.bfloat16 | direct | 0.00 | 0.00 | 0.01 |
| 4096 | 4K | torch.float32 | direct | 0.00 | 0.00 | 0.02 |
| 4194304 | 4M | torch.float16 | direct | 0.01 | 0.29 | 1.15 |
| 4194304 | 4M | torch.bfloat16 | direct | 0.01 | 0.29 | 1.15 |
| 4194304 | 4M | torch.float32 | direct | 0.02 | 0.26 | 2.09 |
| 16777216 | 16M | torch.float16 | direct | 0.05 | 0.32 | 1.29 |
| 16777216 | 16M | torch.bfloat16 | direct | 0.05 | 0.32 | 1.29 |
| 16777216 | 16M | torch.float32 | direct | 0.06 | 0.29 | 2.34 |

### relu_explicit_parallel

| n_total | size_label | dtype | strategy | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 4096 | 4K | torch.float16 | explicit_parallel | 0.00 | 0.00 | 0.01 |
| 4096 | 4K | torch.bfloat16 | explicit_parallel | 0.00 | 0.00 | 0.01 |
| 4096 | 4K | torch.float32 | explicit_parallel | 0.00 | 0.00 | 0.02 |
| 4194304 | 4M | torch.float16 | explicit_parallel | 0.02 | 0.21 | 0.86 |
| 4194304 | 4M | torch.bfloat16 | explicit_parallel | 0.02 | 0.21 | 0.86 |
| 4194304 | 4M | torch.float32 | explicit_parallel | 0.01 | 0.38 | 3.03 |
| 16777216 | 16M | torch.float16 | explicit_parallel | 0.07 | 0.25 | 0.98 |
| 16777216 | 16M | torch.bfloat16 | explicit_parallel | 0.07 | 0.25 | 0.98 |
| 16777216 | 16M | torch.float32 | explicit_parallel | 0.03 | 0.48 | 3.85 |

### relu_register_copy

| n_total | size_label | dtype | strategy | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 4096 | 4K | torch.float16 | register_copy | 0.00 | 0.00 | 0.01 |
| 4096 | 4K | torch.bfloat16 | register_copy | 0.00 | 0.00 | 0.01 |
| 4096 | 4K | torch.float32 | register_copy | 0.00 | 0.00 | 0.02 |
| 4194304 | 4M | torch.float16 | register_copy | 0.01 | 0.65 | 2.61 |
| 4194304 | 4M | torch.bfloat16 | register_copy | 0.01 | 0.65 | 2.61 |
| 4194304 | 4M | torch.float32 | register_copy | 0.01 | 0.39 | 3.12 |
| 16777216 | 16M | torch.float16 | register_copy | 0.02 | 0.91 | 3.63 |
| 16777216 | 16M | torch.bfloat16 | register_copy | 0.02 | 0.91 | 3.63 |
| 16777216 | 16M | torch.float32 | register_copy | 0.03 | 0.49 | 3.91 |

## r4_strategy_gelu

### gelu_direct

| n_total | size_label | dtype | strategy | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 4096 | 4K | torch.float16 | direct | 0.00 | 0.00 | 0.01 |
| 4096 | 4K | torch.bfloat16 | direct | 0.00 | 0.00 | 0.01 |
| 4096 | 4K | torch.float32 | direct | 0.00 | 0.00 | 0.02 |
| 4194304 | 4M | torch.float16 | direct | 0.02 | 0.26 | 1.05 |
| 4194304 | 4M | torch.bfloat16 | direct | 0.02 | 0.26 | 1.05 |
| 4194304 | 4M | torch.float32 | direct | 0.02 | 0.25 | 1.96 |
| 16777216 | 16M | torch.float16 | direct | 0.06 | 0.29 | 1.17 |
| 16777216 | 16M | torch.bfloat16 | direct | 0.06 | 0.29 | 1.16 |
| 16777216 | 16M | torch.float32 | direct | 0.06 | 0.27 | 2.18 |

### gelu_explicit_parallel

| n_total | size_label | dtype | strategy | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 4096 | 4K | torch.float16 | explicit_parallel | 0.00 | 0.00 | 0.01 |
| 4096 | 4K | torch.bfloat16 | explicit_parallel | 0.00 | 0.00 | 0.01 |
| 4096 | 4K | torch.float32 | explicit_parallel | 0.00 | 0.00 | 0.02 |
| 4194304 | 4M | torch.float16 | explicit_parallel | 0.01 | 0.46 | 1.82 |
| 4194304 | 4M | torch.bfloat16 | explicit_parallel | 0.01 | 0.45 | 1.81 |
| 4194304 | 4M | torch.float32 | explicit_parallel | 0.01 | 0.38 | 3.03 |
| 16777216 | 16M | torch.float16 | explicit_parallel | 0.03 | 0.57 | 2.26 |
| 16777216 | 16M | torch.bfloat16 | explicit_parallel | 0.03 | 0.56 | 2.24 |
| 16777216 | 16M | torch.float32 | explicit_parallel | 0.04 | 0.46 | 3.68 |

### gelu_register_copy

| n_total | size_label | dtype | strategy | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 4096 | 4K | torch.float16 | register_copy | 0.00 | 0.00 | 0.01 |
| 4096 | 4K | torch.bfloat16 | register_copy | 0.00 | 0.00 | 0.01 |
| 4096 | 4K | torch.float32 | register_copy | 0.00 | 0.00 | 0.02 |
| 4194304 | 4M | torch.float16 | register_copy | 0.01 | 0.47 | 1.90 |
| 4194304 | 4M | torch.bfloat16 | register_copy | 0.01 | 0.46 | 1.86 |
| 4194304 | 4M | torch.float32 | register_copy | 0.01 | 0.39 | 3.09 |
| 16777216 | 16M | torch.float16 | register_copy | 0.03 | 0.60 | 2.40 |
| 16777216 | 16M | torch.bfloat16 | register_copy | 0.03 | 0.58 | 2.32 |
| 16777216 | 16M | torch.float32 | register_copy | 0.04 | 0.47 | 3.78 |

## r5_boundary

### relu_aligned

| n_total | align_label | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| 2048000 | aligned | 0.01 | 0.17 | 0.67 |

### relu_unaligned_plus_1

| n_total | align_label | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| 2048001 | unaligned_plus_1 | 0.01 | 0.17 | 0.67 |

### relu_unaligned_plus_127

| n_total | align_label | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| 2048127 | unaligned_plus_127 | 0.01 | 0.17 | 0.67 |

## r6_threads

### relu_t128

| n_total | size_label | op_name | threads | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 4096 | 4K | relu | 128 | 0.00 | 0.00 | 0.01 |
| 4194304 | 4M | relu | 128 | 0.02 | 0.21 | 0.85 |
| 16777216 | 16M | relu | 128 | 0.07 | 0.26 | 1.02 |

### relu_t256

| n_total | size_label | op_name | threads | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 4096 | 4K | relu | 256 | 0.00 | 0.00 | 0.01 |
| 4194304 | 4M | relu | 256 | 0.02 | 0.21 | 0.86 |
| 16777216 | 16M | relu | 256 | 0.07 | 0.25 | 0.98 |

### erf_t128

| n_total | size_label | op_name | threads | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 4096 | 4K | erf | 128 | 0.00 | 0.00 | 0.01 |
| 4194304 | 4M | erf | 128 | 0.01 | 0.48 | 1.93 |
| 16777216 | 16M | erf | 128 | 0.03 | 0.60 | 2.40 |

### erf_t256

| n_total | size_label | op_name | threads | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 4096 | 4K | erf | 256 | 0.00 | 0.00 | 0.01 |
| 4194304 | 4M | erf | 256 | 0.01 | 0.48 | 1.90 |
| 16777216 | 16M | erf | 256 | 0.03 | 0.60 | 2.39 |

### mish_t128

| n_total | size_label | op_name | threads | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 4096 | 4K | mish | 128 | 0.00 | 0.00 | 0.01 |
| 4194304 | 4M | mish | 128 | 0.01 | 0.36 | 1.44 |
| 16777216 | 16M | mish | 128 | 0.04 | 0.42 | 1.68 |

### mish_t256

| n_total | size_label | op_name | threads | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 4096 | 4K | mish | 256 | 0.00 | 0.00 | 0.01 |
| 4194304 | 4M | mish | 256 | 0.01 | 0.35 | 1.41 |
| 16777216 | 16M | mish | 256 | 0.04 | 0.42 | 1.67 |

## r7_dtype_npt

### relu_fp32_npt4

| dtype_label | num_per_thread | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| fp32 | 4 | 0.00 | 0.22 | 1.74 |

### relu_fp32_npt8

| dtype_label | num_per_thread | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| fp32 | 8 | 0.00 | 0.21 | 1.72 |

### relu_fp16_npt4

| dtype_label | num_per_thread | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| fp16 | 4 | 0.00 | 0.28 | 1.13 |

### relu_fp16_npt8

| dtype_label | num_per_thread | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| fp16 | 8 | 0.00 | 0.22 | 0.88 |

## relu

### tileops

| n_total | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| 4194304 | torch.float16 | 0.01 | 0.65 | 2.61 |
| 4194304 | torch.bfloat16 | 0.01 | 0.65 | 2.61 |
| 4194304 | torch.float32 | 0.01 | 0.39 | 3.12 |

### baseline

| n_total | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| 4194304 | torch.float16 | 0.01 | 0.63 | 2.51 |
| 4194304 | torch.bfloat16 | 0.01 | 0.64 | 2.55 |
| 4194304 | torch.float32 | 0.01 | 0.39 | 3.11 |

## ada_layer_norm

### tileops

| m | n | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| 1024 | 4096 | torch.float16 | 0.02 | 1.40 | 2.24 |
| 4096 | 4096 | torch.bfloat16 | 0.05 | 1.64 | 2.62 |
| 1024 | 3000 | torch.float16 | 0.04 | 0.38 | 0.61 |
| 1025 | 4096 | torch.float16 | 0.01 | 1.42 | 2.28 |

### baseline

| m | n | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| 1024 | 4096 | torch.float16 | 0.02 | 0.85 | 1.36 |
| 4096 | 4096 | torch.bfloat16 | 0.08 | 1.05 | 1.67 |
| 1024 | 3000 | torch.float16 | 0.02 | 0.75 | 1.20 |
| 1025 | 4096 | torch.float16 | 0.03 | 0.83 | 1.33 |

## ada_layer_norm_zero

### tileops

| m | n | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| 1024 | 4096 | torch.float16 | 0.02 | 1.29 | 2.15 |
| 4096 | 4096 | torch.bfloat16 | 0.06 | 1.57 | 2.62 |
| 1024 | 3000 | torch.float16 | 0.05 | 0.35 | 0.58 |
| 1025 | 4096 | torch.float16 | 0.02 | 1.32 | 2.20 |

### baseline

| m | n | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| 1024 | 4096 | torch.float16 | 0.03 | 0.80 | 1.34 |
| 4096 | 4096 | torch.bfloat16 | 0.11 | 0.96 | 1.59 |
| 1024 | 3000 | torch.float16 | 0.03 | 0.72 | 1.20 |
| 1025 | 4096 | torch.float16 | 0.03 | 0.80 | 1.33 |

## argreduce

### tileops

| m | n | dtype | op_kind | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 1024 | 4096 | torch.float16 | argmax | 3.06 | 0.00 | 0.00 |
| 1024 | 4096 | torch.bfloat16 | argmax | 3.08 | 0.00 | 0.00 |
| 4096 | 4096 | torch.float16 | argmax | 10.69 | 0.00 | 0.00 |
| 1024 | 4096 | torch.float16 | argmin | 3.46 | 0.00 | 0.00 |
| 1024 | 4096 | torch.bfloat16 | argmin | 3.46 | 0.00 | 0.00 |
| 4096 | 4096 | torch.float16 | argmin | 12.11 | 0.00 | 0.00 |

### baseline

| m | n | dtype | op_kind | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 1024 | 4096 | torch.float16 | argmax | 0.02 | 0.19 | 0.37 |
| 1024 | 4096 | torch.bfloat16 | argmax | 0.02 | 0.19 | 0.37 |
| 4096 | 4096 | torch.float16 | argmax | 0.03 | 0.59 | 1.18 |
| 1024 | 4096 | torch.float16 | argmin | 0.02 | 0.19 | 0.37 |
| 1024 | 4096 | torch.bfloat16 | argmin | 0.02 | 0.19 | 0.37 |
| 4096 | 4096 | torch.float16 | argmin | 0.03 | 0.59 | 1.18 |

## batch_norm_fwd

### tileops

| N | C | spatial | dtype | training | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 32 | 64 | () | torch.float16 | True | 0.01 | 0.00 | 0.00 |
| 8 | 64 | (32, 32) | torch.float16 | True | 0.01 | 0.43 | 0.17 |
| 4 | 128 | (32, 32) | torch.float16 | True | 0.01 | 0.43 | 0.17 |
| 4 | 256 | (28, 28) | torch.float16 | True | 0.02 | 0.50 | 0.20 |
| 4 | 128 | (1024, 1024) | torch.float16 | True | 3.94 | 1.36 | 0.55 |
| 4 | 256 | (1024, 1024) | torch.float16 | True | 7.33 | 1.46 | 0.59 |

### torch_cudnn

| N | C | spatial | dtype | training | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 32 | 64 | () | torch.float16 | True | 0.02 | 0.00 | 0.00 |
| 8 | 64 | (32, 32) | torch.float16 | True | 0.01 | 0.37 | 0.15 |
| 4 | 128 | (32, 32) | torch.float16 | True | 0.01 | 0.39 | 0.16 |
| 4 | 256 | (28, 28) | torch.float16 | True | 0.01 | 0.57 | 0.23 |
| 4 | 128 | (1024, 1024) | torch.float16 | True | 4.12 | 1.30 | 0.52 |
| 4 | 256 | (1024, 1024) | torch.float16 | True | 7.28 | 1.47 | 0.59 |

## batch_norm_bwd

### tileops

| N | C | spatial | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 32 | 64 | () | torch.float16 | 0.01 | 0.00 | 0.00 |
| 8 | 64 | (32, 32) | torch.float16 | 0.02 | 0.26 | 0.19 |
| 4 | 128 | (32, 32) | torch.float16 | 0.02 | 0.26 | 0.20 |
| 4 | 256 | (28, 28) | torch.float16 | 0.02 | 0.32 | 0.24 |
| 4 | 128 | (1024, 1024) | torch.float16 | 6.22 | 0.69 | 0.52 |
| 4 | 256 | (1024, 1024) | torch.float16 | 11.27 | 0.76 | 0.57 |

### torch_autograd

| N | C | spatial | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 32 | 64 | () | torch.float16 | 0.02 | 0.00 | 0.00 |
| 8 | 64 | (32, 32) | torch.float16 | 0.03 | 0.16 | 0.12 |
| 4 | 128 | (32, 32) | torch.float16 | 0.02 | 0.19 | 0.14 |
| 4 | 256 | (28, 28) | torch.float16 | 0.02 | 0.27 | 0.20 |
| 4 | 128 | (1024, 1024) | torch.float16 | 12.07 | 0.36 | 0.27 |
| 4 | 256 | (1024, 1024) | torch.float16 | 18.17 | 0.47 | 0.35 |

## r1_vectorization

### add_same_shape_1d

| pattern_name | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| same_shape_1d | 1000000 | 0.00 | 0.24 | 1.47 |

### baseline_same_shape_1d

| pattern_name | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| same_shape_1d | 1000000 | 0.00 | 0.25 | 1.50 |

### add_bias_add_2d

| pattern_name | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| bias_add_2d | 1000000 | 0.00 | 0.27 | 1.08 |

### baseline_bias_add_2d

| pattern_name | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| bias_add_2d | 1000000 | 0.01 | 0.17 | 0.67 |

### add_interleaved_3d

| pattern_name | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| interleaved_3d | 1048576 | 0.00 | 0.46 | 0.93 |

### baseline_interleaved_3d

| pattern_name | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| interleaved_3d | 1048576 | 0.01 | 0.19 | 0.38 |

## r2_small_tensor_binary

### add_same_shape

| pattern_name | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| same_shape | 4096 | 0.00 | 0.00 | 0.01 |

### baseline_same_shape

| pattern_name | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| same_shape | 4096 | 0.00 | 0.00 | 0.01 |

### add_broadcast_3d

| pattern_name | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| broadcast_3d | 4096 | 0.00 | 0.00 | 0.01 |

### baseline_broadcast_3d

| pattern_name | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| broadcast_3d | 4096 | 0.00 | 0.00 | 0.00 |

## r4_strategy_binary

### add_direct_same_shape

| size_label | pattern_name | strategy | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 4K | same_shape | direct | 4096 | 0.00 | 0.00 | 0.01 |
| 4K | same_shape | direct | 4096 | 0.00 | 0.00 | 0.01 |
| 4K | same_shape | direct | 4096 | 0.00 | 0.00 | 0.03 |
| 1M | same_shape | direct | 1048576 | 0.01 | 0.18 | 1.10 |
| 1M | same_shape | direct | 1048576 | 0.01 | 0.18 | 1.10 |
| 1M | same_shape | direct | 1048576 | 0.01 | 0.16 | 1.96 |
| 16M | same_shape | direct | 16777216 | 0.06 | 0.29 | 1.75 |
| 16M | same_shape | direct | 16777216 | 0.06 | 0.29 | 1.75 |
| 16M | same_shape | direct | 16777216 | 0.07 | 0.25 | 3.02 |

### add_direct_bias_add_2d

| size_label | pattern_name | strategy | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 4K | bias_add_2d | direct | 4096 | 0.00 | 0.00 | 0.01 |
| 4K | bias_add_2d | direct | 4096 | 0.00 | 0.00 | 0.01 |
| 4K | bias_add_2d | direct | 4096 | 0.00 | 0.00 | 0.02 |
| 1M | bias_add_2d | direct | 1048576 | 0.01 | 0.20 | 0.79 |
| 1M | bias_add_2d | direct | 1048576 | 0.01 | 0.20 | 0.80 |
| 1M | bias_add_2d | direct | 1048576 | 0.01 | 0.19 | 1.50 |
| 16M | bias_add_2d | direct | 16777216 | 0.05 | 0.32 | 1.27 |
| 16M | bias_add_2d | direct | 16777216 | 0.05 | 0.32 | 1.27 |
| 16M | bias_add_2d | direct | 16777216 | 0.06 | 0.29 | 2.30 |

### add_direct_interleaved_3d

| size_label | pattern_name | strategy | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 4K | interleaved_3d | direct | 4096 | 0.00 | 0.00 | 0.01 |
| 4K | interleaved_3d | direct | 4096 | 0.00 | 0.00 | 0.01 |
| 4K | interleaved_3d | direct | 4096 | 0.00 | 0.00 | 0.01 |
| 1M | interleaved_3d | direct | 1048576 | 0.00 | 0.23 | 0.47 |
| 1M | interleaved_3d | direct | 1048576 | 0.00 | 0.23 | 0.47 |
| 1M | interleaved_3d | direct | 1048576 | 0.00 | 0.22 | 0.89 |
| 16M | interleaved_3d | direct | 16777216 | 0.04 | 0.40 | 0.80 |
| 16M | interleaved_3d | direct | 16777216 | 0.04 | 0.40 | 0.80 |
| 16M | interleaved_3d | direct | 16777216 | 0.04 | 0.39 | 1.57 |

### add_explicit_parallel_same_shape

| size_label | pattern_name | strategy | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 4K | same_shape | explicit_parallel | 4096 | 0.00 | 0.00 | 0.01 |
| 4K | same_shape | explicit_parallel | 4096 | 0.00 | 0.00 | 0.01 |
| 4K | same_shape | explicit_parallel | 4096 | 0.00 | 0.00 | 0.03 |
| 1M | same_shape | explicit_parallel | 1048576 | 0.00 | 0.27 | 1.60 |
| 1M | same_shape | explicit_parallel | 1048576 | 0.00 | 0.27 | 1.59 |
| 1M | same_shape | explicit_parallel | 1048576 | 0.01 | 0.19 | 2.24 |
| 16M | same_shape | explicit_parallel | 16777216 | 0.03 | 0.62 | 3.71 |
| 16M | same_shape | explicit_parallel | 16777216 | 0.03 | 0.62 | 3.71 |
| 16M | same_shape | explicit_parallel | 16777216 | 0.05 | 0.33 | 4.01 |

### add_explicit_parallel_bias_add_2d

| size_label | pattern_name | strategy | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 4K | bias_add_2d | explicit_parallel | 4096 | 0.00 | 0.00 | 0.01 |
| 4K | bias_add_2d | explicit_parallel | 4096 | 0.00 | 0.00 | 0.01 |
| 4K | bias_add_2d | explicit_parallel | 4096 | 0.00 | 0.00 | 0.02 |
| 1M | bias_add_2d | explicit_parallel | 1048576 | 0.00 | 0.32 | 1.26 |
| 1M | bias_add_2d | explicit_parallel | 1048576 | 0.00 | 0.32 | 1.26 |
| 1M | bias_add_2d | explicit_parallel | 1048576 | 0.00 | 0.24 | 1.90 |
| 16M | bias_add_2d | explicit_parallel | 16777216 | 0.02 | 0.91 | 3.63 |
| 16M | bias_add_2d | explicit_parallel | 16777216 | 0.02 | 0.91 | 3.63 |
| 16M | bias_add_2d | explicit_parallel | 16777216 | 0.03 | 0.49 | 3.91 |

### add_explicit_parallel_interleaved_3d

| size_label | pattern_name | strategy | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 4K | interleaved_3d | explicit_parallel | 4096 | 0.00 | 0.00 | 0.01 |
| 4K | interleaved_3d | explicit_parallel | 4096 | 0.00 | 0.00 | 0.01 |
| 4K | interleaved_3d | explicit_parallel | 4096 | 0.00 | 0.00 | 0.01 |
| 1M | interleaved_3d | explicit_parallel | 1048576 | 0.00 | 0.47 | 0.94 |
| 1M | interleaved_3d | explicit_parallel | 1048576 | 0.00 | 0.47 | 0.95 |
| 1M | interleaved_3d | explicit_parallel | 1048576 | 0.00 | 0.38 | 1.54 |
| 16M | interleaved_3d | explicit_parallel | 16777216 | 0.01 | 1.71 | 3.43 |
| 16M | interleaved_3d | explicit_parallel | 16777216 | 0.01 | 1.71 | 3.43 |
| 16M | interleaved_3d | explicit_parallel | 16777216 | 0.02 | 0.95 | 3.82 |

## r4_where

### tileops_where

| n_total | size_label | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| 4096 | 4K | 0.00 | 0.00 | 0.01 |
| 1048576 | 1M | 0.00 | 0.24 | 1.68 |
| 16777216 | 16M | 0.03 | 0.53 | 3.71 |

### baseline_where

| n_total | size_label | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| 4096 | 4K | 0.00 | 0.00 | 0.01 |
| 1048576 | 1M | 0.00 | 0.24 | 1.65 |
| 16777216 | 16M | 0.03 | 0.53 | 3.74 |

## add

### tileops

| n_total | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| 4194304 | torch.float16 | 0.01 | 0.47 | 2.83 |
| 4194304 | torch.bfloat16 | 0.01 | 0.47 | 2.83 |
| 4194304 | torch.float32 | 0.02 | 0.27 | 3.29 |

### baseline

| n_total | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| 4194304 | torch.float16 | 0.01 | 0.46 | 2.79 |
| 4194304 | torch.bfloat16 | 0.01 | 0.46 | 2.79 |
| 4194304 | torch.float32 | 0.02 | 0.28 | 3.30 |

## sub

### tileops

| op_name | dtype | output_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| sub | torch.float16 | torch.float16 | 0.01 | 0.47 | 2.82 |
| sub | torch.float16 | torch.float16 | 0.02 | 0.57 | 3.43 |
| sub | torch.float16 | torch.float16 | 0.03 | 0.64 | 3.83 |

### baseline

| op_name | dtype | output_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| sub | torch.float16 | torch.float16 | 0.01 | 0.46 | 2.79 |
| sub | torch.float16 | torch.float16 | 0.02 | 0.57 | 3.41 |
| sub | torch.float16 | torch.float16 | 0.03 | 0.64 | 3.85 |

## mul

### tileops

| op_name | dtype | output_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| mul | torch.float16 | torch.float16 | 0.01 | 0.47 | 2.83 |
| mul | torch.float16 | torch.float16 | 0.02 | 0.57 | 3.43 |
| mul | torch.float16 | torch.float16 | 0.03 | 0.64 | 3.83 |

### baseline

| op_name | dtype | output_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| mul | torch.float16 | torch.float16 | 0.01 | 0.46 | 2.79 |
| mul | torch.float16 | torch.float16 | 0.02 | 0.57 | 3.41 |
| mul | torch.float16 | torch.float16 | 0.03 | 0.64 | 3.85 |

## div

### tileops

| op_name | dtype | output_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| div | torch.float16 | torch.float16 | 0.01 | 0.45 | 2.72 |
| div | torch.float16 | torch.float16 | 0.02 | 0.57 | 3.44 |
| div | torch.float16 | torch.float16 | 0.03 | 0.63 | 3.77 |

### baseline

| op_name | dtype | output_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| div | torch.float16 | torch.float16 | 0.01 | 0.44 | 2.66 |
| div | torch.float16 | torch.float16 | 0.02 | 0.57 | 3.40 |
| div | torch.float16 | torch.float16 | 0.03 | 0.62 | 3.74 |

## remainder

### tileops

| op_name | dtype | output_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| remainder | torch.float16 | torch.float16 | 0.01 | 0.44 | 2.67 |
| remainder | torch.float16 | torch.float16 | 0.02 | 0.57 | 3.42 |

### baseline

| op_name | dtype | output_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| remainder | torch.float16 | torch.float16 | 0.01 | 0.40 | 2.43 |
| remainder | torch.float16 | torch.float16 | 0.02 | 0.51 | 3.05 |

## pow

### tileops

| op_name | dtype | output_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| pow | torch.float16 | torch.float16 | 0.02 | 0.24 | 1.45 |
| pow | torch.float16 | torch.float16 | 0.04 | 0.28 | 1.67 |

### baseline

| op_name | dtype | output_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| pow | torch.float16 | torch.float16 | 0.02 | 0.24 | 1.45 |
| pow | torch.float16 | torch.float16 | 0.04 | 0.28 | 1.65 |

## floor_divide

### tileops

| op_name | dtype | output_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| floor_divide | torch.float16 | torch.float16 | 0.01 | 0.45 | 2.67 |
| floor_divide | torch.float16 | torch.float16 | 0.02 | 0.57 | 3.42 |

### baseline

| op_name | dtype | output_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| floor_divide | torch.float16 | torch.float16 | 0.02 | 0.18 | 1.10 |
| floor_divide | torch.float16 | torch.float16 | 0.05 | 0.21 | 1.24 |

## lerp

### tileops

| op_name | dtype | output_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| lerp | torch.float16 | torch.float16 | 0.01 | 0.47 | 2.82 |
| lerp | torch.float16 | torch.float16 | 0.02 | 0.57 | 3.43 |

### baseline

| op_name | dtype | output_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| lerp | torch.float16 | torch.float16 | 0.01 | 0.47 | 2.82 |
| lerp | torch.float16 | torch.float16 | 0.02 | 0.57 | 3.43 |

## maximum

### tileops

| op_name | dtype | output_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| maximum | torch.float16 | torch.float16 | 0.01 | 0.46 | 2.77 |
| maximum | torch.float16 | torch.float16 | 0.02 | 0.56 | 3.39 |
| maximum | torch.float16 | torch.float16 | 0.03 | 0.64 | 3.81 |

### baseline

| op_name | dtype | output_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| maximum | torch.float16 | torch.float16 | 0.01 | 0.46 | 2.75 |
| maximum | torch.float16 | torch.float16 | 0.02 | 0.56 | 3.39 |
| maximum | torch.float16 | torch.float16 | 0.03 | 0.63 | 3.81 |

## minimum

### tileops

| op_name | dtype | output_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| minimum | torch.float16 | torch.float16 | 0.01 | 0.46 | 2.77 |
| minimum | torch.float16 | torch.float16 | 0.02 | 0.56 | 3.39 |
| minimum | torch.float16 | torch.float16 | 0.03 | 0.64 | 3.81 |

### baseline

| op_name | dtype | output_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| minimum | torch.float16 | torch.float16 | 0.01 | 0.46 | 2.76 |
| minimum | torch.float16 | torch.float16 | 0.02 | 0.56 | 3.39 |
| minimum | torch.float16 | torch.float16 | 0.03 | 0.63 | 3.81 |

## cmp_eq

### tileops

| op_name | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| eq | torch.float16 | 0.02 | 0.22 | 1.10 |
| eq | torch.float16 | 0.04 | 0.26 | 1.32 |

### baseline

| op_name | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| eq | torch.float16 | 0.01 | 0.52 | 2.58 |
| eq | torch.float16 | 0.02 | 0.64 | 3.22 |

## cmp_ne

### tileops

| op_name | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| ne | torch.float16 | 0.02 | 0.22 | 1.11 |

### baseline

| op_name | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| ne | torch.float16 | 0.01 | 0.52 | 2.58 |

## cmp_gt

### tileops

| op_name | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| gt | torch.float16 | 0.02 | 0.22 | 1.11 |

### baseline

| op_name | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| gt | torch.float16 | 0.01 | 0.51 | 2.56 |

## cmp_lt

### tileops

| op_name | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| lt | torch.float16 | 0.02 | 0.22 | 1.10 |

### baseline

| op_name | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| lt | torch.float16 | 0.01 | 0.51 | 2.55 |

## cmp_ge

### tileops

| op_name | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| ge | torch.float16 | 0.02 | 0.22 | 1.10 |

### baseline

| op_name | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| ge | torch.float16 | 0.01 | 0.51 | 2.56 |

## cmp_le

### tileops

| op_name | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| le | torch.float16 | 0.02 | 0.22 | 1.10 |

### baseline

| op_name | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| le | torch.float16 | 0.01 | 0.51 | 2.55 |

## logical_and

### tileops

| op_name | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| logical_and | torch.float16 | 0.02 | 0.22 | 1.10 |
| logical_and | torch.float16 | 0.04 | 0.26 | 1.32 |

### baseline

| op_name | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| logical_and | torch.float16 | 0.01 | 0.71 | 3.54 |
| logical_and | torch.float16 | 0.01 | 0.93 | 4.67 |

## logical_or

### tileops

| op_name | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| logical_or | torch.float16 | 0.02 | 0.22 | 1.10 |
| logical_or | torch.float16 | 0.04 | 0.26 | 1.32 |

### baseline

| op_name | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| logical_or | torch.float16 | 0.01 | 0.71 | 3.55 |
| logical_or | torch.float16 | 0.01 | 0.94 | 4.69 |

## bitwise_and

### tileops

| op_name | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| bitwise_and | torch.int32 | 0.02 | 0.27 | 3.22 |
| bitwise_and | torch.int32 | 0.03 | 0.31 | 3.75 |

### baseline

| op_name | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| bitwise_and | torch.int32 | 0.02 | 0.28 | 3.31 |
| bitwise_and | torch.int32 | 0.03 | 0.32 | 3.83 |

## bitwise_or

### tileops

| op_name | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| bitwise_or | torch.int32 | 0.02 | 0.27 | 3.22 |

### baseline

| op_name | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| bitwise_or | torch.int32 | 0.02 | 0.28 | 3.30 |

## bitwise_xor

### tileops

| op_name | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| bitwise_xor | torch.int32 | 0.02 | 0.27 | 3.22 |

### baseline

| op_name | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| bitwise_xor | torch.int32 | 0.02 | 0.28 | 3.31 |

## gelu_and_mul

### tileops

| op_name | M | N | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| gelu_and_mul | 1024 | 4096 | torch.float16 | 0.01 | 0.78 | 2.34 |
| gelu_and_mul | 1024 | 10240 | torch.float16 | 0.02 | 0.92 | 2.75 |
| gelu_and_mul | 1024 | 20480 | torch.float16 | 0.04 | 1.04 | 3.11 |

### baseline

| op_name | M | N | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| gelu_and_mul | 1024 | 4096 | torch.float16 | 0.03 | 0.27 | 0.80 |
| gelu_and_mul | 1024 | 10240 | torch.float16 | 0.07 | 0.30 | 0.91 |
| gelu_and_mul | 1024 | 20480 | torch.float16 | 0.13 | 0.32 | 0.96 |

## gelu_tanh_and_mul

### tileops

| op_name | M | N | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| gelu_tanh_and_mul | 1024 | 4096 | torch.float16 | 0.01 | 0.91 | 2.73 |
| gelu_tanh_and_mul | 1024 | 10240 | torch.float16 | 0.02 | 1.14 | 3.42 |
| gelu_tanh_and_mul | 1024 | 20480 | torch.float16 | 0.03 | 1.24 | 3.72 |

### baseline

| op_name | M | N | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| gelu_tanh_and_mul | 1024 | 4096 | torch.float16 | 0.03 | 0.28 | 0.83 |
| gelu_tanh_and_mul | 1024 | 10240 | torch.float16 | 0.07 | 0.31 | 0.94 |
| gelu_tanh_and_mul | 1024 | 20480 | torch.float16 | 0.13 | 0.33 | 1.00 |

## silu_and_mul_strategy

### tileops_direct

| op_name | M | N | dtype | strategy | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| silu_and_mul | 1024 | 4096 | torch.float16 | direct | 0.02 | 0.49 | 1.47 |
| silu_and_mul | 1024 | 4096 | torch.bfloat16 | direct | 0.02 | 0.49 | 1.47 |
| silu_and_mul | 1024 | 4096 | torch.float32 | direct | 0.02 | 0.42 | 2.55 |
| silu_and_mul | 1024 | 10240 | torch.float16 | direct | 0.04 | 0.53 | 1.60 |
| silu_and_mul | 1024 | 10240 | torch.bfloat16 | direct | 0.04 | 0.53 | 1.60 |
| silu_and_mul | 1024 | 10240 | torch.float32 | direct | 0.04 | 0.47 | 2.82 |
| silu_and_mul | 4096 | 4096 | torch.float16 | direct | 0.06 | 0.55 | 1.66 |
| silu_and_mul | 4096 | 4096 | torch.bfloat16 | direct | 0.06 | 0.55 | 1.66 |
| silu_and_mul | 4096 | 4096 | torch.float32 | direct | 0.07 | 0.49 | 2.94 |

### tileops_explicit_parallel

| op_name | M | N | dtype | strategy | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| silu_and_mul | 1024 | 4096 | torch.float16 | explicit_parallel | 0.01 | 0.85 | 2.55 |
| silu_and_mul | 1024 | 4096 | torch.bfloat16 | explicit_parallel | 0.01 | 0.91 | 2.73 |
| silu_and_mul | 1024 | 4096 | torch.float32 | explicit_parallel | 0.02 | 0.55 | 3.28 |
| silu_and_mul | 1024 | 10240 | torch.float16 | explicit_parallel | 0.02 | 0.99 | 2.98 |
| silu_and_mul | 1024 | 10240 | torch.bfloat16 | explicit_parallel | 0.02 | 1.15 | 3.44 |
| silu_and_mul | 1024 | 10240 | torch.float32 | explicit_parallel | 0.03 | 0.63 | 3.80 |
| silu_and_mul | 4096 | 4096 | torch.float16 | explicit_parallel | 0.03 | 1.06 | 3.17 |
| silu_and_mul | 4096 | 4096 | torch.bfloat16 | explicit_parallel | 0.03 | 1.23 | 3.68 |
| silu_and_mul | 4096 | 4096 | torch.float32 | explicit_parallel | 0.05 | 0.67 | 4.00 |

## gelu_and_mul_strategy

### tileops_direct

| op_name | M | N | dtype | strategy | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| gelu_and_mul | 1024 | 4096 | torch.float16 | direct | 0.02 | 0.48 | 1.45 |
| gelu_and_mul | 1024 | 4096 | torch.bfloat16 | direct | 0.02 | 0.48 | 1.45 |
| gelu_and_mul | 1024 | 4096 | torch.float32 | direct | 0.02 | 0.43 | 2.56 |
| gelu_and_mul | 1024 | 10240 | torch.float16 | direct | 0.04 | 0.53 | 1.58 |
| gelu_and_mul | 1024 | 10240 | torch.bfloat16 | direct | 0.04 | 0.53 | 1.58 |
| gelu_and_mul | 1024 | 10240 | torch.float32 | direct | 0.04 | 0.47 | 2.84 |
| gelu_and_mul | 4096 | 4096 | torch.float16 | direct | 0.06 | 0.54 | 1.63 |
| gelu_and_mul | 4096 | 4096 | torch.bfloat16 | direct | 0.06 | 0.54 | 1.63 |
| gelu_and_mul | 4096 | 4096 | torch.float32 | direct | 0.07 | 0.49 | 2.95 |

### tileops_explicit_parallel

| op_name | M | N | dtype | strategy | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| gelu_and_mul | 1024 | 4096 | torch.float16 | explicit_parallel | 0.01 | 0.78 | 2.34 |
| gelu_and_mul | 1024 | 4096 | torch.bfloat16 | explicit_parallel | 0.01 | 0.75 | 2.24 |
| gelu_and_mul | 1024 | 4096 | torch.float32 | explicit_parallel | 0.02 | 0.55 | 3.28 |
| gelu_and_mul | 1024 | 10240 | torch.float16 | explicit_parallel | 0.02 | 0.92 | 2.75 |
| gelu_and_mul | 1024 | 10240 | torch.bfloat16 | explicit_parallel | 0.02 | 0.92 | 2.75 |
| gelu_and_mul | 1024 | 10240 | torch.float32 | explicit_parallel | 0.03 | 0.62 | 3.73 |
| gelu_and_mul | 4096 | 4096 | torch.float16 | explicit_parallel | 0.03 | 1.00 | 2.99 |
| gelu_and_mul | 4096 | 4096 | torch.bfloat16 | explicit_parallel | 0.03 | 0.96 | 2.88 |
| gelu_and_mul | 4096 | 4096 | torch.float32 | explicit_parallel | 0.05 | 0.67 | 3.99 |

## gelu_tanh_and_mul_strategy

### tileops_direct

| op_name | M | N | dtype | strategy | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| gelu_tanh_and_mul | 1024 | 4096 | torch.float16 | direct | 0.02 | 0.49 | 1.48 |
| gelu_tanh_and_mul | 1024 | 4096 | torch.bfloat16 | direct | 0.02 | 0.49 | 1.48 |
| gelu_tanh_and_mul | 1024 | 4096 | torch.float32 | direct | 0.02 | 0.43 | 2.59 |
| gelu_tanh_and_mul | 1024 | 10240 | torch.float16 | direct | 0.04 | 0.54 | 1.61 |
| gelu_tanh_and_mul | 1024 | 10240 | torch.bfloat16 | direct | 0.04 | 0.54 | 1.61 |
| gelu_tanh_and_mul | 1024 | 10240 | torch.float32 | direct | 0.04 | 0.48 | 2.87 |
| gelu_tanh_and_mul | 4096 | 4096 | torch.float16 | direct | 0.06 | 0.56 | 1.67 |
| gelu_tanh_and_mul | 4096 | 4096 | torch.bfloat16 | direct | 0.06 | 0.56 | 1.67 |
| gelu_tanh_and_mul | 4096 | 4096 | torch.float32 | direct | 0.07 | 0.50 | 2.99 |

### tileops_explicit_parallel

| op_name | M | N | dtype | strategy | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| gelu_tanh_and_mul | 1024 | 4096 | torch.float16 | explicit_parallel | 0.01 | 0.91 | 2.73 |
| gelu_tanh_and_mul | 1024 | 4096 | torch.bfloat16 | explicit_parallel | 0.01 | 0.91 | 2.72 |
| gelu_tanh_and_mul | 1024 | 4096 | torch.float32 | explicit_parallel | 0.02 | 0.55 | 3.30 |
| gelu_tanh_and_mul | 1024 | 10240 | torch.float16 | explicit_parallel | 0.02 | 1.14 | 3.42 |
| gelu_tanh_and_mul | 1024 | 10240 | torch.bfloat16 | explicit_parallel | 0.02 | 1.12 | 3.36 |
| gelu_tanh_and_mul | 1024 | 10240 | torch.float32 | explicit_parallel | 0.03 | 0.64 | 3.81 |
| gelu_tanh_and_mul | 4096 | 4096 | torch.float16 | explicit_parallel | 0.03 | 1.20 | 3.60 |
| gelu_tanh_and_mul | 4096 | 4096 | torch.bfloat16 | explicit_parallel | 0.03 | 1.18 | 3.54 |
| gelu_tanh_and_mul | 4096 | 4096 | torch.float32 | explicit_parallel | 0.05 | 0.67 | 4.01 |

## sub_bcast

### tileops

| op_name | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| sub | torch.float16 | 0.01 | 0.65 | 2.60 |
| sub | torch.float16 | 0.01 | 0.83 | 3.31 |
| sub | torch.float16 | 0.02 | 0.93 | 3.73 |

### baseline

| op_name | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| sub | torch.float16 | 0.01 | 0.29 | 1.15 |
| sub | torch.float16 | 0.03 | 0.34 | 1.35 |
| sub | torch.float16 | 0.06 | 0.36 | 1.46 |

## mul_bcast

### tileops

| op_name | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| mul | torch.float16 | 0.01 | 0.65 | 2.60 |
| mul | torch.float16 | 0.01 | 0.83 | 3.32 |
| mul | torch.float16 | 0.02 | 0.93 | 3.73 |

### baseline

| op_name | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| mul | torch.float16 | 0.01 | 0.29 | 1.15 |
| mul | torch.float16 | 0.03 | 0.34 | 1.35 |
| mul | torch.float16 | 0.06 | 0.37 | 1.46 |

## div_bcast

### tileops

| op_name | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| div | torch.float16 | 0.01 | 0.60 | 2.42 |
| div | torch.float16 | 0.01 | 0.77 | 3.07 |
| div | torch.float16 | 0.02 | 0.85 | 3.38 |

### baseline

| op_name | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| div | torch.float16 | 0.02 | 0.27 | 1.08 |
| div | torch.float16 | 0.03 | 0.32 | 1.26 |
| div | torch.float16 | 0.06 | 0.34 | 1.36 |

## binary_strategy

### add_direct

| n_total | shape_label | dtype | strategy | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 4194304 | 1024x4096 | torch.float16 | direct | 0.02 | 0.26 | 1.55 |
| 4194304 | 1024x4096 | torch.bfloat16 | direct | 0.02 | 0.26 | 1.55 |
| 4194304 | 1024x4096 | torch.float32 | direct | 0.02 | 0.22 | 2.58 |
| 10485760 | 1024x10240 | torch.float16 | direct | 0.04 | 0.28 | 1.68 |
| 10485760 | 1024x10240 | torch.bfloat16 | direct | 0.04 | 0.28 | 1.68 |
| 10485760 | 1024x10240 | torch.float32 | direct | 0.04 | 0.24 | 2.91 |
| 20971520 | 1024x20480 | torch.float16 | direct | 0.07 | 0.30 | 1.78 |
| 20971520 | 1024x20480 | torch.bfloat16 | direct | 0.07 | 0.30 | 1.78 |
| 20971520 | 1024x20480 | torch.float32 | direct | 0.08 | 0.26 | 3.07 |

### add_explicit_parallel

| n_total | shape_label | dtype | strategy | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 4194304 | 1024x4096 | torch.float16 | explicit_parallel | 0.01 | 0.47 | 2.83 |
| 4194304 | 1024x4096 | torch.bfloat16 | explicit_parallel | 0.01 | 0.47 | 2.82 |
| 4194304 | 1024x4096 | torch.float32 | explicit_parallel | 0.02 | 0.27 | 3.29 |
| 10485760 | 1024x10240 | torch.float16 | explicit_parallel | 0.02 | 0.57 | 3.43 |
| 10485760 | 1024x10240 | torch.bfloat16 | explicit_parallel | 0.02 | 0.57 | 3.43 |
| 10485760 | 1024x10240 | torch.float32 | explicit_parallel | 0.03 | 0.32 | 3.83 |
| 20971520 | 1024x20480 | torch.float16 | explicit_parallel | 0.03 | 0.64 | 3.83 |
| 20971520 | 1024x20480 | torch.bfloat16 | explicit_parallel | 0.03 | 0.64 | 3.83 |
| 20971520 | 1024x20480 | torch.float32 | explicit_parallel | 0.06 | 0.34 | 4.09 |

## cumulative

### tileops

| m | n | dtype | op_kind | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 1024 | 4096 | torch.float16 | cumsum | 0.06 | 0.07 | 0.28 |
| 1024 | 4096 | torch.bfloat16 | cumsum | 0.06 | 0.07 | 0.28 |
| 4096 | 4096 | torch.float16 | cumsum | 0.12 | 0.14 | 0.56 |
| 1024 | 4096 | torch.float16 | cumprod | 0.06 | 0.07 | 0.28 |
| 1024 | 4096 | torch.bfloat16 | cumprod | 0.06 | 0.07 | 0.28 |
| 4096 | 4096 | torch.float16 | cumprod | 0.12 | 0.14 | 0.56 |

### baseline

| m | n | dtype | op_kind | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 1024 | 4096 | torch.float16 | cumsum | 0.10 | 0.04 | 0.17 |
| 1024 | 4096 | torch.bfloat16 | cumsum | 0.10 | 0.04 | 0.17 |
| 4096 | 4096 | torch.float16 | cumsum | 0.26 | 0.07 | 0.26 |
| 1024 | 4096 | torch.float16 | cumprod | 0.10 | 0.04 | 0.17 |
| 1024 | 4096 | torch.bfloat16 | cumprod | 0.10 | 0.04 | 0.17 |
| 4096 | 4096 | torch.float16 | cumprod | 0.26 | 0.07 | 0.26 |

## dsa_decode

### tileops

| batch | heads | seq_len_q | seq_len_kv | dim | dim_tail | topk | stride_kv | heads_kv | q_start_index_s | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 128 | 1024 | 2048 | 512 | 64 | 2048 | 1 | 1 | 1024 | torch.float16 | 1.14 | 512.45 | 0.26 |
| 1 | 128 | 512 | 4096 | 512 | 64 | 1024 | 1 | 1 | 512 | torch.float16 | 0.31 | 464.23 | 0.48 |

### baseline

| batch | heads | seq_len_q | seq_len_kv | dim | dim_tail | topk | stride_kv | heads_kv | q_start_index_s | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 128 | 1024 | 2048 | 512 | 64 | 2048 | 1 | 1 | 1024 | torch.float16 | 16.50 | 35.39 | 0.02 |
| 1 | 128 | 512 | 4096 | 512 | 64 | 1024 | 1 | 1 | 512 | torch.float16 | 16.73 | 8.73 | 0.01 |

## mla_decode

### tileops

| batch | heads | heads_kv | seq_len_kv | dim | dim_pe | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 32 | 128 | 1 | 8192 | 512 | 64 | torch.float16 | 0.16 | 445.47 | 1.87 |
| 16 | 128 | 1 | 4096 | 512 | 64 | torch.float16 | 0.05 | 379.02 | 1.62 |

### baseline

| batch | heads | heads_kv | seq_len_kv | dim | dim_pe | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 32 | 128 | 1 | 8192 | 512 | 64 | torch.float16 | 0.72 | 101.21 | 0.43 |
| 16 | 128 | 1 | 4096 | 512 | 64 | torch.float16 | 0.19 | 95.76 | 0.41 |

## nsa_cmp_fwd

### tileops

| seq_num | c_seq_len | heads | dim_k | dim_v | group | scale | bc | bs | bk | bv | dtype | accum_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9 | 8192 | 32 | 128 | 128 | 16 | 0.08838834764831845 | 32 | 32 | 128 | 128 | torch.float16 | torch.float32 | 0.32 | 54.26 | 6.99 |
| 16 | 16384 | 32 | 128 | 128 | 16 | 0.08838834764831845 | 32 | 32 | 128 | 128 | torch.float16 | torch.float32 | 158.17 | 0.43 | 0.06 |

### baseline

| seq_num | c_seq_len | heads | dim_k | dim_v | group | scale | bc | bs | bk | bv | dtype | accum_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9 | 8192 | 32 | 128 | 128 | 16 | 0.08838834764831845 | 32 | 32 | 128 | 128 | torch.float16 | torch.float32 | 306.11 | 0.06 | 0.01 |
| 16 | 16384 | 32 | 128 | 128 | 16 | 0.08838834764831845 | 32 | 32 | 128 | 128 | torch.float16 | torch.float32 | 594.53 | 0.12 | 0.01 |

## nsa_fwd

### tileops

| batch | heads | c_seq_len | dim | is_causal | scale | block_size | groups | selected_blocks | dtype | accum_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 16 | 1024 | 64 | True | 0.1 | 32 | 16 | 1 | torch.float16 | torch.float32 | 144.85 | 0.00 | 0.00 |
| 4 | 16 | 8192 | 64 | True | 0.1 | 32 | 16 | 1 | torch.float16 | torch.float32 | 145.26 | 0.01 | 0.00 |
| 2 | 16 | 8192 | 64 | True | 0.1 | 32 | 16 | 4 | torch.float16 | torch.float32 | 146.00 | 0.03 | 0.00 |

### baseline

| batch | heads | c_seq_len | dim | is_causal | scale | block_size | groups | selected_blocks | dtype | accum_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 16 | 1024 | 64 | True | 0.1 | 32 | 16 | 1 | torch.float16 | torch.float32 | 64.82 | 0.00 | 0.00 |
| 4 | 16 | 8192 | 64 | True | 0.1 | 32 | 16 | 1 | torch.float16 | torch.float32 | 518.88 | 0.00 | 0.00 |
| 2 | 16 | 8192 | 64 | True | 0.1 | 32 | 16 | 4 | torch.float16 | torch.float32 | 477.81 | 0.01 | 0.00 |

## nsa_topk

### tileops

| seq_num | c_seq_len | heads | dim | group | scale | selected_block_num | bc | bs | bk | dtype | accum_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | 1024 | 32 | 128 | 16 | 1 | 16 | 32 | 32 | 128 | torch.float16 | torch.float32 | 252.07 | 0.00 | 0.00 |
| 3 | 512 | 32 | 128 | 16 | 1 | 16 | 32 | 32 | 128 | torch.float16 | torch.float32 | 251.38 | 0.00 | 0.00 |
| 9 | 8192 | 32 | 128 | 16 | 1 | 16 | 32 | 32 | 128 | torch.float16 | torch.float32 | 252.37 | 0.07 | 0.00 |

### baseline

| seq_num | c_seq_len | heads | dim | group | scale | selected_block_num | bc | bs | bk | dtype | accum_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | 1024 | 32 | 128 | 16 | 1 | 16 | 32 | 32 | 128 | torch.float16 | torch.float32 | 240.64 | 0.00 | 0.00 |
| 3 | 512 | 32 | 128 | 16 | 1 | 16 | 32 | 32 | 128 | torch.float16 | torch.float32 | 119.68 | 0.00 | 0.00 |
| 9 | 8192 | 32 | 128 | 16 | 1 | 16 | 32 | 32 | 128 | torch.float16 | torch.float32 | 2499.11 | 0.01 | 0.00 |

## dropout

### tileops

| dtype | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| torch.float16 | 4194304 | 0.01 | 0.64 | 2.56 |
| torch.bfloat16 | 4194304 | 0.01 | 0.64 | 2.56 |
| torch.float32 | 4194304 | 0.01 | 0.39 | 3.09 |
| torch.float16 | 10485760 | 0.01 | 0.82 | 3.30 |
| torch.bfloat16 | 10485760 | 0.01 | 0.83 | 3.30 |
| torch.float32 | 10485760 | 0.02 | 0.47 | 3.78 |
| torch.float16 | 20971520 | 0.02 | 0.94 | 3.78 |
| torch.bfloat16 | 20971520 | 0.02 | 0.94 | 3.78 |
| torch.float32 | 20971520 | 0.04 | 0.51 | 4.07 |

### baseline

| dtype | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| torch.float16 | 4194304 | 0.01 | 0.38 | 1.53 |
| torch.bfloat16 | 4194304 | 0.01 | 0.38 | 1.51 |
| torch.float32 | 4194304 | 0.01 | 0.28 | 2.25 |
| torch.float16 | 10485760 | 0.02 | 0.50 | 2.00 |
| torch.bfloat16 | 10485760 | 0.02 | 0.49 | 1.97 |
| torch.float32 | 10485760 | 0.03 | 0.32 | 2.60 |
| torch.float16 | 20971520 | 0.04 | 0.55 | 2.19 |
| torch.bfloat16 | 20971520 | 0.04 | 0.54 | 2.16 |
| torch.float32 | 20971520 | 0.06 | 0.34 | 2.76 |

## relu_fp8

### tileops

| op_name | n_total | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| relu_fp8 | 8388608 | torch.float8_e4m3fn | 0.01 | 0.57 | 1.14 |
| relu_fp8 | 8388608 | torch.float8_e5m2 | 0.02 | 0.45 | 0.91 |
| relu_fp8 | 67108864 | torch.float8_e4m3fn | 0.09 | 0.71 | 1.42 |
| relu_fp8 | 67108864 | torch.float8_e5m2 | 0.12 | 0.54 | 1.09 |
| relu_fp8 | 134217728 | torch.float8_e4m3fn | 0.18 | 0.73 | 1.47 |
| relu_fp8 | 134217728 | torch.float8_e5m2 | 0.24 | 0.56 | 1.12 |

### baseline

| op_name | n_total | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| relu_fp8 | 8388608 | torch.float8_e4m3fn | 0.05 | 0.19 | 0.37 |
| relu_fp8 | 8388608 | torch.float8_e5m2 | 0.04 | 0.19 | 0.38 |
| relu_fp8 | 67108864 | torch.float8_e4m3fn | 0.34 | 0.20 | 0.40 |
| relu_fp8 | 67108864 | torch.float8_e5m2 | 0.33 | 0.20 | 0.41 |
| relu_fp8 | 134217728 | torch.float8_e4m3fn | 0.65 | 0.21 | 0.41 |
| relu_fp8 | 134217728 | torch.float8_e5m2 | 0.63 | 0.21 | 0.42 |

## exp_fp8

### tileops

| op_name | n_total | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| exp_fp8 | 8388608 | torch.float8_e4m3fn | 0.01 | 0.98 | 1.95 |
| exp_fp8 | 8388608 | torch.float8_e5m2 | 0.02 | 0.46 | 0.91 |
| exp_fp8 | 67108864 | torch.float8_e4m3fn | 0.05 | 1.32 | 2.65 |
| exp_fp8 | 67108864 | torch.float8_e5m2 | 0.12 | 0.54 | 1.08 |
| exp_fp8 | 134217728 | torch.float8_e4m3fn | 0.10 | 1.38 | 2.76 |
| exp_fp8 | 134217728 | torch.float8_e5m2 | 0.24 | 0.56 | 1.12 |

### baseline

| op_name | n_total | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| exp_fp8 | 8388608 | torch.float8_e4m3fn | 0.05 | 0.19 | 0.37 |
| exp_fp8 | 8388608 | torch.float8_e5m2 | 0.04 | 0.19 | 0.38 |
| exp_fp8 | 67108864 | torch.float8_e4m3fn | 0.33 | 0.20 | 0.40 |
| exp_fp8 | 67108864 | torch.float8_e5m2 | 0.32 | 0.21 | 0.41 |
| exp_fp8 | 134217728 | torch.float8_e4m3fn | 0.64 | 0.21 | 0.42 |
| exp_fp8 | 134217728 | torch.float8_e5m2 | 0.63 | 0.21 | 0.43 |

## add_fp8

### tileops

| op_name | n_total | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| add_fp8 | 8388608 | torch.float8_e4m3fn | 0.01 | 0.85 | 2.56 |
| add_fp8 | 8388608 | torch.float8_e5m2 | 0.02 | 0.41 | 1.24 |
| add_fp8 | 67108864 | torch.float8_e4m3fn | 0.06 | 1.15 | 3.45 |
| add_fp8 | 67108864 | torch.float8_e5m2 | 0.13 | 0.50 | 1.50 |
| add_fp8 | 134217728 | torch.float8_e4m3fn | 0.11 | 1.20 | 3.61 |
| add_fp8 | 134217728 | torch.float8_e5m2 | 0.26 | 0.52 | 1.56 |

### baseline

| op_name | n_total | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| add_fp8 | 8388608 | torch.float8_e4m3fn | 0.08 | 0.11 | 0.32 |
| add_fp8 | 8388608 | torch.float8_e5m2 | 0.07 | 0.11 | 0.34 |
| add_fp8 | 67108864 | torch.float8_e4m3fn | 0.56 | 0.12 | 0.36 |
| add_fp8 | 67108864 | torch.float8_e5m2 | 0.54 | 0.12 | 0.37 |
| add_fp8 | 134217728 | torch.float8_e4m3fn | 1.07 | 0.12 | 0.37 |
| add_fp8 | 134217728 | torch.float8_e5m2 | 1.04 | 0.13 | 0.39 |

## silu_and_mul_fp8

### tileops

| op_name | M | N | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| silu_and_mul_fp8 | 2048 | 11008 | torch.float8_e4m3fn | 0.04 | 2.58 | 1.55 |
| silu_and_mul_fp8 | 2048 | 11008 | torch.float8_e5m2 | 0.06 | 1.76 | 1.06 |
| silu_and_mul_fp8 | 16384 | 11008 | torch.float8_e4m3fn | 0.31 | 2.90 | 1.74 |
| silu_and_mul_fp8 | 16384 | 11008 | torch.float8_e5m2 | 0.45 | 2.00 | 1.20 |
| silu_and_mul_fp8 | 16384 | 28672 | torch.float8_e4m3fn | 0.77 | 3.06 | 1.84 |
| silu_and_mul_fp8 | 16384 | 28672 | torch.float8_e5m2 | 1.10 | 2.14 | 1.28 |

### baseline

| op_name | M | N | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| silu_and_mul_fp8 | 2048 | 11008 | torch.float8_e4m3fn | 0.29 | 0.38 | 0.23 |
| silu_and_mul_fp8 | 2048 | 11008 | torch.float8_e5m2 | 0.29 | 0.39 | 0.24 |
| silu_and_mul_fp8 | 16384 | 11008 | torch.float8_e4m3fn | 2.02 | 0.45 | 0.27 |
| silu_and_mul_fp8 | 16384 | 11008 | torch.float8_e5m2 | 1.97 | 0.46 | 0.27 |
| silu_and_mul_fp8 | 16384 | 28672 | torch.float8_e4m3fn | 4.12 | 0.57 | 0.34 |
| silu_and_mul_fp8 | 16384 | 28672 | torch.float8_e5m2 | 4.05 | 0.58 | 0.35 |

## engram_gate_conv_bwd

### tileops

| M | seq_len | d | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 32 | 256 | torch.float16 | 294.52 | 0.00 | 0.00 |
| 2 | 64 | 512 | torch.float16 | 298.23 | 0.00 | 0.00 |
| 1 | 128 | 256 | torch.bfloat16 | 298.70 | 0.00 | 0.00 |
| 2 | 16 | 256 | torch.bfloat16 | 299.67 | 0.00 | 0.00 |

## engram_decode

### tileops

| batch | d_mem | d | max_conv_len | conv_kernel_size | dilation | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 512 | 256 | 12 | 4 | 3 | torch.float16 | 201.07 | 0.00 | 0.00 |
| 4 | 1024 | 512 | 20 | 4 | 5 | torch.float16 | 205.89 | 0.00 | 0.00 |
| 8 | 512 | 256 | 18 | 4 | 3 | torch.bfloat16 | 0.05 | 0.09 | 0.01 |

### baseline

| batch | d_mem | d | max_conv_len | conv_kernel_size | dilation | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 512 | 256 | 12 | 4 | 3 | torch.float16 | 0.10 | 0.01 | 0.01 |
| 4 | 1024 | 512 | 20 | 4 | 5 | torch.float16 | 0.13 | 0.06 | 0.02 |
| 8 | 512 | 256 | 18 | 4 | 3 | torch.bfloat16 | 0.12 | 0.04 | 0.01 |

## engram_gate_conv_fwd

### tileops

| M | seq_len | d | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 32 | 256 | torch.float16 | 0.00 | 0.05 | 0.02 |
| 2 | 64 | 512 | torch.float16 | 294.05 | 0.00 | 0.00 |
| 1 | 128 | 256 | torch.bfloat16 | 203.60 | 0.00 | 0.00 |
| 2 | 16 | 256 | torch.bfloat16 | 0.00 | 0.05 | 0.02 |

### baseline

| M | seq_len | d | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 32 | 256 | torch.float16 | 0.08 | 0.00 | 0.00 |
| 2 | 64 | 512 | torch.float16 | 0.09 | 0.02 | 0.01 |
| 1 | 128 | 256 | torch.bfloat16 | 0.09 | 0.01 | 0.00 |
| 2 | 16 | 256 | torch.bfloat16 | 0.08 | 0.00 | 0.00 |

## fft_c2c

### tileops

| n | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| 64 | torch.complex64 | 190.80 | 0.00 | 0.00 |
| 128 | torch.complex64 | 179.90 | 0.00 | 0.00 |
| 256 | torch.complex64 | 191.85 | 0.00 | 0.00 |
| 512 | torch.complex64 | 192.06 | 0.00 | 0.00 |
| 1024 | torch.complex64 | 165.99 | 0.00 | 0.00 |

### baseline

| n | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| 64 | torch.complex64 | 0.00 | 0.00 | 0.00 |
| 128 | torch.complex64 | 0.00 | 0.00 | 0.00 |
| 256 | torch.complex64 | 0.00 | 0.00 | 0.00 |
| 512 | torch.complex64 | 0.00 | 0.01 | 0.00 |
| 1024 | torch.complex64 | 0.00 | 0.02 | 0.01 |

## fft_c2c_lut

### tileops-lut

| n | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| 64 | torch.complex64 | 894.08 | 0.00 | 0.00 |
| 128 | torch.complex64 | 872.76 | 0.00 | 0.00 |
| 256 | torch.complex64 | 1015.16 | 0.00 | 0.00 |
| 512 | torch.complex64 | 1028.48 | 0.00 | 0.00 |
| 1024 | torch.complex64 | 904.90 | 0.00 | 0.00 |
| 4096 | torch.complex64 | 846.99 | 0.00 | 0.00 |
| 16384 | torch.complex64 | 0.01 | 0.08 | 0.02 |

### tileops-base

| n | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| 64 | torch.complex64 | 170.03 | 0.00 | 0.00 |
| 128 | torch.complex64 | 198.80 | 0.00 | 0.00 |
| 256 | torch.complex64 | 158.04 | 0.00 | 0.00 |
| 512 | torch.complex64 | 195.64 | 0.00 | 0.00 |
| 1024 | torch.complex64 | 176.96 | 0.00 | 0.00 |
| 4096 | torch.complex64 | 310.72 | 0.00 | 0.00 |
| 16384 | torch.complex64 | 176.90 | 0.00 | 0.00 |

### baseline

| n | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| 64 | torch.complex64 | 0.00 | 0.00 | 0.00 |
| 128 | torch.complex64 | 0.00 | 0.00 | 0.00 |
| 256 | torch.complex64 | 0.00 | 0.00 | 0.00 |
| 512 | torch.complex64 | 0.00 | 0.01 | 0.00 |
| 1024 | torch.complex64 | 0.00 | 0.02 | 0.01 |
| 4096 | torch.complex64 | 0.01 | 0.05 | 0.01 |
| 16384 | torch.complex64 | 0.01 | 0.09 | 0.02 |

## fused_add_layer_norm

### tileops

| m | n | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| 1024 | 4096 | torch.float16 | 102.11 | 0.00 | 0.00 |
| 4096 | 4096 | torch.bfloat16 | 101.82 | 0.00 | 0.00 |
| 1024 | 3000 | torch.float16 | 100.29 | 0.00 | 0.00 |
| 1025 | 4096 | torch.float16 | 100.58 | 0.00 | 0.00 |

### baseline

| m | n | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| 1024 | 4096 | torch.float16 | 0.06 | 0.44 | 0.59 |
| 4096 | 4096 | torch.bfloat16 | 0.21 | 0.48 | 0.64 |
| 1024 | 3000 | torch.float16 | 0.04 | 0.42 | 0.56 |
| 1025 | 4096 | torch.float16 | 0.06 | 0.44 | 0.59 |

## fused_add_rmsnorm

### tileops

| m | n | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| 1024 | 4096 | torch.float16 | 69.68 | 0.00 | 0.00 |
| 4096 | 4096 | torch.bfloat16 | 69.61 | 0.00 | 0.00 |
| 2048 | 5120 | torch.float16 | 69.94 | 0.00 | 0.00 |
| 1025 | 4096 | torch.float16 | 69.67 | 0.00 | 0.00 |

### baseline

| m | n | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| 1024 | 4096 | torch.float16 | 0.13 | 0.17 | 0.27 |
| 4096 | 4096 | torch.bfloat16 | 0.48 | 0.17 | 0.28 |
| 2048 | 5120 | torch.float16 | 0.32 | 0.16 | 0.26 |
| 1025 | 4096 | torch.float16 | 0.13 | 0.17 | 0.27 |

## gated_deltanet_decode

### tileops

| batch | heads | dim_k | dim_v | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 32 | 128 | 128 | torch.float32 | 0.01 | 0.30 | 0.41 |
| 1 | 32 | 128 | 128 | torch.bfloat16 | 0.01 | 0.31 | 0.21 |
| 8 | 32 | 128 | 128 | torch.float32 | 0.02 | 1.18 | 1.60 |
| 8 | 32 | 128 | 128 | torch.bfloat16 | 0.01 | 2.10 | 1.42 |
| 16 | 32 | 128 | 128 | torch.float32 | 0.04 | 1.24 | 1.67 |
| 16 | 32 | 128 | 128 | torch.bfloat16 | 0.02 | 3.04 | 2.05 |
| 32 | 32 | 128 | 128 | torch.float32 | 0.08 | 1.33 | 1.79 |
| 32 | 32 | 128 | 128 | torch.bfloat16 | 0.03 | 3.31 | 2.23 |
| 1 | 32 | 64 | 64 | torch.float32 | 0.01 | 0.14 | 0.19 |
| 8 | 32 | 64 | 64 | torch.float32 | 0.01 | 0.59 | 0.81 |
| 32 | 32 | 64 | 64 | torch.float32 | 0.04 | 0.71 | 0.97 |
| 64 | 32 | 128 | 128 | torch.float32 | 0.15 | 1.38 | 1.86 |
| 64 | 32 | 128 | 128 | torch.bfloat16 | 0.06 | 3.66 | 2.47 |

### baseline

| batch | heads | dim_k | dim_v | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 32 | 128 | 128 | torch.float32 | 0.03 | 0.09 | 0.13 |
| 1 | 32 | 128 | 128 | torch.bfloat16 | 0.05 | 0.06 | 0.04 |
| 8 | 32 | 128 | 128 | torch.float32 | 0.08 | 0.31 | 0.42 |
| 8 | 32 | 128 | 128 | torch.bfloat16 | 0.11 | 0.23 | 0.15 |
| 16 | 32 | 128 | 128 | torch.float32 | 0.12 | 0.41 | 0.56 |
| 16 | 32 | 128 | 128 | torch.bfloat16 | 0.18 | 0.28 | 0.19 |
| 32 | 32 | 128 | 128 | torch.float32 | 0.21 | 0.47 | 0.64 |
| 32 | 32 | 128 | 128 | torch.bfloat16 | 0.31 | 0.33 | 0.22 |
| 1 | 32 | 64 | 64 | torch.float32 | 0.03 | 0.03 | 0.04 |
| 8 | 32 | 64 | 64 | torch.float32 | 0.04 | 0.16 | 0.22 |
| 32 | 32 | 64 | 64 | torch.float32 | 0.08 | 0.32 | 0.44 |
| 64 | 32 | 128 | 128 | torch.float32 | 0.39 | 0.52 | 0.70 |
| 64 | 32 | 128 | 128 | torch.bfloat16 | 0.56 | 0.36 | 0.24 |

## gated_deltanet_fwd

### tileops

| batch | seq_len | heads | dim_k | dim_v | chunk_size | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 4096 | 4 | 64 | 64 | 32 | torch.float16 | 264.94 | 0.00 | 0.00 |
| 2 | 4096 | 4 | 64 | 64 | 32 | torch.bfloat16 | 258.78 | 0.00 | 0.00 |
| 2 | 2048 | 4 | 64 | 64 | 64 | torch.float16 | 262.90 | 0.00 | 0.00 |
| 2 | 4096 | 4 | 64 | 64 | 64 | torch.float16 | 261.94 | 0.00 | 0.00 |
| 2 | 8192 | 4 | 64 | 64 | 64 | torch.float16 | 493.10 | 0.00 | 0.00 |
| 2 | 16384 | 4 | 64 | 64 | 64 | torch.float16 | 384.15 | 0.00 | 0.00 |
| 2 | 32768 | 4 | 64 | 64 | 64 | torch.float16 | 262.41 | 0.01 | 0.00 |
| 2 | 2048 | 4 | 64 | 64 | 64 | torch.bfloat16 | 0.08 | 1.66 | 0.10 |
| 2 | 4096 | 4 | 64 | 64 | 64 | torch.bfloat16 | 258.83 | 0.00 | 0.00 |
| 2 | 8192 | 4 | 64 | 64 | 64 | torch.bfloat16 | 263.17 | 0.00 | 0.00 |
| 2 | 16384 | 4 | 64 | 64 | 64 | torch.bfloat16 | 262.52 | 0.00 | 0.00 |
| 2 | 32768 | 4 | 64 | 64 | 64 | torch.bfloat16 | 258.99 | 0.01 | 0.00 |

### baseline

| batch | seq_len | heads | dim_k | dim_v | chunk_size | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 4096 | 4 | 64 | 64 | 32 | torch.float16 | 130.94 | 0.00 | 0.00 |
| 2 | 4096 | 4 | 64 | 64 | 32 | torch.bfloat16 | 131.22 | 0.00 | 0.00 |
| 2 | 2048 | 4 | 64 | 64 | 64 | torch.float16 | 45.05 | 0.00 | 0.00 |
| 2 | 4096 | 4 | 64 | 64 | 64 | torch.float16 | 90.84 | 0.00 | 0.00 |
| 2 | 8192 | 4 | 64 | 64 | 64 | torch.float16 | 182.35 | 0.00 | 0.00 |
| 2 | 16384 | 4 | 64 | 64 | 64 | torch.float16 | 363.55 | 0.00 | 0.00 |
| 2 | 32768 | 4 | 64 | 64 | 64 | torch.float16 | 733.48 | 0.00 | 0.00 |
| 2 | 2048 | 4 | 64 | 64 | 64 | torch.bfloat16 | 45.04 | 0.00 | 0.00 |
| 2 | 4096 | 4 | 64 | 64 | 64 | torch.bfloat16 | 90.93 | 0.00 | 0.00 |
| 2 | 8192 | 4 | 64 | 64 | 64 | torch.bfloat16 | 183.00 | 0.00 | 0.00 |
| 2 | 16384 | 4 | 64 | 64 | 64 | torch.bfloat16 | 364.23 | 0.00 | 0.00 |
| 2 | 32768 | 4 | 64 | 64 | 64 | torch.bfloat16 | 730.79 | 0.00 | 0.00 |

## gated_deltanet_bwd

### tileops

| batch | seq_len | heads | dim_k | dim_v | chunk_size | dtype | B | H | S | DK | DV | BC | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 4096 | 4 | 64 | 64 | 32 | torch.float16 | 2 | 4 | 4096 | 64 | 64 | 32 | 2119.95 | 0.00 | 0.00 |
| 2 | 4096 | 4 | 64 | 64 | 32 | torch.bfloat16 | 2 | 4 | 4096 | 64 | 64 | 32 | 900.12 | 0.00 | 0.00 |
| 2 | 2048 | 4 | 64 | 64 | 64 | torch.float16 | 2 | 4 | 2048 | 64 | 64 | 64 | 819.66 | 0.00 | 0.00 |
| 2 | 4096 | 4 | 64 | 64 | 64 | torch.float16 | 2 | 4 | 4096 | 64 | 64 | 64 | 0.34 | 1.56 | 0.09 |
| 2 | 8192 | 4 | 64 | 64 | 64 | torch.float16 | 2 | 4 | 8192 | 64 | 64 | 64 | 818.09 | 0.00 | 0.00 |
| 2 | 16384 | 4 | 64 | 64 | 64 | torch.float16 | 2 | 4 | 16384 | 64 | 64 | 64 | 818.61 | 0.00 | 0.00 |
| 2 | 2048 | 4 | 64 | 64 | 64 | torch.bfloat16 | 2 | 4 | 2048 | 64 | 64 | 64 | 0.19 | 1.40 | 0.08 |
| 2 | 4096 | 4 | 64 | 64 | 64 | torch.bfloat16 | 2 | 4 | 4096 | 64 | 64 | 64 | 0.35 | 1.55 | 0.09 |
| 2 | 8192 | 4 | 64 | 64 | 64 | torch.bfloat16 | 2 | 4 | 8192 | 64 | 64 | 64 | 0.64 | 1.68 | 0.09 |
| 2 | 16384 | 4 | 64 | 64 | 64 | torch.bfloat16 | 2 | 4 | 16384 | 64 | 64 | 64 | 817.00 | 0.00 | 0.00 |

### baseline

| batch | seq_len | heads | dim_k | dim_v | chunk_size | dtype | B | H | S | DK | DV | BC | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 4096 | 4 | 64 | 64 | 32 | torch.float16 | 2 | 4 | 4096 | 64 | 64 | 32 | 49.89 | 0.01 | 0.00 |
| 2 | 4096 | 4 | 64 | 64 | 32 | torch.bfloat16 | 2 | 4 | 4096 | 64 | 64 | 32 | 49.86 | 0.01 | 0.00 |
| 2 | 2048 | 4 | 64 | 64 | 64 | torch.float16 | 2 | 4 | 2048 | 64 | 64 | 64 | 19.34 | 0.01 | 0.00 |
| 2 | 4096 | 4 | 64 | 64 | 64 | torch.float16 | 2 | 4 | 4096 | 64 | 64 | 64 | 39.65 | 0.01 | 0.00 |
| 2 | 8192 | 4 | 64 | 64 | 64 | torch.float16 | 2 | 4 | 8192 | 64 | 64 | 64 | 82.46 | 0.01 | 0.00 |
| 2 | 16384 | 4 | 64 | 64 | 64 | torch.float16 | 2 | 4 | 16384 | 64 | 64 | 64 | 175.41 | 0.01 | 0.00 |
| 2 | 2048 | 4 | 64 | 64 | 64 | torch.bfloat16 | 2 | 4 | 2048 | 64 | 64 | 64 | 19.25 | 0.01 | 0.00 |
| 2 | 4096 | 4 | 64 | 64 | 64 | torch.bfloat16 | 2 | 4 | 4096 | 64 | 64 | 64 | 39.52 | 0.01 | 0.00 |
| 2 | 8192 | 4 | 64 | 64 | 64 | torch.bfloat16 | 2 | 4 | 8192 | 64 | 64 | 64 | 82.46 | 0.01 | 0.00 |
| 2 | 16384 | 4 | 64 | 64 | 64 | torch.bfloat16 | 2 | 4 | 16384 | 64 | 64 | 64 | 175.35 | 0.01 | 0.00 |

## gated_deltanet_fwdbwd

### tileops

| batch | seq_len | heads | dim_k | dim_v | chunk_size | dtype | B | H | S | DK | DV | BC | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 4096 | 4 | 64 | 64 | 32 | torch.float16 | 2 | 4 | 4096 | 64 | 64 | 32 | 931.54 | 0.00 | 0.00 |
| 2 | 4096 | 4 | 64 | 64 | 32 | torch.bfloat16 | 2 | 4 | 4096 | 64 | 64 | 32 | 934.91 | 0.00 | 0.00 |
| 2 | 2048 | 4 | 64 | 64 | 64 | torch.float16 | 2 | 4 | 2048 | 64 | 64 | 64 | 930.27 | 0.00 | 0.00 |
| 2 | 4096 | 4 | 64 | 64 | 64 | torch.float16 | 2 | 4 | 4096 | 64 | 64 | 64 | 1010.73 | 0.00 | 0.00 |
| 2 | 8192 | 4 | 64 | 64 | 64 | torch.float16 | 2 | 4 | 8192 | 64 | 64 | 64 | 927.66 | 0.00 | 0.00 |
| 2 | 16384 | 4 | 64 | 64 | 64 | torch.float16 | 2 | 4 | 16384 | 64 | 64 | 64 | 928.77 | 0.00 | 0.00 |
| 2 | 2048 | 4 | 64 | 64 | 64 | torch.bfloat16 | 2 | 4 | 2048 | 64 | 64 | 64 | 1011.68 | 0.00 | 0.00 |
| 2 | 4096 | 4 | 64 | 64 | 64 | torch.bfloat16 | 2 | 4 | 4096 | 64 | 64 | 64 | 1010.67 | 0.00 | 0.00 |
| 2 | 8192 | 4 | 64 | 64 | 64 | torch.bfloat16 | 2 | 4 | 8192 | 64 | 64 | 64 | 929.39 | 0.00 | 0.00 |
| 2 | 16384 | 4 | 64 | 64 | 64 | torch.bfloat16 | 2 | 4 | 16384 | 64 | 64 | 64 | 927.67 | 0.00 | 0.00 |

### baseline

| batch | seq_len | heads | dim_k | dim_v | chunk_size | dtype | B | H | S | DK | DV | BC | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 4096 | 4 | 64 | 64 | 32 | torch.float16 | 2 | 4 | 4096 | 64 | 64 | 32 | 49.86 | 0.02 | 0.00 |
| 2 | 4096 | 4 | 64 | 64 | 32 | torch.bfloat16 | 2 | 4 | 4096 | 64 | 64 | 32 | 49.84 | 0.02 | 0.00 |
| 2 | 2048 | 4 | 64 | 64 | 64 | torch.float16 | 2 | 4 | 2048 | 64 | 64 | 64 | 19.26 | 0.02 | 0.00 |
| 2 | 4096 | 4 | 64 | 64 | 64 | torch.float16 | 2 | 4 | 4096 | 64 | 64 | 64 | 39.41 | 0.02 | 0.00 |
| 2 | 8192 | 4 | 64 | 64 | 64 | torch.float16 | 2 | 4 | 8192 | 64 | 64 | 64 | 82.54 | 0.02 | 0.00 |
| 2 | 16384 | 4 | 64 | 64 | 64 | torch.float16 | 2 | 4 | 16384 | 64 | 64 | 64 | 175.31 | 0.02 | 0.00 |
| 2 | 2048 | 4 | 64 | 64 | 64 | torch.bfloat16 | 2 | 4 | 2048 | 64 | 64 | 64 | 19.22 | 0.02 | 0.00 |
| 2 | 4096 | 4 | 64 | 64 | 64 | torch.bfloat16 | 2 | 4 | 4096 | 64 | 64 | 64 | 39.38 | 0.02 | 0.00 |
| 2 | 8192 | 4 | 64 | 64 | 64 | torch.bfloat16 | 2 | 4 | 8192 | 64 | 64 | 64 | 82.27 | 0.02 | 0.00 |
| 2 | 16384 | 4 | 64 | 64 | 64 | torch.bfloat16 | 2 | 4 | 16384 | 64 | 64 | 64 | 175.22 | 0.02 | 0.00 |

## gemm

### tileops

| m | n | k | dtype | trans_a | trans_b | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1024 | 1024 | 1024 | torch.float16 | False | False | 40.64 | 0.05 | 0.00 |
| 1 | 7168 | 16384 | torch.float16 | False | True | 0.06 | 3.67 | 3.67 |
| 1 | 18432 | 7168 | torch.bfloat16 | False | True | 0.07 | 3.85 | 3.85 |
| 7168 | 1 | 16384 | torch.float16 | False | False | 0.06 | 3.67 | 3.67 |
| 18432 | 1 | 7168 | torch.bfloat16 | False | False | 0.07 | 3.84 | 3.84 |

### baseline

| m | n | k | dtype | trans_a | trans_b | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1024 | 1024 | 1024 | torch.float16 | False | False | 0.01 | 323.85 | 0.95 |
| 1 | 7168 | 16384 | torch.float16 | False | True | 0.07 | 3.41 | 3.41 |
| 1 | 18432 | 7168 | torch.bfloat16 | False | True | 0.08 | 3.47 | 3.47 |
| 7168 | 1 | 16384 | torch.float16 | False | False | 0.07 | 3.41 | 3.41 |
| 18432 | 1 | 7168 | torch.bfloat16 | False | False | 0.08 | 3.46 | 3.47 |

## gla_fwd

### tileops

| batch | seq_len | heads | dim_k | dim_v | chunk_size | dtype | scale | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 2048 | 4 | 64 | 64 | 64 | torch.float16 | 0.125 | 0.08 | 1.74 | 0.11 |
| 2 | 4096 | 4 | 64 | 64 | 64 | torch.float16 | 0.125 | 0.13 | 2.00 | 0.13 |
| 2 | 8192 | 4 | 64 | 64 | 64 | torch.float16 | 0.125 | 0.26 | 2.06 | 0.13 |
| 2 | 16384 | 4 | 64 | 64 | 64 | torch.float16 | 0.125 | 0.50 | 2.16 | 0.14 |
| 2 | 2048 | 4 | 64 | 64 | 64 | torch.bfloat16 | 0.125 | 0.08 | 1.69 | 0.11 |
| 2 | 4096 | 4 | 64 | 64 | 64 | torch.bfloat16 | 0.125 | 0.13 | 2.00 | 0.12 |
| 2 | 8192 | 4 | 64 | 64 | 64 | torch.bfloat16 | 0.125 | 0.26 | 2.07 | 0.13 |
| 2 | 16384 | 4 | 64 | 64 | 64 | torch.bfloat16 | 0.125 | 0.49 | 2.18 | 0.14 |

### baseline

| batch | seq_len | heads | dim_k | dim_v | chunk_size | dtype | scale | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 2048 | 4 | 64 | 64 | 64 | torch.float16 | 0.125 | 1.99 | 0.07 | 0.00 |
| 2 | 4096 | 4 | 64 | 64 | 64 | torch.float16 | 0.125 | 4.05 | 0.07 | 0.00 |
| 2 | 8192 | 4 | 64 | 64 | 64 | torch.float16 | 0.125 | 8.09 | 0.07 | 0.00 |
| 2 | 16384 | 4 | 64 | 64 | 64 | torch.float16 | 0.125 | 16.17 | 0.07 | 0.00 |
| 2 | 2048 | 4 | 64 | 64 | 64 | torch.bfloat16 | 0.125 | 2.00 | 0.07 | 0.00 |
| 2 | 4096 | 4 | 64 | 64 | 64 | torch.bfloat16 | 0.125 | 4.04 | 0.07 | 0.00 |
| 2 | 8192 | 4 | 64 | 64 | 64 | torch.bfloat16 | 0.125 | 8.09 | 0.07 | 0.00 |
| 2 | 16384 | 4 | 64 | 64 | 64 | torch.bfloat16 | 0.125 | 16.19 | 0.07 | 0.00 |

## gla_bwd

### tileops

| batch | seq_len | heads | dim_k | dim_v | chunk_size | dtype | B | T | H | K | V | BC | scale | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 2048 | 4 | 64 | 64 | 64 | torch.float16 | 2 | 2048 | 4 | 64 | 64 | 64 | 0.125 | 0.15 | 1.76 | 0.10 |
| 2 | 4096 | 4 | 64 | 64 | 64 | torch.float16 | 2 | 4096 | 4 | 64 | 64 | 64 | 0.125 | 0.29 | 1.82 | 0.10 |
| 2 | 8192 | 4 | 64 | 64 | 64 | torch.float16 | 2 | 8192 | 4 | 64 | 64 | 64 | 0.125 | 0.57 | 1.89 | 0.10 |
| 2 | 16384 | 4 | 64 | 64 | 64 | torch.float16 | 2 | 16384 | 4 | 64 | 64 | 64 | 0.125 | 0.99 | 2.16 | 0.12 |
| 2 | 2048 | 4 | 64 | 64 | 64 | torch.bfloat16 | 2 | 2048 | 4 | 64 | 64 | 64 | 0.125 | 0.15 | 1.76 | 0.10 |
| 2 | 4096 | 4 | 64 | 64 | 64 | torch.bfloat16 | 2 | 4096 | 4 | 64 | 64 | 64 | 0.125 | 0.30 | 1.82 | 0.10 |
| 2 | 8192 | 4 | 64 | 64 | 64 | torch.bfloat16 | 2 | 8192 | 4 | 64 | 64 | 64 | 0.125 | 0.56 | 1.92 | 0.10 |
| 2 | 16384 | 4 | 64 | 64 | 64 | torch.bfloat16 | 2 | 16384 | 4 | 64 | 64 | 64 | 0.125 | 1.02 | 2.10 | 0.11 |

### baseline

| batch | seq_len | heads | dim_k | dim_v | chunk_size | dtype | B | T | H | K | V | BC | scale | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 2048 | 4 | 64 | 64 | 64 | torch.float16 | 2 | 2048 | 4 | 64 | 64 | 64 | 0.125 | 5.92 | 0.05 | 0.00 |
| 2 | 4096 | 4 | 64 | 64 | 64 | torch.float16 | 2 | 4096 | 4 | 64 | 64 | 64 | 0.125 | 12.51 | 0.04 | 0.00 |
| 2 | 8192 | 4 | 64 | 64 | 64 | torch.float16 | 2 | 8192 | 4 | 64 | 64 | 64 | 0.125 | 28.49 | 0.04 | 0.00 |
| 2 | 16384 | 4 | 64 | 64 | 64 | torch.float16 | 2 | 16384 | 4 | 64 | 64 | 64 | 0.125 | 70.13 | 0.03 | 0.00 |
| 2 | 2048 | 4 | 64 | 64 | 64 | torch.bfloat16 | 2 | 2048 | 4 | 64 | 64 | 64 | 0.125 | 5.92 | 0.05 | 0.00 |
| 2 | 4096 | 4 | 64 | 64 | 64 | torch.bfloat16 | 2 | 4096 | 4 | 64 | 64 | 64 | 0.125 | 12.42 | 0.04 | 0.00 |
| 2 | 8192 | 4 | 64 | 64 | 64 | torch.bfloat16 | 2 | 8192 | 4 | 64 | 64 | 64 | 0.125 | 28.50 | 0.04 | 0.00 |
| 2 | 16384 | 4 | 64 | 64 | 64 | torch.bfloat16 | 2 | 16384 | 4 | 64 | 64 | 64 | 0.125 | 70.09 | 0.03 | 0.00 |

## gla_fwdbwd

### tileops

| batch | seq_len | heads | dim_k | dim_v | chunk_size | dtype | T | B | BC | H | K | V | scale | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 2048 | 4 | 64 | 64 | 64 | torch.float16 | 2048 | 2 | 64 | 4 | 64 | 64 | 0.125 | 0.22 | 1.81 | 0.10 |
| 2 | 4096 | 4 | 64 | 64 | 64 | torch.float16 | 4096 | 2 | 64 | 4 | 64 | 64 | 0.125 | 0.42 | 1.92 | 0.11 |
| 2 | 8192 | 4 | 64 | 64 | 64 | torch.float16 | 8192 | 2 | 64 | 4 | 64 | 64 | 0.125 | 0.78 | 2.07 | 0.12 |
| 2 | 16384 | 4 | 64 | 64 | 64 | torch.float16 | 16384 | 2 | 64 | 4 | 64 | 64 | 0.125 | 1.36 | 2.37 | 0.14 |
| 2 | 2048 | 4 | 64 | 64 | 64 | torch.bfloat16 | 2048 | 2 | 64 | 4 | 64 | 64 | 0.125 | 0.22 | 1.80 | 0.10 |
| 2 | 4096 | 4 | 64 | 64 | 64 | torch.bfloat16 | 4096 | 2 | 64 | 4 | 64 | 64 | 0.125 | 0.42 | 1.91 | 0.11 |
| 2 | 8192 | 4 | 64 | 64 | 64 | torch.bfloat16 | 8192 | 2 | 64 | 4 | 64 | 64 | 0.125 | 0.79 | 2.04 | 0.12 |
| 2 | 16384 | 4 | 64 | 64 | 64 | torch.bfloat16 | 16384 | 2 | 64 | 4 | 64 | 64 | 0.125 | 1.48 | 2.17 | 0.12 |

### baseline

| batch | seq_len | heads | dim_k | dim_v | chunk_size | dtype | T | B | BC | H | K | V | scale | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 2048 | 4 | 64 | 64 | 64 | torch.float16 | 2048 | 2 | 64 | 4 | 64 | 64 | 0.125 | 5.91 | 0.07 | 0.00 |
| 2 | 4096 | 4 | 64 | 64 | 64 | torch.float16 | 4096 | 2 | 64 | 4 | 64 | 64 | 0.125 | 12.43 | 0.06 | 0.00 |
| 2 | 8192 | 4 | 64 | 64 | 64 | torch.float16 | 8192 | 2 | 64 | 4 | 64 | 64 | 0.125 | 28.46 | 0.06 | 0.00 |
| 2 | 16384 | 4 | 64 | 64 | 64 | torch.float16 | 16384 | 2 | 64 | 4 | 64 | 64 | 0.125 | 70.12 | 0.05 | 0.00 |
| 2 | 2048 | 4 | 64 | 64 | 64 | torch.bfloat16 | 2048 | 2 | 64 | 4 | 64 | 64 | 0.125 | 5.92 | 0.07 | 0.00 |
| 2 | 4096 | 4 | 64 | 64 | 64 | torch.bfloat16 | 4096 | 2 | 64 | 4 | 64 | 64 | 0.125 | 12.43 | 0.06 | 0.00 |
| 2 | 8192 | 4 | 64 | 64 | 64 | torch.bfloat16 | 8192 | 2 | 64 | 4 | 64 | 64 | 0.125 | 28.48 | 0.06 | 0.00 |
| 2 | 16384 | 4 | 64 | 64 | 64 | torch.bfloat16 | 16384 | 2 | 64 | 4 | 64 | 64 | 0.125 | 70.11 | 0.05 | 0.00 |

## gla_decode

### tileops

| batch | heads | dim_k | dim_v | dtype | scale | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 32 | 64 | 64 | torch.float32 | 0.125 | 0.01 | 0.07 | 0.14 |
| 1 | 32 | 128 | 128 | torch.float32 | 0.08838834764831845 | 0.02 | 0.13 | 0.26 |
| 1 | 32 | 128 | 128 | torch.float16 | 0.08838834764831845 | 0.01 | 0.17 | 0.17 |
| 1 | 32 | 128 | 128 | torch.bfloat16 | 0.08838834764831845 | 0.01 | 0.17 | 0.17 |
| 8 | 32 | 128 | 128 | torch.float32 | 0.08838834764831845 | 0.03 | 0.50 | 1.01 |
| 8 | 32 | 128 | 128 | torch.float16 | 0.08838834764831845 | 0.01 | 1.20 | 1.22 |
| 8 | 32 | 128 | 128 | torch.bfloat16 | 0.08838834764831845 | 0.01 | 1.19 | 1.20 |
| 16 | 32 | 128 | 128 | torch.float32 | 0.08838834764831845 | 0.06 | 0.52 | 1.06 |
| 16 | 32 | 128 | 128 | torch.float16 | 0.08838834764831845 | 0.02 | 1.87 | 1.90 |
| 16 | 32 | 128 | 128 | torch.bfloat16 | 0.08838834764831845 | 0.02 | 1.85 | 1.88 |
| 32 | 32 | 128 | 128 | torch.float32 | 0.08838834764831845 | 0.12 | 0.55 | 1.11 |
| 32 | 32 | 128 | 128 | torch.float16 | 0.08838834764831845 | 0.03 | 1.95 | 1.99 |
| 32 | 32 | 128 | 128 | torch.bfloat16 | 0.08838834764831845 | 0.03 | 1.94 | 1.97 |
| 64 | 32 | 128 | 128 | torch.float32 | 0.08838834764831845 | 0.24 | 0.55 | 1.12 |
| 64 | 32 | 128 | 128 | torch.float16 | 0.08838834764831845 | 0.06 | 2.18 | 2.22 |
| 64 | 32 | 128 | 128 | torch.bfloat16 | 0.08838834764831845 | 0.06 | 2.16 | 2.20 |

### baseline

| batch | heads | dim_k | dim_v | dtype | scale | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 32 | 64 | 64 | torch.float32 | 0.125 | 0.01 | 0.04 | 0.08 |
| 1 | 32 | 128 | 128 | torch.float32 | 0.08838834764831845 | 0.02 | 0.13 | 0.26 |
| 1 | 32 | 128 | 128 | torch.float16 | 0.08838834764831845 | 0.04 | 0.06 | 0.06 |
| 1 | 32 | 128 | 128 | torch.bfloat16 | 0.08838834764831845 | 0.04 | 0.06 | 0.06 |
| 8 | 32 | 128 | 128 | torch.float32 | 0.08838834764831845 | 0.05 | 0.32 | 0.66 |
| 8 | 32 | 128 | 128 | torch.float16 | 0.08838834764831845 | 0.09 | 0.20 | 0.20 |
| 8 | 32 | 128 | 128 | torch.bfloat16 | 0.08838834764831845 | 0.09 | 0.20 | 0.20 |
| 16 | 32 | 128 | 128 | torch.float32 | 0.08838834764831845 | 0.09 | 0.36 | 0.74 |
| 16 | 32 | 128 | 128 | torch.float16 | 0.08838834764831845 | 0.15 | 0.23 | 0.23 |
| 16 | 32 | 128 | 128 | torch.bfloat16 | 0.08838834764831845 | 0.15 | 0.23 | 0.23 |
| 32 | 32 | 128 | 128 | torch.float32 | 0.08838834764831845 | 0.17 | 0.39 | 0.78 |
| 32 | 32 | 128 | 128 | torch.float16 | 0.08838834764831845 | 0.27 | 0.25 | 0.26 |
| 32 | 32 | 128 | 128 | torch.bfloat16 | 0.08838834764831845 | 0.27 | 0.25 | 0.25 |
| 64 | 32 | 128 | 128 | torch.float32 | 0.08838834764831845 | 0.33 | 0.41 | 0.83 |
| 64 | 32 | 128 | 128 | torch.float16 | 0.08838834764831845 | 0.50 | 0.27 | 0.28 |
| 64 | 32 | 128 | 128 | torch.bfloat16 | 0.08838834764831845 | 0.50 | 0.27 | 0.27 |

## gqa_fwd

### tileops

| batch | seq_len | heads | heads_kv | dim | causal | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1024 | 8 | 4 | 64 | False | torch.float16 | 139.64 | 0.02 | 0.00 |
| 4 | 2048 | 64 | 4 | 128 | False | torch.float16 | 143.00 | 3.84 | 0.00 |
| 4 | 2048 | 64 | 4 | 128 | False | torch.bfloat16 | 139.75 | 3.93 | 0.00 |

## gqa_bwd

### tileops

| batch | seq_len | heads | heads_kv | dim | causal | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1024 | 8 | 4 | 64 | False | torch.float16 | 0.05 | 102.25 | 0.10 |
| 4 | 2048 | 64 | 4 | 128 | False | torch.float16 | 3.34 | 411.88 | 0.13 |
| 4 | 2048 | 64 | 4 | 128 | False | torch.bfloat16 | 3.24 | 423.84 | 0.13 |

## gqa_decode

### tileops

| batch | heads | heads_kv | seq_len_kv | dim | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 32 | 8 | 8192 | 128 | torch.float16 | 334.27 | 0.00 | 0.00 |
| 4 | 32 | 4 | 4096 | 128 | torch.bfloat16 | 0.04 | 6.78 | 0.85 |
| 8 | 64 | 16 | 8192 | 128 | torch.float16 | 332.71 | 0.01 | 0.00 |

### baseline

| batch | heads | heads_kv | seq_len_kv | dim | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 32 | 8 | 8192 | 128 | torch.float16 | 0.43 | 0.31 | 0.08 |
| 4 | 32 | 4 | 4096 | 128 | torch.bfloat16 | 0.81 | 0.33 | 0.04 |
| 8 | 64 | 16 | 8192 | 128 | torch.float16 | 5.63 | 0.38 | 0.10 |

## gqa_decode_paged

### tileops

| batch | heads | heads_kv | seqlen_kv | dim | page_size | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 16 | 8 | 512 | 128 | 128 | torch.float16 | 364.79 | 0.00 | 0.00 |
| 2 | 8 | 4 | 1024 | 64 | 256 | torch.float16 | 367.59 | 0.00 | 0.00 |
| 1 | 16 | 4 | 2048 | 128 | 512 | torch.float16 | 367.13 | 0.00 | 0.00 |
| 1 | 32 | 16 | 512 | 64 | 128 | torch.float16 | 365.90 | 0.00 | 0.00 |

### baseline

| batch | heads | heads_kv | seqlen_kv | dim | page_size | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 16 | 8 | 512 | 128 | 128 | torch.float16 | 0.07 | 0.06 | 0.03 |
| 2 | 8 | 4 | 1024 | 64 | 256 | torch.float16 | 0.13 | 0.03 | 0.01 |
| 1 | 16 | 4 | 2048 | 128 | 512 | torch.float16 | 0.07 | 0.25 | 0.06 |
| 1 | 32 | 16 | 512 | 64 | 128 | torch.float16 | 0.07 | 0.06 | 0.03 |

## gqa_sliding_window_fwd

### tileops

| batch | seq | heads | heads_kv | dim | is_causal | wl | wr | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 512 | 8 | 2 | 64 | True | -1 | -1 | torch.float16 | 209.62 | 0.00 | 0.00 |
| 2 | 512 | 8 | 2 | 64 | True | 128 | -1 | torch.float16 | 188.77 | 0.00 | 0.00 |
| 2 | 768 | 8 | 2 | 64 | False | 256 | -1 | torch.float16 | 188.34 | 0.01 | 0.00 |
| 2 | 512 | 8 | 2 | 64 | False | 64 | 64 | torch.bfloat16 | 188.80 | 0.00 | 0.00 |
| 1 | 2048 | 8 | 2 | 64 | True | 512 | -1 | torch.float16 | 189.15 | 0.01 | 0.00 |

## gqa_sliding_window_varlen_fwd

### tileops

| batch | heads | heads_kv | dim | is_causal | wl | wr | dtype | max_seqlen_q | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 32 | 8 | 128 | True | -1 | -1 | torch.float16 | 3000 | 0.21 | 345.86 | 0.29 |
| 2 | 32 | 8 | 128 | True | 2000 | -1 | torch.float16 | 3073 | 0.34 | 254.66 | 0.28 |
| 4 | 32 | 8 | 128 | False | 1500 | 1500 | torch.float16 | 3500 | 0.92 | 375.44 | 0.22 |
| 2 | 32 | 8 | 128 | True | -1 | -1 | torch.float16 | 1024 | 0.39 | 409.01 | 0.19 |
| 2 | 32 | 8 | 128 | True | -1 | -1 | torch.float16 | 8193 | 1.86 | 406.60 | 0.15 |

## group_norm

### tileops

| n | c | g | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 8 | 128 | 32 | torch.float16 | 85.31 | 0.00 | 0.00 |
| 8 | 128 | 32 | torch.bfloat16 | 85.44 | 0.00 | 0.00 |
| 4 | 256 | 32 | torch.float16 | 85.67 | 0.00 | 0.00 |
| 4 | 128 | 16 | torch.float16 | 85.75 | 0.00 | 0.00 |

### baseline

| n | c | g | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 8 | 128 | 32 | torch.float16 | 0.01 | 0.36 | 0.29 |
| 8 | 128 | 32 | torch.bfloat16 | 0.01 | 0.35 | 0.28 |
| 4 | 256 | 32 | torch.float16 | 0.02 | 0.25 | 0.20 |
| 4 | 128 | 16 | torch.float16 | 0.02 | 0.15 | 0.12 |

## grouped_gemm_nt

### tileops

| name | batch_sum | batch_count | N | K | dtype | transpose_a | transpose_b | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| grouped_gemm_nt | 16384 | 4 | 4864 | 4096 | torch.float16 | False | True | 124.74 | 5.23 | 0.00 |

### baseline

| name | batch_sum | batch_count | N | K | dtype | transpose_a | transpose_b | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| grouped_gemm_nt | 16384 | 4 | 4864 | 4096 | torch.float16 | False | True | 1.51 | 433.36 | 0.30 |

## grouped_gemm_nn

### tileops

| name | batch_sum | batch_count | N | K | dtype | transpose_a | transpose_b | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| grouped_gemm_nn | 16384 | 4 | 4864 | 4096 | torch.float16 | False | False | 125.01 | 5.22 | 0.00 |

### baseline

| name | batch_sum | batch_count | N | K | dtype | transpose_a | transpose_b | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| grouped_gemm_nn | 16384 | 4 | 4864 | 4096 | torch.float16 | False | False | 1.02 | 638.40 | 0.44 |

## grouped_gemm_tn

### tileops

| name | batch_sum | batch_count | N | K | dtype | transpose_a | transpose_b | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| grouped_gemm_tn | 16384 | 4 | 4864 | 4096 | torch.float16 | True | False | 122.26 | 5.34 | 0.00 |

### baseline

| name | batch_sum | batch_count | N | K | dtype | transpose_a | transpose_b | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| grouped_gemm_tn | 16384 | 4 | 4864 | 4096 | torch.float16 | True | False | 0.99 | 656.56 | 0.46 |

## grouped_gemm_tt

### tileops

| name | batch_sum | batch_count | N | K | dtype | transpose_a | transpose_b | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| grouped_gemm_tt | 16384 | 4 | 4864 | 4096 | torch.float16 | True | True | 122.49 | 5.33 | 0.00 |

### baseline

| name | batch_sum | batch_count | N | K | dtype | transpose_a | transpose_b | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| grouped_gemm_tt | 16384 | 4 | 4864 | 4096 | torch.float16 | True | True | 1.00 | 653.30 | 0.45 |

## grouped_gemm_complete

### tileops

| batch_sum | batch_count | N | K | dtype | transpose_a | transpose_b | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 16384 | 4 | 4864 | 4096 | torch.float16 | True | False | 575.59 | 3.40 | N/A |

### baseline

| batch_sum | batch_count | N | K | dtype | transpose_a | transpose_b | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 16384 | 4 | 4864 | 4096 | torch.float16 | True | False | 4.54 | 431.51 | N/A |

## leaky_relu

### tileops

| op_name | dtype | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| leaky_relu | torch.float16 | 4194304 | 0.01 | 0.69 | 2.76 |
| leaky_relu | torch.bfloat16 | 4194304 | 0.01 | 0.69 | 2.76 |
| leaky_relu | torch.float32 | 4194304 | 0.01 | 0.40 | 3.18 |
| leaky_relu | torch.float16 | 10485760 | 0.01 | 0.82 | 3.29 |
| leaky_relu | torch.bfloat16 | 10485760 | 0.01 | 0.82 | 3.29 |
| leaky_relu | torch.float32 | 10485760 | 0.02 | 0.48 | 3.83 |
| leaky_relu | torch.float16 | 20971520 | 0.02 | 0.92 | 3.67 |
| leaky_relu | torch.bfloat16 | 20971520 | 0.02 | 0.91 | 3.66 |
| leaky_relu | torch.float32 | 20971520 | 0.04 | 0.52 | 4.12 |

### baseline

| op_name | dtype | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| leaky_relu | torch.float16 | 4194304 | 0.01 | 0.66 | 2.62 |
| leaky_relu | torch.bfloat16 | 4194304 | 0.01 | 0.65 | 2.62 |
| leaky_relu | torch.float32 | 4194304 | 0.01 | 0.40 | 3.19 |
| leaky_relu | torch.float16 | 10485760 | 0.01 | 0.84 | 3.37 |
| leaky_relu | torch.bfloat16 | 10485760 | 0.01 | 0.84 | 3.36 |
| leaky_relu | torch.float32 | 10485760 | 0.02 | 0.47 | 3.78 |
| leaky_relu | torch.float16 | 20971520 | 0.02 | 0.95 | 3.82 |
| leaky_relu | torch.bfloat16 | 20971520 | 0.02 | 0.95 | 3.82 |
| leaky_relu | torch.float32 | 20971520 | 0.04 | 0.51 | 4.07 |

## elu

### tileops

| op_name | dtype | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| elu | torch.float16 | 4194304 | 0.01 | 0.38 | 1.50 |
| elu | torch.bfloat16 | 4194304 | 0.01 | 0.38 | 1.53 |
| elu | torch.float32 | 4194304 | 0.01 | 0.31 | 2.49 |
| elu | torch.float16 | 10485760 | 0.02 | 0.45 | 1.80 |
| elu | torch.bfloat16 | 10485760 | 0.02 | 0.46 | 1.82 |
| elu | torch.float32 | 10485760 | 0.03 | 0.36 | 2.90 |
| elu | torch.float16 | 20971520 | 0.04 | 0.48 | 1.94 |
| elu | torch.bfloat16 | 20971520 | 0.04 | 0.49 | 1.97 |
| elu | torch.float32 | 20971520 | 0.05 | 0.38 | 3.06 |

### baseline

| op_name | dtype | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| elu | torch.float16 | 4194304 | 0.01 | 0.43 | 1.71 |
| elu | torch.bfloat16 | 4194304 | 0.01 | 0.42 | 1.69 |
| elu | torch.float32 | 4194304 | 0.01 | 0.37 | 2.99 |
| elu | torch.float16 | 10485760 | 0.02 | 0.52 | 2.09 |
| elu | torch.bfloat16 | 10485760 | 0.02 | 0.51 | 2.06 |
| elu | torch.float32 | 10485760 | 0.02 | 0.46 | 3.68 |
| elu | torch.float16 | 20971520 | 0.04 | 0.57 | 2.29 |
| elu | torch.bfloat16 | 20971520 | 0.04 | 0.57 | 2.26 |
| elu | torch.float32 | 20971520 | 0.04 | 0.50 | 4.02 |

## hardtanh

### tileops

| op_name | dtype | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| hardtanh | torch.float16 | 4194304 | 0.01 | 0.66 | 2.63 |
| hardtanh | torch.bfloat16 | 4194304 | 0.01 | 0.66 | 2.64 |
| hardtanh | torch.float32 | 4194304 | 0.01 | 0.40 | 3.18 |
| hardtanh | torch.float16 | 10485760 | 0.01 | 0.85 | 3.40 |
| hardtanh | torch.bfloat16 | 10485760 | 0.01 | 0.85 | 3.40 |
| hardtanh | torch.float32 | 10485760 | 0.02 | 0.48 | 3.82 |
| hardtanh | torch.float16 | 20971520 | 0.02 | 0.96 | 3.82 |
| hardtanh | torch.bfloat16 | 20971520 | 0.02 | 0.95 | 3.81 |
| hardtanh | torch.float32 | 20971520 | 0.04 | 0.52 | 4.14 |

### baseline

| op_name | dtype | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| hardtanh | torch.float16 | 4194304 | 0.01 | 0.63 | 2.50 |
| hardtanh | torch.bfloat16 | 4194304 | 0.01 | 0.65 | 2.58 |
| hardtanh | torch.float32 | 4194304 | 0.01 | 0.40 | 3.17 |
| hardtanh | torch.float16 | 10485760 | 0.01 | 0.79 | 3.15 |
| hardtanh | torch.bfloat16 | 10485760 | 0.01 | 0.83 | 3.33 |
| hardtanh | torch.float32 | 10485760 | 0.02 | 0.47 | 3.77 |
| hardtanh | torch.float16 | 20971520 | 0.02 | 0.88 | 3.52 |
| hardtanh | torch.bfloat16 | 20971520 | 0.02 | 0.95 | 3.78 |
| hardtanh | torch.float32 | 20971520 | 0.04 | 0.51 | 4.07 |

## softplus

### tileops

| op_name | dtype | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| softplus | torch.float16 | 4194304 | 0.01 | 0.32 | 1.29 |
| softplus | torch.bfloat16 | 4194304 | 0.01 | 0.32 | 1.29 |
| softplus | torch.float32 | 4194304 | 0.01 | 0.37 | 2.97 |
| softplus | torch.float16 | 10485760 | 0.03 | 0.38 | 1.50 |
| softplus | torch.bfloat16 | 10485760 | 0.03 | 0.37 | 1.49 |
| softplus | torch.float32 | 10485760 | 0.02 | 0.44 | 3.50 |
| softplus | torch.float16 | 20971520 | 0.05 | 0.40 | 1.61 |
| softplus | torch.bfloat16 | 20971520 | 0.05 | 0.40 | 1.61 |
| softplus | torch.float32 | 20971520 | 0.05 | 0.46 | 3.72 |

### baseline

| op_name | dtype | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| softplus | torch.float16 | 4194304 | 0.01 | 0.36 | 1.44 |
| softplus | torch.bfloat16 | 4194304 | 0.01 | 0.36 | 1.43 |
| softplus | torch.float32 | 4194304 | 0.01 | 0.34 | 2.71 |
| softplus | torch.float16 | 10485760 | 0.02 | 0.43 | 1.72 |
| softplus | torch.bfloat16 | 10485760 | 0.02 | 0.43 | 1.71 |
| softplus | torch.float32 | 10485760 | 0.03 | 0.42 | 3.34 |
| softplus | torch.float16 | 20971520 | 0.04 | 0.47 | 1.87 |
| softplus | torch.bfloat16 | 20971520 | 0.05 | 0.46 | 1.85 |
| softplus | torch.float32 | 20971520 | 0.05 | 0.45 | 3.63 |

## clamp

### tileops

| op_name | dtype | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| clamp | torch.float16 | 4194304 | 0.01 | 0.66 | 2.65 |
| clamp | torch.bfloat16 | 4194304 | 0.01 | 0.66 | 2.63 |
| clamp | torch.float32 | 4194304 | 0.01 | 0.40 | 3.17 |
| clamp | torch.float16 | 10485760 | 0.01 | 0.85 | 3.40 |
| clamp | torch.bfloat16 | 10485760 | 0.01 | 0.85 | 3.38 |
| clamp | torch.float32 | 10485760 | 0.02 | 0.48 | 3.82 |
| clamp | torch.float16 | 20971520 | 0.02 | 0.96 | 3.84 |
| clamp | torch.bfloat16 | 20971520 | 0.02 | 0.96 | 3.85 |
| clamp | torch.float32 | 20971520 | 0.04 | 0.52 | 4.12 |

### baseline

| op_name | dtype | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| clamp | torch.float16 | 4194304 | 0.01 | 0.63 | 2.51 |
| clamp | torch.bfloat16 | 4194304 | 0.01 | 0.65 | 2.59 |
| clamp | torch.float32 | 4194304 | 0.01 | 0.40 | 3.18 |
| clamp | torch.float16 | 10485760 | 0.01 | 0.79 | 3.16 |
| clamp | torch.bfloat16 | 10485760 | 0.01 | 0.83 | 3.34 |
| clamp | torch.float32 | 10485760 | 0.02 | 0.47 | 3.77 |
| clamp | torch.float16 | 20971520 | 0.02 | 0.88 | 3.52 |
| clamp | torch.bfloat16 | 20971520 | 0.02 | 0.95 | 3.79 |
| clamp | torch.float32 | 20971520 | 0.04 | 0.51 | 4.08 |

## nan_to_num

### tileops

| op_name | dtype | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| nan_to_num | torch.float16 | 4194304 | 0.01 | 0.66 | 2.64 |
| nan_to_num | torch.bfloat16 | 4194304 | 0.01 | 0.66 | 2.63 |
| nan_to_num | torch.float32 | 4194304 | 0.01 | 0.40 | 3.18 |
| nan_to_num | torch.float16 | 10485760 | 0.01 | 0.80 | 3.19 |
| nan_to_num | torch.bfloat16 | 10485760 | 0.01 | 0.80 | 3.20 |
| nan_to_num | torch.float32 | 10485760 | 0.02 | 0.48 | 3.83 |
| nan_to_num | torch.float16 | 20971520 | 0.02 | 0.90 | 3.61 |
| nan_to_num | torch.bfloat16 | 20971520 | 0.02 | 0.90 | 3.61 |
| nan_to_num | torch.float32 | 20971520 | 0.04 | 0.52 | 4.13 |

### baseline

| op_name | dtype | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| nan_to_num | torch.float16 | 4194304 | 0.01 | 0.64 | 2.55 |
| nan_to_num | torch.bfloat16 | 4194304 | 0.01 | 0.64 | 2.55 |
| nan_to_num | torch.float32 | 4194304 | 0.01 | 0.40 | 3.19 |
| nan_to_num | torch.float16 | 10485760 | 0.01 | 0.83 | 3.30 |
| nan_to_num | torch.bfloat16 | 10485760 | 0.01 | 0.83 | 3.30 |
| nan_to_num | torch.float32 | 10485760 | 0.02 | 0.47 | 3.78 |
| nan_to_num | torch.float16 | 20971520 | 0.02 | 0.94 | 3.76 |
| nan_to_num | torch.bfloat16 | 20971520 | 0.02 | 0.94 | 3.75 |
| nan_to_num | torch.float32 | 20971520 | 0.04 | 0.51 | 4.09 |

## prelu

### tileops

| num_channels | dtype | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| 128 | torch.float16 | 131072 | 0.00 | 0.06 | 0.25 |
| 128 | torch.bfloat16 | 131072 | 0.00 | 0.06 | 0.25 |
| 128 | torch.float32 | 131072 | 0.00 | 0.06 | 0.46 |
| 4096 | torch.float16 | 4194304 | 0.01 | 0.68 | 2.74 |
| 4096 | torch.bfloat16 | 4194304 | 0.01 | 0.68 | 2.74 |
| 4096 | torch.float32 | 4194304 | 0.01 | 0.40 | 3.20 |
| 10240 | torch.float16 | 10485760 | 0.01 | 0.82 | 3.27 |
| 10240 | torch.bfloat16 | 10485760 | 0.01 | 0.82 | 3.28 |
| 10240 | torch.float32 | 10485760 | 0.02 | 0.47 | 3.79 |
| 20480 | torch.float16 | 20971520 | 0.02 | 0.92 | 3.67 |
| 20480 | torch.bfloat16 | 20971520 | 0.02 | 0.92 | 3.67 |
| 20480 | torch.float32 | 20971520 | 0.04 | 0.51 | 4.08 |

### baseline

| num_channels | dtype | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| 128 | torch.float16 | 131072 | 0.00 | 0.03 | 0.12 |
| 128 | torch.bfloat16 | 131072 | 0.00 | 0.03 | 0.12 |
| 128 | torch.float32 | 131072 | 0.00 | 0.04 | 0.29 |
| 4096 | torch.float16 | 4194304 | 0.01 | 0.29 | 1.16 |
| 4096 | torch.bfloat16 | 4194304 | 0.01 | 0.28 | 1.14 |
| 4096 | torch.float32 | 4194304 | 0.02 | 0.25 | 2.04 |
| 10240 | torch.float16 | 10485760 | 0.03 | 0.34 | 1.36 |
| 10240 | torch.bfloat16 | 10485760 | 0.03 | 0.34 | 1.34 |
| 10240 | torch.float32 | 10485760 | 0.04 | 0.30 | 2.37 |
| 20480 | torch.float16 | 20971520 | 0.06 | 0.37 | 1.47 |
| 20480 | torch.bfloat16 | 20971520 | 0.06 | 0.36 | 1.46 |
| 20480 | torch.float32 | 20971520 | 0.07 | 0.31 | 2.49 |

## where

### tileops

| dtype | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| torch.float16 | 4194304 | 0.01 | 0.41 | 2.87 |
| torch.bfloat16 | 4194304 | 0.01 | 0.41 | 2.87 |
| torch.float32 | 4194304 | 0.02 | 0.26 | 3.33 |
| torch.float16 | 10485760 | 0.02 | 0.50 | 3.49 |
| torch.bfloat16 | 10485760 | 0.02 | 0.50 | 3.49 |
| torch.float32 | 10485760 | 0.03 | 0.30 | 3.90 |
| torch.float16 | 20971520 | 0.04 | 0.56 | 3.92 |
| torch.bfloat16 | 20971520 | 0.04 | 0.56 | 3.93 |
| torch.float32 | 20971520 | 0.06 | 0.33 | 4.25 |

### baseline

| dtype | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| torch.float16 | 4194304 | 0.01 | 0.42 | 2.91 |
| torch.bfloat16 | 4194304 | 0.01 | 0.42 | 2.91 |
| torch.float32 | 4194304 | 0.02 | 0.26 | 3.37 |
| torch.float16 | 10485760 | 0.02 | 0.51 | 3.54 |
| torch.bfloat16 | 10485760 | 0.02 | 0.51 | 3.54 |
| torch.float32 | 10485760 | 0.03 | 0.30 | 3.94 |
| torch.float16 | 20971520 | 0.04 | 0.56 | 3.95 |
| torch.bfloat16 | 20971520 | 0.04 | 0.57 | 3.96 |
| torch.float32 | 20971520 | 0.06 | 0.33 | 4.25 |

## masked_fill

### tileops

| dtype | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| torch.float16 | 4194304 | 0.01 | 0.54 | 2.71 |
| torch.bfloat16 | 4194304 | 0.01 | 0.55 | 2.76 |
| torch.float32 | 4194304 | 0.01 | 0.35 | 3.15 |
| torch.float16 | 10485760 | 0.02 | 0.67 | 3.36 |
| torch.bfloat16 | 10485760 | 0.02 | 0.67 | 3.36 |
| torch.float32 | 10485760 | 0.02 | 0.42 | 3.82 |
| torch.float16 | 20971520 | 0.03 | 0.77 | 3.85 |
| torch.bfloat16 | 20971520 | 0.03 | 0.77 | 3.85 |
| torch.float32 | 20971520 | 0.05 | 0.46 | 4.12 |

### baseline

| dtype | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- |
| torch.float16 | 4194304 | 0.01 | 0.36 | 1.78 |
| torch.bfloat16 | 4194304 | 0.01 | 0.36 | 1.78 |
| torch.float32 | 4194304 | 0.02 | 0.23 | 2.08 |
| torch.float16 | 10485760 | 0.02 | 0.45 | 2.24 |
| torch.bfloat16 | 10485760 | 0.02 | 0.45 | 2.24 |
| torch.float32 | 10485760 | 0.05 | 0.23 | 2.08 |
| torch.float16 | 20971520 | 0.05 | 0.44 | 2.19 |
| torch.bfloat16 | 20971520 | 0.05 | 0.44 | 2.19 |
| torch.float32 | 20971520 | 0.09 | 0.24 | 2.17 |

## alibi

### tileops

| op_name | seq_len | dim | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| alibi | 512 | 64 | torch.float16 | 0.03 | 0.53 | 1.05 |
| alibi | 512 | 64 | torch.bfloat16 | 0.03 | 0.53 | 1.05 |
| alibi | 512 | 64 | torch.float32 | 0.02 | 0.90 | 3.59 |
| alibi | 2048 | 64 | torch.float16 | 0.26 | 1.03 | 2.06 |
| alibi | 2048 | 64 | torch.bfloat16 | 0.29 | 0.93 | 1.86 |
| alibi | 2048 | 64 | torch.float32 | 0.27 | 0.98 | 3.94 |
| alibi | 4096 | 128 | torch.float16 | 0.86 | 2.51 | 5.02 |
| alibi | 4096 | 128 | torch.bfloat16 | 1.09 | 1.96 | 3.93 |
| alibi | 4096 | 128 | torch.float32 | 2.08 | 1.03 | 4.12 |

### baseline

| op_name | seq_len | dim | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| alibi | 512 | 64 | torch.float16 | 0.08 | 0.21 | 0.41 |
| alibi | 512 | 64 | torch.bfloat16 | 0.08 | 0.21 | 0.41 |
| alibi | 512 | 64 | torch.float32 | 0.06 | 0.30 | 1.22 |
| alibi | 2048 | 64 | torch.float16 | 1.00 | 0.27 | 0.54 |
| alibi | 2048 | 64 | torch.bfloat16 | 1.00 | 0.27 | 0.54 |
| alibi | 2048 | 64 | torch.float32 | 0.65 | 0.41 | 1.65 |
| alibi | 4096 | 128 | torch.float16 | 8.62 | 0.25 | 0.50 |
| alibi | 4096 | 128 | torch.bfloat16 | 8.01 | 0.27 | 0.54 |
| alibi | 4096 | 128 | torch.float32 | 5.32 | 0.40 | 1.62 |

## sinusoidal

### tileops

| op_name | seq_len | dim | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| sinusoidal | 512 | 256 | torch.float16 | 0.00 | 0.04 | 0.09 |
| sinusoidal | 512 | 256 | torch.bfloat16 | 0.00 | 0.04 | 0.09 |
| sinusoidal | 512 | 256 | torch.float32 | 0.00 | 0.05 | 0.21 |
| sinusoidal | 2048 | 300 | torch.float16 | 0.00 | 0.15 | 0.30 |
| sinusoidal | 2048 | 300 | torch.bfloat16 | 0.00 | 0.15 | 0.29 |
| sinusoidal | 2048 | 300 | torch.float32 | 0.00 | 0.13 | 0.51 |
| sinusoidal | 4096 | 512 | torch.float16 | 0.01 | 0.30 | 0.61 |
| sinusoidal | 4096 | 512 | torch.bfloat16 | 0.01 | 0.30 | 0.61 |
| sinusoidal | 4096 | 512 | torch.float32 | 0.01 | 0.19 | 0.75 |

### baseline

| op_name | seq_len | dim | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| sinusoidal | 512 | 256 | torch.float16 | 0.02 | 0.01 | 0.01 |
| sinusoidal | 512 | 256 | torch.bfloat16 | 0.02 | 0.01 | 0.01 |
| sinusoidal | 512 | 256 | torch.float32 | 0.02 | 0.01 | 0.03 |
| sinusoidal | 2048 | 300 | torch.float16 | 0.02 | 0.03 | 0.05 |
| sinusoidal | 2048 | 300 | torch.bfloat16 | 0.02 | 0.03 | 0.05 |
| sinusoidal | 2048 | 300 | torch.float32 | 0.02 | 0.03 | 0.12 |
| sinusoidal | 4096 | 512 | torch.float16 | 0.03 | 0.06 | 0.13 |
| sinusoidal | 4096 | 512 | torch.bfloat16 | 0.03 | 0.06 | 0.13 |
| sinusoidal | 4096 | 512 | torch.float32 | 0.03 | 0.07 | 0.29 |

## leaky_relu_fp8

### tileops

| op_name | dtype | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| leaky_relu | torch.float8_e4m3fn | 4194304 | 0.01 | 0.49 | 0.98 |
| leaky_relu | torch.float8_e5m2 | 4194304 | 0.03 | 0.16 | 0.32 |
| leaky_relu | torch.float8_e4m3fn | 10485760 | 0.02 | 0.57 | 1.14 |
| leaky_relu | torch.float8_e5m2 | 10485760 | 0.05 | 0.20 | 0.41 |
| leaky_relu | torch.float8_e4m3fn | 20971520 | 0.03 | 0.62 | 1.24 |
| leaky_relu | torch.float8_e5m2 | 20971520 | 0.10 | 0.22 | 0.44 |

### baseline

| op_name | dtype | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| leaky_relu | torch.float8_e4m3fn | 4194304 | 0.03 | 0.16 | 0.33 |
| leaky_relu | torch.float8_e5m2 | 4194304 | 0.02 | 0.17 | 0.34 |
| leaky_relu | torch.float8_e4m3fn | 10485760 | 0.05 | 0.19 | 0.38 |
| leaky_relu | torch.float8_e5m2 | 10485760 | 0.05 | 0.20 | 0.40 |
| leaky_relu | torch.float8_e4m3fn | 20971520 | 0.11 | 0.19 | 0.38 |
| leaky_relu | torch.float8_e5m2 | 20971520 | 0.11 | 0.20 | 0.39 |

## elu_fp8

### tileops

| op_name | dtype | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| elu | torch.float8_e4m3fn | 4194304 | 0.01 | 0.66 | 1.33 |
| elu | torch.float8_e5m2 | 4194304 | 0.02 | 0.26 | 0.52 |
| elu | torch.float8_e4m3fn | 10485760 | 0.01 | 0.85 | 1.71 |
| elu | torch.float8_e5m2 | 10485760 | 0.03 | 0.31 | 0.62 |
| elu | torch.float8_e4m3fn | 20971520 | 0.02 | 0.95 | 1.91 |
| elu | torch.float8_e5m2 | 20971520 | 0.07 | 0.32 | 0.64 |

### baseline

| op_name | dtype | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| elu | torch.float8_e4m3fn | 4194304 | 0.03 | 0.14 | 0.28 |
| elu | torch.float8_e5m2 | 4194304 | 0.03 | 0.15 | 0.29 |
| elu | torch.float8_e4m3fn | 10485760 | 0.06 | 0.16 | 0.33 |
| elu | torch.float8_e5m2 | 10485760 | 0.06 | 0.17 | 0.34 |
| elu | torch.float8_e4m3fn | 20971520 | 0.13 | 0.17 | 0.33 |
| elu | torch.float8_e5m2 | 20971520 | 0.12 | 0.17 | 0.34 |

## clamp_fp8

### tileops

| op_name | dtype | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| clamp | torch.float8_e4m3fn | 4194304 | 0.00 | 0.99 | 1.97 |
| clamp | torch.float8_e5m2 | 4194304 | 0.01 | 0.39 | 0.79 |
| clamp | torch.float8_e4m3fn | 10485760 | 0.01 | 1.32 | 2.64 |
| clamp | torch.float8_e5m2 | 10485760 | 0.02 | 0.50 | 0.99 |
| clamp | torch.float8_e4m3fn | 20971520 | 0.01 | 1.57 | 3.13 |
| clamp | torch.float8_e5m2 | 20971520 | 0.04 | 0.51 | 1.02 |

### baseline

| op_name | dtype | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| clamp | torch.float8_e4m3fn | 4194304 | 0.03 | 0.16 | 0.32 |
| clamp | torch.float8_e5m2 | 4194304 | 0.03 | 0.17 | 0.33 |
| clamp | torch.float8_e4m3fn | 10485760 | 0.06 | 0.19 | 0.38 |
| clamp | torch.float8_e5m2 | 10485760 | 0.05 | 0.19 | 0.39 |
| clamp | torch.float8_e4m3fn | 20971520 | 0.11 | 0.19 | 0.37 |
| clamp | torch.float8_e5m2 | 20971520 | 0.11 | 0.19 | 0.38 |

## where_fp8

### tileops

| op_name | dtype | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| where | torch.float8_e4m3fn | 4194304 | 0.01 | 0.51 | 2.03 |
| where | torch.float8_e5m2 | 4194304 | 0.01 | 0.51 | 2.03 |
| where | torch.float8_e4m3fn | 10485760 | 0.02 | 0.58 | 2.33 |
| where | torch.float8_e5m2 | 10485760 | 0.02 | 0.58 | 2.33 |
| where | torch.float8_e4m3fn | 20971520 | 0.03 | 0.65 | 2.58 |
| where | torch.float8_e5m2 | 20971520 | 0.03 | 0.65 | 2.59 |

### baseline

| op_name | dtype | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| where | torch.float8_e4m3fn | 4194304 | 0.01 | 0.59 | 2.37 |
| where | torch.float8_e5m2 | 4194304 | 0.01 | 0.59 | 2.37 |
| where | torch.float8_e4m3fn | 10485760 | 0.01 | 0.75 | 3.00 |
| where | torch.float8_e5m2 | 10485760 | 0.01 | 0.75 | 3.00 |
| where | torch.float8_e4m3fn | 20971520 | 0.02 | 0.86 | 3.43 |
| where | torch.float8_e5m2 | 20971520 | 0.02 | 0.85 | 3.41 |

## masked_fill_fp8

### tileops

| op_name | dtype | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| masked_fill | torch.float8_e4m3fn | 4194304 | 0.01 | 0.58 | 1.74 |
| masked_fill | torch.float8_e5m2 | 4194304 | 0.01 | 0.32 | 0.96 |
| masked_fill | torch.float8_e4m3fn | 10485760 | 0.01 | 0.75 | 2.26 |
| masked_fill | torch.float8_e5m2 | 10485760 | 0.03 | 0.40 | 1.20 |
| masked_fill | torch.float8_e4m3fn | 20971520 | 0.03 | 0.83 | 2.48 |
| masked_fill | torch.float8_e5m2 | 20971520 | 0.05 | 0.41 | 1.24 |

### baseline

| op_name | dtype | n_total | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| masked_fill | torch.float8_e4m3fn | 4194304 | 0.03 | 0.14 | 0.41 |
| masked_fill | torch.float8_e5m2 | 4194304 | 0.03 | 0.14 | 0.42 |
| masked_fill | torch.float8_e4m3fn | 10485760 | 0.07 | 0.16 | 0.48 |
| masked_fill | torch.float8_e5m2 | 10485760 | 0.06 | 0.16 | 0.49 |
| masked_fill | torch.float8_e4m3fn | 20971520 | 0.14 | 0.15 | 0.46 |
| masked_fill | torch.float8_e5m2 | 20971520 | 0.13 | 0.16 | 0.47 |

## instance_norm

### tileops

| n | c | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| 8 | 128 | torch.float16 | 85.02 | 0.00 | 0.00 |
| 8 | 128 | torch.bfloat16 | 85.16 | 0.00 | 0.00 |
| 4 | 256 | torch.float16 | 85.49 | 0.00 | 0.00 |
| 4 | 64 | torch.float16 | 84.60 | 0.00 | 0.00 |

### baseline

| n | c | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| 8 | 128 | torch.float16 | 0.02 | 0.25 | 0.20 |
| 8 | 128 | torch.bfloat16 | 0.02 | 0.25 | 0.20 |
| 4 | 256 | torch.float16 | 0.02 | 0.19 | 0.16 |
| 4 | 64 | torch.float16 | 0.01 | 0.09 | 0.07 |

## layer_norm

### tileops

| m | n | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| 1024 | 4096 | torch.float16 | 84.43 | 0.00 | 0.00 |
| 4096 | 4096 | torch.bfloat16 | 84.95 | 0.00 | 0.00 |
| 2048 | 5120 | torch.float16 | 83.96 | 0.00 | 0.00 |
| 1025 | 4096 | torch.float16 | 84.65 | 0.00 | 0.00 |

### baseline

| m | n | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| 1024 | 4096 | torch.float16 | 0.01 | 1.65 | 1.32 |
| 4096 | 4096 | torch.bfloat16 | 0.03 | 2.59 | 2.07 |
| 2048 | 5120 | torch.float16 | 0.02 | 2.35 | 1.88 |
| 1025 | 4096 | torch.float16 | 0.01 | 1.65 | 1.32 |

## logical_reduce

### tileops

| m | n | dtype | op_kind | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 1024 | 4096 | torch.float16 | any | 54.61 | 0.00 | 0.00 |
| 1024 | 4096 | torch.bfloat16 | any | 54.33 | 0.00 | 0.00 |
| 1024 | 4096 | torch.float32 | any | 54.73 | 0.00 | 0.00 |
| 1024 | 4096 | torch.int32 | any | 54.55 | 0.00 | 0.00 |
| 4096 | 4096 | torch.float16 | any | 54.22 | 0.00 | 0.00 |
| 1024 | 4096 | torch.float16 | all | 54.65 | 0.00 | 0.00 |
| 1024 | 4096 | torch.bfloat16 | all | 54.29 | 0.00 | 0.00 |
| 1024 | 4096 | torch.float32 | all | 54.32 | 0.00 | 0.00 |
| 1024 | 4096 | torch.int32 | all | 54.35 | 0.00 | 0.00 |
| 4096 | 4096 | torch.float16 | all | 54.35 | 0.00 | 0.00 |
| 1024 | 4096 | torch.float16 | count_nonzero | 51.53 | 0.00 | 0.00 |
| 1024 | 4096 | torch.bfloat16 | count_nonzero | 51.82 | 0.00 | 0.00 |
| 1024 | 4096 | torch.float32 | count_nonzero | 51.57 | 0.00 | 0.00 |
| 1024 | 4096 | torch.int32 | count_nonzero | 51.66 | 0.00 | 0.00 |
| 4096 | 4096 | torch.float16 | count_nonzero | 51.89 | 0.00 | 0.00 |

### baseline

| m | n | dtype | op_kind | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 1024 | 4096 | torch.float16 | any | 0.03 | 0.16 | 0.32 |
| 1024 | 4096 | torch.bfloat16 | any | 0.03 | 0.16 | 0.32 |
| 1024 | 4096 | torch.float32 | any | 0.03 | 0.16 | 0.62 |
| 1024 | 4096 | torch.int32 | any | 0.03 | 0.16 | 0.62 |
| 4096 | 4096 | torch.float16 | any | 0.07 | 0.25 | 0.51 |
| 1024 | 4096 | torch.float16 | all | 0.03 | 0.16 | 0.33 |
| 1024 | 4096 | torch.bfloat16 | all | 0.03 | 0.16 | 0.33 |
| 1024 | 4096 | torch.float32 | all | 0.03 | 0.16 | 0.64 |
| 1024 | 4096 | torch.int32 | all | 0.03 | 0.16 | 0.64 |
| 4096 | 4096 | torch.float16 | all | 0.07 | 0.26 | 0.51 |
| 1024 | 4096 | torch.float16 | count_nonzero | 0.03 | 0.12 | 0.25 |
| 1024 | 4096 | torch.bfloat16 | count_nonzero | 0.03 | 0.12 | 0.25 |
| 1024 | 4096 | torch.float32 | count_nonzero | 0.04 | 0.11 | 0.46 |
| 1024 | 4096 | torch.int32 | count_nonzero | 0.04 | 0.11 | 0.45 |
| 4096 | 4096 | torch.float16 | count_nonzero | 0.11 | 0.15 | 0.31 |

## mean_pooling

### tileops

| batch_size | seq_len | heads | dim | chunk_size | dtype | accum_dtype | chunks_per_bacth | seq_num | use_offsets | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 8192 | 64 | 128 | 64 | torch.float16 | torch.float32 | 128 | 1 | 0 | 59.11 | 0.00 | 0.00 |
| 2 | 2048 | 64 | 128 | 64 | torch.float16 | torch.float32 | 32 | 2 | 0 | 58.91 | 0.00 | 0.00 |
| 1 | 8192 | 64 | 128 | 64 | torch.float16 | torch.float32 | 128 | 4 | 1 | 59.56 | 0.00 | 0.00 |
| 1 | 1000 | 64 | 128 | 32 | torch.float16 | torch.float32 | 34 | 4 | 1 | 59.33 | 0.00 | 0.00 |

### baseline

| batch_size | seq_len | heads | dim | chunk_size | dtype | accum_dtype | chunks_per_bacth | seq_num | use_offsets | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 8192 | 64 | 128 | 64 | torch.float16 | torch.float32 | 128 | 1 | 0 | 0.77 | 0.09 | 0.18 |
| 2 | 2048 | 64 | 128 | 64 | torch.float16 | torch.float32 | 32 | 2 | 0 | 0.27 | 0.12 | 0.25 |
| 1 | 8192 | 64 | 128 | 64 | torch.float16 | torch.float32 | 128 | 4 | 1 | 0.80 | 0.08 | 0.17 |
| 1 | 1000 | 64 | 128 | 32 | torch.float16 | torch.float32 | 34 | 4 | 1 | 0.27 | 0.03 | 0.06 |

## mha_fwd

### tileops

| batch | seq_len | heads | dim | causal | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1024 | 8 | 64 | False | torch.float16 | 140.18 | 0.02 | 0.00 |
| 16 | 2048 | 16 | 128 | False | torch.float16 | 139.68 | 3.94 | 0.00 |
| 4 | 4096 | 16 | 128 | False | torch.bfloat16 | 140.19 | 3.92 | 0.00 |

## mha_bwd

### tileops

| batch | seq_len | heads | dim | causal | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1024 | 8 | 64 | False | torch.float16 | 0.04 | 123.50 | 0.17 |
| 16 | 2048 | 16 | 128 | False | torch.float16 | 2.93 | 469.72 | 0.32 |
| 4 | 4096 | 16 | 128 | False | torch.bfloat16 | 2.53 | 543.57 | 0.19 |

## mha_decode

### tileops

| b | h | s_q | s_kv | d | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 32 | 128 | 8192 | 128 | torch.float16 | 0.06 | 294.17 | 2.33 |
| 1 | 32 | 128 | 8192 | 128 | torch.bfloat16 | 490.68 | 0.04 | 0.00 |
| 1 | 32 | 128 | 5 | 128 | torch.float16 | 399.20 | 0.00 | 0.00 |

### baseline

| b | h | s_q | s_kv | d | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 32 | 128 | 8192 | 128 | torch.float16 | 0.07 | 258.20 | 2.05 |
| 1 | 32 | 128 | 8192 | 128 | torch.bfloat16 | 0.07 | 261.47 | 2.07 |
| 1 | 32 | 128 | 5 | 128 | torch.float16 | 0.01 | 1.49 | 0.31 |

## mha_decode_paged

### tileops

| batch | heads | seqlen_q | seqlen_kv | dim | page_size | is_causal | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 16 | 1 | 512 | 128 | 128 | False | torch.float16 | 447.76 | 0.00 | 0.00 |
| 2 | 8 | 1 | 1024 | 64 | 256 | False | torch.float16 | 449.74 | 0.00 | 0.00 |
| 1 | 8 | 1 | 1024 | 64 | 256 | False | torch.float16 | 449.18 | 0.00 | 0.00 |
| 1 | 8 | 1 | 512 | 64 | 256 | False | torch.float16 | 450.33 | 0.00 | 0.00 |

### baseline

| batch | heads | seqlen_q | seqlen_kv | dim | page_size | is_causal | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 16 | 1 | 512 | 128 | 128 | False | torch.float16 | 0.04 | 0.10 | 0.10 |
| 2 | 8 | 1 | 1024 | 64 | 256 | False | torch.float16 | 0.08 | 0.05 | 0.03 |
| 1 | 8 | 1 | 1024 | 64 | 256 | False | torch.float16 | 0.04 | 0.05 | 0.05 |
| 1 | 8 | 1 | 512 | 64 | 256 | False | torch.float16 | 0.03 | 0.03 | 0.03 |

## mhc_post

### tileops

| batch | n_expand | c_x | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 4 | 1280 | torch.bfloat16 | 40.76 | 0.00 | 0.00 |
| 2 | 4 | 1920 | torch.bfloat16 | 41.02 | 0.01 | 0.00 |
| 4 | 4 | 2560 | torch.bfloat16 | 41.03 | 0.02 | 0.00 |

### baseline

| batch | n_expand | c_x | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 4 | 1280 | torch.bfloat16 | 0.01 | 3.97 | 0.00 |
| 2 | 4 | 1920 | torch.bfloat16 | 0.01 | 16.55 | 0.00 |
| 4 | 4 | 2560 | torch.bfloat16 | 0.01 | 56.19 | 0.00 |

## mhc_pre

### tileops

| batch | n_expand | c_x | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 4 | 1280 | torch.bfloat16 | 311.61 | 0.00 | 0.00 |
| 2 | 4 | 1920 | torch.bfloat16 | 309.94 | 0.02 | 0.00 |
| 4 | 4 | 2560 | torch.bfloat16 | 310.44 | 0.06 | 0.00 |

### baseline

| batch | n_expand | c_x | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 4 | 1280 | torch.bfloat16 | 0.27 | 4.59 | 0.00 |
| 2 | 4 | 1920 | torch.bfloat16 | 0.30 | 18.82 | 0.00 |
| 4 | 4 | 2560 | torch.bfloat16 | 0.34 | 59.90 | 0.00 |

## permute_align

### tileops

| total_tokens | top_k | num_experts | block_size | numel | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 512 | 2 | 8 | 16 | 1024 | 0.01 | N/A | 0.00 |
| 2048 | 2 | 8 | 16 | 4096 | 0.01 | N/A | 0.00 |
| 4096 | 2 | 8 | 16 | 8192 | 0.01 | N/A | 0.01 |
| 512 | 6 | 64 | 64 | 3072 | 0.01 | N/A | 0.01 |
| 2048 | 6 | 64 | 64 | 12288 | 0.01 | N/A | 0.01 |
| 4096 | 6 | 64 | 128 | 24576 | 0.02 | N/A | 0.01 |
| 8192 | 6 | 64 | 128 | 49152 | 0.03 | N/A | 0.01 |
| 2048 | 6 | 256 | 128 | 12288 | 0.02 | N/A | 0.02 |
| 8192 | 6 | 256 | 128 | 49152 | 0.03 | N/A | 0.02 |

### triton

| total_tokens | top_k | num_experts | block_size | numel | max_num_blocks | max_padded | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 512 | 2 | 8 | 16 | 1024 | 73 | 1159 | 0.03 | N/A | 0.00 |
| 2048 | 2 | 8 | 16 | 4096 | 265 | 4231 | 0.10 | N/A | 0.00 |
| 4096 | 2 | 8 | 16 | 8192 | 521 | 8327 | 0.20 | N/A | 0.00 |
| 512 | 6 | 64 | 64 | 3072 | 112 | 7167 | 0.02 | N/A | 0.00 |
| 2048 | 6 | 64 | 64 | 12288 | 256 | 16383 | 0.05 | N/A | 0.00 |
| 4096 | 6 | 64 | 128 | 24576 | 257 | 32831 | 0.09 | N/A | 0.00 |
| 8192 | 6 | 64 | 128 | 49152 | 449 | 57407 | 0.16 | N/A | 0.00 |
| 2048 | 6 | 256 | 128 | 12288 | 351 | 44927 | 0.05 | N/A | 0.00 |
| 8192 | 6 | 256 | 128 | 49152 | 639 | 81791 | 0.08 | N/A | 0.01 |

## reduce

### tileops

| m | n | dtype | op_kind | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 1024 | 4096 | torch.float16 | sum | 61.23 | 0.00 | 0.00 |
| 1024 | 4096 | torch.bfloat16 | sum | 61.01 | 0.00 | 0.00 |
| 4096 | 4096 | torch.float16 | sum | 60.96 | 0.00 | 0.00 |
| 1024 | 4096 | torch.float16 | mean | 61.48 | 0.00 | 0.00 |
| 1024 | 4096 | torch.float16 | amax | 60.99 | 0.00 | 0.00 |
| 1024 | 4096 | torch.float16 | amin | 61.46 | 0.00 | 0.00 |
| 1024 | 4096 | torch.float16 | prod | 76.77 | 0.00 | 0.00 |
| 1024 | 4096 | torch.float16 | std | 108.44 | 0.00 | 0.00 |
| 1024 | 4096 | torch.float16 | var | 108.46 | 0.00 | 0.00 |
| 1024 | 4096 | torch.float16 | var_mean | 106.89 | 0.00 | 0.00 |

### baseline

| m | n | dtype | op_kind | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 1024 | 4096 | torch.float16 | sum | 0.03 | 0.16 | 0.32 |
| 1024 | 4096 | torch.bfloat16 | sum | 0.03 | 0.16 | 0.31 |
| 4096 | 4096 | torch.float16 | sum | 0.08 | 0.21 | 0.42 |
| 1024 | 4096 | torch.float16 | mean | 0.03 | 0.16 | 0.32 |
| 1024 | 4096 | torch.float16 | amax | 0.03 | 0.16 | 0.32 |
| 1024 | 4096 | torch.float16 | amin | 0.03 | 0.16 | 0.32 |
| 1024 | 4096 | torch.float16 | prod | 0.03 | 0.16 | 0.32 |
| 1024 | 4096 | torch.float16 | std | 0.04 | 0.33 | 0.22 |
| 1024 | 4096 | torch.float16 | var | 0.04 | 0.33 | 0.22 |
| 1024 | 4096 | torch.float16 | var_mean | 0.05 | 0.25 | 0.17 |

## rms_norm

### tileops

| m | n | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| 1024 | 4096 | torch.float16 | 53.92 | 0.00 | 0.00 |
| 4096 | 4096 | torch.bfloat16 | 53.67 | 0.00 | 0.00 |
| 2048 | 5120 | torch.float16 | 53.46 | 0.00 | 0.00 |
| 1025 | 4096 | torch.float16 | 54.04 | 0.00 | 0.00 |

### baseline

| m | n | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| 1024 | 4096 | torch.float16 | 0.07 | 0.24 | 0.24 |
| 4096 | 4096 | torch.bfloat16 | 0.25 | 0.27 | 0.27 |
| 2048 | 5120 | torch.float16 | 0.17 | 0.24 | 0.24 |
| 1025 | 4096 | torch.float16 | 0.07 | 0.24 | 0.24 |

## rope_neox

### tileops

| seq_len | head_dim | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| 2048 | 64 | torch.float16 | 0.00 | 0.24 | 0.36 |
| 2048 | 64 | torch.bfloat16 | 0.00 | 0.24 | 0.36 |
| 2048 | 64 | torch.float32 | 0.00 | 0.21 | 0.64 |
| 2048 | 128 | torch.float16 | 0.00 | 0.42 | 0.63 |
| 2048 | 128 | torch.bfloat16 | 0.00 | 0.42 | 0.63 |
| 2048 | 128 | torch.float32 | 0.00 | 0.35 | 1.04 |
| 4096 | 128 | torch.float16 | 0.00 | 0.70 | 1.05 |
| 4096 | 128 | torch.bfloat16 | 0.00 | 0.70 | 1.05 |
| 4096 | 128 | torch.float32 | 0.00 | 0.53 | 1.60 |

### baseline

| seq_len | head_dim | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| 2048 | 64 | torch.float16 | 0.01 | 0.04 | 0.06 |
| 2048 | 64 | torch.bfloat16 | 0.01 | 0.04 | 0.06 |
| 2048 | 64 | torch.float32 | 0.01 | 0.04 | 0.12 |
| 2048 | 128 | torch.float16 | 0.01 | 0.07 | 0.11 |
| 2048 | 128 | torch.bfloat16 | 0.01 | 0.07 | 0.11 |
| 2048 | 128 | torch.float32 | 0.01 | 0.07 | 0.22 |
| 4096 | 128 | torch.float16 | 0.02 | 0.13 | 0.19 |
| 4096 | 128 | torch.bfloat16 | 0.02 | 0.13 | 0.19 |
| 4096 | 128 | torch.float32 | 0.02 | 0.12 | 0.37 |

## softmax

### tileops

| m | n | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| 1024 | 4096 | torch.float16 | 76.09 | 0.00 | 0.00 |
| 4096 | 4096 | torch.bfloat16 | 76.10 | 0.00 | 0.00 |
| 1024 | 3000 | torch.float16 | 76.26 | 0.00 | 0.00 |
| 1025 | 4096 | torch.float16 | 76.01 | 0.00 | 0.00 |

### baseline

| m | n | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| 1024 | 4096 | torch.float16 | 0.02 | 0.97 | 0.97 |
| 4096 | 4096 | torch.bfloat16 | 0.06 | 1.14 | 1.14 |
| 1024 | 3000 | torch.float16 | 0.01 | 0.83 | 0.83 |
| 1025 | 4096 | torch.float16 | 0.02 | 0.97 | 0.97 |

## log_softmax

### tileops

| m | n | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| 1024 | 4096 | torch.float16 | 76.63 | 0.00 | 0.00 |
| 4096 | 4096 | torch.bfloat16 | 76.80 | 0.00 | 0.00 |
| 1024 | 3000 | torch.float16 | 77.30 | 0.00 | 0.00 |
| 1025 | 4096 | torch.float16 | 76.35 | 0.00 | 0.00 |

### baseline

| m | n | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| 1024 | 4096 | torch.float16 | 0.02 | 1.37 | 1.10 |
| 4096 | 4096 | torch.bfloat16 | 0.05 | 1.60 | 1.28 |
| 1024 | 3000 | torch.float16 | 0.01 | 1.16 | 0.93 |
| 1025 | 4096 | torch.float16 | 0.02 | 1.37 | 1.10 |

## logsumexp

### tileops

| m | n | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| 1024 | 4096 | torch.float16 | 70.29 | 0.00 | 0.00 |
| 4096 | 4096 | torch.bfloat16 | 69.97 | 0.00 | 0.00 |
| 1024 | 3000 | torch.float16 | 70.06 | 0.00 | 0.00 |
| 1025 | 4096 | torch.float16 | 70.43 | 0.00 | 0.00 |

### baseline

| m | n | dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- |
| 1024 | 4096 | torch.float16 | 0.05 | 0.25 | 0.17 |
| 4096 | 4096 | torch.bfloat16 | 0.10 | 0.50 | 0.33 |
| 1024 | 3000 | torch.float16 | 0.04 | 0.21 | 0.14 |
| 1025 | 4096 | torch.float16 | 0.05 | 0.24 | 0.16 |

## exp

### tileops

| op_name | n_total | dtype | output_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| exp | 262144 | torch.float16 | torch.float16 | 0.00 | 0.11 | 0.46 |
| exp | 1048576 | torch.float16 | torch.float16 | 0.00 | 0.33 | 1.32 |
| exp | 4000000 | torch.float16 | torch.float16 | 0.01 | 0.63 | 2.52 |
| exp | 262144 | torch.bfloat16 | torch.bfloat16 | 0.00 | 0.11 | 0.45 |
| exp | 1048576 | torch.bfloat16 | torch.bfloat16 | 0.00 | 0.33 | 1.31 |
| exp | 4000000 | torch.bfloat16 | torch.bfloat16 | 0.01 | 0.63 | 2.51 |

### baseline

| op_name | n_total | dtype | output_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| exp | 262144 | torch.float16 | torch.float16 | 0.00 | 0.11 | 0.44 |
| exp | 1048576 | torch.float16 | torch.float16 | 0.00 | 0.32 | 1.28 |
| exp | 4000000 | torch.float16 | torch.float16 | 0.01 | 0.63 | 2.53 |
| exp | 262144 | torch.bfloat16 | torch.bfloat16 | 0.00 | 0.11 | 0.44 |
| exp | 1048576 | torch.bfloat16 | torch.bfloat16 | 0.00 | 0.32 | 1.28 |
| exp | 4000000 | torch.bfloat16 | torch.bfloat16 | 0.01 | 0.63 | 2.53 |

## gelu

### tileops

| op_name | n_total | dtype | output_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| gelu | 262144 | torch.float16 | torch.float16 | 0.00 | 0.11 | 0.43 |
| gelu | 1048576 | torch.float16 | torch.float16 | 0.00 | 0.30 | 1.19 |
| gelu | 4000000 | torch.float16 | torch.float16 | 0.01 | 0.47 | 1.90 |
| gelu | 262144 | torch.bfloat16 | torch.bfloat16 | 0.00 | 0.11 | 0.44 |
| gelu | 1048576 | torch.bfloat16 | torch.bfloat16 | 0.00 | 0.29 | 1.16 |
| gelu | 4000000 | torch.bfloat16 | torch.bfloat16 | 0.01 | 0.46 | 1.84 |

### baseline

| op_name | n_total | dtype | output_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| gelu | 262144 | torch.float16 | torch.float16 | 0.00 | 0.10 | 0.41 |
| gelu | 1048576 | torch.float16 | torch.float16 | 0.00 | 0.29 | 1.14 |
| gelu | 4000000 | torch.float16 | torch.float16 | 0.01 | 0.52 | 2.07 |
| gelu | 262144 | torch.bfloat16 | torch.bfloat16 | 0.00 | 0.10 | 0.41 |
| gelu | 1048576 | torch.bfloat16 | torch.bfloat16 | 0.00 | 0.28 | 1.12 |
| gelu | 4000000 | torch.bfloat16 | torch.bfloat16 | 0.01 | 0.50 | 2.01 |

## logical_not

### tileops

| op_name | n_total | dtype | output_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| logical_not | 262144 | torch.float16 | torch.bool | 0.00 | 0.11 | 0.32 |
| logical_not | 1048576 | torch.float16 | torch.bool | 0.00 | 0.21 | 0.64 |
| logical_not | 4000000 | torch.float16 | torch.bool | 0.01 | 0.30 | 0.91 |

### baseline

| op_name | n_total | dtype | output_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| logical_not | 262144 | torch.float16 | torch.bool | 0.00 | 0.11 | 0.34 |
| logical_not | 1048576 | torch.float16 | torch.bool | 0.00 | 0.34 | 1.02 |
| logical_not | 4000000 | torch.float16 | torch.bool | 0.01 | 0.72 | 2.16 |

## bitwise_not

### tileops

| op_name | n_total | dtype | output_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| bitwise_not | 262144 | torch.int32 | torch.int32 | 0.00 | 0.10 | 0.76 |
| bitwise_not | 1048576 | torch.int32 | torch.int32 | 0.01 | 0.19 | 1.55 |
| bitwise_not | 4000000 | torch.int32 | torch.int32 | 0.02 | 0.26 | 2.12 |

### baseline

| op_name | n_total | dtype | output_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| bitwise_not | 262144 | torch.int32 | torch.int32 | 0.00 | 0.11 | 0.85 |
| bitwise_not | 1048576 | torch.int32 | torch.int32 | 0.00 | 0.24 | 1.95 |
| bitwise_not | 4000000 | torch.int32 | torch.int32 | 0.01 | 0.39 | 3.15 |

## isnan

### tileops

| op_name | n_total | dtype | output_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| isnan | 262144 | torch.float16 | torch.bool | 0.00 | 0.11 | 0.32 |
| isnan | 1048576 | torch.float16 | torch.bool | 0.00 | 0.21 | 0.64 |
| isnan | 4000000 | torch.float16 | torch.bool | 0.01 | 0.30 | 0.90 |

### baseline

| op_name | n_total | dtype | output_dtype | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| isnan | 262144 | torch.float16 | torch.bool | 0.00 | 0.11 | 0.34 |
| isnan | 1048576 | torch.float16 | torch.bool | 0.00 | 0.34 | 1.02 |
| isnan | 4000000 | torch.float16 | torch.bool | 0.01 | 0.73 | 2.18 |

## unary_strategy

### relu_direct

| n_total | shape_label | dtype | strategy | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 4194304 | 1024x4096 | torch.float16 | direct | 0.01 | 0.29 | 1.17 |
| 4194304 | 1024x4096 | torch.bfloat16 | direct | 0.01 | 0.29 | 1.17 |
| 4194304 | 1024x4096 | torch.float32 | direct | 0.02 | 0.27 | 2.13 |
| 10485760 | 1024x10240 | torch.float16 | direct | 0.03 | 0.32 | 1.29 |
| 10485760 | 1024x10240 | torch.bfloat16 | direct | 0.03 | 0.32 | 1.29 |
| 10485760 | 1024x10240 | torch.float32 | direct | 0.04 | 0.29 | 2.33 |
| 20971520 | 1024x20480 | torch.float16 | direct | 0.06 | 0.34 | 1.36 |
| 20971520 | 1024x20480 | torch.bfloat16 | direct | 0.06 | 0.33 | 1.33 |
| 20971520 | 1024x20480 | torch.float32 | direct | 0.07 | 0.31 | 2.44 |

### relu_explicit_parallel

| n_total | shape_label | dtype | strategy | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 4194304 | 1024x4096 | torch.float16 | explicit_parallel | 0.02 | 0.22 | 0.88 |
| 4194304 | 1024x4096 | torch.bfloat16 | explicit_parallel | 0.02 | 0.22 | 0.87 |
| 4194304 | 1024x4096 | torch.float32 | explicit_parallel | 0.01 | 0.38 | 3.08 |
| 10485760 | 1024x10240 | torch.float16 | explicit_parallel | 0.04 | 0.25 | 0.98 |
| 10485760 | 1024x10240 | torch.bfloat16 | explicit_parallel | 0.04 | 0.24 | 0.98 |
| 10485760 | 1024x10240 | torch.float32 | explicit_parallel | 0.02 | 0.47 | 3.77 |
| 20971520 | 1024x20480 | torch.float16 | explicit_parallel | 0.08 | 0.26 | 1.03 |
| 20971520 | 1024x20480 | torch.bfloat16 | explicit_parallel | 0.08 | 0.26 | 1.03 |
| 20971520 | 1024x20480 | torch.float32 | explicit_parallel | 0.04 | 0.50 | 4.03 |

### relu_register_copy

| n_total | shape_label | dtype | strategy | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 4194304 | 1024x4096 | torch.float16 | register_copy | 0.01 | 0.66 | 2.65 |
| 4194304 | 1024x4096 | torch.bfloat16 | register_copy | 0.01 | 0.67 | 2.66 |
| 4194304 | 1024x4096 | torch.float32 | register_copy | 0.01 | 0.40 | 3.17 |
| 10485760 | 1024x10240 | torch.float16 | register_copy | 0.01 | 0.85 | 3.40 |
| 10485760 | 1024x10240 | torch.bfloat16 | register_copy | 0.01 | 0.86 | 3.42 |
| 10485760 | 1024x10240 | torch.float32 | register_copy | 0.02 | 0.48 | 3.85 |
| 20971520 | 1024x20480 | torch.float16 | register_copy | 0.02 | 0.96 | 3.86 |
| 20971520 | 1024x20480 | torch.bfloat16 | register_copy | 0.02 | 0.95 | 3.81 |
| 20971520 | 1024x20480 | torch.float32 | register_copy | 0.04 | 0.51 | 4.09 |

## vector_norm

### tileops

| m | n | dtype | op_kind | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 1024 | 4096 | torch.float16 | l1 | 63.52 | 0.00 | 0.00 |
| 1024 | 4096 | torch.bfloat16 | l1 | 63.29 | 0.00 | 0.00 |
| 1024 | 4096 | torch.float32 | l1 | 63.31 | 0.00 | 0.00 |
| 4096 | 4096 | torch.float16 | l1 | 63.28 | 0.00 | 0.00 |
| 1024 | 4096 | torch.float16 | l2 | 63.77 | 0.00 | 0.00 |
| 1024 | 4096 | torch.bfloat16 | l2 | 63.47 | 0.00 | 0.00 |
| 1024 | 4096 | torch.float32 | l2 | 63.45 | 0.00 | 0.00 |
| 4096 | 4096 | torch.float16 | l2 | 63.33 | 0.00 | 0.00 |
| 1024 | 4096 | torch.float16 | inf | 63.67 | 0.00 | 0.00 |
| 1024 | 4096 | torch.bfloat16 | inf | 63.42 | 0.00 | 0.00 |
| 1024 | 4096 | torch.float32 | inf | 63.52 | 0.00 | 0.00 |
| 4096 | 4096 | torch.float16 | inf | 63.24 | 0.00 | 0.00 |

### baseline

| m | n | dtype | op_kind | latency_ms | tflops | bandwidth_tbs |
| --- | --- | --- | --- | --- | --- | --- |
| 1024 | 4096 | torch.float16 | l1 | 0.02 | 0.25 | 0.50 |
| 1024 | 4096 | torch.bfloat16 | l1 | 0.02 | 0.25 | 0.50 |
| 1024 | 4096 | torch.float32 | l1 | 0.02 | 0.22 | 0.88 |
| 4096 | 4096 | torch.float16 | l1 | 0.02 | 0.76 | 1.53 |
| 1024 | 4096 | torch.float16 | l2 | 0.02 | 0.25 | 0.50 |
| 1024 | 4096 | torch.bfloat16 | l2 | 0.02 | 0.25 | 0.50 |
| 1024 | 4096 | torch.float32 | l2 | 0.02 | 0.22 | 0.88 |
| 4096 | 4096 | torch.float16 | l2 | 0.02 | 0.76 | 1.52 |
| 1024 | 4096 | torch.float16 | inf | 0.02 | 0.24 | 0.49 |
| 1024 | 4096 | torch.bfloat16 | inf | 0.02 | 0.24 | 0.49 |
| 1024 | 4096 | torch.float32 | inf | 0.02 | 0.22 | 0.87 |
| 4096 | 4096 | torch.float16 | inf | 0.02 | 0.76 | 1.51 |
