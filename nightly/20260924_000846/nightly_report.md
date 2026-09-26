# ❌ TileOPs Nightly Report

> **2026-09-23 19:01** &ensp;|&ensp; `252a1721` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Correctness** | ✅ &ensp; (514/514 tests across 85 ops) |
| **Benchmarked Ops** | 174 |
| **Benchmark Failures** | ❌ 1 &ensp;|&ensp; ⚠️ 3 skipped |
| **Regressions** (vs 14-day median) | ⚠️ 8 |
| **Baseline Alerts** (< 80%) | ⚠️ 57 |
| **History window** | 12 runs, 2026-09-09 to 2026-09-22 |
| **Roofline anomalies** | ⚠️ 2 |
| **Improvements** (vs 14-day best) | 🎉 10 |
| **Moved since previous run** | 🔵 18 |
| **Never-built kernels** | ⚠️ 24 files &ensp;·&ensp; `kernels/linear_attention/gated_deltanet/compute_w_u_bwd.py` at 0.0% |
| **Untested roofline math** | 876 lines in `perf/` **+28** &ensp;·&ensp; `perf/formulas.py` at 11.7% |
| **Untested op logic** | 2439 lines in `ops/` **+12** &ensp;·&ensp; 39.1% of branches taken **+0.1pp** |
| | <sub>coverage compared against the 2026-09-22 run; no figure means it held</sub> |

## ❌ Benchmark Failures

| Test | Error |
|:-----|:------|
| whole_file | benchmarks/ops/bench_deltanet.py: no test started for 900s at benchmarks/ops/bench_deltanet.py::test_deltanet_dense_pref... |

## ⚠️ Performance Regressions (vs 14-day median)

| Op | Config | Median (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.6660 | 1.0261 | +54.1% | 201.10 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-float16] | 0.6684 | 1.0287 | +53.9% | 200.61 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.3493 | 0.5282 | +51.2% | 195.33 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-float16] | 0.3516 | 0.5274 | +50.0% | 195.65 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-float16] | 0.0929 | 0.1256 | +35.1% | 103.01 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-bfloat16] | 0.0931 | 0.1254 | +34.7% | 103.12 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0568 | 0.0691 | +21.7% | 93.57 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-float16] | 0.0570 | 0.0693 | +21.5% | 93.35 |

## 🎉 Performance Improvements (vs 14-day best)

| Op | Config | Prev Best (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b4-dmem1024-d512-float16] | 0.0824 | 0.0095 | -88.5% | 0.89 |
| **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b8-dmem512-d256-bfloat16] | 0.0333 | 0.0064 | -80.7% | 0.66 |
| **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b1-dmem512-d256-float16] | 0.0328 | 0.0069 | -78.9% | 0.08 |
| **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-dt-bias-bfloat16] | 0.0124 | 0.0058 | -52.9% | 1.44 |
| **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-bfloat16] | 0.0121 | 0.0057 | -52.5% | 1.28 |
| **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-2p7b-b2-s32k-dt-bias-float16] | 0.0443 | 0.0236 | -46.6% | 1.77 |
| **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0042 | 0.0030 | -28.0% | 0.45 |
| **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-780m-b1-s4k-dt-bias-float16] | 0.0042 | 0.0030 | -28.0% | 0.52 |
| **FusedMoeSharedExpertFwdOp** | test_fused_moe_shared_expert_bench[deepseek-v3-t64-bfloat16] | 3.1336 | 2.5388 | -19.0% | 19.98 |
| **FusedMoeSharedExpertFwdOp** | test_fused_moe_shared_expert_bench[kimi-k2-t64-bfloat16] | 3.9394 | 3.2376 | -17.8% | 29.60 |

## 🔵 Moved Since Previous Run

> Moves against the most recent reading. A row restored to its old level appears only here: returning is not a new 14-day record.

| Op | Config | Previous (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b4-dmem1024-d512-float16] | 0.0826 | 0.0095 | -88.5% | 0.89 |
| **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b8-dmem512-d256-bfloat16] | 0.0335 | 0.0064 | -80.8% | 0.66 |
| **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b1-dmem512-d256-float16] | 0.0330 | 0.0069 | -78.9% | 0.08 |
| **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-dt-bias-bfloat16] | 0.0124 | 0.0058 | -53.0% | 1.44 |
| **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-bfloat16] | 0.0121 | 0.0057 | -52.6% | 1.28 |
| **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-2p7b-b2-s32k-dt-bias-float16] | 0.0443 | 0.0236 | -46.6% | 1.77 |
| **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0042 | 0.0030 | -28.0% | 0.45 |
| **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-780m-b1-s4k-dt-bias-float16] | 0.0042 | 0.0030 | -28.0% | 0.52 |
| **FusedMoeSharedExpertFwdOp** | test_fused_moe_shared_expert_bench[deepseek-v3-t64-bfloat16] | 3.1336 | 2.5388 | -19.0% | 19.98 |
| **FusedMoeSharedExpertFwdOp** | test_fused_moe_shared_expert_bench[kimi-k2-t64-bfloat16] | 3.9394 | 3.2376 | -17.8% | 29.60 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0569 | 0.0691 | +21.5% | 93.57 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-float16] | 0.0570 | 0.0693 | +21.5% | 93.35 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-bfloat16] | 0.0931 | 0.1254 | +34.7% | 103.12 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-float16] | 0.0929 | 0.1256 | +35.1% | 103.01 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-float16] | 0.3516 | 0.5274 | +50.0% | 195.65 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.3493 | 0.5282 | +51.2% | 195.33 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.6691 | 1.0261 | +53.4% | 201.10 |
| **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-float16] | 0.6684 | 1.0287 | +53.9% | 200.61 |

## ⚠️ Roofline Model Anomalies

> A FAIL row implies a rate above the hardware's theoretical ceiling: its (flops, bytes) formula or declared roof is wrong, and its SOL reading cannot be trusted. A WARN row exceeds the calibrated ceiling; recheck the formula or the calibration.

| Level | Op | Config | Signal |
|:------|:---|:-------|:-------|
| WARN | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-attn-proj-float16] | 107% of the calibrated ceiling |
| WARN | **GemmFwdOp** | test_gemm_bench[k-dominant-7168x16384-bfloat16] | 108% of the calibrated ceiling |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 80%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-bfloat16] | 0.4537 | 0.1420 | 31.3% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-bfloat16] | 0.4559 | 0.1428 | 31.3% | fa3 |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-b64-complex64] | 0.0152 | 0.0056 | 37.0% | torch-cufft |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-short-bfloat16] | 0.4084 | 0.1593 | 39.0% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-short-bfloat16] | 0.4143 | 0.1656 | 40.0% | fa3 |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c128-b64-complex128] | 0.0205 | 0.0085 | 41.3% | torch-cufft |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-bfloat16] | 1.3108 | 0.5479 | 41.8% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-q-lt-kv-float16] | 0.1228 | 0.0538 | 43.8% | fa3 |
| 🔴 | **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-q-lt-kv-float16] | 0.1222 | 0.0535 | 43.8% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-q-lt-kv-bfloat16] | 0.1216 | 0.0533 | 43.9% | fa3 |

<details>
<summary><strong>47 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-q-lt-kv-bfloat16] | 0.1215 | 0.0534 | 44.0% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-bfloat16] | 1.2419 | 0.5900 | 47.5% | fa3 |
| 🔴 | **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-70b-q-lt-kv-bfloat16] | 0.2052 | 0.0986 | 48.0% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-70b-q-lt-kv-bfloat16] | 0.2042 | 0.0983 | 48.1% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-70b-q-lt-kv-float16] | 0.2065 | 0.0999 | 48.4% | fa3 |
| 🔴 | **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-70b-q-lt-kv-float16] | 0.2055 | 0.0995 | 48.4% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p256-float16] | 0.1650 | 0.0814 | 49.3% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-bfloat16] | 1.1026 | 0.5500 | 49.9% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-405b-p256-float16] | 0.0537 | 0.0269 | 50.1% | fa3 |
| 🔴 | **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-70b-long-w1024-bfloat16] | 1.0272 | 0.5278 | 51.4% | fa3 |
| 🔴 | **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.5273 | 0.2711 | 51.4% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.5282 | 0.2729 | 51.7% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-float16] | 1.0287 | 0.5315 | 51.7% | fa3 |
| 🔴 | **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-70b-long-w1024-float16] | 1.0276 | 0.5311 | 51.7% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-bfloat16] | 1.0261 | 0.5305 | 51.7% | fa3 |
| 🔴 | **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-long-w1024-float16] | 0.5272 | 0.2730 | 51.8% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-float16] | 0.5274 | 0.2738 | 51.9% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-70b-p256-float16] | 0.0665 | 0.0369 | 55.5% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 1.0183 | 0.5784 | 56.8% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-float16] | 0.2433 | 0.1423 | 58.5% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-float16] | 0.2441 | 0.1433 | 58.7% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[throughput-8b-p64-float16] | 0.2477 | 0.1511 | 61.0% | flashinfer |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-float16] | 0.9017 | 0.5516 | 61.2% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-float16] | 0.8929 | 0.5544 | 62.1% | fa3 |
| 🔴 | **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-70b-short-w256-bfloat16] | 0.1257 | 0.0832 | 66.2% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-bfloat16] | 0.1254 | 0.0832 | 66.4% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-float16] | 0.1256 | 0.0835 | 66.5% | fa3 |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-unbatched-complex64] | 0.0081 | 0.0054 | 66.5% | torch-cufft |
| 🔴 | **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-70b-short-w256-float16] | 0.1254 | 0.0836 | 66.7% | fa3 |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-bfloat16] | 0.0969 | 0.0658 | 67.8% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0691 | 0.0471 | 68.2% | fa3 |
| 🔴 | **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0690 | 0.0470 | 68.2% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-float16] | 0.0693 | 0.0473 | 68.3% | fa3 |
| 🔴 | **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-short-w256-float16] | 0.0690 | 0.0471 | 68.3% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-uniform-float16] | 0.0631 | 0.0449 | 71.2% | fa3 |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-float16] | 0.0984 | 0.0703 | 71.4% | fla |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-float16] | 0.8317 | 0.5943 | 71.5% | fa3 |
| 🔴 | **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-uniform-float16] | 0.0629 | 0.0450 | 71.5% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-uniform-bfloat16] | 0.0628 | 0.0449 | 71.5% | fa3 |
| 🔴 | **GroupedQueryAttentionVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-uniform-bfloat16] | 0.0625 | 0.0448 | 71.7% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.8088 | 0.5816 | 71.9% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-softcap50-float16] | 0.1732 | 0.1259 | 72.7% | flashinfer |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-float16] | 0.6183 | 0.4652 | 75.2% | fla |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-bfloat16] | 0.3118 | 0.2359 | 75.6% | fla |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-float16] | 0.1646 | 0.1256 | 76.3% | flashinfer |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-bfloat16] | 0.6105 | 0.4770 | 78.1% | fla |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-float16] | 0.3131 | 0.2477 | 79.1% | fla |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 24 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 876 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 2439 lines in `ops/`, 39.1% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 3598 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

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
| `kernels/attention/gqa_dense.py` | 10.8% |
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
| `kernels/attention/deepseek_nsa_cmp_fwd.py` | 18.1% |
| `kernels/linear_attention/gated_deltanet/prefill/dense.py` | 20.0% |
| `kernels/linear_attention/gated_deltanet/gated_deltanet_fwd.py` | 21.7% |
| `kernels/linear_attention/deltanet/dense_prefill.py` | 22.4% |
| `kernels/linear_attention/gated_deltanet/prefill/common.py` | 23.0% |

<details>
<summary>Untested pure Python, worst 15 files</summary>

| File | Uncovered | Executed |
| --- | --- | --- |
| `perf/formulas.py` | 834 | 11.7% |
| `ops/attention/gqa.py` | 552 | 32.1% |
| `ops/op_base.py` | 199 | 50.4% |
| `ops/linear_attention/gated_deltanet.py` | 118 | 16.3% |
| `ops/pool.py` | 87 | 84.8% |
| `ops/linear_attention/deltanet_inference.py` | 84 | 20.0% |
| `ops/mamba/mamba2_fwd.py` | 84 | 20.0% |
| `ops/rope.py` | 83 | 69.5% |
| `ops/convolution.py` | 82 | 79.7% |
| `ops/elementwise/_base.py` | 79 | 75.0% |
| `ops/linear_attention/deltanet.py` | 71 | 64.0% |
| `ops/moe/staged.py` | 70 | 74.7% |
| `ops/reduction/reduce.py` | 62 | 69.5% |
| `trace/ui.py` | 62 | 24.4% |
| `ops/_roofline_codegen.py` | 60 | 78.1% |

</details>

Per-line detail is in the `htmlcov/` directory of this run's `tileops_op_test` artifact.
