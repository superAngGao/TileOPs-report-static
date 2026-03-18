# TileOPs File Naming Convention Report

> This document identifies files in [tile-ai/TileOPs](https://github.com/tile-ai/TileOPs)
> whose names cannot be statically mapped to operators from the 186-op tracking list.
>
> **Goal:** After renaming, every operator's kernel/test/bench files should be
> discoverable by matching the **op name** or **sub-category name** against
> the file path and/or function name.

## Naming Rules

An operator's files are considered **correctly named** if at least one of:

1. The **file name** contains the op name (e.g. `test_relu.py` for `relu`)
2. The **file name** contains the sub-category name (e.g. `test_binary_arith.py` for `add`)
3. A **directory** in the path contains the op name (e.g. `kernels/norm/ada_layer_norm/fwd.py`)
4. For `path::fn` format, the **function name** contains the op name (e.g. `test_activation.py::test_relu_op`)

If none of these hold, the file needs renaming.

---

## Part 1: Shared Files (restructure into packages)

These single files serve many operators. Recommend splitting into a package
directory where sub-modules are named by sub-category.

| File | # Ops | Suggested Structure |
|:-----|------:|:-------------------|
| `tileops/kernels/elementwise.py` | 64 | `tileops/kernels/elementwise/` package with sub-category modules |

**Example for `tileops/kernels/elementwise.py`:**
```
tileops/kernels/elementwise/
    __init__.py
    binary_arith.py      # add, sub, mul, div, ...
    unary_math.py        # exp, log, sqrt, ...
    activation.py        # relu, gelu, silu, ...
    comparison.py        # eq, ne, gt, lt, ...
    bitwise.py           # bitwise_and, bitwise_or, ...
    logical.py           # logical_not, logical_and, ...
    special.py           # where, clamp, masked_fill, ...
    fused_gated.py       # silu_and_mul, gelu_and_mul, ...
    positional.py        # rope_neox, alibi, sinusoidal, ...
```

---

## Part 2: Individual Naming Mismatches

### Reduce ([#398](https://github.com/tile-ai/TileOPs/issues/398))

| Op | Type | Current Path | Should Contain |
|:---|:-----|:-------------|:--------------|
| `l1_norm` | kernel | `tileops/kernels/reduction/vector_norm/fwd.py` | `l1_norm` or `linalg_vector_norm` in path |
| `l2_norm` | kernel | `tileops/kernels/reduction/vector_norm/fwd.py` | `l2_norm` or `linalg_vector_norm` in path |
| `inf_norm` | kernel | `tileops/kernels/reduction/vector_norm/fwd.py` | `inf_norm` or `linalg_vector_norm` in path |

### GEMM ([#400](https://github.com/tile-ai/TileOPs/issues/400))

| Op | Type | Current Path | Should Contain |
|:---|:-----|:-------------|:--------------|
| `bmm_fp16` | kernel | `tileops/kernels/gemm/gemm.py` | `bmm_fp16` or `bmm` in path |
| `bmm_fp16` | bench | `benchmarks/ops/bench_gemm.py::bench_bmm` | `bmm_fp16` in file or fn |
| `bmm_fp8` | kernel | `tileops/kernels/gemm/gemm.py` | `bmm_fp8` or `bmm` in path |
| `groupgemm_fp16` | kernel | `tileops/kernels/grouped_gemm/grouped_gemm.py` | `groupgemm_fp16` or `groupgemm` in path |
| `groupgemm_fp16` | tests | `tests/ops/test_grouped_gemm.py::test_grouped_gemm` | `groupgemm_fp16` in file or fn |
| `groupgemm_fp16` | bench | `benchmarks/ops/bench_grouped_gemm.py::bench_grouped_gemm` | `groupgemm_fp16` in file or fn |
| `groupgemm_fp8` | kernel | `tileops/kernels/grouped_gemm/grouped_gemm.py` | `groupgemm_fp8` or `groupgemm` in path |
| `groupgemm_fp8` | bench | `benchmarks/ops/bench_grouped_gemm.py::bench_grouped_gemm_fp8` | `groupgemm_fp8` in file or fn |

### Quantize ([#401](https://github.com/tile-ai/TileOPs/issues/401))

| Op | Type | Current Path | Should Contain |
|:---|:-----|:-------------|:--------------|
| `fp8_per_tensor` | kernel | `tileops/kernels/deepseek_mla/fp8_quant.py` | `fp8_per_tensor` or `fp8_quantize` in path |
| `fp8_per_tensor` | tests | `tests/ops/test_fp8_quant.py::test_fp8_quant_op` | `fp8_per_tensor` in file or fn |
| `fp8_per_tensor` | bench | `benchmarks/ops/bench_fp8_quant.py::bench_fp8_quant` | `fp8_per_tensor` in file or fn |
| `fp8_per_block` | kernel | `tileops/kernels/deepseek_mla/fp8_quant.py` | `fp8_per_block` or `fp8_quantize` in path |
| `fp8_per_block` | bench | `benchmarks/ops/bench_fp8_quant.py::bench_fp8_block_quant` | `fp8_per_block` in file or fn |

### Sampling ([#426](https://github.com/tile-ai/TileOPs/issues/426))

| Op | Type | Current Path | Should Contain |
|:---|:-----|:-------------|:--------------|
| `chain_speculative_sampling` | kernel | `tileops/kernels/deepseek_mla/topk_selector.py` | `chain_speculative_sampling` or `chain_speculative_sampling` in path |
| `chain_speculative_sampling` | tests | `tests/ops/test_topk_selector.py::test_topk_selector_op` | `chain_speculative_sampling` in file or fn |
| `chain_speculative_sampling` | bench | `benchmarks/ops/bench_topk_selector.py::bench_topk_selector` | `chain_speculative_sampling` in file or fn |

### Flash Attention ([#403](https://github.com/tile-ai/TileOPs/issues/403))

| Op | Type | Current Path | Should Contain |
|:---|:-----|:-------------|:--------------|
| `flash_prefill_fwd` | kernel | `tileops/kernels/flash_attn/fwd.py` | `flash_prefill_fwd` or `flash_attention` in path |
| `flash_prefill_fwd` | tests | `tests/ops/test_gqa.py::test_gqa_fwd` | `flash_prefill_fwd` in file or fn |
| `flash_prefill_fwd` | tests | `tests/ops/test_mha.py::test_mha_fwd` | `flash_prefill_fwd` in file or fn |
| `flash_prefill_fwd` | bench | `benchmarks/ops/bench_gqa.py::bench_gqa_fwd` | `flash_prefill_fwd` in file or fn |
| `flash_prefill_fwd` | bench | `benchmarks/ops/bench_mha.py::bench_mha_fwd` | `flash_prefill_fwd` in file or fn |
| `flash_prefill_bwd` | kernel | `tileops/kernels/flash_attn/bwd.py` | `flash_prefill_bwd` or `flash_attention` in path |
| `flash_prefill_bwd` | tests | `tests/ops/test_gqa.py::test_gqa_bwd` | `flash_prefill_bwd` in file or fn |
| `flash_prefill_bwd` | tests | `tests/ops/test_mha.py::test_mha_bwd` | `flash_prefill_bwd` in file or fn |
| `flash_prefill_bwd` | bench | `benchmarks/ops/bench_gqa.py::bench_gqa_bwd` | `flash_prefill_bwd` in file or fn |
| `flash_prefill_bwd` | bench | `benchmarks/ops/bench_mha.py::bench_mha_bwd` | `flash_prefill_bwd` in file or fn |
| `flash_prefill_varlen_fwd` | kernel | `tileops/kernels/deepseek_nsa/gqa_sliding_window_varlen_fwd.py` | `flash_prefill_varlen_fwd` or `flash_attention` in path |
| `flash_prefill_varlen_fwd` | tests | `tests/ops/test_gqa_sliding_window_varlen_fwd.py::test_gqa_sliding_window_varlen_fwd_op` | `flash_prefill_varlen_fwd` in file or fn |
| `flash_prefill_varlen_fwd` | bench | `benchmarks/ops/bench_gqa_sliding_window_varlen_fwd.py::bench_gqa_sliding_window_varlen_fwd` | `flash_prefill_varlen_fwd` in file or fn |
| `flash_decode_fwd` | kernel | `tileops/kernels/flash_decode/gqa_decode.py` | `flash_decode_fwd` or `flash_attention` in path |
| `flash_decode_fwd` | kernel | `tileops/kernels/flash_decode/mha_decode.py` | `flash_decode_fwd` or `flash_attention` in path |
| `flash_decode_fwd` | tests | `tests/ops/test_gqa_decode.py::test_gqa_decode` | `flash_decode_fwd` in file or fn |
| `flash_decode_fwd` | tests | `tests/ops/test_mha_decode.py::test_mha_decode` | `flash_decode_fwd` in file or fn |
| `flash_decode_fwd` | bench | `benchmarks/ops/bench_gqa_decode.py::bench_gqa_decode` | `flash_decode_fwd` in file or fn |
| `flash_decode_fwd` | bench | `benchmarks/ops/bench_mha_decode.py::bench_mha_decode` | `flash_decode_fwd` in file or fn |
| `flash_decode_paged_fwd` | kernel | `tileops/kernels/flash_decode/gqa_decode_paged.py` | `flash_decode_paged_fwd` or `flash_attention` in path |
| `flash_decode_paged_fwd` | kernel | `tileops/kernels/flash_decode/mha_decode_paged.py` | `flash_decode_paged_fwd` or `flash_attention` in path |
| `flash_decode_paged_fwd` | tests | `tests/ops/test_gqa_decode_paged.py::test_gqa_decode_paged_op` | `flash_decode_paged_fwd` in file or fn |
| `flash_decode_paged_fwd` | tests | `tests/ops/test_mha_decode_paged.py::test_mha_decode_paged_op` | `flash_decode_paged_fwd` in file or fn |
| `flash_decode_paged_fwd` | bench | `benchmarks/ops/bench_gqa_decode_paged.py::bench_gqa_decode_paged` | `flash_decode_paged_fwd` in file or fn |
| `flash_decode_paged_fwd` | bench | `benchmarks/ops/bench_mha_decode_paged.py::bench_mha_decode_paged` | `flash_decode_paged_fwd` in file or fn |

### Linear Attention ([#405](https://github.com/tile-ai/TileOPs/issues/405))

| Op | Type | Current Path | Should Contain |
|:---|:-----|:-------------|:--------------|
| `gated_deltanet_chunkwise` | tests | `tests/ops/test_fused_gated.py::test_fused_gated` | `gated_deltanet_chunkwise` in file or fn |

---

## Summary

| Category | Issue | Mismatched Files |
|:---------|:------|:----------------|
| Flash Attention | [#403](https://github.com/tile-ai/TileOPs/issues/403) | 25 |
| GEMM | [#400](https://github.com/tile-ai/TileOPs/issues/400) | 8 |
| Linear Attention | [#405](https://github.com/tile-ai/TileOPs/issues/405) | 1 |
| Quantize | [#401](https://github.com/tile-ai/TileOPs/issues/401) | 5 |
| Reduce | [#398](https://github.com/tile-ai/TileOPs/issues/398) | 3 |
| Sampling | [#426](https://github.com/tile-ai/TileOPs/issues/426) | 3 |
| **Elementwise (shared file)** | [#397](https://github.com/tile-ai/TileOPs/issues/397) | 64 (kernel restructure) |
| **Total** | | **109** |
