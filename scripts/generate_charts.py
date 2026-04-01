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

def generate_bar_comparison(op_name: str, metrics: list[str],
                            nightly: dict, output_dir: Path) -> list[Path]:
    """Generate grouped bar chart comparing metrics per config for current run."""
    bench = nightly.get("bench", {})
    op_data = bench.get("ops", {}).get(op_name, {})
    configs = op_data.get("configs", [])
    if not configs:
        return []

    # Filter to configs that have all requested metrics
    valid_configs = []
    for cfg in configs:
        if all(cfg.get(m) is not None for m in metrics):
            valid_configs.append(cfg)

    if not valid_configs:
        return []

    # Shorten config names for display
    def short_name(name: str) -> str:
        # e.g. "test_r2_small_tensor_unary[4096-dtype0]" → last part
        if "[" in name:
            return name.split("[")[-1].rstrip("]")
        parts = name.split("_")
        return "_".join(parts[-3:]) if len(parts) > 3 else name

    labels = [short_name(c["name"]) for c in valid_configs]

    # Limit to top 20 configs by tileops_latency_ms to avoid overcrowding
    if len(valid_configs) > 20:
        paired = list(zip(valid_configs, labels))
        paired.sort(key=lambda x: x[0].get("tileops_latency_ms", 0), reverse=True)
        paired = paired[:20]
        valid_configs = [p[0] for p in paired]
        labels = [p[1] for p in paired]

    import numpy as np
    x = np.arange(len(labels))
    width = 0.8 / len(metrics)

    fig, ax = plt.subplots(figsize=(max(8, len(labels) * 0.6), 5))

    for i, metric in enumerate(metrics):
        vals = [c[metric] for c in valid_configs]
        color = _METRIC_COLORS.get(metric, None)
        ax.bar(x + i * width, vals, width, label=_METRIC_LABELS.get(metric, metric),
               color=color)

    ax.set_title(f"{op_name} — TileOPs vs Baseline")
    ax.set_ylabel("Latency (ms)")
    ax.set_xticks(x + width * (len(metrics) - 1) / 2)
    ax.set_xticklabels(labels, rotation=45, ha="right")
    ax.legend()

    fig.tight_layout()
    out = output_dir / f"{op_name}_bar_comparison.png"
    fig.savefig(out, dpi=150)
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
