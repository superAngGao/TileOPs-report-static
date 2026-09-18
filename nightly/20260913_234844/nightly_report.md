# ❌ TileOPs Nightly Report

> **2026-09-13 18:40** &ensp;|&ensp; `15e4feea` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Correctness** | ✅ &ensp; (517/517 tests across 87 ops) |
| **Benchmarked Ops** | 182 |
| **Benchmark Failures** | ✅ None &ensp;|&ensp; ⚠️ 3 skipped |
| **Regressions** (vs 14-day median) | ✅ None |
| **Baseline Alerts** (< 80%) | ⚠️ 91 |
| **Roofline anomalies** | ❌ 1 impossible |
| **Never-built kernels** | ⚠️ 13 files &ensp;·&ensp; `kernels/attention/deepseek_mla_decode.py` at 5.8% |
| **Untested roofline math** | 827 lines in `perf/` &ensp;·&ensp; `perf/formulas.py` at 11.5% |
| **Untested op logic** | 2651 lines in `ops/` &ensp;·&ensp; 39.0% of branches taken |
| | <sub>coverage compared against the 2026-09-12 run; no figure means it held</sub> |

## ⚠️ Roofline Model Anomalies

> A FAIL row implies a rate above the hardware's theoretical ceiling: its (flops, bytes) formula or declared roof is wrong, and its SOL reading cannot be trusted. A WARN row exceeds the calibrated ceiling; recheck the formula or the calibration.

| Level | Op | Config | Signal |
|:------|:---|:-------|:-------|
| FAIL | **FusedMoeFwdOp** | test_fused_moe_fwd_bench[kimi-k2-decode-bfloat16] | bytes/s over HBM theoretical |
| WARN | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-attn-proj-float16] | 108% of the calibrated ceiling |
| WARN | **GemmFwdOp** | test_gemm_bench[k-dominant-7168x16384-bfloat16] | 109% of the calibrated ceiling |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 80%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-bfloat16] | 0.4564 | 0.1429 | 31.3% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-bfloat16] | 0.4536 | 0.1422 | 31.4% | fa3 |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b4-dmem1024-d512-float16] | 0.0827 | 0.0260 | 31.4% | torch-compile |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-b64-complex64] | 0.0152 | 0.0056 | 37.0% | torch-cufft |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[mha-decode-b32-pv-per-tensor-float8_e4m3fn] | 0.0646 | 0.0249 | 38.6% | flashinfer-bmm-fp8 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-short-bfloat16] | 0.4083 | 0.1595 | 39.1% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-short-bfloat16] | 0.4141 | 0.1654 | 40.0% | fa3 |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b1-dmem512-d256-float16] | 0.0329 | 0.0132 | 40.0% | torch-compile |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c128-b64-complex128] | 0.0205 | 0.0085 | 41.4% | torch-cufft |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-bfloat16] | 1.3099 | 0.5479 | 41.8% | fa3 |

<details>
<summary><strong>81 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[mha-decode-b64-qk-per-tensor-float8_e4m3fn] | 0.1154 | 0.0494 | 42.8% | flashinfer-bmm-fp8 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-q-lt-kv-bfloat16] | 0.1125 | 0.0534 | 47.5% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-bfloat16] | 1.2419 | 0.5896 | 47.5% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-q-lt-kv-float16] | 0.1130 | 0.0537 | 47.5% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p256-float16] | 0.1654 | 0.0813 | 49.2% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-405b-p256-float16] | 0.0535 | 0.0265 | 49.5% | fa3 |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-long-k-pressure-float16] | 0.2842 | 0.1417 | 49.9% | marlin-fp16 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-bfloat16] | 1.1040 | 0.5506 | 49.9% | fa3 |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-small-bfloat16] | 0.0394 | 0.0197 | 49.9% | torch-compile |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-2p7b-b2-s32k-dt-bias-float16] | 0.0444 | 0.0223 | 50.4% | mamba |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-70b-q-lt-kv-float16] | 0.1981 | 0.1000 | 50.5% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-70b-q-lt-kv-bfloat16] | 0.1960 | 0.0994 | 50.7% | fa3 |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-dt-bias-bfloat16] | 0.0124 | 0.0064 | 51.7% | mamba |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[compile-smoke-rect-128x256x256-float16] | 0.0059 | 0.0031 | 52.2% | torch-dequantized-matmul |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-bfloat16] | 0.0121 | 0.0065 | 53.3% | mamba |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-70b-p256-float16] | 0.0672 | 0.0367 | 54.6% | fa3 |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-non-power2-low-cta-float16] | 0.0743 | 0.0408 | 54.8% | marlin-fp32 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 1.0171 | 0.5781 | 56.8% | fa3 |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-medium-bfloat16] | 0.0544 | 0.0313 | 57.5% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-float16] | 0.2443 | 0.1431 | 58.6% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-float16] | 0.2428 | 0.1423 | 58.6% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[throughput-8b-p64-float16] | 0.2491 | 0.1506 | 60.5% | flashinfer |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-float16] | 0.9016 | 0.5518 | 61.2% | fa3 |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-bfloat16] | 0.6379 | 0.3904 | 61.2% | fla |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-float16] | 0.8921 | 0.5538 | 62.1% | fa3 |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-float16] | 0.6369 | 0.3955 | 62.1% | fla |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-hbm-streaming-threshold-float16] | 0.0609 | 0.0380 | 62.5% | marlin-fp32 |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-bfloat16] | 1.4671 | 0.9214 | 62.8% | fla |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b8-dmem512-d256-bfloat16] | 0.0333 | 0.0211 | 63.2% | torch-compile |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[compile-smoke-square-64x64x128-float16] | 0.0042 | 0.0027 | 64.0% | torch-dequantized-matmul |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-bfloat16] | 0.3881 | 0.2487 | 64.1% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-float16] | 1.4293 | 0.9252 | 64.7% | fla |
| 🔴 | **GatedDeltaNetAutogradOp** | test_gated_deltanet_vs_fla_autograd[gdn-autograd-b2-s8k-h4-d64-bfloat16] | 0.3165 | 0.2049 | 64.7% | fla |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-bfloat16] | 0.3163 | 0.2048 | 64.8% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-bfloat16] | 0.7506 | 0.4862 | 64.8% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-bfloat16] | 0.2050 | 0.1338 | 65.2% | fla |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-l2-resident-ish-float16] | 0.0330 | 0.0217 | 65.7% | marlin-fp32 |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-float16] | 0.3806 | 0.2505 | 65.8% | fla |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-float16] | 0.3140 | 0.2083 | 66.3% | fla |
| 🔴 | **GatedDeltaNetAutogradOp** | test_gated_deltanet_vs_fla_autograd[gdn-autograd-b2-s8k-h4-d64-float16] | 0.3139 | 0.2082 | 66.3% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-float16] | 0.2013 | 0.1340 | 66.6% | fla |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-unbatched-complex64] | 0.0081 | 0.0054 | 66.8% | torch-compile |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-float16] | 0.7246 | 0.4896 | 67.6% | fla |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-bfloat16] | 0.0968 | 0.0665 | 68.7% | fla |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[moe-prefill-b128-per-tensor-float8_e4m3fn] | 0.9009 | 0.6259 | 69.5% | flashinfer-bmm-fp8 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-float16] | 0.8333 | 0.5931 | 71.2% | fa3 |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-float16] | 0.0987 | 0.0704 | 71.4% | fla |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.8093 | 0.5812 | 71.8% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-softcap50-float16] | 0.1740 | 0.1252 | 71.9% | flashinfer |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0569 | 0.0410 | 72.0% | flashinfer |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-float16] | 0.0571 | 0.0414 | 72.6% | flashinfer |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b4-4k-bfloat16] | 1.0524 | 0.7713 | 73.3% | torch-cublas |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-2k-bfloat16] | 0.2783 | 0.2046 | 73.5% | torch-cublas |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-float16] | 0.1487 | 0.1095 | 73.7% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-bfloat16] | 0.0932 | 0.0688 | 73.8% | flashinfer |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-uniform-float16] | 0.0607 | 0.0449 | 74.0% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-uniform-bfloat16] | 0.0607 | 0.0449 | 74.1% | fa3 |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-2k-float16] | 0.2805 | 0.2089 | 74.5% | torch-cublas |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-bfloat16] | 0.1444 | 0.1076 | 74.5% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-float16] | 0.0931 | 0.0694 | 74.6% | flashinfer |
| 🔴 | **BmmFwdOp** | test_bmm_bench[moe-prefill-b128-bfloat16] | 0.2896 | 0.2174 | 75.1% | torch-cublas |
| 🔴 | **GroupedQueryAttentionDenseFwdOp** | test_gqa_dense_decode_bench[decode-llama-8b-4k-bfloat16] | 0.2031 | 0.1528 | 75.2% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-float16] | 0.1658 | 0.1252 | 75.6% | flashinfer |
| 🔴 | **GroupedQueryAttentionDenseFwdOp** | test_gqa_dense_decode_bench[decode-llama-8b-4k-float16] | 0.2030 | 0.1539 | 75.8% | fa3 |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-1k-float16] | 0.0406 | 0.0310 | 76.5% | torch-cublas |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-1k-bfloat16] | 0.0406 | 0.0312 | 76.8% | torch-cublas |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.3497 | 0.2696 | 77.1% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-float16] | 0.3522 | 0.2719 | 77.2% | fa3 |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-float16] | 0.6173 | 0.4772 | 77.3% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-float16] | 0.6694 | 0.5190 | 77.5% | flashinfer |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-bfloat16] | 0.0866 | 0.0673 | 77.7% | fla |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-bfloat16] | 0.3114 | 0.2420 | 77.7% | fla |
| 🔴 | **GatedDeltaNetAutogradOp** | test_gated_deltanet_vs_fla_autograd[gdn-autograd-b2-s2k-h4-d64-bfloat16] | 0.0866 | 0.0673 | 77.8% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.6664 | 0.5184 | 77.8% | flashinfer |
| 🔴 | **GatedDeltaNetPrefillBHTDFwdOp** | test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-float16] | 0.2512 | 0.1964 | 78.2% | fla |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0043 | 0.0033 | 78.2% | mamba |
| 🔴 | **GatedDeltaNetPrefillBHTDFwdOp** | test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-bfloat16] | 0.2526 | 0.1984 | 78.5% | fla |
| 🔴 | **GatedDeltaNetAutogradOp** | test_gated_deltanet_vs_fla_autograd[gdn-autograd-b2-s2k-h4-d64-float16] | 0.0866 | 0.0681 | 78.7% | fla |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-float16] | 0.0866 | 0.0681 | 78.7% | fla |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-large-bfloat16] | 0.0716 | 0.0567 | 79.2% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-bfloat16] | 0.6115 | 0.4865 | 79.6% | fla |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 13 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 827 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 2651 lines in `ops/`, 39.0% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 3757 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

### Never-built kernels

| File | Executed |
| --- | --- |
| `kernels/attention/deepseek_mla_decode.py` | 5.8% |
| `kernels/attention/gqa_fwd_ws.py` | 6.4% |
| `kernels/attention/gqa_fwd_fp8.py` | 7.0% |
| `kernels/attention/gqa_dense.py` | 9.8% |
| `kernels/attention/gqa_fwd.py` | 11.2% |
| `kernels/attention/mha_decode_paged.py` | 11.6% |
| `kernels/attention/gqa_decode_bs1_common.py` | 12.4% |
| `kernels/attention/gqa_decode.py` | 13.2% |
| `kernels/attention/mha_decode.py` | 13.2% |
| `kernels/attention/gqa_decode_bs1.py` | 13.4% |
| `kernels/grouped_gemm/grouped_gemm.py` | 15.7% |
| `kernels/attention/gqa_prefill_varlen_fwd.py` | 18.7% |
| `kernels/attention/deepseek_nsa_cmp_fwd.py` | 19.6% |

<details>
<summary>Untested pure Python, worst 15 files</summary>

| File | Uncovered | Executed |
| --- | --- | --- |
| `perf/formulas.py` | 785 | 11.5% |
| `ops/attention/gqa.py` | 673 | 23.9% |
| `ops/pool.py` | 154 | 76.6% |
| `ops/convolution.py` | 120 | 74.1% |
| `ops/op_base.py` | 116 | 57.2% |
| `ops/linear_attention/gated_deltanet.py` | 114 | 72.9% |
| `ops/moe/staged.py` | 106 | 68.5% |
| `ops/reduction/reduce.py` | 100 | 58.5% |
| `ops/elementwise/_base.py` | 88 | 76.7% |
| `ops/mamba/mamba2_fwd.py` | 86 | 20.4% |
| `ops/rope.py` | 85 | 70.4% |
| `ops/_roofline_codegen.py` | 84 | 68.1% |
| `ops/linear_attention/deltanet.py` | 65 | 63.3% |
| `trace/ui.py` | 62 | 24.4% |
| `ops/moe/shared_fused_moe.py` | 58 | 20.5% |

</details>

Per-line detail is in the `htmlcov/` directory of this run's `tileops_op_test` artifact.
