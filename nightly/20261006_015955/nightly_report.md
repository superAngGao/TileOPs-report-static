# ❌ TileOPs Nightly Report

> **2026-10-05 19:43** &ensp;|&ensp; `b3600b1b` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Operators** | 188 |
| **Kernels** | 288 |
| **Specs** | 17 |
| **Workloads** | 1220 |
| **Correctness** | ✅ &ensp; (188/188 ops verified, 1009/1009 tests) |
| **Benchmarked Ops** | 189 |
| **Benchmark Failures** | ✅ None &ensp;|&ensp; ⚠️ 1 skipped |
| **Regressions** (vs 14-day median) | ⚠️ 1 |
| **Baseline Alerts** (< 80%) | ⚠️ 218 |
| **vs Baseline** | ↑ 1421 &ensp;·&ensp; ↓ 507 &ensp;/&ensp; 1928 rows |
| **Rows no reference checked** | ⚠️ 165 |
| **History window** | 15 runs, 2026-09-21 to 2026-10-05 |
| **Roofline anomalies** | ✅ None |
| **Never-built kernels** | ⚠️ 34 files **−1** &ensp;·&ensp; `kernels/linear_attention/gdn/prefill_prepare.py` at 3.4% |
| **Untested roofline math** | 422 lines in `perf/` &ensp;·&ensp; `perf/formulas.py` at 17.4% |
| **Untested op logic** | 925 lines in `ops/` **+10** &ensp;·&ensp; 57.1% of branches taken **−2.7pp** |
| | <sub>coverage compared against the 2026-10-05 run; no figure means it held</sub> |

## ⚠️ Performance Regressions (vs 14-day median)

| Op | Config | Median (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **DeltaNetInferenceFwdOp** | test_deltanet_inference_bench[prefill-8k-bfloat16] | 0.0774 | 0.0854 | +10.4% | 18.96 |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 80%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h128-kv64k-bfloat16] | 32.9482 | 2.4076 | 7.3% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h128-kv48k-bfloat16] | 31.9762 | 2.4004 | 7.5% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h128-kv32k-bfloat16] | 30.1786 | 2.3864 | 7.9% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h64-kv64k-bfloat16] | 8.5209 | 0.7285 | 8.6% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h64-kv48k-bfloat16] | 8.2424 | 0.7205 | 8.7% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h64-kv32k-bfloat16] | 7.7618 | 0.7120 | 9.2% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h128-kv8k-bfloat16] | 24.7171 | 2.3511 | 9.5% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h64-kv8k-bfloat16] | 6.3340 | 0.7001 | 11.1% | flashmla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-long-context-float16] | 12.5370 | 1.4450 | 11.5% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-long-context-bfloat16] | 12.5252 | 1.4462 | 11.6% | fla |

<details>
<summary><strong>208 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-ragged-float16] | 0.9153 | 0.1575 | 17.2% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-ragged-bfloat16] | 0.9173 | 0.1580 | 17.2% | fla |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-32k-bfloat16] | 0.3928 | 0.0873 | 22.2% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[ds-v32-decode-b1-float8_e4m3fn] | 0.2872 | 0.0659 | 22.9% | torch-ref |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-mixed-float16] | 22.3192 | 5.1856 | 23.2% | fa3 |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-131072-float16] | 9.3382 | 2.2453 | 24.0% | quack |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-131072-bfloat16] | 9.4143 | 2.3078 | 24.5% | quack |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-8x1k-float16] | 0.5204 | 0.1338 | 25.7% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-4x1k-float16] | 0.2741 | 0.0706 | 25.8% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-8x1k-bfloat16] | 0.5205 | 0.1343 | 25.8% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-4x1k-bfloat16] | 0.2743 | 0.0710 | 25.9% | fla |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-262144-float16] | 9.3354 | 2.4177 | 25.9% | quack |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-262144-bfloat16] | 9.4408 | 2.5126 | 26.6% | quack |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-wide-gqa-float16] | 0.5242 | 0.1613 | 30.8% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-wide-gqa-bfloat16] | 0.5257 | 0.1624 | 30.9% | fla |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-65536-float32] | 13.1651 | 4.3832 | 33.3% | quack |
| 🔴 | **TopKSelectFwdOp** | test_topk_select_bench[ds-v32-topk-decode-b1] | 0.0634 | 0.0213 | 33.6% | flashinfer |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-rope-float16] | 41.9307 | 14.2587 | 34.0% | fa3 |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-131072-float32] | 13.2189 | 4.7832 | 36.2% | quack |
| 🔴 | **NSACompressedVarlenFwdOp** | test_nsa_compressed_fwd_varlen_bench[prefill-4x1k-float16] | 0.1459 | 0.0536 | 36.7% | fla |
| 🔴 | **NSACompressedVarlenFwdOp** | test_nsa_compressed_fwd_varlen_bench[prefill-8x1k-float16] | 0.2712 | 0.1007 | 37.1% | fla |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-262144-float32] | 13.2109 | 4.9114 | 37.2% | quack |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-32k-bfloat16] | 0.3939 | 0.1589 | 40.4% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-32k-float16] | 0.3936 | 0.1603 | 40.7% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-single-request-float16] | 0.0552 | 0.0226 | 41.0% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-single-request-bfloat16] | 0.0552 | 0.0228 | 41.3% | flashinfer |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-rope-float16] | 1.6616 | 0.6869 | 41.3% | fa3 |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-float16-float8_e4m3fn] | 56.1646 | 23.3035 | 41.5% | fa3 |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b1-float16] | 0.0558 | 0.0234 | 41.9% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b2-float16] | 0.0567 | 0.0238 | 41.9% | flashinfer |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t32] | 0.0137 | 0.0058 | 42.0% | vllm |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b1-bfloat16] | 0.0557 | 0.0234 | 42.0% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b2-bfloat16] | 0.0566 | 0.0238 | 42.1% | flashinfer |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t1] | 0.0121 | 0.0051 | 42.2% | vllm |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-256-float16] | 0.0249 | 0.0108 | 43.4% | quack |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-256-bfloat16] | 0.0250 | 0.0109 | 43.7% | quack |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b6-float16] | 0.0611 | 0.0267 | 43.7% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b6-bfloat16] | 0.0612 | 0.0268 | 43.8% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-b-m4096-s128-float8_e4m3fn-bfloat16] | 0.3379 | 0.1511 | 44.7% | deepgemm |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-65536-bfloat16] | 5.9564 | 2.6795 | 45.0% | fla |
| 🔴 | **NSACompressedVarlenFwdOp** | test_nsa_compressed_fwd_varlen_bench[prefill-ragged-bfloat16] | 0.0396 | 0.0180 | 45.4% | fla |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-16384-bfloat16] | 1.5204 | 0.6941 | 45.6% | fla |
| 🔴 | **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[qwen3-ragged-odd-bfloat16-bfloat16] | 0.4005 | 0.1890 | 47.2% | fa3 |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv128k-bfloat16] | 9.9311 | 4.7592 | 47.9% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv96k-bfloat16] | 9.8572 | 4.7386 | 48.1% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv64k-bfloat16] | 9.6682 | 4.7017 | 48.6% | flashmla |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t512] | 0.0158 | 0.0078 | 49.1% | vllm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx131072-float8_e4m3fn] | 17.2825 | 8.9817 | 52.0% | deepgemm |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-1024-7168-bfloat16] | 0.6794 | 0.3531 | 52.0% | fla |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-4096-bfloat16] | 0.3845 | 0.2011 | 52.3% | fla |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx65536-float8_e4m3fn] | 8.5264 | 4.4744 | 52.5% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx131072-float8_e4m3fn] | 8.6979 | 4.5792 | 52.6% | deepgemm |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv32k-bfloat16] | 8.8224 | 4.6538 | 52.8% | flashmla |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx65536-float8_e4m3fn] | 4.3110 | 2.2833 | 53.0% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx32768-float8_e4m3fn] | 4.1235 | 2.1967 | 53.3% | deepgemm |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[ds-v3-t1] | 0.0096 | 0.0052 | 53.7% | vllm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx32768-float8_e4m3fn] | 2.1291 | 1.1483 | 53.9% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx16384-float8_e4m3fn] | 1.9402 | 1.0537 | 54.3% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx16384-float8_e4m3fn] | 1.0400 | 0.5684 | 54.6% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-4x2048-bfloat16] | 0.2595 | 0.1435 | 55.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-4x2048-float16] | 0.2580 | 0.1427 | 55.3% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx8192-float8_e4m3fn] | 0.8634 | 0.4776 | 55.3% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx8192-float8_e4m3fn] | 0.5022 | 0.2778 | 55.3% | deepgemm |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp4-16384-bfloat16] | 1.6759 | 0.9276 | 55.4% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-16x8192-bfloat16] | 0.8451 | 0.4689 | 55.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-16x8192-float16] | 0.8387 | 0.4656 | 55.5% | flashinfer |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp4-65536-bfloat16] | 6.4581 | 3.5983 | 55.7% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x8192-float16] | 0.8271 | 0.4649 | 56.2% | flashinfer |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[gemma-2b-bfloat16] | 0.3011 | 0.1694 | 56.2% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x8192-bfloat16] | 0.8309 | 0.4686 | 56.4% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx4096-float8_e4m3fn] | 0.2330 | 0.1314 | 56.4% | deepgemm |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[ds-v3-t32] | 0.0100 | 0.0056 | 56.6% | vllm |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-65536-bfloat16] | 3.9097 | 2.2301 | 57.0% | quack |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-65536-float16] | 3.7582 | 2.1656 | 57.6% | quack |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-a-m4096-s128-float8_e4m3fn-bfloat16] | 0.0748 | 0.0433 | 57.8% | deepgemm |
| 🔴 | **LayerNormFwdOp** | test_layer_norm_bench[dit-xl-2-bfloat16] | 0.0059 | 0.0034 | 58.2% | quack |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx4096-float8_e4m3fn] | 0.3282 | 0.1912 | 58.3% | deepgemm |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv8k-bfloat16] | 7.9649 | 4.6422 | 58.3% | flashmla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4096-4096-bfloat16] | 0.4309 | 0.2540 | 59.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4096-4096-float16] | 0.4266 | 0.2516 | 59.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x1024-float16] | 0.1443 | 0.0860 | 59.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x1024-bfloat16] | 0.1445 | 0.0864 | 59.8% | flashinfer |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp4-4096-bfloat16] | 0.4352 | 0.2637 | 60.6% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x8192-float16] | 2.2572 | 1.3735 | 60.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x1024-bfloat16] | 0.2665 | 0.1627 | 61.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x8192-bfloat16] | 2.2664 | 1.3836 | 61.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-16x8192-float16] | 1.5003 | 0.9178 | 61.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x8192-bfloat16] | 0.7740 | 0.4738 | 61.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x1024-float16] | 0.2656 | 0.1627 | 61.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-32x8192-bfloat16] | 1.5008 | 0.9230 | 61.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-16x8192-bfloat16] | 1.5037 | 0.9249 | 61.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-32x8192-float16] | 1.4929 | 0.9187 | 61.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-32x8192-bfloat16] | 2.9696 | 1.8305 | 61.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-16x8192-bfloat16] | 2.9862 | 1.8441 | 61.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x8192-float16] | 0.7635 | 0.4716 | 61.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-16x8192-float16] | 2.9549 | 1.8309 | 62.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x8192-bfloat16] | 1.4993 | 0.9306 | 62.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x8192-float16] | 2.9501 | 1.8325 | 62.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-32x8192-float16] | 2.9243 | 1.8225 | 62.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x8192-float16] | 1.4812 | 0.9234 | 62.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x8192-bfloat16] | 2.9542 | 1.8484 | 62.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x8192-float16] | 1.4737 | 0.9229 | 62.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-4x2048-bfloat16] | 0.2334 | 0.1472 | 63.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x8192-bfloat16] | 1.4806 | 0.9338 | 63.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-4x2048-float16] | 0.2324 | 0.1469 | 63.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-32x8192-float16] | 8.5426 | 5.4231 | 63.5% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-a-m128-s128-float8_e4m3fn-bfloat16] | 0.0208 | 0.0132 | 63.5% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-4x2048-float16] | 0.2261 | 0.1437 | 63.6% | flashinfer |
| 🔴 | **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-float16-float16] | 0.7961 | 0.5074 | 63.7% | fa3 |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-mlp-up-m128-s128-float8_e4m3fn-bfloat16] | 0.0271 | 0.0173 | 63.7% | deepgemm |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp2-65536-bfloat16] | 8.4219 | 5.3687 | 63.7% | fla |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[starcoder-float16] | 0.7883 | 0.5028 | 63.8% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-4x2048-bfloat16] | 0.2260 | 0.1444 | 63.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-16x8192-bfloat16] | 4.2923 | 2.7447 | 63.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4x2048-float16] | 0.4240 | 0.2713 | 64.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4x2048-bfloat16] | 0.4261 | 0.2726 | 64.0% | flashinfer |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp2-16384-bfloat16] | 2.1512 | 1.3793 | 64.1% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-32x8192-bfloat16] | 8.5052 | 5.4545 | 64.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-16x8192-float16] | 4.2497 | 2.7290 | 64.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-16x8192-bfloat16] | 2.8688 | 1.8435 | 64.3% | flashinfer |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[ds-v32-kv2k-bfloat16] | 1.9084 | 1.2300 | 64.5% | flashmla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-32x8192-bfloat16] | 11.3158 | 7.3005 | 64.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-16x8192-float16] | 1.4354 | 0.9264 | 64.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-16x8192-float16] | 5.6482 | 3.6458 | 64.5% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-b-m128-s128-float8_e4m3fn-bfloat16] | 0.0183 | 0.0118 | 64.7% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-16x8192-bfloat16] | 5.6772 | 3.6746 | 64.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-16x8192-bfloat16] | 1.4386 | 0.9320 | 64.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-32x8192-float16] | 5.6069 | 3.6370 | 64.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-32x8192-bfloat16] | 2.8271 | 1.8362 | 65.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-16x8192-float16] | 2.8161 | 1.8309 | 65.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-32x8192-bfloat16] | 5.6407 | 3.6679 | 65.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-32x8192-float16] | 5.5968 | 3.6411 | 65.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-16x8192-bfloat16] | 2.8386 | 1.8466 | 65.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x8192-float16] | 1.4233 | 0.9296 | 65.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x8192-bfloat16] | 1.4274 | 0.9326 | 65.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-32x8192-float16] | 11.1152 | 7.2667 | 65.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-32x8192-bfloat16] | 5.6065 | 3.6658 | 65.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-32x8192-float16] | 2.7910 | 1.8260 | 65.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-16x8192-float16] | 2.8044 | 1.8388 | 65.6% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-o-proj-m128-s1-float8_e4m3fn-bfloat16] | 0.0932 | 0.0614 | 65.9% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[context-chunk-bfloat16] | 0.3198 | 0.2111 | 66.0% | deepgemm |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-32768-bfloat16] | 3.2735 | 2.1639 | 66.1% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-32768-float16] | 3.2748 | 2.1684 | 66.2% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-a-m4096-s1-float8_e4m3fn-bfloat16] | 0.0870 | 0.0578 | 66.4% | deepgemm |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[attn-weights-32k-bfloat16] | 0.0567 | 0.0377 | 66.5% | quack |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[ds-v3-t512] | 0.0119 | 0.0079 | 66.7% | vllm |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-512-float16] | 0.0276 | 0.0184 | 66.7% | quack |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp2-4096-bfloat16] | 0.5533 | 0.3696 | 66.8% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-32x8192-bfloat16] | 5.4485 | 3.6712 | 67.4% | flashinfer |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-512-bfloat16] | 0.0273 | 0.0184 | 67.5% | quack |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-32x8192-float16] | 5.3999 | 3.6459 | 67.5% | flashinfer |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[ds-v32-kv4k-bfloat16] | 0.5124 | 0.3474 | 67.8% | flashmla |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-q-b-m128-s128-float8_e4m3fn-bfloat16] | 0.0283 | 0.0192 | 67.8% | deepgemm |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-256-float32] | 0.0266 | 0.0181 | 67.9% | torch-compile |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-32768-float16] | 1.5054 | 1.0229 | 68.0% | quack |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-kscale-float8_e4m3fn] | 0.4711 | 0.3202 | 68.0% | deepgemm |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t4096] | 0.0378 | 0.0257 | 68.0% | vllm |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-32768-bfloat16] | 1.5390 | 1.0614 | 69.0% | quack |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-16384-float16] | 1.5768 | 1.0953 | 69.5% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-16384-bfloat16] | 1.5751 | 1.0969 | 69.6% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-serving-batch-bfloat16] | 0.0883 | 0.0616 | 69.8% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-o-proj-float8_e4m3fn-bfloat16] | 1.5528 | 1.0850 | 69.9% | deepgemm |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-serving-batch-float16] | 0.0885 | 0.0621 | 70.2% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-8192-bfloat16] | 0.8035 | 0.5642 | 70.2% | flashinfer |
| 🔴 | **RMSNormFwdOp** | test_rms_norm_bench[quack-throughput-131072-float16] | 3.1324 | 2.2010 | 70.3% | quack |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-8192-float16] | 0.8045 | 0.5656 | 70.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4096-4096-bfloat16] | 0.3468 | 0.2443 | 70.4% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-o-proj-m128-s128-float8_e4m3fn-bfloat16] | 0.0664 | 0.0470 | 70.8% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4096-4096-float16] | 0.3434 | 0.2435 | 70.9% | flashinfer |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-float16-float8_e4m3fn] | 1.9667 | 1.3962 | 71.0% | fa3 |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-4096-bfloat16] | 0.4167 | 0.2969 | 71.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x1024-float16] | 0.3295 | 0.2357 | 71.5% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-4096-float16] | 0.4172 | 0.3005 | 72.0% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-float8_e4m3fn] | 0.5143 | 0.3707 | 72.1% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x1024-float16] | 0.1207 | 0.0871 | 72.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x1024-bfloat16] | 0.3285 | 0.2373 | 72.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x1024-bfloat16] | 0.1212 | 0.0879 | 72.5% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-bfloat16] | 0.5287 | 0.3833 | 72.5% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x1024-bfloat16] | 0.4247 | 0.3092 | 72.8% | flashinfer |
| 🔴 | **RMSNormFwdOp** | test_rms_norm_bench[quack-throughput-131072-bfloat16] | 3.1416 | 2.2885 | 72.8% | quack |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x1024-float16] | 0.4216 | 0.3082 | 73.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x1024-bfloat16] | 0.2233 | 0.1633 | 73.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x1024-bfloat16] | 0.2271 | 0.1664 | 73.3% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-qkv-a-2d-float8_e4m3fn-bfloat16] | 0.1529 | 0.1120 | 73.3% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x1024-float16] | 0.2228 | 0.1633 | 73.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x1024-float16] | 0.2255 | 0.1656 | 73.4% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-q-b-2d-float8_e4m3fn-bfloat16] | 0.3597 | 0.2652 | 73.7% | deepgemm |
| 🔴 | **RMSNormFwdOp** | test_rms_norm_bench[quack-throughput-262144-float16] | 3.1826 | 2.3899 | 75.1% | quack |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-down-2d-float8_e4m3fn-bfloat16] | 0.1444 | 0.1085 | 75.2% | deepgemm |
| 🔴 | **DeltaNetChunkBwdOp** | test_deltanet_vs_fla_bwd[deltanet-1.3b-train-bfloat16] | 0.0717 | 0.0542 | 75.7% | fla |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_decode_bench[falcon-7b-2k-bfloat16] | 0.0371 | 0.0282 | 76.1% | fa3 |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-4k-float16] | 0.1180 | 0.0905 | 76.6% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-4k-bfloat16] | 0.1173 | 0.0901 | 76.8% | flashinfer |
| 🔴 | **GLAChunkFwdOp** | test_gla_fwd_bench[train-16k-float16] | 0.6157 | 0.4756 | 77.3% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4x2048-float16] | 0.3386 | 0.2617 | 77.3% | flashinfer |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[qwen3-235b-t32] | 0.0070 | 0.0054 | 77.6% | vllm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4x2048-bfloat16] | 0.3380 | 0.2628 | 77.8% | flashinfer |
| 🔴 | **DeltaNetInferenceFwdOp** | test_deltanet_inference_bench[deltanet-1.3b-continue-bfloat16] | 0.0630 | 0.0491 | 78.0% | fla |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b64-bfloat16] | 0.1288 | 0.1008 | 78.3% | flashinfer |
| 🔴 | **RMSNormFwdOp** | test_rms_norm_bench[quack-throughput-262144-bfloat16] | 3.1840 | 2.4968 | 78.4% | quack |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.5657 | 0.4457 | 78.8% | fa3 |
| 🔴 | **DeltaNetChunkBwdOp** | test_deltanet_vs_fla_bwd[train-4k-float16] | 0.2729 | 0.2152 | 78.8% | fla |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 0.5647 | 0.4456 | 78.9% | fa3 |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-o-proj-2d-float8_e4m3fn-bfloat16] | 0.8705 | 0.6875 | 79.0% | deepgemm |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b64-float16] | 0.1295 | 0.1026 | 79.2% | flashinfer |
| 🔴 | **GLAChunkFwdOp** | test_gla_fwd_bench[train-4k-float16] | 0.1566 | 0.1247 | 79.6% | fla |
| 🔴 | **DeltaNetChunkBwdOp** | test_deltanet_vs_fla_bwd[train-4k-bfloat16] | 0.2721 | 0.2170 | 79.7% | fla |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-mlp-up-2d-float8_e4m3fn-bfloat16] | 0.2418 | 0.1929 | 79.8% | deepgemm |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 34 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 422 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 925 lines in `ops/`, 57.1% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 2600 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

### Never-built kernels

| File | Executed |
| --- | --- |
| `kernels/linear_attention/gdn/prefill_prepare.py` | 3.4% |
| `kernels/linear_attention/gdn/prefill_forward.py` | 3.4% |
| `kernels/linear_attention/kda/fused_program.py` | 5.2% |
| `kernels/linear_attention/kda/chunk_programs.py` | 5.9% |
| `kernels/sampling/top_k_top_p_mask.py` | 6.5% |
| `kernels/attention/gqa/dense_fp8.py` | 7.2% |
| `kernels/attention/gqa/prefill_paged_kv_append.py` | 7.7% |
| `kernels/linear_attention/delta_decode.py` | 7.8% |
| `kernels/attention/mla/decode.py` | 9.9% |
| `kernels/attention/gqa/varlen_fp8.py` | 10.0% |
| `kernels/attention/gqa/dense.py` | 10.5% |
| `kernels/sampling/top_k_mask.py` | 10.8% |
| `kernels/sampling/chain_speculative_sampling.py` | 11.4% |
| `kernels/sampling/sampling_from_probs.py` | 11.8% |
| `kernels/sampling/top_p_mask.py` | 12.4% |
| `kernels/quantization/int8_quant_per_tensor.py` | 12.8% |
| `kernels/linear_attention/gla/varlen_prefill.py` | 13.4% |
| `kernels/linear_attention/kda/decode_program.py` | 13.6% |
| `kernels/attention/gqa/decode_bs1.py` | 14.6% |
| `kernels/linear_attention/gla/dense_prefill_partitioned.py` | 16.1% |
| `kernels/quantization/int8_quant_per_block.py` | 16.1% |
| `kernels/quantization/int8_quant_per_channel.py` | 16.2% |
| `kernels/linear_attention/gla/varlen_prefill_partitioned.py` | 16.5% |
| `kernels/moe/indexed_expert_gemm.py` | 17.0% |
| `kernels/attention/varlen_rope.py` | 17.1% |
| `kernels/gemm/grouped/general.py` | 17.2% |
| `kernels/linear_attention/gla/dense_prefill_subchunk.py` | 17.3% |
| `kernels/attention/gqa/decode_fp8.py` | 17.8% |
| `kernels/sampling/min_p_mask.py` | 19.6% |
| `kernels/attention/nsa/compressed_varlen.py` | 20.0% |
| `kernels/quantization/fp8_quant_per_block.py` | 22.6% |
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
