# ✅ TileOPs Nightly Report

> **2026-08-22 19:15** &ensp;|&ensp; `52dbc08` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Correctness** | ✅ &ensp; (513/513 tests across 92 ops) |
| **Benchmarked Ops** | 191 |
| **Benchmark Failures** | ✅ None &ensp;|&ensp; ⚠️ 13 skipped |
| **Regressions** (vs 14-day best) | ✅ None |
| **Baseline Alerts** (< 80%) | ⚠️ 261 |
| **Never-built kernels** | ⚠️ 9 files &ensp;·&ensp; `kernels/attention/deepseek_mla_decode.py` at 5.8% |
| **Untested roofline math** | 735 lines in `perf/` &ensp;·&ensp; `perf/formulas.py` at 13.1% |
| **Untested op logic** | 2164 lines in `ops/` **−1** &ensp;·&ensp; 43.5% of branches taken **−0.1pp** |
| | <sub>coverage compared against the 2026-08-22 run; no figure means it held</sub> |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 80%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-gate-up-block128-float8_e4m3fn] | 0.3336 | 0.0129 | 3.9% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **CumprodFwdOp** | test_cumprod_bench[long-seq-scan-bfloat16] | 0.2501 | 0.0122 | 4.9% | torch-compile |
| 🔴 | **ProdFwdOp** | test_prod_bench[hidden-state-reduce-bfloat16] | 0.0999 | 0.0078 | 7.8% | flaggems |
| 🔴 | **ProdFwdOp** | test_prod_bench[hidden-state-reduce-float16] | 0.0989 | 0.0079 | 8.0% | flaggems |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-gate-up-block128-float8_e4m3fn] | 1.3499 | 0.1393 | 10.3% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[gemv-down-m1-block128-float8_e4m3fn] | 0.0628 | 0.0078 | 12.4% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **SumFwdOp** | test_sum_bench[hidden-state-reduce-dim0-bfloat16] | 0.0686 | 0.0111 | 16.2% | torch-compile |
| 🔴 | **SharedFusedMoE** | test_shared_fused_moe_bench[1-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 2.5266 | 0.4268 | 16.9% | vllm |
| 🔴 | **AnyFwdOp** | test_any_bench[3d-multidim-reduce-bool] | 0.0214 | 0.0038 | 17.6% | torch-compile |
| 🔴 | **AllFwdOp** | test_all_bench[3d-multidim-reduce-bool] | 0.0217 | 0.0044 | 20.1% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[k-dominant-7168x16384-block128-float8_e4m3fn] | 3.6193 | 0.7704 | 21.3% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **InfNormFwdOp** | test_inf_norm_bench[3d-multidim-reduce-float16] | 0.0216 | 0.0049 | 22.7% | torch-compile |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[large-spatial-float16] | 4.3427 | 1.0182 | 23.4% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-down-block128-float8_e4m3fn] | 0.0391 | 0.0093 | 23.7% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **CumsumFwdOp** | test_cumsum_bench[hidden-state-scan-float16] | 0.0445 | 0.0106 | 23.7% | flaggems |
| 🔴 | **AnyFwdOp** | test_any_bench[mask-validation-4k-bool] | 0.0072 | 0.0017 | 24.1% | torch-compile |
| 🔴 | **AllFwdOp** | test_all_bench[mask-validation-4k-bool] | 0.0074 | 0.0018 | 24.1% | torch-compile |
| 🔴 | **CumsumFwdOp** | test_cumsum_bench[hidden-state-scan-bfloat16] | 0.0436 | 0.0105 | 24.2% | flaggems |
| 🔴 | **GemmFwdOp** | test_gemm_bench[mid-m96-gate-up-bfloat16] | 0.0687 | 0.0169 | 24.6% | torch-cublas |
| 🔴 | **InfNormFwdOp** | test_inf_norm_bench[hidden-state-inf-float16] | 0.0301 | 0.0077 | 25.5% | flaggems |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-decode-gate-up-bfloat16] | 0.0677 | 0.0173 | 25.5% | torch-cublas |
| 🔴 | **InfNormFwdOp** | test_inf_norm_bench[hidden-state-inf-bfloat16] | 0.0306 | 0.0079 | 25.8% | flaggems |
| 🔴 | **ProdFwdOp** | test_prod_bench[long-seq-reduce-bfloat16] | 0.0172 | 0.0045 | 26.2% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-attn-proj-block128-float8_e4m3fn] | 0.8094 | 0.2144 | 26.5% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[lm-head-logits-float32] | 0.0365 | 0.0098 | 26.9% | torch-compile |
| 🔴 | **LogSoftmaxFwdOp** | test_log_softmax_bench[lm-head-logits-float32] | 0.0366 | 0.0099 | 27.0% | torch-compile |
| 🔴 | **CumsumFwdOp** | test_cumsum_bench[long-seq-scan-bfloat16] | 0.0295 | 0.0080 | 27.1% | flaggems |
| 🔴 | **MaxPool1dFwdOp** | test_max_pool1d_bench[textcnn-global-float16] | 0.0134 | 0.0037 | 27.6% | torch-compile |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c128-b64-complex128] | 0.0305 | 0.0085 | 27.8% | torch-cufft |
| 🔴 | **InfNormFwdOp** | test_inf_norm_bench[long-seq-inf-bfloat16] | 0.0177 | 0.0050 | 28.0% | torch-compile |
| 🔴 | **Conv3dFwdOp** | test_conv3d_bench[3d-unet-aspp-3x3x3-rate6-float16] | 0.1269 | 0.0376 | 29.6% | torch-compile |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b4-dmem1024-d512-float16] | 0.0827 | 0.0255 | 30.8% | torch-compile |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-stage2-float16] | 0.0107 | 0.0033 | 30.8% | torch-compile |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[lm-head-logits-bfloat16] | 0.0311 | 0.0096 | 30.9% | torch-compile |
| 🔴 | **AnyFwdOp** | test_any_bench[mask-validation-32k-bool] | 0.0106 | 0.0033 | 31.1% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-down-block128-float8_e4m3fn] | 0.4475 | 0.1430 | 31.9% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **AllFwdOp** | test_all_bench[mask-validation-32k-bool] | 0.0106 | 0.0034 | 32.1% | torch-compile |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[lm-head-logits-float16] | 0.0298 | 0.0096 | 32.3% | torch-compile |
| 🔴 | **Conv3dFwdOp** | test_conv3d_bench[unet-encoder-k3-s1-bfloat16] | 0.3539 | 0.1151 | 32.5% | torch |
| 🔴 | **LogSoftmaxFwdOp** | test_log_softmax_bench[lm-head-logits-float16] | 0.0287 | 0.0097 | 33.8% | torch-compile |
| 🔴 | **Conv3dFwdOp** | test_conv3d_bench[unet-encoder-k3-s1-bias-bfloat16] | 0.3538 | 0.1220 | 34.5% | torch-compile |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-stage3-float16] | 0.0129 | 0.0046 | 35.6% | torch-compile |
| 🔴 | **MaximumFwdOp** | test_maximum_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0396 | 0.0142 | 35.9% | torch-compile |
| 🔴 | **LogSoftmaxFwdOp** | test_log_softmax_bench[lm-head-logits-bfloat16] | 0.0269 | 0.0097 | 35.9% | torch-compile |
| 🔴 | **MinimumFwdOp** | test_minimum_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0396 | 0.0144 | 36.3% | torch-compile |
| 🔴 | **MinimumFwdOp** | test_minimum_manifest_bench[cnn-feat-broadcast-float16] | 0.0396 | 0.0144 | 36.4% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-bfloat16] | 0.4550 | 0.1658 | 36.4% | torch-sdpa |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-bfloat16] | 0.4558 | 0.1661 | 36.4% | torch-sdpa |
| 🔴 | **MaximumFwdOp** | test_maximum_manifest_bench[cnn-feat-broadcast-float16] | 0.0395 | 0.0144 | 36.5% | torch-compile |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-fc-float16] | 0.0061 | 0.0022 | 36.6% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[mid-m32-attn-bfloat16] | 0.0661 | 0.0244 | 36.8% | torch-cublas |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-b64-complex64] | 0.0152 | 0.0056 | 36.9% | torch-cufft |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[wide-n-24576-block128-float8_e4m3fn] | 1.0394 | 0.3833 | 36.9% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-2p7b-b2-s32k-dt-bias-float16] | 0.0600 | 0.0224 | 37.3% | mamba |
| 🔴 | **GemmFwdOp** | test_gemm_bench[mid-m16-attn-bfloat16] | 0.0657 | 0.0245 | 37.3% | torch-cublas |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-stage1-float16] | 0.0109 | 0.0041 | 37.7% | torch-compile |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[mha-decode-b32-pv-per-tensor-float8_e4m3fn] | 0.0646 | 0.0250 | 38.6% | flashinfer-bmm-fp8 |
| 🔴 | **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[textcnn-global-float16] | 0.0193 | 0.0076 | 39.1% | torch-compile |
| 🔴 | **SumFwdOp** | test_sum_bench[3d-multidim-reduce-float16] | 0.0115 | 0.0045 | 39.3% | torch-compile |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b1-dmem512-d256-float16] | 0.0329 | 0.0131 | 39.8% | torch-compile |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-4096-4096-float16-SiluAndMulFwdKernel-direct] | 0.0662 | 0.0269 | 40.6% | torch-compile |
| 🔴 | **ArgminFwdOp** | test_argmin_bench[hidden-state-argmin-bfloat16] | 0.0240 | 0.0098 | 40.9% | flaggems |
| 🔴 | **L1NormFwdOp** | test_l1_norm_bench[3d-multidim-reduce-float16] | 0.0113 | 0.0046 | 41.0% | torch-compile |
| 🔴 | **CountNonzeroFwdOp** | test_count_nonzero_bench[3d-multidim-reduce-float16] | 0.0115 | 0.0047 | 41.1% | torch-compile |
| 🔴 | **ArgminFwdOp** | test_argmin_bench[hidden-state-argmin-float16] | 0.0239 | 0.0099 | 41.4% | flaggems |
| 🔴 | **L2NormFwdOp** | test_l2_norm_bench[3d-multidim-reduce-float16] | 0.0114 | 0.0047 | 41.4% | torch-compile |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-bfloat16] | 0.0154 | 0.0064 | 41.6% | mamba |
| 🔴 | **MeanFwdOp** | test_mean_bench[3d-multidim-reduce-float16] | 0.0115 | 0.0048 | 41.8% | torch-compile |
| 🔴 | **AmaxFwdOp** | test_amax_bench[3d-multidim-reduce-float16] | 0.0115 | 0.0049 | 42.2% | torch-compile |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-1024-11008-float16-SiluAndMulFwdKernel-direct] | 0.0450 | 0.0191 | 42.4% | torch-compile |
| 🔴 | **AminFwdOp** | test_amin_bench[3d-multidim-reduce-float16] | 0.0115 | 0.0049 | 42.5% | torch-compile |
| 🔴 | **MaxPool3dIndicesFwdOp** | test_max_pool3d_indices_bench[c3d-pool1-float16] | 0.3045 | 0.1294 | 42.5% | torch-compile |
| 🔴 | **RopeNeoxPositionIdsFwdOp** | test_rope_neox_position_ids_bench[position-ids-s2k-h32-d128-float16] | 0.0278 | 0.0119 | 42.6% | torch-compile |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[mha-decode-b64-qk-per-tensor-float8_e4m3fn] | 0.1154 | 0.0496 | 43.0% | flashinfer-bmm-fp8 |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-dt-bias-bfloat16] | 0.0149 | 0.0064 | 43.0% | mamba |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-short-bfloat16] | 0.4145 | 0.1794 | 43.3% | torch-sdpa |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-short-bfloat16] | 0.4082 | 0.1789 | 43.8% | torch-sdpa |
| 🔴 | **SharedFusedMoE** | test_shared_fused_moe_bench[4096-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 32.5771 | 14.6897 | 45.1% | vllm |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float16-SiluAndMulFwdKernel-direct] | 0.0178 | 0.0083 | 46.7% | torch-compile |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-bfloat16-SiluAndMulFwdKernel-direct] | 0.0178 | 0.0084 | 47.2% | torch-compile |
| 🔴 | **ArgmaxFwdOp** | test_argmax_bench[hidden-state-argmax-bfloat16] | 0.0240 | 0.0116 | 48.6% | flaggems |
| 🔴 | **RopeNeoxPositionIdsFwdOp** | test_rope_neox_position_ids_bench[position-ids-s4k-h32-d128-bfloat16] | 0.0455 | 0.0223 | 49.0% | torch-compile |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-long-k-pressure-float16] | 0.2833 | 0.1409 | 49.7% | marlin-fp16 |
| 🔴 | **GemmFwdOp** | test_gemm_bench[square-1k-nn-bfloat16] | 0.0144 | 0.0072 | 49.8% | torch-cublas |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-small-bfloat16] | 0.0395 | 0.0197 | 50.0% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[square-1k-nn-float16] | 0.0145 | 0.0072 | 50.0% | torch-cublas |
| 🔴 | **GemmFwdOp** | test_gemm_bench[wide-n-24576-bfloat16] | 0.8996 | 0.4514 | 50.2% | torch-cublas |
| 🔴 | **ArgmaxFwdOp** | test_argmax_bench[hidden-state-argmax-float16] | 0.0239 | 0.0122 | 50.9% | flaggems |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-bfloat16] | 1.3119 | 0.6799 | 51.8% | torch-sdpa |
| 🔴 | **VarFwdOp** | test_var_bench[3d-multidim-reduce-float16] | 0.0120 | 0.0062 | 52.1% | torch-compile |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[compile-smoke-rect-128x256x256-float16] | 0.0059 | 0.0031 | 52.5% | torch-dequantized-matmul |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-gate-up-bfloat16] | 0.3369 | 0.1774 | 52.7% | torch-cublas |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-decode-down-bfloat16] | 0.0247 | 0.0132 | 53.4% | torch-cublas |
| 🔴 | **StdFwdOp** | test_std_bench[3d-multidim-reduce-float16] | 0.0120 | 0.0064 | 53.6% | torch-compile |
| 🔴 | **BitwiseNotFwdOp** | test_bitwise_not_bench[elementwise-256M-int32] | 0.9381 | 0.5044 | 53.8% | torch-compile |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-float16] | 0.0196 | 0.0106 | 54.1% | torch-compile |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-non-power2-low-cta-float16] | 0.0746 | 0.0407 | 54.5% | marlin-fp16 |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-bfloat16] | 0.0195 | 0.0106 | 54.6% | torch-compile |
| 🔴 | **CumprodFwdOp** | test_cumprod_bench[hidden-state-scan-float16] | 0.0444 | 0.0242 | 54.6% | torch-compile |
| 🔴 | **gelu_tanh_and_mul_strategy** | test_fused_gated_strategy_bench[gelu_tanh_and_mul-1024-4096-float16-GeluTanhAndMulFwdKernel-direct] | 0.0178 | 0.0098 | 54.9% | torch-compile |
| 🔴 | **MaxPool3dIndicesFwdOp** | test_max_pool3d_indices_bench[c3d-pool2-float16] | 0.0589 | 0.0327 | 55.5% | torch-compile |
| 🔴 | **BitwiseNotFwdOp** | test_bitwise_not_bench[elementwise-16M-int32] | 0.0610 | 0.0339 | 55.6% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-down-bfloat16] | 0.3212 | 0.1790 | 55.7% | torch-cublas |
| 🔴 | **CumprodFwdOp** | test_cumprod_bench[hidden-state-scan-bfloat16] | 0.0436 | 0.0244 | 55.9% | torch-compile |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-bfloat16] | 1.2435 | 0.7062 | 56.8% | torch-sdpa |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-medium-bfloat16] | 0.0543 | 0.0313 | 57.7% | torch-compile |
| 🔴 | **gelu_and_mul_strategy** | test_fused_gated_strategy_bench[gelu_and_mul-1024-4096-float16-GeluAndMulFwdKernel-direct] | 0.0182 | 0.0107 | 58.4% | torch-compile |
| 🔴 | **RopeYarnFwdOp** | test_rope_yarn_bench[yarn-2d-b1-s8k-h32-d128-float16] | 0.0595 | 0.0348 | 58.6% | torch-compile |
| 🔴 | **RopeLlama31FwdOp** | test_rope_llama31_bench[llama31-2d-b1-s8k-h32-d128-float16] | 0.0594 | 0.0348 | 58.6% | torch-compile |
| 🔴 | **RopeLongRopeFwdOp** | test_rope_longrope_bench[longrope-2d-b1-s8k-h32-d128-float16] | 0.0594 | 0.0348 | 58.6% | torch-compile |
| 🔴 | **LogicalOrFwdOp** | test_logical_bench[logical_or-1024x10240-float16-LogicalOrFwdOp-logical_or] | 0.0171 | 0.0102 | 59.6% | torch-compile |
| 🔴 | **SharedFusedMoE** | test_shared_fused_moe_bench[2048-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 19.5214 | 11.6548 | 59.7% | vllm |
| 🔴 | **RopeNeoxFwdOp** | test_rope_neox_bench[neox-2d-b2-s2k-h32-d128-float16] | 0.0309 | 0.0185 | 59.8% | torch-compile |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[throughput-8b-p64-float16] | 0.2516 | 0.1507 | 59.9% | flashinfer |
| 🔴 | **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[ecg-cnn-dilated-bfloat16] | 0.0224 | 0.0134 | 59.9% | torch-compile |
| 🔴 | **SigmoidFwdOp** | test_sigmoid_manifest_bench[elementwise-256M-float16] | 0.4244 | 0.2602 | 61.3% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[k-dominant-7168x16384-bfloat16] | 2.0616 | 1.2663 | 61.4% | torch-cublas |
| 🔴 | **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[global-1x1-float16] | 0.0133 | 0.0082 | 61.5% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-attn-proj-bfloat16] | 0.5399 | 0.3322 | 61.5% | torch-cublas |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-float16] | 0.6347 | 0.3907 | 61.6% | fla |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-float16] | 0.1123 | 0.0692 | 61.6% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-bfloat16] | 1.1029 | 0.6796 | 61.6% | torch-sdpa |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-bfloat16] | 0.6374 | 0.3934 | 61.7% | fla |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-attn-proj-float16] | 0.5419 | 0.3346 | 61.8% | torch-cublas |
| 🔴 | **HardsigmoidFwdOp** | test_hardsigmoid_manifest_bench[mbv3-se-gate-bfloat16] | 0.0022 | 0.0013 | 61.8% | torch-compile |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-bfloat16] | 0.1122 | 0.0698 | 62.2% | torch-compile |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-hbm-streaming-threshold-float16] | 0.0607 | 0.0379 | 62.3% | marlin-fp32 |
| 🔴 | **LogicalAndFwdOp** | test_logical_bench[logical_and-1024x10240-float16-LogicalAndFwdOp-logical_and] | 0.0171 | 0.0109 | 63.5% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[mid-m64-down-bfloat16] | 0.0207 | 0.0132 | 63.7% | torch-cublas |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b8-dmem512-d256-bfloat16] | 0.0334 | 0.0213 | 63.8% | torch-compile |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[compile-smoke-square-64x64x128-float16] | 0.0043 | 0.0027 | 63.9% | torch-dequantized-matmul |
| 🔴 | **LogSumExpFwdOp** | test_logsumexp_bench[lm-head-logits-bfloat16] | 0.0164 | 0.0105 | 64.0% | torch-compile |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-float16] | 1.4280 | 0.9191 | 64.4% | fla |
| 🔴 | **SigmoidFwdOp** | test_sigmoid_manifest_bench[elementwise-16M-float16] | 0.0288 | 0.0186 | 64.6% | torch-compile |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-float32] | 0.0195 | 0.0127 | 64.8% | torch-compile |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-bfloat16] | 0.3160 | 0.2055 | 65.0% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-bfloat16] | 1.4648 | 0.9539 | 65.1% | fla |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-float16] | 0.3140 | 0.2050 | 65.3% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-float16] | 0.3808 | 0.2492 | 65.4% | fla |
| 🔴 | **VarMeanFwdOp** | test_var_mean_bench[3d-multidim-reduce-float16] | 0.0120 | 0.0079 | 65.7% | torch-compile |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-float16] | 0.2017 | 0.1337 | 66.3% | fla |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-float32] | 0.1074 | 0.0716 | 66.6% | torch-compile |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-unbatched-complex64] | 0.0082 | 0.0054 | 66.7% | torch-cufft |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-bfloat16] | 0.3876 | 0.2584 | 66.7% | fla |
| 🔴 | **GroupNormFwdOp** | test_group_norm_bench[wider-channel-g32-affine-float16] | 0.0060 | 0.0040 | 66.7% | flaggems |
| 🔴 | **AvgPool1dFwdOp** | test_avg_pool1d_bench[ceil-bfloat16] | 0.0035 | 0.0023 | 66.7% | torch-compile |
| 🔴 | **grouped_gemm_tn** | test_grouped_gemm_bench[tn-batch16-m4096-n4096-k4096-float16] | 0.7822 | 0.5217 | 66.7% | torch-compile |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-l2-resident-ish-float16] | 0.0328 | 0.0219 | 66.8% | marlin-fp32 |
| 🔴 | **GroupNormFwdOp** | test_group_norm_bench[tail-spatial-g16-affine-float16] | 0.0061 | 0.0041 | 66.8% | flaggems |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-bfloat16] | 0.7508 | 0.5020 | 66.9% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-float16] | 0.7237 | 0.4867 | 67.2% | fla |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0051 | 0.0034 | 67.3% | mamba |
| 🔴 | **HardsigmoidFwdOp** | test_hardsigmoid_manifest_bench[mbv3-se-gate-deep-bfloat16] | 0.0022 | 0.0015 | 67.7% | torch-compile |
| 🔴 | **AvgPool1dFwdOp** | test_avg_pool1d_bench[audio-downsample-float16] | 0.0062 | 0.0042 | 67.9% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-float16] | 0.2445 | 0.1660 | 67.9% | torch-sdpa |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-float16] | 0.2438 | 0.1658 | 68.0% | torch-sdpa |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-bfloat16] | 0.0970 | 0.0659 | 68.0% | fla |
| 🔴 | **ArgmaxFwdOp** | test_argmax_bench[3d-non-last-axis-argmax-float16] | 0.0056 | 0.0038 | 68.2% | flaggems |
| 🔴 | **HardsigmoidFwdOp** | test_hardsigmoid_manifest_bench[mbv3-se-gate-float16] | 0.0020 | 0.0014 | 68.2% | torch-compile |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-bfloat16] | 0.2050 | 0.1401 | 68.3% | fla |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 1.0173 | 0.7026 | 69.1% | torch-sdpa |
| 🔴 | **GroupNormFwdOp** | test_group_norm_no_affine_bench[tail-spatial-g16-float16] | 0.0052 | 0.0036 | 69.3% | flaggems |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[moe-prefill-b128-per-tensor-float8_e4m3fn] | 0.9008 | 0.6251 | 69.4% | flashinfer-bmm-fp8 |
| 🔴 | **FusedAddRMSNormFwdOp** | test_fused_add_rms_norm_bench[llama-405b-decode-bfloat16] | 0.0062 | 0.0043 | 69.6% | flashinfer |
| 🔴 | **SiluFwdOp** | test_silu_manifest_bench[llama-8b-ffn-prefill-float16] | 0.0504 | 0.0356 | 70.6% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-bfloat16] | 0.3115 | 0.2200 | 70.6% | fla |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-softcap50-float16] | 0.1763 | 0.1253 | 71.1% | flashinfer |
| 🔴 | **LogicalOrFwdOp** | test_logical_bench[logical_or-1024x4096-float16-LogicalOrFwdOp-logical_or] | 0.0080 | 0.0057 | 71.1% | torch |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s16k-h4-d64-float16] | 1.5163 | 1.0819 | 71.4% | fla |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-float16] | 0.0984 | 0.0702 | 71.4% | fla |
| 🔴 | **SigmoidFwdOp** | test_sigmoid_manifest_bench[elementwise-256M-bfloat16] | 0.3676 | 0.2630 | 71.6% | torch-compile |
| 🔴 | **IsinfFwdOp** | test_isinf_bench[elementwise-256M-float16] | 0.2763 | 0.1988 | 72.0% | torch-compile |
| 🔴 | **IsfiniteFwdOp** | test_isfinite_bench[elementwise-256M-bfloat16] | 0.2731 | 0.1967 | 72.0% | torch-compile |
| 🔴 | **IsfiniteFwdOp** | test_isfinite_bench[elementwise-256M-float16] | 0.2731 | 0.1969 | 72.1% | torch-compile |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-float16] | 0.0571 | 0.0412 | 72.2% | flashinfer |
| 🔴 | **IsnanFwdOp** | test_isnan_bench[elementwise-256M-float16] | 0.2732 | 0.1972 | 72.2% | torch-compile |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-float16] | 0.1488 | 0.1077 | 72.4% | fla |
| 🔴 | **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[nondiv-7x7-bfloat16] | 0.0158 | 0.0115 | 72.5% | torch-ref |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-2k-bfloat16] | 0.2817 | 0.2044 | 72.6% | torch-cublas |
| 🔴 | **MaxPool2dFwdOp** | test_max_pool2d_bench[resnet-stem-bfloat16] | 0.0471 | 0.0342 | 72.6% | torch-compile |
| 🔴 | **GroupNormFwdOp** | test_group_norm_no_affine_bench[wider-channel-g32-float16] | 0.0048 | 0.0035 | 72.7% | flaggems |
| 🔴 | **IsinfFwdOp** | test_isinf_bench[elementwise-256M-bfloat16] | 0.2753 | 0.2001 | 72.7% | torch-compile |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0568 | 0.0413 | 72.7% | flashinfer |
| 🔴 | **IsnanFwdOp** | test_isnan_bench[elementwise-256M-bfloat16] | 0.2730 | 0.1986 | 72.8% | torch-compile |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float32-SiluAndMulFwdKernel-direct] | 0.0200 | 0.0146 | 73.0% | torch-compile |
| 🔴 | **SumFwdOp** | test_sum_bench[long-seq-reduce-bfloat16] | 0.0052 | 0.0038 | 73.0% | flaggems |
| 🔴 | **MeanFwdOp** | test_mean_bench[long-seq-reduce-bfloat16] | 0.0052 | 0.0038 | 73.0% | flaggems |
| 🔴 | **HardsigmoidFwdOp** | test_hardsigmoid_manifest_bench[mbv3-se-gate-deep-float16] | 0.0020 | 0.0015 | 73.1% | torch-compile |
| 🔴 | **MaxPool2dFwdOp** | test_max_pool2d_bench[resnet-stem-float16] | 0.0469 | 0.0343 | 73.1% | torch-compile |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[alexnet-ceil-bfloat16] | 0.0237 | 0.0174 | 73.4% | torch-compile |
| 🔴 | **LogicalOrFwdOp** | test_logical_or_manifest_bench[cnn-feat-broadcast-float16] | 0.0164 | 0.0120 | 73.4% | torch-compile |
| 🔴 | **IsfiniteFwdOp** | test_isfinite_bench[elementwise-16M-bfloat16] | 0.0205 | 0.0150 | 73.4% | torch-compile |
| 🔴 | **IsnanFwdOp** | test_isnan_bench[elementwise-16M-float16] | 0.0205 | 0.0150 | 73.4% | torch-compile |
| 🔴 | **IsinfFwdOp** | test_isinf_bench[elementwise-16M-float16] | 0.0206 | 0.0151 | 73.5% | torch-compile |
| 🔴 | **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[sincnet-speaker-local-float16] | 0.0218 | 0.0160 | 73.5% | torch-compile |
| 🔴 | **IsfiniteFwdOp** | test_isfinite_bench[elementwise-16M-float16] | 0.0204 | 0.0150 | 73.6% | torch-compile |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-2k-float16] | 0.2838 | 0.2090 | 73.6% | torch-cublas |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b4-4k-bfloat16] | 1.0406 | 0.7671 | 73.7% | torch-cublas |
| 🔴 | **SigmoidFwdOp** | test_sigmoid_manifest_bench[elementwise-16M-bfloat16] | 0.0253 | 0.0187 | 73.8% | torch-compile |
| 🔴 | **IsnanFwdOp** | test_isnan_bench[elementwise-16M-bfloat16] | 0.0205 | 0.0151 | 73.9% | torch-compile |
| 🔴 | **IsinfFwdOp** | test_isinf_bench[elementwise-16M-bfloat16] | 0.0205 | 0.0152 | 74.0% | torch-compile |
| 🔴 | **GeFwdOp** | test_ge_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0118 | 74.1% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-bfloat16] | 0.6111 | 0.4528 | 74.1% | fla |
| 🔴 | **LogicalOrFwdOp** | test_logical_or_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0164 | 0.0121 | 74.2% | torch-compile |
| 🔴 | **LogicalAndFwdOp** | test_logical_bench[logical_and-1024x4096-float16-LogicalAndFwdOp-logical_and] | 0.0079 | 0.0059 | 74.2% | torch |
| 🔴 | **LtFwdOp** | test_lt_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0118 | 74.3% | torch-compile |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-bfloat16] | 0.0925 | 0.0688 | 74.3% | flashinfer |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p256-float16] | 0.1682 | 0.1252 | 74.4% | flashinfer |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[alexnet-ceil-float16] | 0.0237 | 0.0177 | 74.5% | torch-compile |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-float16] | 0.0932 | 0.0694 | 74.6% | flashinfer |
| 🔴 | **NeFwdOp** | test_ne_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0118 | 74.6% | torch-compile |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s16k-h4-d64-bfloat16] | 1.4488 | 1.0817 | 74.7% | fla |
| 🔴 | **LeFwdOp** | test_le_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0119 | 74.7% | torch-compile |
| 🔴 | **LeFwdOp** | test_le_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0119 | 74.7% | torch-compile |
| 🔴 | **BmmFwdOp** | test_bmm_bench[moe-prefill-b128-bfloat16] | 0.2901 | 0.2167 | 74.7% | torch-cublas |
| 🔴 | **GtFwdOp** | test_gt_manifest_bench[cnn-feat-broadcast-float16] | 0.0160 | 0.0119 | 74.8% | torch-compile |
| 🔴 | **NeFwdOp** | test_ne_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0119 | 74.9% | torch-compile |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-bfloat16] | 0.1444 | 0.1082 | 74.9% | fla |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s8k-h4-d64-float16] | 0.7442 | 0.5576 | 74.9% | fla |
| 🔴 | **EqFwdOp** | test_eq_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0120 | 75.1% | torch-compile |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-float16] | 0.1666 | 0.1252 | 75.1% | flashinfer |
| 🔴 | **EqFwdOp** | test_eq_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0120 | 75.2% | torch-compile |
| 🔴 | **Conv2dFwdOp** | test_conv2d_bench[highres-3x3-s1-float16] | 0.1047 | 0.0788 | 75.3% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-float16] | 0.6175 | 0.4653 | 75.3% | fla |
| 🔴 | **LogicalAndFwdOp** | test_logical_and_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0120 | 75.5% | torch-compile |
| 🔴 | **Conv2dFwdOp** | test_conv2d_bench[highres-3x3-s1-bias-float16] | 0.1049 | 0.0793 | 75.6% | torch-compile |
| 🔴 | **GeFwdOp** | test_ge_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0120 | 75.6% | torch-compile |
| 🔴 | **RopeNonNeoxFwdOp** | test_rope_non_neox_bench[non-neox-2d-b2-s2k-h32-d128-bfloat16] | 0.0252 | 0.0190 | 75.6% | torch-compile |
| 🔴 | **GtFwdOp** | test_gt_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0120 | 75.6% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-float16] | 0.9014 | 0.6823 | 75.7% | torch-sdpa |
| 🔴 | **Conv3dFwdOp** | test_conv3d_bench[video-stage-downsample-k3-s2-float16] | 0.0349 | 0.0264 | 75.8% | torch |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-1k-float16] | 0.0411 | 0.0313 | 76.2% | torch-cublas |
| 🔴 | **LogicalAndFwdOp** | test_logical_and_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0122 | 76.3% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s4k-h4-d64-bfloat16] | 0.1564 | 0.1196 | 76.4% | fla |
| 🔴 | **LtFwdOp** | test_lt_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0122 | 76.5% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-float16] | 0.8916 | 0.6825 | 76.5% | torch-sdpa |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s8k-h4-d64-bfloat16] | 0.7275 | 0.5569 | 76.5% | fla |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[attn-weights-4k-float16] | 0.0112 | 0.0086 | 76.6% | flaggems |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-1k-bfloat16] | 0.0407 | 0.0313 | 76.9% | torch-cublas |
| 🔴 | **LogSumExpFwdOp** | test_logsumexp_bench[lm-head-logits-float16] | 0.0141 | 0.0108 | 76.9% | torch-compile |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[attn-weights-4k-bfloat16] | 0.0113 | 0.0087 | 77.0% | flaggems |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-float16] | 0.6710 | 0.5189 | 77.3% | flashinfer |
| 🔴 | **DeltaNetFwdOp** | test_deltanet_vs_fla_fwd[dn-b2-s16k-h4-d64-float16] | 0.4725 | 0.3665 | 77.6% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.6680 | 0.5182 | 77.6% | flashinfer |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-float16] | 0.0866 | 0.0672 | 77.6% | fla |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[attn-weights-4k-float32] | 0.0143 | 0.0111 | 77.8% | flaggems |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-bfloat16] | 0.0866 | 0.0674 | 77.9% | fla |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s4k-h4-d64-float16] | 0.3696 | 0.2880 | 77.9% | fla |
| 🔴 | **DeltaNetFwdOp** | test_deltanet_vs_fla_fwd[dn-b2-s16k-h4-d64-bfloat16] | 0.4734 | 0.3700 | 78.1% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.3505 | 0.2752 | 78.5% | flashinfer |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-float16] | 0.3513 | 0.2771 | 78.9% | flashinfer |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s4k-h4-d64-bfloat16] | 0.3645 | 0.2883 | 79.1% | fla |
| 🔴 | **DivFwdOp** | test_div_manifest_bench[cnn-feat-broadcast-float16] | 0.0187 | 0.0148 | 79.1% | torch-compile |
| 🔴 | **LogSumExpFwdOp** | test_logsumexp_bench[3d-multidim-reduce-float16] | 0.0126 | 0.0100 | 79.1% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-float16] | 0.3127 | 0.2478 | 79.2% | fla |
| 🔴 | **Conv2dFwdOp** | test_conv2d_bench[classifier-1x1-float16] | 0.0091 | 0.0072 | 79.3% | torch-compile |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-large-bfloat16] | 0.0715 | 0.0567 | 79.3% | torch-compile |
| 🔴 | **FloorDivideFwdOp** | test_floor_divide_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0200 | 0.0159 | 79.5% | torch-compile |
| 🔴 | **FloorDivideFwdOp** | test_floor_divide_manifest_bench[cnn-feat-broadcast-float16] | 0.0198 | 0.0158 | 79.5% | torch-compile |
| 🔴 | **Conv3dFwdOp** | test_conv3d_bench[video-stage-downsample-k3-s2-bias-float16] | 0.0353 | 0.0282 | 79.9% | torch-compile |
| 🔴 | **LogicalNotFwdOp** | test_logical_not_bench[elementwise-16M-float16] | 0.0188 | 0.0150 | 79.9% | torch-compile |

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
| ✅ | LogSoftmaxFwdOp | `tileops.ops.reduction.softmax` | 24 | 0 | 0 | 7.81e-03 |
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
| 🔵 | AbsFwdOp | test_abs_bench[elementwise-16M-float16] | 0.0179 | 0.94 | 3.75 | torch 100.4%, torch-compile 100.2% | - |
| 🔵 | AbsFwdOp | test_abs_bench[elementwise-16M-bfloat16] | 0.0179 | 0.94 | 3.75 | torch 100.4%, torch-compile 100.0% | - |
| 🟡 | AbsFwdOp | test_abs_bench[elementwise-16M-float32] | 0.0340 | 0.49 | 3.94 | torch 99.6%, torch-compile 99.7% | - |
| 🟡 | AbsFwdOp | test_abs_bench[elementwise-256M-float16] | 0.2512 | 1.07 | 4.27 | torch 99.6%, torch-compile 99.5% | - |
| 🟡 | AbsFwdOp | test_abs_bench[elementwise-256M-bfloat16] | 0.2513 | 1.07 | 4.27 | torch 99.6%, torch-compile 99.2% | - |
| 🔵 | AdaLayerNormFwdOp | test_ada_layer_norm_bench[dit-xl-2-float16] | 0.0052 | 1.12 | 1.80 | torch-ref 230.5%, torch-compile 145.7% | - |
| 🔵 | AdaLayerNormFwdOp | test_ada_layer_norm_bench[dit-xl-2-bfloat16] | 0.0053 | 1.10 | 1.77 | torch-ref 226.9%, torch-compile 146.1% | - |
| 🔵 | AdaLayerNormFwdOp | test_ada_layer_norm_bench[llama-8b-prefill-float16] | 0.0198 | 2.12 | 3.39 | torch-ref 209.4%, torch-compile 132.2% | - |
| 🔵 | AdaLayerNormFwdOp | test_ada_layer_norm_bench[llama-8b-prefill-bfloat16] | 0.0199 | 2.11 | 3.38 | torch-ref 210.1%, torch-compile 133.0% | - |
| 🔵 | AdaLayerNormFwdOp | test_ada_layer_norm_bench[llama-8b-decode-bfloat16] | 0.0027 | 0.01 | 0.01 | torch-ref 387.4%, torch-compile 115.7% | - |
| 🔵 | AdaLayerNormZeroFwdOp | test_ada_layer_norm_zero_bench[dit-xl-2-float16] | 0.0062 | 1.14 | 1.90 | torch-ref 238.1%, torch-compile 125.3% | - |
| 🔵 | AdaLayerNormZeroFwdOp | test_ada_layer_norm_zero_bench[dit-xl-2-bfloat16] | 0.0062 | 1.13 | 1.89 | torch-ref 236.4%, torch-compile 130.3% | - |
| 🔵 | AdaLayerNormZeroFwdOp | test_ada_layer_norm_zero_bench[llama-8b-prefill-float16] | 0.0248 | 2.03 | 3.38 | torch-ref 215.1%, torch-compile 110.1% | - |
| 🔵 | AdaLayerNormZeroFwdOp | test_ada_layer_norm_zero_bench[llama-8b-prefill-bfloat16] | 0.0246 | 2.04 | 3.40 | torch-ref 217.2%, torch-compile 114.0% | - |
| 🔵 | AdaLayerNormZeroFwdOp | test_ada_layer_norm_zero_bench[llama-8b-decode-bfloat16] | 0.0028 | 0.01 | 0.01 | torch-ref 410.7%, torch-compile 112.4% | - |
| 🔵 | AdaptiveAvgPool2dFwdOp | test_adaptive_avg_pool2d_bench[resnet-global-float16] | 0.0030 | 0.27 | 0.55 | torch-ref 247.3%, torch-compile 124.7% | - |
| 🟢 | AdaptiveAvgPool2dFwdOp | test_adaptive_avg_pool2d_bench[spp-6x6-float16] | 0.0054 | 0.17 | 0.30 | torch-ref 197.7%, torch-compile 197.1% | - |
| 🔵 | AdaptiveAvgPool2dFwdOp | test_adaptive_avg_pool2d_bench[nondiv-7x7-bfloat16] | 0.0066 | 0.07 | 0.12 | torch-ref 138.8%, torch-compile 138.8% | - |
| 🔵 | AdaptiveMaxPool2dFwdOp | test_adaptive_max_pool2d_bench[global-1x1-float16] | 0.0029 | 0.27 | 0.56 | torch-ref 1526.4%, torch-compile 128.3% | - |
| 🟢 | AdaptiveMaxPool2dFwdOp | test_adaptive_max_pool2d_bench[spp-6x6-float16] | 0.0060 | 0.15 | 0.27 | torch-ref 236.7%, torch-compile 237.2% | - |
| 🟢 | AdaptiveMaxPool2dFwdOp | test_adaptive_max_pool2d_bench[nondiv-7x7-bfloat16] | 0.0065 | 0.08 | 0.12 | torch-ref 175.5%, torch-compile 175.0% | - |
| 🔴 | AdaptiveMaxPool2dIndicesFwdOp | test_adaptive_max_pool2d_indices_bench[global-1x1-float16] | 0.0133 | 0.06 | 0.13 | torch-ref 338.4%, torch-compile 61.5% | - |
| 🟡 | AdaptiveMaxPool2dIndicesFwdOp | test_adaptive_max_pool2d_indices_bench[spp-6x6-float16] | 0.0154 | 0.06 | 0.11 | torch-ref 92.7%, torch-compile 92.7% | - |
| 🔴 | AdaptiveMaxPool2dIndicesFwdOp | test_adaptive_max_pool2d_indices_bench[nondiv-7x7-bfloat16] | 0.0158 | 0.03 | 0.05 | torch-ref 72.5%, torch-compile 72.5% | - |
| 🟡 | AddFwdOp | test_add_manifest_bench[hidden-state-prefill-float16] | 0.0147 | 1.14 | 3.42 | torch 100.9%, torch-compile 99.8% | - |
| 🔵 | AddFwdOp | test_add_manifest_bench[hidden-state-prefill-bfloat16] | 0.0147 | 1.14 | 3.43 | torch 101.5%, torch-compile 100.0% | - |
| 🟡 | AddFwdOp | test_add_manifest_bench[hidden-state-prefill-float32] | 0.0265 | 0.63 | 3.80 | torch 100.0%, torch-compile 99.9% | - |
| 🟡 | AddFwdOp | test_add_manifest_bench[cnn-feat-broadcast-float16] | 0.0166 | 1.55 | 3.09 | torch 275.5%, torch-compile 86.9% | - |
| 🟡 | AddFwdOp | test_add_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0166 | 1.55 | 3.09 | torch 279.0%, torch-compile 86.7% | - |
| 🟡 | AddFwdOp | test_add_manifest_bench[cnn-feat-broadcast-float32] | 0.0267 | 0.96 | 3.85 | torch 184.5%, torch-compile 99.4% | - |
| 🔵 | AlibiFwdOp | test_alibi_bench[llama-prefill-2k-float16] | 0.0649 | 6.21 | 4.14 | torch-ref 912.0%, torch-compile 132.9% | - |
| 🔵 | AlibiFwdOp | test_alibi_bench[llama-prefill-2k-bfloat16] | 0.0645 | 6.24 | 4.16 | torch-ref 917.5%, torch-compile 133.4% | - |
| 🔵 | AlibiFwdOp | test_alibi_bench[llama-prefill-4k-float16] | 0.2844 | 5.66 | 3.78 | torch-ref 917.5%, torch-compile 120.0% | - |
| 🔵 | AlibiFwdOp | test_alibi_bench[llama-prefill-4k-bfloat16] | 0.2857 | 5.64 | 3.76 | torch-ref 913.3%, torch-compile 119.4% | - |
| 🔴 | AllFwdOp | test_all_bench[mask-validation-4k-bool] | 0.0074 | 0.02 | 0.02 | flaggems 25.4%, torch 233.6%, torch-compile 24.1% | - |
| 🔴 | AllFwdOp | test_all_bench[mask-validation-32k-bool] | 0.0106 | 0.10 | 0.10 | flaggems 60.8%, torch 95.8%, torch-compile 32.1% | - |
| 🔴 | AllFwdOp | test_all_bench[3d-multidim-reduce-bool] | 0.0217 | 0.10 | 0.10 | flaggems 54.5%, torch 47.9%, torch-compile 20.1% | - |
| 🟡 | AmaxFwdOp | test_amax_bench[hidden-state-reduce-float16] | 0.0086 | 0.98 | 1.96 | flaggems 89.6%, torch 223.9%, torch-compile 117.9% | - |
| 🟡 | AmaxFwdOp | test_amax_bench[hidden-state-reduce-bfloat16] | 0.0087 | 0.96 | 1.92 | flaggems 89.4%, torch 220.9%, torch-compile 115.8% | - |
| 🟡 | AmaxFwdOp | test_amax_bench[long-seq-reduce-bfloat16] | 0.0052 | 0.40 | 0.80 | flaggems 257.9%, torch 214.6%, torch-compile 90.2% | - |
| 🔴 | AmaxFwdOp | test_amax_bench[3d-multidim-reduce-float16] | 0.0115 | 0.18 | 0.36 | flaggems 107.8%, torch 111.9%, torch-compile 42.2% | - |
| 🔵 | AminFwdOp | test_amin_bench[hidden-state-reduce-float16] | 0.0086 | 0.98 | 1.96 | torch 223.9%, torch-compile 117.9% | - |
| 🔵 | AminFwdOp | test_amin_bench[hidden-state-reduce-bfloat16] | 0.0088 | 0.96 | 1.91 | torch 221.2%, torch-compile 115.3% | - |
| 🟡 | AminFwdOp | test_amin_bench[long-seq-reduce-bfloat16] | 0.0052 | 0.40 | 0.80 | torch 215.9%, torch-compile 89.6% | - |
| 🔴 | AminFwdOp | test_amin_bench[3d-multidim-reduce-float16] | 0.0115 | 0.18 | 0.37 | torch 112.6%, torch-compile 42.5% | - |
| 🔴 | AnyFwdOp | test_any_bench[mask-validation-4k-bool] | 0.0072 | 0.02 | 0.02 | flaggems 26.3%, torch 246.7%, torch-compile 24.1% | - |
| 🔴 | AnyFwdOp | test_any_bench[mask-validation-32k-bool] | 0.0106 | 0.10 | 0.10 | flaggems 61.0%, torch 99.1%, torch-compile 31.1% | - |
| 🔴 | AnyFwdOp | test_any_bench[3d-multidim-reduce-bool] | 0.0214 | 0.10 | 0.10 | flaggems 55.1%, torch 88.1%, torch-compile 17.6% | - |
| 🟢 | ArgmaxFwdOp | test_argmax_bench[lm-head-argmax-float16] | 0.0151 | 0.03 | 0.05 | flaggems 198.7%, torch 233.7%, torch-compile 188.8% | - |
| 🟢 | ArgmaxFwdOp | test_argmax_bench[lm-head-argmax-bfloat16] | 0.0155 | 0.03 | 0.05 | flaggems 184.5%, torch 232.3%, torch-compile 188.4% | - |
| 🔴 | ArgmaxFwdOp | test_argmax_bench[hidden-state-argmax-float16] | 0.0239 | 0.35 | 0.70 | flaggems 50.9%, torch 102.8%, torch-compile 79.4% | - |
| 🔴 | ArgmaxFwdOp | test_argmax_bench[hidden-state-argmax-bfloat16] | 0.0240 | 0.35 | 0.70 | flaggems 48.6%, torch 103.7%, torch-compile 80.8% | - |
| 🔴 | ArgmaxFwdOp | test_argmax_bench[3d-non-last-axis-argmax-float16] | 0.0056 | 0.37 | 1.49 | flaggems 68.2%, torch 198.9%, torch-compile 69.3% | - |
| 🟢 | ArgminFwdOp | test_argmin_bench[lm-head-argmin-float16] | 0.0153 | 0.03 | 0.05 | flaggems 758.0%, torch 231.4%, torch-compile 187.2% | - |
| 🟢 | ArgminFwdOp | test_argmin_bench[lm-head-argmin-bfloat16] | 0.0155 | 0.03 | 0.05 | flaggems 663.2%, torch 232.2%, torch-compile 187.6% | - |
| 🔴 | ArgminFwdOp | test_argmin_bench[hidden-state-argmin-float16] | 0.0239 | 0.35 | 0.70 | flaggems 41.4%, torch 103.1%, torch-compile 79.5% | - |
| 🔴 | ArgminFwdOp | test_argmin_bench[hidden-state-argmin-bfloat16] | 0.0240 | 0.35 | 0.70 | flaggems 40.9%, torch 103.6%, torch-compile 80.7% | - |
| 🔴 | AvgPool1dFwdOp | test_avg_pool1d_bench[audio-downsample-float16] | 0.0062 | 0.51 | 1.02 | torch-ref 248.2%, torch-compile 67.9% | - |
| 🟡 | AvgPool1dFwdOp | test_avg_pool1d_bench[long-temporal-float16] | 0.0213 | 0.96 | 1.92 | torch-ref 278.9%, torch-compile 80.5% | - |
| 🔴 | AvgPool1dFwdOp | test_avg_pool1d_bench[ceil-bfloat16] | 0.0035 | 0.30 | 0.46 | torch-ref 154.6%, torch-compile 66.7% | - |
| 🔵 | AvgPool2dFwdOp | test_avg_pool2d_bench[vision-3x3-s2-float16] | 0.0040 | 0.91 | 1.01 | flaggems 167.0%, torch-ref 228.1%, torch-compile 102.8% | - |
| 🟢 | AvgPool2dFwdOp | test_avg_pool2d_bench[vision-5x5-s2-float16] | 0.0040 | 1.24 | 0.50 | flaggems 179.4%, torch-ref 244.5%, torch-compile 511.2% | - |
| 🔵 | AvgPool2dFwdOp | test_avg_pool2d_bench[ceil-divisor-bfloat16] | 0.0031 | 1.12 | 0.72 | flaggems 184.7%, torch-ref 243.9%, torch-compile 124.5% | - |
| 🟡 | AvgPool3dFwdOp | test_avg_pool3d_bench[video-2x2x2-float16] | 0.0037 | 0.44 | 0.98 | cudnn 160.0%, torch-ref 269.6%, torch-compile 92.2% | - |
| 🟡 | AvgPool3dFwdOp | test_avg_pool3d_bench[ceil-video-float16] | 0.0044 | 0.59 | 0.43 | cudnn 128.5%, torch-ref 259.9%, torch-compile 92.0% | - |
| 🟡 | AvgPool3dFwdOp | test_avg_pool3d_bench[divisor-bfloat16] | 0.0023 | 0.15 | 0.21 | torch-ref 222.5%, torch-compile 84.5% | - |
| 🟢 | BatchNormBwdOp | test_batch_norm_bwd_bench[resnet50-fc-float16] | 0.0071 | 0.00 | 0.00 | torch-autograd 331.2% | - |
| 🟢 | BatchNormBwdOp | test_batch_norm_bwd_bench[resnet50-stage1-float16] | 0.0148 | 0.28 | 0.21 | torch-autograd 186.2% | - |
| 🟢 | BatchNormBwdOp | test_batch_norm_bwd_bench[resnet50-stage2-float16] | 0.0141 | 0.30 | 0.22 | torch-autograd 169.6% | - |
| 🔵 | BatchNormBwdOp | test_batch_norm_bwd_bench[resnet50-stage3-float16] | 0.0171 | 0.38 | 0.28 | torch-autograd 149.6% | - |
| 🟢 | BatchNormBwdOp | test_batch_norm_bwd_bench[large-spatial-float16] | 6.8739 | 0.62 | 0.47 | torch-autograd 188.7% | - |
| 🔴 | BatchNormFwdOp | test_batch_norm_fwd_bench[resnet50-fc-float16] | 0.0061 | 0.00 | 0.00 | flaggems 90.1%, torch-cudnn 184.8%, torch-compile 36.6% | - |
| 🔴 | BatchNormFwdOp | test_batch_norm_fwd_bench[resnet50-stage1-float16] | 0.0109 | 0.48 | 0.19 | flaggems 94.2%, torch-cudnn 103.8%, torch-compile 37.7% | - |
| 🔴 | BatchNormFwdOp | test_batch_norm_fwd_bench[resnet50-stage2-float16] | 0.0107 | 0.49 | 0.20 | flaggems 83.8%, torch-cudnn 97.0%, torch-compile 30.8% | - |
| 🔴 | BatchNormFwdOp | test_batch_norm_fwd_bench[resnet50-stage3-float16] | 0.0129 | 0.62 | 0.25 | flaggems 84.8%, torch-cudnn 86.6%, torch-compile 35.6% | - |
| 🔴 | BatchNormFwdOp | test_batch_norm_fwd_bench[large-spatial-float16] | 4.3427 | 1.24 | 0.49 | flaggems 89.7%, torch-cudnn 104.4%, torch-compile 23.4% | - |
| 🟡 | BitwiseAndFwdOp | test_bitwise_bench[bitwise_and-1024x4096-BitwiseAndFwdOp-bitwise_and] | 0.0150 | 0.28 | 3.35 | torch 98.1%, torch-compile 97.9% | - |
| 🟡 | BitwiseAndFwdOp | test_bitwise_bench[bitwise_and-1024x10240-BitwiseAndFwdOp-bitwise_and] | 0.0326 | 0.32 | 3.86 | torch 98.1%, torch-compile 98.1% | - |
| 🔵 | BitwiseAndFwdOp | test_bitwise_and_manifest_bench[hidden-state-prefill-bool] | 0.0084 | 1.00 | 3.01 | torch 121.1%, torch-compile 107.1% | - |
| 🟡 | BitwiseAndFwdOp | test_bitwise_and_manifest_bench[hidden-state-prefill-int32] | 0.0269 | 0.31 | 3.75 | torch 97.7%, torch-compile 97.4% | - |
| 🟡 | BitwiseAndFwdOp | test_bitwise_and_manifest_bench[hidden-state-prefill-int64] | 0.0498 | 0.17 | 4.04 | torch 100.0%, torch-compile 98.7% | - |
| 🔵 | BitwiseAndFwdOp | test_bitwise_and_manifest_bench[cnn-feat-broadcast-bool] | 0.0081 | 1.59 | 3.17 | torch 558.1%, torch-compile 123.7% | - |
| 🟡 | BitwiseAndFwdOp | test_bitwise_and_manifest_bench[cnn-feat-broadcast-int32] | 0.0275 | 0.47 | 3.74 | torch 179.7%, torch-compile 96.4% | - |
| 🟡 | BitwiseAndFwdOp | test_bitwise_and_manifest_bench[cnn-feat-broadcast-int64] | 0.0528 | 0.24 | 3.90 | torch 110.5%, torch-compile 94.8% | - |
| 🔴 | BitwiseNotFwdOp | test_bitwise_not_bench[elementwise-16M-int32] | 0.0610 | 0.28 | 2.20 | torch 55.8%, torch-compile 55.6% | - |
| 🟡 | BitwiseNotFwdOp | test_bitwise_not_bench[elementwise-16M-int64] | 0.0746 | 0.23 | 3.60 | torch 91.2%, torch-compile 86.8% | - |
| 🔴 | BitwiseNotFwdOp | test_bitwise_not_bench[elementwise-256M-int32] | 0.9381 | 0.29 | 2.29 | torch 53.8%, torch-compile 53.8% | - |
| 🟡 | BitwiseOrFwdOp | test_bitwise_bench[bitwise_or-1024x4096-BitwiseOrFwdOp-bitwise_or] | 0.0149 | 0.28 | 3.38 | torch 97.6%, torch-compile 102.0% | - |
| 🔵 | BitwiseOrFwdOp | test_bitwise_or_manifest_bench[hidden-state-prefill-bool] | 0.0082 | 1.03 | 3.08 | torch 107.8%, torch-compile 104.7% | - |
| 🟡 | BitwiseOrFwdOp | test_bitwise_or_manifest_bench[hidden-state-prefill-int32] | 0.0272 | 0.31 | 3.71 | torch 97.5%, torch-compile 102.4% | - |
| 🟡 | BitwiseOrFwdOp | test_bitwise_or_manifest_bench[hidden-state-prefill-int64] | 0.0499 | 0.17 | 4.04 | torch 99.7%, torch-compile 98.9% | - |
| 🔵 | BitwiseOrFwdOp | test_bitwise_or_manifest_bench[cnn-feat-broadcast-bool] | 0.0081 | 1.58 | 3.16 | torch 544.5%, torch-compile 125.6% | - |
| 🔵 | BitwiseOrFwdOp | test_bitwise_or_manifest_bench[cnn-feat-broadcast-int32] | 0.0275 | 0.47 | 3.74 | torch 179.7%, torch-compile 111.1% | - |
| 🟡 | BitwiseOrFwdOp | test_bitwise_or_manifest_bench[cnn-feat-broadcast-int64] | 0.0524 | 0.25 | 3.92 | torch 111.5%, torch-compile 95.6% | - |
| 🟡 | BitwiseXorFwdOp | test_bitwise_bench[bitwise_xor-1024x4096-BitwiseXorFwdOp-bitwise_xor] | 0.0151 | 0.28 | 3.33 | torch 97.9%, torch-compile 97.5% | - |
| 🔵 | BitwiseXorFwdOp | test_bitwise_xor_manifest_bench[hidden-state-prefill-bool] | 0.0082 | 1.02 | 3.07 | torch 121.5%, torch-compile 107.8% | - |
| 🟡 | BitwiseXorFwdOp | test_bitwise_xor_manifest_bench[hidden-state-prefill-int32] | 0.0269 | 0.31 | 3.75 | torch 97.8%, torch-compile 97.8% | - |
| 🟡 | BitwiseXorFwdOp | test_bitwise_xor_manifest_bench[hidden-state-prefill-int64] | 0.0500 | 0.17 | 4.03 | torch 99.7%, torch-compile 98.7% | - |
| 🔵 | BitwiseXorFwdOp | test_bitwise_xor_manifest_bench[cnn-feat-broadcast-bool] | 0.0080 | 1.60 | 3.20 | torch 563.4%, torch-compile 124.7% | - |
| 🟡 | BitwiseXorFwdOp | test_bitwise_xor_manifest_bench[cnn-feat-broadcast-int32] | 0.0274 | 0.47 | 3.76 | torch 180.6%, torch-compile 96.5% | - |
| 🟡 | BitwiseXorFwdOp | test_bitwise_xor_manifest_bench[cnn-feat-broadcast-int64] | 0.0525 | 0.24 | 3.91 | torch 111.1%, torch-compile 95.4% | - |
| 🟡 | BmmFp8KNFwdOp | test_bmm_fp8_kn_bench[square-b4-1k-per-tensor-float8_e4m3fn] | 0.0390 | 220.21 | 0.43 | torch-fp32-ref 751.9%, flashinfer-bmm-fp8 90.7% | - |
| 🟢 | BmmFp8KNFwdOp | test_bmm_fp8_kn_bench[square-b8-2k-per-tensor-float8_e4m3fn] | 0.3064 | 448.51 | 0.44 | torch-fp32-ref 1325.4%, flashinfer-bmm-fp8 203.4% | - |
| 🔴 | BmmFp8KNFwdOp | test_bmm_fp8_kn_bench[mha-decode-b32-pv-per-tensor-float8_e4m3fn] | 0.0646 | 33.22 | 0.28 | torch-fp32-ref 364.9%, flashinfer-bmm-fp8 38.6% | - |
| 🔴 | BmmFp8KNFwdOp | test_bmm_fp8_kn_bench[mha-decode-b64-qk-per-tensor-float8_e4m3fn] | 0.1154 | 37.22 | 0.45 | torch-fp32-ref 250.2%, flashinfer-bmm-fp8 43.0% | - |
| 🔴 | BmmFp8KNFwdOp | test_bmm_fp8_kn_bench[moe-prefill-b128-per-tensor-float8_e4m3fn] | 0.9008 | 152.58 | 0.37 | torch-fp32-ref 599.2%, flashinfer-bmm-fp8 69.4% | - |
| 🔵 | BmmFp8NKFwdOp | test_bmm_fp8_nk_bench[square-b4-1k-per-tensor-float8_e4m3fn] | 0.0119 | 721.60 | 1.41 | torch-fp32-ref 2466.3%, flashinfer-bmm-fp8 109.7% | - |
| 🔵 | BmmFp8NKFwdOp | test_bmm_fp8_nk_bench[square-b8-2k-per-tensor-float8_e4m3fn] | 0.1198 | 1147.47 | 1.12 | torch-fp32-ref 3397.0%, flashinfer-bmm-fp8 105.5% | - |
| 🔵 | BmmFp8NKFwdOp | test_bmm_fp8_nk_bench[mha-decode-b32-pv-per-tensor-float8_e4m3fn] | 0.0090 | 237.96 | 1.98 | torch-fp32-ref 2622.6%, flashinfer-bmm-fp8 105.3% | - |
| 🔵 | BmmFp8NKFwdOp | test_bmm_fp8_nk_bench[mha-decode-b64-qk-per-tensor-float8_e4m3fn] | 0.0158 | 272.25 | 3.26 | torch-fp32-ref 1826.7%, flashinfer-bmm-fp8 137.0% | - |
| 🔵 | BmmFp8NKFwdOp | test_bmm_fp8_nk_bench[moe-prefill-b128-per-tensor-float8_e4m3fn] | 0.1316 | 1043.99 | 2.55 | torch-fp32-ref 4104.2%, flashinfer-bmm-fp8 105.4% | - |
| 🔵 | BmmFwdOp | test_bmm_bench[small-b8-128-float16] | 0.0027 | 12.34 | 0.29 | flaggems 115.3%, torch-cublas 118.8% | - |
| 🔵 | BmmFwdOp | test_bmm_bench[small-b8-128-bfloat16] | 0.0027 | 12.34 | 0.29 | flaggems 116.5%, torch-cublas 118.8% | - |
| 🔴 | BmmFwdOp | test_bmm_bench[square-b8-1k-float16] | 0.0411 | 418.28 | 1.23 | flaggems 109.6%, torch-cublas 76.2% | - |
| 🔴 | BmmFwdOp | test_bmm_bench[square-b8-1k-bfloat16] | 0.0407 | 421.90 | 1.24 | flaggems 110.3%, torch-cublas 76.9% | - |
| 🟡 | BmmFwdOp | test_bmm_bench[square-b16-512-float16] | 0.0132 | 324.20 | 1.90 | flaggems 114.5%, torch-cublas 91.1% | - |
| 🟡 | BmmFwdOp | test_bmm_bench[square-b16-512-bfloat16] | 0.0133 | 321.87 | 1.89 | flaggems 113.2%, torch-cublas 89.7% | - |
| 🔵 | BmmFwdOp | test_bmm_bench[square-b32-256-float16] | 0.0066 | 162.91 | 1.91 | flaggems 120.4%, torch-cublas 107.3% | - |
| 🔵 | BmmFwdOp | test_bmm_bench[square-b32-256-bfloat16] | 0.0066 | 163.28 | 1.91 | flaggems 120.7%, torch-cublas 107.1% | - |
| 🔴 | BmmFwdOp | test_bmm_bench[square-b4-4k-bfloat16] | 1.0406 | 528.28 | 0.39 | flaggems 92.8%, torch-cublas 73.7% | - |
| 🔴 | BmmFwdOp | test_bmm_bench[square-b8-2k-float16] | 0.2838 | 484.32 | 0.71 | flaggems 97.4%, torch-cublas 73.6% | - |
| 🔴 | BmmFwdOp | test_bmm_bench[square-b8-2k-bfloat16] | 0.2817 | 487.90 | 0.71 | flaggems 96.6%, torch-cublas 72.6% | - |
| 🟡 | BmmFwdOp | test_bmm_bench[mha-decode-b64-qk-float16] | 0.0227 | 189.57 | 3.05 | flaggems 115.1%, torch-cublas 94.3% | - |
| 🟡 | BmmFwdOp | test_bmm_bench[mha-decode-b64-qk-bfloat16] | 0.0225 | 191.19 | 3.08 | flaggems 115.7%, torch-cublas 94.3% | - |
| 🔵 | BmmFwdOp | test_bmm_bench[mha-decode-b64-pv-float16] | 0.0240 | 179.20 | 2.89 | flaggems 169.4%, torch-cublas 101.6% | - |
| 🔵 | BmmFwdOp | test_bmm_bench[mha-decode-b64-pv-bfloat16] | 0.0240 | 179.07 | 2.89 | flaggems 169.4%, torch-cublas 101.7% | - |
| 🔴 | BmmFwdOp | test_bmm_bench[moe-prefill-b128-bfloat16] | 0.2901 | 473.72 | 2.08 | flaggems 102.2%, torch-cublas 74.7% | - |
| 🟢 | CBProducerFwdOp | test_cb_producer_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0072 | 18.72 | 0.59 | torch 527.9% | - |
| 🟢 | CBProducerFwdOp | test_cb_producer_fwd_bench[mamba2-2p7b-b4-s2k-bfloat16] | 0.0119 | 22.64 | 0.71 | torch 447.8% | - |
| 🟡 | CeilFwdOp | test_ceil_bench[elementwise-16M-float16] | 0.0180 | 0.93 | 3.74 | torch 100.0%, torch-compile 99.8% | - |
| 🟡 | CeilFwdOp | test_ceil_bench[elementwise-16M-bfloat16] | 0.0180 | 0.93 | 3.74 | torch 100.0%, torch-compile 99.8% | - |
| 🟡 | CeilFwdOp | test_ceil_bench[elementwise-16M-float32] | 0.0341 | 0.49 | 3.94 | torch 99.7%, torch-compile 99.5% | - |
| 🟡 | CeilFwdOp | test_ceil_bench[elementwise-256M-float16] | 0.2532 | 1.06 | 4.24 | torch 98.8%, torch-compile 98.7% | - |
| 🟡 | CeilFwdOp | test_ceil_bench[elementwise-256M-bfloat16] | 0.2532 | 1.06 | 4.24 | torch 98.9%, torch-compile 98.8% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-float16] | 0.0354 | 0.47 | 3.79 | torch 98.6%, torch-compile 98.9% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-bfloat16] | 0.0354 | 0.47 | 3.79 | torch 98.5%, torch-compile 98.8% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-float32] | 0.0659 | 0.25 | 4.08 | torch 99.6%, torch-compile 99.4% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-256M-float16] | 0.4858 | 0.55 | 4.42 | torch 99.9%, torch-compile 99.9% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-256M-bfloat16] | 0.4856 | 0.55 | 4.42 | torch 99.9%, torch-compile 99.9% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-min-only-float16] | 0.0268 | 0.63 | 3.76 | torch 99.4%, torch-compile 98.4% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-min-only-bfloat16] | 0.0269 | 0.62 | 3.74 | torch 100.0%, torch-compile 98.3% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-min-only-float32] | 0.0500 | 0.34 | 4.03 | torch 98.9%, torch-compile 98.5% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-256M-min-only-float16] | 0.3694 | 0.73 | 4.36 | torch 99.7%, torch-compile 99.9% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-256M-min-only-bfloat16] | 0.3686 | 0.73 | 4.37 | torch 99.8%, torch-compile 100.0% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-max-only-float16] | 0.0266 | 0.63 | 3.78 | torch 99.6%, torch-compile 98.7% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-max-only-bfloat16] | 0.0271 | 0.62 | 3.71 | torch 99.5%, torch-compile 98.2% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-max-only-float32] | 0.0500 | 0.34 | 4.03 | torch 98.8%, torch-compile 98.5% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-256M-max-only-float16] | 0.3689 | 0.73 | 4.37 | torch 99.8%, torch-compile 100.0% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-256M-max-only-bfloat16] | 0.3680 | 0.73 | 4.38 | torch 100.0%, torch-compile 100.2% | - |
| 🔵 | ClampScalarFwdOp | test_clamp_scalar_manifest_bench[elementwise-16M-float16] | 0.0184 | 0.91 | 3.64 | torch 110.1%, torch-compile 100.1% | - |
| 🔵 | ClampScalarFwdOp | test_clamp_scalar_manifest_bench[elementwise-16M-bfloat16] | 0.0184 | 0.91 | 3.64 | torch 103.8%, torch-compile 101.2% | - |
| 🔵 | ClampScalarFwdOp | test_clamp_scalar_manifest_bench[elementwise-16M-float32] | 0.0338 | 0.50 | 3.97 | torch 100.9%, torch-compile 100.6% | - |
| 🔵 | ClampScalarFwdOp | test_clamp_scalar_manifest_bench[elementwise-256M-float16] | 0.2522 | 1.06 | 4.26 | torch 115.7%, torch-compile 100.6% | - |
| 🔵 | ClampScalarFwdOp | test_clamp_scalar_manifest_bench[elementwise-256M-bfloat16] | 0.2525 | 1.06 | 4.25 | torch 109.1%, torch-compile 105.1% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[whisper-large-conv1-float16] | 0.0482 | 38.25 | 0.18 | flaggems 233.3%, torch 118.0%, torch-compile 118.1% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[whisper-large-conv1-bfloat16] | 0.0485 | 37.99 | 0.18 | flaggems 231.3%, torch 116.3%, torch-compile 116.4% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[wav2vec2-layer1-float16] | 0.0067 | 4.90 | 0.50 | flaggems 599.1%, torch 278.5%, torch-compile 278.5% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[wav2vec2-layer1-bfloat16] | 0.0067 | 4.92 | 0.50 | flaggems 602.3%, torch 282.7%, torch-compile 282.7% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[encodec-init-float16] | 0.0035 | 3.05 | 0.45 | flaggems 695.3%, torch 189.0%, torch-compile 189.0% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[encodec-init-bfloat16] | 0.0035 | 3.05 | 0.45 | flaggems 693.6%, torch 188.2%, torch-compile 188.2% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[encodec-deep-float16] | 0.0120 | 32.36 | 0.09 | flaggems 596.5%, torch 141.7%, torch-compile 141.8% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[encodec-deep-bfloat16] | 0.0120 | 32.36 | 0.09 | flaggems 597.1%, torch 141.7%, torch-compile 141.4% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[whisper-large-conv1-bias-float16] | 0.0477 | 38.69 | 0.18 | flaggems 234.1%, torch 145.3%, torch-compile 133.6% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[whisper-large-conv1-bias-bfloat16] | 0.0477 | 38.69 | 0.18 | flaggems 233.7%, torch 145.3%, torch-compile 132.8% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[wav2vec2-layer1-bias-float16] | 0.0069 | 4.98 | 0.48 | flaggems 566.0%, torch 365.3%, torch-compile 311.1% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[wav2vec2-layer1-bias-bfloat16] | 0.0069 | 4.95 | 0.48 | flaggems 564.1%, torch 368.2%, torch-compile 326.7% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[encodec-init-bias-float16] | 0.0036 | 3.21 | 0.44 | flaggems 657.1%, torch 293.8%, torch-compile 250.5% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[encodec-init-bias-bfloat16] | 0.0036 | 3.21 | 0.44 | flaggems 656.1%, torch 296.8%, torch-compile 251.7% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[encodec-deep-bias-float16] | 0.0124 | 31.13 | 0.09 | flaggems 566.1%, torch 164.0%, torch-compile 149.4% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[encodec-deep-bias-bfloat16] | 0.0124 | 31.21 | 0.09 | flaggems 567.8%, torch 163.4%, torch-compile 149.0% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[resnet-3x3-float16] | 0.0130 | 35.59 | 0.13 | flaggems 640.9%, torch 113.1%, torch-compile 89.2% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[resnet-3x3-bfloat16] | 0.0130 | 35.60 | 0.13 | flaggems 639.9%, torch 115.0%, torch-compile 91.4% | - |
| 🟢 | Conv2dFwdOp | test_conv2d_bench[stem-3x3-s2-float16] | 0.0036 | 3.05 | 0.14 | flaggems 366.7%, torch 182.0%, torch-compile 262.2% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[stage-transition-3x3-s2-float16] | 0.0138 | 33.61 | 0.13 | flaggems 862.3%, torch 123.3%, torch-compile 97.4% | - |
| 🔴 | Conv2dFwdOp | test_conv2d_bench[highres-3x3-s1-float16] | 0.1047 | 282.65 | 0.21 | flaggems 702.0%, torch 90.4%, torch-compile 75.3% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[midres-5x5-s1-float16] | 0.0162 | 79.49 | 0.10 | flaggems 1251.5%, torch 120.8%, torch-compile 99.4% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[stage-transition-5x5-s2-float16] | 0.0225 | 57.18 | 0.13 | flaggems 1381.9%, torch 113.4%, torch-compile 99.0% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[stride2-bfloat16] | 0.0111 | 5.21 | 0.05 | flaggems 583.9%, torch 133.6%, torch-compile 109.2% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[resnet-1x1-float16] | 0.0044 | 47.22 | 0.93 | flaggems 1128.3%, torch 96.3%, torch-compile 192.7% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[resnet-1x1-bfloat16] | 0.0044 | 46.88 | 0.92 | flaggems 1121.9%, torch 91.2%, torch-compile 189.1% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[bottleneck-expand-1x1-float16] | 0.0038 | 53.97 | 0.56 | flaggems 747.9%, torch 105.9%, torch-compile 195.0% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[bottleneck-reduce-1x1-float16] | 0.0047 | 43.99 | 0.46 | flaggems 564.4%, torch 92.5%, torch-compile 169.2% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[late-stage-1x1-float16] | 0.0050 | 20.46 | 0.20 | flaggems 306.4%, torch 126.1%, torch-compile 133.1% | - |
| 🔴 | Conv2dFwdOp | test_conv2d_bench[classifier-1x1-float16] | 0.0091 | 11.27 | 0.26 | flaggems 226.7%, torch 98.6%, torch-compile 79.3% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[deeplabv3-aspp-3x3-rate12-float16] | 0.0890 | 108.63 | 0.16 | flaggems 804.1%, torch 133.8%, torch-compile 102.4% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[mobilenetv2-depthwise-float16] | 0.0028 | 0.64 | 0.14 | flaggems 1925.0%, torch 107.9%, torch-compile 197.7% | - |
| 🟢 | Conv2dFwdOp | test_conv2d_bench[resnext-grouped-3x3-float16] | 0.0041 | 3.50 | 0.15 | flaggems 465.9%, torch 460.4%, torch-compile 461.2% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[resnet-3x3-bias-float16] | 0.0132 | 34.94 | 0.13 | flaggems 622.1%, torch 138.3%, torch-compile 88.2% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[resnet-3x3-bias-bfloat16] | 0.0138 | 33.64 | 0.12 | flaggems 598.4%, torch 133.3%, torch-compile 91.6% | - |
| 🟢 | Conv2dFwdOp | test_conv2d_bench[stem-3x3-s2-bias-float16] | 0.0035 | 3.16 | 0.14 | flaggems 351.4%, torch 272.5%, torch-compile 273.4% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[stage-transition-3x3-s2-bias-float16] | 0.0141 | 32.71 | 0.13 | flaggems 831.7%, torch 142.3%, torch-compile 96.8% | - |
| 🔴 | Conv2dFwdOp | test_conv2d_bench[highres-3x3-s1-bias-float16] | 0.1049 | 282.11 | 0.21 | flaggems 699.5%, torch 109.2%, torch-compile 75.6% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[midres-5x5-s1-bias-float16] | 0.0165 | 77.82 | 0.10 | flaggems 1221.5%, torch 140.1%, torch-compile 115.9% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[stage-transition-5x5-s2-bias-float16] | 0.0225 | 57.11 | 0.13 | flaggems 1376.5%, torch 127.5%, torch-compile 99.7% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[stride2-bias-bfloat16] | 0.0116 | 4.99 | 0.05 | flaggems 552.2%, torch 153.9%, torch-compile 107.2% | - |
| 🟢 | Conv2dFwdOp | test_conv2d_bench[resnet-1x1-bias-float16] | 0.0046 | 45.26 | 0.88 | flaggems 1055.2%, torch 254.6%, torch-compile 192.3% | - |
| 🟢 | Conv2dFwdOp | test_conv2d_bench[resnet-1x1-bias-bfloat16] | 0.0046 | 44.95 | 0.88 | flaggems 1048.6%, torch 249.3%, torch-compile 188.2% | - |
| 🟢 | Conv2dFwdOp | test_conv2d_bench[bottleneck-expand-1x1-bias-float16] | 0.0041 | 50.37 | 0.52 | flaggems 674.6%, torch 214.1%, torch-compile 191.4% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[bottleneck-reduce-1x1-bias-float16] | 0.0049 | 41.61 | 0.43 | flaggems 517.8%, torch 147.6%, torch-compile 171.5% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[late-stage-1x1-bias-float16] | 0.0053 | 19.50 | 0.19 | flaggems 280.0%, torch 175.2%, torch-compile 133.9% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[classifier-1x1-bias-float16] | 0.0096 | 10.75 | 0.25 | flaggems 208.0%, torch 123.4%, torch-compile 81.3% | - |
| 🟢 | Conv3dFwdOp | test_conv3d_bench[r3d-stem-k3-s1-float16] | 0.0229 | 90.69 | 1.17 | flaggems 374.1%, torch 500.3%, torch-compile 500.3% | - |
| 🔴 | Conv3dFwdOp | test_conv3d_bench[video-stage-downsample-k3-s2-float16] | 0.0349 | 39.77 | 0.13 | flaggems 623.6%, torch 75.8%, torch-compile 75.8% | - |
| 🔴 | Conv3dFwdOp | test_conv3d_bench[unet-encoder-k3-s1-bfloat16] | 0.3539 | 40.96 | 0.07 | flaggems 89.6%, torch 32.5%, torch-compile 32.6% | - |
| 🔴 | Conv3dFwdOp | test_conv3d_bench[3d-unet-aspp-3x3x3-rate6-float16] | 0.1269 | 57.09 | 0.04 | flaggems 236.6%, torch 29.6%, torch-compile 29.6% | - |
| 🟢 | Conv3dFwdOp | test_conv3d_bench[3d-resnext-grouped-k3-float16] | 0.0157 | 5.51 | 0.15 | flaggems 1617.1%, torch 1787.4%, torch-compile 1752.9% | - |
| 🟢 | Conv3dFwdOp | test_conv3d_bench[r3d-stem-k3-s1-bias-float16] | 0.0229 | 91.25 | 1.17 | flaggems 370.3%, torch 673.5%, torch-compile 549.6% | - |
| 🔴 | Conv3dFwdOp | test_conv3d_bench[video-stage-downsample-k3-s2-bias-float16] | 0.0353 | 39.32 | 0.13 | flaggems 611.6%, torch 84.9%, torch-compile 79.9% | - |
| 🔴 | Conv3dFwdOp | test_conv3d_bench[unet-encoder-k3-s1-bias-bfloat16] | 0.3538 | 41.00 | 0.07 | flaggems 89.3%, torch 39.8%, torch-compile 34.5% | - |
| 🔵 | CosFwdOp | test_cos_bench[elementwise-16M-float16] | 0.0262 | 0.64 | 2.56 | torch 103.8%, torch-compile 107.1% | - |
| 🔵 | CosFwdOp | test_cos_bench[elementwise-16M-bfloat16] | 0.0266 | 0.63 | 2.52 | torch 102.5%, torch-compile 106.9% | - |
| 🟡 | CosFwdOp | test_cos_bench[elementwise-16M-float32] | 0.0359 | 0.47 | 3.74 | torch 95.7%, torch-compile 95.6% | - |
| 🔵 | CosFwdOp | test_cos_bench[elementwise-256M-float16] | 0.3800 | 0.71 | 2.83 | torch 103.3%, torch-compile 107.3% | - |
| 🔵 | CosFwdOp | test_cos_bench[elementwise-256M-bfloat16] | 0.3853 | 0.70 | 2.79 | torch 102.1%, torch-compile 106.9% | - |
| 🔵 | CountNonzeroFwdOp | test_count_nonzero_bench[sparsity-hidden-float16] | 0.0087 | 1.93 | 1.94 | torch 734.7%, torch-compile 104.8% | - |
| 🔵 | CountNonzeroFwdOp | test_count_nonzero_bench[sparsity-hidden-bfloat16] | 0.0088 | 1.91 | 1.91 | torch 722.9%, torch-compile 103.3% | - |
| 🟡 | CountNonzeroFwdOp | test_count_nonzero_bench[sparsity-seq-float16] | 0.0045 | 0.46 | 0.46 | torch 339.0%, torch-compile 87.2% | - |
| 🔴 | CountNonzeroFwdOp | test_count_nonzero_bench[3d-multidim-reduce-float16] | 0.0115 | 0.37 | 0.37 | torch 189.7%, torch-compile 41.1% | - |
| 🔴 | CumprodFwdOp | test_cumprod_bench[hidden-state-scan-float16] | 0.0444 | 0.19 | 0.76 | torch 328.9%, torch-compile 54.6% | - |
| 🔴 | CumprodFwdOp | test_cumprod_bench[hidden-state-scan-bfloat16] | 0.0436 | 0.19 | 0.77 | torch 335.0%, torch-compile 55.9% | - |
| 🔴 | CumprodFwdOp | test_cumprod_bench[long-seq-scan-bfloat16] | 0.2501 | 0.01 | 0.03 | torch 27.1%, torch-compile 4.9% | - |
| 🔴 | CumsumFwdOp | test_cumsum_bench[hidden-state-scan-float16] | 0.0445 | 0.19 | 0.75 | flaggems 23.7%, torch 327.8%, torch-compile 54.4% | - |
| 🔴 | CumsumFwdOp | test_cumsum_bench[hidden-state-scan-bfloat16] | 0.0436 | 0.19 | 0.77 | flaggems 24.2%, torch 335.6%, torch-compile 56.0% | - |
| 🔴 | CumsumFwdOp | test_cumsum_bench[long-seq-scan-bfloat16] | 0.0295 | 0.07 | 0.28 | flaggems 27.1%, torch 229.6%, torch-compile 41.3% | - |
| 🔴 | DaCumsumFwdOp | test_da_cumsum_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0051 | 0.27 | 0.39 | mamba 67.3%, torch-ref 1400.3%, torch-compile 93.7% | - |
| 🔴 | DaCumsumFwdOp | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-bfloat16] | 0.0154 | 0.48 | 0.68 | mamba 41.6%, torch-ref 592.1%, torch-compile 74.0% | - |
| 🟡 | DaCumsumFwdOp | test_da_cumsum_fwd_bench[mamba2-780m-b1-s4k-dt-bias-float16] | 0.0043 | 0.37 | 0.46 | mamba 80.6%, torch-ref 1731.0%, torch-compile 111.9% | - |
| 🔴 | DaCumsumFwdOp | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-dt-bias-bfloat16] | 0.0149 | 0.56 | 0.70 | mamba 43.0%, torch-ref 648.4%, torch-compile 76.8% | - |
| 🔴 | DaCumsumFwdOp | test_da_cumsum_fwd_bench[mamba2-2p7b-b2-s32k-dt-bias-float16] | 0.0600 | 0.70 | 0.87 | mamba 37.3%, torch-ref 394.9%, torch-compile 57.7% | - |
| 🟢 | DeepSeekSparseAttentionDecodeWithKVCacheFwdOp | test_dsa_decode_bench[single-batch-mainstream-float16] | 1.8592 | 314.17 | 0.16 | torch-ref 1020.3%, torch-compile 893.2% | - |
| 🟢 | DeepSeekSparseAttentionDecodeWithKVCacheFwdOp | test_dsa_decode_bench[longer-kv-lower-topk-float16] | 0.5001 | 292.01 | 0.30 | torch-ref 3865.4%, torch-compile 3254.6% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s2k-h4-d64-float16] | 0.1306 | 2.06 | 0.21 | fla 86.7% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s2k-h4-d64-bfloat16] | 0.1316 | 2.04 | 0.21 | fla 86.9% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s4k-h4-d64-float16] | 0.2591 | 2.07 | 0.21 | fla 83.0% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s4k-h4-d64-bfloat16] | 0.2616 | 2.05 | 0.21 | fla 82.7% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s8k-h4-d64-float16] | 0.5059 | 2.12 | 0.22 | fla 85.5% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s8k-h4-d64-bfloat16] | 0.5102 | 2.10 | 0.21 | fla 85.5% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s16k-h4-d64-float16] | 0.9927 | 2.16 | 0.22 | fla 87.0% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s16k-h4-d64-bfloat16] | 1.0035 | 2.14 | 0.22 | fla 86.9% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b1-h8-d128-bfloat16] | 0.0028 | 0.28 | 0.19 | torch 1174.2%, torch-compile 458.5% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b1-h16-d128-bfloat16] | 0.0031 | 0.51 | 0.34 | torch 1137.2%, torch-compile 460.8% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b1-h32-d128-bfloat16] | 0.0034 | 0.94 | 0.63 | torch 1165.6%, torch-compile 486.7% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b1-h48-d128-bfloat16] | 0.0036 | 1.33 | 0.90 | torch 1219.9%, torch-compile 537.8% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b1-h64-d128-bfloat16] | 0.0038 | 1.64 | 1.11 | torch 1143.3%, torch-compile 453.3% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b8-h32-d128-bfloat16] | 0.0087 | 2.90 | 1.96 | torch 1030.2%, torch-compile 438.6% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b8-h48-d128-bfloat16] | 0.0123 | 3.07 | 2.07 | torch 900.2%, torch-compile 320.9% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b8-h64-d128-bfloat16] | 0.0163 | 3.10 | 2.09 | torch 873.7%, torch-compile 316.1% | - |
| 🟡 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s2k-h4-d64-float16] | 0.0628 | 2.14 | 0.34 | fla 98.7% | - |
| 🟡 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s2k-h4-d64-bfloat16] | 0.0630 | 2.13 | 0.34 | fla 99.0% | - |
| 🟡 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s4k-h4-d64-float16] | 0.1096 | 2.45 | 0.38 | fla 89.9% | - |
| 🟡 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s4k-h4-d64-bfloat16] | 0.1097 | 2.45 | 0.38 | fla 90.6% | - |
| 🟡 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s8k-h4-d64-float16] | 0.2336 | 2.30 | 0.36 | fla 81.0% | - |
| 🟡 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s8k-h4-d64-bfloat16] | 0.2348 | 2.29 | 0.36 | fla 81.6% | - |
| 🔴 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s16k-h4-d64-float16] | 0.4725 | 2.27 | 0.36 | fla 77.6% | - |
| 🔴 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s16k-h4-d64-bfloat16] | 0.4734 | 2.27 | 0.36 | fla 78.1% | - |
| 🟡 | DivFwdOp | test_binary_arith_bench[div-1024x4096-float16-float16-DivFwdOp-div-positive] | 0.0085 | 0.49 | 2.96 | torch 103.0%, torch-compile 99.6% | - |
| 🟡 | DivFwdOp | test_binary_arith_bench[div-1024x10240-float16-float16-DivFwdOp-div-positive] | 0.0182 | 0.58 | 3.46 | torch 101.6%, torch-compile 99.1% | - |
| 🟡 | DivFwdOp | test_binary_arith_bench[div-1024x11008-float16-float16-DivFwdOp-div-positive] | 0.0190 | 0.59 | 3.56 | torch 101.4%, torch-compile 98.9% | - |
| 🟡 | DivFwdOp | test_div_manifest_bench[hidden-state-prefill-float16] | 0.0149 | 0.56 | 3.38 | torch 101.8%, torch-compile 98.4% | - |
| 🟡 | DivFwdOp | test_div_manifest_bench[hidden-state-prefill-bfloat16] | 0.0147 | 0.57 | 3.43 | torch 102.8%, torch-compile 99.8% | - |
| 🔵 | DivFwdOp | test_div_manifest_bench[hidden-state-prefill-float32] | 0.0263 | 0.32 | 3.83 | torch 100.8%, torch-compile 106.6% | - |
| 🔴 | DivFwdOp | test_div_manifest_bench[cnn-feat-broadcast-float16] | 0.0187 | 0.69 | 2.75 | torch 271.6%, torch-compile 79.1% | - |
| 🟡 | DivFwdOp | test_div_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0174 | 0.74 | 2.96 | torch 294.7%, torch-compile 82.7% | - |
| 🟡 | DivFwdOp | test_div_manifest_bench[cnn-feat-broadcast-float32] | 0.0269 | 0.48 | 3.81 | torch 196.1%, torch-compile 98.3% | - |
| 🟢 | DropoutFwdOp | test_dropout_bench[tokens-1k-hidden-4k-float16] | 0.0062 | 0.68 | 2.72 | torch 189.1%, torch-compile 182.9% | - |
| 🔵 | DropoutFwdOp | test_dropout_bench[tokens-1k-hidden-4k-float32] | 0.0103 | 0.41 | 3.26 | torch 144.4%, torch-compile 116.5% | - |
| 🟢 | DropoutFwdOp | test_dropout_bench[tokens-1k-hidden-10k-bfloat16] | 0.0123 | 0.85 | 3.41 | torch 192.5%, torch-compile 191.7% | - |
| 🔵 | EluFwdOp | test_elu_manifest_bench[mlp-hidden-float16] | 0.0122 | 2.76 | 2.76 | torch 147.6%, torch-compile 130.8% | - |
| 🔵 | EluFwdOp | test_elu_manifest_bench[mlp-hidden-bfloat16] | 0.0120 | 2.79 | 2.79 | torch 150.8%, torch-compile 139.1% | - |
| 🔵 | EluFwdOp | test_elu_manifest_bench[mlp-hidden-wide-float16] | 0.0219 | 3.07 | 3.07 | torch 150.3%, torch-compile 136.2% | - |
| 🔵 | EluFwdOp | test_elu_manifest_bench[mlp-hidden-wide-bfloat16] | 0.0216 | 3.11 | 3.11 | torch 154.4%, torch-compile 145.2% | - |
| 🔴 | EngramDecodeFwdOp | test_engram_decode_bench[decode-b1-dmem512-d256-float16] | 0.0329 | 0.02 | 0.02 | torch-ref 286.2%, torch-compile 39.8% | - |
| 🔴 | EngramDecodeFwdOp | test_engram_decode_bench[decode-b4-dmem1024-d512-float16] | 0.0827 | 0.10 | 0.03 | torch-ref 146.4%, torch-compile 30.8% | - |
| 🔴 | EngramDecodeFwdOp | test_engram_decode_bench[decode-b8-dmem512-d256-bfloat16] | 0.0334 | 0.13 | 0.02 | torch-ref 333.8%, torch-compile 63.8% | - |
| 🟢 | EngramGateConvBwdOp | test_engram_gate_conv_bwd_bench[bwd-b1-s32-d256-float16] | 0.0111 | 0.04 | 0.02 | torch 1513.8%, torch-compile 432.2% | - |
| 🟢 | EngramGateConvBwdOp | test_engram_gate_conv_bwd_bench[bwd-b2-s64-d512-float16] | 0.0198 | 0.20 | 0.07 | torch 1015.2%, torch-compile 294.6% | - |
| 🟢 | EngramGateConvBwdOp | test_engram_gate_conv_bwd_bench[bwd-b1-s128-d256-bfloat16] | 0.0168 | 0.12 | 0.04 | torch 1100.9%, torch-compile 320.6% | - |
| 🟢 | EngramGateConvFwdOp | test_engram_gate_conv_fwd_bench[fwd-b1-s32-d256-float16] | 0.0040 | 0.05 | 0.02 | torch-ref 1849.7%, torch-compile 255.2% | - |
| 🟢 | EngramGateConvFwdOp | test_engram_gate_conv_fwd_bench[fwd-b2-s64-d512-float16] | 0.0051 | 0.31 | 0.13 | torch-ref 1690.5%, torch-compile 262.7% | - |
| 🟢 | EngramGateConvFwdOp | test_engram_gate_conv_fwd_bench[fwd-b1-s128-d256-bfloat16] | 0.0045 | 0.18 | 0.07 | torch-ref 1789.3%, torch-compile 282.2% | - |
| 🟡 | EqFwdOp | test_comparison_bench[eq-1024x4096-float16-eq] | 0.0080 | 0.52 | 2.61 | torch 97.6%, torch-compile 97.6% | - |
| 🟡 | EqFwdOp | test_comparison_bench[eq-1024x10240-float16-eq] | 0.0172 | 0.61 | 3.05 | torch 93.1%, torch-compile 93.1% | - |
| 🟡 | EqFwdOp | test_eq_manifest_bench[hidden-state-prefill-float16] | 0.0141 | 0.59 | 2.97 | torch 96.1%, torch-compile 96.1% | - |
| 🟡 | EqFwdOp | test_eq_manifest_bench[hidden-state-prefill-bfloat16] | 0.0140 | 0.60 | 3.01 | torch 93.8%, torch-compile 94.0% | - |
| 🔵 | EqFwdOp | test_eq_manifest_bench[hidden-state-prefill-float32] | 0.0223 | 0.38 | 3.39 | torch 100.4%, torch-compile 100.1% | - |
| 🔴 | EqFwdOp | test_eq_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.81 | 2.42 | torch 299.4%, torch-compile 75.2% | - |
| 🔴 | EqFwdOp | test_eq_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.81 | 2.42 | torch 306.4%, torch-compile 75.1% | - |
| 🟡 | EqFwdOp | test_eq_manifest_bench[cnn-feat-broadcast-float32] | 0.0215 | 0.60 | 2.99 | torch 222.9%, torch-compile 86.0% | - |
| 🟡 | ErfFwdOp | test_erf_bench[elementwise-16M-float16] | 0.0283 | 0.59 | 2.37 | torch 93.3%, torch-compile 103.3% | - |
| 🟡 | ErfFwdOp | test_erf_bench[elementwise-16M-bfloat16] | 0.0286 | 0.59 | 2.35 | torch 97.4%, torch-compile 104.0% | - |
| 🟡 | ErfFwdOp | test_erf_bench[elementwise-16M-float32] | 0.0354 | 0.47 | 3.80 | torch 97.2%, torch-compile 97.7% | - |
| 🟡 | ErfFwdOp | test_erf_bench[elementwise-256M-float16] | 0.4210 | 0.64 | 2.55 | torch 91.6%, torch-compile 102.4% | - |
| 🟡 | ErfFwdOp | test_erf_bench[elementwise-256M-bfloat16] | 0.4239 | 0.63 | 2.53 | torch 95.9%, torch-compile 103.0% | - |
| 🟡 | ExpFwdOp | test_exp_bench[elementwise-16M-float16] | 0.0182 | 0.92 | 3.69 | torch 100.0%, torch-compile 99.8% | - |
| 🟡 | ExpFwdOp | test_exp_bench[elementwise-16M-bfloat16] | 0.0184 | 0.91 | 3.65 | torch 99.8%, torch-compile 100.4% | - |
| 🟡 | ExpFwdOp | test_exp_bench[elementwise-16M-float32] | 0.0341 | 0.49 | 3.93 | torch 99.9%, torch-compile 99.6% | - |
| 🟡 | ExpFwdOp | test_exp_bench[elementwise-256M-float16] | 0.2589 | 1.04 | 4.15 | torch 99.1%, torch-compile 99.1% | - |
| 🟡 | ExpFwdOp | test_exp_bench[elementwise-256M-bfloat16] | 0.2613 | 1.03 | 4.11 | torch 99.1%, torch-compile 100.8% | - |
| 🔵 | Expm1FwdOp | test_expm1_bench[elementwise-16M-float16] | 0.0182 | 1.84 | 3.69 | torch 138.8%, torch-compile 147.3% | - |
| 🟢 | Expm1FwdOp | test_expm1_bench[elementwise-16M-bfloat16] | 0.0183 | 1.83 | 3.67 | torch 153.2%, torch-compile 153.5% | - |
| 🔵 | Expm1FwdOp | test_expm1_bench[elementwise-16M-float32] | 0.0341 | 0.98 | 3.93 | torch 100.3%, torch-compile 100.8% | - |
| 🔵 | Expm1FwdOp | test_expm1_bench[elementwise-256M-float16] | 0.2586 | 2.08 | 4.15 | torch 142.2%, torch-compile 152.4% | - |
| 🟢 | Expm1FwdOp | test_expm1_bench[elementwise-256M-bfloat16] | 0.2613 | 2.05 | 4.11 | torch 157.5%, torch-compile 157.2% | - |
| 🔴 | FFTC2CFwdOp | test_fft_bench[fft-4k-c64-unbatched-complex64] | 0.0082 | 0.03 | 0.01 | torch-cufft 66.7%, torch-compile 67.1% | - |
| 🔴 | FFTC2CFwdOp | test_fft_bench[fft-4k-c64-b64-complex64] | 0.0152 | 1.03 | 0.28 | torch-cufft 36.9%, torch-compile 37.0% | - |
| 🔴 | FFTC2CFwdOp | test_fft_bench[fft-4k-c128-b64-complex128] | 0.0305 | 0.52 | 0.28 | torch-cufft 27.8%, torch-compile 27.8% | - |
| 🟢 | FP8LightningIndexerFwdOp | test_fp8_lightning_indexer_bench[lightning-indexer-s8k-h32-d64-bfloat16] | 0.1627 | 52.78 | 1.87 | torch-ref 15849.4%, torch-compile 7688.3% | - |
| 🟡 | FP8QuantFwdOp | test_fp8_quant_bench[kv-index-8k-d64-float16] | 0.0028 | 1.15 | 0.58 | torch-ref 608.1%, torch-compile 90.7% | - |
| 🟢 | FP8QuantFwdOp | test_fp8_quant_bench[kv-index-8k-d64-bfloat16] | 0.0028 | 1.15 | 0.58 | torch-ref 605.6%, torch-compile 242.9% | - |
| 🔵 | FP8QuantFwdOp | test_fp8_quant_bench[kv-index-4k-d128-float32] | 0.0039 | 0.80 | 0.67 | torch-ref 392.7%, torch-compile 123.6% | - |
| 🔵 | FloorDivideFwdOp | test_binary_arith_bench[floor_divide-1024x4096-float16-float16-FloorDivideFwdOp-floor_divide-positive] | 0.0087 | 0.48 | 2.89 | torch 303.6%, torch-compile 100.4% | - |
| 🔵 | FloorDivideFwdOp | test_binary_arith_bench[floor_divide-1024x10240-float16-float16-FloorDivideFwdOp-floor_divide-positive] | 0.0180 | 0.58 | 3.50 | torch 330.2%, torch-compile 100.2% | - |
| 🔵 | FloorDivideFwdOp | test_floor_divide_manifest_bench[hidden-state-prefill-float16] | 0.0151 | 1.11 | 3.33 | torch 320.8%, torch-compile 100.2% | - |
| 🟡 | FloorDivideFwdOp | test_floor_divide_manifest_bench[hidden-state-prefill-bfloat16] | 0.0149 | 1.12 | 3.37 | torch 337.5%, torch-compile 99.8% | - |
| 🔵 | FloorDivideFwdOp | test_floor_divide_manifest_bench[hidden-state-prefill-float32] | 0.0264 | 0.63 | 3.81 | torch 179.9%, torch-compile 100.6% | - |
| 🔴 | FloorDivideFwdOp | test_floor_divide_manifest_bench[cnn-feat-broadcast-float16] | 0.0198 | 1.29 | 2.59 | torch 557.1%, torch-compile 79.5% | - |
| 🔴 | FloorDivideFwdOp | test_floor_divide_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0200 | 1.28 | 2.57 | torch 568.5%, torch-compile 79.5% | - |
| 🟡 | FloorDivideFwdOp | test_floor_divide_manifest_bench[cnn-feat-broadcast-float32] | 0.0271 | 0.95 | 3.79 | torch 373.0%, torch-compile 98.4% | - |
| 🔵 | FloorFwdOp | test_floor_bench[elementwise-16M-float16] | 0.0180 | 0.93 | 3.74 | torch 100.0%, torch-compile 100.1% | - |
| 🟡 | FloorFwdOp | test_floor_bench[elementwise-16M-bfloat16] | 0.0180 | 0.93 | 3.74 | torch 100.2%, torch-compile 99.8% | - |
| 🟡 | FloorFwdOp | test_floor_bench[elementwise-16M-float32] | 0.0340 | 0.49 | 3.94 | torch 99.9%, torch-compile 99.7% | - |
| 🟡 | FloorFwdOp | test_floor_bench[elementwise-256M-float16] | 0.2532 | 1.06 | 4.24 | torch 98.9%, torch-compile 98.7% | - |
| 🟡 | FloorFwdOp | test_floor_bench[elementwise-256M-bfloat16] | 0.2533 | 1.06 | 4.24 | torch 98.8%, torch-compile 98.6% | - |
| 🔵 | FusedAddLayerNormFwdOp | test_fused_add_layer_norm_bench[llama-8b-prefill-float16] | 0.0211 | 2.39 | 3.18 | torch-ref 549.8%, torch-compile 130.5% | - |
| 🔵 | FusedAddLayerNormFwdOp | test_fused_add_layer_norm_bench[llama-8b-prefill-bfloat16] | 0.0220 | 2.29 | 3.06 | torch-ref 532.5%, torch-compile 131.2% | - |
| 🔵 | FusedAddLayerNormFwdOp | test_fused_add_layer_norm_bench[llama-8b-decode-bfloat16] | 0.0031 | 0.01 | 0.02 | torch-ref 602.0%, torch-compile 117.8% | - |
| 🔵 | FusedAddLayerNormFwdOp | test_fused_add_layer_norm_bench[llama-70b-prefill-float16] | 0.0440 | 2.29 | 3.05 | torch-ref 516.4%, torch-compile 102.0% | - |
| 🟡 | FusedAddLayerNormFwdOp | test_fused_add_layer_norm_bench[llama-70b-prefill-bfloat16] | 0.0473 | 2.13 | 2.84 | torch-ref 485.3%, torch-compile 97.6% | - |
| 🔵 | FusedAddLayerNormFwdOp | test_fused_add_layer_norm_bench[llama-70b-decode-bfloat16] | 0.0041 | 0.01 | 0.02 | torch-ref 627.9%, torch-compile 135.7% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-8b-prefill-float16] | 0.0208 | 2.02 | 3.23 | flashinfer 92.8%, vllm 90.2%, torch-ref 1283.5%, torch-compile 94.2% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-8b-prefill-bfloat16] | 0.0213 | 1.97 | 3.15 | flashinfer 90.4%, vllm 89.8%, torch-ref 1264.7%, torch-compile 92.5% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-8b-decode-bfloat16] | 0.0027 | 0.01 | 0.02 | flashinfer 87.1%, vllm 109.4%, torch-ref 1060.0%, torch-compile 87.1% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-70b-prefill-float16] | 0.0377 | 2.22 | 3.56 | flashinfer 95.7%, vllm 95.3%, torch-ref 1361.4%, torch-compile 96.2% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-70b-prefill-bfloat16] | 0.0380 | 2.21 | 3.53 | flashinfer 95.4%, vllm 96.0%, torch-ref 1362.7%, torch-compile 96.0% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-70b-decode-bfloat16] | 0.0035 | 0.01 | 0.02 | flashinfer 82.6%, vllm 100.9%, torch-ref 862.4%, torch-compile 85.3% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-405b-prefill-float16] | 0.0767 | 2.19 | 3.50 | flashinfer 93.0%, vllm 101.5%, torch-ref 1281.3%, torch-compile 93.1% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-405b-prefill-bfloat16] | 0.0855 | 1.96 | 3.14 | flashinfer 83.8%, vllm 91.5%, torch-ref 1159.5%, torch-compile 84.5% | - |
| 🔴 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-405b-decode-bfloat16] | 0.0062 | 0.01 | 0.03 | flashinfer 69.6%, vllm 80.4%, torch-ref 510.8%, torch-compile 100.5% | - |
| 🔵 | FusedMoEExpertsNopadPersistent3WGFwdOp | test_moe_experts_nopad_bench[qwen3-235b-decode-bfloat16] | 2.7716 | 130.17 | 4.07 | vllm-triton 103.0% | - |
| 🔵 | FusedMoEExpertsNopadPersistent3WGFwdOp | test_moe_experts_nopad_bench[qwen3-235b-prefill-bfloat16] | 5.8360 | 494.56 | 1.95 | vllm-triton 121.8% | - |
| 🔵 | FusedMoEExpertsNopadPersistent3WGFwdOp | test_moe_experts_nopad_bench[deepseek-v3-decode-bfloat16] | 5.4208 | 66.55 | 4.16 | vllm-triton 101.7% | - |
| 🔵 | FusedMoEExpertsNopadPersistent3WGFwdOp | test_moe_experts_nopad_bench[deepseek-v3-prefill-bfloat16] | 8.4428 | 341.86 | 2.68 | vllm-triton 103.9% | - |
|  | FusedMoEExpertsNopadPersistent3WGFwdOp | test_moe_experts_nopad_bench[deepseek-v3-ep2-decode-bfloat16] | 2.7242 | 132.43 | 4.14 | - | - |
|  | FusedMoEExpertsNopadPersistent3WGFwdOp | test_moe_experts_nopad_bench[deepseek-v3-ep2-prefill-bfloat16] | 4.1363 | 697.79 | 2.75 | - | - |
| 🔵 | FusedMoeFwdOp | test_fused_moe_fwd_bench[qwen3-235b-decode-bfloat16] | 2.7751 | 130.01 | 4.07 | vllm 103.0% | - |
| 🔵 | FusedMoeFwdOp | test_fused_moe_fwd_bench[qwen3-235b-prefill-bfloat16] | 6.0392 | 477.92 | 1.89 | vllm 121.2% | - |
| 🔵 | FusedMoeFwdOp | test_fused_moe_fwd_bench[deepseek-v3-decode-bfloat16] | 5.4201 | 66.56 | 4.16 | vllm 101.9% | - |
| 🔵 | FusedMoeFwdOp | test_fused_moe_fwd_bench[deepseek-v3-prefill-bfloat16] | 8.3027 | 347.62 | 2.73 | vllm 106.7% | - |
| 🟢 | FusedMoeFwdOp | test_fused_moe_fwd_bench[kimi-k2-decode-bfloat16] | 3.8921 | 92.69 | 5.80 | torch-ref 1455.2% | - |
| 🟢 | FusedMoeFwdOp | test_fused_moe_fwd_bench[kimi-k2-prefill-bfloat16] | 7.9623 | 362.49 | 2.85 | torch-ref 1768.3% | - |
| 🟡 | FusedTopKOp | test_fused_topk_bench[1-384-8-sigmoid-renormalize] | 0.0083 | 0.00 | 0.00 | vllm 99.6% | - |
| 🟡 | FusedTopKOp | test_fused_topk_bench[32-384-8-sigmoid-renormalize] | 0.0119 | 0.02 | 0.00 | vllm 81.7% | - |
| 🟡 | FusedTopKOp | test_fused_topk_bench[512-384-8-sigmoid-renormalize] | 0.0126 | 0.28 | 0.03 | vllm 83.2% | - |
| 🔵 | FusedTopKOp | test_fused_topk_bench[4096-384-8-sigmoid-renormalize] | 0.0203 | 1.40 | 0.17 | vllm 117.5% | - |
| 🔵 | FusedTopKOp | test_fused_topk_bench[1-128-8-softmax-norenormalize] | 0.0042 | 0.00 | 0.00 | vllm 143.1% | - |
| 🔵 | FusedTopKOp | test_fused_topk_bench[32-128-8-softmax-norenormalize] | 0.0074 | 0.01 | 0.00 | vllm 111.7% | - |
| 🔵 | FusedTopKOp | test_fused_topk_bench[512-128-8-softmax-norenormalize] | 0.0078 | 0.15 | 0.02 | vllm 115.2% | - |
| 🔵 | FusedTopKOp | test_fused_topk_bench[4096-128-8-softmax-norenormalize] | 0.0110 | 0.86 | 0.12 | vllm 147.5% | - |
| 🟡 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s2k-h4-d64-float16] | 0.1828 | 1.47 | 0.17 | fla 81.0% | - |
| 🟡 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s2k-h4-d64-bfloat16] | 0.1845 | 1.45 | 0.17 | fla 80.3% | - |
| 🔴 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s4k-h4-d64-float16] | 0.3696 | 1.45 | 0.17 | fla 77.9% | - |
| 🔴 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s4k-h4-d64-bfloat16] | 0.3645 | 1.47 | 0.17 | fla 79.1% | - |
| 🔴 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s8k-h4-d64-float16] | 0.7442 | 1.44 | 0.17 | fla 74.9% | - |
| 🔴 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s8k-h4-d64-bfloat16] | 0.7275 | 1.48 | 0.17 | fla 76.5% | - |
| 🔴 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s16k-h4-d64-float16] | 1.5163 | 1.42 | 0.17 | fla 71.4% | - |
| 🔴 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s16k-h4-d64-bfloat16] | 1.4488 | 1.48 | 0.17 | fla 74.7% | - |
| 🟡 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b1-h8-d128-bfloat16] | 0.0074 | 0.07 | 0.07 | fla 91.0%, torch 410.4%, torch-compile 81.9% | - |
| 🟡 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b1-h16-d128-bfloat16] | 0.0074 | 0.14 | 0.14 | fla 94.0%, torch 428.0%, torch-compile 93.5% | - |
| 🟡 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b1-h32-d128-bfloat16] | 0.0078 | 0.27 | 0.27 | fla 93.4%, torch 459.8%, torch-compile 99.2% | - |
| 🔵 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b1-h48-d128-bfloat16] | 0.0080 | 0.40 | 0.40 | fla 112.1%, torch 507.6%, torch-compile 120.5% | - |
| 🔵 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b1-h64-d128-bfloat16] | 0.0082 | 0.52 | 0.52 | fla 109.4%, torch 516.9%, torch-compile 107.8% | - |
| 🔵 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b8-h32-d128-bfloat16] | 0.0159 | 1.06 | 1.08 | fla 108.3%, torch 564.9%, torch-compile 133.3% | - |
| 🟡 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b8-h48-d128-bfloat16] | 0.0231 | 1.10 | 1.11 | fla 96.5%, torch 523.2%, torch-compile 106.5% | - |
| 🟡 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b8-h64-d128-bfloat16] | 0.0305 | 1.11 | 1.12 | fla 89.4%, torch 519.7%, torch-compile 104.4% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-float16] | 0.0984 | 1.36 | 0.11 | fla 71.4% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-bfloat16] | 0.0970 | 1.38 | 0.11 | fla 68.0% | - |
| 🟡 | GLAFwdOp | test_gla_fwd_bench[gla-init-b2-s4k-h4-d64-float16] | 0.1567 | 1.71 | 0.13 | fla 80.0% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-init-b2-s4k-h4-d64-bfloat16] | 0.1564 | 1.72 | 0.13 | fla 76.4% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-float16] | 0.3127 | 1.72 | 0.13 | fla 79.2% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-bfloat16] | 0.3115 | 1.72 | 0.14 | fla 70.6% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-float16] | 0.6175 | 1.74 | 0.14 | fla 75.3% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-bfloat16] | 0.6111 | 1.76 | 0.14 | fla 74.1% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-float16] | 0.0866 | 12.40 | 0.20 | fla 77.6% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-bfloat16] | 0.0866 | 12.40 | 0.20 | fla 77.9% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-float16] | 0.1488 | 14.43 | 0.23 | fla 72.4% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-bfloat16] | 0.1444 | 14.87 | 0.23 | fla 74.9% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-float16] | 0.3140 | 13.68 | 0.21 | fla 65.3% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-bfloat16] | 0.3160 | 13.59 | 0.21 | fla 65.0% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-float16] | 0.6347 | 13.53 | 0.21 | fla 61.6% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-bfloat16] | 0.6374 | 13.48 | 0.21 | fla 61.7% | - |
| 🔵 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s2k-h4-d64-float16] | 0.0669 | 16.05 | 0.25 | fla 100.4% | - |
| 🔵 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s2k-h4-d64-bfloat16] | 0.0663 | 16.19 | 0.25 | fla 101.7% | - |
| 🟡 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s4k-h4-d64-float16] | 0.1151 | 18.66 | 0.29 | fla 93.5% | - |
| 🟡 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s4k-h4-d64-bfloat16] | 0.1146 | 18.75 | 0.29 | fla 94.5% | - |
| 🟡 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s8k-h4-d64-float16] | 0.2194 | 19.58 | 0.31 | fla 93.5% | - |
| 🟡 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s8k-h4-d64-bfloat16] | 0.2203 | 19.49 | 0.31 | fla 93.3% | - |
| 🟡 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s16k-h4-d64-float16] | 0.4291 | 20.02 | 0.31 | fla 91.0% | - |
| 🟡 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s16k-h4-d64-bfloat16] | 0.4324 | 19.86 | 0.31 | fla 91.0% | - |
| 🟢 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s32k-h4-d64-float16] | 0.1939 | 88.60 | 1.39 | fla 395.6% | - |
| 🟢 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s32k-h4-d64-bfloat16] | 0.1947 | 88.23 | 1.38 | fla 395.0% | - |
| 🔵 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b1-s4k-h16-d128-float16] | 0.1751 | 58.25 | 0.77 | fla 110.4% | - |
| 🔵 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b1-s4k-h16-d128-bfloat16] | 0.1745 | 58.46 | 0.77 | fla 111.5% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-float16] | 0.2017 | 1.33 | 0.08 | fla 66.3% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-bfloat16] | 0.2050 | 1.31 | 0.08 | fla 68.3% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-float16] | 0.3808 | 1.41 | 0.09 | fla 65.4% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-bfloat16] | 0.3876 | 1.39 | 0.09 | fla 66.7% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-float16] | 0.7237 | 1.48 | 0.09 | fla 67.2% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-bfloat16] | 0.7508 | 1.43 | 0.09 | fla 66.9% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-float16] | 1.4280 | 1.50 | 0.09 | fla 64.4% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-bfloat16] | 1.4648 | 1.47 | 0.09 | fla 65.1% | - |
| 🔵 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b1-h8-d128-bfloat16] | 0.0031 | 0.25 | 0.17 | fla 128.9% | - |
| 🔵 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b1-h16-d128-bfloat16] | 0.0033 | 0.47 | 0.32 | fla 126.0% | - |
| 🔵 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b1-h32-d128-bfloat16] | 0.0036 | 0.87 | 0.59 | fla 130.1% | - |
| 🔵 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b1-h48-d128-bfloat16] | 0.0038 | 1.23 | 0.83 | fla 136.7% | - |
| 🔵 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b1-h64-d128-bfloat16] | 0.0042 | 1.50 | 1.02 | fla 138.2% | - |
| 🟢 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b8-h32-d128-bfloat16] | 0.0087 | 2.91 | 1.96 | fla 168.6% | - |
| 🟢 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b8-h48-d128-bfloat16] | 0.0124 | 3.05 | 2.06 | fla 155.7% | - |
| 🟢 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b8-h64-d128-bfloat16] | 0.0161 | 3.14 | 2.12 | fla 155.9% | - |
|  | GatedDeltaNetPrefillBHTDFwdOp | test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-float16] | 0.2512 | 34.20 | 0.34 | - | - |
|  | GatedDeltaNetPrefillBHTDFwdOp | test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-bfloat16] | 0.2517 | 34.13 | 0.34 | - | - |
|  | GatedDeltaNetPrefillBHTDFwdOp | test_gated_deltanet_prefill_bhtd_bench[bhtd-qwen35-gdn-prefill-b1-s128k-h64-d128-float16] | 17.4261 | 63.10 | 0.62 | - | - |
|  | GatedDeltaNetPrefillBHTDFwdOp | test_gated_deltanet_prefill_bhtd_bench[bhtd-qwen35-gdn-prefill-b1-s128k-h64-d128-bfloat16] | 17.5499 | 62.65 | 0.61 | - | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[fallback-gdn-prefill-b1-s4k-h16-d128-bthd-float16] | 0.0794 | 108.17 | 1.07 | fla 247.1% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[fallback-gdn-prefill-b1-s4k-h16-d128-bthd-bfloat16] | 0.0791 | 108.64 | 1.07 | fla 249.9% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h16-d128-bthd-float16] | 0.3654 | 188.06 | 1.84 | fla 400.6% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h16-d128-bthd-bfloat16] | 0.3704 | 185.50 | 1.82 | fla 396.8% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h16-d128-bthd-float16] | 0.6975 | 197.04 | 1.93 | fla 416.4% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h16-d128-bthd-bfloat16] | 0.7071 | 194.37 | 1.90 | fla 412.5% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h16-d128-bthd-float16] | 1.2565 | 218.76 | 2.14 | fla 459.4% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h16-d128-bthd-bfloat16] | 1.2852 | 213.89 | 2.10 | fla 449.4% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h32-d128-bthd-float16] | 0.6882 | 199.70 | 1.96 | fla 321.4% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h32-d128-bthd-bfloat16] | 0.6972 | 197.14 | 1.93 | fla 317.7% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h32-d128-bthd-float16] | 1.2478 | 220.29 | 2.16 | fla 352.6% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h32-d128-bthd-bfloat16] | 1.2809 | 214.59 | 2.10 | fla 344.2% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h32-d128-bthd-float16] | 2.4526 | 224.15 | 2.20 | fla 356.7% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h32-d128-bthd-bfloat16] | 2.5032 | 219.62 | 2.15 | fla 350.4% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h48-d128-bthd-float16] | 1.0526 | 195.85 | 1.92 | fla 300.7% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h48-d128-bthd-bfloat16] | 1.0662 | 193.36 | 1.90 | fla 296.4% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h48-d128-bthd-float16] | 1.9159 | 215.21 | 2.11 | fla 329.5% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h48-d128-bthd-bfloat16] | 1.9451 | 211.98 | 2.08 | fla 324.0% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h48-d128-bthd-float16] | 3.7749 | 218.45 | 2.14 | fla 333.9% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h48-d128-bthd-bfloat16] | 3.8140 | 216.22 | 2.12 | fla 329.8% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h64-d128-bthd-float16] | 1.2252 | 224.36 | 2.20 | fla 319.3% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h64-d128-bthd-bfloat16] | 1.2543 | 219.15 | 2.15 | fla 311.6% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h64-d128-bthd-float16] | 2.3763 | 231.35 | 2.27 | fla 328.8% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h64-d128-bthd-bfloat16] | 2.4267 | 226.55 | 2.22 | fla 321.3% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h64-d128-bthd-float16] | 4.6609 | 235.90 | 2.31 | fla 335.0% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h64-d128-bthd-bfloat16] | 4.7823 | 229.91 | 2.25 | fla 326.0% | - |
| 🟡 | GeFwdOp | test_comparison_bench[ge-1024x4096-float16-ge] | 0.0079 | 0.53 | 2.64 | torch 98.0%, torch-compile 98.0% | - |
| 🟡 | GeFwdOp | test_ge_manifest_bench[hidden-state-prefill-float16] | 0.0142 | 0.59 | 2.96 | torch 93.5%, torch-compile 93.0% | - |
| 🟡 | GeFwdOp | test_ge_manifest_bench[hidden-state-prefill-bfloat16] | 0.0140 | 0.60 | 2.99 | torch 93.3%, torch-compile 93.2% | - |
| 🟡 | GeFwdOp | test_ge_manifest_bench[hidden-state-prefill-float32] | 0.0224 | 0.37 | 3.37 | torch 99.9%, torch-compile 99.6% | - |
| 🔴 | GeFwdOp | test_ge_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.81 | 2.42 | torch 294.8%, torch-compile 74.1% | - |
| 🔴 | GeFwdOp | test_ge_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.81 | 2.43 | torch 300.0%, torch-compile 75.6% | - |
| 🟡 | GeFwdOp | test_ge_manifest_bench[cnn-feat-broadcast-float32] | 0.0213 | 0.60 | 3.02 | torch 220.3%, torch-compile 86.5% | - |
| 🔵 | GeluAndMulFwdOp | test_gelu_and_mul_bench[ffn-gelu-prefill-float16] | 0.0550 | 3.20 | 3.20 | flashinfer 190.5%, torch-ref 368.4%, torch-compile 109.4% | - |
| 🔵 | GeluAndMulFwdOp | test_gelu_and_mul_bench[ffn-gelu-prefill-bfloat16] | 0.0594 | 2.97 | 2.97 | flashinfer 178.6%, torch-ref 345.1%, torch-compile 103.3% | - |
| 🟡 | GeluAndMulFwdOp | test_gelu_and_mul_bench[ffn-gelu-decode-bfloat16] | 0.0016 | 0.05 | 0.05 | flashinfer 424.5%, torch-ref 204.1%, torch-compile 93.9% | - |
| 🟡 | GeluFwdOp | test_gelu_manifest_bench[llama-8b-ffn-prefill-float16] | 0.0529 | 2.78 | 2.22 | torch 90.4%, torch-compile 102.0% | - |
| 🟡 | GeluFwdOp | test_gelu_manifest_bench[llama-8b-ffn-prefill-bfloat16] | 0.0557 | 2.63 | 2.11 | torch 87.9%, torch-compile 100.2% | - |
| 🟡 | GeluFwdOp | test_gelu_manifest_bench[llama-8b-ffn-decode-bfloat16] | 0.0016 | 0.05 | 0.04 | torch 106.1%, torch-compile 91.8% | - |
| 🔵 | GeluTanhAndMulFwdOp | test_gelu_tanh_and_mul_bench[ffn-gelu-tanh-prefill-float16] | 0.0478 | 6.14 | 3.68 | flashinfer 118.0%, torch-ref 401.2%, torch-compile 107.9% | - |
| 🔵 | GeluTanhAndMulFwdOp | test_gelu_tanh_and_mul_bench[ffn-gelu-tanh-prefill-bfloat16] | 0.0491 | 5.98 | 3.59 | flashinfer 116.8%, torch-ref 393.7%, torch-compile 107.0% | - |
| 🔵 | GeluTanhAndMulFwdOp | test_gelu_tanh_and_mul_bench[ffn-gelu-tanh-decode-bfloat16] | 0.0015 | 0.10 | 0.06 | flashinfer 297.8%, torch-ref 208.6%, torch-compile 100.0% | - |
| 🟢 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-decode-gate-up-per-tensor-float8_e4m3fn] | 0.1162 | 33.35 | 0.14 | torch-scaled-mm 208.1% | - |
| 🟢 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-decode-down-per-tensor-float8_e4m3fn] | 0.0254 | 148.00 | 0.66 | torch-scaled-mm 966.4% | - |
| 🟢 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-prefill-gate-up-per-tensor-float8_e4m3fn] | 0.5121 | 242.18 | 0.12 | torch-scaled-mm 672.8% | - |
| 🟢 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-prefill-down-per-tensor-float8_e4m3fn] | 0.2097 | 573.49 | 0.39 | torch-scaled-mm 1594.6% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-decode-gate-up-block128-float8_e4m3fn] | 0.3336 | 11.62 | 0.05 | torch-scaled-mm 83.7%, flashinfer-fp8-blockscale-sm90 3.9% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-decode-down-block128-float8_e4m3fn] | 0.0391 | 96.03 | 0.44 | torch-scaled-mm 715.3%, flashinfer-fp8-blockscale-sm90 23.7% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-prefill-gate-up-block128-float8_e4m3fn] | 1.3499 | 91.87 | 0.05 | torch-scaled-mm 261.7%, flashinfer-fp8-blockscale-sm90 10.3% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-prefill-down-block128-float8_e4m3fn] | 0.4475 | 268.74 | 0.18 | torch-scaled-mm 758.7%, flashinfer-fp8-blockscale-sm90 31.9% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-prefill-attn-proj-block128-float8_e4m3fn] | 0.8094 | 297.14 | 0.12 | torch-scaled-mm 824.9%, flashinfer-fp8-blockscale-sm90 26.5% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[k-dominant-7168x16384-block128-float8_e4m3fn] | 3.6193 | 265.82 | 0.07 | torch-scaled-mm 732.6%, flashinfer-fp8-blockscale-sm90 21.3% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[wide-n-24576-block128-float8_e4m3fn] | 1.0394 | 297.50 | 0.24 | torch-scaled-mm 819.5%, flashinfer-fp8-blockscale-sm90 36.9% | - |
| 🟢 | GemmFp8FwdOp | test_gemm_fp8_bench[small-batch-down-m8-per-tensor-float8_e4m3fn] | 0.0267 | 8.81 | 0.56 | torch-scaled-mm 624.7% | - |
| 🟢 | GemmFp8FwdOp | test_gemm_fp8_bench[gemv-down-m1-per-tensor-float8_e4m3fn] | 0.0258 | 1.14 | 0.57 | torch-scaled-mm 506.9% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[gemv-down-m1-block128-float8_e4m3fn] | 0.0628 | 0.47 | 0.24 | torch-scaled-mm 261.0%, flashinfer-fp8-blockscale-sm90 12.4% | - |
| 🟢 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-decode-gate-up-per-tensor-bias-float8_e4m3fn] | 0.1163 | 33.34 | 0.14 | torch-scaled-mm 208.1% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[square-1k-nn-float16] | 0.0145 | 148.47 | 0.43 | torch-cublas 50.0%, flaggems 81.6% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[square-1k-nn-bfloat16] | 0.0144 | 148.63 | 0.44 | torch-cublas 49.8%, flaggems 81.7% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[ds-v3-decode-gate-up-bfloat16] | 0.0677 | 57.26 | 0.48 | torch-cublas 25.5% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[ds-v3-decode-down-bfloat16] | 0.0247 | 152.32 | 1.29 | torch-cublas 53.4% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[ds-v3-prefill-gate-up-bfloat16] | 0.3369 | 368.15 | 0.32 | torch-cublas 52.7% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[ds-v3-prefill-down-bfloat16] | 0.3212 | 374.35 | 0.33 | torch-cublas 55.7% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[ds-v3-prefill-attn-proj-float16] | 0.5419 | 443.83 | 0.28 | torch-cublas 61.8% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[ds-v3-prefill-attn-proj-bfloat16] | 0.5399 | 445.50 | 0.28 | torch-cublas 61.5% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[k-dominant-7168x16384-bfloat16] | 2.0616 | 466.66 | 0.21 | torch-cublas 61.4% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[wide-n-24576-bfloat16] | 0.8996 | 343.74 | 0.32 | torch-cublas 50.2% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[mid-m16-attn-bfloat16] | 0.0657 | 14.29 | 0.90 | torch-cublas 37.3% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[mid-m32-attn-bfloat16] | 0.0661 | 28.43 | 0.90 | torch-cublas 36.8% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[mid-m64-down-bfloat16] | 0.0207 | 90.76 | 1.48 | torch-cublas 63.7% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[mid-m96-gate-up-bfloat16] | 0.0687 | 42.33 | 0.47 | torch-cublas 24.6% | - |
| 🔴 | GemmW4A16FwdOp | test_gemm_w4a16_bench[compile-smoke-square-64x64x128-float16] | 0.0043 | 0.25 | 0.01 | torch-dequantized-matmul 63.9% | - |
| 🔴 | GemmW4A16FwdOp | test_gemm_w4a16_bench[compile-smoke-rect-128x256x256-float16] | 0.0059 | 2.87 | 0.03 | torch-dequantized-matmul 52.5% | - |
| 🔴 | GemmW4A16FwdOp | test_gemm_w4a16_bench[decode-l2-resident-ish-float16] | 0.0328 | 4.09 | 1.10 | torch-dequantized-matmul 142.9%, marlin-fp32 66.8%, marlin-fp16 66.8% | - |
| 🔴 | GemmW4A16FwdOp | test_gemm_w4a16_bench[decode-hbm-streaming-threshold-float16] | 0.0607 | 4.42 | 1.19 | torch-dequantized-matmul 122.9%, marlin-fp32 62.3%, marlin-fp16 62.4% | - |
| 🔴 | GemmW4A16FwdOp | test_gemm_w4a16_bench[decode-non-power2-low-cta-float16] | 0.0746 | 3.94 | 1.06 | torch-dequantized-matmul 117.0%, marlin-fp32 54.8%, marlin-fp16 54.5% | - |
| 🔴 | GemmW4A16FwdOp | test_gemm_w4a16_bench[decode-long-k-pressure-float16] | 0.2833 | 4.74 | 1.28 | torch-dequantized-matmul 114.3%, marlin-fp32 49.8%, marlin-fp16 49.7% | - |
| 🔵 | GroupNormFwdOp | test_group_norm_bench[image-g32-affine-float16] | 0.0037 | 1.40 | 1.12 | flaggems 107.7%, torch 408.5%, torch-compile 131.6% | - |
| 🔵 | GroupNormFwdOp | test_group_norm_bench[image-g32-affine-bfloat16] | 0.0037 | 1.41 | 1.13 | flaggems 108.6%, torch 411.2%, torch-compile 141.4% | - |
| 🔴 | GroupNormFwdOp | test_group_norm_bench[wider-channel-g32-affine-float16] | 0.0060 | 0.67 | 0.54 | flaggems 66.7%, torch 273.7%, torch-compile 73.1% | - |
| 🔴 | GroupNormFwdOp | test_group_norm_bench[tail-spatial-g16-affine-float16] | 0.0061 | 0.38 | 0.30 | flaggems 66.8%, torch 252.6%, torch-compile 68.4% | - |
| 🔵 | GroupNormFwdOp | test_group_norm_no_affine_bench[image-g32-float16] | 0.0036 | 0.89 | 1.18 | flaggems 100.9%, torch 371.2%, torch-compile 123.4% | - |
| 🔵 | GroupNormFwdOp | test_group_norm_no_affine_bench[image-g32-bfloat16] | 0.0036 | 0.89 | 1.18 | flaggems 100.9%, torch 372.9%, torch-compile 119.8% | - |
| 🔴 | GroupNormFwdOp | test_group_norm_no_affine_bench[wider-channel-g32-float16] | 0.0048 | 0.50 | 0.67 | flaggems 72.7%, torch 295.0%, torch-compile 76.0% | - |
| 🔴 | GroupNormFwdOp | test_group_norm_no_affine_bench[tail-spatial-g16-float16] | 0.0052 | 0.27 | 0.35 | flaggems 69.3%, torch 256.7%, torch-compile 69.9% | - |
| 🟡 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-8b-short-float16] | 0.2036 | 105.49 | 0.33 | torch-sdpa 88.2% | - |
| 🔴 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-8b-short-bfloat16] | 0.4145 | 51.81 | 0.16 | torch-sdpa 43.3% | - |
| 🟡 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-8b-long-float16] | 0.8329 | 206.27 | 0.16 | torch-sdpa 84.9% | - |
| 🔴 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-8b-long-bfloat16] | 1.2435 | 138.16 | 0.11 | torch-sdpa 56.8% | - |
| 🟡 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-70b-short-float16] | 0.1970 | 109.01 | 0.30 | torch-sdpa 91.0% | - |
| 🔴 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-70b-short-bfloat16] | 0.4082 | 52.60 | 0.14 | torch-sdpa 43.8% | - |
| 🟡 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-70b-long-float16] | 0.8083 | 212.53 | 0.15 | torch-sdpa 87.2% | - |
| 🔴 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 1.0173 | 168.87 | 0.12 | torch-sdpa 69.1% | - |
| 🔴 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-8b-p64-float16] | 0.1666 | 12.89 | 0.10 | flashinfer 75.1% | - |
| 🔵 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-8b-long-p64-float16] | 0.2208 | 19.45 | 0.61 | flashinfer 135.4% | - |
| 🔴 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[throughput-8b-p64-float16] | 0.2516 | 8.54 | 0.04 | flashinfer 59.9% | - |
| 🟡 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-70b-p64-float16] | 0.0496 | 21.63 | 0.34 | flashinfer 89.7% | - |
| 🔴 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-8b-p256-float16] | 0.1682 | 12.77 | 0.10 | flashinfer 74.4% | - |
| 🟡 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-70b-p256-float16] | 0.0686 | 15.66 | 0.25 | flashinfer 83.4% | - |
| 🟢 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-405b-p256-float16] | 0.0564 | 19.05 | 0.30 | torch-ref 7074.9% | - |
| 🔴 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-8b-p64-softcap50-float16] | 0.1763 | 12.18 | 0.10 | flashinfer 71.1% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-8b-4k-float16] | 0.1508 | 14.24 | 3.56 | flashinfer 149.1% | - |
| 🟢 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-8b-4k-bfloat16] | 0.1498 | 14.34 | 3.59 | flashinfer 171.4% | - |
| 🟢 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-8b-32k-float16] | 0.2580 | 16.64 | 4.16 | flashinfer 167.1% | - |
| 🟢 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-8b-32k-bfloat16] | 0.2567 | 16.73 | 4.18 | flashinfer 193.8% | - |
| 🟢 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-70b-4k-float16] | 0.0791 | 27.15 | 3.40 | flashinfer 253.5% | - |
| 🟢 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-70b-4k-bfloat16] | 0.0790 | 27.18 | 3.40 | flashinfer 287.6% | - |
| 🟢 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-70b-32k-float16] | 0.1382 | 31.08 | 3.89 | flashinfer 280.9% | - |
| 🟢 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-70b-32k-bfloat16] | 0.1378 | 31.17 | 3.90 | flashinfer 321.1% | - |
| 🟢 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-8b-4k-softcap50-float16] | 0.1621 | 13.25 | 3.32 | torch-sdpa 8192.6% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-1k-float16] | 0.0070 | 2.40 | 0.30 | flashinfer 139.0% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-4k-float16] | 0.0096 | 6.97 | 0.87 | flashinfer 120.3% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-8k-float16] | 0.0132 | 10.16 | 1.27 | flashinfer 106.8% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-16k-float16] | 0.0180 | 14.95 | 1.87 | flashinfer 121.7% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-32k-float16] | 0.0283 | 18.96 | 2.37 | flashinfer 122.3% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-64k-float16] | 0.0457 | 23.48 | 2.94 | flashinfer 116.4% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-128k-float16] | 0.0764 | 28.11 | 3.51 | flashinfer 109.2% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-256k-float16] | 0.1365 | 31.46 | 3.93 | flashinfer 103.6% | - |
| 🔵 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-8b-short-float16] | 0.0370 | 232.11 | 1.13 | flashinfer 107.1% | - |
| 🔵 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-8b-short-bfloat16] | 0.0369 | 232.71 | 1.14 | flashinfer 105.9% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-8b-long-float16] | 0.1622 | 423.78 | 0.52 | flashinfer 99.8% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-8b-long-bfloat16] | 0.1608 | 427.44 | 0.52 | flashinfer 99.6% | - |
| 🔵 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-70b-short-float16] | 0.0381 | 225.39 | 0.99 | flashinfer 102.6% | - |
| 🔵 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-70b-short-bfloat16] | 0.0380 | 225.77 | 0.99 | flashinfer 102.4% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-70b-long-float16] | 0.1622 | 423.65 | 0.47 | flashinfer 99.4% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-70b-long-bfloat16] | 0.1614 | 425.67 | 0.47 | flashinfer 99.3% | - |
| 🔵 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-8b-prefill-dense-float16] | 0.0372 | 231.46 | 1.13 | torch-ref 2957.2%, flashinfer 105.8% | - |
| 🔵 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-8b-prefill-dense-bfloat16] | 0.0370 | 232.87 | 1.13 | torch-ref 2978.7%, flashinfer 105.8% | - |
| 🔵 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-8b-prefill-dense-sm-scale-0.125-float16] | 0.0370 | 232.86 | 1.13 | torch-ref 2971.6%, flashinfer 106.8% | - |
| 🔵 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-8b-prefill-dense-softcap50-float16] | 0.0421 | 204.53 | 1.00 | torch-ref 3076.2%, flashinfer 108.9% | - |
| 🟡 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-8b-prefill-dense-q-lt-kv-float16] | 0.1259 | 511.70 | 0.40 | torch-ref 3251.7%, flashinfer 99.8% | - |
| 🟡 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-8b-prefill-dense-q-lt-kv-bfloat16] | 0.1249 | 515.96 | 0.40 | torch-ref 3276.0%, flashinfer 99.8% | - |
| 🟡 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-70b-prefill-dense-q-lt-kv-float16] | 0.1256 | 512.80 | 0.27 | torch-ref 2997.2%, flashinfer 99.9% | - |
| 🔵 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-70b-prefill-dense-q-lt-kv-bfloat16] | 0.1237 | 520.83 | 0.27 | torch-ref 3042.7%, flashinfer 100.3% | - |
|  | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s896-float16] | 0.0452 | 290.69 | 0.20 | - | - |
|  | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s896-bfloat16] | 0.0453 | 290.28 | 0.20 | - | - |
|  | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s1792-float16] | 0.1290 | 407.98 | 0.14 | - | - |
|  | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s1792-bfloat16] | 0.1290 | 407.98 | 0.14 | - | - |
|  | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s3584-float16] | 0.7505 | 560.86 | 0.09 | - | - |
|  | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s3584-bfloat16] | 0.7504 | 560.88 | 0.09 | - | - |
|  | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s7168-float16] | 2.8485 | 591.05 | 0.05 | - | - |
|  | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s7168-bfloat16] | 2.8447 | 591.84 | 0.05 | - | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-prefill-paged-fullattn-b8-prefix32k-chunk1k-p64-partial-rope64-float16] | 60.6312 | 147.34 | 0.04 | - | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-prefill-paged-fullattn-mixed-b8-p64-partial-rope64-float16] | 30.7499 | 107.94 | 0.04 | - | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-prefill-paged-b8-prefix4k-chunk512-p64-full-rope-float16] | 1.9495 | 149.83 | 0.12 | - | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[gqa-prefill-paged-softcap50-b4-prefix4k-chunk512-p64-float16] | 0.1500 | 121.68 | 0.10 | - | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-prefill-paged-fp8-cache-b8-prefix32k-chunk1k-p64-float16] | 56.0286 | 159.45 | 0.05 | - | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-prefill-paged-fp8-cache-b8-prefix4k-chunk512-p64-float16] | 1.9999 | 146.05 | 0.12 | - | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[gqa-prefill-paged-fp8-cache-softcap50-b4-prefix4k-chunk512-p64-float16] | 0.2072 | 88.12 | 0.07 | - | - |
| 🟢 | GroupedQueryAttentionPrefillVarlenFwdOp | test_gqa_prefill_varlen_fwd_bench[llama-8b-prefill-varlen-uniform-fp16] | 0.1245 | 207.07 | 0.40 | torch-ref 1637.4% | - |
| 🟢 | GroupedQueryAttentionPrefillVarlenFwdOp | test_gqa_prefill_varlen_fwd_bench[llama-8b-prefill-varlen-mixed-fp16] | 0.1399 | 144.01 | 0.28 | torch-ref 1201.6% | - |
| 🟢 | GroupedQueryAttentionPrefillVarlenFwdOp | test_gqa_prefill_varlen_fwd_bench[llama-70b-prefill-varlen-q-lt-kv-bf16] | 0.1958 | 219.49 | 0.24 | torch-ref 1411.7% | - |
| 🔵 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-8b-short-w256-float16] | 0.0398 | 162.34 | 1.05 | flashinfer 103.5% | - |
| 🔵 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0397 | 162.99 | 1.06 | flashinfer 104.0% | - |
| 🔵 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-8b-long-w1024-float16] | 0.1527 | 337.91 | 0.55 | flashinfer 101.8% | - |
| 🔵 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.1511 | 341.45 | 0.56 | flashinfer 101.0% | - |
| 🔵 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-70b-short-w256-float16] | 0.0395 | 163.92 | 0.96 | flashinfer 103.7% | - |
| 🔵 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-70b-short-w256-bfloat16] | 0.0394 | 164.32 | 0.96 | flashinfer 103.9% | - |
| 🔵 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-70b-long-w1024-float16] | 0.1523 | 338.83 | 0.50 | flashinfer 100.6% | - |
| 🔵 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.1509 | 341.85 | 0.50 | flashinfer 100.3% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-float16] | 0.0571 | 113.23 | 0.73 | flashinfer 72.2% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0568 | 113.87 | 0.74 | flashinfer 72.7% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-float16] | 0.3513 | 293.74 | 0.48 | flashinfer 78.9% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.3505 | 294.38 | 0.48 | flashinfer 78.5% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-float16] | 0.0932 | 138.86 | 0.81 | flashinfer 74.6% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-bfloat16] | 0.0925 | 139.77 | 0.82 | flashinfer 74.3% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-float16] | 0.6710 | 307.53 | 0.45 | flashinfer 77.3% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.6680 | 308.93 | 0.45 | flashinfer 77.6% | - |
| 🟡 | GtFwdOp | test_comparison_bench[gt-1024x4096-float16-gt] | 0.0079 | 0.53 | 2.64 | torch 98.4%, torch-compile 98.0% | - |
| 🟡 | GtFwdOp | test_gt_manifest_bench[hidden-state-prefill-float16] | 0.0140 | 0.60 | 3.00 | torch 94.2%, torch-compile 94.5% | - |
| 🟡 | GtFwdOp | test_gt_manifest_bench[hidden-state-prefill-bfloat16] | 0.0140 | 0.60 | 2.99 | torch 93.8%, torch-compile 94.1% | - |
| 🟡 | GtFwdOp | test_gt_manifest_bench[hidden-state-prefill-float32] | 0.0224 | 0.37 | 3.37 | torch 99.9%, torch-compile 99.3% | - |
| 🔴 | GtFwdOp | test_gt_manifest_bench[cnn-feat-broadcast-float16] | 0.0160 | 0.80 | 2.41 | torch 302.5%, torch-compile 74.8% | - |
| 🔴 | GtFwdOp | test_gt_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.81 | 2.42 | torch 308.0%, torch-compile 75.6% | - |
| 🟡 | GtFwdOp | test_gt_manifest_bench[cnn-feat-broadcast-float32] | 0.0214 | 0.60 | 3.00 | torch 224.0%, torch-compile 85.8% | - |
| 🔴 | HardsigmoidFwdOp | test_hardsigmoid_manifest_bench[mbv3-se-gate-float16] | 0.0020 | 0.01 | 0.02 | torch 85.7%, torch-compile 68.2% | - |
| 🔴 | HardsigmoidFwdOp | test_hardsigmoid_manifest_bench[mbv3-se-gate-bfloat16] | 0.0022 | 0.01 | 0.01 | torch 79.4%, torch-compile 61.8% | - |
| 🔴 | HardsigmoidFwdOp | test_hardsigmoid_manifest_bench[mbv3-se-gate-deep-float16] | 0.0020 | 0.05 | 0.06 | torch 74.6%, torch-compile 73.1% | - |
| 🔴 | HardsigmoidFwdOp | test_hardsigmoid_manifest_bench[mbv3-se-gate-deep-bfloat16] | 0.0022 | 0.04 | 0.06 | torch 68.4%, torch-compile 67.7% | - |
| 🟡 | HardswishFwdOp | test_hardswish_manifest_bench[mbv3-stage2-float16] | 0.0131 | 2.95 | 2.95 | torch 89.0%, torch-compile 88.2% | - |
| 🟡 | HardswishFwdOp | test_hardswish_manifest_bench[mbv3-stage2-bfloat16] | 0.0133 | 2.90 | 2.90 | torch 87.5%, torch-compile 87.0% | - |
| 🟡 | HardswishFwdOp | test_hardswish_manifest_bench[mbv3-stage3-float16] | 0.0089 | 2.70 | 2.70 | torch 91.0%, torch-compile 90.3% | - |
| 🟡 | HardswishFwdOp | test_hardswish_manifest_bench[mbv3-stage3-bfloat16] | 0.0091 | 2.65 | 2.65 | torch 89.8%, torch-compile 88.7% | - |
| 🔵 | HardtanhFwdOp | test_hardtanh_manifest_bench[bounded-hidden-float16] | 0.0104 | 0.81 | 3.24 | torch 108.6%, torch-compile 100.3% | - |
| 🔵 | HardtanhFwdOp | test_hardtanh_manifest_bench[bounded-hidden-bfloat16] | 0.0104 | 0.81 | 3.23 | torch 102.8%, torch-compile 100.6% | - |
| 🔵 | HardtanhFwdOp | test_hardtanh_manifest_bench[bounded-conv-feat-float16] | 0.0146 | 0.88 | 3.52 | torch 111.0%, torch-compile 100.6% | - |
| 🔵 | HardtanhFwdOp | test_hardtanh_manifest_bench[bounded-conv-feat-bfloat16] | 0.0146 | 0.88 | 3.52 | torch 104.3%, torch-compile 101.3% | - |
| 🔴 | InfNormFwdOp | test_inf_norm_bench[hidden-state-inf-float16] | 0.0301 | 0.56 | 0.56 | flaggems 25.5%, torch 165.0%, torch-compile 35.2% | - |
| 🔴 | InfNormFwdOp | test_inf_norm_bench[hidden-state-inf-bfloat16] | 0.0306 | 0.55 | 0.55 | flaggems 25.8%, torch 163.6%, torch-compile 36.2% | - |
| 🔴 | InfNormFwdOp | test_inf_norm_bench[long-seq-inf-bfloat16] | 0.0177 | 0.24 | 0.24 | flaggems 77.6%, torch 97.6%, torch-compile 28.0% | - |
| 🔴 | InfNormFwdOp | test_inf_norm_bench[3d-multidim-reduce-float16] | 0.0216 | 0.19 | 0.19 | flaggems 58.9%, torch 89.8%, torch-compile 22.7% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[image-affine-float16] | 0.0035 | 1.52 | 1.21 | flaggems 107.4%, torch 600.0%, torch-compile 88.9% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[image-affine-bfloat16] | 0.0034 | 1.53 | 1.23 | flaggems 108.4%, torch 603.8%, torch-compile 87.8% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[wider-channel-affine-float16] | 0.0035 | 1.16 | 0.93 | flaggems 102.8%, torch 596.3%, torch-compile 82.4% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[tail-spatial-affine-float16] | 0.0027 | 0.43 | 0.34 | flaggems 104.8%, torch 411.9%, torch-compile 89.3% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[image-float16] | 0.0034 | 0.94 | 1.25 | flaggems 102.9%, torch 505.8%, torch-compile 87.6% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[image-bfloat16] | 0.0034 | 0.93 | 1.24 | flaggems 101.9%, torch 502.8%, torch-compile 85.9% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[wider-channel-float16] | 0.0033 | 0.72 | 0.96 | flaggems 99.0%, torch 486.5%, torch-compile 82.7% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[tail-spatial-float16] | 0.0025 | 0.27 | 0.36 | flaggems 103.8%, torch 326.6%, torch-compile 91.1% | - |
| 🔴 | IsfiniteFwdOp | test_isfinite_bench[elementwise-16M-float16] | 0.0204 | 0.82 | 2.46 | torch 309.2%, torch-compile 73.6% | - |
| 🔴 | IsfiniteFwdOp | test_isfinite_bench[elementwise-16M-bfloat16] | 0.0205 | 0.82 | 2.46 | torch 309.5%, torch-compile 73.4% | - |
| 🟡 | IsfiniteFwdOp | test_isfinite_bench[elementwise-16M-float32] | 0.0266 | 0.63 | 3.15 | torch 361.7%, torch-compile 87.6% | - |
| 🔴 | IsfiniteFwdOp | test_isfinite_bench[elementwise-256M-float16] | 0.2731 | 0.98 | 2.95 | torch 334.1%, torch-compile 72.1% | - |
| 🔴 | IsfiniteFwdOp | test_isfinite_bench[elementwise-256M-bfloat16] | 0.2731 | 0.98 | 2.95 | torch 335.2%, torch-compile 72.0% | - |
| 🔴 | IsinfFwdOp | test_isinf_bench[elementwise-16M-float16] | 0.0206 | 0.81 | 2.44 | torch 152.0%, torch-compile 73.5% | - |
| 🔴 | IsinfFwdOp | test_isinf_bench[elementwise-16M-bfloat16] | 0.0205 | 0.82 | 2.45 | torch 153.0%, torch-compile 74.0% | - |
| 🟡 | IsinfFwdOp | test_isinf_bench[elementwise-16M-float32] | 0.0267 | 0.63 | 3.14 | torch 214.5%, torch-compile 87.5% | - |
| 🔴 | IsinfFwdOp | test_isinf_bench[elementwise-256M-float16] | 0.2763 | 0.97 | 2.91 | torch 162.8%, torch-compile 72.0% | - |
| 🔴 | IsinfFwdOp | test_isinf_bench[elementwise-256M-bfloat16] | 0.2753 | 0.98 | 2.93 | torch 163.8%, torch-compile 72.7% | - |
| 🔴 | IsnanFwdOp | test_isnan_bench[elementwise-16M-float16] | 0.0205 | 0.82 | 2.46 | torch 75.0%, torch-compile 73.4% | - |
| 🔴 | IsnanFwdOp | test_isnan_bench[elementwise-16M-bfloat16] | 0.0205 | 0.82 | 2.46 | torch 75.6%, torch-compile 73.9% | - |
| 🟡 | IsnanFwdOp | test_isnan_bench[elementwise-16M-float32] | 0.0266 | 0.63 | 3.15 | torch 88.1%, torch-compile 87.9% | - |
| 🔴 | IsnanFwdOp | test_isnan_bench[elementwise-256M-float16] | 0.2732 | 0.98 | 2.95 | torch 73.8%, torch-compile 72.2% | - |
| 🔴 | IsnanFwdOp | test_isnan_bench[elementwise-256M-bfloat16] | 0.2730 | 0.98 | 2.95 | torch 74.7%, torch-compile 72.8% | - |
| 🔵 | L1NormFwdOp | test_l1_norm_bench[hidden-state-l1-float16] | 0.0076 | 2.19 | 2.19 | flaggems 196.2%, torch 646.0%, torch-compile 109.2% | - |
| 🔵 | L1NormFwdOp | test_l1_norm_bench[hidden-state-l1-bfloat16] | 0.0077 | 2.18 | 2.18 | flaggems 199.6%, torch 644.0%, torch-compile 109.1% | - |
| 🟡 | L1NormFwdOp | test_l1_norm_bench[long-seq-l1-bfloat16] | 0.0051 | 0.82 | 0.82 | flaggems 718.4%, torch 329.0%, torch-compile 86.6% | - |
| 🔴 | L1NormFwdOp | test_l1_norm_bench[3d-multidim-reduce-float16] | 0.0113 | 0.37 | 0.37 | flaggems 217.2%, torch 170.8%, torch-compile 41.0% | - |
| 🔵 | L2NormFwdOp | test_l2_norm_bench[hidden-state-l2-float16] | 0.0077 | 2.17 | 2.17 | flaggems 101.6%, torch 636.8%, torch-compile 112.0% | - |
| 🔵 | L2NormFwdOp | test_l2_norm_bench[hidden-state-l2-bfloat16] | 0.0078 | 2.16 | 2.16 | flaggems 101.0%, torch 638.7%, torch-compile 113.2% | - |
| 🟡 | L2NormFwdOp | test_l2_norm_bench[long-seq-l2-bfloat16] | 0.0052 | 0.81 | 0.81 | flaggems 261.1%, torch 326.5%, torch-compile 87.0% | - |
| 🔴 | L2NormFwdOp | test_l2_norm_bench[3d-multidim-reduce-float16] | 0.0114 | 0.37 | 0.37 | flaggems 118.2%, torch 168.1%, torch-compile 41.4% | - |
| 🟡 | LayerNormFwdOp | test_layer_norm_bench[llama-8b-prefill-float16] | 0.0137 | 3.06 | 2.45 | flaggems 95.8%, flashinfer 155.6%, torch 154.7%, torch-compile 177.8% | - |
| 🟡 | LayerNormFwdOp | test_layer_norm_bench[llama-8b-prefill-bfloat16] | 0.0149 | 2.81 | 2.25 | flaggems 92.5%, flashinfer 142.9%, torch 142.5%, torch-compile 164.6% | - |
| 🔵 | LayerNormFwdOp | test_layer_norm_bench[llama-8b-decode-bfloat16] | 0.0027 | 0.01 | 0.01 | flaggems 103.5%, flashinfer 112.9%, torch 409.4%, torch-compile 115.3% | - |
| 🟡 | LayerNormFwdOp | test_layer_norm_bench[llama-70b-prefill-float16] | 0.0260 | 3.23 | 2.58 | flaggems 99.0%, flashinfer 179.0%, torch 154.3%, torch-compile 117.5% | - |
| 🔵 | LayerNormFwdOp | test_layer_norm_bench[llama-70b-prefill-bfloat16] | 0.0265 | 3.17 | 2.54 | flaggems 104.6%, flashinfer 176.5%, torch 153.1%, torch-compile 125.6% | - |
| 🔵 | LayerNormFwdOp | test_layer_norm_bench[llama-70b-decode-bfloat16] | 0.0035 | 0.01 | 0.02 | flaggems 122.2%, flashinfer 119.4%, torch 579.6%, torch-compile 125.9% | - |
| 🟡 | LayerNormFwdOp | test_layer_norm_bench[llama-405b-prefill-float16] | 0.0501 | 3.35 | 2.68 | flaggems 96.3%, flashinfer 156.0%, torch 146.7%, torch-compile 93.1% | - |
| 🟡 | LayerNormFwdOp | test_layer_norm_bench[llama-405b-prefill-bfloat16] | 0.0508 | 3.30 | 2.64 | flaggems 99.3%, flashinfer 154.2%, torch 146.3%, torch-compile 99.6% | - |
| 🔵 | LayerNormFwdOp | test_layer_norm_bench[llama-405b-decode-bfloat16] | 0.0043 | 0.02 | 0.03 | flaggems 141.5%, flashinfer 140.0%, torch 876.3%, torch-compile 127.4% | - |
| 🟡 | LeFwdOp | test_comparison_bench[le-1024x4096-float16-le] | 0.0080 | 0.52 | 2.61 | torch 96.4%, torch-compile 96.0% | - |
| 🟡 | LeFwdOp | test_le_manifest_bench[hidden-state-prefill-float16] | 0.0140 | 0.60 | 2.99 | torch 92.0%, torch-compile 92.2% | - |
| 🟡 | LeFwdOp | test_le_manifest_bench[hidden-state-prefill-bfloat16] | 0.0140 | 0.60 | 2.99 | torch 93.8%, torch-compile 93.6% | - |
| 🔵 | LeFwdOp | test_le_manifest_bench[hidden-state-prefill-float32] | 0.0223 | 0.38 | 3.38 | torch 100.9%, torch-compile 100.6% | - |
| 🔴 | LeFwdOp | test_le_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.81 | 2.42 | torch 311.2%, torch-compile 74.7% | - |
| 🔴 | LeFwdOp | test_le_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.81 | 2.42 | torch 316.9%, torch-compile 74.7% | - |
| 🟡 | LeFwdOp | test_le_manifest_bench[cnn-feat-broadcast-float32] | 0.0214 | 0.60 | 3.00 | torch 230.9%, torch-compile 86.6% | - |
| 🔵 | LeakyReluFwdOp | test_leaky_relu_manifest_bench[gan-feat-float16] | 0.0184 | 1.82 | 3.64 | torch 100.2%, torch-compile 100.0% | - |
| 🔵 | LeakyReluFwdOp | test_leaky_relu_manifest_bench[gan-feat-bfloat16] | 0.0184 | 1.82 | 3.65 | torch 100.4%, torch-compile 100.2% | - |
| 🔵 | LeakyReluFwdOp | test_leaky_relu_manifest_bench[gan-feat-deep-float16] | 0.0104 | 1.62 | 3.24 | torch 100.3%, torch-compile 100.0% | - |
| 🔵 | LeakyReluFwdOp | test_leaky_relu_manifest_bench[gan-feat-deep-bfloat16] | 0.0104 | 1.62 | 3.24 | torch 100.3%, torch-compile 100.0% | - |
| 🔵 | LerpFwdOp | test_binary_arith_bench[lerp-1024x4096-float16-float16-LerpFwdOp-<lambda>-normal] | 0.0082 | 0.51 | 3.07 | torch 100.4%, torch-compile 100.0% | - |
| 🟡 | LerpFwdOp | test_binary_arith_bench[lerp-1024x10240-float16-float16-LerpFwdOp-<lambda>-normal] | 0.0177 | 0.59 | 3.56 | torch 100.4%, torch-compile 99.8% | - |
| 🟡 | LerpFwdOp | test_lerp_manifest_bench[hidden-state-prefill-float16] | 0.0148 | 1.70 | 3.39 | torch 100.1%, torch-compile 99.9% | - |
| 🔵 | LerpFwdOp | test_lerp_manifest_bench[hidden-state-prefill-bfloat16] | 0.0146 | 1.72 | 3.44 | torch 100.2%, torch-compile 100.0% | - |
| 🟡 | LerpFwdOp | test_lerp_manifest_bench[hidden-state-prefill-float32] | 0.0264 | 0.95 | 3.81 | torch 99.1%, torch-compile 105.6% | - |
| 🟡 | LerpFwdOp | test_lerp_manifest_bench[cnn-feat-broadcast-float16] | 0.0165 | 2.33 | 3.11 | torch 288.0%, torch-compile 87.2% | - |
| 🟡 | LerpFwdOp | test_lerp_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0166 | 2.32 | 3.10 | torch 291.1%, torch-compile 86.5% | - |
| 🟡 | LerpFwdOp | test_lerp_manifest_bench[cnn-feat-broadcast-float32] | 0.0267 | 1.44 | 3.85 | torch 190.5%, torch-compile 99.4% | - |
| 🟡 | LerpTensorFwdOp | test_lerp_tensor_manifest_bench[elementwise-16M-float16] | 0.0351 | 1.44 | 3.83 | torch 99.4%, torch-compile 99.0% | - |
| 🟡 | LerpTensorFwdOp | test_lerp_tensor_manifest_bench[elementwise-16M-bfloat16] | 0.0350 | 1.44 | 3.83 | torch 99.4%, torch-compile 99.3% | - |
| 🟡 | LerpTensorFwdOp | test_lerp_tensor_manifest_bench[elementwise-16M-float32] | 0.0656 | 0.77 | 4.09 | torch 99.4%, torch-compile 99.5% | - |
| 🔵 | LerpTensorFwdOp | test_lerp_tensor_manifest_bench[elementwise-256M-float16] | 0.4858 | 1.66 | 4.42 | torch 100.0%, torch-compile 100.0% | - |
| 🔵 | LerpTensorFwdOp | test_lerp_tensor_manifest_bench[elementwise-256M-bfloat16] | 0.4860 | 1.66 | 4.42 | torch 100.0%, torch-compile 100.0% | - |
| 🟡 | Log1pFwdOp | test_log1p_bench[elementwise-16M-float16] | 0.0284 | 1.18 | 2.37 | torch 92.4%, torch-compile 89.6% | - |
| 🟡 | Log1pFwdOp | test_log1p_bench[elementwise-16M-bfloat16] | 0.0293 | 1.15 | 2.29 | torch 91.8%, torch-compile 89.8% | - |
| 🟡 | Log1pFwdOp | test_log1p_bench[elementwise-16M-float32] | 0.0364 | 0.92 | 3.69 | torch 93.4%, torch-compile 93.4% | - |
| 🟡 | Log1pFwdOp | test_log1p_bench[elementwise-256M-float16] | 0.4151 | 1.29 | 2.59 | torch 91.5%, torch-compile 88.9% | - |
| 🟡 | Log1pFwdOp | test_log1p_bench[elementwise-256M-bfloat16] | 0.4329 | 1.24 | 2.48 | torch 89.6%, torch-compile 88.3% | - |
| 🟡 | LogFwdOp | test_log_bench[elementwise-16M-float16] | 0.0276 | 0.61 | 2.43 | torch 98.3%, torch-compile 99.0% | - |
| 🟡 | LogFwdOp | test_log_bench[elementwise-16M-bfloat16] | 0.0289 | 0.58 | 2.32 | torch 97.1%, torch-compile 96.1% | - |
| 🟡 | LogFwdOp | test_log_bench[elementwise-16M-float32] | 0.0360 | 0.47 | 3.73 | torch 95.2%, torch-compile 94.9% | - |
| 🟡 | LogFwdOp | test_log_bench[elementwise-256M-float16] | 0.4072 | 0.66 | 2.64 | torch 97.6%, torch-compile 98.7% | - |
| 🟡 | LogFwdOp | test_log_bench[elementwise-256M-bfloat16] | 0.4287 | 0.63 | 2.50 | torch 96.2%, torch-compile 95.6% | - |
| 🟢 | LogSoftmaxFwdOp | test_log_softmax_bench[attn-weights-4k-float16] | 0.0087 | 2.40 | 1.92 | flaggems 228.6%, torch 196.7%, torch-compile 176.9% | - |
| 🟢 | LogSoftmaxFwdOp | test_log_softmax_bench[attn-weights-4k-bfloat16] | 0.0087 | 2.40 | 1.92 | flaggems 234.1%, torch 196.3%, torch-compile 176.6% | - |
| 🔵 | LogSoftmaxFwdOp | test_log_softmax_bench[attn-weights-4k-float32] | 0.0120 | 1.74 | 2.79 | flaggems 170.5%, torch 153.5%, torch-compile 130.9% | - |
| 🔵 | LogSoftmaxFwdOp | test_log_softmax_bench[attn-weights-32k-bfloat16] | 0.0585 | 2.87 | 2.29 | flaggems 427.6%, torch 105.2%, torch-compile 122.3% | - |
| 🔴 | LogSoftmaxFwdOp | test_log_softmax_bench[lm-head-logits-float16] | 0.0287 | 0.07 | 0.06 | flaggems 1465.0%, torch 77.0%, torch-compile 33.8% | - |
| 🔴 | LogSoftmaxFwdOp | test_log_softmax_bench[lm-head-logits-bfloat16] | 0.0269 | 0.08 | 0.06 | flaggems 1565.0%, torch 84.9%, torch-compile 35.9% | - |
| 🔴 | LogSoftmaxFwdOp | test_log_softmax_bench[lm-head-logits-float32] | 0.0366 | 0.06 | 0.09 | flaggems 1103.0%, torch 96.1%, torch-compile 27.0% | - |
| 🔵 | LogSumExpFwdOp | test_logsumexp_bench[attn-weights-4k-float16] | 0.0074 | 2.26 | 1.13 | torch 661.6%, torch-compile 135.8% | - |
| 🔵 | LogSumExpFwdOp | test_logsumexp_bench[attn-weights-4k-bfloat16] | 0.0075 | 2.25 | 1.13 | torch 662.2%, torch-compile 134.3% | - |
| 🔵 | LogSumExpFwdOp | test_logsumexp_bench[attn-weights-32k-bfloat16] | 0.0327 | 4.11 | 2.06 | torch 605.5%, torch-compile 127.2% | - |
| 🔴 | LogSumExpFwdOp | test_logsumexp_bench[lm-head-logits-float16] | 0.0141 | 0.12 | 0.06 | torch 329.9%, torch-compile 76.9% | - |
| 🔴 | LogSumExpFwdOp | test_logsumexp_bench[lm-head-logits-bfloat16] | 0.0164 | 0.10 | 0.05 | torch 286.5%, torch-compile 64.0% | - |
| 🔴 | LogSumExpFwdOp | test_logsumexp_bench[3d-multidim-reduce-float16] | 0.0126 | 0.67 | 0.33 | torch 328.8%, torch-compile 79.1% | - |
| 🔴 | LogicalAndFwdOp | test_logical_bench[logical_and-1024x4096-float16-LogicalAndFwdOp-logical_and] | 0.0079 | 0.53 | 2.64 | torch 74.2%, torch-compile 116.5% | - |
| 🔴 | LogicalAndFwdOp | test_logical_bench[logical_and-1024x10240-float16-LogicalAndFwdOp-logical_and] | 0.0171 | 0.61 | 3.06 | torch 71.6%, torch-compile 63.5% | - |
| 🔵 | LogicalAndFwdOp | test_logical_and_manifest_bench[hidden-state-prefill-bool] | 0.0083 | 3.05 | 3.05 | torch 122.5%, torch-compile 107.4% | - |
| 🟡 | LogicalAndFwdOp | test_logical_and_manifest_bench[hidden-state-prefill-float16] | 0.0140 | 1.80 | 3.01 | torch 95.9%, torch-compile 95.6% | - |
| 🟡 | LogicalAndFwdOp | test_logical_and_manifest_bench[hidden-state-prefill-bfloat16] | 0.0141 | 1.78 | 2.97 | torch 92.2%, torch-compile 92.2% | - |
| 🟡 | LogicalAndFwdOp | test_logical_and_manifest_bench[hidden-state-prefill-float32] | 0.0226 | 1.11 | 3.34 | torch 99.3%, torch-compile 99.2% | - |
| 🔵 | LogicalAndFwdOp | test_logical_and_manifest_bench[cnn-feat-broadcast-bool] | 0.0081 | 4.78 | 3.19 | torch 560.3%, torch-compile 123.6% | - |
| 🔴 | LogicalAndFwdOp | test_logical_and_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 2.42 | 2.42 | torch 294.2%, torch-compile 76.3% | - |
| 🔴 | LogicalAndFwdOp | test_logical_and_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 2.42 | 2.42 | torch 301.4%, torch-compile 75.5% | - |
| 🟡 | LogicalAndFwdOp | test_logical_and_manifest_bench[cnn-feat-broadcast-float32] | 0.0213 | 1.81 | 3.02 | torch 218.3%, torch-compile 85.7% | - |
| 🔵 | LogicalNotFwdOp | test_logical_not_bench[elementwise-16M-bool] | 0.0101 | 1.66 | 3.33 | torch 128.9%, torch-compile 119.7% | - |
| 🔴 | LogicalNotFwdOp | test_logical_not_bench[elementwise-16M-float16] | 0.0188 | 0.89 | 2.68 | torch 81.1%, torch-compile 79.9% | - |
| 🟡 | LogicalNotFwdOp | test_logical_not_bench[elementwise-16M-float32] | 0.0261 | 0.64 | 3.21 | torch 89.7%, torch-compile 89.6% | - |
| 🔵 | LogicalNotFwdOp | test_logical_not_bench[elementwise-256M-bool] | 0.1268 | 2.12 | 4.24 | torch 143.2%, torch-compile 130.0% | - |
| 🔴 | LogicalOrFwdOp | test_logical_bench[logical_or-1024x4096-float16-LogicalOrFwdOp-logical_or] | 0.0080 | 0.53 | 2.63 | torch 71.1%, torch-compile 115.7% | - |
| 🔴 | LogicalOrFwdOp | test_logical_bench[logical_or-1024x10240-float16-LogicalOrFwdOp-logical_or] | 0.0171 | 0.61 | 3.06 | torch 61.9%, torch-compile 59.6% | - |
| 🔵 | LogicalOrFwdOp | test_logical_or_manifest_bench[hidden-state-prefill-bool] | 0.0082 | 3.06 | 3.06 | torch 110.1%, torch-compile 107.8% | - |
| 🟡 | LogicalOrFwdOp | test_logical_or_manifest_bench[hidden-state-prefill-float16] | 0.0141 | 1.78 | 2.97 | torch 94.0%, torch-compile 93.8% | - |
| 🟡 | LogicalOrFwdOp | test_logical_or_manifest_bench[hidden-state-prefill-bfloat16] | 0.0140 | 1.80 | 2.99 | torch 92.9%, torch-compile 92.7% | - |
| 🟡 | LogicalOrFwdOp | test_logical_or_manifest_bench[hidden-state-prefill-float32] | 0.0224 | 1.12 | 3.37 | torch 100.1%, torch-compile 99.9% | - |
| 🔵 | LogicalOrFwdOp | test_logical_or_manifest_bench[cnn-feat-broadcast-bool] | 0.0081 | 4.76 | 3.17 | torch 546.7%, torch-compile 126.5% | - |
| 🔴 | LogicalOrFwdOp | test_logical_or_manifest_bench[cnn-feat-broadcast-float16] | 0.0164 | 2.35 | 2.35 | torch 290.8%, torch-compile 73.4% | - |
| 🔴 | LogicalOrFwdOp | test_logical_or_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0164 | 2.36 | 2.36 | torch 298.4%, torch-compile 74.2% | - |
| 🟡 | LogicalOrFwdOp | test_logical_or_manifest_bench[cnn-feat-broadcast-float32] | 0.0214 | 1.80 | 3.00 | torch 216.6%, torch-compile 86.6% | - |
| 🟡 | LtFwdOp | test_comparison_bench[lt-1024x4096-float16-lt] | 0.0080 | 0.52 | 2.62 | torch 96.8%, torch-compile 96.8% | - |
| 🟡 | LtFwdOp | test_lt_manifest_bench[hidden-state-prefill-float16] | 0.0141 | 0.59 | 2.97 | torch 92.8%, torch-compile 92.8% | - |
| 🟡 | LtFwdOp | test_lt_manifest_bench[hidden-state-prefill-bfloat16] | 0.0142 | 0.59 | 2.96 | torch 93.8%, torch-compile 93.4% | - |
| 🔵 | LtFwdOp | test_lt_manifest_bench[hidden-state-prefill-float32] | 0.0223 | 0.38 | 3.38 | torch 101.0%, torch-compile 100.7% | - |
| 🔴 | LtFwdOp | test_lt_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.81 | 2.42 | torch 312.2%, torch-compile 74.3% | - |
| 🔴 | LtFwdOp | test_lt_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.81 | 2.42 | torch 316.9%, torch-compile 76.5% | - |
| 🟡 | LtFwdOp | test_lt_manifest_bench[cnn-feat-broadcast-float32] | 0.0214 | 0.60 | 3.00 | torch 230.2%, torch-compile 86.1% | - |
| 🟡 | MHCPostFwdOp | test_mhc_post_bench[post-small-bfloat16] | 0.0013 | 0.01 | 0.02 | torch-ref 804.9%, torch-compile 97.6% | - |
| 🔵 | MHCPostFwdOp | test_mhc_post_bench[post-medium-bfloat16] | 0.0014 | 0.02 | 0.05 | torch-ref 779.5%, torch-compile 109.2% | - |
| 🔵 | MHCPostFwdOp | test_mhc_post_bench[post-large-bfloat16] | 0.0016 | 0.05 | 0.12 | torch-ref 718.4%, torch-compile 108.2% | - |
| 🔴 | MHCPreFwdOp | test_mhc_pre_bench[pre-small-bfloat16] | 0.0395 | 0.01 | 0.01 | torch-ref 148.7%, torch-compile 50.0% | - |
| 🔴 | MHCPreFwdOp | test_mhc_pre_bench[pre-medium-bfloat16] | 0.0543 | 0.02 | 0.01 | torch-ref 142.5%, torch-compile 57.7% | - |
| 🔴 | MHCPreFwdOp | test_mhc_pre_bench[pre-large-bfloat16] | 0.0715 | 0.03 | 0.02 | torch-ref 163.3%, torch-compile 79.3% | - |
| 🟡 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-2p7b-b1-s2k-bfloat16] | 0.1102 | 73.89 | 0.99 | mamba 98.7%, torch-ref 1954.7%, torch-compile 623.8% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-1p3b-b1-s8k-float16] | 0.2907 | 89.81 | 1.20 | mamba 107.4%, torch-ref 2376.7%, torch-compile 695.0% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-2p7b-b1-s2k-dt-bias-bfloat16] | 0.1092 | 74.54 | 0.99 | mamba 100.0%, torch-ref 1975.1%, torch-compile 630.3% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-1p3b-b1-s8k-dt-bias-float16] | 0.2899 | 90.08 | 1.20 | mamba 107.7%, torch-ref 2385.6%, torch-compile 695.3% | - |
| 🟡 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-2p7b-b1-s2k-init-states-bfloat16] | 0.1106 | 73.60 | 1.01 | mamba 99.9%, torch-ref 1947.0%, torch-compile 614.7% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-1p3b-b1-s8k-init-states-float16] | 0.2912 | 89.66 | 1.21 | mamba 107.8%, torch-ref 2369.9%, torch-compile 692.5% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-2p7b-b1-s2k-dt-bias-init-states-bfloat16] | 0.1098 | 74.19 | 1.01 | mamba 100.4%, torch-ref 1963.3%, torch-compile 619.5% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-1p3b-b1-s8k-dt-bias-init-states-float16] | 0.2899 | 90.08 | 1.21 | mamba 107.7%, torch-ref 2381.8%, torch-compile 694.5% | - |
| 🟡 | MaskedFillFwdOp | test_masked_fill_tensor_manifest_bench[elementwise-16M-float16] | 0.0227 | 0.74 | 3.69 | torch 85.4%, torch-compile 99.3% | - |
| 🟡 | MaskedFillFwdOp | test_masked_fill_tensor_manifest_bench[elementwise-16M-bfloat16] | 0.0226 | 0.74 | 3.71 | torch 85.8%, torch-compile 99.7% | - |
| 🟡 | MaskedFillFwdOp | test_masked_fill_tensor_manifest_bench[elementwise-16M-float32] | 0.0380 | 0.44 | 3.98 | torch 95.4%, torch-compile 98.9% | - |
| 🔵 | MaskedFillFwdOp | test_masked_fill_tensor_manifest_bench[elementwise-256M-float16] | 0.3092 | 0.87 | 4.34 | torch 100.2%, torch-compile 100.2% | - |
| 🟡 | MaskedFillFwdOp | test_masked_fill_tensor_manifest_bench[elementwise-256M-bfloat16] | 0.3104 | 0.86 | 4.32 | torch 99.7%, torch-compile 99.9% | - |
| 🟡 | MaskedFillScalarFwdOp | test_masked_fill_scalar_manifest_bench[elementwise-16M-float16] | 0.0227 | 0.74 | 3.69 | torch 84.9%, torch-compile 99.3% | - |
| 🟡 | MaskedFillScalarFwdOp | test_masked_fill_scalar_manifest_bench[elementwise-16M-bfloat16] | 0.0225 | 0.75 | 3.73 | torch 86.4%, torch-compile 99.8% | - |
| 🟡 | MaskedFillScalarFwdOp | test_masked_fill_scalar_manifest_bench[elementwise-16M-float32] | 0.0378 | 0.44 | 3.99 | torch 95.9%, torch-compile 98.6% | - |
| 🟡 | MaskedFillScalarFwdOp | test_masked_fill_scalar_manifest_bench[elementwise-256M-float16] | 0.3099 | 0.87 | 4.33 | torch 99.8%, torch-compile 99.9% | - |
| 🟡 | MaskedFillScalarFwdOp | test_masked_fill_scalar_manifest_bench[elementwise-256M-bfloat16] | 0.3105 | 0.86 | 4.32 | torch 99.8%, torch-compile 99.9% | - |
| 🔵 | MaxPool1dFwdOp | test_max_pool1d_bench[sincnet-speaker-local-float16] | 0.0114 | 0.92 | 2.45 | torch-ref 443.5%, torch-compile 100.3% | - |
| 🔴 | MaxPool1dFwdOp | test_max_pool1d_bench[textcnn-global-float16] | 0.0134 | 0.16 | 0.31 | torch-ref 196.7%, torch-compile 27.6% | - |
| 🟡 | MaxPool1dFwdOp | test_max_pool1d_bench[ecg-cnn-dilated-bfloat16] | 0.0095 | 1.10 | 1.32 | torch-ref 371.1%, torch-compile 82.2% | - |
| 🔴 | MaxPool1dIndicesFwdOp | test_max_pool1d_indices_bench[sincnet-speaker-local-float16] | 0.0218 | 0.48 | 2.57 | torch-ref 231.9%, torch-compile 73.5% | - |
| 🔴 | MaxPool1dIndicesFwdOp | test_max_pool1d_indices_bench[textcnn-global-float16] | 0.0193 | 0.11 | 0.23 | torch-ref 137.0%, torch-compile 39.1% | - |
| 🔴 | MaxPool1dIndicesFwdOp | test_max_pool1d_indices_bench[ecg-cnn-dilated-bfloat16] | 0.0224 | 0.47 | 1.31 | torch-ref 158.4%, torch-compile 59.9% | - |
| 🔴 | MaxPool2dFwdOp | test_max_pool2d_bench[resnet-stem-float16] | 0.0469 | 1.23 | 1.37 | flaggems 167.4%, torch-ref 296.6%, torch-compile 73.1% | - |
| 🔴 | MaxPool2dFwdOp | test_max_pool2d_bench[resnet-stem-bfloat16] | 0.0471 | 1.23 | 1.36 | flaggems 166.5%, torch-ref 296.5%, torch-compile 72.6% | - |
| 🟡 | MaxPool2dFwdOp | test_max_pool2d_bench[resnet-stem-float32] | 0.0527 | 1.10 | 2.44 | flaggems 153.8%, torch-ref 255.5%, torch-compile 94.2% | - |
| 🔵 | MaxPool2dFwdOp | test_max_pool2d_bench[vgg-block-float16] | 0.0072 | 0.89 | 2.23 | flaggems 205.3%, torch-ref 385.3%, torch-compile 100.7% | - |
| 🔵 | MaxPool2dFwdOp | test_max_pool2d_bench[vgg-block-bfloat16] | 0.0072 | 0.89 | 2.23 | flaggems 205.3%, torch-ref 386.7%, torch-compile 100.9% | - |
| 🟡 | MaxPool2dFwdOp | test_max_pool2d_bench[vgg-block-float32] | 0.0111 | 0.58 | 2.89 | flaggems 150.9%, torch-ref 249.9%, torch-compile 93.4% | - |
| 🔵 | MaxPool2dFwdOp | test_max_pool2d_bench[alexnet-ceil-float16] | 0.0088 | 1.53 | 1.75 | flaggems 256.9%, torch-ref 396.0%, torch-compile 125.2% | - |
| 🔵 | MaxPool2dFwdOp | test_max_pool2d_bench[alexnet-ceil-bfloat16] | 0.0088 | 1.53 | 1.75 | flaggems 258.8%, torch-ref 396.7%, torch-compile 125.2% | - |
| 🔵 | MaxPool2dFwdOp | test_max_pool2d_bench[alexnet-ceil-float32] | 0.0126 | 1.06 | 2.43 | flaggems 180.8%, torch-ref 270.1%, torch-compile 121.8% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[resnet-stem-float16] | 0.1123 | 0.51 | 1.03 | flaggems 70.0%, torch-ref 124.1%, torch-compile 61.6% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[resnet-stem-bfloat16] | 0.1122 | 0.52 | 1.03 | flaggems 69.8%, torch-ref 124.3%, torch-compile 62.2% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[resnet-stem-float32] | 0.1074 | 0.54 | 1.67 | flaggems 75.5%, torch-ref 125.3%, torch-compile 66.6% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[vgg-block-float16] | 0.0196 | 0.33 | 1.47 | flaggems 75.2%, torch-ref 141.2%, torch-compile 54.1% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[vgg-block-bfloat16] | 0.0195 | 0.33 | 1.49 | flaggems 76.1%, torch-ref 143.3%, torch-compile 54.6% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[vgg-block-float32] | 0.0195 | 0.33 | 2.30 | flaggems 85.9%, torch-ref 142.0%, torch-compile 64.8% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[alexnet-ceil-float16] | 0.0237 | 0.57 | 1.15 | flaggems 95.0%, torch-ref 146.4%, torch-compile 74.5% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[alexnet-ceil-bfloat16] | 0.0237 | 0.57 | 1.15 | flaggems 96.0%, torch-ref 146.7%, torch-compile 73.4% | - |
| 🟡 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[alexnet-ceil-float32] | 0.0236 | 0.57 | 1.81 | flaggems 96.6%, torch-ref 144.4%, torch-compile 81.7% | - |
| 🔵 | MaxPool3dFwdOp | test_max_pool3d_bench[c3d-pool1-float16] | 0.0761 | 1.35 | 3.37 | cudnn 395.2%, torch-ref 680.5%, torch-compile 101.3% | - |
| 🔵 | MaxPool3dFwdOp | test_max_pool3d_bench[c3d-pool2-float16] | 0.0236 | 1.09 | 2.45 | cudnn 258.8%, torch-ref 398.9%, torch-compile 104.8% | - |
| 🟢 | MaxPool3dFwdOp | test_max_pool3d_bench[medicalnet-stem-bfloat16] | 0.1111 | 1.72 | 1.05 | cudnn 237.5%, torch-ref 301.5%, torch-compile 833.7% | - |
| 🔴 | MaxPool3dIndicesFwdOp | test_max_pool3d_indices_bench[c3d-pool1-float16] | 0.3045 | 0.34 | 1.52 | torch-ref 170.2%, torch-compile 42.5% | - |
| 🔴 | MaxPool3dIndicesFwdOp | test_max_pool3d_indices_bench[c3d-pool2-float16] | 0.0589 | 0.44 | 1.42 | torch-ref 159.6%, torch-compile 55.5% | - |
| 🔵 | MaxPool3dIndicesFwdOp | test_max_pool3d_indices_bench[medicalnet-stem-bfloat16] | 0.3315 | 0.58 | 0.52 | torch-ref 101.0%, torch-compile 614.2% | - |
| 🟡 | MaximumFwdOp | test_binary_arith_bench[maximum-1024x4096-float16-float16-MaximumFwdOp-maximum-normal] | 0.0086 | 0.49 | 2.93 | torch 100.7%, torch-compile 97.8% | - |
| 🟡 | MaximumFwdOp | test_binary_arith_bench[maximum-1024x10240-float16-float16-MaximumFwdOp-maximum-normal] | 0.0181 | 0.58 | 3.48 | torch 100.5%, torch-compile 98.8% | - |
| 🟡 | MaximumFwdOp | test_binary_arith_bench[maximum-1024x11008-float16-float16-MaximumFwdOp-maximum-normal] | 0.0189 | 0.60 | 3.58 | torch 100.5%, torch-compile 98.7% | - |
| 🟡 | MaximumFwdOp | test_maximum_manifest_bench[hidden-state-prefill-float16] | 0.0147 | 0.57 | 3.42 | torch 100.4%, torch-compile 98.5% | - |
| 🟡 | MaximumFwdOp | test_maximum_manifest_bench[hidden-state-prefill-bfloat16] | 0.0150 | 0.56 | 3.36 | torch 100.3%, torch-compile 98.2% | - |
| 🔵 | MaximumFwdOp | test_maximum_manifest_bench[hidden-state-prefill-float32] | 0.0263 | 0.32 | 3.82 | torch 100.6%, torch-compile 106.4% | - |
| 🔴 | MaximumFwdOp | test_maximum_manifest_bench[cnn-feat-broadcast-float16] | 0.0395 | 0.33 | 1.30 | torch 127.6%, torch-compile 36.5% | - |
| 🔴 | MaximumFwdOp | test_maximum_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0396 | 0.32 | 1.30 | torch 129.6%, torch-compile 35.9% | - |
| 🟡 | MaximumFwdOp | test_maximum_manifest_bench[cnn-feat-broadcast-float32] | 0.0299 | 0.43 | 3.43 | torch 176.8%, torch-compile 88.2% | - |
| 🟡 | MeanFwdOp | test_mean_bench[hidden-state-reduce-float16] | 0.0085 | 0.98 | 1.96 | flaggems 103.8%, torch 579.0%, torch-compile 97.8% | - |
| 🟡 | MeanFwdOp | test_mean_bench[hidden-state-reduce-bfloat16] | 0.0086 | 0.97 | 1.94 | flaggems 103.3%, torch 576.5%, torch-compile 97.4% | - |
| 🔴 | MeanFwdOp | test_mean_bench[long-seq-reduce-bfloat16] | 0.0052 | 0.40 | 0.80 | flaggems 73.0%, torch 323.3%, torch-compile 89.6% | - |
| 🔴 | MeanFwdOp | test_mean_bench[3d-multidim-reduce-float16] | 0.0115 | 0.18 | 0.37 | flaggems 117.5%, torch 167.4%, torch-compile 41.8% | - |
| 🟢 | MeanPoolingForwardOp | test_mean_pooling_bench[dense-mainstream] | 0.1350 | 0.50 | 1.01 | torch-ref 452.4%, torch-compile 314.3% | - |
| 🟢 | MeanPoolingForwardOp | test_mean_pooling_bench[dense-batched] | 0.0704 | 0.48 | 0.97 | torch-ref 359.2%, torch-compile 205.7% | - |
| 🟢 | MeanPoolingForwardOp | test_mean_pooling_bench[varlen-long] | 0.1385 | 0.48 | 0.98 | torch-ref 443.9%, torch-compile 440.8% | - |
| 🟢 | MeanPoolingForwardOp | test_mean_pooling_bench[varlen-tail] | 0.0218 | 0.41 | 0.78 | torch-ref 982.2%, torch-compile 960.8% | - |
| 🟡 | MinimumFwdOp | test_binary_arith_bench[minimum-1024x4096-float16-float16-MinimumFwdOp-minimum-normal] | 0.0086 | 0.49 | 2.91 | torch 101.1%, torch-compile 96.7% | - |
| 🟡 | MinimumFwdOp | test_binary_arith_bench[minimum-1024x10240-float16-float16-MinimumFwdOp-minimum-normal] | 0.0181 | 0.58 | 3.47 | torch 100.5%, torch-compile 98.6% | - |
| 🟡 | MinimumFwdOp | test_binary_arith_bench[minimum-1024x11008-float16-float16-MinimumFwdOp-minimum-normal] | 0.0190 | 0.59 | 3.56 | torch 100.3%, torch-compile 98.8% | - |
| 🟡 | MinimumFwdOp | test_minimum_manifest_bench[hidden-state-prefill-float16] | 0.0150 | 0.56 | 3.35 | torch 100.4%, torch-compile 98.1% | - |
| 🟡 | MinimumFwdOp | test_minimum_manifest_bench[hidden-state-prefill-bfloat16] | 0.0150 | 0.56 | 3.35 | torch 100.4%, torch-compile 98.5% | - |
| 🔵 | MinimumFwdOp | test_minimum_manifest_bench[hidden-state-prefill-float32] | 0.0265 | 0.32 | 3.80 | torch 100.2%, torch-compile 105.5% | - |
| 🔴 | MinimumFwdOp | test_minimum_manifest_bench[cnn-feat-broadcast-float16] | 0.0396 | 0.32 | 1.30 | torch 127.6%, torch-compile 36.4% | - |
| 🔴 | MinimumFwdOp | test_minimum_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0396 | 0.32 | 1.30 | torch 129.1%, torch-compile 36.3% | - |
| 🟡 | MinimumFwdOp | test_minimum_manifest_bench[cnn-feat-broadcast-float32] | 0.0301 | 0.43 | 3.42 | torch 176.6%, torch-compile 87.9% | - |
| 🟡 | MishFwdOp | test_mish_manifest_bench[yolo-p3-float16] | 0.0709 | 1.48 | 1.48 | torch 89.5%, torch-compile 103.5% | - |
| 🟡 | MishFwdOp | test_mish_manifest_bench[yolo-p3-bfloat16] | 0.0708 | 1.48 | 1.48 | torch 90.8%, torch-compile 104.6% | - |
| 🟡 | MishFwdOp | test_mish_manifest_bench[yolo-p4-float16] | 0.0372 | 1.41 | 1.41 | torch 89.9%, torch-compile 103.4% | - |
| 🟡 | MishFwdOp | test_mish_manifest_bench[yolo-p4-bfloat16] | 0.0368 | 1.42 | 1.42 | torch 90.9%, torch-compile 104.8% | - |
| 🟢 | MoeGateUpFwdOp | test_moe_gate_up_bench[deepseek-v3-decode-gate-up-bfloat16] | 3.4611 | 69.49 | 4.37 | torch-ref 191.6%, torch-compile 226.9% | - |
| 🟢 | MoeGateUpFwdOp | test_moe_gate_up_bench[deepseek-v3-prefill-gate-up-bfloat16] | 4.3776 | 439.54 | 3.57 | torch-ref 159.0%, torch-compile 618.5% | - |
| 🔵 | MoeGroupedGemmNopadFwdOp | test_moe_grouped_gemm_nopad_bench[deepseek-v3-decode-gate-up-bfloat16] | 3.7490 | 64.16 | 4.03 | torch-ref 137.9%, torch-compile 156.2% | - |
| 🔵 | MoeGroupedGemmNopadFwdOp | test_moe_grouped_gemm_nopad_bench[deepseek-v3-prefill-gate-up-bfloat16] | 4.2912 | 448.39 | 3.68 | torch-ref 125.9%, torch-compile 251.8% | - |
| 🔵 | MoeGroupedGemmNopadFwdOp | test_moe_grouped_gemm_nopad_bench[deepseek-v3-decode-down-bfloat16] | 1.9090 | 63.00 | 3.98 | torch-ref 141.0%, torch-compile 292.3% | - |
| 🔵 | MoeGroupedGemmNopadFwdOp | test_moe_grouped_gemm_nopad_bench[deepseek-v3-prefill-down-bfloat16] | 2.1531 | 446.83 | 3.77 | torch-ref 132.1%, torch-compile 1198.0% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[kimi-k2-decode-int32] | 0.0169 | 0.00 | 0.01 | triton 287.1% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[kimi-k2-small-int32] | 0.0194 | 0.00 | 0.01 | triton 247.9% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[kimi-k2-medium-int32] | 0.0217 | 0.00 | 0.01 | triton 257.5% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[kimi-k2-prefill-int32] | 0.0410 | 0.00 | 0.01 | triton 208.5% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[deepseek-v3-decode-int32] | 0.0148 | 0.00 | 0.00 | triton 228.9% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[deepseek-v3-small-int32] | 0.0153 | 0.00 | 0.00 | triton 220.0% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[deepseek-v3-medium-int32] | 0.0177 | 0.00 | 0.01 | triton 236.4% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[deepseek-v3-prefill-int32] | 0.0378 | 0.00 | 0.01 | triton 196.2% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[qwen3-decode-int32] | 0.0108 | 0.00 | 0.00 | triton 156.8% | - |
| 🔵 | MoePermuteAlignFwdOp | test_permute_align_bench[qwen3-small-int32] | 0.0121 | 0.00 | 0.00 | triton 149.8% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[qwen3-medium-int32] | 0.0141 | 0.00 | 0.00 | triton 212.0% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[qwen3-prefill-int32] | 0.0318 | 0.00 | 0.01 | triton 251.6% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[kimi-k2-decode-bfloat16] | 0.0106 | 0.00 | 0.01 | vllm 109.9% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[kimi-k2-small-bfloat16] | 0.0118 | 0.00 | 0.35 | vllm 117.0% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[kimi-k2-medium-bfloat16] | 0.0356 | 0.00 | 1.85 | vllm 129.3% | - |
| 🟡 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[kimi-k2-prefill-bfloat16] | 0.2857 | 0.00 | 1.85 | vllm 94.9% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-decode-bfloat16] | 0.0093 | 0.00 | 0.01 | vllm 124.5% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-small-bfloat16] | 0.0104 | 0.00 | 0.40 | vllm 132.2% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-medium-bfloat16] | 0.0337 | 0.00 | 1.96 | vllm 136.2% | - |
| 🟡 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-prefill-bfloat16] | 0.2789 | 0.00 | 1.90 | vllm 96.8% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-235b-decode-bfloat16] | 0.0080 | 0.00 | 0.02 | vllm 144.2% | - |
| 🟢 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-235b-small-bfloat16] | 0.0090 | 0.00 | 0.46 | vllm 153.2% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-235b-medium-bfloat16] | 0.0314 | 0.00 | 2.11 | vllm 146.7% | - |
| 🟡 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-235b-prefill-bfloat16] | 0.2686 | 0.00 | 1.97 | vllm 97.0% | - |
| 🟢 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-30b-decode-bfloat16] | 0.0063 | 0.00 | 0.01 | vllm 168.0% | - |
| 🟢 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-30b-small-bfloat16] | 0.0072 | 0.00 | 0.25 | vllm 173.3% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-30b-medium-bfloat16] | 0.0207 | 0.00 | 1.37 | vllm 139.8% | - |
| 🟡 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-30b-prefill-bfloat16] | 0.1420 | 0.00 | 1.60 | vllm 91.2% | - |
|  | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-ep2-decode-bfloat16] | 0.0087 | 0.00 | 0.02 | - | - |
|  | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-ep2-medium-bfloat16] | 0.0281 | 0.00 | 2.36 | - | - |
|  | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-ep2-prefill-bfloat16] | 0.2100 | 0.00 | 2.52 | - | - |
|  | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-235b-ep2-medium-bfloat16] | 0.0265 | 0.00 | 2.49 | - | - |
| 🟢 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[large-hidden-decode-bfloat16] | 0.0070 | 0.02 | 0.02 | vllm 239.7% | - |
| 🟢 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[large-hidden-small-bfloat16] | 0.0079 | 0.46 | 0.52 | vllm 227.3% | - |
| 🔵 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[large-hidden-medium-bfloat16] | 0.0213 | 2.75 | 3.10 | vllm 137.3% | - |
| 🔵 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[large-hidden-prefill-bfloat16] | 0.1330 | 3.53 | 3.98 | vllm 104.6% | - |
| 🟢 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[small-hidden-decode-bfloat16] | 0.0057 | 0.01 | 0.01 | vllm 158.2% | - |
| 🟢 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[small-hidden-small-bfloat16] | 0.0065 | 0.24 | 0.27 | vllm 153.2% | - |
| 🔵 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[small-hidden-medium-bfloat16] | 0.0116 | 2.18 | 2.45 | vllm 128.2% | - |
| 🔵 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[small-hidden-prefill-bfloat16] | 0.0616 | 3.27 | 3.68 | vllm 109.6% | - |
| 🟡 | MulFwdOp | test_binary_arith_bench[mul-1024x4096-float16-float16-MulFwdOp-mul-normal] | 0.0084 | 0.50 | 2.99 | torch 101.9%, torch-compile 100.0% | - |
| 🔵 | MulFwdOp | test_binary_arith_bench[mul-1024x10240-float16-float16-MulFwdOp-mul-normal] | 0.0176 | 0.59 | 3.57 | torch 100.7%, torch-compile 100.0% | - |
| 🟡 | MulFwdOp | test_binary_arith_bench[mul-1024x11008-float16-float16-MulFwdOp-mul-normal] | 0.0186 | 0.61 | 3.64 | torch 100.0%, torch-compile 99.8% | - |
| 🔵 | MulFwdOp | test_mul_manifest_bench[hidden-state-prefill-float16] | 0.0149 | 0.56 | 3.39 | torch 100.1%, torch-compile 100.1% | - |
| 🟡 | MulFwdOp | test_mul_manifest_bench[hidden-state-prefill-bfloat16] | 0.0147 | 0.57 | 3.42 | torch 100.2%, torch-compile 99.8% | - |
| 🟡 | MulFwdOp | test_mul_manifest_bench[hidden-state-prefill-float32] | 0.0265 | 0.32 | 3.80 | torch 99.6%, torch-compile 99.5% | - |
| 🟡 | MulFwdOp | test_mul_manifest_bench[cnn-feat-broadcast-float16] | 0.0165 | 0.78 | 3.11 | torch 275.2%, torch-compile 86.2% | - |
| 🟡 | MulFwdOp | test_mul_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0165 | 0.78 | 3.11 | torch 280.2%, torch-compile 87.8% | - |
| 🔵 | MulFwdOp | test_mul_manifest_bench[cnn-feat-broadcast-float32] | 0.0266 | 0.48 | 3.87 | torch 187.0%, torch-compile 100.1% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-8b-short-float16] | 0.2438 | 88.08 | 0.48 | torch-sdpa 68.0% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-8b-short-bfloat16] | 0.4550 | 47.20 | 0.26 | torch-sdpa 36.4% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-8b-long-float16] | 0.9014 | 190.59 | 0.26 | torch-sdpa 75.7% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-8b-long-bfloat16] | 1.3119 | 130.95 | 0.18 | torch-sdpa 51.8% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-70b-short-float16] | 0.2445 | 87.83 | 0.48 | torch-sdpa 67.9% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-70b-short-bfloat16] | 0.4558 | 47.11 | 0.26 | torch-sdpa 36.4% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-70b-long-float16] | 0.8916 | 192.70 | 0.26 | torch-sdpa 76.5% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-70b-long-bfloat16] | 1.1029 | 155.78 | 0.21 | torch-sdpa 61.6% | - |
| 🟢 | MultiHeadAttentionDecodePagedWithKVCacheFwdOp | test_mha_decode_paged_bench[single-token-page128-float16] | 0.0061 | 0.69 | 0.69 | flashinfer 150.8% | - |
| 🟢 | MultiHeadAttentionDecodePagedWithKVCacheFwdOp | test_mha_decode_paged_bench[batch2-page256-float16] | 0.0057 | 0.74 | 0.37 | flashinfer 172.5% | - |
| 🟢 | MultiHeadAttentionDecodePagedWithKVCacheFwdOp | test_mha_decode_paged_bench[longer-cache-float16] | 0.0053 | 0.39 | 0.39 | flashinfer 182.6% | - |
| 🟢 | MultiHeadAttentionDecodePagedWithKVCacheFwdOp | test_mha_decode_paged_bench[shorter-cache-float16] | 0.0046 | 0.23 | 0.23 | flashinfer 201.4% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-8b-4k-float16] | 0.5115 | 4.20 | 4.20 | flashinfer 103.5% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-8b-4k-bfloat16] | 0.5106 | 4.21 | 4.21 | flashinfer 103.8% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-8b-32k-float16] | 0.9805 | 4.38 | 4.38 | flashinfer 101.8% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-8b-32k-bfloat16] | 0.9803 | 4.38 | 4.38 | flashinfer 101.9% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-70b-4k-float16] | 0.5140 | 4.18 | 4.18 | flashinfer 103.2% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-70b-4k-bfloat16] | 0.5141 | 4.18 | 4.18 | flashinfer 103.1% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-70b-32k-float16] | 0.9800 | 4.38 | 4.38 | flashinfer 101.9% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-70b-32k-bfloat16] | 0.9798 | 4.38 | 4.38 | flashinfer 101.8% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-8b-short-float16] | 0.0425 | 201.98 | 1.58 | flashinfer 97.6% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-8b-short-bfloat16] | 0.0426 | 201.60 | 1.58 | flashinfer 96.0% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-8b-long-float16] | 0.1682 | 408.65 | 0.80 | flashinfer 97.7% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-8b-long-bfloat16] | 0.1670 | 411.55 | 0.80 | flashinfer 97.2% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-70b-short-float16] | 0.0428 | 200.62 | 1.57 | flashinfer 96.7% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-70b-short-bfloat16] | 0.0424 | 202.75 | 1.58 | flashinfer 96.8% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-70b-long-float16] | 0.1685 | 407.80 | 0.80 | flashinfer 97.3% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-70b-long-bfloat16] | 0.1670 | 411.39 | 0.80 | flashinfer 97.2% | - |
| 🟢 | MultiHeadLatentAttentionDecodeWithKVCacheFwdOp | test_mla_decode_bench[deepseek-v2-4k-float16] | 0.0372 | 288.76 | 1.42 | torch-ref 442.6%, torch-compile 343.8% | - |
| 🟢 | MultiHeadLatentAttentionDecodeWithKVCacheFwdOp | test_mla_decode_bench[deepseek-v2-4k-bfloat16] | 0.0373 | 287.53 | 1.42 | torch-ref 438.3%, torch-compile 358.5% | - |
| 🟢 | MultiHeadLatentAttentionDecodeWithKVCacheFwdOp | test_mla_decode_bench[deepseek-v2-32k-float16] | 0.1189 | 180.55 | 0.85 | torch-ref 230.7%, torch-compile 212.0% | - |
| 🟢 | MultiHeadLatentAttentionDecodeWithKVCacheFwdOp | test_mla_decode_bench[deepseek-v2-32k-bfloat16] | 0.1189 | 180.59 | 0.85 | torch-ref 234.2%, torch-compile 215.2% | - |
| 🟢 | MultiHeadLatentAttentionDecodeWithKVCacheFwdOp | test_mla_decode_bench[deepseek-v3-4k-bfloat16] | 0.0216 | 248.56 | 1.23 | torch-ref 393.1%, torch-compile 323.4% | - |
| 🔵 | MultiHeadLatentAttentionDecodeWithKVCacheFwdOp | test_mla_decode_bench[deepseek-v3-32k-bfloat16] | 0.1180 | 91.03 | 0.43 | torch-ref 145.5%, torch-compile 138.4% | - |
| 🟡 | NanToNumFwdOp | test_nan_to_num_manifest_bench[elementwise-16M-float16] | 0.0189 | 5.32 | 3.55 | torch 101.9%, torch-compile 98.1% | - |
| 🟡 | NanToNumFwdOp | test_nan_to_num_manifest_bench[elementwise-16M-bfloat16] | 0.0189 | 5.32 | 3.55 | torch 101.7%, torch-compile 98.1% | - |
| 🔵 | NanToNumFwdOp | test_nan_to_num_manifest_bench[elementwise-16M-float32] | 0.0339 | 2.97 | 3.96 | torch 100.4%, torch-compile 100.5% | - |
| 🟡 | NanToNumFwdOp | test_nan_to_num_manifest_bench[elementwise-256M-float16] | 0.2651 | 6.07 | 4.05 | torch 103.4%, torch-compile 97.6% | - |
| 🟡 | NanToNumFwdOp | test_nan_to_num_manifest_bench[elementwise-256M-bfloat16] | 0.2639 | 6.10 | 4.07 | torch 103.6%, torch-compile 97.9% | - |
| 🟡 | NeFwdOp | test_comparison_bench[ne-1024x4096-float16-ne] | 0.0080 | 0.52 | 2.61 | torch 97.2%, torch-compile 97.2% | - |
| 🟡 | NeFwdOp | test_ne_manifest_bench[hidden-state-prefill-float16] | 0.0141 | 0.59 | 2.97 | torch 93.2%, torch-compile 93.2% | - |
| 🟡 | NeFwdOp | test_ne_manifest_bench[hidden-state-prefill-bfloat16] | 0.0141 | 0.59 | 2.97 | torch 95.0%, torch-compile 95.0% | - |
| 🟡 | NeFwdOp | test_ne_manifest_bench[hidden-state-prefill-float32] | 0.0224 | 0.38 | 3.38 | torch 99.9%, torch-compile 99.6% | - |
| 🔴 | NeFwdOp | test_ne_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.81 | 2.42 | torch 299.2%, torch-compile 74.9% | - |
| 🔴 | NeFwdOp | test_ne_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.81 | 2.43 | torch 307.2%, torch-compile 74.6% | - |
| 🟡 | NeFwdOp | test_ne_manifest_bench[cnn-feat-broadcast-float32] | 0.0214 | 0.60 | 3.01 | torch 223.7%, torch-compile 86.1% | - |
| 🔵 | NegFwdOp | test_neg_bench[elementwise-16M-float16] | 0.0179 | 0.94 | 3.75 | torch 105.1%, torch-compile 100.1% | - |
| 🔵 | NegFwdOp | test_neg_bench[elementwise-16M-bfloat16] | 0.0179 | 0.94 | 3.75 | torch 100.2%, torch-compile 100.2% | - |
| 🟡 | NegFwdOp | test_neg_bench[elementwise-16M-float32] | 0.0340 | 0.49 | 3.94 | torch 99.7%, torch-compile 99.8% | - |
| 🟡 | NegFwdOp | test_neg_bench[elementwise-256M-float16] | 0.2519 | 1.07 | 4.26 | torch 106.5%, torch-compile 99.1% | - |
| 🟡 | NegFwdOp | test_neg_bench[elementwise-256M-bfloat16] | 0.2511 | 1.07 | 4.28 | torch 99.4%, torch-compile 99.4% | - |
| 🔵 | PowFwdOp | test_binary_arith_bench[pow-1024x4096-float16-float16-PowFwdOp-pow-positive] | 0.0199 | 0.21 | 1.26 | torch 101.1%, torch-compile 118.5% | - |
| 🔵 | PowFwdOp | test_binary_arith_bench[pow-1024x10240-float16-float16-PowFwdOp-pow-positive] | 0.0448 | 0.23 | 1.41 | torch 101.2%, torch-compile 120.7% | - |
| 🔵 | PowFwdOp | test_pow_manifest_bench[hidden-state-prefill-float16] | 0.0365 | 0.69 | 1.38 | torch 101.7%, torch-compile 120.2% | - |
| 🔵 | PowFwdOp | test_pow_manifest_bench[hidden-state-prefill-bfloat16] | 0.0375 | 0.67 | 1.34 | torch 100.8%, torch-compile 120.7% | - |
| 🟡 | PowFwdOp | test_pow_manifest_bench[hidden-state-prefill-float32] | 0.0387 | 0.65 | 2.60 | torch 96.3%, torch-compile 110.2% | - |
| 🔵 | PowFwdOp | test_pow_manifest_bench[cnn-feat-broadcast-float16] | 0.0571 | 0.68 | 0.90 | torch 164.9%, torch-compile 106.9% | - |
| 🔵 | PowFwdOp | test_pow_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0588 | 0.65 | 0.87 | torch 161.7%, torch-compile 104.9% | - |
| 🔵 | PowFwdOp | test_pow_manifest_bench[cnn-feat-broadcast-float32] | 0.0572 | 0.67 | 1.79 | torch 163.6%, torch-compile 102.6% | - |
| 🟡 | PreluFwdOp | test_prelu_manifest_bench[cnn-feat-per-channel-float16] | 0.0147 | 1.75 | 3.51 | torch 321.6%, torch-compile 99.8% | - |
| 🔵 | PreluFwdOp | test_prelu_manifest_bench[cnn-feat-per-channel-bfloat16] | 0.0144 | 1.79 | 3.58 | torch 339.3%, torch-compile 100.0% | - |
| 🔵 | PreluFwdOp | test_prelu_manifest_bench[cnn-feat-per-channel-deep-float16] | 0.0084 | 1.54 | 3.08 | torch 299.6%, torch-compile 100.4% | - |
| 🟡 | PreluFwdOp | test_prelu_manifest_bench[cnn-feat-per-channel-deep-bfloat16] | 0.0082 | 1.57 | 3.14 | torch 314.4%, torch-compile 99.6% | - |
| 🔴 | ProdFwdOp | test_prod_bench[hidden-state-reduce-float16] | 0.0989 | 0.08 | 0.17 | flaggems 8.0%, torch 49.9%, torch-compile 8.4% | - |
| 🔴 | ProdFwdOp | test_prod_bench[hidden-state-reduce-bfloat16] | 0.0999 | 0.08 | 0.17 | flaggems 7.8%, torch 49.8%, torch-compile 8.4% | - |
| 🔴 | ProdFwdOp | test_prod_bench[long-seq-reduce-bfloat16] | 0.0172 | 0.12 | 0.24 | flaggems 78.6%, torch 97.4%, torch-compile 26.2% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-8b-prefill-float16] | 0.0119 | 2.82 | 2.82 | flaggems 106.5%, flashinfer 92.1%, vllm 104.6%, torch-ref 1221.0%, torch-compile 114.2% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-8b-prefill-bfloat16] | 0.0126 | 2.65 | 2.66 | flaggems 98.6%, flashinfer 86.1%, vllm 100.8%, torch-ref 1156.3%, torch-compile 118.0% | - |
| 🔵 | RMSNormFwdOp | test_rms_norm_bench[llama-8b-decode-bfloat16] | 0.0021 | 0.01 | 0.01 | flaggems 159.2%, flashinfer 103.1%, vllm 127.7%, torch-ref 867.7%, torch-compile 106.2% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-70b-prefill-float16] | 0.0210 | 3.19 | 3.20 | flaggems 98.7%, flashinfer 95.5%, vllm 103.0%, torch-ref 1285.3%, torch-compile 93.8% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-70b-prefill-bfloat16] | 0.0219 | 3.07 | 3.07 | flaggems 97.8%, flashinfer 92.0%, vllm 101.0%, torch-ref 1239.2%, torch-compile 96.3% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-70b-decode-bfloat16] | 0.0026 | 0.01 | 0.02 | flaggems 157.9%, flashinfer 98.8%, vllm 118.3%, torch-ref 714.6%, torch-compile 102.4% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-405b-prefill-float16] | 0.0420 | 3.19 | 3.19 | flaggems 95.0%, flashinfer 88.2%, vllm 115.8%, torch-ref 1213.3%, torch-compile 94.5% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-405b-prefill-bfloat16] | 0.0430 | 3.12 | 3.12 | flaggems 95.5%, flashinfer 88.5%, vllm 113.5%, torch-ref 1190.8%, torch-compile 95.4% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-405b-decode-bfloat16] | 0.0036 | 0.02 | 0.03 | flaggems 127.5%, flashinfer 97.4%, vllm 119.5%, torch-ref 555.8%, torch-compile 129.2% | - |
| 🟡 | ReciprocalFwdOp | test_reciprocal_bench[elementwise-16M-float16] | 0.0193 | 0.87 | 3.48 | torch 98.2%, torch-compile 94.4% | - |
| 🟡 | ReciprocalFwdOp | test_reciprocal_bench[elementwise-16M-bfloat16] | 0.0193 | 0.87 | 3.48 | torch 98.3%, torch-compile 94.7% | - |
| 🟡 | ReciprocalFwdOp | test_reciprocal_bench[elementwise-16M-float32] | 0.0341 | 0.49 | 3.94 | torch 99.9%, torch-compile 99.2% | - |
| 🟡 | ReciprocalFwdOp | test_reciprocal_bench[elementwise-256M-float16] | 0.2727 | 0.98 | 3.94 | torch 98.0%, torch-compile 93.9% | - |
| 🟡 | ReciprocalFwdOp | test_reciprocal_bench[elementwise-256M-bfloat16] | 0.2729 | 0.98 | 3.94 | torch 97.9%, torch-compile 94.5% | - |
| 🟡 | ReluFwdOp | test_relu_manifest_bench[hidden-state-prefill-float16] | 0.0103 | 0.81 | 3.25 | torch 104.3%, torch-compile 99.9% | - |
| 🔵 | ReluFwdOp | test_relu_manifest_bench[hidden-state-prefill-bfloat16] | 0.0103 | 0.81 | 3.25 | torch 101.6%, torch-compile 100.3% | - |
| 🔵 | ReluFwdOp | test_relu_manifest_bench[hidden-state-decode-bfloat16] | 0.0013 | 0.00 | 0.01 | torch 110.0%, torch-compile 102.5% | - |
| 🔵 | RemainderFwdOp | test_binary_arith_bench[remainder-1024x4096-float16-float16-RemainderFwdOp-remainder-positive] | 0.0086 | 0.49 | 2.93 | torch 124.2%, torch-compile 100.4% | - |
| 🔵 | RemainderFwdOp | test_binary_arith_bench[remainder-1024x10240-float16-float16-RemainderFwdOp-remainder-positive] | 0.0182 | 0.58 | 3.46 | torch 119.2%, torch-compile 100.0% | - |
| 🔵 | RemainderFwdOp | test_remainder_manifest_bench[hidden-state-prefill-float16] | 0.0155 | 2.17 | 3.25 | torch 116.7%, torch-compile 100.6% | - |
| 🔵 | RemainderFwdOp | test_remainder_manifest_bench[hidden-state-prefill-bfloat16] | 0.0150 | 2.24 | 3.35 | torch 123.7%, torch-compile 100.6% | - |
| 🔵 | RemainderFwdOp | test_remainder_manifest_bench[hidden-state-prefill-float32] | 0.0264 | 1.27 | 3.81 | torch 102.8%, torch-compile 100.8% | - |
| 🟡 | RemainderFwdOp | test_remainder_manifest_bench[cnn-feat-broadcast-float16] | 0.0200 | 2.57 | 2.57 | torch 311.4%, torch-compile 89.0% | - |
| 🟡 | RemainderFwdOp | test_remainder_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0200 | 2.57 | 2.57 | torch 321.6%, torch-compile 93.4% | - |
| 🟡 | RemainderFwdOp | test_remainder_manifest_bench[cnn-feat-broadcast-float32] | 0.0275 | 1.87 | 3.74 | torch 233.3%, torch-compile 97.8% | - |
| 🔵 | RopeLlama31FwdOp | test_rope_llama31_bench[llama31-1d-8k-d128-bfloat16] | 0.0036 | 1.16 | 1.74 | torch-ref 439.9%, torch-compile 114.6% | - |
| 🔴 | RopeLlama31FwdOp | test_rope_llama31_bench[llama31-2d-b1-s8k-h32-d128-float16] | 0.0594 | 2.26 | 2.30 | torch-ref 829.5%, torch-compile 58.6% | - |
| 🔵 | RopeLongRopeFwdOp | test_rope_longrope_bench[longrope-1d-8k-d128-bfloat16] | 0.0036 | 1.17 | 1.76 | torch-ref 443.7%, torch-compile 116.1% | - |
| 🔴 | RopeLongRopeFwdOp | test_rope_longrope_bench[longrope-2d-b1-s8k-h32-d128-float16] | 0.0594 | 2.26 | 2.30 | torch-ref 828.9%, torch-compile 58.6% | - |
| 🔵 | RopeNeoxFwdOp | test_rope_neox_bench[neox-1d-2k-d64-float16] | 0.0018 | 0.29 | 0.43 | torch-ref 517.5%, torch-compile 108.8% | - |
| 🔵 | RopeNeoxFwdOp | test_rope_neox_bench[neox-1d-4k-d128-bfloat16] | 0.0026 | 0.81 | 1.21 | torch-ref 475.3%, torch-compile 121.0% | - |
| 🔴 | RopeNeoxFwdOp | test_rope_neox_bench[neox-2d-b2-s2k-h32-d128-float16] | 0.0309 | 2.17 | 2.19 | torch-ref 881.2%, torch-compile 59.8% | - |
| 🔴 | RopeNeoxPositionIdsFwdOp | test_rope_neox_position_ids_bench[position-ids-s2k-h32-d128-float16] | 0.0278 | 1.21 | 1.24 | vllm 87.1%, torch-ref 464.9%, torch-compile 42.6% | - |
| 🔴 | RopeNeoxPositionIdsFwdOp | test_rope_neox_position_ids_bench[position-ids-s4k-h32-d128-bfloat16] | 0.0455 | 1.47 | 1.52 | vllm 98.2%, torch-ref 548.6%, torch-compile 49.0% | - |
| 🟡 | RopeNonNeoxFwdOp | test_rope_non_neox_bench[non-neox-1d-2k-d64-float16] | 0.0022 | 0.24 | 0.36 | torch-ref 433.8%, torch-compile 91.2% | - |
| 🔴 | RopeNonNeoxFwdOp | test_rope_non_neox_bench[non-neox-2d-b2-s2k-h32-d128-bfloat16] | 0.0252 | 2.66 | 2.69 | torch-ref 1090.1%, torch-compile 75.6% | - |
| 🔵 | RopeYarnFwdOp | test_rope_yarn_bench[yarn-1d-8k-d128-bfloat16] | 0.0036 | 1.16 | 1.74 | torch-ref 440.7%, torch-compile 115.0% | - |
| 🔴 | RopeYarnFwdOp | test_rope_yarn_bench[yarn-2d-b1-s8k-h32-d128-float16] | 0.0595 | 2.26 | 2.29 | torch-ref 827.6%, torch-compile 58.6% | - |
| 🟡 | RoundFwdOp | test_round_bench[elementwise-16M-float16] | 0.0180 | 0.93 | 3.74 | torch 100.1%, torch-compile 99.8% | - |
| 🟡 | RoundFwdOp | test_round_bench[elementwise-16M-bfloat16] | 0.0180 | 0.93 | 3.74 | torch 100.0%, torch-compile 99.7% | - |
| 🟡 | RoundFwdOp | test_round_bench[elementwise-16M-float32] | 0.0340 | 0.49 | 3.94 | torch 99.8%, torch-compile 99.7% | - |
| 🟡 | RoundFwdOp | test_round_bench[elementwise-256M-float16] | 0.2529 | 1.06 | 4.25 | torch 98.9%, torch-compile 98.9% | - |
| 🟡 | RoundFwdOp | test_round_bench[elementwise-256M-bfloat16] | 0.2532 | 1.06 | 4.24 | torch 98.8%, torch-compile 98.7% | - |
| 🟡 | RsqrtFwdOp | test_rsqrt_bench[elementwise-16M-float16] | 0.0182 | 0.92 | 3.69 | torch 100.0%, torch-compile 99.8% | - |
| 🟡 | RsqrtFwdOp | test_rsqrt_bench[elementwise-16M-bfloat16] | 0.0182 | 0.92 | 3.68 | torch 100.0%, torch-compile 99.7% | - |
| 🔵 | RsqrtFwdOp | test_rsqrt_bench[elementwise-16M-float32] | 0.0332 | 0.50 | 4.04 | torch 101.6%, torch-compile 101.5% | - |
| 🟡 | RsqrtFwdOp | test_rsqrt_bench[elementwise-256M-float16] | 0.2555 | 1.05 | 4.20 | torch 99.6%, torch-compile 98.9% | - |
| 🟡 | RsqrtFwdOp | test_rsqrt_bench[elementwise-256M-bfloat16] | 0.2565 | 1.05 | 4.19 | torch 99.2%, torch-compile 98.8% | - |
| 🔵 | SSDChunkScanFwdOp | test_ssd_chunk_scan_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0729 | 88.42 | 1.44 | mamba 138.4%, torch-ref 2689.6%, torch-compile 696.7% | - |
| 🔵 | SSDChunkScanFwdOp | test_ssd_chunk_scan_fwd_bench[mamba2-780m-b1-s4k-bfloat16] | 0.0759 | 84.86 | 1.38 | mamba 133.9%, torch-ref 2582.4%, torch-compile 669.5% | - |
| 🔵 | SSDChunkScanFwdOp | test_ssd_chunk_scan_fwd_bench[mamba2-2p7b-b4-s2k-bfloat16] | 0.2372 | 90.53 | 1.46 | mamba 130.3%, torch-ref 2746.6%, torch-compile 691.5% | - |
| 🔵 | SSDChunkScanFwdOp | test_ssd_chunk_scan_fwd_bench[mamba2-1p3b-b2-s32k-float16] | 1.4672 | 93.68 | 1.52 | mamba 138.6%, torch-ref 2730.9%, torch-compile 678.1% | - |
| 🔵 | SSDChunkStateFwdOp | test_ssd_chunk_state_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0237 | 136.23 | 2.21 | mamba 105.0%, torch-ref 34290.5%, torch-compile 2667.9% | - |
| 🔵 | SSDChunkStateFwdOp | test_ssd_chunk_state_fwd_bench[mamba2-780m-b1-s4k-bfloat16] | 0.0240 | 134.96 | 2.19 | mamba 110.1%, torch-ref 33945.2%, torch-compile 2821.8% | - |
| 🔵 | SSDChunkStateFwdOp | test_ssd_chunk_state_fwd_bench[mamba2-2p7b-b4-s2k-bfloat16] | 0.0655 | 164.68 | 2.65 | mamba 122.1%, torch-ref 41386.1%, torch-compile 3734.1% | - |
| 🔵 | SSDChunkStateFwdOp | test_ssd_chunk_state_fwd_bench[mamba2-780m-b1-s4k-seq-idx-float16] | 0.0286 | 112.94 | 1.84 | mamba 120.8%, torch-ref 28449.7%, torch-compile 2620.1% | - |
| 🔵 | SSDChunkStateFwdOp | test_ssd_chunk_state_fwd_bench[mamba2-780m-b1-s4k-seq-idx-bfloat16] | 0.0289 | 111.81 | 1.82 | mamba 101.2%, torch-ref 28177.2%, torch-compile 2721.8% | - |
| 🔵 | SSDChunkStateFwdOp | test_ssd_chunk_state_fwd_bench[mamba2-1p3b-b2-s32k-seq-idx-float16] | 0.4497 | 153.45 | 2.48 | mamba 144.3%, torch-ref 38489.2%, torch-compile 3706.9% | - |
| 🟢 | SSDDecodeFwdOp | test_ssd_decode_bench[mamba2-1p3b-decode-b1-float16] | 0.0040 | 1.05 | 1.59 | torch-ref 761.5%, torch-compile 223.3% | - |
| 🟢 | SSDDecodeFwdOp | test_ssd_decode_bench[mamba2-1p3b-decode-b1-bfloat16] | 0.0040 | 1.06 | 1.60 | torch-ref 769.3%, torch-compile 228.2% | - |
| 🟢 | SSDDecodeFwdOp | test_ssd_decode_bench[mamba2-2p7b-decode-b8-float16] | 0.0163 | 2.58 | 2.76 | torch-ref 687.6%, torch-compile 187.3% | - |
| 🟢 | SSDDecodeFwdOp | test_ssd_decode_bench[mamba2-780m-decode-b32-float16] | 0.0360 | 2.79 | 2.87 | torch-ref 667.7%, torch-compile 184.7% | - |
| 🟢 | SSDStatePassingFwdOp | test_ssd_state_passing_fwd_bench[mamba2-1p3b-b1-s4k-dstate-float16] | 0.0020 | 0.13 | 0.42 | mamba 429.6%, torch-ref 6205.6%, torch-compile 152.5% | - |
| 🟢 | SSDStatePassingFwdOp | test_ssd_state_passing_fwd_bench[mamba2-1p3b-b1-s4k-dstate-bfloat16] | 0.0020 | 0.13 | 0.41 | mamba 421.0%, torch-ref 6169.4%, torch-compile 206.4% | - |
| 🟢 | SSDStatePassingFwdOp | test_ssd_state_passing_fwd_bench[mamba2-2p7b-b2-s32k-dstate-float16] | 0.0106 | 0.50 | 1.50 | mamba 565.6%, torch-ref 10821.2%, torch-compile 838.1% | - |
| 🔵 | SSDStatePassingFwdOp | test_ssd_state_passing_fwd_bench[mamba2-1p3b-b1-s4k-dstate-init-states-float16] | 0.0020 | 0.13 | 0.43 | mamba 438.7%, torch-ref 6058.4%, torch-compile 109.6% | - |
| 🟢 | SSDStatePassingFwdOp | test_ssd_state_passing_fwd_bench[mamba2-1p3b-b1-s4k-dstate-init-states-bfloat16] | 0.0020 | 0.13 | 0.42 | mamba 431.9%, torch-ref 6026.0%, torch-compile 170.7% | - |
| 🟡 | SSDStatePassingFwdOp | test_ssd_state_passing_fwd_bench[mamba2-1p3b-b1-s4k-flat-init-states-float32] | 0.0220 | 0.76 | 3.25 | mamba 98.2%, torch-ref 579.3%, torch-compile 93.4% | - |
| 🔵 | SeluFwdOp | test_selu_manifest_bench[snn-fc-float16] | 0.0119 | 3.52 | 2.82 | torch 150.8%, torch-compile 135.2% | - |
| 🔵 | SeluFwdOp | test_selu_manifest_bench[snn-fc-bfloat16] | 0.0121 | 3.47 | 2.77 | torch 150.0%, torch-compile 129.4% | - |
| 🔵 | SeluFwdOp | test_selu_manifest_bench[snn-fc-wide-float16] | 0.0213 | 3.94 | 3.15 | torch 154.4%, torch-compile 140.2% | - |
| 🔵 | SeluFwdOp | test_selu_manifest_bench[snn-fc-wide-bfloat16] | 0.0218 | 3.84 | 3.08 | torch 152.5%, torch-compile 133.9% | - |
| 🔴 | SharedFusedMoE | test_shared_fused_moe_bench[1-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 2.5266 | 0.59 | 0.59 | vllm 16.9% | - |
| 🟡 | SharedFusedMoE | test_shared_fused_moe_bench[32-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 4.7470 | 10.09 | 3.66 | vllm 83.5% | - |
| 🔵 | SharedFusedMoE | test_shared_fused_moe_bench[512-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 8.0744 | 94.95 | 4.29 | vllm 108.6% | - |
| 🔴 | SharedFusedMoE | test_shared_fused_moe_bench[2048-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 19.5214 | 157.09 | 1.78 | vllm 59.7% | - |
| 🔴 | SharedFusedMoE | test_shared_fused_moe_bench[4096-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 32.5771 | 188.27 | 1.07 | vllm 45.1% | - |
| 🔴 | SigmoidFwdOp | test_sigmoid_manifest_bench[elementwise-16M-float16] | 0.0288 | 2.33 | 2.33 | torch 80.1%, torch-compile 64.6% | - |
| 🔴 | SigmoidFwdOp | test_sigmoid_manifest_bench[elementwise-16M-bfloat16] | 0.0253 | 2.65 | 2.65 | torch 93.0%, torch-compile 73.8% | - |
| 🟡 | SigmoidFwdOp | test_sigmoid_manifest_bench[elementwise-16M-float32] | 0.0349 | 1.92 | 3.84 | torch 98.5%, torch-compile 97.4% | - |
| 🔴 | SigmoidFwdOp | test_sigmoid_manifest_bench[elementwise-256M-float16] | 0.4244 | 2.53 | 2.53 | torch 75.6%, torch-compile 61.3% | - |
| 🔴 | SigmoidFwdOp | test_sigmoid_manifest_bench[elementwise-256M-bfloat16] | 0.3676 | 2.92 | 2.92 | torch 89.7%, torch-compile 71.6% | - |
| 🟡 | SignFwdOp | test_sign_bench[elementwise-16M-float16] | 0.0190 | 1.77 | 3.54 | torch 95.5%, torch-compile 94.6% | - |
| 🟡 | SignFwdOp | test_sign_bench[elementwise-16M-bfloat16] | 0.0190 | 1.77 | 3.54 | torch 96.0%, torch-compile 94.9% | - |
| 🟡 | SignFwdOp | test_sign_bench[elementwise-16M-float32] | 0.0341 | 0.98 | 3.93 | torch 99.7%, torch-compile 99.7% | - |
| 🟡 | SignFwdOp | test_sign_bench[elementwise-256M-float16] | 0.2703 | 1.99 | 3.97 | torch 94.7%, torch-compile 93.2% | - |
| 🟡 | SignFwdOp | test_sign_bench[elementwise-256M-bfloat16] | 0.2702 | 1.99 | 3.97 | torch 95.7%, torch-compile 94.0% | - |
| 🔵 | SiluAndMulFwdOp | test_silu_and_mul_bench[llama-8b-swiglu-prefill-float16] | 0.0433 | 4.07 | 4.07 | flashinfer 123.2%, torch-ref 437.3%, torch-compile 102.2% | - |
| 🔵 | SiluAndMulFwdOp | test_silu_and_mul_bench[llama-8b-swiglu-prefill-bfloat16] | 0.0433 | 4.07 | 4.07 | flashinfer 124.8%, torch-ref 439.7%, torch-compile 105.9% | - |
| 🟡 | SiluAndMulFwdOp | test_silu_and_mul_bench[llama-8b-swiglu-decode-bfloat16] | 0.0018 | 0.05 | 0.05 | flashinfer 243.6%, torch-ref 201.8%, torch-compile 85.5% | - |
| 🔴 | SiluFwdOp | test_silu_manifest_bench[llama-8b-ffn-prefill-float16] | 0.0504 | 2.91 | 2.33 | torch 75.2%, torch-compile 70.6% | - |
| 🟡 | SiluFwdOp | test_silu_manifest_bench[llama-8b-ffn-prefill-bfloat16] | 0.0432 | 3.40 | 2.72 | torch 87.8%, torch-compile 82.9% | - |
| 🟡 | SiluFwdOp | test_silu_manifest_bench[llama-8b-ffn-decode-bfloat16] | 0.0015 | 0.05 | 0.04 | torch 129.2%, torch-compile 91.7% | - |
| 🔵 | SinFwdOp | test_sin_bench[elementwise-16M-float16] | 0.0256 | 0.66 | 2.62 | torch 102.4%, torch-compile 103.4% | - |
| 🔵 | SinFwdOp | test_sin_bench[elementwise-16M-bfloat16] | 0.0260 | 0.65 | 2.58 | torch 103.0%, torch-compile 103.5% | - |
| 🟡 | SinFwdOp | test_sin_bench[elementwise-16M-float32] | 0.0355 | 0.47 | 3.78 | torch 96.5%, torch-compile 96.4% | - |
| 🔵 | SinFwdOp | test_sin_bench[elementwise-256M-float16] | 0.3708 | 0.72 | 2.90 | torch 101.8%, torch-compile 103.6% | - |
| 🔵 | SinFwdOp | test_sin_bench[elementwise-256M-bfloat16] | 0.3767 | 0.71 | 2.85 | torch 102.5%, torch-compile 103.9% | - |
| 🔵 | SinusoidalFwdOp | test_sinusoidal_bench[transformer-2k-4k-float16] | 0.0424 | 1.19 | 0.40 | torch-ref 250.9%, torch-compile 133.7% | - |
| 🔵 | SinusoidalFwdOp | test_sinusoidal_bench[transformer-2k-4k-bfloat16] | 0.0424 | 1.19 | 0.40 | torch-ref 250.8%, torch-compile 133.9% | - |
| 🔵 | SinusoidalFwdOp | test_sinusoidal_bench[transformer-4k-4k-float16] | 0.0818 | 1.23 | 0.41 | torch-ref 243.5%, torch-compile 136.6% | - |
| 🔵 | SinusoidalFwdOp | test_sinusoidal_bench[transformer-4k-4k-bfloat16] | 0.0818 | 1.23 | 0.41 | torch-ref 243.4%, torch-compile 136.6% | - |
| 🔴 | SoftmaxFwdOp | test_softmax_bench[attn-weights-4k-float16] | 0.0112 | 1.87 | 1.49 | flaggems 76.6%, torch 176.1%, torch-compile 143.6% | - |
| 🔴 | SoftmaxFwdOp | test_softmax_bench[attn-weights-4k-bfloat16] | 0.0113 | 1.86 | 1.49 | flaggems 77.0%, torch 174.2%, torch-compile 148.0% | - |
| 🔴 | SoftmaxFwdOp | test_softmax_bench[attn-weights-4k-float32] | 0.0143 | 1.47 | 2.35 | flaggems 77.8%, torch 141.7%, torch-compile 129.2% | - |
| 🟡 | SoftmaxFwdOp | test_softmax_bench[attn-weights-32k-bfloat16] | 0.0672 | 2.50 | 2.00 | flaggems 95.7%, torch 124.3%, torch-compile 140.1% | - |
| 🔴 | SoftmaxFwdOp | test_softmax_bench[lm-head-logits-float16] | 0.0298 | 0.07 | 0.05 | flaggems 94.4%, torch 110.4%, torch-compile 32.3% | - |
| 🔴 | SoftmaxFwdOp | test_softmax_bench[lm-head-logits-bfloat16] | 0.0311 | 0.07 | 0.05 | flaggems 95.3%, torch 108.4%, torch-compile 30.9% | - |
| 🔴 | SoftmaxFwdOp | test_softmax_bench[lm-head-logits-float32] | 0.0365 | 0.06 | 0.09 | flaggems 85.7%, torch 108.1%, torch-compile 26.9% | - |
| 🟡 | SoftplusFwdOp | test_softplus_manifest_bench[mlp-hidden-float16] | 0.0196 | 2.14 | 1.71 | torch 121.7%, torch-compile 91.3% | - |
| 🟡 | SoftplusFwdOp | test_softplus_manifest_bench[mlp-hidden-bfloat16] | 0.0196 | 2.13 | 1.71 | torch 122.6%, torch-compile 93.0% | - |
| 🟡 | SoftplusFwdOp | test_softplus_manifest_bench[mlp-hidden-wide-float16] | 0.0365 | 2.30 | 1.84 | torch 122.8%, torch-compile 89.8% | - |
| 🟡 | SoftplusFwdOp | test_softplus_manifest_bench[mlp-hidden-wide-bfloat16] | 0.0366 | 2.29 | 1.83 | torch 123.5%, torch-compile 92.4% | - |
| 🟡 | SqrtFwdOp | test_sqrt_bench[elementwise-16M-float16] | 0.0189 | 0.89 | 3.54 | torch 99.7%, torch-compile 98.5% | - |
| 🟡 | SqrtFwdOp | test_sqrt_bench[elementwise-16M-bfloat16] | 0.0190 | 0.88 | 3.54 | torch 99.8%, torch-compile 98.5% | - |
| 🔵 | SqrtFwdOp | test_sqrt_bench[elementwise-16M-float32] | 0.0338 | 0.50 | 3.98 | torch 100.8%, torch-compile 100.5% | - |
| 🟡 | SqrtFwdOp | test_sqrt_bench[elementwise-256M-float16] | 0.2684 | 1.00 | 4.00 | torch 99.1%, torch-compile 98.0% | - |
| 🟡 | SqrtFwdOp | test_sqrt_bench[elementwise-256M-bfloat16] | 0.2696 | 1.00 | 3.98 | torch 99.1%, torch-compile 98.1% | - |
| 🔵 | StdFwdOp | test_std_bench[hidden-state-std-float16] | 0.0099 | 4.22 | 1.69 | flaggems 106.9%, torch 681.1%, torch-compile 189.1% | - |
| 🔵 | StdFwdOp | test_std_bench[hidden-state-std-bfloat16] | 0.0099 | 4.24 | 1.70 | flaggems 112.0%, torch 688.2%, torch-compile 194.8% | - |
| 🟡 | StdFwdOp | test_std_bench[long-seq-std-bfloat16] | 0.0072 | 1.46 | 0.59 | flaggems 183.9%, torch 347.8%, torch-compile 85.7% | - |
| 🔴 | StdFwdOp | test_std_bench[3d-multidim-reduce-float16] | 0.0120 | 0.87 | 0.35 | flaggems 118.9%, torch 223.2%, torch-compile 53.6% | - |
| 🔵 | SubFwdOp | test_binary_arith_bench[sub-1024x4096-float16-float16-SubFwdOp-sub-normal] | 0.0084 | 0.50 | 2.98 | torch 100.8%, torch-compile 100.0% | - |
| 🔵 | SubFwdOp | test_binary_arith_bench[sub-1024x10240-float16-float16-SubFwdOp-sub-normal] | 0.0176 | 0.59 | 3.57 | torch 100.5%, torch-compile 100.2% | - |
| 🔵 | SubFwdOp | test_binary_arith_bench[sub-1024x11008-float16-float16-SubFwdOp-sub-normal] | 0.0185 | 0.61 | 3.65 | torch 100.5%, torch-compile 100.2% | - |
| 🔵 | SubFwdOp | test_sub_manifest_bench[hidden-state-prefill-float16] | 0.0148 | 1.13 | 3.39 | torch 100.2%, torch-compile 100.0% | - |
| 🔵 | SubFwdOp | test_sub_manifest_bench[hidden-state-prefill-bfloat16] | 0.0148 | 1.13 | 3.40 | torch 100.4%, torch-compile 100.0% | - |
| 🟡 | SubFwdOp | test_sub_manifest_bench[hidden-state-prefill-float32] | 0.0265 | 0.63 | 3.80 | torch 99.9%, torch-compile 99.7% | - |
| 🟡 | SubFwdOp | test_sub_manifest_bench[cnn-feat-broadcast-float16] | 0.0165 | 1.56 | 3.11 | torch 277.8%, torch-compile 87.3% | - |
| 🟡 | SubFwdOp | test_sub_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0165 | 1.55 | 3.11 | torch 280.3%, torch-compile 87.8% | - |
| 🟡 | SubFwdOp | test_sub_manifest_bench[cnn-feat-broadcast-float32] | 0.0266 | 0.96 | 3.86 | torch 185.3%, torch-compile 99.5% | - |
| 🟡 | SumFwdOp | test_sum_bench[hidden-state-reduce-float16] | 0.0085 | 0.98 | 1.96 | flaggems 102.6%, torch 578.8%, torch-compile 97.8% | - |
| 🟡 | SumFwdOp | test_sum_bench[hidden-state-reduce-bfloat16] | 0.0086 | 0.97 | 1.94 | flaggems 101.8%, torch 576.5%, torch-compile 97.4% | - |
| 🔴 | SumFwdOp | test_sum_bench[long-seq-reduce-bfloat16] | 0.0052 | 0.40 | 0.80 | flaggems 73.0%, torch 323.9%, torch-compile 84.7% | - |
| 🔴 | SumFwdOp | test_sum_bench[hidden-state-reduce-dim0-bfloat16] | 0.0686 | 0.12 | 0.24 | flaggems 20.0%, torch 65.6%, torch-compile 16.2% | - |
| 🟡 | SumFwdOp | test_sum_bench[hidden-state-reduce-keepdim-bfloat16] | 0.0087 | 0.97 | 1.94 | flaggems 101.7%, torch 575.3%, torch-compile 97.2% | - |
| 🔴 | SumFwdOp | test_sum_bench[3d-multidim-reduce-float16] | 0.0115 | 0.18 | 0.37 | flaggems 117.3%, torch 168.8%, torch-compile 39.3% | - |
| 🟡 | TanhFwdOp | test_tanh_manifest_bench[elementwise-16M-float16] | 0.0210 | 0.80 | 3.19 | torch 98.8%, torch-compile 115.4% | - |
| 🔵 | TanhFwdOp | test_tanh_manifest_bench[elementwise-16M-bfloat16] | 0.0213 | 0.79 | 3.14 | torch 102.6%, torch-compile 114.8% | - |
| 🔵 | TanhFwdOp | test_tanh_manifest_bench[elementwise-16M-float32] | 0.0341 | 0.49 | 3.94 | torch 100.1%, torch-compile 101.1% | - |
| 🟡 | TanhFwdOp | test_tanh_manifest_bench[elementwise-256M-float16] | 0.2988 | 0.90 | 3.59 | torch 97.9%, torch-compile 115.0% | - |
| 🔵 | TanhFwdOp | test_tanh_manifest_bench[elementwise-256M-bfloat16] | 0.3027 | 0.89 | 3.55 | torch 102.4%, torch-compile 115.7% | - |
| 🟢 | TopkSelectorFwdOp | test_topk_selector_bench[topk1024-s32k-kv64k-float32] | 15.6140 | 0.14 | 0.56 | torch 203.9%, torch-compile 203.9% | - |
| 🟢 | TopkSelectorFwdOp | test_topk_selector_bench[topk2048-s32k-kv64k-float32] | 16.2475 | 0.13 | 0.55 | torch 205.0%, torch-compile 204.9% | - |
| 🟡 | TruncFwdOp | test_trunc_bench[elementwise-16M-float16] | 0.0180 | 0.93 | 3.74 | torch 99.8%, torch-compile 100.0% | - |
| 🟡 | TruncFwdOp | test_trunc_bench[elementwise-16M-bfloat16] | 0.0180 | 0.93 | 3.74 | torch 100.0%, torch-compile 99.7% | - |
| 🟡 | TruncFwdOp | test_trunc_bench[elementwise-16M-float32] | 0.0341 | 0.49 | 3.94 | torch 99.7%, torch-compile 99.5% | - |
| 🟡 | TruncFwdOp | test_trunc_bench[elementwise-256M-float16] | 0.2532 | 1.06 | 4.24 | torch 98.9%, torch-compile 98.8% | - |
| 🟡 | TruncFwdOp | test_trunc_bench[elementwise-256M-bfloat16] | 0.2532 | 1.06 | 4.24 | torch 98.8%, torch-compile 98.7% | - |
| 🟢 | VarFwdOp | test_var_bench[hidden-state-var-float16] | 0.0099 | 4.26 | 1.70 | flaggems 152.3%, torch 685.1%, torch-compile 185.4% | - |
| 🟢 | VarFwdOp | test_var_bench[hidden-state-var-bfloat16] | 0.0100 | 4.19 | 1.68 | flaggems 154.0%, torch 680.2%, torch-compile 187.2% | - |
| 🟡 | VarFwdOp | test_var_bench[long-seq-var-bfloat16] | 0.0071 | 1.47 | 0.59 | flaggems 156.1%, torch 348.9%, torch-compile 84.8% | - |
| 🔴 | VarFwdOp | test_var_bench[3d-multidim-reduce-float16] | 0.0120 | 0.88 | 0.35 | flaggems 118.2%, torch 223.5%, torch-compile 52.1% | - |
| 🔵 | VarMeanFwdOp | test_var_mean_bench[hidden-state-var-mean-float16] | 0.0105 | 4.01 | 1.60 | flaggems 144.0%, torch 1111.3%, torch-compile 200.3% | - |
| 🔵 | VarMeanFwdOp | test_var_mean_bench[hidden-state-var-mean-bfloat16] | 0.0106 | 3.96 | 1.58 | flaggems 146.5%, torch 1106.0%, torch-compile 206.6% | - |
| 🔵 | VarMeanFwdOp | test_var_mean_bench[long-seq-var-mean-bfloat16] | 0.0072 | 1.46 | 0.58 | flaggems 154.7%, torch 562.7%, torch-compile 107.5% | - |
| 🔴 | VarMeanFwdOp | test_var_mean_bench[3d-multidim-reduce-float16] | 0.0120 | 0.87 | 0.35 | flaggems 117.5%, torch 374.4%, torch-compile 65.7% | - |
| 🟡 | WhereFwdOp | test_where_manifest_bench[elementwise-16M-float16] | 0.0310 | 0.54 | 3.79 | torch 99.3%, torch-compile 99.1% | - |
| 🟡 | WhereFwdOp | test_where_manifest_bench[elementwise-16M-bfloat16] | 0.0311 | 0.54 | 3.77 | torch 98.9%, torch-compile 98.8% | - |
| 🟡 | WhereFwdOp | test_where_manifest_bench[elementwise-16M-float32] | 0.0537 | 0.31 | 4.06 | torch 99.5%, torch-compile 99.0% | - |
| 🟡 | WhereFwdOp | test_where_manifest_bench[elementwise-256M-float16] | 0.4290 | 0.63 | 4.38 | torch 99.8%, torch-compile 99.8% | - |
| 🟡 | WhereFwdOp | test_where_manifest_bench[elementwise-256M-bfloat16] | 0.4288 | 0.63 | 4.38 | torch 99.8%, torch-compile 99.8% | - |
| 🟡 | div_bcast | test_broadcast_bench[div-1024x4096-1x4096-float16-DivFwdOp-div-positive] | 0.0070 | 0.60 | 2.41 | torch 233.9%, torch-compile 89.0% | - |
| 🟡 | div_bcast | test_broadcast_bench[div-1024x10240-1x10240-float16-DivFwdOp-div-positive] | 0.0150 | 0.70 | 2.80 | torch 242.3%, torch-compile 82.3% | - |
| 🟡 | div_bcast | test_broadcast_bench[div-1024x11008-1x11008-float16-DivFwdOp-div-positive] | 0.0160 | 0.70 | 2.81 | torch 241.8%, torch-compile 81.6% | - |
| 🔴 | gelu_and_mul_strategy | test_fused_gated_strategy_bench[gelu_and_mul-1024-4096-float16-GeluAndMulFwdKernel-direct] | 0.0182 | 0.46 | 1.38 | torch 183.7%, torch-compile 58.4% | - |
| 🔵 | gelu_and_mul_strategy | test_fused_gated_strategy_bench[gelu_and_mul-1024-4096-float16-GeluAndMulFwdKernel-explicit_parallel] | 0.0100 | 0.84 | 2.51 | torch 333.6%, torch-compile 106.4% | - |
| 🔴 | gelu_tanh_and_mul_strategy | test_fused_gated_strategy_bench[gelu_tanh_and_mul-1024-4096-float16-GeluTanhAndMulFwdKernel-direct] | 0.0178 | 0.47 | 1.42 | torch 179.5%, torch-compile 54.9% | - |
| 🔵 | gelu_tanh_and_mul_strategy | test_fused_gated_strategy_bench[gelu_tanh_and_mul-1024-4096-float16-GeluTanhAndMulFwdKernel-explicit_parallel] | 0.0088 | 0.95 | 2.85 | torch 360.9%, torch-compile 110.5% | - |
| 🟡 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-up-T=32768] | 18.6916 | 705.89 | 0.98 | torch 126.2%, deepgemm 98.9%, triton 148.1%, triton-tma 128.7% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-up-T=65536] | 37.3056 | 707.35 | 0.63 | torch 112.3%, deepgemm 111.2%, triton 146.3%, triton-tma 114.5% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-up-T=131072] | 74.8085 | 705.49 | 0.46 | torch 108.1%, deepgemm 100.4%, triton 143.4%, triton-tma 114.2% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-up-T=262144] | 151.9630 | 694.60 | 0.37 | torch 113.1%, deepgemm 101.1%, triton 140.7%, triton-tma 107.2% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[Llama4-128E-up-T=131072] | 31.0565 | 708.07 | 0.87 | torch 104.7%, deepgemm 100.1%, triton 167.8%, triton-tma 132.1% | - |
| 🟡 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[qwen3.5-397B-up-T52429] | 12.5977 | 698.23 | 1.19 | torch 105.5%, deepgemm 99.7%, triton 155.8%, triton-tma 142.2% | - |
| 🟡 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-down-T=32768] | 9.6555 | 683.25 | 1.11 | torch 103.5%, deepgemm 99.3%, triton 151.8%, triton-tma 118.0% | - |
| 🟡 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-down-T=65536] | 19.1613 | 688.58 | 0.78 | torch 129.5%, deepgemm 98.7%, triton 150.9%, triton-tma 110.2% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-down-T=131072] | 38.8974 | 678.41 | 0.61 | torch 107.5%, deepgemm 111.8%, triton 148.6%, triton-tma 113.5% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-down-T=262144] | 77.8570 | 677.87 | 0.52 | torch 107.0%, deepgemm 101.4%, triton 148.3%, triton-tma 108.0% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[Llama4-128E-down-T=131072] | 15.3607 | 715.79 | 0.93 | torch 104.4%, deepgemm 101.1%, triton 150.7%, triton-tma 121.5% | - |
| 🟡 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[qwen3.5-397B-down-T52429] | 6.9645 | 631.50 | 1.39 | torch 106.8%, deepgemm 96.7%, triton 147.6%, triton-tma 129.7% | - |
| 🟡 | grouped_gemm_nn | test_grouped_gemm_bench[nn-batch16-m4096-n4096-k4096-float16] | 0.3411 | 402.89 | 1.77 | torch-ref 90.4%, torch-compile 80.1% | - |
| 🟢 | grouped_gemm_nt | test_grouped_gemm_bench[nt-batch16-m4096-n4096-k4096-float16] | 0.2316 | 593.39 | 2.61 | torch-ref 1005.1%, torch-compile 990.5% | - |
| 🟢 | grouped_gemm_nt | test_grouped_gemm_bench[nt-batch16-m4096-n4096-k4096-bfloat16] | 0.2262 | 607.53 | 2.67 | torch-ref 1027.9%, torch-compile 1011.7% | - |
| 🔴 | grouped_gemm_tn | test_grouped_gemm_bench[tn-batch16-m4096-n4096-k4096-float16] | 0.7822 | 175.70 | 0.77 | torch-ref 67.1%, torch-compile 66.7% | - |
| 🟡 | mul_bcast | test_broadcast_bench[mul-1024x4096-1x4096-float16-MulFwdOp-mul-normal] | 0.0064 | 0.66 | 2.62 | torch 232.5%, torch-compile 94.5% | - |
| 🟡 | mul_bcast | test_broadcast_bench[mul-1024x10240-1x10240-float16-MulFwdOp-mul-normal] | 0.0136 | 0.77 | 3.09 | torch 243.1%, torch-compile 90.8% | - |
| 🟡 | mul_bcast | test_broadcast_bench[mul-1024x11008-1x11008-float16-MulFwdOp-mul-normal] | 0.0145 | 0.78 | 3.11 | torch 243.3%, torch-compile 89.4% | - |
| 🔴 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float16-SiluAndMulFwdKernel-direct] | 0.0178 | 0.47 | 1.41 | torch 177.0%, torch-compile 46.7% | - |
| 🔴 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-11008-float16-SiluAndMulFwdKernel-direct] | 0.0450 | 0.50 | 1.50 | torch 170.7%, torch-compile 42.4% | - |
| 🔴 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-4096-4096-float16-SiluAndMulFwdKernel-direct] | 0.0662 | 0.51 | 1.52 | torch 168.4%, torch-compile 40.6% | - |
| 🔴 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-bfloat16-SiluAndMulFwdKernel-direct] | 0.0178 | 0.47 | 1.41 | torch 177.7%, torch-compile 47.2% | - |
| 🔴 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float32-SiluAndMulFwdKernel-direct] | 0.0200 | 0.42 | 2.51 | torch 173.8%, torch-compile 73.0% | - |
| 🟡 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float16-SiluAndMulFwdKernel-explicit_parallel] | 0.0084 | 0.99 | 2.98 | torch 373.5%, torch-compile 98.5% | - |
| 🔵 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-11008-float16-SiluAndMulFwdKernel-explicit_parallel] | 0.0189 | 1.19 | 3.58 | torch 406.6%, torch-compile 100.7% | - |
| 🔵 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-4096-4096-float16-SiluAndMulFwdKernel-explicit_parallel] | 0.0267 | 1.26 | 3.78 | torch 417.8%, torch-compile 101.0% | - |
| 🔵 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-bfloat16-SiluAndMulFwdKernel-explicit_parallel] | 0.0084 | 1.00 | 2.99 | torch 376.4%, torch-compile 100.0% | - |
| 🟡 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float32-SiluAndMulFwdKernel-explicit_parallel] | 0.0148 | 0.57 | 3.40 | torch 234.3%, torch-compile 98.7% | - |
| 🟡 | sub_bcast | test_broadcast_bench[sub-1024x4096-1x4096-float16-SubFwdOp-sub-normal] | 0.0064 | 0.66 | 2.62 | torch 233.0%, torch-compile 93.0% | - |
| 🟡 | sub_bcast | test_broadcast_bench[sub-1024x10240-1x10240-float16-SubFwdOp-sub-normal] | 0.0136 | 0.77 | 3.09 | torch 243.8%, torch-compile 89.9% | - |
| 🟡 | sub_bcast | test_broadcast_bench[sub-1024x11008-1x11008-float16-SubFwdOp-sub-normal] | 0.0145 | 0.78 | 3.11 | torch 244.3%, torch-compile 89.7% | - |

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
