#!/usr/bin/env python3
"""gen_readme.py — Generate README.md by filling readme_template.md with registry data."""

import argparse
import json
from pathlib import Path

TEMPLATE_PATH = Path(__file__).parent / "readme_template.md"


# ── Helpers ──────────────────────────────────────────────────────────────────

def _bar(count: int, total: int, width: int = 15) -> str:
    if total == 0:
        return "`" + "\u2591" * width + "` 0%"
    filled = round(count / total * width)
    return f"`{'\u2588' * filled}{'\u2591' * (width - filled)}` {count}/{total}"


def _status_icon(impl: bool, tested: bool, test_failed: bool, bench_ok) -> str:
    if impl and tested and bench_ok is True:
        return "\u2705"
    if impl and tested:
        return "\U0001f7e1"
    if impl and test_failed:
        return "\u274c"
    if impl:
        return "\U0001f7e6"
    return "\u2b1c"


def _score_display(score) -> str:
    if score is None:
        return "\u2014"
    return f"{'\u2b50' * score}{'\u2606' * (5 - score)} ({score}/5)"


# ── Section builders ─────────────────────────────────────────────────────────

def _build_assessment(overall: dict) -> str:
    if not overall.get("summary"):
        return ""
    lines = [
        "## Assessment",
        "",
        f"> {overall['summary']}",
        "",
    ]
    recs = overall.get("recommendations", [])
    if recs:
        lines.append("**Recommendations:**")
        lines.append("")
        for i, r in enumerate(recs, 1):
            lines.append(f"{i}. {r}")
        lines.append("")
    return "\n".join(lines)


def _build_category(cat: dict, cat_analysis: dict, ops_registry: dict) -> str:
    name = cat["name"]
    t = cat["total_ops"]
    im = cat["impl_ops"]
    te = cat.get("tested_ops", 0)
    be = cat.get("benched_ops", 0)
    d = cat["done_ops"]

    ca = cat_analysis.get(name, {})
    fs = ca.get("func_score")
    ps = ca.get("perf_score")

    # Header with scores
    score_parts = []
    if fs is not None:
        score_parts.append(f"Func: {_score_display(fs)}")
    if ps is not None:
        score_parts.append(f"Perf: {_score_display(ps)}")
    score_text = " | " + " | ".join(score_parts) if score_parts else ""

    lines = [
        f"### {name}{score_text}",
        "",
        "| | Progress | |",
        "|:--|:---------|:--|",
        f"| Impl | {_bar(im, t)} | |",
        f"| Test | {_bar(te, t)} | |",
        f"| Bench | {_bar(be, t)} | |",
        "",
    ]

    # Claude analysis
    if ca.get("issues"):
        lines += [f"> **Issues:** {ca['issues']}", ""]
    if ca.get("evaluation"):
        lines += [f"> **Evaluation:** {ca['evaluation']}", ""]

    # Per-op table (collapsed)
    lines += [
        "<details>",
        f"<summary>{d}/{t} done - click to expand</summary>",
        "",
        "| | Operator | Test | Bench | Ratio |",
        "|:--|:---------|:----:|:-----:|------:|",
    ]

    for op_s in cat.get("ops", []):
        op_id = op_s["id"]
        op_reg = ops_registry.get(op_id, {})
        icon = _status_icon(
            op_s.get("implemented", False),
            op_s.get("tested", False),
            op_s.get("test_failed", False),
            op_s.get("bench_ok"),
        )
        ts_s = (op_reg.get("test_status") or {}).get("status", "-")
        bs_s = (op_reg.get("bench_status") or {}).get("status", "-")
        ratio = (op_reg.get("bench_status") or {}).get("ratio")
        ratio_s = f"{ratio:.2f}" if ratio is not None else "-"
        lines.append(f"| {icon} | {op_s['name']} | {ts_s} | {bs_s} | {ratio_s} |")

    lines += ["", "</details>", ""]
    return "\n".join(lines)


# ── Main ─────────────────────────────────────────────────────────────────────

def build_readme(registry: dict, analysis: dict | None, pages_url: str) -> str:
    template = TEMPLATE_PATH.read_text(encoding="utf-8")

    summary = registry.get("summary", {})
    ops = registry.get("ops", {})
    generated = registry.get("generated_at", "unknown")

    total = summary.get("total_ops", 0)
    impl = summary.get("impl_ops", 0)
    tested = summary.get("tested_ops", 0)
    benched = summary.get("benched_ops", 0)
    done = summary.get("done_ops", 0)

    # Status counts
    ts = {"passed": 0, "failed": 0, "missing": 0}
    bs = {"qualified": 0, "passed": 0, "underperforming": 0, "failed": 0, "missing": 0}
    for op in ops.values():
        t = (op.get("test_status") or {}).get("status", "missing")
        b = (op.get("bench_status") or {}).get("status", "missing")
        ts[t] = ts.get(t, 0) + 1
        bs[b] = bs.get(b, 0) + 1

    # Build sections
    cat_analysis = (analysis or {}).get("categories", {})
    overall = (analysis or {}).get("overall", {})

    assessment_section = _build_assessment(overall)
    categories_section = "\n".join(
        _build_category(cat, cat_analysis, ops)
        for cat in summary.get("categories", [])
    )

    # Fill template
    replacements = {
        "{{done}}": str(done),
        "{{total}}": str(total),
        "{{pct}}": str(done * 100 // total if total else 0),
        "{{pages_url}}": pages_url,
        "{{generated}}": generated,
        "{{impl}}": str(impl),
        "{{tested}}": str(tested),
        "{{benched}}": str(benched),
        "{{impl_bar}}": _bar(impl, total),
        "{{test_bar}}": _bar(tested, total),
        "{{bench_bar}}": _bar(benched, total),
        "{{done_bar}}": _bar(done, total),
        "{{ts_passed}}": str(ts["passed"]),
        "{{ts_failed}}": str(ts["failed"]),
        "{{ts_missing}}": str(ts["missing"]),
        "{{bs_qualified}}": str(bs.get("qualified", 0)),
        "{{bs_passed}}": str(bs.get("passed", 0)),
        "{{bs_underperforming}}": str(bs.get("underperforming", 0)),
        "{{bs_failed}}": str(bs.get("failed", 0)),
        "{{bs_missing}}": str(bs.get("missing", 0)),
        "{{assessment_section}}": assessment_section,
        "{{categories_section}}": categories_section,
    }

    result = template
    for key, value in replacements.items():
        result = result.replace(key, value)

    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate README.md from template + registry")
    parser.add_argument("--registry", required=True, help="op_registry.json path")
    parser.add_argument("--analysis", default=None, help="analysis.json path")
    parser.add_argument("--output", default="README.md", help="Output path")
    parser.add_argument("--pages-url", default="https://superanggao.github.io/TileOPs-report/nightly/")
    args = parser.parse_args()

    registry = json.loads(Path(args.registry).read_text())

    analysis = None
    if args.analysis and Path(args.analysis).exists():
        try:
            analysis = json.loads(Path(args.analysis).read_text())
        except Exception:
            pass

    readme = build_readme(registry, analysis, args.pages_url)
    Path(args.output).write_text(readme)
    print(f"README written: {args.output}")


if __name__ == "__main__":
    main()
