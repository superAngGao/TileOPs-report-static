#!/usr/bin/env python3
"""claude_utils.py — Claude API 调用的共享工具模块。

提供统一的 API 调用、JSON 提取与校验，供 analyze_report.py、
update_registry.py、bootstrap_registry.py 共同使用。
"""

import json
import os
import re
import sys
import time
from typing import Any

# ---------------------------------------------------------------------------
# 1. 环境变量读取
# ---------------------------------------------------------------------------

def get_api_config() -> tuple[str | None, str | None]:
    """返回 (api_key, base_url)，优先 ANTHROPIC_API_KEY。"""
    api_key = os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_AUTH_TOKEN")
    base_url = os.environ.get("ANTHROPIC_BASE_URL")
    return api_key, base_url


def require_anthropic():
    """导入 anthropic 包，不可用时打印警告并返回 None。"""
    try:
        import anthropic
        return anthropic
    except ImportError:
        print("::warning::anthropic package not installed — skipping Claude calls.",
              file=sys.stderr)
        return None


# ---------------------------------------------------------------------------
# 2. Claude API 调用（带 system prompt、temperature、重试）
# ---------------------------------------------------------------------------

def call_claude(
    prompt: str,
    model: str,
    api_key: str,
    base_url: str | None,
    *,
    system: str | None = None,
    max_tokens: int = 4096,
    temperature: float = 0.0,
    max_retries: int = 2,
) -> str:
    """调用 Claude Messages API，返回文本响应。

    Args:
        prompt:      用户消息内容
        model:       模型 ID
        api_key:     API 密钥
        base_url:    可选的代理 URL
        system:      可选的 system prompt（控制角色和输出行为）
        max_tokens:  最大输出 token 数
        temperature: 采样温度（结构化输出建议 0.0）
        max_retries: 最大重试次数（针对瞬时错误）

    Returns:
        Claude 的文本响应

    Raises:
        Exception: API 调用在所有重试后仍失败
    """
    import anthropic

    client_kwargs: dict = {"api_key": api_key}
    if base_url:
        client_kwargs["base_url"] = base_url
    client = anthropic.Anthropic(**client_kwargs)

    create_kwargs: dict[str, Any] = {
        "model": model,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "messages": [{"role": "user", "content": prompt}],
    }
    if system:
        create_kwargs["system"] = system

    last_exc: Exception | None = None
    for attempt in range(1, max_retries + 1):
        try:
            msg = client.messages.create(**create_kwargs)
            return msg.content[0].text
        except anthropic.APIStatusError as exc:
            # 4xx 客户端错误不重试（除 429 限流）
            if exc.status_code != 429 and 400 <= exc.status_code < 500:
                raise
            last_exc = exc
            wait = min(2 ** attempt, 8)
            print(f"  Claude API 暂时失败 (attempt {attempt}/{max_retries}): "
                  f"{exc.status_code} — 等待 {wait}s 后重试",
                  file=sys.stderr)
            time.sleep(wait)
        except anthropic.APIConnectionError as exc:
            last_exc = exc
            wait = min(2 ** attempt, 8)
            print(f"  Claude API 连接失败 (attempt {attempt}/{max_retries}): "
                  f"{exc} — 等待 {wait}s 后重试",
                  file=sys.stderr)
            time.sleep(wait)

    raise last_exc  # type: ignore[misc]


# ---------------------------------------------------------------------------
# 3. JSON 提取与校验
# ---------------------------------------------------------------------------

def extract_json(text: str) -> dict:
    """从 Claude 响应中提取 JSON 对象。

    依次尝试：
      1. 直接 JSON.parse 整段文本
      2. 提取 ```json ... ``` 代码块
      3. 提取最外层 { ... }

    Raises:
        ValueError: 无法提取有效 JSON
    """
    # 1. 直接解析
    stripped = text.strip()
    try:
        return json.loads(stripped)
    except json.JSONDecodeError:
        pass

    # 2. 代码块
    m = re.search(r"```(?:json)?\s*(\{[\s\S]*?\})\s*```", text)
    if m:
        try:
            return json.loads(m.group(1))
        except json.JSONDecodeError:
            pass

    # 3. 最外层大括号
    m = re.search(r"(\{[\s\S]*\})", text)
    if m:
        try:
            return json.loads(m.group(1))
        except json.JSONDecodeError:
            pass

    raise ValueError(f"无法从 Claude 响应中提取 JSON:\n{text[:400]}")


def validate_json(data: dict, required_keys: list[str], context: str = "") -> bool:
    """校验 JSON 对象是否包含所有必需字段。

    Args:
        data:          待校验的字典
        required_keys: 必需的顶层字段名列表
        context:       用于错误消息的上下文描述

    Returns:
        True 如果校验通过

    Raises:
        ValueError: 缺少必需字段
    """
    missing = [k for k in required_keys if k not in data]
    if missing:
        ctx = f" ({context})" if context else ""
        raise ValueError(f"Claude 输出缺少必需字段{ctx}: {missing}")
    return True


def call_claude_json(
    prompt: str,
    model: str,
    api_key: str,
    base_url: str | None,
    *,
    system: str | None = None,
    required_keys: list[str] | None = None,
    max_tokens: int = 4096,
    max_retries: int = 2,
) -> dict:
    """调用 Claude 并直接返回解析后的 JSON 字典。

    组合了 call_claude + extract_json + validate_json。
    自动设置 temperature=0.0 以提高结构化输出稳定性。

    Args:
        prompt:        用户消息
        model:         模型 ID
        api_key:       API 密钥
        base_url:      可选代理 URL
        system:        可选 system prompt
        required_keys: 可选的 JSON 顶层必需字段列表
        max_tokens:    最大输出 token
        max_retries:   API 重试次数

    Returns:
        解析后的 JSON 字典
    """
    response = call_claude(
        prompt, model, api_key, base_url,
        system=system,
        max_tokens=max_tokens,
        temperature=0.0,
        max_retries=max_retries,
    )
    data = extract_json(response)
    if required_keys:
        validate_json(data, required_keys)
    return data


# ---------------------------------------------------------------------------
# 4. 预定义 System Prompts
# ---------------------------------------------------------------------------

SYSTEM_REPORT_ANALYZER = (
    "You are a senior CI/DevOps engineer reviewing nightly test reports for TileOPs, "
    "a high-performance LLM operator library built on TileLang. "
    "Write concise, actionable analysis in English Markdown. "
    "Use ## Section headers and bullet lists. No greetings or preamble."
)

SYSTEM_SCORE_EVALUATOR = (
    "你是 TileOPs 项目的代码质量评估专家。"
    "根据提供的测试结果、benchmark 数据和 PR 信息，为算子评分。"
    "严格按照指定的 JSON 格式输出，不要输出任何 JSON 以外的文字。"
)

SYSTEM_KERNEL_MAPPER = (
    "你是 TileOPs 项目的代码结构分析专家。"
    "根据代码库文件列表和算子元信息，识别每个算子对应的 kernel 实现文件、"
    "测试文件（含具体测试函数名）以及 benchmark 文件（含具体 bench 函数名）。"
    "严格按照指定的 JSON 格式输出，不要输出任何 JSON 以外的文字。"
)
