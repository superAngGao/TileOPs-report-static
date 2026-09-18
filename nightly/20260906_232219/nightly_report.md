# ❌ TileOPs Nightly Report

> **2026-09-06 19:01** &ensp;|&ensp; `001ef398` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Correctness** | ✅ &ensp; (511/511 tests across 87 ops) |
| **Benchmarked Ops** | 181 |
| **Benchmark Failures** | ✅ None &ensp;|&ensp; ⚠️ 3 skipped |
| **Regressions** (vs 14-day median) | ⚠️ 1 |
| **Baseline Alerts** (< 80%) | ⚠️ 111 |
| **Roofline anomalies** | ❌ 1 impossible |
| **Improvements** (vs 14-day best) | 🎉 34 |
| **Moved since previous run** | 🔵 35 |
| **Never-built kernels** | ⚠️ 11 files &ensp;·&ensp; `kernels/attention/deepseek_mla_decode.py` at 5.8% |
| **Untested roofline math** | 797 lines in `perf/` &ensp;·&ensp; `perf/formulas.py` at 11.5% |
| **Untested op logic** | 2689 lines in `ops/` **+247** &ensp;·&ensp; 38.2% of branches taken **−3.1pp** |
| | <sub>coverage compared against the 2026-09-05 run; no figure means it held</sub> |

## ⚠️ Performance Regressions (vs 14-day median)

| Op | Config | Median (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **FusedMoEExpertsNopadPersistent3WGFwdOp** | test_moe_experts_nopad_bench[qwen3-235b-prefill-float16] | 4.1733 | 6.2467 | +49.7% | 462.04 |

## 🎉 Performance Improvements (vs 14-day best)

| Op | Config | Prev Best (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[global-1x1-float16] | 0.0132 | 0.0033 | -74.9% | 0.24 |
| **MaxPool1dFwdOp** | test_max_pool1d_bench[textcnn-global-float16] | 0.0134 | 0.0040 | -70.5% | 0.53 |
| **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[textcnn-global-float16] | 0.0148 | 0.0050 | -66.2% | 0.42 |
| **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[nondiv-7x7-bfloat16] | 0.0157 | 0.0066 | -58.2% | 0.07 |
| **MaxPool3dIndicesFwdOp** | test_max_pool3d_indices_bench[medicalnet-stem-bfloat16] | 0.2463 | 0.1302 | -47.1% | 1.47 |
| **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[spp-6x6-float16] | 0.0154 | 0.0081 | -47.1% | 0.11 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-float16] | 0.1042 | 0.0555 | -46.7% | 1.04 |
| **MaxPool2dFwdOp** | test_max_pool2d_bench[resnet-stem-bfloat16] | 0.0470 | 0.0279 | -40.6% | 2.07 |
| **MaxPool2dFwdOp** | test_max_pool2d_bench[resnet-stem-float16] | 0.0469 | 0.0284 | -39.6% | 2.04 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-bfloat16] | 0.0863 | 0.0554 | -35.8% | 1.04 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[alexnet-ceil-float16] | 0.0163 | 0.0110 | -32.5% | 1.22 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[alexnet-ceil-bfloat16] | 0.0163 | 0.0110 | -32.5% | 1.22 |
| **MaxPool2dFwdOp** | test_max_pool2d_bench[resnet-stem-float32] | 0.0527 | 0.0362 | -31.3% | 1.60 |
| **AvgPool1dFwdOp** | test_avg_pool1d_bench[audio-downsample-float16] | 0.0061 | 0.0044 | -29.2% | 0.72 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-float32] | 0.0836 | 0.0610 | -27.0% | 0.95 |
| **AvgPool1dFwdOp** | test_avg_pool1d_bench[ceil-bfloat16] | 0.0035 | 0.0025 | -26.9% | 0.41 |
| **AvgPool3dFwdOp** | test_avg_pool3d_bench[ceil-video-float16] | 0.0044 | 0.0033 | -24.3% | 0.79 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-float16] | 0.0121 | 0.0099 | -18.0% | 0.65 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-bfloat16] | 0.0121 | 0.0100 | -17.1% | 0.64 |
| **MaxPool1dFwdOp** | test_max_pool1d_bench[ecg-cnn-dilated-bfloat16] | 0.0095 | 0.0081 | -15.2% | 1.30 |
| **AvgPool1dFwdOp** | test_avg_pool1d_bench[long-temporal-float16] | 0.0212 | 0.0180 | -15.1% | 1.13 |
| **MaxPool3dIndicesFwdOp** | test_max_pool3d_indices_bench[c3d-pool1-float16] | 0.1418 | 0.1211 | -14.6% | 0.85 |
| **MaxPool3dIndicesFwdOp** | test_max_pool3d_indices_bench[c3d-pool2-float16] | 0.0317 | 0.0272 | -14.5% | 0.95 |
| **InstanceNormFwdOp** | test_instance_norm_bench[image-affine-bfloat16] | 0.0034 | 0.0029 | -14.0% | 1.78 |
| **MaxPool3dFwdOp** | test_max_pool3d_bench[medicalnet-stem-bfloat16] | 0.1108 | 0.0961 | -13.3% | 1.99 |
| **InstanceNormFwdOp** | test_instance_norm_bench[image-bfloat16] | 0.0034 | 0.0029 | -13.2% | 1.07 |
| **LayerNormFwdOp** | test_layer_norm_bench[llama-8b-prefill-bfloat16] | 0.0146 | 0.0128 | -12.7% | 3.29 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[alexnet-ceil-float32] | 0.0166 | 0.0145 | -12.5% | 0.92 |
| **InstanceNormFwdOp** | test_instance_norm_bench[image-float16] | 0.0034 | 0.0029 | -12.4% | 1.07 |
| **InstanceNormFwdOp** | test_instance_norm_bench[image-affine-float16] | 0.0034 | 0.0030 | -12.2% | 1.74 |
| **FusedAddLayerNormFwdOp** | test_fused_add_layer_norm_bench[llama-70b-prefill-bfloat16] | 0.0473 | 0.0416 | -12.0% | 2.42 |
| **InstanceNormFwdOp** | test_instance_norm_bench[wider-channel-float16] | 0.0033 | 0.0029 | -11.5% | 0.82 |
| **MaxPool2dFwdOp** | test_max_pool2d_bench[vgg-block-bfloat16] | 0.0072 | 0.0064 | -11.2% | 1.01 |
| **InstanceNormFwdOp** | test_instance_norm_bench[wider-channel-affine-float16] | 0.0035 | 0.0031 | -10.2% | 1.29 |

## 🔵 Moved Since Previous Run

> Moves against the most recent reading. A row restored to its old level appears only here: returning is not a new 14-day record.

| Op | Config | Previous (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[global-1x1-float16] | 0.0133 | 0.0033 | -74.9% | 0.24 |
| **MaxPool1dFwdOp** | test_max_pool1d_bench[textcnn-global-float16] | 0.0134 | 0.0040 | -70.5% | 0.53 |
| **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[textcnn-global-float16] | 0.0148 | 0.0050 | -66.2% | 0.42 |
| **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[nondiv-7x7-bfloat16] | 0.0158 | 0.0066 | -58.4% | 0.07 |
| **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[spp-6x6-float16] | 0.0154 | 0.0081 | -47.2% | 0.11 |
| **MaxPool3dIndicesFwdOp** | test_max_pool3d_indices_bench[medicalnet-stem-bfloat16] | 0.2463 | 0.1302 | -47.1% | 1.47 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-float16] | 0.1042 | 0.0555 | -46.7% | 1.04 |
| **MaxPool2dFwdOp** | test_max_pool2d_bench[resnet-stem-bfloat16] | 0.0470 | 0.0279 | -40.6% | 2.07 |
| **MaxPool2dFwdOp** | test_max_pool2d_bench[resnet-stem-float16] | 0.0471 | 0.0284 | -39.8% | 2.04 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-bfloat16] | 0.0863 | 0.0554 | -35.8% | 1.04 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[alexnet-ceil-float16] | 0.0163 | 0.0110 | -32.5% | 1.22 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[alexnet-ceil-bfloat16] | 0.0163 | 0.0110 | -32.5% | 1.22 |
| **MaxPool2dFwdOp** | test_max_pool2d_bench[resnet-stem-float32] | 0.0527 | 0.0362 | -31.4% | 1.60 |
| **AvgPool1dFwdOp** | test_avg_pool1d_bench[audio-downsample-float16] | 0.0062 | 0.0044 | -29.5% | 0.72 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-float32] | 0.0836 | 0.0610 | -27.0% | 0.95 |
| **AvgPool1dFwdOp** | test_avg_pool1d_bench[ceil-bfloat16] | 0.0035 | 0.0025 | -26.9% | 0.41 |
| **AvgPool3dFwdOp** | test_avg_pool3d_bench[ceil-video-float16] | 0.0044 | 0.0033 | -24.8% | 0.79 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-float16] | 0.0121 | 0.0099 | -18.0% | 0.65 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-bfloat16] | 0.0121 | 0.0100 | -17.1% | 0.64 |
| **RMSNormFwdOp** | test_rms_norm_bench[llama-405b-decode-bfloat16] | 0.0036 | 0.0030 | -15.9% | 0.02 |
| **MaxPool1dFwdOp** | test_max_pool1d_bench[ecg-cnn-dilated-bfloat16] | 0.0095 | 0.0081 | -15.4% | 1.30 |
| **AvgPool1dFwdOp** | test_avg_pool1d_bench[long-temporal-float16] | 0.0213 | 0.0180 | -15.2% | 1.13 |
| **MaxPool3dIndicesFwdOp** | test_max_pool3d_indices_bench[c3d-pool1-float16] | 0.1418 | 0.1211 | -14.6% | 0.85 |
| **MaxPool3dIndicesFwdOp** | test_max_pool3d_indices_bench[c3d-pool2-float16] | 0.0317 | 0.0272 | -14.5% | 0.95 |
| **InstanceNormFwdOp** | test_instance_norm_bench[image-affine-bfloat16] | 0.0034 | 0.0029 | -14.0% | 1.78 |
| **MaxPool3dFwdOp** | test_max_pool3d_bench[medicalnet-stem-bfloat16] | 0.1112 | 0.0961 | -13.6% | 1.99 |
| **InstanceNormFwdOp** | test_instance_norm_bench[image-float16] | 0.0034 | 0.0029 | -13.2% | 1.07 |
| **InstanceNormFwdOp** | test_instance_norm_bench[image-bfloat16] | 0.0034 | 0.0029 | -13.2% | 1.07 |
| **InstanceNormFwdOp** | test_instance_norm_bench[image-affine-float16] | 0.0035 | 0.0030 | -13.0% | 1.74 |
| **LayerNormFwdOp** | test_layer_norm_bench[llama-8b-prefill-bfloat16] | 0.0146 | 0.0128 | -12.7% | 3.29 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[alexnet-ceil-float32] | 0.0166 | 0.0145 | -12.5% | 0.92 |
| **FusedAddLayerNormFwdOp** | test_fused_add_layer_norm_bench[llama-70b-prefill-bfloat16] | 0.0473 | 0.0416 | -12.1% | 2.42 |
| **MaxPool2dFwdOp** | test_max_pool2d_bench[vgg-block-float16] | 0.0072 | 0.0064 | -11.6% | 1.01 |
| **InstanceNormFwdOp** | test_instance_norm_bench[wider-channel-float16] | 0.0033 | 0.0029 | -11.5% | 0.82 |
| **MaxPool2dFwdOp** | test_max_pool2d_bench[vgg-block-bfloat16] | 0.0072 | 0.0064 | -11.4% | 1.01 |

## ⚠️ Roofline Model Anomalies

> A FAIL row implies a rate above the hardware's theoretical ceiling: its (flops, bytes) formula or declared roof is wrong, and its SOL reading cannot be trusted. A WARN row exceeds the calibrated ceiling; recheck the formula or the calibration.

| Level | Op | Config | Signal |
|:------|:---|:-------|:-------|
| FAIL | **FusedMoeFwdOp** | test_fused_moe_fwd_bench[kimi-k2-decode-bfloat16] | bytes/s over HBM theoretical |
| WARN | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-attn-proj-float16] | 107% of the calibrated ceiling |
| WARN | **GemmFwdOp** | test_gemm_bench[k-dominant-7168x16384-bfloat16] | 108% of the calibrated ceiling |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 80%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-gate-up-block128-float8_e4m3fn] | 0.1479 | 0.0129 | 8.7% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[gemv-down-m1-block128-float8_e4m3fn] | 0.0445 | 0.0077 | 17.2% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[k-dominant-7168x16384-block128-float8_e4m3fn] | 3.5867 | 0.7761 | 21.6% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-down-block128-float8_e4m3fn] | 0.0377 | 0.0092 | 24.4% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-attn-proj-block128-float8_e4m3fn] | 0.7693 | 0.2168 | 28.2% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[small-batch-down-m8-per-tensor-float8_e4m3fn] | 0.0266 | 0.0083 | 31.3% | deepgemm |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-bfloat16] | 0.4536 | 0.1421 | 31.3% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-bfloat16] | 0.4560 | 0.1429 | 31.3% | fa3 |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b4-dmem1024-d512-float16] | 0.0826 | 0.0259 | 31.4% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-down-block128-float8_e4m3fn] | 0.4456 | 0.1436 | 32.2% | flashinfer-fp8-blockscale-sm90 |

<details>
<summary><strong>101 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **MeanPoolingFwdOp** | test_mean_pooling_bench[uniform-8k-float16] | 0.1352 | 0.0470 | 34.7% | torch-view-mean |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-gate-up-block128-float8_e4m3fn] | 0.3865 | 0.1399 | 36.2% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-b64-complex64] | 0.0152 | 0.0056 | 37.0% | torch-cufft |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[wide-n-24576-block128-float8_e4m3fn] | 1.0286 | 0.3835 | 37.3% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[mha-decode-b32-pv-per-tensor-float8_e4m3fn] | 0.0646 | 0.0249 | 38.6% | flashinfer-bmm-fp8 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-short-bfloat16] | 0.4083 | 0.1592 | 39.0% | fa3 |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b1-dmem512-d256-float16] | 0.0329 | 0.0131 | 39.7% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[gemv-down-m1-per-tensor-float8_e4m3fn] | 0.0259 | 0.0103 | 39.8% | deepgemm |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-short-bfloat16] | 0.4142 | 0.1656 | 40.0% | fa3 |
| 🔴 | **MeanPoolingFwdOp** | test_mean_pooling_bench[uniform-batched-float16] | 0.0701 | 0.0286 | 40.8% | torch-view-mean |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-down-per-tensor-float8_e4m3fn] | 0.0254 | 0.0104 | 41.0% | deepgemm |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c128-b64-complex128] | 0.0205 | 0.0085 | 41.4% | torch-cufft |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-bfloat16] | 1.3104 | 0.5494 | 41.9% | fa3 |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[mha-decode-b64-qk-per-tensor-float8_e4m3fn] | 0.1155 | 0.0494 | 42.8% | flashinfer-bmm-fp8 |
| 🔴 | **GroupedGemmFwdOp** | test_grouped_gemm_bench[tn-batch16-m4096-n4096-k4096-float16] | 0.7853 | 0.3551 | 45.2% | torch |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-bfloat16] | 1.2421 | 0.5908 | 47.6% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-q-lt-kv-bfloat16] | 0.1130 | 0.0538 | 47.6% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-q-lt-kv-float16] | 0.1132 | 0.0541 | 47.8% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p256-float16] | 0.1655 | 0.0813 | 49.1% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-405b-p256-float16] | 0.0536 | 0.0266 | 49.5% | fa3 |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-long-k-pressure-float16] | 0.2853 | 0.1414 | 49.6% | marlin-fp32 |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-small-bfloat16] | 0.0394 | 0.0196 | 49.8% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-bfloat16] | 1.1020 | 0.5503 | 49.9% | fa3 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-down-per-tensor-float8_e4m3fn] | 0.2110 | 0.1055 | 50.0% | deepgemm |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-2p7b-b2-s32k-dt-bias-float16] | 0.0445 | 0.0224 | 50.2% | mamba |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-70b-q-lt-kv-bfloat16] | 0.1968 | 0.0992 | 50.4% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-70b-q-lt-kv-float16] | 0.1976 | 0.1002 | 50.7% | fa3 |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-dt-bias-bfloat16] | 0.0124 | 0.0064 | 51.5% | mamba |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[compile-smoke-rect-128x256x256-float16] | 0.0059 | 0.0031 | 52.2% | torch-dequantized-matmul |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-bfloat16] | 0.0122 | 0.0064 | 52.9% | mamba |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-non-power2-low-cta-float16] | 0.0745 | 0.0408 | 54.7% | marlin-fp32 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-70b-p256-float16] | 0.0669 | 0.0368 | 54.9% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 1.0169 | 0.5776 | 56.8% | fa3 |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-medium-bfloat16] | 0.0544 | 0.0313 | 57.5% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-float16] | 0.2432 | 0.1424 | 58.5% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-float16] | 0.2446 | 0.1432 | 58.5% | fa3 |
| 🔴 | **TopkSelectorFwdOp** | test_topk_selector_bench[topk1024-s32k-kv64k-float32] | 15.6136 | 9.2733 | 59.4% | flashinfer |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[throughput-8b-p64-float16] | 0.2490 | 0.1509 | 60.6% | flashinfer |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-float16] | 0.9012 | 0.5528 | 61.3% | fa3 |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-float16] | 0.6351 | 0.3908 | 61.5% | fla |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-bfloat16] | 0.6373 | 0.3930 | 61.7% | fla |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-float16] | 0.8917 | 0.5532 | 62.0% | fa3 |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-hbm-streaming-threshold-float16] | 0.0607 | 0.0380 | 62.5% | marlin-fp16 |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b8-dmem512-d256-bfloat16] | 0.0335 | 0.0213 | 63.5% | torch-compile |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[compile-smoke-square-64x64x128-float16] | 0.0042 | 0.0027 | 63.6% | torch-dequantized-matmul |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-float16] | 1.4182 | 0.9178 | 64.7% | fla |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-bfloat16] | 0.3163 | 0.2052 | 64.9% | fla |
| 🔴 | **GatedDeltaNetAutogradOp** | test_gated_deltanet_vs_fla_autograd[gdn-autograd-b2-s8k-h4-d64-bfloat16] | 0.3163 | 0.2054 | 64.9% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-bfloat16] | 1.4664 | 0.9528 | 65.0% | fla |
| 🔴 | **GatedDeltaNetAutogradOp** | test_gated_deltanet_vs_fla_autograd[gdn-autograd-b2-s8k-h4-d64-float16] | 0.3143 | 0.2049 | 65.2% | fla |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-float16] | 0.3137 | 0.2051 | 65.4% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-float16] | 0.3806 | 0.2492 | 65.5% | fla |
| 🔴 | **TopkSelectorFwdOp** | test_topk_selector_bench[topk2048-s32k-kv64k-float32] | 16.2413 | 10.6797 | 65.8% | flashinfer |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-l2-resident-ish-float16] | 0.0328 | 0.0217 | 66.1% | marlin-fp32 |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-float16] | 0.2014 | 0.1339 | 66.5% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-bfloat16] | 0.3878 | 0.2584 | 66.6% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-bfloat16] | 0.7512 | 0.5016 | 66.8% | fla |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-unbatched-complex64] | 0.0081 | 0.0055 | 67.3% | torch-cufft |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-float16] | 0.7239 | 0.4883 | 67.5% | fla |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-bfloat16] | 0.0966 | 0.0657 | 68.1% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-bfloat16] | 0.2051 | 0.1399 | 68.2% | fla |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[moe-prefill-b128-per-tensor-float8_e4m3fn] | 0.9008 | 0.6244 | 69.3% | flashinfer-bmm-fp8 |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-float16] | 0.0987 | 0.0699 | 70.8% | fla |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-float16] | 0.8328 | 0.5925 | 71.2% | fa3 |
| 🔴 | **SharedFusedMoE** | test_shared_fused_moe_bench[1-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 0.5970 | 0.4270 | 71.5% | vllm |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.8081 | 0.5809 | 71.9% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-softcap50-float16] | 0.1739 | 0.1252 | 72.0% | flashinfer |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0569 | 0.0411 | 72.2% | flashinfer |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-float16] | 0.0571 | 0.0412 | 72.2% | flashinfer |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-float16] | 0.1486 | 0.1077 | 72.5% | fla |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b4-4k-bfloat16] | 1.0509 | 0.7697 | 73.2% | torch-cublas |
| 🔴 | **FusedTopKOp** | test_fused_topk_bench[kimi-k2-t512-bias-bfloat16] | 0.0148 | 0.0109 | 73.7% | vllm |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-2k-bfloat16] | 0.2801 | 0.2067 | 73.8% | torch-cublas |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-uniform-bfloat16] | 0.0604 | 0.0447 | 73.9% | fa3 |
| 🔴 | **BmmFwdOp** | test_bmm_bench[moe-prefill-b128-bfloat16] | 0.2908 | 0.2152 | 74.0% | torch-cublas |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-float16] | 0.0932 | 0.0690 | 74.0% | flashinfer |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-uniform-float16] | 0.0608 | 0.0450 | 74.0% | fa3 |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-2k-float16] | 0.2821 | 0.2091 | 74.1% | torch-cublas |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-bfloat16] | 0.0928 | 0.0692 | 74.6% | flashinfer |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-bfloat16] | 0.1444 | 0.1078 | 74.7% | fla |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-float16] | 0.6172 | 0.4650 | 75.3% | fla |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-float16] | 0.1655 | 0.1252 | 75.6% | flashinfer |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-bfloat16] | 0.3114 | 0.2365 | 75.9% | fla |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-1k-bfloat16] | 0.0407 | 0.0309 | 76.0% | torch-cublas |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-1k-float16] | 0.0407 | 0.0311 | 76.4% | torch-cublas |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.6679 | 0.5171 | 77.4% | flashinfer |
| 🔴 | **GatedDeltaNetAutogradOp** | test_gated_deltanet_vs_fla_autograd[gdn-autograd-b2-s2k-h4-d64-float16] | 0.0868 | 0.0672 | 77.4% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-float16] | 0.3521 | 0.2726 | 77.4% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.3499 | 0.2710 | 77.4% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-float16] | 0.6676 | 0.5181 | 77.6% | flashinfer |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-float16] | 0.0866 | 0.0672 | 77.6% | fla |
| 🔴 | **GatedDeltaNetAutogradOp** | test_gated_deltanet_vs_fla_autograd[gdn-autograd-b2-s2k-h4-d64-bfloat16] | 0.0867 | 0.0673 | 77.7% | fla |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-bfloat16] | 0.0866 | 0.0673 | 77.7% | fla |
| 🔴 | **GatedDeltaNetPrefillBHTDFwdOp** | test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-float16] | 0.2512 | 0.1958 | 78.0% | fla |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-bfloat16] | 0.6103 | 0.4770 | 78.2% | fla |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0043 | 0.0033 | 78.2% | mamba |
| 🔴 | **GatedDeltaNetPrefillBHTDFwdOp** | test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-bfloat16] | 0.2525 | 0.1979 | 78.4% | fla |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-float16] | 0.3127 | 0.2479 | 79.3% | fla |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-large-bfloat16] | 0.0716 | 0.0568 | 79.3% | torch-compile |
| 🔴 | **GroupedGemmFwdOp** | test_grouped_gemm_bench[nn-batch16-m4096-n4096-k4096-float16] | 0.3400 | 0.2705 | 79.5% | torch |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s4k-h4-d64-float16] | 0.1570 | 0.1252 | 79.8% | fla |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 11 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 797 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 2689 lines in `ops/`, 38.2% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 3765 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

### Never-built kernels

| File | Executed |
| --- | --- |
| `kernels/attention/deepseek_mla_decode.py` | 5.8% |
| `kernels/attention/gqa_fwd_ws.py` | 6.4% |
| `kernels/attention/gqa_fwd_fp8.py` | 9.8% |
| `kernels/attention/gqa_dense.py` | 10.1% |
| `kernels/attention/gqa_fwd.py` | 11.2% |
| `kernels/attention/mha_decode_paged.py` | 11.6% |
| `kernels/attention/gqa_decode_bs1_common.py` | 12.4% |
| `kernels/attention/mha_decode.py` | 13.2% |
| `kernels/attention/gqa_decode.py` | 13.8% |
| `kernels/attention/deepseek_nsa_cmp_fwd.py` | 18.3% |
| `kernels/attention/gqa_prefill_varlen_fwd.py` | 18.7% |

<details>
<summary>Untested pure Python, worst 15 files</summary>

| File | Uncovered | Executed |
| --- | --- | --- |
| `perf/formulas.py` | 755 | 11.5% |
| `ops/attention/gqa.py` | 643 | 24.5% |
| `ops/pool.py` | 150 | 76.3% |
| `ops/moe/staged.py` | 136 | 49.1% |
| `ops/convolution.py` | 120 | 74.1% |
| `ops/op_base.py` | 116 | 57.2% |
| `ops/linear_attention/gated_deltanet.py` | 114 | 72.9% |
| `ops/reduction/reduce.py` | 100 | 58.5% |
| `ops/elementwise/_base.py` | 88 | 76.7% |
| `ops/mamba/mamba2_fwd.py` | 86 | 20.4% |
| `ops/rope.py` | 85 | 70.4% |
| `ops/_roofline_codegen.py` | 82 | 68.8% |
| `ops/moe/contracts.py` | 80 | 55.6% |
| `ops/linear_attention/deltanet.py` | 65 | 63.3% |
| `trace/ui.py` | 62 | 24.4% |

</details>

Per-line detail is in the `htmlcov/` directory of this run's `tileops_op_test` artifact.
