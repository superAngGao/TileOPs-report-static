# ❌ TileOPs Nightly Report

> **2026-09-08 18:43** &ensp;|&ensp; `e0edbb12` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Correctness** | ✅ &ensp; (512/512 tests across 87 ops) |
| **Benchmarked Ops** | 182 |
| **Benchmark Failures** | ✅ None &ensp;|&ensp; ⚠️ 3 skipped |
| **Regressions** (vs 14-day median) | ⚠️ 1 |
| **Baseline Alerts** (< 80%) | ⚠️ 109 |
| **Roofline anomalies** | ❌ 1 impossible |
| **Improvements** (vs 14-day best) | 🎉 14 |
| **Moved since previous run** | 🔵 14 |
| **Never-built kernels** | ⚠️ 12 files **+1** &ensp;·&ensp; `kernels/attention/deepseek_mla_decode.py` at 5.8% |
| **Untested roofline math** | 826 lines in `perf/` **+29** &ensp;·&ensp; `perf/formulas.py` at 11.5% |
| **Untested op logic** | 2735 lines in `ops/` **+46** &ensp;·&ensp; 38.0% of branches taken **−0.2pp** |
| | <sub>coverage compared against the 2026-09-06 run; no figure means it held</sub> |

## ⚠️ Performance Regressions (vs 14-day median)

| Op | Config | Median (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **FusedMoEExpertsNopadPersistent3WGFwdOp** | test_moe_experts_nopad_bench[qwen3-235b-prefill-float16] | 4.1829 | 6.1298 | +46.5% | 470.85 |

## 🎉 Performance Improvements (vs 14-day best)

| Op | Config | Prev Best (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **MeanPoolingFwdOp** | test_mean_pooling_bench[ragged-tail-float16] | 0.0793 | 0.0093 | -88.3% | 0.91 |
| **MeanPoolingFwdOp** | test_mean_pooling_bench[ragged-batched-float16] | 0.1260 | 0.0243 | -80.7% | 1.40 |
| **MeanPoolingFwdOp** | test_mean_pooling_bench[ragged-even-float16] | 0.1948 | 0.0411 | -78.9% | 1.66 |
| **MeanPoolingFwdOp** | test_mean_pooling_bench[uniform-8k-float16] | 0.1350 | 0.0393 | -70.9% | 1.74 |
| **MeanPoolingFwdOp** | test_mean_pooling_bench[uniform-batched-float16] | 0.0700 | 0.0225 | -67.9% | 1.51 |
| **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[spp-6x6-float16] | 0.0081 | 0.0036 | -55.9% | 0.26 |
| **AdaptiveMaxPool2dFwdOp** | test_adaptive_max_pool2d_bench[nondiv-7x7-bfloat16] | 0.0065 | 0.0033 | -48.8% | 0.15 |
| **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[nondiv-7x7-bfloat16] | 0.0066 | 0.0035 | -47.3% | 0.14 |
| **AdaptiveMaxPool2dFwdOp** | test_adaptive_max_pool2d_bench[spp-6x6-float16] | 0.0060 | 0.0035 | -42.2% | 0.27 |
| **FusedAddRMSNormFwdOp** | test_fused_add_rms_norm_bench[llama-70b-decode-bfloat16] | 0.0030 | 0.0021 | -31.6% | 0.02 |
| **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[ecg-cnn-dilated-bfloat16] | 0.0156 | 0.0117 | -25.0% | 0.90 |
| **AvgPool1dFwdOp** | test_avg_pool1d_bench[long-temporal-float16] | 0.0180 | 0.0149 | -17.6% | 1.38 |
| **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[global-1x1-float16] | 0.0033 | 0.0028 | -15.4% | 0.29 |
| **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[textcnn-global-float16] | 0.0050 | 0.0043 | -14.7% | 0.49 |

## 🔵 Moved Since Previous Run

> Moves against the most recent reading. A row restored to its old level appears only here: returning is not a new 14-day record.

| Op | Config | Previous (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **MeanPoolingFwdOp** | test_mean_pooling_bench[ragged-tail-float16] | 0.0794 | 0.0093 | -88.3% | 0.91 |
| **MeanPoolingFwdOp** | test_mean_pooling_bench[ragged-batched-float16] | 0.1262 | 0.0243 | -80.7% | 1.40 |
| **MeanPoolingFwdOp** | test_mean_pooling_bench[ragged-even-float16] | 0.1948 | 0.0411 | -78.9% | 1.66 |
| **MeanPoolingFwdOp** | test_mean_pooling_bench[uniform-8k-float16] | 0.1352 | 0.0393 | -70.9% | 1.74 |
| **MeanPoolingFwdOp** | test_mean_pooling_bench[uniform-batched-float16] | 0.0701 | 0.0225 | -67.9% | 1.51 |
| **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[spp-6x6-float16] | 0.0081 | 0.0036 | -55.9% | 0.26 |
| **AdaptiveMaxPool2dFwdOp** | test_adaptive_max_pool2d_bench[nondiv-7x7-bfloat16] | 0.0065 | 0.0033 | -49.0% | 0.15 |
| **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[nondiv-7x7-bfloat16] | 0.0066 | 0.0035 | -47.3% | 0.14 |
| **AdaptiveMaxPool2dFwdOp** | test_adaptive_max_pool2d_bench[spp-6x6-float16] | 0.0060 | 0.0035 | -42.6% | 0.27 |
| **FusedAddRMSNormFwdOp** | test_fused_add_rms_norm_bench[llama-70b-decode-bfloat16] | 0.0030 | 0.0021 | -31.6% | 0.02 |
| **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[ecg-cnn-dilated-bfloat16] | 0.0157 | 0.0117 | -25.5% | 0.90 |
| **AvgPool1dFwdOp** | test_avg_pool1d_bench[long-temporal-float16] | 0.0180 | 0.0149 | -17.6% | 1.38 |
| **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[global-1x1-float16] | 0.0033 | 0.0028 | -15.4% | 0.29 |
| **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[textcnn-global-float16] | 0.0050 | 0.0043 | -14.7% | 0.49 |

## ⚠️ Roofline Model Anomalies

> A FAIL row implies a rate above the hardware's theoretical ceiling: its (flops, bytes) formula or declared roof is wrong, and its SOL reading cannot be trusted. A WARN row exceeds the calibrated ceiling; recheck the formula or the calibration.

| Level | Op | Config | Signal |
|:------|:---|:-------|:-------|
| FAIL | **FusedMoeFwdOp** | test_fused_moe_fwd_bench[kimi-k2-decode-bfloat16] | bytes/s over HBM theoretical |
| WARN | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-attn-proj-float16] | 108% of the calibrated ceiling |
| WARN | **GemmFwdOp** | test_gemm_bench[k-dominant-7168x16384-bfloat16] | 108% of the calibrated ceiling |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 80%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-gate-up-block128-float8_e4m3fn] | 0.1482 | 0.0129 | 8.7% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[gemv-down-m1-block128-float8_e4m3fn] | 0.0446 | 0.0077 | 17.3% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[k-dominant-7168x16384-block128-float8_e4m3fn] | 3.5884 | 0.7753 | 21.6% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-down-block128-float8_e4m3fn] | 0.0377 | 0.0092 | 24.4% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-attn-proj-block128-float8_e4m3fn] | 0.7679 | 0.2155 | 28.1% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b4-dmem1024-d512-float16] | 0.0826 | 0.0256 | 31.0% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-bfloat16] | 0.4537 | 0.1419 | 31.3% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-bfloat16] | 0.4559 | 0.1427 | 31.3% | fa3 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[small-batch-down-m8-per-tensor-float8_e4m3fn] | 0.0265 | 0.0084 | 31.5% | deepgemm |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-down-block128-float8_e4m3fn] | 0.4455 | 0.1436 | 32.2% | flashinfer-fp8-blockscale-sm90 |

<details>
<summary><strong>99 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-gate-up-block128-float8_e4m3fn] | 0.3860 | 0.1399 | 36.3% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-b64-complex64] | 0.0152 | 0.0057 | 37.3% | torch-cufft |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[wide-n-24576-block128-float8_e4m3fn] | 1.0275 | 0.3853 | 37.5% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[mha-decode-b32-pv-per-tensor-float8_e4m3fn] | 0.0646 | 0.0249 | 38.5% | flashinfer-bmm-fp8 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-short-bfloat16] | 0.4084 | 0.1592 | 39.0% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-short-bfloat16] | 0.4143 | 0.1654 | 39.9% | fa3 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[gemv-down-m1-per-tensor-float8_e4m3fn] | 0.0259 | 0.0103 | 40.0% | deepgemm |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b1-dmem512-d256-float16] | 0.0329 | 0.0132 | 40.0% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-down-per-tensor-float8_e4m3fn] | 0.0253 | 0.0104 | 41.0% | deepgemm |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c128-b64-complex128] | 0.0205 | 0.0085 | 41.4% | torch-cufft |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-bfloat16] | 1.3099 | 0.5482 | 41.9% | fa3 |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[mha-decode-b64-qk-per-tensor-float8_e4m3fn] | 0.1154 | 0.0496 | 43.0% | flashinfer-bmm-fp8 |
| 🔴 | **GroupedGemmFwdOp** | test_grouped_gemm_bench[tn-batch16-m4096-n4096-k4096-float16] | 0.7847 | 0.3526 | 44.9% | torch |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-q-lt-kv-bfloat16] | 0.1131 | 0.0534 | 47.2% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-bfloat16] | 1.2416 | 0.5896 | 47.5% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-q-lt-kv-float16] | 0.1126 | 0.0540 | 47.9% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p256-float16] | 0.1653 | 0.0812 | 49.1% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-405b-p256-float16] | 0.0536 | 0.0266 | 49.5% | fa3 |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-small-bfloat16] | 0.0395 | 0.0196 | 49.8% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-bfloat16] | 1.1026 | 0.5498 | 49.9% | fa3 |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-long-k-pressure-float16] | 0.2847 | 0.1423 | 50.0% | marlin-fp16 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-down-per-tensor-float8_e4m3fn] | 0.2107 | 0.1058 | 50.2% | deepgemm |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-2p7b-b2-s32k-dt-bias-float16] | 0.0443 | 0.0223 | 50.3% | mamba |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-70b-q-lt-kv-bfloat16] | 0.1965 | 0.0990 | 50.4% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-70b-q-lt-kv-float16] | 0.1970 | 0.0996 | 50.5% | fa3 |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-dt-bias-bfloat16] | 0.0124 | 0.0064 | 51.5% | mamba |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[compile-smoke-rect-128x256x256-float16] | 0.0059 | 0.0031 | 52.2% | torch-dequantized-matmul |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-bfloat16] | 0.0121 | 0.0064 | 53.0% | mamba |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-non-power2-low-cta-float16] | 0.0746 | 0.0406 | 54.5% | marlin-fp16 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-70b-p256-float16] | 0.0669 | 0.0365 | 54.5% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 1.0177 | 0.5776 | 56.8% | fa3 |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-medium-bfloat16] | 0.0544 | 0.0314 | 57.6% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-float16] | 0.2445 | 0.1431 | 58.5% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-float16] | 0.2429 | 0.1422 | 58.6% | fa3 |
| 🔴 | **TopkSelectorFwdOp** | test_topk_selector_bench[topk1024-s32k-kv64k-float32] | 15.6284 | 9.2769 | 59.4% | flashinfer |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[throughput-8b-p64-float16] | 0.2491 | 0.1506 | 60.5% | flashinfer |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-float16] | 0.9019 | 0.5513 | 61.1% | fa3 |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-bfloat16] | 0.6377 | 0.3904 | 61.2% | fla |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-float16] | 0.8908 | 0.5544 | 62.2% | fa3 |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-float16] | 0.6351 | 0.3955 | 62.3% | fla |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-hbm-streaming-threshold-float16] | 0.0607 | 0.0379 | 62.4% | marlin-fp16 |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[compile-smoke-square-64x64x128-float16] | 0.0042 | 0.0027 | 62.9% | torch-dequantized-matmul |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-bfloat16] | 1.4648 | 0.9221 | 62.9% | fla |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b8-dmem512-d256-bfloat16] | 0.0335 | 0.0213 | 63.6% | torch-compile |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-bfloat16] | 0.3881 | 0.2491 | 64.2% | fla |
| 🔴 | **GatedDeltaNetAutogradOp** | test_gated_deltanet_vs_fla_autograd[gdn-autograd-b2-s8k-h4-d64-bfloat16] | 0.3161 | 0.2048 | 64.8% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-bfloat16] | 0.7500 | 0.4861 | 64.8% | fla |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-bfloat16] | 0.3159 | 0.2049 | 64.9% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-float16] | 1.4176 | 0.9241 | 65.2% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-bfloat16] | 0.2051 | 0.1337 | 65.2% | fla |
| 🔴 | **TopkSelectorFwdOp** | test_topk_selector_bench[topk2048-s32k-kv64k-float32] | 16.2426 | 10.6700 | 65.7% | flashinfer |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-float16] | 0.3808 | 0.2508 | 65.9% | fla |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-l2-resident-ish-float16] | 0.0328 | 0.0217 | 66.1% | marlin-fp32 |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-float16] | 0.3144 | 0.2082 | 66.2% | fla |
| 🔴 | **GatedDeltaNetAutogradOp** | test_gated_deltanet_vs_fla_autograd[gdn-autograd-b2-s8k-h4-d64-float16] | 0.3142 | 0.2083 | 66.3% | fla |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-unbatched-complex64] | 0.0081 | 0.0054 | 66.5% | torch-cufft |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-float16] | 0.2013 | 0.1341 | 66.6% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-float16] | 0.7247 | 0.4899 | 67.6% | fla |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-bfloat16] | 0.0972 | 0.0666 | 68.5% | fla |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[moe-prefill-b128-per-tensor-float8_e4m3fn] | 0.9006 | 0.6240 | 69.3% | flashinfer-bmm-fp8 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-float16] | 0.8333 | 0.5926 | 71.1% | fa3 |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-float16] | 0.0984 | 0.0703 | 71.4% | fla |
| 🔴 | **SharedFusedMoE** | test_shared_fused_moe_bench[1-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 0.5968 | 0.4265 | 71.5% | vllm |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.8091 | 0.5810 | 71.8% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-softcap50-float16] | 0.1742 | 0.1252 | 71.9% | flashinfer |
| 🔴 | **GroupedQueryAttentionDenseFwdOp** | test_gqa_dense_decode_bench[decode-llama-8b-4k-bfloat16] | 0.2108 | 0.1526 | 72.4% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-float16] | 0.0569 | 0.0413 | 72.5% | flashinfer |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0567 | 0.0413 | 72.8% | flashinfer |
| 🔴 | **GroupedQueryAttentionDenseFwdOp** | test_gqa_dense_decode_bench[decode-llama-8b-4k-float16] | 0.2104 | 0.1533 | 72.9% | fa3 |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b4-4k-bfloat16] | 1.0517 | 0.7686 | 73.1% | torch-cublas |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-2k-bfloat16] | 0.2796 | 0.2059 | 73.7% | torch-cublas |
| 🔴 | **FusedTopKOp** | test_fused_topk_bench[kimi-k2-t512-bias-bfloat16] | 0.0148 | 0.0109 | 73.7% | vllm |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-float16] | 0.1486 | 0.1096 | 73.7% | fla |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-uniform-float16] | 0.0610 | 0.0450 | 73.8% | fa3 |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-2k-float16] | 0.2814 | 0.2078 | 73.8% | torch-cublas |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-uniform-bfloat16] | 0.0606 | 0.0448 | 73.9% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-float16] | 0.0932 | 0.0690 | 74.0% | flashinfer |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-bfloat16] | 0.1444 | 0.1076 | 74.5% | fla |
| 🔴 | **BmmFwdOp** | test_bmm_bench[moe-prefill-b128-bfloat16] | 0.2905 | 0.2166 | 74.6% | torch-cublas |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-bfloat16] | 0.0928 | 0.0692 | 74.7% | flashinfer |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-float16] | 0.1655 | 0.1252 | 75.7% | flashinfer |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-1k-bfloat16] | 0.0408 | 0.0311 | 76.4% | torch-cublas |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-1k-float16] | 0.0406 | 0.0310 | 76.4% | torch-cublas |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-float16] | 0.6182 | 0.4763 | 77.0% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.3497 | 0.2698 | 77.1% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-float16] | 0.3517 | 0.2714 | 77.2% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.6661 | 0.5171 | 77.6% | flashinfer |
| 🔴 | **GatedDeltaNetAutogradOp** | test_gated_deltanet_vs_fla_autograd[gdn-autograd-b2-s2k-h4-d64-bfloat16] | 0.0867 | 0.0673 | 77.7% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-float16] | 0.6694 | 0.5199 | 77.7% | flashinfer |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-bfloat16] | 0.3114 | 0.2419 | 77.7% | fla |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-bfloat16] | 0.0865 | 0.0673 | 77.8% | fla |
| 🔴 | **GatedDeltaNetPrefillBHTDFwdOp** | test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-float16] | 0.2508 | 0.1966 | 78.4% | fla |
| 🔴 | **GatedDeltaNetAutogradOp** | test_gated_deltanet_vs_fla_autograd[gdn-autograd-b2-s2k-h4-d64-float16] | 0.0867 | 0.0681 | 78.6% | fla |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0043 | 0.0033 | 78.6% | mamba |
| 🔴 | **GatedDeltaNetPrefillBHTDFwdOp** | test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-bfloat16] | 0.2522 | 0.1984 | 78.7% | fla |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-float16] | 0.0865 | 0.0681 | 78.7% | fla |
| 🔴 | **GroupedGemmFwdOp** | test_grouped_gemm_bench[nn-batch16-m4096-n4096-k4096-float16] | 0.3408 | 0.2691 | 79.0% | torch |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-bfloat16] | 0.6114 | 0.4865 | 79.6% | fla |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-large-bfloat16] | 0.0715 | 0.0569 | 79.6% | torch-compile |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 12 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 826 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 2735 lines in `ops/`, 38.0% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 3840 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

### Never-built kernels

| File | Executed |
| --- | --- |
| `kernels/attention/deepseek_mla_decode.py` | 5.8% |
| `kernels/attention/gqa_fwd_ws.py` | 6.4% |
| `kernels/attention/gqa_dense.py` | 9.8% |
| `kernels/attention/gqa_fwd_fp8.py` | 9.8% |
| `kernels/attention/gqa_fwd.py` | 11.2% |
| `kernels/attention/mha_decode_paged.py` | 11.6% |
| `kernels/attention/gqa_decode.py` | 11.7% |
| `kernels/attention/gqa_decode_bs1_common.py` | 12.4% |
| `kernels/attention/mha_decode.py` | 13.2% |
| `kernels/attention/gqa_decode_bs1.py` | 13.4% |
| `kernels/attention/gqa_prefill_varlen_fwd.py` | 18.7% |
| `kernels/attention/deepseek_nsa_cmp_fwd.py` | 19.6% |

<details>
<summary>Untested pure Python, worst 15 files</summary>

| File | Uncovered | Executed |
| --- | --- | --- |
| `perf/formulas.py` | 784 | 11.5% |
| `ops/attention/gqa.py` | 660 | 24.1% |
| `ops/moe/staged.py` | 176 | 46.0% |
| `ops/pool.py` | 155 | 76.5% |
| `ops/convolution.py` | 120 | 74.1% |
| `ops/op_base.py` | 116 | 57.2% |
| `ops/linear_attention/gated_deltanet.py` | 114 | 72.9% |
| `ops/reduction/reduce.py` | 100 | 58.5% |
| `ops/elementwise/_base.py` | 88 | 76.7% |
| `ops/mamba/mamba2_fwd.py` | 86 | 20.4% |
| `ops/rope.py` | 85 | 70.4% |
| `ops/_roofline_codegen.py` | 82 | 68.8% |
| `ops/linear_attention/deltanet.py` | 65 | 63.3% |
| `ops/moe/contracts.py` | 64 | 56.5% |
| `trace/ui.py` | 62 | 24.4% |

</details>

Per-line detail is in the `htmlcov/` directory of this run's `tileops_op_test` artifact.
