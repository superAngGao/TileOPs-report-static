#!/usr/bin/env python3
"""generate_report.py — Generate self-contained HTML report from op_registry.json + analysis.json.

Usage:
    python generate_report.py \
        --date          20260318_220000 \
        --commit        abc123 \
        --report-dir    _gh_pages/nightly/20260318_220000 \
        --html-output   report.html \
        --registry      op_registry.json \
        --analysis-json analysis.json
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
/* Overall progress */
.overall-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(100px,1fr));gap:.5rem;margin:.75rem 0}
.stat-box{background:var(--card);border:1px solid var(--border);border-radius:.375rem;padding:.6rem;text-align:center}
.stat-box .num{font-size:1.4rem;font-weight:700;line-height:1}
.stat-box .lbl{font-size:.72rem;color:var(--muted);margin-top:.15rem}
/* Progress bars */
.bar-wrap{background:#e5e7eb;border-radius:9999px;height:.75rem;overflow:hidden;margin:.25rem 0;box-shadow:inset 0 1px 2px rgba(0,0,0,.08)}
.bar-fill{height:100%;border-radius:9999px;transition:width .6s ease;min-width:2px}
.bar-impl{background:linear-gradient(90deg,#60a5fa,#3b82f6)}
.bar-test{background:linear-gradient(90deg,#4ade80,#22c55e)}
.bar-bench{background:linear-gradient(90deg,#a78bfa,#8b5cf6)}
/* Stacked bar segments */
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
.bar-count{width:120px;text-align:right;color:var(--muted);flex-shrink:0;font-size:.75rem}
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
/* Detail section */
.detail-item{margin:.75rem 0;padding:.75rem;background:#fafafa;border-radius:.375rem;border:1px solid var(--border)}
.detail-item h3{margin:0 0 .35rem;font-size:.88rem}
.detail-issues{color:var(--red);font-size:.85rem;margin:.25rem 0}
.detail-eval{font-size:.85rem;color:var(--text);margin:.25rem 0}
/* Overall assessment */
.rec-list{margin:.5rem 0;padding-left:1.25rem}
.rec-list li{margin:.25rem 0;font-size:.88rem}
/* Mobile */
@media(max-width:600px){
  body{padding:.75rem}
  .card{padding:.75rem}
  h1{font-size:1.25rem}
  .overall-grid{grid-template-columns:repeat(3,1fr);gap:.4rem}
  .stat-box .num{font-size:1.1rem}
  .bar-wrap{height:1rem}
  .bar-row{gap:.35rem;font-size:.8rem;margin:.3rem 0}
  .bar-label{width:42px;font-size:.75rem}
  .bar-count{width:105px;font-size:.68rem}
  .cat-card{grid-template-columns:1fr;gap:.5rem}
  .cat-scores{justify-content:flex-start}
  .score-badge{padding:.2rem .4rem}
  .score-badge .val{font-size:1rem}
  .detail-issues,.detail-eval{font-size:.82rem}
}
"""


# ──────────────────────────────────────────────────────────────────────────────
# HTML builders
# ──────────────────────────────────────────────────────────────────────────────

def _bar_html(pct: float, css_class: str) -> str:
    return (
        f'<div class="bar-wrap">'
        f'<div class="bar-fill {css_class}" style="width:{pct:.1f}%"></div>'
        f'</div>'
    )


def _score_badge(value, label: str, css_class: str) -> str:
    if value is None:
        return f'<div class="score-badge score-null"><span class="val">—</span>{label}</div>'
    return f'<div class="score-badge {css_class}"><span class="val">{value}</span>{label}</div>'


def _stacked_bar(segments: list[tuple[float, str]], total: int) -> str:
    """Render a stacked progress bar. segments: [(count, css_class), ...]."""
    if total == 0:
        return '<div class="bar-wrap"><div class="stacked-bar"></div></div>'
    inner = ""
    for count, cls in segments:
        pct = count / total * 100 if count else 0
        if pct > 0:
            inner += f'<div class="seg {cls}" style="width:{pct:.1f}%"></div>'
    return f'<div class="bar-wrap"><div class="stacked-bar">{inner}</div></div>'


def _count_status(registry_ops: dict, cat_name: str) -> dict:
    """Count test/bench status for ops in a given category from registry."""
    test_counts = {"passed": 0, "failed": 0, "missing": 0}
    bench_counts = {"qualified": 0, "passed": 0, "underperforming": 0, "failed": 0, "missing": 0}
    for op in registry_ops.values():
        if op.get("category") != cat_name:
            continue
        ts = op.get("test_status", {}).get("status", "missing")
        if ts in test_counts:
            test_counts[ts] += 1
        else:
            test_counts["missing"] += 1
        bs = op.get("bench_status", {}).get("status", "missing")
        if bs in bench_counts:
            bench_counts[bs] += 1
        else:
            bench_counts["missing"] += 1
    return {"test": test_counts, "bench": bench_counts}


def build_html(args, prog: dict | None, analysis: dict | None, registry_ops: dict | None = None) -> str:
    date_str = args.date
    commit   = args.commit
    gen_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if analysis is None:
        analysis = {"categories": {}, "overall": {"summary": "No analysis available.", "recommendations": []}}

    parts = [
        "<!DOCTYPE html><html lang='zh-CN'><head>",
        "<meta charset='UTF-8'>",
        "<meta name='viewport' content='width=device-width,initial-scale=1'>",
        f"<title>TileOPs Report · {_esc(date_str)}</title>",
        f"<style>{_CSS}</style>",
        "</head><body>",
    ]

    # ── Section 1: Header ────────────────────────────────────────────────────
    parts += [
        "<h1>TileOPs Nightly Report</h1>",
        f"<p class='meta'>Date: {_esc(date_str)} &nbsp;|&nbsp; "
        f"Commit: <code>{_esc(commit)}</code> &nbsp;|&nbsp; "
        f"Generated: {gen_time}</p>",
    ]

    # ── Section 2: Overall progress ──────────────────────────────────────────
    if prog:
        total   = prog["total_ops"]
        impl    = prog["impl_ops"]
        tested  = prog["tested_ops"]
        benched = prog.get("benched_ops", 0)
        done    = prog["done_ops"]
        pct     = done / total * 100 if total else 0

        # Aggregate test/bench status counts from registry
        all_test = {"passed": 0, "failed": 0, "missing": 0}
        all_bench = {"qualified": 0, "passed": 0, "underperforming": 0, "failed": 0, "missing": 0}
        if registry_ops:
            for op in registry_ops.values():
                ts = op.get("test_status", {}).get("status", "missing")
                all_test[ts] = all_test.get(ts, 0) + 1
                bs = op.get("bench_status", {}).get("status", "missing")
                all_bench[bs] = all_bench.get(bs, 0) + 1

        parts += [
            "<div class='card'>",
            "<h2 style='margin-top:0'>Overall Progress</h2>",
            "<div class='overall-grid'>",
            f"<div class='stat-box'><div class='num'>{total}</div><div class='lbl'>Total Ops</div></div>",
            f"<div class='stat-box'><div class='num' style='color:var(--blue)'>{impl}</div><div class='lbl'>Implemented</div></div>",
            f"<div class='stat-box'><div class='num' style='color:var(--green)'>{tested}</div><div class='lbl'>Tests Pass</div></div>",
            f"<div class='stat-box'><div class='num' style='color:var(--purple)'>{benched}</div><div class='lbl'>Bench Pass</div></div>",
            f"<div class='stat-box'><div class='num' style='font-size:1.1rem'>{done}/{total}</div><div class='lbl'>Done ({pct:.0f}%)</div></div>",
            "</div>",
            # Overall 3-bar: Impl is simple, Test/Bench are stacked
            "<div style='margin-top:.5rem'>",
        ]
        impl_pct = impl / total * 100 if total else 0
        parts.append(
            f'<div class="bar-row"><span class="bar-label">Impl</span>'
            f'<div class="bar-container">{_bar_html(impl_pct, "bar-impl")}</div>'
            f'<span class="bar-count">{impl}/{total}</span></div>'
        )
        if registry_ops:
            # Test stacked bar: passed(green) + failed(red), rest is gray background
            test_bar = _stacked_bar([
                (all_test["passed"], "seg-passed"),
                (all_test["failed"], "seg-failed"),
            ], total)
            test_label = f'{all_test["passed"]}✓ {all_test["failed"]}✗ {all_test["missing"]}—'
            parts.append(
                f'<div class="bar-row"><span class="bar-label">Test</span>'
                f'<div class="bar-container">{test_bar}</div>'
                f'<span class="bar-count">{test_label}</span></div>'
            )
            # Bench stacked bar: qualified+passed(purple) + underperforming(yellow) + failed(red)
            bench_ok = all_bench["qualified"] + all_bench["passed"]
            bench_bar = _stacked_bar([
                (bench_ok, "seg-qualified"),
                (all_bench["underperforming"], "seg-underperforming"),
                (all_bench["failed"], "seg-failed"),
            ], total)
            bench_label = f'{bench_ok}✓ {all_bench["underperforming"]}△ {all_bench["failed"]}✗ {all_bench["missing"]}—'
            parts.append(
                f'<div class="bar-row"><span class="bar-label">Bench</span>'
                f'<div class="bar-container">{bench_bar}</div>'
                f'<span class="bar-count">{bench_label}</span></div>'
            )
        else:
            # Fallback: simple bars when registry not available
            test_pct = tested / total * 100 if total else 0
            bench_pct = benched / total * 100 if total else 0
            for label, p, cls, count in [
                ("Test",  test_pct,  "bar-test",  f"{tested}/{total}"),
                ("Bench", bench_pct, "bar-bench", f"{benched}/{total}"),
            ]:
                parts.append(
                    f'<div class="bar-row"><span class="bar-label">{label}</span>'
                    f'<div class="bar-container">{_bar_html(p, cls)}</div>'
                    f'<span class="bar-count">{count}</span></div>'
                )
        parts += ["</div>", "</div>"]

    # ── Section 3: Per-category progress + scores ────────────────────────────
    parts += ["<div class='card'>", "<h2 style='margin-top:0'>Category Progress</h2>"]

    categories = prog.get("categories", []) if prog else []
    cat_analysis = analysis.get("categories", {})

    for cat in categories:
        name  = cat["name"]
        t     = cat["total_ops"]
        im    = cat["impl_ops"]
        ca    = cat_analysis.get(name, {})
        ps    = ca.get("perf_score")
        fs    = ca.get("func_score")

        impl_pct = im / t * 100 if t else 0

        # Get per-category status counts from registry
        cat_status = _count_status(registry_ops, name) if registry_ops else None

        parts.append('<div class="cat-card">')
        parts.append('<div class="cat-bars">')
        parts.append(f'<h3 style="margin-bottom:.35rem">{_esc(name)}</h3>')

        # Impl bar (always simple)
        parts.append(
            f'<div class="bar-row"><span class="bar-label">Impl</span>'
            f'<div class="bar-container">{_bar_html(impl_pct, "bar-impl")}</div>'
            f'<span class="bar-count">{im}/{t}</span></div>'
        )

        if cat_status:
            tc = cat_status["test"]
            test_bar = _stacked_bar([
                (tc["passed"], "seg-passed"),
                (tc["failed"], "seg-failed"),
            ], t)
            parts.append(
                f'<div class="bar-row"><span class="bar-label">Test</span>'
                f'<div class="bar-container">{test_bar}</div>'
                f'<span class="bar-count">{tc["passed"]}✓ {tc["failed"]}✗ {tc["missing"]}—</span></div>'
            )
            bc = cat_status["bench"]
            bc_ok = bc["qualified"] + bc["passed"]
            bench_bar = _stacked_bar([
                (bc_ok, "seg-qualified"),
                (bc["underperforming"], "seg-underperforming"),
                (bc["failed"], "seg-failed"),
            ], t)
            parts.append(
                f'<div class="bar-row"><span class="bar-label">Bench</span>'
                f'<div class="bar-container">{bench_bar}</div>'
                f'<span class="bar-count">{bc_ok}✓ {bc["underperforming"]}△ {bc["failed"]}✗ {bc["missing"]}—</span></div>'
            )
        else:
            te = cat.get("tested_ops", 0)
            be = cat.get("benched_ops", 0)
            test_pct  = te / t * 100 if t else 0
            bench_pct = be / t * 100 if t else 0
            for label, p, cls, count in [
                ("Test",  test_pct,  "bar-test",  f"{te}/{t}"),
                ("Bench", bench_pct, "bar-bench", f"{be}/{t}"),
            ]:
                parts.append(
                    f'<div class="bar-row"><span class="bar-label">{label}</span>'
                    f'<div class="bar-container">{_bar_html(p, cls)}</div>'
                    f'<span class="bar-count">{count}</span></div>'
                )
        parts.append('</div>')  # cat-bars
        parts.append('<div class="cat-scores">')
        parts.append(_score_badge(ps, "Perf", "score-perf"))
        parts.append(_score_badge(fs, "Func", "score-func"))
        parts.append('</div>')  # cat-scores
        parts.append('</div>')  # cat-card

    parts.append("</div>")  # card

    # ── Section 4: Per-category issues & evaluation ──────────────────────────
    parts += ["<div class='card'>", "<h2 style='margin-top:0'>Category Analysis</h2>"]

    for cat in categories:
        name = cat["name"]
        ca   = cat_analysis.get(name, {})
        issues = ca.get("issues", "")
        evaluation = ca.get("evaluation", "")

        if not issues and not evaluation:
            continue

        parts.append('<div class="detail-item">')
        parts.append(f'<h3>{_esc(name)}</h3>')
        if issues:
            parts.append(f'<div class="detail-issues"><strong>Issues:</strong> {_esc(issues)}</div>')
        if evaluation:
            parts.append(f'<div class="detail-eval"><strong>Evaluation:</strong> {_esc(evaluation)}</div>')
        parts.append('</div>')

    parts.append("</div>")  # card

    # ── Section 5: Overall assessment ────────────────────────────────────────
    overall = analysis.get("overall", {})
    summary = overall.get("summary", "")
    recs    = overall.get("recommendations", [])

    parts += ["<div class='card'>", "<h2 style='margin-top:0'>Overall Assessment</h2>"]
    if summary:
        parts.append(f"<p style='font-size:.88rem;line-height:1.6'>{_esc(summary)}</p>")
    if recs:
        parts.append("<h3>Recommendations</h3>")
        parts.append("<ol class='rec-list'>")
        for r in recs:
            parts.append(f"<li>{_esc(r)}</li>")
        parts.append("</ol>")
    parts.append("</div>")

    # ── Footer ───────────────────────────────────────────────────────────────
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
    parser.add_argument("--date",          required=True, help="Run date timestamp")
    parser.add_argument("--commit",        required=True, help="Git commit hash")
    parser.add_argument("--report-dir",    required=True, help="Report directory")
    parser.add_argument("--html-output",   required=True, help="HTML output path")
    parser.add_argument("--analysis-json", default=None,  help="analysis.json path")
    parser.add_argument("--registry",      required=True, help="op_registry.json path")
    args = parser.parse_args()

    # Load op_registry.json
    reg = None
    registry_ops = None
    prog = None
    try:
        reg = json.loads(Path(args.registry).read_text())
        registry_ops = reg.get("ops")
        prog = reg.get("summary")
    except Exception:
        pass

    # Load analysis.json
    analysis = None
    if args.analysis_json and os.path.exists(args.analysis_json):
        try:
            analysis = json.loads(Path(args.analysis_json).read_text())
        except Exception:
            pass

    html = build_html(args, prog, analysis, registry_ops)

    # Write summary.json for gen_index.py
    if prog:
        summary_path = Path(args.report_dir) / "summary.json"
        summary_path.write_text(json.dumps(prog, ensure_ascii=False, indent=2))
    Path(args.html_output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.html_output).write_text(html)
    print(f"HTML report: {args.html_output}")


if __name__ == "__main__":
    main()
