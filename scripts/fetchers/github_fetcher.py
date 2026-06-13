from __future__ import annotations

import os
from datetime import datetime, timezone

import requests
import yaml

from .base import FetchReport, StrategyItem, USER_AGENT, is_low_quality_item


def load_scraper_config(config_path: str) -> dict:
    data = yaml.safe_load(open(config_path, "r", encoding="utf-8"))
    return data if isinstance(data, dict) else {}


def fetch_github_repos(config_path: str, timeout: int = 20) -> tuple[list[StrategyItem], FetchReport]:
    cfg = load_scraper_config(config_path).get("github", {})
    source_id = str(cfg.get("id", "github_quant"))
    source_name = str(cfg.get("name", "GitHub Quant Repos"))
    query = str(cfg.get("query", "quantitative trading strategy"))
    per_page = int(cfg.get("per_page", 20))
    api_url = "https://api.github.com/search/repositories"

    token = os.getenv("GITHUB_TOKEN", "").strip()
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/vnd.github+json",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    params = {
        "q": query,
        "sort": "updated",
        "order": "desc",
        "per_page": per_page,
    }

    try:
        resp = requests.get(api_url, headers=headers, params=params, timeout=timeout)
        status = resp.status_code
        resp.raise_for_status()
        data = resp.json()
        items: list[StrategyItem] = []
        for repo in data.get("items", []) or []:
            if not isinstance(repo, dict):
                continue
            url = str(repo.get("html_url") or "").strip()
            title = str(repo.get("full_name") or repo.get("name") or "").strip()
            desc = str(repo.get("description") or "")
            topics = repo.get("topics") or []
            lang = repo.get("language") or ""
            stars = repo.get("stargazers_count", 0)
            updated = repo.get("updated_at")
            published_at = None
            if updated:
                try:
                    dt = datetime.fromisoformat(updated.replace("Z", "+00:00"))
                    published_at = dt.astimezone(timezone.utc).replace(microsecond=0).isoformat()
                except Exception:
                    published_at = None
            content_text = (
                f"{desc}\nTopics: {', '.join(topics)}\nLanguage: {lang}\nStars: {stars}"
            ).strip()
            if not url or not title:
                continue
            owner = str(repo.get("owner", {}).get("login") or "")
            if not owner and "/" in title:
                owner = title.split("/", 1)[0]
            item = StrategyItem(
                source_id=source_id,
                source_name=source_name,
                url=url,
                title=title,
                published_at=published_at,
                content_text=content_text,
                author=owner or None,
            )
            if is_low_quality_item(item):
                continue
            items.append(item)
        return items, FetchReport(
            source_id=source_id,
            source_url=api_url,
            ok=True,
            item_count=len(items),
            status_code=status,
            error=None,
        )
    except Exception as e:
        print(f"[warn] GitHub fetch failed: {e}", flush=True)
        return [], FetchReport(
            source_id=source_id,
            source_url=api_url,
            ok=False,
            item_count=0,
            status_code=None,
            error=str(e),
        )
