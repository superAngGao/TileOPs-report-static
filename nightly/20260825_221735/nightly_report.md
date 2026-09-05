# ✅ TileOPs Nightly Report

> **2026-08-25 19:28** &ensp;|&ensp; `31bc3ab` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Correctness** | ✅ &ensp; (514/514 tests across 92 ops) |
| **Benchmarked Ops** | 191 |
| **Benchmark Failures** | ✅ None &ensp;|&ensp; ⚠️ 13 skipped |
| **Regressions** (vs 14-day best) | ✅ None |
| **Baseline Alerts** (< 80%) | ⚠️ 229 |
| **Improvements** (vs 14-day best) | 🎉 2 |
| **Never-built kernels** | ⚠️ 9 files &ensp;·&ensp; `kernels/attention/deepseek_mla_decode.py` at 5.8% |
| **Untested roofline math** | 735 lines in `perf/` &ensp;·&ensp; `perf/formulas.py` at 13.1% |
| **Untested op logic** | 2542 lines in `ops/` **+378** &ensp;·&ensp; 39.4% of branches taken **−4.1pp** |
| | <sub>coverage compared against the 2026-08-24 run; no figure means it held</sub> |

## 🎉 Performance Improvements (vs 14-day best)

| Op | Config | Prev Best (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|---------------:|-----------:|------:|-------:|
| **FFTC2CFwdOp** | test_fft_bench[fft-4k-c128-b64-complex128] | 0.0304 | 0.0204 | -33.0% | 0.77 |
| **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-2p7b-b2-s32k-dt-bias-float16] | 0.0598 | 0.0444 | -25.6% | 0.94 |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 80%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-gate-up-block128-float8_e4m3fn] | 0.1483 | 0.0129 | 8.7% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **SharedFusedMoE** | test_shared_fused_moe_bench[1-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 2.5240 | 0.4264 | 16.9% | vllm |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[gemv-down-m1-block128-float8_e4m3fn] | 0.0446 | 0.0078 | 17.4% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[k-dominant-7168x16384-block128-float8_e4m3fn] | 3.5851 | 0.7733 | 21.6% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[large-spatial-float16] | 4.3416 | 1.0180 | 23.4% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-down-block128-float8_e4m3fn] | 0.0379 | 0.0092 | 24.4% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GemmFwdOp** | test_gemm_bench[mid-m96-gate-up-bfloat16] | 0.0688 | 0.0169 | 24.5% | torch-cublas |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-decode-gate-up-bfloat16] | 0.0677 | 0.0173 | 25.5% | torch-cublas |
| 🔴 | **MaxPool1dFwdOp** | test_max_pool1d_bench[textcnn-global-float16] | 0.0134 | 0.0037 | 27.6% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-attn-proj-block128-float8_e4m3fn] | 0.7705 | 0.2147 | 27.9% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[lm-head-logits-float32] | 0.0348 | 0.0099 | 28.3% | torch-compile |
| 🔴 | **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[textcnn-global-float16] | 0.0193 | 0.0057 | 29.5% | torch-compile |
| 🔴 | **Conv3dFwdOp** | test_conv3d_bench[3d-unet-aspp-3x3x3-rate6-float16] | 0.1268 | 0.0376 | 29.6% | torch |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[lm-head-logits-bfloat16] | 0.0308 | 0.0091 | 29.7% | torch-compile |
| 🔴 | **LogSoftmaxFwdOp** | test_log_softmax_bench[lm-head-logits-float32] | 0.0320 | 0.0099 | 30.9% | torch-compile |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-stage2-float16] | 0.0107 | 0.0033 | 30.9% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[small-batch-down-m8-per-tensor-float8_e4m3fn] | 0.0268 | 0.0083 | 31.0% | deepgemm |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b4-dmem1024-d512-float16] | 0.0825 | 0.0256 | 31.0% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-bfloat16] | 0.4566 | 0.1432 | 31.4% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-bfloat16] | 0.4557 | 0.1435 | 31.5% | fa3 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-down-block128-float8_e4m3fn] | 0.4464 | 0.1433 | 32.1% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[lm-head-logits-float16] | 0.0284 | 0.0091 | 32.2% | torch-compile |
| 🔴 | **Conv3dFwdOp** | test_conv3d_bench[unet-encoder-k3-s1-bfloat16] | 0.3538 | 0.1153 | 32.6% | torch-compile |
| 🔴 | **AnyFwdOp** | test_any_bench[3d-multidim-reduce-bool] | 0.0111 | 0.0037 | 33.8% | torch-compile |
| 🔴 | **Conv3dFwdOp** | test_conv3d_bench[unet-encoder-k3-s1-bias-bfloat16] | 0.3538 | 0.1221 | 34.5% | torch-compile |
| 🔴 | **MeanPoolingForwardOp** | test_mean_pooling_bench[dense-mainstream] | 0.1351 | 0.0470 | 34.8% | torch-view-mean |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-gate-up-block128-float8_e4m3fn] | 0.3852 | 0.1393 | 36.2% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **MaximumFwdOp** | test_maximum_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0393 | 0.0142 | 36.2% | torch-compile |
| 🔴 | **MinimumFwdOp** | test_minimum_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0394 | 0.0144 | 36.6% | torch-compile |
| 🔴 | **AllFwdOp** | test_all_bench[3d-multidim-reduce-bool] | 0.0111 | 0.0041 | 36.8% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[mid-m32-attn-bfloat16] | 0.0662 | 0.0244 | 36.8% | torch-cublas |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-fc-float16] | 0.0061 | 0.0022 | 36.8% | torch-compile |
| 🔴 | **LogSoftmaxFwdOp** | test_log_softmax_bench[lm-head-logits-bfloat16] | 0.0261 | 0.0097 | 37.0% | torch-compile |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-b64-complex64] | 0.0152 | 0.0056 | 37.0% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[mid-m16-attn-bfloat16] | 0.0658 | 0.0245 | 37.2% | torch-cublas |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[wide-n-24576-block128-float8_e4m3fn] | 1.0285 | 0.3829 | 37.2% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-stage3-float16] | 0.0129 | 0.0048 | 37.6% | torch-compile |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-stage1-float16] | 0.0109 | 0.0041 | 37.7% | torch-compile |
| 🔴 | **MaximumFwdOp** | test_maximum_manifest_bench[cnn-feat-broadcast-float16] | 0.0374 | 0.0144 | 38.4% | torch-compile |
| 🔴 | **MinimumFwdOp** | test_minimum_manifest_bench[cnn-feat-broadcast-float16] | 0.0374 | 0.0144 | 38.4% | torch-compile |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[mha-decode-b32-pv-per-tensor-float8_e4m3fn] | 0.0647 | 0.0250 | 38.6% | flashinfer-bmm-fp8 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-short-bfloat16] | 0.4093 | 0.1587 | 38.8% | fa3 |
| 🔴 | **LogSoftmaxFwdOp** | test_log_softmax_bench[lm-head-logits-float16] | 0.0249 | 0.0097 | 38.9% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[gemv-down-m1-per-tensor-float8_e4m3fn] | 0.0259 | 0.0101 | 39.2% | deepgemm |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-short-bfloat16] | 0.4153 | 0.1652 | 39.8% | fa3 |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b1-dmem512-d256-float16] | 0.0330 | 0.0131 | 39.8% | torch-compile |
| 🔴 | **L1NormFwdOp** | test_l1_norm_bench[3d-multidim-reduce-float16] | 0.0113 | 0.0046 | 40.5% | torch-compile |
| 🔴 | **MeanPoolingForwardOp** | test_mean_pooling_bench[dense-batched] | 0.0702 | 0.0285 | 40.6% | torch-view-mean |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-4096-4096-float16-SiluAndMulFwdKernel-direct] | 0.0662 | 0.0269 | 40.7% | torch-compile |
| 🔴 | **L2NormFwdOp** | test_l2_norm_bench[3d-multidim-reduce-float16] | 0.0113 | 0.0046 | 40.8% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-down-per-tensor-float8_e4m3fn] | 0.0253 | 0.0104 | 41.1% | deepgemm |
| 🔴 | **CountNonzeroFwdOp** | test_count_nonzero_bench[3d-multidim-reduce-float16] | 0.0116 | 0.0048 | 41.3% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-bfloat16] | 1.3109 | 0.5488 | 41.9% | fa3 |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c128-b64-complex128] | 0.0204 | 0.0085 | 42.0% | torch-cufft |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-1024-11008-float16-SiluAndMulFwdKernel-direct] | 0.0450 | 0.0190 | 42.4% | torch-compile |
| 🔴 | **MaxPool3dIndicesFwdOp** | test_max_pool3d_indices_bench[c3d-pool1-float16] | 0.3044 | 0.1290 | 42.4% | torch-compile |
| 🔴 | **RopeNeoxPositionIdsFwdOp** | test_rope_neox_position_ids_bench[position-ids-s2k-h32-d128-float16] | 0.0278 | 0.0119 | 42.8% | torch-compile |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[mha-decode-b64-qk-per-tensor-float8_e4m3fn] | 0.1156 | 0.0495 | 42.9% | flashinfer-bmm-fp8 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-prefill-varlen-mixed-fp16] | 0.1404 | 0.0620 | 44.1% | fa3 |
| 🔴 | **InfNormFwdOp** | test_inf_norm_bench[3d-multidim-reduce-float16] | 0.0112 | 0.0050 | 44.2% | torch-compile |
| 🔴 | **SharedFusedMoE** | test_shared_fused_moe_bench[4096-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 32.5542 | 14.5619 | 44.7% | vllm |
| 🔴 | **grouped_gemm_tn** | test_grouped_gemm_bench[tn-batch16-m4096-n4096-k4096-float16] | 0.7828 | 0.3544 | 45.3% | torch |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float16-SiluAndMulFwdKernel-direct] | 0.0178 | 0.0083 | 46.7% | torch-compile |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-405b-p256-float16] | 0.0563 | 0.0265 | 47.1% | fa3 |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-bfloat16-SiluAndMulFwdKernel-direct] | 0.0178 | 0.0084 | 47.3% | torch-compile |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-bfloat16] | 1.2411 | 0.5887 | 47.4% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p256-float16] | 0.1686 | 0.0814 | 48.3% | fa3 |
| 🔴 | **RopeNeoxPositionIdsFwdOp** | test_rope_neox_position_ids_bench[position-ids-s4k-h32-d128-bfloat16] | 0.0455 | 0.0223 | 49.0% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[wide-n-24576-bfloat16] | 0.8992 | 0.4440 | 49.4% | deepgemm |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-small-bfloat16] | 0.0394 | 0.0196 | 49.6% | torch-compile |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-long-k-pressure-float16] | 0.2835 | 0.1410 | 49.8% | marlin-fp16 |
| 🔴 | **GemmFwdOp** | test_gemm_bench[square-1k-nn-bfloat16] | 0.0145 | 0.0072 | 49.8% | torch-cublas |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-bfloat16] | 1.1017 | 0.5494 | 49.9% | fa3 |
| 🔴 | **VarFwdOp** | test_var_bench[3d-multidim-reduce-float16] | 0.0120 | 0.0060 | 50.0% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-down-per-tensor-float8_e4m3fn] | 0.2103 | 0.1052 | 50.0% | deepgemm |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-2p7b-b2-s32k-dt-bias-float16] | 0.0444 | 0.0223 | 50.2% | mamba |
| 🔴 | **GemmFwdOp** | test_gemm_bench[square-1k-nn-float16] | 0.0145 | 0.0073 | 50.2% | torch-cublas |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-70b-prefill-varlen-q-lt-kv-bf16] | 0.1960 | 0.0993 | 50.6% | fa3 |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-dt-bias-bfloat16] | 0.0124 | 0.0064 | 52.1% | mamba |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-gate-up-bfloat16] | 0.3374 | 0.1771 | 52.5% | torch-cublas |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[compile-smoke-rect-128x256x256-float16] | 0.0058 | 0.0031 | 52.8% | torch-dequantized-matmul |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-bfloat16] | 0.0121 | 0.0064 | 53.0% | mamba |
| 🔴 | **StdFwdOp** | test_std_bench[3d-multidim-reduce-float16] | 0.0121 | 0.0064 | 53.3% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-decode-down-bfloat16] | 0.0247 | 0.0132 | 53.4% | torch-cublas |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-70b-p256-float16] | 0.0684 | 0.0368 | 53.7% | fa3 |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-float16] | 0.0196 | 0.0107 | 54.2% | torch-compile |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-bfloat16] | 0.0195 | 0.0106 | 54.6% | torch-compile |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-non-power2-low-cta-float16] | 0.0743 | 0.0407 | 54.9% | marlin-fp32 |
| 🔴 | **gelu_tanh_and_mul_strategy** | test_fused_gated_strategy_bench[gelu_tanh_and_mul-1024-4096-float16-GeluTanhAndMulFwdKernel-direct] | 0.0178 | 0.0098 | 54.9% | torch-compile |
| 🔴 | **MaxPool3dIndicesFwdOp** | test_max_pool3d_indices_bench[c3d-pool2-float16] | 0.0589 | 0.0327 | 55.5% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-down-bfloat16] | 0.3214 | 0.1797 | 55.9% | deepgemm |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 1.0178 | 0.5780 | 56.8% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-prefill-varlen-uniform-fp16] | 0.1249 | 0.0712 | 57.0% | fa3 |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-medium-bfloat16] | 0.0544 | 0.0316 | 58.0% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-float16] | 0.2444 | 0.1432 | 58.6% | fa3 |
| 🔴 | **gelu_and_mul_strategy** | test_fused_gated_strategy_bench[gelu_and_mul-1024-4096-float16-GeluAndMulFwdKernel-direct] | 0.0182 | 0.0107 | 58.6% | torch-compile |
| 🔴 | **RopeYarnFwdOp** | test_rope_yarn_bench[yarn-2d-b1-s8k-h32-d128-float16] | 0.0594 | 0.0349 | 58.7% | torch-compile |
| 🔴 | **RopeLongRopeFwdOp** | test_rope_longrope_bench[longrope-2d-b1-s8k-h32-d128-float16] | 0.0594 | 0.0348 | 58.7% | torch-compile |
| 🔴 | **RopeLlama31FwdOp** | test_rope_llama31_bench[llama31-2d-b1-s8k-h32-d128-float16] | 0.0594 | 0.0349 | 58.7% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-float16] | 0.2434 | 0.1437 | 59.1% | fa3 |
| 🔴 | **SharedFusedMoE** | test_shared_fused_moe_bench[2048-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 19.5397 | 11.5823 | 59.3% | vllm |
| 🔴 | **RopeNeoxFwdOp** | test_rope_neox_bench[neox-2d-b2-s2k-h32-d128-float16] | 0.0310 | 0.0184 | 59.4% | torch-compile |
| 🔴 | **TopkSelectorFwdOp** | test_topk_selector_bench[topk1024-s32k-kv64k-float32] | 15.6143 | 9.2788 | 59.4% | flashinfer |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[throughput-8b-p64-float16] | 0.2516 | 0.1507 | 59.9% | flashinfer |
| 🔴 | **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[ecg-cnn-dilated-bfloat16] | 0.0223 | 0.0134 | 60.0% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-attn-proj-bfloat16] | 0.5405 | 0.3298 | 61.0% | deepgemm |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-float16] | 0.9015 | 0.5520 | 61.2% | fa3 |
| 🔴 | **GemmFwdOp** | test_gemm_bench[k-dominant-7168x16384-bfloat16] | 2.0639 | 1.2646 | 61.3% | torch-cublas |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-float16] | 0.6360 | 0.3908 | 61.5% | fla |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-float16] | 0.1124 | 0.0691 | 61.5% | torch-compile |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-bfloat16] | 0.6389 | 0.3935 | 61.6% | fla |
| 🔴 | **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[global-1x1-float16] | 0.0133 | 0.0082 | 61.7% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-float16] | 0.8914 | 0.5532 | 62.1% | fa3 |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-attn-proj-float16] | 0.5417 | 0.3363 | 62.1% | torch-cublas |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-hbm-streaming-threshold-float16] | 0.0610 | 0.0379 | 62.1% | marlin-fp32 |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-bfloat16] | 0.1123 | 0.0699 | 62.3% | torch-compile |
| 🔴 | **VarMeanFwdOp** | test_var_mean_bench[3d-multidim-reduce-float16] | 0.0121 | 0.0076 | 62.3% | torch-compile |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s896-float16] | 0.0454 | 0.0285 | 62.7% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s896-bfloat16] | 0.0453 | 0.0285 | 62.9% | fa3 |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[compile-smoke-square-64x64x128-float16] | 0.0043 | 0.0027 | 63.2% | torch-dequantized-matmul |
| 🔴 | **GemmFwdOp** | test_gemm_bench[mid-m64-down-bfloat16] | 0.0207 | 0.0132 | 63.8% | torch-cublas |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b8-dmem512-d256-bfloat16] | 0.0335 | 0.0214 | 64.1% | torch-compile |
| 🔴 | **LogSumExpFwdOp** | test_logsumexp_bench[lm-head-logits-bfloat16] | 0.0164 | 0.0105 | 64.1% | torch-compile |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-float16] | 1.4222 | 0.9198 | 64.7% | fla |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-float32] | 0.0195 | 0.0127 | 64.9% | torch-compile |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-bfloat16] | 0.3167 | 0.2056 | 64.9% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-bfloat16] | 1.4642 | 0.9532 | 65.1% | fla |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-float16] | 0.3142 | 0.2050 | 65.2% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-float16] | 0.3808 | 0.2496 | 65.5% | fla |
| 🔴 | **TopkSelectorFwdOp** | test_topk_selector_bench[topk2048-s32k-kv64k-float32] | 16.2322 | 10.6700 | 65.7% | flashinfer |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-unbatched-complex64] | 0.0081 | 0.0054 | 66.1% | torch-cufft |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-float16] | 0.2016 | 0.1337 | 66.3% | fla |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-l2-resident-ish-float16] | 0.0329 | 0.0219 | 66.4% | marlin-fp16 |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s1792-bfloat16] | 0.1289 | 0.0858 | 66.6% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s1792-float16] | 0.1288 | 0.0859 | 66.7% | fa3 |
| 🔴 | **GroupNormFwdOp** | test_group_norm_bench[wider-channel-g32-affine-float16] | 0.0060 | 0.0040 | 66.7% | flaggems |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-bfloat16] | 0.3876 | 0.2584 | 66.7% | fla |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-float32] | 0.1073 | 0.0716 | 66.7% | torch-compile |
| 🔴 | **GroupNormFwdOp** | test_group_norm_no_affine_bench[tail-spatial-g16-float16] | 0.0052 | 0.0035 | 66.9% | torch-compile |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-bfloat16] | 0.7503 | 0.5020 | 66.9% | fla |
| 🔴 | **GroupNormFwdOp** | test_group_norm_bench[tail-spatial-g16-affine-float16] | 0.0060 | 0.0041 | 67.2% | flaggems |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-float16] | 0.7235 | 0.4869 | 67.3% | fla |
| 🔴 | **AvgPool1dFwdOp** | test_avg_pool1d_bench[audio-downsample-float16] | 0.0062 | 0.0042 | 67.6% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-bfloat16] | 0.0971 | 0.0659 | 67.9% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-bfloat16] | 0.2049 | 0.1400 | 68.3% | fla |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[moe-prefill-b128-per-tensor-float8_e4m3fn] | 0.9008 | 0.6248 | 69.4% | flashinfer-bmm-fp8 |
| 🔴 | **FusedAddRMSNormFwdOp** | test_fused_add_rms_norm_bench[llama-405b-decode-bfloat16] | 0.0062 | 0.0043 | 70.2% | flashinfer |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-bfloat16] | 0.3117 | 0.2198 | 70.5% | fla |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s3584-float16] | 0.7504 | 0.5296 | 70.6% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s3584-bfloat16] | 0.7495 | 0.5296 | 70.7% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-softcap50-float16] | 0.1766 | 0.1253 | 71.0% | flashinfer |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s7168-bfloat16] | 2.8474 | 2.0251 | 71.1% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-float16] | 0.8329 | 0.5925 | 71.1% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s7168-float16] | 2.8432 | 2.0248 | 71.2% | fa3 |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-float16] | 0.0986 | 0.0703 | 71.2% | fla |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s16k-h4-d64-float16] | 1.5153 | 1.0816 | 71.4% | fla |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.8094 | 0.5803 | 71.7% | fa3 |
| 🔴 | **MaxPool2dFwdOp** | test_max_pool2d_bench[resnet-stem-float16] | 0.0472 | 0.0340 | 72.1% | torch-compile |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-float16] | 0.0571 | 0.0412 | 72.3% | flashinfer |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-float16] | 0.1487 | 0.1077 | 72.4% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0569 | 0.0412 | 72.4% | flashinfer |
| 🔴 | **MaxPool2dFwdOp** | test_max_pool2d_bench[resnet-stem-bfloat16] | 0.0470 | 0.0341 | 72.6% | torch-compile |
| 🔴 | **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[nondiv-7x7-bfloat16] | 0.0158 | 0.0115 | 72.6% | torch-ref |
| 🔴 | **GroupNormFwdOp** | test_group_norm_no_affine_bench[wider-channel-g32-float16] | 0.0048 | 0.0035 | 72.7% | flaggems |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-2k-bfloat16] | 0.2804 | 0.2050 | 73.1% | torch-cublas |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[alexnet-ceil-bfloat16] | 0.0237 | 0.0174 | 73.4% | torch-compile |
| 🔴 | **LogicalOrFwdOp** | test_logical_or_manifest_bench[cnn-feat-broadcast-float16] | 0.0164 | 0.0120 | 73.5% | torch-compile |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-2k-float16] | 0.2836 | 0.2084 | 73.5% | torch-cublas |
| 🔴 | **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[sincnet-speaker-local-float16] | 0.0218 | 0.0160 | 73.5% | torch-compile |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b4-4k-bfloat16] | 1.0413 | 0.7661 | 73.6% | torch-cublas |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-float16] | 0.0935 | 0.0690 | 73.8% | flashinfer |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-bfloat16] | 0.6115 | 0.4524 | 74.0% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-bfloat16] | 0.0930 | 0.0689 | 74.1% | flashinfer |
| 🔴 | **LogicalOrFwdOp** | test_logical_or_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0164 | 0.0121 | 74.2% | torch-compile |
| 🔴 | **LtFwdOp** | test_lt_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0118 | 74.4% | torch-compile |
| 🔴 | **GeFwdOp** | test_ge_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0118 | 74.4% | torch-compile |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[alexnet-ceil-float16] | 0.0237 | 0.0177 | 74.5% | torch-compile |
| 🔴 | **LeFwdOp** | test_le_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0119 | 74.5% | torch-compile |
| 🔴 | **LeFwdOp** | test_le_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0119 | 74.5% | torch-compile |
| 🔴 | **BmmFwdOp** | test_bmm_bench[moe-prefill-b128-bfloat16] | 0.2896 | 0.2161 | 74.6% | torch-cublas |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s16k-h4-d64-bfloat16] | 1.4486 | 1.0812 | 74.6% | fla |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s8k-h4-d64-float16] | 0.7452 | 0.5569 | 74.7% | fla |
| 🔴 | **GtFwdOp** | test_gt_manifest_bench[cnn-feat-broadcast-float16] | 0.0160 | 0.0119 | 74.8% | torch-compile |
| 🔴 | **NeFwdOp** | test_ne_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0119 | 74.8% | torch-compile |
| 🔴 | **EqFwdOp** | test_eq_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0119 | 74.9% | torch-compile |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-bfloat16] | 0.1444 | 0.1083 | 75.0% | fla |
| 🔴 | **NeFwdOp** | test_ne_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0119 | 75.0% | torch-compile |
| 🔴 | **EqFwdOp** | test_eq_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0119 | 75.0% | torch-compile |
| 🔴 | **LogicalAndFwdOp** | test_logical_and_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0120 | 75.2% | torch-compile |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-float16] | 0.1668 | 0.1256 | 75.3% | flashinfer |
| 🔴 | **Conv2dFwdOp** | test_conv2d_bench[highres-3x3-s1-bias-float16] | 0.1049 | 0.0790 | 75.3% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-float16] | 0.6178 | 0.4655 | 75.3% | fla |
| 🔴 | **GtFwdOp** | test_gt_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0120 | 75.5% | torch-compile |
| 🔴 | **Conv3dFwdOp** | test_conv3d_bench[video-stage-downsample-k3-s2-float16] | 0.0349 | 0.0264 | 75.6% | torch |
| 🔴 | **RopeNonNeoxFwdOp** | test_rope_non_neox_bench[non-neox-2d-b2-s2k-h32-d128-bfloat16] | 0.0252 | 0.0190 | 75.6% | torch-compile |
| 🔴 | **Conv2dFwdOp** | test_conv2d_bench[highres-3x3-s1-float16] | 0.1044 | 0.0790 | 75.6% | torch-compile |
| 🔴 | **GeFwdOp** | test_ge_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0120 | 75.6% | torch-compile |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-1k-bfloat16] | 0.0408 | 0.0310 | 76.0% | torch-cublas |
| 🔴 | **LogicalAndFwdOp** | test_logical_and_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0122 | 76.3% | torch-compile |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float32-SiluAndMulFwdKernel-direct] | 0.0200 | 0.0153 | 76.4% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s4k-h4-d64-bfloat16] | 0.1564 | 0.1196 | 76.5% | fla |
| 🔴 | **LtFwdOp** | test_lt_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0122 | 76.7% | torch-compile |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s8k-h4-d64-bfloat16] | 0.7265 | 0.5569 | 76.7% | fla |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-1k-float16] | 0.0405 | 0.0311 | 76.7% | torch-cublas |
| 🔴 | **LogSumExpFwdOp** | test_logsumexp_bench[lm-head-logits-float16] | 0.0141 | 0.0108 | 76.9% | torch-compile |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.3495 | 0.2696 | 77.1% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-float16] | 0.3518 | 0.2720 | 77.3% | fa3 |
| 🔴 | **DeltaNetFwdOp** | test_deltanet_vs_fla_fwd[dn-b2-s16k-h4-d64-float16] | 0.4729 | 0.3660 | 77.4% | fla |
| 🔴 | **Conv2dFwdOp** | test_conv2d_bench[classifier-1x1-bias-float16] | 0.0095 | 0.0074 | 77.5% | torch-compile |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-float16] | 0.0866 | 0.0672 | 77.6% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.6662 | 0.5174 | 77.7% | flashinfer |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-bfloat16] | 0.0866 | 0.0675 | 77.9% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-float16] | 0.6682 | 0.5211 | 78.0% | flashinfer |
| 🔴 | **GatedDeltaNetPrefillBHTDFwdOp** | test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-float16] | 0.2509 | 0.1957 | 78.0% | fla |
| 🔴 | **DeltaNetFwdOp** | test_deltanet_vs_fla_fwd[dn-b2-s16k-h4-d64-bfloat16] | 0.4737 | 0.3697 | 78.0% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowFwdOp** | test_gqa_sliding_window_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.1516 | 0.1184 | 78.1% | fa3 |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s4k-h4-d64-float16] | 0.3687 | 0.2880 | 78.1% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowFwdOp** | test_gqa_sliding_window_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.1512 | 0.1182 | 78.2% | fa3 |
| 🔴 | **GatedDeltaNetPrefillBHTDFwdOp** | test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-bfloat16] | 0.2525 | 0.1978 | 78.3% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowFwdOp** | test_gqa_sliding_window_fwd_bench[llama-70b-long-w1024-float16] | 0.1528 | 0.1201 | 78.6% | fa3 |
| 🔴 | **LogSumExpFwdOp** | test_logsumexp_bench[3d-multidim-reduce-float16] | 0.0126 | 0.0099 | 78.6% | torch-compile |
| 🔴 | **grouped_gemm_nn** | test_grouped_gemm_bench[nn-batch16-m4096-n4096-k4096-float16] | 0.3408 | 0.2689 | 78.9% | torch |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0043 | 0.0034 | 79.0% | mamba |
| 🔴 | **Conv2dFwdOp** | test_conv2d_bench[classifier-1x1-float16] | 0.0092 | 0.0072 | 79.0% | torch-compile |
| 🔴 | **GroupedQueryAttentionSlidingWindowFwdOp** | test_gqa_sliding_window_fwd_bench[llama-8b-long-w1024-float16] | 0.1529 | 0.1209 | 79.1% | fa3 |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s4k-h4-d64-bfloat16] | 0.3643 | 0.2884 | 79.1% | fla |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-float16] | 0.3128 | 0.2477 | 79.2% | fla |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-large-bfloat16] | 0.0716 | 0.0568 | 79.4% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s4k-h4-d64-float16] | 0.1571 | 0.1254 | 79.8% | fla |

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

| | Op | Config | Device busy (ms) | TFLOPS | BW (TB/s) | Via | Ratio |
|:-|:---|:-------|------------:|-------:|----------:|:----|------:|
| 🔵 | AbsFwdOp | test_abs_bench[elementwise-16M-float16] | 0.0179 | 0.94 | 3.76 | torch 100.4%, torch-compile 100.4% | - |
| 🔵 | AbsFwdOp | test_abs_bench[elementwise-16M-bfloat16] | 0.0179 | 0.94 | 3.76 | torch 100.5%, torch-compile 100.4% | - |
| 🟡 | AbsFwdOp | test_abs_bench[elementwise-16M-float32] | 0.0340 | 0.49 | 3.95 | torch 100.0%, torch-compile 99.8% | - |
| 🔵 | AbsFwdOp | test_abs_bench[elementwise-256M-float16] | 0.2496 | 1.08 | 4.30 | torch 100.1%, torch-compile 100.3% | - |
| 🟡 | AbsFwdOp | test_abs_bench[elementwise-256M-bfloat16] | 0.2498 | 1.07 | 4.30 | torch 100.0%, torch-compile 100.1% | - |
| 🔵 | AdaLayerNormFwdOp | test_ada_layer_norm_bench[dit-xl-2-float16] | 0.0052 | 1.13 | 1.80 | torch-ref 230.6%, torch-compile 145.6% | - |
| 🔵 | AdaLayerNormFwdOp | test_ada_layer_norm_bench[dit-xl-2-bfloat16] | 0.0053 | 1.10 | 1.77 | torch-ref 226.9%, torch-compile 146.1% | - |
| 🔵 | AdaLayerNormFwdOp | test_ada_layer_norm_bench[llama-8b-prefill-float16] | 0.0198 | 2.12 | 3.39 | torch-ref 208.7%, torch-compile 128.8% | - |
| 🔵 | AdaLayerNormFwdOp | test_ada_layer_norm_bench[llama-8b-prefill-bfloat16] | 0.0199 | 2.11 | 3.38 | torch-ref 210.0%, torch-compile 133.0% | - |
| 🔵 | AdaLayerNormFwdOp | test_ada_layer_norm_bench[llama-8b-decode-bfloat16] | 0.0027 | 0.01 | 0.01 | torch-ref 390.4%, torch-compile 115.7% | - |
| 🔵 | AdaLayerNormZeroFwdOp | test_ada_layer_norm_zero_bench[dit-xl-2-float16] | 0.0062 | 1.15 | 1.91 | torch-ref 238.9%, torch-compile 125.4% | - |
| 🔵 | AdaLayerNormZeroFwdOp | test_ada_layer_norm_zero_bench[dit-xl-2-bfloat16] | 0.0062 | 1.14 | 1.90 | torch-ref 238.1%, torch-compile 130.9% | - |
| 🔵 | AdaLayerNormZeroFwdOp | test_ada_layer_norm_zero_bench[llama-8b-prefill-float16] | 0.0247 | 2.03 | 3.39 | torch-ref 214.9%, torch-compile 110.5% | - |
| 🔵 | AdaLayerNormZeroFwdOp | test_ada_layer_norm_zero_bench[llama-8b-prefill-bfloat16] | 0.0246 | 2.04 | 3.40 | torch-ref 217.4%, torch-compile 114.1% | - |
| 🔵 | AdaLayerNormZeroFwdOp | test_ada_layer_norm_zero_bench[llama-8b-decode-bfloat16] | 0.0028 | 0.01 | 0.01 | torch-ref 409.0%, torch-compile 113.5% | - |
| 🔵 | AdaptiveAvgPool2dFwdOp | test_adaptive_avg_pool2d_bench[resnet-global-float16] | 0.0030 | 0.27 | 0.55 | torch-ref 246.2%, torch-compile 124.7% | - |
| 🟢 | AdaptiveAvgPool2dFwdOp | test_adaptive_avg_pool2d_bench[spp-6x6-float16] | 0.0054 | 0.17 | 0.30 | torch-ref 197.6%, torch-compile 197.0% | - |
| 🔵 | AdaptiveAvgPool2dFwdOp | test_adaptive_avg_pool2d_bench[nondiv-7x7-bfloat16] | 0.0066 | 0.07 | 0.12 | torch-ref 138.8%, torch-compile 138.8% | - |
| 🔵 | AdaptiveMaxPool2dFwdOp | test_adaptive_max_pool2d_bench[global-1x1-float16] | 0.0029 | 0.28 | 0.56 | torch-ref 1543.4%, torch-compile 130.7% | - |
| 🟢 | AdaptiveMaxPool2dFwdOp | test_adaptive_max_pool2d_bench[spp-6x6-float16] | 0.0060 | 0.15 | 0.27 | torch-ref 236.7%, torch-compile 237.2% | - |
| 🟢 | AdaptiveMaxPool2dFwdOp | test_adaptive_max_pool2d_bench[nondiv-7x7-bfloat16] | 0.0065 | 0.08 | 0.13 | torch-ref 177.3%, torch-compile 176.3% | - |
| 🔴 | AdaptiveMaxPool2dIndicesFwdOp | test_adaptive_max_pool2d_indices_bench[global-1x1-float16] | 0.0133 | 0.06 | 0.13 | torch-ref 338.3%, torch-compile 61.7% | - |
| 🟡 | AdaptiveMaxPool2dIndicesFwdOp | test_adaptive_max_pool2d_indices_bench[spp-6x6-float16] | 0.0154 | 0.06 | 0.11 | torch-ref 93.1%, torch-compile 92.9% | - |
| 🔴 | AdaptiveMaxPool2dIndicesFwdOp | test_adaptive_max_pool2d_indices_bench[nondiv-7x7-bfloat16] | 0.0158 | 0.03 | 0.05 | torch-ref 72.6%, torch-compile 72.6% | - |
| 🔵 | AddFwdOp | test_add_manifest_bench[hidden-state-prefill-float16] | 0.0147 | 1.14 | 3.43 | torch 101.2%, torch-compile 100.2% | - |
| 🟡 | AddFwdOp | test_add_manifest_bench[hidden-state-prefill-bfloat16] | 0.0147 | 1.14 | 3.42 | torch 101.3%, torch-compile 99.8% | - |
| 🟡 | AddFwdOp | test_add_manifest_bench[hidden-state-prefill-float32] | 0.0265 | 0.63 | 3.80 | torch 100.0%, torch-compile 99.9% | - |
| 🔵 | AddFwdOp | test_add_manifest_bench[cnn-feat-broadcast-float16] | 0.0144 | 1.78 | 3.56 | torch 318.2%, torch-compile 100.0% | - |
| 🔵 | AddFwdOp | test_add_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0144 | 1.79 | 3.58 | torch 322.9%, torch-compile 100.0% | - |
| 🔵 | AddFwdOp | test_add_manifest_bench[cnn-feat-broadcast-float32] | 0.0266 | 0.97 | 3.87 | torch 185.7%, torch-compile 100.0% | - |
| 🔵 | AlibiFwdOp | test_alibi_bench[llama-prefill-2k-float16] | 0.0647 | 6.23 | 4.15 | torch-ref 916.0%, torch-compile 134.0% | - |
| 🔵 | AlibiFwdOp | test_alibi_bench[llama-prefill-2k-bfloat16] | 0.0649 | 6.20 | 4.14 | torch-ref 912.9%, torch-compile 132.7% | - |
| 🔵 | AlibiFwdOp | test_alibi_bench[llama-prefill-4k-float16] | 0.2856 | 5.64 | 3.76 | torch-ref 913.6%, torch-compile 119.6% | - |
| 🔵 | AlibiFwdOp | test_alibi_bench[llama-prefill-4k-bfloat16] | 0.2859 | 5.63 | 3.76 | torch-ref 912.7%, torch-compile 119.3% | - |
| 🟡 | AllFwdOp | test_all_bench[mask-validation-4k-bool] | 0.0020 | 0.07 | 0.07 | flaggems 96.7%, torch 886.9%, torch-compile 93.4% | - |
| 🟡 | AllFwdOp | test_all_bench[mask-validation-32k-bool] | 0.0038 | 0.28 | 0.28 | flaggems 170.3%, torch 269.5%, torch-compile 89.8% | - |
| 🔴 | AllFwdOp | test_all_bench[3d-multidim-reduce-bool] | 0.0111 | 0.19 | 0.19 | flaggems 106.2%, torch 93.8%, torch-compile 36.8% | - |
| 🔵 | AmaxFwdOp | test_amax_bench[hidden-state-reduce-float16] | 0.0074 | 1.13 | 2.26 | flaggems 103.5%, torch 258.6%, torch-compile 136.6% | - |
| 🔵 | AmaxFwdOp | test_amax_bench[hidden-state-reduce-bfloat16] | 0.0074 | 1.13 | 2.26 | flaggems 105.2%, torch 260.3%, torch-compile 136.2% | - |
| 🔵 | AmaxFwdOp | test_amax_bench[long-seq-reduce-bfloat16] | 0.0041 | 0.51 | 1.02 | flaggems 331.9%, torch 274.9%, torch-compile 115.6% | - |
| 🟡 | AmaxFwdOp | test_amax_bench[3d-multidim-reduce-float16] | 0.0057 | 0.37 | 0.74 | flaggems 217.9%, torch 226.4%, torch-compile 88.2% | - |
| 🔵 | AminFwdOp | test_amin_bench[hidden-state-reduce-float16] | 0.0074 | 1.13 | 2.26 | torch 258.6%, torch-compile 136.2% | - |
| 🔵 | AminFwdOp | test_amin_bench[hidden-state-reduce-bfloat16] | 0.0074 | 1.13 | 2.26 | torch 260.8%, torch-compile 136.2% | - |
| 🔵 | AminFwdOp | test_amin_bench[long-seq-reduce-bfloat16] | 0.0041 | 0.51 | 1.02 | torch 273.3%, torch-compile 113.2% | - |
| 🟡 | AminFwdOp | test_amin_bench[3d-multidim-reduce-float16] | 0.0057 | 0.37 | 0.74 | torch 228.8%, torch-compile 85.9% | - |
| 🟡 | AnyFwdOp | test_any_bench[mask-validation-4k-bool] | 0.0020 | 0.07 | 0.07 | flaggems 96.7%, torch 911.5%, torch-compile 88.5% | - |
| 🟡 | AnyFwdOp | test_any_bench[mask-validation-32k-bool] | 0.0037 | 0.28 | 0.28 | flaggems 172.7%, torch 280.3%, torch-compile 88.0% | - |
| 🔴 | AnyFwdOp | test_any_bench[3d-multidim-reduce-bool] | 0.0111 | 0.19 | 0.19 | flaggems 106.1%, torch 169.6%, torch-compile 33.8% | - |
| 🟢 | ArgmaxFwdOp | test_argmax_bench[lm-head-argmax-float16] | 0.0039 | 0.11 | 0.21 | flaggems 772.9%, torch 910.6%, torch-compile 737.8% | - |
| 🟢 | ArgmaxFwdOp | test_argmax_bench[lm-head-argmax-bfloat16] | 0.0040 | 0.10 | 0.21 | flaggems 716.1%, torch 906.0%, torch-compile 730.6% | - |
| 🔵 | ArgmaxFwdOp | test_argmax_bench[hidden-state-argmax-float16] | 0.0092 | 0.92 | 1.83 | flaggems 133.2%, torch 269.2%, torch-compile 207.7% | - |
| 🔵 | ArgmaxFwdOp | test_argmax_bench[hidden-state-argmax-bfloat16] | 0.0096 | 0.87 | 1.74 | flaggems 120.8%, torch 257.5%, torch-compile 201.0% | - |
| 🟡 | ArgmaxFwdOp | test_argmax_bench[3d-non-last-axis-argmax-float16] | 0.0039 | 0.54 | 2.15 | flaggems 98.0%, torch 286.1%, torch-compile 100.0% | - |
| 🟢 | ArgminFwdOp | test_argmin_bench[lm-head-argmin-float16] | 0.0040 | 0.10 | 0.20 | flaggems 2889.6%, torch 884.0%, torch-compile 716.0% | - |
| 🟢 | ArgminFwdOp | test_argmin_bench[lm-head-argmin-bfloat16] | 0.0066 | 0.06 | 0.12 | flaggems 1552.7%, torch 542.3%, torch-compile 438.9% | - |
| 🔵 | ArgminFwdOp | test_argmin_bench[hidden-state-argmin-float16] | 0.0096 | 0.87 | 1.74 | flaggems 102.7%, torch 255.8%, torch-compile 197.3% | - |
| 🟡 | ArgminFwdOp | test_argmin_bench[hidden-state-argmin-bfloat16] | 0.0099 | 0.85 | 1.70 | flaggems 99.7%, torch 252.0%, torch-compile 196.8% | - |
| 🔴 | AvgPool1dFwdOp | test_avg_pool1d_bench[audio-downsample-float16] | 0.0062 | 0.51 | 1.02 | torch-ref 248.2%, torch-compile 67.6% | - |
| 🟡 | AvgPool1dFwdOp | test_avg_pool1d_bench[long-temporal-float16] | 0.0213 | 0.96 | 1.92 | torch-ref 279.1%, torch-compile 80.5% | - |
| 🟡 | AvgPool1dFwdOp | test_avg_pool1d_bench[ceil-bfloat16] | 0.0035 | 0.30 | 0.46 | torch-ref 154.6%, torch-compile 96.3% | - |
| 🔵 | AvgPool2dFwdOp | test_avg_pool2d_bench[vision-3x3-s2-float16] | 0.0040 | 0.91 | 1.01 | flaggems 167.0%, torch-ref 229.5%, torch-compile 103.2% | - |
| 🟢 | AvgPool2dFwdOp | test_avg_pool2d_bench[vision-5x5-s2-float16] | 0.0040 | 1.24 | 0.50 | flaggems 179.4%, torch-ref 244.4%, torch-compile 511.1% | - |
| 🟢 | AvgPool2dFwdOp | test_avg_pool2d_bench[ceil-divisor-bfloat16] | 0.0031 | 1.12 | 0.73 | flaggems 184.7%, torch-ref 244.9%, torch-compile 186.8% | - |
| 🟡 | AvgPool3dFwdOp | test_avg_pool3d_bench[video-2x2x2-float16] | 0.0037 | 0.44 | 0.98 | cudnn 160.0%, torch-ref 269.6%, torch-compile 92.2% | - |
| 🟡 | AvgPool3dFwdOp | test_avg_pool3d_bench[ceil-video-float16] | 0.0044 | 0.59 | 0.43 | cudnn 127.7%, torch-ref 259.9%, torch-compile 92.0% | - |
| 🟡 | AvgPool3dFwdOp | test_avg_pool3d_bench[divisor-bfloat16] | 0.0023 | 0.15 | 0.21 | torch-ref 222.5%, torch-compile 83.1% | - |
| 🟢 | BatchNormBwdOp | test_batch_norm_bwd_bench[resnet50-fc-float16] | 0.0071 | 0.00 | 0.00 | torch-autograd 331.2%, torch-native-batch-norm 178.7% | - |
| 🔵 | BatchNormBwdOp | test_batch_norm_bwd_bench[resnet50-stage1-float16] | 0.0148 | 0.28 | 0.21 | torch-autograd 186.2%, torch-native-batch-norm 127.8% | - |
| 🔵 | BatchNormBwdOp | test_batch_norm_bwd_bench[resnet50-stage2-float16] | 0.0141 | 0.30 | 0.22 | torch-autograd 169.6%, torch-native-batch-norm 107.9% | - |
| 🔵 | BatchNormBwdOp | test_batch_norm_bwd_bench[resnet50-stage3-float16] | 0.0171 | 0.38 | 0.28 | torch-autograd 149.6%, torch-native-batch-norm 103.7% | - |
| 🟢 | BatchNormBwdOp | test_batch_norm_bwd_bench[large-spatial-float16] | 6.8760 | 0.62 | 0.47 | torch-autograd 188.6%, torch-native-batch-norm 171.5% | - |
| 🔴 | BatchNormFwdOp | test_batch_norm_fwd_bench[resnet50-fc-float16] | 0.0061 | 0.00 | 0.00 | flaggems 91.0%, torch-cudnn 185.8%, torch-compile 36.8% | - |
| 🔴 | BatchNormFwdOp | test_batch_norm_fwd_bench[resnet50-stage1-float16] | 0.0109 | 0.48 | 0.19 | flaggems 94.2%, torch-cudnn 104.4%, torch-compile 37.7% | - |
| 🔴 | BatchNormFwdOp | test_batch_norm_fwd_bench[resnet50-stage2-float16] | 0.0107 | 0.49 | 0.20 | flaggems 84.1%, torch-cudnn 97.3%, torch-compile 30.9% | - |
| 🔴 | BatchNormFwdOp | test_batch_norm_fwd_bench[resnet50-stage3-float16] | 0.0129 | 0.62 | 0.25 | flaggems 85.3%, torch-cudnn 86.6%, torch-compile 37.6% | - |
| 🔴 | BatchNormFwdOp | test_batch_norm_fwd_bench[large-spatial-float16] | 4.3416 | 1.24 | 0.49 | flaggems 89.8%, torch-cudnn 104.4%, torch-compile 23.4% | - |
| 🟡 | BitwiseAndFwdOp | test_bitwise_bench[bitwise_and-1024x4096-BitwiseAndFwdOp-bitwise_and] | 0.0147 | 0.28 | 3.42 | torch 100.2%, torch-compile 99.8% | - |
| 🟡 | BitwiseAndFwdOp | test_bitwise_bench[bitwise_and-1024x10240-BitwiseAndFwdOp-bitwise_and] | 0.0321 | 0.33 | 3.92 | torch 99.9%, torch-compile 99.8% | - |
| 🔵 | BitwiseAndFwdOp | test_bitwise_and_manifest_bench[hidden-state-prefill-bool] | 0.0083 | 1.01 | 3.02 | torch 120.9%, torch-compile 107.1% | - |
| 🟡 | BitwiseAndFwdOp | test_bitwise_and_manifest_bench[hidden-state-prefill-int32] | 0.0263 | 0.32 | 3.83 | torch 99.9%, torch-compile 99.5% | - |
| 🔵 | BitwiseAndFwdOp | test_bitwise_and_manifest_bench[hidden-state-prefill-int64] | 0.0492 | 0.17 | 4.09 | torch 100.9%, torch-compile 100.2% | - |
| 🔵 | BitwiseAndFwdOp | test_bitwise_and_manifest_bench[cnn-feat-broadcast-bool] | 0.0081 | 1.59 | 3.17 | torch 558.5%, torch-compile 123.7% | - |
| 🔵 | BitwiseAndFwdOp | test_bitwise_and_manifest_bench[cnn-feat-broadcast-int32] | 0.0265 | 0.49 | 3.88 | torch 186.5%, torch-compile 100.3% | - |
| 🟡 | BitwiseAndFwdOp | test_bitwise_and_manifest_bench[cnn-feat-broadcast-int64] | 0.0503 | 0.26 | 4.09 | torch 116.0%, torch-compile 99.1% | - |
| 🟡 | BitwiseNotFwdOp | test_bitwise_not_bench[elementwise-16M-int32] | 0.0340 | 0.49 | 3.95 | torch 100.0%, torch-compile 99.9% | - |
| 🟡 | BitwiseNotFwdOp | test_bitwise_not_bench[elementwise-16M-int64] | 0.0652 | 0.26 | 4.12 | torch 104.3%, torch-compile 99.5% | - |
| 🔵 | BitwiseNotFwdOp | test_bitwise_not_bench[elementwise-256M-int32] | 0.4986 | 0.54 | 4.31 | torch 101.2%, torch-compile 101.2% | - |
| 🟡 | BitwiseOrFwdOp | test_bitwise_bench[bitwise_or-1024x4096-BitwiseOrFwdOp-bitwise_or] | 0.0148 | 0.28 | 3.40 | torch 98.5%, torch-compile 98.1% | - |
| 🔵 | BitwiseOrFwdOp | test_bitwise_or_manifest_bench[hidden-state-prefill-bool] | 0.0081 | 1.04 | 3.11 | torch 108.7%, torch-compile 105.5% | - |
| 🟡 | BitwiseOrFwdOp | test_bitwise_or_manifest_bench[hidden-state-prefill-int32] | 0.0266 | 0.32 | 3.79 | torch 99.6%, torch-compile 99.6% | - |
| 🔵 | BitwiseOrFwdOp | test_bitwise_or_manifest_bench[hidden-state-prefill-int64] | 0.0492 | 0.17 | 4.10 | torch 101.0%, torch-compile 100.2% | - |
| 🔵 | BitwiseOrFwdOp | test_bitwise_or_manifest_bench[cnn-feat-broadcast-bool] | 0.0081 | 1.59 | 3.17 | torch 546.6%, torch-compile 126.1% | - |
| 🟡 | BitwiseOrFwdOp | test_bitwise_or_manifest_bench[cnn-feat-broadcast-int32] | 0.0267 | 0.48 | 3.86 | torch 184.8%, torch-compile 99.5% | - |
| 🟡 | BitwiseOrFwdOp | test_bitwise_or_manifest_bench[cnn-feat-broadcast-int64] | 0.0503 | 0.26 | 4.09 | torch 116.1%, torch-compile 99.6% | - |
| 🔵 | BitwiseXorFwdOp | test_bitwise_bench[bitwise_xor-1024x4096-BitwiseXorFwdOp-bitwise_xor] | 0.0147 | 0.28 | 3.42 | torch 100.4%, torch-compile 100.2% | - |
| 🔵 | BitwiseXorFwdOp | test_bitwise_xor_manifest_bench[hidden-state-prefill-bool] | 0.0082 | 1.03 | 3.08 | torch 122.0%, torch-compile 107.8% | - |
| 🟡 | BitwiseXorFwdOp | test_bitwise_xor_manifest_bench[hidden-state-prefill-int32] | 0.0265 | 0.32 | 3.80 | torch 99.0%, torch-compile 99.0% | - |
| 🔵 | BitwiseXorFwdOp | test_bitwise_xor_manifest_bench[hidden-state-prefill-int64] | 0.0491 | 0.17 | 4.10 | torch 100.9%, torch-compile 100.0% | - |
| 🔵 | BitwiseXorFwdOp | test_bitwise_xor_manifest_bench[cnn-feat-broadcast-bool] | 0.0080 | 1.61 | 3.21 | torch 565.0%, torch-compile 125.2% | - |
| 🔵 | BitwiseXorFwdOp | test_bitwise_xor_manifest_bench[cnn-feat-broadcast-int32] | 0.0263 | 0.49 | 3.90 | torch 187.2%, torch-compile 100.1% | - |
| 🟡 | BitwiseXorFwdOp | test_bitwise_xor_manifest_bench[cnn-feat-broadcast-int64] | 0.0502 | 0.26 | 4.09 | torch 115.7%, torch-compile 99.0% | - |
| 🟡 | BmmFp8KNFwdOp | test_bmm_fp8_kn_bench[square-b4-1k-per-tensor-float8_e4m3fn] | 0.0391 | 219.66 | 0.43 | torch-fp32-ref 750.4%, flashinfer-bmm-fp8 90.6% | - |
| 🟢 | BmmFp8KNFwdOp | test_bmm_fp8_kn_bench[square-b8-2k-per-tensor-float8_e4m3fn] | 0.3059 | 449.31 | 0.44 | torch-fp32-ref 1326.9%, flashinfer-bmm-fp8 203.8% | - |
| 🔴 | BmmFp8KNFwdOp | test_bmm_fp8_kn_bench[mha-decode-b32-pv-per-tensor-float8_e4m3fn] | 0.0647 | 33.17 | 0.28 | torch-fp32-ref 364.4%, flashinfer-bmm-fp8 38.6% | - |
| 🔴 | BmmFp8KNFwdOp | test_bmm_fp8_kn_bench[mha-decode-b64-qk-per-tensor-float8_e4m3fn] | 0.1156 | 37.15 | 0.44 | torch-fp32-ref 250.1%, flashinfer-bmm-fp8 42.9% | - |
| 🔴 | BmmFp8KNFwdOp | test_bmm_fp8_kn_bench[moe-prefill-b128-per-tensor-float8_e4m3fn] | 0.9008 | 152.57 | 0.37 | torch-fp32-ref 599.5%, flashinfer-bmm-fp8 69.4% | - |
| 🔵 | BmmFp8NKFwdOp | test_bmm_fp8_nk_bench[square-b4-1k-per-tensor-float8_e4m3fn] | 0.0118 | 725.50 | 1.42 | torch-fp32-ref 2480.0%, flashinfer-bmm-fp8 110.3% | - |
| 🔵 | BmmFp8NKFwdOp | test_bmm_fp8_nk_bench[square-b8-2k-per-tensor-float8_e4m3fn] | 0.1197 | 1147.76 | 1.12 | torch-fp32-ref 3395.3%, flashinfer-bmm-fp8 105.1% | - |
| 🔵 | BmmFp8NKFwdOp | test_bmm_fp8_nk_bench[mha-decode-b32-pv-per-tensor-float8_e4m3fn] | 0.0091 | 237.13 | 1.97 | torch-fp32-ref 2613.4%, flashinfer-bmm-fp8 105.1% | - |
| 🔵 | BmmFp8NKFwdOp | test_bmm_fp8_nk_bench[mha-decode-b64-qk-per-tensor-float8_e4m3fn] | 0.0157 | 272.80 | 3.26 | torch-fp32-ref 1830.5%, flashinfer-bmm-fp8 137.2% | - |
| 🔵 | BmmFp8NKFwdOp | test_bmm_fp8_nk_bench[moe-prefill-b128-per-tensor-float8_e4m3fn] | 0.1318 | 1042.97 | 2.55 | torch-fp32-ref 4099.7%, flashinfer-bmm-fp8 105.2% | - |
| 🔵 | BmmFwdOp | test_bmm_bench[small-b8-128-float16] | 0.0027 | 12.48 | 0.29 | flaggems 117.9%, torch-cublas 120.2% | - |
| 🔵 | BmmFwdOp | test_bmm_bench[small-b8-128-bfloat16] | 0.0027 | 12.34 | 0.29 | flaggems 116.5%, torch-cublas 118.8% | - |
| 🔴 | BmmFwdOp | test_bmm_bench[square-b8-1k-float16] | 0.0405 | 423.73 | 1.24 | flaggems 110.6%, torch-cublas 76.7% | - |
| 🔴 | BmmFwdOp | test_bmm_bench[square-b8-1k-bfloat16] | 0.0408 | 420.91 | 1.23 | flaggems 109.6%, torch-cublas 76.0% | - |
| 🟡 | BmmFwdOp | test_bmm_bench[square-b16-512-float16] | 0.0133 | 323.43 | 1.90 | flaggems 113.7%, torch-cublas 91.1% | - |
| 🟡 | BmmFwdOp | test_bmm_bench[square-b16-512-bfloat16] | 0.0133 | 321.87 | 1.89 | flaggems 113.2%, torch-cublas 89.7% | - |
| 🔵 | BmmFwdOp | test_bmm_bench[square-b32-256-float16] | 0.0066 | 162.89 | 1.91 | flaggems 119.9%, torch-cublas 107.3% | - |
| 🔵 | BmmFwdOp | test_bmm_bench[square-b32-256-bfloat16] | 0.0066 | 163.68 | 1.92 | flaggems 120.5%, torch-cublas 107.8% | - |
| 🔴 | BmmFwdOp | test_bmm_bench[square-b4-4k-bfloat16] | 1.0413 | 527.93 | 0.39 | flaggems 92.9%, torch-cublas 73.6% | - |
| 🔴 | BmmFwdOp | test_bmm_bench[square-b8-2k-float16] | 0.2836 | 484.65 | 0.71 | flaggems 97.4%, torch-cublas 73.5% | - |
| 🔴 | BmmFwdOp | test_bmm_bench[square-b8-2k-bfloat16] | 0.2804 | 490.24 | 0.72 | flaggems 97.4%, torch-cublas 73.1% | - |
| 🟡 | BmmFwdOp | test_bmm_bench[mha-decode-b64-qk-float16] | 0.0226 | 189.84 | 3.06 | flaggems 115.4%, torch-cublas 93.9% | - |
| 🟡 | BmmFwdOp | test_bmm_bench[mha-decode-b64-qk-bfloat16] | 0.0225 | 190.65 | 3.07 | flaggems 115.8%, torch-cublas 94.2% | - |
| 🔵 | BmmFwdOp | test_bmm_bench[mha-decode-b64-pv-float16] | 0.0240 | 179.20 | 2.89 | flaggems 169.6%, torch-cublas 101.7% | - |
| 🔵 | BmmFwdOp | test_bmm_bench[mha-decode-b64-pv-bfloat16] | 0.0240 | 178.96 | 2.88 | flaggems 169.1%, torch-cublas 101.7% | - |
| 🔴 | BmmFwdOp | test_bmm_bench[moe-prefill-b128-bfloat16] | 0.2896 | 474.61 | 2.09 | flaggems 102.0%, torch-cublas 74.6% | - |
| 🟢 | CBProducerFwdOp | test_cb_producer_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0072 | 18.72 | 0.59 | torch 528.1% | - |
| 🟢 | CBProducerFwdOp | test_cb_producer_fwd_bench[mamba2-2p7b-b4-s2k-bfloat16] | 0.0118 | 22.67 | 0.71 | torch 448.4% | - |
| 🔵 | CeilFwdOp | test_ceil_bench[elementwise-16M-float16] | 0.0179 | 0.94 | 3.75 | torch 100.5%, torch-compile 100.2% | - |
| 🔵 | CeilFwdOp | test_ceil_bench[elementwise-16M-bfloat16] | 0.0179 | 0.94 | 3.75 | torch 100.4%, torch-compile 100.2% | - |
| 🟡 | CeilFwdOp | test_ceil_bench[elementwise-16M-float32] | 0.0340 | 0.49 | 3.95 | torch 99.8%, torch-compile 99.8% | - |
| 🔵 | CeilFwdOp | test_ceil_bench[elementwise-256M-float16] | 0.2498 | 1.07 | 4.30 | torch 100.2%, torch-compile 100.0% | - |
| 🟡 | CeilFwdOp | test_ceil_bench[elementwise-256M-bfloat16] | 0.2505 | 1.07 | 4.29 | torch 99.9%, torch-compile 100.1% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-float16] | 0.0356 | 0.47 | 3.77 | torch 98.0%, torch-compile 98.5% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-bfloat16] | 0.0354 | 0.47 | 3.79 | torch 98.6%, torch-compile 99.0% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-float32] | 0.0658 | 0.25 | 4.08 | torch 99.6%, torch-compile 99.5% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-256M-float16] | 0.4860 | 0.55 | 4.42 | torch 99.9%, torch-compile 99.8% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-256M-bfloat16] | 0.4855 | 0.55 | 4.42 | torch 99.9%, torch-compile 99.9% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-min-only-float16] | 0.0267 | 0.63 | 3.78 | torch 99.9%, torch-compile 98.8% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-min-only-bfloat16] | 0.0269 | 0.62 | 3.74 | torch 99.7%, torch-compile 98.0% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-min-only-float32] | 0.0500 | 0.34 | 4.02 | torch 98.5%, torch-compile 98.7% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-256M-min-only-float16] | 0.3693 | 0.73 | 4.36 | torch 99.8%, torch-compile 99.9% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-256M-min-only-bfloat16] | 0.3684 | 0.73 | 4.37 | torch 99.8%, torch-compile 100.1% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-max-only-float16] | 0.0266 | 0.63 | 3.79 | torch 99.9%, torch-compile 98.9% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-max-only-bfloat16] | 0.0271 | 0.62 | 3.71 | torch 99.2%, torch-compile 98.1% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-max-only-float32] | 0.0500 | 0.34 | 4.03 | torch 98.9%, torch-compile 98.8% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-256M-max-only-float16] | 0.3688 | 0.73 | 4.37 | torch 99.8%, torch-compile 100.0% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-256M-max-only-bfloat16] | 0.3680 | 0.73 | 4.38 | torch 99.9%, torch-compile 100.2% | - |
| 🔵 | ClampScalarFwdOp | test_clamp_scalar_manifest_bench[elementwise-16M-float16] | 0.0184 | 0.91 | 3.64 | torch 110.2%, torch-compile 100.2% | - |
| 🔵 | ClampScalarFwdOp | test_clamp_scalar_manifest_bench[elementwise-16M-bfloat16] | 0.0184 | 0.91 | 3.64 | torch 104.0%, torch-compile 101.1% | - |
| 🔵 | ClampScalarFwdOp | test_clamp_scalar_manifest_bench[elementwise-16M-float32] | 0.0338 | 0.50 | 3.97 | torch 100.8%, torch-compile 100.6% | - |
| 🔵 | ClampScalarFwdOp | test_clamp_scalar_manifest_bench[elementwise-256M-float16] | 0.2519 | 1.07 | 4.26 | torch 115.9%, torch-compile 100.6% | - |
| 🔵 | ClampScalarFwdOp | test_clamp_scalar_manifest_bench[elementwise-256M-bfloat16] | 0.2520 | 1.07 | 4.26 | torch 109.4%, torch-compile 105.3% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[whisper-large-conv1-float16] | 0.0482 | 38.25 | 0.18 | flaggems 233.0%, torch 118.1%, torch-compile 118.1% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[whisper-large-conv1-bfloat16] | 0.0485 | 37.94 | 0.18 | flaggems 231.3%, torch 116.2%, torch-compile 116.1% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[wav2vec2-layer1-float16] | 0.0067 | 4.90 | 0.50 | flaggems 599.8%, torch 278.5%, torch-compile 278.5% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[wav2vec2-layer1-bfloat16] | 0.0067 | 4.91 | 0.50 | flaggems 602.2%, torch 282.0%, torch-compile 282.5% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[encodec-init-float16] | 0.0035 | 3.05 | 0.45 | flaggems 695.0%, torch 189.1%, torch-compile 188.6% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[encodec-init-bfloat16] | 0.0035 | 3.05 | 0.45 | flaggems 693.2%, torch 189.1%, torch-compile 188.2% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[encodec-deep-float16] | 0.0120 | 32.28 | 0.09 | flaggems 595.5%, torch 141.6%, torch-compile 141.3% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[encodec-deep-bfloat16] | 0.0120 | 32.28 | 0.09 | flaggems 594.9%, torch 141.1%, torch-compile 141.2% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[whisper-large-conv1-bias-float16] | 0.0477 | 38.69 | 0.18 | flaggems 233.9%, torch 145.3%, torch-compile 133.7% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[whisper-large-conv1-bias-bfloat16] | 0.0477 | 38.66 | 0.18 | flaggems 233.8%, torch 145.1%, torch-compile 127.1% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[wav2vec2-layer1-bias-float16] | 0.0069 | 4.98 | 0.48 | flaggems 568.1%, torch 365.0%, torch-compile 325.9% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[wav2vec2-layer1-bias-bfloat16] | 0.0069 | 4.98 | 0.48 | flaggems 566.6%, torch 369.9%, torch-compile 313.4% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[encodec-init-bias-float16] | 0.0036 | 3.21 | 0.44 | flaggems 657.4%, torch 292.8%, torch-compile 251.7% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[encodec-init-bias-bfloat16] | 0.0036 | 3.21 | 0.44 | flaggems 655.4%, torch 297.3%, torch-compile 239.3% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[encodec-deep-bias-float16] | 0.0124 | 31.29 | 0.09 | flaggems 569.9%, torch 164.8%, torch-compile 149.9% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[encodec-deep-bias-bfloat16] | 0.0124 | 31.21 | 0.09 | flaggems 567.8%, torch 163.4%, torch-compile 149.0% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[resnet-3x3-float16] | 0.0130 | 35.59 | 0.13 | flaggems 640.6%, torch 112.6%, torch-compile 89.2% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[resnet-3x3-bfloat16] | 0.0130 | 35.60 | 0.13 | flaggems 640.7%, torch 115.3%, torch-compile 91.4% | - |
| 🟢 | Conv2dFwdOp | test_conv2d_bench[stem-3x3-s2-float16] | 0.0036 | 3.02 | 0.13 | flaggems 363.4%, torch 181.2%, torch-compile 259.8% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[stage-transition-3x3-s2-float16] | 0.0137 | 33.68 | 0.13 | flaggems 865.3%, torch 123.8%, torch-compile 97.7% | - |
| 🔴 | Conv2dFwdOp | test_conv2d_bench[highres-3x3-s1-float16] | 0.1044 | 283.43 | 0.21 | flaggems 703.1%, torch 90.4%, torch-compile 75.6% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[midres-5x5-s1-float16] | 0.0161 | 79.64 | 0.10 | flaggems 1254.2%, torch 121.1%, torch-compile 99.8% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[stage-transition-5x5-s2-float16] | 0.0225 | 57.18 | 0.13 | flaggems 1380.9%, torch 113.2%, torch-compile 99.0% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[stride2-bfloat16] | 0.0111 | 5.19 | 0.05 | flaggems 582.3%, torch 133.4%, torch-compile 108.6% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[resnet-1x1-float16] | 0.0044 | 47.22 | 0.93 | flaggems 1128.7%, torch 97.1%, torch-compile 192.7% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[resnet-1x1-bfloat16] | 0.0044 | 46.88 | 0.92 | flaggems 1123.4%, torch 91.2%, torch-compile 189.1% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[bottleneck-expand-1x1-float16] | 0.0038 | 53.97 | 0.56 | flaggems 751.3%, torch 105.0%, torch-compile 195.0% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[bottleneck-reduce-1x1-float16] | 0.0047 | 43.99 | 0.46 | flaggems 564.7%, torch 93.2%, torch-compile 169.9% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[late-stage-1x1-float16] | 0.0050 | 20.59 | 0.21 | flaggems 309.0%, torch 126.9%, torch-compile 133.3% | - |
| 🔴 | Conv2dFwdOp | test_conv2d_bench[classifier-1x1-float16] | 0.0092 | 11.23 | 0.26 | flaggems 225.9%, torch 98.6%, torch-compile 79.0% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[deeplabv3-aspp-3x3-rate12-float16] | 0.0889 | 108.67 | 0.16 | flaggems 804.7%, torch 133.9%, torch-compile 102.4% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[mobilenetv2-depthwise-float16] | 0.0028 | 0.64 | 0.14 | flaggems 1925.0%, torch 107.9%, torch-compile 196.6% | - |
| 🟢 | Conv2dFwdOp | test_conv2d_bench[resnext-grouped-3x3-float16] | 0.0041 | 3.50 | 0.15 | flaggems 467.4%, torch 461.2%, torch-compile 461.2% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[resnet-3x3-bias-float16] | 0.0133 | 34.86 | 0.13 | flaggems 620.3%, torch 137.9%, torch-compile 88.9% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[resnet-3x3-bias-bfloat16] | 0.0138 | 33.64 | 0.12 | flaggems 599.3%, torch 133.0%, torch-compile 87.9% | - |
| 🟢 | Conv2dFwdOp | test_conv2d_bench[stem-3x3-s2-bias-float16] | 0.0035 | 3.16 | 0.14 | flaggems 350.9%, torch 272.5%, torch-compile 273.3% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[stage-transition-3x3-s2-bias-float16] | 0.0142 | 32.56 | 0.13 | flaggems 827.0%, torch 141.0%, torch-compile 96.9% | - |
| 🔴 | Conv2dFwdOp | test_conv2d_bench[highres-3x3-s1-bias-float16] | 0.1049 | 282.11 | 0.21 | flaggems 699.8%, torch 109.2%, torch-compile 75.3% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[midres-5x5-s1-bias-float16] | 0.0165 | 77.97 | 0.10 | flaggems 1221.8%, torch 139.6%, torch-compile 100.5% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[stage-transition-5x5-s2-bias-float16] | 0.0225 | 57.03 | 0.13 | flaggems 1374.5%, torch 127.4%, torch-compile 100.0% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[stride2-bias-bfloat16] | 0.0116 | 4.99 | 0.05 | flaggems 552.5%, torch 152.8%, torch-compile 107.2% | - |
| 🟢 | Conv2dFwdOp | test_conv2d_bench[resnet-1x1-bias-float16] | 0.0046 | 45.25 | 0.88 | flaggems 1054.0%, torch 254.5%, torch-compile 184.6% | - |
| 🟢 | Conv2dFwdOp | test_conv2d_bench[resnet-1x1-bias-bfloat16] | 0.0046 | 44.95 | 0.88 | flaggems 1049.3%, torch 249.3%, torch-compile 194.4% | - |
| 🟢 | Conv2dFwdOp | test_conv2d_bench[bottleneck-expand-1x1-bias-float16] | 0.0041 | 50.37 | 0.52 | flaggems 673.4%, torch 214.1%, torch-compile 185.2% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[bottleneck-reduce-1x1-bias-float16] | 0.0049 | 41.75 | 0.43 | flaggems 519.5%, torch 148.4%, torch-compile 169.5% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[late-stage-1x1-bias-float16] | 0.0053 | 19.50 | 0.19 | flaggems 279.1%, torch 175.4%, torch-compile 138.8% | - |
| 🔴 | Conv2dFwdOp | test_conv2d_bench[classifier-1x1-bias-float16] | 0.0095 | 10.79 | 0.25 | flaggems 209.4%, torch 124.2%, torch-compile 77.5% | - |
| 🟢 | Conv3dFwdOp | test_conv3d_bench[r3d-stem-k3-s1-float16] | 0.0229 | 90.69 | 1.17 | flaggems 374.1%, torch 500.0%, torch-compile 500.3% | - |
| 🔴 | Conv3dFwdOp | test_conv3d_bench[video-stage-downsample-k3-s2-float16] | 0.0349 | 39.75 | 0.13 | flaggems 622.5%, torch 75.6%, torch-compile 75.6% | - |
| 🔴 | Conv3dFwdOp | test_conv3d_bench[unet-encoder-k3-s1-bfloat16] | 0.3538 | 40.97 | 0.07 | flaggems 89.6%, torch 32.6%, torch-compile 32.6% | - |
| 🔴 | Conv3dFwdOp | test_conv3d_bench[3d-unet-aspp-3x3x3-rate6-float16] | 0.1268 | 57.15 | 0.04 | flaggems 236.8%, torch 29.6%, torch-compile 29.6% | - |
| 🟢 | Conv3dFwdOp | test_conv3d_bench[3d-resnext-grouped-k3-float16] | 0.0157 | 5.51 | 0.15 | flaggems 1615.7%, torch 1659.9%, torch-compile 1627.6% | - |
| 🟢 | Conv3dFwdOp | test_conv3d_bench[r3d-stem-k3-s1-bias-float16] | 0.0230 | 91.00 | 1.17 | flaggems 369.3%, torch 671.4%, torch-compile 548.7% | - |
| 🟡 | Conv3dFwdOp | test_conv3d_bench[video-stage-downsample-k3-s2-bias-float16] | 0.0353 | 39.28 | 0.13 | flaggems 610.7%, torch 84.9%, torch-compile 80.2% | - |
| 🔴 | Conv3dFwdOp | test_conv3d_bench[unet-encoder-k3-s1-bias-bfloat16] | 0.3538 | 41.00 | 0.07 | flaggems 89.3%, torch 39.9%, torch-compile 34.5% | - |
| 🔵 | CosFwdOp | test_cos_bench[elementwise-16M-float16] | 0.0260 | 0.65 | 2.59 | torch 104.8%, torch-compile 108.1% | - |
| 🔵 | CosFwdOp | test_cos_bench[elementwise-16M-bfloat16] | 0.0265 | 0.63 | 2.53 | torch 102.5%, torch-compile 106.6% | - |
| 🟡 | CosFwdOp | test_cos_bench[elementwise-16M-float32] | 0.0352 | 0.48 | 3.81 | torch 97.5%, torch-compile 97.5% | - |
| 🔵 | CosFwdOp | test_cos_bench[elementwise-256M-float16] | 0.3762 | 0.71 | 2.85 | torch 104.3%, torch-compile 108.3% | - |
| 🔵 | CosFwdOp | test_cos_bench[elementwise-256M-bfloat16] | 0.3839 | 0.70 | 2.80 | torch 102.5%, torch-compile 107.3% | - |
| 🔵 | CountNonzeroFwdOp | test_count_nonzero_bench[sparsity-hidden-float16] | 0.0081 | 2.07 | 2.07 | torch 788.2%, torch-compile 113.8% | - |
| 🔵 | CountNonzeroFwdOp | test_count_nonzero_bench[sparsity-hidden-bfloat16] | 0.0081 | 2.08 | 2.08 | torch 793.2%, torch-compile 113.9% | - |
| 🔵 | CountNonzeroFwdOp | test_count_nonzero_bench[sparsity-seq-float16] | 0.0037 | 0.56 | 0.56 | torch 408.5%, torch-compile 104.3% | - |
| 🔴 | CountNonzeroFwdOp | test_count_nonzero_bench[3d-multidim-reduce-float16] | 0.0116 | 0.36 | 0.36 | torch 188.4%, torch-compile 41.3% | - |
| 🟢 | CumprodFwdOp | test_cumprod_bench[hidden-state-scan-float16] | 0.0115 | 0.73 | 2.92 | torch 1269.5%, torch-compile 210.9% | - |
| 🟢 | CumprodFwdOp | test_cumprod_bench[hidden-state-scan-bfloat16] | 0.0109 | 0.77 | 3.08 | torch 1339.3%, torch-compile 223.5% | - |
| 🟢 | CumprodFwdOp | test_cumprod_bench[long-seq-scan-bfloat16] | 0.0070 | 0.30 | 1.19 | torch 961.8%, torch-compile 172.7% | - |
| 🟡 | CumsumFwdOp | test_cumsum_bench[hidden-state-scan-float16] | 0.0115 | 0.73 | 2.91 | flaggems 91.7%, torch 1265.1%, torch-compile 210.0% | - |
| 🟡 | CumsumFwdOp | test_cumsum_bench[hidden-state-scan-bfloat16] | 0.0109 | 0.77 | 3.08 | flaggems 96.8%, torch 1339.6%, torch-compile 223.2% | - |
| 🔵 | CumsumFwdOp | test_cumsum_bench[long-seq-scan-bfloat16] | 0.0070 | 0.30 | 1.19 | flaggems 113.6%, torch 961.8%, torch-compile 172.7% | - |
| 🔴 | DaCumsumFwdOp | test_da_cumsum_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0043 | 0.32 | 0.46 | mamba 79.0%, torch-ref 1675.2%, torch-compile 112.0% | - |
| 🔴 | DaCumsumFwdOp | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-bfloat16] | 0.0121 | 0.61 | 0.86 | mamba 53.0%, torch-ref 749.6%, torch-compile 94.2% | - |
| 🟡 | DaCumsumFwdOp | test_da_cumsum_fwd_bench[mamba2-780m-b1-s4k-dt-bias-float16] | 0.0042 | 0.37 | 0.47 | mamba 81.8%, torch-ref 1749.2%, torch-compile 113.6% | - |
| 🔴 | DaCumsumFwdOp | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-dt-bias-bfloat16] | 0.0124 | 0.68 | 0.85 | mamba 52.1%, torch-ref 779.5%, torch-compile 92.5% | - |
| 🔴 | DaCumsumFwdOp | test_da_cumsum_fwd_bench[mamba2-2p7b-b2-s32k-dt-bias-float16] | 0.0444 | 0.94 | 1.18 | mamba 50.2%, torch-ref 532.4%, torch-compile 77.9% | - |
| 🟢 | DeepSeekSparseAttentionDecodeWithKVCacheFwdOp | test_dsa_decode_bench[single-batch-mainstream-float16] | 1.8618 | 313.74 | 0.16 | torch-ref 1018.8%, torch-compile 892.3%, torch-sdpa 282.5% | - |
| 🟢 | DeepSeekSparseAttentionDecodeWithKVCacheFwdOp | test_dsa_decode_bench[longer-kv-lower-topk-float16] | 0.5007 | 291.63 | 0.30 | torch-ref 3858.0%, torch-compile 3251.3%, torch-sdpa 1053.4%, torch-gather 361.9% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s2k-h4-d64-float16] | 0.1306 | 2.06 | 0.21 | fla 86.7% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s2k-h4-d64-bfloat16] | 0.1316 | 2.04 | 0.21 | fla 86.9% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s4k-h4-d64-float16] | 0.2592 | 2.07 | 0.21 | fla 82.7% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s4k-h4-d64-bfloat16] | 0.2619 | 2.05 | 0.21 | fla 82.8% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s8k-h4-d64-float16] | 0.5057 | 2.12 | 0.22 | fla 85.5% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s8k-h4-d64-bfloat16] | 0.5104 | 2.10 | 0.21 | fla 85.5% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s16k-h4-d64-float16] | 0.9932 | 2.16 | 0.22 | fla 87.0% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s16k-h4-d64-bfloat16] | 1.0032 | 2.14 | 0.22 | fla 86.9% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b1-h8-d128-bfloat16] | 0.0028 | 0.28 | 0.19 | torch 1175.4%, torch-compile 459.6% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b1-h16-d128-bfloat16] | 0.0031 | 0.51 | 0.34 | torch 1138.1%, torch-compile 455.7% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b1-h32-d128-bfloat16] | 0.0034 | 0.94 | 0.63 | torch 1164.3%, torch-compile 483.8% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b1-h48-d128-bfloat16] | 0.0036 | 1.33 | 0.90 | torch 1215.3%, torch-compile 538.1% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b1-h64-d128-bfloat16] | 0.0038 | 1.64 | 1.11 | torch 1143.4%, torch-compile 450.0% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b8-h32-d128-bfloat16] | 0.0087 | 2.90 | 1.96 | torch 1030.2%, torch-compile 458.5% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b8-h48-d128-bfloat16] | 0.0123 | 3.08 | 2.08 | torch 901.0%, torch-compile 321.6% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b8-h64-d128-bfloat16] | 0.0163 | 3.10 | 2.09 | torch 871.3%, torch-compile 315.7% | - |
| 🟡 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s2k-h4-d64-float16] | 0.0627 | 2.14 | 0.34 | fla 98.8% | - |
| 🟡 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s2k-h4-d64-bfloat16] | 0.0629 | 2.13 | 0.34 | fla 99.1% | - |
| 🟡 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s4k-h4-d64-float16] | 0.1095 | 2.45 | 0.38 | fla 89.9% | - |
| 🟡 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s4k-h4-d64-bfloat16] | 0.1097 | 2.45 | 0.38 | fla 90.6% | - |
| 🟡 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s8k-h4-d64-float16] | 0.2337 | 2.30 | 0.36 | fla 81.0% | - |
| 🟡 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s8k-h4-d64-bfloat16] | 0.2344 | 2.29 | 0.36 | fla 81.6% | - |
| 🔴 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s16k-h4-d64-float16] | 0.4729 | 2.27 | 0.36 | fla 77.4% | - |
| 🔴 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s16k-h4-d64-bfloat16] | 0.4737 | 2.27 | 0.35 | fla 78.0% | - |
| 🟡 | DivFwdOp | test_binary_arith_bench[div-1024x4096-float16-float16-DivFwdOp-div-positive] | 0.0084 | 0.50 | 2.98 | torch 103.8%, torch-compile 99.6% | - |
| 🟡 | DivFwdOp | test_binary_arith_bench[div-1024x10240-float16-float16-DivFwdOp-div-positive] | 0.0181 | 0.58 | 3.47 | torch 101.9%, torch-compile 99.6% | - |
| 🟡 | DivFwdOp | test_binary_arith_bench[div-1024x11008-float16-float16-DivFwdOp-div-positive] | 0.0189 | 0.60 | 3.58 | torch 102.0%, torch-compile 99.6% | - |
| 🟡 | DivFwdOp | test_div_manifest_bench[hidden-state-prefill-float16] | 0.0148 | 0.57 | 3.40 | torch 102.6%, torch-compile 99.4% | - |
| 🔵 | DivFwdOp | test_div_manifest_bench[hidden-state-prefill-bfloat16] | 0.0147 | 0.57 | 3.43 | torch 103.0%, torch-compile 100.0% | - |
| 🟡 | DivFwdOp | test_div_manifest_bench[hidden-state-prefill-float32] | 0.0263 | 0.32 | 3.82 | torch 100.3%, torch-compile 99.6% | - |
| 🟡 | DivFwdOp | test_div_manifest_bench[cnn-feat-broadcast-float16] | 0.0160 | 0.80 | 3.20 | torch 316.2%, torch-compile 92.0% | - |
| 🟡 | DivFwdOp | test_div_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0144 | 0.89 | 3.56 | torch 355.5%, torch-compile 99.6% | - |
| 🔵 | DivFwdOp | test_div_manifest_bench[cnn-feat-broadcast-float32] | 0.0265 | 0.49 | 3.88 | torch 200.5%, torch-compile 100.1% | - |
| 🟢 | DropoutFwdOp | test_dropout_bench[tokens-1k-hidden-4k-float16] | 0.0062 | 0.68 | 2.72 | torch 189.1%, torch-compile 182.9% | - |
| 🔵 | DropoutFwdOp | test_dropout_bench[tokens-1k-hidden-4k-float32] | 0.0103 | 0.41 | 3.27 | torch 144.8%, torch-compile 116.5% | - |
| 🟢 | DropoutFwdOp | test_dropout_bench[tokens-1k-hidden-10k-bfloat16] | 0.0123 | 0.85 | 3.40 | torch 192.2%, torch-compile 191.4% | - |
| 🔵 | EluFwdOp | test_elu_manifest_bench[mlp-hidden-float16] | 0.0122 | 2.76 | 2.76 | torch 147.9%, torch-compile 130.5% | - |
| 🔵 | EluFwdOp | test_elu_manifest_bench[mlp-hidden-bfloat16] | 0.0120 | 2.79 | 2.79 | torch 151.1%, torch-compile 139.1% | - |
| 🔵 | EluFwdOp | test_elu_manifest_bench[mlp-hidden-wide-float16] | 0.0218 | 3.08 | 3.08 | torch 150.2%, torch-compile 135.8% | - |
| 🔵 | EluFwdOp | test_elu_manifest_bench[mlp-hidden-wide-bfloat16] | 0.0215 | 3.12 | 3.12 | torch 154.6%, torch-compile 145.8% | - |
| 🔴 | EngramDecodeFwdOp | test_engram_decode_bench[decode-b1-dmem512-d256-float16] | 0.0330 | 0.02 | 0.02 | torch-ref 286.6%, torch-compile 39.8% | - |
| 🔴 | EngramDecodeFwdOp | test_engram_decode_bench[decode-b4-dmem1024-d512-float16] | 0.0825 | 0.10 | 0.03 | torch-ref 146.8%, torch-compile 31.0% | - |
| 🔴 | EngramDecodeFwdOp | test_engram_decode_bench[decode-b8-dmem512-d256-bfloat16] | 0.0335 | 0.13 | 0.02 | torch-ref 332.4%, torch-compile 64.1% | - |
| 🟢 | EngramGateConvBwdOp | test_engram_gate_conv_bwd_bench[bwd-b1-s32-d256-float16] | 0.0111 | 0.04 | 0.02 | torch 1509.0%, torch-compile 443.6% | - |
| 🟢 | EngramGateConvBwdOp | test_engram_gate_conv_bwd_bench[bwd-b2-s64-d512-float16] | 0.0198 | 0.20 | 0.07 | torch 1011.7%, torch-compile 296.7% | - |
| 🟢 | EngramGateConvBwdOp | test_engram_gate_conv_bwd_bench[bwd-b1-s128-d256-bfloat16] | 0.0168 | 0.12 | 0.04 | torch 1098.3%, torch-compile 323.5% | - |
| 🟢 | EngramGateConvFwdOp | test_engram_gate_conv_fwd_bench[fwd-b1-s32-d256-float16] | 0.0040 | 0.05 | 0.02 | torch-ref 1850.0%, torch-compile 284.0% | - |
| 🟢 | EngramGateConvFwdOp | test_engram_gate_conv_fwd_bench[fwd-b2-s64-d512-float16] | 0.0051 | 0.31 | 0.13 | torch-ref 1689.8%, torch-compile 246.8% | - |
| 🟢 | EngramGateConvFwdOp | test_engram_gate_conv_fwd_bench[fwd-b1-s128-d256-bfloat16] | 0.0045 | 0.18 | 0.07 | torch-ref 1791.0%, torch-compile 260.7% | - |
| 🔵 | EqFwdOp | test_comparison_bench[eq-1024x4096-float16-eq] | 0.0076 | 0.56 | 2.78 | torch 103.8%, torch-compile 103.4% | - |
| 🔵 | EqFwdOp | test_comparison_bench[eq-1024x10240-float16-eq] | 0.0158 | 0.66 | 3.32 | torch 101.4%, torch-compile 101.4% | - |
| 🔵 | EqFwdOp | test_eq_manifest_bench[hidden-state-prefill-float16] | 0.0133 | 0.63 | 3.15 | torch 101.9%, torch-compile 101.7% | - |
| 🟡 | EqFwdOp | test_eq_manifest_bench[hidden-state-prefill-bfloat16] | 0.0131 | 0.64 | 3.20 | torch 99.5%, torch-compile 99.5% | - |
| 🟡 | EqFwdOp | test_eq_manifest_bench[hidden-state-prefill-float32] | 0.0223 | 0.38 | 3.38 | torch 99.9%, torch-compile 99.9% | - |
| 🔴 | EqFwdOp | test_eq_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.81 | 2.42 | torch 299.4%, torch-compile 75.0% | - |
| 🔴 | EqFwdOp | test_eq_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.81 | 2.42 | torch 306.6%, torch-compile 74.9% | - |
| 🟡 | EqFwdOp | test_eq_manifest_bench[cnn-feat-broadcast-float32] | 0.0209 | 0.61 | 3.07 | torch 229.4%, torch-compile 88.1% | - |
| 🟡 | ErfFwdOp | test_erf_bench[elementwise-16M-float16] | 0.0284 | 0.59 | 2.36 | torch 93.4%, torch-compile 103.4% | - |
| 🟡 | ErfFwdOp | test_erf_bench[elementwise-16M-bfloat16] | 0.0286 | 0.59 | 2.35 | torch 97.3%, torch-compile 103.5% | - |
| 🟡 | ErfFwdOp | test_erf_bench[elementwise-16M-float32] | 0.0351 | 0.48 | 3.82 | torch 97.8%, torch-compile 98.5% | - |
| 🟡 | ErfFwdOp | test_erf_bench[elementwise-256M-float16] | 0.4215 | 0.64 | 2.55 | torch 91.6%, torch-compile 102.5% | - |
| 🟡 | ErfFwdOp | test_erf_bench[elementwise-256M-bfloat16] | 0.4233 | 0.63 | 2.54 | torch 96.0%, torch-compile 103.2% | - |
| 🔵 | ExpFwdOp | test_exp_bench[elementwise-16M-float16] | 0.0180 | 0.93 | 3.72 | torch 100.9%, torch-compile 100.5% | - |
| 🔵 | ExpFwdOp | test_exp_bench[elementwise-16M-bfloat16] | 0.0182 | 0.92 | 3.69 | torch 100.8%, torch-compile 101.4% | - |
| 🔵 | ExpFwdOp | test_exp_bench[elementwise-16M-float32] | 0.0340 | 0.49 | 3.95 | torch 100.3%, torch-compile 100.1% | - |
| 🔵 | ExpFwdOp | test_exp_bench[elementwise-256M-float16] | 0.2544 | 1.06 | 4.22 | torch 101.0%, torch-compile 101.0% | - |
| 🔵 | ExpFwdOp | test_exp_bench[elementwise-256M-bfloat16] | 0.2570 | 1.04 | 4.18 | torch 100.7%, torch-compile 102.3% | - |
| 🔵 | Expm1FwdOp | test_expm1_bench[elementwise-16M-float16] | 0.0180 | 1.87 | 3.74 | torch 141.0%, torch-compile 150.3% | - |
| 🟢 | Expm1FwdOp | test_expm1_bench[elementwise-16M-bfloat16] | 0.0181 | 1.86 | 3.71 | torch 154.5%, torch-compile 155.1% | - |
| 🔵 | Expm1FwdOp | test_expm1_bench[elementwise-16M-float32] | 0.0340 | 0.99 | 3.95 | torch 100.7%, torch-compile 101.2% | - |
| 🔵 | Expm1FwdOp | test_expm1_bench[elementwise-256M-float16] | 0.2535 | 2.12 | 4.24 | torch 145.0%, torch-compile 155.2% | - |
| 🟢 | Expm1FwdOp | test_expm1_bench[elementwise-256M-bfloat16] | 0.2571 | 2.09 | 4.18 | torch 159.9%, torch-compile 159.8% | - |
| 🔴 | FFTC2CFwdOp | test_fft_bench[fft-4k-c64-unbatched-complex64] | 0.0081 | 0.03 | 0.01 | torch-cufft 66.1%, torch-compile 66.1% | - |
| 🔴 | FFTC2CFwdOp | test_fft_bench[fft-4k-c64-b64-complex64] | 0.0152 | 1.04 | 0.28 | torch-cufft 37.1%, torch-compile 37.0% | - |
| 🔴 | FFTC2CFwdOp | test_fft_bench[fft-4k-c128-b64-complex128] | 0.0204 | 0.77 | 0.41 | torch-cufft 42.0%, torch-compile 42.0% | - |
| 🟢 | FP8LightningIndexerFwdOp | test_fp8_lightning_indexer_bench[lightning-indexer-s8k-h32-d64-bfloat16] | 0.6176 | 55.63 | 1.80 | torch-ref 18131.1%, torch-compile 8051.2% | - |
| 🔵 | FP8QuantFwdOp | test_fp8_quant_bench[kv-index-8k-d64-float16] | 0.0028 | 1.15 | 0.58 | torch-ref 608.1%, torch-compile 100.0% | - |
| 🟡 | FP8QuantFwdOp | test_fp8_quant_bench[kv-index-8k-d64-bfloat16] | 0.0028 | 1.15 | 0.58 | torch-ref 611.6%, torch-compile 98.8% | - |
| 🔵 | FP8QuantFwdOp | test_fp8_quant_bench[kv-index-4k-d128-float32] | 0.0039 | 0.80 | 0.67 | torch-ref 390.2%, torch-compile 123.6% | - |
| 🔵 | FloorDivideFwdOp | test_binary_arith_bench[floor_divide-1024x4096-float16-float16-FloorDivideFwdOp-floor_divide-positive] | 0.0087 | 0.48 | 2.89 | torch 302.9%, torch-compile 100.4% | - |
| 🔵 | FloorDivideFwdOp | test_binary_arith_bench[floor_divide-1024x10240-float16-float16-FloorDivideFwdOp-floor_divide-positive] | 0.0180 | 0.58 | 3.50 | torch 331.2%, torch-compile 100.2% | - |
| 🔵 | FloorDivideFwdOp | test_floor_divide_manifest_bench[hidden-state-prefill-float16] | 0.0151 | 1.11 | 3.33 | torch 321.2%, torch-compile 100.2% | - |
| 🔵 | FloorDivideFwdOp | test_floor_divide_manifest_bench[hidden-state-prefill-bfloat16] | 0.0148 | 1.13 | 3.39 | torch 339.2%, torch-compile 100.2% | - |
| 🔵 | FloorDivideFwdOp | test_floor_divide_manifest_bench[hidden-state-prefill-float32] | 0.0264 | 0.64 | 3.82 | torch 180.2%, torch-compile 100.4% | - |
| 🟡 | FloorDivideFwdOp | test_floor_divide_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 1.61 | 3.22 | torch 694.1%, torch-compile 99.2% | - |
| 🔵 | FloorDivideFwdOp | test_floor_divide_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 1.62 | 3.23 | torch 715.6%, torch-compile 100.0% | - |
| 🔵 | FloorDivideFwdOp | test_floor_divide_manifest_bench[cnn-feat-broadcast-float32] | 0.0266 | 0.97 | 3.86 | torch 381.8%, torch-compile 100.4% | - |
| 🔵 | FloorFwdOp | test_floor_bench[elementwise-16M-float16] | 0.0179 | 0.94 | 3.74 | torch 100.2%, torch-compile 100.0% | - |
| 🔵 | FloorFwdOp | test_floor_bench[elementwise-16M-bfloat16] | 0.0179 | 0.94 | 3.76 | torch 100.4%, torch-compile 100.3% | - |
| 🟡 | FloorFwdOp | test_floor_bench[elementwise-16M-float32] | 0.0340 | 0.49 | 3.95 | torch 100.1%, torch-compile 99.9% | - |
| 🔵 | FloorFwdOp | test_floor_bench[elementwise-256M-float16] | 0.2497 | 1.08 | 4.30 | torch 100.2%, torch-compile 100.1% | - |
| 🔵 | FloorFwdOp | test_floor_bench[elementwise-256M-bfloat16] | 0.2498 | 1.07 | 4.30 | torch 100.2%, torch-compile 100.4% | - |
| 🔵 | FusedAddLayerNormFwdOp | test_fused_add_layer_norm_bench[llama-8b-prefill-float16] | 0.0211 | 2.39 | 3.18 | torch-ref 549.9%, torch-compile 130.5% | - |
| 🔵 | FusedAddLayerNormFwdOp | test_fused_add_layer_norm_bench[llama-8b-prefill-bfloat16] | 0.0220 | 2.29 | 3.05 | torch-ref 531.9%, torch-compile 131.7% | - |
| 🔵 | FusedAddLayerNormFwdOp | test_fused_add_layer_norm_bench[llama-8b-decode-bfloat16] | 0.0032 | 0.01 | 0.02 | torch-ref 597.9%, torch-compile 117.2% | - |
| 🔵 | FusedAddLayerNormFwdOp | test_fused_add_layer_norm_bench[llama-70b-prefill-float16] | 0.0441 | 2.28 | 3.04 | torch-ref 516.2%, torch-compile 101.8% | - |
| 🟡 | FusedAddLayerNormFwdOp | test_fused_add_layer_norm_bench[llama-70b-prefill-bfloat16] | 0.0474 | 2.13 | 2.83 | torch-ref 484.7%, torch-compile 97.8% | - |
| 🔵 | FusedAddLayerNormFwdOp | test_fused_add_layer_norm_bench[llama-70b-decode-bfloat16] | 0.0041 | 0.01 | 0.02 | torch-ref 627.9%, torch-compile 135.7% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-8b-prefill-float16] | 0.0208 | 2.01 | 3.22 | flashinfer 92.8%, vllm 90.0%, torch-ref 1282.2%, torch-compile 94.0% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-8b-prefill-bfloat16] | 0.0213 | 1.97 | 3.15 | flashinfer 90.6%, vllm 89.8%, torch-ref 1261.7%, torch-compile 92.3% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-8b-decode-bfloat16] | 0.0028 | 0.01 | 0.01 | flashinfer 88.4%, vllm 108.2%, torch-ref 1048.1%, torch-compile 86.6% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-70b-prefill-float16] | 0.0377 | 2.23 | 3.56 | flashinfer 96.3%, vllm 95.1%, torch-ref 1364.3%, torch-compile 96.4% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-70b-prefill-bfloat16] | 0.0381 | 2.20 | 3.52 | flashinfer 94.8%, vllm 95.4%, torch-ref 1358.4%, torch-compile 95.7% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-70b-decode-bfloat16] | 0.0035 | 0.01 | 0.02 | flashinfer 83.3%, vllm 101.8%, torch-ref 869.1%, torch-compile 85.6% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-405b-prefill-float16] | 0.0771 | 2.18 | 3.48 | flashinfer 92.6%, vllm 101.0%, torch-ref 1275.6%, torch-compile 92.8% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-405b-prefill-bfloat16] | 0.0855 | 1.96 | 3.14 | flashinfer 83.8%, vllm 91.5%, torch-ref 1160.1%, torch-compile 84.4% | - |
| 🔴 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-405b-decode-bfloat16] | 0.0062 | 0.01 | 0.03 | flashinfer 70.2%, vllm 80.6%, torch-ref 512.9%, torch-compile 101.6% | - |
| 🔵 | FusedMoEExpertsNopadPersistent3WGFwdOp | test_moe_experts_nopad_bench[qwen3-235b-decode-bfloat16] | 2.7693 | 130.28 | 4.08 | vllm-triton 103.1% | - |
| 🔵 | FusedMoEExpertsNopadPersistent3WGFwdOp | test_moe_experts_nopad_bench[qwen3-235b-prefill-bfloat16] | 5.9818 | 482.50 | 1.90 | vllm-triton 121.0% | - |
| 🔵 | FusedMoEExpertsNopadPersistent3WGFwdOp | test_moe_experts_nopad_bench[deepseek-v3-decode-bfloat16] | 5.4138 | 66.64 | 4.17 | vllm-triton 101.8% | - |
| 🔵 | FusedMoEExpertsNopadPersistent3WGFwdOp | test_moe_experts_nopad_bench[deepseek-v3-prefill-bfloat16] | 8.4578 | 341.25 | 2.68 | vllm-triton 105.3% | - |
|  | FusedMoEExpertsNopadPersistent3WGFwdOp | test_moe_experts_nopad_bench[deepseek-v3-ep2-decode-bfloat16] | 2.7242 | 132.43 | 4.14 | - | - |
|  | FusedMoEExpertsNopadPersistent3WGFwdOp | test_moe_experts_nopad_bench[deepseek-v3-ep2-prefill-bfloat16] | 4.1733 | 691.59 | 2.73 | - | - |
| 🔵 | FusedMoeFwdOp | test_fused_moe_fwd_bench[qwen3-235b-decode-bfloat16] | 2.7743 | 130.04 | 4.07 | vllm 103.0% | - |
| 🔵 | FusedMoeFwdOp | test_fused_moe_fwd_bench[qwen3-235b-prefill-bfloat16] | 5.9987 | 481.14 | 1.90 | vllm 120.7% | - |
| 🔵 | FusedMoeFwdOp | test_fused_moe_fwd_bench[deepseek-v3-decode-bfloat16] | 5.4247 | 66.51 | 4.16 | vllm 101.7% | - |
| 🔵 | FusedMoeFwdOp | test_fused_moe_fwd_bench[deepseek-v3-prefill-bfloat16] | 8.2918 | 348.08 | 2.73 | vllm 107.1% | - |
| 🟢 | FusedMoeFwdOp | test_fused_moe_fwd_bench[kimi-k2-decode-bfloat16] | 3.8964 | 92.59 | 5.79 | torch-ref 1453.5% | - |
| 🟢 | FusedMoeFwdOp | test_fused_moe_fwd_bench[kimi-k2-prefill-bfloat16] | 7.8877 | 365.91 | 2.87 | torch-ref 1785.2% | - |
| 🟡 | FusedTopKOp | test_fused_topk_bench[1-384-8-sigmoid-renormalize] | 0.0083 | 0.00 | 0.00 | vllm 99.2% | - |
| 🟡 | FusedTopKOp | test_fused_topk_bench[32-384-8-sigmoid-renormalize] | 0.0119 | 0.02 | 0.00 | vllm 81.4% | - |
| 🟡 | FusedTopKOp | test_fused_topk_bench[512-384-8-sigmoid-renormalize] | 0.0126 | 0.28 | 0.03 | vllm 83.2% | - |
| 🔵 | FusedTopKOp | test_fused_topk_bench[4096-384-8-sigmoid-renormalize] | 0.0203 | 1.40 | 0.17 | vllm 117.4% | - |
| 🔵 | FusedTopKOp | test_fused_topk_bench[1-128-8-softmax-norenormalize] | 0.0043 | 0.00 | 0.00 | vllm 142.1% | - |
| 🔵 | FusedTopKOp | test_fused_topk_bench[32-128-8-softmax-norenormalize] | 0.0074 | 0.01 | 0.00 | vllm 112.1% | - |
| 🔵 | FusedTopKOp | test_fused_topk_bench[512-128-8-softmax-norenormalize] | 0.0078 | 0.15 | 0.02 | vllm 115.6% | - |
| 🔵 | FusedTopKOp | test_fused_topk_bench[4096-128-8-softmax-norenormalize] | 0.0110 | 0.86 | 0.12 | vllm 146.5% | - |
| 🟡 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s2k-h4-d64-float16] | 0.1829 | 1.47 | 0.17 | fla 81.0% | - |
| 🟡 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s2k-h4-d64-bfloat16] | 0.1845 | 1.45 | 0.17 | fla 80.3% | - |
| 🔴 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s4k-h4-d64-float16] | 0.3687 | 1.46 | 0.17 | fla 78.1% | - |
| 🔴 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s4k-h4-d64-bfloat16] | 0.3643 | 1.47 | 0.17 | fla 79.1% | - |
| 🔴 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s8k-h4-d64-float16] | 0.7452 | 1.44 | 0.17 | fla 74.7% | - |
| 🔴 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s8k-h4-d64-bfloat16] | 0.7265 | 1.48 | 0.17 | fla 76.7% | - |
| 🔴 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s16k-h4-d64-float16] | 1.5153 | 1.42 | 0.17 | fla 71.4% | - |
| 🔴 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s16k-h4-d64-bfloat16] | 1.4486 | 1.48 | 0.17 | fla 74.6% | - |
| 🟡 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b1-h8-d128-bfloat16] | 0.0074 | 0.07 | 0.07 | fla 91.4%, torch 410.3%, torch-compile 81.5% | - |
| 🟡 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b1-h16-d128-bfloat16] | 0.0074 | 0.14 | 0.14 | fla 94.6%, torch 429.9%, torch-compile 95.5% | - |
| 🟡 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b1-h32-d128-bfloat16] | 0.0078 | 0.27 | 0.27 | fla 93.8%, torch 459.4%, torch-compile 106.6% | - |
| 🔵 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b1-h48-d128-bfloat16] | 0.0080 | 0.40 | 0.40 | fla 112.7%, torch 507.2%, torch-compile 120.3% | - |
| 🔵 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b1-h64-d128-bfloat16] | 0.0081 | 0.52 | 0.53 | fla 107.3%, torch 515.1%, torch-compile 108.1% | - |
| 🔵 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b8-h32-d128-bfloat16] | 0.0159 | 1.06 | 1.08 | fla 110.5%, torch 564.4%, torch-compile 133.0% | - |
| 🟡 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b8-h48-d128-bfloat16] | 0.0231 | 1.09 | 1.11 | fla 96.1%, torch 522.1%, torch-compile 106.2% | - |
| 🟡 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b8-h64-d128-bfloat16] | 0.0305 | 1.10 | 1.12 | fla 88.1%, torch 518.4%, torch-compile 105.1% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-float16] | 0.0986 | 1.36 | 0.11 | fla 71.2% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-bfloat16] | 0.0971 | 1.38 | 0.11 | fla 67.9% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-init-b2-s4k-h4-d64-float16] | 0.1571 | 1.71 | 0.13 | fla 79.8% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-init-b2-s4k-h4-d64-bfloat16] | 0.1564 | 1.72 | 0.13 | fla 76.5% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-float16] | 0.3128 | 1.72 | 0.13 | fla 79.2% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-bfloat16] | 0.3117 | 1.72 | 0.13 | fla 70.5% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-float16] | 0.6178 | 1.74 | 0.14 | fla 75.3% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-bfloat16] | 0.6115 | 1.76 | 0.14 | fla 74.0% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-float16] | 0.0866 | 12.40 | 0.20 | fla 77.6% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-bfloat16] | 0.0866 | 12.40 | 0.20 | fla 77.9% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-float16] | 0.1487 | 14.44 | 0.23 | fla 72.4% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-bfloat16] | 0.1444 | 14.87 | 0.23 | fla 75.0% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-float16] | 0.3142 | 13.67 | 0.21 | fla 65.2% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-bfloat16] | 0.3167 | 13.56 | 0.21 | fla 64.9% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-float16] | 0.6360 | 13.51 | 0.21 | fla 61.5% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-bfloat16] | 0.6389 | 13.45 | 0.21 | fla 61.6% | - |
| 🔵 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s2k-h4-d64-float16] | 0.0670 | 16.03 | 0.25 | fla 100.3% | - |
| 🔵 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s2k-h4-d64-bfloat16] | 0.0665 | 16.16 | 0.25 | fla 101.5% | - |
| 🟡 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s4k-h4-d64-float16] | 0.1151 | 18.65 | 0.29 | fla 93.5% | - |
| 🟡 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s4k-h4-d64-bfloat16] | 0.1145 | 18.75 | 0.29 | fla 94.5% | - |
| 🟡 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s8k-h4-d64-float16] | 0.2193 | 19.59 | 0.31 | fla 93.6% | - |
| 🟡 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s8k-h4-d64-bfloat16] | 0.2204 | 19.49 | 0.31 | fla 93.2% | - |
| 🟡 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s16k-h4-d64-float16] | 0.4298 | 19.99 | 0.31 | fla 90.8% | - |
| 🟡 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s16k-h4-d64-bfloat16] | 0.4326 | 19.86 | 0.31 | fla 91.0% | - |
| 🟢 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s32k-h4-d64-float16] | 0.1945 | 88.31 | 1.39 | fla 394.1% | - |
| 🟢 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s32k-h4-d64-bfloat16] | 0.1955 | 87.88 | 1.38 | fla 393.8% | - |
| 🔵 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b1-s4k-h16-d128-float16] | 0.1751 | 58.24 | 0.77 | fla 110.4% | - |
| 🔵 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b1-s4k-h16-d128-bfloat16] | 0.1742 | 58.56 | 0.78 | fla 111.8% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-float16] | 0.2016 | 1.33 | 0.08 | fla 66.3% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-bfloat16] | 0.2049 | 1.31 | 0.08 | fla 68.3% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-float16] | 0.3808 | 1.41 | 0.09 | fla 65.5% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-bfloat16] | 0.3876 | 1.39 | 0.09 | fla 66.7% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-float16] | 0.7235 | 1.48 | 0.09 | fla 67.3% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-bfloat16] | 0.7503 | 1.43 | 0.09 | fla 66.9% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-float16] | 1.4222 | 1.51 | 0.10 | fla 64.7% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-bfloat16] | 1.4642 | 1.47 | 0.09 | fla 65.1% | - |
| 🔵 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b1-h8-d128-bfloat16] | 0.0031 | 0.25 | 0.17 | fla 128.2% | - |
| 🔵 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b1-h16-d128-bfloat16] | 0.0033 | 0.48 | 0.32 | fla 127.2% | - |
| 🔵 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b1-h32-d128-bfloat16] | 0.0036 | 0.86 | 0.58 | fla 127.2% | - |
| 🔵 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b1-h48-d128-bfloat16] | 0.0039 | 1.22 | 0.83 | fla 135.5% | - |
| 🔵 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b1-h64-d128-bfloat16] | 0.0042 | 1.52 | 1.02 | fla 139.2% | - |
| 🟢 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b8-h32-d128-bfloat16] | 0.0087 | 2.90 | 1.96 | fla 167.7% | - |
| 🟢 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b8-h48-d128-bfloat16] | 0.0124 | 3.04 | 2.05 | fla 155.5% | - |
| 🟢 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b8-h64-d128-bfloat16] | 0.0161 | 3.14 | 2.12 | fla 156.3% | - |
| 🔴 | GatedDeltaNetPrefillBHTDFwdOp | test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-float16] | 0.2509 | 34.24 | 0.34 | fla 78.0% | - |
| 🔴 | GatedDeltaNetPrefillBHTDFwdOp | test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-bfloat16] | 0.2525 | 34.02 | 0.34 | fla 78.3% | - |
| 🟡 | GatedDeltaNetPrefillBHTDFwdOp | test_gated_deltanet_prefill_bhtd_bench[bhtd-qwen35-gdn-prefill-b1-s128k-h64-d128-float16] | 17.4375 | 63.05 | 0.62 | fla 89.6% | - |
| 🟡 | GatedDeltaNetPrefillBHTDFwdOp | test_gated_deltanet_prefill_bhtd_bench[bhtd-qwen35-gdn-prefill-b1-s128k-h64-d128-bfloat16] | 17.5462 | 62.66 | 0.61 | fla 88.8% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[fallback-gdn-prefill-b1-s4k-h16-d128-bthd-float16] | 0.0790 | 108.70 | 1.07 | fla 249.1% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[fallback-gdn-prefill-b1-s4k-h16-d128-bthd-bfloat16] | 0.0792 | 108.46 | 1.07 | fla 250.3% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h16-d128-bthd-float16] | 0.3660 | 187.77 | 1.84 | fla 400.4% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h16-d128-bthd-bfloat16] | 0.3719 | 184.76 | 1.81 | fla 394.7% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h16-d128-bthd-float16] | 0.6963 | 197.40 | 1.93 | fla 417.4% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h16-d128-bthd-bfloat16] | 0.7082 | 194.06 | 1.90 | fla 410.6% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h16-d128-bthd-float16] | 1.2557 | 218.90 | 2.14 | fla 459.2% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h16-d128-bthd-bfloat16] | 1.2816 | 214.48 | 2.10 | fla 450.5% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h32-d128-bthd-float16] | 0.6850 | 200.64 | 1.97 | fla 323.3% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h32-d128-bthd-bfloat16] | 0.6976 | 197.01 | 1.93 | fla 318.3% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h32-d128-bthd-float16] | 1.2486 | 220.16 | 2.16 | fla 352.0% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h32-d128-bthd-bfloat16] | 1.2807 | 214.63 | 2.10 | fla 343.8% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h32-d128-bthd-float16] | 2.4457 | 224.78 | 2.20 | fla 358.2% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h32-d128-bthd-bfloat16] | 2.5024 | 219.69 | 2.15 | fla 350.8% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h48-d128-bthd-float16] | 1.0508 | 196.20 | 1.92 | fla 301.5% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h48-d128-bthd-bfloat16] | 1.0656 | 193.46 | 1.90 | fla 296.6% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h48-d128-bthd-float16] | 1.9155 | 215.26 | 2.11 | fla 329.5% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h48-d128-bthd-bfloat16] | 1.9438 | 212.12 | 2.08 | fla 324.0% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h48-d128-bthd-float16] | 3.7677 | 218.87 | 2.14 | fla 334.4% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h48-d128-bthd-bfloat16] | 3.8160 | 216.10 | 2.12 | fla 329.8% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h64-d128-bthd-float16] | 1.2236 | 224.66 | 2.20 | fla 319.2% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h64-d128-bthd-bfloat16] | 1.2510 | 219.73 | 2.15 | fla 311.4% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h64-d128-bthd-float16] | 2.3782 | 231.16 | 2.27 | fla 328.1% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h64-d128-bthd-bfloat16] | 2.4277 | 226.45 | 2.22 | fla 321.1% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h64-d128-bthd-float16] | 4.6674 | 235.57 | 2.31 | fla 334.8% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h64-d128-bthd-bfloat16] | 4.7957 | 229.27 | 2.25 | fla 325.0% | - |
| 🔵 | GeFwdOp | test_comparison_bench[ge-1024x4096-float16-ge] | 0.0076 | 0.56 | 2.78 | torch 103.0%, torch-compile 103.4% | - |
| 🔵 | GeFwdOp | test_ge_manifest_bench[hidden-state-prefill-float16] | 0.0131 | 0.64 | 3.20 | torch 100.7%, torch-compile 100.7% | - |
| 🔵 | GeFwdOp | test_ge_manifest_bench[hidden-state-prefill-bfloat16] | 0.0130 | 0.65 | 3.23 | torch 100.7%, torch-compile 100.7% | - |
| 🟡 | GeFwdOp | test_ge_manifest_bench[hidden-state-prefill-float32] | 0.0224 | 0.37 | 3.37 | torch 99.7%, torch-compile 110.9% | - |
| 🔴 | GeFwdOp | test_ge_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.81 | 2.42 | torch 294.7%, torch-compile 74.4% | - |
| 🔴 | GeFwdOp | test_ge_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.81 | 2.42 | torch 299.6%, torch-compile 75.6% | - |
| 🟡 | GeFwdOp | test_ge_manifest_bench[cnn-feat-broadcast-float32] | 0.0207 | 0.62 | 3.10 | torch 226.5%, torch-compile 88.7% | - |
| 🔵 | GeluAndMulFwdOp | test_gelu_and_mul_bench[ffn-gelu-prefill-float16] | 0.0549 | 3.21 | 3.21 | flashinfer 191.0%, torch-ref 369.6%, torch-compile 109.5% | - |
| 🔵 | GeluAndMulFwdOp | test_gelu_and_mul_bench[ffn-gelu-prefill-bfloat16] | 0.0596 | 2.96 | 2.96 | flashinfer 178.2%, torch-ref 344.2%, torch-compile 102.9% | - |
| 🟡 | GeluAndMulFwdOp | test_gelu_and_mul_bench[ffn-gelu-decode-bfloat16] | 0.0016 | 0.05 | 0.05 | flashinfer 424.5%, torch-ref 204.2%, torch-compile 93.9% | - |
| 🟡 | GeluFwdOp | test_gelu_manifest_bench[llama-8b-ffn-prefill-float16] | 0.0526 | 2.79 | 2.23 | torch 90.9%, torch-compile 102.6% | - |
| 🟡 | GeluFwdOp | test_gelu_manifest_bench[llama-8b-ffn-prefill-bfloat16] | 0.0553 | 2.65 | 2.12 | torch 88.2%, torch-compile 101.1% | - |
| 🔵 | GeluFwdOp | test_gelu_manifest_bench[llama-8b-ffn-decode-bfloat16] | 0.0014 | 0.05 | 0.04 | torch 115.9%, torch-compile 102.3% | - |
| 🔵 | GeluTanhAndMulFwdOp | test_gelu_tanh_and_mul_bench[ffn-gelu-tanh-prefill-float16] | 0.0478 | 6.14 | 3.68 | flashinfer 118.4%, torch-ref 401.5%, torch-compile 108.1% | - |
| 🔵 | GeluTanhAndMulFwdOp | test_gelu_tanh_and_mul_bench[ffn-gelu-tanh-prefill-bfloat16] | 0.0495 | 5.93 | 3.56 | flashinfer 116.5%, torch-ref 390.9%, torch-compile 106.2% | - |
| 🟡 | GeluTanhAndMulFwdOp | test_gelu_tanh_and_mul_bench[ffn-gelu-tanh-decode-bfloat16] | 0.0015 | 0.09 | 0.06 | flashinfer 285.4%, torch-ref 198.9%, torch-compile 97.9% | - |
| 🟢 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-decode-gate-up-per-tensor-float8_e4m3fn] | 0.1161 | 33.37 | 0.14 | torch-scaled-mm 208.2% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-decode-down-per-tensor-float8_e4m3fn] | 0.0253 | 148.47 | 0.66 | torch-scaled-mm 967.0%, deepgemm 41.1% | - |
| 🟢 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-prefill-gate-up-per-tensor-float8_e4m3fn] | 0.5106 | 242.87 | 0.12 | torch-scaled-mm 675.8% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-prefill-down-per-tensor-float8_e4m3fn] | 0.2103 | 571.75 | 0.39 | torch-scaled-mm 1590.1%, deepgemm 50.0% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-decode-gate-up-block128-float8_e4m3fn] | 0.1483 | 26.14 | 0.12 | torch-scaled-mm 188.5%, flashinfer-fp8-blockscale-sm90 8.7% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-decode-down-block128-float8_e4m3fn] | 0.0379 | 99.27 | 0.46 | torch-scaled-mm 739.1%, flashinfer-fp8-blockscale-sm90 24.4% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-prefill-gate-up-block128-float8_e4m3fn] | 0.3852 | 321.94 | 0.16 | torch-scaled-mm 917.0%, flashinfer-fp8-blockscale-sm90 36.2% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-prefill-down-block128-float8_e4m3fn] | 0.4464 | 269.42 | 0.18 | torch-scaled-mm 761.0%, flashinfer-fp8-blockscale-sm90 32.1% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-prefill-attn-proj-block128-float8_e4m3fn] | 0.7705 | 312.17 | 0.12 | torch-scaled-mm 867.6%, flashinfer-fp8-blockscale-sm90 27.9% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[k-dominant-7168x16384-block128-float8_e4m3fn] | 3.5851 | 268.35 | 0.07 | torch-scaled-mm 735.2%, flashinfer-fp8-blockscale-sm90 21.6% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[wide-n-24576-block128-float8_e4m3fn] | 1.0285 | 300.68 | 0.24 | torch-scaled-mm 828.3%, flashinfer-fp8-blockscale-sm90 37.2% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[small-batch-down-m8-per-tensor-float8_e4m3fn] | 0.0268 | 8.77 | 0.55 | torch-scaled-mm 622.3%, deepgemm 31.0% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[gemv-down-m1-per-tensor-float8_e4m3fn] | 0.0259 | 1.14 | 0.57 | torch-scaled-mm 504.1%, deepgemm 39.2% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[gemv-down-m1-block128-float8_e4m3fn] | 0.0446 | 0.66 | 0.34 | torch-scaled-mm 368.7%, flashinfer-fp8-blockscale-sm90 17.4% | - |
| 🟢 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-decode-gate-up-per-tensor-bias-float8_e4m3fn] | 0.1167 | 33.22 | 0.14 | torch-scaled-mm 213.1% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[square-1k-nn-float16] | 0.0145 | 148.47 | 0.43 | torch-cublas 50.2%, flaggems 81.6% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[square-1k-nn-bfloat16] | 0.0145 | 148.47 | 0.43 | torch-cublas 49.8%, flaggems 79.0% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[ds-v3-decode-gate-up-bfloat16] | 0.0677 | 57.24 | 0.48 | torch-cublas 25.5%, deepgemm 31.4% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[ds-v3-decode-down-bfloat16] | 0.0247 | 152.32 | 1.29 | torch-cublas 53.4%, deepgemm 55.8% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[ds-v3-prefill-gate-up-bfloat16] | 0.3374 | 367.52 | 0.32 | torch-cublas 52.5%, deepgemm 53.6% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[ds-v3-prefill-down-bfloat16] | 0.3214 | 374.16 | 0.33 | torch-cublas 56.1%, deepgemm 55.9% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[ds-v3-prefill-attn-proj-float16] | 0.5417 | 444.01 | 0.28 | torch-cublas 62.1% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[ds-v3-prefill-attn-proj-bfloat16] | 0.5405 | 444.97 | 0.28 | torch-cublas 61.5%, deepgemm 61.0% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[k-dominant-7168x16384-bfloat16] | 2.0639 | 466.13 | 0.21 | torch-cublas 61.3%, deepgemm 61.3% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[wide-n-24576-bfloat16] | 0.8992 | 343.90 | 0.32 | torch-cublas 50.1%, deepgemm 49.4% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[mid-m16-attn-bfloat16] | 0.0658 | 14.27 | 0.90 | torch-cublas 37.2%, deepgemm 51.4% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[mid-m32-attn-bfloat16] | 0.0662 | 28.39 | 0.90 | torch-cublas 36.8%, deepgemm 46.2% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[mid-m64-down-bfloat16] | 0.0207 | 90.90 | 1.48 | torch-cublas 63.8%, deepgemm 65.3% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[mid-m96-gate-up-bfloat16] | 0.0688 | 42.26 | 0.47 | torch-cublas 24.5%, deepgemm 31.8% | - |
| 🔴 | GemmW4A16FwdOp | test_gemm_w4a16_bench[compile-smoke-square-64x64x128-float16] | 0.0043 | 0.25 | 0.01 | torch-dequantized-matmul 63.2% | - |
| 🔴 | GemmW4A16FwdOp | test_gemm_w4a16_bench[compile-smoke-rect-128x256x256-float16] | 0.0058 | 2.88 | 0.03 | torch-dequantized-matmul 52.8% | - |
| 🔴 | GemmW4A16FwdOp | test_gemm_w4a16_bench[decode-l2-resident-ish-float16] | 0.0329 | 4.08 | 1.10 | torch-dequantized-matmul 142.3%, marlin-fp32 66.6%, marlin-fp16 66.4% | - |
| 🔴 | GemmW4A16FwdOp | test_gemm_w4a16_bench[decode-hbm-streaming-threshold-float16] | 0.0610 | 4.40 | 1.19 | torch-dequantized-matmul 122.7%, marlin-fp32 62.1%, marlin-fp16 62.4% | - |
| 🔴 | GemmW4A16FwdOp | test_gemm_w4a16_bench[decode-non-power2-low-cta-float16] | 0.0743 | 3.95 | 1.07 | torch-dequantized-matmul 118.2%, marlin-fp32 54.9%, marlin-fp16 54.9% | - |
| 🔴 | GemmW4A16FwdOp | test_gemm_w4a16_bench[decode-long-k-pressure-float16] | 0.2835 | 4.73 | 1.28 | torch-dequantized-matmul 113.8%, marlin-fp32 49.8%, marlin-fp16 49.8% | - |
| 🔵 | GroupNormFwdOp | test_group_norm_bench[image-g32-affine-float16] | 0.0037 | 1.40 | 1.12 | flaggems 107.7%, torch 407.7%, torch-compile 132.5% | - |
| 🔵 | GroupNormFwdOp | test_group_norm_bench[image-g32-affine-bfloat16] | 0.0037 | 1.41 | 1.13 | flaggems 108.6%, torch 411.2%, torch-compile 135.4% | - |
| 🔴 | GroupNormFwdOp | test_group_norm_bench[wider-channel-g32-affine-float16] | 0.0060 | 0.67 | 0.54 | flaggems 66.7%, torch 273.1%, torch-compile 73.1% | - |
| 🔴 | GroupNormFwdOp | test_group_norm_bench[tail-spatial-g16-affine-float16] | 0.0060 | 0.38 | 0.30 | flaggems 67.2%, torch 253.4%, torch-compile 73.5% | - |
| 🔵 | GroupNormFwdOp | test_group_norm_no_affine_bench[image-g32-float16] | 0.0036 | 0.89 | 1.18 | flaggems 100.9%, torch 373.0%, torch-compile 123.4% | - |
| 🔵 | GroupNormFwdOp | test_group_norm_no_affine_bench[image-g32-bfloat16] | 0.0036 | 0.89 | 1.18 | flaggems 100.9%, torch 373.0%, torch-compile 119.0% | - |
| 🔴 | GroupNormFwdOp | test_group_norm_no_affine_bench[wider-channel-g32-float16] | 0.0048 | 0.50 | 0.67 | flaggems 72.7%, torch 295.3%, torch-compile 76.7% | - |
| 🔴 | GroupNormFwdOp | test_group_norm_no_affine_bench[tail-spatial-g16-float16] | 0.0052 | 0.27 | 0.35 | flaggems 69.3%, torch 257.7%, torch-compile 66.9% | - |
| 🟡 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-8b-short-float16] | 0.2031 | 105.75 | 0.33 | fa3 82.0% | - |
| 🔴 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-8b-short-bfloat16] | 0.4153 | 51.71 | 0.16 | fa3 39.8% | - |
| 🔴 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-8b-long-float16] | 0.8329 | 206.27 | 0.16 | fa3 71.1% | - |
| 🔴 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-8b-long-bfloat16] | 1.2411 | 138.42 | 0.11 | fa3 47.4% | - |
| 🟡 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-70b-short-float16] | 0.1962 | 109.46 | 0.30 | fa3 81.3% | - |
| 🔴 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-70b-short-bfloat16] | 0.4093 | 52.46 | 0.14 | fa3 38.8% | - |
| 🔴 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-70b-long-float16] | 0.8094 | 212.26 | 0.15 | fa3 71.7% | - |
| 🔴 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 1.0178 | 168.79 | 0.12 | fa3 56.8% | - |
| 🔴 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-8b-p64-float16] | 0.1668 | 12.88 | 0.10 | flashinfer 75.3% | - |
| 🔵 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-8b-long-p64-float16] | 0.2207 | 19.46 | 0.61 | flashinfer 135.6% | - |
| 🔴 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[throughput-8b-p64-float16] | 0.2516 | 8.54 | 0.04 | flashinfer 59.9% | - |
| 🟡 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-70b-p64-float16] | 0.0496 | 21.65 | 0.34 | flashinfer 89.7% | - |
| 🔴 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-8b-p256-float16] | 0.1686 | 12.74 | 0.10 | fa3 48.3%, flashinfer 74.1% | - |
| 🔴 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-70b-p256-float16] | 0.0684 | 15.69 | 0.25 | fa3 53.7%, flashinfer 83.5% | - |
| 🔴 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-405b-p256-float16] | 0.0563 | 19.07 | 0.30 | fa3 47.1% | - |
| 🔴 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-8b-p64-softcap50-float16] | 0.1766 | 12.16 | 0.10 | flashinfer 71.0% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-8b-4k-float16] | 0.1515 | 14.18 | 3.55 | fa3 101.5%, flashinfer 148.7% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-8b-4k-bfloat16] | 0.1500 | 14.31 | 3.58 | fa3 102.0%, flashinfer 172.0% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-8b-32k-float16] | 0.2577 | 16.67 | 4.17 | fa3 104.5%, flashinfer 167.2% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-8b-32k-bfloat16] | 0.2567 | 16.73 | 4.18 | fa3 104.4%, flashinfer 194.2% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-70b-4k-float16] | 0.0792 | 27.11 | 3.40 | fa3 107.7%, flashinfer 253.4% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-70b-4k-bfloat16] | 0.0790 | 27.18 | 3.40 | fa3 107.5%, flashinfer 286.8% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-70b-32k-float16] | 0.1379 | 31.14 | 3.89 | fa3 109.1%, flashinfer 280.7% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-70b-32k-bfloat16] | 0.1375 | 31.23 | 3.91 | fa3 108.5%, flashinfer 320.8% | - |
| 🟢 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-8b-4k-softcap50-float16] | 0.1621 | 13.24 | 3.31 | torch-sdpa 8217.7% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-1k-float16] | 0.0070 | 2.40 | 0.30 | fa3 248.9%, flashinfer 138.5% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-4k-float16] | 0.0096 | 6.97 | 0.87 | fa3 221.3%, flashinfer 120.6% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-8k-float16] | 0.0131 | 10.23 | 1.28 | fa3 177.1%, flashinfer 107.6% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-16k-float16] | 0.0182 | 14.77 | 1.85 | fa3 153.9%, flashinfer 120.4% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-32k-float16] | 0.0283 | 18.96 | 2.37 | fa3 132.9%, flashinfer 122.4% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-64k-float16] | 0.0455 | 23.59 | 2.95 | fa3 126.5%, flashinfer 116.7% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-128k-float16] | 0.0764 | 28.10 | 3.51 | fa3 121.5%, flashinfer 109.0% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-256k-float16] | 0.1360 | 31.58 | 3.95 | fa3 118.7%, flashinfer 104.3% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-8b-short-float16] | 0.0370 | 232.41 | 1.13 | fa3 86.6%, flashinfer 106.7% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-8b-short-bfloat16] | 0.0369 | 233.02 | 1.14 | fa3 86.4%, flashinfer 106.7% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-8b-long-float16] | 0.1622 | 423.73 | 0.52 | fa3 82.8%, flashinfer 99.7% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-8b-long-bfloat16] | 0.1616 | 425.12 | 0.52 | fa3 82.6%, flashinfer 99.5% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-70b-short-float16] | 0.0381 | 225.58 | 0.99 | fa3 83.6%, flashinfer 102.6% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-70b-short-bfloat16] | 0.0380 | 225.77 | 0.99 | fa3 83.6%, flashinfer 102.7% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-70b-long-float16] | 0.1631 | 421.45 | 0.46 | fa3 82.3%, flashinfer 99.4% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-70b-long-bfloat16] | 0.1614 | 425.83 | 0.47 | fa3 81.9%, flashinfer 99.0% | - |
| 🔵 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-8b-prefill-dense-float16] | 0.0371 | 232.26 | 1.13 | torch-ref 2968.2%, flashinfer 106.7% | - |
| 🔵 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-8b-prefill-dense-bfloat16] | 0.0369 | 233.07 | 1.14 | torch-ref 2980.3%, flashinfer 106.2% | - |
| 🔵 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-8b-prefill-dense-sm-scale-0.125-float16] | 0.0370 | 232.46 | 1.13 | torch-ref 2970.2%, flashinfer 106.5% | - |
| 🔵 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-8b-prefill-dense-softcap50-float16] | 0.0420 | 205.00 | 1.00 | torch-ref 3083.6%, flashinfer 109.1% | - |
| 🔵 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-8b-prefill-dense-q-lt-kv-float16] | 0.1261 | 510.92 | 0.40 | torch-ref 3248.2%, flashinfer 100.4% | - |
| 🔵 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-8b-prefill-dense-q-lt-kv-bfloat16] | 0.1243 | 518.28 | 0.40 | torch-ref 3297.8%, flashinfer 100.7% | - |
| 🔵 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-70b-prefill-dense-q-lt-kv-float16] | 0.1251 | 515.10 | 0.27 | torch-ref 3004.6%, flashinfer 100.0% | - |
| 🟡 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-70b-prefill-dense-q-lt-kv-bfloat16] | 0.1243 | 518.48 | 0.27 | torch-ref 3032.4%, flashinfer 99.9% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s896-float16] | 0.0454 | 289.67 | 0.20 | torch-sdpa-dequant 202.9%, fa3 62.7% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s896-bfloat16] | 0.0453 | 290.39 | 0.20 | torch-sdpa-dequant 204.2%, fa3 62.9% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s1792-float16] | 0.1288 | 408.54 | 0.14 | torch-sdpa-dequant 176.3%, fa3 66.7% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s1792-bfloat16] | 0.1289 | 408.19 | 0.14 | torch-sdpa-dequant 175.0%, fa3 66.6% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s3584-float16] | 0.7504 | 560.88 | 0.09 | torch-sdpa-dequant 140.5%, fa3 70.6% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s3584-bfloat16] | 0.7495 | 561.60 | 0.09 | torch-sdpa-dequant 140.7%, fa3 70.7% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s7168-float16] | 2.8432 | 592.16 | 0.05 | torch-sdpa-dequant 120.7%, fa3 71.2% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s7168-bfloat16] | 2.8474 | 591.28 | 0.05 | torch-sdpa-dequant 120.6%, fa3 71.1% | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-prefill-paged-fullattn-b8-prefix32k-chunk1k-p64-partial-rope64-float16] | 60.5759 | 147.48 | 0.04 | - | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-prefill-paged-fullattn-mixed-b8-p64-partial-rope64-float16] | 30.7285 | 108.01 | 0.04 | - | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-prefill-paged-b8-prefix4k-chunk512-p64-full-rope-float16] | 1.9536 | 149.52 | 0.12 | - | - |
| 🟡 | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[gqa-prefill-paged-softcap50-b4-prefix4k-chunk512-p64-float16] | 0.1501 | 121.64 | 0.10 | fa3 91.0% | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-prefill-paged-fp8-cache-b8-prefix32k-chunk1k-p64-float16] | 56.0061 | 159.51 | 0.05 | - | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-prefill-paged-fp8-cache-b8-prefix4k-chunk512-p64-float16] | 2.0009 | 145.98 | 0.12 | - | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[gqa-prefill-paged-fp8-cache-softcap50-b4-prefix4k-chunk512-p64-float16] | 0.2069 | 88.22 | 0.07 | - | - |
| 🔴 | GroupedQueryAttentionPrefillVarlenFwdOp | test_gqa_prefill_varlen_fwd_bench[llama-8b-prefill-varlen-uniform-fp16] | 0.1249 | 206.52 | 0.40 | torch-ref 1632.8%, fa3 57.0% | - |
| 🔴 | GroupedQueryAttentionPrefillVarlenFwdOp | test_gqa_prefill_varlen_fwd_bench[llama-8b-prefill-varlen-mixed-fp16] | 0.1404 | 143.50 | 0.28 | torch-ref 1192.5%, fa3 44.1% | - |
| 🔴 | GroupedQueryAttentionPrefillVarlenFwdOp | test_gqa_prefill_varlen_fwd_bench[llama-70b-prefill-varlen-q-lt-kv-bf16] | 0.1960 | 219.18 | 0.24 | torch-ref 1409.8%, fa3 50.6% | - |
| 🟡 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-8b-short-w256-float16] | 0.0398 | 162.34 | 1.05 | fa3 85.9%, flashinfer 103.2% | - |
| 🟡 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0398 | 162.47 | 1.05 | fa3 85.6%, flashinfer 103.0% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-8b-long-w1024-float16] | 0.1529 | 337.35 | 0.55 | fa3 79.1%, flashinfer 101.5% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.1516 | 340.27 | 0.55 | fa3 78.1%, flashinfer 100.5% | - |
| 🟡 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-70b-short-w256-float16] | 0.0396 | 163.39 | 0.95 | fa3 86.2%, flashinfer 103.6% | - |
| 🟡 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-70b-short-w256-bfloat16] | 0.0394 | 164.19 | 0.96 | fa3 86.5%, flashinfer 104.3% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-70b-long-w1024-float16] | 0.1528 | 337.63 | 0.49 | fa3 78.6%, flashinfer 101.1% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.1512 | 341.10 | 0.50 | fa3 78.2%, flashinfer 99.9% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-float16] | 0.0571 | 113.36 | 0.74 | fa3 82.7%, flashinfer 72.3% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0569 | 113.74 | 0.74 | fa3 82.8%, flashinfer 72.4% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-float16] | 0.3518 | 293.26 | 0.48 | fa3 77.3%, flashinfer 78.5% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.3495 | 295.19 | 0.48 | fa3 77.1%, flashinfer 78.1% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-float16] | 0.0935 | 138.39 | 0.81 | fa3 89.4%, flashinfer 73.8% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-bfloat16] | 0.0930 | 139.10 | 0.81 | fa3 89.4%, flashinfer 74.1% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-float16] | 0.6682 | 308.83 | 0.45 | fa3 79.1%, flashinfer 78.0% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.6662 | 309.76 | 0.45 | fa3 79.1%, flashinfer 77.7% | - |
| 🔵 | GtFwdOp | test_comparison_bench[gt-1024x4096-float16-gt] | 0.0076 | 0.55 | 2.75 | torch 102.5%, torch-compile 102.3% | - |
| 🔵 | GtFwdOp | test_gt_manifest_bench[hidden-state-prefill-float16] | 0.0130 | 0.65 | 3.23 | torch 101.7%, torch-compile 101.2% | - |
| 🔵 | GtFwdOp | test_gt_manifest_bench[hidden-state-prefill-bfloat16] | 0.0130 | 0.64 | 3.22 | torch 101.0%, torch-compile 100.7% | - |
| 🟡 | GtFwdOp | test_gt_manifest_bench[hidden-state-prefill-float32] | 0.0223 | 0.38 | 3.38 | torch 100.0%, torch-compile 99.9% | - |
| 🔴 | GtFwdOp | test_gt_manifest_bench[cnn-feat-broadcast-float16] | 0.0160 | 0.80 | 2.41 | torch 303.6%, torch-compile 74.8% | - |
| 🔴 | GtFwdOp | test_gt_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.81 | 2.42 | torch 308.4%, torch-compile 75.5% | - |
| 🟡 | GtFwdOp | test_gt_manifest_bench[cnn-feat-broadcast-float32] | 0.0209 | 0.61 | 3.07 | torch 229.6%, torch-compile 87.9% | - |
| 🟡 | HardsigmoidFwdOp | test_hardsigmoid_manifest_bench[mbv3-se-gate-float16] | 0.0016 | 0.01 | 0.02 | torch 105.9%, torch-compile 83.3% | - |
| 🟡 | HardsigmoidFwdOp | test_hardsigmoid_manifest_bench[mbv3-se-gate-bfloat16] | 0.0016 | 0.01 | 0.02 | torch 105.8%, torch-compile 82.3% | - |
| 🟡 | HardsigmoidFwdOp | test_hardsigmoid_manifest_bench[mbv3-se-gate-deep-float16] | 0.0017 | 0.06 | 0.07 | torch 90.3%, torch-compile 90.3% | - |
| 🟡 | HardsigmoidFwdOp | test_hardsigmoid_manifest_bench[mbv3-se-gate-deep-bfloat16] | 0.0017 | 0.05 | 0.07 | torch 86.8%, torch-compile 88.7% | - |
| 🟡 | HardswishFwdOp | test_hardswish_manifest_bench[mbv3-stage2-float16] | 0.0129 | 3.00 | 3.00 | torch 90.0%, torch-compile 89.5% | - |
| 🟡 | HardswishFwdOp | test_hardswish_manifest_bench[mbv3-stage2-bfloat16] | 0.0132 | 2.92 | 2.92 | torch 87.9%, torch-compile 87.2% | - |
| 🟡 | HardswishFwdOp | test_hardswish_manifest_bench[mbv3-stage3-float16] | 0.0089 | 2.72 | 2.72 | torch 91.7%, torch-compile 90.6% | - |
| 🟡 | HardswishFwdOp | test_hardswish_manifest_bench[mbv3-stage3-bfloat16] | 0.0090 | 2.67 | 2.67 | torch 90.4%, torch-compile 142.9% | - |
| 🔵 | HardtanhFwdOp | test_hardtanh_manifest_bench[bounded-hidden-float16] | 0.0103 | 0.81 | 3.25 | torch 109.3%, torch-compile 100.6% | - |
| 🔵 | HardtanhFwdOp | test_hardtanh_manifest_bench[bounded-hidden-bfloat16] | 0.0104 | 0.81 | 3.24 | torch 103.1%, torch-compile 100.9% | - |
| 🔵 | HardtanhFwdOp | test_hardtanh_manifest_bench[bounded-conv-feat-float16] | 0.0146 | 0.88 | 3.52 | torch 111.0%, torch-compile 100.4% | - |
| 🔵 | HardtanhFwdOp | test_hardtanh_manifest_bench[bounded-conv-feat-bfloat16] | 0.0146 | 0.88 | 3.52 | torch 104.2%, torch-compile 101.3% | - |
| 🔵 | InfNormFwdOp | test_inf_norm_bench[hidden-state-inf-float16] | 0.0073 | 2.29 | 2.29 | flaggems 104.8%, torch 679.9%, torch-compile 145.0% | - |
| 🔵 | InfNormFwdOp | test_inf_norm_bench[hidden-state-inf-bfloat16] | 0.0074 | 2.28 | 2.28 | flaggems 107.0%, torch 680.9%, torch-compile 150.4% | - |
| 🔵 | InfNormFwdOp | test_inf_norm_bench[long-seq-inf-bfloat16] | 0.0040 | 1.05 | 1.05 | flaggems 344.0%, torch 432.8%, torch-compile 125.6% | - |
| 🔴 | InfNormFwdOp | test_inf_norm_bench[3d-multidim-reduce-float16] | 0.0112 | 0.37 | 0.37 | flaggems 113.4%, torch 171.5%, torch-compile 44.2% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[image-affine-float16] | 0.0035 | 1.52 | 1.21 | flaggems 107.4%, torch 600.0%, torch-compile 88.9% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[image-affine-bfloat16] | 0.0034 | 1.53 | 1.23 | flaggems 108.4%, torch 604.7%, torch-compile 87.8% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[wider-channel-affine-float16] | 0.0035 | 1.16 | 0.93 | flaggems 102.8%, torch 596.3%, torch-compile 83.3% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[tail-spatial-affine-float16] | 0.0027 | 0.43 | 0.35 | flaggems 106.0%, torch 416.9%, torch-compile 90.4% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[image-float16] | 0.0034 | 0.94 | 1.25 | flaggems 102.8%, torch 505.6%, torch-compile 87.6% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[image-bfloat16] | 0.0034 | 0.93 | 1.24 | flaggems 101.9%, torch 502.8%, torch-compile 85.9% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[wider-channel-float16] | 0.0033 | 0.72 | 0.96 | flaggems 99.0%, torch 485.6%, torch-compile 82.7% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[tail-spatial-float16] | 0.0025 | 0.27 | 0.36 | flaggems 103.8%, torch 326.6%, torch-compile 91.1% | - |
| 🔵 | IsfiniteFwdOp | test_isfinite_bench[elementwise-16M-float16] | 0.0147 | 1.14 | 3.43 | torch 429.5%, torch-compile 102.4% | - |
| 🔵 | IsfiniteFwdOp | test_isfinite_bench[elementwise-16M-bfloat16] | 0.0147 | 1.14 | 3.43 | torch 431.8%, torch-compile 102.4% | - |
| 🟡 | IsfiniteFwdOp | test_isfinite_bench[elementwise-16M-float32] | 0.0234 | 0.72 | 3.58 | torch 410.9%, torch-compile 99.7% | - |
| 🔵 | IsfiniteFwdOp | test_isfinite_bench[elementwise-256M-float16] | 0.1862 | 1.44 | 4.32 | torch 490.0%, torch-compile 105.5% | - |
| 🔵 | IsfiniteFwdOp | test_isfinite_bench[elementwise-256M-bfloat16] | 0.1862 | 1.44 | 4.32 | torch 491.4%, torch-compile 105.8% | - |
| 🔵 | IsinfFwdOp | test_isinf_bench[elementwise-16M-float16] | 0.0148 | 1.14 | 3.41 | torch 212.5%, torch-compile 102.6% | - |
| 🔵 | IsinfFwdOp | test_isinf_bench[elementwise-16M-bfloat16] | 0.0148 | 1.14 | 3.41 | torch 213.0%, torch-compile 102.9% | - |
| 🟡 | IsinfFwdOp | test_isinf_bench[elementwise-16M-float32] | 0.0234 | 0.72 | 3.58 | torch 243.8%, torch-compile 99.7% | - |
| 🔵 | IsinfFwdOp | test_isinf_bench[elementwise-256M-float16] | 0.1862 | 1.44 | 4.32 | torch 241.8%, torch-compile 106.7% | - |
| 🔵 | IsinfFwdOp | test_isinf_bench[elementwise-256M-bfloat16] | 0.1858 | 1.44 | 4.33 | torch 242.7%, torch-compile 107.7% | - |
| 🔵 | IsnanFwdOp | test_isnan_bench[elementwise-16M-float16] | 0.0147 | 1.14 | 3.42 | torch 104.4%, torch-compile 102.4% | - |
| 🔵 | IsnanFwdOp | test_isnan_bench[elementwise-16M-bfloat16] | 0.0147 | 1.14 | 3.42 | torch 105.4%, torch-compile 102.8% | - |
| 🟡 | IsnanFwdOp | test_isnan_bench[elementwise-16M-float32] | 0.0235 | 0.72 | 3.58 | torch 99.9%, torch-compile 99.7% | - |
| 🔵 | IsnanFwdOp | test_isnan_bench[elementwise-256M-float16] | 0.1861 | 1.44 | 4.33 | torch 108.3%, torch-compile 106.0% | - |
| 🔵 | IsnanFwdOp | test_isnan_bench[elementwise-256M-bfloat16] | 0.1862 | 1.44 | 4.32 | torch 109.5%, torch-compile 106.6% | - |
| 🔵 | L1NormFwdOp | test_l1_norm_bench[hidden-state-l1-float16] | 0.0074 | 2.28 | 2.28 | flaggems 204.3%, torch 671.1%, torch-compile 113.5% | - |
| 🔵 | L1NormFwdOp | test_l1_norm_bench[hidden-state-l1-bfloat16] | 0.0073 | 2.29 | 2.29 | flaggems 210.0%, torch 680.6%, torch-compile 114.9% | - |
| 🔵 | L1NormFwdOp | test_l1_norm_bench[long-seq-l1-bfloat16] | 0.0039 | 1.07 | 1.07 | flaggems 944.3%, torch 432.8%, torch-compile 120.5% | - |
| 🔴 | L1NormFwdOp | test_l1_norm_bench[3d-multidim-reduce-float16] | 0.0113 | 0.37 | 0.37 | flaggems 217.6%, torch 170.8%, torch-compile 40.5% | - |
| 🔵 | L2NormFwdOp | test_l2_norm_bench[hidden-state-l2-float16] | 0.0074 | 2.26 | 2.26 | flaggems 106.0%, torch 668.1%, torch-compile 116.8% | - |
| 🔵 | L2NormFwdOp | test_l2_norm_bench[hidden-state-l2-bfloat16] | 0.0074 | 2.26 | 2.26 | flaggems 105.6%, torch 671.5%, torch-compile 118.3% | - |
| 🔵 | L2NormFwdOp | test_l2_norm_bench[long-seq-l2-bfloat16] | 0.0040 | 1.05 | 1.05 | flaggems 339.2%, torch 424.0%, torch-compile 112.0% | - |
| 🔴 | L2NormFwdOp | test_l2_norm_bench[3d-multidim-reduce-float16] | 0.0113 | 0.37 | 0.37 | flaggems 119.2%, torch 170.3%, torch-compile 40.8% | - |
| 🟡 | LayerNormFwdOp | test_layer_norm_bench[llama-8b-prefill-float16] | 0.0137 | 3.06 | 2.45 | flaggems 95.8%, flashinfer 155.6%, torch 154.4%, torch-compile 168.9% | - |
| 🟡 | LayerNormFwdOp | test_layer_norm_bench[llama-8b-prefill-bfloat16] | 0.0149 | 2.81 | 2.25 | flaggems 92.4%, flashinfer 143.1%, torch 142.9%, torch-compile 164.6% | - |
| 🟡 | LayerNormFwdOp | test_layer_norm_bench[llama-8b-decode-bfloat16] | 0.0028 | 0.01 | 0.01 | flaggems 101.2%, flashinfer 110.5%, torch 404.6%, torch-compile 98.8% | - |
| 🟡 | LayerNormFwdOp | test_layer_norm_bench[llama-70b-prefill-float16] | 0.0260 | 3.22 | 2.58 | flaggems 99.1%, flashinfer 178.8%, torch 154.1%, torch-compile 118.0% | - |
| 🔵 | LayerNormFwdOp | test_layer_norm_bench[llama-70b-prefill-bfloat16] | 0.0265 | 3.17 | 2.54 | flaggems 104.6%, flashinfer 175.9%, torch 152.6%, torch-compile 126.2% | - |
| 🔵 | LayerNormFwdOp | test_layer_norm_bench[llama-70b-decode-bfloat16] | 0.0034 | 0.01 | 0.02 | flaggems 122.8%, flashinfer 119.1%, torch 580.5%, torch-compile 107.4% | - |
| 🟡 | LayerNormFwdOp | test_layer_norm_bench[llama-405b-prefill-float16] | 0.0502 | 3.34 | 2.67 | flaggems 96.2%, flashinfer 156.1%, torch 146.8%, torch-compile 93.1% | - |
| 🟡 | LayerNormFwdOp | test_layer_norm_bench[llama-405b-prefill-bfloat16] | 0.0509 | 3.30 | 2.64 | flaggems 99.2%, flashinfer 154.1%, torch 146.4%, torch-compile 99.5% | - |
| 🔵 | LayerNormFwdOp | test_layer_norm_bench[llama-405b-decode-bfloat16] | 0.0043 | 0.02 | 0.03 | flaggems 142.2%, flashinfer 140.7%, torch 884.4%, torch-compile 128.4% | - |
| 🔵 | LeFwdOp | test_comparison_bench[le-1024x4096-float16-le] | 0.0076 | 0.55 | 2.77 | torch 102.1%, torch-compile 101.7% | - |
| 🟡 | LeFwdOp | test_le_manifest_bench[hidden-state-prefill-float16] | 0.0130 | 0.65 | 3.23 | torch 99.6%, torch-compile 99.9% | - |
| 🔵 | LeFwdOp | test_le_manifest_bench[hidden-state-prefill-bfloat16] | 0.0131 | 0.64 | 3.20 | torch 100.5%, torch-compile 100.5% | - |
| 🟡 | LeFwdOp | test_le_manifest_bench[hidden-state-prefill-float32] | 0.0225 | 0.37 | 3.36 | torch 100.1%, torch-compile 99.7% | - |
| 🔴 | LeFwdOp | test_le_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.81 | 2.42 | torch 311.2%, torch-compile 74.5% | - |
| 🔴 | LeFwdOp | test_le_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.81 | 2.42 | torch 317.1%, torch-compile 74.5% | - |
| 🟡 | LeFwdOp | test_le_manifest_bench[cnn-feat-broadcast-float32] | 0.0209 | 0.62 | 3.08 | torch 235.4%, torch-compile 88.8% | - |
| 🔵 | LeakyReluFwdOp | test_leaky_relu_manifest_bench[gan-feat-float16] | 0.0184 | 1.82 | 3.65 | torch 100.2%, torch-compile 100.2% | - |
| 🔵 | LeakyReluFwdOp | test_leaky_relu_manifest_bench[gan-feat-bfloat16] | 0.0184 | 1.82 | 3.64 | torch 100.2%, torch-compile 100.0% | - |
| 🔵 | LeakyReluFwdOp | test_leaky_relu_manifest_bench[gan-feat-deep-float16] | 0.0103 | 1.62 | 3.25 | torch 100.6%, torch-compile 100.3% | - |
| 🔵 | LeakyReluFwdOp | test_leaky_relu_manifest_bench[gan-feat-deep-bfloat16] | 0.0103 | 1.62 | 3.25 | torch 100.3%, torch-compile 100.3% | - |
| 🔵 | LerpFwdOp | test_binary_arith_bench[lerp-1024x4096-float16-float16-LerpFwdOp-<lambda>-normal] | 0.0082 | 0.51 | 3.08 | torch 101.2%, torch-compile 100.0% | - |
| 🔵 | LerpFwdOp | test_binary_arith_bench[lerp-1024x10240-float16-float16-LerpFwdOp-<lambda>-normal] | 0.0176 | 0.59 | 3.57 | torch 100.5%, torch-compile 100.2% | - |
| 🔵 | LerpFwdOp | test_lerp_manifest_bench[hidden-state-prefill-float16] | 0.0148 | 1.71 | 3.41 | torch 100.4%, torch-compile 100.2% | - |
| 🔵 | LerpFwdOp | test_lerp_manifest_bench[hidden-state-prefill-bfloat16] | 0.0146 | 1.73 | 3.46 | torch 100.7%, torch-compile 100.0% | - |
| 🟡 | LerpFwdOp | test_lerp_manifest_bench[hidden-state-prefill-float32] | 0.0263 | 0.96 | 3.82 | torch 99.5%, torch-compile 99.5% | - |
| 🟡 | LerpFwdOp | test_lerp_manifest_bench[cnn-feat-broadcast-float16] | 0.0144 | 2.68 | 3.57 | torch 331.3%, torch-compile 99.9% | - |
| 🔵 | LerpFwdOp | test_lerp_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0143 | 2.69 | 3.58 | torch 336.4%, torch-compile 100.0% | - |
| 🟡 | LerpFwdOp | test_lerp_manifest_bench[cnn-feat-broadcast-float32] | 0.0266 | 1.45 | 3.86 | torch 191.2%, torch-compile 99.6% | - |
| 🟡 | LerpTensorFwdOp | test_lerp_tensor_manifest_bench[elementwise-16M-float16] | 0.0350 | 1.44 | 3.83 | torch 99.5%, torch-compile 99.3% | - |
| 🟡 | LerpTensorFwdOp | test_lerp_tensor_manifest_bench[elementwise-16M-bfloat16] | 0.0350 | 1.44 | 3.84 | torch 99.5%, torch-compile 99.3% | - |
| 🟡 | LerpTensorFwdOp | test_lerp_tensor_manifest_bench[elementwise-16M-float32] | 0.0656 | 0.77 | 4.09 | torch 99.2%, torch-compile 99.5% | - |
| 🔵 | LerpTensorFwdOp | test_lerp_tensor_manifest_bench[elementwise-256M-float16] | 0.4859 | 1.66 | 4.42 | torch 100.0%, torch-compile 100.0% | - |
| 🔵 | LerpTensorFwdOp | test_lerp_tensor_manifest_bench[elementwise-256M-bfloat16] | 0.4859 | 1.66 | 4.42 | torch 100.0%, torch-compile 100.1% | - |
| 🔵 | Log1pFwdOp | test_log1p_bench[elementwise-16M-float16] | 0.0181 | 1.85 | 3.70 | torch 144.6%, torch-compile 140.9% | - |
| 🔵 | Log1pFwdOp | test_log1p_bench[elementwise-16M-bfloat16] | 0.0181 | 1.85 | 3.70 | torch 148.0%, torch-compile 145.0% | - |
| 🟡 | Log1pFwdOp | test_log1p_bench[elementwise-16M-float32] | 0.0351 | 0.95 | 3.82 | torch 96.6%, torch-compile 96.6% | - |
| 🔵 | Log1pFwdOp | test_log1p_bench[elementwise-256M-float16] | 0.2540 | 2.11 | 4.23 | torch 149.6%, torch-compile 145.2% | - |
| 🟢 | Log1pFwdOp | test_log1p_bench[elementwise-256M-bfloat16] | 0.2548 | 2.11 | 4.21 | torch 152.2%, torch-compile 150.3% | - |
| 🟢 | LogFwdOp | test_log_bench[elementwise-16M-float16] | 0.0181 | 0.92 | 3.70 | torch 150.1%, torch-compile 150.8% | - |
| 🟢 | LogFwdOp | test_log_bench[elementwise-16M-bfloat16] | 0.0181 | 0.92 | 3.70 | torch 155.4%, torch-compile 154.1% | - |
| 🟡 | LogFwdOp | test_log_bench[elementwise-16M-float32] | 0.0357 | 0.47 | 3.76 | torch 96.0%, torch-compile 95.7% | - |
| 🟢 | LogFwdOp | test_log_bench[elementwise-256M-float16] | 0.2537 | 1.06 | 4.23 | torch 156.5%, torch-compile 158.0% | - |
| 🟢 | LogFwdOp | test_log_bench[elementwise-256M-bfloat16] | 0.2545 | 1.05 | 4.22 | torch 162.2%, torch-compile 161.1% | - |
| 🟢 | LogSoftmaxFwdOp | test_log_softmax_bench[attn-weights-4k-float16] | 0.0090 | 2.33 | 1.86 | flaggems 221.3%, torch 190.8%, torch-compile 165.5% | - |
| 🟢 | LogSoftmaxFwdOp | test_log_softmax_bench[attn-weights-4k-bfloat16] | 0.0088 | 2.37 | 1.90 | flaggems 231.5%, torch 194.0%, torch-compile 174.3% | - |
| 🔵 | LogSoftmaxFwdOp | test_log_softmax_bench[attn-weights-4k-float32] | 0.0115 | 1.83 | 2.92 | flaggems 178.8%, torch 161.3%, torch-compile 137.9% | - |
| 🔵 | LogSoftmaxFwdOp | test_log_softmax_bench[attn-weights-32k-bfloat16] | 0.0570 | 2.94 | 2.35 | flaggems 439.0%, torch 107.5%, torch-compile 124.9% | - |
| 🔴 | LogSoftmaxFwdOp | test_log_softmax_bench[lm-head-logits-float16] | 0.0249 | 0.08 | 0.07 | flaggems 1690.7%, torch 88.9%, torch-compile 38.9% | - |
| 🔴 | LogSoftmaxFwdOp | test_log_softmax_bench[lm-head-logits-bfloat16] | 0.0261 | 0.08 | 0.06 | flaggems 1611.9%, torch 87.6%, torch-compile 37.0% | - |
| 🔴 | LogSoftmaxFwdOp | test_log_softmax_bench[lm-head-logits-float32] | 0.0320 | 0.06 | 0.10 | flaggems 1261.5%, torch 110.0%, torch-compile 30.9% | - |
| 🔵 | LogSumExpFwdOp | test_logsumexp_bench[attn-weights-4k-float16] | 0.0074 | 2.26 | 1.13 | torch 656.4%, torch-compile 131.9% | - |
| 🔵 | LogSumExpFwdOp | test_logsumexp_bench[attn-weights-4k-bfloat16] | 0.0075 | 2.25 | 1.13 | torch 664.4%, torch-compile 134.8% | - |
| 🔵 | LogSumExpFwdOp | test_logsumexp_bench[attn-weights-32k-bfloat16] | 0.0374 | 3.59 | 1.79 | torch 528.2%, torch-compile 110.9% | - |
| 🔴 | LogSumExpFwdOp | test_logsumexp_bench[lm-head-logits-float16] | 0.0141 | 0.12 | 0.06 | torch 327.9%, torch-compile 76.9% | - |
| 🔴 | LogSumExpFwdOp | test_logsumexp_bench[lm-head-logits-bfloat16] | 0.0164 | 0.10 | 0.05 | torch 285.4%, torch-compile 64.1% | - |
| 🔴 | LogSumExpFwdOp | test_logsumexp_bench[3d-multidim-reduce-float16] | 0.0126 | 0.67 | 0.33 | torch 327.5%, torch-compile 78.6% | - |
| 🔵 | LogicalAndFwdOp | test_logical_bench[logical_and-1024x4096-float16-LogicalAndFwdOp-logical_and] | 0.0075 | 0.56 | 2.81 | torch 103.4%, torch-compile 103.0% | - |
| 🔵 | LogicalAndFwdOp | test_logical_bench[logical_and-1024x10240-float16-LogicalAndFwdOp-logical_and] | 0.0157 | 0.67 | 3.33 | torch 102.1%, torch-compile 101.8% | - |
| 🔵 | LogicalAndFwdOp | test_logical_and_manifest_bench[hidden-state-prefill-bool] | 0.0082 | 3.06 | 3.06 | torch 123.0%, torch-compile 107.8% | - |
| 🔵 | LogicalAndFwdOp | test_logical_and_manifest_bench[hidden-state-prefill-float16] | 0.0132 | 1.91 | 3.18 | torch 101.7%, torch-compile 101.2% | - |
| 🔵 | LogicalAndFwdOp | test_logical_and_manifest_bench[hidden-state-prefill-bfloat16] | 0.0129 | 1.95 | 3.25 | torch 101.0%, torch-compile 101.5% | - |
| 🔵 | LogicalAndFwdOp | test_logical_and_manifest_bench[hidden-state-prefill-float32] | 0.0225 | 1.12 | 3.36 | torch 100.0%, torch-compile 100.0% | - |
| 🔵 | LogicalAndFwdOp | test_logical_and_manifest_bench[cnn-feat-broadcast-bool] | 0.0080 | 4.80 | 3.20 | torch 562.5%, torch-compile 123.9% | - |
| 🔴 | LogicalAndFwdOp | test_logical_and_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 2.42 | 2.42 | torch 294.7%, torch-compile 76.3% | - |
| 🔴 | LogicalAndFwdOp | test_logical_and_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 2.42 | 2.42 | torch 301.6%, torch-compile 75.2% | - |
| 🟡 | LogicalAndFwdOp | test_logical_and_manifest_bench[cnn-feat-broadcast-float32] | 0.0208 | 1.86 | 3.09 | torch 223.9%, torch-compile 88.1% | - |
| 🔵 | LogicalNotFwdOp | test_logical_not_bench[elementwise-16M-bool] | 0.0101 | 1.66 | 3.32 | torch 128.5%, torch-compile 119.3% | - |
| 🔵 | LogicalNotFwdOp | test_logical_not_bench[elementwise-16M-float16] | 0.0147 | 1.14 | 3.43 | torch 103.5%, torch-compile 102.2% | - |
| 🟡 | LogicalNotFwdOp | test_logical_not_bench[elementwise-16M-float32] | 0.0235 | 0.71 | 3.57 | torch 99.7%, torch-compile 99.4% | - |
| 🔵 | LogicalNotFwdOp | test_logical_not_bench[elementwise-256M-bool] | 0.1264 | 2.12 | 4.25 | torch 143.8%, torch-compile 130.4% | - |
| 🔵 | LogicalOrFwdOp | test_logical_bench[logical_or-1024x4096-float16-LogicalOrFwdOp-logical_or] | 0.0075 | 0.56 | 2.80 | torch 102.1%, torch-compile 101.7% | - |
| 🔵 | LogicalOrFwdOp | test_logical_bench[logical_or-1024x10240-float16-LogicalOrFwdOp-logical_or] | 0.0158 | 0.66 | 3.31 | torch 101.6%, torch-compile 101.4% | - |
| 🔵 | LogicalOrFwdOp | test_logical_or_manifest_bench[hidden-state-prefill-bool] | 0.0082 | 3.07 | 3.07 | torch 110.9%, torch-compile 108.2% | - |
| 🔵 | LogicalOrFwdOp | test_logical_or_manifest_bench[hidden-state-prefill-float16] | 0.0132 | 1.91 | 3.18 | torch 100.8%, torch-compile 100.7% | - |
| 🔵 | LogicalOrFwdOp | test_logical_or_manifest_bench[hidden-state-prefill-bfloat16] | 0.0129 | 1.95 | 3.25 | torch 100.7%, torch-compile 100.5% | - |
| 🟡 | LogicalOrFwdOp | test_logical_or_manifest_bench[hidden-state-prefill-float32] | 0.0224 | 1.12 | 3.37 | torch 99.9%, torch-compile 110.5% | - |
| 🔵 | LogicalOrFwdOp | test_logical_or_manifest_bench[cnn-feat-broadcast-bool] | 0.0081 | 4.78 | 3.19 | torch 548.4%, torch-compile 127.0% | - |
| 🔴 | LogicalOrFwdOp | test_logical_or_manifest_bench[cnn-feat-broadcast-float16] | 0.0164 | 2.35 | 2.35 | torch 291.1%, torch-compile 73.5% | - |
| 🔴 | LogicalOrFwdOp | test_logical_or_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0164 | 2.36 | 2.36 | torch 298.6%, torch-compile 74.2% | - |
| 🟡 | LogicalOrFwdOp | test_logical_or_manifest_bench[cnn-feat-broadcast-float32] | 0.0209 | 1.84 | 3.07 | torch 222.2%, torch-compile 88.7% | - |
| 🔵 | LtFwdOp | test_comparison_bench[lt-1024x4096-float16-lt] | 0.0076 | 0.56 | 2.78 | torch 102.5%, torch-compile 102.5% | - |
| 🔵 | LtFwdOp | test_lt_manifest_bench[hidden-state-prefill-float16] | 0.0130 | 0.65 | 3.24 | torch 101.0%, torch-compile 101.2% | - |
| 🔵 | LtFwdOp | test_lt_manifest_bench[hidden-state-prefill-bfloat16] | 0.0132 | 0.64 | 3.18 | torch 100.5%, torch-compile 100.5% | - |
| 🟡 | LtFwdOp | test_lt_manifest_bench[hidden-state-prefill-float32] | 0.0225 | 0.37 | 3.35 | torch 100.0%, torch-compile 99.7% | - |
| 🔴 | LtFwdOp | test_lt_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.81 | 2.42 | torch 312.7%, torch-compile 74.4% | - |
| 🔴 | LtFwdOp | test_lt_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.81 | 2.42 | torch 317.1%, torch-compile 76.7% | - |
| 🟡 | LtFwdOp | test_lt_manifest_bench[cnn-feat-broadcast-float32] | 0.0209 | 0.61 | 3.07 | torch 235.5%, torch-compile 88.1% | - |
| 🟡 | MHCPostFwdOp | test_mhc_post_bench[post-small-bfloat16] | 0.0013 | 0.01 | 0.02 | torch-ref 781.0%, torch-compile 97.6% | - |
| 🟡 | MHCPostFwdOp | test_mhc_post_bench[post-medium-bfloat16] | 0.0015 | 0.02 | 0.05 | torch-ref 749.8%, torch-compile 94.6% | - |
| 🔵 | MHCPostFwdOp | test_mhc_post_bench[post-large-bfloat16] | 0.0016 | 0.05 | 0.12 | torch-ref 712.0%, torch-compile 108.0% | - |
| 🔴 | MHCPreFwdOp | test_mhc_pre_bench[pre-small-bfloat16] | 0.0394 | 0.01 | 0.01 | torch-ref 150.2%, torch-compile 49.6% | - |
| 🔴 | MHCPreFwdOp | test_mhc_pre_bench[pre-medium-bfloat16] | 0.0544 | 0.02 | 0.01 | torch-ref 142.9%, torch-compile 58.0% | - |
| 🔴 | MHCPreFwdOp | test_mhc_pre_bench[pre-large-bfloat16] | 0.0716 | 0.03 | 0.02 | torch-ref 163.0%, torch-compile 79.4% | - |
| 🟡 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-2p7b-b1-s2k-bfloat16] | 0.1092 | 74.54 | 0.99 | mamba 99.8%, torch-ref 1973.5%, torch-compile 629.6% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-1p3b-b1-s8k-float16] | 0.2888 | 90.42 | 1.21 | mamba 108.2%, torch-ref 2392.6%, torch-compile 699.0% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-2p7b-b1-s2k-dt-bias-bfloat16] | 0.1090 | 74.69 | 1.00 | mamba 100.2%, torch-ref 1977.1%, torch-compile 631.7% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-1p3b-b1-s8k-dt-bias-float16] | 0.2889 | 90.39 | 1.21 | mamba 108.5%, torch-ref 2390.7%, torch-compile 697.4% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-2p7b-b1-s2k-init-states-bfloat16] | 0.1099 | 74.12 | 1.01 | mamba 100.7%, torch-ref 1960.9%, torch-compile 617.1% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-1p3b-b1-s8k-init-states-float16] | 0.2886 | 90.47 | 1.22 | mamba 108.5%, torch-ref 2391.0%, torch-compile 698.6% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-2p7b-b1-s2k-dt-bias-init-states-bfloat16] | 0.1099 | 74.10 | 1.01 | mamba 100.6%, torch-ref 1960.9%, torch-compile 618.6% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-1p3b-b1-s8k-dt-bias-init-states-float16] | 0.2886 | 90.47 | 1.22 | mamba 108.2%, torch-ref 2391.9%, torch-compile 697.1% | - |
| 🟡 | MaskedFillFwdOp | test_masked_fill_tensor_manifest_bench[elementwise-16M-float16] | 0.0228 | 0.74 | 3.69 | torch 177.2%, torch-compile 99.3% | - |
| 🟡 | MaskedFillFwdOp | test_masked_fill_tensor_manifest_bench[elementwise-16M-bfloat16] | 0.0226 | 0.74 | 3.71 | torch 177.5%, torch-compile 99.7% | - |
| 🟡 | MaskedFillFwdOp | test_masked_fill_tensor_manifest_bench[elementwise-16M-float32] | 0.0381 | 0.44 | 3.97 | torch 192.2%, torch-compile 98.3% | - |
| 🔵 | MaskedFillFwdOp | test_masked_fill_tensor_manifest_bench[elementwise-256M-float16] | 0.3092 | 0.87 | 4.34 | torch 184.3%, torch-compile 100.2% | - |
| 🟡 | MaskedFillFwdOp | test_masked_fill_tensor_manifest_bench[elementwise-256M-bfloat16] | 0.3104 | 0.86 | 4.32 | torch 183.8%, torch-compile 99.9% | - |
| 🟡 | MaskedFillScalarFwdOp | test_masked_fill_scalar_manifest_bench[elementwise-16M-float16] | 0.0228 | 0.74 | 3.69 | torch 164.7%, torch-compile 99.3% | - |
| 🔵 | MaskedFillScalarFwdOp | test_masked_fill_scalar_manifest_bench[elementwise-16M-bfloat16] | 0.0225 | 0.75 | 3.73 | torch 167.5%, torch-compile 100.0% | - |
| 🟡 | MaskedFillScalarFwdOp | test_masked_fill_scalar_manifest_bench[elementwise-16M-float32] | 0.0379 | 0.44 | 3.99 | torch 187.3%, torch-compile 98.4% | - |
| 🟡 | MaskedFillScalarFwdOp | test_masked_fill_scalar_manifest_bench[elementwise-256M-float16] | 0.3101 | 0.87 | 4.33 | torch 182.9%, torch-compile 99.8% | - |
| 🟡 | MaskedFillScalarFwdOp | test_masked_fill_scalar_manifest_bench[elementwise-256M-bfloat16] | 0.3106 | 0.86 | 4.32 | torch 182.8%, torch-compile 99.8% | - |
| 🔵 | MaxPool1dFwdOp | test_max_pool1d_bench[sincnet-speaker-local-float16] | 0.0114 | 0.92 | 2.45 | torch-ref 442.6%, torch-compile 100.0% | - |
| 🔴 | MaxPool1dFwdOp | test_max_pool1d_bench[textcnn-global-float16] | 0.0134 | 0.16 | 0.31 | torch-ref 196.7%, torch-compile 27.6% | - |
| 🟡 | MaxPool1dFwdOp | test_max_pool1d_bench[ecg-cnn-dilated-bfloat16] | 0.0095 | 1.10 | 1.32 | torch-ref 371.5%, torch-compile 82.2% | - |
| 🔴 | MaxPool1dIndicesFwdOp | test_max_pool1d_indices_bench[sincnet-speaker-local-float16] | 0.0218 | 0.48 | 2.57 | torch-ref 232.2%, torch-compile 73.5% | - |
| 🔴 | MaxPool1dIndicesFwdOp | test_max_pool1d_indices_bench[textcnn-global-float16] | 0.0193 | 0.11 | 0.23 | torch-ref 137.0%, torch-compile 29.5% | - |
| 🔴 | MaxPool1dIndicesFwdOp | test_max_pool1d_indices_bench[ecg-cnn-dilated-bfloat16] | 0.0223 | 0.47 | 1.31 | torch-ref 158.6%, torch-compile 60.0% | - |
| 🔴 | MaxPool2dFwdOp | test_max_pool2d_bench[resnet-stem-float16] | 0.0472 | 1.23 | 1.36 | flaggems 166.3%, torch-ref 294.8%, torch-compile 72.1% | - |
| 🔴 | MaxPool2dFwdOp | test_max_pool2d_bench[resnet-stem-bfloat16] | 0.0470 | 1.23 | 1.37 | flaggems 166.8%, torch-ref 296.8%, torch-compile 72.6% | - |
| 🟡 | MaxPool2dFwdOp | test_max_pool2d_bench[resnet-stem-float32] | 0.0529 | 1.09 | 2.43 | flaggems 153.7%, torch-ref 254.8%, torch-compile 93.7% | - |
| 🔵 | MaxPool2dFwdOp | test_max_pool2d_bench[vgg-block-float16] | 0.0072 | 0.89 | 2.23 | flaggems 205.3%, torch-ref 385.8%, torch-compile 101.3% | - |
| 🔵 | MaxPool2dFwdOp | test_max_pool2d_bench[vgg-block-bfloat16] | 0.0072 | 0.89 | 2.23 | flaggems 205.8%, torch-ref 387.2%, torch-compile 100.9% | - |
| 🟡 | MaxPool2dFwdOp | test_max_pool2d_bench[vgg-block-float32] | 0.0111 | 0.58 | 2.90 | flaggems 151.1%, torch-ref 250.8%, torch-compile 93.9% | - |
| 🔵 | MaxPool2dFwdOp | test_max_pool2d_bench[alexnet-ceil-float16] | 0.0088 | 1.53 | 1.75 | flaggems 256.9%, torch-ref 396.0%, torch-compile 125.2% | - |
| 🔵 | MaxPool2dFwdOp | test_max_pool2d_bench[alexnet-ceil-bfloat16] | 0.0088 | 1.54 | 1.76 | flaggems 259.6%, torch-ref 397.4%, torch-compile 125.4% | - |
| 🔵 | MaxPool2dFwdOp | test_max_pool2d_bench[alexnet-ceil-float32] | 0.0126 | 1.07 | 2.44 | flaggems 181.1%, torch-ref 271.1%, torch-compile 122.3% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[resnet-stem-float16] | 0.1124 | 0.51 | 1.03 | flaggems 69.7%, torch-ref 123.7%, torch-compile 61.5% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[resnet-stem-bfloat16] | 0.1123 | 0.51 | 1.03 | flaggems 69.8%, torch-ref 124.3%, torch-compile 62.3% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[resnet-stem-float32] | 0.1073 | 0.54 | 1.68 | flaggems 75.5%, torch-ref 125.5%, torch-compile 66.7% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[vgg-block-float16] | 0.0196 | 0.33 | 1.47 | flaggems 75.4%, torch-ref 141.2%, torch-compile 54.2% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[vgg-block-bfloat16] | 0.0195 | 0.33 | 1.49 | flaggems 76.1%, torch-ref 143.2%, torch-compile 54.6% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[vgg-block-float32] | 0.0195 | 0.33 | 2.30 | flaggems 85.7%, torch-ref 142.1%, torch-compile 64.9% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[alexnet-ceil-float16] | 0.0237 | 0.57 | 1.15 | flaggems 95.0%, torch-ref 146.6%, torch-compile 74.5% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[alexnet-ceil-bfloat16] | 0.0237 | 0.57 | 1.15 | flaggems 95.7%, torch-ref 146.7%, torch-compile 73.4% | - |
| 🟡 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[alexnet-ceil-float32] | 0.0236 | 0.57 | 1.81 | flaggems 96.6%, torch-ref 144.5%, torch-compile 81.7% | - |
| 🔵 | MaxPool3dFwdOp | test_max_pool3d_bench[c3d-pool1-float16] | 0.0763 | 1.35 | 3.37 | cudnn 394.6%, torch-ref 678.2%, torch-compile 101.0% | - |
| 🔵 | MaxPool3dFwdOp | test_max_pool3d_bench[c3d-pool2-float16] | 0.0235 | 1.09 | 2.46 | cudnn 258.0%, torch-ref 398.9%, torch-compile 104.9% | - |
| 🟢 | MaxPool3dFwdOp | test_max_pool3d_bench[medicalnet-stem-bfloat16] | 0.1111 | 1.72 | 1.05 | cudnn 237.3%, torch-ref 301.4%, torch-compile 833.7% | - |
| 🔴 | MaxPool3dIndicesFwdOp | test_max_pool3d_indices_bench[c3d-pool1-float16] | 0.3044 | 0.34 | 1.52 | torch-ref 170.3%, torch-compile 42.4% | - |
| 🔴 | MaxPool3dIndicesFwdOp | test_max_pool3d_indices_bench[c3d-pool2-float16] | 0.0589 | 0.44 | 1.42 | torch-ref 159.4%, torch-compile 55.5% | - |
| 🔵 | MaxPool3dIndicesFwdOp | test_max_pool3d_indices_bench[medicalnet-stem-bfloat16] | 0.3316 | 0.58 | 0.52 | torch-ref 101.0%, torch-compile 614.1% | - |
| 🟡 | MaximumFwdOp | test_binary_arith_bench[maximum-1024x4096-float16-float16-MaximumFwdOp-maximum-normal] | 0.0086 | 0.49 | 2.93 | torch 100.9%, torch-compile 97.6% | - |
| 🟡 | MaximumFwdOp | test_binary_arith_bench[maximum-1024x10240-float16-float16-MaximumFwdOp-maximum-normal] | 0.0180 | 0.58 | 3.49 | torch 100.5%, torch-compile 98.8% | - |
| 🟡 | MaximumFwdOp | test_binary_arith_bench[maximum-1024x11008-float16-float16-MaximumFwdOp-maximum-normal] | 0.0189 | 0.60 | 3.58 | torch 100.5%, torch-compile 98.7% | - |
| 🟡 | MaximumFwdOp | test_maximum_manifest_bench[hidden-state-prefill-float16] | 0.0147 | 0.57 | 3.43 | torch 100.7%, torch-compile 98.7% | - |
| 🟡 | MaximumFwdOp | test_maximum_manifest_bench[hidden-state-prefill-bfloat16] | 0.0149 | 0.56 | 3.37 | torch 100.4%, torch-compile 98.7% | - |
| 🟡 | MaximumFwdOp | test_maximum_manifest_bench[hidden-state-prefill-float32] | 0.0263 | 0.32 | 3.82 | torch 100.6%, torch-compile 99.5% | - |
| 🔴 | MaximumFwdOp | test_maximum_manifest_bench[cnn-feat-broadcast-float16] | 0.0374 | 0.34 | 1.37 | torch 134.8%, torch-compile 38.4% | - |
| 🔴 | MaximumFwdOp | test_maximum_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0393 | 0.33 | 1.31 | torch 130.9%, torch-compile 36.2% | - |
| 🟡 | MaximumFwdOp | test_maximum_manifest_bench[cnn-feat-broadcast-float32] | 0.0294 | 0.44 | 3.50 | torch 180.7%, torch-compile 89.9% | - |
| 🔵 | MeanFwdOp | test_mean_bench[hidden-state-reduce-float16] | 0.0074 | 1.13 | 2.26 | flaggems 119.8%, torch 666.4%, torch-compile 112.5% | - |
| 🔵 | MeanFwdOp | test_mean_bench[hidden-state-reduce-bfloat16] | 0.0074 | 1.13 | 2.26 | flaggems 120.3%, torch 670.7%, torch-compile 113.8% | - |
| 🟡 | MeanFwdOp | test_mean_bench[long-seq-reduce-bfloat16] | 0.0041 | 0.52 | 1.03 | flaggems 93.7%, torch 414.9%, torch-compile 110.2% | - |
| 🟡 | MeanFwdOp | test_mean_bench[3d-multidim-reduce-float16] | 0.0057 | 0.37 | 0.74 | flaggems 238.4%, torch 339.0%, torch-compile 84.8% | - |
| 🔴 | MeanPoolingForwardOp | test_mean_pooling_bench[dense-mainstream] | 0.1351 | 0.50 | 1.01 | torch-ref 455.0%, torch-compile 314.1%, torch-view-mean 34.8% | - |
| 🔴 | MeanPoolingForwardOp | test_mean_pooling_bench[dense-batched] | 0.0702 | 0.48 | 0.97 | torch-ref 372.4%, torch-compile 207.3%, torch-view-mean 40.6% | - |
| 🟢 | MeanPoolingForwardOp | test_mean_pooling_bench[varlen-long] | 0.1387 | 0.48 | 0.98 | torch-ref 446.7%, torch-compile 443.5% | - |
| 🟢 | MeanPoolingForwardOp | test_mean_pooling_bench[varlen-tail] | 0.0218 | 0.41 | 0.78 | torch-ref 982.8%, torch-compile 963.1% | - |
| 🟡 | MinimumFwdOp | test_binary_arith_bench[minimum-1024x4096-float16-float16-MinimumFwdOp-minimum-normal] | 0.0086 | 0.49 | 2.92 | torch 101.5%, torch-compile 97.4% | - |
| 🟡 | MinimumFwdOp | test_binary_arith_bench[minimum-1024x10240-float16-float16-MinimumFwdOp-minimum-normal] | 0.0180 | 0.58 | 3.49 | torch 100.7%, torch-compile 98.9% | - |
| 🟡 | MinimumFwdOp | test_binary_arith_bench[minimum-1024x11008-float16-float16-MinimumFwdOp-minimum-normal] | 0.0189 | 0.60 | 3.57 | torch 100.3%, torch-compile 99.3% | - |
| 🟡 | MinimumFwdOp | test_minimum_manifest_bench[hidden-state-prefill-float16] | 0.0149 | 0.56 | 3.37 | torch 100.9%, torch-compile 98.7% | - |
| 🟡 | MinimumFwdOp | test_minimum_manifest_bench[hidden-state-prefill-bfloat16] | 0.0150 | 0.56 | 3.36 | torch 100.8%, torch-compile 98.5% | - |
| 🟡 | MinimumFwdOp | test_minimum_manifest_bench[hidden-state-prefill-float32] | 0.0265 | 0.32 | 3.80 | torch 100.0%, torch-compile 99.5% | - |
| 🔴 | MinimumFwdOp | test_minimum_manifest_bench[cnn-feat-broadcast-float16] | 0.0374 | 0.34 | 1.37 | torch 135.0%, torch-compile 38.4% | - |
| 🔴 | MinimumFwdOp | test_minimum_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0394 | 0.33 | 1.31 | torch 130.5%, torch-compile 36.6% | - |
| 🟡 | MinimumFwdOp | test_minimum_manifest_bench[cnn-feat-broadcast-float32] | 0.0295 | 0.44 | 3.49 | torch 179.9%, torch-compile 89.6% | - |
| 🟢 | MishFwdOp | test_mish_manifest_bench[yolo-p3-float16] | 0.0404 | 2.60 | 2.60 | torch 157.8%, torch-compile 181.7% | - |
| 🟢 | MishFwdOp | test_mish_manifest_bench[yolo-p3-bfloat16] | 0.0404 | 2.59 | 2.59 | torch 159.1%, torch-compile 183.7% | - |
| 🟢 | MishFwdOp | test_mish_manifest_bench[yolo-p4-float16] | 0.0215 | 2.44 | 2.44 | torch 155.1%, torch-compile 177.8% | - |
| 🟢 | MishFwdOp | test_mish_manifest_bench[yolo-p4-bfloat16] | 0.0216 | 2.42 | 2.42 | torch 155.6%, torch-compile 178.4% | - |
| 🟢 | MoeGateUpFwdOp | test_moe_gate_up_bench[deepseek-v3-decode-gate-up-bfloat16] | 3.4603 | 69.51 | 4.37 | torch-ref 191.8%, torch-compile 227.0% | - |
| 🟢 | MoeGateUpFwdOp | test_moe_gate_up_bench[deepseek-v3-prefill-gate-up-bfloat16] | 4.3982 | 437.49 | 3.56 | torch-ref 158.3%, torch-compile 615.2% | - |
| 🔵 | MoeGroupedGemmNopadFwdOp | test_moe_grouped_gemm_nopad_bench[deepseek-v3-decode-gate-up-bfloat16] | 3.7435 | 64.25 | 4.04 | torch-ref 138.2%, torch-compile 156.4% | - |
| 🔵 | MoeGroupedGemmNopadFwdOp | test_moe_grouped_gemm_nopad_bench[deepseek-v3-prefill-gate-up-bfloat16] | 4.3041 | 447.05 | 3.66 | torch-ref 125.8%, torch-compile 251.4% | - |
| 🔵 | MoeGroupedGemmNopadFwdOp | test_moe_grouped_gemm_nopad_bench[deepseek-v3-decode-down-bfloat16] | 1.9107 | 62.94 | 3.97 | torch-ref 140.9%, torch-compile 292.3% | - |
| 🔵 | MoeGroupedGemmNopadFwdOp | test_moe_grouped_gemm_nopad_bench[deepseek-v3-prefill-down-bfloat16] | 2.1519 | 447.08 | 3.77 | torch-ref 132.2%, torch-compile 1200.2% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[kimi-k2-decode-int32] | 0.0169 | 0.00 | 0.01 | triton 287.1% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[kimi-k2-small-int32] | 0.0194 | 0.00 | 0.01 | triton 247.2% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[kimi-k2-medium-int32] | 0.0217 | 0.00 | 0.01 | triton 257.3% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[kimi-k2-prefill-int32] | 0.0411 | 0.00 | 0.01 | triton 208.5% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[deepseek-v3-decode-int32] | 0.0148 | 0.00 | 0.00 | triton 228.1% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[deepseek-v3-small-int32] | 0.0153 | 0.00 | 0.00 | triton 220.1% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[deepseek-v3-medium-int32] | 0.0177 | 0.00 | 0.01 | triton 236.8% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[deepseek-v3-prefill-int32] | 0.0378 | 0.00 | 0.01 | triton 196.6% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[qwen3-decode-int32] | 0.0108 | 0.00 | 0.00 | triton 156.8% | - |
| 🔵 | MoePermuteAlignFwdOp | test_permute_align_bench[qwen3-small-int32] | 0.0121 | 0.00 | 0.00 | triton 149.9% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[qwen3-medium-int32] | 0.0141 | 0.00 | 0.00 | triton 211.8% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[qwen3-prefill-int32] | 0.0318 | 0.00 | 0.01 | triton 251.6% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[kimi-k2-decode-bfloat16] | 0.0106 | 0.00 | 0.01 | vllm 109.9% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[kimi-k2-small-bfloat16] | 0.0118 | 0.00 | 0.35 | vllm 117.6% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[kimi-k2-medium-bfloat16] | 0.0356 | 0.00 | 1.86 | vllm 129.2% | - |
| 🟡 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[kimi-k2-prefill-bfloat16] | 0.2856 | 0.00 | 1.85 | vllm 95.0% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-decode-bfloat16] | 0.0092 | 0.00 | 0.01 | vllm 125.2% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-small-bfloat16] | 0.0104 | 0.00 | 0.40 | vllm 131.9% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-medium-bfloat16] | 0.0337 | 0.00 | 1.96 | vllm 136.1% | - |
| 🟡 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-prefill-bfloat16] | 0.2789 | 0.00 | 1.90 | vllm 96.9% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-235b-decode-bfloat16] | 0.0080 | 0.00 | 0.02 | vllm 143.0% | - |
| 🟢 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-235b-small-bfloat16] | 0.0090 | 0.00 | 0.46 | vllm 153.4% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-235b-medium-bfloat16] | 0.0314 | 0.00 | 2.11 | vllm 146.8% | - |
| 🟡 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-235b-prefill-bfloat16] | 0.2687 | 0.00 | 1.97 | vllm 97.4% | - |
| 🟢 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-30b-decode-bfloat16] | 0.0063 | 0.00 | 0.01 | vllm 166.7% | - |
| 🟢 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-30b-small-bfloat16] | 0.0072 | 0.00 | 0.25 | vllm 173.8% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-30b-medium-bfloat16] | 0.0207 | 0.00 | 1.37 | vllm 140.0% | - |
| 🟡 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-30b-prefill-bfloat16] | 0.1419 | 0.00 | 1.60 | vllm 91.2% | - |
|  | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-ep2-decode-bfloat16] | 0.0087 | 0.00 | 0.02 | - | - |
|  | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-ep2-medium-bfloat16] | 0.0280 | 0.00 | 2.36 | - | - |
|  | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-ep2-prefill-bfloat16] | 0.2102 | 0.00 | 2.52 | - | - |
|  | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-235b-ep2-medium-bfloat16] | 0.0265 | 0.00 | 2.49 | - | - |
| 🟢 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[large-hidden-decode-bfloat16] | 0.0070 | 0.02 | 0.02 | vllm 237.2% | - |
| 🟢 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[large-hidden-small-bfloat16] | 0.0079 | 0.47 | 0.52 | vllm 227.6% | - |
| 🔵 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[large-hidden-medium-bfloat16] | 0.0213 | 2.75 | 3.10 | vllm 137.0% | - |
| 🔵 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[large-hidden-prefill-bfloat16] | 0.1331 | 3.53 | 3.97 | vllm 104.7% | - |
| 🟢 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[small-hidden-decode-bfloat16] | 0.0057 | 0.01 | 0.01 | vllm 158.2% | - |
| 🟢 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[small-hidden-small-bfloat16] | 0.0065 | 0.24 | 0.27 | vllm 153.4% | - |
| 🔵 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[small-hidden-medium-bfloat16] | 0.0116 | 2.17 | 2.45 | vllm 127.9% | - |
| 🔵 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[small-hidden-prefill-bfloat16] | 0.0616 | 3.27 | 3.68 | vllm 109.5% | - |
| 🔵 | MulFwdOp | test_binary_arith_bench[mul-1024x4096-float16-float16-MulFwdOp-mul-normal] | 0.0084 | 0.50 | 2.99 | torch 101.9%, torch-compile 100.0% | - |
| 🔵 | MulFwdOp | test_binary_arith_bench[mul-1024x10240-float16-float16-MulFwdOp-mul-normal] | 0.0176 | 0.60 | 3.58 | torch 101.1%, torch-compile 100.2% | - |
| 🔵 | MulFwdOp | test_binary_arith_bench[mul-1024x11008-float16-float16-MulFwdOp-mul-normal] | 0.0185 | 0.61 | 3.65 | torch 100.1%, torch-compile 100.2% | - |
| 🟡 | MulFwdOp | test_mul_manifest_bench[hidden-state-prefill-float16] | 0.0149 | 0.56 | 3.39 | torch 100.1%, torch-compile 99.9% | - |
| 🟡 | MulFwdOp | test_mul_manifest_bench[hidden-state-prefill-bfloat16] | 0.0147 | 0.57 | 3.43 | torch 100.2%, torch-compile 100.0% | - |
| 🟡 | MulFwdOp | test_mul_manifest_bench[hidden-state-prefill-float32] | 0.0264 | 0.32 | 3.81 | torch 99.8%, torch-compile 99.5% | - |
| 🔵 | MulFwdOp | test_mul_manifest_bench[cnn-feat-broadcast-float16] | 0.0142 | 0.90 | 3.61 | torch 319.6%, torch-compile 100.0% | - |
| 🔵 | MulFwdOp | test_mul_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0145 | 0.89 | 3.54 | torch 318.3%, torch-compile 100.0% | - |
| 🔵 | MulFwdOp | test_mul_manifest_bench[cnn-feat-broadcast-float32] | 0.0265 | 0.48 | 3.88 | torch 186.3%, torch-compile 100.2% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-8b-short-float16] | 0.2434 | 88.24 | 0.48 | fa3 59.1% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-8b-short-bfloat16] | 0.4557 | 47.12 | 0.26 | fa3 31.5% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-8b-long-float16] | 0.9015 | 190.58 | 0.26 | fa3 61.2% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-8b-long-bfloat16] | 1.3109 | 131.05 | 0.18 | fa3 41.9% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-70b-short-float16] | 0.2444 | 87.85 | 0.48 | fa3 58.6% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-70b-short-bfloat16] | 0.4566 | 47.03 | 0.26 | fa3 31.4% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-70b-long-float16] | 0.8914 | 192.72 | 0.26 | fa3 62.1% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-70b-long-bfloat16] | 1.1017 | 155.94 | 0.21 | fa3 49.9% | - |
| 🟢 | MultiHeadAttentionDecodePagedWithKVCacheFwdOp | test_mha_decode_paged_bench[single-token-page128-float16] | 0.0061 | 0.69 | 0.69 | flashinfer 151.3% | - |
| 🟢 | MultiHeadAttentionDecodePagedWithKVCacheFwdOp | test_mha_decode_paged_bench[batch2-page256-float16] | 0.0057 | 0.73 | 0.37 | fa3 324.3%, flashinfer 169.7% | - |
| 🟢 | MultiHeadAttentionDecodePagedWithKVCacheFwdOp | test_mha_decode_paged_bench[longer-cache-float16] | 0.0053 | 0.40 | 0.40 | fa3 343.8%, flashinfer 181.9% | - |
| 🟢 | MultiHeadAttentionDecodePagedWithKVCacheFwdOp | test_mha_decode_paged_bench[shorter-cache-float16] | 0.0046 | 0.23 | 0.23 | fa3 387.5%, flashinfer 200.7% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-8b-4k-float16] | 0.5114 | 4.20 | 4.20 | fa3 100.2%, flashinfer 103.5% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-8b-4k-bfloat16] | 0.5102 | 4.21 | 4.21 | fa3 100.4%, flashinfer 103.9% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-8b-32k-float16] | 0.9811 | 4.38 | 4.38 | fa3 100.8%, flashinfer 101.9% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-8b-32k-bfloat16] | 0.9811 | 4.38 | 4.38 | fa3 100.6%, flashinfer 101.8% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-70b-4k-float16] | 0.5142 | 4.18 | 4.18 | fa3 100.2%, flashinfer 103.2% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-70b-4k-bfloat16] | 0.5139 | 4.18 | 4.18 | fa3 100.2%, flashinfer 103.2% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-70b-32k-float16] | 0.9798 | 4.38 | 4.38 | fa3 100.8%, flashinfer 102.1% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-70b-32k-bfloat16] | 0.9800 | 4.38 | 4.38 | fa3 100.7%, flashinfer 101.5% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-8b-short-float16] | 0.0428 | 200.70 | 1.57 | fa3 81.5%, flashinfer 95.9% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-8b-short-bfloat16] | 0.0425 | 202.14 | 1.58 | fa3 83.3%, flashinfer 96.2% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-8b-long-float16] | 0.1693 | 405.88 | 0.79 | fa3 82.2%, flashinfer 96.3% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-8b-long-bfloat16] | 0.1675 | 410.26 | 0.80 | fa3 81.6%, flashinfer 96.9% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-70b-short-float16] | 0.0426 | 201.53 | 1.57 | fa3 82.8%, flashinfer 96.5% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-70b-short-bfloat16] | 0.0427 | 201.38 | 1.57 | fa3 82.8%, flashinfer 96.7% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-70b-long-float16] | 0.1689 | 406.95 | 0.79 | fa3 82.3%, flashinfer 97.0% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-70b-long-bfloat16] | 0.1674 | 410.61 | 0.80 | fa3 81.7%, flashinfer 96.9% | - |
| 🟢 | MultiHeadLatentAttentionDecodeWithKVCacheFwdOp | test_mla_decode_bench[deepseek-v2-4k-float16] | 0.0372 | 288.27 | 1.42 | torch-ref 442.5%, torch-compile 353.4% | - |
| 🟢 | MultiHeadLatentAttentionDecodeWithKVCacheFwdOp | test_mla_decode_bench[deepseek-v2-4k-bfloat16] | 0.0374 | 286.79 | 1.41 | torch-ref 438.1%, torch-compile 351.4% | - |
| 🟢 | MultiHeadLatentAttentionDecodeWithKVCacheFwdOp | test_mla_decode_bench[deepseek-v2-32k-float16] | 0.1189 | 180.64 | 0.85 | torch-ref 230.7%, torch-compile 212.4% | - |
| 🟢 | MultiHeadLatentAttentionDecodeWithKVCacheFwdOp | test_mla_decode_bench[deepseek-v2-32k-bfloat16] | 0.1188 | 180.84 | 0.85 | torch-ref 234.2%, torch-compile 215.4% | - |
| 🟢 | MultiHeadLatentAttentionDecodeWithKVCacheFwdOp | test_mla_decode_bench[deepseek-v3-4k-bfloat16] | 0.0217 | 247.82 | 1.22 | torch-ref 391.4%, torch-compile 321.6% | - |
| 🔵 | MultiHeadLatentAttentionDecodeWithKVCacheFwdOp | test_mla_decode_bench[deepseek-v3-32k-bfloat16] | 0.1181 | 90.88 | 0.43 | torch-ref 144.8%, torch-compile 140.4% | - |
| 🟡 | NanToNumFwdOp | test_nan_to_num_manifest_bench[elementwise-16M-float16] | 0.0189 | 5.32 | 3.55 | torch 101.8%, torch-compile 98.2% | - |
| 🟡 | NanToNumFwdOp | test_nan_to_num_manifest_bench[elementwise-16M-bfloat16] | 0.0189 | 5.33 | 3.55 | torch 101.9%, torch-compile 98.3% | - |
| 🔵 | NanToNumFwdOp | test_nan_to_num_manifest_bench[elementwise-16M-float32] | 0.0339 | 2.97 | 3.96 | torch 100.4%, torch-compile 100.2% | - |
| 🟡 | NanToNumFwdOp | test_nan_to_num_manifest_bench[elementwise-256M-float16] | 0.2651 | 6.07 | 4.05 | torch 103.6%, torch-compile 97.8% | - |
| 🟡 | NanToNumFwdOp | test_nan_to_num_manifest_bench[elementwise-256M-bfloat16] | 0.2639 | 6.10 | 4.07 | torch 103.7%, torch-compile 98.0% | - |
| 🔵 | NeFwdOp | test_comparison_bench[ne-1024x4096-float16-ne] | 0.0076 | 0.55 | 2.74 | torch 102.1%, torch-compile 101.7% | - |
| 🔵 | NeFwdOp | test_ne_manifest_bench[hidden-state-prefill-float16] | 0.0130 | 0.64 | 3.22 | torch 101.0%, torch-compile 100.9% | - |
| 🔵 | NeFwdOp | test_ne_manifest_bench[hidden-state-prefill-bfloat16] | 0.0132 | 0.63 | 3.17 | torch 101.4%, torch-compile 101.4% | - |
| 🟡 | NeFwdOp | test_ne_manifest_bench[hidden-state-prefill-float32] | 0.0223 | 0.38 | 3.38 | torch 100.0%, torch-compile 99.7% | - |
| 🔴 | NeFwdOp | test_ne_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.81 | 2.43 | torch 300.8%, torch-compile 75.0% | - |
| 🔴 | NeFwdOp | test_ne_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.81 | 2.43 | torch 307.2%, torch-compile 74.8% | - |
| 🟡 | NeFwdOp | test_ne_manifest_bench[cnn-feat-broadcast-float32] | 0.0208 | 0.62 | 3.09 | torch 229.5%, torch-compile 88.8% | - |
| 🔵 | NegFwdOp | test_neg_bench[elementwise-16M-float16] | 0.0179 | 0.94 | 3.75 | torch 105.4%, torch-compile 100.2% | - |
| 🔵 | NegFwdOp | test_neg_bench[elementwise-16M-bfloat16] | 0.0179 | 0.94 | 3.75 | torch 100.0%, torch-compile 100.0% | - |
| 🟡 | NegFwdOp | test_neg_bench[elementwise-16M-float32] | 0.0340 | 0.49 | 3.95 | torch 99.9%, torch-compile 99.8% | - |
| 🟡 | NegFwdOp | test_neg_bench[elementwise-256M-float16] | 0.2502 | 1.07 | 4.29 | torch 107.4%, torch-compile 99.8% | - |
| 🔵 | NegFwdOp | test_neg_bench[elementwise-256M-bfloat16] | 0.2496 | 1.08 | 4.30 | torch 100.0%, torch-compile 100.2% | - |
| 🔵 | PowFwdOp | test_binary_arith_bench[pow-1024x4096-float16-float16-PowFwdOp-pow-positive] | 0.0201 | 0.21 | 1.25 | torch 100.6%, torch-compile 125.7% | - |
| 🟡 | PowFwdOp | test_binary_arith_bench[pow-1024x10240-float16-float16-PowFwdOp-pow-positive] | 0.0453 | 0.23 | 1.39 | torch 99.9%, torch-compile 118.9% | - |
| 🔵 | PowFwdOp | test_pow_manifest_bench[hidden-state-prefill-float16] | 0.0370 | 0.68 | 1.36 | torch 100.3%, torch-compile 119.0% | - |
| 🟡 | PowFwdOp | test_pow_manifest_bench[hidden-state-prefill-bfloat16] | 0.0378 | 0.67 | 1.33 | torch 99.8%, torch-compile 119.5% | - |
| 🟡 | PowFwdOp | test_pow_manifest_bench[hidden-state-prefill-float32] | 0.0388 | 0.65 | 2.59 | torch 96.3%, torch-compile 108.4% | - |
| 🔵 | PowFwdOp | test_pow_manifest_bench[cnn-feat-broadcast-float16] | 0.0542 | 0.71 | 0.95 | torch 173.2%, torch-compile 112.5% | - |
| 🔵 | PowFwdOp | test_pow_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0543 | 0.71 | 0.95 | torch 175.2%, torch-compile 113.2% | - |
| 🔵 | PowFwdOp | test_pow_manifest_bench[cnn-feat-broadcast-float32] | 0.0574 | 0.67 | 1.79 | torch 163.5%, torch-compile 102.3% | - |
| 🟡 | PreluFwdOp | test_prelu_manifest_bench[cnn-feat-per-channel-float16] | 0.0147 | 1.75 | 3.51 | torch 321.9%, torch-compile 99.8% | - |
| 🟡 | PreluFwdOp | test_prelu_manifest_bench[cnn-feat-per-channel-bfloat16] | 0.0144 | 1.78 | 3.57 | torch 336.7%, torch-compile 100.0% | - |
| 🔵 | PreluFwdOp | test_prelu_manifest_bench[cnn-feat-per-channel-deep-float16] | 0.0084 | 1.54 | 3.08 | torch 299.6%, torch-compile 100.0% | - |
| 🔵 | PreluFwdOp | test_prelu_manifest_bench[cnn-feat-per-channel-deep-bfloat16] | 0.0082 | 1.57 | 3.14 | torch 314.1%, torch-compile 100.0% | - |
| 🔵 | ProdFwdOp | test_prod_bench[hidden-state-reduce-float16] | 0.0074 | 1.13 | 2.27 | flaggems 106.1%, torch 666.2%, torch-compile 112.1% | - |
| 🔵 | ProdFwdOp | test_prod_bench[hidden-state-reduce-bfloat16] | 0.0074 | 1.13 | 2.27 | flaggems 105.6%, torch 672.1%, torch-compile 113.0% | - |
| 🔵 | ProdFwdOp | test_prod_bench[long-seq-reduce-bfloat16] | 0.0044 | 0.48 | 0.96 | flaggems 311.1%, torch 384.6%, torch-compile 101.5% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-8b-prefill-float16] | 0.0119 | 2.82 | 2.82 | flaggems 106.7%, flashinfer 92.2%, vllm 104.6%, torch-ref 1222.1%, torch-compile 114.2% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-8b-prefill-bfloat16] | 0.0126 | 2.65 | 2.66 | flaggems 98.7%, flashinfer 86.2%, vllm 100.8%, torch-ref 1155.6%, torch-compile 114.2% | - |
| 🔵 | RMSNormFwdOp | test_rms_norm_bench[llama-8b-decode-bfloat16] | 0.0021 | 0.01 | 0.01 | flaggems 157.0%, flashinfer 104.6%, vllm 129.2%, torch-ref 866.1%, torch-compile 129.2% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-70b-prefill-float16] | 0.0210 | 3.19 | 3.20 | flaggems 98.9%, flashinfer 95.6%, vllm 103.1%, torch-ref 1286.7%, torch-compile 96.7% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-70b-prefill-bfloat16] | 0.0218 | 3.08 | 3.08 | flaggems 97.5%, flashinfer 91.6%, vllm 101.2%, torch-ref 1240.9%, torch-compile 94.5% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-70b-decode-bfloat16] | 0.0026 | 0.01 | 0.02 | flaggems 157.3%, flashinfer 98.8%, vllm 118.3%, torch-ref 713.4%, torch-compile 137.8% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-405b-prefill-float16] | 0.0420 | 3.20 | 3.20 | flaggems 95.0%, flashinfer 88.3%, vllm 116.4%, torch-ref 1215.1%, torch-compile 94.5% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-405b-prefill-bfloat16] | 0.0430 | 3.12 | 3.12 | flaggems 95.5%, flashinfer 88.4%, vllm 113.5%, torch-ref 1191.2%, torch-compile 95.7% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-405b-decode-bfloat16] | 0.0036 | 0.02 | 0.03 | flaggems 129.4%, flashinfer 97.3%, vllm 120.5%, torch-ref 560.6%, torch-compile 129.9% | - |
| 🟡 | ReciprocalFwdOp | test_reciprocal_bench[elementwise-16M-float16] | 0.0189 | 0.89 | 3.54 | torch 100.0%, torch-compile 96.1% | - |
| 🟡 | ReciprocalFwdOp | test_reciprocal_bench[elementwise-16M-bfloat16] | 0.0189 | 0.89 | 3.55 | torch 100.3%, torch-compile 96.6% | - |
| 🔵 | ReciprocalFwdOp | test_reciprocal_bench[elementwise-16M-float32] | 0.0335 | 0.50 | 4.00 | torch 101.5%, torch-compile 100.7% | - |
| 🟡 | ReciprocalFwdOp | test_reciprocal_bench[elementwise-256M-float16] | 0.2670 | 1.01 | 4.02 | torch 100.1%, torch-compile 95.9% | - |
| 🟡 | ReciprocalFwdOp | test_reciprocal_bench[elementwise-256M-bfloat16] | 0.2673 | 1.00 | 4.02 | torch 100.0%, torch-compile 96.4% | - |
| 🔵 | ReluFwdOp | test_relu_manifest_bench[hidden-state-prefill-float16] | 0.0103 | 0.81 | 3.26 | torch 104.7%, torch-compile 100.3% | - |
| 🔵 | ReluFwdOp | test_relu_manifest_bench[hidden-state-prefill-bfloat16] | 0.0103 | 0.81 | 3.25 | torch 101.6%, torch-compile 100.3% | - |
| 🔵 | ReluFwdOp | test_relu_manifest_bench[hidden-state-decode-bfloat16] | 0.0012 | 0.00 | 0.01 | torch 113.2%, torch-compile 105.3% | - |
| 🔵 | RemainderFwdOp | test_binary_arith_bench[remainder-1024x4096-float16-float16-RemainderFwdOp-remainder-positive] | 0.0085 | 0.49 | 2.95 | torch 124.7%, torch-compile 100.7% | - |
| 🔵 | RemainderFwdOp | test_binary_arith_bench[remainder-1024x10240-float16-float16-RemainderFwdOp-remainder-positive] | 0.0181 | 0.58 | 3.47 | torch 119.6%, torch-compile 100.4% | - |
| 🔵 | RemainderFwdOp | test_remainder_manifest_bench[hidden-state-prefill-float16] | 0.0154 | 2.18 | 3.26 | torch 117.0%, torch-compile 101.0% | - |
| 🔵 | RemainderFwdOp | test_remainder_manifest_bench[hidden-state-prefill-bfloat16] | 0.0149 | 2.25 | 3.37 | torch 124.2%, torch-compile 101.1% | - |
| 🔵 | RemainderFwdOp | test_remainder_manifest_bench[hidden-state-prefill-float32] | 0.0264 | 1.27 | 3.81 | torch 102.9%, torch-compile 101.1% | - |
| 🔵 | RemainderFwdOp | test_remainder_manifest_bench[cnn-feat-broadcast-float16] | 0.0160 | 3.20 | 3.20 | torch 388.0%, torch-compile 110.8% | - |
| 🔵 | RemainderFwdOp | test_remainder_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0161 | 3.20 | 3.20 | torch 399.6%, torch-compile 115.7% | - |
| 🟡 | RemainderFwdOp | test_remainder_manifest_bench[cnn-feat-broadcast-float32] | 0.0269 | 1.91 | 3.81 | torch 238.1%, torch-compile 99.5% | - |
| 🔵 | RopeLlama31FwdOp | test_rope_llama31_bench[llama31-1d-8k-d128-bfloat16] | 0.0036 | 1.16 | 1.74 | torch-ref 440.7%, torch-compile 123.9% | - |
| 🔴 | RopeLlama31FwdOp | test_rope_llama31_bench[llama31-2d-b1-s8k-h32-d128-float16] | 0.0594 | 2.26 | 2.30 | torch-ref 829.5%, torch-compile 58.7% | - |
| 🔵 | RopeLongRopeFwdOp | test_rope_longrope_bench[longrope-1d-8k-d128-bfloat16] | 0.0036 | 1.17 | 1.76 | torch-ref 442.9%, torch-compile 125.0% | - |
| 🔴 | RopeLongRopeFwdOp | test_rope_longrope_bench[longrope-2d-b1-s8k-h32-d128-float16] | 0.0594 | 2.26 | 2.30 | torch-ref 830.0%, torch-compile 58.7% | - |
| 🔵 | RopeNeoxFwdOp | test_rope_neox_bench[neox-1d-2k-d64-float16] | 0.0018 | 0.29 | 0.43 | torch-ref 517.6%, torch-compile 108.8% | - |
| 🔵 | RopeNeoxFwdOp | test_rope_neox_bench[neox-1d-4k-d128-bfloat16] | 0.0026 | 0.81 | 1.21 | torch-ref 475.3%, torch-compile 116.1% | - |
| 🔴 | RopeNeoxFwdOp | test_rope_neox_bench[neox-2d-b2-s2k-h32-d128-float16] | 0.0310 | 2.16 | 2.18 | torch-ref 877.5%, torch-compile 59.4% | - |
| 🔴 | RopeNeoxPositionIdsFwdOp | test_rope_neox_position_ids_bench[position-ids-s2k-h32-d128-float16] | 0.0278 | 1.21 | 1.24 | vllm 87.2%, torch-ref 465.7%, torch-compile 42.8% | - |
| 🔴 | RopeNeoxPositionIdsFwdOp | test_rope_neox_position_ids_bench[position-ids-s4k-h32-d128-bfloat16] | 0.0455 | 1.47 | 1.52 | vllm 97.7%, torch-ref 547.6%, torch-compile 49.0% | - |
| 🟡 | RopeNonNeoxFwdOp | test_rope_non_neox_bench[non-neox-1d-2k-d64-float16] | 0.0022 | 0.24 | 0.36 | torch-ref 435.3%, torch-compile 92.7% | - |
| 🔴 | RopeNonNeoxFwdOp | test_rope_non_neox_bench[non-neox-2d-b2-s2k-h32-d128-bfloat16] | 0.0252 | 2.66 | 2.69 | torch-ref 1088.7%, torch-compile 75.6% | - |
| 🔵 | RopeYarnFwdOp | test_rope_yarn_bench[yarn-1d-8k-d128-bfloat16] | 0.0036 | 1.17 | 1.76 | torch-ref 443.8%, torch-compile 125.0% | - |
| 🔴 | RopeYarnFwdOp | test_rope_yarn_bench[yarn-2d-b1-s8k-h32-d128-float16] | 0.0594 | 2.26 | 2.29 | torch-ref 828.5%, torch-compile 58.7% | - |
| 🔵 | RoundFwdOp | test_round_bench[elementwise-16M-float16] | 0.0179 | 0.94 | 3.75 | torch 100.4%, torch-compile 100.4% | - |
| 🔵 | RoundFwdOp | test_round_bench[elementwise-16M-bfloat16] | 0.0179 | 0.94 | 3.75 | torch 100.4%, torch-compile 100.2% | - |
| 🟡 | RoundFwdOp | test_round_bench[elementwise-16M-float32] | 0.0340 | 0.49 | 3.95 | torch 100.0%, torch-compile 99.7% | - |
| 🔵 | RoundFwdOp | test_round_bench[elementwise-256M-float16] | 0.2498 | 1.07 | 4.30 | torch 100.1%, torch-compile 100.4% | - |
| 🟡 | RoundFwdOp | test_round_bench[elementwise-256M-bfloat16] | 0.2500 | 1.07 | 4.30 | torch 100.1%, torch-compile 99.9% | - |
| 🔵 | RsqrtFwdOp | test_rsqrt_bench[elementwise-16M-float16] | 0.0181 | 0.93 | 3.70 | torch 100.4%, torch-compile 100.1% | - |
| 🔵 | RsqrtFwdOp | test_rsqrt_bench[elementwise-16M-bfloat16] | 0.0181 | 0.92 | 3.70 | torch 100.4%, torch-compile 100.0% | - |
| 🔵 | RsqrtFwdOp | test_rsqrt_bench[elementwise-16M-float32] | 0.0331 | 0.51 | 4.06 | torch 102.1%, torch-compile 101.7% | - |
| 🟡 | RsqrtFwdOp | test_rsqrt_bench[elementwise-256M-float16] | 0.2538 | 1.06 | 4.23 | torch 100.2%, torch-compile 99.6% | - |
| 🟡 | RsqrtFwdOp | test_rsqrt_bench[elementwise-256M-bfloat16] | 0.2541 | 1.06 | 4.23 | torch 100.1%, torch-compile 99.7% | - |
| 🔵 | SSDChunkScanFwdOp | test_ssd_chunk_scan_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0728 | 88.46 | 1.44 | mamba 138.1%, torch-ref 2690.2%, torch-compile 696.4% | - |
| 🔵 | SSDChunkScanFwdOp | test_ssd_chunk_scan_fwd_bench[mamba2-780m-b1-s4k-bfloat16] | 0.0758 | 84.95 | 1.38 | mamba 134.5%, torch-ref 2584.9%, torch-compile 670.9% | - |
| 🔵 | SSDChunkScanFwdOp | test_ssd_chunk_scan_fwd_bench[mamba2-2p7b-b4-s2k-bfloat16] | 0.2376 | 90.39 | 1.46 | mamba 130.1%, torch-ref 2742.1%, torch-compile 690.4% | - |
| 🔵 | SSDChunkScanFwdOp | test_ssd_chunk_scan_fwd_bench[mamba2-1p3b-b2-s32k-float16] | 1.4675 | 93.65 | 1.51 | mamba 138.5%, torch-ref 2731.5%, torch-compile 679.0% | - |
| 🔵 | SSDChunkStateFwdOp | test_ssd_chunk_state_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0238 | 136.04 | 2.21 | mamba 104.7%, torch-ref 34248.6%, torch-compile 2665.8% | - |
| 🔵 | SSDChunkStateFwdOp | test_ssd_chunk_state_fwd_bench[mamba2-780m-b1-s4k-bfloat16] | 0.0239 | 135.31 | 2.20 | mamba 110.7%, torch-ref 34063.0%, torch-compile 2828.9% | - |
| 🔵 | SSDChunkStateFwdOp | test_ssd_chunk_state_fwd_bench[mamba2-2p7b-b4-s2k-bfloat16] | 0.0656 | 164.28 | 2.65 | mamba 122.0%, torch-ref 41302.4%, torch-compile 3725.3% | - |
| 🔵 | SSDChunkStateFwdOp | test_ssd_chunk_state_fwd_bench[mamba2-780m-b1-s4k-seq-idx-float16] | 0.0287 | 112.69 | 1.83 | mamba 121.2%, torch-ref 28411.2%, torch-compile 2611.6% | - |
| 🔵 | SSDChunkStateFwdOp | test_ssd_chunk_state_fwd_bench[mamba2-780m-b1-s4k-seq-idx-bfloat16] | 0.0289 | 111.81 | 1.82 | mamba 101.2%, torch-ref 28190.7%, torch-compile 2721.0% | - |
| 🔵 | SSDChunkStateFwdOp | test_ssd_chunk_state_fwd_bench[mamba2-1p3b-b2-s32k-seq-idx-float16] | 0.4493 | 153.59 | 2.48 | mamba 140.5%, torch-ref 38560.3%, torch-compile 3710.3% | - |
| 🟢 | SSDDecodeFwdOp | test_ssd_decode_bench[mamba2-1p3b-decode-b1-float16] | 0.0040 | 1.05 | 1.58 | torch-ref 752.0%, torch-compile 225.6% | - |
| 🟢 | SSDDecodeFwdOp | test_ssd_decode_bench[mamba2-1p3b-decode-b1-bfloat16] | 0.0040 | 1.06 | 1.60 | torch-ref 765.7%, torch-compile 225.0% | - |
| 🟢 | SSDDecodeFwdOp | test_ssd_decode_bench[mamba2-2p7b-decode-b8-float16] | 0.0163 | 2.58 | 2.76 | torch-ref 689.8%, torch-compile 183.7% | - |
| 🟢 | SSDDecodeFwdOp | test_ssd_decode_bench[mamba2-780m-decode-b32-float16] | 0.0361 | 2.79 | 2.86 | torch-ref 666.5%, torch-compile 193.0% | - |
| 🟢 | SSDStatePassingFwdOp | test_ssd_state_passing_fwd_bench[mamba2-1p3b-b1-s4k-dstate-float16] | 0.0020 | 0.13 | 0.42 | mamba 433.6%, torch-ref 6180.6%, torch-compile 211.5% | - |
| 🟢 | SSDStatePassingFwdOp | test_ssd_state_passing_fwd_bench[mamba2-1p3b-b1-s4k-dstate-bfloat16] | 0.0020 | 0.13 | 0.41 | mamba 422.6%, torch-ref 6205.0%, torch-compile 206.5% | - |
| 🟢 | SSDStatePassingFwdOp | test_ssd_state_passing_fwd_bench[mamba2-2p7b-b2-s32k-dstate-float16] | 0.0106 | 0.50 | 1.50 | mamba 563.0%, torch-ref 10779.0%, torch-compile 870.4% | - |
| 🟢 | SSDStatePassingFwdOp | test_ssd_state_passing_fwd_bench[mamba2-1p3b-b1-s4k-dstate-init-states-float16] | 0.0020 | 0.13 | 0.43 | mamba 438.7%, torch-ref 6036.9%, torch-compile 172.6% | - |
| 🟢 | SSDStatePassingFwdOp | test_ssd_state_passing_fwd_bench[mamba2-1p3b-b1-s4k-dstate-init-states-bfloat16] | 0.0020 | 0.13 | 0.43 | mamba 435.3%, torch-ref 6107.1%, torch-compile 171.2% | - |
| 🟡 | SSDStatePassingFwdOp | test_ssd_state_passing_fwd_bench[mamba2-1p3b-b1-s4k-flat-init-states-float32] | 0.0220 | 0.76 | 3.25 | mamba 98.2%, torch-ref 577.6%, torch-compile 93.2% | - |
| 🔵 | SeluFwdOp | test_selu_manifest_bench[snn-fc-float16] | 0.0117 | 3.57 | 2.86 | torch 152.9%, torch-compile 137.1% | - |
| 🔵 | SeluFwdOp | test_selu_manifest_bench[snn-fc-bfloat16] | 0.0121 | 3.47 | 2.77 | torch 150.0%, torch-compile 129.4% | - |
| 🔵 | SeluFwdOp | test_selu_manifest_bench[snn-fc-wide-float16] | 0.0211 | 3.98 | 3.19 | torch 156.1%, torch-compile 142.1% | - |
| 🔵 | SeluFwdOp | test_selu_manifest_bench[snn-fc-wide-bfloat16] | 0.0217 | 3.87 | 3.10 | torch 153.2%, torch-compile 134.7% | - |
| 🔴 | SharedFusedMoE | test_shared_fused_moe_bench[1-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 2.5240 | 0.59 | 0.59 | vllm 16.9% | - |
| 🟡 | SharedFusedMoE | test_shared_fused_moe_bench[32-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 4.7526 | 10.08 | 3.66 | vllm 83.4% | - |
| 🔵 | SharedFusedMoE | test_shared_fused_moe_bench[512-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 8.0638 | 95.07 | 4.29 | vllm 108.7% | - |
| 🔴 | SharedFusedMoE | test_shared_fused_moe_bench[2048-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 19.5397 | 156.94 | 1.77 | vllm 59.3% | - |
| 🔴 | SharedFusedMoE | test_shared_fused_moe_bench[4096-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 32.5542 | 188.40 | 1.07 | vllm 44.7% | - |
| 🟡 | SigmoidFwdOp | test_sigmoid_manifest_bench[elementwise-16M-float16] | 0.0215 | 3.13 | 3.13 | torch 106.9%, torch-compile 86.4% | - |
| 🟡 | SigmoidFwdOp | test_sigmoid_manifest_bench[elementwise-16M-bfloat16] | 0.0219 | 3.07 | 3.07 | torch 107.8%, torch-compile 85.5% | - |
| 🟡 | SigmoidFwdOp | test_sigmoid_manifest_bench[elementwise-16M-float32] | 0.0344 | 1.95 | 3.90 | torch 99.9%, torch-compile 98.9% | - |
| 🟡 | SigmoidFwdOp | test_sigmoid_manifest_bench[elementwise-256M-float16] | 0.3024 | 3.55 | 3.55 | torch 106.4%, torch-compile 86.0% | - |
| 🟡 | SigmoidFwdOp | test_sigmoid_manifest_bench[elementwise-256M-bfloat16] | 0.3062 | 3.51 | 3.51 | torch 107.6%, torch-compile 86.0% | - |
| 🟡 | SignFwdOp | test_sign_bench[elementwise-16M-float16] | 0.0186 | 1.80 | 3.61 | torch 97.6%, torch-compile 96.6% | - |
| 🟡 | SignFwdOp | test_sign_bench[elementwise-16M-bfloat16] | 0.0186 | 1.80 | 3.61 | torch 97.8%, torch-compile 96.7% | - |
| 🔵 | SignFwdOp | test_sign_bench[elementwise-16M-float32] | 0.0340 | 0.99 | 3.95 | torch 100.0%, torch-compile 100.0% | - |
| 🟡 | SignFwdOp | test_sign_bench[elementwise-256M-float16] | 0.2637 | 2.04 | 4.07 | torch 97.1%, torch-compile 95.2% | - |
| 🟡 | SignFwdOp | test_sign_bench[elementwise-256M-bfloat16] | 0.2636 | 2.04 | 4.07 | torch 98.1%, torch-compile 96.3% | - |
| 🔵 | SiluAndMulFwdOp | test_silu_and_mul_bench[llama-8b-swiglu-prefill-float16] | 0.0434 | 4.06 | 4.06 | flashinfer 122.7%, torch-ref 435.9%, torch-compile 101.9% | - |
| 🔵 | SiluAndMulFwdOp | test_silu_and_mul_bench[llama-8b-swiglu-prefill-bfloat16] | 0.0436 | 4.04 | 4.04 | flashinfer 123.6%, torch-ref 436.4%, torch-compile 104.8% | - |
| 🟡 | SiluAndMulFwdOp | test_silu_and_mul_bench[llama-8b-swiglu-decode-bfloat16] | 0.0017 | 0.05 | 0.05 | flashinfer 248.2%, torch-ref 201.8%, torch-compile 83.3% | - |
| 🟡 | SiluFwdOp | test_silu_manifest_bench[llama-8b-ffn-prefill-float16] | 0.0367 | 4.00 | 3.20 | torch 104.4%, torch-compile 97.5% | - |
| 🟡 | SiluFwdOp | test_silu_manifest_bench[llama-8b-ffn-prefill-bfloat16] | 0.0367 | 4.00 | 3.20 | torch 103.8%, torch-compile 97.8% | - |
| 🟡 | SiluFwdOp | test_silu_manifest_bench[llama-8b-ffn-decode-bfloat16] | 0.0015 | 0.05 | 0.04 | torch 129.1%, torch-compile 89.6% | - |
| 🔵 | SinFwdOp | test_sin_bench[elementwise-16M-float16] | 0.0253 | 0.66 | 2.65 | torch 103.4%, torch-compile 104.6% | - |
| 🔵 | SinFwdOp | test_sin_bench[elementwise-16M-bfloat16] | 0.0259 | 0.65 | 2.59 | torch 103.8%, torch-compile 104.3% | - |
| 🟡 | SinFwdOp | test_sin_bench[elementwise-16M-float32] | 0.0349 | 0.48 | 3.85 | torch 98.4%, torch-compile 98.4% | - |
| 🔵 | SinFwdOp | test_sin_bench[elementwise-256M-float16] | 0.3664 | 0.73 | 2.93 | torch 103.0%, torch-compile 104.9% | - |
| 🔵 | SinFwdOp | test_sin_bench[elementwise-256M-bfloat16] | 0.3746 | 0.72 | 2.87 | torch 103.1%, torch-compile 104.6% | - |
| 🔵 | SinusoidalFwdOp | test_sinusoidal_bench[transformer-2k-4k-float16] | 0.0425 | 1.18 | 0.39 | torch-ref 250.1%, torch-compile 133.4% | - |
| 🔵 | SinusoidalFwdOp | test_sinusoidal_bench[transformer-2k-4k-bfloat16] | 0.0425 | 1.18 | 0.39 | torch-ref 250.3%, torch-compile 133.4% | - |
| 🔵 | SinusoidalFwdOp | test_sinusoidal_bench[transformer-4k-4k-float16] | 0.0819 | 1.23 | 0.41 | torch-ref 243.2%, torch-compile 136.4% | - |
| 🔵 | SinusoidalFwdOp | test_sinusoidal_bench[transformer-4k-4k-bfloat16] | 0.0819 | 1.23 | 0.41 | torch-ref 243.4%, torch-compile 136.3% | - |
| 🔵 | SoftmaxFwdOp | test_softmax_bench[attn-weights-4k-float16] | 0.0084 | 2.49 | 1.99 | flaggems 102.3%, torch 235.0%, torch-compile 191.6% | - |
| 🔵 | SoftmaxFwdOp | test_softmax_bench[attn-weights-4k-bfloat16] | 0.0084 | 2.49 | 1.99 | flaggems 103.0%, torch 233.5%, torch-compile 198.1% | - |
| 🔵 | SoftmaxFwdOp | test_softmax_bench[attn-weights-4k-float32] | 0.0110 | 1.91 | 3.05 | flaggems 100.6%, torch 183.7%, torch-compile 168.0% | - |
| 🔵 | SoftmaxFwdOp | test_softmax_bench[attn-weights-32k-bfloat16] | 0.0615 | 2.73 | 2.18 | flaggems 104.5%, torch 135.9%, torch-compile 153.5% | - |
| 🔴 | SoftmaxFwdOp | test_softmax_bench[lm-head-logits-float16] | 0.0284 | 0.07 | 0.06 | flaggems 99.4%, torch 116.3%, torch-compile 32.2% | - |
| 🔴 | SoftmaxFwdOp | test_softmax_bench[lm-head-logits-bfloat16] | 0.0308 | 0.07 | 0.05 | flaggems 96.5%, torch 109.8%, torch-compile 29.7% | - |
| 🔴 | SoftmaxFwdOp | test_softmax_bench[lm-head-logits-float32] | 0.0348 | 0.06 | 0.09 | flaggems 89.8%, torch 113.2%, torch-compile 28.3% | - |
| 🔵 | SoftplusFwdOp | test_softplus_manifest_bench[mlp-hidden-float16] | 0.0126 | 3.33 | 2.66 | torch 189.2%, torch-compile 142.1% | - |
| 🔵 | SoftplusFwdOp | test_softplus_manifest_bench[mlp-hidden-bfloat16] | 0.0128 | 3.28 | 2.62 | torch 188.5%, torch-compile 142.8% | - |
| 🔵 | SoftplusFwdOp | test_softplus_manifest_bench[mlp-hidden-wide-float16] | 0.0229 | 3.67 | 2.93 | torch 195.2%, torch-compile 143.5% | - |
| 🔵 | SoftplusFwdOp | test_softplus_manifest_bench[mlp-hidden-wide-bfloat16] | 0.0232 | 3.62 | 2.89 | torch 195.4%, torch-compile 146.4% | - |
| 🔵 | SqrtFwdOp | test_sqrt_bench[elementwise-16M-float16] | 0.0186 | 0.90 | 3.61 | torch 101.6%, torch-compile 100.2% | - |
| 🔵 | SqrtFwdOp | test_sqrt_bench[elementwise-16M-bfloat16] | 0.0187 | 0.90 | 3.60 | torch 101.7%, torch-compile 100.3% | - |
| 🔵 | SqrtFwdOp | test_sqrt_bench[elementwise-16M-float32] | 0.0333 | 0.50 | 4.03 | torch 101.9%, torch-compile 101.9% | - |
| 🔵 | SqrtFwdOp | test_sqrt_bench[elementwise-256M-float16] | 0.2628 | 1.02 | 4.09 | torch 101.2%, torch-compile 100.1% | - |
| 🔵 | SqrtFwdOp | test_sqrt_bench[elementwise-256M-bfloat16] | 0.2637 | 1.02 | 4.07 | torch 101.3%, torch-compile 100.2% | - |
| 🔵 | StdFwdOp | test_std_bench[hidden-state-std-float16] | 0.0084 | 4.97 | 1.99 | flaggems 125.4%, torch 800.8%, torch-compile 222.3% | - |
| 🔵 | StdFwdOp | test_std_bench[hidden-state-std-bfloat16] | 0.0085 | 4.93 | 1.97 | flaggems 130.4%, torch 799.4%, torch-compile 226.3% | - |
| 🔵 | StdFwdOp | test_std_bench[long-seq-std-bfloat16] | 0.0052 | 2.02 | 0.81 | flaggems 254.3%, torch 479.6%, torch-compile 122.8% | - |
| 🔴 | StdFwdOp | test_std_bench[3d-multidim-reduce-float16] | 0.0121 | 0.87 | 0.35 | flaggems 118.3%, torch 223.5%, torch-compile 53.3% | - |
| 🔵 | SubFwdOp | test_binary_arith_bench[sub-1024x4096-float16-float16-SubFwdOp-sub-normal] | 0.0084 | 0.50 | 3.00 | torch 101.0%, torch-compile 100.2% | - |
| 🔵 | SubFwdOp | test_binary_arith_bench[sub-1024x10240-float16-float16-SubFwdOp-sub-normal] | 0.0176 | 0.60 | 3.57 | torch 100.6%, torch-compile 100.2% | - |
| 🟡 | SubFwdOp | test_binary_arith_bench[sub-1024x11008-float16-float16-SubFwdOp-sub-normal] | 0.0186 | 0.61 | 3.64 | torch 100.2%, torch-compile 99.8% | - |
| 🔵 | SubFwdOp | test_sub_manifest_bench[hidden-state-prefill-float16] | 0.0148 | 1.13 | 3.40 | torch 100.2%, torch-compile 100.2% | - |
| 🔵 | SubFwdOp | test_sub_manifest_bench[hidden-state-prefill-bfloat16] | 0.0148 | 1.13 | 3.40 | torch 100.4%, torch-compile 100.0% | - |
| 🟡 | SubFwdOp | test_sub_manifest_bench[hidden-state-prefill-float32] | 0.0265 | 0.63 | 3.80 | torch 99.9%, torch-compile 99.9% | - |
| 🔵 | SubFwdOp | test_sub_manifest_bench[cnn-feat-broadcast-float16] | 0.0144 | 1.78 | 3.56 | torch 317.7%, torch-compile 100.1% | - |
| 🔵 | SubFwdOp | test_sub_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0145 | 1.77 | 3.54 | torch 320.3%, torch-compile 100.2% | - |
| 🔵 | SubFwdOp | test_sub_manifest_bench[cnn-feat-broadcast-float32] | 0.0265 | 0.97 | 3.88 | torch 186.3%, torch-compile 100.0% | - |
| 🔵 | SumFwdOp | test_sum_bench[hidden-state-reduce-float16] | 0.0074 | 1.13 | 2.26 | flaggems 118.1%, torch 666.0%, torch-compile 112.5% | - |
| 🔵 | SumFwdOp | test_sum_bench[hidden-state-reduce-bfloat16] | 0.0074 | 1.13 | 2.26 | flaggems 118.5%, torch 673.9%, torch-compile 113.4% | - |
| 🟡 | SumFwdOp | test_sum_bench[long-seq-reduce-bfloat16] | 0.0041 | 0.52 | 1.03 | flaggems 93.7%, torch 416.5%, torch-compile 115.0% | - |
| 🟡 | SumFwdOp | test_sum_bench[hidden-state-reduce-dim0-bfloat16] | 0.0122 | 0.69 | 1.38 | flaggems 112.4%, torch 367.0%, torch-compile 91.6% | - |
| 🔵 | SumFwdOp | test_sum_bench[hidden-state-reduce-keepdim-bfloat16] | 0.0074 | 1.13 | 2.26 | flaggems 118.5%, torch 672.0%, torch-compile 113.4% | - |
| 🟡 | SumFwdOp | test_sum_bench[3d-multidim-reduce-float16] | 0.0057 | 0.37 | 0.73 | flaggems 235.2%, torch 336.9%, torch-compile 83.8% | - |
| 🟡 | TanhFwdOp | test_tanh_manifest_bench[elementwise-16M-float16] | 0.0208 | 0.81 | 3.22 | torch 99.5%, torch-compile 116.0% | - |
| 🔵 | TanhFwdOp | test_tanh_manifest_bench[elementwise-16M-bfloat16] | 0.0213 | 0.79 | 3.15 | torch 102.6%, torch-compile 115.3% | - |
| 🔵 | TanhFwdOp | test_tanh_manifest_bench[elementwise-16M-float32] | 0.0339 | 0.50 | 3.96 | torch 100.5%, torch-compile 101.6% | - |
| 🟡 | TanhFwdOp | test_tanh_manifest_bench[elementwise-256M-float16] | 0.2964 | 0.91 | 3.62 | torch 98.7%, torch-compile 115.9% | - |
| 🔵 | TanhFwdOp | test_tanh_manifest_bench[elementwise-256M-bfloat16] | 0.3026 | 0.89 | 3.55 | torch 102.4%, torch-compile 115.6% | - |
| 🔴 | TopkSelectorFwdOp | test_topk_selector_bench[topk1024-s32k-kv64k-float32] | 15.6143 | 0.14 | 0.56 | torch 203.9%, torch-compile 203.9%, flashinfer 59.4% | - |
| 🔴 | TopkSelectorFwdOp | test_topk_selector_bench[topk2048-s32k-kv64k-float32] | 16.2322 | 0.13 | 0.55 | torch 205.2%, torch-compile 205.2%, flashinfer 65.7% | - |
| 🔵 | TruncFwdOp | test_trunc_bench[elementwise-16M-float16] | 0.0179 | 0.94 | 3.75 | torch 100.4%, torch-compile 100.4% | - |
| 🔵 | TruncFwdOp | test_trunc_bench[elementwise-16M-bfloat16] | 0.0179 | 0.94 | 3.75 | torch 100.4%, torch-compile 100.2% | - |
| 🟡 | TruncFwdOp | test_trunc_bench[elementwise-16M-float32] | 0.0340 | 0.49 | 3.95 | torch 100.0%, torch-compile 99.9% | - |
| 🟡 | TruncFwdOp | test_trunc_bench[elementwise-256M-float16] | 0.2499 | 1.07 | 4.30 | torch 100.1%, torch-compile 99.8% | - |
| 🔵 | TruncFwdOp | test_trunc_bench[elementwise-256M-bfloat16] | 0.2499 | 1.07 | 4.30 | torch 100.1%, torch-compile 100.3% | - |
| 🟢 | VarFwdOp | test_var_bench[hidden-state-var-float16] | 0.0083 | 5.04 | 2.02 | flaggems 180.4%, torch 813.5%, torch-compile 219.6% | - |
| 🟢 | VarFwdOp | test_var_bench[hidden-state-var-bfloat16] | 0.0084 | 5.00 | 2.00 | flaggems 184.0%, torch 811.4%, torch-compile 223.7% | - |
| 🔵 | VarFwdOp | test_var_bench[long-seq-var-bfloat16] | 0.0052 | 2.04 | 0.81 | flaggems 215.5%, torch 482.0%, torch-compile 118.0% | - |
| 🔴 | VarFwdOp | test_var_bench[3d-multidim-reduce-float16] | 0.0120 | 0.87 | 0.35 | flaggems 117.3%, torch 223.9%, torch-compile 50.0% | - |
| 🟢 | VarMeanFwdOp | test_var_mean_bench[hidden-state-var-mean-float16] | 0.0084 | 5.00 | 2.00 | flaggems 179.6%, torch 1388.5%, torch-compile 250.0% | - |
| 🟢 | VarMeanFwdOp | test_var_mean_bench[hidden-state-var-mean-bfloat16] | 0.0084 | 4.98 | 1.99 | flaggems 184.4%, torch 1389.9%, torch-compile 260.1% | - |
| 🔵 | VarMeanFwdOp | test_var_mean_bench[long-seq-var-mean-bfloat16] | 0.0052 | 2.04 | 0.81 | flaggems 216.2%, torch 787.0%, torch-compile 145.3% | - |
| 🔴 | VarMeanFwdOp | test_var_mean_bench[3d-multidim-reduce-float16] | 0.0121 | 0.86 | 0.35 | flaggems 116.9%, torch 372.1%, torch-compile 62.3% | - |
| 🟡 | WhereFwdOp | test_where_manifest_bench[elementwise-16M-float16] | 0.0309 | 0.54 | 3.80 | torch 99.6%, torch-compile 99.3% | - |
| 🟡 | WhereFwdOp | test_where_manifest_bench[elementwise-16M-bfloat16] | 0.0311 | 0.54 | 3.78 | torch 98.8%, torch-compile 98.7% | - |
| 🟡 | WhereFwdOp | test_where_manifest_bench[elementwise-16M-float32] | 0.0536 | 0.31 | 4.07 | torch 99.3%, torch-compile 98.7% | - |
| 🟡 | WhereFwdOp | test_where_manifest_bench[elementwise-256M-float16] | 0.4290 | 0.63 | 4.38 | torch 99.8%, torch-compile 99.8% | - |
| 🟡 | WhereFwdOp | test_where_manifest_bench[elementwise-256M-bfloat16] | 0.4286 | 0.63 | 4.38 | torch 99.9%, torch-compile 99.9% | - |
| 🟡 | div_bcast | test_broadcast_bench[div-1024x4096-1x4096-float16-DivFwdOp-div-positive] | 0.0065 | 0.65 | 2.60 | torch 251.5%, torch-compile 96.0% | - |
| 🟡 | div_bcast | test_broadcast_bench[div-1024x10240-1x10240-float16-DivFwdOp-div-positive] | 0.0133 | 0.79 | 3.14 | torch 271.9%, torch-compile 92.6% | - |
| 🟡 | div_bcast | test_broadcast_bench[div-1024x11008-1x11008-float16-DivFwdOp-div-positive] | 0.0141 | 0.80 | 3.19 | torch 273.8%, torch-compile 92.5% | - |
| 🔴 | gelu_and_mul_strategy | test_fused_gated_strategy_bench[gelu_and_mul-1024-4096-float16-GeluAndMulFwdKernel-direct] | 0.0182 | 0.46 | 1.38 | torch 183.6%, torch-compile 58.6% | - |
| 🔵 | gelu_and_mul_strategy | test_fused_gated_strategy_bench[gelu_and_mul-1024-4096-float16-GeluAndMulFwdKernel-explicit_parallel] | 0.0100 | 0.84 | 2.51 | torch 333.6%, torch-compile 106.4% | - |
| 🔴 | gelu_tanh_and_mul_strategy | test_fused_gated_strategy_bench[gelu_tanh_and_mul-1024-4096-float16-GeluTanhAndMulFwdKernel-direct] | 0.0178 | 0.47 | 1.42 | torch 179.8%, torch-compile 54.9% | - |
| 🔵 | gelu_tanh_and_mul_strategy | test_fused_gated_strategy_bench[gelu_tanh_and_mul-1024-4096-float16-GeluTanhAndMulFwdKernel-explicit_parallel] | 0.0088 | 0.95 | 2.85 | torch 361.2%, torch-compile 110.5% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-up-T=32768] | 18.3029 | 720.88 | 1.00 | torch 127.0%, deepgemm 101.6%, triton 149.6%, triton-tma 126.0% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-up-T=65536] | 37.7019 | 699.92 | 0.63 | torch 108.7%, deepgemm 109.1%, triton 144.8%, triton-tma 113.9% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-up-T=131072] | 75.1731 | 702.07 | 0.46 | torch 107.3%, deepgemm 101.8%, triton 141.9%, triton-tma 112.8% | - |
| 🟡 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-up-T=262144] | 153.0160 | 689.82 | 0.36 | torch 113.3%, deepgemm 99.5%, triton 140.1%, triton-tma 110.9% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[Llama4-128E-up-T=131072] | 31.0985 | 707.12 | 0.87 | torch 104.2%, deepgemm 100.1%, triton 165.0%, triton-tma 129.2% | - |
| 🟡 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[qwen3.5-397B-up-T52429] | 12.6749 | 693.98 | 1.19 | torch 106.1%, deepgemm 98.8%, triton 152.5%, triton-tma 139.5% | - |
| 🟡 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-down-T=32768] | 9.6973 | 680.30 | 1.11 | torch 102.8%, deepgemm 98.7%, triton 151.2%, triton-tma 116.3% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-down-T=65536] | 19.1386 | 689.40 | 0.79 | torch 125.7%, deepgemm 100.9%, triton 150.9%, triton-tma 110.2% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-down-T=131072] | 38.3860 | 687.45 | 0.62 | torch 112.7%, deepgemm 113.5%, triton 150.4%, triton-tma 113.9% | - |
| 🟡 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-down-T=262144] | 78.0244 | 676.41 | 0.52 | torch 106.0%, deepgemm 99.9%, triton 147.6%, triton-tma 107.9% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[Llama4-128E-down-T=131072] | 15.2156 | 722.62 | 0.94 | torch 105.8%, deepgemm 102.9%, triton 153.2%, triton-tma 122.5% | - |
| 🟡 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[qwen3.5-397B-down-T52429] | 6.9340 | 634.27 | 1.39 | torch 108.6%, deepgemm 96.9%, triton 147.8%, triton-tma 128.1% | - |
| 🔴 | grouped_gemm_nn | test_grouped_gemm_bench[nn-batch16-m4096-n4096-k4096-float16] | 0.3408 | 403.26 | 1.77 | torch-ref 90.0%, torch-compile 80.6%, torch 78.9% | - |
| 🔵 | grouped_gemm_nt | test_grouped_gemm_bench[nt-batch16-m4096-n4096-k4096-float16] | 0.2322 | 591.84 | 2.60 | torch-ref 1002.5%, torch-compile 988.3%, torch 115.6% | - |
| 🟡 | grouped_gemm_nt | test_grouped_gemm_bench[nt-batch16-m4096-n4096-k4096-bfloat16] | 0.2264 | 607.02 | 2.67 | torch-ref 1007.9%, torch-compile 992.9%, torch 99.6% | - |
| 🔴 | grouped_gemm_tn | test_grouped_gemm_bench[tn-batch16-m4096-n4096-k4096-float16] | 0.7828 | 175.58 | 0.77 | torch-ref 66.9%, torch-compile 66.8%, torch 45.3% | - |
| 🔵 | mul_bcast | test_broadcast_bench[mul-1024x4096-1x4096-float16-MulFwdOp-mul-normal] | 0.0060 | 0.70 | 2.82 | torch 250.5%, torch-compile 101.6% | - |
| 🔵 | mul_bcast | test_broadcast_bench[mul-1024x10240-1x10240-float16-MulFwdOp-mul-normal] | 0.0123 | 0.85 | 3.42 | torch 268.8%, torch-compile 100.3% | - |
| 🔵 | mul_bcast | test_broadcast_bench[mul-1024x11008-1x11008-float16-MulFwdOp-mul-normal] | 0.0129 | 0.87 | 3.49 | torch 272.9%, torch-compile 100.2% | - |
| 🔴 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float16-SiluAndMulFwdKernel-direct] | 0.0178 | 0.47 | 1.41 | torch 177.0%, torch-compile 46.7% | - |
| 🔴 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-11008-float16-SiluAndMulFwdKernel-direct] | 0.0450 | 0.50 | 1.50 | torch 171.0%, torch-compile 42.4% | - |
| 🔴 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-4096-4096-float16-SiluAndMulFwdKernel-direct] | 0.0662 | 0.51 | 1.52 | torch 168.1%, torch-compile 40.7% | - |
| 🔴 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-bfloat16-SiluAndMulFwdKernel-direct] | 0.0178 | 0.47 | 1.41 | torch 178.3%, torch-compile 47.3% | - |
| 🔴 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float32-SiluAndMulFwdKernel-direct] | 0.0200 | 0.42 | 2.51 | torch 173.3%, torch-compile 76.4% | - |
| 🟡 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float16-SiluAndMulFwdKernel-explicit_parallel] | 0.0084 | 0.99 | 2.98 | torch 373.1%, torch-compile 98.5% | - |
| 🔵 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-11008-float16-SiluAndMulFwdKernel-explicit_parallel] | 0.0188 | 1.20 | 3.59 | torch 408.0%, torch-compile 101.2% | - |
| 🔵 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-4096-4096-float16-SiluAndMulFwdKernel-explicit_parallel] | 0.0267 | 1.26 | 3.78 | torch 417.5%, torch-compile 101.1% | - |
| 🔵 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-bfloat16-SiluAndMulFwdKernel-explicit_parallel] | 0.0084 | 1.00 | 2.99 | torch 377.6%, torch-compile 100.0% | - |
| 🔵 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float32-SiluAndMulFwdKernel-explicit_parallel] | 0.0148 | 0.57 | 3.40 | torch 234.3%, torch-compile 103.2% | - |
| 🔵 | sub_bcast | test_broadcast_bench[sub-1024x4096-1x4096-float16-SubFwdOp-sub-normal] | 0.0058 | 0.72 | 2.90 | torch 258.0%, torch-compile 102.2% | - |
| 🔵 | sub_bcast | test_broadcast_bench[sub-1024x10240-1x10240-float16-SubFwdOp-sub-normal] | 0.0122 | 0.86 | 3.44 | torch 272.3%, torch-compile 100.3% | - |
| 🔵 | sub_bcast | test_broadcast_bench[sub-1024x11008-1x11008-float16-SubFwdOp-sub-normal] | 0.0130 | 0.87 | 3.47 | torch 272.7%, torch-compile 100.0% | - |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 9 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 735 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 2542 lines in `ops/`, 39.4% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 3518 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

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
| `ops/attention/gqa.py` | 507 | 38.4% |
| `ops/moe/staged.py` | 137 | 19.9% |
| `ops/pool.py` | 135 | 76.4% |
| `ops/moe/contracts.py` | 134 | 43.5% |
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

</details>

Per-line detail is in the `htmlcov/` directory of this run's `tileops_op_test` artifact.
