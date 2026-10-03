# ✅ TileOPs Nightly Report

> **2026-09-21 23:48** &ensp;|&ensp; `cbf29a82` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Correctness** | ✅ &ensp; (514/514 tests across 85 ops) |
| **Benchmarked Ops** | 0 |
| **Benchmark Failures** | ✅ None |
| **Regressions** (vs 14-day median) | ✅ None |
| **Baseline Alerts** (< 80%) | ✅ None |
| **History window** | 13 runs, 2026-09-07 to 2026-09-21 |
| **Roofline anomalies** | ✅ None |
| **Never-built kernels** | ⚠️ 24 files &ensp;·&ensp; `kernels/linear_attention/gated_deltanet/compute_w_u_bwd.py` at 0.0% |
| **Untested roofline math** | 832 lines in `perf/` **+28** &ensp;·&ensp; `perf/formulas.py` at 11.8% |
| **Untested op logic** | 2454 lines in `ops/` **−173** &ensp;·&ensp; 38.9% of branches taken **+1.8pp** |
| | <sub>coverage compared against the 2026-09-20 run; no figure means it held</sub> |

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 24 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 832 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 2454 lines in `ops/`, 38.9% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 3569 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

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
| `kernels/attention/gqa_fwd.py` | 10.2% |
| `kernels/attention/gqa_dense.py` | 10.8% |
| `kernels/linear_attention/gated_deltanet/fused_prepare_compute_w_u.py` | 11.4% |
| `kernels/attention/mha_decode.py` | 11.7% |
| `kernels/attention/gqa_decode_bs1_common.py` | 12.4% |
| `kernels/attention/mha_decode_paged.py` | 12.5% |
| `kernels/linear_attention/gated_deltanet_recurrence.py` | 14.1% |
| `kernels/attention/gqa_decode.py` | 14.3% |
| `kernels/attention/gqa_decode_bs1.py` | 14.3% |
| `kernels/moe/indexed_expert_gemm.py` | 15.7% |
| `kernels/attention/gqa_decode_fp8.py` | 15.9% |
| `kernels/attention/gqa_prefill_varlen_fwd.py` | 17.5% |
| `kernels/grouped_gemm/grouped_gemm.py` | 17.7% |
| `kernels/attention/deepseek_nsa_cmp_fwd.py` | 18.1% |
| `kernels/linear_attention/gated_deltanet/prefill/dense.py` | 20.0% |
| `kernels/linear_attention/gated_deltanet/gated_deltanet_fwd.py` | 21.7% |
| `kernels/linear_attention/gated_deltanet/prefill/common.py` | 23.0% |

<details>
<summary>Untested pure Python, worst 15 files</summary>

| File | Uncovered | Executed |
| --- | --- | --- |
| `perf/formulas.py` | 790 | 11.8% |
| `ops/attention/gqa.py` | 648 | 26.2% |
| `ops/op_base.py` | 199 | 50.4% |
| `ops/linear_attention/gated_deltanet.py` | 118 | 16.3% |
| `ops/pool.py` | 87 | 84.8% |
| `ops/mamba/mamba2_fwd.py` | 84 | 20.0% |
| `ops/rope.py` | 83 | 69.5% |
| `ops/moe/staged.py` | 83 | 71.5% |
| `ops/convolution.py` | 82 | 79.7% |
| `ops/elementwise/_base.py` | 79 | 75.0% |
| `ops/linear_attention/deltanet.py` | 71 | 64.0% |
| `ops/reduction/reduce.py` | 62 | 69.5% |
| `trace/ui.py` | 62 | 24.4% |
| `ops/_roofline_codegen.py` | 61 | 78.0% |
| `ops/moe/routed_expert/indexed_routed_expert.py` | 59 | 33.7% |

</details>

Per-line detail is in the `htmlcov/` directory of this run's `tileops_op_test` artifact.
