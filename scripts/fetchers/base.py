from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class StrategyItem:
    source_id: str
    source_name: str
    url: str
    title: str
    published_at: str | None  # ISO-8601 UTC
    content_text: str


@dataclass(frozen=True)
class FetchReport:
    source_id: str
    source_url: str
    ok: bool
    item_count: int
    status_code: int | None = None
    error: str | None = None


USER_AGENT = (
    "quant-strategy-digest/1.0 (+https://github.com/lhjlife-sys/ai_strategy)"
)

MIN_CONTENT_LENGTH = 100

AD_KEYWORDS = (
    "招聘",
    "广告",
    "开户",
    "加微信",
    "扫码",
    "限时优惠",
    "hiring",
    "sponsored",
    "affiliate",
)


def is_low_quality_item(item: StrategyItem) -> bool:
    text = f"{item.title} {item.content_text}".lower()
    if len(item.content_text.strip()) < MIN_CONTENT_LENGTH and len(item.title.strip()) < 20:
        return True
    return any(kw.lower() in text for kw in AD_KEYWORDS)
