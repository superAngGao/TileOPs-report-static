# ✅ TileOPs Nightly Report

> **2026-10-10 20:15** &ensp;|&ensp; `c3146365` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Operators** | 188 |
| **Kernels** | 302 |
| **Specs** | 17 |
| **Workloads** | 1220 |
| **Correctness** | ✅ &ensp; (188/188 ops verified, 1031/1031 tests) |
| **Benchmarked Ops** | 189 |
| **Benchmark Failures** | ✅ None &ensp;|&ensp; ⚠️ 1 skipped |
| **Regressions** (vs 14-day median) | ✅ None |
| **Baseline Alerts** (< 80%) | ⚠️ 163 |
| **vs Baseline** | ↑ 1514 &ensp;·&ensp; ↓ 422 &ensp;/&ensp; 1936 rows |
| **Rows no reference checked** | ⚠️ 165 |
| **History window** | 14 runs, 2026-09-26 to 2026-10-09 |
| **Roofline anomalies** | ✅ None |
| **Improvements** (vs 14-day best) | 🎉 31 |
| **Moved since previous run** | 🔵 31 |
| **Never-built kernels** | ⚠️ 41 files **+3** &ensp;·&ensp; `kernels/linear_attention/gdn/prefill_forward.py` at 3.4% |
| **Untested roofline math** | 422 lines in `perf/` &ensp;·&ensp; `perf/formulas.py` at 17.4% |
| **Untested op logic** | 924 lines in `ops/` &ensp;·&ensp; 57.4% of branches taken |
| | <sub>coverage compared against the 2026-10-09 run; no figure means it held</sub> |

## 🎉 Performance Improvements (vs 14-day best)

| Op | Config | Prev Best (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-long-context-float16] | 12.5206 | 0.4032 | -96.8% | 85.23 |
| **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-long-context-bfloat16] | 12.5197 | 0.4055 | -96.8% | 84.74 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h128-kv64k-bfloat16] | 32.8859 | 2.1780 | -93.4% | 506.17 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h128-kv48k-bfloat16] | 31.9302 | 2.1655 | -93.2% | 509.09 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h128-kv32k-bfloat16] | 30.1569 | 2.1256 | -93.0% | 518.67 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h64-kv64k-bfloat16] | 8.5106 | 0.6704 | -92.1% | 411.24 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h64-kv48k-bfloat16] | 8.2424 | 0.6578 | -92.0% | 419.10 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h64-kv32k-bfloat16] | 7.7567 | 0.6448 | -91.7% | 427.57 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h128-kv8k-bfloat16] | 24.7171 | 2.0767 | -91.6% | 530.86 |
| **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-ragged-bfloat16] | 0.9116 | 0.0821 | -91.0% | 55.65 |
| **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-ragged-float16] | 0.9147 | 0.0830 | -90.9% | 55.06 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h64-kv8k-bfloat16] | 6.3294 | 0.6190 | -90.2% | 445.34 |
| **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-8x1k-bfloat16] | 0.5203 | 0.0805 | -84.5% | 26.71 |
| **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-4x1k-bfloat16] | 0.2738 | 0.0434 | -84.2% | 24.78 |
| **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-8x1k-float16] | 0.4957 | 0.0792 | -84.0% | 27.15 |
| **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-4x1k-float16] | 0.2606 | 0.0430 | -83.5% | 25.01 |
| **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-wide-gqa-float16] | 0.5228 | 0.1206 | -76.9% | 35.63 |
| **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-wide-gqa-bfloat16] | 0.5243 | 0.1221 | -76.7% | 35.19 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv128k-bfloat16] | 9.9291 | 4.2779 | -56.9% | 547.49 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv96k-bfloat16] | 9.8443 | 4.2533 | -56.8% | 550.66 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv64k-bfloat16] | 9.6644 | 4.2331 | -56.2% | 553.29 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv32k-bfloat16] | 8.8224 | 4.1388 | -53.1% | 565.89 |
| **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[qwen3-ragged-odd-bfloat16-bfloat16] | 0.4004 | 0.1972 | -50.7% | 304.38 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv8k-bfloat16] | 7.9635 | 4.0575 | -49.0% | 577.23 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[ds-v32-kv2k-bfloat16] | 1.9059 | 1.0902 | -42.8% | 402.70 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[ds-v32-kv2k-float16] | 1.9078 | 1.0933 | -42.7% | 401.57 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[ds-v32-kv4k-bfloat16] | 0.5122 | 0.3104 | -39.4% | 353.53 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[ds-v32-kv4k-float16] | 0.5130 | 0.3130 | -39.0% | 350.58 |
| **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-float16-float16] | 0.7720 | 0.4806 | -37.7% | 541.50 |
| **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-noncausal-float16-float16] | 0.0226 | 0.0163 | -27.8% | 136.84 |
| **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-serving-step-float16-float16] | 0.3067 | 0.2619 | -14.6% | 239.64 |

## 🔵 Moved Since Previous Run

> Moves against the most recent reading. A row restored to its old level appears only here: returning is not a new 14-day record.

| Op | Config | Previous (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-long-context-float16] | 12.5206 | 0.4032 | -96.8% | 85.23 |
| **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-long-context-bfloat16] | 12.5271 | 0.4055 | -96.8% | 84.74 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h128-kv64k-bfloat16] | 32.9592 | 2.1780 | -93.4% | 506.17 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h128-kv48k-bfloat16] | 31.9772 | 2.1655 | -93.2% | 509.09 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h128-kv32k-bfloat16] | 30.2054 | 2.1256 | -93.0% | 518.67 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h64-kv64k-bfloat16] | 8.5158 | 0.6704 | -92.1% | 411.24 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h64-kv48k-bfloat16] | 8.2438 | 0.6578 | -92.0% | 419.10 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h64-kv32k-bfloat16] | 7.7582 | 0.6448 | -91.7% | 427.57 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h128-kv8k-bfloat16] | 24.7482 | 2.0767 | -91.6% | 530.86 |
| **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-ragged-bfloat16] | 0.9165 | 0.0821 | -91.0% | 55.65 |
| **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-ragged-float16] | 0.9159 | 0.0830 | -90.9% | 55.06 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h64-kv8k-bfloat16] | 6.3331 | 0.6190 | -90.2% | 445.34 |
| **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-8x1k-float16] | 0.5201 | 0.0792 | -84.8% | 27.15 |
| **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-8x1k-bfloat16] | 0.5208 | 0.0805 | -84.5% | 26.71 |
| **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-4x1k-float16] | 0.2742 | 0.0430 | -84.3% | 25.01 |
| **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-4x1k-bfloat16] | 0.2738 | 0.0434 | -84.2% | 24.78 |
| **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-wide-gqa-float16] | 0.5231 | 0.1206 | -76.9% | 35.63 |
| **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-wide-gqa-bfloat16] | 0.5255 | 0.1221 | -76.8% | 35.19 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv128k-bfloat16] | 9.9528 | 4.2779 | -57.0% | 547.49 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv96k-bfloat16] | 9.8443 | 4.2533 | -56.8% | 550.66 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv64k-bfloat16] | 9.6711 | 4.2331 | -56.2% | 553.29 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv32k-bfloat16] | 8.8362 | 4.1388 | -53.2% | 565.89 |
| **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[qwen3-ragged-odd-bfloat16-bfloat16] | 0.4004 | 0.1972 | -50.7% | 304.38 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv8k-bfloat16] | 7.9757 | 4.0575 | -49.1% | 577.23 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[ds-v32-kv2k-bfloat16] | 1.9065 | 1.0902 | -42.8% | 402.70 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[ds-v32-kv2k-float16] | 1.9108 | 1.0933 | -42.8% | 401.57 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[ds-v32-kv4k-bfloat16] | 0.5131 | 0.3104 | -39.5% | 353.53 |
| **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[ds-v32-kv4k-float16] | 0.5131 | 0.3130 | -39.0% | 350.58 |
| **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-float16-float16] | 0.7720 | 0.4806 | -37.7% | 541.50 |
| **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-noncausal-float16-float16] | 0.0226 | 0.0163 | -28.0% | 136.84 |
| **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-serving-step-float16-float16] | 0.3067 | 0.2619 | -14.6% | 239.64 |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 80%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-32k-bfloat16] | 0.3928 | 0.0876 | 22.3% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[ds-v32-decode-b1-float8_e4m3fn] | 0.2865 | 0.0656 | 22.9% | torch-ref |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-mixed-float16] | 22.3820 | 5.1808 | 23.2% | fa3 |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-rope-float16] | 42.0287 | 14.1332 | 33.6% | fa3 |
| 🔴 | **TopKSelectFwdOp** | test_topk_select_bench[ds-v32-topk-decode-b1] | 0.0635 | 0.0217 | 34.1% | flashinfer |
| 🔴 | **NSACompressedVarlenFwdOp** | test_nsa_compressed_fwd_varlen_bench[prefill-4x1k-float16] | 0.1459 | 0.0534 | 36.6% | fla |
| 🔴 | **NSACompressedVarlenFwdOp** | test_nsa_compressed_fwd_varlen_bench[prefill-8x1k-float16] | 0.2712 | 0.1005 | 37.1% | fla |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-32k-bfloat16] | 0.3935 | 0.1595 | 40.5% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-32k-float16] | 0.3938 | 0.1609 | 40.9% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-single-request-float16] | 0.0552 | 0.0227 | 41.1% | flashinfer |

<details>
<summary><strong>153 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-rope-float16] | 1.6627 | 0.6885 | 41.4% | fa3 |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-single-request-bfloat16] | 0.0552 | 0.0228 | 41.4% | flashinfer |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-float16-float8_e4m3fn] | 56.1881 | 23.3475 | 41.5% | fa3 |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b1-float16] | 0.0558 | 0.0233 | 41.8% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b2-float16] | 0.0567 | 0.0237 | 41.8% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b1-bfloat16] | 0.0558 | 0.0234 | 41.9% | flashinfer |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t32] | 0.0137 | 0.0058 | 42.0% | vllm |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b2-bfloat16] | 0.0566 | 0.0238 | 42.1% | flashinfer |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t1] | 0.0121 | 0.0051 | 42.3% | vllm |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b6-float16] | 0.0611 | 0.0267 | 43.6% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b6-bfloat16] | 0.0612 | 0.0268 | 43.9% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-b-m4096-s128-float8_e4m3fn-bfloat16] | 0.3375 | 0.1515 | 44.9% | deepgemm |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-65536-bfloat16] | 5.9570 | 2.6856 | 45.1% | fla |
| 🔴 | **NSACompressedVarlenFwdOp** | test_nsa_compressed_fwd_varlen_bench[prefill-ragged-bfloat16] | 0.0397 | 0.0180 | 45.3% | fla |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-16384-bfloat16] | 1.5238 | 0.6938 | 45.5% | fla |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t512] | 0.0158 | 0.0078 | 49.1% | vllm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx131072-float8_e4m3fn] | 17.2834 | 8.9700 | 51.9% | deepgemm |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-1024-7168-bfloat16] | 0.6780 | 0.3548 | 52.3% | fla |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx65536-float8_e4m3fn] | 8.5293 | 4.4654 | 52.3% | deepgemm |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-4096-bfloat16] | 0.3836 | 0.2014 | 52.5% | fla |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx131072-float8_e4m3fn] | 8.6867 | 4.5847 | 52.8% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx65536-float8_e4m3fn] | 4.3260 | 2.2913 | 53.0% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx32768-float8_e4m3fn] | 4.1160 | 2.1930 | 53.3% | deepgemm |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[ds-v3-t1] | 0.0096 | 0.0052 | 53.7% | vllm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx32768-float8_e4m3fn] | 2.1269 | 1.1457 | 53.9% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx16384-float8_e4m3fn] | 1.9373 | 1.0513 | 54.3% | deepgemm |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp4-65536-bfloat16] | 6.5882 | 3.5989 | 54.6% | fla |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx16384-float8_e4m3fn] | 1.0402 | 0.5690 | 54.7% | deepgemm |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp4-16384-bfloat16] | 1.6785 | 0.9272 | 55.2% | fla |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx8192-float8_e4m3fn] | 0.8631 | 0.4794 | 55.5% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx8192-float8_e4m3fn] | 0.5027 | 0.2800 | 55.7% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-4x2048-bfloat16] | 0.2550 | 0.1431 | 56.1% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx4096-float8_e4m3fn] | 0.2332 | 0.1316 | 56.4% | deepgemm |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[gemma-2b-bfloat16] | 0.3014 | 0.1702 | 56.5% | fa3 |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[ds-v3-t32] | 0.0100 | 0.0056 | 56.6% | vllm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-16x8192-bfloat16] | 0.8199 | 0.4682 | 57.1% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-a-m4096-s128-float8_e4m3fn-bfloat16] | 0.0749 | 0.0432 | 57.7% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-4x2048-float16] | 0.2474 | 0.1430 | 57.8% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx4096-float8_e4m3fn] | 0.3271 | 0.1895 | 57.9% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x8192-bfloat16] | 0.8068 | 0.4680 | 58.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-16x8192-float16] | 0.7963 | 0.4673 | 58.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x8192-float16] | 0.7807 | 0.4663 | 59.7% | flashinfer |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp4-4096-bfloat16] | 0.4344 | 0.2627 | 60.5% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4096-4096-bfloat16] | 0.4176 | 0.2534 | 60.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x1024-bfloat16] | 0.1414 | 0.0866 | 61.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4096-4096-float16] | 0.4034 | 0.2514 | 62.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x1024-float16] | 0.1373 | 0.0859 | 62.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x1024-bfloat16] | 0.2601 | 0.1631 | 62.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-16x8192-bfloat16] | 1.4564 | 0.9240 | 63.4% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-a-m128-s128-float8_e4m3fn-bfloat16] | 0.0208 | 0.0132 | 63.5% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-32x8192-bfloat16] | 1.4498 | 0.9212 | 63.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x8192-bfloat16] | 2.1807 | 1.3881 | 63.6% | flashinfer |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp2-65536-bfloat16] | 8.4207 | 5.3732 | 63.8% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x8192-bfloat16] | 0.7425 | 0.4742 | 63.9% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-mlp-up-m128-s128-float8_e4m3fn-bfloat16] | 0.0271 | 0.0173 | 63.9% | deepgemm |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[starcoder-float16] | 0.7878 | 0.5048 | 64.1% | fa3 |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp2-16384-bfloat16] | 2.1508 | 1.3791 | 64.1% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-16x8192-bfloat16] | 2.8733 | 1.8429 | 64.1% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-b-m128-s128-float8_e4m3fn-bfloat16] | 0.0183 | 0.0118 | 64.2% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-32x8192-bfloat16] | 2.8494 | 1.8328 | 64.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-4x2048-bfloat16] | 0.2282 | 0.1468 | 64.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x1024-float16] | 0.2522 | 0.1627 | 64.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x8192-bfloat16] | 2.8551 | 1.8472 | 64.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x8192-bfloat16] | 1.4362 | 0.9294 | 64.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-32x8192-float16] | 1.4155 | 0.9170 | 64.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x8192-float16] | 2.1175 | 1.3737 | 64.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-4x2048-bfloat16] | 0.2221 | 0.1444 | 65.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x8192-bfloat16] | 1.4337 | 0.9321 | 65.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-16x8192-float16] | 1.4118 | 0.9183 | 65.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x8192-float16] | 0.7232 | 0.4717 | 65.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4x2048-bfloat16] | 0.4161 | 0.2723 | 65.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-16x8192-float16] | 2.7816 | 1.8305 | 65.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-32x8192-float16] | 2.7628 | 1.8207 | 65.9% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[context-chunk-bfloat16] | 0.3202 | 0.2111 | 65.9% | deepgemm |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-32768-float16] | 3.2775 | 2.1634 | 66.0% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-32768-bfloat16] | 3.2745 | 2.1654 | 66.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x8192-float16] | 2.7731 | 1.8355 | 66.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-16x8192-bfloat16] | 4.1399 | 2.7401 | 66.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-4x2048-float16] | 0.2207 | 0.1463 | 66.3% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-o-proj-m128-s1-float8_e4m3fn-bfloat16] | 0.0927 | 0.0616 | 66.5% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x8192-float16] | 1.3873 | 0.9229 | 66.5% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-a-m4096-s1-float8_e4m3fn-bfloat16] | 0.0869 | 0.0579 | 66.5% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x8192-float16] | 1.3926 | 0.9276 | 66.6% | flashinfer |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[ds-v3-t512] | 0.0119 | 0.0079 | 66.7% | vllm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-32x8192-bfloat16] | 8.1807 | 5.4598 | 66.7% | flashinfer |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp2-4096-bfloat16] | 0.5537 | 0.3700 | 66.8% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-16x8192-bfloat16] | 5.4729 | 3.6726 | 67.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-16x8192-bfloat16] | 1.3873 | 0.9315 | 67.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-32x8192-bfloat16] | 10.8796 | 7.3083 | 67.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-4x2048-float16] | 0.2142 | 0.1441 | 67.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-32x8192-bfloat16] | 5.4489 | 3.6664 | 67.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4x2048-float16] | 0.4027 | 0.2713 | 67.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-16x8192-bfloat16] | 2.7377 | 1.8467 | 67.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-32x8192-bfloat16] | 5.4137 | 3.6648 | 67.7% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-kscale-float8_e4m3fn] | 0.4712 | 0.3196 | 67.8% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-32x8192-bfloat16] | 2.7087 | 1.8386 | 67.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x8192-bfloat16] | 1.3797 | 0.9365 | 67.9% | flashinfer |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t4096] | 0.0378 | 0.0257 | 68.0% | vllm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-16x8192-bfloat16] | 2.7224 | 1.8504 | 68.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-16x8192-float16] | 4.0043 | 2.7279 | 68.1% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-q-b-m128-s128-float8_e4m3fn-bfloat16] | 0.0281 | 0.0192 | 68.2% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-32x8192-float16] | 7.9163 | 5.4189 | 68.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-16x8192-float16] | 5.3153 | 3.6460 | 68.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-16x8192-float16] | 1.3419 | 0.9243 | 68.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-32x8192-float16] | 5.2677 | 3.6414 | 69.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-16x8192-float16] | 2.6503 | 1.8350 | 69.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x8192-float16] | 1.3411 | 0.9286 | 69.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-32x8192-float16] | 10.4829 | 7.2675 | 69.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-32x8192-float16] | 2.6309 | 1.8252 | 69.4% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-16384-bfloat16] | 1.5750 | 1.0928 | 69.4% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-16384-float16] | 1.5759 | 1.0938 | 69.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-16x8192-float16] | 2.6473 | 1.8391 | 69.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-32x8192-float16] | 5.2330 | 3.6425 | 69.6% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-serving-batch-float16] | 0.0885 | 0.0620 | 70.0% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-8192-float16] | 0.8032 | 0.5630 | 70.1% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-o-proj-float8_e4m3fn-bfloat16] | 1.5449 | 1.0843 | 70.2% | deepgemm |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-serving-batch-bfloat16] | 0.0883 | 0.0620 | 70.2% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-8192-bfloat16] | 0.8026 | 0.5637 | 70.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-32x8192-bfloat16] | 5.2191 | 3.6705 | 70.3% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-o-proj-m128-s128-float8_e4m3fn-bfloat16] | 0.0664 | 0.0470 | 70.8% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-float16-float8_e4m3fn] | 1.9674 | 1.3971 | 71.0% | fa3 |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-4096-bfloat16] | 0.4166 | 0.2965 | 71.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-32x8192-float16] | 5.0676 | 3.6467 | 72.0% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-4096-float16] | 0.4168 | 0.3000 | 72.0% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-float8_e4m3fn] | 0.5141 | 0.3714 | 72.2% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-bfloat16] | 0.5285 | 0.3835 | 72.6% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4096-4096-bfloat16] | 0.3367 | 0.2445 | 72.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x1024-bfloat16] | 0.3195 | 0.2374 | 74.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4096-4096-float16] | 0.3260 | 0.2431 | 74.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x1024-bfloat16] | 0.1170 | 0.0881 | 75.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x1024-bfloat16] | 0.4107 | 0.3101 | 75.5% | flashinfer |
| 🔴 | **DeltaNetChunkBwdOp** | test_deltanet_vs_fla_bwd[deltanet-1.3b-train-bfloat16] | 0.0717 | 0.0544 | 75.8% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x1024-bfloat16] | 0.2201 | 0.1671 | 75.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x1024-bfloat16] | 0.2156 | 0.1641 | 76.1% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-4k-bfloat16] | 0.1173 | 0.0893 | 76.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x1024-float16] | 0.3080 | 0.2360 | 76.6% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-4k-float16] | 0.1179 | 0.0904 | 76.7% | flashinfer |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[qwen3-235b-t32] | 0.0070 | 0.0054 | 77.2% | vllm |
| 🔴 | **GLAChunkFwdOp** | test_gla_chunk_fwd_bench[train-16k-float16] | 0.6158 | 0.4754 | 77.2% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x1024-float16] | 0.1124 | 0.0874 | 77.8% | flashinfer |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[falcon-7b-2k-bfloat16] | 0.0370 | 0.0288 | 77.8% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x1024-float16] | 0.3953 | 0.3087 | 78.1% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b64-bfloat16] | 0.1290 | 0.1010 | 78.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x1024-float16] | 0.2124 | 0.1667 | 78.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x1024-float16] | 0.2080 | 0.1634 | 78.5% | flashinfer |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 0.5637 | 0.4439 | 78.7% | fa3 |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.5652 | 0.4462 | 78.9% | fa3 |
| 🔴 | **DeltaNetChunkBwdOp** | test_deltanet_vs_fla_bwd[train-4k-float16] | 0.2728 | 0.2155 | 79.0% | fla |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b64-float16] | 0.1298 | 0.1029 | 79.3% | flashinfer |
| 🔴 | **GLAChunkFwdOp** | test_gla_chunk_fwd_bench[train-4k-float16] | 0.1566 | 0.1242 | 79.3% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4x2048-bfloat16] | 0.3319 | 0.2634 | 79.4% | flashinfer |
| 🔴 | **DeltaNetChunkBwdOp** | test_deltanet_vs_fla_bwd[train-4k-bfloat16] | 0.2719 | 0.2165 | 79.6% | fla |
| 🔴 | **GLAChunkFwdOp** | test_gla_chunk_fwd_bench[train-2k-bfloat16] | 0.0937 | 0.0748 | 79.8% | fla |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 41 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
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
| `kernels/linear_attention/kda/chunk_programs.py` | 5.3% |
| `kernels/linear_attention/deltanet/prefill_prepare.py` | 5.7% |
| `kernels/sampling/top_k_top_p_mask.py` | 6.5% |
| `kernels/attention/gqa/prefill_paged_kv_append.py` | 6.9% |
| `kernels/attention/gqa/dense_fp8.py` | 7.0% |
| `kernels/linear_attention/delta_decode.py` | 7.8% |
| `kernels/attention/gqa/varlen_fp8.py` | 9.8% |
| `kernels/attention/mla/decode.py` | 9.9% |
| `kernels/attention/gqa/dense.py` | 10.5% |
| `kernels/sampling/top_k_mask.py` | 10.8% |
| `kernels/sampling/sampling_from_probs.py` | 11.8% |
| `kernels/sampling/chain_speculative_sampling.py` | 11.8% |
| `kernels/sampling/top_p_mask.py` | 12.4% |
| `kernels/quantization/int8_quant_per_tensor.py` | 12.9% |
| `kernels/linear_attention/gla/varlen_prefill.py` | 13.4% |
| `kernels/attention/gqa/paged_ws.py` | 13.5% |
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
| `kernels/attention/dsa/decode.py` | 19.2% |
| `kernels/sampling/min_p_mask.py` | 19.7% |
| `kernels/attention/nsa/compressed_varlen.py` | 20.0% |
| `kernels/quantization/fp8_quant_per_block.py` | 22.6% |
| `kernels/norm/rms_norm_on_chip.py` | 22.7% |
| `kernels/sampling/radix_select.py` | 24.1% |
| `kernels/linear_attention/gla/dense_decode.py` | 24.3% |
| `kernels/linear_attention/gdn/prefill.py` | 24.4% |
| `kernels/linear_attention/kda/prefill.py` | 24.5% |

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
