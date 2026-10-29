# ❌ TileOPs Nightly Report

> **2026-10-24 21:06** &ensp;|&ensp; `87f8e308` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Operators** | 206 |
| **Kernels** | 346 |
| **Specs** | 0 |
| **Workloads** | 1529 |
| **Correctness** | ✅ &ensp; (206/206 ops verified, 1350/1404 tests) |
| **Benchmarked Ops** | 206 |
| **Benchmark Failures** | ✅ None |
| **Regressions** (vs 14-day median) | ⚠️ 4 |
| **Baseline Alerts** (< 99%) | ⚠️ 13 |
| **vs Baseline** | ↑ 2212 &ensp;·&ensp; ↓ 13 &ensp;/&ensp; 2225 rows |
| **Rows no reference checked** | ⚠️ 231 |
| **History window** | 14 runs, 2026-10-10 to 2026-10-24 |
| **Roofline anomalies** | ✅ None |
| **Moved since previous run** | 🔵 6 |
| **Never-built kernels** | ⚠️ 40 files &ensp;·&ensp; `kernels/linear_attention/gdn/prefill_forward.py` at 3.4% |
| **Untested roofline math** | 438 lines in `perf/` &ensp;·&ensp; `perf/formulas.py` at 16.6% |
| **Untested op logic** | 778 lines in `ops/` &ensp;·&ensp; 64.2% of branches taken |
| | <sub>coverage compared against the 2026-10-24 run; no figure means it held</sub> |

## ⚠️ Performance Regressions (vs 14-day median)

| Op | Config | Median (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[global-1x1-unbatched-float16] | 0.0020 | 0.0032 | +58.7% | 0.03 |
| **EngramGateConvBwdOp** | test_engram_gate_conv_bwd_bench[train-s64-float16] | 0.0199 | 0.0273 | +37.1% | 0.16 |
| **AdaptiveMaxPool2dFwdOp** | test_adaptive_max_pool2d_bench[global-1x1-unbatched-float16] | 0.0019 | 0.0023 | +22.0% | 0.04 |
| **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[nondiv-7x7-bfloat16] | 0.0035 | 0.0040 | +13.8% | 0.12 |

## 🔵 Moved Since Previous Run

> Moves against the most recent reading. A row restored to its old level appears only here: returning is not a new 14-day record.

| Op | Config | Previous (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[spp-6x6-float16] | 0.0051 | 0.0039 | -23.1% | 0.23 |
| **AdaptiveMaxPool2dIndicesFwdOp** | test_adaptive_max_pool2d_indices_bench[nondiv-7x7-bfloat16] | 0.0050 | 0.0040 | -21.0% | 0.12 |
| **EngramGateConvFwdOp** | test_engram_gate_conv_fwd_bench[train-s64-float16] | 0.0060 | 0.0048 | -19.7% | 0.39 |
| **EngramGateConvFwdOp** | test_engram_gate_conv_fwd_bench[train-s96-bfloat16] | 0.0085 | 0.0072 | -15.4% | 0.89 |
| **EngramGateConvBwdOp** | test_engram_gate_conv_bwd_bench[train-s32-float16] | 0.0112 | 0.0096 | -14.2% | 0.06 |
| **EngramGateConvBwdOp** | test_engram_gate_conv_bwd_bench[train-s64-float16] | 0.0226 | 0.0273 | +20.7% | 0.16 |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 99%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[qwen35-9b-rope-chunk-float16-float16] | 126.5300 | 20.1054 | 15.9% | fa3 |
| 🔴 | **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[qwen35-9b-mixed-chunk-float16-float16] | 49.6056 | 8.5543 | 17.2% | fa3 |
| 🔴 | **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[qwen35-9b-chunk-fp8kv-float16-float8_e4m3fn] | 85.5487 | 47.8115 | 55.9% | flashinfer |
| 🔴 | **AdaptiveMaxPool2dFwdOp** | test_adaptive_max_pool2d_bench[global-1x1-unbatched-float16] | 0.0023 | 0.0020 | 87.5% | torch-compile |
| 🔴 | **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-fp8-prefill-float8_e4m3fn-float8_e4m3fn-bfloat16] | 0.4621 | 0.4434 | 96.0% | fa3 |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-qkv-a-bfloat16] | 0.1800 | 0.1764 | 98.0% | torch-cublas |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-mlp-up-bfloat16] | 0.3335 | 0.3270 | 98.0% | torch-cublas |
| 🔴 | **ProdFwdOp** | test_prod_bench[3d-non-last-axis-float16] | 0.0035 | 0.0034 | 98.2% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-decode-down-bfloat16] | 0.0135 | 0.0132 | 98.3% | torch-cublas |
| 🔴 | **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[qwen3-fp8-ragged-odd-float8_e4m3fn-float8_e4m3fn-bfloat16] | 0.1628 | 0.1602 | 98.4% | fa3 |

<details>
<summary><strong>3 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-mlp-up-float16] | 0.3389 | 0.3341 | 98.6% | cublaslt-best |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-32768-bfloat16] | 0.2923 | 0.2888 | 98.8% | flashinfer |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-down-bfloat16] | 0.1723 | 0.1705 | 98.9% | cublaslt-best |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 40 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 438 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 778 lines in `ops/`, 64.2% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 2451 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

### Never-built kernels

| File | Executed |
| --- | --- |
| `kernels/linear_attention/gdn/prefill_forward.py` | 3.4% |
| `kernels/linear_attention/gdn/prefill_prepare.py` | 3.6% |
| `kernels/linear_attention/deltanet/prefill_forward.py` | 4.3% |
| `kernels/linear_attention/gdn/prefill_fused.py` | 5.6% |
| `kernels/linear_attention/deltanet/prefill_prepare.py` | 5.7% |
| `kernels/sampling/top_k_top_p_mask.py` | 6.6% |
| `kernels/attention/gqa/paged_rope_prepare.py` | 6.8% |
| `kernels/linear_attention/gdn/prefill_common.py` | 7.4% |
| `kernels/linear_attention/delta_decode.py` | 7.8% |
| `kernels/attention/gqa/paged_fp8_ws.py` | 8.8% |
| `kernels/sampling/top_k_mask.py` | 11.0% |
| `kernels/sampling/sampling_from_probs.py` | 11.8% |
| `kernels/sampling/chain_speculative_sampling.py` | 11.8% |
| `kernels/linear_attention/gla/varlen_prefill.py` | 12.2% |
| `kernels/attention/mla/decode.py` | 12.3% |
| `kernels/sampling/top_p_mask.py` | 12.4% |
| `kernels/attention/gqa/paged_ws.py` | 12.5% |
| `kernels/quantization/int8_quant_per_tensor.py` | 12.9% |
| `kernels/attention/nsa/compressed_varlen.py` | 13.5% |
| `kernels/linear_attention/gla/dense_prefill_partitioned.py` | 14.7% |
| `kernels/linear_attention/gla/varlen_prefill_partitioned.py` | 15.1% |
| `kernels/quantization/int8_quant_per_channel.py` | 15.5% |
| `kernels/quantization/int8_quant_per_block.py` | 16.0% |
| `kernels/linear_attention/gla/dense_prefill_subchunk.py` | 16.7% |
| `kernels/attention/mla/bwd.py` | 16.9% |
| `kernels/moe/indexed_expert_gemm.py` | 17.0% |
| `kernels/gemm/grouped/general.py` | 17.2% |
| `kernels/attention/dsa/paged_mma.py` | 17.3% |
| `kernels/attention/dsa/decode.py` | 18.8% |
| `kernels/linear_attention/deltanet/partition_scan.py` | 19.1% |
| `kernels/sampling/min_p_mask.py` | 19.7% |
| `kernels/attention/gqa/sliding_window_varlen.py` | 20.1% |
| `kernels/norm/instance_norm.py` | 20.8% |
| `kernels/linear_attention/gla/dense_decode.py` | 21.2% |
| `kernels/moe/moe_grouped_gemm.py` | 21.4% |
| `kernels/sampling/radix_select.py` | 21.5% |
| `kernels/quantization/fp8_quant_per_block.py` | 22.4% |
| `kernels/linear_attention/gdn/prefill.py` | 22.4% |
| `kernels/norm/rms_norm_on_chip.py` | 22.8% |
| `kernels/moe/shared_expert_mlp.py` | 23.1% |

<details>
<summary>Untested pure Python, worst 15 files</summary>

| File | Uncovered | Executed |
| --- | --- | --- |
| `perf/formulas.py` | 396 | 16.6% |
| `manifest/plan.py` | 364 | 29.5% |
| `manifest/workload.py` | 181 | 61.2% |
| `ops/op_base.py` | 176 | 69.4% |
| `manifest/primitives.py` | 132 | 61.5% |
| `manifest/expr.py` | 122 | 70.7% |
| `manifest/signature.py` | 107 | 77.2% |
| `ops/_signature_codegen.py` | 105 | 89.1% |
| `trace/ui.py` | 60 | 23.1% |
| `backend/registry.py` | 57 | 46.7% |
| `manifest/kinds.py` | 53 | 79.2% |
| `backend/dispatch.py` | 48 | 40.0% |
| `perf/profile.py` | 42 | 22.2% |
| `ops/reduction/reduce.py` | 27 | 79.4% |
| `ops/moe/fused_moe_shared_expert.py` | 25 | 32.4% |

</details>

Per-line detail is in the `htmlcov/` directory of this run's `tileops_op_test` artifact.
