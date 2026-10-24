# ✅ TileOPs Nightly Report

> **2026-10-23 21:10** &ensp;|&ensp; `08b717ad` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Operators** | 207 |
| **Kernels** | 350 |
| **Specs** | 0 |
| **Workloads** | 1529 |
| **Correctness** | ✅ &ensp; (207/207 ops verified, 1348/1402 tests) |
| **Benchmarked Ops** | 207 |
| **Benchmark Failures** | ✅ None |
| **Regressions** (vs 14-day median) | ✅ None |
| **Baseline Alerts** (< 99%) | ⚠️ 18 |
| **vs Baseline** | ↑ 2207 &ensp;·&ensp; ↓ 18 &ensp;/&ensp; 2225 rows |
| **Rows no reference checked** | ⚠️ 231 |
| **History window** | 14 runs, 2026-10-09 to 2026-10-23 |
| **Roofline anomalies** | ✅ None |
| **Improvements** (vs 14-day best) | 🎉 14 |
| **Moved since previous run** | 🔵 14 |
| **Never-built kernels** | ⚠️ 43 files **−5** &ensp;·&ensp; `kernels/linear_attention/gdn/prefill_forward.py` at 3.4% |
| **Untested roofline math** | 457 lines in `perf/` &ensp;·&ensp; `perf/formulas.py` at 16.3% |
| **Untested op logic** | 796 lines in `ops/` **−15** &ensp;·&ensp; 61.4% of branches taken **+0.4pp** |
| | <sub>coverage compared against the 2026-10-23 run; no figure means it held</sub> |

## 🎉 Performance Improvements (vs 14-day best)

| Op | Config | Prev Best (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **KDAFwdOp** | test_kda_fwd_bench[kda-tp2-4096-bfloat16] | 0.3537 | 0.2907 | -17.8% | 26.15 |
| **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-65536-bfloat16] | 2.2455 | 1.8578 | -17.3% | 16.36 |
| **KDAFwdOp** | test_kda_fwd_bench[kda-tp2-16384-bfloat16] | 1.2605 | 1.0512 | -16.6% | 28.92 |
| **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-16384-bfloat16] | 0.5958 | 0.4982 | -16.4% | 15.26 |
| **KDAFwdOp** | test_kda_fwd_bench[kda-tp4-4096-bfloat16] | 0.2337 | 0.1970 | -15.7% | 19.29 |
| **KDAFwdOp** | test_kda_fwd_bench[kda-tp2-65536-bfloat16] | 4.7775 | 4.0361 | -15.5% | 30.13 |
| **KDAFwdOp** | test_kda_fwd_bench[kda-tp4-16384-bfloat16] | 0.8199 | 0.6961 | -15.1% | 21.84 |
| **KDAFwdOp** | test_kda_fwd_bench[kda-tp1-4096-bfloat16] | 0.5797 | 0.4935 | -14.9% | 30.80 |
| **KDAFwdOp** | test_kda_fwd_bench[kda-tp4-65536-bfloat16] | 3.0835 | 2.6395 | -14.4% | 23.04 |
| **KDAFwdOp** | test_kda_fwd_bench[kda-tp1-16384-bfloat16] | 2.1398 | 1.8382 | -14.1% | 33.08 |
| **KDAFwdOp** | test_kda_fwd_bench[kda-tp1-65536-bfloat16] | 8.3011 | 7.1701 | -13.6% | 33.92 |
| **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-1024-7168-bfloat16] | 0.2940 | 0.2550 | -13.3% | 14.90 |
| **KDAFwdOp** | test_kda_fwd_bench[kda-tp1-1024-7168-bfloat16] | 1.1573 | 1.0077 | -12.9% | 30.17 |
| **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-16x8192-bfloat16] | 2.0101 | 1.7595 | -12.5% | 34.56 |

## 🔵 Moved Since Previous Run

> Moves against the most recent reading. A row restored to its old level appears only here: returning is not a new 14-day record.

| Op | Config | Previous (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **KDAFwdOp** | test_kda_fwd_bench[kda-tp2-4096-bfloat16] | 0.3578 | 0.2907 | -18.8% | 26.15 |
| **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-65536-bfloat16] | 2.2455 | 1.8578 | -17.3% | 16.36 |
| **KDAFwdOp** | test_kda_fwd_bench[kda-tp2-16384-bfloat16] | 1.2649 | 1.0512 | -16.9% | 28.92 |
| **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-16384-bfloat16] | 0.5977 | 0.4982 | -16.6% | 15.26 |
| **KDAFwdOp** | test_kda_fwd_bench[kda-tp2-65536-bfloat16] | 4.7960 | 4.0361 | -15.8% | 30.13 |
| **KDAFwdOp** | test_kda_fwd_bench[kda-tp4-4096-bfloat16] | 0.2337 | 0.1970 | -15.7% | 19.29 |
| **KDAFwdOp** | test_kda_fwd_bench[kda-tp4-16384-bfloat16] | 0.8238 | 0.6961 | -15.5% | 21.84 |
| **KDAFwdOp** | test_kda_fwd_bench[kda-tp1-4096-bfloat16] | 0.5817 | 0.4935 | -15.2% | 30.80 |
| **KDAFwdOp** | test_kda_fwd_bench[kda-tp4-65536-bfloat16] | 3.0835 | 2.6395 | -14.4% | 23.04 |
| **KDAFwdOp** | test_kda_fwd_bench[kda-tp1-16384-bfloat16] | 2.1398 | 1.8382 | -14.1% | 33.08 |
| **KDAFwdOp** | test_kda_fwd_bench[kda-tp1-65536-bfloat16] | 8.3257 | 7.1701 | -13.9% | 33.92 |
| **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-1024-7168-bfloat16] | 0.2955 | 0.2550 | -13.7% | 14.90 |
| **KDAFwdOp** | test_kda_fwd_bench[kda-tp1-1024-7168-bfloat16] | 1.1573 | 1.0077 | -12.9% | 30.17 |
| **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-16x8192-bfloat16] | 2.0101 | 1.7595 | -12.5% | 34.56 |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 99%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[qwen3-8b-chunked-b8-bfloat16] | 0.0684 | 0.0639 | 93.5% | fa3 |
| 🔴 | **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-fp8-prefill-float8_e4m3fn-float8_e4m3fn-bfloat16] | 0.4620 | 0.4433 | 96.0% | fa3 |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-qkv-a-bfloat16] | 0.1817 | 0.1757 | 96.7% | cublaslt-best |
| 🔴 | **MinimumFwdOp** | test_minimum_bench[llama-7b-hidden-float16] | 0.0084 | 0.0082 | 97.7% | torch-compile |
| 🔴 | **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[qwen3-fp8-ragged-odd-float8_e4m3fn-float8_e4m3fn-bfloat16] | 0.1637 | 0.1603 | 97.9% | fa3 |
| 🔴 | **EqFwdOp** | test_eq_bench[linear-bias-bfloat16] | 0.0047 | 0.0046 | 97.9% | torch-compile |
| 🔴 | **GeluAndMulFwdOp** | test_gelu_and_mul_bench[llama-8b-ffn-decode-bfloat16] | 0.0016 | 0.0015 | 98.0% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-q-b-bfloat16] | 0.4140 | 0.4057 | 98.0% | cublaslt-best |
| 🔴 | **ProdFwdOp** | test_prod_bench[3d-non-last-axis-float16] | 0.0035 | 0.0034 | 98.2% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-mlp-up-bfloat16] | 0.3341 | 0.3280 | 98.2% | cublaslt-best |

<details>
<summary><strong>8 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-decode-down-bfloat16] | 0.0135 | 0.0132 | 98.3% | torch-cublas |
| 🔴 | **MaximumFwdOp** | test_maximum_bench[llama-7b-hidden-float16] | 0.0084 | 0.0083 | 98.5% | torch-compile |
| 🔴 | **ClampTensorFwdOp** | test_clamp_bench[16M-max-only-float32] | 0.0494 | 0.0486 | 98.5% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-down-bfloat16] | 0.1725 | 0.1701 | 98.6% | cublaslt-best |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-1k-bfloat16] | 0.0298 | 0.0294 | 98.7% | quack |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-32768-bfloat16] | 0.2923 | 0.2886 | 98.8% | flashinfer |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-mlp-up-float16] | 0.3383 | 0.3341 | 98.8% | cublaslt-best |
| 🔴 | **RMSNormFwdOp** | test_rms_norm_bench[qk-norm-head-bfloat16] | 0.0029 | 0.0029 | 98.9% | torch-compile |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 43 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 457 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 796 lines in `ops/`, 61.4% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 2488 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

### Never-built kernels

| File | Executed |
| --- | --- |
| `kernels/linear_attention/gdn/prefill_forward.py` | 3.4% |
| `kernels/linear_attention/gdn/prefill_prepare.py` | 3.6% |
| `kernels/linear_attention/deltanet/prefill_forward.py` | 4.3% |
| `kernels/linear_attention/gdn/prefill_fused.py` | 5.6% |
| `kernels/linear_attention/deltanet/prefill_prepare.py` | 5.7% |
| `kernels/sampling/top_k_top_p_mask.py` | 6.5% |
| `kernels/attention/gqa/paged_rope_prepare.py` | 6.8% |
| `kernels/attention/gqa/prefill_paged_kv_append.py` | 6.9% |
| `kernels/linear_attention/gdn/prefill_common.py` | 7.4% |
| `kernels/linear_attention/delta_decode.py` | 7.8% |
| `kernels/attention/gqa/paged_fp8_ws.py` | 8.5% |
| `kernels/sampling/top_k_mask.py` | 10.8% |
| `kernels/sampling/sampling_from_probs.py` | 11.8% |
| `kernels/sampling/chain_speculative_sampling.py` | 11.8% |
| `kernels/linear_attention/gla/varlen_prefill.py` | 12.2% |
| `kernels/attention/gqa/paged_ws.py` | 12.3% |
| `kernels/attention/mla/decode.py` | 12.3% |
| `kernels/sampling/top_p_mask.py` | 12.4% |
| `kernels/quantization/int8_quant_per_tensor.py` | 12.9% |
| `kernels/attention/gqa/paged_fp8_decode.py` | 13.0% |
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
| `kernels/attention/gqa/prefill_paged_ws.py` | 17.5% |
| `kernels/attention/dsa/decode.py` | 18.6% |
| `kernels/linear_attention/deltanet/partition_scan.py` | 19.1% |
| `kernels/sampling/min_p_mask.py` | 19.7% |
| `kernels/attention/gqa/sliding_window_varlen.py` | 20.1% |
| `kernels/norm/instance_norm.py` | 20.8% |
| `kernels/linear_attention/gla/dense_decode.py` | 21.2% |
| `kernels/moe/moe_grouped_gemm.py` | 21.4% |
| `kernels/quantization/fp8_quant_per_block.py` | 22.4% |
| `kernels/linear_attention/gdn/prefill.py` | 22.4% |
| `kernels/moe/shared_expert_mlp.py` | 23.1% |
| `kernels/norm/rms_norm_on_chip.py` | 23.1% |
| `kernels/sampling/radix_select.py` | 24.1% |

<details>
<summary>Untested pure Python, worst 15 files</summary>

| File | Uncovered | Executed |
| --- | --- | --- |
| `perf/formulas.py` | 415 | 16.3% |
| `manifest/plan.py` | 364 | 29.5% |
| `manifest/workload.py` | 181 | 61.2% |
| `ops/op_base.py` | 161 | 67.9% |
| `manifest/primitives.py` | 132 | 61.5% |
| `manifest/expr.py` | 122 | 70.7% |
| `manifest/signature.py` | 107 | 77.1% |
| `ops/_signature_codegen.py` | 85 | 89.8% |
| `trace/ui.py` | 60 | 23.1% |
| `backend/registry.py` | 57 | 46.7% |
| `manifest/kinds.py` | 53 | 79.2% |
| `ops/attention/gqa/prefill_paged_kv_append.py` | 53 | 35.4% |
| `backend/dispatch.py` | 48 | 40.0% |
| `perf/profile.py` | 42 | 22.2% |
| `ops/reduction/reduce.py` | 27 | 79.4% |

</details>

Per-line detail is in the `htmlcov/` directory of this run's `tileops_op_test` artifact.
