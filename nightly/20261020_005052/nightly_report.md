# ✅ TileOPs Nightly Report

> **2026-10-19 21:39** &ensp;|&ensp; `4478dd4d` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Operators** | 205 |
| **Kernels** | 337 |
| **Specs** | 0 |
| **Workloads** | 1487 |
| **Correctness** | ✅ &ensp; (205/205 ops verified, 1322/1363 tests) |
| **Benchmarked Ops** | 205 |
| **Benchmark Failures** | ✅ None &ensp;|&ensp; ⚠️ 1 skipped |
| **Regressions** (vs 14-day median) | ✅ None |
| **Baseline Alerts** (< 99%) | ⚠️ 200 |
| **vs Baseline** | ↑ 1988 &ensp;·&ensp; ↓ 200 &ensp;/&ensp; 2188 rows |
| **Rows no reference checked** | ⚠️ 201 |
| **History window** | 13 runs, 2026-10-05 to 2026-10-18 |
| **Roofline anomalies** | ⚠️ 2 |
| **Improvements** (vs 14-day best) | 🎉 17 |
| **New ops** (no 14-day history) | 🆕 6 ops · 69 rows |
| **Moved since previous run** | 🔵 17 |
| **Never-built kernels** | ⚠️ 47 files **+3** &ensp;·&ensp; `kernels/linear_attention/gdn/prefill_forward.py` at 3.4% |
| **Untested roofline math** | 445 lines in `perf/` &ensp;·&ensp; `perf/formulas.py` at 16.2% |
| **Untested op logic** | 812 lines in `ops/` **+2** &ensp;·&ensp; 60.8% of branches taken |
| | <sub>coverage compared against the 2026-10-18 run; no figure means it held</sub> |

## 🎉 Performance Improvements (vs 14-day best)

| Op | Config | Prev Best (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **GLAChunkBwdOp** | test_gla_bwd_bench[train-16k-float16] | 1.4353 | 0.2374 | -83.5% | 30.49 |
| **GLAChunkBwdOp** | test_gla_bwd_bench[train-16k-bfloat16] | 1.3498 | 0.2412 | -82.1% | 30.02 |
| **GLAChunkBwdOp** | test_gla_bwd_bench[train-8k-float16] | 0.6949 | 0.1249 | -82.0% | 28.97 |
| **GLAChunkBwdOp** | test_gla_bwd_bench[train-4k-float16] | 0.3472 | 0.0638 | -81.6% | 28.35 |
| **GLAChunkBwdOp** | test_gla_bwd_bench[train-8k-bfloat16] | 0.6713 | 0.1251 | -81.4% | 28.93 |
| **GLAChunkBwdOp** | test_gla_bwd_bench[train-4k-bfloat16] | 0.3407 | 0.0637 | -81.3% | 28.41 |
| **GLAChunkBwdOp** | test_gla_bwd_bench[train-2k-bfloat16] | 0.1726 | 0.0344 | -80.1% | 26.31 |
| **GLAChunkBwdOp** | test_gla_bwd_bench[train-2k-float16] | 0.1716 | 0.0342 | -80.1% | 26.44 |
| **DeltaNetChunkFwdOp** | test_deltanet_vs_fla_fwd[train-4k-float16] | 0.1087 | 0.0671 | -38.3% | 22.89 |
| **DeltaNetChunkFwdOp** | test_deltanet_vs_fla_fwd[train-4k-bfloat16] | 0.1093 | 0.0676 | -38.2% | 22.73 |
| **DeltaNetChunkFwdOp** | test_deltanet_vs_fla_fwd[train-2k-float16] | 0.0624 | 0.0399 | -36.0% | 19.26 |
| **DeltaNetChunkFwdOp** | test_deltanet_vs_fla_fwd[train-2k-bfloat16] | 0.0628 | 0.0402 | -36.0% | 19.12 |
| **DeltaNetChunkFwdOp** | test_deltanet_vs_fla_fwd[train-16k-bfloat16] | 0.4189 | 0.2755 | -34.2% | 22.31 |
| **DeltaNetChunkFwdOp** | test_deltanet_vs_fla_fwd[train-16k-float16] | 0.4157 | 0.2739 | -34.1% | 22.44 |
| **DeltaNetChunkFwdOp** | test_deltanet_vs_fla_fwd[train-8k-float16] | 0.2151 | 0.1423 | -33.8% | 21.59 |
| **DeltaNetChunkFwdOp** | test_deltanet_vs_fla_fwd[train-8k-bfloat16] | 0.2164 | 0.1433 | -33.8% | 21.45 |
| **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[gpt-oss-sink-decode-bfloat16-bfloat16] | 0.0281 | 0.0240 | -14.7% | 11.40 |

## 🆕 New Ops (no 14-day history)

| Op | Config | Current (ms) | TFLOPS |
|:---|:-------|-----------:|-------:|
| **FusedQKNormRoPEFwdOp** | test_fused_qk_norm_rope_bench[qwen3-8b-t64-bfloat16-bfloat16] | 0.0024 | 0.97 |
| **FusedQKNormRoPEFwdOp** | test_fused_qk_norm_rope_bench[qwen3-8b-t64-float16-float32] | 0.0023 | 0.98 |
| **FusedQKNormRoPEFwdOp** | test_fused_qk_norm_rope_bench[qwen3-8b-t8192-bfloat16-bfloat16] | 0.0460 | 6.38 |
| **FusedQKNormRoPEFwdOp** | test_fused_qk_norm_rope_bench[qwen3-235b-t4096-bfloat16-bfloat16] | 0.0422 | 5.91 |
| **FusedQKNormRoPEFwdOp** | test_fused_qk_norm_rope_bench[glm-4.5-partial-rope-bfloat16-float32] | 0.0666 | 4.50 |
| **FusedQKNormRoPEFwdOp** | test_fused_qk_norm_rope_bench[interleaved-ragged-float16-float16] | 0.0104 | 5.32 |
| **FusedQKNormRoPEFwdOp** | test_fused_qk_norm_rope_bench[interleaved-ragged-bfloat16-float32] | 0.0112 | 4.96 |
| **GemmINT8W8A8FwdOp** | test_gemm_int8_w8a8_bench[llama3-8b-qkv-b1-bfloat16] | 0.0109 | 4.61 |
| **GemmINT8W8A8FwdOp** | test_gemm_int8_w8a8_bench[llama3-8b-qkv-b64-bfloat16] | 0.0109 | 295.27 |
| **GemmINT8W8A8FwdOp** | test_gemm_int8_w8a8_bench[llama3-8b-decode-qkv-bfloat16] | 0.0125 | 515.03 |
| **GemmINT8W8A8FwdOp** | test_gemm_int8_w8a8_bench[llama3-8b-prefill-qkv-bfloat16] | 0.1539 | 1340.26 |
| **GemmINT8W8A8FwdOp** | test_gemm_int8_w8a8_bench[llama3-8b-down-b1-bfloat16] | 0.0218 | 5.39 |
| **GemmINT8W8A8FwdOp** | test_gemm_int8_w8a8_bench[llama3-8b-down-b64-bfloat16] | 0.0221 | 339.45 |
| **GemmINT8W8A8FwdOp** | test_gemm_int8_w8a8_bench[llama3-8b-decode-down-bfloat16] | 0.0237 | 634.44 |
| **GemmINT8W8A8FwdOp** | test_gemm_int8_w8a8_bench[llama3-8b-prefill-down-bfloat16] | 0.3348 | 1436.82 |
| **GemmINT8W8A8FwdOp** | test_gemm_int8_w8a8_bench[llama3-8b-gate-up-b64-bfloat16] | 0.0389 | 386.73 |
| **GemmINT8W8A8FwdOp** | test_gemm_int8_w8a8_bench[llama3-8b-prefill-gateup-bfloat16] | 0.6341 | 1517.49 |
| **GemmINT8W8A8FwdOp** | test_gemm_int8_w8a8_bench[llama3-70b-qkv-b1-bfloat16] | 0.0301 | 5.57 |
| **GemmINT8W8A8FwdOp** | test_gemm_int8_w8a8_bench[llama3-70b-qkv-b64-bfloat16] | 0.0297 | 361.22 |
| **GemmINT8W8A8FwdOp** | test_gemm_int8_w8a8_bench[llama3-70b-dec-qkv-tsr-bfloat16] | 0.0313 | 685.57 |
| **GemmINT8W8A8FwdOp** | test_gemm_int8_w8a8_bench[llama3-70b-prefill-qkv-bfloat16] | 0.4684 | 1467.14 |
| **GemmINT8W8A8FwdOp** | test_gemm_int8_w8a8_bench[llama3-70b-down-b1-bfloat16] | 0.0637 | 7.37 |
| **GemmINT8W8A8FwdOp** | test_gemm_int8_w8a8_bench[llama3-70b-down-b64-bfloat16] | 0.0643 | 467.55 |
| **GemmINT8W8A8FwdOp** | test_gemm_int8_w8a8_bench[llama3-70b-prefill-down-bfloat16] | 1.2585 | 1528.98 |
| **GemmINT8W8A8FwdOp** | test_gemm_int8_w8a8_bench[qwen2.5-7b-qkv-b1-bfloat16] | 0.0081 | 4.09 |
| **GemmINT8W8A8FwdOp** | test_gemm_int8_w8a8_bench[qwen2.5-7b-qkv-b64-bfloat16] | 0.0084 | 251.28 |
| **GemmINT8W8A8FwdOp** | test_gemm_int8_w8a8_bench[qwen2.5-7b-prefill-qkv-bfloat16] | 0.1043 | 1297.23 |
| **GemmINT8W8A8FwdOp** | test_gemm_int8_w8a8_bench[qwen2.5-7b-down-b1-bfloat16] | 0.0253 | 5.37 |
| **GemmINT8W8A8FwdOp** | test_gemm_int8_w8a8_bench[qwen2.5-7b-down-b64-bfloat16] | 0.0256 | 339.91 |
| **GemmINT8W8A8FwdOp** | test_gemm_int8_w8a8_bench[qwen2.5-7b-prefill-down-bfloat16] | 0.3842 | 1447.78 |
| **GemmINT8W8A8FwdOp** | test_gemm_int8_w8a8_bench[qwen2.5-72b-down-b1-bfloat16] | 0.0654 | 7.40 |
| **GemmINT8W8A8FwdOp** | test_gemm_int8_w8a8_bench[qwen2.5-72b-down-b64-bfloat16] | 0.0661 | 468.98 |
| **GemmINT8W8A8FwdOp** | test_gemm_int8_w8a8_bench[qwen2.5-72b-prefill-down-bfloat16] | 1.3063 | 1519.03 |
| **GemmINT8W8A8FwdOp** | test_gemm_int8_w8a8_bench[llama3-8b-qkv-static-a-bfloat16] | 0.0110 | 292.70 |
| **GemmINT8W8A8FwdOp** | test_gemm_int8_w8a8_bench[llama3-8b-qkv-tensor-w-bfloat16] | 0.0109 | 295.72 |
| **GemmINT8W8A8FwdOp** | test_gemm_int8_w8a8_bench[llama3-8b-down-b64-float16] | 0.0222 | 338.95 |
| **SelectiveScanFwdOp** | test_selective_scan_bench[mamba-2.8b-prefill-bfloat16] | 0.3045 | 7.44 |
| **SelectiveScanFwdOp** | test_selective_scan_bench[mamba-2.8b-prefill-float16] | 0.2969 | 7.63 |
| **SelectiveScanFwdOp** | test_selective_scan_bench[mamba-2.8b-decode-bfloat16] | 0.0021 | 0.26 |
| **SelectiveScanFwdOp** | test_selective_scan_bench[mamba-2.8b-decode-b64-bfloat16] | 0.0160 | 2.22 |
| **SelectiveScanFwdOp** | test_selective_scan_bench[mamba-1.4b-prefill-bfloat16] | 0.2365 | 7.66 |
| **SelectiveScanFwdOp** | test_selective_scan_bench[mamba-130m-no-gate-float32] | 0.2333 | 2.78 |
| **SelectiveScanFwdOp** | test_selective_scan_bench[mamba-2.8b-packed-bfloat16] | 0.3503 | 6.47 |
| **SelectiveScanFwdOp** | test_selective_scan_bench[grouped-state-bfloat16] | 1.6450 | 8.32 |
| **SelectiveScanFwdOp** | test_selective_scan_bench[bare-scan-bfloat16] | 0.1181 | 7.46 |
| **MLAPagedFwdOp** | test_mla_paged_bench[ds-v3-4k-bfloat16-bfloat16] | 0.1463 | 500.18 |
| **MLAPagedFwdOp** | test_mla_paged_bench[ds-v3-4k-float16-float16] | 0.1480 | 494.34 |
| **MLAPagedFwdOp** | test_mla_paged_bench[ds-v3-32k-bfloat16-bfloat16] | 0.9809 | 596.86 |
| **MLAPagedFwdOp** | test_mla_paged_bench[ds-v3-mtp-bfloat16-bfloat16] | 0.2564 | 570.82 |
| **MLAPagedFwdOp** | test_mla_paged_bench[kimi-k2-fp8-bfloat16-float8_e4m3fn] | 1.3288 | 220.30 |
| **MLAPagedFwdOp** | test_mla_paged_bench[ds-v3-ragged-bfloat16-bfloat16] | 0.0245 | 123.83 |
| **MLAKVCacheWriteFwdOp** | test_mla_kv_cache_write_bench[ds-v3-decode-bfloat16-bfloat16] | 0.0016 | - |
| **MLAKVCacheWriteFwdOp** | test_mla_kv_cache_write_bench[ds-v3-prefill-bfloat16-bfloat16] | 0.0123 | - |
| **MLAKVCacheWriteFwdOp** | test_mla_kv_cache_write_bench[ds-v3-prefill-float16-float16] | 0.0123 | - |
| **MLAKVCacheWriteFwdOp** | test_mla_kv_cache_write_bench[ds-v3-fp8-rope-bfloat16-float8_e4m3fn-float32] | 0.0059 | 0.94 |
| **MLAKVCacheWriteFwdOp** | test_mla_kv_cache_write_bench[kimi-k2-rope-bfloat16-bfloat16-bfloat16] | 0.0026 | 0.01 |
| **MLAKVCacheWriteFwdOp** | test_mla_kv_cache_write_bench[odd-tokens-neox-fp8-float16-float8_e4m3fn-float16] | 0.0029 | 0.00 |
| **FusedAddRMSNormPerTokenQuantFwdOp** | test_fused_add_rms_norm_per_token_quant_bench[llama-8b-prefill-bfloat16-float8_e4m3fn] | 0.0340 | 4.45 |
| **FusedAddRMSNormPerTokenQuantFwdOp** | test_fused_add_rms_norm_per_token_quant_bench[llama-8b-prefill-i8-bfloat16-int8] | 0.0337 | 4.97 |
| **FusedAddRMSNormPerTokenQuantFwdOp** | test_fused_add_rms_norm_per_token_quant_bench[llama-8b-decode-b1-bfloat16-float8_e4m3fn] | 0.0030 | 0.01 |
| **FusedAddRMSNormPerTokenQuantFwdOp** | test_fused_add_rms_norm_per_token_quant_bench[llama-8b-decode-b64-bfloat16-float8_e4m3fn] | 0.0034 | 0.70 |
| **FusedAddRMSNormPerTokenQuantFwdOp** | test_fused_add_rms_norm_per_token_quant_bench[llama-8b-decode-b256-bfloat16-float8_e4m3fn] | 0.0052 | 1.80 |
| **FusedAddRMSNormPerTokenQuantFwdOp** | test_fused_add_rms_norm_per_token_quant_bench[llama-70b-prefill-bfloat16-float8_e4m3fn] | 0.0710 | 4.26 |
| **FusedAddRMSNormPerTokenQuantFwdOp** | test_fused_add_rms_norm_per_token_quant_bench[llama-70b-prefill-i8-float16-int8] | 0.0687 | 4.89 |
| **FusedAddRMSNormPerTokenQuantFwdOp** | test_fused_add_rms_norm_per_token_quant_bench[llama-70b-decode-b1-bfloat16-float8_e4m3fn] | 0.0036 | 0.02 |
| **FusedAddRMSNormPerTokenQuantFwdOp** | test_fused_add_rms_norm_per_token_quant_bench[llama-70b-decode-b64-bfloat16-float8_e4m3fn] | 0.0045 | 1.05 |
| **FusedAddRMSNormPerTokenQuantFwdOp** | test_fused_add_rms_norm_per_token_quant_bench[llama-70b-decode-b256-bfloat16-float8_e4m3fn] | 0.0076 | 2.48 |
| **FusedAddRMSNormPerTokenQuantFwdOp** | test_fused_add_rms_norm_per_token_quant_bench[clamped-amax-bfloat16-float8_e4m3fn] | 0.0339 | 4.45 |
| **FusedAddRMSNormPerTokenQuantFwdOp** | test_fused_add_rms_norm_per_token_quant_bench[llama-13b-prefill-bfloat16-float8_e4m3fn] | 0.0245 | 3.86 |

## 🔵 Moved Since Previous Run

> Moves against the most recent reading. A row restored to its old level appears only here: returning is not a new 14-day record.

| Op | Config | Previous (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **GLAChunkBwdOp** | test_gla_bwd_bench[train-16k-float16] | 1.4432 | 0.2374 | -83.5% | 30.49 |
| **GLAChunkBwdOp** | test_gla_bwd_bench[train-16k-bfloat16] | 1.3637 | 0.2412 | -82.3% | 30.02 |
| **GLAChunkBwdOp** | test_gla_bwd_bench[train-8k-float16] | 0.7008 | 0.1249 | -82.2% | 28.97 |
| **GLAChunkBwdOp** | test_gla_bwd_bench[train-4k-float16] | 0.3504 | 0.0638 | -81.8% | 28.35 |
| **GLAChunkBwdOp** | test_gla_bwd_bench[train-8k-bfloat16] | 0.6858 | 0.1251 | -81.8% | 28.93 |
| **GLAChunkBwdOp** | test_gla_bwd_bench[train-4k-bfloat16] | 0.3455 | 0.0637 | -81.6% | 28.41 |
| **GLAChunkBwdOp** | test_gla_bwd_bench[train-2k-bfloat16] | 0.1736 | 0.0344 | -80.2% | 26.31 |
| **GLAChunkBwdOp** | test_gla_bwd_bench[train-2k-float16] | 0.1725 | 0.0342 | -80.2% | 26.44 |
| **DeltaNetChunkFwdOp** | test_deltanet_vs_fla_fwd[train-4k-float16] | 0.1092 | 0.0671 | -38.5% | 22.89 |
| **DeltaNetChunkFwdOp** | test_deltanet_vs_fla_fwd[train-4k-bfloat16] | 0.1098 | 0.0676 | -38.4% | 22.73 |
| **DeltaNetChunkFwdOp** | test_deltanet_vs_fla_fwd[train-2k-bfloat16] | 0.0630 | 0.0402 | -36.2% | 19.12 |
| **DeltaNetChunkFwdOp** | test_deltanet_vs_fla_fwd[train-2k-float16] | 0.0625 | 0.0399 | -36.1% | 19.26 |
| **DeltaNetChunkFwdOp** | test_deltanet_vs_fla_fwd[train-16k-bfloat16] | 0.4194 | 0.2755 | -34.3% | 22.31 |
| **DeltaNetChunkFwdOp** | test_deltanet_vs_fla_fwd[train-16k-float16] | 0.4158 | 0.2739 | -34.1% | 22.44 |
| **DeltaNetChunkFwdOp** | test_deltanet_vs_fla_fwd[train-8k-float16] | 0.2153 | 0.1423 | -33.9% | 21.59 |
| **DeltaNetChunkFwdOp** | test_deltanet_vs_fla_fwd[train-8k-bfloat16] | 0.2166 | 0.1433 | -33.8% | 21.45 |
| **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[gpt-oss-sink-decode-bfloat16-bfloat16] | 0.0281 | 0.0240 | -14.7% | 11.40 |

## ⚠️ Roofline Model Anomalies

> A FAIL row implies a rate above the hardware's theoretical ceiling: its (flops, bytes) formula or declared roof is wrong, and its SOL reading cannot be trusted. A WARN row exceeds the calibrated ceiling; recheck the formula or the calibration.

| Level | Op | Config | Signal |
|:------|:---|:-------|:-------|
| WARN | **GemmW4A8FwdOp** | test_gemm_w4a8_bench[ds-r1-down-4k] | 105% of the calibrated ceiling |
| WARN | **GemmW4A8FwdOp** | test_gemm_w4a8_bench[llama-70b-down-4k] | 108% of the calibrated ceiling |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 99%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-32k-bfloat16] | 0.3927 | 0.0873 | 22.2% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[ds-v32-decode-b1-float8_e4m3fn] | 0.2891 | 0.0658 | 22.8% | torch-ref |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-mixed-float16] | 22.6866 | 5.1936 | 22.9% | fa3 |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-rope-float16] | 42.4312 | 14.0810 | 33.2% | fa3 |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-32k-bfloat16] | 0.3917 | 0.1590 | 40.6% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-32k-float16] | 0.3916 | 0.1604 | 41.0% | flashinfer |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-rope-float16] | 1.6741 | 0.6887 | 41.1% | fa3 |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-single-request-float16] | 0.0552 | 0.0227 | 41.1% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-single-request-bfloat16] | 0.0553 | 0.0229 | 41.4% | flashinfer |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-float16-float8_e4m3fn] | 56.2387 | 23.4099 | 41.6% | fa3 |

<details>
<summary><strong>190 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b1-bfloat16] | 0.0551 | 0.0234 | 42.4% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b1-float16] | 0.0551 | 0.0234 | 42.4% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b2-float16] | 0.0558 | 0.0238 | 42.7% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b2-bfloat16] | 0.0557 | 0.0239 | 42.9% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b6-float16] | 0.0610 | 0.0268 | 43.9% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b6-bfloat16] | 0.0609 | 0.0269 | 44.2% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx131072-float8_e4m3fn] | 17.3822 | 8.9894 | 51.7% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx131072-float8_e4m3fn] | 8.7605 | 4.5541 | 52.0% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx65536-float8_e4m3fn] | 8.5751 | 4.4646 | 52.1% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx65536-float8_e4m3fn] | 4.3513 | 2.2853 | 52.5% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx32768-float8_e4m3fn] | 4.1538 | 2.2010 | 53.0% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx32768-float8_e4m3fn] | 2.1445 | 1.1492 | 53.6% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx16384-float8_e4m3fn] | 1.9368 | 1.0499 | 54.2% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx16384-float8_e4m3fn] | 1.0439 | 0.5726 | 54.9% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx8192-float8_e4m3fn] | 0.8658 | 0.4782 | 55.2% | deepgemm |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[gemma-2b-bfloat16] | 0.3033 | 0.1683 | 55.5% | fa3 |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx8192-float8_e4m3fn] | 0.5025 | 0.2808 | 55.9% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx4096-float8_e4m3fn] | 0.2336 | 0.1323 | 56.6% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx4096-float8_e4m3fn] | 0.3264 | 0.1911 | 58.6% | deepgemm |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[starcoder-float16] | 0.7883 | 0.5053 | 64.1% | fa3 |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[context-chunk-bfloat16] | 0.3199 | 0.2120 | 66.3% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-kscale-float8_e4m3fn] | 0.4715 | 0.3211 | 68.1% | deepgemm |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-32768-float16] | 3.1734 | 2.1665 | 68.3% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-32768-bfloat16] | 3.1691 | 2.1647 | 68.3% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-16384-bfloat16] | 1.5643 | 1.0905 | 69.7% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-16384-float16] | 1.5648 | 1.0943 | 69.9% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-serving-batch-float16] | 0.0889 | 0.0623 | 70.1% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-serving-batch-bfloat16] | 0.0887 | 0.0623 | 70.3% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-8192-bfloat16] | 0.7972 | 0.5601 | 70.3% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-8192-float16] | 0.7974 | 0.5643 | 70.8% | flashinfer |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-float16-float8_e4m3fn] | 1.9767 | 1.4059 | 71.1% | fa3 |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-4096-float16] | 0.4149 | 0.2970 | 71.6% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-4096-bfloat16] | 0.4146 | 0.2974 | 71.7% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-float8_e4m3fn] | 0.5152 | 0.3718 | 72.2% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-bfloat16] | 0.5301 | 0.3840 | 72.4% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x8192-bfloat16] | 0.6185 | 0.4685 | 75.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-16x8192-bfloat16] | 0.6160 | 0.4684 | 76.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x8192-bfloat16] | 0.6205 | 0.4725 | 76.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-16x8192-bfloat16] | 1.2041 | 0.9235 | 76.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-32x8192-bfloat16] | 1.2007 | 0.9227 | 76.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-16x8192-bfloat16] | 1.2081 | 0.9284 | 76.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-32x8192-bfloat16] | 2.3797 | 1.8296 | 76.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-32x8192-bfloat16] | 2.3862 | 1.8347 | 76.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-16x8192-bfloat16] | 2.4024 | 1.8486 | 77.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x8192-bfloat16] | 1.2088 | 0.9313 | 77.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-32x8192-bfloat16] | 4.7608 | 3.6710 | 77.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x8192-bfloat16] | 2.3975 | 1.8491 | 77.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x8192-bfloat16] | 1.2116 | 0.9352 | 77.2% | flashinfer |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[falcon-7b-2k-bfloat16] | 0.0372 | 0.0287 | 77.2% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-16x8192-bfloat16] | 2.3901 | 1.8449 | 77.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x8192-bfloat16] | 1.7902 | 1.3824 | 77.2% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-4k-float16] | 0.1165 | 0.0901 | 77.4% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-4k-bfloat16] | 0.1160 | 0.0898 | 77.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-32x8192-bfloat16] | 9.4467 | 7.3148 | 77.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x8192-bfloat16] | 1.2041 | 0.9324 | 77.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-16x8192-float16] | 0.6004 | 0.4651 | 77.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-32x8192-bfloat16] | 7.0436 | 5.4586 | 77.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-16x8192-bfloat16] | 3.5413 | 2.7457 | 77.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-16x8192-bfloat16] | 4.7320 | 3.6735 | 77.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-32x8192-bfloat16] | 4.7226 | 3.6684 | 77.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-16x8192-bfloat16] | 2.3748 | 1.8469 | 77.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-32x8192-bfloat16] | 4.7031 | 3.6715 | 78.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-16x8192-float16] | 2.3462 | 1.8328 | 78.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-16x8192-float16] | 3.4901 | 2.7349 | 78.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-32x8192-float16] | 6.9247 | 5.4314 | 78.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x8192-float16] | 0.5951 | 0.4674 | 78.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-32x8192-float16] | 1.1658 | 0.9165 | 78.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-16x8192-float16] | 1.1692 | 0.9192 | 78.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x8192-float16] | 2.3333 | 1.8361 | 78.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-16x8192-float16] | 4.6248 | 3.6489 | 78.9% | flashinfer |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 0.5653 | 0.4462 | 78.9% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-32x8192-float16] | 2.3029 | 1.8189 | 79.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x8192-float16] | 1.7387 | 1.3738 | 79.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x8192-float16] | 1.1704 | 0.9253 | 79.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x8192-float16] | 0.5954 | 0.4708 | 79.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-16x8192-float16] | 2.3181 | 1.8339 | 79.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x8192-float16] | 1.1695 | 0.9258 | 79.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-32x8192-float16] | 9.1970 | 7.2815 | 79.2% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b64-bfloat16] | 0.1250 | 0.0989 | 79.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-32x8192-float16] | 4.5985 | 3.6423 | 79.2% | flashinfer |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.5664 | 0.4486 | 79.2% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-16x8192-float16] | 2.3239 | 1.8416 | 79.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-32x8192-float16] | 2.3068 | 1.8287 | 79.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-32x8192-float16] | 4.5970 | 3.6449 | 79.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-32x8192-float16] | 4.5957 | 3.6489 | 79.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4096-4096-bfloat16] | 0.3199 | 0.2541 | 79.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-16x8192-float16] | 1.1666 | 0.9279 | 79.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x8192-float16] | 1.1669 | 0.9302 | 79.7% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b64-float16] | 0.1250 | 0.1000 | 80.1% | flashinfer |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-8b-long-float16] | 0.5706 | 0.4588 | 80.4% | fa3 |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[short-prefill-bfloat16] | 0.0702 | 0.0566 | 80.6% | deepgemm |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-8b-long-bfloat16] | 0.5683 | 0.4583 | 80.7% | fa3 |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[falcon-7b-bfloat16] | 0.3137 | 0.2532 | 80.7% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4096-4096-float16] | 0.3107 | 0.2529 | 81.4% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-4k-bfloat16] | 0.0654 | 0.0533 | 81.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4096-4096-bfloat16] | 0.2979 | 0.2445 | 82.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4096-4096-float16] | 0.2937 | 0.2435 | 82.9% | flashinfer |
| 🔴 | **GQAVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-70b-fp8-q-lt-kv-float8_e4m3fn-bfloat16] | 0.1012 | 0.0857 | 84.7% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4x2048-bfloat16] | 0.3227 | 0.2734 | 84.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-4x2048-bfloat16] | 0.1723 | 0.1464 | 85.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-4x2048-bfloat16] | 0.1680 | 0.1435 | 85.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-4x2048-bfloat16] | 0.1685 | 0.1444 | 85.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4x2048-float16] | 0.3150 | 0.2722 | 86.4% | flashinfer |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[llama-8b-softcap-float16] | 0.1566 | 0.1357 | 86.7% | flashinfer |
| 🔴 | **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[qwen3-fp8-ragged-odd-float8_e4m3fn-float8_e4m3fn-bfloat16] | 0.1842 | 0.1604 | 87.1% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-2048-6144-bfloat16] | 0.4139 | 0.3608 | 87.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4x2048-bfloat16] | 0.3017 | 0.2633 | 87.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-6144-2048-bfloat16] | 0.4123 | 0.3603 | 87.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-4x2048-float16] | 0.1673 | 0.1462 | 87.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-4x2048-float16] | 0.1646 | 0.1441 | 87.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4x2048-float16] | 0.2976 | 0.2625 | 88.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-4x2048-float16] | 0.1620 | 0.1435 | 88.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-2048-6144-float16] | 0.3988 | 0.3587 | 89.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-6144-2048-float16] | 0.3975 | 0.3582 | 90.1% | flashinfer |
| 🔴 | **GQAVarlenFwdOp** | test_gqa_varlen_fwd_bench[qwen3-fp8-ragged-float8_e4m3fn-bfloat16] | 0.1100 | 0.0996 | 90.5% | fa3 |
| 🔴 | **GQAVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-rope-partial-bfloat16] | 0.0518 | 0.0469 | 90.5% | fa3 |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-8b-short-float16] | 0.1505 | 0.1371 | 91.1% | fa3 |
| 🔴 | **GQAVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-rope-partial-float16] | 0.0513 | 0.0468 | 91.3% | fa3 |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-8b-short-bfloat16] | 0.1493 | 0.1368 | 91.6% | fa3 |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-short-float16] | 0.1420 | 0.1312 | 92.4% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x1024-bfloat16] | 0.1804 | 0.1668 | 92.5% | flashinfer |
| 🔴 | **MLAVarlenFwdOp** | test_mla_varlen_fwd_bench[ds-v3-mixed-bfloat16] | 25.7758 | 23.8538 | 92.5% | fa3 |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-short-bfloat16] | 0.1415 | 0.1310 | 92.6% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x1024-bfloat16] | 0.2562 | 0.2376 | 92.7% | flashinfer |
| 🔴 | **SharedExpertMLPFwdOp** | test_shared_expert_mlp_bench[kimi-k2-t512-bfloat16] | 0.5991 | 0.5557 | 92.8% | quack |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x1024-bfloat16] | 0.3332 | 0.3105 | 93.2% | flashinfer |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-8b-long-mha-bfloat16] | 0.4410 | 0.4130 | 93.7% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x1024-bfloat16] | 0.1753 | 0.1644 | 93.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x1024-float16] | 0.2516 | 0.2371 | 94.2% | flashinfer |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-long-mha-bfloat16] | 0.4404 | 0.4150 | 94.2% | fa3 |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[gemma-2b-8k-bs1-float16] | 0.0172 | 0.0162 | 94.2% | flashinfer |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-8b-long-mha-float16] | 0.4413 | 0.4161 | 94.3% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x1024-bfloat16] | 0.1733 | 0.1636 | 94.4% | flashinfer |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[gemma-2b-8k-bs1-bfloat16] | 0.0172 | 0.0163 | 94.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x1024-float16] | 0.1761 | 0.1663 | 94.5% | flashinfer |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-long-mha-float16] | 0.4419 | 0.4179 | 94.6% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x1024-bfloat16] | 0.0932 | 0.0883 | 94.7% | flashinfer |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[llama-8b-32k-float16] | 0.2679 | 0.2540 | 94.8% | flashinfer |
| 🔴 | **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-fp8-prefill-float8_e4m3fn-float8_e4m3fn-bfloat16] | 0.4673 | 0.4435 | 94.9% | fa3 |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[llama-8b-4k-float16] | 0.1426 | 0.1353 | 94.9% | flashinfer |
| 🔴 | **LtFwdOp** | test_lt_bench[linear-bias-float32] | 0.0076 | 0.0072 | 95.2% | torch-compile |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[llama-8b-4k-bfloat16] | 0.1418 | 0.1352 | 95.3% | flashinfer |
| 🔴 | **GQAVarlenFwdOp** | test_gqa_varlen_fwd_bench[qwen-ragged-rope-bfloat16] | 0.1011 | 0.0966 | 95.6% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x1024-float16] | 0.3242 | 0.3100 | 95.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x1024-float16] | 0.0918 | 0.0879 | 95.8% | flashinfer |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[llama-8b-32k-bfloat16] | 0.2649 | 0.2541 | 96.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x1024-float16] | 0.1708 | 0.1640 | 96.0% | flashinfer |
| 🔴 | **GQAVarlenFwdOp** | test_gqa_varlen_fwd_bench[qwen-ragged-rope-float16] | 0.1010 | 0.0971 | 96.2% | fa3 |
| 🔴 | **LtFwdOp** | test_lt_bench[linear-bias-bfloat16] | 0.0048 | 0.0047 | 96.7% | torch-compile |
| 🔴 | **LeFwdOp** | test_le_bench[llama-7b-hidden-float16] | 0.0075 | 0.0072 | 96.8% | torch |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[llama-70b-32k-float16] | 0.1432 | 0.1388 | 96.9% | flashinfer |
| 🔴 | **LogicalAndFwdOp** | test_logical_and_bench[llama-7b-hidden-float16] | 0.0074 | 0.0071 | 97.0% | torch-compile |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x1024-bfloat16] | 0.0896 | 0.0869 | 97.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x1024-float16] | 0.1682 | 0.1633 | 97.1% | flashinfer |
| 🔴 | **NeFwdOp** | test_ne_bench[linear-bias-float16] | 0.0048 | 0.0047 | 97.3% | torch-compile |
| 🔴 | **FusedMoEExpertsFwdOp** | test_moe_experts_bench[ds-v3-prefill-bfloat16] | 7.7071 | 7.5107 | 97.5% | flashinfer-cutlass |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[llama-70b-32k-bfloat16] | 0.1424 | 0.1388 | 97.5% | flashinfer |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-1k-bfloat16] | 0.0304 | 0.0296 | 97.5% | quack |
| 🔴 | **FusedMoEExpertsFwdOp** | test_moe_experts_bench[ds-v3-prefill-float16] | 7.9901 | 7.7882 | 97.5% | flashinfer-cutlass |
| 🔴 | **SumFwdOp** | test_sum_bench[3d-multidim-float16] | 0.0048 | 0.0047 | 97.6% | torch-compile |
| 🔴 | **AdaLayerNormFwdOp** | test_ada_layer_norm_bench[llama-8b-decode-bfloat16] | 0.0027 | 0.0027 | 97.7% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-down-bfloat16] | 0.1739 | 0.1699 | 97.7% | cublaslt-best |
| 🔴 | **MoEGroupedGemmFP8FwdOp** | test_moe_grouped_gemm_fp8_bench[ds-v3-e8-up-masked] | 0.0744 | 0.0727 | 97.7% | deepgemm |
| 🔴 | **MHADecodePagedWithKVCacheFwdOp** | test_mha_decode_paged_bench[opt-1.3b-b16-float16] | 0.0791 | 0.0774 | 97.8% | flashinfer |
| 🔴 | **MHCPostFwdOp** | test_mhc_post_bench[hidden-1280] | 0.0014 | 0.0014 | 97.9% | torch-compile |
| 🔴 | **LtFwdOp** | test_lt_bench[linear-bias-float16] | 0.0048 | 0.0047 | 98.0% | torch-compile |
| 🔴 | **MHCPostFwdOp** | test_mhc_post_bench[hidden-2560] | 0.0017 | 0.0016 | 98.1% | torch-compile |
| 🔴 | **GtFwdOp** | test_gt_bench[linear-bias-float32] | 0.0076 | 0.0075 | 98.1% | torch-compile |
| 🔴 | **MeanFwdOp** | test_mean_bench[mlp-intermediate-float32] | 0.0250 | 0.0245 | 98.1% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-qkv-a-bfloat16] | 0.1813 | 0.1780 | 98.2% | cublaslt-best |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-q-b-bfloat16] | 0.4121 | 0.4048 | 98.2% | cublaslt-best |
| 🔴 | **EqFwdOp** | test_eq_bench[linear-bias-bfloat16] | 0.0047 | 0.0046 | 98.3% | torch-compile |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x1024-float16] | 0.0884 | 0.0869 | 98.3% | flashinfer |
| 🔴 | **LogicalAndFwdOp** | test_logical_and_bench[llama-7b-ffn-bfloat16] | 0.0164 | 0.0161 | 98.4% | torch-compile |
| 🔴 | **SumFwdOp** | test_sum_bench[mlp-intermediate-float32] | 0.0249 | 0.0245 | 98.5% | torch-compile |
| 🔴 | **GeFwdOp** | test_ge_bench[linear-bias-float32] | 0.0076 | 0.0075 | 98.5% | torch-compile |
| 🔴 | **VectorNormFwdOp** | test_vector_norm_bench[l2-mlp-intermediate-float32] | 0.0250 | 0.0247 | 98.5% | torch-compile |
| 🔴 | **MinimumFwdOp** | test_minimum_bench[linear-bias-float32] | 0.0102 | 0.0100 | 98.6% | torch-compile |
| 🔴 | **FusedMoEFwdOp** | test_fused_moe_fwd_bench[gpt-oss-120b-decode-bfloat16] | 1.2622 | 1.2445 | 98.6% | vllm |
| 🔴 | **SharedExpertMLPFwdOp** | test_shared_expert_mlp_bench[ds-v3-t4096-bfloat16] | 0.5125 | 0.5053 | 98.6% | quack |
| 🔴 | **VectorNormFwdOp** | test_vector_norm_bench[l2-3d-multidim-float16] | 0.0048 | 0.0047 | 98.7% | torch-compile |
| 🔴 | **MeanFwdOp** | test_mean_bench[3d-multidim-float16] | 0.0048 | 0.0047 | 98.7% | torch-compile |
| 🔴 | **LogicalOrFwdOp** | test_logical_or_bench[linear-bias-float32] | 0.0074 | 0.0073 | 98.7% | torch-compile |
| 🔴 | **ReciprocalFwdOp** | test_reciprocal_bench[16M-bfloat16] | 0.0183 | 0.0181 | 98.8% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-mlp-up-bfloat16] | 0.3325 | 0.3286 | 98.8% | cublaslt-best |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-o-proj-bfloat16] | 1.2694 | 1.2548 | 98.9% | quack |
| 🔴 | **WhereFwdOp** | test_where_bench[16M-float32] | 0.0534 | 0.0528 | 98.9% | torch-compile |
| 🔴 | **LeakyReluFwdOp** | test_leaky_relu_bench[gan-feat-bfloat16] | 0.0179 | 0.0177 | 98.9% | torch-compile |
| 🔴 | **NeFwdOp** | test_ne_bench[linear-bias-float32] | 0.0076 | 0.0076 | 99.0% | torch-compile |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-32768-bfloat16] | 0.2919 | 0.2889 | 99.0% | flashinfer |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 47 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 445 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 812 lines in `ops/`, 60.8% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 2493 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

### Never-built kernels

| File | Executed |
| --- | --- |
| `kernels/linear_attention/gdn/prefill_forward.py` | 3.4% |
| `kernels/linear_attention/gdn/prefill_prepare.py` | 3.6% |
| `kernels/linear_attention/deltanet/prefill_forward.py` | 4.3% |
| `kernels/linear_attention/kda/fused_program.py` | 4.3% |
| `kernels/linear_attention/kda/chunk_programs.py` | 5.0% |
| `kernels/linear_attention/gdn/prefill_common.py` | 5.3% |
| `kernels/linear_attention/deltanet/prefill_prepare.py` | 5.7% |
| `kernels/sampling/top_k_top_p_mask.py` | 6.5% |
| `kernels/attention/gqa/dense_fp8.py` | 6.6% |
| `kernels/linear_attention/kda/inverse.py` | 6.7% |
| `kernels/attention/gqa/paged_rope_prepare.py` | 6.8% |
| `kernels/attention/gqa/prefill_paged_kv_append.py` | 6.9% |
| `kernels/linear_attention/delta_decode.py` | 7.8% |
| `kernels/attention/gqa/paged_fp8_ws.py` | 8.3% |
| `kernels/attention/gqa/dense.py` | 9.6% |
| `kernels/sampling/top_k_mask.py` | 10.8% |
| `kernels/attention/gqa/paged_ws.py` | 10.9% |
| `kernels/attention/mla/decode.py` | 11.1% |
| `kernels/sampling/sampling_from_probs.py` | 11.8% |
| `kernels/sampling/chain_speculative_sampling.py` | 11.8% |
| `kernels/linear_attention/kda/decode_program.py` | 11.9% |
| `kernels/linear_attention/gla/varlen_prefill.py` | 12.2% |
| `kernels/sampling/top_p_mask.py` | 12.4% |
| `kernels/quantization/int8_quant_per_tensor.py` | 12.9% |
| `kernels/attention/gqa/paged_fp8_decode.py` | 13.0% |
| `kernels/attention/nsa/compressed_varlen.py` | 13.5% |
| `kernels/linear_attention/gla/dense_prefill_partitioned.py` | 14.7% |
| `kernels/linear_attention/gla/dense_prefill_subchunk.py` | 14.9% |
| `kernels/linear_attention/gla/varlen_prefill_partitioned.py` | 15.1% |
| `kernels/linear_attention/chunk_prefill.py` | 15.4% |
| `kernels/quantization/int8_quant_per_channel.py` | 15.5% |
| `kernels/quantization/int8_quant_per_block.py` | 16.0% |
| `kernels/attention/gqa/decode_fp8.py` | 16.9% |
| `kernels/moe/indexed_expert_gemm.py` | 17.0% |
| `kernels/gemm/grouped/general.py` | 17.2% |
| `kernels/attention/dsa/decode.py` | 18.6% |
| `kernels/linear_attention/deltanet/partition_scan.py` | 19.1% |
| `kernels/sampling/min_p_mask.py` | 19.7% |
| `kernels/attention/gqa/sliding_window_varlen.py` | 20.1% |
| `kernels/linear_attention/chunk_plan.py` | 20.5% |
| `kernels/norm/instance_norm.py` | 20.8% |
| `kernels/linear_attention/gla/dense_decode.py` | 21.2% |
| `kernels/moe/moe_grouped_gemm.py` | 21.4% |
| `kernels/quantization/fp8_quant_per_block.py` | 22.4% |
| `kernels/linear_attention/gdn/prefill.py` | 22.6% |
| `kernels/norm/rms_norm_on_chip.py` | 23.1% |
| `kernels/sampling/radix_select.py` | 24.1% |

<details>
<summary>Untested pure Python, worst 15 files</summary>

| File | Uncovered | Executed |
| --- | --- | --- |
| `perf/formulas.py` | 403 | 16.2% |
| `manifest/plan.py` | 363 | 29.7% |
| `manifest/workload.py` | 180 | 61.5% |
| `ops/op_base.py` | 163 | 67.5% |
| `manifest/primitives.py` | 132 | 62.2% |
| `manifest/expr.py` | 122 | 70.7% |
| `manifest/signature.py` | 107 | 77.1% |
| `ops/_signature_codegen.py` | 88 | 89.5% |
| `trace/ui.py` | 62 | 24.4% |
| `backend/registry.py` | 57 | 47.2% |
| `manifest/kinds.py` | 53 | 79.2% |
| `ops/attention/gqa/prefill_paged_kv_append.py` | 53 | 35.4% |
| `backend/dispatch.py` | 48 | 40.0% |
| `perf/profile.py` | 42 | 22.2% |
| `ops/reduction/reduce.py` | 27 | 79.4% |

</details>

Per-line detail is in the `htmlcov/` directory of this run's `tileops_op_test` artifact.
