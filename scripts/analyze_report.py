#!/usr/bin/env python3
"""analyze_report.py — Call Claude API to analyze nightly TileOPs report.

Single-call analysis: reads op_registry.json and calls Claude once to produce
structured analysis.json with per-category scores and evaluations.

Environment variables:
  ANTHROPIC_API_KEY or ANTHROPIC_AUTH_TOKEN  — required
  ANTHROPIC_BASE_URL                         — optional, for custom proxy
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

# Category names (must match op_manifest.json)
_CATEGORIES = [
    "Elementwise", "Reduce", "Norm", "Conv & Pooling", "GEMM",
    "Quantize", "Sampling", "Flash Attention", "MoE",
    "Linear Attention", "SSM",
]


# ─────────────────────────────────────────────────────────────────────────────
# Data loaders
# ─────────────────────────────────────────────────────────────────────────────

def _load_progress_detail(registry: dict) -> str:
    """Format per-category, per-op status from registry for the prompt."""
    summary = registry.get("summary")
    ops = registry.get("ops", {})
    if not summary:
        return "No progress data available.\n"

    lines = [
        f"Total ops: {summary['total_ops']} | "
        f"Implemented: {summary['impl_ops']} | "
        f"Tested: {summary['tested_ops']} | "
        f"Benched: {summary.get('benched_ops', 0)} | "
        f"Done: {summary['done_ops']}",
        "",
    ]
    for cat in summary.get("categories", []):
        t = cat["total_ops"]
        im = cat["impl_ops"]
        te = cat.get("tested_ops", 0)
        be = cat.get("benched_ops", 0)
        d = cat["done_ops"]
        lines.append(f"### {cat['name']} ({im}/{t} impl, {te}/{t} tested, {be}/{t} benched, {d}/{t} done)")
        for op in cat.get("ops", []):
            impl_s = "Y" if op.get("implemented") else "N"

            # Get detailed status from registry ops
            reg = ops.get(op.get("id", ""), {})
            ts = reg.get("test_status", {})
            bs = reg.get("bench_status", {})

            test_s = ts.get("status", "missing")
            bench_s = bs.get("status", "missing")
            if bs.get("ratio") is not None:
                bench_s += f"({bs['ratio']:.2f})"

            lines.append(f"  {op['name']} [{op.get('sub','')}]: impl={impl_s} test={test_s} bench={bench_s}")
        lines.append("")
    return "\n".join(lines)


def _load_test_summary(registry: dict) -> str:
    """Derive test summary from registry per-op test_status."""
    ops = registry.get("ops", {})
    if not ops:
        return "No test data available.\n"

    cat_data: dict[str, dict] = {}
    total_passed = total_failed = 0

    for op in ops.values():
        cat_name = op.get("category", "Other")
        ts = op.get("test_status", {})
        status = ts.get("status", "missing")

        cd = cat_data.setdefault(cat_name, {"passed": 0, "failed": 0, "missing": 0, "errors": []})
        if status == "passed":
            cd["passed"] += 1
            total_passed += 1
        elif status == "failed":
            cd["failed"] += 1
            total_failed += 1
            for e in ts.get("errors", [])[:3]:
                cd["errors"].append(f"{op.get('name', '?')}: {e[:200]}")
        else:
            cd["missing"] += 1

    lines = [f"Total ops: {total_passed} passed, {total_failed} failed", ""]
    for cn in sorted(cat_data.keys()):
        cd = cat_data[cn]
        lines.append(f"### {cn}: {cd['passed']} passed, {cd['failed']} failed, {cd['missing']} missing")
        for e in cd["errors"][:5]:
            lines.append(f"  - {e}")
        lines.append("")
    return "\n".join(lines)


def _load_bench_log(registry: dict) -> str:
    """Derive bench summary from registry per-op bench_status."""
    ops = registry.get("ops", {})
    if not ops:
        return "No benchmark data available.\n"

    cat_data: dict[str, dict] = {}

    for op in ops.values():
        cat_name = op.get("category", "Other")
        bs = op.get("bench_status", {})
        status = bs.get("status", "missing")
        ratio = bs.get("ratio")

        cd = cat_data.setdefault(cat_name, {"qualified": 0, "underperforming": 0, "failed": 0, "missing": 0, "ratios": []})
        cd[status] = cd.get(status, 0) + 1
        if ratio is not None:
            cd["ratios"].append((op.get("name", "?"), ratio))

    lines = []
    for cn in sorted(cat_data.keys()):
        cd = cat_data[cn]
        lines.append(f"### {cn}: {cd['qualified']} qualified, {cd['underperforming']} underperforming, {cd['failed']} failed, {cd['missing']} missing")
        for name, r in cd["ratios"]:
            lines.append(f"  {name}: ratio={r:.2f}")
        lines.append("")
    return "\n".join(lines) if lines else "No benchmark data available.\n"


# ─────────────────────────────────────────────────────────────────────────────
# Prompt + System
# ─────────────────────────────────────────────────────────────────────────────

SYSTEM_PROMPT = (
    "You are a senior CI/DevOps engineer analyzing nightly test results for TileOPs, "
    "a high-performance LLM operator library built on TileLang. "
    "You MUST respond with ONLY a valid JSON object. No markdown, no explanation, "
    "no text outside the JSON. The JSON must match the exact schema specified."
)

_CATEGORY_JSON_TEMPLATE = ",\n".join(
    f'    "{c}": {{"perf_score": <1-5 or null>, "func_score": <1-5 or null>, '
    f'"test_summary": {{"passed": N, "failed": N, "missing": N}}, '
    f'"bench_summary": {{"qualified": N, "underperforming": N, "failed": N, "missing": N}}, '
    f'"issues": "<text>", "evaluation": "<text>"}}'
    for c in _CATEGORIES
)


def build_prompt(progress_text: str, test_text: str, bench_text: str) -> str:
    cat_list = ", ".join(_CATEGORIES)
    return f"""Analyze the nightly results for TileOPs.

## Operator Categories
{cat_list}

## Status Definitions

Each operator has a **test status** and a **bench status**:

**Test status** (3 levels):
- `passed`  — all mapped test functions pass
- `failed`  — mapped tests exist but some fail, or test results not found in XML
- `missing` — no test mapping exists for this operator

**Bench status** (4 levels, threshold: ratio >= 0.80 = qualified):
- `qualified(ratio)`       — benchmark exists and performance >= 80% of baseline
- `underperforming(ratio)` — benchmark exists but performance < 80% of baseline
- `failed`                 — benchmark mapping exists but no results in log
- `missing`                — no benchmark mapping exists for this operator

## Implementation Progress
{progress_text}

## Test Results
{test_text}

## Benchmark Log
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

For each category, also count the operators in each status:
- "test_summary":  {{"passed": N, "failed": N, "missing": N}}
- "bench_summary": {{"qualified": N, "underperforming": N, "failed": N, "missing": N}}

For each category, provide:
- "perf_score": performance score 1-5 or null
- "func_score": functional score 1-5 or null
- "test_summary": count of operators in each test status
- "bench_summary": count of operators in each bench status
- "issues": concise description of problems (empty string if none)
- "evaluation": brief assessment of current status and 1-2 actionable recommendations

For the overall project, provide:
- "summary": 2-3 sentence project health assessment
- "recommendations": list of 3 top actionable items

Respond with ONLY this JSON (no other text):
{{
  "categories": {{
{_CATEGORY_JSON_TEMPLATE}
  }},
  "overall": {{
    "summary": "<text>",
    "recommendations": ["<item1>", "<item2>", "<item3>"]
  }}
}}"""


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Call Claude API to analyze nightly TileOPs report, output analysis.json"
    )
    parser.add_argument("--registry", required=True, help="Path to op_registry.json")
    parser.add_argument("--output",   required=True, help="Output path for analysis.json")
    parser.add_argument(
        "--model",
        default="claude-sonnet-4-6",
        help="Claude model ID (default: claude-sonnet-4-6)",
    )
    args = parser.parse_args()

    api_key, base_url = get_api_config()

    if not api_key:
        print(
            "::warning::ANTHROPIC_API_KEY / ANTHROPIC_AUTH_TOKEN not set — "
            "skipping Claude analysis.",
            file=sys.stderr,
        )
        sys.exit(0)

    if require_anthropic() is None:
        sys.exit(0)

    # Load registry
    registry = json.loads(Path(args.registry).read_text())

    # Derive all text from registry
    progress_text = _load_progress_detail(registry)
    test_text = _load_test_summary(registry)
    bench_text = _load_bench_log(registry)

    # Single Claude call → structured JSON
    prompt = build_prompt(progress_text, test_text, bench_text)
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
        # Fallback: empty structure
        analysis = {
            "categories": {c: {"perf_score": None, "func_score": None, "issues": "", "evaluation": ""} for c in _CATEGORIES},
            "overall": {"summary": "Analysis unavailable.", "recommendations": []},
        }

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(analysis, ensure_ascii=False, indent=2))
    print(f"Analysis written: {args.output}")


if __name__ == "__main__":
    main()
