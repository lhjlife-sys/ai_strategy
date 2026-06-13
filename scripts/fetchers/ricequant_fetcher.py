from __future__ import annotations

import time
from datetime import datetime, timezone

import requests
import yaml
from bs4 import BeautifulSoup

from .base import FetchReport, StrategyItem, USER_AGENT, is_low_quality_item


def _load_cfg(config_path: str) -> dict:
    data = yaml.safe_load(open(config_path, "r", encoding="utf-8"))
    if not isinstance(data, dict):
        return {}
    block = data.get("ricequant", {})
    return block if isinstance(block, dict) else {}


def fetch_ricequant(config_path: str, timeout: int = 20) -> tuple[list[StrategyItem], FetchReport]:
    cfg = _load_cfg(config_path)
    source_id = str(cfg.get("id", "ricequant_community"))
    source_name = str(cfg.get("name", "RiceQuant Community"))
    list_url = str(cfg.get("list_url", "https://www.ricequant.com/community/"))
    delay = float(cfg.get("request_delay_sec", 2))

    headers = {"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml"}
    items: list[StrategyItem] = []

    try:
        time.sleep(delay)
        resp = requests.get(list_url, headers=headers, timeout=timeout)
        status = resp.status_code
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "lxml")

        selectors = [
            "a[href*='/community/topic/']",
            "a[href*='/community/post/']",
            "a[href*='/community/']",
        ]
        seen_urls: set[str] = set()
        for sel in selectors:
            for a in soup.select(sel):
                href = a.get("href", "")
                title = a.get_text(" ", strip=True)
                if not href or not title or len(title) < 8:
                    continue
                url = href if href.startswith("http") else f"https://www.ricequant.com{href}"
                if url in seen_urls or url.rstrip("/") == list_url.rstrip("/"):
                    continue
                seen_urls.add(url)
                parent = a.find_parent(["div", "li", "article"])
                snippet = parent.get_text(" ", strip=True)[:600] if parent else title
                item = StrategyItem(
                    source_id=source_id,
                    source_name=source_name,
                    url=url,
                    title=title,
                    published_at=datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
                    content_text=snippet,
                )
                if is_low_quality_item(item):
                    continue
                items.append(item)
                if len(items) >= int(cfg.get("max_items", 25)):
                    break
            if len(items) >= int(cfg.get("max_items", 25)):
                break

        return items, FetchReport(
            source_id=source_id,
            source_url=list_url,
            ok=True,
            item_count=len(items),
            status_code=status,
            error=None if items else "no_items_parsed",
        )
    except Exception as e:
        print(f"[warn] RiceQuant fetch failed: {e}", flush=True)
        return [], FetchReport(
            source_id=source_id,
            source_url=list_url,
            ok=False,
            item_count=0,
            status_code=None,
            error=str(e),
        )
