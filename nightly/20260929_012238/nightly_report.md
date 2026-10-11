# ❌ TileOPs Nightly Report

> **2026-09-28 20:10** &ensp;|&ensp; `fa8acf71` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Correctness** | ✅ &ensp; (510/510 tests across 83 ops) |
| **Benchmarked Ops** | 177 |
| **Benchmark Failures** | ✅ None |
| **Regressions** (vs 14-day median) | ⚠️ 13 |
| **Baseline Alerts** (< 80%) | ⚠️ 21 |
| **History window** | 13 runs, 2026-09-15 to 2026-09-27 |
| **Roofline anomalies** | ✅ None |
| **Improvements** (vs 14-day best) | 🎉 66 |
| **Moved since previous run** | 🔵 80 |
| **Never-built kernels** | ⚠️ 19 files **−1** &ensp;·&ensp; `kernels/linear_attention/gated_deltanet/prefill/forward.py` at 3.5% |
| **Untested roofline math** | 414 lines in `perf/` **+88** &ensp;·&ensp; `perf/formulas.py` at 17.3% |
| **Untested op logic** | 868 lines in `ops/` **−11** &ensp;·&ensp; 58.1% of branches taken **+3.5pp** |
| | <sub>coverage compared against the 2026-09-27 run; no figure means it held</sub> |

## ⚠️ Performance Regressions (vs 14-day median)

| Op | Config | Median (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **FloorDivideFwdOp** | test_floor_divide_bench[cnn-feat-broadcast-float16] | 0.0158 | 0.0225 | +42.6% | 1.14 |
| **FloorDivideFwdOp** | test_floor_divide_bench[cnn-feat-broadcast-bfloat16] | 0.0157 | 0.0221 | +41.2% | 1.16 |
| **FloorDivideFwdOp** | test_floor_divide_bench[linear-bias-bfloat16] | 0.0066 | 0.0093 | +41.2% | 0.91 |
| **RemainderFwdOp** | test_remainder_bench[linear-bias-bfloat16] | 0.0066 | 0.0093 | +40.1% | 1.81 |
| **FloorDivideFwdOp** | test_floor_divide_bench[linear-bias-float16] | 0.0065 | 0.0088 | +34.3% | 0.96 |
| **RemainderFwdOp** | test_remainder_bench[linear-bias-float16] | 0.0066 | 0.0088 | +32.9% | 1.91 |
| **RemainderFwdOp** | test_remainder_bench[cnn-feat-broadcast-float16] | 0.0158 | 0.0202 | +27.3% | 2.55 |
| **RemainderFwdOp** | test_remainder_bench[cnn-feat-broadcast-bfloat16] | 0.0158 | 0.0198 | +25.1% | 2.59 |
| **FloorDivideFwdOp** | test_floor_divide_bench[llama-7b-ffn-bfloat16] | 0.0188 | 0.0224 | +19.1% | 1.00 |
| **FloorDivideFwdOp** | test_floor_divide_bench[hidden-state-prefill-bfloat16] | 0.0149 | 0.0176 | +18.5% | 0.95 |
| **RemainderFwdOp** | test_remainder_bench[llama-7b-ffn-bfloat16] | 0.0189 | 0.0221 | +17.3% | 2.04 |
| **RemainderFwdOp** | test_remainder_bench[hidden-state-prefill-bfloat16] | 0.0149 | 0.0174 | +16.3% | 1.93 |
| **FloorDivideFwdOp** | test_floor_divide_bench[llama-7b-hidden-float16] | 0.0087 | 0.0097 | +11.0% | 0.87 |

## 🎉 Performance Improvements (vs 14-day best)

| Op | Config | Prev Best (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **ProdFwdOp** | test_prod_bench[3d-non-last-axis-float16] | 0.6009 | 0.0034 | -99.4% | 0.62 |
| **InstanceNormFwdOp** | test_instance_norm_bench[image-track-stats-float16] | 0.0326 | 0.0029 | -91.0% | 1.78 |
| **BatchNormBwdOp** | test_batch_norm_bwd_bench[resnet-stage2-float16] | 0.0142 | 0.0029 | -79.3% | 1.60 |
| **BatchNormBwdOp** | test_batch_norm_bwd_bench[large-spatial-float16] | 6.8821 | 1.5091 | -78.1% | 3.20 |
| **BatchNormBwdOp** | test_batch_norm_bwd_bench[resnet-stage1-bfloat16] | 0.0150 | 0.0033 | -77.8% | 1.42 |
| **BatchNormBwdOp** | test_batch_norm_bwd_bench[resnet-stage1-float16] | 0.0149 | 0.0034 | -77.4% | 1.40 |
| **RMSNormFwdOp** | test_rms_norm_bench[qk-norm-head-bfloat16] | 0.0115 | 0.0027 | -76.5% | 1.16 |
| **BatchNormBwdOp** | test_batch_norm_bwd_bench[resnet-stage3-float16] | 0.0171 | 0.0042 | -75.7% | 1.74 |
| **MultiHeadAttentionDecodePagedWithKVCacheFwdOp** | test_mha_decode_paged_bench[speculative-decode-float16] | 0.0302 | 0.0075 | -75.3% | 2.24 |
| **InstanceNormFwdOp** | test_instance_norm_bench[image-eval-float16] | 0.0114 | 0.0028 | -75.3% | 1.49 |
| **AllFwdOp** | test_all_bench[3d-multidim-complex64] | 0.0295 | 0.0075 | -74.6% | 0.56 |
| **AnyFwdOp** | test_any_bench[3d-multidim-complex64] | 0.0295 | 0.0075 | -74.6% | 0.56 |
| **CountNonzeroFwdOp** | test_count_nonzero_bench[3d-multidim-complex64] | 0.0293 | 0.0075 | -74.5% | 0.56 |
| **BatchNormBwdOp** | test_batch_norm_bwd_bench[resnet-fc-float16] | 0.0070 | 0.0020 | -72.0% | 0.01 |
| **BatchNormBwdOp** | test_batch_norm_bwd_bench[resnet-stage3-float32] | 0.0177 | 0.0055 | -69.1% | 1.32 |
| **AllFwdOp** | test_all_bench[3d-multidim-complex128] | 0.0380 | 0.0126 | -66.9% | 0.33 |
| **AnyFwdOp** | test_any_bench[3d-multidim-complex128] | 0.0380 | 0.0126 | -66.9% | 0.33 |
| **CountNonzeroFwdOp** | test_count_nonzero_bench[3d-multidim-complex128] | 0.0378 | 0.0126 | -66.8% | 0.33 |
| **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-short-bfloat16] | 0.4080 | 0.1423 | -65.1% | 150.96 |
| **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-short-bfloat16] | 0.4141 | 0.1495 | -63.9% | 143.64 |
| **AnyFwdOp** | test_any_bench[mask-validation-32k-int32] | 0.0097 | 0.0036 | -63.2% | 0.59 |
| **AllFwdOp** | test_all_bench[mask-validation-32k-int32] | 0.0097 | 0.0036 | -62.8% | 0.58 |
| **CountNonzeroFwdOp** | test_count_nonzero_bench[sparsity-seq-int32] | 0.0096 | 0.0037 | -61.8% | 0.57 |
| **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-bfloat16] | 1.2417 | 0.5680 | -54.3% | 302.47 |
| **AnyFwdOp** | test_any_bench[mask-validation-32k-int64] | 0.0105 | 0.0049 | -53.0% | 0.43 |
| **AllFwdOp** | test_all_bench[mask-validation-32k-int64] | 0.0105 | 0.0050 | -52.1% | 0.42 |
| **CountNonzeroFwdOp** | test_count_nonzero_bench[sparsity-seq-int64] | 0.0104 | 0.0051 | -51.2% | 0.41 |
| **LogSumExpFwdOp** | test_logsumexp_bench[llama-8b-lm-head-float32] | 0.0093 | 0.0047 | -49.7% | 0.44 |
| **LogSumExpFwdOp** | test_logsumexp_bench[lm-head-bfloat16] | 0.0082 | 0.0041 | -49.6% | 0.40 |
| **LogSumExpFwdOp** | test_logsumexp_bench[lm-head-float16] | 0.0081 | 0.0041 | -49.0% | 0.40 |
| **MoePermuteAlignFwdOp** | test_permute_align_bench[qwen3-235b-t1] | 0.0108 | 0.0056 | -47.6% | - |
| **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 1.0162 | 0.5631 | -44.6% | 305.08 |
| **MoePermuteAlignFwdOp** | test_permute_align_bench[qwen3-235b-t32] | 0.0121 | 0.0070 | -42.5% | - |
| **MoePermuteAlignFwdOp** | test_permute_align_bench[qwen3-235b-t512] | 0.0142 | 0.0091 | -35.8% | - |
| **MoePermuteAlignFwdOp** | test_permute_align_bench[ds-v3-t32] | 0.0153 | 0.0099 | -35.6% | - |
| **MoePermuteAlignFwdOp** | test_permute_align_bench[ds-v3-t1] | 0.0148 | 0.0096 | -35.1% | - |
| **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-float16] | 0.8312 | 0.5664 | -31.9% | 303.32 |
| **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.8071 | 0.5617 | -30.4% | 305.86 |
| **MoePermuteAlignFwdOp** | test_permute_align_bench[ds-v3-t512] | 0.0176 | 0.0123 | -29.9% | - |
| **MoePermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t32] | 0.0193 | 0.0136 | -29.6% | - |
| **MoePermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t1] | 0.0167 | 0.0118 | -29.6% | - |
| **CountNonzeroFwdOp** | test_count_nonzero_bench[sparsity-mlp-float16] | 0.0220 | 0.0158 | -28.3% | 2.85 |
| **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-short-float16] | 0.1964 | 0.1416 | -27.9% | 151.69 |
| **CountNonzeroFwdOp** | test_count_nonzero_bench[sparsity-seq-bool] | 0.0034 | 0.0024 | -27.6% | 0.86 |
| **MoePermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t512] | 0.0217 | 0.0158 | -26.9% | - |
| **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-short-float16] | 0.2029 | 0.1498 | -26.2% | 143.36 |
| **AnyFwdOp** | test_any_bench[3d-multidim-bool] | 0.0035 | 0.0027 | -22.2% | 0.78 |
| **CountNonzeroFwdOp** | test_count_nonzero_bench[sparsity-seq-float16] | 0.0037 | 0.0029 | -21.6% | 0.72 |
| **AllFwdOp** | test_all_bench[3d-multidim-bool] | 0.0035 | 0.0028 | -20.4% | 0.76 |
| **ProdFwdOp** | test_prod_bench[mlp-intermediate-float32] | 0.0316 | 0.0252 | -20.2% | 0.89 |
| **MultiHeadAttentionDecodePagedWithKVCacheFwdOp** | test_mha_decode_paged_bench[serving-b2-float16] | 0.0071 | 0.0057 | -19.4% | 0.75 |
| **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-b64-p64-float16-float16] | 0.3094 | 0.2604 | -15.8% | 8.33 |
| **MoePermuteAlignFwdOp** | test_permute_align_bench[ds-v3-t4096] | 0.0375 | 0.0323 | -13.9% | - |
| **MoePermuteAlignFwdOp** | test_permute_align_bench[qwen3-235b-t4096] | 0.0316 | 0.0272 | -13.9% | - |
| **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-p64-float16-float16] | 0.2249 | 0.1945 | -13.5% | 11.15 |
| **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-b64-p16-float16-float16] | 0.4601 | 0.3995 | -13.2% | 5.43 |
| **AminFwdOp** | test_amin_bench[mlp-intermediate-float32] | 0.0290 | 0.0253 | -12.9% | 0.89 |
| **AmaxFwdOp** | test_amax_bench[mlp-intermediate-float32] | 0.0290 | 0.0253 | -12.9% | 0.89 |
| **SumFwdOp** | test_sum_bench[mlp-intermediate-float32] | 0.0290 | 0.0253 | -12.8% | 0.89 |
| **MeanFwdOp** | test_mean_bench[mlp-intermediate-float32] | 0.0291 | 0.0253 | -12.8% | 0.89 |
| **L2NormFwdOp** | test_l2_norm_bench[mlp-intermediate-float32] | 0.0289 | 0.0253 | -12.4% | 1.78 |
| **L1NormFwdOp** | test_l1_norm_bench[mlp-intermediate-float32] | 0.0288 | 0.0253 | -12.3% | 1.78 |
| **InfNormFwdOp** | test_inf_norm_bench[mlp-intermediate-float32] | 0.0289 | 0.0253 | -12.2% | 1.78 |
| **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-p64-softcap-float16-float16] | 0.2382 | 0.2109 | -11.5% | 10.34 |
| **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-p16-float16-float16] | 0.3803 | 0.3380 | -11.1% | 6.42 |
| **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-p256-float16-float16] | 0.2055 | 0.1835 | -10.7% | 11.82 |

## 🔵 Moved Since Previous Run

> Moves against the most recent reading. A row restored to its old level appears only here: returning is not a new 14-day record.

| Op | Config | Previous (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **ProdFwdOp** | test_prod_bench[3d-non-last-axis-float16] | 0.6009 | 0.0034 | -99.4% | 0.62 |
| **InstanceNormFwdOp** | test_instance_norm_bench[image-track-stats-float16] | 0.0326 | 0.0029 | -91.0% | 1.78 |
| **BatchNormBwdOp** | test_batch_norm_bwd_bench[resnet-stage2-float16] | 0.0142 | 0.0029 | -79.3% | 1.60 |
| **BatchNormBwdOp** | test_batch_norm_bwd_bench[large-spatial-float16] | 6.8821 | 1.5091 | -78.1% | 3.20 |
| **BatchNormBwdOp** | test_batch_norm_bwd_bench[resnet-stage1-bfloat16] | 0.0150 | 0.0033 | -77.8% | 1.42 |
| **BatchNormBwdOp** | test_batch_norm_bwd_bench[resnet-stage1-float16] | 0.0149 | 0.0034 | -77.4% | 1.40 |
| **RMSNormFwdOp** | test_rms_norm_bench[qk-norm-head-bfloat16] | 0.0115 | 0.0027 | -76.5% | 1.16 |
| **BatchNormBwdOp** | test_batch_norm_bwd_bench[resnet-stage3-float16] | 0.0171 | 0.0042 | -75.7% | 1.74 |
| **MultiHeadAttentionDecodePagedWithKVCacheFwdOp** | test_mha_decode_paged_bench[speculative-decode-float16] | 0.0302 | 0.0075 | -75.3% | 2.24 |
| **InstanceNormFwdOp** | test_instance_norm_bench[image-eval-float16] | 0.0114 | 0.0028 | -75.3% | 1.49 |
| **AllFwdOp** | test_all_bench[3d-multidim-complex64] | 0.0295 | 0.0075 | -74.6% | 0.56 |
| **AnyFwdOp** | test_any_bench[3d-multidim-complex64] | 0.0295 | 0.0075 | -74.6% | 0.56 |
| **CountNonzeroFwdOp** | test_count_nonzero_bench[3d-multidim-complex64] | 0.0293 | 0.0075 | -74.5% | 0.56 |
| **BatchNormBwdOp** | test_batch_norm_bwd_bench[resnet-fc-float16] | 0.0070 | 0.0020 | -72.0% | 0.01 |
| **BatchNormBwdOp** | test_batch_norm_bwd_bench[resnet-stage3-float32] | 0.0177 | 0.0055 | -69.1% | 1.32 |
| **AllFwdOp** | test_all_bench[3d-multidim-complex128] | 0.0380 | 0.0126 | -66.9% | 0.33 |
| **AnyFwdOp** | test_any_bench[3d-multidim-complex128] | 0.0380 | 0.0126 | -66.9% | 0.33 |
| **CountNonzeroFwdOp** | test_count_nonzero_bench[3d-multidim-complex128] | 0.0378 | 0.0126 | -66.8% | 0.33 |
| **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-short-bfloat16] | 0.4083 | 0.1423 | -65.2% | 150.96 |
| **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-short-bfloat16] | 0.4147 | 0.1495 | -63.9% | 143.64 |
| **AnyFwdOp** | test_any_bench[mask-validation-32k-int32] | 0.0097 | 0.0036 | -63.2% | 0.59 |
| **AllFwdOp** | test_all_bench[mask-validation-32k-int32] | 0.0097 | 0.0036 | -62.8% | 0.58 |
| **CountNonzeroFwdOp** | test_count_nonzero_bench[sparsity-seq-int32] | 0.0097 | 0.0037 | -61.9% | 0.57 |
| **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-bfloat16] | 1.2420 | 0.5680 | -54.3% | 302.47 |
| **AnyFwdOp** | test_any_bench[mask-validation-32k-int64] | 0.0105 | 0.0049 | -53.0% | 0.43 |
| **AllFwdOp** | test_all_bench[mask-validation-32k-int64] | 0.0105 | 0.0050 | -52.1% | 0.42 |
| **CountNonzeroFwdOp** | test_count_nonzero_bench[sparsity-seq-int64] | 0.0104 | 0.0051 | -51.2% | 0.41 |
| **LogSumExpFwdOp** | test_logsumexp_bench[lm-head-float16] | 0.0083 | 0.0041 | -50.3% | 0.40 |
| **LogSumExpFwdOp** | test_logsumexp_bench[lm-head-bfloat16] | 0.0083 | 0.0041 | -50.2% | 0.40 |
| **LogSumExpFwdOp** | test_logsumexp_bench[llama-8b-lm-head-float32] | 0.0093 | 0.0047 | -49.7% | 0.44 |
| **MoePermuteAlignFwdOp** | test_permute_align_bench[qwen3-235b-t1] | 0.0108 | 0.0056 | -47.6% | - |
| **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 1.0174 | 0.5631 | -44.6% | 305.08 |
| **MoePermuteAlignFwdOp** | test_permute_align_bench[qwen3-235b-t32] | 0.0121 | 0.0070 | -42.5% | - |
| **MoePermuteAlignFwdOp** | test_permute_align_bench[qwen3-235b-t512] | 0.0142 | 0.0091 | -35.8% | - |
| **MoePermuteAlignFwdOp** | test_permute_align_bench[ds-v3-t32] | 0.0153 | 0.0099 | -35.6% | - |
| **MoePermuteAlignFwdOp** | test_permute_align_bench[ds-v3-t1] | 0.0148 | 0.0096 | -35.1% | - |
| **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-float16] | 0.8329 | 0.5664 | -32.0% | 303.32 |
| **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.8093 | 0.5617 | -30.6% | 305.86 |
| **MoePermuteAlignFwdOp** | test_permute_align_bench[ds-v3-t512] | 0.0176 | 0.0123 | -29.9% | - |
| **MoePermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t32] | 0.0193 | 0.0136 | -29.6% | - |
| **MoePermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t1] | 0.0167 | 0.0118 | -29.6% | - |
| **CountNonzeroFwdOp** | test_count_nonzero_bench[sparsity-mlp-float16] | 0.0220 | 0.0158 | -28.3% | 2.85 |
| **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-short-float16] | 0.1970 | 0.1416 | -28.1% | 151.69 |
| **CountNonzeroFwdOp** | test_count_nonzero_bench[sparsity-seq-bool] | 0.0034 | 0.0024 | -27.6% | 0.86 |
| **MoePermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t512] | 0.0217 | 0.0158 | -26.9% | - |
| **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-short-float16] | 0.2034 | 0.1498 | -26.3% | 143.36 |
| **AnyFwdOp** | test_any_bench[3d-multidim-bool] | 0.0035 | 0.0027 | -23.0% | 0.78 |
| **CountNonzeroFwdOp** | test_count_nonzero_bench[sparsity-seq-float16] | 0.0037 | 0.0029 | -22.2% | 0.72 |
| **AllFwdOp** | test_all_bench[3d-multidim-bool] | 0.0035 | 0.0028 | -21.5% | 0.76 |
| **ProdFwdOp** | test_prod_bench[mlp-intermediate-float32] | 0.0316 | 0.0252 | -20.2% | 0.89 |
| **MultiHeadAttentionDecodePagedWithKVCacheFwdOp** | test_mha_decode_paged_bench[serving-b2-float16] | 0.0071 | 0.0057 | -19.4% | 0.75 |
| **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-b64-p64-float16-float16] | 0.3094 | 0.2604 | -15.8% | 8.33 |
| **MoePermuteAlignFwdOp** | test_permute_align_bench[ds-v3-t4096] | 0.0376 | 0.0323 | -14.0% | - |
| **MoePermuteAlignFwdOp** | test_permute_align_bench[qwen3-235b-t4096] | 0.0316 | 0.0272 | -13.9% | - |
| **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-p64-float16-float16] | 0.2249 | 0.1945 | -13.5% | 11.15 |
| **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-b64-p16-float16-float16] | 0.4601 | 0.3995 | -13.2% | 5.43 |
| **SumFwdOp** | test_sum_bench[mlp-intermediate-float32] | 0.0291 | 0.0253 | -13.0% | 0.89 |
| **AmaxFwdOp** | test_amax_bench[mlp-intermediate-float32] | 0.0291 | 0.0253 | -13.0% | 0.89 |
| **AminFwdOp** | test_amin_bench[mlp-intermediate-float32] | 0.0290 | 0.0253 | -12.9% | 0.89 |
| **MeanFwdOp** | test_mean_bench[mlp-intermediate-float32] | 0.0291 | 0.0253 | -12.8% | 0.89 |
| **L2NormFwdOp** | test_l2_norm_bench[mlp-intermediate-float32] | 0.0289 | 0.0253 | -12.5% | 1.78 |
| **L1NormFwdOp** | test_l1_norm_bench[mlp-intermediate-float32] | 0.0288 | 0.0253 | -12.3% | 1.78 |
| **InfNormFwdOp** | test_inf_norm_bench[mlp-intermediate-float32] | 0.0289 | 0.0253 | -12.2% | 1.78 |
| **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-p64-softcap-float16-float16] | 0.2382 | 0.2109 | -11.5% | 10.34 |
| **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-p16-float16-float16] | 0.3803 | 0.3380 | -11.1% | 6.42 |
| **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-p256-float16-float16] | 0.2055 | 0.1835 | -10.7% | 11.82 |
| **FloorDivideFwdOp** | test_floor_divide_bench[llama-7b-hidden-float16] | 0.0087 | 0.0097 | +11.0% | 0.87 |
| **RemainderFwdOp** | test_remainder_bench[hidden-state-prefill-float16] | 0.0148 | 0.0165 | +11.3% | 2.03 |
| **RemainderFwdOp** | test_remainder_bench[hidden-state-prefill-bfloat16] | 0.0148 | 0.0174 | +17.3% | 1.93 |
| **RemainderFwdOp** | test_remainder_bench[llama-7b-ffn-bfloat16] | 0.0189 | 0.0221 | +17.3% | 2.04 |
| **FloorDivideFwdOp** | test_floor_divide_bench[hidden-state-prefill-bfloat16] | 0.0148 | 0.0176 | +19.0% | 0.95 |
| **FloorDivideFwdOp** | test_floor_divide_bench[llama-7b-ffn-bfloat16] | 0.0188 | 0.0224 | +19.1% | 1.00 |
| **RemainderFwdOp** | test_remainder_bench[cnn-feat-broadcast-bfloat16] | 0.0159 | 0.0198 | +24.5% | 2.59 |
| **RemainderFwdOp** | test_remainder_bench[cnn-feat-broadcast-float16] | 0.0159 | 0.0202 | +26.8% | 2.55 |
| **RemainderFwdOp** | test_remainder_bench[linear-bias-float16] | 0.0066 | 0.0088 | +32.9% | 1.91 |
| **FloorDivideFwdOp** | test_floor_divide_bench[linear-bias-float16] | 0.0065 | 0.0088 | +34.3% | 0.96 |
| **RemainderFwdOp** | test_remainder_bench[linear-bias-bfloat16] | 0.0066 | 0.0093 | +40.1% | 1.81 |
| **FloorDivideFwdOp** | test_floor_divide_bench[cnn-feat-broadcast-bfloat16] | 0.0158 | 0.0221 | +40.4% | 1.16 |
| **FloorDivideFwdOp** | test_floor_divide_bench[linear-bias-bfloat16] | 0.0066 | 0.0093 | +41.2% | 0.91 |
| **FloorDivideFwdOp** | test_floor_divide_bench[cnn-feat-broadcast-float16] | 0.0158 | 0.0225 | +42.6% | 1.14 |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 80%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-b64-p16-float16-float16] | 0.3995 | 0.2211 | 55.4% | flashinfer |
| 🔴 | **FusedTopKFwdOp** | test_fused_topk_bench[kimi-k2-t512-bias-float32] | 0.0117 | 0.0072 | 61.3% | vllm |
| 🔴 | **MultiHeadLatentAttentionDecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-32k-bfloat16] | 0.3929 | 0.2441 | 62.1% | torch-compile |
| 🔴 | **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-p16-float16-float16] | 0.3380 | 0.2186 | 64.7% | flashinfer |
| 🔴 | **FloorDivideFwdOp** | test_floor_divide_bench[cnn-feat-broadcast-float16] | 0.0225 | 0.0158 | 70.1% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-qkv-a-2d-float8_e4m3fn-bfloat16] | 0.1527 | 0.1096 | 71.8% | deepgemm |
| 🔴 | **FloorDivideFwdOp** | test_floor_divide_bench[cnn-feat-broadcast-bfloat16] | 0.0221 | 0.0160 | 72.1% | torch-compile |
| 🔴 | **FloorDivideFwdOp** | test_floor_divide_bench[linear-bias-bfloat16] | 0.0093 | 0.0067 | 72.2% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-q-b-2d-float8_e4m3fn-bfloat16] | 0.3575 | 0.2624 | 73.4% | deepgemm |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-m1-down-2d-float8_e4m3fn-bfloat16] | 0.0104 | 0.0077 | 73.6% | flashinfer-fp8-blockscale-sm90 |

<details>
<summary><strong>11 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-down-2d-float8_e4m3fn-bfloat16] | 0.1447 | 0.1069 | 73.9% | deepgemm |
| 🔴 | **FloorDivideFwdOp** | test_floor_divide_bench[linear-bias-float16] | 0.0088 | 0.0066 | 75.5% | torch-compile |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-mlp-up-2d-float8_e4m3fn-bfloat16] | 0.2420 | 0.1885 | 77.9% | deepgemm |
| 🔴 | **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-p256-float16-float16] | 0.1835 | 0.1429 | 77.9% | fa3 |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[train-16k-float16] | 0.6176 | 0.4837 | 78.3% | fla |
| 🔴 | **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-405b-p256-float16-float16] | 0.0394 | 0.0309 | 78.5% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 0.5631 | 0.4449 | 79.0% | fa3 |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[train-2k-float16] | 0.0984 | 0.0779 | 79.1% | fla |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.5617 | 0.4452 | 79.3% | fa3 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-o-proj-2d-float8_e4m3fn-bfloat16] | 0.8718 | 0.6917 | 79.3% | deepgemm |
| 🔴 | **EngramGateConvBwdOp** | test_engram_gate_conv_bwd_bench[train-s96-bfloat16] | 0.1048 | 0.0833 | 79.4% | torch-compile |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 19 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 414 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 868 lines in `ops/`, 58.1% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 2515 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

### Never-built kernels

| File | Executed |
| --- | --- |
| `kernels/linear_attention/gated_deltanet/prefill/forward.py` | 3.5% |
| `kernels/linear_attention/gated_deltanet/prefill/prepare.py` | 3.7% |
| `kernels/attention/gqa_fwd_fp8.py` | 8.6% |
| `kernels/attention/gqa_fwd.py` | 8.6% |
| `kernels/attention/deepseek_mla_decode.py` | 8.9% |
| `kernels/attention/gqa_dense.py` | 12.0% |
| `kernels/attention/gqa_decode.py` | 14.8% |
| `kernels/linear_attention/gla/dense_prefill_partitioned.py` | 15.0% |
| `kernels/attention/gqa_decode_bs1.py` | 15.2% |
| `kernels/moe/indexed_expert_gemm.py` | 15.4% |
| `kernels/linear_attention/gla/dense_prefill_subchunk.py` | 16.5% |
| `kernels/attention/deepseek_nsa_cmp_fwd.py` | 17.6% |
| `kernels/grouped_gemm/grouped_gemm.py` | 17.7% |
| `kernels/attention/gqa_decode_fp8.py` | 17.8% |
| `kernels/linear_attention/gated_deltanet/decode.py` | 17.8% |
| `kernels/attention/gqa_prefill_varlen_fwd.py` | 22.0% |
| `kernels/linear_attention/gated_deltanet/prefill/dense.py` | 22.1% |
| `kernels/linear_attention/deltanet/dense_prefill.py` | 24.1% |
| `kernels/moe/shared_expert_mlp.py` | 24.5% |

<details>
<summary>Untested pure Python, worst 15 files</summary>

| File | Uncovered | Executed |
| --- | --- | --- |
| `perf/formulas.py` | 372 | 17.3% |
| `manifest/plan.py` | 349 | 30.3% |
| `manifest/workload.py` | 194 | 58.5% |
| `manifest/primitives.py` | 146 | 54.8% |
| `ops/op_base.py` | 136 | 71.4% |
| `manifest/expr.py` | 122 | 70.7% |
| `ops/attention/gqa.py` | 107 | 57.7% |
| `manifest/signature.py` | 105 | 77.2% |
| `ops/_signature_codegen.py` | 75 | 90.3% |
| `trace/ui.py` | 62 | 24.4% |
| `manifest/kinds.py` | 53 | 79.2% |
| `ops/linear_attention/gated_deltanet.py` | 49 | 27.9% |
| `perf/profile.py` | 42 | 22.2% |
| `backend/registry.py` | 40 | 52.9% |
| `ops/moe/routed_expert/indexed_routed_expert.py` | 38 | 45.7% |

</details>

Per-line detail is in the `htmlcov/` directory of this run's `tileops_op_test` artifact.
