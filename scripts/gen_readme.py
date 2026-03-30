#!/usr/bin/env python3
"""gen_readme.py — Generate README.md from nightly_data.json + analysis.json."""

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


def _build_category(cat_name: str, cat_stats: dict, cat_analysis: dict,
                    test_ops: dict, bench_ops: dict) -> str:
    ca = cat_analysis.get(cat_name, {})
    fs = ca.get("func_score")
    ps = ca.get("perf_score")

    score_parts = []
    if fs is not None:
        score_parts.append(f"Func: {_score_display(fs)}")
    if ps is not None:
        score_parts.append(f"Perf: {_score_display(ps)}")
    score_text = " | " + " | ".join(score_parts) if score_parts else ""

    t_ops = cat_stats.get("test_ops", 0)
    t_passed = cat_stats.get("test_passed", 0)
    t_failed = cat_stats.get("test_failed", 0)
    b_configs = cat_stats.get("bench_configs", 0)
    b_qualified = cat_stats.get("bench_qualified", 0)
    b_underperf = cat_stats.get("bench_underperforming", 0)
    avg_ratio = cat_stats.get("avg_ratio")

    ratio_str = f" | Avg ratio: {avg_ratio:.2f}" if avg_ratio else ""

    lines = [
        f"### {cat_name}{score_text}",
        "",
        "| Metric | Value |",
        "|:-------|------:|",
        f"| Test Ops | {t_passed}/{t_ops} passed |",
        f"| Bench Configs | {b_qualified} qualified / {b_configs} total |",
    ]
    if avg_ratio is not None:
        lines.append(f"| Avg Ratio | {avg_ratio:.2f} |")
    lines.append("")

    if ca.get("issues"):
        lines += [f"> **Issues:** {ca['issues']}", ""]
    if ca.get("evaluation"):
        lines += [f"> **Evaluation:** {ca['evaluation']}", ""]

    # Per-op table (collapsed)
    # Collect ops in this category
    cat_test = {k: v for k, v in test_ops.items() if v.get("category") == cat_name}
    cat_bench = {k: v for k, v in bench_ops.items() if v.get("category") == cat_name}
    all_ops = sorted(set(cat_test) | set(cat_bench))

    if all_ops:
        lines += [
            "<details>",
            f"<summary>{len(all_ops)} ops - click to expand</summary>",
            "",
            "| Op | Test (P/F/S) | Max Err | Bench Configs | Avg Ratio |",
            "|:---|:-------------|--------:|--------------:|----------:|",
        ]

        for op_name in all_ops:
            t = cat_test.get(op_name, {})
            b = cat_bench.get(op_name, {})

            if t:
                test_str = f"{t.get('passed', 0)}/{t.get('failed', 0)}/{t.get('skipped', 0)}"
                err = t.get("max_abs_err")
                err_str = f"{err:.2e}" if err else "\u2014"
            else:
                test_str = "\u2014"
                err_str = "\u2014"

            configs = b.get("configs", [])
            n_configs = len(configs)
            ratios = [c.get("baseline_ratio") for c in configs if c.get("baseline_ratio")]
            avg_r = sum(ratios) / len(ratios) if ratios else None
            ratio_s = f"{avg_r:.2f}" if avg_r else "\u2014"

            lines.append(f"| {op_name} | {test_str} | {err_str} | {n_configs} | {ratio_s} |")

        lines += ["", "</details>", ""]

    return "\n".join(lines)


# ── Main ─────────────────────────────────────────────────────────────────────

def build_readme(data: dict, analysis: dict | None, pages_url: str) -> str:
    template = TEMPLATE_PATH.read_text(encoding="utf-8")

    test = data.get("test", {})
    bench = data.get("bench", {})
    categories = data.get("categories", {})

    cat_analysis = (analysis or {}).get("categories", {})
    overall = (analysis or {}).get("overall", {})

    assessment_section = _build_assessment(overall)
    categories_section = "\n".join(
        _build_category(name, categories[name], cat_analysis,
                        test.get("ops", {}), bench.get("ops", {}))
        for name in sorted(categories)
    )

    replacements = {
        "{{test_passed}}": str(test.get("passed_cases", 0)),
        "{{test_total}}": str(test.get("total_cases", 0)),
        "{{test_failed}}": str(test.get("failed_cases", 0)),
        "{{num_ops}}": str(test.get("total_ops", 0)),
        "{{num_categories}}": str(len(categories)),
        "{{bench_configs}}": str(bench.get("total_configs", 0)),
        "{{bench_ops}}": str(bench.get("total_ops", 0)),
        "{{baseline_alerts}}": str(len(data.get("baseline_alerts", []))),
        "{{pages_url}}": pages_url,
        "{{generated}}": data.get("meta", {}).get("generated_at", "unknown"),
        "{{assessment_section}}": assessment_section,
        "{{categories_section}}": categories_section,
    }

    result = template
    for key, value in replacements.items():
        result = result.replace(key, value)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate README.md from nightly data")
    parser.add_argument("--nightly-data", required=True, help="nightly_data.json path")
    parser.add_argument("--analysis", default=None, help="analysis.json path")
    parser.add_argument("--output", default="README.md", help="Output path")
    parser.add_argument("--pages-url",
                        default="https://superanggao.github.io/TileOPs-report-static/nightly/")
    args = parser.parse_args()

    data = json.loads(Path(args.nightly_data).read_text())

    analysis = None
    if args.analysis and Path(args.analysis).exists():
        try:
            analysis = json.loads(Path(args.analysis).read_text())
        except Exception:
            pass

    readme = build_readme(data, analysis, args.pages_url)
    Path(args.output).write_text(readme)
    print(f"README written: {args.output}")


if __name__ == "__main__":
    main()
