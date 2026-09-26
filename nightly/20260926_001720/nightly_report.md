# ✅ TileOPs Nightly Report

> **2026-09-25 18:48** &ensp;|&ensp; `1a8c844f` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Correctness** | ✅ &ensp; (516/516 tests across 85 ops) |
| **Benchmarked Ops** | 179 |
| **Benchmark Failures** | ✅ None &ensp;|&ensp; ⚠️ 3 skipped |
| **Regressions** (vs 14-day median) | ✅ None |
| **Baseline Alerts** (< 80%) | ⚠️ 29 |
| **History window** | 12 runs, 2026-09-12 to 2026-09-24 |
| **Roofline anomalies** | ✅ None |
| **Improvements** (vs 14-day best) | 🎉 25 |
| **Moved since previous run** | 🔵 25 |
| **Never-built kernels** | ⚠️ 28 files **+1** &ensp;·&ensp; `kernels/linear_attention/gated_deltanet/compute_w_u_bwd.py` at 0.0% |
| **Untested roofline math** | 878 lines in `perf/` &ensp;·&ensp; `perf/formulas.py` at 11.6% |
| **Untested op logic** | 2592 lines in `ops/` **+3** &ensp;·&ensp; 36.4% of branches taken |
| | <sub>coverage compared against the 2026-09-24 run; no figure means it held</sub> |

## 🎉 Performance Improvements (vs 14-day best)

| Op | Config | Prev Best (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-b64-complex64] | 0.0152 | 0.0044 | -71.1% | 3.59 |
| **FFTC2CFwdOp** | test_fft_bench[fft-4k-c128-b64-complex128] | 0.0204 | 0.0072 | -64.6% | 2.17 |
| **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-q-lt-kv-bfloat16] | 0.1213 | 0.0470 | -61.3% | 457.17 |
| **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-q-lt-kv-float16] | 0.1222 | 0.0475 | -61.2% | 452.70 |
| **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-70b-q-lt-kv-float16] | 0.2055 | 0.0877 | -57.3% | 489.68 |
| **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-70b-q-lt-kv-bfloat16] | 0.2043 | 0.0874 | -57.2% | 491.83 |
| **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-unbatched-complex64] | 0.0081 | 0.0036 | -56.3% | 0.07 |
| **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-uniform-bfloat16] | 0.0625 | 0.0354 | -43.4% | 243.40 |
| **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-uniform-float16] | 0.0628 | 0.0356 | -43.4% | 241.87 |
| **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-70b-long-w1024-bfloat16] | 1.0272 | 0.5885 | -42.7% | 350.63 |
| **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-70b-long-w1024-float16] | 1.0276 | 0.5903 | -42.6% | 349.58 |
| **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.5273 | 0.3047 | -42.2% | 338.68 |
| **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-long-w1024-float16] | 0.5272 | 0.3058 | -42.0% | 337.40 |
| **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-70b-short-w256-bfloat16] | 0.1254 | 0.0820 | -34.6% | 157.72 |
| **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-70b-short-w256-float16] | 0.1253 | 0.0821 | -34.5% | 157.47 |
| **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0690 | 0.0457 | -33.7% | 141.39 |
| **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-short-w256-float16] | 0.0690 | 0.0458 | -33.7% | 141.34 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-float16] | 0.0570 | 0.0457 | -19.8% | 141.43 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0568 | 0.0458 | -19.4% | 141.24 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-float16] | 0.3516 | 0.3064 | -12.8% | 336.71 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.3493 | 0.3047 | -12.8% | 338.62 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-bfloat16] | 0.0931 | 0.0818 | -12.2% | 158.15 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-float16] | 0.0929 | 0.0820 | -11.7% | 157.65 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-float16] | 0.6684 | 0.5904 | -11.7% | 349.52 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.6660 | 0.5887 | -11.6% | 350.53 |

## 🔵 Moved Since Previous Run

> Moves against the most recent reading. A row restored to its old level appears only here: returning is not a new 14-day record.

| Op | Config | Previous (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-b64-complex64] | 0.0152 | 0.0044 | -71.2% | 3.59 |
| **FFTC2CFwdOp** | test_fft_bench[fft-4k-c128-b64-complex128] | 0.0205 | 0.0072 | -64.7% | 2.17 |
| **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-q-lt-kv-float16] | 0.1231 | 0.0475 | -61.5% | 452.70 |
| **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-q-lt-kv-bfloat16] | 0.1213 | 0.0470 | -61.3% | 457.17 |
| **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-70b-q-lt-kv-float16] | 0.2059 | 0.0877 | -57.4% | 489.68 |
| **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-70b-q-lt-kv-bfloat16] | 0.2043 | 0.0874 | -57.2% | 491.83 |
| **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-unbatched-complex64] | 0.0081 | 0.0036 | -56.3% | 0.07 |
| **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-uniform-bfloat16] | 0.0628 | 0.0354 | -43.7% | 243.40 |
| **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-uniform-float16] | 0.0628 | 0.0356 | -43.4% | 241.87 |
| **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-70b-long-w1024-bfloat16] | 1.0286 | 0.5885 | -42.8% | 350.63 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-bfloat16] | 1.0275 | 0.5887 | -42.7% | 350.53 |
| **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-70b-long-w1024-float16] | 1.0292 | 0.5903 | -42.6% | 349.58 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-float16] | 1.0291 | 0.5904 | -42.6% | 349.52 |
| **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.5280 | 0.3047 | -42.3% | 338.68 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.5270 | 0.3047 | -42.2% | 338.62 |
| **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-long-w1024-float16] | 0.5280 | 0.3058 | -42.1% | 337.40 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-float16] | 0.5277 | 0.3064 | -41.9% | 336.71 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-bfloat16] | 0.1252 | 0.0818 | -34.7% | 158.15 |
| **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-70b-short-w256-bfloat16] | 0.1254 | 0.0820 | -34.6% | 157.72 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-float16] | 0.1252 | 0.0820 | -34.5% | 157.65 |
| **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-70b-short-w256-float16] | 0.1253 | 0.0821 | -34.5% | 157.47 |
| **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-short-w256-float16] | 0.0692 | 0.0458 | -33.9% | 141.34 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0692 | 0.0458 | -33.8% | 141.24 |
| **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0691 | 0.0457 | -33.8% | 141.39 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-float16] | 0.0691 | 0.0457 | -33.8% | 141.43 |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 80%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-bfloat16] | 0.4535 | 0.1421 | 31.3% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-bfloat16] | 0.4559 | 0.1428 | 31.3% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-short-bfloat16] | 0.4083 | 0.1595 | 39.1% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-short-bfloat16] | 0.4144 | 0.1656 | 40.0% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-bfloat16] | 1.3098 | 0.5481 | 41.9% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-q-lt-kv-float16] | 0.1226 | 0.0539 | 43.9% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-q-lt-kv-bfloat16] | 0.1208 | 0.0535 | 44.3% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-bfloat16] | 1.2420 | 0.5892 | 47.4% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-70b-q-lt-kv-bfloat16] | 0.2042 | 0.0990 | 48.5% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-70b-q-lt-kv-float16] | 0.2052 | 0.0996 | 48.5% | fa3 |

<details>
<summary><strong>19 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p256-float16] | 0.1650 | 0.0814 | 49.3% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-bfloat16] | 1.1028 | 0.5507 | 49.9% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-405b-p256-float16] | 0.0538 | 0.0269 | 50.0% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-70b-p256-float16] | 0.0665 | 0.0368 | 55.4% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 1.0177 | 0.5780 | 56.8% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-float16] | 0.2428 | 0.1422 | 58.6% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-float16] | 0.2443 | 0.1433 | 58.7% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[throughput-8b-p64-float16] | 0.2475 | 0.1509 | 61.0% | flashinfer |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-float16] | 0.9016 | 0.5533 | 61.4% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-float16] | 0.8910 | 0.5530 | 62.1% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-uniform-float16] | 0.0628 | 0.0447 | 71.2% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-float16] | 0.8321 | 0.5926 | 71.2% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-uniform-bfloat16] | 0.0627 | 0.0447 | 71.3% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.8084 | 0.5824 | 72.0% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-softcap50-float16] | 0.1732 | 0.1256 | 72.5% | flashinfer |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-bfloat16] | 0.0943 | 0.0698 | 74.0% | fla |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-float16] | 0.1646 | 0.1256 | 76.3% | flashinfer |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-float16] | 0.0984 | 0.0752 | 76.4% | fla |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-bfloat16] | 0.3114 | 0.2476 | 79.5% | fla |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 28 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 878 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 2592 lines in `ops/`, 36.4% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 4006 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

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
| `kernels/attention/gqa_prefill_varlen_ws.py` | 10.2% |
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
