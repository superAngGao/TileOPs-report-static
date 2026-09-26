# ❌ TileOPs Nightly Report

> **2026-09-24 18:38** &ensp;|&ensp; `85455e46` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Correctness** | ✅ &ensp; (514/514 tests across 85 ops) |
| **Benchmarked Ops** | 179 |
| **Benchmark Failures** | ✅ None &ensp;|&ensp; ⚠️ 3 skipped |
| **Regressions** (vs 14-day median) | ⚠️ 8 |
| **Baseline Alerts** (< 80%) | ⚠️ 57 |
| **History window** | 12 runs, 2026-09-10 to 2026-09-23 |
| **Roofline anomalies** | ✅ None |
| **Never-built kernels** | ⚠️ 27 files **+3** &ensp;·&ensp; `kernels/linear_attention/gated_deltanet/compute_w_u_bwd.py` at 0.0% |
| **Untested roofline math** | 878 lines in `perf/` **+2** &ensp;·&ensp; `perf/formulas.py` at 11.6% |
| **Untested op logic** | 2589 lines in `ops/` **+150** &ensp;·&ensp; 36.5% of branches taken **−2.7pp** |
| | <sub>coverage compared against the 2026-09-23 run; no figure means it held</sub> |

## ⚠️ Performance Regressions (vs 14-day median)

| Op | Config | Median (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-float16] | 0.6692 | 1.0291 | +53.8% | 200.52 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.6691 | 1.0275 | +53.6% | 200.84 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.3501 | 0.5270 | +50.5% | 195.78 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-float16] | 0.3522 | 0.5277 | +49.8% | 195.51 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-bfloat16] | 0.0931 | 0.1252 | +34.5% | 103.28 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-float16] | 0.0932 | 0.1252 | +34.4% | 103.28 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0569 | 0.0692 | +21.7% | 93.44 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-float16] | 0.0571 | 0.0691 | +20.9% | 93.66 |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 80%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-bfloat16] | 0.4537 | 0.1423 | 31.4% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-bfloat16] | 0.4560 | 0.1431 | 31.4% | fa3 |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-b64-complex64] | 0.0152 | 0.0056 | 37.0% | torch-cufft |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-short-bfloat16] | 0.4083 | 0.1594 | 39.0% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-short-bfloat16] | 0.4141 | 0.1655 | 40.0% | fa3 |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c128-b64-complex128] | 0.0205 | 0.0085 | 41.3% | torch-cufft |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-bfloat16] | 1.3098 | 0.5492 | 41.9% | fa3 |
| 🔴 | **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-q-lt-kv-float16] | 0.1231 | 0.0535 | 43.5% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-q-lt-kv-bfloat16] | 0.1216 | 0.0532 | 43.7% | fa3 |
| 🔴 | **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-q-lt-kv-bfloat16] | 0.1213 | 0.0533 | 44.0% | fa3 |

<details>
<summary><strong>47 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-q-lt-kv-float16] | 0.1218 | 0.0537 | 44.1% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-bfloat16] | 1.2428 | 0.5893 | 47.4% | fa3 |
| 🔴 | **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-70b-q-lt-kv-bfloat16] | 0.2043 | 0.0983 | 48.1% | fa3 |
| 🔴 | **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-70b-q-lt-kv-float16] | 0.2059 | 0.0998 | 48.5% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-70b-q-lt-kv-float16] | 0.2052 | 0.0995 | 48.5% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-70b-q-lt-kv-bfloat16] | 0.2044 | 0.0991 | 48.5% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p256-float16] | 0.1649 | 0.0815 | 49.4% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-bfloat16] | 1.1036 | 0.5495 | 49.8% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-405b-p256-float16] | 0.0538 | 0.0270 | 50.2% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.5270 | 0.2714 | 51.5% | fa3 |
| 🔴 | **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-70b-long-w1024-bfloat16] | 1.0286 | 0.5297 | 51.5% | fa3 |
| 🔴 | **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.5280 | 0.2720 | 51.5% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-float16] | 1.0291 | 0.5303 | 51.5% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-bfloat16] | 1.0275 | 0.5297 | 51.5% | fa3 |
| 🔴 | **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-70b-long-w1024-float16] | 1.0292 | 0.5308 | 51.6% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-float16] | 0.5277 | 0.2738 | 51.9% | fa3 |
| 🔴 | **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-long-w1024-float16] | 0.5280 | 0.2744 | 52.0% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-70b-p256-float16] | 0.0667 | 0.0371 | 55.6% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 1.0178 | 0.5777 | 56.8% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-float16] | 0.2448 | 0.1431 | 58.5% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-float16] | 0.2433 | 0.1424 | 58.5% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[throughput-8b-p64-float16] | 0.2475 | 0.1508 | 60.9% | flashinfer |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-float16] | 0.9015 | 0.5521 | 61.2% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-float16] | 0.8925 | 0.5536 | 62.0% | fa3 |
| 🔴 | **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-70b-short-w256-bfloat16] | 0.1254 | 0.0833 | 66.4% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-bfloat16] | 0.1252 | 0.0832 | 66.5% | fa3 |
| 🔴 | **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-70b-short-w256-float16] | 0.1253 | 0.0836 | 66.7% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-float16] | 0.1252 | 0.0836 | 66.8% | fa3 |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-unbatched-complex64] | 0.0081 | 0.0054 | 66.9% | torch-cufft |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-bfloat16] | 0.0969 | 0.0657 | 67.8% | fla |
| 🔴 | **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0691 | 0.0469 | 67.9% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0692 | 0.0471 | 68.1% | fa3 |
| 🔴 | **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-short-w256-float16] | 0.0692 | 0.0473 | 68.3% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-float16] | 0.0691 | 0.0472 | 68.3% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-uniform-float16] | 0.0632 | 0.0448 | 70.9% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-float16] | 0.8335 | 0.5930 | 71.2% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-uniform-bfloat16] | 0.0628 | 0.0448 | 71.3% | fa3 |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-float16] | 0.0985 | 0.0702 | 71.3% | fla |
| 🔴 | **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-uniform-bfloat16] | 0.0628 | 0.0448 | 71.4% | fa3 |
| 🔴 | **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-uniform-float16] | 0.0628 | 0.0449 | 71.5% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.8089 | 0.5815 | 71.9% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-softcap50-float16] | 0.1730 | 0.1258 | 72.7% | flashinfer |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-float16] | 0.6175 | 0.4656 | 75.4% | fla |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-bfloat16] | 0.3114 | 0.2359 | 75.8% | fla |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-float16] | 0.1648 | 0.1256 | 76.2% | flashinfer |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-bfloat16] | 0.6107 | 0.4770 | 78.1% | fla |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-float16] | 0.3131 | 0.2477 | 79.1% | fla |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 27 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 878 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 2589 lines in `ops/`, 36.5% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 4002 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

### Never-built kernels

| File | Executed |
| --- | --- |
| `kernels/linear_attention/gated_deltanet/compute_w_u_bwd.py` | 0.0% |
| `kernels/linear_attention/gated_deltanet/prefill/forward.py` | 3.4% |
| `kernels/linear_attention/gated_deltanet/prefill/prepare.py` | 3.7% |
| `kernels/attention/deepseek_mla_decode.py` | 5.3% |
| `kernels/attention/gqa_fwd_ws.py` | 6.4% |
| `kernels/linear_attention/gated_deltanet/gated_deltanet_bwd.py` | 7.2% |
| `kernels/attention/gqa_fwd_fp8.py` | 7.5% |
| `kernels/attention/gqa_fwd.py` | 10.2% |
| `kernels/linear_attention/gla/dense_prefill_partitioned.py` | 10.5% |
| `kernels/attention/gqa_dense.py` | 10.8% |
| `kernels/linear_attention/gla/dense_prefill_subchunk.py` | 11.1% |
| `kernels/linear_attention/gated_deltanet/fused_prepare_compute_w_u.py` | 11.4% |
| `kernels/attention/mha_decode.py` | 11.7% |
| `kernels/attention/gqa_decode_bs1_common.py` | 12.4% |
| `kernels/attention/mha_decode_paged.py` | 12.5% |
| `kernels/linear_attention/gated_deltanet_recurrence.py` | 14.1% |
| `kernels/attention/gqa_decode.py` | 14.3% |
| `kernels/attention/gqa_decode_bs1.py` | 14.3% |
| `kernels/moe/indexed_expert_gemm.py` | 15.4% |
| `kernels/attention/gqa_decode_fp8.py` | 15.9% |
| `kernels/grouped_gemm/grouped_gemm.py` | 17.7% |
| `kernels/linear_attention/gated_deltanet/decode.py` | 17.8% |
| `kernels/attention/deepseek_nsa_cmp_fwd.py` | 18.1% |
| `kernels/linear_attention/gated_deltanet/prefill/dense.py` | 20.0% |
| `kernels/linear_attention/gated_deltanet/gated_deltanet_fwd.py` | 21.7% |
| `kernels/linear_attention/deltanet/dense_prefill.py` | 22.4% |
| `kernels/linear_attention/gated_deltanet/prefill/common.py` | 23.0% |

<details>
<summary>Untested pure Python, worst 15 files</summary>

| File | Uncovered | Executed |
| --- | --- | --- |
| `perf/formulas.py` | 836 | 11.6% |
| `ops/attention/gqa.py` | 555 | 32.2% |
| `ops/op_base.py` | 278 | 45.6% |
| `manifest/roofline_analysis.py` | 172 | 68.5% |
| `ops/linear_attention/gated_deltanet.py` | 123 | 15.8% |
| `ops/pool.py` | 87 | 84.8% |
| `ops/rope.py` | 84 | 69.9% |
| `ops/linear_attention/deltanet_inference.py` | 84 | 20.0% |
| `ops/mamba/mamba2_fwd.py` | 83 | 21.0% |
| `manifest/rule_eval.py` | 82 | 15.5% |
| `ops/convolution.py` | 82 | 79.7% |
| `ops/elementwise/_base.py` | 79 | 74.8% |
| `ops/linear_attention/gla_inference.py` | 78 | 22.8% |
| `ops/linear_attention/deltanet.py` | 72 | 64.2% |
| `ops/moe/staged.py` | 70 | 74.7% |

</details>

Per-line detail is in the `htmlcov/` directory of this run's `tileops_op_test` artifact.
