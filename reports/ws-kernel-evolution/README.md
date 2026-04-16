# WS Kernel Evolution: From Schedule Redesign To Hardware-Facing Refinements

This report summarizes one kernel evolution path for causal GQA on Hopper:

1. `Single-CTA WGMMA Pipeline -> Baseline WS Pipeline` is a schedule win.
2. `Baseline WS Pipeline -> KV-Locality Reorder` is a memory-system win.
3. `KV-Locality Reorder -> Post-wait0 Delayed Rescale` is a register-flow win.

The short version is simple: first we fixed the information flow, then we made
that schedule fit Hopper better.

## Setup

The main mechanistic discussion uses one representative causal analysis point:
`B=4, S=4096, H=64, Hkv=8, D=128`. We compare milestones under the same GPU and
measurement discipline, and we use multiple evidence types together:

- end-to-end latency
- cycle-level timeline splits
- tensor-pipe utilization
- generated CUDA, `ptxas`, and SASS
- Nsight Compute memory-system counters

That combination matters because it lets us separate "does less work" from
"does the same work with a better schedule."

## 1. Single-CTA Baseline

The pre-WS kernel is already Hopper-oriented: it uses WGMMA and software
pipelining, so it is a meaningful baseline rather than a strawman. Its core
limitation is structural. One CTA still owns the entire local loop over `K/V`
tiles, so data movement, softmax-side work, and Tensor Core issue remain tied
to one CTA-local execution path.

![Single-CTA baseline](figures/pre_pr871_schematic.png)

This is why the pre-WS kernel should not be described with the same vocabulary
as the later WS kernels. The later kernels are about explicit producer /
consumer handoff; the baseline is still a single-CTA software pipeline with
only local overlap across loop iterations.

## 2. Baseline WS As A Schedule Win

The first large gain comes from changing the execution organization itself.
`Baseline WS Pipeline` splits the CTA into one producer warp group and two
consumer warp groups. That change borrows the same class of information-flow
idea emphasized by FlashAttention-3: decouple data movement from Tensor Core
issue, then keep the consumers in a stable ping-pong rhythm.

![Baseline WS schematic](figures/ws_two_wg_schematic.png)

![Three-kernel full cycle](figures/ws_three_kernel_full_cycle.png)

The strongest evidence that this is a schedule win is that the Tensor Core work
does not materially change, but its packing does. Across the pre-WS and
baseline-WS milestones, GMMA work is essentially unchanged, yet tensor-pipe
utilization rises from `35.2%` to `60.0%`. The kernel is not doing less Tensor
Core math; it is feeding and phasing the same math more effectively.

This also matches the size of the end-to-end gain. The first WS milestone
delivers about `30% ~ 41%` lower latency across the production-aligned prefill
shapes we tracked. That is much easier to explain as an architectural schedule
change than as a small local cleanup.

## 3. Reorder As A Memory-System Win

The next milestone, `KV-Locality Reorder`, is more subtle. In the local
steady-state split, the core windows barely move:

- `qk_issue`: `198 -> 200`
- `pv_issue`: `215 -> 216`
- `softmax_core`: `1309 -> 1313`

Yet total measured time still improves from `2919` cycles to `2841` cycles.
That makes a pure "better local compute schedule" explanation too weak. The
improvement is better explained as a memory-system change.

The new Nsight Compute L2 pass sharpens that claim. Reorder does not simply
lower the L2 miss rate. On the canonical shape, the read miss ratio actually
increases from `0.0808` to `0.1145`. What drops instead is total traffic:

- total L2 read lookups: `656k -> 388k`
- absolute L2 read misses: `53.0k -> 44.5k`
- DRAM read bytes: `8.04M -> 7.00M`

So the better description is not "lower miss-rate win." It is a
memory-system-facing traffic-shaping win: reorder reduces how much read traffic
the WS schedule generates, even if the remaining stream does not have a lower
miss ratio.

![Milestone stitched timelines](figures/milestone_stitched_timelines.png)

This step is important because it narrows the remaining search space. Once the
schedule is structurally sound and the memory-system footprint is smaller, the
last gap to the final kernel is no longer well explained by locality alone.

## 4. Delayed Rescale As A Register-Flow Win

The last major gain comes from moving `rescale(acc_o)` to after `wait0`. At
first glance the result looks contradictory, because some launch-side windows
become much larger:

- `qk_issue`: `200 -> 1066`
- `pv_issue`: `216 -> 941`

But the kernel still gets faster overall:

| Milestone | Measured total cycles |
|:--|--:|
| `reorder` | `2841` |
| `reorder + delayed rescale only` | `2716` |
| `anchor` | `2668` |

The reason is that delayed rescale does not make `QK` or `PV` arithmetic
intrinsically cheaper. It changes where the hazard cost is paid.

In `reorder`, the old output path `acc_o *= ss` still lives before `PV`. That
forces one crowded region to carry the current `acc_s` path, the softmax state,
the casted `acc_s` values consumed by `PV`, and the old output accumulator path
at the same time. In the delayed-rescale variant, the `acc_o` path moves to
after `wait0`, so the hottest `pre-PV -> wait1 -> softmax` region becomes much
cleaner.

The delayed-rescale-only experiment is the key isolating test. Without adding
the rest of the anchor machinery, moving rescale alone already reproduces most
of the final shape: `softmax_core` drops from `1313` to `1056`, close to
anchor's `1030`, and total time improves from `2841` to `2716`.

The codegen evidence makes the mechanism concrete. At the generated CUDA level,
the `QK` loops still look broadly similar across `reorder`,
`delayed-rescale-only`, and `anchor`. But the generated SASS is very different:

- `reorder` lowers `QK` into a relatively compact `HGMMA` burst
- `delayed-rescale-only` and `anchor` interleave almost every `HGMMA` with
  `WARPGROUP.DEPBAR + ARRIVE`

The `ptxas` diagnostics point in the same direction. `reorder` gets injected
`warpgroup.wait` and spills, while `delayed-rescale-only` and `anchor` instead
expose WGMMA serialization hazards tied to accumulator access.

So the most defensible interpretation is a coupled one: the source-level
register-flow change causes the compiler to lower the same logical `QK/PV`
stages into a different Hopper `WARPGROUP/HGMMA` schedule, and that new
schedule interacts differently with real accumulator-pipeline constraints.

This also explains the apparent paradox of longer `QK/PV` windows but better
steady-state throughput. The cost does not disappear; it moves. `reorder`
appears to pay more in the downstream `wait1 / softmax-side` region through
spills and injected waits. Delayed rescale pays more in the launch-side
`QK/PV` windows, but it makes the downstream hot window much cleaner, and that
trade is favorable for end-to-end throughput.

## 5. What The Evolution Path Teaches

Taken together, the path is not one long blur of tuning. It has a clean
structure:

- `Single-CTA -> Baseline WS`: schedule / information-flow win
- `Baseline WS -> Reorder`: memory-system / locality win
- `Reorder -> Delayed Rescale`: register-flow win

That decomposition gives each milestone a different role. First, make the
producer / consumer schedule explicit. Then reduce the memory-system footprint
of that schedule. Finally, clean up the register and accumulator flow inside the
consumer hot window.

The practical design lesson from the final step is not "add more waits." It is
"use waits as stage boundaries." `wait1` and `wait0` are useful because they
separate regions with different live values and different accumulator pressure.
In WS kernels, heavy old-state repair work should stay away from the current hot
path whenever possible.

## 6. Failed Directions And Constraints

Several side paths were useful precisely because they did not become the main
explanation.

- More aggressive overlap variants helped map the design space, but the winning
  story was not "more overlap at any cost." The gains were better explained by
  schedule quality, memory-system footprint, and register-flow cleanup.
- Zero-clear and `ScaleOut::Zero` were not a general fix for the causal path.
  The working fix was to move the mask to a post-WGMMA point where the dataflow
  was already stable.
- Wait placement mattered more than simply "release earlier." The high-value
  lesson was to use `wait1` and `wait0` to keep heavy data paths from colliding
  in the same hot window.
- Some limitations were methodological. Fine-grained in-loop timing for the
  pre-WS kernel still hits a TileLang/TVM `WgmmaSyncRewriter` crash in this
  environment, so the pre-WS node has coarse timing but not the same internal
  split as the WS milestones.

## 7. Appendix: Production Shapes Vs FA3

The discussion above focuses on one canonical causal analysis point, but the
same milestone path was also measured on several production-prefill shapes
against FA3 on the same GPU. This table is meant as a scope check: it shows
where the final kernel is already near FA3 and where a meaningful gap remains.

| Shape | Base ms | Reorder ms | Anchor ms | FA3 ms | Anchor / FA3 ms | Anchor TFLOPS | FA3 TFLOPS | Anchor / FA3 TF |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| llama8b-1k | 0.0696 | 0.0719 | n/a | 0.1184 | n/a | n/a | 72.6 | n/a |
| llama8b-4k | 0.3165 | 0.3099 | 0.2630 | 0.2758 | 95.3% | 522.6 | 498.3 | 104.9% |
| llama8b-8k | 1.0321 | 0.9938 | 0.9132 | 0.8371 | 109.1% | 602.0 | 656.7 | 91.7% |
| llama8b-32k | 17.0063 | 16.2642 | 15.4076 | 12.9126 | 119.3% | 570.9 | 681.2 | 83.8% |
| llama8b-128k | 273.6086 | 267.2308 | 259.1798 | 216.1482 | 119.9% | 543.0 | 651.1 | 83.4% |
| llama70b-4k | 0.5636 | 0.5575 | 0.4863 | 0.4680 | 103.9% | 565.2 | 587.3 | 96.2% |
| llama405b-4k | 1.0463 | 1.0164 | 0.9440 | 0.8598 | 109.8% | 582.4 | 639.4 | 91.1% |

Two quick readings are enough for this appendix:

- At `4k`, the final kernel is already close to FA3, and on `llama8b-4k` it is
  slightly faster in elapsed time on this measurement set.
- At longer contexts, the schedule, memory-system, and register-flow
  improvements from this report still matter, but they do not fully close the
  remaining throughput gap to FA3.

`anchor_causal` is intentionally marked `n/a` on `llama8b-1k` because that
configuration does not satisfy `total_pairs >= NUM_SMS` in this setup.

## Summary

The central result is that this kernel evolution path contains one large
schedule win followed by two hardware-facing refinements. Baseline WS wins by
reorganizing information flow. Reorder wins by shrinking the memory-system
footprint. Delayed rescale wins by moving heavy register and accumulator
pressure out of the hottest consumer window.
