# ✅ TileOPs Nightly Report

> **2026-10-06 20:07** &ensp;|&ensp; `991aebf6` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Operators** | 188 |
| **Kernels** | 294 |
| **Specs** | 17 |
| **Workloads** | 1220 |
| **Correctness** | ✅ &ensp; (188/188 ops verified, 1023/1023 tests) |
| **Benchmarked Ops** | 189 |
| **Benchmark Failures** | ✅ None &ensp;|&ensp; ⚠️ 1 skipped |
| **Regressions** (vs 14-day median) | ✅ None |
| **Baseline Alerts** (< 80%) | ⚠️ 200 |
| **vs Baseline** | ↑ 1452 &ensp;·&ensp; ↓ 476 &ensp;/&ensp; 1928 rows |
| **Rows no reference checked** | ⚠️ 165 |
| **History window** | 14 runs, 2026-09-22 to 2026-10-05 |
| **Roofline anomalies** | ✅ None |
| **Improvements** (vs 14-day best) | 🎉 34 |
| **Moved since previous run** | 🔵 37 |
| **Never-built kernels** | ⚠️ 38 files **+4** &ensp;·&ensp; `kernels/linear_attention/gdn/prefill_forward.py` at 3.4% |
| **Untested roofline math** | 422 lines in `perf/` &ensp;·&ensp; `perf/formulas.py` at 17.4% |
| **Untested op logic** | 925 lines in `ops/` &ensp;·&ensp; 57.1% of branches taken |
| | <sub>coverage compared against the 2026-10-05 run; no figure means it held</sub> |

## 🎉 Performance Improvements (vs 14-day best)

| Op | Config | Prev Best (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-131072-float16] | 9.3382 | 2.0623 | -77.9% | 5.21 |
| **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-131072-bfloat16] | 9.4128 | 2.1551 | -77.1% | 4.98 |
| **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-262144-float16] | 9.3327 | 2.1631 | -76.8% | 4.96 |
| **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-262144-bfloat16] | 9.4408 | 2.2682 | -76.0% | 4.73 |
| **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-131072-float32] | 13.2173 | 4.1135 | -68.9% | 2.61 |
| **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-65536-float32] | 13.1634 | 4.1706 | -68.3% | 2.57 |
| **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-262144-float32] | 13.2109 | 4.2512 | -67.8% | 2.53 |
| **DeltaNetInferenceFwdOp** | test_deltanet_inference_bench[deltanet-1.3b-cont-b4-bfloat16] | 0.0805 | 0.0370 | -54.1% | 44.17 |
| **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-65536-bfloat16] | 3.9080 | 2.0643 | -47.2% | 5.20 |
| **LayerNormFwdOp** | test_layer_norm_bench[dit-xl-2-bfloat16] | 0.0059 | 0.0031 | -46.7% | 1.88 |
| **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-65536-float16] | 3.7582 | 2.0702 | -44.9% | 5.19 |
| **DeltaNetInferenceFwdOp** | test_deltanet_inference_bench[deltanet-1.3b-continue-bfloat16] | 0.0612 | 0.0344 | -43.9% | 11.88 |
| **Conv3dFwdOp** | test_conv3d_bench[unet-encoder-bias-bfloat16] | 0.1166 | 0.0669 | -42.7% | 207.95 |
| **Conv3dFwdOp** | test_conv3d_bench[unet-encoder-bfloat16] | 0.1171 | 0.0687 | -41.3% | 202.26 |
| **SoftmaxFwdOp** | test_softmax_bench[attn-weights-32k-bfloat16] | 0.0562 | 0.0361 | -35.7% | 4.64 |
| **RMSNormFwdOp** | test_rms_norm_bench[quack-throughput-131072-bfloat16] | 3.1414 | 2.0825 | -33.7% | 4.12 |
| **RMSNormFwdOp** | test_rms_norm_bench[quack-throughput-131072-float16] | 3.1323 | 2.0780 | -33.7% | 4.13 |
| **DeltaNetInferenceFwdOp** | test_deltanet_inference_bench[prefill-3000-bfloat16] | 0.0530 | 0.0356 | -32.8% | 16.66 |
| **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-32768-bfloat16] | 1.5374 | 1.0355 | -32.6% | 5.18 |
| **LogSoftmaxFwdOp** | test_log_softmax_bench[attn-weights-32k-bfloat16] | 0.0524 | 0.0353 | -32.6% | 4.75 |
| **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-32768-float16] | 1.5042 | 1.0225 | -32.0% | 5.25 |
| **RMSNormFwdOp** | test_rms_norm_bench[quack-throughput-262144-float16] | 3.1808 | 2.1720 | -31.7% | 3.95 |
| **RMSNormFwdOp** | test_rms_norm_bench[quack-throughput-262144-bfloat16] | 3.1840 | 2.1936 | -31.1% | 3.92 |
| **DeltaNetInferenceFwdOp** | test_deltanet_inference_bench[prefill-l2norm-ragged-bfloat16] | 0.0539 | 0.0377 | -30.0% | 11.98 |
| **DeltaNetInferenceFwdOp** | test_deltanet_inference_bench[prefill-2k-bfloat16] | 0.0447 | 0.0325 | -27.3% | 12.45 |
| **DeltaNetInferenceFwdOp** | test_deltanet_inference_bench[prefill-8k-bfloat16] | 0.0773 | 0.0567 | -26.7% | 28.57 |
| **DeltaNetInferenceFwdOp** | test_deltanet_inference_bench[varlen-4x1k-bfloat16] | 0.0410 | 0.0307 | -25.2% | 13.19 |
| **DeltaNetInferenceFwdOp** | test_deltanet_inference_bench[prefill-16k-bfloat16] | 0.1233 | 0.0937 | -24.0% | 34.55 |
| **DeltaNetInferenceFwdOp** | test_deltanet_inference_bench[prefill-12k-continued-bfloat16] | 0.1332 | 0.1047 | -21.4% | 23.19 |
| **Conv3dFwdOp** | test_conv3d_bench[video-down-float16] | 0.0216 | 0.0179 | -17.3% | 69.53 |
| **RMSNormFwdOp** | test_rms_norm_bench[quack-throughput-32768-bfloat16] | 1.2390 | 1.0264 | -17.2% | 4.18 |
| **RMSNormFwdOp** | test_rms_norm_bench[quack-throughput-32768-float16] | 1.2271 | 1.0182 | -17.0% | 4.22 |
| **Conv3dFwdOp** | test_conv3d_bench[video-down-bias-float16] | 0.0218 | 0.0181 | -16.8% | 68.57 |
| **Conv3dFwdOp** | test_conv3d_bench[unet-aspp-float16] | 0.0330 | 0.0288 | -12.7% | 70.78 |

## 🔵 Moved Since Previous Run

> Moves against the most recent reading. A row restored to its old level appears only here: returning is not a new 14-day record.

| Op | Config | Previous (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-131072-float16] | 9.3382 | 2.0623 | -77.9% | 5.21 |
| **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-131072-bfloat16] | 9.4143 | 2.1551 | -77.1% | 4.98 |
| **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-262144-float16] | 9.3354 | 2.1631 | -76.8% | 4.96 |
| **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-262144-bfloat16] | 9.4408 | 2.2682 | -76.0% | 4.73 |
| **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-131072-float32] | 13.2189 | 4.1135 | -68.9% | 2.61 |
| **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-65536-float32] | 13.1651 | 4.1706 | -68.3% | 2.57 |
| **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-262144-float32] | 13.2109 | 4.2512 | -67.8% | 2.53 |
| **DeltaNetInferenceFwdOp** | test_deltanet_inference_bench[deltanet-1.3b-cont-b4-bfloat16] | 0.0824 | 0.0370 | -55.1% | 44.17 |
| **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-65536-bfloat16] | 3.9097 | 2.0643 | -47.2% | 5.20 |
| **LayerNormFwdOp** | test_layer_norm_bench[dit-xl-2-bfloat16] | 0.0059 | 0.0031 | -46.7% | 1.88 |
| **DeltaNetInferenceFwdOp** | test_deltanet_inference_bench[deltanet-1.3b-continue-bfloat16] | 0.0630 | 0.0344 | -45.4% | 11.88 |
| **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-65536-float16] | 3.7582 | 2.0702 | -44.9% | 5.19 |
| **Conv3dFwdOp** | test_conv3d_bench[unet-encoder-bias-bfloat16] | 0.1175 | 0.0669 | -43.1% | 207.95 |
| **Conv3dFwdOp** | test_conv3d_bench[unet-encoder-bfloat16] | 0.1175 | 0.0687 | -41.5% | 202.26 |
| **SoftmaxFwdOp** | test_softmax_bench[attn-weights-32k-bfloat16] | 0.0567 | 0.0361 | -36.3% | 4.64 |
| **DeltaNetInferenceFwdOp** | test_deltanet_inference_bench[prefill-3000-bfloat16] | 0.0554 | 0.0356 | -35.8% | 16.66 |
| **RMSNormFwdOp** | test_rms_norm_bench[quack-throughput-131072-bfloat16] | 3.1416 | 2.0825 | -33.7% | 4.12 |
| **RMSNormFwdOp** | test_rms_norm_bench[quack-throughput-131072-float16] | 3.1324 | 2.0780 | -33.7% | 4.13 |
| **DeltaNetInferenceFwdOp** | test_deltanet_inference_bench[prefill-8k-bfloat16] | 0.0854 | 0.0567 | -33.6% | 28.57 |
| **DeltaNetInferenceFwdOp** | test_deltanet_inference_bench[prefill-2k-bfloat16] | 0.0489 | 0.0325 | -33.6% | 12.45 |
| **DeltaNetInferenceFwdOp** | test_deltanet_inference_bench[prefill-l2norm-ragged-bfloat16] | 0.0564 | 0.0377 | -33.1% | 11.98 |
| **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-32768-bfloat16] | 1.5390 | 1.0355 | -32.7% | 5.18 |
| **LogSoftmaxFwdOp** | test_log_softmax_bench[attn-weights-32k-bfloat16] | 0.0524 | 0.0353 | -32.6% | 4.75 |
| **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-32768-float16] | 1.5054 | 1.0225 | -32.1% | 5.25 |
| **RMSNormFwdOp** | test_rms_norm_bench[quack-throughput-262144-float16] | 3.1826 | 2.1720 | -31.8% | 3.95 |
| **RMSNormFwdOp** | test_rms_norm_bench[quack-throughput-262144-bfloat16] | 3.1840 | 2.1936 | -31.1% | 3.92 |
| **DeltaNetInferenceFwdOp** | test_deltanet_inference_bench[prefill-16k-bfloat16] | 0.1338 | 0.0937 | -30.0% | 34.55 |
| **DeltaNetInferenceFwdOp** | test_deltanet_inference_bench[varlen-4x1k-bfloat16] | 0.0437 | 0.0307 | -29.8% | 13.19 |
| **DeltaNetInferenceFwdOp** | test_deltanet_inference_bench[prefill-12k-continued-bfloat16] | 0.1440 | 0.1047 | -27.3% | 23.19 |
| **RMSNormFwdOp** | test_rms_norm_bench[quack-throughput-65536-float16] | 2.5833 | 2.0589 | -20.3% | 4.17 |
| **Conv3dFwdOp** | test_conv3d_bench[video-down-float16] | 0.0217 | 0.0179 | -17.8% | 69.53 |
| **AvgPool2dFwdOp** | test_avg_pool2d_bench[vision-3x3-s2-float16] | 0.0041 | 0.0034 | -17.3% | 1.18 |
| **RMSNormFwdOp** | test_rms_norm_bench[quack-throughput-32768-bfloat16] | 1.2391 | 1.0264 | -17.2% | 4.18 |
| **RMSNormFwdOp** | test_rms_norm_bench[quack-throughput-32768-float16] | 1.2289 | 1.0182 | -17.1% | 4.22 |
| **Conv3dFwdOp** | test_conv3d_bench[video-down-bias-float16] | 0.0218 | 0.0181 | -16.8% | 68.57 |
| **Conv3dFwdOp** | test_conv3d_bench[unet-aspp-float16] | 0.0331 | 0.0288 | -13.0% | 70.78 |
| **DeltaNetInferenceFwdOp** | test_deltanet_inference_bench[prefill-4k-bfloat16] | 0.1221 | 0.1083 | -11.3% | 59.63 |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 80%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h128-kv64k-bfloat16] | 32.9516 | 2.3951 | 7.3% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h128-kv48k-bfloat16] | 32.0464 | 2.3930 | 7.5% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h128-kv32k-bfloat16] | 30.1569 | 2.3821 | 7.9% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h64-kv64k-bfloat16] | 8.5198 | 0.7296 | 8.6% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h64-kv48k-bfloat16] | 8.2470 | 0.7189 | 8.7% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h64-kv32k-bfloat16] | 7.7567 | 0.7105 | 9.2% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h128-kv8k-bfloat16] | 24.7185 | 2.3497 | 9.5% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h64-kv8k-bfloat16] | 6.3296 | 0.6998 | 11.1% | flashmla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-long-context-float16] | 12.5281 | 1.4450 | 11.5% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-long-context-bfloat16] | 12.5197 | 1.4474 | 11.6% | fla |

<details>
<summary><strong>190 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-ragged-float16] | 0.9159 | 0.1575 | 17.2% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-ragged-bfloat16] | 0.9162 | 0.1578 | 17.2% | fla |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-32k-bfloat16] | 0.3930 | 0.0875 | 22.3% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[ds-v32-decode-b1-float8_e4m3fn] | 0.2866 | 0.0659 | 23.0% | torch-ref |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-mixed-float16] | 22.3732 | 5.2721 | 23.6% | fa3 |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-4x1k-float16] | 0.2741 | 0.0704 | 25.7% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-8x1k-float16] | 0.5203 | 0.1339 | 25.7% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-8x1k-bfloat16] | 0.5205 | 0.1342 | 25.8% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-4x1k-bfloat16] | 0.2742 | 0.0712 | 25.9% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-wide-gqa-float16] | 0.5242 | 0.1615 | 30.8% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-wide-gqa-bfloat16] | 0.5244 | 0.1627 | 31.0% | fla |
| 🔴 | **TopKSelectFwdOp** | test_topk_select_bench[ds-v32-topk-decode-b1] | 0.0634 | 0.0213 | 33.6% | flashinfer |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-rope-float16] | 41.8488 | 14.5635 | 34.8% | fa3 |
| 🔴 | **NSACompressedVarlenFwdOp** | test_nsa_compressed_fwd_varlen_bench[prefill-4x1k-float16] | 0.1458 | 0.0535 | 36.7% | fla |
| 🔴 | **NSACompressedVarlenFwdOp** | test_nsa_compressed_fwd_varlen_bench[prefill-8x1k-float16] | 0.2712 | 0.1005 | 37.0% | fla |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-32k-bfloat16] | 0.3934 | 0.1587 | 40.3% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-32k-float16] | 0.3936 | 0.1609 | 40.9% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-single-request-bfloat16] | 0.0552 | 0.0227 | 41.1% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-single-request-float16] | 0.0552 | 0.0227 | 41.2% | flashinfer |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-float16-float8_e4m3fn] | 56.2097 | 23.2919 | 41.4% | fa3 |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-rope-float16] | 1.6605 | 0.6883 | 41.4% | fa3 |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b1-float16] | 0.0557 | 0.0232 | 41.7% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b1-bfloat16] | 0.0558 | 0.0233 | 41.8% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b2-float16] | 0.0567 | 0.0237 | 41.8% | flashinfer |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t32] | 0.0137 | 0.0058 | 42.0% | vllm |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b2-bfloat16] | 0.0566 | 0.0238 | 42.0% | flashinfer |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t1] | 0.0120 | 0.0051 | 42.6% | vllm |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-256-float16] | 0.0249 | 0.0108 | 43.5% | quack |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b6-float16] | 0.0611 | 0.0267 | 43.7% | flashinfer |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-256-bfloat16] | 0.0250 | 0.0109 | 43.7% | quack |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b6-bfloat16] | 0.0611 | 0.0268 | 43.9% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-b-m4096-s128-float8_e4m3fn-bfloat16] | 0.3376 | 0.1511 | 44.8% | deepgemm |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-65536-bfloat16] | 5.9763 | 2.6814 | 44.9% | fla |
| 🔴 | **NSACompressedVarlenFwdOp** | test_nsa_compressed_fwd_varlen_bench[prefill-ragged-bfloat16] | 0.0396 | 0.0181 | 45.6% | fla |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-16384-bfloat16] | 1.5200 | 0.6940 | 45.7% | fla |
| 🔴 | **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[qwen3-ragged-odd-bfloat16-bfloat16] | 0.4007 | 0.1890 | 47.2% | fa3 |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv128k-bfloat16] | 9.9395 | 4.7546 | 47.8% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv96k-bfloat16] | 9.8558 | 4.7411 | 48.1% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv64k-bfloat16] | 9.6674 | 4.7091 | 48.7% | flashmla |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t512] | 0.0158 | 0.0078 | 49.1% | vllm |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-1024-7168-bfloat16] | 0.6797 | 0.3538 | 52.1% | fla |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx131072-float8_e4m3fn] | 8.7015 | 4.5415 | 52.2% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx131072-float8_e4m3fn] | 17.2530 | 9.0060 | 52.2% | deepgemm |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp8-4096-bfloat16] | 0.3848 | 0.2015 | 52.3% | fla |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx65536-float8_e4m3fn] | 8.4935 | 4.4579 | 52.5% | deepgemm |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv32k-bfloat16] | 8.8408 | 4.6495 | 52.6% | flashmla |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx65536-float8_e4m3fn] | 4.3248 | 2.2942 | 53.0% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx32768-float8_e4m3fn] | 4.1156 | 2.1934 | 53.3% | deepgemm |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[ds-v3-t1] | 0.0096 | 0.0052 | 53.7% | vllm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx32768-float8_e4m3fn] | 2.1262 | 1.1480 | 54.0% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx16384-float8_e4m3fn] | 1.9368 | 1.0577 | 54.6% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx16384-float8_e4m3fn] | 1.0402 | 0.5706 | 54.9% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx8192-float8_e4m3fn] | 0.8633 | 0.4755 | 55.1% | deepgemm |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp4-16384-bfloat16] | 1.6748 | 0.9274 | 55.4% | fla |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx8192-float8_e4m3fn] | 0.5022 | 0.2784 | 55.4% | deepgemm |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp4-65536-bfloat16] | 6.4447 | 3.5957 | 55.8% | fla |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[gemma-2b-bfloat16] | 0.3010 | 0.1692 | 56.2% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-4x2048-bfloat16] | 0.2546 | 0.1431 | 56.2% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q2048-ctx4096-float8_e4m3fn] | 0.2332 | 0.1317 | 56.5% | deepgemm |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[ds-v3-t32] | 0.0100 | 0.0057 | 56.7% | vllm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-16x8192-bfloat16] | 0.8211 | 0.4699 | 57.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-4x2048-float16] | 0.2476 | 0.1428 | 57.7% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-a-m4096-s128-float8_e4m3fn-bfloat16] | 0.0748 | 0.0432 | 57.8% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x8192-bfloat16] | 0.8052 | 0.4676 | 58.1% | flashinfer |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv8k-bfloat16] | 7.9775 | 4.6390 | 58.1% | flashmla |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[index-q4096-ctx4096-float8_e4m3fn] | 0.3262 | 0.1898 | 58.2% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-16x8192-float16] | 0.7960 | 0.4660 | 58.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x8192-float16] | 0.7824 | 0.4670 | 59.7% | flashinfer |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp4-4096-bfloat16] | 0.4351 | 0.2638 | 60.6% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4096-4096-bfloat16] | 0.4175 | 0.2536 | 60.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x1024-bfloat16] | 0.1417 | 0.0864 | 61.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-8x1024-float16] | 0.1372 | 0.0860 | 62.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x1024-bfloat16] | 0.2602 | 0.1631 | 62.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4096-4096-float16] | 0.4030 | 0.2529 | 62.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x8192-bfloat16] | 2.1766 | 1.3792 | 63.4% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-a-m128-s128-float8_e4m3fn-bfloat16] | 0.0208 | 0.0132 | 63.4% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x8192-bfloat16] | 0.7438 | 0.4724 | 63.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-32x8192-bfloat16] | 1.4487 | 0.9208 | 63.6% | flashinfer |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp2-65536-bfloat16] | 8.4370 | 5.3678 | 63.6% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-16x8192-bfloat16] | 1.4522 | 0.9244 | 63.7% | flashinfer |
| 🔴 | **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-float16-float16] | 0.7925 | 0.5058 | 63.8% | fa3 |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-mlp-up-m128-s128-float8_e4m3fn-bfloat16] | 0.0271 | 0.0173 | 63.9% | deepgemm |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[starcoder-float16] | 0.7874 | 0.5035 | 63.9% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-32x8192-bfloat16] | 2.8596 | 1.8308 | 64.0% | flashinfer |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp2-16384-bfloat16] | 2.1514 | 1.3777 | 64.0% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-16x8192-bfloat16] | 2.8804 | 1.8453 | 64.1% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-b-m128-s128-float8_e4m3fn-bfloat16] | 0.0183 | 0.0118 | 64.5% | deepgemm |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[ds-v32-kv2k-bfloat16] | 1.9081 | 1.2299 | 64.5% | flashmla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x1024-float16] | 0.2515 | 0.1624 | 64.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-4x2048-bfloat16] | 0.2277 | 0.1471 | 64.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x8192-bfloat16] | 2.8561 | 1.8487 | 64.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x8192-bfloat16] | 1.4374 | 0.9307 | 64.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x8192-bfloat16] | 1.4323 | 0.9293 | 64.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x8192-float16] | 2.1146 | 1.3737 | 65.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-4x2048-bfloat16] | 0.2221 | 0.1444 | 65.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp8-32x8192-float16] | 1.4066 | 0.9168 | 65.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-16x8192-float16] | 1.4079 | 0.9177 | 65.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x8192-float16] | 0.7215 | 0.4714 | 65.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp4-32x8192-float16] | 2.7708 | 1.8180 | 65.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4x2048-bfloat16] | 0.4163 | 0.2732 | 65.6% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-32768-bfloat16] | 3.2757 | 2.1541 | 65.8% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-16x8192-float16] | 2.7799 | 1.8306 | 65.8% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[context-chunk-bfloat16] | 0.3201 | 0.2111 | 66.0% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x8192-float16] | 2.7726 | 1.8331 | 66.1% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-o-proj-m128-s1-float8_e4m3fn-bfloat16] | 0.0930 | 0.0615 | 66.1% | deepgemm |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-32768-float16] | 3.2776 | 2.1692 | 66.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-16x8192-bfloat16] | 4.1425 | 2.7468 | 66.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-8x8192-float16] | 1.3904 | 0.9241 | 66.5% | flashinfer |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[ds-v3-t512] | 0.0119 | 0.0079 | 66.5% | vllm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x8192-float16] | 1.3938 | 0.9273 | 66.5% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-a-m4096-s1-float8_e4m3fn-bfloat16] | 0.0868 | 0.0578 | 66.6% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-4x2048-float16] | 0.2200 | 0.1465 | 66.6% | flashinfer |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-512-float16] | 0.0276 | 0.0184 | 66.7% | quack |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-32x8192-bfloat16] | 8.1763 | 5.4562 | 66.7% | flashinfer |
| 🔴 | **KDAFwdOp** | test_kda_fwd_bench[kda-tp2-4096-bfloat16] | 0.5532 | 0.3693 | 66.8% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-16x8192-bfloat16] | 1.3899 | 0.9300 | 66.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-16x8192-bfloat16] | 5.4738 | 3.6721 | 67.1% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-32x8192-bfloat16] | 10.8747 | 7.3086 | 67.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-32x8192-bfloat16] | 5.4559 | 3.6687 | 67.2% | flashinfer |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-512-bfloat16] | 0.0274 | 0.0185 | 67.3% | quack |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-4x2048-float16] | 0.2151 | 0.1448 | 67.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-4x2048-float16] | 0.4016 | 0.2714 | 67.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-32x8192-bfloat16] | 2.7180 | 1.8389 | 67.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x8192-bfloat16] | 1.3813 | 0.9350 | 67.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-32x8192-bfloat16] | 5.4139 | 3.6658 | 67.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-16x8192-bfloat16] | 2.7308 | 1.8500 | 67.8% | flashinfer |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[ds-v32-kv4k-bfloat16] | 0.5122 | 0.3473 | 67.8% | flashmla |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-q-b-m128-s128-float8_e4m3fn-bfloat16] | 0.0282 | 0.0192 | 67.8% | deepgemm |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t4096] | 0.0378 | 0.0257 | 67.8% | vllm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-16x8192-bfloat16] | 2.7230 | 1.8495 | 67.9% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-kscale-float8_e4m3fn] | 0.4709 | 0.3206 | 68.1% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-16x8192-float16] | 4.0084 | 2.7306 | 68.1% | flashinfer |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-256-float32] | 0.0266 | 0.0181 | 68.2% | torch-compile |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-16x8192-float16] | 5.3187 | 3.6450 | 68.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-32x8192-float16] | 7.9244 | 5.4328 | 68.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-16x8192-float16] | 1.3429 | 0.9223 | 68.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-16x8192-float16] | 2.6585 | 1.8307 | 68.9% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp2-32x8192-float16] | 5.2716 | 3.6382 | 69.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-32x8192-float16] | 10.4861 | 7.2618 | 69.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-32x8192-float16] | 2.6392 | 1.8276 | 69.2% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-16384-bfloat16] | 1.5746 | 1.0909 | 69.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-16x8192-float16] | 2.6513 | 1.8372 | 69.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x8192-float16] | 1.3371 | 0.9277 | 69.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-32x8192-float16] | 5.2239 | 3.6374 | 69.6% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-8192-bfloat16] | 0.8036 | 0.5605 | 69.8% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-16384-float16] | 1.5769 | 1.1017 | 69.9% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-o-proj-float8_e4m3fn-bfloat16] | 1.5453 | 1.0820 | 70.0% | deepgemm |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-8192-float16] | 0.8031 | 0.5634 | 70.2% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-serving-batch-float16] | 0.0884 | 0.0620 | 70.2% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-serving-batch-bfloat16] | 0.0883 | 0.0620 | 70.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-32x8192-bfloat16] | 5.2132 | 3.6698 | 70.4% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-o-proj-m128-s128-float8_e4m3fn-bfloat16] | 0.0666 | 0.0471 | 70.8% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-float16-float8_e4m3fn] | 1.9621 | 1.3932 | 71.0% | fa3 |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-4096-bfloat16] | 0.4159 | 0.2983 | 71.7% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-32x8192-float16] | 5.0718 | 3.6414 | 71.8% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-b128-4096-float16] | 0.4173 | 0.2997 | 71.8% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-float8_e4m3fn] | 0.5142 | 0.3712 | 72.2% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4096-4096-bfloat16] | 0.3385 | 0.2446 | 72.3% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-bfloat16] | 0.5289 | 0.3831 | 72.4% | deepgemm |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-qkv-a-2d-float8_e4m3fn-bfloat16] | 0.1525 | 0.1120 | 73.5% | deepgemm |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-q-b-2d-float8_e4m3fn-bfloat16] | 0.3571 | 0.2645 | 74.1% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x1024-bfloat16] | 0.3200 | 0.2375 | 74.2% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4096-4096-float16] | 0.3261 | 0.2432 | 74.6% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-down-2d-float8_e4m3fn-bfloat16] | 0.1449 | 0.1087 | 75.0% | deepgemm |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x1024-bfloat16] | 0.1171 | 0.0882 | 75.3% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x1024-bfloat16] | 0.4112 | 0.3106 | 75.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x1024-bfloat16] | 0.2204 | 0.1667 | 75.6% | flashinfer |
| 🔴 | **DeltaNetChunkBwdOp** | test_deltanet_vs_fla_bwd[deltanet-1.3b-train-bfloat16] | 0.0718 | 0.0544 | 75.8% | fla |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x1024-bfloat16] | 0.2152 | 0.1643 | 76.3% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-4k-float16] | 0.1179 | 0.0902 | 76.5% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-4k-bfloat16] | 0.1173 | 0.0898 | 76.6% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-8x1024-float16] | 0.3080 | 0.2364 | 76.7% | flashinfer |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[qwen3-235b-t32] | 0.0070 | 0.0054 | 77.2% | vllm |
| 🔴 | **GLAChunkFwdOp** | test_gla_fwd_bench[train-16k-float16] | 0.6160 | 0.4755 | 77.2% | fla |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_decode_bench[falcon-7b-2k-bfloat16] | 0.0371 | 0.0288 | 77.8% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-2b-8x1024-float16] | 0.1124 | 0.0876 | 78.0% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-symmetric-8x1024-float16] | 0.2125 | 0.1662 | 78.2% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b64-bfloat16] | 0.1288 | 0.1010 | 78.4% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-35b-8x1024-float16] | 0.2081 | 0.1633 | 78.5% | flashinfer |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-397b-tp1-8x1024-float16] | 0.3948 | 0.3100 | 78.5% | flashinfer |
| 🔴 | **DeltaNetChunkBwdOp** | test_deltanet_vs_fla_bwd[train-4k-float16] | 0.2731 | 0.2146 | 78.6% | fla |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-long-bfloat16] | 0.5644 | 0.4454 | 78.9% | fa3 |
| 🔴 | **GDNFwdOp** | test_gdn_fwd_bench[q35-27b-4x2048-bfloat16] | 0.3329 | 0.2630 | 79.0% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[mla-tp-b64-float16] | 0.1292 | 0.1021 | 79.0% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-o-proj-2d-float8_e4m3fn-bfloat16] | 0.8705 | 0.6883 | 79.1% | deepgemm |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-long-float16] | 0.5641 | 0.4462 | 79.1% | fa3 |
| 🔴 | **GLAChunkFwdOp** | test_gla_fwd_bench[train-4k-float16] | 0.1568 | 0.1243 | 79.3% | fla |
| 🔴 | **DeltaNetChunkBwdOp** | test_deltanet_vs_fla_bwd[train-4k-bfloat16] | 0.2724 | 0.2166 | 79.5% | fla |
| 🔴 | **GLAChunkFwdOp** | test_gla_fwd_bench[train-2k-bfloat16] | 0.0938 | 0.0747 | 79.7% | fla |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-mlp-up-2d-float8_e4m3fn-bfloat16] | 0.2423 | 0.1933 | 79.8% | deepgemm |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 38 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 422 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 925 lines in `ops/`, 57.1% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 2600 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

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
| `kernels/sampling/chain_speculative_sampling.py` | 11.5% |
| `kernels/sampling/sampling_from_probs.py` | 11.8% |
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
