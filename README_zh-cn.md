# Quant Strategy Crawler Digest

[![Daily Quant Strategy Digest](https://github.com/lhjlife-sys/ai_strategy/actions/workflows/daily-strategy.yml/badge.svg)](https://github.com/lhjlife-sys/ai_strategy/actions/workflows/daily-strategy.yml)

自动化量化策略爬虫流水线：从 RSS / GitHub / 国内社区抓取策略内容，经 LLM 筛选、分类与摘要后写入 SQLite，渲染 HTML 邮件并通过 SMTP 推送。

## 工作流程

```text
多源抓取 (RSS + GitHub + 聚宽/掘金/米筐)
  -> 标准化与去重
  -> 关键词过滤与来源均衡采样
  -> LLM 批量选择
  -> LLM 分类摘要
  -> SQLite 入库 + JSON 导出
  -> HTML 邮件推送
  -> 可选 commit state/logs/db
```

## 本地运行

```powershell
copy .env.example .env
# 编辑 .env，设置 DRY_RUN=1
.\run.ps1
```

## GitHub Actions

- 定时：每日 08:00 / 20:00（Asia/Shanghai）
- 配置说明见 [GITHUB_SETUP.md](GITHUB_SETUP.md)

## 项目结构

- `config/` — 抓取源、爬虫、prompt、偏好配置
- `scripts/strategy_pipeline.py` — 主入口
- `data/strategies.db` — SQLite 策略库
- `state/sent_items.json` — 邮件去重状态
- `templates/strategy_digest.html.j2` — 邮件模板

## License

GPL-3.0
