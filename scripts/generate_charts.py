#!/usr/bin/env python3
"""generate_charts.py — Generate performance charts from perf_history and nightly data.

Reads chart_config.yaml to determine which operators and chart types to produce,
then generates PNG images.

Chart types:
  - trend:          Line chart of metrics averaged across configs over time.
  - bar_comparison: Grouped bar chart comparing tileops vs baseline per config
                    for the current run.

Usage:
    python scripts/generate_charts.py \
        --config       scripts/chart_config.yaml \
        --perf-history perf_history.json \
        --nightly-data nightly_data.json \
        --output-dir   charts/
"""

import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import yaml

# ---------------------------------------------------------------------------
# Styling
# ---------------------------------------------------------------------------

plt.rcParams.update({
    "figure.facecolor": "white",
    "axes.grid": True,
    "grid.alpha": 0.3,
    "font.size": 10,
})

_METRIC_LABELS = {
    "tileops_latency_ms": "TileOPs Latency (ms)",
    "tileops_tflops": "TileOPs TFLOPS",
    "baseline_ratio": "Baseline Ratio",
    "baseline_latency_ms": "Baseline Latency (ms)",
    "baseline_tflops": "Baseline TFLOPS",
}

_METRIC_COLORS = {
    "tileops_latency_ms": "#2563eb",
    "tileops_tflops": "#16a34a",
    "baseline_ratio": "#d97706",
    "baseline_latency_ms": "#dc2626",
    "baseline_tflops": "#7c3aed",
}


# ---------------------------------------------------------------------------
# Trend chart
# ---------------------------------------------------------------------------

def _avg_metric(run: dict, op_name: str, metric: str) -> float | None:
    """Average a metric across all configs for an op in a single run."""
    op_data = run.get("ops", {}).get(op_name, {})
    if not op_data:
        return None
    values = []
    for cfg in op_data.values():
        v = cfg.get(metric)
        if v is not None:
            values.append(v)
    return sum(values) / len(values) if values else None


def generate_trend(op_name: str, metrics: list[str],
                   history: dict, output_dir: Path) -> list[Path]:
    """Generate trend line charts. One chart per metric."""
    runs = history.get("runs", [])
    if not runs:
        return []

    paths = []
    for metric in metrics:
        dates = []
        values = []
        for run in runs:
            avg = _avg_metric(run, op_name, metric)
            if avg is not None:
                # Use short date for x label: 20260329_222236 → 03-29
                raw = run.get("date", "")
                if len(raw) >= 8:
                    label = f"{raw[4:6]}-{raw[6:8]}"
                else:
                    label = raw
                dates.append(label)
                values.append(avg)

        if not values:
            continue

        fig, ax = plt.subplots(figsize=(8, 4))
        color = _METRIC_COLORS.get(metric, "#333333")
        ax.plot(dates, values, marker="o", color=color, linewidth=2, markersize=5)
        ax.set_title(f"{op_name} — {_METRIC_LABELS.get(metric, metric)}")
        ax.set_xlabel("Date")
        ax.set_ylabel(_METRIC_LABELS.get(metric, metric))

        # Rotate x labels if many points
        if len(dates) > 7:
            plt.xticks(rotation=45, ha="right")

        fig.tight_layout()
        out = output_dir / f"{op_name}_trend_{metric}.png"
        fig.savefig(out, dpi=150)
        plt.close(fig)
        paths.append(out)

    return paths


# ---------------------------------------------------------------------------
# Bar comparison chart
# ---------------------------------------------------------------------------

# Distinct colors for different baseline tags
_BASELINE_TAG_COLORS = [
    "#dc2626", "#7c3aed", "#0891b2", "#ca8a04", "#be185d",
    "#059669", "#9333ea", "#e11d48", "#0d9488", "#c2410c",
]

_TILEOPS_COLOR = "#2563eb"


def _short_config_name(name: str) -> str:
    """Shorten a config name for display."""
    if "[" in name:
        return name.split("[")[-1].rstrip("]")
    parts = name.split("_")
    return "_".join(parts[-3:]) if len(parts) > 3 else name


def _collect_baselines(cfg: dict, suffix: str = "latency_ms") -> list[tuple[str, float]]:
    """Collect all baseline (tag, value) pairs from a config entry.

    *suffix* selects the metric: "latency_ms" or "tflops".
    Includes the primary baseline and any tag-prefixed baselines.
    """
    baselines = []
    primary_tag = cfg.get("baseline_tag")
    primary_val = cfg.get(f"baseline_{suffix}")
    seen_tags = set()
    if primary_tag and primary_val is not None:
        baselines.append((primary_tag, primary_val))
        seen_tags.add(primary_tag)

    for tag in cfg.get("baseline_tags", []):
        if tag in seen_tags:
            continue
        val = cfg.get(f"{tag}_{suffix}")
        if val is not None:
            baselines.append((tag, val))
            seen_tags.add(tag)

    return baselines


# Fixed bar width — calibrated for 3-bar layout, used everywhere for consistency.
_BAR_WIDTH = 0.6
_MAX_SLOTS = 3  # always reserve space for 3 bars so widths look uniform


def _draw_bar_subplots(op_name: str, valid: list[dict], all_tags: list[str],
                       tag_color: dict, suffix: str, ylabel: str,
                       title_suffix: str, output_dir: Path) -> Path | None:
    """Shared logic for bar subplot charts (latency or tflops)."""
    n = len(valid)
    ncols = min(4, n)
    nrows = (n + ncols - 1) // ncols

    fig, axes = plt.subplots(nrows, ncols,
                             figsize=(4.5 * ncols, 3.5 * nrows),
                             squeeze=False)

    for idx, cfg in enumerate(valid):
        row, col = divmod(idx, ncols)
        ax = axes[row][col]

        tileops_key = f"tileops_{suffix}"
        tileops_val = cfg.get(tileops_key)
        if tileops_val is None:
            ax.set_visible(False)
            continue

        baselines = _collect_baselines(cfg, suffix)
        labels = ["TileOPs"] + [tag for tag, _ in baselines]
        values = [tileops_val] + [v for _, v in baselines]
        colors = [_TILEOPS_COLOR] + [tag_color[tag] for tag, _ in baselines]

        bars = ax.bar(range(len(labels)), values, color=colors, width=_BAR_WIDTH)

        # Fix x-axis to always show _MAX_SLOTS positions for uniform bar width
        ax.set_xlim(-0.5, _MAX_SLOTS - 0.5)
        ax.set_xticks(range(len(labels)))
        ax.set_xticklabels(labels, fontsize=7, rotation=30, ha="right")
        ax.set_title(_short_config_name(cfg["name"]), fontsize=8)
        ax.set_ylabel(ylabel, fontsize=8)
        ax.tick_params(axis="y", labelsize=7)

        for bar in bars:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, h,
                    f"{h:.3g}", ha="center", va="bottom", fontsize=7)

    for idx in range(n, nrows * ncols):
        row, col = divmod(idx, ncols)
        axes[row][col].set_visible(False)

    fig.suptitle(f"{op_name} — {title_suffix}", fontsize=12, y=1.01)
    fig.tight_layout()
    out = output_dir / f"{op_name}_bar_{suffix}.png"
    fig.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return out


def generate_bar_comparison(op_name: str, metrics: list[str],
                            nightly: dict, output_dir: Path) -> list[Path]:
    """Generate subplot bar charts: latency and tflops, one subplot per config.

    Each config gets its own subplot.  Each baseline gets its own colored bar.
    Bar width is fixed to match the 3-bar layout.
    """
    bench = nightly.get("bench", {})
    op_data = bench.get("ops", {}).get(op_name, {})
    configs = op_data.get("configs", [])
    if not configs:
        return []

    # Keep configs that have tileops latency and at least one baseline
    valid = []
    for c in configs:
        if c.get("tileops_latency_ms") is not None and _collect_baselines(c):
            valid.append(c)
    if not valid:
        return []

    # Consistent coloring across all configs
    all_tags = sorted({tag for c in valid
                       for tag, _ in _collect_baselines(c, "latency_ms")
                                   + _collect_baselines(c, "tflops")})
    tag_color = {tag: _BASELINE_TAG_COLORS[i % len(_BASELINE_TAG_COLORS)]
                 for i, tag in enumerate(all_tags)}

    paths = []

    # Latency chart
    out = _draw_bar_subplots(op_name, valid, all_tags, tag_color,
                             "latency_ms", "ms", "Latency Comparison", output_dir)
    if out:
        paths.append(out)

    # TFLOPS chart
    valid_tflops = [c for c in valid if c.get("tileops_tflops") is not None]
    if valid_tflops:
        out = _draw_bar_subplots(op_name, valid_tflops, all_tags, tag_color,
                                 "tflops", "TFLOPS", "TFLOPS Comparison", output_dir)
        if out:
            paths.append(out)

    return paths


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Generate performance charts")
    parser.add_argument("--config", required=True, help="chart_config.yaml path")
    parser.add_argument("--perf-history", required=True, help="perf_history.json path")
    parser.add_argument("--nightly-data", required=True, help="nightly_data.json path")
    parser.add_argument("--output-dir", required=True, help="Directory for chart PNGs")
    args = parser.parse_args()

    config = yaml.safe_load(Path(args.config).read_text())
    history = json.loads(Path(args.perf_history).read_text()) if Path(args.perf_history).exists() else {"runs": []}
    nightly = json.loads(Path(args.nightly_data).read_text())

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    all_charts = []
    for op in config.get("operators", []):
        op_name = op["name"]
        for chart in op.get("charts", []):
            chart_type = chart["type"]
            metrics = chart.get("metrics", [])

            if chart_type == "trend":
                paths = generate_trend(op_name, metrics, history, output_dir)
            elif chart_type == "bar_comparison":
                paths = generate_bar_comparison(op_name, metrics, nightly, output_dir)
            else:
                print(f"Unknown chart type: {chart_type}")
                continue
            all_charts.extend(paths)

    print(f"Generated {len(all_charts)} charts in {output_dir}/")
    for p in all_charts:
        print(f"  {p.name}")


if __name__ == "__main__":
    main()
