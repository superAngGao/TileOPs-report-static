# ✅ TileOPs Nightly Report

> **2026-08-28 02:52** &ensp;|&ensp; `094ace3` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Correctness** | ✅ &ensp; (516/516 tests across 92 ops) |
| **Benchmarked Ops** | 191 |
| **Benchmark Failures** | ✅ None &ensp;|&ensp; ⚠️ 13 skipped |
| **Regressions** (vs 14-day median) | ✅ None |
| **Baseline Alerts** (< 80%) | ⚠️ 212 |
| **Roofline anomalies** | ✅ None |
| **Never-built kernels** | ⚠️ 9 files &ensp;·&ensp; `kernels/attention/deepseek_mla_decode.py` at 5.8% |
| **Untested roofline math** | 750 lines in `perf/` &ensp;·&ensp; `perf/formulas.py` at 13.1% |
| **Untested op logic** | 2587 lines in `ops/` &ensp;·&ensp; 39.3% of branches taken |
| | <sub>coverage compared against the 2026-08-28 run; no figure means it held</sub> |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 80%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-gate-up-block128-float8_e4m3fn] | 0.1479 | 0.0129 | 8.7% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **SharedFusedMoE** | test_shared_fused_moe_bench[1-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 2.5198 | 0.4268 | 16.9% | vllm |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[gemv-down-m1-block128-float8_e4m3fn] | 0.0448 | 0.0078 | 17.4% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[k-dominant-7168x16384-block128-float8_e4m3fn] | 3.5854 | 0.7893 | 22.0% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[large-spatial-float16] | 4.3443 | 1.0182 | 23.4% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-down-block128-float8_e4m3fn] | 0.0378 | 0.0092 | 24.5% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GemmFwdOp** | test_gemm_bench[mid-m96-gate-up-bfloat16] | 0.0687 | 0.0169 | 24.6% | torch-cublas |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-decode-gate-up-bfloat16] | 0.0677 | 0.0173 | 25.6% | torch-cublas |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-attn-proj-block128-float8_e4m3fn] | 0.7702 | 0.2144 | 27.8% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **Conv3dFwdOp** | test_conv3d_bench[3d-unet-aspp-3x3x3-rate6-float16] | 0.1263 | 0.0376 | 29.8% | torch |

<details>
<summary><strong>202 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-fc-float16] | 0.0061 | 0.0019 | 30.4% | torch-compile |
| 🔴 | **MaxPool1dFwdOp** | test_max_pool1d_bench[textcnn-global-float16] | 0.0134 | 0.0041 | 30.5% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[small-batch-down-m8-per-tensor-float8_e4m3fn] | 0.0266 | 0.0083 | 31.2% | deepgemm |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-bfloat16] | 0.4564 | 0.1430 | 31.3% | fa3 |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b4-dmem1024-d512-float16] | 0.0825 | 0.0259 | 31.4% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-bfloat16] | 0.4553 | 0.1432 | 31.5% | fa3 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-down-block128-float8_e4m3fn] | 0.4463 | 0.1430 | 32.0% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **Conv3dFwdOp** | test_conv3d_bench[unet-encoder-k3-s1-bfloat16] | 0.3538 | 0.1151 | 32.5% | torch-compile |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-stage2-float16] | 0.0107 | 0.0035 | 32.6% | torch-compile |
| 🔴 | **Conv3dFwdOp** | test_conv3d_bench[unet-encoder-k3-s1-bias-bfloat16] | 0.3545 | 0.1226 | 34.6% | torch-compile |
| 🔴 | **MeanPoolingForwardOp** | test_mean_pooling_bench[dense-mainstream] | 0.1351 | 0.0471 | 34.9% | torch-view-mean |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-stage3-float16] | 0.0129 | 0.0046 | 35.6% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-gate-up-block128-float8_e4m3fn] | 0.3858 | 0.1392 | 36.1% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-b64-complex64] | 0.0152 | 0.0056 | 36.8% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[mid-m32-attn-bfloat16] | 0.0661 | 0.0243 | 36.8% | torch-cublas |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[wide-n-24576-block128-float8_e4m3fn] | 1.0276 | 0.3825 | 37.2% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GemmFwdOp** | test_gemm_bench[mid-m16-attn-bfloat16] | 0.0658 | 0.0245 | 37.2% | torch-cublas |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-stage1-float16] | 0.0109 | 0.0041 | 37.7% | torch-compile |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[mha-decode-b32-pv-per-tensor-float8_e4m3fn] | 0.0647 | 0.0249 | 38.6% | flashinfer-bmm-fp8 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-short-bfloat16] | 0.4089 | 0.1588 | 38.8% | fa3 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[gemv-down-m1-per-tensor-float8_e4m3fn] | 0.0259 | 0.0101 | 39.1% | deepgemm |
| 🔴 | **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[textcnn-global-float16] | 0.0193 | 0.0076 | 39.3% | torch-compile |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-short-bfloat16] | 0.4160 | 0.1652 | 39.7% | fa3 |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b1-dmem512-d256-float16] | 0.0329 | 0.0132 | 40.3% | torch-compile |
| 🔴 | **MeanPoolingForwardOp** | test_mean_pooling_bench[dense-batched] | 0.0702 | 0.0286 | 40.7% | torch-view-mean |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-4096-4096-float16-SiluAndMulFwdKernel-direct] | 0.0662 | 0.0269 | 40.7% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-down-per-tensor-float8_e4m3fn] | 0.0253 | 0.0103 | 40.8% | deepgemm |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c128-b64-complex128] | 0.0205 | 0.0085 | 41.4% | torch-cufft |
| 🔴 | **MaximumFwdOp** | test_maximum_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0343 | 0.0142 | 41.5% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-bfloat16] | 1.3112 | 0.5472 | 41.7% | fa3 |
| 🔴 | **MinimumFwdOp** | test_minimum_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0343 | 0.0144 | 41.9% | torch-compile |
| 🔴 | **MinimumFwdOp** | test_minimum_manifest_bench[cnn-feat-broadcast-float16] | 0.0343 | 0.0144 | 42.0% | torch-compile |
| 🔴 | **MaximumFwdOp** | test_maximum_manifest_bench[cnn-feat-broadcast-float16] | 0.0342 | 0.0144 | 42.0% | torch-compile |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-1024-11008-float16-SiluAndMulFwdKernel-direct] | 0.0450 | 0.0191 | 42.4% | torch-compile |
| 🔴 | **MaxPool3dIndicesFwdOp** | test_max_pool3d_indices_bench[c3d-pool1-float16] | 0.3043 | 0.1292 | 42.5% | torch-compile |
| 🔴 | **RopeNeoxPositionIdsFwdOp** | test_rope_neox_position_ids_bench[position-ids-s2k-h32-d128-float16] | 0.0278 | 0.0119 | 42.7% | torch-compile |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[mha-decode-b64-qk-per-tensor-float8_e4m3fn] | 0.1155 | 0.0496 | 42.9% | flashinfer-bmm-fp8 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-prefill-varlen-mixed-fp16] | 0.1404 | 0.0613 | 43.7% | fa3 |
| 🔴 | **SharedFusedMoE** | test_shared_fused_moe_bench[4096-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 32.5280 | 14.6332 | 45.0% | vllm |
| 🔴 | **grouped_gemm_tn** | test_grouped_gemm_bench[tn-batch16-m4096-n4096-k4096-float16] | 0.7802 | 0.3541 | 45.4% | torch |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float16-SiluAndMulFwdKernel-direct] | 0.0178 | 0.0084 | 46.9% | torch-compile |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-405b-p256-float16] | 0.0563 | 0.0265 | 47.1% | fa3 |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-bfloat16-SiluAndMulFwdKernel-direct] | 0.0178 | 0.0084 | 47.2% | torch-compile |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-bfloat16] | 1.2420 | 0.5892 | 47.4% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p256-float16] | 0.1682 | 0.0809 | 48.1% | fa3 |
| 🔴 | **RopeNeoxPositionIdsFwdOp** | test_rope_neox_position_ids_bench[position-ids-s4k-h32-d128-bfloat16] | 0.0456 | 0.0223 | 48.9% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[wide-n-24576-bfloat16] | 0.8988 | 0.4440 | 49.4% | deepgemm |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-small-bfloat16] | 0.0394 | 0.0196 | 49.6% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-bfloat16] | 1.1024 | 0.5479 | 49.7% | fa3 |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-long-k-pressure-float16] | 0.2831 | 0.1409 | 49.8% | marlin-fp16 |
| 🔴 | **GemmFwdOp** | test_gemm_bench[square-1k-nn-bfloat16] | 0.0144 | 0.0072 | 49.8% | torch-cublas |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-down-per-tensor-float8_e4m3fn] | 0.2100 | 0.1052 | 50.1% | deepgemm |
| 🔴 | **GemmFwdOp** | test_gemm_bench[square-1k-nn-float16] | 0.0145 | 0.0073 | 50.2% | torch-cublas |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-70b-prefill-varlen-q-lt-kv-bf16] | 0.1963 | 0.0986 | 50.2% | fa3 |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-2p7b-b2-s32k-dt-bias-float16] | 0.0444 | 0.0223 | 50.3% | mamba |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-dt-bias-bfloat16] | 0.0124 | 0.0064 | 51.7% | mamba |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-gate-up-bfloat16] | 0.3363 | 0.1765 | 52.5% | torch-cublas |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[compile-smoke-rect-128x256x256-float16] | 0.0058 | 0.0031 | 52.8% | torch-dequantized-matmul |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-bfloat16] | 0.0121 | 0.0064 | 53.0% | mamba |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-decode-down-bfloat16] | 0.0246 | 0.0132 | 53.4% | torch-cublas |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-70b-p256-float16] | 0.0685 | 0.0367 | 53.6% | fa3 |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-float16] | 0.0196 | 0.0106 | 54.1% | torch-compile |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-bfloat16] | 0.0195 | 0.0106 | 54.5% | torch-compile |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-non-power2-low-cta-float16] | 0.0744 | 0.0406 | 54.6% | marlin-fp32 |
| 🔴 | **gelu_tanh_and_mul_strategy** | test_fused_gated_strategy_bench[gelu_tanh_and_mul-1024-4096-float16-GeluTanhAndMulFwdKernel-direct] | 0.0178 | 0.0098 | 54.9% | torch-compile |
| 🔴 | **MaxPool3dIndicesFwdOp** | test_max_pool3d_indices_bench[c3d-pool2-float16] | 0.0588 | 0.0326 | 55.4% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-down-bfloat16] | 0.3221 | 0.1793 | 55.7% | deepgemm |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 1.0187 | 0.5767 | 56.6% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-prefill-varlen-uniform-fp16] | 0.1252 | 0.0710 | 56.7% | fa3 |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-medium-bfloat16] | 0.0544 | 0.0316 | 58.0% | torch-compile |
| 🔴 | **gelu_and_mul_strategy** | test_fused_gated_strategy_bench[gelu_and_mul-1024-4096-float16-GeluAndMulFwdKernel-direct] | 0.0182 | 0.0107 | 58.5% | torch-compile |
| 🔴 | **RopeLlama31FwdOp** | test_rope_llama31_bench[llama31-2d-b1-s8k-h32-d128-float16] | 0.0595 | 0.0348 | 58.6% | torch-compile |
| 🔴 | **RopeLongRopeFwdOp** | test_rope_longrope_bench[longrope-2d-b1-s8k-h32-d128-float16] | 0.0595 | 0.0348 | 58.6% | torch-compile |
| 🔴 | **RopeYarnFwdOp** | test_rope_yarn_bench[yarn-2d-b1-s8k-h32-d128-float16] | 0.0594 | 0.0348 | 58.6% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-float16] | 0.2444 | 0.1434 | 58.7% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-float16] | 0.2429 | 0.1435 | 59.1% | fa3 |
| 🔴 | **SharedFusedMoE** | test_shared_fused_moe_bench[2048-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 19.5730 | 11.5943 | 59.2% | vllm |
| 🔴 | **TopkSelectorFwdOp** | test_topk_selector_bench[topk1024-s32k-kv64k-float32] | 15.6282 | 9.2781 | 59.4% | flashinfer |
| 🔴 | **RopeNeoxFwdOp** | test_rope_neox_bench[neox-2d-b2-s2k-h32-d128-float16] | 0.0310 | 0.0184 | 59.5% | torch-compile |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[throughput-8b-p64-float16] | 0.2519 | 0.1507 | 59.8% | flashinfer |
| 🔴 | **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[ecg-cnn-dilated-bfloat16] | 0.0223 | 0.0134 | 60.0% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[k-dominant-7168x16384-bfloat16] | 2.0606 | 1.2581 | 61.1% | deepgemm |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-float16] | 0.9018 | 0.5524 | 61.3% | fa3 |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-float16] | 0.6367 | 0.3907 | 61.4% | fla |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-attn-proj-bfloat16] | 0.5391 | 0.3311 | 61.4% | torch-cublas |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-bfloat16] | 0.6385 | 0.3934 | 61.6% | fla |
| 🔴 | **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[global-1x1-float16] | 0.0133 | 0.0082 | 61.7% | torch-compile |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-float16] | 0.1122 | 0.0693 | 61.8% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-float16] | 0.8928 | 0.5527 | 61.9% | fa3 |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-attn-proj-float16] | 0.5407 | 0.3356 | 62.1% | torch-cublas |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-bfloat16] | 0.1123 | 0.0697 | 62.1% | torch-compile |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-hbm-streaming-threshold-float16] | 0.0607 | 0.0379 | 62.4% | marlin-fp32 |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s896-bfloat16] | 0.0454 | 0.0284 | 62.5% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s896-float16] | 0.0453 | 0.0284 | 62.6% | fa3 |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[compile-smoke-square-64x64x128-float16] | 0.0043 | 0.0027 | 62.9% | torch-dequantized-matmul |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b8-dmem512-d256-bfloat16] | 0.0334 | 0.0211 | 63.1% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[mid-m64-down-bfloat16] | 0.0206 | 0.0132 | 63.7% | torch-cublas |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-float16] | 1.4256 | 0.9200 | 64.5% | fla |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-float32] | 0.0195 | 0.0127 | 64.9% | torch-compile |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-bfloat16] | 1.4673 | 0.9534 | 65.0% | fla |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-bfloat16] | 0.3162 | 0.2055 | 65.0% | fla |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-float16] | 0.3142 | 0.2050 | 65.3% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-float16] | 0.3809 | 0.2496 | 65.5% | fla |
| 🔴 | **TopkSelectorFwdOp** | test_topk_selector_bench[topk2048-s32k-kv64k-float32] | 16.2340 | 10.6717 | 65.7% | flashinfer |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-float16] | 0.2017 | 0.1337 | 66.3% | fla |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-l2-resident-ish-float16] | 0.0329 | 0.0219 | 66.4% | marlin-fp16 |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s1792-float16] | 0.1290 | 0.0858 | 66.5% | fa3 |
| 🔴 | **GroupNormFwdOp** | test_group_norm_bench[wider-channel-g32-affine-float16] | 0.0060 | 0.0040 | 66.7% | flaggems |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-float32] | 0.1077 | 0.0719 | 66.7% | torch-compile |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-bfloat16] | 0.3874 | 0.2584 | 66.7% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-bfloat16] | 0.7509 | 0.5021 | 66.9% | fla |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-unbatched-complex64] | 0.0081 | 0.0054 | 66.9% | torch-cufft |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s1792-bfloat16] | 0.1287 | 0.0862 | 67.0% | fa3 |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-float16] | 0.7250 | 0.4863 | 67.1% | fla |
| 🔴 | **GroupNormFwdOp** | test_group_norm_bench[tail-spatial-g16-affine-float16] | 0.0060 | 0.0041 | 67.2% | flaggems |
| 🔴 | **GroupNormFwdOp** | test_group_norm_no_affine_bench[tail-spatial-g16-float16] | 0.0052 | 0.0035 | 67.5% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-bfloat16] | 0.0973 | 0.0658 | 67.6% | fla |
| 🔴 | **AvgPool1dFwdOp** | test_avg_pool1d_bench[audio-downsample-float16] | 0.0062 | 0.0042 | 67.9% | torch-compile |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-bfloat16] | 0.2049 | 0.1401 | 68.4% | fla |
| 🔴 | **LtFwdOp** | test_lt_manifest_bench[cnn-feat-broadcast-float16] | 0.0172 | 0.0118 | 68.7% | torch-compile |
| 🔴 | **GeFwdOp** | test_ge_manifest_bench[cnn-feat-broadcast-float16] | 0.0172 | 0.0118 | 68.8% | torch-compile |
| 🔴 | **LeFwdOp** | test_le_manifest_bench[cnn-feat-broadcast-float16] | 0.0173 | 0.0119 | 68.8% | torch-compile |
| 🔴 | **FusedAddRMSNormFwdOp** | test_fused_add_rms_norm_bench[llama-405b-decode-bfloat16] | 0.0063 | 0.0043 | 68.9% | flashinfer |
| 🔴 | **LeFwdOp** | test_le_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0172 | 0.0119 | 69.0% | torch-compile |
| 🔴 | **NeFwdOp** | test_ne_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0172 | 0.0118 | 69.0% | torch-compile |
| 🔴 | **EqFwdOp** | test_eq_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0173 | 0.0120 | 69.2% | torch-compile |
| 🔴 | **LogicalOrFwdOp** | test_logical_or_manifest_bench[cnn-feat-broadcast-float16] | 0.0174 | 0.0121 | 69.2% | torch-compile |
| 🔴 | **GtFwdOp** | test_gt_manifest_bench[cnn-feat-broadcast-float16] | 0.0172 | 0.0119 | 69.2% | torch-compile |
| 🔴 | **NeFwdOp** | test_ne_manifest_bench[cnn-feat-broadcast-float16] | 0.0172 | 0.0119 | 69.3% | torch-compile |
| 🔴 | **EqFwdOp** | test_eq_manifest_bench[cnn-feat-broadcast-float16] | 0.0172 | 0.0119 | 69.3% | torch-compile |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[moe-prefill-b128-per-tensor-float8_e4m3fn] | 0.9008 | 0.6249 | 69.4% | flashinfer-bmm-fp8 |
| 🔴 | **GtFwdOp** | test_gt_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0172 | 0.0120 | 69.4% | torch-compile |
| 🔴 | **LogicalAndFwdOp** | test_logical_and_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0172 | 0.0120 | 69.7% | torch-compile |
| 🔴 | **LogicalOrFwdOp** | test_logical_or_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0174 | 0.0122 | 69.7% | torch-compile |
| 🔴 | **GeFwdOp** | test_ge_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0172 | 0.0120 | 69.9% | torch-compile |
| 🔴 | **LogicalAndFwdOp** | test_logical_and_manifest_bench[cnn-feat-broadcast-float16] | 0.0172 | 0.0121 | 70.5% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-bfloat16] | 0.3115 | 0.2200 | 70.6% | fla |
| 🔴 | **LtFwdOp** | test_lt_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0172 | 0.0122 | 70.7% | torch-compile |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s3584-bfloat16] | 0.7490 | 0.5296 | 70.7% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s3584-float16] | 0.7489 | 0.5298 | 70.7% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s7168-bfloat16] | 2.8526 | 2.0221 | 70.9% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-softcap50-float16] | 0.1766 | 0.1252 | 70.9% | flashinfer |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s7168-float16] | 2.8482 | 2.0241 | 71.1% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-float16] | 0.8320 | 0.5924 | 71.2% | fa3 |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s16k-h4-d64-float16] | 1.5163 | 1.0817 | 71.3% | fla |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-float16] | 0.0984 | 0.0702 | 71.4% | fla |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.8085 | 0.5801 | 71.7% | fa3 |
| 🔴 | **MaxPool2dFwdOp** | test_max_pool2d_bench[resnet-stem-bfloat16] | 0.0472 | 0.0340 | 72.0% | torch-compile |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-float16] | 0.1487 | 0.1077 | 72.4% | fla |
| 🔴 | **GroupNormFwdOp** | test_group_norm_no_affine_bench[wider-channel-g32-float16] | 0.0048 | 0.0035 | 72.4% | flaggems |
| 🔴 | **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[nondiv-7x7-bfloat16] | 0.0158 | 0.0115 | 72.5% | torch-ref |
| 🔴 | **MaxPool2dFwdOp** | test_max_pool2d_bench[resnet-stem-float16] | 0.0471 | 0.0342 | 72.5% | torch-compile |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0567 | 0.0412 | 72.6% | flashinfer |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-float16] | 0.0570 | 0.0414 | 72.7% | flashinfer |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float32-SiluAndMulFwdKernel-direct] | 0.0201 | 0.0146 | 72.7% | torch-compile |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-2k-bfloat16] | 0.2800 | 0.2047 | 73.1% | torch-cublas |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[alexnet-ceil-bfloat16] | 0.0237 | 0.0174 | 73.5% | torch-compile |
| 🔴 | **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[sincnet-speaker-local-float16] | 0.0218 | 0.0160 | 73.6% | torch-compile |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-2k-float16] | 0.2833 | 0.2089 | 73.7% | torch-cublas |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-bfloat16] | 0.6110 | 0.4522 | 74.0% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-float16] | 0.0931 | 0.0690 | 74.1% | flashinfer |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b4-4k-bfloat16] | 1.0429 | 0.7726 | 74.1% | torch-cublas |
| 🔴 | **BmmFwdOp** | test_bmm_bench[moe-prefill-b128-bfloat16] | 0.2910 | 0.2156 | 74.1% | torch-cublas |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[alexnet-ceil-float16] | 0.0237 | 0.0177 | 74.5% | torch-compile |
| 🔴 | **CountNonzeroFwdOp** | test_count_nonzero_bench[3d-multidim-reduce-float16] | 0.0064 | 0.0048 | 74.5% | torch-compile |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-bfloat16] | 0.0928 | 0.0692 | 74.6% | flashinfer |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s16k-h4-d64-bfloat16] | 1.4503 | 1.0812 | 74.6% | fla |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s8k-h4-d64-float16] | 0.7452 | 0.5570 | 74.8% | fla |
| 🔴 | **Conv2dFwdOp** | test_conv2d_bench[highres-3x3-s1-bias-float16] | 0.1049 | 0.0787 | 75.0% | torch-compile |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-bfloat16] | 0.1444 | 0.1082 | 75.0% | fla |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-float16] | 0.1668 | 0.1252 | 75.0% | flashinfer |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-float16] | 0.6173 | 0.4654 | 75.4% | fla |
| 🔴 | **Conv2dFwdOp** | test_conv2d_bench[highres-3x3-s1-float16] | 0.1047 | 0.0791 | 75.5% | torch-compile |
| 🔴 | **RopeNonNeoxFwdOp** | test_rope_non_neox_bench[non-neox-2d-b2-s2k-h32-d128-bfloat16] | 0.0252 | 0.0190 | 75.6% | torch-compile |
| 🔴 | **Conv3dFwdOp** | test_conv3d_bench[video-stage-downsample-k3-s2-float16] | 0.0349 | 0.0264 | 75.6% | torch |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s4k-h4-d64-bfloat16] | 0.1564 | 0.1195 | 76.4% | fla |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-1k-bfloat16] | 0.0407 | 0.0311 | 76.5% | torch-cublas |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-1k-float16] | 0.0407 | 0.0312 | 76.5% | torch-cublas |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s8k-h4-d64-bfloat16] | 0.7265 | 0.5576 | 76.8% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.3497 | 0.2708 | 77.5% | fa3 |
| 🔴 | **DeltaNetFwdOp** | test_deltanet_vs_fla_fwd[dn-b2-s16k-h4-d64-float16] | 0.4728 | 0.3663 | 77.5% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-float16] | 0.6693 | 0.5194 | 77.6% | flashinfer |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-float16] | 0.0866 | 0.0672 | 77.6% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-float16] | 0.3512 | 0.2727 | 77.6% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.6661 | 0.5180 | 77.8% | flashinfer |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-bfloat16] | 0.0866 | 0.0675 | 77.9% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowFwdOp** | test_gqa_sliding_window_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.1517 | 0.1184 | 78.0% | fa3 |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s4k-h4-d64-float16] | 0.3691 | 0.2882 | 78.1% | fla |
| 🔴 | **GatedDeltaNetPrefillBHTDFwdOp** | test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-float16] | 0.2509 | 0.1962 | 78.2% | fla |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0043 | 0.0033 | 78.2% | mamba |
| 🔴 | **GroupedQueryAttentionSlidingWindowFwdOp** | test_gqa_sliding_window_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.1513 | 0.1184 | 78.2% | fa3 |
| 🔴 | **GatedDeltaNetPrefillBHTDFwdOp** | test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-bfloat16] | 0.2525 | 0.1976 | 78.3% | fla |
| 🔴 | **DeltaNetFwdOp** | test_deltanet_vs_fla_fwd[dn-b2-s16k-h4-d64-bfloat16] | 0.4728 | 0.3702 | 78.3% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowFwdOp** | test_gqa_sliding_window_fwd_bench[llama-70b-long-w1024-float16] | 0.1525 | 0.1195 | 78.4% | fa3 |
| 🔴 | **Conv2dFwdOp** | test_conv2d_bench[classifier-1x1-float16] | 0.0092 | 0.0072 | 78.7% | torch-compile |
| 🔴 | **GroupedQueryAttentionSlidingWindowFwdOp** | test_gqa_sliding_window_fwd_bench[llama-8b-long-w1024-float16] | 0.1531 | 0.1204 | 78.7% | fa3 |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s4k-h4-d64-bfloat16] | 0.3649 | 0.2877 | 78.9% | fla |
| 🔴 | **grouped_gemm_nn** | test_grouped_gemm_bench[nn-batch16-m4096-n4096-k4096-float16] | 0.3400 | 0.2692 | 79.2% | torch |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-float16] | 0.3128 | 0.2477 | 79.2% | fla |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-large-bfloat16] | 0.0716 | 0.0568 | 79.3% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s4k-h4-d64-float16] | 0.1569 | 0.1254 | 80.0% | fla |
| 🔴 | **Conv3dFwdOp** | test_conv3d_bench[video-stage-downsample-k3-s2-bias-float16] | 0.0353 | 0.0282 | 80.0% | torch-compile |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 9 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 750 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 2587 lines in `ops/`, 39.3% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 3590 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

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
