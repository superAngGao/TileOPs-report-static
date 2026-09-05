# ❌ TileOPs Nightly Report

> **2026-08-26 23:04** &ensp;|&ensp; `2c075f6` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Correctness** | ✅ &ensp; (516/516 tests across 92 ops) |
| **Benchmarked Ops** | 191 |
| **Benchmark Failures** | ✅ None &ensp;|&ensp; ⚠️ 13 skipped |
| **Regressions** (vs 14-day median) | ⚠️ 1 |
| **Baseline Alerts** (< 80%) | ⚠️ 213 |
| **Roofline anomalies** | ⚠️ 38 |
| **Never-built kernels** | ⚠️ 9 files &ensp;·&ensp; `kernels/attention/deepseek_mla_decode.py` at 5.8% |
| **Untested roofline math** | 750 lines in `perf/` **+15** &ensp;·&ensp; `perf/formulas.py` at 13.1% |
| **Untested op logic** | 2587 lines in `ops/` **+45** &ensp;·&ensp; 39.3% of branches taken |
| | <sub>coverage compared against the 2026-08-26 run; no figure means it held</sub> |

## ⚠️ Performance Regressions (vs 14-day median)

| Op | Config | Median (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **LogSumExpFwdOp** | test_logsumexp_bench[3d-multidim-reduce-float16] | 0.0126 | 0.0140 | +10.7% | 0.60 |

## ⚠️ Roofline Model Anomalies

> A FAIL row implies a rate above the hardware's theoretical ceiling: its (flops, bytes) formula or declared roof is wrong, and its SOL reading cannot be trusted. A WARN row exceeds the calibrated ceiling; recheck the formula or the calibration.

| Level | Op | Config | Signal |
|:------|:---|:-------|:-------|
| WARN | **AbsFwdOp** | test_abs_bench[elementwise-256M-float16] | 106% of the calibrated ceiling |
| WARN | **AbsFwdOp** | test_abs_bench[elementwise-256M-bfloat16] | 105% of the calibrated ceiling |
| WARN | **BitwiseNotFwdOp** | test_bitwise_not_bench[elementwise-256M-int32] | 106% of the calibrated ceiling |
| WARN | **CeilFwdOp** | test_ceil_bench[elementwise-256M-float16] | 106% of the calibrated ceiling |
| WARN | **CeilFwdOp** | test_ceil_bench[elementwise-256M-bfloat16] | 106% of the calibrated ceiling |
| WARN | **ClampFwdOp** | test_clamp_tensor_bench[elementwise-256M-float16] | 109% of the calibrated ceiling |
| WARN | **ClampFwdOp** | test_clamp_tensor_bench[elementwise-256M-bfloat16] | 109% of the calibrated ceiling |
| WARN | **ClampFwdOp** | test_clamp_tensor_bench[elementwise-256M-min-only-float16] | 107% of the calibrated ceiling |
| WARN | **ClampFwdOp** | test_clamp_tensor_bench[elementwise-256M-min-only-bfloat16] | 107% of the calibrated ceiling |
| WARN | **ClampFwdOp** | test_clamp_tensor_bench[elementwise-256M-max-only-float16] | 107% of the calibrated ceiling |
| WARN | **ClampFwdOp** | test_clamp_tensor_bench[elementwise-256M-max-only-bfloat16] | 108% of the calibrated ceiling |
| WARN | **FloorFwdOp** | test_floor_bench[elementwise-256M-float16] | 106% of the calibrated ceiling |
| WARN | **FloorFwdOp** | test_floor_bench[elementwise-256M-bfloat16] | 106% of the calibrated ceiling |
| WARN | **IsfiniteFwdOp** | test_isfinite_bench[elementwise-256M-float16] | 106% of the calibrated ceiling |
| WARN | **IsfiniteFwdOp** | test_isfinite_bench[elementwise-256M-bfloat16] | 106% of the calibrated ceiling |
| WARN | **IsinfFwdOp** | test_isinf_bench[elementwise-256M-float16] | 106% of the calibrated ceiling |
| WARN | **IsinfFwdOp** | test_isinf_bench[elementwise-256M-bfloat16] | 106% of the calibrated ceiling |
| WARN | **IsnanFwdOp** | test_isnan_bench[elementwise-256M-float16] | 106% of the calibrated ceiling |
| WARN | **IsnanFwdOp** | test_isnan_bench[elementwise-256M-bfloat16] | 106% of the calibrated ceiling |
| WARN | **LerpTensorFwdOp** | test_lerp_tensor_manifest_bench[elementwise-256M-float16] | 109% of the calibrated ceiling |
| WARN | **LerpTensorFwdOp** | test_lerp_tensor_manifest_bench[elementwise-256M-bfloat16] | 109% of the calibrated ceiling |
| WARN | **MaskedFillFwdOp** | test_masked_fill_tensor_manifest_bench[elementwise-256M-float16] | 107% of the calibrated ceiling |
| WARN | **MaskedFillFwdOp** | test_masked_fill_tensor_manifest_bench[elementwise-256M-bfloat16] | 106% of the calibrated ceiling |
| WARN | **MaskedFillScalarFwdOp** | test_masked_fill_scalar_manifest_bench[elementwise-256M-float16] | 106% of the calibrated ceiling |
| WARN | **MaskedFillScalarFwdOp** | test_masked_fill_scalar_manifest_bench[elementwise-256M-bfloat16] | 106% of the calibrated ceiling |
| WARN | **MoeGateUpFwdOp** | test_moe_gate_up_bench[deepseek-v3-decode-gate-up-bfloat16] | 107% of the calibrated ceiling |
| WARN | **MultiHeadAttentionDecodeWithKVCacheFwdOp** | test_mha_decode_bench[llama-8b-32k-float16] | 107% of the calibrated ceiling |
| WARN | **MultiHeadAttentionDecodeWithKVCacheFwdOp** | test_mha_decode_bench[llama-8b-32k-bfloat16] | 108% of the calibrated ceiling |
| WARN | **MultiHeadAttentionDecodeWithKVCacheFwdOp** | test_mha_decode_bench[llama-70b-32k-float16] | 108% of the calibrated ceiling |
| WARN | **MultiHeadAttentionDecodeWithKVCacheFwdOp** | test_mha_decode_bench[llama-70b-32k-bfloat16] | 108% of the calibrated ceiling |
| WARN | **NegFwdOp** | test_neg_bench[elementwise-256M-float16] | 106% of the calibrated ceiling |
| WARN | **NegFwdOp** | test_neg_bench[elementwise-256M-bfloat16] | 106% of the calibrated ceiling |
| WARN | **RoundFwdOp** | test_round_bench[elementwise-256M-float16] | 106% of the calibrated ceiling |
| WARN | **RoundFwdOp** | test_round_bench[elementwise-256M-bfloat16] | 106% of the calibrated ceiling |
| WARN | **TruncFwdOp** | test_trunc_bench[elementwise-256M-float16] | 106% of the calibrated ceiling |
| WARN | **TruncFwdOp** | test_trunc_bench[elementwise-256M-bfloat16] | 106% of the calibrated ceiling |
| WARN | **WhereFwdOp** | test_where_manifest_bench[elementwise-256M-float16] | 108% of the calibrated ceiling |
| WARN | **WhereFwdOp** | test_where_manifest_bench[elementwise-256M-bfloat16] | 108% of the calibrated ceiling |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 80%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-gate-up-block128-float8_e4m3fn] | 0.1482 | 0.0129 | 8.7% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **SharedFusedMoE** | test_shared_fused_moe_bench[1-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 2.5217 | 0.4265 | 16.9% | vllm |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[gemv-down-m1-block128-float8_e4m3fn] | 0.0447 | 0.0078 | 17.4% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[k-dominant-7168x16384-block128-float8_e4m3fn] | 3.5890 | 0.7840 | 21.9% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[large-spatial-float16] | 4.3432 | 1.0183 | 23.4% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-down-block128-float8_e4m3fn] | 0.0378 | 0.0092 | 24.5% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GemmFwdOp** | test_gemm_bench[mid-m96-gate-up-bfloat16] | 0.0687 | 0.0170 | 24.7% | torch-cublas |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-decode-gate-up-bfloat16] | 0.0677 | 0.0173 | 25.5% | torch-cublas |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-attn-proj-block128-float8_e4m3fn] | 0.7706 | 0.2143 | 27.8% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[textcnn-global-float16] | 0.0193 | 0.0057 | 29.5% | torch-compile |
| 🔴 | **Conv3dFwdOp** | test_conv3d_bench[3d-unet-aspp-3x3x3-rate6-float16] | 0.1264 | 0.0376 | 29.8% | torch-compile |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-fc-float16] | 0.0061 | 0.0019 | 30.4% | torch-compile |
| 🔴 | **MaxPool1dFwdOp** | test_max_pool1d_bench[textcnn-global-float16] | 0.0135 | 0.0041 | 30.4% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[small-batch-down-m8-per-tensor-float8_e4m3fn] | 0.0266 | 0.0083 | 31.2% | deepgemm |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-bfloat16] | 0.4566 | 0.1428 | 31.3% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-bfloat16] | 0.4553 | 0.1431 | 31.4% | fa3 |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b4-dmem1024-d512-float16] | 0.0824 | 0.0260 | 31.6% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-down-block128-float8_e4m3fn] | 0.4458 | 0.1439 | 32.3% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **Conv3dFwdOp** | test_conv3d_bench[unet-encoder-k3-s1-bfloat16] | 0.3542 | 0.1154 | 32.6% | torch |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-stage2-float16] | 0.0107 | 0.0035 | 32.6% | torch-compile |
| 🔴 | **Conv3dFwdOp** | test_conv3d_bench[unet-encoder-k3-s1-bias-bfloat16] | 0.3538 | 0.1222 | 34.5% | torch-compile |
| 🔴 | **MeanPoolingForwardOp** | test_mean_pooling_bench[dense-mainstream] | 0.1350 | 0.0470 | 34.8% | torch-view-mean |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-gate-up-block128-float8_e4m3fn] | 0.3850 | 0.1391 | 36.1% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-b64-complex64] | 0.0152 | 0.0056 | 36.8% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[mid-m32-attn-bfloat16] | 0.0661 | 0.0244 | 36.8% | torch-cublas |
| 🔴 | **GemmFwdOp** | test_gemm_bench[mid-m16-attn-bfloat16] | 0.0658 | 0.0245 | 37.2% | torch-cublas |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[wide-n-24576-block128-float8_e4m3fn] | 1.0264 | 0.3828 | 37.3% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-stage3-float16] | 0.0129 | 0.0048 | 37.6% | torch-compile |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-stage1-float16] | 0.0110 | 0.0041 | 37.6% | torch-compile |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[mha-decode-b32-pv-per-tensor-float8_e4m3fn] | 0.0647 | 0.0250 | 38.6% | flashinfer-bmm-fp8 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-short-bfloat16] | 0.4087 | 0.1589 | 38.9% | fa3 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[gemv-down-m1-per-tensor-float8_e4m3fn] | 0.0259 | 0.0101 | 39.2% | deepgemm |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-short-bfloat16] | 0.4155 | 0.1652 | 39.8% | fa3 |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b1-dmem512-d256-float16] | 0.0329 | 0.0132 | 40.0% | torch-compile |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-4096-4096-float16-SiluAndMulFwdKernel-direct] | 0.0662 | 0.0269 | 40.6% | torch-compile |
| 🔴 | **MeanPoolingForwardOp** | test_mean_pooling_bench[dense-batched] | 0.0702 | 0.0285 | 40.6% | torch-view-mean |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-down-per-tensor-float8_e4m3fn] | 0.0254 | 0.0104 | 40.8% | deepgemm |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c128-b64-complex128] | 0.0205 | 0.0085 | 41.4% | torch-cufft |
| 🔴 | **MaximumFwdOp** | test_maximum_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0342 | 0.0142 | 41.4% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-bfloat16] | 1.3124 | 0.5474 | 41.7% | fa3 |
| 🔴 | **MaximumFwdOp** | test_maximum_manifest_bench[cnn-feat-broadcast-float16] | 0.0342 | 0.0143 | 41.9% | torch-compile |
| 🔴 | **MinimumFwdOp** | test_minimum_manifest_bench[cnn-feat-broadcast-float16] | 0.0342 | 0.0144 | 42.0% | torch-compile |
| 🔴 | **MinimumFwdOp** | test_minimum_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0342 | 0.0144 | 42.1% | torch-compile |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-1024-11008-float16-SiluAndMulFwdKernel-direct] | 0.0451 | 0.0190 | 42.3% | torch-compile |
| 🔴 | **MaxPool3dIndicesFwdOp** | test_max_pool3d_indices_bench[c3d-pool1-float16] | 0.3043 | 0.1290 | 42.4% | torch-compile |
| 🔴 | **RopeNeoxPositionIdsFwdOp** | test_rope_neox_position_ids_bench[position-ids-s2k-h32-d128-float16] | 0.0278 | 0.0119 | 42.7% | torch-compile |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[mha-decode-b64-qk-per-tensor-float8_e4m3fn] | 0.1155 | 0.0496 | 42.9% | flashinfer-bmm-fp8 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-prefill-varlen-mixed-fp16] | 0.1401 | 0.0615 | 43.9% | fa3 |
| 🔴 | **SharedFusedMoE** | test_shared_fused_moe_bench[4096-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 32.5292 | 14.4755 | 44.5% | vllm |
| 🔴 | **grouped_gemm_tn** | test_grouped_gemm_bench[tn-batch16-m4096-n4096-k4096-float16] | 0.7808 | 0.3538 | 45.3% | torch |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float16-SiluAndMulFwdKernel-direct] | 0.0178 | 0.0083 | 46.8% | torch-compile |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-bfloat16-SiluAndMulFwdKernel-direct] | 0.0179 | 0.0084 | 47.1% | torch-compile |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-405b-p256-float16] | 0.0563 | 0.0266 | 47.2% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-bfloat16] | 1.2426 | 0.5891 | 47.4% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p256-float16] | 0.1682 | 0.0813 | 48.3% | fa3 |
| 🔴 | **RopeNeoxPositionIdsFwdOp** | test_rope_neox_position_ids_bench[position-ids-s4k-h32-d128-bfloat16] | 0.0456 | 0.0223 | 48.8% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[wide-n-24576-bfloat16] | 0.8996 | 0.4442 | 49.4% | deepgemm |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-small-bfloat16] | 0.0394 | 0.0196 | 49.6% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-bfloat16] | 1.1024 | 0.5475 | 49.7% | fa3 |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-long-k-pressure-float16] | 0.2836 | 0.1410 | 49.7% | marlin-fp16 |
| 🔴 | **GemmFwdOp** | test_gemm_bench[square-1k-nn-bfloat16] | 0.0145 | 0.0072 | 49.8% | torch-cublas |
| 🔴 | **GemmFwdOp** | test_gemm_bench[square-1k-nn-float16] | 0.0145 | 0.0072 | 50.0% | torch-cublas |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-2p7b-b2-s32k-dt-bias-float16] | 0.0444 | 0.0222 | 50.1% | mamba |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-down-per-tensor-float8_e4m3fn] | 0.2103 | 0.1055 | 50.2% | deepgemm |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-70b-prefill-varlen-q-lt-kv-bf16] | 0.1961 | 0.0984 | 50.2% | fa3 |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-dt-bias-bfloat16] | 0.0124 | 0.0064 | 51.4% | mamba |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-gate-up-bfloat16] | 0.3376 | 0.1765 | 52.3% | torch-cublas |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[compile-smoke-rect-128x256x256-float16] | 0.0058 | 0.0031 | 52.6% | torch-dequantized-matmul |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-bfloat16] | 0.0121 | 0.0064 | 53.0% | mamba |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-decode-down-bfloat16] | 0.0246 | 0.0132 | 53.4% | torch-cublas |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-70b-p256-float16] | 0.0684 | 0.0367 | 53.7% | fa3 |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-float16] | 0.0196 | 0.0106 | 54.1% | torch-compile |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-bfloat16] | 0.0195 | 0.0106 | 54.6% | torch-compile |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-non-power2-low-cta-float16] | 0.0743 | 0.0406 | 54.6% | marlin-fp32 |
| 🔴 | **gelu_tanh_and_mul_strategy** | test_fused_gated_strategy_bench[gelu_tanh_and_mul-1024-4096-float16-GeluTanhAndMulFwdKernel-direct] | 0.0178 | 0.0098 | 54.9% | torch-compile |
| 🔴 | **MaxPool3dIndicesFwdOp** | test_max_pool3d_indices_bench[c3d-pool2-float16] | 0.0590 | 0.0325 | 55.1% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-down-bfloat16] | 0.3216 | 0.1797 | 55.9% | deepgemm |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 1.0192 | 0.5784 | 56.8% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-prefill-varlen-uniform-fp16] | 0.1250 | 0.0713 | 57.1% | fa3 |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-medium-bfloat16] | 0.0544 | 0.0314 | 57.7% | torch-compile |
| 🔴 | **RopeLongRopeFwdOp** | test_rope_longrope_bench[longrope-2d-b1-s8k-h32-d128-float16] | 0.0594 | 0.0348 | 58.6% | torch-compile |
| 🔴 | **gelu_and_mul_strategy** | test_fused_gated_strategy_bench[gelu_and_mul-1024-4096-float16-GeluAndMulFwdKernel-direct] | 0.0182 | 0.0107 | 58.6% | torch-compile |
| 🔴 | **RopeYarnFwdOp** | test_rope_yarn_bench[yarn-2d-b1-s8k-h32-d128-float16] | 0.0594 | 0.0348 | 58.6% | torch-compile |
| 🔴 | **RopeLlama31FwdOp** | test_rope_llama31_bench[llama31-2d-b1-s8k-h32-d128-float16] | 0.0594 | 0.0348 | 58.7% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-float16] | 0.2438 | 0.1434 | 58.8% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-float16] | 0.2436 | 0.1435 | 58.9% | fa3 |
| 🔴 | **TopkSelectorFwdOp** | test_topk_selector_bench[topk1024-s32k-kv64k-float32] | 15.6212 | 9.2722 | 59.4% | flashinfer |
| 🔴 | **SharedFusedMoE** | test_shared_fused_moe_bench[2048-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 19.5167 | 11.6330 | 59.6% | vllm |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[throughput-8b-p64-float16] | 0.2518 | 0.1506 | 59.8% | flashinfer |
| 🔴 | **RopeNeoxFwdOp** | test_rope_neox_bench[neox-2d-b2-s2k-h32-d128-float16] | 0.0308 | 0.0185 | 59.9% | torch-compile |
| 🔴 | **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[ecg-cnn-dilated-bfloat16] | 0.0224 | 0.0134 | 59.9% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[k-dominant-7168x16384-bfloat16] | 2.0590 | 1.2577 | 61.1% | deepgemm |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-float16] | 0.9029 | 0.5516 | 61.1% | fa3 |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-attn-proj-float16] | 0.5446 | 0.3342 | 61.4% | torch-cublas |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-float16] | 0.6359 | 0.3908 | 61.5% | fla |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-attn-proj-bfloat16] | 0.5399 | 0.3318 | 61.5% | torch-cublas |
| 🔴 | **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[global-1x1-float16] | 0.0133 | 0.0082 | 61.5% | torch-compile |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-bfloat16] | 0.6378 | 0.3934 | 61.7% | fla |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-float16] | 0.8924 | 0.5507 | 61.7% | fa3 |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-float16] | 0.1122 | 0.0693 | 61.8% | torch-compile |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-bfloat16] | 0.1122 | 0.0700 | 62.4% | torch-compile |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-hbm-streaming-threshold-float16] | 0.0606 | 0.0379 | 62.6% | marlin-fp32 |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s896-float16] | 0.0453 | 0.0284 | 62.6% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s896-bfloat16] | 0.0454 | 0.0284 | 62.6% | fa3 |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[compile-smoke-square-64x64x128-float16] | 0.0043 | 0.0027 | 62.7% | torch-dequantized-matmul |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b8-dmem512-d256-bfloat16] | 0.0334 | 0.0212 | 63.4% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[mid-m64-down-bfloat16] | 0.0207 | 0.0132 | 63.8% | torch-cublas |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-float16] | 1.4273 | 0.9213 | 64.5% | fla |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-float32] | 0.0195 | 0.0126 | 64.6% | torch-compile |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-bfloat16] | 0.3166 | 0.2055 | 64.9% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-bfloat16] | 1.4652 | 0.9541 | 65.1% | fla |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-float16] | 0.3140 | 0.2050 | 65.3% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-float16] | 0.3809 | 0.2495 | 65.5% | fla |
| 🔴 | **TopkSelectorFwdOp** | test_topk_selector_bench[topk2048-s32k-kv64k-float32] | 16.2611 | 10.6741 | 65.6% | flashinfer |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-unbatched-complex64] | 0.0082 | 0.0054 | 66.3% | torch-cufft |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-l2-resident-ish-float16] | 0.0329 | 0.0218 | 66.3% | marlin-fp16 |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-float16] | 0.2017 | 0.1337 | 66.3% | fla |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-float32] | 0.1074 | 0.0715 | 66.5% | torch-compile |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s1792-bfloat16] | 0.1288 | 0.0858 | 66.6% | fa3 |
| 🔴 | **AvgPool1dFwdOp** | test_avg_pool1d_bench[ceil-bfloat16] | 0.0035 | 0.0023 | 66.7% | torch-compile |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-bfloat16] | 0.3876 | 0.2585 | 66.7% | fla |
| 🔴 | **GroupNormFwdOp** | test_group_norm_bench[wider-channel-g32-affine-float16] | 0.0059 | 0.0040 | 66.8% | flaggems |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s1792-float16] | 0.1286 | 0.0860 | 66.9% | fa3 |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-bfloat16] | 0.7502 | 0.5021 | 66.9% | fla |
| 🔴 | **GroupNormFwdOp** | test_group_norm_no_affine_bench[tail-spatial-g16-float16] | 0.0052 | 0.0035 | 67.1% | torch-compile |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-float16] | 0.7246 | 0.4866 | 67.2% | fla |
| 🔴 | **GroupNormFwdOp** | test_group_norm_bench[tail-spatial-g16-affine-float16] | 0.0060 | 0.0041 | 67.2% | flaggems |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-bfloat16] | 0.0968 | 0.0658 | 68.0% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-bfloat16] | 0.2049 | 0.1401 | 68.3% | fla |
| 🔴 | **GeFwdOp** | test_ge_manifest_bench[cnn-feat-broadcast-float16] | 0.0172 | 0.0118 | 68.5% | torch-compile |
| 🔴 | **FusedAddRMSNormFwdOp** | test_fused_add_rms_norm_bench[llama-405b-decode-bfloat16] | 0.0062 | 0.0043 | 68.6% | flashinfer |
| 🔴 | **LeFwdOp** | test_le_manifest_bench[cnn-feat-broadcast-float16] | 0.0173 | 0.0119 | 68.6% | torch-compile |
| 🔴 | **LtFwdOp** | test_lt_manifest_bench[cnn-feat-broadcast-float16] | 0.0172 | 0.0118 | 68.9% | torch-compile |
| 🔴 | **LeFwdOp** | test_le_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0172 | 0.0119 | 68.9% | torch-compile |
| 🔴 | **NeFwdOp** | test_ne_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0172 | 0.0118 | 69.0% | torch-compile |
| 🔴 | **LogicalOrFwdOp** | test_logical_or_manifest_bench[cnn-feat-broadcast-float16] | 0.0174 | 0.0120 | 69.1% | torch-compile |
| 🔴 | **EqFwdOp** | test_eq_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0172 | 0.0119 | 69.2% | torch-compile |
| 🔴 | **GtFwdOp** | test_gt_manifest_bench[cnn-feat-broadcast-float16] | 0.0172 | 0.0119 | 69.2% | torch-compile |
| 🔴 | **NeFwdOp** | test_ne_manifest_bench[cnn-feat-broadcast-float16] | 0.0172 | 0.0119 | 69.3% | torch-compile |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[moe-prefill-b128-per-tensor-float8_e4m3fn] | 0.9007 | 0.6240 | 69.3% | flashinfer-bmm-fp8 |
| 🔴 | **EqFwdOp** | test_eq_manifest_bench[cnn-feat-broadcast-float16] | 0.0172 | 0.0119 | 69.3% | torch-compile |
| 🔴 | **LogicalOrFwdOp** | test_logical_or_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0174 | 0.0121 | 69.5% | torch-compile |
| 🔴 | **GtFwdOp** | test_gt_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0173 | 0.0120 | 69.5% | torch-compile |
| 🔴 | **LogicalAndFwdOp** | test_logical_and_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0172 | 0.0120 | 69.7% | torch-compile |
| 🔴 | **GeFwdOp** | test_ge_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0172 | 0.0120 | 69.8% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-bfloat16] | 0.3120 | 0.2197 | 70.4% | fla |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s3584-bfloat16] | 0.7508 | 0.5299 | 70.6% | fa3 |
| 🔴 | **LogicalAndFwdOp** | test_logical_and_manifest_bench[cnn-feat-broadcast-float16] | 0.0172 | 0.0122 | 70.6% | torch-compile |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s3584-float16] | 0.7486 | 0.5288 | 70.6% | fa3 |
| 🔴 | **LtFwdOp** | test_lt_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0172 | 0.0122 | 70.7% | torch-compile |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-softcap50-float16] | 0.1765 | 0.1255 | 71.1% | flashinfer |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s7168-bfloat16] | 2.8493 | 2.0276 | 71.2% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s7168-float16] | 2.8457 | 2.0263 | 71.2% | fa3 |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s16k-h4-d64-float16] | 1.5171 | 1.0813 | 71.3% | fla |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-float16] | 0.0984 | 0.0702 | 71.4% | fla |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-float16] | 0.8302 | 0.5937 | 71.5% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.8084 | 0.5813 | 71.9% | fa3 |
| 🔴 | **MaxPool2dFwdOp** | test_max_pool2d_bench[resnet-stem-float16] | 0.0471 | 0.0340 | 72.1% | torch-compile |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-float16] | 0.1488 | 0.1076 | 72.4% | fla |
| 🔴 | **MaxPool2dFwdOp** | test_max_pool2d_bench[resnet-stem-bfloat16] | 0.0470 | 0.0341 | 72.5% | torch-compile |
| 🔴 | **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[nondiv-7x7-bfloat16] | 0.0158 | 0.0115 | 72.5% | torch-compile |
| 🔴 | **LogSumExpFwdOp** | test_logsumexp_bench[3d-multidim-reduce-float16] | 0.0140 | 0.0101 | 72.5% | torch-compile |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-float16] | 0.0569 | 0.0413 | 72.5% | flashinfer |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0568 | 0.0412 | 72.6% | flashinfer |
| 🔴 | **GroupNormFwdOp** | test_group_norm_no_affine_bench[wider-channel-g32-float16] | 0.0048 | 0.0035 | 72.7% | flaggems |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float32-SiluAndMulFwdKernel-direct] | 0.0201 | 0.0146 | 72.9% | torch-compile |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-2k-float16] | 0.2839 | 0.2078 | 73.2% | torch-cublas |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-2k-bfloat16] | 0.2797 | 0.2056 | 73.5% | torch-cublas |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[alexnet-ceil-bfloat16] | 0.0237 | 0.0174 | 73.5% | torch-compile |
| 🔴 | **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[sincnet-speaker-local-float16] | 0.0218 | 0.0161 | 73.8% | torch-compile |
| 🔴 | **CountNonzeroFwdOp** | test_count_nonzero_bench[3d-multidim-reduce-float16] | 0.0064 | 0.0047 | 73.9% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-bfloat16] | 0.6116 | 0.4519 | 73.9% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-float16] | 0.0933 | 0.0690 | 73.9% | flashinfer |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b4-4k-bfloat16] | 1.0435 | 0.7726 | 74.1% | torch-cublas |
| 🔴 | **BmmFwdOp** | test_bmm_bench[moe-prefill-b128-bfloat16] | 0.2907 | 0.2164 | 74.4% | torch-cublas |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[alexnet-ceil-float16] | 0.0237 | 0.0177 | 74.5% | torch-compile |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s16k-h4-d64-bfloat16] | 1.4514 | 1.0813 | 74.5% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-bfloat16] | 0.0927 | 0.0692 | 74.6% | flashinfer |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s8k-h4-d64-float16] | 0.7455 | 0.5572 | 74.7% | fla |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-bfloat16] | 0.1445 | 0.1082 | 74.9% | fla |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-float16] | 0.1669 | 0.1252 | 75.0% | flashinfer |
| 🔴 | **Conv2dFwdOp** | test_conv2d_bench[highres-3x3-s1-bias-float16] | 0.1052 | 0.0790 | 75.1% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-float16] | 0.6181 | 0.4644 | 75.1% | fla |
| 🔴 | **Conv3dFwdOp** | test_conv3d_bench[video-stage-downsample-k3-s2-float16] | 0.0349 | 0.0263 | 75.4% | torch-compile |
| 🔴 | **RopeNonNeoxFwdOp** | test_rope_non_neox_bench[non-neox-2d-b2-s2k-h32-d128-bfloat16] | 0.0252 | 0.0190 | 75.5% | torch-compile |
| 🔴 | **Conv2dFwdOp** | test_conv2d_bench[highres-3x3-s1-float16] | 0.1049 | 0.0792 | 75.5% | torch-compile |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-1k-float16] | 0.0406 | 0.0310 | 76.2% | torch-cublas |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-1k-bfloat16] | 0.0408 | 0.0312 | 76.4% | torch-cublas |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s4k-h4-d64-bfloat16] | 0.1564 | 0.1195 | 76.4% | fla |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s8k-h4-d64-bfloat16] | 0.7262 | 0.5573 | 76.8% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-float16] | 0.3513 | 0.2719 | 77.4% | fa3 |
| 🔴 | **DeltaNetFwdOp** | test_deltanet_vs_fla_fwd[dn-b2-s16k-h4-d64-float16] | 0.4732 | 0.3662 | 77.4% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.3497 | 0.2709 | 77.5% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.6675 | 0.5174 | 77.5% | flashinfer |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-float16] | 0.0865 | 0.0672 | 77.7% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-float16] | 0.6693 | 0.5207 | 77.8% | flashinfer |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-bfloat16] | 0.0867 | 0.0675 | 77.8% | fla |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s4k-h4-d64-float16] | 0.3692 | 0.2880 | 78.0% | fla |
| 🔴 | **GatedDeltaNetPrefillBHTDFwdOp** | test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-float16] | 0.2511 | 0.1961 | 78.1% | fla |
| 🔴 | **DeltaNetFwdOp** | test_deltanet_vs_fla_fwd[dn-b2-s16k-h4-d64-bfloat16] | 0.4733 | 0.3699 | 78.2% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowFwdOp** | test_gqa_sliding_window_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.1513 | 0.1183 | 78.2% | fa3 |
| 🔴 | **SumFwdOp** | test_sum_bench[3d-multidim-reduce-float16] | 0.0057 | 0.0045 | 78.2% | torch-compile |
| 🔴 | **GroupedQueryAttentionSlidingWindowFwdOp** | test_gqa_sliding_window_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.1512 | 0.1183 | 78.3% | fa3 |
| 🔴 | **GatedDeltaNetPrefillBHTDFwdOp** | test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-bfloat16] | 0.2527 | 0.1981 | 78.4% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowFwdOp** | test_gqa_sliding_window_fwd_bench[llama-70b-long-w1024-float16] | 0.1528 | 0.1200 | 78.6% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowFwdOp** | test_gqa_sliding_window_fwd_bench[llama-8b-long-w1024-float16] | 0.1525 | 0.1201 | 78.7% | fa3 |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0042 | 0.0033 | 78.8% | mamba |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s4k-h4-d64-bfloat16] | 0.3648 | 0.2877 | 78.9% | fla |
| 🔴 | **grouped_gemm_nn** | test_grouped_gemm_bench[nn-batch16-m4096-n4096-k4096-float16] | 0.3406 | 0.2689 | 79.0% | torch |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-large-bfloat16] | 0.0715 | 0.0567 | 79.2% | torch-compile |
| 🔴 | **Conv2dFwdOp** | test_conv2d_bench[classifier-1x1-float16] | 0.0091 | 0.0072 | 79.3% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-float16] | 0.3127 | 0.2482 | 79.3% | fla |
| 🔴 | **Conv3dFwdOp** | test_conv3d_bench[video-stage-downsample-k3-s2-bias-float16] | 0.0353 | 0.0281 | 79.6% | torch-compile |

<details>
<summary><strong>Full Correctness Results (92 ops)</strong></summary>

| | Op | Module | Pass | Fail | Skip | Max Error |
|:-|:---|:-------|-----:|-----:|-----:|----------:|
| ✅ | AdaLayerNormFwdOp | `tileops.ops.norm.ada_layer_norm` | 8 | 0 | 0 | 1.56e-02 |
| ✅ | AdaLayerNormZeroFwdOp | `tileops.ops.norm.ada_layer_norm_zero` | 8 | 0 | 0 | 1.56e-02 |
| ✅ | AdaptiveAvgPool2dFwdOp | `tileops.ops.pool` | 4 | 0 | 0 | - |
| ✅ | AdaptiveMaxPool2dIndicesFwdOp | `tileops.ops.pool` | 2 | 0 | 0 | - |
| ✅ | AddFwdKernel | `tileops.kernels.elementwise.arithmetic` | 1 | 0 | 0 | - |
| ✅ | AddFwdOp | `tileops.ops.elementwise.arithmetic` | 4 | 0 | 0 | - |
| ✅ | AllFwdOp | `tileops.ops.reduction.logical_reduce` | 7 | 0 | 0 | - |
| ✅ | AmaxFwdOp | `tileops.ops.reduction.reduce` | 5 | 0 | 0 | - |
| ✅ | AminFwdOp | `tileops.ops.reduction.reduce` | 5 | 0 | 0 | - |
| ✅ | AnyFwdOp | `tileops.ops.reduction.logical_reduce` | 7 | 0 | 0 | - |
| ✅ | ArgmaxFwdOp | `tileops.ops.reduction.argreduce` | 5 | 0 | 0 | - |
| ✅ | ArgminFwdOp | `tileops.ops.reduction.argreduce` | 5 | 0 | 0 | - |
| ✅ | AvgPool1dFwdOp | `tileops.ops.pool` | 2 | 0 | 0 | - |
| ✅ | AvgPool2dFwdOp | `tileops.ops.pool` | 7 | 0 | 0 | - |
| ✅ | AvgPool3dFwdOp | `tileops.ops.pool` | 2 | 0 | 0 | - |
| ✅ | BitwiseAndFwdOp | `tileops.ops.elementwise.bitwise` | 1 | 0 | 0 | - |
| ✅ | BitwiseOrFwdOp | `tileops.ops.elementwise.bitwise` | 1 | 0 | 0 | - |
| ✅ | BitwiseXorFwdOp | `tileops.ops.elementwise.bitwise` | 1 | 0 | 0 | - |
| ✅ | BmmFp8KNFwdOp | `tileops.ops.gemm.bmm` | 2 | 0 | 0 | 3.12e-02 |
| ✅ | BmmFwdOp | `tileops.ops.gemm.bmm` | 9 | 0 | 0 | - |
| ✅ | Conv1dFwdOp | `tileops.ops.convolution` | 11 | 0 | 0 | 1.25e-01 |
| ✅ | Conv2dFwdOp | `tileops.ops.convolution` | 11 | 0 | 0 | 6.25e-02 |
| ✅ | Conv3dFwdOp | `tileops.ops.convolution` | 5 | 0 | 0 | 5.00e-01 |
| ✅ | CountNonzeroFwdOp | `tileops.ops.reduction.logical_reduce` | 7 | 0 | 0 | - |
| ✅ | CumprodFwdOp | `tileops.ops.reduction.cumulative` | 5 | 0 | 0 | 1.95e-03 |
| ✅ | CumsumFwdOp | `tileops.ops.reduction.cumulative` | 5 | 0 | 0 | 5.00e-01 |
| ✅ | DaCumsumFwdOp | `tileops.ops.mamba.da_cumsum` | 4 | 0 | 0 | 6.10e-05 |
| ✅ | DeepSeekSparseAttentionDecodeWithKVCacheFwdOp | `tileops.ops.attention.deepseek_dsa` | 1 | 0 | 0 | 2.44e-04 |
| ✅ | DeltaNetDecodeFwdOp | `tileops.ops.linear_attention.deltanet_recurrence` | 6 | 0 | 0 | 9.54e-07 |
| ✅ | EngramDecodeFwdOp | `tileops.ops.sequence_modeling.engram_decode` | 2 | 0 | 0 | 1.56e-02 |
| ✅ | EngramGateConvBwdOp | `tileops.ops.sequence_modeling.engram` | 3 | 0 | 0 | 1.51e-03 |
| ✅ | EngramGateConvFwdOp | `tileops.ops.sequence_modeling.engram` | 2 | 0 | 0 | 1.77e-02 |
| ✅ | FFTC2CFwdOp | `tileops.ops.fft` | 7 | 0 | 0 | 7.86e-05 |
| ✅ | FP8LightningIndexerFwdOp | `tileops.ops.fp8_lightning_indexer` | 1 | 0 | 0 | - |
| ✅ | FP8QuantFwdOp | `tileops.ops.fp8_quant` | 4 | 0 | 0 | 3.20e+01 |
| ✅ | FusedAddLayerNormFwdOp | `tileops.ops.norm.fused_add_layer_norm` | 8 | 0 | 0 | 6.25e-02 |
| ✅ | FusedAddRMSNormFwdOp | `tileops.ops.norm.fused_add_rms_norm` | 8 | 0 | 0 | 3.12e-02 |
| ✅ | GLADecodeFwdOp | `tileops.ops.linear_attention.gla_recurrence` | 4 | 0 | 0 | 3.05e-05 |
| ✅ | GatedDeltaNetDecodeFwdOp | `tileops.ops.linear_attention.gated_deltanet` | 5 | 0 | 0 | 4.88e-04 |
| ✅ | GatedDeltaNetPrefillBHTDFwdOp | `tileops.ops.linear_attention.gated_deltanet` | 2 | 0 | 0 | 3.05e-05 |
| ✅ | GeluAndMulFwdOp | `tileops.ops.elementwise.activations` | 1 | 0 | 0 | 7.81e-03 |
| ✅ | GeluTanhAndMulFwdOp | `tileops.ops.elementwise.activations` | 1 | 0 | 0 | 7.81e-03 |
| ✅ | GemmFp8FwdOp | `tileops.ops.gemm.gemm` | 3 | 0 | 0 | 3.12e-02 |
| ✅ | GemmFwdOp | `tileops.ops.gemm.gemm` | 17 | 0 | 0 | 1.00e+00 |
| ✅ | GemmW4A16FwdOp | `tileops.ops.gemm.gemm` | 1 | 0 | 0 | 1.56e-02 |
| ✅ | GroupNormFwdOp | `tileops.ops.norm.group_norm` | 11 | 0 | 0 | 1.95e-03 |
| ✅ | GroupedGemmFwdOp | `tileops.ops.gemm.grouped_gemm` | 3 | 0 | 0 | - |
| ✅ | GroupedQueryAttentionBwdOp | `tileops.ops.attention.gqa` | 2 | 0 | 0 | 3.91e-03 |
| ✅ | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | `tileops.ops.attention.gqa` | 6 | 0 | 0 | 2.44e-04 |
| ✅ | GroupedQueryAttentionDecodeWithKVCacheFwdOp | `tileops.ops.attention.gqa` | 1 | 0 | 0 | 1.30e-04 |
| ✅ | GroupedQueryAttentionFwdOp | `tileops.ops.attention.gqa` | 2 | 0 | 0 | 1.95e-03 |
| ✅ | GroupedQueryAttentionSlidingWindowFwdOp | `tileops.ops.attention.gqa` | 12 | 0 | 0 | 2.44e-04 |
| ✅ | GroupedQueryAttentionSlidingWindowVarlenFwdOp | `tileops.ops.attention.gqa` | 12 | 0 | 0 | 2.44e-04 |
| ✅ | InfNormFwdOp | `tileops.ops.reduction.vector_norm` | 5 | 0 | 0 | - |
| ✅ | InstanceNormFwdOp | `tileops.ops.norm.instance_norm` | 5 | 0 | 0 | 4.77e-07 |
| ✅ | L1NormFwdOp | `tileops.ops.reduction.vector_norm` | 5 | 0 | 0 | 3.05e-05 |
| ✅ | L2NormFwdOp | `tileops.ops.reduction.vector_norm` | 5 | 0 | 0 | 1.91e-06 |
| ✅ | LayerNormFwdOp | `tileops.ops.norm.layer_norm` | 14 | 0 | 0 | 3.12e-02 |
| ✅ | LogSoftmaxFwdOp | `tileops.ops.reduction.softmax` | 24 | 0 | 0 | 7.81e-03 |
| ✅ | LogSumExpFwdOp | `tileops.ops.reduction.softmax` | 26 | 0 | 0 | 4.77e-07 |
| ✅ | MHCPostFwdOp | `tileops.ops.sequence_modeling.mhc` | 2 | 0 | 0 | - |
| ✅ | MHCPreFwdOp | `tileops.ops.sequence_modeling.mhc` | 2 | 0 | 0 | 3.12e-02 |
| ✅ | MaxPool1dIndicesFwdOp | `tileops.ops.pool` | 4 | 0 | 0 | - |
| ✅ | MaxPool2dIndicesFwdOp | `tileops.ops.pool` | 4 | 0 | 0 | - |
| ✅ | MaxPool3dIndicesFwdOp | `tileops.ops.pool` | 4 | 0 | 0 | - |
| ✅ | MeanFwdOp | `tileops.ops.reduction.reduce` | 5 | 0 | 0 | - |
| ✅ | MeanPoolingForwardOp | `tileops.ops.pool` | 5 | 0 | 0 | 3.05e-05 |
| ✅ | MultiHeadAttentionBwdOp | `tileops.ops.attention.mha` | 2 | 0 | 0 | 1.95e-03 |
| ✅ | MultiHeadAttentionDecodePagedWithKVCacheFwdOp | `tileops.ops.attention.mha` | 3 | 0 | 0 | 1.22e-04 |
| ✅ | MultiHeadAttentionDecodeWithKVCacheFwdOp | `tileops.ops.attention.mha` | 1 | 0 | 0 | 9.77e-04 |
| ✅ | MultiHeadAttentionFwdOp | `tileops.ops.attention.mha` | 2 | 0 | 0 | 9.77e-04 |
| ✅ | NSAFwdVarlenOp | `tileops.ops.attention.deepseek_nsa` | 2 | 0 | 0 | 4.88e-04 |
| ✅ | ProdFwdOp | `tileops.ops.reduction.reduce` | 6 | 0 | 0 | - |
| ✅ | RMSNormFwdOp | `tileops.ops.norm.rms_norm` | 10 | 0 | 0 | 3.12e-02 |
| ✅ | ReluFwdKernel | `tileops.kernels.elementwise.activations` | 2 | 0 | 0 | - |
| ✅ | ReluFwdOp | `tileops.ops.elementwise.activations` | 2 | 0 | 0 | - |
| ✅ | RopeLlama31FwdOp | `tileops.ops.rope` | 2 | 0 | 0 | 1.95e-03 |
| ✅ | RopeLongRopeFwdOp | `tileops.ops.rope` | 2 | 0 | 0 | 3.91e-03 |
| ✅ | RopeNeoxFwdOp | `tileops.ops.rope` | 3 | 0 | 0 | 3.91e-03 |
| ✅ | RopeNonNeoxFwdOp | `tileops.ops.rope` | 3 | 0 | 0 | 3.91e-03 |
| ✅ | RopeYarnFwdOp | `tileops.ops.rope` | 2 | 0 | 0 | 1.95e-03 |
| ✅ | SSDChunkScanFwdOp | `tileops.ops.mamba.ssd_chunk_scan` | 2 | 0 | 0 | 3.02e-04 |
| ✅ | SSDChunkStateFwdOp | `tileops.ops.mamba.ssd_chunk_state` | 3 | 0 | 0 | 2.19e-05 |
| ✅ | SSDStatePassingFwdOp | `tileops.ops.mamba.ssd_state_passing` | 2 | 0 | 0 | 2.98e-08 |
| ✅ | SiluAndMulFwdOp | `tileops.ops.elementwise.activations` | 2 | 0 | 0 | 3.91e-03 |
| ✅ | SoftmaxFwdOp | `tileops.ops.reduction.softmax` | 24 | 0 | 0 | 7.63e-06 |
| ✅ | StdFwdOp | `tileops.ops.reduction.reduce` | 17 | 0 | 0 | - |
| ✅ | SumFwdOp | `tileops.ops.reduction.reduce` | 6 | 0 | 0 | - |
| ✅ | TopkSelectorFwdOp | `tileops.ops.topk_selector` | 3 | 0 | 0 | 1.31e+05 |
| ✅ | VarFwdOp | `tileops.ops.reduction.reduce` | 19 | 0 | 0 | - |
| ✅ | VarMeanFwdOp | `tileops.ops.reduction.reduce` | 17 | 0 | 0 | - |
| ✅ | function | `builtins` | 10 | 0 | 0 | 3.91e-03 |

</details>

<details>
<summary><strong>Full Benchmark Results (1137 configs across 191 ops)</strong></summary>

> SOL = algorithmic speed-of-light efficiency: `max(bytes/BW, flops/roof) / device-busy` against the calibrated ceilings. `bytes` is the algorithm's minimum traffic (not measured DRAM bytes); `flops` follows the TileOPs counting convention; the roof is the unit an optimal implementation would use, not the running kernel's. M/C = memory/compute-bound; ✅ at ≥90% (M) / ≥80% (C); lat-bound rows are too small for the model to judge.

| | Op | Config | Device busy (ms) | TFLOPS | BW (TB/s) | SOL | Via | Ratio |
|:-|:---|:-------|------------:|-------:|----------:|----:|:----|------:|
| 🔵 | AbsFwdOp | test_abs_bench[elementwise-16M-float16] | 0.0179 | 0.94 | 3.76 | ✅ 92% M | torch 100.5%, torch-compile 100.2% | - |
| 🔵 | AbsFwdOp | test_abs_bench[elementwise-16M-bfloat16] | 0.0179 | 0.94 | 3.75 | ✅ 92% M | torch 100.2%, torch-compile 100.2% | - |
| 🟡 | AbsFwdOp | test_abs_bench[elementwise-16M-float32] | 0.0340 | 0.49 | 3.95 | ✅ 97% M | torch 100.0%, torch-compile 99.8% | - |
| 🟡 | AbsFwdOp | test_abs_bench[elementwise-256M-float16] | 0.2499 | 1.07 | 4.30 | ⚠️ 106% M | torch 99.9%, torch-compile 99.9% | - |
| 🟡 | AbsFwdOp | test_abs_bench[elementwise-256M-bfloat16] | 0.2501 | 1.07 | 4.29 | ⚠️ 105% M | torch 99.8%, torch-compile 99.8% | - |
| 🔵 | AdaLayerNormFwdOp | test_ada_layer_norm_bench[dit-xl-2-float16] | 0.0052 | 1.12 | 1.80 | <sub>lat-bound</sub> | torch-ref 231.1%, torch-compile 145.1% | - |
| 🔵 | AdaLayerNormFwdOp | test_ada_layer_norm_bench[dit-xl-2-bfloat16] | 0.0053 | 1.10 | 1.77 | <sub>lat-bound</sub> | torch-ref 226.9%, torch-compile 146.1% | - |
| 🔵 | AdaLayerNormFwdOp | test_ada_layer_norm_bench[llama-8b-prefill-float16] | 0.0198 | 2.12 | 3.39 | 83% M | torch-ref 209.0%, torch-compile 128.9% | - |
| 🔵 | AdaLayerNormFwdOp | test_ada_layer_norm_bench[llama-8b-prefill-bfloat16] | 0.0199 | 2.11 | 3.38 | 83% M | torch-ref 210.2%, torch-compile 132.8% | - |
| 🔵 | AdaLayerNormFwdOp | test_ada_layer_norm_bench[llama-8b-decode-bfloat16] | 0.0027 | 0.01 | 0.01 | <sub>lat-bound</sub> | torch-ref 389.6%, torch-compile 114.4% | - |
| 🔵 | AdaLayerNormZeroFwdOp | test_ada_layer_norm_zero_bench[dit-xl-2-float16] | 0.0062 | 1.14 | 1.90 | <sub>lat-bound</sub> | torch-ref 237.6%, torch-compile 125.3% | - |
| 🔵 | AdaLayerNormZeroFwdOp | test_ada_layer_norm_zero_bench[dit-xl-2-bfloat16] | 0.0062 | 1.14 | 1.90 | <sub>lat-bound</sub> | torch-ref 238.2%, torch-compile 130.9% | - |
| 🔵 | AdaLayerNormZeroFwdOp | test_ada_layer_norm_zero_bench[llama-8b-prefill-float16] | 0.0248 | 2.03 | 3.38 | 83% M | torch-ref 214.7%, torch-compile 110.7% | - |
| 🔵 | AdaLayerNormZeroFwdOp | test_ada_layer_norm_zero_bench[llama-8b-prefill-bfloat16] | 0.0247 | 2.04 | 3.40 | 84% M | torch-ref 217.2%, torch-compile 114.0% | - |
| 🔵 | AdaLayerNormZeroFwdOp | test_ada_layer_norm_zero_bench[llama-8b-decode-bfloat16] | 0.0028 | 0.01 | 0.01 | <sub>lat-bound</sub> | torch-ref 409.1%, torch-compile 113.5% | - |
| 🔵 | AdaptiveAvgPool2dFwdOp | test_adaptive_avg_pool2d_bench[resnet-global-float16] | 0.0030 | 0.27 | 0.55 | <sub>lat-bound</sub> | torch-ref 247.3%, torch-compile 124.7% | - |
| 🟢 | AdaptiveAvgPool2dFwdOp | test_adaptive_avg_pool2d_bench[spp-6x6-float16] | 0.0054 | 0.17 | 0.30 | <sub>lat-bound</sub> | torch-ref 197.6%, torch-compile 197.6% | - |
| 🔵 | AdaptiveAvgPool2dFwdOp | test_adaptive_avg_pool2d_bench[nondiv-7x7-bfloat16] | 0.0066 | 0.07 | 0.12 | <sub>lat-bound</sub> | torch-ref 138.8%, torch-compile 138.8% | - |
| 🔵 | AdaptiveMaxPool2dFwdOp | test_adaptive_max_pool2d_bench[global-1x1-float16] | 0.0029 | 0.27 | 0.56 | <sub>lat-bound</sub> | torch-ref 1528.3%, torch-compile 128.3% | - |
| 🟢 | AdaptiveMaxPool2dFwdOp | test_adaptive_max_pool2d_bench[spp-6x6-float16] | 0.0060 | 0.15 | 0.27 | <sub>lat-bound</sub> | torch-ref 237.3%, torch-compile 237.3% | - |
| 🟢 | AdaptiveMaxPool2dFwdOp | test_adaptive_max_pool2d_bench[nondiv-7x7-bfloat16] | 0.0065 | 0.08 | 0.13 | <sub>lat-bound</sub> | torch-ref 176.8%, torch-compile 176.3% | - |
| 🔴 | AdaptiveMaxPool2dIndicesFwdOp | test_adaptive_max_pool2d_indices_bench[global-1x1-float16] | 0.0133 | 0.06 | 0.13 | <sub>lat-bound</sub> | torch-ref 338.3%, torch-compile 61.5% | - |
| 🟡 | AdaptiveMaxPool2dIndicesFwdOp | test_adaptive_max_pool2d_indices_bench[spp-6x6-float16] | 0.0154 | 0.06 | 0.11 | <sub>lat-bound</sub> | torch-ref 92.7%, torch-compile 92.8% | - |
| 🔴 | AdaptiveMaxPool2dIndicesFwdOp | test_adaptive_max_pool2d_indices_bench[nondiv-7x7-bfloat16] | 0.0158 | 0.03 | 0.05 | <sub>lat-bound</sub> | torch-ref 72.7%, torch-compile 72.5% | - |
| 🔵 | AddFwdOp | test_add_manifest_bench[hidden-state-prefill-float16] | 0.0147 | 1.14 | 3.43 | 84% M | torch 101.3%, torch-compile 100.2% | - |
| 🔵 | AddFwdOp | test_add_manifest_bench[hidden-state-prefill-bfloat16] | 0.0147 | 1.14 | 3.43 | 84% M | torch 101.5%, torch-compile 100.3% | - |
| 🟡 | AddFwdOp | test_add_manifest_bench[hidden-state-prefill-float32] | 0.0265 | 0.63 | 3.80 | ✅ 93% M | torch 100.1%, torch-compile 99.9% | - |
| 🟡 | AddFwdOp | test_add_manifest_bench[cnn-feat-broadcast-float16] | 0.0146 | 1.76 | 3.53 | 87% M | torch 314.3%, torch-compile 99.1% | - |
| 🟡 | AddFwdOp | test_add_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0146 | 1.76 | 3.53 | 87% M | torch 318.5%, torch-compile 98.7% | - |
| 🟡 | AddFwdOp | test_add_manifest_bench[cnn-feat-broadcast-float32] | 0.0266 | 0.96 | 3.86 | ✅ 95% M | torch 184.7%, torch-compile 99.8% | - |
| 🔵 | AlibiFwdOp | test_alibi_bench[llama-prefill-2k-float16] | 0.0646 | 6.23 | 4.16 | ✅ 102% M | torch-ref 916.1%, torch-compile 134.1% | - |
| 🔵 | AlibiFwdOp | test_alibi_bench[llama-prefill-2k-bfloat16] | 0.0647 | 6.23 | 4.15 | ✅ 102% M | torch-ref 915.0%, torch-compile 133.1% | - |
| 🔵 | AlibiFwdOp | test_alibi_bench[llama-prefill-4k-float16] | 0.2844 | 5.66 | 3.78 | ✅ 93% M | torch-ref 917.3%, torch-compile 120.0% | - |
| 🔵 | AlibiFwdOp | test_alibi_bench[llama-prefill-4k-bfloat16] | 0.2840 | 5.67 | 3.78 | ✅ 93% M | torch-ref 918.7%, torch-compile 119.9% | - |
| 🟡 | AllFwdOp | test_all_bench[mask-validation-4k-bool] | 0.0020 | 0.07 | 0.07 | <sub>lat-bound</sub> | flaggems 96.7%, torch 888.5%, torch-compile 93.4% | - |
| 🟡 | AllFwdOp | test_all_bench[mask-validation-32k-bool] | 0.0038 | 0.28 | 0.28 | <sub>lat-bound</sub> | flaggems 170.3%, torch 269.5%, torch-compile 92.4% | - |
| 🟡 | AllFwdOp | test_all_bench[3d-multidim-reduce-bool] | 0.0045 | 0.46 | 0.46 | <sub>lat-bound</sub> | flaggems 258.4%, torch 227.5%, torch-compile 94.3% | - |
| 🔵 | AmaxFwdOp | test_amax_bench[hidden-state-reduce-float16] | 0.0074 | 1.13 | 2.26 | 56% M | flaggems 103.4%, torch 259.2%, torch-compile 136.4% | - |
| 🔵 | AmaxFwdOp | test_amax_bench[hidden-state-reduce-bfloat16] | 0.0074 | 1.13 | 2.26 | 56% M | flaggems 105.2%, torch 260.3%, torch-compile 136.2% | - |
| 🔵 | AmaxFwdOp | test_amax_bench[long-seq-reduce-bfloat16] | 0.0041 | 0.51 | 1.02 | <sub>lat-bound</sub> | flaggems 332.0%, torch 275.8%, torch-compile 115.6% | - |
| 🟡 | AmaxFwdOp | test_amax_bench[3d-multidim-reduce-float16] | 0.0057 | 0.37 | 0.74 | <sub>lat-bound</sub> | flaggems 217.7%, torch 227.0%, torch-compile 91.0% | - |
| 🔵 | AminFwdOp | test_amin_bench[hidden-state-reduce-float16] | 0.0074 | 1.13 | 2.26 | 56% M | torch 259.0%, torch-compile 136.2% | - |
| 🔵 | AminFwdOp | test_amin_bench[hidden-state-reduce-bfloat16] | 0.0074 | 1.13 | 2.26 | 56% M | torch 260.3%, torch-compile 136.2% | - |
| 🔵 | AminFwdOp | test_amin_bench[long-seq-reduce-bfloat16] | 0.0041 | 0.51 | 1.02 | <sub>lat-bound</sub> | torch 275.0%, torch-compile 121.1% | - |
| 🟡 | AminFwdOp | test_amin_bench[3d-multidim-reduce-float16] | 0.0057 | 0.37 | 0.74 | <sub>lat-bound</sub> | torch 226.9%, torch-compile 88.2% | - |
| 🟡 | AnyFwdOp | test_any_bench[mask-validation-4k-bool] | 0.0020 | 0.07 | 0.07 | <sub>lat-bound</sub> | flaggems 96.7%, torch 911.5%, torch-compile 88.5% | - |
| 🟡 | AnyFwdOp | test_any_bench[mask-validation-32k-bool] | 0.0038 | 0.28 | 0.28 | <sub>lat-bound</sub> | flaggems 170.4%, torch 278.8%, torch-compile 87.3% | - |
| 🟡 | AnyFwdOp | test_any_bench[3d-multidim-reduce-bool] | 0.0045 | 0.46 | 0.46 | <sub>lat-bound</sub> | flaggems 258.4%, torch 413.0%, torch-compile 82.4% | - |
| 🟢 | ArgmaxFwdOp | test_argmax_bench[lm-head-argmax-float16] | 0.0039 | 0.11 | 0.21 | <sub>lat-bound</sub> | flaggems 773.5%, torch 911.6%, torch-compile 736.4% | - |
| 🟢 | ArgmaxFwdOp | test_argmax_bench[lm-head-argmax-bfloat16] | 0.0040 | 0.10 | 0.21 | <sub>lat-bound</sub> | flaggems 716.1%, torch 907.3%, torch-compile 732.3% | - |
| 🔵 | ArgmaxFwdOp | test_argmax_bench[hidden-state-argmax-float16] | 0.0092 | 0.91 | 1.83 | 45% M | flaggems 132.8%, torch 267.9%, torch-compile 207.0% | - |
| 🔵 | ArgmaxFwdOp | test_argmax_bench[hidden-state-argmax-bfloat16] | 0.0096 | 0.87 | 1.74 | 43% M | flaggems 120.6%, torch 258.1%, torch-compile 201.0% | - |
| 🟡 | ArgmaxFwdOp | test_argmax_bench[3d-non-last-axis-argmax-float16] | 0.0039 | 0.54 | 2.15 | <sub>lat-bound</sub> | flaggems 98.0%, torch 285.2%, torch-compile 100.4% | - |
| 🟢 | ArgminFwdOp | test_argmin_bench[lm-head-argmin-float16] | 0.0040 | 0.10 | 0.20 | <sub>lat-bound</sub> | flaggems 2895.2%, torch 881.6%, torch-compile 716.8% | - |
| 🟢 | ArgminFwdOp | test_argmin_bench[lm-head-argmin-bfloat16] | 0.0067 | 0.06 | 0.12 | <sub>lat-bound</sub> | flaggems 1542.6%, torch 539.4%, torch-compile 437.0% | - |
| 🔵 | ArgminFwdOp | test_argmin_bench[hidden-state-argmin-float16] | 0.0097 | 0.87 | 1.74 | 43% M | flaggems 102.6%, torch 255.0%, torch-compile 196.7% | - |
| 🔵 | ArgminFwdOp | test_argmin_bench[hidden-state-argmin-bfloat16] | 0.0099 | 0.85 | 1.70 | 42% M | flaggems 100.0%, torch 251.7%, torch-compile 196.8% | - |
| 🔵 | AvgPool1dFwdOp | test_avg_pool1d_bench[audio-downsample-float16] | 0.0062 | 0.51 | 1.02 | <sub>lat-bound</sub> | torch-ref 248.2%, torch-compile 103.1% | - |
| 🟡 | AvgPool1dFwdOp | test_avg_pool1d_bench[long-temporal-float16] | 0.0212 | 0.96 | 1.93 | 47% M | torch-ref 279.4%, torch-compile 80.6% | - |
| 🔴 | AvgPool1dFwdOp | test_avg_pool1d_bench[ceil-bfloat16] | 0.0035 | 0.30 | 0.46 | <sub>lat-bound</sub> | torch-ref 153.7%, torch-compile 66.7% | - |
| 🔵 | AvgPool2dFwdOp | test_avg_pool2d_bench[vision-3x3-s2-float16] | 0.0040 | 0.91 | 1.01 | <sub>lat-bound</sub> | flaggems 167.0%, torch-ref 229.0%, torch-compile 103.2% | - |
| 🟢 | AvgPool2dFwdOp | test_avg_pool2d_bench[vision-5x5-s2-float16] | 0.0040 | 1.24 | 0.50 | <sub>lat-bound</sub> | flaggems 179.4%, torch-ref 244.1%, torch-compile 511.1% | - |
| 🔵 | AvgPool2dFwdOp | test_avg_pool2d_bench[ceil-divisor-bfloat16] | 0.0031 | 1.12 | 0.72 | <sub>lat-bound</sub> | flaggems 184.7%, torch-ref 243.9%, torch-compile 124.5% | - |
| 🔵 | AvgPool3dFwdOp | test_avg_pool3d_bench[video-2x2x2-float16] | 0.0037 | 0.44 | 0.98 | <sub>lat-bound</sub> | cudnn 160.0%, torch-ref 269.5%, torch-compile 131.3% | - |
| 🟡 | AvgPool3dFwdOp | test_avg_pool3d_bench[ceil-video-float16] | 0.0044 | 0.59 | 0.43 | <sub>lat-bound</sub> | cudnn 127.8%, torch-ref 259.9%, torch-compile 92.3% | - |
| 🟡 | AvgPool3dFwdOp | test_avg_pool3d_bench[divisor-bfloat16] | 0.0023 | 0.15 | 0.21 | <sub>lat-bound</sub> | torch-ref 222.5%, torch-compile 84.5% | - |
| 🟢 | BatchNormBwdOp | test_batch_norm_bwd_bench[resnet50-fc-float16] | 0.0071 | 0.00 | 0.00 | <sub>lat-bound</sub> | torch-autograd 331.5%, torch-native-batch-norm 178.8% | - |
| 🔵 | BatchNormBwdOp | test_batch_norm_bwd_bench[resnet50-stage1-float16] | 0.0148 | 0.28 | 0.21 | <sub>lat-bound</sub> | torch-autograd 187.0%, torch-native-batch-norm 127.7% | - |
| 🔵 | BatchNormBwdOp | test_batch_norm_bwd_bench[resnet50-stage2-float16] | 0.0141 | 0.30 | 0.22 | <sub>lat-bound</sub> | torch-autograd 169.8%, torch-native-batch-norm 108.4% | - |
| 🔵 | BatchNormBwdOp | test_batch_norm_bwd_bench[resnet50-stage3-float16] | 0.0171 | 0.38 | 0.28 | <sub>lat-bound</sub> | torch-autograd 149.6%, torch-native-batch-norm 103.6% | - |
| 🟢 | BatchNormBwdOp | test_batch_norm_bwd_bench[large-spatial-float16] | 6.8767 | 0.62 | 0.47 | 12% M | torch-autograd 188.6%, torch-native-batch-norm 171.6% | - |
| 🔴 | BatchNormFwdOp | test_batch_norm_fwd_bench[resnet50-fc-float16] | 0.0061 | 0.00 | 0.00 | <sub>lat-bound</sub> | flaggems 90.6%, torch-cudnn 184.8%, torch-compile 30.4% | - |
| 🔴 | BatchNormFwdOp | test_batch_norm_fwd_bench[resnet50-stage1-float16] | 0.0110 | 0.48 | 0.19 | <sub>lat-bound</sub> | flaggems 94.2%, torch-cudnn 104.0%, torch-compile 37.6% | - |
| 🔴 | BatchNormFwdOp | test_batch_norm_fwd_bench[resnet50-stage2-float16] | 0.0107 | 0.49 | 0.20 | <sub>lat-bound</sub> | flaggems 83.8%, torch-cudnn 97.0%, torch-compile 32.6% | - |
| 🔴 | BatchNormFwdOp | test_batch_norm_fwd_bench[resnet50-stage3-float16] | 0.0129 | 0.62 | 0.25 | <sub>lat-bound</sub> | flaggems 85.3%, torch-cudnn 86.6%, torch-compile 37.6% | - |
| 🔴 | BatchNormFwdOp | test_batch_norm_fwd_bench[large-spatial-float16] | 4.3432 | 1.24 | 0.49 | 12% M | flaggems 89.7%, torch-cudnn 104.4%, torch-compile 23.4% | - |
| 🔵 | BitwiseAndFwdOp | test_bitwise_bench[bitwise_and-1024x4096-BitwiseAndFwdOp-bitwise_and] | 0.0147 | 0.28 | 3.42 | - | torch 100.1%, torch-compile 100.0% | - |
| 🟡 | BitwiseAndFwdOp | test_bitwise_bench[bitwise_and-1024x10240-BitwiseAndFwdOp-bitwise_and] | 0.0321 | 0.33 | 3.92 | - | torch 99.6%, torch-compile 99.6% | - |
| 🔵 | BitwiseAndFwdOp | test_bitwise_and_manifest_bench[hidden-state-prefill-bool] | 0.0083 | 1.01 | 3.02 | 74% M | torch 121.2%, torch-compile 107.3% | - |
| 🔵 | BitwiseAndFwdOp | test_bitwise_and_manifest_bench[hidden-state-prefill-int32] | 0.0262 | 0.32 | 3.84 | ✅ 94% M | torch 100.2%, torch-compile 100.0% | - |
| 🔵 | BitwiseAndFwdOp | test_bitwise_and_manifest_bench[hidden-state-prefill-int64] | 0.0493 | 0.17 | 4.09 | ✅ 100% M | torch 100.7%, torch-compile 100.0% | - |
| 🔵 | BitwiseAndFwdOp | test_bitwise_and_manifest_bench[cnn-feat-broadcast-bool] | 0.0083 | 1.56 | 3.11 | 76% M | torch 547.3%, torch-compile 120.9% | - |
| 🔵 | BitwiseAndFwdOp | test_bitwise_and_manifest_bench[cnn-feat-broadcast-int32] | 0.0265 | 0.48 | 3.88 | ✅ 95% M | torch 187.0%, torch-compile 100.2% | - |
| 🟡 | BitwiseAndFwdOp | test_bitwise_and_manifest_bench[cnn-feat-broadcast-int64] | 0.0500 | 0.26 | 4.11 | ✅ 101% M | torch 116.7%, torch-compile 99.6% | - |
| 🟡 | BitwiseNotFwdOp | test_bitwise_not_bench[elementwise-16M-int32] | 0.0340 | 0.49 | 3.95 | ✅ 97% M | torch 99.8%, torch-compile 99.8% | - |
| 🟡 | BitwiseNotFwdOp | test_bitwise_not_bench[elementwise-16M-int64] | 0.0651 | 0.26 | 4.12 | ✅ 101% M | torch 104.5%, torch-compile 99.5% | - |
| 🔵 | BitwiseNotFwdOp | test_bitwise_not_bench[elementwise-256M-int32] | 0.4985 | 0.54 | 4.31 | ⚠️ 106% M | torch 101.2%, torch-compile 101.2% | - |
| 🟡 | BitwiseOrFwdOp | test_bitwise_bench[bitwise_or-1024x4096-BitwiseOrFwdOp-bitwise_or] | 0.0148 | 0.28 | 3.40 | - | torch 98.7%, torch-compile 98.3% | - |
| 🔵 | BitwiseOrFwdOp | test_bitwise_or_manifest_bench[hidden-state-prefill-bool] | 0.0081 | 1.04 | 3.11 | 76% M | torch 108.7%, torch-compile 105.5% | - |
| 🟡 | BitwiseOrFwdOp | test_bitwise_or_manifest_bench[hidden-state-prefill-int32] | 0.0265 | 0.32 | 3.79 | ✅ 93% M | torch 99.8%, torch-compile 99.7% | - |
| 🔵 | BitwiseOrFwdOp | test_bitwise_or_manifest_bench[hidden-state-prefill-int64] | 0.0492 | 0.17 | 4.09 | ✅ 100% M | torch 100.9%, torch-compile 100.3% | - |
| 🔵 | BitwiseOrFwdOp | test_bitwise_or_manifest_bench[cnn-feat-broadcast-bool] | 0.0082 | 1.56 | 3.12 | 77% M | torch 538.1%, torch-compile 124.1% | - |
| 🟡 | BitwiseOrFwdOp | test_bitwise_or_manifest_bench[cnn-feat-broadcast-int32] | 0.0266 | 0.48 | 3.86 | ✅ 95% M | torch 185.2%, torch-compile 99.5% | - |
| 🔵 | BitwiseOrFwdOp | test_bitwise_or_manifest_bench[cnn-feat-broadcast-int64] | 0.0499 | 0.26 | 4.12 | ✅ 101% M | torch 116.3%, torch-compile 100.1% | - |
| 🔵 | BitwiseXorFwdOp | test_bitwise_bench[bitwise_xor-1024x4096-BitwiseXorFwdOp-bitwise_xor] | 0.0147 | 0.28 | 3.42 | - | torch 100.6%, torch-compile 100.0% | - |
| 🔵 | BitwiseXorFwdOp | test_bitwise_xor_manifest_bench[hidden-state-prefill-bool] | 0.0082 | 1.03 | 3.08 | 76% M | torch 121.7%, torch-compile 107.6% | - |
| 🟡 | BitwiseXorFwdOp | test_bitwise_xor_manifest_bench[hidden-state-prefill-int32] | 0.0265 | 0.32 | 3.80 | ✅ 93% M | torch 99.3%, torch-compile 99.0% | - |
| 🔵 | BitwiseXorFwdOp | test_bitwise_xor_manifest_bench[hidden-state-prefill-int64] | 0.0492 | 0.17 | 4.09 | ✅ 101% M | torch 101.1%, torch-compile 100.0% | - |
| 🔵 | BitwiseXorFwdOp | test_bitwise_xor_manifest_bench[cnn-feat-broadcast-bool] | 0.0083 | 1.56 | 3.11 | 76% M | torch 547.3%, torch-compile 121.7% | - |
| 🔵 | BitwiseXorFwdOp | test_bitwise_xor_manifest_bench[cnn-feat-broadcast-int32] | 0.0264 | 0.49 | 3.90 | ✅ 96% M | torch 187.4%, torch-compile 100.0% | - |
| 🟡 | BitwiseXorFwdOp | test_bitwise_xor_manifest_bench[cnn-feat-broadcast-int64] | 0.0501 | 0.26 | 4.10 | ✅ 101% M | torch 116.2%, torch-compile 99.6% | - |
| 🟡 | BmmFp8KNFwdOp | test_bmm_fp8_kn_bench[square-b4-1k-per-tensor-float8_e4m3fn] | 0.0390 | 220.04 | 0.43 | 18% C | torch-fp32-ref 753.1%, flashinfer-bmm-fp8 91.0% | - |
| 🟢 | BmmFp8KNFwdOp | test_bmm_fp8_kn_bench[square-b8-2k-per-tensor-float8_e4m3fn] | 0.3064 | 448.51 | 0.44 | 36% C | torch-fp32-ref 1324.6%, flashinfer-bmm-fp8 203.2% | - |
| 🔴 | BmmFp8KNFwdOp | test_bmm_fp8_kn_bench[mha-decode-b32-pv-per-tensor-float8_e4m3fn] | 0.0647 | 33.21 | 0.28 | 7% M | torch-fp32-ref 364.9%, flashinfer-bmm-fp8 38.6% | - |
| 🔴 | BmmFp8KNFwdOp | test_bmm_fp8_kn_bench[mha-decode-b64-qk-per-tensor-float8_e4m3fn] | 0.1155 | 37.19 | 0.44 | 11% M | torch-fp32-ref 250.2%, flashinfer-bmm-fp8 42.9% | - |
| 🔴 | BmmFp8KNFwdOp | test_bmm_fp8_kn_bench[moe-prefill-b128-per-tensor-float8_e4m3fn] | 0.9007 | 152.59 | 0.37 | 12% C | torch-fp32-ref 599.3%, flashinfer-bmm-fp8 69.3% | - |
| 🔵 | BmmFp8NKFwdOp | test_bmm_fp8_nk_bench[square-b4-1k-per-tensor-float8_e4m3fn] | 0.0119 | 722.57 | 1.41 | 58% C | torch-fp32-ref 2469.2%, flashinfer-bmm-fp8 109.8% | - |
| 🔵 | BmmFp8NKFwdOp | test_bmm_fp8_nk_bench[square-b8-2k-per-tensor-float8_e4m3fn] | 0.1196 | 1148.69 | 1.12 | ✅ 92% C | torch-fp32-ref 3397.9%, flashinfer-bmm-fp8 105.1% | - |
| 🔵 | BmmFp8NKFwdOp | test_bmm_fp8_nk_bench[mha-decode-b32-pv-per-tensor-float8_e4m3fn] | 0.0091 | 237.13 | 1.97 | 48% M | torch-fp32-ref 2612.2%, flashinfer-bmm-fp8 105.0% | - |
| 🔵 | BmmFp8NKFwdOp | test_bmm_fp8_nk_bench[mha-decode-b64-qk-per-tensor-float8_e4m3fn] | 0.0157 | 272.80 | 3.26 | 80% M | torch-fp32-ref 1830.6%, flashinfer-bmm-fp8 137.5% | - |
| 🔵 | BmmFp8NKFwdOp | test_bmm_fp8_nk_bench[moe-prefill-b128-per-tensor-float8_e4m3fn] | 0.1316 | 1044.62 | 2.55 | ✅ 84% C | torch-fp32-ref 4109.1%, flashinfer-bmm-fp8 105.1% | - |
| 🔵 | BmmFwdOp | test_bmm_bench[small-b8-128-float16] | 0.0027 | 12.48 | 0.29 | <sub>lat-bound</sub> | flaggems 117.9%, torch-cublas 120.2% | - |
| 🔵 | BmmFwdOp | test_bmm_bench[small-b8-128-bfloat16] | 0.0027 | 12.34 | 0.29 | <sub>lat-bound</sub> | flaggems 116.5%, torch-cublas 118.8% | - |
| 🔴 | BmmFwdOp | test_bmm_bench[square-b8-1k-float16] | 0.0406 | 422.73 | 1.24 | 64% C | flaggems 110.2%, torch-cublas 76.2% | - |
| 🔴 | BmmFwdOp | test_bmm_bench[square-b8-1k-bfloat16] | 0.0408 | 421.07 | 1.23 | 60% C | flaggems 109.7%, torch-cublas 76.4% | - |
| 🟡 | BmmFwdOp | test_bmm_bench[square-b16-512-float16] | 0.0133 | 323.81 | 1.90 | 49% C | flaggems 114.1%, torch-cublas 91.0% | - |
| 🟡 | BmmFwdOp | test_bmm_bench[square-b16-512-bfloat16] | 0.0134 | 321.10 | 1.88 | 46% M | flaggems 112.9%, torch-cublas 89.5% | - |
| 🔵 | BmmFwdOp | test_bmm_bench[square-b32-256-float16] | 0.0066 | 162.91 | 1.91 | 47% M | flaggems 120.4%, torch-cublas 107.3% | - |
| 🔵 | BmmFwdOp | test_bmm_bench[square-b32-256-bfloat16] | 0.0066 | 163.68 | 1.92 | 47% M | flaggems 120.5%, torch-cublas 107.8% | - |
| 🔴 | BmmFwdOp | test_bmm_bench[square-b4-4k-bfloat16] | 1.0435 | 526.86 | 0.39 | 75% C | flaggems 92.4%, torch-cublas 74.1% | - |
| 🔴 | BmmFwdOp | test_bmm_bench[square-b8-2k-float16] | 0.2839 | 484.16 | 0.71 | 73% C | flaggems 97.6%, torch-cublas 73.2% | - |
| 🔴 | BmmFwdOp | test_bmm_bench[square-b8-2k-bfloat16] | 0.2797 | 491.36 | 0.72 | 70% C | flaggems 97.6%, torch-cublas 73.5% | - |
| 🟡 | BmmFwdOp | test_bmm_bench[mha-decode-b64-qk-float16] | 0.0225 | 191.19 | 3.08 | 76% M | flaggems 115.7%, torch-cublas 94.2% | - |
| 🟡 | BmmFwdOp | test_bmm_bench[mha-decode-b64-qk-bfloat16] | 0.0224 | 191.74 | 3.09 | 76% M | flaggems 115.6%, torch-cublas 94.7% | - |
| 🔵 | BmmFwdOp | test_bmm_bench[mha-decode-b64-pv-float16] | 0.0239 | 179.43 | 2.89 | 71% M | flaggems 170.2%, torch-cublas 101.9% | - |
| 🔵 | BmmFwdOp | test_bmm_bench[mha-decode-b64-pv-bfloat16] | 0.0239 | 179.43 | 2.89 | 71% M | flaggems 169.4%, torch-cublas 101.7% | - |
| 🔴 | BmmFwdOp | test_bmm_bench[moe-prefill-b128-bfloat16] | 0.2907 | 472.73 | 2.08 | 68% C | flaggems 101.8%, torch-cublas 74.4% | - |
| 🟢 | CBProducerFwdOp | test_cb_producer_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0072 | 18.72 | 0.59 | <sub>lat-bound</sub> | torch 528.6% | - |
| 🟢 | CBProducerFwdOp | test_cb_producer_fwd_bench[mamba2-2p7b-b4-s2k-bfloat16] | 0.0119 | 22.61 | 0.71 | <sub>lat-bound</sub> | torch 446.6% | - |
| 🔵 | CeilFwdOp | test_ceil_bench[elementwise-16M-float16] | 0.0179 | 0.94 | 3.75 | ✅ 92% M | torch 100.4%, torch-compile 100.2% | - |
| 🔵 | CeilFwdOp | test_ceil_bench[elementwise-16M-bfloat16] | 0.0179 | 0.94 | 3.76 | ✅ 92% M | torch 100.5%, torch-compile 100.2% | - |
| 🟡 | CeilFwdOp | test_ceil_bench[elementwise-16M-float32] | 0.0340 | 0.49 | 3.95 | ✅ 97% M | torch 100.0%, torch-compile 99.6% | - |
| 🟡 | CeilFwdOp | test_ceil_bench[elementwise-256M-float16] | 0.2500 | 1.07 | 4.30 | ⚠️ 106% M | torch 100.1%, torch-compile 100.0% | - |
| 🔵 | CeilFwdOp | test_ceil_bench[elementwise-256M-bfloat16] | 0.2499 | 1.07 | 4.30 | ⚠️ 106% M | torch 100.2%, torch-compile 100.0% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-float16] | 0.0355 | 0.47 | 3.78 | ✅ 93% M | torch 98.2%, torch-compile 99.0% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-bfloat16] | 0.0355 | 0.47 | 3.78 | ✅ 93% M | torch 98.2%, torch-compile 98.7% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-float32] | 0.0659 | 0.25 | 4.07 | ✅ 100% M | torch 99.4%, torch-compile 99.3% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-256M-float16] | 0.4859 | 0.55 | 4.42 | ⚠️ 109% M | torch 99.9%, torch-compile 99.8% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-256M-bfloat16] | 0.4855 | 0.55 | 4.42 | ⚠️ 109% M | torch 99.9%, torch-compile 99.9% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-min-only-float16] | 0.0267 | 0.63 | 3.77 | ✅ 93% M | torch 99.8%, torch-compile 98.7% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-min-only-bfloat16] | 0.0269 | 0.62 | 3.74 | ✅ 92% M | torch 99.9%, torch-compile 98.2% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-min-only-float32] | 0.0501 | 0.33 | 4.02 | ✅ 99% M | torch 98.5%, torch-compile 98.2% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-256M-min-only-float16] | 0.3693 | 0.73 | 4.36 | ⚠️ 107% M | torch 99.7%, torch-compile 99.9% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-256M-min-only-bfloat16] | 0.3687 | 0.73 | 4.37 | ⚠️ 107% M | torch 99.8%, torch-compile 100.0% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-max-only-float16] | 0.0266 | 0.63 | 3.79 | ✅ 93% M | torch 99.9%, torch-compile 98.9% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-max-only-bfloat16] | 0.0271 | 0.62 | 3.71 | ✅ 91% M | torch 99.3%, torch-compile 98.2% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-max-only-float32] | 0.0500 | 0.34 | 4.03 | ✅ 99% M | torch 99.0%, torch-compile 98.4% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-256M-max-only-float16] | 0.3689 | 0.73 | 4.37 | ⚠️ 107% M | torch 99.8%, torch-compile 100.0% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-256M-max-only-bfloat16] | 0.3679 | 0.73 | 4.38 | ⚠️ 108% M | torch 100.0%, torch-compile 100.3% | - |
| 🔵 | ClampScalarFwdOp | test_clamp_scalar_manifest_bench[elementwise-16M-float16] | 0.0184 | 0.91 | 3.64 | 89% M | torch 110.2%, torch-compile 100.3% | - |
| 🔵 | ClampScalarFwdOp | test_clamp_scalar_manifest_bench[elementwise-16M-bfloat16] | 0.0184 | 0.91 | 3.64 | 89% M | torch 103.8%, torch-compile 101.2% | - |
| 🔵 | ClampScalarFwdOp | test_clamp_scalar_manifest_bench[elementwise-16M-float32] | 0.0339 | 0.50 | 3.96 | ✅ 97% M | torch 100.8%, torch-compile 100.4% | - |
| 🔵 | ClampScalarFwdOp | test_clamp_scalar_manifest_bench[elementwise-256M-float16] | 0.2518 | 1.07 | 4.26 | ✅ 105% M | torch 116.0%, torch-compile 100.8% | - |
| 🔵 | ClampScalarFwdOp | test_clamp_scalar_manifest_bench[elementwise-256M-bfloat16] | 0.2525 | 1.06 | 4.25 | ✅ 104% M | torch 109.0%, torch-compile 105.2% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[whisper-large-conv1-float16] | 0.0482 | 38.23 | 0.18 | 6% C | flaggems 232.8%, torch 118.0%, torch-compile 118.1% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[whisper-large-conv1-bfloat16] | 0.0485 | 37.99 | 0.18 | 5% C | flaggems 230.9%, torch 116.3%, torch-compile 116.4% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[wav2vec2-layer1-float16] | 0.0067 | 4.92 | 0.50 | <sub>lat-bound</sub> | flaggems 603.3%, torch 279.8%, torch-compile 279.8% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[wav2vec2-layer1-bfloat16] | 0.0067 | 4.90 | 0.50 | <sub>lat-bound</sub> | flaggems 600.0%, torch 281.8%, torch-compile 281.8% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[encodec-init-float16] | 0.0036 | 3.03 | 0.45 | <sub>lat-bound</sub> | flaggems 691.2%, torch 187.4%, torch-compile 186.5% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[encodec-init-bfloat16] | 0.0035 | 3.05 | 0.45 | <sub>lat-bound</sub> | flaggems 693.7%, torch 189.1%, torch-compile 189.1% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[encodec-deep-float16] | 0.0120 | 32.28 | 0.09 | <sub>lat-bound</sub> | flaggems 595.5%, torch 141.6%, torch-compile 141.3% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[encodec-deep-bfloat16] | 0.0120 | 32.28 | 0.09 | <sub>lat-bound</sub> | flaggems 595.6%, torch 141.3%, torch-compile 140.8% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[whisper-large-conv1-bias-float16] | 0.0478 | 38.63 | 0.18 | 6% C | flaggems 233.8%, torch 145.0%, torch-compile 133.6% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[whisper-large-conv1-bias-bfloat16] | 0.0477 | 38.66 | 0.18 | 6% C | flaggems 232.6%, torch 145.1%, torch-compile 132.7% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[wav2vec2-layer1-bias-float16] | 0.0069 | 4.98 | 0.48 | <sub>lat-bound</sub> | flaggems 566.7%, torch 365.3%, torch-compile 311.1% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[wav2vec2-layer1-bias-bfloat16] | 0.0069 | 4.95 | 0.48 | <sub>lat-bound</sub> | flaggems 565.4%, torch 368.2%, torch-compile 312.4% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[encodec-init-bias-float16] | 0.0036 | 3.19 | 0.44 | <sub>lat-bound</sub> | flaggems 652.4%, torch 290.8%, torch-compile 237.2% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[encodec-init-bias-bfloat16] | 0.0036 | 3.19 | 0.44 | <sub>lat-bound</sub> | flaggems 651.5%, torch 295.6%, torch-compile 237.2% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[encodec-deep-bias-float16] | 0.0124 | 31.21 | 0.09 | <sub>lat-bound</sub> | flaggems 567.9%, torch 164.4%, torch-compile 150.2% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[encodec-deep-bias-bfloat16] | 0.0124 | 31.29 | 0.09 | <sub>lat-bound</sub> | flaggems 569.6%, torch 164.1%, torch-compile 150.1% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[resnet-3x3-float16] | 0.0130 | 35.59 | 0.13 | <sub>lat-bound</sub> | flaggems 640.2%, torch 113.5%, torch-compile 88.9% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[resnet-3x3-bfloat16] | 0.0130 | 35.59 | 0.13 | <sub>lat-bound</sub> | flaggems 640.4%, torch 114.3%, torch-compile 90.4% | - |
| 🟢 | Conv2dFwdOp | test_conv2d_bench[stem-3x3-s2-float16] | 0.0036 | 3.02 | 0.13 | <sub>lat-bound</sub> | flaggems 363.4%, torch 179.5%, torch-compile 258.9% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[stage-transition-3x3-s2-float16] | 0.0138 | 33.61 | 0.13 | <sub>lat-bound</sub> | flaggems 861.4%, torch 123.2%, torch-compile 97.4% | - |
| 🔴 | Conv2dFwdOp | test_conv2d_bench[highres-3x3-s1-float16] | 0.1049 | 282.01 | 0.21 | 43% C | flaggems 699.9%, torch 90.3%, torch-compile 75.5% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[midres-5x5-s1-float16] | 0.0161 | 79.64 | 0.10 | <sub>lat-bound</sub> | flaggems 1255.1%, torch 121.0%, torch-compile 99.8% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[stage-transition-5x5-s2-float16] | 0.0224 | 57.26 | 0.13 | 9% C | flaggems 1380.5%, torch 113.4%, torch-compile 99.0% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[stride2-bfloat16] | 0.0111 | 5.19 | 0.05 | <sub>lat-bound</sub> | flaggems 581.9%, torch 133.1%, torch-compile 108.6% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[resnet-1x1-float16] | 0.0044 | 47.22 | 0.93 | <sub>lat-bound</sub> | flaggems 1129.4%, torch 97.1%, torch-compile 193.4% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[resnet-1x1-bfloat16] | 0.0044 | 46.89 | 0.92 | <sub>lat-bound</sub> | flaggems 1122.4%, torch 91.2%, torch-compile 189.1% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[bottleneck-expand-1x1-float16] | 0.0038 | 54.41 | 0.57 | <sub>lat-bound</sub> | flaggems 755.3%, torch 105.9%, torch-compile 195.7% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[bottleneck-reduce-1x1-float16] | 0.0047 | 43.99 | 0.46 | <sub>lat-bound</sub> | flaggems 565.1%, torch 93.1%, torch-compile 171.6% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[late-stage-1x1-float16] | 0.0050 | 20.59 | 0.21 | <sub>lat-bound</sub> | flaggems 308.3%, torch 127.6%, torch-compile 133.3% | - |
| 🔴 | Conv2dFwdOp | test_conv2d_bench[classifier-1x1-float16] | 0.0091 | 11.27 | 0.26 | <sub>lat-bound</sub> | flaggems 226.3%, torch 98.9%, torch-compile 79.3% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[deeplabv3-aspp-3x3-rate12-float16] | 0.0889 | 108.67 | 0.16 | 16% C | flaggems 805.1%, torch 133.9%, torch-compile 102.4% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[mobilenetv2-depthwise-float16] | 0.0028 | 0.64 | 0.14 | <sub>lat-bound</sub> | flaggems 1925.0%, torch 106.8%, torch-compile 196.6% | - |
| 🟢 | Conv2dFwdOp | test_conv2d_bench[resnext-grouped-3x3-float16] | 0.0041 | 3.50 | 0.15 | <sub>lat-bound</sub> | flaggems 467.4%, torch 460.9%, torch-compile 462.0% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[resnet-3x3-bias-float16] | 0.0133 | 34.85 | 0.13 | <sub>lat-bound</sub> | flaggems 620.3%, torch 138.1%, torch-compile 92.8% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[resnet-3x3-bias-bfloat16] | 0.0138 | 33.64 | 0.12 | <sub>lat-bound</sub> | flaggems 598.8%, torch 133.7%, torch-compile 86.5% | - |
| 🟢 | Conv2dFwdOp | test_conv2d_bench[stem-3x3-s2-bias-float16] | 0.0035 | 3.16 | 0.14 | <sub>lat-bound</sub> | flaggems 352.3%, torch 271.6%, torch-compile 273.4% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[stage-transition-3x3-s2-bias-float16] | 0.0142 | 32.56 | 0.13 | <sub>lat-bound</sub> | flaggems 828.4%, torch 140.8%, torch-compile 104.0% | - |
| 🔴 | Conv2dFwdOp | test_conv2d_bench[highres-3x3-s1-bias-float16] | 0.1052 | 281.42 | 0.21 | 43% C | flaggems 694.6%, torch 108.9%, torch-compile 75.1% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[midres-5x5-s1-bias-float16] | 0.0165 | 77.96 | 0.10 | <sub>lat-bound</sub> | flaggems 1220.9%, torch 138.4%, torch-compile 99.8% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[stage-transition-5x5-s2-bias-float16] | 0.0226 | 56.95 | 0.13 | 9% C | flaggems 1372.0%, torch 127.1%, torch-compile 104.5% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[stride2-bias-bfloat16] | 0.0116 | 4.98 | 0.05 | <sub>lat-bound</sub> | flaggems 551.0%, torch 152.3%, torch-compile 108.2% | - |
| 🟢 | Conv2dFwdOp | test_conv2d_bench[resnet-1x1-bias-float16] | 0.0046 | 45.26 | 0.88 | <sub>lat-bound</sub> | flaggems 1053.9%, torch 254.6%, torch-compile 193.0% | - |
| 🟢 | Conv2dFwdOp | test_conv2d_bench[resnet-1x1-bias-bfloat16] | 0.0046 | 44.95 | 0.88 | <sub>lat-bound</sub> | flaggems 1049.3%, torch 249.3%, torch-compile 181.2% | - |
| 🟢 | Conv2dFwdOp | test_conv2d_bench[bottleneck-expand-1x1-bias-float16] | 0.0041 | 50.37 | 0.52 | <sub>lat-bound</sub> | flaggems 675.0%, torch 214.8%, torch-compile 185.9% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[bottleneck-reduce-1x1-bias-float16] | 0.0050 | 41.48 | 0.43 | <sub>lat-bound</sub> | flaggems 517.4%, torch 146.4%, torch-compile 168.7% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[late-stage-1x1-bias-float16] | 0.0053 | 19.50 | 0.19 | <sub>lat-bound</sub> | flaggems 279.4%, torch 175.2%, torch-compile 132.1% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[classifier-1x1-bias-float16] | 0.0095 | 10.79 | 0.25 | <sub>lat-bound</sub> | flaggems 208.7%, torch 125.8%, torch-compile 80.9% | - |
| 🟢 | Conv3dFwdOp | test_conv3d_bench[r3d-stem-k3-s1-float16] | 0.0230 | 90.57 | 1.17 | 29% M | flaggems 373.8%, torch 499.7%, torch-compile 499.7% | - |
| 🔴 | Conv3dFwdOp | test_conv3d_bench[video-stage-downsample-k3-s2-float16] | 0.0349 | 39.74 | 0.13 | 6% C | flaggems 622.2%, torch 75.5%, torch-compile 75.4% | - |
| 🔴 | Conv3dFwdOp | test_conv3d_bench[unet-encoder-k3-s1-bfloat16] | 0.3542 | 40.92 | 0.07 | 6% C | flaggems 89.4%, torch 32.6%, torch-compile 32.6% | - |
| 🔴 | Conv3dFwdOp | test_conv3d_bench[3d-unet-aspp-3x3x3-rate6-float16] | 0.1264 | 57.35 | 0.04 | 9% C | flaggems 237.7%, torch 29.8%, torch-compile 29.8% | - |
| 🟢 | Conv3dFwdOp | test_conv3d_bench[3d-resnext-grouped-k3-float16] | 0.0157 | 5.51 | 0.15 | <sub>lat-bound</sub> | flaggems 1616.4%, torch 1650.5%, torch-compile 1630.8% | - |
| 🟢 | Conv3dFwdOp | test_conv3d_bench[r3d-stem-k3-s1-bias-float16] | 0.0230 | 91.19 | 1.17 | 29% M | flaggems 370.9%, torch 673.4%, torch-compile 549.5% | - |
| 🔴 | Conv3dFwdOp | test_conv3d_bench[video-stage-downsample-k3-s2-bias-float16] | 0.0353 | 39.32 | 0.13 | 6% C | flaggems 611.6%, torch 85.0%, torch-compile 79.6% | - |
| 🔴 | Conv3dFwdOp | test_conv3d_bench[unet-encoder-k3-s1-bias-bfloat16] | 0.3538 | 40.99 | 0.07 | 6% C | flaggems 89.3%, torch 39.7%, torch-compile 34.5% | - |
| 🔵 | CosFwdOp | test_cos_bench[elementwise-16M-float16] | 0.0261 | 0.64 | 2.57 | 63% M | torch 104.7%, torch-compile 106.9% | - |
| 🔵 | CosFwdOp | test_cos_bench[elementwise-16M-bfloat16] | 0.0265 | 0.63 | 2.54 | 62% M | torch 103.3%, torch-compile 106.8% | - |
| 🟡 | CosFwdOp | test_cos_bench[elementwise-16M-float32] | 0.0352 | 0.48 | 3.81 | ✅ 94% M | torch 97.6%, torch-compile 97.5% | - |
| 🔵 | CosFwdOp | test_cos_bench[elementwise-256M-float16] | 0.3780 | 0.71 | 2.84 | 70% M | torch 103.9%, torch-compile 107.7% | - |
| 🔵 | CosFwdOp | test_cos_bench[elementwise-256M-bfloat16] | 0.3824 | 0.70 | 2.81 | 69% M | torch 102.8%, torch-compile 107.9% | - |
| 🔵 | CountNonzeroFwdOp | test_count_nonzero_bench[sparsity-hidden-float16] | 0.0081 | 2.06 | 2.07 | 51% M | torch 784.7%, torch-compile 112.0% | - |
| 🔵 | CountNonzeroFwdOp | test_count_nonzero_bench[sparsity-hidden-bfloat16] | 0.0081 | 2.07 | 2.07 | 51% M | torch 787.6%, torch-compile 112.2% | - |
| 🔵 | CountNonzeroFwdOp | test_count_nonzero_bench[sparsity-seq-float16] | 0.0037 | 0.56 | 0.57 | <sub>lat-bound</sub> | torch 409.5%, torch-compile 106.0% | - |
| 🔴 | CountNonzeroFwdOp | test_count_nonzero_bench[3d-multidim-reduce-float16] | 0.0064 | 0.66 | 0.66 | <sub>lat-bound</sub> | torch 340.6%, torch-compile 73.9% | - |
| 🟢 | CumprodFwdOp | test_cumprod_bench[hidden-state-scan-float16] | 0.0115 | 0.73 | 2.92 | 72% M | torch 1269.9%, torch-compile 210.9% | - |
| 🟢 | CumprodFwdOp | test_cumprod_bench[hidden-state-scan-bfloat16] | 0.0109 | 0.77 | 3.07 | 76% M | torch 1338.9%, torch-compile 223.4% | - |
| 🟢 | CumprodFwdOp | test_cumprod_bench[long-seq-scan-bfloat16] | 0.0070 | 0.30 | 1.19 | <sub>lat-bound</sub> | torch 962.3%, torch-compile 172.7% | - |
| 🟡 | CumsumFwdOp | test_cumsum_bench[hidden-state-scan-float16] | 0.0115 | 0.73 | 2.92 | 72% M | flaggems 92.2%, torch 1270.2%, torch-compile 210.6% | - |
| 🟡 | CumsumFwdOp | test_cumsum_bench[hidden-state-scan-bfloat16] | 0.0109 | 0.77 | 3.08 | 76% M | flaggems 96.9%, torch 1339.6%, torch-compile 223.5% | - |
| 🔵 | CumsumFwdOp | test_cumsum_bench[long-seq-scan-bfloat16] | 0.0070 | 0.30 | 1.19 | <sub>lat-bound</sub> | flaggems 113.6%, torch 962.7%, torch-compile 173.2% | - |
| 🔴 | DaCumsumFwdOp | test_da_cumsum_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0042 | 0.33 | 0.47 | <sub>lat-bound</sub> | mamba 78.8%, torch-ref 1685.2%, torch-compile 112.8% | - |
| 🔴 | DaCumsumFwdOp | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-bfloat16] | 0.0121 | 0.61 | 0.86 | <sub>lat-bound</sub> | mamba 53.0%, torch-ref 748.8%, torch-compile 94.2% | - |
| 🟡 | DaCumsumFwdOp | test_da_cumsum_fwd_bench[mamba2-780m-b1-s4k-dt-bias-float16] | 0.0042 | 0.37 | 0.47 | <sub>lat-bound</sub> | mamba 81.8%, torch-ref 1753.1%, torch-compile 113.6% | - |
| 🔴 | DaCumsumFwdOp | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-dt-bias-bfloat16] | 0.0124 | 0.68 | 0.85 | <sub>lat-bound</sub> | mamba 51.4%, torch-ref 776.8%, torch-compile 92.2% | - |
| 🔴 | DaCumsumFwdOp | test_da_cumsum_fwd_bench[mamba2-2p7b-b2-s32k-dt-bias-float16] | 0.0444 | 0.94 | 1.18 | 29% M | mamba 50.1%, torch-ref 533.2%, torch-compile 78.3% | - |
| 🟢 | DeepSeekSparseAttentionDecodeWithKVCacheFwdOp | test_dsa_decode_bench[single-batch-mainstream-float16] | 1.8624 | 313.64 | 0.16 | 47% C | torch-ref 1018.3%, torch-compile 891.9%, torch-sdpa 282.5% | - |
| 🟢 | DeepSeekSparseAttentionDecodeWithKVCacheFwdOp | test_dsa_decode_bench[longer-kv-lower-topk-float16] | 0.5008 | 291.61 | 0.30 | 44% C | torch-ref 3857.8%, torch-compile 3251.5%, torch-sdpa 1053.1%, torch-gather 362.1% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s2k-h4-d64-float16] | 0.1306 | 2.06 | 0.21 | 5% M | fla 86.8% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s2k-h4-d64-bfloat16] | 0.1316 | 2.04 | 0.21 | 5% M | fla 87.0% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s4k-h4-d64-float16] | 0.2592 | 2.07 | 0.21 | 5% M | fla 82.9% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s4k-h4-d64-bfloat16] | 0.2616 | 2.05 | 0.21 | 5% M | fla 82.7% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s8k-h4-d64-float16] | 0.5051 | 2.13 | 0.22 | 5% M | fla 85.7% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s8k-h4-d64-bfloat16] | 0.5104 | 2.10 | 0.21 | 5% M | fla 85.4% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s16k-h4-d64-float16] | 0.9933 | 2.16 | 0.22 | 5% M | fla 86.9% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s16k-h4-d64-bfloat16] | 1.0029 | 2.14 | 0.22 | 5% M | fla 86.8% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b1-h8-d128-bfloat16] | 0.0028 | 0.28 | 0.19 | <sub>lat-bound</sub> | torch 1175.2%, torch-compile 457.3% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b1-h16-d128-bfloat16] | 0.0031 | 0.51 | 0.35 | <sub>lat-bound</sub> | torch 1151.0%, torch-compile 466.7% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b1-h32-d128-bfloat16] | 0.0034 | 0.94 | 0.63 | <sub>lat-bound</sub> | torch 1164.8%, torch-compile 480.0% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b1-h48-d128-bfloat16] | 0.0036 | 1.33 | 0.90 | <sub>lat-bound</sub> | torch 1221.1%, torch-compile 552.2% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b1-h64-d128-bfloat16] | 0.0038 | 1.64 | 1.11 | <sub>lat-bound</sub> | torch 1142.9%, torch-compile 467.5% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b8-h32-d128-bfloat16] | 0.0087 | 2.89 | 1.95 | 48% M | torch 1026.4%, torch-compile 436.8% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b8-h48-d128-bfloat16] | 0.0123 | 3.07 | 2.07 | 51% M | torch 901.8%, torch-compile 320.8% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b8-h64-d128-bfloat16] | 0.0163 | 3.10 | 2.10 | 52% M | torch 875.7%, torch-compile 316.7% | - |
| 🟡 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s2k-h4-d64-float16] | 0.0627 | 2.14 | 0.34 | 8% M | fla 98.8% | - |
| 🟡 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s2k-h4-d64-bfloat16] | 0.0629 | 2.13 | 0.34 | 8% M | fla 99.1% | - |
| 🟡 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s4k-h4-d64-float16] | 0.1095 | 2.45 | 0.38 | 9% M | fla 90.0% | - |
| 🟡 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s4k-h4-d64-bfloat16] | 0.1096 | 2.45 | 0.38 | 9% M | fla 90.5% | - |
| 🟡 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s8k-h4-d64-float16] | 0.2337 | 2.30 | 0.36 | 9% M | fla 80.9% | - |
| 🟡 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s8k-h4-d64-bfloat16] | 0.2347 | 2.29 | 0.36 | 9% M | fla 81.5% | - |
| 🔴 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s16k-h4-d64-float16] | 0.4732 | 2.27 | 0.36 | 9% M | fla 77.4% | - |
| 🔴 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s16k-h4-d64-bfloat16] | 0.4733 | 2.27 | 0.36 | 9% M | fla 78.2% | - |
| 🔵 | DivFwdOp | test_binary_arith_bench[div-1024x4096-float16-float16-DivFwdOp-div-positive] | 0.0084 | 0.50 | 2.98 | - | torch 104.2%, torch-compile 100.0% | - |
| 🟡 | DivFwdOp | test_binary_arith_bench[div-1024x10240-float16-float16-DivFwdOp-div-positive] | 0.0181 | 0.58 | 3.47 | - | torch 101.9%, torch-compile 99.5% | - |
| 🟡 | DivFwdOp | test_binary_arith_bench[div-1024x11008-float16-float16-DivFwdOp-div-positive] | 0.0189 | 0.60 | 3.58 | - | torch 102.2%, torch-compile 99.5% | - |
| 🟡 | DivFwdOp | test_div_manifest_bench[hidden-state-prefill-float16] | 0.0148 | 0.57 | 3.40 | 84% M | torch 102.5%, torch-compile 99.4% | - |
| 🔵 | DivFwdOp | test_div_manifest_bench[hidden-state-prefill-bfloat16] | 0.0147 | 0.57 | 3.43 | 84% M | torch 103.0%, torch-compile 100.0% | - |
| 🟡 | DivFwdOp | test_div_manifest_bench[hidden-state-prefill-float32] | 0.0263 | 0.32 | 3.83 | ✅ 94% M | torch 100.5%, torch-compile 99.6% | - |
| 🟡 | DivFwdOp | test_div_manifest_bench[cnn-feat-broadcast-float16] | 0.0171 | 0.75 | 3.01 | 74% M | torch 297.1%, torch-compile 86.5% | - |
| 🟡 | DivFwdOp | test_div_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0147 | 0.87 | 3.49 | 86% M | torch 349.1%, torch-compile 97.6% | - |
| 🟡 | DivFwdOp | test_div_manifest_bench[cnn-feat-broadcast-float32] | 0.0268 | 0.48 | 3.84 | ✅ 94% M | torch 197.1%, torch-compile 98.8% | - |
| 🟢 | DropoutFwdOp | test_dropout_bench[tokens-1k-hidden-4k-float16] | 0.0062 | 0.68 | 2.72 | 67% M | torch 189.1%, torch-compile 182.9% | - |
| 🔵 | DropoutFwdOp | test_dropout_bench[tokens-1k-hidden-4k-float32] | 0.0103 | 0.41 | 3.26 | 80% M | torch 144.4%, torch-compile 116.2% | - |
| 🟢 | DropoutFwdOp | test_dropout_bench[tokens-1k-hidden-10k-bfloat16] | 0.0123 | 0.85 | 3.40 | 84% M | torch 191.9%, torch-compile 191.4% | - |
| 🔵 | EluFwdOp | test_elu_manifest_bench[mlp-hidden-float16] | 0.0122 | 2.76 | 2.76 | 68% M | torch 147.6%, torch-compile 130.5% | - |
| 🔵 | EluFwdOp | test_elu_manifest_bench[mlp-hidden-bfloat16] | 0.0120 | 2.79 | 2.79 | 69% M | torch 150.8%, torch-compile 139.1% | - |
| 🔵 | EluFwdOp | test_elu_manifest_bench[mlp-hidden-wide-float16] | 0.0218 | 3.08 | 3.08 | 76% M | torch 150.4%, torch-compile 136.0% | - |
| 🔵 | EluFwdOp | test_elu_manifest_bench[mlp-hidden-wide-bfloat16] | 0.0216 | 3.10 | 3.10 | 76% M | torch 153.8%, torch-compile 144.8% | - |
| 🔴 | EngramDecodeFwdOp | test_engram_decode_bench[decode-b1-dmem512-d256-float16] | 0.0329 | 0.02 | 0.02 | 0% M | torch-ref 285.0%, torch-compile 40.0% | - |
| 🔴 | EngramDecodeFwdOp | test_engram_decode_bench[decode-b4-dmem1024-d512-float16] | 0.0824 | 0.10 | 0.03 | 1% M | torch-ref 147.1%, torch-compile 31.6% | - |
| 🔴 | EngramDecodeFwdOp | test_engram_decode_bench[decode-b8-dmem512-d256-bfloat16] | 0.0334 | 0.13 | 0.02 | 1% M | torch-ref 332.2%, torch-compile 63.4% | - |
| 🟢 | EngramGateConvBwdOp | test_engram_gate_conv_bwd_bench[bwd-b1-s32-d256-float16] | 0.0112 | 0.04 | 0.02 | <sub>lat-bound</sub> | torch 1505.5%, torch-compile 440.2% | - |
| 🟢 | EngramGateConvBwdOp | test_engram_gate_conv_bwd_bench[bwd-b2-s64-d512-float16] | 0.0198 | 0.20 | 0.07 | <sub>lat-bound</sub> | torch 1009.4%, torch-compile 292.4% | - |
| 🟢 | EngramGateConvBwdOp | test_engram_gate_conv_bwd_bench[bwd-b1-s128-d256-bfloat16] | 0.0167 | 0.12 | 0.04 | <sub>lat-bound</sub> | torch 1101.7%, torch-compile 326.0% | - |
| 🟢 | EngramGateConvFwdOp | test_engram_gate_conv_fwd_bench[fwd-b1-s32-d256-float16] | 0.0040 | 0.05 | 0.02 | <sub>lat-bound</sub> | torch-ref 1850.2%, torch-compile 292.0% | - |
| 🟢 | EngramGateConvFwdOp | test_engram_gate_conv_fwd_bench[fwd-b2-s64-d512-float16] | 0.0051 | 0.31 | 0.13 | <sub>lat-bound</sub> | torch-ref 1689.6%, torch-compile 239.2% | - |
| 🟢 | EngramGateConvFwdOp | test_engram_gate_conv_fwd_bench[fwd-b1-s128-d256-bfloat16] | 0.0045 | 0.18 | 0.07 | <sub>lat-bound</sub> | torch-ref 1788.6%, torch-compile 261.4% | - |
| 🔵 | EqFwdOp | test_comparison_bench[eq-1024x4096-float16-eq] | 0.0076 | 0.56 | 2.78 | - | torch 103.8%, torch-compile 103.8% | - |
| 🔵 | EqFwdOp | test_comparison_bench[eq-1024x10240-float16-eq] | 0.0158 | 0.66 | 3.32 | - | torch 101.6%, torch-compile 101.4% | - |
| 🔵 | EqFwdOp | test_eq_manifest_bench[hidden-state-prefill-float16] | 0.0133 | 0.63 | 3.14 | 77% M | torch 101.4%, torch-compile 101.4% | - |
| 🟡 | EqFwdOp | test_eq_manifest_bench[hidden-state-prefill-bfloat16] | 0.0131 | 0.64 | 3.19 | 78% M | torch 99.6%, torch-compile 99.4% | - |
| 🔵 | EqFwdOp | test_eq_manifest_bench[hidden-state-prefill-float32] | 0.0223 | 0.38 | 3.38 | 83% M | torch 100.0%, torch-compile 111.9% | - |
| 🔴 | EqFwdOp | test_eq_manifest_bench[cnn-feat-broadcast-float16] | 0.0172 | 0.75 | 2.24 | 55% M | torch 277.1%, torch-compile 69.3% | - |
| 🔴 | EqFwdOp | test_eq_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0172 | 0.74 | 2.23 | 55% M | torch 283.3%, torch-compile 69.2% | - |
| 🟡 | EqFwdOp | test_eq_manifest_bench[cnn-feat-broadcast-float32] | 0.0215 | 0.60 | 2.99 | 73% M | torch 222.5%, torch-compile 85.8% | - |
| 🟡 | ErfFwdOp | test_erf_bench[elementwise-16M-float16] | 0.0284 | 0.59 | 2.36 | 58% M | torch 93.0%, torch-compile 103.2% | - |
| 🟡 | ErfFwdOp | test_erf_bench[elementwise-16M-bfloat16] | 0.0285 | 0.59 | 2.36 | 58% M | torch 97.3%, torch-compile 104.3% | - |
| 🟡 | ErfFwdOp | test_erf_bench[elementwise-16M-float32] | 0.0350 | 0.48 | 3.83 | ✅ 94% M | torch 98.0%, torch-compile 98.6% | - |
| 🟡 | ErfFwdOp | test_erf_bench[elementwise-256M-float16] | 0.4215 | 0.64 | 2.55 | 63% M | torch 91.6%, torch-compile 102.6% | - |
| 🟡 | ErfFwdOp | test_erf_bench[elementwise-256M-bfloat16] | 0.4233 | 0.63 | 2.54 | 62% M | torch 96.0%, torch-compile 103.1% | - |
| 🔵 | ExpFwdOp | test_exp_bench[elementwise-16M-float16] | 0.0181 | 0.93 | 3.71 | ✅ 91% M | torch 100.9%, torch-compile 100.5% | - |
| 🔵 | ExpFwdOp | test_exp_bench[elementwise-16M-bfloat16] | 0.0182 | 0.92 | 3.69 | ✅ 91% M | torch 101.0%, torch-compile 101.2% | - |
| 🔵 | ExpFwdOp | test_exp_bench[elementwise-16M-float32] | 0.0340 | 0.49 | 3.95 | ✅ 97% M | torch 100.2%, torch-compile 100.1% | - |
| 🔵 | ExpFwdOp | test_exp_bench[elementwise-256M-float16] | 0.2544 | 1.06 | 4.22 | ✅ 104% M | torch 100.7%, torch-compile 100.9% | - |
| 🔵 | ExpFwdOp | test_exp_bench[elementwise-256M-bfloat16] | 0.2572 | 1.04 | 4.17 | ✅ 103% M | torch 100.6%, torch-compile 102.2% | - |
| 🔵 | Expm1FwdOp | test_expm1_bench[elementwise-16M-float16] | 0.0180 | 1.87 | 3.73 | ✅ 92% M | torch 140.7%, torch-compile 150.0% | - |
| 🟢 | Expm1FwdOp | test_expm1_bench[elementwise-16M-bfloat16] | 0.0181 | 1.86 | 3.71 | ✅ 91% M | torch 155.1%, torch-compile 155.0% | - |
| 🔵 | Expm1FwdOp | test_expm1_bench[elementwise-16M-float32] | 0.0340 | 0.99 | 3.95 | ✅ 97% M | torch 100.8%, torch-compile 101.4% | - |
| 🔵 | Expm1FwdOp | test_expm1_bench[elementwise-256M-float16] | 0.2542 | 2.11 | 4.22 | ✅ 104% M | torch 144.7%, torch-compile 155.1% | - |
| 🟢 | Expm1FwdOp | test_expm1_bench[elementwise-256M-bfloat16] | 0.2573 | 2.09 | 4.17 | ✅ 103% M | torch 159.9%, torch-compile 159.7% | - |
| 🔴 | FFTC2CFwdOp | test_fft_bench[fft-4k-c64-unbatched-complex64] | 0.0082 | 0.03 | 0.01 | <sub>lat-bound</sub> | torch-cufft 66.3%, torch-compile 67.1% | - |
| 🔴 | FFTC2CFwdOp | test_fft_bench[fft-4k-c64-b64-complex64] | 0.0152 | 1.03 | 0.28 | <sub>lat-bound</sub> | torch-cufft 37.2%, torch-compile 36.8% | - |
| 🔴 | FFTC2CFwdOp | test_fft_bench[fft-4k-c128-b64-complex128] | 0.0205 | 0.77 | 0.41 | 10% M | torch-cufft 41.4%, torch-compile 41.4% | - |
| 🟢 | FP8LightningIndexerFwdOp | test_fp8_lightning_indexer_bench[lightning-indexer-s8k-h32-d64-bfloat16] | 0.6177 | 55.63 | 1.80 | 44% M | torch-ref 18135.9%, torch-compile 8053.3% | - |
| 🟡 | FP8QuantFwdOp | test_fp8_quant_bench[kv-index-8k-d64-float16] | 0.0028 | 1.15 | 0.58 | <sub>lat-bound</sub> | torch-ref 605.8%, torch-compile 98.8% | - |
| 🟡 | FP8QuantFwdOp | test_fp8_quant_bench[kv-index-8k-d64-bfloat16] | 0.0028 | 1.15 | 0.58 | <sub>lat-bound</sub> | torch-ref 611.6%, torch-compile 90.7% | - |
| 🔵 | FP8QuantFwdOp | test_fp8_quant_bench[kv-index-4k-d128-float32] | 0.0039 | 0.80 | 0.67 | <sub>lat-bound</sub> | torch-ref 391.9%, torch-compile 106.5% | - |
| 🔵 | FloorDivideFwdOp | test_binary_arith_bench[floor_divide-1024x4096-float16-float16-FloorDivideFwdOp-floor_divide-positive] | 0.0087 | 0.48 | 2.89 | - | torch 302.9%, torch-compile 100.4% | - |
| 🔵 | FloorDivideFwdOp | test_binary_arith_bench[floor_divide-1024x10240-float16-float16-FloorDivideFwdOp-floor_divide-positive] | 0.0180 | 0.58 | 3.50 | - | torch 330.4%, torch-compile 100.2% | - |
| 🔵 | FloorDivideFwdOp | test_floor_divide_manifest_bench[hidden-state-prefill-float16] | 0.0151 | 1.11 | 3.33 | 82% M | torch 320.8%, torch-compile 100.2% | - |
| 🔵 | FloorDivideFwdOp | test_floor_divide_manifest_bench[hidden-state-prefill-bfloat16] | 0.0149 | 1.13 | 3.38 | 83% M | torch 338.5%, torch-compile 100.2% | - |
| 🔵 | FloorDivideFwdOp | test_floor_divide_manifest_bench[hidden-state-prefill-float32] | 0.0264 | 0.64 | 3.81 | ✅ 94% M | torch 180.0%, torch-compile 100.4% | - |
| 🟡 | FloorDivideFwdOp | test_floor_divide_manifest_bench[cnn-feat-broadcast-float16] | 0.0170 | 1.51 | 3.03 | 74% M | torch 644.1%, torch-compile 93.0% | - |
| 🟡 | FloorDivideFwdOp | test_floor_divide_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0169 | 1.52 | 3.04 | 75% M | torch 681.1%, torch-compile 94.1% | - |
| 🟡 | FloorDivideFwdOp | test_floor_divide_manifest_bench[cnn-feat-broadcast-float32] | 0.0269 | 0.95 | 3.82 | ✅ 94% M | torch 377.1%, torch-compile 99.2% | - |
| 🔵 | FloorFwdOp | test_floor_bench[elementwise-16M-float16] | 0.0179 | 0.94 | 3.76 | ✅ 92% M | torch 100.4%, torch-compile 100.4% | - |
| 🔵 | FloorFwdOp | test_floor_bench[elementwise-16M-bfloat16] | 0.0179 | 0.94 | 3.76 | ✅ 92% M | torch 100.5%, torch-compile 100.4% | - |
| 🟡 | FloorFwdOp | test_floor_bench[elementwise-16M-float32] | 0.0340 | 0.49 | 3.95 | ✅ 97% M | torch 99.8%, torch-compile 99.8% | - |
| 🔵 | FloorFwdOp | test_floor_bench[elementwise-256M-float16] | 0.2500 | 1.07 | 4.30 | ⚠️ 106% M | torch 100.2%, torch-compile 100.4% | - |
| 🟡 | FloorFwdOp | test_floor_bench[elementwise-256M-bfloat16] | 0.2499 | 1.07 | 4.30 | ⚠️ 106% M | torch 100.2%, torch-compile 99.9% | - |
| 🔵 | FusedAddLayerNormFwdOp | test_fused_add_layer_norm_bench[llama-8b-prefill-float16] | 0.0211 | 2.39 | 3.18 | 78% M | torch-ref 550.1%, torch-compile 130.5% | - |
| 🔵 | FusedAddLayerNormFwdOp | test_fused_add_layer_norm_bench[llama-8b-prefill-bfloat16] | 0.0220 | 2.29 | 3.05 | 75% M | torch-ref 532.8%, torch-compile 131.3% | - |
| 🔵 | FusedAddLayerNormFwdOp | test_fused_add_layer_norm_bench[llama-8b-decode-bfloat16] | 0.0031 | 0.01 | 0.02 | <sub>lat-bound</sub> | torch-ref 602.0%, torch-compile 118.4% | - |
| 🔵 | FusedAddLayerNormFwdOp | test_fused_add_layer_norm_bench[llama-70b-prefill-float16] | 0.0442 | 2.28 | 3.04 | 75% M | torch-ref 514.9%, torch-compile 101.7% | - |
| 🟡 | FusedAddLayerNormFwdOp | test_fused_add_layer_norm_bench[llama-70b-prefill-bfloat16] | 0.0474 | 2.12 | 2.83 | 70% M | torch-ref 483.7%, torch-compile 97.3% | - |
| 🔵 | FusedAddLayerNormFwdOp | test_fused_add_layer_norm_bench[llama-70b-decode-bfloat16] | 0.0041 | 0.01 | 0.02 | <sub>lat-bound</sub> | torch-ref 628.7%, torch-compile 136.4% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-8b-prefill-float16] | 0.0208 | 2.02 | 3.23 | 79% M | flashinfer 92.9%, vllm 90.1%, torch-ref 1285.2%, torch-compile 94.0% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-8b-prefill-bfloat16] | 0.0213 | 1.97 | 3.14 | 77% M | flashinfer 90.5%, vllm 89.7%, torch-ref 1260.6%, torch-compile 92.3% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-8b-decode-bfloat16] | 0.0028 | 0.01 | 0.01 | <sub>lat-bound</sub> | flashinfer 84.3%, vllm 108.1%, torch-ref 1046.5%, torch-compile 117.5% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-70b-prefill-float16] | 0.0378 | 2.22 | 3.55 | 87% M | flashinfer 95.6%, vllm 95.0%, torch-ref 1359.2%, torch-compile 96.4% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-70b-prefill-bfloat16] | 0.0381 | 2.20 | 3.53 | 87% M | flashinfer 95.2%, vllm 95.9%, torch-ref 1358.2%, torch-compile 95.9% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-70b-decode-bfloat16] | 0.0035 | 0.01 | 0.02 | <sub>lat-bound</sub> | flashinfer 82.6%, vllm 100.9%, torch-ref 859.6%, torch-compile 84.9% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-405b-prefill-float16] | 0.0766 | 2.19 | 3.50 | 86% M | flashinfer 93.1%, vllm 101.5%, torch-ref 1284.1%, torch-compile 94.1% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-405b-prefill-bfloat16] | 0.0851 | 1.97 | 3.15 | 77% M | flashinfer 84.0%, vllm 91.8%, torch-ref 1163.9%, torch-compile 84.8% | - |
| 🔴 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-405b-decode-bfloat16] | 0.0062 | 0.01 | 0.03 | <sub>lat-bound</sub> | flashinfer 68.6%, vllm 80.4%, torch-ref 510.8%, torch-compile 94.3% | - |
| 🔵 | FusedMoEExpertsNopadPersistent3WGFwdOp | test_moe_experts_nopad_bench[qwen3-235b-decode-bfloat16] | 2.7727 | 130.12 | 4.07 | ✅ 100% M | vllm-triton 102.9% | - |
| 🔵 | FusedMoEExpertsNopadPersistent3WGFwdOp | test_moe_experts_nopad_bench[qwen3-235b-prefill-bfloat16] | 5.9580 | 484.42 | 1.91 | 69% C | vllm-triton 119.5% | - |
| 🔵 | FusedMoEExpertsNopadPersistent3WGFwdOp | test_moe_experts_nopad_bench[deepseek-v3-decode-bfloat16] | 5.4158 | 66.62 | 4.17 | ✅ 102% M | vllm-triton 101.8% | - |
| 🔵 | FusedMoEExpertsNopadPersistent3WGFwdOp | test_moe_experts_nopad_bench[deepseek-v3-prefill-bfloat16] | 8.3547 | 345.46 | 2.71 | 67% M | vllm-triton 106.0% | - |
|  | FusedMoEExpertsNopadPersistent3WGFwdOp | test_moe_experts_nopad_bench[deepseek-v3-ep2-decode-bfloat16] | 2.7273 | 132.28 | 4.14 | ✅ 102% M | - | - |
|  | FusedMoEExpertsNopadPersistent3WGFwdOp | test_moe_experts_nopad_bench[deepseek-v3-ep2-prefill-bfloat16] | 4.1258 | 699.54 | 2.76 | ✅ 100% C | - | - |
| 🔵 | FusedMoeFwdOp | test_fused_moe_fwd_bench[qwen3-235b-decode-bfloat16] | 2.7738 | 130.06 | 4.07 | - | vllm 103.1% | - |
| 🔵 | FusedMoeFwdOp | test_fused_moe_fwd_bench[qwen3-235b-prefill-bfloat16] | 6.0711 | 475.40 | 1.88 | - | vllm 118.7% | - |
| 🔵 | FusedMoeFwdOp | test_fused_moe_fwd_bench[deepseek-v3-decode-bfloat16] | 5.4246 | 66.51 | 4.16 | - | vllm 101.7% | - |
| 🔵 | FusedMoeFwdOp | test_fused_moe_fwd_bench[deepseek-v3-prefill-bfloat16] | 8.3481 | 345.74 | 2.72 | - | vllm 107.1% | - |
| 🟢 | FusedMoeFwdOp | test_fused_moe_fwd_bench[kimi-k2-decode-bfloat16] | 3.9020 | 92.46 | 5.78 | - | torch-ref 1451.4% | - |
| 🟢 | FusedMoeFwdOp | test_fused_moe_fwd_bench[kimi-k2-prefill-bfloat16] | 7.8792 | 366.31 | 2.88 | - | torch-ref 1787.0% | - |
| 🟡 | FusedTopKOp | test_fused_topk_bench[1-384-8-sigmoid-renormalize] | 0.0083 | 0.00 | 0.00 | - | vllm 99.2% | - |
| 🟡 | FusedTopKOp | test_fused_topk_bench[32-384-8-sigmoid-renormalize] | 0.0119 | 0.02 | 0.00 | - | vllm 81.5% | - |
| 🟡 | FusedTopKOp | test_fused_topk_bench[512-384-8-sigmoid-renormalize] | 0.0126 | 0.28 | 0.03 | - | vllm 83.2% | - |
| 🔵 | FusedTopKOp | test_fused_topk_bench[4096-384-8-sigmoid-renormalize] | 0.0202 | 1.40 | 0.17 | - | vllm 117.4% | - |
| 🔵 | FusedTopKOp | test_fused_topk_bench[1-128-8-softmax-norenormalize] | 0.0043 | 0.00 | 0.00 | - | vllm 142.1% | - |
| 🔵 | FusedTopKOp | test_fused_topk_bench[32-128-8-softmax-norenormalize] | 0.0074 | 0.01 | 0.00 | - | vllm 113.0% | - |
| 🔵 | FusedTopKOp | test_fused_topk_bench[512-128-8-softmax-norenormalize] | 0.0078 | 0.15 | 0.02 | - | vllm 115.6% | - |
| 🔵 | FusedTopKOp | test_fused_topk_bench[4096-128-8-softmax-norenormalize] | 0.0110 | 0.86 | 0.12 | - | vllm 147.2% | - |
| 🟡 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s2k-h4-d64-float16] | 0.1829 | 1.47 | 0.17 | 4% M | fla 81.0% | - |
| 🟡 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s2k-h4-d64-bfloat16] | 0.1845 | 1.45 | 0.17 | 4% M | fla 80.3% | - |
| 🔴 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s4k-h4-d64-float16] | 0.3692 | 1.45 | 0.17 | 4% M | fla 78.0% | - |
| 🔴 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s4k-h4-d64-bfloat16] | 0.3648 | 1.47 | 0.17 | 4% M | fla 78.9% | - |
| 🔴 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s8k-h4-d64-float16] | 0.7455 | 1.44 | 0.17 | 4% M | fla 74.7% | - |
| 🔴 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s8k-h4-d64-bfloat16] | 0.7262 | 1.48 | 0.17 | 4% M | fla 76.8% | - |
| 🔴 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s16k-h4-d64-float16] | 1.5171 | 1.42 | 0.17 | 4% M | fla 71.3% | - |
| 🔴 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s16k-h4-d64-bfloat16] | 1.4514 | 1.48 | 0.17 | 4% M | fla 74.5% | - |
| 🟡 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b1-h8-d128-bfloat16] | 0.0074 | 0.07 | 0.07 | <sub>lat-bound</sub> | fla 91.0%, torch 409.5%, torch-compile 81.0% | - |
| 🟡 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b1-h16-d128-bfloat16] | 0.0074 | 0.14 | 0.14 | <sub>lat-bound</sub> | fla 94.8%, torch 428.5%, torch-compile 92.2% | - |
| 🟡 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b1-h32-d128-bfloat16] | 0.0078 | 0.27 | 0.27 | <sub>lat-bound</sub> | fla 93.5%, torch 457.1%, torch-compile 99.6% | - |
| 🔵 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b1-h48-d128-bfloat16] | 0.0079 | 0.40 | 0.40 | <sub>lat-bound</sub> | fla 113.3%, torch 509.3%, torch-compile 130.8% | - |
| 🔵 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b1-h64-d128-bfloat16] | 0.0081 | 0.52 | 0.53 | <sub>lat-bound</sub> | fla 107.5%, torch 516.9%, torch-compile 108.3% | - |
| 🔵 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b8-h32-d128-bfloat16] | 0.0159 | 1.06 | 1.08 | 26% M | fla 110.7%, torch 564.5%, torch-compile 133.3% | - |
| 🟡 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b8-h48-d128-bfloat16] | 0.0231 | 1.10 | 1.11 | 27% M | fla 96.7%, torch 523.3%, torch-compile 106.5% | - |
| 🟡 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b8-h64-d128-bfloat16] | 0.0305 | 1.10 | 1.12 | 28% M | fla 88.0%, torch 517.6%, torch-compile 105.2% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-float16] | 0.0984 | 1.36 | 0.11 | 3% M | fla 71.4% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-bfloat16] | 0.0968 | 1.39 | 0.11 | 3% M | fla 68.0% | - |
| 🟡 | GLAFwdOp | test_gla_fwd_bench[gla-init-b2-s4k-h4-d64-float16] | 0.1568 | 1.71 | 0.13 | 3% M | fla 80.1% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-init-b2-s4k-h4-d64-bfloat16] | 0.1564 | 1.72 | 0.13 | 3% M | fla 76.4% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-float16] | 0.3127 | 1.72 | 0.13 | 3% M | fla 79.3% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-bfloat16] | 0.3120 | 1.72 | 0.13 | 3% M | fla 70.4% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-float16] | 0.6181 | 1.74 | 0.14 | 3% M | fla 75.1% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-bfloat16] | 0.6116 | 1.76 | 0.14 | 3% M | fla 73.9% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-float16] | 0.0865 | 12.41 | 0.20 | 5% M | fla 77.7% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-bfloat16] | 0.0867 | 12.39 | 0.20 | 5% M | fla 77.8% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-float16] | 0.1488 | 14.44 | 0.23 | 6% M | fla 72.4% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-bfloat16] | 0.1445 | 14.86 | 0.23 | 6% M | fla 74.9% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-float16] | 0.3140 | 13.68 | 0.21 | 5% M | fla 65.3% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-bfloat16] | 0.3166 | 13.56 | 0.21 | 5% M | fla 64.9% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-float16] | 0.6359 | 13.51 | 0.21 | 5% M | fla 61.5% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-bfloat16] | 0.6378 | 13.47 | 0.21 | 5% M | fla 61.7% | - |
| 🔵 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s2k-h4-d64-float16] | 0.0669 | 16.04 | 0.25 | 6% M | fla 100.3% | - |
| 🔵 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s2k-h4-d64-bfloat16] | 0.0664 | 16.16 | 0.25 | 6% M | fla 101.5% | - |
| 🟡 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s4k-h4-d64-float16] | 0.1151 | 18.66 | 0.29 | 7% M | fla 93.5% | - |
| 🟡 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s4k-h4-d64-bfloat16] | 0.1145 | 18.75 | 0.29 | 7% M | fla 94.5% | - |
| 🟡 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s8k-h4-d64-float16] | 0.2193 | 19.59 | 0.31 | 7% M | fla 93.5% | - |
| 🟡 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s8k-h4-d64-bfloat16] | 0.2204 | 19.49 | 0.31 | 7% M | fla 93.3% | - |
| 🟡 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s16k-h4-d64-float16] | 0.4289 | 20.03 | 0.31 | 8% M | fla 91.1% | - |
| 🟡 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s16k-h4-d64-bfloat16] | 0.4323 | 19.87 | 0.31 | 8% M | fla 91.0% | - |
| 🟢 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s32k-h4-d64-float16] | 0.1955 | 87.90 | 1.38 | 31% M | fla 392.9% | - |
| 🟢 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s32k-h4-d64-bfloat16] | 0.1951 | 88.04 | 1.38 | 31% M | fla 394.4% | - |
| 🔵 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b1-s4k-h16-d128-float16] | 0.1748 | 58.35 | 0.77 | 19% M | fla 110.8% | - |
| 🔵 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b1-s4k-h16-d128-bfloat16] | 0.1745 | 58.46 | 0.77 | 19% M | fla 111.4% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-float16] | 0.2017 | 1.33 | 0.08 | 2% M | fla 66.3% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-bfloat16] | 0.2049 | 1.31 | 0.08 | 2% M | fla 68.3% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-float16] | 0.3809 | 1.41 | 0.09 | 2% M | fla 65.5% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-bfloat16] | 0.3876 | 1.39 | 0.09 | 2% M | fla 66.7% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-float16] | 0.7246 | 1.48 | 0.09 | 2% M | fla 67.2% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-bfloat16] | 0.7502 | 1.43 | 0.09 | 2% M | fla 66.9% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-float16] | 1.4273 | 1.50 | 0.09 | 2% M | fla 64.5% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-bfloat16] | 1.4652 | 1.47 | 0.09 | 2% M | fla 65.1% | - |
| 🔵 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b1-h8-d128-bfloat16] | 0.0031 | 0.25 | 0.17 | <sub>lat-bound</sub> | fla 127.8% | - |
| 🔵 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b1-h16-d128-bfloat16] | 0.0033 | 0.47 | 0.32 | <sub>lat-bound</sub> | fla 126.0% | - |
| 🔵 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b1-h32-d128-bfloat16] | 0.0036 | 0.86 | 0.58 | <sub>lat-bound</sub> | fla 128.1% | - |
| 🔵 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b1-h48-d128-bfloat16] | 0.0039 | 1.23 | 0.83 | <sub>lat-bound</sub> | fla 136.1% | - |
| 🔵 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b1-h64-d128-bfloat16] | 0.0042 | 1.50 | 1.02 | <sub>lat-bound</sub> | fla 138.2% | - |
| 🟢 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b8-h32-d128-bfloat16] | 0.0087 | 2.90 | 1.96 | 48% M | fla 167.7% | - |
| 🟢 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b8-h48-d128-bfloat16] | 0.0124 | 3.05 | 2.06 | 51% M | fla 155.7% | - |
| 🟢 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b8-h64-d128-bfloat16] | 0.0161 | 3.13 | 2.11 | 52% M | fla 156.2% | - |
| 🔴 | GatedDeltaNetPrefillBHTDFwdOp | test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-float16] | 0.2511 | 34.21 | 0.34 | 8% M | fla 78.1% | - |
| 🔴 | GatedDeltaNetPrefillBHTDFwdOp | test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-bfloat16] | 0.2527 | 34.00 | 0.34 | 8% M | fla 78.4% | - |
| 🟡 | GatedDeltaNetPrefillBHTDFwdOp | test_gated_deltanet_prefill_bhtd_bench[bhtd-qwen35-gdn-prefill-b1-s128k-h64-d128-float16] | 17.4167 | 63.13 | 0.62 | 15% M | fla 89.7% | - |
| 🟡 | GatedDeltaNetPrefillBHTDFwdOp | test_gated_deltanet_prefill_bhtd_bench[bhtd-qwen35-gdn-prefill-b1-s128k-h64-d128-bfloat16] | 17.5483 | 62.66 | 0.61 | 15% M | fla 88.8% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[fallback-gdn-prefill-b1-s4k-h16-d128-bthd-float16] | 0.0792 | 108.50 | 1.07 | 26% M | fla 248.0% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[fallback-gdn-prefill-b1-s4k-h16-d128-bthd-bfloat16] | 0.0794 | 108.17 | 1.07 | 26% M | fla 248.6% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h16-d128-bthd-float16] | 0.3656 | 187.99 | 1.84 | 45% M | fla 400.6% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h16-d128-bthd-bfloat16] | 0.3726 | 184.43 | 1.81 | 44% M | fla 394.5% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h16-d128-bthd-float16] | 0.6962 | 197.42 | 1.93 | 48% M | fla 417.6% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h16-d128-bthd-bfloat16] | 0.7062 | 194.62 | 1.91 | 47% M | fla 412.7% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h16-d128-bthd-float16] | 1.2609 | 218.01 | 2.14 | 52% M | fla 457.2% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h16-d128-bthd-bfloat16] | 1.2839 | 214.09 | 2.10 | 52% M | fla 449.2% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h32-d128-bthd-float16] | 0.6836 | 201.05 | 1.97 | 48% M | fla 324.2% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h32-d128-bthd-bfloat16] | 0.6976 | 197.02 | 1.93 | 47% M | fla 318.2% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h32-d128-bthd-float16] | 1.2466 | 220.51 | 2.16 | 53% M | fla 352.6% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h32-d128-bthd-bfloat16] | 1.2796 | 214.81 | 2.11 | 52% M | fla 344.1% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h32-d128-bthd-float16] | 2.4489 | 224.49 | 2.20 | 54% M | fla 357.3% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h32-d128-bthd-bfloat16] | 2.5070 | 219.29 | 2.15 | 53% M | fla 349.9% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h48-d128-bthd-float16] | 1.0517 | 196.02 | 1.92 | 47% M | fla 301.2% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h48-d128-bthd-bfloat16] | 1.0654 | 193.50 | 1.90 | 47% M | fla 296.6% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h48-d128-bthd-float16] | 1.9123 | 215.61 | 2.11 | 52% M | fla 330.4% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h48-d128-bthd-bfloat16] | 1.9426 | 212.25 | 2.08 | 51% M | fla 324.5% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h48-d128-bthd-float16] | 3.7748 | 218.46 | 2.14 | 53% M | fla 333.8% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h48-d128-bthd-bfloat16] | 3.8114 | 216.36 | 2.12 | 52% M | fla 330.4% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h64-d128-bthd-float16] | 1.2227 | 224.81 | 2.20 | 54% M | fla 319.3% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h64-d128-bthd-bfloat16] | 1.2536 | 219.26 | 2.15 | 53% M | fla 310.5% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h64-d128-bthd-float16] | 2.3787 | 231.12 | 2.26 | 56% M | fla 327.9% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h64-d128-bthd-bfloat16] | 2.4342 | 225.84 | 2.21 | 54% M | fla 319.9% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h64-d128-bthd-float16] | 4.6651 | 235.69 | 2.31 | 57% M | fla 335.0% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h64-d128-bthd-bfloat16] | 4.7838 | 229.84 | 2.25 | 55% M | fla 325.7% | - |
| 🔵 | GeFwdOp | test_comparison_bench[ge-1024x4096-float16-ge] | 0.0076 | 0.56 | 2.78 | - | torch 103.0%, torch-compile 103.0% | - |
| 🔵 | GeFwdOp | test_ge_manifest_bench[hidden-state-prefill-float16] | 0.0132 | 0.64 | 3.18 | 78% M | torch 100.0%, torch-compile 100.1% | - |
| 🔵 | GeFwdOp | test_ge_manifest_bench[hidden-state-prefill-bfloat16] | 0.0130 | 0.64 | 3.22 | 79% M | torch 100.5%, torch-compile 100.5% | - |
| 🟡 | GeFwdOp | test_ge_manifest_bench[hidden-state-prefill-float32] | 0.0224 | 0.37 | 3.37 | 83% M | torch 99.9%, torch-compile 99.7% | - |
| 🔴 | GeFwdOp | test_ge_manifest_bench[cnn-feat-broadcast-float16] | 0.0172 | 0.75 | 2.24 | 55% M | torch 272.9%, torch-compile 68.5% | - |
| 🔴 | GeFwdOp | test_ge_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0172 | 0.75 | 2.24 | 55% M | torch 276.9%, torch-compile 69.8% | - |
| 🟡 | GeFwdOp | test_ge_manifest_bench[cnn-feat-broadcast-float32] | 0.0213 | 0.60 | 3.01 | 74% M | torch 219.9%, torch-compile 86.2% | - |
| 🔵 | GeluAndMulFwdOp | test_gelu_and_mul_bench[ffn-gelu-prefill-float16] | 0.0550 | 3.20 | 3.20 | 79% M | flashinfer 191.0%, torch-ref 369.3%, torch-compile 109.9% | - |
| 🔵 | GeluAndMulFwdOp | test_gelu_and_mul_bench[ffn-gelu-prefill-bfloat16] | 0.0597 | 2.95 | 2.95 | 73% M | flashinfer 177.8%, torch-ref 343.4%, torch-compile 102.2% | - |
| 🔵 | GeluAndMulFwdOp | test_gelu_and_mul_bench[ffn-gelu-decode-bfloat16] | 0.0015 | 0.06 | 0.06 | <sub>lat-bound</sub> | flashinfer 442.6%, torch-ref 212.8%, torch-compile 102.1% | - |
| 🟡 | GeluFwdOp | test_gelu_manifest_bench[llama-8b-ffn-prefill-float16] | 0.0526 | 2.79 | 2.23 | 55% M | torch 90.8%, torch-compile 102.5% | - |
| 🟡 | GeluFwdOp | test_gelu_manifest_bench[llama-8b-ffn-prefill-bfloat16] | 0.0552 | 2.66 | 2.13 | 52% M | torch 88.2%, torch-compile 101.3% | - |
| 🔵 | GeluFwdOp | test_gelu_manifest_bench[llama-8b-ffn-decode-bfloat16] | 0.0014 | 0.05 | 0.04 | <sub>lat-bound</sub> | torch 113.3%, torch-compile 100.0% | - |
| 🔵 | GeluTanhAndMulFwdOp | test_gelu_tanh_and_mul_bench[ffn-gelu-tanh-prefill-float16] | 0.0476 | 6.16 | 3.70 | ✅ 91% M | flashinfer 118.3%, torch-ref 402.7%, torch-compile 108.2% | - |
| 🔵 | GeluTanhAndMulFwdOp | test_gelu_tanh_and_mul_bench[ffn-gelu-tanh-prefill-bfloat16] | 0.0493 | 5.95 | 3.57 | 88% M | flashinfer 116.8%, torch-ref 392.3%, torch-compile 106.5% | - |
| 🟡 | GeluTanhAndMulFwdOp | test_gelu_tanh_and_mul_bench[ffn-gelu-tanh-decode-bfloat16] | 0.0015 | 0.10 | 0.06 | <sub>lat-bound</sub> | flashinfer 291.5%, torch-ref 203.2%, torch-compile 99.9% | - |
| 🟢 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-decode-gate-up-per-tensor-float8_e4m3fn] | 0.1160 | 33.40 | 0.14 | 4% M | torch-scaled-mm 208.9% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-decode-down-per-tensor-float8_e4m3fn] | 0.0254 | 147.73 | 0.66 | 16% M | torch-scaled-mm 961.7%, deepgemm 40.8% | - |
| 🟢 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-prefill-gate-up-per-tensor-float8_e4m3fn] | 0.5109 | 242.75 | 0.12 | 19% C | torch-scaled-mm 675.4% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-prefill-down-per-tensor-float8_e4m3fn] | 0.2103 | 571.92 | 0.39 | 46% C | torch-scaled-mm 1590.0%, deepgemm 50.2% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-decode-gate-up-block128-float8_e4m3fn] | 0.1482 | 26.15 | 0.12 | 3% M | torch-scaled-mm 188.4%, flashinfer-fp8-blockscale-sm90 8.7% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-decode-down-block128-float8_e4m3fn] | 0.0378 | 99.44 | 0.46 | 11% M | torch-scaled-mm 738.9%, flashinfer-fp8-blockscale-sm90 24.5% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-prefill-gate-up-block128-float8_e4m3fn] | 0.3850 | 322.16 | 0.16 | 26% C | torch-scaled-mm 917.5%, flashinfer-fp8-blockscale-sm90 36.1% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-prefill-down-block128-float8_e4m3fn] | 0.4458 | 269.78 | 0.19 | 22% C | torch-scaled-mm 762.0%, flashinfer-fp8-blockscale-sm90 32.3% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-prefill-attn-proj-block128-float8_e4m3fn] | 0.7706 | 312.12 | 0.12 | 25% C | torch-scaled-mm 866.3%, flashinfer-fp8-blockscale-sm90 27.8% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[k-dominant-7168x16384-block128-float8_e4m3fn] | 3.5890 | 268.06 | 0.07 | 21% C | torch-scaled-mm 734.6%, flashinfer-fp8-blockscale-sm90 21.9% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[wide-n-24576-block128-float8_e4m3fn] | 1.0264 | 301.27 | 0.24 | 24% C | torch-scaled-mm 830.1%, flashinfer-fp8-blockscale-sm90 37.3% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[small-batch-down-m8-per-tensor-float8_e4m3fn] | 0.0266 | 8.83 | 0.56 | 14% M | torch-scaled-mm 625.9%, deepgemm 31.2% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[gemv-down-m1-per-tensor-float8_e4m3fn] | 0.0259 | 1.13 | 0.57 | 14% M | torch-scaled-mm 503.7%, deepgemm 39.2% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[gemv-down-m1-block128-float8_e4m3fn] | 0.0447 | 0.66 | 0.34 | 8% M | torch-scaled-mm 368.1%, flashinfer-fp8-blockscale-sm90 17.4% | - |
| 🟢 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-decode-gate-up-per-tensor-bias-float8_e4m3fn] | 0.1169 | 33.14 | 0.14 | 3% M | torch-scaled-mm 212.2% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[square-1k-nn-float16] | 0.0145 | 148.47 | 0.43 | 22% C | torch-cublas 50.0%, flaggems 79.4% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[square-1k-nn-bfloat16] | 0.0145 | 148.48 | 0.43 | 21% C | torch-cublas 49.8%, flaggems 80.3% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[ds-v3-decode-gate-up-bfloat16] | 0.0677 | 57.23 | 0.48 | 12% M | torch-cublas 25.5%, deepgemm 31.6% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[ds-v3-decode-down-bfloat16] | 0.0246 | 152.52 | 1.29 | 32% M | torch-cublas 53.4%, deepgemm 55.8% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[ds-v3-prefill-gate-up-bfloat16] | 0.3376 | 367.37 | 0.31 | 52% C | torch-cublas 52.3%, deepgemm 53.5% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[ds-v3-prefill-down-bfloat16] | 0.3216 | 373.94 | 0.33 | 53% C | torch-cublas 55.9%, deepgemm 55.9% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[ds-v3-prefill-attn-proj-float16] | 0.5446 | 441.61 | 0.28 | 67% C | torch-cublas 61.4% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[ds-v3-prefill-attn-proj-bfloat16] | 0.5399 | 445.51 | 0.28 | 64% C | torch-cublas 61.5%, deepgemm 61.5% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[k-dominant-7168x16384-bfloat16] | 2.0590 | 467.24 | 0.21 | 67% C | torch-cublas 61.1%, deepgemm 61.1% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[wide-n-24576-bfloat16] | 0.8996 | 343.74 | 0.32 | 49% C | torch-cublas 50.3%, deepgemm 49.4% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[mid-m16-attn-bfloat16] | 0.0658 | 14.27 | 0.90 | 22% M | torch-cublas 37.2%, deepgemm 51.4% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[mid-m32-attn-bfloat16] | 0.0661 | 28.43 | 0.90 | 22% M | torch-cublas 36.8%, deepgemm 46.2% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[mid-m64-down-bfloat16] | 0.0207 | 90.90 | 1.48 | 36% M | torch-cublas 63.8%, deepgemm 65.2% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[mid-m96-gate-up-bfloat16] | 0.0687 | 42.31 | 0.47 | 11% M | torch-cublas 24.7%, deepgemm 31.9% | - |
| 🔴 | GemmW4A16FwdOp | test_gemm_w4a16_bench[compile-smoke-square-64x64x128-float16] | 0.0043 | 0.24 | 0.01 | <sub>lat-bound</sub> | torch-dequantized-matmul 62.7% | - |
| 🔴 | GemmW4A16FwdOp | test_gemm_w4a16_bench[compile-smoke-rect-128x256x256-float16] | 0.0058 | 2.87 | 0.03 | <sub>lat-bound</sub> | torch-dequantized-matmul 52.6% | - |
| 🔴 | GemmW4A16FwdOp | test_gemm_w4a16_bench[decode-l2-resident-ish-float16] | 0.0329 | 4.08 | 1.10 | 27% M | torch-dequantized-matmul 142.3%, marlin-fp32 66.5%, marlin-fp16 66.3% | - |
| 🔴 | GemmW4A16FwdOp | test_gemm_w4a16_bench[decode-hbm-streaming-threshold-float16] | 0.0606 | 4.43 | 1.19 | 29% M | torch-dequantized-matmul 123.3%, marlin-fp32 62.6%, marlin-fp16 62.7% | - |
| 🔴 | GemmW4A16FwdOp | test_gemm_w4a16_bench[decode-non-power2-low-cta-float16] | 0.0743 | 3.95 | 1.07 | 26% M | torch-dequantized-matmul 118.0%, marlin-fp32 54.6%, marlin-fp16 55.0% | - |
| 🔴 | GemmW4A16FwdOp | test_gemm_w4a16_bench[decode-long-k-pressure-float16] | 0.2836 | 4.73 | 1.28 | 31% M | torch-dequantized-matmul 113.8%, marlin-fp32 49.8%, marlin-fp16 49.7% | - |
| 🔵 | GroupNormFwdOp | test_group_norm_bench[image-g32-affine-float16] | 0.0037 | 1.41 | 1.13 | <sub>lat-bound</sub> | flaggems 108.6%, torch 411.2%, torch-compile 132.8% | - |
| 🔵 | GroupNormFwdOp | test_group_norm_bench[image-g32-affine-bfloat16] | 0.0037 | 1.41 | 1.13 | <sub>lat-bound</sub> | flaggems 108.6%, torch 411.2%, torch-compile 135.3% | - |
| 🔴 | GroupNormFwdOp | test_group_norm_bench[wider-channel-g32-affine-float16] | 0.0059 | 0.68 | 0.54 | <sub>lat-bound</sub> | flaggems 66.8%, torch 274.4%, torch-compile 76.6% | - |
| 🔴 | GroupNormFwdOp | test_group_norm_bench[tail-spatial-g16-affine-float16] | 0.0060 | 0.38 | 0.30 | <sub>lat-bound</sub> | flaggems 67.2%, torch 253.7%, torch-compile 73.5% | - |
| 🔵 | GroupNormFwdOp | test_group_norm_no_affine_bench[image-g32-float16] | 0.0036 | 0.89 | 1.18 | <sub>lat-bound</sub> | flaggems 100.9%, torch 371.2%, torch-compile 123.4% | - |
| 🔵 | GroupNormFwdOp | test_group_norm_no_affine_bench[image-g32-bfloat16] | 0.0036 | 0.89 | 1.18 | <sub>lat-bound</sub> | flaggems 100.9%, torch 373.0%, torch-compile 119.8% | - |
| 🔴 | GroupNormFwdOp | test_group_norm_no_affine_bench[wider-channel-g32-float16] | 0.0048 | 0.50 | 0.67 | <sub>lat-bound</sub> | flaggems 72.7%, torch 295.3%, torch-compile 80.7% | - |
| 🔴 | GroupNormFwdOp | test_group_norm_no_affine_bench[tail-spatial-g16-float16] | 0.0052 | 0.26 | 0.35 | <sub>lat-bound</sub> | flaggems 68.9%, torch 255.5%, torch-compile 67.1% | - |
| 🟡 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-8b-short-float16] | 0.2030 | 105.78 | 0.33 | 16% C | fa3 81.8% | - |
| 🔴 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-8b-short-bfloat16] | 0.4155 | 51.68 | 0.16 | 7% C | fa3 39.8% | - |
| 🔴 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-8b-long-float16] | 0.8302 | 206.93 | 0.16 | 31% C | fa3 71.5% | - |
| 🔴 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-8b-long-bfloat16] | 1.2426 | 138.26 | 0.11 | 20% C | fa3 47.4% | - |
| 🟡 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-70b-short-float16] | 0.1964 | 109.34 | 0.30 | 17% C | fa3 81.0% | - |
| 🔴 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-70b-short-bfloat16] | 0.4087 | 52.55 | 0.14 | 8% C | fa3 38.9% | - |
| 🔴 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-70b-long-float16] | 0.8084 | 212.51 | 0.15 | 32% C | fa3 71.9% | - |
| 🔴 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 1.0192 | 168.56 | 0.12 | 24% C | fa3 56.8% | - |
| 🔴 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-8b-p64-float16] | 0.1669 | 12.87 | 0.10 | 3% M | flashinfer 75.0% | - |
| 🔵 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-8b-long-p64-float16] | 0.2205 | 19.47 | 0.61 | 15% M | flashinfer 135.8% | - |
| 🔴 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[throughput-8b-p64-float16] | 0.2518 | 8.53 | 0.04 | 1% C | flashinfer 59.8% | - |
| 🟡 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-70b-p64-float16] | 0.0497 | 21.62 | 0.34 | 8% M | flashinfer 89.6% | - |
| 🔴 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-8b-p256-float16] | 0.1682 | 12.77 | 0.10 | 2% M | fa3 48.3%, flashinfer 74.4% | - |
| 🔴 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-70b-p256-float16] | 0.0684 | 15.71 | 0.25 | 6% M | fa3 53.7%, flashinfer 83.7% | - |
| 🔴 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-405b-p256-float16] | 0.0563 | 19.06 | 0.30 | 7% M | fa3 47.2% | - |
| 🔴 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-8b-p64-softcap50-float16] | 0.1765 | 12.17 | 0.10 | 2% M | flashinfer 71.1% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-8b-4k-float16] | 0.1511 | 14.21 | 3.56 | 87% M | fa3 102.1%, flashinfer 148.5% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-8b-4k-bfloat16] | 0.1499 | 14.33 | 3.59 | 88% M | fa3 101.8%, flashinfer 171.1% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-8b-32k-float16] | 0.2578 | 16.66 | 4.17 | ✅ 102% M | fa3 104.4%, flashinfer 167.0% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-8b-32k-bfloat16] | 0.2564 | 16.75 | 4.19 | ✅ 103% M | fa3 104.5%, flashinfer 194.7% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-70b-4k-float16] | 0.0792 | 27.11 | 3.40 | 83% M | fa3 107.6%, flashinfer 252.0% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-70b-4k-bfloat16] | 0.0790 | 27.17 | 3.40 | 83% M | fa3 107.7%, flashinfer 287.6% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-70b-32k-float16] | 0.1379 | 31.15 | 3.89 | ✅ 95% M | fa3 109.0%, flashinfer 280.2% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-70b-32k-bfloat16] | 0.1375 | 31.24 | 3.91 | ✅ 95% M | fa3 108.8%, flashinfer 321.6% | - |
| 🟢 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-8b-4k-softcap50-float16] | 0.1617 | 13.28 | 3.32 | 81% M | torch-sdpa 8240.3% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-1k-float16] | 0.0070 | 2.40 | 0.30 | <sub>lat-bound</sub> | fa3 249.0%, flashinfer 139.0% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-4k-float16] | 0.0096 | 6.99 | 0.88 | <sub>lat-bound</sub> | fa3 222.0%, flashinfer 121.0% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-8k-float16] | 0.0131 | 10.23 | 1.28 | 31% M | fa3 177.3%, flashinfer 107.7% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-16k-float16] | 0.0182 | 14.72 | 1.84 | 45% M | fa3 153.5%, flashinfer 119.6% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-32k-float16] | 0.0283 | 18.96 | 2.37 | 58% M | fa3 132.8%, flashinfer 122.5% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-64k-float16] | 0.0455 | 23.60 | 2.95 | 72% M | fa3 126.7%, flashinfer 116.8% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-128k-float16] | 0.0764 | 28.09 | 3.51 | 86% M | fa3 121.7%, flashinfer 109.0% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-256k-float16] | 0.1364 | 31.48 | 3.93 | ✅ 97% M | fa3 118.5%, flashinfer 103.9% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-8b-short-float16] | 0.0370 | 232.41 | 1.13 | 35% C | fa3 86.1%, flashinfer 106.3% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-8b-short-bfloat16] | 0.0369 | 232.61 | 1.14 | 33% C | fa3 86.0%, flashinfer 106.0% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-8b-long-float16] | 0.1617 | 424.87 | 0.52 | 64% C | fa3 83.4%, flashinfer 100.5% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-8b-long-bfloat16] | 0.1609 | 427.02 | 0.52 | 61% C | fa3 82.3%, flashinfer 99.4% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-70b-short-float16] | 0.0382 | 225.01 | 0.99 | 34% C | fa3 83.5%, flashinfer 102.5% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-70b-short-bfloat16] | 0.0380 | 226.15 | 0.99 | 32% C | fa3 83.6%, flashinfer 103.3% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-70b-long-float16] | 0.1627 | 422.40 | 0.46 | 64% C | fa3 82.3%, flashinfer 99.7% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-70b-long-bfloat16] | 0.1619 | 424.36 | 0.47 | 61% C | fa3 82.0%, flashinfer 99.0% | - |
| 🔵 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-8b-prefill-dense-float16] | 0.0370 | 232.87 | 1.13 | 35% C | torch-ref 2977.2%, flashinfer 106.3% | - |
| 🔵 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-8b-prefill-dense-bfloat16] | 0.0370 | 232.87 | 1.13 | 33% C | torch-ref 2977.1%, flashinfer 105.6% | - |
| 🔵 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-8b-prefill-dense-sm-scale-0.125-float16] | 0.0371 | 232.26 | 1.13 | 35% C | torch-ref 2967.3%, flashinfer 106.4% | - |
| 🔵 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-8b-prefill-dense-softcap50-float16] | 0.0420 | 204.85 | 1.00 | 31% C | torch-ref 3082.2%, flashinfer 109.2% | - |
| 🟡 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-8b-prefill-dense-q-lt-kv-float16] | 0.1257 | 512.41 | 0.40 | 77% C | torch-ref 3258.3%, flashinfer 99.8% | - |
| 🟡 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-8b-prefill-dense-q-lt-kv-bfloat16] | 0.1249 | 515.76 | 0.40 | 74% C | torch-ref 3283.5%, flashinfer 99.4% | - |
| 🟡 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-70b-prefill-dense-q-lt-kv-float16] | 0.1253 | 514.18 | 0.27 | 78% C | torch-ref 3001.0%, flashinfer 99.5% | - |
| 🔵 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-70b-prefill-dense-q-lt-kv-bfloat16] | 0.1237 | 520.97 | 0.27 | 74% C | torch-ref 3040.3%, flashinfer 100.2% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s896-float16] | 0.0453 | 290.28 | 0.20 | 23% C | torch-sdpa-dequant 203.4%, fa3 62.6% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s896-bfloat16] | 0.0454 | 289.67 | 0.20 | 23% C | torch-sdpa-dequant 203.7%, fa3 62.6% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s1792-float16] | 0.1286 | 409.00 | 0.14 | 33% C | torch-sdpa-dequant 176.3%, fa3 66.9% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s1792-bfloat16] | 0.1288 | 408.59 | 0.14 | 33% C | torch-sdpa-dequant 175.2%, fa3 66.6% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s3584-float16] | 0.7486 | 562.23 | 0.09 | 45% C | torch-sdpa-dequant 140.5%, fa3 70.6% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s3584-bfloat16] | 0.7508 | 560.57 | 0.09 | 45% C | torch-sdpa-dequant 140.2%, fa3 70.6% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s7168-float16] | 2.8457 | 591.65 | 0.05 | 47% C | torch-sdpa-dequant 120.5%, fa3 71.2% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s7168-bfloat16] | 2.8493 | 590.90 | 0.05 | 47% C | torch-sdpa-dequant 120.4%, fa3 71.2% | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-prefill-paged-fullattn-b8-prefix32k-chunk1k-p64-partial-rope64-float16] | 60.5337 | 147.58 | 0.04 | 22% C | - | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-prefill-paged-fullattn-mixed-b8-p64-partial-rope64-float16] | 30.7740 | 107.85 | 0.04 | 16% C | - | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-prefill-paged-b8-prefix4k-chunk512-p64-full-rope-float16] | 1.9491 | 149.86 | 0.12 | 22% C | - | - |
| 🟡 | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[gqa-prefill-paged-softcap50-b4-prefix4k-chunk512-p64-float16] | 0.1496 | 122.02 | 0.10 | 16% C | fa3 91.6% | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-prefill-paged-fp8-cache-b8-prefix32k-chunk1k-p64-float16] | 56.0124 | 159.49 | 0.05 | 24% C | - | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-prefill-paged-fp8-cache-b8-prefix4k-chunk512-p64-float16] | 2.0018 | 145.92 | 0.12 | 22% C | - | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[gqa-prefill-paged-fp8-cache-softcap50-b4-prefix4k-chunk512-p64-float16] | 0.2070 | 88.20 | 0.07 | 12% C | - | - |
| 🔴 | GroupedQueryAttentionPrefillVarlenFwdOp | test_gqa_prefill_varlen_fwd_bench[llama-8b-prefill-varlen-uniform-fp16] | 0.1250 | 206.31 | 0.40 | - | torch-ref 1630.2%, fa3 57.1% | - |
| 🔴 | GroupedQueryAttentionPrefillVarlenFwdOp | test_gqa_prefill_varlen_fwd_bench[llama-8b-prefill-varlen-mixed-fp16] | 0.1401 | 143.81 | 0.28 | - | torch-ref 1196.1%, fa3 43.9% | - |
| 🔴 | GroupedQueryAttentionPrefillVarlenFwdOp | test_gqa_prefill_varlen_fwd_bench[llama-70b-prefill-varlen-q-lt-kv-bf16] | 0.1961 | 219.09 | 0.24 | - | torch-ref 1410.2%, fa3 50.2% | - |
| 🟡 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-8b-short-w256-float16] | 0.0397 | 162.86 | 1.06 | 26% M | fa3 85.8%, flashinfer 104.2% | - |
| 🟡 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0396 | 163.26 | 1.06 | 26% M | fa3 85.9%, flashinfer 104.0% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-8b-long-w1024-float16] | 0.1525 | 338.23 | 0.55 | 51% C | fa3 78.7%, flashinfer 101.3% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.1512 | 341.28 | 0.55 | 49% C | fa3 78.3%, flashinfer 101.7% | - |
| 🟡 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-70b-short-w256-float16] | 0.0396 | 163.39 | 0.95 | 25% C | fa3 86.3%, flashinfer 103.5% | - |
| 🟡 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-70b-short-w256-bfloat16] | 0.0396 | 163.39 | 0.95 | 23% M | fa3 86.0%, flashinfer 103.2% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-70b-long-w1024-float16] | 0.1528 | 337.63 | 0.49 | 51% C | fa3 78.6%, flashinfer 100.7% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.1513 | 340.99 | 0.50 | 49% C | fa3 78.2%, flashinfer 100.2% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-float16] | 0.0569 | 113.61 | 0.74 | 14% M | fa3 82.9%, flashinfer 72.5% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0568 | 113.77 | 0.74 | 14% M | fa3 82.8%, flashinfer 72.6% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-float16] | 0.3513 | 293.71 | 0.48 | 42% C | fa3 77.4%, flashinfer 78.6% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.3497 | 295.06 | 0.48 | 40% C | fa3 77.5%, flashinfer 78.7% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-float16] | 0.0933 | 138.67 | 0.81 | 18% C | fa3 89.7%, flashinfer 73.9% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-bfloat16] | 0.0927 | 139.48 | 0.81 | 17% M | fa3 89.6%, flashinfer 74.6% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-float16] | 0.6693 | 308.34 | 0.45 | 45% C | fa3 78.9%, flashinfer 77.8% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.6675 | 309.14 | 0.45 | 43% C | fa3 78.8%, flashinfer 77.5% | - |
| 🔵 | GtFwdOp | test_comparison_bench[gt-1024x4096-float16-gt] | 0.0076 | 0.55 | 2.75 | - | torch 102.5%, torch-compile 102.1% | - |
| 🔵 | GtFwdOp | test_gt_manifest_bench[hidden-state-prefill-float16] | 0.0130 | 0.65 | 3.23 | 79% M | torch 101.6%, torch-compile 101.6% | - |
| 🔵 | GtFwdOp | test_gt_manifest_bench[hidden-state-prefill-bfloat16] | 0.0131 | 0.64 | 3.20 | 79% M | torch 100.7%, torch-compile 100.5% | - |
| 🔵 | GtFwdOp | test_gt_manifest_bench[hidden-state-prefill-float32] | 0.0223 | 0.38 | 3.38 | 83% M | torch 100.2%, torch-compile 112.2% | - |
| 🔴 | GtFwdOp | test_gt_manifest_bench[cnn-feat-broadcast-float16] | 0.0172 | 0.74 | 2.23 | 55% M | torch 280.1%, torch-compile 69.2% | - |
| 🔴 | GtFwdOp | test_gt_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0173 | 0.74 | 2.23 | 55% M | torch 284.0%, torch-compile 69.5% | - |
| 🟡 | GtFwdOp | test_gt_manifest_bench[cnn-feat-broadcast-float32] | 0.0214 | 0.60 | 3.00 | 74% M | torch 224.1%, torch-compile 85.7% | - |
| 🟡 | HardsigmoidFwdOp | test_hardsigmoid_manifest_bench[mbv3-se-gate-float16] | 0.0016 | 0.01 | 0.02 | <sub>lat-bound</sub> | torch 105.9%, torch-compile 82.3% | - |
| 🟡 | HardsigmoidFwdOp | test_hardsigmoid_manifest_bench[mbv3-se-gate-bfloat16] | 0.0016 | 0.01 | 0.02 | <sub>lat-bound</sub> | torch 105.9%, torch-compile 82.4% | - |
| 🟡 | HardsigmoidFwdOp | test_hardsigmoid_manifest_bench[mbv3-se-gate-deep-float16] | 0.0017 | 0.06 | 0.07 | <sub>lat-bound</sub> | torch 92.3%, torch-compile 92.2% | - |
| 🟡 | HardsigmoidFwdOp | test_hardsigmoid_manifest_bench[mbv3-se-gate-deep-bfloat16] | 0.0017 | 0.05 | 0.07 | <sub>lat-bound</sub> | torch 89.6%, torch-compile 88.7% | - |
| 🟡 | HardswishFwdOp | test_hardswish_manifest_bench[mbv3-stage2-float16] | 0.0129 | 2.99 | 2.99 | 73% M | torch 89.8%, torch-compile 89.3% | - |
| 🟡 | HardswishFwdOp | test_hardswish_manifest_bench[mbv3-stage2-bfloat16] | 0.0132 | 2.92 | 2.92 | 72% M | torch 88.1%, torch-compile 87.6% | - |
| 🟡 | HardswishFwdOp | test_hardswish_manifest_bench[mbv3-stage3-float16] | 0.0089 | 2.72 | 2.72 | 67% M | torch 91.7%, torch-compile 91.0% | - |
| 🟡 | HardswishFwdOp | test_hardswish_manifest_bench[mbv3-stage3-bfloat16] | 0.0090 | 2.67 | 2.67 | 66% M | torch 90.4%, torch-compile 89.4% | - |
| 🔵 | HardtanhFwdOp | test_hardtanh_manifest_bench[bounded-hidden-float16] | 0.0104 | 0.81 | 3.24 | 80% M | torch 108.6%, torch-compile 100.6% | - |
| 🔵 | HardtanhFwdOp | test_hardtanh_manifest_bench[bounded-hidden-bfloat16] | 0.0104 | 0.81 | 3.24 | 80% M | torch 103.1%, torch-compile 100.9% | - |
| 🔵 | HardtanhFwdOp | test_hardtanh_manifest_bench[bounded-conv-feat-float16] | 0.0146 | 0.88 | 3.52 | 86% M | torch 110.8%, torch-compile 100.3% | - |
| 🔵 | HardtanhFwdOp | test_hardtanh_manifest_bench[bounded-conv-feat-bfloat16] | 0.0146 | 0.88 | 3.52 | 87% M | torch 104.2%, torch-compile 101.3% | - |
| 🔵 | InfNormFwdOp | test_inf_norm_bench[hidden-state-inf-float16] | 0.0074 | 2.28 | 2.28 | 56% M | flaggems 104.4%, torch 676.2%, torch-compile 144.8% | - |
| 🔵 | InfNormFwdOp | test_inf_norm_bench[hidden-state-inf-bfloat16] | 0.0074 | 2.28 | 2.28 | 56% M | flaggems 106.9%, torch 680.4%, torch-compile 150.0% | - |
| 🔵 | InfNormFwdOp | test_inf_norm_bench[long-seq-inf-bfloat16] | 0.0040 | 1.04 | 1.04 | <sub>lat-bound</sub> | flaggems 340.5%, torch 428.6%, torch-compile 122.2% | - |
| 🔵 | InfNormFwdOp | test_inf_norm_bench[3d-multidim-reduce-float16] | 0.0045 | 0.94 | 0.94 | <sub>lat-bound</sub> | flaggems 285.3%, torch 433.0%, torch-compile 110.4% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[image-affine-float16] | 0.0035 | 1.52 | 1.21 | <sub>lat-bound</sub> | flaggems 107.4%, torch 599.1%, torch-compile 88.9% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[image-affine-bfloat16] | 0.0034 | 1.53 | 1.23 | <sub>lat-bound</sub> | flaggems 108.4%, torch 604.7%, torch-compile 87.8% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[wider-channel-affine-float16] | 0.0035 | 1.16 | 0.93 | <sub>lat-bound</sub> | flaggems 102.8%, torch 595.4%, torch-compile 82.4% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[tail-spatial-affine-float16] | 0.0027 | 0.43 | 0.34 | <sub>lat-bound</sub> | flaggems 104.8%, torch 413.2%, torch-compile 89.3% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[image-float16] | 0.0034 | 0.94 | 1.25 | <sub>lat-bound</sub> | flaggems 102.9%, torch 505.7%, torch-compile 87.6% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[image-bfloat16] | 0.0034 | 0.93 | 1.24 | <sub>lat-bound</sub> | flaggems 102.8%, torch 502.8%, torch-compile 85.9% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[wider-channel-float16] | 0.0033 | 0.72 | 0.96 | <sub>lat-bound</sub> | flaggems 99.0%, torch 485.6%, torch-compile 82.7% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[tail-spatial-float16] | 0.0025 | 0.27 | 0.36 | <sub>lat-bound</sub> | flaggems 103.8%, torch 326.6%, torch-compile 91.1% | - |
| 🔵 | IsfiniteFwdOp | test_isfinite_bench[elementwise-16M-float16] | 0.0147 | 1.14 | 3.43 | 84% M | torch 430.8%, torch-compile 102.4% | - |
| 🔵 | IsfiniteFwdOp | test_isfinite_bench[elementwise-16M-bfloat16] | 0.0147 | 1.14 | 3.43 | 84% M | torch 432.1%, torch-compile 102.4% | - |
| 🟡 | IsfiniteFwdOp | test_isfinite_bench[elementwise-16M-float32] | 0.0234 | 0.72 | 3.59 | 88% M | torch 411.1%, torch-compile 99.9% | - |
| 🔵 | IsfiniteFwdOp | test_isfinite_bench[elementwise-256M-float16] | 0.1862 | 1.44 | 4.32 | ⚠️ 106% M | torch 489.9%, torch-compile 105.6% | - |
| 🔵 | IsfiniteFwdOp | test_isfinite_bench[elementwise-256M-bfloat16] | 0.1862 | 1.44 | 4.33 | ⚠️ 106% M | torch 491.7%, torch-compile 105.8% | - |
| 🔵 | IsinfFwdOp | test_isinf_bench[elementwise-16M-float16] | 0.0148 | 1.14 | 3.41 | 84% M | torch 212.2%, torch-compile 102.6% | - |
| 🔵 | IsinfFwdOp | test_isinf_bench[elementwise-16M-bfloat16] | 0.0148 | 1.13 | 3.40 | 84% M | torch 212.8%, torch-compile 102.8% | - |
| 🟡 | IsinfFwdOp | test_isinf_bench[elementwise-16M-float32] | 0.0235 | 0.72 | 3.58 | 88% M | torch 242.6%, torch-compile 99.5% | - |
| 🔵 | IsinfFwdOp | test_isinf_bench[elementwise-256M-float16] | 0.1862 | 1.44 | 4.33 | ⚠️ 106% M | torch 241.8%, torch-compile 106.7% | - |
| 🔵 | IsinfFwdOp | test_isinf_bench[elementwise-256M-bfloat16] | 0.1858 | 1.44 | 4.33 | ⚠️ 106% M | torch 242.9%, torch-compile 107.7% | - |
| 🔵 | IsnanFwdOp | test_isnan_bench[elementwise-16M-float16] | 0.0147 | 1.14 | 3.42 | 84% M | torch 104.6%, torch-compile 102.4% | - |
| 🔵 | IsnanFwdOp | test_isnan_bench[elementwise-16M-bfloat16] | 0.0147 | 1.14 | 3.43 | 84% M | torch 105.5%, torch-compile 103.0% | - |
| 🟡 | IsnanFwdOp | test_isnan_bench[elementwise-16M-float32] | 0.0234 | 0.72 | 3.58 | 88% M | torch 100.1%, torch-compile 99.7% | - |
| 🔵 | IsnanFwdOp | test_isnan_bench[elementwise-256M-float16] | 0.1864 | 1.44 | 4.32 | ⚠️ 106% M | torch 108.1%, torch-compile 105.8% | - |
| 🔵 | IsnanFwdOp | test_isnan_bench[elementwise-256M-bfloat16] | 0.1862 | 1.44 | 4.32 | ⚠️ 106% M | torch 109.5%, torch-compile 106.6% | - |
| 🔵 | L1NormFwdOp | test_l1_norm_bench[hidden-state-l1-float16] | 0.0074 | 2.28 | 2.28 | 56% M | flaggems 203.9%, torch 672.6%, torch-compile 113.5% | - |
| 🔵 | L1NormFwdOp | test_l1_norm_bench[hidden-state-l1-bfloat16] | 0.0074 | 2.28 | 2.28 | 56% M | flaggems 209.1%, torch 677.0%, torch-compile 114.3% | - |
| 🔵 | L1NormFwdOp | test_l1_norm_bench[long-seq-l1-bfloat16] | 0.0039 | 1.07 | 1.07 | <sub>lat-bound</sub> | flaggems 945.9%, torch 432.8%, torch-compile 120.5% | - |
| 🔵 | L1NormFwdOp | test_l1_norm_bench[3d-multidim-reduce-float16] | 0.0045 | 0.92 | 0.92 | <sub>lat-bound</sub> | flaggems 540.9%, torch 423.9%, torch-compile 101.4% | - |
| 🔵 | L2NormFwdOp | test_l2_norm_bench[hidden-state-l2-float16] | 0.0074 | 2.26 | 2.26 | 56% M | flaggems 106.0%, torch 666.8%, torch-compile 116.8% | - |
| 🔵 | L2NormFwdOp | test_l2_norm_bench[hidden-state-l2-bfloat16] | 0.0074 | 2.26 | 2.26 | 56% M | flaggems 105.6%, torch 672.1%, torch-compile 118.1% | - |
| 🔵 | L2NormFwdOp | test_l2_norm_bench[long-seq-l2-bfloat16] | 0.0040 | 1.05 | 1.05 | <sub>lat-bound</sub> | flaggems 340.6%, torch 424.9%, torch-compile 112.5% | - |
| 🔵 | L2NormFwdOp | test_l2_norm_bench[3d-multidim-reduce-float16] | 0.0047 | 0.90 | 0.90 | <sub>lat-bound</sub> | flaggems 289.0%, torch 411.0%, torch-compile 104.1% | - |
| 🟡 | LayerNormFwdOp | test_layer_norm_bench[llama-8b-prefill-float16] | 0.0137 | 3.06 | 2.45 | 60% M | flaggems 95.6%, flashinfer 155.6%, torch 154.6%, torch-compile 177.6% | - |
| 🟡 | LayerNormFwdOp | test_layer_norm_bench[llama-8b-prefill-bfloat16] | 0.0149 | 2.81 | 2.25 | 55% M | flaggems 92.4%, flashinfer 142.9%, torch 143.1%, torch-compile 164.6% | - |
| 🔵 | LayerNormFwdOp | test_layer_norm_bench[llama-8b-decode-bfloat16] | 0.0028 | 0.01 | 0.01 | <sub>lat-bound</sub> | flaggems 102.3%, flashinfer 111.6%, torch 405.2%, torch-compile 113.9% | - |
| 🟡 | LayerNormFwdOp | test_layer_norm_bench[llama-70b-prefill-float16] | 0.0260 | 3.22 | 2.58 | 63% M | flaggems 98.8%, flashinfer 178.7%, torch 154.1%, torch-compile 118.1% | - |
| 🔵 | LayerNormFwdOp | test_layer_norm_bench[llama-70b-prefill-bfloat16] | 0.0265 | 3.16 | 2.53 | 62% M | flaggems 104.5%, flashinfer 175.9%, torch 152.2%, torch-compile 126.0% | - |
| 🔵 | LayerNormFwdOp | test_layer_norm_bench[llama-70b-decode-bfloat16] | 0.0035 | 0.01 | 0.02 | <sub>lat-bound</sub> | flaggems 121.3%, flashinfer 119.4%, torch 579.6%, torch-compile 107.4% | - |
| 🟡 | LayerNormFwdOp | test_layer_norm_bench[llama-405b-prefill-float16] | 0.0502 | 3.34 | 2.68 | 66% M | flaggems 96.5%, flashinfer 156.4%, torch 147.6%, torch-compile 93.2% | - |
| 🟡 | LayerNormFwdOp | test_layer_norm_bench[llama-405b-prefill-bfloat16] | 0.0509 | 3.30 | 2.64 | 65% M | flaggems 99.2%, flashinfer 154.3%, torch 146.8%, torch-compile 99.6% | - |
| 🔵 | LayerNormFwdOp | test_layer_norm_bench[llama-405b-decode-bfloat16] | 0.0043 | 0.02 | 0.03 | <sub>lat-bound</sub> | flaggems 142.0%, flashinfer 140.5%, torch 881.7%, torch-compile 127.9% | - |
| 🔵 | LeFwdOp | test_comparison_bench[le-1024x4096-float16-le] | 0.0076 | 0.55 | 2.75 | - | torch 101.7%, torch-compile 100.8% | - |
| 🟡 | LeFwdOp | test_le_manifest_bench[hidden-state-prefill-float16] | 0.0130 | 0.65 | 3.23 | 79% M | torch 99.9%, torch-compile 99.6% | - |
| 🔵 | LeFwdOp | test_le_manifest_bench[hidden-state-prefill-bfloat16] | 0.0131 | 0.64 | 3.20 | 79% M | torch 100.4%, torch-compile 100.2% | - |
| 🔵 | LeFwdOp | test_le_manifest_bench[hidden-state-prefill-float32] | 0.0225 | 0.37 | 3.36 | 82% M | torch 100.0%, torch-compile 110.7% | - |
| 🔴 | LeFwdOp | test_le_manifest_bench[cnn-feat-broadcast-float16] | 0.0173 | 0.74 | 2.23 | 55% M | torch 287.0%, torch-compile 68.6% | - |
| 🔴 | LeFwdOp | test_le_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0172 | 0.74 | 2.23 | 55% M | torch 292.8%, torch-compile 68.9% | - |
| 🟡 | LeFwdOp | test_le_manifest_bench[cnn-feat-broadcast-float32] | 0.0215 | 0.60 | 2.99 | 73% M | torch 229.6%, torch-compile 86.0% | - |
| 🔵 | LeakyReluFwdOp | test_leaky_relu_manifest_bench[gan-feat-float16] | 0.0184 | 1.82 | 3.65 | 90% M | torch 100.4%, torch-compile 100.2% | - |
| 🔵 | LeakyReluFwdOp | test_leaky_relu_manifest_bench[gan-feat-bfloat16] | 0.0184 | 1.82 | 3.65 | 90% M | torch 100.3%, torch-compile 100.0% | - |
| 🔵 | LeakyReluFwdOp | test_leaky_relu_manifest_bench[gan-feat-deep-float16] | 0.0103 | 1.62 | 3.25 | 80% M | torch 100.9%, torch-compile 100.3% | - |
| 🔵 | LeakyReluFwdOp | test_leaky_relu_manifest_bench[gan-feat-deep-bfloat16] | 0.0103 | 1.62 | 3.25 | 80% M | torch 100.6%, torch-compile 100.3% | - |
| 🔵 | LerpFwdOp | test_binary_arith_bench[lerp-1024x4096-float16-float16-LerpFwdOp-<lambda>-normal] | 0.0081 | 0.52 | 3.10 | - | torch 101.2%, torch-compile 100.8% | - |
| 🔵 | LerpFwdOp | test_binary_arith_bench[lerp-1024x10240-float16-float16-LerpFwdOp-<lambda>-normal] | 0.0176 | 0.59 | 3.57 | - | torch 100.7%, torch-compile 100.2% | - |
| 🔵 | LerpFwdOp | test_lerp_manifest_bench[hidden-state-prefill-float16] | 0.0148 | 1.71 | 3.41 | 84% M | torch 100.6%, torch-compile 100.1% | - |
| 🔵 | LerpFwdOp | test_lerp_manifest_bench[hidden-state-prefill-bfloat16] | 0.0146 | 1.72 | 3.45 | 85% M | torch 100.4%, torch-compile 100.0% | - |
| 🟡 | LerpFwdOp | test_lerp_manifest_bench[hidden-state-prefill-float32] | 0.0263 | 0.96 | 3.82 | ✅ 94% M | torch 99.6%, torch-compile 99.5% | - |
| 🟡 | LerpFwdOp | test_lerp_manifest_bench[cnn-feat-broadcast-float16] | 0.0145 | 2.65 | 3.54 | 87% M | torch 329.3%, torch-compile 99.1% | - |
| 🟡 | LerpFwdOp | test_lerp_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0145 | 2.65 | 3.54 | 87% M | torch 331.7%, torch-compile 98.7% | - |
| 🟡 | LerpFwdOp | test_lerp_manifest_bench[cnn-feat-broadcast-float32] | 0.0267 | 1.44 | 3.85 | ✅ 95% M | torch 190.5%, torch-compile 99.5% | - |
| 🟡 | LerpTensorFwdOp | test_lerp_tensor_manifest_bench[elementwise-16M-float16] | 0.0350 | 1.44 | 3.84 | ✅ 94% M | torch 99.6%, torch-compile 99.4% | - |
| 🟡 | LerpTensorFwdOp | test_lerp_tensor_manifest_bench[elementwise-16M-bfloat16] | 0.0350 | 1.44 | 3.83 | ✅ 94% M | torch 99.5%, torch-compile 99.1% | - |
| 🟡 | LerpTensorFwdOp | test_lerp_tensor_manifest_bench[elementwise-16M-float32] | 0.0655 | 0.77 | 4.10 | ✅ 101% M | torch 99.7%, torch-compile 99.5% | - |
| 🔵 | LerpTensorFwdOp | test_lerp_tensor_manifest_bench[elementwise-256M-float16] | 0.4856 | 1.66 | 4.42 | ⚠️ 109% M | torch 100.1%, torch-compile 100.1% | - |
| 🔵 | LerpTensorFwdOp | test_lerp_tensor_manifest_bench[elementwise-256M-bfloat16] | 0.4860 | 1.66 | 4.42 | ⚠️ 109% M | torch 100.0%, torch-compile 100.0% | - |
| 🔵 | Log1pFwdOp | test_log1p_bench[elementwise-16M-float16] | 0.0181 | 1.85 | 3.70 | ✅ 91% M | torch 144.8%, torch-compile 140.7% | - |
| 🔵 | Log1pFwdOp | test_log1p_bench[elementwise-16M-bfloat16] | 0.0181 | 1.85 | 3.70 | ✅ 91% M | torch 147.8%, torch-compile 144.3% | - |
| 🟡 | Log1pFwdOp | test_log1p_bench[elementwise-16M-float32] | 0.0351 | 0.96 | 3.83 | ✅ 94% M | torch 97.0%, torch-compile 96.7% | - |
| 🔵 | Log1pFwdOp | test_log1p_bench[elementwise-256M-float16] | 0.2541 | 2.11 | 4.22 | ✅ 104% M | torch 149.5%, torch-compile 145.4% | - |
| 🟢 | Log1pFwdOp | test_log1p_bench[elementwise-256M-bfloat16] | 0.2549 | 2.11 | 4.21 | ✅ 104% M | torch 152.2%, torch-compile 150.1% | - |
| 🟢 | LogFwdOp | test_log_bench[elementwise-16M-float16] | 0.0181 | 0.93 | 3.71 | ✅ 91% M | torch 150.2%, torch-compile 151.2% | - |
| 🟢 | LogFwdOp | test_log_bench[elementwise-16M-bfloat16] | 0.0181 | 0.93 | 3.71 | ✅ 91% M | torch 155.0%, torch-compile 153.7% | - |
| 🟡 | LogFwdOp | test_log_bench[elementwise-16M-float32] | 0.0356 | 0.47 | 3.77 | ✅ 93% M | torch 96.4%, torch-compile 96.1% | - |
| 🟢 | LogFwdOp | test_log_bench[elementwise-256M-float16] | 0.2538 | 1.06 | 4.23 | ✅ 104% M | torch 156.4%, torch-compile 158.0% | - |
| 🟢 | LogFwdOp | test_log_bench[elementwise-256M-bfloat16] | 0.2544 | 1.06 | 4.22 | ✅ 104% M | torch 162.2%, torch-compile 161.2% | - |
| 🟢 | LogSoftmaxFwdOp | test_log_softmax_bench[attn-weights-4k-float16] | 0.0090 | 2.33 | 1.87 | 46% M | flaggems 222.1%, torch 191.1%, torch-compile 165.8% | - |
| 🟢 | LogSoftmaxFwdOp | test_log_softmax_bench[attn-weights-4k-bfloat16] | 0.0088 | 2.37 | 1.90 | 47% M | flaggems 231.5%, torch 193.9%, torch-compile 175.0% | - |
| 🔵 | LogSoftmaxFwdOp | test_log_softmax_bench[attn-weights-4k-float32] | 0.0115 | 1.83 | 2.93 | 72% M | flaggems 179.3%, torch 161.5%, torch-compile 138.3% | - |
| 🔵 | LogSoftmaxFwdOp | test_log_softmax_bench[attn-weights-32k-bfloat16] | 0.0568 | 2.95 | 2.36 | 58% M | flaggems 440.7%, torch 108.0%, torch-compile 125.3% | - |
| 🟡 | LogSoftmaxFwdOp | test_log_softmax_bench[lm-head-logits-float16] | 0.0105 | 0.20 | 0.16 | <sub>lat-bound</sub> | flaggems 4006.9%, torch 211.0%, torch-compile 92.4% | - |
| 🟡 | LogSoftmaxFwdOp | test_log_softmax_bench[lm-head-logits-bfloat16] | 0.0105 | 0.20 | 0.16 | <sub>lat-bound</sub> | flaggems 4011.1%, torch 217.4%, torch-compile 86.3% | - |
| 🟡 | LogSoftmaxFwdOp | test_log_softmax_bench[lm-head-logits-float32] | 0.0108 | 0.19 | 0.30 | <sub>lat-bound</sub> | flaggems 3733.7%, torch 325.1%, torch-compile 91.4% | - |
| 🔵 | LogSumExpFwdOp | test_logsumexp_bench[attn-weights-4k-float16] | 0.0074 | 2.26 | 1.13 | <sub>lat-bound</sub> | torch 656.4%, torch-compile 135.8% | - |
| 🔵 | LogSumExpFwdOp | test_logsumexp_bench[attn-weights-4k-bfloat16] | 0.0075 | 2.25 | 1.13 | <sub>lat-bound</sub> | torch 663.5%, torch-compile 134.8% | - |
| 🟢 | LogSumExpFwdOp | test_logsumexp_bench[attn-weights-32k-bfloat16] | 0.0270 | 4.96 | 2.48 | 61% M | torch 733.0%, torch-compile 153.8% | - |
| 🔵 | LogSumExpFwdOp | test_logsumexp_bench[lm-head-logits-float16] | 0.0082 | 0.20 | 0.10 | <sub>lat-bound</sub> | torch 564.3%, torch-compile 132.4% | - |
| 🔵 | LogSumExpFwdOp | test_logsumexp_bench[lm-head-logits-bfloat16] | 0.0082 | 0.20 | 0.10 | <sub>lat-bound</sub> | torch 570.7%, torch-compile 128.1% | - |
| 🔴 | LogSumExpFwdOp | test_logsumexp_bench[3d-multidim-reduce-float16] | 0.0140 | 0.60 | 0.30 | <sub>lat-bound</sub> | torch 295.9%, torch-compile 72.5% | - |
| 🔵 | LogicalAndFwdOp | test_logical_bench[logical_and-1024x4096-float16-LogicalAndFwdOp-logical_and] | 0.0075 | 0.56 | 2.80 | - | torch 103.4%, torch-compile 102.6% | - |
| 🔵 | LogicalAndFwdOp | test_logical_bench[logical_and-1024x10240-float16-LogicalAndFwdOp-logical_and] | 0.0157 | 0.67 | 3.33 | - | torch 102.0%, torch-compile 101.6% | - |
| 🔵 | LogicalAndFwdOp | test_logical_and_manifest_bench[hidden-state-prefill-bool] | 0.0082 | 3.06 | 3.06 | 75% M | torch 123.0%, torch-compile 107.4% | - |
| 🔵 | LogicalAndFwdOp | test_logical_and_manifest_bench[hidden-state-prefill-float16] | 0.0132 | 1.91 | 3.19 | 78% M | torch 101.6%, torch-compile 101.3% | - |
| 🔵 | LogicalAndFwdOp | test_logical_and_manifest_bench[hidden-state-prefill-bfloat16] | 0.0130 | 1.94 | 3.24 | 80% M | torch 100.5%, torch-compile 100.6% | - |
| 🔵 | LogicalAndFwdOp | test_logical_and_manifest_bench[hidden-state-prefill-float32] | 0.0225 | 1.12 | 3.36 | 83% M | torch 100.0%, torch-compile 111.5% | - |
| 🔵 | LogicalAndFwdOp | test_logical_and_manifest_bench[cnn-feat-broadcast-bool] | 0.0082 | 4.70 | 3.14 | 77% M | torch 551.6%, torch-compile 121.9% | - |
| 🔴 | LogicalAndFwdOp | test_logical_and_manifest_bench[cnn-feat-broadcast-float16] | 0.0172 | 2.24 | 2.24 | 55% M | torch 272.3%, torch-compile 70.6% | - |
| 🔴 | LogicalAndFwdOp | test_logical_and_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0172 | 2.24 | 2.24 | 55% M | torch 278.4%, torch-compile 69.7% | - |
| 🟡 | LogicalAndFwdOp | test_logical_and_manifest_bench[cnn-feat-broadcast-float32] | 0.0213 | 1.81 | 3.01 | 74% M | torch 218.2%, torch-compile 85.7% | - |
| 🔵 | LogicalNotFwdOp | test_logical_not_bench[elementwise-16M-bool] | 0.0101 | 1.66 | 3.32 | 82% M | torch 128.5%, torch-compile 119.6% | - |
| 🔵 | LogicalNotFwdOp | test_logical_not_bench[elementwise-16M-float16] | 0.0147 | 1.14 | 3.42 | 84% M | torch 103.5%, torch-compile 102.1% | - |
| 🟡 | LogicalNotFwdOp | test_logical_not_bench[elementwise-16M-float32] | 0.0235 | 0.71 | 3.57 | 88% M | torch 99.6%, torch-compile 99.5% | - |
| 🔵 | LogicalNotFwdOp | test_logical_not_bench[elementwise-256M-bool] | 0.1263 | 2.12 | 4.25 | ✅ 104% M | torch 143.7%, torch-compile 130.5% | - |
| 🔵 | LogicalOrFwdOp | test_logical_bench[logical_or-1024x4096-float16-LogicalOrFwdOp-logical_or] | 0.0075 | 0.56 | 2.80 | - | torch 102.1%, torch-compile 101.7% | - |
| 🔵 | LogicalOrFwdOp | test_logical_bench[logical_or-1024x10240-float16-LogicalOrFwdOp-logical_or] | 0.0158 | 0.66 | 3.31 | - | torch 101.6%, torch-compile 101.4% | - |
| 🔵 | LogicalOrFwdOp | test_logical_or_manifest_bench[hidden-state-prefill-bool] | 0.0082 | 3.07 | 3.07 | 75% M | torch 110.5%, torch-compile 108.6% | - |
| 🔵 | LogicalOrFwdOp | test_logical_or_manifest_bench[hidden-state-prefill-float16] | 0.0132 | 1.90 | 3.17 | 78% M | torch 100.7%, torch-compile 100.5% | - |
| 🔵 | LogicalOrFwdOp | test_logical_or_manifest_bench[hidden-state-prefill-bfloat16] | 0.0129 | 1.95 | 3.26 | 80% M | torch 101.1%, torch-compile 100.6% | - |
| 🟡 | LogicalOrFwdOp | test_logical_or_manifest_bench[hidden-state-prefill-float32] | 0.0225 | 1.12 | 3.36 | 83% M | torch 99.7%, torch-compile 110.5% | - |
| 🔵 | LogicalOrFwdOp | test_logical_or_manifest_bench[cnn-feat-broadcast-bool] | 0.0083 | 4.63 | 3.09 | 76% M | torch 531.9%, torch-compile 123.1% | - |
| 🔴 | LogicalOrFwdOp | test_logical_or_manifest_bench[cnn-feat-broadcast-float16] | 0.0174 | 2.21 | 2.21 | 54% M | torch 273.2%, torch-compile 69.1% | - |
| 🔴 | LogicalOrFwdOp | test_logical_or_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0174 | 2.21 | 2.21 | 54% M | torch 279.6%, torch-compile 69.5% | - |
| 🟡 | LogicalOrFwdOp | test_logical_or_manifest_bench[cnn-feat-broadcast-float32] | 0.0214 | 1.80 | 3.00 | 74% M | torch 217.2%, torch-compile 86.6% | - |
| 🔵 | LtFwdOp | test_comparison_bench[lt-1024x4096-float16-lt] | 0.0076 | 0.56 | 2.78 | - | torch 102.5%, torch-compile 102.1% | - |
| 🔵 | LtFwdOp | test_lt_manifest_bench[hidden-state-prefill-float16] | 0.0130 | 0.65 | 3.23 | 79% M | torch 101.0%, torch-compile 101.0% | - |
| 🔵 | LtFwdOp | test_lt_manifest_bench[hidden-state-prefill-bfloat16] | 0.0132 | 0.63 | 3.17 | 78% M | torch 100.2%, torch-compile 100.2% | - |
| 🔵 | LtFwdOp | test_lt_manifest_bench[hidden-state-prefill-float32] | 0.0226 | 0.37 | 3.35 | 82% M | torch 100.0%, torch-compile 109.5% | - |
| 🔴 | LtFwdOp | test_lt_manifest_bench[cnn-feat-broadcast-float16] | 0.0172 | 0.75 | 2.24 | 55% M | torch 288.7%, torch-compile 68.9% | - |
| 🔴 | LtFwdOp | test_lt_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0172 | 0.74 | 2.23 | 55% M | torch 292.2%, torch-compile 70.7% | - |
| 🟡 | LtFwdOp | test_lt_manifest_bench[cnn-feat-broadcast-float32] | 0.0216 | 0.60 | 2.98 | 73% M | torch 227.9%, torch-compile 85.5% | - |
| 🔵 | MHCPostFwdOp | test_mhc_post_bench[post-small-bfloat16] | 0.0013 | 0.01 | 0.02 | <sub>lat-bound</sub> | torch-ref 802.5%, torch-compile 100.0% | - |
| 🟡 | MHCPostFwdOp | test_mhc_post_bench[post-medium-bfloat16] | 0.0014 | 0.02 | 0.05 | <sub>lat-bound</sub> | torch-ref 765.6%, torch-compile 97.8% | - |
| 🔵 | MHCPostFwdOp | test_mhc_post_bench[post-large-bfloat16] | 0.0016 | 0.05 | 0.12 | <sub>lat-bound</sub> | torch-ref 714.0%, torch-compile 108.0% | - |
| 🔴 | MHCPreFwdOp | test_mhc_pre_bench[pre-small-bfloat16] | 0.0394 | 0.01 | 0.01 | 0% M | torch-ref 150.1%, torch-compile 49.6% | - |
| 🔴 | MHCPreFwdOp | test_mhc_pre_bench[pre-medium-bfloat16] | 0.0544 | 0.02 | 0.01 | 0% M | torch-ref 143.3%, torch-compile 57.7% | - |
| 🔴 | MHCPreFwdOp | test_mhc_pre_bench[pre-large-bfloat16] | 0.0715 | 0.03 | 0.02 | 0% M | torch-ref 163.6%, torch-compile 79.2% | - |
| 🟡 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-2p7b-b1-s2k-bfloat16] | 0.1092 | 74.58 | 0.99 | 24% M | mamba 99.9%, torch-ref 1972.1%, torch-compile 631.5% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-1p3b-b1-s8k-float16] | 0.2884 | 90.54 | 1.21 | 30% M | mamba 108.4%, torch-ref 2395.6%, torch-compile 699.5% | - |
| 🟡 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-2p7b-b1-s2k-dt-bias-bfloat16] | 0.1092 | 74.60 | 0.99 | 24% M | mamba 99.9%, torch-ref 1977.0%, torch-compile 630.5% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-1p3b-b1-s8k-dt-bias-float16] | 0.2881 | 90.64 | 1.21 | 30% M | mamba 108.4%, torch-ref 2397.4%, torch-compile 698.6% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-2p7b-b1-s2k-init-states-bfloat16] | 0.1098 | 74.19 | 1.01 | 25% M | mamba 100.4%, torch-ref 1963.2%, torch-compile 618.2% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-1p3b-b1-s8k-init-states-float16] | 0.2886 | 90.48 | 1.22 | 30% M | mamba 108.7%, torch-ref 2391.9%, torch-compile 698.7% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-2p7b-b1-s2k-dt-bias-init-states-bfloat16] | 0.1097 | 74.21 | 1.01 | 25% M | mamba 100.5%, torch-ref 1964.6%, torch-compile 619.7% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-1p3b-b1-s8k-dt-bias-init-states-float16] | 0.2888 | 90.40 | 1.22 | 30% M | mamba 108.1%, torch-ref 2391.7%, torch-compile 697.1% | - |
| 🟡 | MaskedFillFwdOp | test_masked_fill_tensor_manifest_bench[elementwise-16M-float16] | 0.0227 | 0.74 | 3.69 | ✅ 91% M | torch 177.6%, torch-compile 99.5% | - |
| 🟡 | MaskedFillFwdOp | test_masked_fill_tensor_manifest_bench[elementwise-16M-bfloat16] | 0.0226 | 0.74 | 3.71 | ✅ 91% M | torch 177.9%, torch-compile 99.7% | - |
| 🟡 | MaskedFillFwdOp | test_masked_fill_tensor_manifest_bench[elementwise-16M-float32] | 0.0380 | 0.44 | 3.97 | ✅ 98% M | torch 192.3%, torch-compile 98.7% | - |
| 🔵 | MaskedFillFwdOp | test_masked_fill_tensor_manifest_bench[elementwise-256M-float16] | 0.3092 | 0.87 | 4.34 | ⚠️ 107% M | torch 184.3%, torch-compile 100.2% | - |
| 🟡 | MaskedFillFwdOp | test_masked_fill_tensor_manifest_bench[elementwise-256M-bfloat16] | 0.3103 | 0.87 | 4.33 | ⚠️ 106% M | torch 184.0%, torch-compile 99.9% | - |
| 🟡 | MaskedFillScalarFwdOp | test_masked_fill_scalar_manifest_bench[elementwise-16M-float16] | 0.0227 | 0.74 | 3.69 | ✅ 91% M | torch 165.2%, torch-compile 99.3% | - |
| 🟡 | MaskedFillScalarFwdOp | test_masked_fill_scalar_manifest_bench[elementwise-16M-bfloat16] | 0.0225 | 0.75 | 3.73 | ✅ 92% M | torch 167.5%, torch-compile 99.9% | - |
| 🟡 | MaskedFillScalarFwdOp | test_masked_fill_scalar_manifest_bench[elementwise-16M-float32] | 0.0379 | 0.44 | 3.98 | ✅ 98% M | torch 187.2%, torch-compile 98.4% | - |
| 🟡 | MaskedFillScalarFwdOp | test_masked_fill_scalar_manifest_bench[elementwise-256M-float16] | 0.3102 | 0.87 | 4.33 | ⚠️ 106% M | torch 182.8%, torch-compile 99.8% | - |
| 🟡 | MaskedFillScalarFwdOp | test_masked_fill_scalar_manifest_bench[elementwise-256M-bfloat16] | 0.3104 | 0.86 | 4.32 | ⚠️ 106% M | torch 182.9%, torch-compile 99.9% | - |
| 🔵 | MaxPool1dFwdOp | test_max_pool1d_bench[sincnet-speaker-local-float16] | 0.0114 | 0.92 | 2.45 | 60% M | torch-ref 442.3%, torch-compile 100.0% | - |
| 🔴 | MaxPool1dFwdOp | test_max_pool1d_bench[textcnn-global-float16] | 0.0135 | 0.16 | 0.31 | <sub>lat-bound</sub> | torch-ref 196.2%, torch-compile 30.4% | - |
| 🟡 | MaxPool1dFwdOp | test_max_pool1d_bench[ecg-cnn-dilated-bfloat16] | 0.0095 | 1.10 | 1.32 | 33% M | torch-ref 372.4%, torch-compile 82.5% | - |
| 🔴 | MaxPool1dIndicesFwdOp | test_max_pool1d_indices_bench[sincnet-speaker-local-float16] | 0.0218 | 0.48 | 2.57 | 63% M | torch-ref 232.2%, torch-compile 73.8% | - |
| 🔴 | MaxPool1dIndicesFwdOp | test_max_pool1d_indices_bench[textcnn-global-float16] | 0.0193 | 0.11 | 0.23 | <sub>lat-bound</sub> | torch-ref 137.0%, torch-compile 29.5% | - |
| 🔴 | MaxPool1dIndicesFwdOp | test_max_pool1d_indices_bench[ecg-cnn-dilated-bfloat16] | 0.0224 | 0.47 | 1.31 | 32% M | torch-ref 158.2%, torch-compile 59.9% | - |
| 🔴 | MaxPool2dFwdOp | test_max_pool2d_bench[resnet-stem-float16] | 0.0471 | 1.23 | 1.36 | 33% M | flaggems 166.3%, torch-ref 294.8%, torch-compile 72.1% | - |
| 🔴 | MaxPool2dFwdOp | test_max_pool2d_bench[resnet-stem-bfloat16] | 0.0470 | 1.23 | 1.37 | 34% M | flaggems 166.8%, torch-ref 296.8%, torch-compile 72.5% | - |
| 🟡 | MaxPool2dFwdOp | test_max_pool2d_bench[resnet-stem-float32] | 0.0527 | 1.10 | 2.44 | 60% M | flaggems 153.8%, torch-ref 255.4%, torch-compile 94.2% | - |
| 🔵 | MaxPool2dFwdOp | test_max_pool2d_bench[vgg-block-float16] | 0.0072 | 0.89 | 2.23 | 55% M | flaggems 205.6%, torch-ref 385.3%, torch-compile 100.9% | - |
| 🔵 | MaxPool2dFwdOp | test_max_pool2d_bench[vgg-block-bfloat16] | 0.0072 | 0.89 | 2.23 | 55% M | flaggems 205.4%, torch-ref 387.2%, torch-compile 100.9% | - |
| 🟡 | MaxPool2dFwdOp | test_max_pool2d_bench[vgg-block-float32] | 0.0111 | 0.58 | 2.90 | 71% M | flaggems 151.4%, torch-ref 250.3%, torch-compile 93.3% | - |
| 🔵 | MaxPool2dFwdOp | test_max_pool2d_bench[alexnet-ceil-float16] | 0.0088 | 1.53 | 1.75 | 43% M | flaggems 256.6%, torch-ref 396.0%, torch-compile 125.2% | - |
| 🔵 | MaxPool2dFwdOp | test_max_pool2d_bench[alexnet-ceil-bfloat16] | 0.0087 | 1.54 | 1.76 | 43% M | flaggems 260.1%, torch-ref 398.1%, torch-compile 125.6% | - |
| 🔵 | MaxPool2dFwdOp | test_max_pool2d_bench[alexnet-ceil-float32] | 0.0126 | 1.06 | 2.43 | 60% M | flaggems 180.8%, torch-ref 270.1%, torch-compile 121.8% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[resnet-stem-float16] | 0.1122 | 0.52 | 1.03 | 25% M | flaggems 69.9%, torch-ref 124.1%, torch-compile 61.8% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[resnet-stem-bfloat16] | 0.1122 | 0.52 | 1.03 | 25% M | flaggems 69.7%, torch-ref 124.3%, torch-compile 62.4% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[resnet-stem-float32] | 0.1074 | 0.54 | 1.67 | 41% M | flaggems 75.6%, torch-ref 125.3%, torch-compile 66.5% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[vgg-block-float16] | 0.0196 | 0.33 | 1.47 | 36% M | flaggems 75.2%, torch-ref 141.2%, torch-compile 54.1% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[vgg-block-bfloat16] | 0.0195 | 0.33 | 1.49 | 36% M | flaggems 76.0%, torch-ref 143.1%, torch-compile 54.6% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[vgg-block-float32] | 0.0195 | 0.33 | 2.30 | 57% M | flaggems 85.7%, torch-ref 141.8%, torch-compile 64.6% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[alexnet-ceil-float16] | 0.0237 | 0.57 | 1.15 | 28% M | flaggems 94.9%, torch-ref 146.4%, torch-compile 74.5% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[alexnet-ceil-bfloat16] | 0.0237 | 0.57 | 1.15 | 28% M | flaggems 96.0%, torch-ref 146.8%, torch-compile 73.5% | - |
| 🟡 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[alexnet-ceil-float32] | 0.0236 | 0.57 | 1.81 | 44% M | flaggems 96.5%, torch-ref 144.6%, torch-compile 82.0% | - |
| 🔵 | MaxPool3dFwdOp | test_max_pool3d_bench[c3d-pool1-float16] | 0.0763 | 1.35 | 3.37 | 83% M | cudnn 394.7%, torch-ref 679.1%, torch-compile 101.1% | - |
| 🔵 | MaxPool3dFwdOp | test_max_pool3d_bench[c3d-pool2-float16] | 0.0236 | 1.09 | 2.45 | 60% M | cudnn 258.8%, torch-ref 399.1%, torch-compile 104.9% | - |
| 🟢 | MaxPool3dFwdOp | test_max_pool3d_bench[medicalnet-stem-bfloat16] | 0.1111 | 1.72 | 1.05 | 26% M | cudnn 237.4%, torch-ref 301.5%, torch-compile 833.7% | - |
| 🔴 | MaxPool3dIndicesFwdOp | test_max_pool3d_indices_bench[c3d-pool1-float16] | 0.3043 | 0.34 | 1.52 | 37% M | torch-ref 170.3%, torch-compile 42.4% | - |
| 🔴 | MaxPool3dIndicesFwdOp | test_max_pool3d_indices_bench[c3d-pool2-float16] | 0.0590 | 0.44 | 1.41 | 35% M | torch-ref 159.2%, torch-compile 55.1% | - |
| 🔵 | MaxPool3dIndicesFwdOp | test_max_pool3d_indices_bench[medicalnet-stem-bfloat16] | 0.3316 | 0.58 | 0.52 | 13% M | torch-ref 101.0%, torch-compile 614.1% | - |
| 🟡 | MaximumFwdOp | test_binary_arith_bench[maximum-1024x4096-float16-float16-MaximumFwdOp-maximum-normal] | 0.0086 | 0.49 | 2.92 | - | torch 100.7%, torch-compile 97.4% | - |
| 🟡 | MaximumFwdOp | test_binary_arith_bench[maximum-1024x10240-float16-float16-MaximumFwdOp-maximum-normal] | 0.0180 | 0.58 | 3.49 | - | torch 100.9%, torch-compile 98.9% | - |
| 🟡 | MaximumFwdOp | test_binary_arith_bench[maximum-1024x11008-float16-float16-MaximumFwdOp-maximum-normal] | 0.0189 | 0.60 | 3.58 | - | torch 100.5%, torch-compile 99.0% | - |
| 🟡 | MaximumFwdOp | test_maximum_manifest_bench[hidden-state-prefill-float16] | 0.0147 | 0.57 | 3.43 | 84% M | torch 100.7%, torch-compile 98.9% | - |
| 🟡 | MaximumFwdOp | test_maximum_manifest_bench[hidden-state-prefill-bfloat16] | 0.0150 | 0.56 | 3.36 | 83% M | torch 100.4%, torch-compile 98.4% | - |
| 🟡 | MaximumFwdOp | test_maximum_manifest_bench[hidden-state-prefill-float32] | 0.0263 | 0.32 | 3.83 | ✅ 94% M | torch 100.7%, torch-compile 99.8% | - |
| 🔴 | MaximumFwdOp | test_maximum_manifest_bench[cnn-feat-broadcast-float16] | 0.0342 | 0.38 | 1.50 | 37% M | torch 147.4%, torch-compile 41.9% | - |
| 🔴 | MaximumFwdOp | test_maximum_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0342 | 0.38 | 1.50 | 37% M | torch 149.7%, torch-compile 41.4% | - |
| 🟡 | MaximumFwdOp | test_maximum_manifest_bench[cnn-feat-broadcast-float32] | 0.0278 | 0.46 | 3.70 | ✅ 91% M | torch 191.0%, torch-compile 95.0% | - |
| 🔵 | MeanFwdOp | test_mean_bench[hidden-state-reduce-float16] | 0.0074 | 1.13 | 2.26 | 56% M | flaggems 119.8%, torch 666.4%, torch-compile 112.3% | - |
| 🔵 | MeanFwdOp | test_mean_bench[hidden-state-reduce-bfloat16] | 0.0074 | 1.13 | 2.26 | 56% M | flaggems 120.2%, torch 671.5%, torch-compile 113.8% | - |
| 🟡 | MeanFwdOp | test_mean_bench[long-seq-reduce-bfloat16] | 0.0041 | 0.52 | 1.03 | <sub>lat-bound</sub> | flaggems 92.9%, torch 415.8%, torch-compile 115.0% | - |
| 🟡 | MeanFwdOp | test_mean_bench[3d-multidim-reduce-float16] | 0.0057 | 0.37 | 0.74 | <sub>lat-bound</sub> | flaggems 236.5%, torch 336.0%, torch-compile 81.5% | - |
| 🔴 | MeanPoolingForwardOp | test_mean_pooling_bench[dense-mainstream] | 0.1350 | 0.50 | 1.01 | - | torch-ref 455.8%, torch-compile 314.4%, torch-view-mean 34.8% | - |
| 🔴 | MeanPoolingForwardOp | test_mean_pooling_bench[dense-batched] | 0.0702 | 0.48 | 0.97 | - | torch-ref 372.5%, torch-compile 208.8%, torch-view-mean 40.6% | - |
| 🟢 | MeanPoolingForwardOp | test_mean_pooling_bench[varlen-long] | 0.1385 | 0.48 | 0.98 | - | torch-ref 447.4%, torch-compile 444.2% | - |
| 🟢 | MeanPoolingForwardOp | test_mean_pooling_bench[varlen-tail] | 0.0218 | 0.41 | 0.78 | - | torch-ref 983.0%, torch-compile 963.4% | - |
| 🟡 | MinimumFwdOp | test_binary_arith_bench[minimum-1024x4096-float16-float16-MinimumFwdOp-minimum-normal] | 0.0086 | 0.49 | 2.92 | - | torch 101.5%, torch-compile 97.0% | - |
| 🟡 | MinimumFwdOp | test_binary_arith_bench[minimum-1024x10240-float16-float16-MinimumFwdOp-minimum-normal] | 0.0181 | 0.58 | 3.47 | - | torch 100.4%, torch-compile 98.4% | - |
| 🟡 | MinimumFwdOp | test_binary_arith_bench[minimum-1024x11008-float16-float16-MinimumFwdOp-minimum-normal] | 0.0190 | 0.59 | 3.56 | - | torch 100.3%, torch-compile 99.0% | - |
| 🟡 | MinimumFwdOp | test_minimum_manifest_bench[hidden-state-prefill-float16] | 0.0150 | 0.56 | 3.36 | 83% M | torch 100.4%, torch-compile 98.3% | - |
| 🟡 | MinimumFwdOp | test_minimum_manifest_bench[hidden-state-prefill-bfloat16] | 0.0150 | 0.56 | 3.36 | 83% M | torch 100.6%, torch-compile 98.7% | - |
| 🟡 | MinimumFwdOp | test_minimum_manifest_bench[hidden-state-prefill-float32] | 0.0265 | 0.32 | 3.80 | ✅ 93% M | torch 100.0%, torch-compile 99.3% | - |
| 🔴 | MinimumFwdOp | test_minimum_manifest_bench[cnn-feat-broadcast-float16] | 0.0342 | 0.38 | 1.50 | 37% M | torch 147.7%, torch-compile 42.0% | - |
| 🔴 | MinimumFwdOp | test_minimum_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0342 | 0.38 | 1.50 | 37% M | torch 149.4%, torch-compile 42.1% | - |
| 🟡 | MinimumFwdOp | test_minimum_manifest_bench[cnn-feat-broadcast-float32] | 0.0278 | 0.46 | 3.70 | ✅ 91% M | torch 190.3%, torch-compile 95.3% | - |
| 🟢 | MishFwdOp | test_mish_manifest_bench[yolo-p3-float16] | 0.0401 | 2.61 | 2.61 | 64% M | torch 158.2%, torch-compile 182.7% | - |
| 🟢 | MishFwdOp | test_mish_manifest_bench[yolo-p3-bfloat16] | 0.0404 | 2.59 | 2.59 | 64% M | torch 158.3%, torch-compile 182.9% | - |
| 🟢 | MishFwdOp | test_mish_manifest_bench[yolo-p4-float16] | 0.0215 | 2.44 | 2.44 | 60% M | torch 154.6%, torch-compile 178.1% | - |
| 🟢 | MishFwdOp | test_mish_manifest_bench[yolo-p4-bfloat16] | 0.0216 | 2.42 | 2.42 | 60% M | torch 155.3%, torch-compile 178.4% | - |
| 🟢 | MoeGateUpFwdOp | test_moe_gate_up_bench[deepseek-v3-decode-gate-up-bfloat16] | 3.4606 | 69.50 | 4.37 | ⚠️ 107% M | torch-ref 191.7%, torch-compile 227.2% | - |
| 🟢 | MoeGateUpFwdOp | test_moe_gate_up_bench[deepseek-v3-prefill-gate-up-bfloat16] | 4.3930 | 438.01 | 3.56 | 87% M | torch-ref 158.3%, torch-compile 616.1% | - |
| 🔵 | MoeGroupedGemmNopadFwdOp | test_moe_grouped_gemm_nopad_bench[deepseek-v3-decode-gate-up-bfloat16] | 3.7438 | 64.25 | 4.04 | ✅ 99% M | torch-ref 138.0%, torch-compile 156.3% | - |
| 🔵 | MoeGroupedGemmNopadFwdOp | test_moe_grouped_gemm_nopad_bench[deepseek-v3-prefill-gate-up-bfloat16] | 4.3017 | 447.30 | 3.67 | ✅ 90% M | torch-ref 125.6%, torch-compile 251.2% | - |
| 🔵 | MoeGroupedGemmNopadFwdOp | test_moe_grouped_gemm_nopad_bench[deepseek-v3-decode-down-bfloat16] | 1.9100 | 62.96 | 3.97 | ✅ 98% M | torch-ref 140.9%, torch-compile 292.5% | - |
| 🔵 | MoeGroupedGemmNopadFwdOp | test_moe_grouped_gemm_nopad_bench[deepseek-v3-prefill-down-bfloat16] | 2.1538 | 446.70 | 3.77 | ✅ 93% M | torch-ref 132.0%, torch-compile 1198.7% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[kimi-k2-decode-int32] | 0.0169 | 0.00 | 0.01 | <sub>lat-bound</sub> | triton 287.6% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[kimi-k2-small-int32] | 0.0194 | 0.00 | 0.01 | <sub>lat-bound</sub> | triton 247.9% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[kimi-k2-medium-int32] | 0.0217 | 0.00 | 0.01 | 0% M | triton 257.5% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[kimi-k2-prefill-int32] | 0.0410 | 0.00 | 0.01 | 0% M | triton 208.7% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[deepseek-v3-decode-int32] | 0.0148 | 0.00 | 0.00 | <sub>lat-bound</sub> | triton 228.1% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[deepseek-v3-small-int32] | 0.0153 | 0.00 | 0.00 | <sub>lat-bound</sub> | triton 220.1% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[deepseek-v3-medium-int32] | 0.0177 | 0.00 | 0.01 | <sub>lat-bound</sub> | triton 236.1% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[deepseek-v3-prefill-int32] | 0.0378 | 0.00 | 0.01 | 0% M | triton 196.5% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[qwen3-decode-int32] | 0.0108 | 0.00 | 0.00 | <sub>lat-bound</sub> | triton 156.8% | - |
| 🔵 | MoePermuteAlignFwdOp | test_permute_align_bench[qwen3-small-int32] | 0.0121 | 0.00 | 0.00 | <sub>lat-bound</sub> | triton 149.6% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[qwen3-medium-int32] | 0.0141 | 0.00 | 0.00 | <sub>lat-bound</sub> | triton 211.6% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[qwen3-prefill-int32] | 0.0318 | 0.00 | 0.01 | 0% M | triton 251.6% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[kimi-k2-decode-bfloat16] | 0.0106 | 0.00 | 0.01 | <sub>lat-bound</sub> | vllm 110.5% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[kimi-k2-small-bfloat16] | 0.0118 | 0.00 | 0.35 | <sub>lat-bound</sub> | vllm 117.0% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[kimi-k2-medium-bfloat16] | 0.0356 | 0.00 | 1.86 | 46% M | vllm 129.3% | - |
| 🟡 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[kimi-k2-prefill-bfloat16] | 0.2854 | 0.00 | 1.85 | 46% M | vllm 94.6% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-decode-bfloat16] | 0.0092 | 0.00 | 0.01 | <sub>lat-bound</sub> | vllm 125.6% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-small-bfloat16] | 0.0104 | 0.00 | 0.40 | <sub>lat-bound</sub> | vllm 132.1% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-medium-bfloat16] | 0.0337 | 0.00 | 1.96 | 48% M | vllm 136.7% | - |
| 🟡 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-prefill-bfloat16] | 0.2789 | 0.00 | 1.90 | 47% M | vllm 96.8% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-235b-decode-bfloat16] | 0.0080 | 0.00 | 0.02 | <sub>lat-bound</sub> | vllm 143.4% | - |
| 🟢 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-235b-small-bfloat16] | 0.0090 | 0.00 | 0.46 | <sub>lat-bound</sub> | vllm 153.4% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-235b-medium-bfloat16] | 0.0313 | 0.00 | 2.11 | 52% M | vllm 146.8% | - |
| 🟡 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-235b-prefill-bfloat16] | 0.2688 | 0.00 | 1.97 | 48% M | vllm 97.3% | - |
| 🟢 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-30b-decode-bfloat16] | 0.0063 | 0.00 | 0.01 | <sub>lat-bound</sub> | vllm 167.5% | - |
| 🟢 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-30b-small-bfloat16] | 0.0072 | 0.00 | 0.25 | <sub>lat-bound</sub> | vllm 173.3% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-30b-medium-bfloat16] | 0.0207 | 0.00 | 1.37 | 34% M | vllm 139.9% | - |
| 🟡 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-30b-prefill-bfloat16] | 0.1419 | 0.00 | 1.60 | 39% M | vllm 91.3% | - |
|  | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-ep2-decode-bfloat16] | 0.0087 | 0.00 | 0.02 | <sub>lat-bound</sub> | - | - |
|  | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-ep2-medium-bfloat16] | 0.0280 | 0.00 | 2.36 | 58% M | - | - |
|  | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-ep2-prefill-bfloat16] | 0.2101 | 0.00 | 2.52 | 62% M | - | - |
|  | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-235b-ep2-medium-bfloat16] | 0.0264 | 0.00 | 2.50 | 61% M | - | - |
| 🟢 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[large-hidden-decode-bfloat16] | 0.0070 | 0.02 | 0.02 | <sub>lat-bound</sub> | vllm 238.1% | - |
| 🟢 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[large-hidden-small-bfloat16] | 0.0079 | 0.47 | 0.52 | <sub>lat-bound</sub> | vllm 227.9% | - |
| 🔵 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[large-hidden-medium-bfloat16] | 0.0214 | 2.75 | 3.09 | 76% M | vllm 137.2% | - |
| 🔵 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[large-hidden-prefill-bfloat16] | 0.1329 | 3.53 | 3.98 | ✅ 98% M | vllm 104.7% | - |
| 🟢 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[small-hidden-decode-bfloat16] | 0.0057 | 0.01 | 0.01 | <sub>lat-bound</sub> | vllm 157.3% | - |
| 🟢 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[small-hidden-small-bfloat16] | 0.0065 | 0.24 | 0.27 | <sub>lat-bound</sub> | vllm 152.7% | - |
| 🔵 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[small-hidden-medium-bfloat16] | 0.0116 | 2.18 | 2.45 | 60% M | vllm 128.2% | - |
| 🔵 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[small-hidden-prefill-bfloat16] | 0.0615 | 3.27 | 3.69 | ✅ 91% M | vllm 109.6% | - |
| 🔵 | MulFwdOp | test_binary_arith_bench[mul-1024x4096-float16-float16-MulFwdOp-mul-normal] | 0.0084 | 0.50 | 2.99 | - | torch 101.9%, torch-compile 100.4% | - |
| 🟡 | MulFwdOp | test_binary_arith_bench[mul-1024x10240-float16-float16-MulFwdOp-mul-normal] | 0.0176 | 0.60 | 3.57 | - | torch 100.9%, torch-compile 99.9% | - |
| 🔵 | MulFwdOp | test_binary_arith_bench[mul-1024x11008-float16-float16-MulFwdOp-mul-normal] | 0.0185 | 0.61 | 3.65 | - | torch 100.3%, torch-compile 100.3% | - |
| 🔵 | MulFwdOp | test_mul_manifest_bench[hidden-state-prefill-float16] | 0.0148 | 0.56 | 3.39 | 83% M | torch 100.2%, torch-compile 100.2% | - |
| 🔵 | MulFwdOp | test_mul_manifest_bench[hidden-state-prefill-bfloat16] | 0.0147 | 0.57 | 3.43 | 84% M | torch 100.7%, torch-compile 100.4% | - |
| 🟡 | MulFwdOp | test_mul_manifest_bench[hidden-state-prefill-float32] | 0.0264 | 0.32 | 3.81 | ✅ 94% M | torch 99.7%, torch-compile 99.5% | - |
| 🟡 | MulFwdOp | test_mul_manifest_bench[cnn-feat-broadcast-float16] | 0.0144 | 0.89 | 3.58 | 88% M | torch 316.7%, torch-compile 99.1% | - |
| 🟡 | MulFwdOp | test_mul_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0146 | 0.88 | 3.52 | 87% M | torch 316.2%, torch-compile 99.1% | - |
| 🔵 | MulFwdOp | test_mul_manifest_bench[cnn-feat-broadcast-float32] | 0.0265 | 0.48 | 3.88 | ✅ 95% M | torch 185.9%, torch-compile 100.2% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-8b-short-float16] | 0.2436 | 88.17 | 0.48 | 13% C | fa3 58.9% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-8b-short-bfloat16] | 0.4553 | 47.16 | 0.26 | 7% C | fa3 31.4% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-8b-long-float16] | 0.9029 | 190.28 | 0.26 | 29% C | fa3 61.1% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-8b-long-bfloat16] | 1.3124 | 130.90 | 0.18 | 19% C | fa3 41.7% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-70b-short-float16] | 0.2438 | 88.07 | 0.48 | 13% C | fa3 58.8% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-70b-short-bfloat16] | 0.4566 | 47.03 | 0.26 | 7% C | fa3 31.3% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-70b-long-float16] | 0.8924 | 192.51 | 0.26 | 29% C | fa3 61.7% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-70b-long-bfloat16] | 1.1024 | 155.84 | 0.21 | 22% C | fa3 49.7% | - |
| 🟢 | MultiHeadAttentionDecodePagedWithKVCacheFwdOp | test_mha_decode_paged_bench[single-token-page128-float16] | 0.0061 | 0.68 | 0.68 | <sub>lat-bound</sub> | flashinfer 150.5% | - |
| 🟢 | MultiHeadAttentionDecodePagedWithKVCacheFwdOp | test_mha_decode_paged_bench[batch2-page256-float16] | 0.0058 | 0.72 | 0.36 | <sub>lat-bound</sub> | fa3 317.5%, flashinfer 167.8% | - |
| 🟢 | MultiHeadAttentionDecodePagedWithKVCacheFwdOp | test_mha_decode_paged_bench[longer-cache-float16] | 0.0053 | 0.39 | 0.39 | <sub>lat-bound</sub> | fa3 340.8%, flashinfer 180.9% | - |
| 🟢 | MultiHeadAttentionDecodePagedWithKVCacheFwdOp | test_mha_decode_paged_bench[shorter-cache-float16] | 0.0046 | 0.23 | 0.23 | <sub>lat-bound</sub> | fa3 390.3%, flashinfer 202.1% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-8b-4k-float16] | 0.5110 | 4.20 | 4.20 | ✅ 103% M | fa3 100.3%, flashinfer 103.6% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-8b-4k-bfloat16] | 0.5106 | 4.21 | 4.21 | ✅ 103% M | fa3 100.2%, flashinfer 103.8% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-8b-32k-float16] | 0.9808 | 4.38 | 4.38 | ⚠️ 107% M | fa3 100.9%, flashinfer 102.6% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-8b-32k-bfloat16] | 0.9808 | 4.38 | 4.38 | ⚠️ 108% M | fa3 100.7%, flashinfer 101.8% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-70b-4k-float16] | 0.5144 | 4.17 | 4.18 | ✅ 102% M | fa3 100.2%, flashinfer 103.2% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-70b-4k-bfloat16] | 0.5138 | 4.18 | 4.18 | ✅ 103% M | fa3 100.1%, flashinfer 103.2% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-70b-32k-float16] | 0.9804 | 4.38 | 4.38 | ⚠️ 108% M | fa3 100.8%, flashinfer 101.8% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-70b-32k-bfloat16] | 0.9797 | 4.38 | 4.38 | ⚠️ 108% M | fa3 100.6%, flashinfer 101.7% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-8b-short-float16] | 0.0425 | 201.98 | 1.58 | 39% M | fa3 81.9%, flashinfer 96.8% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-8b-short-bfloat16] | 0.0425 | 202.28 | 1.58 | 39% M | fa3 83.7%, flashinfer 96.3% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-8b-long-float16] | 0.1691 | 406.34 | 0.79 | 61% C | fa3 82.3%, flashinfer 96.2% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-8b-long-bfloat16] | 0.1675 | 410.33 | 0.80 | 59% C | fa3 81.6%, flashinfer 96.8% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-70b-short-float16] | 0.0426 | 201.83 | 1.58 | 39% M | fa3 82.9%, flashinfer 96.7% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-70b-short-bfloat16] | 0.0426 | 201.53 | 1.57 | 39% M | fa3 82.8%, flashinfer 96.2% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-70b-long-float16] | 0.1684 | 408.19 | 0.80 | 62% C | fa3 82.4%, flashinfer 97.1% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-70b-long-bfloat16] | 0.1676 | 410.02 | 0.80 | 59% C | fa3 81.9%, flashinfer 96.8% | - |
| 🟢 | MultiHeadLatentAttentionDecodeWithKVCacheFwdOp | test_mla_decode_bench[deepseek-v2-4k-float16] | 0.0373 | 287.53 | 1.42 | 43% C | torch-ref 441.4%, torch-compile 342.3% | - |
| 🟢 | MultiHeadLatentAttentionDecodeWithKVCacheFwdOp | test_mla_decode_bench[deepseek-v2-4k-bfloat16] | 0.0373 | 287.53 | 1.42 | 41% C | torch-ref 438.9%, torch-compile 356.3% | - |
| 🟢 | MultiHeadLatentAttentionDecodeWithKVCacheFwdOp | test_mla_decode_bench[deepseek-v2-32k-float16] | 0.1189 | 180.59 | 0.85 | 27% C | torch-ref 230.7%, torch-compile 212.5% | - |
| 🟢 | MultiHeadLatentAttentionDecodeWithKVCacheFwdOp | test_mla_decode_bench[deepseek-v2-32k-bfloat16] | 0.1189 | 180.64 | 0.85 | 26% C | torch-ref 233.6%, torch-compile 215.8% | - |
| 🟢 | MultiHeadLatentAttentionDecodeWithKVCacheFwdOp | test_mla_decode_bench[deepseek-v3-4k-bfloat16] | 0.0217 | 247.82 | 1.22 | 35% C | torch-ref 393.4%, torch-compile 342.2% | - |
| 🔵 | MultiHeadLatentAttentionDecodeWithKVCacheFwdOp | test_mla_decode_bench[deepseek-v3-32k-bfloat16] | 0.1180 | 90.98 | 0.43 | 13% C | torch-ref 145.2%, torch-compile 140.5% | - |
| 🟡 | NanToNumFwdOp | test_nan_to_num_manifest_bench[elementwise-16M-float16] | 0.0189 | 5.31 | 3.54 | 87% M | torch 101.5%, torch-compile 98.1% | - |
| 🟡 | NanToNumFwdOp | test_nan_to_num_manifest_bench[elementwise-16M-bfloat16] | 0.0189 | 5.32 | 3.55 | 87% M | torch 101.5%, torch-compile 98.3% | - |
| 🔵 | NanToNumFwdOp | test_nan_to_num_manifest_bench[elementwise-16M-float32] | 0.0339 | 2.97 | 3.96 | ✅ 97% M | torch 100.3%, torch-compile 100.2% | - |
| 🟡 | NanToNumFwdOp | test_nan_to_num_manifest_bench[elementwise-256M-float16] | 0.2650 | 6.08 | 4.05 | ✅ 100% M | torch 103.5%, torch-compile 97.8% | - |
| 🟡 | NanToNumFwdOp | test_nan_to_num_manifest_bench[elementwise-256M-bfloat16] | 0.2638 | 6.11 | 4.07 | ✅ 100% M | torch 103.6%, torch-compile 98.2% | - |
| 🔵 | NeFwdOp | test_comparison_bench[ne-1024x4096-float16-ne] | 0.0076 | 0.55 | 2.74 | - | torch 102.1%, torch-compile 102.1% | - |
| 🔵 | NeFwdOp | test_ne_manifest_bench[hidden-state-prefill-float16] | 0.0131 | 0.64 | 3.21 | 79% M | torch 100.7%, torch-compile 100.4% | - |
| 🔵 | NeFwdOp | test_ne_manifest_bench[hidden-state-prefill-bfloat16] | 0.0132 | 0.63 | 3.17 | 78% M | torch 101.2%, torch-compile 101.2% | - |
| 🟡 | NeFwdOp | test_ne_manifest_bench[hidden-state-prefill-float32] | 0.0224 | 0.38 | 3.38 | 83% M | torch 99.9%, torch-compile 99.7% | - |
| 🔴 | NeFwdOp | test_ne_manifest_bench[cnn-feat-broadcast-float16] | 0.0172 | 0.75 | 2.24 | 55% M | torch 276.5%, torch-compile 69.3% | - |
| 🔴 | NeFwdOp | test_ne_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0172 | 0.75 | 2.25 | 55% M | torch 284.7%, torch-compile 69.0% | - |
| 🟡 | NeFwdOp | test_ne_manifest_bench[cnn-feat-broadcast-float32] | 0.0215 | 0.60 | 2.99 | 73% M | torch 222.6%, torch-compile 85.8% | - |
| 🔵 | NegFwdOp | test_neg_bench[elementwise-16M-float16] | 0.0179 | 0.94 | 3.75 | ✅ 92% M | torch 105.2%, torch-compile 100.0% | - |
| 🔵 | NegFwdOp | test_neg_bench[elementwise-16M-bfloat16] | 0.0179 | 0.94 | 3.75 | ✅ 92% M | torch 100.2%, torch-compile 100.2% | - |
| 🟡 | NegFwdOp | test_neg_bench[elementwise-16M-float32] | 0.0340 | 0.49 | 3.95 | ✅ 97% M | torch 99.8%, torch-compile 99.8% | - |
| 🟡 | NegFwdOp | test_neg_bench[elementwise-256M-float16] | 0.2496 | 1.08 | 4.30 | ⚠️ 106% M | torch 107.6%, torch-compile 100.0% | - |
| 🔵 | NegFwdOp | test_neg_bench[elementwise-256M-bfloat16] | 0.2495 | 1.08 | 4.30 | ⚠️ 106% M | torch 100.1%, torch-compile 100.3% | - |
| 🔵 | PowFwdOp | test_binary_arith_bench[pow-1024x4096-float16-float16-PowFwdOp-pow-positive] | 0.0201 | 0.21 | 1.25 | - | torch 100.6%, torch-compile 117.9% | - |
| 🔵 | PowFwdOp | test_binary_arith_bench[pow-1024x10240-float16-float16-PowFwdOp-pow-positive] | 0.0453 | 0.23 | 1.39 | - | torch 100.1%, torch-compile 118.8% | - |
| 🟡 | PowFwdOp | test_pow_manifest_bench[hidden-state-prefill-float16] | 0.0370 | 0.68 | 1.36 | 33% M | torch 99.9%, torch-compile 118.8% | - |
| 🔵 | PowFwdOp | test_pow_manifest_bench[hidden-state-prefill-bfloat16] | 0.0377 | 0.67 | 1.34 | 33% M | torch 100.7%, torch-compile 120.0% | - |
| 🟡 | PowFwdOp | test_pow_manifest_bench[hidden-state-prefill-float32] | 0.0387 | 0.65 | 2.60 | 64% M | torch 96.3%, torch-compile 109.7% | - |
| 🔵 | PowFwdOp | test_pow_manifest_bench[cnn-feat-broadcast-float16] | 0.0580 | 0.66 | 0.89 | 22% M | torch 161.9%, torch-compile 105.5% | - |
| 🔵 | PowFwdOp | test_pow_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0587 | 0.66 | 0.88 | 21% M | torch 162.0%, torch-compile 105.1% | - |
| 🔵 | PowFwdOp | test_pow_manifest_bench[cnn-feat-broadcast-float32] | 0.0565 | 0.68 | 1.82 | 45% M | torch 165.9%, torch-compile 103.5% | - |
| 🔵 | PreluFwdOp | test_prelu_manifest_bench[cnn-feat-per-channel-float16] | 0.0146 | 1.76 | 3.51 | 86% M | torch 322.0%, torch-compile 100.0% | - |
| 🔵 | PreluFwdOp | test_prelu_manifest_bench[cnn-feat-per-channel-bfloat16] | 0.0144 | 1.79 | 3.58 | 88% M | torch 339.7%, torch-compile 100.2% | - |
| 🔵 | PreluFwdOp | test_prelu_manifest_bench[cnn-feat-per-channel-deep-float16] | 0.0084 | 1.54 | 3.08 | 76% M | torch 299.6%, torch-compile 100.4% | - |
| 🟡 | PreluFwdOp | test_prelu_manifest_bench[cnn-feat-per-channel-deep-bfloat16] | 0.0082 | 1.57 | 3.14 | 77% M | torch 314.7%, torch-compile 99.8% | - |
| 🔵 | ProdFwdOp | test_prod_bench[hidden-state-reduce-float16] | 0.0074 | 1.13 | 2.27 | 56% M | flaggems 106.1%, torch 666.7%, torch-compile 112.1% | - |
| 🔵 | ProdFwdOp | test_prod_bench[hidden-state-reduce-bfloat16] | 0.0074 | 1.13 | 2.27 | 56% M | flaggems 105.6%, torch 671.0%, torch-compile 113.0% | - |
| 🔵 | ProdFwdOp | test_prod_bench[long-seq-reduce-bfloat16] | 0.0043 | 0.49 | 0.97 | <sub>lat-bound</sub> | flaggems 314.1%, torch 388.9%, torch-compile 108.9% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-8b-prefill-float16] | 0.0119 | 2.83 | 2.83 | 69% M | flaggems 106.9%, flashinfer 92.2%, vllm 104.8%, torch-ref 1225.5%, torch-compile 114.6% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-8b-prefill-bfloat16] | 0.0126 | 2.65 | 2.66 | 65% M | flaggems 99.0%, flashinfer 86.2%, vllm 100.5%, torch-ref 1155.2%, torch-compile 114.2% | - |
| 🔵 | RMSNormFwdOp | test_rms_norm_bench[llama-8b-decode-bfloat16] | 0.0021 | 0.01 | 0.01 | <sub>lat-bound</sub> | flaggems 160.0%, flashinfer 104.6%, vllm 127.7%, torch-ref 866.1%, torch-compile 129.2% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-70b-prefill-float16] | 0.0210 | 3.20 | 3.20 | 79% M | flaggems 98.9%, flashinfer 95.7%, vllm 102.9%, torch-ref 1286.9%, torch-compile 93.9% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-70b-prefill-bfloat16] | 0.0218 | 3.08 | 3.08 | 76% M | flaggems 98.0%, flashinfer 91.8%, vllm 101.4%, torch-ref 1241.9%, torch-compile 96.7% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-70b-decode-bfloat16] | 0.0026 | 0.01 | 0.02 | <sub>lat-bound</sub> | flaggems 157.3%, flashinfer 98.7%, vllm 118.3%, torch-ref 713.1%, torch-compile 139.0% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-405b-prefill-float16] | 0.0420 | 3.20 | 3.20 | 79% M | flaggems 95.1%, flashinfer 88.5%, vllm 116.0%, torch-ref 1214.2%, torch-compile 94.4% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-405b-prefill-bfloat16] | 0.0430 | 3.12 | 3.12 | 77% M | flaggems 95.2%, flashinfer 88.5%, vllm 112.9%, torch-ref 1189.0%, torch-compile 95.2% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-405b-decode-bfloat16] | 0.0036 | 0.02 | 0.03 | <sub>lat-bound</sub> | flaggems 129.4%, flashinfer 98.2%, vllm 120.5%, torch-ref 559.7%, torch-compile 117.8% | - |
| 🟡 | ReciprocalFwdOp | test_reciprocal_bench[elementwise-16M-float16] | 0.0189 | 0.89 | 3.55 | 87% M | torch 100.2%, torch-compile 96.3% | - |
| 🟡 | ReciprocalFwdOp | test_reciprocal_bench[elementwise-16M-bfloat16] | 0.0189 | 0.89 | 3.54 | 87% M | torch 100.2%, torch-compile 96.5% | - |
| 🔵 | ReciprocalFwdOp | test_reciprocal_bench[elementwise-16M-float32] | 0.0335 | 0.50 | 4.01 | ✅ 98% M | torch 101.3%, torch-compile 100.8% | - |
| 🟡 | ReciprocalFwdOp | test_reciprocal_bench[elementwise-256M-float16] | 0.2672 | 1.00 | 4.02 | ✅ 99% M | torch 100.0%, torch-compile 95.8% | - |
| 🟡 | ReciprocalFwdOp | test_reciprocal_bench[elementwise-256M-bfloat16] | 0.2674 | 1.00 | 4.02 | ✅ 99% M | torch 100.0%, torch-compile 96.4% | - |
| 🔵 | ReluFwdOp | test_relu_manifest_bench[hidden-state-prefill-float16] | 0.0103 | 0.81 | 3.26 | 80% M | torch 104.7%, torch-compile 100.3% | - |
| 🔵 | ReluFwdOp | test_relu_manifest_bench[hidden-state-prefill-bfloat16] | 0.0103 | 0.81 | 3.25 | 80% M | torch 101.6%, torch-compile 100.2% | - |
| 🔵 | ReluFwdOp | test_relu_manifest_bench[hidden-state-decode-bfloat16] | 0.0012 | 0.00 | 0.01 | <sub>lat-bound</sub> | torch 113.2%, torch-compile 100.0% | - |
| 🔵 | RemainderFwdOp | test_binary_arith_bench[remainder-1024x4096-float16-float16-RemainderFwdOp-remainder-positive] | 0.0085 | 0.49 | 2.95 | - | torch 124.7%, torch-compile 100.7% | - |
| 🔵 | RemainderFwdOp | test_binary_arith_bench[remainder-1024x10240-float16-float16-RemainderFwdOp-remainder-positive] | 0.0181 | 0.58 | 3.47 | - | torch 119.6%, torch-compile 100.4% | - |
| 🔵 | RemainderFwdOp | test_remainder_manifest_bench[hidden-state-prefill-float16] | 0.0154 | 2.18 | 3.26 | 80% M | torch 117.0%, torch-compile 100.8% | - |
| 🔵 | RemainderFwdOp | test_remainder_manifest_bench[hidden-state-prefill-bfloat16] | 0.0149 | 2.25 | 3.37 | 83% M | torch 124.0%, torch-compile 101.1% | - |
| 🔵 | RemainderFwdOp | test_remainder_manifest_bench[hidden-state-prefill-float32] | 0.0264 | 1.27 | 3.82 | ✅ 94% M | torch 103.2%, torch-compile 101.3% | - |
| 🔵 | RemainderFwdOp | test_remainder_manifest_bench[cnn-feat-broadcast-float16] | 0.0171 | 3.00 | 3.00 | 74% M | torch 363.2%, torch-compile 103.7% | - |
| 🔵 | RemainderFwdOp | test_remainder_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0171 | 3.01 | 3.01 | 74% M | torch 376.7%, torch-compile 109.0% | - |
| 🟡 | RemainderFwdOp | test_remainder_manifest_bench[cnn-feat-broadcast-float32] | 0.0272 | 1.89 | 3.77 | ✅ 93% M | torch 235.6%, torch-compile 98.4% | - |
| 🔵 | RopeLlama31FwdOp | test_rope_llama31_bench[llama31-1d-8k-d128-bfloat16] | 0.0036 | 1.16 | 1.74 | <sub>lat-bound</sub> | torch-ref 439.9%, torch-compile 123.9% | - |
| 🔴 | RopeLlama31FwdOp | test_rope_llama31_bench[llama31-2d-b1-s8k-h32-d128-float16] | 0.0594 | 2.26 | 2.30 | 56% M | torch-ref 828.9%, torch-compile 58.7% | - |
| 🔵 | RopeLongRopeFwdOp | test_rope_longrope_bench[longrope-1d-8k-d128-bfloat16] | 0.0036 | 1.17 | 1.75 | <sub>lat-bound</sub> | torch-ref 443.6%, torch-compile 125.0% | - |
| 🔴 | RopeLongRopeFwdOp | test_rope_longrope_bench[longrope-2d-b1-s8k-h32-d128-float16] | 0.0594 | 2.26 | 2.29 | 56% M | torch-ref 829.0%, torch-compile 58.6% | - |
| 🔵 | RopeNeoxFwdOp | test_rope_neox_bench[neox-1d-2k-d64-float16] | 0.0018 | 0.29 | 0.43 | <sub>lat-bound</sub> | torch-ref 517.5%, torch-compile 108.8% | - |
| 🔵 | RopeNeoxFwdOp | test_rope_neox_bench[neox-1d-4k-d128-bfloat16] | 0.0026 | 0.81 | 1.21 | <sub>lat-bound</sub> | torch-ref 475.3%, torch-compile 116.1% | - |
| 🔴 | RopeNeoxFwdOp | test_rope_neox_bench[neox-2d-b2-s2k-h32-d128-float16] | 0.0308 | 2.18 | 2.19 | 54% M | torch-ref 880.9%, torch-compile 59.9% | - |
| 🔴 | RopeNeoxPositionIdsFwdOp | test_rope_neox_position_ids_bench[position-ids-s2k-h32-d128-float16] | 0.0278 | 1.21 | 1.25 | 26% M | vllm 87.3%, torch-ref 466.7%, torch-compile 42.7% | - |
| 🔴 | RopeNeoxPositionIdsFwdOp | test_rope_neox_position_ids_bench[position-ids-s4k-h32-d128-bfloat16] | 0.0456 | 1.47 | 1.52 | 34% M | vllm 97.8%, torch-ref 545.5%, torch-compile 48.8% | - |
| 🟡 | RopeNonNeoxFwdOp | test_rope_non_neox_bench[non-neox-1d-2k-d64-float16] | 0.0022 | 0.24 | 0.36 | <sub>lat-bound</sub> | torch-ref 435.3%, torch-compile 91.2% | - |
| 🔴 | RopeNonNeoxFwdOp | test_rope_non_neox_bench[non-neox-2d-b2-s2k-h32-d128-bfloat16] | 0.0252 | 2.66 | 2.69 | 66% M | torch-ref 1088.6%, torch-compile 75.5% | - |
| 🔵 | RopeYarnFwdOp | test_rope_yarn_bench[yarn-1d-8k-d128-bfloat16] | 0.0036 | 1.16 | 1.74 | <sub>lat-bound</sub> | torch-ref 440.7%, torch-compile 123.9% | - |
| 🔴 | RopeYarnFwdOp | test_rope_yarn_bench[yarn-2d-b1-s8k-h32-d128-float16] | 0.0594 | 2.26 | 2.29 | 56% M | torch-ref 828.3%, torch-compile 58.6% | - |
| 🔵 | RoundFwdOp | test_round_bench[elementwise-16M-float16] | 0.0179 | 0.94 | 3.75 | ✅ 92% M | torch 100.3%, torch-compile 100.2% | - |
| 🔵 | RoundFwdOp | test_round_bench[elementwise-16M-bfloat16] | 0.0179 | 0.94 | 3.76 | ✅ 92% M | torch 100.7%, torch-compile 100.3% | - |
| 🟡 | RoundFwdOp | test_round_bench[elementwise-16M-float32] | 0.0340 | 0.49 | 3.95 | ✅ 97% M | torch 99.9%, torch-compile 100.0% | - |
| 🟡 | RoundFwdOp | test_round_bench[elementwise-256M-float16] | 0.2499 | 1.07 | 4.30 | ⚠️ 106% M | torch 100.2%, torch-compile 100.0% | - |
| 🔵 | RoundFwdOp | test_round_bench[elementwise-256M-bfloat16] | 0.2499 | 1.07 | 4.30 | ⚠️ 106% M | torch 100.2%, torch-compile 100.3% | - |
| 🔵 | RsqrtFwdOp | test_rsqrt_bench[elementwise-16M-float16] | 0.0181 | 0.92 | 3.70 | ✅ 91% M | torch 100.4%, torch-compile 100.2% | - |
| 🔵 | RsqrtFwdOp | test_rsqrt_bench[elementwise-16M-bfloat16] | 0.0181 | 0.93 | 3.71 | ✅ 91% M | torch 100.6%, torch-compile 100.4% | - |
| 🔵 | RsqrtFwdOp | test_rsqrt_bench[elementwise-16M-float32] | 0.0331 | 0.51 | 4.06 | ✅ 100% M | torch 102.0%, torch-compile 101.8% | - |
| 🟡 | RsqrtFwdOp | test_rsqrt_bench[elementwise-256M-float16] | 0.2539 | 1.06 | 4.23 | ✅ 104% M | torch 100.2%, torch-compile 99.7% | - |
| 🟡 | RsqrtFwdOp | test_rsqrt_bench[elementwise-256M-bfloat16] | 0.2534 | 1.06 | 4.24 | ✅ 104% M | torch 100.4%, torch-compile 100.0% | - |
| 🔵 | SSDChunkScanFwdOp | test_ssd_chunk_scan_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0729 | 88.34 | 1.44 | 35% M | mamba 138.0%, torch-ref 2684.6%, torch-compile 695.5% | - |
| 🔵 | SSDChunkScanFwdOp | test_ssd_chunk_scan_fwd_bench[mamba2-780m-b1-s4k-bfloat16] | 0.0761 | 84.63 | 1.38 | 34% M | mamba 133.9%, torch-ref 2574.8%, torch-compile 669.1% | - |
| 🔵 | SSDChunkScanFwdOp | test_ssd_chunk_scan_fwd_bench[mamba2-2p7b-b4-s2k-bfloat16] | 0.2370 | 90.63 | 1.46 | 36% M | mamba 130.4%, torch-ref 2750.9%, torch-compile 692.0% | - |
| 🔵 | SSDChunkScanFwdOp | test_ssd_chunk_scan_fwd_bench[mamba2-1p3b-b2-s32k-float16] | 1.4696 | 93.52 | 1.51 | 37% M | mamba 138.4%, torch-ref 2726.6%, torch-compile 678.8% | - |
| 🔵 | SSDChunkStateFwdOp | test_ssd_chunk_state_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0238 | 136.14 | 2.21 | 54% M | mamba 105.2%, torch-ref 34251.9%, torch-compile 2666.5% | - |
| 🔵 | SSDChunkStateFwdOp | test_ssd_chunk_state_fwd_bench[mamba2-780m-b1-s4k-bfloat16] | 0.0240 | 134.69 | 2.19 | 54% M | mamba 109.8%, torch-ref 33876.7%, torch-compile 2815.7% | - |
| 🔵 | SSDChunkStateFwdOp | test_ssd_chunk_state_fwd_bench[mamba2-2p7b-b4-s2k-bfloat16] | 0.0656 | 164.36 | 2.65 | 65% M | mamba 121.8%, torch-ref 41318.7%, torch-compile 3726.4% | - |
| 🔵 | SSDChunkStateFwdOp | test_ssd_chunk_state_fwd_bench[mamba2-780m-b1-s4k-seq-idx-float16] | 0.0287 | 112.81 | 1.83 | 45% M | mamba 120.8%, torch-ref 28417.5%, torch-compile 2616.2% | - |
| 🔵 | SSDChunkStateFwdOp | test_ssd_chunk_state_fwd_bench[mamba2-780m-b1-s4k-seq-idx-bfloat16] | 0.0290 | 111.69 | 1.82 | 45% M | mamba 100.6%, torch-ref 28147.2%, torch-compile 2721.2% | - |
| 🔵 | SSDChunkStateFwdOp | test_ssd_chunk_state_fwd_bench[mamba2-1p3b-b2-s32k-seq-idx-float16] | 0.4494 | 153.53 | 2.48 | 61% M | mamba 144.3%, torch-ref 38519.7%, torch-compile 3709.0% | - |
| 🟢 | SSDDecodeFwdOp | test_ssd_decode_bench[mamba2-1p3b-decode-b1-float16] | 0.0040 | 1.06 | 1.60 | <sub>lat-bound</sub> | torch-ref 756.5%, torch-compile 229.8% | - |
| 🟢 | SSDDecodeFwdOp | test_ssd_decode_bench[mamba2-1p3b-decode-b1-bfloat16] | 0.0040 | 1.06 | 1.60 | <sub>lat-bound</sub> | torch-ref 766.3%, torch-compile 227.5% | - |
| 🟢 | SSDDecodeFwdOp | test_ssd_decode_bench[mamba2-2p7b-decode-b8-float16] | 0.0163 | 2.58 | 2.77 | 68% M | torch-ref 690.2%, torch-compile 187.2% | - |
| 🟢 | SSDDecodeFwdOp | test_ssd_decode_bench[mamba2-780m-decode-b32-float16] | 0.0363 | 2.78 | 2.85 | 70% M | torch-ref 663.0%, torch-compile 191.9% | - |
| 🟢 | SSDStatePassingFwdOp | test_ssd_state_passing_fwd_bench[mamba2-1p3b-b1-s4k-dstate-float16] | 0.0019 | 0.14 | 0.43 | <sub>lat-bound</sub> | mamba 436.7%, torch-ref 6314.9%, torch-compile 213.3% | - |
| 🟢 | SSDStatePassingFwdOp | test_ssd_state_passing_fwd_bench[mamba2-1p3b-b1-s4k-dstate-bfloat16] | 0.0020 | 0.13 | 0.41 | <sub>lat-bound</sub> | mamba 421.0%, torch-ref 6206.8%, torch-compile 206.4% | - |
| 🟢 | SSDStatePassingFwdOp | test_ssd_state_passing_fwd_bench[mamba2-2p7b-b2-s32k-dstate-float16] | 0.0106 | 0.50 | 1.50 | 37% M | mamba 564.9%, torch-ref 10901.8%, torch-compile 858.6% | - |
| 🔵 | SSDStatePassingFwdOp | test_ssd_state_passing_fwd_bench[mamba2-1p3b-b1-s4k-dstate-init-states-float16] | 0.0020 | 0.13 | 0.43 | <sub>lat-bound</sub> | mamba 438.7%, torch-ref 6061.4%, torch-compile 108.1% | - |
| 🔵 | SSDStatePassingFwdOp | test_ssd_state_passing_fwd_bench[mamba2-1p3b-b1-s4k-dstate-init-states-bfloat16] | 0.0020 | 0.13 | 0.42 | <sub>lat-bound</sub> | mamba 442.9%, torch-ref 6054.0%, torch-compile 106.4% | - |
| 🟡 | SSDStatePassingFwdOp | test_ssd_state_passing_fwd_bench[mamba2-1p3b-b1-s4k-flat-init-states-float32] | 0.0219 | 0.77 | 3.25 | 80% M | mamba 98.5%, torch-ref 578.8%, torch-compile 93.4% | - |
| 🔵 | SeluFwdOp | test_selu_manifest_bench[snn-fc-float16] | 0.0117 | 3.57 | 2.86 | 70% M | torch 152.9%, torch-compile 137.1% | - |
| 🔵 | SeluFwdOp | test_selu_manifest_bench[snn-fc-bfloat16] | 0.0121 | 3.47 | 2.77 | 68% M | torch 150.0%, torch-compile 129.4% | - |
| 🔵 | SeluFwdOp | test_selu_manifest_bench[snn-fc-wide-float16] | 0.0211 | 3.98 | 3.19 | 78% M | torch 156.1%, torch-compile 142.6% | - |
| 🔵 | SeluFwdOp | test_selu_manifest_bench[snn-fc-wide-bfloat16] | 0.0218 | 3.86 | 3.08 | 76% M | torch 152.5%, torch-compile 134.3% | - |
| 🔴 | SharedFusedMoE | test_shared_fused_moe_bench[1-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 2.5217 | 0.59 | 0.59 | - | vllm 16.9% | - |
| 🟡 | SharedFusedMoE | test_shared_fused_moe_bench[32-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 4.7400 | 10.11 | 3.67 | - | vllm 83.6% | - |
| 🔵 | SharedFusedMoE | test_shared_fused_moe_bench[512-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 8.0613 | 95.10 | 4.30 | - | vllm 108.8% | - |
| 🔴 | SharedFusedMoE | test_shared_fused_moe_bench[2048-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 19.5167 | 157.13 | 1.78 | - | vllm 59.6% | - |
| 🔴 | SharedFusedMoE | test_shared_fused_moe_bench[4096-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 32.5292 | 188.54 | 1.07 | - | vllm 44.5% | - |
| 🟡 | SigmoidFwdOp | test_sigmoid_manifest_bench[elementwise-16M-float16] | 0.0214 | 3.13 | 3.13 | 77% M | torch 106.9%, torch-compile 86.6% | - |
| 🟡 | SigmoidFwdOp | test_sigmoid_manifest_bench[elementwise-16M-bfloat16] | 0.0218 | 3.08 | 3.08 | 76% M | torch 107.6%, torch-compile 85.6% | - |
| 🟡 | SigmoidFwdOp | test_sigmoid_manifest_bench[elementwise-16M-float32] | 0.0344 | 1.95 | 3.90 | ✅ 96% M | torch 100.0%, torch-compile 98.9% | - |
| 🟡 | SigmoidFwdOp | test_sigmoid_manifest_bench[elementwise-256M-float16] | 0.3024 | 3.55 | 3.55 | 87% M | torch 106.2%, torch-compile 86.1% | - |
| 🟡 | SigmoidFwdOp | test_sigmoid_manifest_bench[elementwise-256M-bfloat16] | 0.3068 | 3.50 | 3.50 | 86% M | torch 107.5%, torch-compile 85.8% | - |
| 🟡 | SignFwdOp | test_sign_bench[elementwise-16M-float16] | 0.0186 | 1.80 | 3.61 | 89% M | torch 97.4%, torch-compile 96.5% | - |
| 🟡 | SignFwdOp | test_sign_bench[elementwise-16M-bfloat16] | 0.0186 | 1.80 | 3.60 | 89% M | torch 97.6%, torch-compile 96.7% | - |
| 🟡 | SignFwdOp | test_sign_bench[elementwise-16M-float32] | 0.0340 | 0.99 | 3.95 | ✅ 97% M | torch 100.0%, torch-compile 99.9% | - |
| 🟡 | SignFwdOp | test_sign_bench[elementwise-256M-float16] | 0.2636 | 2.04 | 4.07 | ✅ 100% M | torch 97.2%, torch-compile 95.4% | - |
| 🟡 | SignFwdOp | test_sign_bench[elementwise-256M-bfloat16] | 0.2637 | 2.04 | 4.07 | ✅ 100% M | torch 98.2%, torch-compile 96.2% | - |
| 🔵 | SiluAndMulFwdOp | test_silu_and_mul_bench[llama-8b-swiglu-prefill-float16] | 0.0435 | 4.05 | 4.05 | ✅ 99% M | flashinfer 122.6%, torch-ref 435.1%, torch-compile 101.5% | - |
| 🔵 | SiluAndMulFwdOp | test_silu_and_mul_bench[llama-8b-swiglu-prefill-bfloat16] | 0.0433 | 4.07 | 4.07 | ✅ 100% M | flashinfer 124.4%, torch-ref 439.0%, torch-compile 105.4% | - |
| 🟡 | SiluAndMulFwdOp | test_silu_and_mul_bench[llama-8b-swiglu-decode-bfloat16] | 0.0017 | 0.05 | 0.05 | <sub>lat-bound</sub> | flashinfer 248.2%, torch-ref 201.8%, torch-compile 88.9% | - |
| 🟡 | SiluFwdOp | test_silu_manifest_bench[llama-8b-ffn-prefill-float16] | 0.0367 | 4.00 | 3.20 | 79% M | torch 103.0%, torch-compile 96.8% | - |
| 🟡 | SiluFwdOp | test_silu_manifest_bench[llama-8b-ffn-prefill-bfloat16] | 0.0365 | 4.02 | 3.22 | 79% M | torch 103.9%, torch-compile 97.8% | - |
| 🟡 | SiluFwdOp | test_silu_manifest_bench[llama-8b-ffn-decode-bfloat16] | 0.0015 | 0.05 | 0.04 | <sub>lat-bound</sub> | torch 127.1%, torch-compile 89.6% | - |
| 🔵 | SinFwdOp | test_sin_bench[elementwise-16M-float16] | 0.0254 | 0.66 | 2.64 | 65% M | torch 103.0%, torch-compile 104.2% | - |
| 🔵 | SinFwdOp | test_sin_bench[elementwise-16M-bfloat16] | 0.0259 | 0.65 | 2.59 | 64% M | torch 103.2%, torch-compile 103.6% | - |
| 🟡 | SinFwdOp | test_sin_bench[elementwise-16M-float32] | 0.0348 | 0.48 | 3.85 | ✅ 95% M | torch 98.4%, torch-compile 98.4% | - |
| 🔵 | SinFwdOp | test_sin_bench[elementwise-256M-float16] | 0.3670 | 0.73 | 2.93 | 72% M | torch 102.8%, torch-compile 104.9% | - |
| 🔵 | SinFwdOp | test_sin_bench[elementwise-256M-bfloat16] | 0.3735 | 0.72 | 2.87 | 71% M | torch 103.3%, torch-compile 104.8% | - |
| 🔵 | SinusoidalFwdOp | test_sinusoidal_bench[transformer-2k-4k-float16] | 0.0425 | 1.18 | 0.39 | 10% M | torch-ref 250.4%, torch-compile 133.4% | - |
| 🔵 | SinusoidalFwdOp | test_sinusoidal_bench[transformer-2k-4k-bfloat16] | 0.0425 | 1.18 | 0.39 | 10% M | torch-ref 250.6%, torch-compile 133.4% | - |
| 🔵 | SinusoidalFwdOp | test_sinusoidal_bench[transformer-4k-4k-float16] | 0.0818 | 1.23 | 0.41 | 10% M | torch-ref 243.2%, torch-compile 136.5% | - |
| 🔵 | SinusoidalFwdOp | test_sinusoidal_bench[transformer-4k-4k-bfloat16] | 0.0818 | 1.23 | 0.41 | 10% M | torch-ref 243.3%, torch-compile 136.5% | - |
| 🔵 | SoftmaxFwdOp | test_softmax_bench[attn-weights-4k-float16] | 0.0084 | 2.49 | 1.99 | 49% M | flaggems 102.3%, torch 235.0%, torch-compile 191.6% | - |
| 🔵 | SoftmaxFwdOp | test_softmax_bench[attn-weights-4k-bfloat16] | 0.0084 | 2.50 | 2.00 | 49% M | flaggems 103.2%, torch 234.3%, torch-compile 198.8% | - |
| 🔵 | SoftmaxFwdOp | test_softmax_bench[attn-weights-4k-float32] | 0.0110 | 1.90 | 3.04 | 75% M | flaggems 100.7%, torch 183.5%, torch-compile 175.0% | - |
| 🔵 | SoftmaxFwdOp | test_softmax_bench[attn-weights-32k-bfloat16] | 0.0617 | 2.72 | 2.17 | 53% M | flaggems 104.1%, torch 134.9%, torch-compile 152.2% | - |
| 🟡 | SoftmaxFwdOp | test_softmax_bench[lm-head-logits-float16] | 0.0106 | 0.19 | 0.16 | <sub>lat-bound</sub> | flaggems 266.4%, torch 311.8%, torch-compile 91.2% | - |
| 🟡 | SoftmaxFwdOp | test_softmax_bench[lm-head-logits-bfloat16] | 0.0106 | 0.19 | 0.16 | <sub>lat-bound</sub> | flaggems 280.6%, torch 319.4%, torch-compile 91.2% | - |
| 🟡 | SoftmaxFwdOp | test_softmax_bench[lm-head-logits-float32] | 0.0109 | 0.19 | 0.30 | <sub>lat-bound</sub> | flaggems 285.7%, torch 360.1%, torch-compile 85.4% | - |
| 🔵 | SoftplusFwdOp | test_softplus_manifest_bench[mlp-hidden-float16] | 0.0126 | 3.33 | 2.66 | 65% M | torch 189.1%, torch-compile 142.1% | - |
| 🔵 | SoftplusFwdOp | test_softplus_manifest_bench[mlp-hidden-bfloat16] | 0.0128 | 3.28 | 2.62 | 64% M | torch 188.5%, torch-compile 143.0% | - |
| 🔵 | SoftplusFwdOp | test_softplus_manifest_bench[mlp-hidden-wide-float16] | 0.0229 | 3.67 | 2.93 | 72% M | torch 195.2%, torch-compile 143.5% | - |
| 🔵 | SoftplusFwdOp | test_softplus_manifest_bench[mlp-hidden-wide-bfloat16] | 0.0232 | 3.62 | 2.89 | 71% M | torch 194.8%, torch-compile 145.6% | - |
| 🔵 | SqrtFwdOp | test_sqrt_bench[elementwise-16M-float16] | 0.0186 | 0.90 | 3.61 | 89% M | torch 101.7%, torch-compile 100.3% | - |
| 🔵 | SqrtFwdOp | test_sqrt_bench[elementwise-16M-bfloat16] | 0.0187 | 0.90 | 3.60 | 88% M | torch 101.7%, torch-compile 100.4% | - |
| 🔵 | SqrtFwdOp | test_sqrt_bench[elementwise-16M-float32] | 0.0334 | 0.50 | 4.02 | ✅ 99% M | torch 101.8%, torch-compile 101.7% | - |
| 🔵 | SqrtFwdOp | test_sqrt_bench[elementwise-256M-float16] | 0.2627 | 1.02 | 4.09 | ✅ 100% M | torch 101.2%, torch-compile 100.0% | - |
| 🔵 | SqrtFwdOp | test_sqrt_bench[elementwise-256M-bfloat16] | 0.2636 | 1.02 | 4.07 | ✅ 100% M | torch 101.3%, torch-compile 100.2% | - |
| 🔵 | StdFwdOp | test_std_bench[hidden-state-std-float16] | 0.0084 | 4.97 | 1.99 | 49% M | flaggems 125.4%, torch 801.5%, torch-compile 222.3% | - |
| 🔵 | StdFwdOp | test_std_bench[hidden-state-std-bfloat16] | 0.0085 | 4.94 | 1.98 | 49% M | flaggems 130.7%, torch 801.5%, torch-compile 226.8% | - |
| 🔵 | StdFwdOp | test_std_bench[long-seq-std-bfloat16] | 0.0052 | 2.02 | 0.81 | <sub>lat-bound</sub> | flaggems 253.7%, torch 481.2%, torch-compile 118.5% | - |
| 🔵 | StdFwdOp | test_std_bench[3d-multidim-reduce-float16] | 0.0052 | 2.02 | 0.81 | <sub>lat-bound</sub> | flaggems 275.3%, torch 519.1%, torch-compile 119.1% | - |
| 🔵 | SubFwdOp | test_binary_arith_bench[sub-1024x4096-float16-float16-SubFwdOp-sub-normal] | 0.0084 | 0.50 | 2.99 | - | torch 101.2%, torch-compile 100.4% | - |
| 🔵 | SubFwdOp | test_binary_arith_bench[sub-1024x10240-float16-float16-SubFwdOp-sub-normal] | 0.0176 | 0.59 | 3.57 | - | torch 100.5%, torch-compile 100.2% | - |
| 🔵 | SubFwdOp | test_binary_arith_bench[sub-1024x11008-float16-float16-SubFwdOp-sub-normal] | 0.0186 | 0.61 | 3.64 | - | torch 100.2%, torch-compile 100.2% | - |
| 🔵 | SubFwdOp | test_sub_manifest_bench[hidden-state-prefill-float16] | 0.0148 | 1.13 | 3.40 | 83% M | torch 100.4%, torch-compile 100.2% | - |
| 🔵 | SubFwdOp | test_sub_manifest_bench[hidden-state-prefill-bfloat16] | 0.0148 | 1.13 | 3.40 | 84% M | torch 100.9%, torch-compile 100.2% | - |
| 🟡 | SubFwdOp | test_sub_manifest_bench[hidden-state-prefill-float32] | 0.0265 | 0.63 | 3.80 | ✅ 93% M | torch 100.0%, torch-compile 99.6% | - |
| 🟡 | SubFwdOp | test_sub_manifest_bench[cnn-feat-broadcast-float16] | 0.0146 | 1.76 | 3.53 | 87% M | torch 314.1%, torch-compile 99.1% | - |
| 🟡 | SubFwdOp | test_sub_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0146 | 1.76 | 3.53 | 87% M | torch 319.3%, torch-compile 99.7% | - |
| 🟡 | SubFwdOp | test_sub_manifest_bench[cnn-feat-broadcast-float32] | 0.0266 | 0.97 | 3.86 | ✅ 95% M | torch 185.8%, torch-compile 99.8% | - |
| 🔵 | SumFwdOp | test_sum_bench[hidden-state-reduce-float16] | 0.0074 | 1.13 | 2.26 | 56% M | flaggems 118.1%, torch 666.4%, torch-compile 112.5% | - |
| 🔵 | SumFwdOp | test_sum_bench[hidden-state-reduce-bfloat16] | 0.0074 | 1.13 | 2.26 | 56% M | flaggems 118.5%, torch 671.1%, torch-compile 113.4% | - |
| 🟡 | SumFwdOp | test_sum_bench[long-seq-reduce-bfloat16] | 0.0041 | 0.52 | 1.03 | <sub>lat-bound</sub> | flaggems 93.7%, torch 417.3%, torch-compile 115.0% | - |
| 🟡 | SumFwdOp | test_sum_bench[hidden-state-reduce-dim0-bfloat16] | 0.0121 | 0.69 | 1.38 | 34% M | flaggems 112.8%, torch 368.3%, torch-compile 91.8% | - |
| 🔵 | SumFwdOp | test_sum_bench[hidden-state-reduce-keepdim-bfloat16] | 0.0074 | 1.13 | 2.26 | 56% M | flaggems 118.5%, torch 671.1%, torch-compile 113.4% | - |
| 🔴 | SumFwdOp | test_sum_bench[3d-multidim-reduce-float16] | 0.0057 | 0.37 | 0.73 | <sub>lat-bound</sub> | flaggems 235.2%, torch 336.3%, torch-compile 78.2% | - |
| 🟡 | TanhFwdOp | test_tanh_manifest_bench[elementwise-16M-float16] | 0.0208 | 0.81 | 3.23 | 79% M | torch 99.6%, torch-compile 116.6% | - |
| 🔵 | TanhFwdOp | test_tanh_manifest_bench[elementwise-16M-bfloat16] | 0.0213 | 0.79 | 3.15 | 77% M | torch 102.4%, torch-compile 115.2% | - |
| 🔵 | TanhFwdOp | test_tanh_manifest_bench[elementwise-16M-float32] | 0.0339 | 0.50 | 3.96 | ✅ 97% M | torch 100.8%, torch-compile 101.6% | - |
| 🟡 | TanhFwdOp | test_tanh_manifest_bench[elementwise-256M-float16] | 0.2956 | 0.91 | 3.63 | 89% M | torch 98.7%, torch-compile 116.5% | - |
| 🔵 | TanhFwdOp | test_tanh_manifest_bench[elementwise-256M-bfloat16] | 0.3027 | 0.89 | 3.55 | 87% M | torch 102.4%, torch-compile 116.3% | - |
| 🔴 | TopkSelectorFwdOp | test_topk_selector_bench[topk1024-s32k-kv64k-float32] | 15.6212 | 0.14 | 0.56 | 14% M | torch 203.8%, torch-compile 203.8%, flashinfer 59.4% | - |
| 🔴 | TopkSelectorFwdOp | test_topk_selector_bench[topk2048-s32k-kv64k-float32] | 16.2611 | 0.13 | 0.54 | 13% M | torch 204.9%, torch-compile 204.9%, flashinfer 65.6% | - |
| 🔵 | TruncFwdOp | test_trunc_bench[elementwise-16M-float16] | 0.0179 | 0.94 | 3.75 | ✅ 92% M | torch 100.4%, torch-compile 100.2% | - |
| 🔵 | TruncFwdOp | test_trunc_bench[elementwise-16M-bfloat16] | 0.0179 | 0.94 | 3.75 | ✅ 92% M | torch 100.2%, torch-compile 100.2% | - |
| 🟡 | TruncFwdOp | test_trunc_bench[elementwise-16M-float32] | 0.0340 | 0.49 | 3.94 | ✅ 97% M | torch 99.9%, torch-compile 99.7% | - |
| 🟡 | TruncFwdOp | test_trunc_bench[elementwise-256M-float16] | 0.2499 | 1.07 | 4.30 | ⚠️ 106% M | torch 100.2%, torch-compile 100.0% | - |
| 🔵 | TruncFwdOp | test_trunc_bench[elementwise-256M-bfloat16] | 0.2500 | 1.07 | 4.30 | ⚠️ 106% M | torch 100.1%, torch-compile 100.2% | - |
| 🟢 | VarFwdOp | test_var_bench[hidden-state-var-float16] | 0.0084 | 5.02 | 2.01 | 49% M | flaggems 179.7%, torch 810.3%, torch-compile 218.8% | - |
| 🟢 | VarFwdOp | test_var_bench[hidden-state-var-bfloat16] | 0.0084 | 5.00 | 2.00 | 49% M | flaggems 184.0%, torch 812.6%, torch-compile 223.7% | - |
| 🔵 | VarFwdOp | test_var_bench[long-seq-var-bfloat16] | 0.0052 | 2.04 | 0.81 | <sub>lat-bound</sub> | flaggems 216.2%, torch 483.2%, torch-compile 122.4% | - |
| 🔵 | VarFwdOp | test_var_bench[3d-multidim-reduce-float16] | 0.0051 | 2.05 | 0.82 | <sub>lat-bound</sub> | flaggems 276.2%, torch 525.6%, torch-compile 123.8% | - |
| 🟢 | VarMeanFwdOp | test_var_mean_bench[hidden-state-var-mean-float16] | 0.0084 | 5.00 | 2.00 | 49% M | flaggems 179.8%, torch 1389.5%, torch-compile 250.0% | - |
| 🟢 | VarMeanFwdOp | test_var_mean_bench[hidden-state-var-mean-bfloat16] | 0.0084 | 4.96 | 1.99 | 49% M | flaggems 183.3%, torch 1386.7%, torch-compile 259.1% | - |
| 🟢 | VarMeanFwdOp | test_var_mean_bench[long-seq-var-mean-bfloat16] | 0.0052 | 2.04 | 0.81 | <sub>lat-bound</sub> | flaggems 216.2%, torch 788.8%, torch-compile 153.4% | - |
| 🟢 | VarMeanFwdOp | test_var_mean_bench[3d-multidim-reduce-float16] | 0.0052 | 2.04 | 0.81 | <sub>lat-bound</sub> | flaggems 275.2%, torch 873.9%, torch-compile 156.0% | - |
| 🟡 | WhereFwdOp | test_where_manifest_bench[elementwise-16M-float16] | 0.0310 | 0.54 | 3.79 | ✅ 93% M | torch 99.1%, torch-compile 99.1% | - |
| 🟡 | WhereFwdOp | test_where_manifest_bench[elementwise-16M-bfloat16] | 0.0312 | 0.54 | 3.77 | ✅ 93% M | torch 98.7%, torch-compile 98.5% | - |
| 🟡 | WhereFwdOp | test_where_manifest_bench[elementwise-16M-float32] | 0.0535 | 0.31 | 4.08 | ✅ 100% M | torch 99.8%, torch-compile 98.9% | - |
| 🟡 | WhereFwdOp | test_where_manifest_bench[elementwise-256M-float16] | 0.4290 | 0.63 | 4.38 | ⚠️ 108% M | torch 99.8%, torch-compile 99.8% | - |
| 🟡 | WhereFwdOp | test_where_manifest_bench[elementwise-256M-bfloat16] | 0.4286 | 0.63 | 4.38 | ⚠️ 108% M | torch 99.9%, torch-compile 99.8% | - |
| 🟡 | div_bcast | test_broadcast_bench[div-1024x4096-1x4096-float16-DivFwdOp-div-positive] | 0.0064 | 0.65 | 2.61 | - | torch 253.2%, torch-compile 96.5% | - |
| 🟡 | div_bcast | test_broadcast_bench[div-1024x10240-1x10240-float16-DivFwdOp-div-positive] | 0.0132 | 0.79 | 3.17 | - | torch 274.5%, torch-compile 93.1% | - |
| 🟡 | div_bcast | test_broadcast_bench[div-1024x11008-1x11008-float16-DivFwdOp-div-positive] | 0.0153 | 0.74 | 2.96 | - | torch 253.7%, torch-compile 86.0% | - |
| 🔴 | gelu_and_mul_strategy | test_fused_gated_strategy_bench[gelu_and_mul-1024-4096-float16-GeluAndMulFwdKernel-direct] | 0.0182 | 0.46 | 1.38 | - | torch 184.1%, torch-compile 58.6% | - |
| 🔵 | gelu_and_mul_strategy | test_fused_gated_strategy_bench[gelu_and_mul-1024-4096-float16-GeluAndMulFwdKernel-explicit_parallel] | 0.0100 | 0.83 | 2.50 | - | torch 332.8%, torch-compile 106.0% | - |
| 🔴 | gelu_tanh_and_mul_strategy | test_fused_gated_strategy_bench[gelu_tanh_and_mul-1024-4096-float16-GeluTanhAndMulFwdKernel-direct] | 0.0178 | 0.47 | 1.42 | - | torch 179.6%, torch-compile 54.9% | - |
| 🔵 | gelu_tanh_and_mul_strategy | test_fused_gated_strategy_bench[gelu_tanh_and_mul-1024-4096-float16-GeluTanhAndMulFwdKernel-explicit_parallel] | 0.0088 | 0.95 | 2.85 | - | torch 360.9%, torch-compile 110.5% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-up-T=32768] | 18.1854 | 725.53 | 1.00 | - | torch 126.8%, deepgemm 101.3%, triton 151.9%, triton-tma 129.7% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-up-T=65536] | 37.6031 | 701.76 | 0.63 | - | torch 108.0%, deepgemm 108.7%, triton 144.8%, triton-tma 116.3% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-up-T=131072] | 75.0504 | 703.22 | 0.46 | - | torch 107.0%, deepgemm 100.5%, triton 141.6%, triton-tma 111.6% | - |
| 🟡 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-up-T=262144] | 152.6760 | 691.35 | 0.37 | - | torch 114.8%, deepgemm 98.8%, triton 141.1%, triton-tma 109.9% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[Llama4-128E-up-T=131072] | 30.9611 | 710.25 | 0.88 | - | torch 103.9%, deepgemm 100.2%, triton 167.9%, triton-tma 131.1% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[qwen3.5-397B-up-T52429] | 12.7116 | 691.98 | 1.18 | - | torch 104.3%, deepgemm 100.9%, triton 151.6%, triton-tma 134.4% | - |
| 🟡 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-down-T=32768] | 9.7054 | 679.73 | 1.11 | - | torch 102.8%, deepgemm 99.5%, triton 151.2%, triton-tma 116.0% | - |
| 🟡 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-down-T=65536] | 19.1642 | 688.48 | 0.78 | - | torch 116.6%, deepgemm 97.4%, triton 151.1%, triton-tma 110.5% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-down-T=131072] | 38.4814 | 685.74 | 0.61 | - | torch 109.0%, deepgemm 107.2%, triton 150.2%, triton-tma 113.5% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-down-T=262144] | 76.9473 | 685.88 | 0.53 | - | torch 109.7%, deepgemm 100.8%, triton 149.6%, triton-tma 110.9% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[Llama4-128E-down-T=131072] | 15.2979 | 718.73 | 0.93 | - | torch 103.0%, deepgemm 103.1%, triton 151.7%, triton-tma 119.7% | - |
| 🟡 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[qwen3.5-397B-down-T52429] | 6.9207 | 635.50 | 1.40 | - | torch 108.6%, deepgemm 97.4%, triton 148.0%, triton-tma 130.4% | - |
| 🔴 | grouped_gemm_nn | test_grouped_gemm_bench[nn-batch16-m4096-n4096-k4096-float16] | 0.3406 | 403.55 | 1.77 | 61% C | torch-ref 90.0%, torch-compile 80.8%, torch 79.0% | - |
| 🔵 | grouped_gemm_nt | test_grouped_gemm_bench[nt-batch16-m4096-n4096-k4096-float16] | 0.2320 | 592.28 | 2.60 | ✅ 90% C | torch-ref 1003.6%, torch-compile 989.2%, torch 116.1% | - |
| 🟡 | grouped_gemm_nt | test_grouped_gemm_bench[nt-batch16-m4096-n4096-k4096-bfloat16] | 0.2264 | 606.98 | 2.67 | ✅ 87% C | torch-ref 1008.5%, torch-compile 992.7%, torch 99.4% | - |
| 🔴 | grouped_gemm_tn | test_grouped_gemm_bench[tn-batch16-m4096-n4096-k4096-float16] | 0.7808 | 176.03 | 0.77 | 27% C | torch-ref 67.5%, torch-compile 66.9%, torch 45.3% | - |
| 🔵 | mul_bcast | test_broadcast_bench[mul-1024x4096-1x4096-float16-MulFwdOp-mul-normal] | 0.0060 | 0.70 | 2.81 | - | torch 249.2%, torch-compile 101.1% | - |
| 🔵 | mul_bcast | test_broadcast_bench[mul-1024x10240-1x10240-float16-MulFwdOp-mul-normal] | 0.0123 | 0.86 | 3.42 | - | torch 269.4%, torch-compile 100.5% | - |
| 🟡 | mul_bcast | test_broadcast_bench[mul-1024x11008-1x11008-float16-MulFwdOp-mul-normal] | 0.0130 | 0.87 | 3.47 | - | torch 271.4%, torch-compile 99.8% | - |
| 🔴 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float16-SiluAndMulFwdKernel-direct] | 0.0178 | 0.47 | 1.41 | - | torch 177.0%, torch-compile 46.8% | - |
| 🔴 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-11008-float16-SiluAndMulFwdKernel-direct] | 0.0451 | 0.50 | 1.50 | - | torch 170.7%, torch-compile 42.3% | - |
| 🔴 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-4096-4096-float16-SiluAndMulFwdKernel-direct] | 0.0662 | 0.51 | 1.52 | - | torch 168.2%, torch-compile 40.6% | - |
| 🔴 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-bfloat16-SiluAndMulFwdKernel-direct] | 0.0179 | 0.47 | 1.41 | - | torch 177.8%, torch-compile 47.1% | - |
| 🔴 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float32-SiluAndMulFwdKernel-direct] | 0.0201 | 0.42 | 2.51 | - | torch 173.2%, torch-compile 72.9% | - |
| 🟡 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float16-SiluAndMulFwdKernel-explicit_parallel] | 0.0084 | 1.00 | 2.99 | - | torch 374.5%, torch-compile 98.9% | - |
| 🔵 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-11008-float16-SiluAndMulFwdKernel-explicit_parallel] | 0.0189 | 1.19 | 3.58 | - | torch 406.8%, torch-compile 100.7% | - |
| 🔵 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-4096-4096-float16-SiluAndMulFwdKernel-explicit_parallel] | 0.0267 | 1.26 | 3.77 | - | torch 417.1%, torch-compile 100.8% | - |
| 🟡 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-bfloat16-SiluAndMulFwdKernel-explicit_parallel] | 0.0084 | 0.99 | 2.98 | - | torch 375.4%, torch-compile 99.2% | - |
| 🟡 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float32-SiluAndMulFwdKernel-explicit_parallel] | 0.0148 | 0.57 | 3.40 | - | torch 235.0%, torch-compile 98.9% | - |
| 🔵 | sub_bcast | test_broadcast_bench[sub-1024x4096-1x4096-float16-SubFwdOp-sub-normal] | 0.0058 | 0.72 | 2.90 | - | torch 258.0%, torch-compile 102.8% | - |
| 🔵 | sub_bcast | test_broadcast_bench[sub-1024x10240-1x10240-float16-SubFwdOp-sub-normal] | 0.0122 | 0.86 | 3.45 | - | torch 272.9%, torch-compile 100.5% | - |
| 🔵 | sub_bcast | test_broadcast_bench[sub-1024x11008-1x11008-float16-SubFwdOp-sub-normal] | 0.0130 | 0.87 | 3.46 | - | torch 272.0%, torch-compile 100.0% | - |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 9 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 750 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 2587 lines in `ops/`, 39.3% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 3577 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

### Never-built kernels

| File | Executed |
| --- | --- |
| `kernels/attention/deepseek_mla_decode.py` | 5.8% |
| `kernels/attention/gqa_fwd_ws.py` | 6.6% |
| `kernels/attention/gqa_fwd_fp8.py` | 9.8% |
| `kernels/attention/gqa_prefill_fwd_ws.py` | 10.2% |
| `kernels/attention/mha_decode_paged.py` | 11.6% |
| `kernels/attention/gqa_decode_bs1_common.py` | 12.4% |
| `kernels/attention/deepseek_nsa_cmp_fwd.py` | 18.3% |
| `kernels/attention/gqa_prefill_varlen_fwd.py` | 18.7% |
| `kernels/attention/gqa_fwd.py` | 21.4% |

<details>
<summary>Untested pure Python, worst 15 files</summary>

| File | Uncovered | Executed |
| --- | --- | --- |
| `perf/formulas.py` | 708 | 13.1% |
| `ops/attention/gqa.py` | 518 | 38.6% |
| `ops/moe/staged.py` | 137 | 19.9% |
| `ops/pool.py` | 135 | 76.4% |
| `ops/moe/contracts.py` | 134 | 43.5% |
| `ops/convolution.py` | 115 | 75.2% |
| `ops/linear_attention/gated_deltanet.py` | 111 | 73.3% |
| `ops/reduction/reduce.py` | 100 | 58.0% |
| `ops/op_base.py` | 94 | 61.8% |
| `ops/elementwise/_base.py` | 88 | 76.7% |
| `ops/mamba/mamba2_fwd.py` | 86 | 20.4% |
| `ops/rope.py` | 84 | 70.6% |
| `ops/_roofline_codegen.py` | 82 | 68.8% |
| `ops/linear_attention/deltanet.py` | 62 | 64.0% |
| `trace/ui.py` | 62 | 24.4% |

</details>

Per-line detail is in the `htmlcov/` directory of this run's `tileops_op_test` artifact.
