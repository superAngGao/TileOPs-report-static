# ✅ TileOPs Nightly Report

> **2026-10-13 20:18** &ensp;|&ensp; `a79a21e4` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Operators** | 189 |
| **Kernels** | 306 |
| **Specs** | 16 |
| **Workloads** | 1237 |
| **Correctness** | ✅ &ensp; (189/189 ops verified, 1063/1064 tests) |
| **Benchmarked Ops** | 190 |
| **Benchmark Failures** | ✅ None &ensp;|&ensp; ⚠️ 1 skipped |
| **Regressions** (vs 14-day median) | ✅ None |
| **Baseline Alerts** (< 80%) | ⚠️ 145 |
| **vs Baseline** | ↑ 1556 &ensp;·&ensp; ↓ 399 &ensp;/&ensp; 1955 rows |
| **Rows no reference checked** | ⚠️ 165 |
| **History window** | 14 runs, 2026-09-29 to 2026-10-12 |
| **Roofline anomalies** | ✅ None |
| **Improvements** (vs 14-day best) | 🎉 26 |
| **Moved since previous run** | 🔵 26 |
| **Never-built kernels** | ⚠️ 42 files &ensp;·&ensp; `kernels/linear_attention/gdn/prefill_forward.py` at 3.4% |
| **Untested roofline math** | 436 lines in `perf/` **+14** &ensp;·&ensp; `perf/formulas.py` at 17.1% |
| **Untested op logic** | 810 lines in `ops/` **+11** &ensp;·&ensp; 58.9% of branches taken |
| | <sub>coverage compared against the 2026-10-12 run; no figure means it held</sub> |

## 🎉 Performance Improvements (vs 14-day best)

| Op | Config | Prev Best (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-b-m4096-s128-float8_e4m3fn-bfloat16] | 0.3375 | 0.1586 | -53.0% | 868.33 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-a-m4096-s128-float8_e4m3fn-bfloat16] | 0.0747 | 0.0368 | -50.7% | 918.54 |
| **FusedTopKFwdOp** | test_fused_topk_bench[kimi-k2-t512-bias-bfloat16] | 0.0074 | 0.0041 | -43.9% | 0.62 |
| **FusedTopKFwdOp** | test_fused_topk_bench[kimi-k2-t512-bias-float16] | 0.0074 | 0.0042 | -43.7% | 0.62 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-a-m128-s128-float8_e4m3fn-bfloat16] | 0.0207 | 0.0117 | -43.5% | 90.62 |
| **FusedTopKFwdOp** | test_fused_topk_bench[kimi-k2-t512-bias-float32] | 0.0074 | 0.0043 | -41.7% | 0.60 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-mlp-up-m128-s128-float8_e4m3fn-bfloat16] | 0.0270 | 0.0163 | -39.5% | 462.41 |
| **FusedTopKFwdOp** | test_fused_topk_bench[kimi-k2-t512-bfloat16] | 0.0059 | 0.0036 | -39.2% | 0.66 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-a-m4096-s1-float8_e4m3fn-bfloat16] | 0.0866 | 0.0540 | -37.6% | 626.70 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-o-proj-m128-s1-float8_e4m3fn-bfloat16] | 0.0926 | 0.0579 | -37.5% | 521.71 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-q-b-m128-s128-float8_e4m3fn-bfloat16] | 0.0281 | 0.0183 | -34.9% | 531.26 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-b-m128-s128-float8_e4m3fn-bfloat16] | 0.0182 | 0.0121 | -33.8% | 357.61 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-o-proj-float8_e4m3fn-bfloat16] | 1.5444 | 1.0805 | -30.0% | 890.55 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-o-proj-m128-s128-float8_e4m3fn-bfloat16] | 0.0662 | 0.0493 | -25.6% | 612.50 |
| **FusedTopKFwdOp** | test_fused_topk_bench[qwen3-235b-t512-float16] | 0.0040 | 0.0030 | -25.0% | 0.24 |
| **FusedTopKFwdOp** | test_fused_topk_bench[qwen3-235b-t512-bfloat16] | 0.0040 | 0.0030 | -24.2% | 0.24 |
| **FusedTopKFwdOp** | test_fused_topk_bench[qwen3-235b-t512-float32] | 0.0040 | 0.0030 | -23.4% | 0.24 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-qkv-a-blk-float8_e4m3fn-bfloat16] | 0.2088 | 0.1674 | -19.8% | 741.07 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-qkv-a-bias-float8_e4m3fn-bfloat16] | 0.0144 | 0.0119 | -17.6% | 327.76 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-qkv-a-float8_e4m3fn-bfloat16] | 0.0139 | 0.0115 | -17.2% | 337.81 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-qkv-a-float8_e4m3fn-float16] | 0.0139 | 0.0115 | -16.9% | 337.78 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-m1-down-float8_e4m3fn-bfloat16] | 0.0096 | 0.0080 | -16.1% | 5.48 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-qkv-a-float8_e4m3fn-bfloat16] | 0.1256 | 0.1089 | -13.3% | 1139.15 |
| **GeluFwdOp** | test_gelu_bench[llama-8b-ffn-prefill-bfloat16] | 0.0402 | 0.0355 | -11.8% | 4.14 |
| **GemmW4A16FwdOp** | test_gemm_w4a16_bench[qwen3-32b-prefill-down-float16] | 0.1021 | 0.0908 | -11.1% | 372.36 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-down-blk-float8_e4m3fn-bfloat16] | 0.0132 | 0.0118 | -10.2% | 319.67 |

## 🔵 Moved Since Previous Run

> Moves against the most recent reading. A row restored to its old level appears only here: returning is not a new 14-day record.

| Op | Config | Previous (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-b-m4096-s128-float8_e4m3fn-bfloat16] | 0.3382 | 0.1586 | -53.1% | 868.33 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-a-m4096-s128-float8_e4m3fn-bfloat16] | 0.0747 | 0.0368 | -50.7% | 918.54 |
| **FusedTopKFwdOp** | test_fused_topk_bench[kimi-k2-t512-bias-bfloat16] | 0.0074 | 0.0041 | -44.1% | 0.62 |
| **FusedTopKFwdOp** | test_fused_topk_bench[kimi-k2-t512-bias-float16] | 0.0074 | 0.0042 | -43.7% | 0.62 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-a-m128-s128-float8_e4m3fn-bfloat16] | 0.0208 | 0.0117 | -43.6% | 90.62 |
| **FusedTopKFwdOp** | test_fused_topk_bench[kimi-k2-t512-bias-float32] | 0.0074 | 0.0043 | -42.0% | 0.60 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-mlp-up-m128-s128-float8_e4m3fn-bfloat16] | 0.0270 | 0.0163 | -39.6% | 462.41 |
| **FusedTopKFwdOp** | test_fused_topk_bench[kimi-k2-t512-bfloat16] | 0.0059 | 0.0036 | -39.2% | 0.66 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-a-m4096-s1-float8_e4m3fn-bfloat16] | 0.0867 | 0.0540 | -37.7% | 626.70 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-o-proj-m128-s1-float8_e4m3fn-bfloat16] | 0.0928 | 0.0579 | -37.7% | 521.71 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-q-b-m128-s128-float8_e4m3fn-bfloat16] | 0.0281 | 0.0183 | -35.0% | 531.26 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-b-m128-s128-float8_e4m3fn-bfloat16] | 0.0183 | 0.0121 | -33.9% | 357.61 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-o-proj-float8_e4m3fn-bfloat16] | 1.5467 | 1.0805 | -30.1% | 890.55 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-o-proj-m128-s128-float8_e4m3fn-bfloat16] | 0.0666 | 0.0493 | -26.0% | 612.50 |
| **FusedTopKFwdOp** | test_fused_topk_bench[qwen3-235b-t512-float16] | 0.0040 | 0.0030 | -25.0% | 0.24 |
| **FusedTopKFwdOp** | test_fused_topk_bench[qwen3-235b-t512-bfloat16] | 0.0040 | 0.0030 | -24.2% | 0.24 |
| **FusedTopKFwdOp** | test_fused_topk_bench[qwen3-235b-t512-float32] | 0.0040 | 0.0030 | -23.4% | 0.24 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-qkv-a-blk-float8_e4m3fn-bfloat16] | 0.2091 | 0.1674 | -19.9% | 741.07 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-qkv-a-bias-float8_e4m3fn-bfloat16] | 0.0145 | 0.0119 | -17.9% | 327.76 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-qkv-a-float8_e4m3fn-bfloat16] | 0.0139 | 0.0115 | -17.2% | 337.81 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-qkv-a-float8_e4m3fn-float16] | 0.0139 | 0.0115 | -17.1% | 337.78 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-m1-down-float8_e4m3fn-bfloat16] | 0.0096 | 0.0080 | -16.3% | 5.48 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-qkv-a-float8_e4m3fn-bfloat16] | 0.1258 | 0.1089 | -13.4% | 1139.15 |
| **GemmW4A16FwdOp** | test_gemm_w4a16_bench[qwen3-32b-prefill-down-float16] | 0.1036 | 0.0908 | -12.4% | 372.36 |
| **GeluFwdOp** | test_gelu_bench[llama-8b-ffn-prefill-bfloat16] | 0.0404 | 0.0355 | -12.1% | 4.14 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-decode-down-blk-float8_e4m3fn-bfloat16] | 0.0132 | 0.0118 | -10.2% | 319.67 |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 80%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-32k-bfloat16] | 0.3859 | 0.0871 | 22.6% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[ds-v32-decode-b1-float8_e4m3fn] | 0.2870 | 0.0656 | 22.9% | torch-ref |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-mixed-float16] | 22.3490 | 5.1942 | 23.2% | fa3 |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-rope-float16] | 41.9353 | 14.1293 | 33.7% | fa3 |
| 🔴 | **TopKSelectFwdOp** | test_topk_select_bench[ds-v32-topk-decode-b1] | 0.0634 | 0.0216 | 34.1% | flashinfer |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-rope-float16] | 1.6664 | 0.6850 | 41.1% | fa3 |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-32k-bfloat16] | 0.3855 | 0.1595 | 41.4% | flashinfer |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-float16-float8_e4m3fn] | 56.1863 | 23.2897 | 41.4% | fa3 |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-32k-float16] | 0.3856 | 0.1607 | 41.7% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-single-request-float16] | 0.0542 | 0.0227 | 41.9% | flashinfer |

<details>
<summary><strong>135 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-single-request-bfloat16] | 0.0542 | 0.0227 | 41.9% | flashinfer |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t32] | 0.0137 | 0.0058 | 42.0% | vllm |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t1] | 0.0121 | 0.0051 | 42.4% | vllm |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b1-float16] | 0.0541 | 0.0234 | 43.2% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b1-bfloat16] | 0.0541 | 0.0234 | 43.2% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b2-float16] | 0.0547 | 0.0237 | 43.4% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b2-bfloat16] | 0.0548 | 0.0238 | 43.4% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b6-float16] | 0.0594 | 0.0267 | 44.9% | flashinfer |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-65536-bfloat16] | 5.9636 | 2.6825 | 45.0% | fla |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b6-bfloat16] | 0.0594 | 0.0268 | 45.1% | flashinfer |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-16384-bfloat16] | 1.5182 | 0.6940 | 45.7% | fla |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t512] | 0.0158 | 0.0078 | 49.1% | vllm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx131072-float8_e4m3fn] | 17.2968 | 8.9846 | 51.9% | deepgemm |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-1024-7168-bfloat16] | 0.6781 | 0.3537 | 52.2% | fla |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-4096-bfloat16] | 0.3844 | 0.2011 | 52.3% | fla |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx65536-float8_e4m3fn] | 8.4945 | 4.4560 | 52.5% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx131072-float8_e4m3fn] | 8.7109 | 4.5875 | 52.7% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx65536-float8_e4m3fn] | 4.3191 | 2.2799 | 52.8% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx32768-float8_e4m3fn] | 4.1161 | 2.1826 | 53.0% | deepgemm |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[ds-v3-t1] | 0.0096 | 0.0052 | 53.7% | vllm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx32768-float8_e4m3fn] | 2.1291 | 1.1515 | 54.1% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx16384-float8_e4m3fn] | 1.9355 | 1.0531 | 54.4% | deepgemm |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp4-65536-bfloat16] | 6.5848 | 3.5978 | 54.6% | fla |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx16384-float8_e4m3fn] | 1.0404 | 0.5730 | 55.1% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx8192-float8_e4m3fn] | 0.8632 | 0.4757 | 55.1% | deepgemm |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp4-16384-bfloat16] | 1.6786 | 0.9258 | 55.1% | fla |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx8192-float8_e4m3fn] | 0.5022 | 0.2791 | 55.6% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-4x2048-bfloat16] | 0.2545 | 0.1433 | 56.3% | flashinfer |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[gemma-2b-bfloat16] | 0.3018 | 0.1703 | 56.4% | fa3 |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx4096-float8_e4m3fn] | 0.2335 | 0.1322 | 56.6% | deepgemm |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[ds-v3-t32] | 0.0100 | 0.0057 | 56.9% | vllm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-16x8192-bfloat16] | 0.8211 | 0.4679 | 57.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-4x2048-float16] | 0.2471 | 0.1425 | 57.7% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx4096-float8_e4m3fn] | 0.3272 | 0.1894 | 57.9% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x8192-bfloat16] | 0.8070 | 0.4674 | 57.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-16x8192-float16] | 0.7996 | 0.4668 | 58.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x8192-float16] | 0.7847 | 0.4667 | 59.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4096-4096-bfloat16] | 0.4177 | 0.2528 | 60.5% | flashinfer |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp4-4096-bfloat16] | 0.4322 | 0.2617 | 60.6% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x1024-bfloat16] | 0.1418 | 0.0866 | 61.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x1024-bfloat16] | 0.2602 | 0.1625 | 62.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4096-4096-float16] | 0.4037 | 0.2525 | 62.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x1024-float16] | 0.1372 | 0.0861 | 62.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-32x8192-bfloat16] | 1.4514 | 0.9212 | 63.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x8192-bfloat16] | 2.1772 | 1.3822 | 63.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-16x8192-bfloat16] | 1.4530 | 0.9230 | 63.5% | flashinfer |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp2-65536-bfloat16] | 8.4201 | 5.3653 | 63.7% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x8192-bfloat16] | 0.7421 | 0.4731 | 63.7% | flashinfer |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[starcoder-float16] | 0.7871 | 0.5039 | 64.0% | fa3 |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp2-16384-bfloat16] | 2.1503 | 1.3765 | 64.0% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-16x8192-bfloat16] | 2.8782 | 1.8447 | 64.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-32x8192-bfloat16] | 2.8556 | 1.8310 | 64.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x1024-float16] | 0.2525 | 0.1620 | 64.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-4x2048-bfloat16] | 0.2279 | 0.1472 | 64.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x8192-bfloat16] | 1.4388 | 0.9297 | 64.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x8192-bfloat16] | 2.8553 | 1.8484 | 64.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x8192-bfloat16] | 1.4348 | 0.9303 | 64.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-32x8192-float16] | 1.4119 | 0.9160 | 64.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-16x8192-float16] | 1.4148 | 0.9185 | 64.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-4x2048-bfloat16] | 0.2218 | 0.1442 | 65.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x8192-float16] | 2.1134 | 1.3742 | 65.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x8192-float16] | 0.7203 | 0.4716 | 65.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4x2048-bfloat16] | 0.4158 | 0.2725 | 65.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-32x8192-float16] | 2.7668 | 1.8194 | 65.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-16x8192-float16] | 2.7807 | 1.8319 | 65.9% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[context-chunk-bfloat16] | 0.3201 | 0.2113 | 66.0% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x8192-float16] | 2.7789 | 1.8356 | 66.1% | flashinfer |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp2-4096-bfloat16] | 0.5536 | 0.3665 | 66.2% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-16x8192-bfloat16] | 4.1408 | 2.7437 | 66.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-4x2048-float16] | 0.2205 | 0.1462 | 66.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x8192-float16] | 1.3952 | 0.9254 | 66.3% | flashinfer |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[ds-v3-t512] | 0.0119 | 0.0079 | 66.4% | vllm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x8192-float16] | 1.3888 | 0.9232 | 66.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-32x8192-bfloat16] | 8.1833 | 5.4562 | 66.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-16x8192-bfloat16] | 1.3870 | 0.9282 | 66.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-16x8192-bfloat16] | 5.4726 | 3.6713 | 67.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-32x8192-bfloat16] | 10.8880 | 7.3063 | 67.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-32x8192-bfloat16] | 5.4584 | 3.6676 | 67.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-4x2048-float16] | 0.2143 | 0.1443 | 67.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-32x8192-bfloat16] | 2.7225 | 1.8336 | 67.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4x2048-float16] | 0.4016 | 0.2711 | 67.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-16x8192-bfloat16] | 2.7351 | 1.8489 | 67.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x8192-bfloat16] | 1.3823 | 0.9360 | 67.7% | flashinfer |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t4096] | 0.0379 | 0.0257 | 67.8% | vllm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-32x8192-bfloat16] | 5.4056 | 3.6669 | 67.8% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-kscale-float8_e4m3fn] | 0.4711 | 0.3197 | 67.9% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-16x8192-bfloat16] | 2.7250 | 1.8503 | 67.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-16x8192-float16] | 4.0049 | 2.7226 | 68.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-32x8192-float16] | 7.9233 | 5.4186 | 68.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-16x8192-float16] | 1.3463 | 0.9228 | 68.5% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-32768-bfloat16] | 3.1443 | 2.1581 | 68.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-16x8192-float16] | 5.3088 | 3.6461 | 68.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-16x8192-float16] | 2.6542 | 1.8305 | 69.0% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-32768-float16] | 3.1455 | 2.1702 | 69.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-32x8192-float16] | 5.2689 | 3.6403 | 69.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-16x8192-float16] | 2.6567 | 1.8371 | 69.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-32x8192-float16] | 2.6319 | 1.8238 | 69.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-32x8192-float16] | 10.4748 | 7.2701 | 69.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x8192-float16] | 1.3379 | 0.9307 | 69.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-32x8192-float16] | 5.2387 | 3.6465 | 69.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-32x8192-bfloat16] | 5.2119 | 3.6687 | 70.4% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-16384-float16] | 1.5519 | 1.0971 | 70.7% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-serving-batch-bfloat16] | 0.0872 | 0.0617 | 70.8% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-16384-bfloat16] | 1.5517 | 1.0989 | 70.8% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-serving-batch-float16] | 0.0875 | 0.0620 | 70.9% | flashinfer |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-float16-float8_e4m3fn] | 1.9681 | 1.3982 | 71.0% | fa3 |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-8192-float16] | 0.7915 | 0.5649 | 71.4% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-8192-bfloat16] | 0.7895 | 0.5638 | 71.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-32x8192-float16] | 5.0622 | 3.6481 | 72.1% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-float8_e4m3fn] | 0.5143 | 0.3717 | 72.3% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4096-4096-bfloat16] | 0.3379 | 0.2444 | 72.3% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-bfloat16] | 0.5285 | 0.3829 | 72.5% | deepgemm |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-4096-bfloat16] | 0.4104 | 0.2981 | 72.6% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-4096-float16] | 0.4113 | 0.3003 | 73.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x1024-bfloat16] | 0.3189 | 0.2375 | 74.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4096-4096-float16] | 0.3263 | 0.2436 | 74.7% | flashinfer |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[falcon-7b-2k-bfloat16] | 0.0370 | 0.0277 | 75.0% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x1024-bfloat16] | 0.1172 | 0.0880 | 75.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x1024-bfloat16] | 0.4111 | 0.3091 | 75.2% | flashinfer |
| 🔴 | **DeltaNetChunkBwdOp** | test_deltanet_vs_fla_bwd[deltanet-1.3b-train-bfloat16] | 0.0723 | 0.0544 | 75.3% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x1024-bfloat16] | 0.2206 | 0.1672 | 75.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x1024-bfloat16] | 0.2158 | 0.1636 | 75.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x1024-float16] | 0.3081 | 0.2367 | 76.8% | flashinfer |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[qwen3-235b-t32] | 0.0070 | 0.0054 | 77.2% | vllm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x1024-float16] | 0.1129 | 0.0872 | 77.2% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-4k-bfloat16] | 0.1151 | 0.0895 | 77.7% | flashinfer |
| 🔴 | **GLAChunkFwdOp** | test_gla_chunk_fwd_bench[train-16k-float16] | 0.6157 | 0.4799 | 77.9% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x1024-float16] | 0.3949 | 0.3086 | 78.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x1024-float16] | 0.2122 | 0.1661 | 78.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x1024-float16] | 0.2084 | 0.1634 | 78.4% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-4k-float16] | 0.1157 | 0.0908 | 78.4% | flashinfer |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 0.5638 | 0.4452 | 79.0% | fa3 |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.5660 | 0.4484 | 79.2% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4x2048-bfloat16] | 0.3317 | 0.2632 | 79.3% | flashinfer |
| 🔴 | **GLAChunkFwdOp** | test_gla_chunk_fwd_bench[train-4k-float16] | 0.1567 | 0.1252 | 79.9% | fla |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 42 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 436 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 810 lines in `ops/`, 58.9% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 2495 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

### Never-built kernels

| File | Executed |
| --- | --- |
| `kernels/linear_attention/gdn/prefill_forward.py` | 3.4% |
| `kernels/linear_attention/gdn/prefill_prepare.py` | 3.4% |
| `kernels/linear_attention/kda/fused_program.py` | 3.6% |
| `kernels/linear_attention/deltanet/prefill_forward.py` | 4.3% |
| `kernels/linear_attention/kda/chunk_programs.py` | 5.1% |
| `kernels/linear_attention/deltanet/prefill_prepare.py` | 5.7% |
| `kernels/sampling/top_k_top_p_mask.py` | 6.5% |
| `kernels/attention/gqa/dense_fp8.py` | 6.6% |
| `kernels/attention/gqa/prefill_paged_kv_append.py` | 6.9% |
| `kernels/linear_attention/delta_decode.py` | 7.8% |
| `kernels/attention/gqa/dense.py` | 9.6% |
| `kernels/attention/gqa/varlen_fp8.py` | 9.7% |
| `kernels/sampling/top_k_mask.py` | 10.8% |
| `kernels/sampling/sampling_from_probs.py` | 11.8% |
| `kernels/sampling/chain_speculative_sampling.py` | 11.8% |
| `kernels/linear_attention/kda/decode_program.py` | 11.9% |
| `kernels/attention/mla/decode.py` | 12.1% |
| `kernels/linear_attention/gla/varlen_prefill.py` | 12.2% |
| `kernels/sampling/top_p_mask.py` | 12.4% |
| `kernels/attention/gqa/decode_bs1.py` | 12.7% |
| `kernels/quantization/int8_quant_per_tensor.py` | 12.9% |
| `kernels/attention/gqa/paged_ws.py` | 13.0% |
| `kernels/attention/nsa/compressed_varlen.py` | 13.5% |
| `kernels/linear_attention/gla/dense_prefill_partitioned.py` | 14.7% |
| `kernels/linear_attention/gla/dense_prefill_subchunk.py` | 14.9% |
| `kernels/linear_attention/gla/varlen_prefill_partitioned.py` | 15.1% |
| `kernels/quantization/int8_quant_per_channel.py` | 15.7% |
| `kernels/quantization/int8_quant_per_block.py` | 16.0% |
| `kernels/linear_attention/chunk_prefill.py` | 16.7% |
| `kernels/attention/gqa/decode_fp8.py` | 16.9% |
| `kernels/moe/indexed_expert_gemm.py` | 17.0% |
| `kernels/attention/varlen_rope.py` | 17.1% |
| `kernels/gemm/grouped/general.py` | 17.2% |
| `kernels/attention/dsa/decode.py` | 18.6% |
| `kernels/linear_attention/deltanet/partition_scan.py` | 19.1% |
| `kernels/sampling/min_p_mask.py` | 19.7% |
| `kernels/linear_attention/gla/dense_decode.py` | 21.2% |
| `kernels/quantization/fp8_quant_per_block.py` | 22.4% |
| `kernels/norm/rms_norm_on_chip.py` | 23.0% |
| `kernels/linear_attention/gdn/prefill.py` | 23.3% |
| `kernels/sampling/radix_select.py` | 24.1% |
| `kernels/linear_attention/chunk_plan.py` | 24.2% |

<details>
<summary>Untested pure Python, worst 15 files</summary>

| File | Uncovered | Executed |
| --- | --- | --- |
| `perf/formulas.py` | 394 | 17.1% |
| `manifest/plan.py` | 356 | 30.1% |
| `manifest/workload.py` | 194 | 58.5% |
| `ops/op_base.py` | 155 | 67.8% |
| `manifest/primitives.py` | 152 | 56.4% |
| `manifest/expr.py` | 122 | 70.7% |
| `manifest/signature.py` | 107 | 76.7% |
| `ops/_signature_codegen.py` | 87 | 89.5% |
| `trace/ui.py` | 62 | 24.4% |
| `manifest/kinds.py` | 53 | 79.2% |
| `ops/attention/gqa/prefill_paged_kv_append.py` | 53 | 35.4% |
| `backend/registry.py` | 48 | 50.0% |
| `perf/profile.py` | 42 | 22.2% |
| `ops/reduction/reduce.py` | 27 | 79.4% |
| `ops/moe/fused_moe_shared_expert.py` | 25 | 32.4% |

</details>

Per-line detail is in the `htmlcov/` directory of this run's `tileops_op_test` artifact.
