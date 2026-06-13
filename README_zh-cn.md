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
  -> SQLite 入库 + Markdown 汇总文档
  -> HTML 邮件推送
  -> 可选 commit state/logs/db/archive
```

## 策略汇总文档

每次运行后自动从 SQLite 全量导出 [`docs/strategy_archive.md`](docs/strategy_archive.md)，包含：

- 收录时间、发布时间、作者、来源
- 策略分类、摘要、要点、回测线索、风险
- 按月目录分组，便于长期查阅

本地 `DRY_RUN=1` 运行后也会更新该文档。

## 本地运行

```powershell
copy .env.example .env
# 编辑 .env，设置 DRY_RUN=1
.\run.ps1
```

## GitHub Actions

- 定时：每日 06:00 / 18:00（Asia/Shanghai）
- 配置说明见 [GITHUB_SETUP.md](GITHUB_SETUP.md)

## 项目结构

- `config/` — 抓取源、爬虫、prompt、偏好配置
- `scripts/strategy_pipeline.py` — 主入口
- `data/strategies.db` — SQLite 策略库
- `docs/strategy_archive.md` — 历史策略 Markdown 汇总
- `state/sent_items.json` — 邮件去重状态
- `templates/strategy_digest.html.j2` — 邮件模板

## License

GPL-3.0
