# ✅ TileOPs Nightly Report

> **2026-08-29 19:10** &ensp;|&ensp; `c799953` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Correctness** | ✅ &ensp; (527/527 tests across 92 ops) |
| **Benchmarked Ops** | 189 |
| **Benchmark Failures** | ✅ None &ensp;|&ensp; ⚠️ 13 skipped |
| **Regressions** (vs 14-day median) | ✅ None |
| **Baseline Alerts** (< 80%) | ⚠️ 161 |
| **Roofline anomalies** | ⚠️ 2 |
| **Improvements** (vs 14-day best) | 🎉 73 |
| **Moved since previous run** | 🔵 77 |
| **Never-built kernels** | ⚠️ 9 files &ensp;·&ensp; `kernels/attention/deepseek_mla_decode.py` at 5.8% |
| **Untested roofline math** | 750 lines in `perf/` &ensp;·&ensp; `perf/formulas.py` at 13.1% |
| **Untested op logic** | 2589 lines in `ops/` **+2** &ensp;·&ensp; 39.2% of branches taken **−0.2pp** |
| | <sub>coverage compared against the 2026-08-29 run; no figure means it held</sub> |

## 🎉 Performance Improvements (vs 14-day best)

| Op | Config | Prev Best (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **SharedFusedMoE** | test_shared_fused_moe_bench[1-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 2.4995 | 0.5980 | -76.1% | 2.50 |
| **GemmFwdOp** | test_gemm_bench[mid-m96-gate-up-bfloat16] | 0.0686 | 0.0164 | -76.1% | 177.06 |
| **GemmFwdOp** | test_gemm_bench[ds-v3-decode-gate-up-bfloat16] | 0.0676 | 0.0170 | -74.8% | 227.63 |
| **Conv3dFwdOp** | test_conv3d_bench[3d-unet-aspp-3x3x3-rate6-float16] | 0.1256 | 0.0331 | -73.7% | 219.05 |
| **SinusoidalFwdOp** | test_sinusoidal_bench[transformer-4k-4k-bfloat16] | 0.0818 | 0.0251 | -69.3% | 4.01 |
| **SinusoidalFwdOp** | test_sinusoidal_bench[transformer-4k-4k-float16] | 0.0818 | 0.0252 | -69.2% | 4.00 |
| **SinusoidalFwdOp** | test_sinusoidal_bench[transformer-2k-4k-bfloat16] | 0.0424 | 0.0136 | -67.9% | 3.70 |
| **SinusoidalFwdOp** | test_sinusoidal_bench[transformer-2k-4k-float16] | 0.0424 | 0.0136 | -67.8% | 3.69 |
| **Conv3dFwdOp** | test_conv3d_bench[unet-encoder-k3-s1-bias-bfloat16] | 0.3536 | 0.1178 | -66.7% | 123.10 |
| **Conv3dFwdOp** | test_conv3d_bench[unet-encoder-k3-s1-bfloat16] | 0.3539 | 0.1192 | -66.3% | 121.57 |
| **GemmFwdOp** | test_gemm_bench[mid-m16-attn-bfloat16] | 0.0657 | 0.0236 | -64.0% | 39.78 |
| **GemmFwdOp** | test_gemm_bench[mid-m32-attn-bfloat16] | 0.0660 | 0.0240 | -63.6% | 78.19 |
| **SharedFusedMoE** | test_shared_fused_moe_bench[4096-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 32.5280 | 13.8066 | -57.6% | 444.22 |
| **MaximumFwdOp** | test_maximum_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0342 | 0.0164 | -52.2% | 0.78 |
| **MaximumFwdOp** | test_maximum_manifest_bench[cnn-feat-broadcast-float16] | 0.0342 | 0.0165 | -51.7% | 0.78 |
| **MinimumFwdOp** | test_minimum_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0342 | 0.0166 | -51.5% | 0.77 |
| **GemmFwdOp** | test_gemm_bench[square-1k-nn-float16] | 0.0145 | 0.0071 | -50.9% | 302.29 |
| **GemmFwdOp** | test_gemm_bench[square-1k-nn-bfloat16] | 0.0144 | 0.0071 | -50.8% | 302.29 |
| **MinimumFwdOp** | test_minimum_manifest_bench[cnn-feat-broadcast-float16] | 0.0342 | 0.0168 | -50.8% | 0.76 |
| **SharedFusedMoE** | test_shared_fused_moe_bench[2048-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 19.5167 | 9.6449 | -50.6% | 317.95 |
| **GemmFwdOp** | test_gemm_bench[wide-n-24576-bfloat16] | 0.8986 | 0.4629 | -48.5% | 668.05 |
| **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-down-bfloat16] | 0.3209 | 0.1839 | -42.7% | 653.92 |
| **GemmFwdOp** | test_gemm_bench[ds-v3-decode-down-bfloat16] | 0.0245 | 0.0145 | -40.8% | 258.68 |
| **GemmFwdOp** | test_gemm_bench[k-dominant-7168x16384-bfloat16] | 2.0569 | 1.2690 | -38.3% | 758.16 |
| **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-attn-proj-bfloat16] | 0.5391 | 0.3363 | -37.6% | 715.18 |
| **Conv3dFwdOp** | test_conv3d_bench[video-stage-downsample-k3-s2-bias-float16] | 0.0353 | 0.0220 | -37.5% | 62.94 |
| **Conv3dFwdOp** | test_conv3d_bench[video-stage-downsample-k3-s2-float16] | 0.0349 | 0.0219 | -37.2% | 63.38 |
| **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-attn-proj-float16] | 0.5398 | 0.3404 | -36.9% | 706.61 |
| **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-gate-up-bfloat16] | 0.3360 | 0.2137 | -36.4% | 580.43 |
| **GemmFwdOp** | test_gemm_bench[mid-m64-down-bfloat16] | 0.0206 | 0.0133 | -35.3% | 140.82 |
| **SharedFusedMoE** | test_shared_fused_moe_bench[512-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 8.0564 | 5.3516 | -33.6% | 143.26 |
| **GeluFwdOp** | test_gelu_manifest_bench[llama-8b-ffn-prefill-bfloat16] | 0.0551 | 0.0394 | -28.6% | 3.73 |
| **ErfFwdOp** | test_erf_bench[elementwise-256M-bfloat16] | 0.4232 | 0.3032 | -28.4% | 0.89 |
| **SharedFusedMoE** | test_shared_fused_moe_bench[32-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 4.7400 | 3.4276 | -27.7% | 13.98 |
| **ErfFwdOp** | test_erf_bench[elementwise-256M-float16] | 0.4203 | 0.3040 | -27.7% | 0.88 |
| **GeluFwdOp** | test_gelu_manifest_bench[llama-8b-ffn-prefill-float16] | 0.0526 | 0.0387 | -26.4% | 3.79 |
| **GeluAndMulFwdOp** | test_gelu_and_mul_bench[ffn-gelu-prefill-bfloat16] | 0.0594 | 0.0452 | -23.8% | 3.89 |
| **ErfFwdOp** | test_erf_bench[elementwise-16M-bfloat16] | 0.0284 | 0.0219 | -22.9% | 0.77 |
| **LogicalOrFwdOp** | test_logical_or_manifest_bench[cnn-feat-broadcast-float16] | 0.0164 | 0.0126 | -22.7% | 3.05 |
| **LogicalOrFwdOp** | test_logical_or_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0164 | 0.0127 | -22.3% | 3.03 |
| **NeFwdOp** | test_ne_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0124 | -21.8% | 1.03 |
| **LogicalAndFwdOp** | test_logical_and_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0124 | -21.6% | 3.10 |
| **ErfFwdOp** | test_erf_bench[elementwise-16M-float16] | 0.0282 | 0.0221 | -21.5% | 0.76 |
| **GeFwdOp** | test_ge_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0125 | -21.5% | 1.03 |
| **LtFwdOp** | test_lt_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0125 | -21.4% | 1.03 |
| **EqFwdOp** | test_eq_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0125 | -21.3% | 1.03 |
| **LeFwdOp** | test_le_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0125 | -21.3% | 1.03 |
| **LeFwdOp** | test_le_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0125 | -21.0% | 1.02 |
| **NeFwdOp** | test_ne_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0125 | -21.0% | 1.02 |
| **EqFwdOp** | test_eq_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0126 | -20.8% | 1.02 |
| **GtFwdOp** | test_gt_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0126 | -20.8% | 1.02 |
| **LogicalAndFwdOp** | test_logical_and_manifest_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0126 | -20.8% | 3.06 |
| **CountNonzeroFwdOp** | test_count_nonzero_bench[3d-multidim-reduce-float16] | 0.0064 | 0.0051 | -20.6% | 0.83 |
| **GtFwdOp** | test_gt_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0126 | -20.4% | 1.02 |
| **GeFwdOp** | test_ge_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0158 | 0.0126 | -20.2% | 1.02 |
| **LtFwdOp** | test_lt_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0128 | -19.4% | 1.00 |
| **AmaxFwdOp** | test_amax_bench[3d-multidim-reduce-float16] | 0.0057 | 0.0046 | -19.2% | 0.46 |
| **AminFwdOp** | test_amin_bench[3d-multidim-reduce-float16] | 0.0057 | 0.0046 | -19.2% | 0.46 |
| **SumFwdOp** | test_sum_bench[3d-multidim-reduce-float16] | 0.0057 | 0.0046 | -19.1% | 0.46 |
| **MeanFwdOp** | test_mean_bench[3d-multidim-reduce-float16] | 0.0057 | 0.0046 | -18.6% | 0.46 |
| **GeluAndMulFwdOp** | test_gelu_and_mul_bench[ffn-gelu-prefill-float16] | 0.0548 | 0.0447 | -18.6% | 3.94 |
| **SigmoidFwdOp** | test_sigmoid_manifest_bench[elementwise-256M-bfloat16] | 0.3062 | 0.2519 | -17.7% | 4.26 |
| **SigmoidFwdOp** | test_sigmoid_manifest_bench[elementwise-256M-float16] | 0.3017 | 0.2516 | -16.6% | 4.27 |
| **gelu_and_mul_strategy** | test_fused_gated_strategy_bench[gelu_and_mul-1024-4096-float16-GeluAndMulFwdKernel-explicit_parallel] | 0.0099 | 0.0084 | -15.2% | 1.00 |
| **SigmoidFwdOp** | test_sigmoid_manifest_bench[elementwise-16M-bfloat16] | 0.0218 | 0.0185 | -15.1% | 3.63 |
| **SigmoidFwdOp** | test_sigmoid_manifest_bench[elementwise-16M-float16] | 0.0214 | 0.0185 | -13.6% | 3.63 |
| **SinFwdOp** | test_sin_bench[elementwise-256M-bfloat16] | 0.3735 | 0.3273 | -12.4% | 0.82 |
| **SinFwdOp** | test_sin_bench[elementwise-256M-float16] | 0.3663 | 0.3221 | -12.1% | 0.83 |
| **HardswishFwdOp** | test_hardswish_manifest_bench[mbv3-stage3-bfloat16] | 0.0090 | 0.0080 | -11.7% | 3.02 |
| **CosFwdOp** | test_cos_bench[elementwise-256M-float16] | 0.3760 | 0.3321 | -11.7% | 0.81 |
| **CosFwdOp** | test_cos_bench[elementwise-256M-bfloat16] | 0.3819 | 0.3394 | -11.1% | 0.79 |
| **MishFwdOp** | test_mish_manifest_bench[yolo-p4-float16] | 0.0213 | 0.0191 | -10.3% | 2.74 |
| **HardswishFwdOp** | test_hardswish_manifest_bench[mbv3-stage3-float16] | 0.0089 | 0.0080 | -10.1% | 3.02 |

## 🔵 Moved Since Previous Run

> Moves against the most recent reading. A row restored to its old level appears only here: returning is not a new 14-day record.

| Op | Config | Previous (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **SharedFusedMoE** | test_shared_fused_moe_bench[1-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 2.5203 | 0.5980 | -76.3% | 2.50 |
| **GemmFwdOp** | test_gemm_bench[mid-m96-gate-up-bfloat16] | 0.0687 | 0.0164 | -76.1% | 177.06 |
| **GemmFwdOp** | test_gemm_bench[ds-v3-decode-gate-up-bfloat16] | 0.0677 | 0.0170 | -74.9% | 227.63 |
| **Conv3dFwdOp** | test_conv3d_bench[3d-unet-aspp-3x3x3-rate6-float16] | 0.1269 | 0.0331 | -73.9% | 219.05 |
| **SinusoidalFwdOp** | test_sinusoidal_bench[transformer-4k-4k-bfloat16] | 0.0819 | 0.0251 | -69.3% | 4.01 |
| **SinusoidalFwdOp** | test_sinusoidal_bench[transformer-4k-4k-float16] | 0.0819 | 0.0252 | -69.3% | 4.00 |
| **SinusoidalFwdOp** | test_sinusoidal_bench[transformer-2k-4k-float16] | 0.0426 | 0.0136 | -68.0% | 3.69 |
| **SinusoidalFwdOp** | test_sinusoidal_bench[transformer-2k-4k-bfloat16] | 0.0424 | 0.0136 | -67.9% | 3.70 |
| **Conv3dFwdOp** | test_conv3d_bench[unet-encoder-k3-s1-bias-bfloat16] | 0.3536 | 0.1178 | -66.7% | 123.10 |
| **Conv3dFwdOp** | test_conv3d_bench[unet-encoder-k3-s1-bfloat16] | 0.3542 | 0.1192 | -66.3% | 121.57 |
| **GemmFwdOp** | test_gemm_bench[mid-m16-attn-bfloat16] | 0.0657 | 0.0236 | -64.0% | 39.78 |
| **GemmFwdOp** | test_gemm_bench[mid-m32-attn-bfloat16] | 0.0660 | 0.0240 | -63.6% | 78.19 |
| **SharedFusedMoE** | test_shared_fused_moe_bench[4096-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 32.5298 | 13.8066 | -57.6% | 444.22 |
| **MaximumFwdOp** | test_maximum_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0342 | 0.0164 | -52.2% | 0.78 |
| **MaximumFwdOp** | test_maximum_manifest_bench[cnn-feat-broadcast-float16] | 0.0342 | 0.0165 | -51.7% | 0.78 |
| **MinimumFwdOp** | test_minimum_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0342 | 0.0166 | -51.5% | 0.77 |
| **GemmFwdOp** | test_gemm_bench[square-1k-nn-float16] | 0.0145 | 0.0071 | -50.9% | 302.29 |
| **MinimumFwdOp** | test_minimum_manifest_bench[cnn-feat-broadcast-float16] | 0.0342 | 0.0168 | -50.8% | 0.76 |
| **GemmFwdOp** | test_gemm_bench[square-1k-nn-bfloat16] | 0.0144 | 0.0071 | -50.8% | 302.29 |
| **SharedFusedMoE** | test_shared_fused_moe_bench[2048-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 19.5344 | 9.6449 | -50.6% | 317.95 |
| **GemmFwdOp** | test_gemm_bench[wide-n-24576-bfloat16] | 0.8996 | 0.4629 | -48.5% | 668.05 |
| **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-down-bfloat16] | 0.3213 | 0.1839 | -42.8% | 653.92 |
| **GemmFwdOp** | test_gemm_bench[ds-v3-decode-down-bfloat16] | 0.0246 | 0.0145 | -41.0% | 258.68 |
| **GemmFwdOp** | test_gemm_bench[k-dominant-7168x16384-bfloat16] | 2.0595 | 1.2690 | -38.4% | 758.16 |
| **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-attn-proj-bfloat16] | 0.5397 | 0.3363 | -37.7% | 715.18 |
| **Conv3dFwdOp** | test_conv3d_bench[video-stage-downsample-k3-s2-bias-float16] | 0.0353 | 0.0220 | -37.6% | 62.94 |
| **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-attn-proj-float16] | 0.5437 | 0.3404 | -37.4% | 706.61 |
| **Conv3dFwdOp** | test_conv3d_bench[video-stage-downsample-k3-s2-float16] | 0.0349 | 0.0219 | -37.3% | 63.38 |
| **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-gate-up-bfloat16] | 0.3379 | 0.2137 | -36.8% | 580.43 |
| **GemmFwdOp** | test_gemm_bench[mid-m64-down-bfloat16] | 0.0207 | 0.0133 | -35.4% | 140.82 |
| **SharedFusedMoE** | test_shared_fused_moe_bench[512-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 8.0618 | 5.3516 | -33.6% | 143.26 |
| **GeluFwdOp** | test_gelu_manifest_bench[llama-8b-ffn-prefill-bfloat16] | 0.0553 | 0.0394 | -28.9% | 3.73 |
| **ErfFwdOp** | test_erf_bench[elementwise-256M-bfloat16] | 0.4234 | 0.3032 | -28.4% | 0.89 |
| **ErfFwdOp** | test_erf_bench[elementwise-256M-float16] | 0.4217 | 0.3040 | -27.9% | 0.88 |
| **LogicalAndFwdOp** | test_logical_and_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0172 | 0.0124 | -27.8% | 3.10 |
| **SharedFusedMoE** | test_shared_fused_moe_bench[32-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 4.7436 | 3.4276 | -27.7% | 13.98 |
| **NeFwdOp** | test_ne_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0172 | 0.0124 | -27.6% | 1.03 |
| **LeFwdOp** | test_le_manifest_bench[cnn-feat-broadcast-float16] | 0.0173 | 0.0125 | -27.6% | 1.03 |
| **LogicalOrFwdOp** | test_logical_or_manifest_bench[cnn-feat-broadcast-float16] | 0.0174 | 0.0126 | -27.5% | 3.05 |
| **GeFwdOp** | test_ge_manifest_bench[cnn-feat-broadcast-float16] | 0.0172 | 0.0125 | -27.5% | 1.03 |
| **EqFwdOp** | test_eq_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0172 | 0.0125 | -27.5% | 1.03 |
| **LtFwdOp** | test_lt_manifest_bench[cnn-feat-broadcast-float16] | 0.0172 | 0.0125 | -27.4% | 1.03 |
| **LogicalOrFwdOp** | test_logical_or_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0175 | 0.0127 | -27.3% | 3.03 |
| **LeFwdOp** | test_le_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0172 | 0.0125 | -27.3% | 1.02 |
| **GtFwdOp** | test_gt_manifest_bench[cnn-feat-broadcast-float16] | 0.0172 | 0.0126 | -27.1% | 1.02 |
| **NeFwdOp** | test_ne_manifest_bench[cnn-feat-broadcast-float16] | 0.0172 | 0.0125 | -27.0% | 1.02 |
| **LogicalAndFwdOp** | test_logical_and_manifest_bench[cnn-feat-broadcast-float16] | 0.0172 | 0.0126 | -27.0% | 3.06 |
| **EqFwdOp** | test_eq_manifest_bench[cnn-feat-broadcast-float16] | 0.0172 | 0.0126 | -26.8% | 1.02 |
| **GtFwdOp** | test_gt_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0173 | 0.0126 | -26.8% | 1.02 |
| **GeFwdOp** | test_ge_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0172 | 0.0126 | -26.6% | 1.02 |
| **GeluFwdOp** | test_gelu_manifest_bench[llama-8b-ffn-prefill-float16] | 0.0526 | 0.0387 | -26.4% | 3.79 |
| **LtFwdOp** | test_lt_manifest_bench[cnn-feat-broadcast-bfloat16] | 0.0172 | 0.0128 | -25.8% | 1.00 |
| **GeluAndMulFwdOp** | test_gelu_and_mul_bench[ffn-gelu-prefill-bfloat16] | 0.0595 | 0.0452 | -24.0% | 3.89 |
| **ErfFwdOp** | test_erf_bench[elementwise-16M-bfloat16] | 0.0286 | 0.0219 | -23.3% | 0.77 |
| **ErfFwdOp** | test_erf_bench[elementwise-16M-float16] | 0.0283 | 0.0221 | -21.8% | 0.76 |
| **CountNonzeroFwdOp** | test_count_nonzero_bench[3d-multidim-reduce-float16] | 0.0064 | 0.0051 | -21.0% | 0.83 |
| **AmaxFwdOp** | test_amax_bench[3d-multidim-reduce-float16] | 0.0057 | 0.0046 | -19.7% | 0.46 |
| **AminFwdOp** | test_amin_bench[3d-multidim-reduce-float16] | 0.0057 | 0.0046 | -19.7% | 0.46 |
| **SumFwdOp** | test_sum_bench[3d-multidim-reduce-float16] | 0.0057 | 0.0046 | -19.6% | 0.46 |
| **MeanFwdOp** | test_mean_bench[3d-multidim-reduce-float16] | 0.0057 | 0.0046 | -19.1% | 0.46 |
| **GeluAndMulFwdOp** | test_gelu_and_mul_bench[ffn-gelu-prefill-float16] | 0.0551 | 0.0447 | -18.9% | 3.94 |
| **SigmoidFwdOp** | test_sigmoid_manifest_bench[elementwise-256M-bfloat16] | 0.3068 | 0.2519 | -17.9% | 4.26 |
| **SigmoidFwdOp** | test_sigmoid_manifest_bench[elementwise-256M-float16] | 0.3024 | 0.2516 | -16.8% | 4.27 |
| **gelu_and_mul_strategy** | test_fused_gated_strategy_bench[gelu_and_mul-1024-4096-float16-GeluAndMulFwdKernel-explicit_parallel] | 0.0100 | 0.0084 | -16.6% | 1.00 |
| **SigmoidFwdOp** | test_sigmoid_manifest_bench[elementwise-16M-bfloat16] | 0.0219 | 0.0185 | -15.4% | 3.63 |
| **SigmoidFwdOp** | test_sigmoid_manifest_bench[elementwise-16M-float16] | 0.0215 | 0.0185 | -13.9% | 3.63 |
| **HardswishFwdOp** | test_hardswish_manifest_bench[mbv3-stage2-bfloat16] | 0.0132 | 0.0115 | -13.3% | 3.36 |
| **EqFwdOp** | test_eq_manifest_bench[cnn-feat-broadcast-float32] | 0.0215 | 0.0188 | -12.8% | 0.68 |
| **SinFwdOp** | test_sin_bench[elementwise-256M-bfloat16] | 0.3736 | 0.3273 | -12.4% | 0.82 |
| **SinFwdOp** | test_sin_bench[elementwise-256M-float16] | 0.3668 | 0.3221 | -12.2% | 0.83 |
| **CosFwdOp** | test_cos_bench[elementwise-256M-float16] | 0.3766 | 0.3321 | -11.8% | 0.81 |
| **HardswishFwdOp** | test_hardswish_manifest_bench[mbv3-stage3-bfloat16] | 0.0090 | 0.0080 | -11.7% | 3.02 |
| **CosFwdOp** | test_cos_bench[elementwise-256M-bfloat16] | 0.3839 | 0.3394 | -11.6% | 0.79 |
| **div_bcast** | test_broadcast_bench[div-1024x11008-1x11008-float16-DivFwdOp-div-positive] | 0.0153 | 0.0136 | -11.3% | 0.83 |
| **MishFwdOp** | test_mish_manifest_bench[yolo-p4-float16] | 0.0214 | 0.0191 | -10.8% | 2.74 |
| **MishFwdOp** | test_mish_manifest_bench[yolo-p4-bfloat16] | 0.0216 | 0.0194 | -10.2% | 2.70 |
| **MishFwdOp** | test_mish_manifest_bench[yolo-p3-float16] | 0.0402 | 0.0361 | -10.2% | 2.90 |

## ⚠️ Roofline Model Anomalies

> A FAIL row implies a rate above the hardware's theoretical ceiling: its (flops, bytes) formula or declared roof is wrong, and its SOL reading cannot be trusted. A WARN row exceeds the calibrated ceiling; recheck the formula or the calibration.

| Level | Op | Config | Signal |
|:------|:---|:-------|:-------|
| WARN | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-attn-proj-float16] | 107% of the calibrated ceiling |
| WARN | **GemmFwdOp** | test_gemm_bench[k-dominant-7168x16384-bfloat16] | 108% of the calibrated ceiling |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 80%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-gate-up-block128-float8_e4m3fn] | 0.1482 | 0.0129 | 8.7% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[gemv-down-m1-block128-float8_e4m3fn] | 0.0444 | 0.0077 | 17.3% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[k-dominant-7168x16384-block128-float8_e4m3fn] | 3.5901 | 0.7772 | 21.6% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[large-spatial-float16] | 4.3461 | 1.0180 | 23.4% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-down-block128-float8_e4m3fn] | 0.0376 | 0.0092 | 24.5% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **MaxPool1dFwdOp** | test_max_pool1d_bench[textcnn-global-float16] | 0.0135 | 0.0037 | 27.6% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-attn-proj-block128-float8_e4m3fn] | 0.7702 | 0.2155 | 28.0% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b4-dmem1024-d512-float16] | 0.0826 | 0.0256 | 31.0% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-bfloat16] | 0.4566 | 0.1430 | 31.3% | fa3 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[small-batch-down-m8-per-tensor-float8_e4m3fn] | 0.0265 | 0.0084 | 31.5% | deepgemm |

<details>
<summary><strong>151 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-bfloat16] | 0.4553 | 0.1435 | 31.5% | fa3 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-down-block128-float8_e4m3fn] | 0.4458 | 0.1437 | 32.2% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-stage2-float16] | 0.0107 | 0.0035 | 32.6% | torch-compile |
| 🔴 | **MeanPoolingForwardOp** | test_mean_pooling_bench[dense-mainstream] | 0.1351 | 0.0470 | 34.8% | torch-view-mean |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-stage3-float16] | 0.0129 | 0.0046 | 35.4% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-gate-up-block128-float8_e4m3fn] | 0.3857 | 0.1399 | 36.3% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-fc-float16] | 0.0061 | 0.0022 | 36.8% | torch-compile |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-b64-complex64] | 0.0152 | 0.0056 | 36.8% | torch-cufft |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[wide-n-24576-block128-float8_e4m3fn] | 1.0272 | 0.3832 | 37.3% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **BatchNormFwdOp** | test_batch_norm_fwd_bench[resnet50-stage1-float16] | 0.0109 | 0.0041 | 37.7% | torch-compile |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[mha-decode-b32-pv-per-tensor-float8_e4m3fn] | 0.0647 | 0.0251 | 38.7% | flashinfer-bmm-fp8 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-short-bfloat16] | 0.4089 | 0.1591 | 38.9% | fa3 |
| 🔴 | **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[textcnn-global-float16] | 0.0193 | 0.0076 | 39.1% | torch-compile |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-short-bfloat16] | 0.4158 | 0.1652 | 39.7% | fa3 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[gemv-down-m1-per-tensor-float8_e4m3fn] | 0.0259 | 0.0103 | 39.8% | deepgemm |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b1-dmem512-d256-float16] | 0.0329 | 0.0131 | 39.9% | torch-compile |
| 🔴 | **MeanPoolingForwardOp** | test_mean_pooling_bench[dense-batched] | 0.0702 | 0.0285 | 40.6% | torch-view-mean |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-4096-4096-float16-SiluAndMulFwdKernel-direct] | 0.0662 | 0.0269 | 40.7% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-down-per-tensor-float8_e4m3fn] | 0.0254 | 0.0104 | 40.8% | deepgemm |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c128-b64-complex128] | 0.0205 | 0.0085 | 41.4% | torch-cufft |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-bfloat16] | 1.3118 | 0.5474 | 41.7% | fa3 |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-1024-11008-float16-SiluAndMulFwdKernel-direct] | 0.0450 | 0.0191 | 42.4% | torch-compile |
| 🔴 | **MaxPool3dIndicesFwdOp** | test_max_pool3d_indices_bench[c3d-pool1-float16] | 0.3041 | 0.1295 | 42.6% | torch-compile |
| 🔴 | **RopeNeoxPositionIdsFwdOp** | test_rope_neox_position_ids_bench[position-ids-s2k-h32-d128-float16] | 0.0278 | 0.0119 | 42.8% | torch-compile |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[mha-decode-b64-qk-per-tensor-float8_e4m3fn] | 0.1154 | 0.0498 | 43.1% | flashinfer-bmm-fp8 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-prefill-varlen-mixed-fp16] | 0.1403 | 0.0613 | 43.7% | fa3 |
| 🔴 | **GroupedGemmFwdOp** | test_grouped_gemm_bench[tn-batch16-m4096-n4096-k4096-float16] | 0.7815 | 0.3542 | 45.3% | torch |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float16-SiluAndMulFwdKernel-direct] | 0.0178 | 0.0083 | 46.7% | torch-compile |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-bfloat16-SiluAndMulFwdKernel-direct] | 0.0178 | 0.0084 | 47.4% | torch-compile |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-bfloat16] | 1.2418 | 0.5903 | 47.5% | fa3 |
| 🔴 | **RopeNeoxPositionIdsFwdOp** | test_rope_neox_position_ids_bench[position-ids-s4k-h32-d128-bfloat16] | 0.0456 | 0.0223 | 48.8% | torch-compile |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p256-float16] | 0.1654 | 0.0811 | 49.0% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-405b-p256-float16] | 0.0536 | 0.0266 | 49.5% | fa3 |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-small-bfloat16] | 0.0394 | 0.0196 | 49.6% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-bfloat16] | 1.1034 | 0.5481 | 49.7% | fa3 |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-long-k-pressure-float16] | 0.2844 | 0.1420 | 49.9% | marlin-fp32 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-down-per-tensor-float8_e4m3fn] | 0.2108 | 0.1055 | 50.0% | deepgemm |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-2p7b-b2-s32k-dt-bias-float16] | 0.0444 | 0.0223 | 50.3% | mamba |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-70b-prefill-varlen-q-lt-kv-bf16] | 0.1971 | 0.0992 | 50.3% | fa3 |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[compile-smoke-rect-128x256x256-float16] | 0.0059 | 0.0030 | 51.6% | torch-dequantized-matmul |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-dt-bias-bfloat16] | 0.0124 | 0.0064 | 51.7% | mamba |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-bfloat16] | 0.0121 | 0.0064 | 52.8% | mamba |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-float16] | 0.0196 | 0.0107 | 54.2% | torch-compile |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-non-power2-low-cta-float16] | 0.0745 | 0.0406 | 54.5% | marlin-fp16 |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-bfloat16] | 0.0195 | 0.0106 | 54.6% | torch-compile |
| 🔴 | **gelu_tanh_and_mul_strategy** | test_fused_gated_strategy_bench[gelu_tanh_and_mul-1024-4096-float16-GeluTanhAndMulFwdKernel-direct] | 0.0178 | 0.0098 | 54.9% | torch-compile |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-70b-p256-float16] | 0.0668 | 0.0369 | 55.3% | fa3 |
| 🔴 | **MaxPool3dIndicesFwdOp** | test_max_pool3d_indices_bench[c3d-pool2-float16] | 0.0589 | 0.0327 | 55.5% | torch-compile |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 1.0175 | 0.5757 | 56.6% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-prefill-varlen-uniform-fp16] | 0.1249 | 0.0716 | 57.3% | fa3 |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-medium-bfloat16] | 0.0544 | 0.0315 | 57.9% | torch-compile |
| 🔴 | **RopeLlama31FwdOp** | test_rope_llama31_bench[llama31-2d-b1-s8k-h32-d128-float16] | 0.0598 | 0.0348 | 58.3% | torch-compile |
| 🔴 | **RopeYarnFwdOp** | test_rope_yarn_bench[yarn-2d-b1-s8k-h32-d128-float16] | 0.0595 | 0.0348 | 58.6% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-float16] | 0.2445 | 0.1433 | 58.6% | fa3 |
| 🔴 | **RopeLongRopeFwdOp** | test_rope_longrope_bench[longrope-2d-b1-s8k-h32-d128-float16] | 0.0595 | 0.0349 | 58.7% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-float16] | 0.2432 | 0.1435 | 59.0% | fa3 |
| 🔴 | **TopkSelectorFwdOp** | test_topk_selector_bench[topk1024-s32k-kv64k-float32] | 15.6384 | 9.2818 | 59.4% | flashinfer |
| 🔴 | **RopeNeoxFwdOp** | test_rope_neox_bench[neox-2d-b2-s2k-h32-d128-float16] | 0.0310 | 0.0184 | 59.4% | torch-compile |
| 🔴 | **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[ecg-cnn-dilated-bfloat16] | 0.0223 | 0.0134 | 60.0% | torch-compile |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[throughput-8b-p64-float16] | 0.2492 | 0.1505 | 60.4% | flashinfer |
| 🔴 | **gelu_and_mul_strategy** | test_fused_gated_strategy_bench[gelu_and_mul-1024-4096-float16-GeluAndMulFwdKernel-direct] | 0.0176 | 0.0107 | 60.7% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-float16] | 0.9013 | 0.5521 | 61.3% | fa3 |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-float16] | 0.1124 | 0.0692 | 61.5% | torch-compile |
| 🔴 | **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[global-1x1-float16] | 0.0132 | 0.0082 | 61.6% | torch-compile |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-float16] | 0.6332 | 0.3909 | 61.7% | fla |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s16k-h4-d64-bfloat16] | 0.6363 | 0.3930 | 61.8% | fla |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-float16] | 0.8932 | 0.5535 | 62.0% | fa3 |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-bfloat16] | 0.1122 | 0.0698 | 62.2% | torch-compile |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s896-bfloat16] | 0.0454 | 0.0283 | 62.3% | fa3 |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-hbm-streaming-threshold-float16] | 0.0608 | 0.0379 | 62.4% | marlin-fp32 |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s896-float16] | 0.0453 | 0.0284 | 62.6% | fa3 |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b8-dmem512-d256-bfloat16] | 0.0334 | 0.0213 | 63.8% | torch-compile |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[compile-smoke-square-64x64x128-float16] | 0.0043 | 0.0027 | 63.9% | torch-dequantized-matmul |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-float32] | 0.0195 | 0.0126 | 64.8% | torch-compile |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-float16] | 1.4190 | 0.9212 | 64.9% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s16k-h4-d64-bfloat16] | 1.4646 | 0.9554 | 65.2% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-float16] | 0.7360 | 0.4825 | 65.6% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-float16] | 0.3802 | 0.2494 | 65.6% | fla |
| 🔴 | **TopkSelectorFwdOp** | test_topk_selector_bench[topk2048-s32k-kv64k-float32] | 16.2512 | 10.6738 | 65.7% | flashinfer |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-l2-resident-ish-float16] | 0.0330 | 0.0217 | 65.7% | marlin-fp32 |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-bfloat16] | 0.3117 | 0.2054 | 65.9% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s8k-h4-d64-bfloat16] | 0.7520 | 0.4987 | 66.3% | fla |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s8k-h4-d64-float16] | 0.3091 | 0.2051 | 66.3% | fla |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-float16] | 0.2013 | 0.1339 | 66.5% | fla |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[resnet-stem-float32] | 0.1075 | 0.0715 | 66.6% | torch-compile |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s1792-float16] | 0.1289 | 0.0858 | 66.6% | fa3 |
| 🔴 | **AvgPool1dFwdOp** | test_avg_pool1d_bench[ceil-bfloat16] | 0.0035 | 0.0023 | 66.7% | torch-compile |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s4k-h4-d64-bfloat16] | 0.3882 | 0.2588 | 66.7% | fla |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-unbatched-complex64] | 0.0081 | 0.0054 | 66.9% | torch-cufft |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-8b-prefill-fp8tc-bn224-s1792-bfloat16] | 0.1289 | 0.0863 | 67.0% | fa3 |
| 🔴 | **GroupNormFwdOp** | test_group_norm_bench[wider-channel-g32-affine-float16] | 0.0059 | 0.0040 | 67.0% | flaggems |
| 🔴 | **GroupNormFwdOp** | test_group_norm_bench[tail-spatial-g16-affine-float16] | 0.0061 | 0.0041 | 67.0% | flaggems |
| 🔴 | **AvgPool1dFwdOp** | test_avg_pool1d_bench[audio-downsample-float16] | 0.0062 | 0.0042 | 67.4% | torch-compile |
| 🔴 | **GroupNormFwdOp** | test_group_norm_no_affine_bench[tail-spatial-g16-float16] | 0.0052 | 0.0035 | 67.5% | torch-compile |
| 🔴 | **GatedDeltaNetBwdOp** | test_gated_deltanet_vs_fla_bwd[gdn-bwd-b2-s2k-h4-d64-bfloat16] | 0.2053 | 0.1400 | 68.2% | fla |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-bfloat16] | 0.0960 | 0.0658 | 68.5% | fla |
| 🔴 | **BmmFp8KNFwdOp** | test_bmm_fp8_kn_bench[moe-prefill-b128-per-tensor-float8_e4m3fn] | 0.9007 | 0.6236 | 69.2% | flashinfer-bmm-fp8 |
| 🔴 | **FusedAddRMSNormFwdOp** | test_fused_add_rms_norm_bench[llama-405b-decode-bfloat16] | 0.0062 | 0.0044 | 70.1% | flashinfer |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s3584-float16] | 0.7497 | 0.5284 | 70.5% | fa3 |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-float16] | 0.0985 | 0.0699 | 71.0% | fla |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s7168-float16] | 2.8489 | 2.0249 | 71.1% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s7168-bfloat16] | 2.8523 | 2.0275 | 71.1% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-float16] | 0.8333 | 0.5926 | 71.1% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillFwdOp** | test_gqa_prefill_fp8_tensor_core_bench[llama-70b-prefill-fp8tc-bn224-s3584-bfloat16] | 0.7493 | 0.5334 | 71.2% | fa3 |
| 🔴 | **SharedFusedMoE** | test_shared_fused_moe_bench[1-384-8-7168-2048-18432-sigmoid-renormalize-correctionbias-2.827-bfloat16] | 0.5980 | 0.4266 | 71.3% | vllm |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.8085 | 0.5801 | 71.7% | fa3 |
| 🔴 | **MaxPool2dFwdOp** | test_max_pool2d_bench[resnet-stem-bfloat16] | 0.0471 | 0.0340 | 72.2% | torch-compile |
| 🔴 | **GroupNormFwdOp** | test_group_norm_no_affine_bench[wider-channel-g32-float16] | 0.0048 | 0.0035 | 72.2% | flaggems |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-softcap50-float16] | 0.1740 | 0.1256 | 72.2% | flashinfer |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0570 | 0.0412 | 72.3% | flashinfer |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-float16] | 0.1487 | 0.1077 | 72.4% | fla |
| 🔴 | **MaxPool2dFwdOp** | test_max_pool2d_bench[resnet-stem-float16] | 0.0471 | 0.0341 | 72.5% | torch-compile |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-float16] | 0.0571 | 0.0414 | 72.6% | flashinfer |
| 🔴 | **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[nondiv-7x7-bfloat16] | 0.0158 | 0.0115 | 72.6% | torch-ref |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-2k-bfloat16] | 0.2793 | 0.2035 | 72.9% | torch-cublas |
| 🔴 | **silu_and_mul_strategy** | test_fused_gated_strategy_bench[silu_and_mul-1024-4096-float32-SiluAndMulFwdKernel-direct] | 0.0200 | 0.0146 | 73.0% | torch-compile |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[alexnet-ceil-bfloat16] | 0.0237 | 0.0174 | 73.5% | torch-compile |
| 🔴 | **MaxPool1dIndicesFwdOp** | test_max_pool1d_indices_bench[sincnet-speaker-local-float16] | 0.0217 | 0.0160 | 73.8% | torch-compile |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-2k-float16] | 0.2826 | 0.2090 | 74.0% | torch-cublas |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-bfloat16] | 0.0930 | 0.0688 | 74.0% | flashinfer |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-float16] | 0.0930 | 0.0691 | 74.3% | flashinfer |
| 🔴 | **BmmFwdOp** | test_bmm_bench[moe-prefill-b128-bfloat16] | 0.2905 | 0.2157 | 74.3% | torch-cublas |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[alexnet-ceil-float16] | 0.0237 | 0.0177 | 74.5% | torch-compile |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s4k-h4-d64-bfloat16] | 0.1444 | 0.1079 | 74.7% | fla |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b4-4k-bfloat16] | 1.0383 | 0.7768 | 74.8% | torch-cublas |
| 🔴 | **Conv2dFwdOp** | test_conv2d_bench[highres-3x3-s1-float16] | 0.1048 | 0.0788 | 75.2% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-float16] | 0.6175 | 0.4652 | 75.3% | fla |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-float16] | 0.1657 | 0.1252 | 75.5% | flashinfer |
| 🔴 | **RopeNonNeoxFwdOp** | test_rope_non_neox_bench[non-neox-2d-b2-s2k-h32-d128-bfloat16] | 0.0252 | 0.0190 | 75.6% | torch-compile |
| 🔴 | **Conv2dFwdOp** | test_conv2d_bench[highres-3x3-s1-bias-float16] | 0.1049 | 0.0793 | 75.6% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-bfloat16] | 0.3114 | 0.2357 | 75.7% | fla |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-1k-bfloat16] | 0.0407 | 0.0313 | 76.8% | torch-cublas |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-1k-float16] | 0.0404 | 0.0311 | 77.0% | torch-cublas |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.3503 | 0.2702 | 77.1% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.6680 | 0.5162 | 77.3% | flashinfer |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-float16] | 0.3517 | 0.2729 | 77.6% | fa3 |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-float16] | 0.0865 | 0.0672 | 77.6% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-float16] | 0.6692 | 0.5203 | 77.7% | flashinfer |
| 🔴 | **GatedDeltaNetBHTDFwdOp** | test_gated_deltanet_bhtd_vs_fla_fwd[gdn-bhtd-b2-s2k-h4-d64-bfloat16] | 0.0866 | 0.0673 | 77.8% | fla |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-bfloat16] | 0.6113 | 0.4771 | 78.0% | fla |
| 🔴 | **GatedDeltaNetPrefillBHTDFwdOp** | test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-float16] | 0.2512 | 0.1963 | 78.1% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowFwdOp** | test_gqa_sliding_window_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.1511 | 0.1183 | 78.3% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowFwdOp** | test_gqa_sliding_window_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.1516 | 0.1188 | 78.4% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowFwdOp** | test_gqa_sliding_window_fwd_bench[llama-8b-long-w1024-float16] | 0.1528 | 0.1198 | 78.4% | fa3 |
| 🔴 | **GatedDeltaNetPrefillBHTDFwdOp** | test_gated_deltanet_prefill_bhtd_bench[bhtd-fallback-gdn-prefill-b1-s4k-h16-d128-bfloat16] | 0.2516 | 0.1979 | 78.7% | fla |
| 🔴 | **GroupedGemmFwdOp** | test_grouped_gemm_bench[nn-batch16-m4096-n4096-k4096-float16] | 0.3415 | 0.2694 | 78.9% | torch |
| 🔴 | **Conv2dFwdOp** | test_conv2d_bench[classifier-1x1-float16] | 0.0091 | 0.0072 | 79.0% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-float16] | 0.3128 | 0.2473 | 79.1% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowFwdOp** | test_gqa_sliding_window_fwd_bench[llama-70b-long-w1024-float16] | 0.1524 | 0.1206 | 79.1% | fa3 |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-large-bfloat16] | 0.0715 | 0.0568 | 79.4% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s4k-h4-d64-float16] | 0.1568 | 0.1253 | 79.9% | fla |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 9 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 750 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 2589 lines in `ops/`, 39.2% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 3592 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

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
| `ops/convolution.py` | 120 | 74.1% |
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
