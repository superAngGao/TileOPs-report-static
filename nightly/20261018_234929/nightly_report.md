# ✅ TileOPs Nightly Report

> **2026-10-18 21:40** &ensp;|&ensp; `57bd5446` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Operators** | 198 |
| **Kernels** | 325 |
| **Specs** | 7 |
| **Workloads** | 1392 |
| **Correctness** | ✅ &ensp; (198/198 ops verified, 1266/1303 tests) |
| **Benchmarked Ops** | 199 |
| **Benchmark Failures** | ✅ None &ensp;|&ensp; ⚠️ 1 skipped |
| **Regressions** (vs 14-day median) | ✅ None |
| **Baseline Alerts** (< 99%) | ⚠️ 213 |
| **vs Baseline** | ↑ 1897 &ensp;·&ensp; ↓ 213 &ensp;/&ensp; 2110 rows |
| **Rows no reference checked** | ⚠️ 190 |
| **History window** | not read |
| **Roofline anomalies** | ⚠️ 2 |
| **Never-built kernels** | ⚠️ 44 files &ensp;·&ensp; `kernels/linear_attention/gdn/prefill_forward.py` at 3.4% |
| **Untested roofline math** | 445 lines in `perf/` &ensp;·&ensp; `perf/formulas.py` at 16.2% |
| **Untested op logic** | 810 lines in `ops/` &ensp;·&ensp; 60.8% of branches taken |

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
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-32k-bfloat16] | 0.3927 | 0.0869 | 22.1% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[ds-v32-decode-b1-float8_e4m3fn] | 0.2890 | 0.0659 | 22.8% | torch-ref |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-mixed-float16] | 22.7224 | 5.1896 | 22.8% | fa3 |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-rope-float16] | 42.4050 | 14.0820 | 33.2% | fa3 |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-32k-bfloat16] | 0.3920 | 0.1592 | 40.6% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-32k-float16] | 0.3916 | 0.1601 | 40.9% | flashinfer |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-rope-float16] | 1.6769 | 0.6893 | 41.1% | fa3 |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-single-request-float16] | 0.0553 | 0.0228 | 41.2% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-single-request-bfloat16] | 0.0552 | 0.0228 | 41.3% | flashinfer |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-float16-float8_e4m3fn] | 56.5795 | 23.4845 | 41.5% | fa3 |

<details>
<summary><strong>203 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b1-float16] | 0.0551 | 0.0233 | 42.3% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b1-bfloat16] | 0.0552 | 0.0234 | 42.4% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b2-float16] | 0.0558 | 0.0238 | 42.7% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b2-bfloat16] | 0.0557 | 0.0239 | 42.8% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b6-float16] | 0.0609 | 0.0268 | 44.0% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b6-bfloat16] | 0.0610 | 0.0269 | 44.1% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx131072-float8_e4m3fn] | 17.4108 | 8.9652 | 51.5% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx131072-float8_e4m3fn] | 8.7654 | 4.5739 | 52.2% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx65536-float8_e4m3fn] | 4.3442 | 2.2818 | 52.5% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx65536-float8_e4m3fn] | 8.5572 | 4.4956 | 52.5% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx32768-float8_e4m3fn] | 4.1486 | 2.1923 | 52.8% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx32768-float8_e4m3fn] | 2.1469 | 1.1507 | 53.6% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx16384-float8_e4m3fn] | 1.9398 | 1.0600 | 54.6% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx16384-float8_e4m3fn] | 1.0448 | 0.5725 | 54.8% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx8192-float8_e4m3fn] | 0.8646 | 0.4784 | 55.3% | deepgemm |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[gemma-2b-bfloat16] | 0.3031 | 0.1683 | 55.5% | fa3 |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx8192-float8_e4m3fn] | 0.5036 | 0.2812 | 55.8% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx4096-float8_e4m3fn] | 0.2336 | 0.1318 | 56.4% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx4096-float8_e4m3fn] | 0.3283 | 0.1909 | 58.1% | deepgemm |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[starcoder-float16] | 0.7875 | 0.5053 | 64.2% | fa3 |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[context-chunk-bfloat16] | 0.3202 | 0.2116 | 66.1% | deepgemm |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-32768-bfloat16] | 3.1682 | 2.1512 | 67.9% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-32768-float16] | 3.1702 | 2.1596 | 68.1% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-kscale-float8_e4m3fn] | 0.4716 | 0.3220 | 68.3% | deepgemm |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-16384-float16] | 1.5655 | 1.0930 | 69.8% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-serving-batch-float16] | 0.0888 | 0.0623 | 70.1% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-serving-batch-bfloat16] | 0.0886 | 0.0622 | 70.2% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-16384-bfloat16] | 1.5648 | 1.1002 | 70.3% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-8192-bfloat16] | 0.7971 | 0.5638 | 70.7% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-8192-float16] | 0.7990 | 0.5660 | 70.8% | flashinfer |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-float16-float8_e4m3fn] | 1.9735 | 1.4054 | 71.2% | fa3 |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-4096-bfloat16] | 0.4152 | 0.2965 | 71.4% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-4096-float16] | 0.4152 | 0.2978 | 71.7% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-float8_e4m3fn] | 0.5148 | 0.3716 | 72.2% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-bfloat16] | 0.5296 | 0.3839 | 72.5% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-16x8192-bfloat16] | 0.6287 | 0.4680 | 74.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x8192-bfloat16] | 0.6251 | 0.4686 | 75.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x8192-bfloat16] | 0.6268 | 0.4720 | 75.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-16x8192-bfloat16] | 1.2240 | 0.9225 | 75.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-32x8192-bfloat16] | 2.4207 | 1.8295 | 75.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-16x8192-bfloat16] | 2.4377 | 1.8447 | 75.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-32x8192-bfloat16] | 1.2170 | 0.9224 | 75.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-32x8192-bfloat16] | 9.6296 | 7.3117 | 75.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-32x8192-bfloat16] | 7.1870 | 5.4588 | 75.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-16x8192-bfloat16] | 4.8219 | 3.6688 | 76.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x8192-bfloat16] | 2.4287 | 1.8485 | 76.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-16x8192-bfloat16] | 3.6188 | 2.7550 | 76.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x8192-bfloat16] | 1.2207 | 0.9305 | 76.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-16x8192-bfloat16] | 2.4223 | 1.8471 | 76.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-16x8192-bfloat16] | 2.4233 | 1.8487 | 76.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x8192-bfloat16] | 1.8127 | 1.3832 | 76.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-16x8192-bfloat16] | 1.2152 | 0.9277 | 76.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-32x8192-bfloat16] | 2.4130 | 1.8427 | 76.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-32x8192-bfloat16] | 4.7958 | 3.6661 | 76.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x8192-bfloat16] | 1.2176 | 0.9320 | 76.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x8192-bfloat16] | 1.2175 | 0.9344 | 76.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-32x8192-bfloat16] | 4.7769 | 3.6698 | 76.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-32x8192-bfloat16] | 4.7811 | 3.6747 | 76.9% | flashinfer |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[falcon-7b-2k-bfloat16] | 0.0372 | 0.0287 | 77.1% | fa3 |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-4k-float16] | 0.1167 | 0.0900 | 77.1% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-4k-bfloat16] | 0.1161 | 0.0898 | 77.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-16x8192-float16] | 0.5987 | 0.4645 | 77.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-16x8192-float16] | 2.3462 | 1.8303 | 78.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4096-4096-bfloat16] | 0.3253 | 0.2540 | 78.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-32x8192-float16] | 9.3056 | 7.2741 | 78.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-16x8192-float16] | 3.4866 | 2.7308 | 78.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-32x8192-float16] | 6.9279 | 5.4281 | 78.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x8192-float16] | 0.5950 | 0.4672 | 78.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-16x8192-float16] | 1.1686 | 0.9188 | 78.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-16x8192-float16] | 4.6405 | 3.6509 | 78.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-32x8192-float16] | 1.1620 | 0.9168 | 78.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x8192-float16] | 2.3258 | 1.8351 | 78.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-32x8192-float16] | 2.3040 | 1.8183 | 78.9% | flashinfer |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 0.5653 | 0.4462 | 78.9% | fa3 |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b64-bfloat16] | 0.1249 | 0.0986 | 79.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x8192-float16] | 1.7405 | 1.3753 | 79.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x8192-float16] | 1.1703 | 0.9254 | 79.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x8192-float16] | 1.1686 | 0.9242 | 79.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-16x8192-float16] | 1.1689 | 0.9245 | 79.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-16x8192-float16] | 2.3185 | 1.8343 | 79.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-32x8192-float16] | 4.6075 | 3.6460 | 79.1% | flashinfer |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.5663 | 0.4484 | 79.2% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-16x8192-float16] | 2.3210 | 1.8395 | 79.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-32x8192-float16] | 2.3078 | 1.8296 | 79.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x8192-float16] | 0.5936 | 0.4707 | 79.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-32x8192-float16] | 4.5936 | 3.6439 | 79.3% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b64-float16] | 0.1251 | 0.0993 | 79.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-32x8192-float16] | 4.5907 | 3.6480 | 79.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x8192-float16] | 1.1691 | 0.9302 | 79.6% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[short-prefill-bfloat16] | 0.0702 | 0.0565 | 80.5% | deepgemm |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-8b-long-bfloat16] | 0.5684 | 0.4580 | 80.6% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4096-4096-bfloat16] | 0.3031 | 0.2444 | 80.7% | flashinfer |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[falcon-7b-bfloat16] | 0.3139 | 0.2534 | 80.7% | fa3 |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-8b-long-float16] | 0.5702 | 0.4604 | 80.7% | fa3 |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-4k-bfloat16] | 0.0656 | 0.0534 | 81.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4096-4096-float16] | 0.3105 | 0.2529 | 81.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4096-4096-float16] | 0.2939 | 0.2435 | 82.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4x2048-bfloat16] | 0.3283 | 0.2725 | 83.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-4x2048-bfloat16] | 0.1758 | 0.1463 | 83.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-4x2048-bfloat16] | 0.1717 | 0.1434 | 83.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-4x2048-bfloat16] | 0.1720 | 0.1443 | 83.9% | flashinfer |
| 🔴 | **GQAVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-70b-fp8-q-lt-kv-float8_e4m3fn-bfloat16] | 0.1011 | 0.0858 | 84.8% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4x2048-bfloat16] | 0.3071 | 0.2627 | 85.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4x2048-float16] | 0.3156 | 0.2719 | 86.1% | flashinfer |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[llama-8b-softcap-float16] | 0.1563 | 0.1355 | 86.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-2048-6144-bfloat16] | 0.4138 | 0.3609 | 87.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-4x2048-float16] | 0.1673 | 0.1460 | 87.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-6144-2048-bfloat16] | 0.4118 | 0.3604 | 87.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-4x2048-float16] | 0.1642 | 0.1439 | 87.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4x2048-float16] | 0.2974 | 0.2621 | 88.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-4x2048-float16] | 0.1620 | 0.1432 | 88.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-2048-6144-float16] | 0.3994 | 0.3586 | 89.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-6144-2048-float16] | 0.3968 | 0.3581 | 90.2% | flashinfer |
| 🔴 | **GQAVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-rope-partial-bfloat16] | 0.0519 | 0.0469 | 90.3% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x1024-bfloat16] | 0.2620 | 0.2368 | 90.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x1024-bfloat16] | 0.1836 | 0.1663 | 90.6% | flashinfer |
| 🔴 | **GQAVarlenFwdOp** | test_gqa_varlen_fwd_bench[qwen3-fp8-ragged-float8_e4m3fn-bfloat16] | 0.1098 | 0.0996 | 90.7% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x1024-bfloat16] | 0.0970 | 0.0880 | 90.8% | flashinfer |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-8b-short-float16] | 0.1506 | 0.1372 | 91.1% | fa3 |
| 🔴 | **GQAVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-rope-partial-float16] | 0.0513 | 0.0469 | 91.3% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x1024-bfloat16] | 0.3389 | 0.3097 | 91.4% | flashinfer |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-8b-short-bfloat16] | 0.1495 | 0.1369 | 91.5% | fa3 |
| 🔴 | **GLAChunkBwdOp** | test_gla_bwd_bench[train-16k-float16] | 1.4432 | 1.3237 | 91.7% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x1024-bfloat16] | 0.1782 | 0.1638 | 91.9% | flashinfer |
| 🔴 | **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[llama-405b-p256-float16-float16] | 0.0396 | 0.0364 | 92.0% | fa3 |
| 🔴 | **MLAVarlenFwdOp** | test_mla_varlen_fwd_bench[ds-v3-mixed-bfloat16] | 25.8810 | 23.8883 | 92.3% | fa3 |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-short-float16] | 0.1418 | 0.1309 | 92.3% | fa3 |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-short-bfloat16] | 0.1413 | 0.1308 | 92.6% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x1024-bfloat16] | 0.1761 | 0.1631 | 92.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x1024-bfloat16] | 0.0934 | 0.0867 | 92.9% | flashinfer |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-long-mha-float16] | 0.4426 | 0.4150 | 93.8% | fa3 |
| 🔴 | **SharedExpertMLPFwdOp** | test_shared_expert_mlp_bench[kimi-k2-t512-bfloat16] | 0.6029 | 0.5654 | 93.8% | quack |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-long-mha-bfloat16] | 0.4412 | 0.4138 | 93.8% | fa3 |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-8b-long-mha-float16] | 0.4419 | 0.4156 | 94.1% | fa3 |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-8b-long-mha-bfloat16] | 0.4400 | 0.4142 | 94.2% | fa3 |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[gemma-2b-8k-bs1-bfloat16] | 0.0172 | 0.0163 | 94.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x1024-float16] | 0.2512 | 0.2368 | 94.3% | flashinfer |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[gemma-2b-8k-bs1-float16] | 0.0172 | 0.0162 | 94.4% | flashinfer |
| 🔴 | **LeFwdOp** | test_le_bench[linear-bias-float32] | 0.0076 | 0.0072 | 94.6% | torch-compile |
| 🔴 | **GeFwdOp** | test_ge_bench[linear-bias-float32] | 0.0077 | 0.0073 | 94.6% | torch-compile |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x1024-float16] | 0.1759 | 0.1665 | 94.6% | flashinfer |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[llama-8b-4k-float16] | 0.1428 | 0.1353 | 94.8% | flashinfer |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[llama-8b-4k-bfloat16] | 0.1419 | 0.1353 | 95.3% | flashinfer |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[llama-8b-32k-float16] | 0.2664 | 0.2540 | 95.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x1024-float16] | 0.3240 | 0.3090 | 95.4% | flashinfer |
| 🔴 | **GQAVarlenFwdOp** | test_gqa_varlen_fwd_bench[qwen-ragged-rope-bfloat16] | 0.1011 | 0.0965 | 95.4% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x1024-float16] | 0.0920 | 0.0879 | 95.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x1024-float16] | 0.1708 | 0.1635 | 95.8% | flashinfer |
| 🔴 | **LogicalOrFwdOp** | test_logical_or_bench[linear-bias-float32] | 0.0074 | 0.0071 | 95.9% | torch-compile |
| 🔴 | **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[qwen3-ragged-odd-bfloat16-bfloat16] | 0.1973 | 0.1891 | 95.9% | fa3 |
| 🔴 | **LogicalAndFwdOp** | test_logical_and_bench[llama-7b-hidden-float16] | 0.0074 | 0.0071 | 95.9% | torch-compile |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[llama-8b-32k-bfloat16] | 0.2648 | 0.2540 | 95.9% | flashinfer |
| 🔴 | **GQAVarlenFwdOp** | test_gqa_varlen_fwd_bench[qwen-ragged-rope-float16] | 0.1011 | 0.0970 | 96.0% | fa3 |
| 🔴 | **GLAChunkBwdOp** | test_gla_bwd_bench[train-8k-float16] | 0.7008 | 0.6770 | 96.6% | fla |
| 🔴 | **LeFwdOp** | test_le_bench[linear-bias-bfloat16] | 0.0048 | 0.0046 | 96.7% | torch-compile |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[llama-70b-32k-float16] | 0.1436 | 0.1388 | 96.7% | flashinfer |
| 🔴 | **LeFwdOp** | test_le_bench[llama-7b-hidden-float16] | 0.0075 | 0.0073 | 97.0% | torch-compile |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x1024-float16] | 0.1680 | 0.1630 | 97.0% | flashinfer |
| 🔴 | **RemainderFwdOp** | test_remainder_bench[cnn-feat-broadcast-float32] | 0.0275 | 0.0267 | 97.2% | torch-compile |
| 🔴 | **GLAChunkBwdOp** | test_gla_bwd_bench[train-16k-bfloat16] | 1.3637 | 1.3255 | 97.2% | fla |
| 🔴 | **FusedMoEExpertsFwdOp** | test_moe_experts_bench[ds-v3-prefill-float16] | 7.9490 | 7.7354 | 97.3% | flashinfer-cutlass |
| 🔴 | **MinimumFwdOp** | test_minimum_bench[llama-7b-hidden-float16] | 0.0084 | 0.0081 | 97.3% | torch-compile |
| 🔴 | **DeltaNetChunkFwdOp** | test_deltanet_vs_fla_fwd[train-2k-bfloat16] | 0.0630 | 0.0615 | 97.6% | fla |
| 🔴 | **GeFwdOp** | test_ge_bench[llama-7b-hidden-float16] | 0.0075 | 0.0073 | 97.7% | torch-compile |
| 🔴 | **NeFwdOp** | test_ne_bench[linear-bias-bfloat16] | 0.0049 | 0.0048 | 97.7% | torch-compile |
| 🔴 | **NeFwdOp** | test_ne_bench[linear-bias-float32] | 0.0077 | 0.0075 | 97.7% | torch-compile |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[llama-70b-32k-bfloat16] | 0.1419 | 0.1386 | 97.7% | flashinfer |
| 🔴 | **MeanFwdOp** | test_mean_bench[mlp-intermediate-float32] | 0.0252 | 0.0246 | 97.7% | torch-compile |
| 🔴 | **MHADecodePagedWithKVCacheFwdOp** | test_mha_decode_paged_bench[opt-1.3b-b16-float16] | 0.0792 | 0.0774 | 97.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-32768-bfloat16] | 0.2955 | 0.2889 | 97.8% | flashinfer |
| 🔴 | **MHCPostFwdOp** | test_mhc_post_bench[hidden-1280] | 0.0014 | 0.0014 | 97.8% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-qkv-a-bfloat16] | 0.1820 | 0.1780 | 97.8% | cublaslt-best |
| 🔴 | **MoEGroupedGemmFP8FwdOp** | test_moe_grouped_gemm_fp8_bench[ds-v3-e8-up-masked] | 0.0744 | 0.0728 | 97.8% | deepgemm |
| 🔴 | **DeltaNetChunkFwdOp** | test_deltanet_vs_fla_fwd[train-2k-float16] | 0.0625 | 0.0612 | 97.9% | fla |
| 🔴 | **SumFwdOp** | test_sum_bench[mlp-intermediate-float32] | 0.0251 | 0.0246 | 97.9% | torch-compile |
| 🔴 | **VectorNormFwdOp** | test_vector_norm_bench[l2-mlp-intermediate-float32] | 0.0251 | 0.0246 | 98.0% | torch-compile |
| 🔴 | **SumFwdOp** | test_sum_bench[3d-multidim-float16] | 0.0048 | 0.0047 | 98.0% | torch-compile |
| 🔴 | **DivFwdOp** | test_div_bench[linear-bias-bfloat16] | 0.0063 | 0.0062 | 98.0% | torch-compile |
| 🔴 | **FloorDivideFwdOp** | test_floor_divide_bench[cnn-feat-broadcast-float32] | 0.0271 | 0.0266 | 98.0% | torch-compile |
| 🔴 | **VectorNormFwdOp** | test_vector_norm_bench[l2-3d-multidim-float16] | 0.0048 | 0.0047 | 98.0% | torch-compile |
| 🔴 | **LtFwdOp** | test_lt_bench[linear-bias-float16] | 0.0048 | 0.0047 | 98.0% | torch-compile |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x1024-float16] | 0.0884 | 0.0867 | 98.1% | flashinfer |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-down-bfloat16] | 0.1733 | 0.1701 | 98.2% | cublaslt-best |
| 🔴 | **ProdFwdOp** | test_prod_bench[mlp-intermediate-float32] | 0.0251 | 0.0247 | 98.3% | torch-compile |
| 🔴 | **FusedMoEFwdOp** | test_fused_moe_fwd_bench[gpt-oss-120b-decode-bfloat16] | 1.2642 | 1.2448 | 98.5% | vllm |
| 🔴 | **DeltaNetChunkFwdOp** | test_deltanet_vs_fla_fwd[train-8k-float16] | 0.2153 | 0.2120 | 98.5% | fla |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-q-b-bfloat16] | 0.4136 | 0.4073 | 98.5% | cublaslt-best |
| 🔴 | **EqFwdOp** | test_eq_bench[linear-bias-float32] | 0.0077 | 0.0076 | 98.5% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-mlp-up-float16] | 0.3369 | 0.3321 | 98.6% | cublaslt-best |
| 🔴 | **LogicalAndFwdOp** | test_logical_and_bench[linear-bias-float16] | 0.0048 | 0.0048 | 98.7% | torch-compile |
| 🔴 | **MaxPool2dIndicesFwdOp** | test_max_pool2d_indices_bench[vgg-block-float32] | 0.0131 | 0.0129 | 98.7% | torch-compile |
| 🔴 | **DeltaNetChunkFwdOp** | test_deltanet_vs_fla_fwd[train-8k-bfloat16] | 0.2166 | 0.2138 | 98.7% | fla |
| 🔴 | **GLAChunkBwdOp** | test_gla_bwd_bench[train-8k-bfloat16] | 0.6858 | 0.6772 | 98.8% | fla |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-o-proj-bfloat16] | 1.2694 | 1.2542 | 98.8% | quack |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-decode-down-bfloat16] | 0.0135 | 0.0133 | 98.8% | torch-cublas |
| 🔴 | **AdaLayerNormFwdOp** | test_ada_layer_norm_bench[llama-8b-decode-bfloat16] | 0.0027 | 0.0027 | 98.8% | torch-compile |
| 🔴 | **LogicalAndFwdOp** | test_logical_and_bench[hidden-state-prefill-float32] | 0.0221 | 0.0218 | 98.9% | torch |
| 🔴 | **MaximumFwdOp** | test_maximum_bench[llama-7b-hidden-float16] | 0.0084 | 0.0083 | 98.9% | torch-compile |
| 🔴 | **RMSNormFwdOp** | test_rms_norm_bench[qk-norm-head-bfloat16] | 0.0029 | 0.0029 | 98.9% | torch-compile |
| 🔴 | **LogicalAndFwdOp** | test_logical_and_bench[linear-bias-float32] | 0.0074 | 0.0073 | 98.9% | torch-compile |
| 🔴 | **SharedExpertMLPFwdOp** | test_shared_expert_mlp_bench[ds-v3-t4096-bfloat16] | 0.5100 | 0.5046 | 98.9% | quack |
| 🔴 | **MHCPostFwdOp** | test_mhc_post_bench[hidden-1920] | 0.0015 | 0.0015 | 98.9% | torch-compile |
| 🔴 | **WhereFwdOp** | test_where_bench[16M-float16] | 0.0304 | 0.0301 | 99.0% | torch-compile |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 44 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 445 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 810 lines in `ops/`, 60.8% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 2493 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

### Never-built kernels

| File | Executed |
| --- | --- |
| `kernels/linear_attention/gdn/prefill_forward.py` | 3.4% |
| `kernels/linear_attention/gdn/prefill_prepare.py` | 3.5% |
| `kernels/linear_attention/deltanet/prefill_forward.py` | 4.3% |
| `kernels/linear_attention/kda/fused_program.py` | 4.3% |
| `kernels/linear_attention/kda/chunk_programs.py` | 5.0% |
| `kernels/linear_attention/deltanet/prefill_prepare.py` | 5.7% |
| `kernels/sampling/top_k_top_p_mask.py` | 6.5% |
| `kernels/attention/gqa/dense_fp8.py` | 6.6% |
| `kernels/linear_attention/kda/inverse.py` | 6.7% |
| `kernels/attention/gqa/prefill_paged_kv_append.py` | 6.9% |
| `kernels/linear_attention/delta_decode.py` | 7.8% |
| `kernels/attention/gqa/paged_rope_prepare.py` | 8.8% |
| `kernels/attention/gqa/dense.py` | 9.6% |
| `kernels/sampling/top_k_mask.py` | 10.8% |
| `kernels/sampling/sampling_from_probs.py` | 11.8% |
| `kernels/sampling/chain_speculative_sampling.py` | 11.8% |
| `kernels/linear_attention/kda/decode_program.py` | 11.9% |
| `kernels/attention/mla/decode.py` | 12.1% |
| `kernels/linear_attention/gla/varlen_prefill.py` | 12.2% |
| `kernels/sampling/top_p_mask.py` | 12.4% |
| `kernels/attention/gqa/paged_ws.py` | 12.4% |
| `kernels/quantization/int8_quant_per_tensor.py` | 12.9% |
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
| `kernels/norm/rms_norm_on_chip.py` | 23.1% |
| `kernels/linear_attention/gdn/prefill.py` | 23.7% |
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
