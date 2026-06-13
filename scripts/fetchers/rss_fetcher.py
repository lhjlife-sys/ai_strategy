from __future__ import annotations

from datetime import datetime, timezone
from typing import Iterable

import feedparser
import requests
import yaml
from bs4 import BeautifulSoup
from dateutil import parser as date_parser

from ..author_extract import rss_entry_authors
from .base import FetchReport, StrategyItem, USER_AGENT, is_low_quality_item


class Source:
    def __init__(self, id: str, name: str, url: str):
        self.id = id
        self.name = name
        self.url = url


def load_sources(config_path: str) -> list[Source]:
    data = yaml.safe_load(open(config_path, "r", encoding="utf-8"))
    sources = data.get("sources", []) if isinstance(data, dict) else []
    out: list[Source] = []
    for s in sources:
        if not isinstance(s, dict):
            continue
        sid = str(s.get("id", "")).strip()
        name = str(s.get("name", sid)).strip() or sid
        url = str(s.get("url", "")).strip()
        if sid and url:
            out.append(Source(id=sid, name=name, url=url))
    return out


def _html_to_text(html: str) -> str:
    soup = BeautifulSoup(html or "", "html.parser")
    text = soup.get_text(" ", strip=True)
    return " ".join(text.split())


def _parse_datetime_to_utc_iso(value: str | None) -> str | None:
    if not value:
        return None
    try:
        dt = date_parser.parse(value)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        dt = dt.astimezone(timezone.utc).replace(microsecond=0)
        return dt.isoformat()
    except Exception:
        return None


def fetch_all_rss(sources: Iterable[Source], timeout: int = 20) -> tuple[list[StrategyItem], list[FetchReport]]:
    all_items: list[StrategyItem] = []
    reports: list[FetchReport] = []
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/rss+xml, application/xml, text/xml;q=0.9, */*;q=0.8",
    }
    for s in sources:
        try:
            response = requests.get(s.url, headers=headers, timeout=timeout)
            status_code = response.status_code
            response.raise_for_status()
            parsed = feedparser.parse(response.content)
            items: list[StrategyItem] = []
            for e in parsed.entries or []:
                url = (getattr(e, "link", None) or getattr(e, "id", None) or "").strip()
                title = (getattr(e, "title", None) or "").strip()
                published_raw = getattr(e, "published", None) or getattr(e, "updated", None) or None
                published_at = _parse_datetime_to_utc_iso(published_raw)

                content_html = ""
                if hasattr(e, "content") and e.content:
                    try:
                        content_html = e.content[0].value or ""
                    except Exception:
                        content_html = ""
                if not content_html:
                    content_html = getattr(e, "summary", None) or getattr(e, "description", None) or ""

                content_text = _html_to_text(content_html)
                if not url or not title:
                    continue
                item = StrategyItem(
                    source_id=s.id,
                    source_name=s.name,
                    url=url,
                    title=title,
                    published_at=published_at,
                    content_text=content_text,
                    author=rss_entry_authors(e),
                )
                if is_low_quality_item(item):
                    continue
                items.append(item)
            all_items.extend(items)
            reports.append(
                FetchReport(
                    source_id=s.id,
                    source_url=s.url,
                    ok=True,
                    item_count=len(items),
                    status_code=status_code,
                    error=None,
                )
            )
        except Exception as e:
            print(f"[warn] failed to fetch RSS source {s.id} ({s.url}): {e}", flush=True)
            reports.append(
                FetchReport(
                    source_id=s.id,
                    source_url=s.url,
                    ok=False,
                    item_count=0,
                    status_code=None,
                    error=str(e),
                )
            )
    return all_items, reports


def sort_items_newest_first(items: Iterable[StrategyItem]) -> list[StrategyItem]:
    def key(i: StrategyItem) -> tuple[int, str]:
        if i.published_at is None:
            return (0, "")
        try:
            dt = datetime.fromisoformat(i.published_at)
            return (1, dt.isoformat())
        except Exception:
            return (0, "")

    return sorted(list(items), key=key, reverse=True)
