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


def generate_bar_comparison(op_name: str, metrics: list[str],
                            nightly: dict, output_dir: Path) -> list[Path]:
    """Generate subplot bar chart: one subplot per config, tileops vs baseline.

    Each config gets its own subplot so different latency scales don't squash
    smaller values.  Baseline bars are colored by baseline_tag.
    """
    bench = nightly.get("bench", {})
    op_data = bench.get("ops", {}).get(op_name, {})
    configs = op_data.get("configs", [])
    if not configs:
        return []

    # Keep configs that have both tileops and baseline latency
    valid = [c for c in configs
             if c.get("tileops_latency_ms") is not None
             and c.get("baseline_latency_ms") is not None]
    if not valid:
        return []

    # Assign a color to each unique baseline_tag
    tags = sorted({c.get("baseline_tag", "baseline") for c in valid})
    tag_color = {tag: _BASELINE_TAG_COLORS[i % len(_BASELINE_TAG_COLORS)]
                 for i, tag in enumerate(tags)}

    # Layout: up to 4 columns
    n = len(valid)
    ncols = min(4, n)
    nrows = (n + ncols - 1) // ncols

    fig, axes = plt.subplots(nrows, ncols,
                             figsize=(4 * ncols, 3.5 * nrows),
                             squeeze=False)

    for idx, cfg in enumerate(valid):
        row, col = divmod(idx, ncols)
        ax = axes[row][col]

        tileops_ms = cfg["tileops_latency_ms"]
        baseline_ms = cfg["baseline_latency_ms"]
        tag = cfg.get("baseline_tag", "baseline")

        bars = ax.bar(
            [0, 1],
            [tileops_ms, baseline_ms],
            color=[_TILEOPS_COLOR, tag_color[tag]],
            width=0.6,
        )
        ax.set_xticks([0, 1])
        ax.set_xticklabels(["TileOPs", tag], fontsize=8)
        ax.set_title(_short_config_name(cfg["name"]), fontsize=8)
        ax.set_ylabel("ms", fontsize=8)
        ax.tick_params(axis="y", labelsize=7)

        # Show value on top of each bar
        for bar in bars:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, h,
                    f"{h:.3g}", ha="center", va="bottom", fontsize=7)

    # Hide unused subplots
    for idx in range(n, nrows * ncols):
        row, col = divmod(idx, ncols)
        axes[row][col].set_visible(False)

    fig.suptitle(f"{op_name} — TileOPs vs Baseline", fontsize=12, y=1.01)
    fig.tight_layout()
    out = output_dir / f"{op_name}_bar_comparison.png"
    fig.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return [out]


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
