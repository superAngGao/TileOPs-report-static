# ❌ TileOPs Nightly Report

> **2026-09-05 19:52** &ensp;|&ensp; `b4fc7863` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Correctness** | ✅ &ensp; (509/509 tests across 87 ops) |
| **Benchmarked Ops** | 181 |
| **Benchmark Failures** | ✅ None &ensp;|&ensp; ⚠️ 13 skipped |
| **Regressions** (vs 14-day median) | ⚠️ 1 |
| **Baseline Alerts** (< 80%) | ⚠️ 120 |
| **Roofline anomalies** | ❌ 1 impossible |
| **Improvements** (vs 14-day best) | 🎉 48 |
| **Moved since previous run** | 🔵 47 |
| **Never-built kernels** | ⚠️ 11 files **−1** &ensp;·&ensp; `kernels/attention/deepseek_mla_decode.py` at 5.8% |
| **Untested roofline math** | 797 lines in `perf/` &ensp;·&ensp; `perf/formulas.py` at 11.5% |
| **Untested op logic** | 2442 lines in `ops/` &ensp;·&ensp; 41.2% of branches taken |
| | <sub>coverage compared against the 2026-09-04 run; no figure means it held</sub> |

## ⚠️ Performance Regressions (vs 14-day median)

| Op | Config | Median (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **FusedMoEExpertsNopadPersistent3WGFwdOp** | test_moe_experts_nopad_bench[qwen3-235b-prefill-float16] | 4.1595 | 6.2662 | +50.6% | 460.60 |

## 🎉 Performance Improvements (vs 14-day best)

| Op | Config | Prev Best (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **BatchNormFwdOp** | test_batch_norm_fwd_bench[large-spatial-float16] | 4.3383 | 0.9093 | -79.0% | 5.90 |
| **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-stage2-float16] | 0.0107 | 0.0026 | -76.0% | 2.05 |
| **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-stage1-float16] | 0.0109 | 0.0028 | -74.2% | 1.86 |
| **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-stage3-float16] | 0.0128 | 0.0037 | -71.3% | 2.18 |
| **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-fc-float16] | 0.0061 | 0.0018 | -71.1% | 0.01 |
| **MaxPool3dIndicesFwdOp** | test_max_pool3d_indices_bench[c3d-pool1-float16] | 0.3039 | 0.1418 | -53.3% | 0.72 |
| **FusedAddRMSNormFwdOp** | test_fused_add_rms_norm_bench[llama-405b-decode-bfloat16] | 0.0062 | 0.0032 | -48.7% | 0.03 |
| **MaxPool3dIndicesFwdOp** | test_max_pool3d_indices_bench[c3d-pool2-float16] | 0.0588 | 0.0317 | -46.0% | 0.81 |
| **Conv2dFwdOp** | test_conv2d_bench[resnet-3x3-bias-bfloat16] | 0.0137 | 0.0075 | -45.2% | 61.55 |
| **Conv2dFwdOp** | test_conv2d_bench[resnet-3x3-float16] | 0.0130 | 0.0071 | -45.2% | 65.09 |
| **Conv2dFwdOp** | test_conv2d_bench[resnet-3x3-bfloat16] | 0.0130 | 0.0071 | -45.2% | 65.09 |
| **Conv2dFwdOp** | test_conv2d_bench[resnet-3x3-bias-float16] | 0.0132 | 0.0075 | -43.5% | 61.80 |
| **GroupNormFwdOp** | test_group_norm_no_affine_bench[tail-spatial-g16-float16] | 0.0052 | 0.0031 | -40.5% | 0.45 |
| **Conv2dFwdOp** | test_conv2d_bench[highres-3x3-s1-float16] | 0.1044 | 0.0641 | -38.6% | 461.85 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-float16] | 0.0196 | 0.0121 | -38.3% | 0.53 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-bfloat16] | 0.0194 | 0.0121 | -37.8% | 0.53 |
| **Conv2dFwdOp** | test_conv2d_bench[highres-3x3-s1-bias-float16] | 0.1037 | 0.0654 | -36.9% | 452.35 |
| **GroupNormFwdOp** | test_group_norm_bench[tail-spatial-g16-affine-float16] | 0.0060 | 0.0039 | -35.4% | 0.59 |
| **GroupNormFwdOp** | test_group_norm_bench[wider-channel-g32-affine-float16] | 0.0059 | 0.0038 | -35.1% | 1.05 |
| **Conv2dFwdOp** | test_conv2d_bench[midres-5x5-s1-float16] | 0.0161 | 0.0106 | -34.0% | 120.92 |
| **Conv2dFwdOp** | test_conv2d_bench[midres-5x5-s1-bias-float16] | 0.0164 | 0.0111 | -32.7% | 116.05 |
| **Conv2dFwdOp** | test_conv2d_bench[stage-transition-3x3-s2-float16] | 0.0137 | 0.0093 | -31.9% | 49.49 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[alexnet-ceil-bfloat16] | 0.0237 | 0.0163 | -31.3% | 0.83 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[alexnet-ceil-float16] | 0.0237 | 0.0163 | -31.1% | 0.82 |
| **Conv2dFwdOp** | test_conv2d_bench[stage-transition-3x3-s2-bias-float16] | 0.0141 | 0.0099 | -30.1% | 46.79 |
| **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[ecg-cnn-dilated-bfloat16] | 0.0223 | 0.0156 | -30.0% | 0.67 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[alexnet-ceil-float32] | 0.0236 | 0.0166 | -29.7% | 0.81 |
| **GroupNormFwdOp** | test_group_norm_no_affine_bench[wider-channel-g32-float16] | 0.0048 | 0.0034 | -29.3% | 0.71 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-float32] | 0.0195 | 0.0139 | -28.9% | 0.46 |
| **Conv2dFwdOp** | test_conv2d_bench[stride2-bfloat16] | 0.0110 | 0.0081 | -26.5% | 7.14 |
| **MaxPool3dIndicesFwdOp** | test_max_pool3d_indices_bench[medicalnet-stem-bfloat16] | 0.3314 | 0.2463 | -25.7% | 0.77 |
| **Conv2dFwdOp** | test_conv2d_bench[stride2-bias-bfloat16] | 0.0115 | 0.0086 | -24.9% | 6.72 |
| **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[textcnn-global-float16] | 0.0193 | 0.0148 | -23.4% | 0.14 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-bfloat16] | 0.1122 | 0.0863 | -23.1% | 0.67 |
| **Conv2dFwdOp** | test_conv2d_bench[classifier-1x1-float16] | 0.0090 | 0.0069 | -23.0% | 14.80 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-float32] | 0.1071 | 0.0836 | -22.0% | 0.69 |
| **Conv2dFwdOp** | test_conv2d_bench[stage-transition-5x5-s2-float16] | 0.0224 | 0.0175 | -21.8% | 73.25 |
| **Conv2dFwdOp** | test_conv2d_bench[stage-transition-5x5-s2-bias-float16] | 0.0224 | 0.0180 | -19.6% | 71.37 |
| **Conv2dFwdOp** | test_conv2d_bench[late-stage-1x1-bias-float16] | 0.0052 | 0.0042 | -19.5% | 24.38 |
| **Conv2dFwdOp** | test_conv2d_bench[late-stage-1x1-float16] | 0.0050 | 0.0040 | -19.2% | 25.49 |
| **Conv2dFwdOp** | test_conv2d_bench[classifier-1x1-bias-float16] | 0.0094 | 0.0076 | -18.7% | 13.45 |
| **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[sincnet-speaker-local-float16] | 0.0217 | 0.0180 | -17.1% | 0.58 |
| **FusedAddRMSNormFwdOp** | test_fused_add_rms_norm_bench[llama-405b-prefill-bfloat16] | 0.0851 | 0.0734 | -13.7% | 2.28 |
| **Conv2dFwdOp** | test_conv2d_bench[stem-3x3-s2-float16] | 0.0036 | 0.0031 | -13.5% | 3.53 |
| **Conv1dFwdOp** | test_conv1d_bench[whisper-large-conv1-bfloat16] | 0.0483 | 0.0428 | -11.3% | 43.05 |
| **Conv1dFwdOp** | test_conv1d_bench[whisper-large-conv1-float16] | 0.0480 | 0.0428 | -10.9% | 43.05 |
| **Conv1dFwdOp** | test_conv1d_bench[whisper-large-conv1-bias-bfloat16] | 0.0475 | 0.0427 | -10.2% | 43.27 |
| **Conv1dFwdOp** | test_conv1d_bench[whisper-large-conv1-bias-float16] | 0.0475 | 0.0427 | -10.2% | 43.27 |

## 🔵 Moved Since Previous Run

> Moves against the most recent reading. A row restored to its old level appears only here: returning is not a new 14-day record.

| Op | Config | Previous (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **BatchNormFwdOp** | test_batch_norm_fwd_bench[large-spatial-float16] | 4.3420 | 0.9093 | -79.1% | 5.90 |
| **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-stage2-float16] | 0.0107 | 0.0026 | -76.0% | 2.05 |
| **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-stage1-float16] | 0.0109 | 0.0028 | -74.3% | 1.86 |
| **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-stage3-float16] | 0.0129 | 0.0037 | -71.6% | 2.18 |
| **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-fc-float16] | 0.0061 | 0.0018 | -71.2% | 0.01 |
| **MaxPool3dIndicesFwdOp** | test_max_pool3d_indices_bench[c3d-pool1-float16] | 0.3041 | 0.1418 | -53.4% | 0.72 |
| **FusedAddRMSNormFwdOp** | test_fused_add_rms_norm_bench[llama-405b-decode-bfloat16] | 0.0062 | 0.0032 | -49.1% | 0.03 |
| **MaxPool3dIndicesFwdOp** | test_max_pool3d_indices_bench[c3d-pool2-float16] | 0.0589 | 0.0317 | -46.1% | 0.81 |
| **Conv2dFwdOp** | test_conv2d_bench[resnet-3x3-float16] | 0.0130 | 0.0071 | -45.3% | 65.09 |
| **Conv2dFwdOp** | test_conv2d_bench[resnet-3x3-bfloat16] | 0.0130 | 0.0071 | -45.3% | 65.09 |
| **Conv2dFwdOp** | test_conv2d_bench[resnet-3x3-bias-bfloat16] | 0.0137 | 0.0075 | -45.2% | 61.55 |
| **Conv2dFwdOp** | test_conv2d_bench[resnet-3x3-bias-float16] | 0.0133 | 0.0075 | -43.6% | 61.80 |
| **GroupNormFwdOp** | test_group_norm_no_affine_bench[tail-spatial-g16-float16] | 0.0052 | 0.0031 | -40.5% | 0.45 |
| **Conv2dFwdOp** | test_conv2d_bench[highres-3x3-s1-float16] | 0.1048 | 0.0641 | -38.8% | 461.85 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-float16] | 0.0197 | 0.0121 | -38.5% | 0.53 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-bfloat16] | 0.0194 | 0.0121 | -37.9% | 0.53 |
| **Conv2dFwdOp** | test_conv2d_bench[highres-3x3-s1-bias-float16] | 0.1051 | 0.0654 | -37.8% | 452.35 |
| **GroupNormFwdOp** | test_group_norm_bench[tail-spatial-g16-affine-float16] | 0.0061 | 0.0039 | -35.8% | 0.59 |
| **GroupNormFwdOp** | test_group_norm_bench[wider-channel-g32-affine-float16] | 0.0059 | 0.0038 | -35.1% | 1.05 |
| **Conv2dFwdOp** | test_conv2d_bench[midres-5x5-s1-float16] | 0.0161 | 0.0106 | -34.0% | 120.92 |
| **Conv2dFwdOp** | test_conv2d_bench[midres-5x5-s1-bias-float16] | 0.0165 | 0.0111 | -32.8% | 116.05 |
| **Conv2dFwdOp** | test_conv2d_bench[stage-transition-3x3-s2-float16] | 0.0138 | 0.0093 | -32.3% | 49.49 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[alexnet-ceil-bfloat16] | 0.0237 | 0.0163 | -31.4% | 0.83 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[alexnet-ceil-float16] | 0.0237 | 0.0163 | -31.2% | 0.82 |
| **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[ecg-cnn-dilated-bfloat16] | 0.0224 | 0.0156 | -30.3% | 0.67 |
| **Conv2dFwdOp** | test_conv2d_bench[stage-transition-3x3-s2-bias-float16] | 0.0142 | 0.0099 | -30.2% | 46.79 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[alexnet-ceil-float32] | 0.0236 | 0.0166 | -29.8% | 0.81 |
| **GroupNormFwdOp** | test_group_norm_no_affine_bench[wider-channel-g32-float16] | 0.0048 | 0.0034 | -29.6% | 0.71 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-float32] | 0.0195 | 0.0139 | -29.0% | 0.46 |
| **Conv2dFwdOp** | test_conv2d_bench[stride2-bfloat16] | 0.0111 | 0.0081 | -27.2% | 7.14 |
| **MaxPool3dIndicesFwdOp** | test_max_pool3d_indices_bench[medicalnet-stem-bfloat16] | 0.3315 | 0.2463 | -25.7% | 0.77 |
| **Conv2dFwdOp** | test_conv2d_bench[stride2-bias-bfloat16] | 0.0116 | 0.0086 | -25.7% | 6.72 |
| **Conv2dFwdOp** | test_conv2d_bench[classifier-1x1-float16] | 0.0091 | 0.0069 | -23.9% | 14.80 |
| **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[textcnn-global-float16] | 0.0193 | 0.0148 | -23.5% | 0.14 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-bfloat16] | 0.1124 | 0.0863 | -23.3% | 0.67 |
| **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-float32] | 0.1078 | 0.0836 | -22.5% | 0.69 |
| **Conv2dFwdOp** | test_conv2d_bench[stage-transition-5x5-s2-float16] | 0.0225 | 0.0175 | -21.9% | 73.25 |
| **Conv2dFwdOp** | test_conv2d_bench[late-stage-1x1-bias-float16] | 0.0053 | 0.0042 | -20.0% | 24.38 |
| **Conv2dFwdOp** | test_conv2d_bench[stage-transition-5x5-s2-bias-float16] | 0.0225 | 0.0180 | -19.9% | 71.37 |
| **Conv2dFwdOp** | test_conv2d_bench[classifier-1x1-bias-float16] | 0.0095 | 0.0076 | -19.8% | 13.45 |
| **Conv2dFwdOp** | test_conv2d_bench[late-stage-1x1-float16] | 0.0050 | 0.0040 | -19.2% | 25.49 |
| **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[sincnet-speaker-local-float16] | 0.0218 | 0.0180 | -17.3% | 0.58 |
| **FusedAddRMSNormFwdOp** | test_fused_add_rms_norm_bench[llama-405b-prefill-bfloat16] | 0.0852 | 0.0734 | -13.8% | 2.28 |
| **Conv1dFwdOp** | test_conv1d_bench[whisper-large-conv1-bfloat16] | 0.0485 | 0.0428 | -11.7% | 43.05 |
| **Conv1dFwdOp** | test_conv1d_bench[whisper-large-conv1-float16] | 0.0482 | 0.0428 | -11.2% | 43.05 |
| **Conv1dFwdOp** | test_conv1d_bench[whisper-large-conv1-bias-float16] | 0.0477 | 0.0427 | -10.7% | 43.27 |
| **Conv1dFwdOp** | test_conv1d_bench[whisper-large-conv1-bias-bfloat16] | 0.0477 | 0.0427 | -10.5% | 43.27 |

## ⚠️ Roofline Model Anomalies

> A FAIL row implies a rate above the hardware's theoretical ceiling: its (flops, bytes) formula or declared roof is wrong, and its SOL reading cannot be trusted. A WARN row exceeds the calibrated ceiling; recheck the formula or the calibration.

| Level | Op | Config | Signal |
|:------|:---|:-------|:-------|
| FAIL | **FusedMoeFwdOp** | test_fused_moe_fwd_bench[kimi-k2-decode-bfloat16] | bytes/s over HBM theoretical |
| WARN | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-attn-proj-float16] | 107% of the calibrated ceiling |
| WARN | **GemmFwdOp** | test_gemm_bench[k-dominant-7168x16384-bfloat16] | 107% of the calibrated ceiling |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 80%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-gate-up-block128-float8_e4m3fn] | 0.1482 | 0.0129 | 8.7% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[gemv-down-m1-block128-float8_e4m3fn] | 0.0445 | 0.0077 | 17.3% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[k-dominant-7168x16384-block128-float8_e4m3fn] | 3.5845 | 0.7745 | 21.6% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-down-block128-float8_e4m3fn] | 0.0377 | 0.0092 | 24.4% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-attn-proj-block128-float8_e4m3fn] | 0.7685 | 0.2151 | 28.0% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **MaxPool1dFwdOp** | test_max_pool1d_bench[textcnn-global-float16] | 0.0134 | 0.0041 | 30.5% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-bfloat16] | 0.4539 | 0.1420 | 31.3% | fa3 |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b4-dmem1024-d512-float16] | 0.0827 | 0.0259 | 31.3% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-bfloat16] | 0.4558 | 0.1430 | 31.4% | fa3 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[small-batch-down-m8-per-tensor-float8_e4m3fn] | 0.0266 | 0.0084 | 31.4% | deepgemm |

<details>
<summary><strong>110 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-down-block128-float8_e4m3fn] | 0.4458 | 0.1434 | 32.2% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **MeanPoolingFwdOp** | test_mean_pooling_bench[uniform-8k-float16] | 0.1350 | 0.0470 | 34.8% | torch-view-mean |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-gate-up-block128-float8_e4m3fn] | 0.3866 | 0.1399 | 36.2% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-b64-complex64] | 0.0152 | 0.0056 | 36.8% | torch-cufft |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[wide-n-24576-block128-float8_e4m3fn] | 1.0273 | 0.3854 | 37.5% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[mha-decode-b32-pv-per-tensor-float8_e4m3fn] | 0.0646 | 0.0249 | 38.5% | flashinfer-bmm-fp8 |
| 🔴 | **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[textcnn-global-float16] | 0.0148 | 0.0057 | 38.6% | torch-compile |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-short-bfloat16] | 0.4084 | 0.1595 | 39.0% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-short-bfloat16] | 0.4144 | 0.1656 | 40.0% | fa3 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[gemv-down-m1-per-tensor-float8_e4m3fn] | 0.0259 | 0.0103 | 40.0% | deepgemm |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b1-dmem512-d256-float16] | 0.0329 | 0.0132 | 40.1% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-down-per-tensor-float8_e4m3fn] | 0.0254 | 0.0103 | 40.6% | deepgemm |
| 🔴 | **MeanPoolingFwdOp** | test_mean_pooling_bench[uniform-batched-float16] | 0.0700 | 0.0285 | 40.7% | torch-view-mean |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c128-b64-complex128] | 0.0205 | 0.0085 | 41.4% | torch-cufft |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-bfloat16] | 1.3102 | 0.5476 | 41.8% | fa3 |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[mha-decode-b64-qk-per-tensor-float8_e4m3fn] | 0.1154 | 0.0496 | 43.0% | flashinfer-bmm-fp8 |
| 🔴 | **GroupedGemmFwdOp** | test_grouped_gemm_bench[tn-batch16-m4096-n4096-k4096-float16] | 0.7862 | 0.3559 | 45.3% | torch |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-bfloat16] | 1.2418 | 0.5895 | 47.5% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-q-lt-kv-bfloat16] | 0.1130 | 0.0538 | 47.7% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-q-lt-kv-float16] | 0.1132 | 0.0545 | 48.2% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p256-float16] | 0.1653 | 0.0807 | 48.8% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-405b-p256-float16] | 0.0536 | 0.0266 | 49.6% | fa3 |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-long-k-pressure-float16] | 0.2846 | 0.1413 | 49.6% | marlin-fp16 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-down-per-tensor-float8_e4m3fn] | 0.2101 | 0.1047 | 49.8% | deepgemm |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-small-bfloat16] | 0.0394 | 0.0196 | 49.8% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-bfloat16] | 1.1029 | 0.5501 | 49.9% | fa3 |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-2p7b-b2-s32k-dt-bias-float16] | 0.0444 | 0.0223 | 50.1% | mamba |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-70b-q-lt-kv-bfloat16] | 0.1970 | 0.0988 | 50.2% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-70b-q-lt-kv-float16] | 0.1979 | 0.1008 | 50.9% | fa3 |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-dt-bias-bfloat16] | 0.0124 | 0.0064 | 51.5% | mamba |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[compile-smoke-rect-128x256x256-float16] | 0.0059 | 0.0031 | 52.2% | torch-dequantized-matmul |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-bfloat16] | 0.0122 | 0.0064 | 52.8% | mamba |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-non-power2-low-cta-float16] | 0.0745 | 0.0408 | 54.7% | marlin-fp32 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-70b-p256-float16] | 0.0669 | 0.0368 | 55.0% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 1.0174 | 0.5789 | 56.9% | fa3 |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-medium-bfloat16] | 0.0544 | 0.0313 | 57.6% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-float16] | 0.2433 | 0.1423 | 58.5% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-float16] | 0.2441 | 0.1433 | 58.7% | fa3 |
| 🔴 | **TopkSelectorFwdOp** | test_topk_selector_bench[topk1024-s32k-kv64k-float32] | 15.6372 | 9.2854 | 59.4% | flashinfer |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[throughput-8b-p64-float16] | 0.2489 | 0.1506 | 60.5% | flashinfer |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-float16] | 0.9011 | 0.5516 | 61.2% | fa3 |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-float16] | 0.6355 | 0.3909 | 61.5% | fla |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-bfloat16] | 0.6372 | 0.3930 | 61.7% | fla |
| 🔴 | **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[global-1x1-float16] | 0.0133 | 0.0082 | 61.7% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-float16] | 0.8929 | 0.5528 | 61.9% | fa3 |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-hbm-streaming-threshold-float16] | 0.0609 | 0.0380 | 62.5% | marlin-fp32 |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[compile-smoke-square-64x64x128-float16] | 0.0042 | 0.0027 | 62.9% | torch-dequantized-matmul |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b8-dmem512-d256-bfloat16] | 0.0334 | 0.0212 | 63.6% | torch-compile |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-float16] | 1.4200 | 0.9173 | 64.6% | fla |
| 🔴 | **GatedDeltaNetAutogradOp** | test_gated_deltanet_vs_fla_autograd[gdn-autograd-b2-s8k-h4-d64-bfloat16] | 0.3164 | 0.2051 | 64.8% | fla |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-bfloat16] | 0.3160 | 0.2051 | 64.9% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-bfloat16] | 1.4653 | 0.9523 | 65.0% | fla |
| 🔴 | **GatedDeltaNetAutogradOp** | test_gated_deltanet_vs_fla_autograd[gdn-autograd-b2-s8k-h4-d64-float16] | 0.3146 | 0.2051 | 65.2% | fla |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-float16] | 0.3142 | 0.2051 | 65.3% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-float16] | 0.3810 | 0.2491 | 65.4% | fla |
| 🔴 | **TopkSelectorFwdOp** | test_topk_selector_bench[topk2048-s32k-kv64k-float32] | 16.2402 | 10.6702 | 65.7% | flashinfer |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-l2-resident-ish-float16] | 0.0328 | 0.0217 | 66.1% | marlin-fp32 |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-float16] | 0.1042 | 0.0690 | 66.3% | torch-compile |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-float16] | 0.2015 | 0.1337 | 66.3% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-bfloat16] | 0.3883 | 0.2580 | 66.5% | fla |
| 🔴 | **AvgPool1dFwdOp** | test_avg_pool1d_bench[ceil-bfloat16] | 0.0035 | 0.0023 | 66.7% | torch-compile |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-bfloat16] | 0.7517 | 0.5013 | 66.7% | fla |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-unbatched-complex64] | 0.0081 | 0.0054 | 66.9% | torch-cufft |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-float16] | 0.7244 | 0.4883 | 67.4% | fla |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-bfloat16] | 0.0970 | 0.0657 | 67.7% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-bfloat16] | 0.2056 | 0.1394 | 67.8% | fla |
| 🔴 | **AvgPool1dFwdOp** | test_avg_pool1d_bench[audio-downsample-float16] | 0.0062 | 0.0042 | 67.9% | torch-compile |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[moe-prefill-b128-per-tensor-float8_e4m3fn] | 0.9006 | 0.6241 | 69.3% | flashinfer-bmm-fp8 |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-float16] | 0.0984 | 0.0699 | 71.0% | fla |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-float16] | 0.8335 | 0.5941 | 71.3% | fa3 |
| 🔴 | **SharedFusedMoE** | test_shared_fused_moe_bench[1-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 0.5983 | 0.4265 | 71.3% | vllm |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.8082 | 0.5810 | 71.9% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-softcap50-float16] | 0.1740 | 0.1252 | 72.0% | flashinfer |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0569 | 0.0410 | 72.0% | flashinfer |
| 🔴 | **MaxPool2dFwdOp** | test_max_pool2d_bench[resnet-stem-float16] | 0.0471 | 0.0340 | 72.2% | torch-compile |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-float16] | 0.0571 | 0.0412 | 72.2% | flashinfer |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-float16] | 0.1488 | 0.1077 | 72.3% | fla |
| 🔴 | **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[nondiv-7x7-bfloat16] | 0.0158 | 0.0115 | 72.6% | torch-compile |
| 🔴 | **MaxPool2dFwdOp** | test_max_pool2d_bench[resnet-stem-bfloat16] | 0.0470 | 0.0342 | 72.8% | torch-compile |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-2k-bfloat16] | 0.2797 | 0.2052 | 73.4% | torch-cublas |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b4-4k-bfloat16] | 1.0517 | 0.7735 | 73.6% | torch-cublas |
| 🔴 | **FusedTopKOp** | test_fused_topk_bench[kimi-k2-t512-bias-bfloat16] | 0.0148 | 0.0109 | 73.6% | vllm |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-bfloat16] | 0.0932 | 0.0689 | 73.9% | flashinfer |
| 🔴 | **BmmFwdOp** | test_bmm_bench[moe-prefill-b128-bfloat16] | 0.2910 | 0.2154 | 74.0% | torch-cublas |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-uniform-float16] | 0.0608 | 0.0450 | 74.1% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-uniform-bfloat16] | 0.0604 | 0.0448 | 74.1% | fa3 |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-2k-float16] | 0.2814 | 0.2089 | 74.2% | torch-cublas |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-float16] | 0.0929 | 0.0691 | 74.3% | flashinfer |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-bfloat16] | 0.1444 | 0.1078 | 74.6% | fla |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-float16] | 0.6181 | 0.4643 | 75.1% | fla |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-float16] | 0.1655 | 0.1252 | 75.6% | flashinfer |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-bfloat16] | 0.3119 | 0.2361 | 75.7% | fla |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-1k-bfloat16] | 0.0408 | 0.0311 | 76.1% | torch-cublas |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-1k-float16] | 0.0407 | 0.0312 | 76.5% | torch-cublas |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-float16] | 0.3507 | 0.2713 | 77.4% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-float16] | 0.6686 | 0.5179 | 77.5% | flashinfer |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.6673 | 0.5168 | 77.5% | flashinfer |
| 🔴 | **GatedDeltaNetAutogradOp** | test_gated_deltanet_vs_fla_autograd[gdn-autograd-b2-s2k-h4-d64-float16] | 0.0867 | 0.0672 | 77.5% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.3492 | 0.2710 | 77.6% | fa3 |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-float16] | 0.0865 | 0.0672 | 77.6% | fla |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-bfloat16] | 0.0866 | 0.0674 | 77.8% | fla |
| 🔴 | **GatedDeltaNetAutogradOp** | test_gated_deltanet_vs_fla_autograd[gdn-autograd-b2-s2k-h4-d64-bfloat16] | 0.0866 | 0.0674 | 77.8% | fla |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-bfloat16] | 0.6109 | 0.4769 | 78.1% | fla |
| 🔴 | **GatedDeltaNetPrefillBHTDFwdOp** | test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-float16] | 0.2512 | 0.1962 | 78.1% | fla |
| 🔴 | **GatedDeltaNetPrefillBHTDFwdOp** | test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-bfloat16] | 0.2524 | 0.1978 | 78.4% | fla |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-float16] | 0.3132 | 0.2475 | 79.0% | fla |
| 🔴 | **GroupedGemmFwdOp** | test_grouped_gemm_bench[nn-batch16-m4096-n4096-k4096-float16] | 0.3411 | 0.2705 | 79.3% | torch |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-large-bfloat16] | 0.0716 | 0.0569 | 79.5% | torch-compile |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0042 | 0.0034 | 79.5% | mamba |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s4k-h4-d64-float16] | 0.1568 | 0.1253 | 79.9% | fla |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 11 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 797 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 2442 lines in `ops/`, 41.2% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 3518 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

### Never-built kernels

| File | Executed |
| --- | --- |
| `kernels/attention/deepseek_mla_decode.py` | 5.8% |
| `kernels/attention/gqa_fwd_ws.py` | 6.4% |
| `kernels/attention/gqa_fwd_fp8.py` | 9.8% |
| `kernels/attention/gqa_dense.py` | 10.2% |
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
| `ops/attention/gqa.py` | 414 | 31.1% |
| `ops/pool.py` | 150 | 76.3% |
| `ops/moe/staged.py` | 136 | 49.1% |
| `ops/convolution.py` | 120 | 74.1% |
| `ops/linear_attention/gated_deltanet.py` | 114 | 72.9% |
| `ops/reduction/reduce.py` | 100 | 58.5% |
| `ops/op_base.py` | 99 | 60.1% |
| `ops/elementwise/_base.py` | 88 | 76.7% |
| `ops/mamba/mamba2_fwd.py` | 86 | 20.4% |
| `ops/rope.py` | 85 | 70.4% |
| `ops/_roofline_codegen.py` | 82 | 68.8% |
| `ops/moe/contracts.py` | 80 | 55.6% |
| `ops/linear_attention/deltanet.py` | 65 | 63.3% |
| `trace/ui.py` | 62 | 24.4% |

</details>

Per-line detail is in the `htmlcov/` directory of this run's `tileops_op_test` artifact.
