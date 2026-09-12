discovered 54 benchmark files

=== [1/54] benchmarks/ops/attention/bench_deepseek_dsa_decode.py ===
benchmarks/ops/attention/bench_deepseek_dsa_decode.py::test_dsa_decode_bench[single-batch-mainstream-float16]
benchmarks/ops/attention/bench_deepseek_dsa_decode.py::test_dsa_decode_bench[longer-kv-lower-topk-float16]

2 tests collected in 2.52s
..                                                                       [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/attention/bench_deepseek_dsa_decode.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

benchmarks/ops/attention/bench_deepseek_dsa_decode.py::test_dsa_decode_bench[single-batch-mainstream-float16]
  /usr/local/lib/python3.12/dist-packages/torch/_inductor/compile_fx.py:321: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
2 passed, 15 warnings in 13.57s
--- benchmarks/ops/attention/bench_deepseek_dsa_decode.py finished in 19s ---

=== [2/54] benchmarks/ops/attention/bench_deepseek_mla_decode.py ===
benchmarks/ops/attention/bench_deepseek_mla_decode.py::test_mla_decode_bench[deepseek-v2-4k-float16]
benchmarks/ops/attention/bench_deepseek_mla_decode.py::test_mla_decode_bench[deepseek-v2-4k-bfloat16]
benchmarks/ops/attention/bench_deepseek_mla_decode.py::test_mla_decode_bench[deepseek-v2-32k-float16]
benchmarks/ops/attention/bench_deepseek_mla_decode.py::test_mla_decode_bench[deepseek-v2-32k-bfloat16]
benchmarks/ops/attention/bench_deepseek_mla_decode.py::test_mla_decode_bench[deepseek-v3-4k-bfloat16]
benchmarks/ops/attention/bench_deepseek_mla_decode.py::test_mla_decode_bench[deepseek-v3-32k-bfloat16]

6 tests collected in 2.54s
......                                                                   [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/attention/bench_deepseek_mla_decode.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
6 passed, 14 warnings in 21.06s
--- benchmarks/ops/attention/bench_deepseek_mla_decode.py finished in 22s ---

=== [3/54] benchmarks/ops/attention/bench_deepseek_nsa.py ===
benchmarks/ops/attention/bench_deepseek_nsa.py::test_nsa_cmp_fwd_varlen_bench[nsa-cmp-s8k-r8-h32-d128-float16]
benchmarks/ops/attention/bench_deepseek_nsa.py::test_nsa_cmp_fwd_varlen_bench[nsa-cmp-s4k-r4-h32-d128-float16]
benchmarks/ops/attention/bench_deepseek_nsa.py::test_nsa_topk_varlen_bench[nsa-topk-s8k-r8-h32-d128-float16]
benchmarks/ops/attention/bench_deepseek_nsa.py::test_nsa_topk_varlen_bench[nsa-topk-s4k-r4-h32-d128-float16]
benchmarks/ops/attention/bench_deepseek_nsa.py::test_nsa_fwd_varlen_bench[nsa-slc-s8k-r4-h16-d64-b1-float16]
benchmarks/ops/attention/bench_deepseek_nsa.py::test_nsa_fwd_varlen_bench[nsa-slc-s8k-r2-h16-d64-b4-float16]

6 tests collected in 2.52s
......                                                                   [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/attention/bench_deepseek_nsa.py::test_nsa_cmp_fwd_varlen_bench[nsa-cmp-s8k-r8-h32-d128-float16]
benchmarks/ops/attention/bench_deepseek_nsa.py::test_nsa_cmp_fwd_varlen_bench[nsa-cmp-s4k-r4-h32-d128-float16]
benchmarks/ops/attention/bench_deepseek_nsa.py::test_nsa_topk_varlen_bench[nsa-topk-s8k-r8-h32-d128-float16]
benchmarks/ops/attention/bench_deepseek_nsa.py::test_nsa_topk_varlen_bench[nsa-topk-s4k-r4-h32-d128-float16]
benchmarks/ops/attention/bench_deepseek_nsa.py::test_nsa_fwd_varlen_bench[nsa-slc-s8k-r4-h16-d64-b1-float16]
benchmarks/ops/attention/bench_deepseek_nsa.py::test_nsa_fwd_varlen_bench[nsa-slc-s8k-r2-h16-d64-b4-float16]
  /usr/local/lib/python3.12/dist-packages/tilelang/jit/kernel.py:161: DeprecationWarning: `tl.disable_tma_lower` is deprecated and will be removed in v0.1.10. Use `T.copy(..., disable_tma=True)` per-copy instead.
    instance = cls(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
6 passed, 6 warnings in 9.00s
--- benchmarks/ops/attention/bench_deepseek_nsa.py finished in 9s ---

=== [4/54] benchmarks/ops/attention/bench_gqa.py ===
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-8b-short-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-8b-short-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-8b-long-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-8b-long-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-70b-short-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-70b-short-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-70b-long-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-70b-long-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_dense_decode_bench[decode-llama-8b-4k-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_dense_decode_bench[decode-llama-8b-4k-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_dense_decode_bench[decode-llama-8b-32k-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_dense_decode_bench[decode-llama-8b-32k-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_dense_decode_bench[decode-llama-70b-4k-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_dense_decode_bench[decode-llama-70b-4k-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_dense_decode_bench[decode-llama-70b-32k-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_dense_decode_bench[decode-llama-70b-32k-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_dense_decode_bench[decode-llama-8b-4k-softcap50-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_dense_decode_bench[decode-qwen3-30b-a3b-bs1-1k-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_dense_decode_bench[decode-qwen3-30b-a3b-bs1-4k-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_dense_decode_bench[decode-qwen3-30b-a3b-bs1-8k-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_dense_decode_bench[decode-qwen3-30b-a3b-bs1-16k-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_dense_decode_bench[decode-qwen3-30b-a3b-bs1-32k-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_dense_decode_bench[decode-qwen3-30b-a3b-bs1-64k-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_dense_decode_bench[decode-qwen3-30b-a3b-bs1-128k-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_dense_decode_bench[decode-qwen3-30b-a3b-bs1-256k-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_varlen_fwd_bench[llama-8b-uniform-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_varlen_fwd_bench[llama-8b-uniform-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_varlen_fwd_bench[llama-8b-q-lt-kv-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_varlen_fwd_bench[llama-8b-q-lt-kv-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_varlen_fwd_bench[llama-70b-q-lt-kv-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_varlen_fwd_bench[llama-70b-q-lt-kv-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-prefill-paged-fullattn-b8-prefix32k-chunk1k-p64-partial-rope64-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-prefill-paged-fullattn-mixed-b8-p64-partial-rope64-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-prefill-paged-b8-prefix4k-chunk512-p64-full-rope-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_paged_with_kv_cache_fwd_bench[gqa-prefill-paged-softcap50-b4-prefix4k-chunk512-p64-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-prefill-paged-fp8-cache-b8-prefix32k-chunk1k-p64-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-prefill-paged-fp8-cache-b8-prefix4k-chunk512-p64-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_paged_with_kv_cache_fwd_bench[gqa-prefill-paged-fp8-cache-softcap50-b4-prefix4k-chunk512-p64-float16]

38 tests collected in 2.52s
......................................                                   [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-8b-short-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-8b-short-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-8b-long-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-8b-long-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-70b-short-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-70b-short-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-70b-long-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-70b-long-bfloat16]
  /home/ci-runner/runner/_work/TileOPs/TileOPs/src/tileops/kernels/kernel_base.py:165: UserWarning: FlashAttnBwdPreprocessKernel does not define autotune_configs; falling back to the provided config or default_config.
    warnings.warn(  # noqa: B028

benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-prefill-paged-fullattn-b8-prefix32k-chunk1k-p64-partial-rope64-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-prefill-paged-fullattn-mixed-b8-p64-partial-rope64-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-prefill-paged-b8-prefix4k-chunk512-p64-full-rope-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_paged_with_kv_cache_fwd_bench[gqa-prefill-paged-softcap50-b4-prefix4k-chunk512-p64-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-prefill-paged-fp8-cache-b8-prefix32k-chunk1k-p64-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-prefill-paged-fp8-cache-b8-prefix4k-chunk512-p64-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_paged_with_kv_cache_fwd_bench[gqa-prefill-paged-fp8-cache-softcap50-b4-prefix4k-chunk512-p64-float16]
  /usr/local/lib/python3.12/dist-packages/tilelang/jit/kernel.py:161: DeprecationWarning: `tl.disable_tma_lower` is deprecated and will be removed in v0.1.10. Use `T.copy(..., disable_tma=True)` per-copy instead.
    instance = cls(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
38 passed, 15 warnings in 102.87s (0:01:42)
--- benchmarks/ops/attention/bench_gqa.py finished in 103s ---

=== [5/54] benchmarks/ops/attention/bench_gqa_decode_paged.py ===
benchmarks/ops/attention/bench_gqa_decode_paged.py::test_gqa_decode_paged_bench[serving-8b-p64-float16]
benchmarks/ops/attention/bench_gqa_decode_paged.py::test_gqa_decode_paged_bench[serving-8b-long-p64-float16]
benchmarks/ops/attention/bench_gqa_decode_paged.py::test_gqa_decode_paged_bench[throughput-8b-p64-float16]
benchmarks/ops/attention/bench_gqa_decode_paged.py::test_gqa_decode_paged_bench[serving-70b-p64-float16]
benchmarks/ops/attention/bench_gqa_decode_paged.py::test_gqa_decode_paged_bench[serving-8b-p256-float16]
benchmarks/ops/attention/bench_gqa_decode_paged.py::test_gqa_decode_paged_bench[serving-70b-p256-float16]
benchmarks/ops/attention/bench_gqa_decode_paged.py::test_gqa_decode_paged_bench[serving-405b-p256-float16]
benchmarks/ops/attention/bench_gqa_decode_paged.py::test_gqa_decode_paged_bench[serving-8b-p64-softcap50-float16]
benchmarks/ops/attention/bench_gqa_decode_paged.py::test_gqa_decode_paged_bench[serving-8b-p16-float16]
benchmarks/ops/attention/bench_gqa_decode_paged.py::test_gqa_decode_paged_bench[throughput-8b-p16-float16]
benchmarks/ops/attention/bench_gqa_decode_paged.py::test_gqa_decode_paged_bench[serving-70b-p16-float16]

11 tests collected in 2.51s
........sss                                                              [100%]Benchmark report saved to profile_run.log

8 passed, 3 skipped in 11.31s
--- benchmarks/ops/attention/bench_gqa_decode_paged.py finished in 12s ---

=== [6/54] benchmarks/ops/attention/bench_gqa_sliding_window_varlen.py ===
benchmarks/ops/attention/bench_gqa_sliding_window_varlen.py::test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-float16]
benchmarks/ops/attention/bench_gqa_sliding_window_varlen.py::test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-bfloat16]
benchmarks/ops/attention/bench_gqa_sliding_window_varlen.py::test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-float16]
benchmarks/ops/attention/bench_gqa_sliding_window_varlen.py::test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-bfloat16]
benchmarks/ops/attention/bench_gqa_sliding_window_varlen.py::test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-float16]
benchmarks/ops/attention/bench_gqa_sliding_window_varlen.py::test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-bfloat16]
benchmarks/ops/attention/bench_gqa_sliding_window_varlen.py::test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-float16]
benchmarks/ops/attention/bench_gqa_sliding_window_varlen.py::test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-bfloat16]

8 tests collected in 2.51s
........                                                                 [100%]Benchmark report saved to profile_run.log

8 passed in 131.08s (0:02:11)
--- benchmarks/ops/attention/bench_gqa_sliding_window_varlen.py finished in 132s ---

=== [7/54] benchmarks/ops/attention/bench_mha.py ===
benchmarks/ops/attention/bench_mha.py::test_mha_bwd_bench[llama-8b-short-float16]
benchmarks/ops/attention/bench_mha.py::test_mha_bwd_bench[llama-8b-short-bfloat16]
benchmarks/ops/attention/bench_mha.py::test_mha_bwd_bench[llama-8b-long-float16]
benchmarks/ops/attention/bench_mha.py::test_mha_bwd_bench[llama-8b-long-bfloat16]
benchmarks/ops/attention/bench_mha.py::test_mha_bwd_bench[llama-70b-short-float16]
benchmarks/ops/attention/bench_mha.py::test_mha_bwd_bench[llama-70b-short-bfloat16]
benchmarks/ops/attention/bench_mha.py::test_mha_bwd_bench[llama-70b-long-float16]
benchmarks/ops/attention/bench_mha.py::test_mha_bwd_bench[llama-70b-long-bfloat16]

8 tests collected in 1.99s
........                                                                 [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/attention/bench_mha.py::test_mha_bwd_bench[llama-8b-short-float16]
benchmarks/ops/attention/bench_mha.py::test_mha_bwd_bench[llama-8b-short-bfloat16]
benchmarks/ops/attention/bench_mha.py::test_mha_bwd_bench[llama-8b-long-float16]
benchmarks/ops/attention/bench_mha.py::test_mha_bwd_bench[llama-8b-long-bfloat16]
benchmarks/ops/attention/bench_mha.py::test_mha_bwd_bench[llama-70b-short-float16]
benchmarks/ops/attention/bench_mha.py::test_mha_bwd_bench[llama-70b-short-bfloat16]
benchmarks/ops/attention/bench_mha.py::test_mha_bwd_bench[llama-70b-long-float16]
benchmarks/ops/attention/bench_mha.py::test_mha_bwd_bench[llama-70b-long-bfloat16]
  /home/ci-runner/runner/_work/TileOPs/TileOPs/src/tileops/kernels/kernel_base.py:165: UserWarning: FlashAttnBwdPreprocessKernel does not define autotune_configs; falling back to the provided config or default_config.
    warnings.warn(  # noqa: B028

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
8 passed, 8 warnings in 8.73s
--- benchmarks/ops/attention/bench_mha.py finished in 9s ---

=== [8/54] benchmarks/ops/attention/bench_mha_decode_paged.py ===
benchmarks/ops/attention/bench_mha_decode_paged.py::test_mha_decode_paged_bench[single-token-page128-float16]
benchmarks/ops/attention/bench_mha_decode_paged.py::test_mha_decode_paged_bench[batch2-page256-float16]
benchmarks/ops/attention/bench_mha_decode_paged.py::test_mha_decode_paged_bench[longer-cache-float16]
benchmarks/ops/attention/bench_mha_decode_paged.py::test_mha_decode_paged_bench[shorter-cache-float16]

4 tests collected in 1.97s
....                                                                     [100%]Benchmark report saved to profile_run.log

4 passed in 34.94s
--- benchmarks/ops/attention/bench_mha_decode_paged.py finished in 35s ---

=== [9/54] benchmarks/ops/bench_ada_layer_norm.py ===
benchmarks/ops/bench_ada_layer_norm.py::test_ada_layer_norm_bench[dit-xl-2-float16]
benchmarks/ops/bench_ada_layer_norm.py::test_ada_layer_norm_bench[dit-xl-2-bfloat16]
benchmarks/ops/bench_ada_layer_norm.py::test_ada_layer_norm_bench[llama-8b-prefill-float16]
benchmarks/ops/bench_ada_layer_norm.py::test_ada_layer_norm_bench[llama-8b-prefill-bfloat16]
benchmarks/ops/bench_ada_layer_norm.py::test_ada_layer_norm_bench[llama-8b-decode-bfloat16]
benchmarks/ops/bench_ada_layer_norm.py::test_ada_layer_norm_zero_bench[dit-xl-2-float16]
benchmarks/ops/bench_ada_layer_norm.py::test_ada_layer_norm_zero_bench[dit-xl-2-bfloat16]
benchmarks/ops/bench_ada_layer_norm.py::test_ada_layer_norm_zero_bench[llama-8b-prefill-float16]
benchmarks/ops/bench_ada_layer_norm.py::test_ada_layer_norm_zero_bench[llama-8b-prefill-bfloat16]
benchmarks/ops/bench_ada_layer_norm.py::test_ada_layer_norm_zero_bench[llama-8b-decode-bfloat16]

10 tests collected in 2.08s
..........                                                               [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_ada_layer_norm.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
10 passed, 14 warnings in 13.63s
--- benchmarks/ops/bench_ada_layer_norm.py finished in 14s ---

=== [10/54] benchmarks/ops/bench_argreduce.py ===
benchmarks/ops/bench_argreduce.py::test_argmax_bench[lm-head-argmax-float16]
benchmarks/ops/bench_argreduce.py::test_argmax_bench[lm-head-argmax-bfloat16]
benchmarks/ops/bench_argreduce.py::test_argmax_bench[hidden-state-argmax-float16]
benchmarks/ops/bench_argreduce.py::test_argmax_bench[hidden-state-argmax-bfloat16]
benchmarks/ops/bench_argreduce.py::test_argmax_bench[3d-non-last-axis-argmax-float16]
benchmarks/ops/bench_argreduce.py::test_argmin_bench[lm-head-argmin-float16]
benchmarks/ops/bench_argreduce.py::test_argmin_bench[lm-head-argmin-bfloat16]
benchmarks/ops/bench_argreduce.py::test_argmin_bench[hidden-state-argmin-float16]
benchmarks/ops/bench_argreduce.py::test_argmin_bench[hidden-state-argmin-bfloat16]

9 tests collected in 2.01s
.........                                                                [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_argreduce.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_argreduce.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
9 passed, 58 warnings in 13.89s
--- benchmarks/ops/bench_argreduce.py finished in 14s ---

=== [11/54] benchmarks/ops/bench_batch_norm.py ===
benchmarks/ops/bench_batch_norm.py::test_batch_norm_fwd_bench[resnet50-fc-float16]
benchmarks/ops/bench_batch_norm.py::test_batch_norm_fwd_bench[resnet50-stage1-float16]
benchmarks/ops/bench_batch_norm.py::test_batch_norm_fwd_bench[resnet50-stage2-float16]
benchmarks/ops/bench_batch_norm.py::test_batch_norm_fwd_bench[resnet50-stage3-float16]
benchmarks/ops/bench_batch_norm.py::test_batch_norm_fwd_bench[large-spatial-float16]
benchmarks/ops/bench_batch_norm.py::test_batch_norm_bwd_bench[resnet50-fc-float16]
benchmarks/ops/bench_batch_norm.py::test_batch_norm_bwd_bench[resnet50-stage1-float16]
benchmarks/ops/bench_batch_norm.py::test_batch_norm_bwd_bench[resnet50-stage2-float16]
benchmarks/ops/bench_batch_norm.py::test_batch_norm_bwd_bench[resnet50-stage3-float16]
benchmarks/ops/bench_batch_norm.py::test_batch_norm_bwd_bench[large-spatial-float16]

10 tests collected in 1.96s
..........                                                               [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_batch_norm.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_batch_norm.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
10 passed, 58 warnings in 30.31s
--- benchmarks/ops/bench_batch_norm.py finished in 31s ---

=== [12/54] benchmarks/ops/bench_binary_elementwise.py ===
benchmarks/ops/bench_binary_elementwise.py::test_binary_arith_bench[sub-1024x4096-float16-float16-SubFwdOp-sub-normal]
benchmarks/ops/bench_binary_elementwise.py::test_binary_arith_bench[sub-1024x10240-float16-float16-SubFwdOp-sub-normal]
benchmarks/ops/bench_binary_elementwise.py::test_binary_arith_bench[sub-1024x11008-float16-float16-SubFwdOp-sub-normal]
benchmarks/ops/bench_binary_elementwise.py::test_binary_arith_bench[mul-1024x4096-float16-float16-MulFwdOp-mul-normal]
benchmarks/ops/bench_binary_elementwise.py::test_binary_arith_bench[mul-1024x10240-float16-float16-MulFwdOp-mul-normal]
benchmarks/ops/bench_binary_elementwise.py::test_binary_arith_bench[mul-1024x11008-float16-float16-MulFwdOp-mul-normal]
benchmarks/ops/bench_binary_elementwise.py::test_binary_arith_bench[div-1024x4096-float16-float16-DivFwdOp-div-positive]
benchmarks/ops/bench_binary_elementwise.py::test_binary_arith_bench[div-1024x10240-float16-float16-DivFwdOp-div-positive]
benchmarks/ops/bench_binary_elementwise.py::test_binary_arith_bench[div-1024x11008-float16-float16-DivFwdOp-div-positive]
benchmarks/ops/bench_binary_elementwise.py::test_binary_arith_bench[remainder-1024x4096-float16-float16-RemainderFwdOp-remainder-positive]
benchmarks/ops/bench_binary_elementwise.py::test_binary_arith_bench[remainder-1024x10240-float16-float16-RemainderFwdOp-remainder-positive]
benchmarks/ops/bench_binary_elementwise.py::test_binary_arith_bench[pow-1024x4096-float16-float16-PowFwdOp-pow-positive]
benchmarks/ops/bench_binary_elementwise.py::test_binary_arith_bench[pow-1024x10240-float16-float16-PowFwdOp-pow-positive]
benchmarks/ops/bench_binary_elementwise.py::test_binary_arith_bench[floor_divide-1024x4096-float16-float16-FloorDivideFwdOp-floor_divide-positive]
benchmarks/ops/bench_binary_elementwise.py::test_binary_arith_bench[floor_divide-1024x10240-float16-float16-FloorDivideFwdOp-floor_divide-positive]
benchmarks/ops/bench_binary_elementwise.py::test_binary_arith_bench[lerp-1024x4096-float16-float16-LerpFwdOp-<lambda>-normal]
benchmarks/ops/bench_binary_elementwise.py::test_binary_arith_bench[lerp-1024x10240-float16-float16-LerpFwdOp-<lambda>-normal]
benchmarks/ops/bench_binary_elementwise.py::test_binary_arith_bench[maximum-1024x4096-float16-float16-MaximumFwdOp-maximum-normal]
benchmarks/ops/bench_binary_elementwise.py::test_binary_arith_bench[maximum-1024x10240-float16-float16-MaximumFwdOp-maximum-normal]
benchmarks/ops/bench_binary_elementwise.py::test_binary_arith_bench[maximum-1024x11008-float16-float16-MaximumFwdOp-maximum-normal]
benchmarks/ops/bench_binary_elementwise.py::test_binary_arith_bench[minimum-1024x4096-float16-float16-MinimumFwdOp-minimum-normal]
benchmarks/ops/bench_binary_elementwise.py::test_binary_arith_bench[minimum-1024x10240-float16-float16-MinimumFwdOp-minimum-normal]
benchmarks/ops/bench_binary_elementwise.py::test_binary_arith_bench[minimum-1024x11008-float16-float16-MinimumFwdOp-minimum-normal]
benchmarks/ops/bench_binary_elementwise.py::test_comparison_bench[eq-1024x4096-float16-eq]
benchmarks/ops/bench_binary_elementwise.py::test_comparison_bench[eq-1024x10240-float16-eq]
benchmarks/ops/bench_binary_elementwise.py::test_comparison_bench[ne-1024x4096-float16-ne]
benchmarks/ops/bench_binary_elementwise.py::test_comparison_bench[gt-1024x4096-float16-gt]
benchmarks/ops/bench_binary_elementwise.py::test_comparison_bench[lt-1024x4096-float16-lt]
benchmarks/ops/bench_binary_elementwise.py::test_comparison_bench[ge-1024x4096-float16-ge]
benchmarks/ops/bench_binary_elementwise.py::test_comparison_bench[le-1024x4096-float16-le]
benchmarks/ops/bench_binary_elementwise.py::test_logical_bench[logical_and-1024x4096-float16-LogicalAndFwdOp-logical_and]
benchmarks/ops/bench_binary_elementwise.py::test_logical_bench[logical_and-1024x10240-float16-LogicalAndFwdOp-logical_and]
benchmarks/ops/bench_binary_elementwise.py::test_logical_bench[logical_or-1024x4096-float16-LogicalOrFwdOp-logical_or]
benchmarks/ops/bench_binary_elementwise.py::test_logical_bench[logical_or-1024x10240-float16-LogicalOrFwdOp-logical_or]
benchmarks/ops/bench_binary_elementwise.py::test_bitwise_bench[bitwise_and-1024x4096-BitwiseAndFwdOp-bitwise_and]
benchmarks/ops/bench_binary_elementwise.py::test_bitwise_bench[bitwise_and-1024x10240-BitwiseAndFwdOp-bitwise_and]
benchmarks/ops/bench_binary_elementwise.py::test_bitwise_bench[bitwise_or-1024x4096-BitwiseOrFwdOp-bitwise_or]
benchmarks/ops/bench_binary_elementwise.py::test_bitwise_bench[bitwise_xor-1024x4096-BitwiseXorFwdOp-bitwise_xor]
benchmarks/ops/bench_binary_elementwise.py::test_silu_and_mul_bench[llama-8b-swiglu-prefill-float16]
benchmarks/ops/bench_binary_elementwise.py::test_silu_and_mul_bench[llama-8b-swiglu-prefill-bfloat16]
benchmarks/ops/bench_binary_elementwise.py::test_silu_and_mul_bench[llama-8b-swiglu-decode-bfloat16]
benchmarks/ops/bench_binary_elementwise.py::test_gelu_and_mul_bench[ffn-gelu-prefill-float16]
benchmarks/ops/bench_binary_elementwise.py::test_gelu_and_mul_bench[ffn-gelu-prefill-bfloat16]
benchmarks/ops/bench_binary_elementwise.py::test_gelu_and_mul_bench[ffn-gelu-decode-bfloat16]
benchmarks/ops/bench_binary_elementwise.py::test_gelu_tanh_and_mul_bench[ffn-gelu-tanh-prefill-float16]
benchmarks/ops/bench_binary_elementwise.py::test_gelu_tanh_and_mul_bench[ffn-gelu-tanh-prefill-bfloat16]
benchmarks/ops/bench_binary_elementwise.py::test_gelu_tanh_and_mul_bench[ffn-gelu-tanh-decode-bfloat16]
benchmarks/ops/bench_binary_elementwise.py::test_fused_gated_default_strategy_is_the_fast_one[silu_and_mul-1024-4096-float16-SiluAndMulFwdKernel]
benchmarks/ops/bench_binary_elementwise.py::test_fused_gated_default_strategy_is_the_fast_one[silu_and_mul-1024-11008-float16-SiluAndMulFwdKernel]
benchmarks/ops/bench_binary_elementwise.py::test_fused_gated_default_strategy_is_the_fast_one[silu_and_mul-4096-4096-float16-SiluAndMulFwdKernel]
benchmarks/ops/bench_binary_elementwise.py::test_fused_gated_default_strategy_is_the_fast_one[silu_and_mul-1024-4096-bfloat16-SiluAndMulFwdKernel]
benchmarks/ops/bench_binary_elementwise.py::test_fused_gated_default_strategy_is_the_fast_one[silu_and_mul-1024-4096-float32-SiluAndMulFwdKernel]
benchmarks/ops/bench_binary_elementwise.py::test_fused_gated_default_strategy_is_the_fast_one[gelu_and_mul-1024-4096-float16-GeluAndMulFwdKernel]
benchmarks/ops/bench_binary_elementwise.py::test_fused_gated_default_strategy_is_the_fast_one[gelu_tanh_and_mul-1024-4096-float16-GeluTanhAndMulFwdKernel]
benchmarks/ops/bench_binary_elementwise.py::test_broadcast_bench[sub-1024x4096-1x4096-float16-SubFwdOp-sub-normal]
benchmarks/ops/bench_binary_elementwise.py::test_broadcast_bench[sub-1024x10240-1x10240-float16-SubFwdOp-sub-normal]
benchmarks/ops/bench_binary_elementwise.py::test_broadcast_bench[sub-1024x11008-1x11008-float16-SubFwdOp-sub-normal]
benchmarks/ops/bench_binary_elementwise.py::test_broadcast_bench[mul-1024x4096-1x4096-float16-MulFwdOp-mul-normal]
benchmarks/ops/bench_binary_elementwise.py::test_broadcast_bench[mul-1024x10240-1x10240-float16-MulFwdOp-mul-normal]
benchmarks/ops/bench_binary_elementwise.py::test_broadcast_bench[mul-1024x11008-1x11008-float16-MulFwdOp-mul-normal]
benchmarks/ops/bench_binary_elementwise.py::test_broadcast_bench[div-1024x4096-1x4096-float16-DivFwdOp-div-positive]
benchmarks/ops/bench_binary_elementwise.py::test_broadcast_bench[div-1024x10240-1x10240-float16-DivFwdOp-div-positive]
benchmarks/ops/bench_binary_elementwise.py::test_broadcast_bench[div-1024x11008-1x11008-float16-DivFwdOp-div-positive]

63 tests collected in 1.92s
...............................................................          [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_binary_elementwise.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
63 passed, 14 warnings in 51.07s
--- benchmarks/ops/bench_binary_elementwise.py finished in 52s ---

=== [13/54] benchmarks/ops/bench_bmm.py ===
benchmarks/ops/bench_bmm.py::test_bmm_bench[small-b8-128-float16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[small-b8-128-bfloat16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[square-b8-1k-float16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[square-b8-1k-bfloat16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[square-b16-512-float16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[square-b16-512-bfloat16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[square-b32-256-float16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[square-b32-256-bfloat16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[square-b4-4k-bfloat16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[square-b8-2k-float16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[square-b8-2k-bfloat16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[mha-decode-b64-qk-float16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[mha-decode-b64-qk-bfloat16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[mha-decode-b64-pv-float16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[mha-decode-b64-pv-bfloat16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[moe-prefill-b128-bfloat16]
benchmarks/ops/bench_bmm.py::test_bmm_fp8_kn_bench[square-b4-1k-per-tensor-float8_e4m3fn]
benchmarks/ops/bench_bmm.py::test_bmm_fp8_kn_bench[square-b8-2k-per-tensor-float8_e4m3fn]
benchmarks/ops/bench_bmm.py::test_bmm_fp8_kn_bench[mha-decode-b32-pv-per-tensor-float8_e4m3fn]
benchmarks/ops/bench_bmm.py::test_bmm_fp8_kn_bench[mha-decode-b64-qk-per-tensor-float8_e4m3fn]
benchmarks/ops/bench_bmm.py::test_bmm_fp8_kn_bench[moe-prefill-b128-per-tensor-float8_e4m3fn]
benchmarks/ops/bench_bmm.py::test_bmm_fp8_nk_bench[square-b4-1k-per-tensor-float8_e4m3fn]
benchmarks/ops/bench_bmm.py::test_bmm_fp8_nk_bench[square-b8-2k-per-tensor-float8_e4m3fn]
benchmarks/ops/bench_bmm.py::test_bmm_fp8_nk_bench[mha-decode-b32-pv-per-tensor-float8_e4m3fn]
benchmarks/ops/bench_bmm.py::test_bmm_fp8_nk_bench[mha-decode-b64-qk-per-tensor-float8_e4m3fn]
benchmarks/ops/bench_bmm.py::test_bmm_fp8_nk_bench[moe-prefill-b128-per-tensor-float8_e4m3fn]

26 tests collected in 1.96s
..........................                                               [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_bmm.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_bmm.py::test_bmm_fp8_kn_bench[square-b4-1k-per-tensor-float8_e4m3fn]
  /home/ci-runner/runner/_work/TileOPs/TileOPs/src/tileops/ops/op_base.py:607: UserWarning: BmmFp8KNFwdOp: b has layout [B,K,N] (shape=(4, 1024, 1024)); triggering an extra transpose(-2,-1).contiguous() DtoD copy before the fp8-TN WGMMA kernel. For best performance pass b as [B,N,K] (K-innermost) for the zero-copy fast path.
    return self.forward(*args, **kwargs)

benchmarks/ops/bench_bmm.py::test_bmm_fp8_kn_bench[square-b8-2k-per-tensor-float8_e4m3fn]
  /home/ci-runner/runner/_work/TileOPs/TileOPs/src/tileops/ops/op_base.py:607: UserWarning: BmmFp8KNFwdOp: b has layout [B,K,N] (shape=(8, 2048, 2048)); triggering an extra transpose(-2,-1).contiguous() DtoD copy before the fp8-TN WGMMA kernel. For best performance pass b as [B,N,K] (K-innermost) for the zero-copy fast path.
    return self.forward(*args, **kwargs)

benchmarks/ops/bench_bmm.py::test_bmm_fp8_kn_bench[mha-decode-b32-pv-per-tensor-float8_e4m3fn]
  /home/ci-runner/runner/_work/TileOPs/TileOPs/src/tileops/ops/op_base.py:607: UserWarning: BmmFp8KNFwdOp: b has layout [B,K,N] (shape=(32, 2048, 128)); triggering an extra transpose(-2,-1).contiguous() DtoD copy before the fp8-TN WGMMA kernel. For best performance pass b as [B,N,K] (K-innermost) for the zero-copy fast path.
    return self.forward(*args, **kwargs)

benchmarks/ops/bench_bmm.py::test_bmm_fp8_kn_bench[mha-decode-b64-qk-per-tensor-float8_e4m3fn]
  /home/ci-runner/runner/_work/TileOPs/TileOPs/src/tileops/ops/op_base.py:607: UserWarning: BmmFp8KNFwdOp: b has layout [B,K,N] (shape=(64, 128, 2048)); triggering an extra transpose(-2,-1).contiguous() DtoD copy before the fp8-TN WGMMA kernel. For best performance pass b as [B,N,K] (K-innermost) for the zero-copy fast path.
    return self.forward(*args, **kwargs)

benchmarks/ops/bench_bmm.py::test_bmm_fp8_kn_bench[moe-prefill-b128-per-tensor-float8_e4m3fn]
  /home/ci-runner/runner/_work/TileOPs/TileOPs/src/tileops/ops/op_base.py:607: UserWarning: BmmFp8KNFwdOp: b has layout [B,K,N] (shape=(128, 2048, 512)); triggering an extra transpose(-2,-1).contiguous() DtoD copy before the fp8-TN WGMMA kernel. For best performance pass b as [B,N,K] (K-innermost) for the zero-copy fast path.
    return self.forward(*args, **kwargs)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
26 passed, 49 warnings in 49.54s
--- benchmarks/ops/bench_bmm.py finished in 50s ---

=== [14/54] benchmarks/ops/bench_convolution.py ===
benchmarks/ops/bench_convolution.py::test_conv1d_bench[whisper-large-conv1-float16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[whisper-large-conv1-bfloat16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[wav2vec2-layer1-float16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[wav2vec2-layer1-bfloat16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[encodec-init-float16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[encodec-init-bfloat16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[encodec-deep-float16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[encodec-deep-bfloat16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[whisper-large-conv1-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[whisper-large-conv1-bias-bfloat16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[wav2vec2-layer1-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[wav2vec2-layer1-bias-bfloat16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[encodec-init-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[encodec-init-bias-bfloat16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[encodec-deep-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[encodec-deep-bias-bfloat16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[resnet-3x3-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[resnet-3x3-bfloat16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[stem-3x3-s2-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[stage-transition-3x3-s2-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[highres-3x3-s1-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[midres-5x5-s1-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[stage-transition-5x5-s2-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[stride2-bfloat16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[resnet-1x1-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[resnet-1x1-bfloat16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[bottleneck-expand-1x1-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[bottleneck-reduce-1x1-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[late-stage-1x1-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[classifier-1x1-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[deeplabv3-aspp-3x3-rate12-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[mobilenetv2-depthwise-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[resnext-grouped-3x3-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[resnet-3x3-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[resnet-3x3-bias-bfloat16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[stem-3x3-s2-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[stage-transition-3x3-s2-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[highres-3x3-s1-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[midres-5x5-s1-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[stage-transition-5x5-s2-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[stride2-bias-bfloat16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[resnet-1x1-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[resnet-1x1-bias-bfloat16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[bottleneck-expand-1x1-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[bottleneck-reduce-1x1-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[late-stage-1x1-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[classifier-1x1-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv3d_bench[r3d-stem-k3-s1-float16]
benchmarks/ops/bench_convolution.py::test_conv3d_bench[video-stage-downsample-k3-s2-float16]
benchmarks/ops/bench_convolution.py::test_conv3d_bench[unet-encoder-k3-s1-bfloat16]
benchmarks/ops/bench_convolution.py::test_conv3d_bench[3d-unet-aspp-3x3x3-rate6-float16]
benchmarks/ops/bench_convolution.py::test_conv3d_bench[3d-resnext-grouped-k3-float16]
benchmarks/ops/bench_convolution.py::test_conv3d_bench[r3d-stem-k3-s1-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv3d_bench[video-stage-downsample-k3-s2-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv3d_bench[unet-encoder-k3-s1-bias-bfloat16]

55 tests collected in 1.94s
.......................................................                  [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_convolution.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_convolution.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
55 passed, 58 warnings in 52.32s
--- benchmarks/ops/bench_convolution.py finished in 53s ---

=== [15/54] benchmarks/ops/bench_cumulative.py ===
benchmarks/ops/bench_cumulative.py::test_cumsum_bench[hidden-state-scan-float16]
benchmarks/ops/bench_cumulative.py::test_cumsum_bench[hidden-state-scan-bfloat16]
benchmarks/ops/bench_cumulative.py::test_cumsum_bench[long-seq-scan-bfloat16]
benchmarks/ops/bench_cumulative.py::test_cumprod_bench[hidden-state-scan-float16]
benchmarks/ops/bench_cumulative.py::test_cumprod_bench[hidden-state-scan-bfloat16]
benchmarks/ops/bench_cumulative.py::test_cumprod_bench[long-seq-scan-bfloat16]

6 tests collected in 1.97s
......                                                                   [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_cumulative.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_cumulative.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
6 passed, 58 warnings in 12.60s
--- benchmarks/ops/bench_cumulative.py finished in 13s ---

=== [16/54] benchmarks/ops/bench_deltanet.py ===
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_fwd[dn-b2-s2k-h4-d64-float16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_fwd[dn-b2-s2k-h4-d64-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_fwd[dn-b2-s4k-h4-d64-float16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_fwd[dn-b2-s4k-h4-d64-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_fwd[dn-b2-s8k-h4-d64-float16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_fwd[dn-b2-s8k-h4-d64-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_fwd[dn-b2-s16k-h4-d64-float16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_fwd[dn-b2-s16k-h4-d64-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_bwd[dn-bwd-b2-s2k-h4-d64-float16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_bwd[dn-bwd-b2-s2k-h4-d64-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_bwd[dn-bwd-b2-s4k-h4-d64-float16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_bwd[dn-bwd-b2-s4k-h4-d64-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_bwd[dn-bwd-b2-s8k-h4-d64-float16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_bwd[dn-bwd-b2-s8k-h4-d64-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_bwd[dn-bwd-b2-s16k-h4-d64-float16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_bwd[dn-bwd-b2-s16k-h4-d64-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_autograd[dn-autograd-b2-s2k-h4-d64-float16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_autograd[dn-autograd-b2-s2k-h4-d64-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_autograd[dn-autograd-b2-s8k-h4-d64-float16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_autograd[dn-autograd-b2-s8k-h4-d64-bfloat16]

=============================== warnings summary ===============================
../../../../../../usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
20 tests collected in 13.99s
....................                                                     [100%]Benchmark report saved to profile_run.log

20 passed in 106.38s (0:01:46)
--- benchmarks/ops/bench_deltanet.py finished in 107s ---

=== [17/54] benchmarks/ops/bench_deltanet_recurrence.py ===
benchmarks/ops/bench_deltanet_recurrence.py::test_deltanet_decode_bench[delta-decode-serving-b1-h8-d128-bfloat16]
benchmarks/ops/bench_deltanet_recurrence.py::test_deltanet_decode_bench[delta-decode-serving-b1-h16-d128-bfloat16]
benchmarks/ops/bench_deltanet_recurrence.py::test_deltanet_decode_bench[delta-decode-serving-b1-h32-d128-bfloat16]
benchmarks/ops/bench_deltanet_recurrence.py::test_deltanet_decode_bench[delta-decode-serving-b1-h48-d128-bfloat16]
benchmarks/ops/bench_deltanet_recurrence.py::test_deltanet_decode_bench[delta-decode-serving-b1-h64-d128-bfloat16]
benchmarks/ops/bench_deltanet_recurrence.py::test_deltanet_decode_bench[delta-decode-serving-b8-h32-d128-bfloat16]
benchmarks/ops/bench_deltanet_recurrence.py::test_deltanet_decode_bench[delta-decode-serving-b8-h48-d128-bfloat16]
benchmarks/ops/bench_deltanet_recurrence.py::test_deltanet_decode_bench[delta-decode-serving-b8-h64-d128-bfloat16]

8 tests collected in 1.95s
........                                                                 [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_deltanet_recurrence.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

benchmarks/ops/bench_deltanet_recurrence.py::test_deltanet_decode_bench[delta-decode-serving-b1-h8-d128-bfloat16]
  /usr/local/lib/python3.12/dist-packages/torch/_inductor/compile_fx.py:321: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
8 passed, 15 warnings in 15.06s
--- benchmarks/ops/bench_deltanet_recurrence.py finished in 16s ---

=== [18/54] benchmarks/ops/bench_dropout.py ===
benchmarks/ops/bench_dropout.py::test_dropout_bench[tokens-1k-hidden-4k-float16]
benchmarks/ops/bench_dropout.py::test_dropout_bench[tokens-1k-hidden-4k-float32]
benchmarks/ops/bench_dropout.py::test_dropout_bench[tokens-1k-hidden-10k-bfloat16]

3 tests collected in 2.01s
...                                                                      [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_dropout.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
3 passed, 14 warnings in 8.78s
--- benchmarks/ops/bench_dropout.py finished in 9s ---

=== [19/54] benchmarks/ops/bench_elementwise_manifest.py ===
benchmarks/ops/bench_elementwise_manifest.py::test_relu_manifest_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_relu_manifest_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_relu_manifest_bench[hidden-state-decode-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_gelu_manifest_bench[llama-8b-ffn-prefill-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_gelu_manifest_bench[llama-8b-ffn-prefill-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_gelu_manifest_bench[llama-8b-ffn-decode-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_silu_manifest_bench[llama-8b-ffn-prefill-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_silu_manifest_bench[llama-8b-ffn-prefill-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_silu_manifest_bench[llama-8b-ffn-decode-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_hardswish_manifest_bench[mbv3-stage2-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_hardswish_manifest_bench[mbv3-stage2-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_hardswish_manifest_bench[mbv3-stage3-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_hardswish_manifest_bench[mbv3-stage3-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_hardsigmoid_manifest_bench[mbv3-se-gate-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_hardsigmoid_manifest_bench[mbv3-se-gate-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_hardsigmoid_manifest_bench[mbv3-se-gate-deep-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_hardsigmoid_manifest_bench[mbv3-se-gate-deep-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_mish_manifest_bench[yolo-p3-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_mish_manifest_bench[yolo-p3-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_mish_manifest_bench[yolo-p4-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_mish_manifest_bench[yolo-p4-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_selu_manifest_bench[snn-fc-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_selu_manifest_bench[snn-fc-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_selu_manifest_bench[snn-fc-wide-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_selu_manifest_bench[snn-fc-wide-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_leaky_relu_manifest_bench[gan-feat-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_leaky_relu_manifest_bench[gan-feat-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_leaky_relu_manifest_bench[gan-feat-deep-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_leaky_relu_manifest_bench[gan-feat-deep-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_elu_manifest_bench[mlp-hidden-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_elu_manifest_bench[mlp-hidden-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_elu_manifest_bench[mlp-hidden-wide-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_elu_manifest_bench[mlp-hidden-wide-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_hardtanh_manifest_bench[bounded-hidden-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_hardtanh_manifest_bench[bounded-hidden-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_hardtanh_manifest_bench[bounded-conv-feat-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_hardtanh_manifest_bench[bounded-conv-feat-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_softplus_manifest_bench[mlp-hidden-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_softplus_manifest_bench[mlp-hidden-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_softplus_manifest_bench[mlp-hidden-wide-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_softplus_manifest_bench[mlp-hidden-wide-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_sigmoid_manifest_bench[elementwise-16M-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_sigmoid_manifest_bench[elementwise-16M-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_sigmoid_manifest_bench[elementwise-16M-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_sigmoid_manifest_bench[elementwise-256M-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_sigmoid_manifest_bench[elementwise-256M-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_tanh_manifest_bench[elementwise-16M-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_tanh_manifest_bench[elementwise-16M-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_tanh_manifest_bench[elementwise-16M-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_tanh_manifest_bench[elementwise-256M-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_tanh_manifest_bench[elementwise-256M-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_clamp_scalar_manifest_bench[elementwise-16M-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_clamp_scalar_manifest_bench[elementwise-16M-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_clamp_scalar_manifest_bench[elementwise-16M-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_clamp_scalar_manifest_bench[elementwise-256M-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_clamp_scalar_manifest_bench[elementwise-256M-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_nan_to_num_manifest_bench[elementwise-16M-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_nan_to_num_manifest_bench[elementwise-16M-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_nan_to_num_manifest_bench[elementwise-16M-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_nan_to_num_manifest_bench[elementwise-256M-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_nan_to_num_manifest_bench[elementwise-256M-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_prelu_manifest_bench[cnn-feat-per-channel-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_prelu_manifest_bench[cnn-feat-per-channel-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_prelu_manifest_bench[cnn-feat-per-channel-deep-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_prelu_manifest_bench[cnn-feat-per-channel-deep-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_masked_fill_tensor_manifest_bench[elementwise-16M-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_masked_fill_tensor_manifest_bench[elementwise-16M-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_masked_fill_tensor_manifest_bench[elementwise-16M-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_masked_fill_tensor_manifest_bench[elementwise-256M-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_masked_fill_tensor_manifest_bench[elementwise-256M-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_masked_fill_scalar_manifest_bench[elementwise-16M-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_masked_fill_scalar_manifest_bench[elementwise-16M-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_masked_fill_scalar_manifest_bench[elementwise-16M-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_masked_fill_scalar_manifest_bench[elementwise-256M-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_masked_fill_scalar_manifest_bench[elementwise-256M-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_add_manifest_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_add_manifest_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_add_manifest_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_add_manifest_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_add_manifest_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_add_manifest_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_sub_manifest_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_sub_manifest_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_sub_manifest_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_sub_manifest_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_sub_manifest_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_sub_manifest_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_mul_manifest_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_mul_manifest_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_mul_manifest_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_mul_manifest_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_mul_manifest_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_mul_manifest_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_div_manifest_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_div_manifest_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_div_manifest_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_div_manifest_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_div_manifest_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_div_manifest_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_remainder_manifest_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_remainder_manifest_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_remainder_manifest_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_remainder_manifest_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_remainder_manifest_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_remainder_manifest_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_pow_manifest_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_pow_manifest_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_pow_manifest_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_pow_manifest_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_pow_manifest_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_pow_manifest_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_floor_divide_manifest_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_floor_divide_manifest_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_floor_divide_manifest_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_floor_divide_manifest_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_floor_divide_manifest_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_floor_divide_manifest_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_lerp_manifest_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_lerp_manifest_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_lerp_manifest_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_lerp_manifest_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_lerp_manifest_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_lerp_manifest_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_maximum_manifest_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_maximum_manifest_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_maximum_manifest_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_maximum_manifest_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_maximum_manifest_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_maximum_manifest_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_minimum_manifest_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_minimum_manifest_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_minimum_manifest_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_minimum_manifest_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_minimum_manifest_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_minimum_manifest_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_eq_manifest_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_eq_manifest_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_eq_manifest_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_eq_manifest_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_eq_manifest_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_eq_manifest_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_ne_manifest_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_ne_manifest_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_ne_manifest_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_ne_manifest_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_ne_manifest_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_ne_manifest_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_gt_manifest_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_gt_manifest_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_gt_manifest_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_gt_manifest_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_gt_manifest_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_gt_manifest_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_lt_manifest_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_lt_manifest_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_lt_manifest_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_lt_manifest_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_lt_manifest_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_lt_manifest_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_ge_manifest_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_ge_manifest_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_ge_manifest_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_ge_manifest_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_ge_manifest_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_ge_manifest_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_le_manifest_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_le_manifest_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_le_manifest_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_le_manifest_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_le_manifest_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_le_manifest_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_logical_and_manifest_bench[hidden-state-prefill-bool]
benchmarks/ops/bench_elementwise_manifest.py::test_logical_and_manifest_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_logical_and_manifest_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_logical_and_manifest_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_logical_and_manifest_bench[cnn-feat-broadcast-bool]
benchmarks/ops/bench_elementwise_manifest.py::test_logical_and_manifest_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_logical_and_manifest_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_logical_and_manifest_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_logical_or_manifest_bench[hidden-state-prefill-bool]
benchmarks/ops/bench_elementwise_manifest.py::test_logical_or_manifest_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_logical_or_manifest_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_logical_or_manifest_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_logical_or_manifest_bench[cnn-feat-broadcast-bool]
benchmarks/ops/bench_elementwise_manifest.py::test_logical_or_manifest_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_logical_or_manifest_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_logical_or_manifest_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_bitwise_and_manifest_bench[hidden-state-prefill-bool]
benchmarks/ops/bench_elementwise_manifest.py::test_bitwise_and_manifest_bench[hidden-state-prefill-int32]
benchmarks/ops/bench_elementwise_manifest.py::test_bitwise_and_manifest_bench[hidden-state-prefill-int64]
benchmarks/ops/bench_elementwise_manifest.py::test_bitwise_and_manifest_bench[cnn-feat-broadcast-bool]
benchmarks/ops/bench_elementwise_manifest.py::test_bitwise_and_manifest_bench[cnn-feat-broadcast-int32]
benchmarks/ops/bench_elementwise_manifest.py::test_bitwise_and_manifest_bench[cnn-feat-broadcast-int64]
benchmarks/ops/bench_elementwise_manifest.py::test_bitwise_or_manifest_bench[hidden-state-prefill-bool]
benchmarks/ops/bench_elementwise_manifest.py::test_bitwise_or_manifest_bench[hidden-state-prefill-int32]
benchmarks/ops/bench_elementwise_manifest.py::test_bitwise_or_manifest_bench[hidden-state-prefill-int64]
benchmarks/ops/bench_elementwise_manifest.py::test_bitwise_or_manifest_bench[cnn-feat-broadcast-bool]
benchmarks/ops/bench_elementwise_manifest.py::test_bitwise_or_manifest_bench[cnn-feat-broadcast-int32]
benchmarks/ops/bench_elementwise_manifest.py::test_bitwise_or_manifest_bench[cnn-feat-broadcast-int64]
benchmarks/ops/bench_elementwise_manifest.py::test_bitwise_xor_manifest_bench[hidden-state-prefill-bool]
benchmarks/ops/bench_elementwise_manifest.py::test_bitwise_xor_manifest_bench[hidden-state-prefill-int32]
benchmarks/ops/bench_elementwise_manifest.py::test_bitwise_xor_manifest_bench[hidden-state-prefill-int64]
benchmarks/ops/bench_elementwise_manifest.py::test_bitwise_xor_manifest_bench[cnn-feat-broadcast-bool]
benchmarks/ops/bench_elementwise_manifest.py::test_bitwise_xor_manifest_bench[cnn-feat-broadcast-int32]
benchmarks/ops/bench_elementwise_manifest.py::test_bitwise_xor_manifest_bench[cnn-feat-broadcast-int64]
benchmarks/ops/bench_elementwise_manifest.py::test_where_manifest_bench[elementwise-16M-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_where_manifest_bench[elementwise-16M-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_where_manifest_bench[elementwise-16M-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_where_manifest_bench[elementwise-256M-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_where_manifest_bench[elementwise-256M-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_lerp_tensor_manifest_bench[elementwise-16M-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_lerp_tensor_manifest_bench[elementwise-16M-bfloat16]
benchmarks/ops/bench_elementwise_manifest.py::test_lerp_tensor_manifest_bench[elementwise-16M-float32]
benchmarks/ops/bench_elementwise_manifest.py::test_lerp_tensor_manifest_bench[elementwise-256M-float16]
benchmarks/ops/bench_elementwise_manifest.py::test_lerp_tensor_manifest_bench[elementwise-256M-bfloat16]

215 tests collected in 2.05s
........................................................................ [ 33%]
........................................................................ [ 66%]
.......................................................................  [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_elementwise_manifest.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
215 passed, 14 warnings in 136.14s (0:02:16)
--- benchmarks/ops/bench_elementwise_manifest.py finished in 137s ---

=== [20/54] benchmarks/ops/bench_engram.py ===
benchmarks/ops/bench_engram.py::test_engram_gate_conv_fwd_bench[fwd-b1-s32-d256-float16]
benchmarks/ops/bench_engram.py::test_engram_gate_conv_fwd_bench[fwd-b2-s64-d512-float16]
benchmarks/ops/bench_engram.py::test_engram_gate_conv_fwd_bench[fwd-b1-s128-d256-bfloat16]
benchmarks/ops/bench_engram.py::test_engram_gate_conv_bwd_bench[bwd-b1-s32-d256-float16]
benchmarks/ops/bench_engram.py::test_engram_gate_conv_bwd_bench[bwd-b2-s64-d512-float16]
benchmarks/ops/bench_engram.py::test_engram_gate_conv_bwd_bench[bwd-b1-s128-d256-bfloat16]
benchmarks/ops/bench_engram.py::test_engram_decode_bench[decode-b1-dmem512-d256-float16]
benchmarks/ops/bench_engram.py::test_engram_decode_bench[decode-b4-dmem1024-d512-float16]
benchmarks/ops/bench_engram.py::test_engram_decode_bench[decode-b8-dmem512-d256-bfloat16]

9 tests collected in 1.94s
.........                                                                [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_engram.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

benchmarks/ops/bench_engram.py::test_engram_decode_bench[decode-b1-dmem512-d256-float16]
  /usr/local/lib/python3.12/dist-packages/torch/_inductor/compile_fx.py:321: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
9 passed, 15 warnings in 29.43s
--- benchmarks/ops/bench_engram.py finished in 30s ---

=== [21/54] benchmarks/ops/bench_fft.py ===
benchmarks/ops/bench_fft.py::test_fft_bench[fft-4k-c64-unbatched-complex64]
benchmarks/ops/bench_fft.py::test_fft_bench[fft-4k-c64-b64-complex64]
benchmarks/ops/bench_fft.py::test_fft_bench[fft-4k-c128-b64-complex128]

3 tests collected in 2.04s
...                                                                      [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_fft.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

benchmarks/ops/bench_fft.py::test_fft_bench[fft-4k-c64-unbatched-complex64]
  /usr/local/lib/python3.12/dist-packages/torch/_inductor/lowering.py:2633: UserWarning: Torchinductor does not support code generation for complex operators. Performance may be worse than eager.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
3 passed, 15 warnings in 9.78s
--- benchmarks/ops/bench_fft.py finished in 10s ---

=== [22/54] benchmarks/ops/bench_fp8_lightning_indexer.py ===
benchmarks/ops/bench_fp8_lightning_indexer.py::test_fp8_lightning_indexer_bench[lightning-indexer-s8k-h32-d64-bfloat16]

1 test collected in 1.96s
.                                                                        [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_fp8_lightning_indexer.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

benchmarks/ops/bench_fp8_lightning_indexer.py::test_fp8_lightning_indexer_bench[lightning-indexer-s8k-h32-d64-bfloat16]
  /usr/local/lib/python3.12/dist-packages/torch/_inductor/compile_fx.py:321: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
1 passed, 15 warnings in 17.10s
--- benchmarks/ops/bench_fp8_lightning_indexer.py finished in 18s ---

=== [23/54] benchmarks/ops/bench_fp8_quant.py ===
benchmarks/ops/bench_fp8_quant.py::test_fp8_quant_bench[kv-index-8k-d64-float16]
benchmarks/ops/bench_fp8_quant.py::test_fp8_quant_bench[kv-index-8k-d64-bfloat16]
benchmarks/ops/bench_fp8_quant.py::test_fp8_quant_bench[kv-index-4k-d128-float32]

3 tests collected in 1.97s
...                                                                      [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_fp8_quant.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
3 passed, 14 warnings in 9.39s
--- benchmarks/ops/bench_fp8_quant.py finished in 10s ---

=== [24/54] benchmarks/ops/bench_fused_moe_experts.py ===
benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_nopad_bench[qwen3-235b-decode-float16]
benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_nopad_bench[qwen3-235b-decode-bfloat16]
benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_nopad_bench[qwen3-235b-prefill-float16]
benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_nopad_bench[qwen3-235b-prefill-bfloat16]
benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_nopad_bench[deepseek-v3-decode-float16]
benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_nopad_bench[deepseek-v3-decode-bfloat16]
benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_nopad_bench[deepseek-v3-prefill-float16]
benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_nopad_bench[deepseek-v3-prefill-bfloat16]

=============================== warnings summary ===============================
../../../../../../usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

../../../../../../usr/local/lib/python3.12/dist-packages/_pytest/assertion/rewrite.py:197
  /usr/local/lib/python3.12/dist-packages/_pytest/assertion/rewrite.py:197: RuntimeWarning: vLLM CUTLASS MoE baseline unavailable (No module named 'vllm.model_executor.layers.fused_moe.cutlass_moe'); the vllm-cutlass column will be omitted from results.
    exec(co, module.__dict__)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
8 tests collected in 12.51s
........                                                                 [100%]Benchmark report saved to profile_run.log

8 passed in 18.03s
--- benchmarks/ops/bench_fused_moe_experts.py finished in 19s ---

=== [25/54] benchmarks/ops/bench_gated_deltanet.py ===
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s2k-h4-d64-float16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s2k-h4-d64-bfloat16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s4k-h4-d64-float16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s4k-h4-d64-bfloat16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s8k-h4-d64-float16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s8k-h4-d64-bfloat16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s16k-h4-d64-float16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s16k-h4-d64-bfloat16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s32k-h4-d64-float16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s32k-h4-d64-bfloat16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_vs_fla_fwd[gdn-bthd-b1-s4k-h16-d128-float16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_vs_fla_fwd[gdn-bthd-b1-s4k-h16-d128-bfloat16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-float16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-bfloat16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-float16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-bfloat16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-float16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-bfloat16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-float16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-bfloat16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-float16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-bfloat16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-float16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-bfloat16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-float16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-bfloat16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-float16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-bfloat16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_vs_fla_autograd[gdn-autograd-b2-s2k-h4-d64-float16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_vs_fla_autograd[gdn-autograd-b2-s2k-h4-d64-bfloat16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_vs_fla_autograd[gdn-autograd-b2-s8k-h4-d64-float16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_vs_fla_autograd[gdn-autograd-b2-s8k-h4-d64-bfloat16]

=============================== warnings summary ===============================
../../../../../../usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
32 tests collected in 13.75s
................................                                         [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-float16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-bfloat16]
  /usr/local/lib/python3.12/dist-packages/tilelang/jit/kernel.py:161: DeprecationWarning: `tl.disable_tma_lower` is deprecated and will be removed in v0.1.10. Use `T.copy(..., disable_tma=True)` per-copy instead.
    instance = cls(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
32 passed, 2 warnings in 146.97s (0:02:26)
--- benchmarks/ops/bench_gated_deltanet.py finished in 148s ---

=== [26/54] benchmarks/ops/bench_gated_deltanet_prefill.py ===
benchmarks/ops/bench_gated_deltanet_prefill.py::test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-float16]
benchmarks/ops/bench_gated_deltanet_prefill.py::test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-bfloat16]
benchmarks/ops/bench_gated_deltanet_prefill.py::test_gated_deltanet_prefill_bhtd_bench[bhtd-qwen35-gdn-prefill-b1-s128k-h64-d128-float16]
benchmarks/ops/bench_gated_deltanet_prefill.py::test_gated_deltanet_prefill_bhtd_bench[bhtd-qwen35-gdn-prefill-b1-s128k-h64-d128-bfloat16]
benchmarks/ops/bench_gated_deltanet_prefill.py::test_gated_deltanet_prefill_fwd_bench[fallback-gdn-prefill-b1-s4k-h16-d128-bthd-float16]
benchmarks/ops/bench_gated_deltanet_prefill.py::test_gated_deltanet_prefill_fwd_bench[fallback-gdn-prefill-b1-s4k-h16-d128-bthd-bfloat16]
benchmarks/ops/bench_gated_deltanet_prefill.py::test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h16-d128-bthd-float16]
benchmarks/ops/bench_gated_deltanet_prefill.py::test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h16-d128-bthd-bfloat16]
benchmarks/ops/bench_gated_deltanet_prefill.py::test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h16-d128-bthd-float16]
benchmarks/ops/bench_gated_deltanet_prefill.py::test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h16-d128-bthd-bfloat16]
benchmarks/ops/bench_gated_deltanet_prefill.py::test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h16-d128-bthd-float16]
benchmarks/ops/bench_gated_deltanet_prefill.py::test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h16-d128-bthd-bfloat16]
benchmarks/ops/bench_gated_deltanet_prefill.py::test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h32-d128-bthd-float16]
benchmarks/ops/bench_gated_deltanet_prefill.py::test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h32-d128-bthd-bfloat16]
benchmarks/ops/bench_gated_deltanet_prefill.py::test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h32-d128-bthd-float16]
benchmarks/ops/bench_gated_deltanet_prefill.py::test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h32-d128-bthd-bfloat16]
benchmarks/ops/bench_gated_deltanet_prefill.py::test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h32-d128-bthd-float16]
benchmarks/ops/bench_gated_deltanet_prefill.py::test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h32-d128-bthd-bfloat16]
benchmarks/ops/bench_gated_deltanet_prefill.py::test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h48-d128-bthd-float16]
benchmarks/ops/bench_gated_deltanet_prefill.py::test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h48-d128-bthd-bfloat16]
benchmarks/ops/bench_gated_deltanet_prefill.py::test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h48-d128-bthd-float16]
benchmarks/ops/bench_gated_deltanet_prefill.py::test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h48-d128-bthd-bfloat16]
benchmarks/ops/bench_gated_deltanet_prefill.py::test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h48-d128-bthd-float16]
benchmarks/ops/bench_gated_deltanet_prefill.py::test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h48-d128-bthd-bfloat16]
benchmarks/ops/bench_gated_deltanet_prefill.py::test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h64-d128-bthd-float16]
benchmarks/ops/bench_gated_deltanet_prefill.py::test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h64-d128-bthd-bfloat16]
benchmarks/ops/bench_gated_deltanet_prefill.py::test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h64-d128-bthd-float16]
benchmarks/ops/bench_gated_deltanet_prefill.py::test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h64-d128-bthd-bfloat16]
benchmarks/ops/bench_gated_deltanet_prefill.py::test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h64-d128-bthd-float16]
benchmarks/ops/bench_gated_deltanet_prefill.py::test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h64-d128-bthd-bfloat16]

=============================== warnings summary ===============================
../../../../../../usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
30 tests collected in 14.05s
..............................                                           [100%]Benchmark report saved to profile_run.log

30 passed in 207.40s (0:03:27)
--- benchmarks/ops/bench_gated_deltanet_prefill.py finished in 208s ---

=== [27/54] benchmarks/ops/bench_gated_deltanet_recurrence.py ===
benchmarks/ops/bench_gated_deltanet_recurrence.py::test_gated_deltanet_decode_bench[gdn-decode-serving-b1-h8-d128-bfloat16]
benchmarks/ops/bench_gated_deltanet_recurrence.py::test_gated_deltanet_decode_bench[gdn-decode-serving-b1-h16-d128-bfloat16]
benchmarks/ops/bench_gated_deltanet_recurrence.py::test_gated_deltanet_decode_bench[gdn-decode-serving-b1-h32-d128-bfloat16]
benchmarks/ops/bench_gated_deltanet_recurrence.py::test_gated_deltanet_decode_bench[gdn-decode-serving-b1-h48-d128-bfloat16]
benchmarks/ops/bench_gated_deltanet_recurrence.py::test_gated_deltanet_decode_bench[gdn-decode-serving-b1-h64-d128-bfloat16]
benchmarks/ops/bench_gated_deltanet_recurrence.py::test_gated_deltanet_decode_bench[gdn-decode-serving-b8-h32-d128-bfloat16]
benchmarks/ops/bench_gated_deltanet_recurrence.py::test_gated_deltanet_decode_bench[gdn-decode-serving-b8-h48-d128-bfloat16]
benchmarks/ops/bench_gated_deltanet_recurrence.py::test_gated_deltanet_decode_bench[gdn-decode-serving-b8-h64-d128-bfloat16]

=============================== warnings summary ===============================
../../../../../../usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
8 tests collected in 13.84s
........                                                                 [100%]Benchmark report saved to profile_run.log

8 passed in 4.60s
--- benchmarks/ops/bench_gated_deltanet_recurrence.py finished in 5s ---

=== [28/54] benchmarks/ops/bench_gemm.py ===
benchmarks/ops/bench_gemm.py::test_gemm_bench[square-1k-nn-float16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[square-1k-nn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[ds-v3-decode-gate-up-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[ds-v3-decode-down-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[ds-v3-prefill-gate-up-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[ds-v3-prefill-down-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[ds-v3-prefill-attn-proj-float16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[ds-v3-prefill-attn-proj-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[k-dominant-7168x16384-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[wide-n-24576-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[mid-m16-attn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[mid-m32-attn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[mid-m64-down-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[mid-m96-gate-up-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[ds-v3-decode-gate-up-b1-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[ds-v3-decode-gate-up-b2-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-decode-gate-up-per-tensor-float8_e4m3fn]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-decode-down-per-tensor-float8_e4m3fn]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-prefill-gate-up-per-tensor-float8_e4m3fn]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-prefill-down-per-tensor-float8_e4m3fn]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-decode-gate-up-block128-float8_e4m3fn]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-decode-down-block128-float8_e4m3fn]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-prefill-gate-up-block128-float8_e4m3fn]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-prefill-down-block128-float8_e4m3fn]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-prefill-attn-proj-block128-float8_e4m3fn]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[k-dominant-7168x16384-block128-float8_e4m3fn]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[wide-n-24576-block128-float8_e4m3fn]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[small-batch-down-m8-per-tensor-float8_e4m3fn]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[gemv-down-m1-per-tensor-float8_e4m3fn]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[gemv-down-m1-block128-float8_e4m3fn]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-decode-gate-up-per-tensor-bias-float8_e4m3fn]
benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[compile-smoke-square-64x64x128-float16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[compile-smoke-rect-128x256x256-float16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[decode-l2-resident-ish-float16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[decode-hbm-streaming-threshold-float16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[decode-non-power2-low-cta-float16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[decode-long-k-pressure-float16]

37 tests collected in 1.97s
.....................................                                    [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_gemm.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_gemm.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
37 passed, 58 warnings in 207.48s (0:03:27)
--- benchmarks/ops/bench_gemm.py finished in 208s ---

=== [29/54] benchmarks/ops/bench_gla_chunkwise.py ===
benchmarks/ops/bench_gla_chunkwise.py::test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-float16]
benchmarks/ops/bench_gla_chunkwise.py::test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-bfloat16]
benchmarks/ops/bench_gla_chunkwise.py::test_gla_fwd_bench[gla-init-b2-s4k-h4-d64-float16]
benchmarks/ops/bench_gla_chunkwise.py::test_gla_fwd_bench[gla-init-b2-s4k-h4-d64-bfloat16]
benchmarks/ops/bench_gla_chunkwise.py::test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-float16]
benchmarks/ops/bench_gla_chunkwise.py::test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-bfloat16]
benchmarks/ops/bench_gla_chunkwise.py::test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-float16]
benchmarks/ops/bench_gla_chunkwise.py::test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-bfloat16]
benchmarks/ops/bench_gla_chunkwise.py::test_gla_bwd_bench[gla-bwd-b2-s2k-h4-d64-float16]
benchmarks/ops/bench_gla_chunkwise.py::test_gla_bwd_bench[gla-bwd-b2-s2k-h4-d64-bfloat16]
benchmarks/ops/bench_gla_chunkwise.py::test_gla_bwd_bench[gla-bwd-b2-s4k-h4-d64-float16]
benchmarks/ops/bench_gla_chunkwise.py::test_gla_bwd_bench[gla-bwd-b2-s4k-h4-d64-bfloat16]
benchmarks/ops/bench_gla_chunkwise.py::test_gla_bwd_bench[gla-bwd-b2-s8k-h4-d64-float16]
benchmarks/ops/bench_gla_chunkwise.py::test_gla_bwd_bench[gla-bwd-b2-s8k-h4-d64-bfloat16]
benchmarks/ops/bench_gla_chunkwise.py::test_gla_bwd_bench[gla-bwd-b2-s16k-h4-d64-float16]
benchmarks/ops/bench_gla_chunkwise.py::test_gla_bwd_bench[gla-bwd-b2-s16k-h4-d64-bfloat16]

=============================== warnings summary ===============================
../../../../../../usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
16 tests collected in 14.13s
........XXXXXXXX                                                         [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_gla_chunkwise.py: 56 warnings
  /usr/local/lib/python3.12/dist-packages/tilelang/jit/kernel.py:161: DeprecationWarning: `tl.disable_tma_lower` is deprecated and will be removed in v0.1.10. Use `T.copy(..., disable_tma=True)` per-copy instead.
    instance = cls(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
8 passed, 8 xpassed, 56 warnings in 129.22s (0:02:09)
--- benchmarks/ops/bench_gla_chunkwise.py finished in 130s ---

=== [30/54] benchmarks/ops/bench_gla_recurrence.py ===
benchmarks/ops/bench_gla_recurrence.py::test_gla_decode_bench[gla-decode-serving-b1-h8-d128-bfloat16]
benchmarks/ops/bench_gla_recurrence.py::test_gla_decode_bench[gla-decode-serving-b1-h16-d128-bfloat16]
benchmarks/ops/bench_gla_recurrence.py::test_gla_decode_bench[gla-decode-serving-b1-h32-d128-bfloat16]
benchmarks/ops/bench_gla_recurrence.py::test_gla_decode_bench[gla-decode-serving-b1-h48-d128-bfloat16]
benchmarks/ops/bench_gla_recurrence.py::test_gla_decode_bench[gla-decode-serving-b1-h64-d128-bfloat16]
benchmarks/ops/bench_gla_recurrence.py::test_gla_decode_bench[gla-decode-serving-b8-h32-d128-bfloat16]
benchmarks/ops/bench_gla_recurrence.py::test_gla_decode_bench[gla-decode-serving-b8-h48-d128-bfloat16]
benchmarks/ops/bench_gla_recurrence.py::test_gla_decode_bench[gla-decode-serving-b8-h64-d128-bfloat16]

=============================== warnings summary ===============================
../../../../../../usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
8 tests collected in 13.83s
........                                                                 [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_gla_recurrence.py::test_gla_decode_bench[gla-decode-serving-b1-h8-d128-bfloat16]
  /usr/local/lib/python3.12/dist-packages/torch/_inductor/compile_fx.py:321: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
8 passed, 1 warning in 10.01s
--- benchmarks/ops/bench_gla_recurrence.py finished in 11s ---

=== [31/54] benchmarks/ops/bench_group_norm.py ===
benchmarks/ops/bench_group_norm.py::test_group_norm_bench[image-g32-affine-float16]
benchmarks/ops/bench_group_norm.py::test_group_norm_bench[image-g32-affine-bfloat16]
benchmarks/ops/bench_group_norm.py::test_group_norm_bench[wider-channel-g32-affine-float16]
benchmarks/ops/bench_group_norm.py::test_group_norm_bench[tail-spatial-g16-affine-float16]
benchmarks/ops/bench_group_norm.py::test_group_norm_no_affine_bench[image-g32-float16]
benchmarks/ops/bench_group_norm.py::test_group_norm_no_affine_bench[image-g32-bfloat16]
benchmarks/ops/bench_group_norm.py::test_group_norm_no_affine_bench[wider-channel-g32-float16]
benchmarks/ops/bench_group_norm.py::test_group_norm_no_affine_bench[tail-spatial-g16-float16]

8 tests collected in 1.96s
........                                                                 [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_group_norm.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_group_norm.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
8 passed, 58 warnings in 39.22s
--- benchmarks/ops/bench_group_norm.py finished in 40s ---

=== [32/54] benchmarks/ops/bench_grouped_gemm.py ===
benchmarks/ops/bench_grouped_gemm.py::test_grouped_gemm_bench[nt-batch16-m4096-n4096-k4096-float16]
benchmarks/ops/bench_grouped_gemm.py::test_grouped_gemm_bench[nt-batch16-m4096-n4096-k4096-bfloat16]
benchmarks/ops/bench_grouped_gemm.py::test_grouped_gemm_bench[nn-batch16-m4096-n4096-k4096-float16]
benchmarks/ops/bench_grouped_gemm.py::test_grouped_gemm_bench[tn-batch16-m4096-n4096-k4096-float16]

4 tests collected in 2.00s
....                                                                     [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_grouped_gemm.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
4 passed, 14 warnings in 20.37s
--- benchmarks/ops/bench_grouped_gemm.py finished in 21s ---

=== [33/54] benchmarks/ops/bench_independent_elementwise.py ===
benchmarks/ops/bench_independent_elementwise.py::test_clamp_tensor_bench[elementwise-16M-float16]
benchmarks/ops/bench_independent_elementwise.py::test_clamp_tensor_bench[elementwise-16M-bfloat16]
benchmarks/ops/bench_independent_elementwise.py::test_clamp_tensor_bench[elementwise-16M-float32]
benchmarks/ops/bench_independent_elementwise.py::test_clamp_tensor_bench[elementwise-256M-float16]
benchmarks/ops/bench_independent_elementwise.py::test_clamp_tensor_bench[elementwise-256M-bfloat16]
benchmarks/ops/bench_independent_elementwise.py::test_clamp_tensor_bench[elementwise-16M-min-only-float16]
benchmarks/ops/bench_independent_elementwise.py::test_clamp_tensor_bench[elementwise-16M-min-only-bfloat16]
benchmarks/ops/bench_independent_elementwise.py::test_clamp_tensor_bench[elementwise-16M-min-only-float32]
benchmarks/ops/bench_independent_elementwise.py::test_clamp_tensor_bench[elementwise-256M-min-only-float16]
benchmarks/ops/bench_independent_elementwise.py::test_clamp_tensor_bench[elementwise-256M-min-only-bfloat16]
benchmarks/ops/bench_independent_elementwise.py::test_clamp_tensor_bench[elementwise-16M-max-only-float16]
benchmarks/ops/bench_independent_elementwise.py::test_clamp_tensor_bench[elementwise-16M-max-only-bfloat16]
benchmarks/ops/bench_independent_elementwise.py::test_clamp_tensor_bench[elementwise-16M-max-only-float32]
benchmarks/ops/bench_independent_elementwise.py::test_clamp_tensor_bench[elementwise-256M-max-only-float16]
benchmarks/ops/bench_independent_elementwise.py::test_clamp_tensor_bench[elementwise-256M-max-only-bfloat16]
benchmarks/ops/bench_independent_elementwise.py::test_alibi_bench[llama-prefill-2k-float16]
benchmarks/ops/bench_independent_elementwise.py::test_alibi_bench[llama-prefill-2k-bfloat16]
benchmarks/ops/bench_independent_elementwise.py::test_alibi_bench[llama-prefill-4k-float16]
benchmarks/ops/bench_independent_elementwise.py::test_alibi_bench[llama-prefill-4k-bfloat16]
benchmarks/ops/bench_independent_elementwise.py::test_sinusoidal_bench[transformer-2k-4k-float16]
benchmarks/ops/bench_independent_elementwise.py::test_sinusoidal_bench[transformer-2k-4k-bfloat16]
benchmarks/ops/bench_independent_elementwise.py::test_sinusoidal_bench[transformer-4k-4k-float16]
benchmarks/ops/bench_independent_elementwise.py::test_sinusoidal_bench[transformer-4k-4k-bfloat16]

23 tests collected in 2.00s
.......................                                                  [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_independent_elementwise.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
23 passed, 14 warnings in 22.91s
--- benchmarks/ops/bench_independent_elementwise.py finished in 23s ---

=== [34/54] benchmarks/ops/bench_instance_norm.py ===
benchmarks/ops/bench_instance_norm.py::test_instance_norm_bench[image-affine-float16]
benchmarks/ops/bench_instance_norm.py::test_instance_norm_bench[image-affine-bfloat16]
benchmarks/ops/bench_instance_norm.py::test_instance_norm_bench[wider-channel-affine-float16]
benchmarks/ops/bench_instance_norm.py::test_instance_norm_bench[tail-spatial-affine-float16]
benchmarks/ops/bench_instance_norm.py::test_instance_norm_bench[image-float16]
benchmarks/ops/bench_instance_norm.py::test_instance_norm_bench[image-bfloat16]
benchmarks/ops/bench_instance_norm.py::test_instance_norm_bench[wider-channel-float16]
benchmarks/ops/bench_instance_norm.py::test_instance_norm_bench[tail-spatial-float16]

8 tests collected in 1.90s
........                                                                 [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_instance_norm.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_instance_norm.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
8 passed, 58 warnings in 52.30s
--- benchmarks/ops/bench_instance_norm.py finished in 53s ---

=== [35/54] benchmarks/ops/bench_logical_reduce.py ===
benchmarks/ops/bench_logical_reduce.py::test_any_bench[mask-validation-4k-bool]
benchmarks/ops/bench_logical_reduce.py::test_any_bench[mask-validation-32k-bool]
benchmarks/ops/bench_logical_reduce.py::test_any_bench[3d-multidim-reduce-bool]
benchmarks/ops/bench_logical_reduce.py::test_all_bench[mask-validation-4k-bool]
benchmarks/ops/bench_logical_reduce.py::test_all_bench[mask-validation-32k-bool]
benchmarks/ops/bench_logical_reduce.py::test_all_bench[3d-multidim-reduce-bool]
benchmarks/ops/bench_logical_reduce.py::test_count_nonzero_bench[sparsity-hidden-float16]
benchmarks/ops/bench_logical_reduce.py::test_count_nonzero_bench[sparsity-hidden-bfloat16]
benchmarks/ops/bench_logical_reduce.py::test_count_nonzero_bench[sparsity-seq-float16]
benchmarks/ops/bench_logical_reduce.py::test_count_nonzero_bench[3d-multidim-reduce-float16]

10 tests collected in 2.05s
..........                                                               [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_logical_reduce.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_logical_reduce.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
10 passed, 58 warnings in 19.08s
--- benchmarks/ops/bench_logical_reduce.py finished in 20s ---

=== [36/54] benchmarks/ops/bench_mamba.py ===
benchmarks/ops/bench_mamba.py::test_cb_producer_fwd_bench[mamba2-780m-b1-s4k-float16]
benchmarks/ops/bench_mamba.py::test_cb_producer_fwd_bench[mamba2-2p7b-b4-s2k-bfloat16]
benchmarks/ops/bench_mamba.py::test_da_cumsum_fwd_bench[mamba2-780m-b1-s4k-float16]
benchmarks/ops/bench_mamba.py::test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-bfloat16]
benchmarks/ops/bench_mamba.py::test_da_cumsum_fwd_bench[mamba2-780m-b1-s4k-dt-bias-float16]
benchmarks/ops/bench_mamba.py::test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-dt-bias-bfloat16]
benchmarks/ops/bench_mamba.py::test_da_cumsum_fwd_bench[mamba2-2p7b-b2-s32k-dt-bias-float16]
benchmarks/ops/bench_mamba.py::test_ssd_chunk_scan_fwd_bench[mamba2-780m-b1-s4k-float16]
benchmarks/ops/bench_mamba.py::test_ssd_chunk_scan_fwd_bench[mamba2-780m-b1-s4k-bfloat16]
benchmarks/ops/bench_mamba.py::test_ssd_chunk_scan_fwd_bench[mamba2-2p7b-b4-s2k-bfloat16]
benchmarks/ops/bench_mamba.py::test_ssd_chunk_scan_fwd_bench[mamba2-1p3b-b2-s32k-float16]
benchmarks/ops/bench_mamba.py::test_ssd_chunk_state_fwd_bench[mamba2-780m-b1-s4k-float16]
benchmarks/ops/bench_mamba.py::test_ssd_chunk_state_fwd_bench[mamba2-780m-b1-s4k-bfloat16]
benchmarks/ops/bench_mamba.py::test_ssd_chunk_state_fwd_bench[mamba2-2p7b-b4-s2k-bfloat16]
benchmarks/ops/bench_mamba.py::test_ssd_chunk_state_fwd_bench[mamba2-780m-b1-s4k-seq-idx-float16]
benchmarks/ops/bench_mamba.py::test_ssd_chunk_state_fwd_bench[mamba2-780m-b1-s4k-seq-idx-bfloat16]
benchmarks/ops/bench_mamba.py::test_ssd_chunk_state_fwd_bench[mamba2-1p3b-b2-s32k-seq-idx-float16]
benchmarks/ops/bench_mamba.py::test_ssd_state_passing_fwd_bench[mamba2-1p3b-b1-s4k-dstate-float16]
benchmarks/ops/bench_mamba.py::test_ssd_state_passing_fwd_bench[mamba2-1p3b-b1-s4k-dstate-bfloat16]
benchmarks/ops/bench_mamba.py::test_ssd_state_passing_fwd_bench[mamba2-2p7b-b2-s32k-dstate-float16]
benchmarks/ops/bench_mamba.py::test_ssd_state_passing_fwd_bench[mamba2-1p3b-b1-s4k-dstate-init-states-float16]
benchmarks/ops/bench_mamba.py::test_ssd_state_passing_fwd_bench[mamba2-1p3b-b1-s4k-dstate-init-states-bfloat16]
benchmarks/ops/bench_mamba.py::test_ssd_state_passing_fwd_bench[mamba2-1p3b-b1-s4k-flat-init-states-float32]
benchmarks/ops/bench_mamba.py::test_ssd_decode_bench[mamba2-1p3b-decode-b1-float16]
benchmarks/ops/bench_mamba.py::test_ssd_decode_bench[mamba2-1p3b-decode-b1-bfloat16]
benchmarks/ops/bench_mamba.py::test_ssd_decode_bench[mamba2-2p7b-decode-b8-float16]
benchmarks/ops/bench_mamba.py::test_ssd_decode_bench[mamba2-780m-decode-b32-float16]

27 tests collected in 10.11s
...........................                                              [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_mamba.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

benchmarks/ops/bench_mamba.py::test_ssd_chunk_scan_fwd_bench[mamba2-780m-b1-s4k-float16]
  /usr/local/lib/python3.12/dist-packages/torch/_inductor/compile_fx.py:321: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
27 passed, 15 warnings in 119.75s (0:01:59)
--- benchmarks/ops/bench_mamba.py finished in 120s ---

=== [37/54] benchmarks/ops/bench_mamba2_e2e.py ===
benchmarks/ops/bench_mamba2_e2e.py::test_mamba2_fwd_bench[mamba2-2p7b-b1-s2k-bfloat16]
benchmarks/ops/bench_mamba2_e2e.py::test_mamba2_fwd_bench[mamba2-1p3b-b1-s8k-float16]
benchmarks/ops/bench_mamba2_e2e.py::test_mamba2_fwd_bench[mamba2-2p7b-b1-s2k-dt-bias-bfloat16]
benchmarks/ops/bench_mamba2_e2e.py::test_mamba2_fwd_bench[mamba2-1p3b-b1-s8k-dt-bias-float16]
benchmarks/ops/bench_mamba2_e2e.py::test_mamba2_fwd_bench[mamba2-2p7b-b1-s2k-init-states-bfloat16]
benchmarks/ops/bench_mamba2_e2e.py::test_mamba2_fwd_bench[mamba2-1p3b-b1-s8k-init-states-float16]
benchmarks/ops/bench_mamba2_e2e.py::test_mamba2_fwd_bench[mamba2-2p7b-b1-s2k-dt-bias-init-states-bfloat16]
benchmarks/ops/bench_mamba2_e2e.py::test_mamba2_fwd_bench[mamba2-1p3b-b1-s8k-dt-bias-init-states-float16]

8 tests collected in 9.91s
........                                                                 [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_mamba2_e2e.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

benchmarks/ops/bench_mamba2_e2e.py::test_mamba2_fwd_bench[mamba2-2p7b-b1-s2k-bfloat16]
  /usr/local/lib/python3.12/dist-packages/torch/_inductor/compile_fx.py:321: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
8 passed, 15 warnings in 65.80s (0:01:05)
--- benchmarks/ops/bench_mamba2_e2e.py finished in 66s ---

=== [38/54] benchmarks/ops/bench_mean_pooling.py ===
benchmarks/ops/bench_mean_pooling.py::test_mean_pooling_bench[uniform-8k-float16]
benchmarks/ops/bench_mean_pooling.py::test_mean_pooling_bench[uniform-batched-float16]
benchmarks/ops/bench_mean_pooling.py::test_mean_pooling_bench[ragged-even-float16]
benchmarks/ops/bench_mean_pooling.py::test_mean_pooling_bench[ragged-tail-float16]
benchmarks/ops/bench_mean_pooling.py::test_mean_pooling_bench[ragged-batched-float16]

5 tests collected in 1.89s
.....                                                                    [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_mean_pooling.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
5 passed, 14 warnings in 40.70s
--- benchmarks/ops/bench_mean_pooling.py finished in 41s ---

=== [39/54] benchmarks/ops/bench_mhc.py ===
benchmarks/ops/bench_mhc.py::test_mhc_pre_bench[pre-small-bfloat16]
benchmarks/ops/bench_mhc.py::test_mhc_pre_bench[pre-medium-bfloat16]
benchmarks/ops/bench_mhc.py::test_mhc_pre_bench[pre-large-bfloat16]
benchmarks/ops/bench_mhc.py::test_mhc_post_bench[post-small-bfloat16]
benchmarks/ops/bench_mhc.py::test_mhc_post_bench[post-medium-bfloat16]
benchmarks/ops/bench_mhc.py::test_mhc_post_bench[post-large-bfloat16]

6 tests collected in 1.99s
......                                                                   [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_mhc.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

benchmarks/ops/bench_mhc.py::test_mhc_pre_bench[pre-small-bfloat16]
  /usr/local/lib/python3.12/dist-packages/torch/_inductor/compile_fx.py:321: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
6 passed, 15 warnings in 15.77s
--- benchmarks/ops/bench_mhc.py finished in 16s ---

=== [40/54] benchmarks/ops/bench_moe_fused_moe.py ===
benchmarks/ops/bench_moe_fused_moe.py::test_fused_moe_fwd_bench[qwen3-235b-decode-bfloat16]
benchmarks/ops/bench_moe_fused_moe.py::test_fused_moe_fwd_bench[qwen3-235b-prefill-bfloat16]
benchmarks/ops/bench_moe_fused_moe.py::test_fused_moe_fwd_bench[deepseek-v3-decode-bfloat16]
benchmarks/ops/bench_moe_fused_moe.py::test_fused_moe_fwd_bench[deepseek-v3-prefill-bfloat16]
benchmarks/ops/bench_moe_fused_moe.py::test_fused_moe_fwd_bench[kimi-k2-decode-bfloat16]
benchmarks/ops/bench_moe_fused_moe.py::test_fused_moe_fwd_bench[kimi-k2-prefill-bfloat16]

=============================== warnings summary ===============================
../../../../../../usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
6 tests collected in 12.75s
......                                                                   [100%]Benchmark report saved to profile_run.log

6 passed in 16.53s
--- benchmarks/ops/bench_moe_fused_moe.py finished in 17s ---

=== [41/54] benchmarks/ops/bench_moe_fused_topk.py ===
benchmarks/ops/bench_moe_fused_topk.py::test_fused_topk_bench[kimi-k2-t32-bfloat16]
benchmarks/ops/bench_moe_fused_topk.py::test_fused_topk_bench[kimi-k2-t512-bfloat16]
benchmarks/ops/bench_moe_fused_topk.py::test_fused_topk_bench[kimi-k2-t4096-bfloat16]
benchmarks/ops/bench_moe_fused_topk.py::test_fused_topk_bench[kimi-k2-t512-bias-bfloat16]
benchmarks/ops/bench_moe_fused_topk.py::test_fused_topk_bench[qwen3-235b-t32-bfloat16]
benchmarks/ops/bench_moe_fused_topk.py::test_fused_topk_bench[qwen3-235b-t512-bfloat16]
benchmarks/ops/bench_moe_fused_topk.py::test_fused_topk_bench[qwen3-235b-t4096-bfloat16]

=============================== warnings summary ===============================
../../../../../../usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
7 tests collected in 12.54s
.......                                                                  [100%]Benchmark report saved to profile_run.log

7 passed in 2.94s
--- benchmarks/ops/bench_moe_fused_topk.py finished in 4s ---

=== [42/54] benchmarks/ops/bench_moe_gate_up.py ===
benchmarks/ops/bench_moe_gate_up.py::test_moe_gate_up_bench[deepseek-v3-decode-gate-up-bfloat16]
benchmarks/ops/bench_moe_gate_up.py::test_moe_gate_up_bench[deepseek-v3-prefill-gate-up-bfloat16]

2 tests collected in 1.92s
..                                                                       [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_moe_gate_up.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
2 passed, 14 warnings in 50.93s
--- benchmarks/ops/bench_moe_gate_up.py finished in 52s ---

=== [43/54] benchmarks/ops/bench_moe_grouped_gemm_nopad.py ===
benchmarks/ops/bench_moe_grouped_gemm_nopad.py::test_moe_grouped_gemm_nopad_bench[deepseek-v3-decode-gate-up-bfloat16]
benchmarks/ops/bench_moe_grouped_gemm_nopad.py::test_moe_grouped_gemm_nopad_bench[deepseek-v3-prefill-gate-up-bfloat16]
benchmarks/ops/bench_moe_grouped_gemm_nopad.py::test_moe_grouped_gemm_nopad_bench[deepseek-v3-decode-down-bfloat16]
benchmarks/ops/bench_moe_grouped_gemm_nopad.py::test_moe_grouped_gemm_nopad_bench[deepseek-v3-prefill-down-bfloat16]

4 tests collected in 1.99s
....                                                                     [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_moe_grouped_gemm_nopad.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
4 passed, 14 warnings in 57.63s
--- benchmarks/ops/bench_moe_grouped_gemm_nopad.py finished in 58s ---

=== [44/54] benchmarks/ops/bench_moe_permute_align.py ===
benchmarks/ops/bench_moe_permute_align.py::test_permute_align_bench[kimi-k2-decode-int32]
benchmarks/ops/bench_moe_permute_align.py::test_permute_align_bench[kimi-k2-small-int32]
benchmarks/ops/bench_moe_permute_align.py::test_permute_align_bench[kimi-k2-medium-int32]
benchmarks/ops/bench_moe_permute_align.py::test_permute_align_bench[kimi-k2-prefill-int32]
benchmarks/ops/bench_moe_permute_align.py::test_permute_align_bench[deepseek-v3-decode-int32]
benchmarks/ops/bench_moe_permute_align.py::test_permute_align_bench[deepseek-v3-small-int32]
benchmarks/ops/bench_moe_permute_align.py::test_permute_align_bench[deepseek-v3-medium-int32]
benchmarks/ops/bench_moe_permute_align.py::test_permute_align_bench[deepseek-v3-prefill-int32]
benchmarks/ops/bench_moe_permute_align.py::test_permute_align_bench[qwen3-decode-int32]
benchmarks/ops/bench_moe_permute_align.py::test_permute_align_bench[qwen3-small-int32]
benchmarks/ops/bench_moe_permute_align.py::test_permute_align_bench[qwen3-medium-int32]
benchmarks/ops/bench_moe_permute_align.py::test_permute_align_bench[qwen3-prefill-int32]

12 tests collected in 2.14s
............                                                             [100%]Benchmark report saved to profile_run.log

12 passed in 7.89s
--- benchmarks/ops/bench_moe_permute_align.py finished in 8s ---

=== [45/54] benchmarks/ops/bench_moe_shared_fused_moe.py ===
benchmarks/ops/bench_moe_shared_fused_moe.py::test_shared_fused_moe_bench[1-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16]
benchmarks/ops/bench_moe_shared_fused_moe.py::test_shared_fused_moe_bench[32-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16]
benchmarks/ops/bench_moe_shared_fused_moe.py::test_shared_fused_moe_bench[512-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16]
benchmarks/ops/bench_moe_shared_fused_moe.py::test_shared_fused_moe_bench[2048-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16]
benchmarks/ops/bench_moe_shared_fused_moe.py::test_shared_fused_moe_bench[4096-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16]

=============================== warnings summary ===============================
../../../../../../usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
5 tests collected in 12.63s
.....                                                                    [100%]Benchmark report saved to profile_run.log

5 passed in 15.34s
--- benchmarks/ops/bench_moe_shared_fused_moe.py finished in 16s ---

=== [46/54] benchmarks/ops/bench_moe_staged.py ===
benchmarks/ops/bench_moe_staged.py::test_moe_pre_permute_bench[small-float16]
benchmarks/ops/bench_moe_staged.py::test_moe_pre_permute_bench[small-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_pre_permute_bench[prefill-float16]
benchmarks/ops/bench_moe_staged.py::test_moe_pre_permute_bench[prefill-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_post_permute_bench[small-float16]
benchmarks/ops/bench_moe_staged.py::test_moe_post_permute_bench[small-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_post_permute_bench[prefill-float16]
benchmarks/ops/bench_moe_staged.py::test_moe_post_permute_bench[prefill-bfloat16]

=============================== warnings summary ===============================
../../../../../../usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
8 tests collected in 12.66s
........                                                                 [100%]Benchmark report saved to profile_run.log

8 passed in 4.07s
--- benchmarks/ops/bench_moe_staged.py finished in 5s ---

=== [47/54] benchmarks/ops/bench_norm.py ===
benchmarks/ops/bench_norm.py::test_rms_norm_bench[llama-8b-prefill-float16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[llama-8b-prefill-bfloat16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[llama-8b-decode-bfloat16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[llama-70b-prefill-float16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[llama-70b-prefill-bfloat16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[llama-70b-decode-bfloat16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[llama-405b-prefill-float16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[llama-405b-prefill-bfloat16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[llama-405b-decode-bfloat16]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_bench[llama-8b-prefill-float16]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_bench[llama-8b-prefill-bfloat16]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_bench[llama-8b-decode-bfloat16]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_bench[llama-70b-prefill-float16]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_bench[llama-70b-prefill-bfloat16]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_bench[llama-70b-decode-bfloat16]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_bench[llama-405b-prefill-float16]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_bench[llama-405b-prefill-bfloat16]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_bench[llama-405b-decode-bfloat16]
benchmarks/ops/bench_norm.py::test_layer_norm_bench[llama-8b-prefill-float16]
benchmarks/ops/bench_norm.py::test_layer_norm_bench[llama-8b-prefill-bfloat16]
benchmarks/ops/bench_norm.py::test_layer_norm_bench[llama-8b-decode-bfloat16]
benchmarks/ops/bench_norm.py::test_layer_norm_bench[llama-70b-prefill-float16]
benchmarks/ops/bench_norm.py::test_layer_norm_bench[llama-70b-prefill-bfloat16]
benchmarks/ops/bench_norm.py::test_layer_norm_bench[llama-70b-decode-bfloat16]
benchmarks/ops/bench_norm.py::test_layer_norm_bench[llama-405b-prefill-float16]
benchmarks/ops/bench_norm.py::test_layer_norm_bench[llama-405b-prefill-bfloat16]
benchmarks/ops/bench_norm.py::test_layer_norm_bench[llama-405b-decode-bfloat16]
benchmarks/ops/bench_norm.py::test_fused_add_layer_norm_bench[llama-8b-prefill-float16]
benchmarks/ops/bench_norm.py::test_fused_add_layer_norm_bench[llama-8b-prefill-bfloat16]
benchmarks/ops/bench_norm.py::test_fused_add_layer_norm_bench[llama-8b-decode-bfloat16]
benchmarks/ops/bench_norm.py::test_fused_add_layer_norm_bench[llama-70b-prefill-float16]
benchmarks/ops/bench_norm.py::test_fused_add_layer_norm_bench[llama-70b-prefill-bfloat16]
benchmarks/ops/bench_norm.py::test_fused_add_layer_norm_bench[llama-70b-decode-bfloat16]

33 tests collected in 1.97s
.................................                                        [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_norm.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_norm.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
33 passed, 58 warnings in 44.21s
--- benchmarks/ops/bench_norm.py finished in 45s ---

=== [48/54] benchmarks/ops/bench_pool.py ===
benchmarks/ops/bench_pool.py::test_avg_pool1d_bench[audio-downsample-float16]
benchmarks/ops/bench_pool.py::test_avg_pool1d_bench[long-temporal-float16]
benchmarks/ops/bench_pool.py::test_avg_pool1d_bench[ceil-bfloat16]
benchmarks/ops/bench_pool.py::test_avg_pool2d_bench[vision-3x3-s2-float16]
benchmarks/ops/bench_pool.py::test_avg_pool2d_bench[vision-5x5-s2-float16]
benchmarks/ops/bench_pool.py::test_avg_pool2d_bench[ceil-divisor-bfloat16]
benchmarks/ops/bench_pool.py::test_avg_pool3d_bench[video-2x2x2-float16]
benchmarks/ops/bench_pool.py::test_avg_pool3d_bench[ceil-video-float16]
benchmarks/ops/bench_pool.py::test_avg_pool3d_bench[divisor-bfloat16]
benchmarks/ops/bench_pool.py::test_max_pool2d_bench[resnet-stem-float16]
benchmarks/ops/bench_pool.py::test_max_pool2d_bench[resnet-stem-bfloat16]
benchmarks/ops/bench_pool.py::test_max_pool2d_bench[resnet-stem-float32]
benchmarks/ops/bench_pool.py::test_max_pool2d_bench[vgg-block-float16]
benchmarks/ops/bench_pool.py::test_max_pool2d_bench[vgg-block-bfloat16]
benchmarks/ops/bench_pool.py::test_max_pool2d_bench[vgg-block-float32]
benchmarks/ops/bench_pool.py::test_max_pool2d_bench[alexnet-ceil-float16]
benchmarks/ops/bench_pool.py::test_max_pool2d_bench[alexnet-ceil-bfloat16]
benchmarks/ops/bench_pool.py::test_max_pool2d_bench[alexnet-ceil-float32]
benchmarks/ops/bench_pool.py::test_max_pool2d_indices_bench[resnet-stem-float16]
benchmarks/ops/bench_pool.py::test_max_pool2d_indices_bench[resnet-stem-bfloat16]
benchmarks/ops/bench_pool.py::test_max_pool2d_indices_bench[resnet-stem-float32]
benchmarks/ops/bench_pool.py::test_max_pool2d_indices_bench[vgg-block-float16]
benchmarks/ops/bench_pool.py::test_max_pool2d_indices_bench[vgg-block-bfloat16]
benchmarks/ops/bench_pool.py::test_max_pool2d_indices_bench[vgg-block-float32]
benchmarks/ops/bench_pool.py::test_max_pool2d_indices_bench[alexnet-ceil-float16]
benchmarks/ops/bench_pool.py::test_max_pool2d_indices_bench[alexnet-ceil-bfloat16]
benchmarks/ops/bench_pool.py::test_max_pool2d_indices_bench[alexnet-ceil-float32]
benchmarks/ops/bench_pool.py::test_max_pool1d_bench[sincnet-speaker-local-float16]
benchmarks/ops/bench_pool.py::test_max_pool1d_bench[textcnn-global-float16]
benchmarks/ops/bench_pool.py::test_max_pool1d_bench[ecg-cnn-dilated-bfloat16]
benchmarks/ops/bench_pool.py::test_max_pool1d_indices_bench[sincnet-speaker-local-float16]
benchmarks/ops/bench_pool.py::test_max_pool1d_indices_bench[textcnn-global-float16]
benchmarks/ops/bench_pool.py::test_max_pool1d_indices_bench[ecg-cnn-dilated-bfloat16]
benchmarks/ops/bench_pool.py::test_max_pool3d_bench[c3d-pool1-float16]
benchmarks/ops/bench_pool.py::test_max_pool3d_bench[c3d-pool2-float16]
benchmarks/ops/bench_pool.py::test_max_pool3d_bench[medicalnet-stem-bfloat16]
benchmarks/ops/bench_pool.py::test_max_pool3d_indices_bench[c3d-pool1-float16]
benchmarks/ops/bench_pool.py::test_max_pool3d_indices_bench[c3d-pool2-float16]
benchmarks/ops/bench_pool.py::test_max_pool3d_indices_bench[medicalnet-stem-bfloat16]
benchmarks/ops/bench_pool.py::test_adaptive_avg_pool2d_bench[resnet-global-float16]
benchmarks/ops/bench_pool.py::test_adaptive_avg_pool2d_bench[spp-6x6-float16]
benchmarks/ops/bench_pool.py::test_adaptive_avg_pool2d_bench[nondiv-7x7-bfloat16]
benchmarks/ops/bench_pool.py::test_adaptive_max_pool2d_bench[global-1x1-float16]
benchmarks/ops/bench_pool.py::test_adaptive_max_pool2d_bench[spp-6x6-float16]
benchmarks/ops/bench_pool.py::test_adaptive_max_pool2d_bench[nondiv-7x7-bfloat16]
benchmarks/ops/bench_pool.py::test_adaptive_max_pool2d_indices_bench[global-1x1-float16]
benchmarks/ops/bench_pool.py::test_adaptive_max_pool2d_indices_bench[spp-6x6-float16]
benchmarks/ops/bench_pool.py::test_adaptive_max_pool2d_indices_bench[nondiv-7x7-bfloat16]

48 tests collected in 1.95s
..........................................FFFFFF                         [100%]Benchmark report saved to profile_run.log

=================================== FAILURES ===================================
______________ test_adaptive_max_pool2d_bench[global-1x1-float16] ______________

n = 8, c_in = 2048, h_in = 7, w_in = 7, output_size = (1, 1)
dtype = torch.float16, tune = True

    @pytest.mark.parametrize(
        "n, c_in, h_in, w_in, output_size, dtype, tune",
        workload_params(load_workloads(AdaptiveMaxPool2dFwdOp), _adaptive_pool2d_args),
    )
    def test_adaptive_max_pool2d_bench(
        n: int,
        c_in: int,
        h_in: int,
        w_in: int,
        output_size: tuple[int, int],
        dtype: torch.dtype,
        tune: bool,
    ) -> None:
        test = AdaptiveMaxPool2dBenchmarkWorkload(n, c_in, h_in, w_in, output_size, dtype)
        inputs = test.gen_inputs()
    
        op = AdaptiveMaxPool2dFwdOp(output_size=output_size, tune=tune)
        bm = ManifestBenchmark(op, test)
    
        _tag, _baseline_fn = pool_baseline(type(op).__name__, test, *inputs)
>       bm.compare(
            {
                "tileops": op,
                _tag: _baseline_fn,
                "torch-ref": test.ref_program,
                "torch-compile": compiled_reference(test),
            },
            *inputs,
        )

benchmarks/ops/bench_pool.py:1418: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
benchmarks/benchmark_base.py:370: in compare
    bench_kernel(
benchmarks/timing.py:629: in bench_kernel
    _call_raw()
benchmarks/timing.py:626: in _call_raw
    return fn(*args) if args else fn()
           ^^^^^^^^^
src/tileops/ops/op_base.py:607: in __call__
    return self.forward(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
src/tileops/ops/pool.py:1498: in forward
    return type(self)._wrapped(input, self._instance_key)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_library/custom_ops.py:863: in __call__
    return self._opoverload(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_ops.py:875: in __call__
    return self._op(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_library/autograd.py:123: in autograd_impl
    result = forward_no_grad(*args, Metadata(keyset, keyword_only_args))
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_library/autograd.py:41: in forward_no_grad
    result = op.redispatch(keyset & _C._after_autograd_keyset, *args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_ops.py:882: in redispatch
    return self._handle.redispatch_boxed(keyset, *args, **kwargs)  # type: ignore[return-value]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_library/custom_ops.py:441: in backend_impl
    result = self._backend_fns[device_type](*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_compile.py:54: in inner
    return disable_fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_dynamo/eval_frame.py:1446: in _fn
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_library/custom_ops.py:502: in wrapped_fn
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
src/tileops/ops/pool.py:1718: in _fwd
    return get_instance(instance_key)._eager_forward(input)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
src/tileops/ops/pool.py:1521: in _eager_forward
    kernel = self.get_or_build_kernel(
src/tileops/ops/op_base.py:388: in get_or_build_kernel
    entries[key] = build()
                   ^^^^^^^
src/tileops/ops/pool.py:1525: in <lambda>
    build=lambda: self.kernel_map[self._kernel_slot](
src/tileops/kernels/pool/common.py:104: in __init__
    self.init_config(config, tune)
src/tileops/kernels/kernel_base.py:179: in init_config
    self.autotune()
src/tileops/kernels/kernel_base.py:379: in autotune
    tuned_kernel = self.tune_jit_kernel(
src/tileops/kernels/kernel_base.py:367: in tune_jit_kernel
    return self._call_autotuned_kernel(autotuned_kernel_fn, jit_kernel, seed_config)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
src/tileops/kernels/kernel_base.py:279: in _call_autotuned_kernel
    return autotuned_kernel_fn(**self._autotune_initial_kwargs(kernel=kernel, config=config))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/tilelang/autotuner/tuner.py:1329: in __call__
    artifact = autotuner.run()
               ^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <tilelang.autotuner.tuner.AutoTuner object at 0xde891f69730>, warmup = 25
rep = 50, timeout = 100, use_pipeline = False, enable_grouped_compile = False
group_compile_size = 2, benchmark_devices = None, benchmark_multi_gpu = False

    def run(
        self,
        warmup: int = 25,
        rep: int = 100,
        timeout: int = 180,
        use_pipeline: bool = False,
        enable_grouped_compile: bool = False,
        group_compile_size: int = 2,
        benchmark_devices: list[int] | None = None,
        benchmark_multi_gpu: bool = False,
    ):
        """Run the auto-tuning process.
    
        Args:
            warmup: Number of warmup iterations.
            rep: Number of repetitions for timing.
            timeout: Maximum time per configuration.
            use_pipeline: Whether to pipeline benchmarking with compilation.
            enable_grouped_compile: Whether to enable grouped compilation.
            group_compile_size: Number of configurations in one compile unit.
            benchmark_devices: CUDA device ordinals used for benchmark workers when benchmark_multi_gpu=True.
            benchmark_multi_gpu: Whether to benchmark configurations across multiple CUDA GPUs.
    
        Returns:
            AutotuneResult: Results of the auto-tuning process.
        """
        _init_logger_handlers()
    
        sig = inspect.signature(self.fn)
        parameters = sig.parameters
    
        # NOTE(chaofan):  We need to extract some parameters from the closure.
        # Consider the case:
        #   def gemm(M, N, K):
        #       def kernel(...)
        # If we only extract source, M/N/K will be symbolic and there will be cache problem.
        extra_parameters: dict[str, Any] = {}
        cells = self.fn.__closure__
        var_names = self.fn.__code__.co_freevars
        if cells is not None:
            assert len(var_names) == len(cells), "Number of free variables does not match"
            for var_name, cell in zip(var_names, cells):
                if var_name in parameters:
                    continue
                # Cell content must be serializable
>               assert isinstance(cell.cell_contents, (int, float, str, bool, type(None))), (
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                    f"Cell contents {cell.cell_contents} is not serializable: {type(cell.cell_contents)}"
                )
E               AssertionError: Cell contents <tileops.kernels.pool.adaptive_max_pool2d._PlaneStaging object at 0xde8d823a660> is not serializable: <class 'tileops.kernels.pool.adaptive_max_pool2d._PlaneStaging'>

/usr/local/lib/python3.12/dist-packages/tilelang/autotuner/tuner.py:927: AssertionError
----------------------------- Captured stdout call -----------------------------
Start autotuning AdaptiveMaxPool2dKernel...
_______________ test_adaptive_max_pool2d_bench[spp-6x6-float16] ________________

n = 2, c_in = 128, h_in = 56, w_in = 56, output_size = (6, 6)
dtype = torch.float16, tune = True

    @pytest.mark.parametrize(
        "n, c_in, h_in, w_in, output_size, dtype, tune",
        workload_params(load_workloads(AdaptiveMaxPool2dFwdOp), _adaptive_pool2d_args),
    )
    def test_adaptive_max_pool2d_bench(
        n: int,
        c_in: int,
        h_in: int,
        w_in: int,
        output_size: tuple[int, int],
        dtype: torch.dtype,
        tune: bool,
    ) -> None:
        test = AdaptiveMaxPool2dBenchmarkWorkload(n, c_in, h_in, w_in, output_size, dtype)
        inputs = test.gen_inputs()
    
        op = AdaptiveMaxPool2dFwdOp(output_size=output_size, tune=tune)
        bm = ManifestBenchmark(op, test)
    
        _tag, _baseline_fn = pool_baseline(type(op).__name__, test, *inputs)
>       bm.compare(
            {
                "tileops": op,
                _tag: _baseline_fn,
                "torch-ref": test.ref_program,
                "torch-compile": compiled_reference(test),
            },
            *inputs,
        )

benchmarks/ops/bench_pool.py:1418: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
benchmarks/benchmark_base.py:370: in compare
    bench_kernel(
benchmarks/timing.py:629: in bench_kernel
    _call_raw()
benchmarks/timing.py:626: in _call_raw
    return fn(*args) if args else fn()
           ^^^^^^^^^
src/tileops/ops/op_base.py:607: in __call__
    return self.forward(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
src/tileops/ops/pool.py:1498: in forward
    return type(self)._wrapped(input, self._instance_key)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_library/custom_ops.py:863: in __call__
    return self._opoverload(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_ops.py:875: in __call__
    return self._op(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_library/autograd.py:123: in autograd_impl
    result = forward_no_grad(*args, Metadata(keyset, keyword_only_args))
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_library/autograd.py:41: in forward_no_grad
    result = op.redispatch(keyset & _C._after_autograd_keyset, *args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_ops.py:882: in redispatch
    return self._handle.redispatch_boxed(keyset, *args, **kwargs)  # type: ignore[return-value]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_library/custom_ops.py:441: in backend_impl
    result = self._backend_fns[device_type](*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_compile.py:54: in inner
    return disable_fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_dynamo/eval_frame.py:1446: in _fn
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_library/custom_ops.py:502: in wrapped_fn
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
src/tileops/ops/pool.py:1718: in _fwd
    return get_instance(instance_key)._eager_forward(input)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
src/tileops/ops/pool.py:1521: in _eager_forward
    kernel = self.get_or_build_kernel(
src/tileops/ops/op_base.py:388: in get_or_build_kernel
    entries[key] = build()
                   ^^^^^^^
src/tileops/ops/pool.py:1525: in <lambda>
    build=lambda: self.kernel_map[self._kernel_slot](
src/tileops/kernels/pool/common.py:104: in __init__
    self.init_config(config, tune)
src/tileops/kernels/kernel_base.py:179: in init_config
    self.autotune()
src/tileops/kernels/kernel_base.py:379: in autotune
    tuned_kernel = self.tune_jit_kernel(
src/tileops/kernels/kernel_base.py:367: in tune_jit_kernel
    return self._call_autotuned_kernel(autotuned_kernel_fn, jit_kernel, seed_config)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
src/tileops/kernels/kernel_base.py:279: in _call_autotuned_kernel
    return autotuned_kernel_fn(**self._autotune_initial_kwargs(kernel=kernel, config=config))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/tilelang/autotuner/tuner.py:1329: in __call__
    artifact = autotuner.run()
               ^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <tilelang.autotuner.tuner.AutoTuner object at 0xde88d5434a0>, warmup = 25
rep = 50, timeout = 100, use_pipeline = False, enable_grouped_compile = False
group_compile_size = 2, benchmark_devices = None, benchmark_multi_gpu = False

    def run(
        self,
        warmup: int = 25,
        rep: int = 100,
        timeout: int = 180,
        use_pipeline: bool = False,
        enable_grouped_compile: bool = False,
        group_compile_size: int = 2,
        benchmark_devices: list[int] | None = None,
        benchmark_multi_gpu: bool = False,
    ):
        """Run the auto-tuning process.
    
        Args:
            warmup: Number of warmup iterations.
            rep: Number of repetitions for timing.
            timeout: Maximum time per configuration.
            use_pipeline: Whether to pipeline benchmarking with compilation.
            enable_grouped_compile: Whether to enable grouped compilation.
            group_compile_size: Number of configurations in one compile unit.
            benchmark_devices: CUDA device ordinals used for benchmark workers when benchmark_multi_gpu=True.
            benchmark_multi_gpu: Whether to benchmark configurations across multiple CUDA GPUs.
    
        Returns:
            AutotuneResult: Results of the auto-tuning process.
        """
        _init_logger_handlers()
    
        sig = inspect.signature(self.fn)
        parameters = sig.parameters
    
        # NOTE(chaofan):  We need to extract some parameters from the closure.
        # Consider the case:
        #   def gemm(M, N, K):
        #       def kernel(...)
        # If we only extract source, M/N/K will be symbolic and there will be cache problem.
        extra_parameters: dict[str, Any] = {}
        cells = self.fn.__closure__
        var_names = self.fn.__code__.co_freevars
        if cells is not None:
            assert len(var_names) == len(cells), "Number of free variables does not match"
            for var_name, cell in zip(var_names, cells):
                if var_name in parameters:
                    continue
                # Cell content must be serializable
>               assert isinstance(cell.cell_contents, (int, float, str, bool, type(None))), (
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                    f"Cell contents {cell.cell_contents} is not serializable: {type(cell.cell_contents)}"
                )
E               AssertionError: Cell contents <tileops.kernels.pool.adaptive_max_pool2d._PlaneStaging object at 0xde88d543fb0> is not serializable: <class 'tileops.kernels.pool.adaptive_max_pool2d._PlaneStaging'>

/usr/local/lib/python3.12/dist-packages/tilelang/autotuner/tuner.py:927: AssertionError
----------------------------- Captured stdout call -----------------------------
Start autotuning AdaptiveMaxPool2dKernel...
_____________ test_adaptive_max_pool2d_bench[nondiv-7x7-bfloat16] ______________

n = 2, c_in = 64, h_in = 55, w_in = 57, output_size = (7, 7)
dtype = torch.bfloat16, tune = True

    @pytest.mark.parametrize(
        "n, c_in, h_in, w_in, output_size, dtype, tune",
        workload_params(load_workloads(AdaptiveMaxPool2dFwdOp), _adaptive_pool2d_args),
    )
    def test_adaptive_max_pool2d_bench(
        n: int,
        c_in: int,
        h_in: int,
        w_in: int,
        output_size: tuple[int, int],
        dtype: torch.dtype,
        tune: bool,
    ) -> None:
        test = AdaptiveMaxPool2dBenchmarkWorkload(n, c_in, h_in, w_in, output_size, dtype)
        inputs = test.gen_inputs()
    
        op = AdaptiveMaxPool2dFwdOp(output_size=output_size, tune=tune)
        bm = ManifestBenchmark(op, test)
    
        _tag, _baseline_fn = pool_baseline(type(op).__name__, test, *inputs)
>       bm.compare(
            {
                "tileops": op,
                _tag: _baseline_fn,
                "torch-ref": test.ref_program,
                "torch-compile": compiled_reference(test),
            },
            *inputs,
        )

benchmarks/ops/bench_pool.py:1418: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
benchmarks/benchmark_base.py:370: in compare
    bench_kernel(
benchmarks/timing.py:629: in bench_kernel
    _call_raw()
benchmarks/timing.py:626: in _call_raw
    return fn(*args) if args else fn()
           ^^^^^^^^^
src/tileops/ops/op_base.py:607: in __call__
    return self.forward(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
src/tileops/ops/pool.py:1498: in forward
    return type(self)._wrapped(input, self._instance_key)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_library/custom_ops.py:863: in __call__
    return self._opoverload(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_ops.py:875: in __call__
    return self._op(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_library/autograd.py:123: in autograd_impl
    result = forward_no_grad(*args, Metadata(keyset, keyword_only_args))
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_library/autograd.py:41: in forward_no_grad
    result = op.redispatch(keyset & _C._after_autograd_keyset, *args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_ops.py:882: in redispatch
    return self._handle.redispatch_boxed(keyset, *args, **kwargs)  # type: ignore[return-value]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_library/custom_ops.py:441: in backend_impl
    result = self._backend_fns[device_type](*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_compile.py:54: in inner
    return disable_fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_dynamo/eval_frame.py:1446: in _fn
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_library/custom_ops.py:502: in wrapped_fn
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
src/tileops/ops/pool.py:1718: in _fwd
    return get_instance(instance_key)._eager_forward(input)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
src/tileops/ops/pool.py:1521: in _eager_forward
    kernel = self.get_or_build_kernel(
src/tileops/ops/op_base.py:388: in get_or_build_kernel
    entries[key] = build()
                   ^^^^^^^
src/tileops/ops/pool.py:1525: in <lambda>
    build=lambda: self.kernel_map[self._kernel_slot](
src/tileops/kernels/pool/common.py:104: in __init__
    self.init_config(config, tune)
src/tileops/kernels/kernel_base.py:179: in init_config
    self.autotune()
src/tileops/kernels/kernel_base.py:379: in autotune
    tuned_kernel = self.tune_jit_kernel(
src/tileops/kernels/kernel_base.py:367: in tune_jit_kernel
    return self._call_autotuned_kernel(autotuned_kernel_fn, jit_kernel, seed_config)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
src/tileops/kernels/kernel_base.py:279: in _call_autotuned_kernel
    return autotuned_kernel_fn(**self._autotune_initial_kwargs(kernel=kernel, config=config))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/tilelang/autotuner/tuner.py:1329: in __call__
    artifact = autotuner.run()
               ^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <tilelang.autotuner.tuner.AutoTuner object at 0xde8d81498b0>, warmup = 25
rep = 50, timeout = 100, use_pipeline = False, enable_grouped_compile = False
group_compile_size = 2, benchmark_devices = None, benchmark_multi_gpu = False

    def run(
        self,
        warmup: int = 25,
        rep: int = 100,
        timeout: int = 180,
        use_pipeline: bool = False,
        enable_grouped_compile: bool = False,
        group_compile_size: int = 2,
        benchmark_devices: list[int] | None = None,
        benchmark_multi_gpu: bool = False,
    ):
        """Run the auto-tuning process.
    
        Args:
            warmup: Number of warmup iterations.
            rep: Number of repetitions for timing.
            timeout: Maximum time per configuration.
            use_pipeline: Whether to pipeline benchmarking with compilation.
            enable_grouped_compile: Whether to enable grouped compilation.
            group_compile_size: Number of configurations in one compile unit.
            benchmark_devices: CUDA device ordinals used for benchmark workers when benchmark_multi_gpu=True.
            benchmark_multi_gpu: Whether to benchmark configurations across multiple CUDA GPUs.
    
        Returns:
            AutotuneResult: Results of the auto-tuning process.
        """
        _init_logger_handlers()
    
        sig = inspect.signature(self.fn)
        parameters = sig.parameters
    
        # NOTE(chaofan):  We need to extract some parameters from the closure.
        # Consider the case:
        #   def gemm(M, N, K):
        #       def kernel(...)
        # If we only extract source, M/N/K will be symbolic and there will be cache problem.
        extra_parameters: dict[str, Any] = {}
        cells = self.fn.__closure__
        var_names = self.fn.__code__.co_freevars
        if cells is not None:
            assert len(var_names) == len(cells), "Number of free variables does not match"
            for var_name, cell in zip(var_names, cells):
                if var_name in parameters:
                    continue
                # Cell content must be serializable
>               assert isinstance(cell.cell_contents, (int, float, str, bool, type(None))), (
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                    f"Cell contents {cell.cell_contents} is not serializable: {type(cell.cell_contents)}"
                )
E               AssertionError: Cell contents <tileops.kernels.pool.adaptive_max_pool2d._PlaneStaging object at 0xde8d8148050> is not serializable: <class 'tileops.kernels.pool.adaptive_max_pool2d._PlaneStaging'>

/usr/local/lib/python3.12/dist-packages/tilelang/autotuner/tuner.py:927: AssertionError
----------------------------- Captured stdout call -----------------------------
Start autotuning AdaptiveMaxPool2dKernel...
__________ test_adaptive_max_pool2d_indices_bench[global-1x1-float16] __________

n = 8, c_in = 2048, h_in = 7, w_in = 7, output_size = (1, 1)
dtype = torch.float16, tune = True

    @pytest.mark.parametrize(
        "n, c_in, h_in, w_in, output_size, dtype, tune",
        workload_params(load_workloads(AdaptiveMaxPool2dIndicesFwdOp), _adaptive_pool2d_args),
    )
    def test_adaptive_max_pool2d_indices_bench(
        n: int,
        c_in: int,
        h_in: int,
        w_in: int,
        output_size: tuple[int, int],
        dtype: torch.dtype,
        tune: bool,
    ) -> None:
        test = AdaptiveMaxPool2dBenchmarkWorkload(
            n, c_in, h_in, w_in, output_size, dtype, return_indices=True
        )
        inputs = test.gen_inputs()
    
        op = AdaptiveMaxPool2dIndicesFwdOp(output_size=output_size, tune=tune)
        bm = ManifestBenchmark(op, test)
    
        _tag, _baseline_fn = pool_baseline(type(op).__name__, test, *inputs)
>       bm.compare(
            {
                "tileops": op,
                _tag: _baseline_fn,
                "torch-ref": test.ref_program,
                "torch-compile": compiled_reference(test),
            },
            *inputs,
        )

benchmarks/ops/bench_pool.py:1451: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
benchmarks/benchmark_base.py:370: in compare
    bench_kernel(
benchmarks/timing.py:629: in bench_kernel
    _call_raw()
benchmarks/timing.py:626: in _call_raw
    return fn(*args) if args else fn()
           ^^^^^^^^^
src/tileops/ops/op_base.py:607: in __call__
    return self.forward(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
src/tileops/ops/pool.py:1681: in forward
    return type(self)._wrapped(input, self._instance_key)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_library/custom_ops.py:863: in __call__
    return self._opoverload(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_ops.py:875: in __call__
    return self._op(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_library/autograd.py:123: in autograd_impl
    result = forward_no_grad(*args, Metadata(keyset, keyword_only_args))
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_library/autograd.py:41: in forward_no_grad
    result = op.redispatch(keyset & _C._after_autograd_keyset, *args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_ops.py:882: in redispatch
    return self._handle.redispatch_boxed(keyset, *args, **kwargs)  # type: ignore[return-value]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_library/custom_ops.py:441: in backend_impl
    result = self._backend_fns[device_type](*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_compile.py:54: in inner
    return disable_fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_dynamo/eval_frame.py:1446: in _fn
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_library/custom_ops.py:502: in wrapped_fn
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
src/tileops/ops/pool.py:1700: in _fwd
    return get_instance(instance_key)._eager_forward(input)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
src/tileops/ops/pool.py:1521: in _eager_forward
    kernel = self.get_or_build_kernel(
src/tileops/ops/op_base.py:388: in get_or_build_kernel
    entries[key] = build()
                   ^^^^^^^
src/tileops/ops/pool.py:1525: in <lambda>
    build=lambda: self.kernel_map[self._kernel_slot](
src/tileops/kernels/pool/common.py:104: in __init__
    self.init_config(config, tune)
src/tileops/kernels/kernel_base.py:179: in init_config
    self.autotune()
src/tileops/kernels/kernel_base.py:379: in autotune
    tuned_kernel = self.tune_jit_kernel(
src/tileops/kernels/kernel_base.py:367: in tune_jit_kernel
    return self._call_autotuned_kernel(autotuned_kernel_fn, jit_kernel, seed_config)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
src/tileops/kernels/kernel_base.py:279: in _call_autotuned_kernel
    return autotuned_kernel_fn(**self._autotune_initial_kwargs(kernel=kernel, config=config))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/tilelang/autotuner/tuner.py:1329: in __call__
    artifact = autotuner.run()
               ^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <tilelang.autotuner.tuner.AutoTuner object at 0xde8d82e3020>, warmup = 25
rep = 50, timeout = 100, use_pipeline = False, enable_grouped_compile = False
group_compile_size = 2, benchmark_devices = None, benchmark_multi_gpu = False

    def run(
        self,
        warmup: int = 25,
        rep: int = 100,
        timeout: int = 180,
        use_pipeline: bool = False,
        enable_grouped_compile: bool = False,
        group_compile_size: int = 2,
        benchmark_devices: list[int] | None = None,
        benchmark_multi_gpu: bool = False,
    ):
        """Run the auto-tuning process.
    
        Args:
            warmup: Number of warmup iterations.
            rep: Number of repetitions for timing.
            timeout: Maximum time per configuration.
            use_pipeline: Whether to pipeline benchmarking with compilation.
            enable_grouped_compile: Whether to enable grouped compilation.
            group_compile_size: Number of configurations in one compile unit.
            benchmark_devices: CUDA device ordinals used for benchmark workers when benchmark_multi_gpu=True.
            benchmark_multi_gpu: Whether to benchmark configurations across multiple CUDA GPUs.
    
        Returns:
            AutotuneResult: Results of the auto-tuning process.
        """
        _init_logger_handlers()
    
        sig = inspect.signature(self.fn)
        parameters = sig.parameters
    
        # NOTE(chaofan):  We need to extract some parameters from the closure.
        # Consider the case:
        #   def gemm(M, N, K):
        #       def kernel(...)
        # If we only extract source, M/N/K will be symbolic and there will be cache problem.
        extra_parameters: dict[str, Any] = {}
        cells = self.fn.__closure__
        var_names = self.fn.__code__.co_freevars
        if cells is not None:
            assert len(var_names) == len(cells), "Number of free variables does not match"
            for var_name, cell in zip(var_names, cells):
                if var_name in parameters:
                    continue
                # Cell content must be serializable
>               assert isinstance(cell.cell_contents, (int, float, str, bool, type(None))), (
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                    f"Cell contents {cell.cell_contents} is not serializable: {type(cell.cell_contents)}"
                )
E               AssertionError: Cell contents <tileops.kernels.pool.adaptive_max_pool2d._PlaneStaging object at 0xde8d825ad50> is not serializable: <class 'tileops.kernels.pool.adaptive_max_pool2d._PlaneStaging'>

/usr/local/lib/python3.12/dist-packages/tilelang/autotuner/tuner.py:927: AssertionError
----------------------------- Captured stdout call -----------------------------
Start autotuning AdaptiveMaxPool2dWithIndicesKernel...
___________ test_adaptive_max_pool2d_indices_bench[spp-6x6-float16] ____________

n = 2, c_in = 128, h_in = 56, w_in = 56, output_size = (6, 6)
dtype = torch.float16, tune = True

    @pytest.mark.parametrize(
        "n, c_in, h_in, w_in, output_size, dtype, tune",
        workload_params(load_workloads(AdaptiveMaxPool2dIndicesFwdOp), _adaptive_pool2d_args),
    )
    def test_adaptive_max_pool2d_indices_bench(
        n: int,
        c_in: int,
        h_in: int,
        w_in: int,
        output_size: tuple[int, int],
        dtype: torch.dtype,
        tune: bool,
    ) -> None:
        test = AdaptiveMaxPool2dBenchmarkWorkload(
            n, c_in, h_in, w_in, output_size, dtype, return_indices=True
        )
        inputs = test.gen_inputs()
    
        op = AdaptiveMaxPool2dIndicesFwdOp(output_size=output_size, tune=tune)
        bm = ManifestBenchmark(op, test)
    
        _tag, _baseline_fn = pool_baseline(type(op).__name__, test, *inputs)
>       bm.compare(
            {
                "tileops": op,
                _tag: _baseline_fn,
                "torch-ref": test.ref_program,
                "torch-compile": compiled_reference(test),
            },
            *inputs,
        )

benchmarks/ops/bench_pool.py:1451: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
benchmarks/benchmark_base.py:370: in compare
    bench_kernel(
benchmarks/timing.py:629: in bench_kernel
    _call_raw()
benchmarks/timing.py:626: in _call_raw
    return fn(*args) if args else fn()
           ^^^^^^^^^
src/tileops/ops/op_base.py:607: in __call__
    return self.forward(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
src/tileops/ops/pool.py:1681: in forward
    return type(self)._wrapped(input, self._instance_key)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_library/custom_ops.py:863: in __call__
    return self._opoverload(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_ops.py:875: in __call__
    return self._op(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_library/autograd.py:123: in autograd_impl
    result = forward_no_grad(*args, Metadata(keyset, keyword_only_args))
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_library/autograd.py:41: in forward_no_grad
    result = op.redispatch(keyset & _C._after_autograd_keyset, *args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_ops.py:882: in redispatch
    return self._handle.redispatch_boxed(keyset, *args, **kwargs)  # type: ignore[return-value]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_library/custom_ops.py:441: in backend_impl
    result = self._backend_fns[device_type](*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_compile.py:54: in inner
    return disable_fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_dynamo/eval_frame.py:1446: in _fn
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_library/custom_ops.py:502: in wrapped_fn
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
src/tileops/ops/pool.py:1700: in _fwd
    return get_instance(instance_key)._eager_forward(input)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
src/tileops/ops/pool.py:1521: in _eager_forward
    kernel = self.get_or_build_kernel(
src/tileops/ops/op_base.py:388: in get_or_build_kernel
    entries[key] = build()
                   ^^^^^^^
src/tileops/ops/pool.py:1525: in <lambda>
    build=lambda: self.kernel_map[self._kernel_slot](
src/tileops/kernels/pool/common.py:104: in __init__
    self.init_config(config, tune)
src/tileops/kernels/kernel_base.py:179: in init_config
    self.autotune()
src/tileops/kernels/kernel_base.py:379: in autotune
    tuned_kernel = self.tune_jit_kernel(
src/tileops/kernels/kernel_base.py:367: in tune_jit_kernel
    return self._call_autotuned_kernel(autotuned_kernel_fn, jit_kernel, seed_config)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
src/tileops/kernels/kernel_base.py:279: in _call_autotuned_kernel
    return autotuned_kernel_fn(**self._autotune_initial_kwargs(kernel=kernel, config=config))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/tilelang/autotuner/tuner.py:1329: in __call__
    artifact = autotuner.run()
               ^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <tilelang.autotuner.tuner.AutoTuner object at 0xde8d82afcb0>, warmup = 25
rep = 50, timeout = 100, use_pipeline = False, enable_grouped_compile = False
group_compile_size = 2, benchmark_devices = None, benchmark_multi_gpu = False

    def run(
        self,
        warmup: int = 25,
        rep: int = 100,
        timeout: int = 180,
        use_pipeline: bool = False,
        enable_grouped_compile: bool = False,
        group_compile_size: int = 2,
        benchmark_devices: list[int] | None = None,
        benchmark_multi_gpu: bool = False,
    ):
        """Run the auto-tuning process.
    
        Args:
            warmup: Number of warmup iterations.
            rep: Number of repetitions for timing.
            timeout: Maximum time per configuration.
            use_pipeline: Whether to pipeline benchmarking with compilation.
            enable_grouped_compile: Whether to enable grouped compilation.
            group_compile_size: Number of configurations in one compile unit.
            benchmark_devices: CUDA device ordinals used for benchmark workers when benchmark_multi_gpu=True.
            benchmark_multi_gpu: Whether to benchmark configurations across multiple CUDA GPUs.
    
        Returns:
            AutotuneResult: Results of the auto-tuning process.
        """
        _init_logger_handlers()
    
        sig = inspect.signature(self.fn)
        parameters = sig.parameters
    
        # NOTE(chaofan):  We need to extract some parameters from the closure.
        # Consider the case:
        #   def gemm(M, N, K):
        #       def kernel(...)
        # If we only extract source, M/N/K will be symbolic and there will be cache problem.
        extra_parameters: dict[str, Any] = {}
        cells = self.fn.__closure__
        var_names = self.fn.__code__.co_freevars
        if cells is not None:
            assert len(var_names) == len(cells), "Number of free variables does not match"
            for var_name, cell in zip(var_names, cells):
                if var_name in parameters:
                    continue
                # Cell content must be serializable
>               assert isinstance(cell.cell_contents, (int, float, str, bool, type(None))), (
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                    f"Cell contents {cell.cell_contents} is not serializable: {type(cell.cell_contents)}"
                )
E               AssertionError: Cell contents <tileops.kernels.pool.adaptive_max_pool2d._PlaneStaging object at 0xde8d83b0d40> is not serializable: <class 'tileops.kernels.pool.adaptive_max_pool2d._PlaneStaging'>

/usr/local/lib/python3.12/dist-packages/tilelang/autotuner/tuner.py:927: AssertionError
----------------------------- Captured stdout call -----------------------------
Start autotuning AdaptiveMaxPool2dWithIndicesKernel...
_________ test_adaptive_max_pool2d_indices_bench[nondiv-7x7-bfloat16] __________

n = 2, c_in = 64, h_in = 55, w_in = 57, output_size = (7, 7)
dtype = torch.bfloat16, tune = True

    @pytest.mark.parametrize(
        "n, c_in, h_in, w_in, output_size, dtype, tune",
        workload_params(load_workloads(AdaptiveMaxPool2dIndicesFwdOp), _adaptive_pool2d_args),
    )
    def test_adaptive_max_pool2d_indices_bench(
        n: int,
        c_in: int,
        h_in: int,
        w_in: int,
        output_size: tuple[int, int],
        dtype: torch.dtype,
        tune: bool,
    ) -> None:
        test = AdaptiveMaxPool2dBenchmarkWorkload(
            n, c_in, h_in, w_in, output_size, dtype, return_indices=True
        )
        inputs = test.gen_inputs()
    
        op = AdaptiveMaxPool2dIndicesFwdOp(output_size=output_size, tune=tune)
        bm = ManifestBenchmark(op, test)
    
        _tag, _baseline_fn = pool_baseline(type(op).__name__, test, *inputs)
>       bm.compare(
            {
                "tileops": op,
                _tag: _baseline_fn,
                "torch-ref": test.ref_program,
                "torch-compile": compiled_reference(test),
            },
            *inputs,
        )

benchmarks/ops/bench_pool.py:1451: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
benchmarks/benchmark_base.py:370: in compare
    bench_kernel(
benchmarks/timing.py:629: in bench_kernel
    _call_raw()
benchmarks/timing.py:626: in _call_raw
    return fn(*args) if args else fn()
           ^^^^^^^^^
src/tileops/ops/op_base.py:607: in __call__
    return self.forward(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
src/tileops/ops/pool.py:1681: in forward
    return type(self)._wrapped(input, self._instance_key)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_library/custom_ops.py:863: in __call__
    return self._opoverload(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_ops.py:875: in __call__
    return self._op(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_library/autograd.py:123: in autograd_impl
    result = forward_no_grad(*args, Metadata(keyset, keyword_only_args))
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_library/autograd.py:41: in forward_no_grad
    result = op.redispatch(keyset & _C._after_autograd_keyset, *args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_ops.py:882: in redispatch
    return self._handle.redispatch_boxed(keyset, *args, **kwargs)  # type: ignore[return-value]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_library/custom_ops.py:441: in backend_impl
    result = self._backend_fns[device_type](*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_compile.py:54: in inner
    return disable_fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_dynamo/eval_frame.py:1446: in _fn
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/torch/_library/custom_ops.py:502: in wrapped_fn
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
src/tileops/ops/pool.py:1700: in _fwd
    return get_instance(instance_key)._eager_forward(input)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
src/tileops/ops/pool.py:1521: in _eager_forward
    kernel = self.get_or_build_kernel(
src/tileops/ops/op_base.py:388: in get_or_build_kernel
    entries[key] = build()
                   ^^^^^^^
src/tileops/ops/pool.py:1525: in <lambda>
    build=lambda: self.kernel_map[self._kernel_slot](
src/tileops/kernels/pool/common.py:104: in __init__
    self.init_config(config, tune)
src/tileops/kernels/kernel_base.py:179: in init_config
    self.autotune()
src/tileops/kernels/kernel_base.py:379: in autotune
    tuned_kernel = self.tune_jit_kernel(
src/tileops/kernels/kernel_base.py:367: in tune_jit_kernel
    return self._call_autotuned_kernel(autotuned_kernel_fn, jit_kernel, seed_config)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
src/tileops/kernels/kernel_base.py:279: in _call_autotuned_kernel
    return autotuned_kernel_fn(**self._autotune_initial_kwargs(kernel=kernel, config=config))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
/usr/local/lib/python3.12/dist-packages/tilelang/autotuner/tuner.py:1329: in __call__
    artifact = autotuner.run()
               ^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <tilelang.autotuner.tuner.AutoTuner object at 0xde8d83bef60>, warmup = 25
rep = 50, timeout = 100, use_pipeline = False, enable_grouped_compile = False
group_compile_size = 2, benchmark_devices = None, benchmark_multi_gpu = False

    def run(
        self,
        warmup: int = 25,
        rep: int = 100,
        timeout: int = 180,
        use_pipeline: bool = False,
        enable_grouped_compile: bool = False,
        group_compile_size: int = 2,
        benchmark_devices: list[int] | None = None,
        benchmark_multi_gpu: bool = False,
    ):
        """Run the auto-tuning process.
    
        Args:
            warmup: Number of warmup iterations.
            rep: Number of repetitions for timing.
            timeout: Maximum time per configuration.
            use_pipeline: Whether to pipeline benchmarking with compilation.
            enable_grouped_compile: Whether to enable grouped compilation.
            group_compile_size: Number of configurations in one compile unit.
            benchmark_devices: CUDA device ordinals used for benchmark workers when benchmark_multi_gpu=True.
            benchmark_multi_gpu: Whether to benchmark configurations across multiple CUDA GPUs.
    
        Returns:
            AutotuneResult: Results of the auto-tuning process.
        """
        _init_logger_handlers()
    
        sig = inspect.signature(self.fn)
        parameters = sig.parameters
    
        # NOTE(chaofan):  We need to extract some parameters from the closure.
        # Consider the case:
        #   def gemm(M, N, K):
        #       def kernel(...)
        # If we only extract source, M/N/K will be symbolic and there will be cache problem.
        extra_parameters: dict[str, Any] = {}
        cells = self.fn.__closure__
        var_names = self.fn.__code__.co_freevars
        if cells is not None:
            assert len(var_names) == len(cells), "Number of free variables does not match"
            for var_name, cell in zip(var_names, cells):
                if var_name in parameters:
                    continue
                # Cell content must be serializable
>               assert isinstance(cell.cell_contents, (int, float, str, bool, type(None))), (
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                    f"Cell contents {cell.cell_contents} is not serializable: {type(cell.cell_contents)}"
                )
E               AssertionError: Cell contents <tileops.kernels.pool.adaptive_max_pool2d._PlaneStaging object at 0xde8d83beb70> is not serializable: <class 'tileops.kernels.pool.adaptive_max_pool2d._PlaneStaging'>

/usr/local/lib/python3.12/dist-packages/tilelang/autotuner/tuner.py:927: AssertionError
----------------------------- Captured stdout call -----------------------------
Start autotuning AdaptiveMaxPool2dWithIndicesKernel...
=============================== warnings summary ===============================
benchmarks/ops/bench_pool.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

benchmarks/ops/bench_pool.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ============================
FAILED benchmarks/ops/bench_pool.py::test_adaptive_max_pool2d_bench[global-1x1-float16] - AssertionError: Cell contents <tileops.kernels.pool.adaptive_max_pool2d._PlaneStaging object at 0xde8d823a660> is not serializable: <class 'tileops.kernels.pool.adaptive_max_pool2d._PlaneStaging'>
FAILED benchmarks/ops/bench_pool.py::test_adaptive_max_pool2d_bench[spp-6x6-float16] - AssertionError: Cell contents <tileops.kernels.pool.adaptive_max_pool2d._PlaneStaging object at 0xde88d543fb0> is not serializable: <class 'tileops.kernels.pool.adaptive_max_pool2d._PlaneStaging'>
FAILED benchmarks/ops/bench_pool.py::test_adaptive_max_pool2d_bench[nondiv-7x7-bfloat16] - AssertionError: Cell contents <tileops.kernels.pool.adaptive_max_pool2d._PlaneStaging object at 0xde8d8148050> is not serializable: <class 'tileops.kernels.pool.adaptive_max_pool2d._PlaneStaging'>
FAILED benchmarks/ops/bench_pool.py::test_adaptive_max_pool2d_indices_bench[global-1x1-float16] - AssertionError: Cell contents <tileops.kernels.pool.adaptive_max_pool2d._PlaneStaging object at 0xde8d825ad50> is not serializable: <class 'tileops.kernels.pool.adaptive_max_pool2d._PlaneStaging'>
FAILED benchmarks/ops/bench_pool.py::test_adaptive_max_pool2d_indices_bench[spp-6x6-float16] - AssertionError: Cell contents <tileops.kernels.pool.adaptive_max_pool2d._PlaneStaging object at 0xde8d83b0d40> is not serializable: <class 'tileops.kernels.pool.adaptive_max_pool2d._PlaneStaging'>
FAILED benchmarks/ops/bench_pool.py::test_adaptive_max_pool2d_indices_bench[nondiv-7x7-bfloat16] - AssertionError: Cell contents <tileops.kernels.pool.adaptive_max_pool2d._PlaneStaging object at 0xde8d83beb70> is not serializable: <class 'tileops.kernels.pool.adaptive_max_pool2d._PlaneStaging'>
6 failed, 42 passed, 58 warnings in 67.03s (0:01:07)
--- benchmarks/ops/bench_pool.py finished in 68s ---

=== [49/54] benchmarks/ops/bench_reduce.py ===
benchmarks/ops/bench_reduce.py::test_sum_bench[hidden-state-reduce-float16]
benchmarks/ops/bench_reduce.py::test_sum_bench[hidden-state-reduce-bfloat16]
benchmarks/ops/bench_reduce.py::test_sum_bench[long-seq-reduce-bfloat16]
benchmarks/ops/bench_reduce.py::test_sum_bench[hidden-state-reduce-dim0-bfloat16]
benchmarks/ops/bench_reduce.py::test_sum_bench[hidden-state-reduce-keepdim-bfloat16]
benchmarks/ops/bench_reduce.py::test_sum_bench[3d-multidim-reduce-float16]
benchmarks/ops/bench_reduce.py::test_mean_bench[hidden-state-reduce-float16]
benchmarks/ops/bench_reduce.py::test_mean_bench[hidden-state-reduce-bfloat16]
benchmarks/ops/bench_reduce.py::test_mean_bench[long-seq-reduce-bfloat16]
benchmarks/ops/bench_reduce.py::test_mean_bench[3d-multidim-reduce-float16]
benchmarks/ops/bench_reduce.py::test_amax_bench[hidden-state-reduce-float16]
benchmarks/ops/bench_reduce.py::test_amax_bench[hidden-state-reduce-bfloat16]
benchmarks/ops/bench_reduce.py::test_amax_bench[long-seq-reduce-bfloat16]
benchmarks/ops/bench_reduce.py::test_amax_bench[3d-multidim-reduce-float16]
benchmarks/ops/bench_reduce.py::test_amin_bench[hidden-state-reduce-float16]
benchmarks/ops/bench_reduce.py::test_amin_bench[hidden-state-reduce-bfloat16]
benchmarks/ops/bench_reduce.py::test_amin_bench[long-seq-reduce-bfloat16]
benchmarks/ops/bench_reduce.py::test_amin_bench[3d-multidim-reduce-float16]
benchmarks/ops/bench_reduce.py::test_prod_bench[hidden-state-reduce-float16]
benchmarks/ops/bench_reduce.py::test_prod_bench[hidden-state-reduce-bfloat16]
benchmarks/ops/bench_reduce.py::test_prod_bench[long-seq-reduce-bfloat16]
benchmarks/ops/bench_reduce.py::test_std_bench[hidden-state-std-float16]
benchmarks/ops/bench_reduce.py::test_std_bench[hidden-state-std-bfloat16]
benchmarks/ops/bench_reduce.py::test_std_bench[long-seq-std-bfloat16]
benchmarks/ops/bench_reduce.py::test_std_bench[3d-multidim-reduce-float16]
benchmarks/ops/bench_reduce.py::test_var_bench[hidden-state-var-float16]
benchmarks/ops/bench_reduce.py::test_var_bench[hidden-state-var-bfloat16]
benchmarks/ops/bench_reduce.py::test_var_bench[long-seq-var-bfloat16]
benchmarks/ops/bench_reduce.py::test_var_bench[3d-multidim-reduce-float16]
benchmarks/ops/bench_reduce.py::test_var_mean_bench[hidden-state-var-mean-float16]
benchmarks/ops/bench_reduce.py::test_var_mean_bench[hidden-state-var-mean-bfloat16]
benchmarks/ops/bench_reduce.py::test_var_mean_bench[long-seq-var-mean-bfloat16]
benchmarks/ops/bench_reduce.py::test_var_mean_bench[3d-multidim-reduce-float16]

33 tests collected in 2.01s
.................................                                        [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_reduce.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_reduce.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
33 passed, 58 warnings in 34.21s
--- benchmarks/ops/bench_reduce.py finished in 35s ---

=== [50/54] benchmarks/ops/bench_rope.py ===
benchmarks/ops/bench_rope.py::test_rope_neox_bench[neox-1d-2k-d64-float16]
benchmarks/ops/bench_rope.py::test_rope_neox_bench[neox-1d-4k-d128-bfloat16]
benchmarks/ops/bench_rope.py::test_rope_neox_bench[neox-2d-b2-s2k-h32-d128-float16]
benchmarks/ops/bench_rope.py::test_rope_non_neox_bench[non-neox-1d-2k-d64-float16]
benchmarks/ops/bench_rope.py::test_rope_non_neox_bench[non-neox-2d-b2-s2k-h32-d128-bfloat16]
benchmarks/ops/bench_rope.py::test_rope_llama31_bench[llama31-1d-8k-d128-bfloat16]
benchmarks/ops/bench_rope.py::test_rope_llama31_bench[llama31-2d-b1-s8k-h32-d128-float16]
benchmarks/ops/bench_rope.py::test_rope_yarn_bench[yarn-1d-8k-d128-bfloat16]
benchmarks/ops/bench_rope.py::test_rope_yarn_bench[yarn-2d-b1-s8k-h32-d128-float16]
benchmarks/ops/bench_rope.py::test_rope_longrope_bench[longrope-1d-8k-d128-bfloat16]
benchmarks/ops/bench_rope.py::test_rope_longrope_bench[longrope-2d-b1-s8k-h32-d128-float16]
benchmarks/ops/bench_rope.py::test_rope_neox_position_ids_bench[position-ids-s2k-h32-d128-float16]
benchmarks/ops/bench_rope.py::test_rope_neox_position_ids_bench[position-ids-s4k-h32-d128-bfloat16]

13 tests collected in 2.08s
.............                                                            [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_rope.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
13 passed, 14 warnings in 14.34s
--- benchmarks/ops/bench_rope.py finished in 15s ---

=== [51/54] benchmarks/ops/bench_softmax.py ===
benchmarks/ops/bench_softmax.py::test_softmax_bench[attn-weights-4k-float16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[attn-weights-4k-bfloat16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[attn-weights-4k-float32]
benchmarks/ops/bench_softmax.py::test_softmax_bench[attn-weights-32k-bfloat16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[lm-head-logits-float16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[lm-head-logits-bfloat16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[lm-head-logits-float32]
benchmarks/ops/bench_softmax.py::test_log_softmax_bench[attn-weights-4k-float16]
benchmarks/ops/bench_softmax.py::test_log_softmax_bench[attn-weights-4k-bfloat16]
benchmarks/ops/bench_softmax.py::test_log_softmax_bench[attn-weights-4k-float32]
benchmarks/ops/bench_softmax.py::test_log_softmax_bench[attn-weights-32k-bfloat16]
benchmarks/ops/bench_softmax.py::test_log_softmax_bench[lm-head-logits-float16]
benchmarks/ops/bench_softmax.py::test_log_softmax_bench[lm-head-logits-bfloat16]
benchmarks/ops/bench_softmax.py::test_log_softmax_bench[lm-head-logits-float32]
benchmarks/ops/bench_softmax.py::test_logsumexp_bench[attn-weights-4k-float16]
benchmarks/ops/bench_softmax.py::test_logsumexp_bench[attn-weights-4k-bfloat16]
benchmarks/ops/bench_softmax.py::test_logsumexp_bench[attn-weights-32k-bfloat16]
benchmarks/ops/bench_softmax.py::test_logsumexp_bench[lm-head-logits-float16]
benchmarks/ops/bench_softmax.py::test_logsumexp_bench[lm-head-logits-bfloat16]
benchmarks/ops/bench_softmax.py::test_logsumexp_bench[3d-multidim-reduce-float16]

20 tests collected in 2.04s
....................                                                     [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_softmax.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_softmax.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
20 passed, 58 warnings in 27.04s
--- benchmarks/ops/bench_softmax.py finished in 28s ---

=== [52/54] benchmarks/ops/bench_topk_selector.py ===
benchmarks/ops/bench_topk_selector.py::test_topk_selector_bench[topk1024-s32k-kv64k-float32]
benchmarks/ops/bench_topk_selector.py::test_topk_selector_bench[topk2048-s32k-kv64k-float32]

2 tests collected in 1.95s
..                                                                       [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_topk_selector.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
2 passed, 14 warnings in 125.94s (0:02:05)
--- benchmarks/ops/bench_topk_selector.py finished in 127s ---

=== [53/54] benchmarks/ops/bench_unary_elementwise.py ===
benchmarks/ops/bench_unary_elementwise.py::test_exp_bench[elementwise-16M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_exp_bench[elementwise-16M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_exp_bench[elementwise-16M-float32]
benchmarks/ops/bench_unary_elementwise.py::test_exp_bench[elementwise-256M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_exp_bench[elementwise-256M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_log_bench[elementwise-16M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_log_bench[elementwise-16M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_log_bench[elementwise-16M-float32]
benchmarks/ops/bench_unary_elementwise.py::test_log_bench[elementwise-256M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_log_bench[elementwise-256M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_sqrt_bench[elementwise-16M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_sqrt_bench[elementwise-16M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_sqrt_bench[elementwise-16M-float32]
benchmarks/ops/bench_unary_elementwise.py::test_sqrt_bench[elementwise-256M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_sqrt_bench[elementwise-256M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_rsqrt_bench[elementwise-16M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_rsqrt_bench[elementwise-16M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_rsqrt_bench[elementwise-16M-float32]
benchmarks/ops/bench_unary_elementwise.py::test_rsqrt_bench[elementwise-256M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_rsqrt_bench[elementwise-256M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_abs_bench[elementwise-16M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_abs_bench[elementwise-16M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_abs_bench[elementwise-16M-float32]
benchmarks/ops/bench_unary_elementwise.py::test_abs_bench[elementwise-256M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_abs_bench[elementwise-256M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_neg_bench[elementwise-16M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_neg_bench[elementwise-16M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_neg_bench[elementwise-16M-float32]
benchmarks/ops/bench_unary_elementwise.py::test_neg_bench[elementwise-256M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_neg_bench[elementwise-256M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_reciprocal_bench[elementwise-16M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_reciprocal_bench[elementwise-16M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_reciprocal_bench[elementwise-16M-float32]
benchmarks/ops/bench_unary_elementwise.py::test_reciprocal_bench[elementwise-256M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_reciprocal_bench[elementwise-256M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_sign_bench[elementwise-16M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_sign_bench[elementwise-16M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_sign_bench[elementwise-16M-float32]
benchmarks/ops/bench_unary_elementwise.py::test_sign_bench[elementwise-256M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_sign_bench[elementwise-256M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_sin_bench[elementwise-16M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_sin_bench[elementwise-16M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_sin_bench[elementwise-16M-float32]
benchmarks/ops/bench_unary_elementwise.py::test_sin_bench[elementwise-256M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_sin_bench[elementwise-256M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_cos_bench[elementwise-16M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_cos_bench[elementwise-16M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_cos_bench[elementwise-16M-float32]
benchmarks/ops/bench_unary_elementwise.py::test_cos_bench[elementwise-256M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_cos_bench[elementwise-256M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_floor_bench[elementwise-16M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_floor_bench[elementwise-16M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_floor_bench[elementwise-16M-float32]
benchmarks/ops/bench_unary_elementwise.py::test_floor_bench[elementwise-256M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_floor_bench[elementwise-256M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_ceil_bench[elementwise-16M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_ceil_bench[elementwise-16M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_ceil_bench[elementwise-16M-float32]
benchmarks/ops/bench_unary_elementwise.py::test_ceil_bench[elementwise-256M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_ceil_bench[elementwise-256M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_round_bench[elementwise-16M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_round_bench[elementwise-16M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_round_bench[elementwise-16M-float32]
benchmarks/ops/bench_unary_elementwise.py::test_round_bench[elementwise-256M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_round_bench[elementwise-256M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_trunc_bench[elementwise-16M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_trunc_bench[elementwise-16M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_trunc_bench[elementwise-16M-float32]
benchmarks/ops/bench_unary_elementwise.py::test_trunc_bench[elementwise-256M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_trunc_bench[elementwise-256M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_erf_bench[elementwise-16M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_erf_bench[elementwise-16M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_erf_bench[elementwise-16M-float32]
benchmarks/ops/bench_unary_elementwise.py::test_erf_bench[elementwise-256M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_erf_bench[elementwise-256M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_log1p_bench[elementwise-16M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_log1p_bench[elementwise-16M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_log1p_bench[elementwise-16M-float32]
benchmarks/ops/bench_unary_elementwise.py::test_log1p_bench[elementwise-256M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_log1p_bench[elementwise-256M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_expm1_bench[elementwise-16M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_expm1_bench[elementwise-16M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_expm1_bench[elementwise-16M-float32]
benchmarks/ops/bench_unary_elementwise.py::test_expm1_bench[elementwise-256M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_expm1_bench[elementwise-256M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_logical_not_bench[elementwise-16M-bool]
benchmarks/ops/bench_unary_elementwise.py::test_logical_not_bench[elementwise-16M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_logical_not_bench[elementwise-16M-float32]
benchmarks/ops/bench_unary_elementwise.py::test_logical_not_bench[elementwise-256M-bool]
benchmarks/ops/bench_unary_elementwise.py::test_bitwise_not_bench[elementwise-16M-int32]
benchmarks/ops/bench_unary_elementwise.py::test_bitwise_not_bench[elementwise-16M-int64]
benchmarks/ops/bench_unary_elementwise.py::test_bitwise_not_bench[elementwise-256M-int32]
benchmarks/ops/bench_unary_elementwise.py::test_isnan_bench[elementwise-16M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_isnan_bench[elementwise-16M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_isnan_bench[elementwise-16M-float32]
benchmarks/ops/bench_unary_elementwise.py::test_isnan_bench[elementwise-256M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_isnan_bench[elementwise-256M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_isinf_bench[elementwise-16M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_isinf_bench[elementwise-16M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_isinf_bench[elementwise-16M-float32]
benchmarks/ops/bench_unary_elementwise.py::test_isinf_bench[elementwise-256M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_isinf_bench[elementwise-256M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_isfinite_bench[elementwise-16M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_isfinite_bench[elementwise-16M-bfloat16]
benchmarks/ops/bench_unary_elementwise.py::test_isfinite_bench[elementwise-16M-float32]
benchmarks/ops/bench_unary_elementwise.py::test_isfinite_bench[elementwise-256M-float16]
benchmarks/ops/bench_unary_elementwise.py::test_isfinite_bench[elementwise-256M-bfloat16]

107 tests collected in 2.00s
........................................................................ [ 67%]
...................................                                      [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_unary_elementwise.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
107 passed, 14 warnings in 63.69s (0:01:03)
--- benchmarks/ops/bench_unary_elementwise.py finished in 64s ---

=== [54/54] benchmarks/ops/bench_vector_norm.py ===
benchmarks/ops/bench_vector_norm.py::test_l1_norm_bench[hidden-state-l1-float16]
benchmarks/ops/bench_vector_norm.py::test_l1_norm_bench[hidden-state-l1-bfloat16]
benchmarks/ops/bench_vector_norm.py::test_l1_norm_bench[long-seq-l1-bfloat16]
benchmarks/ops/bench_vector_norm.py::test_l1_norm_bench[3d-multidim-reduce-float16]
benchmarks/ops/bench_vector_norm.py::test_l2_norm_bench[hidden-state-l2-float16]
benchmarks/ops/bench_vector_norm.py::test_l2_norm_bench[hidden-state-l2-bfloat16]
benchmarks/ops/bench_vector_norm.py::test_l2_norm_bench[long-seq-l2-bfloat16]
benchmarks/ops/bench_vector_norm.py::test_l2_norm_bench[3d-multidim-reduce-float16]
benchmarks/ops/bench_vector_norm.py::test_inf_norm_bench[hidden-state-inf-float16]
benchmarks/ops/bench_vector_norm.py::test_inf_norm_bench[hidden-state-inf-bfloat16]
benchmarks/ops/bench_vector_norm.py::test_inf_norm_bench[long-seq-inf-bfloat16]
benchmarks/ops/bench_vector_norm.py::test_inf_norm_bench[3d-multidim-reduce-float16]

12 tests collected in 2.04s
............                                                             [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_vector_norm.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_vector_norm.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
12 passed, 58 warnings in 16.41s
--- benchmarks/ops/bench_vector_norm.py finished in 17s ---

1 benchmark file(s) failed:
  benchmarks/ops/bench_pool.py
