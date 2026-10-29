discovered 60 benchmark files

=== [1/60] benchmarks/ops/bench_argreduce.py ===
RUNNING [1/60] 30s: benchmarks/ops/bench_argreduce.py::test_argmin_bench[3d-non-last-axis-float16]
benchmarks/ops/bench_argreduce.py::test_argmax_bench[lm-head-float16]
benchmarks/ops/bench_argreduce.py::test_argmax_bench[lm-head-bfloat16]
benchmarks/ops/bench_argreduce.py::test_argmax_bench[hidden-state-float16]
benchmarks/ops/bench_argreduce.py::test_argmax_bench[hidden-state-bfloat16]
benchmarks/ops/bench_argreduce.py::test_argmax_bench[3d-non-last-axis-float16]
benchmarks/ops/bench_argreduce.py::test_argmax_bench[llama-8b-lm-head-float32]
benchmarks/ops/bench_argreduce.py::test_argmin_bench[lm-head-float16]
benchmarks/ops/bench_argreduce.py::test_argmin_bench[lm-head-bfloat16]
benchmarks/ops/bench_argreduce.py::test_argmin_bench[hidden-state-float16]
benchmarks/ops/bench_argreduce.py::test_argmin_bench[hidden-state-bfloat16]
benchmarks/ops/bench_argreduce.py::test_argmin_bench[3d-non-last-axis-float16]
benchmarks/ops/bench_argreduce.py::test_argmin_bench[llama-8b-lm-head-float32]

12 tests collected in 3.55s
............                                                             [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_argreduce.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_argreduce.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
12 passed, 58 warnings in 24.07s
--- benchmarks/ops/bench_argreduce.py finished in 32s ---

=== [2/60] benchmarks/ops/bench_batch_norm.py ===
benchmarks/ops/bench_batch_norm.py::test_batch_norm_fwd_bench[resnet-fc-float16]
benchmarks/ops/bench_batch_norm.py::test_batch_norm_fwd_bench[resnet-stage1-float16]
benchmarks/ops/bench_batch_norm.py::test_batch_norm_fwd_bench[resnet-stage1-bfloat16]
benchmarks/ops/bench_batch_norm.py::test_batch_norm_fwd_bench[resnet-stage2-float16]
benchmarks/ops/bench_batch_norm.py::test_batch_norm_fwd_bench[resnet-stage3-float16]
benchmarks/ops/bench_batch_norm.py::test_batch_norm_fwd_bench[resnet-stage3-float32]
benchmarks/ops/bench_batch_norm.py::test_batch_norm_fwd_bench[large-spatial-float16]
benchmarks/ops/bench_batch_norm.py::test_batch_norm_fwd_bench[resnet-stage3-eval-float16]
benchmarks/ops/bench_batch_norm.py::test_batch_norm_fwd_bench[resnet-stem-bfloat16]
benchmarks/ops/bench_batch_norm.py::test_batch_norm_bwd_bench[resnet-fc-float16]
benchmarks/ops/bench_batch_norm.py::test_batch_norm_bwd_bench[resnet-stage1-float16]
benchmarks/ops/bench_batch_norm.py::test_batch_norm_bwd_bench[resnet-stage1-bfloat16]
benchmarks/ops/bench_batch_norm.py::test_batch_norm_bwd_bench[resnet-stage2-float16]
benchmarks/ops/bench_batch_norm.py::test_batch_norm_bwd_bench[resnet-stage3-float16]
benchmarks/ops/bench_batch_norm.py::test_batch_norm_bwd_bench[resnet-stage3-float32]
benchmarks/ops/bench_batch_norm.py::test_batch_norm_bwd_bench[large-spatial-float16]

16 tests collected in 2.11s
.........F......                                                         [100%]Benchmark report saved to profile_run.log

=================================== FAILURES ===================================
_________________ test_batch_norm_bwd_bench[resnet-fc-float16] _________________

reference = <bound method BatchNormBwdCall.ref_program of <workloads.norm.BatchNormBwdCall object at 0x7fb444f266f0>>
inputs = (tensor([[ 0.3467,  0.2318, -0.0622,  ...,  0.4216,  0.8433, -0.5674],
        [ 0.7695,  1.0566, -1.6660,  ..., -1.27...       0.9309, 0.9190, 1.2417, 0.9744, 0.9884, 1.1434, 0.9223, 0.8636, 1.2321,
        1.0042], device='cuda:0'), None)

    def verify(
        reference: Callable | None,
        inputs: tuple,
        *,
        evidence: Evidence,
        requests: dict[str, Request],
        preserve_reference_inputs: bool = False,
    ) -> dict[str, CheckResult]:
        """Check every request against one run of the reference, restoring inputs even on failure.
    
        The reference's result stays allocated while the requests run, so no request's output
        can reuse memory that already holds the expected values. Negative controls run once; a
        Custom probe runs once per request. A request marked ``preserve_inputs``, and the
        reference under ``preserve_reference_inputs``, must leave *inputs* unchanged, probes
        included, even where nothing is compared. A failure names its request. Reference OOM
        leaves every request unchecked; request failures always propagate.
        """
        if evidence.kind not in ("exact", "partial", "custom"):
            if preserve_reference_inputs and reference is not None:
                try:
                    check_inputs_preserved(Request(reference, inputs), inputs)
                except AssertionError as exc:
                    raise AssertionError(f"reference: {exc}") from exc
            _check_preserving(requests, inputs)
            return {name: CheckResult(0, None, None, describe(evidence)) for name in requests}
        if reference is None:
            raise ValueError(
                "a checked workload must supply ref_program; declare Unestablished explicitly"
            )
        shared = _unique(inputs)
        pristine = _snapshot(shared)
        try:
            try:
                try:
                    produced_by_reference = reference(*inputs)
                    expected = _copy_outputs(produced_by_reference)
                finally:
                    if preserve_reference_inputs:
                        _require_unchanged(shared, pristine)
            except torch.OutOfMemoryError:
                _restore(shared, pristine)
                _check_preserving(requests, inputs)
                return {
                    name: CheckResult(0, None, None, "reference ran out of memory") for name in requests
                }
            except AssertionError as exc:
                raise AssertionError(f"reference: {exc}") from exc
            _restore(shared, pristine)
            results = {}
            for name, request in requests.items():
                own = [t for t in _unique(request.args) if all(t is not s for s in shared)]
                own_pristine = _snapshot(own)
                try:
                    if request.reset is not None:
                        request.reset()
                    with torch.no_grad():
                        produced = _copy_outputs(request.run(*request.args))
                    if request.preserve_inputs:
                        _require_unchanged(shared, pristine)
>                   results[name] = compare_outputs(produced, expected, evidence)
                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

workloads/numerics.py:549: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
workloads/numerics.py:354: in compare_outputs
    list(_tensor_pairs(a, b)) for a, b in zip(outputs[:claimed], targets[:claimed], strict=True)
    ^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

got = tensor([], device='cuda:0')
expected = tensor([ -3.0743,  -5.4343,  -0.0729,   8.3093,   0.9296,   0.8550,   7.6754,
         -2.5599,   2.1214,   4.1019,  -...0086,
         -0.5668,   8.7757,  -5.9195,  -9.2598,  -0.2902,   4.2808,  11.9325,
          1.5757], device='cuda:0')

    def _tensor_pairs(got: Any, expected: Any):
        """Validate structure before any numerical strategy can accept an output."""
        if isinstance(expected, torch.Tensor):
            assert isinstance(got, torch.Tensor), "expected a tensor output"
>           assert got.shape == expected.shape, f"shape mismatch: {got.shape} != {expected.shape}"
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^
E           AssertionError: shape mismatch: torch.Size([0]) != torch.Size([64])

workloads/numerics.py:285: AssertionError

The above exception was the direct cause of the following exception:

case = Case(id='resnet-fc-float16')

    @pytest.mark.parametrize("case", bench.cases(BatchNormBwdOp), ids=lambda case: case.id)
    def test_batch_norm_bwd_bench(case):
        op = BatchNormBwdOp(**case.arguments)
>       bench.Runner(op, case).compare(
            {"torch-autograd": _torch_bn_bwd, "torch-native-batch-norm": _aten_bn_bwd}
        )

benchmarks/ops/bench_batch_norm.py:89: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
benchmarks/api.py:282: in compare
    checks = self._verify(plan)
             ^^^^^^^^^^^^^^^^^^
benchmarks/api.py:331: in _verify
    checks |= verify(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

reference = <bound method BatchNormBwdCall.ref_program of <workloads.norm.BatchNormBwdCall object at 0x7fb444f266f0>>
inputs = (tensor([[ 0.3467,  0.2318, -0.0622,  ...,  0.4216,  0.8433, -0.5674],
        [ 0.7695,  1.0566, -1.6660,  ..., -1.27...       0.9309, 0.9190, 1.2417, 0.9744, 0.9884, 1.1434, 0.9223, 0.8636, 1.2321,
        1.0042], device='cuda:0'), None)

    def verify(
        reference: Callable | None,
        inputs: tuple,
        *,
        evidence: Evidence,
        requests: dict[str, Request],
        preserve_reference_inputs: bool = False,
    ) -> dict[str, CheckResult]:
        """Check every request against one run of the reference, restoring inputs even on failure.
    
        The reference's result stays allocated while the requests run, so no request's output
        can reuse memory that already holds the expected values. Negative controls run once; a
        Custom probe runs once per request. A request marked ``preserve_inputs``, and the
        reference under ``preserve_reference_inputs``, must leave *inputs* unchanged, probes
        included, even where nothing is compared. A failure names its request. Reference OOM
        leaves every request unchecked; request failures always propagate.
        """
        if evidence.kind not in ("exact", "partial", "custom"):
            if preserve_reference_inputs and reference is not None:
                try:
                    check_inputs_preserved(Request(reference, inputs), inputs)
                except AssertionError as exc:
                    raise AssertionError(f"reference: {exc}") from exc
            _check_preserving(requests, inputs)
            return {name: CheckResult(0, None, None, describe(evidence)) for name in requests}
        if reference is None:
            raise ValueError(
                "a checked workload must supply ref_program; declare Unestablished explicitly"
            )
        shared = _unique(inputs)
        pristine = _snapshot(shared)
        try:
            try:
                try:
                    produced_by_reference = reference(*inputs)
                    expected = _copy_outputs(produced_by_reference)
                finally:
                    if preserve_reference_inputs:
                        _require_unchanged(shared, pristine)
            except torch.OutOfMemoryError:
                _restore(shared, pristine)
                _check_preserving(requests, inputs)
                return {
                    name: CheckResult(0, None, None, "reference ran out of memory") for name in requests
                }
            except AssertionError as exc:
                raise AssertionError(f"reference: {exc}") from exc
            _restore(shared, pristine)
            results = {}
            for name, request in requests.items():
                own = [t for t in _unique(request.args) if all(t is not s for s in shared)]
                own_pristine = _snapshot(own)
                try:
                    if request.reset is not None:
                        request.reset()
                    with torch.no_grad():
                        produced = _copy_outputs(request.run(*request.args))
                    if request.preserve_inputs:
                        _require_unchanged(shared, pristine)
                    results[name] = compare_outputs(produced, expected, evidence)
                    del produced
                    if isinstance(evidence, Custom) and evidence.probe is not None:
                        evidence.probe(request.run, request.args)
                        if request.preserve_inputs:
                            _require_unchanged(shared, pristine)
                except (AssertionError, ValueError) as exc:
>                   raise type(exc)(f"{name}: {exc}") from exc
E                   AssertionError: torch-native-batch-norm: shape mismatch: torch.Size([0]) != torch.Size([64])

workloads/numerics.py:556: AssertionError
=============================== warnings summary ===============================
benchmarks/ops/bench_batch_norm.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_batch_norm.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ============================
FAILED benchmarks/ops/bench_batch_norm.py::test_batch_norm_bwd_bench[resnet-fc-float16] - AssertionError: torch-native-batch-norm: shape mismatch: torch.Size([0]) != torch.Size([64])
1 failed, 15 passed, 58 warnings in 21.92s
--- benchmarks/ops/bench_batch_norm.py finished in 28s ---

=== [3/60] benchmarks/ops/bench_bmm.py ===
RUNNING [3/60] 30s: benchmarks/ops/bench_bmm.py::test_bmm_bench[square-128-float16]
RUNNING [3/60] 60s: benchmarks/ops/bench_bmm.py::test_bmm_bench[square-1k-bfloat16]
RUNNING [3/60] 90s: benchmarks/ops/bench_bmm.py::test_bmm_bench[square-256-bfloat16]
RUNNING [3/60] 120s: benchmarks/ops/bench_bmm.py::test_bmm_bench[square-2k-float16]
RUNNING [3/60] 150s: benchmarks/ops/bench_bmm.py::test_bmm_bench[mha-decode-qk-bfloat16]
RUNNING [3/60] 180s: benchmarks/ops/bench_bmm.py::test_bmm_bench[moe-prefill-bfloat16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[square-128-float16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[square-128-bfloat16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[square-1k-float16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[square-1k-bfloat16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[square-512-float16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[square-512-bfloat16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[square-256-float16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[square-256-bfloat16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[square-4k-bfloat16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[square-2k-float16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[square-2k-bfloat16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[mha-decode-qk-float16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[mha-decode-qk-bfloat16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[mha-decode-pv-float16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[mha-decode-pv-bfloat16]
benchmarks/ops/bench_bmm.py::test_bmm_bench[moe-prefill-bfloat16]
benchmarks/ops/bench_bmm.py::test_bmm_fp8_bench[square-1k-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_bmm.py::test_bmm_fp8_bench[square-2k-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_bmm.py::test_bmm_fp8_bench[mha-decode-pv-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_bmm.py::test_bmm_fp8_bench[mha-decode-qk-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_bmm.py::test_bmm_fp8_bench[moe-prefill-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_bmm.py::test_bmm_fp8_bench[square-1k-nk-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_bmm.py::test_bmm_fp8_bench[square-2k-nk-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_bmm.py::test_bmm_fp8_bench[mha-decode-pv-nk-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_bmm.py::test_bmm_fp8_bench[mha-decode-qk-nk-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_bmm.py::test_bmm_fp8_bench[moe-prefill-nk-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_bmm.py::test_bmm_fp8_bench[square-1k-float8_e4m3fn-float16]

27 tests collected in 3.80s
...........................                                              [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_bmm.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_bmm.py::test_bmm_fp8_bench[square-1k-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_bmm.py::test_bmm_fp8_bench[square-1k-float8_e4m3fn-float16]
  /home/ci-runner/runner/_work/TileOPs/TileOPs/src/tileops/_ops/gemm/bmm.py:172: UserWarning: BMMFP8FwdOp: b (shape=(4, 1024, 1024)) does not lie K-innermost, so it is transposed into a new buffer before the FP8 WGMMA kernel, which reads only that order. Passing b K-innermost skips the copy and is the faster call.
    b = self._as_k_innermost(b, a.dtype, a.device)

benchmarks/ops/bench_bmm.py::test_bmm_fp8_bench[square-2k-float8_e4m3fn-bfloat16]
  /home/ci-runner/runner/_work/TileOPs/TileOPs/src/tileops/_ops/gemm/bmm.py:172: UserWarning: BMMFP8FwdOp: b (shape=(8, 2048, 2048)) does not lie K-innermost, so it is transposed into a new buffer before the FP8 WGMMA kernel, which reads only that order. Passing b K-innermost skips the copy and is the faster call.
    b = self._as_k_innermost(b, a.dtype, a.device)

benchmarks/ops/bench_bmm.py::test_bmm_fp8_bench[mha-decode-pv-float8_e4m3fn-bfloat16]
  /home/ci-runner/runner/_work/TileOPs/TileOPs/src/tileops/_ops/gemm/bmm.py:172: UserWarning: BMMFP8FwdOp: b (shape=(32, 2048, 128)) does not lie K-innermost, so it is transposed into a new buffer before the FP8 WGMMA kernel, which reads only that order. Passing b K-innermost skips the copy and is the faster call.
    b = self._as_k_innermost(b, a.dtype, a.device)

benchmarks/ops/bench_bmm.py::test_bmm_fp8_bench[mha-decode-qk-float8_e4m3fn-bfloat16]
  /home/ci-runner/runner/_work/TileOPs/TileOPs/src/tileops/_ops/gemm/bmm.py:172: UserWarning: BMMFP8FwdOp: b (shape=(64, 128, 2048)) does not lie K-innermost, so it is transposed into a new buffer before the FP8 WGMMA kernel, which reads only that order. Passing b K-innermost skips the copy and is the faster call.
    b = self._as_k_innermost(b, a.dtype, a.device)

benchmarks/ops/bench_bmm.py::test_bmm_fp8_bench[moe-prefill-float8_e4m3fn-bfloat16]
  /home/ci-runner/runner/_work/TileOPs/TileOPs/src/tileops/_ops/gemm/bmm.py:172: UserWarning: BMMFP8FwdOp: b (shape=(128, 2048, 512)) does not lie K-innermost, so it is transposed into a new buffer before the FP8 WGMMA kernel, which reads only that order. Passing b K-innermost skips the copy and is the faster call.
    b = self._as_k_innermost(b, a.dtype, a.device)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
27 passed, 50 warnings in 184.62s (0:03:04)
--- benchmarks/ops/bench_bmm.py finished in 192s ---

=== [4/60] benchmarks/ops/bench_chain_speculative_sampling.py ===
RUNNING [4/60] 30s: benchmarks/ops/bench_chain_speculative_sampling.py::test_chain_speculative_sampling_bench[llama-8b-b16-n4]
RUNNING [4/60] 60s: benchmarks/ops/bench_chain_speculative_sampling.py::test_chain_speculative_sampling_bench[llama-8b-b16-n4]
RUNNING [4/60] 90s: benchmarks/ops/bench_chain_speculative_sampling.py::test_chain_speculative_sampling_bench[llama-8b-b16-n4]
RUNNING [4/60] 120s: benchmarks/ops/bench_chain_speculative_sampling.py::test_chain_speculative_sampling_bench[qwen3-235b-eagle-n5]
benchmarks/ops/bench_chain_speculative_sampling.py::test_chain_speculative_sampling_bench[llama-8b-b16-n4]
benchmarks/ops/bench_chain_speculative_sampling.py::test_chain_speculative_sampling_bench[llama-8b-b64-n4]
benchmarks/ops/bench_chain_speculative_sampling.py::test_chain_speculative_sampling_bench[ds-v3-mtp-n1]
benchmarks/ops/bench_chain_speculative_sampling.py::test_chain_speculative_sampling_bench[ds-v3-mtp-n3]
benchmarks/ops/bench_chain_speculative_sampling.py::test_chain_speculative_sampling_bench[qwen3-235b-eagle-n5]
benchmarks/ops/bench_chain_speculative_sampling.py::test_chain_speculative_sampling_bench[llama-8b-b17-n8]
benchmarks/ops/bench_chain_speculative_sampling.py::test_chain_speculative_sampling_bench[llama2-7b-b256-n1]

7 tests collected in 2.97s
.......                                                                  [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_chain_speculative_sampling.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
7 passed, 14 warnings in 123.94s (0:02:03)
--- benchmarks/ops/bench_chain_speculative_sampling.py finished in 131s ---

=== [5/60] benchmarks/ops/bench_convolution.py ===
RUNNING [5/60] 30s: benchmarks/ops/bench_convolution.py::test_conv2d_bench[midres-float16]
RUNNING [5/60] 60s: benchmarks/ops/bench_convolution.py::test_conv3d_bench[resnext-grouped-float16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[whisper-conv1-float16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[whisper-conv1-bfloat16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[wav2vec2-layer1-float16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[wav2vec2-layer1-bfloat16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[encodec-init-float16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[encodec-init-bfloat16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[encodec-deep-float16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[encodec-deep-bfloat16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[whisper-conv1-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[whisper-conv1-bias-bfloat16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[wav2vec2-layer1-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[wav2vec2-layer1-bias-bfloat16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[encodec-init-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[encodec-init-bias-bfloat16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[encodec-deep-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv1d_bench[encodec-deep-bias-bfloat16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[resnet-3x3-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[resnet-3x3-bfloat16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[stem-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[stage-down-3x3-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[highres-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[midres-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[stage-down-5x5-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[stride2-bfloat16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[resnet-1x1-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[resnet-1x1-bfloat16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[bottleneck-expand-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[bottleneck-reduce-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[late-stage-1x1-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[classifier-1x1-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[deeplabv3-aspp-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[mbv2-depthwise-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[resnext-grouped-3x3-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[resnet-3x3-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[resnet-3x3-bias-bfloat16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[stem-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[stage-down-3x3-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[highres-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[midres-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[stage-down-5x5-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[stride2-bias-bfloat16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[resnet-1x1-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[resnet-1x1-bias-bfloat16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[bottleneck-expand-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[bottleneck-reduce-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[late-stage-1x1-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv2d_bench[classifier-1x1-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv3d_bench[r3d-stem-float16]
benchmarks/ops/bench_convolution.py::test_conv3d_bench[video-down-float16]
benchmarks/ops/bench_convolution.py::test_conv3d_bench[unet-encoder-bfloat16]
benchmarks/ops/bench_convolution.py::test_conv3d_bench[unet-aspp-float16]
benchmarks/ops/bench_convolution.py::test_conv3d_bench[resnext-grouped-float16]
benchmarks/ops/bench_convolution.py::test_conv3d_bench[r3d-stem-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv3d_bench[video-down-bias-float16]
benchmarks/ops/bench_convolution.py::test_conv3d_bench[unet-encoder-bias-bfloat16]

55 tests collected in 3.12s
.......................................................                  [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_convolution.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

benchmarks/ops/bench_convolution.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
55 passed, 58 warnings in 62.00s (0:01:01)
--- benchmarks/ops/bench_convolution.py finished in 69s ---

=== [6/60] benchmarks/ops/bench_cumulative.py ===
benchmarks/ops/bench_cumulative.py::test_cumsum_bench[hidden-state-float16]
benchmarks/ops/bench_cumulative.py::test_cumsum_bench[hidden-state-bfloat16]
benchmarks/ops/bench_cumulative.py::test_cumsum_bench[hidden-state-f32-bfloat16-float32]
benchmarks/ops/bench_cumulative.py::test_cumsum_bench[long-seq-bfloat16]
benchmarks/ops/bench_cumulative.py::test_cumsum_bench[llama-13b-hidden-float32]
benchmarks/ops/bench_cumulative.py::test_cumprod_bench[hidden-state-float16]
benchmarks/ops/bench_cumulative.py::test_cumprod_bench[hidden-state-bfloat16]
benchmarks/ops/bench_cumulative.py::test_cumprod_bench[hidden-state-f32-bfloat16-float32]
benchmarks/ops/bench_cumulative.py::test_cumprod_bench[long-seq-bfloat16]
benchmarks/ops/bench_cumulative.py::test_cumprod_bench[llama-13b-hidden-float32]

10 tests collected in 3.23s
..F.......                                                               [100%]Benchmark report saved to profile_run.log

=================================== FAILURES ===================================
_____________ test_cumsum_bench[hidden-state-f32-bfloat16-float32] _____________

reference = <bound method CumulativeWorkload.ref_program of <workloads.reduction.CumulativeCall object at 0x7fe1a9a3b6b0>>
inputs = (tensor([[ 0.5469,  0.5430, -0.7227,  ...,  1.7500, -2.2969, -0.6133],
        [ 1.1172, -0.2910,  2.0781,  ...,  0.10...
        [ 0.0654,  0.0835,  0.6914,  ...,  0.2656, -0.6484,  0.0742]],
       device='cuda:0', dtype=torch.bfloat16),)

    def verify(
        reference: Callable | None,
        inputs: tuple,
        *,
        evidence: Evidence,
        requests: dict[str, Request],
        preserve_reference_inputs: bool = False,
    ) -> dict[str, CheckResult]:
        """Check every request against one run of the reference, restoring inputs even on failure.
    
        The reference's result stays allocated while the requests run, so no request's output
        can reuse memory that already holds the expected values. Negative controls run once; a
        Custom probe runs once per request. A request marked ``preserve_inputs``, and the
        reference under ``preserve_reference_inputs``, must leave *inputs* unchanged, probes
        included, even where nothing is compared. A failure names its request. Reference OOM
        leaves every request unchecked; request failures always propagate.
        """
        if evidence.kind not in ("exact", "partial", "custom"):
            if preserve_reference_inputs and reference is not None:
                try:
                    check_inputs_preserved(Request(reference, inputs), inputs)
                except AssertionError as exc:
                    raise AssertionError(f"reference: {exc}") from exc
            _check_preserving(requests, inputs)
            return {name: CheckResult(0, None, None, describe(evidence)) for name in requests}
        if reference is None:
            raise ValueError(
                "a checked workload must supply ref_program; declare Unestablished explicitly"
            )
        shared = _unique(inputs)
        pristine = _snapshot(shared)
        try:
            try:
                try:
                    produced_by_reference = reference(*inputs)
                    expected = _copy_outputs(produced_by_reference)
                finally:
                    if preserve_reference_inputs:
                        _require_unchanged(shared, pristine)
            except torch.OutOfMemoryError:
                _restore(shared, pristine)
                _check_preserving(requests, inputs)
                return {
                    name: CheckResult(0, None, None, "reference ran out of memory") for name in requests
                }
            except AssertionError as exc:
                raise AssertionError(f"reference: {exc}") from exc
            _restore(shared, pristine)
            results = {}
            for name, request in requests.items():
                own = [t for t in _unique(request.args) if all(t is not s for s in shared)]
                own_pristine = _snapshot(own)
                try:
                    if request.reset is not None:
                        request.reset()
                    with torch.no_grad():
                        produced = _copy_outputs(request.run(*request.args))
                    if request.preserve_inputs:
                        _require_unchanged(shared, pristine)
>                   results[name] = compare_outputs(produced, expected, evidence)
                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

workloads/numerics.py:549: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
workloads/numerics.py:354: in compare_outputs
    list(_tensor_pairs(a, b)) for a, b in zip(outputs[:claimed], targets[:claimed], strict=True)
    ^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

got = tensor([[  0.5469,   1.0938,   0.3672,  ..., -29.8750, -32.0000, -32.7500],
        [  1.1172,   0.8281,   2.9062,  .....     [  0.0654,   0.1484,   0.8398,  ..., -15.6250, -16.2500, -16.2500]],
       device='cuda:0', dtype=torch.bfloat16)
expected = tensor([[  0.5469,   1.0898,   0.3672,  ..., -29.8253, -32.1222, -32.7354],
        [  1.1172,   0.8262,   2.9043,  .....3.5808,   4.5730],
        [  0.0654,   0.1489,   0.8403,  ..., -15.6221, -16.2706, -16.1964]],
       device='cuda:0')

    def _tensor_pairs(got: Any, expected: Any):
        """Validate structure before any numerical strategy can accept an output."""
        if isinstance(expected, torch.Tensor):
            assert isinstance(got, torch.Tensor), "expected a tensor output"
            assert got.shape == expected.shape, f"shape mismatch: {got.shape} != {expected.shape}"
>           assert got.dtype == expected.dtype, f"dtype mismatch: {got.dtype} != {expected.dtype}"
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^
E           AssertionError: dtype mismatch: torch.bfloat16 != torch.float32

workloads/numerics.py:286: AssertionError

The above exception was the direct cause of the following exception:

case = Case(id='hidden-state-f32-bfloat16-float32')

    @pytest.mark.parametrize("case", bench.cases(CumsumFwdOp), ids=lambda case: case.id)
    def test_cumsum_bench(case) -> None:
        op = CumsumFwdOp(**case.arguments)
        flaggems_cumsum = flaggems_op("cumsum")
        dim = case.workload.dim
    
        def flaggems_fn(x):
            return flaggems_cumsum(x, dim)
    
        torch_cumsum = case.torch
        if case.inputs[0].dtype == torch.bfloat16:
            torch_cumsum = bench.Implementation(
                torch_cumsum, noncomparable_reason="torch accumulates a bfloat16 cumsum in bfloat16"
            )
>       bench.Runner(op, case).compare(
            {
                FLAGGEMS_TAG: flaggems_fn,
                "torch": torch_cumsum,
                TORCH_COMPILE_TAG: compiled_reference(case.torch),
            }
        )

benchmarks/ops/bench_cumulative.py:33: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
benchmarks/api.py:282: in compare
    checks = self._verify(plan)
             ^^^^^^^^^^^^^^^^^^
benchmarks/api.py:331: in _verify
    checks |= verify(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

reference = <bound method CumulativeWorkload.ref_program of <workloads.reduction.CumulativeCall object at 0x7fe1a9a3b6b0>>
inputs = (tensor([[ 0.5469,  0.5430, -0.7227,  ...,  1.7500, -2.2969, -0.6133],
        [ 1.1172, -0.2910,  2.0781,  ...,  0.10...
        [ 0.0654,  0.0835,  0.6914,  ...,  0.2656, -0.6484,  0.0742]],
       device='cuda:0', dtype=torch.bfloat16),)

    def verify(
        reference: Callable | None,
        inputs: tuple,
        *,
        evidence: Evidence,
        requests: dict[str, Request],
        preserve_reference_inputs: bool = False,
    ) -> dict[str, CheckResult]:
        """Check every request against one run of the reference, restoring inputs even on failure.
    
        The reference's result stays allocated while the requests run, so no request's output
        can reuse memory that already holds the expected values. Negative controls run once; a
        Custom probe runs once per request. A request marked ``preserve_inputs``, and the
        reference under ``preserve_reference_inputs``, must leave *inputs* unchanged, probes
        included, even where nothing is compared. A failure names its request. Reference OOM
        leaves every request unchecked; request failures always propagate.
        """
        if evidence.kind not in ("exact", "partial", "custom"):
            if preserve_reference_inputs and reference is not None:
                try:
                    check_inputs_preserved(Request(reference, inputs), inputs)
                except AssertionError as exc:
                    raise AssertionError(f"reference: {exc}") from exc
            _check_preserving(requests, inputs)
            return {name: CheckResult(0, None, None, describe(evidence)) for name in requests}
        if reference is None:
            raise ValueError(
                "a checked workload must supply ref_program; declare Unestablished explicitly"
            )
        shared = _unique(inputs)
        pristine = _snapshot(shared)
        try:
            try:
                try:
                    produced_by_reference = reference(*inputs)
                    expected = _copy_outputs(produced_by_reference)
                finally:
                    if preserve_reference_inputs:
                        _require_unchanged(shared, pristine)
            except torch.OutOfMemoryError:
                _restore(shared, pristine)
                _check_preserving(requests, inputs)
                return {
                    name: CheckResult(0, None, None, "reference ran out of memory") for name in requests
                }
            except AssertionError as exc:
                raise AssertionError(f"reference: {exc}") from exc
            _restore(shared, pristine)
            results = {}
            for name, request in requests.items():
                own = [t for t in _unique(request.args) if all(t is not s for s in shared)]
                own_pristine = _snapshot(own)
                try:
                    if request.reset is not None:
                        request.reset()
                    with torch.no_grad():
                        produced = _copy_outputs(request.run(*request.args))
                    if request.preserve_inputs:
                        _require_unchanged(shared, pristine)
                    results[name] = compare_outputs(produced, expected, evidence)
                    del produced
                    if isinstance(evidence, Custom) and evidence.probe is not None:
                        evidence.probe(request.run, request.args)
                        if request.preserve_inputs:
                            _require_unchanged(shared, pristine)
                except (AssertionError, ValueError) as exc:
>                   raise type(exc)(f"{name}: {exc}") from exc
E                   AssertionError: flaggems: dtype mismatch: torch.bfloat16 != torch.float32

workloads/numerics.py:556: AssertionError
----------------------------- Captured stdout call -----------------------------
2026-10-25 17:09:51  [TileLang:tilelang.jit.kernel:INFO] (kernel.py:129): TileLang begins to compile kernel `main` with `out_idx=[1]`
2026-10-25 17:09:51  [TileLang:tilelang.jit.kernel:INFO] (kernel.py:137): TileLang completes to compile kernel `main`
=============================== warnings summary ===============================
benchmarks/ops/bench_cumulative.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_cumulative.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ============================
FAILED benchmarks/ops/bench_cumulative.py::test_cumsum_bench[hidden-state-f32-bfloat16-float32] - AssertionError: flaggems: dtype mismatch: torch.bfloat16 != torch.float32
1 failed, 9 passed, 58 warnings in 19.88s
--- benchmarks/ops/bench_cumulative.py finished in 27s ---

=== [7/60] benchmarks/ops/bench_deltanet.py ===
RUNNING [7/60] 30s: benchmarks/ops/bench_deltanet.py::test_deltanet_fwd_bench[varlen-4x1k-bfloat16]
RUNNING [7/60] 60s: benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_bwd[train-4k-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_fwd_bench[prefill-2k-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_fwd_bench[prefill-8k-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_fwd_bench[prefill-16k-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_fwd_bench[prefill-4k-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_fwd_bench[prefill-12k-continued-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_fwd_bench[decode-continued-float16]
benchmarks/ops/bench_deltanet.py::test_deltanet_fwd_bench[decode-continued-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_fwd_bench[varlen-4x1k-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_fwd_bench[varlen-ragged-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_fwd_bench[prefill-3000-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_fwd_bench[prefill-l2norm-4k-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_fwd_bench[prefill-l2norm-ragged-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_fwd_bench[decode-fresh-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_fwd_bench[decode-l2norm-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_fwd_bench[decode-narrow-b17-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_fwd_bench[deltanet-1.3b-continue-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_fwd_bench[deltanet-1.3b-decode-b32-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_fwd_bench[deltanet-1.3b-cont-b4-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_fwd[train-2k-float16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_fwd[train-2k-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_fwd[train-4k-float16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_fwd[train-4k-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_fwd[train-8k-float16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_fwd[train-8k-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_fwd[train-16k-float16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_fwd[train-16k-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_fwd[deltanet-1.3b-train-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_bwd[train-2k-float16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_bwd[train-2k-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_bwd[train-4k-float16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_bwd[train-4k-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_bwd[train-8k-float16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_bwd[train-8k-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_bwd[train-16k-float16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_bwd[train-16k-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_vs_fla_bwd[deltanet-1.3b-train-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_decode_bench[serving-b1-h8-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_decode_bench[serving-b1-h16-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_decode_bench[serving-b1-h32-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_decode_bench[serving-b1-h48-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_decode_bench[serving-b1-h64-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_decode_bench[serving-b8-h32-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_decode_bench[serving-b8-h48-bfloat16]
benchmarks/ops/bench_deltanet.py::test_deltanet_decode_bench[serving-b8-h64-bfloat16]

44 tests collected in 5.04s
............................................                             [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_deltanet.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
44 passed, 14 warnings in 75.81s (0:01:15)
--- benchmarks/ops/bench_deltanet.py finished in 85s ---

=== [8/60] benchmarks/ops/bench_dsa_decode.py ===
RUNNING [8/60] 30s: collecting tests
RUNNING [8/60] 60s: collecting tests
RUNNING [8/60] 90s: benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[ds-v32-kv2k-float16]
RUNNING [8/60] 120s: benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[ds-v32-kv4k-float16]
RUNNING [8/60] 150s: benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[mla-d576-h128-kv8k-bfloat16]
RUNNING [8/60] 180s: benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[mla-d576-h128-kv32k-bfloat16]
RUNNING [8/60] 210s: benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[mla-d576-h128-kv32k-bfloat16]
RUNNING [8/60] 240s: benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[mla-d576-h128-kv64k-bfloat16]
RUNNING [8/60] 270s: benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[mla-d576-h128-kv96k-bfloat16]
RUNNING [8/60] 300s: benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[mla-d576-h128-kv128k-bfloat16]
RUNNING [8/60] 330s: benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[mla-d512-h64-kv8k-bfloat16]
RUNNING [8/60] 360s: benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[mla-d512-h64-kv48k-bfloat16]
RUNNING [8/60] 391s: benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[mla-d512-h128-kv8k-bfloat16]
RUNNING [8/60] 421s: benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[mla-d512-h128-kv32k-bfloat16]
RUNNING [8/60] 451s: benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[mla-d512-h128-kv64k-bfloat16]
benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[ds-v32-kv2k-float16]
benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[ds-v32-kv2k-bfloat16]
benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[ds-v32-kv4k-float16]
benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[ds-v32-kv4k-bfloat16]
benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[mla-d576-h128-kv8k-bfloat16]
benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[mla-d576-h128-kv32k-bfloat16]
benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[mla-d576-h128-kv64k-bfloat16]
benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[mla-d576-h128-kv96k-bfloat16]
benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[mla-d576-h128-kv128k-bfloat16]
benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[mla-d512-h64-kv8k-bfloat16]
benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[mla-d512-h64-kv32k-bfloat16]
benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[mla-d512-h64-kv48k-bfloat16]
benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[mla-d512-h64-kv64k-bfloat16]
benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[mla-d512-h128-kv8k-bfloat16]
benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[mla-d512-h128-kv32k-bfloat16]
benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[mla-d512-h128-kv48k-bfloat16]
benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[mla-d512-h128-kv64k-bfloat16]

17 tests collected in 73.20s (0:01:13)
.................                                                        [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_dsa_decode.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

benchmarks/ops/bench_dsa_decode.py::test_dsa_decode_bench[ds-v32-kv2k-float16]
  /usr/local/lib/python3.12/dist-packages/torch/_inductor/compile_fx.py:321: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
17 passed, 15 warnings in 394.93s (0:06:34)
--- benchmarks/ops/bench_dsa_decode.py finished in 479s ---

=== [9/60] benchmarks/ops/bench_dsa_paged.py ===
RUNNING [9/60] 30s: benchmarks/ops/bench_dsa_paged.py::test_dsa_paged_bench[ds-v32-tp2-1k]
benchmarks/ops/bench_dsa_paged.py::test_dsa_paged_bench[ds-v32-32k]
benchmarks/ops/bench_dsa_paged.py::test_dsa_paged_bench[ds-v32-mtp-128k]
benchmarks/ops/bench_dsa_paged.py::test_dsa_paged_bench[ds-v32-tp2-1k]

3 tests collected in 5.66s
...                                                                      [100%]Benchmark report saved to profile_run.log

3 passed in 27.16s
--- benchmarks/ops/bench_dsa_paged.py finished in 37s ---

=== [10/60] benchmarks/ops/bench_elementwise.py ===
RUNNING [10/60] 30s: benchmarks/ops/bench_elementwise.py::test_sub_bench[cnn-feat-broadcast-float32]
RUNNING [10/60] 60s: benchmarks/ops/bench_elementwise.py::test_remainder_bench[linear-bias-float32]
RUNNING [10/60] 90s: benchmarks/ops/bench_elementwise.py::test_lerp_bench[linear-bias-float16]
RUNNING [10/60] 120s: benchmarks/ops/bench_elementwise.py::test_minimum_bench[cnn-feat-broadcast-float32]
RUNNING [10/60] 150s: benchmarks/ops/bench_elementwise.py::test_eq_bench[llama-7b-hidden-float16]
RUNNING [10/60] 180s: benchmarks/ops/bench_elementwise.py::test_gt_bench[cnn-feat-broadcast-float32]
RUNNING [10/60] 210s: benchmarks/ops/bench_elementwise.py::test_lt_bench[linear-bias-float32]
RUNNING [10/60] 240s: benchmarks/ops/bench_elementwise.py::test_le_bench[cnn-feat-broadcast-float16]
RUNNING [10/60] 270s: benchmarks/ops/bench_elementwise.py::test_logical_and_bench[cnn-feat-broadcast-bfloat16]
RUNNING [10/60] 300s: benchmarks/ops/bench_elementwise.py::test_logical_or_bench[cnn-feat-broadcast-bool]
RUNNING [10/60] 330s: benchmarks/ops/bench_elementwise.py::test_bitwise_and_bench[hidden-state-prefill-int32]
RUNNING [10/60] 360s: benchmarks/ops/bench_elementwise.py::test_bitwise_or_bench[hidden-state-prefill-int64]
RUNNING [10/60] 391s: benchmarks/ops/bench_elementwise.py::test_bitwise_xor_bench[cnn-feat-broadcast-int32]
RUNNING [10/60] 421s: benchmarks/ops/bench_elementwise.py::test_alibi_bench[mpt-7b-4k-bfloat16]
RUNNING [10/60] 451s: benchmarks/ops/bench_elementwise.py::test_where_bench[256M-bfloat16]
RUNNING [10/60] 481s: benchmarks/ops/bench_elementwise.py::test_silu_bench[llama-8b-ffn-prefill-bfloat16]
RUNNING [10/60] 511s: benchmarks/ops/bench_elementwise.py::test_mish_bench[yolo-p4-float16]
RUNNING [10/60] 541s: benchmarks/ops/bench_elementwise.py::test_elu_bench[mlp-hidden-wide-float16]
RUNNING [10/60] 571s: benchmarks/ops/bench_elementwise.py::test_clamp_bench[256M-float16]
RUNNING [10/60] 601s: benchmarks/ops/bench_elementwise.py::test_clamp_bench[256M-max-only-bfloat16]
RUNNING [10/60] 631s: benchmarks/ops/bench_elementwise.py::test_nan_to_num_bench[256M-bfloat16]
RUNNING [10/60] 661s: benchmarks/ops/bench_elementwise.py::test_sqrt_bench[16M-float16]
RUNNING [10/60] 691s: benchmarks/ops/bench_elementwise.py::test_abs_bench[16M-float16]
RUNNING [10/60] 721s: benchmarks/ops/bench_elementwise.py::test_reciprocal_bench[16M-float16]
RUNNING [10/60] 751s: benchmarks/ops/bench_elementwise.py::test_sin_bench[16M-float16]
RUNNING [10/60] 781s: benchmarks/ops/bench_elementwise.py::test_floor_bench[16M-float16]
RUNNING [10/60] 811s: benchmarks/ops/bench_elementwise.py::test_round_bench[16M-float16]
RUNNING [10/60] 841s: benchmarks/ops/bench_elementwise.py::test_erf_bench[16M-float16]
RUNNING [10/60] 871s: benchmarks/ops/bench_elementwise.py::test_expm1_bench[16M-float16]
RUNNING [10/60] 901s: benchmarks/ops/bench_elementwise.py::test_tanh_bench[16M-float16]
RUNNING [10/60] 931s: benchmarks/ops/bench_elementwise.py::test_bitwise_not_bench[16M-int64]
RUNNING [10/60] 961s: benchmarks/ops/bench_elementwise.py::test_isinf_bench[256M-float16]
RUNNING [10/60] 991s: benchmarks/ops/bench_elementwise.py::test_dropout_bench[hidden-4k-float16]
benchmarks/ops/bench_elementwise.py::test_prelu_bench[cnn-feat-float16]
benchmarks/ops/bench_elementwise.py::test_prelu_bench[cnn-feat-bfloat16]
benchmarks/ops/bench_elementwise.py::test_prelu_bench[cnn-feat-deep-float16]
benchmarks/ops/bench_elementwise.py::test_prelu_bench[cnn-feat-deep-bfloat16]
benchmarks/ops/bench_elementwise.py::test_masked_fill_bench[16M-float16]
benchmarks/ops/bench_elementwise.py::test_masked_fill_bench[16M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_masked_fill_bench[16M-float32]
benchmarks/ops/bench_elementwise.py::test_masked_fill_bench[256M-float16]
benchmarks/ops/bench_elementwise.py::test_masked_fill_bench[256M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_masked_fill_scalar_bench[16M-float16]
benchmarks/ops/bench_elementwise.py::test_masked_fill_scalar_bench[16M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_masked_fill_scalar_bench[16M-float32]
benchmarks/ops/bench_elementwise.py::test_masked_fill_scalar_bench[256M-float16]
benchmarks/ops/bench_elementwise.py::test_masked_fill_scalar_bench[256M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_add_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise.py::test_add_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise.py::test_add_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise.py::test_add_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise.py::test_add_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise.py::test_add_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise.py::test_add_bench[llama-7b-ffn-float16]
benchmarks/ops/bench_elementwise.py::test_add_bench[llama-7b-ffn-bfloat16]
benchmarks/ops/bench_elementwise.py::test_add_bench[llama-7b-ffn-float32]
benchmarks/ops/bench_elementwise.py::test_add_bench[linear-bias-float16]
benchmarks/ops/bench_elementwise.py::test_add_bench[linear-bias-bfloat16]
benchmarks/ops/bench_elementwise.py::test_add_bench[linear-bias-float32]
benchmarks/ops/bench_elementwise.py::test_sub_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise.py::test_sub_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise.py::test_sub_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise.py::test_sub_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise.py::test_sub_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise.py::test_sub_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise.py::test_sub_bench[llama-7b-ffn-float16]
benchmarks/ops/bench_elementwise.py::test_sub_bench[llama-7b-ffn-bfloat16]
benchmarks/ops/bench_elementwise.py::test_sub_bench[llama-7b-ffn-float32]
benchmarks/ops/bench_elementwise.py::test_sub_bench[linear-bias-float16]
benchmarks/ops/bench_elementwise.py::test_sub_bench[linear-bias-bfloat16]
benchmarks/ops/bench_elementwise.py::test_sub_bench[linear-bias-float32]
benchmarks/ops/bench_elementwise.py::test_sub_bench[llama-7b-hidden-float16]
benchmarks/ops/bench_elementwise.py::test_sub_bench[phi-2-ffn-float16]
benchmarks/ops/bench_elementwise.py::test_sub_bench[phi-2-ffn-bias-float16]
benchmarks/ops/bench_elementwise.py::test_sub_bench[llama-7b-ffn-bias-float16]
benchmarks/ops/bench_elementwise.py::test_mul_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise.py::test_mul_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise.py::test_mul_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise.py::test_mul_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise.py::test_mul_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise.py::test_mul_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise.py::test_mul_bench[llama-7b-ffn-float16]
benchmarks/ops/bench_elementwise.py::test_mul_bench[llama-7b-ffn-bfloat16]
benchmarks/ops/bench_elementwise.py::test_mul_bench[llama-7b-ffn-float32]
benchmarks/ops/bench_elementwise.py::test_mul_bench[linear-bias-float16]
benchmarks/ops/bench_elementwise.py::test_mul_bench[linear-bias-bfloat16]
benchmarks/ops/bench_elementwise.py::test_mul_bench[linear-bias-float32]
benchmarks/ops/bench_elementwise.py::test_mul_bench[llama-7b-hidden-float16]
benchmarks/ops/bench_elementwise.py::test_mul_bench[phi-2-ffn-float16]
benchmarks/ops/bench_elementwise.py::test_mul_bench[phi-2-ffn-bias-float16]
benchmarks/ops/bench_elementwise.py::test_mul_bench[llama-7b-ffn-bias-float16]
benchmarks/ops/bench_elementwise.py::test_div_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise.py::test_div_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise.py::test_div_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise.py::test_div_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise.py::test_div_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise.py::test_div_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise.py::test_div_bench[llama-7b-ffn-float16]
benchmarks/ops/bench_elementwise.py::test_div_bench[llama-7b-ffn-bfloat16]
benchmarks/ops/bench_elementwise.py::test_div_bench[llama-7b-ffn-float32]
benchmarks/ops/bench_elementwise.py::test_div_bench[linear-bias-float16]
benchmarks/ops/bench_elementwise.py::test_div_bench[linear-bias-bfloat16]
benchmarks/ops/bench_elementwise.py::test_div_bench[linear-bias-float32]
benchmarks/ops/bench_elementwise.py::test_div_bench[llama-7b-hidden-float16]
benchmarks/ops/bench_elementwise.py::test_div_bench[phi-2-ffn-float16]
benchmarks/ops/bench_elementwise.py::test_div_bench[phi-2-ffn-bias-float16]
benchmarks/ops/bench_elementwise.py::test_div_bench[llama-7b-ffn-bias-float16]
benchmarks/ops/bench_elementwise.py::test_remainder_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise.py::test_remainder_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise.py::test_remainder_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise.py::test_remainder_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise.py::test_remainder_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise.py::test_remainder_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise.py::test_remainder_bench[llama-7b-ffn-float16]
benchmarks/ops/bench_elementwise.py::test_remainder_bench[llama-7b-ffn-bfloat16]
benchmarks/ops/bench_elementwise.py::test_remainder_bench[llama-7b-ffn-float32]
benchmarks/ops/bench_elementwise.py::test_remainder_bench[linear-bias-float16]
benchmarks/ops/bench_elementwise.py::test_remainder_bench[linear-bias-bfloat16]
benchmarks/ops/bench_elementwise.py::test_remainder_bench[linear-bias-float32]
benchmarks/ops/bench_elementwise.py::test_remainder_bench[llama-7b-hidden-float16]
benchmarks/ops/bench_elementwise.py::test_remainder_bench[phi-2-ffn-float16]
benchmarks/ops/bench_elementwise.py::test_pow_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise.py::test_pow_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise.py::test_pow_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise.py::test_pow_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise.py::test_pow_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise.py::test_pow_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise.py::test_pow_bench[llama-7b-ffn-float16]
benchmarks/ops/bench_elementwise.py::test_pow_bench[llama-7b-ffn-bfloat16]
benchmarks/ops/bench_elementwise.py::test_pow_bench[llama-7b-ffn-float32]
benchmarks/ops/bench_elementwise.py::test_pow_bench[linear-bias-float16]
benchmarks/ops/bench_elementwise.py::test_pow_bench[linear-bias-bfloat16]
benchmarks/ops/bench_elementwise.py::test_pow_bench[linear-bias-float32]
benchmarks/ops/bench_elementwise.py::test_pow_bench[llama-7b-hidden-float16]
benchmarks/ops/bench_elementwise.py::test_pow_bench[phi-2-ffn-float16]
benchmarks/ops/bench_elementwise.py::test_floor_divide_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise.py::test_floor_divide_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise.py::test_floor_divide_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise.py::test_floor_divide_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise.py::test_floor_divide_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise.py::test_floor_divide_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise.py::test_floor_divide_bench[llama-7b-ffn-float16]
benchmarks/ops/bench_elementwise.py::test_floor_divide_bench[llama-7b-ffn-bfloat16]
benchmarks/ops/bench_elementwise.py::test_floor_divide_bench[llama-7b-ffn-float32]
benchmarks/ops/bench_elementwise.py::test_floor_divide_bench[linear-bias-float16]
benchmarks/ops/bench_elementwise.py::test_floor_divide_bench[linear-bias-bfloat16]
benchmarks/ops/bench_elementwise.py::test_floor_divide_bench[linear-bias-float32]
benchmarks/ops/bench_elementwise.py::test_floor_divide_bench[llama-7b-hidden-float16]
benchmarks/ops/bench_elementwise.py::test_floor_divide_bench[phi-2-ffn-float16]
benchmarks/ops/bench_elementwise.py::test_lerp_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise.py::test_lerp_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise.py::test_lerp_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise.py::test_lerp_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise.py::test_lerp_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise.py::test_lerp_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise.py::test_lerp_bench[llama-7b-ffn-float16]
benchmarks/ops/bench_elementwise.py::test_lerp_bench[llama-7b-ffn-bfloat16]
benchmarks/ops/bench_elementwise.py::test_lerp_bench[llama-7b-ffn-float32]
benchmarks/ops/bench_elementwise.py::test_lerp_bench[linear-bias-float16]
benchmarks/ops/bench_elementwise.py::test_lerp_bench[linear-bias-bfloat16]
benchmarks/ops/bench_elementwise.py::test_lerp_bench[linear-bias-float32]
benchmarks/ops/bench_elementwise.py::test_lerp_bench[llama-7b-hidden-float16]
benchmarks/ops/bench_elementwise.py::test_lerp_bench[phi-2-ffn-float16]
benchmarks/ops/bench_elementwise.py::test_maximum_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise.py::test_maximum_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise.py::test_maximum_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise.py::test_maximum_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise.py::test_maximum_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise.py::test_maximum_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise.py::test_maximum_bench[llama-7b-ffn-float16]
benchmarks/ops/bench_elementwise.py::test_maximum_bench[llama-7b-ffn-bfloat16]
benchmarks/ops/bench_elementwise.py::test_maximum_bench[llama-7b-ffn-float32]
benchmarks/ops/bench_elementwise.py::test_maximum_bench[linear-bias-float16]
benchmarks/ops/bench_elementwise.py::test_maximum_bench[linear-bias-bfloat16]
benchmarks/ops/bench_elementwise.py::test_maximum_bench[linear-bias-float32]
benchmarks/ops/bench_elementwise.py::test_maximum_bench[llama-7b-hidden-float16]
benchmarks/ops/bench_elementwise.py::test_maximum_bench[phi-2-ffn-float16]
benchmarks/ops/bench_elementwise.py::test_minimum_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise.py::test_minimum_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise.py::test_minimum_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise.py::test_minimum_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise.py::test_minimum_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise.py::test_minimum_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise.py::test_minimum_bench[llama-7b-ffn-float16]
benchmarks/ops/bench_elementwise.py::test_minimum_bench[llama-7b-ffn-bfloat16]
benchmarks/ops/bench_elementwise.py::test_minimum_bench[llama-7b-ffn-float32]
benchmarks/ops/bench_elementwise.py::test_minimum_bench[linear-bias-float16]
benchmarks/ops/bench_elementwise.py::test_minimum_bench[linear-bias-bfloat16]
benchmarks/ops/bench_elementwise.py::test_minimum_bench[linear-bias-float32]
benchmarks/ops/bench_elementwise.py::test_minimum_bench[llama-7b-hidden-float16]
benchmarks/ops/bench_elementwise.py::test_minimum_bench[phi-2-ffn-float16]
benchmarks/ops/bench_elementwise.py::test_eq_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise.py::test_eq_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise.py::test_eq_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise.py::test_eq_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise.py::test_eq_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise.py::test_eq_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise.py::test_eq_bench[llama-7b-ffn-float16]
benchmarks/ops/bench_elementwise.py::test_eq_bench[llama-7b-ffn-bfloat16]
benchmarks/ops/bench_elementwise.py::test_eq_bench[llama-7b-ffn-float32]
benchmarks/ops/bench_elementwise.py::test_eq_bench[linear-bias-float16]
benchmarks/ops/bench_elementwise.py::test_eq_bench[linear-bias-bfloat16]
benchmarks/ops/bench_elementwise.py::test_eq_bench[linear-bias-float32]
benchmarks/ops/bench_elementwise.py::test_eq_bench[llama-7b-hidden-float16]
benchmarks/ops/bench_elementwise.py::test_eq_bench[phi-2-ffn-float16]
benchmarks/ops/bench_elementwise.py::test_ne_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise.py::test_ne_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise.py::test_ne_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise.py::test_ne_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise.py::test_ne_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise.py::test_ne_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise.py::test_ne_bench[llama-7b-ffn-float16]
benchmarks/ops/bench_elementwise.py::test_ne_bench[llama-7b-ffn-bfloat16]
benchmarks/ops/bench_elementwise.py::test_ne_bench[llama-7b-ffn-float32]
benchmarks/ops/bench_elementwise.py::test_ne_bench[linear-bias-float16]
benchmarks/ops/bench_elementwise.py::test_ne_bench[linear-bias-bfloat16]
benchmarks/ops/bench_elementwise.py::test_ne_bench[linear-bias-float32]
benchmarks/ops/bench_elementwise.py::test_ne_bench[llama-7b-hidden-float16]
benchmarks/ops/bench_elementwise.py::test_gt_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise.py::test_gt_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise.py::test_gt_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise.py::test_gt_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise.py::test_gt_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise.py::test_gt_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise.py::test_gt_bench[llama-7b-ffn-float16]
benchmarks/ops/bench_elementwise.py::test_gt_bench[llama-7b-ffn-bfloat16]
benchmarks/ops/bench_elementwise.py::test_gt_bench[llama-7b-ffn-float32]
benchmarks/ops/bench_elementwise.py::test_gt_bench[linear-bias-float16]
benchmarks/ops/bench_elementwise.py::test_gt_bench[linear-bias-bfloat16]
benchmarks/ops/bench_elementwise.py::test_gt_bench[linear-bias-float32]
benchmarks/ops/bench_elementwise.py::test_gt_bench[llama-7b-hidden-float16]
benchmarks/ops/bench_elementwise.py::test_lt_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise.py::test_lt_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise.py::test_lt_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise.py::test_lt_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise.py::test_lt_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise.py::test_lt_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise.py::test_lt_bench[llama-7b-ffn-float16]
benchmarks/ops/bench_elementwise.py::test_lt_bench[llama-7b-ffn-bfloat16]
benchmarks/ops/bench_elementwise.py::test_lt_bench[llama-7b-ffn-float32]
benchmarks/ops/bench_elementwise.py::test_lt_bench[linear-bias-float16]
benchmarks/ops/bench_elementwise.py::test_lt_bench[linear-bias-bfloat16]
benchmarks/ops/bench_elementwise.py::test_lt_bench[linear-bias-float32]
benchmarks/ops/bench_elementwise.py::test_lt_bench[llama-7b-hidden-float16]
benchmarks/ops/bench_elementwise.py::test_ge_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise.py::test_ge_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise.py::test_ge_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise.py::test_ge_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise.py::test_ge_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise.py::test_ge_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise.py::test_ge_bench[llama-7b-ffn-float16]
benchmarks/ops/bench_elementwise.py::test_ge_bench[llama-7b-ffn-bfloat16]
benchmarks/ops/bench_elementwise.py::test_ge_bench[llama-7b-ffn-float32]
benchmarks/ops/bench_elementwise.py::test_ge_bench[linear-bias-float16]
benchmarks/ops/bench_elementwise.py::test_ge_bench[linear-bias-bfloat16]
benchmarks/ops/bench_elementwise.py::test_ge_bench[linear-bias-float32]
benchmarks/ops/bench_elementwise.py::test_ge_bench[llama-7b-hidden-float16]
benchmarks/ops/bench_elementwise.py::test_le_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise.py::test_le_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise.py::test_le_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise.py::test_le_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise.py::test_le_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise.py::test_le_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise.py::test_le_bench[llama-7b-ffn-float16]
benchmarks/ops/bench_elementwise.py::test_le_bench[llama-7b-ffn-bfloat16]
benchmarks/ops/bench_elementwise.py::test_le_bench[llama-7b-ffn-float32]
benchmarks/ops/bench_elementwise.py::test_le_bench[linear-bias-float16]
benchmarks/ops/bench_elementwise.py::test_le_bench[linear-bias-bfloat16]
benchmarks/ops/bench_elementwise.py::test_le_bench[linear-bias-float32]
benchmarks/ops/bench_elementwise.py::test_le_bench[llama-7b-hidden-float16]
benchmarks/ops/bench_elementwise.py::test_logical_and_bench[hidden-state-prefill-bool]
benchmarks/ops/bench_elementwise.py::test_logical_and_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise.py::test_logical_and_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise.py::test_logical_and_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise.py::test_logical_and_bench[cnn-feat-broadcast-bool]
benchmarks/ops/bench_elementwise.py::test_logical_and_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise.py::test_logical_and_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise.py::test_logical_and_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise.py::test_logical_and_bench[llama-7b-ffn-bool]
benchmarks/ops/bench_elementwise.py::test_logical_and_bench[llama-7b-ffn-float16]
benchmarks/ops/bench_elementwise.py::test_logical_and_bench[llama-7b-ffn-bfloat16]
benchmarks/ops/bench_elementwise.py::test_logical_and_bench[llama-7b-ffn-float32]
benchmarks/ops/bench_elementwise.py::test_logical_and_bench[linear-bias-bool]
benchmarks/ops/bench_elementwise.py::test_logical_and_bench[linear-bias-float16]
benchmarks/ops/bench_elementwise.py::test_logical_and_bench[linear-bias-bfloat16]
benchmarks/ops/bench_elementwise.py::test_logical_and_bench[linear-bias-float32]
benchmarks/ops/bench_elementwise.py::test_logical_and_bench[llama-7b-hidden-float16]
benchmarks/ops/bench_elementwise.py::test_logical_and_bench[phi-2-ffn-float16]
benchmarks/ops/bench_elementwise.py::test_logical_or_bench[hidden-state-prefill-bool]
benchmarks/ops/bench_elementwise.py::test_logical_or_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise.py::test_logical_or_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise.py::test_logical_or_bench[hidden-state-prefill-float32]
benchmarks/ops/bench_elementwise.py::test_logical_or_bench[cnn-feat-broadcast-bool]
benchmarks/ops/bench_elementwise.py::test_logical_or_bench[cnn-feat-broadcast-float16]
benchmarks/ops/bench_elementwise.py::test_logical_or_bench[cnn-feat-broadcast-bfloat16]
benchmarks/ops/bench_elementwise.py::test_logical_or_bench[cnn-feat-broadcast-float32]
benchmarks/ops/bench_elementwise.py::test_logical_or_bench[llama-7b-ffn-bool]
benchmarks/ops/bench_elementwise.py::test_logical_or_bench[llama-7b-ffn-float16]
benchmarks/ops/bench_elementwise.py::test_logical_or_bench[llama-7b-ffn-bfloat16]
benchmarks/ops/bench_elementwise.py::test_logical_or_bench[llama-7b-ffn-float32]
benchmarks/ops/bench_elementwise.py::test_logical_or_bench[linear-bias-bool]
benchmarks/ops/bench_elementwise.py::test_logical_or_bench[linear-bias-float16]
benchmarks/ops/bench_elementwise.py::test_logical_or_bench[linear-bias-bfloat16]
benchmarks/ops/bench_elementwise.py::test_logical_or_bench[linear-bias-float32]
benchmarks/ops/bench_elementwise.py::test_logical_or_bench[llama-7b-hidden-float16]
benchmarks/ops/bench_elementwise.py::test_logical_or_bench[phi-2-ffn-float16]
benchmarks/ops/bench_elementwise.py::test_bitwise_and_bench[hidden-state-prefill-bool]
benchmarks/ops/bench_elementwise.py::test_bitwise_and_bench[hidden-state-prefill-int32]
benchmarks/ops/bench_elementwise.py::test_bitwise_and_bench[hidden-state-prefill-int64]
benchmarks/ops/bench_elementwise.py::test_bitwise_and_bench[cnn-feat-broadcast-bool]
benchmarks/ops/bench_elementwise.py::test_bitwise_and_bench[cnn-feat-broadcast-int32]
benchmarks/ops/bench_elementwise.py::test_bitwise_and_bench[cnn-feat-broadcast-int64]
benchmarks/ops/bench_elementwise.py::test_bitwise_and_bench[llama-7b-ffn-bool]
benchmarks/ops/bench_elementwise.py::test_bitwise_and_bench[llama-7b-ffn-int32]
benchmarks/ops/bench_elementwise.py::test_bitwise_and_bench[llama-7b-ffn-int64]
benchmarks/ops/bench_elementwise.py::test_bitwise_and_bench[linear-bias-bool]
benchmarks/ops/bench_elementwise.py::test_bitwise_and_bench[linear-bias-int32]
benchmarks/ops/bench_elementwise.py::test_bitwise_and_bench[linear-bias-int64]
benchmarks/ops/bench_elementwise.py::test_bitwise_and_bench[llama-7b-hidden-int32]
benchmarks/ops/bench_elementwise.py::test_bitwise_and_bench[phi-2-ffn-int32]
benchmarks/ops/bench_elementwise.py::test_bitwise_or_bench[hidden-state-prefill-bool]
benchmarks/ops/bench_elementwise.py::test_bitwise_or_bench[hidden-state-prefill-int32]
benchmarks/ops/bench_elementwise.py::test_bitwise_or_bench[hidden-state-prefill-int64]
benchmarks/ops/bench_elementwise.py::test_bitwise_or_bench[cnn-feat-broadcast-bool]
benchmarks/ops/bench_elementwise.py::test_bitwise_or_bench[cnn-feat-broadcast-int32]
benchmarks/ops/bench_elementwise.py::test_bitwise_or_bench[cnn-feat-broadcast-int64]
benchmarks/ops/bench_elementwise.py::test_bitwise_or_bench[llama-7b-ffn-bool]
benchmarks/ops/bench_elementwise.py::test_bitwise_or_bench[llama-7b-ffn-int32]
benchmarks/ops/bench_elementwise.py::test_bitwise_or_bench[llama-7b-ffn-int64]
benchmarks/ops/bench_elementwise.py::test_bitwise_or_bench[linear-bias-bool]
benchmarks/ops/bench_elementwise.py::test_bitwise_or_bench[linear-bias-int32]
benchmarks/ops/bench_elementwise.py::test_bitwise_or_bench[linear-bias-int64]
benchmarks/ops/bench_elementwise.py::test_bitwise_or_bench[llama-7b-hidden-int32]
benchmarks/ops/bench_elementwise.py::test_bitwise_xor_bench[hidden-state-prefill-bool]
benchmarks/ops/bench_elementwise.py::test_bitwise_xor_bench[hidden-state-prefill-int32]
benchmarks/ops/bench_elementwise.py::test_bitwise_xor_bench[hidden-state-prefill-int64]
benchmarks/ops/bench_elementwise.py::test_bitwise_xor_bench[cnn-feat-broadcast-bool]
benchmarks/ops/bench_elementwise.py::test_bitwise_xor_bench[cnn-feat-broadcast-int32]
benchmarks/ops/bench_elementwise.py::test_bitwise_xor_bench[cnn-feat-broadcast-int64]
benchmarks/ops/bench_elementwise.py::test_bitwise_xor_bench[llama-7b-ffn-bool]
benchmarks/ops/bench_elementwise.py::test_bitwise_xor_bench[llama-7b-ffn-int32]
benchmarks/ops/bench_elementwise.py::test_bitwise_xor_bench[llama-7b-ffn-int64]
benchmarks/ops/bench_elementwise.py::test_bitwise_xor_bench[linear-bias-bool]
benchmarks/ops/bench_elementwise.py::test_bitwise_xor_bench[linear-bias-int32]
benchmarks/ops/bench_elementwise.py::test_bitwise_xor_bench[linear-bias-int64]
benchmarks/ops/bench_elementwise.py::test_bitwise_xor_bench[llama-7b-hidden-int32]
benchmarks/ops/bench_elementwise.py::test_alibi_bench[mpt-7b-2k-float16]
benchmarks/ops/bench_elementwise.py::test_alibi_bench[mpt-7b-2k-bfloat16]
benchmarks/ops/bench_elementwise.py::test_alibi_bench[mpt-7b-4k-float16]
benchmarks/ops/bench_elementwise.py::test_alibi_bench[mpt-7b-4k-bfloat16]
benchmarks/ops/bench_elementwise.py::test_sinusoidal_bench[transformer-2k-4k-float16]
benchmarks/ops/bench_elementwise.py::test_sinusoidal_bench[transformer-2k-4k-bfloat16]
benchmarks/ops/bench_elementwise.py::test_sinusoidal_bench[transformer-4k-4k-float16]
benchmarks/ops/bench_elementwise.py::test_sinusoidal_bench[transformer-4k-4k-bfloat16]
benchmarks/ops/bench_elementwise.py::test_where_bench[16M-float16]
benchmarks/ops/bench_elementwise.py::test_where_bench[16M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_where_bench[16M-float32]
benchmarks/ops/bench_elementwise.py::test_where_bench[256M-float16]
benchmarks/ops/bench_elementwise.py::test_where_bench[256M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_lerp_tensor_bench[16M-float16]
benchmarks/ops/bench_elementwise.py::test_lerp_tensor_bench[16M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_lerp_tensor_bench[16M-float32]
benchmarks/ops/bench_elementwise.py::test_lerp_tensor_bench[256M-float16]
benchmarks/ops/bench_elementwise.py::test_lerp_tensor_bench[256M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_relu_bench[hidden-state-prefill-float16]
benchmarks/ops/bench_elementwise.py::test_relu_bench[hidden-state-prefill-bfloat16]
benchmarks/ops/bench_elementwise.py::test_relu_bench[hidden-state-decode-bfloat16]
benchmarks/ops/bench_elementwise.py::test_gelu_bench[llama-8b-ffn-prefill-float16]
benchmarks/ops/bench_elementwise.py::test_gelu_bench[llama-8b-ffn-prefill-bfloat16]
benchmarks/ops/bench_elementwise.py::test_gelu_bench[llama-8b-ffn-decode-bfloat16]
benchmarks/ops/bench_elementwise.py::test_silu_bench[llama-8b-ffn-prefill-float16]
benchmarks/ops/bench_elementwise.py::test_silu_bench[llama-8b-ffn-prefill-bfloat16]
benchmarks/ops/bench_elementwise.py::test_silu_bench[llama-8b-ffn-decode-bfloat16]
benchmarks/ops/bench_elementwise.py::test_hardswish_bench[mbv3-stage2-float16]
benchmarks/ops/bench_elementwise.py::test_hardswish_bench[mbv3-stage2-bfloat16]
benchmarks/ops/bench_elementwise.py::test_hardswish_bench[mbv3-stage3-float16]
benchmarks/ops/bench_elementwise.py::test_hardswish_bench[mbv3-stage3-bfloat16]
benchmarks/ops/bench_elementwise.py::test_hardsigmoid_bench[mbv3-se-gate-float16]
benchmarks/ops/bench_elementwise.py::test_hardsigmoid_bench[mbv3-se-gate-bfloat16]
benchmarks/ops/bench_elementwise.py::test_hardsigmoid_bench[mbv3-se-gate-deep-float16]
benchmarks/ops/bench_elementwise.py::test_hardsigmoid_bench[mbv3-se-gate-deep-bfloat16]
benchmarks/ops/bench_elementwise.py::test_mish_bench[yolo-p3-float16]
benchmarks/ops/bench_elementwise.py::test_mish_bench[yolo-p3-bfloat16]
benchmarks/ops/bench_elementwise.py::test_mish_bench[yolo-p4-float16]
benchmarks/ops/bench_elementwise.py::test_mish_bench[yolo-p4-bfloat16]
benchmarks/ops/bench_elementwise.py::test_selu_bench[snn-fc-float16]
benchmarks/ops/bench_elementwise.py::test_selu_bench[snn-fc-bfloat16]
benchmarks/ops/bench_elementwise.py::test_selu_bench[snn-fc-wide-float16]
benchmarks/ops/bench_elementwise.py::test_selu_bench[snn-fc-wide-bfloat16]
benchmarks/ops/bench_elementwise.py::test_leaky_relu_bench[gan-feat-float16]
benchmarks/ops/bench_elementwise.py::test_leaky_relu_bench[gan-feat-bfloat16]
benchmarks/ops/bench_elementwise.py::test_leaky_relu_bench[gan-feat-deep-float16]
benchmarks/ops/bench_elementwise.py::test_leaky_relu_bench[gan-feat-deep-bfloat16]
benchmarks/ops/bench_elementwise.py::test_elu_bench[mlp-hidden-float16]
benchmarks/ops/bench_elementwise.py::test_elu_bench[mlp-hidden-bfloat16]
benchmarks/ops/bench_elementwise.py::test_elu_bench[mlp-hidden-wide-float16]
benchmarks/ops/bench_elementwise.py::test_elu_bench[mlp-hidden-wide-bfloat16]
benchmarks/ops/bench_elementwise.py::test_hardtanh_bench[bounded-hidden-float16]
benchmarks/ops/bench_elementwise.py::test_hardtanh_bench[bounded-hidden-bfloat16]
benchmarks/ops/bench_elementwise.py::test_hardtanh_bench[bounded-conv-feat-float16]
benchmarks/ops/bench_elementwise.py::test_hardtanh_bench[bounded-conv-feat-bfloat16]
benchmarks/ops/bench_elementwise.py::test_softplus_bench[mlp-hidden-float16]
benchmarks/ops/bench_elementwise.py::test_softplus_bench[mlp-hidden-bfloat16]
benchmarks/ops/bench_elementwise.py::test_softplus_bench[mlp-hidden-wide-float16]
benchmarks/ops/bench_elementwise.py::test_softplus_bench[mlp-hidden-wide-bfloat16]
benchmarks/ops/bench_elementwise.py::test_clamp_bench[16M-float16]
benchmarks/ops/bench_elementwise.py::test_clamp_bench[16M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_clamp_bench[16M-float32]
benchmarks/ops/bench_elementwise.py::test_clamp_bench[256M-float16]
benchmarks/ops/bench_elementwise.py::test_clamp_bench[256M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_clamp_bench[16M-min-only-float16]
benchmarks/ops/bench_elementwise.py::test_clamp_bench[16M-min-only-bfloat16]
benchmarks/ops/bench_elementwise.py::test_clamp_bench[16M-min-only-float32]
benchmarks/ops/bench_elementwise.py::test_clamp_bench[256M-min-only-float16]
benchmarks/ops/bench_elementwise.py::test_clamp_bench[256M-min-only-bfloat16]
benchmarks/ops/bench_elementwise.py::test_clamp_bench[16M-max-only-float16]
benchmarks/ops/bench_elementwise.py::test_clamp_bench[16M-max-only-bfloat16]
benchmarks/ops/bench_elementwise.py::test_clamp_bench[16M-max-only-float32]
benchmarks/ops/bench_elementwise.py::test_clamp_bench[256M-max-only-float16]
benchmarks/ops/bench_elementwise.py::test_clamp_bench[256M-max-only-bfloat16]
benchmarks/ops/bench_elementwise.py::test_clamp_scalar_bench[16M-float16]
benchmarks/ops/bench_elementwise.py::test_clamp_scalar_bench[16M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_clamp_scalar_bench[16M-float32]
benchmarks/ops/bench_elementwise.py::test_clamp_scalar_bench[256M-float16]
benchmarks/ops/bench_elementwise.py::test_clamp_scalar_bench[256M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_nan_to_num_bench[16M-float16]
benchmarks/ops/bench_elementwise.py::test_nan_to_num_bench[16M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_nan_to_num_bench[16M-float32]
benchmarks/ops/bench_elementwise.py::test_nan_to_num_bench[256M-float16]
benchmarks/ops/bench_elementwise.py::test_nan_to_num_bench[256M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_exp_bench[16M-float16]
benchmarks/ops/bench_elementwise.py::test_exp_bench[16M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_exp_bench[16M-float32]
benchmarks/ops/bench_elementwise.py::test_exp_bench[256M-float16]
benchmarks/ops/bench_elementwise.py::test_exp_bench[256M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_log_bench[16M-float16]
benchmarks/ops/bench_elementwise.py::test_log_bench[16M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_log_bench[16M-float32]
benchmarks/ops/bench_elementwise.py::test_log_bench[256M-float16]
benchmarks/ops/bench_elementwise.py::test_log_bench[256M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_sqrt_bench[16M-float16]
benchmarks/ops/bench_elementwise.py::test_sqrt_bench[16M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_sqrt_bench[16M-float32]
benchmarks/ops/bench_elementwise.py::test_sqrt_bench[256M-float16]
benchmarks/ops/bench_elementwise.py::test_sqrt_bench[256M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_rsqrt_bench[16M-float16]
benchmarks/ops/bench_elementwise.py::test_rsqrt_bench[16M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_rsqrt_bench[16M-float32]
benchmarks/ops/bench_elementwise.py::test_rsqrt_bench[256M-float16]
benchmarks/ops/bench_elementwise.py::test_rsqrt_bench[256M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_abs_bench[16M-float16]
benchmarks/ops/bench_elementwise.py::test_abs_bench[16M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_abs_bench[16M-float32]
benchmarks/ops/bench_elementwise.py::test_abs_bench[256M-float16]
benchmarks/ops/bench_elementwise.py::test_abs_bench[256M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_neg_bench[16M-float16]
benchmarks/ops/bench_elementwise.py::test_neg_bench[16M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_neg_bench[16M-float32]
benchmarks/ops/bench_elementwise.py::test_neg_bench[256M-float16]
benchmarks/ops/bench_elementwise.py::test_neg_bench[256M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_reciprocal_bench[16M-float16]
benchmarks/ops/bench_elementwise.py::test_reciprocal_bench[16M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_reciprocal_bench[16M-float32]
benchmarks/ops/bench_elementwise.py::test_reciprocal_bench[256M-float16]
benchmarks/ops/bench_elementwise.py::test_reciprocal_bench[256M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_sign_bench[16M-float16]
benchmarks/ops/bench_elementwise.py::test_sign_bench[16M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_sign_bench[16M-float32]
benchmarks/ops/bench_elementwise.py::test_sign_bench[256M-float16]
benchmarks/ops/bench_elementwise.py::test_sign_bench[256M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_sin_bench[16M-float16]
benchmarks/ops/bench_elementwise.py::test_sin_bench[16M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_sin_bench[16M-float32]
benchmarks/ops/bench_elementwise.py::test_sin_bench[256M-float16]
benchmarks/ops/bench_elementwise.py::test_sin_bench[256M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_cos_bench[16M-float16]
benchmarks/ops/bench_elementwise.py::test_cos_bench[16M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_cos_bench[16M-float32]
benchmarks/ops/bench_elementwise.py::test_cos_bench[256M-float16]
benchmarks/ops/bench_elementwise.py::test_cos_bench[256M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_floor_bench[16M-float16]
benchmarks/ops/bench_elementwise.py::test_floor_bench[16M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_floor_bench[16M-float32]
benchmarks/ops/bench_elementwise.py::test_floor_bench[256M-float16]
benchmarks/ops/bench_elementwise.py::test_floor_bench[256M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_ceil_bench[16M-float16]
benchmarks/ops/bench_elementwise.py::test_ceil_bench[16M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_ceil_bench[16M-float32]
benchmarks/ops/bench_elementwise.py::test_ceil_bench[256M-float16]
benchmarks/ops/bench_elementwise.py::test_ceil_bench[256M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_round_bench[16M-float16]
benchmarks/ops/bench_elementwise.py::test_round_bench[16M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_round_bench[16M-float32]
benchmarks/ops/bench_elementwise.py::test_round_bench[256M-float16]
benchmarks/ops/bench_elementwise.py::test_round_bench[256M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_trunc_bench[16M-float16]
benchmarks/ops/bench_elementwise.py::test_trunc_bench[16M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_trunc_bench[16M-float32]
benchmarks/ops/bench_elementwise.py::test_trunc_bench[256M-float16]
benchmarks/ops/bench_elementwise.py::test_trunc_bench[256M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_erf_bench[16M-float16]
benchmarks/ops/bench_elementwise.py::test_erf_bench[16M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_erf_bench[16M-float32]
benchmarks/ops/bench_elementwise.py::test_erf_bench[256M-float16]
benchmarks/ops/bench_elementwise.py::test_erf_bench[256M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_log1p_bench[16M-float16]
benchmarks/ops/bench_elementwise.py::test_log1p_bench[16M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_log1p_bench[16M-float32]
benchmarks/ops/bench_elementwise.py::test_log1p_bench[256M-float16]
benchmarks/ops/bench_elementwise.py::test_log1p_bench[256M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_expm1_bench[16M-float16]
benchmarks/ops/bench_elementwise.py::test_expm1_bench[16M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_expm1_bench[16M-float32]
benchmarks/ops/bench_elementwise.py::test_expm1_bench[256M-float16]
benchmarks/ops/bench_elementwise.py::test_expm1_bench[256M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_sigmoid_bench[16M-float16]
benchmarks/ops/bench_elementwise.py::test_sigmoid_bench[16M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_sigmoid_bench[16M-float32]
benchmarks/ops/bench_elementwise.py::test_sigmoid_bench[256M-float16]
benchmarks/ops/bench_elementwise.py::test_sigmoid_bench[256M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_tanh_bench[16M-float16]
benchmarks/ops/bench_elementwise.py::test_tanh_bench[16M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_tanh_bench[16M-float32]
benchmarks/ops/bench_elementwise.py::test_tanh_bench[256M-float16]
benchmarks/ops/bench_elementwise.py::test_tanh_bench[256M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_logical_not_bench[16M-bool]
benchmarks/ops/bench_elementwise.py::test_logical_not_bench[16M-float16]
benchmarks/ops/bench_elementwise.py::test_logical_not_bench[16M-float32]
benchmarks/ops/bench_elementwise.py::test_logical_not_bench[256M-bool]
benchmarks/ops/bench_elementwise.py::test_bitwise_not_bench[16M-int32]
benchmarks/ops/bench_elementwise.py::test_bitwise_not_bench[16M-int64]
benchmarks/ops/bench_elementwise.py::test_bitwise_not_bench[256M-int32]
benchmarks/ops/bench_elementwise.py::test_isnan_bench[16M-float16]
benchmarks/ops/bench_elementwise.py::test_isnan_bench[16M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_isnan_bench[16M-float32]
benchmarks/ops/bench_elementwise.py::test_isnan_bench[256M-float16]
benchmarks/ops/bench_elementwise.py::test_isnan_bench[256M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_isinf_bench[16M-float16]
benchmarks/ops/bench_elementwise.py::test_isinf_bench[16M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_isinf_bench[16M-float32]
benchmarks/ops/bench_elementwise.py::test_isinf_bench[256M-float16]
benchmarks/ops/bench_elementwise.py::test_isinf_bench[256M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_isfinite_bench[16M-float16]
benchmarks/ops/bench_elementwise.py::test_isfinite_bench[16M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_isfinite_bench[16M-float32]
benchmarks/ops/bench_elementwise.py::test_isfinite_bench[256M-float16]
benchmarks/ops/bench_elementwise.py::test_isfinite_bench[256M-bfloat16]
benchmarks/ops/bench_elementwise.py::test_dropout_bench[hidden-4k-float16]
benchmarks/ops/bench_elementwise.py::test_dropout_bench[hidden-4k-float32]
benchmarks/ops/bench_elementwise.py::test_dropout_bench[hidden-10k-bfloat16]

517 tests collected in 3.99s
........................................................................ [ 13%]
........................................................................ [ 27%]
........................................................................ [ 41%]
........................................................................ [ 55%]
........................................................................ [ 69%]
........................................................................ [ 83%]
........................................................................ [ 97%]
.............                                                            [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_elementwise.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
517 passed, 14 warnings in 1003.97s (0:16:43)
--- benchmarks/ops/bench_elementwise.py finished in 1013s ---

=== [11/60] benchmarks/ops/bench_engram.py ===
benchmarks/ops/bench_engram.py::test_engram_gate_conv_fwd_bench[train-s32-float16]
benchmarks/ops/bench_engram.py::test_engram_gate_conv_fwd_bench[train-s64-float16]
benchmarks/ops/bench_engram.py::test_engram_gate_conv_fwd_bench[train-s128-bfloat16]
benchmarks/ops/bench_engram.py::test_engram_gate_conv_fwd_bench[train-s96-bfloat16]
benchmarks/ops/bench_engram.py::test_engram_gate_conv_bwd_bench[train-s32-float16]
benchmarks/ops/bench_engram.py::test_engram_gate_conv_bwd_bench[train-s64-float16]
benchmarks/ops/bench_engram.py::test_engram_gate_conv_bwd_bench[train-s128-bfloat16]
benchmarks/ops/bench_engram.py::test_engram_gate_conv_bwd_bench[train-s96-bfloat16]
benchmarks/ops/bench_engram.py::test_engram_decode_bench[serving-b1-float16]
benchmarks/ops/bench_engram.py::test_engram_decode_bench[serving-b4-float16]
benchmarks/ops/bench_engram.py::test_engram_decode_bench[serving-b8-bfloat16]

11 tests collected in 3.01s
...........                                                              [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_engram.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
11 passed, 14 warnings in 15.67s
--- benchmarks/ops/bench_engram.py finished in 23s ---

=== [12/60] benchmarks/ops/bench_fft.py ===
RUNNING [12/60] 30s: benchmarks/ops/bench_fft.py::test_fft_bench[scientific-1m-complex128]
benchmarks/ops/bench_fft.py::test_fft_bench[latency-4k-complex64]
benchmarks/ops/bench_fft.py::test_fft_bench[throughput-4k-complex64]
benchmarks/ops/bench_fft.py::test_fft_bench[throughput-4k-complex128]
benchmarks/ops/bench_fft.py::test_fft_bench[longconv-16k-complex64]
benchmarks/ops/bench_fft.py::test_fft_bench[longconv-64k-complex64]
benchmarks/ops/bench_fft.py::test_fft_bench[spectrogram-1k-complex64]
benchmarks/ops/bench_fft.py::test_fft_bench[fnet-512-complex64]
benchmarks/ops/bench_fft.py::test_fft_bench[shortconv-64-complex64]
benchmarks/ops/bench_fft.py::test_fft_bench[scientific-1m-complex128]
benchmarks/ops/bench_fft.py::test_fft_bench[spectrogram-1k-b300-complex64]

10 tests collected in 3.14s
..........                                                               [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_fft.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
10 passed, 14 warnings in 25.01s
--- benchmarks/ops/bench_fft.py finished in 32s ---

=== [13/60] benchmarks/ops/bench_fp8_lightning_indexer.py ===
RUNNING [13/60] 30s: benchmarks/ops/bench_fp8_lightning_indexer.py::test_fp8_lightning_indexer_bench[index-q2048-ctx4096-float8_e4m3fn]
RUNNING [13/60] 60s: benchmarks/ops/bench_fp8_lightning_indexer.py::test_fp8_lightning_indexer_bench[index-q4096-ctx32768-float8_e4m3fn]
RUNNING [13/60] 90s: benchmarks/ops/bench_fp8_lightning_indexer.py::test_fp8_lightning_indexer_bench[index-q4096-ctx131072-float8_e4m3fn]
benchmarks/ops/bench_fp8_lightning_indexer.py::test_fp8_lightning_indexer_bench[chunk-prefill-bfloat16]
benchmarks/ops/bench_fp8_lightning_indexer.py::test_fp8_lightning_indexer_bench[chunk-prefill-float8_e4m3fn]
benchmarks/ops/bench_fp8_lightning_indexer.py::test_fp8_lightning_indexer_bench[chunk-prefill-kscale-float8_e4m3fn]
benchmarks/ops/bench_fp8_lightning_indexer.py::test_fp8_lightning_indexer_bench[short-prefill-bfloat16]
benchmarks/ops/bench_fp8_lightning_indexer.py::test_fp8_lightning_indexer_bench[context-chunk-bfloat16]
benchmarks/ops/bench_fp8_lightning_indexer.py::test_fp8_lightning_indexer_bench[index-q2048-ctx4096-float8_e4m3fn]
benchmarks/ops/bench_fp8_lightning_indexer.py::test_fp8_lightning_indexer_bench[index-q2048-ctx8192-float8_e4m3fn]
benchmarks/ops/bench_fp8_lightning_indexer.py::test_fp8_lightning_indexer_bench[index-q2048-ctx16384-float8_e4m3fn]
benchmarks/ops/bench_fp8_lightning_indexer.py::test_fp8_lightning_indexer_bench[index-q2048-ctx32768-float8_e4m3fn]
benchmarks/ops/bench_fp8_lightning_indexer.py::test_fp8_lightning_indexer_bench[index-q2048-ctx65536-float8_e4m3fn]
benchmarks/ops/bench_fp8_lightning_indexer.py::test_fp8_lightning_indexer_bench[index-q2048-ctx131072-float8_e4m3fn]
benchmarks/ops/bench_fp8_lightning_indexer.py::test_fp8_lightning_indexer_bench[index-q4096-ctx4096-float8_e4m3fn]
benchmarks/ops/bench_fp8_lightning_indexer.py::test_fp8_lightning_indexer_bench[index-q4096-ctx8192-float8_e4m3fn]
benchmarks/ops/bench_fp8_lightning_indexer.py::test_fp8_lightning_indexer_bench[index-q4096-ctx16384-float8_e4m3fn]
benchmarks/ops/bench_fp8_lightning_indexer.py::test_fp8_lightning_indexer_bench[index-q4096-ctx32768-float8_e4m3fn]
benchmarks/ops/bench_fp8_lightning_indexer.py::test_fp8_lightning_indexer_bench[index-q4096-ctx65536-float8_e4m3fn]
benchmarks/ops/bench_fp8_lightning_indexer.py::test_fp8_lightning_indexer_bench[index-q4096-ctx131072-float8_e4m3fn]
benchmarks/ops/bench_fp8_lightning_indexer.py::test_fp8_lightning_indexer_bench[ds-v32-decode-b1-float8_e4m3fn]

18 tests collected in 5.23s
..................                                                       [100%]Benchmark report saved to profile_run.log

18 passed in 104.03s (0:01:44)
--- benchmarks/ops/bench_fp8_lightning_indexer.py finished in 113s ---

=== [14/60] benchmarks/ops/bench_fp8_quant.py ===
benchmarks/ops/bench_fp8_quant.py::test_fp8_quant_bench[kv-index-8k-float16]
benchmarks/ops/bench_fp8_quant.py::test_fp8_quant_bench[kv-index-8k-bfloat16]
benchmarks/ops/bench_fp8_quant.py::test_fp8_quant_bench[kv-index-4k-float32]
benchmarks/ops/bench_fp8_quant.py::test_fp8_quant_bench[kv-index-context-chunk-float16]
benchmarks/ops/bench_fp8_quant.py::test_fp8_quant_bench[kv-index-context-chunk-bfloat16]

5 tests collected in 3.01s
.....                                                                    [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_fp8_quant.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
5 passed, 14 warnings in 6.20s
--- benchmarks/ops/bench_fp8_quant.py finished in 13s ---

=== [15/60] benchmarks/ops/bench_fp8_quant_per_block.py ===
benchmarks/ops/bench_fp8_quant_per_block.py::test_fp8_quant_per_block_bench[ds-v3-mlp-down-bfloat16]
benchmarks/ops/bench_fp8_quant_per_block.py::test_fp8_quant_per_block_bench[ds-v3-expert-gate-up-bfloat16]
benchmarks/ops/bench_fp8_quant_per_block.py::test_fp8_quant_per_block_bench[ds-v3-expert-gate-up-float32]
benchmarks/ops/bench_fp8_quant_per_block.py::test_fp8_quant_per_block_bench[qwen3-235b-qkv-bfloat16]
benchmarks/ops/bench_fp8_quant_per_block.py::test_fp8_quant_per_block_bench[qwen3-235b-qkv-float16]
benchmarks/ops/bench_fp8_quant_per_block.py::test_fp8_quant_per_block_bench[gpt-oss-expert-down-bfloat16]
benchmarks/ops/bench_fp8_quant_per_block.py::test_fp8_quant_per_block_bench[ragged-k-float16]

7 tests collected in 2.99s
.......                                                                  [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_fp8_quant_per_block.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
7 passed, 14 warnings in 21.70s
--- benchmarks/ops/bench_fp8_quant_per_block.py finished in 29s ---

=== [16/60] benchmarks/ops/bench_fused_gated.py ===
RUNNING [16/60] 30s: benchmarks/ops/bench_fused_gated.py::test_gelu_and_mul_bench[llama-8b-prefill-tanh-float16]
benchmarks/ops/bench_fused_gated.py::test_silu_and_mul_bench[llama-8b-ffn-prefill-float16]
benchmarks/ops/bench_fused_gated.py::test_silu_and_mul_bench[llama-8b-ffn-prefill-bfloat16]
benchmarks/ops/bench_fused_gated.py::test_silu_and_mul_bench[llama-8b-ffn-decode-bfloat16]
benchmarks/ops/bench_fused_gated.py::test_silu_and_mul_bench[qwen3-8b-swiglu-b32-bfloat16]
benchmarks/ops/bench_fused_gated.py::test_gelu_and_mul_bench[llama-8b-ffn-prefill-float16]
benchmarks/ops/bench_fused_gated.py::test_gelu_and_mul_bench[llama-8b-ffn-prefill-bfloat16]
benchmarks/ops/bench_fused_gated.py::test_gelu_and_mul_bench[llama-8b-ffn-decode-bfloat16]
benchmarks/ops/bench_fused_gated.py::test_gelu_and_mul_bench[llama-8b-prefill-tanh-float16]
benchmarks/ops/bench_fused_gated.py::test_gelu_and_mul_bench[llama-8b-prefill-tanh-bfloat16]
benchmarks/ops/bench_fused_gated.py::test_gelu_and_mul_bench[llama-8b-decode-tanh-bfloat16]

10 tests collected in 1.62s
..........                                                               [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_fused_gated.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
10 passed, 14 warnings in 33.02s
--- benchmarks/ops/bench_fused_gated.py finished in 38s ---

=== [17/60] benchmarks/ops/bench_fused_moe.py ===
RUNNING [17/60] 30s: benchmarks/ops/bench_fused_moe.py::test_fused_moe_fwd_bench[qwen3-235b-decode-bfloat16]
RUNNING [17/60] 60s: benchmarks/ops/bench_fused_moe.py::test_fused_moe_fwd_bench[qwen3-235b-decode-bfloat16]
RUNNING [17/60] 90s: benchmarks/ops/bench_fused_moe.py::test_fused_moe_fwd_bench[qwen3-235b-decode-bfloat16]
RUNNING [17/60] 120s: benchmarks/ops/bench_fused_moe.py::test_fused_moe_fwd_bench[qwen3-235b-decode-bfloat16]
RUNNING [17/60] 150s: benchmarks/ops/bench_fused_moe.py::test_fused_moe_fwd_bench[qwen3-235b-decode-bfloat16]
RUNNING [17/60] 180s: benchmarks/ops/bench_fused_moe.py::test_fused_moe_fwd_bench[qwen3-235b-decode-bfloat16]
RUNNING [17/60] 210s: benchmarks/ops/bench_fused_moe.py::test_fused_moe_fwd_bench[qwen3-235b-decode-bfloat16]
RUNNING [17/60] 240s: benchmarks/ops/bench_fused_moe.py::test_fused_moe_fwd_bench[qwen3-235b-decode-bfloat16]
RUNNING [17/60] 270s: benchmarks/ops/bench_fused_moe.py::test_fused_moe_fwd_bench[qwen3-235b-decode-bfloat16]
RUNNING [17/60] 300s: benchmarks/ops/bench_fused_moe.py::test_fused_moe_fwd_bench[qwen3-235b-decode-bfloat16]
RUNNING [17/60] 330s: benchmarks/ops/bench_fused_moe.py::test_fused_moe_fwd_bench[qwen3-235b-decode-bfloat16]
RUNNING [17/60] 360s: benchmarks/ops/bench_fused_moe.py::test_fused_moe_fwd_bench[qwen3-235b-decode-bfloat16]
RUNNING [17/60] 391s: benchmarks/ops/bench_fused_moe.py::test_fused_moe_fwd_bench[qwen3-235b-decode-bfloat16]
RUNNING [17/60] 421s: benchmarks/ops/bench_fused_moe.py::test_fused_moe_fwd_bench[qwen3-235b-decode-bfloat16]
RUNNING [17/60] 451s: benchmarks/ops/bench_fused_moe.py::test_fused_moe_fwd_bench[qwen3-235b-decode-bfloat16]
RUNNING [17/60] 481s: benchmarks/ops/bench_fused_moe.py::test_fused_moe_fwd_bench[qwen3-235b-decode-bfloat16]
RUNNING [17/60] 511s: benchmarks/ops/bench_fused_moe.py::test_fused_moe_fwd_bench[ds-v3-grouped-decode-bfloat16]
RUNNING [17/60] 541s: benchmarks/ops/bench_fused_moe.py::test_fused_moe_fwd_bench[kimi-k2-prefill-bfloat16]
RUNNING [17/60] 571s: benchmarks/ops/bench_fused_moe.py::test_fused_moe_shared_expert_bench[kimi-k2-t32-bfloat16]
RUNNING [17/60] 601s: benchmarks/ops/bench_fused_moe.py::test_fused_moe_shared_expert_bench[kimi-k2-t128-bfloat16]
RUNNING [17/60] 631s: benchmarks/ops/bench_fused_moe.py::test_fused_moe_shared_expert_bench[kimi-k2-t2048-bfloat16]
RUNNING [17/60] 661s: benchmarks/ops/bench_fused_moe.py::test_fused_moe_shared_expert_bench[kimi-k2-t4096-bfloat16]
RUNNING [17/60] 691s: benchmarks/ops/bench_fused_moe.py::test_fused_moe_shared_expert_bench[ds-v3-grouped-t64-bfloat16]
RUNNING [17/60] 721s: benchmarks/ops/bench_fused_moe.py::test_fused_moe_shared_expert_bench[ds-v3-grouped-t4096-bfloat16]
RUNNING [17/60] 751s: benchmarks/ops/bench_fused_moe.py::test_fused_moe_shared_expert_bench[glm45-t512-bfloat16]
RUNNING [17/60] 781s: benchmarks/ops/bench_fused_moe.py::test_shared_expert_mlp_bench[kimi-k2-t1-bfloat16]
RUNNING [17/60] 811s: benchmarks/ops/bench_fused_moe.py::test_shared_expert_mlp_bench[kimi-k2-t512-bfloat16]
RUNNING [17/60] 841s: benchmarks/ops/bench_fused_moe.py::test_shared_expert_mlp_bench[ds-v3-t4096-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_fwd_bench[qwen3-235b-decode-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_fwd_bench[qwen3-235b-decode-float16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_fwd_bench[qwen3-235b-prefill-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_fwd_bench[ds-v3-grouped-decode-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_fwd_bench[ds-v3-grouped-prefill-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_fwd_bench[kimi-k2-decode-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_fwd_bench[kimi-k2-prefill-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_fwd_bench[qwen3-30b-decode-b1-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_fwd_bench[qwen3-30b-decode-b32-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_fwd_bench[gpt-oss-120b-decode-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_fwd_bench[gpt-oss-120b-prefill-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_fwd_bench[gpt-oss-20b-prefill-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_shared_expert_bench[kimi-k2-t1-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_shared_expert_bench[kimi-k2-t32-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_shared_expert_bench[kimi-k2-t64-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_shared_expert_bench[kimi-k2-t128-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_shared_expert_bench[kimi-k2-t512-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_shared_expert_bench[kimi-k2-t2048-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_shared_expert_bench[kimi-k2-t4096-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_shared_expert_bench[ds-v3-grouped-t1-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_shared_expert_bench[ds-v3-grouped-t32-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_shared_expert_bench[ds-v3-grouped-t32-float16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_shared_expert_bench[ds-v3-grouped-t64-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_shared_expert_bench[ds-v3-grouped-t128-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_shared_expert_bench[ds-v3-grouped-t512-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_shared_expert_bench[ds-v3-grouped-t2048-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_shared_expert_bench[ds-v3-grouped-t4096-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_shared_expert_bench[glm45-t1-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_shared_expert_bench[glm45-t32-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_shared_expert_bench[glm45-t64-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_shared_expert_bench[glm45-t128-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_shared_expert_bench[glm45-t512-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_shared_expert_bench[glm45-t2048-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_shared_expert_bench[glm45-t4096-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_fused_moe_shared_expert_bench[qwen3-235b-t512-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_shared_expert_mlp_bench[kimi-k2-t1-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_shared_expert_mlp_bench[kimi-k2-t512-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_shared_expert_mlp_bench[ds-v3-t32-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_shared_expert_mlp_bench[ds-v3-t32-float16]
benchmarks/ops/bench_fused_moe.py::test_shared_expert_mlp_bench[ds-v3-t4096-bfloat16]
benchmarks/ops/bench_fused_moe.py::test_shared_expert_mlp_bench[glm45-t32-bfloat16]

41 tests collected in 2.01s
.........................................                                [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_fused_moe.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
41 passed, 14 warnings in 859.62s (0:14:19)
--- benchmarks/ops/bench_fused_moe.py finished in 865s ---

=== [18/60] benchmarks/ops/bench_fused_moe_experts.py ===
RUNNING [18/60] 30s: benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_bench[qwen3-235b-prefill-float16]
RUNNING [18/60] 60s: benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_bench[ds-v3-decode-bfloat16]
RUNNING [18/60] 90s: benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_bench[ds-v3-prefill-bfloat16]
RUNNING [18/60] 120s: benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_bench[gpt-oss-20b-prefill-bfloat16]
RUNNING [18/60] 150s: benchmarks/ops/bench_fused_moe_experts.py::test_indexed_expert_mlp_bench[ds-v3-t64-float16]
benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_bench[qwen3-235b-decode-float16]
benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_bench[qwen3-235b-decode-bfloat16]
benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_bench[qwen3-235b-prefill-float16]
benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_bench[qwen3-235b-prefill-bfloat16]
benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_bench[ds-v3-decode-float16]
benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_bench[ds-v3-decode-bfloat16]
benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_bench[ds-v3-prefill-float16]
benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_bench[ds-v3-prefill-bfloat16]
benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_bench[gpt-oss-120b-decode-bfloat16]
benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_bench[gpt-oss-120b-prefill-bfloat16]
benchmarks/ops/bench_fused_moe_experts.py::test_moe_experts_bench[gpt-oss-20b-prefill-bfloat16]
benchmarks/ops/bench_fused_moe_experts.py::test_indexed_expert_mlp_bench[ds-v3-t1-float16]
benchmarks/ops/bench_fused_moe_experts.py::test_indexed_expert_mlp_bench[ds-v3-t1-bfloat16]
benchmarks/ops/bench_fused_moe_experts.py::test_indexed_expert_mlp_bench[ds-v3-t32-float16]
benchmarks/ops/bench_fused_moe_experts.py::test_indexed_expert_mlp_bench[ds-v3-t32-bfloat16]
benchmarks/ops/bench_fused_moe_experts.py::test_indexed_expert_mlp_bench[ds-v3-t64-float16]
benchmarks/ops/bench_fused_moe_experts.py::test_indexed_expert_mlp_bench[ds-v3-t64-bfloat16]
benchmarks/ops/bench_fused_moe_experts.py::test_indexed_expert_mlp_bench[qwen3-235b-t32-float16]
benchmarks/ops/bench_fused_moe_experts.py::test_indexed_expert_mlp_bench[qwen3-235b-t32-bfloat16]

19 tests collected in 1.92s
...................                                                      [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_fused_moe_experts.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
19 passed, 14 warnings in 172.69s (0:02:52)
--- benchmarks/ops/bench_fused_moe_experts.py finished in 178s ---

=== [19/60] benchmarks/ops/bench_fused_qk_norm_rope.py ===
benchmarks/ops/bench_fused_qk_norm_rope.py::test_fused_qk_norm_rope_bench[qwen3-8b-t64-bfloat16-bfloat16]
benchmarks/ops/bench_fused_qk_norm_rope.py::test_fused_qk_norm_rope_bench[qwen3-8b-t64-float16-float32]
benchmarks/ops/bench_fused_qk_norm_rope.py::test_fused_qk_norm_rope_bench[qwen3-8b-t8192-bfloat16-bfloat16]
benchmarks/ops/bench_fused_qk_norm_rope.py::test_fused_qk_norm_rope_bench[qwen3-235b-t4096-bfloat16-bfloat16]
benchmarks/ops/bench_fused_qk_norm_rope.py::test_fused_qk_norm_rope_bench[glm-4.5-partial-rope-bfloat16-float32]
benchmarks/ops/bench_fused_qk_norm_rope.py::test_fused_qk_norm_rope_bench[interleaved-ragged-float16-float16]
benchmarks/ops/bench_fused_qk_norm_rope.py::test_fused_qk_norm_rope_bench[interleaved-ragged-bfloat16-float32]

7 tests collected in 1.64s
.......                                                                  [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_fused_qk_norm_rope.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
7 passed, 14 warnings in 8.74s
--- benchmarks/ops/bench_fused_qk_norm_rope.py finished in 14s ---

=== [20/60] benchmarks/ops/bench_fused_topk.py ===
benchmarks/ops/bench_fused_topk.py::test_fused_topk_bench[kimi-k2-t32-bfloat16]
benchmarks/ops/bench_fused_topk.py::test_fused_topk_bench[kimi-k2-t512-bfloat16]
benchmarks/ops/bench_fused_topk.py::test_fused_topk_bench[kimi-k2-t4096-bfloat16]
benchmarks/ops/bench_fused_topk.py::test_fused_topk_bench[kimi-k2-t512-bias-bfloat16]
benchmarks/ops/bench_fused_topk.py::test_fused_topk_bench[kimi-k2-t512-bias-float16]
benchmarks/ops/bench_fused_topk.py::test_fused_topk_bench[kimi-k2-t512-bias-float32]
benchmarks/ops/bench_fused_topk.py::test_fused_topk_bench[qwen3-235b-t32-bfloat16]
benchmarks/ops/bench_fused_topk.py::test_fused_topk_bench[qwen3-235b-t512-bfloat16]
benchmarks/ops/bench_fused_topk.py::test_fused_topk_bench[qwen3-235b-t512-float16]
benchmarks/ops/bench_fused_topk.py::test_fused_topk_bench[qwen3-235b-t512-float32]
benchmarks/ops/bench_fused_topk.py::test_fused_topk_bench[qwen3-235b-t4096-bfloat16]
benchmarks/ops/bench_fused_topk.py::test_fused_topk_bench[ds-v3-grouped-t1-bfloat16]
benchmarks/ops/bench_fused_topk.py::test_fused_topk_bench[ds-v3-grouped-t32-bfloat16]
benchmarks/ops/bench_fused_topk.py::test_fused_topk_bench[ds-v3-grouped-t64-bfloat16]
benchmarks/ops/bench_fused_topk.py::test_fused_topk_bench[ds-v3-grouped-t64-float16]
benchmarks/ops/bench_fused_topk.py::test_fused_topk_bench[ds-v3-grouped-t64-float32]
benchmarks/ops/bench_fused_topk.py::test_fused_topk_bench[ds-v3-grouped-t4096-bfloat16]

17 tests collected in 1.83s
.................                                                        [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_fused_topk.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
17 passed, 14 warnings in 24.42s
--- benchmarks/ops/bench_fused_topk.py finished in 30s ---

=== [21/60] benchmarks/ops/bench_gdn.py ===
RUNNING [21/60] 30s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[prefill-4k-float16]
RUNNING [21/60] 60s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[prefill-32k-bfloat16]
RUNNING [21/60] 90s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[decode-b8-bfloat16]
RUNNING [21/60] 120s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[decode-beta-l2norm-bfloat16]
RUNNING [21/60] 150s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-16384-bfloat16]
RUNNING [21/60] 180s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-1024-7168-bfloat16]
RUNNING [21/60] 210s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-32x8192-float16]
RUNNING [21/60] 240s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-8192-float16]
RUNNING [21/60] 270s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-2048-6144-bfloat16]
RUNNING [21/60] 300s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-32x8192-float16]
RUNNING [21/60] 330s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-16384-float16]
RUNNING [21/60] 361s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-4096-4096-float16]
RUNNING [21/60] 391s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-8x8192-float16]
RUNNING [21/60] 421s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-65536-bfloat16]
RUNNING [21/60] 451s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-4096-float16]
RUNNING [21/60] 481s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-1024-7168-bfloat16]
RUNNING [21/60] 511s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-16x8192-bfloat16]
RUNNING [21/60] 541s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-65536-bfloat16]
RUNNING [21/60] 571s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-4096-float16]
RUNNING [21/60] 601s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-2048-6144-bfloat16]
RUNNING [21/60] 631s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-16x8192-bfloat16]
RUNNING [21/60] 661s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-32768-float16]
RUNNING [21/60] 691s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-2048-float16]
RUNNING [21/60] 721s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-1024-7168-bfloat16]
RUNNING [21/60] 751s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-16x8192-bfloat16]
RUNNING [21/60] 781s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-2b-16384-float16]
RUNNING [21/60] 811s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-2b-6144-2048-bfloat16]
RUNNING [21/60] 841s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-2b-8x1024-float16]
RUNNING [21/60] 871s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-65536-float16]
RUNNING [21/60] 901s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-8192-bfloat16]
RUNNING [21/60] 931s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-4096-4096-float16]
RUNNING [21/60] 961s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-8x1024-bfloat16]
RUNNING [21/60] 991s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-32x8192-bfloat16]
RUNNING [21/60] 1021s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-gva-decode-b8-float16]
RUNNING [21/60] 1051s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-gva-decode-b64-float16]
RUNNING [21/60] 1081s: benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-gva-decode-b512-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[prefill-4k-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[prefill-4k-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[prefill-12k-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[prefill-12k-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[prefill-32k-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[prefill-32k-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[decode-b1-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[decode-b1-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[decode-b8-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[decode-b8-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[prefill-continued-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[prefill-narrow-state-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[varlen-4x1k-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[varlen-ragged-grouped-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[prefill-3000-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[prefill-raw-4k-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[prefill-raw-ragged-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[decode-fresh-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[decode-gate-fused-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[decode-beta-l2norm-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[decode-vfirst-b17-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[prefill-v-first-4k-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[prefill-v-first-narrow-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[varlen-v-first-ragged-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-65536-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-65536-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-32768-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-32768-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-16384-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-16384-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-4096-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-4096-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-2048-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-2048-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-6144-2048-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-6144-2048-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-4096-4096-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-4096-4096-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-2048-6144-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-2048-6144-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-1024-7168-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-1024-7168-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-4x2048-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-4x2048-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-8x1024-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-8x1024-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-8x8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-8x8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-16x8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-16x8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-32x8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp8-32x8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-65536-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-65536-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-32768-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-32768-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-16384-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-16384-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-4096-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-4096-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-2048-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-2048-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-6144-2048-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-6144-2048-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-4096-4096-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-4096-4096-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-2048-6144-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-2048-6144-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-1024-7168-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-1024-7168-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-4x2048-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-4x2048-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-8x1024-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-8x1024-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-8x8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-8x8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-16x8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-16x8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-32x8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp4-32x8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-65536-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-65536-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-32768-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-32768-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-16384-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-16384-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-4096-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-4096-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-2048-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-2048-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-6144-2048-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-6144-2048-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-4096-4096-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-4096-4096-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-2048-6144-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-2048-6144-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-1024-7168-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-1024-7168-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-4x2048-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-4x2048-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-8x1024-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-8x1024-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-8x8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-8x8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-16x8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-16x8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-32x8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp2-32x8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-65536-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-65536-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-32768-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-32768-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-16384-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-16384-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-4096-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-4096-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-2048-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-2048-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-6144-2048-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-6144-2048-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-4096-4096-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-4096-4096-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-2048-6144-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-2048-6144-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-1024-7168-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-1024-7168-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-4x2048-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-4x2048-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-8x1024-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-8x1024-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-8x8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-8x8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-16x8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-16x8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-32x8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-397b-tp1-32x8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-65536-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-65536-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-32768-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-32768-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-16384-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-16384-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-4096-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-4096-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-2048-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-2048-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-6144-2048-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-6144-2048-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-4096-4096-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-4096-4096-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-2048-6144-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-2048-6144-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-1024-7168-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-1024-7168-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-4x2048-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-4x2048-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-8x1024-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-8x1024-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-8x8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-8x8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-16x8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-16x8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-32x8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-35b-32x8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-65536-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-65536-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-32768-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-32768-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-16384-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-16384-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-4096-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-4096-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-2048-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-2048-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-6144-2048-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-6144-2048-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-4096-4096-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-4096-4096-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-2048-6144-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-2048-6144-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-1024-7168-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-1024-7168-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-4x2048-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-4x2048-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-8x1024-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-8x1024-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-8x8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-8x8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-16x8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-16x8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-32x8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-27b-32x8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-2b-65536-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-2b-65536-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-2b-16384-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-2b-16384-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-2b-8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-2b-8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-2b-2048-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-2b-2048-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-2b-6144-2048-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-2b-6144-2048-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-2b-4096-4096-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-2b-4096-4096-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-2b-2048-6144-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-2b-2048-6144-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-2b-1024-7168-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-2b-1024-7168-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-2b-4x2048-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-2b-4x2048-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-2b-8x1024-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-2b-8x1024-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-2b-8x8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-2b-8x8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-2b-16x8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-2b-16x8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-2b-32x8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-2b-32x8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-65536-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-65536-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-32768-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-32768-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-16384-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-16384-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-4096-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-4096-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-2048-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-2048-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-6144-2048-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-6144-2048-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-4096-4096-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-4096-4096-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-2048-6144-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-2048-6144-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-1024-7168-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-1024-7168-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-4x2048-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-4x2048-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-8x1024-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-8x1024-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-8x8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-8x8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-16x8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-16x8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-32x8192-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-symmetric-32x8192-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-gva-decode-b1-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-gva-decode-b1-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-gva-decode-b4-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-gva-decode-b4-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-gva-decode-b8-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-gva-decode-b8-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-gva-decode-b16-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-gva-decode-b16-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-gva-decode-b32-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-gva-decode-b32-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-gva-decode-b64-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-gva-decode-b64-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-gva-decode-b128-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-gva-decode-b128-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-gva-decode-b256-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-gva-decode-b256-bfloat16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-gva-decode-b512-float16]
benchmarks/ops/bench_gdn.py::test_gdn_fwd_bench[q35-gva-decode-b512-bfloat16]

278 tests collected in 7.56s
........................................................................ [ 25%]
........................................................................ [ 51%]
........................................................................ [ 77%]
..............................................................           [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_gdn.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
278 passed, 14 warnings in 1073.89s (0:17:53)
--- benchmarks/ops/bench_gdn.py finished in 1086s ---

=== [22/60] benchmarks/ops/bench_gemm.py ===
RUNNING [22/60] 30s: benchmarks/ops/bench_gemm.py::test_gemm_bench[square-1k-bfloat16]
RUNNING [22/60] 60s: benchmarks/ops/bench_gemm.py::test_gemm_bench[ds-v3-prefill-qkv-a-bfloat16]
RUNNING [22/60] 90s: benchmarks/ops/bench_gemm.py::test_gemm_bench[ds-v3-prefill-mlp-up-bfloat16]
RUNNING [22/60] 120s: benchmarks/ops/bench_gemm.py::test_gemm_bench[ds-v3-prefill-o-proj-bfloat16]
RUNNING [22/60] 150s: benchmarks/ops/bench_gemm.py::test_gemm_bench[ds-v3-prefill-q-b-bfloat16]
RUNNING [22/60] 180s: benchmarks/ops/bench_gemm.py::test_gemm_bench[ds-v3-m64-down-bfloat16]
RUNNING [22/60] 210s: benchmarks/ops/bench_gemm.py::test_gemm_bench[ds-v3-m2-qkv-a-bfloat16]
RUNNING [22/60] 240s: benchmarks/ops/bench_gemm.py::test_gemm_bench[qwen3-8b-down-prefill-bfloat16]
RUNNING [22/60] 270s: benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-prefill-qkv-a-float8_e4m3fn-bfloat16]
RUNNING [22/60] 300s: benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-prefill-down-blk-float8_e4m3fn-bfloat16]
RUNNING [22/60] 330s: benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-m1-down-blk-float8_e4m3fn-bfloat16]
RUNNING [22/60] 360s: benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-decode-qkv-a-2d-float8_e4m3fn-bfloat16]
RUNNING [22/60] 391s: benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-decode-qkv-a-2d-float8_e4m3fn-bfloat16]
RUNNING [22/60] 421s: benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-prefill-qkv-a-2d-float8_e4m3fn-bfloat16]
RUNNING [22/60] 451s: benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-prefill-q-b-2d-float8_e4m3fn-bfloat16]
RUNNING [22/60] 481s: benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-kv-a-m128-s128-float8_e4m3fn-bfloat16]
RUNNING [22/60] 511s: benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-kv-b-m128-s1-float8_e4m3fn-bfloat16]
RUNNING [22/60] 541s: benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-mlp-up-m128-s1-float8_e4m3fn-bfloat16]
RUNNING [22/60] 571s: benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-kv-b-m4096-s128-float8_e4m3fn-bfloat16]
RUNNING [22/60] 601s: benchmarks/ops/bench_gemm.py::test_gemm_int8_w8a8_bench[llama3-70b-down-b1-bfloat16]
RUNNING [22/60] 631s: benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[single-tile-float16]
RUNNING [22/60] 661s: benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[decode-l2-resident-float16]
RUNNING [22/60] 691s: benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[decode-long-k-float16]
RUNNING [22/60] 721s: benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[llama-8b-prefill-down-float16]
RUNNING [22/60] 751s: benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-up-b1]
RUNNING [22/60] 781s: benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-tp8-4k]
RUNNING [22/60] 811s: benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-up-b48]
RUNNING [22/60] 841s: benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-up-tp8-b16]
RUNNING [22/60] 871s: benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-b97]
RUNNING [22/60] 901s: benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-down-b257]
RUNNING [22/60] 931s: benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-down-tp8-b192]
benchmarks/ops/bench_gemm.py::test_gemm_bench[square-1k-float16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[square-1k-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[ds-v3-decode-qkv-a-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[ds-v3-decode-down-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[ds-v3-prefill-qkv-a-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[ds-v3-prefill-down-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[ds-v3-prefill-mlp-up-float16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[ds-v3-prefill-mlp-up-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[ds-v3-prefill-o-proj-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[ds-v3-prefill-q-b-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[ds-v3-m16-mlp-up-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[ds-v3-m32-mlp-up-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[ds-v3-m64-down-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[ds-v3-m96-qkv-a-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[ds-v3-m1-qkv-a-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[ds-v3-m2-qkv-a-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[qwen3-8b-gate-up-decode-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[qwen3-8b-gate-up-b32-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[qwen3-8b-down-prefill-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_bench[vit-l16-in21k-head-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-decode-qkv-a-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-decode-down-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-prefill-qkv-a-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-prefill-down-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-decode-qkv-a-blk-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-decode-down-blk-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-prefill-qkv-a-blk-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-prefill-down-blk-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-prefill-mlp-up-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-prefill-o-proj-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-prefill-q-b-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-m8-down-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-m1-down-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-m1-down-blk-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-decode-qkv-a-2d-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-decode-down-2d-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-prefill-qkv-a-2d-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-prefill-down-2d-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-prefill-mlp-up-2d-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-prefill-o-proj-2d-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-prefill-q-b-2d-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-m1-down-2d-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-decode-qkv-a-bias-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-decode-qkv-a-float8_e4m3fn-float16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-decode-qkv-a-blk-float8_e4m3fn-float16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-kv-a-m128-s1-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-kv-a-m128-s128-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-q-b-m128-s1-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-q-b-m128-s128-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-kv-b-m128-s1-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-kv-b-m128-s128-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-o-proj-m128-s1-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-o-proj-m128-s128-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-mlp-up-m128-s1-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-mlp-up-m128-s128-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-kv-a-m4096-s1-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-kv-a-m4096-s128-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-kv-b-m4096-s1-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_fp8_bench[ds-v3-kv-b-m4096-s128-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_int8_w8a8_bench[llama3-8b-qkv-b1-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_int8_w8a8_bench[llama3-8b-qkv-b64-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_int8_w8a8_bench[llama3-8b-decode-qkv-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_int8_w8a8_bench[llama3-8b-prefill-qkv-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_int8_w8a8_bench[llama3-8b-down-b1-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_int8_w8a8_bench[llama3-8b-down-b64-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_int8_w8a8_bench[llama3-8b-decode-down-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_int8_w8a8_bench[llama3-8b-prefill-down-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_int8_w8a8_bench[llama3-8b-gate-up-b64-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_int8_w8a8_bench[llama3-8b-prefill-gateup-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_int8_w8a8_bench[llama3-70b-qkv-b1-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_int8_w8a8_bench[llama3-70b-qkv-b64-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_int8_w8a8_bench[llama3-70b-dec-qkv-tsr-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_int8_w8a8_bench[llama3-70b-prefill-qkv-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_int8_w8a8_bench[llama3-70b-down-b1-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_int8_w8a8_bench[llama3-70b-down-b64-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_int8_w8a8_bench[llama3-70b-prefill-down-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_int8_w8a8_bench[qwen2.5-7b-qkv-b1-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_int8_w8a8_bench[qwen2.5-7b-qkv-b64-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_int8_w8a8_bench[qwen2.5-7b-prefill-qkv-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_int8_w8a8_bench[qwen2.5-7b-down-b1-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_int8_w8a8_bench[qwen2.5-7b-down-b64-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_int8_w8a8_bench[qwen2.5-7b-prefill-down-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_int8_w8a8_bench[qwen2.5-72b-down-b1-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_int8_w8a8_bench[qwen2.5-72b-down-b64-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_int8_w8a8_bench[qwen2.5-72b-prefill-down-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_int8_w8a8_bench[llama3-8b-qkv-static-a-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_int8_w8a8_bench[llama3-8b-qkv-tensor-w-bfloat16]
benchmarks/ops/bench_gemm.py::test_gemm_int8_w8a8_bench[llama3-8b-down-b64-float16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[single-tile-float16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[multi-tile-float16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[decode-l2-resident-float16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[decode-hbm-streaming-float16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[decode-non-pow2-float16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[decode-long-k-float16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[decode-b2-float16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[decode-b8-float16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[decode-b32-float16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[chunked-prefill-tile-float16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[prefill-mlp-up-float16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[llama-8b-decode-down-float16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[llama-8b-prefill-down-float16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[qwen3-32b-prefill-down-float16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a16_bench[decode-tp8-attn-out-float16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-b1]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-b64]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-4k]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-up-b1]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-up-b64]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-up-4k]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-down-b1]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-down-b64]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-down-4k]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-up-b1]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-up-b64]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-up-4k]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-b2]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-b8]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-b16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-b32]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-b96]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-b128]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-b512]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-b1024]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-up-tp8-b1]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-up-tp8-4k]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-tp8-b1]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-tp8-4k]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-up-tp8-b1]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-down-tp8-b1]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-b33]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-b48]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-up-b32]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-up-b33]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-up-b48]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-down-b32]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-down-b33]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-down-b48]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-up-b32]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-up-b33]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-up-b48]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-up-tp8-b8]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-up-tp8-b16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-up-tp8-b32]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-up-tp8-b33]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-up-tp8-b48]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-up-tp8-b64]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-tp8-b8]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-tp8-b16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-tp8-b32]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-tp8-b33]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-tp8-b48]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-tp8-b64]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-up-tp8-b8]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-up-tp8-b16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-up-tp8-b32]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-up-tp8-b33]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-up-tp8-b48]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-up-tp8-b64]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-down-tp8-b8]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-down-tp8-b16]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-down-tp8-b32]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-down-tp8-b33]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-down-tp8-b48]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-down-tp8-b64]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-b65]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-b80]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-b81]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-b97]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-b129]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-b192]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-b193]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-b256]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-b257]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-b384]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-b385]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-b513]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-b576]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-b577]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-down-b65]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-down-b129]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-down-b193]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-down-b257]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-down-b513]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-tp8-b65]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-tp8-b96]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-tp8-b97]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-tp8-b128]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-tp8-b129]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-tp8-b160]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-tp8-b161]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-tp8-b192]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-tp8-b193]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-down-tp8-b256]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-down-tp8-b96]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-down-tp8-b129]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-down-tp8-b192]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[llama-70b-down-tp8-b256]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-up-b65]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-up-b129]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-up-b257]
benchmarks/ops/bench_gemm.py::test_gemm_w4a8_bench[ds-r1-up-b513]

201 tests collected in 4.17s
........................................................................ [ 35%]
........................................................................ [ 71%]
.........................................................                [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_gemm.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_gemm.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
201 passed, 58 warnings in 936.68s (0:15:36)
--- benchmarks/ops/bench_gemm.py finished in 946s ---

=== [23/60] benchmarks/ops/bench_gla.py ===
RUNNING [23/60] 30s: benchmarks/ops/bench_gla.py::test_gla_chunk_fwd_bench[train-2k-float16]
RUNNING [23/60] 60s: benchmarks/ops/bench_gla.py::test_gla_chunk_fwd_bench[train-8k-float16]
RUNNING [23/60] 90s: benchmarks/ops/bench_gla.py::test_gla_bwd_bench[train-2k-float16]
RUNNING [23/60] 120s: benchmarks/ops/bench_gla.py::test_gla_bwd_bench[train-4k-float16]
RUNNING [23/60] 150s: benchmarks/ops/bench_gla.py::test_gla_bwd_bench[train-4k-float16]
RUNNING [23/60] 180s: benchmarks/ops/bench_gla.py::test_gla_bwd_bench[train-8k-float16]
RUNNING [23/60] 210s: benchmarks/ops/bench_gla.py::test_gla_bwd_bench[train-16k-float16]
RUNNING [23/60] 240s: benchmarks/ops/bench_gla.py::test_gla_fwd_bench[varlen-ragged-float16]
RUNNING [23/60] 270s: benchmarks/ops/bench_gla.py::test_gla_fwd_bench[gla-continue-b4-bfloat16]
benchmarks/ops/bench_gla.py::test_gla_chunk_fwd_bench[train-2k-float16]
benchmarks/ops/bench_gla.py::test_gla_chunk_fwd_bench[train-2k-bfloat16]
benchmarks/ops/bench_gla.py::test_gla_chunk_fwd_bench[train-4k-float16]
benchmarks/ops/bench_gla.py::test_gla_chunk_fwd_bench[train-4k-bfloat16]
benchmarks/ops/bench_gla.py::test_gla_chunk_fwd_bench[train-8k-float16]
benchmarks/ops/bench_gla.py::test_gla_chunk_fwd_bench[train-8k-bfloat16]
benchmarks/ops/bench_gla.py::test_gla_chunk_fwd_bench[train-16k-float16]
benchmarks/ops/bench_gla.py::test_gla_chunk_fwd_bench[train-16k-bfloat16]
benchmarks/ops/bench_gla.py::test_gla_bwd_bench[train-2k-float16]
benchmarks/ops/bench_gla.py::test_gla_bwd_bench[train-2k-bfloat16]
benchmarks/ops/bench_gla.py::test_gla_bwd_bench[train-4k-float16]
benchmarks/ops/bench_gla.py::test_gla_bwd_bench[train-4k-bfloat16]
benchmarks/ops/bench_gla.py::test_gla_bwd_bench[train-8k-float16]
benchmarks/ops/bench_gla.py::test_gla_bwd_bench[train-8k-bfloat16]
benchmarks/ops/bench_gla.py::test_gla_bwd_bench[train-16k-float16]
benchmarks/ops/bench_gla.py::test_gla_bwd_bench[train-16k-bfloat16]
benchmarks/ops/bench_gla.py::test_gla_fwd_bench[prefill-2k-bfloat16]
benchmarks/ops/bench_gla.py::test_gla_fwd_bench[prefill-4k-bfloat16]
benchmarks/ops/bench_gla.py::test_gla_fwd_bench[prefill-8k-bfloat16]
benchmarks/ops/bench_gla.py::test_gla_fwd_bench[prefill-16k-bfloat16]
benchmarks/ops/bench_gla.py::test_gla_fwd_bench[varlen-4x1k-bfloat16]
benchmarks/ops/bench_gla.py::test_gla_fwd_bench[varlen-ragged-float16]
benchmarks/ops/bench_gla.py::test_gla_fwd_bench[prefill-3000-bfloat16]
benchmarks/ops/bench_gla.py::test_gla_fwd_bench[decode-b1-d64-bfloat16]
benchmarks/ops/bench_gla.py::test_gla_fwd_bench[decode-b8-d128-bfloat16]
benchmarks/ops/bench_gla.py::test_gla_fwd_bench[decode-first-token-float16]
benchmarks/ops/bench_gla.py::test_gla_fwd_bench[gla-short-continuation-bfloat16]
benchmarks/ops/bench_gla.py::test_gla_fwd_bench[gla-continue-b4-bfloat16]
benchmarks/ops/bench_gla.py::test_gla_decode_bench[serving-b1-h8-bfloat16]
benchmarks/ops/bench_gla.py::test_gla_decode_bench[serving-b1-h16-bfloat16]
benchmarks/ops/bench_gla.py::test_gla_decode_bench[serving-b1-h32-bfloat16]
benchmarks/ops/bench_gla.py::test_gla_decode_bench[serving-b1-h48-bfloat16]
benchmarks/ops/bench_gla.py::test_gla_decode_bench[serving-b1-h64-bfloat16]
benchmarks/ops/bench_gla.py::test_gla_decode_bench[serving-b8-h32-bfloat16]
benchmarks/ops/bench_gla.py::test_gla_decode_bench[serving-b8-h48-bfloat16]
benchmarks/ops/bench_gla.py::test_gla_decode_bench[serving-b8-h64-bfloat16]

=============================== warnings summary ===============================
../../../../../../usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
36 tests collected in 13.01s
....................................                                     [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_gla.py: 57 warnings
  /usr/local/lib/python3.12/dist-packages/tilelang/jit/kernel.py:161: DeprecationWarning: `tl.disable_tma_lower` is deprecated and will be removed in v0.1.10. Use `T.copy(..., disable_tma=True)` per-copy instead.
    instance = cls(

benchmarks/ops/bench_gla.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/tilelang/cache/kernel_cache.py:394: DeprecationWarning: `tl.disable_tma_lower` is deprecated and will be removed in v0.1.10. Use `T.copy(..., disable_tma=True)` per-copy instead.
    kernel = JITKernel(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
36 passed, 71 warnings in 267.01s (0:04:27)
--- benchmarks/ops/bench_gla.py finished in 285s ---

=== [24/60] benchmarks/ops/bench_gqa.py ===
RUNNING [24/60] 30s: benchmarks/ops/bench_gqa.py::test_gqa_bwd_bench[llama-70b-short-bfloat16]
RUNNING [24/60] 60s: benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[llama-8b-4k-float16]
RUNNING [24/60] 90s: benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[llama-8b-4k-bfloat16]
RUNNING [24/60] 120s: benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[llama-8b-softcap-float16]
RUNNING [24/60] 150s: benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[falcon-7b-2k-bfloat16]
RUNNING [24/60] 180s: benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[gemma-2b-8k-bs1-bfloat16]
RUNNING [24/60] 210s: benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[gemma-2b-8k-b16-float16]
RUNNING [24/60] 240s: benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[prefill-rope-float16]
RUNNING [24/60] 270s: benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[prefill-rope-float16]
RUNNING [24/60] 300s: benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[gpt-oss-sinks-prefill-2k-bfloat16]
RUNNING [24/60] 330s: benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[gpt-oss-sinks-prefill-2k-bfloat16]
RUNNING [24/60] 360s: benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[gpt-oss-sinks-prefill-4k-bfloat16]
RUNNING [24/60] 391s: benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[gpt-oss-sinks-prefill-8k-float16]
RUNNING [24/60] 421s: benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[gpt-oss-sinks-prefill-8k-float16]
RUNNING [24/60] 451s: benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[gpt-oss-sinks-window-128-float16]
RUNNING [24/60] 481s: benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[gpt-oss-sinks-window-128-float16]
RUNNING [24/60] 511s: benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[gpt-oss-sinks-window-128-bfloat16]
RUNNING [24/60] 541s: benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[gpt-oss-sinks-window-128-bfloat16]
RUNNING [24/60] 571s: benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[gpt-oss-sinks-decode-8k-bfloat16]
RUNNING [24/60] 601s: benchmarks/ops/bench_gqa.py::test_gqa_dense_with_lse_fwd_bench[llama-8b-short-float16]
RUNNING [24/60] 631s: benchmarks/ops/bench_gqa.py::test_gqa_dense_with_lse_fwd_bench[llama-8b-short-bfloat16]
RUNNING [24/60] 661s: benchmarks/ops/bench_gqa.py::test_gqa_dense_with_lse_fwd_bench[llama-8b-long-float16]
RUNNING [24/60] 691s: benchmarks/ops/bench_gqa.py::test_gqa_dense_with_lse_fwd_bench[llama-8b-long-bfloat16]
RUNNING [24/60] 721s: benchmarks/ops/bench_gqa.py::test_gqa_dense_with_lse_fwd_bench[llama-70b-long-bfloat16]
RUNNING [24/60] 751s: benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-uniform-float16]
RUNNING [24/60] 781s: benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-uniform-float16]
RUNNING [24/60] 811s: benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-uniform-float16]
RUNNING [24/60] 841s: benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-uniform-bfloat16]
RUNNING [24/60] 871s: benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-uniform-bfloat16]
RUNNING [24/60] 901s: benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[gpt-oss-uniform-float16]
RUNNING [24/60] 931s: benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[gpt-oss-uniform-float16]
RUNNING [24/60] 961s: benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[gpt-oss-uniform-bfloat16]
RUNNING [24/60] 991s: benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[gpt-oss-uniform-bfloat16]
RUNNING [24/60] 1021s: benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-short-w256-float16]
RUNNING [24/60] 1051s: benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-short-w256-float16]
RUNNING [24/60] 1081s: benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-short-w256-bfloat16]
RUNNING [24/60] 1112s: benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-short-w256-bfloat16]
RUNNING [24/60] 1142s: benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-70b-long-w1024-float16]
RUNNING [24/60] 1172s: benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[gpt-oss-rope-interleaved-float16]
RUNNING [24/60] 1202s: benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-70b-fp8-q-lt-kv-float8_e4m3fn-bfloat16]
RUNNING [24/60] 1232s: benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-p64-float16-float16]
RUNNING [24/60] 1262s: benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-b64-p64-float16-float16]
RUNNING [24/60] 1292s: benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-p64-softcap-float16-float16]
RUNNING [24/60] 1322s: benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-b64-p16-float16-float16]
RUNNING [24/60] 1352s: benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-p256-cut-float16-float16]
RUNNING [24/60] 1382s: benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-sliding-window-float16-float16]
::warning::Benchmark sweep exceeded 7200s; continuing [24/60] benchmarks/ops/bench_gqa.py
RUNNING [24/60] 1412s: benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[gpt-oss-120b-window-bfloat16-bfloat16]
RUNNING [24/60] 1442s: benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[gpt-oss-120b-window-bfloat16-bfloat16]
RUNNING [24/60] 1472s: benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[qwen3-ragged-odd-bfloat16-bfloat16]
RUNNING [24/60] 1502s: benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[qwen-ragged-rope-bfloat16-bfloat16]
RUNNING [24/60] 1532s: benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-fp8kv-decode-float16-float8_e4m3fn]
RUNNING [24/60] 1562s: benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-70b-fp8kv-p16-bfloat16-float8_e4m3fn]
RUNNING [24/60] 1592s: benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-fp8kv-prefill-bfloat16-float8_e4m3fn]
RUNNING [24/60] 1622s: benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-fp8-decode-float8_e4m3fn-float8_e4m3fn-bfloat16]
RUNNING [24/60] 1652s: benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[qwen35-9b-rope-chunk-float16-float16]
RUNNING [24/60] 1682s: benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[synthetic-softcap-chunk-float16-float16]
RUNNING [24/60] 1712s: benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[synthetic-softcap-chunk-float16-float16]
RUNNING [24/60] 1742s: benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[synthetic-softcap-chunk-float16-float16]
RUNNING [24/60] 1772s: benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[gemma-2b-chunk-bfloat16-bfloat16]
RUNNING [24/60] 1802s: benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[gemma-2b-chunk-bfloat16-bfloat16]
RUNNING [24/60] 1833s: benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[qwen35-9b-chunk-fp8kv-float16-float8_e4m3fn]
RUNNING [24/60] 1863s: benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[softcap-chunk-fp8kv-float16-float8_e4m3fn]
benchmarks/ops/bench_gqa.py::test_gqa_bwd_bench[llama-8b-short-float16]
benchmarks/ops/bench_gqa.py::test_gqa_bwd_bench[llama-8b-short-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_bwd_bench[llama-8b-long-float16]
benchmarks/ops/bench_gqa.py::test_gqa_bwd_bench[llama-8b-long-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_bwd_bench[llama-70b-short-float16]
benchmarks/ops/bench_gqa.py::test_gqa_bwd_bench[llama-70b-short-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_bwd_bench[llama-70b-long-float16]
benchmarks/ops/bench_gqa.py::test_gqa_bwd_bench[llama-70b-long-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_bwd_bench[llama-8b-short-mha-float16]
benchmarks/ops/bench_gqa.py::test_gqa_bwd_bench[llama-8b-short-mha-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_bwd_bench[llama-8b-long-mha-float16]
benchmarks/ops/bench_gqa.py::test_gqa_bwd_bench[llama-8b-long-mha-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_bwd_bench[llama-70b-short-mha-float16]
benchmarks/ops/bench_gqa.py::test_gqa_bwd_bench[llama-70b-short-mha-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_bwd_bench[llama-70b-long-mha-float16]
benchmarks/ops/bench_gqa.py::test_gqa_bwd_bench[llama-70b-long-mha-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[llama-8b-4k-float16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[llama-8b-4k-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[llama-8b-32k-float16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[llama-8b-32k-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[llama-70b-4k-float16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[llama-70b-4k-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[llama-70b-32k-float16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[llama-70b-32k-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[llama-8b-softcap-float16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[qwen3-30b-1k-float16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[qwen3-30b-4k-float16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[qwen3-30b-8k-float16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[qwen3-30b-16k-float16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[qwen3-30b-32k-float16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[qwen3-30b-64k-float16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[qwen3-30b-128k-float16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[qwen3-30b-256k-float16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[falcon-7b-2k-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[starcoder-8k-float16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[starcoderbase-3b-8k-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[gemma-2b-8k-bs1-float16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[gemma-2b-8k-bs1-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[gemma-2b-8k-b16-float16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[gemma-2b-8k-b16-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[prefill-rope-float16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[prefill-rope-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[prefill-scaled-float8_e4m3fn-float16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[qwen3-8b-chunked-prefill-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[qwen3-8b-chunked-b8-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[gpt-oss-sinks-prefill-2k-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[gpt-oss-sinks-prefill-4k-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[gpt-oss-sinks-prefill-8k-float16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[gpt-oss-sinks-prefill-8k-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[gpt-oss-sinks-window-128-float16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[gpt-oss-sinks-window-128-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[gpt-oss-sinks-decode-8k-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[scaled-fp8-sinks-prefill-float8_e4m3fn-float16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_with_lse_fwd_bench[llama-8b-short-float16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_with_lse_fwd_bench[llama-8b-short-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_with_lse_fwd_bench[llama-8b-long-float16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_with_lse_fwd_bench[llama-8b-long-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_with_lse_fwd_bench[llama-70b-long-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_dense_with_lse_fwd_bench[llama-8b-long-mha-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-uniform-float16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-uniform-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-q-lt-kv-float16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-q-lt-kv-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-70b-q-lt-kv-float16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-70b-q-lt-kv-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[gpt-oss-uniform-float16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[gpt-oss-uniform-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[gpt-oss-q-lt-kv-float16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[gpt-oss-q-lt-kv-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-short-w256-float16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-short-w256-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-long-w1024-float16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-long-w1024-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-70b-short-w256-float16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-70b-short-w256-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-70b-long-w1024-float16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-70b-long-w1024-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[gemma4-31b-uniform-float16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[gemma4-31b-uniform-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[gemma4-31b-q-lt-kv-float16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[gemma4-31b-q-lt-kv-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[gemma4-26b-a4b-ragged-float16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[gemma4-26b-a4b-ragged-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-uniform-rope-float16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-uniform-rope-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[gpt-oss-rope-interleaved-float16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[gpt-oss-rope-interleaved-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-rope-partial-float16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-rope-partial-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[qwen-ragged-rope-float16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[qwen-ragged-rope-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-fp8-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-70b-fp8-q-lt-kv-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[qwen3-fp8-ragged-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-fp8-w256-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[gpt-oss-sink-mixed-float16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[gpt-oss-sink-mixed-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_varlen_fwd_bench[llama-8b-fp8-sink-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-float16-float16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-p64-float16-float16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-32k-p64-float16-float16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-b64-p64-float16-float16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-70b-p64-float16-float16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-p256-float16-float16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-70b-p256-float16-float16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-405b-p256-float16-float16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-p64-softcap-float16-float16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-p16-float16-float16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-b64-p16-float16-float16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-70b-p16-float16-float16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-p64-cut-float16-float16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-p256-cut-float16-float16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-serving-step-float16-float16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-sliding-window-float16-float16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-noncausal-float16-float16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[gpt-oss-120b-window-bfloat16-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[qwen3-ragged-odd-bfloat16-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-rope-decode-float16-float16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-rope-decode-bfloat16-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-rope-prefill-float16-float16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-rope-prefill-bfloat16-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[qwen-ragged-rope-float16-float16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[qwen-ragged-rope-bfloat16-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[gpt-oss-sink-mixed-bfloat16-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[gpt-oss-sink-decode-bfloat16-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-fp8kv-decode-float16-float8_e4m3fn]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-fp8kv-decode-bfloat16-float8_e4m3fn]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-70b-fp8kv-p16-bfloat16-float8_e4m3fn]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-fp8kv-prefill-float16-float8_e4m3fn]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-fp8kv-prefill-bfloat16-float8_e4m3fn]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-fp8-decode-float8_e4m3fn-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-fp8-prefill-float8_e4m3fn-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[qwen3-fp8-ragged-odd-float8_e4m3fn-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[qwen-fp8kv-ragged-rope-bfloat16-float8_e4m3fn]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[qwen35-9b-rope-chunk-float16-float16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[qwen35-9b-mixed-chunk-float16-float16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-rope-chunk-float16-float16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[synthetic-softcap-chunk-float16-float16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[falcon-7b-chunk-bfloat16-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[starcoder-chunk-float16-float16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[gemma-2b-chunk-bfloat16-bfloat16]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[qwen35-9b-chunk-fp8kv-float16-float8_e4m3fn]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[llama-8b-chunk-fp8kv-float16-float8_e4m3fn]
benchmarks/ops/bench_gqa.py::test_gqa_paged_fwd_bench[softcap-chunk-fp8kv-float16-float8_e4m3fn]

144 tests collected in 7.86s
........................................................................ [ 50%]
........................................................................ [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_gqa.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

benchmarks/ops/bench_gqa.py::test_gqa_dense_fwd_bench[prefill-rope-float16]
  /usr/local/lib/python3.12/dist-packages/torch/_inductor/compile_fx.py:321: UserWarning: TensorFloat32 tensor cores for float32 matrix multiplication available but not enabled. Consider setting `torch.set_float32_matmul_precision('high')` for better performance.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
144 passed, 15 warnings in 1869.60s (0:31:09)
--- benchmarks/ops/bench_gqa.py finished in 1882s ---

=== [25/60] benchmarks/ops/bench_group_norm.py ===
RUNNING [25/60] 30s: benchmarks/ops/bench_group_norm.py::test_group_norm_no_affine_bench[image-float16]
benchmarks/ops/bench_group_norm.py::test_group_norm_bench[image-affine-float16]
benchmarks/ops/bench_group_norm.py::test_group_norm_bench[image-affine-bfloat16]
benchmarks/ops/bench_group_norm.py::test_group_norm_bench[wider-channel-affine-float16]
benchmarks/ops/bench_group_norm.py::test_group_norm_bench[wider-channel-affine-float32]
benchmarks/ops/bench_group_norm.py::test_group_norm_bench[tail-spatial-affine-float16]
benchmarks/ops/bench_group_norm.py::test_group_norm_no_affine_bench[image-float16]
benchmarks/ops/bench_group_norm.py::test_group_norm_no_affine_bench[image-bfloat16]
benchmarks/ops/bench_group_norm.py::test_group_norm_no_affine_bench[wider-channel-float16]
benchmarks/ops/bench_group_norm.py::test_group_norm_no_affine_bench[wider-channel-float32]
benchmarks/ops/bench_group_norm.py::test_group_norm_no_affine_bench[tail-spatial-float16]

10 tests collected in 3.16s
..........                                                               [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_group_norm.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_group_norm.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
10 passed, 58 warnings in 37.49s
--- benchmarks/ops/bench_group_norm.py finished in 44s ---

=== [26/60] benchmarks/ops/bench_grouped_gemm.py ===
RUNNING [26/60] 30s: benchmarks/ops/bench_grouped_gemm.py::test_grouped_gemm_bench[moe-fwd-bfloat16]
RUNNING [26/60] 60s: benchmarks/ops/bench_grouped_gemm.py::test_grouped_gemm_bench[qwen3-30b-ep8-routed1k-bfloat16]
benchmarks/ops/bench_grouped_gemm.py::test_grouped_gemm_bench[moe-fwd-float16]
benchmarks/ops/bench_grouped_gemm.py::test_grouped_gemm_bench[moe-fwd-bfloat16]
benchmarks/ops/bench_grouped_gemm.py::test_grouped_gemm_bench[moe-dgrad-float16]
benchmarks/ops/bench_grouped_gemm.py::test_grouped_gemm_bench[moe-wgrad-float16]
benchmarks/ops/bench_grouped_gemm.py::test_grouped_gemm_bench[qwen3-30b-ep8-empty-bfloat16]
benchmarks/ops/bench_grouped_gemm.py::test_grouped_gemm_bench[qwen3-30b-ep8-routed1k-bfloat16]
benchmarks/ops/bench_grouped_gemm.py::test_grouped_gemm_bench[qwen3-30b-ep8-ragged-bfloat16]

7 tests collected in 1.69s
.......                                                                  [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_grouped_gemm.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
7 passed, 14 warnings in 64.76s (0:01:04)
--- benchmarks/ops/bench_grouped_gemm.py finished in 70s ---

=== [27/60] benchmarks/ops/bench_hadamard_transform.py ===
benchmarks/ops/bench_hadamard_transform.py::test_hadamard_transform_bench[llama-8b-prefill-float16]
benchmarks/ops/bench_hadamard_transform.py::test_hadamard_transform_bench[llama-8b-prefill-bfloat16]
benchmarks/ops/bench_hadamard_transform.py::test_hadamard_transform_bench[llama-8b-decode-bfloat16]
benchmarks/ops/bench_hadamard_transform.py::test_hadamard_transform_bench[llama-70b-prefill-bfloat16]
benchmarks/ops/bench_hadamard_transform.py::test_hadamard_transform_bench[llama-70b-decode-bfloat16]
benchmarks/ops/bench_hadamard_transform.py::test_hadamard_transform_bench[llama3-head-dim-bfloat16]
benchmarks/ops/bench_hadamard_transform.py::test_hadamard_transform_bench[non-pow2-order20-bfloat16]

7 tests collected in 1.50s
.......                                                                  [100%]Benchmark report saved to profile_run.log

7 passed in 2.81s
--- benchmarks/ops/bench_hadamard_transform.py finished in 7s ---

=== [28/60] benchmarks/ops/bench_instance_norm.py ===
RUNNING [28/60] 30s: benchmarks/ops/bench_instance_norm.py::test_instance_norm_bench[image-bfloat16]
benchmarks/ops/bench_instance_norm.py::test_instance_norm_bench[image-affine-float16]
benchmarks/ops/bench_instance_norm.py::test_instance_norm_bench[image-affine-bfloat16]
benchmarks/ops/bench_instance_norm.py::test_instance_norm_bench[wider-channel-affine-float16]
benchmarks/ops/bench_instance_norm.py::test_instance_norm_bench[wider-channel-affine-float32]
benchmarks/ops/bench_instance_norm.py::test_instance_norm_bench[tail-spatial-affine-float16]
benchmarks/ops/bench_instance_norm.py::test_instance_norm_bench[image-float16]
benchmarks/ops/bench_instance_norm.py::test_instance_norm_bench[image-bfloat16]
benchmarks/ops/bench_instance_norm.py::test_instance_norm_bench[wider-channel-float16]
benchmarks/ops/bench_instance_norm.py::test_instance_norm_bench[wider-channel-float32]
benchmarks/ops/bench_instance_norm.py::test_instance_norm_bench[tail-spatial-float16]
benchmarks/ops/bench_instance_norm.py::test_instance_norm_bench[image-track-stats-float16]
benchmarks/ops/bench_instance_norm.py::test_instance_norm_bench[image-eval-float16]

12 tests collected in 1.59s
............                                                             [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_instance_norm.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_instance_norm.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
12 passed, 58 warnings in 42.99s
--- benchmarks/ops/bench_instance_norm.py finished in 47s ---

=== [29/60] benchmarks/ops/bench_int4_quant_per_group.py ===
benchmarks/ops/bench_int4_quant_per_group.py::test_int4_quant_per_group_bench[llama-8b-mlp-up-float16]
benchmarks/ops/bench_int4_quant_per_group.py::test_int4_quant_per_group_bench[llama-8b-q-proj-float16]
benchmarks/ops/bench_int4_quant_per_group.py::test_int4_quant_per_group_bench[llama-70b-mlp-down-float16]
benchmarks/ops/bench_int4_quant_per_group.py::test_int4_quant_per_group_bench[qwen3-32b-o-proj-float16]
benchmarks/ops/bench_int4_quant_per_group.py::test_int4_quant_per_group_bench[qwen2-7b-mlp-up-float16]
benchmarks/ops/bench_int4_quant_per_group.py::test_int4_quant_per_group_bench[qwen2-7b-mlp-down-float16]
benchmarks/ops/bench_int4_quant_per_group.py::test_int4_quant_per_group_bench[opt-13b-mlp-up-float16]
benchmarks/ops/bench_int4_quant_per_group.py::test_int4_quant_per_group_bench[llama-8b-mlp-up-chan-float16]

8 tests collected in 1.55s
........                                                                 [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_int4_quant_per_group.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
8 passed, 14 warnings in 7.61s
--- benchmarks/ops/bench_int4_quant_per_group.py finished in 12s ---

=== [30/60] benchmarks/ops/bench_int8_dequant.py ===
benchmarks/ops/bench_int8_dequant.py::test_int8_dequant_per_channel_bench[llama-8b-mlp-up-bfloat16]
benchmarks/ops/bench_int8_dequant.py::test_int8_dequant_per_channel_bench[llama-8b-mlp-up-float16]
benchmarks/ops/bench_int8_dequant.py::test_int8_dequant_per_channel_bench[llama-70b-mlp-down-bfloat16]
benchmarks/ops/bench_int8_dequant.py::test_int8_dequant_per_channel_bench[llama-8b-mlp-down-float32]
benchmarks/ops/bench_int8_dequant.py::test_int8_dequant_per_channel_bench[gpt-oss-20b-mlp-up-bfloat16]
benchmarks/ops/bench_int8_dequant.py::test_int8_dequant_per_channel_bench[ragged-k-float16]
benchmarks/ops/bench_int8_dequant.py::test_int8_dequant_per_channel_bench[ragged-k-few-rows-bfloat16]
benchmarks/ops/bench_int8_dequant.py::test_int8_dequant_per_tensor_bench[llama-8b-prefill-bfloat16]
benchmarks/ops/bench_int8_dequant.py::test_int8_dequant_per_tensor_bench[llama-8b-decode-bfloat16]
benchmarks/ops/bench_int8_dequant.py::test_int8_dequant_per_tensor_bench[qwen3-32b-prefill-float16]
benchmarks/ops/bench_int8_dequant.py::test_int8_dequant_per_tensor_bench[qwen3-32b-prefill-float32]
benchmarks/ops/bench_int8_dequant.py::test_int8_dequant_per_tensor_bench[gpt-oss-prefill-bfloat16]
benchmarks/ops/bench_int8_dequant.py::test_int8_dequant_per_tensor_bench[ragged-k-float32]
benchmarks/ops/bench_int8_dequant.py::test_int8_dequant_per_tensor_bench[ragged-k-few-rows-float16]
benchmarks/ops/bench_int8_dequant.py::test_int8_dequant_per_block_bench[ds-v3-prefill-bfloat16]
benchmarks/ops/bench_int8_dequant.py::test_int8_dequant_per_block_bench[ds-v3-decode-bfloat16]
benchmarks/ops/bench_int8_dequant.py::test_int8_dequant_per_block_bench[qwen3-235b-prefill-float16]
benchmarks/ops/bench_int8_dequant.py::test_int8_dequant_per_block_bench[gpt-oss-prefill-bfloat16]
benchmarks/ops/bench_int8_dequant.py::test_int8_dequant_per_block_bench[ragged-k-float32]
benchmarks/ops/bench_int8_dequant.py::test_int8_dequant_per_block_bench[ragged-k-few-rows-float16]

20 tests collected in 1.54s
....................                                                     [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_int8_dequant.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
20 passed, 14 warnings in 18.34s
--- benchmarks/ops/bench_int8_dequant.py finished in 23s ---

=== [31/60] benchmarks/ops/bench_int8_quant_per_block.py ===
benchmarks/ops/bench_int8_quant_per_block.py::test_int8_quant_per_block_bench[ds-v3-prefill-float16]
benchmarks/ops/bench_int8_quant_per_block.py::test_int8_quant_per_block_bench[ds-v3-prefill-bfloat16]
benchmarks/ops/bench_int8_quant_per_block.py::test_int8_quant_per_block_bench[ds-v3-decode-bfloat16]
benchmarks/ops/bench_int8_quant_per_block.py::test_int8_quant_per_block_bench[qwen3-235b-prefill-bfloat16]
benchmarks/ops/bench_int8_quant_per_block.py::test_int8_quant_per_block_bench[qwen3-235b-prefill-float32]
benchmarks/ops/bench_int8_quant_per_block.py::test_int8_quant_per_block_bench[ds-v3-decode-few-tokens-bfloat16]
benchmarks/ops/bench_int8_quant_per_block.py::test_int8_quant_per_block_bench[gpt-oss-20b-prefill-bfloat16]
benchmarks/ops/bench_int8_quant_per_block.py::test_int8_quant_per_block_bench[ragged-k-float16]

8 tests collected in 1.54s
........                                                                 [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_int8_quant_per_block.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
8 passed, 14 warnings in 12.86s
--- benchmarks/ops/bench_int8_quant_per_block.py finished in 17s ---

=== [32/60] benchmarks/ops/bench_int8_quant_per_channel.py ===
benchmarks/ops/bench_int8_quant_per_channel.py::test_int8_quant_per_channel_bench[llama-8b-mlp-up-float16]
benchmarks/ops/bench_int8_quant_per_channel.py::test_int8_quant_per_channel_bench[llama-8b-mlp-up-bfloat16]
benchmarks/ops/bench_int8_quant_per_channel.py::test_int8_quant_per_channel_bench[llama-70b-mlp-down-bfloat16]
benchmarks/ops/bench_int8_quant_per_channel.py::test_int8_quant_per_channel_bench[qwen3-32b-o-proj-bfloat16]
benchmarks/ops/bench_int8_quant_per_channel.py::test_int8_quant_per_channel_bench[qwen3-32b-o-proj-float32]
benchmarks/ops/bench_int8_quant_per_channel.py::test_int8_quant_per_channel_bench[gpt-oss-20b-mlp-up-bfloat16]
benchmarks/ops/bench_int8_quant_per_channel.py::test_int8_quant_per_channel_bench[ragged-k-float16]
benchmarks/ops/bench_int8_quant_per_channel.py::test_int8_quant_per_channel_bench[ragged-k-few-rows-bfloat16]

8 tests collected in 1.51s
........                                                                 [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_int8_quant_per_channel.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
8 passed, 14 warnings in 9.53s
--- benchmarks/ops/bench_int8_quant_per_channel.py finished in 13s ---

=== [33/60] benchmarks/ops/bench_int8_quant_per_tensor.py ===
benchmarks/ops/bench_int8_quant_per_tensor.py::test_int8_quant_per_tensor_bench[llama-8b-prefill-float16]
benchmarks/ops/bench_int8_quant_per_tensor.py::test_int8_quant_per_tensor_bench[llama-8b-prefill-bfloat16]
benchmarks/ops/bench_int8_quant_per_tensor.py::test_int8_quant_per_tensor_bench[llama-8b-decode-bfloat16]
benchmarks/ops/bench_int8_quant_per_tensor.py::test_int8_quant_per_tensor_bench[qwen3-32b-prefill-bfloat16]
benchmarks/ops/bench_int8_quant_per_tensor.py::test_int8_quant_per_tensor_bench[qwen3-32b-prefill-float32]
benchmarks/ops/bench_int8_quant_per_tensor.py::test_int8_quant_per_tensor_bench[gpt-oss-20b-decode-bfloat16]
benchmarks/ops/bench_int8_quant_per_tensor.py::test_int8_quant_per_tensor_bench[gpt-oss-20b-prefill-bfloat16]
benchmarks/ops/bench_int8_quant_per_tensor.py::test_int8_quant_per_tensor_bench[odd-hidden-prefill-float16]

8 tests collected in 1.54s
........                                                                 [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_int8_quant_per_tensor.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
8 passed, 14 warnings in 12.87s
--- benchmarks/ops/bench_int8_quant_per_tensor.py finished in 18s ---

=== [34/60] benchmarks/ops/bench_kda.py ===
RUNNING [34/60] 30s: benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kl48-tp1-s16384-bfloat16]
RUNNING [34/60] 60s: benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kl48-tp8-s131072-bfloat16]
RUNNING [34/60] 90s: benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kimi-k3-tp4-s4096-bfloat16]
RUNNING [34/60] 120s: benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kimi-k3-tp1-mixed8k-bfloat16]
RUNNING [34/60] 150s: benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-tp2-65536-bfloat16]
RUNNING [34/60] 180s: benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-tp1-1024-7168-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-tp1-4x1024-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-tp1-4x1024-float16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-tp1-4x8192-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-tp1-decode-b1-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-tp1-decode-b64-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-tp1-raw-gate-4096-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-raw-gate-decode-b8-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-bounded-packed-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kl48-tp1-s1024-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kl48-tp1-s16384-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kl48-tp2-s4096-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kl48-tp2-s32768-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kl48-tp4-s4096-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kl48-tp4-s65536-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kl48-tp8-s4096-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kl48-tp8-s131072-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kl48-tp1-mixed8k-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kl48-tp8-4x8192-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kl48-tp8-cont256-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kl48-tp8-cont4096-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kl48-tp8-b32-s256-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kimi-k3-tp1-s1024-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kimi-k3-tp1-s4096-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kimi-k3-tp1-s16384-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kimi-k3-tp2-s4096-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kimi-k3-tp2-s32768-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kimi-k3-tp4-s4096-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kimi-k3-tp4-s65536-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kimi-k3-tp8-s4096-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kimi-k3-tp8-s131072-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kimi-k3-tp1-mixed8k-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kimi-k3-tp8-4x8192-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kimi-k3-tp8-cont256-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kimi-k3-tp8-cont4096-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kimi-k3-tp8-b32-s256-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-tp1-4096-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-tp1-16384-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-tp1-65536-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-tp2-4096-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-tp2-16384-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-tp2-65536-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-tp4-4096-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-tp4-16384-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-tp4-65536-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-tp8-4096-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-tp8-16384-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-tp8-65536-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-tp1-1024-7168-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-tp1-16x8192-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-tp8-1024-7168-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-tp8-16x8192-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-tp1-decode-b8-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-tp1-decode-b32-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-tp1-decode-b128-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-tp1-decode-b256-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-tp8-decode-b32-bfloat16]
benchmarks/ops/bench_kda.py::test_kda_fwd_bench[kda-tp8-decode-b256-bfloat16]

57 tests collected in 5.08s
.........................................................                [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_kda.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
57 passed, 14 warnings in 186.66s (0:03:06)
--- benchmarks/ops/bench_kda.py finished in 196s ---

=== [35/60] benchmarks/ops/bench_logical_reduce.py ===
RUNNING [35/60] 30s: benchmarks/ops/bench_logical_reduce.py::test_any_bench[mask-validation-32k-int64]
RUNNING [35/60] 60s: benchmarks/ops/bench_logical_reduce.py::test_count_nonzero_bench[sparsity-seq-float16]
benchmarks/ops/bench_logical_reduce.py::test_any_bench[mask-validation-4k-bool]
benchmarks/ops/bench_logical_reduce.py::test_any_bench[mask-validation-4k-float16]
benchmarks/ops/bench_logical_reduce.py::test_any_bench[mask-validation-4k-bfloat16]
benchmarks/ops/bench_logical_reduce.py::test_any_bench[mask-validation-4k-float32]
benchmarks/ops/bench_logical_reduce.py::test_any_bench[mask-validation-32k-bool]
benchmarks/ops/bench_logical_reduce.py::test_any_bench[mask-validation-32k-int32]
benchmarks/ops/bench_logical_reduce.py::test_any_bench[mask-validation-32k-int64]
benchmarks/ops/bench_logical_reduce.py::test_any_bench[3d-multidim-bool]
benchmarks/ops/bench_logical_reduce.py::test_any_bench[3d-multidim-complex64]
benchmarks/ops/bench_logical_reduce.py::test_any_bench[3d-multidim-complex128]
benchmarks/ops/bench_logical_reduce.py::test_any_bench[mlp-intermediate-bool]
benchmarks/ops/bench_logical_reduce.py::test_all_bench[mask-validation-4k-bool]
benchmarks/ops/bench_logical_reduce.py::test_all_bench[mask-validation-4k-float16]
benchmarks/ops/bench_logical_reduce.py::test_all_bench[mask-validation-4k-bfloat16]
benchmarks/ops/bench_logical_reduce.py::test_all_bench[mask-validation-4k-float32]
benchmarks/ops/bench_logical_reduce.py::test_all_bench[mask-validation-32k-bool]
benchmarks/ops/bench_logical_reduce.py::test_all_bench[mask-validation-32k-int32]
benchmarks/ops/bench_logical_reduce.py::test_all_bench[mask-validation-32k-int64]
benchmarks/ops/bench_logical_reduce.py::test_all_bench[3d-multidim-bool]
benchmarks/ops/bench_logical_reduce.py::test_all_bench[3d-multidim-complex64]
benchmarks/ops/bench_logical_reduce.py::test_all_bench[3d-multidim-complex128]
benchmarks/ops/bench_logical_reduce.py::test_all_bench[mlp-intermediate-bool]
benchmarks/ops/bench_logical_reduce.py::test_count_nonzero_bench[sparsity-hidden-float16]
benchmarks/ops/bench_logical_reduce.py::test_count_nonzero_bench[sparsity-hidden-bfloat16]
benchmarks/ops/bench_logical_reduce.py::test_count_nonzero_bench[sparsity-hidden-float32]
benchmarks/ops/bench_logical_reduce.py::test_count_nonzero_bench[sparsity-seq-float16]
benchmarks/ops/bench_logical_reduce.py::test_count_nonzero_bench[sparsity-seq-bool]
benchmarks/ops/bench_logical_reduce.py::test_count_nonzero_bench[sparsity-seq-int32]
benchmarks/ops/bench_logical_reduce.py::test_count_nonzero_bench[sparsity-seq-int64]
benchmarks/ops/bench_logical_reduce.py::test_count_nonzero_bench[3d-multidim-float16]
benchmarks/ops/bench_logical_reduce.py::test_count_nonzero_bench[3d-multidim-complex64]
benchmarks/ops/bench_logical_reduce.py::test_count_nonzero_bench[3d-multidim-complex128]
benchmarks/ops/bench_logical_reduce.py::test_count_nonzero_bench[sparsity-mlp-float16]

33 tests collected in 3.22s
.................................                                        [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_logical_reduce.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_logical_reduce.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
33 passed, 58 warnings in 69.20s (0:01:09)
--- benchmarks/ops/bench_logical_reduce.py finished in 77s ---

=== [36/60] benchmarks/ops/bench_mamba.py ===
RUNNING [36/60] 30s: benchmarks/ops/bench_mamba.py::test_ssd_chunk_scan_fwd_bench[mamba2-2p7b-bfloat16]
RUNNING [36/60] 60s: benchmarks/ops/bench_mamba.py::test_ssd_state_passing_fwd_bench[mamba2-2p7b-float16]
RUNNING [36/60] 90s: benchmarks/ops/bench_mamba.py::test_ssd_decode_bench[mamba2-1p3b-float16]
RUNNING [36/60] 120s: benchmarks/ops/bench_mamba.py::test_mamba2_fwd_bench[mamba2-1p3b-float16]
RUNNING [36/60] 150s: benchmarks/ops/bench_mamba.py::test_causal_conv1d_bench[mamba2-2.7b-prefill-32k-bfloat16]
RUNNING [36/60] 180s: benchmarks/ops/bench_mamba.py::test_selective_scan_bench[grouped-state-bfloat16]
benchmarks/ops/bench_mamba.py::test_ssd_chunk_coupling_fwd_bench[mamba2-780m-float16]
benchmarks/ops/bench_mamba.py::test_ssd_chunk_coupling_fwd_bench[mamba2-2p7b-bfloat16]
benchmarks/ops/bench_mamba.py::test_ssd_chunk_coupling_fwd_bench[mamba2-grouped-prefill-float16]
benchmarks/ops/bench_mamba.py::test_ssd_chunk_cumsum_fwd_bench[mamba2-780m-float16]
benchmarks/ops/bench_mamba.py::test_ssd_chunk_cumsum_fwd_bench[mamba2-1p3b-bfloat16]
benchmarks/ops/bench_mamba.py::test_ssd_chunk_cumsum_fwd_bench[mamba2-780m-dt-bias-float16]
benchmarks/ops/bench_mamba.py::test_ssd_chunk_cumsum_fwd_bench[mamba2-1p3b-dt-bias-bfloat16]
benchmarks/ops/bench_mamba.py::test_ssd_chunk_cumsum_fwd_bench[mamba2-2p7b-float16]
benchmarks/ops/bench_mamba.py::test_ssd_chunk_scan_fwd_bench[mamba2-780m-float16]
benchmarks/ops/bench_mamba.py::test_ssd_chunk_scan_fwd_bench[mamba2-780m-bfloat16]
benchmarks/ops/bench_mamba.py::test_ssd_chunk_scan_fwd_bench[mamba2-2p7b-bfloat16]
benchmarks/ops/bench_mamba.py::test_ssd_chunk_scan_fwd_bench[mamba2-1p3b-float16]
benchmarks/ops/bench_mamba.py::test_ssd_chunk_state_fwd_bench[mamba2-780m-float16-float32]
benchmarks/ops/bench_mamba.py::test_ssd_chunk_state_fwd_bench[mamba2-780m-bfloat16-float32]
benchmarks/ops/bench_mamba.py::test_ssd_chunk_state_fwd_bench[mamba2-2p7b-bfloat16-float32]
benchmarks/ops/bench_mamba.py::test_ssd_chunk_state_fwd_bench[mamba2-780m-seq-idx-float16-float32]
benchmarks/ops/bench_mamba.py::test_ssd_chunk_state_fwd_bench[mamba2-780m-seq-idx-bfloat16-float32]
benchmarks/ops/bench_mamba.py::test_ssd_chunk_state_fwd_bench[mamba2-1p3b-float16-float32]
benchmarks/ops/bench_mamba.py::test_ssd_state_passing_fwd_bench[mamba2-1p3b-float16]
benchmarks/ops/bench_mamba.py::test_ssd_state_passing_fwd_bench[mamba2-1p3b-bfloat16]
benchmarks/ops/bench_mamba.py::test_ssd_state_passing_fwd_bench[mamba2-2p7b-float16]
benchmarks/ops/bench_mamba.py::test_ssd_state_passing_fwd_bench[mamba2-1p3b-init-float16]
benchmarks/ops/bench_mamba.py::test_ssd_state_passing_fwd_bench[mamba2-1p3b-init-bfloat16]
benchmarks/ops/bench_mamba.py::test_ssd_state_passing_fwd_bench[mamba2-1p3b-flat-float32]
benchmarks/ops/bench_mamba.py::test_ssd_decode_bench[mamba2-1p3b-float16]
benchmarks/ops/bench_mamba.py::test_ssd_decode_bench[mamba2-1p3b-bfloat16]
benchmarks/ops/bench_mamba.py::test_ssd_decode_bench[mamba2-2p7b-float16]
benchmarks/ops/bench_mamba.py::test_ssd_decode_bench[mamba2-780m-float16]
benchmarks/ops/bench_mamba.py::test_mamba2_fwd_bench[mamba2-2p7b-bfloat16]
benchmarks/ops/bench_mamba.py::test_mamba2_fwd_bench[mamba2-1p3b-float16]
benchmarks/ops/bench_mamba.py::test_mamba2_fwd_bench[mamba2-2p7b-dt-bias-bfloat16]
benchmarks/ops/bench_mamba.py::test_mamba2_fwd_bench[mamba2-1p3b-dt-bias-float16]
benchmarks/ops/bench_mamba.py::test_mamba2_fwd_bench[mamba2-2p7b-init-bfloat16]
benchmarks/ops/bench_mamba.py::test_mamba2_fwd_bench[mamba2-1p3b-init-float16]
benchmarks/ops/bench_mamba.py::test_mamba2_fwd_bench[mamba2-2p7b-dt-bias-init-bfloat16]
benchmarks/ops/bench_mamba.py::test_mamba2_fwd_bench[mamba2-1p3b-dt-bias-init-float16]
benchmarks/ops/bench_mamba.py::test_causal_conv1d_bench[mamba2-2.7b-prefill-4k-bfloat16]
benchmarks/ops/bench_mamba.py::test_causal_conv1d_bench[mamba2-2.7b-pf4k-nost-bfloat16]
benchmarks/ops/bench_mamba.py::test_causal_conv1d_bench[mamba2-2.7b-prefill-32k-bfloat16]
benchmarks/ops/bench_mamba.py::test_causal_conv1d_bench[qwen3-next-pf4k-ragged-float16]
benchmarks/ops/bench_mamba.py::test_causal_conv1d_bench[qwen3-next-prefill-32k-float16]
benchmarks/ops/bench_mamba.py::test_causal_conv1d_update_bench[mamba2-2.7b-decode-b1-bfloat16]
benchmarks/ops/bench_mamba.py::test_causal_conv1d_update_bench[mamba2-2.7b-decode-b64-bfloat16]
benchmarks/ops/bench_mamba.py::test_causal_conv1d_update_bench[mamba2-2.7b-decode-b256-bfloat16]
benchmarks/ops/bench_mamba.py::test_causal_conv1d_update_bench[qwen3-next-decode-b64-float16]
benchmarks/ops/bench_mamba.py::test_selective_scan_bench[mamba-2.8b-prefill-bfloat16]
benchmarks/ops/bench_mamba.py::test_selective_scan_bench[mamba-2.8b-prefill-float16]
benchmarks/ops/bench_mamba.py::test_selective_scan_bench[mamba-2.8b-decode-bfloat16]
benchmarks/ops/bench_mamba.py::test_selective_scan_bench[mamba-2.8b-decode-b64-bfloat16]
benchmarks/ops/bench_mamba.py::test_selective_scan_bench[mamba-1.4b-prefill-bfloat16]
benchmarks/ops/bench_mamba.py::test_selective_scan_bench[mamba-130m-no-gate-float32]
benchmarks/ops/bench_mamba.py::test_selective_scan_bench[mamba-2.8b-packed-bfloat16]
benchmarks/ops/bench_mamba.py::test_selective_scan_bench[grouped-state-bfloat16]
benchmarks/ops/bench_mamba.py::test_selective_scan_bench[bare-scan-bfloat16]

54 tests collected in 8.98s
......................................................                   [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_mamba.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
54 passed, 14 warnings in 171.85s (0:02:51)
--- benchmarks/ops/bench_mamba.py finished in 186s ---

=== [37/60] benchmarks/ops/bench_merge_attention_states.py ===
RUNNING [37/60] 30s: benchmarks/ops/bench_merge_attention_states.py::test_merge_attention_states_bench[ds-v3-chunked-prefill-float16]
benchmarks/ops/bench_merge_attention_states.py::test_merge_attention_states_bench[ds-v3-chunked-prefill-bfloat16]
benchmarks/ops/bench_merge_attention_states.py::test_merge_attention_states_bench[ds-v3-chunked-prefill-float16]
benchmarks/ops/bench_merge_attention_states.py::test_merge_attention_states_bench[llama-70b-cascade-bfloat16]
benchmarks/ops/bench_merge_attention_states.py::test_merge_attention_states_bench[qwen3-235b-dcp-bfloat16]
benchmarks/ops/bench_merge_attention_states.py::test_merge_attention_states_bench[qwen3-235b-dcp-ragged-float16]
benchmarks/ops/bench_merge_attention_states.py::test_merge_attention_states_bench[ds-v3-chunked-log2-bfloat16]
benchmarks/ops/bench_merge_attention_states.py::test_merge_attention_states_bench[ds-v3-chunked-log2-float16]
benchmarks/ops/bench_merge_attention_states.py::test_merge_attention_states_bench[llama-70b-cascade-log2-bfloat16]
benchmarks/ops/bench_merge_attention_states.py::test_merge_attention_states_bench[qwen3-235b-dcp-log2-bfloat16]
benchmarks/ops/bench_merge_attention_states.py::test_merge_attention_states_bench[qwen3-dcp-ragged-log2-float16]

10 tests collected in 8.05s
..........                                                               [100%]Benchmark report saved to profile_run.log

10 passed in 28.36s
--- benchmarks/ops/bench_merge_attention_states.py finished in 41s ---

=== [38/60] benchmarks/ops/bench_mha.py ===
RUNNING [38/60] 30s: benchmarks/ops/bench_mha.py::test_mha_decode_paged_bench[speculative-decode-float16]
benchmarks/ops/bench_mha.py::test_mha_decode_paged_bench[serving-p128-float16]
benchmarks/ops/bench_mha.py::test_mha_decode_paged_bench[serving-b2-float16]
benchmarks/ops/bench_mha.py::test_mha_decode_paged_bench[serving-kv1k-float16]
benchmarks/ops/bench_mha.py::test_mha_decode_paged_bench[serving-kv512-float16]
benchmarks/ops/bench_mha.py::test_mha_decode_paged_bench[speculative-decode-float16]
benchmarks/ops/bench_mha.py::test_mha_decode_paged_bench[opt-1.3b-b1-float16]
benchmarks/ops/bench_mha.py::test_mha_decode_paged_bench[opt-1.3b-b16-float16]

7 tests collected in 7.77s
.......                                                                  [100%]Benchmark report saved to profile_run.log

7 passed in 21.89s
--- benchmarks/ops/bench_mha.py finished in 34s ---

=== [39/60] benchmarks/ops/bench_mhc.py ===
benchmarks/ops/bench_mhc.py::test_mhc_pre_bench[hidden-1280]
benchmarks/ops/bench_mhc.py::test_mhc_pre_bench[hidden-1920]
benchmarks/ops/bench_mhc.py::test_mhc_pre_bench[hidden-2560]
benchmarks/ops/bench_mhc.py::test_mhc_post_bench[hidden-1280]
benchmarks/ops/bench_mhc.py::test_mhc_post_bench[hidden-1920]
benchmarks/ops/bench_mhc.py::test_mhc_post_bench[hidden-2560]

6 tests collected in 2.98s
......                                                                   [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_mhc.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
6 passed, 14 warnings in 11.74s
--- benchmarks/ops/bench_mhc.py finished in 19s ---

=== [40/60] benchmarks/ops/bench_min_p_mask.py ===
benchmarks/ops/bench_min_p_mask.py::test_min_p_mask_bench[llama-8b-b1-bfloat16]
benchmarks/ops/bench_min_p_mask.py::test_min_p_mask_bench[llama-8b-b1-float32]
benchmarks/ops/bench_min_p_mask.py::test_min_p_mask_bench[llama-8b-b64-bfloat16]
benchmarks/ops/bench_min_p_mask.py::test_min_p_mask_bench[llama-8b-b256-float16]
benchmarks/ops/bench_min_p_mask.py::test_min_p_mask_bench[llama-8b-b256-bfloat16]
benchmarks/ops/bench_min_p_mask.py::test_min_p_mask_bench[qwen3-235b-b128-bfloat16]
benchmarks/ops/bench_min_p_mask.py::test_min_p_mask_bench[deepseek-v3-b17-bfloat16]
benchmarks/ops/bench_min_p_mask.py::test_min_p_mask_bench[llama2-7b-b100-float16]

8 tests collected in 2.99s
........                                                                 [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_min_p_mask.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
8 passed, 14 warnings in 12.98s
--- benchmarks/ops/bench_min_p_mask.py finished in 20s ---

=== [41/60] benchmarks/ops/bench_mla.py ===
RUNNING [41/60] 30s: benchmarks/ops/bench_mla.py::test_mla_decode_bench[ds-v2-4k-bfloat16]
RUNNING [41/60] 60s: benchmarks/ops/bench_mla.py::test_mla_decode_bench[ds-v3-serving-batch-bfloat16]
RUNNING [41/60] 90s: benchmarks/ops/bench_mla.py::test_mla_decode_bench[mla-tp-b1-bfloat16]
RUNNING [41/60] 120s: benchmarks/ops/bench_mla.py::test_mla_paged_bench[kimi-k2-fp8-bfloat16-float8_e4m3fn]
RUNNING [41/60] 150s: benchmarks/ops/bench_mla.py::test_mla_varlen_fwd_bench[ds-v3-8x4k-bfloat16]
RUNNING [41/60] 180s: benchmarks/ops/bench_mla.py::test_mla_varlen_fwd_bench[ds-v3-8x4k-bfloat16]
RUNNING [41/60] 210s: benchmarks/ops/bench_mla.py::test_mla_varlen_fwd_bench[ds-v3-8x4k-bfloat16]
RUNNING [41/60] 240s: benchmarks/ops/bench_mla.py::test_mla_varlen_fwd_bench[ds-v3-8x4k-float16]
RUNNING [41/60] 270s: benchmarks/ops/bench_mla.py::test_mla_varlen_fwd_bench[ds-v3-8x4k-float16]
RUNNING [41/60] 300s: benchmarks/ops/bench_mla.py::test_mla_varlen_fwd_bench[ds-v3-8x4k-float16]
RUNNING [41/60] 330s: benchmarks/ops/bench_mla.py::test_mla_varlen_fwd_bench[ds-v3-mixed-bfloat16]
RUNNING [41/60] 360s: benchmarks/ops/bench_mla.py::test_mla_varlen_fwd_bench[kimi-k2-4x8k-bfloat16]
RUNNING [41/60] 391s: benchmarks/ops/bench_mla.py::test_mla_dense_bwd_bench[ds-v3-b2-8k-bfloat16]
RUNNING [41/60] 421s: benchmarks/ops/bench_mla.py::test_mla_varlen_bwd_bench[ds-v3-mixed-bfloat16]
benchmarks/ops/bench_mla.py::test_mla_decode_bench[ds-v2-4k-float16]
benchmarks/ops/bench_mla.py::test_mla_decode_bench[ds-v2-4k-bfloat16]
benchmarks/ops/bench_mla.py::test_mla_decode_bench[ds-v2-32k-float16]
benchmarks/ops/bench_mla.py::test_mla_decode_bench[ds-v2-32k-bfloat16]
benchmarks/ops/bench_mla.py::test_mla_decode_bench[ds-v3-4k-bfloat16]
benchmarks/ops/bench_mla.py::test_mla_decode_bench[ds-v3-32k-bfloat16]
benchmarks/ops/bench_mla.py::test_mla_decode_bench[ds-v3-single-request-float16]
benchmarks/ops/bench_mla.py::test_mla_decode_bench[ds-v3-single-request-bfloat16]
benchmarks/ops/bench_mla.py::test_mla_decode_bench[ds-v3-serving-batch-float16]
benchmarks/ops/bench_mla.py::test_mla_decode_bench[ds-v3-serving-batch-bfloat16]
benchmarks/ops/bench_mla.py::test_mla_decode_bench[mla-b128-4096-float16]
benchmarks/ops/bench_mla.py::test_mla_decode_bench[mla-b128-4096-bfloat16]
benchmarks/ops/bench_mla.py::test_mla_decode_bench[mla-b128-8192-float16]
benchmarks/ops/bench_mla.py::test_mla_decode_bench[mla-b128-8192-bfloat16]
benchmarks/ops/bench_mla.py::test_mla_decode_bench[mla-b128-16384-float16]
benchmarks/ops/bench_mla.py::test_mla_decode_bench[mla-b128-16384-bfloat16]
benchmarks/ops/bench_mla.py::test_mla_decode_bench[mla-b128-32768-float16]
benchmarks/ops/bench_mla.py::test_mla_decode_bench[mla-b128-32768-bfloat16]
benchmarks/ops/bench_mla.py::test_mla_decode_bench[mla-tp-b1-float16]
benchmarks/ops/bench_mla.py::test_mla_decode_bench[mla-tp-b1-bfloat16]
benchmarks/ops/bench_mla.py::test_mla_decode_bench[mla-tp-b2-float16]
benchmarks/ops/bench_mla.py::test_mla_decode_bench[mla-tp-b2-bfloat16]
benchmarks/ops/bench_mla.py::test_mla_decode_bench[mla-tp-b6-float16]
benchmarks/ops/bench_mla.py::test_mla_decode_bench[mla-tp-b6-bfloat16]
benchmarks/ops/bench_mla.py::test_mla_decode_bench[mla-tp-b64-float16]
benchmarks/ops/bench_mla.py::test_mla_decode_bench[mla-tp-b64-bfloat16]
benchmarks/ops/bench_mla.py::test_mla_paged_bench[ds-v3-4k-bfloat16-bfloat16]
benchmarks/ops/bench_mla.py::test_mla_paged_bench[ds-v3-4k-float16-float16]
benchmarks/ops/bench_mla.py::test_mla_paged_bench[ds-v3-32k-bfloat16-bfloat16]
benchmarks/ops/bench_mla.py::test_mla_paged_bench[ds-v3-mtp-bfloat16-bfloat16]
benchmarks/ops/bench_mla.py::test_mla_paged_bench[kimi-k2-fp8-bfloat16-float8_e4m3fn]
benchmarks/ops/bench_mla.py::test_mla_paged_bench[ds-v3-ragged-bfloat16-bfloat16]
benchmarks/ops/bench_mla.py::test_mla_varlen_fwd_bench[ds-v3-8x4k-bfloat16]
benchmarks/ops/bench_mla.py::test_mla_varlen_fwd_bench[ds-v3-8x4k-float16]
benchmarks/ops/bench_mla.py::test_mla_varlen_fwd_bench[ds-v3-mixed-bfloat16]
benchmarks/ops/bench_mla.py::test_mla_varlen_fwd_bench[kimi-k2-4x8k-bfloat16]
benchmarks/ops/bench_mla.py::test_mla_dense_bwd_bench[ds-v3-4k-bfloat16]
benchmarks/ops/bench_mla.py::test_mla_dense_bwd_bench[ds-v3-4k-float16]
benchmarks/ops/bench_mla.py::test_mla_dense_bwd_bench[ds-v3-b2-8k-bfloat16]
benchmarks/ops/bench_mla.py::test_mla_dense_bwd_bench[kimi-k2-8k-bfloat16]
benchmarks/ops/bench_mla.py::test_mla_dense_bwd_bench[ds-v2-lite-3k-bfloat16]
benchmarks/ops/bench_mla.py::test_mla_varlen_bwd_bench[ds-v3-8x4k-bfloat16]
benchmarks/ops/bench_mla.py::test_mla_varlen_bwd_bench[ds-v3-8x4k-float16]
benchmarks/ops/bench_mla.py::test_mla_varlen_bwd_bench[ds-v3-mixed-bfloat16]
benchmarks/ops/bench_mla.py::test_mla_varlen_bwd_bench[kimi-k2-4x8k-bfloat16]

45 tests collected in 4.13s
.............................................                            [100%]Benchmark report saved to profile_run.log

45 passed in 430.46s (0:07:10)
--- benchmarks/ops/bench_mla.py finished in 437s ---

=== [42/60] benchmarks/ops/bench_mla_cache_write.py ===
RUNNING [42/60] 30s: benchmarks/ops/bench_mla_cache_write.py::test_mla_kv_cache_write_bench[ds-v3-prefill-float16-float16]
benchmarks/ops/bench_mla_cache_write.py::test_mla_kv_cache_write_bench[ds-v3-decode-bfloat16-bfloat16]
benchmarks/ops/bench_mla_cache_write.py::test_mla_kv_cache_write_bench[ds-v3-prefill-bfloat16-bfloat16]
benchmarks/ops/bench_mla_cache_write.py::test_mla_kv_cache_write_bench[ds-v3-prefill-float16-float16]
benchmarks/ops/bench_mla_cache_write.py::test_mla_kv_cache_write_bench[ds-v3-fp8-rope-bfloat16-float8_e4m3fn-float32]
benchmarks/ops/bench_mla_cache_write.py::test_mla_kv_cache_write_bench[kimi-k2-rope-bfloat16-bfloat16-bfloat16]
benchmarks/ops/bench_mla_cache_write.py::test_mla_kv_cache_write_bench[odd-tokens-neox-fp8-float16-float8_e4m3fn-float16]

6 tests collected in 4.01s
......                                                                   [100%]Benchmark report saved to profile_run.log

6 passed in 27.26s
--- benchmarks/ops/bench_mla_cache_write.py finished in 34s ---

=== [43/60] benchmarks/ops/bench_moe_grouped_gemm_fp8.py ===
RUNNING [43/60] 30s: benchmarks/ops/bench_moe_grouped_gemm_fp8.py::test_moe_grouped_gemm_fp8_bench[ds-v3-dec-b64-down]
RUNNING [43/60] 60s: benchmarks/ops/bench_moe_grouped_gemm_fp8.py::test_moe_grouped_gemm_fp8_bench[kimi-k2-dec-b64-up]
benchmarks/ops/bench_moe_grouped_gemm_fp8.py::test_moe_grouped_gemm_fp8_bench[ds-v3-e8-up-masked]
benchmarks/ops/bench_moe_grouped_gemm_fp8.py::test_moe_grouped_gemm_fp8_bench[ds-v3-e8-down-masked]
benchmarks/ops/bench_moe_grouped_gemm_fp8.py::test_moe_grouped_gemm_fp8_bench[ds-v3-dec-b64-up]
benchmarks/ops/bench_moe_grouped_gemm_fp8.py::test_moe_grouped_gemm_fp8_bench[ds-v3-dec-b64-down]
benchmarks/ops/bench_moe_grouped_gemm_fp8.py::test_moe_grouped_gemm_fp8_bench[ds-v3-dec-b256-up]
benchmarks/ops/bench_moe_grouped_gemm_fp8.py::test_moe_grouped_gemm_fp8_bench[ds-v3-dec-b256-down]
benchmarks/ops/bench_moe_grouped_gemm_fp8.py::test_moe_grouped_gemm_fp8_bench[qwen3-235b-dec-b64-up]
benchmarks/ops/bench_moe_grouped_gemm_fp8.py::test_moe_grouped_gemm_fp8_bench[qwen3-235b-dec-b64-down]
benchmarks/ops/bench_moe_grouped_gemm_fp8.py::test_moe_grouped_gemm_fp8_bench[qwen3-235b-dec-b256-up]
benchmarks/ops/bench_moe_grouped_gemm_fp8.py::test_moe_grouped_gemm_fp8_bench[qwen3-235b-dec-b256-down]
benchmarks/ops/bench_moe_grouped_gemm_fp8.py::test_moe_grouped_gemm_fp8_bench[kimi-k2-dec-b64-up]
benchmarks/ops/bench_moe_grouped_gemm_fp8.py::test_moe_grouped_gemm_fp8_bench[kimi-k2-dec-b64-down]
benchmarks/ops/bench_moe_grouped_gemm_fp8.py::test_moe_grouped_gemm_fp8_bench[kimi-k2-dec-b256-up]
benchmarks/ops/bench_moe_grouped_gemm_fp8.py::test_moe_grouped_gemm_fp8_bench[kimi-k2-dec-b256-down]

14 tests collected in 3.58s
..............                                                           [100%]Benchmark report saved to profile_run.log

14 passed in 66.55s (0:01:06)
--- benchmarks/ops/bench_moe_grouped_gemm_fp8.py finished in 74s ---

=== [44/60] benchmarks/ops/bench_moe_permute_align.py ===
benchmarks/ops/bench_moe_permute_align.py::test_permute_align_bench[kimi-k2-t1]
benchmarks/ops/bench_moe_permute_align.py::test_permute_align_bench[kimi-k2-t32]
benchmarks/ops/bench_moe_permute_align.py::test_permute_align_bench[kimi-k2-t512]
benchmarks/ops/bench_moe_permute_align.py::test_permute_align_bench[kimi-k2-t4096]
benchmarks/ops/bench_moe_permute_align.py::test_permute_align_bench[ds-v3-t1]
benchmarks/ops/bench_moe_permute_align.py::test_permute_align_bench[ds-v3-t32]
benchmarks/ops/bench_moe_permute_align.py::test_permute_align_bench[ds-v3-t512]
benchmarks/ops/bench_moe_permute_align.py::test_permute_align_bench[ds-v3-t4096]
benchmarks/ops/bench_moe_permute_align.py::test_permute_align_bench[qwen3-235b-t1]
benchmarks/ops/bench_moe_permute_align.py::test_permute_align_bench[qwen3-235b-t32]
benchmarks/ops/bench_moe_permute_align.py::test_permute_align_bench[qwen3-235b-t512]
benchmarks/ops/bench_moe_permute_align.py::test_permute_align_bench[qwen3-235b-t4096]

12 tests collected in 1.93s
............                                                             [100%]Benchmark report saved to profile_run.log

12 passed in 10.66s
--- benchmarks/ops/bench_moe_permute_align.py finished in 16s ---

=== [45/60] benchmarks/ops/bench_moe_staged.py ===
RUNNING [45/60] 30s: benchmarks/ops/bench_moe_staged.py::test_moe_grouped_gemm_bench[qwen3-30b-ep8-routed256-bfloat16]
RUNNING [45/60] 60s: benchmarks/ops/bench_moe_staged.py::test_moe_expert_mlp_bench[qwen3-235b-decode-float16]
RUNNING [45/60] 90s: benchmarks/ops/bench_moe_staged.py::test_moe_expert_mlp_bench[qwen3-235b-decode-float16]
RUNNING [45/60] 120s: benchmarks/ops/bench_moe_staged.py::test_moe_expert_mlp_bench[ds-v3-prefill-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_pre_permute_bench[decode-t32-float16]
benchmarks/ops/bench_moe_staged.py::test_moe_pre_permute_bench[decode-t32-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_pre_permute_bench[prefill-t512-float16]
benchmarks/ops/bench_moe_staged.py::test_moe_pre_permute_bench[prefill-t512-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_pre_permute_bench[ds-v3-ep8-t100-float16]
benchmarks/ops/bench_moe_staged.py::test_moe_pre_permute_bench[ds-v3-ep8-t100-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_pre_permute_bench[qwen3-30b-ep8-b1-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_post_permute_bench[decode-t32-float16]
benchmarks/ops/bench_moe_staged.py::test_moe_post_permute_bench[decode-t32-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_post_permute_bench[decode-t32-float16-float16]
benchmarks/ops/bench_moe_staged.py::test_moe_post_permute_bench[decode-t32-bfloat16-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_post_permute_bench[prefill-t512-float16]
benchmarks/ops/bench_moe_staged.py::test_moe_post_permute_bench[prefill-t512-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_post_permute_bench[ds-v3-ep8-t100-float16]
benchmarks/ops/bench_moe_staged.py::test_moe_post_permute_bench[ds-v3-ep8-t100-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_post_permute_bench[qwen3-30b-ep8-b1-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_grouped_gemm_bench[ds-v3-decode-mlp-up-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_grouped_gemm_bench[ds-v3-decode-mlp-up-float16]
benchmarks/ops/bench_moe_staged.py::test_moe_grouped_gemm_bench[ds-v3-prefill-mlp-up-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_grouped_gemm_bench[ds-v3-decode-down-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_grouped_gemm_bench[ds-v3-decode-down-bfloat16-float32]
benchmarks/ops/bench_moe_staged.py::test_moe_grouped_gemm_bench[ds-v3-prefill-down-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_grouped_gemm_bench[ds-v3-decode-swiglu-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_grouped_gemm_bench[ds-v3-prefill-swiglu-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_grouped_gemm_bench[ds-v3-ep8-masked-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_grouped_gemm_bench[qwen3-30b-ep8-decode-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_grouped_gemm_bench[qwen3-30b-ep8-routed256-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_grouped_gemm_bench[gpt-oss-120b-t64-up-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_grouped_gemm_bench[gpt-oss-120b-t64-down-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_grouped_gemm_bench[gpt-oss-120b-t4096-up-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_grouped_gemm_bench[gpt-oss-120b-t4096-down-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_grouped_gemm_bench[gpt-oss-20b-t1024-up-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_grouped_gemm_bench[gpt-oss-20b-t1024-down-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_expert_mlp_bench[qwen3-235b-decode-float16]
benchmarks/ops/bench_moe_staged.py::test_moe_expert_mlp_bench[qwen3-235b-decode-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_expert_mlp_bench[qwen3-235b-prefill-float16]
benchmarks/ops/bench_moe_staged.py::test_moe_expert_mlp_bench[qwen3-235b-prefill-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_expert_mlp_bench[ds-v3-decode-float16]
benchmarks/ops/bench_moe_staged.py::test_moe_expert_mlp_bench[ds-v3-decode-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_expert_mlp_bench[ds-v3-prefill-float16]
benchmarks/ops/bench_moe_staged.py::test_moe_expert_mlp_bench[ds-v3-prefill-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_expert_mlp_bench[gpt-oss-120b-decode-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_expert_mlp_bench[gpt-oss-120b-prefill-bfloat16]
benchmarks/ops/bench_moe_staged.py::test_moe_expert_mlp_bench[gpt-oss-20b-prefill-bfloat16]

44 tests collected in 1.89s
............................................                             [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_moe_staged.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
44 passed, 14 warnings in 121.97s (0:02:01)
--- benchmarks/ops/bench_moe_staged.py finished in 128s ---

=== [46/60] benchmarks/ops/bench_norm.py ===
RUNNING [46/60] 30s: benchmarks/ops/bench_norm.py::test_rms_norm_bench[llama-405b-prefill-bfloat16]
RUNNING [46/60] 60s: benchmarks/ops/bench_norm.py::test_rms_norm_bench[quack-throughput-16384-bfloat16]
RUNNING [46/60] 90s: benchmarks/ops/bench_norm.py::test_rms_norm_bench[quack-throughput-131072-float16]
RUNNING [46/60] 120s: benchmarks/ops/bench_norm.py::test_rms_norm_bench[quack-throughput-262144-bfloat16]
RUNNING [46/60] 150s: benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_per_token_quant_bench[llama-70b-decode-b1-bfloat16-float8_e4m3fn]
RUNNING [46/60] 180s: benchmarks/ops/bench_norm.py::test_fused_add_layer_norm_bench[llama-8b-prefill-float16]
RUNNING [46/60] 210s: benchmarks/ops/bench_norm.py::test_fused_add_layer_norm_bench[llama-8b-decode-bfloat16]
RUNNING [46/60] 240s: benchmarks/ops/bench_norm.py::test_fused_add_layer_norm_bench[llama-70b-prefill-bfloat16]
RUNNING [46/60] 270s: benchmarks/ops/bench_norm.py::test_ada_layer_norm_bench[dit-xl-2-float32]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[llama-8b-prefill-float16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[llama-8b-prefill-bfloat16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[llama-8b-decode-bfloat16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[llama-70b-prefill-float16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[llama-70b-prefill-bfloat16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[llama-70b-decode-bfloat16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[llama-405b-prefill-float16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[llama-405b-prefill-bfloat16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[llama-405b-decode-bfloat16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[llama-13b-prefill-bfloat16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[qk-norm-head-bfloat16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[quack-throughput-256-float16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[quack-throughput-256-bfloat16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[quack-throughput-512-float16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[quack-throughput-512-bfloat16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[quack-throughput-1024-float16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[quack-throughput-1024-bfloat16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[quack-throughput-2048-float16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[quack-throughput-2048-bfloat16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[quack-throughput-4096-float16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[quack-throughput-4096-bfloat16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[quack-throughput-8192-float16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[quack-throughput-8192-bfloat16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[quack-throughput-16384-float16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[quack-throughput-16384-bfloat16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[quack-throughput-32768-float16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[quack-throughput-32768-bfloat16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[quack-throughput-65536-float16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[quack-throughput-65536-bfloat16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[quack-throughput-131072-float16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[quack-throughput-131072-bfloat16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[quack-throughput-262144-float16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[quack-throughput-262144-bfloat16]
benchmarks/ops/bench_norm.py::test_rms_norm_bench[qwen3-8b-qk-norm-decode-bfloat16]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_bench[llama-8b-prefill-float16]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_bench[llama-8b-prefill-bfloat16]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_bench[llama-8b-decode-bfloat16]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_bench[llama-70b-prefill-float16]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_bench[llama-70b-prefill-bfloat16]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_bench[llama-70b-decode-bfloat16]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_bench[llama-405b-prefill-float16]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_bench[llama-405b-prefill-bfloat16]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_bench[llama-405b-decode-bfloat16]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_bench[llama-13b-prefill-bfloat16]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_per_token_quant_bench[llama-8b-prefill-bfloat16-float8_e4m3fn]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_per_token_quant_bench[llama-8b-prefill-i8-bfloat16-int8]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_per_token_quant_bench[llama-8b-decode-b1-bfloat16-float8_e4m3fn]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_per_token_quant_bench[llama-8b-decode-b64-bfloat16-float8_e4m3fn]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_per_token_quant_bench[llama-8b-decode-b256-bfloat16-float8_e4m3fn]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_per_token_quant_bench[llama-70b-prefill-bfloat16-float8_e4m3fn]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_per_token_quant_bench[llama-70b-prefill-i8-float16-int8]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_per_token_quant_bench[llama-70b-decode-b1-bfloat16-float8_e4m3fn]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_per_token_quant_bench[llama-70b-decode-b64-bfloat16-float8_e4m3fn]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_per_token_quant_bench[llama-70b-decode-b256-bfloat16-float8_e4m3fn]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_per_token_quant_bench[clamped-amax-bfloat16-float8_e4m3fn]
benchmarks/ops/bench_norm.py::test_fused_add_rms_norm_per_token_quant_bench[llama-13b-prefill-bfloat16-float8_e4m3fn]
benchmarks/ops/bench_norm.py::test_layer_norm_bench[llama-8b-prefill-float16]
benchmarks/ops/bench_norm.py::test_layer_norm_bench[llama-8b-prefill-bfloat16]
benchmarks/ops/bench_norm.py::test_layer_norm_bench[llama-8b-decode-bfloat16]
benchmarks/ops/bench_norm.py::test_layer_norm_bench[llama-70b-prefill-float16]
benchmarks/ops/bench_norm.py::test_layer_norm_bench[llama-70b-prefill-bfloat16]
benchmarks/ops/bench_norm.py::test_layer_norm_bench[llama-70b-decode-bfloat16]
benchmarks/ops/bench_norm.py::test_layer_norm_bench[llama-405b-prefill-float16]
benchmarks/ops/bench_norm.py::test_layer_norm_bench[llama-405b-prefill-bfloat16]
benchmarks/ops/bench_norm.py::test_layer_norm_bench[llama-405b-decode-bfloat16]
benchmarks/ops/bench_norm.py::test_layer_norm_bench[llama-13b-prefill-float32]
benchmarks/ops/bench_norm.py::test_layer_norm_bench[dit-xl-2-bfloat16]
benchmarks/ops/bench_norm.py::test_fused_add_layer_norm_bench[llama-8b-prefill-float16]
benchmarks/ops/bench_norm.py::test_fused_add_layer_norm_bench[llama-8b-prefill-bfloat16]
benchmarks/ops/bench_norm.py::test_fused_add_layer_norm_bench[llama-8b-decode-bfloat16]
benchmarks/ops/bench_norm.py::test_fused_add_layer_norm_bench[llama-70b-prefill-float16]
benchmarks/ops/bench_norm.py::test_fused_add_layer_norm_bench[llama-70b-prefill-bfloat16]
benchmarks/ops/bench_norm.py::test_fused_add_layer_norm_bench[llama-70b-decode-bfloat16]
benchmarks/ops/bench_norm.py::test_fused_add_layer_norm_bench[llama-13b-prefill-float32]
benchmarks/ops/bench_norm.py::test_ada_layer_norm_bench[dit-xl-2-float16]
benchmarks/ops/bench_norm.py::test_ada_layer_norm_bench[dit-xl-2-bfloat16]
benchmarks/ops/bench_norm.py::test_ada_layer_norm_bench[dit-xl-2-float32]
benchmarks/ops/bench_norm.py::test_ada_layer_norm_bench[llama-8b-prefill-float16]
benchmarks/ops/bench_norm.py::test_ada_layer_norm_bench[llama-8b-prefill-bfloat16]
benchmarks/ops/bench_norm.py::test_ada_layer_norm_bench[llama-8b-decode-bfloat16]
benchmarks/ops/bench_norm.py::test_ada_layer_norm_zero_bench[dit-xl-2-float16]
benchmarks/ops/bench_norm.py::test_ada_layer_norm_zero_bench[dit-xl-2-bfloat16]
benchmarks/ops/bench_norm.py::test_ada_layer_norm_zero_bench[dit-xl-2-float32]
benchmarks/ops/bench_norm.py::test_ada_layer_norm_zero_bench[llama-8b-prefill-float16]
benchmarks/ops/bench_norm.py::test_ada_layer_norm_zero_bench[llama-8b-prefill-bfloat16]
benchmarks/ops/bench_norm.py::test_ada_layer_norm_zero_bench[llama-8b-decode-bfloat16]

86 tests collected in 3.51s
........................................................................ [ 83%]
..............                                                           [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_norm.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_norm.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
86 passed, 58 warnings in 282.50s (0:04:42)
--- benchmarks/ops/bench_norm.py finished in 290s ---

=== [47/60] benchmarks/ops/bench_nsa.py ===
RUNNING [47/60] 30s: benchmarks/ops/bench_nsa.py::test_nsa_compressed_fwd_varlen_bench[prefill-4x1k-float16]
RUNNING [47/60] 60s: benchmarks/ops/bench_nsa.py::test_nsa_fwd_varlen_bench[prefill-2x4k-float16]
benchmarks/ops/bench_nsa.py::test_nsa_compressed_fwd_varlen_bench[prefill-8x1k-float16]
benchmarks/ops/bench_nsa.py::test_nsa_compressed_fwd_varlen_bench[prefill-4x1k-float16]
benchmarks/ops/bench_nsa.py::test_nsa_compressed_fwd_varlen_bench[prefill-ragged-bfloat16]
benchmarks/ops/bench_nsa.py::test_nsa_topk_varlen_bench[prefill-8x1k-float16]
benchmarks/ops/bench_nsa.py::test_nsa_topk_varlen_bench[prefill-8x1k-bfloat16]
benchmarks/ops/bench_nsa.py::test_nsa_topk_varlen_bench[prefill-4x1k-float16]
benchmarks/ops/bench_nsa.py::test_nsa_topk_varlen_bench[prefill-4x1k-bfloat16]
benchmarks/ops/bench_nsa.py::test_nsa_topk_varlen_bench[prefill-ragged-float16]
benchmarks/ops/bench_nsa.py::test_nsa_topk_varlen_bench[prefill-ragged-bfloat16]
benchmarks/ops/bench_nsa.py::test_nsa_topk_varlen_bench[prefill-long-context-float16]
benchmarks/ops/bench_nsa.py::test_nsa_topk_varlen_bench[prefill-long-context-bfloat16]
benchmarks/ops/bench_nsa.py::test_nsa_topk_varlen_bench[prefill-wide-gqa-float16]
benchmarks/ops/bench_nsa.py::test_nsa_topk_varlen_bench[prefill-wide-gqa-bfloat16]
benchmarks/ops/bench_nsa.py::test_nsa_fwd_varlen_bench[prefill-4x2k-float16]
benchmarks/ops/bench_nsa.py::test_nsa_fwd_varlen_bench[prefill-2x4k-float16]
benchmarks/ops/bench_nsa.py::test_nsa_fwd_varlen_bench[prefill-noncausal-2x4k-float16]
benchmarks/ops/bench_nsa.py::test_nsa_fwd_varlen_bench[prefill-ragged-bfloat16]

17 tests collected in 4.34s
.................                                                        [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_nsa.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
17 passed, 14 warnings in 55.82s
--- benchmarks/ops/bench_nsa.py finished in 64s ---

=== [48/60] benchmarks/ops/bench_paged_cache_gather.py ===
benchmarks/ops/bench_paged_cache_gather.py::test_paged_kv_cache_gather_bench[ds-v3-chunk-fp8-float8_e4m3fn-bfloat16]
benchmarks/ops/bench_paged_cache_gather.py::test_paged_kv_cache_gather_bench[ds-v3-mixed-bfloat16]
benchmarks/ops/bench_paged_cache_gather.py::test_paged_kv_cache_gather_bench[llama-70b-cp-bfloat16]
benchmarks/ops/bench_paged_cache_gather.py::test_paged_kv_cache_gather_bench[mla-small-float16]
benchmarks/ops/bench_paged_cache_gather.py::test_paged_kv_cache_gather_bench[mla-chunk-fp8-fp16-float8_e4m3fn-float16]
benchmarks/ops/bench_paged_cache_gather.py::test_paged_kv_cache_gather_bench[llama-cp-unaligned-bfloat16]
benchmarks/ops/bench_paged_cache_gather.py::test_paged_kv_cache_gather_bench[mla-b256-bfloat16]

7 tests collected in 4.02s
.......                                                                  [100%]Benchmark report saved to profile_run.log

7 passed in 9.95s
--- benchmarks/ops/bench_paged_cache_gather.py finished in 17s ---

=== [49/60] benchmarks/ops/bench_paged_cache_write.py ===
benchmarks/ops/bench_paged_cache_write.py::test_paged_kv_cache_write_bench[llama-8b-decode-bfloat16-bfloat16]
benchmarks/ops/bench_paged_cache_write.py::test_paged_kv_cache_write_bench[llama-8b-decode-float16-float16]
benchmarks/ops/bench_paged_cache_write.py::test_paged_kv_cache_write_bench[llama-8b-prefill-bfloat16-bfloat16]
benchmarks/ops/bench_paged_cache_write.py::test_paged_kv_cache_write_bench[qwen3-235b-fp8-bfloat16-float8_e4m3fn]
benchmarks/ops/bench_paged_cache_write.py::test_paged_kv_cache_write_bench[gpt-oss-120b-bfloat16-bfloat16]
benchmarks/ops/bench_paged_cache_write.py::test_paged_kv_cache_write_bench[odd-tokens-and-page-float16-float16]
benchmarks/ops/bench_paged_cache_write.py::test_paged_kv_cache_write_bench[qwen3-235b-fp8-fp16-float16-float8_e4m3fn]

7 tests collected in 4.00s
.......                                                                  [100%]Benchmark report saved to profile_run.log

7 passed in 11.44s
--- benchmarks/ops/bench_paged_cache_write.py finished in 19s ---

=== [50/60] benchmarks/ops/bench_pool.py ===
RUNNING [50/60] 30s: benchmarks/ops/bench_pool.py::test_max_pool2d_bench[alexnet-ceil-bfloat16]
RUNNING [50/60] 60s: benchmarks/ops/bench_pool.py::test_mean_pooling_bench[uniform-8k-bfloat16-float32]
benchmarks/ops/bench_pool.py::test_avg_pool1d_bench[audio-downsample-float16]
benchmarks/ops/bench_pool.py::test_avg_pool1d_bench[audio-downsample-float32]
benchmarks/ops/bench_pool.py::test_avg_pool1d_bench[long-temporal-float16]
benchmarks/ops/bench_pool.py::test_avg_pool1d_bench[ceil-bfloat16]
benchmarks/ops/bench_pool.py::test_avg_pool2d_bench[vision-3x3-s2-float16]
benchmarks/ops/bench_pool.py::test_avg_pool2d_bench[vision-3x3-s2-float32]
benchmarks/ops/bench_pool.py::test_avg_pool2d_bench[vision-5x5-s2-float16]
benchmarks/ops/bench_pool.py::test_avg_pool2d_bench[ceil-divisor-bfloat16]
benchmarks/ops/bench_pool.py::test_avg_pool3d_bench[video-2x2x2-float16]
benchmarks/ops/bench_pool.py::test_avg_pool3d_bench[video-2x2x2-float32]
benchmarks/ops/bench_pool.py::test_avg_pool3d_bench[ceil-video-float16]
benchmarks/ops/bench_pool.py::test_avg_pool3d_bench[divisor-bfloat16]
benchmarks/ops/bench_pool.py::test_max_pool1d_bench[sincnet-local-float16]
benchmarks/ops/bench_pool.py::test_max_pool1d_bench[sincnet-local-float32]
benchmarks/ops/bench_pool.py::test_max_pool1d_bench[textcnn-global-float16]
benchmarks/ops/bench_pool.py::test_max_pool1d_bench[ecg-cnn-dilated-bfloat16]
benchmarks/ops/bench_pool.py::test_max_pool1d_indices_bench[sincnet-local-float16]
benchmarks/ops/bench_pool.py::test_max_pool1d_indices_bench[sincnet-local-float32]
benchmarks/ops/bench_pool.py::test_max_pool1d_indices_bench[textcnn-global-float16]
benchmarks/ops/bench_pool.py::test_max_pool1d_indices_bench[ecg-cnn-dilated-bfloat16]
benchmarks/ops/bench_pool.py::test_max_pool2d_bench[resnet-stem-float16]
benchmarks/ops/bench_pool.py::test_max_pool2d_bench[resnet-stem-bfloat16]
benchmarks/ops/bench_pool.py::test_max_pool2d_bench[resnet-stem-float32]
benchmarks/ops/bench_pool.py::test_max_pool2d_bench[vgg-block-float16]
benchmarks/ops/bench_pool.py::test_max_pool2d_bench[vgg-block-bfloat16]
benchmarks/ops/bench_pool.py::test_max_pool2d_bench[vgg-block-float32]
benchmarks/ops/bench_pool.py::test_max_pool2d_bench[alexnet-ceil-float16]
benchmarks/ops/bench_pool.py::test_max_pool2d_bench[alexnet-ceil-bfloat16]
benchmarks/ops/bench_pool.py::test_max_pool2d_bench[alexnet-ceil-float32]
benchmarks/ops/bench_pool.py::test_max_pool2d_indices_bench[resnet-stem-float16]
benchmarks/ops/bench_pool.py::test_max_pool2d_indices_bench[resnet-stem-bfloat16]
benchmarks/ops/bench_pool.py::test_max_pool2d_indices_bench[resnet-stem-float32]
benchmarks/ops/bench_pool.py::test_max_pool2d_indices_bench[vgg-block-float16]
benchmarks/ops/bench_pool.py::test_max_pool2d_indices_bench[vgg-block-bfloat16]
benchmarks/ops/bench_pool.py::test_max_pool2d_indices_bench[vgg-block-float32]
benchmarks/ops/bench_pool.py::test_max_pool2d_indices_bench[alexnet-ceil-float16]
benchmarks/ops/bench_pool.py::test_max_pool2d_indices_bench[alexnet-ceil-bfloat16]
benchmarks/ops/bench_pool.py::test_max_pool2d_indices_bench[alexnet-ceil-float32]
benchmarks/ops/bench_pool.py::test_max_pool3d_bench[c3d-pool1-float16]
benchmarks/ops/bench_pool.py::test_max_pool3d_bench[c3d-pool1-float32]
benchmarks/ops/bench_pool.py::test_max_pool3d_bench[c3d-pool2-float16]
benchmarks/ops/bench_pool.py::test_max_pool3d_bench[medicalnet-stem-bfloat16]
benchmarks/ops/bench_pool.py::test_max_pool3d_indices_bench[c3d-pool1-float16]
benchmarks/ops/bench_pool.py::test_max_pool3d_indices_bench[c3d-pool1-float32]
benchmarks/ops/bench_pool.py::test_max_pool3d_indices_bench[c3d-pool2-float16]
benchmarks/ops/bench_pool.py::test_max_pool3d_indices_bench[medicalnet-stem-bfloat16]
benchmarks/ops/bench_pool.py::test_adaptive_avg_pool2d_bench[resnet-gap-float16]
benchmarks/ops/bench_pool.py::test_adaptive_avg_pool2d_bench[spp-6x6-float16]
benchmarks/ops/bench_pool.py::test_adaptive_avg_pool2d_bench[nondiv-7x7-bfloat16]
benchmarks/ops/bench_pool.py::test_adaptive_avg_pool2d_bench[resnet-gap-unbatched-float16]
benchmarks/ops/bench_pool.py::test_adaptive_max_pool2d_bench[global-1x1-float16]
benchmarks/ops/bench_pool.py::test_adaptive_max_pool2d_bench[spp-6x6-float16]
benchmarks/ops/bench_pool.py::test_adaptive_max_pool2d_bench[nondiv-7x7-bfloat16]
benchmarks/ops/bench_pool.py::test_adaptive_max_pool2d_bench[global-1x1-unbatched-float16]
benchmarks/ops/bench_pool.py::test_adaptive_max_pool2d_indices_bench[global-1x1-float16]
benchmarks/ops/bench_pool.py::test_adaptive_max_pool2d_indices_bench[spp-6x6-float16]
benchmarks/ops/bench_pool.py::test_adaptive_max_pool2d_indices_bench[nondiv-7x7-bfloat16]
benchmarks/ops/bench_pool.py::test_adaptive_max_pool2d_indices_bench[global-1x1-unbatched-float16]
benchmarks/ops/bench_pool.py::test_mean_pooling_bench[uniform-8k-float16-float32]
benchmarks/ops/bench_pool.py::test_mean_pooling_bench[uniform-8k-bfloat16-float32]
benchmarks/ops/bench_pool.py::test_mean_pooling_bench[uniform-batched-float16-float32]
benchmarks/ops/bench_pool.py::test_mean_pooling_bench[ragged-even-float16-float32]
benchmarks/ops/bench_pool.py::test_mean_pooling_bench[ragged-even-float32-float32]
benchmarks/ops/bench_pool.py::test_mean_pooling_bench[ragged-tail-float16-float32]
benchmarks/ops/bench_pool.py::test_mean_pooling_bench[ragged-batched-float16-float32]

65 tests collected in 2.60s
.................................................................        [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_pool.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

benchmarks/ops/bench_pool.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
65 passed, 58 warnings in 79.50s (0:01:19)
--- benchmarks/ops/bench_pool.py finished in 85s ---

=== [51/60] benchmarks/ops/bench_reduce.py ===
RUNNING [51/60] 30s: benchmarks/ops/bench_reduce.py::test_amax_bench[3d-multidim-float16]
RUNNING [51/60] 60s: benchmarks/ops/bench_reduce.py::test_var_mean_bench[hidden-state-biased-bfloat16]
benchmarks/ops/bench_reduce.py::test_sum_bench[hidden-state-float16]
benchmarks/ops/bench_reduce.py::test_sum_bench[hidden-state-bfloat16]
benchmarks/ops/bench_reduce.py::test_sum_bench[long-seq-bfloat16]
benchmarks/ops/bench_reduce.py::test_sum_bench[hidden-state-dim0-bfloat16]
benchmarks/ops/bench_reduce.py::test_sum_bench[hidden-state-keepdim-bfloat16]
benchmarks/ops/bench_reduce.py::test_sum_bench[3d-multidim-float16]
benchmarks/ops/bench_reduce.py::test_sum_bench[mlp-intermediate-float32]
benchmarks/ops/bench_reduce.py::test_sum_bench[hidden-state-bfloat16-float32]
benchmarks/ops/bench_reduce.py::test_mean_bench[hidden-state-float16]
benchmarks/ops/bench_reduce.py::test_mean_bench[hidden-state-bfloat16]
benchmarks/ops/bench_reduce.py::test_mean_bench[long-seq-bfloat16]
benchmarks/ops/bench_reduce.py::test_mean_bench[3d-multidim-float16]
benchmarks/ops/bench_reduce.py::test_mean_bench[mlp-intermediate-float32]
benchmarks/ops/bench_reduce.py::test_mean_bench[hidden-state-bfloat16-float32]
benchmarks/ops/bench_reduce.py::test_amax_bench[hidden-state-float16]
benchmarks/ops/bench_reduce.py::test_amax_bench[hidden-state-bfloat16]
benchmarks/ops/bench_reduce.py::test_amax_bench[long-seq-bfloat16]
benchmarks/ops/bench_reduce.py::test_amax_bench[3d-multidim-float16]
benchmarks/ops/bench_reduce.py::test_amax_bench[mlp-intermediate-float32]
benchmarks/ops/bench_reduce.py::test_amin_bench[hidden-state-float16]
benchmarks/ops/bench_reduce.py::test_amin_bench[hidden-state-bfloat16]
benchmarks/ops/bench_reduce.py::test_amin_bench[long-seq-bfloat16]
benchmarks/ops/bench_reduce.py::test_amin_bench[3d-multidim-float16]
benchmarks/ops/bench_reduce.py::test_amin_bench[mlp-intermediate-float32]
benchmarks/ops/bench_reduce.py::test_prod_bench[hidden-state-float16]
benchmarks/ops/bench_reduce.py::test_prod_bench[hidden-state-bfloat16]
benchmarks/ops/bench_reduce.py::test_prod_bench[long-seq-bfloat16]
benchmarks/ops/bench_reduce.py::test_prod_bench[3d-non-last-axis-float16]
benchmarks/ops/bench_reduce.py::test_prod_bench[mlp-intermediate-float32]
benchmarks/ops/bench_reduce.py::test_prod_bench[hidden-state-bfloat16-float32]
benchmarks/ops/bench_reduce.py::test_std_bench[hidden-state-float16]
benchmarks/ops/bench_reduce.py::test_std_bench[hidden-state-bfloat16]
benchmarks/ops/bench_reduce.py::test_std_bench[long-seq-bfloat16]
benchmarks/ops/bench_reduce.py::test_std_bench[3d-multidim-float16]
benchmarks/ops/bench_reduce.py::test_std_bench[mlp-intermediate-float32]
benchmarks/ops/bench_reduce.py::test_std_bench[hidden-state-biased-bfloat16]
benchmarks/ops/bench_reduce.py::test_var_bench[hidden-state-float16]
benchmarks/ops/bench_reduce.py::test_var_bench[hidden-state-bfloat16]
benchmarks/ops/bench_reduce.py::test_var_bench[long-seq-bfloat16]
benchmarks/ops/bench_reduce.py::test_var_bench[3d-multidim-float16]
benchmarks/ops/bench_reduce.py::test_var_bench[mlp-intermediate-float32]
benchmarks/ops/bench_reduce.py::test_var_bench[hidden-state-biased-bfloat16]
benchmarks/ops/bench_reduce.py::test_var_mean_bench[hidden-state-float16]
benchmarks/ops/bench_reduce.py::test_var_mean_bench[hidden-state-bfloat16]
benchmarks/ops/bench_reduce.py::test_var_mean_bench[long-seq-bfloat16]
benchmarks/ops/bench_reduce.py::test_var_mean_bench[3d-multidim-float16]
benchmarks/ops/bench_reduce.py::test_var_mean_bench[mlp-intermediate-float32]
benchmarks/ops/bench_reduce.py::test_var_mean_bench[hidden-state-biased-bfloat16]

48 tests collected in 1.70s
................................................                         [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_reduce.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_reduce.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
48 passed, 58 warnings in 56.03s
--- benchmarks/ops/bench_reduce.py finished in 61s ---

=== [52/60] benchmarks/ops/bench_rope.py ===
RUNNING [52/60] 30s: benchmarks/ops/bench_rope.py::test_rope_neox_position_ids_bench[qwen3-8b-decode-b32-bfloat16-int32]
benchmarks/ops/bench_rope.py::test_rope_bench[neox-1d-2k-float16]
benchmarks/ops/bench_rope.py::test_rope_bench[neox-1d-2k-float32]
benchmarks/ops/bench_rope.py::test_rope_bench[neox-1d-4k-bfloat16]
benchmarks/ops/bench_rope.py::test_rope_bench[neox-2d-2k-float16]
benchmarks/ops/bench_rope.py::test_rope_bench[interleaved-1d-2k-float16]
benchmarks/ops/bench_rope.py::test_rope_bench[interleaved-2d-2k-bfloat16]
benchmarks/ops/bench_rope.py::test_rope_bench[interleaved-1d-5k-float32]
benchmarks/ops/bench_rope.py::test_rope_llama31_bench[1d-8k-bfloat16]
benchmarks/ops/bench_rope.py::test_rope_llama31_bench[2d-8k-float16]
benchmarks/ops/bench_rope.py::test_rope_llama31_bench[1d-5k-float32]
benchmarks/ops/bench_rope.py::test_yarn_bench[1d-8k-bfloat16]
benchmarks/ops/bench_rope.py::test_yarn_bench[2d-8k-float16]
benchmarks/ops/bench_rope.py::test_yarn_bench[1d-5k-float32]
benchmarks/ops/bench_rope.py::test_rope_longrope_bench[1d-8k-bfloat16]
benchmarks/ops/bench_rope.py::test_rope_longrope_bench[2d-8k-float16]
benchmarks/ops/bench_rope.py::test_rope_longrope_bench[1d-5k-float32]
benchmarks/ops/bench_rope.py::test_rope_longrope_bench[1d-8k-rescaled-bfloat16-float32]
benchmarks/ops/bench_rope.py::test_rope_longrope_bench[1d-8k-rescaled-bfloat16-float16]
benchmarks/ops/bench_rope.py::test_rope_longrope_bench[1d-8k-rescaled-bfloat16-bfloat16]
benchmarks/ops/bench_rope.py::test_rope_neox_position_ids_bench[prefill-2k-float16-int32]
benchmarks/ops/bench_rope.py::test_rope_neox_position_ids_bench[prefill-4k-bfloat16-int32]
benchmarks/ops/bench_rope.py::test_rope_neox_position_ids_bench[prefill-varlen-float32-int64]
benchmarks/ops/bench_rope.py::test_rope_neox_position_ids_bench[qwen3-8b-decode-b32-bfloat16-int32]

23 tests collected in 1.59s
.......................                                                  [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_rope.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
23 passed, 14 warnings in 27.14s
--- benchmarks/ops/bench_rope.py finished in 32s ---

=== [53/60] benchmarks/ops/bench_sampling_from_probs.py ===
RUNNING [53/60] 30s: benchmarks/ops/bench_sampling_from_probs.py::test_sampling_from_probs_bench[llama2-7b-b100]
benchmarks/ops/bench_sampling_from_probs.py::test_sampling_from_probs_bench[llama-8b-b1]
benchmarks/ops/bench_sampling_from_probs.py::test_sampling_from_probs_bench[llama-8b-b64]
benchmarks/ops/bench_sampling_from_probs.py::test_sampling_from_probs_bench[llama-8b-b256]
benchmarks/ops/bench_sampling_from_probs.py::test_sampling_from_probs_bench[qwen3-235b-b128]
benchmarks/ops/bench_sampling_from_probs.py::test_sampling_from_probs_bench[gpt-oss-120b-b64]
benchmarks/ops/bench_sampling_from_probs.py::test_sampling_from_probs_bench[ds-v3-b17]
benchmarks/ops/bench_sampling_from_probs.py::test_sampling_from_probs_bench[llama2-7b-b100]

7 tests collected in 1.53s
.......                                                                  [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_sampling_from_probs.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
7 passed, 14 warnings in 28.83s
--- benchmarks/ops/bench_sampling_from_probs.py finished in 34s ---

=== [54/60] benchmarks/ops/bench_smooth_quant.py ===
benchmarks/ops/bench_smooth_quant.py::test_smooth_quant_bench[llama-8b-prefill-float16]
benchmarks/ops/bench_smooth_quant.py::test_smooth_quant_bench[llama-8b-prefill-bfloat16]
benchmarks/ops/bench_smooth_quant.py::test_smooth_quant_bench[llama-8b-decode-bfloat16]
benchmarks/ops/bench_smooth_quant.py::test_smooth_quant_bench[llama-70b-prefill-bfloat16]
benchmarks/ops/bench_smooth_quant.py::test_smooth_quant_bench[gpt-oss-20b-prefill-bfloat16]
benchmarks/ops/bench_smooth_quant.py::test_smooth_quant_bench[ragged-k-float16]
benchmarks/ops/bench_smooth_quant.py::test_smooth_quant_bench[ragged-k-decode-bfloat16]

7 tests collected in 3.01s
.......                                                                  [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_smooth_quant.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
7 passed, 14 warnings in 12.49s
--- benchmarks/ops/bench_smooth_quant.py finished in 19s ---

=== [55/60] benchmarks/ops/bench_softmax.py ===
RUNNING [55/60] 30s: benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-256-bfloat16]
RUNNING [55/60] 60s: benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-16384-float16]
RUNNING [55/60] 90s: benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-65536-float32]
RUNNING [55/60] 120s: benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-262144-bfloat16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[attn-weights-4k-float16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[attn-weights-4k-bfloat16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[attn-weights-4k-float32]
benchmarks/ops/bench_softmax.py::test_softmax_bench[attn-weights-32k-bfloat16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[lm-head-float16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[lm-head-bfloat16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[lm-head-float32]
benchmarks/ops/bench_softmax.py::test_softmax_bench[llama-8b-lm-head-bfloat16-float32]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-256-float16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-256-bfloat16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-256-float32]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-512-float16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-512-bfloat16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-512-float32]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-1024-float16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-1024-bfloat16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-1024-float32]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-2048-float16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-2048-bfloat16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-2048-float32]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-4096-float16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-4096-bfloat16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-4096-float32]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-8192-float16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-8192-bfloat16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-8192-float32]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-16384-float16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-16384-bfloat16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-16384-float32]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-32768-float16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-32768-bfloat16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-32768-float32]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-65536-float16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-65536-bfloat16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-65536-float32]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-131072-float16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-131072-bfloat16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-131072-float32]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-262144-float16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-262144-bfloat16]
benchmarks/ops/bench_softmax.py::test_softmax_bench[quack-throughput-262144-float32]
benchmarks/ops/bench_softmax.py::test_softmax_bench[qwen3-8b-lm-head-b1-float32]
benchmarks/ops/bench_softmax.py::test_log_softmax_bench[attn-weights-4k-float16]
benchmarks/ops/bench_softmax.py::test_log_softmax_bench[attn-weights-4k-bfloat16]
benchmarks/ops/bench_softmax.py::test_log_softmax_bench[attn-weights-4k-float32]
benchmarks/ops/bench_softmax.py::test_log_softmax_bench[attn-weights-32k-bfloat16]
benchmarks/ops/bench_softmax.py::test_log_softmax_bench[lm-head-float16]
benchmarks/ops/bench_softmax.py::test_log_softmax_bench[lm-head-bfloat16]
benchmarks/ops/bench_softmax.py::test_log_softmax_bench[lm-head-float32]
benchmarks/ops/bench_softmax.py::test_log_softmax_bench[llama-8b-lm-head-bfloat16-float32]
benchmarks/ops/bench_softmax.py::test_logsumexp_bench[attn-weights-4k-float16]
benchmarks/ops/bench_softmax.py::test_logsumexp_bench[attn-weights-4k-bfloat16]
benchmarks/ops/bench_softmax.py::test_logsumexp_bench[attn-weights-32k-bfloat16]
benchmarks/ops/bench_softmax.py::test_logsumexp_bench[lm-head-float16]
benchmarks/ops/bench_softmax.py::test_logsumexp_bench[lm-head-bfloat16]
benchmarks/ops/bench_softmax.py::test_logsumexp_bench[3d-multidim-float16]
benchmarks/ops/bench_softmax.py::test_logsumexp_bench[llama-8b-lm-head-float32]

57 tests collected in 2.09s
.........................................................                [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_softmax.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_softmax.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
57 passed, 58 warnings in 142.91s (0:02:22)
--- benchmarks/ops/bench_softmax.py finished in 149s ---

=== [56/60] benchmarks/ops/bench_top_k_mask.py ===
benchmarks/ops/bench_top_k_mask.py::test_top_k_mask_bench[llama-8b-b1-bfloat16]
benchmarks/ops/bench_top_k_mask.py::test_top_k_mask_bench[llama-8b-b1-float32]
benchmarks/ops/bench_top_k_mask.py::test_top_k_mask_bench[llama-8b-b64-bfloat16]
benchmarks/ops/bench_top_k_mask.py::test_top_k_mask_bench[llama-8b-b256-float16]
benchmarks/ops/bench_top_k_mask.py::test_top_k_mask_bench[llama-8b-b256-bfloat16]
benchmarks/ops/bench_top_k_mask.py::test_top_k_mask_bench[qwen3-235b-b128-bfloat16]
benchmarks/ops/bench_top_k_mask.py::test_top_k_mask_bench[gpt-oss-120b-b64-bfloat16]
benchmarks/ops/bench_top_k_mask.py::test_top_k_mask_bench[gpt2-b17-mixed-float16]
benchmarks/ops/bench_top_k_mask.py::test_top_k_mask_bench[deepseek-v3-b17-mixed-bfloat16]

9 tests collected in 1.54s
.........                                                                [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_top_k_mask.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
9 passed, 14 warnings in 23.50s
--- benchmarks/ops/bench_top_k_mask.py finished in 29s ---

=== [57/60] benchmarks/ops/bench_top_k_top_p_mask.py ===
benchmarks/ops/bench_top_k_top_p_mask.py::test_top_k_top_p_mask_bench[llama-8b-b1-bfloat16]
benchmarks/ops/bench_top_k_top_p_mask.py::test_top_k_top_p_mask_bench[llama-8b-b1-float32]
benchmarks/ops/bench_top_k_top_p_mask.py::test_top_k_top_p_mask_bench[llama-8b-b64-bfloat16]
benchmarks/ops/bench_top_k_top_p_mask.py::test_top_k_top_p_mask_bench[llama-8b-b256-float16]
benchmarks/ops/bench_top_k_top_p_mask.py::test_top_k_top_p_mask_bench[llama-8b-b256-bfloat16]
benchmarks/ops/bench_top_k_top_p_mask.py::test_top_k_top_p_mask_bench[qwen3-235b-b128-bfloat16]
benchmarks/ops/bench_top_k_top_p_mask.py::test_top_k_top_p_mask_bench[gpt2-b17-mixed-float16]
benchmarks/ops/bench_top_k_top_p_mask.py::test_top_k_top_p_mask_bench[deepseek-v3-b100-bfloat16]

8 tests collected in 1.55s
........                                                                 [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_top_k_top_p_mask.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
8 passed, 14 warnings in 20.69s
--- benchmarks/ops/bench_top_k_top_p_mask.py finished in 26s ---

=== [58/60] benchmarks/ops/bench_top_p_mask.py ===
benchmarks/ops/bench_top_p_mask.py::test_top_p_mask_bench[llama-8b-b1-bfloat16]
benchmarks/ops/bench_top_p_mask.py::test_top_p_mask_bench[llama-8b-b1-float32]
benchmarks/ops/bench_top_p_mask.py::test_top_p_mask_bench[llama-8b-b64-bfloat16]
benchmarks/ops/bench_top_p_mask.py::test_top_p_mask_bench[llama-8b-b256-float16]
benchmarks/ops/bench_top_p_mask.py::test_top_p_mask_bench[llama-8b-b256-bfloat16]
benchmarks/ops/bench_top_p_mask.py::test_top_p_mask_bench[qwen3-235b-b128-bfloat16]
benchmarks/ops/bench_top_p_mask.py::test_top_p_mask_bench[gpt-oss-120b-b64-bfloat16]
benchmarks/ops/bench_top_p_mask.py::test_top_p_mask_bench[deepseek-v3-b17-bfloat16]
benchmarks/ops/bench_top_p_mask.py::test_top_p_mask_bench[llama2-7b-b100-float16]

9 tests collected in 1.54s
.........                                                                [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_top_p_mask.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
9 passed, 14 warnings in 23.65s
--- benchmarks/ops/bench_top_p_mask.py finished in 29s ---

=== [59/60] benchmarks/ops/bench_topk_select.py ===
RUNNING [59/60] 30s: benchmarks/ops/bench_topk_select.py::test_topk_select_bench[prefill-k1024]
RUNNING [59/60] 60s: benchmarks/ops/bench_topk_select.py::test_topk_select_bench[prefill-k1024]
RUNNING [59/60] 90s: benchmarks/ops/bench_topk_select.py::test_topk_select_bench[prefill-k1024]
RUNNING [59/60] 120s: benchmarks/ops/bench_topk_select.py::test_topk_select_bench[prefill-k1024]
benchmarks/ops/bench_topk_select.py::test_topk_select_bench[prefill-k1024]
benchmarks/ops/bench_topk_select.py::test_topk_select_bench[prefill-k2048]
benchmarks/ops/bench_topk_select.py::test_topk_select_bench[ds-v32-topk-decode-b1]

3 tests collected in 6.72s
...                                                                      [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_topk_select.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
3 passed, 14 warnings in 137.62s (0:02:17)
--- benchmarks/ops/bench_topk_select.py finished in 148s ---

=== [60/60] benchmarks/ops/bench_vector_norm.py ===
RUNNING [60/60] 30s: benchmarks/ops/bench_vector_norm.py::test_vector_norm_bench[inf-long-seq-bfloat16]
benchmarks/ops/bench_vector_norm.py::test_vector_norm_bench[l1-hidden-state-float16]
benchmarks/ops/bench_vector_norm.py::test_vector_norm_bench[l1-hidden-state-bfloat16]
benchmarks/ops/bench_vector_norm.py::test_vector_norm_bench[l1-long-seq-bfloat16]
benchmarks/ops/bench_vector_norm.py::test_vector_norm_bench[l1-3d-multidim-float16]
benchmarks/ops/bench_vector_norm.py::test_vector_norm_bench[l1-mlp-intermediate-float32]
benchmarks/ops/bench_vector_norm.py::test_vector_norm_bench[l1-hidden-state-fp32-bfloat16-float32]
benchmarks/ops/bench_vector_norm.py::test_vector_norm_bench[l2-hidden-state-float16]
benchmarks/ops/bench_vector_norm.py::test_vector_norm_bench[l2-hidden-state-bfloat16]
benchmarks/ops/bench_vector_norm.py::test_vector_norm_bench[l2-long-seq-bfloat16]
benchmarks/ops/bench_vector_norm.py::test_vector_norm_bench[l2-3d-multidim-float16]
benchmarks/ops/bench_vector_norm.py::test_vector_norm_bench[l2-mlp-intermediate-float32]
benchmarks/ops/bench_vector_norm.py::test_vector_norm_bench[l2-hidden-state-fp32-bfloat16-float32]
benchmarks/ops/bench_vector_norm.py::test_vector_norm_bench[inf-hidden-state-float16]
benchmarks/ops/bench_vector_norm.py::test_vector_norm_bench[inf-hidden-state-bfloat16]
benchmarks/ops/bench_vector_norm.py::test_vector_norm_bench[inf-long-seq-bfloat16]
benchmarks/ops/bench_vector_norm.py::test_vector_norm_bench[inf-3d-multidim-float16]
benchmarks/ops/bench_vector_norm.py::test_vector_norm_bench[inf-mlp-intermediate-float32]
benchmarks/ops/bench_vector_norm.py::test_vector_norm_bench[inf-hidden-state-fp32-bfloat16-float32]

18 tests collected in 2.00s
..................                                                       [100%]Benchmark report saved to profile_run.log

=============================== warnings summary ===============================
benchmarks/ops/bench_vector_norm.py: 44 warnings
  /usr/local/lib/python3.12/dist-packages/triton/runtime/autotuner.py:101: DeprecationWarning: warmup, rep, and use_cuda_graph parameters are deprecated. See https://github.com/triton-lang/triton/pull/4496 for details.
    warnings.warn(("warmup, rep, and use_cuda_graph parameters are deprecated. See "

benchmarks/ops/bench_vector_norm.py: 14 warnings
  /usr/local/lib/python3.12/dist-packages/torch/jit/_script.py:365: DeprecationWarning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`.
    warnings.warn(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
18 passed, 58 warnings in 33.22s
--- benchmarks/ops/bench_vector_norm.py finished in 39s ---

2 benchmark file(s) failed:
  benchmarks/ops/bench_batch_norm.py
  benchmarks/ops/bench_cumulative.py
