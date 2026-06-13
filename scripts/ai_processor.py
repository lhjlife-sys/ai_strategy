from __future__ import annotations

import json
import os
from typing import Any

from openai import OpenAI
from pydantic import BaseModel, Field
from tenacity import retry, stop_after_attempt, wait_exponential

from .author_extract import infer_author


class TokenUsage(BaseModel):
    input_tokens: int = 0
    output_tokens: int = 0
    total_tokens: int = 0
    reasoning_tokens: int = 0
    cached_input_tokens: int = 0
    api_mode: str = ""
    response_id: str | None = None
    reasoning_summary: list[str] = Field(default_factory=list)


class SelectionResult(BaseModel):
    items: list["SelectedItemResult"] = Field(default_factory=list)
    token_usage: TokenUsage = Field(default_factory=TokenUsage)


class SelectedItemResult(BaseModel):
    index: int
    score: int = Field(ge=0, le=100)
    reason: str


class ClassifiedStrategyItem(BaseModel):
    sig: str
    title: str
    url: str
    source_name: str
    published_at: str | None = None
    summary: str = ""
    strategy_type: str = "multi"
    asset_class: str = "multi"
    market: str = "global"
    frequency: str | None = None
    data_requirements: list[str] = Field(default_factory=list)
    backtest_hint: str | None = None
    risk_notes: str | None = None
    author: str | None = None
    translated_title: str
    translated_summary: str
    key_points: list[str] = Field(default_factory=list)
    why_it_matters: str | None = None


class ClassificationResult(BaseModel):
    items: list[ClassifiedStrategyItem] = Field(default_factory=list)
    token_usage: TokenUsage = Field(default_factory=TokenUsage)
    expected_count: int = 0
    returned_count: int = 0
    fallback_count: int = 0
    missing_sigs: list[str] = Field(default_factory=list)


SELECTION_RESPONSE_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "index": {"type": "integer"},
                    "score": {"type": "integer", "minimum": 0, "maximum": 100},
                    "reason": {"type": "string"},
                },
                "required": ["index", "score", "reason"],
            },
        },
    },
    "required": ["items"],
}

CLASSIFICATION_RESPONSE_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "sig": {"type": "string"},
                    "title": {"type": "string"},
                    "url": {"type": "string"},
                    "source_name": {"type": "string"},
                    "published_at": {"type": ["string", "null"]},
                    "summary": {"type": "string"},
                    "strategy_type": {"type": "string"},
                    "asset_class": {"type": "string"},
                    "market": {"type": "string"},
                    "frequency": {"type": ["string", "null"]},
                    "data_requirements": {"type": "array", "items": {"type": "string"}},
                    "backtest_hint": {"type": ["string", "null"]},
                    "risk_notes": {"type": ["string", "null"]},
                    "author": {"type": ["string", "null"]},
                    "translated_title": {"type": "string"},
                    "translated_summary": {"type": "string"},
                    "key_points": {"type": "array", "items": {"type": "string"}},
                    "why_it_matters": {"type": ["string", "null"]},
                },
                "required": [
                    "sig", "title", "url", "source_name", "published_at", "summary",
                    "strategy_type", "asset_class", "market", "frequency", "data_requirements",
                    "backtest_hint", "risk_notes", "author", "translated_title", "translated_summary",
                    "key_points", "why_it_matters",
                ],
            },
        },
    },
    "required": ["items"],
}


def _use_json_object_mode() -> bool:
    mode = os.getenv("LLM_JSON_MODE", "").strip().lower()
    if mode in {"json_object", "1", "true", "yes"}:
        return True
    base = os.getenv("OPENAI_BASE_URL", "").lower()
    return "deepseek.com" in base


def _client() -> OpenAI:
    base_url = os.getenv("OPENAI_BASE_URL", "").strip()
    if base_url:
        return OpenAI(base_url=base_url)
    return OpenAI()


def _normalize_selection_items(data: Any) -> list[dict[str, Any]]:
    if not isinstance(data, dict):
        return []
    raw_items = data.get("items")
    if not isinstance(raw_items, list):
        return []
    normalized: list[dict[str, Any]] = []
    for item in raw_items:
        if not isinstance(item, dict):
            continue
        idx = item.get("index", item.get("i"))
        if idx is None:
            continue
        try:
            idx_int = int(idx)
        except (TypeError, ValueError):
            continue
        score = item.get("score", 0)
        try:
            score_int = int(score)
        except (TypeError, ValueError):
            score_int = 0
        reason = str(item.get("reason") or item.get("why") or "")
        normalized.append({"index": idx_int, "score": score_int, "reason": reason})
    return normalized


def _get(obj: Any, name: str, default: Any = None) -> Any:
    if isinstance(obj, dict):
        return obj.get(name, default)
    return getattr(obj, name, default)


def _token_usage_from_response(resp: Any, *, api_mode: str) -> TokenUsage:
    usage = _get(resp, "usage")
    if usage is None:
        return TokenUsage(api_mode=api_mode, response_id=_get(resp, "id"))
    input_details = _get(usage, "input_tokens_details") or _get(usage, "prompt_tokens_details")
    output_details = _get(usage, "output_tokens_details") or _get(usage, "completion_tokens_details")
    input_tokens = int(_get(usage, "input_tokens") or _get(usage, "prompt_tokens") or 0)
    output_tokens = int(_get(usage, "output_tokens") or _get(usage, "completion_tokens") or 0)
    total_tokens = int(_get(usage, "total_tokens") or input_tokens + output_tokens)
    reasoning_tokens = int(_get(output_details, "reasoning_tokens", 0) or 0)
    cached_input_tokens = int(_get(input_details, "cached_tokens", 0) or 0)
    return TokenUsage(
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        total_tokens=total_tokens,
        reasoning_tokens=reasoning_tokens,
        cached_input_tokens=cached_input_tokens,
        api_mode=api_mode,
        response_id=_get(resp, "id"),
    )


def _response_text(resp: Any) -> str:
    output_text = _get(resp, "output_text")
    if output_text:
        return str(output_text)
    chunks: list[str] = []
    for output in _get(resp, "output", []) or []:
        for content in _get(output, "content", []) or []:
            text = _get(content, "text")
            if text:
                chunks.append(str(text))
    return "".join(chunks)


def _parse_json_content(content: str) -> Any:
    if not content:
        return {}
    return json.loads(content)


def _chat_response_format(schema_name: str, schema: dict[str, Any]) -> dict[str, Any]:
    return {
        "type": "json_schema",
        "json_schema": {"name": schema_name, "schema": schema, "strict": True},
    }


def _normalize_api_mode(api_mode: str | None) -> str:
    value = (api_mode or "chat").strip().lower()
    if value not in {"responses", "chat"}:
        raise ValueError(f"Invalid OPENAI_API_MODE: {api_mode!r}")
    return value


def _chat_json(
    model: str,
    system: str,
    user: str,
    *,
    schema_name: str,
    schema: dict[str, Any],
) -> tuple[Any, TokenUsage]:
    client = _client()
    request: dict[str, Any] = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": 0.2,
        "max_tokens": int(os.getenv("OPENAI_MAX_TOKENS", "8192")),
    }
    if _use_json_object_mode():
        request["response_format"] = {"type": "json_object"}
    else:
        request["response_format"] = _chat_response_format(schema_name, schema)
    resp = client.chat.completions.create(**request)
    content = resp.choices[0].message.content or "{}"
    return _parse_json_content(content), _token_usage_from_response(resp, api_mode="chat")


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=10))
def _complete_json(
    model: str,
    system: str,
    user: str,
    *,
    schema_name: str,
    schema: dict[str, Any],
    api_mode: str = "chat",
) -> tuple[Any, TokenUsage]:
    return _chat_json(model=model, system=system, user=user, schema_name=schema_name, schema=schema)


def _render_prompt(template: str, vars_map: dict[str, str]) -> str:
    out = template
    for k, v in vars_map.items():
        out = out.replace("{{ " + k + " }}", v).replace("{{" + k + "}}", v)
    return out


def _combine_token_usage(usages: list[TokenUsage], *, api_mode: str) -> TokenUsage:
    response_ids = [u.response_id for u in usages if u.response_id]
    return TokenUsage(
        input_tokens=sum(u.input_tokens for u in usages),
        output_tokens=sum(u.output_tokens for u in usages),
        total_tokens=sum(u.total_tokens for u in usages),
        reasoning_tokens=sum(u.reasoning_tokens for u in usages),
        cached_input_tokens=sum(u.cached_input_tokens for u in usages),
        api_mode=api_mode,
        response_id=", ".join(response_ids) if response_ids else None,
    )


def select_items(
    candidates: list[dict],
    *,
    model: str,
    max_selected: int,
    topic_hint: str | None = None,
    system_prompt: str | None = None,
    user_prompt_template: str | None = None,
    api_mode: str = "chat",
) -> SelectionResult:
    slim = []
    for i, it in enumerate(candidates):
        slim.append(
            {
                "index": i,
                "title": it.get("title", ""),
                "source": it.get("source_name", it.get("source_id", "")),
                "url": it.get("url", ""),
                "published_at": it.get("published_at"),
                "content": (it.get("content_text", "") or "")[:500],
            }
        )

    if system_prompt and user_prompt_template:
        system = system_prompt
        user = _render_prompt(
            user_prompt_template,
            {
                "user_preference": topic_hint or "",
                "max_selected": str(max_selected),
                "items_json": json.dumps(slim, ensure_ascii=False),
            },
        )
    else:
        hint = f"Topic focus: {topic_hint}\n" if topic_hint else ""
        system = "You are a quant strategy editor. Respond with valid JSON only."
        user = (
            f"{hint}Select up to {max_selected} strategy items.\n"
            'Return JSON: {"items":[{"index":0,"score":85,"reason":"..."}]}\n\n'
            f"Items: {json.dumps(slim, ensure_ascii=False)}"
        )

    data, token_usage = _complete_json(
        model=model,
        system=system,
        user=user,
        schema_name="selection_result",
        schema=SELECTION_RESPONSE_SCHEMA,
        api_mode=api_mode,
    )
    normalized_items = _normalize_selection_items(data)
    if normalized_items:
        data = {"items": normalized_items}
    try:
        res = SelectionResult.model_validate(data)
    except Exception as exc:
        print(f"[warn] selection JSON validation failed: {exc}", flush=True)
        res = SelectionResult(items=[])
    res.token_usage = token_usage

    clean_items: list[SelectedItemResult] = []
    seen_indices: set[int] = set()
    for item in res.items:
        if item.index in seen_indices:
            continue
        if 0 <= item.index < len(candidates):
            clean_items.append(item)
            seen_indices.add(item.index)
    res.items = clean_items[:max_selected]
    return res


def classify_and_summarize(
    items: list[dict],
    *,
    model: str,
    target_language: str,
    system_prompt: str,
    user_prompt_template: str,
    api_mode: str = "chat",
    batch_size: int = 3,
) -> ClassificationResult:
    batch_size = max(1, batch_size)

    def build_payload(batch_items: list[dict]) -> list[dict]:
        payload: list[dict] = []
        for it in batch_items:
            payload.append(
                {
                    "sig": str(it.get("sig") or ""),
                    "title": str(it.get("title") or ""),
                    "url": str(it.get("url") or ""),
                    "source_name": str(it.get("source_name") or ""),
                    "published_at": it.get("published_at"),
                    "content": (it.get("content_text", "") or "")[:2000],
                    "author_hint": it.get("author") or infer_author(it),
                }
            )
        return payload

    def classify_payload(payload: list[dict]) -> tuple[list[ClassifiedStrategyItem], TokenUsage]:
        user = _render_prompt(
            user_prompt_template,
            {
                "target_language": target_language,
                "items_json": json.dumps(payload, ensure_ascii=False),
            },
        )
        data, token_usage = _complete_json(
            model=model,
            system=system_prompt,
            user=user,
            schema_name="classification_result",
            schema=CLASSIFICATION_RESPONSE_SCHEMA,
            api_mode=api_mode,
        )
        if isinstance(data, list):
            raw_items = data
        elif isinstance(data, dict):
            raw_items = data.get("items", [])
        else:
            raw_items = []
        out: list[ClassifiedStrategyItem] = []
        if not isinstance(raw_items, list):
            return out, token_usage
        for r in raw_items:
            try:
                out.append(ClassifiedStrategyItem.model_validate(r))
            except Exception:
                continue
        return out, token_usage

    def fallback_item(it: dict) -> ClassifiedStrategyItem:
        content = (it.get("content_text", "") or it.get("title", "") or "")[:500]
        return ClassifiedStrategyItem(
            sig=str(it.get("sig") or ""),
            title=str(it.get("title") or ""),
            url=str(it.get("url") or ""),
            source_name=str(it.get("source_name") or ""),
            published_at=it.get("published_at"),
            summary="",
            author=it.get("author"),
            translated_title=str(it.get("title") or ""),
            translated_summary=str(content),
            key_points=[],
            why_it_matters=None,
        )

    translated_by_sig: dict[str, ClassifiedStrategyItem] = {}
    usages: list[TokenUsage] = []
    returned_count = 0
    fallback_count = 0
    missing_sigs: list[str] = []

    for start in range(0, len(items), batch_size):
        batch = items[start : start + batch_size]
        payload = build_payload(batch)
        classified_batch, usage = classify_payload(payload)
        usages.append(usage)
        returned_count += len(classified_batch)
        for item in classified_batch:
            if item.sig and item.sig not in translated_by_sig:
                translated_by_sig[item.sig] = item

        missing_payload = [p for p in payload if p["sig"] not in translated_by_sig]
        for missing in missing_payload:
            original = next((it for it in batch if str(it.get("sig") or "") == missing["sig"]), missing)
            retry_items, retry_usage = classify_payload([missing])
            usages.append(retry_usage)
            returned_count += len(retry_items)
            retry_item = next((it for it in retry_items if it.sig == missing["sig"]), None)
            if retry_item is not None:
                translated_by_sig[missing["sig"]] = retry_item
                continue
            missing_sigs.append(missing["sig"])
            translated_by_sig[missing["sig"]] = fallback_item(original)
            fallback_count += 1

    ordered_items = [
        translated_by_sig[str(it.get("sig") or "")]
        for it in items
        if str(it.get("sig") or "") in translated_by_sig
    ]
    return ClassificationResult(
        items=ordered_items,
        token_usage=_combine_token_usage(usages, api_mode=api_mode),
        expected_count=len(items),
        returned_count=returned_count,
        fallback_count=fallback_count,
        missing_sigs=missing_sigs,
    )
