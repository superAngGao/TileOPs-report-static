# ❌ TileOPs Nightly Report

> **2026-10-09 19:52** &ensp;|&ensp; `7c351e30` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Operators** | 188 |
| **Kernels** | 300 |
| **Specs** | 17 |
| **Workloads** | 1220 |
| **Correctness** | ✅ &ensp; (188/188 ops verified, 1030/1030 tests) |
| **Benchmarked Ops** | 189 |
| **Benchmark Failures** | ✅ None &ensp;|&ensp; ⚠️ 1 skipped |
| **Regressions** (vs 14-day median) | ⚠️ 1 |
| **Baseline Alerts** (< 80%) | ⚠️ 190 |
| **vs Baseline** | ↑ 1480 &ensp;·&ensp; ↓ 454 &ensp;/&ensp; 1934 rows |
| **Rows no reference checked** | ⚠️ 165 |
| **History window** | 14 runs, 2026-09-25 to 2026-10-08 |
| **Roofline anomalies** | ✅ None |
| **Improvements** (vs 14-day best) | 🎉 4 |
| **Moved since previous run** | 🔵 5 |
| **Never-built kernels** | ⚠️ 38 files &ensp;·&ensp; `kernels/linear_attention/gdn/prefill_forward.py` at 3.4% |
| **Untested roofline math** | 422 lines in `perf/` &ensp;·&ensp; `perf/formulas.py` at 17.4% |
| **Untested op logic** | 924 lines in `ops/` &ensp;·&ensp; 57.4% of branches taken |
| | <sub>coverage compared against the 2026-10-08 run; no figure means it held</sub> |

## ⚠️ Performance Regressions (vs 14-day median)

| Op | Config | Median (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-262144-float32] | 4.2544 | 4.7248 | +11.1% | 2.27 |

## 🎉 Performance Improvements (vs 14-day best)

| Op | Config | Prev Best (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **NSAVarlenFwdOp** | test_nsa_fwd_varlen_bench[prefill-ragged-bfloat16] | 0.0496 | 0.0250 | -49.7% | 80.39 |
| **NSAVarlenFwdOp** | test_nsa_fwd_varlen_bench[prefill-4x2k-float16] | 0.0321 | 0.0176 | -45.2% | 60.53 |
| **NSAVarlenFwdOp** | test_nsa_fwd_varlen_bench[prefill-2x4k-float16] | 0.0489 | 0.0281 | -42.6% | 96.08 |
| **NSAVarlenFwdOp** | test_nsa_fwd_varlen_bench[prefill-noncausal-2x4k-float16] | 0.0488 | 0.0307 | -37.2% | 88.73 |

## 🔵 Moved Since Previous Run

> Moves against the most recent reading. A row restored to its old level appears only here: returning is not a new 14-day record.

| Op | Config | Previous (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **NSAVarlenFwdOp** | test_nsa_fwd_varlen_bench[prefill-ragged-bfloat16] | 0.0498 | 0.0250 | -49.9% | 80.39 |
| **NSAVarlenFwdOp** | test_nsa_fwd_varlen_bench[prefill-4x2k-float16] | 0.0321 | 0.0176 | -45.2% | 60.53 |
| **NSAVarlenFwdOp** | test_nsa_fwd_varlen_bench[prefill-2x4k-float16] | 0.0492 | 0.0281 | -43.0% | 96.08 |
| **NSAVarlenFwdOp** | test_nsa_fwd_varlen_bench[prefill-noncausal-2x4k-float16] | 0.0489 | 0.0307 | -37.2% | 88.73 |
| **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-262144-float32] | 4.2515 | 4.7248 | +11.1% | 2.27 |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 80%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h128-kv64k-bfloat16] | 32.9592 | 2.3975 | 7.3% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h128-kv48k-bfloat16] | 31.9772 | 2.3927 | 7.5% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h128-kv32k-bfloat16] | 30.2054 | 2.3856 | 7.9% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h64-kv64k-bfloat16] | 8.5158 | 0.7278 | 8.6% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h64-kv48k-bfloat16] | 8.2438 | 0.7179 | 8.7% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h64-kv32k-bfloat16] | 7.7582 | 0.7090 | 9.1% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h128-kv8k-bfloat16] | 24.7482 | 2.3509 | 9.5% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h64-kv8k-bfloat16] | 6.3331 | 0.6998 | 11.1% | flashmla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-long-context-float16] | 12.5206 | 1.4450 | 11.5% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-long-context-bfloat16] | 12.5271 | 1.4463 | 11.6% | fla |

<details>
<summary><strong>180 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-ragged-float16] | 0.9159 | 0.1576 | 17.2% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-ragged-bfloat16] | 0.9165 | 0.1578 | 17.2% | fla |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-32k-bfloat16] | 0.3935 | 0.0873 | 22.2% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[ds-v32-decode-b1-float8_e4m3fn] | 0.2869 | 0.0655 | 22.8% | torch-ref |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-mixed-float16] | 22.3735 | 5.1790 | 23.2% | fa3 |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-8x1k-float16] | 0.5201 | 0.1339 | 25.7% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-8x1k-bfloat16] | 0.5208 | 0.1342 | 25.8% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-4x1k-float16] | 0.2742 | 0.0707 | 25.8% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-4x1k-bfloat16] | 0.2738 | 0.0713 | 26.1% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-wide-gqa-float16] | 0.5231 | 0.1613 | 30.8% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-wide-gqa-bfloat16] | 0.5255 | 0.1623 | 30.9% | fla |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-rope-float16] | 41.8956 | 14.2711 | 34.1% | fa3 |
| 🔴 | **TopKSelectFwdOp** | test_topk_select_bench[ds-v32-topk-decode-b1] | 0.0633 | 0.0217 | 34.2% | flashinfer |
| 🔴 | **NSACompressedVarlenFwdOp** | test_nsa_compressed_fwd_varlen_bench[prefill-4x1k-float16] | 0.1459 | 0.0534 | 36.6% | fla |
| 🔴 | **NSACompressedVarlenFwdOp** | test_nsa_compressed_fwd_varlen_bench[prefill-8x1k-float16] | 0.2711 | 0.1005 | 37.1% | fla |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-32k-bfloat16] | 0.3933 | 0.1590 | 40.4% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-32k-float16] | 0.3936 | 0.1603 | 40.7% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-single-request-float16] | 0.0552 | 0.0227 | 41.2% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-single-request-bfloat16] | 0.0552 | 0.0228 | 41.2% | flashinfer |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-rope-float16] | 1.6628 | 0.6868 | 41.3% | fa3 |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-float16-float8_e4m3fn] | 56.1582 | 23.3188 | 41.5% | fa3 |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b1-float16] | 0.0558 | 0.0233 | 41.7% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b2-float16] | 0.0566 | 0.0237 | 41.9% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b1-bfloat16] | 0.0557 | 0.0234 | 42.0% | flashinfer |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t32] | 0.0137 | 0.0058 | 42.0% | vllm |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b2-bfloat16] | 0.0566 | 0.0238 | 42.1% | flashinfer |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t1] | 0.0121 | 0.0051 | 42.3% | vllm |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b6-float16] | 0.0611 | 0.0267 | 43.7% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b6-bfloat16] | 0.0611 | 0.0268 | 43.9% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-b-m4096-s128-float8_e4m3fn-bfloat16] | 0.3376 | 0.1514 | 44.8% | deepgemm |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-65536-bfloat16] | 5.9632 | 2.6816 | 45.0% | fla |
| 🔴 | **NSACompressedVarlenFwdOp** | test_nsa_compressed_fwd_varlen_bench[prefill-ragged-bfloat16] | 0.0397 | 0.0180 | 45.3% | fla |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-16384-bfloat16] | 1.5187 | 0.6936 | 45.7% | fla |
| 🔴 | **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[qwen3-ragged-odd-bfloat16-bfloat16] | 0.4004 | 0.1888 | 47.1% | fa3 |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv128k-bfloat16] | 9.9528 | 4.7519 | 47.7% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv96k-bfloat16] | 9.8443 | 4.7384 | 48.1% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv64k-bfloat16] | 9.6711 | 4.6940 | 48.5% | flashmla |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t512] | 0.0158 | 0.0078 | 49.1% | vllm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx131072-float8_e4m3fn] | 17.3050 | 9.0171 | 52.1% | deepgemm |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-1024-7168-bfloat16] | 0.6771 | 0.3544 | 52.3% | fla |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-4096-bfloat16] | 0.3844 | 0.2014 | 52.4% | fla |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx65536-float8_e4m3fn] | 8.5464 | 4.4781 | 52.4% | deepgemm |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv32k-bfloat16] | 8.8362 | 4.6549 | 52.7% | flashmla |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx131072-float8_e4m3fn] | 8.6840 | 4.5765 | 52.7% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx65536-float8_e4m3fn] | 4.3119 | 2.2830 | 52.9% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx32768-float8_e4m3fn] | 4.1086 | 2.2027 | 53.6% | deepgemm |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[ds-v3-t1] | 0.0096 | 0.0052 | 53.7% | vllm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx32768-float8_e4m3fn] | 2.1305 | 1.1480 | 53.9% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx16384-float8_e4m3fn] | 1.9391 | 1.0540 | 54.4% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx16384-float8_e4m3fn] | 1.0403 | 0.5726 | 55.0% | deepgemm |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp4-16384-bfloat16] | 1.6775 | 0.9268 | 55.2% | fla |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx8192-float8_e4m3fn] | 0.8632 | 0.4770 | 55.3% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx8192-float8_e4m3fn] | 0.5036 | 0.2798 | 55.6% | deepgemm |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp4-65536-bfloat16] | 6.4547 | 3.5969 | 55.7% | fla |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[gemma-2b-bfloat16] | 0.3015 | 0.1681 | 55.8% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-4x2048-bfloat16] | 0.2551 | 0.1430 | 56.1% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx4096-float8_e4m3fn] | 0.2336 | 0.1317 | 56.4% | deepgemm |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[ds-v3-t32] | 0.0100 | 0.0056 | 56.6% | vllm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-16x8192-bfloat16] | 0.8205 | 0.4679 | 57.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-4x2048-float16] | 0.2474 | 0.1426 | 57.7% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-a-m4096-s128-float8_e4m3fn-bfloat16] | 0.0749 | 0.0434 | 57.9% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx4096-float8_e4m3fn] | 0.3268 | 0.1896 | 58.0% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x8192-bfloat16] | 0.8051 | 0.4676 | 58.1% | flashinfer |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv8k-bfloat16] | 7.9757 | 4.6351 | 58.1% | flashmla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-16x8192-float16] | 0.7952 | 0.4642 | 58.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x8192-float16] | 0.7816 | 0.4665 | 59.7% | flashinfer |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp4-4096-bfloat16] | 0.4350 | 0.2631 | 60.5% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4096-4096-bfloat16] | 0.4171 | 0.2533 | 60.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x1024-bfloat16] | 0.1413 | 0.0864 | 61.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4096-4096-float16] | 0.4033 | 0.2526 | 62.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x1024-bfloat16] | 0.2597 | 0.1627 | 62.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x1024-float16] | 0.1369 | 0.0860 | 62.8% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-a-m128-s128-float8_e4m3fn-bfloat16] | 0.0207 | 0.0131 | 63.3% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x8192-bfloat16] | 2.1768 | 1.3816 | 63.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-32x8192-bfloat16] | 1.4485 | 0.9195 | 63.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-16x8192-bfloat16] | 1.4512 | 0.9228 | 63.6% | flashinfer |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp2-65536-bfloat16] | 8.4318 | 5.3687 | 63.7% | fla |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-mlp-up-m128-s128-float8_e4m3fn-bfloat16] | 0.0271 | 0.0173 | 63.8% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x8192-bfloat16] | 0.7412 | 0.4728 | 63.8% | flashinfer |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp2-16384-bfloat16] | 2.1529 | 1.3788 | 64.0% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-16x8192-bfloat16] | 2.8756 | 1.8433 | 64.1% | flashinfer |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[starcoder-float16] | 0.7874 | 0.5048 | 64.1% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-32x8192-bfloat16] | 2.8533 | 1.8298 | 64.1% | flashinfer |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[ds-v32-kv2k-bfloat16] | 1.9065 | 1.2282 | 64.4% | flashmla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-4x2048-bfloat16] | 0.2272 | 0.1465 | 64.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x1024-float16] | 0.2516 | 0.1623 | 64.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x8192-bfloat16] | 1.4409 | 0.9301 | 64.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x8192-bfloat16] | 2.8565 | 1.8463 | 64.6% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-b-m128-s128-float8_e4m3fn-bfloat16] | 0.0183 | 0.0118 | 64.8% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x8192-float16] | 2.1158 | 1.3714 | 64.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-4x2048-bfloat16] | 0.2224 | 0.1444 | 65.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-32x8192-float16] | 1.4094 | 0.9161 | 65.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x8192-bfloat16] | 1.4299 | 0.9324 | 65.2% | flashinfer |
| 🔴 | **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-float16-float16] | 0.7720 | 0.5044 | 65.3% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-16x8192-float16] | 1.4113 | 0.9224 | 65.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x8192-float16] | 0.7208 | 0.4714 | 65.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4x2048-bfloat16] | 0.4165 | 0.2724 | 65.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-32x8192-float16] | 2.7688 | 1.8176 | 65.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-16x8192-float16] | 2.7817 | 1.8291 | 65.8% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[context-chunk-bfloat16] | 0.3196 | 0.2108 | 66.0% | deepgemm |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-32768-float16] | 3.2761 | 2.1623 | 66.0% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-32768-bfloat16] | 3.2745 | 2.1628 | 66.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x8192-float16] | 2.7724 | 1.8334 | 66.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-16x8192-bfloat16] | 4.1370 | 2.7409 | 66.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x8192-float16] | 1.3944 | 0.9253 | 66.4% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-o-proj-m128-s1-float8_e4m3fn-bfloat16] | 0.0926 | 0.0615 | 66.4% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x8192-float16] | 1.3894 | 0.9240 | 66.5% | flashinfer |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[ds-v3-t512] | 0.0119 | 0.0079 | 66.6% | vllm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-4x2048-float16] | 0.2200 | 0.1465 | 66.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-32x8192-bfloat16] | 8.1779 | 5.4543 | 66.7% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-a-m4096-s1-float8_e4m3fn-bfloat16] | 0.0866 | 0.0578 | 66.8% | deepgemm |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp2-4096-bfloat16] | 0.5531 | 0.3698 | 66.9% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-16x8192-bfloat16] | 1.3901 | 0.9316 | 67.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-16x8192-bfloat16] | 5.4695 | 3.6694 | 67.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-4x2048-float16] | 0.2141 | 0.1437 | 67.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-32x8192-bfloat16] | 10.8675 | 7.3034 | 67.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-16x8192-bfloat16] | 2.7422 | 1.8430 | 67.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-32x8192-bfloat16] | 5.4559 | 3.6676 | 67.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x8192-bfloat16] | 1.3858 | 0.9339 | 67.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-32x8192-bfloat16] | 5.4221 | 3.6646 | 67.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-16x8192-bfloat16] | 2.7268 | 1.8432 | 67.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4x2048-float16] | 0.4015 | 0.2716 | 67.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-32x8192-bfloat16] | 2.7157 | 1.8386 | 67.7% | flashinfer |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[ds-v32-kv4k-bfloat16] | 0.5131 | 0.3476 | 67.8% | flashmla |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-kscale-float8_e4m3fn] | 0.4711 | 0.3199 | 67.9% | deepgemm |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t4096] | 0.0377 | 0.0257 | 68.1% | vllm |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-q-b-m128-s128-float8_e4m3fn-bfloat16] | 0.0281 | 0.0191 | 68.1% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-16x8192-float16] | 3.9979 | 2.7294 | 68.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-32x8192-float16] | 7.9196 | 5.4286 | 68.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-16x8192-float16] | 5.3067 | 3.6472 | 68.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-16x8192-float16] | 1.3428 | 0.9230 | 68.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-32x8192-float16] | 2.6412 | 1.8226 | 69.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-16x8192-float16] | 2.6569 | 1.8339 | 69.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-32x8192-float16] | 5.2679 | 3.6451 | 69.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-32x8192-float16] | 10.4822 | 7.2655 | 69.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x8192-float16] | 1.3381 | 0.9278 | 69.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-16x8192-float16] | 2.6480 | 1.8368 | 69.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-32x8192-float16] | 5.2369 | 3.6382 | 69.5% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-16384-float16] | 1.5757 | 1.0960 | 69.6% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-16384-bfloat16] | 1.5767 | 1.0995 | 69.7% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-serving-batch-float16] | 0.0884 | 0.0619 | 70.0% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-8192-bfloat16] | 0.8047 | 0.5637 | 70.0% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-o-proj-float8_e4m3fn-bfloat16] | 1.5488 | 1.0859 | 70.1% | deepgemm |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-8192-float16] | 0.8057 | 0.5654 | 70.2% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-serving-batch-bfloat16] | 0.0883 | 0.0620 | 70.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-32x8192-bfloat16] | 5.2103 | 3.6652 | 70.3% | flashinfer |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-float16-float8_e4m3fn] | 1.9651 | 1.3954 | 71.0% | fa3 |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-o-proj-m128-s128-float8_e4m3fn-bfloat16] | 0.0664 | 0.0472 | 71.1% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-4096-bfloat16] | 0.4167 | 0.2972 | 71.3% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-4096-float16] | 0.4171 | 0.2992 | 71.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-32x8192-float16] | 5.0710 | 3.6446 | 71.9% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-float8_e4m3fn] | 0.5146 | 0.3703 | 72.0% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-bfloat16] | 0.5283 | 0.3832 | 72.5% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4096-4096-bfloat16] | 0.3369 | 0.2444 | 72.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x1024-bfloat16] | 0.3194 | 0.2370 | 74.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4096-4096-float16] | 0.3260 | 0.2431 | 74.6% | flashinfer |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[falcon-7b-2k-bfloat16] | 0.0371 | 0.0277 | 74.7% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x1024-bfloat16] | 0.1170 | 0.0880 | 75.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x1024-bfloat16] | 0.4109 | 0.3093 | 75.3% | flashinfer |
| 🔴 | **DeltaNetChunkBwdOp** | test_deltanet_vs_fla_bwd[deltanet-1.3b-train-bfloat16] | 0.0719 | 0.0543 | 75.6% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x1024-bfloat16] | 0.2195 | 0.1662 | 75.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x1024-bfloat16] | 0.2160 | 0.1637 | 75.8% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-4k-bfloat16] | 0.1171 | 0.0894 | 76.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x1024-float16] | 0.3082 | 0.2364 | 76.7% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-4k-float16] | 0.1179 | 0.0907 | 76.9% | flashinfer |
| 🔴 | **GLAChunkFwdOp** | test_gla_chunk_fwd_bench[train-16k-float16] | 0.6163 | 0.4750 | 77.1% | fla |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[qwen3-235b-t32] | 0.0070 | 0.0054 | 77.2% | vllm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x1024-float16] | 0.1128 | 0.0872 | 77.3% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b64-bfloat16] | 0.1288 | 0.1007 | 78.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x1024-float16] | 0.3944 | 0.3086 | 78.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x1024-float16] | 0.2122 | 0.1661 | 78.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x1024-float16] | 0.2080 | 0.1635 | 78.6% | flashinfer |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 0.5647 | 0.4451 | 78.8% | fa3 |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.5656 | 0.4458 | 78.8% | fa3 |
| 🔴 | **DeltaNetChunkBwdOp** | test_deltanet_vs_fla_bwd[train-4k-float16] | 0.2725 | 0.2154 | 79.0% | fla |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b64-float16] | 0.1295 | 0.1025 | 79.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4x2048-bfloat16] | 0.3314 | 0.2632 | 79.4% | flashinfer |
| 🔴 | **GLAChunkFwdOp** | test_gla_chunk_fwd_bench[train-4k-float16] | 0.1567 | 0.1246 | 79.5% | fla |
| 🔴 | **DeltaNetChunkBwdOp** | test_deltanet_vs_fla_bwd[train-4k-bfloat16] | 0.2721 | 0.2170 | 79.8% | fla |
| 🔴 | **GLAChunkFwdOp** | test_gla_chunk_fwd_bench[train-2k-bfloat16] | 0.0935 | 0.0747 | 79.9% | fla |

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
