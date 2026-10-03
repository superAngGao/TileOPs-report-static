discovered 49 benchmark files

=== [1/49] benchmarks/ops/attention/bench_deepseek_dsa_decode.py ===
benchmarks/ops/attention/bench_deepseek_dsa_decode.py::test_dsa_decode_bench[single-batch-mainstream-float16]
benchmarks/ops/attention/bench_deepseek_dsa_decode.py::test_dsa_decode_bench[longer-kv-lower-topk-float16]

2 tests collected in 1.98s
..                                                                       [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/attention/bench_deepseek_dsa_decode.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

benchmarks/ops/attention/bench_deepseek_dsa_decode.py::test_dsa_decode_bench[single-batch-mainstream-float16]
  /usr/local/lib/python3.12/dist-packages/torch/_inductor/compile_fx.py:321: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
2 passed, 15 warnings in 13.76s
--- benchmarks/ops/attention/bench_deepseek_dsa_decode.py finished in 18s ---

=== [2/49] benchmarks/ops/attention/bench_deepseek_mla_decode.py ===
benchmarks/ops/attention/bench_deepseek_mla_decode.py::test_mla_decode_bench[deepseek-v2-4k-float16]
benchmarks/ops/attention/bench_deepseek_mla_decode.py::test_mla_decode_bench[deepseek-v2-4k-bfloat16]
benchmarks/ops/attention/bench_deepseek_mla_decode.py::test_mla_decode_bench[deepseek-v2-32k-float16]
benchmarks/ops/attention/bench_deepseek_mla_decode.py::test_mla_decode_bench[deepseek-v2-32k-bfloat16]
benchmarks/ops/attention/bench_deepseek_mla_decode.py::test_mla_decode_bench[deepseek-v3-4k-bfloat16]
benchmarks/ops/attention/bench_deepseek_mla_decode.py::test_mla_decode_bench[deepseek-v3-32k-bfloat16]

6 tests collected in 2.02s
......                                                                   [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/attention/bench_deepseek_mla_decode.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
6 passed, 14 warnings in 20.90s
--- benchmarks/ops/attention/bench_deepseek_mla_decode.py finished in 21s ---

=== [3/49] benchmarks/ops/attention/bench_deepseek_nsa.py ===
benchmarks/ops/attention/bench_deepseek_nsa.py::test_nsa_cmp_fwd_varlen_bench[nsa-cmp-s8k-r8-h32-d128-float16]
benchmarks/ops/attention/bench_deepseek_nsa.py::test_nsa_cmp_fwd_varlen_bench[nsa-cmp-s4k-r4-h32-d128-float16]
benchmarks/ops/attention/bench_deepseek_nsa.py::test_nsa_topk_varlen_bench[nsa-topk-s8k-r8-h32-d128-float16]
benchmarks/ops/attention/bench_deepseek_nsa.py::test_nsa_topk_varlen_bench[nsa-topk-s4k-r4-h32-d128-float16]
benchmarks/ops/attention/bench_deepseek_nsa.py::test_nsa_fwd_varlen_bench[nsa-slc-s8k-r4-h16-d64-b1-float16]
benchmarks/ops/attention/bench_deepseek_nsa.py::test_nsa_fwd_varlen_bench[nsa-slc-s8k-r2-h16-d64-b4-float16]

6 tests collected in 2.03s
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
6 passed, 6 warnings in 10.75s
--- benchmarks/ops/attention/bench_deepseek_nsa.py finished in 11s ---

=== [4/49] benchmarks/ops/attention/bench_gqa.py ===
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-8b-short-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-8b-short-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-8b-long-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-8b-long-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-70b-short-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-70b-short-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-70b-long-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-70b-long-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_varlen_fwd_bench[llama-8b-uniform-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_varlen_fwd_bench[llama-8b-uniform-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_varlen_fwd_bench[llama-8b-q-lt-kv-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_varlen_fwd_bench[llama-8b-q-lt-kv-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_varlen_fwd_bench[llama-70b-q-lt-kv-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_varlen_fwd_bench[llama-70b-q-lt-kv-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-bfloat16]
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
benchmarks/ops/attention/bench_gqa.py::test_gqa_dense_prefill_bench[prefill-rope-neox-q256-kv1792-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_dense_prefill_bench[prefill-rope-neox-q256-kv1792-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_dense_prefill_bench[prefill-scaled-q256-kv1792-float8_e4m3fn]
benchmarks/ops/attention/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-uniform-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-uniform-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-q-lt-kv-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-q-lt-kv-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-70b-q-lt-kv-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-70b-q-lt-kv-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-short-w256-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-short-w256-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-long-w1024-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-long-w1024-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-70b-short-w256-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-70b-short-w256-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-70b-long-w1024-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-70b-long-w1024-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-prefill-paged-fullattn-b8-prefix32k-chunk1k-p64-partial-rope64-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-prefill-paged-fullattn-mixed-b8-p64-partial-rope64-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-prefill-paged-b8-prefix4k-chunk512-p64-full-rope-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_paged_with_kv_cache_fwd_bench[gqa-prefill-paged-softcap50-b4-prefix4k-chunk512-p64-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-prefill-paged-fp8-cache-b8-prefix32k-chunk1k-p64-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-prefill-paged-fp8-cache-b8-prefix4k-chunk512-p64-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_prefill_paged_with_kv_cache_fwd_bench[gqa-prefill-paged-fp8-cache-softcap50-b4-prefix4k-chunk512-p64-float16]

63 tests collected in 1.97s
...............................................................          [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-8b-short-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-8b-short-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-8b-long-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-8b-long-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-70b-short-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-70b-short-bfloat16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-70b-long-float16]
benchmarks/ops/attention/bench_gqa.py::test_gqa_bwd_bench[llama-70b-long-bfloat16]
  /home/ci-runner/runner/_work/TileOPs/TileOPs/src/tileops/kernels/kernel_base.py:190: UserWarning: FlashAttnBwdPreprocessKernel does not define autotune_configs; falling back to the provided config or default_config.
    warnings.warn(  # noqa: B028

benchmarks/ops/attention/bench_gqa.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

benchmarks/ops/attention/bench_gqa.py::test_gqa_dense_prefill_bench[prefill-rope-neox-q256-kv1792-float16]
  /usr/local/lib/python3.12/dist-packages/torch/_inductor/compile_fx.py:321: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
    warnings.warn(

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
63 passed, 30 warnings in 287.76s (0:04:47)
--- benchmarks/ops/attention/bench_gqa.py finished in 288s ---

=== [5/49] benchmarks/ops/attention/bench_gqa_decode_paged.py ===
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

11 tests collected in 2.05s
........sss                                                              [100%]Benchmark report saved to profile_run.log

8 passed, 3 skipped in 11.45s
--- benchmarks/ops/attention/bench_gqa_decode_paged.py finished in 12s ---

=== [6/49] benchmarks/ops/attention/bench_mha.py ===
benchmarks/ops/attention/bench_mha.py::test_mha_bwd_bench[llama-8b-short-float16]
benchmarks/ops/attention/bench_mha.py::test_mha_bwd_bench[llama-8b-short-bfloat16]
benchmarks/ops/attention/bench_mha.py::test_mha_bwd_bench[llama-8b-long-float16]
benchmarks/ops/attention/bench_mha.py::test_mha_bwd_bench[llama-8b-long-bfloat16]
benchmarks/ops/attention/bench_mha.py::test_mha_bwd_bench[llama-70b-short-float16]
benchmarks/ops/attention/bench_mha.py::test_mha_bwd_bench[llama-70b-short-bfloat16]
benchmarks/ops/attention/bench_mha.py::test_mha_bwd_bench[llama-70b-long-float16]
benchmarks/ops/attention/bench_mha.py::test_mha_bwd_bench[llama-70b-long-bfloat16]

8 tests collected in 2.06s
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
  /home/ci-runner/runner/_work/TileOPs/TileOPs/src/tileops/kernels/kernel_base.py:190: UserWarning: FlashAttnBwdPreprocessKernel does not define autotune_configs; falling back to the provided config or default_config.
    warnings.warn(  # noqa: B028

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
8 passed, 8 warnings in 8.83s
--- benchmarks/ops/attention/bench_mha.py finished in 9s ---

=== [7/49] benchmarks/ops/attention/bench_mha_decode_paged.py ===
benchmarks/ops/attention/bench_mha_decode_paged.py::test_mha_decode_paged_bench[single-token-page128-float16]
benchmarks/ops/attention/bench_mha_decode_paged.py::test_mha_decode_paged_bench[batch2-page256-float16]
benchmarks/ops/attention/bench_mha_decode_paged.py::test_mha_decode_paged_bench[longer-cache-float16]
benchmarks/ops/attention/bench_mha_decode_paged.py::test_mha_decode_paged_bench[shorter-cache-float16]

4 tests collected in 1.65s
....                                                                     [100%]Benchmark report saved to profile_run.log

4 passed in 35.72s
--- benchmarks/ops/attention/bench_mha_decode_paged.py finished in 36s ---

=== [8/49] benchmarks/ops/bench_ada_layer_norm.py ===
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

10 tests collected in 1.42s
..........                                                               [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_ada_layer_norm.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
10 passed, 14 warnings in 13.30s
--- benchmarks/ops/bench_ada_layer_norm.py finished in 14s ---

=== [9/49] benchmarks/ops/bench_argreduce.py ===
benchmarks/ops/bench_argreduce.py::test_argmax_bench[lm-head-argmax-float16]
benchmarks/ops/bench_argreduce.py::test_argmax_bench[lm-head-argmax-bfloat16]
benchmarks/ops/bench_argreduce.py::test_argmax_bench[hidden-state-argmax-float16]
benchmarks/ops/bench_argreduce.py::test_argmax_bench[hidden-state-argmax-bfloat16]
benchmarks/ops/bench_argreduce.py::test_argmax_bench[3d-non-last-axis-argmax-float16]
benchmarks/ops/bench_argreduce.py::test_argmin_bench[lm-head-argmin-float16]
benchmarks/ops/bench_argreduce.py::test_argmin_bench[lm-head-argmin-bfloat16]
benchmarks/ops/bench_argreduce.py::test_argmin_bench[hidden-state-argmin-float16]
benchmarks/ops/bench_argreduce.py::test_argmin_bench[hidden-state-argmin-bfloat16]

9 tests collected in 1.41s
.........                                                                [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_argreduce.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_argreduce.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
9 passed, 58 warnings in 13.69s
--- benchmarks/ops/bench_argreduce.py finished in 14s ---

=== [10/49] benchmarks/ops/bench_batch_norm.py ===
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

10 tests collected in 1.31s
..........                                                               [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_batch_norm.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_batch_norm.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
10 passed, 58 warnings in 18.40s
--- benchmarks/ops/bench_batch_norm.py finished in 19s ---

=== [11/49] benchmarks/ops/bench_binary_elementwise.py ===
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

63 tests collected in 1.42s
...............................................................          [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_binary_elementwise.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
63 passed, 14 warnings in 50.93s
--- benchmarks/ops/bench_binary_elementwise.py finished in 52s ---

=== [12/49] benchmarks/ops/bench_bmm.py ===
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

26 tests collected in 1.44s
..........................                                               [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_bmm.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_bmm.py::test_bmm_fp8_kn_bench[square-b4-1k-per-tensor-float8_e4m3fn]
  /home/ci-runner/runner/_work/TileOPs/TileOPs/src/tileops/ops/gemm/bmm.py:438: UserWarning: BmmFp8FwdOp: b (shape=(4, 1024, 1024)) does not lie K-innermost, so it is transposed into a new buffer before the FP8 WGMMA kernel, which reads only that order. Passing b K-innermost skips the copy and is the faster call.
    b = self._as_k_innermost(b, a.dtype, a.device)

benchmarks/ops/bench_bmm.py::test_bmm_fp8_kn_bench[square-b8-2k-per-tensor-float8_e4m3fn]
  /home/ci-runner/runner/_work/TileOPs/TileOPs/src/tileops/ops/gemm/bmm.py:438: UserWarning: BmmFp8FwdOp: b (shape=(8, 2048, 2048)) does not lie K-innermost, so it is transposed into a new buffer before the FP8 WGMMA kernel, which reads only that order. Passing b K-innermost skips the copy and is the faster call.
    b = self._as_k_innermost(b, a.dtype, a.device)

benchmarks/ops/bench_bmm.py::test_bmm_fp8_kn_bench[mha-decode-b32-pv-per-tensor-float8_e4m3fn]
  /home/ci-runner/runner/_work/TileOPs/TileOPs/src/tileops/ops/gemm/bmm.py:438: UserWarning: BmmFp8FwdOp: b (shape=(32, 2048, 128)) does not lie K-innermost, so it is transposed into a new buffer before the FP8 WGMMA kernel, which reads only that order. Passing b K-innermost skips the copy and is the faster call.
    b = self._as_k_innermost(b, a.dtype, a.device)

benchmarks/ops/bench_bmm.py::test_bmm_fp8_kn_bench[mha-decode-b64-qk-per-tensor-float8_e4m3fn]
  /home/ci-runner/runner/_work/TileOPs/TileOPs/src/tileops/ops/gemm/bmm.py:438: UserWarning: BmmFp8FwdOp: b (shape=(64, 128, 2048)) does not lie K-innermost, so it is transposed into a new buffer before the FP8 WGMMA kernel, which reads only that order. Passing b K-innermost skips the copy and is the faster call.
    b = self._as_k_innermost(b, a.dtype, a.device)

benchmarks/ops/bench_bmm.py::test_bmm_fp8_kn_bench[moe-prefill-b128-per-tensor-float8_e4m3fn]
  /home/ci-runner/runner/_work/TileOPs/TileOPs/src/tileops/ops/gemm/bmm.py:438: UserWarning: BmmFp8FwdOp: b (shape=(128, 2048, 512)) does not lie K-innermost, so it is transposed into a new buffer before the FP8 WGMMA kernel, which reads only that order. Passing b K-innermost skips the copy and is the faster call.
    b = self._as_k_innermost(b, a.dtype, a.device)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
26 passed, 49 warnings in 49.67s
--- benchmarks/ops/bench_bmm.py finished in 50s ---

=== [13/49] benchmarks/ops/bench_convolution.py ===
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

55 tests collected in 1.34s
.......................................................                  [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_convolution.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_convolution.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
55 passed, 58 warnings in 54.13s
--- benchmarks/ops/bench_convolution.py finished in 55s ---

=== [14/49] benchmarks/ops/bench_cumulative.py ===
benchmarks/ops/bench_cumulative.py::test_cumsum_bench[hidden-state-scan-float16]
benchmarks/ops/bench_cumulative.py::test_cumsum_bench[hidden-state-scan-bfloat16]
benchmarks/ops/bench_cumulative.py::test_cumsum_bench[long-seq-scan-bfloat16]
benchmarks/ops/bench_cumulative.py::test_cumprod_bench[hidden-state-scan-float16]
benchmarks/ops/bench_cumulative.py::test_cumprod_bench[hidden-state-scan-bfloat16]
benchmarks/ops/bench_cumulative.py::test_cumprod_bench[long-seq-scan-bfloat16]

6 tests collected in 1.35s
......                                                                   [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_cumulative.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_cumulative.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
6 passed, 58 warnings in 12.63s
--- benchmarks/ops/bench_cumulative.py finished in 13s ---

=== [15/49] benchmarks/ops/bench_deltanet.py ===
benchmarks/ops/bench_deltanet.py::test_deltanet_dense_prefill_bench[prefill-medium-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_dense_prefill_bench[prefill-long-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_dense_prefill_bench[prefill-very-long-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_dense_prefill_bench[prefill-wide-bfloat16]
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
24 tests collected in 13.82s
.STALLED: benchmarks/ops/bench_deltanet.py: no test started for 900s at benchmarks/ops/bench_deltanet.py::test_deltanet_dense_prefill_bench[prefill-long-bfloat16]; killed, stack dump at bench_stack_dumps/bench_deltanet.txt
--- benchmarks/ops/bench_deltanet.py finished in 913s ---

=== [16/49] benchmarks/ops/bench_deltanet_recurrence.py ===
benchmarks/ops/bench_deltanet_recurrence.py::test_deltanet_decode_bench[delta-decode-serving-b1-h8-d128-bfloat16]
benchmarks/ops/bench_deltanet_recurrence.py::test_deltanet_decode_bench[delta-decode-serving-b1-h16-d128-bfloat16]
benchmarks/ops/bench_deltanet_recurrence.py::test_deltanet_decode_bench[delta-decode-serving-b1-h32-d128-bfloat16]
benchmarks/ops/bench_deltanet_recurrence.py::test_deltanet_decode_bench[delta-decode-serving-b1-h48-d128-bfloat16]
benchmarks/ops/bench_deltanet_recurrence.py::test_deltanet_decode_bench[delta-decode-serving-b1-h64-d128-bfloat16]
benchmarks/ops/bench_deltanet_recurrence.py::test_deltanet_decode_bench[delta-decode-serving-b8-h32-d128-bfloat16]
benchmarks/ops/bench_deltanet_recurrence.py::test_deltanet_decode_bench[delta-decode-serving-b8-h48-d128-bfloat16]
benchmarks/ops/bench_deltanet_recurrence.py::test_deltanet_decode_bench[delta-decode-serving-b8-h64-d128-bfloat16]

8 tests collected in 1.62s
........                                                                 [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_deltanet_recurrence.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

benchmarks/ops/bench_deltanet_recurrence.py::test_deltanet_decode_bench[delta-decode-serving-b1-h8-d128-bfloat16]
  /usr/local/lib/python3.12/dist-packages/torch/_inductor/compile_fx.py:321: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
8 passed, 15 warnings in 15.38s
--- benchmarks/ops/bench_deltanet_recurrence.py finished in 16s ---

=== [17/49] benchmarks/ops/bench_dropout.py ===
benchmarks/ops/bench_dropout.py::test_dropout_bench[tokens-1k-hidden-4k-float16]
benchmarks/ops/bench_dropout.py::test_dropout_bench[tokens-1k-hidden-4k-float32]
benchmarks/ops/bench_dropout.py::test_dropout_bench[tokens-1k-hidden-10k-bfloat16]

3 tests collected in 1.29s
...                                                                      [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_dropout.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
3 passed, 14 warnings in 8.42s
--- benchmarks/ops/bench_dropout.py finished in 9s ---

=== [18/49] benchmarks/ops/bench_elementwise_manifest.py ===
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

215 tests collected in 1.40s
........................................................................ [ 33%]
........................................................................ [ 66%]
.......................................................................  [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_elementwise_manifest.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
215 passed, 14 warnings in 130.16s (0:02:10)
--- benchmarks/ops/bench_elementwise_manifest.py finished in 131s ---

=== [19/49] benchmarks/ops/bench_engram.py ===
benchmarks/ops/bench_engram.py::test_engram_gate_conv_fwd_bench[fwd-b1-s32-d256-float16]
benchmarks/ops/bench_engram.py::test_engram_gate_conv_fwd_bench[fwd-b2-s64-d512-float16]
benchmarks/ops/bench_engram.py::test_engram_gate_conv_fwd_bench[fwd-b1-s128-d256-bfloat16]
benchmarks/ops/bench_engram.py::test_engram_gate_conv_bwd_bench[bwd-b1-s32-d256-float16]
benchmarks/ops/bench_engram.py::test_engram_gate_conv_bwd_bench[bwd-b2-s64-d512-float16]
benchmarks/ops/bench_engram.py::test_engram_gate_conv_bwd_bench[bwd-b1-s128-d256-bfloat16]
benchmarks/ops/bench_engram.py::test_engram_decode_bench[decode-b1-dmem512-d256-float16]
benchmarks/ops/bench_engram.py::test_engram_decode_bench[decode-b4-dmem1024-d512-float16]
benchmarks/ops/bench_engram.py::test_engram_decode_bench[decode-b8-dmem512-d256-bfloat16]

9 tests collected in 1.39s
.........                                                                [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_engram.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

benchmarks/ops/bench_engram.py::test_engram_decode_bench[decode-b1-dmem512-d256-float16]
  /usr/local/lib/python3.12/dist-packages/torch/_inductor/compile_fx.py:321: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
9 passed, 15 warnings in 83.11s (0:01:23)
--- benchmarks/ops/bench_engram.py finished in 84s ---

=== [20/49] benchmarks/ops/bench_fft.py ===
benchmarks/ops/bench_fft.py::test_fft_bench[fft-4k-c64-unbatched-complex64]
benchmarks/ops/bench_fft.py::test_fft_bench[fft-4k-c64-b64-complex64]
benchmarks/ops/bench_fft.py::test_fft_bench[fft-4k-c128-b64-complex128]

3 tests collected in 1.23s
...                                                                      [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_fft.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

benchmarks/ops/bench_fft.py::test_fft_bench[fft-4k-c64-unbatched-complex64]
  /usr/local/lib/python3.12/dist-packages/torch/_inductor/lowering.py:2633: UserWarning: Torchinductor does not support code generation for complex operators. Performance may be worse than eager.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
3 passed, 15 warnings in 9.83s
--- benchmarks/ops/bench_fft.py finished in 10s ---

=== [21/49] benchmarks/ops/bench_fp8_lightning_indexer.py ===
benchmarks/ops/bench_fp8_lightning_indexer.py::test_fp8_lightning_indexer_bench[lightning-indexer-s8k-h32-d64-bfloat16]

1 test collected in 1.31s
.                                                                        [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_fp8_lightning_indexer.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

benchmarks/ops/bench_fp8_lightning_indexer.py::test_fp8_lightning_indexer_bench[lightning-indexer-s8k-h32-d64-bfloat16]
  /usr/local/lib/python3.12/dist-packages/torch/_inductor/compile_fx.py:321: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
1 passed, 15 warnings in 17.38s
--- benchmarks/ops/bench_fp8_lightning_indexer.py finished in 18s ---

=== [22/49] benchmarks/ops/bench_fp8_quant.py ===
benchmarks/ops/bench_fp8_quant.py::test_fp8_quant_bench[kv-index-8k-d64-float16]
benchmarks/ops/bench_fp8_quant.py::test_fp8_quant_bench[kv-index-8k-d64-bfloat16]
benchmarks/ops/bench_fp8_quant.py::test_fp8_quant_bench[kv-index-4k-d128-float32]

3 tests collected in 1.26s
...                                                                      [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_fp8_quant.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
3 passed, 14 warnings in 8.95s
--- benchmarks/ops/bench_fp8_quant.py finished in 9s ---

=== [23/49] benchmarks/ops/bench_fused_moe_experts.py ===
benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_bench[qwen3-235b-decode-float16]
benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_bench[qwen3-235b-decode-bfloat16]
benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_bench[qwen3-235b-prefill-float16]
benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_bench[qwen3-235b-prefill-bfloat16]
benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_bench[deepseek-v3-decode-float16]
benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_bench[deepseek-v3-decode-bfloat16]
benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_bench[deepseek-v3-prefill-float16]
benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_bench[deepseek-v3-prefill-bfloat16]
benchmarks/ops/bench_fused_moe_experts.py::test_indexed_expert_mlp_bench[deepseek-v3-decode-1-float16]
benchmarks/ops/bench_fused_moe_experts.py::test_indexed_expert_mlp_bench[deepseek-v3-decode-1-bfloat16]
benchmarks/ops/bench_fused_moe_experts.py::test_indexed_expert_mlp_bench[deepseek-v3-decode-32-float16]
benchmarks/ops/bench_fused_moe_experts.py::test_indexed_expert_mlp_bench[deepseek-v3-decode-32-bfloat16]
benchmarks/ops/bench_fused_moe_experts.py::test_indexed_expert_mlp_bench[deepseek-v3-decode-64-float16]
benchmarks/ops/bench_fused_moe_experts.py::test_indexed_expert_mlp_bench[deepseek-v3-decode-64-bfloat16]
benchmarks/ops/bench_fused_moe_experts.py::test_indexed_expert_mlp_bench[qwen3-235b-decode-32-float16]
benchmarks/ops/bench_fused_moe_experts.py::test_indexed_expert_mlp_bench[qwen3-235b-decode-32-bfloat16]

=============================== warnings summary ===============================
../../../../../../usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

../../../../../../usr/local/lib/python3.12/dist-packages/_pytest/assertion/rewrite.py:197
  /usr/local/lib/python3.12/dist-packages/_pytest/assertion/rewrite.py:197: RuntimeWarning: vLLM CUTLASS MoE baseline unavailable (No module named 'vllm.model_executor.layers.fused_moe.cutlass_moe'); the vllm-cutlass column will be omitted from results.
    exec(co, module.__dict__)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
16 tests collected in 11.62s
................                                                         [100%]Benchmark report saved to profile_run.log

16 passed in 150.99s (0:02:30)
--- benchmarks/ops/bench_fused_moe_experts.py finished in 152s ---

=== [24/49] benchmarks/ops/bench_gated_deltanet.py ===
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_dense_prefill_bench[serving-prefill-medium-float16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_dense_prefill_bench[serving-prefill-medium-bfloat16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_dense_prefill_bench[serving-prefill-long-irregular-float16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_dense_prefill_bench[serving-prefill-long-irregular-bfloat16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_dense_prefill_bench[serving-prefill-long-float16]
benchmarks/ops/bench_gated_deltanet.py::test_gated_deltanet_dense_prefill_bench[serving-prefill-long-bfloat16]

=============================== warnings summary ===============================
../../../../../../usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
6 tests collected in 13.71s
......                                                                   [100%]Benchmark report saved to profile_run.log

6 passed in 6.55s
--- benchmarks/ops/bench_gated_deltanet.py finished in 7s ---

=== [25/49] benchmarks/ops/bench_gemm.py ===
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
benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[batched-decode-two-requests-float16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[batched-decode-server-batch-float16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[batched-decode-wide-batch-float16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[chunked-prefill-tile-float16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[prefill-mlp-up-projection-float16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[decode-llama3-8b-mlp-down-float16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[prefill-llama3-8b-mlp-down-float16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[prefill-qwen3-32b-mlp-down-float16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[decode-tp8-attention-out-float16]

46 tests collected in 1.37s
..............................................                           [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_gemm.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_gemm.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
46 passed, 58 warnings in 280.92s (0:04:40)
--- benchmarks/ops/bench_gemm.py finished in 282s ---

=== [26/49] benchmarks/ops/bench_gla_chunkwise.py ===
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
16 tests collected in 13.57s
........XXXXXXXX                                                         [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_gla_chunkwise.py: 56 warnings
  /usr/local/lib/python3.12/dist-packages/tilelang/jit/kernel.py:161: DeprecationWarning: `tl.disable_tma_lower` is deprecated and will be removed in v0.1.10. Use `T.copy(..., disable_tma=True)` per-copy instead.
    instance = cls(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
8 passed, 8 xpassed, 56 warnings in 13.01s
--- benchmarks/ops/bench_gla_chunkwise.py finished in 14s ---

=== [27/49] benchmarks/ops/bench_gla_recurrence.py ===
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
8 tests collected in 13.82s
........                                                                 [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_gla_recurrence.py::test_gla_decode_bench[gla-decode-serving-b1-h8-d128-bfloat16]
  /usr/local/lib/python3.12/dist-packages/torch/_inductor/compile_fx.py:321: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
8 passed, 1 warning in 9.62s
--- benchmarks/ops/bench_gla_recurrence.py finished in 10s ---

=== [28/49] benchmarks/ops/bench_group_norm.py ===
benchmarks/ops/bench_group_norm.py::test_group_norm_bench[image-g32-affine-float16]
benchmarks/ops/bench_group_norm.py::test_group_norm_bench[image-g32-affine-bfloat16]
benchmarks/ops/bench_group_norm.py::test_group_norm_bench[wider-channel-g32-affine-float16]
benchmarks/ops/bench_group_norm.py::test_group_norm_bench[tail-spatial-g16-affine-float16]
benchmarks/ops/bench_group_norm.py::test_group_norm_no_affine_bench[image-g32-float16]
benchmarks/ops/bench_group_norm.py::test_group_norm_no_affine_bench[image-g32-bfloat16]
benchmarks/ops/bench_group_norm.py::test_group_norm_no_affine_bench[wider-channel-g32-float16]
benchmarks/ops/bench_group_norm.py::test_group_norm_no_affine_bench[tail-spatial-g16-float16]

8 tests collected in 1.40s
........                                                                 [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_group_norm.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_group_norm.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
8 passed, 58 warnings in 15.33s
--- benchmarks/ops/bench_group_norm.py finished in 16s ---

=== [29/49] benchmarks/ops/bench_grouped_gemm.py ===
benchmarks/ops/bench_grouped_gemm.py::test_grouped_gemm_bench[nt-batch16-m4096-n4096-k4096-float16]
benchmarks/ops/bench_grouped_gemm.py::test_grouped_gemm_bench[nt-batch16-m4096-n4096-k4096-bfloat16]
benchmarks/ops/bench_grouped_gemm.py::test_grouped_gemm_bench[nn-batch16-m4096-n4096-k4096-float16]
benchmarks/ops/bench_grouped_gemm.py::test_grouped_gemm_bench[tn-batch16-m4096-n4096-k4096-float16]

4 tests collected in 1.36s
....                                                                     [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_grouped_gemm.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

benchmarks/ops/bench_grouped_gemm.py::test_grouped_gemm_bench[nt-batch16-m4096-n4096-k4096-float16]
benchmarks/ops/bench_grouped_gemm.py::test_grouped_gemm_bench[nt-batch16-m4096-n4096-k4096-bfloat16]
benchmarks/ops/bench_grouped_gemm.py::test_grouped_gemm_bench[nn-batch16-m4096-n4096-k4096-float16]
benchmarks/ops/bench_grouped_gemm.py::test_grouped_gemm_bench[tn-batch16-m4096-n4096-k4096-float16]
  /home/ci-runner/runner/_work/TileOPs/TileOPs/src/tileops/kernels/kernel_base.py:190: UserWarning: GemmTemplate does not define autotune_configs; falling back to the provided config or default_config.
    warnings.warn(  # noqa: B028

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
4 passed, 18 warnings in 12.59s
--- benchmarks/ops/bench_grouped_gemm.py finished in 13s ---

=== [30/49] benchmarks/ops/bench_independent_elementwise.py ===
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

23 tests collected in 1.39s
.......................                                                  [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_independent_elementwise.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
23 passed, 14 warnings in 23.17s
--- benchmarks/ops/bench_independent_elementwise.py finished in 24s ---

=== [31/49] benchmarks/ops/bench_instance_norm.py ===
benchmarks/ops/bench_instance_norm.py::test_instance_norm_bench[image-affine-float16]
benchmarks/ops/bench_instance_norm.py::test_instance_norm_bench[image-affine-bfloat16]
benchmarks/ops/bench_instance_norm.py::test_instance_norm_bench[wider-channel-affine-float16]
benchmarks/ops/bench_instance_norm.py::test_instance_norm_bench[tail-spatial-affine-float16]
benchmarks/ops/bench_instance_norm.py::test_instance_norm_bench[image-float16]
benchmarks/ops/bench_instance_norm.py::test_instance_norm_bench[image-bfloat16]
benchmarks/ops/bench_instance_norm.py::test_instance_norm_bench[wider-channel-float16]
benchmarks/ops/bench_instance_norm.py::test_instance_norm_bench[tail-spatial-float16]

8 tests collected in 1.33s
........                                                                 [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_instance_norm.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_instance_norm.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
8 passed, 58 warnings in 14.56s
--- benchmarks/ops/bench_instance_norm.py finished in 15s ---

=== [32/49] benchmarks/ops/bench_logical_reduce.py ===
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

10 tests collected in 1.40s
..........                                                               [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_logical_reduce.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_logical_reduce.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
10 passed, 58 warnings in 18.01s
--- benchmarks/ops/bench_logical_reduce.py finished in 19s ---

=== [33/49] benchmarks/ops/bench_mamba.py ===
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

27 tests collected in 9.48s
...........................                                              [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_mamba.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

benchmarks/ops/bench_mamba.py::test_ssd_chunk_scan_fwd_bench[mamba2-780m-b1-s4k-float16]
  /usr/local/lib/python3.12/dist-packages/torch/_inductor/compile_fx.py:321: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
27 passed, 15 warnings in 95.15s (0:01:35)
--- benchmarks/ops/bench_mamba.py finished in 96s ---

=== [34/49] benchmarks/ops/bench_mamba2_e2e.py ===
benchmarks/ops/bench_mamba2_e2e.py::test_mamba2_fwd_bench[mamba2-2p7b-b1-s2k-bfloat16]
benchmarks/ops/bench_mamba2_e2e.py::test_mamba2_fwd_bench[mamba2-1p3b-b1-s8k-float16]
benchmarks/ops/bench_mamba2_e2e.py::test_mamba2_fwd_bench[mamba2-2p7b-b1-s2k-dt-bias-bfloat16]
benchmarks/ops/bench_mamba2_e2e.py::test_mamba2_fwd_bench[mamba2-1p3b-b1-s8k-dt-bias-float16]
benchmarks/ops/bench_mamba2_e2e.py::test_mamba2_fwd_bench[mamba2-2p7b-b1-s2k-init-states-bfloat16]
benchmarks/ops/bench_mamba2_e2e.py::test_mamba2_fwd_bench[mamba2-1p3b-b1-s8k-init-states-float16]
benchmarks/ops/bench_mamba2_e2e.py::test_mamba2_fwd_bench[mamba2-2p7b-b1-s2k-dt-bias-init-states-bfloat16]
benchmarks/ops/bench_mamba2_e2e.py::test_mamba2_fwd_bench[mamba2-1p3b-b1-s8k-dt-bias-init-states-float16]

8 tests collected in 9.39s
........                                                                 [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_mamba2_e2e.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

benchmarks/ops/bench_mamba2_e2e.py::test_mamba2_fwd_bench[mamba2-2p7b-b1-s2k-bfloat16]
  /usr/local/lib/python3.12/dist-packages/torch/_inductor/compile_fx.py:321: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
8 passed, 15 warnings in 58.50s
--- benchmarks/ops/bench_mamba2_e2e.py finished in 59s ---

=== [35/49] benchmarks/ops/bench_mean_pooling.py ===
benchmarks/ops/bench_mean_pooling.py::test_mean_pooling_bench[uniform-8k-float16]
benchmarks/ops/bench_mean_pooling.py::test_mean_pooling_bench[uniform-batched-float16]
benchmarks/ops/bench_mean_pooling.py::test_mean_pooling_bench[ragged-even-float16]
benchmarks/ops/bench_mean_pooling.py::test_mean_pooling_bench[ragged-tail-float16]
benchmarks/ops/bench_mean_pooling.py::test_mean_pooling_bench[ragged-batched-float16]

5 tests collected in 1.36s
.....                                                                    [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_mean_pooling.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
5 passed, 14 warnings in 24.15s
--- benchmarks/ops/bench_mean_pooling.py finished in 25s ---

=== [36/49] benchmarks/ops/bench_mhc.py ===
benchmarks/ops/bench_mhc.py::test_mhc_pre_bench[pre-small-bfloat16]
benchmarks/ops/bench_mhc.py::test_mhc_pre_bench[pre-medium-bfloat16]
benchmarks/ops/bench_mhc.py::test_mhc_pre_bench[pre-large-bfloat16]
benchmarks/ops/bench_mhc.py::test_mhc_post_bench[post-small-bfloat16]
benchmarks/ops/bench_mhc.py::test_mhc_post_bench[post-medium-bfloat16]
benchmarks/ops/bench_mhc.py::test_mhc_post_bench[post-large-bfloat16]

6 tests collected in 1.29s
......                                                                   [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_mhc.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

benchmarks/ops/bench_mhc.py::test_mhc_pre_bench[pre-small-bfloat16]
  /usr/local/lib/python3.12/dist-packages/torch/_inductor/compile_fx.py:321: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
6 passed, 15 warnings in 52.49s
--- benchmarks/ops/bench_mhc.py finished in 53s ---

=== [37/49] benchmarks/ops/bench_moe_fused_moe.py ===
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
6 tests collected in 11.79s
......                                                                   [100%]Benchmark report saved to profile_run.log

6 passed in 17.03s
--- benchmarks/ops/bench_moe_fused_moe.py finished in 18s ---

=== [38/49] benchmarks/ops/bench_moe_fused_moe_shared_expert.py ===
benchmarks/ops/bench_moe_fused_moe_shared_expert.py::test_fused_moe_shared_expert_bench[kimi-k2-t1-bfloat16]
benchmarks/ops/bench_moe_fused_moe_shared_expert.py::test_fused_moe_shared_expert_bench[kimi-k2-t32-bfloat16]
benchmarks/ops/bench_moe_fused_moe_shared_expert.py::test_fused_moe_shared_expert_bench[kimi-k2-t64-bfloat16]
benchmarks/ops/bench_moe_fused_moe_shared_expert.py::test_fused_moe_shared_expert_bench[kimi-k2-t128-bfloat16]
benchmarks/ops/bench_moe_fused_moe_shared_expert.py::test_fused_moe_shared_expert_bench[kimi-k2-t512-bfloat16]
benchmarks/ops/bench_moe_fused_moe_shared_expert.py::test_fused_moe_shared_expert_bench[kimi-k2-t2048-bfloat16]
benchmarks/ops/bench_moe_fused_moe_shared_expert.py::test_fused_moe_shared_expert_bench[kimi-k2-t4096-bfloat16]
benchmarks/ops/bench_moe_fused_moe_shared_expert.py::test_fused_moe_shared_expert_bench[deepseek-v3-t1-bfloat16]
benchmarks/ops/bench_moe_fused_moe_shared_expert.py::test_fused_moe_shared_expert_bench[deepseek-v3-t32-bfloat16]
benchmarks/ops/bench_moe_fused_moe_shared_expert.py::test_fused_moe_shared_expert_bench[deepseek-v3-t64-bfloat16]
benchmarks/ops/bench_moe_fused_moe_shared_expert.py::test_fused_moe_shared_expert_bench[deepseek-v3-t128-bfloat16]
benchmarks/ops/bench_moe_fused_moe_shared_expert.py::test_fused_moe_shared_expert_bench[deepseek-v3-t512-bfloat16]
benchmarks/ops/bench_moe_fused_moe_shared_expert.py::test_fused_moe_shared_expert_bench[deepseek-v3-t2048-bfloat16]
benchmarks/ops/bench_moe_fused_moe_shared_expert.py::test_fused_moe_shared_expert_bench[deepseek-v3-t4096-bfloat16]
benchmarks/ops/bench_moe_fused_moe_shared_expert.py::test_fused_moe_shared_expert_bench[glm-4.5-t1-bfloat16]
benchmarks/ops/bench_moe_fused_moe_shared_expert.py::test_fused_moe_shared_expert_bench[glm-4.5-t32-bfloat16]
benchmarks/ops/bench_moe_fused_moe_shared_expert.py::test_fused_moe_shared_expert_bench[glm-4.5-t64-bfloat16]
benchmarks/ops/bench_moe_fused_moe_shared_expert.py::test_fused_moe_shared_expert_bench[glm-4.5-t128-bfloat16]
benchmarks/ops/bench_moe_fused_moe_shared_expert.py::test_fused_moe_shared_expert_bench[glm-4.5-t512-bfloat16]
benchmarks/ops/bench_moe_fused_moe_shared_expert.py::test_fused_moe_shared_expert_bench[glm-4.5-t2048-bfloat16]
benchmarks/ops/bench_moe_fused_moe_shared_expert.py::test_fused_moe_shared_expert_bench[glm-4.5-t4096-bfloat16]
benchmarks/ops/bench_moe_fused_moe_shared_expert.py::test_fused_moe_shared_expert_bench[qwen3-235b-routed-only-bfloat16]

=============================== warnings summary ===============================
../../../../../../usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
22 tests collected in 11.53s
......................                                                   [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_moe_fused_moe_shared_expert.py::test_fused_moe_shared_expert_bench[qwen3-235b-routed-only-bfloat16]
  /usr/local/lib/python3.12/dist-packages/_pytest/python.py:166: UserWarning: No baseline recorded for FusedMoeSharedExpertFwdOp: vLLM is not installed, or the row is routed-only and the vLLM path here always builds a shared expert.
    result = testfunction(**testargs)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
22 passed, 1 warning in 115.15s (0:01:55)
--- benchmarks/ops/bench_moe_fused_moe_shared_expert.py finished in 116s ---

=== [39/49] benchmarks/ops/bench_moe_fused_topk.py ===
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
7 tests collected in 11.56s
.......                                                                  [100%]Benchmark report saved to profile_run.log

7 passed in 2.89s
--- benchmarks/ops/bench_moe_fused_topk.py finished in 4s ---

=== [40/49] benchmarks/ops/bench_moe_permute_align.py ===
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

12 tests collected in 1.64s
............                                                             [100%]Benchmark report saved to profile_run.log

12 passed in 8.02s
--- benchmarks/ops/bench_moe_permute_align.py finished in 8s ---

=== [41/49] benchmarks/ops/bench_moe_staged.py ===
benchmarks/ops/bench_moe_staged.py::test_moe_pre_permute_bench[small-float16]
benchmarks/ops/bench_moe_staged.py::test_moe_pre_permute_bench[small-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_pre_permute_bench[prefill-float16]
benchmarks/ops/bench_moe_staged.py::test_moe_pre_permute_bench[prefill-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_post_permute_bench[small-float16]
benchmarks/ops/bench_moe_staged.py::test_moe_post_permute_bench[small-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_post_permute_bench[prefill-float16]
benchmarks/ops/bench_moe_staged.py::test_moe_post_permute_bench[prefill-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_grouped_gemm_bench[deepseek-v3-decode-gate-up-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_grouped_gemm_bench[deepseek-v3-prefill-gate-up-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_grouped_gemm_bench[deepseek-v3-decode-down-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_grouped_gemm_bench[deepseek-v3-prefill-down-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_grouped_gemm_bench[deepseek-v3-decode-gate-up-fused-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_grouped_gemm_bench[deepseek-v3-prefill-gate-up-fused-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_expert_mlp_bench[qwen3-235b-decode-float16]
benchmarks/ops/bench_moe_staged.py::test_moe_expert_mlp_bench[qwen3-235b-decode-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_expert_mlp_bench[qwen3-235b-prefill-float16]
benchmarks/ops/bench_moe_staged.py::test_moe_expert_mlp_bench[qwen3-235b-prefill-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_expert_mlp_bench[deepseek-v3-decode-float16]
benchmarks/ops/bench_moe_staged.py::test_moe_expert_mlp_bench[deepseek-v3-decode-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_expert_mlp_bench[deepseek-v3-prefill-float16]
benchmarks/ops/bench_moe_staged.py::test_moe_expert_mlp_bench[deepseek-v3-prefill-bfloat16]

=============================== warnings summary ===============================
../../../../../../usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
22 tests collected in 11.68s
......................                                                   [100%]Benchmark report saved to profile_run.log

22 passed in 78.26s (0:01:18)
--- benchmarks/ops/bench_moe_staged.py finished in 79s ---

=== [42/49] benchmarks/ops/bench_norm.py ===
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

33 tests collected in 1.35s
.................................                                        [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_norm.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_norm.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
33 passed, 58 warnings in 44.59s
--- benchmarks/ops/bench_norm.py finished in 45s ---

=== [43/49] benchmarks/ops/bench_pool.py ===
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

48 tests collected in 1.34s
................................................                         [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_pool.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

benchmarks/ops/bench_pool.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
48 passed, 58 warnings in 44.61s
--- benchmarks/ops/bench_pool.py finished in 45s ---

=== [44/49] benchmarks/ops/bench_reduce.py ===
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

33 tests collected in 1.37s
.................................                                        [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_reduce.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_reduce.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
33 passed, 58 warnings in 34.73s
--- benchmarks/ops/bench_reduce.py finished in 35s ---

=== [45/49] benchmarks/ops/bench_rope.py ===
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

13 tests collected in 1.31s
.............                                                            [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_rope.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
13 passed, 14 warnings in 14.86s
--- benchmarks/ops/bench_rope.py finished in 15s ---

=== [46/49] benchmarks/ops/bench_softmax.py ===
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

20 tests collected in 1.38s
....................                                                     [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_softmax.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_softmax.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
20 passed, 58 warnings in 27.97s
--- benchmarks/ops/bench_softmax.py finished in 29s ---

=== [47/49] benchmarks/ops/bench_topk_selector.py ===
benchmarks/ops/bench_topk_selector.py::test_topk_selector_bench[topk1024-s32k-kv64k-float32]
benchmarks/ops/bench_topk_selector.py::test_topk_selector_bench[topk2048-s32k-kv64k-float32]

2 tests collected in 1.29s
..                                                                       [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_topk_selector.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
2 passed, 14 warnings in 125.64s (0:02:05)
--- benchmarks/ops/bench_topk_selector.py finished in 126s ---

=== [48/49] benchmarks/ops/bench_unary_elementwise.py ===
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

107 tests collected in 1.38s
........................................................................ [ 67%]
...................................                                      [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_unary_elementwise.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
107 passed, 14 warnings in 65.05s (0:01:05)
--- benchmarks/ops/bench_unary_elementwise.py finished in 66s ---

=== [49/49] benchmarks/ops/bench_vector_norm.py ===
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

12 tests collected in 1.37s
............                                                             [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_vector_norm.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_vector_norm.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
12 passed, 58 warnings in 16.69s
--- benchmarks/ops/bench_vector_norm.py finished in 17s ---

1 benchmark file(s) failed:
  benchmarks/ops/bench_deltanet.py
