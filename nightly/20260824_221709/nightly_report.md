# ❌ TileOPs Nightly Report

> **2026-08-24 19:43** &ensp;|&ensp; `b473fac` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Correctness** | ✅ &ensp; (513/513 tests across 92 ops) |
| **Benchmarked Ops** | 191 |
| **Benchmark Failures** | ✅ None &ensp;|&ensp; ⚠️ 13 skipped |
| **Regressions** (vs 14-day best) | ⚠️ 3 |
| **Baseline Alerts** (< 80%) | ⚠️ 233 |
| **Improvements** (vs 14-day best) | 🎉 49 |
| **Never-built kernels** | ⚠️ 9 files &ensp;·&ensp; `kernels/attention/deepseek_mla_decode.py` at 5.8% |
| **Untested roofline math** | 735 lines in `perf/` &ensp;·&ensp; `perf/formulas.py` at 13.1% |
| **Untested op logic** | 2164 lines in `ops/` &ensp;·&ensp; 43.5% of branches taken |
| | <sub>coverage compared against the 2026-08-23 run; no figure means it held</sub> |

## ⚠️ Performance Regressions (vs 14-day best)

| Op | Config | Best (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|----------:|-----------:|------:|-------:|
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[lightning-indexer-s8k-h32-d64-bfloat16] | 0.1626 | 0.6174 | +279.8% | 55.65 |
| **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-4096-4096-float16-SiluAndMulFwdKernel-direct] | 0.0661 | 0.0822 | +24.4% | 0.41 |
| **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-1024-11008-float16-SiluAndMulFwdKernel-direct] | 0.0450 | 0.0555 | +23.5% | 0.41 |

## 🎉 Performance Improvements (vs 14-day best)

| Op | Config | Prev Best (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|---------------:|-----------:|------:|-------:|
| **CumprodFwdOp** | test_cumprod_bench[long-seq-scan-bfloat16] | 0.2500 | 0.0070 | -97.2% | 0.30 |
| **ProdFwdOp** | test_prod_bench[hidden-state-reduce-bfloat16] | 0.0996 | 0.0075 | -92.5% | 1.12 |
| **ProdFwdOp** | test_prod_bench[hidden-state-reduce-float16] | 0.0986 | 0.0079 | -92.0% | 1.07 |
| **SumFwdOp** | test_sum_bench[hidden-state-reduce-dim0-bfloat16] | 0.0685 | 0.0121 | -82.3% | 0.69 |
| **InfNormFwdOp** | test_inf_norm_bench[long-seq-inf-bfloat16] | 0.0169 | 0.0040 | -76.1% | 1.04 |
| **CumsumFwdOp** | test_cumsum_bench[long-seq-scan-bfloat16] | 0.0294 | 0.0070 | -76.0% | 0.30 |
| **ProdFwdOp** | test_prod_bench[long-seq-reduce-bfloat16] | 0.0172 | 0.0043 | -75.1% | 0.49 |
| **CumprodFwdOp** | test_cumprod_bench[hidden-state-scan-bfloat16] | 0.0435 | 0.0109 | -74.9% | 0.77 |
| **CumsumFwdOp** | test_cumsum_bench[hidden-state-scan-bfloat16] | 0.0434 | 0.0109 | -74.9% | 0.77 |
| **InfNormFwdOp** | test_inf_norm_bench[hidden-state-inf-bfloat16] | 0.0291 | 0.0074 | -74.7% | 2.28 |
| **InfNormFwdOp** | test_inf_norm_bench[hidden-state-inf-float16] | 0.0289 | 0.0073 | -74.6% | 2.29 |
| **ArgmaxFwdOp** | test_argmax_bench[lm-head-argmax-float16] | 0.0151 | 0.0039 | -74.3% | 0.11 |
| **CumprodFwdOp** | test_cumprod_bench[hidden-state-scan-float16] | 0.0442 | 0.0115 | -74.0% | 0.73 |
| **CumsumFwdOp** | test_cumsum_bench[hidden-state-scan-float16] | 0.0442 | 0.0115 | -74.0% | 0.73 |
| **ArgmaxFwdOp** | test_argmax_bench[lm-head-argmax-bfloat16] | 0.0153 | 0.0040 | -74.0% | 0.10 |
| **ArgminFwdOp** | test_argmin_bench[lm-head-argmin-float16] | 0.0150 | 0.0040 | -73.4% | 0.10 |
| **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-gate-up-block128-float8_e4m3fn] | 1.3345 | 0.3870 | -71.0% | 320.45 |
| **ArgmaxFwdOp** | test_argmax_bench[hidden-state-argmax-float16] | 0.0239 | 0.0092 | -61.7% | 0.92 |
| **ArgmaxFwdOp** | test_argmax_bench[hidden-state-argmax-bfloat16] | 0.0239 | 0.0096 | -59.8% | 0.87 |
| **ArgminFwdOp** | test_argmin_bench[hidden-state-argmin-float16] | 0.0239 | 0.0096 | -59.7% | 0.87 |
| **ArgminFwdOp** | test_argmin_bench[hidden-state-argmin-bfloat16] | 0.0239 | 0.0099 | -58.8% | 0.85 |
| **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-gate-up-block128-float8_e4m3fn] | 0.3334 | 0.1481 | -55.6% | 26.17 |
| **AllFwdOp** | test_all_bench[3d-multidim-reduce-bool] | 0.0213 | 0.0111 | -48.0% | 0.19 |
| **InfNormFwdOp** | test_inf_norm_bench[3d-multidim-reduce-float16] | 0.0215 | 0.0112 | -47.8% | 0.37 |
| **BitwiseNotFwdOp** | test_bitwise_not_bench[elementwise-256M-int32] | 0.9374 | 0.4986 | -46.8% | 0.54 |
| **BitwiseNotFwdOp** | test_bitwise_not_bench[elementwise-16M-int32] | 0.0605 | 0.0340 | -43.8% | 0.49 |
| **MishFwdOp** | test_mish_manifest_bench[yolo-p3-float16] | 0.0709 | 0.0403 | -43.2% | 2.60 |
| **MishFwdOp** | test_mish_manifest_bench[yolo-p3-bfloat16] | 0.0706 | 0.0405 | -42.6% | 2.59 |
| **MishFwdOp** | test_mish_manifest_bench[yolo-p4-float16] | 0.0370 | 0.0214 | -42.0% | 2.45 |
| **MishFwdOp** | test_mish_manifest_bench[yolo-p4-bfloat16] | 0.0368 | 0.0216 | -41.2% | 2.42 |
| **Log1pFwdOp** | test_log1p_bench[elementwise-256M-bfloat16] | 0.4327 | 0.2549 | -41.1% | 2.11 |
| **LogFwdOp** | test_log_bench[elementwise-256M-bfloat16] | 0.4279 | 0.2544 | -40.5% | 1.06 |
| **Log1pFwdOp** | test_log1p_bench[elementwise-256M-float16] | 0.4147 | 0.2542 | -38.7% | 2.11 |
| **Log1pFwdOp** | test_log1p_bench[elementwise-16M-bfloat16] | 0.0292 | 0.0181 | -37.9% | 1.85 |
| **LogFwdOp** | test_log_bench[elementwise-256M-float16] | 0.4069 | 0.2534 | -37.7% | 1.06 |
| **LogFwdOp** | test_log_bench[elementwise-16M-bfloat16] | 0.0289 | 0.0181 | -37.4% | 0.93 |
| **SoftplusFwdOp** | test_softplus_manifest_bench[mlp-hidden-wide-float16] | 0.0364 | 0.0228 | -37.2% | 3.67 |
| **SoftplusFwdOp** | test_softplus_manifest_bench[mlp-hidden-wide-bfloat16] | 0.0366 | 0.0233 | -36.4% | 3.61 |
| **Log1pFwdOp** | test_log1p_bench[elementwise-16M-float16] | 0.0282 | 0.0181 | -35.6% | 1.85 |
| **IsinfFwdOp** | test_isinf_bench[elementwise-256M-float16] | 0.2761 | 0.1862 | -32.6% | 1.44 |
| **IsinfFwdOp** | test_isinf_bench[elementwise-256M-bfloat16] | 0.2750 | 0.1857 | -32.5% | 1.45 |
| **IsfiniteFwdOp** | test_isfinite_bench[elementwise-256M-bfloat16] | 0.2729 | 0.1862 | -31.8% | 1.44 |
| **IsfiniteFwdOp** | test_isfinite_bench[elementwise-256M-float16] | 0.2729 | 0.1862 | -31.8% | 1.44 |
| **IsnanFwdOp** | test_isnan_bench[elementwise-256M-bfloat16] | 0.2730 | 0.1863 | -31.7% | 1.44 |
| **IsnanFwdOp** | test_isnan_bench[elementwise-256M-float16] | 0.2730 | 0.1863 | -31.7% | 1.44 |
| **GemmFp8FwdOp** | test_gemm_fp8_bench[gemv-down-m1-block128-float8_e4m3fn] | 0.0627 | 0.0446 | -28.9% | 0.66 |
| **SigmoidFwdOp** | test_sigmoid_manifest_bench[elementwise-256M-float16] | 0.4243 | 0.3018 | -28.9% | 3.56 |
| **SiluFwdOp** | test_silu_manifest_bench[llama-8b-ffn-prefill-float16] | 0.0504 | 0.0366 | -27.4% | 4.01 |
| **SigmoidFwdOp** | test_sigmoid_manifest_bench[elementwise-256M-bfloat16] | 0.3673 | 0.3084 | -16.0% | 3.48 |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 80%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-gate-up-block128-float8_e4m3fn] | 0.1481 | 0.0129 | 8.7% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **SharedFusedMoE** | test_shared_fused_moe_bench[1-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 2.5280 | 0.4262 | 16.9% | vllm |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[gemv-down-m1-block128-float8_e4m3fn] | 0.0446 | 0.0078 | 17.4% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[k-dominant-7168x16384-block128-float8_e4m3fn] | 3.5879 | 0.7726 | 21.5% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[large-spatial-float16] | 4.3442 | 1.0184 | 23.4% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-down-block128-float8_e4m3fn] | 0.0377 | 0.0092 | 24.5% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GemmFwdOp** | test_gemm_bench[mid-m96-gate-up-bfloat16] | 0.0687 | 0.0169 | 24.6% | torch-cublas |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-decode-gate-up-bfloat16] | 0.0678 | 0.0172 | 25.4% | torch-cublas |
| 🔴 | **MaxPool1dFwdOp** | test_max_pool1d_bench[textcnn-global-float16] | 0.0134 | 0.0037 | 27.6% | torch-compile |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c128-b64-complex128] | 0.0305 | 0.0085 | 27.8% | torch-cufft |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-attn-proj-block128-float8_e4m3fn] | 0.7704 | 0.2147 | 27.9% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[lm-head-logits-float32] | 0.0348 | 0.0098 | 28.1% | torch-compile |
| 🔴 | **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[textcnn-global-float16] | 0.0193 | 0.0057 | 29.5% | torch-compile |
| 🔴 | **Conv3dFwdOp** | test_conv3d_bench[3d-unet-aspp-3x3x3-rate6-float16] | 0.1269 | 0.0376 | 29.6% | torch-compile |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-fc-float16] | 0.0061 | 0.0018 | 29.8% | torch-compile |
| 🔴 | **LogSoftmaxFwdOp** | test_log_softmax_bench[lm-head-logits-float32] | 0.0319 | 0.0098 | 30.8% | torch-compile |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-stage2-float16] | 0.0107 | 0.0033 | 30.8% | torch-compile |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[lm-head-logits-bfloat16] | 0.0308 | 0.0095 | 30.9% | torch-compile |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b4-dmem1024-d512-float16] | 0.0827 | 0.0256 | 31.0% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[small-batch-down-m8-per-tensor-float8_e4m3fn] | 0.0267 | 0.0083 | 31.1% | deepgemm |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-bfloat16] | 0.4565 | 0.1431 | 31.3% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-bfloat16] | 0.4562 | 0.1433 | 31.4% | fa3 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-down-block128-float8_e4m3fn] | 0.4457 | 0.1431 | 32.1% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **Conv3dFwdOp** | test_conv3d_bench[unet-encoder-k3-s1-bfloat16] | 0.3542 | 0.1153 | 32.5% | torch |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-4096-4096-float16-SiluAndMulFwdKernel-direct] | 0.0822 | 0.0269 | 32.7% | torch-compile |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[lm-head-logits-float16] | 0.0284 | 0.0095 | 33.5% | torch-compile |
| 🔴 | **AnyFwdOp** | test_any_bench[3d-multidim-reduce-bool] | 0.0111 | 0.0037 | 33.5% | torch-compile |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-1024-11008-float16-SiluAndMulFwdKernel-direct] | 0.0555 | 0.0190 | 34.3% | torch-compile |
| 🔴 | **LogSoftmaxFwdOp** | test_log_softmax_bench[lm-head-logits-bfloat16] | 0.0262 | 0.0090 | 34.4% | torch-compile |
| 🔴 | **Conv3dFwdOp** | test_conv3d_bench[unet-encoder-k3-s1-bias-bfloat16] | 0.3536 | 0.1224 | 34.6% | torch-compile |
| 🔴 | **MeanPoolingForwardOp** | test_mean_pooling_bench[dense-mainstream] | 0.1352 | 0.0470 | 34.8% | torch-view-mean |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-stage3-float16] | 0.0129 | 0.0046 | 35.5% | torch-compile |
| 🔴 | **MaximumFwdOp** | test_maximum_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0392 | 0.0142 | 36.1% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-gate-up-block128-float8_e4m3fn] | 0.3870 | 0.1408 | 36.4% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **LogSoftmaxFwdOp** | test_log_softmax_bench[lm-head-logits-float16] | 0.0249 | 0.0091 | 36.4% | torch-compile |
| 🔴 | **MinimumFwdOp** | test_minimum_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0392 | 0.0144 | 36.7% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[mid-m32-attn-bfloat16] | 0.0662 | 0.0243 | 36.7% | torch-cublas |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-b64-complex64] | 0.0152 | 0.0056 | 37.0% | torch-cufft |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-2p7b-b2-s32k-dt-bias-float16] | 0.0599 | 0.0223 | 37.2% | mamba |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[wide-n-24576-block128-float8_e4m3fn] | 1.0266 | 0.3822 | 37.2% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GemmFwdOp** | test_gemm_bench[mid-m16-attn-bfloat16] | 0.0658 | 0.0245 | 37.3% | torch-cublas |
| 🔴 | **MaximumFwdOp** | test_maximum_manifest_bench[cnn-feat-broadcast-float16] | 0.0374 | 0.0143 | 38.3% | torch-compile |
| 🔴 | **MinimumFwdOp** | test_minimum_manifest_bench[cnn-feat-broadcast-float16] | 0.0374 | 0.0144 | 38.4% | torch-compile |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[mha-decode-b32-pv-per-tensor-float8_e4m3fn] | 0.0647 | 0.0249 | 38.5% | flashinfer-bmm-fp8 |
| 🔴 | **AllFwdOp** | test_all_bench[3d-multidim-reduce-bool] | 0.0111 | 0.0043 | 38.5% | torch-compile |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float16-SiluAndMulFwdKernel-direct] | 0.0216 | 0.0084 | 38.6% | torch-compile |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-short-bfloat16] | 0.4092 | 0.1588 | 38.8% | fa3 |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-bfloat16-SiluAndMulFwdKernel-direct] | 0.0216 | 0.0084 | 38.9% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[gemv-down-m1-per-tensor-float8_e4m3fn] | 0.0258 | 0.0101 | 39.2% | deepgemm |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-short-bfloat16] | 0.4154 | 0.1654 | 39.8% | fa3 |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b1-dmem512-d256-float16] | 0.0330 | 0.0133 | 40.3% | torch-compile |
| 🔴 | **SumFwdOp** | test_sum_bench[3d-multidim-reduce-float16] | 0.0113 | 0.0046 | 40.5% | torch-compile |
| 🔴 | **MeanPoolingForwardOp** | test_mean_pooling_bench[dense-batched] | 0.0702 | 0.0286 | 40.7% | torch-view-mean |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-down-per-tensor-float8_e4m3fn] | 0.0253 | 0.0104 | 40.9% | deepgemm |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-stage1-float16] | 0.0109 | 0.0045 | 40.9% | torch-compile |
| 🔴 | **L2NormFwdOp** | test_l2_norm_bench[3d-multidim-reduce-float16] | 0.0113 | 0.0046 | 41.0% | torch-compile |
| 🔴 | **CountNonzeroFwdOp** | test_count_nonzero_bench[3d-multidim-reduce-float16] | 0.0116 | 0.0048 | 41.1% | torch-compile |
| 🔴 | **L1NormFwdOp** | test_l1_norm_bench[3d-multidim-reduce-float16] | 0.0113 | 0.0046 | 41.2% | torch-compile |
| 🔴 | **MeanFwdOp** | test_mean_bench[3d-multidim-reduce-float16] | 0.0113 | 0.0047 | 41.4% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-bfloat16] | 1.3118 | 0.5471 | 41.7% | fa3 |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-bfloat16] | 0.0154 | 0.0064 | 41.8% | mamba |
| 🔴 | **MaxPool3dIndicesFwdOp** | test_max_pool3d_indices_bench[c3d-pool1-float16] | 0.3044 | 0.1294 | 42.5% | torch-compile |
| 🔴 | **RopeNeoxPositionIdsFwdOp** | test_rope_neox_position_ids_bench[position-ids-s2k-h32-d128-float16] | 0.0278 | 0.0119 | 42.6% | torch-compile |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-dt-bias-bfloat16] | 0.0148 | 0.0064 | 42.9% | mamba |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[mha-decode-b64-qk-per-tensor-float8_e4m3fn] | 0.1154 | 0.0497 | 43.1% | flashinfer-bmm-fp8 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-prefill-varlen-mixed-fp16] | 0.1405 | 0.0614 | 43.7% | fa3 |
| 🔴 | **InfNormFwdOp** | test_inf_norm_bench[3d-multidim-reduce-float16] | 0.0112 | 0.0049 | 43.9% | torch-compile |
| 🔴 | **AminFwdOp** | test_amin_bench[3d-multidim-reduce-float16] | 0.0113 | 0.0050 | 43.9% | torch-compile |
| 🔴 | **AmaxFwdOp** | test_amax_bench[3d-multidim-reduce-float16] | 0.0113 | 0.0050 | 43.9% | torch-compile |
| 🔴 | **SharedFusedMoE** | test_shared_fused_moe_bench[4096-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 32.5463 | 14.6270 | 44.9% | vllm |
| 🔴 | **grouped_gemm_tn** | test_grouped_gemm_bench[tn-batch16-m4096-n4096-k4096-float16] | 0.7820 | 0.3525 | 45.1% | torch |
| 🔴 | **gelu_tanh_and_mul_strategy** | test_fused_gated_strategy_bench[gelu_tanh_and_mul-1024-4096-float16-GeluTanhAndMulFwdKernel-direct] | 0.0216 | 0.0098 | 45.1% | torch-compile |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-405b-p256-float16] | 0.0563 | 0.0266 | 47.1% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-bfloat16] | 1.2427 | 0.5891 | 47.4% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p256-float16] | 0.1683 | 0.0812 | 48.3% | fa3 |
| 🔴 | **RopeNeoxPositionIdsFwdOp** | test_rope_neox_position_ids_bench[position-ids-s4k-h32-d128-bfloat16] | 0.0457 | 0.0222 | 48.6% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[wide-n-24576-bfloat16] | 0.9017 | 0.4419 | 49.0% | deepgemm |
| 🔴 | **gelu_and_mul_strategy** | test_fused_gated_strategy_bench[gelu_and_mul-1024-4096-float16-GeluAndMulFwdKernel-direct] | 0.0216 | 0.0107 | 49.3% | torch-compile |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-long-k-pressure-float16] | 0.2834 | 0.1408 | 49.7% | marlin-fp16 |
| 🔴 | **GemmFwdOp** | test_gemm_bench[square-1k-nn-bfloat16] | 0.0145 | 0.0072 | 49.8% | torch-cublas |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-small-bfloat16] | 0.0395 | 0.0197 | 49.8% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-bfloat16] | 1.1015 | 0.5495 | 49.9% | fa3 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-down-per-tensor-float8_e4m3fn] | 0.2109 | 0.1056 | 50.1% | deepgemm |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-70b-prefill-varlen-q-lt-kv-bf16] | 0.1963 | 0.0985 | 50.2% | fa3 |
| 🔴 | **GemmFwdOp** | test_gemm_bench[square-1k-nn-float16] | 0.0145 | 0.0073 | 50.2% | torch-cublas |
| 🔴 | **VarFwdOp** | test_var_bench[3d-multidim-reduce-float16] | 0.0120 | 0.0060 | 50.4% | torch-compile |
| 🔴 | **StdFwdOp** | test_std_bench[3d-multidim-reduce-float16] | 0.0121 | 0.0063 | 52.2% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-gate-up-bfloat16] | 0.3370 | 0.1766 | 52.4% | torch-cublas |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[compile-smoke-rect-128x256x256-float16] | 0.0059 | 0.0031 | 52.5% | torch-dequantized-matmul |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-decode-down-bfloat16] | 0.0246 | 0.0132 | 53.6% | torch-cublas |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-70b-p256-float16] | 0.0685 | 0.0368 | 53.8% | fa3 |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-float16] | 0.0196 | 0.0107 | 54.2% | torch-compile |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-non-power2-low-cta-float16] | 0.0745 | 0.0406 | 54.5% | marlin-fp16 |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-bfloat16] | 0.0195 | 0.0106 | 54.6% | torch-compile |
| 🔴 | **MaxPool3dIndicesFwdOp** | test_max_pool3d_indices_bench[c3d-pool2-float16] | 0.0588 | 0.0327 | 55.6% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-down-bfloat16] | 0.3214 | 0.1798 | 55.9% | deepgemm |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 1.0192 | 0.5770 | 56.6% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-prefill-varlen-uniform-fp16] | 0.1251 | 0.0715 | 57.1% | fa3 |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-medium-bfloat16] | 0.0544 | 0.0314 | 57.7% | torch-compile |
| 🔴 | **RopeYarnFwdOp** | test_rope_yarn_bench[yarn-2d-b1-s8k-h32-d128-float16] | 0.0595 | 0.0349 | 58.6% | torch-compile |
| 🔴 | **RopeLongRopeFwdOp** | test_rope_longrope_bench[longrope-2d-b1-s8k-h32-d128-float16] | 0.0595 | 0.0349 | 58.6% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-float16] | 0.2444 | 0.1433 | 58.6% | fa3 |
| 🔴 | **RopeLlama31FwdOp** | test_rope_llama31_bench[llama31-2d-b1-s8k-h32-d128-float16] | 0.0594 | 0.0349 | 58.8% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-float16] | 0.2435 | 0.1435 | 59.0% | fa3 |
| 🔴 | **SharedFusedMoE** | test_shared_fused_moe_bench[2048-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 19.5743 | 11.6008 | 59.3% | vllm |
| 🔴 | **TopkSelectorFwdOp** | test_topk_selector_bench[topk1024-s32k-kv64k-float32] | 15.6297 | 9.2719 | 59.3% | flashinfer |
| 🔴 | **RopeNeoxFwdOp** | test_rope_neox_bench[neox-2d-b2-s2k-h32-d128-float16] | 0.0308 | 0.0184 | 59.8% | torch-compile |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[throughput-8b-p64-float16] | 0.2518 | 0.1507 | 59.9% | flashinfer |
| 🔴 | **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[ecg-cnn-dilated-bfloat16] | 0.0223 | 0.0134 | 60.0% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-float16] | 0.9026 | 0.5513 | 61.1% | fa3 |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-attn-proj-bfloat16] | 0.5398 | 0.3301 | 61.2% | deepgemm |
| 🔴 | **GemmFwdOp** | test_gemm_bench[k-dominant-7168x16384-bfloat16] | 2.0598 | 1.2622 | 61.3% | deepgemm |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-float16] | 0.1126 | 0.0691 | 61.3% | torch-compile |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-float16] | 0.6363 | 0.3908 | 61.4% | fla |
| 🔴 | **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[global-1x1-float16] | 0.0133 | 0.0082 | 61.5% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-float16] | 0.8926 | 0.5515 | 61.8% | fa3 |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-bfloat16] | 0.6370 | 0.3936 | 61.8% | fla |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-attn-proj-float16] | 0.5448 | 0.3368 | 61.8% | torch-cublas |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-bfloat16] | 0.1124 | 0.0700 | 62.3% | torch-compile |
| 🔴 | **LogSumExpFwdOp** | test_logsumexp_bench[lm-head-logits-bfloat16] | 0.0165 | 0.0103 | 62.3% | torch-compile |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s896-bfloat16] | 0.0454 | 0.0283 | 62.4% | fa3 |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-hbm-streaming-threshold-float16] | 0.0606 | 0.0379 | 62.4% | marlin-fp32 |
| 🔴 | **VarMeanFwdOp** | test_var_mean_bench[3d-multidim-reduce-float16] | 0.0121 | 0.0076 | 62.5% | torch-compile |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[compile-smoke-square-64x64x128-float16] | 0.0043 | 0.0027 | 62.7% | torch-dequantized-matmul |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s896-float16] | 0.0453 | 0.0286 | 63.1% | fa3 |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b8-dmem512-d256-bfloat16] | 0.0334 | 0.0212 | 63.3% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[mid-m64-down-bfloat16] | 0.0207 | 0.0132 | 63.9% | torch-cublas |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-float16] | 1.4237 | 0.9204 | 64.6% | fla |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-bfloat16] | 0.3166 | 0.2056 | 64.9% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-bfloat16] | 1.4680 | 0.9536 | 65.0% | fla |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-float32] | 0.0195 | 0.0127 | 65.2% | torch-compile |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-float16] | 0.3138 | 0.2051 | 65.4% | fla |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0051 | 0.0033 | 65.4% | mamba |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-float16] | 0.3809 | 0.2495 | 65.5% | fla |
| 🔴 | **TopkSelectorFwdOp** | test_topk_selector_bench[topk2048-s32k-kv64k-float32] | 16.2375 | 10.6697 | 65.7% | flashinfer |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-l2-resident-ish-float16] | 0.0330 | 0.0217 | 65.8% | marlin-fp16 |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-float16] | 0.2017 | 0.1337 | 66.3% | fla |
| 🔴 | **GroupNormFwdOp** | test_group_norm_bench[wider-channel-g32-affine-float16] | 0.0060 | 0.0040 | 66.7% | flaggems |
| 🔴 | **AvgPool1dFwdOp** | test_avg_pool1d_bench[ceil-bfloat16] | 0.0035 | 0.0023 | 66.7% | torch-compile |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-bfloat16] | 0.3875 | 0.2584 | 66.7% | fla |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s1792-float16] | 0.1288 | 0.0860 | 66.7% | fa3 |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-float32] | 0.1073 | 0.0716 | 66.7% | torch-compile |
| 🔴 | **GroupNormFwdOp** | test_group_norm_bench[tail-spatial-g16-affine-float16] | 0.0061 | 0.0041 | 66.8% | flaggems |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float32-SiluAndMulFwdKernel-direct] | 0.0218 | 0.0146 | 66.9% | torch-compile |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-bfloat16] | 0.7504 | 0.5018 | 66.9% | fla |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s1792-bfloat16] | 0.1290 | 0.0863 | 66.9% | fa3 |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-unbatched-complex64] | 0.0081 | 0.0054 | 66.9% | torch-cufft |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-float16] | 0.7228 | 0.4867 | 67.3% | fla |
| 🔴 | **GroupNormFwdOp** | test_group_norm_no_affine_bench[tail-spatial-g16-float16] | 0.0052 | 0.0035 | 67.5% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-bfloat16] | 0.0969 | 0.0659 | 68.0% | fla |
| 🔴 | **AvgPool1dFwdOp** | test_avg_pool1d_bench[audio-downsample-float16] | 0.0061 | 0.0042 | 68.2% | torch-compile |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-bfloat16] | 0.2049 | 0.1401 | 68.4% | fla |
| 🔴 | **FusedAddRMSNormFwdOp** | test_fused_add_rms_norm_bench[llama-405b-decode-bfloat16] | 0.0062 | 0.0043 | 68.6% | flashinfer |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[moe-prefill-b128-per-tensor-float8_e4m3fn] | 0.9006 | 0.6245 | 69.3% | flashinfer-bmm-fp8 |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s3584-bfloat16] | 0.7495 | 0.5289 | 70.6% | fa3 |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-bfloat16] | 0.3114 | 0.2200 | 70.7% | fla |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s3584-float16] | 0.7495 | 0.5302 | 70.7% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-softcap50-float16] | 0.1765 | 0.1252 | 71.0% | flashinfer |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s7168-bfloat16] | 2.8453 | 2.0226 | 71.1% | fa3 |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-float16] | 0.0986 | 0.0702 | 71.2% | fla |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-float16] | 0.8322 | 0.5925 | 71.2% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s7168-float16] | 2.8449 | 2.0283 | 71.3% | fa3 |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s16k-h4-d64-float16] | 1.5163 | 1.0812 | 71.3% | fla |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.8080 | 0.5802 | 71.8% | fa3 |
| 🔴 | **MaxPool2dFwdOp** | test_max_pool2d_bench[resnet-stem-bfloat16] | 0.0473 | 0.0340 | 72.0% | torch-compile |
| 🔴 | **MaxPool2dFwdOp** | test_max_pool2d_bench[resnet-stem-float16] | 0.0471 | 0.0340 | 72.3% | torch-compile |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-float16] | 0.1488 | 0.1077 | 72.4% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0567 | 0.0411 | 72.6% | flashinfer |
| 🔴 | **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[nondiv-7x7-bfloat16] | 0.0158 | 0.0115 | 72.6% | torch-ref |
| 🔴 | **GroupNormFwdOp** | test_group_norm_no_affine_bench[wider-channel-g32-float16] | 0.0048 | 0.0035 | 72.7% | flaggems |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-float16] | 0.0569 | 0.0414 | 72.8% | flashinfer |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-2k-bfloat16] | 0.2802 | 0.2045 | 73.0% | torch-cublas |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[alexnet-ceil-bfloat16] | 0.0237 | 0.0174 | 73.4% | torch-compile |
| 🔴 | **LogicalOrFwdOp** | test_logical_or_manifest_bench[cnn-feat-broadcast-float16] | 0.0164 | 0.0120 | 73.5% | torch-compile |
| 🔴 | **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[sincnet-speaker-local-float16] | 0.0218 | 0.0160 | 73.6% | torch-compile |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-2k-float16] | 0.2832 | 0.2089 | 73.8% | torch-cublas |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b4-4k-bfloat16] | 1.0435 | 0.7705 | 73.8% | torch-cublas |
| 🔴 | **BmmFwdOp** | test_bmm_bench[moe-prefill-b128-bfloat16] | 0.2911 | 0.2152 | 73.9% | torch-cublas |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-bfloat16] | 0.6112 | 0.4522 | 74.0% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-float16] | 0.0931 | 0.0691 | 74.2% | flashinfer |
| 🔴 | **LtFwdOp** | test_lt_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0118 | 74.3% | torch-compile |
| 🔴 | **LogicalOrFwdOp** | test_logical_or_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0164 | 0.0122 | 74.4% | torch-compile |
| 🔴 | **NeFwdOp** | test_ne_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0118 | 74.4% | torch-compile |
| 🔴 | **GeFwdOp** | test_ge_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0118 | 74.5% | torch-compile |
| 🔴 | **LeFwdOp** | test_le_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0119 | 74.5% | torch-compile |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-bfloat16] | 0.0930 | 0.0693 | 74.6% | flashinfer |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s16k-h4-d64-bfloat16] | 1.4487 | 1.0809 | 74.6% | fla |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[alexnet-ceil-float16] | 0.0237 | 0.0177 | 74.6% | torch-compile |
| 🔴 | **LeFwdOp** | test_le_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0119 | 74.7% | torch-compile |
| 🔴 | **GtFwdOp** | test_gt_manifest_bench[cnn-feat-broadcast-float16] | 0.0160 | 0.0119 | 74.8% | torch-compile |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-bfloat16] | 0.1445 | 0.1082 | 74.9% | fla |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s8k-h4-d64-float16] | 0.7446 | 0.5576 | 74.9% | fla |
| 🔴 | **EqFwdOp** | test_eq_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0119 | 74.9% | torch-compile |
| 🔴 | **NeFwdOp** | test_ne_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0119 | 75.0% | torch-compile |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-float16] | 0.1669 | 0.1252 | 75.0% | flashinfer |
| 🔴 | **LogSumExpFwdOp** | test_logsumexp_bench[lm-head-logits-float16] | 0.0141 | 0.0106 | 75.1% | torch-compile |
| 🔴 | **EqFwdOp** | test_eq_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0119 | 75.2% | torch-compile |
| 🔴 | **Conv3dFwdOp** | test_conv3d_bench[video-stage-downsample-k3-s2-float16] | 0.0349 | 0.0263 | 75.2% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-float16] | 0.6180 | 0.4652 | 75.3% | fla |
| 🔴 | **Conv2dFwdOp** | test_conv2d_bench[highres-3x3-s1-float16] | 0.1047 | 0.0790 | 75.4% | torch-compile |
| 🔴 | **GtFwdOp** | test_gt_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0120 | 75.4% | torch-compile |
| 🔴 | **LogicalAndFwdOp** | test_logical_and_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0120 | 75.4% | torch-compile |
| 🔴 | **RopeNonNeoxFwdOp** | test_rope_non_neox_bench[non-neox-2d-b2-s2k-h32-d128-bfloat16] | 0.0252 | 0.0190 | 75.5% | torch-compile |
| 🔴 | **Conv2dFwdOp** | test_conv2d_bench[highres-3x3-s1-bias-float16] | 0.1050 | 0.0793 | 75.6% | torch-compile |
| 🔴 | **GeFwdOp** | test_ge_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0120 | 75.8% | torch-compile |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-1k-bfloat16] | 0.0407 | 0.0310 | 76.1% | torch-cublas |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s4k-h4-d64-bfloat16] | 0.1564 | 0.1191 | 76.2% | fla |
| 🔴 | **LogicalAndFwdOp** | test_logical_and_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0121 | 76.3% | torch-compile |
| 🔴 | **LtFwdOp** | test_lt_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0122 | 76.6% | torch-compile |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s8k-h4-d64-bfloat16] | 0.7267 | 0.5569 | 76.6% | fla |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-1k-float16] | 0.0406 | 0.0311 | 76.7% | torch-cublas |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-float16] | 0.3518 | 0.2714 | 77.1% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.3492 | 0.2700 | 77.3% | fa3 |
| 🔴 | **DeltaNetFwdOp** | test_deltanet_vs_fla_fwd[dn-b2-s16k-h4-d64-float16] | 0.4726 | 0.3661 | 77.5% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.6661 | 0.5171 | 77.6% | flashinfer |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-float16] | 0.0866 | 0.0672 | 77.6% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-float16] | 0.6677 | 0.5185 | 77.6% | flashinfer |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-bfloat16] | 0.0866 | 0.0675 | 77.9% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowFwdOp** | test_gqa_sliding_window_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.1517 | 0.1183 | 78.0% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowFwdOp** | test_gqa_sliding_window_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.1516 | 0.1184 | 78.1% | fa3 |
| 🔴 | **GatedDeltaNetPrefillBHTDFwdOp** | test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-float16] | 0.2508 | 0.1960 | 78.1% | fla |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s4k-h4-d64-float16] | 0.3686 | 0.2882 | 78.2% | fla |
| 🔴 | **DeltaNetFwdOp** | test_deltanet_vs_fla_fwd[dn-b2-s16k-h4-d64-bfloat16] | 0.4729 | 0.3700 | 78.2% | fla |
| 🔴 | **GatedDeltaNetPrefillBHTDFwdOp** | test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-bfloat16] | 0.2526 | 0.1979 | 78.3% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowFwdOp** | test_gqa_sliding_window_fwd_bench[llama-70b-long-w1024-float16] | 0.1528 | 0.1199 | 78.5% | fa3 |
| 🔴 | **Conv2dFwdOp** | test_conv2d_bench[classifier-1x1-float16] | 0.0092 | 0.0072 | 78.7% | torch-compile |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s4k-h4-d64-bfloat16] | 0.3648 | 0.2879 | 78.9% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowFwdOp** | test_gqa_sliding_window_fwd_bench[llama-8b-long-w1024-float16] | 0.1529 | 0.1209 | 79.0% | fa3 |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-float16] | 0.3132 | 0.2476 | 79.0% | fla |
| 🔴 | **grouped_gemm_nn** | test_grouped_gemm_bench[nn-batch16-m4096-n4096-k4096-float16] | 0.3407 | 0.2696 | 79.1% | torch |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-large-bfloat16] | 0.0715 | 0.0567 | 79.3% | torch-compile |
| 🔴 | **Conv3dFwdOp** | test_conv3d_bench[video-stage-downsample-k3-s2-bias-float16] | 0.0353 | 0.0281 | 79.5% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s4k-h4-d64-float16] | 0.1569 | 0.1254 | 79.9% | fla |

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
| ✅ | FFTC2CFwdOp | `tileops.ops.fft` | 6 | 0 | 0 | 3.68e-05 |
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
| ✅ | LogSoftmaxFwdOp | `tileops.ops.reduction.softmax` | 24 | 0 | 0 | 9.54e-07 |
| ✅ | LogSumExpFwdOp | `tileops.ops.reduction.softmax` | 24 | 0 | 0 | 4.77e-07 |
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
| ✅ | ProdFwdOp | `tileops.ops.reduction.reduce` | 6 | 0 | 0 | 7.28e-12 |
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

| | Op | Config | Device busy (ms) | TFLOPS | BW (TB/s) | Via | Ratio |
|:-|:---|:-------|------------:|-------:|----------:|:----|------:|
| 🔵 | AbsFwdOp | test_abs_bench[elementwise-16M-float16] | 0.0179 | 0.94 | 3.75 | torch 100.4%, torch-compile 100.2% | - |
| 🔵 | AbsFwdOp | test_abs_bench[elementwise-16M-bfloat16] | 0.0179 | 0.94 | 3.75 | torch 100.2%, torch-compile 100.2% | - |
| 🟡 | AbsFwdOp | test_abs_bench[elementwise-16M-float32] | 0.0340 | 0.49 | 3.94 | torch 99.7%, torch-compile 99.6% | - |
| 🔵 | AbsFwdOp | test_abs_bench[elementwise-256M-float16] | 0.2498 | 1.07 | 4.30 | torch 100.0%, torch-compile 100.0% | - |
| 🟡 | AbsFwdOp | test_abs_bench[elementwise-256M-bfloat16] | 0.2499 | 1.07 | 4.30 | torch 100.0%, torch-compile 99.8% | - |
| 🔵 | AdaLayerNormFwdOp | test_ada_layer_norm_bench[dit-xl-2-float16] | 0.0052 | 1.13 | 1.81 | torch-ref 231.3%, torch-compile 146.0% | - |
| 🔵 | AdaLayerNormFwdOp | test_ada_layer_norm_bench[dit-xl-2-bfloat16] | 0.0053 | 1.11 | 1.78 | torch-ref 227.7%, torch-compile 147.0% | - |
| 🔵 | AdaLayerNormFwdOp | test_ada_layer_norm_bench[llama-8b-prefill-float16] | 0.0198 | 2.12 | 3.39 | torch-ref 209.4%, torch-compile 129.1% | - |
| 🔵 | AdaLayerNormFwdOp | test_ada_layer_norm_bench[llama-8b-prefill-bfloat16] | 0.0199 | 2.11 | 3.38 | torch-ref 210.5%, torch-compile 133.9% | - |
| 🔵 | AdaLayerNormFwdOp | test_ada_layer_norm_bench[llama-8b-decode-bfloat16] | 0.0027 | 0.01 | 0.01 | torch-ref 389.2%, torch-compile 115.7% | - |
| 🔵 | AdaLayerNormZeroFwdOp | test_ada_layer_norm_zero_bench[dit-xl-2-float16] | 0.0062 | 1.14 | 1.90 | torch-ref 238.7%, torch-compile 125.3% | - |
| 🔵 | AdaLayerNormZeroFwdOp | test_ada_layer_norm_zero_bench[dit-xl-2-bfloat16] | 0.0062 | 1.13 | 1.89 | torch-ref 236.5%, torch-compile 130.3% | - |
| 🔵 | AdaLayerNormZeroFwdOp | test_ada_layer_norm_zero_bench[llama-8b-prefill-float16] | 0.0248 | 2.03 | 3.39 | torch-ref 215.5%, torch-compile 110.8% | - |
| 🔵 | AdaLayerNormZeroFwdOp | test_ada_layer_norm_zero_bench[llama-8b-prefill-bfloat16] | 0.0247 | 2.04 | 3.40 | torch-ref 217.5%, torch-compile 114.0% | - |
| 🔵 | AdaLayerNormZeroFwdOp | test_ada_layer_norm_zero_bench[llama-8b-decode-bfloat16] | 0.0028 | 0.01 | 0.01 | torch-ref 412.4%, torch-compile 114.1% | - |
| 🔵 | AdaptiveAvgPool2dFwdOp | test_adaptive_avg_pool2d_bench[resnet-global-float16] | 0.0030 | 0.27 | 0.55 | torch-ref 246.3%, torch-compile 124.7% | - |
| 🟢 | AdaptiveAvgPool2dFwdOp | test_adaptive_avg_pool2d_bench[spp-6x6-float16] | 0.0054 | 0.17 | 0.30 | torch-ref 196.4%, torch-compile 195.9% | - |
| 🔵 | AdaptiveAvgPool2dFwdOp | test_adaptive_avg_pool2d_bench[nondiv-7x7-bfloat16] | 0.0066 | 0.07 | 0.12 | torch-ref 138.8%, torch-compile 138.8% | - |
| 🔵 | AdaptiveMaxPool2dFwdOp | test_adaptive_max_pool2d_bench[global-1x1-float16] | 0.0029 | 0.28 | 0.56 | torch-ref 1543.4%, torch-compile 129.6% | - |
| 🟢 | AdaptiveMaxPool2dFwdOp | test_adaptive_max_pool2d_bench[spp-6x6-float16] | 0.0060 | 0.15 | 0.27 | torch-ref 237.2%, torch-compile 237.2% | - |
| 🟢 | AdaptiveMaxPool2dFwdOp | test_adaptive_max_pool2d_bench[nondiv-7x7-bfloat16] | 0.0065 | 0.08 | 0.13 | torch-ref 176.3%, torch-compile 176.3% | - |
| 🔴 | AdaptiveMaxPool2dIndicesFwdOp | test_adaptive_max_pool2d_indices_bench[global-1x1-float16] | 0.0133 | 0.06 | 0.13 | torch-ref 338.6%, torch-compile 61.5% | - |
| 🟡 | AdaptiveMaxPool2dIndicesFwdOp | test_adaptive_max_pool2d_indices_bench[spp-6x6-float16] | 0.0154 | 0.06 | 0.11 | torch-ref 92.9%, torch-compile 92.9% | - |
| 🔴 | AdaptiveMaxPool2dIndicesFwdOp | test_adaptive_max_pool2d_indices_bench[nondiv-7x7-bfloat16] | 0.0158 | 0.03 | 0.05 | torch-ref 72.6%, torch-compile 72.6% | - |
| 🔵 | AddFwdOp | test_add_manifest_bench[hidden-state-prefill-float16] | 0.0147 | 1.14 | 3.43 | torch 101.1%, torch-compile 100.0% | - |
| 🔵 | AddFwdOp | test_add_manifest_bench[hidden-state-prefill-bfloat16] | 0.0147 | 1.14 | 3.43 | torch 101.5%, torch-compile 100.0% | - |
| 🟡 | AddFwdOp | test_add_manifest_bench[hidden-state-prefill-float32] | 0.0265 | 0.63 | 3.80 | torch 100.1%, torch-compile 99.9% | - |
| 🔵 | AddFwdOp | test_add_manifest_bench[cnn-feat-broadcast-float16] | 0.0144 | 1.78 | 3.57 | torch 317.8%, torch-compile 100.2% | - |
| 🔵 | AddFwdOp | test_add_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0144 | 1.79 | 3.58 | torch 325.4%, torch-compile 100.2% | - |
| 🟡 | AddFwdOp | test_add_manifest_bench[cnn-feat-broadcast-float32] | 0.0266 | 0.97 | 3.86 | torch 186.1%, torch-compile 99.9% | - |
| 🔵 | AlibiFwdOp | test_alibi_bench[llama-prefill-2k-float16] | 0.0651 | 6.18 | 4.12 | torch-ref 909.0%, torch-compile 132.4% | - |
| 🔵 | AlibiFwdOp | test_alibi_bench[llama-prefill-2k-bfloat16] | 0.0645 | 6.24 | 4.16 | torch-ref 916.8%, torch-compile 133.8% | - |
| 🔵 | AlibiFwdOp | test_alibi_bench[llama-prefill-4k-float16] | 0.2852 | 5.65 | 3.76 | torch-ref 914.6%, torch-compile 119.8% | - |
| 🔵 | AlibiFwdOp | test_alibi_bench[llama-prefill-4k-bfloat16] | 0.2847 | 5.66 | 3.77 | torch-ref 916.3%, torch-compile 119.6% | - |
| 🟡 | AllFwdOp | test_all_bench[mask-validation-4k-bool] | 0.0020 | 0.07 | 0.07 | flaggems 96.7%, torch 885.3%, torch-compile 91.8% | - |
| 🟡 | AllFwdOp | test_all_bench[mask-validation-32k-bool] | 0.0037 | 0.28 | 0.28 | flaggems 171.8%, torch 272.6%, torch-compile 90.6% | - |
| 🔴 | AllFwdOp | test_all_bench[3d-multidim-reduce-bool] | 0.0111 | 0.19 | 0.19 | flaggems 105.8%, torch 93.1%, torch-compile 38.5% | - |
| 🔵 | AmaxFwdOp | test_amax_bench[hidden-state-reduce-float16] | 0.0074 | 1.13 | 2.26 | flaggems 103.5%, torch 259.1%, torch-compile 136.2% | - |
| 🔵 | AmaxFwdOp | test_amax_bench[hidden-state-reduce-bfloat16] | 0.0074 | 1.13 | 2.26 | flaggems 105.4%, torch 260.6%, torch-compile 136.2% | - |
| 🔵 | AmaxFwdOp | test_amax_bench[long-seq-reduce-bfloat16] | 0.0041 | 0.51 | 1.02 | flaggems 330.5%, torch 275.8%, torch-compile 120.3% | - |
| 🔴 | AmaxFwdOp | test_amax_bench[3d-multidim-reduce-float16] | 0.0113 | 0.19 | 0.37 | flaggems 109.6%, torch 114.2%, torch-compile 43.9% | - |
| 🔵 | AminFwdOp | test_amin_bench[hidden-state-reduce-float16] | 0.0074 | 1.13 | 2.26 | torch 258.8%, torch-compile 136.6% | - |
| 🔵 | AminFwdOp | test_amin_bench[hidden-state-reduce-bfloat16] | 0.0074 | 1.13 | 2.26 | torch 260.3%, torch-compile 136.4% | - |
| 🔵 | AminFwdOp | test_amin_bench[long-seq-reduce-bfloat16] | 0.0041 | 0.51 | 1.02 | torch 275.0%, torch-compile 114.1% | - |
| 🔴 | AminFwdOp | test_amin_bench[3d-multidim-reduce-float16] | 0.0113 | 0.19 | 0.37 | torch 114.5%, torch-compile 43.9% | - |
| 🟡 | AnyFwdOp | test_any_bench[mask-validation-4k-bool] | 0.0020 | 0.07 | 0.07 | flaggems 96.8%, torch 909.8%, torch-compile 88.5% | - |
| 🟡 | AnyFwdOp | test_any_bench[mask-validation-32k-bool] | 0.0038 | 0.28 | 0.28 | flaggems 170.4%, torch 278.0%, torch-compile 87.3% | - |
| 🔴 | AnyFwdOp | test_any_bench[3d-multidim-reduce-bool] | 0.0111 | 0.19 | 0.19 | flaggems 106.1%, torch 169.5%, torch-compile 33.5% | - |
| 🟢 | ArgmaxFwdOp | test_argmax_bench[lm-head-argmax-float16] | 0.0039 | 0.11 | 0.21 | flaggems 775.6%, torch 909.9%, torch-compile 740.5% | - |
| 🟢 | ArgmaxFwdOp | test_argmax_bench[lm-head-argmax-bfloat16] | 0.0040 | 0.10 | 0.21 | flaggems 715.7%, torch 905.6%, torch-compile 732.3% | - |
| 🔵 | ArgmaxFwdOp | test_argmax_bench[hidden-state-argmax-float16] | 0.0092 | 0.92 | 1.83 | flaggems 133.2%, torch 268.5%, torch-compile 207.7% | - |
| 🔵 | ArgmaxFwdOp | test_argmax_bench[hidden-state-argmax-bfloat16] | 0.0096 | 0.87 | 1.74 | flaggems 120.9%, torch 258.1%, torch-compile 201.3% | - |
| 🟡 | ArgmaxFwdOp | test_argmax_bench[3d-non-last-axis-argmax-float16] | 0.0039 | 0.54 | 2.15 | flaggems 97.5%, torch 286.1%, torch-compile 117.2% | - |
| 🟢 | ArgminFwdOp | test_argmin_bench[lm-head-argmin-float16] | 0.0040 | 0.10 | 0.20 | flaggems 2890.8%, torch 885.6%, torch-compile 715.2% | - |
| 🟢 | ArgminFwdOp | test_argmin_bench[lm-head-argmin-bfloat16] | 0.0066 | 0.06 | 0.12 | flaggems 1546.8%, torch 540.2%, torch-compile 437.6% | - |
| 🔵 | ArgminFwdOp | test_argmin_bench[hidden-state-argmin-float16] | 0.0096 | 0.87 | 1.74 | flaggems 103.0%, torch 255.1%, torch-compile 197.3% | - |
| 🟡 | ArgminFwdOp | test_argmin_bench[hidden-state-argmin-bfloat16] | 0.0099 | 0.85 | 1.70 | flaggems 100.0%, torch 251.8%, torch-compile 196.8% | - |
| 🔴 | AvgPool1dFwdOp | test_avg_pool1d_bench[audio-downsample-float16] | 0.0061 | 0.51 | 1.02 | torch-ref 249.5%, torch-compile 68.2% | - |
| 🟡 | AvgPool1dFwdOp | test_avg_pool1d_bench[long-temporal-float16] | 0.0213 | 0.96 | 1.92 | torch-ref 279.1%, torch-compile 80.5% | - |
| 🔴 | AvgPool1dFwdOp | test_avg_pool1d_bench[ceil-bfloat16] | 0.0035 | 0.30 | 0.46 | torch-ref 153.7%, torch-compile 66.7% | - |
| 🔵 | AvgPool2dFwdOp | test_avg_pool2d_bench[vision-3x3-s2-float16] | 0.0040 | 0.91 | 1.01 | flaggems 166.9%, torch-ref 229.0%, torch-compile 103.2% | - |
| 🟢 | AvgPool2dFwdOp | test_avg_pool2d_bench[vision-5x5-s2-float16] | 0.0040 | 1.24 | 0.50 | flaggems 179.4%, torch-ref 244.4%, torch-compile 511.1% | - |
| 🔵 | AvgPool2dFwdOp | test_avg_pool2d_bench[ceil-divisor-bfloat16] | 0.0031 | 1.12 | 0.73 | flaggems 184.8%, torch-ref 244.0%, torch-compile 123.5% | - |
| 🔵 | AvgPool3dFwdOp | test_avg_pool3d_bench[video-2x2x2-float16] | 0.0037 | 0.43 | 0.97 | cudnn 158.6%, torch-ref 267.2%, torch-compile 130.2% | - |
| 🟡 | AvgPool3dFwdOp | test_avg_pool3d_bench[ceil-video-float16] | 0.0044 | 0.59 | 0.43 | cudnn 128.1%, torch-ref 260.6%, torch-compile 92.0% | - |
| 🟡 | AvgPool3dFwdOp | test_avg_pool3d_bench[divisor-bfloat16] | 0.0023 | 0.15 | 0.21 | torch-ref 221.0%, torch-compile 82.5% | - |
| 🟢 | BatchNormBwdOp | test_batch_norm_bwd_bench[resnet50-fc-float16] | 0.0070 | 0.00 | 0.00 | torch-autograd 332.5%, torch-native-batch-norm 178.7% | - |
| 🔵 | BatchNormBwdOp | test_batch_norm_bwd_bench[resnet50-stage1-float16] | 0.0148 | 0.28 | 0.21 | torch-autograd 186.6%, torch-native-batch-norm 127.7% | - |
| 🔵 | BatchNormBwdOp | test_batch_norm_bwd_bench[resnet50-stage2-float16] | 0.0141 | 0.30 | 0.22 | torch-autograd 170.0%, torch-native-batch-norm 108.4% | - |
| 🔵 | BatchNormBwdOp | test_batch_norm_bwd_bench[resnet50-stage3-float16] | 0.0171 | 0.38 | 0.28 | torch-autograd 149.0%, torch-native-batch-norm 103.4% | - |
| 🟢 | BatchNormBwdOp | test_batch_norm_bwd_bench[large-spatial-float16] | 6.8730 | 0.62 | 0.47 | torch-autograd 188.8%, torch-native-batch-norm 171.6% | - |
| 🔴 | BatchNormFwdOp | test_batch_norm_fwd_bench[resnet50-fc-float16] | 0.0061 | 0.00 | 0.00 | flaggems 90.6%, torch-cudnn 184.8%, torch-compile 29.8% | - |
| 🔴 | BatchNormFwdOp | test_batch_norm_fwd_bench[resnet50-stage1-float16] | 0.0109 | 0.48 | 0.19 | flaggems 94.2%, torch-cudnn 103.8%, torch-compile 40.9% | - |
| 🔴 | BatchNormFwdOp | test_batch_norm_fwd_bench[resnet50-stage2-float16] | 0.0107 | 0.49 | 0.20 | flaggems 83.5%, torch-cudnn 97.3%, torch-compile 30.8% | - |
| 🔴 | BatchNormFwdOp | test_batch_norm_fwd_bench[resnet50-stage3-float16] | 0.0129 | 0.62 | 0.25 | flaggems 84.9%, torch-cudnn 86.3%, torch-compile 35.5% | - |
| 🔴 | BatchNormFwdOp | test_batch_norm_fwd_bench[large-spatial-float16] | 4.3442 | 1.24 | 0.49 | flaggems 89.8%, torch-cudnn 104.4%, torch-compile 23.4% | - |
| 🟡 | BitwiseAndFwdOp | test_bitwise_bench[bitwise_and-1024x4096-BitwiseAndFwdOp-bitwise_and] | 0.0148 | 0.28 | 3.41 | torch 100.0%, torch-compile 99.8% | - |
| 🟡 | BitwiseAndFwdOp | test_bitwise_bench[bitwise_and-1024x10240-BitwiseAndFwdOp-bitwise_and] | 0.0321 | 0.33 | 3.91 | torch 99.8%, torch-compile 99.5% | - |
| 🔵 | BitwiseAndFwdOp | test_bitwise_and_manifest_bench[hidden-state-prefill-bool] | 0.0084 | 1.00 | 3.01 | torch 120.7%, torch-compile 107.3% | - |
| 🟡 | BitwiseAndFwdOp | test_bitwise_and_manifest_bench[hidden-state-prefill-int32] | 0.0262 | 0.32 | 3.84 | torch 100.2%, torch-compile 99.8% | - |
| 🔵 | BitwiseAndFwdOp | test_bitwise_and_manifest_bench[hidden-state-prefill-int64] | 0.0491 | 0.17 | 4.10 | torch 101.0%, torch-compile 100.1% | - |
| 🔵 | BitwiseAndFwdOp | test_bitwise_and_manifest_bench[cnn-feat-broadcast-bool] | 0.0081 | 1.59 | 3.17 | torch 557.7%, torch-compile 123.7% | - |
| 🔵 | BitwiseAndFwdOp | test_bitwise_and_manifest_bench[cnn-feat-broadcast-int32] | 0.0264 | 0.49 | 3.89 | torch 186.8%, torch-compile 100.2% | - |
| 🟡 | BitwiseAndFwdOp | test_bitwise_and_manifest_bench[cnn-feat-broadcast-int64] | 0.0500 | 0.26 | 4.11 | torch 116.5%, torch-compile 99.5% | - |
| 🟡 | BitwiseNotFwdOp | test_bitwise_not_bench[elementwise-16M-int32] | 0.0340 | 0.49 | 3.95 | torch 99.9%, torch-compile 99.7% | - |
| 🟡 | BitwiseNotFwdOp | test_bitwise_not_bench[elementwise-16M-int64] | 0.0652 | 0.26 | 4.12 | torch 104.3%, torch-compile 99.2% | - |
| 🔵 | BitwiseNotFwdOp | test_bitwise_not_bench[elementwise-256M-int32] | 0.4986 | 0.54 | 4.31 | torch 101.2%, torch-compile 101.2% | - |
| 🟡 | BitwiseOrFwdOp | test_bitwise_bench[bitwise_or-1024x4096-BitwiseOrFwdOp-bitwise_or] | 0.0148 | 0.28 | 3.40 | torch 98.7%, torch-compile 98.5% | - |
| 🔵 | BitwiseOrFwdOp | test_bitwise_or_manifest_bench[hidden-state-prefill-bool] | 0.0081 | 1.03 | 3.10 | torch 108.3%, torch-compile 105.1% | - |
| 🟡 | BitwiseOrFwdOp | test_bitwise_or_manifest_bench[hidden-state-prefill-int32] | 0.0265 | 0.32 | 3.79 | torch 99.9%, torch-compile 99.7% | - |
| 🔵 | BitwiseOrFwdOp | test_bitwise_or_manifest_bench[hidden-state-prefill-int64] | 0.0493 | 0.17 | 4.09 | torch 100.7%, torch-compile 100.0% | - |
| 🔵 | BitwiseOrFwdOp | test_bitwise_or_manifest_bench[cnn-feat-broadcast-bool] | 0.0081 | 1.58 | 3.17 | torch 545.5%, torch-compile 125.4% | - |
| 🟡 | BitwiseOrFwdOp | test_bitwise_or_manifest_bench[cnn-feat-broadcast-int32] | 0.0266 | 0.48 | 3.86 | torch 185.6%, torch-compile 99.4% | - |
| 🟡 | BitwiseOrFwdOp | test_bitwise_or_manifest_bench[cnn-feat-broadcast-int64] | 0.0502 | 0.26 | 4.09 | torch 115.9%, torch-compile 99.5% | - |
| 🔵 | BitwiseXorFwdOp | test_bitwise_bench[bitwise_xor-1024x4096-BitwiseXorFwdOp-bitwise_xor] | 0.0147 | 0.29 | 3.43 | torch 101.1%, torch-compile 100.6% | - |
| 🔵 | BitwiseXorFwdOp | test_bitwise_xor_manifest_bench[hidden-state-prefill-bool] | 0.0081 | 1.03 | 3.09 | torch 122.2%, torch-compile 108.1% | - |
| 🟡 | BitwiseXorFwdOp | test_bitwise_xor_manifest_bench[hidden-state-prefill-int32] | 0.0265 | 0.32 | 3.80 | torch 99.5%, torch-compile 104.8% | - |
| 🔵 | BitwiseXorFwdOp | test_bitwise_xor_manifest_bench[hidden-state-prefill-int64] | 0.0492 | 0.17 | 4.09 | torch 100.7%, torch-compile 100.3% | - |
| 🔵 | BitwiseXorFwdOp | test_bitwise_xor_manifest_bench[cnn-feat-broadcast-bool] | 0.0080 | 1.61 | 3.21 | torch 564.8%, torch-compile 125.2% | - |
| 🔵 | BitwiseXorFwdOp | test_bitwise_xor_manifest_bench[cnn-feat-broadcast-int32] | 0.0263 | 0.49 | 3.90 | torch 187.7%, torch-compile 116.2% | - |
| 🟡 | BitwiseXorFwdOp | test_bitwise_xor_manifest_bench[cnn-feat-broadcast-int64] | 0.0501 | 0.26 | 4.10 | torch 116.3%, torch-compile 99.4% | - |
| 🟡 | BmmFp8KNFwdOp | test_bmm_fp8_kn_bench[square-b4-1k-per-tensor-float8_e4m3fn] | 0.0390 | 220.21 | 0.43 | torch-fp32-ref 753.6%, flashinfer-bmm-fp8 90.9% | - |
| 🟢 | BmmFp8KNFwdOp | test_bmm_fp8_kn_bench[square-b8-2k-per-tensor-float8_e4m3fn] | 0.3060 | 449.12 | 0.44 | torch-fp32-ref 1326.2%, flashinfer-bmm-fp8 203.5% | - |
| 🔴 | BmmFp8KNFwdOp | test_bmm_fp8_kn_bench[mha-decode-b32-pv-per-tensor-float8_e4m3fn] | 0.0647 | 33.21 | 0.28 | torch-fp32-ref 364.9%, flashinfer-bmm-fp8 38.5% | - |
| 🔴 | BmmFp8KNFwdOp | test_bmm_fp8_kn_bench[mha-decode-b64-qk-per-tensor-float8_e4m3fn] | 0.1154 | 37.23 | 0.45 | torch-fp32-ref 250.3%, flashinfer-bmm-fp8 43.1% | - |
| 🔴 | BmmFp8KNFwdOp | test_bmm_fp8_kn_bench[moe-prefill-b128-per-tensor-float8_e4m3fn] | 0.9006 | 152.60 | 0.37 | torch-fp32-ref 599.5%, flashinfer-bmm-fp8 69.3% | - |
| 🔵 | BmmFp8NKFwdOp | test_bmm_fp8_nk_bench[square-b4-1k-per-tensor-float8_e4m3fn] | 0.0119 | 721.66 | 1.41 | torch-fp32-ref 2466.1%, flashinfer-bmm-fp8 109.7% | - |
| 🔵 | BmmFp8NKFwdOp | test_bmm_fp8_nk_bench[square-b8-2k-per-tensor-float8_e4m3fn] | 0.1196 | 1149.61 | 1.12 | torch-fp32-ref 3400.2%, flashinfer-bmm-fp8 105.5% | - |
| 🔵 | BmmFp8NKFwdOp | test_bmm_fp8_nk_bench[mha-decode-b32-pv-per-tensor-float8_e4m3fn] | 0.0090 | 237.97 | 1.98 | torch-fp32-ref 2621.3%, flashinfer-bmm-fp8 105.3% | - |
| 🔵 | BmmFp8NKFwdOp | test_bmm_fp8_nk_bench[mha-decode-b64-qk-per-tensor-float8_e4m3fn] | 0.0157 | 272.80 | 3.26 | torch-fp32-ref 1829.6%, flashinfer-bmm-fp8 137.4% | - |
| 🔵 | BmmFp8NKFwdOp | test_bmm_fp8_nk_bench[moe-prefill-b128-per-tensor-float8_e4m3fn] | 0.1319 | 1042.08 | 2.54 | torch-fp32-ref 4101.6%, flashinfer-bmm-fp8 105.0% | - |
| 🔵 | BmmFwdOp | test_bmm_bench[small-b8-128-float16] | 0.0027 | 12.34 | 0.29 | flaggems 116.5%, torch-cublas 118.8% | - |
| 🔵 | BmmFwdOp | test_bmm_bench[small-b8-128-bfloat16] | 0.0027 | 12.34 | 0.29 | flaggems 116.5%, torch-cublas 118.8% | - |
| 🔴 | BmmFwdOp | test_bmm_bench[square-b8-1k-float16] | 0.0406 | 423.07 | 1.24 | flaggems 110.5%, torch-cublas 76.7% | - |
| 🔴 | BmmFwdOp | test_bmm_bench[square-b8-1k-bfloat16] | 0.0407 | 421.74 | 1.24 | flaggems 110.0%, torch-cublas 76.1% | - |
| 🟡 | BmmFwdOp | test_bmm_bench[square-b16-512-float16] | 0.0132 | 324.20 | 1.90 | flaggems 114.1%, torch-cublas 91.3% | - |
| 🟡 | BmmFwdOp | test_bmm_bench[square-b16-512-bfloat16] | 0.0133 | 322.64 | 1.89 | flaggems 113.5%, torch-cublas 89.9% | - |
| 🔵 | BmmFwdOp | test_bmm_bench[square-b32-256-float16] | 0.0066 | 162.89 | 1.91 | flaggems 119.9%, torch-cublas 107.3% | - |
| 🔵 | BmmFwdOp | test_bmm_bench[square-b32-256-bfloat16] | 0.0066 | 163.68 | 1.92 | flaggems 120.5%, torch-cublas 107.3% | - |
| 🔴 | BmmFwdOp | test_bmm_bench[square-b4-4k-bfloat16] | 1.0435 | 526.85 | 0.39 | flaggems 93.1%, torch-cublas 73.8% | - |
| 🔴 | BmmFwdOp | test_bmm_bench[square-b8-2k-float16] | 0.2832 | 485.31 | 0.71 | flaggems 97.5%, torch-cublas 73.8% | - |
| 🔴 | BmmFwdOp | test_bmm_bench[square-b8-2k-bfloat16] | 0.2802 | 490.57 | 0.72 | flaggems 97.6%, torch-cublas 73.0% | - |
| 🟡 | BmmFwdOp | test_bmm_bench[mha-decode-b64-qk-float16] | 0.0225 | 190.66 | 3.07 | flaggems 115.6%, torch-cublas 94.3% | - |
| 🟡 | BmmFwdOp | test_bmm_bench[mha-decode-b64-qk-bfloat16] | 0.0225 | 191.19 | 3.08 | flaggems 115.5%, torch-cublas 94.3% | - |
| 🔵 | BmmFwdOp | test_bmm_bench[mha-decode-b64-pv-float16] | 0.0239 | 179.44 | 2.89 | flaggems 169.9%, torch-cublas 101.7% | - |
| 🔵 | BmmFwdOp | test_bmm_bench[mha-decode-b64-pv-bfloat16] | 0.0239 | 179.44 | 2.89 | flaggems 170.0%, torch-cublas 101.7% | - |
| 🔴 | BmmFwdOp | test_bmm_bench[moe-prefill-b128-bfloat16] | 0.2911 | 472.18 | 2.08 | flaggems 101.4%, torch-cublas 73.9% | - |
| 🟢 | CBProducerFwdOp | test_cb_producer_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0071 | 18.81 | 0.59 | torch 530.0% | - |
| 🟢 | CBProducerFwdOp | test_cb_producer_fwd_bench[mamba2-2p7b-b4-s2k-bfloat16] | 0.0118 | 22.67 | 0.71 | torch 448.4% | - |
| 🔵 | CeilFwdOp | test_ceil_bench[elementwise-16M-float16] | 0.0179 | 0.94 | 3.75 | torch 100.4%, torch-compile 100.4% | - |
| 🔵 | CeilFwdOp | test_ceil_bench[elementwise-16M-bfloat16] | 0.0179 | 0.94 | 3.75 | torch 100.4%, torch-compile 100.4% | - |
| 🟡 | CeilFwdOp | test_ceil_bench[elementwise-16M-float32] | 0.0340 | 0.49 | 3.95 | torch 99.8%, torch-compile 100.0% | - |
| 🟡 | CeilFwdOp | test_ceil_bench[elementwise-256M-float16] | 0.2506 | 1.07 | 4.28 | torch 99.9%, torch-compile 99.7% | - |
| 🔵 | CeilFwdOp | test_ceil_bench[elementwise-256M-bfloat16] | 0.2497 | 1.07 | 4.30 | torch 100.3%, torch-compile 100.0% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-float16] | 0.0355 | 0.47 | 3.78 | torch 98.2%, torch-compile 98.9% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-bfloat16] | 0.0355 | 0.47 | 3.79 | torch 98.5%, torch-compile 98.9% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-float32] | 0.0658 | 0.25 | 4.08 | torch 99.6%, torch-compile 99.4% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-256M-float16] | 0.4859 | 0.55 | 4.42 | torch 99.9%, torch-compile 99.8% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-256M-bfloat16] | 0.4855 | 0.55 | 4.42 | torch 99.9%, torch-compile 99.9% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-min-only-float16] | 0.0267 | 0.63 | 3.77 | torch 99.6%, torch-compile 98.6% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-min-only-bfloat16] | 0.0269 | 0.62 | 3.74 | torch 99.5%, torch-compile 98.1% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-min-only-float32] | 0.0500 | 0.34 | 4.02 | torch 98.9%, torch-compile 98.5% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-256M-min-only-float16] | 0.3693 | 0.73 | 4.36 | torch 99.8%, torch-compile 99.9% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-256M-min-only-bfloat16] | 0.3684 | 0.73 | 4.37 | torch 99.8%, torch-compile 100.1% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-max-only-float16] | 0.0266 | 0.63 | 3.79 | torch 99.8%, torch-compile 99.0% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-max-only-bfloat16] | 0.0271 | 0.62 | 3.72 | torch 99.6%, torch-compile 98.4% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-max-only-float32] | 0.0500 | 0.34 | 4.03 | torch 98.9%, torch-compile 98.3% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-256M-max-only-float16] | 0.3688 | 0.73 | 4.37 | torch 99.8%, torch-compile 100.0% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-256M-max-only-bfloat16] | 0.3677 | 0.73 | 4.38 | torch 100.0%, torch-compile 100.3% | - |
| 🔵 | ClampScalarFwdOp | test_clamp_scalar_manifest_bench[elementwise-16M-float16] | 0.0184 | 0.91 | 3.64 | torch 110.1%, torch-compile 100.2% | - |
| 🔵 | ClampScalarFwdOp | test_clamp_scalar_manifest_bench[elementwise-16M-bfloat16] | 0.0184 | 0.91 | 3.64 | torch 103.6%, torch-compile 101.2% | - |
| 🔵 | ClampScalarFwdOp | test_clamp_scalar_manifest_bench[elementwise-16M-float32] | 0.0338 | 0.50 | 3.97 | torch 100.8%, torch-compile 100.7% | - |
| 🔵 | ClampScalarFwdOp | test_clamp_scalar_manifest_bench[elementwise-256M-float16] | 0.2524 | 1.06 | 4.25 | torch 115.7%, torch-compile 100.6% | - |
| 🔵 | ClampScalarFwdOp | test_clamp_scalar_manifest_bench[elementwise-256M-bfloat16] | 0.2521 | 1.06 | 4.26 | torch 109.3%, torch-compile 105.4% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[whisper-large-conv1-float16] | 0.0481 | 38.27 | 0.18 | flaggems 232.7%, torch 118.2%, torch-compile 118.2% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[whisper-large-conv1-bfloat16] | 0.0485 | 37.99 | 0.18 | flaggems 231.0%, torch 116.2%, torch-compile 116.4% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[wav2vec2-layer1-float16] | 0.0067 | 4.92 | 0.50 | flaggems 601.4%, torch 279.8%, torch-compile 279.8% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[wav2vec2-layer1-bfloat16] | 0.0067 | 4.92 | 0.50 | flaggems 602.9%, torch 283.2%, torch-compile 283.2% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[encodec-init-float16] | 0.0036 | 3.03 | 0.45 | flaggems 689.2%, torch 187.4%, torch-compile 186.5% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[encodec-init-bfloat16] | 0.0036 | 3.03 | 0.45 | flaggems 688.3%, torch 187.4%, torch-compile 186.9% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[encodec-deep-float16] | 0.0120 | 32.28 | 0.09 | flaggems 595.5%, torch 141.3%, torch-compile 141.3% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[encodec-deep-bfloat16] | 0.0120 | 32.28 | 0.09 | flaggems 595.5%, torch 141.3%, torch-compile 141.3% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[whisper-large-conv1-bias-float16] | 0.0477 | 38.67 | 0.18 | flaggems 233.6%, torch 145.2%, torch-compile 128.0% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[whisper-large-conv1-bias-bfloat16] | 0.0477 | 38.69 | 0.18 | flaggems 234.1%, torch 145.3%, torch-compile 127.0% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[wav2vec2-layer1-bias-float16] | 0.0069 | 4.98 | 0.48 | flaggems 566.2%, torch 365.3%, torch-compile 325.5% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[wav2vec2-layer1-bias-bfloat16] | 0.0069 | 4.95 | 0.48 | flaggems 564.1%, torch 367.7%, torch-compile 312.4% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[encodec-init-bias-float16] | 0.0036 | 3.19 | 0.44 | flaggems 652.3%, torch 291.2%, torch-compile 237.2% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[encodec-init-bias-bfloat16] | 0.0036 | 3.21 | 0.44 | flaggems 655.8%, torch 297.3%, torch-compile 239.3% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[encodec-deep-bias-float16] | 0.0124 | 31.21 | 0.09 | flaggems 567.5%, torch 164.2%, torch-compile 149.8% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[encodec-deep-bias-bfloat16] | 0.0124 | 31.29 | 0.09 | flaggems 568.6%, torch 164.1%, torch-compile 150.1% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[resnet-3x3-float16] | 0.0130 | 35.59 | 0.13 | flaggems 640.4%, torch 113.3%, torch-compile 88.9% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[resnet-3x3-bfloat16] | 0.0130 | 35.59 | 0.13 | flaggems 639.8%, torch 114.5%, torch-compile 90.1% | - |
| 🟢 | Conv2dFwdOp | test_conv2d_bench[stem-3x3-s2-float16] | 0.0036 | 3.02 | 0.13 | flaggems 363.4%, torch 181.2%, torch-compile 259.8% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[stage-transition-3x3-s2-float16] | 0.0138 | 33.53 | 0.13 | flaggems 858.8%, torch 123.0%, torch-compile 97.2% | - |
| 🔴 | Conv2dFwdOp | test_conv2d_bench[highres-3x3-s1-float16] | 0.1047 | 282.65 | 0.21 | flaggems 701.8%, torch 90.5%, torch-compile 75.4% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[midres-5x5-s1-float16] | 0.0162 | 79.49 | 0.10 | flaggems 1250.7%, torch 120.6%, torch-compile 99.2% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[stage-transition-5x5-s2-float16] | 0.0225 | 57.18 | 0.13 | flaggems 1381.4%, torch 113.0%, torch-compile 99.0% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[stride2-bfloat16] | 0.0111 | 5.21 | 0.05 | flaggems 583.6%, torch 133.4%, torch-compile 108.9% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[resnet-1x1-float16] | 0.0044 | 47.22 | 0.93 | flaggems 1127.9%, torch 96.4%, torch-compile 192.7% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[resnet-1x1-bfloat16] | 0.0044 | 47.22 | 0.93 | flaggems 1130.9%, torch 91.9%, torch-compile 191.2% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[bottleneck-expand-1x1-float16] | 0.0038 | 53.97 | 0.56 | flaggems 746.2%, torch 105.0%, torch-compile 194.1% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[bottleneck-reduce-1x1-float16] | 0.0047 | 43.99 | 0.46 | flaggems 564.4%, torch 92.5%, torch-compile 169.9% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[late-stage-1x1-float16] | 0.0050 | 20.59 | 0.21 | flaggems 308.3%, torch 127.6%, torch-compile 133.3% | - |
| 🔴 | Conv2dFwdOp | test_conv2d_bench[classifier-1x1-float16] | 0.0092 | 11.23 | 0.26 | flaggems 225.2%, torch 99.0%, torch-compile 78.7% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[deeplabv3-aspp-3x3-rate12-float16] | 0.0889 | 108.71 | 0.16 | flaggems 805.3%, torch 133.9%, torch-compile 102.3% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[mobilenetv2-depthwise-float16] | 0.0028 | 0.64 | 0.14 | flaggems 1925.7%, torch 108.0%, torch-compile 196.7% | - |
| 🟢 | Conv2dFwdOp | test_conv2d_bench[resnext-grouped-3x3-float16] | 0.0041 | 3.50 | 0.15 | flaggems 467.4%, torch 460.5%, torch-compile 461.2% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[resnet-3x3-bias-float16] | 0.0132 | 34.93 | 0.13 | flaggems 621.1%, torch 137.9%, torch-compile 88.6% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[resnet-3x3-bias-bfloat16] | 0.0137 | 33.71 | 0.12 | flaggems 599.7%, torch 134.0%, torch-compile 90.4% | - |
| 🟢 | Conv2dFwdOp | test_conv2d_bench[stem-3x3-s2-bias-float16] | 0.0035 | 3.16 | 0.14 | flaggems 350.9%, torch 271.6%, torch-compile 273.4% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[stage-transition-3x3-s2-bias-float16] | 0.0141 | 32.71 | 0.13 | flaggems 832.1%, torch 141.4%, torch-compile 96.6% | - |
| 🔴 | Conv2dFwdOp | test_conv2d_bench[highres-3x3-s1-bias-float16] | 0.1050 | 281.94 | 0.21 | flaggems 698.6%, torch 109.3%, torch-compile 75.6% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[midres-5x5-s1-bias-float16] | 0.0165 | 77.81 | 0.10 | flaggems 1221.4%, torch 138.0%, torch-compile 101.4% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[stage-transition-5x5-s2-bias-float16] | 0.0225 | 57.10 | 0.13 | flaggems 1375.9%, torch 127.6%, torch-compile 99.9% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[stride2-bias-bfloat16] | 0.0116 | 4.99 | 0.05 | flaggems 552.8%, torch 152.5%, torch-compile 108.0% | - |
| 🟢 | Conv2dFwdOp | test_conv2d_bench[resnet-1x1-bias-float16] | 0.0046 | 45.26 | 0.88 | flaggems 1054.5%, torch 254.6%, torch-compile 192.0% | - |
| 🟢 | Conv2dFwdOp | test_conv2d_bench[resnet-1x1-bias-bfloat16] | 0.0046 | 44.95 | 0.88 | flaggems 1049.7%, torch 250.0%, torch-compile 201.4% | - |
| 🟢 | Conv2dFwdOp | test_conv2d_bench[bottleneck-expand-1x1-bias-float16] | 0.0041 | 50.37 | 0.52 | flaggems 673.4%, torch 214.8%, torch-compile 191.4% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[bottleneck-reduce-1x1-bias-float16] | 0.0050 | 41.48 | 0.43 | flaggems 516.5%, torch 146.4%, torch-compile 170.6% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[late-stage-1x1-bias-float16] | 0.0053 | 19.50 | 0.19 | flaggems 280.0%, torch 176.3%, torch-compile 138.2% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[classifier-1x1-bias-float16] | 0.0095 | 10.82 | 0.25 | flaggems 209.4%, torch 126.6%, torch-compile 82.2% | - |
| 🟢 | Conv3dFwdOp | test_conv3d_bench[r3d-stem-k3-s1-float16] | 0.0229 | 90.69 | 1.17 | flaggems 374.1%, torch 500.4%, torch-compile 500.3% | - |
| 🔴 | Conv3dFwdOp | test_conv3d_bench[video-stage-downsample-k3-s2-float16] | 0.0349 | 39.74 | 0.13 | flaggems 622.5%, torch 75.4%, torch-compile 75.2% | - |
| 🔴 | Conv3dFwdOp | test_conv3d_bench[unet-encoder-k3-s1-bfloat16] | 0.3542 | 40.92 | 0.07 | flaggems 89.4%, torch 32.5%, torch-compile 32.6% | - |
| 🔴 | Conv3dFwdOp | test_conv3d_bench[3d-unet-aspp-3x3x3-rate6-float16] | 0.1269 | 57.13 | 0.04 | flaggems 236.6%, torch 29.6%, torch-compile 29.6% | - |
| 🟢 | Conv3dFwdOp | test_conv3d_bench[3d-resnext-grouped-k3-float16] | 0.0157 | 5.51 | 0.15 | flaggems 1616.7%, torch 1784.2%, torch-compile 1685.5% | - |
| 🟢 | Conv3dFwdOp | test_conv3d_bench[r3d-stem-k3-s1-bias-float16] | 0.0230 | 90.87 | 1.17 | flaggems 368.6%, torch 671.7%, torch-compile 547.5% | - |
| 🔴 | Conv3dFwdOp | test_conv3d_bench[video-stage-downsample-k3-s2-bias-float16] | 0.0353 | 39.30 | 0.13 | flaggems 611.1%, torch 84.8%, torch-compile 79.5% | - |
| 🔴 | Conv3dFwdOp | test_conv3d_bench[unet-encoder-k3-s1-bias-bfloat16] | 0.3536 | 41.02 | 0.07 | flaggems 89.3%, torch 39.9%, torch-compile 34.6% | - |
| 🔵 | CosFwdOp | test_cos_bench[elementwise-16M-float16] | 0.0260 | 0.65 | 2.58 | torch 104.6%, torch-compile 107.8% | - |
| 🔵 | CosFwdOp | test_cos_bench[elementwise-16M-bfloat16] | 0.0264 | 0.64 | 2.54 | torch 103.1%, torch-compile 107.6% | - |
| 🟡 | CosFwdOp | test_cos_bench[elementwise-16M-float32] | 0.0352 | 0.48 | 3.81 | torch 97.7%, torch-compile 97.6% | - |
| 🔵 | CosFwdOp | test_cos_bench[elementwise-256M-float16] | 0.3772 | 0.71 | 2.85 | torch 104.2%, torch-compile 108.3% | - |
| 🔵 | CosFwdOp | test_cos_bench[elementwise-256M-bfloat16] | 0.3828 | 0.70 | 2.80 | torch 102.7%, torch-compile 107.8% | - |
| 🔵 | CountNonzeroFwdOp | test_count_nonzero_bench[sparsity-hidden-float16] | 0.0081 | 2.06 | 2.07 | torch 785.4%, torch-compile 111.8% | - |
| 🔵 | CountNonzeroFwdOp | test_count_nonzero_bench[sparsity-hidden-bfloat16] | 0.0081 | 2.07 | 2.07 | torch 788.5%, torch-compile 112.5% | - |
| 🔵 | CountNonzeroFwdOp | test_count_nonzero_bench[sparsity-seq-float16] | 0.0037 | 0.56 | 0.57 | torch 410.3%, torch-compile 103.5% | - |
| 🔴 | CountNonzeroFwdOp | test_count_nonzero_bench[3d-multidim-reduce-float16] | 0.0116 | 0.36 | 0.36 | torch 188.4%, torch-compile 41.1% | - |
| 🟢 | CumprodFwdOp | test_cumprod_bench[hidden-state-scan-float16] | 0.0115 | 0.73 | 2.92 | torch 1268.8%, torch-compile 210.9% | - |
| 🟢 | CumprodFwdOp | test_cumprod_bench[hidden-state-scan-bfloat16] | 0.0109 | 0.77 | 3.08 | torch 1339.6%, torch-compile 223.5% | - |
| 🟢 | CumprodFwdOp | test_cumprod_bench[long-seq-scan-bfloat16] | 0.0070 | 0.30 | 1.19 | torch 962.3%, torch-compile 172.7% | - |
| 🟡 | CumsumFwdOp | test_cumsum_bench[hidden-state-scan-float16] | 0.0115 | 0.73 | 2.92 | flaggems 92.2%, torch 1269.9%, torch-compile 210.6% | - |
| 🟡 | CumsumFwdOp | test_cumsum_bench[hidden-state-scan-bfloat16] | 0.0109 | 0.77 | 3.07 | flaggems 96.8%, torch 1339.5%, torch-compile 223.4% | - |
| 🔵 | CumsumFwdOp | test_cumsum_bench[long-seq-scan-bfloat16] | 0.0070 | 0.30 | 1.19 | flaggems 113.7%, torch 961.8%, torch-compile 172.7% | - |
| 🔴 | DaCumsumFwdOp | test_da_cumsum_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0051 | 0.27 | 0.39 | mamba 65.4%, torch-ref 1401.3%, torch-compile 93.7% | - |
| 🔴 | DaCumsumFwdOp | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-bfloat16] | 0.0154 | 0.48 | 0.68 | mamba 41.8%, torch-ref 592.6%, torch-compile 74.0% | - |
| 🟡 | DaCumsumFwdOp | test_da_cumsum_fwd_bench[mamba2-780m-b1-s4k-dt-bias-float16] | 0.0043 | 0.37 | 0.46 | mamba 80.6%, torch-ref 1731.3%, torch-compile 111.9% | - |
| 🔴 | DaCumsumFwdOp | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-dt-bias-bfloat16] | 0.0148 | 0.56 | 0.71 | mamba 42.9%, torch-ref 649.2%, torch-compile 77.2% | - |
| 🔴 | DaCumsumFwdOp | test_da_cumsum_fwd_bench[mamba2-2p7b-b2-s32k-dt-bias-float16] | 0.0599 | 0.70 | 0.87 | mamba 37.2%, torch-ref 395.4%, torch-compile 57.7% | - |
| 🟢 | DeepSeekSparseAttentionDecodeWithKVCacheFwdOp | test_dsa_decode_bench[single-batch-mainstream-float16] | 1.8607 | 313.91 | 0.16 | torch-ref 1019.5%, torch-compile 892.7%, torch-sdpa 282.6% | - |
| 🟢 | DeepSeekSparseAttentionDecodeWithKVCacheFwdOp | test_dsa_decode_bench[longer-kv-lower-topk-float16] | 0.5005 | 291.76 | 0.30 | torch-ref 3859.8%, torch-compile 3252.3%, torch-sdpa 1053.3%, torch-gather 362.3% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s2k-h4-d64-float16] | 0.1307 | 2.05 | 0.21 | fla 86.7% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s2k-h4-d64-bfloat16] | 0.1316 | 2.04 | 0.21 | fla 87.0% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s4k-h4-d64-float16] | 0.2595 | 2.07 | 0.21 | fla 82.6% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s4k-h4-d64-bfloat16] | 0.2619 | 2.05 | 0.21 | fla 82.7% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s8k-h4-d64-float16] | 0.5052 | 2.13 | 0.22 | fla 85.6% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s8k-h4-d64-bfloat16] | 0.5107 | 2.10 | 0.21 | fla 85.4% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s16k-h4-d64-float16] | 0.9924 | 2.16 | 0.22 | fla 87.1% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s16k-h4-d64-bfloat16] | 1.0041 | 2.14 | 0.22 | fla 86.7% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b1-h8-d128-bfloat16] | 0.0028 | 0.28 | 0.19 | torch 1176.4%, torch-compile 459.6% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b1-h16-d128-bfloat16] | 0.0031 | 0.51 | 0.34 | torch 1138.4%, torch-compile 456.8% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b1-h32-d128-bfloat16] | 0.0034 | 0.94 | 0.63 | torch 1163.5%, torch-compile 480.8% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b1-h48-d128-bfloat16] | 0.0036 | 1.33 | 0.90 | torch 1220.8%, torch-compile 541.9% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b1-h64-d128-bfloat16] | 0.0038 | 1.64 | 1.11 | torch 1141.7%, torch-compile 450.8% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b8-h32-d128-bfloat16] | 0.0087 | 2.90 | 1.96 | torch 1029.4%, torch-compile 438.2% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b8-h48-d128-bfloat16] | 0.0123 | 3.07 | 2.07 | torch 901.8%, torch-compile 321.7% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b8-h64-d128-bfloat16] | 0.0163 | 3.09 | 2.09 | torch 870.0%, torch-compile 315.3% | - |
| 🟡 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s2k-h4-d64-float16] | 0.0628 | 2.14 | 0.34 | fla 98.7% | - |
| 🟡 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s2k-h4-d64-bfloat16] | 0.0629 | 2.13 | 0.34 | fla 99.1% | - |
| 🟡 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s4k-h4-d64-float16] | 0.1095 | 2.45 | 0.38 | fla 90.0% | - |
| 🟡 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s4k-h4-d64-bfloat16] | 0.1097 | 2.45 | 0.38 | fla 90.5% | - |
| 🟡 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s8k-h4-d64-float16] | 0.2337 | 2.30 | 0.36 | fla 81.1% | - |
| 🟡 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s8k-h4-d64-bfloat16] | 0.2346 | 2.29 | 0.36 | fla 81.4% | - |
| 🔴 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s16k-h4-d64-float16] | 0.4726 | 2.27 | 0.36 | fla 77.5% | - |
| 🔴 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s16k-h4-d64-bfloat16] | 0.4729 | 2.27 | 0.36 | fla 78.2% | - |
| 🟡 | DivFwdOp | test_binary_arith_bench[div-1024x4096-float16-float16-DivFwdOp-div-positive] | 0.0085 | 0.49 | 2.97 | torch 103.4%, torch-compile 99.6% | - |
| 🟡 | DivFwdOp | test_binary_arith_bench[div-1024x10240-float16-float16-DivFwdOp-div-positive] | 0.0181 | 0.58 | 3.47 | torch 101.9%, torch-compile 99.7% | - |
| 🟡 | DivFwdOp | test_binary_arith_bench[div-1024x11008-float16-float16-DivFwdOp-div-positive] | 0.0189 | 0.60 | 3.58 | torch 101.9%, torch-compile 99.5% | - |
| 🟡 | DivFwdOp | test_div_manifest_bench[hidden-state-prefill-float16] | 0.0148 | 0.57 | 3.40 | torch 102.3%, torch-compile 99.2% | - |
| 🔵 | DivFwdOp | test_div_manifest_bench[hidden-state-prefill-bfloat16] | 0.0147 | 0.57 | 3.43 | torch 102.9%, torch-compile 100.1% | - |
| 🟡 | DivFwdOp | test_div_manifest_bench[hidden-state-prefill-float32] | 0.0263 | 0.32 | 3.83 | torch 100.6%, torch-compile 99.8% | - |
| 🟡 | DivFwdOp | test_div_manifest_bench[cnn-feat-broadcast-float16] | 0.0160 | 0.80 | 3.21 | torch 317.2%, torch-compile 92.4% | - |
| 🟡 | DivFwdOp | test_div_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0144 | 0.89 | 3.56 | torch 355.2%, torch-compile 99.6% | - |
| 🔵 | DivFwdOp | test_div_manifest_bench[cnn-feat-broadcast-float32] | 0.0265 | 0.49 | 3.88 | torch 200.6%, torch-compile 100.1% | - |
| 🟢 | DropoutFwdOp | test_dropout_bench[tokens-1k-hidden-4k-float16] | 0.0062 | 0.68 | 2.72 | torch 189.1%, torch-compile 182.9% | - |
| 🔵 | DropoutFwdOp | test_dropout_bench[tokens-1k-hidden-4k-float32] | 0.0103 | 0.41 | 3.26 | torch 144.7%, torch-compile 116.1% | - |
| 🟢 | DropoutFwdOp | test_dropout_bench[tokens-1k-hidden-10k-bfloat16] | 0.0123 | 0.85 | 3.40 | torch 191.9%, torch-compile 191.2% | - |
| 🔵 | EluFwdOp | test_elu_manifest_bench[mlp-hidden-float16] | 0.0122 | 2.76 | 2.76 | torch 147.6%, torch-compile 130.5% | - |
| 🔵 | EluFwdOp | test_elu_manifest_bench[mlp-hidden-bfloat16] | 0.0120 | 2.79 | 2.79 | torch 151.1%, torch-compile 139.1% | - |
| 🔵 | EluFwdOp | test_elu_manifest_bench[mlp-hidden-wide-float16] | 0.0219 | 3.06 | 3.06 | torch 150.0%, torch-compile 135.9% | - |
| 🔵 | EluFwdOp | test_elu_manifest_bench[mlp-hidden-wide-bfloat16] | 0.0215 | 3.12 | 3.12 | torch 154.2%, torch-compile 145.1% | - |
| 🔴 | EngramDecodeFwdOp | test_engram_decode_bench[decode-b1-dmem512-d256-float16] | 0.0330 | 0.02 | 0.02 | torch-ref 287.0%, torch-compile 40.3% | - |
| 🔴 | EngramDecodeFwdOp | test_engram_decode_bench[decode-b4-dmem1024-d512-float16] | 0.0827 | 0.10 | 0.03 | torch-ref 146.6%, torch-compile 31.0% | - |
| 🔴 | EngramDecodeFwdOp | test_engram_decode_bench[decode-b8-dmem512-d256-bfloat16] | 0.0334 | 0.13 | 0.02 | torch-ref 333.1%, torch-compile 63.3% | - |
| 🟢 | EngramGateConvBwdOp | test_engram_gate_conv_bwd_bench[bwd-b1-s32-d256-float16] | 0.0111 | 0.04 | 0.02 | torch 1510.3%, torch-compile 448.1% | - |
| 🟢 | EngramGateConvBwdOp | test_engram_gate_conv_bwd_bench[bwd-b2-s64-d512-float16] | 0.0198 | 0.20 | 0.07 | torch 1012.6%, torch-compile 301.0% | - |
| 🟢 | EngramGateConvBwdOp | test_engram_gate_conv_bwd_bench[bwd-b1-s128-d256-bfloat16] | 0.0168 | 0.12 | 0.04 | torch 1096.4%, torch-compile 324.2% | - |
| 🟢 | EngramGateConvFwdOp | test_engram_gate_conv_fwd_bench[fwd-b1-s32-d256-float16] | 0.0040 | 0.05 | 0.02 | torch-ref 1851.2%, torch-compile 272.4% | - |
| 🟢 | EngramGateConvFwdOp | test_engram_gate_conv_fwd_bench[fwd-b2-s64-d512-float16] | 0.0051 | 0.31 | 0.13 | torch-ref 1692.4%, torch-compile 246.2% | - |
| 🟢 | EngramGateConvFwdOp | test_engram_gate_conv_fwd_bench[fwd-b1-s128-d256-bfloat16] | 0.0045 | 0.18 | 0.07 | torch-ref 1789.3%, torch-compile 260.0% | - |
| 🔵 | EqFwdOp | test_comparison_bench[eq-1024x4096-float16-eq] | 0.0076 | 0.55 | 2.77 | torch 103.4%, torch-compile 103.4% | - |
| 🔵 | EqFwdOp | test_comparison_bench[eq-1024x10240-float16-eq] | 0.0158 | 0.66 | 3.32 | torch 101.0%, torch-compile 101.2% | - |
| 🔵 | EqFwdOp | test_eq_manifest_bench[hidden-state-prefill-float16] | 0.0133 | 0.63 | 3.16 | torch 102.2%, torch-compile 101.9% | - |
| 🟡 | EqFwdOp | test_eq_manifest_bench[hidden-state-prefill-bfloat16] | 0.0131 | 0.64 | 3.20 | torch 99.5%, torch-compile 99.8% | - |
| 🟡 | EqFwdOp | test_eq_manifest_bench[hidden-state-prefill-float32] | 0.0224 | 0.38 | 3.38 | torch 99.9%, torch-compile 99.6% | - |
| 🔴 | EqFwdOp | test_eq_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.81 | 2.43 | torch 299.6%, torch-compile 75.2% | - |
| 🔴 | EqFwdOp | test_eq_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.81 | 2.42 | torch 306.2%, torch-compile 74.9% | - |
| 🟡 | EqFwdOp | test_eq_manifest_bench[cnn-feat-broadcast-float32] | 0.0210 | 0.61 | 3.06 | torch 228.9%, torch-compile 87.9% | - |
| 🟡 | ErfFwdOp | test_erf_bench[elementwise-16M-float16] | 0.0284 | 0.59 | 2.36 | torch 93.1%, torch-compile 102.7% | - |
| 🟡 | ErfFwdOp | test_erf_bench[elementwise-16M-bfloat16] | 0.0285 | 0.59 | 2.35 | torch 97.2%, torch-compile 103.7% | - |
| 🟡 | ErfFwdOp | test_erf_bench[elementwise-16M-float32] | 0.0350 | 0.48 | 3.83 | torch 98.1%, torch-compile 98.8% | - |
| 🟡 | ErfFwdOp | test_erf_bench[elementwise-256M-float16] | 0.4215 | 0.64 | 2.55 | torch 91.6%, torch-compile 102.4% | - |
| 🟡 | ErfFwdOp | test_erf_bench[elementwise-256M-bfloat16] | 0.4236 | 0.63 | 2.53 | torch 96.0%, torch-compile 103.2% | - |
| 🔵 | ExpFwdOp | test_exp_bench[elementwise-16M-float16] | 0.0181 | 0.93 | 3.71 | torch 100.8%, torch-compile 100.5% | - |
| 🔵 | ExpFwdOp | test_exp_bench[elementwise-16M-bfloat16] | 0.0182 | 0.92 | 3.69 | torch 100.9%, torch-compile 101.4% | - |
| 🔵 | ExpFwdOp | test_exp_bench[elementwise-16M-float32] | 0.0340 | 0.49 | 3.95 | torch 100.4%, torch-compile 100.3% | - |
| 🔵 | ExpFwdOp | test_exp_bench[elementwise-256M-float16] | 0.2544 | 1.06 | 4.22 | torch 100.8%, torch-compile 100.8% | - |
| 🔵 | ExpFwdOp | test_exp_bench[elementwise-256M-bfloat16] | 0.2573 | 1.04 | 4.17 | torch 100.6%, torch-compile 102.3% | - |
| 🔵 | Expm1FwdOp | test_expm1_bench[elementwise-16M-float16] | 0.0180 | 1.87 | 3.74 | torch 140.6%, torch-compile 149.6% | - |
| 🟢 | Expm1FwdOp | test_expm1_bench[elementwise-16M-bfloat16] | 0.0181 | 1.86 | 3.71 | torch 154.5%, torch-compile 154.4% | - |
| 🔵 | Expm1FwdOp | test_expm1_bench[elementwise-16M-float32] | 0.0340 | 0.99 | 3.95 | torch 100.7%, torch-compile 101.2% | - |
| 🔵 | Expm1FwdOp | test_expm1_bench[elementwise-256M-float16] | 0.2542 | 2.11 | 4.22 | torch 144.7%, torch-compile 154.8% | - |
| 🟢 | Expm1FwdOp | test_expm1_bench[elementwise-256M-bfloat16] | 0.2572 | 2.09 | 4.18 | torch 159.9%, torch-compile 159.5% | - |
| 🔴 | FFTC2CFwdOp | test_fft_bench[fft-4k-c64-unbatched-complex64] | 0.0081 | 0.03 | 0.01 | torch-cufft 66.9%, torch-compile 66.9% | - |
| 🔴 | FFTC2CFwdOp | test_fft_bench[fft-4k-c64-b64-complex64] | 0.0152 | 1.03 | 0.28 | torch-cufft 37.0%, torch-compile 37.0% | - |
| 🔴 | FFTC2CFwdOp | test_fft_bench[fft-4k-c128-b64-complex128] | 0.0305 | 0.52 | 0.28 | torch-cufft 27.8%, torch-compile 27.8% | - |
| 🟢 | FP8LightningIndexerFwdOp | test_fp8_lightning_indexer_bench[lightning-indexer-s8k-h32-d64-bfloat16] | 0.6174 | 55.65 | 1.80 | torch-ref 18138.9%, torch-compile 8040.0% | - |
| 🟢 | FP8QuantFwdOp | test_fp8_quant_bench[kv-index-8k-d64-float16] | 0.0028 | 1.15 | 0.58 | torch-ref 605.8%, torch-compile 243.0% | - |
| 🟡 | FP8QuantFwdOp | test_fp8_quant_bench[kv-index-8k-d64-bfloat16] | 0.0028 | 1.15 | 0.58 | torch-ref 614.0%, torch-compile 98.8% | - |
| 🔵 | FP8QuantFwdOp | test_fp8_quant_bench[kv-index-4k-d128-float32] | 0.0040 | 0.79 | 0.66 | torch-ref 389.6%, torch-compile 106.5% | - |
| 🔵 | FloorDivideFwdOp | test_binary_arith_bench[floor_divide-1024x4096-float16-float16-FloorDivideFwdOp-floor_divide-positive] | 0.0087 | 0.48 | 2.89 | torch 302.9%, torch-compile 100.4% | - |
| 🔵 | FloorDivideFwdOp | test_binary_arith_bench[floor_divide-1024x10240-float16-float16-FloorDivideFwdOp-floor_divide-positive] | 0.0180 | 0.58 | 3.50 | torch 331.2%, torch-compile 100.4% | - |
| 🔵 | FloorDivideFwdOp | test_floor_divide_manifest_bench[hidden-state-prefill-float16] | 0.0151 | 1.11 | 3.34 | torch 321.7%, torch-compile 100.3% | - |
| 🔵 | FloorDivideFwdOp | test_floor_divide_manifest_bench[hidden-state-prefill-bfloat16] | 0.0149 | 1.13 | 3.38 | torch 338.7%, torch-compile 100.2% | - |
| 🔵 | FloorDivideFwdOp | test_floor_divide_manifest_bench[hidden-state-prefill-float32] | 0.0264 | 0.64 | 3.82 | torch 180.0%, torch-compile 100.6% | - |
| 🟡 | FloorDivideFwdOp | test_floor_divide_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 1.61 | 3.22 | torch 685.8%, torch-compile 99.0% | - |
| 🟡 | FloorDivideFwdOp | test_floor_divide_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 1.62 | 3.23 | torch 749.3%, torch-compile 99.8% | - |
| 🔵 | FloorDivideFwdOp | test_floor_divide_manifest_bench[cnn-feat-broadcast-float32] | 0.0266 | 0.96 | 3.86 | torch 380.9%, torch-compile 100.2% | - |
| 🔵 | FloorFwdOp | test_floor_bench[elementwise-16M-float16] | 0.0179 | 0.94 | 3.74 | torch 100.2%, torch-compile 100.2% | - |
| 🔵 | FloorFwdOp | test_floor_bench[elementwise-16M-bfloat16] | 0.0179 | 0.94 | 3.75 | torch 100.4%, torch-compile 100.2% | - |
| 🟡 | FloorFwdOp | test_floor_bench[elementwise-16M-float32] | 0.0340 | 0.49 | 3.95 | torch 100.0%, torch-compile 99.9% | - |
| 🔵 | FloorFwdOp | test_floor_bench[elementwise-256M-float16] | 0.2496 | 1.08 | 4.30 | torch 100.3%, torch-compile 100.1% | - |
| 🔵 | FloorFwdOp | test_floor_bench[elementwise-256M-bfloat16] | 0.2496 | 1.08 | 4.30 | torch 100.3%, torch-compile 100.2% | - |
| 🔵 | FusedAddLayerNormFwdOp | test_fused_add_layer_norm_bench[llama-8b-prefill-float16] | 0.0211 | 2.39 | 3.19 | torch-ref 550.4%, torch-compile 135.2% | - |
| 🔵 | FusedAddLayerNormFwdOp | test_fused_add_layer_norm_bench[llama-8b-prefill-bfloat16] | 0.0220 | 2.29 | 3.05 | torch-ref 531.7%, torch-compile 131.0% | - |
| 🔵 | FusedAddLayerNormFwdOp | test_fused_add_layer_norm_bench[llama-8b-decode-bfloat16] | 0.0032 | 0.01 | 0.02 | torch-ref 597.9%, torch-compile 117.2% | - |
| 🔵 | FusedAddLayerNormFwdOp | test_fused_add_layer_norm_bench[llama-70b-prefill-float16] | 0.0442 | 2.28 | 3.04 | torch-ref 515.1%, torch-compile 101.6% | - |
| 🟡 | FusedAddLayerNormFwdOp | test_fused_add_layer_norm_bench[llama-70b-prefill-bfloat16] | 0.0475 | 2.12 | 2.83 | torch-ref 483.5%, torch-compile 97.2% | - |
| 🔵 | FusedAddLayerNormFwdOp | test_fused_add_layer_norm_bench[llama-70b-decode-bfloat16] | 0.0041 | 0.01 | 0.02 | torch-ref 626.2%, torch-compile 135.5% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-8b-prefill-float16] | 0.0208 | 2.02 | 3.23 | flashinfer 92.8%, vllm 90.0%, torch-ref 1284.5%, torch-compile 93.8% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-8b-prefill-bfloat16] | 0.0213 | 1.97 | 3.15 | flashinfer 90.5%, vllm 89.8%, torch-ref 1264.3%, torch-compile 92.5% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-8b-decode-bfloat16] | 0.0027 | 0.01 | 0.02 | flashinfer 87.6%, vllm 109.4%, torch-ref 1058.9%, torch-compile 120.0% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-70b-prefill-float16] | 0.0378 | 2.22 | 3.55 | flashinfer 95.9%, vllm 95.0%, torch-ref 1361.8%, torch-compile 96.4% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-70b-prefill-bfloat16] | 0.0380 | 2.21 | 3.53 | flashinfer 95.1%, vllm 96.0%, torch-ref 1363.8%, torch-compile 95.9% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-70b-decode-bfloat16] | 0.0035 | 0.01 | 0.02 | flashinfer 82.6%, vllm 100.9%, torch-ref 859.7%, torch-compile 86.2% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-405b-prefill-float16] | 0.0768 | 2.18 | 3.50 | flashinfer 92.9%, vllm 101.3%, torch-ref 1280.4%, torch-compile 93.9% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-405b-prefill-bfloat16] | 0.0855 | 1.96 | 3.14 | flashinfer 83.9%, vllm 91.4%, torch-ref 1159.1%, torch-compile 84.4% | - |
| 🔴 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-405b-decode-bfloat16] | 0.0062 | 0.01 | 0.03 | flashinfer 68.6%, vllm 80.4%, torch-ref 511.4%, torch-compile 93.6% | - |
| 🔵 | FusedMoEExpertsNopadPersistent3WGFwdOp | test_moe_experts_nopad_bench[qwen3-235b-decode-bfloat16] | 2.7726 | 130.12 | 4.07 | vllm-triton 103.0% | - |
| 🔵 | FusedMoEExpertsNopadPersistent3WGFwdOp | test_moe_experts_nopad_bench[qwen3-235b-prefill-bfloat16] | 6.0374 | 478.05 | 1.89 | vllm-triton 120.0% | - |
| 🔵 | FusedMoEExpertsNopadPersistent3WGFwdOp | test_moe_experts_nopad_bench[deepseek-v3-decode-bfloat16] | 5.4159 | 66.61 | 4.17 | vllm-triton 101.8% | - |
| 🔵 | FusedMoEExpertsNopadPersistent3WGFwdOp | test_moe_experts_nopad_bench[deepseek-v3-prefill-bfloat16] | 8.4890 | 339.99 | 2.67 | vllm-triton 104.0% | - |
|  | FusedMoEExpertsNopadPersistent3WGFwdOp | test_moe_experts_nopad_bench[deepseek-v3-ep2-decode-bfloat16] | 2.7228 | 132.50 | 4.15 | - | - |
|  | FusedMoEExpertsNopadPersistent3WGFwdOp | test_moe_experts_nopad_bench[deepseek-v3-ep2-prefill-bfloat16] | 4.1410 | 696.98 | 2.75 | - | - |
| 🔵 | FusedMoeFwdOp | test_fused_moe_fwd_bench[qwen3-235b-decode-bfloat16] | 2.7727 | 130.12 | 4.07 | vllm 103.1% | - |
| 🔵 | FusedMoeFwdOp | test_fused_moe_fwd_bench[qwen3-235b-prefill-bfloat16] | 6.0667 | 475.75 | 1.88 | vllm 120.0% | - |
| 🔵 | FusedMoeFwdOp | test_fused_moe_fwd_bench[deepseek-v3-decode-bfloat16] | 5.4253 | 66.50 | 4.16 | vllm 101.7% | - |
| 🔵 | FusedMoeFwdOp | test_fused_moe_fwd_bench[deepseek-v3-prefill-bfloat16] | 8.3550 | 345.45 | 2.71 | vllm 106.1% | - |
| 🟢 | FusedMoeFwdOp | test_fused_moe_fwd_bench[kimi-k2-decode-bfloat16] | 3.8889 | 92.77 | 5.80 | torch-ref 1456.4% | - |
| 🟢 | FusedMoeFwdOp | test_fused_moe_fwd_bench[kimi-k2-prefill-bfloat16] | 7.8753 | 366.49 | 2.88 | torch-ref 1787.9% | - |
| 🔵 | FusedTopKOp | test_fused_topk_bench[1-384-8-sigmoid-renormalize] | 0.0083 | 0.00 | 0.00 | vllm 100.0% | - |
| 🟡 | FusedTopKOp | test_fused_topk_bench[32-384-8-sigmoid-renormalize] | 0.0119 | 0.02 | 0.00 | vllm 81.5% | - |
| 🟡 | FusedTopKOp | test_fused_topk_bench[512-384-8-sigmoid-renormalize] | 0.0126 | 0.28 | 0.03 | vllm 83.2% | - |
| 🔵 | FusedTopKOp | test_fused_topk_bench[4096-384-8-sigmoid-renormalize] | 0.0203 | 1.40 | 0.17 | vllm 117.5% | - |
| 🔵 | FusedTopKOp | test_fused_topk_bench[1-128-8-softmax-norenormalize] | 0.0043 | 0.00 | 0.00 | vllm 142.1% | - |
| 🔵 | FusedTopKOp | test_fused_topk_bench[32-128-8-softmax-norenormalize] | 0.0074 | 0.01 | 0.00 | vllm 112.1% | - |
| 🔵 | FusedTopKOp | test_fused_topk_bench[512-128-8-softmax-norenormalize] | 0.0078 | 0.15 | 0.02 | vllm 115.6% | - |
| 🔵 | FusedTopKOp | test_fused_topk_bench[4096-128-8-softmax-norenormalize] | 0.0110 | 0.86 | 0.12 | vllm 146.9% | - |
| 🟡 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s2k-h4-d64-float16] | 0.1829 | 1.47 | 0.17 | fla 81.0% | - |
| 🟡 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s2k-h4-d64-bfloat16] | 0.1844 | 1.46 | 0.17 | fla 80.3% | - |
| 🔴 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s4k-h4-d64-float16] | 0.3686 | 1.46 | 0.17 | fla 78.2% | - |
| 🔴 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s4k-h4-d64-bfloat16] | 0.3648 | 1.47 | 0.17 | fla 78.9% | - |
| 🔴 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s8k-h4-d64-float16] | 0.7446 | 1.44 | 0.17 | fla 74.9% | - |
| 🔴 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s8k-h4-d64-bfloat16] | 0.7267 | 1.48 | 0.17 | fla 76.6% | - |
| 🔴 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s16k-h4-d64-float16] | 1.5163 | 1.42 | 0.17 | fla 71.3% | - |
| 🔴 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s16k-h4-d64-bfloat16] | 1.4487 | 1.48 | 0.17 | fla 74.6% | - |
| 🟡 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b1-h8-d128-bfloat16] | 0.0074 | 0.07 | 0.07 | fla 90.6%, torch 409.5%, torch-compile 80.6% | - |
| 🟡 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b1-h16-d128-bfloat16] | 0.0074 | 0.14 | 0.14 | fla 94.8%, torch 428.0%, torch-compile 90.1% | - |
| 🟡 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b1-h32-d128-bfloat16] | 0.0078 | 0.27 | 0.27 | fla 93.9%, torch 456.8%, torch-compile 106.5% | - |
| 🔵 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b1-h48-d128-bfloat16] | 0.0079 | 0.40 | 0.40 | fla 112.9%, torch 508.5%, torch-compile 130.2% | - |
| 🔵 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b1-h64-d128-bfloat16] | 0.0082 | 0.52 | 0.52 | fla 108.6%, torch 513.0%, torch-compile 119.2% | - |
| 🔵 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b8-h32-d128-bfloat16] | 0.0159 | 1.06 | 1.08 | fla 110.3%, torch 564.1%, torch-compile 133.1% | - |
| 🟡 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b8-h48-d128-bfloat16] | 0.0231 | 1.09 | 1.11 | fla 96.4%, torch 522.3%, torch-compile 106.2% | - |
| 🟡 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b8-h64-d128-bfloat16] | 0.0304 | 1.11 | 1.12 | fla 88.5%, torch 518.7%, torch-compile 105.2% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-float16] | 0.0986 | 1.36 | 0.11 | fla 71.2% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-bfloat16] | 0.0969 | 1.39 | 0.11 | fla 68.0% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-init-b2-s4k-h4-d64-float16] | 0.1569 | 1.71 | 0.13 | fla 79.9% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-init-b2-s4k-h4-d64-bfloat16] | 0.1564 | 1.72 | 0.13 | fla 76.2% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-float16] | 0.3132 | 1.71 | 0.13 | fla 79.0% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-bfloat16] | 0.3114 | 1.72 | 0.14 | fla 70.7% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-float16] | 0.6180 | 1.74 | 0.14 | fla 75.3% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-bfloat16] | 0.6112 | 1.76 | 0.14 | fla 74.0% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-float16] | 0.0866 | 12.40 | 0.20 | fla 77.6% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-bfloat16] | 0.0866 | 12.40 | 0.20 | fla 77.9% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-float16] | 0.1488 | 14.43 | 0.23 | fla 72.4% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-bfloat16] | 0.1445 | 14.86 | 0.23 | fla 74.9% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-float16] | 0.3138 | 13.69 | 0.21 | fla 65.4% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-bfloat16] | 0.3166 | 13.57 | 0.21 | fla 64.9% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-float16] | 0.6363 | 13.50 | 0.21 | fla 61.4% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-bfloat16] | 0.6370 | 13.48 | 0.21 | fla 61.8% | - |
| 🔵 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s2k-h4-d64-float16] | 0.0669 | 16.05 | 0.25 | fla 100.4% | - |
| 🔵 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s2k-h4-d64-bfloat16] | 0.0664 | 16.16 | 0.25 | fla 101.6% | - |
| 🟡 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s4k-h4-d64-float16] | 0.1151 | 18.66 | 0.29 | fla 93.5% | - |
| 🟡 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s4k-h4-d64-bfloat16] | 0.1145 | 18.75 | 0.29 | fla 94.5% | - |
| 🟡 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s8k-h4-d64-float16] | 0.2192 | 19.59 | 0.31 | fla 93.5% | - |
| 🟡 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s8k-h4-d64-bfloat16] | 0.2204 | 19.49 | 0.31 | fla 93.3% | - |
| 🟡 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s16k-h4-d64-float16] | 0.4290 | 20.02 | 0.31 | fla 91.1% | - |
| 🟡 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s16k-h4-d64-bfloat16] | 0.4327 | 19.85 | 0.31 | fla 90.9% | - |
| 🟢 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s32k-h4-d64-float16] | 0.1949 | 88.16 | 1.38 | fla 394.0% | - |
| 🟢 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s32k-h4-d64-bfloat16] | 0.1950 | 88.12 | 1.38 | fla 394.6% | - |
| 🔵 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b1-s4k-h16-d128-float16] | 0.1750 | 58.28 | 0.77 | fla 110.5% | - |
| 🔵 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b1-s4k-h16-d128-bfloat16] | 0.1742 | 58.55 | 0.77 | fla 111.9% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-float16] | 0.2017 | 1.33 | 0.08 | fla 66.3% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-bfloat16] | 0.2049 | 1.31 | 0.08 | fla 68.4% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-float16] | 0.3809 | 1.41 | 0.09 | fla 65.5% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-bfloat16] | 0.3875 | 1.39 | 0.09 | fla 66.7% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-float16] | 0.7228 | 1.49 | 0.09 | fla 67.3% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-bfloat16] | 0.7504 | 1.43 | 0.09 | fla 66.9% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-float16] | 1.4237 | 1.51 | 0.10 | fla 64.6% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-bfloat16] | 1.4680 | 1.46 | 0.09 | fla 65.0% | - |
| 🔵 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b1-h8-d128-bfloat16] | 0.0031 | 0.25 | 0.17 | fla 128.9% | - |
| 🔵 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b1-h16-d128-bfloat16] | 0.0033 | 0.48 | 0.32 | fla 127.2% | - |
| 🔵 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b1-h32-d128-bfloat16] | 0.0036 | 0.87 | 0.59 | fla 129.7% | - |
| 🔵 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b1-h48-d128-bfloat16] | 0.0038 | 1.23 | 0.83 | fla 136.6% | - |
| 🔵 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b1-h64-d128-bfloat16] | 0.0042 | 1.50 | 1.02 | fla 138.2% | - |
| 🟢 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b8-h32-d128-bfloat16] | 0.0087 | 2.89 | 1.95 | fla 167.2% | - |
| 🟢 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b8-h48-d128-bfloat16] | 0.0124 | 3.05 | 2.06 | fla 155.7% | - |
| 🟢 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b8-h64-d128-bfloat16] | 0.0161 | 3.14 | 2.12 | fla 156.5% | - |
| 🔴 | GatedDeltaNetPrefillBHTDFwdOp | test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-float16] | 0.2508 | 34.24 | 0.34 | fla 78.1% | - |
| 🔴 | GatedDeltaNetPrefillBHTDFwdOp | test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-bfloat16] | 0.2526 | 34.01 | 0.34 | fla 78.3% | - |
| 🟡 | GatedDeltaNetPrefillBHTDFwdOp | test_gated_deltanet_prefill_bhtd_bench[bhtd-qwen35-gdn-prefill-b1-s128k-h64-d128-float16] | 17.4198 | 63.12 | 0.62 | fla 89.7% | - |
| 🟡 | GatedDeltaNetPrefillBHTDFwdOp | test_gated_deltanet_prefill_bhtd_bench[bhtd-qwen35-gdn-prefill-b1-s128k-h64-d128-bfloat16] | 17.5479 | 62.66 | 0.61 | fla 88.8% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[fallback-gdn-prefill-b1-s4k-h16-d128-bthd-float16] | 0.0792 | 108.53 | 1.07 | fla 247.7% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[fallback-gdn-prefill-b1-s4k-h16-d128-bthd-bfloat16] | 0.0794 | 108.19 | 1.07 | fla 248.6% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h16-d128-bthd-float16] | 0.3653 | 188.10 | 1.84 | fla 401.0% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h16-d128-bthd-bfloat16] | 0.3711 | 185.18 | 1.82 | fla 396.1% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h16-d128-bthd-float16] | 0.6972 | 197.12 | 1.93 | fla 416.5% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h16-d128-bthd-bfloat16] | 0.7069 | 194.43 | 1.91 | fla 412.5% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h16-d128-bthd-float16] | 1.2572 | 218.65 | 2.14 | fla 459.1% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h16-d128-bthd-bfloat16] | 1.2814 | 214.52 | 2.10 | fla 450.1% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h32-d128-bthd-float16] | 0.6862 | 200.30 | 1.96 | fla 322.8% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h32-d128-bthd-bfloat16] | 0.7005 | 196.21 | 1.92 | fla 316.7% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h32-d128-bthd-float16] | 1.2458 | 220.65 | 2.16 | fla 352.8% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h32-d128-bthd-bfloat16] | 1.2767 | 215.30 | 2.11 | fla 344.7% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h32-d128-bthd-float16] | 2.4458 | 224.77 | 2.20 | fla 357.7% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h32-d128-bthd-bfloat16] | 2.5076 | 219.23 | 2.15 | fla 350.0% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h48-d128-bthd-float16] | 1.0493 | 196.48 | 1.93 | fla 302.0% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h48-d128-bthd-bfloat16] | 1.0652 | 193.54 | 1.90 | fla 296.8% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h48-d128-bthd-float16] | 1.9168 | 215.10 | 2.11 | fla 329.2% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h48-d128-bthd-bfloat16] | 1.9437 | 212.13 | 2.08 | fla 324.5% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h48-d128-bthd-float16] | 3.7766 | 218.35 | 2.14 | fla 333.6% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h48-d128-bthd-bfloat16] | 3.8074 | 216.59 | 2.12 | fla 330.4% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h64-d128-bthd-float16] | 1.2242 | 224.53 | 2.20 | fla 319.0% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h64-d128-bthd-bfloat16] | 1.2532 | 219.35 | 2.15 | fla 311.1% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h64-d128-bthd-float16] | 2.3772 | 231.26 | 2.27 | fla 328.8% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h64-d128-bthd-bfloat16] | 2.4273 | 226.49 | 2.22 | fla 320.5% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h64-d128-bthd-float16] | 4.6645 | 235.72 | 2.31 | fla 335.0% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h64-d128-bthd-bfloat16] | 4.7856 | 229.75 | 2.25 | fla 325.8% | - |
| 🔵 | GeFwdOp | test_comparison_bench[ge-1024x4096-float16-ge] | 0.0076 | 0.55 | 2.77 | torch 102.5%, torch-compile 102.5% | - |
| 🔵 | GeFwdOp | test_ge_manifest_bench[hidden-state-prefill-float16] | 0.0132 | 0.64 | 3.19 | torch 100.4%, torch-compile 100.4% | - |
| 🔵 | GeFwdOp | test_ge_manifest_bench[hidden-state-prefill-bfloat16] | 0.0130 | 0.64 | 3.22 | torch 100.7%, torch-compile 100.2% | - |
| 🟡 | GeFwdOp | test_ge_manifest_bench[hidden-state-prefill-float32] | 0.0224 | 0.37 | 3.37 | torch 99.9%, torch-compile 111.1% | - |
| 🔴 | GeFwdOp | test_ge_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.81 | 2.42 | torch 294.8%, torch-compile 74.5% | - |
| 🔴 | GeFwdOp | test_ge_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.81 | 2.43 | torch 300.0%, torch-compile 75.8% | - |
| 🟡 | GeFwdOp | test_ge_manifest_bench[cnn-feat-broadcast-float32] | 0.0207 | 0.62 | 3.10 | torch 226.1%, torch-compile 88.6% | - |
| 🔵 | GeluAndMulFwdOp | test_gelu_and_mul_bench[ffn-gelu-prefill-float16] | 0.0550 | 3.20 | 3.20 | flashinfer 190.8%, torch-ref 368.8%, torch-compile 109.6% | - |
| 🔵 | GeluAndMulFwdOp | test_gelu_and_mul_bench[ffn-gelu-prefill-bfloat16] | 0.0595 | 2.96 | 2.96 | flashinfer 178.2%, torch-ref 344.2%, torch-compile 102.6% | - |
| 🟡 | GeluAndMulFwdOp | test_gelu_and_mul_bench[ffn-gelu-decode-bfloat16] | 0.0015 | 0.06 | 0.06 | flashinfer 433.3%, torch-ref 206.3%, torch-compile 93.8% | - |
| 🟡 | GeluFwdOp | test_gelu_manifest_bench[llama-8b-ffn-prefill-float16] | 0.0527 | 2.78 | 2.23 | torch 90.5%, torch-compile 102.3% | - |
| 🟡 | GeluFwdOp | test_gelu_manifest_bench[llama-8b-ffn-prefill-bfloat16] | 0.0553 | 2.66 | 2.13 | torch 88.6%, torch-compile 100.9% | - |
| 🔵 | GeluFwdOp | test_gelu_manifest_bench[llama-8b-ffn-decode-bfloat16] | 0.0014 | 0.05 | 0.04 | torch 120.8%, torch-compile 102.2% | - |
| 🔵 | GeluTanhAndMulFwdOp | test_gelu_tanh_and_mul_bench[ffn-gelu-tanh-prefill-float16] | 0.0477 | 6.15 | 3.69 | flashinfer 118.7%, torch-ref 402.4%, torch-compile 108.1% | - |
| 🔵 | GeluTanhAndMulFwdOp | test_gelu_tanh_and_mul_bench[ffn-gelu-tanh-prefill-bfloat16] | 0.0493 | 5.95 | 3.57 | flashinfer 116.9%, torch-ref 391.8%, torch-compile 106.6% | - |
| 🔵 | GeluTanhAndMulFwdOp | test_gelu_tanh_and_mul_bench[ffn-gelu-tanh-decode-bfloat16] | 0.0015 | 0.10 | 0.06 | flashinfer 297.8%, torch-ref 206.6%, torch-compile 101.1% | - |
| 🟢 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-decode-gate-up-per-tensor-float8_e4m3fn] | 0.1162 | 33.36 | 0.14 | torch-scaled-mm 208.6% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-decode-down-per-tensor-float8_e4m3fn] | 0.0253 | 148.28 | 0.66 | torch-scaled-mm 965.8%, deepgemm 40.9% | - |
| 🟢 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-prefill-gate-up-per-tensor-float8_e4m3fn] | 0.5108 | 242.77 | 0.12 | torch-scaled-mm 672.4% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-prefill-down-per-tensor-float8_e4m3fn] | 0.2109 | 570.32 | 0.39 | torch-scaled-mm 1585.6%, deepgemm 50.1% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-decode-gate-up-block128-float8_e4m3fn] | 0.1481 | 26.17 | 0.12 | torch-scaled-mm 188.7%, flashinfer-fp8-blockscale-sm90 8.7% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-decode-down-block128-float8_e4m3fn] | 0.0377 | 99.61 | 0.46 | torch-scaled-mm 740.3%, flashinfer-fp8-blockscale-sm90 24.5% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-prefill-gate-up-block128-float8_e4m3fn] | 0.3870 | 320.45 | 0.16 | torch-scaled-mm 912.7%, flashinfer-fp8-blockscale-sm90 36.4% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-prefill-down-block128-float8_e4m3fn] | 0.4457 | 269.80 | 0.19 | torch-scaled-mm 762.3%, flashinfer-fp8-blockscale-sm90 32.1% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-prefill-attn-proj-block128-float8_e4m3fn] | 0.7704 | 312.21 | 0.12 | torch-scaled-mm 867.0%, flashinfer-fp8-blockscale-sm90 27.9% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[k-dominant-7168x16384-block128-float8_e4m3fn] | 3.5879 | 268.14 | 0.07 | torch-scaled-mm 736.3%, flashinfer-fp8-blockscale-sm90 21.5% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[wide-n-24576-block128-float8_e4m3fn] | 1.0266 | 301.22 | 0.24 | torch-scaled-mm 830.1%, flashinfer-fp8-blockscale-sm90 37.2% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[small-batch-down-m8-per-tensor-float8_e4m3fn] | 0.0267 | 8.81 | 0.56 | torch-scaled-mm 625.0%, deepgemm 31.1% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[gemv-down-m1-per-tensor-float8_e4m3fn] | 0.0258 | 1.14 | 0.57 | torch-scaled-mm 504.8%, deepgemm 39.2% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[gemv-down-m1-block128-float8_e4m3fn] | 0.0446 | 0.66 | 0.34 | torch-scaled-mm 368.5%, flashinfer-fp8-blockscale-sm90 17.4% | - |
| 🟢 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-decode-gate-up-per-tensor-bias-float8_e4m3fn] | 0.1166 | 33.24 | 0.14 | torch-scaled-mm 212.8% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[square-1k-nn-float16] | 0.0145 | 148.47 | 0.43 | torch-cublas 50.2%, flaggems 81.6% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[square-1k-nn-bfloat16] | 0.0145 | 148.48 | 0.44 | torch-cublas 49.8%, flaggems 79.2% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[ds-v3-decode-gate-up-bfloat16] | 0.0678 | 57.18 | 0.48 | torch-cublas 25.4%, deepgemm 31.4% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[ds-v3-decode-down-bfloat16] | 0.0246 | 152.72 | 1.29 | torch-cublas 53.6%, deepgemm 55.9% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[ds-v3-prefill-gate-up-bfloat16] | 0.3370 | 368.03 | 0.32 | torch-cublas 52.4%, deepgemm 53.7% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[ds-v3-prefill-down-bfloat16] | 0.3214 | 374.22 | 0.33 | torch-cublas 56.1%, deepgemm 55.9% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[ds-v3-prefill-attn-proj-float16] | 0.5448 | 441.45 | 0.28 | torch-cublas 61.8% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[ds-v3-prefill-attn-proj-bfloat16] | 0.5398 | 445.56 | 0.28 | torch-cublas 61.4%, deepgemm 61.2% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[k-dominant-7168x16384-bfloat16] | 2.0598 | 467.06 | 0.21 | torch-cublas 61.6%, deepgemm 61.3% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[wide-n-24576-bfloat16] | 0.9017 | 342.93 | 0.32 | torch-cublas 50.2%, deepgemm 49.0% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[mid-m16-attn-bfloat16] | 0.0658 | 14.29 | 0.90 | torch-cublas 37.3%, deepgemm 51.6% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[mid-m32-attn-bfloat16] | 0.0662 | 28.38 | 0.90 | torch-cublas 36.7%, deepgemm 46.1% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[mid-m64-down-bfloat16] | 0.0207 | 90.90 | 1.48 | torch-cublas 63.9%, deepgemm 65.2% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[mid-m96-gate-up-bfloat16] | 0.0687 | 42.29 | 0.47 | torch-cublas 24.6%, deepgemm 31.9% | - |
| 🔴 | GemmW4A16FwdOp | test_gemm_w4a16_bench[compile-smoke-square-64x64x128-float16] | 0.0043 | 0.24 | 0.01 | torch-dequantized-matmul 62.7% | - |
| 🔴 | GemmW4A16FwdOp | test_gemm_w4a16_bench[compile-smoke-rect-128x256x256-float16] | 0.0059 | 2.87 | 0.03 | torch-dequantized-matmul 52.5% | - |
| 🔴 | GemmW4A16FwdOp | test_gemm_w4a16_bench[decode-l2-resident-ish-float16] | 0.0330 | 4.06 | 1.10 | torch-dequantized-matmul 141.6%, marlin-fp32 66.2%, marlin-fp16 65.8% | - |
| 🔴 | GemmW4A16FwdOp | test_gemm_w4a16_bench[decode-hbm-streaming-threshold-float16] | 0.0606 | 4.43 | 1.19 | torch-dequantized-matmul 123.4%, marlin-fp32 62.4%, marlin-fp16 62.7% | - |
| 🔴 | GemmW4A16FwdOp | test_gemm_w4a16_bench[decode-non-power2-low-cta-float16] | 0.0745 | 3.94 | 1.06 | torch-dequantized-matmul 117.5%, marlin-fp32 54.6%, marlin-fp16 54.5% | - |
| 🔴 | GemmW4A16FwdOp | test_gemm_w4a16_bench[decode-long-k-pressure-float16] | 0.2834 | 4.74 | 1.28 | torch-dequantized-matmul 113.9%, marlin-fp32 49.9%, marlin-fp16 49.7% | - |
| 🔵 | GroupNormFwdOp | test_group_norm_bench[image-g32-affine-float16] | 0.0037 | 1.40 | 1.12 | flaggems 107.7%, torch 407.8%, torch-compile 138.5% | - |
| 🔵 | GroupNormFwdOp | test_group_norm_bench[image-g32-affine-bfloat16] | 0.0037 | 1.42 | 1.14 | flaggems 109.5%, torch 415.6%, torch-compile 136.5% | - |
| 🔴 | GroupNormFwdOp | test_group_norm_bench[wider-channel-g32-affine-float16] | 0.0060 | 0.67 | 0.54 | flaggems 66.7%, torch 273.4%, torch-compile 72.6% | - |
| 🔴 | GroupNormFwdOp | test_group_norm_bench[tail-spatial-g16-affine-float16] | 0.0061 | 0.38 | 0.30 | flaggems 66.8%, torch 252.1%, torch-compile 68.4% | - |
| 🔵 | GroupNormFwdOp | test_group_norm_no_affine_bench[image-g32-float16] | 0.0036 | 0.89 | 1.18 | flaggems 100.9%, torch 372.1%, torch-compile 116.7% | - |
| 🔵 | GroupNormFwdOp | test_group_norm_no_affine_bench[image-g32-bfloat16] | 0.0036 | 0.89 | 1.18 | flaggems 100.9%, torch 372.1%, torch-compile 119.8% | - |
| 🔴 | GroupNormFwdOp | test_group_norm_no_affine_bench[wider-channel-g32-float16] | 0.0048 | 0.50 | 0.67 | flaggems 72.7%, torch 295.4%, torch-compile 80.7% | - |
| 🔴 | GroupNormFwdOp | test_group_norm_no_affine_bench[tail-spatial-g16-float16] | 0.0052 | 0.27 | 0.35 | flaggems 69.3%, torch 257.1%, torch-compile 67.5% | - |
| 🟡 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-8b-short-float16] | 0.2029 | 105.86 | 0.33 | fa3 81.9% | - |
| 🔴 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-8b-short-bfloat16] | 0.4154 | 51.69 | 0.16 | fa3 39.8% | - |
| 🔴 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-8b-long-float16] | 0.8322 | 206.43 | 0.16 | fa3 71.2% | - |
| 🔴 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-8b-long-bfloat16] | 1.2427 | 138.25 | 0.11 | fa3 47.4% | - |
| 🟡 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-70b-short-float16] | 0.1961 | 109.49 | 0.30 | fa3 81.2% | - |
| 🔴 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-70b-short-bfloat16] | 0.4092 | 52.47 | 0.14 | fa3 38.8% | - |
| 🔴 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-70b-long-float16] | 0.8080 | 212.61 | 0.15 | fa3 71.8% | - |
| 🔴 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 1.0192 | 168.56 | 0.12 | fa3 56.6% | - |
| 🔴 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-8b-p64-float16] | 0.1669 | 12.87 | 0.10 | flashinfer 75.0% | - |
| 🔵 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-8b-long-p64-float16] | 0.2206 | 19.47 | 0.61 | flashinfer 135.8% | - |
| 🔴 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[throughput-8b-p64-float16] | 0.2518 | 8.53 | 0.04 | flashinfer 59.9% | - |
| 🟡 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-70b-p64-float16] | 0.0496 | 21.63 | 0.34 | flashinfer 89.8% | - |
| 🔴 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-8b-p256-float16] | 0.1683 | 12.76 | 0.10 | fa3 48.3%, flashinfer 74.5% | - |
| 🔴 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-70b-p256-float16] | 0.0685 | 15.68 | 0.25 | fa3 53.8%, flashinfer 83.5% | - |
| 🔴 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-405b-p256-float16] | 0.0563 | 19.06 | 0.30 | fa3 47.1% | - |
| 🔴 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-8b-p64-softcap50-float16] | 0.1765 | 12.17 | 0.10 | flashinfer 71.0% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-8b-4k-float16] | 0.1513 | 14.20 | 3.55 | fa3 101.8%, flashinfer 148.0% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-8b-4k-bfloat16] | 0.1503 | 14.29 | 3.58 | fa3 101.8%, flashinfer 170.7% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-8b-32k-float16] | 0.2579 | 16.65 | 4.16 | fa3 104.3%, flashinfer 166.3% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-8b-32k-bfloat16] | 0.2567 | 16.73 | 4.18 | fa3 104.3%, flashinfer 193.3% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-70b-4k-float16] | 0.0793 | 27.09 | 3.39 | fa3 107.8%, flashinfer 251.6% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-70b-4k-bfloat16] | 0.0791 | 27.16 | 3.40 | fa3 107.7%, flashinfer 287.6% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-70b-32k-float16] | 0.1382 | 31.08 | 3.89 | fa3 108.8%, flashinfer 279.8% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-70b-32k-bfloat16] | 0.1376 | 31.22 | 3.90 | fa3 108.5%, flashinfer 321.1% | - |
| 🟢 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-8b-4k-softcap50-float16] | 0.1616 | 13.29 | 3.33 | torch-sdpa 8246.3% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-1k-float16] | 0.0070 | 2.40 | 0.30 | fa3 249.1%, flashinfer 139.0% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-4k-float16] | 0.0096 | 6.99 | 0.88 | fa3 220.3%, flashinfer 120.7% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-8k-float16] | 0.0132 | 10.18 | 1.27 | fa3 176.2%, flashinfer 106.8% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-16k-float16] | 0.0182 | 14.77 | 1.85 | fa3 154.4%, flashinfer 120.5% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-32k-float16] | 0.0283 | 18.95 | 2.37 | fa3 132.6%, flashinfer 122.4% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-64k-float16] | 0.0456 | 23.56 | 2.94 | fa3 126.3%, flashinfer 116.4% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-128k-float16] | 0.0764 | 28.10 | 3.51 | fa3 121.5%, flashinfer 108.8% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-256k-float16] | 0.1362 | 31.54 | 3.94 | fa3 118.8%, flashinfer 104.3% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-8b-short-float16] | 0.0371 | 231.61 | 1.13 | fa3 86.0%, flashinfer 106.5% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-8b-short-bfloat16] | 0.0369 | 233.02 | 1.14 | fa3 86.5%, flashinfer 106.7% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-8b-long-float16] | 0.1627 | 422.40 | 0.52 | fa3 82.9%, flashinfer 99.2% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-8b-long-bfloat16] | 0.1613 | 426.13 | 0.52 | fa3 82.5%, flashinfer 100.0% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-70b-short-float16] | 0.0382 | 225.11 | 0.99 | fa3 83.7%, flashinfer 102.6% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-70b-short-bfloat16] | 0.0380 | 226.15 | 0.99 | fa3 83.6%, flashinfer 103.1% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-70b-long-float16] | 0.1627 | 422.48 | 0.46 | fa3 82.3%, flashinfer 99.6% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-70b-long-bfloat16] | 0.1617 | 424.99 | 0.47 | fa3 81.7%, flashinfer 98.8% | - |
| 🔵 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-8b-prefill-dense-float16] | 0.0373 | 230.87 | 1.13 | torch-ref 2952.7%, flashinfer 105.3% | - |
| 🔵 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-8b-prefill-dense-bfloat16] | 0.0369 | 233.27 | 1.14 | torch-ref 2984.3%, flashinfer 106.5% | - |
| 🔵 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-8b-prefill-dense-sm-scale-0.125-float16] | 0.0371 | 232.26 | 1.13 | torch-ref 2970.8%, flashinfer 106.0% | - |
| 🔵 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-8b-prefill-dense-softcap50-float16] | 0.0421 | 204.53 | 1.00 | torch-ref 3081.2%, flashinfer 108.6% | - |
| 🔵 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-8b-prefill-dense-q-lt-kv-float16] | 0.1263 | 510.01 | 0.40 | torch-ref 3241.7%, flashinfer 100.1% | - |
| 🔵 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-8b-prefill-dense-q-lt-kv-bfloat16] | 0.1243 | 518.28 | 0.40 | torch-ref 3298.3%, flashinfer 100.7% | - |
| 🟡 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-70b-prefill-dense-q-lt-kv-float16] | 0.1252 | 514.57 | 0.27 | torch-ref 3003.4%, flashinfer 99.9% | - |
| 🟡 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-70b-prefill-dense-q-lt-kv-bfloat16] | 0.1238 | 520.56 | 0.27 | torch-ref 3039.4%, flashinfer 99.8% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s896-float16] | 0.0453 | 290.49 | 0.20 | torch-sdpa-dequant 202.8%, fa3 63.1% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s896-bfloat16] | 0.0454 | 289.87 | 0.20 | torch-sdpa-dequant 204.0%, fa3 62.4% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s1792-float16] | 0.1288 | 408.33 | 0.14 | torch-sdpa-dequant 176.2%, fa3 66.7% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s1792-bfloat16] | 0.1290 | 407.98 | 0.14 | torch-sdpa-dequant 174.8%, fa3 66.9% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s3584-float16] | 0.7495 | 561.60 | 0.09 | torch-sdpa-dequant 140.5%, fa3 70.7% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s3584-bfloat16] | 0.7495 | 561.55 | 0.09 | torch-sdpa-dequant 140.2%, fa3 70.6% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s7168-float16] | 2.8449 | 591.81 | 0.05 | torch-sdpa-dequant 120.6%, fa3 71.3% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s7168-bfloat16] | 2.8453 | 591.73 | 0.05 | torch-sdpa-dequant 120.6%, fa3 71.1% | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-prefill-paged-fullattn-b8-prefix32k-chunk1k-p64-partial-rope64-float16] | 60.6283 | 147.35 | 0.04 | - | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-prefill-paged-fullattn-mixed-b8-p64-partial-rope64-float16] | 30.7355 | 107.99 | 0.04 | - | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-prefill-paged-b8-prefix4k-chunk512-p64-full-rope-float16] | 1.9500 | 149.79 | 0.12 | - | - |
| 🟡 | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[gqa-prefill-paged-softcap50-b4-prefix4k-chunk512-p64-float16] | 0.1499 | 121.80 | 0.10 | fa3 91.2% | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-prefill-paged-fp8-cache-b8-prefix32k-chunk1k-p64-float16] | 55.9919 | 159.55 | 0.05 | - | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-prefill-paged-fp8-cache-b8-prefix4k-chunk512-p64-float16] | 2.0061 | 145.60 | 0.12 | - | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[gqa-prefill-paged-fp8-cache-softcap50-b4-prefix4k-chunk512-p64-float16] | 0.2071 | 88.14 | 0.07 | - | - |
| 🔴 | GroupedQueryAttentionPrefillVarlenFwdOp | test_gqa_prefill_varlen_fwd_bench[llama-8b-prefill-varlen-uniform-fp16] | 0.1251 | 206.15 | 0.40 | torch-ref 1629.5%, fa3 57.1% | - |
| 🔴 | GroupedQueryAttentionPrefillVarlenFwdOp | test_gqa_prefill_varlen_fwd_bench[llama-8b-prefill-varlen-mixed-fp16] | 0.1405 | 143.42 | 0.28 | torch-ref 1195.5%, fa3 43.7% | - |
| 🔴 | GroupedQueryAttentionPrefillVarlenFwdOp | test_gqa_prefill_varlen_fwd_bench[llama-70b-prefill-varlen-q-lt-kv-bf16] | 0.1963 | 218.93 | 0.24 | torch-ref 1408.7%, fa3 50.2% | - |
| 🟡 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-8b-short-w256-float16] | 0.0398 | 162.47 | 1.05 | fa3 86.0%, flashinfer 103.5% | - |
| 🟡 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0397 | 162.86 | 1.06 | fa3 85.5%, flashinfer 103.4% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-8b-long-w1024-float16] | 0.1529 | 337.38 | 0.55 | fa3 79.0%, flashinfer 101.6% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.1517 | 340.05 | 0.55 | fa3 78.0%, flashinfer 100.8% | - |
| 🟡 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-70b-short-w256-float16] | 0.0396 | 163.52 | 0.95 | fa3 86.5%, flashinfer 103.8% | - |
| 🟡 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-70b-short-w256-bfloat16] | 0.0395 | 163.79 | 0.96 | fa3 86.2%, flashinfer 103.4% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-70b-long-w1024-float16] | 0.1528 | 337.59 | 0.49 | fa3 78.5%, flashinfer 100.2% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.1516 | 340.27 | 0.50 | fa3 78.1%, flashinfer 99.9% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-float16] | 0.0569 | 113.61 | 0.74 | fa3 82.9%, flashinfer 72.8% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0567 | 114.12 | 0.74 | fa3 83.1%, flashinfer 72.6% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-float16] | 0.3518 | 293.27 | 0.48 | fa3 77.1%, flashinfer 78.6% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.3492 | 295.46 | 0.48 | fa3 77.3%, flashinfer 78.3% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-float16] | 0.0931 | 138.96 | 0.81 | fa3 89.6%, flashinfer 74.2% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-bfloat16] | 0.0930 | 139.10 | 0.81 | fa3 89.7%, flashinfer 74.6% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-float16] | 0.6677 | 309.04 | 0.45 | fa3 79.1%, flashinfer 77.6% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.6661 | 309.81 | 0.45 | fa3 79.1%, flashinfer 77.6% | - |
| 🔵 | GtFwdOp | test_comparison_bench[gt-1024x4096-float16-gt] | 0.0076 | 0.55 | 2.75 | torch 102.5%, torch-compile 102.1% | - |
| 🔵 | GtFwdOp | test_gt_manifest_bench[hidden-state-prefill-float16] | 0.0130 | 0.65 | 3.23 | torch 101.2%, torch-compile 101.2% | - |
| 🔵 | GtFwdOp | test_gt_manifest_bench[hidden-state-prefill-bfloat16] | 0.0130 | 0.64 | 3.22 | torch 100.7%, torch-compile 101.0% | - |
| 🔵 | GtFwdOp | test_gt_manifest_bench[hidden-state-prefill-float32] | 0.0223 | 0.38 | 3.38 | torch 100.0%, torch-compile 112.2% | - |
| 🔴 | GtFwdOp | test_gt_manifest_bench[cnn-feat-broadcast-float16] | 0.0160 | 0.80 | 2.41 | torch 302.6%, torch-compile 74.8% | - |
| 🔴 | GtFwdOp | test_gt_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.81 | 2.42 | torch 308.0%, torch-compile 75.4% | - |
| 🟡 | GtFwdOp | test_gt_manifest_bench[cnn-feat-broadcast-float32] | 0.0209 | 0.61 | 3.07 | torch 230.8%, torch-compile 87.8% | - |
| 🟡 | HardsigmoidFwdOp | test_hardsigmoid_manifest_bench[mbv3-se-gate-float16] | 0.0016 | 0.01 | 0.02 | torch 105.9%, torch-compile 82.4% | - |
| 🟡 | HardsigmoidFwdOp | test_hardsigmoid_manifest_bench[mbv3-se-gate-bfloat16] | 0.0016 | 0.01 | 0.02 | torch 105.9%, torch-compile 82.4% | - |
| 🟡 | HardsigmoidFwdOp | test_hardsigmoid_manifest_bench[mbv3-se-gate-deep-float16] | 0.0017 | 0.06 | 0.07 | torch 88.4%, torch-compile 88.5% | - |
| 🟡 | HardsigmoidFwdOp | test_hardsigmoid_manifest_bench[mbv3-se-gate-deep-bfloat16] | 0.0017 | 0.06 | 0.07 | torch 88.4%, torch-compile 90.3% | - |
| 🟡 | HardswishFwdOp | test_hardswish_manifest_bench[mbv3-stage2-float16] | 0.0129 | 2.99 | 2.99 | torch 90.1%, torch-compile 89.3% | - |
| 🟡 | HardswishFwdOp | test_hardswish_manifest_bench[mbv3-stage2-bfloat16] | 0.0132 | 2.92 | 2.92 | torch 87.9%, torch-compile 87.3% | - |
| 🟡 | HardswishFwdOp | test_hardswish_manifest_bench[mbv3-stage3-float16] | 0.0089 | 2.72 | 2.72 | torch 91.7%, torch-compile 91.0% | - |
| 🟡 | HardswishFwdOp | test_hardswish_manifest_bench[mbv3-stage3-bfloat16] | 0.0090 | 2.67 | 2.67 | torch 90.4%, torch-compile 89.4% | - |
| 🔵 | HardtanhFwdOp | test_hardtanh_manifest_bench[bounded-hidden-float16] | 0.0104 | 0.81 | 3.24 | torch 108.6%, torch-compile 100.3% | - |
| 🔵 | HardtanhFwdOp | test_hardtanh_manifest_bench[bounded-hidden-bfloat16] | 0.0104 | 0.81 | 3.23 | torch 102.8%, torch-compile 100.6% | - |
| 🔵 | HardtanhFwdOp | test_hardtanh_manifest_bench[bounded-conv-feat-float16] | 0.0146 | 0.88 | 3.52 | torch 111.0%, torch-compile 100.4% | - |
| 🔵 | HardtanhFwdOp | test_hardtanh_manifest_bench[bounded-conv-feat-bfloat16] | 0.0146 | 0.88 | 3.51 | torch 104.0%, torch-compile 101.1% | - |
| 🔵 | InfNormFwdOp | test_inf_norm_bench[hidden-state-inf-float16] | 0.0073 | 2.29 | 2.29 | flaggems 104.4%, torch 680.3%, torch-compile 145.0% | - |
| 🔵 | InfNormFwdOp | test_inf_norm_bench[hidden-state-inf-bfloat16] | 0.0074 | 2.28 | 2.28 | flaggems 106.5%, torch 681.7%, torch-compile 150.4% | - |
| 🔵 | InfNormFwdOp | test_inf_norm_bench[long-seq-inf-bfloat16] | 0.0040 | 1.04 | 1.04 | flaggems 340.6%, torch 430.2%, torch-compile 123.9% | - |
| 🔴 | InfNormFwdOp | test_inf_norm_bench[3d-multidim-reduce-float16] | 0.0112 | 0.37 | 0.37 | flaggems 113.4%, torch 171.2%, torch-compile 43.9% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[image-affine-float16] | 0.0035 | 1.52 | 1.21 | flaggems 107.4%, torch 599.1%, torch-compile 88.9% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[image-affine-bfloat16] | 0.0034 | 1.53 | 1.23 | flaggems 108.4%, torch 603.8%, torch-compile 87.8% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[wider-channel-affine-float16] | 0.0035 | 1.16 | 0.93 | flaggems 102.8%, torch 595.4%, torch-compile 82.4% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[tail-spatial-affine-float16] | 0.0027 | 0.43 | 0.34 | flaggems 104.8%, torch 411.9%, torch-compile 89.3% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[image-float16] | 0.0034 | 0.93 | 1.24 | flaggems 102.0%, torch 501.1%, torch-compile 86.8% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[image-bfloat16] | 0.0034 | 0.93 | 1.24 | flaggems 102.8%, torch 502.8%, torch-compile 85.9% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[wider-channel-float16] | 0.0033 | 0.72 | 0.96 | flaggems 99.0%, torch 486.4%, torch-compile 83.6% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[tail-spatial-float16] | 0.0025 | 0.27 | 0.36 | flaggems 103.8%, torch 326.4%, torch-compile 91.1% | - |
| 🔵 | IsfiniteFwdOp | test_isfinite_bench[elementwise-16M-float16] | 0.0147 | 1.14 | 3.43 | torch 429.6%, torch-compile 102.4% | - |
| 🔵 | IsfiniteFwdOp | test_isfinite_bench[elementwise-16M-bfloat16] | 0.0147 | 1.14 | 3.43 | torch 431.5%, torch-compile 102.4% | - |
| 🟡 | IsfiniteFwdOp | test_isfinite_bench[elementwise-16M-float32] | 0.0234 | 0.72 | 3.58 | torch 410.4%, torch-compile 99.8% | - |
| 🔵 | IsfiniteFwdOp | test_isfinite_bench[elementwise-256M-float16] | 0.1862 | 1.44 | 4.32 | torch 489.9%, torch-compile 105.6% | - |
| 🔵 | IsfiniteFwdOp | test_isfinite_bench[elementwise-256M-bfloat16] | 0.1862 | 1.44 | 4.32 | torch 491.5%, torch-compile 105.6% | - |
| 🔵 | IsinfFwdOp | test_isinf_bench[elementwise-16M-float16] | 0.0148 | 1.14 | 3.41 | torch 212.4%, torch-compile 102.6% | - |
| 🔵 | IsinfFwdOp | test_isinf_bench[elementwise-16M-bfloat16] | 0.0148 | 1.14 | 3.41 | torch 213.0%, torch-compile 103.0% | - |
| 🟡 | IsinfFwdOp | test_isinf_bench[elementwise-16M-float32] | 0.0234 | 0.72 | 3.58 | torch 243.8%, torch-compile 99.7% | - |
| 🔵 | IsinfFwdOp | test_isinf_bench[elementwise-256M-float16] | 0.1862 | 1.44 | 4.33 | torch 241.7%, torch-compile 106.8% | - |
| 🔵 | IsinfFwdOp | test_isinf_bench[elementwise-256M-bfloat16] | 0.1857 | 1.45 | 4.34 | torch 242.8%, torch-compile 107.7% | - |
| 🔵 | IsnanFwdOp | test_isnan_bench[elementwise-16M-float16] | 0.0147 | 1.14 | 3.42 | torch 104.5%, torch-compile 102.3% | - |
| 🔵 | IsnanFwdOp | test_isnan_bench[elementwise-16M-bfloat16] | 0.0147 | 1.14 | 3.42 | torch 105.4%, torch-compile 102.6% | - |
| 🟡 | IsnanFwdOp | test_isnan_bench[elementwise-16M-float32] | 0.0235 | 0.72 | 3.58 | torch 100.0%, torch-compile 99.6% | - |
| 🔵 | IsnanFwdOp | test_isnan_bench[elementwise-256M-float16] | 0.1863 | 1.44 | 4.32 | torch 108.2%, torch-compile 105.9% | - |
| 🔵 | IsnanFwdOp | test_isnan_bench[elementwise-256M-bfloat16] | 0.1863 | 1.44 | 4.32 | torch 109.5%, torch-compile 106.6% | - |
| 🔵 | L1NormFwdOp | test_l1_norm_bench[hidden-state-l1-float16] | 0.0074 | 2.28 | 2.28 | flaggems 204.3%, torch 671.3%, torch-compile 113.5% | - |
| 🔵 | L1NormFwdOp | test_l1_norm_bench[hidden-state-l1-bfloat16] | 0.0074 | 2.28 | 2.28 | flaggems 208.7%, torch 675.7%, torch-compile 114.8% | - |
| 🔵 | L1NormFwdOp | test_l1_norm_bench[long-seq-l1-bfloat16] | 0.0039 | 1.07 | 1.07 | flaggems 943.7%, torch 432.9%, torch-compile 115.6% | - |
| 🔴 | L1NormFwdOp | test_l1_norm_bench[3d-multidim-reduce-float16] | 0.0113 | 0.37 | 0.37 | flaggems 218.2%, torch 171.3%, torch-compile 41.2% | - |
| 🔵 | L2NormFwdOp | test_l2_norm_bench[hidden-state-l2-float16] | 0.0075 | 2.25 | 2.25 | flaggems 105.6%, torch 665.7%, torch-compile 116.3% | - |
| 🔵 | L2NormFwdOp | test_l2_norm_bench[hidden-state-l2-bfloat16] | 0.0074 | 2.26 | 2.26 | flaggems 106.0%, torch 670.8%, torch-compile 118.5% | - |
| 🔵 | L2NormFwdOp | test_l2_norm_bench[long-seq-l2-bfloat16] | 0.0040 | 1.05 | 1.05 | flaggems 338.4%, torch 423.2%, torch-compile 112.0% | - |
| 🔴 | L2NormFwdOp | test_l2_norm_bench[3d-multidim-reduce-float16] | 0.0113 | 0.37 | 0.37 | flaggems 119.5%, torch 170.6%, torch-compile 41.0% | - |
| 🟡 | LayerNormFwdOp | test_layer_norm_bench[llama-8b-prefill-float16] | 0.0137 | 3.06 | 2.45 | flaggems 95.7%, flashinfer 155.6%, torch 155.1%, torch-compile 168.9% | - |
| 🟡 | LayerNormFwdOp | test_layer_norm_bench[llama-8b-prefill-bfloat16] | 0.0149 | 2.81 | 2.25 | flaggems 92.5%, flashinfer 143.6%, torch 142.9%, torch-compile 171.5% | - |
| 🔵 | LayerNormFwdOp | test_layer_norm_bench[llama-8b-decode-bfloat16] | 0.0027 | 0.01 | 0.01 | flaggems 103.5%, flashinfer 112.9%, torch 411.8%, torch-compile 100.0% | - |
| 🟡 | LayerNormFwdOp | test_layer_norm_bench[llama-70b-prefill-float16] | 0.0260 | 3.23 | 2.59 | flaggems 99.0%, flashinfer 179.3%, torch 155.2%, torch-compile 118.5% | - |
| 🔵 | LayerNormFwdOp | test_layer_norm_bench[llama-70b-prefill-bfloat16] | 0.0265 | 3.17 | 2.53 | flaggems 104.6%, flashinfer 176.0%, torch 152.8%, torch-compile 126.1% | - |
| 🔵 | LayerNormFwdOp | test_layer_norm_bench[llama-70b-decode-bfloat16] | 0.0034 | 0.01 | 0.02 | flaggems 123.4%, flashinfer 120.6%, torch 584.1%, torch-compile 107.5% | - |
| 🟡 | LayerNormFwdOp | test_layer_norm_bench[llama-405b-prefill-float16] | 0.0502 | 3.34 | 2.67 | flaggems 96.2%, flashinfer 156.0%, torch 146.8%, torch-compile 93.1% | - |
| 🟡 | LayerNormFwdOp | test_layer_norm_bench[llama-405b-prefill-bfloat16] | 0.0509 | 3.30 | 2.64 | flaggems 99.1%, flashinfer 153.9%, torch 146.8%, torch-compile 99.8% | - |
| 🔵 | LayerNormFwdOp | test_layer_norm_bench[llama-405b-decode-bfloat16] | 0.0043 | 0.02 | 0.03 | flaggems 142.5%, flashinfer 141.8%, torch 884.3%, torch-compile 128.4% | - |
| 🔵 | LeFwdOp | test_comparison_bench[le-1024x4096-float16-le] | 0.0076 | 0.55 | 2.75 | torch 101.3%, torch-compile 101.3% | - |
| 🟡 | LeFwdOp | test_le_manifest_bench[hidden-state-prefill-float16] | 0.0130 | 0.64 | 3.22 | torch 99.3%, torch-compile 99.0% | - |
| 🔵 | LeFwdOp | test_le_manifest_bench[hidden-state-prefill-bfloat16] | 0.0131 | 0.64 | 3.20 | torch 100.7%, torch-compile 100.2% | - |
| 🟡 | LeFwdOp | test_le_manifest_bench[hidden-state-prefill-float32] | 0.0225 | 0.37 | 3.36 | torch 100.0%, torch-compile 99.7% | - |
| 🔴 | LeFwdOp | test_le_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.81 | 2.42 | torch 311.4%, torch-compile 74.7% | - |
| 🔴 | LeFwdOp | test_le_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.81 | 2.42 | torch 317.0%, torch-compile 74.5% | - |
| 🟡 | LeFwdOp | test_le_manifest_bench[cnn-feat-broadcast-float32] | 0.0209 | 0.61 | 3.07 | torch 235.3%, torch-compile 88.5% | - |
| 🔵 | LeakyReluFwdOp | test_leaky_relu_manifest_bench[gan-feat-float16] | 0.0184 | 1.82 | 3.65 | torch 100.4%, torch-compile 100.3% | - |
| 🟡 | LeakyReluFwdOp | test_leaky_relu_manifest_bench[gan-feat-bfloat16] | 0.0185 | 1.82 | 3.63 | torch 100.0%, torch-compile 99.8% | - |
| 🔵 | LeakyReluFwdOp | test_leaky_relu_manifest_bench[gan-feat-deep-float16] | 0.0104 | 1.62 | 3.24 | torch 100.3%, torch-compile 100.3% | - |
| 🔵 | LeakyReluFwdOp | test_leaky_relu_manifest_bench[gan-feat-deep-bfloat16] | 0.0103 | 1.62 | 3.25 | torch 100.6%, torch-compile 100.3% | - |
| 🔵 | LerpFwdOp | test_binary_arith_bench[lerp-1024x4096-float16-float16-LerpFwdOp-<lambda>-normal] | 0.0082 | 0.51 | 3.08 | torch 101.0%, torch-compile 100.0% | - |
| 🟡 | LerpFwdOp | test_binary_arith_bench[lerp-1024x10240-float16-float16-LerpFwdOp-<lambda>-normal] | 0.0177 | 0.59 | 3.56 | torch 100.3%, torch-compile 99.9% | - |
| 🔵 | LerpFwdOp | test_lerp_manifest_bench[hidden-state-prefill-float16] | 0.0148 | 1.71 | 3.41 | torch 100.2%, torch-compile 100.1% | - |
| 🔵 | LerpFwdOp | test_lerp_manifest_bench[hidden-state-prefill-bfloat16] | 0.0146 | 1.72 | 3.45 | torch 100.4%, torch-compile 100.0% | - |
| 🟡 | LerpFwdOp | test_lerp_manifest_bench[hidden-state-prefill-float32] | 0.0263 | 0.96 | 3.82 | torch 99.5%, torch-compile 99.4% | - |
| 🟡 | LerpFwdOp | test_lerp_manifest_bench[cnn-feat-broadcast-float16] | 0.0144 | 2.67 | 3.56 | torch 330.8%, torch-compile 99.8% | - |
| 🔵 | LerpFwdOp | test_lerp_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0143 | 2.69 | 3.58 | torch 336.6%, torch-compile 100.0% | - |
| 🟡 | LerpFwdOp | test_lerp_manifest_bench[cnn-feat-broadcast-float32] | 0.0266 | 1.45 | 3.86 | torch 191.9%, torch-compile 99.6% | - |
| 🟡 | LerpTensorFwdOp | test_lerp_tensor_manifest_bench[elementwise-16M-float16] | 0.0350 | 1.44 | 3.83 | torch 99.4%, torch-compile 99.1% | - |
| 🟡 | LerpTensorFwdOp | test_lerp_tensor_manifest_bench[elementwise-16M-bfloat16] | 0.0350 | 1.44 | 3.84 | torch 99.6%, torch-compile 99.4% | - |
| 🟡 | LerpTensorFwdOp | test_lerp_tensor_manifest_bench[elementwise-16M-float32] | 0.0655 | 0.77 | 4.10 | torch 99.4%, torch-compile 99.7% | - |
| 🔵 | LerpTensorFwdOp | test_lerp_tensor_manifest_bench[elementwise-256M-float16] | 0.4858 | 1.66 | 4.42 | torch 100.0%, torch-compile 100.0% | - |
| 🔵 | LerpTensorFwdOp | test_lerp_tensor_manifest_bench[elementwise-256M-bfloat16] | 0.4860 | 1.66 | 4.42 | torch 100.0%, torch-compile 100.0% | - |
| 🔵 | Log1pFwdOp | test_log1p_bench[elementwise-16M-float16] | 0.0181 | 1.85 | 3.70 | torch 144.4%, torch-compile 141.1% | - |
| 🔵 | Log1pFwdOp | test_log1p_bench[elementwise-16M-bfloat16] | 0.0181 | 1.85 | 3.70 | torch 148.0%, torch-compile 145.0% | - |
| 🟡 | Log1pFwdOp | test_log1p_bench[elementwise-16M-float32] | 0.0352 | 0.95 | 3.82 | torch 96.8%, torch-compile 96.5% | - |
| 🔵 | Log1pFwdOp | test_log1p_bench[elementwise-256M-float16] | 0.2542 | 2.11 | 4.22 | torch 149.5%, torch-compile 145.4% | - |
| 🔵 | Log1pFwdOp | test_log1p_bench[elementwise-256M-bfloat16] | 0.2549 | 2.11 | 4.21 | torch 152.1%, torch-compile 149.8% | - |
| 🔵 | LogFwdOp | test_log_bench[elementwise-16M-float16] | 0.0181 | 0.92 | 3.70 | torch 149.6%, torch-compile 149.9% | - |
| 🟢 | LogFwdOp | test_log_bench[elementwise-16M-bfloat16] | 0.0181 | 0.93 | 3.71 | torch 155.1%, torch-compile 153.5% | - |
| 🟡 | LogFwdOp | test_log_bench[elementwise-16M-float32] | 0.0357 | 0.47 | 3.76 | torch 96.1%, torch-compile 95.6% | - |
| 🟢 | LogFwdOp | test_log_bench[elementwise-256M-float16] | 0.2534 | 1.06 | 4.24 | torch 156.8%, torch-compile 158.6% | - |
| 🟢 | LogFwdOp | test_log_bench[elementwise-256M-bfloat16] | 0.2544 | 1.06 | 4.22 | torch 162.2%, torch-compile 161.3% | - |
| 🟢 | LogSoftmaxFwdOp | test_log_softmax_bench[attn-weights-4k-float16] | 0.0090 | 2.32 | 1.86 | flaggems 220.9%, torch 190.4%, torch-compile 164.9% | - |
| 🟢 | LogSoftmaxFwdOp | test_log_softmax_bench[attn-weights-4k-bfloat16] | 0.0088 | 2.37 | 1.90 | flaggems 231.5%, torch 194.2%, torch-compile 174.6% | - |
| 🔵 | LogSoftmaxFwdOp | test_log_softmax_bench[attn-weights-4k-float32] | 0.0115 | 1.83 | 2.92 | flaggems 179.0%, torch 160.9%, torch-compile 137.1% | - |
| 🔵 | LogSoftmaxFwdOp | test_log_softmax_bench[attn-weights-32k-bfloat16] | 0.0567 | 2.96 | 2.37 | flaggems 440.9%, torch 108.6%, torch-compile 126.4% | - |
| 🔴 | LogSoftmaxFwdOp | test_log_softmax_bench[lm-head-logits-float16] | 0.0249 | 0.08 | 0.07 | flaggems 1698.1%, torch 90.0%, torch-compile 36.4% | - |
| 🔴 | LogSoftmaxFwdOp | test_log_softmax_bench[lm-head-logits-bfloat16] | 0.0262 | 0.08 | 0.06 | flaggems 1612.8%, torch 88.0%, torch-compile 34.4% | - |
| 🔴 | LogSoftmaxFwdOp | test_log_softmax_bench[lm-head-logits-float32] | 0.0319 | 0.06 | 0.10 | flaggems 1263.4%, torch 110.1%, torch-compile 30.8% | - |
| 🔵 | LogSumExpFwdOp | test_logsumexp_bench[attn-weights-4k-float16] | 0.0074 | 2.26 | 1.13 | torch 656.9%, torch-compile 135.8% | - |
| 🔵 | LogSumExpFwdOp | test_logsumexp_bench[attn-weights-4k-bfloat16] | 0.0075 | 2.25 | 1.13 | torch 662.2%, torch-compile 134.3% | - |
| 🔵 | LogSumExpFwdOp | test_logsumexp_bench[attn-weights-32k-bfloat16] | 0.0411 | 3.27 | 1.63 | torch 482.1%, torch-compile 101.1% | - |
| 🔴 | LogSumExpFwdOp | test_logsumexp_bench[lm-head-logits-float16] | 0.0141 | 0.12 | 0.06 | torch 328.5%, torch-compile 75.1% | - |
| 🔴 | LogSumExpFwdOp | test_logsumexp_bench[lm-head-logits-bfloat16] | 0.0165 | 0.10 | 0.05 | torch 280.7%, torch-compile 62.3% | - |
| 🟡 | LogSumExpFwdOp | test_logsumexp_bench[3d-multidim-reduce-float16] | 0.0125 | 0.67 | 0.33 | torch 328.6%, torch-compile 81.4% | - |
| 🔵 | LogicalAndFwdOp | test_logical_bench[logical_and-1024x4096-float16-LogicalAndFwdOp-logical_and] | 0.0075 | 0.56 | 2.80 | torch 103.0%, torch-compile 102.6% | - |
| 🔵 | LogicalAndFwdOp | test_logical_bench[logical_and-1024x10240-float16-LogicalAndFwdOp-logical_and] | 0.0157 | 0.67 | 3.33 | torch 101.8%, torch-compile 101.8% | - |
| 🔵 | LogicalAndFwdOp | test_logical_and_manifest_bench[hidden-state-prefill-bool] | 0.0083 | 3.05 | 3.05 | torch 122.5%, torch-compile 107.0% | - |
| 🔵 | LogicalAndFwdOp | test_logical_and_manifest_bench[hidden-state-prefill-float16] | 0.0132 | 1.91 | 3.19 | torch 101.8%, torch-compile 101.5% | - |
| 🔵 | LogicalAndFwdOp | test_logical_and_manifest_bench[hidden-state-prefill-bfloat16] | 0.0130 | 1.94 | 3.24 | torch 101.2%, torch-compile 100.5% | - |
| 🔵 | LogicalAndFwdOp | test_logical_and_manifest_bench[hidden-state-prefill-float32] | 0.0225 | 1.12 | 3.36 | torch 100.0%, torch-compile 111.4% | - |
| 🔵 | LogicalAndFwdOp | test_logical_and_manifest_bench[cnn-feat-broadcast-bool] | 0.0081 | 4.78 | 3.19 | torch 560.3%, torch-compile 123.4% | - |
| 🔴 | LogicalAndFwdOp | test_logical_and_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 2.42 | 2.42 | torch 294.8%, torch-compile 76.3% | - |
| 🔴 | LogicalAndFwdOp | test_logical_and_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 2.42 | 2.42 | torch 302.0%, torch-compile 75.4% | - |
| 🟡 | LogicalAndFwdOp | test_logical_and_manifest_bench[cnn-feat-broadcast-float32] | 0.0208 | 1.86 | 3.09 | torch 224.8%, torch-compile 88.3% | - |
| 🔵 | LogicalNotFwdOp | test_logical_not_bench[elementwise-16M-bool] | 0.0101 | 1.65 | 3.31 | torch 128.1%, torch-compile 119.2% | - |
| 🔵 | LogicalNotFwdOp | test_logical_not_bench[elementwise-16M-float16] | 0.0148 | 1.14 | 3.41 | torch 103.3%, torch-compile 101.7% | - |
| 🟡 | LogicalNotFwdOp | test_logical_not_bench[elementwise-16M-float32] | 0.0235 | 0.71 | 3.57 | torch 99.6%, torch-compile 99.3% | - |
| 🔵 | LogicalNotFwdOp | test_logical_not_bench[elementwise-256M-bool] | 0.1263 | 2.12 | 4.25 | torch 144.0%, torch-compile 130.4% | - |
| 🔵 | LogicalOrFwdOp | test_logical_bench[logical_or-1024x4096-float16-LogicalOrFwdOp-logical_or] | 0.0075 | 0.56 | 2.80 | torch 102.1%, torch-compile 135.9% | - |
| 🔵 | LogicalOrFwdOp | test_logical_bench[logical_or-1024x10240-float16-LogicalOrFwdOp-logical_or] | 0.0158 | 0.66 | 3.31 | torch 101.4%, torch-compile 101.4% | - |
| 🔵 | LogicalOrFwdOp | test_logical_or_manifest_bench[hidden-state-prefill-bool] | 0.0082 | 3.07 | 3.07 | torch 110.5%, torch-compile 108.2% | - |
| 🔵 | LogicalOrFwdOp | test_logical_or_manifest_bench[hidden-state-prefill-float16] | 0.0132 | 1.91 | 3.19 | torch 101.2%, torch-compile 101.0% | - |
| 🔵 | LogicalOrFwdOp | test_logical_or_manifest_bench[hidden-state-prefill-bfloat16] | 0.0129 | 1.96 | 3.26 | torch 101.2%, torch-compile 100.8% | - |
| 🟡 | LogicalOrFwdOp | test_logical_or_manifest_bench[hidden-state-prefill-float32] | 0.0225 | 1.12 | 3.36 | torch 99.9%, torch-compile 99.7% | - |
| 🔵 | LogicalOrFwdOp | test_logical_or_manifest_bench[cnn-feat-broadcast-bool] | 0.0081 | 4.78 | 3.19 | torch 548.4%, torch-compile 127.0% | - |
| 🔴 | LogicalOrFwdOp | test_logical_or_manifest_bench[cnn-feat-broadcast-float16] | 0.0164 | 2.36 | 2.36 | torch 291.7%, torch-compile 73.5% | - |
| 🔴 | LogicalOrFwdOp | test_logical_or_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0164 | 2.36 | 2.36 | torch 298.6%, torch-compile 74.4% | - |
| 🟡 | LogicalOrFwdOp | test_logical_or_manifest_bench[cnn-feat-broadcast-float32] | 0.0209 | 1.84 | 3.07 | torch 222.4%, torch-compile 88.7% | - |
| 🔵 | LtFwdOp | test_comparison_bench[lt-1024x4096-float16-lt] | 0.0076 | 0.56 | 2.78 | torch 102.1%, torch-compile 102.6% | - |
| 🔵 | LtFwdOp | test_lt_manifest_bench[hidden-state-prefill-float16] | 0.0130 | 0.65 | 3.23 | torch 100.7%, torch-compile 101.2% | - |
| 🔵 | LtFwdOp | test_lt_manifest_bench[hidden-state-prefill-bfloat16] | 0.0132 | 0.64 | 3.18 | torch 101.0%, torch-compile 100.6% | - |
| 🔵 | LtFwdOp | test_lt_manifest_bench[hidden-state-prefill-float32] | 0.0225 | 0.37 | 3.35 | torch 100.0%, torch-compile 109.7% | - |
| 🔴 | LtFwdOp | test_lt_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.81 | 2.42 | torch 311.2%, torch-compile 74.3% | - |
| 🔴 | LtFwdOp | test_lt_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.81 | 2.42 | torch 317.5%, torch-compile 76.6% | - |
| 🟡 | LtFwdOp | test_lt_manifest_bench[cnn-feat-broadcast-float32] | 0.0209 | 0.61 | 3.07 | torch 235.1%, torch-compile 88.1% | - |
| 🟡 | MHCPostFwdOp | test_mhc_post_bench[post-small-bfloat16] | 0.0013 | 0.01 | 0.02 | torch-ref 802.5%, torch-compile 95.1% | - |
| 🟡 | MHCPostFwdOp | test_mhc_post_bench[post-medium-bfloat16] | 0.0014 | 0.02 | 0.05 | torch-ref 779.5%, torch-compile 97.7% | - |
| 🔵 | MHCPostFwdOp | test_mhc_post_bench[post-large-bfloat16] | 0.0016 | 0.05 | 0.12 | torch-ref 709.9%, torch-compile 101.0% | - |
| 🔴 | MHCPreFwdOp | test_mhc_pre_bench[pre-small-bfloat16] | 0.0395 | 0.01 | 0.01 | torch-ref 150.1%, torch-compile 49.8% | - |
| 🔴 | MHCPreFwdOp | test_mhc_pre_bench[pre-medium-bfloat16] | 0.0544 | 0.02 | 0.01 | torch-ref 143.2%, torch-compile 57.7% | - |
| 🔴 | MHCPreFwdOp | test_mhc_pre_bench[pre-large-bfloat16] | 0.0715 | 0.03 | 0.02 | torch-ref 163.7%, torch-compile 79.3% | - |
| 🟡 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-2p7b-b1-s2k-bfloat16] | 0.1100 | 74.03 | 0.99 | mamba 99.4%, torch-ref 1959.0%, torch-compile 624.9% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-1p3b-b1-s8k-float16] | 0.2909 | 89.77 | 1.20 | mamba 107.5%, torch-ref 2376.2%, torch-compile 693.8% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-2p7b-b1-s2k-dt-bias-bfloat16] | 0.1091 | 74.65 | 1.00 | mamba 100.4%, torch-ref 1977.0%, torch-compile 631.2% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-1p3b-b1-s8k-dt-bias-float16] | 0.2904 | 89.92 | 1.20 | mamba 107.5%, torch-ref 2381.0%, torch-compile 693.5% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-2p7b-b1-s2k-init-states-bfloat16] | 0.1106 | 73.63 | 1.01 | mamba 100.1%, torch-ref 1946.0%, torch-compile 613.4% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-1p3b-b1-s8k-init-states-float16] | 0.2915 | 89.57 | 1.20 | mamba 107.2%, torch-ref 2368.9%, torch-compile 692.0% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-2p7b-b1-s2k-dt-bias-init-states-bfloat16] | 0.1099 | 74.11 | 1.01 | mamba 100.6%, torch-ref 1961.8%, torch-compile 618.1% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-1p3b-b1-s8k-dt-bias-init-states-float16] | 0.2899 | 90.06 | 1.21 | mamba 107.8%, torch-ref 2381.9%, torch-compile 694.0% | - |
| 🟡 | MaskedFillFwdOp | test_masked_fill_tensor_manifest_bench[elementwise-16M-float16] | 0.0227 | 0.74 | 3.69 | torch 177.1%, torch-compile 99.4% | - |
| 🟡 | MaskedFillFwdOp | test_masked_fill_tensor_manifest_bench[elementwise-16M-bfloat16] | 0.0226 | 0.74 | 3.71 | torch 177.4%, torch-compile 99.6% | - |
| 🟡 | MaskedFillFwdOp | test_masked_fill_tensor_manifest_bench[elementwise-16M-float32] | 0.0380 | 0.44 | 3.97 | torch 192.3%, torch-compile 98.5% | - |
| 🔵 | MaskedFillFwdOp | test_masked_fill_tensor_manifest_bench[elementwise-256M-float16] | 0.3093 | 0.87 | 4.34 | torch 184.3%, torch-compile 100.2% | - |
| 🟡 | MaskedFillFwdOp | test_masked_fill_tensor_manifest_bench[elementwise-256M-bfloat16] | 0.3103 | 0.87 | 4.33 | torch 184.0%, torch-compile 99.9% | - |
| 🟡 | MaskedFillScalarFwdOp | test_masked_fill_scalar_manifest_bench[elementwise-16M-float16] | 0.0228 | 0.74 | 3.69 | torch 165.0%, torch-compile 99.2% | - |
| 🟡 | MaskedFillScalarFwdOp | test_masked_fill_scalar_manifest_bench[elementwise-16M-bfloat16] | 0.0225 | 0.75 | 3.73 | torch 167.5%, torch-compile 99.9% | - |
| 🟡 | MaskedFillScalarFwdOp | test_masked_fill_scalar_manifest_bench[elementwise-16M-float32] | 0.0379 | 0.44 | 3.99 | torch 187.4%, torch-compile 98.6% | - |
| 🟡 | MaskedFillScalarFwdOp | test_masked_fill_scalar_manifest_bench[elementwise-256M-float16] | 0.3101 | 0.87 | 4.33 | torch 182.9%, torch-compile 99.8% | - |
| 🟡 | MaskedFillScalarFwdOp | test_masked_fill_scalar_manifest_bench[elementwise-256M-bfloat16] | 0.3104 | 0.86 | 4.32 | torch 182.9%, torch-compile 99.9% | - |
| 🔵 | MaxPool1dFwdOp | test_max_pool1d_bench[sincnet-speaker-local-float16] | 0.0114 | 0.92 | 2.45 | torch-ref 443.8%, torch-compile 100.3% | - |
| 🔴 | MaxPool1dFwdOp | test_max_pool1d_bench[textcnn-global-float16] | 0.0134 | 0.16 | 0.31 | torch-ref 196.4%, torch-compile 27.6% | - |
| 🟡 | MaxPool1dFwdOp | test_max_pool1d_bench[ecg-cnn-dilated-bfloat16] | 0.0095 | 1.10 | 1.32 | torch-ref 371.5%, torch-compile 82.2% | - |
| 🔴 | MaxPool1dIndicesFwdOp | test_max_pool1d_indices_bench[sincnet-speaker-local-float16] | 0.0218 | 0.48 | 2.57 | torch-ref 231.9%, torch-compile 73.6% | - |
| 🔴 | MaxPool1dIndicesFwdOp | test_max_pool1d_indices_bench[textcnn-global-float16] | 0.0193 | 0.11 | 0.23 | torch-ref 137.0%, torch-compile 29.5% | - |
| 🔴 | MaxPool1dIndicesFwdOp | test_max_pool1d_indices_bench[ecg-cnn-dilated-bfloat16] | 0.0223 | 0.47 | 1.31 | torch-ref 158.4%, torch-compile 60.0% | - |
| 🔴 | MaxPool2dFwdOp | test_max_pool2d_bench[resnet-stem-float16] | 0.0471 | 1.23 | 1.36 | flaggems 166.4%, torch-ref 295.0%, torch-compile 72.3% | - |
| 🔴 | MaxPool2dFwdOp | test_max_pool2d_bench[resnet-stem-bfloat16] | 0.0473 | 1.22 | 1.36 | flaggems 165.8%, torch-ref 294.6%, torch-compile 72.0% | - |
| 🟡 | MaxPool2dFwdOp | test_max_pool2d_bench[resnet-stem-float32] | 0.0528 | 1.09 | 2.43 | flaggems 153.9%, torch-ref 255.0%, torch-compile 93.9% | - |
| 🔵 | MaxPool2dFwdOp | test_max_pool2d_bench[vgg-block-float16] | 0.0072 | 0.89 | 2.23 | flaggems 205.4%, torch-ref 385.3%, torch-compile 100.9% | - |
| 🔵 | MaxPool2dFwdOp | test_max_pool2d_bench[vgg-block-bfloat16] | 0.0072 | 0.89 | 2.23 | flaggems 205.3%, torch-ref 387.1%, torch-compile 100.9% | - |
| 🟡 | MaxPool2dFwdOp | test_max_pool2d_bench[vgg-block-float32] | 0.0111 | 0.58 | 2.90 | flaggems 151.2%, torch-ref 250.3%, torch-compile 93.6% | - |
| 🔵 | MaxPool2dFwdOp | test_max_pool2d_bench[alexnet-ceil-float16] | 0.0088 | 1.53 | 1.75 | flaggems 256.6%, torch-ref 396.3%, torch-compile 125.2% | - |
| 🔵 | MaxPool2dFwdOp | test_max_pool2d_bench[alexnet-ceil-bfloat16] | 0.0088 | 1.53 | 1.75 | flaggems 259.5%, torch-ref 396.7%, torch-compile 125.2% | - |
| 🔵 | MaxPool2dFwdOp | test_max_pool2d_bench[alexnet-ceil-float32] | 0.0126 | 1.06 | 2.43 | flaggems 180.5%, torch-ref 270.1%, torch-compile 122.0% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[resnet-stem-float16] | 0.1126 | 0.51 | 1.03 | flaggems 69.7%, torch-ref 123.4%, torch-compile 61.3% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[resnet-stem-bfloat16] | 0.1124 | 0.51 | 1.03 | flaggems 69.7%, torch-ref 124.1%, torch-compile 62.3% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[resnet-stem-float32] | 0.1073 | 0.54 | 1.68 | flaggems 75.5%, torch-ref 125.5%, torch-compile 66.7% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[vgg-block-float16] | 0.0196 | 0.33 | 1.47 | flaggems 75.2%, torch-ref 141.4%, torch-compile 54.2% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[vgg-block-bfloat16] | 0.0195 | 0.33 | 1.49 | flaggems 76.0%, torch-ref 143.3%, torch-compile 54.6% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[vgg-block-float32] | 0.0195 | 0.33 | 2.30 | flaggems 85.7%, torch-ref 142.0%, torch-compile 65.2% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[alexnet-ceil-float16] | 0.0237 | 0.57 | 1.15 | flaggems 95.0%, torch-ref 146.6%, torch-compile 74.6% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[alexnet-ceil-bfloat16] | 0.0237 | 0.57 | 1.15 | flaggems 95.8%, torch-ref 146.7%, torch-compile 73.4% | - |
| 🟡 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[alexnet-ceil-float32] | 0.0236 | 0.57 | 1.81 | flaggems 96.6%, torch-ref 144.6%, torch-compile 82.0% | - |
| 🔵 | MaxPool3dFwdOp | test_max_pool3d_bench[c3d-pool1-float16] | 0.0763 | 1.35 | 3.37 | cudnn 394.3%, torch-ref 678.2%, torch-compile 101.0% | - |
| 🔵 | MaxPool3dFwdOp | test_max_pool3d_bench[c3d-pool2-float16] | 0.0235 | 1.09 | 2.46 | cudnn 258.6%, torch-ref 399.6%, torch-compile 104.9% | - |
| 🟢 | MaxPool3dFwdOp | test_max_pool3d_bench[medicalnet-stem-bfloat16] | 0.1113 | 1.71 | 1.05 | cudnn 237.0%, torch-ref 300.7%, torch-compile 832.3% | - |
| 🔴 | MaxPool3dIndicesFwdOp | test_max_pool3d_indices_bench[c3d-pool1-float16] | 0.3044 | 0.34 | 1.52 | torch-ref 170.0%, torch-compile 42.5% | - |
| 🔴 | MaxPool3dIndicesFwdOp | test_max_pool3d_indices_bench[c3d-pool2-float16] | 0.0588 | 0.44 | 1.42 | torch-ref 159.9%, torch-compile 55.6% | - |
| 🔵 | MaxPool3dIndicesFwdOp | test_max_pool3d_indices_bench[medicalnet-stem-bfloat16] | 0.3315 | 0.58 | 0.52 | torch-ref 101.0%, torch-compile 614.2% | - |
| 🟡 | MaximumFwdOp | test_binary_arith_bench[maximum-1024x4096-float16-float16-MaximumFwdOp-maximum-normal] | 0.0086 | 0.49 | 2.93 | torch 101.1%, torch-compile 97.8% | - |
| 🟡 | MaximumFwdOp | test_binary_arith_bench[maximum-1024x10240-float16-float16-MaximumFwdOp-maximum-normal] | 0.0180 | 0.58 | 3.49 | torch 100.7%, torch-compile 98.9% | - |
| 🟡 | MaximumFwdOp | test_binary_arith_bench[maximum-1024x11008-float16-float16-MaximumFwdOp-maximum-normal] | 0.0189 | 0.60 | 3.58 | torch 100.7%, torch-compile 99.0% | - |
| 🟡 | MaximumFwdOp | test_maximum_manifest_bench[hidden-state-prefill-float16] | 0.0147 | 0.57 | 3.43 | torch 100.6%, torch-compile 98.5% | - |
| 🟡 | MaximumFwdOp | test_maximum_manifest_bench[hidden-state-prefill-bfloat16] | 0.0149 | 0.56 | 3.37 | torch 100.6%, torch-compile 98.5% | - |
| 🟡 | MaximumFwdOp | test_maximum_manifest_bench[hidden-state-prefill-float32] | 0.0263 | 0.32 | 3.82 | torch 100.7%, torch-compile 99.8% | - |
| 🔴 | MaximumFwdOp | test_maximum_manifest_bench[cnn-feat-broadcast-float16] | 0.0374 | 0.34 | 1.37 | torch 135.0%, torch-compile 38.3% | - |
| 🔴 | MaximumFwdOp | test_maximum_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0392 | 0.33 | 1.31 | torch 130.9%, torch-compile 36.1% | - |
| 🟡 | MaximumFwdOp | test_maximum_manifest_bench[cnn-feat-broadcast-float32] | 0.0293 | 0.44 | 3.51 | torch 181.0%, torch-compile 90.1% | - |
| 🔵 | MeanFwdOp | test_mean_bench[hidden-state-reduce-float16] | 0.0074 | 1.13 | 2.26 | flaggems 119.8%, torch 666.2%, torch-compile 112.5% | - |
| 🔵 | MeanFwdOp | test_mean_bench[hidden-state-reduce-bfloat16] | 0.0074 | 1.13 | 2.26 | flaggems 120.3%, torch 672.2%, torch-compile 113.8% | - |
| 🟡 | MeanFwdOp | test_mean_bench[long-seq-reduce-bfloat16] | 0.0040 | 0.52 | 1.04 | flaggems 94.1%, torch 418.2%, torch-compile 109.1% | - |
| 🔴 | MeanFwdOp | test_mean_bench[3d-multidim-reduce-float16] | 0.0113 | 0.19 | 0.37 | flaggems 119.6%, torch 169.4%, torch-compile 41.4% | - |
| 🔴 | MeanPoolingForwardOp | test_mean_pooling_bench[dense-mainstream] | 0.1352 | 0.50 | 1.01 | torch-ref 454.8%, torch-compile 313.9%, torch-view-mean 34.8% | - |
| 🔴 | MeanPoolingForwardOp | test_mean_pooling_bench[dense-batched] | 0.0702 | 0.48 | 0.97 | torch-ref 372.5%, torch-compile 208.7%, torch-view-mean 40.7% | - |
| 🟢 | MeanPoolingForwardOp | test_mean_pooling_bench[varlen-long] | 0.1386 | 0.48 | 0.98 | torch-ref 447.4%, torch-compile 444.0% | - |
| 🟢 | MeanPoolingForwardOp | test_mean_pooling_bench[varlen-tail] | 0.0218 | 0.41 | 0.78 | torch-ref 982.9%, torch-compile 962.9% | - |
| 🟡 | MinimumFwdOp | test_binary_arith_bench[minimum-1024x4096-float16-float16-MinimumFwdOp-minimum-normal] | 0.0086 | 0.49 | 2.92 | torch 101.5%, torch-compile 97.0% | - |
| 🟡 | MinimumFwdOp | test_binary_arith_bench[minimum-1024x10240-float16-float16-MinimumFwdOp-minimum-normal] | 0.0181 | 0.58 | 3.48 | torch 100.7%, torch-compile 98.8% | - |
| 🟡 | MinimumFwdOp | test_binary_arith_bench[minimum-1024x11008-float16-float16-MinimumFwdOp-minimum-normal] | 0.0189 | 0.60 | 3.57 | torch 100.5%, torch-compile 99.2% | - |
| 🟡 | MinimumFwdOp | test_minimum_manifest_bench[hidden-state-prefill-float16] | 0.0149 | 0.56 | 3.37 | torch 100.8%, torch-compile 98.8% | - |
| 🟡 | MinimumFwdOp | test_minimum_manifest_bench[hidden-state-prefill-bfloat16] | 0.0150 | 0.56 | 3.35 | torch 100.4%, torch-compile 98.5% | - |
| 🟡 | MinimumFwdOp | test_minimum_manifest_bench[hidden-state-prefill-float32] | 0.0265 | 0.32 | 3.80 | torch 100.1%, torch-compile 99.3% | - |
| 🔴 | MinimumFwdOp | test_minimum_manifest_bench[cnn-feat-broadcast-float16] | 0.0374 | 0.34 | 1.37 | torch 134.9%, torch-compile 38.4% | - |
| 🔴 | MinimumFwdOp | test_minimum_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0392 | 0.33 | 1.31 | torch 130.9%, torch-compile 36.7% | - |
| 🟡 | MinimumFwdOp | test_minimum_manifest_bench[cnn-feat-broadcast-float32] | 0.0294 | 0.44 | 3.49 | torch 180.8%, torch-compile 89.8% | - |
| 🟢 | MishFwdOp | test_mish_manifest_bench[yolo-p3-float16] | 0.0403 | 2.60 | 2.60 | torch 157.9%, torch-compile 182.1% | - |
| 🟢 | MishFwdOp | test_mish_manifest_bench[yolo-p3-bfloat16] | 0.0405 | 2.59 | 2.59 | torch 158.3%, torch-compile 182.9% | - |
| 🟢 | MishFwdOp | test_mish_manifest_bench[yolo-p4-float16] | 0.0214 | 2.45 | 2.45 | torch 155.4%, torch-compile 178.4% | - |
| 🟢 | MishFwdOp | test_mish_manifest_bench[yolo-p4-bfloat16] | 0.0216 | 2.42 | 2.42 | torch 155.3%, torch-compile 228.1% | - |
| 🟢 | MoeGateUpFwdOp | test_moe_gate_up_bench[deepseek-v3-decode-gate-up-bfloat16] | 3.4594 | 69.53 | 4.37 | torch-ref 191.8%, torch-compile 227.2% | - |
| 🟢 | MoeGateUpFwdOp | test_moe_gate_up_bench[deepseek-v3-prefill-gate-up-bfloat16] | 4.4089 | 436.43 | 3.55 | torch-ref 158.1%, torch-compile 614.2% | - |
| 🔵 | MoeGroupedGemmNopadFwdOp | test_moe_grouped_gemm_nopad_bench[deepseek-v3-decode-gate-up-bfloat16] | 3.7451 | 64.22 | 4.04 | torch-ref 138.0%, torch-compile 156.3% | - |
| 🔵 | MoeGroupedGemmNopadFwdOp | test_moe_grouped_gemm_nopad_bench[deepseek-v3-prefill-gate-up-bfloat16] | 4.2967 | 447.82 | 3.67 | torch-ref 125.9%, torch-compile 251.5% | - |
| 🔵 | MoeGroupedGemmNopadFwdOp | test_moe_grouped_gemm_nopad_bench[deepseek-v3-decode-down-bfloat16] | 1.9105 | 62.95 | 3.97 | torch-ref 140.9%, torch-compile 292.4% | - |
| 🔵 | MoeGroupedGemmNopadFwdOp | test_moe_grouped_gemm_nopad_bench[deepseek-v3-prefill-down-bfloat16] | 2.1523 | 447.00 | 3.77 | torch-ref 132.1%, torch-compile 1199.8% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[kimi-k2-decode-int32] | 0.0169 | 0.00 | 0.01 | triton 287.2% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[kimi-k2-small-int32] | 0.0195 | 0.00 | 0.01 | triton 247.2% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[kimi-k2-medium-int32] | 0.0217 | 0.00 | 0.01 | triton 257.5% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[kimi-k2-prefill-int32] | 0.0410 | 0.00 | 0.01 | triton 208.7% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[deepseek-v3-decode-int32] | 0.0148 | 0.00 | 0.00 | triton 228.5% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[deepseek-v3-small-int32] | 0.0153 | 0.00 | 0.00 | triton 220.1% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[deepseek-v3-medium-int32] | 0.0177 | 0.00 | 0.01 | triton 236.1% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[deepseek-v3-prefill-int32] | 0.0378 | 0.00 | 0.01 | triton 196.5% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[qwen3-decode-int32] | 0.0108 | 0.00 | 0.00 | triton 156.8% | - |
| 🔵 | MoePermuteAlignFwdOp | test_permute_align_bench[qwen3-small-int32] | 0.0121 | 0.00 | 0.00 | triton 149.9% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[qwen3-medium-int32] | 0.0141 | 0.00 | 0.00 | triton 211.8% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[qwen3-prefill-int32] | 0.0318 | 0.00 | 0.01 | triton 251.2% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[kimi-k2-decode-bfloat16] | 0.0106 | 0.00 | 0.01 | vllm 110.2% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[kimi-k2-small-bfloat16] | 0.0118 | 0.00 | 0.35 | vllm 117.0% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[kimi-k2-medium-bfloat16] | 0.0356 | 0.00 | 1.86 | vllm 129.3% | - |
| 🟡 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[kimi-k2-prefill-bfloat16] | 0.2855 | 0.00 | 1.85 | vllm 94.9% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-decode-bfloat16] | 0.0092 | 0.00 | 0.01 | vllm 125.3% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-small-bfloat16] | 0.0104 | 0.00 | 0.40 | vllm 132.2% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-medium-bfloat16] | 0.0337 | 0.00 | 1.96 | vllm 136.7% | - |
| 🟡 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-prefill-bfloat16] | 0.2789 | 0.00 | 1.90 | vllm 96.8% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-235b-decode-bfloat16] | 0.0080 | 0.00 | 0.02 | vllm 143.4% | - |
| 🟢 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-235b-small-bfloat16] | 0.0090 | 0.00 | 0.46 | vllm 152.8% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-235b-medium-bfloat16] | 0.0313 | 0.00 | 2.11 | vllm 147.2% | - |
| 🟡 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-235b-prefill-bfloat16] | 0.2686 | 0.00 | 1.97 | vllm 97.2% | - |
| 🟢 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-30b-decode-bfloat16] | 0.0063 | 0.00 | 0.01 | vllm 167.0% | - |
| 🟢 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-30b-small-bfloat16] | 0.0072 | 0.00 | 0.25 | vllm 173.8% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-30b-medium-bfloat16] | 0.0207 | 0.00 | 1.37 | vllm 139.7% | - |
| 🟡 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-30b-prefill-bfloat16] | 0.1419 | 0.00 | 1.60 | vllm 91.3% | - |
|  | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-ep2-decode-bfloat16] | 0.0087 | 0.00 | 0.02 | - | - |
|  | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-ep2-medium-bfloat16] | 0.0280 | 0.00 | 2.36 | - | - |
|  | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-ep2-prefill-bfloat16] | 0.2101 | 0.00 | 2.52 | - | - |
|  | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-235b-ep2-medium-bfloat16] | 0.0264 | 0.00 | 2.50 | - | - |
| 🟢 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[large-hidden-decode-bfloat16] | 0.0070 | 0.02 | 0.02 | vllm 238.5% | - |
| 🟢 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[large-hidden-small-bfloat16] | 0.0079 | 0.47 | 0.52 | vllm 227.2% | - |
| 🔵 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[large-hidden-medium-bfloat16] | 0.0214 | 2.75 | 3.09 | vllm 137.1% | - |
| 🔵 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[large-hidden-prefill-bfloat16] | 0.1329 | 3.53 | 3.98 | vllm 104.7% | - |
| 🟢 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[small-hidden-decode-bfloat16] | 0.0057 | 0.01 | 0.01 | vllm 156.7% | - |
| 🟢 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[small-hidden-small-bfloat16] | 0.0065 | 0.24 | 0.27 | vllm 152.2% | - |
| 🔵 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[small-hidden-medium-bfloat16] | 0.0116 | 2.18 | 2.45 | vllm 128.0% | - |
| 🔵 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[small-hidden-prefill-bfloat16] | 0.0615 | 3.27 | 3.69 | vllm 109.7% | - |
| 🔵 | MulFwdOp | test_binary_arith_bench[mul-1024x4096-float16-float16-MulFwdOp-mul-normal] | 0.0084 | 0.50 | 2.99 | torch 101.9%, torch-compile 100.0% | - |
| 🔵 | MulFwdOp | test_binary_arith_bench[mul-1024x10240-float16-float16-MulFwdOp-mul-normal] | 0.0176 | 0.60 | 3.57 | torch 100.9%, torch-compile 100.0% | - |
| 🔵 | MulFwdOp | test_binary_arith_bench[mul-1024x11008-float16-float16-MulFwdOp-mul-normal] | 0.0185 | 0.61 | 3.65 | torch 100.2%, torch-compile 100.2% | - |
| 🔵 | MulFwdOp | test_mul_manifest_bench[hidden-state-prefill-float16] | 0.0148 | 0.56 | 3.39 | torch 100.2%, torch-compile 100.2% | - |
| 🔵 | MulFwdOp | test_mul_manifest_bench[hidden-state-prefill-bfloat16] | 0.0147 | 0.57 | 3.43 | torch 100.3%, torch-compile 100.3% | - |
| 🟡 | MulFwdOp | test_mul_manifest_bench[hidden-state-prefill-float32] | 0.0265 | 0.32 | 3.80 | torch 99.5%, torch-compile 99.4% | - |
| 🔵 | MulFwdOp | test_mul_manifest_bench[cnn-feat-broadcast-float16] | 0.0142 | 0.90 | 3.61 | torch 319.6%, torch-compile 100.0% | - |
| 🔵 | MulFwdOp | test_mul_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0145 | 0.89 | 3.55 | torch 319.5%, torch-compile 100.2% | - |
| 🔵 | MulFwdOp | test_mul_manifest_bench[cnn-feat-broadcast-float32] | 0.0265 | 0.49 | 3.88 | torch 186.2%, torch-compile 100.4% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-8b-short-float16] | 0.2435 | 88.21 | 0.48 | fa3 59.0% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-8b-short-bfloat16] | 0.4562 | 47.07 | 0.26 | fa3 31.4% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-8b-long-float16] | 0.9026 | 190.33 | 0.26 | fa3 61.1% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-8b-long-bfloat16] | 1.3118 | 130.97 | 0.18 | fa3 41.7% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-70b-short-float16] | 0.2444 | 87.86 | 0.48 | fa3 58.6% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-70b-short-bfloat16] | 0.4565 | 47.04 | 0.26 | fa3 31.3% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-70b-long-float16] | 0.8926 | 192.46 | 0.26 | fa3 61.8% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-70b-long-bfloat16] | 1.1015 | 155.97 | 0.21 | fa3 49.9% | - |
| 🟢 | MultiHeadAttentionDecodePagedWithKVCacheFwdOp | test_mha_decode_paged_bench[single-token-page128-float16] | 0.0060 | 0.70 | 0.70 | flashinfer 154.1% | - |
| 🟢 | MultiHeadAttentionDecodePagedWithKVCacheFwdOp | test_mha_decode_paged_bench[batch2-page256-float16] | 0.0057 | 0.74 | 0.37 | fa3 325.7%, flashinfer 171.8% | - |
| 🟢 | MultiHeadAttentionDecodePagedWithKVCacheFwdOp | test_mha_decode_paged_bench[longer-cache-float16] | 0.0053 | 0.39 | 0.39 | fa3 341.7%, flashinfer 181.4% | - |
| 🟢 | MultiHeadAttentionDecodePagedWithKVCacheFwdOp | test_mha_decode_paged_bench[shorter-cache-float16] | 0.0046 | 0.23 | 0.23 | fa3 386.2%, flashinfer 200.7% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-8b-4k-float16] | 0.5111 | 4.20 | 4.20 | fa3 100.3%, flashinfer 103.6% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-8b-4k-bfloat16] | 0.5104 | 4.21 | 4.21 | fa3 100.2%, flashinfer 103.9% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-8b-32k-float16] | 0.9809 | 4.38 | 4.38 | fa3 100.6%, flashinfer 101.8% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-8b-32k-bfloat16] | 0.9820 | 4.37 | 4.37 | fa3 100.4%, flashinfer 101.7% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-70b-4k-float16] | 0.5139 | 4.18 | 4.18 | fa3 100.2%, flashinfer 103.3% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-70b-4k-bfloat16] | 0.5139 | 4.18 | 4.18 | fa3 100.1%, flashinfer 103.1% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-70b-32k-float16] | 0.9811 | 4.38 | 4.38 | fa3 100.5%, flashinfer 101.5% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-70b-32k-bfloat16] | 0.9798 | 4.38 | 4.38 | fa3 100.7%, flashinfer 101.7% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-8b-short-float16] | 0.0425 | 201.98 | 1.58 | fa3 81.9%, flashinfer 96.8% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-8b-short-bfloat16] | 0.0425 | 202.28 | 1.58 | fa3 83.5%, flashinfer 96.4% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-8b-long-float16] | 0.1682 | 408.50 | 0.80 | fa3 82.2%, flashinfer 98.2% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-8b-long-bfloat16] | 0.1669 | 411.75 | 0.80 | fa3 81.8%, flashinfer 97.1% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-70b-short-float16] | 0.0428 | 200.77 | 1.57 | fa3 82.7%, flashinfer 96.4% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-70b-short-bfloat16] | 0.0425 | 202.06 | 1.58 | fa3 83.0%, flashinfer 96.7% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-70b-long-float16] | 0.1679 | 409.28 | 0.80 | fa3 83.1%, flashinfer 97.9% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-70b-long-bfloat16] | 0.1672 | 411.04 | 0.80 | fa3 81.8%, flashinfer 97.4% | - |
| 🟢 | MultiHeadLatentAttentionDecodeWithKVCacheFwdOp | test_mla_decode_bench[deepseek-v2-4k-float16] | 0.0374 | 287.28 | 1.42 | torch-ref 440.4%, torch-compile 342.5% | - |
| 🟢 | MultiHeadLatentAttentionDecodeWithKVCacheFwdOp | test_mla_decode_bench[deepseek-v2-4k-bfloat16] | 0.0375 | 286.67 | 1.41 | torch-ref 437.6%, torch-compile 350.4% | - |
| 🟢 | MultiHeadLatentAttentionDecodeWithKVCacheFwdOp | test_mla_decode_bench[deepseek-v2-32k-float16] | 0.1188 | 180.74 | 0.85 | torch-ref 230.8%, torch-compile 212.1% | - |
| 🟢 | MultiHeadLatentAttentionDecodeWithKVCacheFwdOp | test_mla_decode_bench[deepseek-v2-32k-bfloat16] | 0.1188 | 180.74 | 0.85 | torch-ref 233.9%, torch-compile 215.3% | - |
| 🟢 | MultiHeadLatentAttentionDecodeWithKVCacheFwdOp | test_mla_decode_bench[deepseek-v3-4k-bfloat16] | 0.0216 | 248.18 | 1.22 | torch-ref 392.3%, torch-compile 323.7% | - |
| 🔵 | MultiHeadLatentAttentionDecodeWithKVCacheFwdOp | test_mla_decode_bench[deepseek-v3-32k-bfloat16] | 0.1179 | 91.06 | 0.43 | torch-ref 145.1%, torch-compile 138.7% | - |
| 🟡 | NanToNumFwdOp | test_nan_to_num_manifest_bench[elementwise-16M-float16] | 0.0189 | 5.31 | 3.54 | torch 101.5%, torch-compile 98.0% | - |
| 🟡 | NanToNumFwdOp | test_nan_to_num_manifest_bench[elementwise-16M-bfloat16] | 0.0189 | 5.32 | 3.55 | torch 101.5%, torch-compile 98.3% | - |
| 🔵 | NanToNumFwdOp | test_nan_to_num_manifest_bench[elementwise-16M-float32] | 0.0340 | 2.96 | 3.95 | torch 100.3%, torch-compile 100.1% | - |
| 🟡 | NanToNumFwdOp | test_nan_to_num_manifest_bench[elementwise-256M-float16] | 0.2650 | 6.08 | 4.05 | torch 103.5%, torch-compile 97.6% | - |
| 🟡 | NanToNumFwdOp | test_nan_to_num_manifest_bench[elementwise-256M-bfloat16] | 0.2639 | 6.10 | 4.07 | torch 103.7%, torch-compile 97.9% | - |
| 🔵 | NeFwdOp | test_comparison_bench[ne-1024x4096-float16-ne] | 0.0076 | 0.55 | 2.74 | torch 102.1%, torch-compile 102.1% | - |
| 🔵 | NeFwdOp | test_ne_manifest_bench[hidden-state-prefill-float16] | 0.0130 | 0.64 | 3.22 | torch 101.1%, torch-compile 100.9% | - |
| 🔵 | NeFwdOp | test_ne_manifest_bench[hidden-state-prefill-bfloat16] | 0.0132 | 0.63 | 3.17 | torch 101.7%, torch-compile 101.2% | - |
| 🟡 | NeFwdOp | test_ne_manifest_bench[hidden-state-prefill-float32] | 0.0223 | 0.38 | 3.38 | torch 99.9%, torch-compile 111.5% | - |
| 🔴 | NeFwdOp | test_ne_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.81 | 2.43 | torch 300.0%, torch-compile 75.0% | - |
| 🔴 | NeFwdOp | test_ne_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.81 | 2.43 | torch 307.3%, torch-compile 74.4% | - |
| 🟡 | NeFwdOp | test_ne_manifest_bench[cnn-feat-broadcast-float32] | 0.0208 | 0.62 | 3.08 | torch 229.2%, torch-compile 88.5% | - |
| 🔵 | NegFwdOp | test_neg_bench[elementwise-16M-float16] | 0.0179 | 0.94 | 3.75 | torch 105.4%, torch-compile 100.2% | - |
| 🔵 | NegFwdOp | test_neg_bench[elementwise-16M-bfloat16] | 0.0179 | 0.94 | 3.76 | torch 100.5%, torch-compile 100.4% | - |
| 🟡 | NegFwdOp | test_neg_bench[elementwise-16M-float32] | 0.0340 | 0.49 | 3.95 | torch 99.9%, torch-compile 99.8% | - |
| 🟡 | NegFwdOp | test_neg_bench[elementwise-256M-float16] | 0.2498 | 1.07 | 4.30 | torch 107.5%, torch-compile 100.0% | - |
| 🟡 | NegFwdOp | test_neg_bench[elementwise-256M-bfloat16] | 0.2501 | 1.07 | 4.29 | torch 99.9%, torch-compile 99.8% | - |
| 🔵 | PowFwdOp | test_binary_arith_bench[pow-1024x4096-float16-float16-PowFwdOp-pow-positive] | 0.0201 | 0.21 | 1.25 | torch 100.5%, torch-compile 125.5% | - |
| 🔵 | PowFwdOp | test_binary_arith_bench[pow-1024x10240-float16-float16-PowFwdOp-pow-positive] | 0.0452 | 0.23 | 1.39 | torch 100.4%, torch-compile 119.8% | - |
| 🔵 | PowFwdOp | test_pow_manifest_bench[hidden-state-prefill-float16] | 0.0369 | 0.68 | 1.36 | torch 100.2%, torch-compile 118.2% | - |
| 🔵 | PowFwdOp | test_pow_manifest_bench[hidden-state-prefill-bfloat16] | 0.0377 | 0.67 | 1.33 | torch 100.6%, torch-compile 119.5% | - |
| 🟡 | PowFwdOp | test_pow_manifest_bench[hidden-state-prefill-float32] | 0.0388 | 0.65 | 2.59 | torch 96.5%, torch-compile 108.3% | - |
| 🔵 | PowFwdOp | test_pow_manifest_bench[cnn-feat-broadcast-float16] | 0.0542 | 0.71 | 0.95 | torch 173.8%, torch-compile 113.1% | - |
| 🔵 | PowFwdOp | test_pow_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0542 | 0.71 | 0.95 | torch 176.3%, torch-compile 113.6% | - |
| 🔵 | PowFwdOp | test_pow_manifest_bench[cnn-feat-broadcast-float32] | 0.0573 | 0.67 | 1.79 | torch 163.9%, torch-compile 102.4% | - |
| 🔵 | PreluFwdOp | test_prelu_manifest_bench[cnn-feat-per-channel-float16] | 0.0146 | 1.76 | 3.51 | torch 321.9%, torch-compile 100.0% | - |
| 🟡 | PreluFwdOp | test_prelu_manifest_bench[cnn-feat-per-channel-bfloat16] | 0.0144 | 1.78 | 3.57 | torch 337.6%, torch-compile 100.0% | - |
| 🔵 | PreluFwdOp | test_prelu_manifest_bench[cnn-feat-per-channel-deep-float16] | 0.0084 | 1.54 | 3.08 | torch 299.6%, torch-compile 100.4% | - |
| 🔵 | PreluFwdOp | test_prelu_manifest_bench[cnn-feat-per-channel-deep-bfloat16] | 0.0082 | 1.57 | 3.14 | torch 314.1%, torch-compile 100.0% | - |
| 🟡 | ProdFwdOp | test_prod_bench[hidden-state-reduce-float16] | 0.0079 | 1.07 | 2.13 | flaggems 99.6%, torch 624.8%, torch-compile 105.3% | - |
| 🔵 | ProdFwdOp | test_prod_bench[hidden-state-reduce-bfloat16] | 0.0075 | 1.12 | 2.25 | flaggems 104.5%, torch 664.0%, torch-compile 111.8% | - |
| 🔵 | ProdFwdOp | test_prod_bench[long-seq-reduce-bfloat16] | 0.0043 | 0.49 | 0.98 | flaggems 317.2%, torch 390.8%, torch-compile 105.2% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-8b-prefill-float16] | 0.0119 | 2.83 | 2.83 | flaggems 106.7%, flashinfer 92.5%, vllm 105.1%, torch-ref 1226.8%, torch-compile 114.5% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-8b-prefill-bfloat16] | 0.0126 | 2.65 | 2.66 | flaggems 99.0%, flashinfer 86.1%, vllm 100.5%, torch-ref 1155.7%, torch-compile 114.4% | - |
| 🔵 | RMSNormFwdOp | test_rms_norm_bench[llama-8b-decode-bfloat16] | 0.0020 | 0.01 | 0.01 | flaggems 162.5%, flashinfer 104.7%, vllm 130.5%, torch-ref 875.8%, torch-compile 131.2% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-70b-prefill-float16] | 0.0210 | 3.19 | 3.19 | flaggems 98.8%, flashinfer 95.6%, vllm 103.0%, torch-ref 1285.7%, torch-compile 93.9% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-70b-prefill-bfloat16] | 0.0219 | 3.07 | 3.07 | flaggems 97.5%, flashinfer 92.0%, vllm 101.0%, torch-ref 1239.4%, torch-compile 94.3% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-70b-decode-bfloat16] | 0.0026 | 0.01 | 0.02 | flaggems 157.3%, flashinfer 100.0%, vllm 118.3%, torch-ref 713.4%, torch-compile 138.4% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-405b-prefill-float16] | 0.0419 | 3.20 | 3.20 | flaggems 95.3%, flashinfer 88.4%, vllm 116.6%, torch-ref 1216.7%, torch-compile 94.6% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-405b-prefill-bfloat16] | 0.0429 | 3.13 | 3.13 | flaggems 95.5%, flashinfer 88.2%, vllm 113.6%, torch-ref 1191.7%, torch-compile 95.2% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-405b-decode-bfloat16] | 0.0036 | 0.02 | 0.03 | flaggems 128.3%, flashinfer 97.4%, vllm 120.3%, torch-ref 556.6%, torch-compile 118.1% | - |
| 🟡 | ReciprocalFwdOp | test_reciprocal_bench[elementwise-16M-float16] | 0.0189 | 0.89 | 3.55 | torch 100.1%, torch-compile 96.3% | - |
| 🟡 | ReciprocalFwdOp | test_reciprocal_bench[elementwise-16M-bfloat16] | 0.0189 | 0.89 | 3.54 | torch 100.2%, torch-compile 96.5% | - |
| 🔵 | ReciprocalFwdOp | test_reciprocal_bench[elementwise-16M-float32] | 0.0335 | 0.50 | 4.01 | torch 101.4%, torch-compile 100.9% | - |
| 🟡 | ReciprocalFwdOp | test_reciprocal_bench[elementwise-256M-float16] | 0.2671 | 1.01 | 4.02 | torch 100.0%, torch-compile 95.9% | - |
| 🟡 | ReciprocalFwdOp | test_reciprocal_bench[elementwise-256M-bfloat16] | 0.2673 | 1.00 | 4.02 | torch 100.0%, torch-compile 96.5% | - |
| 🔵 | ReluFwdOp | test_relu_manifest_bench[hidden-state-prefill-float16] | 0.0103 | 0.81 | 3.25 | torch 104.3%, torch-compile 100.0% | - |
| 🔵 | ReluFwdOp | test_relu_manifest_bench[hidden-state-prefill-bfloat16] | 0.0103 | 0.81 | 3.25 | torch 101.9%, torch-compile 100.3% | - |
| 🔵 | ReluFwdOp | test_relu_manifest_bench[hidden-state-decode-bfloat16] | 0.0012 | 0.00 | 0.01 | torch 115.8%, torch-compile 100.1% | - |
| 🔵 | RemainderFwdOp | test_binary_arith_bench[remainder-1024x4096-float16-float16-RemainderFwdOp-remainder-positive] | 0.0086 | 0.49 | 2.93 | torch 124.2%, torch-compile 100.4% | - |
| 🔵 | RemainderFwdOp | test_binary_arith_bench[remainder-1024x10240-float16-float16-RemainderFwdOp-remainder-positive] | 0.0181 | 0.58 | 3.48 | torch 119.8%, torch-compile 100.5% | - |
| 🔵 | RemainderFwdOp | test_remainder_manifest_bench[hidden-state-prefill-float16] | 0.0154 | 2.18 | 3.26 | torch 117.2%, torch-compile 100.8% | - |
| 🔵 | RemainderFwdOp | test_remainder_manifest_bench[hidden-state-prefill-bfloat16] | 0.0149 | 2.25 | 3.37 | torch 124.2%, torch-compile 101.1% | - |
| 🔵 | RemainderFwdOp | test_remainder_manifest_bench[hidden-state-prefill-float32] | 0.0264 | 1.27 | 3.81 | torch 103.0%, torch-compile 101.1% | - |
| 🔵 | RemainderFwdOp | test_remainder_manifest_bench[cnn-feat-broadcast-float16] | 0.0160 | 3.20 | 3.20 | torch 388.6%, torch-compile 110.8% | - |
| 🔵 | RemainderFwdOp | test_remainder_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0161 | 3.19 | 3.19 | torch 398.8%, torch-compile 115.5% | - |
| 🟡 | RemainderFwdOp | test_remainder_manifest_bench[cnn-feat-broadcast-float32] | 0.0269 | 1.91 | 3.81 | torch 238.6%, torch-compile 99.5% | - |
| 🔵 | RopeLlama31FwdOp | test_rope_llama31_bench[llama31-1d-8k-d128-bfloat16] | 0.0036 | 1.16 | 1.74 | torch-ref 439.9%, torch-compile 114.2% | - |
| 🔴 | RopeLlama31FwdOp | test_rope_llama31_bench[llama31-2d-b1-s8k-h32-d128-float16] | 0.0594 | 2.26 | 2.30 | torch-ref 829.9%, torch-compile 58.8% | - |
| 🔵 | RopeLongRopeFwdOp | test_rope_longrope_bench[longrope-1d-8k-d128-bfloat16] | 0.0036 | 1.17 | 1.76 | torch-ref 442.9%, torch-compile 116.0% | - |
| 🔴 | RopeLongRopeFwdOp | test_rope_longrope_bench[longrope-2d-b1-s8k-h32-d128-float16] | 0.0595 | 2.25 | 2.29 | torch-ref 828.4%, torch-compile 58.6% | - |
| 🔵 | RopeNeoxFwdOp | test_rope_neox_bench[neox-1d-2k-d64-float16] | 0.0018 | 0.29 | 0.43 | torch-ref 517.5%, torch-compile 108.8% | - |
| 🔵 | RopeNeoxFwdOp | test_rope_neox_bench[neox-1d-4k-d128-bfloat16] | 0.0026 | 0.81 | 1.21 | torch-ref 475.3%, torch-compile 117.3% | - |
| 🔴 | RopeNeoxFwdOp | test_rope_neox_bench[neox-2d-b2-s2k-h32-d128-float16] | 0.0308 | 2.18 | 2.19 | torch-ref 881.0%, torch-compile 59.8% | - |
| 🔴 | RopeNeoxPositionIdsFwdOp | test_rope_neox_position_ids_bench[position-ids-s2k-h32-d128-float16] | 0.0278 | 1.21 | 1.24 | vllm 87.2%, torch-ref 465.7%, torch-compile 42.6% | - |
| 🔴 | RopeNeoxPositionIdsFwdOp | test_rope_neox_position_ids_bench[position-ids-s4k-h32-d128-bfloat16] | 0.0457 | 1.47 | 1.51 | vllm 97.4%, torch-ref 544.6%, torch-compile 48.6% | - |
| 🟡 | RopeNonNeoxFwdOp | test_rope_non_neox_bench[non-neox-1d-2k-d64-float16] | 0.0022 | 0.24 | 0.36 | torch-ref 435.2%, torch-compile 92.7% | - |
| 🔴 | RopeNonNeoxFwdOp | test_rope_non_neox_bench[non-neox-2d-b2-s2k-h32-d128-bfloat16] | 0.0252 | 2.66 | 2.69 | torch-ref 1088.7%, torch-compile 75.5% | - |
| 🔵 | RopeYarnFwdOp | test_rope_yarn_bench[yarn-1d-8k-d128-bfloat16] | 0.0036 | 1.16 | 1.74 | torch-ref 439.8%, torch-compile 115.0% | - |
| 🔴 | RopeYarnFwdOp | test_rope_yarn_bench[yarn-2d-b1-s8k-h32-d128-float16] | 0.0595 | 2.25 | 2.29 | torch-ref 827.1%, torch-compile 58.6% | - |
| 🔵 | RoundFwdOp | test_round_bench[elementwise-16M-float16] | 0.0179 | 0.94 | 3.74 | torch 100.4%, torch-compile 100.2% | - |
| 🔵 | RoundFwdOp | test_round_bench[elementwise-16M-bfloat16] | 0.0179 | 0.94 | 3.75 | torch 100.3%, torch-compile 100.1% | - |
| 🟡 | RoundFwdOp | test_round_bench[elementwise-16M-float32] | 0.0340 | 0.49 | 3.95 | torch 99.9%, torch-compile 99.9% | - |
| 🟡 | RoundFwdOp | test_round_bench[elementwise-256M-float16] | 0.2506 | 1.07 | 4.28 | torch 99.9%, torch-compile 99.7% | - |
| 🔵 | RoundFwdOp | test_round_bench[elementwise-256M-bfloat16] | 0.2498 | 1.07 | 4.30 | torch 100.2%, torch-compile 100.1% | - |
| 🔵 | RsqrtFwdOp | test_rsqrt_bench[elementwise-16M-float16] | 0.0181 | 0.93 | 3.71 | torch 100.5%, torch-compile 100.4% | - |
| 🔵 | RsqrtFwdOp | test_rsqrt_bench[elementwise-16M-bfloat16] | 0.0181 | 0.93 | 3.71 | torch 100.5%, torch-compile 100.2% | - |
| 🔵 | RsqrtFwdOp | test_rsqrt_bench[elementwise-16M-float32] | 0.0331 | 0.51 | 4.05 | torch 101.9%, torch-compile 101.6% | - |
| 🟡 | RsqrtFwdOp | test_rsqrt_bench[elementwise-256M-float16] | 0.2537 | 1.06 | 4.23 | torch 100.0%, torch-compile 99.8% | - |
| 🔵 | RsqrtFwdOp | test_rsqrt_bench[elementwise-256M-bfloat16] | 0.2530 | 1.06 | 4.24 | torch 100.4%, torch-compile 100.1% | - |
| 🔵 | SSDChunkScanFwdOp | test_ssd_chunk_scan_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0732 | 88.07 | 1.44 | mamba 137.6%, torch-ref 2678.9%, torch-compile 693.5% | - |
| 🔵 | SSDChunkScanFwdOp | test_ssd_chunk_scan_fwd_bench[mamba2-780m-b1-s4k-bfloat16] | 0.0759 | 84.88 | 1.38 | mamba 134.1%, torch-ref 2584.6%, torch-compile 670.6% | - |
| 🔵 | SSDChunkScanFwdOp | test_ssd_chunk_scan_fwd_bench[mamba2-2p7b-b4-s2k-bfloat16] | 0.2372 | 90.54 | 1.46 | mamba 130.2%, torch-ref 2745.9%, torch-compile 691.2% | - |
| 🔵 | SSDChunkScanFwdOp | test_ssd_chunk_scan_fwd_bench[mamba2-1p3b-b2-s32k-float16] | 1.4677 | 93.64 | 1.51 | mamba 138.6%, torch-ref 2729.8%, torch-compile 680.1% | - |
| 🔵 | SSDChunkStateFwdOp | test_ssd_chunk_state_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0238 | 135.86 | 2.21 | mamba 105.1%, torch-ref 34172.5%, torch-compile 2659.3% | - |
| 🔵 | SSDChunkStateFwdOp | test_ssd_chunk_state_fwd_bench[mamba2-780m-b1-s4k-bfloat16] | 0.0240 | 134.78 | 2.19 | mamba 110.3%, torch-ref 33920.1%, torch-compile 2814.7% | - |
| 🔵 | SSDChunkStateFwdOp | test_ssd_chunk_state_fwd_bench[mamba2-2p7b-b4-s2k-bfloat16] | 0.0656 | 164.44 | 2.65 | mamba 122.3%, torch-ref 41360.9%, torch-compile 3733.8% | - |
| 🔵 | SSDChunkStateFwdOp | test_ssd_chunk_state_fwd_bench[mamba2-780m-b1-s4k-seq-idx-float16] | 0.0287 | 112.62 | 1.83 | mamba 120.7%, torch-ref 28367.7%, torch-compile 2611.0% | - |
| 🔵 | SSDChunkStateFwdOp | test_ssd_chunk_state_fwd_bench[mamba2-780m-b1-s4k-seq-idx-bfloat16] | 0.0290 | 111.69 | 1.82 | mamba 100.9%, torch-ref 28149.4%, torch-compile 2717.6% | - |
| 🔵 | SSDChunkStateFwdOp | test_ssd_chunk_state_fwd_bench[mamba2-1p3b-b2-s32k-seq-idx-float16] | 0.4492 | 153.62 | 2.48 | mamba 140.6%, torch-ref 38558.4%, torch-compile 3711.2% | - |
| 🟢 | SSDDecodeFwdOp | test_ssd_decode_bench[mamba2-1p3b-decode-b1-float16] | 0.0040 | 1.06 | 1.60 | torch-ref 765.3%, torch-compile 228.2% | - |
| 🟢 | SSDDecodeFwdOp | test_ssd_decode_bench[mamba2-1p3b-decode-b1-bfloat16] | 0.0040 | 1.06 | 1.60 | torch-ref 767.3%, torch-compile 229.8% | - |
| 🟢 | SSDDecodeFwdOp | test_ssd_decode_bench[mamba2-2p7b-decode-b8-float16] | 0.0163 | 2.57 | 2.76 | torch-ref 685.5%, torch-compile 184.3% | - |
| 🟢 | SSDDecodeFwdOp | test_ssd_decode_bench[mamba2-780m-decode-b32-float16] | 0.0361 | 2.79 | 2.86 | torch-ref 667.5%, torch-compile 192.5% | - |
| 🟢 | SSDStatePassingFwdOp | test_ssd_state_passing_fwd_bench[mamba2-1p3b-b1-s4k-dstate-float16] | 0.0020 | 0.13 | 0.42 | mamba 431.4%, torch-ref 6229.6%, torch-compile 209.9% | - |
| 🟢 | SSDStatePassingFwdOp | test_ssd_state_passing_fwd_bench[mamba2-1p3b-b1-s4k-dstate-bfloat16] | 0.0020 | 0.13 | 0.42 | mamba 427.9%, torch-ref 6296.7%, torch-compile 209.8% | - |
| 🟢 | SSDStatePassingFwdOp | test_ssd_state_passing_fwd_bench[mamba2-2p7b-b2-s32k-dstate-float16] | 0.0106 | 0.50 | 1.50 | mamba 565.4%, torch-ref 10892.4%, torch-compile 861.3% | - |
| 🟢 | SSDStatePassingFwdOp | test_ssd_state_passing_fwd_bench[mamba2-1p3b-b1-s4k-dstate-init-states-float16] | 0.0020 | 0.13 | 0.43 | mamba 435.2%, torch-ref 6029.0%, torch-compile 171.2% | - |
| 🔵 | SSDStatePassingFwdOp | test_ssd_state_passing_fwd_bench[mamba2-1p3b-b1-s4k-dstate-init-states-bfloat16] | 0.0020 | 0.13 | 0.43 | mamba 442.3%, torch-ref 6198.4%, torch-compile 110.6% | - |
| 🟡 | SSDStatePassingFwdOp | test_ssd_state_passing_fwd_bench[mamba2-1p3b-b1-s4k-flat-init-states-float32] | 0.0219 | 0.77 | 3.25 | mamba 98.4%, torch-ref 579.3%, torch-compile 93.1% | - |
| 🔵 | SeluFwdOp | test_selu_manifest_bench[snn-fc-float16] | 0.0117 | 3.57 | 2.86 | torch 152.9%, torch-compile 137.1% | - |
| 🔵 | SeluFwdOp | test_selu_manifest_bench[snn-fc-bfloat16] | 0.0121 | 3.47 | 2.77 | torch 150.5%, torch-compile 129.1% | - |
| 🔵 | SeluFwdOp | test_selu_manifest_bench[snn-fc-wide-float16] | 0.0210 | 3.99 | 3.19 | torch 155.9%, torch-compile 142.2% | - |
| 🔵 | SeluFwdOp | test_selu_manifest_bench[snn-fc-wide-bfloat16] | 0.0218 | 3.85 | 3.08 | torch 153.0%, torch-compile 134.0% | - |
| 🔴 | SharedFusedMoE | test_shared_fused_moe_bench[1-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 2.5280 | 0.59 | 0.59 | vllm 16.9% | - |
| 🟡 | SharedFusedMoE | test_shared_fused_moe_bench[32-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 4.7455 | 10.10 | 3.66 | vllm 83.5% | - |
| 🔵 | SharedFusedMoE | test_shared_fused_moe_bench[512-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 8.0566 | 95.16 | 4.30 | vllm 108.9% | - |
| 🔴 | SharedFusedMoE | test_shared_fused_moe_bench[2048-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 19.5743 | 156.66 | 1.77 | vllm 59.3% | - |
| 🔴 | SharedFusedMoE | test_shared_fused_moe_bench[4096-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 32.5463 | 188.45 | 1.07 | vllm 44.9% | - |
| 🟡 | SigmoidFwdOp | test_sigmoid_manifest_bench[elementwise-16M-float16] | 0.0214 | 3.13 | 3.13 | torch 107.2%, torch-compile 86.9% | - |
| 🟡 | SigmoidFwdOp | test_sigmoid_manifest_bench[elementwise-16M-bfloat16] | 0.0218 | 3.08 | 3.08 | torch 107.8%, torch-compile 85.6% | - |
| 🟡 | SigmoidFwdOp | test_sigmoid_manifest_bench[elementwise-16M-float32] | 0.0344 | 1.95 | 3.91 | torch 100.0%, torch-compile 99.0% | - |
| 🟡 | SigmoidFwdOp | test_sigmoid_manifest_bench[elementwise-256M-float16] | 0.3018 | 3.56 | 3.56 | torch 106.6%, torch-compile 86.3% | - |
| 🟡 | SigmoidFwdOp | test_sigmoid_manifest_bench[elementwise-256M-bfloat16] | 0.3084 | 3.48 | 3.48 | torch 107.3%, torch-compile 85.4% | - |
| 🟡 | SignFwdOp | test_sign_bench[elementwise-16M-float16] | 0.0186 | 1.80 | 3.61 | torch 97.4%, torch-compile 96.6% | - |
| 🟡 | SignFwdOp | test_sign_bench[elementwise-16M-bfloat16] | 0.0186 | 1.80 | 3.61 | torch 97.9%, torch-compile 96.9% | - |
| 🟡 | SignFwdOp | test_sign_bench[elementwise-16M-float32] | 0.0341 | 0.99 | 3.94 | torch 99.8%, torch-compile 99.7% | - |
| 🟡 | SignFwdOp | test_sign_bench[elementwise-256M-float16] | 0.2636 | 2.04 | 4.07 | torch 97.1%, torch-compile 95.6% | - |
| 🟡 | SignFwdOp | test_sign_bench[elementwise-256M-bfloat16] | 0.2635 | 2.04 | 4.07 | torch 98.1%, torch-compile 96.4% | - |
| 🔵 | SiluAndMulFwdOp | test_silu_and_mul_bench[llama-8b-swiglu-prefill-float16] | 0.0434 | 4.06 | 4.06 | flashinfer 123.4%, torch-ref 436.4%, torch-compile 101.8% | - |
| 🔵 | SiluAndMulFwdOp | test_silu_and_mul_bench[llama-8b-swiglu-prefill-bfloat16] | 0.0433 | 4.07 | 4.07 | flashinfer 124.7%, torch-ref 439.3%, torch-compile 105.5% | - |
| 🟡 | SiluAndMulFwdOp | test_silu_and_mul_bench[llama-8b-swiglu-decode-bfloat16] | 0.0017 | 0.05 | 0.05 | flashinfer 248.2%, torch-ref 205.6%, torch-compile 87.1% | - |
| 🟡 | SiluFwdOp | test_silu_manifest_bench[llama-8b-ffn-prefill-float16] | 0.0366 | 4.01 | 3.21 | torch 103.5%, torch-compile 96.9% | - |
| 🟡 | SiluFwdOp | test_silu_manifest_bench[llama-8b-ffn-prefill-bfloat16] | 0.0365 | 4.02 | 3.22 | torch 104.4%, torch-compile 98.2% | - |
| 🟡 | SiluFwdOp | test_silu_manifest_bench[llama-8b-ffn-decode-bfloat16] | 0.0015 | 0.05 | 0.04 | torch 129.8%, torch-compile 95.7% | - |
| 🔵 | SinFwdOp | test_sin_bench[elementwise-16M-float16] | 0.0254 | 0.66 | 2.64 | torch 103.3%, torch-compile 104.5% | - |
| 🔵 | SinFwdOp | test_sin_bench[elementwise-16M-bfloat16] | 0.0258 | 0.65 | 2.60 | torch 103.7%, torch-compile 104.7% | - |
| 🟡 | SinFwdOp | test_sin_bench[elementwise-16M-float32] | 0.0349 | 0.48 | 3.85 | torch 98.4%, torch-compile 98.3% | - |
| 🔵 | SinFwdOp | test_sin_bench[elementwise-256M-float16] | 0.3669 | 0.73 | 2.93 | torch 102.9%, torch-compile 104.9% | - |
| 🔵 | SinFwdOp | test_sin_bench[elementwise-256M-bfloat16] | 0.3740 | 0.72 | 2.87 | torch 103.2%, torch-compile 104.4% | - |
| 🔵 | SinusoidalFwdOp | test_sinusoidal_bench[transformer-2k-4k-float16] | 0.0424 | 1.19 | 0.40 | torch-ref 250.9%, torch-compile 133.7% | - |
| 🔵 | SinusoidalFwdOp | test_sinusoidal_bench[transformer-2k-4k-bfloat16] | 0.0424 | 1.19 | 0.40 | torch-ref 251.5%, torch-compile 133.7% | - |
| 🔵 | SinusoidalFwdOp | test_sinusoidal_bench[transformer-4k-4k-float16] | 0.0818 | 1.23 | 0.41 | torch-ref 243.6%, torch-compile 136.5% | - |
| 🔵 | SinusoidalFwdOp | test_sinusoidal_bench[transformer-4k-4k-bfloat16] | 0.0819 | 1.23 | 0.41 | torch-ref 243.4%, torch-compile 136.4% | - |
| 🔵 | SoftmaxFwdOp | test_softmax_bench[attn-weights-4k-float16] | 0.0084 | 2.49 | 1.99 | flaggems 102.3%, torch 235.4%, torch-compile 191.6% | - |
| 🔵 | SoftmaxFwdOp | test_softmax_bench[attn-weights-4k-bfloat16] | 0.0084 | 2.50 | 2.00 | flaggems 103.4%, torch 234.4%, torch-compile 198.8% | - |
| 🔵 | SoftmaxFwdOp | test_softmax_bench[attn-weights-4k-float32] | 0.0110 | 1.90 | 3.04 | flaggems 100.3%, torch 183.3%, torch-compile 167.0% | - |
| 🔵 | SoftmaxFwdOp | test_softmax_bench[attn-weights-32k-bfloat16] | 0.0615 | 2.73 | 2.18 | flaggems 104.6%, torch 135.5%, torch-compile 153.2% | - |
| 🔴 | SoftmaxFwdOp | test_softmax_bench[lm-head-logits-float16] | 0.0284 | 0.07 | 0.06 | flaggems 99.0%, torch 116.9%, torch-compile 33.5% | - |
| 🔴 | SoftmaxFwdOp | test_softmax_bench[lm-head-logits-bfloat16] | 0.0308 | 0.07 | 0.05 | flaggems 96.4%, torch 110.3%, torch-compile 30.9% | - |
| 🔴 | SoftmaxFwdOp | test_softmax_bench[lm-head-logits-float32] | 0.0348 | 0.06 | 0.09 | flaggems 90.0%, torch 113.2%, torch-compile 28.1% | - |
| 🔵 | SoftplusFwdOp | test_softplus_manifest_bench[mlp-hidden-float16] | 0.0126 | 3.33 | 2.66 | torch 189.1%, torch-compile 142.1% | - |
| 🔵 | SoftplusFwdOp | test_softplus_manifest_bench[mlp-hidden-bfloat16] | 0.0128 | 3.28 | 2.62 | torch 188.2%, torch-compile 143.0% | - |
| 🔵 | SoftplusFwdOp | test_softplus_manifest_bench[mlp-hidden-wide-float16] | 0.0228 | 3.67 | 2.94 | torch 196.2%, torch-compile 144.5% | - |
| 🔵 | SoftplusFwdOp | test_softplus_manifest_bench[mlp-hidden-wide-bfloat16] | 0.0233 | 3.61 | 2.88 | torch 194.9%, torch-compile 145.5% | - |
| 🔵 | SqrtFwdOp | test_sqrt_bench[elementwise-16M-float16] | 0.0186 | 0.90 | 3.60 | torch 101.4%, torch-compile 100.0% | - |
| 🔵 | SqrtFwdOp | test_sqrt_bench[elementwise-16M-bfloat16] | 0.0187 | 0.90 | 3.59 | torch 101.4%, torch-compile 100.2% | - |
| 🔵 | SqrtFwdOp | test_sqrt_bench[elementwise-16M-float32] | 0.0334 | 0.50 | 4.02 | torch 101.9%, torch-compile 101.7% | - |
| 🔵 | SqrtFwdOp | test_sqrt_bench[elementwise-256M-float16] | 0.2628 | 1.02 | 4.09 | torch 101.2%, torch-compile 100.0% | - |
| 🔵 | SqrtFwdOp | test_sqrt_bench[elementwise-256M-bfloat16] | 0.2636 | 1.02 | 4.07 | torch 101.3%, torch-compile 100.2% | - |
| 🔵 | StdFwdOp | test_std_bench[hidden-state-std-float16] | 0.0084 | 4.97 | 1.99 | flaggems 125.4%, torch 802.3%, torch-compile 222.3% | - |
| 🔵 | StdFwdOp | test_std_bench[hidden-state-std-bfloat16] | 0.0085 | 4.93 | 1.97 | flaggems 130.4%, torch 798.9%, torch-compile 226.3% | - |
| 🔵 | StdFwdOp | test_std_bench[long-seq-std-bfloat16] | 0.0052 | 2.02 | 0.81 | flaggems 254.3%, torch 480.2%, torch-compile 119.1% | - |
| 🔴 | StdFwdOp | test_std_bench[3d-multidim-reduce-float16] | 0.0121 | 0.87 | 0.35 | flaggems 118.3%, torch 222.9%, torch-compile 52.2% | - |
| 🔵 | SubFwdOp | test_binary_arith_bench[sub-1024x4096-float16-float16-SubFwdOp-sub-normal] | 0.0084 | 0.50 | 2.99 | torch 101.2%, torch-compile 100.6% | - |
| 🔵 | SubFwdOp | test_binary_arith_bench[sub-1024x10240-float16-float16-SubFwdOp-sub-normal] | 0.0176 | 0.59 | 3.57 | torch 100.5%, torch-compile 100.0% | - |
| 🔵 | SubFwdOp | test_binary_arith_bench[sub-1024x11008-float16-float16-SubFwdOp-sub-normal] | 0.0185 | 0.61 | 3.65 | torch 100.3%, torch-compile 100.2% | - |
| 🔵 | SubFwdOp | test_sub_manifest_bench[hidden-state-prefill-float16] | 0.0148 | 1.13 | 3.40 | torch 100.2%, torch-compile 100.2% | - |
| 🔵 | SubFwdOp | test_sub_manifest_bench[hidden-state-prefill-bfloat16] | 0.0148 | 1.13 | 3.40 | torch 100.8%, torch-compile 100.2% | - |
| 🟡 | SubFwdOp | test_sub_manifest_bench[hidden-state-prefill-float32] | 0.0265 | 0.63 | 3.80 | torch 100.1%, torch-compile 99.9% | - |
| 🔵 | SubFwdOp | test_sub_manifest_bench[cnn-feat-broadcast-float16] | 0.0144 | 1.78 | 3.56 | torch 317.5%, torch-compile 100.0% | - |
| 🟡 | SubFwdOp | test_sub_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0145 | 1.77 | 3.54 | torch 319.6%, torch-compile 99.8% | - |
| 🟡 | SubFwdOp | test_sub_manifest_bench[cnn-feat-broadcast-float32] | 0.0265 | 0.97 | 3.87 | torch 187.3%, torch-compile 99.9% | - |
| 🔵 | SumFwdOp | test_sum_bench[hidden-state-reduce-float16] | 0.0074 | 1.13 | 2.26 | flaggems 118.1%, torch 666.0%, torch-compile 112.5% | - |
| 🔵 | SumFwdOp | test_sum_bench[hidden-state-reduce-bfloat16] | 0.0074 | 1.13 | 2.26 | flaggems 118.5%, torch 670.7%, torch-compile 113.4% | - |
| 🟡 | SumFwdOp | test_sum_bench[long-seq-reduce-bfloat16] | 0.0041 | 0.52 | 1.03 | flaggems 93.7%, torch 416.5%, torch-compile 108.7% | - |
| 🟡 | SumFwdOp | test_sum_bench[hidden-state-reduce-dim0-bfloat16] | 0.0121 | 0.69 | 1.38 | flaggems 112.7%, torch 368.5%, torch-compile 91.8% | - |
| 🔵 | SumFwdOp | test_sum_bench[hidden-state-reduce-keepdim-bfloat16] | 0.0075 | 1.13 | 2.25 | flaggems 118.0%, torch 669.0%, torch-compile 112.9% | - |
| 🔴 | SumFwdOp | test_sum_bench[3d-multidim-reduce-float16] | 0.0113 | 0.19 | 0.37 | flaggems 119.3%, torch 170.8%, torch-compile 40.5% | - |
| 🟡 | TanhFwdOp | test_tanh_manifest_bench[elementwise-16M-float16] | 0.0208 | 0.81 | 3.23 | torch 99.7%, torch-compile 116.3% | - |
| 🔵 | TanhFwdOp | test_tanh_manifest_bench[elementwise-16M-bfloat16] | 0.0213 | 0.79 | 3.14 | torch 102.6%, torch-compile 115.4% | - |
| 🔵 | TanhFwdOp | test_tanh_manifest_bench[elementwise-16M-float32] | 0.0339 | 0.50 | 3.96 | torch 100.7%, torch-compile 101.5% | - |
| 🟡 | TanhFwdOp | test_tanh_manifest_bench[elementwise-256M-float16] | 0.2956 | 0.91 | 3.63 | torch 98.7%, torch-compile 116.5% | - |
| 🔵 | TanhFwdOp | test_tanh_manifest_bench[elementwise-256M-bfloat16] | 0.3031 | 0.89 | 3.54 | torch 102.2%, torch-compile 115.5% | - |
| 🔴 | TopkSelectorFwdOp | test_topk_selector_bench[topk1024-s32k-kv64k-float32] | 15.6297 | 0.14 | 0.56 | torch 203.6%, torch-compile 203.6%, flashinfer 59.3% | - |
| 🔴 | TopkSelectorFwdOp | test_topk_selector_bench[topk2048-s32k-kv64k-float32] | 16.2375 | 0.13 | 0.55 | torch 205.0%, torch-compile 205.1%, flashinfer 65.7% | - |
| 🔵 | TruncFwdOp | test_trunc_bench[elementwise-16M-float16] | 0.0179 | 0.94 | 3.75 | torch 100.4%, torch-compile 100.2% | - |
| 🔵 | TruncFwdOp | test_trunc_bench[elementwise-16M-bfloat16] | 0.0179 | 0.94 | 3.75 | torch 100.5%, torch-compile 100.2% | - |
| 🟡 | TruncFwdOp | test_trunc_bench[elementwise-16M-float32] | 0.0340 | 0.49 | 3.95 | torch 99.8%, torch-compile 99.7% | - |
| 🔵 | TruncFwdOp | test_trunc_bench[elementwise-256M-float16] | 0.2498 | 1.07 | 4.30 | torch 100.2%, torch-compile 100.0% | - |
| 🟡 | TruncFwdOp | test_trunc_bench[elementwise-256M-bfloat16] | 0.2505 | 1.07 | 4.29 | torch 99.9%, torch-compile 99.9% | - |
| 🟢 | VarFwdOp | test_var_bench[hidden-state-var-float16] | 0.0084 | 5.02 | 2.01 | flaggems 179.7%, torch 810.3%, torch-compile 218.6% | - |
| 🟢 | VarFwdOp | test_var_bench[hidden-state-var-bfloat16] | 0.0084 | 5.01 | 2.01 | flaggems 184.3%, torch 812.2%, torch-compile 224.5% | - |
| 🔵 | VarFwdOp | test_var_bench[long-seq-var-bfloat16] | 0.0052 | 2.04 | 0.81 | flaggems 216.2%, torch 483.2%, torch-compile 118.7% | - |
| 🔴 | VarFwdOp | test_var_bench[3d-multidim-reduce-float16] | 0.0120 | 0.87 | 0.35 | flaggems 117.9%, torch 223.7%, torch-compile 50.4% | - |
| 🟢 | VarMeanFwdOp | test_var_mean_bench[hidden-state-var-mean-float16] | 0.0084 | 5.00 | 2.00 | flaggems 179.8%, torch 1390.6%, torch-compile 250.0% | - |
| 🟢 | VarMeanFwdOp | test_var_mean_bench[hidden-state-var-mean-bfloat16] | 0.0084 | 4.98 | 1.99 | flaggems 184.4%, torch 1390.9%, torch-compile 259.7% | - |
| 🔵 | VarMeanFwdOp | test_var_mean_bench[long-seq-var-mean-bfloat16] | 0.0052 | 2.04 | 0.81 | flaggems 216.2%, torch 787.6%, torch-compile 147.2% | - |
| 🔴 | VarMeanFwdOp | test_var_mean_bench[3d-multidim-reduce-float16] | 0.0121 | 0.86 | 0.35 | flaggems 116.9%, torch 373.1%, torch-compile 62.5% | - |
| 🟡 | WhereFwdOp | test_where_manifest_bench[elementwise-16M-float16] | 0.0309 | 0.54 | 3.80 | torch 99.3%, torch-compile 99.1% | - |
| 🟡 | WhereFwdOp | test_where_manifest_bench[elementwise-16M-bfloat16] | 0.0311 | 0.54 | 3.77 | torch 99.0%, torch-compile 98.7% | - |
| 🟡 | WhereFwdOp | test_where_manifest_bench[elementwise-16M-float32] | 0.0533 | 0.31 | 4.09 | torch 100.3%, torch-compile 99.6% | - |
| 🟡 | WhereFwdOp | test_where_manifest_bench[elementwise-256M-float16] | 0.4291 | 0.63 | 4.38 | torch 99.8%, torch-compile 99.8% | - |
| 🟡 | WhereFwdOp | test_where_manifest_bench[elementwise-256M-bfloat16] | 0.4286 | 0.63 | 4.38 | torch 99.9%, torch-compile 99.9% | - |
| 🟡 | div_bcast | test_broadcast_bench[div-1024x4096-1x4096-float16-DivFwdOp-div-positive] | 0.0065 | 0.65 | 2.60 | torch 252.0%, torch-compile 96.0% | - |
| 🟡 | div_bcast | test_broadcast_bench[div-1024x10240-1x10240-float16-DivFwdOp-div-positive] | 0.0133 | 0.79 | 3.14 | torch 272.2%, torch-compile 92.3% | - |
| 🟡 | div_bcast | test_broadcast_bench[div-1024x11008-1x11008-float16-DivFwdOp-div-positive] | 0.0141 | 0.80 | 3.19 | torch 274.0%, torch-compile 92.8% | - |
| 🔴 | gelu_and_mul_strategy | test_fused_gated_strategy_bench[gelu_and_mul-1024-4096-float16-GeluAndMulFwdKernel-direct] | 0.0216 | 0.39 | 1.16 | torch 154.6%, torch-compile 49.3% | - |
| 🔵 | gelu_and_mul_strategy | test_fused_gated_strategy_bench[gelu_and_mul-1024-4096-float16-GeluAndMulFwdKernel-explicit_parallel] | 0.0100 | 0.84 | 2.51 | torch 333.5%, torch-compile 106.4% | - |
| 🔴 | gelu_tanh_and_mul_strategy | test_fused_gated_strategy_bench[gelu_tanh_and_mul-1024-4096-float16-GeluTanhAndMulFwdKernel-direct] | 0.0216 | 0.39 | 1.16 | torch 147.5%, torch-compile 45.1% | - |
| 🔵 | gelu_tanh_and_mul_strategy | test_fused_gated_strategy_bench[gelu_tanh_and_mul-1024-4096-float16-GeluTanhAndMulFwdKernel-explicit_parallel] | 0.0088 | 0.95 | 2.85 | torch 361.2%, torch-compile 110.9% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-up-T=32768] | 18.1814 | 725.70 | 1.00 | torch 126.9%, deepgemm 101.7%, triton 152.0%, triton-tma 127.3% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-up-T=65536] | 37.5122 | 703.46 | 0.63 | torch 105.7%, deepgemm 109.6%, triton 145.8%, triton-tma 110.0% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-up-T=131072] | 74.8445 | 705.15 | 0.46 | torch 107.5%, deepgemm 100.2%, triton 142.0%, triton-tma 113.5% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-up-T=262144] | 151.3490 | 697.42 | 0.37 | torch 112.4%, deepgemm 100.4%, triton 142.9%, triton-tma 108.0% | - |
| 🟡 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[Llama4-128E-up-T=131072] | 31.0676 | 707.82 | 0.87 | torch 103.5%, deepgemm 99.4%, triton 168.1%, triton-tma 131.4% | - |
| 🟡 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[qwen3.5-397B-up-T52429] | 12.6930 | 692.99 | 1.18 | torch 106.5%, deepgemm 100.0%, triton 154.4%, triton-tma 145.7% | - |
| 🟡 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-down-T=32768] | 9.6454 | 683.96 | 1.11 | torch 103.1%, deepgemm 99.6%, triton 152.3%, triton-tma 118.6% | - |
| 🟡 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-down-T=65536] | 19.1609 | 688.60 | 0.78 | torch 128.5%, deepgemm 98.0%, triton 150.9%, triton-tma 109.3% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-down-T=131072] | 38.4690 | 685.96 | 0.61 | torch 117.6%, deepgemm 115.1%, triton 150.0%, triton-tma 114.8% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-down-T=262144] | 77.8555 | 677.88 | 0.52 | torch 105.6%, deepgemm 100.2%, triton 147.8%, triton-tma 108.3% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[Llama4-128E-down-T=131072] | 15.2954 | 718.85 | 0.93 | torch 103.5%, deepgemm 101.4%, triton 150.6%, triton-tma 123.4% | - |
| 🟡 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[qwen3.5-397B-down-T52429] | 6.9651 | 631.44 | 1.39 | torch 105.7%, deepgemm 95.0%, triton 146.7%, triton-tma 129.8% | - |
| 🔴 | grouped_gemm_nn | test_grouped_gemm_bench[nn-batch16-m4096-n4096-k4096-float16] | 0.3407 | 403.44 | 1.77 | torch-ref 90.2%, torch-compile 80.7%, torch 79.1% | - |
| 🔵 | grouped_gemm_nt | test_grouped_gemm_bench[nt-batch16-m4096-n4096-k4096-float16] | 0.2327 | 590.70 | 2.60 | torch-ref 1000.3%, torch-compile 986.1%, torch 115.3% | - |
| 🟡 | grouped_gemm_nt | test_grouped_gemm_bench[nt-batch16-m4096-n4096-k4096-bfloat16] | 0.2266 | 606.42 | 2.66 | torch-ref 1007.0%, torch-compile 992.5%, torch 99.3% | - |
| 🔴 | grouped_gemm_tn | test_grouped_gemm_bench[tn-batch16-m4096-n4096-k4096-float16] | 0.7820 | 175.75 | 0.77 | torch-ref 67.2%, torch-compile 66.8%, torch 45.1% | - |
| 🔵 | mul_bcast | test_broadcast_bench[mul-1024x4096-1x4096-float16-MulFwdOp-mul-normal] | 0.0060 | 0.70 | 2.81 | torch 248.7%, torch-compile 101.1% | - |
| 🔵 | mul_bcast | test_broadcast_bench[mul-1024x10240-1x10240-float16-MulFwdOp-mul-normal] | 0.0123 | 0.85 | 3.41 | torch 268.3%, torch-compile 100.3% | - |
| 🔵 | mul_bcast | test_broadcast_bench[mul-1024x11008-1x11008-float16-MulFwdOp-mul-normal] | 0.0129 | 0.87 | 3.50 | torch 273.4%, torch-compile 100.2% | - |
| 🔴 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float16-SiluAndMulFwdKernel-direct] | 0.0216 | 0.39 | 1.16 | torch 146.0%, torch-compile 38.6% | - |
| 🔴 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-11008-float16-SiluAndMulFwdKernel-direct] | 0.0555 | 0.41 | 1.22 | torch 138.4%, torch-compile 34.3% | - |
| 🔴 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-4096-4096-float16-SiluAndMulFwdKernel-direct] | 0.0822 | 0.41 | 1.22 | torch 135.3%, torch-compile 32.7% | - |
| 🔴 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-bfloat16-SiluAndMulFwdKernel-direct] | 0.0216 | 0.39 | 1.16 | torch 146.6%, torch-compile 38.9% | - |
| 🔴 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float32-SiluAndMulFwdKernel-direct] | 0.0218 | 0.38 | 2.31 | torch 159.1%, torch-compile 66.9% | - |
| 🟡 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float16-SiluAndMulFwdKernel-explicit_parallel] | 0.0084 | 1.00 | 2.99 | torch 375.8%, torch-compile 98.9% | - |
| 🔵 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-11008-float16-SiluAndMulFwdKernel-explicit_parallel] | 0.0189 | 1.19 | 3.58 | torch 407.4%, torch-compile 100.8% | - |
| 🔵 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-4096-4096-float16-SiluAndMulFwdKernel-explicit_parallel] | 0.0266 | 1.26 | 3.78 | torch 418.0%, torch-compile 101.2% | - |
| 🟡 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-bfloat16-SiluAndMulFwdKernel-explicit_parallel] | 0.0084 | 0.99 | 2.98 | torch 375.4%, torch-compile 99.6% | - |
| 🟡 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float32-SiluAndMulFwdKernel-explicit_parallel] | 0.0148 | 0.57 | 3.40 | torch 234.6%, torch-compile 98.5% | - |
| 🟢 | sub_bcast | test_broadcast_bench[sub-1024x4096-1x4096-float16-SubFwdOp-sub-normal] | 0.0058 | 0.72 | 2.88 | torch 256.6%, torch-compile 159.3% | - |
| 🔵 | sub_bcast | test_broadcast_bench[sub-1024x10240-1x10240-float16-SubFwdOp-sub-normal] | 0.0122 | 0.86 | 3.44 | torch 272.4%, torch-compile 100.5% | - |
| 🔵 | sub_bcast | test_broadcast_bench[sub-1024x11008-1x11008-float16-SubFwdOp-sub-normal] | 0.0130 | 0.87 | 3.48 | torch 273.3%, torch-compile 100.2% | - |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 9 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 735 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 2164 lines in `ops/`, 43.5% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 3140 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

### Never-built kernels

| File | Executed |
| --- | --- |
| `kernels/attention/deepseek_mla_decode.py` | 5.8% |
| `kernels/attention/gqa_fwd_ws.py` | 6.6% |
| `kernels/attention/gqa_fwd_fp8.py` | 9.8% |
| `kernels/attention/gqa_prefill_fwd_ws.py` | 9.9% |
| `kernels/attention/mha_decode_paged.py` | 11.6% |
| `kernels/attention/gqa_decode_bs1_common.py` | 12.4% |
| `kernels/attention/deepseek_nsa_cmp_fwd.py` | 18.3% |
| `kernels/attention/gqa_prefill_varlen_fwd.py` | 18.7% |
| `kernels/attention/gqa_fwd.py` | 21.3% |

<details>
<summary>Untested pure Python, worst 15 files</summary>

| File | Uncovered | Executed |
| --- | --- | --- |
| `perf/formulas.py` | 708 | 13.1% |
| `ops/attention/gqa.py` | 399 | 43.1% |
| `ops/pool.py` | 135 | 76.4% |
| `ops/convolution.py` | 112 | 75.4% |
| `ops/linear_attention/gated_deltanet.py` | 107 | 73.6% |
| `ops/reduction/reduce.py` | 100 | 58.0% |
| `ops/op_base.py` | 93 | 61.9% |
| `ops/elementwise/_base.py` | 88 | 76.7% |
| `ops/mamba/mamba2_fwd.py` | 85 | 19.0% |
| `ops/rope.py` | 84 | 70.6% |
| `ops/_roofline_codegen.py` | 82 | 68.8% |
| `trace/ui.py` | 62 | 24.4% |
| `ops/linear_attention/deltanet.py` | 60 | 64.1% |
| `ops/moe/shared_fused_moe.py` | 42 | 25.0% |
| `backend/registry.py` | 40 | 52.9% |

</details>

Per-line detail is in the `htmlcov/` directory of this run's `tileops_op_test` artifact.
