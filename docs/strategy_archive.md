# 量化策略汇总

> 自动生成 · 最后更新：2026-06-13 20:23 · Asia/Shanghai
> 共 8 条策略

## 目录

- [2026-06（8）](#2026-06)

---

## 2026-06

### 配对交易执行策略

- **收录时间**：2026-06-13 20:23
- **发布时间**：2026-06-11 06:22
- **作者**：/u/Luctom
- **来源**：Reddit r/algotrading
- **分类**：套利 · stock · us
- **频率**：daily
- **摘要**：作者开发了一个面向零售交易的统计套利策略，专注于配对交易。其流水线包括候选资产对筛选、基于卡尔曼滤波的价差拟合和交易阈值优化。以SRLN-BKLN ETF对为例，样本内预期月收益率为26个基点，样本外为24个基点，收益微薄。为超越标普500，需运行多个配对，但筛选条件严格，当前仅能产生少量可交易对。作者探索了ETF-股票组合以扩展标的池。执行方面面临滑点、成交价、策略容量等问题，并需确定何时弃用配对及实现自动化。
- **要点**：
  - 配对交易流水线使用卡尔曼滤波和多目标优化。
  - 单对收益较低，需多对组合。
  - 执行挑战包括滑点、容量和配对管理。
- **回测线索**：In-sample expected return 26bps/month, out-of-sample 24bps/month; single-pair returns low; multi-pair approach.
- **风险**：Slippage and fill prices; strategy capacity limits; need to decide when to discard pairs; automation challenges.
- **策略价值**：为零售交易者提供了一套系统化的统计套利实现方案，但实际盈利取决于执行细节。
- **筛选评分**：85
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1u2gwd1/pairs_trading_execution/)

---

### laurentvv/Trading-AI：面向纳斯达克与原油ETF的混合AI交易系统

- **收录时间**：2026-06-13 20:23
- **发布时间**：2026-06-12 21:20
- **作者**：laurentvv
- **来源**：GitHub Quant Repos
- **分类**：机器学习 · stock · us
- **摘要**：这是一个高级混合AI专家系统，用于纳斯达克和WTI原油ETF交易。系统融合了量化机器学习、大型语言模型（Gemma 4）、TimesFM 2.5时间序列模型、视觉图表分析以及EIA基本面数据。它以高准确率信号为目标，支持双标的策略并通过Trading 212执行交易。项目使用Python 3.12开发，涉及算法交易、深度学习、情感分析等多个领域。目前已获得1个星标。
- **要点**：
  - 集成量化ML、LLM、TimesFM和视觉分析等多种AI技术。
  - 专注于纳斯达克和WTI原油ETF的双标的策略。
  - 利用EIA基本面数据和情感分析辅助决策。
  - 通过Trading 212 API实现自动化执行。
- **风险**：模型过拟合风险；LLM可能产生幻觉；多模型集成增加复杂性；依赖外部数据源可用性。
- **策略价值**：该项目展示了将多种前沿AI技术（包括大语言模型）整合到交易系统中的实际尝试，可能为量化交易提供新的混合方法参考。
- **筛选评分**：80
- **原文**：[链接](https://github.com/laurentvv/Trading-AI)

---

### CryptoQuantix：加密货币量化交易引擎

- **收录时间**：2026-06-13 20:23
- **发布时间**：2026-06-13 16:25
- **作者**：CryptoQuantix
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · crypto · global
- **频率**：intraday
- **摘要**：CryptoQuantix是一个面向加密货币期货/永续合约的量化交易引擎。它支持Deribit执行和Binance数据。该引擎包含3个经过4年多周期数据验证的策略。功能包括自动宏观门控、投资组合风险管理和操作仪表盘。源代码对个人用户开放，商业使用需付费许可。项目使用Python编写，支持异步操作。
- **要点**：
  - 开源引擎，适用于加密货币期货交易，内置风险管理。
  - 三个预验证策略，基于4年多周期数据。
  - 包含宏观门控和操作仪表盘功能。
- **回测线索**：Validated on 4 years of multi-cycle data. No specific performance numbers given.
- **风险**：Strategy risk depends on underlying strategies; licensed for personal use only; commercial license required for business.
- **策略价值**：为零售和专业加密货币量化交易者提供了稳健的策略部署和定制基础。
- **筛选评分**：80
- **原文**：[链接](https://github.com/CryptoQuantix/CryptoQuantix)

---

### 使用LightGBM进行前向破产预测：方法、结果及时间泄漏教训

- **收录时间**：2026-06-13 20:23
- **发布时间**：2026-06-13 19:26
- **作者**：/u/SeaOk5482
- **来源**：Reddit r/algotrading
- **分类**：机器学习 · stock · us
- **摘要**：作者基于LightGBM构建了一个会计数据驱动的破产预测模型。初始随机交叉验证的AUROC高达约0.95，但由于时间泄漏问题，这一结果并不可靠。采用严格的扩展窗口前向验证后，样本外AUROC降至0.78，与学术文献中的最佳结果一致。模型成功识别了赫兹、WeWork、精神航空等知名破产案例，并正确将微软评为低风险。模型存在行业条件阈值缺失的问题，可能导致对NextEra等公司产生误报。此外，年报数据滞后导致未能及时捕捉Bed Bath and Beyond等公司的破产，引入季度数据可改善时效性。
- **要点**：
  - 时间泄漏是面板数据机器学习中的常见陷阱，前向验证至关重要。
  - 样本外AUROC降至0.78，与学术结果相符。
  - 模型正确识别了多个高知名度破产案例。
  - 局限性包括行业偏差和年报数据滞后。
- **回测线索**：Walk-forward backtest from 2016-2021, OOS AUROC 0.78, comparable to academic benchmarks.
- **风险**：Temporal leakage if using random CV; sector-conditional thresholds needed; annual data lag may miss mid-year events.
- **策略价值**：可靠的破产预测可改进信用风险评估和量化策略中的因子构建。
- **筛选评分**：90
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1u4ogml/walkforward_bankruptcy_prediction_with_lightgbm/)

---

### Yuyutsu01/项目Aegis

- **收录时间**：2026-06-13 20:14
- **发布时间**：2026-06-12 22:59
- **作者**：未知
- **来源**：GitHub Quant Repos
- **分类**：机器学习 · multi · global
- **摘要**：Project AEGIS是一个研究级量化交易框架，实现了混合元策略架构。标准强化学习模型在非平稳金融环境中常因高噪声信号比而效果不佳。AEGIS通过解耦策略执行和优化来解决这一问题。框架使用Python编写，属于GitHub上的量化交易项目。目前该项目已获得2个星标。它结合了梯度提升和强化学习来提高策略的适应性。该框架旨在为高频交易和复杂市场环境提供更稳健的执行方案。
- **要点**：
  - AEGIS采用混合元策略架构，将强化学习与梯度提升结合。
  - 针对金融市场的非平稳性，通过解耦设计提升模型鲁棒性。
  - 项目目前处于研究阶段，仅在GitHub上获得2个星标。
- **风险**：强化学习模型在非平稳金融环境中容易过拟合，且高噪声信号比可能导致策略不稳定。
- **策略价值**：该框架为处理高噪声金融数据提供了新的方法，有望提升量化策略在复杂环境下的执行效果。
- **筛选评分**：80
- **原文**：[链接](https://github.com/Yuyutsu01/Project_Aegis)

---

### Krexind/量化交易

- **收录时间**：2026-06-13 19:31
- **发布时间**：2026-06-13 19:28
- **作者**：未知
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · multi · global
- **频率**：daily
- **摘要**：该项目是一个量化交易策略集合，包含VIX计算器、模式识别、蒙特卡洛模拟、Heikin-Ashi蜡烛图和配对交易等多种策略。它涵盖了算法交易、布林带、商品交易、MACD、动量策略、期权策略、统计套利等技术。编程语言为Python，获得36颗星。该仓库适用于学习多种量化交易思路。策略类型多样，从趋势跟踪到统计套利均有涉及。数据源需自行准备，回测结果未提供。
- **要点**：
  - 包含VIX计算器、模式识别、蒙特卡洛模拟等多种策略
  - 基于Python实现，适合学习多种交易思想
  - 未提供回测结果，需自行验证策略有效性
- **策略价值**：该仓库提供了一个多策略量化交易工具箱，适合初学者快速了解并实践不同交易逻辑。
- **筛选评分**：80
- **原文**：[链接](https://github.com/Krexind/quant-trading)

---

### 每日摆动预测代理：从回测到小规模实盘测试，寻求反馈

- **收录时间**：2026-06-13 19:31
- **发布时间**：2026-06-13 15:22
- **作者**：未知
- **来源**：Reddit r/algotrading
- **分类**：趋势跟踪 · stock · us
- **频率**：daily
- **摘要**：该系统基于日线OHLCV数据预测下一交易日的涨跌方向。包含规划层和执行层，规划层由基础模型、集成层和权限过滤器组成。回测四年表现积极，准确率约55.5%，但作者认识到回测不等于实盘。已开始用小资金进行实盘测试以发现执行问题。系统通过集成多个基础模型并动态调整权重来提高预测稳定性。权限层根据市场状态决定是否交易。回测中覆盖率为68.9%，但准确率仍有提升空间。作者欢迎社区反馈以改进系统。
- **要点**：
  - 系统由规划层和执行层组成，规划层包含基础模型、集成和权限过滤
  - 回测四年，自信预测准确率55.5%，策略总回报3.29
  - 已进入小规模实盘测试，重点排查执行漏洞
- **回测线索**：Backtest over ~4 years: confident accuracy 0.555, total strategy return 3.29, compounded return 17.
- **风险**：Backtest performance may not reflect live results; execution bugs; overfitting risk; low accuracy (55%)
- **策略价值**：该代理展示了从回测到实盘过渡的实际案例，强调了回测与实盘之间可能存在的差距，对量化交易者具有借鉴意义。
- **筛选评分**：85
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1u4kdi7/daily_swing_prediction_agent_moving_from_backtest/)

---

### Created a Profitable Algo with 8 years of backtesting

- **收录时间**：2026-06-13 19:29
- **发布时间**：2026-06-11 08:25
- **作者**：未知
- **来源**：Reddit r/algotrading
- **分类**：综合/其他 · multi · global
- **摘要**：I've been backtesting a couple of intraday NQ futures strategies (5m signals, 1m execution, real commissions + slippage) and have several years of results — decent profit factor, controlled drawdowns, a few thousand trades. Before I scale up I'd love to hear from people who've made the jump: which metrics did you actually weight when deciding a backtest was trustworthy (PF, win rate, max DD, Sharpe, year-by-year consistency?), what made you throw a strategy out even though the headline numbers l
- **筛选评分**：91
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1u2js33/created_a_profitable_algo_with_8_years_of/)

---
