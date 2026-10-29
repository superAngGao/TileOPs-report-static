# ❌ TileOPs Nightly Report

> **2026-10-25 20:02** &ensp;|&ensp; `d05abdbc` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Operators** | 206 |
| **Kernels** | 347 |
| **Specs** | 0 |
| **Workloads** | 1539 |
| **Correctness** | ✅ &ensp; (206/206 ops verified, 1359/1413 tests) |
| **Benchmarked Ops** | 206 |
| **Benchmark Failures** | ❌ 2 |
| **Regressions** (vs 14-day median) | ⚠️ 1 |
| **Baseline Alerts** (< 99%) | ⚠️ 10 |
| **vs Baseline** | ↑ 2226 &ensp;·&ensp; ↓ 10 &ensp;/&ensp; 2236 rows |
| **Rows no reference checked** | ⚠️ 226 |
| **History window** | 14 runs, 2026-10-11 to 2026-10-25 |
| **Roofline anomalies** | ✅ None |
| **New ops** (no 14-day history) | 🆕 1 ops · 6 rows |
| **Never-built kernels** | ✅ None |
| **Untested roofline math** | 0 lines in `perf/` |
| **Untested op logic** | 0 lines in `ops/` &ensp;·&ensp; 0.0% of branches taken |
| | <sub>coverage compared against the 2026-10-25 run; no figure means it held</sub> |

## ❌ Benchmark Failures

| Test | Error |
|:-----|:------|
| test_batch_norm_bwd_bench[resnet-fc-float16] | AssertionError: torch-native-batch-norm: shape mismatch: torch.Size([0]) != torch.Size([64]) |
| test_cumsum_bench[hidden-state-f32-bfloat16-float32] | AssertionError: flaggems: dtype mismatch: torch.bfloat16 != torch.float32 |

## ⚠️ Performance Regressions (vs 14-day median)

| Op | Config | Median (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **FusedAddLayerNormFwdOp** | test_fused_add_layer_norm_bench[llama-70b-decode-bfloat16] | 0.0036 | 0.0044 | +21.2% | 0.01 |

## 🆕 New Ops (no 14-day history)

| Op | Config | Current (ms) | TFLOPS |
|:---|:-------|-----------:|-------:|
| **GQADenseWithLSEFwdOp** | test_gqa_dense_with_lse_fwd_bench[llama-8b-short-float16] | 0.0435 | 200.18 |
| **GQADenseWithLSEFwdOp** | test_gqa_dense_with_lse_fwd_bench[llama-8b-short-bfloat16] | 0.0433 | 201.07 |
| **GQADenseWithLSEFwdOp** | test_gqa_dense_with_lse_fwd_bench[llama-8b-long-float16] | 0.1748 | 397.30 |
| **GQADenseWithLSEFwdOp** | test_gqa_dense_with_lse_fwd_bench[llama-8b-long-bfloat16] | 0.1730 | 401.48 |
| **GQADenseWithLSEFwdOp** | test_gqa_dense_with_lse_fwd_bench[llama-70b-long-bfloat16] | 0.1727 | 402.12 |
| **GQADenseWithLSEFwdOp** | test_gqa_dense_with_lse_fwd_bench[llama-8b-long-mha-bfloat16] | 0.1742 | 398.65 |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 99%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **CumprodFwdOp** | test_cumprod_bench[hidden-state-f32-bfloat16-float32] | 0.0474 | 0.0262 | 55.2% | torch-compile |
| 🔴 | **GQADenseWithLSEFwdOp** | test_gqa_dense_with_lse_fwd_bench[llama-8b-short-bfloat16] | 0.0433 | 0.0317 | 73.3% | fa3 |
| 🔴 | **GQADenseWithLSEFwdOp** | test_gqa_dense_with_lse_fwd_bench[llama-8b-short-float16] | 0.0435 | 0.0319 | 73.3% | fa3 |
| 🔴 | **GQADenseWithLSEFwdOp** | test_gqa_dense_with_lse_fwd_bench[llama-70b-long-bfloat16] | 0.1727 | 0.1322 | 76.5% | fa3 |
| 🔴 | **GQADenseWithLSEFwdOp** | test_gqa_dense_with_lse_fwd_bench[llama-8b-long-bfloat16] | 0.1730 | 0.1328 | 76.8% | fa3 |
| 🔴 | **GQADenseWithLSEFwdOp** | test_gqa_dense_with_lse_fwd_bench[llama-8b-long-float16] | 0.1748 | 0.1347 | 77.1% | fa3 |
| 🔴 | **GQADenseWithLSEFwdOp** | test_gqa_dense_with_lse_fwd_bench[llama-8b-long-mha-bfloat16] | 0.1742 | 0.1364 | 78.3% | fa3 |
| 🔴 | **GELUAndMulFwdOp** | test_gelu_and_mul_bench[llama-8b-ffn-decode-bfloat16] | 0.0016 | 0.0015 | 96.0% | torch-compile |
| 🔴 | **MinimumFwdOp** | test_minimum_bench[llama-7b-hidden-float16] | 0.0084 | 0.0082 | 97.5% | torch-compile |
| 🔴 | **ClampScalarFwdOp** | test_clamp_scalar_bench[256M-float16] | 0.2584 | 0.2555 | 98.9% | torch-compile |

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 0 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 0 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 0 lines in `ops/`, - of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 18152 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

<details>
<summary>Untested pure Python, worst 15 files</summary>

| File | Uncovered | Executed |
| --- | --- | --- |
| `_kernels/linear_attention/gdn/prefill_prepare.py` | 741 | 4.0% |
| `_kernels/attention/gqa/paged_fp8_ws.py` | 640 | 8.6% |
| `_kernels/attention/gqa/paged_ws.py` | 557 | 12.1% |
| `_kernels/attention/mla/decode.py` | 545 | 12.4% |
| `_perf/formulas.py` | 398 | 16.6% |
| `_kernels/attention/dsa/decode.py` | 388 | 18.8% |
| `_kernels/attention/gqa/dense.py` | 388 | 63.2% |
| `_kernels/sampling/top_k_top_p_mask.py` | 370 | 6.8% |
| `_kernels/linear_attention/kda/chunk_programs.py` | 352 | 36.6% |
| `_kernels/gemm/dense.py` | 330 | 79.6% |
| `_kernels/gemm/fp8_1d2d.py` | 316 | 48.8% |
| `_kernels/linear_attention/gdn/prefill_forward.py` | 309 | 4.0% |
| `_kernels/quantization/int8_quant_per_channel.py` | 272 | 16.0% |
| `_kernels/linear_attention/gla/varlen_prefill.py` | 269 | 12.1% |
| `_kernels/attention/nsa/compressed_varlen.py` | 258 | 13.7% |

</details>

Per-line detail is in the `htmlcov/` directory of this run's `tileops_op_test` artifact.
