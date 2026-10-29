# ❌ TileOPs Nightly Report

> **2026-10-22 19:48** &ensp;|&ensp; `0bbb3b76` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Operators** | 207 |
| **Kernels** | 349 |
| **Specs** | 0 |
| **Workloads** | 1500 |
| **Correctness** | ✅ &ensp; (179/207 ops verified, 1333/1387 tests) |
| **Benchmarked Ops** | 105 |
| **Benchmark Failures** | ❌ 1061 &ensp;|&ensp; ⚠️ 1 skipped |
| **Regressions** (vs 14-day median) | ✅ None |
| **Baseline Alerts** (< 99%) | ⚠️ 14 |
| **vs Baseline** | ↑ 1120 &ensp;·&ensp; ↓ 14 &ensp;/&ensp; 1134 rows |
| **Rows no reference checked** | ⚠️ 192 |
| **History window** | 13 runs, 2026-10-08 to 2026-10-21 |
| **Roofline anomalies** | ✅ None |
| **Improvements** (vs 14-day best) | 🎉 23 |
| **Moved since previous run** | 🔵 23 |
| **Never-built kernels** | ⚠️ 48 files **+1** &ensp;·&ensp; `kernels/linear_attention/gdn/prefill_forward.py` at 3.4% |
| **Untested roofline math** | 457 lines in `perf/` &ensp;·&ensp; `perf/formulas.py` at 16.3% |
| **Untested op logic** | 811 lines in `ops/` **−1** &ensp;·&ensp; 60.9% of branches taken |
| | <sub>coverage compared against the 2026-10-21 run; no figure means it held</sub> |

## ❌ Benchmark Failures

| Test | Error |
|:-----|:------|
| test_argmax_bench[lm-head-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_argmax_bench[lm-head-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_argmax_bench[hidden-state-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_argmax_bench[hidden-state-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_argmax_bench[3d-non-last-axis-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_argmax_bench[llama-8b-lm-head-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_argmin_bench[lm-head-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_argmin_bench[lm-head-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_argmin_bench[hidden-state-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_argmin_bench[hidden-state-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_argmin_bench[3d-non-last-axis-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_argmin_bench[llama-8b-lm-head-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_batch_norm_fwd_bench[resnet-fc-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_batch_norm_fwd_bench[resnet-stage1-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_batch_norm_fwd_bench[resnet-stage1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_batch_norm_fwd_bench[resnet-stage2-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_batch_norm_fwd_bench[resnet-stage3-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_batch_norm_fwd_bench[resnet-stage3-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_batch_norm_fwd_bench[large-spatial-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_batch_norm_fwd_bench[resnet-stage3-eval-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_batch_norm_fwd_bench[resnet-stem-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_batch_norm_bwd_bench[resnet-fc-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_batch_norm_bwd_bench[resnet-stage1-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_batch_norm_bwd_bench[resnet-stage1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_batch_norm_bwd_bench[resnet-stage2-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_batch_norm_bwd_bench[resnet-stage3-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_batch_norm_bwd_bench[resnet-stage3-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_batch_norm_bwd_bench[large-spatial-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bmm_bench[square-128-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bmm_bench[square-128-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bmm_bench[square-1k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bmm_bench[square-1k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bmm_bench[square-512-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bmm_bench[square-512-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bmm_bench[square-256-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bmm_bench[square-256-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bmm_bench[square-4k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bmm_bench[square-2k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bmm_bench[square-2k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bmm_bench[mha-decode-qk-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bmm_bench[mha-decode-qk-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bmm_bench[mha-decode-pv-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bmm_bench[mha-decode-pv-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bmm_bench[moe-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bmm_fp8_bench[square-1k-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bmm_fp8_bench[square-2k-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bmm_fp8_bench[mha-decode-pv-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bmm_fp8_bench[mha-decode-qk-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bmm_fp8_bench[moe-prefill-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bmm_fp8_bench[square-1k-nk-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bmm_fp8_bench[square-2k-nk-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bmm_fp8_bench[mha-decode-pv-nk-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bmm_fp8_bench[mha-decode-qk-nk-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bmm_fp8_bench[moe-prefill-nk-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bmm_fp8_bench[square-1k-float8_e4m3fn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_chain_speculative_sampling_bench[llama-8b-b16-n4] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_chain_speculative_sampling_bench[llama-8b-b64-n4] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_chain_speculative_sampling_bench[ds-v3-mtp-n1] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_chain_speculative_sampling_bench[ds-v3-mtp-n3] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_chain_speculative_sampling_bench[qwen3-235b-eagle-n5] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_chain_speculative_sampling_bench[llama-8b-b17-n8] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_chain_speculative_sampling_bench[llama2-7b-b256-n1] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv1d_bench[whisper-conv1-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv1d_bench[whisper-conv1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv1d_bench[wav2vec2-layer1-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv1d_bench[wav2vec2-layer1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv1d_bench[encodec-init-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv1d_bench[encodec-init-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv1d_bench[encodec-deep-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv1d_bench[encodec-deep-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv1d_bench[whisper-conv1-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv1d_bench[whisper-conv1-bias-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv1d_bench[wav2vec2-layer1-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv1d_bench[wav2vec2-layer1-bias-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv1d_bench[encodec-init-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv1d_bench[encodec-init-bias-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv1d_bench[encodec-deep-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv1d_bench[encodec-deep-bias-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[resnet-3x3-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[resnet-3x3-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[stem-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[stage-down-3x3-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[highres-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[midres-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[stage-down-5x5-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[stride2-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[resnet-1x1-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[resnet-1x1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[bottleneck-expand-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[bottleneck-reduce-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[late-stage-1x1-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[classifier-1x1-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[deeplabv3-aspp-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[mbv2-depthwise-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[resnext-grouped-3x3-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[resnet-3x3-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[resnet-3x3-bias-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[stem-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[stage-down-3x3-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[highres-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[midres-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[stage-down-5x5-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[stride2-bias-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[resnet-1x1-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[resnet-1x1-bias-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[bottleneck-expand-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[bottleneck-reduce-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[late-stage-1x1-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv2d_bench[classifier-1x1-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv3d_bench[r3d-stem-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv3d_bench[video-down-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv3d_bench[unet-encoder-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv3d_bench[unet-aspp-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv3d_bench[resnext-grouped-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv3d_bench[r3d-stem-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv3d_bench[video-down-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_conv3d_bench[unet-encoder-bias-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_cumsum_bench[hidden-state-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_cumsum_bench[hidden-state-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_cumsum_bench[long-seq-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_cumsum_bench[llama-13b-hidden-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_cumprod_bench[hidden-state-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_cumprod_bench[hidden-state-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_cumprod_bench[long-seq-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_cumprod_bench[llama-13b-hidden-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_fwd_bench[prefill-2k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_fwd_bench[prefill-8k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_fwd_bench[prefill-16k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_fwd_bench[prefill-4k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_fwd_bench[prefill-12k-continued-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_fwd_bench[decode-continued-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_fwd_bench[decode-continued-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_fwd_bench[varlen-4x1k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_fwd_bench[varlen-ragged-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_fwd_bench[prefill-3000-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_fwd_bench[prefill-l2norm-4k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_fwd_bench[prefill-l2norm-ragged-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_fwd_bench[decode-fresh-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_fwd_bench[decode-l2norm-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_fwd_bench[decode-narrow-b17-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_fwd_bench[deltanet-1.3b-continue-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_fwd_bench[deltanet-1.3b-decode-b32-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_fwd_bench[deltanet-1.3b-cont-b4-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_vs_fla_fwd[train-2k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_vs_fla_fwd[train-2k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_vs_fla_fwd[train-4k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_vs_fla_fwd[train-4k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_vs_fla_fwd[train-8k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_vs_fla_fwd[train-8k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_vs_fla_fwd[train-16k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_vs_fla_fwd[train-16k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_vs_fla_fwd[deltanet-1.3b-train-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_vs_fla_bwd[train-2k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_vs_fla_bwd[train-2k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_vs_fla_bwd[train-4k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_vs_fla_bwd[train-4k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_vs_fla_bwd[train-8k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_vs_fla_bwd[train-8k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_vs_fla_bwd[train-16k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_vs_fla_bwd[train-16k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_vs_fla_bwd[deltanet-1.3b-train-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_decode_bench[serving-b1-h8-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_decode_bench[serving-b1-h16-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_decode_bench[serving-b1-h32-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_decode_bench[serving-b1-h48-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_decode_bench[serving-b1-h64-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_decode_bench[serving-b8-h32-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_decode_bench[serving-b8-h48-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_deltanet_decode_bench[serving-b8-h64-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_dsa_decode_bench[ds-v32-kv2k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_dsa_decode_bench[ds-v32-kv2k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_dsa_decode_bench[ds-v32-kv4k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_dsa_decode_bench[ds-v32-kv4k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_dsa_decode_bench[mla-d576-h128-kv8k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_dsa_decode_bench[mla-d576-h128-kv32k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_dsa_decode_bench[mla-d576-h128-kv64k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_dsa_decode_bench[mla-d576-h128-kv96k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_dsa_decode_bench[mla-d576-h128-kv128k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_dsa_decode_bench[mla-d512-h64-kv8k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_dsa_decode_bench[mla-d512-h64-kv32k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_dsa_decode_bench[mla-d512-h64-kv48k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_dsa_decode_bench[mla-d512-h64-kv64k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_dsa_decode_bench[mla-d512-h128-kv8k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_dsa_decode_bench[mla-d512-h128-kv32k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_dsa_decode_bench[mla-d512-h128-kv48k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_dsa_decode_bench[mla-d512-h128-kv64k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_dsa_paged_bench[ds-v32-32k] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_dsa_paged_bench[ds-v32-mtp-128k] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_dsa_paged_bench[ds-v32-tp2-1k] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_prelu_bench[cnn-feat-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_prelu_bench[cnn-feat-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_prelu_bench[cnn-feat-deep-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_prelu_bench[cnn-feat-deep-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_masked_fill_bench[16M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_masked_fill_bench[16M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_masked_fill_bench[16M-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_masked_fill_bench[256M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_masked_fill_bench[256M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_masked_fill_scalar_bench[16M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_masked_fill_scalar_bench[16M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_masked_fill_scalar_bench[16M-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_masked_fill_scalar_bench[256M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_masked_fill_scalar_bench[256M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_add_bench[hidden-state-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_add_bench[hidden-state-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_add_bench[hidden-state-prefill-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_add_bench[cnn-feat-broadcast-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_add_bench[cnn-feat-broadcast-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_add_bench[cnn-feat-broadcast-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_add_bench[llama-7b-ffn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_add_bench[llama-7b-ffn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_add_bench[llama-7b-ffn-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_add_bench[linear-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_add_bench[linear-bias-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_add_bench[linear-bias-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sub_bench[hidden-state-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sub_bench[hidden-state-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sub_bench[hidden-state-prefill-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sub_bench[cnn-feat-broadcast-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sub_bench[cnn-feat-broadcast-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sub_bench[cnn-feat-broadcast-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sub_bench[llama-7b-ffn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sub_bench[llama-7b-ffn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sub_bench[llama-7b-ffn-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sub_bench[linear-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sub_bench[linear-bias-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sub_bench[linear-bias-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sub_bench[llama-7b-hidden-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sub_bench[phi-2-ffn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sub_bench[phi-2-ffn-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sub_bench[llama-7b-ffn-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mul_bench[hidden-state-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mul_bench[hidden-state-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mul_bench[hidden-state-prefill-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mul_bench[cnn-feat-broadcast-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mul_bench[cnn-feat-broadcast-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mul_bench[cnn-feat-broadcast-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mul_bench[llama-7b-ffn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mul_bench[llama-7b-ffn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mul_bench[llama-7b-ffn-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mul_bench[linear-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mul_bench[linear-bias-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mul_bench[linear-bias-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mul_bench[llama-7b-hidden-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mul_bench[phi-2-ffn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mul_bench[phi-2-ffn-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mul_bench[llama-7b-ffn-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_div_bench[hidden-state-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_div_bench[hidden-state-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_div_bench[hidden-state-prefill-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_div_bench[cnn-feat-broadcast-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_div_bench[cnn-feat-broadcast-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_div_bench[cnn-feat-broadcast-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_div_bench[llama-7b-ffn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_div_bench[llama-7b-ffn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_div_bench[llama-7b-ffn-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_div_bench[linear-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_div_bench[linear-bias-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_div_bench[linear-bias-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_div_bench[llama-7b-hidden-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_div_bench[phi-2-ffn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_div_bench[phi-2-ffn-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_div_bench[llama-7b-ffn-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_remainder_bench[hidden-state-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_remainder_bench[hidden-state-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_remainder_bench[hidden-state-prefill-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_remainder_bench[cnn-feat-broadcast-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_remainder_bench[cnn-feat-broadcast-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_remainder_bench[cnn-feat-broadcast-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_remainder_bench[llama-7b-ffn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_remainder_bench[llama-7b-ffn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_remainder_bench[llama-7b-ffn-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_remainder_bench[linear-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_remainder_bench[linear-bias-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_remainder_bench[linear-bias-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_remainder_bench[llama-7b-hidden-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_remainder_bench[phi-2-ffn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_pow_bench[hidden-state-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_pow_bench[hidden-state-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_pow_bench[hidden-state-prefill-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_pow_bench[cnn-feat-broadcast-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_pow_bench[cnn-feat-broadcast-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_pow_bench[cnn-feat-broadcast-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_pow_bench[llama-7b-ffn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_pow_bench[llama-7b-ffn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_pow_bench[llama-7b-ffn-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_pow_bench[linear-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_pow_bench[linear-bias-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_pow_bench[linear-bias-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_pow_bench[llama-7b-hidden-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_pow_bench[phi-2-ffn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_floor_divide_bench[hidden-state-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_floor_divide_bench[hidden-state-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_floor_divide_bench[hidden-state-prefill-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_floor_divide_bench[cnn-feat-broadcast-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_floor_divide_bench[cnn-feat-broadcast-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_floor_divide_bench[cnn-feat-broadcast-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_floor_divide_bench[llama-7b-ffn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_floor_divide_bench[llama-7b-ffn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_floor_divide_bench[llama-7b-ffn-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_floor_divide_bench[linear-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_floor_divide_bench[linear-bias-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_floor_divide_bench[linear-bias-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_floor_divide_bench[llama-7b-hidden-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_floor_divide_bench[phi-2-ffn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lerp_bench[hidden-state-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lerp_bench[hidden-state-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lerp_bench[hidden-state-prefill-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lerp_bench[cnn-feat-broadcast-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lerp_bench[cnn-feat-broadcast-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lerp_bench[cnn-feat-broadcast-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lerp_bench[llama-7b-ffn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lerp_bench[llama-7b-ffn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lerp_bench[llama-7b-ffn-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lerp_bench[linear-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lerp_bench[linear-bias-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lerp_bench[linear-bias-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lerp_bench[llama-7b-hidden-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lerp_bench[phi-2-ffn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_maximum_bench[hidden-state-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_maximum_bench[hidden-state-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_maximum_bench[hidden-state-prefill-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_maximum_bench[cnn-feat-broadcast-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_maximum_bench[cnn-feat-broadcast-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_maximum_bench[cnn-feat-broadcast-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_maximum_bench[llama-7b-ffn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_maximum_bench[llama-7b-ffn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_maximum_bench[llama-7b-ffn-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_maximum_bench[linear-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_maximum_bench[linear-bias-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_maximum_bench[linear-bias-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_maximum_bench[llama-7b-hidden-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_maximum_bench[phi-2-ffn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_minimum_bench[hidden-state-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_minimum_bench[hidden-state-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_minimum_bench[hidden-state-prefill-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_minimum_bench[cnn-feat-broadcast-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_minimum_bench[cnn-feat-broadcast-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_minimum_bench[cnn-feat-broadcast-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_minimum_bench[llama-7b-ffn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_minimum_bench[llama-7b-ffn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_minimum_bench[llama-7b-ffn-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_minimum_bench[linear-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_minimum_bench[linear-bias-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_minimum_bench[linear-bias-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_minimum_bench[llama-7b-hidden-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_minimum_bench[phi-2-ffn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_eq_bench[hidden-state-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_eq_bench[hidden-state-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_eq_bench[hidden-state-prefill-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_eq_bench[cnn-feat-broadcast-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_eq_bench[cnn-feat-broadcast-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_eq_bench[cnn-feat-broadcast-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_eq_bench[llama-7b-ffn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_eq_bench[llama-7b-ffn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_eq_bench[llama-7b-ffn-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_eq_bench[linear-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_eq_bench[linear-bias-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_eq_bench[linear-bias-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_eq_bench[llama-7b-hidden-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_eq_bench[phi-2-ffn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ne_bench[hidden-state-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ne_bench[hidden-state-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ne_bench[hidden-state-prefill-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ne_bench[cnn-feat-broadcast-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ne_bench[cnn-feat-broadcast-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ne_bench[cnn-feat-broadcast-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ne_bench[llama-7b-ffn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ne_bench[llama-7b-ffn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ne_bench[llama-7b-ffn-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ne_bench[linear-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ne_bench[linear-bias-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ne_bench[linear-bias-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ne_bench[llama-7b-hidden-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gt_bench[hidden-state-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gt_bench[hidden-state-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gt_bench[hidden-state-prefill-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gt_bench[cnn-feat-broadcast-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gt_bench[cnn-feat-broadcast-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gt_bench[cnn-feat-broadcast-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gt_bench[llama-7b-ffn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gt_bench[llama-7b-ffn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gt_bench[llama-7b-ffn-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gt_bench[linear-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gt_bench[linear-bias-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gt_bench[linear-bias-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gt_bench[llama-7b-hidden-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lt_bench[hidden-state-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lt_bench[hidden-state-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lt_bench[hidden-state-prefill-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lt_bench[cnn-feat-broadcast-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lt_bench[cnn-feat-broadcast-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lt_bench[cnn-feat-broadcast-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lt_bench[llama-7b-ffn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lt_bench[llama-7b-ffn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lt_bench[llama-7b-ffn-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lt_bench[linear-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lt_bench[linear-bias-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lt_bench[linear-bias-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lt_bench[llama-7b-hidden-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ge_bench[hidden-state-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ge_bench[hidden-state-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ge_bench[hidden-state-prefill-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ge_bench[cnn-feat-broadcast-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ge_bench[cnn-feat-broadcast-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ge_bench[cnn-feat-broadcast-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ge_bench[llama-7b-ffn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ge_bench[llama-7b-ffn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ge_bench[llama-7b-ffn-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ge_bench[linear-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ge_bench[linear-bias-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ge_bench[linear-bias-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ge_bench[llama-7b-hidden-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_le_bench[hidden-state-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_le_bench[hidden-state-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_le_bench[hidden-state-prefill-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_le_bench[cnn-feat-broadcast-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_le_bench[cnn-feat-broadcast-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_le_bench[cnn-feat-broadcast-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_le_bench[llama-7b-ffn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_le_bench[llama-7b-ffn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_le_bench[llama-7b-ffn-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_le_bench[linear-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_le_bench[linear-bias-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_le_bench[linear-bias-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_le_bench[llama-7b-hidden-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_and_bench[hidden-state-prefill-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_and_bench[hidden-state-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_and_bench[hidden-state-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_and_bench[hidden-state-prefill-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_and_bench[cnn-feat-broadcast-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_and_bench[cnn-feat-broadcast-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_and_bench[cnn-feat-broadcast-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_and_bench[cnn-feat-broadcast-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_and_bench[llama-7b-ffn-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_and_bench[llama-7b-ffn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_and_bench[llama-7b-ffn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_and_bench[llama-7b-ffn-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_and_bench[linear-bias-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_and_bench[linear-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_and_bench[linear-bias-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_and_bench[linear-bias-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_and_bench[llama-7b-hidden-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_and_bench[phi-2-ffn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_or_bench[hidden-state-prefill-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_or_bench[hidden-state-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_or_bench[hidden-state-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_or_bench[hidden-state-prefill-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_or_bench[cnn-feat-broadcast-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_or_bench[cnn-feat-broadcast-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_or_bench[cnn-feat-broadcast-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_or_bench[cnn-feat-broadcast-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_or_bench[llama-7b-ffn-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_or_bench[llama-7b-ffn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_or_bench[llama-7b-ffn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_or_bench[llama-7b-ffn-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_or_bench[linear-bias-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_or_bench[linear-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_or_bench[linear-bias-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_or_bench[linear-bias-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_or_bench[llama-7b-hidden-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_or_bench[phi-2-ffn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_and_bench[hidden-state-prefill-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_and_bench[hidden-state-prefill-int32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_and_bench[hidden-state-prefill-int64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_and_bench[cnn-feat-broadcast-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_and_bench[cnn-feat-broadcast-int32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_and_bench[cnn-feat-broadcast-int64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_and_bench[llama-7b-ffn-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_and_bench[llama-7b-ffn-int32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_and_bench[llama-7b-ffn-int64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_and_bench[linear-bias-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_and_bench[linear-bias-int32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_and_bench[linear-bias-int64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_and_bench[llama-7b-hidden-int32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_and_bench[phi-2-ffn-int32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_or_bench[hidden-state-prefill-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_or_bench[hidden-state-prefill-int32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_or_bench[hidden-state-prefill-int64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_or_bench[cnn-feat-broadcast-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_or_bench[cnn-feat-broadcast-int32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_or_bench[cnn-feat-broadcast-int64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_or_bench[llama-7b-ffn-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_or_bench[llama-7b-ffn-int32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_or_bench[llama-7b-ffn-int64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_or_bench[linear-bias-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_or_bench[linear-bias-int32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_or_bench[linear-bias-int64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_or_bench[llama-7b-hidden-int32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_xor_bench[hidden-state-prefill-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_xor_bench[hidden-state-prefill-int32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_xor_bench[hidden-state-prefill-int64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_xor_bench[cnn-feat-broadcast-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_xor_bench[cnn-feat-broadcast-int32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_xor_bench[cnn-feat-broadcast-int64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_xor_bench[llama-7b-ffn-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_xor_bench[llama-7b-ffn-int32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_xor_bench[llama-7b-ffn-int64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_xor_bench[linear-bias-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_xor_bench[linear-bias-int32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_xor_bench[linear-bias-int64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_xor_bench[llama-7b-hidden-int32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_alibi_bench[mpt-7b-2k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_alibi_bench[mpt-7b-2k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_alibi_bench[mpt-7b-4k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_alibi_bench[mpt-7b-4k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sinusoidal_bench[transformer-2k-4k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sinusoidal_bench[transformer-2k-4k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sinusoidal_bench[transformer-4k-4k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sinusoidal_bench[transformer-4k-4k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_where_bench[16M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_where_bench[16M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_where_bench[16M-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_where_bench[256M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_where_bench[256M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lerp_tensor_bench[16M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lerp_tensor_bench[16M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lerp_tensor_bench[16M-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lerp_tensor_bench[256M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lerp_tensor_bench[256M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_relu_bench[hidden-state-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_relu_bench[hidden-state-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_relu_bench[hidden-state-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gelu_bench[llama-8b-ffn-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gelu_bench[llama-8b-ffn-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gelu_bench[llama-8b-ffn-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_silu_bench[llama-8b-ffn-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_silu_bench[llama-8b-ffn-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_silu_bench[llama-8b-ffn-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_hardswish_bench[mbv3-stage2-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_hardswish_bench[mbv3-stage2-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_hardswish_bench[mbv3-stage3-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_hardswish_bench[mbv3-stage3-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_hardsigmoid_bench[mbv3-se-gate-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_hardsigmoid_bench[mbv3-se-gate-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_hardsigmoid_bench[mbv3-se-gate-deep-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_hardsigmoid_bench[mbv3-se-gate-deep-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mish_bench[yolo-p3-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mish_bench[yolo-p3-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mish_bench[yolo-p4-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mish_bench[yolo-p4-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_selu_bench[snn-fc-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_selu_bench[snn-fc-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_selu_bench[snn-fc-wide-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_selu_bench[snn-fc-wide-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_leaky_relu_bench[gan-feat-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_leaky_relu_bench[gan-feat-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_leaky_relu_bench[gan-feat-deep-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_leaky_relu_bench[gan-feat-deep-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_elu_bench[mlp-hidden-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_elu_bench[mlp-hidden-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_elu_bench[mlp-hidden-wide-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_elu_bench[mlp-hidden-wide-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_hardtanh_bench[bounded-hidden-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_hardtanh_bench[bounded-hidden-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_hardtanh_bench[bounded-conv-feat-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_hardtanh_bench[bounded-conv-feat-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softplus_bench[mlp-hidden-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softplus_bench[mlp-hidden-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softplus_bench[mlp-hidden-wide-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softplus_bench[mlp-hidden-wide-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_clamp_bench[16M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_clamp_bench[16M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_clamp_bench[16M-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_clamp_bench[256M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_clamp_bench[256M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_clamp_bench[16M-min-only-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_clamp_bench[16M-min-only-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_clamp_bench[16M-min-only-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_clamp_bench[256M-min-only-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_clamp_bench[256M-min-only-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_clamp_bench[16M-max-only-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_clamp_bench[16M-max-only-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_clamp_bench[16M-max-only-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_clamp_bench[256M-max-only-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_clamp_bench[256M-max-only-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_clamp_scalar_bench[16M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_clamp_scalar_bench[16M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_clamp_scalar_bench[16M-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_clamp_scalar_bench[256M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_clamp_scalar_bench[256M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_nan_to_num_bench[16M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_nan_to_num_bench[16M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_nan_to_num_bench[16M-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_nan_to_num_bench[256M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_nan_to_num_bench[256M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_exp_bench[16M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_exp_bench[16M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_exp_bench[16M-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_exp_bench[256M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_exp_bench[256M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_log_bench[16M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_log_bench[16M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_log_bench[16M-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_log_bench[256M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_log_bench[256M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sqrt_bench[16M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sqrt_bench[16M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sqrt_bench[16M-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sqrt_bench[256M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sqrt_bench[256M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rsqrt_bench[16M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rsqrt_bench[16M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rsqrt_bench[16M-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rsqrt_bench[256M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rsqrt_bench[256M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_abs_bench[16M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_abs_bench[16M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_abs_bench[16M-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_abs_bench[256M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_abs_bench[256M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_neg_bench[16M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_neg_bench[16M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_neg_bench[16M-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_neg_bench[256M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_neg_bench[256M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_reciprocal_bench[16M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_reciprocal_bench[16M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_reciprocal_bench[16M-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_reciprocal_bench[256M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_reciprocal_bench[256M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sign_bench[16M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sign_bench[16M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sign_bench[16M-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sign_bench[256M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sign_bench[256M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sin_bench[16M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sin_bench[16M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sin_bench[16M-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sin_bench[256M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sin_bench[256M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_cos_bench[16M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_cos_bench[16M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_cos_bench[16M-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_cos_bench[256M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_cos_bench[256M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_floor_bench[16M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_floor_bench[16M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_floor_bench[16M-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_floor_bench[256M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_floor_bench[256M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ceil_bench[16M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ceil_bench[16M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ceil_bench[16M-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ceil_bench[256M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ceil_bench[256M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_round_bench[16M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_round_bench[16M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_round_bench[16M-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_round_bench[256M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_round_bench[256M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_trunc_bench[16M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_trunc_bench[16M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_trunc_bench[16M-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_trunc_bench[256M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_trunc_bench[256M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_erf_bench[16M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_erf_bench[16M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_erf_bench[16M-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_erf_bench[256M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_erf_bench[256M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_log1p_bench[16M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_log1p_bench[16M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_log1p_bench[16M-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_log1p_bench[256M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_log1p_bench[256M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_expm1_bench[16M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_expm1_bench[16M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_expm1_bench[16M-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_expm1_bench[256M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_expm1_bench[256M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sigmoid_bench[16M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sigmoid_bench[16M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sigmoid_bench[16M-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sigmoid_bench[256M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sigmoid_bench[256M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_tanh_bench[16M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_tanh_bench[16M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_tanh_bench[16M-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_tanh_bench[256M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_tanh_bench[256M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_not_bench[16M-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_not_bench[16M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_not_bench[16M-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logical_not_bench[256M-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_not_bench[16M-int32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_not_bench[16M-int64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_bitwise_not_bench[256M-int32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_isnan_bench[16M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_isnan_bench[16M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_isnan_bench[16M-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_isnan_bench[256M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_isnan_bench[256M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_isinf_bench[16M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_isinf_bench[16M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_isinf_bench[16M-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_isinf_bench[256M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_isinf_bench[256M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_isfinite_bench[16M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_isfinite_bench[16M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_isfinite_bench[16M-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_isfinite_bench[256M-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_isfinite_bench[256M-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_dropout_bench[hidden-4k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_dropout_bench[hidden-4k-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_dropout_bench[hidden-10k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_engram_gate_conv_fwd_bench[train-s32-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_engram_gate_conv_fwd_bench[train-s64-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_engram_gate_conv_fwd_bench[train-s128-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_engram_gate_conv_fwd_bench[train-s96-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_engram_gate_conv_bwd_bench[train-s32-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_engram_gate_conv_bwd_bench[train-s64-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_engram_gate_conv_bwd_bench[train-s128-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_engram_gate_conv_bwd_bench[train-s96-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_engram_decode_bench[serving-b1-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_engram_decode_bench[serving-b4-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_engram_decode_bench[serving-b8-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fft_bench[latency-4k-complex64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fft_bench[throughput-4k-complex64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fft_bench[throughput-4k-complex128] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fft_bench[longconv-16k-complex64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fft_bench[longconv-64k-complex64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fft_bench[spectrogram-1k-complex64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fft_bench[fnet-512-complex64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fft_bench[shortconv-64-complex64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fft_bench[scientific-1m-complex128] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fft_bench[spectrogram-1k-b300-complex64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fp8_lightning_indexer_bench[chunk-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fp8_lightning_indexer_bench[chunk-prefill-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fp8_lightning_indexer_bench[chunk-prefill-kscale-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fp8_lightning_indexer_bench[short-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fp8_lightning_indexer_bench[context-chunk-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fp8_lightning_indexer_bench[index-q2048-ctx4096-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fp8_lightning_indexer_bench[index-q2048-ctx8192-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fp8_lightning_indexer_bench[index-q2048-ctx16384-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fp8_lightning_indexer_bench[index-q2048-ctx32768-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fp8_lightning_indexer_bench[index-q2048-ctx65536-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fp8_lightning_indexer_bench[index-q2048-ctx131072-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fp8_lightning_indexer_bench[index-q4096-ctx4096-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fp8_lightning_indexer_bench[index-q4096-ctx8192-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fp8_lightning_indexer_bench[index-q4096-ctx16384-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fp8_lightning_indexer_bench[index-q4096-ctx32768-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fp8_lightning_indexer_bench[index-q4096-ctx65536-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fp8_lightning_indexer_bench[index-q4096-ctx131072-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fp8_lightning_indexer_bench[ds-v32-decode-b1-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fp8_quant_bench[kv-index-8k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fp8_quant_bench[kv-index-8k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fp8_quant_bench[kv-index-4k-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fp8_quant_bench[kv-index-context-chunk-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fp8_quant_bench[kv-index-context-chunk-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fp8_quant_per_block_bench[ds-v3-mlp-down-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fp8_quant_per_block_bench[ds-v3-expert-gate-up-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fp8_quant_per_block_bench[ds-v3-expert-gate-up-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fp8_quant_per_block_bench[qwen3-235b-qkv-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fp8_quant_per_block_bench[qwen3-235b-qkv-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fp8_quant_per_block_bench[gpt-oss-expert-down-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fp8_quant_per_block_bench[ragged-k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_silu_and_mul_bench[llama-8b-ffn-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_silu_and_mul_bench[llama-8b-ffn-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_silu_and_mul_bench[llama-8b-ffn-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_silu_and_mul_bench[qwen3-8b-swiglu-b32-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gelu_and_mul_bench[llama-8b-ffn-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gelu_and_mul_bench[llama-8b-ffn-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gelu_and_mul_bench[llama-8b-ffn-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gelu_tanh_and_mul_bench[llama-8b-ffn-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gelu_tanh_and_mul_bench[llama-8b-ffn-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gelu_tanh_and_mul_bench[llama-8b-ffn-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_fwd_bench[qwen3-235b-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_fwd_bench[qwen3-235b-decode-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_fwd_bench[qwen3-235b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_fwd_bench[ds-v3-grouped-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_fwd_bench[ds-v3-grouped-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_fwd_bench[kimi-k2-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_fwd_bench[kimi-k2-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_fwd_bench[qwen3-30b-decode-b1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_fwd_bench[qwen3-30b-decode-b32-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_fwd_bench[gpt-oss-120b-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_fwd_bench[gpt-oss-120b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_fwd_bench[gpt-oss-20b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_shared_expert_bench[kimi-k2-t1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_shared_expert_bench[kimi-k2-t32-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_shared_expert_bench[kimi-k2-t64-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_shared_expert_bench[kimi-k2-t128-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_shared_expert_bench[kimi-k2-t512-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_shared_expert_bench[kimi-k2-t2048-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_shared_expert_bench[kimi-k2-t4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_shared_expert_bench[ds-v3-grouped-t1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_shared_expert_bench[ds-v3-grouped-t32-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_shared_expert_bench[ds-v3-grouped-t32-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_shared_expert_bench[ds-v3-grouped-t64-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_shared_expert_bench[ds-v3-grouped-t128-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_shared_expert_bench[ds-v3-grouped-t512-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_shared_expert_bench[ds-v3-grouped-t2048-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_shared_expert_bench[ds-v3-grouped-t4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_shared_expert_bench[glm45-t1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_shared_expert_bench[glm45-t32-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_shared_expert_bench[glm45-t64-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_shared_expert_bench[glm45-t128-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_shared_expert_bench[glm45-t512-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_shared_expert_bench[glm45-t2048-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_shared_expert_bench[glm45-t4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_moe_shared_expert_bench[qwen3-235b-t512-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_shared_expert_mlp_bench[kimi-k2-t1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_shared_expert_mlp_bench[kimi-k2-t512-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_shared_expert_mlp_bench[ds-v3-t32-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_shared_expert_mlp_bench[ds-v3-t32-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_shared_expert_mlp_bench[ds-v3-t4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_shared_expert_mlp_bench[glm45-t32-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_experts_bench[qwen3-235b-decode-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_experts_bench[qwen3-235b-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_experts_bench[qwen3-235b-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_experts_bench[qwen3-235b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_experts_bench[ds-v3-decode-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_experts_bench[ds-v3-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_experts_bench[ds-v3-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_experts_bench[ds-v3-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_experts_bench[gpt-oss-120b-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_experts_bench[gpt-oss-120b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_experts_bench[gpt-oss-20b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_indexed_expert_mlp_bench[ds-v3-t1-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_indexed_expert_mlp_bench[ds-v3-t1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_indexed_expert_mlp_bench[ds-v3-t32-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_indexed_expert_mlp_bench[ds-v3-t32-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_indexed_expert_mlp_bench[ds-v3-t64-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_indexed_expert_mlp_bench[ds-v3-t64-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_indexed_expert_mlp_bench[qwen3-235b-t32-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_indexed_expert_mlp_bench[qwen3-235b-t32-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_qk_norm_rope_bench[qwen3-8b-t64-bfloat16-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_qk_norm_rope_bench[qwen3-8b-t64-float16-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_qk_norm_rope_bench[qwen3-8b-t8192-bfloat16-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_qk_norm_rope_bench[qwen3-235b-t4096-bfloat16-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_qk_norm_rope_bench[glm-4.5-partial-rope-bfloat16-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_qk_norm_rope_bench[interleaved-ragged-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_qk_norm_rope_bench[interleaved-ragged-bfloat16-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_topk_bench[kimi-k2-t32-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_topk_bench[kimi-k2-t512-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_topk_bench[kimi-k2-t4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_topk_bench[kimi-k2-t512-bias-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_topk_bench[kimi-k2-t512-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_topk_bench[kimi-k2-t512-bias-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_topk_bench[qwen3-235b-t32-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_topk_bench[qwen3-235b-t512-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_topk_bench[qwen3-235b-t512-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_topk_bench[qwen3-235b-t512-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_topk_bench[qwen3-235b-t4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_topk_bench[ds-v3-grouped-t1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_topk_bench[ds-v3-grouped-t32-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_topk_bench[ds-v3-grouped-t64-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_topk_bench[ds-v3-grouped-t64-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_topk_bench[ds-v3-grouped-t64-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_topk_bench[ds-v3-grouped-t4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[prefill-4k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[prefill-4k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[prefill-12k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[prefill-12k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[prefill-32k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[prefill-32k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[decode-b1-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[decode-b1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[decode-b8-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[decode-b8-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[prefill-continued-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[prefill-narrow-state-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[varlen-4x1k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[varlen-ragged-grouped-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[prefill-3000-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[prefill-raw-4k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[prefill-raw-ragged-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[decode-fresh-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[decode-gate-fused-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[decode-beta-l2norm-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[decode-vfirst-b17-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[prefill-v-first-4k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[prefill-v-first-narrow-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[varlen-v-first-ragged-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp8-65536-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp8-65536-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp8-32768-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp8-32768-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp8-16384-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp8-16384-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp8-8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp8-8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp8-4096-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp8-4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp8-2048-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp8-2048-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp8-6144-2048-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp8-6144-2048-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp8-4096-4096-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp8-4096-4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp8-2048-6144-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp8-2048-6144-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp8-1024-7168-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp8-1024-7168-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp8-4x2048-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp8-4x2048-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp8-8x1024-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp8-8x1024-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp8-8x8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp8-8x8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp8-16x8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp8-16x8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp8-32x8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp8-32x8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp4-65536-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp4-65536-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp4-32768-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp4-32768-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp4-16384-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp4-16384-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp4-8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp4-8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp4-4096-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp4-4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp4-2048-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp4-2048-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp4-6144-2048-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp4-6144-2048-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp4-4096-4096-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp4-4096-4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp4-2048-6144-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp4-2048-6144-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp4-1024-7168-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp4-1024-7168-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp4-4x2048-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp4-4x2048-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp4-8x1024-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp4-8x1024-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp4-8x8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp4-8x8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp4-16x8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp4-16x8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp4-32x8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp4-32x8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp2-65536-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp2-65536-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp2-32768-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp2-32768-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp2-16384-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp2-16384-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp2-8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp2-8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp2-4096-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp2-4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp2-2048-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp2-2048-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp2-6144-2048-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp2-6144-2048-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp2-4096-4096-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp2-4096-4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp2-2048-6144-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp2-2048-6144-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp2-1024-7168-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp2-1024-7168-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp2-4x2048-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp2-4x2048-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp2-8x1024-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp2-8x1024-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp2-8x8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp2-8x8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp2-16x8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp2-16x8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp2-32x8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp2-32x8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp1-65536-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp1-65536-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp1-32768-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp1-32768-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp1-16384-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp1-16384-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp1-8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp1-8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp1-4096-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp1-4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp1-2048-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp1-2048-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp1-6144-2048-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp1-6144-2048-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp1-4096-4096-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp1-4096-4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp1-2048-6144-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp1-2048-6144-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp1-1024-7168-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp1-1024-7168-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp1-4x2048-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp1-4x2048-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp1-8x1024-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp1-8x1024-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp1-8x8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp1-8x8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp1-16x8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp1-16x8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp1-32x8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-397b-tp1-32x8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-35b-65536-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-35b-65536-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-35b-32768-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-35b-32768-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-35b-16384-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-35b-16384-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-35b-8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-35b-8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-35b-4096-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-35b-4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-35b-2048-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-35b-2048-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-35b-6144-2048-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-35b-6144-2048-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-35b-4096-4096-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-35b-4096-4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-35b-2048-6144-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-35b-2048-6144-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-35b-1024-7168-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-35b-1024-7168-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-35b-4x2048-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-35b-4x2048-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-35b-8x1024-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-35b-8x1024-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-35b-8x8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-35b-8x8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-35b-16x8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-35b-16x8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-35b-32x8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-35b-32x8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-27b-65536-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-27b-65536-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-27b-32768-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-27b-32768-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-27b-16384-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-27b-16384-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-27b-8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-27b-8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-27b-4096-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-27b-4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-27b-2048-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-27b-2048-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-27b-6144-2048-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-27b-6144-2048-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-27b-4096-4096-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-27b-4096-4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-27b-2048-6144-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-27b-2048-6144-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-27b-1024-7168-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-27b-1024-7168-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-27b-4x2048-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-27b-4x2048-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-27b-8x1024-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-27b-8x1024-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-27b-8x8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-27b-8x8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-27b-16x8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-27b-16x8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-27b-32x8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-27b-32x8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-2b-65536-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-2b-65536-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-2b-16384-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-2b-16384-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-2b-8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-2b-8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |

## 🎉 Performance Improvements (vs 14-day best)

| Op | Config | Prev Best (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **GQADenseFwdOp** | test_gqa_dense_fwd_bench[falcon-7b-2k-bfloat16] | 0.0370 | 0.0156 | -57.8% | 77.78 |
| **GQADenseFwdOp** | test_gqa_dense_fwd_bench[gpt-oss-sinks-decode-8k-bfloat16] | 0.4336 | 0.2537 | -41.5% | 34.52 |
| **GQADenseFwdOp** | test_gqa_dense_fwd_bench[gemma-2b-8k-bs1-bfloat16] | 0.0169 | 0.0113 | -33.3% | 5.97 |
| **GQADenseFwdOp** | test_gqa_dense_fwd_bench[gemma-2b-8k-bs1-float16] | 0.0169 | 0.0114 | -32.7% | 5.92 |
| **GQADenseFwdOp** | test_gqa_dense_fwd_bench[gpt-oss-sinks-window-128-bfloat16] | 0.1982 | 0.1355 | -31.6% | 128.50 |
| **GQADenseFwdOp** | test_gqa_dense_fwd_bench[gpt-oss-sinks-window-128-float16] | 0.1982 | 0.1362 | -31.3% | 127.86 |
| **AminFwdOp** | test_amin_bench[3d-multidim-float16] | 0.0047 | 0.0036 | -23.6% | 0.58 |
| **SumFwdOp** | test_sum_bench[3d-multidim-float16] | 0.0047 | 0.0036 | -23.0% | 0.57 |
| **AmaxFwdOp** | test_amax_bench[3d-multidim-float16] | 0.0047 | 0.0036 | -23.0% | 0.57 |
| **MeanFwdOp** | test_mean_bench[3d-multidim-float16] | 0.0048 | 0.0037 | -22.8% | 0.57 |
| **VectorNormFwdOp** | test_vector_norm_bench[l1-3d-multidim-float16] | 0.0047 | 0.0036 | -21.9% | 1.15 |
| **VectorNormFwdOp** | test_vector_norm_bench[inf-3d-multidim-float16] | 0.0047 | 0.0036 | -21.9% | 1.15 |
| **VectorNormFwdOp** | test_vector_norm_bench[l2-3d-multidim-float16] | 0.0048 | 0.0037 | -21.5% | 1.12 |
| **GQAVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-rope-partial-float16] | 0.0511 | 0.0405 | -20.7% | 205.06 |
| **GQAVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-rope-partial-bfloat16] | 0.0514 | 0.0409 | -20.4% | 202.97 |
| **GQADenseFwdOp** | test_gqa_dense_fwd_bench[gpt-oss-sinks-prefill-2k-bfloat16] | 0.1324 | 0.1067 | -19.4% | 328.59 |
| **GQAVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-70b-fp8-q-lt-kv-float8_e4m3fn-bfloat16] | 0.1008 | 0.0813 | -19.3% | 533.67 |
| **GQADenseFwdOp** | test_gqa_dense_fwd_bench[llama-8b-softcap-float16] | 0.1561 | 0.1318 | -15.6% | 16.55 |
| **GQAVarlenFwdOp** | test_gqa_varlen_fwd_bench[qwen3-fp8-ragged-float8_e4m3fn-bfloat16] | 0.1091 | 0.0942 | -13.7% | 484.46 |
| **GQADenseFwdOp** | test_gqa_dense_fwd_bench[gpt-oss-sinks-prefill-8k-bfloat16] | 1.5249 | 1.3234 | -13.2% | 423.61 |
| **GQADenseFwdOp** | test_gqa_dense_fwd_bench[gpt-oss-sinks-prefill-8k-float16] | 1.5269 | 1.3276 | -13.1% | 422.28 |
| **GQADenseFwdOp** | test_gqa_dense_fwd_bench[gpt-oss-sinks-prefill-4k-bfloat16] | 0.4280 | 0.3732 | -12.8% | 375.57 |
| **GQADenseFwdOp** | test_gqa_dense_fwd_bench[starcoderbase-3b-8k-bfloat16] | 0.0317 | 0.0280 | -11.7% | 53.18 |

## 🔵 Moved Since Previous Run

> Moves against the most recent reading. A row restored to its old level appears only here: returning is not a new 14-day record.

| Op | Config | Previous (ms) | Current (ms) | Delta | TFLOPS |
|:---|:-------|------------:|-----------:|------:|-------:|
| **GQADenseFwdOp** | test_gqa_dense_fwd_bench[falcon-7b-2k-bfloat16] | 0.0370 | 0.0156 | -57.8% | 77.78 |
| **GQADenseFwdOp** | test_gqa_dense_fwd_bench[gpt-oss-sinks-decode-8k-bfloat16] | 0.4336 | 0.2537 | -41.5% | 34.52 |
| **GQADenseFwdOp** | test_gqa_dense_fwd_bench[gemma-2b-8k-bs1-bfloat16] | 0.0171 | 0.0113 | -34.0% | 5.97 |
| **GQADenseFwdOp** | test_gqa_dense_fwd_bench[gemma-2b-8k-bs1-float16] | 0.0171 | 0.0114 | -33.5% | 5.92 |
| **GQADenseFwdOp** | test_gqa_dense_fwd_bench[gpt-oss-sinks-window-128-bfloat16] | 0.1982 | 0.1355 | -31.6% | 128.50 |
| **GQADenseFwdOp** | test_gqa_dense_fwd_bench[gpt-oss-sinks-window-128-float16] | 0.1982 | 0.1362 | -31.3% | 127.86 |
| **AminFwdOp** | test_amin_bench[3d-multidim-float16] | 0.0048 | 0.0036 | -24.2% | 0.58 |
| **SumFwdOp** | test_sum_bench[3d-multidim-float16] | 0.0048 | 0.0036 | -23.5% | 0.57 |
| **AmaxFwdOp** | test_amax_bench[3d-multidim-float16] | 0.0048 | 0.0036 | -23.5% | 0.57 |
| **MeanFwdOp** | test_mean_bench[3d-multidim-float16] | 0.0048 | 0.0037 | -22.8% | 0.57 |
| **VectorNormFwdOp** | test_vector_norm_bench[l1-3d-multidim-float16] | 0.0047 | 0.0036 | -22.4% | 1.15 |
| **VectorNormFwdOp** | test_vector_norm_bench[inf-3d-multidim-float16] | 0.0047 | 0.0036 | -22.4% | 1.15 |
| **VectorNormFwdOp** | test_vector_norm_bench[l2-3d-multidim-float16] | 0.0048 | 0.0037 | -22.0% | 1.12 |
| **GQAVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-rope-partial-bfloat16] | 0.0522 | 0.0409 | -21.7% | 202.97 |
| **GQAVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-8b-rope-partial-float16] | 0.0515 | 0.0405 | -21.3% | 205.06 |
| **GQADenseFwdOp** | test_gqa_dense_fwd_bench[gpt-oss-sinks-prefill-2k-bfloat16] | 0.1324 | 0.1067 | -19.4% | 328.59 |
| **GQAVarlenFwdOp** | test_gqa_varlen_fwd_bench[llama-70b-fp8-q-lt-kv-float8_e4m3fn-bfloat16] | 0.1009 | 0.0813 | -19.4% | 533.67 |
| **GQADenseFwdOp** | test_gqa_dense_fwd_bench[llama-8b-softcap-float16] | 0.1569 | 0.1318 | -16.0% | 16.55 |
| **GQAVarlenFwdOp** | test_gqa_varlen_fwd_bench[qwen3-fp8-ragged-float8_e4m3fn-bfloat16] | 0.1100 | 0.0942 | -14.3% | 484.46 |
| **GQADenseFwdOp** | test_gqa_dense_fwd_bench[starcoderbase-3b-8k-bfloat16] | 0.0327 | 0.0280 | -14.3% | 53.18 |
| **GQADenseFwdOp** | test_gqa_dense_fwd_bench[gpt-oss-sinks-prefill-8k-bfloat16] | 1.5249 | 1.3234 | -13.2% | 423.61 |
| **GQADenseFwdOp** | test_gqa_dense_fwd_bench[gpt-oss-sinks-prefill-8k-float16] | 1.5269 | 1.3276 | -13.1% | 422.28 |
| **GQADenseFwdOp** | test_gqa_dense_fwd_bench[gpt-oss-sinks-prefill-4k-bfloat16] | 0.4280 | 0.3732 | -12.8% | 375.57 |

## 🔴 Baseline Performance Alerts

> TileOPs is slower than baseline (ratio < 99%). Ratio = baseline device-busy / tileops device-busy.

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[qwen3-fp8-ragged-odd-float8_e4m3fn-float8_e4m3fn-bfloat16] | 0.1837 | 0.1603 | 87.2% | fa3 |
| 🔴 | **GQADenseFwdOp** | test_gqa_dense_fwd_bench[qwen3-8b-chunked-b8-bfloat16] | 0.0686 | 0.0639 | 93.1% | fa3 |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-long-mha-bfloat16] | 0.4354 | 0.4135 | 95.0% | fa3 |
| 🔴 | **GQAPagedFwdOp** | test_gqa_paged_fwd_bench[llama-8b-fp8-prefill-float8_e4m3fn-float8_e4m3fn-bfloat16] | 0.4665 | 0.4434 | 95.0% | fa3 |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-8b-long-mha-bfloat16] | 0.4329 | 0.4139 | 95.6% | fa3 |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-70b-long-mha-float16] | 0.4346 | 0.4164 | 95.8% | fa3 |
| 🔴 | **GQABwdOp** | test_gqa_bwd_bench[llama-8b-long-mha-float16] | 0.4341 | 0.4166 | 96.0% | fa3 |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-o-proj-bfloat16] | 1.2618 | 1.2328 | 97.7% | cublaslt-best |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-down-bfloat16] | 0.1745 | 0.1708 | 97.9% | cublaslt-best |
| 🔴 | **MHADecodePagedWithKVCacheFwdOp** | test_mha_decode_paged_bench[opt-1.3b-b16-float16] | 0.0790 | 0.0773 | 98.0% | flashinfer |

<details>
<summary><strong>4 more alerts</strong></summary>

| | Op | Config | TileOPs (ms) | Baseline (ms) | Ratio | Via |
|:-|:---|:-------|------------:|-------------:|------:|:----|
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-qkv-a-bfloat16] | 0.1811 | 0.1778 | 98.2% | torch-cublas |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-decode-down-bfloat16] | 0.0134 | 0.0132 | 98.6% | torch-cublas |
| 🔴 | **GemmFwdOp** | test_gemm_bench[ds-v3-prefill-q-b-bfloat16] | 0.4136 | 0.4078 | 98.6% | cublaslt-best |
| 🔴 | **GemmINT8W8A8FwdOp** | test_gemm_int8_w8a8_bench[qwen2.5-7b-prefill-qkv-bfloat16] | 0.1052 | 0.1037 | 98.7% | vllm |

</details>

## Coverage

| Signal | Value | What it means | What a bad number costs |
| --- | --- | --- | --- |
| Never-built kernels | 48 files | no test constructs these kernels | the kernel stops compiling and nothing says so until someone runs it |
| Untested roofline math | 457 lines in `perf/` | cost-model statements that never executed | benchmarks report wrong TFLOPS while every correctness test passes |
| Untested op logic | 811 lines in `ops/`, 60.9% of branches | validation and dispatch paths not taken | a reversed shape or dtype check returns a wrong result instead of raising |

Everything outside `kernels/` accounts for 2503 untested lines; the two rows above carry the ones with an owner. Track the direction, not the absolute value. Smoke-only cases run in `gpu-smoke.yml`, so code reached solely by them counts as untested here.

### Never-built kernels

| File | Executed |
| --- | --- |
| `kernels/linear_attention/gdn/prefill_forward.py` | 3.4% |
| `kernels/linear_attention/gdn/prefill_prepare.py` | 3.6% |
| `kernels/linear_attention/deltanet/prefill_forward.py` | 4.3% |
| `kernels/linear_attention/kda/fused_program.py` | 4.3% |
| `kernels/linear_attention/kda/chunk_programs.py` | 5.0% |
| `kernels/linear_attention/gdn/prefill_common.py` | 5.3% |
| `kernels/linear_attention/gdn/prefill_fused.py` | 5.6% |
| `kernels/linear_attention/deltanet/prefill_prepare.py` | 5.7% |
| `kernels/sampling/top_k_top_p_mask.py` | 6.5% |
| `kernels/linear_attention/kda/inverse.py` | 6.7% |
| `kernels/attention/gqa/paged_rope_prepare.py` | 6.8% |
| `kernels/attention/gqa/prefill_paged_kv_append.py` | 6.9% |
| `kernels/linear_attention/delta_decode.py` | 7.8% |
| `kernels/attention/gqa/paged_fp8_ws.py` | 9.0% |
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
| `kernels/attention/mla/bwd.py` | 16.9% |
| `kernels/moe/indexed_expert_gemm.py` | 17.0% |
| `kernels/gemm/grouped/general.py` | 17.2% |
| `kernels/attention/dsa/paged_mma.py` | 17.3% |
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
| `kernels/linear_attention/gdn/prefill.py` | 22.4% |
| `kernels/norm/rms_norm_on_chip.py` | 23.1% |
| `kernels/sampling/radix_select.py` | 24.1% |

<details>
<summary>Untested pure Python, worst 15 files</summary>

| File | Uncovered | Executed |
| --- | --- | --- |
| `perf/formulas.py` | 415 | 16.3% |
| `manifest/plan.py` | 364 | 29.5% |
| `manifest/workload.py` | 181 | 61.2% |
| `ops/op_base.py` | 161 | 67.9% |
| `manifest/primitives.py` | 132 | 61.5% |
| `manifest/expr.py` | 122 | 70.7% |
| `manifest/signature.py` | 107 | 77.1% |
| `ops/_signature_codegen.py` | 87 | 89.6% |
| `trace/ui.py` | 60 | 23.1% |
| `backend/registry.py` | 57 | 46.7% |
| `manifest/kinds.py` | 53 | 79.2% |
| `ops/attention/gqa/prefill_paged_kv_append.py` | 53 | 35.4% |
| `backend/dispatch.py` | 48 | 40.0% |
| `perf/profile.py` | 42 | 22.2% |
| `ops/reduction/reduce.py` | 27 | 79.4% |

</details>

Per-line detail is in the `htmlcov/` directory of this run's `tileops_op_test` artifact.
