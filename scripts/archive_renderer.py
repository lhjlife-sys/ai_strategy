from __future__ import annotations

from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

from dateutil import tz

from .db_store import fetch_all_strategies
from .utils import utc_now_iso


STRATEGY_TYPE_LABELS = {
    "trend": "趋势跟踪",
    "mean_reversion": "均值回归",
    "arbitrage": "套利",
    "factor": "因子",
    "ml": "机器学习",
    "options": "期权",
    "market_making": "做市",
    "multi": "综合/其他",
}


def _format_dt(value: str | None, timezone_name: str, *, fallback: str = "—") -> str:
    if not value:
        return fallback
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        local_tz = tz.gettz(timezone_name)
        if local_tz is not None:
            dt = dt.astimezone(local_tz)
        return dt.replace(microsecond=0).strftime("%Y-%m-%d %H:%M")
    except Exception:
        return value[:16] if len(value) >= 16 else value


def _month_key(processed_at: str | None) -> str:
    if not processed_at or len(processed_at) < 7:
        return "unknown"
    return processed_at[:7]


def _display_title(item: dict[str, Any]) -> str:
    return str(item.get("translated_title") or item.get("title") or "未命名策略")


def _slug_heading(text: str) -> str:
    return text.replace("\n", " ").strip()


def _render_entry(item: dict[str, Any], *, timezone_name: str) -> str:
    title = _display_title(item)
    strategy_type = STRATEGY_TYPE_LABELS.get(
        str(item.get("strategy_type") or "multi"),
        str(item.get("strategy_type") or "multi"),
    )
    asset_class = item.get("asset_class") or "multi"
    market = item.get("market") or "global"
    key_points = item.get("key_points") or []
    points_block = ""
    if key_points:
        points_block = "\n".join(f"  - {p}" for p in key_points)

    lines = [
        f"### {_slug_heading(title)}",
        "",
        f"- **收录时间**：{_format_dt(item.get('processed_at'), timezone_name)}",
        f"- **发布时间**：{_format_dt(item.get('published_at'), timezone_name)}",
        f"- **作者**：{item.get('author') or '未知'}",
        f"- **来源**：{item.get('source_name') or '—'}",
        f"- **分类**：{strategy_type} · {asset_class} · {market}",
    ]
    if item.get("frequency"):
        lines.append(f"- **频率**：{item['frequency']}")
    if item.get("translated_summary"):
        lines.append(f"- **摘要**：{item['translated_summary']}")
    if points_block:
        lines.append("- **要点**：")
        lines.append(points_block)
    if item.get("backtest_hint"):
        lines.append(f"- **回测线索**：{item['backtest_hint']}")
    if item.get("risk_notes"):
        lines.append(f"- **风险**：{item['risk_notes']}")
    if item.get("why_it_matters"):
        lines.append(f"- **策略价值**：{item['why_it_matters']}")
    if item.get("selection_score"):
        lines.append(f"- **筛选评分**：{item['selection_score']}")
    url = item.get("url") or ""
    if url:
        lines.append(f"- **原文**：[链接]({url})")
    lines.append("")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def render_strategy_archive_md(
    db_path: str | Path,
    *,
    timezone: str,
    output_path: str | Path,
) -> int:
    items = fetch_all_strategies(db_path)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in items:
        grouped[_month_key(item.get("processed_at"))].append(item)

    months = sorted(grouped.keys(), reverse=True)
    now_local = _format_dt(utc_now_iso(), timezone)

    parts = [
        "# 量化策略汇总",
        "",
        f"> 自动生成 · 最后更新：{now_local} · {timezone}",
        f"> 共 {len(items)} 条策略",
        "",
        "## 目录",
        "",
    ]

    for month in months:
        if month == "unknown":
            label = "未分类"
            anchor = "unknown"
        else:
            label = month
            anchor = month
        parts.append(f"- [{label}（{len(grouped[month])}）](#{anchor})")
    parts.extend(["", "---", ""])

    for month in months:
        if month == "unknown":
            parts.extend(["## 未分类", ""])
        else:
            parts.extend([f"## {month}", ""])
        for item in grouped[month]:
            parts.append(_render_entry(item, timezone_name=timezone))

    output_path.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
    return len(items)
