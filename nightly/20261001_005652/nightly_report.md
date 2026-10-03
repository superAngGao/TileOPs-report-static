# ✅ TileOPs Nightly Report

> **2026-09-30 19:10** &ensp;|&ensp; `bbd496a9` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Correctness** | ✅ &ensp; (514/514 tests across 85 ops) |
| **Benchmarked Ops** | 190 |
| **Benchmark Failures** | ✅ None |
| **Regressions** (vs 14-day median) | ✅ None |
| **Baseline Alerts** (< 80%) | ⚠️ 18 |
| **History window** | 14 runs, 2026-09-16 to 2026-09-29 |
| **Roofline anomalies** | ✅ None |
| **Never-built kernels** | ⚠️ 23 files **+5** &ensp;·&ensp; `kernels/linear_attention/gated_deltanet/prefill_forward.py` at 3.5% |
| **Untested roofline math** | 414 lines in `perf/` &ensp;·&ensp; `perf/formulas.py` at 17.3% |
| **Untested op logic** | 953 lines in `ops/` **−54** &ensp;·&ensp; 59.2% of branches taken **+1.1pp** |
| | <sub>coverage compared against the 2026-09-29 run; no figure means it held</sub> |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 80%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-b64-p16-float16-float16] | 0.4000 | 0.2215 | 55.4% | flashinfer |
| 🔴 | **FusedTopKFwdOp** | test_fused_topk_bench[kimi-k2-t512-bias-float32] | 0.0117 | 0.0072 | 61.3% | vllm |
| 🔴 | **MultiHeadLatentAttentionDecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-32k-bfloat16] | 0.3928 | 0.2424 | 61.7% | torch-compile |
| 🔴 | **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-p16-float16-float16] | 0.3385 | 0.2188 | 64.6% | flashinfer |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-qkv-a-2d-float8_e4m3fn-bfloat16] | 0.1524 | 0.1089 | 71.4% | deepgemm |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-q-b-2d-float8_e4m3fn-bfloat16] | 0.3587 | 0.2617 | 73.0% | deepgemm |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-down-2d-float8_e4m3fn-bfloat16] | 0.1449 | 0.1063 | 73.3% | deepgemm |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-m1-down-2d-float8_e4m3fn-bfloat16] | 0.0105 | 0.0077 | 73.4% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **EngramGateConvBwdOp** | test_engram_gate_conv_bwd_bench[train-s96-bfloat16] | 0.1049 | 0.0810 | 77.2% | torch-compile |
| 🔴 | **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-405b-p256-float16-float16] | 0.0401 | 0.0310 | 77.3% | fa3 |

<details>
<summary><strong>8 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-p256-float16-float16] | 0.1823 | 0.1423 | 78.1% | fa3 |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[train-16k-float16] | 0.6178 | 0.4831 | 78.2% | fla |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 0.5643 | 0.4454 | 78.9% | fa3 |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-o-proj-2d-float8_e4m3fn-bfloat16] | 0.8723 | 0.6888 | 79.0% | deepgemm |
| 🔴 | **GemmFp8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-mlp-up-2d-float8_e4m3fn-bfloat16] | 0.2416 | 0.1910 | 79.0% | deepgemm |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[train-2k-float16] | 0.0984 | 0.0778 | 79.1% | fla |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.5625 | 0.4454 | 79.2% | fa3 |
| 🔴 | **GroupedQueryAttentionPagedFwdOp** | test_gqa_paged_fwd_bench[llama-70b-p256-float16-float16] | 0.0578 | 0.0461 | 79.9% | fa3 |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 23 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 414 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 953 lines in `ops/`, 59.2% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 2609 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

### Never-built kernels

| File | Executed |
| --- | --- |
| `kernels/linear_attention/gated_deltanet/prefill_forward.py` | 3.5% |
| `kernels/linear_attention/gated_deltanet/prefill_prepare.py` | 3.7% |
| `kernels/sampling/top_k_top_p_mask.py` | 5.8% |
| `kernels/attention/deepseek_mla_decode.py` | 6.2% |
| `kernels/attention/gqa_fwd_fp8.py` | 7.1% |
| `kernels/attention/gqa_fwd.py` | 7.7% |
| `kernels/sampling/top_k_mask.py` | 9.1% |
| `kernels/attention/gqa_dense.py` | 10.9% |
| `kernels/sampling/top_p_mask.py` | 12.4% |
| `kernels/quantization/int8_quant_per_tensor.py` | 12.8% |
| `kernels/attention/gqa_decode_bs1.py` | 13.8% |
| `kernels/attention/gqa_decode.py` | 14.8% |
| `kernels/linear_attention/gla/dense_prefill_partitioned.py` | 15.0% |
| `kernels/quantization/int8_quant_per_block.py` | 16.1% |
| `kernels/attention/gqa_decode_fp8.py` | 16.1% |
| `kernels/quantization/int8_quant_per_channel.py` | 16.2% |
| `kernels/linear_attention/gla/dense_prefill_subchunk.py` | 16.5% |
| `kernels/moe/indexed_expert_gemm.py` | 17.1% |
| `kernels/grouped_gemm/grouped_gemm.py` | 17.2% |
| `kernels/sampling/min_p_mask.py` | 19.6% |
| `kernels/attention/deepseek_nsa_cmp_fwd.py` | 20.0% |
| `kernels/linear_attention/gated_deltanet/decode.py` | 21.1% |
| `kernels/quantization/fp8_quant_per_block.py` | 22.6% |

<details>
<summary>Untested pure Python, worst 15 files</summary>

| File | Uncovered | Executed |
| --- | --- | --- |
| `perf/formulas.py` | 372 | 17.3% |
| `manifest/plan.py` | 349 | 30.3% |
| `manifest/workload.py` | 194 | 58.5% |
| `ops/op_base.py` | 174 | 69.6% |
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
