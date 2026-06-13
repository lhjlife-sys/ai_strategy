from __future__ import annotations

import re
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
    block = data.get("juejin", {})
    return block if isinstance(block, dict) else {}


def fetch_juejin(config_path: str, timeout: int = 20) -> tuple[list[StrategyItem], FetchReport]:
    cfg = _load_cfg(config_path)
    source_id = str(cfg.get("id", "juejin_quant"))
    source_name = str(cfg.get("name", "Juejin Quant"))
    tag_id = str(cfg.get("tag_id", "254700319141126"))
    api_url = str(cfg.get("api_url", "https://api.juejin.cn/content_api/v1/article/query_tag"))
    delay = float(cfg.get("request_delay_sec", 2))

    headers = {
        "User-Agent": USER_AGENT,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    payload = {
        "tag_id": tag_id,
        "sort_type": 2,
        "cursor": "0",
    }

    try:
        time.sleep(delay)
        resp = requests.post(api_url, headers=headers, json=payload, timeout=timeout)
        status = resp.status_code
        resp.raise_for_status()
        data = resp.json()
        articles = (data.get("data") or []) if isinstance(data, dict) else []
        items: list[StrategyItem] = []

        for entry in articles:
            if not isinstance(entry, dict):
                continue
            article = entry.get("article_info") or entry
            if not isinstance(article, dict):
                continue
            article_id = str(article.get("article_id") or entry.get("article_id") or "")
            title = str(article.get("title") or "").strip()
            brief = str(article.get("brief_content") or article.get("abstract") or "")
            ctime = article.get("ctime")
            published_at = None
            if ctime:
                try:
                    dt = datetime.fromtimestamp(int(ctime), tz=timezone.utc)
                    published_at = dt.replace(microsecond=0).isoformat()
                except Exception:
                    published_at = None
            url = f"https://juejin.cn/post/{article_id}" if article_id else ""
            if not url or not title:
                continue
            item = StrategyItem(
                source_id=source_id,
                source_name=source_name,
                url=url,
                title=title,
                published_at=published_at,
                content_text=brief or title,
            )
            if is_low_quality_item(item):
                continue
            items.append(item)
            if len(items) >= int(cfg.get("max_items", 25)):
                break

        if items:
            return items, FetchReport(
                source_id=source_id,
                source_url=api_url,
                ok=True,
                item_count=len(items),
                status_code=status,
                error=None,
            )

        fallback_url = str(cfg.get("fallback_url", "https://juejin.cn/tag/%E9%87%8F%E5%8C%96"))
        time.sleep(delay)
        html_resp = requests.get(fallback_url, headers={"User-Agent": USER_AGENT}, timeout=timeout)
        html_resp.raise_for_status()
        soup = BeautifulSoup(html_resp.text, "lxml")
        for a in soup.select("a[href*='/post/']"):
            href = a.get("href", "")
            title = a.get_text(" ", strip=True)
            if not re.search(r"/post/\d+", href) or not title:
                continue
            url = href if href.startswith("http") else f"https://juejin.cn{href}"
            item = StrategyItem(
                source_id=source_id,
                source_name=source_name,
                url=url,
                title=title,
                published_at=datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
                content_text=title,
            )
            if is_low_quality_item(item) or any(x.url == url for x in items):
                continue
            items.append(item)
            if len(items) >= int(cfg.get("max_items", 25)):
                break

        return items, FetchReport(
            source_id=source_id,
            source_url=fallback_url,
            ok=True,
            item_count=len(items),
            status_code=html_resp.status_code,
            error=None if items else "empty_after_fallback",
        )
    except Exception as e:
        print(f"[warn] Juejin fetch failed: {e}", flush=True)
        return [], FetchReport(
            source_id=source_id,
            source_url=api_url,
            ok=False,
            item_count=0,
            status_code=None,
            error=str(e),
        )
