# ✅ TileOPs Nightly Report

> **2026-10-01 19:21** &ensp;|&ensp; `fd22cb26` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Correctness** | ✅ &ensp; (514/514 tests across 85 ops) |
| **Benchmarked Ops** | 192 |
| **Benchmark Failures** | ✅ None |
| **Regressions** (vs 14-day median) | ✅ None |
| **Baseline Alerts** (< 80%) | ⚠️ 18 |
| **History window** | 14 runs, 2026-09-17 to 2026-09-30 |
| **Roofline anomalies** | ✅ None |
| **Improvements** (vs 14-day best) | 🎉 4 |
| **Moved since previous run** | 🔵 6 |
| **Never-built kernels** | ⚠️ 27 files **+4** &ensp;·&ensp; `kernels/linear_attention/gated_deltanet/prefill_forward.py` at 3.5% |
| **Untested roofline math** | 414 lines in `perf/` &ensp;·&ensp; `perf/formulas.py` at 17.3% |
| **Untested op logic** | 907 lines in `ops/` **−46** &ensp;·&ensp; 59.4% of branches taken **+0.3pp** |
| | <sub>coverage compared against the 2026-09-30 run; no figure means it held</sub> |

## 🎉 Performance Improvements (vs 14-day best)

| Op | Config | Prev Best (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **GLAInferenceFwdOp** | test_gla_inference_bench[prefill-16k-bfloat16] | 0.3480 | 0.2638 | -24.2% | 10.24 |
| **GLAInferenceFwdOp** | test_gla_inference_bench[prefill-2k-bfloat16] | 0.0805 | 0.0612 | -23.9% | 5.51 |
| **GLAInferenceFwdOp** | test_gla_inference_bench[prefill-4k-bfloat16] | 0.1307 | 0.1014 | -22.4% | 6.66 |
| **GLAInferenceFwdOp** | test_gla_inference_bench[prefill-8k-bfloat16] | 0.2476 | 0.2010 | -18.8% | 6.72 |

## 🔵 Moved Since Previous Run

> Moves against the most recent reading. A row restored to its old level appears only here: returning is not a new 14-day record.

| Op | Config | Previous (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **GLAInferenceFwdOp** | test_gla_inference_bench[prefill-16k-bfloat16] | 0.3484 | 0.2638 | -24.3% | 10.24 |
| **GLAInferenceFwdOp** | test_gla_inference_bench[prefill-2k-bfloat16] | 0.0806 | 0.0612 | -24.0% | 5.51 |
| **GLAInferenceFwdOp** | test_gla_inference_bench[prefill-4k-bfloat16] | 0.1307 | 0.1014 | -22.4% | 6.66 |
| **GLAInferenceFwdOp** | test_gla_inference_bench[prefill-8k-bfloat16] | 0.2476 | 0.2010 | -18.8% | 6.72 |
| **RemainderFwdOp** | test_remainder_bench[linear-bias-bfloat16] | 0.0074 | 0.0064 | -14.2% | 2.63 |
| **RemainderFwdOp** | test_remainder_bench[linear-bias-float16] | 0.0072 | 0.0063 | -12.9% | 2.67 |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 80%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-b64-p16-float16-float16] | 0.4006 | 0.2210 | 55.2% | flashinfer |
| 🔴 | **MultiHeadLatentAttentionDecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-32k-bfloat16] | 0.3932 | 0.2391 | 60.8% | torch-compile |
| 🔴 | **FusedTopKFwdOp** | test_fused_topk_bench[kimi-k2-t512-bias-float32] | 0.0117 | 0.0072 | 61.0% | vllm |
| 🔴 | **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-p16-float16-float16] | 0.3382 | 0.2186 | 64.6% | flashinfer |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-qkv-a-2d-float8_e4m3fn-bfloat16] | 0.1525 | 0.1090 | 71.5% | deepgemm |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-q-b-2d-float8_e4m3fn-bfloat16] | 0.3581 | 0.2597 | 72.5% | deepgemm |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-down-2d-float8_e4m3fn-bfloat16] | 0.1450 | 0.1066 | 73.5% | deepgemm |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-m1-down-2d-float8_e4m3fn-bfloat16] | 0.0105 | 0.0077 | 73.7% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-mlp-up-2d-float8_e4m3fn-bfloat16] | 0.2427 | 0.1887 | 77.8% | deepgemm |
| 🔴 | **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-405b-p256-float16-float16] | 0.0400 | 0.0312 | 77.9% | fa3 |

<details>
<summary><strong>8 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-p256-float16-float16] | 0.1825 | 0.1426 | 78.1% | fa3 |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[train-16k-float16] | 0.6177 | 0.4835 | 78.3% | fla |
| 🔴 | **DeltaNetBwdOp** | test_deltanet_vs_fla_bwd[train-4k-float16] | 0.2740 | 0.2145 | 78.3% | fla |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-o-proj-2d-float8_e4m3fn-bfloat16] | 0.8708 | 0.6852 | 78.7% | deepgemm |
| 🔴 | **DeltaNetBwdOp** | test_deltanet_vs_fla_bwd[train-4k-bfloat16] | 0.2739 | 0.2163 | 79.0% | fla |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[train-2k-float16] | 0.0985 | 0.0779 | 79.0% | fla |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 0.5630 | 0.4451 | 79.1% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.5619 | 0.4459 | 79.4% | fa3 |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 27 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 414 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 907 lines in `ops/`, 59.4% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 2565 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

### Never-built kernels

| File | Executed |
| --- | --- |
| `kernels/linear_attention/gated_deltanet/prefill_forward.py` | 3.5% |
| `kernels/linear_attention/gated_deltanet/prefill_prepare.py` | 3.7% |
| `kernels/attention/deepseek_mla_decode.py` | 6.2% |
| `kernels/sampling/top_k_top_p_mask.py` | 6.3% |
| `kernels/attention/gqa_fwd_fp8.py` | 7.1% |
| `kernels/attention/gqa_fwd.py` | 7.7% |
| `kernels/sampling/top_k_mask.py` | 10.5% |
| `kernels/attention/gqa_dense.py` | 10.9% |
| `kernels/sampling/chain_speculative_sampling.py` | 11.4% |
| `kernels/sampling/sampling_from_probs.py` | 11.8% |
| `kernels/linear_attention/gla/varlen_prefill.py` | 11.8% |
| `kernels/sampling/top_p_mask.py` | 12.4% |
| `kernels/quantization/int8_quant_per_tensor.py` | 12.8% |
| `kernels/attention/gqa_decode_bs1.py` | 13.8% |
| `kernels/attention/gqa_decode.py` | 14.8% |
| `kernels/linear_attention/gla/dense_prefill_partitioned.py` | 15.0% |
| `kernels/linear_attention/gla/dense_prefill_subchunk.py` | 15.6% |
| `kernels/quantization/int8_quant_per_block.py` | 16.1% |
| `kernels/attention/gqa_decode_fp8.py` | 16.1% |
| `kernels/quantization/int8_quant_per_channel.py` | 16.2% |
| `kernels/moe/indexed_expert_gemm.py` | 17.1% |
| `kernels/grouped_gemm/grouped_gemm.py` | 17.2% |
| `kernels/sampling/min_p_mask.py` | 19.6% |
| `kernels/attention/deepseek_nsa_cmp_fwd.py` | 20.0% |
| `kernels/linear_attention/gated_deltanet/decode.py` | 21.4% |
| `kernels/quantization/fp8_quant_per_block.py` | 22.6% |
| `kernels/sampling/radix_select.py` | 23.6% |

<details>
<summary>Untested pure Python, worst 15 files</summary>

| File | Uncovered | Executed |
| --- | --- | --- |
| `perf/formulas.py` | 372 | 17.3% |
| `manifest/plan.py` | 349 | 30.3% |
| `manifest/workload.py` | 194 | 58.5% |
| `ops/op_base.py` | 156 | 70.1% |
| `manifest/primitives.py` | 146 | 54.8% |
| `manifest/expr.py` | 122 | 70.7% |
| `manifest/signature.py` | 109 | 76.3% |
| `ops/attention/gqa.py` | 103 | 56.7% |
| `ops/_signature_codegen.py` | 88 | 88.9% |
| `trace/ui.py` | 62 | 24.4% |
| `manifest/kinds.py` | 53 | 79.2% |
| `backend/registry.py` | 48 | 50.0% |
| `perf/profile.py` | 42 | 22.2% |
| `ops/rope.py` | 27 | 84.6% |
| `ops/reduction/reduce.py` | 27 | 80.1% |

</details>

Per-line detail is in the `htmlcov/` directory of this run's `tileops_op_test` artifact.
