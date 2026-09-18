# ❌ TileOPs Nightly Report

> **2026-09-17 18:50** &ensp;|&ensp; `3037d716` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Correctness** | ✅ &ensp; (514/514 tests across 85 ops) |
| **Benchmarked Ops** | 175 |
| **Benchmark Failures** | ❌ 1 &ensp;|&ensp; ⚠️ 3 skipped |
| **Regressions** (vs 14-day median) | ✅ None |
| **Baseline Alerts** (< 80%) | ⚠️ 66 |
| **Roofline anomalies** | ❌ 8 impossible |
| **Improvements** (vs 14-day best) | 🎉 2 |
| **Moved since previous run** | 🔵 3 |
| **Never-built kernels** | ⚠️ 26 files **+1** &ensp;·&ensp; `kernels/linear_attention/gated_deltanet/compute_w_u_bwd.py` at 0.0% |
| **Untested roofline math** | 788 lines in `perf/` **+1** &ensp;·&ensp; `perf/formulas.py` at 11.8% |
| **Untested op logic** | 2599 lines in `ops/` **−33** &ensp;·&ensp; 37.1% of branches taken **−0.1pp** |
| | <sub>coverage compared against the 2026-09-16 run; no figure means it held</sub> |

## ❌ Benchmark Failures

| Test | Error |
|:-----|:------|
| test_gqa_prefill_paged_with_kv_cache_fwd_bench[gqa-prefill-paged-softcap50-b4-prefix4k-chunk512-p64-float16] | TypeError: _fa3_gqa_prefill_paged.<locals>._run() missing 1 required positional argument: 'max_q' |

## 🎉 Performance Improvements (vs 14-day best)

| Op | Config | Prev Best (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **FusedTopKOp** | test_fused_topk_bench[kimi-k2-t32-bfloat16] | 0.0064 | 0.0033 | -49.3% | 0.07 |
| **FusedTopKOp** | test_fused_topk_bench[qwen3-235b-t32-bfloat16] | 0.0040 | 0.0029 | -26.2% | 0.03 |

## 🔵 Moved Since Previous Run

> Moves against the most recent reading. A row restored to its old level appears only here: returning is not a new 14-day record.

| Op | Config | Previous (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **FusedTopKOp** | test_fused_topk_bench[kimi-k2-t32-bfloat16] | 0.0064 | 0.0033 | -49.3% | 0.07 |
| **FusedTopKOp** | test_fused_topk_bench[qwen3-235b-t32-bfloat16] | 0.0040 | 0.0029 | -26.2% | 0.03 |
| **TopkSelectorFwdOp** | test_topk_selector_bench[topk2048-s32k-kv64k-float32] | 11.2452 | 12.8081 | +13.9% | 0.17 |

## ⚠️ Roofline Model Anomalies

> A FAIL row implies a rate above the hardware's theoretical ceiling: its (flops, bytes) formula or declared roof is wrong, and its SOL reading cannot be trusted. A WARN row exceeds the calibrated ceiling; recheck the formula or the calibration.

| Level | Op | Config | Signal |
|:------|:---|:-------|:-------|
| FAIL | **IndexedExpertMLPFwdOp** | test_indexed_expert_mlp_bench[deepseek-v3-decode-1-float16] | bytes/s over HBM theoretical |
| FAIL | **IndexedExpertMLPFwdOp** | test_indexed_expert_mlp_bench[deepseek-v3-decode-1-bfloat16] | bytes/s over HBM theoretical |
| FAIL | **IndexedExpertMLPFwdOp** | test_indexed_expert_mlp_bench[deepseek-v3-decode-32-float16] | bytes/s over HBM theoretical |
| FAIL | **IndexedExpertMLPFwdOp** | test_indexed_expert_mlp_bench[deepseek-v3-decode-32-bfloat16] | bytes/s over HBM theoretical |
| FAIL | **IndexedExpertMLPFwdOp** | test_indexed_expert_mlp_bench[deepseek-v3-decode-64-float16] | bytes/s over HBM theoretical |
| FAIL | **IndexedExpertMLPFwdOp** | test_indexed_expert_mlp_bench[deepseek-v3-decode-64-bfloat16] | bytes/s over HBM theoretical |
| FAIL | **IndexedExpertMLPFwdOp** | test_indexed_expert_mlp_bench[qwen3-235b-decode-32-float16] | bytes/s over HBM theoretical |
| FAIL | **IndexedExpertMLPFwdOp** | test_indexed_expert_mlp_bench[qwen3-235b-decode-32-bfloat16] | bytes/s over HBM theoretical |
| WARN | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-attn-proj-float16] | 107% of the calibrated ceiling |
| WARN | **GemmFwdOp** | test_gemm_bench[k-dominant-7168x16384-bfloat16] | 108% of the calibrated ceiling |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 80%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-bfloat16] | 0.4563 | 0.1428 | 31.3% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-bfloat16] | 0.4536 | 0.1423 | 31.4% | fa3 |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b4-dmem1024-d512-float16] | 0.0824 | 0.0261 | 31.7% | torch-compile |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-b64-complex64] | 0.0152 | 0.0056 | 37.0% | torch-cufft |
| 🔴 | **BmmFp8FwdOp** | test_bmm_fp8_kn_bench[mha-decode-b32-pv-per-tensor-float8_e4m3fn] | 0.0646 | 0.0249 | 38.5% | flashinfer-bmm-fp8 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-short-bfloat16] | 0.4083 | 0.1593 | 39.0% | fa3 |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b1-dmem512-d256-float16] | 0.0330 | 0.0132 | 39.9% | torch-compile |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-short-bfloat16] | 0.4142 | 0.1657 | 40.0% | fa3 |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c128-b64-complex128] | 0.0205 | 0.0085 | 41.3% | torch-cufft |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-bfloat16] | 1.3098 | 0.5466 | 41.7% | fa3 |

<details>
<summary><strong>56 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **BmmFp8FwdOp** | test_bmm_fp8_kn_bench[mha-decode-b64-qk-per-tensor-float8_e4m3fn] | 0.1152 | 0.0496 | 43.0% | flashinfer-bmm-fp8 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-bfloat16] | 1.2428 | 0.5899 | 47.5% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-q-lt-kv-bfloat16] | 0.1132 | 0.0537 | 47.5% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-q-lt-kv-float16] | 0.1128 | 0.0545 | 48.3% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p256-float16] | 0.1654 | 0.0812 | 49.1% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-405b-p256-float16] | 0.0536 | 0.0266 | 49.6% | fa3 |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-small-bfloat16] | 0.0394 | 0.0196 | 49.6% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-bfloat16] | 1.1023 | 0.5492 | 49.8% | fa3 |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-2p7b-b2-s32k-dt-bias-float16] | 0.0444 | 0.0223 | 50.2% | mamba |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-70b-q-lt-kv-bfloat16] | 0.1973 | 0.0993 | 50.3% | fa3 |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-70b-q-lt-kv-float16] | 0.1972 | 0.1000 | 50.7% | fa3 |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-dt-bias-bfloat16] | 0.0124 | 0.0064 | 51.5% | mamba |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-1p3b-b8-s2k-bfloat16] | 0.0121 | 0.0064 | 53.0% | mamba |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-70b-p256-float16] | 0.0670 | 0.0369 | 55.1% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 1.0183 | 0.5778 | 56.7% | fa3 |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-medium-bfloat16] | 0.0544 | 0.0313 | 57.6% | torch-compile |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-short-float16] | 0.2444 | 0.1431 | 58.5% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-short-float16] | 0.2432 | 0.1424 | 58.6% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[throughput-8b-p64-float16] | 0.2488 | 0.1506 | 60.5% | flashinfer |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-8b-long-float16] | 0.9001 | 0.5521 | 61.3% | fa3 |
| 🔴 | **MultiHeadAttentionBwdOp** | test_mha_bwd_bench[llama-70b-long-float16] | 0.8903 | 0.5543 | 62.3% | fa3 |
| 🔴 | **EngramDecodeFwdOp** | test_engram_decode_bench[decode-b8-dmem512-d256-bfloat16] | 0.0334 | 0.0213 | 63.7% | torch-compile |
| 🔴 | **FFTC2CFwdOp** | test_fft_bench[fft-4k-c64-unbatched-complex64] | 0.0081 | 0.0054 | 66.9% | torch-cufft |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-bfloat16] | 0.0971 | 0.0658 | 67.8% | fla |
| 🔴 | **BmmFp8FwdOp** | test_bmm_fp8_kn_bench[moe-prefill-b128-per-tensor-float8_e4m3fn] | 0.9007 | 0.6241 | 69.3% | flashinfer-bmm-fp8 |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-long-k-pressure-float16] | 0.2033 | 0.1412 | 69.4% | marlin-fp16 |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-non-power2-low-cta-float16] | 0.0579 | 0.0407 | 70.3% | marlin-fp32 |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s2k-h4-d64-float16] | 0.0987 | 0.0702 | 71.2% | fla |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-8b-long-float16] | 0.8316 | 0.5928 | 71.3% | fa3 |
| 🔴 | **GroupedQueryAttentionBwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.8087 | 0.5809 | 71.8% | fa3 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-softcap50-float16] | 0.1740 | 0.1252 | 72.0% | flashinfer |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-bfloat16] | 0.0568 | 0.0410 | 72.2% | flashinfer |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-short-w256-float16] | 0.0570 | 0.0413 | 72.5% | flashinfer |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-2k-bfloat16] | 0.2825 | 0.2058 | 72.9% | torch-cublas |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b4-4k-bfloat16] | 1.0532 | 0.7713 | 73.2% | torch-cublas |
| 🔴 | **BmmFwdOp** | test_bmm_bench[moe-prefill-b128-bfloat16] | 0.2940 | 0.2156 | 73.3% | torch-cublas |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-uniform-bfloat16] | 0.0608 | 0.0449 | 73.8% | fa3 |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-2k-float16] | 0.2826 | 0.2087 | 73.8% | torch-cublas |
| 🔴 | **GroupedQueryAttentionPrefillVarlenFwdOp** | test_gqa_prefill_varlen_fwd_bench[llama-8b-uniform-float16] | 0.0607 | 0.0449 | 73.9% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-bfloat16] | 0.0932 | 0.0692 | 74.2% | flashinfer |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-short-w256-float16] | 0.0930 | 0.0691 | 74.3% | flashinfer |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-float16] | 0.6182 | 0.4643 | 75.1% | fla |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-l2-resident-ish-float16] | 0.0287 | 0.0217 | 75.4% | marlin-fp32 |
| 🔴 | **GroupedQueryAttentionDecodePagedWithKVCacheFwdOp** | test_gqa_decode_paged_bench[serving-8b-p64-float16] | 0.1655 | 0.1252 | 75.6% | flashinfer |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-bfloat16] | 0.3114 | 0.2359 | 75.7% | fla |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-1k-bfloat16] | 0.0407 | 0.0309 | 76.0% | torch-cublas |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-b8-1k-float16] | 0.0407 | 0.0311 | 76.5% | torch-cublas |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-bfloat16] | 0.6683 | 0.5164 | 77.3% | flashinfer |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-bfloat16] | 0.3498 | 0.2708 | 77.4% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-8b-long-w1024-float16] | 0.3520 | 0.2729 | 77.5% | fa3 |
| 🔴 | **GroupedQueryAttentionSlidingWindowVarlenFwdOp** | test_gqa_sliding_window_varlen_fwd_bench[llama-70b-long-w1024-float16] | 0.6677 | 0.5195 | 77.8% | flashinfer |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-init-b2-s16k-h4-d64-bfloat16] | 0.6115 | 0.4762 | 77.9% | fla |
| 🔴 | **DaCumsumFwdOp** | test_da_cumsum_fwd_bench[mamba2-780m-b1-s4k-float16] | 0.0043 | 0.0033 | 78.2% | mamba |
| 🔴 | **GemmW4A16FwdOp** | test_gemm_w4a16_bench[decode-hbm-streaming-threshold-float16] | 0.0484 | 0.0380 | 78.7% | marlin-fp32 |
| 🔴 | **GLAFwdOp** | test_gla_fwd_bench[gla-noinit-b2-s8k-h4-d64-float16] | 0.3128 | 0.2477 | 79.2% | fla |
| 🔴 | **MHCPreFwdOp** | test_mhc_pre_bench[pre-large-bfloat16] | 0.0715 | 0.0569 | 79.5% | torch-compile |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 26 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 788 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 2599 lines in `ops/`, 37.1% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 3666 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

### Never-built kernels

| File | Executed |
| --- | --- |
| `kernels/linear_attention/gated_deltanet/compute_w_u_bwd.py` | 0.0% |
| `kernels/linear_attention/gated_deltanet/prefill/cp_fwd.py` | 0.0% |
| `kernels/linear_attention/gated_deltanet/prefill/fused_fwd.py` | 0.0% |
| `kernels/linear_attention/gated_deltanet/prefill/gemm_lowering.py` | 0.0% |
| `kernels/linear_attention/gated_deltanet/prefill/prepare_h.py` | 0.0% |
| `kernels/linear_attention/gated_deltanet/prefill/utils.py` | 0.0% |
| `kernels/attention/deepseek_mla_decode.py` | 5.3% |
| `kernels/linear_attention/gated_deltanet/gated_deltanet_prefill.py` | 5.6% |
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
| `kernels/linear_attention/gated_deltanet/gated_deltanet_fwd.py` | 21.9% |

<details>
<summary>Untested pure Python, worst 15 files</summary>

| File | Uncovered | Executed |
| --- | --- | --- |
| `perf/formulas.py` | 746 | 11.8% |
| `ops/attention/gqa.py` | 647 | 26.1% |
| `ops/pool.py` | 150 | 76.7% |
| `ops/op_base.py` | 117 | 58.9% |
| `ops/convolution.py` | 111 | 73.0% |
| `ops/reduction/reduce.py` | 100 | 58.3% |
| `ops/moe/staged.py` | 96 | 68.3% |
| `ops/mamba/mamba2_fwd.py` | 86 | 20.4% |
| `ops/_roofline_codegen.py` | 84 | 68.1% |
| `ops/elementwise/_base.py` | 84 | 74.2% |
| `ops/rope.py` | 83 | 69.1% |
| `ops/linear_attention/gated_deltanet.py` | 80 | 18.4% |
| `ops/linear_attention/deltanet.py` | 71 | 64.0% |
| `trace/ui.py` | 62 | 24.4% |
| `ops/moe/routed_expert/indexed_routed_expert.py` | 61 | 33.0% |

</details>

Per-line detail is in the `htmlcov/` directory of this run's `tileops_op_test` artifact.
