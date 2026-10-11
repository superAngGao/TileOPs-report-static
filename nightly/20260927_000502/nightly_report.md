# ❌ TileOPs Nightly Report

> **2026-09-26 19:05** &ensp;|&ensp; `44727e21` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Correctness** | ✅ &ensp; (517/517 tests across 85 ops) |
| **Benchmarked Ops** | 179 |
| **Benchmark Failures** | ✅ None &ensp;|&ensp; ⚠️ 3 skipped |
| **Regressions** (vs 14-day median) | ⚠️ 7 |
| **Baseline Alerts** (< 80%) | ⚠️ 56 |
| **History window** | 13 runs, 2026-09-12 to 2026-09-25 |
| **Roofline anomalies** | ✅ None |
| **Improvements** (vs 14-day best) | 🎉 6 |
| **Moved since previous run** | 🔵 13 |
| **Never-built kernels** | ⚠️ 28 files &ensp;·&ensp; `kernels/linear_attention/gated_deltanet/compute_w_u_bwd.py` at 0.0% |
| **Untested roofline math** | 507 lines in `perf/` **−371** &ensp;·&ensp; `perf/formulas.py` at 9.0% |
| **Untested op logic** | 1847 lines in `ops/` **−745** &ensp;·&ensp; 37.2% of branches taken **+0.7pp** |
| | <sub>coverage compared against the 2026-09-25 run; no figure means it held</sub> |

## ⚠️ Performance Regressions (vs 14-day median)

| Op | Config | Median (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **SumFwdOp** | test_sum_bench[hidden-state-reduce-bfloat16-float32] | 0.0093 | 0.0385 | +315.2% | 0.22 |
| **BmmFp8FwdOp** | test_bmm_fp8_bench[mha-decode-b32-pv-per-tensor-float8_e4m3fn-bfloat16] | 0.0090 | 0.0148 | +63.8% | 145.26 |
| **BmmFp8FwdOp** | test_bmm_fp8_bench[mha-decode-b64-qk-per-tensor-float8_e4m3fn-bfloat16] | 0.0157 | 0.0247 | +56.9% | 173.85 |
| **BmmFp8FwdOp** | test_bmm_fp8_bench[moe-prefill-b128-per-tensor-float8_e4m3fn-bfloat16] | 0.1327 | 0.2013 | +51.7% | 682.61 |
| **BmmFp8FwdOp** | test_bmm_fp8_bench[square-b4-1k-per-tensor-float8_e4m3fn-float16] | 0.0118 | 0.0159 | +34.3% | 540.11 |
| **BmmFp8FwdOp** | test_bmm_fp8_bench[square-b4-1k-per-tensor-float8_e4m3fn-bfloat16] | 0.0118 | 0.0158 | +33.5% | 543.39 |
| **BmmFp8FwdOp** | test_bmm_fp8_bench[square-b8-2k-per-tensor-float8_e4m3fn-bfloat16] | 0.1206 | 0.1404 | +16.4% | 978.80 |

## 🎉 Performance Improvements (vs 14-day best)

| Op | Config | Prev Best (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **MoeExpertMLPFwdOp** | test_moe_expert_mlp_bench[qwen3-235b-prefill-bfloat16] | 6.8220 | 4.7518 | -30.3% | 607.48 |
| **MoeExpertMLPFwdOp** | test_moe_expert_mlp_bench[deepseek-v3-prefill-bfloat16] | 9.0563 | 6.4324 | -29.0% | 448.76 |
| **MoeExpertMLPFwdOp** | test_moe_expert_mlp_bench[deepseek-v3-prefill-float16] | 9.3663 | 6.6871 | -28.6% | 431.67 |
| **MoeGroupedGemmFwdOp** | test_moe_grouped_gemm_bench[deepseek-v3-prefill-down-bfloat16] | 2.9131 | 2.0893 | -28.3% | 460.48 |
| **MoeExpertMLPFwdOp** | test_moe_expert_mlp_bench[qwen3-235b-prefill-float16] | 6.9563 | 5.0338 | -27.6% | 573.45 |
| **MoeGroupedGemmFwdOp** | test_moe_grouped_gemm_bench[deepseek-v3-prefill-gate-up-bfloat16] | 5.7220 | 4.1898 | -26.8% | 459.25 |

## 🔵 Moved Since Previous Run

> Moves against the most recent reading. A row restored to its old level appears only here: returning is not a new 14-day record.

| Op | Config | Previous (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **MoeExpertMLPFwdOp** | test_moe_expert_mlp_bench[qwen3-235b-prefill-bfloat16] | 6.9073 | 4.7518 | -31.2% | 607.48 |
| **MoeExpertMLPFwdOp** | test_moe_expert_mlp_bench[deepseek-v3-prefill-bfloat16] | 9.2083 | 6.4324 | -30.1% | 448.76 |
| **MoeExpertMLPFwdOp** | test_moe_expert_mlp_bench[deepseek-v3-prefill-float16] | 9.5450 | 6.6871 | -29.9% | 431.67 |
| **MoeExpertMLPFwdOp** | test_moe_expert_mlp_bench[qwen3-235b-prefill-float16] | 7.1181 | 5.0338 | -29.3% | 573.45 |
| **MoeGroupedGemmFwdOp** | test_moe_grouped_gemm_bench[deepseek-v3-prefill-gate-up-bfloat16] | 5.8523 | 4.1898 | -28.4% | 459.25 |
| **MoeGroupedGemmFwdOp** | test_moe_grouped_gemm_bench[deepseek-v3-prefill-down-bfloat16] | 2.9131 | 2.0893 | -28.3% | 460.48 |
| **BmmFp8FwdOp** | test_bmm_fp8_bench[square-b8-2k-per-tensor-float8_e4m3fn-bfloat16] | 0.1206 | 0.1404 | +16.4% | 978.80 |
| **BmmFp8FwdOp** | test_bmm_fp8_bench[square-b4-1k-per-tensor-float8_e4m3fn-bfloat16] | 0.0118 | 0.0158 | +33.5% | 543.39 |
| **BmmFp8FwdOp** | test_bmm_fp8_bench[square-b4-1k-per-tensor-float8_e4m3fn-float16] | 0.0118 | 0.0159 | +34.3% | 540.11 |
| **BmmFp8FwdOp** | test_bmm_fp8_bench[moe-prefill-b128-per-tensor-float8_e4m3fn-bfloat16] | 0.1330 | 0.2013 | +51.4% | 682.61 |
| **BmmFp8FwdOp** | test_bmm_fp8_bench[mha-decode-b64-qk-per-tensor-float8_e4m3fn-bfloat16] | 0.0158 | 0.0247 | +56.6% | 173.85 |
| **BmmFp8FwdOp** | test_bmm_fp8_bench[mha-decode-b32-pv-per-tensor-float8_e4m3fn-bfloat16] | 0.0090 | 0.0148 | +63.8% | 145.26 |
| **SumFwdOp** | test_sum_bench[hidden-state-reduce-bfloat16-float32] | 0.0092 | 0.0385 | +316.6% | 0.22 |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 80%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **ProdFwdOp** | test_prod_bench[3d-non-last-axis-reduce-float16] | 0.6009 | 0.0035 | 0.6% | torch-compile |
| 🔴 | **InstanceNormFwdOp** | test_instance_norm_bench[image-track-running-stats-float16] | 0.0330 | 0.0029 | 8.9% | torch-compile |
| 🔴 | **SumFwdOp** | test_sum_bench[hidden-state-reduce-bfloat16-float32] | 0.0385 | 0.0083 | 21.6% | torch-compile |
| 🔴 | **MeanFwdOp** | test_mean_bench[hidden-state-reduce-bfloat16-float32] | 0.0386 | 0.0084 | 21.7% | torch-compile |
| 🔴 | **ProdFwdOp** | test_prod_bench[hidden-state-reduce-bfloat16-float32] | 0.0374 | 0.0084 | 22.3% | torch-compile |
| 🔴 | **L1NormFwdOp** | test_l1_norm_bench[hidden-state-l1-bfloat16-float32] | 0.0372 | 0.0084 | 22.5% | torch-compile |
| 🔴 | **L2NormFwdOp** | test_l2_norm_bench[hidden-state-l2-bfloat16-float32] | 0.0373 | 0.0087 | 23.4% | torch-compile |
| 🔴 | **RMSNormFwdOp** | test_rms_norm_bench[qk-norm-head-bfloat16] | 0.0115 | 0.0028 | 24.5% | torch-compile |
| 🔴 | **InfNormFwdOp** | test_inf_norm_bench[hidden-state-inf-bfloat16-float32] | 0.0372 | 0.0110 | 29.6% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-bfloat16] | 0.4533 | 0.1419 | 31.3% | fa3 |

<details>
<summary><strong>46 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-bfloat16] | 0.4561 | 0.1430 | 31.4% | fa3 |
| 🔴 | **InstanceNormFwdOp** | test_instance_norm_bench[image-running-stats-float16] | 0.0114 | 0.0043 | 37.7% | torch-compile |
| 🔴 | **CountNonzeroFwdOp** | test_count_nonzero_bench[3d-multidim-reduce-complex64] | 0.0293 | 0.0111 | 38.0% | torch-compile |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-short-bfloat16] | 0.4080 | 0.1597 | 39.1% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-short-bfloat16] | 0.4144 | 0.1657 | 40.0% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-bfloat16] | 1.3096 | 0.5481 | 41.9% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-q-lt-kv-float16] | 0.1224 | 0.0535 | 43.7% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-q-lt-kv-bfloat16] | 0.1211 | 0.0536 | 44.2% | fa3 |
| 🔴 | **AnyFwdOp** | test_any_bench[3d-multidim-reduce-complex64] | 0.0295 | 0.0133 | 45.0% | torch-compile |
| 🔴 | **AnyFwdOp** | test_any_bench[3d-multidim-reduce-complex128] | 0.0381 | 0.0173 | 45.4% | torch-compile |
| 🔴 | **AnyFwdOp** | test_any_bench[mask-validation-32k-int32] | 0.0097 | 0.0045 | 46.4% | torch-compile |
| 🔴 | **AllFwdOp** | test_all_bench[3d-multidim-reduce-complex128] | 0.0380 | 0.0180 | 47.3% | torch-compile |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-bfloat16] | 1.2417 | 0.5894 | 47.5% | fa3 |
| 🔴 | **AllFwdOp** | test_all_bench[3d-multidim-reduce-complex64] | 0.0294 | 0.0140 | 47.5% | torch-compile |
| 🔴 | **AllFwdOp** | test_all_bench[mask-validation-32k-int32] | 0.0098 | 0.0046 | 47.5% | torch-compile |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-70b-q-lt-kv-bfloat16] | 0.2046 | 0.0983 | 48.0% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-70b-q-lt-kv-float16] | 0.2050 | 0.0997 | 48.6% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p256-float16] | 0.1651 | 0.0812 | 49.2% | fa3 |
| 🔴 | **CountNonzeroFwdOp** | test_count_nonzero_bench[sparsity-seq-int32] | 0.0096 | 0.0048 | 49.8% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-bfloat16] | 1.1032 | 0.5508 | 49.9% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-405b-p256-float16] | 0.0537 | 0.0269 | 50.1% | fa3 |
| 🔴 | **CountNonzeroFwdOp** | test_count_nonzero_bench[3d-multidim-reduce-complex128] | 0.0379 | 0.0210 | 55.4% | torch-compile |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-70b-p256-float16] | 0.0666 | 0.0370 | 55.5% | fa3 |
| 🔴 | **AnyFwdOp** | test_any_bench[mask-validation-32k-int64] | 0.0105 | 0.0059 | 55.9% | torch-compile |
| 🔴 | **BatchNormBwdOp** | test_batch_norm_bwd_bench[resnet50-stage3-float32] | 0.0177 | 0.0100 | 56.8% | torch-native-batch-norm |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 1.0168 | 0.5781 | 56.9% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-float16] | 0.2429 | 0.1425 | 58.7% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-float16] | 0.2443 | 0.1434 | 58.7% | fa3 |
| 🔴 | **FusedTopKFwdOp** | test_fused_topk_bench[kimi-k2-t512-bias-float32] | 0.0118 | 0.0072 | 61.1% | vllm |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-float16] | 0.9016 | 0.5515 | 61.2% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[throughput-8b-p64-float16] | 0.2473 | 0.1513 | 61.2% | flashinfer |
| 🔴 | **AllFwdOp** | test_all_bench[mask-validation-32k-int64] | 0.0106 | 0.0065 | 61.2% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-float16] | 0.8920 | 0.5534 | 62.0% | fa3 |
| 🔴 | **CountNonzeroFwdOp** | test_count_nonzero_bench[sparsity-seq-int64] | 0.0104 | 0.0065 | 62.6% | torch-compile |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-uniform-float16] | 0.0628 | 0.0447 | 71.2% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-float16] | 0.8312 | 0.5922 | 71.2% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-uniform-bfloat16] | 0.0626 | 0.0448 | 71.6% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.8071 | 0.5808 | 72.0% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-softcap50-float16] | 0.1732 | 0.1256 | 72.5% | flashinfer |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-float16] | 0.1648 | 0.1256 | 76.2% | flashinfer |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-float16] | 0.0988 | 0.0757 | 76.7% | fla |
| 🔴 | **CountNonzeroFwdOp** | test_count_nonzero_bench[sparsity-mlp-intermediate-float16] | 0.0221 | 0.0172 | 77.8% | torch-compile |
| 🔴 | **EngramGateConvBwdOp** | test_engram_gate_conv_bwd_bench[bwd-b3-s96-d768-bfloat16] | 0.1048 | 0.0818 | 78.1% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-bfloat16] | 0.0951 | 0.0743 | 78.1% | fla |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-float16] | 0.6171 | 0.4834 | 78.3% | fla |
| 🔴 | **ProdFwdOp** | test_prod_bench[mlp-intermediate-reduce-float32] | 0.0316 | 0.0249 | 78.8% | torch-compile |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 28 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 507 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 1847 lines in `ops/`, 37.2% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 4019 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

### Never-built kernels

| File | Executed |
| --- | --- |
| `kernels/linear_attention/gated_deltanet/compute_w_u_bwd.py` | 0.0% |
| `kernels/linear_attention/gated_deltanet/prefill/forward.py` | 3.4% |
| `kernels/linear_attention/gated_deltanet/prefill/prepare.py` | 3.7% |
| `kernels/attention/deepseek_mla_decode.py` | 5.3% |
| `kernels/attention/gqa_fwd_ws.py` | 6.4% |
| `kernels/linear_attention/gated_deltanet/gated_deltanet_bwd.py` | 7.2% |
| `kernels/attention/gqa_fwd_fp8.py` | 7.5% |
| `kernels/attention/gqa_prefill_varlen_ws.py` | 10.2% |
| `kernels/attention/gqa_fwd.py` | 10.2% |
| `kernels/linear_attention/gla/dense_prefill_partitioned.py` | 10.5% |
| `kernels/attention/gqa_dense.py` | 10.8% |
| `kernels/linear_attention/gla/dense_prefill_subchunk.py` | 11.1% |
| `kernels/linear_attention/gated_deltanet/fused_prepare_compute_w_u.py` | 11.4% |
| `kernels/attention/mha_decode.py` | 11.7% |
| `kernels/attention/gqa_decode_bs1_common.py` | 12.4% |
| `kernels/attention/mha_decode_paged.py` | 12.5% |
| `kernels/linear_attention/gated_deltanet_recurrence.py` | 14.1% |
| `kernels/attention/gqa_decode.py` | 14.3% |
| `kernels/attention/gqa_decode_bs1.py` | 14.3% |
| `kernels/moe/indexed_expert_gemm.py` | 15.4% |
| `kernels/attention/gqa_decode_fp8.py` | 15.9% |
| `kernels/grouped_gemm/grouped_gemm.py` | 17.7% |
| `kernels/linear_attention/gated_deltanet/decode.py` | 17.8% |
| `kernels/attention/deepseek_nsa_cmp_fwd.py` | 18.1% |
| `kernels/linear_attention/gated_deltanet/prefill/dense.py` | 20.0% |
| `kernels/linear_attention/gated_deltanet/gated_deltanet_fwd.py` | 21.7% |
| `kernels/linear_attention/deltanet/dense_prefill.py` | 22.4% |
| `kernels/linear_attention/gated_deltanet/prefill/common.py` | 23.0% |

<details>
<summary>Untested pure Python, worst 15 files</summary>

| File | Uncovered | Executed |
| --- | --- | --- |
| `ops/attention/gqa.py` | 555 | 32.2% |
| `perf/formulas.py` | 465 | 9.0% |
| `manifest/roofline_analysis.py` | 388 | 28.9% |
| `manifest/plan.py` | 349 | 30.3% |
| `ops/op_base.py` | 284 | 55.4% |
| `manifest/workload.py` | 174 | 60.8% |
| `manifest/expr.py` | 131 | 68.5% |
| `ops/linear_attention/gated_deltanet.py` | 123 | 15.8% |
| `manifest/signature.py` | 106 | 77.1% |
| `ops/linear_attention/deltanet_inference.py` | 84 | 20.0% |
| `manifest/primitives.py` | 83 | 63.3% |
| `manifest/rule_eval.py` | 82 | 15.5% |
| `ops/_signature_codegen.py` | 79 | 89.6% |
| `ops/linear_attention/gla_inference.py` | 78 | 22.8% |
| `trace/ui.py` | 62 | 24.4% |

</details>

Per-line detail is in the `htmlcov/` directory of this run's `tileops_op_test` artifact.
