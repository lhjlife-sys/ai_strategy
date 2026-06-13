from __future__ import annotations

import re
from urllib.parse import urlparse


def infer_author(item: dict) -> str | None:
    source_id = str(item.get("source_id") or "")
    existing = item.get("author")
    if existing and str(existing).strip():
        return str(existing).strip()

    url = str(item.get("url") or "")
    title = str(item.get("title") or "")
    content = str(item.get("content_text") or item.get("raw_content") or "")

    if source_id == "github_quant" or "github.com" in url:
        author = _github_owner(url, title)
        if author:
            return author

    if source_id == "reddit_algotrading" or "reddit.com" in url:
        author = _reddit_author(url, content)
        if author:
            return author

    if source_id.startswith("arxiv"):
        author = item.get("author")
        if author and str(author).strip():
            return str(author).strip()

    return None


def resolve_author(*, llm_author: str | None, inferred: str | None) -> str:
    if llm_author and str(llm_author).strip():
        return _normalize_author(str(llm_author))
    if inferred and str(inferred).strip():
        return _normalize_author(str(inferred))
    return "未知"


def _normalize_author(name: str) -> str:
    value = name.strip()
    if value.lower().startswith("/u/"):
        return value[3:]
    if value.lower().startswith("u/"):
        return value[2:]
    return value


def _github_owner(url: str, title: str) -> str | None:
    parsed = urlparse(url)
    if parsed.netloc.endswith("github.com"):
        parts = [p for p in parsed.path.split("/") if p]
        if parts:
            return parts[0]
    if "/" in title:
        owner = title.split("/", 1)[0].strip()
        if owner:
            return owner
    return None


def _reddit_author(url: str, content: str) -> str | None:
    match = re.search(r"submitted by /u/([\w-]+)", content, re.IGNORECASE)
    if match:
        return match.group(1)
    match = re.search(r"reddit\.com/u(?:ser)?/([\w-]+)", url, re.IGNORECASE)
    if match:
        return match.group(1)
    match = re.search(r"reddit\.com/r/\w+/comments/\w+/([^/]+)/?", url, re.IGNORECASE)
    return None


def rss_entry_authors(entry: object) -> str | None:
    authors: list[str] = []
    if hasattr(entry, "authors") and entry.authors:
        for author in entry.authors:
            name = getattr(author, "name", None) or getattr(author, "email", None)
            if name:
                authors.append(str(name).strip())
    elif hasattr(entry, "author") and entry.author:
        authors.append(str(entry.author).strip())
    elif hasattr(entry, "author_detail") and entry.author_detail:
        name = getattr(entry.author_detail, "name", None)
        if name:
            authors.append(str(name).strip())
    if not authors:
        return None
    return ", ".join(authors[:5])
