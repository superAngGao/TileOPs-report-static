# ❌ TileOPs Nightly Report

> **2026-10-02 19:23** &ensp;|&ensp; `0b1d6247` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Correctness** | ✅ &ensp; (516/516 tests across 82 ops) |
| **Benchmarked Ops** | 188 |
| **Benchmark Failures** | ✅ None |
| **Regressions** (vs 14-day median) | ⚠️ 15 |
| **Baseline Alerts** (< 80%) | ⚠️ 25 |
| **History window** | 14 runs, 2026-09-18 to 2026-10-01 |
| **Roofline anomalies** | ✅ None |
| **Improvements** (vs 14-day best) | 🎉 14 |
| **Moved since previous run** | 🔵 27 |
| **Never-built kernels** | ⚠️ 30 files **+3** &ensp;·&ensp; `kernels/linear_attention/gated_deltanet/prefill_forward.py` at 3.0% |
| **Untested roofline math** | 422 lines in `perf/` **+8** &ensp;·&ensp; `perf/formulas.py` at 17.4% |
| **Untested op logic** | 893 lines in `ops/` **−14** &ensp;·&ensp; 60.1% of branches taken **+0.6pp** |
| | <sub>coverage compared against the 2026-10-01 run; no figure means it held</sub> |

## ⚠️ Performance Regressions (vs 14-day median)

| Op | Config | Median (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[prefill-narrow-state-bfloat16] | 0.0527 | 0.0739 | +40.3% | 25.43 |
| **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[prefill-v-first-4k-bfloat16] | 0.0799 | 0.1029 | +28.8% | 73.04 |
| **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[prefill-4k-bfloat16] | 0.0794 | 0.1012 | +27.5% | 74.28 |
| **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[prefill-continued-bfloat16] | 0.0799 | 0.1015 | +27.0% | 74.07 |
| **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[prefill-4k-float16] | 0.0797 | 0.1004 | +26.0% | 74.83 |
| **GLABwdOp** | test_gla_bwd_bench[train-4k-float16] | 0.3693 | 0.4197 | +13.6% | 4.31 |
| **GLABwdOp** | test_gla_bwd_bench[train-8k-bfloat16] | 0.7246 | 0.8229 | +13.6% | 4.40 |
| **GLABwdOp** | test_gla_bwd_bench[train-4k-bfloat16] | 0.3659 | 0.4137 | +13.1% | 4.37 |
| **GLABwdOp** | test_gla_bwd_bench[train-8k-float16] | 0.7469 | 0.8441 | +13.0% | 4.29 |
| **GLABwdOp** | test_gla_bwd_bench[train-16k-float16] | 1.5193 | 1.7149 | +12.9% | 4.22 |
| **GLABwdOp** | test_gla_bwd_bench[train-2k-bfloat16] | 0.1841 | 0.2076 | +12.7% | 4.36 |
| **GLABwdOp** | test_gla_bwd_bench[train-2k-float16] | 0.1827 | 0.2059 | +12.7% | 4.40 |
| **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[prefill-12k-bfloat16] | 0.2056 | 0.2316 | +12.6% | 97.37 |
| **GLABwdOp** | test_gla_bwd_bench[train-16k-bfloat16] | 1.4610 | 1.6436 | +12.5% | 4.40 |
| **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[prefill-12k-float16] | 0.2051 | 0.2297 | +12.0% | 98.18 |

## 🎉 Performance Improvements (vs 14-day best)

| Op | Config | Prev Best (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **GLAInferenceFwdOp** | test_gla_inference_bench[decode-first-token-float16] | 0.0094 | 0.0028 | -70.8% | 2.15 |
| **GLAInferenceFwdOp** | test_gla_inference_bench[decode-b1-d64-bfloat16] | 0.0048 | 0.0021 | -55.0% | 0.31 |
| **GLAInferenceFwdOp** | test_gla_inference_bench[prefill-3000-bfloat16] | 0.0707 | 0.0553 | -21.7% | 8.94 |
| **SoftmaxFwdOp** | test_softmax_bench[attn-weights-4k-float16] | 0.0084 | 0.0070 | -17.1% | 3.01 |
| **GLAInferenceFwdOp** | test_gla_inference_bench[decode-b8-d128-bfloat16] | 0.0141 | 0.0119 | -16.1% | 1.77 |
| **SoftmaxFwdOp** | test_softmax_bench[attn-weights-4k-bfloat16] | 0.0083 | 0.0072 | -13.5% | 2.91 |
| **LogSumExpFwdOp** | test_logsumexp_bench[attn-weights-4k-float16] | 0.0073 | 0.0064 | -13.1% | 2.63 |
| **CountNonzeroFwdOp** | test_count_nonzero_bench[sparsity-hidden-float32] | 0.0124 | 0.0109 | -12.6% | 1.54 |
| **LogSoftmaxFwdOp** | test_log_softmax_bench[attn-weights-4k-float16] | 0.0084 | 0.0074 | -11.8% | 2.82 |
| **CountNonzeroFwdOp** | test_count_nonzero_bench[3d-multidim-complex128] | 0.0126 | 0.0112 | -11.2% | 0.38 |
| **AllFwdOp** | test_all_bench[3d-multidim-complex128] | 0.0126 | 0.0112 | -10.7% | 0.37 |
| **LogSoftmaxFwdOp** | test_log_softmax_bench[attn-weights-4k-bfloat16] | 0.0087 | 0.0078 | -10.7% | 2.70 |
| **GLAInferenceFwdOp** | test_gla_inference_bench[varlen-ragged-float16] | 0.2763 | 0.2476 | -10.4% | 21.75 |
| **LogSumExpFwdOp** | test_logsumexp_bench[attn-weights-4k-bfloat16] | 0.0074 | 0.0067 | -10.3% | 2.52 |

## 🔵 Moved Since Previous Run

> Moves against the most recent reading. A row restored to its old level appears only here: returning is not a new 14-day record.

| Op | Config | Previous (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **GLAInferenceFwdOp** | test_gla_inference_bench[decode-first-token-float16] | 0.0094 | 0.0028 | -70.8% | 2.15 |
| **GLAInferenceFwdOp** | test_gla_inference_bench[decode-b1-d64-bfloat16] | 0.0048 | 0.0021 | -55.6% | 0.31 |
| **GLAInferenceFwdOp** | test_gla_inference_bench[prefill-3000-bfloat16] | 0.0707 | 0.0553 | -21.7% | 8.94 |
| **SoftmaxFwdOp** | test_softmax_bench[attn-weights-4k-float16] | 0.0085 | 0.0070 | -17.7% | 3.01 |
| **GLAInferenceFwdOp** | test_gla_inference_bench[decode-b8-d128-bfloat16] | 0.0141 | 0.0119 | -16.1% | 1.77 |
| **SoftmaxFwdOp** | test_softmax_bench[attn-weights-4k-bfloat16] | 0.0083 | 0.0072 | -13.5% | 2.91 |
| **LogSumExpFwdOp** | test_logsumexp_bench[attn-weights-4k-float16] | 0.0073 | 0.0064 | -13.1% | 2.63 |
| **LogSoftmaxFwdOp** | test_log_softmax_bench[attn-weights-4k-float16] | 0.0084 | 0.0074 | -11.8% | 2.82 |
| **CountNonzeroFwdOp** | test_count_nonzero_bench[3d-multidim-complex128] | 0.0126 | 0.0112 | -11.2% | 0.38 |
| **LogSoftmaxFwdOp** | test_log_softmax_bench[attn-weights-4k-bfloat16] | 0.0087 | 0.0078 | -10.7% | 2.70 |
| **GLAInferenceFwdOp** | test_gla_inference_bench[varlen-ragged-float16] | 0.2763 | 0.2476 | -10.4% | 21.75 |
| **LogSumExpFwdOp** | test_logsumexp_bench[attn-weights-4k-bfloat16] | 0.0074 | 0.0067 | -10.3% | 2.52 |
| **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[prefill-12k-float16] | 0.2054 | 0.2297 | +11.8% | 98.18 |
| **GLABwdOp** | test_gla_bwd_bench[train-16k-bfloat16] | 1.4614 | 1.6436 | +12.5% | 4.40 |
| **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[prefill-12k-bfloat16] | 0.2057 | 0.2316 | +12.6% | 97.37 |
| **GLABwdOp** | test_gla_bwd_bench[train-2k-float16] | 0.1827 | 0.2059 | +12.7% | 4.40 |
| **GLABwdOp** | test_gla_bwd_bench[train-2k-bfloat16] | 0.1841 | 0.2076 | +12.7% | 4.36 |
| **GLABwdOp** | test_gla_bwd_bench[train-16k-float16] | 1.5193 | 1.7149 | +12.9% | 4.22 |
| **GLABwdOp** | test_gla_bwd_bench[train-8k-float16] | 0.7469 | 0.8441 | +13.0% | 4.29 |
| **GLABwdOp** | test_gla_bwd_bench[train-4k-bfloat16] | 0.3657 | 0.4137 | +13.1% | 4.37 |
| **GLABwdOp** | test_gla_bwd_bench[train-4k-float16] | 0.3700 | 0.4197 | +13.4% | 4.31 |
| **GLABwdOp** | test_gla_bwd_bench[train-8k-bfloat16] | 0.7247 | 0.8229 | +13.6% | 4.40 |
| **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[prefill-4k-float16] | 0.0799 | 0.1004 | +25.7% | 74.83 |
| **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[prefill-4k-bfloat16] | 0.0797 | 0.1012 | +26.9% | 74.28 |
| **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[prefill-continued-bfloat16] | 0.0799 | 0.1015 | +27.0% | 74.07 |
| **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[prefill-v-first-4k-bfloat16] | 0.0799 | 0.1029 | +28.8% | 73.04 |
| **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[prefill-narrow-state-bfloat16] | 0.0527 | 0.0739 | +40.3% | 25.43 |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 80%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **NSACmpVarlenFwdOp** | test_nsa_cmp_fwd_varlen_bench[prefill-4x1k-float16] | 0.1440 | 0.0515 | 35.8% | fla |
| 🔴 | **NSACmpVarlenFwdOp** | test_nsa_cmp_fwd_varlen_bench[prefill-8x1k-float16] | 0.2664 | 0.0982 | 36.9% | fla |
| 🔴 | **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-b64-p16-float16-float16] | 0.4006 | 0.2213 | 55.2% | flashinfer |
| 🔴 | **FusedTopKFwdOp** | test_fused_topk_bench[kimi-k2-t512-bias-float32] | 0.0117 | 0.0072 | 61.0% | vllm |
| 🔴 | **MultiHeadLatentAttentionDecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-32k-bfloat16] | 0.3925 | 0.2423 | 61.7% | torch-compile |
| 🔴 | **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-p16-float16-float16] | 0.3381 | 0.2186 | 64.6% | flashinfer |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-qkv-a-2d-float8_e4m3fn-bfloat16] | 0.1526 | 0.1099 | 72.0% | deepgemm |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-down-2d-float8_e4m3fn-bfloat16] | 0.1445 | 0.1061 | 73.4% | deepgemm |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-q-b-2d-float8_e4m3fn-bfloat16] | 0.3576 | 0.2625 | 73.4% | deepgemm |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-m1-down-2d-float8_e4m3fn-bfloat16] | 0.0105 | 0.0077 | 73.5% | flashinfer-fp8-blockscale-sm90 |

<details>
<summary><strong>15 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[train-16k-float16] | 1.7149 | 1.2892 | 75.2% | fla |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[train-8k-float16] | 0.8441 | 0.6583 | 78.0% | fla |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[train-16k-float16] | 0.6180 | 0.4836 | 78.2% | fla |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-mlp-up-2d-float8_e4m3fn-bfloat16] | 0.2421 | 0.1898 | 78.4% | deepgemm |
| 🔴 | **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-405b-p256-float16-float16] | 0.0396 | 0.0310 | 78.4% | fa3 |
| 🔴 | **DeltaNetBwdOp** | test_deltanet_vs_fla_bwd[train-4k-float16] | 0.2739 | 0.2148 | 78.4% | fla |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[train-16k-bfloat16] | 1.6436 | 1.2899 | 78.5% | fla |
| 🔴 | **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-p256-float16-float16] | 0.1811 | 0.1427 | 78.8% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 0.5635 | 0.4453 | 79.0% | fa3 |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[train-2k-float16] | 0.0983 | 0.0779 | 79.2% | fla |
| 🔴 | **DeltaNetBwdOp** | test_deltanet_vs_fla_bwd[train-4k-bfloat16] | 0.2733 | 0.2165 | 79.2% | fla |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-o-proj-2d-float8_e4m3fn-bfloat16] | 0.8692 | 0.6899 | 79.4% | deepgemm |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.5622 | 0.4464 | 79.4% | fa3 |
| 🔴 | **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-70b-p256-float16-float16] | 0.0576 | 0.0461 | 80.0% | fa3 |
| 🔴 | **GLABwdOp** | test_gla_bwd_bench[train-8k-bfloat16] | 0.8229 | 0.6582 | 80.0% | fla |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 30 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 422 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 893 lines in `ops/`, 60.1% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 2567 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

### Never-built kernels

| File | Executed |
| --- | --- |
| `kernels/linear_attention/gated_deltanet/prefill_forward.py` | 3.0% |
| `kernels/linear_attention/gated_deltanet/prefill_prepare.py` | 3.2% |
| `kernels/attention/deepseek_mla_decode.py` | 6.2% |
| `kernels/sampling/top_k_top_p_mask.py` | 6.3% |
| `kernels/attention/gqa_fwd_fp8.py` | 7.1% |
| `kernels/attention/gqa_fwd.py` | 7.7% |
| `kernels/linear_attention/delta_decode.py` | 7.8% |
| `kernels/sampling/top_k_mask.py` | 10.5% |
| `kernels/attention/gqa_dense.py` | 10.9% |
| `kernels/sampling/chain_speculative_sampling.py` | 11.4% |
| `kernels/sampling/sampling_from_probs.py` | 11.8% |
| `kernels/linear_attention/gla/varlen_prefill.py` | 11.8% |
| `kernels/sampling/top_p_mask.py` | 12.4% |
| `kernels/quantization/int8_quant_per_tensor.py` | 12.8% |
| `kernels/attention/gqa_decode_bs1.py` | 13.8% |
| `kernels/attention/gqa_decode.py` | 14.8% |
| `kernels/linear_attention/gla/varlen_prefill_partitioned.py` | 14.9% |
| `kernels/linear_attention/gla/dense_prefill_partitioned.py` | 15.0% |
| `kernels/linear_attention/gla/dense_prefill_subchunk.py` | 15.6% |
| `kernels/quantization/int8_quant_per_block.py` | 16.1% |
| `kernels/attention/gqa_decode_fp8.py` | 16.1% |
| `kernels/quantization/int8_quant_per_channel.py` | 16.2% |
| `kernels/moe/indexed_expert_gemm.py` | 17.0% |
| `kernels/grouped_gemm/grouped_gemm.py` | 17.2% |
| `kernels/attention/varlen_rope.py` | 17.3% |
| `kernels/sampling/min_p_mask.py` | 19.6% |
| `kernels/attention/deepseek_nsa_cmp_fwd.py` | 20.0% |
| `kernels/linear_attention/gla/dense_decode.py` | 22.2% |
| `kernels/quantization/fp8_quant_per_block.py` | 22.6% |
| `kernels/sampling/radix_select.py` | 23.6% |

<details>
<summary>Untested pure Python, worst 15 files</summary>

| File | Uncovered | Executed |
| --- | --- | --- |
| `perf/formulas.py` | 380 | 17.4% |
| `manifest/plan.py` | 356 | 30.1% |
| `manifest/workload.py` | 194 | 58.5% |
| `ops/op_base.py` | 156 | 70.7% |
| `manifest/primitives.py` | 146 | 54.8% |
| `manifest/expr.py` | 122 | 70.7% |
| `manifest/signature.py` | 109 | 76.3% |
| `ops/attention/gqa.py` | 103 | 56.7% |
| `ops/_signature_codegen.py` | 88 | 89.2% |
| `trace/ui.py` | 62 | 24.4% |
| `manifest/kinds.py` | 53 | 79.2% |
| `backend/registry.py` | 48 | 50.0% |
| `perf/profile.py` | 42 | 22.2% |
| `ops/rope.py` | 28 | 84.1% |
| `ops/reduction/reduce.py` | 27 | 80.1% |

</details>

Per-line detail is in the `htmlcov/` directory of this run's `tileops_op_test` artifact.
