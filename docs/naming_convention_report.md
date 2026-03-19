# TileOPs File Naming Convention Report

> Based on DEVELOPMENT.md conventions from tile-ai/TileOPs
>
> Generated: 2026-03-19 | Total ops: 186

## Convention Reference (from DEVELOPMENT.md)

```
Kernel: tileops/kernels/{operator_name}/   (package directory with __init__.py)
Op:     tileops/ops/{operator_name}.py
Test:   tests/ops/test_{operator_name}.py
Bench:  benchmarks/ops/bench_{operator_name}.py
```

Every `tileops/kernels/*` subpackage must have an `__init__.py` with explicit
`__all__` and `from .module import Symbol` re-exports.

### Status Legend

| Status | Meaning |
|:------:|:--------|
| OK | Current path matches the DEVELOPMENT.md convention |
| RENAME | Current path exists but does not match convention |
| TODO | File does not exist yet (not implemented); shows what it SHOULD be named |

---

## Category: Elementwise (#397)

| Op | File Type | Current Path | Convention Path | Status |
|:---|:----------|:-------------|:----------------|:------:|
| add | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/add/` | RENAME |
| add | op | `tileops/ops/elementwise.py` | `tileops/ops/add.py` | RENAME |
| add | test | `tests/ops/test_binary_arith.py::test_add_broadcast`, `tests/ops/test_binary_arith.py::test_add_same_shape`, `tests/ops/test_binary_arith.py::test_add_strategies` | `tests/ops/test_add.py` | RENAME |
| add | bench | `benchmarks/ops/bench_binary_arith.py::bench_add`, `benchmarks/ops/bench_binary_strategy.py::bench_add_strategies` | `benchmarks/ops/bench_add.py` | RENAME |
| sub | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/sub/` | RENAME |
| sub | op | `tileops/ops/elementwise.py` | `tileops/ops/sub.py` | RENAME |
| sub | test | `tests/ops/test_binary_arith.py::test_sub_op` | `tests/ops/test_sub.py` | RENAME |
| sub | bench | `benchmarks/ops/bench_binary_arith.py::bench_sub` | `benchmarks/ops/bench_sub.py` | RENAME |
| mul | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/mul/` | RENAME |
| mul | op | `tileops/ops/elementwise.py` | `tileops/ops/mul.py` | RENAME |
| mul | test | `tests/ops/test_binary_arith.py::test_mul_op` | `tests/ops/test_mul.py` | RENAME |
| mul | bench | `benchmarks/ops/bench_binary_arith.py::bench_mul` | `benchmarks/ops/bench_mul.py` | RENAME |
| div | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/div/` | RENAME |
| div | op | `tileops/ops/elementwise.py` | `tileops/ops/div.py` | RENAME |
| div | test | `tests/ops/test_binary_arith.py::test_div_op` | `tests/ops/test_div.py` | RENAME |
| div | bench | `benchmarks/ops/bench_binary_arith.py::bench_div` | `benchmarks/ops/bench_div.py` | RENAME |
| remainder | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/remainder/` | RENAME |
| remainder | op | `tileops/ops/elementwise.py` | `tileops/ops/remainder.py` | RENAME |
| remainder | test | `tests/ops/test_binary_arith.py::test_remainder_op` | `tests/ops/test_remainder.py` | RENAME |
| remainder | bench | `benchmarks/ops/bench_binary_arith.py::bench_remainder` | `benchmarks/ops/bench_remainder.py` | RENAME |
| pow | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/pow/` | RENAME |
| pow | op | `tileops/ops/elementwise.py` | `tileops/ops/pow.py` | RENAME |
| pow | test | `tests/ops/test_binary_arith.py::test_pow_op` | `tests/ops/test_pow.py` | RENAME |
| pow | bench | `benchmarks/ops/bench_binary_arith.py::bench_pow` | `benchmarks/ops/bench_pow.py` | RENAME |
| floor_divide | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/floor_divide/` | RENAME |
| floor_divide | op | `tileops/ops/elementwise.py` | `tileops/ops/floor_divide.py` | RENAME |
| floor_divide | test | `tests/ops/test_binary_arith.py::test_floor_divide_op` | `tests/ops/test_floor_divide.py` | RENAME |
| floor_divide | bench | `benchmarks/ops/bench_binary_arith.py::bench_floor_divide` | `benchmarks/ops/bench_floor_divide.py` | RENAME |
| lerp | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/lerp/` | RENAME |
| lerp | op | `tileops/ops/elementwise.py` | `tileops/ops/lerp.py` | RENAME |
| lerp | test | `tests/ops/test_binary_arith.py::test_lerp_op` | `tests/ops/test_lerp.py` | RENAME |
| lerp | bench | `benchmarks/ops/bench_binary_arith.py::bench_lerp` | `benchmarks/ops/bench_lerp.py` | RENAME |
| maximum | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/maximum/` | RENAME |
| maximum | op | `tileops/ops/elementwise.py` | `tileops/ops/maximum.py` | RENAME |
| maximum | test | `tests/ops/test_binary_arith.py::test_maximum_nan_propagation`, `tests/ops/test_binary_arith.py::test_maximum_op` | `tests/ops/test_maximum.py` | RENAME |
| maximum | bench | `benchmarks/ops/bench_binary_arith.py::bench_maximum` | `benchmarks/ops/bench_maximum.py` | RENAME |
| minimum | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/minimum/` | RENAME |
| minimum | op | `tileops/ops/elementwise.py` | `tileops/ops/minimum.py` | RENAME |
| minimum | test | `tests/ops/test_binary_arith.py::test_minimum_nan_propagation`, `tests/ops/test_binary_arith.py::test_minimum_op` | `tests/ops/test_minimum.py` | RENAME |
| minimum | bench | `benchmarks/ops/bench_binary_arith.py::bench_minimum` | `benchmarks/ops/bench_minimum.py` | RENAME |
| exp | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/exp/` | RENAME |
| exp | op | `tileops/ops/elementwise.py` | `tileops/ops/exp.py` | RENAME |
| exp | test | `tests/ops/test_unary_math.py::test_exp`, `tests/ops/test_unary_math.py::test_exp_edge` | `tests/ops/test_exp.py` | RENAME |
| exp | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_exp` | `benchmarks/ops/bench_exp.py` | RENAME |
| log | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/log/` | RENAME |
| log | op | `tileops/ops/elementwise.py` | `tileops/ops/log.py` | RENAME |
| log | test | `tests/ops/test_unary_math.py::test_log`, `tests/ops/test_unary_math.py::test_log_edge` | `tests/ops/test_log.py` | RENAME |
| log | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_log` | `benchmarks/ops/bench_log.py` | RENAME |
| sqrt | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/sqrt/` | RENAME |
| sqrt | op | `tileops/ops/elementwise.py` | `tileops/ops/sqrt.py` | RENAME |
| sqrt | test | `tests/ops/test_unary_math.py::test_sqrt`, `tests/ops/test_unary_math.py::test_sqrt_edge` | `tests/ops/test_sqrt.py` | RENAME |
| sqrt | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_sqrt` | `benchmarks/ops/bench_sqrt.py` | RENAME |
| rsqrt | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/rsqrt/` | RENAME |
| rsqrt | op | `tileops/ops/elementwise.py` | `tileops/ops/rsqrt.py` | RENAME |
| rsqrt | test | `tests/ops/test_unary_math.py::test_rsqrt`, `tests/ops/test_unary_math.py::test_rsqrt_edge` | `tests/ops/test_rsqrt.py` | RENAME |
| rsqrt | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_rsqrt` | `benchmarks/ops/bench_rsqrt.py` | RENAME |
| abs | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/abs/` | RENAME |
| abs | op | `tileops/ops/elementwise.py` | `tileops/ops/abs.py` | RENAME |
| abs | test | `tests/ops/test_unary_math.py::test_abs` | `tests/ops/test_abs.py` | RENAME |
| abs | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_abs` | `benchmarks/ops/bench_abs.py` | RENAME |
| neg | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/neg/` | RENAME |
| neg | op | `tileops/ops/elementwise.py` | `tileops/ops/neg.py` | RENAME |
| neg | test | `tests/ops/test_unary_math.py::test_neg` | `tests/ops/test_neg.py` | RENAME |
| neg | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_neg` | `benchmarks/ops/bench_neg.py` | RENAME |
| reciprocal | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/reciprocal/` | RENAME |
| reciprocal | op | `tileops/ops/elementwise.py` | `tileops/ops/reciprocal.py` | RENAME |
| reciprocal | test | `tests/ops/test_unary_math.py::test_reciprocal`, `tests/ops/test_unary_math.py::test_reciprocal_edge` | `tests/ops/test_reciprocal.py` | RENAME |
| reciprocal | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_reciprocal` | `benchmarks/ops/bench_reciprocal.py` | RENAME |
| sign | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/sign/` | RENAME |
| sign | op | `tileops/ops/elementwise.py` | `tileops/ops/sign.py` | RENAME |
| sign | test | `tests/ops/test_unary_math.py::test_sign`, `tests/ops/test_unary_math.py::test_sign_edge` | `tests/ops/test_sign.py` | RENAME |
| sign | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_sign` | `benchmarks/ops/bench_sign.py` | RENAME |
| sin | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/sin/` | RENAME |
| sin | op | `tileops/ops/elementwise.py` | `tileops/ops/sin.py` | RENAME |
| sin | test | `tests/ops/test_unary_math.py::test_sin` | `tests/ops/test_sin.py` | RENAME |
| sin | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_sin` | `benchmarks/ops/bench_sin.py` | RENAME |
| cos | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/cos/` | RENAME |
| cos | op | `tileops/ops/elementwise.py` | `tileops/ops/cos.py` | RENAME |
| cos | test | `tests/ops/test_unary_math.py::test_cos` | `tests/ops/test_cos.py` | RENAME |
| cos | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_cos` | `benchmarks/ops/bench_cos.py` | RENAME |
| floor | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/floor/` | RENAME |
| floor | op | `tileops/ops/elementwise.py` | `tileops/ops/floor.py` | RENAME |
| floor | test | `tests/ops/test_unary_math.py::test_floor` | `tests/ops/test_floor.py` | RENAME |
| floor | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_floor` | `benchmarks/ops/bench_floor.py` | RENAME |
| ceil | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/ceil/` | RENAME |
| ceil | op | `tileops/ops/elementwise.py` | `tileops/ops/ceil.py` | RENAME |
| ceil | test | `tests/ops/test_unary_math.py::test_ceil` | `tests/ops/test_ceil.py` | RENAME |
| ceil | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_ceil` | `benchmarks/ops/bench_ceil.py` | RENAME |
| round | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/round/` | RENAME |
| round | op | `tileops/ops/elementwise.py` | `tileops/ops/round.py` | RENAME |
| round | test | `tests/ops/test_unary_math.py::test_round` | `tests/ops/test_round.py` | RENAME |
| round | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_round` | `benchmarks/ops/bench_round.py` | RENAME |
| trunc | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/trunc/` | RENAME |
| trunc | op | `tileops/ops/elementwise.py` | `tileops/ops/trunc.py` | RENAME |
| trunc | test | `tests/ops/test_unary_math.py::test_trunc` | `tests/ops/test_trunc.py` | RENAME |
| trunc | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_trunc` | `benchmarks/ops/bench_trunc.py` | RENAME |
| erf | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/erf/` | RENAME |
| erf | op | `tileops/ops/elementwise.py` | `tileops/ops/erf.py` | RENAME |
| erf | test | `tests/ops/test_unary_math.py::test_erf`, `tests/ops/test_unary_math.py::test_erf_edge` | `tests/ops/test_erf.py` | RENAME |
| erf | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_erf` | `benchmarks/ops/bench_erf.py` | RENAME |
| log1p | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/log1p/` | RENAME |
| log1p | op | `tileops/ops/elementwise.py` | `tileops/ops/log1p.py` | RENAME |
| log1p | test | `tests/ops/test_unary_math.py::test_log1p`, `tests/ops/test_unary_math.py::test_log1p_edge` | `tests/ops/test_log1p.py` | RENAME |
| log1p | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_log1p` | `benchmarks/ops/bench_log1p.py` | RENAME |
| expm1 | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/expm1/` | RENAME |
| expm1 | op | `tileops/ops/elementwise.py` | `tileops/ops/expm1.py` | RENAME |
| expm1 | test | `tests/ops/test_unary_math.py::test_expm1`, `tests/ops/test_unary_math.py::test_expm1_edge` | `tests/ops/test_expm1.py` | RENAME |
| expm1 | bench | `benchmarks/ops/bench_unary_elementwise.py::bench_expm1` | `benchmarks/ops/bench_expm1.py` | RENAME |
| relu | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/relu/` | RENAME |
| relu | op | `tileops/ops/elementwise.py` | `tileops/ops/relu.py` | RENAME |
| relu | test | `tests/ops/test_activation.py::test_relu_op`, `tests/ops/test_activation.py::test_relu_strategies` | `tests/ops/test_relu.py` | RENAME |
| relu | bench | `benchmarks/ops/bench_activation.py::bench_relu`, `benchmarks/ops/bench_unary_strategy.py::bench_relu_strategies` | `benchmarks/ops/bench_relu.py` | RENAME |
| gelu | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/gelu/` | RENAME |
| gelu | op | `tileops/ops/elementwise.py` | `tileops/ops/gelu.py` | RENAME |
| gelu | test | `tests/ops/test_activation.py::test_gelu` | `tests/ops/test_gelu.py` | RENAME |
| gelu | bench | `benchmarks/ops/bench_activation.py::bench_gelu` | `benchmarks/ops/bench_gelu.py` | RENAME |
| silu | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/silu/` | RENAME |
| silu | op | `tileops/ops/elementwise.py` | `tileops/ops/silu.py` | RENAME |
| silu | test | `tests/ops/test_activation.py::test_silu` | `tests/ops/test_silu.py` | RENAME |
| silu | bench | `benchmarks/ops/bench_activation.py::bench_silu` | `benchmarks/ops/bench_silu.py` | RENAME |
| sigmoid | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/sigmoid/` | RENAME |
| sigmoid | op | `tileops/ops/elementwise.py` | `tileops/ops/sigmoid.py` | RENAME |
| sigmoid | test | `tests/ops/test_activation.py::test_sigmoid`, `tests/ops/test_activation.py::test_sigmoid_edge` | `tests/ops/test_sigmoid.py` | RENAME |
| sigmoid | bench | `benchmarks/ops/bench_activation.py::bench_sigmoid` | `benchmarks/ops/bench_sigmoid.py` | RENAME |
| tanh | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/tanh/` | RENAME |
| tanh | op | `tileops/ops/elementwise.py` | `tileops/ops/tanh.py` | RENAME |
| tanh | test | `tests/ops/test_activation.py::test_tanh`, `tests/ops/test_activation.py::test_tanh_edge` | `tests/ops/test_tanh.py` | RENAME |
| tanh | bench | `benchmarks/ops/bench_activation.py::bench_tanh` | `benchmarks/ops/bench_tanh.py` | RENAME |
| leaky_relu | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/leaky_relu/` | RENAME |
| leaky_relu | op | `tileops/ops/elementwise.py` | `tileops/ops/leaky_relu.py` | RENAME |
| leaky_relu | test | `-` | `tests/ops/test_leaky_relu.py` | TODO |
| leaky_relu | bench | `benchmarks/ops/bench_activation.py::bench_leaky_relu` | `benchmarks/ops/bench_leaky_relu.py` | RENAME |
| elu | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/elu/` | RENAME |
| elu | op | `tileops/ops/elementwise.py` | `tileops/ops/elu.py` | RENAME |
| elu | test | `-` | `tests/ops/test_elu.py` | TODO |
| elu | bench | `benchmarks/ops/bench_activation.py::bench_elu` | `benchmarks/ops/bench_elu.py` | RENAME |
| selu | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/selu/` | RENAME |
| selu | op | `tileops/ops/elementwise.py` | `tileops/ops/selu.py` | RENAME |
| selu | test | `tests/ops/test_activation.py::test_selu` | `tests/ops/test_selu.py` | RENAME |
| selu | bench | `benchmarks/ops/bench_activation.py::bench_selu` | `benchmarks/ops/bench_selu.py` | RENAME |
| hardswish | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/hardswish/` | RENAME |
| hardswish | op | `tileops/ops/elementwise.py` | `tileops/ops/hardswish.py` | RENAME |
| hardswish | test | `tests/ops/test_activation.py::test_hardswish` | `tests/ops/test_hardswish.py` | RENAME |
| hardswish | bench | `benchmarks/ops/bench_activation.py::bench_hardswish` | `benchmarks/ops/bench_hardswish.py` | RENAME |
| hardsigmoid | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/hardsigmoid/` | RENAME |
| hardsigmoid | op | `tileops/ops/elementwise.py` | `tileops/ops/hardsigmoid.py` | RENAME |
| hardsigmoid | test | `tests/ops/test_activation.py::test_hardsigmoid` | `tests/ops/test_hardsigmoid.py` | RENAME |
| hardsigmoid | bench | `benchmarks/ops/bench_activation.py::bench_hardsigmoid` | `benchmarks/ops/bench_hardsigmoid.py` | RENAME |
| hardtanh | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/hardtanh/` | RENAME |
| hardtanh | op | `tileops/ops/elementwise.py` | `tileops/ops/hardtanh.py` | RENAME |
| hardtanh | test | `-` | `tests/ops/test_hardtanh.py` | TODO |
| hardtanh | bench | `benchmarks/ops/bench_activation.py::bench_hardtanh` | `benchmarks/ops/bench_hardtanh.py` | RENAME |
| softplus | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/softplus/` | RENAME |
| softplus | op | `tileops/ops/elementwise.py` | `tileops/ops/softplus.py` | RENAME |
| softplus | test | `-` | `tests/ops/test_softplus.py` | TODO |
| softplus | bench | `benchmarks/ops/bench_activation.py::bench_softplus` | `benchmarks/ops/bench_softplus.py` | RENAME |
| mish | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/mish/` | RENAME |
| mish | op | `tileops/ops/elementwise.py` | `tileops/ops/mish.py` | RENAME |
| mish | test | `tests/ops/test_activation.py::test_mish` | `tests/ops/test_mish.py` | RENAME |
| mish | bench | `benchmarks/ops/bench_activation.py::bench_mish` | `benchmarks/ops/bench_mish.py` | RENAME |
| prelu | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/prelu/` | RENAME |
| prelu | op | `tileops/ops/elementwise.py` | `tileops/ops/prelu.py` | RENAME |
| prelu | test | `-` | `tests/ops/test_prelu.py` | TODO |
| prelu | bench | `benchmarks/ops/bench_activation.py::bench_prelu` | `benchmarks/ops/bench_prelu.py` | RENAME |
| silu_and_mul | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/silu_and_mul/` | RENAME |
| silu_and_mul | op | `tileops/ops/elementwise.py` | `tileops/ops/silu_and_mul.py` | RENAME |
| silu_and_mul | test | `tests/ops/test_fused_gated.py::test_silu_and_mul_op` | `tests/ops/test_silu_and_mul.py` | RENAME |
| silu_and_mul | bench | `benchmarks/ops/bench_activation.py::bench_silu_and_mul` | `benchmarks/ops/bench_silu_and_mul.py` | RENAME |
| gelu_and_mul | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/gelu_and_mul/` | RENAME |
| gelu_and_mul | op | `tileops/ops/elementwise.py` | `tileops/ops/gelu_and_mul.py` | RENAME |
| gelu_and_mul | test | `tests/ops/test_fused_gated.py::test_gelu_and_mul_op` | `tests/ops/test_gelu_and_mul.py` | RENAME |
| gelu_and_mul | bench | `benchmarks/ops/bench_activation.py::bench_gelu_and_mul` | `benchmarks/ops/bench_gelu_and_mul.py` | RENAME |
| gelu_tanh_and_mul | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/gelu_tanh_and_mul/` | RENAME |
| gelu_tanh_and_mul | op | `tileops/ops/elementwise.py` | `tileops/ops/gelu_tanh_and_mul.py` | RENAME |
| gelu_tanh_and_mul | test | `tests/ops/test_fused_gated.py::test_gelu_tanh_and_mul_op` | `tests/ops/test_gelu_tanh_and_mul.py` | RENAME |
| gelu_tanh_and_mul | bench | `benchmarks/ops/bench_activation.py::bench_gelu_tanh_and_mul` | `benchmarks/ops/bench_gelu_tanh_and_mul.py` | RENAME |
| eq | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/eq/` | RENAME |
| eq | op | `tileops/ops/elementwise.py` | `tileops/ops/eq.py` | RENAME |
| eq | test | `tests/ops/test_comparison.py::test_eq_edge_case`, `tests/ops/test_comparison.py::test_eq_op` | `tests/ops/test_eq.py` | RENAME |
| eq | bench | `benchmarks/ops/bench_binary_elementwise.py::bench_eq` | `benchmarks/ops/bench_eq.py` | RENAME |
| ne | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/ne/` | RENAME |
| ne | op | `tileops/ops/elementwise.py` | `tileops/ops/ne.py` | RENAME |
| ne | test | `tests/ops/test_comparison.py::test_ne_op` | `tests/ops/test_ne.py` | RENAME |
| ne | bench | `benchmarks/ops/bench_binary_elementwise.py::bench_ne` | `benchmarks/ops/bench_ne.py` | RENAME |
| gt | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/gt/` | RENAME |
| gt | op | `tileops/ops/elementwise.py` | `tileops/ops/gt.py` | RENAME |
| gt | test | `tests/ops/test_comparison.py::test_gt_op` | `tests/ops/test_gt.py` | RENAME |
| gt | bench | `benchmarks/ops/bench_binary_elementwise.py::bench_gt` | `benchmarks/ops/bench_gt.py` | RENAME |
| lt | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/lt/` | RENAME |
| lt | op | `tileops/ops/elementwise.py` | `tileops/ops/lt.py` | RENAME |
| lt | test | `tests/ops/test_comparison.py::test_lt_op` | `tests/ops/test_lt.py` | RENAME |
| lt | bench | `benchmarks/ops/bench_binary_elementwise.py::bench_lt` | `benchmarks/ops/bench_lt.py` | RENAME |
| ge | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/ge/` | RENAME |
| ge | op | `tileops/ops/elementwise.py` | `tileops/ops/ge.py` | RENAME |
| ge | test | `tests/ops/test_comparison.py::test_ge_op` | `tests/ops/test_ge.py` | RENAME |
| ge | bench | `benchmarks/ops/bench_binary_elementwise.py::bench_ge` | `benchmarks/ops/bench_ge.py` | RENAME |
| le | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/le/` | RENAME |
| le | op | `tileops/ops/elementwise.py` | `tileops/ops/le.py` | RENAME |
| le | test | `tests/ops/test_comparison.py::test_le_op` | `tests/ops/test_le.py` | RENAME |
| le | bench | `benchmarks/ops/bench_binary_elementwise.py::bench_le` | `benchmarks/ops/bench_le.py` | RENAME |
| bitwise_and | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/bitwise_and/` | RENAME |
| bitwise_and | op | `tileops/ops/elementwise.py` | `tileops/ops/bitwise_and.py` | RENAME |
| bitwise_and | test | `tests/ops/test_bitwise.py::test_bitwise_and_op` | `tests/ops/test_bitwise_and.py` | RENAME |
| bitwise_and | bench | `benchmarks/ops/bench_binary_elementwise.py::bench_bitwise_and` | `benchmarks/ops/bench_bitwise_and.py` | RENAME |
| bitwise_or | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/bitwise_or/` | RENAME |
| bitwise_or | op | `tileops/ops/elementwise.py` | `tileops/ops/bitwise_or.py` | RENAME |
| bitwise_or | test | `tests/ops/test_bitwise.py::test_bitwise_or_op` | `tests/ops/test_bitwise_or.py` | RENAME |
| bitwise_or | bench | `benchmarks/ops/bench_binary_elementwise.py::bench_bitwise_or` | `benchmarks/ops/bench_bitwise_or.py` | RENAME |
| bitwise_xor | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/bitwise_xor/` | RENAME |
| bitwise_xor | op | `tileops/ops/elementwise.py` | `tileops/ops/bitwise_xor.py` | RENAME |
| bitwise_xor | test | `tests/ops/test_bitwise.py::test_bitwise_xor_op` | `tests/ops/test_bitwise_xor.py` | RENAME |
| bitwise_xor | bench | `benchmarks/ops/bench_binary_elementwise.py::bench_bitwise_xor` | `benchmarks/ops/bench_bitwise_xor.py` | RENAME |
| bitwise_not | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/bitwise_not/` | RENAME |
| bitwise_not | op | `tileops/ops/elementwise.py` | `tileops/ops/bitwise_not.py` | RENAME |
| bitwise_not | test | `tests/ops/test_bitwise.py::test_bitwise_not` | `tests/ops/test_bitwise_not.py` | RENAME |
| bitwise_not | bench | `benchmarks/ops/bench_binary_elementwise.py::bench_bitwise_not` | `benchmarks/ops/bench_bitwise_not.py` | RENAME |
| logical_not | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/logical_not/` | RENAME |
| logical_not | op | `tileops/ops/elementwise.py` | `tileops/ops/logical_not.py` | RENAME |
| logical_not | test | `tests/ops/test_logical.py::test_logical_not` | `tests/ops/test_logical_not.py` | RENAME |
| logical_not | bench | `benchmarks/ops/bench_binary_elementwise.py::bench_logical_not` | `benchmarks/ops/bench_logical_not.py` | RENAME |
| logical_and | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/logical_and/` | RENAME |
| logical_and | op | `tileops/ops/elementwise.py` | `tileops/ops/logical_and.py` | RENAME |
| logical_and | test | `tests/ops/test_logical.py::test_logical_and_op` | `tests/ops/test_logical_and.py` | RENAME |
| logical_and | bench | `benchmarks/ops/bench_binary_elementwise.py::bench_logical_and` | `benchmarks/ops/bench_logical_and.py` | RENAME |
| logical_or | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/logical_or/` | RENAME |
| logical_or | op | `tileops/ops/elementwise.py` | `tileops/ops/logical_or.py` | RENAME |
| logical_or | test | `tests/ops/test_logical.py::test_logical_or_op` | `tests/ops/test_logical_or.py` | RENAME |
| logical_or | bench | `benchmarks/ops/bench_binary_elementwise.py::bench_logical_or` | `benchmarks/ops/bench_logical_or.py` | RENAME |
| where | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/where/` | RENAME |
| where | op | `tileops/ops/elementwise.py` | `tileops/ops/where.py` | RENAME |
| where | test | `-` | `tests/ops/test_where.py` | TODO |
| where | bench | `-` | `benchmarks/ops/bench_where.py` | TODO |
| clamp | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/clamp/` | RENAME |
| clamp | op | `tileops/ops/elementwise.py` | `tileops/ops/clamp.py` | RENAME |
| clamp | test | `-` | `tests/ops/test_clamp.py` | TODO |
| clamp | bench | `-` | `benchmarks/ops/bench_clamp.py` | TODO |
| masked_fill | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/masked_fill/` | RENAME |
| masked_fill | op | `tileops/ops/elementwise.py` | `tileops/ops/masked_fill.py` | RENAME |
| masked_fill | test | `-` | `tests/ops/test_masked_fill.py` | TODO |
| masked_fill | bench | `-` | `benchmarks/ops/bench_masked_fill.py` | TODO |
| nan_to_num | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/nan_to_num/` | RENAME |
| nan_to_num | op | `tileops/ops/elementwise.py` | `tileops/ops/nan_to_num.py` | RENAME |
| nan_to_num | test | `-` | `tests/ops/test_nan_to_num.py` | TODO |
| nan_to_num | bench | `-` | `benchmarks/ops/bench_nan_to_num.py` | TODO |
| isnan | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/isnan/` | RENAME |
| isnan | op | `tileops/ops/elementwise.py` | `tileops/ops/isnan.py` | RENAME |
| isnan | test | `tests/ops/test_special_elementwise.py::test_isnan`, `tests/ops/test_special_elementwise.py::test_isnan_edge` | `tests/ops/test_isnan.py` | RENAME |
| isnan | bench | `-` | `benchmarks/ops/bench_isnan.py` | TODO |
| isinf | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/isinf/` | RENAME |
| isinf | op | `tileops/ops/elementwise.py` | `tileops/ops/isinf.py` | RENAME |
| isinf | test | `tests/ops/test_special_elementwise.py::test_isinf`, `tests/ops/test_special_elementwise.py::test_isinf_edge` | `tests/ops/test_isinf.py` | RENAME |
| isinf | bench | `-` | `benchmarks/ops/bench_isinf.py` | TODO |
| isfinite | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/isfinite/` | RENAME |
| isfinite | op | `tileops/ops/elementwise.py` | `tileops/ops/isfinite.py` | RENAME |
| isfinite | test | `tests/ops/test_special_elementwise.py::test_isfinite`, `tests/ops/test_special_elementwise.py::test_isfinite_edge` | `tests/ops/test_isfinite.py` | RENAME |
| isfinite | bench | `-` | `benchmarks/ops/bench_isfinite.py` | TODO |
| dropout | kernel | `tileops/kernels/dropout.py` | `tileops/kernels/dropout/` | RENAME |
| dropout | op | `tileops/ops/dropout.py` | `tileops/ops/dropout.py` | OK |
| dropout | test | `tests/ops/test_dropout.py::test_dropout` | `tests/ops/test_dropout.py` | OK |
| dropout | bench | `benchmarks/ops/bench_dropout.py::bench_dropout` | `benchmarks/ops/bench_dropout.py` | OK |
| rope_neox | kernel | `tileops/kernels/rope.py` | `tileops/kernels/rope_neox/` | RENAME |
| rope_neox | op | `tileops/ops/rope.py` | `tileops/ops/rope_neox.py` | RENAME |
| rope_neox | test | `tests/ops/test_rope.py::test_rope_neox` | `tests/ops/test_rope_neox.py` | RENAME |
| rope_neox | bench | `benchmarks/ops/bench_rope.py::bench_rope_neox` | `benchmarks/ops/bench_rope_neox.py` | RENAME |
| rope_non_neox | kernel | `tileops/kernels/rope.py` | `tileops/kernels/rope_non_neox/` | RENAME |
| rope_non_neox | op | `tileops/ops/rope.py` | `tileops/ops/rope_non_neox.py` | RENAME |
| rope_non_neox | test | `tests/ops/test_rope.py::test_rope_non_neox` | `tests/ops/test_rope_non_neox.py` | RENAME |
| rope_non_neox | bench | `benchmarks/ops/bench_rope.py::bench_rope_non_neox` | `benchmarks/ops/bench_rope_non_neox.py` | RENAME |
| rope_llama31 | kernel | `tileops/kernels/rope.py` | `tileops/kernels/rope_llama31/` | RENAME |
| rope_llama31 | op | `tileops/ops/rope.py` | `tileops/ops/rope_llama31.py` | RENAME |
| rope_llama31 | test | `tests/ops/test_rope.py::test_rope_llama31` | `tests/ops/test_rope_llama31.py` | RENAME |
| rope_llama31 | bench | `benchmarks/ops/bench_rope.py::bench_rope_llama31` | `benchmarks/ops/bench_rope_llama31.py` | RENAME |
| yarn_rope | kernel | `-` | `tileops/kernels/yarn_rope/` | TODO |
| yarn_rope | op | `-` | `tileops/ops/yarn_rope.py` | TODO |
| yarn_rope | test | `-` | `tests/ops/test_yarn_rope.py` | TODO |
| yarn_rope | bench | `-` | `benchmarks/ops/bench_yarn_rope.py` | TODO |
| longrope | kernel | `-` | `tileops/kernels/longrope/` | TODO |
| longrope | op | `-` | `tileops/ops/longrope.py` | TODO |
| longrope | test | `-` | `tests/ops/test_longrope.py` | TODO |
| longrope | bench | `-` | `benchmarks/ops/bench_longrope.py` | TODO |
| alibi | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/alibi/` | RENAME |
| alibi | op | `tileops/ops/elementwise.py` | `tileops/ops/alibi.py` | RENAME |
| alibi | test | `-` | `tests/ops/test_alibi.py` | TODO |
| alibi | bench | `-` | `benchmarks/ops/bench_alibi.py` | TODO |
| sinusoidal | kernel | `tileops/kernels/elementwise.py` | `tileops/kernels/sinusoidal/` | RENAME |
| sinusoidal | op | `tileops/ops/elementwise.py` | `tileops/ops/sinusoidal.py` | RENAME |
| sinusoidal | test | `-` | `tests/ops/test_sinusoidal.py` | TODO |
| sinusoidal | bench | `-` | `benchmarks/ops/bench_sinusoidal.py` | TODO |

## Category: Reduce (#398)

| Op | File Type | Current Path | Convention Path | Status |
|:---|:----------|:-------------|:----------------|:------:|
| sum | kernel | `-` | `tileops/kernels/sum/` | TODO |
| sum | op | `tileops/ops/reduction/reduce.py` | `tileops/ops/sum.py` | RENAME |
| sum | test | `-` | `tests/ops/test_sum.py` | TODO |
| sum | bench | `-` | `benchmarks/ops/bench_sum.py` | TODO |
| mean | kernel | `-` | `tileops/kernels/mean/` | TODO |
| mean | op | `tileops/ops/reduction/reduce.py` | `tileops/ops/mean.py` | RENAME |
| mean | test | `-` | `tests/ops/test_mean.py` | TODO |
| mean | bench | `-` | `benchmarks/ops/bench_mean.py` | TODO |
| amin | kernel | `-` | `tileops/kernels/amin/` | TODO |
| amin | op | `tileops/ops/reduction/reduce.py` | `tileops/ops/amin.py` | RENAME |
| amin | test | `-` | `tests/ops/test_amin.py` | TODO |
| amin | bench | `-` | `benchmarks/ops/bench_amin.py` | TODO |
| amax | kernel | `-` | `tileops/kernels/amax/` | TODO |
| amax | op | `tileops/ops/reduction/reduce.py` | `tileops/ops/amax.py` | RENAME |
| amax | test | `-` | `tests/ops/test_amax.py` | TODO |
| amax | bench | `-` | `benchmarks/ops/bench_amax.py` | TODO |
| prod | kernel | `-` | `tileops/kernels/prod/` | TODO |
| prod | op | `tileops/ops/reduction/reduce.py` | `tileops/ops/prod.py` | RENAME |
| prod | test | `-` | `tests/ops/test_prod.py` | TODO |
| prod | bench | `-` | `benchmarks/ops/bench_prod.py` | TODO |
| std | kernel | `-` | `tileops/kernels/std/` | TODO |
| std | op | `tileops/ops/reduction/reduce.py` | `tileops/ops/std.py` | RENAME |
| std | test | `-` | `tests/ops/test_std.py` | TODO |
| std | bench | `-` | `benchmarks/ops/bench_std.py` | TODO |
| var | kernel | `-` | `tileops/kernels/var/` | TODO |
| var | op | `tileops/ops/reduction/reduce.py` | `tileops/ops/var.py` | RENAME |
| var | test | `-` | `tests/ops/test_var.py` | TODO |
| var | bench | `-` | `benchmarks/ops/bench_var.py` | TODO |
| var_mean | kernel | `-` | `tileops/kernels/var_mean/` | TODO |
| var_mean | op | `tileops/ops/reduction/reduce.py` | `tileops/ops/var_mean.py` | RENAME |
| var_mean | test | `-` | `tests/ops/test_var_mean.py` | TODO |
| var_mean | bench | `-` | `benchmarks/ops/bench_var_mean.py` | TODO |
| softmax | kernel | `-` | `tileops/kernels/softmax/` | TODO |
| softmax | op | `tileops/ops/reduction/softmax.py` | `tileops/ops/softmax.py` | RENAME |
| softmax | test | `-` | `tests/ops/test_softmax.py` | TODO |
| softmax | bench | `-` | `benchmarks/ops/bench_softmax.py` | TODO |
| log_softmax | kernel | `-` | `tileops/kernels/log_softmax/` | TODO |
| log_softmax | op | `tileops/ops/reduction/log_softmax.py` | `tileops/ops/log_softmax.py` | RENAME |
| log_softmax | test | `-` | `tests/ops/test_log_softmax.py` | TODO |
| log_softmax | bench | `-` | `benchmarks/ops/bench_log_softmax.py` | TODO |
| logsumexp | kernel | `-` | `tileops/kernels/logsumexp/` | TODO |
| logsumexp | op | `tileops/ops/reduction/logsumexp.py` | `tileops/ops/logsumexp.py` | RENAME |
| logsumexp | test | `-` | `tests/ops/test_logsumexp.py` | TODO |
| logsumexp | bench | `-` | `benchmarks/ops/bench_logsumexp.py` | TODO |
| argmax | kernel | `-` | `tileops/kernels/argmax/` | TODO |
| argmax | op | `tileops/ops/reduction/argmax.py` | `tileops/ops/argmax.py` | RENAME |
| argmax | test | `-` | `tests/ops/test_argmax.py` | TODO |
| argmax | bench | `-` | `benchmarks/ops/bench_argmax.py` | TODO |
| argmin | kernel | `-` | `tileops/kernels/argmin/` | TODO |
| argmin | op | `tileops/ops/reduction/argmin.py` | `tileops/ops/argmin.py` | RENAME |
| argmin | test | `-` | `tests/ops/test_argmin.py` | TODO |
| argmin | bench | `-` | `benchmarks/ops/bench_argmin.py` | TODO |
| cumsum | kernel | `-` | `tileops/kernels/cumsum/` | TODO |
| cumsum | op | `tileops/ops/reduction/cumsum.py` | `tileops/ops/cumsum.py` | RENAME |
| cumsum | test | `-` | `tests/ops/test_cumsum.py` | TODO |
| cumsum | bench | `-` | `benchmarks/ops/bench_cumsum.py` | TODO |
| cumprod | kernel | `-` | `tileops/kernels/cumprod/` | TODO |
| cumprod | op | `tileops/ops/reduction/cumprod.py` | `tileops/ops/cumprod.py` | RENAME |
| cumprod | test | `-` | `tests/ops/test_cumprod.py` | TODO |
| cumprod | bench | `-` | `benchmarks/ops/bench_cumprod.py` | TODO |
| any | kernel | `-` | `tileops/kernels/any/` | TODO |
| any | op | `tileops/ops/reduction/any_op.py` | `tileops/ops/any.py` | RENAME |
| any | test | `-` | `tests/ops/test_any.py` | TODO |
| any | bench | `-` | `benchmarks/ops/bench_any.py` | TODO |
| all | kernel | `-` | `tileops/kernels/all/` | TODO |
| all | op | `tileops/ops/reduction/all_op.py` | `tileops/ops/all.py` | RENAME |
| all | test | `-` | `tests/ops/test_all.py` | TODO |
| all | bench | `-` | `benchmarks/ops/bench_all.py` | TODO |
| l1_norm | kernel | `tileops/kernels/reduction/vector_norm/fwd.py` | `tileops/kernels/l1_norm/` | RENAME |
| l1_norm | op | `tileops/ops/reduction/l1_norm.py` | `tileops/ops/l1_norm.py` | RENAME |
| l1_norm | test | `tests/ops/test_vector_norm.py::test_l1_norm` | `tests/ops/test_l1_norm.py` | RENAME |
| l1_norm | bench | `benchmarks/ops/bench_vector_norm.py::bench_l1_norm` | `benchmarks/ops/bench_l1_norm.py` | RENAME |
| l2_norm | kernel | `tileops/kernels/reduction/vector_norm/fwd.py` | `tileops/kernels/l2_norm/` | RENAME |
| l2_norm | op | `tileops/ops/reduction/l2_norm.py` | `tileops/ops/l2_norm.py` | RENAME |
| l2_norm | test | `tests/ops/test_vector_norm.py::test_l2_norm` | `tests/ops/test_l2_norm.py` | RENAME |
| l2_norm | bench | `benchmarks/ops/bench_vector_norm.py::bench_l2_norm` | `benchmarks/ops/bench_l2_norm.py` | RENAME |
| inf_norm | kernel | `tileops/kernels/reduction/vector_norm/fwd.py` | `tileops/kernels/inf_norm/` | RENAME |
| inf_norm | op | `tileops/ops/reduction/inf_norm.py` | `tileops/ops/inf_norm.py` | RENAME |
| inf_norm | test | `tests/ops/test_vector_norm.py::test_inf_norm` | `tests/ops/test_inf_norm.py` | RENAME |
| inf_norm | bench | `benchmarks/ops/bench_vector_norm.py::bench_inf_norm` | `benchmarks/ops/bench_inf_norm.py` | RENAME |

## Category: Norm (#399)

| Op | File Type | Current Path | Convention Path | Status |
|:---|:----------|:-------------|:----------------|:------:|
| layer_norm | kernel | `tileops/kernels/norm/layer_norm.py` | `tileops/kernels/layer_norm/` | RENAME |
| layer_norm | op | `tileops/ops/norm/layer_norm.py` | `tileops/ops/layer_norm.py` | RENAME |
| layer_norm | test | `tests/ops/test_layer_norm.py::test_layer_norm_3d`, `tests/ops/test_layer_norm.py::test_layer_norm_op` | `tests/ops/test_layer_norm.py` | OK |
| layer_norm | bench | `benchmarks/ops/bench_layer_norm.py::bench_layer_norm` | `benchmarks/ops/bench_layer_norm.py` | OK |
| batch_norm | kernel | `tileops/kernels/norm/batch_norm.py` | `tileops/kernels/batch_norm/` | RENAME |
| batch_norm | op | `tileops/ops/norm/batch_norm.py` | `tileops/ops/batch_norm.py` | RENAME |
| batch_norm | test | `tests/ops/test_batch_norm.py::test_batch_norm_bwd`, `tests/ops/test_batch_norm.py::test_batch_norm_fwd` | `tests/ops/test_batch_norm.py` | OK |
| batch_norm | bench | `benchmarks/ops/bench_batch_norm.py::bench_batch_norm` | `benchmarks/ops/bench_batch_norm.py` | OK |
| group_norm | kernel | `tileops/kernels/norm/group_norm.py` | `tileops/kernels/group_norm/` | RENAME |
| group_norm | op | `tileops/ops/norm/group_norm.py` | `tileops/ops/group_norm.py` | RENAME |
| group_norm | test | `tests/ops/test_group_norm.py::test_group_norm_non_contiguous`, `tests/ops/test_group_norm.py::test_group_norm_op` | `tests/ops/test_group_norm.py` | OK |
| group_norm | bench | `benchmarks/ops/bench_group_norm.py::bench_group_norm` | `benchmarks/ops/bench_group_norm.py` | OK |
| instance_norm | kernel | `tileops/kernels/norm/instance_norm/__init__.py` | `tileops/kernels/instance_norm/` | RENAME |
| instance_norm | op | `tileops/ops/norm/instance_norm.py` | `tileops/ops/instance_norm.py` | RENAME |
| instance_norm | test | `tests/ops/test_instance_norm.py::test_instance_norm_non_contiguous`, `tests/ops/test_instance_norm.py::test_instance_norm_op` | `tests/ops/test_instance_norm.py` | OK |
| instance_norm | bench | `benchmarks/ops/bench_instance_norm.py::bench_instance_norm` | `benchmarks/ops/bench_instance_norm.py` | OK |
| rms_norm | kernel | `tileops/kernels/norm/rms_norm.py` | `tileops/kernels/rms_norm/` | RENAME |
| rms_norm | op | `tileops/ops/norm/rms_norm.py` | `tileops/ops/rms_norm.py` | RENAME |
| rms_norm | test | `tests/ops/test_rms_norm.py::test_rms_norm_3d`, `tests/ops/test_rms_norm.py::test_rms_norm_op` | `tests/ops/test_rms_norm.py` | OK |
| rms_norm | bench | `benchmarks/ops/bench_rms_norm.py::bench_rms_norm` | `benchmarks/ops/bench_rms_norm.py` | OK |
| qk_norm | kernel | `tileops/kernels/norm/qk_norm/__init__.py` | `tileops/kernels/qk_norm/` | RENAME |
| qk_norm | op | `-` | `tileops/ops/qk_norm.py` | TODO |
| qk_norm | test | `-` | `tests/ops/test_qk_norm.py` | TODO |
| qk_norm | bench | `-` | `benchmarks/ops/bench_qk_norm.py` | TODO |
| ada_layer_norm | kernel | `tileops/kernels/norm/ada_layer_norm/fwd.py` | `tileops/kernels/ada_layer_norm/` | RENAME |
| ada_layer_norm | op | `tileops/ops/norm/ada_layer_norm.py` | `tileops/ops/ada_layer_norm.py` | RENAME |
| ada_layer_norm | test | `tests/ops/test_ada_layer_norm.py::test_ada_layer_norm_3d`, `tests/ops/test_ada_layer_norm.py::test_ada_layer_norm_op` | `tests/ops/test_ada_layer_norm.py` | OK |
| ada_layer_norm | bench | `benchmarks/ops/bench_ada_layer_norm.py::bench_ada_layer_norm` | `benchmarks/ops/bench_ada_layer_norm.py` | OK |
| ada_layer_norm_zero | kernel | `tileops/kernels/norm/ada_layer_norm_zero/__init__.py` | `tileops/kernels/ada_layer_norm_zero/` | RENAME |
| ada_layer_norm_zero | op | `tileops/ops/norm/ada_layer_norm_zero.py` | `tileops/ops/ada_layer_norm_zero.py` | RENAME |
| ada_layer_norm_zero | test | `tests/ops/test_ada_layer_norm_zero.py::test_ada_layer_norm_zero_3d`, `tests/ops/test_ada_layer_norm_zero.py::test_ada_layer_norm_zero_op` | `tests/ops/test_ada_layer_norm_zero.py` | OK |
| ada_layer_norm_zero | bench | `benchmarks/ops/bench_ada_layer_norm.py::bench_ada_layer_norm_zero` | `benchmarks/ops/bench_ada_layer_norm_zero.py` | RENAME |
| fused_add_layer_norm | kernel | `tileops/kernels/norm/fused_add_norm/fwd.py` | `tileops/kernels/fused_add_layer_norm/` | RENAME |
| fused_add_layer_norm | op | `tileops/ops/norm/fused_add_layer_norm.py` | `tileops/ops/fused_add_layer_norm.py` | RENAME |
| fused_add_layer_norm | test | `tests/ops/test_fused_add_layer_norm.py::test_fused_add_layer_norm_3d`, `tests/ops/test_fused_add_layer_norm.py::test_fused_add_layer_norm_op` | `tests/ops/test_fused_add_layer_norm.py` | OK |
| fused_add_layer_norm | bench | `benchmarks/ops/bench_fused_add_layer_norm.py::bench_fused_add_layer_norm` | `benchmarks/ops/bench_fused_add_layer_norm.py` | OK |
| fused_add_rmsnorm | kernel | `tileops/kernels/norm/fused_add_norm/fwd.py` | `tileops/kernels/fused_add_rmsnorm/` | RENAME |
| fused_add_rmsnorm | op | `tileops/ops/norm/fused_add_rmsnorm.py` | `tileops/ops/fused_add_rmsnorm.py` | RENAME |
| fused_add_rmsnorm | test | `tests/ops/test_fused_add_rmsnorm.py::test_fused_add_rmsnorm_3d`, `tests/ops/test_fused_add_rmsnorm.py::test_fused_add_rmsnorm_op` | `tests/ops/test_fused_add_rmsnorm.py` | OK |
| fused_add_rmsnorm | bench | `benchmarks/ops/bench_fused_add_layer_norm.py::bench_fused_add_rmsnorm` | `benchmarks/ops/bench_fused_add_rmsnorm.py` | RENAME |

## Category: Conv & Pooling (#402)

| Op | File Type | Current Path | Convention Path | Status |
|:---|:----------|:-------------|:----------------|:------:|
| conv1d | kernel | `-` | `tileops/kernels/conv1d/` | TODO |
| conv1d | op | `-` | `tileops/ops/conv1d.py` | TODO |
| conv1d | test | `-` | `tests/ops/test_conv1d.py` | TODO |
| conv1d | bench | `-` | `benchmarks/ops/bench_conv1d.py` | TODO |
| conv2d | kernel | `-` | `tileops/kernels/conv2d/` | TODO |
| conv2d | op | `-` | `tileops/ops/conv2d.py` | TODO |
| conv2d | test | `-` | `tests/ops/test_conv2d.py` | TODO |
| conv2d | bench | `-` | `benchmarks/ops/bench_conv2d.py` | TODO |
| conv3d | kernel | `-` | `tileops/kernels/conv3d/` | TODO |
| conv3d | op | `-` | `tileops/ops/conv3d.py` | TODO |
| conv3d | test | `-` | `tests/ops/test_conv3d.py` | TODO |
| conv3d | bench | `-` | `benchmarks/ops/bench_conv3d.py` | TODO |
| conv_transpose1d | kernel | `-` | `tileops/kernels/conv_transpose1d/` | TODO |
| conv_transpose1d | op | `-` | `tileops/ops/conv_transpose1d.py` | TODO |
| conv_transpose1d | test | `-` | `tests/ops/test_conv_transpose1d.py` | TODO |
| conv_transpose1d | bench | `-` | `benchmarks/ops/bench_conv_transpose1d.py` | TODO |
| conv_transpose2d | kernel | `-` | `tileops/kernels/conv_transpose2d/` | TODO |
| conv_transpose2d | op | `-` | `tileops/ops/conv_transpose2d.py` | TODO |
| conv_transpose2d | test | `-` | `tests/ops/test_conv_transpose2d.py` | TODO |
| conv_transpose2d | bench | `-` | `benchmarks/ops/bench_conv_transpose2d.py` | TODO |
| depthwise_conv2d | kernel | `-` | `tileops/kernels/depthwise_conv2d/` | TODO |
| depthwise_conv2d | op | `-` | `tileops/ops/depthwise_conv2d.py` | TODO |
| depthwise_conv2d | test | `-` | `tests/ops/test_depthwise_conv2d.py` | TODO |
| depthwise_conv2d | bench | `-` | `benchmarks/ops/bench_depthwise_conv2d.py` | TODO |
| grouped_conv2d | kernel | `-` | `tileops/kernels/grouped_conv2d/` | TODO |
| grouped_conv2d | op | `-` | `tileops/ops/grouped_conv2d.py` | TODO |
| grouped_conv2d | test | `-` | `tests/ops/test_grouped_conv2d.py` | TODO |
| grouped_conv2d | bench | `-` | `benchmarks/ops/bench_grouped_conv2d.py` | TODO |
| dilated_conv2d | kernel | `-` | `tileops/kernels/dilated_conv2d/` | TODO |
| dilated_conv2d | op | `-` | `tileops/ops/dilated_conv2d.py` | TODO |
| dilated_conv2d | test | `-` | `tests/ops/test_dilated_conv2d.py` | TODO |
| dilated_conv2d | bench | `-` | `benchmarks/ops/bench_dilated_conv2d.py` | TODO |
| max_pool1d | kernel | `-` | `tileops/kernels/max_pool1d/` | TODO |
| max_pool1d | op | `-` | `tileops/ops/max_pool1d.py` | TODO |
| max_pool1d | test | `-` | `tests/ops/test_max_pool1d.py` | TODO |
| max_pool1d | bench | `-` | `benchmarks/ops/bench_max_pool1d.py` | TODO |
| max_pool2d | kernel | `-` | `tileops/kernels/max_pool2d/` | TODO |
| max_pool2d | op | `-` | `tileops/ops/max_pool2d.py` | TODO |
| max_pool2d | test | `-` | `tests/ops/test_max_pool2d.py` | TODO |
| max_pool2d | bench | `-` | `benchmarks/ops/bench_max_pool2d.py` | TODO |
| max_pool3d | kernel | `-` | `tileops/kernels/max_pool3d/` | TODO |
| max_pool3d | op | `-` | `tileops/ops/max_pool3d.py` | TODO |
| max_pool3d | test | `-` | `tests/ops/test_max_pool3d.py` | TODO |
| max_pool3d | bench | `-` | `benchmarks/ops/bench_max_pool3d.py` | TODO |
| avg_pool1d | kernel | `-` | `tileops/kernels/avg_pool1d/` | TODO |
| avg_pool1d | op | `-` | `tileops/ops/avg_pool1d.py` | TODO |
| avg_pool1d | test | `-` | `tests/ops/test_avg_pool1d.py` | TODO |
| avg_pool1d | bench | `-` | `benchmarks/ops/bench_avg_pool1d.py` | TODO |
| avg_pool2d | kernel | `-` | `tileops/kernels/avg_pool2d/` | TODO |
| avg_pool2d | op | `-` | `tileops/ops/avg_pool2d.py` | TODO |
| avg_pool2d | test | `-` | `tests/ops/test_avg_pool2d.py` | TODO |
| avg_pool2d | bench | `-` | `benchmarks/ops/bench_avg_pool2d.py` | TODO |
| avg_pool3d | kernel | `-` | `tileops/kernels/avg_pool3d/` | TODO |
| avg_pool3d | op | `-` | `tileops/ops/avg_pool3d.py` | TODO |
| avg_pool3d | test | `-` | `tests/ops/test_avg_pool3d.py` | TODO |
| avg_pool3d | bench | `-` | `benchmarks/ops/bench_avg_pool3d.py` | TODO |
| adaptive_avg_pool2d | kernel | `-` | `tileops/kernels/adaptive_avg_pool2d/` | TODO |
| adaptive_avg_pool2d | op | `-` | `tileops/ops/adaptive_avg_pool2d.py` | TODO |
| adaptive_avg_pool2d | test | `-` | `tests/ops/test_adaptive_avg_pool2d.py` | TODO |
| adaptive_avg_pool2d | bench | `-` | `benchmarks/ops/bench_adaptive_avg_pool2d.py` | TODO |
| adaptive_max_pool2d | kernel | `-` | `tileops/kernels/adaptive_max_pool2d/` | TODO |
| adaptive_max_pool2d | op | `-` | `tileops/ops/adaptive_max_pool2d.py` | TODO |
| adaptive_max_pool2d | test | `-` | `tests/ops/test_adaptive_max_pool2d.py` | TODO |
| adaptive_max_pool2d | bench | `-` | `benchmarks/ops/bench_adaptive_max_pool2d.py` | TODO |

## Category: GEMM (#400)

| Op | File Type | Current Path | Convention Path | Status |
|:---|:----------|:-------------|:----------------|:------:|
| gemm_fp16 | kernel | `tileops/kernels/gemm/gemm.py` | `tileops/kernels/gemm_fp16/` | RENAME |
| gemm_fp16 | op | `tileops/ops/gemm.py` | `tileops/ops/gemm_fp16.py` | RENAME |
| gemm_fp16 | test | `tests/ops/test_gemm.py::test_gemm` | `tests/ops/test_gemm_fp16.py` | RENAME |
| gemm_fp16 | bench | `benchmarks/ops/bench_gemm.py::bench_gemm` | `benchmarks/ops/bench_gemm_fp16.py` | RENAME |
| gemm_fp8 | kernel | `tileops/kernels/gemm/gemm.py` | `tileops/kernels/gemm_fp8/` | RENAME |
| gemm_fp8 | op | `tileops/ops/gemm.py` | `tileops/ops/gemm_fp8.py` | RENAME |
| gemm_fp8 | test | `-` | `tests/ops/test_gemm_fp8.py` | TODO |
| gemm_fp8 | bench | `benchmarks/ops/bench_gemm.py::bench_gemm_fp8` | `benchmarks/ops/bench_gemm_fp8.py` | RENAME |
| gemm_fp8_block_scaled | kernel | `tileops/kernels/gemm/gemm.py` | `tileops/kernels/gemm_fp8_block_scaled/` | RENAME |
| gemm_fp8_block_scaled | op | `tileops/ops/gemm.py` | `tileops/ops/gemm_fp8_block_scaled.py` | RENAME |
| gemm_fp8_block_scaled | test | `-` | `tests/ops/test_gemm_fp8_block_scaled.py` | TODO |
| gemm_fp8_block_scaled | bench | `benchmarks/ops/bench_gemm.py::bench_gemm_fp8_block_scaled` | `benchmarks/ops/bench_gemm_fp8_block_scaled.py` | RENAME |
| gemv_fp16 | kernel | `tileops/kernels/gemm/gemv.py` | `tileops/kernels/gemv_fp16/` | RENAME |
| gemv_fp16 | op | `tileops/ops/gemm.py` | `tileops/ops/gemv_fp16.py` | RENAME |
| gemv_fp16 | test | `tests/ops/test_gemm.py::test_gemv_boundary_lhs_row`, `tests/ops/test_gemm.py::test_gemv_boundary_rhs_col` | `tests/ops/test_gemv_fp16.py` | RENAME |
| gemv_fp16 | bench | `benchmarks/ops/bench_gemm.py::bench_gemv` | `benchmarks/ops/bench_gemv_fp16.py` | RENAME |
| gemv_fp8 | kernel | `tileops/kernels/gemm/gemv.py` | `tileops/kernels/gemv_fp8/` | RENAME |
| gemv_fp8 | op | `tileops/ops/gemm.py` | `tileops/ops/gemv_fp8.py` | RENAME |
| gemv_fp8 | test | `-` | `tests/ops/test_gemv_fp8.py` | TODO |
| gemv_fp8 | bench | `benchmarks/ops/bench_gemm.py::bench_gemv_fp8` | `benchmarks/ops/bench_gemv_fp8.py` | RENAME |
| small_batch_gemm_fp16 | kernel | `tileops/kernels/gemm/gemm.py` | `tileops/kernels/small_batch_gemm_fp16/` | RENAME |
| small_batch_gemm_fp16 | op | `tileops/ops/gemm.py` | `tileops/ops/small_batch_gemm_fp16.py` | RENAME |
| small_batch_gemm_fp16 | test | `-` | `tests/ops/test_small_batch_gemm_fp16.py` | TODO |
| small_batch_gemm_fp16 | bench | `benchmarks/ops/bench_gemm.py::bench_small_batch_gemm` | `benchmarks/ops/bench_small_batch_gemm_fp16.py` | RENAME |
| small_batch_gemm_fp8 | kernel | `tileops/kernels/gemm/gemm.py` | `tileops/kernels/small_batch_gemm_fp8/` | RENAME |
| small_batch_gemm_fp8 | op | `tileops/ops/gemm.py` | `tileops/ops/small_batch_gemm_fp8.py` | RENAME |
| small_batch_gemm_fp8 | test | `-` | `tests/ops/test_small_batch_gemm_fp8.py` | TODO |
| small_batch_gemm_fp8 | bench | `benchmarks/ops/bench_gemm.py::bench_small_batch_gemm_fp8` | `benchmarks/ops/bench_small_batch_gemm_fp8.py` | RENAME |
| bmm_fp16 | kernel | `tileops/kernels/gemm/gemm.py` | `tileops/kernels/bmm_fp16/` | RENAME |
| bmm_fp16 | op | `-` | `tileops/ops/bmm_fp16.py` | TODO |
| bmm_fp16 | test | `-` | `tests/ops/test_bmm_fp16.py` | TODO |
| bmm_fp16 | bench | `benchmarks/ops/bench_gemm.py::bench_bmm` | `benchmarks/ops/bench_bmm_fp16.py` | RENAME |
| bmm_fp8 | kernel | `tileops/kernels/gemm/gemm.py` | `tileops/kernels/bmm_fp8/` | RENAME |
| bmm_fp8 | op | `-` | `tileops/ops/bmm_fp8.py` | TODO |
| bmm_fp8 | test | `-` | `tests/ops/test_bmm_fp8.py` | TODO |
| bmm_fp8 | bench | `benchmarks/ops/bench_gemm.py::bench_bmm_fp8` | `benchmarks/ops/bench_bmm_fp8.py` | RENAME |
| groupgemm_fp16 | kernel | `tileops/kernels/grouped_gemm/grouped_gemm.py` | `tileops/kernels/groupgemm_fp16/` | RENAME |
| groupgemm_fp16 | op | `tileops/ops/grouped_gemm.py` | `tileops/ops/groupgemm_fp16.py` | RENAME |
| groupgemm_fp16 | test | `tests/ops/test_grouped_gemm.py::test_grouped_gemm` | `tests/ops/test_groupgemm_fp16.py` | RENAME |
| groupgemm_fp16 | bench | `benchmarks/ops/bench_grouped_gemm.py::bench_grouped_gemm` | `benchmarks/ops/bench_groupgemm_fp16.py` | RENAME |
| groupgemm_fp8 | kernel | `tileops/kernels/grouped_gemm/grouped_gemm.py` | `tileops/kernels/groupgemm_fp8/` | RENAME |
| groupgemm_fp8 | op | `tileops/ops/grouped_gemm.py` | `tileops/ops/groupgemm_fp8.py` | RENAME |
| groupgemm_fp8 | test | `-` | `tests/ops/test_groupgemm_fp8.py` | TODO |
| groupgemm_fp8 | bench | `benchmarks/ops/bench_grouped_gemm.py::bench_grouped_gemm_fp8` | `benchmarks/ops/bench_groupgemm_fp8.py` | RENAME |
| outer | kernel | `-` | `tileops/kernels/outer/` | TODO |
| outer | op | `-` | `tileops/ops/outer.py` | TODO |
| outer | test | `-` | `tests/ops/test_outer.py` | TODO |
| outer | bench | `-` | `benchmarks/ops/bench_outer.py` | TODO |
| w4a16 | kernel | `-` | `tileops/kernels/w4a16/` | TODO |
| w4a16 | op | `-` | `tileops/ops/w4a16.py` | TODO |
| w4a16 | test | `-` | `tests/ops/test_w4a16.py` | TODO |
| w4a16 | bench | `-` | `benchmarks/ops/bench_w4a16.py` | TODO |
| w8a8 | kernel | `-` | `tileops/kernels/w8a8/` | TODO |
| w8a8 | op | `-` | `tileops/ops/w8a8.py` | TODO |
| w8a8 | test | `-` | `tests/ops/test_w8a8.py` | TODO |
| w8a8 | bench | `-` | `benchmarks/ops/bench_w8a8.py` | TODO |
| w8a8_int8 | kernel | `-` | `tileops/kernels/w8a8_int8/` | TODO |
| w8a8_int8 | op | `-` | `tileops/ops/w8a8_int8.py` | TODO |
| w8a8_int8 | test | `-` | `tests/ops/test_w8a8_int8.py` | TODO |
| w8a8_int8 | bench | `-` | `benchmarks/ops/bench_w8a8_int8.py` | TODO |
| weight_only_int4 | kernel | `-` | `tileops/kernels/weight_only_int4/` | TODO |
| weight_only_int4 | op | `-` | `tileops/ops/weight_only_int4.py` | TODO |
| weight_only_int4 | test | `-` | `tests/ops/test_weight_only_int4.py` | TODO |
| weight_only_int4 | bench | `-` | `benchmarks/ops/bench_weight_only_int4.py` | TODO |
| fp4 | kernel | `-` | `tileops/kernels/fp4/` | TODO |
| fp4 | op | `-` | `tileops/ops/fp4.py` | TODO |
| fp4 | test | `-` | `tests/ops/test_fp4.py` | TODO |
| fp4 | bench | `-` | `benchmarks/ops/bench_fp4.py` | TODO |
| sparse_gemm_fp16 | kernel | `-` | `tileops/kernels/sparse_gemm_fp16/` | TODO |
| sparse_gemm_fp16 | op | `-` | `tileops/ops/sparse_gemm_fp16.py` | TODO |
| sparse_gemm_fp16 | test | `-` | `tests/ops/test_sparse_gemm_fp16.py` | TODO |
| sparse_gemm_fp16 | bench | `-` | `benchmarks/ops/bench_sparse_gemm_fp16.py` | TODO |
| sparse_gemm_fp8 | kernel | `-` | `tileops/kernels/sparse_gemm_fp8/` | TODO |
| sparse_gemm_fp8 | op | `-` | `tileops/ops/sparse_gemm_fp8.py` | TODO |
| sparse_gemm_fp8 | test | `-` | `tests/ops/test_sparse_gemm_fp8.py` | TODO |
| sparse_gemm_fp8 | bench | `-` | `benchmarks/ops/bench_sparse_gemm_fp8.py` | TODO |

## Category: Quantize (#401)

| Op | File Type | Current Path | Convention Path | Status |
|:---|:----------|:-------------|:----------------|:------:|
| int8_per_tensor | kernel | `-` | `tileops/kernels/int8_per_tensor/` | TODO |
| int8_per_tensor | op | `-` | `tileops/ops/int8_per_tensor.py` | TODO |
| int8_per_tensor | test | `-` | `tests/ops/test_int8_per_tensor.py` | TODO |
| int8_per_tensor | bench | `-` | `benchmarks/ops/bench_int8_per_tensor.py` | TODO |
| int8_per_channel | kernel | `-` | `tileops/kernels/int8_per_channel/` | TODO |
| int8_per_channel | op | `-` | `tileops/ops/int8_per_channel.py` | TODO |
| int8_per_channel | test | `-` | `tests/ops/test_int8_per_channel.py` | TODO |
| int8_per_channel | bench | `-` | `benchmarks/ops/bench_int8_per_channel.py` | TODO |
| int8_per_block | kernel | `-` | `tileops/kernels/int8_per_block/` | TODO |
| int8_per_block | op | `-` | `tileops/ops/int8_per_block.py` | TODO |
| int8_per_block | test | `-` | `tests/ops/test_int8_per_block.py` | TODO |
| int8_per_block | bench | `-` | `benchmarks/ops/bench_int8_per_block.py` | TODO |
| smooth_quant | kernel | `-` | `tileops/kernels/smooth_quant/` | TODO |
| smooth_quant | op | `-` | `tileops/ops/smooth_quant.py` | TODO |
| smooth_quant | test | `-` | `tests/ops/test_smooth_quant.py` | TODO |
| smooth_quant | bench | `-` | `benchmarks/ops/bench_smooth_quant.py` | TODO |
| int4_per_channel | kernel | `-` | `tileops/kernels/int4_per_channel/` | TODO |
| int4_per_channel | op | `-` | `tileops/ops/int4_per_channel.py` | TODO |
| int4_per_channel | test | `-` | `tests/ops/test_int4_per_channel.py` | TODO |
| int4_per_channel | bench | `-` | `benchmarks/ops/bench_int4_per_channel.py` | TODO |
| int4_per_block | kernel | `-` | `tileops/kernels/int4_per_block/` | TODO |
| int4_per_block | op | `-` | `tileops/ops/int4_per_block.py` | TODO |
| int4_per_block | test | `-` | `tests/ops/test_int4_per_block.py` | TODO |
| int4_per_block | bench | `-` | `benchmarks/ops/bench_int4_per_block.py` | TODO |
| nf4 | kernel | `-` | `tileops/kernels/nf4/` | TODO |
| nf4 | op | `-` | `tileops/ops/nf4.py` | TODO |
| nf4 | test | `-` | `tests/ops/test_nf4.py` | TODO |
| nf4 | bench | `-` | `benchmarks/ops/bench_nf4.py` | TODO |
| fp8_per_tensor | kernel | `tileops/kernels/deepseek_mla/fp8_quant.py` | `tileops/kernels/fp8_per_tensor/` | RENAME |
| fp8_per_tensor | op | `tileops/ops/fp8_quant.py` | `tileops/ops/fp8_per_tensor.py` | RENAME |
| fp8_per_tensor | test | `tests/ops/test_fp8_quant.py::test_fp8_quant_op` | `tests/ops/test_fp8_per_tensor.py` | RENAME |
| fp8_per_tensor | bench | `benchmarks/ops/bench_fp8_quant.py::bench_fp8_quant` | `benchmarks/ops/bench_fp8_per_tensor.py` | RENAME |
| fp8_per_block | kernel | `tileops/kernels/deepseek_mla/fp8_quant.py` | `tileops/kernels/fp8_per_block/` | RENAME |
| fp8_per_block | op | `-` | `tileops/ops/fp8_per_block.py` | TODO |
| fp8_per_block | test | `-` | `tests/ops/test_fp8_per_block.py` | TODO |
| fp8_per_block | bench | `benchmarks/ops/bench_fp8_quant.py::bench_fp8_block_quant` | `benchmarks/ops/bench_fp8_per_block.py` | RENAME |
| fp8_cast_transpose | kernel | `-` | `tileops/kernels/fp8_cast_transpose/` | TODO |
| fp8_cast_transpose | op | `-` | `tileops/ops/fp8_cast_transpose.py` | TODO |
| fp8_cast_transpose | test | `-` | `tests/ops/test_fp8_cast_transpose.py` | TODO |
| fp8_cast_transpose | bench | `-` | `benchmarks/ops/bench_fp8_cast_transpose.py` | TODO |

## Category: Sampling (#426)

| Op | File Type | Current Path | Convention Path | Status |
|:---|:----------|:-------------|:----------------|:------:|
| top_k | kernel | `-` | `tileops/kernels/top_k/` | TODO |
| top_k | op | `-` | `tileops/ops/top_k.py` | TODO |
| top_k | test | `-` | `tests/ops/test_top_k.py` | TODO |
| top_k | bench | `-` | `benchmarks/ops/bench_top_k.py` | TODO |
| top_p | kernel | `-` | `tileops/kernels/top_p/` | TODO |
| top_p | op | `-` | `tileops/ops/top_p.py` | TODO |
| top_p | test | `-` | `tests/ops/test_top_p.py` | TODO |
| top_p | bench | `-` | `benchmarks/ops/bench_top_p.py` | TODO |
| min_p | kernel | `-` | `tileops/kernels/min_p/` | TODO |
| min_p | op | `-` | `tileops/ops/min_p.py` | TODO |
| min_p | test | `-` | `tests/ops/test_min_p.py` | TODO |
| min_p | bench | `-` | `benchmarks/ops/bench_min_p.py` | TODO |
| top_k_top_p | kernel | `-` | `tileops/kernels/top_k_top_p/` | TODO |
| top_k_top_p | op | `-` | `tileops/ops/top_k_top_p.py` | TODO |
| top_k_top_p | test | `-` | `tests/ops/test_top_k_top_p.py` | TODO |
| top_k_top_p | bench | `-` | `benchmarks/ops/bench_top_k_top_p.py` | TODO |
| temperature_scale | kernel | `-` | `tileops/kernels/temperature_scale/` | TODO |
| temperature_scale | op | `-` | `tileops/ops/temperature_scale.py` | TODO |
| temperature_scale | test | `-` | `tests/ops/test_temperature_scale.py` | TODO |
| temperature_scale | bench | `-` | `benchmarks/ops/bench_temperature_scale.py` | TODO |
| sampling_from_probs | kernel | `-` | `tileops/kernels/sampling_from_probs/` | TODO |
| sampling_from_probs | op | `-` | `tileops/ops/sampling_from_probs.py` | TODO |
| sampling_from_probs | test | `-` | `tests/ops/test_sampling_from_probs.py` | TODO |
| sampling_from_probs | bench | `-` | `benchmarks/ops/bench_sampling_from_probs.py` | TODO |
| chain_speculative_sampling | kernel | `tileops/kernels/deepseek_mla/topk_selector.py` | `tileops/kernels/chain_speculative_sampling/` | RENAME |
| chain_speculative_sampling | op | `tileops/ops/topk_selector.py` | `tileops/ops/chain_speculative_sampling.py` | RENAME |
| chain_speculative_sampling | test | `tests/ops/test_topk_selector.py::test_topk_selector_op` | `tests/ops/test_chain_speculative_sampling.py` | RENAME |
| chain_speculative_sampling | bench | `benchmarks/ops/bench_topk_selector.py::bench_topk_selector` | `benchmarks/ops/bench_chain_speculative_sampling.py` | RENAME |

## Category: Flash Attention (#403)

| Op | File Type | Current Path | Convention Path | Status |
|:---|:----------|:-------------|:----------------|:------:|
| flash_prefill_fwd | kernel | `tileops/kernels/flash_attn/fwd.py` | `tileops/kernels/flash_prefill_fwd/` | RENAME |
| flash_prefill_fwd | op | `tileops/ops/gqa.py`, `tileops/ops/mha.py` | `tileops/ops/flash_prefill_fwd.py` | RENAME |
| flash_prefill_fwd | test | `tests/ops/test_gqa.py::test_gqa_fwd`, `tests/ops/test_mha.py::test_mha_fwd` | `tests/ops/test_flash_prefill_fwd.py` | RENAME |
| flash_prefill_fwd | bench | `benchmarks/ops/bench_gqa.py::bench_gqa_fwd`, `benchmarks/ops/bench_mha.py::bench_mha_fwd` | `benchmarks/ops/bench_flash_prefill_fwd.py` | RENAME |
| flash_prefill_bwd | kernel | `tileops/kernels/flash_attn/bwd.py` | `tileops/kernels/flash_prefill_bwd/` | RENAME |
| flash_prefill_bwd | op | `tileops/ops/gqa.py`, `tileops/ops/mha.py` | `tileops/ops/flash_prefill_bwd.py` | RENAME |
| flash_prefill_bwd | test | `tests/ops/test_gqa.py::test_gqa_bwd`, `tests/ops/test_mha.py::test_mha_bwd` | `tests/ops/test_flash_prefill_bwd.py` | RENAME |
| flash_prefill_bwd | bench | `benchmarks/ops/bench_gqa.py::bench_gqa_bwd`, `benchmarks/ops/bench_mha.py::bench_mha_bwd` | `benchmarks/ops/bench_flash_prefill_bwd.py` | RENAME |
| flash_prefill_varlen_fwd | kernel | `tileops/kernels/deepseek_nsa/gqa_sliding_window_varlen_fwd.py` | `tileops/kernels/flash_prefill_varlen_fwd/` | RENAME |
| flash_prefill_varlen_fwd | op | `tileops/ops/gqa_sliding_window_varlen_fwd.py` | `tileops/ops/flash_prefill_varlen_fwd.py` | RENAME |
| flash_prefill_varlen_fwd | test | `tests/ops/test_gqa_sliding_window_varlen_fwd.py::test_gqa_sliding_window_varlen_fwd_op` | `tests/ops/test_flash_prefill_varlen_fwd.py` | RENAME |
| flash_prefill_varlen_fwd | bench | `benchmarks/ops/bench_gqa_sliding_window_varlen_fwd.py::bench_gqa_sliding_window_varlen_fwd` | `benchmarks/ops/bench_flash_prefill_varlen_fwd.py` | RENAME |
| flash_prefill_varlen_bwd | kernel | `-` | `tileops/kernels/flash_prefill_varlen_bwd/` | TODO |
| flash_prefill_varlen_bwd | op | `-` | `tileops/ops/flash_prefill_varlen_bwd.py` | TODO |
| flash_prefill_varlen_bwd | test | `-` | `tests/ops/test_flash_prefill_varlen_bwd.py` | TODO |
| flash_prefill_varlen_bwd | bench | `-` | `benchmarks/ops/bench_flash_prefill_varlen_bwd.py` | TODO |
| flash_decode_fwd | kernel | `tileops/kernels/flash_decode/gqa_decode.py`, `tileops/kernels/flash_decode/mha_decode.py` | `tileops/kernels/flash_decode_fwd/` | RENAME |
| flash_decode_fwd | op | `tileops/ops/gqa_decode.py`, `tileops/ops/mha_decode.py` | `tileops/ops/flash_decode_fwd.py` | RENAME |
| flash_decode_fwd | test | `tests/ops/test_gqa_decode.py::test_gqa_decode`, `tests/ops/test_mha_decode.py::test_mha_decode` | `tests/ops/test_flash_decode_fwd.py` | RENAME |
| flash_decode_fwd | bench | `benchmarks/ops/bench_gqa_decode.py::bench_gqa_decode`, `benchmarks/ops/bench_mha_decode.py::bench_mha_decode` | `benchmarks/ops/bench_flash_decode_fwd.py` | RENAME |
| flash_decode_paged_fwd | kernel | `tileops/kernels/flash_decode/gqa_decode_paged.py`, `tileops/kernels/flash_decode/mha_decode_paged.py` | `tileops/kernels/flash_decode_paged_fwd/` | RENAME |
| flash_decode_paged_fwd | op | `tileops/ops/gqa_decode_paged.py`, `tileops/ops/mha_decode_paged.py` | `tileops/ops/flash_decode_paged_fwd.py` | RENAME |
| flash_decode_paged_fwd | test | `tests/ops/test_gqa_decode_paged.py::test_gqa_decode_paged_op`, `tests/ops/test_mha_decode_paged.py::test_mha_decode_paged_op` | `tests/ops/test_flash_decode_paged_fwd.py` | RENAME |
| flash_decode_paged_fwd | bench | `benchmarks/ops/bench_gqa_decode_paged.py::bench_gqa_decode_paged`, `benchmarks/ops/bench_mha_decode_paged.py::bench_mha_decode_paged` | `benchmarks/ops/bench_flash_decode_paged_fwd.py` | RENAME |
| flash_decode_varlen_fwd | kernel | `-` | `tileops/kernels/flash_decode_varlen_fwd/` | TODO |
| flash_decode_varlen_fwd | op | `-` | `tileops/ops/flash_decode_varlen_fwd.py` | TODO |
| flash_decode_varlen_fwd | test | `-` | `tests/ops/test_flash_decode_varlen_fwd.py` | TODO |
| flash_decode_varlen_fwd | bench | `-` | `benchmarks/ops/bench_flash_decode_varlen_fwd.py` | TODO |
| flash_chunked_prefill_fwd | kernel | `-` | `tileops/kernels/flash_chunked_prefill_fwd/` | TODO |
| flash_chunked_prefill_fwd | op | `-` | `tileops/ops/flash_chunked_prefill_fwd.py` | TODO |
| flash_chunked_prefill_fwd | test | `-` | `tests/ops/test_flash_chunked_prefill_fwd.py` | TODO |
| flash_chunked_prefill_fwd | bench | `-` | `benchmarks/ops/bench_flash_chunked_prefill_fwd.py` | TODO |
| mla_prefill_fwd | kernel | `-` | `tileops/kernels/mla_prefill_fwd/` | TODO |
| mla_prefill_fwd | op | `-` | `tileops/ops/mla_prefill_fwd.py` | TODO |
| mla_prefill_fwd | test | `-` | `tests/ops/test_mla_prefill_fwd.py` | TODO |
| mla_prefill_fwd | bench | `-` | `benchmarks/ops/bench_mla_prefill_fwd.py` | TODO |
| mla_prefill_bwd | kernel | `-` | `tileops/kernels/mla_prefill_bwd/` | TODO |
| mla_prefill_bwd | op | `-` | `tileops/ops/mla_prefill_bwd.py` | TODO |
| mla_prefill_bwd | test | `-` | `tests/ops/test_mla_prefill_bwd.py` | TODO |
| mla_prefill_bwd | bench | `-` | `benchmarks/ops/bench_mla_prefill_bwd.py` | TODO |
| mla_decode_fwd | kernel | `tileops/kernels/deepseek_mla/deepseek_mla_decode.py` | `tileops/kernels/mla_decode_fwd/` | RENAME |
| mla_decode_fwd | op | `tileops/ops/deepseek_mla_decode.py` | `tileops/ops/mla_decode_fwd.py` | RENAME |
| mla_decode_fwd | test | `tests/ops/test_deepseek_mla_decode.py::test_mla_decode` | `tests/ops/test_mla_decode_fwd.py` | RENAME |
| mla_decode_fwd | bench | `benchmarks/ops/bench_deepseek_mla_decode.py::bench_mla_decode` | `benchmarks/ops/bench_mla_decode_fwd.py` | RENAME |
| mla_decode_paged_fwd | kernel | `-` | `tileops/kernels/mla_decode_paged_fwd/` | TODO |
| mla_decode_paged_fwd | op | `-` | `tileops/ops/mla_decode_paged_fwd.py` | TODO |
| mla_decode_paged_fwd | test | `-` | `tests/ops/test_mla_decode_paged_fwd.py` | TODO |
| mla_decode_paged_fwd | bench | `-` | `benchmarks/ops/bench_mla_decode_paged_fwd.py` | TODO |
| nsa_prefill_fwd | kernel | `tileops/kernels/deepseek_nsa/nsa_fwd.py`, `tileops/kernels/deepseek_nsa/nsa_cmp_fwd.py` | `tileops/kernels/nsa_prefill_fwd/` | RENAME |
| nsa_prefill_fwd | op | `tileops/ops/deepseek_nsa.py` | `tileops/ops/nsa_prefill_fwd.py` | RENAME |
| nsa_prefill_fwd | test | `tests/ops/test_deepseek_nsa_fwd.py::test_nsa_varlen_op`, `tests/ops/test_deepseek_nsa_cmp_fwd.py::test_nsa_cmp_fwd_varlen_op` | `tests/ops/test_nsa_prefill_fwd.py` | RENAME |
| nsa_prefill_fwd | bench | `benchmarks/ops/bench_deepseek_nsa_fwd.py::bench_nsa_fwd`, `benchmarks/ops/bench_deepseek_nsa_cmp_fwd.py::bench_nsa_cmp_fwd` | `benchmarks/ops/bench_nsa_prefill_fwd.py` | RENAME |
| nsa_decode_fwd | kernel | `-` | `tileops/kernels/nsa_decode_fwd/` | TODO |
| nsa_decode_fwd | op | `-` | `tileops/ops/nsa_decode_fwd.py` | TODO |
| nsa_decode_fwd | test | `-` | `tests/ops/test_nsa_decode_fwd.py` | TODO |
| nsa_decode_fwd | bench | `-` | `benchmarks/ops/bench_nsa_decode_fwd.py` | TODO |
| dsa_prefill_fwd | kernel | `-` | `tileops/kernels/dsa_prefill_fwd/` | TODO |
| dsa_prefill_fwd | op | `-` | `tileops/ops/dsa_prefill_fwd.py` | TODO |
| dsa_prefill_fwd | test | `-` | `tests/ops/test_dsa_prefill_fwd.py` | TODO |
| dsa_prefill_fwd | bench | `-` | `benchmarks/ops/bench_dsa_prefill_fwd.py` | TODO |
| dsa_decode_fwd | kernel | `tileops/kernels/deepseek_mla/deepseek_dsa_decode.py` | `tileops/kernels/dsa_decode_fwd/` | RENAME |
| dsa_decode_fwd | op | `tileops/ops/deepseek_dsa_decode.py` | `tileops/ops/dsa_decode_fwd.py` | RENAME |
| dsa_decode_fwd | test | `tests/ops/test_deepseek_dsa_decode.py::test_sparse_mla_decode` | `tests/ops/test_dsa_decode_fwd.py` | RENAME |
| dsa_decode_fwd | bench | `benchmarks/ops/bench_deepseek_dsa_decode.py::bench_dsa_decode` | `benchmarks/ops/bench_dsa_decode_fwd.py` | RENAME |

## Category: MoE (#404)

| Op | File Type | Current Path | Convention Path | Status |
|:---|:----------|:-------------|:----------------|:------:|
| permute_align | kernel | `tileops/kernels/moe/permute_align.py` | `tileops/kernels/permute_align/` | RENAME |
| permute_align | op | `-` | `tileops/ops/permute_align.py` | TODO |
| permute_align | test | `tests/ops/test_moe_permute_align.py::test_permute_align_op` | `tests/ops/test_permute_align.py` | RENAME |
| permute_align | bench | `benchmarks/ops/bench_moe_permute_align.py::bench_permute_align` | `benchmarks/ops/bench_permute_align.py` | RENAME |
| unpermute_depad | kernel | `-` | `tileops/kernels/unpermute_depad/` | TODO |
| unpermute_depad | op | `-` | `tileops/ops/unpermute_depad.py` | TODO |
| unpermute_depad | test | `-` | `tests/ops/test_unpermute_depad.py` | TODO |
| unpermute_depad | bench | `-` | `benchmarks/ops/bench_unpermute_depad.py` | TODO |
| fused_moe_deepseek | kernel | `-` | `tileops/kernels/fused_moe_deepseek/` | TODO |
| fused_moe_deepseek | op | `-` | `tileops/ops/fused_moe_deepseek.py` | TODO |
| fused_moe_deepseek | test | `-` | `tests/ops/test_fused_moe_deepseek.py` | TODO |
| fused_moe_deepseek | bench | `-` | `benchmarks/ops/bench_fused_moe_deepseek.py` | TODO |
| fused_moe_glm | kernel | `-` | `tileops/kernels/fused_moe_glm/` | TODO |
| fused_moe_glm | op | `-` | `tileops/ops/fused_moe_glm.py` | TODO |
| fused_moe_glm | test | `-` | `tests/ops/test_fused_moe_glm.py` | TODO |
| fused_moe_glm | bench | `-` | `benchmarks/ops/bench_fused_moe_glm.py` | TODO |
| fused_moe_kimi | kernel | `-` | `tileops/kernels/fused_moe_kimi/` | TODO |
| fused_moe_kimi | op | `-` | `tileops/ops/fused_moe_kimi.py` | TODO |
| fused_moe_kimi | test | `-` | `tests/ops/test_fused_moe_kimi.py` | TODO |
| fused_moe_kimi | bench | `-` | `benchmarks/ops/bench_fused_moe_kimi.py` | TODO |
| fused_moe_qwen | kernel | `-` | `tileops/kernels/fused_moe_qwen/` | TODO |
| fused_moe_qwen | op | `-` | `tileops/ops/fused_moe_qwen.py` | TODO |
| fused_moe_qwen | test | `-` | `tests/ops/test_fused_moe_qwen.py` | TODO |
| fused_moe_qwen | bench | `-` | `benchmarks/ops/bench_fused_moe_qwen.py` | TODO |

## Category: Linear Attention (#405)

| Op | File Type | Current Path | Convention Path | Status |
|:---|:----------|:-------------|:----------------|:------:|
| gated_deltanet_chunkwise | kernel | `tileops/kernels/linear_attn/gated_delta_net/gated_deltanet_fwd.py`, `tileops/kernels/linear_attn/gated_delta_net/gated_deltanet_bwd.py`, `tileops/kernels/linear_attn/gated_delta_net/fused_prepare_compute_w_u.py`, `tileops/kernels/linear_attn/gated_delta_net/compute_w_u_bwd.py` | `tileops/kernels/gated_deltanet_chunkwise/` | RENAME |
| gated_deltanet_chunkwise | op | `tileops/ops/gated_deltanet.py` | `tileops/ops/gated_deltanet_chunkwise.py` | RENAME |
| gated_deltanet_chunkwise | test | `tests/ops/test_gated_deltanet_fwd.py::test_gated_deltanet_fwd`, `tests/ops/test_gated_deltanet_bwd.py::test_gated_deltanet_bwd`, `tests/ops/test_fused_gated.py::test_fused_gated` | `tests/ops/test_gated_deltanet_chunkwise.py` | RENAME |
| gated_deltanet_chunkwise | bench | `benchmarks/ops/bench_gated_deltanet_vs_fla.py::bench_gated_deltanet_fwd`, `benchmarks/ops/bench_gated_deltanet_vs_fla.py::bench_gated_deltanet_bwd` | `benchmarks/ops/bench_gated_deltanet_chunkwise.py` | RENAME |
| gated_deltanet_recurrence | kernel | `tileops/kernels/linear_attn/gated_delta_net/gated_deltanet_decode.py` | `tileops/kernels/gated_deltanet_recurrence/` | RENAME |
| gated_deltanet_recurrence | op | `tileops/ops/gated_deltanet_decode.py` | `tileops/ops/gated_deltanet_recurrence.py` | RENAME |
| gated_deltanet_recurrence | test | `tests/ops/test_gated_deltanet_decode.py::test_gated_deltanet_decode`, `tests/ops/test_gated_deltanet_decode.py::test_gated_deltanet_decode_multi_step` | `tests/ops/test_gated_deltanet_recurrence.py` | RENAME |
| gated_deltanet_recurrence | bench | `benchmarks/ops/bench_gated_deltanet_decode.py::bench_gated_deltanet_decode` | `benchmarks/ops/bench_gated_deltanet_recurrence.py` | RENAME |
| deltanet_chunkwise | kernel | `-` | `tileops/kernels/deltanet_chunkwise/` | TODO |
| deltanet_chunkwise | op | `tileops/ops/engram_fwd.py` | `tileops/ops/deltanet_chunkwise.py` | RENAME |
| deltanet_chunkwise | test | `-` | `tests/ops/test_deltanet_chunkwise.py` | TODO |
| deltanet_chunkwise | bench | `-` | `benchmarks/ops/bench_deltanet_chunkwise.py` | TODO |
| deltanet_recurrence | kernel | `-` | `tileops/kernels/deltanet_recurrence/` | TODO |
| deltanet_recurrence | op | `tileops/ops/engram_decode.py` | `tileops/ops/deltanet_recurrence.py` | RENAME |
| deltanet_recurrence | test | `-` | `tests/ops/test_deltanet_recurrence.py` | TODO |
| deltanet_recurrence | bench | `-` | `benchmarks/ops/bench_deltanet_recurrence.py` | TODO |
| gla_chunkwise | kernel | `tileops/kernels/linear_attn/gla/gla_fwd.py`, `tileops/kernels/linear_attn/gla/gla_bwd.py` | `tileops/kernels/gla_chunkwise/` | RENAME |
| gla_chunkwise | op | `-` | `tileops/ops/gla_chunkwise.py` | TODO |
| gla_chunkwise | test | `tests/ops/test_gla_fwd.py::test_gla_fwd`, `tests/ops/test_gla_bwd.py::test_gla_bwd` | `tests/ops/test_gla_chunkwise.py` | RENAME |
| gla_chunkwise | bench | `benchmarks/ops/bench_gla.py::bench_gla_fwd`, `benchmarks/ops/bench_gla.py::bench_gla_bwd` | `benchmarks/ops/bench_gla_chunkwise.py` | RENAME |
| gla_recurrence | kernel | `tileops/kernels/linear_attn/gla/gla_decode.py` | `tileops/kernels/gla_recurrence/` | RENAME |
| gla_recurrence | op | `-` | `tileops/ops/gla_recurrence.py` | TODO |
| gla_recurrence | test | `tests/ops/test_gla_decode.py::test_gla_decode` | `tests/ops/test_gla_recurrence.py` | RENAME |
| gla_recurrence | bench | `benchmarks/ops/bench_gla_decode.py::bench_gla_decode` | `benchmarks/ops/bench_gla_recurrence.py` | RENAME |
| retnet_chunkwise | kernel | `-` | `tileops/kernels/retnet_chunkwise/` | TODO |
| retnet_chunkwise | op | `-` | `tileops/ops/retnet_chunkwise.py` | TODO |
| retnet_chunkwise | test | `-` | `tests/ops/test_retnet_chunkwise.py` | TODO |
| retnet_chunkwise | bench | `-` | `benchmarks/ops/bench_retnet_chunkwise.py` | TODO |
| retnet_recurrence | kernel | `-` | `tileops/kernels/retnet_recurrence/` | TODO |
| retnet_recurrence | op | `-` | `tileops/ops/retnet_recurrence.py` | TODO |
| retnet_recurrence | test | `-` | `tests/ops/test_retnet_recurrence.py` | TODO |
| retnet_recurrence | bench | `-` | `benchmarks/ops/bench_retnet_recurrence.py` | TODO |

## Category: SSM (#406)

| Op | File Type | Current Path | Convention Path | Status |
|:---|:----------|:-------------|:----------------|:------:|
| mamba1 | kernel | `-` | `tileops/kernels/mamba1/` | TODO |
| mamba1 | op | `-` | `tileops/ops/mamba1.py` | TODO |
| mamba1 | test | `-` | `tests/ops/test_mamba1.py` | TODO |
| mamba1 | bench | `-` | `benchmarks/ops/bench_mamba1.py` | TODO |
| mamba2 | kernel | `-` | `tileops/kernels/mamba2/` | TODO |
| mamba2 | op | `-` | `tileops/ops/mamba2.py` | TODO |
| mamba2 | test | `-` | `tests/ops/test_mamba2.py` | TODO |
| mamba2 | bench | `-` | `benchmarks/ops/bench_mamba2.py` | TODO |

---

## Summary

### Per Category

| Category | OK | RENAME | TODO | Total Entries |
|:---------|---:|-------:|-----:|--------------:|
| Elementwise (#397) | 3 | 257 | 28 | 288 |
| Reduce (#398) | 0 | 29 | 51 | 80 |
| Norm (#399) | 16 | 21 | 3 | 40 |
| Conv & Pooling (#402) | 0 | 0 | 64 | 64 |
| GEMM (#400) | 0 | 34 | 42 | 76 |
| Quantize (#401) | 0 | 6 | 34 | 40 |
| Sampling (#426) | 0 | 4 | 24 | 28 |
| Flash Attention (#403) | 0 | 32 | 32 | 64 |
| MoE (#404) | 0 | 3 | 21 | 24 |
| Linear Attention (#405) | 0 | 16 | 16 | 32 |
| SSM (#406) | 0 | 0 | 8 | 8 |

### Grand Total

| OK | RENAME | TODO | Total |
|---:|-------:|-----:|------:|
| 19 | 402 | 323 | 744 |

Total ops: 186 x 4 file types = 744 entries.
