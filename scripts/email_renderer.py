from __future__ import annotations

from collections import defaultdict
from datetime import datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

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


def group_items_by_strategy_type(items: list[dict]) -> list[dict]:
    groups: dict[str, list[dict]] = defaultdict(list)
    for it in items:
        stype = str(it.get("strategy_type") or "multi")
        groups[stype].append(it)
    ordered_types = sorted(groups.keys(), key=lambda k: (k == "multi", k))
    return [
        {
            "strategy_type": t,
            "label": STRATEGY_TYPE_LABELS.get(t, t),
            "entries": groups[t],
        }
        for t in ordered_types
    ]


def render_digest_html(
    *,
    template_path: str | Path,
    subject: str,
    generated_at: str,
    timezone: str,
    items: list[dict],
    token_usage_summary: str | None = None,
    schedule_summary: str | None = None,
) -> str:
    template_path = Path(template_path)
    env = Environment(
        loader=FileSystemLoader(str(template_path.parent)),
        autoescape=select_autoescape(enabled_extensions=("html", "xml", "j2")),
    )
    tmpl = env.get_template(template_path.name)
    return tmpl.render(
        subject=subject,
        generated_at=generated_at,
        timezone=timezone,
        items=items,
        grouped_items=group_items_by_strategy_type(items),
        strategy_type_labels=STRATEGY_TYPE_LABELS,
        token_usage_summary=token_usage_summary,
        schedule_summary=schedule_summary,
        now=datetime.utcnow(),
    )
