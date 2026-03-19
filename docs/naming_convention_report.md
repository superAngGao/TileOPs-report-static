# TileOPs File Naming Convention Report

> Goal: Every op's kernel/op/test/bench files should be discoverable by
> matching the op name or sub-category name against file path/function name.

> Generated: 2026-03-19 | Total ops: 186

## Naming Rules

1. **Kernel files**: `tileops/kernels/<category_dir>/<sub_category>.py` or a package
   `tileops/kernels/<category_dir>/<sub_category>/`. The file/directory name MUST
   contain either the sub-category name or the op name.
2. **Op files**: `tileops/ops/<category_dir>/<op_name>.py` or a shared file whose
   name contains the sub-category (e.g., `elementwise.py` is acceptable for
   elementwise ops, but only if the file also appears under a category directory).
3. **Test files**: `tests/ops/test_<sub_category>.py` or `tests/ops/test_<op_name>.py`.
   The test **function** name must contain the op name (e.g., `test_add_broadcast`).
4. **Bench files**: `benchmarks/ops/bench_<sub_category>.py` or
   `benchmarks/ops/bench_<op_name>.py`. The bench function name must contain the op
   name.
5. For the shared `tileops/kernels/elementwise.py`, the proposed restructuring is:
   `tileops/kernels/elementwise/<sub_category>.py` (one file per sub-category).

### Status Legend

| Status | Meaning |
|:------:|:--------|
| OK | Current path already contains op name or sub-category name |
| RENAME | Path does not contain op/sub name; a rename is proposed |
| N/A | File type not implemented for this op |

---

## Category: Elementwise (#397)

### Sub-category: binary_arith

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| add | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/binary_arith.py` | RENAME |
| add | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/binary_arith.py` | RENAME |
| add | test | `tests/ops/test_binary_arith.py::test_add_broadcast`, `tests/ops/test_binary_arith.py::test_add_same_shape`, `tests/ops/test_binary_arith.py::test_add_strategies` | `tests/ops/test_binary_arith.py::test_add_broadcast`, `tests/ops/test_binary_arith.py::test_add_same_shape`, `tests/ops/test_binary_arith.py::test_add_strategies` (OK) | OK |
| add | bench | `benchmarks/ops/bench_binary_arith.py::bench_add`, `benchmarks/ops/bench_binary_strategy.py::bench_add_strategies` | `benchmarks/ops/bench_binary_arith.py::bench_add`, `benchmarks/ops/bench_binary_strategy.py::bench_add_strategies` (OK) | OK |
| sub | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/binary_arith.py` | RENAME |
| sub | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/binary_arith.py` | RENAME |
| sub | test | `tests/ops/test_binary_arith.py::test_sub_op` | `tests/ops/test_binary_arith.py::test_sub_op` (OK) | OK |
| sub | bench | `benchmarks/ops/bench_binary_arith.py::bench_sub` | `benchmarks/ops/bench_binary_arith.py::bench_sub` (OK) | OK |
| mul | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/binary_arith.py` | RENAME |
| mul | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/binary_arith.py` | RENAME |
| mul | test | `tests/ops/test_binary_arith.py::test_mul_op` | `tests/ops/test_binary_arith.py::test_mul_op` (OK) | OK |
| mul | bench | `benchmarks/ops/bench_binary_arith.py::bench_mul` | `benchmarks/ops/bench_binary_arith.py::bench_mul` (OK) | OK |
| div | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/binary_arith.py` | RENAME |
| div | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/binary_arith.py` | RENAME |
| div | test | `tests/ops/test_binary_arith.py::test_div_op` | `tests/ops/test_binary_arith.py::test_div_op` (OK) | OK |
| div | bench | `benchmarks/ops/bench_binary_arith.py::bench_div` | `benchmarks/ops/bench_binary_arith.py::bench_div` (OK) | OK |
| remainder | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/binary_arith.py` | RENAME |
| remainder | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/binary_arith.py` | RENAME |
| remainder | test | `tests/ops/test_binary_arith.py::test_remainder_op` | `tests/ops/test_binary_arith.py::test_remainder_op` (OK) | OK |
| remainder | bench | `benchmarks/ops/bench_binary_arith.py::bench_remainder` | `benchmarks/ops/bench_binary_arith.py::bench_remainder` (OK) | OK |
| pow | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/binary_arith.py` | RENAME |
| pow | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/binary_arith.py` | RENAME |
| pow | test | `tests/ops/test_binary_arith.py::test_pow_op` | `tests/ops/test_binary_arith.py::test_pow_op` (OK) | OK |
| pow | bench | `benchmarks/ops/bench_binary_arith.py::bench_pow` | `benchmarks/ops/bench_binary_arith.py::bench_pow` (OK) | OK |
| floor_divide | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/binary_arith.py` | RENAME |
| floor_divide | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/binary_arith.py` | RENAME |
| floor_divide | test | `tests/ops/test_binary_arith.py::test_floor_divide_op` | `tests/ops/test_binary_arith.py::test_floor_divide_op` (OK) | OK |
| floor_divide | bench | `benchmarks/ops/bench_binary_arith.py::bench_floor_divide` | `benchmarks/ops/bench_binary_arith.py::bench_floor_divide` (OK) | OK |
| lerp | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/binary_arith.py` | RENAME |
| lerp | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/binary_arith.py` | RENAME |
| lerp | test | `tests/ops/test_binary_arith.py::test_lerp_op` | `tests/ops/test_binary_arith.py::test_lerp_op` (OK) | OK |
| lerp | bench | `benchmarks/ops/bench_binary_arith.py::bench_lerp` | `benchmarks/ops/bench_binary_arith.py::bench_lerp` (OK) | OK |
| maximum | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/binary_arith.py` | RENAME |
| maximum | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/binary_arith.py` | RENAME |
| maximum | test | `tests/ops/test_binary_arith.py::test_maximum_nan_propagation`, `tests/ops/test_binary_arith.py::test_maximum_op` | `tests/ops/test_binary_arith.py::test_maximum_nan_propagation`, `tests/ops/test_binary_arith.py::test_maximum_op` (OK) | OK |
| maximum | bench | `benchmarks/ops/bench_binary_arith.py::bench_maximum` | `benchmarks/ops/bench_binary_arith.py::bench_maximum` (OK) | OK |
| minimum | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/binary_arith.py` | RENAME |
| minimum | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/binary_arith.py` | RENAME |
| minimum | test | `tests/ops/test_binary_arith.py::test_minimum_nan_propagation`, `tests/ops/test_binary_arith.py::test_minimum_op` | `tests/ops/test_binary_arith.py::test_minimum_nan_propagation`, `tests/ops/test_binary_arith.py::test_minimum_op` (OK) | OK |
| minimum | bench | `benchmarks/ops/bench_binary_arith.py::bench_minimum` | `benchmarks/ops/bench_binary_arith.py::bench_minimum` (OK) | OK |

### Sub-category: unary_math

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| exp | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/unary_math.py` | RENAME |
| exp | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/unary_math.py` | RENAME |
| exp | test | `tests/ops/test_unary_math.py::test_exp`, `tests/ops/test_unary_math.py::test_exp_edge` | `tests/ops/test_unary_math.py::test_exp`, `tests/ops/test_unary_math.py::test_exp_edge` (OK) | OK |
| exp | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_exp` | `benchmarks/ops/bench_unary_math.py::bench_exp` | RENAME |
| log | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/unary_math.py` | RENAME |
| log | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/unary_math.py` | RENAME |
| log | test | `tests/ops/test_unary_math.py::test_log`, `tests/ops/test_unary_math.py::test_log_edge` | `tests/ops/test_unary_math.py::test_log`, `tests/ops/test_unary_math.py::test_log_edge` (OK) | OK |
| log | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_log` | `benchmarks/ops/bench_unary_math.py::bench_log` | RENAME |
| sqrt | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/unary_math.py` | RENAME |
| sqrt | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/unary_math.py` | RENAME |
| sqrt | test | `tests/ops/test_unary_math.py::test_sqrt`, `tests/ops/test_unary_math.py::test_sqrt_edge` | `tests/ops/test_unary_math.py::test_sqrt`, `tests/ops/test_unary_math.py::test_sqrt_edge` (OK) | OK |
| sqrt | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_sqrt` | `benchmarks/ops/bench_unary_math.py::bench_sqrt` | RENAME |
| rsqrt | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/unary_math.py` | RENAME |
| rsqrt | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/unary_math.py` | RENAME |
| rsqrt | test | `tests/ops/test_unary_math.py::test_rsqrt`, `tests/ops/test_unary_math.py::test_rsqrt_edge` | `tests/ops/test_unary_math.py::test_rsqrt`, `tests/ops/test_unary_math.py::test_rsqrt_edge` (OK) | OK |
| rsqrt | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_rsqrt` | `benchmarks/ops/bench_unary_math.py::bench_rsqrt` | RENAME |
| abs | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/unary_math.py` | RENAME |
| abs | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/unary_math.py` | RENAME |
| abs | test | `tests/ops/test_unary_math.py::test_abs` | `tests/ops/test_unary_math.py::test_abs` (OK) | OK |
| abs | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_abs` | `benchmarks/ops/bench_unary_math.py::bench_abs` | RENAME |
| neg | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/unary_math.py` | RENAME |
| neg | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/unary_math.py` | RENAME |
| neg | test | `tests/ops/test_unary_math.py::test_neg` | `tests/ops/test_unary_math.py::test_neg` (OK) | OK |
| neg | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_neg` | `benchmarks/ops/bench_unary_math.py::bench_neg` | RENAME |
| reciprocal | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/unary_math.py` | RENAME |
| reciprocal | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/unary_math.py` | RENAME |
| reciprocal | test | `tests/ops/test_unary_math.py::test_reciprocal`, `tests/ops/test_unary_math.py::test_reciprocal_edge` | `tests/ops/test_unary_math.py::test_reciprocal`, `tests/ops/test_unary_math.py::test_reciprocal_edge` (OK) | OK |
| reciprocal | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_reciprocal` | `benchmarks/ops/bench_unary_math.py::bench_reciprocal` | RENAME |
| sign | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/unary_math.py` | RENAME |
| sign | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/unary_math.py` | RENAME |
| sign | test | `tests/ops/test_unary_math.py::test_sign`, `tests/ops/test_unary_math.py::test_sign_edge` | `tests/ops/test_unary_math.py::test_sign`, `tests/ops/test_unary_math.py::test_sign_edge` (OK) | OK |
| sign | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_sign` | `benchmarks/ops/bench_unary_math.py::bench_sign` | RENAME |
| sin | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/unary_math.py` | RENAME |
| sin | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/unary_math.py` | RENAME |
| sin | test | `tests/ops/test_unary_math.py::test_sin` | `tests/ops/test_unary_math.py::test_sin` (OK) | OK |
| sin | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_sin` | `benchmarks/ops/bench_unary_math.py::bench_sin` | RENAME |
| cos | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/unary_math.py` | RENAME |
| cos | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/unary_math.py` | RENAME |
| cos | test | `tests/ops/test_unary_math.py::test_cos` | `tests/ops/test_unary_math.py::test_cos` (OK) | OK |
| cos | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_cos` | `benchmarks/ops/bench_unary_math.py::bench_cos` | RENAME |
| floor | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/unary_math.py` | RENAME |
| floor | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/unary_math.py` | RENAME |
| floor | test | `tests/ops/test_unary_math.py::test_floor` | `tests/ops/test_unary_math.py::test_floor` (OK) | OK |
| floor | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_floor` | `benchmarks/ops/bench_unary_math.py::bench_floor` | RENAME |
| ceil | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/unary_math.py` | RENAME |
| ceil | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/unary_math.py` | RENAME |
| ceil | test | `tests/ops/test_unary_math.py::test_ceil` | `tests/ops/test_unary_math.py::test_ceil` (OK) | OK |
| ceil | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_ceil` | `benchmarks/ops/bench_unary_math.py::bench_ceil` | RENAME |
| round | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/unary_math.py` | RENAME |
| round | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/unary_math.py` | RENAME |
| round | test | `tests/ops/test_unary_math.py::test_round` | `tests/ops/test_unary_math.py::test_round` (OK) | OK |
| round | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_round` | `benchmarks/ops/bench_unary_math.py::bench_round` | RENAME |
| trunc | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/unary_math.py` | RENAME |
| trunc | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/unary_math.py` | RENAME |
| trunc | test | `tests/ops/test_unary_math.py::test_trunc` | `tests/ops/test_unary_math.py::test_trunc` (OK) | OK |
| trunc | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_trunc` | `benchmarks/ops/bench_unary_math.py::bench_trunc` | RENAME |
| erf | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/unary_math.py` | RENAME |
| erf | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/unary_math.py` | RENAME |
| erf | test | `tests/ops/test_unary_math.py::test_erf`, `tests/ops/test_unary_math.py::test_erf_edge` | `tests/ops/test_unary_math.py::test_erf`, `tests/ops/test_unary_math.py::test_erf_edge` (OK) | OK |
| erf | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_erf` | `benchmarks/ops/bench_unary_math.py::bench_erf` | RENAME |
| log1p | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/unary_math.py` | RENAME |
| log1p | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/unary_math.py` | RENAME |
| log1p | test | `tests/ops/test_unary_math.py::test_log1p`, `tests/ops/test_unary_math.py::test_log1p_edge` | `tests/ops/test_unary_math.py::test_log1p`, `tests/ops/test_unary_math.py::test_log1p_edge` (OK) | OK |
| log1p | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_log1p` | `benchmarks/ops/bench_unary_math.py::bench_log1p` | RENAME |
| expm1 | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/unary_math.py` | RENAME |
| expm1 | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/unary_math.py` | RENAME |
| expm1 | test | `tests/ops/test_unary_math.py::test_expm1`, `tests/ops/test_unary_math.py::test_expm1_edge` | `tests/ops/test_unary_math.py::test_expm1`, `tests/ops/test_unary_math.py::test_expm1_edge` (OK) | OK |
| expm1 | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_expm1` | `benchmarks/ops/bench_unary_math.py::bench_expm1` | RENAME |

### Sub-category: activation

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| relu | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/activation.py` | RENAME |
| relu | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/activation.py` | RENAME |
| relu | test | `tests/ops/test_activation.py::test_relu_op`, `tests/ops/test_activation.py::test_relu_strategies` | `tests/ops/test_activation.py::test_relu_op`, `tests/ops/test_activation.py::test_relu_strategies` (OK) | OK |
| relu | bench | `benchmarks/ops/bench_activation.py::bench_relu`, `benchmarks/ops/bench_unary_strategy.py::bench_relu_strategies` | `benchmarks/ops/bench_activation.py::bench_relu`, `benchmarks/ops/bench_unary_strategy.py::bench_relu_strategies` (OK) | OK |
| gelu | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/activation.py` | RENAME |
| gelu | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/activation.py` | RENAME |
| gelu | test | `tests/ops/test_activation.py::test_gelu` | `tests/ops/test_activation.py::test_gelu` (OK) | OK |
| gelu | bench | `benchmarks/ops/bench_activation.py::bench_gelu` | `benchmarks/ops/bench_activation.py::bench_gelu` (OK) | OK |
| silu | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/activation.py` | RENAME |
| silu | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/activation.py` | RENAME |
| silu | test | `tests/ops/test_activation.py::test_silu` | `tests/ops/test_activation.py::test_silu` (OK) | OK |
| silu | bench | `benchmarks/ops/bench_activation.py::bench_silu` | `benchmarks/ops/bench_activation.py::bench_silu` (OK) | OK |
| sigmoid | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/activation.py` | RENAME |
| sigmoid | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/activation.py` | RENAME |
| sigmoid | test | `tests/ops/test_activation.py::test_sigmoid`, `tests/ops/test_activation.py::test_sigmoid_edge` | `tests/ops/test_activation.py::test_sigmoid`, `tests/ops/test_activation.py::test_sigmoid_edge` (OK) | OK |
| sigmoid | bench | `benchmarks/ops/bench_activation.py::bench_sigmoid` | `benchmarks/ops/bench_activation.py::bench_sigmoid` (OK) | OK |
| tanh | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/activation.py` | RENAME |
| tanh | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/activation.py` | RENAME |
| tanh | test | `tests/ops/test_activation.py::test_tanh`, `tests/ops/test_activation.py::test_tanh_edge` | `tests/ops/test_activation.py::test_tanh`, `tests/ops/test_activation.py::test_tanh_edge` (OK) | OK |
| tanh | bench | `benchmarks/ops/bench_activation.py::bench_tanh` | `benchmarks/ops/bench_activation.py::bench_tanh` (OK) | OK |
| leaky_relu | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/activation.py` | RENAME |
| leaky_relu | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/activation.py` | RENAME |
| leaky_relu | test | - | - | N/A |
| leaky_relu | bench | `benchmarks/ops/bench_activation.py::bench_leaky_relu` | `benchmarks/ops/bench_activation.py::bench_leaky_relu` (OK) | OK |
| elu | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/activation.py` | RENAME |
| elu | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/activation.py` | RENAME |
| elu | test | - | - | N/A |
| elu | bench | `benchmarks/ops/bench_activation.py::bench_elu` | `benchmarks/ops/bench_activation.py::bench_elu` (OK) | OK |
| selu | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/activation.py` | RENAME |
| selu | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/activation.py` | RENAME |
| selu | test | `tests/ops/test_activation.py::test_selu` | `tests/ops/test_activation.py::test_selu` (OK) | OK |
| selu | bench | `benchmarks/ops/bench_activation.py::bench_selu` | `benchmarks/ops/bench_activation.py::bench_selu` (OK) | OK |
| hardswish | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/activation.py` | RENAME |
| hardswish | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/activation.py` | RENAME |
| hardswish | test | `tests/ops/test_activation.py::test_hardswish` | `tests/ops/test_activation.py::test_hardswish` (OK) | OK |
| hardswish | bench | `benchmarks/ops/bench_activation.py::bench_hardswish` | `benchmarks/ops/bench_activation.py::bench_hardswish` (OK) | OK |
| hardsigmoid | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/activation.py` | RENAME |
| hardsigmoid | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/activation.py` | RENAME |
| hardsigmoid | test | `tests/ops/test_activation.py::test_hardsigmoid` | `tests/ops/test_activation.py::test_hardsigmoid` (OK) | OK |
| hardsigmoid | bench | `benchmarks/ops/bench_activation.py::bench_hardsigmoid` | `benchmarks/ops/bench_activation.py::bench_hardsigmoid` (OK) | OK |
| hardtanh | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/activation.py` | RENAME |
| hardtanh | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/activation.py` | RENAME |
| hardtanh | test | - | - | N/A |
| hardtanh | bench | `benchmarks/ops/bench_activation.py::bench_hardtanh` | `benchmarks/ops/bench_activation.py::bench_hardtanh` (OK) | OK |
| softplus | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/activation.py` | RENAME |
| softplus | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/activation.py` | RENAME |
| softplus | test | - | - | N/A |
| softplus | bench | `benchmarks/ops/bench_activation.py::bench_softplus` | `benchmarks/ops/bench_activation.py::bench_softplus` (OK) | OK |
| mish | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/activation.py` | RENAME |
| mish | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/activation.py` | RENAME |
| mish | test | `tests/ops/test_activation.py::test_mish` | `tests/ops/test_activation.py::test_mish` (OK) | OK |
| mish | bench | `benchmarks/ops/bench_activation.py::bench_mish` | `benchmarks/ops/bench_activation.py::bench_mish` (OK) | OK |
| prelu | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/activation.py` | RENAME |
| prelu | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/activation.py` | RENAME |
| prelu | test | - | - | N/A |
| prelu | bench | `benchmarks/ops/bench_activation.py::bench_prelu` | `benchmarks/ops/bench_activation.py::bench_prelu` (OK) | OK |

### Sub-category: fused_gated_activation

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| silu_and_mul | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/fused_gated_activation.py` | RENAME |
| silu_and_mul | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/fused_gated_activation.py` | RENAME |
| silu_and_mul | test | `tests/ops/test_fused_gated.py::test_silu_and_mul_op` | `tests/ops/test_fused_gated_activation.py::test_silu_and_mul` | RENAME |
| silu_and_mul | bench | `benchmarks/ops/bench_activation.py::bench_silu_and_mul` | `benchmarks/ops/bench_fused_gated_activation.py::bench_silu_and_mul` | RENAME |
| gelu_and_mul | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/fused_gated_activation.py` | RENAME |
| gelu_and_mul | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/fused_gated_activation.py` | RENAME |
| gelu_and_mul | test | `tests/ops/test_fused_gated.py::test_gelu_and_mul_op` | `tests/ops/test_fused_gated_activation.py::test_gelu_and_mul` | RENAME |
| gelu_and_mul | bench | `benchmarks/ops/bench_activation.py::bench_gelu_and_mul` | `benchmarks/ops/bench_fused_gated_activation.py::bench_gelu_and_mul` | RENAME |
| gelu_tanh_and_mul | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/fused_gated_activation.py` | RENAME |
| gelu_tanh_and_mul | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/fused_gated_activation.py` | RENAME |
| gelu_tanh_and_mul | test | `tests/ops/test_fused_gated.py::test_gelu_tanh_and_mul_op` | `tests/ops/test_fused_gated_activation.py::test_gelu_tanh_and_mul` | RENAME |
| gelu_tanh_and_mul | bench | `benchmarks/ops/bench_activation.py::bench_gelu_tanh_and_mul` | `benchmarks/ops/bench_fused_gated_activation.py::bench_gelu_tanh_and_mul` | RENAME |

### Sub-category: comparison

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| eq | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/comparison.py` | RENAME |
| eq | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/comparison.py` | RENAME |
| eq | test | `tests/ops/test_comparison.py::test_eq_edge_case`, `tests/ops/test_comparison.py::test_eq_op` | `tests/ops/test_comparison.py::test_eq_edge_case`, `tests/ops/test_comparison.py::test_eq_op` (OK) | OK |
| eq | bench | `benchmarks/ops/bench_binary_elementwise.py::bench_eq` | `benchmarks/ops/bench_comparison.py::bench_eq` | RENAME |
| ne | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise.py` (OK) | OK |
| ne | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/comparison.py` | RENAME |
| ne | test | `tests/ops/test_comparison.py::test_ne_op` | `tests/ops/test_comparison.py::test_ne_op` (OK) | OK |
| ne | bench | `benchmarks/ops/bench_binary_elementwise.py::bench_ne` | `benchmarks/ops/bench_comparison.py::bench_ne` | RENAME |
| gt | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/comparison.py` | RENAME |
| gt | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/comparison.py` | RENAME |
| gt | test | `tests/ops/test_comparison.py::test_gt_op` | `tests/ops/test_comparison.py::test_gt_op` (OK) | OK |
| gt | bench | `benchmarks/ops/bench_binary_elementwise.py::bench_gt` | `benchmarks/ops/bench_comparison.py::bench_gt` | RENAME |
| lt | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/comparison.py` | RENAME |
| lt | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/comparison.py` | RENAME |
| lt | test | `tests/ops/test_comparison.py::test_lt_op` | `tests/ops/test_comparison.py::test_lt_op` (OK) | OK |
| lt | bench | `benchmarks/ops/bench_binary_elementwise.py::bench_lt` | `benchmarks/ops/bench_comparison.py::bench_lt` | RENAME |
| ge | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/comparison.py` | RENAME |
| ge | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/comparison.py` | RENAME |
| ge | test | `tests/ops/test_comparison.py::test_ge_op` | `tests/ops/test_comparison.py::test_ge_op` (OK) | OK |
| ge | bench | `benchmarks/ops/bench_binary_elementwise.py::bench_ge` | `benchmarks/ops/bench_comparison.py::bench_ge` | RENAME |
| le | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise.py` (OK) | OK |
| le | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise.py` (OK) | OK |
| le | test | `tests/ops/test_comparison.py::test_le_op` | `tests/ops/test_comparison.py::test_le_op` (OK) | OK |
| le | bench | `benchmarks/ops/bench_binary_elementwise.py::bench_le` | `benchmarks/ops/bench_binary_elementwise.py::bench_le` (OK) | OK |

### Sub-category: bitwise

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| bitwise_and | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/bitwise.py` | RENAME |
| bitwise_and | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/bitwise.py` | RENAME |
| bitwise_and | test | `tests/ops/test_bitwise.py::test_bitwise_and_op` | `tests/ops/test_bitwise.py::test_bitwise_and_op` (OK) | OK |
| bitwise_and | bench | `benchmarks/ops/bench_binary_elementwise.py::bench_bitwise_and` | `benchmarks/ops/bench_bitwise.py::bench_bitwise_and` | RENAME |
| bitwise_or | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/bitwise.py` | RENAME |
| bitwise_or | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/bitwise.py` | RENAME |
| bitwise_or | test | `tests/ops/test_bitwise.py::test_bitwise_or_op` | `tests/ops/test_bitwise.py::test_bitwise_or_op` (OK) | OK |
| bitwise_or | bench | `benchmarks/ops/bench_binary_elementwise.py::bench_bitwise_or` | `benchmarks/ops/bench_bitwise.py::bench_bitwise_or` | RENAME |
| bitwise_xor | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/bitwise.py` | RENAME |
| bitwise_xor | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/bitwise.py` | RENAME |
| bitwise_xor | test | `tests/ops/test_bitwise.py::test_bitwise_xor_op` | `tests/ops/test_bitwise.py::test_bitwise_xor_op` (OK) | OK |
| bitwise_xor | bench | `benchmarks/ops/bench_binary_elementwise.py::bench_bitwise_xor` | `benchmarks/ops/bench_bitwise.py::bench_bitwise_xor` | RENAME |
| bitwise_not | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/bitwise.py` | RENAME |
| bitwise_not | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/bitwise.py` | RENAME |
| bitwise_not | test | `tests/ops/test_bitwise.py::test_bitwise_not` | `tests/ops/test_bitwise.py::test_bitwise_not` (OK) | OK |
| bitwise_not | bench | `benchmarks/ops/bench_binary_elementwise.py::bench_bitwise_not` | `benchmarks/ops/bench_bitwise.py::bench_bitwise_not` | RENAME |

### Sub-category: logical

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| logical_not | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/logical.py` | RENAME |
| logical_not | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/logical.py` | RENAME |
| logical_not | test | `tests/ops/test_logical.py::test_logical_not` | `tests/ops/test_logical.py::test_logical_not` (OK) | OK |
| logical_not | bench | `benchmarks/ops/bench_binary_elementwise.py::bench_logical_not` | `benchmarks/ops/bench_logical.py::bench_logical_not` | RENAME |
| logical_and | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/logical.py` | RENAME |
| logical_and | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/logical.py` | RENAME |
| logical_and | test | `tests/ops/test_logical.py::test_logical_and_op` | `tests/ops/test_logical.py::test_logical_and_op` (OK) | OK |
| logical_and | bench | `benchmarks/ops/bench_binary_elementwise.py::bench_logical_and` | `benchmarks/ops/bench_logical.py::bench_logical_and` | RENAME |
| logical_or | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/logical.py` | RENAME |
| logical_or | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/logical.py` | RENAME |
| logical_or | test | `tests/ops/test_logical.py::test_logical_or_op` | `tests/ops/test_logical.py::test_logical_or_op` (OK) | OK |
| logical_or | bench | `benchmarks/ops/bench_binary_elementwise.py::bench_logical_or` | `benchmarks/ops/bench_logical.py::bench_logical_or` | RENAME |

### Sub-category: special_elementwise

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| where | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/special_elementwise.py` | RENAME |
| where | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/special_elementwise.py` | RENAME |
| where | test | - | - | N/A |
| where | bench | - | - | N/A |
| clamp | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/special_elementwise.py` | RENAME |
| clamp | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/special_elementwise.py` | RENAME |
| clamp | test | - | - | N/A |
| clamp | bench | - | - | N/A |
| masked_fill | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/special_elementwise.py` | RENAME |
| masked_fill | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/special_elementwise.py` | RENAME |
| masked_fill | test | - | - | N/A |
| masked_fill | bench | - | - | N/A |
| nan_to_num | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/special_elementwise.py` | RENAME |
| nan_to_num | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/special_elementwise.py` | RENAME |
| nan_to_num | test | - | - | N/A |
| nan_to_num | bench | - | - | N/A |
| isnan | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/special_elementwise.py` | RENAME |
| isnan | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/special_elementwise.py` | RENAME |
| isnan | test | `tests/ops/test_special_elementwise.py::test_isnan`, `tests/ops/test_special_elementwise.py::test_isnan_edge` | `tests/ops/test_special_elementwise.py::test_isnan`, `tests/ops/test_special_elementwise.py::test_isnan_edge` (OK) | OK |
| isnan | bench | - | - | N/A |
| isinf | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/special_elementwise.py` | RENAME |
| isinf | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/special_elementwise.py` | RENAME |
| isinf | test | `tests/ops/test_special_elementwise.py::test_isinf`, `tests/ops/test_special_elementwise.py::test_isinf_edge` | `tests/ops/test_special_elementwise.py::test_isinf`, `tests/ops/test_special_elementwise.py::test_isinf_edge` (OK) | OK |
| isinf | bench | - | - | N/A |
| isfinite | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/special_elementwise.py` | RENAME |
| isfinite | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/special_elementwise.py` | RENAME |
| isfinite | test | `tests/ops/test_special_elementwise.py::test_isfinite`, `tests/ops/test_special_elementwise.py::test_isfinite_edge` | `tests/ops/test_special_elementwise.py::test_isfinite`, `tests/ops/test_special_elementwise.py::test_isfinite_edge` (OK) | OK |
| isfinite | bench | - | - | N/A |

### Sub-category: dropout

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| dropout | kernel | `tileops/kernels/dropout.py` | `tileops/kernels/dropout.py` (OK) | OK |
| dropout | op | `tileops/ops/dropout.py` | `tileops/ops/dropout.py` (OK) | OK |
| dropout | test | `tests/ops/test_dropout.py::test_dropout` | `tests/ops/test_dropout.py::test_dropout` (OK) | OK |
| dropout | bench | `benchmarks/ops/bench_dropout.py::bench_dropout` | `benchmarks/ops/bench_dropout.py::bench_dropout` (OK) | OK |

### Sub-category: rope

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| rope_neox | kernel | `tileops/kernels/rope.py` | `tileops/kernels/rope.py` (OK) | OK |
| rope_neox | op | `tileops/ops/rope.py` | `tileops/ops/rope.py` (OK) | OK |
| rope_neox | test | `tests/ops/test_rope.py::test_rope_neox` | `tests/ops/test_rope.py::test_rope_neox` (OK) | OK |
| rope_neox | bench | `benchmarks/ops/bench_rope.py::bench_rope_neox` | `benchmarks/ops/bench_rope.py::bench_rope_neox` (OK) | OK |
| rope_non_neox | kernel | `tileops/kernels/rope.py` | `tileops/kernels/rope.py` (OK) | OK |
| rope_non_neox | op | `tileops/ops/rope.py` | `tileops/ops/rope.py` (OK) | OK |
| rope_non_neox | test | `tests/ops/test_rope.py::test_rope_non_neox` | `tests/ops/test_rope.py::test_rope_non_neox` (OK) | OK |
| rope_non_neox | bench | `benchmarks/ops/bench_rope.py::bench_rope_non_neox` | `benchmarks/ops/bench_rope.py::bench_rope_non_neox` (OK) | OK |
| rope_llama31 | kernel | `tileops/kernels/rope.py` | `tileops/kernels/rope.py` (OK) | OK |
| rope_llama31 | op | `tileops/ops/rope.py` | `tileops/ops/rope.py` (OK) | OK |
| rope_llama31 | test | `tests/ops/test_rope.py::test_rope_llama31` | `tests/ops/test_rope.py::test_rope_llama31` (OK) | OK |
| rope_llama31 | bench | `benchmarks/ops/bench_rope.py::bench_rope_llama31` | `benchmarks/ops/bench_rope.py::bench_rope_llama31` (OK) | OK |
| yarn_rope | kernel | `-` | `-` | N/A |
| yarn_rope | op | `-` | `-` | N/A |
| yarn_rope | test | `-` | `-` | N/A |
| yarn_rope | bench | `-` | `-` | N/A |
| longrope | kernel | `-` | `-` | N/A |
| longrope | op | `-` | `-` | N/A |
| longrope | test | `-` | `-` | N/A |
| longrope | bench | `-` | `-` | N/A |

### Sub-category: alibi

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| alibi | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/alibi.py` | RENAME |
| alibi | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/alibi.py` | RENAME |
| alibi | test | - | - | N/A |
| alibi | bench | - | - | N/A |

### Sub-category: sinusoidal

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| sinusoidal | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elementwise/sinusoidal.py` | RENAME |
| sinusoidal | op | `tileops/ops/elementwise.py` | `tileops/ops/elementwise/sinusoidal.py` | RENAME |
| sinusoidal | test | - | - | N/A |
| sinusoidal | bench | - | - | N/A |

---

## Category: Reduce (#398)

### Sub-category: reduce

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| sum | kernel | `-` | `-` | N/A |
| sum | op | `-` | `-` | N/A |
| sum | test | `-` | `-` | N/A |
| sum | bench | `-` | `-` | N/A |
| mean | kernel | `-` | `-` | N/A |
| mean | op | `-` | `-` | N/A |
| mean | test | `-` | `-` | N/A |
| mean | bench | `-` | `-` | N/A |
| amin | kernel | `-` | `-` | N/A |
| amin | op | `-` | `-` | N/A |
| amin | test | `-` | `-` | N/A |
| amin | bench | `-` | `-` | N/A |
| amax | kernel | `-` | `-` | N/A |
| amax | op | `-` | `-` | N/A |
| amax | test | `-` | `-` | N/A |
| amax | bench | `-` | `-` | N/A |
| prod | kernel | `-` | `-` | N/A |
| prod | op | `-` | `-` | N/A |
| prod | test | `-` | `-` | N/A |
| prod | bench | `-` | `-` | N/A |
| std | kernel | `-` | `-` | N/A |
| std | op | `-` | `-` | N/A |
| std | test | `-` | `-` | N/A |
| std | bench | `-` | `-` | N/A |
| var | kernel | `-` | `-` | N/A |
| var | op | `-` | `-` | N/A |
| var | test | `-` | `-` | N/A |
| var | bench | `-` | `-` | N/A |
| var_mean | kernel | `-` | `-` | N/A |
| var_mean | op | `-` | `-` | N/A |
| var_mean | test | `-` | `-` | N/A |
| var_mean | bench | `-` | `-` | N/A |

### Sub-category: softmax

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| softmax | kernel | `-` | `-` | N/A |
| softmax | op | `-` | `-` | N/A |
| softmax | test | `-` | `-` | N/A |
| softmax | bench | `-` | `-` | N/A |
| log_softmax | kernel | `-` | `-` | N/A |
| log_softmax | op | `-` | `-` | N/A |
| log_softmax | test | `-` | `-` | N/A |
| log_softmax | bench | `-` | `-` | N/A |
| logsumexp | kernel | `-` | `-` | N/A |
| logsumexp | op | `-` | `-` | N/A |
| logsumexp | test | `-` | `-` | N/A |
| logsumexp | bench | `-` | `-` | N/A |

### Sub-category: argreduce

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| argmax | kernel | `-` | `-` | N/A |
| argmax | op | `-` | `-` | N/A |
| argmax | test | `-` | `-` | N/A |
| argmax | bench | `-` | `-` | N/A |
| argmin | kernel | `-` | `-` | N/A |
| argmin | op | `-` | `-` | N/A |
| argmin | test | `-` | `-` | N/A |
| argmin | bench | `-` | `-` | N/A |

### Sub-category: cumulative

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| cumsum | kernel | `-` | `-` | N/A |
| cumsum | op | `-` | `-` | N/A |
| cumsum | test | `-` | `-` | N/A |
| cumsum | bench | `-` | `-` | N/A |
| cumprod | kernel | `-` | `-` | N/A |
| cumprod | op | `-` | `-` | N/A |
| cumprod | test | `-` | `-` | N/A |
| cumprod | bench | `-` | `-` | N/A |

### Sub-category: logical_reduce

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| any | kernel | `-` | `-` | N/A |
| any | op | `-` | `-` | N/A |
| any | test | `-` | `-` | N/A |
| any | bench | `-` | `-` | N/A |
| all | kernel | `-` | `-` | N/A |
| all | op | `-` | `-` | N/A |
| all | test | `-` | `-` | N/A |
| all | bench | `-` | `-` | N/A |

### Sub-category: linalg_vector_norm

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| l1_norm | kernel | `tileops/kernels/reduction/vector_norm/fwd.py` | `tileops/kernels/reduction/linalg_vector_norm.py` | RENAME |
| l1_norm | op | `tileops/ops/reduction/l1_norm.py` | `tileops/ops/reduction/l1_norm.py` (OK) | OK |
| l1_norm | test | `tests/ops/test_vector_norm.py::test_l1_norm` | `tests/ops/test_linalg_vector_norm.py::test_l1_norm` | RENAME |
| l1_norm | bench | `benchmarks/ops/bench_vector_norm.py::bench_l1_norm` | `benchmarks/ops/bench_linalg_vector_norm.py::bench_l1_norm` | RENAME |
| l2_norm | kernel | `tileops/kernels/reduction/vector_norm/fwd.py` | `tileops/kernels/reduction/linalg_vector_norm.py` | RENAME |
| l2_norm | op | `tileops/ops/reduction/l2_norm.py` | `tileops/ops/reduction/l2_norm.py` (OK) | OK |
| l2_norm | test | `tests/ops/test_vector_norm.py::test_l2_norm` | `tests/ops/test_linalg_vector_norm.py::test_l2_norm` | RENAME |
| l2_norm | bench | `benchmarks/ops/bench_vector_norm.py::bench_l2_norm` | `benchmarks/ops/bench_linalg_vector_norm.py::bench_l2_norm` | RENAME |
| inf_norm | kernel | `tileops/kernels/reduction/vector_norm/fwd.py` | `tileops/kernels/reduction/linalg_vector_norm.py` | RENAME |
| inf_norm | op | `tileops/ops/reduction/inf_norm.py` | `tileops/ops/reduction/inf_norm.py` (OK) | OK |
| inf_norm | test | `tests/ops/test_vector_norm.py::test_inf_norm` | `tests/ops/test_linalg_vector_norm.py::test_inf_norm` | RENAME |
| inf_norm | bench | `benchmarks/ops/bench_vector_norm.py::bench_inf_norm` | `benchmarks/ops/bench_linalg_vector_norm.py::bench_inf_norm` | RENAME |

---

## Category: Norm (#399)

### Sub-category: layer_norm

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| layer_norm | kernel | `tileops/kernels/norm/layer_norm.py` | `tileops/kernels/norm/layer_norm.py` (OK) | OK |
| layer_norm | op | `tileops/ops/norm/layer_norm.py` | `tileops/ops/norm/layer_norm.py` (OK) | OK |
| layer_norm | test | `tests/ops/test_layer_norm.py::test_layer_norm_3d`, `tests/ops/test_layer_norm.py::test_layer_norm_op` | `tests/ops/test_layer_norm.py::test_layer_norm_3d`, `tests/ops/test_layer_norm.py::test_layer_norm_op` (OK) | OK |
| layer_norm | bench | `benchmarks/ops/bench_layer_norm.py::bench_layer_norm` | `benchmarks/ops/bench_layer_norm.py::bench_layer_norm` (OK) | OK |

### Sub-category: batch_norm

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| batch_norm | kernel | `tileops/kernels/norm/batch_norm.py` | `tileops/kernels/norm/batch_norm.py` (OK) | OK |
| batch_norm | op | `tileops/ops/norm/batch_norm.py` | `tileops/ops/norm/batch_norm.py` (OK) | OK |
| batch_norm | test | `tests/ops/test_batch_norm.py::test_batch_norm_bwd`, `tests/ops/test_batch_norm.py::test_batch_norm_fwd` | `tests/ops/test_batch_norm.py::test_batch_norm_bwd`, `tests/ops/test_batch_norm.py::test_batch_norm_fwd` (OK) | OK |
| batch_norm | bench | `benchmarks/ops/bench_batch_norm.py::bench_batch_norm` | `benchmarks/ops/bench_batch_norm.py::bench_batch_norm` (OK) | OK |

### Sub-category: group_norm

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| group_norm | kernel | `tileops/kernels/norm/group_norm.py` | `tileops/kernels/norm/group_norm.py` (OK) | OK |
| group_norm | op | `tileops/ops/norm/group_norm.py` | `tileops/ops/norm/group_norm.py` (OK) | OK |
| group_norm | test | `tests/ops/test_group_norm.py::test_group_norm_non_contiguous`, `tests/ops/test_group_norm.py::test_group_norm_op` | `tests/ops/test_group_norm.py::test_group_norm_non_contiguous`, `tests/ops/test_group_norm.py::test_group_norm_op` (OK) | OK |
| group_norm | bench | `benchmarks/ops/bench_group_norm.py::bench_group_norm` | `benchmarks/ops/bench_group_norm.py::bench_group_norm` (OK) | OK |

### Sub-category: instance_norm

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| instance_norm | kernel | `tileops/kernels/norm/instance_norm/__init__.py` | `tileops/kernels/norm/instance_norm/__init__.py` (OK) | OK |
| instance_norm | op | `tileops/ops/norm/instance_norm.py` | `tileops/ops/norm/instance_norm.py` (OK) | OK |
| instance_norm | test | `tests/ops/test_instance_norm.py::test_instance_norm_non_contiguous`, `tests/ops/test_instance_norm.py::test_instance_norm_op` | `tests/ops/test_instance_norm.py::test_instance_norm_non_contiguous`, `tests/ops/test_instance_norm.py::test_instance_norm_op` (OK) | OK |
| instance_norm | bench | `benchmarks/ops/bench_instance_norm.py::bench_instance_norm` | `benchmarks/ops/bench_instance_norm.py::bench_instance_norm` (OK) | OK |

### Sub-category: rms_norm

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| rms_norm | kernel | `tileops/kernels/norm/rms_norm.py` | `tileops/kernels/norm/rms_norm.py` (OK) | OK |
| rms_norm | op | `tileops/ops/norm/rms_norm.py` | `tileops/ops/norm/rms_norm.py` (OK) | OK |
| rms_norm | test | `tests/ops/test_rms_norm.py::test_rms_norm_3d`, `tests/ops/test_rms_norm.py::test_rms_norm_op` | `tests/ops/test_rms_norm.py::test_rms_norm_3d`, `tests/ops/test_rms_norm.py::test_rms_norm_op` (OK) | OK |
| rms_norm | bench | `benchmarks/ops/bench_rms_norm.py::bench_rms_norm` | `benchmarks/ops/bench_rms_norm.py::bench_rms_norm` (OK) | OK |

### Sub-category: qk_norm

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| qk_norm | kernel | `tileops/kernels/norm/qk_norm/__init__.py` | `tileops/kernels/norm/qk_norm/__init__.py` (OK) | OK |
| qk_norm | op | - | - | N/A |
| qk_norm | test | - | - | N/A |
| qk_norm | bench | - | - | N/A |

### Sub-category: ada_layer_norm

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| ada_layer_norm | kernel | `tileops/kernels/norm/ada_layer_norm/fwd.py` | `tileops/kernels/norm/ada_layer_norm/fwd.py` (OK) | OK |
| ada_layer_norm | op | `tileops/ops/norm/ada_layer_norm.py` | `tileops/ops/norm/ada_layer_norm.py` (OK) | OK |
| ada_layer_norm | test | `tests/ops/test_ada_layer_norm.py::test_ada_layer_norm_3d`, `tests/ops/test_ada_layer_norm.py::test_ada_layer_norm_op` | `tests/ops/test_ada_layer_norm.py::test_ada_layer_norm_3d`, `tests/ops/test_ada_layer_norm.py::test_ada_layer_norm_op` (OK) | OK |
| ada_layer_norm | bench | `benchmarks/ops/bench_ada_layer_norm.py::bench_ada_layer_norm` | `benchmarks/ops/bench_ada_layer_norm.py::bench_ada_layer_norm` (OK) | OK |

### Sub-category: ada_layer_norm_zero

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| ada_layer_norm_zero | kernel | `tileops/kernels/norm/ada_layer_norm_zero/__init__.py` | `tileops/kernels/norm/ada_layer_norm_zero/__init__.py` (OK) | OK |
| ada_layer_norm_zero | op | `tileops/ops/norm/ada_layer_norm_zero.py` | `tileops/ops/norm/ada_layer_norm_zero.py` (OK) | OK |
| ada_layer_norm_zero | test | `tests/ops/test_ada_layer_norm_zero.py::test_ada_layer_norm_zero_3d`, `tests/ops/test_ada_layer_norm_zero.py::test_ada_layer_norm_zero_op` | `tests/ops/test_ada_layer_norm_zero.py::test_ada_layer_norm_zero_3d`, `tests/ops/test_ada_layer_norm_zero.py::test_ada_layer_norm_zero_op` (OK) | OK |
| ada_layer_norm_zero | bench | `benchmarks/ops/bench_ada_layer_norm.py::bench_ada_layer_norm_zero` | `benchmarks/ops/bench_ada_layer_norm_zero.py::bench_ada_layer_norm_zero` | RENAME |

### Sub-category: fused_add_norm

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| fused_add_layer_norm | kernel | `tileops/kernels/norm/fused_add_norm/fwd.py` | `tileops/kernels/norm/fused_add_norm/fwd.py` (OK) | OK |
| fused_add_layer_norm | op | `tileops/ops/norm/fused_add_layer_norm.py` | `tileops/ops/norm/fused_add_layer_norm.py` (OK) | OK |
| fused_add_layer_norm | test | `tests/ops/test_fused_add_layer_norm.py::test_fused_add_layer_norm_3d`, `tests/ops/test_fused_add_layer_norm.py::test_fused_add_layer_norm_op` | `tests/ops/test_fused_add_layer_norm.py::test_fused_add_layer_norm_3d`, `tests/ops/test_fused_add_layer_norm.py::test_fused_add_layer_norm_op` (OK) | OK |
| fused_add_layer_norm | bench | `benchmarks/ops/bench_fused_add_layer_norm.py::bench_fused_add_layer_norm` | `benchmarks/ops/bench_fused_add_layer_norm.py::bench_fused_add_layer_norm` (OK) | OK |
| fused_add_rmsnorm | kernel | `tileops/kernels/norm/fused_add_norm/fwd.py` | `tileops/kernels/norm/fused_add_norm/fwd.py` (OK) | OK |
| fused_add_rmsnorm | op | `tileops/ops/norm/fused_add_rmsnorm.py` | `tileops/ops/norm/fused_add_rmsnorm.py` (OK) | OK |
| fused_add_rmsnorm | test | `tests/ops/test_fused_add_rmsnorm.py::test_fused_add_rmsnorm_3d`, `tests/ops/test_fused_add_rmsnorm.py::test_fused_add_rmsnorm_op` | `tests/ops/test_fused_add_rmsnorm.py::test_fused_add_rmsnorm_3d`, `tests/ops/test_fused_add_rmsnorm.py::test_fused_add_rmsnorm_op` (OK) | OK |
| fused_add_rmsnorm | bench | `benchmarks/ops/bench_fused_add_layer_norm.py::bench_fused_add_rmsnorm` | `benchmarks/ops/bench_fused_add_norm.py::bench_fused_add_rmsnorm` | RENAME |

---

## Category: Conv & Pooling (#402)

### Sub-category: conv

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| conv1d | kernel | `-` | `-` | N/A |
| conv1d | op | `-` | `-` | N/A |
| conv1d | test | `-` | `-` | N/A |
| conv1d | bench | `-` | `-` | N/A |
| conv2d | kernel | `-` | `-` | N/A |
| conv2d | op | `-` | `-` | N/A |
| conv2d | test | `-` | `-` | N/A |
| conv2d | bench | `-` | `-` | N/A |
| conv3d | kernel | `-` | `-` | N/A |
| conv3d | op | `-` | `-` | N/A |
| conv3d | test | `-` | `-` | N/A |
| conv3d | bench | `-` | `-` | N/A |

### Sub-category: conv_transpose

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| conv_transpose1d | kernel | `-` | `-` | N/A |
| conv_transpose1d | op | `-` | `-` | N/A |
| conv_transpose1d | test | `-` | `-` | N/A |
| conv_transpose1d | bench | `-` | `-` | N/A |
| conv_transpose2d | kernel | `-` | `-` | N/A |
| conv_transpose2d | op | `-` | `-` | N/A |
| conv_transpose2d | test | `-` | `-` | N/A |
| conv_transpose2d | bench | `-` | `-` | N/A |

### Sub-category: depthwise

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| depthwise_conv2d | kernel | `-` | `-` | N/A |
| depthwise_conv2d | op | `-` | `-` | N/A |
| depthwise_conv2d | test | `-` | `-` | N/A |
| depthwise_conv2d | bench | `-` | `-` | N/A |

### Sub-category: grouped

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| grouped_conv2d | kernel | `-` | `-` | N/A |
| grouped_conv2d | op | `-` | `-` | N/A |
| grouped_conv2d | test | `-` | `-` | N/A |
| grouped_conv2d | bench | `-` | `-` | N/A |

### Sub-category: dilated

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| dilated_conv2d | kernel | `-` | `-` | N/A |
| dilated_conv2d | op | `-` | `-` | N/A |
| dilated_conv2d | test | `-` | `-` | N/A |
| dilated_conv2d | bench | `-` | `-` | N/A |

### Sub-category: max_pool

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| max_pool1d | kernel | `-` | `-` | N/A |
| max_pool1d | op | `-` | `-` | N/A |
| max_pool1d | test | `-` | `-` | N/A |
| max_pool1d | bench | `-` | `-` | N/A |
| max_pool2d | kernel | `-` | `-` | N/A |
| max_pool2d | op | `-` | `-` | N/A |
| max_pool2d | test | `-` | `-` | N/A |
| max_pool2d | bench | `-` | `-` | N/A |
| max_pool3d | kernel | `-` | `-` | N/A |
| max_pool3d | op | `-` | `-` | N/A |
| max_pool3d | test | `-` | `-` | N/A |
| max_pool3d | bench | `-` | `-` | N/A |

### Sub-category: avg_pool

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| avg_pool1d | kernel | `-` | `-` | N/A |
| avg_pool1d | op | `-` | `-` | N/A |
| avg_pool1d | test | `-` | `-` | N/A |
| avg_pool1d | bench | `-` | `-` | N/A |
| avg_pool2d | kernel | `-` | `-` | N/A |
| avg_pool2d | op | `-` | `-` | N/A |
| avg_pool2d | test | `-` | `-` | N/A |
| avg_pool2d | bench | `-` | `-` | N/A |
| avg_pool3d | kernel | `-` | `-` | N/A |
| avg_pool3d | op | `-` | `-` | N/A |
| avg_pool3d | test | `-` | `-` | N/A |
| avg_pool3d | bench | `-` | `-` | N/A |

### Sub-category: adaptive_pool

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| adaptive_avg_pool2d | kernel | `-` | `-` | N/A |
| adaptive_avg_pool2d | op | `-` | `-` | N/A |
| adaptive_avg_pool2d | test | `-` | `-` | N/A |
| adaptive_avg_pool2d | bench | `-` | `-` | N/A |
| adaptive_max_pool2d | kernel | `-` | `-` | N/A |
| adaptive_max_pool2d | op | `-` | `-` | N/A |
| adaptive_max_pool2d | test | `-` | `-` | N/A |
| adaptive_max_pool2d | bench | `-` | `-` | N/A |

---

## Category: GEMM (#400)

### Sub-category: gemm

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| gemm_fp16 | kernel | `tileops/kernels/gemm/gemm.py` | `tileops/kernels/gemm/gemm.py` (OK) | OK |
| gemm_fp16 | op | `tileops/ops/gemm.py` | `tileops/ops/gemm.py` (OK) | OK |
| gemm_fp16 | test | `tests/ops/test_gemm.py::test_gemm` | `tests/ops/test_gemm.py::test_gemm_fp16` | RENAME |
| gemm_fp16 | bench | `benchmarks/ops/bench_gemm.py::bench_gemm` | `benchmarks/ops/bench_gemm.py::bench_gemm_fp16` | RENAME |
| gemm_fp8 | kernel | `tileops/kernels/gemm/gemm.py` | `tileops/kernels/gemm/gemm.py` (OK) | OK |
| gemm_fp8 | op | `tileops/ops/gemm.py` | `tileops/ops/gemm.py` (OK) | OK |
| gemm_fp8 | test | - | - | N/A |
| gemm_fp8 | bench | `benchmarks/ops/bench_gemm.py::bench_gemm_fp8` | `benchmarks/ops/bench_gemm.py::bench_gemm_fp8` (OK) | OK |
| gemm_fp8_block_scaled | kernel | `tileops/kernels/gemm/gemm.py` | `tileops/kernels/gemm/gemm.py` (OK) | OK |
| gemm_fp8_block_scaled | op | `tileops/ops/gemm.py` | `tileops/ops/gemm.py` (OK) | OK |
| gemm_fp8_block_scaled | test | - | - | N/A |
| gemm_fp8_block_scaled | bench | `benchmarks/ops/bench_gemm.py::bench_gemm_fp8_block_scaled` | `benchmarks/ops/bench_gemm.py::bench_gemm_fp8_block_scaled` (OK) | OK |
| gemv_fp16 | kernel | `tileops/kernels/gemm/gemv.py` | `tileops/kernels/gemm/gemv.py` (OK) | OK |
| gemv_fp16 | op | `tileops/ops/gemm.py` | `tileops/ops/gemm.py` (OK) | OK |
| gemv_fp16 | test | `tests/ops/test_gemm.py::test_gemv_boundary_lhs_row`, `tests/ops/test_gemm.py::test_gemv_boundary_rhs_col` | `tests/ops/test_gemm.py::test_gemv_fp16` | RENAME |
| gemv_fp16 | bench | `benchmarks/ops/bench_gemm.py::bench_gemv` | `benchmarks/ops/bench_gemm.py::bench_gemv_fp16` | RENAME |
| gemv_fp8 | kernel | `tileops/kernels/gemm/gemv.py` | `tileops/kernels/gemm/gemv.py` (OK) | OK |
| gemv_fp8 | op | `tileops/ops/gemm.py` | `tileops/ops/gemm.py` (OK) | OK |
| gemv_fp8 | test | - | - | N/A |
| gemv_fp8 | bench | `benchmarks/ops/bench_gemm.py::bench_gemv_fp8` | `benchmarks/ops/bench_gemm.py::bench_gemv_fp8` (OK) | OK |
| small_batch_gemm_fp16 | kernel | `tileops/kernels/gemm/gemm.py` | `tileops/kernels/gemm/gemm.py` (OK) | OK |
| small_batch_gemm_fp16 | op | `tileops/ops/gemm.py` | `tileops/ops/gemm.py` (OK) | OK |
| small_batch_gemm_fp16 | test | - | - | N/A |
| small_batch_gemm_fp16 | bench | `benchmarks/ops/bench_gemm.py::bench_small_batch_gemm` | `benchmarks/ops/bench_gemm.py::bench_small_batch_gemm_fp16` | RENAME |
| small_batch_gemm_fp8 | kernel | `tileops/kernels/gemm/gemm.py` | `tileops/kernels/gemm/gemm.py` (OK) | OK |
| small_batch_gemm_fp8 | op | `tileops/ops/gemm.py` | `tileops/ops/gemm.py` (OK) | OK |
| small_batch_gemm_fp8 | test | - | - | N/A |
| small_batch_gemm_fp8 | bench | `benchmarks/ops/bench_gemm.py::bench_small_batch_gemm_fp8` | `benchmarks/ops/bench_gemm.py::bench_small_batch_gemm_fp8` (OK) | OK |

### Sub-category: bmm

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| bmm_fp16 | kernel | `tileops/kernels/gemm/gemm.py` | `tileops/kernels/gemm/bmm.py` | RENAME |
| bmm_fp16 | op | - | - | N/A |
| bmm_fp16 | test | - | - | N/A |
| bmm_fp16 | bench | `benchmarks/ops/bench_gemm.py::bench_bmm` | `benchmarks/ops/bench_bmm.py::bench_bmm_fp16` | RENAME |
| bmm_fp8 | kernel | `tileops/kernels/gemm/gemm.py` | `tileops/kernels/gemm/bmm.py` | RENAME |
| bmm_fp8 | op | - | - | N/A |
| bmm_fp8 | test | - | - | N/A |
| bmm_fp8 | bench | `benchmarks/ops/bench_gemm.py::bench_bmm_fp8` | `benchmarks/ops/bench_bmm.py::bench_bmm_fp8` | RENAME |

### Sub-category: groupgemm

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| groupgemm_fp16 | kernel | `tileops/kernels/grouped_gemm/grouped_gemm.py` | `tileops/kernels/gemm/groupgemm.py` | RENAME |
| groupgemm_fp16 | op | `tileops/ops/grouped_gemm.py` | `tileops/ops/gemm/groupgemm_fp16.py` | RENAME |
| groupgemm_fp16 | test | `tests/ops/test_grouped_gemm.py::test_grouped_gemm` | `tests/ops/test_groupgemm.py::test_groupgemm_fp16` | RENAME |
| groupgemm_fp16 | bench | `benchmarks/ops/bench_grouped_gemm.py::bench_grouped_gemm` | `benchmarks/ops/bench_groupgemm.py::bench_groupgemm_fp16` | RENAME |
| groupgemm_fp8 | kernel | `tileops/kernels/grouped_gemm/grouped_gemm.py` | `tileops/kernels/gemm/groupgemm.py` | RENAME |
| groupgemm_fp8 | op | `tileops/ops/grouped_gemm.py` | `tileops/ops/gemm/groupgemm_fp8.py` | RENAME |
| groupgemm_fp8 | test | - | - | N/A |
| groupgemm_fp8 | bench | `benchmarks/ops/bench_grouped_gemm.py::bench_grouped_gemm_fp8` | `benchmarks/ops/bench_groupgemm.py::bench_groupgemm_fp8` | RENAME |

### Sub-category: outer

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| outer | kernel | `-` | `-` | N/A |
| outer | op | `-` | `-` | N/A |
| outer | test | `-` | `-` | N/A |
| outer | bench | `-` | `-` | N/A |

### Sub-category: lowbit_gemm

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| w4a16 | kernel | `-` | `-` | N/A |
| w4a16 | op | `-` | `-` | N/A |
| w4a16 | test | `-` | `-` | N/A |
| w4a16 | bench | `-` | `-` | N/A |
| w8a8 | kernel | `-` | `-` | N/A |
| w8a8 | op | `-` | `-` | N/A |
| w8a8 | test | `-` | `-` | N/A |
| w8a8 | bench | `-` | `-` | N/A |
| w8a8_int8 | kernel | `-` | `-` | N/A |
| w8a8_int8 | op | `-` | `-` | N/A |
| w8a8_int8 | test | `-` | `-` | N/A |
| w8a8_int8 | bench | `-` | `-` | N/A |
| weight_only_int4 | kernel | `-` | `-` | N/A |
| weight_only_int4 | op | `-` | `-` | N/A |
| weight_only_int4 | test | `-` | `-` | N/A |
| weight_only_int4 | bench | `-` | `-` | N/A |
| fp4 | kernel | `-` | `-` | N/A |
| fp4 | op | `-` | `-` | N/A |
| fp4 | test | `-` | `-` | N/A |
| fp4 | bench | `-` | `-` | N/A |

### Sub-category: sparse_gemm_2_4

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| sparse_gemm_fp16 | kernel | `-` | `-` | N/A |
| sparse_gemm_fp16 | op | `-` | `-` | N/A |
| sparse_gemm_fp16 | test | `-` | `-` | N/A |
| sparse_gemm_fp16 | bench | `-` | `-` | N/A |
| sparse_gemm_fp8 | kernel | `-` | `-` | N/A |
| sparse_gemm_fp8 | op | `-` | `-` | N/A |
| sparse_gemm_fp8 | test | `-` | `-` | N/A |
| sparse_gemm_fp8 | bench | `-` | `-` | N/A |

---

## Category: Quantize (#401)

### Sub-category: int8_quantize

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| int8_per_tensor | kernel | `-` | `-` | N/A |
| int8_per_tensor | op | `-` | `-` | N/A |
| int8_per_tensor | test | `-` | `-` | N/A |
| int8_per_tensor | bench | `-` | `-` | N/A |
| int8_per_channel | kernel | `-` | `-` | N/A |
| int8_per_channel | op | `-` | `-` | N/A |
| int8_per_channel | test | `-` | `-` | N/A |
| int8_per_channel | bench | `-` | `-` | N/A |
| int8_per_block | kernel | `-` | `-` | N/A |
| int8_per_block | op | `-` | `-` | N/A |
| int8_per_block | test | `-` | `-` | N/A |
| int8_per_block | bench | `-` | `-` | N/A |
| smooth_quant | kernel | `-` | `-` | N/A |
| smooth_quant | op | `-` | `-` | N/A |
| smooth_quant | test | `-` | `-` | N/A |
| smooth_quant | bench | `-` | `-` | N/A |

### Sub-category: int4_quantize

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| int4_per_channel | kernel | `-` | `-` | N/A |
| int4_per_channel | op | `-` | `-` | N/A |
| int4_per_channel | test | `-` | `-` | N/A |
| int4_per_channel | bench | `-` | `-` | N/A |
| int4_per_block | kernel | `-` | `-` | N/A |
| int4_per_block | op | `-` | `-` | N/A |
| int4_per_block | test | `-` | `-` | N/A |
| int4_per_block | bench | `-` | `-` | N/A |
| nf4 | kernel | `-` | `-` | N/A |
| nf4 | op | `-` | `-` | N/A |
| nf4 | test | `-` | `-` | N/A |
| nf4 | bench | `-` | `-` | N/A |

### Sub-category: fp8_quantize

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| fp8_per_tensor | kernel | `tileops/kernels/deepseek_mla/fp8_quant.py` | `tileops/kernels/quantize/fp8_quantize.py` | RENAME |
| fp8_per_tensor | op | `tileops/ops/fp8_quant.py` | `tileops/ops/quantize/fp8_per_tensor.py` | RENAME |
| fp8_per_tensor | test | `tests/ops/test_fp8_quant.py::test_fp8_quant_op` | `tests/ops/test_fp8_quantize.py::test_fp8_per_tensor` | RENAME |
| fp8_per_tensor | bench | `benchmarks/ops/bench_fp8_quant.py::bench_fp8_quant` | `benchmarks/ops/bench_fp8_quantize.py::bench_fp8_per_tensor` | RENAME |
| fp8_per_block | kernel | `tileops/kernels/deepseek_mla/fp8_quant.py` | `tileops/kernels/quantize/fp8_quantize.py` | RENAME |
| fp8_per_block | op | - | - | N/A |
| fp8_per_block | test | - | - | N/A |
| fp8_per_block | bench | `benchmarks/ops/bench_fp8_quant.py::bench_fp8_block_quant` | `benchmarks/ops/bench_fp8_quantize.py::bench_fp8_per_block` | RENAME |
| fp8_cast_transpose | kernel | `-` | `-` | N/A |
| fp8_cast_transpose | op | `-` | `-` | N/A |
| fp8_cast_transpose | test | `-` | `-` | N/A |
| fp8_cast_transpose | bench | `-` | `-` | N/A |

---

## Category: Sampling (#426)

### Sub-category: top_k

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| top_k | kernel | `-` | `-` | N/A |
| top_k | op | `-` | `-` | N/A |
| top_k | test | `-` | `-` | N/A |
| top_k | bench | `-` | `-` | N/A |

### Sub-category: top_p

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| top_p | kernel | `-` | `-` | N/A |
| top_p | op | `-` | `-` | N/A |
| top_p | test | `-` | `-` | N/A |
| top_p | bench | `-` | `-` | N/A |

### Sub-category: min_p

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| min_p | kernel | `-` | `-` | N/A |
| min_p | op | `-` | `-` | N/A |
| min_p | test | `-` | `-` | N/A |
| min_p | bench | `-` | `-` | N/A |

### Sub-category: top_k_top_p

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| top_k_top_p | kernel | `-` | `-` | N/A |
| top_k_top_p | op | `-` | `-` | N/A |
| top_k_top_p | test | `-` | `-` | N/A |
| top_k_top_p | bench | `-` | `-` | N/A |

### Sub-category: temperature_scale

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| temperature_scale | kernel | `-` | `-` | N/A |
| temperature_scale | op | `-` | `-` | N/A |
| temperature_scale | test | `-` | `-` | N/A |
| temperature_scale | bench | `-` | `-` | N/A |

### Sub-category: sampling_from_probs

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| sampling_from_probs | kernel | `-` | `-` | N/A |
| sampling_from_probs | op | `-` | `-` | N/A |
| sampling_from_probs | test | `-` | `-` | N/A |
| sampling_from_probs | bench | `-` | `-` | N/A |

### Sub-category: chain_speculative_sampling

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| chain_speculative_sampling | kernel | `tileops/kernels/deepseek_mla/topk_selector.py` | `tileops/kernels/sampling/chain_speculative_sampling.py` | RENAME |
| chain_speculative_sampling | op | `tileops/ops/topk_selector.py` | `tileops/ops/sampling/chain_speculative_sampling.py` | RENAME |
| chain_speculative_sampling | test | `tests/ops/test_topk_selector.py::test_topk_selector_op` | `tests/ops/test_chain_speculative_sampling.py::test_chain_speculative_sampling` | RENAME |
| chain_speculative_sampling | bench | `benchmarks/ops/bench_topk_selector.py::bench_topk_selector` | `benchmarks/ops/bench_chain_speculative_sampling.py::bench_chain_speculative_sampling` | RENAME |

---

## Category: Flash Attention (#403)

### Sub-category: flash_attention

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| flash_prefill_fwd | kernel | `tileops/kernels/flash_attn/fwd.py` | `tileops/kernels/flash_attn/flash_attention.py` | RENAME |
| flash_prefill_fwd | op | `tileops/ops/gqa.py`, `tileops/ops/mha.py` | `tileops/ops/flash_attn/flash_prefill_fwd.py` | RENAME |
| flash_prefill_fwd | test | `tests/ops/test_gqa.py::test_gqa_fwd`, `tests/ops/test_mha.py::test_mha_fwd` | `tests/ops/test_flash_attention.py::test_flash_prefill_fwd` | RENAME |
| flash_prefill_fwd | bench | `benchmarks/ops/bench_gqa.py::bench_gqa_fwd`, `benchmarks/ops/bench_mha.py::bench_mha_fwd` | `benchmarks/ops/bench_flash_attention.py::bench_flash_prefill_fwd` | RENAME |
| flash_prefill_bwd | kernel | `tileops/kernels/flash_attn/bwd.py` | `tileops/kernels/flash_attn/flash_attention.py` | RENAME |
| flash_prefill_bwd | op | `tileops/ops/gqa.py`, `tileops/ops/mha.py` | `tileops/ops/flash_attn/flash_prefill_bwd.py` | RENAME |
| flash_prefill_bwd | test | `tests/ops/test_gqa.py::test_gqa_bwd`, `tests/ops/test_mha.py::test_mha_bwd` | `tests/ops/test_flash_attention.py::test_flash_prefill_bwd` | RENAME |
| flash_prefill_bwd | bench | `benchmarks/ops/bench_gqa.py::bench_gqa_bwd`, `benchmarks/ops/bench_mha.py::bench_mha_bwd` | `benchmarks/ops/bench_flash_attention.py::bench_flash_prefill_bwd` | RENAME |
| flash_prefill_varlen_fwd | kernel | `tileops/kernels/deepseek_nsa/gqa_sliding_window_varlen_fwd.py` | `tileops/kernels/flash_attn/flash_attention.py` | RENAME |
| flash_prefill_varlen_fwd | op | `tileops/ops/gqa_sliding_window_varlen_fwd.py` | `tileops/ops/flash_attn/flash_prefill_varlen_fwd.py` | RENAME |
| flash_prefill_varlen_fwd | test | `tests/ops/test_gqa_sliding_window_varlen_fwd.py::test_gqa_sliding_window_varlen_fwd_op` | `tests/ops/test_flash_attention.py::test_flash_prefill_varlen_fwd` | RENAME |
| flash_prefill_varlen_fwd | bench | `benchmarks/ops/bench_gqa_sliding_window_varlen_fwd.py::bench_gqa_sliding_window_varlen_fwd` | `benchmarks/ops/bench_flash_attention.py::bench_flash_prefill_varlen_fwd` | RENAME |
| flash_prefill_varlen_bwd | kernel | `-` | `-` | N/A |
| flash_prefill_varlen_bwd | op | `-` | `-` | N/A |
| flash_prefill_varlen_bwd | test | `-` | `-` | N/A |
| flash_prefill_varlen_bwd | bench | `-` | `-` | N/A |
| flash_decode_fwd | kernel | `tileops/kernels/flash_decode/gqa_decode.py`, `tileops/kernels/flash_decode/mha_decode.py` | `tileops/kernels/flash_attn/flash_attention.py` | RENAME |
| flash_decode_fwd | op | `tileops/ops/gqa_decode.py`, `tileops/ops/mha_decode.py` | `tileops/ops/flash_attn/flash_decode_fwd.py` | RENAME |
| flash_decode_fwd | test | `tests/ops/test_gqa_decode.py::test_gqa_decode`, `tests/ops/test_mha_decode.py::test_mha_decode` | `tests/ops/test_flash_attention.py::test_flash_decode_fwd` | RENAME |
| flash_decode_fwd | bench | `benchmarks/ops/bench_gqa_decode.py::bench_gqa_decode`, `benchmarks/ops/bench_mha_decode.py::bench_mha_decode` | `benchmarks/ops/bench_flash_attention.py::bench_flash_decode_fwd` | RENAME |
| flash_decode_paged_fwd | kernel | `tileops/kernels/flash_decode/gqa_decode_paged.py`, `tileops/kernels/flash_decode/mha_decode_paged.py` | `tileops/kernels/flash_attn/flash_attention.py` | RENAME |
| flash_decode_paged_fwd | op | `tileops/ops/gqa_decode_paged.py`, `tileops/ops/mha_decode_paged.py` | `tileops/ops/flash_attn/flash_decode_paged_fwd.py` | RENAME |
| flash_decode_paged_fwd | test | `tests/ops/test_gqa_decode_paged.py::test_gqa_decode_paged_op`, `tests/ops/test_mha_decode_paged.py::test_mha_decode_paged_op` | `tests/ops/test_flash_attention.py::test_flash_decode_paged_fwd` | RENAME |
| flash_decode_paged_fwd | bench | `benchmarks/ops/bench_gqa_decode_paged.py::bench_gqa_decode_paged`, `benchmarks/ops/bench_mha_decode_paged.py::bench_mha_decode_paged` | `benchmarks/ops/bench_flash_attention.py::bench_flash_decode_paged_fwd` | RENAME |
| flash_decode_varlen_fwd | kernel | `-` | `-` | N/A |
| flash_decode_varlen_fwd | op | `-` | `-` | N/A |
| flash_decode_varlen_fwd | test | `-` | `-` | N/A |
| flash_decode_varlen_fwd | bench | `-` | `-` | N/A |
| flash_chunked_prefill_fwd | kernel | `-` | `-` | N/A |
| flash_chunked_prefill_fwd | op | `-` | `-` | N/A |
| flash_chunked_prefill_fwd | test | `-` | `-` | N/A |
| flash_chunked_prefill_fwd | bench | `-` | `-` | N/A |

### Sub-category: mla

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| mla_prefill_fwd | kernel | `-` | `-` | N/A |
| mla_prefill_fwd | op | `-` | `-` | N/A |
| mla_prefill_fwd | test | `-` | `-` | N/A |
| mla_prefill_fwd | bench | `-` | `-` | N/A |
| mla_prefill_bwd | kernel | `-` | `-` | N/A |
| mla_prefill_bwd | op | `-` | `-` | N/A |
| mla_prefill_bwd | test | `-` | `-` | N/A |
| mla_prefill_bwd | bench | `-` | `-` | N/A |
| mla_decode_fwd | kernel | `tileops/kernels/deepseek_mla/deepseek_mla_decode.py` | `tileops/kernels/deepseek_mla/deepseek_mla_decode.py` (OK) | OK |
| mla_decode_fwd | op | `tileops/ops/deepseek_mla_decode.py` | `tileops/ops/deepseek_mla_decode.py` (OK) | OK |
| mla_decode_fwd | test | `tests/ops/test_deepseek_mla_decode.py::test_mla_decode` | `tests/ops/test_mla.py::test_mla_decode_fwd` | RENAME |
| mla_decode_fwd | bench | `benchmarks/ops/bench_deepseek_mla_decode.py::bench_mla_decode` | `benchmarks/ops/bench_mla.py::bench_mla_decode_fwd` | RENAME |
| mla_decode_paged_fwd | kernel | `-` | `-` | N/A |
| mla_decode_paged_fwd | op | `-` | `-` | N/A |
| mla_decode_paged_fwd | test | `-` | `-` | N/A |
| mla_decode_paged_fwd | bench | `-` | `-` | N/A |

### Sub-category: nsa

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| nsa_prefill_fwd | kernel | `tileops/kernels/deepseek_nsa/nsa_fwd.py`, `tileops/kernels/deepseek_nsa/nsa_cmp_fwd.py` | `tileops/kernels/deepseek_nsa/nsa_fwd.py`, `tileops/kernels/deepseek_nsa/nsa_cmp_fwd.py` (OK) | OK |
| nsa_prefill_fwd | op | `tileops/ops/deepseek_nsa.py` | `tileops/ops/deepseek_nsa.py` (OK) | OK |
| nsa_prefill_fwd | test | `tests/ops/test_deepseek_nsa_fwd.py::test_nsa_varlen_op`, `tests/ops/test_deepseek_nsa_cmp_fwd.py::test_nsa_cmp_fwd_varlen_op` | `tests/ops/test_nsa.py::test_nsa_prefill_fwd` | RENAME |
| nsa_prefill_fwd | bench | `benchmarks/ops/bench_deepseek_nsa_fwd.py::bench_nsa_fwd`, `benchmarks/ops/bench_deepseek_nsa_cmp_fwd.py::bench_nsa_cmp_fwd` | `benchmarks/ops/bench_nsa.py::bench_nsa_prefill_fwd` | RENAME |
| nsa_decode_fwd | kernel | `-` | `-` | N/A |
| nsa_decode_fwd | op | `-` | `-` | N/A |
| nsa_decode_fwd | test | `-` | `-` | N/A |
| nsa_decode_fwd | bench | `-` | `-` | N/A |

### Sub-category: dsa

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| dsa_prefill_fwd | kernel | `-` | `-` | N/A |
| dsa_prefill_fwd | op | `-` | `-` | N/A |
| dsa_prefill_fwd | test | `-` | `-` | N/A |
| dsa_prefill_fwd | bench | `-` | `-` | N/A |
| dsa_decode_fwd | kernel | `tileops/kernels/deepseek_mla/deepseek_dsa_decode.py` | `tileops/kernels/deepseek_mla/deepseek_dsa_decode.py` (OK) | OK |
| dsa_decode_fwd | op | `tileops/ops/deepseek_dsa_decode.py` | `tileops/ops/deepseek_dsa_decode.py` (OK) | OK |
| dsa_decode_fwd | test | `tests/ops/test_deepseek_dsa_decode.py::test_sparse_mla_decode` | `tests/ops/test_dsa.py::test_dsa_decode_fwd` | RENAME |
| dsa_decode_fwd | bench | `benchmarks/ops/bench_deepseek_dsa_decode.py::bench_dsa_decode` | `benchmarks/ops/bench_dsa.py::bench_dsa_decode_fwd` | RENAME |

---

## Category: MoE (#404)

### Sub-category: permute_align

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| permute_align | kernel | `tileops/kernels/moe/permute_align.py` | `tileops/kernels/moe/permute_align.py` (OK) | OK |
| permute_align | op | - | - | N/A |
| permute_align | test | `tests/ops/test_moe_permute_align.py::test_permute_align_op` | `tests/ops/test_moe_permute_align.py::test_permute_align_op` (OK) | OK |
| permute_align | bench | `benchmarks/ops/bench_moe_permute_align.py::bench_permute_align` | `benchmarks/ops/bench_moe_permute_align.py::bench_permute_align` (OK) | OK |

### Sub-category: unpermute_depad

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| unpermute_depad | kernel | `-` | `-` | N/A |
| unpermute_depad | op | `-` | `-` | N/A |
| unpermute_depad | test | `-` | `-` | N/A |
| unpermute_depad | bench | `-` | `-` | N/A |

### Sub-category: fused_moe

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| fused_moe_deepseek | kernel | `-` | `-` | N/A |
| fused_moe_deepseek | op | `-` | `-` | N/A |
| fused_moe_deepseek | test | `-` | `-` | N/A |
| fused_moe_deepseek | bench | `-` | `-` | N/A |
| fused_moe_glm | kernel | `-` | `-` | N/A |
| fused_moe_glm | op | `-` | `-` | N/A |
| fused_moe_glm | test | `-` | `-` | N/A |
| fused_moe_glm | bench | `-` | `-` | N/A |
| fused_moe_kimi | kernel | `-` | `-` | N/A |
| fused_moe_kimi | op | `-` | `-` | N/A |
| fused_moe_kimi | test | `-` | `-` | N/A |
| fused_moe_kimi | bench | `-` | `-` | N/A |
| fused_moe_qwen | kernel | `-` | `-` | N/A |
| fused_moe_qwen | op | `-` | `-` | N/A |
| fused_moe_qwen | test | `-` | `-` | N/A |
| fused_moe_qwen | bench | `-` | `-` | N/A |

---

## Category: Linear Attention (#405)

### Sub-category: gated_deltanet

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| gated_deltanet_chunkwise | kernel | `tileops/kernels/linear_attn/gated_delta_net/gated_deltanet_fwd.py`, `tileops/kernels/linear_attn/gated_delta_net/gated_deltanet_bwd.py`, `tileops/kernels/linear_attn/gated_delta_net/fused_prepare_compute_w_u.py`, `tileops/kernels/linear_attn/gated_delta_net/compute_w_u_bwd.py` | `tileops/kernels/linear_attn/gated_delta_net/gated_deltanet_fwd.py`, `tileops/kernels/linear_attn/gated_delta_net/gated_deltanet_bwd.py`, `tileops/kernels/linear_attn/gated_delta_net/fused_prepare_compute_w_u.py`, `tileops/kernels/linear_attn/gated_delta_net/compute_w_u_bwd.py` (OK) | OK |
| gated_deltanet_chunkwise | op | `tileops/ops/gated_deltanet.py` | `tileops/ops/gated_deltanet.py` (OK) | OK |
| gated_deltanet_chunkwise | test | `tests/ops/test_gated_deltanet_fwd.py::test_gated_deltanet_fwd`, `tests/ops/test_gated_deltanet_bwd.py::test_gated_deltanet_bwd`, `tests/ops/test_fused_gated.py::test_fused_gated` | `tests/ops/test_gated_deltanet.py::test_gated_deltanet_chunkwise` | RENAME |
| gated_deltanet_chunkwise | bench | `benchmarks/ops/bench_gated_deltanet_vs_fla.py::bench_gated_deltanet_fwd`, `benchmarks/ops/bench_gated_deltanet_vs_fla.py::bench_gated_deltanet_bwd` | `benchmarks/ops/bench_gated_deltanet.py::bench_gated_deltanet_chunkwise` | RENAME |
| gated_deltanet_recurrence | kernel | `tileops/kernels/linear_attn/gated_delta_net/gated_deltanet_decode.py` | `tileops/kernels/linear_attn/gated_delta_net/gated_deltanet_decode.py` (OK) | OK |
| gated_deltanet_recurrence | op | `tileops/ops/gated_deltanet_decode.py` | `tileops/ops/gated_deltanet_decode.py` (OK) | OK |
| gated_deltanet_recurrence | test | `tests/ops/test_gated_deltanet_decode.py::test_gated_deltanet_decode`, `tests/ops/test_gated_deltanet_decode.py::test_gated_deltanet_decode_multi_step` | `tests/ops/test_gated_deltanet.py::test_gated_deltanet_recurrence` | RENAME |
| gated_deltanet_recurrence | bench | `benchmarks/ops/bench_gated_deltanet_decode.py::bench_gated_deltanet_decode` | `benchmarks/ops/bench_gated_deltanet.py::bench_gated_deltanet_recurrence` | RENAME |

### Sub-category: deltanet

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| deltanet_chunkwise | kernel | `-` | `-` | N/A |
| deltanet_chunkwise | op | `-` | `-` | N/A |
| deltanet_chunkwise | test | `-` | `-` | N/A |
| deltanet_chunkwise | bench | `-` | `-` | N/A |
| deltanet_recurrence | kernel | `-` | `-` | N/A |
| deltanet_recurrence | op | `-` | `-` | N/A |
| deltanet_recurrence | test | `-` | `-` | N/A |
| deltanet_recurrence | bench | `-` | `-` | N/A |

### Sub-category: gla

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| gla_chunkwise | kernel | `tileops/kernels/linear_attn/gla/gla_fwd.py`, `tileops/kernels/linear_attn/gla/gla_bwd.py` | `tileops/kernels/linear_attn/gla/gla_fwd.py`, `tileops/kernels/linear_attn/gla/gla_bwd.py` (OK) | OK |
| gla_chunkwise | op | - | - | N/A |
| gla_chunkwise | test | `tests/ops/test_gla_fwd.py::test_gla_fwd`, `tests/ops/test_gla_bwd.py::test_gla_bwd` | `tests/ops/test_gla.py::test_gla_chunkwise` | RENAME |
| gla_chunkwise | bench | `benchmarks/ops/bench_gla.py::bench_gla_fwd`, `benchmarks/ops/bench_gla.py::bench_gla_bwd` | `benchmarks/ops/bench_gla.py::bench_gla_chunkwise` | RENAME |
| gla_recurrence | kernel | `tileops/kernels/linear_attn/gla/gla_decode.py` | `tileops/kernels/linear_attn/gla/gla_decode.py` (OK) | OK |
| gla_recurrence | op | - | - | N/A |
| gla_recurrence | test | `tests/ops/test_gla_decode.py::test_gla_decode` | `tests/ops/test_gla.py::test_gla_recurrence` | RENAME |
| gla_recurrence | bench | `benchmarks/ops/bench_gla_decode.py::bench_gla_decode` | `benchmarks/ops/bench_gla.py::bench_gla_recurrence` | RENAME |

### Sub-category: retnet

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| retnet_chunkwise | kernel | `-` | `-` | N/A |
| retnet_chunkwise | op | `-` | `-` | N/A |
| retnet_chunkwise | test | `-` | `-` | N/A |
| retnet_chunkwise | bench | `-` | `-` | N/A |
| retnet_recurrence | kernel | `-` | `-` | N/A |
| retnet_recurrence | op | `-` | `-` | N/A |
| retnet_recurrence | test | `-` | `-` | N/A |
| retnet_recurrence | bench | `-` | `-` | N/A |

---

## Category: SSM (#406)

### Sub-category: mamba1

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| mamba1 | kernel | `-` | `-` | N/A |
| mamba1 | op | `-` | `-` | N/A |
| mamba1 | test | `-` | `-` | N/A |
| mamba1 | bench | `-` | `-` | N/A |

### Sub-category: mamba2

| Op | File Type | Current Path | Proposed Path | Status |
|:---|:----------|:-------------|:--------------|:------:|
| mamba2 | kernel | `-` | `-` | N/A |
| mamba2 | op | `-` | `-` | N/A |
| mamba2 | test | `-` | `-` | N/A |
| mamba2 | bench | `-` | `-` | N/A |

---

## Summary

| Category | Issue | OK | RENAME | N/A | Total Entries |
|:---------|:------|---:|-------:|----:|--------------:|
| Elementwise | #397 | 96 | 164 | 28 | 288 |
| Reduce | #398 | 3 | 9 | 68 | 80 |
| Norm | #399 | 35 | 2 | 3 | 40 |
| Conv & Pooling | #402 | 0 | 0 | 64 | 64 |
| GEMM | #400 | 18 | 16 | 42 | 76 |
| Quantize | #401 | 0 | 6 | 34 | 40 |
| Sampling | #426 | 0 | 4 | 24 | 28 |
| Flash Attention | #403 | 6 | 26 | 32 | 64 |
| MoE | #404 | 3 | 0 | 21 | 24 |
| Linear Attention | #405 | 6 | 8 | 18 | 32 |
| SSM | #406 | 0 | 0 | 8 | 8 |
| **Total** | | **167** | **235** | **342** | **744** |

- **OK**: 167 entries (22.4%) -- naming is already discoverable
- **RENAME**: 235 entries (31.6%) -- need path/name adjustment
- **N/A**: 342 entries (46.0%) -- not yet implemented
