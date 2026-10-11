# ❌ TileOPs Nightly Report

> **2026-10-04 19:54** &ensp;|&ensp; `10e653b3` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Operators** | 186 |
| **Kernels** | 284 |
| **Specs** | 19 |
| **Workloads** | 1173 |
| **Correctness** | ✅ &ensp; (183/186 ops verified, 1044/1044 tests) |
| **Benchmarked Ops** | 186 |
| **Benchmark Failures** | ❌ 76 |
| **Regressions** (vs 14-day median) | ✅ None |
| **Baseline Alerts** (< 80%) | ⚠️ 195 |
| **vs Baseline** | ↑ 1358 &ensp;·&ensp; ↓ 467 &ensp;/&ensp; 1825 rows |
| **Rows no reference checked** | ⚠️ 85 |
| **History window** | 14 runs, 2026-09-20 to 2026-10-03 |
| **Roofline anomalies** | ✅ None |
| **Never-built kernels** | ⚠️ 32 files &ensp;·&ensp; `kernels/linear_attention/gated_deltanet/prefill_forward.py` at 3.0% |
| **Untested roofline math** | 422 lines in `perf/` &ensp;·&ensp; `perf/formulas.py` at 17.4% |
| **Untested op logic** | 894 lines in `ops/` &ensp;·&ensp; 60.4% of branches taken |
| | <sub>coverage compared against the 2026-10-03 run; no figure means it held</sub> |

## ❌ Benchmark Failures

| Test | Error |
|:-----|:------|
| test_chain_speculative_sampling_bench[llama-8b-b16-n4] | AssertionError: flashinfer: |
| test_chain_speculative_sampling_bench[llama-8b-b64-n4] | AssertionError: flashinfer: |
| test_chain_speculative_sampling_bench[ds-v3-mtp-n1] | AssertionError: flashinfer: |
| test_chain_speculative_sampling_bench[ds-v3-mtp-n3] | AssertionError: flashinfer: |
| test_chain_speculative_sampling_bench[qwen3-235b-eagle-n5] | AssertionError: flashinfer: |
| test_chain_speculative_sampling_bench[llama-8b-b17-n8] | AssertionError: flashinfer: |
| test_chain_speculative_sampling_bench[llama2-7b-b256-n1] | AssertionError: flashinfer: |
| test_conv2d_bench[deeplabv3-aspp-float16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 104 / 262144 (0.0%)
Greatest absolute differe... |
| test_cumsum_bench[llama-13b-hidden-float32] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 3 / 20971520 (0.0%)
Greatest absolute differe... |
| test_mla_decode_bench[ds-v2-4k-bfloat16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 7305 / 2097152 (0.3%)
Greatest absolute diffe... |
| test_mla_decode_bench[ds-v3-4k-bfloat16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 3668 / 1048576 (0.3%)
Greatest absolute diffe... |
| test_mla_decode_bench[ds-v3-single-request-bfloat16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 247 / 65536 (0.4%)
Greatest absolute differen... |
| test_mla_decode_bench[ds-v3-serving-batch-bfloat16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 618 / 786432 (0.1%)
Greatest absolute differe... |
| test_mla_decode_bench[ds-mla-b128-4096-bfloat16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 178 / 8388608 (0.0%)
Greatest absolute differ... |
| test_mla_decode_bench[ds-mla-b128-8192-bfloat16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 1 / 8388608 (0.0%)
Greatest absolute differen... |
| test_mla_decode_bench[deepseek-mla-tp-batch1-bfloat16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 128 / 32768 (0.4%)
Greatest absolute differen... |
| test_mla_decode_bench[deepseek-mla-tp-batch2-bfloat16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 257 / 65536 (0.4%)
Greatest absolute differen... |
| test_mla_decode_bench[deepseek-mla-tp-batch6-bfloat16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 568 / 196608 (0.3%)
Greatest absolute differe... |
| test_mla_decode_bench[deepseek-mla-tp-batch64-bfloat16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 6771 / 2097152 (0.3%)
Greatest absolute diffe... |
| test_gated_deltanet_fwd_bench[decode-b1-float16] | AssertionError: flashinfer: Tensor-likes are not close!

Mismatched elements: 57 / 2048 (2.8%)
Greatest absolute differe... |
| test_gated_deltanet_fwd_bench[decode-b1-bfloat16] | AssertionError: flashinfer: Tensor-likes are not close!

Mismatched elements: 922 / 2048 (45.0%)
Greatest absolute diffe... |
| test_gated_deltanet_fwd_bench[decode-b8-float16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 2 / 32768 (0.0%)
Greatest absolute difference... |
| test_gated_deltanet_fwd_bench[decode-b8-bfloat16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 3 / 32768 (0.0%)
Greatest absolute difference... |
| test_gated_deltanet_fwd_bench[decode-fresh-bfloat16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 7 / 32768 (0.0%)
Greatest absolute difference... |
| test_gated_deltanet_fwd_bench[decode-vfirst-b17-bfloat16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 1 / 26112 (0.0%)
Greatest absolute difference... |
| test_gated_deltanet_fwd_bench[q35-gva-decode-b1-float16] | AssertionError: flashinfer: Tensor-likes are not close!

Mismatched elements: 147 / 4096 (3.6%)
Greatest absolute differ... |
| test_gated_deltanet_fwd_bench[q35-gva-decode-b1-bfloat16] | AssertionError: flashinfer: Tensor-likes are not close!

Mismatched elements: 1812 / 4096 (44.2%)
Greatest absolute diff... |
| test_gated_deltanet_fwd_bench[q35-gva-decode-b4-float16] | AssertionError: flashinfer: Tensor-likes are not close!

Mismatched elements: 435 / 16384 (2.7%)
Greatest absolute diffe... |
| test_gated_deltanet_fwd_bench[q35-gva-decode-b4-bfloat16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 3 / 16384 (0.0%)
Greatest absolute difference... |
| test_gated_deltanet_fwd_bench[q35-gva-decode-b8-float16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 1 / 32768 (0.0%)
Greatest absolute difference... |
| test_gated_deltanet_fwd_bench[q35-gva-decode-b8-bfloat16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 2 / 32768 (0.0%)
Greatest absolute difference... |
| test_gated_deltanet_fwd_bench[q35-gva-decode-b16-float16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 4 / 65536 (0.0%)
Greatest absolute difference... |
| test_gated_deltanet_fwd_bench[q35-gva-decode-b16-bfloat16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 4 / 65536 (0.0%)
Greatest absolute difference... |
| test_gated_deltanet_fwd_bench[q35-gva-decode-b32-float16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 3 / 131072 (0.0%)
Greatest absolute differenc... |
| test_gated_deltanet_fwd_bench[q35-gva-decode-b32-bfloat16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 5 / 131072 (0.0%)
Greatest absolute differenc... |
| test_gated_deltanet_fwd_bench[q35-gva-decode-b64-float16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 6 / 262144 (0.0%)
Greatest absolute differenc... |
| test_gated_deltanet_fwd_bench[q35-gva-decode-b64-bfloat16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 23 / 262144 (0.0%)
Greatest absolute differen... |
| test_gated_deltanet_fwd_bench[q35-gva-decode-b128-float16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 14 / 524288 (0.0%)
Greatest absolute differen... |
| test_gated_deltanet_fwd_bench[q35-gva-decode-b128-bfloat16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 34 / 524288 (0.0%)
Greatest absolute differen... |
| test_gated_deltanet_fwd_bench[q35-gva-decode-b256-float16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 21 / 1048576 (0.0%)
Greatest absolute differe... |
| test_gated_deltanet_fwd_bench[q35-gva-decode-b256-bfloat16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 75 / 1048576 (0.0%)
Greatest absolute differe... |
| test_gated_deltanet_fwd_bench[q35-gva-decode-b512-float16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 64 / 2097152 (0.0%)
Greatest absolute differe... |
| test_gated_deltanet_fwd_bench[q35-gva-decode-b512-bfloat16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 131 / 2097152 (0.0%)
Greatest absolute differ... |
| test_gqa_bwd_bench[llama-8b-short-bfloat16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 1331 / 8388608 (0.0%)
Greatest absolute diffe... |
| test_gqa_bwd_bench[llama-8b-long-bfloat16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 833 / 16777216 (0.0%)
Greatest absolute diffe... |
| test_gqa_bwd_bench[llama-70b-short-float16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 8 / 1048576 (0.0%)
Greatest absolute differen... |
| test_gqa_bwd_bench[llama-70b-short-bfloat16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 1281 / 8388608 (0.0%)
Greatest absolute diffe... |
| test_gqa_bwd_bench[llama-70b-long-float16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 2 / 2097152 (0.0%)
Greatest absolute differen... |
| test_gqa_bwd_bench[llama-70b-long-bfloat16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 701 / 16777216 (0.0%)
Greatest absolute diffe... |
| test_gqa_bwd_bench[llama-8b-short-mha-bfloat16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 1329 / 8388608 (0.0%)
Greatest absolute diffe... |
| test_gqa_bwd_bench[llama-8b-long-mha-bfloat16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 692 / 16777216 (0.0%)
Greatest absolute diffe... |
| test_gqa_bwd_bench[llama-70b-short-mha-bfloat16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 1273 / 8388608 (0.0%)
Greatest absolute diffe... |
| test_gqa_bwd_bench[llama-70b-long-mha-bfloat16] | AssertionError: tileops: Tensor-likes are not close!

Mismatched elements: 619 / 16777216 (0.0%)
Greatest absolute diffe... |
| test_int8_quant_per_block_bench[ds-v3-prefill-float16] | AssertionError: torch-compile: Tensor-likes are not equal!

Mismatched elements: 1689 / 29360128 (0.0%)
Greatest absolut... |
| test_int8_quant_per_block_bench[ds-v3-prefill-bfloat16] | AssertionError: torch-compile: Tensor-likes are not equal!

Mismatched elements: 9016 / 29360128 (0.0%)
Greatest absolut... |
| test_int8_quant_per_block_bench[ds-v3-decode-bfloat16] | AssertionError: torch-compile: Tensor-likes are not equal!

Mismatched elements: 166 / 458752 (0.0%)
Greatest absolute d... |
| test_int8_quant_per_block_bench[qwen3-235b-prefill-bfloat16] | AssertionError: torch-compile: Tensor-likes are not equal!

Mismatched elements: 5225 / 16777216 (0.0%)
Greatest absolut... |
| test_int8_quant_per_block_bench[qwen3-235b-prefill-float32] | AssertionError: torch-compile: Tensor-likes are not equal!

Mismatched elements: 13 / 16777216 (0.0%)
Greatest absolute ... |
| test_int8_quant_per_block_bench[ds-v3-decode-few-tokens-bfloat16] | AssertionError: torch-compile: Tensor-likes are not equal!

Mismatched elements: 51 / 121856 (0.0%)
Greatest absolute di... |
| test_int8_quant_per_block_bench[gpt-oss-20b-prefill-bfloat16] | AssertionError: torch-compile: Tensor-likes are not equal!

Mismatched elements: 2660 / 8640000 (0.0%)
Greatest absolute... |
| test_int8_quant_per_block_bench[ragged-k-float16] | AssertionError: torch-compile: Tensor-likes are not equal!

Mismatched elements: 269 / 4099000 (0.0%)
Greatest absolute ... |
| test_int8_quant_per_tensor_bench[qwen3-32b-prefill-float32] | AssertionError: torch-compile: quantized codes differ |
| test_fused_moe_shared_expert_bench[kimi-k2-t32-bfloat16] | torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 21.00 GiB. GPU 0 has a total capacity of 139.80 GiB of whi... |
| test_fused_moe_shared_expert_bench[kimi-k2-t64-bfloat16] | torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 21.00 GiB. GPU 0 has a total capacity of 139.80 GiB of whi... |
| test_fused_moe_shared_expert_bench[kimi-k2-t128-bfloat16] | torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 21.00 GiB. GPU 0 has a total capacity of 139.80 GiB of whi... |
| test_fused_moe_shared_expert_bench[kimi-k2-t512-bfloat16] | torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 21.00 GiB. GPU 0 has a total capacity of 139.80 GiB of whi... |
| test_fused_moe_shared_expert_bench[kimi-k2-t2048-bfloat16] | torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 21.00 GiB. GPU 0 has a total capacity of 139.80 GiB of whi... |
| test_fused_moe_shared_expert_bench[kimi-k2-t4096-bfloat16] | torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 21.00 GiB. GPU 0 has a total capacity of 139.80 GiB of whi... |
| test_fused_moe_shared_expert_bench[ds-v3-t1-bfloat16] | torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 14.00 GiB. GPU 0 has a total capacity of 139.80 GiB of whi... |
| test_fused_moe_shared_expert_bench[ds-v3-t32-bfloat16] | torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 14.00 GiB. GPU 0 has a total capacity of 139.80 GiB of whi... |
| test_fused_moe_shared_expert_bench[ds-v3-t32-float16] | torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 14.00 GiB. GPU 0 has a total capacity of 139.80 GiB of whi... |
| test_fused_moe_shared_expert_bench[ds-v3-t64-bfloat16] | torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 14.00 GiB. GPU 0 has a total capacity of 139.80 GiB of whi... |
| test_fused_moe_shared_expert_bench[ds-v3-t128-bfloat16] | torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 14.00 GiB. GPU 0 has a total capacity of 139.80 GiB of whi... |
| test_fused_moe_shared_expert_bench[ds-v3-t512-bfloat16] | torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 14.00 GiB. GPU 0 has a total capacity of 139.80 GiB of whi... |
| test_fused_moe_shared_expert_bench[ds-v3-t2048-bfloat16] | torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 14.00 GiB. GPU 0 has a total capacity of 139.80 GiB of whi... |
| test_fused_moe_shared_expert_bench[ds-v3-t4096-bfloat16] | torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 14.00 GiB. GPU 0 has a total capacity of 139.80 GiB of whi... |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 80%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h128-kv64k-bfloat16] | 32.9078 | 2.4023 | 7.3% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h128-kv48k-bfloat16] | 31.9302 | 2.3941 | 7.5% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h128-kv32k-bfloat16] | 30.1602 | 2.3853 | 7.9% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h64-kv64k-bfloat16] | 8.5106 | 0.7281 | 8.6% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h64-kv48k-bfloat16] | 8.2489 | 0.7188 | 8.7% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h64-kv32k-bfloat16] | 7.7603 | 0.7108 | 9.2% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h128-kv8k-bfloat16] | 24.7952 | 2.3473 | 9.5% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d512-h64-kv8k-bfloat16] | 6.3330 | 0.7004 | 11.1% | flashmla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-long-context-float16] | 12.5233 | 1.4458 | 11.6% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-long-context-bfloat16] | 12.5253 | 1.4473 | 11.6% | fla |

<details>
<summary><strong>185 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-ragged-float16] | 0.9177 | 0.1576 | 17.2% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-ragged-bfloat16] | 0.9116 | 0.1580 | 17.3% | fla |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-32k-bfloat16] | 0.3930 | 0.0871 | 22.2% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[ds-v32-indexer-decode-b1-float8_e4m3fn] | 0.2870 | 0.0660 | 23.0% | torch-ref |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-mixed-float16] | 22.3781 | 5.2848 | 23.6% | fa3 |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-131072-float16] | 9.3452 | 2.2454 | 24.0% | quack |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-131072-bfloat16] | 9.4128 | 2.3084 | 24.5% | quack |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-4x1k-float16] | 0.2739 | 0.0704 | 25.7% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-8x1k-float16] | 0.5201 | 0.1344 | 25.8% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-8x1k-bfloat16] | 0.5203 | 0.1345 | 25.8% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-4x1k-bfloat16] | 0.2745 | 0.0711 | 25.9% | fla |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-262144-float16] | 9.3353 | 2.4224 | 25.9% | quack |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-262144-bfloat16] | 9.4420 | 2.5126 | 26.6% | quack |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-wide-gqa-float16] | 0.5239 | 0.1615 | 30.8% | fla |
| 🔴 | **NSATopKVarlenFwdOp** | test_nsa_topk_varlen_bench[prefill-wide-gqa-bfloat16] | 0.5252 | 0.1625 | 30.9% | fla |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-65536-float32] | 13.1634 | 4.3767 | 33.2% | quack |
| 🔴 | **TopKSelectFwdOp** | test_topk_select_bench[ds-v32-topk-decode-b1] | 0.0632 | 0.0214 | 33.9% | flashinfer |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-rope-float16] | 41.8836 | 14.4100 | 34.4% | fa3 |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-131072-float32] | 13.2173 | 4.7846 | 36.2% | quack |
| 🔴 | **NSACompressedVarlenFwdOp** | test_nsa_compressed_fwd_varlen_bench[prefill-4x1k-float16] | 0.1457 | 0.0535 | 36.7% | fla |
| 🔴 | **NSACompressedVarlenFwdOp** | test_nsa_compressed_fwd_varlen_bench[prefill-8x1k-float16] | 0.2711 | 0.1008 | 37.2% | fla |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-262144-float32] | 13.2114 | 4.9179 | 37.2% | quack |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-32k-bfloat16] | 0.3935 | 0.1596 | 40.6% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-32k-float16] | 0.3934 | 0.1609 | 40.9% | flashinfer |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-rope-float16] | 1.6682 | 0.6867 | 41.2% | fa3 |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-single-request-float16] | 0.0553 | 0.0229 | 41.4% | flashinfer |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[qwen35-9b-float16-float8_e4m3fn] | 56.2264 | 23.3024 | 41.4% | fa3 |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[deepseek-mla-tp-batch1-float16] | 0.0558 | 0.0233 | 41.7% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[deepseek-mla-tp-batch2-float16] | 0.0566 | 0.0236 | 41.8% | flashinfer |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t32] | 0.0137 | 0.0058 | 42.0% | vllm |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t1] | 0.0122 | 0.0051 | 42.1% | vllm |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-256-float16] | 0.0249 | 0.0108 | 43.4% | quack |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-256-bfloat16] | 0.0250 | 0.0109 | 43.6% | quack |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[deepseek-mla-tp-batch6-float16] | 0.0612 | 0.0268 | 43.8% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-b-m4096-s128-float8_e4m3fn-bfloat16] | 0.3380 | 0.1511 | 44.7% | deepgemm |
| 🔴 | **NSACompressedVarlenFwdOp** | test_nsa_compressed_fwd_varlen_bench[nsa-ragged-prefill-bf16-bfloat16] | 0.0397 | 0.0180 | 45.4% | fla |
| 🔴 | **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[qwen3-ragged-odd-bfloat16-bfloat16] | 0.4011 | 0.1894 | 47.2% | fa3 |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv128k-bfloat16] | 9.9373 | 4.7533 | 47.8% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv96k-bfloat16] | 9.8670 | 4.7312 | 47.9% | flashmla |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv64k-bfloat16] | 9.6723 | 4.7045 | 48.6% | flashmla |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t512] | 0.0158 | 0.0078 | 49.1% | vllm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[ds-index-q4096-ctx131072-float8_e4m3fn] | 17.2751 | 8.9710 | 51.9% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[ds-index-q2048-ctx131072-float8_e4m3fn] | 8.7442 | 4.5538 | 52.1% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[ds-index-q4096-ctx65536-float8_e4m3fn] | 8.5146 | 4.4598 | 52.4% | deepgemm |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv32k-bfloat16] | 8.8315 | 4.6577 | 52.7% | flashmla |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[ds-index-q2048-ctx65536-float8_e4m3fn] | 4.3079 | 2.2892 | 53.1% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[ds-index-q4096-ctx32768-float8_e4m3fn] | 4.1134 | 2.1944 | 53.3% | deepgemm |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[ds-v3-t1] | 0.0096 | 0.0052 | 53.7% | vllm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[ds-index-q4096-ctx16384-float8_e4m3fn] | 1.9386 | 1.0509 | 54.2% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[ds-index-q2048-ctx32768-float8_e4m3fn] | 2.1266 | 1.1544 | 54.3% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[ds-index-q4096-ctx8192-float8_e4m3fn] | 0.8633 | 0.4741 | 54.9% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[ds-index-q2048-ctx16384-float8_e4m3fn] | 1.0394 | 0.5719 | 55.0% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[ds-index-q2048-ctx8192-float8_e4m3fn] | 0.5026 | 0.2795 | 55.6% | deepgemm |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[gemma-2b-bfloat16] | 0.3014 | 0.1697 | 56.3% | fa3 |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[ds-index-q2048-ctx4096-float8_e4m3fn] | 0.2333 | 0.1316 | 56.4% | deepgemm |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[ds-v3-t32] | 0.0100 | 0.0056 | 56.6% | vllm |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-65536-bfloat16] | 3.9120 | 2.2309 | 57.0% | quack |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-65536-float16] | 3.7658 | 2.1683 | 57.6% | quack |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-a-m4096-s128-float8_e4m3fn-bfloat16] | 0.0749 | 0.0432 | 57.7% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[ds-index-q4096-ctx4096-float8_e4m3fn] | 0.3267 | 0.1895 | 58.0% | deepgemm |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp2-4x2048-float16] | 0.2465 | 0.1432 | 58.1% | flashinfer |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[mla-d576-h128-kv8k-bfloat16] | 7.9635 | 4.6303 | 58.1% | flashmla |
| 🔴 | **LayerNormFwdOp** | test_layer_norm_bench[dit-xl-2-bfloat16] | 0.0059 | 0.0034 | 58.1% | quack |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp2-4x2048-bfloat16] | 0.2464 | 0.1434 | 58.2% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp8-16x8192-bfloat16] | 0.8007 | 0.4672 | 58.3% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp8-16x8192-float16] | 0.7974 | 0.4660 | 58.5% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp4-8x8192-bfloat16] | 0.7873 | 0.4682 | 59.5% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp4-8x8192-float16] | 0.7837 | 0.4668 | 59.6% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp1-4096-4096-float16] | 0.4048 | 0.2520 | 62.3% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp1-4096-4096-bfloat16] | 0.4039 | 0.2529 | 62.6% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp4-8x1024-float16] | 0.1368 | 0.0861 | 62.9% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-a-m128-s128-float8_e4m3fn-bfloat16] | 0.0208 | 0.0131 | 63.1% | deepgemm |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp4-8x1024-bfloat16] | 0.1369 | 0.0866 | 63.2% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-mlp-up-m128-s128-float8_e4m3fn-bfloat16] | 0.0271 | 0.0173 | 63.7% | deepgemm |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[starcoder-float16] | 0.7884 | 0.5036 | 63.9% | fa3 |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-b-m128-s128-float8_e4m3fn-bfloat16] | 0.0183 | 0.0118 | 64.3% | deepgemm |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[ds-v32-kv2k-bfloat16] | 1.9074 | 1.2295 | 64.5% | flashmla |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp2-8x1024-float16] | 0.2518 | 0.1623 | 64.5% | flashinfer |
| 🔴 | **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-float16-float16] | 0.7842 | 0.5065 | 64.6% | fa3 |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-27b-8x8192-bfloat16] | 2.1358 | 1.3809 | 64.7% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp2-8x1024-bfloat16] | 0.2518 | 0.1629 | 64.7% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp8-32x8192-float16] | 1.4099 | 0.9151 | 64.9% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-2b-8x8192-bfloat16] | 0.7256 | 0.4722 | 65.1% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-27b-8x8192-float16] | 2.1126 | 1.3755 | 65.1% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp8-32x8192-bfloat16] | 1.4155 | 0.9218 | 65.1% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp4-16x8192-float16] | 1.4062 | 0.9180 | 65.3% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[indexer-context-chunk-bfloat16] | 0.3236 | 0.2117 | 65.4% | deepgemm |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp4-16x8192-bfloat16] | 1.4124 | 0.9241 | 65.4% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-2b-8x8192-float16] | 0.7193 | 0.4711 | 65.5% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp4-32x8192-float16] | 2.7668 | 1.8176 | 65.7% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp2-16x8192-bfloat16] | 2.8084 | 1.8448 | 65.7% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp4-32x8192-bfloat16] | 2.7797 | 1.8311 | 65.9% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-mla-b128-32768-float16] | 3.2797 | 2.1612 | 65.9% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp2-16x8192-float16] | 2.7758 | 1.8308 | 66.0% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-o-proj-m128-s1-float8_e4m3fn-bfloat16] | 0.0931 | 0.0614 | 66.0% | deepgemm |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-mla-b128-32768-bfloat16] | 3.2759 | 2.1632 | 66.0% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp2-8x8192-bfloat16] | 1.4071 | 0.9301 | 66.1% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp1-8x8192-bfloat16] | 2.7925 | 1.8466 | 66.1% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-35b-8x8192-float16] | 1.3971 | 0.9249 | 66.2% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp1-8x8192-float16] | 2.7668 | 1.8339 | 66.3% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-symmetric-4x2048-bfloat16] | 0.2217 | 0.1472 | 66.4% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp2-8x8192-float16] | 1.3917 | 0.9239 | 66.4% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-35b-8x8192-bfloat16] | 1.3955 | 0.9293 | 66.6% | flashinfer |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[ds-v3-t512] | 0.0119 | 0.0079 | 66.6% | vllm |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-symmetric-4x2048-float16] | 0.2206 | 0.1470 | 66.6% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-kv-a-m4096-s1-float8_e4m3fn-bfloat16] | 0.0867 | 0.0578 | 66.7% | deepgemm |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[attn-weights-32k-bfloat16] | 0.0566 | 0.0378 | 66.8% | quack |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-35b-4x2048-bfloat16] | 0.2147 | 0.1438 | 67.0% | flashinfer |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-512-float16] | 0.0275 | 0.0184 | 67.0% | quack |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-512-bfloat16] | 0.0275 | 0.0184 | 67.1% | quack |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-35b-4x2048-float16] | 0.2141 | 0.1439 | 67.2% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp1-4x2048-float16] | 0.4024 | 0.2712 | 67.4% | flashinfer |
| 🔴 | **DSADecodeWithKVCacheFwdOp** | test_dsa_decode_bench[ds-v32-kv4k-bfloat16] | 0.5127 | 0.3471 | 67.7% | flashmla |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp1-4x2048-bfloat16] | 0.4013 | 0.2719 | 67.8% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-q-b-m128-s128-float8_e4m3fn-bfloat16] | 0.0282 | 0.0191 | 67.8% | deepgemm |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-kscale-float8_e4m3fn] | 0.4712 | 0.3197 | 67.9% | deepgemm |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-32768-float16] | 1.5045 | 1.0226 | 68.0% | quack |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-27b-16x8192-bfloat16] | 4.0372 | 2.7465 | 68.0% | flashinfer |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[kimi-k2-t4096] | 0.0377 | 0.0257 | 68.1% | vllm |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-27b-16x8192-float16] | 3.9980 | 2.7339 | 68.4% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-27b-32x8192-float16] | 7.9180 | 5.4222 | 68.5% | flashinfer |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-256-float32] | 0.0264 | 0.0181 | 68.5% | torch-compile |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-27b-32x8192-bfloat16] | 7.9543 | 5.4531 | 68.6% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-2b-16x8192-bfloat16] | 1.3509 | 0.9273 | 68.6% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp1-16x8192-bfloat16] | 5.3427 | 3.6686 | 68.7% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp1-16x8192-float16] | 5.3003 | 3.6465 | 68.8% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-35b-16x8192-bfloat16] | 2.6810 | 1.8467 | 68.9% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-2b-16x8192-float16] | 1.3389 | 0.9237 | 69.0% | flashinfer |
| 🔴 | **SoftmaxFwdOp** | test_softmax_bench[quack-throughput-32768-bfloat16] | 1.5384 | 1.0627 | 69.1% | quack |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp2-32x8192-float16] | 5.2672 | 3.6416 | 69.1% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-35b-16x8192-float16] | 2.6522 | 1.8340 | 69.2% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp2-32x8192-bfloat16] | 5.3044 | 3.6698 | 69.2% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-2b-32x8192-float16] | 2.6371 | 1.8278 | 69.3% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp1-32x8192-bfloat16] | 10.5437 | 7.3126 | 69.3% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-mla-b128-16384-bfloat16] | 1.5770 | 1.0941 | 69.4% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-symmetric-16x8192-bfloat16] | 2.6641 | 1.8502 | 69.5% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-symmetric-8x8192-float16] | 1.3366 | 0.9289 | 69.5% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-35b-32x8192-float16] | 5.2322 | 3.6426 | 69.6% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-35b-32x8192-bfloat16] | 5.2632 | 3.6660 | 69.7% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp1-32x8192-float16] | 10.4341 | 7.2704 | 69.7% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-2b-32x8192-bfloat16] | 2.6434 | 1.8430 | 69.7% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-symmetric-16x8192-float16] | 2.6423 | 1.8428 | 69.7% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-mla-b128-16384-float16] | 1.5790 | 1.1018 | 69.8% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-symmetric-8x8192-bfloat16] | 1.3420 | 0.9369 | 69.8% | flashinfer |
| 🔴 | **RMSNormFwdOp** | test_rms_norm_bench[quack-throughput-131072-float16] | 3.1323 | 2.2033 | 70.3% | quack |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-o-proj-float8_e4m3fn-bfloat16] | 1.5461 | 1.0879 | 70.4% | deepgemm |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v3-serving-batch-float16] | 0.0884 | 0.0622 | 70.4% | flashinfer |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-mla-b128-8192-float16] | 0.8042 | 0.5665 | 70.5% | flashinfer |
| 🔴 | **GQAPrefillPagedWithKVCacheFwdOp** | test_gqa_prefill_paged_with_kv_cache_fwd_bench[llama-8b-float16-float8_e4m3fn] | 1.9839 | 1.3987 | 70.5% | fa3 |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-float8_e4m3fn] | 0.5246 | 0.3720 | 70.9% | deepgemm |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-o-proj-m128-s128-float8_e4m3fn-bfloat16] | 0.0664 | 0.0472 | 71.0% | flashinfer-fp8-blockscale-sm90 |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[chunk-prefill-bfloat16] | 0.5369 | 0.3841 | 71.5% | deepgemm |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-mla-b128-4096-float16] | 0.4174 | 0.2993 | 71.7% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-symmetric-32x8192-float16] | 5.0860 | 3.6518 | 71.8% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-symmetric-32x8192-bfloat16] | 5.0802 | 3.6773 | 72.4% | flashinfer |
| 🔴 | **RMSNormFwdOp** | test_rms_norm_bench[quack-throughput-131072-bfloat16] | 3.1414 | 2.2902 | 72.9% | quack |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-qkv-a-2d-float8_e4m3fn-bfloat16] | 0.1528 | 0.1121 | 73.4% | deepgemm |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-q-b-2d-float8_e4m3fn-bfloat16] | 0.3589 | 0.2645 | 73.7% | deepgemm |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_decode_bench[falcon-7b-2k-bfloat16] | 0.0371 | 0.0277 | 74.7% | fa3 |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-27b-4096-4096-float16] | 0.3265 | 0.2439 | 74.7% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-27b-4096-4096-bfloat16] | 0.3268 | 0.2444 | 74.8% | flashinfer |
| 🔴 | **RMSNormFwdOp** | test_rms_norm_bench[quack-throughput-262144-float16] | 3.1827 | 2.3880 | 75.0% | quack |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-down-2d-float8_e4m3fn-bfloat16] | 0.1447 | 0.1090 | 75.3% | deepgemm |
| 🔴 | **DeltaNetChunkBwdOp** | test_deltanet_vs_fla_bwd[deltanet-1.3b-train-bfloat16] | 0.0719 | 0.0543 | 75.5% | fla |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[ds-v2-4k-float16] | 0.1179 | 0.0903 | 76.6% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-27b-8x1024-float16] | 0.3077 | 0.2356 | 76.6% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-27b-8x1024-bfloat16] | 0.3090 | 0.2369 | 76.7% | flashinfer |
| 🔴 | **FP8LightningIndexerFwdOp** | test_fp8_lightning_indexer_bench[indexer-short-prefill-bfloat16] | 0.0736 | 0.0565 | 76.7% | deepgemm |
| 🔴 | **GLAChunkFwdOp** | test_gla_fwd_bench[train-16k-float16] | 0.6170 | 0.4752 | 77.0% | fla |
| 🔴 | **MoEPermuteAlignFwdOp** | test_permute_align_bench[qwen3-235b-t32] | 0.0070 | 0.0054 | 77.2% | vllm |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-2b-8x1024-bfloat16] | 0.1134 | 0.0881 | 77.6% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp1-8x1024-bfloat16] | 0.3972 | 0.3087 | 77.7% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-397b-tp1-8x1024-float16] | 0.3962 | 0.3085 | 77.9% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-2b-8x1024-float16] | 0.1124 | 0.0876 | 77.9% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-symmetric-8x1024-bfloat16] | 0.2134 | 0.1664 | 78.0% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-symmetric-8x1024-float16] | 0.2131 | 0.1666 | 78.2% | flashinfer |
| 🔴 | **RMSNormFwdOp** | test_rms_norm_bench[quack-throughput-262144-bfloat16] | 3.1856 | 2.4930 | 78.3% | quack |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-35b-8x1024-float16] | 0.2083 | 0.1636 | 78.5% | flashinfer |
| 🔴 | **GatedDeltaNetFwdOp** | test_gated_deltanet_fwd_bench[q35-35b-8x1024-bfloat16] | 0.2083 | 0.1638 | 78.6% | flashinfer |
| 🔴 | **DeltaNetChunkBwdOp** | test_deltanet_vs_fla_bwd[train-4k-float16] | 0.2726 | 0.2151 | 78.9% | fla |
| 🔴 | **MLADecodeWithKVCacheFwdOp** | test_mla_decode_bench[deepseek-mla-tp-batch64-float16] | 0.1296 | 0.1024 | 79.0% | flashinfer |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-o-proj-2d-float8_e4m3fn-bfloat16] | 0.8704 | 0.6908 | 79.4% | deepgemm |
| 🔴 | **GLAChunkFwdOp** | test_gla_fwd_bench[train-4k-float16] | 0.1561 | 0.1242 | 79.6% | fla |
| 🔴 | **DeltaNetChunkBwdOp** | test_deltanet_vs_fla_bwd[train-4k-bfloat16] | 0.2716 | 0.2163 | 79.6% | fla |
| 🔴 | **GemmFP8FwdOp** | test_gemm_fp8_bench[ds-v3-prefill-mlp-up-2d-float8_e4m3fn-bfloat16] | 0.2423 | 0.1931 | 79.7% | deepgemm |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 32 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 422 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 894 lines in `ops/`, 60.4% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 2569 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

### Never-built kernels

| File | Executed |
| --- | --- |
| `kernels/linear_attention/gated_deltanet/prefill_forward.py` | 3.0% |
| `kernels/linear_attention/gated_deltanet/prefill_prepare.py` | 3.3% |
| `kernels/sampling/top_k_top_p_mask.py` | 6.5% |
| `kernels/attention/gqa/dense_fp8.py` | 6.8% |
| `kernels/attention/gqa/prefill_paged_kv_append.py` | 7.7% |
| `kernels/linear_attention/delta_decode.py` | 7.8% |
| `kernels/attention/mla/decode.py` | 9.9% |
| `kernels/attention/gqa/varlen_fp8.py` | 10.0% |
| `kernels/sampling/top_k_mask.py` | 10.5% |
| `kernels/attention/gqa/dense.py` | 10.5% |
| `kernels/sampling/chain_speculative_sampling.py` | 11.4% |
| `kernels/sampling/sampling_from_probs.py` | 11.8% |
| `kernels/sampling/top_p_mask.py` | 12.4% |
| `kernels/quantization/int8_quant_per_tensor.py` | 12.8% |
| `kernels/linear_attention/gla/varlen_prefill.py` | 13.4% |
| `kernels/attention/gqa/decode_bs1.py` | 13.8% |
| `kernels/attention/gqa/decode.py` | 14.0% |
| `kernels/linear_attention/gla/dense_prefill_partitioned.py` | 16.1% |
| `kernels/quantization/int8_quant_per_block.py` | 16.1% |
| `kernels/attention/gqa/decode_fp8.py` | 16.1% |
| `kernels/quantization/int8_quant_per_channel.py` | 16.2% |
| `kernels/linear_attention/gla/varlen_prefill_partitioned.py` | 16.5% |
| `kernels/moe/indexed_expert_gemm.py` | 17.0% |
| `kernels/attention/varlen_rope.py` | 17.1% |
| `kernels/gemm/grouped/general.py` | 17.2% |
| `kernels/linear_attention/gla/dense_prefill_subchunk.py` | 17.3% |
| `kernels/sampling/min_p_mask.py` | 19.6% |
| `kernels/attention/nsa/compressed_varlen.py` | 20.0% |
| `kernels/quantization/fp8_quant_per_block.py` | 22.6% |
| `kernels/sampling/radix_select.py` | 24.1% |
| `kernels/linear_attention/gla/dense_decode.py` | 24.3% |
| `kernels/linear_attention/gated_deltanet/prefill.py` | 24.4% |

<details>
<summary>Untested pure Python, worst 15 files</summary>

| File | Uncovered | Executed |
| --- | --- | --- |
| `perf/formulas.py` | 380 | 17.4% |
| `manifest/plan.py` | 356 | 30.1% |
| `manifest/workload.py` | 194 | 58.5% |
| `ops/op_base.py` | 157 | 70.7% |
| `manifest/primitives.py` | 149 | 54.4% |
| `manifest/expr.py` | 122 | 70.7% |
| `manifest/signature.py` | 109 | 76.3% |
| `ops/_signature_codegen.py` | 88 | 89.4% |
| `trace/ui.py` | 62 | 24.4% |
| `ops/attention/gqa/prefill_paged_kv_append.py` | 54 | 36.5% |
| `manifest/kinds.py` | 53 | 79.2% |
| `backend/registry.py` | 48 | 50.0% |
| `perf/profile.py` | 42 | 22.2% |
| `ops/rope.py` | 28 | 84.1% |
| `ops/reduction/reduce.py` | 27 | 80.1% |

</details>

Per-line detail is in the `htmlcov/` directory of this run's `tileops_op_test` artifact.
