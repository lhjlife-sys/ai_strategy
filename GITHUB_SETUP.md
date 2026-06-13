# GitHub Actions Setup Checklist

Push completed. Configure secrets at:
https://github.com/lhjlife-sys/ai_strategy/settings/secrets/actions

## Manual Setup (Web UI)

Open: https://github.com/lhjlife-sys/ai_strategy/settings/secrets/actions

Click **New repository secret** for each row below. Values can be copied from your local `.env` (same keys as `ai_daily` if you reuse that stack):

| Secret Name | Copy from `.env` key |
|-------------|----------------------|
| `OPENAI_API_KEY` | `OPENAI_API_KEY` |
| `SMTP_USER` | `SMTP_USER` |
| `SMTP_PASSWORD` | `SMTP_PASSWORD` |
| `EMAIL_FROM` | `EMAIL_FROM` |
| `EMAIL_TO` | `EMAIL_TO` |

Optional (GitHub repo search rate limits):

| Secret Name | Copy from `.env` key |
|-------------|----------------------|
| `GITHUB_TOKEN` | `GITHUB_TOKEN` (PAT with `public_repo` or `repo`) |

Optional repository **Variables** (not secrets): https://github.com/lhjlife-sys/ai_strategy/settings/variables/actions

| Variable | Suggested value |
|----------|-----------------|
| `EMAIL_SUBJECT` | `Quant Strategy Digest` |
| `DRY_RUN` | `0` |

## Required Secrets

| Name | Value |
|------|-------|
| OPENAI_API_KEY | DeepSeek API key |
| SMTP_USER | QQ email address |
| SMTP_PASSWORD | QQ mail auth code (16 chars) |
| EMAIL_FROM | Same as SMTP_USER |
| EMAIL_TO | Recipient email |

## Optional Secrets

| Name | Value |
|------|-------|
| GITHUB_TOKEN | GitHub PAT for higher API rate limits on repo search |

## Optional Variables

https://github.com/lhjlife-sys/ai_strategy/settings/variables/actions

Workflow defaults are already set in `.github/workflows/daily-strategy.yml`:
- DRY_RUN=0, COMMIT_RUNTIME_STATE=1
- OPENAI_API_MODE=chat, deepseek-v4-flash models
- cron: 22:00 UTC = 06:00 Beijing, 10:00 UTC = 18:00 Beijing (twice daily)

## Test

1. Actions -> Daily Quant Strategy Digest -> Run workflow
2. Expect log: `Fetched N`, `Selected M`, `Email sent via smtp`
3. Next day ~06:00 and ~18:00 auto run (may delay 5-15 min)

## Local

Keep local `.env` with `DRY_RUN=1` to avoid duplicate emails.

Run:

```powershell
python scripts/strategy_pipeline.py
```
