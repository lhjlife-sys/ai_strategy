# 量化策略汇总

> 自动生成 · 最后更新：2026-06-16 07:31 · Asia/Shanghai
> 共 30 条策略

## 目录

- [2026-06（30）](#2026-06)

---

## 2026-06

### 相关性涌现与两个耦合限价订单簿中的Epps效应

- **收录时间**：2026-06-16 07:31
- **发布时间**：2026-06-15 12:00
- **作者**：Chris Angstmann, Tim Gebbie
- **来源**：arXiv q-fin.TR (Trading)
- **分类**：做市 · stock · global
- **频率**：intraday
- **摘要**：本文提出了两个耦合限价订单簿中相关性涌现和Epps效应的统一解析模型。模型从订单流及其创建、取消和扩散的离散随机游走描述开始。在订单创建层面引入簿之间的配对交易耦合。文章阐明了离散模型如何简化为具有移动反应边界（定义交易价格）的耦合反应-扩散方程。利用耦合的正则化局部响应表示，推导了实现相关性作为聚合时间函数的近似闭式表达式。Epps效应被证明源于三种不同机制：异步事件时钟（子ordination）、有限耦合响应时间及其组合。该模型为理解高频市场微观结构中的相关性动态提供了理论基础。
- **要点**：
  - 提出了两个耦合限价订单簿的统一分析模型，揭示相关性涌现机制。
  - Epps效应来自异步时钟、有限响应时间及其组合三种机制。
  - 推导了相关性随聚合时间变化的近似闭式表达式。
- **策略价值**：该研究有助于理解市场微观结构中相关性的动态形成机制，对高频交易策略设计具有理论指导意义。
- **筛选评分**：68
- **原文**：[链接](https://arxiv.org/abs/2606.14182)

---

### 大家是否发现2023-2024年主要是隔夜波动，而2025-2026年则不同？

- **收录时间**：2026-06-16 07:31
- **发布时间**：2026-06-14 06:30
- **作者**：NationalOwl9561
- **来源**：Reddit r/algotrading
- **分类**：期权 · stock · us
- **频率**：intraday
- **摘要**：一位算法交易者发现其日内0DTE卖出策略在回测中于2025-2026年表现极佳。但在2023-2024年，市场以隔夜跳空为主，该策略落后于简单买入持有SPY。他质疑是否需要接受这一事实，并思考市场何时会重回隔夜主导的状态。该讨论反映了市场制度变化对短期策略的影响。
- **要点**：
  - 日内0DTE卖出策略在隔夜跳空为主的市场中表现不佳。
  - 2023-2024年与2025-2026年的市场制度存在明显差异。
  - 交易者需关注市场制度变化对策略有效性的影响。
- **回测线索**：回测显示该策略在2025-2026年表现优异，但在2023-2024年因隔夜跳空而落后于买入持有。
- **风险**：隔夜跳空风险和策略对市场波动率变化的敏感性。
- **策略价值**：该讨论提醒算法交易者注意市场微观结构变化对策略表现的重大影响，尤其是隔夜波动对日内期权策略的冲击。
- **筛选评分**：74
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1u543cy/anyone_else_find_20232024_to_be_mostly_overnight/)

---

### 参考约束的多期均值-方差高维投资组合优化

- **收录时间**：2026-06-16 07:31
- **发布时间**：2026-06-15 12:00
- **作者**：Yutao Deng, Jianjun Gao, Weichen Wang
- **来源**：arXiv Quantitative Finance
- **分类**：因子 · multi · global
- **摘要**：多期均值-方差投资组合优化是Markowitz静态模型的扩展。该框架对估计误差敏感。本文提出参考约束的多期均值-方差框架，惩罚偏离参考组合的行为。该优化结合了动态策略和参考组合的优势。关键贡献是在高维渐近条件下刻画了样本外夏普比率。研究表明参考惩罚和投资期限共同影响优化表现。正则化在多期与单期优化中作用不同。仿真和实际数据表明该框架显著提高了稳定性和样本外夏普比率。
- **要点**：
  - 提出参考约束多期均值-方差框架，减少估计误差影响。
  - 在高维渐近下理论刻画样本外夏普比率。
  - 通过惩罚偏离参考组合实现动态与静态平衡。
  - 实证显示显著改善多期策略的稳定性和夏普比率。
- **回测线索**：论文通过模拟和实际数据验证了改进的夏普比率。
- **风险**：均值和协方差矩阵的估计误差可能导致性能偏差。
- **策略价值**：该研究为高维投资组合优化提供了理论支撑和实用方法，有助于实际投资中提高风险调整后收益。
- **筛选评分**：75
- **原文**：[链接](https://arxiv.org/abs/2606.13697)

---

### jzd101/突破跟随101

- **收录时间**：2026-06-16 07:31
- **发布时间**：2026-06-15 21:03
- **作者**：jzd101
- **来源**：GitHub Quant Repos
- **分类**：趋势跟踪 · forex · global
- **频率**：intraday
- **摘要**：这是一个基于突破跟随趋势策略的自动化量化交易系统。该系统专门针对黄金（XAUUSD）进行了优化。它通过布林带突破来交易波动性扩张。系统使用EMA确认趋势方向，并用成交量均线过滤信号。策略代码使用Python编写。该项目在GitHub上有2颗星。该系统旨在自动化执行突破交易。
- **要点**：
  - 基于突破跟随趋势策略，专为黄金交易优化。
  - 使用布林带、EMA和成交量均线作为信号。
  - 采用Python实现，自动化执行交易。
- **风险**：虚假突破和震荡市场中的回调风险。
- **策略价值**：该策略为黄金交易者提供了一个自动化的突破跟踪系统，有助于捕捉趋势性波动机会。
- **筛选评分**：79
- **原文**：[链接](https://github.com/jzd101/breakout-follow-101)

---

### 二次抛售论被打破？

- **收录时间**：2026-06-16 07:31
- **发布时间**：2026-06-16 05:42
- **作者**：medphysik
- **来源**：Reddit r/algotrading
- **分类**：趋势跟踪 · stock · us
- **频率**：intraday
- **摘要**：作者通过自举法分析QQQ历史中5%日内跌幅后的走势，探讨二次抛售的可能性。当前QQQ走势已显著超过历史预期范围。结果相当惊人。后续需关注伊朗和平消息及通缩冲击对美联储会议的影响。
- **要点**：
  - 使用自举法分析QQQ历史5%日内跌幅事件。
  - 当前走势突破历史预期范围。
  - 认为二次抛售论可能失效。
- **回测线索**：bootstrapping prior events to compare current price action against historical ranges
- **风险**：limited sample size; historical patterns may break due to regime change; event-driven uncertainty
- **策略价值**：该分析有助于交易者理解极端下跌后的市场行为，及时调整风险敞口。
- **筛选评分**：80
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1u6ucoe/secondary_flush_thesis_broken/)

---

### LeFi8/autobacktest - AI驱动的量化交易策略自动回测优化工具

- **收录时间**：2026-06-16 07:31
- **发布时间**：2026-06-16 01:17
- **作者**：LeFi8
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · multi · global
- **摘要**：该项目是一个AI驱动的量化交易策略自动回测优化工具。它利用LLM代理、回测引擎和统计门控，实现策略的迭代优化。支持多种交易策略的回测与优化。使用Python语言开发。旨在通过自动化流程提高策略开发效率。
- **要点**：
  - 结合LLM代理和统计门控进行策略迭代优化。
  - 支持自动化回测与参数优化。
  - 开源项目，适合量化开发者使用。
- **回测线索**：AI-driven iterative backtesting optimization with statistical gates for strategy refinement
- **风险**：overfitting and lookahead bias if not carefully controlled; user must ensure proper data splitting
- **策略价值**：该工具可大幅降低策略开发和回测的手动工作，加速从想法到实盘的转化。
- **筛选评分**：82
- **原文**：[链接](https://github.com/LeFi8/autobacktest)

---

### 检测LLM预测中的超前偏差

- **收录时间**：2026-06-16 07:31
- **发布时间**：2026-06-15 12:00
- **作者**：Zhenyu Gao, Wenxi Jiang, Yutong Yan
- **来源**：arXiv q-fin.TR (Trading)
- **分类**：机器学习 · stock · us
- **摘要**：本文提出了一种统计程序，用于检测大型语言模型生成的经济预测中的超前偏差。利用仅包含日期的召回查询，估计模型内化已实现结果信息的概率，称为超前倾向（LAP）。在样本期内，LAP显著为正，而在训练数据截止点后基本降至零。研究表明，在准确性回归中，LAP与LLM预测的正交互作用表明存在超前偏差污染。该测试应用于两个预测任务：新闻标题预测股票回报和财报电话会议记录预测资本支出。在两个应用中，高LAP的公司-日期组合上LLM预测的预测能力被放大，而在训练截止后的样本中交互作用失去显著性。该测试为评估LLM生成预测的有效性和可靠性提供了一种经济高效的诊断工具。
- **要点**：
  - 提出超前倾向（LAP）统计量用于检测LLM预测中的超前偏差。
  - 在训练数据截止点前LAP显著为正，截止后接近零。
  - LAP与LLM预测的正交互作用指示偏差污染。
  - 新闻标题和财报电话会议两个任务验证了测试有效性。
- **风险**：lookahead bias contamination may inflate predictive power; interaction test loses significance post-training-cutoff
- **策略价值**：该测试有助于鉴别LLM在金融预测中是否无意中使用了未来信息，从而提升模型的可信度和实际应用价值。
- **筛选评分**：85
- **原文**：[链接](https://arxiv.org/abs/2512.23847)

---

### 如何判断策略是真的在衰减还是处于正常回撤？

- **收录时间**：2026-06-15 23:44
- **发布时间**：2026-06-12 17:14
- **作者**：Historical_Blood_408
- **来源**：Reddit r/algotrading
- **分类**：综合/其他 · multi · global
- **摘要**：一位交易者讨论了如何区分策略衰减和正常回撤。他们建议从回测中定义预期的回撤分布，只有当实际回撤超过第95百分位数时才减仓或停止。此外，还建议单独跟踪交易层面的优势（如平均盈亏比和胜率），因为PnL可能持平而优势逐渐减弱。这种方法提供了统计上的触发点，减少主观判断。然而，即使如此，交易者仍然会不断质疑自己的决策。
- **要点**：
  - 使用回测中的回撤分布作为基准，以第95百分位数为行动触发点。
  - 独立监控交易层面的优势指标，以检测衰减。
  - 避免仅凭主观感受调整策略。
- **回测线索**：Uses expected drawdown distribution from backtest as benchmark; suggests tracking edge statistics from backtest.
- **风险**：Risk of overfitting drawdown distribution; strategy decay may be subtle; psychological temptation to second-guess.
- **策略价值**：为量化交易者提供了一种系统化的方法来识别策略失效，避免过早放弃或过度持有。
- **筛选评分**：60
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1u3q7ko/how_do_you_tell_a_strategy_is_actually_decaying/)

---

### 从期权中恢复风险中性矩

- **收录时间**：2026-06-15 23:44
- **发布时间**：2026-06-15 12:00
- **作者**：Tjeerd De Vries
- **来源**：arXiv Quantitative Finance
- **分类**：期权 · forex · global
- **摘要**：本文提出了一种投影估计方法，用于从期权价格中提取风险中性依赖性，解决了自Ross (1976)以来的开放问题。该方法利用观察到的期权投资组合来近似依赖于多个资产的支付函数，在不完全市场中提供估计，并具有有限样本误差界。将该方法应用于瑞士国家银行关于欧元/瑞郎下限的两个意外公告，发现依赖性占欧元/瑞郎和美元/瑞郎同时大幅下跌概率变化的三分之二。因此，针对欧元/瑞郎的政策重塑了瑞郎市场的依赖性。
- **要点**：
  - 提出一种投影估计器从期权价格中提取风险中性依赖性。
  - 方法适用于不完全市场并提供有限样本误差界。
  - 实证显示瑞士央行公告中依赖性解释了三分之二的风险变化。
- **风险**：Incomplete markets; dependence estimation may be sensitive to model assumptions.
- **策略价值**：该技术可帮助投资者更好地理解期权隐含的资产间依赖关系，从而改进风险管理和定价。
- **筛选评分**：65
- **原文**：[链接](https://arxiv.org/abs/2601.14852)

---

### Hermes Quant自主系统性研究前十名优胜策略

- **收录时间**：2026-06-15 23:44
- **发布时间**：2026-06-15 22:01
- **作者**：paappraiser
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · multi · global
- **摘要**：该仓库列出了来自Hermes Quant自主系统性研究的前十名优胜量化交易策略。使用Python实现，但未提供具体策略细节或回测结果。可作为策略灵感来源。
- **要点**：
  - 包含十种不同的量化交易策略。
  - 来自Hermes Quant的自主研究。
- **策略价值**：提供了多个经过自主研究筛选的优胜策略，可能为投资者带来启发。
- **筛选评分**：85
- **原文**：[链接](https://github.com/paappraiser/quantloop-top10)

---

### 基于订单簿不平衡的量化交易回测工具

- **收录时间**：2026-06-15 23:44
- **发布时间**：2026-06-15 23:14
- **作者**：lukaszkazala
- **来源**：GitHub Quant Repos
- **分类**：做市 · stock · global
- **频率**：intraday
- **摘要**：该仓库提供了一个基于订单簿不平衡和市场微观结构分析的量化交易策略。使用Python实现，但未提供详细的策略逻辑或回测结果。订单簿不平衡通常用于高频交易和做市策略。
- **要点**：
  - 策略基于订单簿不平衡指标。
  - 属于市场微观结构分析。
- **策略价值**：订单簿不平衡是高频交易中的常见信号，该仓库为研究和回测提供了基础工具。
- **筛选评分**：85
- **原文**：[链接](https://github.com/lukaszkazala/orderbook-imbalance-backtester)

---

### 系统性周度期权收入策略的方法论与经验总结

- **收录时间**：2026-06-15 23:44
- **发布时间**：2026-06-15 23:23
- **作者**：RationalBeliever
- **来源**：Reddit r/algotrading
- **分类**：期权 · stock · us
- **频率**：weekly
- **摘要**：该策略交易单一标的的周度期权，每周卖出定义风险的信用价差，持有至到期或触发止损。回测跨度约十年，约540周，使用真实成交价和每条腿手续费。核心采用信念层级排序：最深、溢价最高的设置优先，否则降至较低层级，最后为现金或小额多头溢价。不同波动率下最佳设置不同，层级动态调整攻击性。最关键、最反直觉的教训是：止损策略必须按层级设置，高信念层级不可设定工作止损，否则会破坏优势。深层设置无工作止损，仅有一个样本内从未触发的宽幅后盾，因为深层设置盘中会暂时下跌但到期前恢复，止损只会锁定本应盈利的亏损。只有浅层（近价且恢复缓慢）使用工作止损。触发时机与水平同样重要，中等速度的“等待突破后退出”窗口表现最差。深层设置通过结构性而非反应性的方式避免灾难，在十年最差的一周中未产生任何合格交易，未遭受损失。
- **要点**：
  - 策略基于周度期权信用价差，信念层级动态调整。
  - 高信念层级不应设止损，低信念层级需要止损。
  - 触发时机比触发水平更重要。
- **回测线索**：回测跨度约十年（约540周），采用真实成交价和每条腿手续费。关键发现：止损必须根据市场状态设置；高信念层级不使用激活止损。
- **风险**：尾部风险、期权指派风险、流动性风险、波动性模式变化风险。
- **策略价值**：提供了期权收入策略设计的系统性框架和反直觉的止损规则，对实盘和回测有重要指导意义。
- **筛选评分**：90
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1u6jpeo/discussion_of_my_methodology_and_learnings_for/)

---

### 期货数据：如何处理合约换月？

- **收录时间**：2026-06-15 07:03
- **发布时间**：2026-06-14 07:03
- **作者**：nuclearmeltdown2015
- **来源**：Reddit r/algotrading
- **分类**：机器学习 · futures · global
- **频率**：daily
- **摘要**：该讨论聚焦于期货数据中合约换月（rollover）的处理方法，特别是针对机器学习模型训练。用户提到使用“巴拿马运河”法进行向后调整，但被建议改用比例调整法以保留价格变化的幅度。例如，10年前原油从70涨到75是大波动，但向后调整后看起来像180到185，幅度变小，不利于模型学习。用户尝试将新3个月数据拼接并向后调整历史数据，但发现回测结果显著变差。经过审计，怀疑是调整方法影响了模型预测。用户询问其他交易者如何选择调整方法，是否直接使用原始数据，以及遇到类似问题的解决方式。
- **要点**：
  - 向后调整会扭曲价格变化的幅度，可能降低机器学习模型的学习效果。
  - 比例调整法被建议用于保留价格变化的相对大小。
  - 加入新数据后回测结果显著变化，提示调整方法对模型性能影响很大。
- **回测线索**：Adding 3 months of data with back adjustment drastically changed backtest results, highlighting sensitivity to adjustment method.
- **风险**：Back adjustment distorts price magnitude (e.g., old moves appear smaller), may confuse ML models; raw data may have gaps/large jumps at roll points.
- **策略价值**：正确的合约换月处理对于期货量化交易模型的稳定性和准确性至关重要，不恰当的方法会导致模型失效。
- **筛选评分**：70
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1u54spe/futures_data_how_to_handle_rollovers/)

---

### Krexibd/quant-trading - 量化交易策略库

- **收录时间**：2026-06-15 07:03
- **发布时间**：2026-06-15 06:57
- **作者**：Krexibd
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · multi · global
- **摘要**：这是一个Python编写的量化交易策略库，包含VIX计算器、蒙特卡洛模拟、配对交易和模式识别等模块。主题涵盖算法交易、自动化量化交易、加密货币量化交易、高频交易和实时交易。支持量化信号生成、策略回测和交易机器人框架。目前获取4个星标，属于小型开源项目。提供API接口用于实盘交易。适合开发者学习和扩展量化交易策略。
- **要点**：
  - 包含VIX计算、蒙特卡洛模拟、配对交易、模式识别。
  - 支持加密货币等资产类别。
  - 提供量化交易框架和API。
  - 语言为Python，星标4。
- **策略价值**：提供了一站式量化交易策略工具集，便于快速实验和部署多种策略。
- **筛选评分**：85
- **原文**：[链接](https://github.com/Krexibd/quant-trading)

---

### QQQ恢复预测与当前对比

- **收录时间**：2026-06-15 07:03
- **发布时间**：2026-06-14 21:04
- **作者**：medphysik
- **来源**：Reddit r/algotrading
- **分类**：均值回归 · stock · us
- **频率**：daily
- **摘要**：本报告对QQQ在52周高点附近下跌的历史进行了深入统计分析。使用bootstrap方法计算中位数指标，发现中位数主要跌幅为-3.86%，次要跌幅为-4.74%。中位数到达底部所需时间为11个交易日。初始跌幅与后续下跌的相关性无统计显著性，因此无法预测底部。技术指标如RSI、MACD等在确认底部时易发出错误信号，导致死猫反弹。回测基于21次历史事件，样本量有限。投资者在应用此策略时需警惕市场尾部风险和假突破。
- **要点**：
  - 中位数主要跌幅-3.86%，次要跌幅-4.74%，底部时间约11天。
  - 初始跌幅对后续底部无统计预测能力。
  - 技术指标在底部识别中常出现假信号。
  - 回测样本量小，需谨慎外推。
- **回测线索**：基于21次历史交易，使用10000次bootstrap迭代计算中位数和95%置信区间，评估跌幅和底部时间。
- **风险**：统计能力有限，无法根据首次跌幅预测底部；技术指标易给出虚假信号（死猫反弹）。
- **策略价值**：为量化买入下跌策略提供了基于统计的预期参数，但强调不可依赖单一指标进行择时。
- **筛选评分**：90
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1u5knm1/projected_qqq_recovery_versus_current/)

---

### Krexind/quant-trading - 量化交易策略库

- **收录时间**：2026-06-15 07:03
- **发布时间**：2026-06-15 06:55
- **作者**：Krexind
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · multi · global
- **摘要**：这是一个Python实现的高级量化金融策略库，包含VIX计算器、模式识别、蒙特卡洛模拟、Heikin-Ashi指标和配对交易。主题涉及布林带、MACD、动量策略、期权策略、统计套利和基本面量化分析。支持商品交易和加密货币交易。提供交易机器人框架和回测系统。目前已获36个星标，社区认可度较高。适合中高级量化开发者使用。
- **要点**：
  - 包含多种经典策略：配对交易、动量、统计套利、期权策略。
  - 结合基本面与量化分析（quantimental）。
  - 支持商品和加密货币交易。
  - 星标36，较活跃。
- **策略价值**：提供了丰富的量化策略模板和基本面整合思路，适合构建多策略交易系统。
- **筛选评分**：85
- **原文**：[链接](https://github.com/Krexind/quant-trading)

---

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
