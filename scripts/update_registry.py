#!/usr/bin/env python3
"""update_registry.py — 每日更新算子注册表。

执行流程：
  1. 扫描 TileOPs 中当日（或指定日期后）merge 的 PR
  2. 将 PR 涉及的文件匹配到对应算子，更新 kernel 变更元数据
  3. 扫描代码库（可选），判断各算子的 implemented 状态
  4. 解析 test_results.xml，更新各算子的测试状态
  5. 解析 benchmark 日志和 bench_results.xml，提取性能数据
  6. 调用 Claude 对有变化的算子重新评估 func_score / perf_score / has_bugs
  7. 加载 op_manifest.json（可选），计算汇总统计写入 registry["summary"]
  8. 将更新写回 op_registry.json 和 op_data/*.yaml

用法：
    python scripts/update_registry.py \\
        --registry    scripts/op_registry.json \\
        --op-data-dir scripts/op_data/ \\
        --test-xml    path/to/test_results.xml \\
        --bench-log   path/to/tileops_benchmarks.log \\
        --bench-xml   path/to/bench_results.xml \\
        --tileops-repo tile-ai/TileOPs \\
        --repo-dir    /path/to/TileOPs \\
        --manifest    scripts/op_manifest.json \\
        [--since-date YYYY-MM-DD]   # 默认昨天

环境变量：
    ANTHROPIC_API_KEY 或 ANTHROPIC_AUTH_TOKEN  必需（用于 Claude 评估）
    ANTHROPIC_BASE_URL                          可选
    GH_TOKEN                                    必需（用于 gh CLI 扫描 PR）
"""

import argparse
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

from claude_utils import (
    call_claude_json,
    get_api_config,
    require_anthropic,
    SYSTEM_SCORE_EVALUATOR,
    SYSTEM_KERNEL_MAPPER,
)

try:
    import yaml as _yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

NOW_ISO  = datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
NOW_DATE = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")
TODAY    = datetime.now(tz=timezone.utc).date()



# ─────────────────────────────────────────────────────────────────────────────
# 1. 注册表 I/O
# ─────────────────────────────────────────────────────────────────────────────

def load_registry(path: str) -> dict:
    p = Path(path)
    if not p.exists():
        print(f"⚠ op_registry.json 不存在: {path}", file=sys.stderr)
        return {"schema_version": "2.0", "ops": {}}
    return json.loads(p.read_text())


def save_registry(registry: dict, path: str) -> None:
    registry["generated_at"] = NOW_ISO
    Path(path).write_text(
        json.dumps(registry, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def load_op_yaml(op_data_dir: str, op_id: str) -> dict | None:
    path = Path(op_data_dir) / f"{op_id}.yaml"
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    if HAS_YAML:
        return _yaml.safe_load(text) or {}
    # 降级：尝试 JSON 解析（bootstrap 可能写的是 JSON）
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {}


def save_op_yaml(op_data_dir: str, op_id: str, data: dict) -> None:
    path = Path(op_data_dir) / f"{op_id}.yaml"
    if not path.exists():
        return  # 不创建新文件，bootstrap 负责创建
    if HAS_YAML:
        path.write_text(
            _yaml.dump(data, allow_unicode=True, default_flow_style=False,
                       sort_keys=False, width=120),
            encoding="utf-8",
        )
    else:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2))


def deep_update(base: dict, updates: dict) -> dict:
    """递归合并 updates 到 base（返回 base 的引用）。"""
    for k, v in updates.items():
        if isinstance(v, dict) and isinstance(base.get(k), dict):
            deep_update(base[k], v)
        else:
            base[k] = v
    return base


# ─────────────────────────────────────────────────────────────────────────────
# 2. GitHub PR 扫描
# ─────────────────────────────────────────────────────────────────────────────

def _gh(args_list: list[str], timeout: int = 60) -> str | None:
    """运行 gh CLI 命令，返回 stdout 或 None（失败时）。"""
    try:
        result = subprocess.run(
            ["gh"] + args_list,
            capture_output=True, text=True, timeout=timeout,
        )
        if result.returncode != 0:
            print(f"  gh 命令失败: {' '.join(args_list[:4])}: {result.stderr[:200]}",
                  file=sys.stderr)
            return None
        return result.stdout
    except (subprocess.TimeoutExpired, FileNotFoundError) as exc:
        print(f"  gh CLI 不可用: {exc}", file=sys.stderr)
        return None


def get_merged_prs(tileops_repo: str, since_date: str) -> list[dict]:
    """返回 since_date 之后 merge 进 main 的 PR 列表。"""
    out = _gh([
        "pr", "list",
        "--repo",   tileops_repo,
        "--state",  "merged",
        "--base",   "main",
        "--search", f"merged:>={since_date}",
        "--limit",  "100",
        "--json",   "number,title,mergedAt,author,url",
    ])
    if not out:
        return []
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        return []


def get_pr_files(tileops_repo: str, pr_number: int) -> list[str]:
    """返回 PR 修改的文件路径列表。"""
    out = _gh([
        "pr", "view", str(pr_number),
        "--repo", tileops_repo,
        "--json", "files",
        "-q",     ".files[].path",
    ], timeout=30)
    if not out:
        return []
    return [line.strip() for line in out.splitlines() if line.strip()]


def _path_matches(changed: str, mapped: str) -> bool:
    """判断 PR 变更路径是否匹配注册表中的文件路径（去掉 ::fn 后缀后比较）。"""
    mapped_path = mapped.split("::")[0]
    # 完全匹配 or 其中一个是另一个的后缀
    return (changed == mapped_path
            or changed.endswith("/" + mapped_path)
            or mapped_path.endswith("/" + changed))


def match_pr_to_ops(registry: dict, changed_files: list[str]) -> set[str]:
    """找出 PR 涉及的算子 ID 集合。"""
    affected: set[str] = set()
    for op_id, op_data in registry.get("ops", {}).items():
        for file_list in op_data.get("files", {}).values():
            for mapped in file_list:
                if any(_path_matches(cf, mapped) for cf in changed_files):
                    affected.add(op_id)
                    break
            else:
                continue
            break
    return affected


def is_kernel_file(op_data: dict, filepath: str) -> bool:
    """判断 filepath 是否属于该算子的 kernel 文件。"""
    for mapped in op_data.get("files", {}).get("kernel", []):
        if _path_matches(filepath, mapped):
            return True
    return False


# ─────────────────────────────────────────────────────────────────────────────
# 2b. Claude 增量映射重建（对 PR 受影响的算子）
# ─────────────────────────────────────────────────────────────────────────────

def remap_affected_ops(
    registry: dict,
    affected_op_ids: set[str],
    manifest: dict,
    repo_dir: str,
    model: str,
    api_key: str,
    base_url: str | None,
) -> dict[str, dict]:
    """对受 PR 影响的算子，调用 Claude 重建 kernel/test/bench 文件映射。

    Returns: {op_id: {kernel: [...], tests: [...], bench: [...]}}
    """
    from bootstrap_registry import get_compact_tree, build_file_mapping_prompt

    if not affected_op_ids or not repo_dir or not api_key:
        return {}

    # 构建文件树（传给 Claude）
    file_tree = get_compact_tree(repo_dir)

    # 按 category 分组受影响的算子
    ops_by_cat: dict[str, list[dict]] = {}
    op_id_to_cat: dict[str, str] = {}
    for cat in manifest.get("categories", []):
        for op in cat.get("ops", []):
            if op["id"] in affected_op_ids:
                cat_name = cat["name"]
                ops_by_cat.setdefault(cat_name, [])
                # 附加已有的 auto_files 信息
                reg_op = registry.get("ops", {}).get(op["id"], {})
                op_copy = dict(op)
                op_copy["_auto_files"] = {
                    "op":    reg_op.get("files", {}).get("op", []),
                    "tests": reg_op.get("files", {}).get("tests", []),
                    "bench": reg_op.get("files", {}).get("bench", []),
                }
                ops_by_cat[cat_name].append(op_copy)

    result: dict[str, dict] = {}

    for cat_name, ops_batch in ops_by_cat.items():
        try:
            prompt = build_file_mapping_prompt(ops_batch, file_tree, cat_name)
            data = call_claude_json(
                prompt, model, api_key, base_url,
                system=SYSTEM_KERNEL_MAPPER,
                required_keys=["mappings"],
                max_tokens=8192,
            )
            for item in data.get("mappings", []):
                # 硬过滤：排除列表中的文件路径
                from bootstrap_registry import EXCLUDED_OPS
                def _filter_excluded(paths: list[str]) -> list[str]:
                    return [p for p in paths
                            if not any(ex in p.lower() for ex in EXCLUDED_OPS)]
                kernel = _filter_excluded(item.get("kernel", []))
                tests  = _filter_excluded(item.get("tests", []))
                bench  = _filter_excluded(item.get("bench", []))
                if not kernel:
                    tests = []
                    bench = []
                result[item["id"]] = {
                    "kernel": kernel,
                    "tests":  tests,
                    "bench":  bench,
                }
            print(f"  Claude 映射重建 [{cat_name}]: {len(ops_batch)} 个算子")
        except Exception as exc:
            print(f"  ⚠ Claude 映射重建失败 [{cat_name}]: {exc}", file=sys.stderr)

    return result


# ─────────────────────────────────────────────────────────────────────────────
# 3. 测试结果解析
# ─────────────────────────────────────────────────────────────────────────────

def parse_test_xml(test_xml: str | None) -> dict[str, dict]:
    """
    解析 JUnit XML，返回 {fn_name: {passed: bool, errors: [str]}}。
    fn_name 取 testcase.name 中 '[' 之前的部分。
    """
    results: dict[str, dict] = {}
    if not test_xml or not Path(test_xml).exists():
        return results
    try:
        root = ET.parse(test_xml).getroot()
    except ET.ParseError:
        return results

    for tc in root.iter("testcase"):
        fn = tc.get("name", "").split("[")[0]
        if not fn:
            continue
        fail_el = tc.find("failure")
        err_el  = tc.find("error")

        if fn not in results:
            results[fn] = {"passed": True, "errors": []}

        if fail_el is not None or err_el is not None:
            results[fn]["passed"] = False
            elem = fail_el if fail_el is not None else err_el
            msg  = (elem.get("message") or "")
            body = (elem.text or "")
            combined = (msg + "\n" + body).strip()[:600]
            results[fn]["errors"].append(combined)

    return results


def parse_test_log(test_log: str | None) -> dict[str, dict]:
    """
    解析 pytest 文本日志，返回 {fn_name: {passed: bool, errors: [str]}}。
    匹配格式：tests/ops/test_activation.py::test_relu_op[params] PASSED/FAILED
    """
    results: dict[str, dict] = {}
    if not test_log or not Path(test_log).exists():
        return results
    try:
        text = Path(test_log).read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return results

    pat = re.compile(
        r"^(tests/\S+?)::(\w+)(?:\[.*?\])?\s+(PASSED|FAILED|ERROR)",
        re.MULTILINE,
    )
    for m in pat.finditer(text):
        fn = m.group(2)
        status = m.group(3)
        if fn not in results:
            results[fn] = {"passed": True, "errors": []}
        if status in ("FAILED", "ERROR"):
            results[fn]["passed"] = False

    return results


def get_op_test_status(op_data: dict, test_results: dict) -> dict:
    """
    计算算子的测试状态。
    返回 {last_run, passed, errors, status}。

    status 取值：
      - "passed"  : tests 映射存在 且 全部通过
      - "failed"  : tests 映射存在，但有失败或 XML 中无结果
      - "missing" : tests 映射为空（无 test 文件）
    """
    test_entries = op_data.get("files", {}).get("tests", [])
    if not test_entries:
        return {
            "last_run": NOW_DATE,
            "passed":   None,
            "errors":   [],
            "status":   "missing",
        }

    all_errors: list[str] = []
    all_passed = True
    any_found  = False

    for entry in test_entries:
        fn = entry.split("::")[-1] if "::" in entry else entry
        if fn in test_results:
            any_found = True
            r = test_results[fn]
            if not r["passed"]:
                all_passed = False
                all_errors.extend(r["errors"])

    if not any_found:
        # 有映射但 XML 中没找到结果 → 视为 failed
        return {
            "last_run": NOW_DATE,
            "passed":   False,
            "errors":   [],
            "status":   "failed",
        }

    return {
        "last_run": NOW_DATE,
        "passed":   all_passed,
        "errors":   all_errors[:5],
        "status":   "passed" if all_passed else "failed",
    }


# ─────────────────────────────────────────────────────────────────────────────
# 4. Benchmark 日志解析
# ─────────────────────────────────────────────────────────────────────────────

def _parse_md_table(lines: list[str]) -> list[dict[str, str]]:
    """解析 Markdown 表格行，返回 [{col_name: value, ...}, ...]。"""
    if len(lines) < 3:
        return []
    # 第 1 行: | col1 | col2 | ...
    headers = [h.strip() for h in lines[0].strip().strip("|").split("|")]
    # 第 2 行: | --- | --- | ... (分隔符，跳过)
    rows = []
    for line in lines[2:]:
        line = line.strip()
        if not line or not line.startswith("|"):
            break
        vals = [v.strip() for v in line.strip("|").split("|")]
        if len(vals) == len(headers):
            rows.append(dict(zip(headers, vals)))
    return rows


def parse_bench_log(bench_log: str | None) -> dict[str, dict]:
    """
    从 benchmark 日志中提取性能数据。

    解析 Markdown 格式的 benchmark 报告：
      ## <bench_name>
      ### tileops
      | ... | latency_ms | ... |
      ### baseline
      | ... | latency_ms | ... |

    对每个 bench，计算 ratio = baseline_avg_latency / tileops_avg_latency。
    返回 {bench_name: {tileops, baseline, ratio, summary}}。
    """
    results: dict[str, dict] = {}
    if not bench_log or not Path(bench_log).exists():
        return results
    try:
        text = Path(bench_log).read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return results

    lines = text.splitlines()
    n = len(lines)
    i = 0

    # 查找 "===== profile_run.log summary =====" 之后的内容
    while i < n and "profile_run.log summary" not in lines[i]:
        i += 1

    current_bench = None
    current_section = None  # "tileops" or "baseline"
    bench_data: dict[str, dict[str, list[dict]]] = {}  # {bench_name: {tileops: [...], baseline: [...]}}

    while i < n:
        line = lines[i].strip()

        # ## bench_name（顶级 section，排除 Environment 等非 bench 段）
        if line.startswith("## ") and not line.startswith("## Environment"):
            current_bench = line[3:].strip().lower()
            current_section = None
            bench_data.setdefault(current_bench, {"tileops": [], "baseline": []})

        # ### tileops 或 ### baseline
        elif line.startswith("### "):
            section_name = line[4:].strip().lower()
            if section_name in ("tileops", "baseline") and current_bench:
                current_section = section_name
                # 解析紧跟的 Markdown 表格
                table_lines = []
                j = i + 1
                # 跳过空行
                while j < n and not lines[j].strip():
                    j += 1
                # 收集表格行
                while j < n and lines[j].strip().startswith("|"):
                    table_lines.append(lines[j])
                    j += 1
                rows = _parse_md_table(table_lines)
                bench_data[current_bench][current_section] = rows
                i = j
                continue
            else:
                # 非 tileops/baseline 的子段（如 ### relu_direct），作为独立 bench
                current_bench = section_name
                current_section = None
                bench_data.setdefault(current_bench, {"tileops": [], "baseline": []})

        i += 1

    # 计算每个 bench 的 ratio
    for bench_name, data in bench_data.items():
        tileops_rows = data.get("tileops", [])
        baseline_rows = data.get("baseline", [])

        if not tileops_rows:
            continue

        # 提取 latency_ms 列的平均值
        def _avg_latency(rows: list[dict]) -> float | None:
            vals = []
            for r in rows:
                try:
                    vals.append(float(r.get("latency_ms", "")))
                except (ValueError, TypeError):
                    pass
            return sum(vals) / len(vals) if vals else None

        tileops_lat = _avg_latency(tileops_rows)
        baseline_lat = _avg_latency(baseline_rows)

        if tileops_lat is None or tileops_lat == 0:
            continue

        # 异常检测：tileops 与 baseline 差距超过 10 倍 → ratio 视为无效
        if baseline_lat and baseline_lat > 0:
            raw_ratio = baseline_lat / tileops_lat
            if raw_ratio > 10 or raw_ratio < 0.1:
                ratio = None  # 数据异常，不计入
            else:
                ratio = round(raw_ratio, 4)
        else:
            ratio = None

        results[bench_name] = {
            "tileops":  f"{tileops_lat:.4f} ms",
            "baseline": f"{baseline_lat:.4f} ms" if baseline_lat else "N/A",
            "ratio":    ratio,
            "summary":  f"TileOps {tileops_lat:.4f}ms vs Baseline {baseline_lat:.4f}ms"
                        + (f" (ratio {ratio:.2f})" if ratio else "")
                        if baseline_lat else f"TileOps {tileops_lat:.4f}ms (no baseline)",
        }

    return results


def parse_bench_xml(bench_xml: str | None) -> tuple[set[str], set[str]]:
    """解析 bench JUnit XML，返回 (passed_classnames, failed_classnames)。

    Uses classname attribute (e.g. 'benchmarks.ops.bench_activation').
    """
    passed: set[str] = set()
    failed: set[str] = set()
    if not bench_xml or not Path(bench_xml).exists():
        return passed, failed
    try:
        root = ET.parse(bench_xml).getroot()
    except ET.ParseError:
        return passed, failed
    for tc in root.iter("testcase"):
        classname = tc.get("classname", "")
        has_failure = tc.find("failure") is not None or tc.find("error") is not None
        if has_failure:
            failed.add(classname)
        else:
            passed.add(classname)
    return passed, failed


def get_op_bench_data(op_data: dict, bench_results: dict) -> dict | None:
    """提取算子对应的 benchmark 数据。

    优先按 ::fn_name 精确匹配（与 test 粒度一致），
    无函数名后缀时降级为文件 stem 匹配。
    """
    bench_entries = op_data.get("files", {}).get("bench", [])
    if not bench_entries:
        return None

    found = {}
    for entry in bench_entries:
        if "::" in entry:
            # 函数级匹配：benchmarks/ops/bench_activation.py::bench_relu -> bench_relu
            fn = entry.split("::")[-1].lower()
            if fn in bench_results:
                found[fn] = bench_results[fn]
            # bench log 中的 key 可能没有 bench_ 前缀（如 "relu" vs "bench_relu"）
            elif fn.startswith("bench_"):
                short = fn[len("bench_"):]
                if short in bench_results:
                    found[short] = bench_results[short]
        else:
            # 降级：文件级匹配（兼容旧格式）
            stem = Path(entry).stem.lower()
            for key, data in bench_results.items():
                if key.startswith(stem) or stem.startswith(key.split("_")[0]):
                    found[key] = data

    return found if found else None


BENCH_QUALIFIED_RATIO = 0.8   # ratio >= 0.8 即达标


def get_op_bench_status(op_data: dict, bench_results: dict, bench_xml_passed: set[str] = None, bench_xml_failed: set[str] = None) -> dict:
    """
    计算算子的 benchmark 状态。
    返回 {last_run, status, ratio, details}。

    status 取值：
      - "qualified"        : bench 存在 且 ratio >= 0.8
      - "underperforming"  : bench 存在 且 ratio < 0.8
      - "passed"           : bench XML 显示通过，但无 ratio 数据
      - "failed"           : bench 映射存在，但 log 中无结果或运行失败
      - "missing"          : bench 映射为空（无 bench 文件）
    """
    bench_entries = op_data.get("files", {}).get("bench", [])
    if not bench_entries:
        return {
            "last_run": NOW_DATE,
            "status":   "missing",
            "ratio":    None,
            "details":  [],
        }

    # ── Bench XML matching ────────────────────────────────────────────────
    xml_any_passed = False
    xml_any_failed = False
    if bench_xml_passed is not None or bench_xml_failed is not None:
        _xml_passed = bench_xml_passed or set()
        _xml_failed = bench_xml_failed or set()
        for entry in bench_entries:
            # Convert entry to classname:
            # benchmarks/ops/bench_activation.py::bench_relu → benchmarks.ops.bench_activation
            file_part = entry.split("::")[0]  # take file path part before ::
            # Remove .py suffix and replace / with .
            classname = file_part.replace("/", ".").removesuffix(".py")
            if classname in _xml_passed:
                xml_any_passed = True
            if classname in _xml_failed:
                xml_any_failed = True

    # ── Bench log data ────────────────────────────────────────────────────
    bench_data = get_op_bench_data(op_data, bench_results)
    if bench_data:
        # 汇总所有 bench 函数的 ratio，取最小值作为整体 ratio
        details = [{"bench_fn": fn, **v} for fn, v in bench_data.items()]
        ratios = [v["ratio"] for v in bench_data.values() if v.get("ratio") is not None]

        if ratios:
            min_ratio = min(ratios)
            status = "qualified" if min_ratio >= BENCH_QUALIFIED_RATIO else "underperforming"
            return {
                "last_run": NOW_DATE,
                "status":   status,
                "ratio":    round(min_ratio, 4),
                "details":  details,
            }

        # Has bench data but no ratio — fall through to XML check below
        # (keep details for potential use)

    # ── No ratio data from bench log, check XML results ───────────────────
    if xml_any_passed:
        return {
            "last_run": NOW_DATE,
            "status":   "passed",
            "ratio":    None,
            "details":  [],
        }

    if xml_any_failed:
        return {
            "last_run": NOW_DATE,
            "status":   "failed",
            "ratio":    None,
            "details":  [],
        }

    # 有映射但 log 和 XML 中都没找到结果
    return {
        "last_run": NOW_DATE,
        "status":   "failed",
        "ratio":    None,
        "details":  [],
    }


# ─────────────────────────────────────────────────────────────────────────────
# 5. Claude 评估
# ─────────────────────────────────────────────────────────────────────────────

def build_score_prompt(ops_batch: list[dict]) -> str:
    return f"""你是 TileOPs 项目的代码审查专家。请根据以下信息为每个算子打分。

## 评分标准

### func_score（功能完整性，1-5）
- 1 = 骨架/占位符，基本不可用
- 2 = 基础功能，仅支持最简单的形状/类型
- 3 = 主要功能实现，但缺少边界情况处理
- 4 = 接近完整，仅有次要功能缺失
- 5 = 完整实现，覆盖所有预期场景

### perf_score（性能，相对 baseline，1-5）
- 1 = <50% baseline
- 2 = 50-75%
- 3 = 75-90%
- 4 = 90-100%
- 5 = >100%（超越 baseline）

### has_bugs
- 如果测试失败或 benchmark 异常，通常为 true

## 算子状态数据
```json
{json.dumps(ops_batch, ensure_ascii=False, indent=2)}
```

## 输出格式
严格输出 JSON，不含其他文字：
{{
  "updates": [
    {{
      "id": "ew.binary_arith.add",
      "func_score": 4,
      "func_score_notes": "前向传播完整，缺少 inplace 操作和复数类型",
      "perf_score": 4,
      "has_bugs": false,
      "bugs": []
    }}
  ]
}}

注意：
- 信息不足时某字段可设为 null（不强行猜测）
- 只输出**有实质变化**的算子（如当前分数已正确，可不输出）
- func_score_notes 限 1-2 句，说明原因或缺失点
- bugs 为 string 列表，简短描述已知问题"""


# ─────────────────────────────────────────────────────────────────────────────
# 6. 汇总统计
# ─────────────────────────────────────────────────────────────────────────────

def compute_summary(registry: dict, manifest: dict) -> dict:
    """从 registry 计算汇总统计，替代 progress.json。"""
    ops = registry.get("ops", {})

    categories_out = []
    grand_impl = grand_tested = grand_benched = grand_done = 0

    for cat in manifest.get("categories", []):
        cat_impl = cat_tested = cat_benched = cat_done = 0
        ops_out = []

        for mop in cat.get("ops", []):
            op_id = mop["id"]
            op_data = ops.get(op_id, {})

            # implemented: registry 中有 kernel 文件映射即为已实现
            implemented = bool(op_data.get("files", {}).get("kernel"))

            # test status
            ts = op_data.get("test_status", {})
            ts_status = ts.get("status", "missing")
            tested = ts_status == "passed"
            test_failed = ts_status == "failed"

            # bench status
            bs = op_data.get("bench_status", {})
            bs_status = bs.get("status", "missing")
            bench_ok = True if bs_status in ("qualified", "passed") else (False if bs_status in ("underperforming", "failed") else None)

            # overall status
            if implemented and tested and bench_ok is True:
                status = "done"
            elif implemented and tested:
                status = "tested"
            elif implemented and not tested and ts_status == "missing":
                status = "impl_only"
            elif implemented:
                status = "partial"
            else:
                status = "missing"

            if implemented: cat_impl += 1
            if tested: cat_tested += 1
            if bench_ok is True: cat_benched += 1
            if status == "done": cat_done += 1

            # Store implemented in registry for downstream use
            op_data["implemented"] = implemented

            ops_out.append({
                "id": op_id,
                "name": mop["name"],
                "sub": mop.get("sub", ""),
                "implemented": implemented,
                "tested": tested,
                "test_failed": test_failed,
                "bench_ok": bench_ok,
                "status": status,
            })

        grand_impl += cat_impl
        grand_tested += cat_tested
        grand_benched += cat_benched
        grand_done += cat_done

        categories_out.append({
            "id": cat["id"],
            "name": cat["name"],
            "issue": cat.get("issue"),
            "difficulty": cat.get("difficulty"),
            "total_ops": len(cat["ops"]),
            "impl_ops": cat_impl,
            "tested_ops": cat_tested,
            "benched_ops": cat_benched,
            "done_ops": cat_done,
            "ops": ops_out,
        })

    return {
        "generated_at": NOW_ISO,
        "total_ops": manifest.get("total_ops", 0),
        "impl_ops": grand_impl,
        "tested_ops": grand_tested,
        "benched_ops": grand_benched,
        "done_ops": grand_done,
        "categories": categories_out,
    }


# ─────────────────────────────────────────────────────────────────────────────
# 7. 主逻辑
# ─────────────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="每日更新 TileOPs 算子注册表")
    parser.add_argument("--registry",     required=True, help="op_registry.json 路径")
    parser.add_argument("--op-data-dir",  required=True, help="op_data/ 目录路径")
    parser.add_argument("--test-xml",     default=None,  help="test_results.xml 路径")
    parser.add_argument("--test-log",     default=None,  help="tileops_op_test.log 路径（XML 不存在时的 fallback）")
    parser.add_argument("--bench-log",    default=None,  help="tileops_benchmarks.log 路径")
    parser.add_argument("--bench-xml",    default=None,  help="bench_results.xml 路径")
    parser.add_argument("--tileops-repo", default="tile-ai/TileOPs",
                        help="TileOPs GitHub 仓库（owner/name）")
    parser.add_argument("--since-date",   default=None,
                        help="扫描 PR 的起始日期 YYYY-MM-DD（默认昨天）")
    parser.add_argument("--model",        default="claude-sonnet-4-6")
    parser.add_argument("--skip-claude",  action="store_true",
                        help="跳过 Claude 评估步骤")
    parser.add_argument("--repo-dir",     default=None,  help="TileOPs 仓库根目录（用于 Claude 增量映射重建）")
    parser.add_argument("--manifest",     default=None,  help="op_manifest.json 路径（用于类别结构和 op_classes）")
    args = parser.parse_args()

    api_key, base_url = get_api_config()

    since_date = args.since_date or str(TODAY - timedelta(days=1))

    # ── 加载注册表 ───────────────────────────────────────────────────────────
    print(f"加载注册表: {args.registry}")
    registry = load_registry(args.registry)
    n_ops = len(registry.get("ops", {}))
    print(f"  {n_ops} 个算子")
    if n_ops == 0:
        print("  ⚠ 注册表为空，请先运行 bootstrap_registry.py", file=sys.stderr)

    # ── PR 扫描 ──────────────────────────────────────────────────────────────
    print(f"\n扫描 {args.tileops_repo} 中 {since_date} 之后的 merged PR ...")
    prs = get_merged_prs(args.tileops_repo, since_date)
    print(f"  找到 {len(prs)} 个 PR")

    # pr_kernel_updates: op_id -> 最新 PR 信息（只记录影响 kernel 文件的 PR）
    pr_kernel_updates: dict[str, dict] = {}
    # pr_any_updates: op_id -> 最新 PR 信息（影响任意文件）
    pr_any_updates: dict[str, dict] = {}

    for pr in prs:
        pr_num    = pr["number"]
        pr_author = pr.get("author", {}).get("login", "unknown")
        pr_merged = pr.get("mergedAt", NOW_ISO)
        pr_url    = pr.get("url", "")
        pr_title  = pr.get("title", "")

        changed_files = get_pr_files(args.tileops_repo, pr_num)
        if not changed_files:
            continue

        affected_ops = match_pr_to_ops(registry, changed_files)
        if affected_ops:
            print(f"  PR #{pr_num} ({pr_title[:50]}): 影响 {len(affected_ops)} 个算子")

        for op_id in affected_ops:
            op_data = registry["ops"].get(op_id, {})
            pr_info = {
                "number":   pr_num,
                "author":   pr_author,
                "mergedAt": pr_merged,
                "url":      pr_url,
                "title":    pr_title,
            }
            # 更新最新 PR（按 mergedAt 时间）
            existing = pr_any_updates.get(op_id, {})
            if not existing or pr_merged > existing.get("mergedAt", ""):
                pr_any_updates[op_id] = pr_info

            # 只有 kernel 文件变化时才更新 kernel_last_*
            if any(is_kernel_file(op_data, cf) for cf in changed_files):
                existing_k = pr_kernel_updates.get(op_id, {})
                if not existing_k or pr_merged > existing_k.get("mergedAt", ""):
                    pr_kernel_updates[op_id] = pr_info

    print(f"  {len(pr_any_updates)} 个算子受 PR 影响, "
          f"其中 {len(pr_kernel_updates)} 个有 kernel 变更")

    # ── Claude 增量映射重建（对受影响的算子）──────────────────────────────────
    if pr_any_updates and args.repo_dir and not args.skip_claude and api_key:
        manifest_for_remap = None
        if args.manifest:
            mp = Path(args.manifest)
            if mp.exists():
                manifest_for_remap = json.loads(mp.read_text())
        if manifest_for_remap:
            print(f"\n对 {len(pr_any_updates)} 个受影响算子重建文件映射 ...")
            remap_results = remap_affected_ops(
                registry, set(pr_any_updates.keys()), manifest_for_remap,
                args.repo_dir, args.model, api_key, base_url,
            )
            for op_id, new_files in remap_results.items():
                if op_id in registry.get("ops", {}):
                    op = registry["ops"][op_id]
                    # 更新映射，保留 op 文件（op 不由 Claude 管理）
                    op["files"]["kernel"] = new_files.get("kernel", op["files"].get("kernel", []))
                    op["files"]["tests"]  = new_files.get("tests",  op["files"].get("tests", []))
                    op["files"]["bench"]  = new_files.get("bench",  op["files"].get("bench", []))
                    op["files_last_scanned"] = NOW_ISO
            print(f"  更新了 {len(remap_results)} 个算子的文件映射")

    # ── 测试结果 ─────────────────────────────────────────────────────────────
    print(f"\n解析测试结果: {args.test_xml or '(未提供)'}")
    test_results = parse_test_xml(args.test_xml)
    if not test_results and args.test_log:
        print(f"  XML 为空，fallback 到 pytest log: {args.test_log}")
        test_results = parse_test_log(args.test_log)
    print(f"  {len(test_results)} 个测试函数")

    # ── Benchmark 日志 ───────────────────────────────────────────────────────
    print(f"解析 benchmark 日志: {args.bench_log or '(未提供)'}")
    bench_results = parse_bench_log(args.bench_log)
    print(f"  {len(bench_results)} 个 benchmark 有数据")

    # ── Benchmark XML ─────────────────────────────────────────────────────
    print(f"解析 benchmark XML: {args.bench_xml or '(未提供)'}")
    bench_xml_passed, bench_xml_failed = parse_bench_xml(args.bench_xml)
    print(f"  {len(bench_xml_passed)} passed, {len(bench_xml_failed)} failed")

    # ── 更新每个算子 ─────────────────────────────────────────────────────────
    print("\n更新算子记录 ...")
    ops_to_score: list[dict] = []   # 需要 Claude 重新评分的算子

    for op_id, op_data in registry.get("ops", {}).items():
        registry_updates: dict = {}   # 更新到 op_registry.json
        yaml_updates: dict     = {}   # 更新到 YAML 文件
        needs_score = False

        # PR kernel 元数据
        if op_id in pr_kernel_updates:
            pk = pr_kernel_updates[op_id]
            meta = {
                "kernel_last_updated":   pk["mergedAt"],
                "kernel_last_pr_number": pk["number"],
                "kernel_last_pr_url":    pk["url"],
                "kernel_last_pr_author": pk["author"],
                "kernel_last_pr_title":  pk["title"],
            }
            registry_updates["kernel_last_updated"]   = pk["mergedAt"]
            registry_updates["kernel_last_pr_author"] = pk["author"]
            yaml_updates.update(meta)
            needs_score = True

        # 测试状态（仅当有 test 数据时更新，否则保留已有值）
        if test_results:
            test_status = get_op_test_status(op_data, test_results)
            yaml_updates["test_status"] = test_status
            registry_updates["test_status"] = test_status
            if test_status["status"] == "failed" and op_data.get("has_bugs") is None:
                registry_updates["has_bugs"] = True
                yaml_updates["has_bugs"]     = True
            if test_status["status"] != "missing":
                needs_score = True
        else:
            test_status = op_data.get("test_status") or {"status": "missing"}

        # Benchmark 状态（仅当有 bench 数据时更新，否则保留已有值）
        has_bench_data = bench_results or bench_xml_passed or bench_xml_failed
        if has_bench_data:
            bench_status = get_op_bench_status(op_data, bench_results, bench_xml_passed, bench_xml_failed)
            yaml_updates["bench_status"] = bench_status
            registry_updates["bench_status"] = bench_status
            if bench_status["details"]:
                yaml_updates.setdefault("perf_details", {})["results"] = bench_status["details"]
                yaml_updates.setdefault("perf_details", {})["last_run"] = NOW_DATE
            if bench_status["status"] not in ("missing",):
                needs_score = True
        else:
            bench_status = op_data.get("bench_status") or {"status": "missing"}

        # 收集需要评分的算子信息
        if needs_score or op_id in pr_any_updates:
            ops_to_score.append({
                "id":                  op_id,
                "name":                op_data.get("name", ""),
                "category":            op_data.get("category", ""),
                "current_func_score":  op_data.get("func_score"),
                "current_perf_score":  op_data.get("perf_score"),
                "current_has_bugs":    op_data.get("has_bugs"),
                "test_status":         test_status,
                "bench_status":        bench_status,
                "pr_title":            pr_any_updates.get(op_id, {}).get("title"),
            })

        # 写回注册表
        if registry_updates:
            op_data.update(registry_updates)
            op_data["last_updated"] = NOW_ISO

        # 写回 YAML
        if yaml_updates:
            yaml_data = load_op_yaml(args.op_data_dir, op_id)
            if yaml_data is not None:
                deep_update(yaml_data, yaml_updates)
                yaml_data["last_updated"] = NOW_ISO
                yaml_data["updated_by"]   = "nightly-auto"
                save_op_yaml(args.op_data_dir, op_id, yaml_data)

    print(f"  {len(ops_to_score)} 个算子待 Claude 评分")

    # ── Claude 评分 ──────────────────────────────────────────────────────────
    if ops_to_score and not args.skip_claude and api_key:
        if require_anthropic() is None:
            args.skip_claude = True

    if ops_to_score and not args.skip_claude and api_key:
        batch_size = 20
        total_updated = 0
        for i in range(0, len(ops_to_score), batch_size):
            batch = ops_to_score[i : i + batch_size]
            print(f"  Claude 评分批次 {i // batch_size + 1}/{(len(ops_to_score) - 1) // batch_size + 1}"
                  f" ({len(batch)} 个算子) ...")
            try:
                prompt = build_score_prompt(batch)
                data   = call_claude_json(
                    prompt, args.model, api_key, base_url,
                    system=SYSTEM_SCORE_EVALUATOR,
                    required_keys=["updates"],
                )

                for item in data.get("updates", []):
                    op_id = item.get("id")
                    if not op_id or op_id not in registry.get("ops", {}):
                        continue

                    # 更新 registry JSON
                    op = registry["ops"][op_id]
                    for field in ("func_score", "perf_score", "has_bugs"):
                        if field in item and item[field] is not None:
                            op[field] = item[field]
                    op["last_updated"] = NOW_ISO

                    # 更新 YAML
                    yaml_data = load_op_yaml(args.op_data_dir, op_id)
                    if yaml_data is not None:
                        for field in ("func_score", "func_score_notes",
                                      "perf_score", "has_bugs", "bugs"):
                            if field in item:
                                yaml_data[field] = item[field]
                        if "func_score" in item:
                            yaml_data["func_score_updated"] = NOW_DATE
                        if "perf_score" in item:
                            yaml_data["perf_score_updated"] = NOW_DATE
                        yaml_data["last_updated"] = NOW_ISO
                        yaml_data["updated_by"]   = "claude-nightly"
                        save_op_yaml(args.op_data_dir, op_id, yaml_data)

                    total_updated += 1

                print(f"    更新了 {len(data.get('updates', []))} 个算子")

            except Exception as exc:
                print(f"  ⚠ Claude 评分失败: {exc}", file=sys.stderr)

        print(f"  Claude 共更新 {total_updated} 个算子")
    elif ops_to_score and not api_key:
        print("  ⚠ 未设置 ANTHROPIC_API_KEY，跳过 Claude 评分", file=sys.stderr)

    # ── 计算汇总统计 ──────────────────────────────────────────────────────
    manifest = None
    if args.manifest:
        manifest_path = Path(args.manifest)
        if manifest_path.exists():
            manifest = json.loads(manifest_path.read_text())

    if manifest:
        print("\n计算汇总统计 ...")
        summary = compute_summary(registry, manifest)
        registry["summary"] = summary
        print(f"  impl={summary['impl_ops']} tested={summary['tested_ops']} "
              f"benched={summary['benched_ops']} done={summary['done_ops']}/{summary['total_ops']}")

    # ── 保存注册表 ───────────────────────────────────────────────────────────
    save_registry(registry, args.registry)
    print(f"\n注册表已保存: {args.registry}")
    print("完成！")


if __name__ == "__main__":
    main()
