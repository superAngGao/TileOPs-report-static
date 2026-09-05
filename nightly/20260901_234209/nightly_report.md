# ✅ TileOPs Nightly Report

> **2026-09-01 22:20** &ensp;|&ensp; `4157ef4e` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Correctness** | ✅ &ensp; (528/528 tests across 92 ops) |
| **Benchmarked Ops** | 0 |
| **Benchmark Failures** | ✅ None |
| **Regressions** (vs 14-day median) | ✅ None |
| **Baseline Alerts** (< 80%) | ✅ None |
| **Roofline anomalies** | ✅ None |
| **Never-built kernels** | ⚠️ 9 files &ensp;·&ensp; `kernels/attention/deepseek_mla_decode.py` at 5.8% |
| **Untested roofline math** | 752 lines in `perf/` **+2** &ensp;·&ensp; `perf/formulas.py` at 11.6% |
| **Untested op logic** | 2495 lines in `ops/` **−108** &ensp;·&ensp; 40.5% of branches taken **+1.4pp** |
| | <sub>coverage compared against the 2026-08-31 run; no figure means it held</sub> |

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 9 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 752 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 2495 lines in `ops/`, 40.5% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 3530 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

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
| `perf/formulas.py` | 710 | 11.6% |
| `ops/attention/gqa.py` | 518 | 38.6% |
| `ops/pool.py` | 136 | 76.4% |
| `ops/moe/staged.py` | 131 | 51.8% |
| `ops/convolution.py` | 120 | 74.1% |
| `ops/linear_attention/gated_deltanet.py` | 111 | 73.3% |
| `ops/op_base.py` | 102 | 60.0% |
| `ops/reduction/reduce.py` | 100 | 58.5% |
| `ops/elementwise/_base.py` | 88 | 76.7% |
| `ops/mamba/mamba2_fwd.py` | 86 | 20.4% |
| `ops/rope.py` | 85 | 70.4% |
| `ops/_roofline_codegen.py` | 80 | 69.6% |
| `ops/moe/contracts.py` | 75 | 54.3% |
| `ops/linear_attention/deltanet.py` | 62 | 64.0% |
| `trace/ui.py` | 62 | 24.4% |

</details>

Per-line detail is in the `htmlcov/` directory of this run's `tileops_op_test` artifact.
