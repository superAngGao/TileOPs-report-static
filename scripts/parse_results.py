#!/usr/bin/env python3
"""parse_results.py — Parse upstream JUnit XML artifacts into nightly_data.json.

Reads test_results.xml and bench_results.xml produced by TileOPs nightly CI,
auto-discovers ops from embedded JUnit properties, derives categories from
op_module paths, and outputs a self-contained nightly_data.json.

Usage:
    python scripts/parse_results.py \
        --test-xml       test_results.xml \
        --bench-xml      bench_results.xml \
        [--perf-history  perf_history.json] \
        --date           20260330_220000 \
        --commit         abc123 \
        --output         nightly_data.json
"""

import argparse
import json
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

BASELINE_ALERT_THRESHOLD = 0.80
REGRESSION_THRESHOLD = 0.10  # 10% latency increase
REGRESSION_ABS_MIN = 0.01   # ignore < 0.01 ms
NOISE_FLOOR = 0.05          # ignore <= 5% fluctuations

# Subdirectory → category name (for modules like tileops.ops.norm.rms_norm)
_SUBDIR_CATEGORIES = {
    "norm": "Norm",
    "moe": "MoE",
    "reduction": "Reduction",
}

# Keyword → category name (for flat modules like tileops.ops.gemm)
_KEYWORD_CATEGORIES = {
    "Conv": ["conv", "pooling"],
    "GEMM": ["gemm", "grouped_gemm"],
    "Attention": ["mha", "gqa", "sliding_window", "attention"],
    "DeepSeek": ["deepseek", "mla", "dsa", "nsa"],
    "SSM": ["deltanet", "gated_deltanet", "ssd", "gla", "gated_mamba"],
    "MHC": ["mhc"],
    "Transform": ["rope", "fft"],
    "Dropout": ["dropout"],
    "Elementwise": ["elementwise", "binary", "unary"],
    "Quantize": ["quantize", "fp8"],
}


# ---------------------------------------------------------------------------
# Category derivation
# ---------------------------------------------------------------------------

def derive_category(op_module: str | None) -> str:
    """Derive a human-readable category from an op_module path.

    Examples:
        'tileops.ops.norm.rms_norm'  → 'Norm'
        'tileops.ops.gemm'           → 'GEMM'
        'tileops.ops.mha_fwd'        → 'Attention'
    """
    if not op_module:
        return "Other"

    # Strip common prefix
    path = op_module
    for prefix in ("tileops.ops.", "tileops.kernels."):
        if path.startswith(prefix):
            path = path[len(prefix):]
            break

    parts = path.split(".")

    # Subdirectory-based: tileops.ops.norm.rms_norm → parts = ["norm", "rms_norm"]
    if len(parts) > 1 and parts[0] in _SUBDIR_CATEGORIES:
        return _SUBDIR_CATEGORIES[parts[0]]

    # Flat module: keyword matching on the first part
    name = parts[0]
    for category, keywords in _KEYWORD_CATEGORIES.items():
        for kw in keywords:
            if name == kw or name.startswith(kw + "_") or name.startswith(kw):
                return category

    return "Other"


# ---------------------------------------------------------------------------
# JUnit XML parsing
# ---------------------------------------------------------------------------

def _get_properties(tc: ET.Element) -> dict[str, str]:
    """Extract <property> elements from a testcase."""
    props = {}
    for ps in tc.iter("properties"):
        for p in ps.iter("property"):
            props[p.attrib.get("name", "")] = p.attrib.get("value", "")
    return props


def _get_outcome(tc: ET.Element) -> str:
    if tc.find("skipped") is not None:
        return "skipped"
    if tc.find("failure") is not None or tc.find("error") is not None:
        return "failed"
    return "passed"


def _failure_message(tc: ET.Element) -> str | None:
    for tag in ("failure", "error"):
        el = tc.find(tag)
        if el is not None:
            return el.attrib.get("message", "")
    return None


def parse_test_xml(path: str) -> dict:
    """Parse test_results.xml → per-op test data."""
    ops: dict[str, dict] = {}
    total = passed = failed = skipped = 0

    try:
        tree = ET.parse(path)
    except (ET.ParseError, FileNotFoundError) as e:
        print(f"::warning::Cannot parse test XML {path}: {e}", file=sys.stderr)
        return {"total_cases": 0, "passed_cases": 0, "failed_cases": 0,
                "skipped_cases": 0, "ops": {}}

    for tc in tree.iter("testcase"):
        props = _get_properties(tc)
        outcome = _get_outcome(tc)
        total += 1
        if outcome == "passed":
            passed += 1
        elif outcome == "failed":
            failed += 1
        else:
            skipped += 1

        op_name = props.get("op", "")
        if not op_name:
            continue

        if op_name not in ops:
            ops[op_name] = {
                "module": props.get("op_module", ""),
                "category": derive_category(props.get("op_module")),
                "passed": 0,
                "failed": 0,
                "skipped": 0,
                "max_abs_err": None,
                "failing_tests": [],
            }

        d = ops[op_name]
        d[outcome] += 1

        # Track max absolute error
        err_str = props.get("max_abs_err")
        if err_str:
            try:
                err = float(err_str)
                if d["max_abs_err"] is None or err > d["max_abs_err"]:
                    d["max_abs_err"] = err
            except ValueError:
                pass

        if outcome == "failed":
            name = tc.attrib.get("name", "")
            msg = _failure_message(tc) or ""
            d["failing_tests"].append({"name": name, "message": msg[:200]})

    return {
        "total_cases": total,
        "passed_cases": passed,
        "failed_cases": failed,
        "skipped_cases": skipped,
        "ops": ops,
    }


def parse_bench_xml(path: str) -> dict:
    """Parse bench_results.xml → per-op bench data + failures."""
    ops: dict[str, dict] = {}
    failures: list[dict] = []
    total_configs = 0

    try:
        tree = ET.parse(path)
    except (ET.ParseError, FileNotFoundError) as e:
        print(f"::warning::Cannot parse bench XML {path}: {e}", file=sys.stderr)
        return {"total_configs": 0, "ops": {}, "failures": []}

    for tc in tree.iter("testcase"):
        props = _get_properties(tc)
        outcome = _get_outcome(tc)

        op_name = props.get("op", "")

        if outcome == "failed":
            failures.append({
                "name": tc.attrib.get("name", ""),
                "op": op_name or None,
                "message": (_failure_message(tc) or "")[:200],
            })
            continue

        if outcome == "skipped" or not op_name:
            continue

        total_configs += 1

        if op_name not in ops:
            ops[op_name] = {
                "module": props.get("op_module", ""),
                "category": derive_category(props.get("op_module")),
                "configs": [],
            }

        config: dict = {"name": tc.attrib.get("name", "")}
        for key in ("tileops_latency_ms", "tileops_tflops", "tileops_bandwidth_tbs",
                     "baseline_latency_ms", "baseline_tflops", "baseline_ratio"):
            if key in props:
                try:
                    config[key] = float(props[key])
                except ValueError:
                    pass

        for key in ("tileops_variant", "baseline_tag"):
            if key in props:
                config[key] = props[key]

        # Extract tag-prefixed baseline fields ({tag}_latency_ms, etc.)
        # These are written by upstream conftest for all baselines beyond the first.
        _TAG_SUFFIXES = ("_latency_ms", "_tflops", "_ratio")
        seen_tags = set()
        for pname, pval in props.items():
            for suffix in _TAG_SUFFIXES:
                if pname.endswith(suffix):
                    tag = pname[:-len(suffix)]
                    if tag in ("tileops", "baseline"):
                        break  # already handled above
                    try:
                        config[pname] = float(pval)
                    except ValueError:
                        pass
                    seen_tags.add(tag)
                    break
        if seen_tags:
            config["baseline_tags"] = sorted(seen_tags)

        ops[op_name]["configs"].append(config)

    return {"total_configs": total_configs, "ops": ops, "failures": failures}


# ---------------------------------------------------------------------------
# Category aggregation
# ---------------------------------------------------------------------------

def compute_categories(test_data: dict, bench_data: dict) -> dict:
    """Aggregate per-category statistics."""
    cats: dict[str, dict] = defaultdict(lambda: {
        "test_ops": 0, "test_passed": 0, "test_failed": 0,
        "bench_ops": 0, "bench_configs": 0,
        "bench_qualified": 0, "bench_underperforming": 0, "bench_failed": 0,
        "ratios": [],
    })

    for op_name, op in test_data.get("ops", {}).items():
        cat = op["category"]
        cats[cat]["test_ops"] += 1
        if op["failed"] == 0 and op["passed"] > 0:
            cats[cat]["test_passed"] += 1
        elif op["failed"] > 0:
            cats[cat]["test_failed"] += 1

    for op_name, op in bench_data.get("ops", {}).items():
        cat = op["category"]
        cats[cat]["bench_ops"] += 1
        for cfg in op["configs"]:
            cats[cat]["bench_configs"] += 1
            ratio = cfg.get("baseline_ratio")
            if ratio is not None:
                cats[cat]["ratios"].append(ratio)
                if ratio >= BASELINE_ALERT_THRESHOLD:
                    cats[cat]["bench_qualified"] += 1
                else:
                    cats[cat]["bench_underperforming"] += 1

    # Compute average ratios, remove raw list
    result = {}
    for name in sorted(cats):
        c = cats[name]
        ratios = c.pop("ratios")
        c["avg_ratio"] = round(sum(ratios) / len(ratios), 4) if ratios else None
        result[name] = c

    return result


# ---------------------------------------------------------------------------
# Baseline alerts
# ---------------------------------------------------------------------------

def detect_baseline_alerts(bench_data: dict) -> list[dict]:
    """Find configs where tileops is significantly slower than baseline."""
    alerts = []
    for op_name, op in bench_data.get("ops", {}).items():
        for cfg in op["configs"]:
            ratio = cfg.get("baseline_ratio")
            if ratio is not None and ratio < BASELINE_ALERT_THRESHOLD:
                alerts.append({
                    "op": op_name,
                    "config": cfg["name"],
                    "tileops_ms": cfg.get("tileops_latency_ms"),
                    "baseline_ms": cfg.get("baseline_latency_ms"),
                    "ratio": ratio,
                    "baseline_tag": cfg.get("baseline_tag", "baseline"),
                })
    alerts.sort(key=lambda x: x.get("ratio", 1))
    return alerts


# ---------------------------------------------------------------------------
# Regression / improvement detection (from perf_history)
# ---------------------------------------------------------------------------

def _find_best_latency(runs: list[dict], op: str, config_name: str) -> float | None:
    """Find best (lowest) tileops latency for an op+config across history."""
    best = None
    for run in runs:
        op_data = run.get("ops", {}).get(op, {})
        cfg_data = op_data.get(config_name, {})
        tileops_data = cfg_data.get("tileops", {})
        lat = tileops_data.get("latency_ms")
        if lat is not None and (best is None or lat < best):
            best = lat
    return best


def detect_regressions(bench_data: dict, history_path: str | None) -> tuple[list, list]:
    """Detect regressions and improvements vs perf history."""
    if not history_path or not Path(history_path).exists():
        return [], []

    try:
        history = json.loads(Path(history_path).read_text())
    except (json.JSONDecodeError, OSError):
        return [], []

    runs = history.get("runs", [])
    if not runs:
        return [], []

    regressions = []
    improvements = []

    for op_name, op in bench_data.get("ops", {}).items():
        for cfg in op["configs"]:
            lat = cfg.get("tileops_latency_ms")
            if lat is None:
                continue
            best = _find_best_latency(runs, op_name, cfg["name"])
            if best is None:
                continue

            delta = (lat - best) / best
            if (delta > REGRESSION_THRESHOLD
                    and delta > NOISE_FLOOR
                    and (lat - best) > REGRESSION_ABS_MIN):
                regressions.append({
                    "op": op_name,
                    "config": cfg["name"],
                    "best_ms": round(best, 4),
                    "curr_ms": round(lat, 4),
                    "delta_pct": round(delta * 100, 1),
                    "tflops": cfg.get("tileops_tflops"),
                })
            elif delta < -REGRESSION_THRESHOLD and abs(delta) > NOISE_FLOOR:
                improvements.append({
                    "op": op_name,
                    "config": cfg["name"],
                    "best_ms": round(best, 4),
                    "curr_ms": round(lat, 4),
                    "delta_pct": round(delta * 100, 1),
                    "tflops": cfg.get("tileops_tflops"),
                })

    regressions.sort(key=lambda x: -x["delta_pct"])
    improvements.sort(key=lambda x: x["delta_pct"])
    return regressions, improvements


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def build_nightly_data(args) -> dict:
    """Build the complete nightly_data.json structure."""
    test_data = {"total_cases": 0, "passed_cases": 0, "failed_cases": 0,
                 "skipped_cases": 0, "ops": {}}
    bench_data = {"total_configs": 0, "ops": {}, "failures": []}

    if args.test_xml and Path(args.test_xml).exists():
        test_data = parse_test_xml(args.test_xml)

    if args.bench_xml and Path(args.bench_xml).exists():
        bench_data = parse_bench_xml(args.bench_xml)

    categories = compute_categories(test_data, bench_data)
    baseline_alerts = detect_baseline_alerts(bench_data)
    regressions, improvements = detect_regressions(
        bench_data, getattr(args, "perf_history", None))

    return {
        "meta": {
            "date": args.date,
            "commit": args.commit,
            "generated_at": datetime.now(tz=timezone.utc).isoformat(),
        },
        "test": {
            "total_ops": len(test_data["ops"]),
            "total_cases": test_data["total_cases"],
            "passed_cases": test_data["passed_cases"],
            "failed_cases": test_data["failed_cases"],
            "skipped_cases": test_data["skipped_cases"],
            "ops": test_data["ops"],
        },
        "bench": {
            "total_ops": len(bench_data["ops"]),
            "total_configs": bench_data["total_configs"],
            "ops": bench_data["ops"],
            "failures": bench_data["failures"],
        },
        "categories": categories,
        "baseline_alerts": baseline_alerts,
        "regressions": regressions,
        "improvements": improvements,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Parse upstream JUnit XML artifacts into nightly_data.json")
    parser.add_argument("--test-xml", help="Path to test_results.xml")
    parser.add_argument("--bench-xml", help="Path to bench_results.xml")
    parser.add_argument("--perf-history", help="Path to perf_history.json (optional)")
    parser.add_argument("--date", required=True, help="Run date timestamp")
    parser.add_argument("--commit", required=True, help="Git commit hash")
    parser.add_argument("--output", required=True, help="Output nightly_data.json path")
    args = parser.parse_args()

    data = build_nightly_data(args)

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2))

    t = data["test"]
    b = data["bench"]
    print(f"Parsed: {t['total_ops']} test ops ({t['passed_cases']}/{t['total_cases']} cases), "
          f"{b['total_ops']} bench ops ({b['total_configs']} configs), "
          f"{len(data['categories'])} categories, "
          f"{len(data['baseline_alerts'])} alerts, "
          f"{len(data['regressions'])} regressions, "
          f"{len(data['improvements'])} improvements")
    print(f"Output: {args.output}")


if __name__ == "__main__":
    main()
