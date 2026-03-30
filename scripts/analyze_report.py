#!/usr/bin/env python3
"""analyze_report.py — Call Claude API to analyze nightly TileOPs results.

Reads nightly_data.json (produced by parse_results.py) and calls Claude once
to produce structured analysis.json with per-category scores and evaluations.

Usage:
    python scripts/analyze_report.py \
        --nightly-data  nightly_data.json \
        --output        analysis.json \
        [--model        claude-sonnet-4-6]

Environment variables:
    ANTHROPIC_API_KEY or ANTHROPIC_AUTH_TOKEN  — required
    ANTHROPIC_BASE_URL                        — optional
"""

import argparse
import json
import sys
from pathlib import Path

from claude_utils import (
    call_claude_json,
    get_api_config,
    require_anthropic,
)


# ---------------------------------------------------------------------------
# Format nightly_data for Claude prompt
# ---------------------------------------------------------------------------

def _format_progress(data: dict) -> str:
    """Format overall + per-category progress summary."""
    test = data.get("test", {})
    bench = data.get("bench", {})
    cats = data.get("categories", {})

    lines = [
        f"Test: {test.get('total_ops', 0)} ops, "
        f"{test.get('passed_cases', 0)}/{test.get('total_cases', 0)} cases passed, "
        f"{test.get('failed_cases', 0)} failed, {test.get('skipped_cases', 0)} skipped",
        f"Bench: {bench.get('total_ops', 0)} ops, {bench.get('total_configs', 0)} configs",
        f"Baseline alerts (ratio < 0.80): {len(data.get('baseline_alerts', []))}",
        f"Regressions: {len(data.get('regressions', []))}",
        f"Improvements: {len(data.get('improvements', []))}",
        "",
    ]

    for cat_name in sorted(cats):
        c = cats[cat_name]
        ratio_str = f", avg_ratio={c['avg_ratio']:.2f}" if c.get("avg_ratio") else ""
        lines.append(
            f"### {cat_name}: "
            f"test={c['test_passed']}/{c['test_ops']} passed, {c['test_failed']} failed | "
            f"bench={c['bench_qualified']} qualified, {c['bench_underperforming']} underperf "
            f"({c['bench_configs']} configs){ratio_str}"
        )

    return "\n".join(lines)


def _format_test_details(data: dict) -> str:
    """Format per-op test details, focusing on failures."""
    test = data.get("test", {})
    ops = test.get("ops", {})
    if not ops:
        return "No test data available.\n"

    lines = []
    # Failed ops first
    failed_ops = {k: v for k, v in ops.items() if v["failed"] > 0}
    if failed_ops:
        lines.append(f"### Failed ops ({len(failed_ops)}):")
        for name in sorted(failed_ops):
            op = failed_ops[name]
            total = op["passed"] + op["failed"] + op["skipped"]
            err_str = f", max_err={op['max_abs_err']:.2e}" if op.get("max_abs_err") else ""
            lines.append(f"  {name} [{op['category']}]: {op['failed']}/{total} failed{err_str}")
            for ft in op["failing_tests"][:3]:
                lines.append(f"    - {ft['name']}: {ft['message'][:100]}")
        lines.append("")

    # Summary of passing ops
    passed_ops = [k for k, v in ops.items() if v["failed"] == 0 and v["passed"] > 0]
    lines.append(f"### Passing ops ({len(passed_ops)}): {', '.join(sorted(passed_ops)[:20])}")
    if len(passed_ops) > 20:
        lines.append(f"  ... and {len(passed_ops) - 20} more")

    return "\n".join(lines)


def _format_bench_details(data: dict) -> str:
    """Format benchmark details + alerts + regressions."""
    bench = data.get("bench", {})
    ops = bench.get("ops", {})
    if not ops:
        return "No benchmark data available.\n"

    lines = []

    # Per-op summary with worst ratios
    lines.append("### Per-op benchmark summary:")
    for name in sorted(ops):
        op = ops[name]
        ratios = [c.get("baseline_ratio") for c in op["configs"] if c.get("baseline_ratio")]
        if ratios:
            avg = sum(ratios) / len(ratios)
            worst = min(ratios)
            lines.append(f"  {name} [{op['category']}]: {len(op['configs'])} configs, "
                         f"avg_ratio={avg:.2f}, worst={worst:.2f}")
        else:
            lines.append(f"  {name} [{op['category']}]: {len(op['configs'])} configs, no ratio data")
    lines.append("")

    # Baseline alerts
    alerts = data.get("baseline_alerts", [])
    if alerts:
        lines.append(f"### Baseline alerts ({len(alerts)} configs below 0.80 ratio):")
        for a in alerts[:15]:
            lines.append(f"  {a['op']} | {a['config']} | ratio={a['ratio']:.2f} "
                         f"| tileops={a.get('tileops_ms', '?')}ms "
                         f"| baseline={a.get('baseline_ms', '?')}ms ({a['baseline_tag']})")
        if len(alerts) > 15:
            lines.append(f"  ... and {len(alerts) - 15} more")
        lines.append("")

    # Regressions
    regs = data.get("regressions", [])
    if regs:
        lines.append(f"### Regressions ({len(regs)} vs 14-day best):")
        for r in regs[:10]:
            lines.append(f"  {r['op']} | {r['config']} | +{r['delta_pct']:.1f}% "
                         f"({r['best_ms']}ms → {r['curr_ms']}ms)")
        lines.append("")

    # Improvements
    imps = data.get("improvements", [])
    if imps:
        lines.append(f"### Improvements ({len(imps)} vs 14-day best):")
        for i in imps[:10]:
            lines.append(f"  {i['op']} | {i['config']} | {i['delta_pct']:.1f}% "
                         f"({i['best_ms']}ms → {i['curr_ms']}ms)")
        lines.append("")

    # Bench failures
    failures = bench.get("failures", [])
    if failures:
        lines.append(f"### Bench failures ({len(failures)}):")
        for f in failures[:10]:
            lines.append(f"  {f.get('op', '?')} | {f['name']}: {f['message'][:100]}")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Prompt
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = (
    "You are a senior CI/DevOps engineer analyzing nightly test results for TileOPs, "
    "a high-performance LLM operator library built on TileLang. "
    "You MUST respond with ONLY a valid JSON object. No markdown, no explanation, "
    "no text outside the JSON. The JSON must match the exact schema specified."
)


def build_prompt(progress_text: str, test_text: str, bench_text: str,
                 categories: list[str]) -> str:
    cat_list = ", ".join(categories)

    cat_json = ",\n".join(
        f'    "{c}": {{"perf_score": <1-5 or null>, "func_score": <1-5 or null>, '
        f'"issues": "<text>", "evaluation": "<text>"}}'
        for c in categories
    )

    return f"""Analyze the nightly results for TileOPs.

## Discovered Categories
{cat_list}

## Status Definitions

**Test results**: per-testcase pass/fail/skip, aggregated per op (by class name).
**Benchmark results**: per-config latency, TFLOPS, baseline_ratio (= baseline_latency / tileops_latency).
  - ratio >= 1.0 means TileOPs is faster than baseline
  - ratio >= 0.80 is "qualified" (acceptable)
  - ratio < 0.80 is "underperforming" (needs optimization)

## Overall Progress
{progress_text}

## Test Results
{test_text}

## Benchmark Results
{bench_text}

## Instructions

Score each category on TWO dimensions:

**perf_score** (performance, from benchmarks):
- 1 = <50% of baseline on average
- 2 = 50-75% of baseline
- 3 = 75-90% of baseline
- 4 = 90-100% of baseline
- 5 = >100% of baseline (exceeds)
- null = no benchmark data for this category

**func_score** (functional correctness, from tests):
- 1 = Most tests fail, fundamental issues
- 2 = Many failures, major gaps
- 3 = Mixed results, some ops broken
- 4 = Mostly passing, minor issues
- 5 = All or nearly all tests pass
- null = no test data for this category

For each category, provide:
- "perf_score": performance score 1-5 or null
- "func_score": functional score 1-5 or null
- "issues": concise description of problems (empty string if none)
- "evaluation": brief assessment and 1-2 actionable recommendations

For the overall project:
- "summary": 2-3 sentence project health assessment
- "recommendations": list of 3 top actionable items

Respond with ONLY this JSON:
{{
  "categories": {{
{cat_json}
  }},
  "overall": {{
    "summary": "<text>",
    "recommendations": ["<item1>", "<item2>", "<item3>"]
  }}
}}"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Call Claude API to analyze nightly TileOPs report")
    parser.add_argument("--nightly-data", required=True, help="Path to nightly_data.json")
    parser.add_argument("--output", required=True, help="Output path for analysis.json")
    parser.add_argument("--model", default="claude-sonnet-4-6",
                        help="Claude model ID (default: claude-sonnet-4-6)")
    args = parser.parse_args()

    api_key, base_url = get_api_config()
    if not api_key:
        print("::warning::ANTHROPIC_API_KEY / ANTHROPIC_AUTH_TOKEN not set — "
              "skipping Claude analysis.", file=sys.stderr)
        sys.exit(0)

    if require_anthropic() is None:
        sys.exit(0)

    data = json.loads(Path(args.nightly_data).read_text())
    categories = sorted(data.get("categories", {}).keys())

    if not categories:
        print("::warning::No categories found in nightly data — skipping analysis.",
              file=sys.stderr)
        sys.exit(0)

    progress_text = _format_progress(data)
    test_text = _format_test_details(data)
    bench_text = _format_bench_details(data)

    prompt = build_prompt(progress_text, test_text, bench_text, categories)
    print("Calling Claude for structured analysis ...")

    try:
        analysis = call_claude_json(
            prompt, args.model, api_key, base_url,
            system=SYSTEM_PROMPT,
            required_keys=["categories", "overall"],
            max_tokens=4096,
        )
    except Exception as exc:
        print(f"::warning::Claude analysis failed: {exc}", file=sys.stderr)
        analysis = {
            "categories": {
                c: {"perf_score": None, "func_score": None, "issues": "", "evaluation": ""}
                for c in categories
            },
            "overall": {"summary": "Analysis unavailable.", "recommendations": []},
        }

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(analysis, ensure_ascii=False, indent=2))
    print(f"Analysis written: {args.output}")


if __name__ == "__main__":
    main()
