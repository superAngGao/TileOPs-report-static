# ❌ TileOPs Nightly Report

> **2026-11-14 20:16** &ensp;|&ensp; `abe2086e` &ensp;|&ensp; NVIDIA H200

| | |
|---|---|
| **Operators** | 206 |
| **Kernels** | 355 |
| **Specs** | 0 |
| **Workloads** | 1585 |
| **Correctness** | ✅ &ensp; (2/206 ops verified, 0/0 tests) |
| **Benchmarked Ops** | 2 |
| **Benchmark Failures** | ❌ 2327 |
| **Regressions** (vs 14-day median) | ✅ None |
| **Baseline Alerts** (< 99%) | ✅ None |
| **vs Baseline** | ↑ 12 &ensp;·&ensp; ↓ 0 &ensp;/&ensp; 12 rows |
| **History window** | 13 runs, 2026-10-31 to 2026-11-12 |
| **Roofline anomalies** | ✅ None |

## ❌ Benchmark Failures

| Test | Error |
|:-----|:------|
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
| test_cumsum_bench[hidden-state-f32-bfloat16-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_cumsum_bench[long-seq-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_cumsum_bench[llama-13b-hidden-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_cumsum_bench[few-long-seq-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_cumprod_bench[hidden-state-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_cumprod_bench[hidden-state-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_cumprod_bench[hidden-state-f32-bfloat16-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_cumprod_bench[long-seq-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_cumprod_bench[llama-13b-hidden-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_cumprod_bench[few-long-seq-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
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
| test_masked_fill_bench[attn-padding-mask-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_masked_fill_bench[attn-padding-mask-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_masked_fill_bench[attn-padding-mask-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
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
| test_masked_fill_scalar_bench[attn-padding-mask-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_masked_fill_scalar_bench[attn-padding-mask-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_masked_fill_scalar_bench[attn-padding-mask-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
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
| test_div_bench[ragged-chan-broadcast-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_div_bench[unaligned-same-shape-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_div_bench[flat-prime-length-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_div_bench[unaligned-row-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
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
| test_where_bench[attn-causal-mask-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_where_bench[attn-causal-mask-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_where_bench[attn-causal-mask-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
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
| test_lerp_tensor_bench[cnn-feat-channel-weight-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lerp_tensor_bench[cnn-feat-channel-weight-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lerp_tensor_bench[cnn-feat-channel-weight-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lerp_tensor_bench[16M-scalar-weight-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lerp_tensor_bench[16M-scalar-weight-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_lerp_tensor_bench[16M-scalar-weight-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
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
| test_clamp_bench[cnn-feat-channel-bounds-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_clamp_bench[cnn-feat-channel-bounds-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_clamp_bench[cnn-feat-channel-bounds-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
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
| test_gelu_and_mul_bench[llama-8b-prefill-tanh-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gelu_and_mul_bench[llama-8b-prefill-tanh-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gelu_and_mul_bench[llama-8b-decode-tanh-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
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
| test_gdn_fwd_bench[q35-2b-2048-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-2b-2048-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-2b-6144-2048-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-2b-6144-2048-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-2b-4096-4096-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-2b-4096-4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-2b-2048-6144-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-2b-2048-6144-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-2b-1024-7168-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-2b-1024-7168-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-2b-4x2048-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-2b-4x2048-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-2b-8x1024-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-2b-8x1024-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-2b-8x8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-2b-8x8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-2b-16x8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-2b-16x8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-2b-32x8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-2b-32x8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-symmetric-65536-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-symmetric-65536-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-symmetric-32768-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-symmetric-32768-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-symmetric-16384-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-symmetric-16384-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-symmetric-8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-symmetric-8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-symmetric-4096-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-symmetric-4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-symmetric-2048-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-symmetric-2048-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-symmetric-6144-2048-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-symmetric-6144-2048-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-symmetric-4096-4096-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-symmetric-4096-4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-symmetric-2048-6144-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-symmetric-2048-6144-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-symmetric-1024-7168-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-symmetric-1024-7168-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-symmetric-4x2048-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-symmetric-4x2048-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-symmetric-8x1024-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-symmetric-8x1024-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-symmetric-8x8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-symmetric-8x8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-symmetric-16x8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-symmetric-16x8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-symmetric-32x8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-symmetric-32x8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-gva-decode-b1-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-gva-decode-b1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-gva-decode-b4-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-gva-decode-b4-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-gva-decode-b8-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-gva-decode-b8-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-gva-decode-b16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-gva-decode-b16-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-gva-decode-b32-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-gva-decode-b32-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-gva-decode-b64-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-gva-decode-b64-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-gva-decode-b128-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-gva-decode-b128-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-gva-decode-b256-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-gva-decode-b256-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-gva-decode-b512-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gdn_fwd_bench[q35-gva-decode-b512-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_bench[square-1k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_bench[square-1k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_bench[ds-v3-decode-qkv-a-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_bench[ds-v3-decode-down-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_bench[ds-v3-prefill-qkv-a-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_bench[ds-v3-prefill-down-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_bench[ds-v3-prefill-mlp-up-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_bench[ds-v3-prefill-mlp-up-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_bench[ds-v3-prefill-o-proj-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_bench[ds-v3-prefill-q-b-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_bench[ds-v3-m16-mlp-up-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_bench[ds-v3-m32-mlp-up-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_bench[ds-v3-m64-down-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_bench[ds-v3-m96-qkv-a-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_bench[ds-v3-m1-qkv-a-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_bench[ds-v3-m2-qkv-a-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_bench[qwen3-8b-gate-up-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_bench[qwen3-8b-gate-up-b32-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_bench[qwen3-8b-down-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_bench[vit-l16-in21k-head-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_bench[ds-v3-wgrad-qkv-a-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_bench[ds-v3-wgrad-mlp-up-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_bench[ds-v3-wgrad-q-b-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_bench[square-4k-tt-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_bench[qwen2.5-7b-qkv-b1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_bench[qwen2.5-7b-qkv-b64-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_bench[qwen2.5-7b-prefill-qkv-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-decode-qkv-a-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-decode-down-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-prefill-qkv-a-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-prefill-down-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-decode-qkv-a-blk-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-decode-down-blk-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-prefill-qkv-a-blk-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-prefill-down-blk-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-prefill-mlp-up-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-prefill-o-proj-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-prefill-q-b-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-m8-down-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-m1-down-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-m1-down-blk-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-decode-qkv-a-2d-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-decode-down-2d-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-prefill-qkv-a-2d-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-prefill-down-2d-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-prefill-mlp-up-2d-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-prefill-o-proj-2d-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-prefill-q-b-2d-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-m1-down-2d-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-decode-qkv-a-bias-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-decode-qkv-a-float8_e4m3fn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-decode-qkv-a-blk-float8_e4m3fn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-kv-a-m128-s1-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-kv-a-m128-s128-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-q-b-m128-s1-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-q-b-m128-s128-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-kv-b-m128-s1-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-kv-b-m128-s128-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-o-proj-m128-s1-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-o-proj-m128-s128-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-mlp-up-m128-s1-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-mlp-up-m128-s128-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-kv-a-m4096-s1-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-kv-a-m4096-s128-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-kv-b-m4096-s1-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_fp8_bench[ds-v3-kv-b-m4096-s128-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_int8_w8a8_bench[llama3-8b-qkv-b1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_int8_w8a8_bench[llama3-8b-qkv-b64-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_int8_w8a8_bench[llama3-8b-decode-qkv-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_int8_w8a8_bench[llama3-8b-prefill-qkv-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_int8_w8a8_bench[llama3-8b-down-b1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_int8_w8a8_bench[llama3-8b-down-b64-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_int8_w8a8_bench[llama3-8b-decode-down-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_int8_w8a8_bench[llama3-8b-prefill-down-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_int8_w8a8_bench[llama3-8b-gate-up-b64-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_int8_w8a8_bench[llama3-8b-prefill-gateup-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_int8_w8a8_bench[llama3-70b-qkv-b1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_int8_w8a8_bench[llama3-70b-qkv-b64-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_int8_w8a8_bench[llama3-70b-dec-qkv-tsr-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_int8_w8a8_bench[llama3-70b-prefill-qkv-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_int8_w8a8_bench[llama3-70b-down-b1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_int8_w8a8_bench[llama3-70b-down-b64-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_int8_w8a8_bench[llama3-70b-prefill-down-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_int8_w8a8_bench[qwen2.5-7b-qkv-b1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_int8_w8a8_bench[qwen2.5-7b-qkv-b64-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_int8_w8a8_bench[qwen2.5-7b-prefill-qkv-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_int8_w8a8_bench[qwen2.5-7b-down-b1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_int8_w8a8_bench[qwen2.5-7b-down-b64-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_int8_w8a8_bench[qwen2.5-7b-prefill-down-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_int8_w8a8_bench[qwen2.5-72b-down-b1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_int8_w8a8_bench[qwen2.5-72b-down-b64-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_int8_w8a8_bench[qwen2.5-72b-prefill-down-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_int8_w8a8_bench[llama3-8b-qkv-static-a-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_int8_w8a8_bench[llama3-8b-qkv-tensor-w-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_int8_w8a8_bench[llama3-8b-down-b64-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a16_bench[single-tile-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a16_bench[multi-tile-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a16_bench[decode-l2-resident-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a16_bench[decode-hbm-streaming-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a16_bench[decode-non-pow2-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a16_bench[decode-long-k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a16_bench[decode-b2-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a16_bench[decode-b8-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a16_bench[decode-b32-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a16_bench[chunked-prefill-tile-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a16_bench[prefill-mlp-up-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a16_bench[llama-8b-decode-down-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a16_bench[llama-8b-prefill-down-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a16_bench[qwen3-32b-prefill-down-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a16_bench[decode-tp8-attn-out-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-b1] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-b64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-4k] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-up-b1] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-up-b64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-up-4k] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-down-b1] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-down-b64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-down-4k] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-up-b1] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-up-b64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-up-4k] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-b2] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-b8] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-b16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-b32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-b96] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-b128] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-b512] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-b1024] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-up-tp8-b1] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-up-tp8-4k] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-tp8-b1] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-tp8-4k] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-up-tp8-b1] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-down-tp8-b1] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-b33] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-b48] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-up-b32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-up-b33] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-up-b48] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-down-b32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-down-b33] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-down-b48] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-up-b32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-up-b33] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-up-b48] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-up-tp8-b8] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-up-tp8-b16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-up-tp8-b32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-up-tp8-b33] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-up-tp8-b48] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-up-tp8-b64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-tp8-b8] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-tp8-b16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-tp8-b32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-tp8-b33] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-tp8-b48] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-tp8-b64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-up-tp8-b8] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-up-tp8-b16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-up-tp8-b32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-up-tp8-b33] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-up-tp8-b48] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-up-tp8-b64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-down-tp8-b8] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-down-tp8-b16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-down-tp8-b32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-down-tp8-b33] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-down-tp8-b48] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-down-tp8-b64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-b65] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-b80] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-b81] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-b97] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-b129] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-b192] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-b193] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-b256] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-b257] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-b384] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-b385] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-b513] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-b576] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-b577] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-down-b65] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-down-b129] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-down-b193] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-down-b257] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-down-b513] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-tp8-b65] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-tp8-b96] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-tp8-b97] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-tp8-b128] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-tp8-b129] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-tp8-b160] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-tp8-b161] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-tp8-b192] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-tp8-b193] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-down-tp8-b256] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-down-tp8-b96] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-down-tp8-b129] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-down-tp8-b192] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-70b-down-tp8-b256] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-up-b65] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-up-b129] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-up-b257] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[ds-r1-up-b513] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-8b-up-b33] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gemm_w4a8_bench[llama-8b-up-b128] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_chunk_fwd_bench[train-2k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_chunk_fwd_bench[train-2k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_chunk_fwd_bench[train-4k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_chunk_fwd_bench[train-4k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_chunk_fwd_bench[train-8k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_chunk_fwd_bench[train-8k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_chunk_fwd_bench[train-16k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_chunk_fwd_bench[train-16k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_bwd_bench[train-2k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_bwd_bench[train-2k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_bwd_bench[train-4k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_bwd_bench[train-4k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_bwd_bench[train-8k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_bwd_bench[train-8k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_bwd_bench[train-16k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_bwd_bench[train-16k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_fwd_bench[prefill-2k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_fwd_bench[prefill-4k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_fwd_bench[prefill-8k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_fwd_bench[prefill-16k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_fwd_bench[varlen-4x1k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_fwd_bench[varlen-ragged-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_fwd_bench[prefill-3000-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_fwd_bench[decode-b1-d64-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_fwd_bench[decode-b8-d128-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_fwd_bench[decode-first-token-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_fwd_bench[gla-short-continuation-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_fwd_bench[gla-continue-b4-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_decode_bench[serving-b1-h8-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_decode_bench[serving-b1-h16-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_decode_bench[serving-b1-h32-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_decode_bench[serving-b1-h48-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_decode_bench[serving-b1-h64-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_decode_bench[serving-b8-h32-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_decode_bench[serving-b8-h48-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gla_decode_bench[serving-b8-h64-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_bwd_bench[llama-8b-short-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_bwd_bench[llama-8b-short-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_bwd_bench[llama-8b-long-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_bwd_bench[llama-8b-long-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_bwd_bench[llama-70b-short-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_bwd_bench[llama-70b-short-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_bwd_bench[llama-70b-long-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_bwd_bench[llama-70b-long-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_bwd_bench[llama-8b-short-mha-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_bwd_bench[llama-8b-short-mha-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_bwd_bench[llama-8b-long-mha-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_bwd_bench[llama-8b-long-mha-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_bwd_bench[llama-70b-short-mha-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_bwd_bench[llama-70b-short-mha-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_bwd_bench[llama-70b-long-mha-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_bwd_bench[llama-70b-long-mha-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[llama-8b-4k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[llama-8b-4k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[llama-8b-32k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[llama-8b-32k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[llama-70b-4k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[llama-70b-4k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[llama-70b-32k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[llama-70b-32k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[llama-8b-softcap-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[llama-8b-4k-draft4-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[llama-8b-4k-draft4-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[llama-70b-4k-draft8-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[llama-70b-4k-draft8-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[chatglm3-6b-32k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[qwen3-30b-1k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[qwen3-30b-4k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[qwen3-30b-8k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[qwen3-30b-16k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[qwen3-30b-32k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[qwen3-30b-64k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[qwen3-30b-128k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[qwen3-30b-256k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[falcon-7b-2k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[starcoder-8k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[starcoderbase-3b-8k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[gemma-2b-8k-bs1-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[gemma-2b-8k-bs1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[gemma-2b-8k-b16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[gemma-2b-8k-b16-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[prefill-rope-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[prefill-rope-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[prefill-scaled-float8_e4m3fn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[qwen3-8b-chunked-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[qwen3-8b-chunked-b8-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[gpt-oss-sinks-prefill-2k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[gpt-oss-sinks-prefill-4k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[gpt-oss-sinks-prefill-8k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[gpt-oss-sinks-prefill-8k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[gpt-oss-sinks-window-128-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[gpt-oss-sinks-window-128-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[gpt-oss-sinks-decode-8k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_fwd_bench[scaled-fp8-sinks-prefill-float8_e4m3fn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_with_lse_fwd_bench[llama-8b-short-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_with_lse_fwd_bench[llama-8b-short-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_with_lse_fwd_bench[llama-8b-long-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_with_lse_fwd_bench[llama-8b-long-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_with_lse_fwd_bench[llama-70b-long-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_dense_with_lse_fwd_bench[llama-8b-long-mha-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-8b-uniform-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-8b-uniform-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-8b-q-lt-kv-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-8b-q-lt-kv-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-70b-q-lt-kv-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-70b-q-lt-kv-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[gpt-oss-uniform-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[gpt-oss-uniform-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[gpt-oss-q-lt-kv-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[gpt-oss-q-lt-kv-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-8b-short-w256-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-8b-short-w256-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-8b-long-w1024-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-8b-long-w1024-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-70b-short-w256-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-70b-short-w256-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-70b-long-w1024-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-70b-long-w1024-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[gemma4-31b-uniform-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[gemma4-31b-uniform-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[gemma4-31b-q-lt-kv-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[gemma4-31b-q-lt-kv-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[gemma4-26b-a4b-ragged-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[gemma4-26b-a4b-ragged-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-8b-uniform-rope-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-8b-uniform-rope-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[gpt-oss-rope-interleaved-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[gpt-oss-rope-interleaved-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-8b-rope-partial-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-8b-rope-partial-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[qwen-ragged-rope-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[qwen-ragged-rope-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-8b-serve-mixed-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-8b-serve-mixed-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-70b-serve-mixed-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-70b-serve-mixed-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[gpt-oss-serve-mixed-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[gpt-oss-serve-mixed-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-8b-chunk-decodes-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-8b-chunk-decodes-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-8b-decode-batch-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-8b-decode-batch-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-8b-decode-long-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-8b-decode-long-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-8b-spec-verify-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-8b-spec-verify-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-70b-spec-verify16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-70b-spec-verify16-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-70b-spec-long-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-70b-spec-long-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-8b-serve-rope-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-8b-serve-rope-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[gpt-oss-serve-window-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[gpt-oss-serve-window-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-8b-long-rope-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-8b-long-rope-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-8b-fp8-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-70b-fp8-q-lt-kv-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[qwen3-fp8-ragged-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-8b-fp8-w256-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[gpt-oss-sink-mixed-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[gpt-oss-sink-mixed-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_varlen_fwd_bench[llama-8b-fp8-sink-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[llama-8b-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[llama-8b-p64-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[llama-8b-32k-p64-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[llama-8b-b64-p64-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[llama-70b-p64-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[llama-8b-p256-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[llama-70b-p256-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[llama-405b-p256-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[llama-8b-p64-softcap-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[llama-8b-p16-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[llama-8b-b64-p16-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[llama-70b-p16-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[llama-8b-p64-cut-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[llama-8b-p256-cut-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[llama-8b-serving-step-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[llama-8b-sliding-window-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[llama-8b-noncausal-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[gpt-oss-120b-window-bfloat16-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[qwen3-ragged-odd-bfloat16-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[llama-8b-rope-decode-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[llama-8b-rope-decode-bfloat16-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[llama-8b-rope-prefill-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[llama-8b-rope-prefill-bfloat16-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[qwen-ragged-rope-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[qwen-ragged-rope-bfloat16-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[gpt-oss-sink-mixed-bfloat16-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[gpt-oss-sink-decode-bfloat16-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[llama-8b-fp8kv-decode-float16-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[llama-8b-fp8kv-decode-bfloat16-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[llama-70b-fp8kv-p16-bfloat16-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[llama-8b-fp8kv-prefill-float16-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[llama-8b-fp8kv-prefill-bfloat16-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[llama-8b-fp8-decode-float8_e4m3fn-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[llama-8b-fp8-prefill-float8_e4m3fn-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[qwen3-fp8-ragged-odd-float8_e4m3fn-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[qwen-fp8kv-ragged-rope-bfloat16-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[qwen35-9b-rope-chunk-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[qwen35-9b-mixed-chunk-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[llama-8b-rope-chunk-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[synthetic-softcap-chunk-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[falcon-7b-chunk-bfloat16-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[starcoder-chunk-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[gemma-2b-chunk-bfloat16-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[qwen35-9b-chunk-fp8kv-float16-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[llama-8b-chunk-fp8kv-float16-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_gqa_paged_fwd_bench[softcap-chunk-fp8kv-float16-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_group_norm_bench[image-affine-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_group_norm_bench[image-affine-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_group_norm_bench[wider-channel-affine-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_group_norm_bench[wider-channel-affine-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_group_norm_bench[tail-spatial-affine-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_group_norm_no_affine_bench[image-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_group_norm_no_affine_bench[image-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_group_norm_no_affine_bench[wider-channel-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_group_norm_no_affine_bench[wider-channel-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_group_norm_no_affine_bench[tail-spatial-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_grouped_gemm_bench[moe-fwd-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_grouped_gemm_bench[moe-fwd-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_grouped_gemm_bench[moe-dgrad-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_grouped_gemm_bench[moe-wgrad-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_grouped_gemm_bench[qwen3-30b-ep8-empty-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_grouped_gemm_bench[qwen3-30b-ep8-routed1k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_grouped_gemm_bench[qwen3-30b-ep8-ragged-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_grouped_gemm_bench[qwen3-30b-ep8-skew-up-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_grouped_gemm_bench[qwen3-30b-ep8-skew-down-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_grouped_gemm_bench[qwen3-30b-ep8-skew-dec-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_hadamard_transform_bench[llama-8b-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_hadamard_transform_bench[llama-8b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_hadamard_transform_bench[llama-8b-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_hadamard_transform_bench[llama-70b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_hadamard_transform_bench[llama-70b-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_hadamard_transform_bench[llama3-head-dim-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_hadamard_transform_bench[non-pow2-order20-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_instance_norm_bench[image-affine-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_instance_norm_bench[image-affine-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_instance_norm_bench[wider-channel-affine-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_instance_norm_bench[wider-channel-affine-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_instance_norm_bench[tail-spatial-affine-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_instance_norm_bench[image-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_instance_norm_bench[image-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_instance_norm_bench[wider-channel-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_instance_norm_bench[wider-channel-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_instance_norm_bench[tail-spatial-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_instance_norm_bench[image-track-stats-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_instance_norm_bench[image-eval-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int4_quant_per_group_bench[llama-8b-mlp-up-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int4_quant_per_group_bench[llama-8b-q-proj-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int4_quant_per_group_bench[llama-70b-mlp-down-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int4_quant_per_group_bench[qwen3-32b-o-proj-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int4_quant_per_group_bench[qwen2-7b-mlp-up-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int4_quant_per_group_bench[qwen2-7b-mlp-down-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int4_quant_per_group_bench[opt-13b-mlp-up-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int4_quant_per_group_bench[llama-8b-mlp-up-chan-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_dequant_per_channel_bench[llama-8b-mlp-up-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_dequant_per_channel_bench[llama-8b-mlp-up-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_dequant_per_channel_bench[llama-70b-mlp-down-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_dequant_per_channel_bench[llama-8b-mlp-down-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_dequant_per_channel_bench[gpt-oss-20b-mlp-up-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_dequant_per_channel_bench[ragged-k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_dequant_per_channel_bench[ragged-k-few-rows-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_dequant_per_tensor_bench[llama-8b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_dequant_per_tensor_bench[llama-8b-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_dequant_per_tensor_bench[qwen3-32b-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_dequant_per_tensor_bench[qwen3-32b-prefill-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_dequant_per_tensor_bench[gpt-oss-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_dequant_per_tensor_bench[ragged-k-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_dequant_per_tensor_bench[ragged-k-few-rows-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_dequant_per_block_bench[ds-v3-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_dequant_per_block_bench[ds-v3-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_dequant_per_block_bench[qwen3-235b-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_dequant_per_block_bench[gpt-oss-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_dequant_per_block_bench[ragged-k-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_dequant_per_block_bench[ragged-k-few-rows-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_quant_per_block_bench[ds-v3-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_quant_per_block_bench[ds-v3-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_quant_per_block_bench[ds-v3-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_quant_per_block_bench[qwen3-235b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_quant_per_block_bench[qwen3-235b-prefill-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_quant_per_block_bench[ds-v3-decode-few-tokens-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_quant_per_block_bench[gpt-oss-20b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_quant_per_block_bench[ragged-k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_quant_per_channel_bench[llama-8b-mlp-up-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_quant_per_channel_bench[llama-8b-mlp-up-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_quant_per_channel_bench[llama-70b-mlp-down-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_quant_per_channel_bench[qwen3-32b-o-proj-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_quant_per_channel_bench[qwen3-32b-o-proj-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_quant_per_channel_bench[gpt-oss-20b-mlp-up-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_quant_per_channel_bench[ragged-k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_quant_per_channel_bench[ragged-k-few-rows-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_quant_per_tensor_bench[llama-8b-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_quant_per_tensor_bench[llama-8b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_quant_per_tensor_bench[llama-8b-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_quant_per_tensor_bench[qwen3-32b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_quant_per_tensor_bench[qwen3-32b-prefill-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_quant_per_tensor_bench[gpt-oss-20b-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_quant_per_tensor_bench[gpt-oss-20b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_int8_quant_per_tensor_bench[odd-hidden-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kda-tp1-4x1024-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kda-tp1-4x1024-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kda-tp1-4x8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kda-tp1-decode-b1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kda-tp1-decode-b64-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kda-tp1-raw-gate-4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kda-raw-gate-decode-b8-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kda-bounded-packed-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kl48-tp1-s1024-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kl48-tp1-s16384-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kl48-tp2-s4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kl48-tp2-s32768-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kl48-tp4-s4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kl48-tp4-s65536-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kl48-tp8-s4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kl48-tp8-s131072-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kl48-tp1-mixed8k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kl48-tp8-4x8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kl48-tp8-cont256-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kl48-tp8-cont4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kl48-tp8-b32-s256-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kimi-k3-tp1-s1024-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kimi-k3-tp1-s4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kimi-k3-tp1-s16384-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kimi-k3-tp2-s4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kimi-k3-tp2-s32768-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kimi-k3-tp4-s4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kimi-k3-tp4-s65536-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kimi-k3-tp8-s4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kimi-k3-tp8-s131072-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kimi-k3-tp1-mixed8k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kimi-k3-tp8-4x8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kimi-k3-tp8-cont256-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kimi-k3-tp8-cont4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kimi-k3-tp8-b32-s256-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kda-tp1-4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kda-tp1-16384-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kda-tp1-65536-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kda-tp2-4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kda-tp2-16384-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kda-tp2-65536-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kda-tp4-4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kda-tp4-16384-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kda-tp4-65536-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kda-tp8-4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kda-tp8-16384-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kda-tp8-65536-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kda-tp1-1024-7168-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kda-tp1-16x8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kda-tp8-1024-7168-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kda-tp8-16x8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kda-tp1-decode-b8-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kda-tp1-decode-b32-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kda-tp1-decode-b128-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kda-tp1-decode-b256-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kda-tp8-decode-b32-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_kda_fwd_bench[kda-tp8-decode-b256-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_any_bench[mask-validation-4k-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_any_bench[mask-validation-4k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_any_bench[mask-validation-4k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_any_bench[mask-validation-4k-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_any_bench[mask-validation-32k-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_any_bench[mask-validation-32k-int32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_any_bench[mask-validation-32k-int64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_any_bench[3d-multidim-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_any_bench[3d-multidim-complex64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_any_bench[3d-multidim-complex128] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_any_bench[mlp-intermediate-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_all_bench[mask-validation-4k-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_all_bench[mask-validation-4k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_all_bench[mask-validation-4k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_all_bench[mask-validation-4k-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_all_bench[mask-validation-32k-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_all_bench[mask-validation-32k-int32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_all_bench[mask-validation-32k-int64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_all_bench[3d-multidim-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_all_bench[3d-multidim-complex64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_all_bench[3d-multidim-complex128] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_all_bench[mlp-intermediate-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_count_nonzero_bench[sparsity-hidden-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_count_nonzero_bench[sparsity-hidden-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_count_nonzero_bench[sparsity-hidden-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_count_nonzero_bench[sparsity-seq-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_count_nonzero_bench[sparsity-seq-bool] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_count_nonzero_bench[sparsity-seq-int32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_count_nonzero_bench[sparsity-seq-int64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_count_nonzero_bench[3d-multidim-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_count_nonzero_bench[3d-multidim-complex64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_count_nonzero_bench[3d-multidim-complex128] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_count_nonzero_bench[sparsity-mlp-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ssd_chunk_coupling_fwd_bench[mamba2-780m-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ssd_chunk_coupling_fwd_bench[mamba2-2p7b-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ssd_chunk_coupling_fwd_bench[mamba2-grouped-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ssd_chunk_cumsum_fwd_bench[mamba2-780m-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ssd_chunk_cumsum_fwd_bench[mamba2-1p3b-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ssd_chunk_cumsum_fwd_bench[mamba2-780m-dt-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ssd_chunk_cumsum_fwd_bench[mamba2-1p3b-dt-bias-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ssd_chunk_cumsum_fwd_bench[mamba2-2p7b-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ssd_chunk_scan_fwd_bench[mamba2-780m-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ssd_chunk_scan_fwd_bench[mamba2-780m-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ssd_chunk_scan_fwd_bench[mamba2-2p7b-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ssd_chunk_scan_fwd_bench[mamba2-1p3b-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ssd_chunk_state_fwd_bench[mamba2-780m-float16-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ssd_chunk_state_fwd_bench[mamba2-780m-bfloat16-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ssd_chunk_state_fwd_bench[mamba2-2p7b-bfloat16-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ssd_chunk_state_fwd_bench[mamba2-780m-seq-idx-float16-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ssd_chunk_state_fwd_bench[mamba2-780m-seq-idx-bfloat16-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ssd_chunk_state_fwd_bench[mamba2-1p3b-float16-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ssd_state_passing_fwd_bench[mamba2-1p3b-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ssd_state_passing_fwd_bench[mamba2-1p3b-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ssd_state_passing_fwd_bench[mamba2-2p7b-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ssd_state_passing_fwd_bench[mamba2-1p3b-init-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ssd_state_passing_fwd_bench[mamba2-1p3b-init-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ssd_state_passing_fwd_bench[mamba2-1p3b-flat-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ssd_decode_bench[mamba2-1p3b-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ssd_decode_bench[mamba2-1p3b-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ssd_decode_bench[mamba2-2p7b-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ssd_decode_bench[mamba2-780m-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mamba2_fwd_bench[mamba2-2p7b-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mamba2_fwd_bench[mamba2-1p3b-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mamba2_fwd_bench[mamba2-2p7b-dt-bias-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mamba2_fwd_bench[mamba2-1p3b-dt-bias-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mamba2_fwd_bench[mamba2-2p7b-init-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mamba2_fwd_bench[mamba2-1p3b-init-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mamba2_fwd_bench[mamba2-2p7b-dt-bias-init-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mamba2_fwd_bench[mamba2-1p3b-dt-bias-init-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_causal_conv1d_bench[mamba2-2.7b-prefill-4k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_causal_conv1d_bench[mamba2-2.7b-pf4k-nost-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_causal_conv1d_bench[mamba2-2.7b-prefill-32k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_causal_conv1d_bench[qwen3-next-pf4k-ragged-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_causal_conv1d_bench[qwen3-next-prefill-32k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_causal_conv1d_update_bench[mamba2-2.7b-decode-b1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_causal_conv1d_update_bench[mamba2-2.7b-decode-b64-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_causal_conv1d_update_bench[mamba2-2.7b-decode-b256-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_causal_conv1d_update_bench[qwen3-next-decode-b64-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_selective_scan_bench[mamba-2.8b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_selective_scan_bench[mamba-2.8b-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_selective_scan_bench[mamba-2.8b-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_selective_scan_bench[mamba-2.8b-decode-b64-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_selective_scan_bench[mamba-1.4b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_selective_scan_bench[mamba-130m-no-gate-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_selective_scan_bench[mamba-2.8b-packed-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_selective_scan_bench[grouped-state-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_selective_scan_bench[bare-scan-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_merge_attention_states_bench[ds-v3-chunked-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_merge_attention_states_bench[ds-v3-chunked-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_merge_attention_states_bench[llama-70b-cascade-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_merge_attention_states_bench[qwen3-235b-dcp-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_merge_attention_states_bench[qwen3-235b-dcp-ragged-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_merge_attention_states_bench[ds-v3-chunked-log2-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_merge_attention_states_bench[ds-v3-chunked-log2-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_merge_attention_states_bench[llama-70b-cascade-log2-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_merge_attention_states_bench[qwen3-235b-dcp-log2-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_merge_attention_states_bench[qwen3-dcp-ragged-log2-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mha_decode_paged_bench[serving-p128-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mha_decode_paged_bench[serving-b2-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mha_decode_paged_bench[serving-kv1k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mha_decode_paged_bench[serving-kv512-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mha_decode_paged_bench[speculative-decode-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mha_decode_paged_bench[opt-1.3b-b1-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mha_decode_paged_bench[opt-1.3b-b16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mha_decode_paged_bench[phi-2-b16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mha_decode_paged_bench[llama-2-7b-spec-b16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mha_decode_paged_bench[gemma-7b-spec-b8-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mhc_pre_bench[hidden-1280] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mhc_pre_bench[hidden-1920] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mhc_pre_bench[hidden-2560] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mhc_post_bench[hidden-1280] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mhc_post_bench[hidden-1920] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mhc_post_bench[hidden-2560] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_min_p_mask_bench[llama-8b-b1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_min_p_mask_bench[llama-8b-b1-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_min_p_mask_bench[llama-8b-b64-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_min_p_mask_bench[llama-8b-b256-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_min_p_mask_bench[llama-8b-b256-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_min_p_mask_bench[qwen3-235b-b128-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_min_p_mask_bench[deepseek-v3-b17-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_min_p_mask_bench[llama2-7b-b100-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_decode_bench[ds-v2-4k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_decode_bench[ds-v2-4k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_decode_bench[ds-v2-32k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_decode_bench[ds-v2-32k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_decode_bench[ds-v3-4k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_decode_bench[ds-v3-32k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_decode_bench[ds-v3-single-request-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_decode_bench[ds-v3-single-request-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_decode_bench[ds-v3-serving-batch-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_decode_bench[ds-v3-serving-batch-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_decode_bench[mla-b128-4096-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_decode_bench[mla-b128-4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_decode_bench[mla-b128-8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_decode_bench[mla-b128-8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_decode_bench[mla-b128-16384-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_decode_bench[mla-b128-16384-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_decode_bench[mla-b128-32768-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_decode_bench[mla-b128-32768-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_decode_bench[mla-tp-b1-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_decode_bench[mla-tp-b1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_decode_bench[mla-tp-b2-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_decode_bench[mla-tp-b2-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_decode_bench[mla-tp-b6-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_decode_bench[mla-tp-b6-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_decode_bench[mla-tp-b64-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_decode_bench[mla-tp-b64-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_paged_bench[ds-v3-4k-bfloat16-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_paged_bench[ds-v3-4k-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_paged_bench[ds-v3-32k-bfloat16-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_paged_bench[ds-v3-mtp-bfloat16-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_paged_bench[kimi-k2-fp8-bfloat16-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_paged_bench[ds-v3-ragged-bfloat16-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_varlen_fwd_bench[ds-v3-8x4k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_varlen_fwd_bench[ds-v3-8x4k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_varlen_fwd_bench[ds-v3-mixed-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_varlen_fwd_bench[kimi-k2-4x8k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_dense_bwd_bench[ds-v3-4k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_dense_bwd_bench[ds-v3-4k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_dense_bwd_bench[ds-v3-b2-8k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_dense_bwd_bench[kimi-k2-8k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_dense_bwd_bench[ds-v2-lite-3k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_varlen_bwd_bench[ds-v3-8x4k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_varlen_bwd_bench[ds-v3-8x4k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_varlen_bwd_bench[ds-v3-mixed-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_varlen_bwd_bench[kimi-k2-4x8k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_kv_cache_write_bench[ds-v3-decode-bfloat16-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_kv_cache_write_bench[ds-v3-prefill-bfloat16-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_kv_cache_write_bench[ds-v3-prefill-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_kv_cache_write_bench[ds-v3-fp8-rope-bfloat16-float8_e4m3fn-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_kv_cache_write_bench[kimi-k2-rope-bfloat16-bfloat16-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mla_kv_cache_write_bench[odd-tokens-neox-fp8-float16-float8_e4m3fn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_fp8_bench[ds-v3-e8-up-masked] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_fp8_bench[ds-v3-e8-down-masked] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_fp8_bench[ds-v3-dec-b64-up] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_fp8_bench[ds-v3-dec-b64-down] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_fp8_bench[ds-v3-dec-b256-up] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_fp8_bench[ds-v3-dec-b256-down] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_fp8_bench[qwen3-235b-dec-b64-up] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_fp8_bench[qwen3-235b-dec-b64-down] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_fp8_bench[qwen3-235b-dec-b256-up] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_fp8_bench[qwen3-235b-dec-b256-down] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_fp8_bench[kimi-k2-dec-b64-up] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_fp8_bench[kimi-k2-dec-b64-down] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_fp8_bench[kimi-k2-dec-b256-up] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_fp8_bench[kimi-k2-dec-b256-down] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_fp8_bench[qwen3-30b-ep8-skew-up] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_fp8_bench[qwen3-30b-ep8-skew-down] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_fp8_bench[ds-v3-ep8-prefill-up] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_fp8_bench[ds-v3-ep8-prefill-down] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_permute_align_bench[kimi-k2-t1] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_permute_align_bench[kimi-k2-t32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_permute_align_bench[kimi-k2-t512] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_permute_align_bench[kimi-k2-t4096] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_permute_align_bench[ds-v3-t1] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_permute_align_bench[ds-v3-t32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_permute_align_bench[ds-v3-t512] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_permute_align_bench[ds-v3-t4096] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_permute_align_bench[qwen3-235b-t1] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_permute_align_bench[qwen3-235b-t32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_permute_align_bench[qwen3-235b-t512] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_permute_align_bench[qwen3-235b-t4096] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_pre_permute_bench[decode-t32-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_pre_permute_bench[decode-t32-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_pre_permute_bench[prefill-t512-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_pre_permute_bench[prefill-t512-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_pre_permute_bench[ds-v3-ep8-t100-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_pre_permute_bench[ds-v3-ep8-t100-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_pre_permute_bench[qwen3-30b-ep8-b1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_post_permute_bench[decode-t32-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_post_permute_bench[decode-t32-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_post_permute_bench[decode-t32-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_post_permute_bench[decode-t32-bfloat16-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_post_permute_bench[prefill-t512-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_post_permute_bench[prefill-t512-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_post_permute_bench[ds-v3-ep8-t100-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_post_permute_bench[ds-v3-ep8-t100-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_post_permute_bench[qwen3-30b-ep8-b1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_bench[ds-v3-decode-mlp-up-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_bench[ds-v3-decode-mlp-up-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_bench[ds-v3-prefill-mlp-up-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_bench[ds-v3-decode-down-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_bench[ds-v3-decode-down-bfloat16-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_bench[ds-v3-prefill-down-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_bench[ds-v3-decode-swiglu-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_bench[ds-v3-prefill-swiglu-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_bench[ds-v3-ep8-masked-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_bench[qwen3-30b-ep8-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_bench[qwen3-30b-ep8-routed256-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_bench[gpt-oss-120b-t64-up-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_bench[gpt-oss-120b-t64-down-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_bench[gpt-oss-120b-t4096-up-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_bench[gpt-oss-120b-t4096-down-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_bench[gpt-oss-20b-t1024-up-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_grouped_gemm_bench[gpt-oss-20b-t1024-down-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_expert_mlp_bench[qwen3-235b-decode-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_expert_mlp_bench[qwen3-235b-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_expert_mlp_bench[qwen3-235b-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_expert_mlp_bench[qwen3-235b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_expert_mlp_bench[ds-v3-decode-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_expert_mlp_bench[ds-v3-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_expert_mlp_bench[ds-v3-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_expert_mlp_bench[ds-v3-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_expert_mlp_bench[gpt-oss-120b-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_expert_mlp_bench[gpt-oss-120b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_moe_expert_mlp_bench[gpt-oss-20b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[llama-8b-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[llama-8b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[llama-8b-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[llama-70b-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[llama-70b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[llama-70b-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[llama-405b-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[llama-405b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[llama-405b-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[llama-13b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[qk-norm-head-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[quack-throughput-256-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[quack-throughput-256-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[quack-throughput-512-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[quack-throughput-512-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[quack-throughput-1024-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[quack-throughput-1024-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[quack-throughput-2048-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[quack-throughput-2048-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[quack-throughput-4096-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[quack-throughput-4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[quack-throughput-8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[quack-throughput-8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[quack-throughput-16384-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[quack-throughput-16384-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[quack-throughput-32768-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[quack-throughput-32768-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[quack-throughput-65536-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[quack-throughput-65536-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[quack-throughput-131072-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[quack-throughput-131072-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[quack-throughput-262144-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[quack-throughput-262144-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rms_norm_bench[qwen3-8b-qk-norm-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_add_rms_norm_bench[llama-8b-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_add_rms_norm_bench[llama-8b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_add_rms_norm_bench[llama-8b-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_add_rms_norm_bench[llama-70b-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_add_rms_norm_bench[llama-70b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_add_rms_norm_bench[llama-70b-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_add_rms_norm_bench[llama-405b-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_add_rms_norm_bench[llama-405b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_add_rms_norm_bench[llama-405b-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_add_rms_norm_bench[llama-13b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_add_rms_norm_per_token_quant_bench[llama-8b-prefill-bfloat16-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_add_rms_norm_per_token_quant_bench[llama-8b-prefill-i8-bfloat16-int8] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_add_rms_norm_per_token_quant_bench[llama-8b-decode-b1-bfloat16-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_add_rms_norm_per_token_quant_bench[llama-8b-decode-b64-bfloat16-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_add_rms_norm_per_token_quant_bench[llama-8b-decode-b256-bfloat16-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_add_rms_norm_per_token_quant_bench[llama-70b-prefill-bfloat16-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_add_rms_norm_per_token_quant_bench[llama-70b-prefill-i8-float16-int8] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_add_rms_norm_per_token_quant_bench[llama-70b-decode-b1-bfloat16-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_add_rms_norm_per_token_quant_bench[llama-70b-decode-b64-bfloat16-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_add_rms_norm_per_token_quant_bench[llama-70b-decode-b256-bfloat16-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_add_rms_norm_per_token_quant_bench[clamped-amax-bfloat16-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_add_rms_norm_per_token_quant_bench[llama-13b-prefill-bfloat16-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_layer_norm_bench[llama-8b-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_layer_norm_bench[llama-8b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_layer_norm_bench[llama-8b-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_layer_norm_bench[llama-70b-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_layer_norm_bench[llama-70b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_layer_norm_bench[llama-70b-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_layer_norm_bench[llama-405b-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_layer_norm_bench[llama-405b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_layer_norm_bench[llama-405b-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_layer_norm_bench[llama-13b-prefill-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_layer_norm_bench[dit-xl-2-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_add_layer_norm_bench[llama-8b-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_add_layer_norm_bench[llama-8b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_add_layer_norm_bench[llama-8b-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_add_layer_norm_bench[llama-70b-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_add_layer_norm_bench[llama-70b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_add_layer_norm_bench[llama-70b-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_fused_add_layer_norm_bench[llama-13b-prefill-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ada_layer_norm_bench[dit-xl-2-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ada_layer_norm_bench[dit-xl-2-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ada_layer_norm_bench[dit-xl-2-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ada_layer_norm_bench[llama-8b-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ada_layer_norm_bench[llama-8b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ada_layer_norm_bench[llama-8b-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ada_layer_norm_zero_bench[dit-xl-2-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ada_layer_norm_zero_bench[dit-xl-2-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ada_layer_norm_zero_bench[dit-xl-2-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ada_layer_norm_zero_bench[llama-8b-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ada_layer_norm_zero_bench[llama-8b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_ada_layer_norm_zero_bench[llama-8b-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_nsa_compressed_fwd_varlen_bench[prefill-8x1k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_nsa_compressed_fwd_varlen_bench[prefill-4x1k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_nsa_compressed_fwd_varlen_bench[prefill-ragged-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_nsa_topk_varlen_bench[prefill-8x1k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_nsa_topk_varlen_bench[prefill-8x1k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_nsa_topk_varlen_bench[prefill-4x1k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_nsa_topk_varlen_bench[prefill-4x1k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_nsa_topk_varlen_bench[prefill-ragged-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_nsa_topk_varlen_bench[prefill-ragged-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_nsa_topk_varlen_bench[prefill-long-context-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_nsa_topk_varlen_bench[prefill-long-context-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_nsa_topk_varlen_bench[prefill-wide-gqa-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_nsa_topk_varlen_bench[prefill-wide-gqa-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_nsa_fwd_varlen_bench[prefill-4x2k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_nsa_fwd_varlen_bench[prefill-2x4k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_nsa_fwd_varlen_bench[prefill-noncausal-2x4k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_nsa_fwd_varlen_bench[prefill-ragged-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_paged_kv_cache_gather_bench[ds-v3-chunk-fp8-float8_e4m3fn-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_paged_kv_cache_gather_bench[ds-v3-mixed-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_paged_kv_cache_gather_bench[llama-70b-cp-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_paged_kv_cache_gather_bench[mla-small-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_paged_kv_cache_gather_bench[mla-chunk-fp8-fp16-float8_e4m3fn-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_paged_kv_cache_gather_bench[llama-cp-unaligned-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_paged_kv_cache_gather_bench[mla-b256-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_paged_kv_cache_write_bench[llama-8b-decode-bfloat16-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_paged_kv_cache_write_bench[llama-8b-decode-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_paged_kv_cache_write_bench[llama-8b-prefill-bfloat16-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_paged_kv_cache_write_bench[qwen3-235b-fp8-bfloat16-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_paged_kv_cache_write_bench[gpt-oss-120b-bfloat16-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_paged_kv_cache_write_bench[odd-tokens-and-page-float16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_paged_kv_cache_write_bench[qwen3-235b-fp8-fp16-float16-float8_e4m3fn] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_avg_pool1d_bench[audio-downsample-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_avg_pool1d_bench[audio-downsample-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_avg_pool1d_bench[long-temporal-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_avg_pool1d_bench[ceil-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_avg_pool2d_bench[vision-3x3-s2-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_avg_pool2d_bench[vision-3x3-s2-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_avg_pool2d_bench[vision-5x5-s2-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_avg_pool2d_bench[ceil-divisor-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_avg_pool3d_bench[video-2x2x2-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_avg_pool3d_bench[video-2x2x2-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_avg_pool3d_bench[ceil-video-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_avg_pool3d_bench[divisor-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool1d_bench[sincnet-local-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool1d_bench[sincnet-local-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool1d_bench[textcnn-global-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool1d_bench[ecg-cnn-dilated-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool1d_indices_bench[sincnet-local-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool1d_indices_bench[sincnet-local-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool1d_indices_bench[textcnn-global-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool1d_indices_bench[ecg-cnn-dilated-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool2d_bench[resnet-stem-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool2d_bench[resnet-stem-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool2d_bench[resnet-stem-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool2d_bench[vgg-block-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool2d_bench[vgg-block-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool2d_bench[vgg-block-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool2d_bench[alexnet-ceil-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool2d_bench[alexnet-ceil-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool2d_bench[alexnet-ceil-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool2d_indices_bench[resnet-stem-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool2d_indices_bench[resnet-stem-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool2d_indices_bench[resnet-stem-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool2d_indices_bench[vgg-block-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool2d_indices_bench[vgg-block-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool2d_indices_bench[vgg-block-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool2d_indices_bench[alexnet-ceil-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool2d_indices_bench[alexnet-ceil-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool2d_indices_bench[alexnet-ceil-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool3d_bench[c3d-pool1-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool3d_bench[c3d-pool1-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool3d_bench[c3d-pool2-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool3d_bench[medicalnet-stem-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool3d_indices_bench[c3d-pool1-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool3d_indices_bench[c3d-pool1-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool3d_indices_bench[c3d-pool2-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_max_pool3d_indices_bench[medicalnet-stem-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_adaptive_avg_pool2d_bench[resnet-gap-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_adaptive_avg_pool2d_bench[spp-6x6-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_adaptive_avg_pool2d_bench[nondiv-7x7-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_adaptive_avg_pool2d_bench[resnet-gap-unbatched-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_adaptive_max_pool2d_bench[global-1x1-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_adaptive_max_pool2d_bench[spp-6x6-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_adaptive_max_pool2d_bench[nondiv-7x7-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_adaptive_max_pool2d_bench[global-1x1-unbatched-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_adaptive_max_pool2d_indices_bench[global-1x1-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_adaptive_max_pool2d_indices_bench[spp-6x6-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_adaptive_max_pool2d_indices_bench[nondiv-7x7-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_adaptive_max_pool2d_indices_bench[global-1x1-unbatched-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mean_pooling_bench[uniform-8k-float16-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mean_pooling_bench[uniform-8k-bfloat16-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mean_pooling_bench[uniform-batched-float16-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mean_pooling_bench[ragged-even-float16-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mean_pooling_bench[ragged-even-float32-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mean_pooling_bench[ragged-tail-float16-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mean_pooling_bench[ragged-batched-float16-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sum_bench[hidden-state-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sum_bench[hidden-state-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sum_bench[long-seq-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sum_bench[hidden-state-dim0-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sum_bench[hidden-state-keepdim-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sum_bench[3d-multidim-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sum_bench[mlp-intermediate-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sum_bench[hidden-state-bfloat16-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mean_bench[hidden-state-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mean_bench[hidden-state-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mean_bench[long-seq-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mean_bench[3d-multidim-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mean_bench[mlp-intermediate-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_mean_bench[hidden-state-bfloat16-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_amax_bench[hidden-state-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_amax_bench[hidden-state-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_amax_bench[long-seq-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_amax_bench[3d-multidim-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_amax_bench[mlp-intermediate-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_amin_bench[hidden-state-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_amin_bench[hidden-state-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_amin_bench[long-seq-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_amin_bench[3d-multidim-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_amin_bench[mlp-intermediate-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_prod_bench[hidden-state-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_prod_bench[hidden-state-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_prod_bench[long-seq-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_prod_bench[3d-non-last-axis-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_prod_bench[mlp-intermediate-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_prod_bench[hidden-state-bfloat16-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_std_bench[hidden-state-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_std_bench[hidden-state-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_std_bench[long-seq-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_std_bench[3d-multidim-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_std_bench[mlp-intermediate-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_std_bench[hidden-state-biased-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_var_bench[hidden-state-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_var_bench[hidden-state-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_var_bench[long-seq-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_var_bench[3d-multidim-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_var_bench[mlp-intermediate-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_var_bench[hidden-state-biased-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_var_mean_bench[hidden-state-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_var_mean_bench[hidden-state-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_var_mean_bench[long-seq-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_var_mean_bench[3d-multidim-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_var_mean_bench[mlp-intermediate-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_var_mean_bench[hidden-state-biased-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rope_bench[neox-1d-2k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rope_bench[neox-1d-2k-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rope_bench[neox-1d-4k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rope_bench[neox-2d-2k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rope_bench[interleaved-1d-2k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rope_bench[interleaved-2d-2k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rope_bench[interleaved-1d-5k-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rope_llama31_bench[1d-8k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rope_llama31_bench[2d-8k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rope_llama31_bench[1d-5k-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_yarn_bench[1d-8k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_yarn_bench[2d-8k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_yarn_bench[1d-5k-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rope_longrope_bench[1d-8k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rope_longrope_bench[2d-8k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rope_longrope_bench[1d-5k-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rope_longrope_bench[1d-8k-rescaled-bfloat16-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rope_longrope_bench[1d-8k-rescaled-bfloat16-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rope_longrope_bench[1d-8k-rescaled-bfloat16-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rope_neox_position_ids_bench[prefill-2k-float16-int32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rope_neox_position_ids_bench[prefill-4k-bfloat16-int32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rope_neox_position_ids_bench[prefill-varlen-float32-int64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_rope_neox_position_ids_bench[qwen3-8b-decode-b32-bfloat16-int32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sampling_from_probs_bench[llama-8b-b1] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sampling_from_probs_bench[llama-8b-b64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sampling_from_probs_bench[llama-8b-b256] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sampling_from_probs_bench[qwen3-235b-b128] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sampling_from_probs_bench[gpt-oss-120b-b64] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sampling_from_probs_bench[ds-v3-b17] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_sampling_from_probs_bench[llama2-7b-b100] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_smooth_quant_bench[llama-8b-prefill-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_smooth_quant_bench[llama-8b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_smooth_quant_bench[llama-8b-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_smooth_quant_bench[llama-70b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_smooth_quant_bench[gpt-oss-20b-prefill-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_smooth_quant_bench[ragged-k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_smooth_quant_bench[ragged-k-decode-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[attn-weights-4k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[attn-weights-4k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[attn-weights-4k-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[attn-weights-32k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[lm-head-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[lm-head-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[lm-head-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[llama-8b-lm-head-bfloat16-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-256-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-256-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-256-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-512-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-512-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-512-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-1024-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-1024-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-1024-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-2048-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-2048-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-2048-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-4096-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-4096-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-4096-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-8192-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-8192-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-8192-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-16384-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-16384-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-16384-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-32768-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-32768-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-32768-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-65536-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-65536-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-65536-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-131072-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-131072-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-131072-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-262144-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-262144-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[quack-throughput-262144-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_softmax_bench[qwen3-8b-lm-head-b1-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_log_softmax_bench[attn-weights-4k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_log_softmax_bench[attn-weights-4k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_log_softmax_bench[attn-weights-4k-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_log_softmax_bench[attn-weights-32k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_log_softmax_bench[lm-head-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_log_softmax_bench[lm-head-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_log_softmax_bench[lm-head-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_log_softmax_bench[llama-8b-lm-head-bfloat16-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logsumexp_bench[attn-weights-4k-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logsumexp_bench[attn-weights-4k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logsumexp_bench[attn-weights-32k-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logsumexp_bench[lm-head-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logsumexp_bench[lm-head-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logsumexp_bench[3d-multidim-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_logsumexp_bench[llama-8b-lm-head-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_top_k_mask_bench[llama-8b-b1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_top_k_mask_bench[llama-8b-b1-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_top_k_mask_bench[llama-8b-b64-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_top_k_mask_bench[llama-8b-b256-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_top_k_mask_bench[llama-8b-b256-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_top_k_mask_bench[qwen3-235b-b128-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_top_k_mask_bench[gpt-oss-120b-b64-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_top_k_mask_bench[gpt2-b17-mixed-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_top_k_mask_bench[deepseek-v3-b17-mixed-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_top_k_top_p_mask_bench[llama-8b-b1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_top_k_top_p_mask_bench[llama-8b-b1-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_top_k_top_p_mask_bench[llama-8b-b64-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_top_k_top_p_mask_bench[llama-8b-b256-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_top_k_top_p_mask_bench[llama-8b-b256-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_top_k_top_p_mask_bench[qwen3-235b-b128-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_top_k_top_p_mask_bench[gpt2-b17-mixed-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_top_k_top_p_mask_bench[deepseek-v3-b100-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_top_p_mask_bench[llama-8b-b1-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_top_p_mask_bench[llama-8b-b1-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_top_p_mask_bench[llama-8b-b64-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_top_p_mask_bench[llama-8b-b256-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_top_p_mask_bench[llama-8b-b256-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_top_p_mask_bench[qwen3-235b-b128-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_top_p_mask_bench[gpt-oss-120b-b64-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_top_p_mask_bench[deepseek-v3-b17-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_top_p_mask_bench[llama2-7b-b100-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_topk_select_bench[prefill-k1024] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_topk_select_bench[prefill-k2048] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_topk_select_bench[ds-v32-topk-decode-b1] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_vector_norm_bench[l1-hidden-state-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_vector_norm_bench[l1-hidden-state-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_vector_norm_bench[l1-long-seq-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_vector_norm_bench[l1-3d-multidim-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_vector_norm_bench[l1-mlp-intermediate-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_vector_norm_bench[l1-hidden-state-fp32-bfloat16-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_vector_norm_bench[l2-hidden-state-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_vector_norm_bench[l2-hidden-state-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_vector_norm_bench[l2-long-seq-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_vector_norm_bench[l2-3d-multidim-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_vector_norm_bench[l2-mlp-intermediate-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_vector_norm_bench[l2-hidden-state-fp32-bfloat16-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_vector_norm_bench[inf-hidden-state-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_vector_norm_bench[inf-hidden-state-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_vector_norm_bench[inf-long-seq-bfloat16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_vector_norm_bench[inf-3d-multidim-float16] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_vector_norm_bench[inf-mlp-intermediate-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
| test_vector_norm_bench[inf-hidden-state-fp32-bfloat16-float32] | torch.AcceleratorError: CUDA error: CUDA-capable device(s) is/are busy or unavailable
Search for `cudaErrorDevicesUnavai... |
