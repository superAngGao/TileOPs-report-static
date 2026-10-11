# ❌ TileOPs Nightly Report

> **2026-09-27 18:59** &ensp;|&ensp; `ee3ebaf2` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Correctness** | ✅ &ensp; (511/511 tests across 84 ops) |
| **Benchmarked Ops** | 177 |
| **Benchmark Failures** | ✅ None &ensp;|&ensp; ⚠️ 1 skipped |
| **Regressions** (vs 14-day median) | ⚠️ 2 |
| **Baseline Alerts** (< 80%) | ⚠️ 44 |
| **History window** | 14 runs, 2026-09-13 to 2026-09-27 |
| **Roofline anomalies** | ✅ None |
| **Improvements** (vs 14-day best) | 🎉 2 |
| **Moved since previous run** | 🔵 4 |
| **Never-built kernels** | ⚠️ 20 files **−8** &ensp;·&ensp; `kernels/linear_attention/gated_deltanet/prefill/forward.py` at 3.4% |
| **Untested roofline math** | 326 lines in `perf/` **+1** &ensp;·&ensp; `perf/formulas.py` at 18.4% |
| **Untested op logic** | 879 lines in `ops/` **−86** &ensp;·&ensp; 54.6% of branches taken **+1.3pp** |
| | <sub>coverage compared against the 2026-09-27 run; no figure means it held</sub> |

## ⚠️ Performance Regressions (vs 14-day median)

| Op | Config | Median (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **MultiHeadAttentionDecodePagedWithKVCacheFwdOp** | test_mha_decode_paged_bench[serving-b2-float16] | 0.0059 | 0.0071 | +20.3% | 0.60 |
| **MultiHeadAttentionDecodePagedWithKVCacheFwdOp** | test_mha_decode_paged_bench[serving-p128-float16] | 0.0060 | 0.0069 | +14.1% | 0.62 |

## 🎉 Performance Improvements (vs 14-day best)

| Op | Config | Prev Best (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **NSAVarlenFwdOp** | test_nsa_fwd_varlen_bench[prefill-2x4k-float16] | 0.0807 | 0.0492 | -39.1% | 54.82 |
| **NSAVarlenFwdOp** | test_nsa_fwd_varlen_bench[prefill-4x2k-float16] | 0.0505 | 0.0323 | -36.1% | 33.03 |

## 🔵 Moved Since Previous Run

> Moves against the most recent reading. A row restored to its old level appears only here: returning is not a new 14-day record.

| Op | Config | Previous (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **NSAVarlenFwdOp** | test_nsa_fwd_varlen_bench[prefill-2x4k-float16] | 0.0807 | 0.0492 | -39.1% | 54.82 |
| **NSAVarlenFwdOp** | test_nsa_fwd_varlen_bench[prefill-4x2k-float16] | 0.0505 | 0.0323 | -36.1% | 33.03 |
| **MultiHeadAttentionDecodePagedWithKVCacheFwdOp** | test_mha_decode_paged_bench[serving-p128-float16] | 0.0060 | 0.0069 | +14.1% | 0.62 |
| **MultiHeadAttentionDecodePagedWithKVCacheFwdOp** | test_mha_decode_paged_bench[serving-b2-float16] | 0.0059 | 0.0071 | +20.3% | 0.60 |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 80%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **ProdFwdOp** | test_prod_bench[3d-non-last-axis-float16] | 0.6009 | 0.0035 | 0.6% | torch-compile |
| 🔴 | **InstanceNormFwdOp** | test_instance_norm_bench[image-track-stats-float16] | 0.0326 | 0.0029 | 9.0% | torch-compile |
| 🔴 | **InstanceNormFwdOp** | test_instance_norm_bench[image-eval-float16] | 0.0114 | 0.0029 | 25.3% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-bfloat16] | 0.4539 | 0.1420 | 31.3% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-bfloat16] | 0.4560 | 0.1429 | 31.3% | fa3 |
| 🔴 | **RMSNormFwdOp** | test_rms_norm_bench[qk-norm-head-bfloat16] | 0.0115 | 0.0037 | 32.3% | torch-compile |
| 🔴 | **CountNonzeroFwdOp** | test_count_nonzero_bench[3d-multidim-complex64] | 0.0293 | 0.0112 | 38.1% | torch-compile |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-short-bfloat16] | 0.4083 | 0.1591 | 39.0% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-short-bfloat16] | 0.4147 | 0.1657 | 40.0% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-bfloat16] | 1.3098 | 0.5492 | 41.9% | fa3 |

<details>
<summary><strong>34 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **AnyFwdOp** | test_any_bench[3d-multidim-complex64] | 0.0295 | 0.0133 | 45.0% | torch-compile |
| 🔴 | **AnyFwdOp** | test_any_bench[3d-multidim-complex128] | 0.0380 | 0.0172 | 45.3% | torch-compile |
| 🔴 | **AllFwdOp** | test_all_bench[3d-multidim-complex128] | 0.0380 | 0.0180 | 47.2% | torch-compile |
| 🔴 | **AnyFwdOp** | test_any_bench[mask-validation-32k-int32] | 0.0097 | 0.0046 | 47.4% | torch-compile |
| 🔴 | **AllFwdOp** | test_all_bench[mask-validation-32k-int32] | 0.0097 | 0.0046 | 47.4% | torch-compile |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-bfloat16] | 1.2420 | 0.5895 | 47.5% | fa3 |
| 🔴 | **AllFwdOp** | test_all_bench[3d-multidim-complex64] | 0.0295 | 0.0140 | 47.6% | torch-compile |
| 🔴 | **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-b64-p16-float16-float16] | 0.4601 | 0.2215 | 48.1% | flashinfer |
| 🔴 | **CountNonzeroFwdOp** | test_count_nonzero_bench[sparsity-seq-int32] | 0.0097 | 0.0048 | 49.3% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-bfloat16] | 1.1028 | 0.5510 | 50.0% | fa3 |
| 🔴 | **CountNonzeroFwdOp** | test_count_nonzero_bench[3d-multidim-complex128] | 0.0378 | 0.0211 | 55.6% | torch-compile |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 1.0174 | 0.5781 | 56.8% | fa3 |
| 🔴 | **BatchNormBwdOp** | test_batch_norm_bwd_bench[resnet-stage3-float32] | 0.0177 | 0.0101 | 57.0% | torch-native-batch-norm |
| 🔴 | **AnyFwdOp** | test_any_bench[mask-validation-32k-int64] | 0.0105 | 0.0060 | 57.0% | torch-compile |
| 🔴 | **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-p16-float16-float16] | 0.3803 | 0.2187 | 57.5% | flashinfer |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-float16] | 0.2444 | 0.1429 | 58.5% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-float16] | 0.2432 | 0.1424 | 58.6% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-float16] | 0.9016 | 0.5521 | 61.2% | fa3 |
| 🔴 | **FusedTopKFwdOp** | test_fused_topk_bench[kimi-k2-t512-bias-float32] | 0.0117 | 0.0072 | 61.3% | vllm |
| 🔴 | **AllFwdOp** | test_all_bench[mask-validation-32k-int64] | 0.0105 | 0.0065 | 61.6% | torch-compile |
| 🔴 | **MultiHeadAttentionDecodePagedWithKVCacheFwdOp** | test_mha_decode_paged_bench[speculative-decode-float16] | 0.0302 | 0.0187 | 61.8% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-float16] | 0.8936 | 0.5528 | 61.9% | fa3 |
| 🔴 | **CountNonzeroFwdOp** | test_count_nonzero_bench[sparsity-seq-int64] | 0.0104 | 0.0065 | 62.3% | torch-compile |
| 🔴 | **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-p256-float16-float16] | 0.2055 | 0.1432 | 69.7% | fa3 |
| 🔴 | **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-b64-p64-float16-float16] | 0.3094 | 0.2207 | 71.3% | flashinfer |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-float16] | 0.8329 | 0.5947 | 71.4% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.8093 | 0.5818 | 71.9% | fa3 |
| 🔴 | **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-70b-p256-float16-float16] | 0.0599 | 0.0461 | 77.0% | fa3 |
| 🔴 | **CountNonzeroFwdOp** | test_count_nonzero_bench[sparsity-mlp-float16] | 0.0220 | 0.0172 | 78.1% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[train-16k-float16] | 0.6180 | 0.4831 | 78.2% | fla |
| 🔴 | **ProdFwdOp** | test_prod_bench[mlp-intermediate-float32] | 0.0316 | 0.0249 | 78.6% | torch-compile |
| 🔴 | **EngramGateConvBwdOp** | test_engram_gate_conv_bwd_bench[train-s96-bfloat16] | 0.1048 | 0.0825 | 78.7% | torch-compile |
| 🔴 | **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-405b-p256-float16-float16] | 0.0393 | 0.0310 | 79.1% | fa3 |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[train-2k-float16] | 0.0985 | 0.0779 | 79.1% | fla |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 20 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 326 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 879 lines in `ops/`, 54.6% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 2437 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

### Never-built kernels

| File | Executed |
| --- | --- |
| `kernels/linear_attention/gated_deltanet/prefill/forward.py` | 3.4% |
| `kernels/linear_attention/gated_deltanet/prefill/prepare.py` | 3.7% |
| `kernels/attention/deepseek_mla_decode.py` | 5.3% |
| `kernels/attention/gqa_fwd_fp8.py` | 7.5% |
| `kernels/attention/gqa_fwd.py` | 9.3% |
| `kernels/linear_attention/gla/dense_prefill_partitioned.py` | 10.5% |
| `kernels/attention/gqa_dense.py` | 10.8% |
| `kernels/linear_attention/gla/dense_prefill_subchunk.py` | 11.1% |
| `kernels/attention/mha_decode_paged.py` | 13.2% |
| `kernels/attention/gqa_decode.py` | 14.3% |
| `kernels/attention/gqa_decode_bs1.py` | 14.3% |
| `kernels/moe/indexed_expert_gemm.py` | 15.4% |
| `kernels/attention/gqa_decode_fp8.py` | 15.9% |
| `kernels/grouped_gemm/grouped_gemm.py` | 17.7% |
| `kernels/linear_attention/gated_deltanet/decode.py` | 17.8% |
| `kernels/attention/deepseek_nsa_cmp_fwd.py` | 18.1% |
| `kernels/linear_attention/gated_deltanet/prefill/dense.py` | 20.0% |
| `kernels/attention/gqa_prefill_varlen_fwd.py` | 21.4% |
| `kernels/linear_attention/deltanet/dense_prefill.py` | 22.4% |
| `kernels/linear_attention/gated_deltanet/prefill/common.py` | 23.0% |

<details>
<summary>Untested pure Python, worst 15 files</summary>

| File | Uncovered | Executed |
| --- | --- | --- |
| `manifest/plan.py` | 349 | 30.3% |
| `perf/formulas.py` | 284 | 18.4% |
| `manifest/workload.py` | 194 | 58.5% |
| `ops/op_base.py` | 157 | 65.7% |
| `manifest/primitives.py` | 144 | 54.9% |
| `manifest/expr.py` | 122 | 70.7% |
| `ops/attention/gqa.py` | 121 | 55.2% |
| `manifest/signature.py` | 105 | 77.2% |
| `ops/_signature_codegen.py` | 75 | 90.3% |
| `trace/ui.py` | 62 | 24.4% |
| `manifest/kinds.py` | 53 | 79.2% |
| `ops/linear_attention/gated_deltanet.py` | 50 | 26.5% |
| `perf/profile.py` | 42 | 22.2% |
| `backend/registry.py` | 40 | 52.9% |
| `ops/moe/routed_expert/indexed_routed_expert.py` | 38 | 45.7% |

</details>

Per-line detail is in the `htmlcov/` directory of this run's `tileops_op_test` artifact.
