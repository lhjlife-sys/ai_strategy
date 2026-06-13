from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Iterable

from .utils import utc_now_iso


SCHEMA = """
CREATE TABLE IF NOT EXISTS strategies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sig TEXT UNIQUE NOT NULL,
    source_id TEXT,
    source_name TEXT,
    url TEXT,
    title TEXT,
    published_at TEXT,
    raw_content TEXT,
    strategy_type TEXT,
    asset_class TEXT,
    market TEXT,
    frequency TEXT,
    data_requirements TEXT,
    backtest_hint TEXT,
    risk_notes TEXT,
    translated_title TEXT,
    translated_summary TEXT,
    key_points TEXT,
    why_it_matters TEXT,
    selection_score INTEGER,
    selection_reason TEXT,
    fetched_at TEXT,
    processed_at TEXT,
    emailed_at TEXT
);
CREATE INDEX IF NOT EXISTS idx_strategies_published ON strategies(published_at);
CREATE INDEX IF NOT EXISTS idx_strategies_type ON strategies(strategy_type);
"""


def init_db(path: str | Path) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(p) as conn:
        conn.executescript(SCHEMA)


def upsert_strategies(path: str | Path, rows: Iterable[dict]) -> int:
    init_db(path)
    now = utc_now_iso()
    count = 0
    with sqlite3.connect(path) as conn:
        for row in rows:
            sig = str(row.get("sig") or "")
            if not sig:
                continue
            key_points = row.get("key_points") or []
            data_req = row.get("data_requirements") or []
            conn.execute(
                """
                INSERT INTO strategies (
                    sig, source_id, source_name, url, title, published_at, raw_content,
                    strategy_type, asset_class, market, frequency, data_requirements,
                    backtest_hint, risk_notes, translated_title, translated_summary,
                    key_points, why_it_matters, selection_score, selection_reason,
                    fetched_at, processed_at, emailed_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(sig) DO UPDATE SET
                    source_id=excluded.source_id,
                    source_name=excluded.source_name,
                    url=excluded.url,
                    title=excluded.title,
                    published_at=excluded.published_at,
                    raw_content=excluded.raw_content,
                    strategy_type=excluded.strategy_type,
                    asset_class=excluded.asset_class,
                    market=excluded.market,
                    frequency=excluded.frequency,
                    data_requirements=excluded.data_requirements,
                    backtest_hint=excluded.backtest_hint,
                    risk_notes=excluded.risk_notes,
                    translated_title=excluded.translated_title,
                    translated_summary=excluded.translated_summary,
                    key_points=excluded.key_points,
                    why_it_matters=excluded.why_it_matters,
                    selection_score=excluded.selection_score,
                    selection_reason=excluded.selection_reason,
                    processed_at=excluded.processed_at,
                    emailed_at=COALESCE(strategies.emailed_at, excluded.emailed_at)
                """,
                (
                    sig,
                    row.get("source_id"),
                    row.get("source_name"),
                    row.get("url"),
                    row.get("title"),
                    row.get("published_at"),
                    (row.get("raw_content") or row.get("content_text") or "")[:8192],
                    row.get("strategy_type"),
                    row.get("asset_class"),
                    row.get("market"),
                    row.get("frequency"),
                    json.dumps(data_req, ensure_ascii=False),
                    row.get("backtest_hint"),
                    row.get("risk_notes"),
                    row.get("translated_title"),
                    row.get("translated_summary"),
                    json.dumps(key_points, ensure_ascii=False),
                    row.get("why_it_matters"),
                    row.get("selection_score"),
                    row.get("selection_reason"),
                    row.get("fetched_at") or now,
                    now,
                    row.get("emailed_at"),
                ),
            )
            count += 1
        conn.commit()
    return count


def mark_emailed(path: str | Path, sigs: Iterable[str]) -> None:
    now = utc_now_iso()
    with sqlite3.connect(path) as conn:
        for sig in sigs:
            if sig:
                conn.execute(
                    "UPDATE strategies SET emailed_at = ? WHERE sig = ?",
                    (now, sig),
                )
        conn.commit()
