# ✅ TileOPs Nightly Report

> **2026-10-08 19:38** &ensp;|&ensp; `86c15907` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Operators** | 188 |
| **Kernels** | 297 |
| **Specs** | 17 |
| **Workloads** | 1220 |
| **Correctness** | ✅ &ensp; (188/188 ops verified, 1027/1027 tests) |
| **Benchmarked Ops** | 189 |
| **Benchmark Failures** | ✅ None &ensp;|&ensp; ⚠️ 1 skipped |
| **Regressions** (vs 14-day median) | ✅ None |
| **Baseline Alerts** (< 80%) | ⚠️ 190 |
| **vs Baseline** | ↑ 1471 &ensp;·&ensp; ↓ 457 &ensp;/&ensp; 1928 rows |
| **Rows no reference checked** | ⚠️ 165 |
| **History window** | 14 runs, 2026-09-24 to 2026-10-07 |
| **Roofline anomalies** | ✅ None |
| **Improvements** (vs 14-day best) | 🎉 5 |
| **Moved since previous run** | 🔵 5 |
| **Never-built kernels** | ⚠️ 38 files &ensp;·&ensp; `kernels/linear_attention/gdn/prefill_forward.py` at 3.4% |
| **Untested roofline math** | 422 lines in `perf/` &ensp;·&ensp; `perf/formulas.py` at 17.4% |
| **Untested op logic** | 924 lines in `ops/` &ensp;·&ensp; 57.4% of branches taken |
| | <sub>coverage compared against the 2026-10-07 run; no figure means it held</sub> |

## 🎉 Performance Improvements (vs 14-day best)

| Op | Config | Prev Best (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-q-b-2d-float8_e4m3fn-bfloat16] | 0.3571 | 0.2669 | -25.2% | 1159.40 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-down-2d-float8_e4m3fn-bfloat16] | 0.1438 | 0.1079 | -24.9% | 1114.85 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-qkv-a-2d-float8_e4m3fn-bfloat16] | 0.1525 | 0.1157 | -24.1% | 1071.75 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-mlp-up-2d-float8_e4m3fn-bfloat16] | 0.2418 | 0.1946 | -19.5% | 1236.54 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-o-proj-2d-float8_e4m3fn-bfloat16] | 0.8682 | 0.7088 | -18.4% | 1357.51 |

## 🔵 Moved Since Previous Run

> Moves against the most recent reading. A row restored to its old level appears only here: returning is not a new 14-day record.

| Op | Config | Previous (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-q-b-2d-float8_e4m3fn-bfloat16] | 0.3591 | 0.2669 | -25.7% | 1159.40 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-down-2d-float8_e4m3fn-bfloat16] | 0.1438 | 0.1079 | -24.9% | 1114.85 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-qkv-a-2d-float8_e4m3fn-bfloat16] | 0.1526 | 0.1157 | -24.2% | 1071.75 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-mlp-up-2d-float8_e4m3fn-bfloat16] | 0.2425 | 0.1946 | -19.8% | 1236.54 |
| **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-o-proj-2d-float8_e4m3fn-bfloat16] | 0.8691 | 0.7088 | -18.4% | 1357.51 |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 80%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h128-kv64k-bfloat16] | 32.8859 | 2.3972 | 7.3% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h128-kv48k-bfloat16] | 32.0038 | 2.3960 | 7.5% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h128-kv32k-bfloat16] | 30.1803 | 2.3859 | 7.9% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h64-kv64k-bfloat16] | 8.5110 | 0.7284 | 8.6% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h64-kv48k-bfloat16] | 8.2489 | 0.7185 | 8.7% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h64-kv32k-bfloat16] | 7.7664 | 0.7096 | 9.1% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h128-kv8k-bfloat16] | 24.7482 | 2.3506 | 9.5% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h64-kv8k-bfloat16] | 6.3294 | 0.6990 | 11.0% | flashmla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-long-context-float16] | 12.5251 | 1.4455 | 11.5% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-long-context-bfloat16] | 12.5273 | 1.4477 | 11.6% | fla |

<details>
<summary><strong>180 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-ragged-bfloat16] | 0.9159 | 0.1578 | 17.2% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-ragged-float16] | 0.9147 | 0.1581 | 17.3% | fla |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-32k-bfloat16] | 0.3931 | 0.0874 | 22.2% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[ds-v32-decode-b1-float8_e4m3fn] | 0.2873 | 0.0656 | 22.8% | torch-ref |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-mixed-float16] | 22.3756 | 5.1959 | 23.2% | fa3 |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-8x1k-float16] | 0.5204 | 0.1339 | 25.7% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-8x1k-bfloat16] | 0.5210 | 0.1342 | 25.8% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-4x1k-float16] | 0.2739 | 0.0706 | 25.8% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-4x1k-bfloat16] | 0.2742 | 0.0710 | 25.9% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-wide-gqa-float16] | 0.5232 | 0.1620 | 30.9% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-wide-gqa-bfloat16] | 0.5243 | 0.1630 | 31.1% | fla |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-rope-float16] | 41.8954 | 14.2027 | 33.9% | fa3 |
| 🔴 | **TopKSelectFwdOp** | test_topk_select_bench[ds-v32-topk-decode-b1] | 0.0635 | 0.0217 | 34.1% | flashinfer |
| 🔴 | **NSACompressedVarlenFwdOp** | test_nsa_compressed_fwd_varlen_bench[prefill-4x1k-float16] | 0.1459 | 0.0536 | 36.8% | fla |
| 🔴 | **NSACompressedVarlenFwdOp** | test_nsa_compressed_fwd_varlen_bench[prefill-8x1k-float16] | 0.2710 | 0.1004 | 37.1% | fla |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-32k-bfloat16] | 0.3936 | 0.1591 | 40.4% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-32k-float16] | 0.3939 | 0.1606 | 40.8% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-single-request-float16] | 0.0551 | 0.0227 | 41.1% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-single-request-bfloat16] | 0.0553 | 0.0228 | 41.2% | flashinfer |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-rope-float16] | 1.6625 | 0.6867 | 41.3% | fa3 |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-float16-float8_e4m3fn] | 56.2617 | 23.3427 | 41.5% | fa3 |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b1-float16] | 0.0557 | 0.0233 | 41.8% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b1-bfloat16] | 0.0558 | 0.0233 | 41.8% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b2-float16] | 0.0567 | 0.0237 | 41.9% | flashinfer |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t32] | 0.0137 | 0.0058 | 42.0% | vllm |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b2-bfloat16] | 0.0567 | 0.0238 | 42.0% | flashinfer |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t1] | 0.0121 | 0.0051 | 42.3% | vllm |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b6-float16] | 0.0611 | 0.0267 | 43.7% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b6-bfloat16] | 0.0611 | 0.0268 | 43.8% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-b-m4096-s128-float8_e4m3fn-bfloat16] | 0.3383 | 0.1515 | 44.8% | deepgemm |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-65536-bfloat16] | 5.9497 | 2.6802 | 45.1% | fla |
| 🔴 | **NSACompressedVarlenFwdOp** | test_nsa_compressed_fwd_varlen_bench[prefill-ragged-bfloat16] | 0.0396 | 0.0181 | 45.6% | fla |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-16384-bfloat16] | 1.5198 | 0.6948 | 45.7% | fla |
| 🔴 | **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[qwen3-ragged-odd-bfloat16-bfloat16] | 0.4013 | 0.1891 | 47.1% | fa3 |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv128k-bfloat16] | 9.9291 | 4.7572 | 47.9% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv96k-bfloat16] | 9.8551 | 4.7391 | 48.1% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv64k-bfloat16] | 9.6822 | 4.7067 | 48.6% | flashmla |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t512] | 0.0158 | 0.0078 | 49.1% | vllm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx131072-float8_e4m3fn] | 17.2778 | 8.9378 | 51.7% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx131072-float8_e4m3fn] | 8.7320 | 4.5422 | 52.0% | deepgemm |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-1024-7168-bfloat16] | 0.6777 | 0.3540 | 52.2% | fla |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-4096-bfloat16] | 0.3836 | 0.2015 | 52.5% | fla |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx65536-float8_e4m3fn] | 8.4983 | 4.4682 | 52.6% | deepgemm |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv32k-bfloat16] | 8.8354 | 4.6496 | 52.6% | flashmla |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx65536-float8_e4m3fn] | 4.3186 | 2.2879 | 53.0% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx32768-float8_e4m3fn] | 4.1108 | 2.1912 | 53.3% | deepgemm |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[ds-v3-t1] | 0.0096 | 0.0052 | 53.7% | vllm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx16384-float8_e4m3fn] | 1.9382 | 1.0489 | 54.1% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx32768-float8_e4m3fn] | 2.1244 | 1.1549 | 54.4% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx16384-float8_e4m3fn] | 1.0401 | 0.5681 | 54.6% | deepgemm |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp4-16384-bfloat16] | 1.6786 | 0.9261 | 55.2% | fla |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx8192-float8_e4m3fn] | 0.8633 | 0.4774 | 55.3% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx8192-float8_e4m3fn] | 0.5027 | 0.2786 | 55.4% | deepgemm |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp4-65536-bfloat16] | 6.4578 | 3.5969 | 55.7% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-4x2048-bfloat16] | 0.2545 | 0.1430 | 56.2% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx4096-float8_e4m3fn] | 0.2333 | 0.1316 | 56.4% | deepgemm |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[gemma-2b-bfloat16] | 0.3012 | 0.1699 | 56.4% | fa3 |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[ds-v3-t32] | 0.0100 | 0.0056 | 56.6% | vllm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-16x8192-bfloat16] | 0.8214 | 0.4691 | 57.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-4x2048-float16] | 0.2468 | 0.1426 | 57.8% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-a-m4096-s128-float8_e4m3fn-bfloat16] | 0.0747 | 0.0432 | 57.9% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx4096-float8_e4m3fn] | 0.3262 | 0.1895 | 58.1% | deepgemm |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv8k-bfloat16] | 7.9705 | 4.6391 | 58.2% | flashmla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x8192-bfloat16] | 0.8045 | 0.4684 | 58.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-16x8192-float16] | 0.7953 | 0.4648 | 58.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x8192-float16] | 0.7832 | 0.4667 | 59.6% | flashinfer |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp4-4096-bfloat16] | 0.4344 | 0.2631 | 60.6% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4096-4096-bfloat16] | 0.4168 | 0.2529 | 60.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x1024-bfloat16] | 0.1416 | 0.0864 | 61.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4096-4096-float16] | 0.4026 | 0.2520 | 62.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x1024-bfloat16] | 0.2603 | 0.1629 | 62.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x1024-float16] | 0.1369 | 0.0861 | 62.9% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-a-m128-s128-float8_e4m3fn-bfloat16] | 0.0208 | 0.0132 | 63.3% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-16x8192-bfloat16] | 1.4543 | 0.9225 | 63.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x8192-bfloat16] | 0.7439 | 0.4720 | 63.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-32x8192-bfloat16] | 1.4527 | 0.9219 | 63.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x8192-bfloat16] | 2.1785 | 1.3825 | 63.5% | flashinfer |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp2-65536-bfloat16] | 8.4236 | 5.3745 | 63.8% | fla |
| 🔴 | **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-float16-float16] | 0.7925 | 0.5059 | 63.8% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-16x8192-bfloat16] | 2.8790 | 1.8440 | 64.0% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-mlp-up-m128-s128-float8_e4m3fn-bfloat16] | 0.0270 | 0.0173 | 64.1% | deepgemm |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[starcoder-float16] | 0.7885 | 0.5056 | 64.1% | fa3 |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp2-16384-bfloat16] | 2.1493 | 1.3790 | 64.2% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-32x8192-bfloat16] | 2.8520 | 1.8314 | 64.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-4x2048-bfloat16] | 0.2279 | 0.1468 | 64.4% | flashinfer |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[ds-v32-kv2k-bfloat16] | 1.9059 | 1.2289 | 64.5% | flashmla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x8192-bfloat16] | 2.8552 | 1.8450 | 64.6% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-b-m128-s128-float8_e4m3fn-bfloat16] | 0.0183 | 0.0118 | 64.7% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x1024-float16] | 0.2510 | 0.1625 | 64.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x8192-bfloat16] | 1.4368 | 0.9308 | 64.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x8192-float16] | 2.1150 | 1.3736 | 65.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x8192-bfloat16] | 1.4334 | 0.9312 | 65.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-32x8192-float16] | 1.4086 | 0.9171 | 65.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-4x2048-bfloat16] | 0.2215 | 0.1443 | 65.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-16x8192-float16] | 1.4119 | 0.9209 | 65.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x8192-float16] | 0.7193 | 0.4701 | 65.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4x2048-bfloat16] | 0.4167 | 0.2724 | 65.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-32x8192-float16] | 2.7706 | 1.8165 | 65.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-16x8192-float16] | 2.7837 | 1.8316 | 65.8% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-32768-bfloat16] | 3.2790 | 2.1618 | 65.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x8192-float16] | 2.7764 | 1.8314 | 66.0% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-32768-float16] | 3.2739 | 2.1615 | 66.0% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[context-chunk-bfloat16] | 0.3198 | 0.2113 | 66.1% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-16x8192-bfloat16] | 4.1416 | 2.7433 | 66.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x8192-float16] | 1.3949 | 0.9250 | 66.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x8192-float16] | 1.3908 | 0.9229 | 66.4% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-o-proj-m128-s1-float8_e4m3fn-bfloat16] | 0.0927 | 0.0616 | 66.5% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-32x8192-bfloat16] | 8.1822 | 5.4499 | 66.6% | flashinfer |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[ds-v3-t512] | 0.0119 | 0.0079 | 66.7% | vllm |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-a-m4096-s1-float8_e4m3fn-bfloat16] | 0.0868 | 0.0579 | 66.7% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-16x8192-bfloat16] | 1.3897 | 0.9274 | 66.7% | flashinfer |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp2-4096-bfloat16] | 0.5533 | 0.3693 | 66.8% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-16x8192-bfloat16] | 5.4839 | 3.6706 | 66.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-4x2048-float16] | 0.2196 | 0.1472 | 67.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-4x2048-float16] | 0.2139 | 0.1435 | 67.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-32x8192-bfloat16] | 10.8854 | 7.3074 | 67.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-32x8192-bfloat16] | 5.4489 | 3.6635 | 67.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-16x8192-bfloat16] | 2.7371 | 1.8437 | 67.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4x2048-float16] | 0.4020 | 0.2714 | 67.5% | flashinfer |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[ds-v32-kv4k-bfloat16] | 0.5129 | 0.3470 | 67.7% | flashmla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-32x8192-bfloat16] | 5.4123 | 3.6643 | 67.7% | flashinfer |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t4096] | 0.0378 | 0.0256 | 67.7% | vllm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x8192-bfloat16] | 1.3822 | 0.9368 | 67.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-16x8192-bfloat16] | 2.7284 | 1.8496 | 67.8% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-q-b-m128-s128-float8_e4m3fn-bfloat16] | 0.0282 | 0.0191 | 67.9% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-kscale-float8_e4m3fn] | 0.4711 | 0.3199 | 67.9% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-32x8192-bfloat16] | 2.7124 | 1.8427 | 67.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-16x8192-float16] | 3.9986 | 2.7265 | 68.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-32x8192-float16] | 7.9234 | 5.4314 | 68.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-16x8192-float16] | 1.3428 | 0.9224 | 68.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-16x8192-float16] | 5.3081 | 3.6483 | 68.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-16x8192-float16] | 2.6540 | 1.8295 | 68.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-32x8192-float16] | 5.2765 | 3.6403 | 69.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x8192-float16] | 1.3391 | 0.9277 | 69.3% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-16384-bfloat16] | 1.5751 | 1.0918 | 69.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-16x8192-float16] | 2.6511 | 1.8378 | 69.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-32x8192-float16] | 10.4717 | 7.2650 | 69.4% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-16384-float16] | 1.5769 | 1.0942 | 69.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-32x8192-float16] | 2.6332 | 1.8321 | 69.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-32x8192-float16] | 5.2304 | 3.6412 | 69.6% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-serving-batch-float16] | 0.0883 | 0.0618 | 70.0% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-o-proj-float8_e4m3fn-bfloat16] | 1.5444 | 1.0814 | 70.0% | deepgemm |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-8192-float16] | 0.8052 | 0.5646 | 70.1% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-serving-batch-bfloat16] | 0.0883 | 0.0621 | 70.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-32x8192-bfloat16] | 5.2073 | 3.6662 | 70.4% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-8192-bfloat16] | 0.8021 | 0.5651 | 70.5% | flashinfer |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-float16-float8_e4m3fn] | 1.9670 | 1.3950 | 70.9% | fa3 |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-o-proj-m128-s128-float8_e4m3fn-bfloat16] | 0.0664 | 0.0472 | 71.1% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-4096-bfloat16] | 0.4164 | 0.2979 | 71.5% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-4096-float16] | 0.4172 | 0.2990 | 71.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-32x8192-float16] | 5.0772 | 3.6408 | 71.7% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-float8_e4m3fn] | 0.5141 | 0.3713 | 72.2% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4096-4096-bfloat16] | 0.3377 | 0.2443 | 72.3% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-bfloat16] | 0.5287 | 0.3834 | 72.5% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x1024-bfloat16] | 0.3192 | 0.2373 | 74.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4096-4096-float16] | 0.3259 | 0.2432 | 74.6% | flashinfer |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[falcon-7b-2k-bfloat16] | 0.0371 | 0.0278 | 75.0% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x1024-bfloat16] | 0.1169 | 0.0880 | 75.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x1024-bfloat16] | 0.4101 | 0.3103 | 75.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x1024-bfloat16] | 0.2201 | 0.1666 | 75.7% | flashinfer |
| 🔴 | **DeltaNetChunkBwdOp** | test_deltanet_vs_fla_bwd[deltanet-1.3b-train-bfloat16] | 0.0717 | 0.0543 | 75.7% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x1024-bfloat16] | 0.2156 | 0.1634 | 75.8% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-4k-bfloat16] | 0.1174 | 0.0896 | 76.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x1024-float16] | 0.3082 | 0.2361 | 76.6% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-4k-float16] | 0.1175 | 0.0901 | 76.7% | flashinfer |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[qwen3-235b-t32] | 0.0070 | 0.0054 | 77.2% | vllm |
| 🔴 | **GLAChunkFwdOp** | test_gla_fwd_bench[train-16k-float16] | 0.6154 | 0.4756 | 77.3% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x1024-float16] | 0.1128 | 0.0874 | 77.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x1024-float16] | 0.3952 | 0.3091 | 78.2% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b64-bfloat16] | 0.1289 | 0.1008 | 78.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x1024-float16] | 0.2080 | 0.1633 | 78.5% | flashinfer |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 0.5637 | 0.4437 | 78.7% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x1024-float16] | 0.2118 | 0.1668 | 78.7% | flashinfer |
| 🔴 | **DeltaNetChunkBwdOp** | test_deltanet_vs_fla_bwd[train-4k-float16] | 0.2729 | 0.2153 | 78.9% | fla |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.5652 | 0.4460 | 78.9% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4x2048-bfloat16] | 0.3314 | 0.2628 | 79.3% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b64-float16] | 0.1294 | 0.1026 | 79.3% | flashinfer |
| 🔴 | **GLAChunkFwdOp** | test_gla_fwd_bench[train-4k-float16] | 0.1567 | 0.1246 | 79.5% | fla |
| 🔴 | **DeltaNetChunkBwdOp** | test_deltanet_vs_fla_bwd[train-4k-bfloat16] | 0.2724 | 0.2169 | 79.6% | fla |
| 🔴 | **GLAChunkFwdOp** | test_gla_fwd_bench[train-2k-bfloat16] | 0.0938 | 0.0748 | 79.8% | fla |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 38 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 422 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 924 lines in `ops/`, 57.4% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 2599 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

### Never-built kernels

| File | Executed |
| --- | --- |
| `kernels/linear_attention/gdn/prefill_forward.py` | 3.4% |
| `kernels/linear_attention/gdn/prefill_prepare.py` | 3.4% |
| `kernels/linear_attention/deltanet/prefill_forward.py` | 4.3% |
| `kernels/linear_attention/kda/fused_program.py` | 5.2% |
| `kernels/linear_attention/deltanet/prefill_prepare.py` | 5.7% |
| `kernels/linear_attention/kda/chunk_programs.py` | 5.9% |
| `kernels/sampling/top_k_top_p_mask.py` | 6.5% |
| `kernels/attention/gqa/prefill_paged_kv_append.py` | 6.9% |
| `kernels/attention/gqa/dense_fp8.py` | 7.2% |
| `kernels/linear_attention/delta_decode.py` | 7.8% |
| `kernels/attention/mla/decode.py` | 9.9% |
| `kernels/attention/gqa/varlen_fp8.py` | 10.0% |
| `kernels/attention/gqa/dense.py` | 10.5% |
| `kernels/sampling/top_k_mask.py` | 10.8% |
| `kernels/sampling/sampling_from_probs.py` | 11.8% |
| `kernels/sampling/chain_speculative_sampling.py` | 11.8% |
| `kernels/sampling/top_p_mask.py` | 12.4% |
| `kernels/quantization/int8_quant_per_tensor.py` | 12.9% |
| `kernels/linear_attention/gla/varlen_prefill.py` | 13.4% |
| `kernels/linear_attention/kda/decode_program.py` | 13.6% |
| `kernels/attention/gqa/decode_bs1.py` | 14.6% |
| `kernels/quantization/int8_quant_per_channel.py` | 15.7% |
| `kernels/linear_attention/gla/dense_prefill_partitioned.py` | 16.1% |
| `kernels/quantization/int8_quant_per_block.py` | 16.2% |
| `kernels/linear_attention/gla/varlen_prefill_partitioned.py` | 16.5% |
| `kernels/moe/indexed_expert_gemm.py` | 17.0% |
| `kernels/attention/varlen_rope.py` | 17.1% |
| `kernels/gemm/grouped/general.py` | 17.2% |
| `kernels/linear_attention/gla/dense_prefill_subchunk.py` | 17.3% |
| `kernels/attention/gqa/decode_fp8.py` | 17.8% |
| `kernels/linear_attention/deltanet/partition_scan.py` | 19.1% |
| `kernels/sampling/min_p_mask.py` | 19.7% |
| `kernels/attention/nsa/compressed_varlen.py` | 20.0% |
| `kernels/quantization/fp8_quant_per_block.py` | 22.6% |
| `kernels/norm/rms_norm_on_chip.py` | 22.7% |
| `kernels/sampling/radix_select.py` | 24.1% |
| `kernels/linear_attention/gla/dense_decode.py` | 24.3% |
| `kernels/linear_attention/gdn/prefill.py` | 24.4% |

<details>
<summary>Untested pure Python, worst 15 files</summary>

| File | Uncovered | Executed |
| --- | --- | --- |
| `perf/formulas.py` | 380 | 17.4% |
| `manifest/plan.py` | 356 | 30.1% |
| `manifest/workload.py` | 194 | 58.5% |
| `ops/op_base.py` | 187 | 65.1% |
| `manifest/primitives.py` | 149 | 54.4% |
| `manifest/expr.py` | 122 | 70.7% |
| `manifest/signature.py` | 109 | 76.3% |
| `ops/_signature_codegen.py` | 88 | 89.4% |
| `trace/ui.py` | 62 | 24.4% |
| `ops/attention/gqa/prefill_paged_kv_append.py` | 56 | 35.6% |
| `manifest/kinds.py` | 53 | 79.2% |
| `backend/registry.py` | 48 | 50.0% |
| `perf/profile.py` | 42 | 22.2% |
| `ops/rope.py` | 28 | 84.1% |
| `ops/reduction/reduce.py` | 27 | 80.1% |

</details>

Per-line detail is in the `htmlcov/` directory of this run's `tileops_op_test` artifact.
