# 量化策略汇总

> 自动生成 · 最后更新：2026-06-14 19:54 · Asia/Shanghai
> 共 15 条策略

## 目录

- [2026-06（15）](#2026-06)

---

## 2026-06

### 我构建了一个工具，用自然语言查询SEC的10-K/10-Q文件，并拒绝编造财务数据

- **收录时间**：2026-06-14 19:54
- **发布时间**：2026-06-12 23:12
- **作者**：Meta_Fazer
- **来源**：Reddit r/algotrading
- **分类**：机器学习 · stock · us
- **摘要**：作者对大型语言模型编造财务数字感到沮丧，因此构建了FinRAG，一个专门针对SEC文件的检索增强生成（RAG）管道。用户可以询问如“苹果公司2024财年自由现金流是多少？”这样的问题，系统会返回带有精确引用的答案，包括公司、文件期间、章节和页码。如果证据不够强（可信度低于0.85），系统会拒绝回答而非猜测。管道中内置了自动拒绝协议。检索方式融合了BM25稀疏搜索和密集嵌入，并通过倒数排名融合进行排序，再经过交叉编码器进行第二遍精确过滤。LangGraph状态机在检索前对查询进行路由，LLM作为裁判实时对每个响应评分。对算法交易者特别有用：可查询收益电话会议记录获取管理层语气和指引；多轮会话记忆允许在一次对话中比较多个文件；API已开放。提供了演示链接，并希望获得反馈。
- **要点**：
  - FinRAG是一个专注SEC文件的RAG管道，提供带有精确引用的答案。
  - 采用BM25稀疏搜索、密集嵌入和交叉编码器混合检索策略。
  - 具备自动拒绝回答机制，当证据置信度低于0.85时不会编造数据。
  - 支持多轮会话，可比较多个文件，并能查询收益电话会议记录。
- **风险**：May not work for non-English or non-SEC documents; relies on document quality; refusal protocol may omit some valid answers.
- **策略价值**：对算法交易者而言，该工具能快速、可靠地从SEC文件中提取财务数据，减少LLM幻觉风险，提升基本面分析效率。
- **筛选评分**：65
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1u3y26m/i_built_a_tool_that_queries_sec_10k10q_filings_in/)

---

### Fast-meadowvole9864/策略工厂

- **收录时间**：2026-06-14 19:54
- **发布时间**：2026-06-14 18:07
- **作者**：Fast-meadowvole9864
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · multi · global
- **摘要**：该仓库提供了一个模块化的量化引擎，用于构建交易策略。它强调鲁棒性验证、向前优化和置换测试。代码使用Python编写，但设计模式描述中提到了多种语言如C#和Kotlin。项目目前拥有0星，可能是一个新的或未被广泛关注的工具。主题包括自动化、设计模式、测试工具等。该引擎旨在支持多种策略类型和资产类别。它可能适合那些希望构建自定义策略框架的开发者。没有提供具体的交易策略示例。
- **要点**：
  - 提供模块化量化引擎，支持向前优化和置换测试。
  - 项目使用Python，但设计模式参考文献涉及C#和Kotlin。
  - 当前星数为0，表明项目可能处于早期阶段。
  - 强调鲁棒性验证和自动化的策略构建流程。
- **回测线索**：框架包含向前优化和置换测试，可用于回测验证。
- **策略价值**：该框架为开发者提供了一个灵活的基础设施，以便通过严谨的验证方法构建和测试多种交易策略。
- **筛选评分**：75
- **原文**：[链接](https://github.com/Fast-meadowvole9864/Strategy-Factory)

---

### 量化交易框架

- **收录时间**：2026-06-14 19:54
- **发布时间**：2026-06-14 14:39
- **作者**：jellyfishing2346
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · stock · us
- **摘要**：该仓库提供了一套量化交易框架，包含了动量策略和均值回归策略的实现。框架支持Walk-Forward回测，能够有效评估策略的稳健性。内置了风险分析模块，用于衡量投资组合的风险暴露。利用Plotly Dash构建了交互式仪表盘，便于可视化分析。框架基于Backtrader、yfinance和SQLite缓存构建，数据获取和存储高效。提供了在线演示部署于Render平台，方便用户直接体验。代码以Python编写，适合量化交易爱好者学习和使用。
- **要点**：
  - 包含动量与均值回归两种策略
  - 支持Walk-Forward回测和风险分析
  - 集成Plotly Dash交互式仪表盘
  - 基于Backtrader、yfinance和SQLite构建
- **回测线索**：采用Walk-Forward回测方法验证策略
- **策略价值**：该框架为量化策略开发提供了完整的工具链，降低了从研究到部署的门槛。
- **筛选评分**：80
- **原文**：[链接](https://github.com/jellyfishing2346/quantitative-finance)

---

### 潜在警告：QQQ从高点下跌约5%后，二次下跌平均为首次下跌的两倍，底部在17.2天后出现

- **收录时间**：2026-06-14 19:54
- **发布时间**：2026-06-14 07:51
- **作者**：medphysik
- **来源**：Reddit r/algotrading
- **分类**：均值回归 · stock · us
- **频率**：daily
- **摘要**：该帖子分析了QQT在从高点下跌约5%后，首次下跌与二次下跌的关系，基于21个近高点交易样本。主要发现包括：首次下跌平均为-3.97%，二次下跌平均为-8.09%（约两倍），到达底部的平均时间为17.2个交易日。二次下跌的幅度与首次下跌的幅度之间没有相关性。交易者应预期在买入下跌后约3.5周的波动和下行。数据来自QQQ的历史价格。
- **要点**：
  - 二次下跌幅度平均是首次下跌的两倍（-8.09% vs -3.97%）。
  - 从高点下跌后到达底部平均需要17.2个交易日。
  - 首次下跌的大小无法预测二次下跌的深度（相关性为零）。
- **回测线索**：Backtested on 21 near-high trades, showing average secondary flush of -8.09% and 17.2 days to bottom.
- **风险**：Zero correlation between primary and secondary flush magnitudes; timing of bottom is uncertain; sample size is small (21 trades).
- **策略价值**：该分析为抄底策略提供了量化风险管理依据，提醒投资者即使小幅下跌后也可能出现更大跌幅，且回调幅度不可预测。
- **筛选评分**：85
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1u55teb/potential_warning_after_a_roughly_5_drop_from/)

---

### AArt1552/向量化加密货币回测器

- **收录时间**：2026-06-14 06:59
- **发布时间**：2026-06-14 03:59
- **作者**：AArt1552
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · crypto · global
- **摘要**：这是一个高性能的向量化回测器，专为山寨币交易策略优化设计。它利用比特币价格变动和高级量化分析来驱动策略回测。该工具使用Python编写，支持多种加密货币交易策略的回测。它包含algotrading、altcoin、backtesting等多个主题标签。项目在GitHub上获得1颗星，表明其处于早期阶段。该回测器适用于加密货币量化交易研究和开发。它可能支持多种数据频率，但具体未明确说明。用户需要提供OHLCV数据来进行回测。该项目由AArt1552创建和维护。
- **要点**：
  - 向量化实现，提高回测速度。
  - 专注于山寨币，利用比特币价格行动。
  - 支持多种加密货币交易策略。
  - Python编写，适合量化分析。
- **回测线索**：Vectorized implementation for high-speed backtesting of multiple strategies.
- **风险**：Backtesting risks include overfitting and look-ahead bias; performance may not reflect live trading.
- **策略价值**：该工具为加密货币量化交易者提供了一个高效的回测平台，有助于快速验证和优化基于比特币走势的山寨币交易策略。
- **筛选评分**：60
- **原文**：[链接](https://github.com/AArt1552/Vectorized-Crypto-Backtester)

---

### Barrazar274/the-0050-project

- **收录时间**：2026-06-14 06:59
- **发布时间**：2026-06-14 05:12
- **作者**：Barrazar274
- **来源**：GitHub Quant Repos
- **分类**：机器学习 · stock · global
- **频率**：daily
- **摘要**：一个量化交易项目，比较自定义机器学习策略（LightGBM）与台湾0050指数买入持有策略的表现。项目使用Python实现，包括回测和ETF轮动。作者将其标记为失败实验。
- **要点**：
  - 比较ML策略与0050买入持有。
  - 使用LightGBM和ETF轮动。
  - 项目被标记为失败实验，可能策略效果不佳。
- **回测线索**：Backtested data comparing ML strategies vs. 0050 buy-and-hold; ETF rotation used; labeled as failed experiment.
- **风险**：Project labeled as failed experiment; ML strategies underperformed or had issues; no live trading results.
- **策略价值**：该实验记录了一种常见量化研究方法（ML对比基准），即使失败也有学习价值。
- **筛选评分**：60
- **原文**：[链接](https://github.com/Barrazar274/the-0050-project)

---

### 更新：抄底（2026年6月）——我们的交易与历史对比如何？

- **收录时间**：2026-06-14 06:59
- **发布时间**：2026-06-14 04:00
- **作者**：medphysik
- **来源**：Reddit r/algotrading
- **分类**：均值回归 · stock · us
- **频率**：daily
- **摘要**：一位交易员更新了QQQ的抄底策略，该策略在-4.8%的下跌后触发。基于25年回测中21个相似案例（接近52周高点），策略在3个月内胜率80%，但平均最大回撤为-8.41%。当前交易正处于第5天，历史平均路径显示初期可能进一步下挫。回测统计包括各时间段平均回报和最大回撤分布。作者指出该策略在历史中具有韧性，但提醒短期波动风险。
- **要点**：
  - 策略条件: QQQ在52周高点5%以内时，买入单日-3.3%至-6.3%的跌幅。
  - 25年回测显示3个月胜率80%，平均回报+4.68%。
  - 平均最大回撤-8.41%，前1-2个月波动最大。
- **回测线索**：25-year backtest with 21 instances, 1-month avg return +0.50% (70% win), 3-month +4.68% (80% win), average max drawdown -8.41%
- **风险**：High volatility in first 1-2 months; average drawdown -8.41% before recovery; historical performance not guarantee of future results.
- **策略价值**：该策略为利用市场短期恐慌提供量化依据，但需承受中期回撤风险。
- **筛选评分**：85
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1u50l99/update_buying_the_dip_june_2026_how_is_our_trade/)

---

### 每日摆动预测智能体：从回测到小规模实盘测试。寻求反馈。

- **收录时间**：2026-06-14 06:59
- **发布时间**：2026-06-13 15:22
- **作者**：SeanLeePeasant
- **来源**：Reddit r/algotrading
- **分类**：趋势跟踪 · stock · us
- **频率**：daily
- **摘要**：该智能体基于Python构建，用于预测每日蜡烛图的方向。系统分为规划层和执行层：规划层包含基础模型层、集成层和权限层（机制过滤器）。基础模型层产生多个方向预测，集成层根据概率和近期表现加权综合，权限层决定是否允许交易。回测超过4年，准确率55.54%，策略总收益329.48%。目前正用小资金进行实盘测试以发现执行错误。作者意识到回测与实盘差距，谨慎推进。
- **要点**：
  - 系统使用OHLCV数据预测每日方向，包含基础模型、集成和权限过滤三层。
  - 回测覆盖4年，自信预测准确率55.54%，策略复合收益329.48%。
  - 已过渡到小规模实盘测试，重点排查执行错误。
- **回测线索**：Backtest over ~4 years positive with confident accuracy 55.54% and total strategy return 329.48% (compounded).
- **风险**：Backtest performance not same as live; small equity test to fix execution bugs.
- **策略价值**：展示了从回测到实盘的系统化过渡方法，强调回测局限性和小资金验证的必要性。
- **筛选评分**：85
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1u4kdi7/daily_swing_prediction_agent_moving_from_backtest/)

---

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
