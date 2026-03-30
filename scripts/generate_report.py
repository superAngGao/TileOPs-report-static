#!/usr/bin/env python3
"""generate_report.py — Generate self-contained HTML report from nightly_data.json + analysis.json.

Usage:
    python scripts/generate_report.py \
        --date           20260330_220000 \
        --commit         abc123 \
        --report-dir     _gh_pages/nightly/20260330_220000 \
        --html-output    report.html \
        --nightly-data   nightly_data.json \
        --analysis-json  analysis.json
"""

import argparse
import json
import os
from datetime import datetime
from pathlib import Path


def _esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ──────────────────────────────────────────────────────────────────────────────
# CSS
# ──────────────────────────────────────────────────────────────────────────────

_CSS = """
:root{--green:#22c55e;--yellow:#f59e0b;--red:#ef4444;--blue:#3b82f6;--purple:#8b5cf6;
      --bg:#f9fafb;--card:#fff;--border:#e5e7eb;--text:#111827;--muted:#6b7280}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:system-ui,sans-serif;background:var(--bg);color:var(--text);padding:1.5rem;max-width:1100px;margin:0 auto}
h1{font-size:1.5rem;font-weight:700;margin-bottom:.25rem}
h2{font-size:1.15rem;font-weight:600;margin:1.5rem 0 .75rem;border-bottom:2px solid var(--border);padding-bottom:.25rem}
h3{font-size:.95rem;font-weight:600;margin:.75rem 0 .25rem}
.meta{color:var(--muted);font-size:.82rem;margin-bottom:1.5rem}
.card{background:var(--card);border:1px solid var(--border);border-radius:.5rem;padding:1rem 1.25rem;margin-bottom:1rem}
/* Overall grid */
.overall-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(100px,1fr));gap:.5rem;margin:.75rem 0}
.stat-box{background:var(--card);border:1px solid var(--border);border-radius:.375rem;padding:.6rem;text-align:center}
.stat-box .num{font-size:1.4rem;font-weight:700;line-height:1}
.stat-box .lbl{font-size:.72rem;color:var(--muted);margin-top:.15rem}
/* Progress bars */
.bar-wrap{background:#e5e7eb;border-radius:9999px;height:.75rem;overflow:hidden;margin:.25rem 0;box-shadow:inset 0 1px 2px rgba(0,0,0,.08)}
.bar-fill{height:100%;border-radius:9999px;transition:width .6s ease;min-width:2px}
.bar-test{background:linear-gradient(90deg,#4ade80,#22c55e)}
.bar-bench{background:linear-gradient(90deg,#a78bfa,#8b5cf6)}
/* Stacked bars */
.stacked-bar{display:flex;height:100%;border-radius:9999px;overflow:hidden}
.stacked-bar .seg{height:100%;transition:width .6s ease}
.stacked-bar .seg:first-child{border-radius:9999px 0 0 9999px}
.stacked-bar .seg:last-child{border-radius:0 9999px 9999px 0}
.stacked-bar .seg:only-child{border-radius:9999px}
.seg-passed{background:linear-gradient(90deg,#4ade80,#22c55e)}.seg-failed{background:linear-gradient(90deg,#f87171,#ef4444)}
.seg-qualified{background:linear-gradient(90deg,#a78bfa,#7c3aed)}.seg-underperforming{background:linear-gradient(90deg,#fbbf24,#f59e0b)}
.bar-row{display:flex;align-items:center;gap:.5rem;font-size:.82rem;margin:.2rem 0}
.bar-label{width:50px;color:var(--muted);flex-shrink:0;font-weight:500}
.bar-container{flex:1;min-width:60px}
.bar-count{width:140px;text-align:right;color:var(--muted);flex-shrink:0;font-size:.75rem}
/* Category card */
.cat-card{display:grid;grid-template-columns:1fr auto;gap:.75rem;padding:.75rem 0;border-bottom:1px solid var(--border)}
.cat-card:last-child{border-bottom:none}
.cat-bars{min-width:0}
.cat-scores{display:flex;gap:.4rem;align-items:flex-start;flex-shrink:0}
.score-badge{display:inline-flex;flex-direction:column;align-items:center;padding:.3rem .5rem;
             border-radius:.375rem;font-size:.72rem;font-weight:600;min-width:44px}
.score-badge .val{font-size:1.1rem;line-height:1}
.score-perf{background:#ede9fe;color:#5b21b6}.score-func{background:#dcfce7;color:#166534}
.score-null{background:#f3f4f6;color:#9ca3af}
/* Tables */
.data-table{width:100%;border-collapse:collapse;font-size:.82rem;margin:.5rem 0}
.data-table th{text-align:left;padding:.4rem .5rem;background:#f9fafb;border-bottom:2px solid var(--border);font-weight:600;font-size:.75rem;color:var(--muted)}
.data-table td{padding:.35rem .5rem;border-bottom:1px solid var(--border);vertical-align:middle}
.data-table tr:hover{background:#f0f9ff}
.badge{display:inline-block;padding:.1rem .4rem;border-radius:.25rem;font-size:.72rem;font-weight:600}
.badge-red{background:#fee2e2;color:#991b1b}.badge-yellow{background:#fef3c7;color:#92400e}
.badge-green{background:#dcfce7;color:#166534}.badge-blue{background:#dbeafe;color:#1e40af}
/* Detail section */
.detail-item{margin:.75rem 0;padding:.75rem;background:#fafafa;border-radius:.375rem;border:1px solid var(--border)}
.detail-item h3{margin:0 0 .35rem;font-size:.88rem}
.detail-issues{color:var(--red);font-size:.85rem;margin:.25rem 0}
.detail-eval{font-size:.85rem;color:var(--text);margin:.25rem 0}
/* Assessment */
.rec-list{margin:.5rem 0;padding-left:1.25rem}
.rec-list li{margin:.25rem 0;font-size:.88rem}
/* Mobile */
@media(max-width:600px){
  body{padding:.75rem}.card{padding:.75rem}h1{font-size:1.25rem}
  .overall-grid{grid-template-columns:repeat(3,1fr);gap:.4rem}
  .stat-box .num{font-size:1.1rem}
  .cat-card{grid-template-columns:1fr;gap:.5rem}
  .cat-scores{justify-content:flex-start}
  .data-table{font-size:.75rem}
}
"""


# ──────────────────────────────────────────────────────────────────────────────
# HTML helpers
# ──────────────────────────────────────────────────────────────────────────────

def _stacked_bar(segments: list[tuple[float, str]], total: int) -> str:
    if total == 0:
        return '<div class="bar-wrap"><div class="stacked-bar"></div></div>'
    inner = ""
    for count, cls in segments:
        pct = count / total * 100 if count else 0
        if pct > 0:
            inner += f'<div class="seg {cls}" style="width:{pct:.1f}%"></div>'
    return f'<div class="bar-wrap"><div class="stacked-bar">{inner}</div></div>'


def _score_badge(value, label: str, css_class: str) -> str:
    if value is None:
        return f'<div class="score-badge score-null"><span class="val">—</span>{label}</div>'
    return f'<div class="score-badge {css_class}"><span class="val">{value}</span>{label}</div>'


def _ratio_badge(ratio: float | None) -> str:
    if ratio is None:
        return '<span class="badge badge-blue">—</span>'
    if ratio >= 1.0:
        return f'<span class="badge badge-green">{ratio:.0%}</span>'
    if ratio >= 0.80:
        return f'<span class="badge badge-yellow">{ratio:.0%}</span>'
    return f'<span class="badge badge-red">{ratio:.0%}</span>'


# ──────────────────────────────────────────────────────────────────────────────
# HTML builder
# ──────────────────────────────────────────────────────────────────────────────

def build_html(args, data: dict, analysis: dict | None) -> str:
    date_str = args.date
    commit = args.commit
    gen_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if analysis is None:
        analysis = {"categories": {}, "overall": {
            "summary": "No analysis available.", "recommendations": []}}

    test = data.get("test", {})
    bench = data.get("bench", {})
    categories = data.get("categories", {})

    parts = [
        "<!DOCTYPE html><html lang='zh-CN'><head>",
        "<meta charset='UTF-8'>",
        "<meta name='viewport' content='width=device-width,initial-scale=1'>",
        f"<title>TileOPs Report · {_esc(date_str)}</title>",
        f"<style>{_CSS}</style>",
        "</head><body>",
    ]

    # ── Header ────────────────────────────────────────────────────────────
    parts += [
        "<h1>TileOPs Nightly Report</h1>",
        f"<p class='meta'>Date: {_esc(date_str)} &nbsp;|&nbsp; "
        f"Commit: <code>{_esc(commit)}</code> &nbsp;|&nbsp; "
        f"Generated: {gen_time}</p>",
    ]

    # ── Overall Summary ───────────────────────────────────────────────────
    t_ops = test.get("total_ops", 0)
    t_cases = test.get("total_cases", 0)
    t_passed = test.get("passed_cases", 0)
    t_failed = test.get("failed_cases", 0)
    b_ops = bench.get("total_ops", 0)
    b_configs = bench.get("total_configs", 0)
    n_alerts = len(data.get("baseline_alerts", []))
    n_regs = len(data.get("regressions", []))
    n_imps = len(data.get("improvements", []))

    health = "pass" if t_failed == 0 and n_regs == 0 and not bench.get("failures") else "warn"

    parts += [
        "<div class='card'>",
        "<h2 style='margin-top:0'>Overall Summary</h2>",
        "<div class='overall-grid'>",
        f"<div class='stat-box'><div class='num'>{t_ops}</div><div class='lbl'>Test Ops</div></div>",
        f"<div class='stat-box'><div class='num' style='color:var(--green)'>{t_passed}/{t_cases}</div><div class='lbl'>Cases Pass</div></div>",
        f"<div class='stat-box'><div class='num' style='color:var(--purple)'>{b_ops}</div><div class='lbl'>Bench Ops</div></div>",
        f"<div class='stat-box'><div class='num'>{b_configs}</div><div class='lbl'>Bench Configs</div></div>",
        f"<div class='stat-box'><div class='num' style='color:var(--{'red' if n_alerts else 'green'})'>{n_alerts}</div><div class='lbl'>Alerts</div></div>",
        f"<div class='stat-box'><div class='num'>{len(categories)}</div><div class='lbl'>Categories</div></div>",
        "</div>",
    ]

    # Test bar: passed/failed/skipped
    if t_cases > 0:
        test_bar = _stacked_bar([
            (t_passed, "seg-passed"),
            (t_failed, "seg-failed"),
        ], t_cases)
        parts.append(
            f'<div class="bar-row"><span class="bar-label">Test</span>'
            f'<div class="bar-container">{test_bar}</div>'
            f'<span class="bar-count">{t_passed}✓ {t_failed}✗ {test.get("skipped_cases", 0)}—</span></div>'
        )

    # Bench bar: qualified/underperforming
    total_q = sum(c.get("bench_qualified", 0) for c in categories.values())
    total_u = sum(c.get("bench_underperforming", 0) for c in categories.values())
    total_bf = len(bench.get("failures", []))
    if b_configs > 0 or total_bf > 0:
        bench_bar = _stacked_bar([
            (total_q, "seg-qualified"),
            (total_u, "seg-underperforming"),
            (total_bf, "seg-failed"),
        ], total_q + total_u + total_bf)
        parts.append(
            f'<div class="bar-row"><span class="bar-label">Bench</span>'
            f'<div class="bar-container">{bench_bar}</div>'
            f'<span class="bar-count">{total_q}✓ {total_u}△ {total_bf}✗</span></div>'
        )

    parts.append("</div>")  # card

    # ── Category Progress ─────────────────────────────────────────────────
    parts += ["<div class='card'>", "<h2 style='margin-top:0'>Category Progress</h2>"]

    cat_analysis = analysis.get("categories", {})
    for cat_name in sorted(categories):
        c = categories[cat_name]
        ca = cat_analysis.get(cat_name, {})

        parts.append('<div class="cat-card"><div class="cat-bars">')
        ratio_str = f" (avg ratio: {c['avg_ratio']:.0%})" if c.get("avg_ratio") else ""
        parts.append(f'<h3 style="margin-bottom:.35rem">{_esc(cat_name)}{_esc(ratio_str)}</h3>')

        # Test bar
        t_total = c["test_ops"]
        if t_total > 0:
            test_bar = _stacked_bar([
                (c["test_passed"], "seg-passed"),
                (c["test_failed"], "seg-failed"),
            ], t_total)
            parts.append(
                f'<div class="bar-row"><span class="bar-label">Test</span>'
                f'<div class="bar-container">{test_bar}</div>'
                f'<span class="bar-count">{c["test_passed"]}✓ {c["test_failed"]}✗ / {t_total} ops</span></div>'
            )

        # Bench bar
        b_total = c["bench_configs"]
        if b_total > 0:
            bench_bar = _stacked_bar([
                (c["bench_qualified"], "seg-qualified"),
                (c["bench_underperforming"], "seg-underperforming"),
            ], b_total)
            parts.append(
                f'<div class="bar-row"><span class="bar-label">Bench</span>'
                f'<div class="bar-container">{bench_bar}</div>'
                f'<span class="bar-count">{c["bench_qualified"]}✓ {c["bench_underperforming"]}△ / {b_total} cfgs</span></div>'
            )

        parts.append('</div><div class="cat-scores">')
        parts.append(_score_badge(ca.get("perf_score"), "Perf", "score-perf"))
        parts.append(_score_badge(ca.get("func_score"), "Func", "score-func"))
        parts.append('</div></div>')  # cat-scores, cat-card

    parts.append("</div>")  # card

    # ── Test Failures ─────────────────────────────────────────────────────
    failed_ops = {k: v for k, v in test.get("ops", {}).items() if v.get("failed", 0) > 0}
    if failed_ops:
        parts += ["<div class='card'>", f"<h2 style='margin-top:0'>Test Failures ({len(failed_ops)} ops)</h2>"]
        parts.append('<table class="data-table"><thead><tr>')
        parts.append('<th>Op</th><th>Category</th><th>Pass/Fail/Skip</th><th>Max Err</th><th>Failing Tests</th>')
        parts.append('</tr></thead><tbody>')
        for name in sorted(failed_ops):
            op = failed_ops[name]
            err_str = f"{op['max_abs_err']:.2e}" if op.get("max_abs_err") else "—"
            tests_str = ", ".join(t["name"] for t in op["failing_tests"][:3])
            if len(op["failing_tests"]) > 3:
                tests_str += f" (+{len(op['failing_tests']) - 3})"
            parts.append(
                f'<tr><td><strong>{_esc(name)}</strong></td>'
                f'<td>{_esc(op.get("category", ""))}</td>'
                f'<td>{op["passed"]}/{op["failed"]}/{op["skipped"]}</td>'
                f'<td>{err_str}</td>'
                f'<td style="font-size:.75rem">{_esc(tests_str)}</td></tr>'
            )
        parts.append('</tbody></table></div>')

    # ── Benchmark Failures ────────────────────────────────────────────────
    bench_failures = bench.get("failures", [])
    if bench_failures:
        parts += ["<div class='card'>", f"<h2 style='margin-top:0'>Benchmark Failures ({len(bench_failures)})</h2>"]
        parts.append('<table class="data-table"><thead><tr><th>Test</th><th>Error</th></tr></thead><tbody>')
        for f in bench_failures:
            msg = _esc(f.get("message", "")[:120])
            parts.append(f'<tr><td>{_esc(f["name"])}</td><td style="font-size:.75rem">{msg}</td></tr>')
        parts.append('</tbody></table></div>')

    # ── Baseline Alerts ───────────────────────────────────────────────────
    alerts = data.get("baseline_alerts", [])
    if alerts:
        parts += ["<div class='card'>", f"<h2 style='margin-top:0'>Baseline Alerts ({len(alerts)} configs &lt; 80%)</h2>"]
        parts.append('<table class="data-table"><thead><tr>')
        parts.append('<th>Op</th><th>Config</th><th>TileOPs (ms)</th><th>Baseline (ms)</th><th>Ratio</th><th>Via</th>')
        parts.append('</tr></thead><tbody>')
        for a in alerts[:50]:
            parts.append(
                f'<tr><td><strong>{_esc(a["op"])}</strong></td>'
                f'<td style="font-size:.75rem">{_esc(a["config"])}</td>'
                f'<td>{a.get("tileops_ms", 0):.4f}</td>'
                f'<td>{a.get("baseline_ms", 0):.4f}</td>'
                f'<td>{_ratio_badge(a.get("ratio"))}</td>'
                f'<td>{_esc(str(a.get("baseline_tag", "")))}</td></tr>'
            )
        parts.append('</tbody></table></div>')

    # ── Regressions ───────────────────────────────────────────────────────
    regressions = data.get("regressions", [])
    if regressions:
        parts += ["<div class='card'>", f"<h2 style='margin-top:0'>Performance Regressions ({len(regressions)})</h2>"]
        parts.append('<table class="data-table"><thead><tr>')
        parts.append('<th>Op</th><th>Config</th><th>Best (ms)</th><th>Current (ms)</th><th>Delta</th><th>TFLOPS</th>')
        parts.append('</tr></thead><tbody>')
        for r in regressions:
            tflops_str = f"{r['tflops']:.2f}" if r.get("tflops") else "—"
            parts.append(
                f'<tr><td><strong>{_esc(r["op"])}</strong></td>'
                f'<td style="font-size:.75rem">{_esc(r["config"])}</td>'
                f'<td>{r["best_ms"]:.4f}</td><td>{r["curr_ms"]:.4f}</td>'
                f'<td><span class="badge badge-red">+{r["delta_pct"]:.1f}%</span></td>'
                f'<td>{tflops_str}</td></tr>'
            )
        parts.append('</tbody></table></div>')

    # ── Improvements ──────────────────────────────────────────────────────
    improvements = data.get("improvements", [])
    if improvements:
        parts += ["<div class='card'>", f"<h2 style='margin-top:0'>Performance Improvements ({len(improvements)})</h2>"]
        parts.append('<table class="data-table"><thead><tr>')
        parts.append('<th>Op</th><th>Config</th><th>Prev Best (ms)</th><th>Current (ms)</th><th>Delta</th><th>TFLOPS</th>')
        parts.append('</tr></thead><tbody>')
        for r in improvements:
            tflops_str = f"{r['tflops']:.2f}" if r.get("tflops") else "—"
            parts.append(
                f'<tr><td><strong>{_esc(r["op"])}</strong></td>'
                f'<td style="font-size:.75rem">{_esc(r["config"])}</td>'
                f'<td>{r["best_ms"]:.4f}</td><td>{r["curr_ms"]:.4f}</td>'
                f'<td><span class="badge badge-green">{r["delta_pct"]:.1f}%</span></td>'
                f'<td>{tflops_str}</td></tr>'
            )
        parts.append('</tbody></table></div>')

    # ── Category Analysis ─────────────────────────────────────────────────
    if any(ca.get("issues") or ca.get("evaluation") for ca in cat_analysis.values()):
        parts += ["<div class='card'>", "<h2 style='margin-top:0'>Category Analysis</h2>"]
        for cat_name in sorted(cat_analysis):
            ca = cat_analysis[cat_name]
            issues = ca.get("issues", "")
            evaluation = ca.get("evaluation", "")
            if not issues and not evaluation:
                continue
            parts.append('<div class="detail-item">')
            parts.append(f'<h3>{_esc(cat_name)}</h3>')
            if issues:
                parts.append(f'<div class="detail-issues"><strong>Issues:</strong> {_esc(issues)}</div>')
            if evaluation:
                parts.append(f'<div class="detail-eval"><strong>Evaluation:</strong> {_esc(evaluation)}</div>')
            parts.append('</div>')
        parts.append("</div>")

    # ── Overall Assessment ────────────────────────────────────────────────
    overall = analysis.get("overall", {})
    summary = overall.get("summary", "")
    recs = overall.get("recommendations", [])

    parts += ["<div class='card'>", "<h2 style='margin-top:0'>Overall Assessment</h2>"]
    if summary:
        parts.append(f"<p style='font-size:.88rem;line-height:1.6'>{_esc(summary)}</p>")
    if recs:
        parts.append("<h3>Recommendations</h3><ol class='rec-list'>")
        for r in recs:
            parts.append(f"<li>{_esc(r)}</li>")
        parts.append("</ol>")
    parts.append("</div>")

    # ── Footer ────────────────────────────────────────────────────────────
    parts += [
        "<p style='text-align:center;color:var(--muted);font-size:.72rem;margin-top:1.5rem'>",
        "Generated by Claude &mdash; review for accuracy before acting on recommendations.",
        "</p>",
        "</body></html>",
    ]

    return "\n".join(parts)


# ──────────────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Generate TileOPs nightly HTML report")
    parser.add_argument("--date", required=True, help="Run date timestamp")
    parser.add_argument("--commit", required=True, help="Git commit hash")
    parser.add_argument("--report-dir", required=True, help="Report directory")
    parser.add_argument("--html-output", required=True, help="HTML output path")
    parser.add_argument("--nightly-data", required=True, help="nightly_data.json path")
    parser.add_argument("--analysis-json", default=None, help="analysis.json path")
    args = parser.parse_args()

    data = json.loads(Path(args.nightly_data).read_text())

    analysis = None
    if args.analysis_json and os.path.exists(args.analysis_json):
        try:
            analysis = json.loads(Path(args.analysis_json).read_text())
        except Exception:
            pass

    html = build_html(args, data, analysis)

    # Write summary.json for gen_index.py
    test = data.get("test", {})
    bench = data.get("bench", {})
    summary = {
        "test_total": test.get("total_cases", 0),
        "test_passed": test.get("passed_cases", 0),
        "test_failed": test.get("failed_cases", 0),
        "test_ops": test.get("total_ops", 0),
        "bench_configs": bench.get("total_configs", 0),
        "bench_ops": bench.get("total_ops", 0),
        "baseline_alerts": len(data.get("baseline_alerts", [])),
        "categories": len(data.get("categories", {})),
    }
    summary_path = Path(args.report_dir) / "summary.json"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2))

    Path(args.html_output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.html_output).write_text(html)
    print(f"HTML report: {args.html_output}")


if __name__ == "__main__":
    main()
