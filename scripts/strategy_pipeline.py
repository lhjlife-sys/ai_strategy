from __future__ import annotations

import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

from dateutil import tz
import yaml
from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

load_dotenv(REPO_ROOT / ".env")

from scripts.ai_processor import TokenUsage, classify_and_summarize, select_items  # noqa: E402
from scripts.archive_renderer import render_strategy_archive_md  # noqa: E402
from scripts.author_extract import infer_author, resolve_author  # noqa: E402
from scripts.db_store import mark_emailed, upsert_strategies  # noqa: E402
from scripts.email_renderer import render_digest_html  # noqa: E402
from scripts.email_sender_smtp import send_email_smtp  # noqa: E402
from scripts.fetchers.github_fetcher import fetch_github_repos  # noqa: E402
from scripts.fetchers.joinquant_fetcher import fetch_joinquant  # noqa: E402
from scripts.fetchers.juejin_fetcher import fetch_juejin  # noqa: E402
from scripts.fetchers.ricequant_fetcher import fetch_ricequant  # noqa: E402
from scripts.fetchers.rss_fetcher import fetch_all_rss, load_sources, sort_items_newest_first  # noqa: E402
from scripts.normalize import strategy_item_to_dict  # noqa: E402
from scripts.run_log_store import load_dedup_signatures_from_logs, trim_old_logs, write_run_log  # noqa: E402
from scripts.state_store import filter_new_items, load_state, mark_sent, save_state  # noqa: E402
from scripts.utils import getenv_int, getenv_str, utc_now_iso, write_json  # noqa: E402


def _log(msg: str) -> None:
    print(msg, flush=True)


def _load_yaml(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data if isinstance(data, dict) else {}


EXCLUDE_KEYWORDS = (
    "hiring",
    "job opening",
    "recruitment",
    "sponsored",
    "giveaway",
    "coupon",
    "招聘",
    "广告",
    "开户送",
)

TOPIC_KEYWORDS = (
    ("trend", ("trend", "momentum", "breakout", "moving average", "均线", "趋势")),
    ("mean_reversion", ("mean reversion", "reversal", "bollinger", "均值回归", "反转")),
    ("arbitrage", ("arbitrage", "spread", "pairs", "套利", "价差")),
    ("factor", ("factor", "alpha", "beta", "value", "momentum factor", "因子")),
    ("ml", ("machine learning", "deep learning", "lstm", "xgboost", "神经网络", "机器学习")),
    ("options", ("option", "volatility", "greeks", "期权", "波动率")),
    ("crypto", ("bitcoin", "crypto", "ethereum", "区块链")),
)


def _item_search_text(item: dict) -> str:
    parts = [
        item.get("title", ""),
        item.get("source_name", ""),
        item.get("content_text", ""),
    ]
    return " ".join(str(p) for p in parts if p).lower()


def _exclude_reason(item: dict) -> str | None:
    text = _item_search_text(item)
    for kw in EXCLUDE_KEYWORDS:
        if kw.lower() in text:
            return f"excluded_keyword:{kw}"
    return None


def _filter_excluded_items(items: list[dict]) -> tuple[list[dict], list[dict]]:
    kept, excluded = [], []
    for item in items:
        reason = _exclude_reason(item)
        if reason:
            excluded.append({**item, "exclude_reason": reason})
        else:
            kept.append(item)
    return kept, excluded


def _topic_cluster(item: dict) -> str:
    text = _item_search_text(item)
    for label, keywords in TOPIC_KEYWORDS:
        if any(kw in text for kw in keywords):
            return label
    return "misc"


def _balanced_candidate_sample(items: list[dict], limit: int) -> list[dict]:
    if limit <= 0:
        return []
    source_groups: dict[str, list[dict]] = defaultdict(list)
    source_order: list[str] = []
    for item in items:
        source = str(item.get("source_name") or item.get("source_id") or "unknown")
        if source not in source_groups:
            source_order.append(source)
        source_groups[source].append(item)

    sampled: list[dict] = []
    positions = {s: 0 for s in source_order}
    while len(sampled) < limit:
        progressed = False
        for source in source_order:
            bucket = source_groups[source]
            pos = positions[source]
            if pos < len(bucket):
                sampled.append(bucket[pos])
                positions[source] += 1
                progressed = True
            if len(sampled) >= limit:
                break
        if not progressed:
            break
    return sampled


def _schedule_summary_from_github_event(*, timezone_name: str) -> str | None:
    if os.getenv("GITHUB_EVENT_NAME") != "schedule":
        return None
    event_path = os.getenv("GITHUB_EVENT_PATH")
    if not event_path:
        return None
    try:
        with open(event_path, "r", encoding="utf-8") as f:
            event = json.load(f)
    except Exception:
        return None
    cron = str(event.get("schedule") or "").strip()
    parts = cron.split()
    if len(parts) != 5:
        return None
    minute, hour, day_of_month, month, day_of_week = parts
    if not (minute.isdigit() and hour.isdigit()):
        return f"计划触发：{cron} UTC"
    if (day_of_month, month, day_of_week) != ("*", "*", "*"):
        return f"计划触发：{cron} UTC"
    local_tz = tz.gettz(timezone_name)
    if local_tz is None:
        return f"计划触发：{cron} UTC"
    try:
        import datetime as _dt

        utc_dt = _dt.datetime.now(tz=_dt.timezone.utc).replace(
            hour=int(hour), minute=int(minute), second=0, microsecond=0
        )
        local_dt = utc_dt.astimezone(local_tz)
    except Exception:
        return f"计划触发：{cron} UTC"
    return f"计划触发：每日 {local_dt.strftime('%H:%M')} · {timezone_name}（cron: {cron} UTC）"


def _format_token_usage_summary(
    *,
    selection_model: str,
    selection_usage: TokenUsage,
    classification_model: str,
    classification_usage: TokenUsage,
) -> str:
    return (
        "本次运行 token 消耗："
        f"selection({selection_model}) input {selection_usage.input_tokens}, output {selection_usage.output_tokens}；"
        f"classification({classification_model}) input {classification_usage.input_tokens}, output {classification_usage.output_tokens}。"
    )


def fetch_all_sources(sources_path: str, scrapers_path: str) -> tuple[list[dict], list[dict]]:
    all_items: list[dict] = []
    reports: list[dict] = []

    rss_sources = load_sources(sources_path)
    if rss_sources:
        rss_items, rss_reports = fetch_all_rss(rss_sources)
        all_items.extend(strategy_item_to_dict(i) for i in sort_items_newest_first(rss_items))
        reports.extend(r.__dict__ for r in rss_reports)

    gh_items, gh_report = fetch_github_repos(scrapers_path)
    all_items.extend(strategy_item_to_dict(i) for i in gh_items)
    reports.append(gh_report.__dict__)

    for fetch_fn in (fetch_joinquant, fetch_juejin, fetch_ricequant):
        cn_items, cn_report = fetch_fn(scrapers_path)
        all_items.extend(strategy_item_to_dict(i) for i in cn_items)
        reports.append(cn_report.__dict__)

    return all_items, reports


def main() -> int:
    sources_path = getenv_str("SOURCES_CONFIG", str(REPO_ROOT / "config" / "sources.yaml"))
    scrapers_path = getenv_str("SCRAPERS_CONFIG", str(REPO_ROOT / "config" / "scrapers.yaml"))
    prompts_path = getenv_str("PROMPTS_CONFIG", str(REPO_ROOT / "config" / "prompts.yaml"))
    settings_path = getenv_str("SETTINGS_CONFIG", str(REPO_ROOT / "config" / "settings.yaml"))
    state_path = getenv_str("STATE_PATH", str(REPO_ROOT / "state" / "sent_items.json"))
    db_path = getenv_str("DB_PATH", str(REPO_ROOT / "data" / "strategies.db"))
    template_path = getenv_str("TEMPLATE_PATH", str(REPO_ROOT / "templates" / "strategy_digest.html.j2"))
    logs_dir = getenv_str("LOGS_DIR", str(REPO_ROOT / "logs"))

    max_candidates = getenv_int("MAX_CANDIDATES", 80)
    max_selected = getenv_int("MAX_SELECTED", 15)
    min_match_score = getenv_int("MIN_MATCH_SCORE", 50)
    max_per_source = getenv_int("MAX_PER_SOURCE", 2)
    batch_size = getenv_int("CLASSIFICATION_BATCH_SIZE", getenv_int("TRANSLATION_BATCH_SIZE", 3))
    target_language = getenv_str("TARGET_LANGUAGE", "zh-CN")
    timezone_name = getenv_str("TIMEZONE", "Asia/Shanghai")
    api_mode = getenv_str("OPENAI_API_MODE", "chat").strip().lower()
    selection_model = getenv_str("SELECTION_MODEL", "deepseek-v4-flash")
    classification_model = getenv_str(
        "CLASSIFICATION_MODEL",
        getenv_str("TRANSLATION_MODEL", selection_model),
    )
    dry_run = getenv_str("DRY_RUN", "").lower() in {"1", "true", "yes"}

    email_to = os.getenv("EMAIL_TO", "")
    email_from = os.getenv("EMAIL_FROM", "")

    prompts = _load_yaml(prompts_path)
    settings = _load_yaml(settings_path)
    pipeline_cfg = settings.get("pipeline", {})
    user_preference = getenv_str(
        "USER_PREFERENCE",
        str(pipeline_cfg.get("user_preference", "")),
    )

    selection_cfg = prompts.get("selection", {})
    classification_cfg = prompts.get("classification", {})
    selection_system = str(selection_cfg.get("system", "")).strip()
    selection_user = str(selection_cfg.get("user", "")).strip()
    classification_system = str(classification_cfg.get("system", "")).strip()
    classification_user = str(classification_cfg.get("user", "")).strip()
    if not all([selection_system, selection_user, classification_system, classification_user]):
        raise RuntimeError("Invalid prompts config: selection and classification prompts are required.")

    normalized, fetch_reports = fetch_all_sources(sources_path, scrapers_path)
    _log(f"Fetched {len(normalized)} total strategy items.")

    state = load_state(state_path)
    new_items = filter_new_items(normalized, state)
    log_sigs = load_dedup_signatures_from_logs(logs_dir)
    new_items = [it for it in new_items if it.get("sig") not in log_sigs]
    _log(f"After dedup: {len(new_items)} new items.")

    eligible_items, excluded_items = _filter_excluded_items(new_items)
    candidates = _balanced_candidate_sample(eligible_items, max_candidates)
    _log(
        f"Candidate filtering: {len(excluded_items)} excluded, "
        f"{len(candidates)} balanced candidates from {len(eligible_items)} eligible."
    )

    selected: list[dict] = []
    classified: list[dict] = []
    selection_token_usage = TokenUsage(api_mode=api_mode)
    classification_token_usage = TokenUsage(api_mode=api_mode)
    evaluation_logs: list[dict] = []

    if candidates:
        selection_res = select_items(
            candidates,
            model=selection_model,
            max_selected=max_selected,
            topic_hint=user_preference,
            system_prompt=selection_system,
            user_prompt_template=selection_user,
            api_mode=api_mode,
        )
        selection_token_usage = selection_res.token_usage
        selected_by_index = {item.index: item for item in selection_res.items}

        source_counts: Counter[str] = Counter()
        for idx, meta in sorted(selected_by_index.items(), key=lambda x: x[1].score, reverse=True):
            if idx >= len(candidates):
                continue
            it = candidates[idx]
            if meta.score < min_match_score:
                continue
            source = str(it.get("source_name") or "unknown")
            if source_counts[source] >= max_per_source:
                continue
            source_counts[source] += 1
            selected.append(
                {
                    **it,
                    "selection_score": meta.score,
                    "selection_reason": meta.reason,
                }
            )
            evaluation_logs.append(
                {
                    "sig": it.get("sig"),
                    "title": it.get("title"),
                    "score": meta.score,
                    "reason": meta.reason,
                }
            )
            if len(selected) >= max_selected:
                break

        _log(f"Selected {len(selected)} items after LLM selection and source caps.")

        for idx, it in enumerate(selected):
            selected[idx] = {**it, "author": infer_author(it)}

        if selected:
            try:
                class_res = classify_and_summarize(
                    selected,
                    model=classification_model,
                    target_language=target_language,
                    system_prompt=classification_system,
                    user_prompt_template=classification_user,
                    api_mode=api_mode,
                    batch_size=batch_size,
                )
                classification_token_usage = class_res.token_usage
                for idx, item in enumerate(class_res.items):
                    orig = selected[idx] if idx < len(selected) else {}
                    classified.append(
                        {
                            "sig": item.sig,
                            "source_id": orig.get("source_id"),
                            "source_name": item.source_name,
                            "url": item.url,
                            "title": item.title,
                            "published_at": item.published_at,
                            "raw_content": orig.get("content_text", ""),
                            "content_text": orig.get("content_text", ""),
                            "strategy_type": item.strategy_type,
                            "asset_class": item.asset_class,
                            "market": item.market,
                            "frequency": item.frequency,
                            "data_requirements": item.data_requirements,
                            "backtest_hint": item.backtest_hint,
                            "risk_notes": item.risk_notes,
                            "translated_title": item.translated_title,
                            "translated_summary": item.translated_summary,
                            "key_points": item.key_points,
                            "why_it_matters": item.why_it_matters,
                            "author": resolve_author(
                                llm_author=item.author,
                                inferred=orig.get("author"),
                            ),
                            "selection_score": orig.get("selection_score", 0),
                            "selection_reason": orig.get("selection_reason", ""),
                        }
                    )
            except Exception as e:
                _log(f"[warn] classification_failed: {e}")
                for it in selected:
                    content = (it.get("content_text", "") or it.get("title", ""))[:500]
                    classified.append(
                        {
                            **it,
                            "strategy_type": "multi",
                            "asset_class": "multi",
                            "market": "global",
                            "frequency": None,
                            "data_requirements": [],
                            "backtest_hint": None,
                            "risk_notes": None,
                            "translated_title": it.get("title"),
                            "translated_summary": content,
                            "key_points": [],
                            "why_it_matters": None,
                            "author": resolve_author(llm_author=None, inferred=it.get("author")),
                            "raw_content": it.get("content_text", ""),
                            "classification_error": str(e),
                        }
                    )

            db_count = upsert_strategies(db_path, classified)
            _log(f"Upserted {db_count} rows into {db_path}.")

    archive_path = getenv_str("ARCHIVE_PATH", str(REPO_ROOT / "docs" / "strategy_archive.md"))
    archive_count = render_strategy_archive_md(
        db_path,
        timezone=timezone_name,
        output_path=archive_path,
    )
    _log(f"Updated archive: {archive_path} ({archive_count} strategies)")

    processed = classified
    subject_date = utc_now_iso()[:10]
    subject = getenv_str("EMAIL_SUBJECT", f"Quant Strategy Digest · {subject_date}")
    schedule_summary = _schedule_summary_from_github_event(timezone_name=timezone_name)

    local_tz = tz.gettz(timezone_name)
    generated_at = utc_now_iso()
    if local_tz is not None:
        try:
            import datetime as _dt

            generated_at = _dt.datetime.now(tz=local_tz).replace(microsecond=0).isoformat()
        except Exception:
            pass

    html = render_digest_html(
        template_path=template_path,
        subject=subject,
        generated_at=generated_at,
        timezone=timezone_name,
        items=processed,
        token_usage_summary=_format_token_usage_summary(
            selection_model=selection_model,
            selection_usage=selection_token_usage,
            classification_model=classification_model,
            classification_usage=classification_token_usage,
        ),
        schedule_summary=schedule_summary,
    )

    out_dir = REPO_ROOT / "out"
    out_dir.mkdir(parents=True, exist_ok=True)
    html_path = out_dir / "strategy_digest.html"
    html_path.write_text(html, encoding="utf-8")
    write_json(out_dir / "processed_strategies.json", processed)
    _log(f"Rendered HTML: {html_path}")

    run_payload_base = {
        "run_at": utc_now_iso(),
        "counts": {
            "fetched": len(normalized),
            "deduped_candidates": len(candidates),
            "selected": len(selected),
            "classified": len(classified),
        },
        "fetch_reports": fetch_reports,
        "evaluation_results": evaluation_logs,
        "selected_items": classified,
    }

    if dry_run:
        _log("DRY_RUN enabled: skipping email send and state update.")
        write_run_log(logs_dir, {**run_payload_base, "mode": "dry_run", "pushed_items": []})
        trim_old_logs(logs_dir, keep=120)
        return 0

    if not email_to or not email_from:
        raise RuntimeError("Missing EMAIL_TO or EMAIL_FROM (required unless DRY_RUN=1).")

    resp = send_email_smtp(from_email=email_from, to_email=email_to, subject=subject, html=html)
    _log(f"Email sent via smtp: {resp}")

    mark_sent(state, classified)
    save_state(state_path, state)
    mark_emailed(db_path, [it.get("sig") for it in classified if it.get("sig")])
    _log(f"Updated state: {state_path}")

    write_run_log(
        logs_dir,
        {
            **run_payload_base,
            "mode": "normal",
            "pushed_items": classified,
            "email_response": resp,
        },
    )
    trim_old_logs(logs_dir, keep=120)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
