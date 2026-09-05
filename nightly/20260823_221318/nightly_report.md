# ❌ TileOPs Nightly Report

> **2026-08-23 19:17** &ensp;|&ensp; `f4e9c3f` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Correctness** | ✅ &ensp; (513/513 tests across 92 ops) |
| **Benchmarked Ops** | 191 |
| **Benchmark Failures** | ✅ None &ensp;|&ensp; ⚠️ 13 skipped |
| **Regressions** (vs 14-day best) | ⚠️ 1 |
| **Baseline Alerts** (< 80%) | ⚠️ 293 |
| **Never-built kernels** | ⚠️ 9 files &ensp;·&ensp; `kernels/attention/deepseek_mla_decode.py` at 5.8% |
| **Untested roofline math** | 735 lines in `perf/` &ensp;·&ensp; `perf/formulas.py` at 13.1% |
| **Untested op logic** | 2164 lines in `ops/` &ensp;·&ensp; 43.5% of branches taken |
| | <sub>coverage compared against the 2026-08-23 run; no figure means it held</sub> |

## ⚠️ Performance Regressions (vs 14-day best)

| Op | Config | Best (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|----------:|-----------:|------:|-------:|
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[lightning-indexer-s8k-h32-d64-bfloat16] | 0.1626 | 0.6180 | +280.2% | 55.60 |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 80%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-gate-up-block128-float8_e4m3fn] | 0.3424 | 0.0129 | 3.8% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **CumprodFwdOp** | test_cumprod_bench[long-seq-scan-bfloat16] | 0.2501 | 0.0122 | 4.9% | torch-compile |
| 🔴 | **ProdFwdOp** | test_prod_bench[hidden-state-reduce-bfloat16] | 0.0998 | 0.0078 | 7.8% | flaggems |
| 🔴 | **ProdFwdOp** | test_prod_bench[hidden-state-reduce-float16] | 0.0989 | 0.0078 | 7.9% | flaggems |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-gate-up-block128-float8_e4m3fn] | 1.3359 | 0.1382 | 10.3% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[gemv-down-m1-block128-float8_e4m3fn] | 0.0631 | 0.0077 | 12.3% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **SumFwdOp** | test_sum_bench[hidden-state-reduce-dim0-bfloat16] | 0.0686 | 0.0111 | 16.2% | torch-compile |
| 🔴 | **SharedFusedMoE** | test_shared_fused_moe_bench[1-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 2.5204 | 0.4265 | 16.9% | vllm |
| 🔴 | **AnyFwdOp** | test_any_bench[3d-multidim-reduce-bool] | 0.0214 | 0.0040 | 18.7% | torch-compile |
| 🔴 | **AllFwdOp** | test_all_bench[3d-multidim-reduce-bool] | 0.0216 | 0.0041 | 19.1% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[k-dominant-7168x16384-block128-float8_e4m3fn] | 3.6222 | 0.7706 | 21.3% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[large-spatial-float16] | 4.3427 | 1.0179 | 23.4% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-down-block128-float8_e4m3fn] | 0.0389 | 0.0092 | 23.7% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **CumsumFwdOp** | test_cumsum_bench[hidden-state-scan-float16] | 0.0444 | 0.0106 | 23.8% | flaggems |
| 🔴 | **AnyFwdOp** | test_any_bench[mask-validation-4k-bool] | 0.0072 | 0.0017 | 24.1% | torch-compile |
| 🔴 | **InfNormFwdOp** | test_inf_norm_bench[3d-multidim-reduce-float16] | 0.0216 | 0.0052 | 24.1% | torch-compile |
| 🔴 | **CumsumFwdOp** | test_cumsum_bench[hidden-state-scan-bfloat16] | 0.0435 | 0.0105 | 24.2% | flaggems |
| 🔴 | **AllFwdOp** | test_all_bench[mask-validation-4k-bool] | 0.0074 | 0.0018 | 24.3% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[mid-m96-gate-up-bfloat16] | 0.0687 | 0.0168 | 24.5% | torch-cublas |
| 🔴 | **LogSoftmaxFwdOp** | test_log_softmax_bench[lm-head-logits-float32] | 0.0366 | 0.0092 | 25.2% | torch-compile |
| 🔴 | **InfNormFwdOp** | test_inf_norm_bench[hidden-state-inf-float16] | 0.0302 | 0.0077 | 25.4% | flaggems |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[lm-head-logits-float32] | 0.0364 | 0.0093 | 25.6% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-decode-gate-up-bfloat16] | 0.0677 | 0.0173 | 25.6% | torch-cublas |
| 🔴 | **InfNormFwdOp** | test_inf_norm_bench[hidden-state-inf-bfloat16] | 0.0306 | 0.0079 | 25.8% | flaggems |
| 🔴 | **ProdFwdOp** | test_prod_bench[long-seq-reduce-bfloat16] | 0.0172 | 0.0044 | 25.9% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-attn-proj-block128-float8_e4m3fn] | 0.8100 | 0.2144 | 26.5% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **CumsumFwdOp** | test_cumsum_bench[long-seq-scan-bfloat16] | 0.0295 | 0.0080 | 27.1% | flaggems |
| 🔴 | **MaxPool1dFwdOp** | test_max_pool1d_bench[textcnn-global-float16] | 0.0135 | 0.0037 | 27.6% | torch-compile |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c128-b64-complex128] | 0.0305 | 0.0085 | 27.8% | torch-cufft |
| 🔴 | **InfNormFwdOp** | test_inf_norm_bench[long-seq-inf-bfloat16] | 0.0177 | 0.0050 | 28.3% | torch-compile |
| 🔴 | **Conv3dFwdOp** | test_conv3d_bench[3d-unet-aspp-3x3x3-rate6-float16] | 0.1265 | 0.0376 | 29.7% | torch-compile |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[lm-head-logits-float16] | 0.0299 | 0.0092 | 30.6% | torch-compile |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[lm-head-logits-bfloat16] | 0.0311 | 0.0096 | 30.9% | torch-compile |
| 🔴 | **AnyFwdOp** | test_any_bench[mask-validation-32k-bool] | 0.0106 | 0.0033 | 31.1% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[small-batch-down-m8-per-tensor-float8_e4m3fn] | 0.0267 | 0.0083 | 31.2% | deepgemm |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b4-dmem1024-d512-float16] | 0.0826 | 0.0259 | 31.3% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-bfloat16] | 0.4567 | 0.1430 | 31.3% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-bfloat16] | 0.4559 | 0.1432 | 31.4% | fa3 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-down-block128-float8_e4m3fn] | 0.4486 | 0.1429 | 31.9% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **Conv3dFwdOp** | test_conv3d_bench[unet-encoder-k3-s1-bfloat16] | 0.3550 | 0.1152 | 32.5% | torch-compile |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-stage2-float16] | 0.0107 | 0.0035 | 32.6% | torch-compile |
| 🔴 | **AllFwdOp** | test_all_bench[mask-validation-32k-bool] | 0.0106 | 0.0035 | 32.9% | torch-compile |
| 🔴 | **LogSoftmaxFwdOp** | test_log_softmax_bench[lm-head-logits-float16] | 0.0287 | 0.0097 | 33.7% | torch-compile |
| 🔴 | **Conv3dFwdOp** | test_conv3d_bench[unet-encoder-k3-s1-bias-bfloat16] | 0.3545 | 0.1223 | 34.5% | torch-compile |
| 🔴 | **MeanPoolingForwardOp** | test_mean_pooling_bench[dense-mainstream] | 0.1353 | 0.0471 | 34.8% | torch-view-mean |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-stage3-float16] | 0.0129 | 0.0046 | 35.6% | torch-compile |
| 🔴 | **MaximumFwdOp** | test_maximum_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0396 | 0.0142 | 35.9% | torch-compile |
| 🔴 | **LogSoftmaxFwdOp** | test_log_softmax_bench[lm-head-logits-bfloat16] | 0.0269 | 0.0097 | 35.9% | torch-compile |
| 🔴 | **MinimumFwdOp** | test_minimum_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0396 | 0.0144 | 36.3% | torch-compile |
| 🔴 | **MinimumFwdOp** | test_minimum_manifest_bench[cnn-feat-broadcast-float16] | 0.0395 | 0.0144 | 36.4% | torch-compile |
| 🔴 | **MaximumFwdOp** | test_maximum_manifest_bench[cnn-feat-broadcast-float16] | 0.0395 | 0.0144 | 36.5% | torch-compile |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-fc-float16] | 0.0061 | 0.0022 | 36.8% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[mid-m32-attn-bfloat16] | 0.0661 | 0.0244 | 36.9% | torch-cublas |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[wide-n-24576-block128-float8_e4m3fn] | 1.0368 | 0.3829 | 36.9% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-b64-complex64] | 0.0152 | 0.0056 | 37.0% | torch-cufft |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-2p7b-b2-s32k-dt-bias-float16] | 0.0598 | 0.0223 | 37.3% | mamba |
| 🔴 | **GemmFwdOp** | test_gemm_bench[mid-m16-attn-bfloat16] | 0.0657 | 0.0245 | 37.3% | torch-cublas |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-stage1-float16] | 0.0109 | 0.0041 | 37.7% | torch-compile |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[mha-decode-b32-pv-per-tensor-float8_e4m3fn] | 0.0647 | 0.0250 | 38.6% | flashinfer-bmm-fp8 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-short-bfloat16] | 0.4094 | 0.1588 | 38.8% | fa3 |
| 🔴 | **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[textcnn-global-float16] | 0.0193 | 0.0076 | 39.1% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[gemv-down-m1-per-tensor-float8_e4m3fn] | 0.0258 | 0.0102 | 39.4% | deepgemm |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-short-bfloat16] | 0.4159 | 0.1652 | 39.7% | fa3 |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b1-dmem512-d256-float16] | 0.0329 | 0.0131 | 39.9% | torch-compile |
| 🔴 | **SumFwdOp** | test_sum_bench[3d-multidim-reduce-float16] | 0.0115 | 0.0046 | 40.4% | torch-compile |
| 🔴 | **MeanPoolingForwardOp** | test_mean_pooling_bench[dense-batched] | 0.0702 | 0.0285 | 40.6% | torch-view-mean |
| 🔴 | **MeanFwdOp** | test_mean_bench[3d-multidim-reduce-float16] | 0.0115 | 0.0047 | 40.6% | torch-compile |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-4096-4096-float16-SiluAndMulFwdKernel-direct] | 0.0662 | 0.0269 | 40.7% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-down-per-tensor-float8_e4m3fn] | 0.0254 | 0.0104 | 40.9% | deepgemm |
| 🔴 | **L1NormFwdOp** | test_l1_norm_bench[3d-multidim-reduce-float16] | 0.0113 | 0.0046 | 41.0% | torch-compile |
| 🔴 | **ArgminFwdOp** | test_argmin_bench[hidden-state-argmin-bfloat16] | 0.0240 | 0.0099 | 41.2% | flaggems |
| 🔴 | **ArgminFwdOp** | test_argmin_bench[hidden-state-argmin-float16] | 0.0239 | 0.0099 | 41.3% | flaggems |
| 🔴 | **CountNonzeroFwdOp** | test_count_nonzero_bench[3d-multidim-reduce-float16] | 0.0115 | 0.0048 | 41.6% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-bfloat16] | 1.3119 | 0.5493 | 41.9% | fa3 |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-bfloat16] | 0.0154 | 0.0065 | 42.0% | mamba |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-1024-11008-float16-SiluAndMulFwdKernel-direct] | 0.0451 | 0.0191 | 42.3% | torch-compile |
| 🔴 | **MaxPool3dIndicesFwdOp** | test_max_pool3d_indices_bench[c3d-pool1-float16] | 0.3041 | 0.1293 | 42.5% | torch-compile |
| 🔴 | **AminFwdOp** | test_amin_bench[3d-multidim-reduce-float16] | 0.0115 | 0.0049 | 42.6% | torch-compile |
| 🔴 | **RopeNeoxPositionIdsFwdOp** | test_rope_neox_position_ids_bench[position-ids-s2k-h32-d128-float16] | 0.0278 | 0.0119 | 42.6% | torch-compile |
| 🔴 | **L2NormFwdOp** | test_l2_norm_bench[3d-multidim-reduce-float16] | 0.0114 | 0.0049 | 42.7% | torch-compile |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-dt-bias-bfloat16] | 0.0148 | 0.0064 | 42.9% | mamba |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[mha-decode-b64-qk-per-tensor-float8_e4m3fn] | 0.1154 | 0.0498 | 43.1% | flashinfer-bmm-fp8 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-prefill-varlen-mixed-fp16] | 0.1401 | 0.0615 | 43.9% | fa3 |
| 🔴 | **SharedFusedMoE** | test_shared_fused_moe_bench[4096-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 32.5404 | 14.6493 | 45.0% | vllm |
| 🔴 | **AmaxFwdOp** | test_amax_bench[3d-multidim-reduce-float16] | 0.0115 | 0.0052 | 45.2% | torch-compile |
| 🔴 | **grouped_gemm_tn** | test_grouped_gemm_bench[tn-batch16-m4096-n4096-k4096-float16] | 0.7812 | 0.3537 | 45.3% | torch |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float16-SiluAndMulFwdKernel-direct] | 0.0178 | 0.0083 | 46.7% | torch-compile |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-405b-p256-float16] | 0.0563 | 0.0266 | 47.1% | fa3 |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-bfloat16-SiluAndMulFwdKernel-direct] | 0.0178 | 0.0084 | 47.2% | torch-compile |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-bfloat16] | 1.2425 | 0.5892 | 47.4% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p256-float16] | 0.1682 | 0.0813 | 48.3% | fa3 |
| 🔴 | **ArgmaxFwdOp** | test_argmax_bench[hidden-state-argmax-bfloat16] | 0.0239 | 0.0116 | 48.7% | flaggems |
| 🔴 | **RopeNeoxPositionIdsFwdOp** | test_rope_neox_position_ids_bench[position-ids-s4k-h32-d128-bfloat16] | 0.0456 | 0.0222 | 48.7% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[wide-n-24576-bfloat16] | 0.9007 | 0.4432 | 49.2% | deepgemm |
| 🔴 | **GemmFwdOp** | test_gemm_bench[square-1k-nn-bfloat16] | 0.0145 | 0.0072 | 49.8% | torch-cublas |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-long-k-pressure-float16] | 0.2831 | 0.1410 | 49.8% | marlin-fp16 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-bfloat16] | 1.1018 | 0.5495 | 49.9% | fa3 |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-small-bfloat16] | 0.0395 | 0.0197 | 49.9% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[square-1k-nn-float16] | 0.0145 | 0.0072 | 50.0% | torch-cublas |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-down-per-tensor-float8_e4m3fn] | 0.2098 | 0.1057 | 50.4% | deepgemm |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-70b-prefill-varlen-q-lt-kv-bf16] | 0.1963 | 0.0991 | 50.5% | fa3 |
| 🔴 | **ArgmaxFwdOp** | test_argmax_bench[hidden-state-argmax-float16] | 0.0239 | 0.0122 | 50.9% | flaggems |
| 🔴 | **VarFwdOp** | test_var_bench[3d-multidim-reduce-float16] | 0.0119 | 0.0062 | 52.3% | torch-compile |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[compile-smoke-rect-128x256x256-float16] | 0.0059 | 0.0031 | 52.5% | torch-dequantized-matmul |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-gate-up-bfloat16] | 0.3360 | 0.1774 | 52.8% | torch-cublas |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-decode-down-bfloat16] | 0.0246 | 0.0132 | 53.4% | torch-cublas |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-70b-p256-float16] | 0.0684 | 0.0367 | 53.7% | fa3 |
| 🔴 | **StdFwdOp** | test_std_bench[3d-multidim-reduce-float16] | 0.0120 | 0.0064 | 53.7% | torch-compile |
| 🔴 | **BitwiseNotFwdOp** | test_bitwise_not_bench[elementwise-256M-int32] | 0.9380 | 0.5046 | 53.8% | torch |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-float16] | 0.0196 | 0.0106 | 54.1% | torch-compile |
| 🔴 | **CumprodFwdOp** | test_cumprod_bench[hidden-state-scan-float16] | 0.0444 | 0.0243 | 54.6% | torch-compile |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-bfloat16] | 0.0195 | 0.0106 | 54.6% | torch-compile |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-non-power2-low-cta-float16] | 0.0745 | 0.0408 | 54.7% | marlin-fp32 |
| 🔴 | **gelu_tanh_and_mul_strategy** | test_fused_gated_strategy_bench[gelu_tanh_and_mul-1024-4096-float16-GeluTanhAndMulFwdKernel-direct] | 0.0178 | 0.0098 | 54.9% | torch-compile |
| 🔴 | **MaxPool3dIndicesFwdOp** | test_max_pool3d_indices_bench[c3d-pool2-float16] | 0.0588 | 0.0326 | 55.4% | torch-compile |
| 🔴 | **BitwiseNotFwdOp** | test_bitwise_not_bench[elementwise-16M-int32] | 0.0610 | 0.0339 | 55.6% | torch-compile |
| 🔴 | **CumprodFwdOp** | test_cumprod_bench[hidden-state-scan-bfloat16] | 0.0436 | 0.0244 | 55.9% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-down-bfloat16] | 0.3209 | 0.1804 | 56.2% | deepgemm |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 1.0192 | 0.5766 | 56.6% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-prefill-varlen-uniform-fp16] | 0.1252 | 0.0712 | 56.9% | fa3 |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-medium-bfloat16] | 0.0544 | 0.0314 | 57.7% | torch-compile |
| 🔴 | **gelu_and_mul_strategy** | test_fused_gated_strategy_bench[gelu_and_mul-1024-4096-float16-GeluAndMulFwdKernel-direct] | 0.0182 | 0.0107 | 58.6% | torch-compile |
| 🔴 | **RopeYarnFwdOp** | test_rope_yarn_bench[yarn-2d-b1-s8k-h32-d128-float16] | 0.0594 | 0.0348 | 58.6% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-float16] | 0.2442 | 0.1431 | 58.6% | fa3 |
| 🔴 | **RopeLlama31FwdOp** | test_rope_llama31_bench[llama31-2d-b1-s8k-h32-d128-float16] | 0.0595 | 0.0349 | 58.7% | torch-compile |
| 🔴 | **RopeLongRopeFwdOp** | test_rope_longrope_bench[longrope-2d-b1-s8k-h32-d128-float16] | 0.0594 | 0.0349 | 58.8% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-float16] | 0.2437 | 0.1435 | 58.9% | fa3 |
| 🔴 | **TopkSelectorFwdOp** | test_topk_selector_bench[topk1024-s32k-kv64k-float32] | 15.6229 | 9.2720 | 59.4% | flashinfer |
| 🔴 | **SharedFusedMoE** | test_shared_fused_moe_bench[2048-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 19.5712 | 11.6230 | 59.4% | vllm |
| 🔴 | **RopeNeoxFwdOp** | test_rope_neox_bench[neox-2d-b2-s2k-h32-d128-float16] | 0.0310 | 0.0184 | 59.5% | torch-compile |
| 🔴 | **LogicalOrFwdOp** | test_logical_bench[logical_or-1024x10240-float16-LogicalOrFwdOp-logical_or] | 0.0171 | 0.0102 | 59.6% | torch-compile |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[throughput-8b-p64-float16] | 0.2516 | 0.1507 | 59.9% | flashinfer |
| 🔴 | **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[ecg-cnn-dilated-bfloat16] | 0.0223 | 0.0134 | 59.9% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[k-dominant-7168x16384-bfloat16] | 2.0651 | 1.2602 | 61.0% | deepgemm |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-float16] | 0.9025 | 0.5515 | 61.1% | fa3 |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-attn-proj-bfloat16] | 0.5424 | 0.3315 | 61.1% | deepgemm |
| 🔴 | **SigmoidFwdOp** | test_sigmoid_manifest_bench[elementwise-256M-float16] | 0.4247 | 0.2606 | 61.4% | torch-compile |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-float16] | 0.6354 | 0.3906 | 61.5% | fla |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-float16] | 0.1123 | 0.0692 | 61.6% | torch-compile |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-bfloat16] | 0.6379 | 0.3934 | 61.7% | fla |
| 🔴 | **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[global-1x1-float16] | 0.0133 | 0.0082 | 61.7% | torch-compile |
| 🔴 | **HardsigmoidFwdOp** | test_hardsigmoid_manifest_bench[mbv3-se-gate-bfloat16] | 0.0022 | 0.0013 | 61.8% | torch-compile |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-bfloat16] | 0.1124 | 0.0697 | 62.0% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-attn-proj-float16] | 0.5414 | 0.3362 | 62.1% | torch-cublas |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-float16] | 0.8921 | 0.5540 | 62.1% | fa3 |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-hbm-streaming-threshold-float16] | 0.0608 | 0.0379 | 62.3% | marlin-fp32 |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s896-bfloat16] | 0.0453 | 0.0284 | 62.8% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s896-float16] | 0.0454 | 0.0285 | 62.8% | fa3 |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[compile-smoke-square-64x64x128-float16] | 0.0043 | 0.0027 | 63.1% | torch-dequantized-matmul |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b8-dmem512-d256-bfloat16] | 0.0335 | 0.0212 | 63.3% | torch-compile |
| 🔴 | **LogicalAndFwdOp** | test_logical_bench[logical_and-1024x10240-float16-LogicalAndFwdOp-logical_and] | 0.0171 | 0.0109 | 63.7% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[mid-m64-down-bfloat16] | 0.0207 | 0.0132 | 63.8% | torch-cublas |
| 🔴 | **LogSumExpFwdOp** | test_logsumexp_bench[lm-head-logits-bfloat16] | 0.0164 | 0.0105 | 64.0% | torch-compile |
| 🔴 | **VarMeanFwdOp** | test_var_mean_bench[3d-multidim-reduce-float16] | 0.0121 | 0.0077 | 64.2% | torch-compile |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-float16] | 1.4238 | 0.9208 | 64.7% | fla |
| 🔴 | **SigmoidFwdOp** | test_sigmoid_manifest_bench[elementwise-16M-float16] | 0.0287 | 0.0186 | 64.7% | torch-compile |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-float32] | 0.0195 | 0.0127 | 64.9% | torch-compile |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-bfloat16] | 0.3164 | 0.2055 | 64.9% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-bfloat16] | 1.4644 | 0.9536 | 65.1% | fla |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-float16] | 0.3139 | 0.2050 | 65.3% | fla |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0051 | 0.0033 | 65.4% | mamba |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-float16] | 0.3809 | 0.2493 | 65.5% | fla |
| 🔴 | **TopkSelectorFwdOp** | test_topk_selector_bench[topk2048-s32k-kv64k-float32] | 16.2446 | 10.6661 | 65.7% | flashinfer |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-l2-resident-ish-float16] | 0.0331 | 0.0218 | 65.8% | marlin-fp16 |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-float16] | 0.2016 | 0.1336 | 66.3% | fla |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-float32] | 0.1077 | 0.0715 | 66.4% | torch-compile |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s1792-float16] | 0.1288 | 0.0858 | 66.6% | fa3 |
| 🔴 | **GroupNormFwdOp** | test_group_norm_bench[wider-channel-g32-affine-float16] | 0.0060 | 0.0040 | 66.7% | flaggems |
| 🔴 | **AvgPool1dFwdOp** | test_avg_pool1d_bench[ceil-bfloat16] | 0.0035 | 0.0023 | 66.7% | torch-compile |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-bfloat16] | 0.3876 | 0.2584 | 66.7% | fla |
| 🔴 | **GroupNormFwdOp** | test_group_norm_bench[tail-spatial-g16-affine-float16] | 0.0061 | 0.0041 | 66.8% | flaggems |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s1792-bfloat16] | 0.1287 | 0.0861 | 66.9% | fa3 |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-bfloat16] | 0.7503 | 0.5017 | 66.9% | fla |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-unbatched-complex64] | 0.0081 | 0.0054 | 66.9% | torch-cufft |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-float16] | 0.7227 | 0.4863 | 67.3% | fla |
| 🔴 | **ArgmaxFwdOp** | test_argmax_bench[3d-non-last-axis-argmax-float16] | 0.0056 | 0.0038 | 67.6% | flaggems |
| 🔴 | **HardsigmoidFwdOp** | test_hardsigmoid_manifest_bench[mbv3-se-gate-deep-bfloat16] | 0.0022 | 0.0015 | 67.7% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-bfloat16] | 0.0971 | 0.0658 | 67.8% | fla |
| 🔴 | **AvgPool1dFwdOp** | test_avg_pool1d_bench[audio-downsample-float16] | 0.0062 | 0.0042 | 67.9% | torch-compile |
| 🔴 | **HardsigmoidFwdOp** | test_hardsigmoid_manifest_bench[mbv3-se-gate-float16] | 0.0020 | 0.0014 | 68.2% | torch-compile |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-bfloat16] | 0.2048 | 0.1400 | 68.4% | fla |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[moe-prefill-b128-per-tensor-float8_e4m3fn] | 0.9007 | 0.6237 | 69.2% | flashinfer-bmm-fp8 |
| 🔴 | **GroupNormFwdOp** | test_group_norm_no_affine_bench[tail-spatial-g16-float16] | 0.0052 | 0.0036 | 69.3% | flaggems |
| 🔴 | **FusedAddRMSNormFwdOp** | test_fused_add_rms_norm_bench[llama-405b-decode-bfloat16] | 0.0062 | 0.0043 | 69.6% | flashinfer |
| 🔴 | **SiluFwdOp** | test_silu_manifest_bench[llama-8b-ffn-prefill-float16] | 0.0505 | 0.0355 | 70.3% | torch-compile |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s3584-float16] | 0.7497 | 0.5276 | 70.4% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s3584-bfloat16] | 0.7507 | 0.5295 | 70.5% | fa3 |
| 🔴 | **LogicalAndFwdOp** | test_logical_bench[logical_and-1024x4096-float16-LogicalAndFwdOp-logical_and] | 0.0079 | 0.0056 | 70.6% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-bfloat16] | 0.3114 | 0.2204 | 70.8% | fla |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-softcap50-float16] | 0.1764 | 0.1252 | 71.0% | flashinfer |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s7168-bfloat16] | 2.8501 | 2.0260 | 71.1% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s7168-float16] | 2.8449 | 2.0237 | 71.1% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-float16] | 0.8313 | 0.5925 | 71.3% | fa3 |
| 🔴 | **LogicalOrFwdOp** | test_logical_bench[logical_or-1024x4096-float16-LogicalOrFwdOp-logical_or] | 0.0079 | 0.0057 | 71.4% | torch |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s16k-h4-d64-float16] | 1.5146 | 1.0817 | 71.4% | fla |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-float16] | 0.0984 | 0.0703 | 71.4% | fla |
| 🔴 | **SigmoidFwdOp** | test_sigmoid_manifest_bench[elementwise-256M-bfloat16] | 0.3678 | 0.2634 | 71.6% | torch-compile |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.8092 | 0.5802 | 71.7% | fa3 |
| 🔴 | **IsinfFwdOp** | test_isinf_bench[elementwise-256M-float16] | 0.2762 | 0.1988 | 72.0% | torch-compile |
| 🔴 | **IsfiniteFwdOp** | test_isfinite_bench[elementwise-256M-bfloat16] | 0.2731 | 0.1966 | 72.0% | torch-compile |
| 🔴 | **MaxPool2dFwdOp** | test_max_pool2d_bench[resnet-stem-float16] | 0.0472 | 0.0340 | 72.0% | torch-compile |
| 🔴 | **IsfiniteFwdOp** | test_isfinite_bench[elementwise-256M-float16] | 0.2731 | 0.1968 | 72.1% | torch-compile |
| 🔴 | **MaxPool2dFwdOp** | test_max_pool2d_bench[resnet-stem-bfloat16] | 0.0471 | 0.0340 | 72.2% | torch-compile |
| 🔴 | **IsnanFwdOp** | test_isnan_bench[elementwise-256M-float16] | 0.2731 | 0.1972 | 72.2% | torch-compile |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-float16] | 0.1487 | 0.1076 | 72.4% | fla |
| 🔴 | **GroupNormFwdOp** | test_group_norm_no_affine_bench[wider-channel-g32-float16] | 0.0048 | 0.0035 | 72.4% | flaggems |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-float16] | 0.0569 | 0.0413 | 72.7% | flashinfer |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0567 | 0.0412 | 72.7% | flashinfer |
| 🔴 | **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[nondiv-7x7-bfloat16] | 0.0158 | 0.0115 | 72.7% | torch-ref |
| 🔴 | **IsinfFwdOp** | test_isinf_bench[elementwise-256M-bfloat16] | 0.2753 | 0.2001 | 72.7% | torch-compile |
| 🔴 | **IsnanFwdOp** | test_isnan_bench[elementwise-256M-bfloat16] | 0.2730 | 0.1985 | 72.7% | torch-compile |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float32-SiluAndMulFwdKernel-direct] | 0.0200 | 0.0146 | 72.8% | torch-compile |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-2k-bfloat16] | 0.2813 | 0.2051 | 72.9% | torch-cublas |
| 🔴 | **SumFwdOp** | test_sum_bench[long-seq-reduce-bfloat16] | 0.0052 | 0.0038 | 73.0% | flaggems |
| 🔴 | **MeanFwdOp** | test_mean_bench[long-seq-reduce-bfloat16] | 0.0052 | 0.0038 | 73.0% | flaggems |
| 🔴 | **HardsigmoidFwdOp** | test_hardsigmoid_manifest_bench[mbv3-se-gate-deep-float16] | 0.0020 | 0.0015 | 73.0% | torch |
| 🔴 | **LogicalOrFwdOp** | test_logical_or_manifest_bench[cnn-feat-broadcast-float16] | 0.0164 | 0.0120 | 73.2% | torch-compile |
| 🔴 | **IsfiniteFwdOp** | test_isfinite_bench[elementwise-16M-float16] | 0.0205 | 0.0150 | 73.3% | torch-compile |
| 🔴 | **IsinfFwdOp** | test_isinf_bench[elementwise-16M-float16] | 0.0206 | 0.0151 | 73.5% | torch-compile |
| 🔴 | **IsfiniteFwdOp** | test_isfinite_bench[elementwise-16M-bfloat16] | 0.0204 | 0.0150 | 73.5% | torch-compile |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[alexnet-ceil-bfloat16] | 0.0237 | 0.0174 | 73.5% | torch-compile |
| 🔴 | **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[sincnet-speaker-local-float16] | 0.0218 | 0.0160 | 73.7% | torch-compile |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-2k-float16] | 0.2835 | 0.2089 | 73.7% | torch-cublas |
| 🔴 | **IsnanFwdOp** | test_isnan_bench[elementwise-16M-float16] | 0.0204 | 0.0151 | 73.7% | torch-compile |
| 🔴 | **SigmoidFwdOp** | test_sigmoid_manifest_bench[elementwise-16M-bfloat16] | 0.0253 | 0.0187 | 73.8% | torch-compile |
| 🔴 | **IsinfFwdOp** | test_isinf_bench[elementwise-16M-bfloat16] | 0.0206 | 0.0152 | 73.9% | torch-compile |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-float16] | 0.0932 | 0.0690 | 74.0% | flashinfer |
| 🔴 | **IsnanFwdOp** | test_isnan_bench[elementwise-16M-bfloat16] | 0.0205 | 0.0151 | 74.0% | torch-compile |
| 🔴 | **LogicalOrFwdOp** | test_logical_or_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0164 | 0.0121 | 74.0% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-bfloat16] | 0.6107 | 0.4527 | 74.1% | fla |
| 🔴 | **BmmFwdOp** | test_bmm_bench[moe-prefill-b128-bfloat16] | 0.2896 | 0.2151 | 74.3% | torch-cublas |
| 🔴 | **LtFwdOp** | test_lt_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0118 | 74.3% | torch-compile |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-bfloat16] | 0.0931 | 0.0692 | 74.4% | flashinfer |
| 🔴 | **GeFwdOp** | test_ge_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0118 | 74.5% | torch-compile |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[alexnet-ceil-float16] | 0.0237 | 0.0177 | 74.5% | torch-compile |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s16k-h4-d64-bfloat16] | 1.4497 | 1.0806 | 74.5% | fla |
| 🔴 | **LeFwdOp** | test_le_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0119 | 74.7% | torch-compile |
| 🔴 | **NeFwdOp** | test_ne_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0119 | 74.7% | torch-compile |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s8k-h4-d64-float16] | 0.7449 | 0.5566 | 74.7% | fla |
| 🔴 | **LeFwdOp** | test_le_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0119 | 74.9% | torch-compile |
| 🔴 | **GtFwdOp** | test_gt_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0119 | 74.9% | torch-compile |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b4-4k-bfloat16] | 1.0377 | 0.7778 | 75.0% | torch-cublas |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-bfloat16] | 0.1444 | 0.1082 | 75.0% | fla |
| 🔴 | **EqFwdOp** | test_eq_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0120 | 75.0% | torch-compile |
| 🔴 | **NeFwdOp** | test_ne_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0119 | 75.0% | torch-compile |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-float16] | 0.1669 | 0.1252 | 75.0% | flashinfer |
| 🔴 | **EqFwdOp** | test_eq_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0119 | 75.0% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-float16] | 0.6179 | 0.4649 | 75.2% | fla |
| 🔴 | **GtFwdOp** | test_gt_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0120 | 75.2% | torch-compile |
| 🔴 | **Conv2dFwdOp** | test_conv2d_bench[highres-3x3-s1-bias-float16] | 0.1050 | 0.0790 | 75.3% | torch-compile |
| 🔴 | **Conv2dFwdOp** | test_conv2d_bench[highres-3x3-s1-float16] | 0.1047 | 0.0788 | 75.3% | torch-compile |
| 🔴 | **LogicalAndFwdOp** | test_logical_and_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0120 | 75.5% | torch-compile |
| 🔴 | **RopeNonNeoxFwdOp** | test_rope_non_neox_bench[non-neox-2d-b2-s2k-h32-d128-bfloat16] | 0.0252 | 0.0190 | 75.5% | torch-compile |
| 🔴 | **Conv3dFwdOp** | test_conv3d_bench[video-stage-downsample-k3-s2-float16] | 0.0349 | 0.0264 | 75.8% | torch |
| 🔴 | **GeFwdOp** | test_ge_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0120 | 75.8% | torch-compile |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-1k-bfloat16] | 0.0408 | 0.0310 | 76.0% | torch-cublas |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s4k-h4-d64-bfloat16] | 0.1564 | 0.1191 | 76.2% | fla |
| 🔴 | **LogicalAndFwdOp** | test_logical_and_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0122 | 76.3% | torch-compile |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[attn-weights-4k-float16] | 0.0113 | 0.0086 | 76.4% | flaggems |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[attn-weights-4k-bfloat16] | 0.0113 | 0.0086 | 76.5% | flaggems |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-1k-float16] | 0.0409 | 0.0313 | 76.6% | torch-cublas |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s8k-h4-d64-bfloat16] | 0.7267 | 0.5574 | 76.7% | fla |
| 🔴 | **LtFwdOp** | test_lt_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0122 | 76.8% | torch-compile |
| 🔴 | **LogSumExpFwdOp** | test_logsumexp_bench[lm-head-logits-float16] | 0.0141 | 0.0108 | 76.9% | torch-compile |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.6687 | 0.5169 | 77.3% | flashinfer |
| 🔴 | **DeltaNetFwdOp** | test_deltanet_vs_fla_fwd[dn-b2-s16k-h4-d64-float16] | 0.4728 | 0.3656 | 77.3% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.3493 | 0.2702 | 77.3% | fa3 |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[attn-weights-4k-float32] | 0.0143 | 0.0111 | 77.4% | flaggems |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-float16] | 0.3515 | 0.2721 | 77.4% | fa3 |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-float16] | 0.0866 | 0.0672 | 77.6% | fla |
| 🔴 | **Conv2dFwdOp** | test_conv2d_bench[classifier-1x1-bias-float16] | 0.0095 | 0.0074 | 77.8% | torch-compile |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-bfloat16] | 0.0866 | 0.0674 | 77.9% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-float16] | 0.6677 | 0.5204 | 77.9% | flashinfer |
| 🔴 | **GroupedQueryAttentionSlidingWindowFwdOp** | test_gqa_sliding_window_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.1511 | 0.1179 | 78.0% | fa3 |
| 🔴 | **GatedDeltaNetPrefillBHTDFwdOp** | test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-float16] | 0.2512 | 0.1960 | 78.0% | fla |
| 🔴 | **DeltaNetFwdOp** | test_deltanet_vs_fla_fwd[dn-b2-s16k-h4-d64-bfloat16] | 0.4737 | 0.3699 | 78.1% | fla |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s4k-h4-d64-float16] | 0.3691 | 0.2883 | 78.1% | fla |
| 🔴 | **GatedDeltaNetPrefillBHTDFwdOp** | test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-bfloat16] | 0.2526 | 0.1977 | 78.3% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowFwdOp** | test_gqa_sliding_window_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.1513 | 0.1189 | 78.6% | fa3 |
| 🔴 | **LogSumExpFwdOp** | test_logsumexp_bench[3d-multidim-reduce-float16] | 0.0126 | 0.0100 | 78.7% | torch-compile |
| 🔴 | **Conv2dFwdOp** | test_conv2d_bench[classifier-1x1-float16] | 0.0092 | 0.0072 | 78.8% | torch-compile |
| 🔴 | **GroupedQueryAttentionSlidingWindowFwdOp** | test_gqa_sliding_window_fwd_bench[llama-70b-long-w1024-float16] | 0.1528 | 0.1204 | 78.8% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowFwdOp** | test_gqa_sliding_window_fwd_bench[llama-8b-long-w1024-float16] | 0.1530 | 0.1206 | 78.8% | fa3 |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[gla-bwd-b2-s4k-h4-d64-bfloat16] | 0.3650 | 0.2878 | 78.8% | fla |
| 🔴 | **grouped_gemm_nn** | test_grouped_gemm_bench[nn-batch16-m4096-n4096-k4096-float16] | 0.3409 | 0.2691 | 78.9% | torch |
| 🔴 | **DivFwdOp** | test_div_manifest_bench[cnn-feat-broadcast-float16] | 0.0187 | 0.0148 | 79.1% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-float16] | 0.3128 | 0.2477 | 79.2% | fla |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-large-bfloat16] | 0.0716 | 0.0568 | 79.4% | torch-compile |
| 🔴 | **FloorDivideFwdOp** | test_floor_divide_manifest_bench[cnn-feat-broadcast-float16] | 0.0199 | 0.0158 | 79.4% | torch-compile |
| 🔴 | **Conv3dFwdOp** | test_conv3d_bench[video-stage-downsample-k3-s2-bias-float16] | 0.0353 | 0.0281 | 79.5% | torch-compile |
| 🔴 | **FloorDivideFwdOp** | test_floor_divide_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0200 | 0.0159 | 79.5% | torch-compile |
| 🔴 | **LogicalNotFwdOp** | test_logical_not_bench[elementwise-16M-float16] | 0.0188 | 0.0150 | 79.9% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s4k-h4-d64-float16] | 0.1568 | 0.1254 | 79.9% | fla |

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
| 🔵 | AbsFwdOp | test_abs_bench[elementwise-16M-bfloat16] | 0.0179 | 0.94 | 3.75 | torch 100.4%, torch-compile 100.2% | - |
| 🟡 | AbsFwdOp | test_abs_bench[elementwise-16M-float32] | 0.0341 | 0.49 | 3.94 | torch 99.8%, torch-compile 99.6% | - |
| 🟡 | AbsFwdOp | test_abs_bench[elementwise-256M-float16] | 0.2519 | 1.07 | 4.26 | torch 99.1%, torch-compile 99.3% | - |
| 🟡 | AbsFwdOp | test_abs_bench[elementwise-256M-bfloat16] | 0.2506 | 1.07 | 4.28 | torch 99.6%, torch-compile 99.8% | - |
| 🔵 | AdaLayerNormFwdOp | test_ada_layer_norm_bench[dit-xl-2-float16] | 0.0052 | 1.12 | 1.80 | torch-ref 230.5%, torch-compile 145.1% | - |
| 🔵 | AdaLayerNormFwdOp | test_ada_layer_norm_bench[dit-xl-2-bfloat16] | 0.0053 | 1.10 | 1.77 | torch-ref 226.3%, torch-compile 146.1% | - |
| 🔵 | AdaLayerNormFwdOp | test_ada_layer_norm_bench[llama-8b-prefill-float16] | 0.0198 | 2.12 | 3.39 | torch-ref 209.5%, torch-compile 129.1% | - |
| 🔵 | AdaLayerNormFwdOp | test_ada_layer_norm_bench[llama-8b-prefill-bfloat16] | 0.0199 | 2.11 | 3.38 | torch-ref 210.3%, torch-compile 133.8% | - |
| 🔵 | AdaLayerNormFwdOp | test_ada_layer_norm_bench[llama-8b-decode-bfloat16] | 0.0027 | 0.01 | 0.01 | torch-ref 390.3%, torch-compile 113.9% | - |
| 🔵 | AdaLayerNormZeroFwdOp | test_ada_layer_norm_zero_bench[dit-xl-2-float16] | 0.0062 | 1.14 | 1.90 | torch-ref 237.6%, torch-compile 125.3% | - |
| 🔵 | AdaLayerNormZeroFwdOp | test_ada_layer_norm_zero_bench[dit-xl-2-bfloat16] | 0.0062 | 1.14 | 1.90 | torch-ref 238.1%, torch-compile 130.9% | - |
| 🔵 | AdaLayerNormZeroFwdOp | test_ada_layer_norm_zero_bench[llama-8b-prefill-float16] | 0.0247 | 2.03 | 3.39 | torch-ref 215.3%, torch-compile 110.6% | - |
| 🔵 | AdaLayerNormZeroFwdOp | test_ada_layer_norm_zero_bench[llama-8b-prefill-bfloat16] | 0.0247 | 2.04 | 3.40 | torch-ref 217.0%, torch-compile 114.1% | - |
| 🔵 | AdaLayerNormZeroFwdOp | test_ada_layer_norm_zero_bench[llama-8b-decode-bfloat16] | 0.0028 | 0.01 | 0.01 | torch-ref 410.1%, torch-compile 112.4% | - |
| 🔵 | AdaptiveAvgPool2dFwdOp | test_adaptive_avg_pool2d_bench[resnet-global-float16] | 0.0030 | 0.27 | 0.55 | torch-ref 247.3%, torch-compile 124.7% | - |
| 🟢 | AdaptiveAvgPool2dFwdOp | test_adaptive_avg_pool2d_bench[spp-6x6-float16] | 0.0054 | 0.17 | 0.30 | torch-ref 197.0%, torch-compile 197.0% | - |
| 🔵 | AdaptiveAvgPool2dFwdOp | test_adaptive_avg_pool2d_bench[nondiv-7x7-bfloat16] | 0.0066 | 0.07 | 0.12 | torch-ref 138.8%, torch-compile 138.8% | - |
| 🔵 | AdaptiveMaxPool2dFwdOp | test_adaptive_max_pool2d_bench[global-1x1-float16] | 0.0029 | 0.27 | 0.56 | torch-ref 1528.8%, torch-compile 128.3% | - |
| 🟢 | AdaptiveMaxPool2dFwdOp | test_adaptive_max_pool2d_bench[spp-6x6-float16] | 0.0060 | 0.15 | 0.27 | torch-ref 237.2%, torch-compile 237.2% | - |
| 🟢 | AdaptiveMaxPool2dFwdOp | test_adaptive_max_pool2d_bench[nondiv-7x7-bfloat16] | 0.0065 | 0.08 | 0.13 | torch-ref 176.8%, torch-compile 176.8% | - |
| 🔴 | AdaptiveMaxPool2dIndicesFwdOp | test_adaptive_max_pool2d_indices_bench[global-1x1-float16] | 0.0133 | 0.06 | 0.13 | torch-ref 338.3%, torch-compile 61.7% | - |
| 🟡 | AdaptiveMaxPool2dIndicesFwdOp | test_adaptive_max_pool2d_indices_bench[spp-6x6-float16] | 0.0154 | 0.06 | 0.11 | torch-ref 92.8%, torch-compile 92.8% | - |
| 🔴 | AdaptiveMaxPool2dIndicesFwdOp | test_adaptive_max_pool2d_indices_bench[nondiv-7x7-bfloat16] | 0.0158 | 0.03 | 0.05 | torch-ref 72.7%, torch-compile 72.7% | - |
| 🟡 | AddFwdOp | test_add_manifest_bench[hidden-state-prefill-float16] | 0.0147 | 1.14 | 3.42 | torch 100.9%, torch-compile 100.0% | - |
| 🔵 | AddFwdOp | test_add_manifest_bench[hidden-state-prefill-bfloat16] | 0.0147 | 1.14 | 3.43 | torch 101.5%, torch-compile 100.2% | - |
| 🟡 | AddFwdOp | test_add_manifest_bench[hidden-state-prefill-float32] | 0.0265 | 0.63 | 3.79 | torch 99.9%, torch-compile 99.5% | - |
| 🟡 | AddFwdOp | test_add_manifest_bench[cnn-feat-broadcast-float16] | 0.0166 | 1.55 | 3.09 | torch 275.5%, torch-compile 86.9% | - |
| 🟡 | AddFwdOp | test_add_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0166 | 1.55 | 3.09 | torch 279.2%, torch-compile 86.5% | - |
| 🟡 | AddFwdOp | test_add_manifest_bench[cnn-feat-broadcast-float32] | 0.0267 | 0.96 | 3.85 | torch 185.1%, torch-compile 99.5% | - |
| 🔵 | AlibiFwdOp | test_alibi_bench[llama-prefill-2k-float16] | 0.0646 | 6.24 | 4.16 | torch-ref 916.7%, torch-compile 133.8% | - |
| 🔵 | AlibiFwdOp | test_alibi_bench[llama-prefill-2k-bfloat16] | 0.0647 | 6.23 | 4.15 | torch-ref 915.4%, torch-compile 133.7% | - |
| 🔵 | AlibiFwdOp | test_alibi_bench[llama-prefill-4k-float16] | 0.2855 | 5.64 | 3.76 | torch-ref 913.9%, torch-compile 119.6% | - |
| 🔵 | AlibiFwdOp | test_alibi_bench[llama-prefill-4k-bfloat16] | 0.2844 | 5.66 | 3.78 | torch-ref 917.2%, torch-compile 119.9% | - |
| 🔴 | AllFwdOp | test_all_bench[mask-validation-4k-bool] | 0.0074 | 0.02 | 0.02 | flaggems 25.4%, torch 234.1%, torch-compile 24.3% | - |
| 🔴 | AllFwdOp | test_all_bench[mask-validation-32k-bool] | 0.0106 | 0.10 | 0.10 | flaggems 61.0%, torch 96.5%, torch-compile 32.9% | - |
| 🔴 | AllFwdOp | test_all_bench[3d-multidim-reduce-bool] | 0.0216 | 0.10 | 0.10 | flaggems 54.6%, torch 47.9%, torch-compile 19.1% | - |
| 🟡 | AmaxFwdOp | test_amax_bench[hidden-state-reduce-float16] | 0.0086 | 0.98 | 1.96 | flaggems 89.5%, torch 223.9%, torch-compile 117.9% | - |
| 🟡 | AmaxFwdOp | test_amax_bench[hidden-state-reduce-bfloat16] | 0.0088 | 0.96 | 1.91 | flaggems 89.4%, torch 220.1%, torch-compile 115.3% | - |
| 🟡 | AmaxFwdOp | test_amax_bench[long-seq-reduce-bfloat16] | 0.0052 | 0.40 | 0.80 | flaggems 259.5%, torch 215.9%, torch-compile 89.0% | - |
| 🔴 | AmaxFwdOp | test_amax_bench[3d-multidim-reduce-float16] | 0.0115 | 0.18 | 0.37 | flaggems 108.4%, torch 112.8%, torch-compile 45.2% | - |
| 🔵 | AminFwdOp | test_amin_bench[hidden-state-reduce-float16] | 0.0086 | 0.98 | 1.96 | torch 224.3%, torch-compile 118.3% | - |
| 🔵 | AminFwdOp | test_amin_bench[hidden-state-reduce-bfloat16] | 0.0087 | 0.96 | 1.92 | torch 221.1%, torch-compile 115.8% | - |
| 🟡 | AminFwdOp | test_amin_bench[long-seq-reduce-bfloat16] | 0.0052 | 0.40 | 0.80 | torch 215.2%, torch-compile 90.3% | - |
| 🔴 | AminFwdOp | test_amin_bench[3d-multidim-reduce-float16] | 0.0115 | 0.18 | 0.37 | torch 112.5%, torch-compile 42.6% | - |
| 🔴 | AnyFwdOp | test_any_bench[mask-validation-4k-bool] | 0.0072 | 0.02 | 0.02 | flaggems 26.3%, torch 247.8%, torch-compile 24.1% | - |
| 🔴 | AnyFwdOp | test_any_bench[mask-validation-32k-bool] | 0.0106 | 0.10 | 0.10 | flaggems 60.7%, torch 99.1%, torch-compile 31.1% | - |
| 🔴 | AnyFwdOp | test_any_bench[3d-multidim-reduce-bool] | 0.0214 | 0.10 | 0.10 | flaggems 55.2%, torch 88.3%, torch-compile 18.7% | - |
| 🟢 | ArgmaxFwdOp | test_argmax_bench[lm-head-argmax-float16] | 0.0151 | 0.03 | 0.05 | flaggems 198.3%, torch 232.6%, torch-compile 188.6% | - |
| 🟢 | ArgmaxFwdOp | test_argmax_bench[lm-head-argmax-bfloat16] | 0.0155 | 0.03 | 0.05 | flaggems 183.8%, torch 232.7%, torch-compile 188.0% | - |
| 🔴 | ArgmaxFwdOp | test_argmax_bench[hidden-state-argmax-float16] | 0.0239 | 0.35 | 0.70 | flaggems 50.9%, torch 102.8%, torch-compile 79.4% | - |
| 🔴 | ArgmaxFwdOp | test_argmax_bench[hidden-state-argmax-bfloat16] | 0.0239 | 0.35 | 0.70 | flaggems 48.7%, torch 104.0%, torch-compile 80.9% | - |
| 🔴 | ArgmaxFwdOp | test_argmax_bench[3d-non-last-axis-argmax-float16] | 0.0056 | 0.37 | 1.49 | flaggems 67.6%, torch 198.3%, torch-compile 81.2% | - |
| 🟢 | ArgminFwdOp | test_argmin_bench[lm-head-argmin-float16] | 0.0152 | 0.03 | 0.05 | flaggems 759.4%, torch 231.2%, torch-compile 187.8% | - |
| 🟢 | ArgminFwdOp | test_argmin_bench[lm-head-argmin-bfloat16] | 0.0154 | 0.03 | 0.05 | flaggems 665.8%, torch 232.6%, torch-compile 188.6% | - |
| 🔴 | ArgminFwdOp | test_argmin_bench[hidden-state-argmin-float16] | 0.0239 | 0.35 | 0.70 | flaggems 41.3%, torch 102.8%, torch-compile 79.4% | - |
| 🔴 | ArgminFwdOp | test_argmin_bench[hidden-state-argmin-bfloat16] | 0.0240 | 0.35 | 0.70 | flaggems 41.2%, torch 103.6%, torch-compile 80.7% | - |
| 🔴 | AvgPool1dFwdOp | test_avg_pool1d_bench[audio-downsample-float16] | 0.0062 | 0.51 | 1.02 | torch-ref 248.2%, torch-compile 67.9% | - |
| 🟡 | AvgPool1dFwdOp | test_avg_pool1d_bench[long-temporal-float16] | 0.0213 | 0.96 | 1.92 | torch-ref 278.9%, torch-compile 80.5% | - |
| 🔴 | AvgPool1dFwdOp | test_avg_pool1d_bench[ceil-bfloat16] | 0.0035 | 0.30 | 0.46 | torch-ref 153.7%, torch-compile 66.7% | - |
| 🔵 | AvgPool2dFwdOp | test_avg_pool2d_bench[vision-3x3-s2-float16] | 0.0040 | 0.90 | 1.00 | flaggems 165.6%, torch-ref 227.2%, torch-compile 102.4% | - |
| 🟢 | AvgPool2dFwdOp | test_avg_pool2d_bench[vision-5x5-s2-float16] | 0.0040 | 1.24 | 0.50 | flaggems 179.4%, torch-ref 243.7%, torch-compile 511.1% | - |
| 🔵 | AvgPool2dFwdOp | test_avg_pool2d_bench[ceil-divisor-bfloat16] | 0.0031 | 1.12 | 0.72 | flaggems 184.7%, torch-ref 243.9%, torch-compile 124.5% | - |
| 🔵 | AvgPool3dFwdOp | test_avg_pool3d_bench[video-2x2x2-float16] | 0.0037 | 0.44 | 0.98 | cudnn 160.0%, torch-ref 269.6%, torch-compile 131.3% | - |
| 🟡 | AvgPool3dFwdOp | test_avg_pool3d_bench[ceil-video-float16] | 0.0044 | 0.59 | 0.43 | cudnn 127.7%, torch-ref 259.5%, torch-compile 92.0% | - |
| 🟡 | AvgPool3dFwdOp | test_avg_pool3d_bench[divisor-bfloat16] | 0.0023 | 0.15 | 0.21 | torch-ref 222.5%, torch-compile 83.1% | - |
| 🟢 | BatchNormBwdOp | test_batch_norm_bwd_bench[resnet50-fc-float16] | 0.0070 | 0.00 | 0.00 | torch-autograd 332.3%, torch-native-batch-norm 179.1% | - |
| 🔵 | BatchNormBwdOp | test_batch_norm_bwd_bench[resnet50-stage1-float16] | 0.0148 | 0.28 | 0.21 | torch-autograd 186.3%, torch-native-batch-norm 127.9% | - |
| 🔵 | BatchNormBwdOp | test_batch_norm_bwd_bench[resnet50-stage2-float16] | 0.0141 | 0.30 | 0.22 | torch-autograd 169.8%, torch-native-batch-norm 108.4% | - |
| 🔵 | BatchNormBwdOp | test_batch_norm_bwd_bench[resnet50-stage3-float16] | 0.0171 | 0.38 | 0.28 | torch-autograd 150.1%, torch-native-batch-norm 103.8% | - |
| 🟢 | BatchNormBwdOp | test_batch_norm_bwd_bench[large-spatial-float16] | 6.8754 | 0.62 | 0.47 | torch-autograd 188.6%, torch-native-batch-norm 171.6% | - |
| 🔴 | BatchNormFwdOp | test_batch_norm_fwd_bench[resnet50-fc-float16] | 0.0061 | 0.00 | 0.00 | flaggems 90.5%, torch-cudnn 185.8%, torch-compile 36.8% | - |
| 🔴 | BatchNormFwdOp | test_batch_norm_fwd_bench[resnet50-stage1-float16] | 0.0109 | 0.48 | 0.19 | flaggems 94.4%, torch-cudnn 103.8%, torch-compile 37.7% | - |
| 🔴 | BatchNormFwdOp | test_batch_norm_fwd_bench[resnet50-stage2-float16] | 0.0107 | 0.49 | 0.20 | flaggems 83.5%, torch-cudnn 97.0%, torch-compile 32.6% | - |
| 🔴 | BatchNormFwdOp | test_batch_norm_fwd_bench[resnet50-stage3-float16] | 0.0129 | 0.62 | 0.25 | flaggems 85.1%, torch-cudnn 86.6%, torch-compile 35.6% | - |
| 🔴 | BatchNormFwdOp | test_batch_norm_fwd_bench[large-spatial-float16] | 4.3427 | 1.24 | 0.49 | flaggems 89.7%, torch-cudnn 104.4%, torch-compile 23.4% | - |
| 🟡 | BitwiseAndFwdOp | test_bitwise_bench[bitwise_and-1024x4096-BitwiseAndFwdOp-bitwise_and] | 0.0151 | 0.28 | 3.34 | torch 97.7%, torch-compile 97.7% | - |
| 🟡 | BitwiseAndFwdOp | test_bitwise_bench[bitwise_and-1024x10240-BitwiseAndFwdOp-bitwise_and] | 0.0326 | 0.32 | 3.86 | torch 98.2%, torch-compile 98.0% | - |
| 🔵 | BitwiseAndFwdOp | test_bitwise_and_manifest_bench[hidden-state-prefill-bool] | 0.0084 | 1.00 | 3.01 | torch 120.7%, torch-compile 107.1% | - |
| 🟡 | BitwiseAndFwdOp | test_bitwise_and_manifest_bench[hidden-state-prefill-int32] | 0.0269 | 0.31 | 3.74 | torch 97.7%, torch-compile 97.5% | - |
| 🟡 | BitwiseAndFwdOp | test_bitwise_and_manifest_bench[hidden-state-prefill-int64] | 0.0498 | 0.17 | 4.04 | torch 99.9%, torch-compile 98.9% | - |
| 🔵 | BitwiseAndFwdOp | test_bitwise_and_manifest_bench[cnn-feat-broadcast-bool] | 0.0081 | 1.59 | 3.17 | torch 558.1%, torch-compile 123.7% | - |
| 🟡 | BitwiseAndFwdOp | test_bitwise_and_manifest_bench[cnn-feat-broadcast-int32] | 0.0275 | 0.47 | 3.74 | torch 179.8%, torch-compile 96.5% | - |
| 🟡 | BitwiseAndFwdOp | test_bitwise_and_manifest_bench[cnn-feat-broadcast-int64] | 0.0527 | 0.24 | 3.90 | torch 110.7%, torch-compile 94.4% | - |
| 🔴 | BitwiseNotFwdOp | test_bitwise_not_bench[elementwise-16M-int32] | 0.0610 | 0.28 | 2.20 | torch 55.8%, torch-compile 55.6% | - |
| 🟡 | BitwiseNotFwdOp | test_bitwise_not_bench[elementwise-16M-int64] | 0.0745 | 0.23 | 3.60 | torch 91.3%, torch-compile 86.9% | - |
| 🔴 | BitwiseNotFwdOp | test_bitwise_not_bench[elementwise-256M-int32] | 0.9380 | 0.29 | 2.29 | torch 53.8%, torch-compile 53.8% | - |
| 🟡 | BitwiseOrFwdOp | test_bitwise_bench[bitwise_or-1024x4096-BitwiseOrFwdOp-bitwise_or] | 0.0149 | 0.28 | 3.37 | torch 97.4%, torch-compile 97.2% | - |
| 🔵 | BitwiseOrFwdOp | test_bitwise_or_manifest_bench[hidden-state-prefill-bool] | 0.0082 | 1.03 | 3.08 | torch 107.8%, torch-compile 104.3% | - |
| 🟡 | BitwiseOrFwdOp | test_bitwise_or_manifest_bench[hidden-state-prefill-int32] | 0.0271 | 0.31 | 3.72 | torch 97.8%, torch-compile 97.9% | - |
| 🟡 | BitwiseOrFwdOp | test_bitwise_or_manifest_bench[hidden-state-prefill-int64] | 0.0499 | 0.17 | 4.04 | torch 99.6%, torch-compile 98.5% | - |
| 🔵 | BitwiseOrFwdOp | test_bitwise_or_manifest_bench[cnn-feat-broadcast-bool] | 0.0081 | 1.59 | 3.17 | torch 546.7%, torch-compile 126.1% | - |
| 🟡 | BitwiseOrFwdOp | test_bitwise_or_manifest_bench[cnn-feat-broadcast-int32] | 0.0275 | 0.47 | 3.74 | torch 179.7%, torch-compile 96.7% | - |
| 🟡 | BitwiseOrFwdOp | test_bitwise_or_manifest_bench[cnn-feat-broadcast-int64] | 0.0524 | 0.25 | 3.92 | torch 111.3%, torch-compile 96.0% | - |
| 🟡 | BitwiseXorFwdOp | test_bitwise_bench[bitwise_xor-1024x4096-BitwiseXorFwdOp-bitwise_xor] | 0.0152 | 0.28 | 3.32 | torch 97.5%, torch-compile 100.4% | - |
| 🔵 | BitwiseXorFwdOp | test_bitwise_xor_manifest_bench[hidden-state-prefill-bool] | 0.0082 | 1.03 | 3.08 | torch 121.7%, torch-compile 108.0% | - |
| 🟡 | BitwiseXorFwdOp | test_bitwise_xor_manifest_bench[hidden-state-prefill-int32] | 0.0268 | 0.31 | 3.75 | torch 98.1%, torch-compile 97.7% | - |
| 🟡 | BitwiseXorFwdOp | test_bitwise_xor_manifest_bench[hidden-state-prefill-int64] | 0.0499 | 0.17 | 4.04 | torch 99.9%, torch-compile 99.0% | - |
| 🔵 | BitwiseXorFwdOp | test_bitwise_xor_manifest_bench[cnn-feat-broadcast-bool] | 0.0081 | 1.59 | 3.19 | torch 560.3%, torch-compile 124.2% | - |
| 🟡 | BitwiseXorFwdOp | test_bitwise_xor_manifest_bench[cnn-feat-broadcast-int32] | 0.0274 | 0.47 | 3.76 | torch 180.7%, torch-compile 96.5% | - |
| 🟡 | BitwiseXorFwdOp | test_bitwise_xor_manifest_bench[cnn-feat-broadcast-int64] | 0.0525 | 0.24 | 3.91 | torch 110.5%, torch-compile 95.3% | - |
| 🟡 | BmmFp8KNFwdOp | test_bmm_fp8_kn_bench[square-b4-1k-per-tensor-float8_e4m3fn] | 0.0390 | 220.39 | 0.43 | torch-fp32-ref 753.5%, flashinfer-bmm-fp8 91.1% | - |
| 🟢 | BmmFp8KNFwdOp | test_bmm_fp8_kn_bench[square-b8-2k-per-tensor-float8_e4m3fn] | 0.3062 | 448.86 | 0.44 | torch-fp32-ref 1325.9%, flashinfer-bmm-fp8 203.4% | - |
| 🔴 | BmmFp8KNFwdOp | test_bmm_fp8_kn_bench[mha-decode-b32-pv-per-tensor-float8_e4m3fn] | 0.0647 | 33.17 | 0.28 | torch-fp32-ref 364.5%, flashinfer-bmm-fp8 38.6% | - |
| 🔴 | BmmFp8KNFwdOp | test_bmm_fp8_kn_bench[mha-decode-b64-qk-per-tensor-float8_e4m3fn] | 0.1154 | 37.22 | 0.45 | torch-fp32-ref 250.1%, flashinfer-bmm-fp8 43.1% | - |
| 🔴 | BmmFp8KNFwdOp | test_bmm_fp8_kn_bench[moe-prefill-b128-per-tensor-float8_e4m3fn] | 0.9007 | 152.59 | 0.37 | torch-fp32-ref 600.0%, flashinfer-bmm-fp8 69.2% | - |
| 🔵 | BmmFp8NKFwdOp | test_bmm_fp8_nk_bench[square-b4-1k-per-tensor-float8_e4m3fn] | 0.0118 | 725.44 | 1.42 | torch-fp32-ref 2479.0%, flashinfer-bmm-fp8 110.3% | - |
| 🔵 | BmmFp8NKFwdOp | test_bmm_fp8_nk_bench[square-b8-2k-per-tensor-float8_e4m3fn] | 0.1200 | 1145.63 | 1.12 | torch-fp32-ref 3391.9%, flashinfer-bmm-fp8 105.0% | - |
| 🔵 | BmmFp8NKFwdOp | test_bmm_fp8_nk_bench[mha-decode-b32-pv-per-tensor-float8_e4m3fn] | 0.0090 | 237.97 | 1.98 | torch-fp32-ref 2620.6%, flashinfer-bmm-fp8 105.7% | - |
| 🔵 | BmmFp8NKFwdOp | test_bmm_fp8_nk_bench[mha-decode-b64-qk-per-tensor-float8_e4m3fn] | 0.0157 | 273.37 | 3.27 | torch-fp32-ref 1832.8%, flashinfer-bmm-fp8 137.7% | - |
| 🔵 | BmmFp8NKFwdOp | test_bmm_fp8_nk_bench[moe-prefill-b128-per-tensor-float8_e4m3fn] | 0.1317 | 1043.22 | 2.55 | torch-fp32-ref 4103.6%, flashinfer-bmm-fp8 104.9% | - |
| 🔵 | BmmFwdOp | test_bmm_bench[small-b8-128-float16] | 0.0027 | 12.48 | 0.29 | flaggems 117.8%, torch-cublas 120.2% | - |
| 🔵 | BmmFwdOp | test_bmm_bench[small-b8-128-bfloat16] | 0.0027 | 12.34 | 0.29 | flaggems 116.5%, torch-cublas 118.8% | - |
| 🔴 | BmmFwdOp | test_bmm_bench[square-b8-1k-float16] | 0.0409 | 419.76 | 1.23 | flaggems 110.2%, torch-cublas 76.6% | - |
| 🔴 | BmmFwdOp | test_bmm_bench[square-b8-1k-bfloat16] | 0.0408 | 420.75 | 1.23 | flaggems 109.6%, torch-cublas 76.0% | - |
| 🟡 | BmmFwdOp | test_bmm_bench[square-b16-512-float16] | 0.0133 | 323.42 | 1.90 | flaggems 114.2%, torch-cublas 91.1% | - |
| 🟡 | BmmFwdOp | test_bmm_bench[square-b16-512-bfloat16] | 0.0133 | 321.88 | 1.89 | flaggems 113.7%, torch-cublas 90.4% | - |
| 🔵 | BmmFwdOp | test_bmm_bench[square-b32-256-float16] | 0.0066 | 162.91 | 1.91 | flaggems 119.9%, torch-cublas 107.3% | - |
| 🔵 | BmmFwdOp | test_bmm_bench[square-b32-256-bfloat16] | 0.0066 | 163.68 | 1.92 | flaggems 120.5%, torch-cublas 107.8% | - |
| 🔴 | BmmFwdOp | test_bmm_bench[square-b4-4k-bfloat16] | 1.0377 | 529.78 | 0.39 | flaggems 93.0%, torch-cublas 75.0% | - |
| 🔴 | BmmFwdOp | test_bmm_bench[square-b8-2k-float16] | 0.2835 | 484.84 | 0.71 | flaggems 97.4%, torch-cublas 73.7% | - |
| 🔴 | BmmFwdOp | test_bmm_bench[square-b8-2k-bfloat16] | 0.2813 | 488.51 | 0.72 | flaggems 97.1%, torch-cublas 72.9% | - |
| 🟡 | BmmFwdOp | test_bmm_bench[mha-decode-b64-qk-float16] | 0.0225 | 191.19 | 3.08 | flaggems 115.8%, torch-cublas 94.4% | - |
| 🟡 | BmmFwdOp | test_bmm_bench[mha-decode-b64-qk-bfloat16] | 0.0225 | 190.65 | 3.07 | flaggems 115.1%, torch-cublas 94.0% | - |
| 🔵 | BmmFwdOp | test_bmm_bench[mha-decode-b64-pv-float16] | 0.0240 | 179.20 | 2.89 | flaggems 169.3%, torch-cublas 101.7% | - |
| 🔵 | BmmFwdOp | test_bmm_bench[mha-decode-b64-pv-bfloat16] | 0.0240 | 178.96 | 2.88 | flaggems 169.7%, torch-cublas 101.5% | - |
| 🔴 | BmmFwdOp | test_bmm_bench[moe-prefill-b128-bfloat16] | 0.2896 | 474.61 | 2.09 | flaggems 102.0%, torch-cublas 74.3% | - |
| 🟢 | CBProducerFwdOp | test_cb_producer_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0072 | 18.72 | 0.59 | torch 528.1% | - |
| 🟢 | CBProducerFwdOp | test_cb_producer_fwd_bench[mamba2-2p7b-b4-s2k-bfloat16] | 0.0119 | 22.61 | 0.71 | torch 447.7% | - |
| 🟡 | CeilFwdOp | test_ceil_bench[elementwise-16M-float16] | 0.0180 | 0.93 | 3.73 | torch 99.8%, torch-compile 99.6% | - |
| 🟡 | CeilFwdOp | test_ceil_bench[elementwise-16M-bfloat16] | 0.0180 | 0.93 | 3.73 | torch 99.9%, torch-compile 99.7% | - |
| 🟡 | CeilFwdOp | test_ceil_bench[elementwise-16M-float32] | 0.0341 | 0.49 | 3.94 | torch 99.8%, torch-compile 99.9% | - |
| 🟡 | CeilFwdOp | test_ceil_bench[elementwise-256M-float16] | 0.2527 | 1.06 | 4.25 | torch 99.0%, torch-compile 99.2% | - |
| 🟡 | CeilFwdOp | test_ceil_bench[elementwise-256M-bfloat16] | 0.2532 | 1.06 | 4.24 | torch 98.9%, torch-compile 98.7% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-float16] | 0.0355 | 0.47 | 3.78 | torch 98.2%, torch-compile 98.8% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-bfloat16] | 0.0355 | 0.47 | 3.79 | torch 98.4%, torch-compile 98.8% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-float32] | 0.0658 | 0.25 | 4.08 | torch 99.5%, torch-compile 99.4% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-256M-float16] | 0.4861 | 0.55 | 4.42 | torch 99.8%, torch-compile 99.8% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-256M-bfloat16] | 0.4855 | 0.55 | 4.42 | torch 99.9%, torch-compile 99.9% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-min-only-float16] | 0.0268 | 0.63 | 3.76 | torch 99.6%, torch-compile 98.4% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-min-only-bfloat16] | 0.0269 | 0.62 | 3.74 | torch 99.6%, torch-compile 98.1% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-min-only-float32] | 0.0498 | 0.34 | 4.04 | torch 100.2%, torch-compile 98.9% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-256M-min-only-float16] | 0.3693 | 0.73 | 4.36 | torch 99.8%, torch-compile 99.9% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-256M-min-only-bfloat16] | 0.3688 | 0.73 | 4.37 | torch 99.7%, torch-compile 99.9% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-max-only-float16] | 0.0266 | 0.63 | 3.79 | torch 99.9%, torch-compile 99.0% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-max-only-bfloat16] | 0.0271 | 0.62 | 3.72 | torch 99.4%, torch-compile 98.2% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-16M-max-only-float32] | 0.0499 | 0.34 | 4.03 | torch 99.7%, torch-compile 99.4% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-256M-max-only-float16] | 0.3690 | 0.73 | 4.36 | torch 99.8%, torch-compile 100.0% | - |
| 🟡 | ClampFwdOp | test_clamp_tensor_bench[elementwise-256M-max-only-bfloat16] | 0.3679 | 0.73 | 4.38 | torch 100.0%, torch-compile 100.2% | - |
| 🔵 | ClampScalarFwdOp | test_clamp_scalar_manifest_bench[elementwise-16M-float16] | 0.0184 | 0.91 | 3.64 | torch 110.1%, torch-compile 100.2% | - |
| 🔵 | ClampScalarFwdOp | test_clamp_scalar_manifest_bench[elementwise-16M-bfloat16] | 0.0184 | 0.91 | 3.64 | torch 103.6%, torch-compile 101.0% | - |
| 🔵 | ClampScalarFwdOp | test_clamp_scalar_manifest_bench[elementwise-16M-float32] | 0.0339 | 0.50 | 3.96 | torch 100.6%, torch-compile 100.5% | - |
| 🔵 | ClampScalarFwdOp | test_clamp_scalar_manifest_bench[elementwise-256M-float16] | 0.2517 | 1.07 | 4.27 | torch 116.0%, torch-compile 100.7% | - |
| 🔵 | ClampScalarFwdOp | test_clamp_scalar_manifest_bench[elementwise-256M-bfloat16] | 0.2520 | 1.07 | 4.26 | torch 109.3%, torch-compile 105.3% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[whisper-large-conv1-float16] | 0.0482 | 38.22 | 0.18 | flaggems 233.0%, torch 118.0%, torch-compile 118.1% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[whisper-large-conv1-bfloat16] | 0.0485 | 37.94 | 0.18 | flaggems 230.9%, torch 116.2%, torch-compile 116.1% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[wav2vec2-layer1-float16] | 0.0067 | 4.92 | 0.50 | flaggems 601.8%, torch 279.8%, torch-compile 279.8% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[wav2vec2-layer1-bfloat16] | 0.0067 | 4.91 | 0.50 | flaggems 602.4%, torch 282.0%, torch-compile 282.0% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[encodec-init-float16] | 0.0036 | 3.03 | 0.45 | flaggems 692.0%, torch 186.5%, torch-compile 187.0% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[encodec-init-bfloat16] | 0.0036 | 3.03 | 0.45 | flaggems 688.3%, torch 186.5%, torch-compile 187.4% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[encodec-deep-float16] | 0.0120 | 32.28 | 0.09 | flaggems 595.9%, torch 141.3%, torch-compile 141.6% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[encodec-deep-bfloat16] | 0.0120 | 32.36 | 0.09 | flaggems 597.1%, torch 141.7%, torch-compile 141.4% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[whisper-large-conv1-bias-float16] | 0.0477 | 38.66 | 0.18 | flaggems 233.9%, torch 145.2%, torch-compile 133.7% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[whisper-large-conv1-bias-bfloat16] | 0.0477 | 38.66 | 0.18 | flaggems 233.7%, torch 145.1%, torch-compile 132.7% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[wav2vec2-layer1-bias-float16] | 0.0069 | 4.99 | 0.48 | flaggems 568.0%, torch 366.1%, torch-compile 325.8% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[wav2vec2-layer1-bias-bfloat16] | 0.0069 | 4.95 | 0.48 | flaggems 564.6%, torch 367.8%, torch-compile 326.8% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[encodec-init-bias-float16] | 0.0036 | 3.21 | 0.44 | flaggems 660.1%, torch 293.7%, torch-compile 240.1% | - |
| 🟢 | Conv1dFwdOp | test_conv1d_bench[encodec-init-bias-bfloat16] | 0.0036 | 3.21 | 0.44 | flaggems 656.2%, torch 297.3%, torch-compile 250.9% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[encodec-deep-bias-float16] | 0.0124 | 31.21 | 0.09 | flaggems 567.0%, torch 164.7%, torch-compile 149.5% | - |
| 🔵 | Conv1dFwdOp | test_conv1d_bench[encodec-deep-bias-bfloat16] | 0.0124 | 31.29 | 0.09 | flaggems 568.4%, torch 163.8%, torch-compile 149.6% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[resnet-3x3-float16] | 0.0130 | 35.50 | 0.13 | flaggems 639.3%, torch 113.5%, torch-compile 88.4% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[resnet-3x3-bfloat16] | 0.0130 | 35.59 | 0.13 | flaggems 640.5%, torch 114.8%, torch-compile 91.1% | - |
| 🟢 | Conv2dFwdOp | test_conv2d_bench[stem-3x3-s2-float16] | 0.0036 | 3.02 | 0.13 | flaggems 364.4%, torch 180.4%, torch-compile 261.7% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[stage-transition-3x3-s2-float16] | 0.0138 | 33.53 | 0.13 | flaggems 859.7%, torch 123.2%, torch-compile 97.4% | - |
| 🔴 | Conv2dFwdOp | test_conv2d_bench[highres-3x3-s1-float16] | 0.1047 | 282.61 | 0.21 | flaggems 701.5%, torch 90.4%, torch-compile 75.3% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[midres-5x5-s1-float16] | 0.0161 | 79.64 | 0.10 | flaggems 1254.9%, torch 121.0%, torch-compile 100.4% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[stage-transition-5x5-s2-float16] | 0.0225 | 57.18 | 0.13 | flaggems 1381.7%, torch 113.4%, torch-compile 98.9% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[stride2-bfloat16] | 0.0111 | 5.21 | 0.05 | flaggems 583.9%, torch 133.7%, torch-compile 109.2% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[resnet-1x1-float16] | 0.0044 | 47.21 | 0.93 | flaggems 1128.4%, torch 96.3%, torch-compile 192.6% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[resnet-1x1-bfloat16] | 0.0044 | 46.88 | 0.92 | flaggems 1124.1%, torch 91.2%, torch-compile 189.1% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[bottleneck-expand-1x1-float16] | 0.0038 | 53.97 | 0.56 | flaggems 748.7%, torch 105.1%, torch-compile 193.7% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[bottleneck-reduce-1x1-float16] | 0.0047 | 43.99 | 0.46 | flaggems 565.1%, torch 92.5%, torch-compile 169.8% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[late-stage-1x1-float16] | 0.0050 | 20.52 | 0.20 | flaggems 307.4%, torch 126.5%, torch-compile 132.9% | - |
| 🔴 | Conv2dFwdOp | test_conv2d_bench[classifier-1x1-float16] | 0.0092 | 11.19 | 0.26 | flaggems 224.8%, torch 98.6%, torch-compile 78.8% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[deeplabv3-aspp-3x3-rate12-float16] | 0.0889 | 108.67 | 0.16 | flaggems 803.9%, torch 133.8%, torch-compile 102.4% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[mobilenetv2-depthwise-float16] | 0.0028 | 0.65 | 0.14 | flaggems 1934.9%, torch 108.5%, torch-compile 197.7% | - |
| 🟢 | Conv2dFwdOp | test_conv2d_bench[resnext-grouped-3x3-float16] | 0.0041 | 3.50 | 0.15 | flaggems 467.0%, torch 461.2%, torch-compile 461.2% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[resnet-3x3-bias-float16] | 0.0133 | 34.85 | 0.13 | flaggems 620.0%, torch 137.8%, torch-compile 88.7% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[resnet-3x3-bias-bfloat16] | 0.0138 | 33.56 | 0.12 | flaggems 596.9%, torch 132.9%, torch-compile 88.6% | - |
| 🟢 | Conv2dFwdOp | test_conv2d_bench[stem-3x3-s2-bias-float16] | 0.0035 | 3.16 | 0.14 | flaggems 352.3%, torch 273.4%, torch-compile 275.2% | - |
| 🟡 | Conv2dFwdOp | test_conv2d_bench[stage-transition-3x3-s2-bias-float16] | 0.0142 | 32.63 | 0.13 | flaggems 829.8%, torch 141.1%, torch-compile 97.1% | - |
| 🔴 | Conv2dFwdOp | test_conv2d_bench[highres-3x3-s1-bias-float16] | 0.1050 | 281.94 | 0.21 | flaggems 696.5%, torch 109.1%, torch-compile 75.3% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[midres-5x5-s1-bias-float16] | 0.0165 | 77.97 | 0.10 | flaggems 1221.0%, torch 138.3%, torch-compile 100.4% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[stage-transition-5x5-s2-bias-float16] | 0.0225 | 57.11 | 0.13 | flaggems 1375.0%, torch 127.6%, torch-compile 100.2% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[stride2-bias-bfloat16] | 0.0116 | 4.98 | 0.05 | flaggems 551.1%, torch 153.4%, torch-compile 106.9% | - |
| 🟢 | Conv2dFwdOp | test_conv2d_bench[resnet-1x1-bias-float16] | 0.0046 | 45.25 | 0.88 | flaggems 1053.6%, torch 254.5%, torch-compile 193.7% | - |
| 🟢 | Conv2dFwdOp | test_conv2d_bench[resnet-1x1-bias-bfloat16] | 0.0046 | 44.95 | 0.88 | flaggems 1047.2%, torch 250.0%, torch-compile 188.9% | - |
| 🟢 | Conv2dFwdOp | test_conv2d_bench[bottleneck-expand-1x1-bias-float16] | 0.0041 | 50.37 | 0.52 | flaggems 673.4%, torch 214.1%, torch-compile 189.1% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[bottleneck-reduce-1x1-bias-float16] | 0.0050 | 41.48 | 0.43 | flaggems 516.1%, torch 147.1%, torch-compile 171.0% | - |
| 🔵 | Conv2dFwdOp | test_conv2d_bench[late-stage-1x1-bias-float16] | 0.0053 | 19.50 | 0.19 | flaggems 280.6%, torch 175.8%, torch-compile 137.6% | - |
| 🔴 | Conv2dFwdOp | test_conv2d_bench[classifier-1x1-bias-float16] | 0.0095 | 10.82 | 0.25 | flaggems 209.4%, torch 124.2%, torch-compile 77.8% | - |
| 🟢 | Conv3dFwdOp | test_conv3d_bench[r3d-stem-k3-s1-float16] | 0.0229 | 90.69 | 1.17 | flaggems 374.0%, torch 500.4%, torch-compile 500.4% | - |
| 🔴 | Conv3dFwdOp | test_conv3d_bench[video-stage-downsample-k3-s2-float16] | 0.0349 | 39.74 | 0.13 | flaggems 623.4%, torch 75.8%, torch-compile 75.8% | - |
| 🔴 | Conv3dFwdOp | test_conv3d_bench[unet-encoder-k3-s1-bfloat16] | 0.3550 | 40.84 | 0.07 | flaggems 89.2%, torch 32.5%, torch-compile 32.5% | - |
| 🔴 | Conv3dFwdOp | test_conv3d_bench[3d-unet-aspp-3x3x3-rate6-float16] | 0.1265 | 57.30 | 0.04 | flaggems 237.4%, torch 29.7%, torch-compile 29.7% | - |
| 🟢 | Conv3dFwdOp | test_conv3d_bench[3d-resnext-grouped-k3-float16] | 0.0157 | 5.51 | 0.15 | flaggems 1616.8%, torch 1690.7%, torch-compile 1682.5% | - |
| 🟢 | Conv3dFwdOp | test_conv3d_bench[r3d-stem-k3-s1-bias-float16] | 0.0229 | 91.25 | 1.17 | flaggems 370.3%, torch 674.8%, torch-compile 549.7% | - |
| 🔴 | Conv3dFwdOp | test_conv3d_bench[video-stage-downsample-k3-s2-bias-float16] | 0.0353 | 39.26 | 0.13 | flaggems 610.8%, torch 84.8%, torch-compile 79.5% | - |
| 🔴 | Conv3dFwdOp | test_conv3d_bench[unet-encoder-k3-s1-bias-bfloat16] | 0.3545 | 40.92 | 0.07 | flaggems 89.1%, torch 39.8%, torch-compile 34.5% | - |
| 🔵 | CosFwdOp | test_cos_bench[elementwise-16M-float16] | 0.0263 | 0.64 | 2.56 | torch 104.1%, torch-compile 106.2% | - |
| 🔵 | CosFwdOp | test_cos_bench[elementwise-16M-bfloat16] | 0.0265 | 0.63 | 2.53 | torch 102.7%, torch-compile 107.0% | - |
| 🟡 | CosFwdOp | test_cos_bench[elementwise-16M-float32] | 0.0359 | 0.47 | 3.74 | torch 95.9%, torch-compile 95.8% | - |
| 🔵 | CosFwdOp | test_cos_bench[elementwise-256M-float16] | 0.3803 | 0.71 | 2.82 | torch 103.3%, torch-compile 107.4% | - |
| 🔵 | CosFwdOp | test_cos_bench[elementwise-256M-bfloat16] | 0.3856 | 0.70 | 2.78 | torch 102.0%, torch-compile 107.0% | - |
| 🔵 | CountNonzeroFwdOp | test_count_nonzero_bench[sparsity-hidden-float16] | 0.0086 | 1.94 | 1.94 | torch 737.0%, torch-compile 105.5% | - |
| 🔵 | CountNonzeroFwdOp | test_count_nonzero_bench[sparsity-hidden-bfloat16] | 0.0088 | 1.90 | 1.90 | torch 723.1%, torch-compile 103.1% | - |
| 🟡 | CountNonzeroFwdOp | test_count_nonzero_bench[sparsity-seq-float16] | 0.0045 | 0.46 | 0.46 | torch 337.6%, torch-compile 85.9% | - |
| 🔴 | CountNonzeroFwdOp | test_count_nonzero_bench[3d-multidim-reduce-float16] | 0.0115 | 0.37 | 0.37 | torch 189.7%, torch-compile 41.6% | - |
| 🔴 | CumprodFwdOp | test_cumprod_bench[hidden-state-scan-float16] | 0.0444 | 0.19 | 0.76 | torch 328.3%, torch-compile 54.6% | - |
| 🔴 | CumprodFwdOp | test_cumprod_bench[hidden-state-scan-bfloat16] | 0.0436 | 0.19 | 0.77 | torch 335.1%, torch-compile 55.9% | - |
| 🔴 | CumprodFwdOp | test_cumprod_bench[long-seq-scan-bfloat16] | 0.2501 | 0.01 | 0.03 | torch 27.1%, torch-compile 4.9% | - |
| 🔴 | CumsumFwdOp | test_cumsum_bench[hidden-state-scan-float16] | 0.0444 | 0.19 | 0.76 | flaggems 23.8%, torch 328.9%, torch-compile 54.5% | - |
| 🔴 | CumsumFwdOp | test_cumsum_bench[hidden-state-scan-bfloat16] | 0.0435 | 0.19 | 0.77 | flaggems 24.2%, torch 335.8%, torch-compile 56.0% | - |
| 🔴 | CumsumFwdOp | test_cumsum_bench[long-seq-scan-bfloat16] | 0.0295 | 0.07 | 0.28 | flaggems 27.1%, torch 229.8%, torch-compile 41.3% | - |
| 🔴 | DaCumsumFwdOp | test_da_cumsum_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0051 | 0.27 | 0.39 | mamba 65.4%, torch-ref 1400.0%, torch-compile 93.7% | - |
| 🔴 | DaCumsumFwdOp | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-bfloat16] | 0.0154 | 0.48 | 0.68 | mamba 42.0%, torch-ref 590.9%, torch-compile 74.2% | - |
| 🟡 | DaCumsumFwdOp | test_da_cumsum_fwd_bench[mamba2-780m-b1-s4k-dt-bias-float16] | 0.0043 | 0.37 | 0.46 | mamba 80.6%, torch-ref 1730.6%, torch-compile 111.9% | - |
| 🔴 | DaCumsumFwdOp | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-dt-bias-bfloat16] | 0.0148 | 0.56 | 0.71 | mamba 42.9%, torch-ref 648.5%, torch-compile 77.0% | - |
| 🔴 | DaCumsumFwdOp | test_da_cumsum_fwd_bench[mamba2-2p7b-b2-s32k-dt-bias-float16] | 0.0598 | 0.70 | 0.88 | mamba 37.3%, torch-ref 396.5%, torch-compile 57.9% | - |
| 🟢 | DeepSeekSparseAttentionDecodeWithKVCacheFwdOp | test_dsa_decode_bench[single-batch-mainstream-float16] | 1.8589 | 314.23 | 0.16 | torch-ref 1020.8%, torch-compile 893.7%, torch-sdpa 282.9% | - |
| 🟢 | DeepSeekSparseAttentionDecodeWithKVCacheFwdOp | test_dsa_decode_bench[longer-kv-lower-topk-float16] | 0.5001 | 292.00 | 0.30 | torch-ref 3862.8%, torch-compile 3255.6%, torch-sdpa 1054.9%, torch-gather 362.6% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s2k-h4-d64-float16] | 0.1306 | 2.06 | 0.21 | fla 86.8% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s2k-h4-d64-bfloat16] | 0.1316 | 2.04 | 0.21 | fla 86.9% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s4k-h4-d64-float16] | 0.2594 | 2.07 | 0.21 | fla 82.6% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s4k-h4-d64-bfloat16] | 0.2620 | 2.05 | 0.21 | fla 82.6% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s8k-h4-d64-float16] | 0.5046 | 2.13 | 0.22 | fla 85.7% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s8k-h4-d64-bfloat16] | 0.5103 | 2.10 | 0.21 | fla 85.4% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s16k-h4-d64-float16] | 0.9942 | 2.16 | 0.22 | fla 86.9% | - |
| 🟡 | DeltaNetBwdOp | test_deltanet_vs_fla_bwd[dn-bwd-b2-s16k-h4-d64-bfloat16] | 1.0038 | 2.14 | 0.22 | fla 86.9% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b1-h8-d128-bfloat16] | 0.0028 | 0.28 | 0.19 | torch 1175.4%, torch-compile 459.6% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b1-h16-d128-bfloat16] | 0.0031 | 0.51 | 0.35 | torch 1152.0%, torch-compile 465.6% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b1-h32-d128-bfloat16] | 0.0034 | 0.94 | 0.63 | torch 1165.7%, torch-compile 481.9% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b1-h48-d128-bfloat16] | 0.0036 | 1.32 | 0.89 | torch 1209.3%, torch-compile 548.4% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b1-h64-d128-bfloat16] | 0.0038 | 1.64 | 1.11 | torch 1141.7%, torch-compile 487.5% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b8-h32-d128-bfloat16] | 0.0087 | 2.89 | 1.95 | torch 1026.0%, torch-compile 437.7% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b8-h48-d128-bfloat16] | 0.0123 | 3.08 | 2.08 | torch 901.9%, torch-compile 322.1% | - |
| 🟢 | DeltaNetDecodeFwdOp | test_deltanet_decode_bench[delta-decode-serving-b8-h64-d128-bfloat16] | 0.0163 | 3.09 | 2.09 | torch 871.6%, torch-compile 315.5% | - |
| 🟡 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s2k-h4-d64-float16] | 0.0627 | 2.14 | 0.34 | fla 98.8% | - |
| 🟡 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s2k-h4-d64-bfloat16] | 0.0630 | 2.13 | 0.34 | fla 99.0% | - |
| 🟡 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s4k-h4-d64-float16] | 0.1094 | 2.45 | 0.39 | fla 90.0% | - |
| 🟡 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s4k-h4-d64-bfloat16] | 0.1096 | 2.45 | 0.38 | fla 90.6% | - |
| 🟡 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s8k-h4-d64-float16] | 0.2337 | 2.30 | 0.36 | fla 81.0% | - |
| 🟡 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s8k-h4-d64-bfloat16] | 0.2347 | 2.29 | 0.36 | fla 81.5% | - |
| 🔴 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s16k-h4-d64-float16] | 0.4728 | 2.27 | 0.36 | fla 77.3% | - |
| 🔴 | DeltaNetFwdOp | test_deltanet_vs_fla_fwd[dn-b2-s16k-h4-d64-bfloat16] | 0.4737 | 2.27 | 0.35 | fla 78.1% | - |
| 🟡 | DivFwdOp | test_binary_arith_bench[div-1024x4096-float16-float16-DivFwdOp-div-positive] | 0.0085 | 0.49 | 2.96 | torch 103.0%, torch-compile 99.2% | - |
| 🟡 | DivFwdOp | test_binary_arith_bench[div-1024x10240-float16-float16-DivFwdOp-div-positive] | 0.0182 | 0.58 | 3.46 | torch 101.6%, torch-compile 99.2% | - |
| 🟡 | DivFwdOp | test_binary_arith_bench[div-1024x11008-float16-float16-DivFwdOp-div-positive] | 0.0190 | 0.59 | 3.56 | torch 101.4%, torch-compile 99.0% | - |
| 🟡 | DivFwdOp | test_div_manifest_bench[hidden-state-prefill-float16] | 0.0149 | 0.56 | 3.38 | torch 101.7%, torch-compile 98.5% | - |
| 🟡 | DivFwdOp | test_div_manifest_bench[hidden-state-prefill-bfloat16] | 0.0147 | 0.57 | 3.42 | torch 102.8%, torch-compile 99.7% | - |
| 🟡 | DivFwdOp | test_div_manifest_bench[hidden-state-prefill-float32] | 0.0263 | 0.32 | 3.82 | torch 100.4%, torch-compile 99.5% | - |
| 🔴 | DivFwdOp | test_div_manifest_bench[cnn-feat-broadcast-float16] | 0.0187 | 0.69 | 2.75 | torch 270.9%, torch-compile 79.1% | - |
| 🟡 | DivFwdOp | test_div_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0174 | 0.74 | 2.95 | torch 295.0%, torch-compile 82.5% | - |
| 🟡 | DivFwdOp | test_div_manifest_bench[cnn-feat-broadcast-float32] | 0.0269 | 0.48 | 3.81 | torch 196.9%, torch-compile 98.2% | - |
| 🟢 | DropoutFwdOp | test_dropout_bench[tokens-1k-hidden-4k-float16] | 0.0062 | 0.68 | 2.72 | torch 189.6%, torch-compile 183.4% | - |
| 🔵 | DropoutFwdOp | test_dropout_bench[tokens-1k-hidden-4k-float32] | 0.0103 | 0.41 | 3.27 | torch 144.5%, torch-compile 116.5% | - |
| 🟢 | DropoutFwdOp | test_dropout_bench[tokens-1k-hidden-10k-bfloat16] | 0.0123 | 0.85 | 3.40 | torch 192.5%, torch-compile 191.2% | - |
| 🔵 | EluFwdOp | test_elu_manifest_bench[mlp-hidden-float16] | 0.0122 | 2.76 | 2.76 | torch 147.6%, torch-compile 130.5% | - |
| 🔵 | EluFwdOp | test_elu_manifest_bench[mlp-hidden-bfloat16] | 0.0120 | 2.79 | 2.79 | torch 151.1%, torch-compile 138.8% | - |
| 🔵 | EluFwdOp | test_elu_manifest_bench[mlp-hidden-wide-float16] | 0.0218 | 3.08 | 3.08 | torch 150.0%, torch-compile 135.8% | - |
| 🔵 | EluFwdOp | test_elu_manifest_bench[mlp-hidden-wide-bfloat16] | 0.0215 | 3.12 | 3.12 | torch 154.7%, torch-compile 145.8% | - |
| 🔴 | EngramDecodeFwdOp | test_engram_decode_bench[decode-b1-dmem512-d256-float16] | 0.0329 | 0.02 | 0.02 | torch-ref 286.2%, torch-compile 39.9% | - |
| 🔴 | EngramDecodeFwdOp | test_engram_decode_bench[decode-b4-dmem1024-d512-float16] | 0.0826 | 0.10 | 0.03 | torch-ref 147.0%, torch-compile 31.3% | - |
| 🔴 | EngramDecodeFwdOp | test_engram_decode_bench[decode-b8-dmem512-d256-bfloat16] | 0.0335 | 0.13 | 0.02 | torch-ref 332.6%, torch-compile 63.3% | - |
| 🟢 | EngramGateConvBwdOp | test_engram_gate_conv_bwd_bench[bwd-b1-s32-d256-float16] | 0.0111 | 0.04 | 0.02 | torch 1512.2%, torch-compile 434.4% | - |
| 🟢 | EngramGateConvBwdOp | test_engram_gate_conv_bwd_bench[bwd-b2-s64-d512-float16] | 0.0198 | 0.20 | 0.07 | torch 1012.5%, torch-compile 286.1% | - |
| 🟢 | EngramGateConvBwdOp | test_engram_gate_conv_bwd_bench[bwd-b1-s128-d256-bfloat16] | 0.0167 | 0.12 | 0.04 | torch 1105.5%, torch-compile 322.8% | - |
| 🟢 | EngramGateConvFwdOp | test_engram_gate_conv_fwd_bench[fwd-b1-s32-d256-float16] | 0.0040 | 0.05 | 0.02 | torch-ref 1850.0%, torch-compile 292.9% | - |
| 🟢 | EngramGateConvFwdOp | test_engram_gate_conv_fwd_bench[fwd-b2-s64-d512-float16] | 0.0051 | 0.31 | 0.13 | torch-ref 1685.1%, torch-compile 289.0% | - |
| 🟢 | EngramGateConvFwdOp | test_engram_gate_conv_fwd_bench[fwd-b1-s128-d256-bfloat16] | 0.0045 | 0.18 | 0.07 | torch-ref 1788.9%, torch-compile 261.4% | - |
| 🟡 | EqFwdOp | test_comparison_bench[eq-1024x4096-float16-eq] | 0.0080 | 0.52 | 2.62 | torch 98.0%, torch-compile 98.4% | - |
| 🟡 | EqFwdOp | test_comparison_bench[eq-1024x10240-float16-eq] | 0.0172 | 0.61 | 3.05 | torch 93.3%, torch-compile 93.3% | - |
| 🟡 | EqFwdOp | test_eq_manifest_bench[hidden-state-prefill-float16] | 0.0141 | 0.59 | 2.97 | torch 96.0%, torch-compile 95.7% | - |
| 🟡 | EqFwdOp | test_eq_manifest_bench[hidden-state-prefill-bfloat16] | 0.0140 | 0.60 | 3.01 | torch 93.8%, torch-compile 93.8% | - |
| 🔵 | EqFwdOp | test_eq_manifest_bench[hidden-state-prefill-float32] | 0.0223 | 0.38 | 3.38 | torch 100.3%, torch-compile 100.0% | - |
| 🔴 | EqFwdOp | test_eq_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.81 | 2.42 | torch 299.2%, torch-compile 75.0% | - |
| 🔴 | EqFwdOp | test_eq_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.81 | 2.42 | torch 306.4%, torch-compile 75.0% | - |
| 🟡 | EqFwdOp | test_eq_manifest_bench[cnn-feat-broadcast-float32] | 0.0215 | 0.60 | 2.99 | torch 222.7%, torch-compile 85.8% | - |
| 🟡 | ErfFwdOp | test_erf_bench[elementwise-16M-float16] | 0.0284 | 0.59 | 2.37 | torch 93.5%, torch-compile 103.7% | - |
| 🟡 | ErfFwdOp | test_erf_bench[elementwise-16M-bfloat16] | 0.0285 | 0.59 | 2.35 | torch 97.4%, torch-compile 104.3% | - |
| 🟡 | ErfFwdOp | test_erf_bench[elementwise-16M-float32] | 0.0354 | 0.47 | 3.80 | torch 96.9%, torch-compile 97.7% | - |
| 🟡 | ErfFwdOp | test_erf_bench[elementwise-256M-float16] | 0.4209 | 0.64 | 2.55 | torch 91.7%, torch-compile 102.5% | - |
| 🟡 | ErfFwdOp | test_erf_bench[elementwise-256M-bfloat16] | 0.4244 | 0.63 | 2.53 | torch 95.8%, torch-compile 103.1% | - |
| 🟡 | ExpFwdOp | test_exp_bench[elementwise-16M-float16] | 0.0182 | 0.92 | 3.68 | torch 99.9%, torch-compile 99.7% | - |
| 🔵 | ExpFwdOp | test_exp_bench[elementwise-16M-bfloat16] | 0.0184 | 0.91 | 3.65 | torch 100.0%, torch-compile 100.2% | - |
| 🟡 | ExpFwdOp | test_exp_bench[elementwise-16M-float32] | 0.0341 | 0.49 | 3.93 | torch 100.0%, torch-compile 99.8% | - |
| 🟡 | ExpFwdOp | test_exp_bench[elementwise-256M-float16] | 0.2588 | 1.04 | 4.15 | torch 99.2%, torch-compile 99.2% | - |
| 🟡 | ExpFwdOp | test_exp_bench[elementwise-256M-bfloat16] | 0.2614 | 1.03 | 4.11 | torch 99.0%, torch-compile 100.7% | - |
| 🔵 | Expm1FwdOp | test_expm1_bench[elementwise-16M-float16] | 0.0182 | 1.85 | 3.69 | torch 138.6%, torch-compile 148.4% | - |
| 🟢 | Expm1FwdOp | test_expm1_bench[elementwise-16M-bfloat16] | 0.0183 | 1.83 | 3.67 | torch 152.6%, torch-compile 152.6% | - |
| 🔵 | Expm1FwdOp | test_expm1_bench[elementwise-16M-float32] | 0.0341 | 0.98 | 3.93 | torch 100.5%, torch-compile 100.8% | - |
| 🔵 | Expm1FwdOp | test_expm1_bench[elementwise-256M-float16] | 0.2584 | 2.08 | 4.15 | torch 142.2%, torch-compile 152.8% | - |
| 🟢 | Expm1FwdOp | test_expm1_bench[elementwise-256M-bfloat16] | 0.2614 | 2.05 | 4.11 | torch 157.3%, torch-compile 157.2% | - |
| 🔴 | FFTC2CFwdOp | test_fft_bench[fft-4k-c64-unbatched-complex64] | 0.0081 | 0.03 | 0.01 | torch-cufft 66.9%, torch-compile 67.3% | - |
| 🔴 | FFTC2CFwdOp | test_fft_bench[fft-4k-c64-b64-complex64] | 0.0152 | 1.03 | 0.28 | torch-cufft 37.0%, torch-compile 37.0% | - |
| 🔴 | FFTC2CFwdOp | test_fft_bench[fft-4k-c128-b64-complex128] | 0.0305 | 0.52 | 0.28 | torch-cufft 27.8%, torch-compile 27.8% | - |
| 🟢 | FP8LightningIndexerFwdOp | test_fp8_lightning_indexer_bench[lightning-indexer-s8k-h32-d64-bfloat16] | 0.6180 | 55.60 | 1.80 | torch-ref 18117.1%, torch-compile 8031.0% | - |
| 🟡 | FP8QuantFwdOp | test_fp8_quant_bench[kv-index-8k-d64-float16] | 0.0028 | 1.13 | 0.58 | torch-ref 599.1%, torch-compile 88.6% | - |
| 🟡 | FP8QuantFwdOp | test_fp8_quant_bench[kv-index-8k-d64-bfloat16] | 0.0028 | 1.13 | 0.58 | torch-ref 598.9%, torch-compile 89.7% | - |
| 🔵 | FP8QuantFwdOp | test_fp8_quant_bench[kv-index-4k-d128-float32] | 0.0039 | 0.80 | 0.67 | torch-ref 392.6%, torch-compile 106.5% | - |
| 🔵 | FloorDivideFwdOp | test_binary_arith_bench[floor_divide-1024x4096-float16-float16-FloorDivideFwdOp-floor_divide-positive] | 0.0087 | 0.48 | 2.89 | torch 302.9%, torch-compile 100.7% | - |
| 🟡 | FloorDivideFwdOp | test_binary_arith_bench[floor_divide-1024x10240-float16-float16-FloorDivideFwdOp-floor_divide-positive] | 0.0180 | 0.58 | 3.49 | torch 329.8%, torch-compile 99.8% | - |
| 🔵 | FloorDivideFwdOp | test_floor_divide_manifest_bench[hidden-state-prefill-float16] | 0.0151 | 1.11 | 3.33 | torch 320.8%, torch-compile 100.2% | - |
| 🟡 | FloorDivideFwdOp | test_floor_divide_manifest_bench[hidden-state-prefill-bfloat16] | 0.0149 | 1.12 | 3.37 | torch 337.3%, torch-compile 99.8% | - |
| 🔵 | FloorDivideFwdOp | test_floor_divide_manifest_bench[hidden-state-prefill-float32] | 0.0264 | 0.63 | 3.81 | torch 179.3%, torch-compile 100.4% | - |
| 🔴 | FloorDivideFwdOp | test_floor_divide_manifest_bench[cnn-feat-broadcast-float16] | 0.0199 | 1.29 | 2.59 | torch 549.8%, torch-compile 79.4% | - |
| 🔴 | FloorDivideFwdOp | test_floor_divide_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0200 | 1.28 | 2.57 | torch 568.9%, torch-compile 79.5% | - |
| 🟡 | FloorDivideFwdOp | test_floor_divide_manifest_bench[cnn-feat-broadcast-float32] | 0.0272 | 0.95 | 3.78 | torch 372.8%, torch-compile 98.2% | - |
| 🔵 | FloorFwdOp | test_floor_bench[elementwise-16M-float16] | 0.0180 | 0.93 | 3.74 | torch 100.0%, torch-compile 100.0% | - |
| 🟡 | FloorFwdOp | test_floor_bench[elementwise-16M-bfloat16] | 0.0180 | 0.93 | 3.74 | torch 100.2%, torch-compile 99.8% | - |
| 🟡 | FloorFwdOp | test_floor_bench[elementwise-16M-float32] | 0.0340 | 0.49 | 3.94 | torch 99.8%, torch-compile 99.7% | - |
| 🟡 | FloorFwdOp | test_floor_bench[elementwise-256M-float16] | 0.2527 | 1.06 | 4.25 | torch 99.1%, torch-compile 99.0% | - |
| 🟡 | FloorFwdOp | test_floor_bench[elementwise-256M-bfloat16] | 0.2530 | 1.06 | 4.24 | torch 98.9%, torch-compile 98.7% | - |
| 🔵 | FusedAddLayerNormFwdOp | test_fused_add_layer_norm_bench[llama-8b-prefill-float16] | 0.0211 | 2.39 | 3.19 | torch-ref 551.3%, torch-compile 136.0% | - |
| 🔵 | FusedAddLayerNormFwdOp | test_fused_add_layer_norm_bench[llama-8b-prefill-bfloat16] | 0.0220 | 2.29 | 3.05 | torch-ref 532.1%, torch-compile 131.6% | - |
| 🔵 | FusedAddLayerNormFwdOp | test_fused_add_layer_norm_bench[llama-8b-decode-bfloat16] | 0.0031 | 0.01 | 0.02 | torch-ref 603.1%, torch-compile 118.4% | - |
| 🔵 | FusedAddLayerNormFwdOp | test_fused_add_layer_norm_bench[llama-70b-prefill-float16] | 0.0441 | 2.28 | 3.04 | torch-ref 515.5%, torch-compile 101.9% | - |
| 🟡 | FusedAddLayerNormFwdOp | test_fused_add_layer_norm_bench[llama-70b-prefill-bfloat16] | 0.0473 | 2.13 | 2.84 | torch-ref 484.9%, torch-compile 97.6% | - |
| 🔵 | FusedAddLayerNormFwdOp | test_fused_add_layer_norm_bench[llama-70b-decode-bfloat16] | 0.0041 | 0.01 | 0.02 | torch-ref 627.9%, torch-compile 135.7% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-8b-prefill-float16] | 0.0208 | 2.02 | 3.23 | flashinfer 92.7%, vllm 90.1%, torch-ref 1283.9%, torch-compile 94.0% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-8b-prefill-bfloat16] | 0.0212 | 1.97 | 3.16 | flashinfer 90.9%, vllm 90.1%, torch-ref 1264.3%, torch-compile 92.6% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-8b-decode-bfloat16] | 0.0027 | 0.01 | 0.02 | flashinfer 85.9%, vllm 109.4%, torch-ref 1058.9%, torch-compile 87.1% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-70b-prefill-float16] | 0.0378 | 2.22 | 3.55 | flashinfer 95.4%, vllm 95.1%, torch-ref 1359.2%, torch-compile 96.1% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-70b-prefill-bfloat16] | 0.0380 | 2.21 | 3.53 | flashinfer 95.2%, vllm 95.8%, torch-ref 1361.4%, torch-compile 95.8% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-70b-decode-bfloat16] | 0.0035 | 0.01 | 0.02 | flashinfer 82.6%, vllm 100.9%, torch-ref 859.6%, torch-compile 84.4% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-405b-prefill-float16] | 0.0768 | 2.18 | 3.50 | flashinfer 93.0%, vllm 101.4%, torch-ref 1280.3%, torch-compile 93.2% | - |
| 🟡 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-405b-prefill-bfloat16] | 0.0854 | 1.97 | 3.14 | flashinfer 84.0%, vllm 91.5%, torch-ref 1160.7%, torch-compile 84.6% | - |
| 🔴 | FusedAddRMSNormFwdOp | test_fused_add_rms_norm_bench[llama-405b-decode-bfloat16] | 0.0062 | 0.01 | 0.03 | flashinfer 69.6%, vllm 80.4%, torch-ref 510.3%, torch-compile 94.3% | - |
| 🔵 | FusedMoEExpertsNopadPersistent3WGFwdOp | test_moe_experts_nopad_bench[qwen3-235b-decode-bfloat16] | 2.7711 | 130.19 | 4.07 | vllm-triton 103.0% | - |
| 🔵 | FusedMoEExpertsNopadPersistent3WGFwdOp | test_moe_experts_nopad_bench[qwen3-235b-prefill-bfloat16] | 6.0908 | 473.86 | 1.87 | vllm-triton 118.8% | - |
| 🔵 | FusedMoEExpertsNopadPersistent3WGFwdOp | test_moe_experts_nopad_bench[deepseek-v3-decode-bfloat16] | 5.4193 | 66.57 | 4.16 | vllm-triton 101.7% | - |
| 🔵 | FusedMoEExpertsNopadPersistent3WGFwdOp | test_moe_experts_nopad_bench[deepseek-v3-prefill-bfloat16] | 8.4322 | 342.29 | 2.69 | vllm-triton 105.2% | - |
|  | FusedMoEExpertsNopadPersistent3WGFwdOp | test_moe_experts_nopad_bench[deepseek-v3-ep2-decode-bfloat16] | 2.7252 | 132.39 | 4.14 | - | - |
|  | FusedMoEExpertsNopadPersistent3WGFwdOp | test_moe_experts_nopad_bench[deepseek-v3-ep2-prefill-bfloat16] | 4.1293 | 698.97 | 2.76 | - | - |
| 🔵 | FusedMoeFwdOp | test_fused_moe_fwd_bench[qwen3-235b-decode-bfloat16] | 2.7717 | 130.16 | 4.07 | vllm 103.1% | - |
| 🔵 | FusedMoeFwdOp | test_fused_moe_fwd_bench[qwen3-235b-prefill-bfloat16] | 6.1437 | 469.78 | 1.85 | vllm 119.1% | - |
| 🔵 | FusedMoeFwdOp | test_fused_moe_fwd_bench[deepseek-v3-decode-bfloat16] | 5.4235 | 66.52 | 4.16 | vllm 101.8% | - |
| 🔵 | FusedMoeFwdOp | test_fused_moe_fwd_bench[deepseek-v3-prefill-bfloat16] | 8.3882 | 344.08 | 2.70 | vllm 105.9% | - |
| 🟢 | FusedMoeFwdOp | test_fused_moe_fwd_bench[kimi-k2-decode-bfloat16] | 3.8921 | 92.69 | 5.80 | torch-ref 1455.5% | - |
| 🟢 | FusedMoeFwdOp | test_fused_moe_fwd_bench[kimi-k2-prefill-bfloat16] | 7.8827 | 366.14 | 2.88 | torch-ref 1786.2% | - |
| 🟡 | FusedTopKOp | test_fused_topk_bench[1-384-8-sigmoid-renormalize] | 0.0083 | 0.00 | 0.00 | vllm 99.6% | - |
| 🟡 | FusedTopKOp | test_fused_topk_bench[32-384-8-sigmoid-renormalize] | 0.0119 | 0.02 | 0.00 | vllm 81.6% | - |
| 🟡 | FusedTopKOp | test_fused_topk_bench[512-384-8-sigmoid-renormalize] | 0.0126 | 0.28 | 0.03 | vllm 83.3% | - |
| 🔵 | FusedTopKOp | test_fused_topk_bench[4096-384-8-sigmoid-renormalize] | 0.0203 | 1.40 | 0.17 | vllm 117.4% | - |
| 🔵 | FusedTopKOp | test_fused_topk_bench[1-128-8-softmax-norenormalize] | 0.0043 | 0.00 | 0.00 | vllm 142.1% | - |
| 🔵 | FusedTopKOp | test_fused_topk_bench[32-128-8-softmax-norenormalize] | 0.0074 | 0.01 | 0.00 | vllm 112.1% | - |
| 🔵 | FusedTopKOp | test_fused_topk_bench[512-128-8-softmax-norenormalize] | 0.0078 | 0.15 | 0.02 | vllm 115.2% | - |
| 🔵 | FusedTopKOp | test_fused_topk_bench[4096-128-8-softmax-norenormalize] | 0.0110 | 0.86 | 0.12 | vllm 147.2% | - |
| 🟡 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s2k-h4-d64-float16] | 0.1829 | 1.47 | 0.17 | fla 81.1% | - |
| 🟡 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s2k-h4-d64-bfloat16] | 0.1844 | 1.46 | 0.17 | fla 80.4% | - |
| 🔴 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s4k-h4-d64-float16] | 0.3691 | 1.45 | 0.17 | fla 78.1% | - |
| 🔴 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s4k-h4-d64-bfloat16] | 0.3650 | 1.47 | 0.17 | fla 78.8% | - |
| 🔴 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s8k-h4-d64-float16] | 0.7449 | 1.44 | 0.17 | fla 74.7% | - |
| 🔴 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s8k-h4-d64-bfloat16] | 0.7267 | 1.48 | 0.17 | fla 76.7% | - |
| 🔴 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s16k-h4-d64-float16] | 1.5146 | 1.42 | 0.17 | fla 71.4% | - |
| 🔴 | GLABwdOp | test_gla_bwd_bench[gla-bwd-b2-s16k-h4-d64-bfloat16] | 1.4497 | 1.48 | 0.17 | fla 74.5% | - |
| 🟡 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b1-h8-d128-bfloat16] | 0.0075 | 0.07 | 0.07 | fla 91.0%, torch 408.2%, torch-compile 81.6% | - |
| 🟡 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b1-h16-d128-bfloat16] | 0.0074 | 0.14 | 0.14 | fla 94.0%, torch 429.3%, torch-compile 90.1% | - |
| 🟡 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b1-h32-d128-bfloat16] | 0.0078 | 0.27 | 0.27 | fla 93.8%, torch 459.0%, torch-compile 100.4% | - |
| 🔵 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b1-h48-d128-bfloat16] | 0.0079 | 0.40 | 0.40 | fla 112.5%, torch 508.9%, torch-compile 130.7% | - |
| 🔵 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b1-h64-d128-bfloat16] | 0.0081 | 0.52 | 0.53 | fla 107.1%, torch 515.7%, torch-compile 119.7% | - |
| 🔵 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b8-h32-d128-bfloat16] | 0.0159 | 1.06 | 1.08 | fla 110.1%, torch 563.7%, torch-compile 133.1% | - |
| 🟡 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b8-h48-d128-bfloat16] | 0.0231 | 1.09 | 1.11 | fla 96.3%, torch 522.3%, torch-compile 106.7% | - |
| 🟡 | GLADecodeFwdOp | test_gla_decode_bench[gla-decode-serving-b8-h64-d128-bfloat16] | 0.0305 | 1.10 | 1.12 | fla 87.9%, torch 517.4%, torch-compile 104.8% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-float16] | 0.0984 | 1.36 | 0.11 | fla 71.4% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-bfloat16] | 0.0971 | 1.38 | 0.11 | fla 67.8% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-init-b2-s4k-h4-d64-float16] | 0.1568 | 1.71 | 0.13 | fla 79.9% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-init-b2-s4k-h4-d64-bfloat16] | 0.1564 | 1.72 | 0.13 | fla 76.2% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-float16] | 0.3128 | 1.72 | 0.13 | fla 79.2% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-bfloat16] | 0.3114 | 1.72 | 0.14 | fla 70.8% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-float16] | 0.6179 | 1.74 | 0.14 | fla 75.2% | - |
| 🔴 | GLAFwdOp | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-bfloat16] | 0.6107 | 1.76 | 0.14 | fla 74.1% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-float16] | 0.0866 | 12.40 | 0.20 | fla 77.6% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-bfloat16] | 0.0866 | 12.40 | 0.20 | fla 77.9% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-float16] | 0.1487 | 14.44 | 0.23 | fla 72.4% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-bfloat16] | 0.1444 | 14.87 | 0.23 | fla 75.0% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-float16] | 0.3139 | 13.68 | 0.21 | fla 65.3% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-bfloat16] | 0.3164 | 13.57 | 0.21 | fla 64.9% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-float16] | 0.6354 | 13.52 | 0.21 | fla 61.5% | - |
| 🔴 | GatedDeltaNetBHTDFwdOp | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-bfloat16] | 0.6379 | 13.47 | 0.21 | fla 61.7% | - |
| 🔵 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s2k-h4-d64-float16] | 0.0669 | 16.05 | 0.25 | fla 100.4% | - |
| 🔵 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s2k-h4-d64-bfloat16] | 0.0663 | 16.20 | 0.26 | fla 101.7% | - |
| 🟡 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s4k-h4-d64-float16] | 0.1151 | 18.66 | 0.29 | fla 93.5% | - |
| 🟡 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s4k-h4-d64-bfloat16] | 0.1145 | 18.75 | 0.29 | fla 94.5% | - |
| 🟡 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s8k-h4-d64-float16] | 0.2192 | 19.59 | 0.31 | fla 93.5% | - |
| 🟡 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s8k-h4-d64-bfloat16] | 0.2204 | 19.49 | 0.31 | fla 93.2% | - |
| 🟡 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s16k-h4-d64-float16] | 0.4298 | 19.98 | 0.31 | fla 90.8% | - |
| 🟡 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s16k-h4-d64-bfloat16] | 0.4324 | 19.87 | 0.31 | fla 90.9% | - |
| 🟢 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s32k-h4-d64-float16] | 0.1948 | 88.18 | 1.38 | fla 394.3% | - |
| 🟢 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b2-s32k-h4-d64-bfloat16] | 0.1952 | 88.01 | 1.38 | fla 394.3% | - |
| 🔵 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b1-s4k-h16-d128-float16] | 0.1749 | 58.32 | 0.77 | fla 110.8% | - |
| 🔵 | GatedDeltaNetBTHDFwdOp | test_gated_deltanet_vs_fla_fwd[gdn-bthd-b1-s4k-h16-d128-bfloat16] | 0.1742 | 58.54 | 0.77 | fla 111.7% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-float16] | 0.2016 | 1.33 | 0.08 | fla 66.3% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-bfloat16] | 0.2048 | 1.31 | 0.08 | fla 68.4% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-float16] | 0.3809 | 1.41 | 0.09 | fla 65.5% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-bfloat16] | 0.3876 | 1.39 | 0.09 | fla 66.7% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-float16] | 0.7227 | 1.49 | 0.09 | fla 67.3% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-bfloat16] | 0.7503 | 1.43 | 0.09 | fla 66.9% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-float16] | 1.4238 | 1.51 | 0.10 | fla 64.7% | - |
| 🔴 | GatedDeltaNetBwdOp | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-bfloat16] | 1.4644 | 1.47 | 0.09 | fla 65.1% | - |
| 🔵 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b1-h8-d128-bfloat16] | 0.0031 | 0.26 | 0.17 | fla 129.5% | - |
| 🔵 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b1-h16-d128-bfloat16] | 0.0033 | 0.48 | 0.32 | fla 127.2% | - |
| 🔵 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b1-h32-d128-bfloat16] | 0.0036 | 0.87 | 0.59 | fla 129.2% | - |
| 🔵 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b1-h48-d128-bfloat16] | 0.0038 | 1.23 | 0.83 | fla 136.7% | - |
| 🔵 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b1-h64-d128-bfloat16] | 0.0042 | 1.50 | 1.02 | fla 138.2% | - |
| 🟢 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b8-h32-d128-bfloat16] | 0.0087 | 2.89 | 1.95 | fla 167.4% | - |
| 🟢 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b8-h48-d128-bfloat16] | 0.0124 | 3.05 | 2.06 | fla 155.7% | - |
| 🟢 | GatedDeltaNetDecodeFwdOp | test_gated_deltanet_decode_bench[gdn-decode-serving-b8-h64-d128-bfloat16] | 0.0161 | 3.13 | 2.11 | fla 155.8% | - |
| 🔴 | GatedDeltaNetPrefillBHTDFwdOp | test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-float16] | 0.2512 | 34.20 | 0.34 | fla 78.0% | - |
| 🔴 | GatedDeltaNetPrefillBHTDFwdOp | test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-bfloat16] | 0.2526 | 34.00 | 0.34 | fla 78.3% | - |
| 🟡 | GatedDeltaNetPrefillBHTDFwdOp | test_gated_deltanet_prefill_bhtd_bench[bhtd-qwen35-gdn-prefill-b1-s128k-h64-d128-float16] | 17.4203 | 63.12 | 0.62 | fla 89.6% | - |
| 🟡 | GatedDeltaNetPrefillBHTDFwdOp | test_gated_deltanet_prefill_bhtd_bench[bhtd-qwen35-gdn-prefill-b1-s128k-h64-d128-bfloat16] | 17.5467 | 62.66 | 0.61 | fla 88.8% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[fallback-gdn-prefill-b1-s4k-h16-d128-bthd-float16] | 0.0791 | 108.55 | 1.07 | fla 247.5% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[fallback-gdn-prefill-b1-s4k-h16-d128-bthd-bfloat16] | 0.0793 | 108.33 | 1.07 | fla 248.9% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h16-d128-bthd-float16] | 0.3654 | 188.05 | 1.84 | fla 401.1% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h16-d128-bthd-bfloat16] | 0.3718 | 184.81 | 1.81 | fla 395.5% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h16-d128-bthd-float16] | 0.6972 | 197.12 | 1.93 | fla 417.0% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h16-d128-bthd-bfloat16] | 0.7068 | 194.45 | 1.91 | fla 411.6% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h16-d128-bthd-float16] | 1.2571 | 218.66 | 2.14 | fla 458.9% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h16-d128-bthd-bfloat16] | 1.2828 | 214.28 | 2.10 | fla 450.6% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h32-d128-bthd-float16] | 0.6860 | 200.35 | 1.96 | fla 323.0% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h32-d128-bthd-bfloat16] | 0.6980 | 196.90 | 1.93 | fla 317.9% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h32-d128-bthd-float16] | 1.2465 | 220.51 | 2.16 | fla 352.6% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h32-d128-bthd-bfloat16] | 1.2795 | 214.83 | 2.11 | fla 344.0% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h32-d128-bthd-float16] | 2.4485 | 224.53 | 2.20 | fla 357.4% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h32-d128-bthd-bfloat16] | 2.5053 | 219.44 | 2.15 | fla 350.3% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h48-d128-bthd-float16] | 1.0522 | 195.94 | 1.92 | fla 301.1% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h48-d128-bthd-bfloat16] | 1.0657 | 193.44 | 1.90 | fla 296.9% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h48-d128-bthd-float16] | 1.9163 | 215.17 | 2.11 | fla 329.5% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h48-d128-bthd-bfloat16] | 1.9442 | 212.07 | 2.08 | fla 324.2% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h48-d128-bthd-float16] | 3.7706 | 218.70 | 2.14 | fla 334.1% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h48-d128-bthd-bfloat16] | 3.8169 | 216.05 | 2.12 | fla 329.5% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h64-d128-bthd-float16] | 1.2236 | 224.64 | 2.20 | fla 319.2% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s32k-h64-d128-bthd-bfloat16] | 1.2533 | 219.32 | 2.15 | fla 310.8% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h64-d128-bthd-float16] | 2.3779 | 231.19 | 2.27 | fla 328.1% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s64k-h64-d128-bthd-bfloat16] | 2.4301 | 226.23 | 2.22 | fla 320.7% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h64-d128-bthd-float16] | 4.6581 | 236.04 | 2.31 | fla 335.3% | - |
| 🟢 | GatedDeltaNetPrefillBTHDFwdOp | test_gated_deltanet_prefill_fwd_bench[qwen35-gdn-prefill-b1-s128k-h64-d128-bthd-bfloat16] | 4.7845 | 229.81 | 2.25 | fla 325.9% | - |
| 🟡 | GeFwdOp | test_comparison_bench[ge-1024x4096-float16-ge] | 0.0079 | 0.53 | 2.64 | torch 98.0%, torch-compile 127.0% | - |
| 🟡 | GeFwdOp | test_ge_manifest_bench[hidden-state-prefill-float16] | 0.0142 | 0.59 | 2.95 | torch 93.5%, torch-compile 93.0% | - |
| 🟡 | GeFwdOp | test_ge_manifest_bench[hidden-state-prefill-bfloat16] | 0.0140 | 0.60 | 2.99 | torch 93.6%, torch-compile 93.4% | - |
| 🟡 | GeFwdOp | test_ge_manifest_bench[hidden-state-prefill-float32] | 0.0224 | 0.37 | 3.37 | torch 99.9%, torch-compile 110.7% | - |
| 🔴 | GeFwdOp | test_ge_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.81 | 2.42 | torch 294.8%, torch-compile 74.5% | - |
| 🔴 | GeFwdOp | test_ge_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.81 | 2.43 | torch 300.1%, torch-compile 75.8% | - |
| 🟡 | GeFwdOp | test_ge_manifest_bench[cnn-feat-broadcast-float32] | 0.0213 | 0.60 | 3.02 | torch 220.8%, torch-compile 86.2% | - |
| 🔵 | GeluAndMulFwdOp | test_gelu_and_mul_bench[ffn-gelu-prefill-float16] | 0.0549 | 3.21 | 3.21 | flashinfer 191.0%, torch-ref 369.2%, torch-compile 110.3% | - |
| 🔵 | GeluAndMulFwdOp | test_gelu_and_mul_bench[ffn-gelu-prefill-bfloat16] | 0.0594 | 2.97 | 2.97 | flashinfer 178.4%, torch-ref 344.8%, torch-compile 102.8% | - |
| 🟡 | GeluAndMulFwdOp | test_gelu_and_mul_bench[ffn-gelu-decode-bfloat16] | 0.0015 | 0.06 | 0.06 | flashinfer 433.3%, torch-ref 206.3%, torch-compile 95.8% | - |
| 🟡 | GeluFwdOp | test_gelu_manifest_bench[llama-8b-ffn-prefill-float16] | 0.0529 | 2.77 | 2.22 | torch 90.7%, torch-compile 101.7% | - |
| 🟡 | GeluFwdOp | test_gelu_manifest_bench[llama-8b-ffn-prefill-bfloat16] | 0.0557 | 2.63 | 2.11 | torch 87.8%, torch-compile 99.9% | - |
| 🟡 | GeluFwdOp | test_gelu_manifest_bench[llama-8b-ffn-decode-bfloat16] | 0.0016 | 0.05 | 0.04 | torch 108.2%, torch-compile 89.8% | - |
| 🔵 | GeluTanhAndMulFwdOp | test_gelu_tanh_and_mul_bench[ffn-gelu-tanh-prefill-float16] | 0.0476 | 6.16 | 3.70 | flashinfer 118.5%, torch-ref 402.8%, torch-compile 108.9% | - |
| 🔵 | GeluTanhAndMulFwdOp | test_gelu_tanh_and_mul_bench[ffn-gelu-tanh-prefill-bfloat16] | 0.0491 | 5.98 | 3.59 | flashinfer 117.0%, torch-ref 393.6%, torch-compile 107.5% | - |
| 🔵 | GeluTanhAndMulFwdOp | test_gelu_tanh_and_mul_bench[ffn-gelu-tanh-decode-bfloat16] | 0.0015 | 0.10 | 0.06 | flashinfer 295.7%, torch-ref 208.7%, torch-compile 100.1% | - |
| 🟢 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-decode-gate-up-per-tensor-float8_e4m3fn] | 0.1163 | 33.33 | 0.14 | torch-scaled-mm 208.1% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-decode-down-per-tensor-float8_e4m3fn] | 0.0254 | 148.10 | 0.66 | torch-scaled-mm 964.3%, deepgemm 40.9% | - |
| 🟢 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-prefill-gate-up-per-tensor-float8_e4m3fn] | 0.5109 | 242.75 | 0.12 | torch-scaled-mm 675.7% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-prefill-down-per-tensor-float8_e4m3fn] | 0.2098 | 573.23 | 0.39 | torch-scaled-mm 1595.1%, deepgemm 50.4% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-decode-gate-up-block128-float8_e4m3fn] | 0.3424 | 11.32 | 0.05 | torch-scaled-mm 81.4%, flashinfer-fp8-blockscale-sm90 3.8% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-decode-down-block128-float8_e4m3fn] | 0.0389 | 96.62 | 0.44 | torch-scaled-mm 718.2%, flashinfer-fp8-blockscale-sm90 23.7% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-prefill-gate-up-block128-float8_e4m3fn] | 1.3359 | 92.83 | 0.05 | torch-scaled-mm 265.2%, flashinfer-fp8-blockscale-sm90 10.3% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-prefill-down-block128-float8_e4m3fn] | 0.4486 | 268.09 | 0.18 | torch-scaled-mm 757.0%, flashinfer-fp8-blockscale-sm90 31.9% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-prefill-attn-proj-block128-float8_e4m3fn] | 0.8100 | 296.95 | 0.12 | torch-scaled-mm 823.8%, flashinfer-fp8-blockscale-sm90 26.5% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[k-dominant-7168x16384-block128-float8_e4m3fn] | 3.6222 | 265.61 | 0.07 | torch-scaled-mm 727.8%, flashinfer-fp8-blockscale-sm90 21.3% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[wide-n-24576-block128-float8_e4m3fn] | 1.0368 | 298.25 | 0.24 | torch-scaled-mm 822.0%, flashinfer-fp8-blockscale-sm90 36.9% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[small-batch-down-m8-per-tensor-float8_e4m3fn] | 0.0267 | 8.81 | 0.56 | torch-scaled-mm 625.2%, deepgemm 31.2% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[gemv-down-m1-per-tensor-float8_e4m3fn] | 0.0258 | 1.14 | 0.57 | torch-scaled-mm 504.4%, deepgemm 39.4% | - |
| 🔴 | GemmFp8FwdOp | test_gemm_fp8_bench[gemv-down-m1-block128-float8_e4m3fn] | 0.0631 | 0.47 | 0.24 | torch-scaled-mm 261.1%, flashinfer-fp8-blockscale-sm90 12.3% | - |
| 🟢 | GemmFp8FwdOp | test_gemm_fp8_bench[ds-v3-decode-gate-up-per-tensor-bias-float8_e4m3fn] | 0.1167 | 33.22 | 0.14 | torch-scaled-mm 212.5% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[square-1k-nn-float16] | 0.0145 | 148.47 | 0.43 | torch-cublas 50.0%, flaggems 79.9% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[square-1k-nn-bfloat16] | 0.0145 | 148.47 | 0.43 | torch-cublas 49.8%, flaggems 79.2% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[ds-v3-decode-gate-up-bfloat16] | 0.0677 | 57.26 | 0.48 | torch-cublas 25.6%, deepgemm 31.4% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[ds-v3-decode-down-bfloat16] | 0.0246 | 152.72 | 1.29 | torch-cublas 53.4%, deepgemm 55.9% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[ds-v3-prefill-gate-up-bfloat16] | 0.3360 | 369.15 | 0.32 | torch-cublas 52.8%, deepgemm 54.1% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[ds-v3-prefill-down-bfloat16] | 0.3209 | 374.70 | 0.33 | torch-cublas 56.5%, deepgemm 56.2% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[ds-v3-prefill-attn-proj-float16] | 0.5414 | 444.22 | 0.28 | torch-cublas 62.1% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[ds-v3-prefill-attn-proj-bfloat16] | 0.5424 | 443.44 | 0.28 | torch-cublas 61.3%, deepgemm 61.1% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[k-dominant-7168x16384-bfloat16] | 2.0651 | 465.88 | 0.21 | torch-cublas 61.3%, deepgemm 61.0% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[wide-n-24576-bfloat16] | 0.9007 | 343.32 | 0.32 | torch-cublas 50.3%, deepgemm 49.2% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[mid-m16-attn-bfloat16] | 0.0657 | 14.29 | 0.90 | torch-cublas 37.3%, deepgemm 51.6% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[mid-m32-attn-bfloat16] | 0.0661 | 28.42 | 0.90 | torch-cublas 36.9%, deepgemm 46.3% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[mid-m64-down-bfloat16] | 0.0207 | 90.90 | 1.48 | torch-cublas 63.8%, deepgemm 65.3% | - |
| 🔴 | GemmFwdOp | test_gemm_bench[mid-m96-gate-up-bfloat16] | 0.0687 | 42.34 | 0.47 | torch-cublas 24.5%, deepgemm 31.9% | - |
| 🔴 | GemmW4A16FwdOp | test_gemm_w4a16_bench[compile-smoke-square-64x64x128-float16] | 0.0043 | 0.25 | 0.01 | torch-dequantized-matmul 63.1% | - |
| 🔴 | GemmW4A16FwdOp | test_gemm_w4a16_bench[compile-smoke-rect-128x256x256-float16] | 0.0059 | 2.86 | 0.03 | torch-dequantized-matmul 52.5% | - |
| 🔴 | GemmW4A16FwdOp | test_gemm_w4a16_bench[decode-l2-resident-ish-float16] | 0.0331 | 4.05 | 1.09 | torch-dequantized-matmul 140.4%, marlin-fp32 66.2%, marlin-fp16 65.8% | - |
| 🔴 | GemmW4A16FwdOp | test_gemm_w4a16_bench[decode-hbm-streaming-threshold-float16] | 0.0608 | 4.42 | 1.19 | torch-dequantized-matmul 122.9%, marlin-fp32 62.3%, marlin-fp16 62.6% | - |
| 🔴 | GemmW4A16FwdOp | test_gemm_w4a16_bench[decode-non-power2-low-cta-float16] | 0.0745 | 3.94 | 1.06 | torch-dequantized-matmul 117.7%, marlin-fp32 54.7%, marlin-fp16 54.8% | - |
| 🔴 | GemmW4A16FwdOp | test_gemm_w4a16_bench[decode-long-k-pressure-float16] | 0.2831 | 4.74 | 1.28 | torch-dequantized-matmul 113.9%, marlin-fp32 49.9%, marlin-fp16 49.8% | - |
| 🔵 | GroupNormFwdOp | test_group_norm_bench[image-g32-affine-float16] | 0.0037 | 1.40 | 1.12 | flaggems 107.7%, torch 407.7%, torch-compile 131.6% | - |
| 🔵 | GroupNormFwdOp | test_group_norm_bench[image-g32-affine-bfloat16] | 0.0037 | 1.41 | 1.13 | flaggems 108.6%, torch 411.2%, torch-compile 141.4% | - |
| 🔴 | GroupNormFwdOp | test_group_norm_bench[wider-channel-g32-affine-float16] | 0.0060 | 0.67 | 0.54 | flaggems 66.7%, torch 273.9%, torch-compile 76.3% | - |
| 🔴 | GroupNormFwdOp | test_group_norm_bench[tail-spatial-g16-affine-float16] | 0.0061 | 0.38 | 0.30 | flaggems 66.8%, torch 251.6%, torch-compile 73.2% | - |
| 🔵 | GroupNormFwdOp | test_group_norm_no_affine_bench[image-g32-float16] | 0.0036 | 0.89 | 1.18 | flaggems 100.9%, torch 372.1%, torch-compile 117.1% | - |
| 🔵 | GroupNormFwdOp | test_group_norm_no_affine_bench[image-g32-bfloat16] | 0.0036 | 0.89 | 1.18 | flaggems 100.9%, torch 372.1%, torch-compile 129.7% | - |
| 🔴 | GroupNormFwdOp | test_group_norm_no_affine_bench[wider-channel-g32-float16] | 0.0048 | 0.50 | 0.67 | flaggems 72.4%, torch 295.0%, torch-compile 76.4% | - |
| 🔴 | GroupNormFwdOp | test_group_norm_no_affine_bench[tail-spatial-g16-float16] | 0.0052 | 0.27 | 0.35 | flaggems 69.3%, torch 258.3%, torch-compile 69.9% | - |
| 🟡 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-8b-short-float16] | 0.2030 | 105.80 | 0.33 | fa3 81.8% | - |
| 🔴 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-8b-short-bfloat16] | 0.4159 | 51.63 | 0.16 | fa3 39.7% | - |
| 🔴 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-8b-long-float16] | 0.8313 | 206.67 | 0.16 | fa3 71.3% | - |
| 🔴 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-8b-long-bfloat16] | 1.2425 | 138.27 | 0.11 | fa3 47.4% | - |
| 🟡 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-70b-short-float16] | 0.1964 | 109.35 | 0.30 | fa3 81.1% | - |
| 🔴 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-70b-short-bfloat16] | 0.4094 | 52.45 | 0.14 | fa3 38.8% | - |
| 🔴 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-70b-long-float16] | 0.8092 | 212.29 | 0.15 | fa3 71.7% | - |
| 🔴 | GroupedQueryAttentionBwdOp | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 1.0192 | 168.57 | 0.12 | fa3 56.6% | - |
| 🔴 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-8b-p64-float16] | 0.1669 | 12.87 | 0.10 | flashinfer 75.0% | - |
| 🔵 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-8b-long-p64-float16] | 0.2205 | 19.48 | 0.61 | flashinfer 135.8% | - |
| 🔴 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[throughput-8b-p64-float16] | 0.2516 | 8.53 | 0.04 | flashinfer 59.9% | - |
| 🟡 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-70b-p64-float16] | 0.0495 | 21.68 | 0.34 | flashinfer 89.9% | - |
| 🔴 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-8b-p256-float16] | 0.1682 | 12.77 | 0.10 | fa3 48.3%, flashinfer 74.5% | - |
| 🔴 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-70b-p256-float16] | 0.0684 | 15.69 | 0.25 | fa3 53.7%, flashinfer 83.5% | - |
| 🔴 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-405b-p256-float16] | 0.0563 | 19.06 | 0.30 | fa3 47.1% | - |
| 🔴 | GroupedQueryAttentionDecodePagedWithKVCacheFwdOp | test_gqa_decode_paged_bench[serving-8b-p64-softcap50-float16] | 0.1764 | 12.17 | 0.10 | flashinfer 71.0% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-8b-4k-float16] | 0.1505 | 14.27 | 3.57 | fa3 102.4%, flashinfer 148.8% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-8b-4k-bfloat16] | 0.1500 | 14.32 | 3.58 | fa3 101.7%, flashinfer 171.9% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-8b-32k-float16] | 0.2574 | 16.68 | 4.17 | fa3 104.6%, flashinfer 167.7% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-8b-32k-bfloat16] | 0.2563 | 16.76 | 4.19 | fa3 104.6%, flashinfer 193.8% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-70b-4k-float16] | 0.0793 | 27.09 | 3.39 | fa3 107.8%, flashinfer 253.4% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-70b-4k-bfloat16] | 0.0790 | 27.17 | 3.40 | fa3 107.5%, flashinfer 287.7% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-70b-32k-float16] | 0.1381 | 31.10 | 3.89 | fa3 109.0%, flashinfer 280.4% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-70b-32k-bfloat16] | 0.1377 | 31.20 | 3.90 | fa3 108.7%, flashinfer 321.3% | - |
| 🟢 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[llama-8b-4k-softcap50-float16] | 0.1617 | 13.28 | 3.32 | torch-sdpa 8242.8% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-1k-float16] | 0.0070 | 2.40 | 0.30 | fa3 248.2%, flashinfer 139.0% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-4k-float16] | 0.0096 | 6.97 | 0.87 | fa3 219.8%, flashinfer 120.6% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-8k-float16] | 0.0132 | 10.18 | 1.27 | fa3 176.7%, flashinfer 106.8% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-16k-float16] | 0.0182 | 14.74 | 1.84 | fa3 153.2%, flashinfer 119.9% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-32k-float16] | 0.0284 | 18.94 | 2.37 | fa3 132.4%, flashinfer 122.5% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-64k-float16] | 0.0455 | 23.61 | 2.95 | fa3 126.5%, flashinfer 117.0% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-128k-float16] | 0.0765 | 28.07 | 3.51 | fa3 121.2%, flashinfer 108.8% | - |
| 🔵 | GroupedQueryAttentionDecodeWithKVCacheFwdOp | test_gqa_decode_bench[qwen3-30b-a3b-bs1-256k-float16] | 0.1367 | 31.41 | 3.93 | fa3 118.6%, flashinfer 103.8% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-8b-short-float16] | 0.0371 | 231.51 | 1.13 | fa3 86.0%, flashinfer 106.5% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-8b-short-bfloat16] | 0.0368 | 233.22 | 1.14 | fa3 86.3%, flashinfer 107.0% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-8b-long-float16] | 0.1622 | 423.57 | 0.52 | fa3 82.8%, flashinfer 99.8% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-8b-long-bfloat16] | 0.1612 | 426.34 | 0.52 | fa3 82.9%, flashinfer 100.1% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-70b-short-float16] | 0.0381 | 225.58 | 0.99 | fa3 83.9%, flashinfer 102.6% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-70b-short-bfloat16] | 0.0381 | 225.58 | 0.99 | fa3 83.2%, flashinfer 102.4% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-70b-long-float16] | 0.1632 | 421.07 | 0.46 | fa3 82.1%, flashinfer 99.5% | - |
| 🟡 | GroupedQueryAttentionFwdOp | test_gqa_fwd_bench[llama-70b-long-bfloat16] | 0.1625 | 422.98 | 0.46 | fa3 82.0%, flashinfer 98.7% | - |
| 🔵 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-8b-prefill-dense-float16] | 0.0369 | 233.07 | 1.14 | torch-ref 2979.2%, flashinfer 106.1% | - |
| 🔵 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-8b-prefill-dense-bfloat16] | 0.0368 | 233.68 | 1.14 | torch-ref 2987.9%, flashinfer 106.4% | - |
| 🔵 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-8b-prefill-dense-sm-scale-0.125-float16] | 0.0370 | 232.76 | 1.13 | torch-ref 2972.1%, flashinfer 106.7% | - |
| 🔵 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-8b-prefill-dense-softcap50-float16] | 0.0421 | 204.53 | 1.00 | torch-ref 3080.8%, flashinfer 108.7% | - |
| 🟡 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-8b-prefill-dense-q-lt-kv-float16] | 0.1261 | 510.85 | 0.40 | torch-ref 3249.2%, flashinfer 99.9% | - |
| 🟡 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-8b-prefill-dense-q-lt-kv-bfloat16] | 0.1253 | 514.31 | 0.40 | torch-ref 3273.9%, flashinfer 99.9% | - |
| 🟡 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-70b-prefill-dense-q-lt-kv-float16] | 0.1255 | 513.26 | 0.27 | torch-ref 2995.0%, flashinfer 99.3% | - |
| 🔵 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fwd_bench[llama-70b-prefill-dense-q-lt-kv-bfloat16] | 0.1236 | 521.37 | 0.27 | torch-ref 3045.6%, flashinfer 100.3% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s896-float16] | 0.0454 | 289.67 | 0.20 | torch-sdpa-dequant 202.8%, fa3 62.8% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s896-bfloat16] | 0.0453 | 290.28 | 0.20 | torch-sdpa-dequant 204.3%, fa3 62.8% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s1792-float16] | 0.1288 | 408.64 | 0.14 | torch-sdpa-dequant 175.7%, fa3 66.6% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s1792-bfloat16] | 0.1287 | 408.69 | 0.14 | torch-sdpa-dequant 174.9%, fa3 66.9% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s3584-float16] | 0.7497 | 561.45 | 0.09 | torch-sdpa-dequant 140.7%, fa3 70.4% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s3584-bfloat16] | 0.7507 | 560.67 | 0.09 | torch-sdpa-dequant 139.6%, fa3 70.5% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s7168-float16] | 2.8449 | 591.80 | 0.05 | torch-sdpa-dequant 120.7%, fa3 71.1% | - |
| 🔴 | GroupedQueryAttentionPrefillFwdOp | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s7168-bfloat16] | 2.8501 | 590.72 | 0.05 | torch-sdpa-dequant 120.4%, fa3 71.1% | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-prefill-paged-fullattn-b8-prefix32k-chunk1k-p64-partial-rope64-float16] | 60.6487 | 147.30 | 0.04 | - | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-prefill-paged-fullattn-mixed-b8-p64-partial-rope64-float16] | 30.7253 | 108.02 | 0.04 | - | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-prefill-paged-b8-prefix4k-chunk512-p64-full-rope-float16] | 1.9522 | 149.62 | 0.12 | - | - |
| 🟡 | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[gqa-prefill-paged-softcap50-b4-prefix4k-chunk512-p64-float16] | 0.1499 | 121.82 | 0.10 | fa3 91.4% | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-prefill-paged-fp8-cache-b8-prefix32k-chunk1k-p64-float16] | 56.0383 | 159.42 | 0.05 | - | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-prefill-paged-fp8-cache-b8-prefix4k-chunk512-p64-float16] | 1.9997 | 146.07 | 0.12 | - | - |
|  | GroupedQueryAttentionPrefillPagedWithKVCacheFwdOp | test_gqa_prefill_paged_with_kv_cache_fwd_bench[gqa-prefill-paged-fp8-cache-softcap50-b4-prefix4k-chunk512-p64-float16] | 0.2068 | 88.27 | 0.07 | - | - |
| 🔴 | GroupedQueryAttentionPrefillVarlenFwdOp | test_gqa_prefill_varlen_fwd_bench[llama-8b-prefill-varlen-uniform-fp16] | 0.1252 | 205.99 | 0.40 | torch-ref 1628.6%, fa3 56.9% | - |
| 🔴 | GroupedQueryAttentionPrefillVarlenFwdOp | test_gqa_prefill_varlen_fwd_bench[llama-8b-prefill-varlen-mixed-fp16] | 0.1401 | 143.75 | 0.28 | torch-ref 1198.8%, fa3 43.9% | - |
| 🔴 | GroupedQueryAttentionPrefillVarlenFwdOp | test_gqa_prefill_varlen_fwd_bench[llama-70b-prefill-varlen-q-lt-kv-bf16] | 0.1963 | 218.86 | 0.24 | torch-ref 1408.1%, fa3 50.5% | - |
| 🟡 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-8b-short-w256-float16] | 0.0398 | 162.47 | 1.05 | fa3 86.0%, flashinfer 103.3% | - |
| 🟡 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0398 | 162.60 | 1.05 | fa3 85.6%, flashinfer 103.2% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-8b-long-w1024-float16] | 0.1530 | 337.21 | 0.55 | fa3 78.8%, flashinfer 101.6% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.1513 | 341.06 | 0.55 | fa3 78.6%, flashinfer 101.3% | - |
| 🟡 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-70b-short-w256-float16] | 0.0395 | 163.92 | 0.96 | fa3 86.7%, flashinfer 104.4% | - |
| 🟡 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-70b-short-w256-bfloat16] | 0.0395 | 163.79 | 0.96 | fa3 86.1%, flashinfer 103.3% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-70b-long-w1024-float16] | 0.1528 | 337.67 | 0.49 | fa3 78.8%, flashinfer 101.1% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowFwdOp | test_gqa_sliding_window_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.1511 | 341.49 | 0.50 | fa3 78.0%, flashinfer 100.4% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-float16] | 0.0569 | 113.67 | 0.74 | fa3 82.8%, flashinfer 72.7% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0567 | 114.06 | 0.74 | fa3 82.9%, flashinfer 72.7% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-float16] | 0.3515 | 293.56 | 0.48 | fa3 77.4%, flashinfer 78.3% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.3493 | 295.38 | 0.48 | fa3 77.3%, flashinfer 78.3% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-float16] | 0.0932 | 138.72 | 0.81 | fa3 89.7%, flashinfer 74.0% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-bfloat16] | 0.0931 | 139.00 | 0.81 | fa3 89.6%, flashinfer 74.4% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-float16] | 0.6677 | 309.06 | 0.45 | fa3 79.3%, flashinfer 77.9% | - |
| 🔴 | GroupedQueryAttentionSlidingWindowVarlenFwdOp | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.6687 | 308.62 | 0.45 | fa3 78.8%, flashinfer 77.3% | - |
| 🟡 | GtFwdOp | test_comparison_bench[gt-1024x4096-float16-gt] | 0.0079 | 0.53 | 2.64 | torch 98.4%, torch-compile 98.0% | - |
| 🟡 | GtFwdOp | test_gt_manifest_bench[hidden-state-prefill-float16] | 0.0140 | 0.60 | 2.99 | torch 94.1%, torch-compile 93.8% | - |
| 🟡 | GtFwdOp | test_gt_manifest_bench[hidden-state-prefill-bfloat16] | 0.0140 | 0.60 | 2.99 | torch 93.8%, torch-compile 93.6% | - |
| 🟡 | GtFwdOp | test_gt_manifest_bench[hidden-state-prefill-float32] | 0.0224 | 0.38 | 3.38 | torch 99.9%, torch-compile 99.6% | - |
| 🔴 | GtFwdOp | test_gt_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.81 | 2.42 | torch 303.0%, torch-compile 74.9% | - |
| 🔴 | GtFwdOp | test_gt_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.81 | 2.42 | torch 308.6%, torch-compile 75.2% | - |
| 🟡 | GtFwdOp | test_gt_manifest_bench[cnn-feat-broadcast-float32] | 0.0214 | 0.60 | 3.00 | torch 224.2%, torch-compile 85.4% | - |
| 🔴 | HardsigmoidFwdOp | test_hardsigmoid_manifest_bench[mbv3-se-gate-float16] | 0.0020 | 0.01 | 0.02 | torch 85.7%, torch-compile 68.2% | - |
| 🔴 | HardsigmoidFwdOp | test_hardsigmoid_manifest_bench[mbv3-se-gate-bfloat16] | 0.0022 | 0.01 | 0.01 | torch 79.4%, torch-compile 61.8% | - |
| 🔴 | HardsigmoidFwdOp | test_hardsigmoid_manifest_bench[mbv3-se-gate-deep-float16] | 0.0020 | 0.05 | 0.06 | torch 73.0%, torch-compile 73.0% | - |
| 🔴 | HardsigmoidFwdOp | test_hardsigmoid_manifest_bench[mbv3-se-gate-deep-bfloat16] | 0.0022 | 0.04 | 0.06 | torch 69.1%, torch-compile 67.7% | - |
| 🟡 | HardswishFwdOp | test_hardswish_manifest_bench[mbv3-stage2-float16] | 0.0130 | 2.96 | 2.96 | torch 89.2%, torch-compile 88.7% | - |
| 🟡 | HardswishFwdOp | test_hardswish_manifest_bench[mbv3-stage2-bfloat16] | 0.0133 | 2.90 | 2.90 | torch 87.5%, torch-compile 87.0% | - |
| 🟡 | HardswishFwdOp | test_hardswish_manifest_bench[mbv3-stage3-float16] | 0.0089 | 2.70 | 2.70 | torch 91.0%, torch-compile 90.3% | - |
| 🟡 | HardswishFwdOp | test_hardswish_manifest_bench[mbv3-stage3-bfloat16] | 0.0091 | 2.66 | 2.66 | torch 89.7%, torch-compile 89.0% | - |
| 🔵 | HardtanhFwdOp | test_hardtanh_manifest_bench[bounded-hidden-float16] | 0.0104 | 0.81 | 3.23 | torch 108.3%, torch-compile 100.0% | - |
| 🔵 | HardtanhFwdOp | test_hardtanh_manifest_bench[bounded-hidden-bfloat16] | 0.0104 | 0.81 | 3.24 | torch 103.4%, torch-compile 100.9% | - |
| 🔵 | HardtanhFwdOp | test_hardtanh_manifest_bench[bounded-conv-feat-float16] | 0.0146 | 0.88 | 3.52 | torch 111.0%, torch-compile 100.4% | - |
| 🔵 | HardtanhFwdOp | test_hardtanh_manifest_bench[bounded-conv-feat-bfloat16] | 0.0146 | 0.88 | 3.52 | torch 104.4%, torch-compile 101.3% | - |
| 🔴 | InfNormFwdOp | test_inf_norm_bench[hidden-state-inf-float16] | 0.0302 | 0.56 | 0.56 | flaggems 25.4%, torch 164.4%, torch-compile 35.2% | - |
| 🔴 | InfNormFwdOp | test_inf_norm_bench[hidden-state-inf-bfloat16] | 0.0306 | 0.55 | 0.55 | flaggems 25.8%, torch 163.7%, torch-compile 36.2% | - |
| 🔴 | InfNormFwdOp | test_inf_norm_bench[long-seq-inf-bfloat16] | 0.0177 | 0.24 | 0.24 | flaggems 77.4%, torch 97.7%, torch-compile 28.3% | - |
| 🔴 | InfNormFwdOp | test_inf_norm_bench[3d-multidim-reduce-float16] | 0.0216 | 0.19 | 0.19 | flaggems 58.7%, torch 89.2%, torch-compile 24.1% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[image-affine-float16] | 0.0035 | 1.52 | 1.21 | flaggems 107.4%, torch 600.0%, torch-compile 88.9% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[image-affine-bfloat16] | 0.0034 | 1.53 | 1.23 | flaggems 108.4%, torch 604.7%, torch-compile 87.8% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[wider-channel-affine-float16] | 0.0035 | 1.16 | 0.93 | flaggems 102.8%, torch 596.3%, torch-compile 83.3% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[tail-spatial-affine-float16] | 0.0027 | 0.43 | 0.35 | flaggems 106.0%, torch 418.0%, torch-compile 90.4% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[image-float16] | 0.0034 | 0.94 | 1.25 | flaggems 102.9%, torch 505.7%, torch-compile 87.6% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[image-bfloat16] | 0.0034 | 0.93 | 1.24 | flaggems 102.8%, torch 502.8%, torch-compile 85.9% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[wider-channel-float16] | 0.0033 | 0.72 | 0.96 | flaggems 99.0%, torch 486.5%, torch-compile 82.7% | - |
| 🟡 | InstanceNormFwdOp | test_instance_norm_bench[tail-spatial-float16] | 0.0025 | 0.27 | 0.36 | flaggems 103.8%, torch 326.6%, torch-compile 89.9% | - |
| 🔴 | IsfiniteFwdOp | test_isfinite_bench[elementwise-16M-float16] | 0.0205 | 0.82 | 2.46 | torch 309.2%, torch-compile 73.3% | - |
| 🔴 | IsfiniteFwdOp | test_isfinite_bench[elementwise-16M-bfloat16] | 0.0204 | 0.82 | 2.46 | torch 310.3%, torch-compile 73.5% | - |
| 🟡 | IsfiniteFwdOp | test_isfinite_bench[elementwise-16M-float32] | 0.0266 | 0.63 | 3.15 | torch 361.6%, torch-compile 87.7% | - |
| 🔴 | IsfiniteFwdOp | test_isfinite_bench[elementwise-256M-float16] | 0.2731 | 0.98 | 2.95 | torch 334.1%, torch-compile 72.1% | - |
| 🔴 | IsfiniteFwdOp | test_isfinite_bench[elementwise-256M-bfloat16] | 0.2731 | 0.98 | 2.95 | torch 335.2%, torch-compile 72.0% | - |
| 🔴 | IsinfFwdOp | test_isinf_bench[elementwise-16M-float16] | 0.0206 | 0.81 | 2.44 | torch 152.0%, torch-compile 73.5% | - |
| 🔴 | IsinfFwdOp | test_isinf_bench[elementwise-16M-bfloat16] | 0.0206 | 0.82 | 2.45 | torch 152.7%, torch-compile 73.9% | - |
| 🟡 | IsinfFwdOp | test_isinf_bench[elementwise-16M-float32] | 0.0267 | 0.63 | 3.14 | torch 214.0%, torch-compile 87.4% | - |
| 🔴 | IsinfFwdOp | test_isinf_bench[elementwise-256M-float16] | 0.2762 | 0.97 | 2.92 | torch 162.9%, torch-compile 72.0% | - |
| 🔴 | IsinfFwdOp | test_isinf_bench[elementwise-256M-bfloat16] | 0.2753 | 0.98 | 2.93 | torch 163.8%, torch-compile 72.7% | - |
| 🔴 | IsnanFwdOp | test_isnan_bench[elementwise-16M-float16] | 0.0204 | 0.82 | 2.46 | torch 75.1%, torch-compile 73.7% | - |
| 🔴 | IsnanFwdOp | test_isnan_bench[elementwise-16M-bfloat16] | 0.0205 | 0.82 | 2.46 | torch 75.7%, torch-compile 74.0% | - |
| 🟡 | IsnanFwdOp | test_isnan_bench[elementwise-16M-float32] | 0.0266 | 0.63 | 3.15 | torch 88.1%, torch-compile 87.7% | - |
| 🔴 | IsnanFwdOp | test_isnan_bench[elementwise-256M-float16] | 0.2731 | 0.98 | 2.95 | torch 73.8%, torch-compile 72.2% | - |
| 🔴 | IsnanFwdOp | test_isnan_bench[elementwise-256M-bfloat16] | 0.2730 | 0.98 | 2.95 | torch 74.7%, torch-compile 72.7% | - |
| 🔵 | L1NormFwdOp | test_l1_norm_bench[hidden-state-l1-float16] | 0.0077 | 2.18 | 2.19 | flaggems 195.4%, torch 643.8%, torch-compile 108.7% | - |
| 🔵 | L1NormFwdOp | test_l1_norm_bench[hidden-state-l1-bfloat16] | 0.0077 | 2.17 | 2.17 | flaggems 198.3%, torch 642.1%, torch-compile 108.7% | - |
| 🟡 | L1NormFwdOp | test_l1_norm_bench[long-seq-l1-bfloat16] | 0.0052 | 0.81 | 0.81 | flaggems 715.5%, torch 328.6%, torch-compile 87.6% | - |
| 🔴 | L1NormFwdOp | test_l1_norm_bench[3d-multidim-reduce-float16] | 0.0113 | 0.37 | 0.37 | flaggems 217.2%, torch 170.9%, torch-compile 41.0% | - |
| 🔵 | L2NormFwdOp | test_l2_norm_bench[hidden-state-l2-float16] | 0.0077 | 2.17 | 2.17 | flaggems 101.6%, torch 636.6%, torch-compile 112.0% | - |
| 🔵 | L2NormFwdOp | test_l2_norm_bench[hidden-state-l2-bfloat16] | 0.0078 | 2.16 | 2.16 | flaggems 100.8%, torch 639.5%, torch-compile 113.2% | - |
| 🟡 | L2NormFwdOp | test_l2_norm_bench[long-seq-l2-bfloat16] | 0.0052 | 0.81 | 0.81 | flaggems 261.1%, torch 326.9%, torch-compile 91.4% | - |
| 🔴 | L2NormFwdOp | test_l2_norm_bench[3d-multidim-reduce-float16] | 0.0114 | 0.37 | 0.37 | flaggems 118.5%, torch 168.8%, torch-compile 42.7% | - |
| 🟡 | LayerNormFwdOp | test_layer_norm_bench[llama-8b-prefill-float16] | 0.0137 | 3.06 | 2.45 | flaggems 95.3%, flashinfer 155.2%, torch 154.6%, torch-compile 168.5% | - |
| 🟡 | LayerNormFwdOp | test_layer_norm_bench[llama-8b-prefill-bfloat16] | 0.0149 | 2.81 | 2.25 | flaggems 92.3%, flashinfer 143.1%, torch 143.0%, torch-compile 164.6% | - |
| 🔵 | LayerNormFwdOp | test_layer_norm_bench[llama-8b-decode-bfloat16] | 0.0027 | 0.01 | 0.01 | flaggems 103.5%, flashinfer 111.8%, torch 409.4%, torch-compile 115.3% | - |
| 🟡 | LayerNormFwdOp | test_layer_norm_bench[llama-70b-prefill-float16] | 0.0260 | 3.23 | 2.58 | flaggems 98.8%, flashinfer 179.1%, torch 155.2%, torch-compile 118.1% | - |
| 🔵 | LayerNormFwdOp | test_layer_norm_bench[llama-70b-prefill-bfloat16] | 0.0264 | 3.17 | 2.54 | flaggems 104.6%, flashinfer 176.3%, torch 152.8%, torch-compile 126.4% | - |
| 🔵 | LayerNormFwdOp | test_layer_norm_bench[llama-70b-decode-bfloat16] | 0.0034 | 0.01 | 0.02 | flaggems 122.4%, flashinfer 119.6%, torch 585.1%, torch-compile 108.4% | - |
| 🟡 | LayerNormFwdOp | test_layer_norm_bench[llama-405b-prefill-float16] | 0.0501 | 3.35 | 2.68 | flaggems 96.4%, flashinfer 156.5%, torch 147.3%, torch-compile 93.3% | - |
| 🟡 | LayerNormFwdOp | test_layer_norm_bench[llama-405b-prefill-bfloat16] | 0.0509 | 3.30 | 2.64 | flaggems 99.2%, flashinfer 154.1%, torch 146.1%, torch-compile 99.3% | - |
| 🔵 | LayerNormFwdOp | test_layer_norm_bench[llama-405b-decode-bfloat16] | 0.0043 | 0.02 | 0.03 | flaggems 142.5%, flashinfer 140.7%, torch 885.4%, torch-compile 127.6% | - |
| 🟡 | LeFwdOp | test_comparison_bench[le-1024x4096-float16-le] | 0.0080 | 0.52 | 2.61 | torch 96.0%, torch-compile 96.0% | - |
| 🟡 | LeFwdOp | test_le_manifest_bench[hidden-state-prefill-float16] | 0.0140 | 0.60 | 2.99 | torch 92.3%, torch-compile 92.0% | - |
| 🟡 | LeFwdOp | test_le_manifest_bench[hidden-state-prefill-bfloat16] | 0.0140 | 0.60 | 2.99 | torch 94.3%, torch-compile 93.8% | - |
| 🔵 | LeFwdOp | test_le_manifest_bench[hidden-state-prefill-float32] | 0.0223 | 0.38 | 3.38 | torch 100.4%, torch-compile 111.5% | - |
| 🔴 | LeFwdOp | test_le_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.81 | 2.42 | torch 311.9%, torch-compile 74.7% | - |
| 🔴 | LeFwdOp | test_le_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.81 | 2.42 | torch 317.4%, torch-compile 74.9% | - |
| 🟡 | LeFwdOp | test_le_manifest_bench[cnn-feat-broadcast-float32] | 0.0214 | 0.60 | 3.00 | torch 229.9%, torch-compile 86.5% | - |
| 🔵 | LeakyReluFwdOp | test_leaky_relu_manifest_bench[gan-feat-float16] | 0.0184 | 1.82 | 3.64 | torch 100.2%, torch-compile 100.0% | - |
| 🟡 | LeakyReluFwdOp | test_leaky_relu_manifest_bench[gan-feat-bfloat16] | 0.0184 | 1.82 | 3.64 | torch 100.2%, torch-compile 99.8% | - |
| 🔵 | LeakyReluFwdOp | test_leaky_relu_manifest_bench[gan-feat-deep-float16] | 0.0103 | 1.62 | 3.25 | torch 100.6%, torch-compile 100.3% | - |
| 🔵 | LeakyReluFwdOp | test_leaky_relu_manifest_bench[gan-feat-deep-bfloat16] | 0.0104 | 1.62 | 3.24 | torch 100.3%, torch-compile 100.0% | - |
| 🔵 | LerpFwdOp | test_binary_arith_bench[lerp-1024x4096-float16-float16-LerpFwdOp-<lambda>-normal] | 0.0082 | 0.51 | 3.08 | torch 101.2%, torch-compile 100.4% | - |
| 🟡 | LerpFwdOp | test_binary_arith_bench[lerp-1024x10240-float16-float16-LerpFwdOp-<lambda>-normal] | 0.0177 | 0.59 | 3.55 | torch 100.2%, torch-compile 99.8% | - |
| 🟡 | LerpFwdOp | test_lerp_manifest_bench[hidden-state-prefill-float16] | 0.0148 | 1.69 | 3.39 | torch 99.8%, torch-compile 99.6% | - |
| 🟡 | LerpFwdOp | test_lerp_manifest_bench[hidden-state-prefill-bfloat16] | 0.0146 | 1.72 | 3.44 | torch 100.2%, torch-compile 99.8% | - |
| 🟡 | LerpFwdOp | test_lerp_manifest_bench[hidden-state-prefill-float32] | 0.0264 | 0.95 | 3.81 | torch 99.2%, torch-compile 98.9% | - |
| 🟡 | LerpFwdOp | test_lerp_manifest_bench[cnn-feat-broadcast-float16] | 0.0165 | 2.33 | 3.11 | torch 288.4%, torch-compile 87.2% | - |
| 🟡 | LerpFwdOp | test_lerp_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0166 | 2.32 | 3.09 | torch 290.9%, torch-compile 86.3% | - |
| 🟡 | LerpFwdOp | test_lerp_manifest_bench[cnn-feat-broadcast-float32] | 0.0267 | 1.44 | 3.85 | torch 190.5%, torch-compile 99.4% | - |
| 🟡 | LerpTensorFwdOp | test_lerp_tensor_manifest_bench[elementwise-16M-float16] | 0.0350 | 1.44 | 3.83 | torch 99.5%, torch-compile 99.5% | - |
| 🟡 | LerpTensorFwdOp | test_lerp_tensor_manifest_bench[elementwise-16M-bfloat16] | 0.0350 | 1.44 | 3.83 | torch 99.5%, torch-compile 99.3% | - |
| 🟡 | LerpTensorFwdOp | test_lerp_tensor_manifest_bench[elementwise-16M-float32] | 0.0656 | 0.77 | 4.09 | torch 99.3%, torch-compile 99.4% | - |
| 🔵 | LerpTensorFwdOp | test_lerp_tensor_manifest_bench[elementwise-256M-float16] | 0.4857 | 1.66 | 4.42 | torch 100.0%, torch-compile 100.0% | - |
| 🔵 | LerpTensorFwdOp | test_lerp_tensor_manifest_bench[elementwise-256M-bfloat16] | 0.4860 | 1.66 | 4.42 | torch 100.0%, torch-compile 100.0% | - |
| 🟡 | Log1pFwdOp | test_log1p_bench[elementwise-16M-float16] | 0.0284 | 1.18 | 2.36 | torch 92.5%, torch-compile 89.6% | - |
| 🟡 | Log1pFwdOp | test_log1p_bench[elementwise-16M-bfloat16] | 0.0292 | 1.15 | 2.29 | torch 91.5%, torch-compile 89.4% | - |
| 🟡 | Log1pFwdOp | test_log1p_bench[elementwise-16M-float32] | 0.0364 | 0.92 | 3.68 | torch 93.2%, torch-compile 93.2% | - |
| 🟡 | Log1pFwdOp | test_log1p_bench[elementwise-256M-float16] | 0.4148 | 1.29 | 2.59 | torch 91.6%, torch-compile 88.9% | - |
| 🟡 | Log1pFwdOp | test_log1p_bench[elementwise-256M-bfloat16] | 0.4337 | 1.24 | 2.48 | torch 89.5%, torch-compile 88.0% | - |
| 🟡 | LogFwdOp | test_log_bench[elementwise-16M-float16] | 0.0277 | 0.60 | 2.42 | torch 98.3%, torch-compile 98.0% | - |
| 🟡 | LogFwdOp | test_log_bench[elementwise-16M-bfloat16] | 0.0289 | 0.58 | 2.32 | torch 97.1%, torch-compile 96.7% | - |
| 🟡 | LogFwdOp | test_log_bench[elementwise-16M-float32] | 0.0360 | 0.47 | 3.72 | torch 95.2%, torch-compile 94.8% | - |
| 🟡 | LogFwdOp | test_log_bench[elementwise-256M-float16] | 0.4070 | 0.66 | 2.64 | torch 97.5%, torch-compile 98.5% | - |
| 🟡 | LogFwdOp | test_log_bench[elementwise-256M-bfloat16] | 0.4279 | 0.63 | 2.51 | torch 96.4%, torch-compile 95.9% | - |
| 🟢 | LogSoftmaxFwdOp | test_log_softmax_bench[attn-weights-4k-float16] | 0.0087 | 2.40 | 1.92 | flaggems 228.6%, torch 196.7%, torch-compile 170.3% | - |
| 🟢 | LogSoftmaxFwdOp | test_log_softmax_bench[attn-weights-4k-bfloat16] | 0.0087 | 2.40 | 1.92 | flaggems 233.9%, torch 196.3%, torch-compile 176.6% | - |
| 🔵 | LogSoftmaxFwdOp | test_log_softmax_bench[attn-weights-4k-float32] | 0.0120 | 1.74 | 2.79 | flaggems 170.7%, torch 153.7%, torch-compile 131.1% | - |
| 🔵 | LogSoftmaxFwdOp | test_log_softmax_bench[attn-weights-32k-bfloat16] | 0.0585 | 2.87 | 2.29 | flaggems 427.6%, torch 105.1%, torch-compile 122.6% | - |
| 🔴 | LogSoftmaxFwdOp | test_log_softmax_bench[lm-head-logits-float16] | 0.0287 | 0.07 | 0.06 | flaggems 1465.4%, torch 77.1%, torch-compile 33.7% | - |
| 🔴 | LogSoftmaxFwdOp | test_log_softmax_bench[lm-head-logits-bfloat16] | 0.0269 | 0.08 | 0.06 | flaggems 1568.2%, torch 84.9%, torch-compile 35.9% | - |
| 🔴 | LogSoftmaxFwdOp | test_log_softmax_bench[lm-head-logits-float32] | 0.0366 | 0.06 | 0.09 | flaggems 1102.9%, torch 96.2%, torch-compile 25.2% | - |
| 🔵 | LogSumExpFwdOp | test_logsumexp_bench[attn-weights-4k-float16] | 0.0074 | 2.26 | 1.13 | torch 657.3%, torch-compile 135.8% | - |
| 🔵 | LogSumExpFwdOp | test_logsumexp_bench[attn-weights-4k-bfloat16] | 0.0075 | 2.25 | 1.13 | torch 667.0%, torch-compile 134.8% | - |
| 🔵 | LogSumExpFwdOp | test_logsumexp_bench[attn-weights-32k-bfloat16] | 0.0327 | 4.10 | 2.05 | torch 605.8%, torch-compile 126.9% | - |
| 🔴 | LogSumExpFwdOp | test_logsumexp_bench[lm-head-logits-float16] | 0.0141 | 0.12 | 0.06 | torch 329.5%, torch-compile 76.9% | - |
| 🔴 | LogSumExpFwdOp | test_logsumexp_bench[lm-head-logits-bfloat16] | 0.0164 | 0.10 | 0.05 | torch 287.5%, torch-compile 64.0% | - |
| 🔴 | LogSumExpFwdOp | test_logsumexp_bench[3d-multidim-reduce-float16] | 0.0126 | 0.66 | 0.33 | torch 326.8%, torch-compile 78.7% | - |
| 🔴 | LogicalAndFwdOp | test_logical_bench[logical_and-1024x4096-float16-LogicalAndFwdOp-logical_and] | 0.0079 | 0.53 | 2.64 | torch 74.2%, torch-compile 70.6% | - |
| 🔴 | LogicalAndFwdOp | test_logical_bench[logical_and-1024x10240-float16-LogicalAndFwdOp-logical_and] | 0.0171 | 0.61 | 3.07 | torch 71.7%, torch-compile 63.7% | - |
| 🔵 | LogicalAndFwdOp | test_logical_and_manifest_bench[hidden-state-prefill-bool] | 0.0082 | 3.06 | 3.06 | torch 123.0%, torch-compile 107.4% | - |
| 🟡 | LogicalAndFwdOp | test_logical_and_manifest_bench[hidden-state-prefill-float16] | 0.0140 | 1.80 | 3.01 | torch 96.1%, torch-compile 95.7% | - |
| 🟡 | LogicalAndFwdOp | test_logical_and_manifest_bench[hidden-state-prefill-bfloat16] | 0.0142 | 1.78 | 2.96 | torch 92.3%, torch-compile 91.6% | - |
| 🟡 | LogicalAndFwdOp | test_logical_and_manifest_bench[hidden-state-prefill-float32] | 0.0226 | 1.11 | 3.34 | torch 99.4%, torch-compile 99.6% | - |
| 🔵 | LogicalAndFwdOp | test_logical_and_manifest_bench[cnn-feat-broadcast-bool] | 0.0081 | 4.78 | 3.19 | torch 560.3%, torch-compile 123.4% | - |
| 🔴 | LogicalAndFwdOp | test_logical_and_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 2.42 | 2.42 | torch 294.4%, torch-compile 76.3% | - |
| 🔴 | LogicalAndFwdOp | test_logical_and_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 2.42 | 2.42 | torch 302.0%, torch-compile 75.5% | - |
| 🟡 | LogicalAndFwdOp | test_logical_and_manifest_bench[cnn-feat-broadcast-float32] | 0.0213 | 1.81 | 3.02 | torch 218.5%, torch-compile 85.9% | - |
| 🔵 | LogicalNotFwdOp | test_logical_not_bench[elementwise-16M-bool] | 0.0101 | 1.66 | 3.33 | torch 128.9%, torch-compile 120.0% | - |
| 🔴 | LogicalNotFwdOp | test_logical_not_bench[elementwise-16M-float16] | 0.0188 | 0.89 | 2.68 | torch 81.1%, torch-compile 79.9% | - |
| 🟡 | LogicalNotFwdOp | test_logical_not_bench[elementwise-16M-float32] | 0.0261 | 0.64 | 3.22 | torch 89.8%, torch-compile 89.7% | - |
| 🔵 | LogicalNotFwdOp | test_logical_not_bench[elementwise-256M-bool] | 0.1268 | 2.12 | 4.23 | torch 143.2%, torch-compile 130.1% | - |
| 🔴 | LogicalOrFwdOp | test_logical_bench[logical_or-1024x4096-float16-LogicalOrFwdOp-logical_or] | 0.0079 | 0.53 | 2.64 | torch 71.4%, torch-compile 115.7% | - |
| 🔴 | LogicalOrFwdOp | test_logical_bench[logical_or-1024x10240-float16-LogicalOrFwdOp-logical_or] | 0.0171 | 0.61 | 3.06 | torch 62.1%, torch-compile 59.6% | - |
| 🔵 | LogicalOrFwdOp | test_logical_or_manifest_bench[hidden-state-prefill-bool] | 0.0082 | 3.07 | 3.07 | torch 110.5%, torch-compile 107.8% | - |
| 🟡 | LogicalOrFwdOp | test_logical_or_manifest_bench[hidden-state-prefill-float16] | 0.0141 | 1.78 | 2.97 | torch 94.1%, torch-compile 94.1% | - |
| 🟡 | LogicalOrFwdOp | test_logical_or_manifest_bench[hidden-state-prefill-bfloat16] | 0.0140 | 1.80 | 2.99 | torch 92.8%, torch-compile 92.7% | - |
| 🔵 | LogicalOrFwdOp | test_logical_or_manifest_bench[hidden-state-prefill-float32] | 0.0224 | 1.12 | 3.37 | torch 100.1%, torch-compile 100.0% | - |
| 🔵 | LogicalOrFwdOp | test_logical_or_manifest_bench[cnn-feat-broadcast-bool] | 0.0081 | 4.76 | 3.17 | torch 546.6%, torch-compile 126.5% | - |
| 🔴 | LogicalOrFwdOp | test_logical_or_manifest_bench[cnn-feat-broadcast-float16] | 0.0164 | 2.35 | 2.35 | torch 290.8%, torch-compile 73.2% | - |
| 🔴 | LogicalOrFwdOp | test_logical_or_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0164 | 2.36 | 2.36 | torch 298.2%, torch-compile 74.0% | - |
| 🟡 | LogicalOrFwdOp | test_logical_or_manifest_bench[cnn-feat-broadcast-float32] | 0.0214 | 1.80 | 3.00 | torch 217.2%, torch-compile 86.5% | - |
| 🟡 | LtFwdOp | test_comparison_bench[lt-1024x4096-float16-lt] | 0.0080 | 0.52 | 2.62 | torch 96.8%, torch-compile 96.6% | - |
| 🟡 | LtFwdOp | test_lt_manifest_bench[hidden-state-prefill-float16] | 0.0141 | 0.59 | 2.97 | torch 93.0%, torch-compile 92.8% | - |
| 🟡 | LtFwdOp | test_lt_manifest_bench[hidden-state-prefill-bfloat16] | 0.0141 | 0.59 | 2.97 | torch 94.0%, torch-compile 93.9% | - |
| 🔵 | LtFwdOp | test_lt_manifest_bench[hidden-state-prefill-float32] | 0.0223 | 0.38 | 3.38 | torch 101.2%, torch-compile 100.9% | - |
| 🔴 | LtFwdOp | test_lt_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.81 | 2.42 | torch 311.2%, torch-compile 74.3% | - |
| 🔴 | LtFwdOp | test_lt_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.81 | 2.43 | torch 317.9%, torch-compile 76.8% | - |
| 🟡 | LtFwdOp | test_lt_manifest_bench[cnn-feat-broadcast-float32] | 0.0214 | 0.60 | 3.00 | torch 230.5%, torch-compile 86.1% | - |
| 🟡 | MHCPostFwdOp | test_mhc_post_bench[post-small-bfloat16] | 0.0013 | 0.01 | 0.02 | torch-ref 783.4%, torch-compile 92.9% | - |
| 🔵 | MHCPostFwdOp | test_mhc_post_bench[post-medium-bfloat16] | 0.0014 | 0.02 | 0.05 | torch-ref 781.8%, torch-compile 115.9% | - |
| 🔵 | MHCPostFwdOp | test_mhc_post_bench[post-large-bfloat16] | 0.0016 | 0.05 | 0.12 | torch-ref 708.1%, torch-compile 108.0% | - |
| 🔴 | MHCPreFwdOp | test_mhc_pre_bench[pre-small-bfloat16] | 0.0395 | 0.01 | 0.01 | torch-ref 150.0%, torch-compile 49.9% | - |
| 🔴 | MHCPreFwdOp | test_mhc_pre_bench[pre-medium-bfloat16] | 0.0544 | 0.02 | 0.01 | torch-ref 143.4%, torch-compile 57.7% | - |
| 🔴 | MHCPreFwdOp | test_mhc_pre_bench[pre-large-bfloat16] | 0.0716 | 0.03 | 0.02 | torch-ref 163.6%, torch-compile 79.4% | - |
| 🟡 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-2p7b-b1-s2k-bfloat16] | 0.1100 | 73.99 | 0.99 | mamba 99.0%, torch-ref 1957.4%, torch-compile 624.1% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-1p3b-b1-s8k-float16] | 0.2906 | 89.86 | 1.20 | mamba 108.0%, torch-ref 2376.9%, torch-compile 695.0% | - |
| 🟡 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-2p7b-b1-s2k-dt-bias-bfloat16] | 0.1092 | 74.58 | 0.99 | mamba 99.9%, torch-ref 1976.8%, torch-compile 631.7% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-1p3b-b1-s8k-dt-bias-float16] | 0.2900 | 90.06 | 1.20 | mamba 107.9%, torch-ref 2382.8%, torch-compile 694.7% | - |
| 🟡 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-2p7b-b1-s2k-init-states-bfloat16] | 0.1107 | 73.57 | 1.00 | mamba 99.9%, torch-ref 1944.9%, torch-compile 613.4% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-1p3b-b1-s8k-init-states-float16] | 0.2913 | 89.65 | 1.21 | mamba 107.6%, torch-ref 2370.9%, torch-compile 693.7% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-2p7b-b1-s2k-dt-bias-init-states-bfloat16] | 0.1098 | 74.16 | 1.01 | mamba 100.8%, torch-ref 1963.0%, torch-compile 619.6% | - |
| 🔵 | Mamba2FwdOp | test_mamba2_fwd_bench[mamba2-1p3b-b1-s8k-dt-bias-init-states-float16] | 0.2905 | 89.89 | 1.21 | mamba 107.7%, torch-ref 2378.4%, torch-compile 692.9% | - |
| 🟡 | MaskedFillFwdOp | test_masked_fill_tensor_manifest_bench[elementwise-16M-float16] | 0.0228 | 0.74 | 3.68 | torch 85.0%, torch-compile 99.2% | - |
| 🟡 | MaskedFillFwdOp | test_masked_fill_tensor_manifest_bench[elementwise-16M-bfloat16] | 0.0226 | 0.74 | 3.71 | torch 85.8%, torch-compile 100.0% | - |
| 🟡 | MaskedFillFwdOp | test_masked_fill_tensor_manifest_bench[elementwise-16M-float32] | 0.0380 | 0.44 | 3.97 | torch 95.2%, torch-compile 98.7% | - |
| 🔵 | MaskedFillFwdOp | test_masked_fill_tensor_manifest_bench[elementwise-256M-float16] | 0.3093 | 0.87 | 4.34 | torch 100.1%, torch-compile 100.2% | - |
| 🟡 | MaskedFillFwdOp | test_masked_fill_tensor_manifest_bench[elementwise-256M-bfloat16] | 0.3101 | 0.87 | 4.33 | torch 99.7%, torch-compile 100.0% | - |
| 🟡 | MaskedFillScalarFwdOp | test_masked_fill_scalar_manifest_bench[elementwise-16M-float16] | 0.0227 | 0.74 | 3.69 | torch 84.9%, torch-compile 99.2% | - |
| 🟡 | MaskedFillScalarFwdOp | test_masked_fill_scalar_manifest_bench[elementwise-16M-bfloat16] | 0.0225 | 0.75 | 3.73 | torch 86.6%, torch-compile 100.1% | - |
| 🟡 | MaskedFillScalarFwdOp | test_masked_fill_scalar_manifest_bench[elementwise-16M-float32] | 0.0378 | 0.44 | 3.99 | torch 96.0%, torch-compile 98.5% | - |
| 🟡 | MaskedFillScalarFwdOp | test_masked_fill_scalar_manifest_bench[elementwise-256M-float16] | 0.3100 | 0.87 | 4.33 | torch 99.8%, torch-compile 99.9% | - |
| 🟡 | MaskedFillScalarFwdOp | test_masked_fill_scalar_manifest_bench[elementwise-256M-bfloat16] | 0.3105 | 0.86 | 4.32 | torch 99.8%, torch-compile 99.9% | - |
| 🔵 | MaxPool1dFwdOp | test_max_pool1d_bench[sincnet-speaker-local-float16] | 0.0114 | 0.92 | 2.45 | torch-ref 442.3%, torch-compile 100.0% | - |
| 🔴 | MaxPool1dFwdOp | test_max_pool1d_bench[textcnn-global-float16] | 0.0135 | 0.16 | 0.31 | torch-ref 196.2%, torch-compile 27.6% | - |
| 🟡 | MaxPool1dFwdOp | test_max_pool1d_bench[ecg-cnn-dilated-bfloat16] | 0.0095 | 1.10 | 1.32 | torch-ref 371.2%, torch-compile 82.2% | - |
| 🔴 | MaxPool1dIndicesFwdOp | test_max_pool1d_indices_bench[sincnet-speaker-local-float16] | 0.0218 | 0.48 | 2.57 | torch-ref 232.2%, torch-compile 73.7% | - |
| 🔴 | MaxPool1dIndicesFwdOp | test_max_pool1d_indices_bench[textcnn-global-float16] | 0.0193 | 0.11 | 0.23 | torch-ref 137.0%, torch-compile 39.1% | - |
| 🔴 | MaxPool1dIndicesFwdOp | test_max_pool1d_indices_bench[ecg-cnn-dilated-bfloat16] | 0.0223 | 0.47 | 1.31 | torch-ref 158.4%, torch-compile 59.9% | - |
| 🔴 | MaxPool2dFwdOp | test_max_pool2d_bench[resnet-stem-float16] | 0.0472 | 1.22 | 1.36 | flaggems 166.0%, torch-ref 294.4%, torch-compile 72.0% | - |
| 🔴 | MaxPool2dFwdOp | test_max_pool2d_bench[resnet-stem-bfloat16] | 0.0471 | 1.23 | 1.36 | flaggems 166.0%, torch-ref 296.0%, torch-compile 72.2% | - |
| 🟡 | MaxPool2dFwdOp | test_max_pool2d_bench[resnet-stem-float32] | 0.0528 | 1.09 | 2.43 | flaggems 153.8%, torch-ref 255.3%, torch-compile 93.7% | - |
| 🔵 | MaxPool2dFwdOp | test_max_pool2d_bench[vgg-block-float16] | 0.0072 | 0.89 | 2.23 | flaggems 205.3%, torch-ref 385.3%, torch-compile 100.9% | - |
| 🔵 | MaxPool2dFwdOp | test_max_pool2d_bench[vgg-block-bfloat16] | 0.0072 | 0.90 | 2.24 | flaggems 206.2%, torch-ref 388.6%, torch-compile 101.3% | - |
| 🟡 | MaxPool2dFwdOp | test_max_pool2d_bench[vgg-block-float32] | 0.0111 | 0.58 | 2.90 | flaggems 151.2%, torch-ref 250.3%, torch-compile 93.6% | - |
| 🔵 | MaxPool2dFwdOp | test_max_pool2d_bench[alexnet-ceil-float16] | 0.0088 | 1.53 | 1.75 | flaggems 256.6%, torch-ref 395.6%, torch-compile 125.2% | - |
| 🔵 | MaxPool2dFwdOp | test_max_pool2d_bench[alexnet-ceil-bfloat16] | 0.0087 | 1.54 | 1.76 | flaggems 260.1%, torch-ref 398.2%, torch-compile 125.6% | - |
| 🔵 | MaxPool2dFwdOp | test_max_pool2d_bench[alexnet-ceil-float32] | 0.0127 | 1.06 | 2.43 | flaggems 180.1%, torch-ref 269.4%, torch-compile 121.6% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[resnet-stem-float16] | 0.1123 | 0.51 | 1.03 | flaggems 69.8%, torch-ref 124.0%, torch-compile 61.6% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[resnet-stem-bfloat16] | 0.1124 | 0.51 | 1.03 | flaggems 69.6%, torch-ref 124.1%, torch-compile 62.0% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[resnet-stem-float32] | 0.1077 | 0.54 | 1.67 | flaggems 75.3%, torch-ref 125.0%, torch-compile 66.4% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[vgg-block-float16] | 0.0196 | 0.33 | 1.47 | flaggems 75.2%, torch-ref 141.4%, torch-compile 54.1% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[vgg-block-bfloat16] | 0.0195 | 0.33 | 1.49 | flaggems 76.0%, torch-ref 143.3%, torch-compile 54.6% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[vgg-block-float32] | 0.0195 | 0.33 | 2.30 | flaggems 85.9%, torch-ref 142.0%, torch-compile 64.9% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[alexnet-ceil-float16] | 0.0237 | 0.57 | 1.15 | flaggems 95.0%, torch-ref 146.4%, torch-compile 74.5% | - |
| 🔴 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[alexnet-ceil-bfloat16] | 0.0237 | 0.57 | 1.15 | flaggems 95.9%, torch-ref 146.9%, torch-compile 73.5% | - |
| 🟡 | MaxPool2dIndicesFwdOp | test_max_pool2d_indices_bench[alexnet-ceil-float32] | 0.0236 | 0.57 | 1.81 | flaggems 96.6%, torch-ref 144.7%, torch-compile 82.0% | - |
| 🔵 | MaxPool3dFwdOp | test_max_pool3d_bench[c3d-pool1-float16] | 0.0762 | 1.35 | 3.37 | cudnn 394.8%, torch-ref 679.4%, torch-compile 101.2% | - |
| 🔵 | MaxPool3dFwdOp | test_max_pool3d_bench[c3d-pool2-float16] | 0.0235 | 1.09 | 2.46 | cudnn 259.0%, torch-ref 399.9%, torch-compile 104.9% | - |
| 🟢 | MaxPool3dFwdOp | test_max_pool3d_bench[medicalnet-stem-bfloat16] | 0.1111 | 1.72 | 1.05 | cudnn 237.4%, torch-ref 301.3%, torch-compile 834.0% | - |
| 🔴 | MaxPool3dIndicesFwdOp | test_max_pool3d_indices_bench[c3d-pool1-float16] | 0.3041 | 0.34 | 1.52 | torch-ref 170.2%, torch-compile 42.5% | - |
| 🔴 | MaxPool3dIndicesFwdOp | test_max_pool3d_indices_bench[c3d-pool2-float16] | 0.0588 | 0.44 | 1.42 | torch-ref 159.4%, torch-compile 55.4% | - |
| 🔵 | MaxPool3dIndicesFwdOp | test_max_pool3d_indices_bench[medicalnet-stem-bfloat16] | 0.3315 | 0.58 | 0.52 | torch-ref 101.0%, torch-compile 614.2% | - |
| 🟡 | MaximumFwdOp | test_binary_arith_bench[maximum-1024x4096-float16-float16-MaximumFwdOp-maximum-normal] | 0.0086 | 0.49 | 2.93 | torch 101.1%, torch-compile 97.4% | - |
| 🟡 | MaximumFwdOp | test_binary_arith_bench[maximum-1024x10240-float16-float16-MaximumFwdOp-maximum-normal] | 0.0181 | 0.58 | 3.48 | torch 100.5%, torch-compile 98.8% | - |
| 🟡 | MaximumFwdOp | test_binary_arith_bench[maximum-1024x11008-float16-float16-MaximumFwdOp-maximum-normal] | 0.0189 | 0.60 | 3.58 | torch 100.5%, torch-compile 99.0% | - |
| 🟡 | MaximumFwdOp | test_maximum_manifest_bench[hidden-state-prefill-float16] | 0.0147 | 0.57 | 3.43 | torch 100.8%, torch-compile 98.6% | - |
| 🟡 | MaximumFwdOp | test_maximum_manifest_bench[hidden-state-prefill-bfloat16] | 0.0149 | 0.56 | 3.37 | torch 100.4%, torch-compile 98.3% | - |
| 🟡 | MaximumFwdOp | test_maximum_manifest_bench[hidden-state-prefill-float32] | 0.0263 | 0.32 | 3.82 | torch 100.5%, torch-compile 99.8% | - |
| 🔴 | MaximumFwdOp | test_maximum_manifest_bench[cnn-feat-broadcast-float16] | 0.0395 | 0.33 | 1.30 | torch 127.4%, torch-compile 36.5% | - |
| 🔴 | MaximumFwdOp | test_maximum_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0396 | 0.32 | 1.30 | torch 129.5%, torch-compile 35.9% | - |
| 🟡 | MaximumFwdOp | test_maximum_manifest_bench[cnn-feat-broadcast-float32] | 0.0300 | 0.43 | 3.43 | torch 177.6%, torch-compile 88.0% | - |
| 🟡 | MeanFwdOp | test_mean_bench[hidden-state-reduce-float16] | 0.0085 | 0.98 | 1.96 | flaggems 104.1%, torch 579.4%, torch-compile 97.8% | - |
| 🟡 | MeanFwdOp | test_mean_bench[hidden-state-reduce-bfloat16] | 0.0087 | 0.97 | 1.94 | flaggems 103.0%, torch 574.6%, torch-compile 97.1% | - |
| 🔴 | MeanFwdOp | test_mean_bench[long-seq-reduce-bfloat16] | 0.0052 | 0.40 | 0.80 | flaggems 73.0%, torch 323.3%, torch-compile 85.9% | - |
| 🔴 | MeanFwdOp | test_mean_bench[3d-multidim-reduce-float16] | 0.0115 | 0.18 | 0.37 | flaggems 117.9%, torch 168.2%, torch-compile 40.6% | - |
| 🔴 | MeanPoolingForwardOp | test_mean_pooling_bench[dense-mainstream] | 0.1353 | 0.50 | 1.01 | torch-ref 452.9%, torch-compile 313.7%, torch-view-mean 34.8% | - |
| 🔴 | MeanPoolingForwardOp | test_mean_pooling_bench[dense-batched] | 0.0702 | 0.48 | 0.97 | torch-ref 372.5%, torch-compile 207.8%, torch-view-mean 40.6% | - |
| 🟢 | MeanPoolingForwardOp | test_mean_pooling_bench[varlen-long] | 0.1386 | 0.48 | 0.98 | torch-ref 443.7%, torch-compile 442.8% | - |
| 🟢 | MeanPoolingForwardOp | test_mean_pooling_bench[varlen-tail] | 0.0218 | 0.41 | 0.78 | torch-ref 977.2%, torch-compile 957.9% | - |
| 🟡 | MinimumFwdOp | test_binary_arith_bench[minimum-1024x4096-float16-float16-MinimumFwdOp-minimum-normal] | 0.0086 | 0.49 | 2.91 | torch 101.1%, torch-compile 97.0% | - |
| 🟡 | MinimumFwdOp | test_binary_arith_bench[minimum-1024x10240-float16-float16-MinimumFwdOp-minimum-normal] | 0.0181 | 0.58 | 3.47 | torch 100.4%, torch-compile 98.2% | - |
| 🟡 | MinimumFwdOp | test_binary_arith_bench[minimum-1024x11008-float16-float16-MinimumFwdOp-minimum-normal] | 0.0189 | 0.60 | 3.57 | torch 100.5%, torch-compile 99.2% | - |
| 🟡 | MinimumFwdOp | test_minimum_manifest_bench[hidden-state-prefill-float16] | 0.0150 | 0.56 | 3.35 | torch 100.2%, torch-compile 98.3% | - |
| 🟡 | MinimumFwdOp | test_minimum_manifest_bench[hidden-state-prefill-bfloat16] | 0.0150 | 0.56 | 3.35 | torch 100.3%, torch-compile 98.3% | - |
| 🟡 | MinimumFwdOp | test_minimum_manifest_bench[hidden-state-prefill-float32] | 0.0265 | 0.32 | 3.79 | torch 99.8%, torch-compile 99.3% | - |
| 🔴 | MinimumFwdOp | test_minimum_manifest_bench[cnn-feat-broadcast-float16] | 0.0395 | 0.33 | 1.30 | torch 128.0%, torch-compile 36.4% | - |
| 🔴 | MinimumFwdOp | test_minimum_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0396 | 0.32 | 1.30 | torch 129.4%, torch-compile 36.3% | - |
| 🟡 | MinimumFwdOp | test_minimum_manifest_bench[cnn-feat-broadcast-float32] | 0.0301 | 0.43 | 3.41 | torch 176.8%, torch-compile 88.0% | - |
| 🟡 | MishFwdOp | test_mish_manifest_bench[yolo-p3-float16] | 0.0710 | 1.48 | 1.48 | torch 89.7%, torch-compile 103.7% | - |
| 🟡 | MishFwdOp | test_mish_manifest_bench[yolo-p3-bfloat16] | 0.0708 | 1.48 | 1.48 | torch 90.4%, torch-compile 104.5% | - |
| 🟡 | MishFwdOp | test_mish_manifest_bench[yolo-p4-float16] | 0.0371 | 1.41 | 1.41 | torch 89.5%, torch-compile 103.1% | - |
| 🟡 | MishFwdOp | test_mish_manifest_bench[yolo-p4-bfloat16] | 0.0370 | 1.42 | 1.42 | torch 91.0%, torch-compile 104.5% | - |
| 🟢 | MoeGateUpFwdOp | test_moe_gate_up_bench[deepseek-v3-decode-gate-up-bfloat16] | 3.4606 | 69.50 | 4.37 | torch-ref 191.7%, torch-compile 227.2% | - |
| 🟢 | MoeGateUpFwdOp | test_moe_gate_up_bench[deepseek-v3-prefill-gate-up-bfloat16] | 4.4032 | 436.99 | 3.55 | torch-ref 157.8%, torch-compile 614.1% | - |
| 🔵 | MoeGroupedGemmNopadFwdOp | test_moe_grouped_gemm_nopad_bench[deepseek-v3-decode-gate-up-bfloat16] | 3.7472 | 64.19 | 4.04 | torch-ref 138.1%, torch-compile 156.2% | - |
| 🔵 | MoeGroupedGemmNopadFwdOp | test_moe_grouped_gemm_nopad_bench[deepseek-v3-prefill-gate-up-bfloat16] | 4.3180 | 445.61 | 3.65 | torch-ref 125.6%, torch-compile 250.8% | - |
| 🔵 | MoeGroupedGemmNopadFwdOp | test_moe_grouped_gemm_nopad_bench[deepseek-v3-decode-down-bfloat16] | 1.9087 | 63.01 | 3.98 | torch-ref 141.1%, torch-compile 292.6% | - |
| 🔵 | MoeGroupedGemmNopadFwdOp | test_moe_grouped_gemm_nopad_bench[deepseek-v3-prefill-down-bfloat16] | 2.1535 | 446.75 | 3.77 | torch-ref 131.8%, torch-compile 1198.7% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[kimi-k2-decode-int32] | 0.0169 | 0.00 | 0.01 | triton 287.9% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[kimi-k2-small-int32] | 0.0194 | 0.00 | 0.01 | triton 247.3% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[kimi-k2-medium-int32] | 0.0217 | 0.00 | 0.01 | triton 258.3% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[kimi-k2-prefill-int32] | 0.0410 | 0.00 | 0.01 | triton 208.6% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[deepseek-v3-decode-int32] | 0.0148 | 0.00 | 0.00 | triton 227.9% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[deepseek-v3-small-int32] | 0.0153 | 0.00 | 0.00 | triton 220.1% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[deepseek-v3-medium-int32] | 0.0177 | 0.00 | 0.01 | triton 236.7% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[deepseek-v3-prefill-int32] | 0.0378 | 0.00 | 0.01 | triton 196.6% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[qwen3-decode-int32] | 0.0108 | 0.00 | 0.00 | triton 156.8% | - |
| 🔵 | MoePermuteAlignFwdOp | test_permute_align_bench[qwen3-small-int32] | 0.0121 | 0.00 | 0.00 | triton 149.9% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[qwen3-medium-int32] | 0.0141 | 0.00 | 0.00 | triton 212.3% | - |
| 🟢 | MoePermuteAlignFwdOp | test_permute_align_bench[qwen3-prefill-int32] | 0.0318 | 0.00 | 0.01 | triton 251.4% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[kimi-k2-decode-bfloat16] | 0.0106 | 0.00 | 0.01 | vllm 110.2% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[kimi-k2-small-bfloat16] | 0.0118 | 0.00 | 0.35 | vllm 117.3% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[kimi-k2-medium-bfloat16] | 0.0356 | 0.00 | 1.85 | vllm 129.2% | - |
| 🟡 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[kimi-k2-prefill-bfloat16] | 0.2854 | 0.00 | 1.85 | vllm 95.0% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-decode-bfloat16] | 0.0093 | 0.00 | 0.01 | vllm 124.8% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-small-bfloat16] | 0.0104 | 0.00 | 0.40 | vllm 132.2% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-medium-bfloat16] | 0.0337 | 0.00 | 1.96 | vllm 136.7% | - |
| 🟡 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-prefill-bfloat16] | 0.2788 | 0.00 | 1.90 | vllm 96.9% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-235b-decode-bfloat16] | 0.0080 | 0.00 | 0.02 | vllm 143.8% | - |
| 🟢 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-235b-small-bfloat16] | 0.0090 | 0.00 | 0.46 | vllm 152.8% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-235b-medium-bfloat16] | 0.0314 | 0.00 | 2.11 | vllm 146.8% | - |
| 🟡 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-235b-prefill-bfloat16] | 0.2685 | 0.00 | 1.97 | vllm 97.2% | - |
| 🟢 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-30b-decode-bfloat16] | 0.0063 | 0.00 | 0.01 | vllm 167.5% | - |
| 🟢 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-30b-small-bfloat16] | 0.0072 | 0.00 | 0.25 | vllm 173.3% | - |
| 🔵 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-30b-medium-bfloat16] | 0.0207 | 0.00 | 1.37 | vllm 139.8% | - |
| 🟡 | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-30b-prefill-bfloat16] | 0.1419 | 0.00 | 1.60 | vllm 91.4% | - |
|  | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-ep2-decode-bfloat16] | 0.0087 | 0.00 | 0.02 | - | - |
|  | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-ep2-medium-bfloat16] | 0.0280 | 0.00 | 2.36 | - | - |
|  | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[deepseek-v3-ep2-prefill-bfloat16] | 0.2100 | 0.00 | 2.52 | - | - |
|  | MoePermuteNopadFwdOp | test_moe_permute_nopad_bench[qwen3-235b-ep2-medium-bfloat16] | 0.0264 | 0.00 | 2.50 | - | - |
| 🟢 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[large-hidden-decode-bfloat16] | 0.0070 | 0.02 | 0.02 | vllm 237.0% | - |
| 🟢 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[large-hidden-small-bfloat16] | 0.0078 | 0.47 | 0.53 | vllm 229.4% | - |
| 🔵 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[large-hidden-medium-bfloat16] | 0.0214 | 2.75 | 3.09 | vllm 137.1% | - |
| 🔵 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[large-hidden-prefill-bfloat16] | 0.1330 | 3.53 | 3.98 | vllm 104.7% | - |
| 🟢 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[small-hidden-decode-bfloat16] | 0.0057 | 0.01 | 0.01 | vllm 158.2% | - |
| 🟢 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[small-hidden-small-bfloat16] | 0.0065 | 0.24 | 0.27 | vllm 152.4% | - |
| 🔵 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[small-hidden-medium-bfloat16] | 0.0116 | 2.18 | 2.45 | vllm 128.1% | - |
| 🔵 | MoeUnpermuteFwdOp | test_moe_unpermute_bench[small-hidden-prefill-bfloat16] | 0.0615 | 3.27 | 3.68 | vllm 109.6% | - |
| 🔵 | MulFwdOp | test_binary_arith_bench[mul-1024x4096-float16-float16-MulFwdOp-mul-normal] | 0.0084 | 0.50 | 2.99 | torch 101.9%, torch-compile 100.0% | - |
| 🟡 | MulFwdOp | test_binary_arith_bench[mul-1024x10240-float16-float16-MulFwdOp-mul-normal] | 0.0176 | 0.59 | 3.57 | torch 100.7%, torch-compile 99.9% | - |
| 🔵 | MulFwdOp | test_binary_arith_bench[mul-1024x11008-float16-float16-MulFwdOp-mul-normal] | 0.0185 | 0.61 | 3.65 | torch 100.4%, torch-compile 100.0% | - |
| 🔵 | MulFwdOp | test_mul_manifest_bench[hidden-state-prefill-float16] | 0.0149 | 0.56 | 3.38 | torch 100.0%, torch-compile 100.0% | - |
| 🟡 | MulFwdOp | test_mul_manifest_bench[hidden-state-prefill-bfloat16] | 0.0147 | 0.57 | 3.42 | torch 100.2%, torch-compile 99.8% | - |
| 🟡 | MulFwdOp | test_mul_manifest_bench[hidden-state-prefill-float32] | 0.0265 | 0.32 | 3.80 | torch 99.4%, torch-compile 99.4% | - |
| 🟡 | MulFwdOp | test_mul_manifest_bench[cnn-feat-broadcast-float16] | 0.0165 | 0.78 | 3.11 | torch 275.4%, torch-compile 86.3% | - |
| 🟡 | MulFwdOp | test_mul_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0165 | 0.78 | 3.12 | torch 279.9%, torch-compile 88.0% | - |
| 🔵 | MulFwdOp | test_mul_manifest_bench[cnn-feat-broadcast-float32] | 0.0265 | 0.48 | 3.87 | torch 185.8%, torch-compile 100.1% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-8b-short-float16] | 0.2437 | 88.12 | 0.48 | fa3 58.9% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-8b-short-bfloat16] | 0.4559 | 47.10 | 0.26 | fa3 31.4% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-8b-long-float16] | 0.9025 | 190.36 | 0.26 | fa3 61.1% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-8b-long-bfloat16] | 1.3119 | 130.96 | 0.18 | fa3 41.9% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-70b-short-float16] | 0.2442 | 87.94 | 0.48 | fa3 58.6% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-70b-short-bfloat16] | 0.4567 | 47.02 | 0.26 | fa3 31.3% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-70b-long-float16] | 0.8921 | 192.59 | 0.26 | fa3 62.1% | - |
| 🔴 | MultiHeadAttentionBwdOp | test_mha_bwd_bench[llama-70b-long-bfloat16] | 1.1018 | 155.92 | 0.21 | fa3 49.9% | - |
| 🟢 | MultiHeadAttentionDecodePagedWithKVCacheFwdOp | test_mha_decode_paged_bench[single-token-page128-float16] | 0.0060 | 0.70 | 0.70 | flashinfer 152.8% | - |
| 🟢 | MultiHeadAttentionDecodePagedWithKVCacheFwdOp | test_mha_decode_paged_bench[batch2-page256-float16] | 0.0058 | 0.72 | 0.36 | fa3 318.2%, flashinfer 167.1% | - |
| 🟢 | MultiHeadAttentionDecodePagedWithKVCacheFwdOp | test_mha_decode_paged_bench[longer-cache-float16] | 0.0052 | 0.40 | 0.40 | fa3 346.9%, flashinfer 183.2% | - |
| 🟢 | MultiHeadAttentionDecodePagedWithKVCacheFwdOp | test_mha_decode_paged_bench[shorter-cache-float16] | 0.0046 | 0.23 | 0.23 | fa3 390.9%, flashinfer 201.4% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-8b-4k-float16] | 0.5117 | 4.20 | 4.20 | fa3 100.3%, flashinfer 103.4% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-8b-4k-bfloat16] | 0.5105 | 4.21 | 4.21 | fa3 100.2%, flashinfer 103.8% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-8b-32k-float16] | 0.9807 | 4.38 | 4.38 | fa3 101.1%, flashinfer 101.9% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-8b-32k-bfloat16] | 0.9813 | 4.38 | 4.38 | fa3 100.6%, flashinfer 101.7% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-70b-4k-float16] | 0.5140 | 4.18 | 4.18 | fa3 100.2%, flashinfer 103.3% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-70b-4k-bfloat16] | 0.5141 | 4.18 | 4.18 | fa3 100.2%, flashinfer 103.1% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-70b-32k-float16] | 0.9801 | 4.38 | 4.38 | fa3 100.7%, flashinfer 101.9% | - |
| 🔵 | MultiHeadAttentionDecodeWithKVCacheFwdOp | test_mha_decode_bench[llama-70b-32k-bfloat16] | 0.9807 | 4.38 | 4.38 | fa3 100.6%, flashinfer 101.6% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-8b-short-float16] | 0.0426 | 201.68 | 1.58 | fa3 81.7%, flashinfer 96.5% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-8b-short-bfloat16] | 0.0423 | 203.20 | 1.59 | fa3 83.6%, flashinfer 96.1% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-8b-long-float16] | 0.1687 | 407.41 | 0.80 | fa3 82.3%, flashinfer 96.7% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-8b-long-bfloat16] | 0.1675 | 410.21 | 0.80 | fa3 81.5%, flashinfer 96.9% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-70b-short-float16] | 0.0426 | 201.75 | 1.58 | fa3 82.8%, flashinfer 96.7% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-70b-short-bfloat16] | 0.0428 | 200.70 | 1.57 | fa3 82.5%, flashinfer 96.0% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-70b-long-float16] | 0.1693 | 405.95 | 0.79 | fa3 82.7%, flashinfer 96.7% | - |
| 🟡 | MultiHeadAttentionFwdOp | test_mha_fwd_bench[llama-70b-long-bfloat16] | 0.1670 | 411.39 | 0.80 | fa3 81.8%, flashinfer 97.6% | - |
| 🟢 | MultiHeadLatentAttentionDecodeWithKVCacheFwdOp | test_mla_decode_bench[deepseek-v2-4k-float16] | 0.0373 | 288.03 | 1.42 | torch-ref 441.4%, torch-compile 342.1% | - |
| 🟢 | MultiHeadLatentAttentionDecodeWithKVCacheFwdOp | test_mla_decode_bench[deepseek-v2-4k-bfloat16] | 0.0374 | 286.79 | 1.41 | torch-ref 437.5%, torch-compile 350.1% | - |
| 🟢 | MultiHeadLatentAttentionDecodeWithKVCacheFwdOp | test_mla_decode_bench[deepseek-v2-32k-float16] | 0.1189 | 180.59 | 0.85 | torch-ref 230.4%, torch-compile 211.9% | - |
| 🟢 | MultiHeadLatentAttentionDecodeWithKVCacheFwdOp | test_mla_decode_bench[deepseek-v2-32k-bfloat16] | 0.1189 | 180.59 | 0.85 | torch-ref 234.5%, torch-compile 215.1% | - |
| 🟢 | MultiHeadLatentAttentionDecodeWithKVCacheFwdOp | test_mla_decode_bench[deepseek-v3-4k-bfloat16] | 0.0216 | 248.18 | 1.22 | torch-ref 392.6%, torch-compile 323.8% | - |
| 🔵 | MultiHeadLatentAttentionDecodeWithKVCacheFwdOp | test_mla_decode_bench[deepseek-v3-32k-bfloat16] | 0.1180 | 91.02 | 0.43 | torch-ref 145.2%, torch-compile 136.9% | - |
| 🟡 | NanToNumFwdOp | test_nan_to_num_manifest_bench[elementwise-16M-float16] | 0.0189 | 5.31 | 3.54 | torch 101.5%, torch-compile 98.0% | - |
| 🟡 | NanToNumFwdOp | test_nan_to_num_manifest_bench[elementwise-16M-bfloat16] | 0.0189 | 5.33 | 3.55 | torch 101.8%, torch-compile 98.3% | - |
| 🔵 | NanToNumFwdOp | test_nan_to_num_manifest_bench[elementwise-16M-float32] | 0.0340 | 2.96 | 3.95 | torch 100.3%, torch-compile 100.2% | - |
| 🟡 | NanToNumFwdOp | test_nan_to_num_manifest_bench[elementwise-256M-float16] | 0.2650 | 6.08 | 4.05 | torch 103.5%, torch-compile 97.7% | - |
| 🟡 | NanToNumFwdOp | test_nan_to_num_manifest_bench[elementwise-256M-bfloat16] | 0.2640 | 6.10 | 4.07 | torch 103.5%, torch-compile 98.1% | - |
| 🟡 | NeFwdOp | test_comparison_bench[ne-1024x4096-float16-ne] | 0.0080 | 0.52 | 2.62 | torch 97.6%, torch-compile 97.6% | - |
| 🟡 | NeFwdOp | test_ne_manifest_bench[hidden-state-prefill-float16] | 0.0141 | 0.59 | 2.97 | torch 93.2%, torch-compile 93.0% | - |
| 🟡 | NeFwdOp | test_ne_manifest_bench[hidden-state-prefill-bfloat16] | 0.0141 | 0.60 | 2.98 | torch 95.0%, torch-compile 95.2% | - |
| 🟡 | NeFwdOp | test_ne_manifest_bench[hidden-state-prefill-float32] | 0.0224 | 0.37 | 3.37 | torch 99.8%, torch-compile 99.6% | - |
| 🔴 | NeFwdOp | test_ne_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.81 | 2.43 | torch 299.8%, torch-compile 75.0% | - |
| 🔴 | NeFwdOp | test_ne_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.81 | 2.43 | torch 307.3%, torch-compile 74.7% | - |
| 🟡 | NeFwdOp | test_ne_manifest_bench[cnn-feat-broadcast-float32] | 0.0214 | 0.60 | 3.00 | torch 224.1%, torch-compile 86.2% | - |
| 🔵 | NegFwdOp | test_neg_bench[elementwise-16M-float16] | 0.0179 | 0.94 | 3.75 | torch 105.3%, torch-compile 100.1% | - |
| 🔵 | NegFwdOp | test_neg_bench[elementwise-16M-bfloat16] | 0.0179 | 0.94 | 3.74 | torch 100.0%, torch-compile 100.0% | - |
| 🟡 | NegFwdOp | test_neg_bench[elementwise-16M-float32] | 0.0340 | 0.49 | 3.94 | torch 99.8%, torch-compile 99.7% | - |
| 🟡 | NegFwdOp | test_neg_bench[elementwise-256M-float16] | 0.2517 | 1.07 | 4.27 | torch 106.7%, torch-compile 99.3% | - |
| 🟡 | NegFwdOp | test_neg_bench[elementwise-256M-bfloat16] | 0.2512 | 1.07 | 4.27 | torch 99.4%, torch-compile 99.6% | - |
| 🔵 | PowFwdOp | test_binary_arith_bench[pow-1024x4096-float16-float16-PowFwdOp-pow-positive] | 0.0199 | 0.21 | 1.26 | torch 101.1%, torch-compile 118.6% | - |
| 🔵 | PowFwdOp | test_binary_arith_bench[pow-1024x10240-float16-float16-PowFwdOp-pow-positive] | 0.0450 | 0.23 | 1.40 | torch 100.9%, torch-compile 119.5% | - |
| 🔵 | PowFwdOp | test_pow_manifest_bench[hidden-state-prefill-float16] | 0.0367 | 0.69 | 1.37 | torch 100.7%, torch-compile 119.2% | - |
| 🔵 | PowFwdOp | test_pow_manifest_bench[hidden-state-prefill-bfloat16] | 0.0376 | 0.67 | 1.34 | torch 100.9%, torch-compile 120.1% | - |
| 🟡 | PowFwdOp | test_pow_manifest_bench[hidden-state-prefill-float32] | 0.0387 | 0.65 | 2.60 | torch 96.7%, torch-compile 108.9% | - |
| 🔵 | PowFwdOp | test_pow_manifest_bench[cnn-feat-broadcast-float16] | 0.0571 | 0.67 | 0.90 | torch 164.8%, torch-compile 106.7% | - |
| 🔵 | PowFwdOp | test_pow_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0590 | 0.65 | 0.87 | torch 161.6%, torch-compile 104.2% | - |
| 🔵 | PowFwdOp | test_pow_manifest_bench[cnn-feat-broadcast-float32] | 0.0572 | 0.67 | 1.80 | torch 164.1%, torch-compile 121.1% | - |
| 🔵 | PreluFwdOp | test_prelu_manifest_bench[cnn-feat-per-channel-float16] | 0.0146 | 1.76 | 3.51 | torch 321.4%, torch-compile 100.0% | - |
| 🟡 | PreluFwdOp | test_prelu_manifest_bench[cnn-feat-per-channel-bfloat16] | 0.0144 | 1.78 | 3.57 | torch 336.7%, torch-compile 99.8% | - |
| 🔵 | PreluFwdOp | test_prelu_manifest_bench[cnn-feat-per-channel-deep-float16] | 0.0084 | 1.54 | 3.08 | torch 299.6%, torch-compile 100.4% | - |
| 🟡 | PreluFwdOp | test_prelu_manifest_bench[cnn-feat-per-channel-deep-bfloat16] | 0.0082 | 1.57 | 3.14 | torch 314.4%, torch-compile 99.6% | - |
| 🔴 | ProdFwdOp | test_prod_bench[hidden-state-reduce-float16] | 0.0989 | 0.08 | 0.17 | flaggems 7.9%, torch 49.8%, torch-compile 8.4% | - |
| 🔴 | ProdFwdOp | test_prod_bench[hidden-state-reduce-bfloat16] | 0.0998 | 0.08 | 0.17 | flaggems 7.8%, torch 49.8%, torch-compile 8.4% | - |
| 🔴 | ProdFwdOp | test_prod_bench[long-seq-reduce-bfloat16] | 0.0172 | 0.12 | 0.24 | flaggems 79.0%, torch 97.8%, torch-compile 25.9% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-8b-prefill-float16] | 0.0119 | 2.83 | 2.83 | flaggems 106.6%, flashinfer 92.5%, vllm 104.8%, torch-ref 1224.2%, torch-compile 114.5% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-8b-prefill-bfloat16] | 0.0126 | 2.65 | 2.66 | flaggems 98.7%, flashinfer 86.3%, vllm 100.5%, torch-ref 1155.7%, torch-compile 118.0% | - |
| 🔵 | RMSNormFwdOp | test_rms_norm_bench[llama-8b-decode-bfloat16] | 0.0021 | 0.01 | 0.01 | flaggems 158.4%, flashinfer 104.6%, vllm 127.7%, torch-ref 866.1%, torch-compile 106.2% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-70b-prefill-float16] | 0.0209 | 3.21 | 3.21 | flaggems 99.1%, flashinfer 95.9%, vllm 103.5%, torch-ref 1291.9%, torch-compile 94.5% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-70b-prefill-bfloat16] | 0.0218 | 3.08 | 3.08 | flaggems 97.8%, flashinfer 91.6%, vllm 101.3%, torch-ref 1242.2%, torch-compile 94.7% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-70b-decode-bfloat16] | 0.0026 | 0.01 | 0.02 | flaggems 157.3%, flashinfer 98.7%, vllm 118.3%, torch-ref 713.5%, torch-compile 102.4% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-405b-prefill-float16] | 0.0420 | 3.20 | 3.20 | flaggems 95.3%, flashinfer 88.5%, vllm 116.1%, torch-ref 1216.0%, torch-compile 94.5% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-405b-prefill-bfloat16] | 0.0431 | 3.11 | 3.12 | flaggems 95.3%, flashinfer 88.4%, vllm 113.7%, torch-ref 1188.4%, torch-compile 96.8% | - |
| 🟡 | RMSNormFwdOp | test_rms_norm_bench[llama-405b-decode-bfloat16] | 0.0036 | 0.02 | 0.03 | flaggems 128.3%, flashinfer 97.4%, vllm 119.5%, torch-ref 555.8%, torch-compile 116.8% | - |
| 🟡 | ReciprocalFwdOp | test_reciprocal_bench[elementwise-16M-float16] | 0.0193 | 0.87 | 3.48 | torch 98.3%, torch-compile 94.3% | - |
| 🟡 | ReciprocalFwdOp | test_reciprocal_bench[elementwise-16M-bfloat16] | 0.0193 | 0.87 | 3.48 | torch 98.2%, torch-compile 94.7% | - |
| 🟡 | ReciprocalFwdOp | test_reciprocal_bench[elementwise-16M-float32] | 0.0341 | 0.49 | 3.94 | torch 99.5%, torch-compile 99.0% | - |
| 🟡 | ReciprocalFwdOp | test_reciprocal_bench[elementwise-256M-float16] | 0.2727 | 0.98 | 3.94 | torch 98.0%, torch-compile 93.9% | - |
| 🟡 | ReciprocalFwdOp | test_reciprocal_bench[elementwise-256M-bfloat16] | 0.2729 | 0.98 | 3.93 | torch 98.0%, torch-compile 94.5% | - |
| 🔵 | ReluFwdOp | test_relu_manifest_bench[hidden-state-prefill-float16] | 0.0103 | 0.81 | 3.25 | torch 104.8%, torch-compile 100.2% | - |
| 🔵 | ReluFwdOp | test_relu_manifest_bench[hidden-state-prefill-bfloat16] | 0.0103 | 0.81 | 3.25 | torch 101.9%, torch-compile 100.3% | - |
| 🟡 | ReluFwdOp | test_relu_manifest_bench[hidden-state-decode-bfloat16] | 0.0012 | 0.00 | 0.01 | torch 112.8%, torch-compile 97.4% | - |
| 🔵 | RemainderFwdOp | test_binary_arith_bench[remainder-1024x4096-float16-float16-RemainderFwdOp-remainder-positive] | 0.0085 | 0.49 | 2.95 | torch 124.7%, torch-compile 101.1% | - |
| 🟡 | RemainderFwdOp | test_binary_arith_bench[remainder-1024x10240-float16-float16-RemainderFwdOp-remainder-positive] | 0.0182 | 0.58 | 3.46 | torch 119.4%, torch-compile 99.9% | - |
| 🔵 | RemainderFwdOp | test_remainder_manifest_bench[hidden-state-prefill-float16] | 0.0155 | 2.16 | 3.24 | torch 116.5%, torch-compile 100.4% | - |
| 🔵 | RemainderFwdOp | test_remainder_manifest_bench[hidden-state-prefill-bfloat16] | 0.0150 | 2.24 | 3.36 | torch 123.7%, torch-compile 100.8% | - |
| 🔵 | RemainderFwdOp | test_remainder_manifest_bench[hidden-state-prefill-float32] | 0.0264 | 1.27 | 3.81 | torch 103.0%, torch-compile 101.1% | - |
| 🟡 | RemainderFwdOp | test_remainder_manifest_bench[cnn-feat-broadcast-float16] | 0.0200 | 2.56 | 2.56 | torch 310.6%, torch-compile 88.7% | - |
| 🟡 | RemainderFwdOp | test_remainder_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0199 | 2.58 | 2.58 | torch 322.0%, torch-compile 93.3% | - |
| 🟡 | RemainderFwdOp | test_remainder_manifest_bench[cnn-feat-broadcast-float32] | 0.0275 | 1.87 | 3.74 | torch 233.9%, torch-compile 97.5% | - |
| 🔵 | RopeLlama31FwdOp | test_rope_llama31_bench[llama31-1d-8k-d128-bfloat16] | 0.0036 | 1.16 | 1.74 | torch-ref 439.8%, torch-compile 123.9% | - |
| 🔴 | RopeLlama31FwdOp | test_rope_llama31_bench[llama31-2d-b1-s8k-h32-d128-float16] | 0.0595 | 2.26 | 2.29 | torch-ref 828.2%, torch-compile 58.7% | - |
| 🔵 | RopeLongRopeFwdOp | test_rope_longrope_bench[longrope-1d-8k-d128-bfloat16] | 0.0036 | 1.16 | 1.74 | torch-ref 439.8%, torch-compile 123.9% | - |
| 🔴 | RopeLongRopeFwdOp | test_rope_longrope_bench[longrope-2d-b1-s8k-h32-d128-float16] | 0.0594 | 2.26 | 2.30 | torch-ref 829.3%, torch-compile 58.8% | - |
| 🔵 | RopeNeoxFwdOp | test_rope_neox_bench[neox-1d-2k-d64-float16] | 0.0018 | 0.29 | 0.43 | torch-ref 517.5%, torch-compile 108.7% | - |
| 🔵 | RopeNeoxFwdOp | test_rope_neox_bench[neox-1d-4k-d128-bfloat16] | 0.0026 | 0.81 | 1.21 | torch-ref 476.5%, torch-compile 121.0% | - |
| 🔴 | RopeNeoxFwdOp | test_rope_neox_bench[neox-2d-b2-s2k-h32-d128-float16] | 0.0310 | 2.17 | 2.18 | torch-ref 877.5%, torch-compile 59.5% | - |
| 🔴 | RopeNeoxPositionIdsFwdOp | test_rope_neox_position_ids_bench[position-ids-s2k-h32-d128-float16] | 0.0278 | 1.21 | 1.24 | vllm 87.1%, torch-ref 465.1%, torch-compile 42.6% | - |
| 🔴 | RopeNeoxPositionIdsFwdOp | test_rope_neox_position_ids_bench[position-ids-s4k-h32-d128-bfloat16] | 0.0456 | 1.47 | 1.52 | vllm 97.4%, torch-ref 546.0%, torch-compile 48.7% | - |
| 🟡 | RopeNonNeoxFwdOp | test_rope_non_neox_bench[non-neox-1d-2k-d64-float16] | 0.0022 | 0.24 | 0.36 | torch-ref 433.8%, torch-compile 91.2% | - |
| 🔴 | RopeNonNeoxFwdOp | test_rope_non_neox_bench[non-neox-2d-b2-s2k-h32-d128-bfloat16] | 0.0252 | 2.66 | 2.69 | torch-ref 1090.6%, torch-compile 75.5% | - |
| 🔵 | RopeYarnFwdOp | test_rope_yarn_bench[yarn-1d-8k-d128-bfloat16] | 0.0036 | 1.17 | 1.76 | torch-ref 443.8%, torch-compile 125.0% | - |
| 🔴 | RopeYarnFwdOp | test_rope_yarn_bench[yarn-2d-b1-s8k-h32-d128-float16] | 0.0594 | 2.26 | 2.29 | torch-ref 829.1%, torch-compile 58.6% | - |
| 🟡 | RoundFwdOp | test_round_bench[elementwise-16M-float16] | 0.0180 | 0.93 | 3.73 | torch 99.8%, torch-compile 99.6% | - |
| 🟡 | RoundFwdOp | test_round_bench[elementwise-16M-bfloat16] | 0.0180 | 0.93 | 3.74 | torch 100.2%, torch-compile 99.9% | - |
| 🟡 | RoundFwdOp | test_round_bench[elementwise-16M-float32] | 0.0341 | 0.49 | 3.94 | torch 99.9%, torch-compile 99.4% | - |
| 🟡 | RoundFwdOp | test_round_bench[elementwise-256M-float16] | 0.2531 | 1.06 | 4.24 | torch 98.9%, torch-compile 98.8% | - |
| 🟡 | RoundFwdOp | test_round_bench[elementwise-256M-bfloat16] | 0.2532 | 1.06 | 4.24 | torch 98.9%, torch-compile 99.0% | - |
| 🟡 | RsqrtFwdOp | test_rsqrt_bench[elementwise-16M-float16] | 0.0182 | 0.92 | 3.69 | torch 100.0%, torch-compile 99.7% | - |
| 🟡 | RsqrtFwdOp | test_rsqrt_bench[elementwise-16M-bfloat16] | 0.0182 | 0.92 | 3.68 | torch 99.8%, torch-compile 99.5% | - |
| 🔵 | RsqrtFwdOp | test_rsqrt_bench[elementwise-16M-float32] | 0.0332 | 0.50 | 4.04 | torch 101.6%, torch-compile 101.5% | - |
| 🟡 | RsqrtFwdOp | test_rsqrt_bench[elementwise-256M-float16] | 0.2561 | 1.05 | 4.19 | torch 99.2%, torch-compile 98.8% | - |
| 🟡 | RsqrtFwdOp | test_rsqrt_bench[elementwise-256M-bfloat16] | 0.2565 | 1.05 | 4.19 | torch 99.2%, torch-compile 98.5% | - |
| 🔵 | SSDChunkScanFwdOp | test_ssd_chunk_scan_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0728 | 88.50 | 1.44 | mamba 137.9%, torch-ref 2689.5%, torch-compile 696.9% | - |
| 🔵 | SSDChunkScanFwdOp | test_ssd_chunk_scan_fwd_bench[mamba2-780m-b1-s4k-bfloat16] | 0.0760 | 84.77 | 1.38 | mamba 133.9%, torch-ref 2579.1%, torch-compile 669.8% | - |
| 🔵 | SSDChunkScanFwdOp | test_ssd_chunk_scan_fwd_bench[mamba2-2p7b-b4-s2k-bfloat16] | 0.2378 | 90.31 | 1.45 | mamba 129.9%, torch-ref 2742.4%, torch-compile 689.7% | - |
| 🔵 | SSDChunkScanFwdOp | test_ssd_chunk_scan_fwd_bench[mamba2-1p3b-b2-s32k-float16] | 1.4693 | 93.54 | 1.51 | mamba 138.5%, torch-ref 2727.6%, torch-compile 678.4% | - |
| 🔵 | SSDChunkStateFwdOp | test_ssd_chunk_state_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0238 | 135.95 | 2.21 | mamba 104.6%, torch-ref 34223.8%, torch-compile 2663.5% | - |
| 🔵 | SSDChunkStateFwdOp | test_ssd_chunk_state_fwd_bench[mamba2-780m-b1-s4k-bfloat16] | 0.0239 | 135.32 | 2.20 | mamba 110.4%, torch-ref 34055.1%, torch-compile 2830.7% | - |
| 🔵 | SSDChunkStateFwdOp | test_ssd_chunk_state_fwd_bench[mamba2-2p7b-b4-s2k-bfloat16] | 0.0656 | 164.36 | 2.65 | mamba 121.9%, torch-ref 41342.1%, torch-compile 3727.4% | - |
| 🔵 | SSDChunkStateFwdOp | test_ssd_chunk_state_fwd_bench[mamba2-780m-b1-s4k-seq-idx-float16] | 0.0286 | 113.25 | 1.84 | mamba 121.3%, torch-ref 28531.2%, torch-compile 2627.3% | - |
| 🔵 | SSDChunkStateFwdOp | test_ssd_chunk_state_fwd_bench[mamba2-780m-b1-s4k-seq-idx-bfloat16] | 0.0290 | 111.44 | 1.81 | mamba 100.4%, torch-ref 28102.2%, torch-compile 2715.4% | - |
| 🔵 | SSDChunkStateFwdOp | test_ssd_chunk_state_fwd_bench[mamba2-1p3b-b2-s32k-seq-idx-float16] | 0.4492 | 153.61 | 2.48 | mamba 144.4%, torch-ref 38530.0%, torch-compile 3710.6% | - |
| 🟢 | SSDDecodeFwdOp | test_ssd_decode_bench[mamba2-1p3b-decode-b1-float16] | 0.0040 | 1.05 | 1.58 | torch-ref 756.8%, torch-compile 225.6% | - |
| 🟢 | SSDDecodeFwdOp | test_ssd_decode_bench[mamba2-1p3b-decode-b1-bfloat16] | 0.0040 | 1.06 | 1.60 | torch-ref 768.5%, torch-compile 225.0% | - |
| 🟢 | SSDDecodeFwdOp | test_ssd_decode_bench[mamba2-2p7b-decode-b8-float16] | 0.0163 | 2.58 | 2.77 | torch-ref 687.9%, torch-compile 187.9% | - |
| 🟢 | SSDDecodeFwdOp | test_ssd_decode_bench[mamba2-780m-decode-b32-float16] | 0.0362 | 2.78 | 2.85 | torch-ref 664.1%, torch-compile 183.1% | - |
| 🟢 | SSDStatePassingFwdOp | test_ssd_state_passing_fwd_bench[mamba2-1p3b-b1-s4k-dstate-float16] | 0.0019 | 0.14 | 0.44 | mamba 449.2%, torch-ref 6406.7%, torch-compile 217.0% | - |
| 🟢 | SSDStatePassingFwdOp | test_ssd_state_passing_fwd_bench[mamba2-1p3b-b1-s4k-dstate-bfloat16] | 0.0020 | 0.13 | 0.41 | mamba 427.4%, torch-ref 6162.9%, torch-compile 206.4% | - |
| 🟢 | SSDStatePassingFwdOp | test_ssd_state_passing_fwd_bench[mamba2-2p7b-b2-s32k-dstate-float16] | 0.0106 | 0.50 | 1.50 | mamba 563.8%, torch-ref 10823.5%, torch-compile 855.8% | - |
| 🟢 | SSDStatePassingFwdOp | test_ssd_state_passing_fwd_bench[mamba2-1p3b-b1-s4k-dstate-init-states-float16] | 0.0020 | 0.13 | 0.42 | mamba 433.5%, torch-ref 5956.9%, torch-compile 169.9% | - |
| 🟢 | SSDStatePassingFwdOp | test_ssd_state_passing_fwd_bench[mamba2-1p3b-b1-s4k-dstate-init-states-bfloat16] | 0.0020 | 0.13 | 0.43 | mamba 444.9%, torch-ref 6119.4%, torch-compile 172.5% | - |
| 🟡 | SSDStatePassingFwdOp | test_ssd_state_passing_fwd_bench[mamba2-1p3b-b1-s4k-flat-init-states-float32] | 0.0219 | 0.77 | 3.26 | mamba 98.7%, torch-ref 580.5%, torch-compile 93.3% | - |
| 🔵 | SeluFwdOp | test_selu_manifest_bench[snn-fc-float16] | 0.0119 | 3.52 | 2.82 | torch 151.1%, torch-compile 135.2% | - |
| 🔵 | SeluFwdOp | test_selu_manifest_bench[snn-fc-bfloat16] | 0.0121 | 3.46 | 2.77 | torch 150.1%, torch-compile 129.2% | - |
| 🔵 | SeluFwdOp | test_selu_manifest_bench[snn-fc-wide-float16] | 0.0213 | 3.93 | 3.14 | torch 153.5%, torch-compile 140.0% | - |
| 🔵 | SeluFwdOp | test_selu_manifest_bench[snn-fc-wide-bfloat16] | 0.0217 | 3.87 | 3.09 | torch 153.0%, torch-compile 134.5% | - |
| 🔴 | SharedFusedMoE | test_shared_fused_moe_bench[1-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 2.5204 | 0.59 | 0.59 | vllm 16.9% | - |
| 🟡 | SharedFusedMoE | test_shared_fused_moe_bench[32-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 4.7434 | 10.10 | 3.66 | vllm 83.6% | - |
| 🔵 | SharedFusedMoE | test_shared_fused_moe_bench[512-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 8.0768 | 94.92 | 4.29 | vllm 108.6% | - |
| 🔴 | SharedFusedMoE | test_shared_fused_moe_bench[2048-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 19.5712 | 156.69 | 1.77 | vllm 59.4% | - |
| 🔴 | SharedFusedMoE | test_shared_fused_moe_bench[4096-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 32.5404 | 188.48 | 1.07 | vllm 45.0% | - |
| 🔴 | SigmoidFwdOp | test_sigmoid_manifest_bench[elementwise-16M-float16] | 0.0287 | 2.34 | 2.34 | torch 80.1%, torch-compile 64.7% | - |
| 🔴 | SigmoidFwdOp | test_sigmoid_manifest_bench[elementwise-16M-bfloat16] | 0.0253 | 2.65 | 2.65 | torch 93.0%, torch-compile 73.8% | - |
| 🟡 | SigmoidFwdOp | test_sigmoid_manifest_bench[elementwise-16M-float32] | 0.0349 | 1.92 | 3.84 | torch 98.4%, torch-compile 97.3% | - |
| 🔴 | SigmoidFwdOp | test_sigmoid_manifest_bench[elementwise-256M-float16] | 0.4247 | 2.53 | 2.53 | torch 75.7%, torch-compile 61.4% | - |
| 🔴 | SigmoidFwdOp | test_sigmoid_manifest_bench[elementwise-256M-bfloat16] | 0.3678 | 2.92 | 2.92 | torch 89.7%, torch-compile 71.6% | - |
| 🟡 | SignFwdOp | test_sign_bench[elementwise-16M-float16] | 0.0190 | 1.77 | 3.54 | torch 95.5%, torch-compile 94.6% | - |
| 🟡 | SignFwdOp | test_sign_bench[elementwise-16M-bfloat16] | 0.0190 | 1.77 | 3.54 | torch 96.0%, torch-compile 95.1% | - |
| 🟡 | SignFwdOp | test_sign_bench[elementwise-16M-float32] | 0.0341 | 0.99 | 3.94 | torch 99.8%, torch-compile 99.8% | - |
| 🟡 | SignFwdOp | test_sign_bench[elementwise-256M-float16] | 0.2705 | 1.98 | 3.97 | torch 94.7%, torch-compile 93.2% | - |
| 🟡 | SignFwdOp | test_sign_bench[elementwise-256M-bfloat16] | 0.2703 | 1.99 | 3.97 | torch 95.7%, torch-compile 94.0% | - |
| 🔵 | SiluAndMulFwdOp | test_silu_and_mul_bench[llama-8b-swiglu-prefill-float16] | 0.0433 | 4.07 | 4.07 | flashinfer 123.3%, torch-ref 437.5%, torch-compile 102.1% | - |
| 🔵 | SiluAndMulFwdOp | test_silu_and_mul_bench[llama-8b-swiglu-prefill-bfloat16] | 0.0434 | 4.06 | 4.06 | flashinfer 124.0%, torch-ref 438.1%, torch-compile 105.3% | - |
| 🟡 | SiluAndMulFwdOp | test_silu_and_mul_bench[llama-8b-swiglu-decode-bfloat16] | 0.0018 | 0.05 | 0.05 | flashinfer 243.6%, torch-ref 198.2%, torch-compile 83.6% | - |
| 🔴 | SiluFwdOp | test_silu_manifest_bench[llama-8b-ffn-prefill-float16] | 0.0505 | 2.91 | 2.32 | torch 74.9%, torch-compile 70.3% | - |
| 🟡 | SiluFwdOp | test_silu_manifest_bench[llama-8b-ffn-prefill-bfloat16] | 0.0434 | 3.38 | 2.71 | torch 88.5%, torch-compile 82.4% | - |
| 🟡 | SiluFwdOp | test_silu_manifest_bench[llama-8b-ffn-decode-bfloat16] | 0.0015 | 0.05 | 0.04 | torch 127.1%, torch-compile 98.0% | - |
| 🔵 | SinFwdOp | test_sin_bench[elementwise-16M-float16] | 0.0256 | 0.66 | 2.62 | torch 102.6%, torch-compile 103.5% | - |
| 🔵 | SinFwdOp | test_sin_bench[elementwise-16M-bfloat16] | 0.0260 | 0.64 | 2.58 | torch 103.2%, torch-compile 103.2% | - |
| 🟡 | SinFwdOp | test_sin_bench[elementwise-16M-float32] | 0.0355 | 0.47 | 3.79 | torch 96.9%, torch-compile 96.7% | - |
| 🔵 | SinFwdOp | test_sin_bench[elementwise-256M-float16] | 0.3709 | 0.72 | 2.90 | torch 101.9%, torch-compile 104.0% | - |
| 🔵 | SinFwdOp | test_sin_bench[elementwise-256M-bfloat16] | 0.3770 | 0.71 | 2.85 | torch 102.4%, torch-compile 103.7% | - |
| 🔵 | SinusoidalFwdOp | test_sinusoidal_bench[transformer-2k-4k-float16] | 0.0424 | 1.19 | 0.40 | torch-ref 250.8%, torch-compile 133.7% | - |
| 🔵 | SinusoidalFwdOp | test_sinusoidal_bench[transformer-2k-4k-bfloat16] | 0.0424 | 1.19 | 0.40 | torch-ref 251.2%, torch-compile 133.7% | - |
| 🔵 | SinusoidalFwdOp | test_sinusoidal_bench[transformer-4k-4k-float16] | 0.0818 | 1.23 | 0.41 | torch-ref 243.6%, torch-compile 136.5% | - |
| 🔵 | SinusoidalFwdOp | test_sinusoidal_bench[transformer-4k-4k-bfloat16] | 0.0818 | 1.23 | 0.41 | torch-ref 243.5%, torch-compile 136.5% | - |
| 🔴 | SoftmaxFwdOp | test_softmax_bench[attn-weights-4k-float16] | 0.0113 | 1.86 | 1.49 | flaggems 76.4%, torch 175.8%, torch-compile 143.2% | - |
| 🔴 | SoftmaxFwdOp | test_softmax_bench[attn-weights-4k-bfloat16] | 0.0113 | 1.86 | 1.49 | flaggems 76.5%, torch 173.7%, torch-compile 147.6% | - |
| 🔴 | SoftmaxFwdOp | test_softmax_bench[attn-weights-4k-float32] | 0.0143 | 1.47 | 2.35 | flaggems 77.4%, torch 141.2%, torch-compile 129.1% | - |
| 🟡 | SoftmaxFwdOp | test_softmax_bench[attn-weights-32k-bfloat16] | 0.0670 | 2.50 | 2.00 | flaggems 95.8%, torch 124.6%, torch-compile 140.8% | - |
| 🔴 | SoftmaxFwdOp | test_softmax_bench[lm-head-logits-float16] | 0.0299 | 0.07 | 0.05 | flaggems 94.3%, torch 110.3%, torch-compile 30.6% | - |
| 🔴 | SoftmaxFwdOp | test_softmax_bench[lm-head-logits-bfloat16] | 0.0311 | 0.07 | 0.05 | flaggems 95.3%, torch 108.4%, torch-compile 30.9% | - |
| 🔴 | SoftmaxFwdOp | test_softmax_bench[lm-head-logits-float32] | 0.0364 | 0.06 | 0.09 | flaggems 85.8%, torch 108.0%, torch-compile 25.6% | - |
| 🟡 | SoftplusFwdOp | test_softplus_manifest_bench[mlp-hidden-float16] | 0.0196 | 2.14 | 1.71 | torch 121.7%, torch-compile 91.5% | - |
| 🟡 | SoftplusFwdOp | test_softplus_manifest_bench[mlp-hidden-bfloat16] | 0.0196 | 2.13 | 1.71 | torch 122.7%, torch-compile 93.2% | - |
| 🟡 | SoftplusFwdOp | test_softplus_manifest_bench[mlp-hidden-wide-float16] | 0.0364 | 2.30 | 1.84 | torch 122.6%, torch-compile 90.2% | - |
| 🟡 | SoftplusFwdOp | test_softplus_manifest_bench[mlp-hidden-wide-bfloat16] | 0.0366 | 2.29 | 1.83 | torch 123.5%, torch-compile 92.3% | - |
| 🟡 | SqrtFwdOp | test_sqrt_bench[elementwise-16M-float16] | 0.0189 | 0.89 | 3.55 | torch 99.8%, torch-compile 98.5% | - |
| 🟡 | SqrtFwdOp | test_sqrt_bench[elementwise-16M-bfloat16] | 0.0190 | 0.88 | 3.54 | torch 100.0%, torch-compile 98.7% | - |
| 🔵 | SqrtFwdOp | test_sqrt_bench[elementwise-16M-float32] | 0.0338 | 0.50 | 3.97 | torch 100.8%, torch-compile 100.5% | - |
| 🟡 | SqrtFwdOp | test_sqrt_bench[elementwise-256M-float16] | 0.2682 | 1.00 | 4.00 | torch 99.2%, torch-compile 98.0% | - |
| 🟡 | SqrtFwdOp | test_sqrt_bench[elementwise-256M-bfloat16] | 0.2694 | 1.00 | 3.99 | torch 99.2%, torch-compile 98.0% | - |
| 🔵 | StdFwdOp | test_std_bench[hidden-state-std-float16] | 0.0100 | 4.21 | 1.69 | flaggems 106.4%, torch 679.6%, torch-compile 188.8% | - |
| 🔵 | StdFwdOp | test_std_bench[hidden-state-std-bfloat16] | 0.0099 | 4.25 | 1.70 | flaggems 112.5%, torch 689.1%, torch-compile 195.1% | - |
| 🟡 | StdFwdOp | test_std_bench[long-seq-std-bfloat16] | 0.0072 | 1.46 | 0.59 | flaggems 183.5%, torch 347.8%, torch-compile 86.6% | - |
| 🔴 | StdFwdOp | test_std_bench[3d-multidim-reduce-float16] | 0.0120 | 0.88 | 0.35 | flaggems 119.2%, torch 223.5%, torch-compile 53.7% | - |
| 🔵 | SubFwdOp | test_binary_arith_bench[sub-1024x4096-float16-float16-SubFwdOp-sub-normal] | 0.0084 | 0.50 | 2.98 | torch 100.8%, torch-compile 100.0% | - |
| 🔵 | SubFwdOp | test_binary_arith_bench[sub-1024x10240-float16-float16-SubFwdOp-sub-normal] | 0.0176 | 0.59 | 3.57 | torch 100.5%, torch-compile 100.0% | - |
| 🔵 | SubFwdOp | test_binary_arith_bench[sub-1024x11008-float16-float16-SubFwdOp-sub-normal] | 0.0186 | 0.61 | 3.64 | torch 100.2%, torch-compile 100.0% | - |
| 🔵 | SubFwdOp | test_sub_manifest_bench[hidden-state-prefill-float16] | 0.0148 | 1.13 | 3.39 | torch 100.0%, torch-compile 100.0% | - |
| 🔵 | SubFwdOp | test_sub_manifest_bench[hidden-state-prefill-bfloat16] | 0.0148 | 1.13 | 3.40 | torch 100.6%, torch-compile 100.0% | - |
| 🟡 | SubFwdOp | test_sub_manifest_bench[hidden-state-prefill-float32] | 0.0265 | 0.63 | 3.79 | torch 99.9%, torch-compile 99.5% | - |
| 🟡 | SubFwdOp | test_sub_manifest_bench[cnn-feat-broadcast-float16] | 0.0165 | 1.56 | 3.11 | torch 276.7%, torch-compile 87.4% | - |
| 🟡 | SubFwdOp | test_sub_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0165 | 1.55 | 3.11 | torch 280.7%, torch-compile 87.8% | - |
| 🟡 | SubFwdOp | test_sub_manifest_bench[cnn-feat-broadcast-float32] | 0.0266 | 0.96 | 3.86 | torch 186.8%, torch-compile 99.6% | - |
| 🟡 | SumFwdOp | test_sum_bench[hidden-state-reduce-float16] | 0.0085 | 0.98 | 1.96 | flaggems 102.6%, torch 577.7%, torch-compile 97.4% | - |
| 🟡 | SumFwdOp | test_sum_bench[hidden-state-reduce-bfloat16] | 0.0087 | 0.97 | 1.94 | flaggems 101.5%, torch 573.8%, torch-compile 97.2% | - |
| 🔴 | SumFwdOp | test_sum_bench[long-seq-reduce-bfloat16] | 0.0052 | 0.40 | 0.80 | flaggems 73.0%, torch 324.5%, torch-compile 84.7% | - |
| 🔴 | SumFwdOp | test_sum_bench[hidden-state-reduce-dim0-bfloat16] | 0.0686 | 0.12 | 0.24 | flaggems 19.9%, torch 65.5%, torch-compile 16.2% | - |
| 🟡 | SumFwdOp | test_sum_bench[hidden-state-reduce-keepdim-bfloat16] | 0.0086 | 0.97 | 1.94 | flaggems 101.8%, torch 575.9%, torch-compile 97.4% | - |
| 🔴 | SumFwdOp | test_sum_bench[3d-multidim-reduce-float16] | 0.0115 | 0.18 | 0.37 | flaggems 117.3%, torch 168.8%, torch-compile 40.4% | - |
| 🟡 | TanhFwdOp | test_tanh_manifest_bench[elementwise-16M-float16] | 0.0210 | 0.80 | 3.19 | torch 98.6%, torch-compile 114.8% | - |
| 🔵 | TanhFwdOp | test_tanh_manifest_bench[elementwise-16M-bfloat16] | 0.0213 | 0.79 | 3.15 | torch 102.4%, torch-compile 115.2% | - |
| 🟡 | TanhFwdOp | test_tanh_manifest_bench[elementwise-16M-float32] | 0.0341 | 0.49 | 3.93 | torch 99.9%, torch-compile 100.8% | - |
| 🟡 | TanhFwdOp | test_tanh_manifest_bench[elementwise-256M-float16] | 0.2985 | 0.90 | 3.60 | torch 97.9%, torch-compile 115.5% | - |
| 🔵 | TanhFwdOp | test_tanh_manifest_bench[elementwise-256M-bfloat16] | 0.3026 | 0.89 | 3.55 | torch 102.4%, torch-compile 115.9% | - |
| 🔴 | TopkSelectorFwdOp | test_topk_selector_bench[topk1024-s32k-kv64k-float32] | 15.6229 | 0.14 | 0.56 | torch 203.8%, torch-compile 203.7%, flashinfer 59.4% | - |
| 🔴 | TopkSelectorFwdOp | test_topk_selector_bench[topk2048-s32k-kv64k-float32] | 16.2446 | 0.13 | 0.55 | torch 205.0%, torch-compile 205.0%, flashinfer 65.7% | - |
| 🟡 | TruncFwdOp | test_trunc_bench[elementwise-16M-float16] | 0.0180 | 0.93 | 3.74 | torch 100.1%, torch-compile 100.0% | - |
| 🟡 | TruncFwdOp | test_trunc_bench[elementwise-16M-bfloat16] | 0.0180 | 0.93 | 3.74 | torch 100.0%, torch-compile 99.8% | - |
| 🟡 | TruncFwdOp | test_trunc_bench[elementwise-16M-float32] | 0.0341 | 0.49 | 3.94 | torch 99.7%, torch-compile 99.6% | - |
| 🟡 | TruncFwdOp | test_trunc_bench[elementwise-256M-float16] | 0.2532 | 1.06 | 4.24 | torch 98.9%, torch-compile 98.7% | - |
| 🟡 | TruncFwdOp | test_trunc_bench[elementwise-256M-bfloat16] | 0.2532 | 1.06 | 4.24 | torch 98.8%, torch-compile 98.6% | - |
| 🟢 | VarFwdOp | test_var_bench[hidden-state-var-float16] | 0.0099 | 4.26 | 1.70 | flaggems 152.3%, torch 686.4%, torch-compile 185.4% | - |
| 🟢 | VarFwdOp | test_var_bench[hidden-state-var-bfloat16] | 0.0100 | 4.19 | 1.68 | flaggems 154.0%, torch 679.9%, torch-compile 187.2% | - |
| 🟡 | VarFwdOp | test_var_bench[long-seq-var-bfloat16] | 0.0071 | 1.47 | 0.59 | flaggems 155.8%, torch 348.4%, torch-compile 88.3% | - |
| 🔴 | VarFwdOp | test_var_bench[3d-multidim-reduce-float16] | 0.0119 | 0.88 | 0.35 | flaggems 118.2%, torch 224.1%, torch-compile 52.3% | - |
| 🔵 | VarMeanFwdOp | test_var_mean_bench[hidden-state-var-mean-float16] | 0.0105 | 4.00 | 1.60 | flaggems 143.6%, torch 1108.5%, torch-compile 199.7% | - |
| 🔵 | VarMeanFwdOp | test_var_mean_bench[hidden-state-var-mean-bfloat16] | 0.0106 | 3.95 | 1.58 | flaggems 146.3%, torch 1103.2%, torch-compile 206.3% | - |
| 🔵 | VarMeanFwdOp | test_var_mean_bench[long-seq-var-mean-bfloat16] | 0.0072 | 1.46 | 0.58 | flaggems 154.7%, torch 561.5%, torch-compile 107.1% | - |
| 🔴 | VarMeanFwdOp | test_var_mean_bench[3d-multidim-reduce-float16] | 0.0121 | 0.87 | 0.35 | flaggems 117.4%, torch 373.8%, torch-compile 64.2% | - |
| 🟡 | WhereFwdOp | test_where_manifest_bench[elementwise-16M-float16] | 0.0309 | 0.54 | 3.80 | torch 99.3%, torch-compile 99.2% | - |
| 🟡 | WhereFwdOp | test_where_manifest_bench[elementwise-16M-bfloat16] | 0.0311 | 0.54 | 3.78 | torch 99.0%, torch-compile 98.8% | - |
| 🟡 | WhereFwdOp | test_where_manifest_bench[elementwise-16M-float32] | 0.0535 | 0.31 | 4.07 | torch 99.8%, torch-compile 99.0% | - |
| 🟡 | WhereFwdOp | test_where_manifest_bench[elementwise-256M-float16] | 0.4293 | 0.63 | 4.38 | torch 99.7%, torch-compile 99.8% | - |
| 🟡 | WhereFwdOp | test_where_manifest_bench[elementwise-256M-bfloat16] | 0.4287 | 0.63 | 4.38 | torch 99.9%, torch-compile 99.9% | - |
| 🟡 | div_bcast | test_broadcast_bench[div-1024x4096-1x4096-float16-DivFwdOp-div-positive] | 0.0070 | 0.60 | 2.40 | torch 232.5%, torch-compile 88.8% | - |
| 🟡 | div_bcast | test_broadcast_bench[div-1024x10240-1x10240-float16-DivFwdOp-div-positive] | 0.0150 | 0.70 | 2.80 | torch 242.0%, torch-compile 82.3% | - |
| 🟡 | div_bcast | test_broadcast_bench[div-1024x11008-1x11008-float16-DivFwdOp-div-positive] | 0.0160 | 0.70 | 2.81 | torch 241.7%, torch-compile 81.8% | - |
| 🔴 | gelu_and_mul_strategy | test_fused_gated_strategy_bench[gelu_and_mul-1024-4096-float16-GeluAndMulFwdKernel-direct] | 0.0182 | 0.46 | 1.38 | torch 183.7%, torch-compile 58.6% | - |
| 🔵 | gelu_and_mul_strategy | test_fused_gated_strategy_bench[gelu_and_mul-1024-4096-float16-GeluAndMulFwdKernel-explicit_parallel] | 0.0100 | 0.84 | 2.51 | torch 333.9%, torch-compile 106.4% | - |
| 🔴 | gelu_tanh_and_mul_strategy | test_fused_gated_strategy_bench[gelu_tanh_and_mul-1024-4096-float16-GeluTanhAndMulFwdKernel-direct] | 0.0178 | 0.47 | 1.41 | torch 179.5%, torch-compile 54.9% | - |
| 🔵 | gelu_tanh_and_mul_strategy | test_fused_gated_strategy_bench[gelu_tanh_and_mul-1024-4096-float16-GeluTanhAndMulFwdKernel-explicit_parallel] | 0.0088 | 0.95 | 2.85 | torch 361.2%, torch-compile 110.5% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-up-T=32768] | 18.4609 | 714.71 | 0.99 | torch 119.8%, deepgemm 100.6%, triton 149.8%, triton-tma 125.0% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-up-T=65536] | 37.3487 | 706.54 | 0.63 | torch 117.1%, deepgemm 113.0%, triton 145.9%, triton-tma 110.9% | - |
| 🟡 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-up-T=131072] | 75.2425 | 701.42 | 0.46 | torch 109.0%, deepgemm 98.9%, triton 143.6%, triton-tma 111.8% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-up-T=262144] | 152.3520 | 692.83 | 0.37 | torch 111.5%, deepgemm 100.5%, triton 141.4%, triton-tma 107.2% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[Llama4-128E-up-T=131072] | 31.1425 | 706.12 | 0.87 | torch 104.7%, deepgemm 100.4%, triton 166.4%, triton-tma 131.3% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[qwen3.5-397B-up-T52429] | 12.5640 | 700.10 | 1.20 | torch 105.0%, deepgemm 100.8%, triton 154.2%, triton-tma 155.7% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-down-T=32768] | 9.6121 | 686.33 | 1.12 | torch 103.0%, deepgemm 101.2%, triton 152.6%, triton-tma 116.5% | - |
| 🟡 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-down-T=65536] | 19.1638 | 688.49 | 0.78 | torch 127.6%, deepgemm 99.7%, triton 151.1%, triton-tma 109.9% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-down-T=131072] | 38.3707 | 687.72 | 0.62 | torch 116.7%, deepgemm 108.0%, triton 151.1%, triton-tma 113.3% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[GLM-5-744B-down-T=262144] | 78.0748 | 675.97 | 0.52 | torch 106.1%, deepgemm 100.4%, triton 147.4%, triton-tma 107.8% | - |
| 🔵 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[Llama4-128E-down-T=131072] | 15.0911 | 728.58 | 0.94 | torch 105.0%, deepgemm 103.3%, triton 152.9%, triton-tma 121.0% | - |
| 🟡 | grouped_gemm_3wg_baselines | test_grouped_gemm_baselines[qwen3.5-397B-down-T52429] | 6.8965 | 637.72 | 1.40 | torch 109.7%, deepgemm 97.8%, triton 148.6%, triton-tma 129.7% | - |
| 🔴 | grouped_gemm_nn | test_grouped_gemm_bench[nn-batch16-m4096-n4096-k4096-float16] | 0.3409 | 403.11 | 1.77 | torch-ref 89.9%, torch-compile 80.8%, torch 78.9% | - |
| 🔵 | grouped_gemm_nt | test_grouped_gemm_bench[nt-batch16-m4096-n4096-k4096-float16] | 0.2326 | 590.98 | 2.60 | torch-ref 1000.7%, torch-compile 986.8%, torch 115.7% | - |
| 🟡 | grouped_gemm_nt | test_grouped_gemm_bench[nt-batch16-m4096-n4096-k4096-bfloat16] | 0.2273 | 604.63 | 2.66 | torch-ref 1003.8%, torch-compile 989.8%, torch 99.0% | - |
| 🔴 | grouped_gemm_tn | test_grouped_gemm_bench[tn-batch16-m4096-n4096-k4096-float16] | 0.7812 | 175.94 | 0.77 | torch-ref 67.1%, torch-compile 66.8%, torch 45.3% | - |
| 🟡 | mul_bcast | test_broadcast_bench[mul-1024x4096-1x4096-float16-MulFwdOp-mul-normal] | 0.0064 | 0.66 | 2.62 | torch 232.5%, torch-compile 94.5% | - |
| 🟡 | mul_bcast | test_broadcast_bench[mul-1024x10240-1x10240-float16-MulFwdOp-mul-normal] | 0.0136 | 0.77 | 3.09 | torch 242.8%, torch-compile 90.8% | - |
| 🟡 | mul_bcast | test_broadcast_bench[mul-1024x11008-1x11008-float16-MulFwdOp-mul-normal] | 0.0145 | 0.78 | 3.11 | torch 243.0%, torch-compile 89.2% | - |
| 🔴 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float16-SiluAndMulFwdKernel-direct] | 0.0178 | 0.47 | 1.41 | torch 177.0%, torch-compile 46.7% | - |
| 🔴 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-11008-float16-SiluAndMulFwdKernel-direct] | 0.0451 | 0.50 | 1.50 | torch 171.2%, torch-compile 42.3% | - |
| 🔴 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-4096-4096-float16-SiluAndMulFwdKernel-direct] | 0.0662 | 0.51 | 1.52 | torch 168.3%, torch-compile 40.7% | - |
| 🔴 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-bfloat16-SiluAndMulFwdKernel-direct] | 0.0178 | 0.47 | 1.41 | torch 177.9%, torch-compile 47.2% | - |
| 🔴 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float32-SiluAndMulFwdKernel-direct] | 0.0200 | 0.42 | 2.51 | torch 173.3%, torch-compile 72.8% | - |
| 🟡 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float16-SiluAndMulFwdKernel-explicit_parallel] | 0.0084 | 0.99 | 2.98 | torch 373.9%, torch-compile 98.5% | - |
| 🔵 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-11008-float16-SiluAndMulFwdKernel-explicit_parallel] | 0.0189 | 1.19 | 3.58 | torch 407.8%, torch-compile 100.8% | - |
| 🔵 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-4096-4096-float16-SiluAndMulFwdKernel-explicit_parallel] | 0.0267 | 1.26 | 3.77 | torch 417.0%, torch-compile 100.8% | - |
| 🟡 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-bfloat16-SiluAndMulFwdKernel-explicit_parallel] | 0.0084 | 0.99 | 2.98 | torch 375.0%, torch-compile 99.6% | - |
| 🟡 | silu_and_mul_strategy | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float32-SiluAndMulFwdKernel-explicit_parallel] | 0.0148 | 0.57 | 3.40 | torch 234.8%, torch-compile 98.5% | - |
| 🟡 | sub_bcast | test_broadcast_bench[sub-1024x4096-1x4096-float16-SubFwdOp-sub-normal] | 0.0064 | 0.66 | 2.64 | torch 234.7%, torch-compile 93.5% | - |
| 🟡 | sub_bcast | test_broadcast_bench[sub-1024x10240-1x10240-float16-SubFwdOp-sub-normal] | 0.0136 | 0.77 | 3.09 | torch 244.0%, torch-compile 89.9% | - |
| 🟡 | sub_bcast | test_broadcast_bench[sub-1024x11008-1x11008-float16-SubFwdOp-sub-normal] | 0.0145 | 0.78 | 3.11 | torch 244.5%, torch-compile 89.6% | - |

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
