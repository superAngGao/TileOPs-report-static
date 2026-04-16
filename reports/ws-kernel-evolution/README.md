# WS Kernel Evolution: From Schedule Redesign To Hardware-Facing Refinements

## Introduction

This report asks how a Hopper causal GQA forward kernel moved from a
single-CTA WGMMA pipeline to a warp-specialized WS kernel that recovers most of
the practical gap to FA3, while still leaving a visible long-context gap that
can be explained rather than hand-waved away.

The main point is that this evolution path is not one long blur of tuning. It
contains one foundational schedule redesign and then two smaller
hardware-facing refinements:

1. `Single-CTA WGMMA Pipeline -> Baseline WS Pipeline` is a schedule win.
2. `Baseline WS Pipeline -> KV-Locality Reorder` is a memory-system win.
3. `KV-Locality Reorder -> Post-wait0 Delayed Rescale` is a register-flow win.

The short version is simple: first we fixed the information flow, then we made
that schedule fit Hopper better.

## End-To-End Results Vs FA3

Before the mechanism sections, it helps to see the end-to-end outcome. The same
milestone path was measured on several production-prefill shapes against FA3 on
the same GPU. For the final causal row, we now report the best available anchor
strategy per shape: either the original paired anchor or the newer single-tile
outer-scheduler variant.

| Shape | Base ms | Reorder ms | Best Anchor ms | Anchor Variant | FA3 ms | Best Anchor / FA3 ms | Best Anchor TFLOPS | FA3 TFLOPS | Best Anchor / FA3 TF |
| --- | ---: | ---: | ---: | :-- | ---: | ---: | ---: | ---: | ---: |
| llama8b-4k | 0.3165 | 0.3099 | 0.2665 | paired | 0.2758 | 96.6% | 515.8 | 498.3 | 103.5% |
| llama8b-8k | 1.0321 | 0.9938 | 0.9151 | paired | 0.8371 | 109.3% | 600.7 | 656.7 | 91.5% |
| llama8b-32k | 17.0063 | 16.2642 | 14.3983 | single-tile | 12.9126 | 111.5% | 610.9 | 681.2 | 89.7% |
| llama8b-128k | 273.6086 | 267.2308 | 254.9966 | paired | 216.1482 | 118.0% | 551.9 | 651.1 | 84.8% |
| llama8b-256k | 1130.9110 | 1081.5928 | 1033.3350 | paired | 873.7935 | 118.3% | 544.8 | 644.3 | 84.5% |
| llama70b-4k | 0.5636 | 0.5575 | 0.4863 | paired | 0.4680 | 103.9% | 565.2 | 587.3 | 96.2% |
| llama405b-4k | 1.0463 | 1.0164 | 0.9440 | paired | 0.8598 | 109.8% | 582.4 | 639.4 | 91.1% |

Three front-door readings matter:

- At `4k`, the final anchor-style kernel is already close to FA3, and on
  `llama8b-4k` it is slightly faster in elapsed time on this measurement set.
- The first WS milestone is the dominant structural step-change.
- At longer contexts, the path still helps materially, but it does not fully
  close the remaining gap to FA3.

The `Best Anchor` column is intentionally dispatch-oriented. For the
`llama8b` causal rows, it takes the better of the paired and single-tile
anchor strategies from a follow-up paired-vs-single sweep; for the larger-model
`4k` rows, only the paired anchor has been measured so far, so `Best Anchor`
remains the paired result there.

The `llama8b-256k` row was added in a follow-up run under the same measurement
setup as the rest of the table.

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

Relative to the single-CTA baseline, this step makes three concrete structural
changes. `K/V` movement is pulled into a dedicated producer warp group, the
consumer body is split into `WG1` and `WG2` with explicit handoff between them,
and the kernel adopts the persistent WS execution style used by the later
milestones. So this is not a local cleanup inside one loop body; it is a change
in who does the work and how that work is phased.

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

That is consistent with the actual source-level change. Reorder keeps the same
`1 producer + 2 consumers` WS skeleton and nearly the same consumer core body.
What changes is the traversal order of the persistent kernel: the work becomes
more `KV`-head-friendly, so neighboring iterations reuse a more similar `K/V`
working set. This is why the memory-system footprint improves even though the
local arithmetic windows look almost unchanged.

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

Here the exact code motion is the key fact. In `reorder`, the old output path
still performs `rescale(acc_o)` before `PV`. In the delayed-rescale variant,
that work is removed from the `pre-PV` region and moved to after `wait0`. The
full anchor kernel keeps that same post-`wait0` placement and layers its own
wait-placement cleanup on top, but the isolated delayed-rescale-only result
shows that the rescale move is already the dominant source-level change.

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

## 6. A Causal-Specific Scheduler Choice: Paired Vs Single-Tile

The three-step mainline above explains how the final anchor kernel emerged, but
it does not fully explain the remaining long-sequence gap to FA3. That gap led
to one more causal-specific question: should the outer scheduler continue to use
the current paired causal work unit, or should it switch to a single-tile work
unit that more closely matches FA3's causal scheduler?

This is a causal-specific design choice because pairing is not arbitrary. The
current anchor kernel uses a paired outer work unit `(k, M-1-k)` to flatten the
causal triangle imbalance: each outer work item mixes one light tile from the
top of the triangle with one heavy tile from the bottom. That is a sensible
local balancing strategy, especially at short sequence lengths. But it also
makes the outer scheduler coarser. FA3 does not use this paired work unit. Its
causal scheduler issues single tiles, then relies on reverse-`m_block`
ordering, query-head-space sectioning, and dynamic persistent issuance to
recover load balance and locality.

To separate these two strategies, we built a single-tile outer-scheduler
variant that keeps the inner anchor compute body largely unchanged while
removing pairing from the outer work unit. The result is not a new mainline
kernel yet, but it is already useful as a design probe.

| Shape | Paired Anchor ms | Single-Tile ms | Single / Paired |
| --- | ---: | ---: | ---: |
| llama8b-4k | 0.2665 | 0.3428 | 128.6% |
| llama8b-8k | 0.9151 | 1.0156 | 111.0% |
| llama8b-16k | 3.4973 | 3.4788 | 99.5% |
| llama8b-32k | 15.2967 | 14.3983 | 94.1% |
| llama8b-64k | 61.8354 | 60.4092 | 97.7% |
| llama8b-128k | 254.9966 | 256.7521 | 100.7% |
| llama8b-256k | 1033.3350 | 1034.1890 | 100.1% |

This table shows a clear crossover shape. Pairing is the right outer strategy
for small shapes, where the extra scheduler freedom of single-tile does not pay
for itself. Around `16k`, the two become nearly identical. At `32k-64k`,
single-tile becomes meaningfully better. And by `128k-256k`, the single-tile
outer scheduler remains competitive but does not yet deliver a decisive
end-to-end win on its own.

The Nsight Compute data makes that last point more precise. At `64k`, `128k`,
and `256k`, the single-tile outer scheduler consistently produces a more
FA3-like memory-system signature:

- lower L2 miss rate
- lower or comparable DRAM read
- higher total L2 bytes

So single-tile is not a dead end. It really does release some scheduler freedom
and improve cache behavior. But it is also not a complete explanation by
itself. In this report, that result is best read as a new causal-specific
design lesson rather than as a replacement for the earlier three-step story:

- pairing is still the right outer strategy for short contexts
- single-tile becomes the more interesting outer strategy once context grows
- but closing the residual long-sequence gap still requires more than just
  changing scheduler granularity

This also suggests a practical dispatch intuition for future kernels. A
conservative policy would keep paired scheduling below `32k` and only consider
single-tile outer scheduling at `32k+`. An exploratory policy could already
treat `16k` as a crossover region worth benchmarking, while still keeping
paired scheduling as the safer default there.

## 7. Failed Directions And Constraints

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

## Summary

The central result is that this kernel evolution path contains one large
schedule win followed by two hardware-facing refinements. Baseline WS wins by
reorganizing information flow. Reorder wins by shrinking the memory-system
footprint. Delayed rescale wins by moving heavy register and accumulator
pressure out of the hottest consumer window.
