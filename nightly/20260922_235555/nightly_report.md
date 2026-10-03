# ✅ TileOPs Nightly Report

> **2026-09-22 18:38** &ensp;|&ensp; `b07a259f` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Correctness** | ✅ &ensp; (514/514 tests across 85 ops) |
| **Benchmarked Ops** | 176 |
| **Benchmark Failures** | ✅ None &ensp;|&ensp; ⚠️ 3 skipped |
| **Regressions** (vs 14-day median) | ✅ None |
| **Baseline Alerts** (< 80%) | ⚠️ 57 |
| **History window** | 12 runs, 2026-09-08 to 2026-09-21 |
| **Roofline anomalies** | ⚠️ 3 |
| **Never-built kernels** | ⚠️ 24 files &ensp;·&ensp; `kernels/linear_attention/gated_deltanet/compute_w_u_bwd.py` at 0.0% |
| **Untested roofline math** | 848 lines in `perf/` **+44** &ensp;·&ensp; `perf/formulas.py` at 11.8% |
| **Untested op logic** | 2427 lines in `ops/` **−200** &ensp;·&ensp; 39.0% of branches taken **+1.9pp** |
| | <sub>coverage compared against the 2026-09-20 run; no figure means it held</sub> |

## ⚠️ Roofline Model Anomalies

> A FAIL row implies a rate above the hardware's theoretical ceiling: its (flops, bytes) formula or declared roof is wrong, and its SOL reading cannot be trusted. A WARN row exceeds the calibrated ceiling; recheck the formula or the calibration.

| Level | Op | Config | Signal |
|:------|:---|:-------|:-------|
| WARN | **BmmFwdOp** | test_bmm_bench[square-b4-4k-bfloat16] | 105% of the calibrated ceiling |
| WARN | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-attn-proj-float16] | 107% of the calibrated ceiling |
| WARN | **GemmFwdOp** | test_gemm_bench[k-dominant-7168x16384-bfloat16] | 108% of the calibrated ceiling |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 80%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-bfloat16] | 0.4558 | 0.1430 | 31.4% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-bfloat16] | 0.4533 | 0.1423 | 31.4% | fa3 |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b4-dmem1024-d512-float16] | 0.0826 | 0.0260 | 31.5% | torch-compile |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-b64-complex64] | 0.0152 | 0.0056 | 37.0% | torch-cufft |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-short-bfloat16] | 0.4084 | 0.1596 | 39.1% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-short-bfloat16] | 0.4141 | 0.1654 | 39.9% | fa3 |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b1-dmem512-d256-float16] | 0.0330 | 0.0132 | 40.1% | torch-compile |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c128-b64-complex128] | 0.0205 | 0.0085 | 41.3% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-bfloat16] | 1.3102 | 0.5479 | 41.8% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-q-lt-kv-bfloat16] | 0.1126 | 0.0535 | 47.5% | fa3 |

<details>
<summary><strong>47 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-bfloat16] | 1.2422 | 0.5916 | 47.6% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-q-lt-kv-float16] | 0.1129 | 0.0539 | 47.7% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p256-float16] | 0.1651 | 0.0815 | 49.3% | fa3 |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-small-bfloat16] | 0.0394 | 0.0197 | 49.9% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-bfloat16] | 1.1021 | 0.5506 | 50.0% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-405b-p256-float16] | 0.0537 | 0.0269 | 50.1% | fa3 |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-2p7b-b2-s32k-dt-bias-float16] | 0.0443 | 0.0223 | 50.3% | mamba |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-70b-q-lt-kv-float16] | 0.1984 | 0.1002 | 50.5% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-70b-q-lt-kv-bfloat16] | 0.1965 | 0.0992 | 50.5% | fa3 |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-dt-bias-bfloat16] | 0.0124 | 0.0064 | 51.4% | mamba |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-bfloat16] | 0.0121 | 0.0064 | 53.0% | mamba |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-70b-p256-float16] | 0.0666 | 0.0371 | 55.6% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 1.0176 | 0.5776 | 56.8% | fa3 |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-medium-bfloat16] | 0.0544 | 0.0313 | 57.6% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-float16] | 0.2447 | 0.1430 | 58.5% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-float16] | 0.2426 | 0.1424 | 58.7% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[throughput-8b-p64-float16] | 0.2476 | 0.1508 | 60.9% | flashinfer |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-float16] | 0.9017 | 0.5518 | 61.2% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-float16] | 0.8913 | 0.5530 | 62.0% | fa3 |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b8-dmem512-d256-bfloat16] | 0.0335 | 0.0211 | 62.8% | torch-compile |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-unbatched-complex64] | 0.0081 | 0.0054 | 66.9% | torch-cufft |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-bfloat16] | 0.0971 | 0.0657 | 67.7% | fla |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-long-k-pressure-float16] | 0.2032 | 0.1426 | 70.2% | marlin-fp16 |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-non-power2-low-cta-float16] | 0.0578 | 0.0407 | 70.4% | marlin-fp32 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-float16] | 0.8320 | 0.5926 | 71.2% | fa3 |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-float16] | 0.0982 | 0.0702 | 71.5% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0569 | 0.0410 | 72.0% | flashinfer |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.8073 | 0.5826 | 72.2% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-float16] | 0.0570 | 0.0414 | 72.6% | flashinfer |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-softcap50-float16] | 0.1729 | 0.1256 | 72.6% | flashinfer |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-uniform-float16] | 0.0608 | 0.0450 | 74.0% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-uniform-bfloat16] | 0.0605 | 0.0449 | 74.2% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-float16] | 0.0929 | 0.0690 | 74.2% | flashinfer |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-bfloat16] | 0.0931 | 0.0693 | 74.4% | flashinfer |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-l2-resident-ish-float16] | 0.0287 | 0.0217 | 75.5% | marlin-fp32 |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-float16] | 0.6173 | 0.4659 | 75.5% | fla |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-bfloat16] | 0.3115 | 0.2359 | 75.8% | fla |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-float16] | 0.1648 | 0.1256 | 76.2% | flashinfer |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.6691 | 0.5165 | 77.2% | flashinfer |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.3493 | 0.2703 | 77.4% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-float16] | 0.3516 | 0.2723 | 77.4% | fa3 |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-bfloat16] | 0.6112 | 0.4764 | 77.9% | fla |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-float16] | 0.6684 | 0.5214 | 78.0% | flashinfer |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-hbm-streaming-threshold-float16] | 0.0486 | 0.0381 | 78.3% | marlin-fp16 |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-float16] | 0.3127 | 0.2477 | 79.2% | fla |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-large-bfloat16] | 0.0716 | 0.0567 | 79.2% | torch-compile |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0042 | 0.0034 | 79.5% | mamba |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 24 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 848 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 2427 lines in `ops/`, 39.0% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 3558 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

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
| `perf/formulas.py` | 806 | 11.8% |
| `ops/attention/gqa.py` | 635 | 26.2% |
| `ops/op_base.py` | 199 | 50.4% |
| `ops/linear_attention/gated_deltanet.py` | 118 | 16.3% |
| `ops/pool.py` | 87 | 84.8% |
| `ops/mamba/mamba2_fwd.py` | 84 | 20.0% |
| `ops/rope.py` | 83 | 69.5% |
| `ops/convolution.py` | 82 | 79.7% |
| `ops/elementwise/_base.py` | 79 | 75.0% |
| `ops/linear_attention/deltanet.py` | 71 | 64.0% |
| `ops/moe/staged.py` | 70 | 74.7% |
| `ops/reduction/reduce.py` | 62 | 69.5% |
| `trace/ui.py` | 62 | 24.4% |
| `ops/_roofline_codegen.py` | 60 | 78.1% |
| `ops/moe/routed_expert/indexed_routed_expert.py` | 59 | 33.7% |

</details>

Per-line detail is in the `htmlcov/` directory of this run's `tileops_op_test` artifact.
