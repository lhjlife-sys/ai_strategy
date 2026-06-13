from __future__ import annotations

from dataclasses import asdict

from .fetchers.base import StrategyItem
from .state_store import item_signature


def strategy_item_to_dict(item: StrategyItem) -> dict:
    d = asdict(item)
    d["sig"] = item_signature(item.url, item.title, item.published_at)
    return d
