#!/usr/bin/env python3
"""update_perf_history.py — Append current run's bench data to perf_history.json.

Reads nightly_data.json (produced by parse_results.py) and appends a compact
run record to perf_history.json, which lives on the gh-data orphan branch.

Usage:
    python scripts/update_perf_history.py \
        --nightly-data  nightly_data.json \
        --perf-history  path/to/perf_history.json
"""

import argparse
import json
from pathlib import Path

# Fields to keep per config (drop verbose fields like config name, variant)
_KEEP_FIELDS = (
    "tileops_latency_ms",
    "tileops_tflops",
    "tileops_bandwidth_tbs",
    "baseline_latency_ms",
    "baseline_tflops",
    "baseline_ratio",
    "baseline_tag",
)


def extract_run(nightly: dict) -> dict:
    """Build a compact run record from nightly_data.json."""
    meta = nightly.get("meta", {})
    bench = nightly.get("bench", {})

    ops: dict[str, dict] = {}
    for op_name, op_data in bench.get("ops", {}).items():
        configs: dict[str, dict] = {}
        for cfg in op_data.get("configs", []):
            cfg_name = cfg.get("name", "")
            if not cfg_name:
                continue
            entry = {}
            for key in _KEEP_FIELDS:
                if key in cfg:
                    entry[key] = cfg[key]
            if entry:
                configs[cfg_name] = entry
        if configs:
            ops[op_name] = configs

    return {
        "date": meta.get("date", ""),
        "commit": meta.get("commit", ""),
        "ops": ops,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Append bench data to perf_history.json")
    parser.add_argument("--nightly-data", required=True,
                        help="Path to nightly_data.json")
    parser.add_argument("--perf-history", required=True,
                        help="Path to perf_history.json (will be created if missing)")
    args = parser.parse_args()

    # Load nightly data
    nightly = json.loads(Path(args.nightly_data).read_text())
    run = extract_run(nightly)

    if not run["ops"]:
        print("No bench data found in nightly_data.json — skipping.")
        return

    # Load or init history
    hist_path = Path(args.perf_history)
    if hist_path.exists():
        history = json.loads(hist_path.read_text())
    else:
        history = {"runs": []}

    # Dedup: skip if same date+commit already recorded
    for existing in history["runs"]:
        if existing.get("date") == run["date"] and existing.get("commit") == run["commit"]:
            print(f"Run {run['date']} ({run['commit'][:8]}) already in history — skipping.")
            return

    history["runs"].append(run)

    hist_path.parent.mkdir(parents=True, exist_ok=True)
    hist_path.write_text(json.dumps(history, ensure_ascii=False, indent=2) + "\n")

    print(f"Appended run {run['date']} ({run['commit'][:8]}): "
          f"{len(run['ops'])} ops")


if __name__ == "__main__":
    main()
