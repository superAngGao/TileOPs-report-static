# ✅ TileOPs Nightly Report

> **2026-10-26 20:28** &ensp;|&ensp; `f7e03a75` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Operators** | 206 |
| **Kernels** | 348 |
| **Specs** | 0 |
| **Workloads** | 1539 |
| **Correctness** | ✅ &ensp; (206/206 ops verified, 1360/1414 tests) |
| **Benchmarked Ops** | 206 |
| **Benchmark Failures** | ✅ None |
| **Regressions** (vs 14-day median) | ✅ None |
| **Baseline Alerts** (< 99%) | ⚠️ 3 |
| **vs Baseline** | ↑ 2235 &ensp;·&ensp; ↓ 3 &ensp;/&ensp; 2238 rows |
| **Rows no reference checked** | ⚠️ 226 |
| **History window** | 14 runs, 2026-10-12 to 2026-10-26 |
| **Roofline anomalies** | ✅ None |
| **Never-built kernels** | ✅ None |
| **Untested roofline math** | 0 lines in `perf/` |
| **Untested op logic** | 0 lines in `ops/` &ensp;·&ensp; 0.0% of branches taken |
| | <sub>coverage compared against the 2026-10-26 run; no figure means it held</sub> |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 99%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **NeFwdOp** | test_ne_bench[linear-bias-float16] | 0.0047 | 0.0045 | 97.6% | torch-compile |
| 🔴 | **RMSNormFwdOp** | test_rms_norm_bench[qk-norm-head-bfloat16] | 0.0029 | 0.0028 | 97.8% | torch-compile |
| 🔴 | **WhereFwdOp** | test_where_bench[16M-float32] | 0.0534 | 0.0527 | 98.6% | torch-compile |

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 0 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 0 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 0 lines in `ops/`, - of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 18454 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

<details>
<summary>Untested pure Python, worst 15 files</summary>

| File | Uncovered | Executed |
| --- | --- | --- |
| `_kernels/linear_attention/gdn/prefill_prepare.py` | 741 | 4.0% |
| `_kernels/attention/gqa/dense.py` | 683 | 56.2% |
| `_kernels/attention/gqa/paged_fp8_ws.py` | 640 | 8.6% |
| `_kernels/attention/gqa/paged_ws.py` | 557 | 12.1% |
| `_kernels/attention/mla/decode.py` | 545 | 12.4% |
| `_perf/formulas.py` | 398 | 16.6% |
| `_kernels/attention/dsa/decode.py` | 388 | 18.8% |
| `_kernels/sampling/top_k_top_p_mask.py` | 367 | 6.9% |
| `_kernels/linear_attention/kda/chunk_programs.py` | 352 | 36.6% |
| `_kernels/gemm/dense.py` | 330 | 79.6% |
| `_kernels/gemm/fp8_1d2d.py` | 316 | 48.8% |
| `_kernels/linear_attention/gdn/prefill_forward.py` | 309 | 4.0% |
| `_kernels/linear_attention/gla/varlen_prefill.py` | 269 | 12.1% |
| `_kernels/quantization/int8_quant_per_channel.py` | 269 | 16.2% |
| `_kernels/attention/nsa/compressed_varlen.py` | 258 | 13.7% |

</details>

Per-line detail is in the `htmlcov/` directory of this run's `tileops_op_test` artifact.
