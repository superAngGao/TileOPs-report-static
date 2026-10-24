# ✅ TileOPs Nightly Report

> **2026-10-20 20:27** &ensp;|&ensp; `bcd2c64d` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Operators** | 205 |
| **Kernels** | 341 |
| **Specs** | 0 |
| **Workloads** | 1487 |
| **Correctness** | ✅ &ensp; (205/205 ops verified, 1323/1371 tests) |
| **Benchmarked Ops** | 205 |
| **Benchmark Failures** | ✅ None &ensp;|&ensp; ⚠️ 1 skipped |
| **Regressions** (vs 14-day median) | ✅ None |
| **Baseline Alerts** (< 99%) | ⚠️ 143 |
| **vs Baseline** | ↑ 2045 &ensp;·&ensp; ↓ 143 &ensp;/&ensp; 2188 rows |
| **Rows no reference checked** | ⚠️ 201 |
| **History window** | 13 runs, 2026-10-06 to 2026-10-19 |
| **Roofline anomalies** | ✅ None |
| **Improvements** (vs 14-day best) | 🎉 54 |
| **Moved since previous run** | 🔵 54 |
| **Never-built kernels** | ⚠️ 48 files **+1** &ensp;·&ensp; `kernels/linear_attention/gdn/prefill_forward.py` at 3.4% |
| **Untested roofline math** | 445 lines in `perf/` &ensp;·&ensp; `perf/formulas.py` at 16.2% |
| **Untested op logic** | 810 lines in `ops/` **−2** &ensp;·&ensp; 60.9% of branches taken **+0.1pp** |
| | <sub>coverage compared against the 2026-10-19 run; no figure means it held</sub> |

## 🎉 Performance Improvements (vs 14-day best)

| Op | Config | Prev Best (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[ds-v32-decode-b1-float8_e4m3fn] | 0.2865 | 0.0055 | -98.1% | 49.63 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-32k-bfloat16] | 0.3857 | 0.0775 | -79.9% | 472.12 |
| **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-mixed-float16] | 22.3449 | 4.9841 | -77.7% | 669.18 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b1-float16] | 0.0540 | 0.0133 | -75.3% | 42.85 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b1-bfloat16] | 0.0540 | 0.0134 | -75.2% | 42.64 |
| **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-float16-float8_e4m3fn] | 56.1582 | 14.5406 | -74.1% | 617.40 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-single-request-bfloat16] | 0.0542 | 0.0140 | -74.1% | 81.40 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-single-request-float16] | 0.0542 | 0.0140 | -74.1% | 81.40 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b2-float16] | 0.0547 | 0.0147 | -73.1% | 77.69 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b2-bfloat16] | 0.0547 | 0.0148 | -73.0% | 77.52 |
| **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-rope-float16] | 41.8488 | 13.6554 | -67.4% | 657.42 |
| **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-rope-float16] | 1.6605 | 0.5613 | -66.2% | 525.53 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-32k-bfloat16] | 0.3853 | 0.1424 | -63.0% | 513.92 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b6-float16] | 0.0594 | 0.0222 | -62.6% | 154.48 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b6-bfloat16] | 0.0594 | 0.0222 | -62.6% | 154.48 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-32k-float16] | 0.3853 | 0.1450 | -62.4% | 504.85 |
| **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[gemma-2b-bfloat16] | 0.3010 | 0.1385 | -54.0% | 529.74 |
| **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-float16-float8_e4m3fn] | 1.9621 | 0.9447 | -51.9% | 312.23 |
| **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[starcoder-float16] | 0.7869 | 0.3925 | -50.1% | 563.55 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx131072-float8_e4m3fn] | 17.2530 | 8.9488 | -48.1% | 978.92 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx65536-float8_e4m3fn] | 8.4935 | 4.4092 | -48.1% | 977.64 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx32768-float8_e4m3fn] | 4.1086 | 2.1526 | -47.6% | 968.96 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx131072-float8_e4m3fn] | 8.6840 | 4.5868 | -47.2% | 962.52 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx65536-float8_e4m3fn] | 4.3091 | 2.2811 | -47.1% | 960.07 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx16384-float8_e4m3fn] | 1.9355 | 1.0299 | -46.8% | 945.13 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx32768-float8_e4m3fn] | 2.1241 | 1.1329 | -46.7% | 951.25 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx16384-float8_e4m3fn] | 1.0396 | 0.5580 | -46.3% | 934.47 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx8192-float8_e4m3fn] | 0.8631 | 0.4634 | -46.3% | 900.28 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx4096-float8_e4m3fn] | 0.3262 | 0.1763 | -45.9% | 788.81 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx8192-float8_e4m3fn] | 0.5022 | 0.2718 | -45.9% | 895.31 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx4096-float8_e4m3fn] | 0.2328 | 0.1281 | -45.0% | 814.06 |
| **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[synthetic-softcap-float16-float8_e4m3fn] | 0.1733 | 0.0978 | -43.6% | 192.52 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-32768-float16] | 3.1455 | 1.8876 | -40.0% | 620.32 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-serving-batch-float16] | 0.0874 | 0.0525 | -40.0% | 392.21 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-32768-bfloat16] | 3.1410 | 1.8884 | -39.9% | 620.05 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-serving-batch-bfloat16] | 0.0871 | 0.0524 | -39.8% | 392.69 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-kscale-float8_e4m3fn] | 0.4709 | 0.2857 | -39.3% | 30.83 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-16384-bfloat16] | 1.5499 | 0.9590 | -38.1% | 610.47 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-16384-float16] | 1.5519 | 0.9612 | -38.1% | 609.09 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-8192-bfloat16] | 0.7894 | 0.4961 | -37.2% | 590.12 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-8192-float16] | 0.7905 | 0.4981 | -37.0% | 587.69 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-float8_e4m3fn] | 0.5141 | 0.3299 | -35.8% | 26.70 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[context-chunk-bfloat16] | 0.3196 | 0.2068 | -35.3% | 414.61 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-4096-bfloat16] | 0.4099 | 0.2658 | -35.2% | 550.70 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-4096-float16] | 0.4106 | 0.2666 | -35.1% | 549.12 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-bfloat16] | 0.5283 | 0.3436 | -35.0% | 25.64 |
| **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[falcon-7b-bfloat16] | 0.3123 | 0.2077 | -33.5% | 327.58 |
| **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[synthetic-softcap-float16] | 0.1305 | 0.0883 | -32.4% | 213.32 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-4k-float16] | 0.1153 | 0.0794 | -31.1% | 460.92 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-4k-bfloat16] | 0.1151 | 0.0794 | -31.0% | 460.73 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-4k-bfloat16] | 0.0645 | 0.0468 | -27.4% | 390.82 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[short-prefill-bfloat16] | 0.0698 | 0.0518 | -25.8% | 169.87 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b64-bfloat16] | 0.1246 | 0.0950 | -23.7% | 385.16 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b64-float16] | 0.1250 | 0.0954 | -23.6% | 383.54 |

## 🔵 Moved Since Previous Run

> Moves against the most recent reading. A row restored to its old level appears only here: returning is not a new 14-day record.

| Op | Config | Previous (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[ds-v32-decode-b1-float8_e4m3fn] | 0.2891 | 0.0055 | -98.1% | 49.63 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-32k-bfloat16] | 0.3927 | 0.0775 | -80.3% | 472.12 |
| **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-mixed-float16] | 22.6866 | 4.9841 | -78.0% | 669.18 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b1-float16] | 0.0551 | 0.0133 | -75.8% | 42.85 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b1-bfloat16] | 0.0551 | 0.0134 | -75.7% | 42.64 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-single-request-bfloat16] | 0.0553 | 0.0140 | -74.6% | 81.40 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-single-request-float16] | 0.0552 | 0.0140 | -74.6% | 81.40 |
| **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-float16-float8_e4m3fn] | 56.2387 | 14.5406 | -74.1% | 617.40 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b2-float16] | 0.0558 | 0.0147 | -73.6% | 77.69 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b2-bfloat16] | 0.0557 | 0.0148 | -73.5% | 77.52 |
| **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-rope-float16] | 42.4312 | 13.6554 | -67.8% | 657.42 |
| **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-rope-float16] | 1.6741 | 0.5613 | -66.5% | 525.53 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-32k-bfloat16] | 0.3917 | 0.1424 | -63.6% | 513.92 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b6-float16] | 0.0610 | 0.0222 | -63.6% | 154.48 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b6-bfloat16] | 0.0609 | 0.0222 | -63.6% | 154.48 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-32k-float16] | 0.3916 | 0.1450 | -63.0% | 504.85 |
| **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[gemma-2b-bfloat16] | 0.3033 | 0.1385 | -54.3% | 529.74 |
| **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-float16-float8_e4m3fn] | 1.9767 | 0.9447 | -52.2% | 312.23 |
| **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[starcoder-float16] | 0.7883 | 0.3925 | -50.2% | 563.55 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx65536-float8_e4m3fn] | 8.5751 | 4.4092 | -48.6% | 977.64 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx131072-float8_e4m3fn] | 17.3822 | 8.9488 | -48.5% | 978.92 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx32768-float8_e4m3fn] | 4.1538 | 2.1526 | -48.2% | 968.96 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx131072-float8_e4m3fn] | 8.7605 | 4.5868 | -47.6% | 962.52 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx65536-float8_e4m3fn] | 4.3513 | 2.2811 | -47.6% | 960.07 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx32768-float8_e4m3fn] | 2.1445 | 1.1329 | -47.2% | 951.25 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx16384-float8_e4m3fn] | 1.9368 | 1.0299 | -46.8% | 945.13 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx16384-float8_e4m3fn] | 1.0439 | 0.5580 | -46.5% | 934.47 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx8192-float8_e4m3fn] | 0.8658 | 0.4634 | -46.5% | 900.28 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx4096-float8_e4m3fn] | 0.3264 | 0.1763 | -46.0% | 788.81 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx8192-float8_e4m3fn] | 0.5025 | 0.2718 | -45.9% | 895.31 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx4096-float8_e4m3fn] | 0.2336 | 0.1281 | -45.2% | 814.06 |
| **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[synthetic-softcap-float16-float8_e4m3fn] | 0.1746 | 0.0978 | -44.0% | 192.52 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-serving-batch-float16] | 0.0889 | 0.0525 | -41.0% | 392.21 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-serving-batch-bfloat16] | 0.0887 | 0.0524 | -40.9% | 392.69 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-32768-float16] | 3.1734 | 1.8876 | -40.5% | 620.32 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-32768-bfloat16] | 3.1691 | 1.8884 | -40.4% | 620.05 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-kscale-float8_e4m3fn] | 0.4715 | 0.2857 | -39.4% | 30.83 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-16384-bfloat16] | 1.5643 | 0.9590 | -38.7% | 610.47 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-16384-float16] | 1.5648 | 0.9612 | -38.6% | 609.09 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-8192-bfloat16] | 0.7972 | 0.4961 | -37.8% | 590.12 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-8192-float16] | 0.7974 | 0.4981 | -37.5% | 587.69 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-float8_e4m3fn] | 0.5152 | 0.3299 | -36.0% | 26.70 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-4096-bfloat16] | 0.4146 | 0.2658 | -35.9% | 550.70 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-4096-float16] | 0.4149 | 0.2666 | -35.8% | 549.12 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[context-chunk-bfloat16] | 0.3199 | 0.2068 | -35.4% | 414.61 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-bfloat16] | 0.5301 | 0.3436 | -35.2% | 25.64 |
| **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[falcon-7b-bfloat16] | 0.3137 | 0.2077 | -33.8% | 327.58 |
| **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[synthetic-softcap-float16] | 0.1317 | 0.0883 | -33.0% | 213.32 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-4k-float16] | 0.1165 | 0.0794 | -31.8% | 460.92 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-4k-bfloat16] | 0.1160 | 0.0794 | -31.5% | 460.73 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-4k-bfloat16] | 0.0654 | 0.0468 | -28.5% | 390.82 |
| **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[short-prefill-bfloat16] | 0.0702 | 0.0518 | -26.3% | 169.87 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b64-bfloat16] | 0.1250 | 0.0950 | -24.0% | 385.16 |
| **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b64-float16] | 0.1250 | 0.0954 | -23.6% | 383.54 |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 99%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x8192-bfloat16] | 0.6187 | 0.4687 | 75.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-16x8192-bfloat16] | 0.6171 | 0.4682 | 75.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x8192-bfloat16] | 0.6210 | 0.4725 | 76.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-16x8192-bfloat16] | 1.2048 | 0.9231 | 76.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-32x8192-bfloat16] | 1.2028 | 0.9221 | 76.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x8192-bfloat16] | 1.2111 | 0.9308 | 76.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-16x8192-bfloat16] | 1.2074 | 0.9286 | 76.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-32x8192-bfloat16] | 2.3845 | 1.8352 | 77.0% | flashinfer |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[falcon-7b-2k-bfloat16] | 0.0372 | 0.0287 | 77.1% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-32x8192-bfloat16] | 4.7552 | 3.6653 | 77.1% | flashinfer |

<details>
<summary><strong>133 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x8192-bfloat16] | 1.2123 | 0.9347 | 77.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x8192-bfloat16] | 2.3950 | 1.8492 | 77.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-32x8192-bfloat16] | 9.4573 | 7.3053 | 77.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-16x8192-bfloat16] | 2.3971 | 1.8516 | 77.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x8192-bfloat16] | 1.7889 | 1.3820 | 77.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-16x8192-bfloat16] | 3.5409 | 2.7437 | 77.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x8192-bfloat16] | 1.2026 | 0.9321 | 77.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-16x8192-bfloat16] | 4.7329 | 3.6711 | 77.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-32x8192-bfloat16] | 2.3680 | 1.8373 | 77.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-32x8192-bfloat16] | 7.0397 | 5.4622 | 77.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-16x8192-bfloat16] | 2.3800 | 1.8471 | 77.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-16x8192-bfloat16] | 2.3778 | 1.8486 | 77.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-32x8192-bfloat16] | 4.7177 | 3.6711 | 77.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-32x8192-float16] | 9.3423 | 7.2706 | 77.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-32x8192-bfloat16] | 4.7116 | 3.6675 | 77.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-16x8192-float16] | 0.5990 | 0.4663 | 77.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-16x8192-float16] | 2.3398 | 1.8309 | 78.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-16x8192-float16] | 3.4857 | 2.7290 | 78.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-16x8192-float16] | 1.1726 | 0.9181 | 78.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-32x8192-float16] | 6.9314 | 5.4309 | 78.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x8192-float16] | 0.5944 | 0.4666 | 78.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-32x8192-float16] | 1.1657 | 0.9168 | 78.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-16x8192-float16] | 4.6357 | 3.6522 | 78.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x8192-float16] | 1.7423 | 1.3731 | 78.8% | flashinfer |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.5664 | 0.4470 | 78.9% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x8192-float16] | 2.3254 | 1.8355 | 78.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-16x8192-float16] | 2.3205 | 1.8342 | 79.0% | flashinfer |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 0.5646 | 0.4466 | 79.1% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-32x8192-float16] | 4.6064 | 3.6448 | 79.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x8192-float16] | 0.5942 | 0.4705 | 79.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-32x8192-float16] | 2.2938 | 1.8185 | 79.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x8192-float16] | 1.1671 | 0.9254 | 79.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-16x8192-float16] | 2.3146 | 1.8365 | 79.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-32x8192-float16] | 4.5957 | 3.6467 | 79.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-16x8192-float16] | 1.1670 | 0.9260 | 79.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-32x8192-float16] | 4.5955 | 3.6464 | 79.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4096-4096-bfloat16] | 0.3197 | 0.2540 | 79.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x8192-float16] | 1.1622 | 0.9240 | 79.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x8192-float16] | 1.1680 | 0.9292 | 79.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-32x8192-float16] | 2.3011 | 1.8327 | 79.7% | flashinfer |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-8b-long-bfloat16] | 0.5682 | 0.4583 | 80.7% | fa3 |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-8b-long-float16] | 0.5704 | 0.4602 | 80.7% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4096-4096-float16] | 0.3106 | 0.2531 | 81.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4096-4096-bfloat16] | 0.2978 | 0.2446 | 82.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4096-4096-float16] | 0.2934 | 0.2433 | 82.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4x2048-bfloat16] | 0.3230 | 0.2731 | 84.5% | flashinfer |
| 🔴 | **GQAVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-70b-fp8-q-lt-kv-float8_e4m3fn-bfloat16] | 0.1013 | 0.0858 | 84.7% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-4x2048-bfloat16] | 0.1730 | 0.1466 | 84.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-4x2048-bfloat16] | 0.1678 | 0.1438 | 85.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-4x2048-bfloat16] | 0.1684 | 0.1446 | 85.9% | flashinfer |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[llama-8b-softcap-float16] | 0.1577 | 0.1356 | 86.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4x2048-float16] | 0.3155 | 0.2717 | 86.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-4x2048-float16] | 0.1677 | 0.1457 | 86.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-2048-6144-bfloat16] | 0.4142 | 0.3606 | 87.1% | flashinfer |
| 🔴 | **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[qwen3-fp8-ragged-odd-float8_e4m3fn-float8_e4m3fn-bfloat16] | 0.1839 | 0.1602 | 87.1% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4x2048-bfloat16] | 0.3018 | 0.2630 | 87.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-6144-2048-bfloat16] | 0.4122 | 0.3604 | 87.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-4x2048-float16] | 0.1644 | 0.1438 | 87.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4x2048-float16] | 0.2975 | 0.2620 | 88.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-4x2048-float16] | 0.1622 | 0.1429 | 88.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-2048-6144-float16] | 0.3995 | 0.3587 | 89.8% | flashinfer |
| 🔴 | **GQAVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-rope-partial-bfloat16] | 0.0521 | 0.0469 | 90.0% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-6144-2048-float16] | 0.3971 | 0.3581 | 90.2% | flashinfer |
| 🔴 | **GQAVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-rope-partial-float16] | 0.0519 | 0.0469 | 90.3% | fa3 |
| 🔴 | **GQAVarlenFwdOp** | test_gqa_varlen_fwd_bench[qwen3-fp8-ragged-float8_e4m3fn-bfloat16] | 0.1100 | 0.0997 | 90.7% | fa3 |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-8b-short-float16] | 0.1508 | 0.1373 | 91.1% | fa3 |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-8b-short-bfloat16] | 0.1496 | 0.1368 | 91.4% | fa3 |
| 🔴 | **MLAVarlenFwdOp** | test_mla_varlen_fwd_bench[ds-v3-mixed-bfloat16] | 25.7943 | 23.7137 | 91.9% | fa3 |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-short-float16] | 0.1420 | 0.1312 | 92.3% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x1024-bfloat16] | 0.2573 | 0.2377 | 92.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x1024-bfloat16] | 0.1803 | 0.1666 | 92.4% | flashinfer |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-short-bfloat16] | 0.1416 | 0.1311 | 92.6% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x1024-bfloat16] | 0.3330 | 0.3103 | 93.2% | flashinfer |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-8b-long-mha-bfloat16] | 0.4420 | 0.4130 | 93.4% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x1024-bfloat16] | 0.1755 | 0.1642 | 93.6% | flashinfer |
| 🔴 | **SharedExpertMLPFwdOp** | test_shared_expert_mlp_bench[kimi-k2-t512-bfloat16] | 0.6005 | 0.5630 | 93.7% | quack |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-8b-long-mha-float16] | 0.4425 | 0.4149 | 93.8% | fa3 |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-long-mha-bfloat16] | 0.4401 | 0.4133 | 93.9% | fa3 |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-long-mha-float16] | 0.4429 | 0.4162 | 94.0% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x1024-float16] | 0.2518 | 0.2369 | 94.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x1024-float16] | 0.1764 | 0.1662 | 94.2% | flashinfer |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[gemma-2b-8k-bs1-bfloat16] | 0.0172 | 0.0163 | 94.3% | flashinfer |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[gemma-2b-8k-bs1-float16] | 0.0172 | 0.0162 | 94.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x1024-bfloat16] | 0.1733 | 0.1636 | 94.4% | flashinfer |
| 🔴 | **LtFwdOp** | test_lt_bench[linear-bias-float32] | 0.0076 | 0.0072 | 94.8% | torch-compile |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x1024-bfloat16] | 0.0932 | 0.0884 | 94.8% | flashinfer |
| 🔴 | **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-fp8-prefill-float8_e4m3fn-float8_e4m3fn-bfloat16] | 0.4672 | 0.4435 | 94.9% | fa3 |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[llama-8b-32k-float16] | 0.2674 | 0.2540 | 95.0% | flashinfer |
| 🔴 | **FusedMoEExpertsFwdOp** | test_moe_experts_bench[ds-v3-prefill-float16] | 8.0614 | 7.6654 | 95.1% | flashinfer-cutlass |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[llama-8b-4k-float16] | 0.1424 | 0.1354 | 95.1% | flashinfer |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[llama-8b-32k-bfloat16] | 0.2668 | 0.2540 | 95.2% | flashinfer |
| 🔴 | **GQAVarlenFwdOp** | test_gqa_varlen_fwd_bench[qwen-ragged-rope-bfloat16] | 0.1013 | 0.0965 | 95.2% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x1024-float16] | 0.0921 | 0.0877 | 95.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x1024-float16] | 0.3247 | 0.3095 | 95.3% | flashinfer |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[llama-8b-4k-bfloat16] | 0.1417 | 0.1351 | 95.3% | flashinfer |
| 🔴 | **GeFwdOp** | test_ge_bench[linear-bias-float32] | 0.0077 | 0.0073 | 95.6% | torch-compile |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x1024-float16] | 0.1711 | 0.1637 | 95.7% | flashinfer |
| 🔴 | **GQAVarlenFwdOp** | test_gqa_varlen_fwd_bench[qwen-ragged-rope-float16] | 0.1012 | 0.0971 | 96.0% | fa3 |
| 🔴 | **NeFwdOp** | test_ne_bench[linear-bias-float16] | 0.0048 | 0.0046 | 96.0% | torch-compile |
| 🔴 | **LogicalAndFwdOp** | test_logical_and_bench[linear-bias-float32] | 0.0074 | 0.0072 | 96.5% | torch-compile |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[llama-70b-32k-float16] | 0.1432 | 0.1389 | 97.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x1024-float16] | 0.1681 | 0.1631 | 97.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x1024-bfloat16] | 0.0896 | 0.0871 | 97.2% | flashinfer |
| 🔴 | **SumFwdOp** | test_sum_bench[3d-multidim-float16] | 0.0048 | 0.0046 | 97.3% | torch-compile |
| 🔴 | **LeFwdOp** | test_le_bench[linear-bias-bfloat16] | 0.0048 | 0.0046 | 97.3% | torch-compile |
| 🔴 | **BmmFwdOp** | test_bmm_bench[square-1k-bfloat16] | 0.0303 | 0.0295 | 97.4% | quack |
| 🔴 | **LogicalAndFwdOp** | test_logical_and_bench[linear-bias-float16] | 0.0049 | 0.0047 | 97.4% | torch-compile |
| 🔴 | **MoEGroupedGemmFP8FwdOp** | test_moe_grouped_gemm_fp8_bench[ds-v3-e8-up-masked] | 0.0744 | 0.0727 | 97.7% | deepgemm |
| 🔴 | **FusedMoEExpertsFwdOp** | test_moe_experts_bench[ds-v3-prefill-bfloat16] | 7.6763 | 7.5036 | 97.8% | flashinfer-cutlass |
| 🔴 | **LogicalAndFwdOp** | test_logical_and_bench[llama-7b-ffn-float16] | 0.0164 | 0.0160 | 97.8% | torch-compile |
| 🔴 | **MHCPostFwdOp** | test_mhc_post_bench[hidden-1280] | 0.0014 | 0.0014 | 97.8% | torch-compile |
| 🔴 | **LogicalOrFwdOp** | test_logical_or_bench[llama-7b-hidden-float16] | 0.0072 | 0.0071 | 97.8% | torch |
| 🔴 | **MHCPostFwdOp** | test_mhc_post_bench[hidden-1920] | 0.0015 | 0.0015 | 97.9% | torch-compile |
| 🔴 | **MHADecodePagedWithKVCacheFwdOp** | test_mha_decode_paged_bench[opt-1.3b-b16-float16] | 0.0791 | 0.0774 | 97.9% | flashinfer |
| 🔴 | **NeFwdOp** | test_ne_bench[linear-bias-float32] | 0.0077 | 0.0075 | 97.9% | torch-compile |
| 🔴 | **SiluFwdOp** | test_silu_bench[llama-8b-ffn-decode-bfloat16] | 0.0015 | 0.0015 | 97.9% | torch-compile |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[llama-70b-32k-bfloat16] | 0.1417 | 0.1388 | 97.9% | flashinfer |
| 🔴 | **MeanFwdOp** | test_mean_bench[mlp-intermediate-float32] | 0.0250 | 0.0245 | 98.0% | torch-compile |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x1024-float16] | 0.0884 | 0.0866 | 98.0% | flashinfer |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-qkv-a-bfloat16] | 0.1821 | 0.1784 | 98.0% | cublaslt-best |
| 🔴 | **ReciprocalFwdOp** | test_reciprocal_bench[16M-bfloat16] | 0.0184 | 0.0180 | 98.1% | torch-compile |
| 🔴 | **MHCPostFwdOp** | test_mhc_post_bench[hidden-2560] | 0.0017 | 0.0016 | 98.1% | torch-compile |
| 🔴 | **FusedMoEFwdOp** | test_fused_moe_fwd_bench[gpt-oss-120b-decode-bfloat16] | 1.2684 | 1.2452 | 98.2% | vllm |
| 🔴 | **VectorNormFwdOp** | test_vector_norm_bench[l2-3d-multidim-float16] | 0.0048 | 0.0047 | 98.3% | torch-compile |
| 🔴 | **SumFwdOp** | test_sum_bench[mlp-intermediate-float32] | 0.0250 | 0.0246 | 98.4% | torch-compile |
| 🔴 | **VectorNormFwdOp** | test_vector_norm_bench[l2-mlp-intermediate-float32] | 0.0250 | 0.0247 | 98.5% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-mlp-up-bfloat16] | 0.3349 | 0.3303 | 98.6% | cublaslt-best |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-down-bfloat16] | 0.1730 | 0.1708 | 98.7% | cublaslt-best |
| 🔴 | **MaximumFwdOp** | test_maximum_bench[linear-bias-float32] | 0.0101 | 0.0100 | 98.7% | torch-compile |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-q-b-bfloat16] | 0.4136 | 0.4085 | 98.8% | cublaslt-best |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx131072-float8_e4m3fn] | 4.5868 | 4.5359 | 98.9% | deepgemm |
| 🔴 | **RMSNormFwdOp** | test_rms_norm_bench[qk-norm-head-bfloat16] | 0.0029 | 0.0028 | 98.9% | torch-compile |
| 🔴 | **ClampTensorFwdOp** | test_clamp_bench[16M-min-only-float32] | 0.0493 | 0.0488 | 99.0% | torch |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 48 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 445 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 810 lines in `ops/`, 60.9% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 2491 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

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
| `kernels/attention/gqa/paged_fp8_ws.py` | 9.1% |
| `kernels/attention/gqa/dense.py` | 9.6% |
| `kernels/sampling/top_k_mask.py` | 10.8% |
| `kernels/sampling/sampling_from_probs.py` | 11.8% |
| `kernels/sampling/chain_speculative_sampling.py` | 11.8% |
| `kernels/linear_attention/kda/decode_program.py` | 11.9% |
| `kernels/linear_attention/gla/varlen_prefill.py` | 12.2% |
| `kernels/attention/gqa/paged_ws.py` | 12.3% |
| `kernels/attention/mla/decode.py` | 12.3% |
| `kernels/sampling/top_p_mask.py` | 12.4% |
| `kernels/quantization/int8_quant_per_tensor.py` | 12.9% |
| `kernels/attention/gqa/paged_fp8_decode.py` | 13.0% |
| `kernels/attention/nsa/compressed_varlen.py` | 13.5% |
| `kernels/linear_attention/gla/dense_prefill_partitioned.py` | 14.7% |
| `kernels/linear_attention/gla/varlen_prefill_partitioned.py` | 15.1% |
| `kernels/linear_attention/chunk_prefill.py` | 15.4% |
| `kernels/quantization/int8_quant_per_channel.py` | 15.5% |
| `kernels/quantization/int8_quant_per_block.py` | 16.0% |
| `kernels/linear_attention/gla/dense_prefill_subchunk.py` | 16.7% |
| `kernels/attention/gqa/decode_fp8.py` | 16.9% |
| `kernels/moe/indexed_expert_gemm.py` | 17.0% |
| `kernels/gemm/grouped/general.py` | 17.2% |
| `kernels/attention/gqa/prefill_paged_ws.py` | 17.6% |
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
| `ops/op_base.py` | 161 | 67.9% |
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
