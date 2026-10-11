# ✅ TileOPs Nightly Report

> **2026-09-29 18:52** &ensp;|&ensp; `2ce972f9` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Correctness** | ✅ &ensp; (513/513 tests across 84 ops) |
| **Benchmarked Ops** | 179 |
| **Benchmark Failures** | ✅ None |
| **Regressions** (vs 14-day median) | ✅ None |
| **Baseline Alerts** (< 80%) | ⚠️ 17 |
| **History window** | 14 runs, 2026-09-15 to 2026-09-28 |
| **Roofline anomalies** | ✅ None |
| **Moved since previous run** | 🔵 12 |
| **Never-built kernels** | ⚠️ 18 files **−1** &ensp;·&ensp; `kernels/linear_attention/gated_deltanet/prefill/forward.py` at 3.5% |
| **Untested roofline math** | 414 lines in `perf/` &ensp;·&ensp; `perf/formulas.py` at 17.3% |
| **Untested op logic** | 1007 lines in `ops/` **+139** &ensp;·&ensp; 58.1% of branches taken |
| | <sub>coverage compared against the 2026-09-28 run; no figure means it held</sub> |

## 🔵 Moved Since Previous Run

> Moves against the most recent reading. A row restored to its old level appears only here: returning is not a new 14-day record.

| Op | Config | Previous (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **FloorDivideFwdOp** | test_floor_divide_bench[cnn-feat-broadcast-float16] | 0.0225 | 0.0148 | -34.4% | 1.74 |
| **FloorDivideFwdOp** | test_floor_divide_bench[cnn-feat-broadcast-bfloat16] | 0.0221 | 0.0147 | -33.7% | 1.75 |
| **FloorDivideFwdOp** | test_floor_divide_bench[linear-bias-bfloat16] | 0.0093 | 0.0065 | -29.9% | 1.29 |
| **FloorDivideFwdOp** | test_floor_divide_bench[linear-bias-float16] | 0.0088 | 0.0062 | -29.2% | 1.35 |
| **RemainderFwdOp** | test_remainder_bench[cnn-feat-broadcast-float16] | 0.0202 | 0.0153 | -24.0% | 3.36 |
| **RemainderFwdOp** | test_remainder_bench[cnn-feat-broadcast-bfloat16] | 0.0198 | 0.0157 | -20.7% | 3.27 |
| **RemainderFwdOp** | test_remainder_bench[linear-bias-bfloat16] | 0.0093 | 0.0074 | -20.0% | 2.26 |
| **RemainderFwdOp** | test_remainder_bench[linear-bias-float16] | 0.0088 | 0.0072 | -17.8% | 2.32 |
| **FloorDivideFwdOp** | test_floor_divide_bench[hidden-state-prefill-bfloat16] | 0.0176 | 0.0148 | -16.3% | 1.14 |
| **FloorDivideFwdOp** | test_floor_divide_bench[llama-7b-ffn-bfloat16] | 0.0224 | 0.0188 | -16.3% | 1.20 |
| **RemainderFwdOp** | test_remainder_bench[llama-7b-ffn-bfloat16] | 0.0221 | 0.0198 | -10.7% | 2.28 |
| **RemainderFwdOp** | test_remainder_bench[hidden-state-prefill-bfloat16] | 0.0174 | 0.0156 | -10.5% | 2.16 |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 80%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-b64-p16-float16-float16] | 0.4002 | 0.2211 | 55.3% | flashinfer |
| 🔴 | **FusedTopKFwdOp** | test_fused_topk_bench[kimi-k2-t512-bias-float32] | 0.0117 | 0.0072 | 61.3% | vllm |
| 🔴 | **MultiHeadLatentAttentionDecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-32k-bfloat16] | 0.3931 | 0.2446 | 62.2% | torch-compile |
| 🔴 | **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-p16-float16-float16] | 0.3380 | 0.2188 | 64.7% | flashinfer |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-qkv-a-2d-float8_e4m3fn-bfloat16] | 0.1528 | 0.1094 | 71.6% | deepgemm |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-q-b-2d-float8_e4m3fn-bfloat16] | 0.3584 | 0.2620 | 73.1% | deepgemm |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-m1-down-2d-float8_e4m3fn-bfloat16] | 0.0105 | 0.0077 | 73.4% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-down-2d-float8_e4m3fn-bfloat16] | 0.1447 | 0.1062 | 73.4% | deepgemm |
| 🔴 | **EngramGateConvBwdOp** | test_engram_gate_conv_bwd_bench[train-s96-bfloat16] | 0.1048 | 0.0812 | 77.4% | torch-compile |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[train-16k-float16] | 0.6180 | 0.4832 | 78.2% | fla |

<details>
<summary><strong>7 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-o-proj-2d-float8_e4m3fn-bfloat16] | 0.8705 | 0.6808 | 78.2% | deepgemm |
| 🔴 | **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-405b-p256-float16-float16] | 0.0397 | 0.0310 | 78.2% | fa3 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-mlp-up-2d-float8_e4m3fn-bfloat16] | 0.2420 | 0.1895 | 78.3% | deepgemm |
| 🔴 | **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-p256-float16-float16] | 0.1811 | 0.1425 | 78.7% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 0.5635 | 0.4452 | 79.0% | fa3 |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[train-2k-float16] | 0.0985 | 0.0780 | 79.2% | fla |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.5633 | 0.4471 | 79.4% | fa3 |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 18 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 414 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 1007 lines in `ops/`, 58.1% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 2658 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

### Never-built kernels

| File | Executed |
| --- | --- |
| `kernels/linear_attention/gated_deltanet/prefill/forward.py` | 3.5% |
| `kernels/linear_attention/gated_deltanet/prefill/prepare.py` | 3.7% |
| `kernels/attention/gqa_fwd_fp8.py` | 8.6% |
| `kernels/attention/gqa_fwd.py` | 8.6% |
| `kernels/attention/deepseek_mla_decode.py` | 9.0% |
| `kernels/attention/gqa_dense.py` | 12.0% |
| `kernels/linear_attention/gla/dense_prefill_partitioned.py` | 15.0% |
| `kernels/attention/gqa_decode.py` | 15.0% |
| `kernels/attention/gqa_decode_bs1.py` | 15.2% |
| `kernels/moe/indexed_expert_gemm.py` | 15.4% |
| `kernels/linear_attention/gla/dense_prefill_subchunk.py` | 16.5% |
| `kernels/attention/deepseek_nsa_cmp_fwd.py` | 17.6% |
| `kernels/grouped_gemm/grouped_gemm.py` | 17.7% |
| `kernels/attention/gqa_decode_fp8.py` | 17.8% |
| `kernels/linear_attention/gated_deltanet/decode.py` | 17.8% |
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
| `ops/op_base.py` | 158 | 72.4% |
| `manifest/primitives.py` | 146 | 54.8% |
| `manifest/expr.py` | 121 | 70.9% |
| `ops/attention/gqa.py` | 107 | 57.9% |
| `manifest/signature.py` | 105 | 77.2% |
| `ops/_signature_codegen.py` | 75 | 90.3% |
| `trace/ui.py` | 62 | 24.4% |
| `manifest/kinds.py` | 53 | 79.2% |
| `ops/linear_attention/gated_deltanet.py` | 49 | 27.9% |
| `backend/registry.py` | 48 | 50.0% |
| `perf/profile.py` | 42 | 22.2% |
| `ops/moe/routed_expert/indexed_routed_expert.py` | 38 | 45.7% |

</details>

Per-line detail is in the `htmlcov/` directory of this run's `tileops_op_test` artifact.
