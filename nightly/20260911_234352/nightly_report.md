# ✅ TileOPs Nightly Report

> **2026-09-11 18:06** &ensp;|&ensp; `2716800e` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Correctness** | ✅ &ensp; (517/517 tests across 87 ops) |
| **Benchmarked Ops** | 0 |
| **Benchmark Failures** | ✅ None |
| **Regressions** (vs 14-day median) | ✅ None |
| **Baseline Alerts** (< 80%) | ✅ None |
| **Roofline anomalies** | ✅ None |
| **Never-built kernels** | ⚠️ 13 files **−1** &ensp;·&ensp; `kernels/attention/deepseek_mla_decode.py` at 5.8% |
| **Untested roofline math** | 827 lines in `perf/` &ensp;·&ensp; `perf/formulas.py` at 11.5% |
| **Untested op logic** | 2651 lines in `ops/` **−28** &ensp;·&ensp; 39.0% of branches taken **+0.1pp** |
| | <sub>coverage compared against the 2026-09-10 run; no figure means it held</sub> |

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 13 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 827 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 2651 lines in `ops/`, 39.0% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 3757 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

### Never-built kernels

| File | Executed |
| --- | --- |
| `kernels/attention/deepseek_mla_decode.py` | 5.8% |
| `kernels/attention/gqa_fwd_ws.py` | 6.4% |
| `kernels/attention/gqa_fwd_fp8.py` | 6.8% |
| `kernels/attention/gqa_dense.py` | 9.8% |
| `kernels/attention/gqa_fwd.py` | 11.2% |
| `kernels/attention/mha_decode_paged.py` | 11.6% |
| `kernels/attention/gqa_decode_bs1_common.py` | 12.4% |
| `kernels/attention/gqa_decode.py` | 13.2% |
| `kernels/attention/mha_decode.py` | 13.2% |
| `kernels/attention/gqa_decode_bs1.py` | 13.4% |
| `kernels/grouped_gemm/grouped_gemm.py` | 15.7% |
| `kernels/attention/gqa_prefill_varlen_fwd.py` | 18.7% |
| `kernels/attention/deepseek_nsa_cmp_fwd.py` | 19.6% |

<details>
<summary>Untested pure Python, worst 15 files</summary>

| File | Uncovered | Executed |
| --- | --- | --- |
| `perf/formulas.py` | 785 | 11.5% |
| `ops/attention/gqa.py` | 673 | 23.9% |
| `ops/pool.py` | 154 | 76.6% |
| `ops/convolution.py` | 120 | 74.1% |
| `ops/op_base.py` | 116 | 57.2% |
| `ops/linear_attention/gated_deltanet.py` | 114 | 72.9% |
| `ops/moe/staged.py` | 106 | 68.5% |
| `ops/reduction/reduce.py` | 100 | 58.5% |
| `ops/elementwise/_base.py` | 88 | 76.7% |
| `ops/mamba/mamba2_fwd.py` | 86 | 20.4% |
| `ops/rope.py` | 85 | 70.4% |
| `ops/_roofline_codegen.py` | 84 | 68.1% |
| `ops/linear_attention/deltanet.py` | 65 | 63.3% |
| `trace/ui.py` | 62 | 24.4% |
| `ops/moe/shared_fused_moe.py` | 58 | 20.5% |

</details>

Per-line detail is in the `htmlcov/` directory of this run's `tileops_op_test` artifact.
