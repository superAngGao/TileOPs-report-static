#!/usr/bin/env python3
"""bootstrap_registry.py — 初始化算子注册表，使用 Claude 扫描 TileOPs 代码库建立文件映射。

对每个算子：
  - 自动搜索 op 类文件（grep op_classes）、test 函数文件（grep test_fns）
  - 调用 Claude 识别对应的 kernel 实现文件
  - 生成 op_registry.json（JSON 汇总）和 op_data/<id>.yaml（详细记录）

用法：
    python scripts/bootstrap_registry.py \\
        --manifest    scripts/op_manifest.json \\
        --repo-dir    TileOPs/ \\
        --registry    scripts/op_registry.json \\
        --op-data-dir scripts/op_data/ \\
        [--skip-claude]   # 跳过 Claude，仅生成骨架

环境变量：
    ANTHROPIC_API_KEY 或 ANTHROPIC_AUTH_TOKEN  必需（--skip-claude 时可省略）
    ANTHROPIC_BASE_URL                          可选
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from claude_utils import (
    call_claude_json,
    get_api_config,
    SYSTEM_KERNEL_MAPPER,
)

try:
    import yaml as _yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

NOW_ISO = datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
NOW_DATE = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")

# ── 排除列表：不在 186 算子列表中的算子名，Claude 不应将其文件归属到任何算子 ──
EXCLUDED_OPS = [
    "engram",
]

# ── 扫描目录 ─────────────────────────────────────────────────────────────────
KERNEL_DIRS = ["tilelang", "tileops/kernels", "tileops/kernel"]
OP_DIRS     = ["tileops/ops", "tileops"]
TEST_DIRS   = ["tests"]
BENCH_DIRS  = ["benchmarks"]


# ─────────────────────────────────────────────────────────────────────────────
# 1. 代码库扫描工具
# ─────────────────────────────────────────────────────────────────────────────

def get_py_files(repo_dir: str, subdirs: list[str]) -> list[str]:
    """返回指定子目录下所有 .py 文件的相对路径（相对 repo_dir）。"""
    repo = Path(repo_dir)
    files = []
    for d in subdirs:
        target = repo / d
        if not target.exists():
            continue
        for f in sorted(target.rglob("*.py")):
            files.append(str(f.relative_to(repo)))
    return files


def get_compact_tree(repo_dir: str) -> str:
    """
    返回 kernel/op/test/bench 目录下所有 .py 文件的路径列表（紧凑格式）。
    用于传给 Claude。
    """
    all_dirs = KERNEL_DIRS + OP_DIRS + TEST_DIRS + BENCH_DIRS
    seen_dirs = set()
    unique_dirs = []
    for d in all_dirs:
        if d not in seen_dirs:
            seen_dirs.add(d)
            unique_dirs.append(d)

    files = get_py_files(repo_dir, unique_dirs)
    return "\n".join(files) if files else "(no .py files found)"


def search_definition(repo_dir: str, pattern: str, search_dirs: list[str]) -> list[str]:
    """在指定目录的 .py 文件中搜索 pattern，返回匹配的文件相对路径列表。"""
    repo = Path(repo_dir)
    results = []
    compiled = re.compile(pattern)
    for d in search_dirs:
        target = repo / d
        if not target.exists():
            continue
        for f in sorted(target.rglob("*.py")):
            try:
                text = f.read_text(encoding="utf-8", errors="ignore")
                if compiled.search(text):
                    results.append(str(f.relative_to(repo)))
            except OSError:
                pass
    return results


def auto_map_op(op: dict, repo_dir: str, category: dict) -> dict:
    """
    自动映射 op/test/bench 文件（无需 Claude）：
      - op 文件：搜索 op_classes 中类名的定义
      - test 文件：搜索 test_fns 中函数名的定义，返回 path::fn_name 格式
      - bench 文件：从 manifest 已有的 bench_file 字段
      - kernel 文件：空列表，留给 Claude 填写
    """
    # op 文件
    op_files = []
    for cls in op.get("op_classes", []):
        found = search_definition(repo_dir, rf"\bclass\s+{re.escape(cls)}\b", OP_DIRS)
        op_files.extend(found)
    op_files = sorted(set(op_files))

    # test 文件（带函数名后缀）
    test_entries = []
    for fn in op.get("test_fns", []):
        found = search_definition(repo_dir, rf"\bdef\s+{re.escape(fn)}\b", TEST_DIRS)
        for f in found:
            test_entries.append(f"{f}::{fn}")
    test_entries = sorted(set(test_entries))

    # bench 文件
    bench_files = []
    if bf := op.get("bench_file"):
        bench_files = [bf]

    return {
        "kernel": [],         # Claude 填写
        "op":     op_files,
        "tests":  test_entries,
        "bench":  bench_files,
    }


# ─────────────────────────────────────────────────────────────────────────────
# 2. Claude API — Kernel 文件识别
# ─────────────────────────────────────────────────────────────────────────────

def build_file_mapping_prompt(ops_batch: list[dict], file_tree: str, cat_name: str) -> str:
    """
    构建让 Claude 识别 kernel/test/bench 文件的 prompt。
    ops_batch 中每项已含 auto_files（op 路径由 grep 预填）。
    """
    ops_summary = []
    for op in ops_batch:
        af = op.get("_auto_files", {})
        ops_summary.append(
            f"  - id={op['id']}, name={op['name']}, sub={op.get('sub','')}"
            f", op_files={af.get('op', [])}"
            f", auto_tests={af.get('tests', [])}"
            f", auto_bench={af.get('bench', [])}"
        )
    ops_text = "\n".join(ops_summary)
    excluded_text = ", ".join(EXCLUDED_OPS) if EXCLUDED_OPS else "（暂无）"

    return f"""你在分析 TileOPs 项目（高性能 LLM 算子库，基于 TileLang）的代码结构。

## 代码库 .py 文件列表
```
{file_tree}
```

## 任务
为类别「{cat_name}」下的每个算子找到对应的三类文件：

1. **kernel** — 实际执行 GPU/tile 计算的核心实现文件，通常位于 `tilelang/` 或 `tileops/kernels/` 下，
   与 `tileops/ops/` 下的高层封装（op 文件）区分。

2. **tests** — 测试该算子正确性的测试文件，通常位于 `tests/` 下。
   格式为 `文件路径::函数名`，例如 `tests/ops/test_activation.py::test_relu_op`。
   如果一个文件中有多个测试函数对应同一个算子，全部列出。

3. **bench** — 对该算子做性能基准测试的 benchmark 文件，通常位于 `benchmarks/` 下。
   格式为 `文件路径::函数名`，例如 `benchmarks/ops/bench_activation.py::bench_relu`。
   与 tests 粒度一致，需要定位到具体的 bench 函数。
   如果一个文件中有多个 bench 函数对应同一个算子，全部列出。

## 算子列表（已知 op 封装文件及自动扫描结果）
{ops_text}

## 排除列表
以下算子名不在我们的追踪范围内，它们的文件（kernel/test/bench）**绝对不能**归属到列表中的任何算子：
{excluded_text}

包含这些名称的文件路径（如 `tileops/kernels/engram/`、`test_engram_fwd.py`、`bench_engram_fwd.py`）必须忽略。

## 匹配指南
- 算子名称和文件名可能不完全一致，请根据语义理解匹配
- `auto_tests` 和 `auto_bench` 是自动 grep 的初步结果，可能遗漏或不精确。请在此基础上补充未被发现的测试函数和 benchmark 函数
- 对于测试文件，请仔细判断哪些 test 函数与该算子相关，即使函数名不包含算子名称
- 对于 benchmark 文件，请找出文件中以 `bench_` 开头的函数，判断其与算子的对应关系
- 一个测试/bench 文件可能覆盖多个算子（如 bench_activation.py 覆盖 relu/gelu/silu 等）
- 多个算子共享同一文件时均列出
- 找不到对应文件时对应字段为空列表 []

## 输出前自检（逐条核实，每条都必须通过）
生成结果后，请按以下 checklist 逐一检查并修正：

- [ ] **排除列表过滤**：结果中是否有任何文件路径包含排除列表中的算子名（如 engram）？如有，删除该条目
- [ ] **kernel-test-bench 一致性**：是否有算子的 kernel 为空，但 tests 或 bench 不为空？如有，重新审视：
  - 是否遗漏了该算子的 kernel 文件？重新在文件列表中搜索
  - 如果确实找不到 kernel，说明该 tests/bench 可能不属于这个算子，将 kernel/tests/bench 全部清空为 []
- [ ] **映射归属准确性**：tests 和 bench 中的函数是否确实测试/评测的是该算子，而非另一个同名或相似的算子？

## 输出格式
严格输出 JSON，不含其他文字：
{{
  "mappings": [
    {{
      "id": "ew.activation.relu",
      "kernel": ["tileops/kernels/elementwise.py"],
      "tests": ["tests/ops/test_activation.py::test_relu_op", "tests/ops/test_activation.py::test_relu_strategies"],
      "bench": ["benchmarks/ops/bench_activation.py::bench_relu", "benchmarks/ops/bench_activation.py::bench_relu_strategies"]
    }}
  ]
}}

路径相对于仓库根目录。"""


# ─────────────────────────────────────────────────────────────────────────────
# 3. YAML 生成
# ─────────────────────────────────────────────────────────────────────────────

def _make_op_record(op: dict, files: dict, now_iso: str) -> dict:
    """构造算子的完整数据字典（用于序列化为 YAML）。"""
    return {
        "id":          op["id"],
        "name":        op["name"],
        "category":    op.get("category", ""),
        "category_id": op.get("category_id"),
        "sub":         op.get("sub", ""),
        "issue":       op.get("issue"),

        # 文件映射（Claude 每周维护）
        "files": {
            "kernel": files.get("kernel", []),
            "op":     files.get("op",     []),
            "tests":  files.get("tests",  []),
            "bench":  files.get("bench",  []),
        },
        "files_last_scanned": now_iso,

        # 功能完整性评分（1-5，Claude 每日维护）
        # 1=骨架 2=基础功能 3=主要功能 4=接近完整 5=完整
        "func_score":         None,
        "func_score_notes":   "",
        "func_score_updated": None,

        # 性能评分（1-5，相对 baseline）
        # 1=<50%  2=50-75%  3=75-90%  4=90-100%  5=>100%
        "perf_score": None,
        "perf_details": {
            "baseline": None,
            "last_run": None,
            "summary":  None,
            "results":  [],
        },
        "perf_score_updated": None,

        # Bug 状态（Claude 每日维护）
        "has_bugs": None,
        "bugs":     [],

        # Kernel 文件最近 PR 信息（每日 PR 扫描维护）
        "kernel_last_updated":    None,
        "kernel_last_pr_number":  None,
        "kernel_last_pr_url":     None,
        "kernel_last_pr_author":  None,
        "kernel_last_pr_title":   None,

        # 最新 nightly 测试状态（每日维护）
        "test_status": {
            "last_run": None,
            "passed":   None,
            "errors":   [],
        },

        # 元数据
        "last_updated": now_iso,
        "updated_by":   "bootstrap",
    }


def write_op_yaml(op_data_dir: Path, op_id: str, record: dict) -> None:
    """将算子记录写为 YAML 文件。"""
    path = op_data_dir / f"{op_id}.yaml"
    if HAS_YAML:
        path.write_text(
            _yaml.dump(record, allow_unicode=True, default_flow_style=False,
                       sort_keys=False, width=120),
            encoding="utf-8",
        )
    else:
        # 降级：写 JSON（扩展名仍用 .yaml，内容为 JSON）
        path.write_text(json.dumps(record, ensure_ascii=False, indent=2))


# ─────────────────────────────────────────────────────────────────────────────
# 4. op_registry.json 生成
# ─────────────────────────────────────────────────────────────────────────────

def build_registry(manifest: dict, all_files: dict[str, dict], now_iso: str) -> dict:
    """
    生成 op_registry.json。
    all_files: {op_id: {kernel, op, tests, bench}}
    """
    ops_dict: dict = {}
    for cat in manifest["categories"]:
        for op in cat["ops"]:
            op_id = op["id"]
            files = all_files.get(op_id, {"kernel": [], "op": [], "tests": [], "bench": []})
            ops_dict[op_id] = {
                "id":          op_id,
                "name":        op["name"],
                "category":    cat["name"],
                "category_id": cat["id"],
                "sub":         op.get("sub", ""),
                "issue":       cat.get("issue"),
                "files": {
                    "kernel": files.get("kernel", []),
                    "op":     files.get("op",     []),
                    "tests":  files.get("tests",  []),
                    "bench":  files.get("bench",  []),
                },
                "func_score":            None,
                "perf_score":            None,
                "has_bugs":              None,
                "kernel_last_updated":   None,
                "kernel_last_pr_author": None,
                "last_updated":          now_iso,
            }

    return {
        "schema_version": "2.0",
        "generated_at":   now_iso,
        "total_ops":       manifest["total_ops"],
        "ops":             ops_dict,
    }


# ─────────────────────────────────────────────────────────────────────────────
# 5. 主逻辑
# ─────────────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="初始化 TileOPs 算子注册表（JSON + YAML）"
    )
    parser.add_argument("--manifest",    required=True,
                        help="op_manifest.json 路径")
    parser.add_argument("--repo-dir",    required=True,
                        help="TileOPs 仓库根目录")
    parser.add_argument("--registry",    required=True,
                        help="输出 op_registry.json 路径")
    parser.add_argument("--op-data-dir", required=True,
                        help="输出 op_data/ 目录路径")
    parser.add_argument("--model",       default="claude-sonnet-4-6",
                        help="Claude 模型 ID")
    parser.add_argument("--skip-claude", action="store_true",
                        help="跳过 Claude API（仅自动映射，kernel 为空列表）")
    args = parser.parse_args()

    api_key, base_url = get_api_config()

    if not args.skip_claude and not api_key:
        print("错误：需要设置 ANTHROPIC_API_KEY 或 ANTHROPIC_AUTH_TOKEN", file=sys.stderr)
        print("提示：加 --skip-claude 可跳过 Claude，仅生成文件结构骨架", file=sys.stderr)
        sys.exit(1)

    if not HAS_YAML:
        print("警告：pyyaml 未安装，YAML 文件将以 JSON 格式写入", file=sys.stderr)

    # 加载 manifest
    manifest_path = Path(args.manifest)
    if not manifest_path.exists():
        print(f"错误：manifest 不存在: {args.manifest}", file=sys.stderr)
        sys.exit(1)
    manifest = json.loads(manifest_path.read_text())
    print(f"加载 manifest: {manifest['total_ops']} 个算子，{len(manifest['categories'])} 个类别")

    # 准备输出目录
    op_data_dir = Path(args.op_data_dir)
    op_data_dir.mkdir(parents=True, exist_ok=True)
    Path(args.registry).parent.mkdir(parents=True, exist_ok=True)

    # 扫描代码库文件树（传给 Claude）
    print(f"扫描代码库: {args.repo_dir} ...")
    file_tree = get_compact_tree(args.repo_dir)
    n_files = file_tree.count("\n") + 1
    print(f"  找到 {n_files} 个 .py 文件")

    # 逐类别处理
    all_files: dict[str, dict] = {}   # op_id -> {kernel, op, tests, bench}

    for cat in manifest["categories"]:
        cat_name = cat["name"]
        ops      = cat["ops"]
        print(f"\n[{cat_name}] {len(ops)} 个算子")

        # Step A: 自动映射 op/test/bench
        for op in ops:
            op["category"]    = cat_name
            op["category_id"] = cat["id"]
            op["issue"]       = cat.get("issue")
            op["_auto_files"] = auto_map_op(op, args.repo_dir, cat)

        # Step B: Claude 识别 kernel/test/bench 文件
        claude_map: dict[str, dict] = {}
        if not args.skip_claude and api_key:
            try:
                prompt = build_file_mapping_prompt(ops, file_tree, cat_name)
                data   = call_claude_json(
                    prompt, args.model, api_key, base_url,
                    system=SYSTEM_KERNEL_MAPPER,
                    required_keys=["mappings"],
                    max_tokens=8192,
                )
                for item in data.get("mappings", []):
                    # 硬过滤：排除列表中的文件路径
                    def _filter_excluded(paths: list[str]) -> list[str]:
                        return [p for p in paths
                                if not any(ex in p.lower() for ex in EXCLUDED_OPS)]
                    kernel = _filter_excluded(item.get("kernel", []))
                    tests  = _filter_excluded(item.get("tests", []))
                    bench  = _filter_excluded(item.get("bench", []))
                    # 一致性：无 kernel 则清空 tests/bench
                    if not kernel:
                        tests = []
                        bench = []
                    claude_map[item["id"]] = {
                        "kernel": kernel,
                        "tests":  tests,
                        "bench":  bench,
                    }
                n_kernel = sum(1 for v in claude_map.values() if v["kernel"])
                n_tests  = sum(1 for v in claude_map.values() if v["tests"])
                n_bench  = sum(1 for v in claude_map.values() if v["bench"])
                print(f"  Claude: {n_kernel} kernel, {n_tests} test, {n_bench} bench 映射")
            except Exception as exc:
                print(f"  ⚠ Claude 失败: {exc}", file=sys.stderr)
        else:
            print("  跳过 Claude 文件映射")

        # Step C: 合并 Claude + auto 结果，写 YAML
        # Claude 结果优先；auto grep 结果作为补充
        for op in ops:
            op_id  = op["id"]
            auto   = op["_auto_files"]
            cm     = claude_map.get(op_id, {})
            kernel = cm.get("kernel", [])
            tests  = cm.get("tests", []) or auto["tests"]
            bench  = cm.get("bench", []) or auto["bench"]
            # 一致性：无 kernel 则清空 tests/bench
            if not kernel:
                tests = []
                bench = []
            files  = {
                "kernel": kernel,
                "op":     auto["op"],
                "tests":  tests,
                "bench":  bench,
            }
            all_files[op_id] = files

            record = _make_op_record(op, files, NOW_ISO)
            write_op_yaml(op_data_dir, op_id, record)

        print(f"  YAML 文件已生成: {len(ops)} 个")

    # 生成 op_registry.json
    print("\n生成 op_registry.json ...")
    registry = build_registry(manifest, all_files, NOW_ISO)
    Path(args.registry).write_text(
        json.dumps(registry, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"  {args.registry}  ({len(registry['ops'])} 个算子)")
    print("\n完成！")


if __name__ == "__main__":
    main()
