# 量化策略汇总

> 自动生成 · 最后更新：2026-07-02 07:08 · Asia/Shanghai
> 共 189 条策略

## 目录

- [2026-07（13）](#2026-07)
- [2026-06（176）](#2026-06)

---

## 2026-07

### 通过大偏差生成合理的压力场景

- **收录时间**：2026-07-02 07:08
- **发布时间**：2026-07-01 12:00
- **作者**：Anand Deo
- **来源**：arXiv Quantitative Finance
- **分类**：综合/其他 · multi · global
- **摘要**：本文提出了一种基于大偏差原理的系统性压力场景生成方法。该方法能在外推极端场景时保持压力机制的相对合理性。即使历史数据中缺乏极端观测，该程序也能生成有信息量的压力场景。在两种金融网络模型上的数值实验表明，该方法能准确恢复压力损失分布和关键压力诊断指标。相比之下，基准生成器无法产生任何压力样本。该方法为压力测试提供了更可靠的场景选择。
- **要点**：
  - 利用大偏差原理生成合理的极端压力场景，避免人工选择的偏差。
  - 能在外推过程中保持压力机制的相对合理性，即使历史数据有限。
  - 在金融网络模型上验证，成功恢复压力损失分布，优于基准方法。
- **回测线索**：Numerical experiments on two financial network models show the method recovers stressed loss law and key diagnostics, even when benchmark generators fail.
- **风险**：Model risk: relies on large-deviations principle and assumed risk factor dynamics; may not capture true tail dependencies.
- **策略价值**：该方法改进了压力测试中的情景生成，使得极端风险更易于评估和管理，对金融机构的风险管理有实际应用价值。
- **筛选评分**：65
- **原文**：[链接](https://arxiv.org/abs/2606.31122)

---

### 金融巨浪开始的实时识别

- **收录时间**：2026-07-02 07:08
- **发布时间**：2026-07-01 12:00
- **作者**：Rosie Hayward, Orla Lennon, Fabio Biancalana
- **来源**：arXiv Quantitative Finance
- **分类**：机器学习 · multi · global
- **频率**：intraday
- **摘要**：本文将金融波动率与光学和水动力学中的巨浪现象进行类比，利用薛定谔方程和克尔非线性来识别极端事件。通过移动时间窗口分析波动率指标，发现安德森局域化现象在巨浪峰值前出现。方法能实时检测波动率飙升，在VIX、VXO和VSTOXX指数上分别准确识别了除一个外所有主要峰值。回测显示，该方法在合理历史数据下能预警87.5%的极端事件。该技术为金融危机预警提供了新工具。
- **要点**：
  - 将金融波动率巨浪类比于光学和水动力学中的巨浪，使用薛定谔方程建模。
  - 通过移动窗口分析，发现最小特征值的数值梯度在极端事件开始时可靠飙升。
  - 在VIX、VXO和VSTOXX上成功检测到87.5%的主要峰值。
- **回测线索**：Out-of-sample tests on VXO and VSTOXX detected 87.5% (7/8) of major peaks.
- **风险**：False positives possible; relies on historical data and specific model assumptions; may not generalize to all financial systems.
- **策略价值**：该方法能实时识别金融极端事件的开始，为风险管理和危机预警提供了有效的量化工具。
- **筛选评分**：70
- **原文**：[链接](https://arxiv.org/abs/2606.31475)

---

### 预测市场中的结算操纵

- **收录时间**：2026-07-02 07:08
- **发布时间**：2026-07-01 12:00
- **作者**：David Dai, Ruizhe Jia, Shihao Yu
- **来源**：arXiv q-fin.TR (Trading)
- **分类**：套利 · crypto · global
- **频率**：intraday
- **摘要**：本文构建了一个模型，展示了预测市场中的结算操纵现象。这些市场的合约结算价格受交易者买卖标的资产的影响。操纵者通过影响结算价格获利，主要来自散户交易者。基于Polymarket的5分钟比特币合约数据，发现结算时刻现货订单流激增，导致价格大幅反转。而15分钟合约中操纵现象基本消失，表明延长合约期限能有效消除操纵。研究结果支持通过市场设计减少操纵。该模型有助于理解预测市场的财富转移和价格发现机制。
- **要点**：
  - 预测市场合约结算价可被交易者操纵，导致财富从散户向操纵者转移。
  - Polymarket的5分钟比特币合约在结算时刻订单流激增，产生价格反转。
  - 15分钟合约无显著操纵，延长合约期限是有效的市场设计手段。
- **风险**：Manipulation may be transient; market design changes could eliminate opportunity. Regulatory and reputational risks.
- **策略价值**：该研究揭示了预测市场中的操纵风险，并为市场设计提供了可操作的改进方向，对监管和平台运营具有重要指导意义。
- **筛选评分**：75
- **原文**：[链接](https://arxiv.org/abs/2606.31675)

---

### 部署100亿印度卢比于印度F&O：严格0.5%月度最大回撤的策略架构

- **收录时间**：2026-07-02 07:08
- **发布时间**：2026-07-01 03:31
- **作者**：socialcalliper
- **来源**：Reddit r/algotrading
- **分类**：期权 · multi · global
- **频率**：daily
- **摘要**：一位来自迪拜自营交易公司的量化开发人员计划进入印度期货和期权市场。他们获得了一个严格的机构授权：100亿印度卢比资本，月目标收益1%，最大月回撤0.5%，胜率约75%，且需要最小化滑点。他们考虑使用Nifty/Bank Nifty指数产品，并探索delta中性期权卖出、日历价差或统计套利策略。他们提出了关于容量与滑点、尾部风险对冲、基础设施以及税务摩擦等问题。需要同行为这些约束下的策略架构提供建议。该策略需要在严格的回撤限制下部署大规模资金。
- **要点**：
  - 机构级授权：100亿印度卢比，月目标1%，最大回撤0.5%
  - 考虑delta中性期权策略、日历价差或统计套利
  - 关注大资金冲击成本和尾部风险对冲
  - 需要专业的基础设施和税务规划
- **风险**：极端尾部风险，大资金冲击成本，印度STT税可能侵蚀高频模型利润，0.5%月度回撤限制非常严格。
- **策略价值**：该讨论展示了在严格风险约束下大规模部署期权策略的实际挑战和解决方案。
- **筛选评分**：85
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1ujz3c0/deploying_100cr_inr_in_indian_fno_strategy/)

---

### NQ超短线交易早期回测结果

- **收录时间**：2026-07-02 07:08
- **发布时间**：2026-07-02 03:09
- **作者**：MalefactorX
- **来源**：Reddit r/algotrading
- **分类**：均值回归 · futures · us
- **频率**：intraday
- **摘要**：这是一个针对NQ期货的超短线交易策略回测结果。回测周期为2026年1月至6月，共174天。初始资金1万美元，最终权益24,565美元，总回报145.65%。同期SPY基准回报8.29%。策略年化复合增长率559.67%。共执行1,140笔交易，其中多头568笔，空头572笔。胜率42.37%，平均每笔盈利0.1278%，最大盈利0.56%，最大亏损0.19%。平均持仓时间12分钟。最大回撤5.77%，夏普比率11.92。策略基于多次时间框架。作者计划将其自动化。该策略已在手动交易中得到验证。
- **要点**：
  - 5个月回测表现强劲，夏普比率11.92
  - 胜率42.37%，但平均盈利为正
  - 持仓时间极短，平均12分钟
  - 最大回撤控制在5.77%
- **回测线索**：5个月回测，1140笔交易，夏普比率11.92，最大回撤5.77%，胜率42.37%，平均持仓12分钟。
- **风险**：样本期短（仅5个月），高频率交易可能导致过拟合，单一合约交易，实盘需考虑滑点和手续费。
- **策略价值**：该回测展示了超短线策略在NQ期货上的潜在高收益，为自动化交易提供了基础。
- **筛选评分**：85
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1ukux8w/early_backtesting_results_nq_hyperscalper/)

---

### 量化板块轮动策略

- **收录时间**：2026-07-02 07:08
- **发布时间**：2026-07-02 06:40
- **作者**：garroshub
- **来源**：GitHub Quant Repos
- **分类**：趋势跟踪 · stock · us
- **摘要**：该策略利用动量和波动率信号进行ETF板块轮动。它是一个量化交易策略，使用Python实现。该策略结合了大型语言模型进行策略分析。策略基于金融、投资策略和量化金融主题。在GitHub上获得11颗星。作者是garroshub。该策略旨在捕捉板块间的相对强弱。使用ETF作为交易工具。
- **要点**：
  - 利用动量和波动率信号进行板块轮动
  - 结合LLM进行策略分析
  - 使用Python实现
  - 专注于ETF交易
- **风险**：板块集中风险；市场体制转变可能影响动量信号。
- **策略价值**：该策略提供了一个系统化的板块轮动方法，结合了传统量化信号与先进的语言模型分析。
- **筛选评分**：90
- **原文**：[链接](https://github.com/garroshub/Quant_Sector_Rotation_Strategy)

---

### unnolavo/xauusd_lab

- **收录时间**：2026-07-01 20:34
- **发布时间**：2026-07-01 10:36
- **作者**：unnolavo
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · futures · global
- **摘要**：这是一个用于分析XAUUSD（黄金兑美元）并开发量化交易策略的研究平台。项目使用Python语言实现。目前该仓库获得0颗星标。平台可能包含数据分析、回测等功能。XAUUSD是重要的全球资产，具有高波动性。该平台旨在帮助交易者开发系统化策略。由于是公开仓库，用户可自由使用和贡献。项目可能还处于早期阶段。量化交易策略的开发需要数据、模型和风险管理。
- **要点**：
  - 专注于XAUUSD（黄金兑美元）的量化交易策略开发。
  - 使用Python语言实现，属于开源研究项目。
  - 目前星标数为0，可能为新项目。
  - 平台性质为研究分析，涵盖数据探索和策略开发。
- **策略价值**：该平台为黄金量化交易提供了一个开源研究起点，有助于降低策略开发门槛。
- **筛选评分**：50
- **原文**：[链接](https://github.com/unnolavo/xauusd_lab)

---

### 刚完成USTEC H4斐波那契策略回测：6年数据，60.3%胜率。对指标有何看法？

- **收录时间**：2026-07-01 20:34
- **发布时间**：2026-07-01 17:39
- **作者**：iam_warrior
- **来源**：Reddit r/algotrading
- **分类**：趋势跟踪 · stock · us
- **频率**：intraday
- **摘要**：作者在USTEC（纳斯达克）H4周期上测试了一个确定性斐波那契模式策略，使用6年历史数据（从1万美元模拟账户开始）。总收益260.60%，净利润36,056美元，胜率60.3%，共574笔交易。利润因子2.77，修正夏普比率3.40，最大回撤仅3.5%。作者认为这样的低回撤与高收益组合看起来过于完美，怀疑可能过度优化。帖子还提到使用内置AI助手根据每日市场状态过滤交易时段。作者在编辑中修正了夏普比率，并指出回测中步行前向和样本外结果不适用于确定性规则。
- **要点**：
  - 策略总收益260.60%，胜率60.3%，利润因子2.77，修正夏普3.40。
  - 最大回撤仅3.5%，作者怀疑过拟合。
  - 使用AI助手辅助判断市场状态，过滤低质量交易机会。
- **回测线索**：6年回测，574笔交易，总收益260.60%，胜率60.3%，利润因子2.77，修正夏普比率3.40，最大回撤3.5%。但作者质疑低回撤的可持续性，可能存在过拟合。
- **风险**：潜在过拟合风险，低回撤可能不可复现；静态参数假设忽略市场状态变化；样本外表现未验证。
- **策略价值**：该帖子提醒量化交易者警惕回测中的过拟合迹象，即使指标看似完美也需审慎验证。
- **筛选评分**：55
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1ukgzs3/just_finished_backtesting_a_fibo_h4_strategy_on/)

---

### baobach/hft_papers —— 量化金融论文精选

- **收录时间**：2026-07-01 20:34
- **发布时间**：2026-07-01 15:32
- **作者**：baobach
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · multi · global
- **摘要**：这是一个精心整理的量化金融论文集，涵盖学术、算法交易、高频交易等主题。支持Python语言，截至报告时获得106颗星。该列表为研究人员和交易者提供了一个集中的文献入口，便于了解HFT领域的最新进展。
- **要点**：
  - 收录多篇HFT相关论文，涵盖策略、市场微观结构等。
  - 资源开源且持续更新，便于学习参考。
- **策略价值**：该合集为量化研究员和交易者高效获取HFT相关文献提供了便利，有助于跟踪学术前沿。
- **筛选评分**：55
- **原文**：[链接](https://github.com/baobach/hft_papers)

---

### 美中贸易战对全球油籽供应链的级联影响

- **收录时间**：2026-07-01 20:34
- **发布时间**：2026-07-01 12:00
- **作者**：Diksha Gupta, Ritwick Mishra, Achla Marathe, Krista Danielle Yu, Anil Vullikanti
- **来源**：arXiv Quantitative Finance
- **分类**：因子 · futures · global
- **摘要**：本文开发了一个基于线性规划的投入产出（IO）模型，以捕捉贸易政策冲击导致的供应链级联中断，并纳入贸易重新分配和生产调整等缓解机制。该模型通过最小化总未满足需求来高效计算近似均衡解。以美中贸易战对全球油籽供应链的影响为例，发现美国对华油籽出口中断70%会导致全球产出损失3.27%，其中中国损失14.02%。允许巴西向中国重新分配20%的油籽可将全球损失降至1.36%，但最终需求仍面临压力。生产扩张作为额外缓解机制，会在减少全球最终需求损失与保护巴西国内流量之间产生权衡。国内重新分配不成比例地将损失转移至小型经济体，而全球来源扩张则更均匀地分布损失。
- **要点**：
  - 使用线性规划IO模型分析贸易战对全球油籽供应链的级联影响。
  - 美国对华油籽出口中断70%导致全球产出损失3.27%，中国损失14.02%。
  - 巴西重新分配20%出口可大幅降低全球损失，但小型经济体承受更大冲击。
- **风险**：模型依赖简化假设和线性规划近似，数据质量影响结果；实际贸易调整可能更复杂。
- **策略价值**：该研究为量化贸易政策冲击对供应链的影响提供了可计算的框架，有助于政策制定者评估缓解措施的效果。
- **筛选评分**：60
- **原文**：[链接](https://arxiv.org/abs/2606.30685)

---

### 基于市场状态条件分布的交易策略比较：应用于标普500的GAMLSS/ZAGA框架

- **收录时间**：2026-07-01 20:34
- **发布时间**：2026-07-01 12:00
- **作者**：Krzysztof Ozimek
- **来源**：arXiv Quantitative Finance
- **分类**：机器学习 · stock · us
- **摘要**：本文提出了一种分布性框架，用于比较交易策略在不同市场条件下的表现。传统方法将回测性能简化为单一数值，忽略了市场状态的影响。作者使用146个样本外回测区间（2002-2025年）对标普500进行测试，计算多项式支持向量机策略（SVMP）和买入持有基准（BH）的调整信息比率。通过广义可加模型对位置、尺度和形状参数进行建模，并采用零调整伽马分布，将分布参数与市场状态协变量（已实现波动率和累计市场动量）关联。策略比较基于在不同市场状态下期望调整信息比率的差异及其方差差异。参数自助法检验了三个零假设，结果显示SVMP与BH的优劣关系取决于市场状态。该GAMLSS/ZAGA框架为传统策略评估提供了严谨且实用的替代方案。
- **要点**：
  - 使用GAMLSS/ZAGA模型对调整信息比率的分布进行建模，并关联市场状态。
  - 实证发现SVMP与BH的绩效优势取决于市场波动率和动量组合。
  - 提供了参数自助检验方法，用于比较期望值和方差在不同市场状态下的差异。
- **回测线索**：Walk-forward backtest with 146 out-of-sample folds on S&P 500 from 2002 to 2025; Adjusted Information Ratio used as performance metric.
- **风险**：Strategy performance is regime-dependent; risks include overfitting and reliance on covariate selection for market regimes.
- **策略价值**：该方法使交易策略评估更贴近实际市场动态，避免单一统计量带来的误导，有助于投资者根据市场环境优化策略选择。
- **筛选评分**：80
- **原文**：[链接](https://arxiv.org/abs/2606.31251)

---

### 两年构建多策略算法投资组合，分享真实数据，好奇如何比较

- **收录时间**：2026-07-01 20:34
- **发布时间**：2026-07-01 18:06
- **作者**：KeepCalmAnCarryOn
- **来源**：Reddit r/algotrading
- **分类**：综合/其他 · multi · global
- **摘要**：作者运行了一个由8个独立策略组成的系统化投资组合，覆盖股票、外汇和加密货币，历时两年。文章分享了每个策略的回测表现，包括年化收益率、夏普比率和最大回撤，时间跨度从1990年到2026年。策略B表现最佳，夏普比率1.88，年化33.2%；策略H则亏损，夏普-0.13。作者还展示了生存偏差校正前后的对比，以及危机期间的累计回报。管道淘汰率约85%，其中有一个策略因前瞻性错误在实盘后被关闭。一个新信号通过了所有测试，目前处于模拟交易阶段。作者向社区提问：长达25年以上的回测中夏普1.7-1.9是否真实？以及实盘的最低夏普门槛应设为多少。
- **要点**：
  - 8个独立策略覆盖股票、外汇和加密货币，回测窗口25-30年。
  - 策略B夏普1.88，年化33.2%；策略H亏损，夏普-0.13。
  - 生存偏差校正显著降低了策略B和D的回测表现。
  - 管道淘汰率85%，曾有一个策略因前瞻性错误失败。
- **回测线索**：回测窗口长达25-30年，经过生存偏差校正，提供了危机期间（如2008年金融危机、2020年新冠、2022年熊市）的累计回报。策略B和D展示了生存偏差校正前后的巨大差异。
- **风险**：可能存在数据窥探偏差；策略H持续亏损但仍运行；曾经发现一个前瞻性错误导致实盘夏普比率变为-0.16；管道淘汰率约85%。
- **策略价值**：该帖子提供了多年多策略回测的真实数据，并诚实地讨论了偏差和风险管理，对评估量化策略的可行性和可靠性具有参考价值。
- **筛选评分**：85
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1ukhgxe/title_2_years_building_a_multistrategy_algo/)

---

### 基于签名的最优执行统计套利策略与路径依赖交易信号

- **收录时间**：2026-07-01 20:34
- **发布时间**：2026-07-01 12:00
- **作者**：Gianmarco Morbelli, Sven Karbach, Mike Derksen
- **来源**：arXiv q-fin.TR (Trading)
- **分类**：套利 · stock · us
- **频率**：intraday
- **摘要**：本文开发了一个基于签名的框架，用于统计套利策略中的最优执行，其中预测信号具有路径依赖性。Alpha过程和交易速度都被建模为时间增强市场路径截断签名的线性泛函，使信号生成和执行处于同一截断签名基础上。该交易规则能够根据信号的实现历史做出反应，同时考虑临时市场冲击、库存暴露、终端清算和近似美元中性。主要贡献是一个二次简化定理：在签名线性交易速度类中，受限的路径依赖执行问题转化为政策系数的有限维凹二次规划。在均值回复对数价差模型下进行合成实验后，发现拟合政策实现了比z-score经典阈值基准更高的周转回报率。文章展示了相同工作流程如何在历史股票配对交易回测中部署，其中拟合签名政策在会计指标上再次优于基准。
- **要点**：
  - 提出基于签名的统计套利最优执行框架，信号与执行统一建模
  - 通过二次简化定理将路径依赖执行问题转化为有限维凹二次规划
  - 合成实验和股票配对回测均显示优于传统z-score基准
  - 考虑了市场冲击、库存风险和终端清算等实际约束
- **回测线索**：Synthetic experiments under mean-reverting log-spread model and historical equity pairs-trading backtest both show fitted signature policy outperforms z-score benchmark.
- **风险**：Model risk from signature truncation, reliance on market impact assumptions, and liquidity constraints during execution.
- **策略价值**：该框架为统计套利交易提供了一种可解析优化的执行方法，能够有效结合路径依赖信号并管理执行风险，具有实际应用价值。
- **筛选评分**：90
- **原文**：[链接](https://arxiv.org/abs/2606.31387)

---

## 2026-06

### KineticSim: A Lightweight, High-Performance Execution Engine for Real-Time Market Simulators

- **收录时间**：2026-07-01 07:06
- **发布时间**：2026-06-30 12:00
- **作者**：Shakya Jayakody, Prarthinie Jayakody
- **来源**：arXiv q-fin.TR (Trading)
- **分类**：综合/其他 · multi · global
- **摘要**：arXiv:2606.21784v2 Announce Type: replace-cross Abstract: Simulating financial markets at scale with multi-agent (Agent-Based) models is critical for market design, regulatory stress-testing, and reinforcement learning, but traditional CPU simulators are bottlenecked by sequential processing while vectorized GPU frameworks suffer from kernel-launch overhead and redundant global-memory round-trips. We formalize, analyze, and evaluate a reusable parallel design pattern: persistent, state-carrying 
- **筛选评分**：70
- **原文**：[链接](https://arxiv.org/abs/2606.21784)

---

### 基于流动性的算法交易策略审计

- **收录时间**：2026-07-01 07:06
- **发布时间**：2026-06-30 12:00
- **作者**：Irene Aldridge
- **来源**：arXiv Quantitative Finance
- **分类**：综合/其他 · stock · us
- **摘要**：本文证明仅从交易和价格历史即可识别算法策略的流动性净需求。通过一个多期后悔分解，该统计量的符号可将线性策略分类为净流动性消费者或提供者，从可观测数据中恢复Kyle（1985）的知情交易者/做市商二分法。在AR(1)成本过程下，该统计量等于策略规模乘以Roll（1984）隐含价差的平方，使得修正直接成为当前非流动性的代理变量。将模型扩展到内生价格影响和N个相关策略的聚合，得到流动性平衡条件，其违反会导致规模为N平方的福利损失，即一种闭式火情销售外部性。利用CRSP股票数据（2016-2025）进行校准，跟踪COVID-19和2022年利率冲击事件期间的隐含价差。该估计量可在O(Tnd)时间内计算。
- **要点**：
  - 仅需交易和价格历史即可识别策略的流动性净需求，无需策略信号或优化问题知识。
  - 统计量的符号将策略分类为流动性消费者或提供者，与Kyle模型一致。
  - 在AR(1)成本下，统计量等于策略规模与隐含价差平方的乘积。
  - 模型扩展至相关策略时，流动性平衡条件违反会导致N平方量级的福利损失。
- **回测线索**：Calibrated on CRSP equity data from 2016 to 2025, tracking implied spreads through COVID-19 and 2022 rate shock episodes.
- **风险**：Fire-sale externality: violation of liquidity-balance condition leads to welfare loss scaling as N squared.
- **策略价值**：该研究提供了一种无需内部信息即可审计算法交易策略流动性影响的方法，有助于监管机构识别潜在的系统性风险。
- **筛选评分**：80
- **原文**：[链接](https://arxiv.org/abs/2606.29018)

---

### 排序空间中的统计套利

- **收录时间**：2026-07-01 07:06
- **发布时间**：2026-06-30 12:00
- **作者**：Y. -F. Li, G. Papanicolaou
- **来源**：arXiv Quantitative Finance
- **分类**：均值回归 · stock · global
- **频率**：intraday
- **摘要**：本文提出在排序空间中研究股票市场动态，即按市值排名而非公司名称对股票进行索引。与传统名称空间相比，排序空间提供了更结构化的市场视角。深度神经网络（DNN）在排序空间中训练时，统计套利表现显著优于名称空间。性能提升源于排序空间更稳健的市场表示以及残差收益更强的均值回归特性，这促进了更有效的学习。研究表明，领域知情的特征变换对于提高深度神经网络在噪声金融环境中的性能至关重要。实验覆盖了大量股票数据，验证了排序空间方法的有效性。文章强调数据变换在机器学习交易策略中的关键作用。
- **要点**：
  - 按市值排名将股票映射到排序空间，降低波动性并提高信噪比。
  - 深度神经网络在排序空间中学习均值回归残差，套利表现更优。
  - 顺序空间的稳健表示减少了噪声干扰，提升了模型泛化能力。
- **回测线索**：论文表明，在排序空间中使用深度神经网络进行统计套利表现优于名称空间，具有更强均值回归特性。
- **风险**：深度神经网络可能过拟合；排序空间的稳定性依赖于市值排名，排名变化可能带来风险；模型在极端市场条件下可能失效。
- **策略价值**：该方法为量化交易中深度学习应用提供了关键的数据预处理思路，通过排序变换显著提升统计套利策略的有效性。
- **筛选评分**：85
- **原文**：[链接](https://arxiv.org/abs/2410.06568)

---

### 如何解析SEC 8-K文件以提取前瞻性指引语言（纯Python，无需NLP）

- **收录时间**：2026-07-01 07:06
- **发布时间**：2026-07-01 02:59
- **作者**：ShowEuphoric
- **来源**：Reddit r/algotrading
- **分类**：因子 · stock · us
- **频率**：daily
- **摘要**：作者构建了一个纯Python管道，用于从SEC 8-K文件中提取前瞻性指引语句。数据源是免费的EDGAR全文搜索API，可快速获取标普500公司的所有8-K文件。实际指引语言通常位于附件99.1（财报新闻稿）中，而非8-K主体部分。句子分割使用正则表达式按句号划分，并过滤掉长度不足30个字符的片段。指引语句的识别基于关键词匹配，包括“guidance”、“outlook”、“expects”等。事件类型分类也采用类似的关键词扫描，用于标记8-K报告的事件类型（如财报发布、指引更新、收购等）。整个过程无需NLP模型或外部依赖，仅依赖标准库，可在廉价VPS上每分钟处理数百份文件。
- **要点**：
  - 使用免费EDGAR API获取8-K文件，无需付费。
  - 通过正则表达式和关键词匹配提取指引语句，无需NLP。
  - 附件99.1是前瞻性指引的主要来源。
- **风险**：关键词匹配可能遗漏上下文或误分类；仅依赖标准库可能无法处理复杂句式；需要定期更新关键词列表。
- **策略价值**：该方法提供了一种低成本、高效率的自动化基本面数据提取方式，可用于构建基于管理层指引的量化因子。
- **筛选评分**：85
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1ujy65z/how_i_parse_sec_8k_filings_to_extract/)

---

### 我的Polymarket套利机器人被迫进行方向性押注，每笔押注有7%以上优势，却损失了3184美元。原因如下。

- **收录时间**：2026-07-01 07:06
- **发布时间**：2026-06-30 23:47
- **作者**：File-Environmental
- **来源**：Reddit r/algotrading
- **分类**：套利 · crypto · global
- **频率**：intraday
- **摘要**：作者运营了一个跨交易所套利机器人，在Polymarket的电子竞技市场上利用体育博彩赔率。机器人通过去杠杆得到公平价值，然后在Polymarket上以7%以上的优势挂出被动限价单，并对冲另一结果以锁定套利。但通常订单仅单边成交，导致未对冲的方向性头寸。尽管这些头寸具有正期望值，但最终累计亏损3184美元。主要原因有两个：一是报价过时，作者抓取的赔率可能滞后30分钟，导致机器人在真实市场变动后仍挂单；二是去杠杆方法（Shin's method）在1月使用后未再验证。数据显示，在2555场比赛中，近三分之一的对局中盘口移动超过5个百分点，而作者的报价停滞不前。LoL和Dota市场的尾部移动可达30个百分点，其中LoL是最大亏损来源。套利部分盈利8293美元，合计净收益约5000美元。作者认为亏损源于逆向选择：其机器人的报价被更知情的交易者利用。
- **要点**：
  - 机器人执行跨交易所套利，但被动限价单导致单边成交，产生方向性风险。
  - 损失3124美元，主要原因是报价过时和去杠杆方法未经验证。
  - 近三分之一的对局中盘口移动超过5个百分点，显示了报价滞后的严重性。
- **回测线索**：净盈利约5000美元，其中套利盈利8293美元，方向性亏损3184美元。
- **风险**：逆向选择：过时的报价被知情交易者利用；假设去杠杆方法（Shin's method）未经验证；订单执行延迟导致方向性风险敞口。
- **策略价值**：该案例揭示了统计套利在实际执行中因价格延迟和模型假设而面临的逆向选择风险，对量化交易系统设计具有警示意义。
- **筛选评分**：90
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1ujsw6m/my_polymarket_arb_bot_forced_me_to_take/)

---

### 大量AI策略 - 方法

- **收录时间**：2026-06-30 20:07
- **发布时间**：2026-06-30 10:51
- **作者**：xburbx1
- **来源**：Reddit r/algotrading
- **分类**：机器学习 · stock · us
- **频率**：daily
- **摘要**：作者利用AI构建了一个连接经纪商的交易平台，并生成了大量具有风险上限的策略。经过多年回测，根据最大回撤、最大连续亏损次数、年化增长率和盈利因子筛选出表现较好的策略。目前50个策略中有约10个正在模拟账户中进行前瞻测试，其中4个表现良好。计划在每策略达到100笔交易后投入真实资金，并在策略突破预设回撤阈值时停止运行。该方法旨在在时间衰减生效前捕获利润。作者询问是否有人尝试过类似的AI驱动方法。
- **要点**：
  - 使用AI生成50个策略，通过回测筛选出10个进行模拟前瞻测试。
  - 筛选指标包括最大回撤、最大连续亏损、年化增长率和盈利因子。
  - 计划在策略完成100笔交易后投入真实资金，并设置最大回撤止损。
- **回测线索**：Backtested over several years; selected strategies based on max drawdown, max losers in a row, CAGR, profit factor.
- **风险**：Drawdown and maximum consecutive losers are key risks; strategies may fail after hitting drawdown limit.
- **策略价值**：展示了如何利用AI大规模生成交易策略并结合严格的回测与风险管理流程，为量化交易者提供了一种系统化的策略开发与部署思路。
- **筛选评分**：80
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1ujd2e6/lots_of_ai_strats_approach/)

---

### 人工智能溢价

- **收录时间**：2026-06-30 20:07
- **发布时间**：2026-06-30 12:00
- **作者**：Nicola Borri, Yukun Liu, Aleh Tsyvinski
- **来源**：arXiv Quantitative Finance
- **分类**：因子 · multi · global
- **频率**：weekly
- **摘要**：该研究利用来自OpenRouter的380万亿个AI消费代币数据（覆盖全球约2%的月度AI消费），分析了AI对公司、市场和工人的影响。通过构建基于代币增长、美元增长和用户增长的AI因子，估计公司层面的AI贝塔，并刻画AI溢价。研究发现，与AI因子正相关的公司（高AI贝塔）后续收益更高，价值加权多空策略每周收益64.1个基点。溢价在密集使用前沿AI（如闭源模型、付费用户、长提示）的维度上显著，而在随意使用或开源模型上不显著。AI溢价不仅存在于科技公司，还扩展到面向消费者和资本密集型行业，但在新兴市场（包括中国）中缺失。在职业层面，非重复性交互工作与AI正相关，而分析性、科学性和操作控制技能负相关。研究还提供了智能体经济崛起的早期证据。
- **要点**：
  - 构建了基于高频AI消费数据的AI因子和AI贝塔。
  - 高AI贝塔公司的多空策略每周超额收益达64.1个基点。
  - AI溢价在闭源模型、付费用户和长提示等前沿使用维度上更大。
  - 溢价在全球范围内存在，但在新兴市场缺失；非重复性交互工作受益更多。
- **回测线索**：A value-weighted long-short strategy earns 64.1 basis points per week based on high AI beta vs low AI beta firms.
- **风险**：The premium is absent in emerging markets including China; heterogeneity across different AI consumption margins; requires access to proprietary OpenRouter token consumption data.
- **策略价值**：该研究为量化投资提供了基于AI实际消费数据的新因子，有助于捕捉AI驱动的跨资产收益机会。
- **筛选评分**：85
- **原文**：[链接](https://arxiv.org/abs/2606.30583)

---

### 文本信号的供应链传播：LLM嵌入与截面收益可预测性

- **收录时间**：2026-06-30 20:07
- **发布时间**：2026-06-30 12:00
- **作者**：Asef Yılkı
- **来源**：arXiv Quantitative Finance
- **分类**：因子 · stock · us
- **摘要**：该研究将大语言模型（LLM）嵌入与供应链知识图谱结合，构建资产定价框架。使用FinBERT嵌入255家标普500公司2011-2025年10-K报告，生成直接和网络增强两类收益预测因子。Fama-MacBeth回归显示网络增强因子具有显著预测力（Newey-West t=-2.64），且不受动量、波动率和规模影响。基于该因子的多空组合年化夏普比0.86，五因子alpha 7.27%（t=2.30）。预测能力在样本外、安慰剂检验和行业中性化后依然稳健。结果表明企业间网络结构包含超越文本披露的定价信息。
- **要点**：
  - LLM嵌入经供应链知识图谱传播后预测力显著提升。
  - 网络增强因子在Fama-MacBeth回归中t统计量显著。
  - 多空组合夏普比率0.86，五因子alpha 7.27%。
  - 预测力在样本外和多重检验中保持稳健。
- **回测线索**：长短期组合年化夏普比率0.86，Fama-French五因子alpha为7.27%（t=2.30），经样本外测试、安慰剂检验和行业中性化验证。
- **风险**：可能受前瞻性偏差影响；模型复杂度较高；供应链数据质量依赖信息来源。
- **策略价值**：结合NLP和供应链网络信息生成新的因子，为跨公司信息传导提供可操作的量化工具。
- **筛选评分**：85
- **原文**：[链接](https://arxiv.org/abs/2606.29290)

---

### 对每个币种组合运行100种策略的模拟盘计划：避免被假阳性误导

- **收录时间**：2026-06-30 20:07
- **发布时间**：2026-06-30 11:18
- **作者**：Low-Ad5658
- **来源**：Reddit r/algotrading
- **分类**：综合/其他 · crypto · global
- **摘要**：作者正在对20种加密货币运行6种策略，并在模拟盘中计入费用。通过让数据自行匹配策略和币种，避免主观猜测。意识到100种组合中少数会因运气表现良好，因此不信任当前的盈利结果。计划使用假发现率校正作为参考，而非硬性阈值，以避免误杀真实但低胜率的趋势策略。尚未有组合盈利超过费用，故仅构建过滤机制。
- **要点**：
  - 模拟盘测试6种策略×20种加密货币的组合，计入费用。
  - 使用假发现率校正作为参考，而非严格统计门槛。
  - 避免硬阈值误杀低胜率但真实的趋势策略。
  - 目前无组合扣除费用后盈利，尚未宣称有效。
- **回测线索**：正在进行模拟盘测试，包含6种策略和20种加密货币，已考虑费用。
- **风险**：多重比较可能导致假阳性；低胜率趋势策略可能被硬性统计阈值误杀。
- **策略价值**：为多策略多品种测试提供了实用的假阳性过滤思路，平衡统计严谨性与策略存活率。
- **筛选评分**：85
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1ujdmtd/running_100_strategy_per_coin_combos_on_paper/)

---

### 反弹无方向：符号、幅度与股票收益可预测性的微观结构

- **收录时间**：2026-06-30 20:07
- **发布时间**：2026-06-30 12:00
- **作者**：Victoria Portnaya
- **来源**：arXiv q-fin.TR (Trading)
- **分类**：均值回归 · stock · us
- **频率**：daily
- **摘要**：基于Fourier-Residue Identity（FRI）分解，发现SPY的滞后一阶自相关性完全由幅度驱动，而非方向反转。符号检验不显著（p=0.11），而总检验p<10^{-12}，表明大波动后次日波动减小是买卖价差反弹的结果。滞后三阶出现显著的方向反转（p=0.02），体现了部分价格调整机制。跨资产面板显示均值回归仅限于交易所交易股票和主权债券，其他资产接近随机游走。所有估计量通过27项单元检验，蒙特卡洛模拟证实GARCH下5%水平正确。研究揭示了传统方差比检验无法区分的两种自相关来源，为交易策略提供了微观结构视角。
- **要点**：
  - SPY的滞后一阶自相关性完全由幅度效应引起，而非方向反转。
  - FRI分解将自相关分为符号和幅度通道，分别检验。
  - 滞后三阶存在方向反转，与部分价格调整相关。
  - 均值回归仅存在于股票和主权债券，其他资产无此特征。
- **回测线索**：Monte Carlo simulation confirms correct 5% size under GARCH; all estimators pass 27 unit tests.
- **风险**：Bid-ask bounce and non-synchronous constituent staleness may introduce magnitude effects without directional reversal; credit ETFs, commodities, FX, and crypto show no mean reversion.
- **策略价值**：该研究准确区分了交易成本驱动的反弹与真正的方向性反转，有助于避免被错误信号误导。
- **筛选评分**：90
- **原文**：[链接](https://arxiv.org/abs/2606.29591)

---

### HRP - 专业级量化研究平台

- **收录时间**：2026-06-30 06:51
- **发布时间**：2026-06-30 00:11
- **作者**：fmag-labs
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · multi · global
- **摘要**：HRP是一个个人使用的专业级量化研究平台。该平台专注于系统化交易策略的开发。项目使用Python语言编写。目前该项目在GitHub上获得了一颗星。它旨在为量化交易者提供全面的研究工具。平台可能包括数据获取、回测和策略分析等功能。HRP适合有一定编程基础的量化研究者。它可以帮助用户从想法到实现完整的策略。平台的设计强调专业性和可靠性。用户可以通过该平台进行策略的快速原型设计和测试。
- **要点**：
  - HRP是一个个人使用的专业级量化研究平台。
  - 专注于系统化交易策略的开发，使用Python编写。
  - 适合有一定编程基础的量化研究者。
- **策略价值**：HRP为量化交易者提供了一个集成的研究环境，有助于加速策略开发流程。
- **筛选评分**：55
- **原文**：[链接](https://github.com/fmag-labs/HRP)

---

### QS-Trader：量化交易策略的回测框架

- **收录时间**：2026-06-30 06:51
- **发布时间**：2026-06-30 02:21
- **作者**：QuantSpaceGit
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · multi · global
- **摘要**：QS-Trader是一个基于Python的量化交易策略回测框架。该框架支持算法交易和金融市场分析。主要编程语言是Python。项目当前处于早期阶段，尚无星标。该框架旨在为量化交易者提供便捷的回测工具。目前缺乏文档和示例策略。用户可自行扩展策略逻辑和数据接口。
- **要点**：
  - Python实现的量化回测框架，支持多种策略。
  - 项目初始阶段，无用户基础或经过验证的用例。
  - 适合作为学习和快速原型开发的工具。
- **回测线索**：Framework for backtesting; no strategy-specific performance reported.
- **风险**：New repository with 0 stars; no evidence of robustness or support.
- **策略价值**：为量化交易者提供开源回测工具，可降低策略开发门槛，但需谨慎评估其可靠性和成熟度。
- **筛选评分**：60
- **原文**：[链接](https://github.com/QuantSpaceGit/QS-Trader)

---

### 重尾分布下全局最小方差投资组合协方差估计的决策几何

- **收录时间**：2026-06-30 06:51
- **发布时间**：2026-06-29 12:00
- **作者**：Xavier Fonseca
- **来源**：arXiv Quantitative Finance
- **分类**：因子 · stock · us
- **频率**：daily
- **摘要**：该论文研究了协方差估计误差如何影响全局最小方差投资组合的表现。作者证明了精确的遗憾恒等式和非渐近界限，表明决策遗憾只通过组合权重的作用依赖估计误差。他们推导了决策几何：GMVP遗憾对误差矩阵的(p-1)维投影不变，且对协方差尺度方向不变。该框架应用于重尾收益（尾指数在2到4之间），建立了遗憾收敛速率。通过偏t/t-copula模拟设计和预注册分析验证了理论。决策聚焦的优势在于更尖锐的常数和集中度折扣，而非更快的速率。该结果补充了决策聚焦学习方法的估计几何和一致性理论。
- **要点**：
  - 协方差估计误差对GMVP的影响可通过决策几何精确刻画，遗憾只与组合权重相关。
  - 在重尾分布下，遗憾收敛速率由中心算子范数速率决定。
  - 决策聚焦方法提供更优常数和集中度折扣，但速率不变。
- **回测线索**：Simulation with skew-t/t-copula and pre-registered analysis confirms theoretical results.
- **风险**：Heavy tails and high conditioning can significantly degrade performance; estimator choice matters less than decision geometry.
- **策略价值**：该研究指导量化从业者应更关注组合权重对误差的敏感性，而非单纯追求协方差估计的精度，从而提升实盘表现。
- **筛选评分**：80
- **原文**：[链接](https://arxiv.org/abs/2606.27462)

---

### Grünwald-Letnikov分数导数检测的（非）有效市场状态与粗糙波动率

- **收录时间**：2026-06-30 06:51
- **发布时间**：2026-06-29 12:00
- **作者**：Daniele Angelini
- **来源**：arXiv Quantitative Finance
- **分类**：因子 · stock · us
- **频率**：daily
- **摘要**：该论文提出了一种基于离散Grünwald-Letnikov分数导数的自适应Kolmogorov-Smirnov检测框架。该框架能够从单次观测轨迹中识别分数过程的自我相似性，克服了长期记忆下的相位转变问题。GL滤波器去除了低频长期记忆奇异性，同时保留了有限维H自相似性。作者推导了滤波后的经验过程极限，证明了Hurst估计量的一致性及局部渐近行为。通过蒙特卡洛模拟验证了方法的有效性。在金融应用中，该方法能检测到实现波动率和股指价格中的粗糙波动率及市场状态。该方法可识别持续性、反持续性及有效市场状态。论文为市场状态分类提供了新的统计工具。
- **要点**：
  - 引入基于Grünwald-Letnikov分数导数的自适应KS框架，克服了长期记忆下的相位转变。
  - 证明了新Hurst估计量的一致性和局部渐近行为。
  - 在实现波动率和股指价格中成功检测到粗糙波动率和不同市场状态。
- **回测线索**：Monte Carlo simulations validate the method; applied to realized volatility and equity index prices.
- **风险**：Method is statistical and may not directly translate to trading performance; long-memory assumptions may not hold in all regimes.
- **策略价值**：该研究为量化交易者提供了一种新的统计工具，能够更准确地识别市场状态，从而优化风险管理与策略设计。
- **筛选评分**：85
- **原文**：[链接](https://arxiv.org/abs/2606.27932)

---

### Claude算法交易机器人，2周零亏损

- **收录时间**：2026-06-29 22:02
- **发布时间**：2026-06-29 06:46
- **作者**：TastyTrading
- **来源**：Reddit r/algotrading
- **分类**：趋势跟踪 · stock · us
- **频率**：daily
- **摘要**：一位Reddit用户分享了其基于Claude的算法交易机器人的经验，该机器人在两周内实现了零亏损。机器人交易TQQQ和SQQQ，旨在每天正确预测方向。第1天买入TQQQ，第2至第9天仅买入SQQQ，因1.5%隔夜跳空过滤规则而跳过两天。用户编写了一个自定义Ruby脚本，使用K线数据生成信号，并通过Claude MCP在Robinhood上执行。整个系统在一次晚餐讨论后的一天内构建并回测。用户因记录时间短而保持怀疑，但态度乐观。用户邀请其他交易者分享他们的剥头皮策略。
- **要点**：
  - 两周内零亏损，但样本量小，仅2周。
  - 策略为每日方向性交易，使用3倍杠杆ETF TQQQ和SQQQ。
  - 系统使用Ruby脚本生成信号，Claude MCP对接Robinhood执行。
  - 存在过度拟合风险，杠杆ETF放大了潜在亏损。
- **回测线索**：Backtested in one day, but no performance metrics provided.
- **风险**：Very short live track record (2 weeks); uses leveraged ETFs (3x) which amplify losses; small sample size; potential overfitting; reliance on a single daily direction call.
- **策略价值**：展示了利用AI工具（Claude）快速搭建交易系统的可能性，但需警惕短期业绩的不可持续性。
- **筛选评分**：50
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1uib768/claude_algo_bot_2_weeks_0_losses/)

---

### 金融工具集：量化金融应用合集

- **收录时间**：2026-06-29 22:02
- **发布时间**：2026-06-29 16:11
- **作者**：ShauryaGoel1305
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · multi · global
- **摘要**：该仓库包含11个端到端量化金融应用。应用使用Python和Streamlit构建。涵盖股票分析、衍生品定价、投资组合优化等功能。还包括回测和基于NLP的交易策略。适合对量化金融各领域感兴趣的开发者。每个应用均可独立运行和交互。代码开源，便于学习和修改。目前尚无星标，可能为新建项目。用户可基于这些工具快速构建自己的策略。但需注意各模块的数据依赖和假设。
- **要点**：
  - 包含11个量化金融应用，覆盖股票、期权、组合优化等。
  - 所有应用基于Python和Streamlit，可交互使用。
  - 集成NLP驱动的交易策略，扩展了传统量化方法。
- **风险**：工具集合涵盖多种功能，但需自行验证各模块的准确性和实用性
- **策略价值**：该项目为量化金融从业者提供了一个全面的开源工具集，可加速策略开发和教学。
- **筛选评分**：80
- **原文**：[链接](https://github.com/ShauryaGoel1305/Finance-Tools)

---

### 日内期货回测指标分享

- **收录时间**：2026-06-29 22:02
- **发布时间**：2026-06-29 10:58
- **作者**：whereisurgodnow
- **来源**：Reddit r/algotrading
- **分类**：趋势跟踪 · futures · us
- **频率**：intraday
- **摘要**：用户在Reddit分享其日内期货算法回测结果。回测覆盖2019年至2026年6月。交易品种包括MES、MNQ和M2K微型期货。回测仅基于点值，未考虑滑点和佣金。MES执行天数1218天，总点数8315.97，日均6.83点。胜率约57.6%，夏普比率2.77，最大回撤760.89点。MNQ执行天数1099天，总点数40613.48，日均36.95点。胜率57.8%，夏普比率3.09，最大回撤2948.28点。用户正在进行模拟交易以验证策略。
- **要点**：
  - 日内期货策略在MES、MNQ、M2K上均取得高夏普比率（>2.5）。
  - 回测未考虑滑点和佣金，实际收益可能低于报告值。
  - 胜率约57.6%-57.9%，且多空收益均衡。
- **回测线索**：回测显示2019-2026年高夏普比率和胜率，但未包含滑点和佣金
- **风险**：未计入滑点和佣金，实际表现可能较差；当前仅基于点值计算，需考虑交易成本
- **策略价值**：该回测指标展示了日内期货策略的潜在盈利能力，但提醒了交易成本对实际表现的重要影响。
- **筛选评分**：85
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1uigjwq/intraday_futures_backtest_metrics/)

---

### 动量与均值回归量化交易策略

- **收录时间**：2026-06-29 22:02
- **发布时间**：2026-06-29 21:38
- **作者**：lenafilko
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · stock · global
- **摘要**：该仓库实现了一个向量化回测模拟引擎。引擎评估的是一种混合阿尔法策略。该策略结合了截面动量与均值回归模型。均值回归部分采用了逆波动率缩放。项目使用Python编写。目前该仓库尚未获得星标。策略的详细参数和实现细节需查看代码。该引擎适用于量化策略的初步验证。
- **要点**：
  - 混合了截面动量和逆波动率缩放均值回归两种模型。
  - 提供向量化回测引擎，适合策略验证。
  - 使用Python实现，易于扩展。
- **回测线索**：此为回测引擎，可对混合策略进行模拟评估
- **风险**：策略为混合模型，但未提供具体绩效数据，需自行验证
- **策略价值**：该策略结合两种经典因子，为量化交易者提供了一个可复用的混合策略回测框架。
- **筛选评分**：90
- **原文**：[链接](https://github.com/lenafilko/Momentum-Mean-Reversion-Quantitative-Trading-Strategy)

---

### CrayonDing0909/quant-binance-spot - 币安现货量化交易框架

- **收录时间**：2026-06-29 06:58
- **发布时间**：2026-06-29 02:04
- **作者**：CrayonDing0909
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · crypto · global
- **摘要**：1. 这是一个针对币安现货市场的量化交易框架。2. 支持回测、策略开发和实盘交易。3. 使用Python语言编写。4. 提供完整的交易功能模块。5. 适合加密货币量化交易者。6. 目前处于早期阶段，没有任何星标。7. 可能包含基本的风控和订单管理功能。
- **要点**：
  - 专为币安现货设计的量化框架，支持回测与实盘。
  - 基于Python，易于扩展。
  - 项目刚起步，需谨慎使用。
- **回测线索**：Framework includes backtesting functionality.
- **风险**：New repository (0 stars); limited documentation; untested in production; potential bugs.
- **策略价值**：为加密货币量化交易者提供了一个可定制的现货交易框架，降低了开发门槛。
- **筛选评分**：65
- **原文**：[链接](https://github.com/CrayonDing0909/quant-binance-spot)

---

### Building a Simple LONG/SHORT Fractal Strategy in TradingView

- **收录时间**：2026-06-29 06:58
- **发布时间**：2026-06-29 03:54
- **作者**：Droy-333
- **来源**：Reddit r/algotrading
- **分类**：综合/其他 · multi · global
- **摘要**：Can someone help? I’m working on a fractal trading strategy and I want to code it properly in TradingView. The basic idea is simple: Higher timeframe gives the bias, lower timeframe gives the entry. I don’t want to overcomplicate it with too many concepts. The model is mainly: Daily /for bias 1H for swing entry 1h for structure sconfirmation Then only LONG or SHORT signals on the chart I’m trying to make it more mechanical so I can backtest it properly instead of just eyeballing setups. The part
- **筛选评分**：70
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1ui6zcw/building_a_simple_longshort_fractal_strategy_in/)

---

### 关于“周一确立周基调”的16年NQ回测验证

- **收录时间**：2026-06-29 06:58
- **发布时间**：2026-06-28 22:36
- **作者**：jjd1226
- **来源**：Reddit r/algotrading
- **分类**：趋势跟踪 · futures · us
- **频率**：weekly
- **摘要**：1. 研究者对NQ（纳斯达克100期货）进行了16年的回测，检验“周一确立周基调”的说法。2. 发现到周三时，价格相对周一开盘价的方向能预测周收盘方向，准确率约76%。3. 该结果在样本外数据中保持有效。4. 策略核心逻辑是观察周三价格高于或低于周一开盘价。5. 若周三价格高于周一开盘，则周收盘大概率高于周一开盘。6. 反之则周收盘低于周一开盘。7. 该模式在16年数据中持续有效。8. 未提及交易成本、滑点等因素。9. 仅适用于NQ单一品种。10. 需要警惕市场环境变化导致模式失效。
- **要点**：
  - 周三价格相对周一开盘的方向预测周收盘方向准确率达76%。
  - 基于16年NQ数据，样本外验证有效。
  - 策略简单，仅需每日开盘和收盘数据。
- **回测线索**：16 years backtest on NQ; out-of-sample validation; 76% accuracy
- **风险**：Single instrument tested; transaction costs and slippage not accounted; potential regime change; overfitting risk.
- **策略价值**：提供了一个简单且历史验证有效的周度方向预测信号，可用于期货或指数交易。
- **筛选评分**：90
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1uhywj4/kept_hearing_monday_sets_the_tone_for_the_week_so/)

---

### imlast999/MT5交易机器人

- **收录时间**：2026-06-28 19:45
- **发布时间**：2026-06-28 09:25
- **作者**：imlast999
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · multi · global
- **频率**：intraday
- **摘要**：这是一个用Python开发的MetaTrader 5算法交易机器人。它集成了Discord通知功能。该机器人支持历史回测、滚动前测试、模拟交易和实盘执行。它提供了一个实时网页仪表板来监控交易。机器人包含高级风险管理功能。它针对EURUSD、XAUUSD和BTCEUR进行了量化策略验证。项目使用Python语言，当前星标数为1。
- **要点**：
  - 完整的交易生命周期支持：回测、模拟、实盘。
  - 集成Discord通知和实时网页仪表板。
  - 适用于外汇、黄金和加密货币交易对。
- **回测线索**：Historical and walk-forward backtesting available.
- **风险**：Risks include technical failures in live trading and overfitting during strategy validation.
- **策略价值**：该机器人提供了一个易于使用的MT5自动化交易解决方案，适合个人交易者快速部署和测试策略。
- **筛选评分**：90
- **原文**：[链接](https://github.com/imlast999/BOT-MT5)

---

### GGTEFG/机器学习交易研究

- **收录时间**：2026-06-28 19:45
- **发布时间**：2026-06-28 18:53
- **作者**：GGTEFG
- **来源**：GitHub Quant Repos
- **分类**：机器学习 · multi · global
- **摘要**：这是一个用于交易的量化机器学习研究框架。它实现了诚实的滚动前验证，包括数据清洗和禁入期、缩减夏普比率和泄露检测。该框架支持XGBoost、CatBoost和PyTorch模型。它还包含一个策略生成器，可自动创建交易策略。框架生成MetaTrader 5的EA文件。项目使用Python语言开发，当前星标数为0。框架旨在提高量化交易研究的可靠性和严谨性。它提供了一系列工具来防止过拟合和数据泄露。
- **要点**：
  - 采用严格的滚动前验证方法，包括数据清洗和禁入期。
  - 支持多种机器学习模型：XGBoost、CatBoost、PyTorch。
  - 内置策略生成器，可自动生成MQL5 EA。
- **回测线索**：Walk-forward validation with purge/embargo, deflated Sharpe ratio, and leakage detection.
- **风险**：Risk of overfitting and model decay over time.
- **策略价值**：该框架为机器学习交易研究提供了严谨的验证流程，有助于避免常见的数据泄露和过拟合问题。
- **筛选评分**：95
- **原文**：[链接](https://github.com/GGTEFG/ml-trading-research)

---

### 2026年QQQ回撤与二次冲击恢复分析

- **收录时间**：2026-06-28 06:58
- **发布时间**：2026-06-27 21:19
- **作者**：medphysik
- **来源**：Reddit r/algotrading
- **分类**：均值回归 · stock · us
- **频率**：daily
- **摘要**：该分析研究了2026年QQQ的回撤和二次冲击恢复模式，并与历史相似事件进行了对比。历史中，类似的市场冲击中初始回撤中位数为-12.3%，通常在18个交易日内触底。2026年回撤幅度为-12.0%，但下跌过程持续了103天，属于缓慢下跌而非快速暴跌。尽管如此，恢复力度强劲，当前价格已比危机前峰值高出11.5%，优于历史中位数的+8.2%。二次冲击（即反弹后的再次回调）的平均深度为-6.4%，持续时间中位数为17天，95%置信区间为-10.2%至-2.5%。典型历史范围显示，二次冲击深度通常在-3.0%至-8.5%之间，持续时间8至27天，回调幅度抹去此前反弹的25.5%至77.5%。截至2026年6月下旬，当前二次冲击深度为-5.2%，处于历史典型范围中心，表明市场可能正在接近调整尾声。该分析基于100,000次自举迭代的均值统计，提供了更紧致的置信区间。
- **要点**：
  - 2026年QQQ回撤幅度-12.0%，与历史中位数-12.3%接近，但耗时103天，远超中位数18天。
  - 二次冲击平均深度-6.4%，95%置信区间-10.2%至-2.5%，持续时间中位数17天。
  - 当前二次冲击深度-5.2%，处于历史典型范围（-3.0%至-8.5%）中心，可能接近调整结束。
- **风险**：Historical patterns may not repeat; 2026 slow bleed deviated from typical flash crash; secondary shock depth and duration vary widely.
- **策略价值**：该分析有助于量化市场在重大回撤后的恢复模式，为投资者提供择时和风险控制的统计参考。
- **筛选评分**：75
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1uh2lyc/analyzing_2026_qqq_drawdown_and_secondary_shock/)

---

### If you test on the same data you optimized on, you don't have a backtest

- **收录时间**：2026-06-28 06:58
- **发布时间**：2026-06-28 06:00
- **作者**：Nvestiq
- **来源**：Reddit r/algotrading
- **分类**：综合/其他 · multi · global
- **摘要**：This is the first thing we check when someone shows us a strategy, and it's where most "great" backtests fall apart. If you tune your parameters on a stretch of data and then measure performance on that same stretch, the result tells you nothing. The system didn't learn an edge, it fit the noise in that specific window. It'll look pristine in testing and unravel the moment it touches data it hasn't seen. So this is what discipline can help fix that: Carve off the last 20-30% of your data before 
- **筛选评分**：80
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1uhf90i/if_you_test_on_the_same_data_you_optimized_on_you/)

---

### 外汇代理表现

- **收录时间**：2026-06-27 19:25
- **发布时间**：2026-06-24 22:35
- **作者**：Actual_Resort1892
- **来源**：Reddit r/algotrading
- **分类**：趋势跟踪 · forex · global
- **频率**：intraday
- **摘要**：该策略在外汇市场上取得了显著收益。EURUSD达到38.7点盈利，CHFJPY盈利61.4点，NZDUSD盈利30.1点，GBPJPY盈利65.7点。交易在5分钟时间框架内执行。这些结果来自单一交易记录，缺乏历史回测验证。策略似乎基于趋势跟踪或动量突破。交易频率较高，属于日内交易。需要注意市场滑点和点差成本可能影响实际表现。该策略可能仅在特定市场条件下有效。用户需谨慎评估其稳健性。
- **要点**：
  - EURUSD盈利38.7点，CHFJPY盈利61.4点
  - NZDUSD盈利30.1点，GBPJPY盈利65.7点
  - 交易使用5分钟时间框架
- **风险**：Potential overfitting to recent market conditions; slippage and spread costs on 5-minute timeframe may erode profits; sample size of trades is small.
- **策略价值**：该策略展示了高频日内外汇交易中潜在的高收益机会，但需警惕过拟合和执行成本。
- **筛选评分**：55
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1uef9sk/fx_agent_performance/)

---

### Millan678/trading-research-platform

- **收录时间**：2026-06-27 19:25
- **发布时间**：2026-06-27 15:55
- **作者**：Millan678
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · multi · global
- **摘要**：这是一个自主的64阶段研究生态系统，用于系统化交易策略分析、验证和科学发现。平台专注于研究功能，不直接用于实盘交易。支持回测和因果推断。基于Python开发。当前获得0颗星。技术栈包括科学计算和量化分析工具。
- **要点**：
  - 64阶段自主研究生态系统
  - 支持回测与因果推断
  - 仅用于研究目的
- **回测线索**：Supports backtesting and causal inference for strategy validation.
- **风险**：Research-only platform, not intended for live trading. May lack real-time execution and risk controls.
- **策略价值**：该平台为量化研究者提供了完整的策略验证框架，有助于科学发现和策略优化。
- **筛选评分**：55
- **原文**：[链接](https://github.com/Millan678/trading-research-platform)

---

### 每日开盘算法——今日交易

- **收录时间**：2026-06-27 19:25
- **发布时间**：2026-06-26 03:25
- **作者**：Actual_Resort1892
- **来源**：Reddit r/algotrading
- **分类**：趋势跟踪 · forex · global
- **频率**：daily
- **摘要**：该策略基于每日开盘价进行交易。提交者展示了在CHFJPY、GBPJPY和US30上的盈利结果。CHFJPY获利62.2点，GBPJPY获利65.4点，US30获利48.93点。该策略最初流行于股票市场，但也适用于外汇和指数。策略思路是捕捉开盘后的短期动量。交易频率为每日一次。需要关注点差和滑点对收益的影响。
- **要点**：
  - 基于每日开盘价交易
  - 适用于外汇和指数
  - 当日表现盈利
- **风险**：Performance may vary across different market conditions; slippage and spread impact real results. Only one session reported.
- **策略价值**：每日开盘策略简单实用，可跨资产类别应用，适合日内交易者参考。
- **筛选评分**：60
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1ufjvwe/daily_open_algo_todays_session/)

---

### Darkdemon55-cmd/Mylo

- **收录时间**：2026-06-27 19:25
- **发布时间**：2026-06-27 07:50
- **作者**：Darkdemon55-cmd
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · multi · global
- **摘要**：这是一个生产级的智能金融情报平台。它拥有三面板界面，包括AI聊天、策略编辑器和分析仪表盘。平台支持多LLM协调，用于交易算法和量化研究。包含模型路由、辩论系统、安全的Python沙箱。集成了vectorbt和backtrader用于回测。实现了风险控制功能。技术栈包括FastAPI、React、PostgreSQL和Weaviate。
- **要点**：
  - 三面板界面集成AI聊天、策略编辑和分析仪表盘
  - 多LLM协调与辩论系统增强决策能力
  - 内置安全沙箱和风险控制机制
- **回测线索**：Supports backtesting via vectorbt and backtrader.
- **风险**：Secure sandbox limits risk but agentic AI decisions may introduce unforeseen behaviors. Research-only platform not proven in live trading.
- **策略价值**：该平台整合了多智能体AI与量化交易研究，提供了一站式的策略开发与回测环境。
- **筛选评分**：75
- **原文**：[链接](https://github.com/Darkdemon55-cmd/Mylo)

---

### Option prices from operational-time reaction-boundary lattices

- **收录时间**：2026-06-27 07:01
- **发布时间**：2026-06-26 12:00
- **作者**：Chris Angstmann, Tim Gebbie
- **来源**：arXiv q-fin.TR (Trading)
- **分类**：综合/其他 · multi · global
- **摘要**：arXiv:2606.09564v2 Announce Type: replace-cross Abstract: We consider the role of a continuum operational time u and its mapping to calendar time t and how these relate to event time for option pricing problems. We derive option-pricing equations from an operational-time Markov lattice rather than from a calendar-time diffusion. The primitive model is a nearest-neighbour log-price lattice with state- and time-dependent transition probabilities. Its Chapman-Kolmogorov decomposition yields discret
- **筛选评分**：50
- **原文**：[链接](https://arxiv.org/abs/2606.09564)

---

### 影响算法交易的其他因素：应关注哪些股票

- **收录时间**：2026-06-27 07:01
- **发布时间**：2026-06-27 00:04
- **作者**：MormonMoron
- **来源**：Reddit r/algotrading
- **分类**：因子 · stock · us
- **频率**：weekly
- **摘要**：作者运营一个每周优化约95只股票的算法交易系统。系统通过筛选和验证后通常保留45只股票。作者曾移除了SaaS股票，但因配置文件回滚导致意外重仓。该策略从2026年4月21日至回撤前获利13%，但NOW和CRM两只股票造成巨额亏损，最终净收益降至4.5%（基准VTI为3.75%）。在455笔交易中，453笔盈利共3400美元，2笔亏损共2300美元。作者正在寻找更有效的止损机制。
- **要点**：
  - 每周对约95只股票进行优化和筛选，保留约45只。
  - 由于配置文件错误，重新引入了本应排除的SaaS股票。
  - 两笔重大亏损几乎抵消了453笔盈利，强调了分散化和风险管理的重要性。
- **回测线索**：Up 13% from 4/21/26 to peak, then dropped to 4.5% after two losses. Total 455 trades with 99.6% win rate but large average loss on losers.
- **风险**：少数头寸可能造成巨大回撤，如案例中两个SaaS股票导致利润大幅缩水。需要更好的止损策略，但过紧的止损可能误伤盈利交易。
- **策略价值**：凸显了股票筛选和风险管理在算法交易中的关键作用，以及配置管理失误可能带来的严重后果。
- **筛选评分**：70
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1ugazs2/other_things_that_affect_algo_trading_which/)

---

### 今日的几笔盈利

- **收录时间**：2026-06-27 07:01
- **发布时间**：2026-06-26 05:22
- **作者**：ilovezwatch
- **来源**：Reddit r/algotrading
- **分类**：综合/其他 · stock · us
- **频率**：intraday
- **摘要**：作者利用Claude（AI工具）和自身交易理论开发了一个算法交易系统。该系统经过反复回测和优化，目前能生成做多和做空信号。作者仍需手动输入交易，但计划次日实现自动下单。界面最初为终端，后来增加了网页显示。作者表示策略仍在改进中，并非完美。
- **要点**：
  - 使用AI工具Claude辅助开发算法交易策略。
  - 经过回测和迭代优化，目前能捕捉多空信号。
  - 计划从手动交易过渡到全自动化执行。
- **回测线索**：Backtested and iteratively improved the strategy.
- **风险**：目前仍需手动执行交易，存在操作延迟和错误风险。策略仍在开发中，尚未经过完全实盘验证。
- **策略价值**：展示了个人交易者如何利用AI工具快速构建和迭代量化策略，并逐步实现自动化。
- **筛选评分**：75
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1ufmzot/couple_wins_today/)

---

### USD/UZS交易回测引擎

- **收录时间**：2026-06-27 07:01
- **发布时间**：2026-06-26 18:02
- **作者**：AdlTokhirov
- **来源**：GitHub Quant Repos
- **分类**：趋势跟踪 · forex · global
- **频率**：daily
- **摘要**：这是一个基于Python的开源量化回测引擎。它专注于美元兑乌兹别克斯坦苏姆（USD/UZS）汇率。该引擎采用移动平均线交叉策略生成交易信号。用户可以使用历史数据测试策略表现。项目源码托管在GitHub上，目前星标数为0。它提供了回测框架，但尚未包含实盘交易功能。
- **要点**：
  - 使用移动平均线交叉策略进行交易信号生成。
  - 专注于美元兑乌兹别克斯坦苏姆（USD/UZS）这一小众外汇对。
  - 基于Python开发，提供完整的回测框架。
- **回测线索**：Backtesting engine for moving average crossover on USD/UZS
- **风险**：Moving average crossover strategies can produce whipsaws and lag in trending markets.
- **策略价值**：为新兴市场外汇对提供了可定制的量化回测工具，有助于探索非主流交易品种。
- **筛选评分**：85
- **原文**：[链接](https://github.com/AdlTokhirov/usd-uzs-trading-backtester)

---

### 请批评我的黄金模型

- **收录时间**：2026-06-26 20:10
- **发布时间**：2026-06-26 07:57
- **作者**：JanaBhar
- **来源**：Reddit r/algotrading
- **分类**：因子 · futures · global
- **频率**：monthly
- **摘要**：该模型将黄金月度收益分解为宏观因子可解释部分和残差（不可解释部分）。使用实际利率、美元强弱、信用利差和通胀变化作为预测变量，通过岭回归拟合。标准化在1973-2002年，从2003年开始滚动预测。当前不可解释部分处于第90百分位，历史上这种高位往往导致黄金在12-24个月内大幅下跌。但模型同时发现当残差处于上升趋势时，黄金在6-12个月内有70%概率上涨，形成矛盾信号。模型有两个高残差区间：1979-1982和1982-1984，以及2025年9月至今。
- **要点**：
  - 岭回归模型将黄金收益分解为宏观因子和残差
  - 当前残差处于历史第90百分位，历史上后12-24个月黄金通常下跌
  - 但残差上升趋势时，黄金短期（6-12个月）上涨概率达70%
- **回测线索**：使用1973-2002年数据标准化，2003年开始滚动岭回归；模型分解黄金月度收益为可解释和不可解释部分。
- **风险**：模型基于历史关系，可能因市场结构变化而失效；不可解释部分处于极高分位时黄金通常下跌，但短期趋势可能相反，存在信号冲突。
- **策略价值**：提供了一种利用宏观因子的黄金择时方法，但揭示了短期趋势与长期风险之间的冲突，对构建策略有警示意义
- **筛选评分**：50
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1ufqqkl/some_pls_critique/)

---

### 量化智投 - A股量化交易平台

- **收录时间**：2026-06-26 20:10
- **发布时间**：2026-06-26 12:35
- **作者**：zhangshujuan1314
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · stock · cn
- **摘要**：QuantZhiTou是一个基于人工智能的量化交易平台，专注于A股市场。该平台提供策略回测、参数优化、蒙特卡洛模拟、模拟交易和风控功能。使用Python编程语言。目前拥有0颗星（截至发布时）。旨在为量化交易者提供一站式解决方案。
- **要点**：
  - AI驱动的量化交易平台，支持A股市场
  - 包括回测、优化、模拟交易和风险控制
  - 目前处于初期阶段，星数为0
- **策略价值**：为A股量化交易者提供了一个集成了AI和多种功能的开源平台，降低了量化交易的门槛
- **筛选评分**：65
- **原文**：[链接](https://github.com/zhangshujuan1314/quanttrader)

---

### 重尾收益下的大宗商品ETF投资组合优化

- **收录时间**：2026-06-26 20:10
- **发布时间**：2026-06-26 12:00
- **作者**：Nicholas Appiah, Ali Jaffri, Dilmi C. W. Hettiachchi-Halpe-Kankanamalage, Svetlozar T. Rachev
- **来源**：arXiv Quantitative Finance
- **分类**：因子 · stock · us
- **频率**：daily
- **摘要**：本文研究了大宗商品ETF在重尾收益分布下的投资组合优化问题。使用2018年12月12日至2024年12月16日30只美国上市大宗商品ETF的每日数据，涵盖农业、能源、金属和广泛商品指数。比较了被动买入持有、均值方差和条件风险价值（CVaR）优化组合（含纯多头和限制多空策略）。结果显示能源和广泛商品指数基金波动性、偏度和超额峰度显著。历史优化表明最小风险和CVaR组合表现更稳定，改善了夏普、卡尔玛和STARR0.95比率。极值诊断显示优化组合仍面临尾部风险。动态扩展（ARMA-GARCH、t-copula、一步预测）在结合最小风险或CVaR目标时提升了表现，但动态均值方差切线组合因预期收益估计误差表现不佳。交易成本检验表明实际价值依赖于换手率控制，低换手率的动态CVaR切线组合更具韧性。总之，大宗商品ETF配置受益于保守和下行风险意识优化，但仍需显式尾部风险和实现诊断。
- **要点**：
  - 采用最小风险和CVaR优化的投资组合提供了更稳定的累计表现
  - 动态优化结合ARMA-GARCH和t-copula在CVaR目标下效果更好
  - 交易成本控制对动态优化实际效果至关重要
- **回测线索**：Backtest from 2018-12-12 to 2024-12-16 using rolling optimization; dynamic extension with ARMA-GARCH and copula improves performance.
- **风险**：Heavy-tailed returns cause extreme downside risk; optimized portfolios still exposed to tail risk; transaction costs can erode dynamic gains.
- **策略价值**：为大宗商品ETF投资者提供了在重尾风险下进行稳健资产配置的实用框架和风险考量
- **筛选评分**：75
- **原文**：[链接](https://arxiv.org/abs/2606.26625)

---

### 预训练时间序列基础模型用于金融收益率预测

- **收录时间**：2026-06-26 20:10
- **发布时间**：2026-06-26 12:00
- **作者**：Miquel Noguer I Alonso, Rodolfo Pereira Franklin
- **来源**：arXiv Quantitative Finance
- **分类**：机器学习 · stock · us
- **摘要**：本文在保守的金融环境下评估了预训练时间序列基础模型（TSFM）与从头训练的神经网络基线。测试了TimeGPT、TimesFM、Moirai、Chronos等模型，与NBEATS、NHITS、PatchTST、iTransformer、KAN在五只美国流动性股票（AAPL、AMZN、GOOG、JPM、META）上进行对比。使用线性收益率和对数收益率，在均衡上下文预算和滚动起点协议下比较。预训练TSFM在排名分布中占主导地位，Moirai-2.0和TimesFM-2.5平均排名最强，在AAPL、JPM、GOOG、AMZN任务上领先。然而，iTransformer基线赢得了META的两个任务，表明本地监督学习仍可超越通用预训练。重要的是，相对于随机漫步基准的收益很小且稀疏。仅Chronos在AMZN和Moirai-2.0在GOOG上的Diebold-Mariano检验拒绝了同等或更差的预测准确性。结论是TSFM可作为实用的先验，降低低数据场景下的模型开发成本，但并非产生统计可靠阿尔法的通用引擎。
- **要点**：
  - 预训练TSFM在排名上占优，Moirai-2.0和TimesFM-2.5表现最佳。
  - 相对于随机漫步的预测提升很小，仅两个案例统计显著。
  - 本地监督学习（iTransformer）在特定资产上仍可优于预训练模型。
- **回测线索**：Models outperformed random walk only for Chronos on AMZN and Moirai-2.0 on GOOG (Diebold-Mariano test).
- **风险**：Low signal-to-noise ratio in financial returns; gains over random walk are small and sparse; not a universal solution for alpha generation.
- **策略价值**：该研究表明预训练时间序列模型可作为有用的先验降低开发成本，但在实际部署中不能依赖其产生稳定的超额收益，对量化选股策略的实用性有限。
- **筛选评分**：80
- **原文**：[链接](https://arxiv.org/abs/2606.27100)

---

### Angad2005/Trading-Strategy（交易策略）——增强型布林带均值回归策略量化回测框架

- **收录时间**：2026-06-26 20:10
- **发布时间**：2026-06-26 07:35
- **作者**：Angad2005
- **来源**：GitHub Quant Repos
- **分类**：均值回归 · multi · global
- **摘要**：这是一个端到端量化回测框架，实现了增强型布林带均值回归策略。该框架包含基于ATR的风险管理、真实的交易成本模拟和市场状态分析。代码使用Python编写，目前在GitHub上获得1颗星。策略通过布林带识别超买超卖信号，并结合平均真实波幅（ATR）动态调整止损和仓位。框架支持用户自定义参数，便于在不同市场条件下进行测试。该回测框架提供了完整的回测流程，包括数据获取、策略执行、绩效评估和可视化。它旨在帮助量化交易者快速验证和优化均值回归策略。
- **要点**：
  - 基于布林带的均值回归策略，结合ATR风险管理。
  - 包含真实交易成本和市场状态分析。
  - Python实现，提供完整的回测流程。
- **回测线索**：Framework includes ATR-based risk management, realistic transaction costs, and regime analysis.
- **策略价值**：该框架为量化交易者提供了一个即用型的回测工具，特别适合快速验证和优化基于布林带的均值回归策略，降低了策略开发的门槛。
- **筛选评分**：80
- **原文**：[链接](https://github.com/Angad2005/Trading-Stratergy)

---

### 基于深度强化学习的加密货币市场动态多对交易策略

- **收录时间**：2026-06-26 20:10
- **发布时间**：2026-06-26 12:00
- **作者**：Damian Lebiedz, Robert Slepaczuk
- **来源**：arXiv q-fin.TR (Trading)
- **分类**：套利 · crypto · global
- **频率**：intraday
- **摘要**：本研究旨在确定深度强化学习（DRL）作为专业执行覆盖层能否增强加密货币市场中高度波动的配对交易。尽管该策略的传统实现在传统股票市场中被证明是成功的，但在高方差环境中常常表现出僵化并面临严重的发散风险。为了应对这一需求，本研究引入了创新概念。我们开发了分层“过滤-排序”配对选择方法和专有的“固定风险，自适应均值”执行模型。该系统采用具有长短期记忆（LSTM）层的近端策略优化（PPO）代理，在严格确定性风险管理边界内指导执行决策。在币安USD-M期货市场的1小时间隔数据上评估，优化后的强化学习策略在样本外表现显著优于启发式基线。平稳圆形块自举鲁棒性检验证实，代理的风险调整后超额表现在10%水平上统计显著。尽管略低于更严格的5%阈值，但这一结果凸显了数字资产特有的极端异质方差。最终，本文通过引入统计套利与DRL执行策略相结合的混合架构，为量化金融文献做出了贡献。此外，它通过确定性屏蔽提供了一种新颖的安全强化学习框架，证明将神经策略锚定在统计稳健边界上能有效缓解严重的发散风险。
- **要点**：
  - 采用分层“过滤-排序”方法选择交易对，并应用“固定风险，自适应均值”执行模型。
  - 使用带有LSTM层的PPO代理，在确定性风险管理边界内优化执行决策。
  - 在币安USD-M期货1小时间隔数据上，样本外表现显著优于启发式基线。
  - 鲁棒性检验表明风险调整后超额收益在10%水平显著，但未达到5%标准。
- **回测线索**：Out-of-sample outperformance over heuristic baseline; robustness confirmed via stationary circular block bootstrap at 10% significance.
- **风险**：Extreme idiosyncratic variance typical of digital assets; statistical significance only at 10% level, not 5%; divergence risks mitigated by deterministic shielding.
- **策略价值**：该策略展示了如何将深度强化学习与统计套利结合，通过确定性屏蔽安全地应用于高波动加密货币市场，为量化交易提供了新的混合架构。
- **筛选评分**：85
- **原文**：[链接](https://arxiv.org/abs/2606.04574)

---

### 有没有人过去或现在将Webull Level 2 API接入到他们的设置中？

- **收录时间**：2026-06-26 07:12
- **发布时间**：2026-06-23 10:12
- **作者**：_WARBUD_
- **来源**：Reddit r/algotrading
- **分类**：做市 · stock · us
- **频率**：intraday
- **摘要**：1. 该帖子来自Reddit r/algotrading社区。
2. 用户询问是否有人目前或曾经将Webull Level 2 API集成到其交易设置中。
3. 作者表示，没有Level 2数据如同让交易机器人蒙眼作战。
4. 他提到Webull的Level 2数据提供50层深度。
5. 作者还提供了相关端点和截图的链接。
6. 他正在寻求有实际集成经验的交易者的反馈。
- **要点**：
  - 作者询问Webull Level 2 API接入经验
  - 认为没有深度数据如同蒙眼交易
  - 提供了50层深度数据的截图链接
- **策略价值**：Webull Level 2 API的集成可以显著提升基于订单流和深度数据的交易策略的精确度。
- **筛选评分**：50
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1ud4b1e/does_anyone_have_webull_level_2_api_plugged_in_to/)

---

### 连续时间下的无模型投资组合配置

- **收录时间**：2026-06-26 07:12
- **发布时间**：2026-06-25 12:00
- **作者**：Henry Chiu
- **来源**：arXiv Quantitative Finance
- **分类**：综合/其他 · multi · global
- **摘要**：本文提出了一种非概率、路径依赖的连续时间投资组合配置框架，扩展了自融资概念，导出了路径依赖偏微分方程的解，并给出了显式解示例。作为应用，将Vovk的聚合算法和Cover的通用算法扩展到连续时间，实现了多策略组合跟踪，误差界为O(1)和O(ln t)。该工作将Cover定理推广到连续时间无模型设置。
- **要点**：
  - 提出路径依赖的连续时间投资组合框架
  - 将自融资概念扩展到策略配置
  - 给出显式解公式
  - 实现连续时间多策略聚合算法
- **风险**：模型假设价格路径可能不连续且变异性无界，需谨慎处理极端市场条件。
- **策略价值**：该研究为模型无关的投资组合配置提供了严格的数学基础，并扩展了经典通用组合方法到连续时间场景。
- **筛选评分**：60
- **原文**：[链接](https://arxiv.org/abs/2411.05470)

---

### QuantCore量化核心框架

- **收录时间**：2026-06-26 07:12
- **发布时间**：2026-06-26 04:40
- **作者**：Maulikjain2407
- **来源**：GitHub Quant Repos
- **分类**：机器学习 · multi · global
- **摘要**：一个端到端的量化交易框架，支持机器学习驱动的策略开发和回测。
- **要点**：
  - 提供完整的策略开发流程
  - 集成机器学习模型
  - 支持回测验证
- **策略价值**：该框架降低了使用机器学习进行量化交易的门槛，使开发者能够快速迭代和验证策略。
- **筛选评分**：60
- **原文**：[链接](https://github.com/Maulikjain2407/QuantCore)

---

### 量化回放收集器

- **收录时间**：2026-06-26 07:12
- **发布时间**：2026-06-25 23:11
- **作者**：Vinnnnnie21
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · crypto · global
- **摘要**：这是一个用于主观加密货币交易分析的K线回放、事件标注、策略一致性审核和量化研究工具。
- **要点**：
  - 提供K线回放功能
  - 支持事件标注
  - 用于策略一致性审核
  - 适用于主观交易分析的量化研究
- **策略价值**：该工具帮助加密货币交易者系统地审核和优化其主观交易策略，提升策略执行的一致性。
- **筛选评分**：65
- **原文**：[链接](https://github.com/Vinnnnnie21/quant-replay-collector)

---

### 如何处理0DTE期权算法的滑点问题？

- **收录时间**：2026-06-26 07:12
- **发布时间**：2026-06-26 01:52
- **作者**：Axonum
- **来源**：Reddit r/algotrading
- **分类**：期权 · stock · us
- **频率**：intraday
- **摘要**：一位交易者分享了其实盘0DTE期权算法遇到的问题。从模拟交易转到实盘后，入场时出现显著滑点。限价中点订单经常无法成交，因为价格在提交后很快移动了5%甚至10%。询问是否应改用市价单来保证成交。社区成员可能讨论订单类型选择、流动性考虑和滑点控制方法。该帖反映了高频期权策略实盘执行中的典型挑战。
- **要点**：
  - 0DTE期权实盘交易中限价单常因价格快速移动而无法成交。
  - 滑点主要出现在入场阶段，退出相对可控。
  - 固定使用市价单可能加剧滑点，需平衡成交概率与成本。
- **风险**：0DTE期权流动性高度时段性，滑点大；限价单可能无法成交，市价单可能导致过度滑点；价格快速波动易导致执行偏差。
- **策略价值**：该问题指出了日内期权策略实盘执行的核心难点，引发对订单执行算法的深入讨论。
- **筛选评分**：70
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1ufhadr/how_to_deal_with_slippage_for_my_0dte_options_algo/)

---

### 具有潮流、知情和不知情交易者的做市策略

- **收录时间**：2026-06-26 07:12
- **发布时间**：2026-06-25 12:00
- **作者**：Emilio Barucci, Adrien Mathieu, Leandro Sánchez-Betancourt
- **来源**：arXiv q-fin.TR (Trading)
- **分类**：做市 · stock · global
- **频率**：intraday
- **摘要**：该研究刻画了一个连续时间最优流动性提供问题的解，市场中同时存在知情和不知情交易者。模型中，资产价格表现出潮流——即相对于基本价值的短期偏离。基于潮流值，对知情和不知情交易者的到达过程进行了建模。做市商知道存在这两组交易者，但仅能观察匿名订单到达。研究了做市商控制问题的完全信息和部分信息版本。在这些框架下，刻画了信息的价值，并找到了流动性价格与市场中知情交易者比例的函数关系。讨论了如何从市场数据校准模型参数，并量化了相对于忽略这些不可观测短期偏差的策略的超额收益。对于部分信息设置，探讨了如何超越卡尔曼-布西滤波器从市场到达中提取潮流信息。
- **要点**：
  - 做市商面临知情与不知情交易者混杂的订单流，需动态调整报价。
  - 价格短期潮流影响交易者到达，做市商可通过模型提取信息优化决策。
  - 部分信息下可采用比卡尔曼滤波更先进的信号提取方法。
- **回测线索**：讨论了如何从市场数据校准模型参数，并量化了相对于忽略短期偏差策略的超额收益。
- **风险**：存在逆向选择风险，做市商需准确区分知情与不知情交易者；短期价格潮流可能导致库存风险。
- **策略价值**：为做市商在高频环境中利用不对称信息制定报价策略提供了理论框架和实证校准方法。
- **筛选评分**：70
- **原文**：[链接](https://arxiv.org/abs/2501.03658)

---

### 推理-计算前沿与限价订单簿预测的低延迟高效架构

- **收录时间**：2026-06-26 07:12
- **发布时间**：2026-06-25 12:00
- **作者**：C. Evans Hedges
- **来源**：arXiv q-fin.TR (Trading)
- **分类**：机器学习 · stock · us
- **频率**：intraday
- **摘要**：该研究探讨了限价订单簿预测中是否存在类似缩放定律的推理-计算前沿。使用了FI-2010数据集和从决策树到神经LOB的一系列模型。发现预测损失与结构性前向工作之间的经验前沿可以用幂律很好地描述。特别是，将MLPLOB架构族排除后，低中计算量非MLPLOB前沿的幂律拟合能够外推至多个数量级，并在排除的高计算量MLPLOB目标前沿上达到R²=0.941。类似的延迟空间分析结果显著较弱，表明延迟不仅仅是带噪声的计算量。基于这一差距，提出了FastBiNLOB，一种由硬件友好的时间和特征混合操作构建的密集轴可分离LOB混合器。在五种子实验中，FastBiNLOB以显著低于现有已发表最先进架构的延迟超过了已发布的y₁₀和y₁₀₀宏F1目标。
- **要点**：
  - 限价订单簿预测存在推理-计算前沿，可用幂律拟合。
  - 延迟并非简单的带噪计算量，其与预测性能的关系较弱。
  - 提出的FastBiNLOB架构在更低延迟下实现了更高的宏F1分数。
- **回测线索**：在FI-2010数据集上进行了实证验证，展示了预测损失与计算量之间的幂律关系，并对比了MLPLOB等架构的性能。
- **策略价值**：该研究为高频交易中通过适量计算提升预测精度提供了量化基准，并给出了一个实用的低延迟架构方案。
- **筛选评分**：90
- **原文**：[链接](https://arxiv.org/abs/2606.25986)

---

### Q-agent

- **收录时间**：2026-06-25 20:15
- **发布时间**：2026-06-24 21:06
- **作者**：WolfpackOfOne
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · multi · global
- **摘要**：该框架是一个基于智能体的量化研究框架，专注于数据管道、笔记本和交易策略开发。使用Python语言实现。项目在GitHub上托管，目前获得4颗星。主题包括人工智能代理、Lean算法交易平台、QuantConnect平台以及量化金融。该框架支持多种资产类别和市场。它可作为开发各类量化策略的基础工具。框架设计强调模块化与可扩展性。适合研究者快速搭建量化研究环境。
- **要点**：
  - 项目提供智能体驱动的量化研究框架。
  - 支持数据管道、笔记本和策略开发流程。
  - 兼容Lean和QuantConnect等回测平台。
  - 使用Python语言，适合量化研究快速迭代。
- **策略价值**：该框架为量化研究人员提供了一个统一、灵活的智能体平台，可显著加速从研究到策略部署的周期。
- **筛选评分**：60
- **原文**：[链接](https://github.com/WolfpackOfOne/Q-agent)

---

### 面向可持续性感知的多空组合优化的两阶段决策支持系统

- **收录时间**：2026-06-25 20:15
- **发布时间**：2026-06-25 12:00
- **作者**：Giacomo di Tollo, Massimiliano Kaucic, Filippo Piccotto
- **来源**：arXiv Quantitative Finance
- **分类**：因子 · stock · global
- **频率**：daily
- **摘要**：本文提出一个两阶段决策支持系统，用于在ESG约束下优化多空投资组合。第一阶段使用TODIMSort和MEREC方法对资产进行多标准分类，动态生成多空候选集。第二阶段构建最大化Omega比率的非凸优化模型，并采用自适应粒子群算法求解，该算法能从多种重组算子中选择最优算子，并辅以投影修复机制处理约束。实证基于STOXX Europe 600指数的421只股票。结果表明，引入ESG的多空组合在经风险调整后的收益上通常优于非ESG组合和市值加权基准。该系统能够根据市场环境和投资者偏好动态调整。
- **要点**：
  - 两阶段流程：先按ESG指标分类资产，再优化组合权重。
  - 自适应粒子群求解器可动态选择最优算子，提高求解质量。
  - ESG多空组合在STOXX Europe 600上表现优于传统基准。
- **回测线索**：Empirical study on 421 stocks from STOXX Europe 600; ESG-enhanced long-short portfolios show competitive or superior performance versus non-ESG and market-value-weighted benchmarks.
- **风险**：Model risk from multi-criteria sorting and particle swarm optimization; reliance on ESG data quality and availability; non-convex optimization may yield local optima.
- **策略价值**：为可持续投资提供了系统化的量化框架，使投资者能在ESG约束下实现多空策略的优化配置。
- **筛选评分**：65
- **原文**：[链接](https://arxiv.org/abs/2606.25696)

---

### 伊朗策略

- **收录时间**：2026-06-25 20:15
- **发布时间**：2026-06-25 13:25
- **作者**：Must_Dragonfruit
- **来源**：Reddit r/algotrading
- **分类**：因子 · stock · us
- **频率**：daily
- **摘要**：该策略名为“霍尔木兹海峡”，基于地缘政治事件（中东重建）构建主题投资组合。做多重建材料供应链中的股票（如骨料、水泥、钢铁、木材替代品、设备、工程总承包），同时做空SPY。交易为纸面仿真，起始于2026年6月1日，首日收益7%。回测显示年化收益率149%，夏普比率4.77，最大回撤-1.67%，但作者承认存在事后偏见。策略本质是叙事驱动，并非量化优势。持仓包括VMC、MLM、EXP等22只个股，每只权重4.5%，做空SPY权重100%。用户可调整权重和股票池来个性化策略。
- **要点**：
  - 基于中东重建主题，做多材料股、做空SPY。
  - 首日纸面收益7%，但回测可能存在严重过拟合。
  - 作者强调这是叙事倾斜，非可复制的量化策略。
- **回测线索**：Illustrative backtest from 2026-06-01 shows CAGR 149.0, Sharpe 4.77, maxDD -1.67, but flagged as hindsight bias; forward paper trade returned +6.73% on first day.
- **风险**：Geopolitical risk (Middle East conflict), narrative tilt without measured edge, high concentration in reconstruction sector, backtest overfitting potential.
- **策略价值**：展示了如何将地缘政治事件快速转化为主题交易思路，但需警惕回测中的生存偏差和事后偏见。
- **筛选评分**：70
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1uf10vv/the_iran_strategy/)

---

### 基于高频收益的加密货币交互时间依赖加权有向网络

- **收录时间**：2026-06-25 20:15
- **发布时间**：2026-06-25 12:00
- **作者**：Shubhangam Shukla, Mahesh Peyyala, Abhijit Chakraborty
- **来源**：arXiv q-fin.TR (Trading)
- **分类**：机器学习 · crypto · global
- **频率**：intraday
- **摘要**：本研究利用2020-2025年的高频价格数据，构建了加密货币市场的有向加权网络，以分析资产间的相互影响。通过统计显著的Granger因果关系量化了影响流。归一化收益呈现厚尾分布，符合金融市场典型特征。网络显示链接权重和节点强度的高度异质性，少数加密货币对市场动态贡献显著。基于节点出强度排名揭示了动态变化的层级结构。以太坊始终是最有影响力的资产，而比特币的重要性逐渐下降。排名结构随时间大幅变化，多种加密货币交替进入前列。结果表明加密货币生态系统竞争激烈且非稳定。
- **要点**：
  - 以太坊持续位居影响力榜首，比特币重要性下降。
  - 网络链接权重分布不均，少数资产主导市场。
  - 排名结构随时间高度动态，缺乏稳定层级。
- **风险**：Model risk due to Granger causality assumptions; network inference may be sensitive to window length and significance thresholds; heavy-tailed distributions imply tail risk.
- **策略价值**：该研究为理解加密货币市场影响力结构提供了量化框架，有助于识别系统性重要资产和风险传导路径。
- **筛选评分**：75
- **原文**：[链接](https://arxiv.org/abs/2606.25466)

---

### 用于商品期货市场日历价差策略的分层图学习

- **收录时间**：2026-06-25 20:15
- **发布时间**：2026-06-25 12:00
- **作者**：Yoonsik Hong, Diego Klabjan
- **来源**：arXiv q-fin.TR (Trading)
- **分类**：套利 · futures · us
- **摘要**：本文提出了一种分层图学习方法，用于商品期货市场的日历价差策略。商品期货可分层表示：上层为底层资产，下层为单个期货合约。不同层级间的边捕捉资产间相关性，跨层级边连接合约与其底层资产。作者首先从理论上证明日历价差策略具有比多头策略更高的风险调整收益和更低的风险。然后，他们设计了一种方法将学习预测转换为日历价差头寸。该模型利用到期日相关的相互关系预测期货价格波动。在芝加哥商品交易所（CME）集团的期货数据上，该方法在预测和交易表现上均优于基准模型。研究发现，到期日相关的相互关系对预测至关重要。基于分层图学习的日历价差交易可以有效进行统计套利。
- **要点**：
  - 提出分层图学习模型用于商品期货日历价差策略。
  - 理论证明日历价差策略具有更高信息比率和更低风险。
  - 在CME期货数据上表现优于基准，利用跨合约相关性。
- **回测线索**：Empirical results on CME Group futures show superior prediction and trading performance.
- **风险**：Complex model; may require high-frequency data; risk of overfitting to market microstructure.
- **策略价值**：为期货市场统计套利提供了一种新颖的图学习方法，有效利用了合约间的到期日依赖关系。
- **筛选评分**：80
- **原文**：[链接](https://arxiv.org/abs/2606.25811)

---

### 使用机器学习预测周最高价是否超过周中位数高

- **收录时间**：2026-06-25 20:15
- **发布时间**：2026-06-25 13:23
- **作者**：Expert_CBCD
- **来源**：Reddit r/algotrading
- **分类**：机器学习 · stock · us
- **频率**：weekly
- **摘要**：该模型使用机器学习预测某股票周最高价是否超过其中位数高（相对于周一开盘价）。模型使用少于10个变量，训练测试采用滚动10年/1个月周期。仅当预测概率大于60%或小于40%时才执行交易。在SPY上的回测显示，策略1（触及中位数高即卖出）胜率为70.18%，平均每笔收益0.26%。策略2（持有至周五收盘）胜率为57.89%，平均收益0.55%，年化收益率约28.6%。累计利润方面，策略1为54.02%，策略2为142.50%。基线策略（每周买入）胜率仅49.72%。模型在其它ETF和股票上也取得了类似结果。该方法仅基于价格数据，不依赖基本面信息。
- **要点**：
  - 预测周高是否超过中位数高，基于周开盘价。
  - 使用滚动10年/1个月训练测试周期，仅交易高概率信号。
  - SPY回测中策略2年化收益约28.6%，累进利润142.5%。
- **回测线索**：Backtested on SPY from 2005 with rolling 10yr/1mo train-test, achieving 70% win rate on timing exits.
- **风险**：Overfitting risk due to many custom parameters; only tested on SPY and some ETFs; no out-of-sample validation beyond what's shown.
- **策略价值**：展示了一种简单的机器学习方法用于优化周内择时，可能显著提升持有期收益。
- **筛选评分**：85
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1uf0ztl/using_machine_learning_to_predict_whether_weekly/)

---

### EasyQuant 事件驱动量化交易框架

- **收录时间**：2026-06-25 20:15
- **发布时间**：2026-06-25 10:45
- **作者**：AlanFokCo
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · stock · cn
- **摘要**：EasyQuant 是一个针对中国A股市场的事件驱动量化交易框架。它支持策略回测、风险指标分析和实际部署。该框架使用 eqlib 核心库，便于快速开发。项目采用 Python 语言编写，开源且免费。目前拥有13个星标，社区较小但专注。其主要功能包括回测引擎和风险管理系统。该框架适合中国A股市场的个人和机构投资者。它可以帮助用户验证交易策略的有效性。框架的事件驱动模式能够模拟真实市场环境。
- **要点**：
  - 针对中国A股市场的开源量化交易框架。
  - 支持事件驱动策略回测和风险管理。
  - 使用 Python 编写，集成 eqlib 核心库。
- **回测线索**：Framework supports backtesting and risk metric analysis.
- **风险**：Open-source, limited user base (13 stars), may require customization.
- **策略价值**：为A股投资者提供了一个免费、可定制的量化交易研究和部署平台。
- **筛选评分**：90
- **原文**：[链接](https://github.com/AlanFokCo/EasyQuant)

---

### 路径空间鲁棒贝叶斯投资组合选择

- **收录时间**：2026-06-25 07:02
- **发布时间**：2026-06-24 12:00
- **作者**：Andy Au
- **来源**：arXiv Quantitative Finance
- **分类**：机器学习 · stock · global
- **摘要**：该论文提出一种鲁棒贝叶斯投资组合选择方法，投资者通过卡尔曼-布西滤波学习未知资产漂移并交易均值方差最优组合。模型允许对手方以相对熵为代价扭曲观测价格规律，使策略对模型误设具有鲁棒性。由于财富和信念由同一布朗运动驱动，单一扭曲同时影响交易利润和滤波结果。鲁棒策略及其价格可解析求解；至一阶近似，鲁棒性代价为非鲁棒投资者损失方差的一半。该策略通过立方修正项抑制大仓位。在已知漂移情况下，非鲁棒策略成本无限；而在学习环境下损失有限且成本可计算。鲁棒性的新结构源于惩罚项的缩放方式而非学习机制：价值缩放精确保持仿射策略。
- **要点**：
  - 通过卡尔曼滤波学习资产漂移，结合均值方差最优组合交易。
  - 引入对手方扭曲价格观测规律，使策略对模型误设具有鲁棒性。
  - 鲁棒策略解析解显示，代价为损失方差的一半，并通过立方项抑制大仓位。
  - 学习环境使得非鲁棒策略的损失有界，鲁棒性成本有限。
- **风险**：模型误设风险；对手方扭曲观测价格的风险；鲁棒性代价为损失方差的一半。
- **策略价值**：该研究为贝叶斯投资者提供了一种可解析求解的鲁棒组合策略，有效应对模型误设风险。
- **筛选评分**：50
- **原文**：[链接](https://arxiv.org/abs/2606.24212)

---

### TIP-Search: Time-Predictable Inference Scheduling for Market Prediction under Uncertain Load

- **收录时间**：2026-06-25 07:02
- **发布时间**：2026-06-24 12:00
- **作者**：Xibai Wang
- **来源**：arXiv Quantitative Finance
- **分类**：综合/其他 · multi · global
- **摘要**：arXiv:2506.08026v4 Announce Type: replace-cross Abstract: Real-time market prediction services need correct predictions before a decision deadline; a correct prediction delivered late is not usable. TIP-Search studies time-predictable inference scheduling over fixed market predictors under uncertain load. It filters conformal latency-quantile feasible models, dispatches over finite workers, and uses shielded constrained online experts to trade accuracy, queue pressure, and deadline risk. On the 
- **筛选评分**：55
- **原文**：[链接](https://arxiv.org/abs/2506.08026)

---

### MT5 Backtest Analyser

- **收录时间**：2026-06-25 07:02
- **发布时间**：2026-06-23 19:00
- **作者**：alexkyse
- **来源**：Reddit r/algotrading
- **分类**：综合/其他 · multi · global
- **摘要**：Hey reddit, I'm a senior software developer and since long time ago I felt the process of analysing, sharing MT5 backtests and strategies with other members was always a hassle, screenshots, downloading html reports etc, so I decided to build StrategyLens. StrategyLens is free, allows you to analyse your strategies and create portfolios in local, everything stays in your computer, no cloud information is sent unless you decide to share the strategy with other people which has a feature to create
- **筛选评分**：65
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1uddzgz/mt5_backtest_analyser/)

---

### AI交易系统：多智能体LangGraph与事件驱动架构

- **收录时间**：2026-06-25 07:02
- **发布时间**：2026-06-23 22:46
- **作者**：sdalli
- **来源**：GitHub Quant Repos
- **分类**：机器学习 · multi · global
- **频率**：intraday
- **摘要**：这是一个机构级 AI 交易系统，采用多智能体 LangGraph 工作流、TimescaleDB 时序数据库优化和事件驱动的微服务架构。系统设计用于高频市场数据摄入、量化策略执行和自动化投资组合管理，结合 LLM 进行基本面和技术分析。代码库使用 Python 编写，目前星级为 0。系统强调可扩展性和低延迟，适合专业交易环境。多智能体协作可处理复杂决策任务。事件驱动架构确保实时响应。
- **要点**：
  - 多智能体 LangGraph 工作流支持复杂决策。
  - TimescaleDB 优化时序数据存储与查询。
  - 事件驱动微服务架构适合高频交易。
  - 集成 LLM 进行基本面和技术分析。
- **风险**：Complex architecture may introduce latency; LLM-based decisions can be unpredictable; system requires significant infrastructure.
- **策略价值**：该系统展示了如何将先进 AI 架构（多智能体、事件驱动）应用于量化交易，为构建高性能交易系统提供了参考。
- **筛选评分**：75
- **原文**：[链接](https://github.com/sdalli/ai-trading-system)

---

### FinSentQuant：基于FinBERT的量化交易平台

- **收录时间**：2026-06-25 07:02
- **发布时间**：2026-06-24 20:48
- **作者**：harinivs20
- **来源**：GitHub Quant Repos
- **分类**：机器学习 · stock · global
- **频率**：daily
- **摘要**：FinSentQuant 是一个全栈量化交易平台，使用 FinBERT 分析金融新闻情绪并生成交易信号。它能够获取实时股票市场数据，执行基于情绪的策略回测，并与买入持有基准进行比较。平台采用 Python 开发，目前处于初始阶段。情绪分析模型基于 FinBERT，可对新闻文本进行情感分类。回测模块支持自定义策略参数。该平台有助于验证情绪因子在股票交易中的有效性。用户可以通过代码库进行部署和测试。
- **要点**：
  - 利用 FinBERT 进行金融新闻情绪分析。
  - 支持实时数据获取和策略回测。
  - 与买入持有基准进行绩效比较。
  - Python 实现，开源可定制。
- **回测线索**：Includes sentiment-driven strategy backtesting and comparison with buy and hold benchmark.
- **风险**：Sentiment signals may be noisy and subject to news quality; backtest overfitting possible.
- **策略价值**：该平台使交易者能够系统化地利用新闻情绪生成交易信号，提供从数据到回测的完整流程。
- **筛选评分**：80
- **原文**：[链接](https://github.com/harinivs20/FinSentQuant)

---

### 发布 pandas-ta-classic v0.6.52：新增SMC流动性扫荡指标 + Ichimoku/MACD修复

- **收录时间**：2026-06-25 07:02
- **发布时间**：2026-06-24 23:27
- **作者**：AMGraduate564
- **来源**：Reddit r/algotrading
- **分类**：综合/其他 · multi · global
- **摘要**：pandas-ta-classic v0.6.52 版本发布，这是一个社区维护的 pandas-ta 分支。新增了智能资金概念流动性扫荡指标，用于检测流动性扫荡蜡烛形态。该指标返回 +1（看涨扫荡）、-1（看跌扫荡）或 0（无扫荡）。还修复了 Ichimoku 指标的多处 bug，包括返回元组而非 DataFrame 的问题。MACD 扩展指标修复了静默回退的问题，现在会在无效 MA 类型时抛出错误。CPR 指标输出从字符串改为 int8，更便于数值计算。总共包含 193 个指标和 62 个原生 CDL 模式，无需 TA-Lib。安装简单，只需 pip install pandas-ta-classic。社区维护，欢迎反馈和 PR。
- **要点**：
  - 新增 SMC 流动性扫荡指标，参数可调。
  - 修复 Ichimoku 和 MACD 扩展的多个 bug。
  - CPR 输出从字符串改为 int8，提升兼容性。
  - 无需 TA-Lib 即可使用所有形态识别。
- **风险**：SMC indicators can lead to overfitting if parameters are not carefully chosen.
- **策略价值**：该库为量化交易者提供了增强的技术分析工具集，尤其是 SMC 指标可应用于多种资产的回测与实盘。
- **筛选评分**：90
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1uegoa6/release_pandastaclassic_v0652_new_smc_liquidity/)

---

### A-RYAN-KR/回测代理

- **收录时间**：2026-06-24 20:18
- **发布时间**：2026-06-23 20:18
- **作者**：A-RYAN-KR
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · multi · global
- **摘要**：该项目是一个AI驱动的回测和量化交易研究代理。它自动化策略测试、性能分析、风险评价和优化过程。利用大型语言模型驱动的工作流和金融分析技术。支持在历史市场数据上进行策略回测。项目主题包括智能体人工智能、算法交易、自动交易等。使用Python编程语言开发。目前获得0个星标。这是一个开源的回测工具。可以用于量化金融研究和策略开发。它整合了多种金融分析功能。
- **要点**：
  - 自动化回测与性能分析
  - 使用LLM驱动的金融分析工作流
  - 支持多种策略优化
  - 基于Python的开源项目
- **回测线索**：该项目利用LLM驱动的自动化回测和性能分析工作流，支持策略优化。
- **策略价值**：该工具通过AI和LLM技术降低了量化策略回测和优化的门槛，提高了研究效率。
- **筛选评分**：50
- **原文**：[链接](https://github.com/A-RYAN-KR/Backtesting-Agent)

---

### NY Striker V2.2：慢速周后MNQ止损被触发

- **收录时间**：2026-06-24 20:18
- **发布时间**：2026-06-23 01:01
- **作者**：B_Ware321
- **来源**：Reddit r/algotrading
- **分类**：趋势跟踪 · futures · us
- **频率**：intraday
- **摘要**：交易者报告了NY Striker V2.2策略在MNQ微型纳斯达克期货上的表现。策略上周大部分时间未交易，直到一次机会出现。虽然交易接近后止损被轻微触发，但之后价格朝预期方向移动。账户整体仍处于盈利状态，且得益于正滑点。该策略似乎交易频率较低，等待高概率机会。
- **要点**：
  - NY Striker V2.2策略交易MNQ期货，上周大部分时间未交易
  - 一笔交易中，价格仅小幅触及止损后按预期方向运行
  - 账户总体盈利，滑点带来了正向影响
- **风险**：Stop loss clipping risk, slippage impact, low trading frequency may lead to inactivity periods
- **策略价值**：展示了期货算法交易中止损设置与滑点管理的实际案例，对风险控制有参考意义。
- **筛选评分**：70
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1ucqbu5/ny_striker_v22_after_a_slow_week_clipped_mnq_sl/)

---

### 当AI遇上金融（StockAgent）：基于大语言模型的模拟真实环境股票交易

- **收录时间**：2026-06-24 20:18
- **发布时间**：2026-06-24 12:00
- **作者**：Chong Zhang, Xinyi Liu, Zhongmou Zhang, Mingyu Jin, Lingyao Li, Zhenting Wang, Wenyue Hua, Dong Shu, Suiyuan Zhu, Xiaobo Jin, Sujian Li, Mengnan Du, Yongfeng Zhang
- **来源**：arXiv q-fin.TR (Trading)
- **分类**：机器学习 · stock · global
- **摘要**：该研究提出了StockAgent，一个基于大语言模型的多智能体AI系统，用于模拟投资者对真实股票市场的交易行为。系统允许用户评估宏观经济、政策变化、公司基本面等外部因素对交易行为的影响。StockAgent避免了现有模拟系统中的测试集泄露问题，防止模型利用与测试数据相关的先验知识。实验在不同LLM下进行，展示了关键外部因素对股票交易行为及价格波动规则的影响。研究为基于LLM的投资建议和股票推荐提供了有价值的见解。代码已开源。
- **要点**：
  - StockAgent是多智能体LLM系统，模拟投资者交易行为
  - 支持评估多种外部因素对交易的影响
  - 避免了测试集泄露，确保评估公正
  - 为LLM驱动的投资建议提供新思路
- **风险**：Model overfitting risk, reliance on LLM prior knowledge (mitigated by leakage avoidance), simulation realism limitations
- **策略价值**：为利用LLM进行市场仿真和投资策略研究提供了开源框架，具有重要的实践和学术价值。
- **筛选评分**：70
- **原文**：[链接](https://arxiv.org/abs/2407.18957)

---

### Claude算法机器人第二周：100%胜率

- **收录时间**：2026-06-24 20:18
- **发布时间**：2026-06-23 06:39
- **作者**：TastyTrading
- **来源**：Reddit r/algotrading
- **分类**：趋势跟踪 · stock · us
- **频率**：daily
- **摘要**：一位交易者分享了使用Claude MCP连接器和Robinhood代理交易机器人进行交易的经验。机器人每天仅交易一次，选择TQQQ或SQQQ之一，并采用严格的风险管理。在第二周，机器人实现了100%的日胜率，包括一天因市场跳空1.5%而选择不交易。回测结果显示年化收益率45%，最大回撤6.6%，夏普比率2.07。该策略通过简单规则过滤市场异常日，并已连续多日盈利。作者对代理交易机器人充满热情，并推荐其他人尝试。
- **要点**：
  - 机器人每天仅交易一次，使用TQQQ或SQQQ杠杆ETF
  - 第二周实现100%胜率，避开市场跳空日
  - 回测年化收益率45%，最大回撤6.6%，夏普比率2.07
  - 使用Claude MCP和Robinhood的代理交易平台
- **回测线索**：Annualized return: 45%, max drawdown: 6.6%, Sharpe ratio: 2.07 (half in-sample, half out-of-sample, averaged)
- **风险**：Leverage risk from TQQQ/SQQQ, single trade per day increases idiosyncratic risk, gap risk due to overnight gaps, overfitting potential
- **策略价值**：展示了结合LLM和简单规则的高胜率日内交易策略，具有实际参考价值。
- **筛选评分**：75
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1uczfiw/claude_algo_bot_week_2_100_wins/)

---

### 跨收益分布的投资组合管理

- **收录时间**：2026-06-24 20:18
- **发布时间**：2026-06-24 12:00
- **作者**：Jozef Barunik, Lukas Janasek, Attila Sarkany
- **来源**：arXiv Quantitative Finance
- **分类**：因子 · stock · us
- **频率**：daily
- **摘要**：该研究提出了一个动态投资组合选择框架，投资者可以针对收益分布的特定区域进行优化。样本外测试显示，不同分位数策略形成有序前沿：专注于下行风险的策略提供最佳左尾保护和最高夏普比率，而专注于上分位数的策略获得最高平均收益。相比波动率管理组合，这些策略的优势集中在下行尾部分散度高的时期。来自收益、增长和下行保护产品的资金流证据支持将分位数指数视为简化的任务度量指标。该框架为投资者根据自身风险偏好定制投资组合提供了理论支持。
- **要点**：
  - 不同分位数策略形成有序前沿，下行策略夏普比率最高，上分位数策略收益最高。
  - 策略优势主要出现在下行尾部波动较大的时期。
  - 资金流数据验证了分位数指数的实际意义。
- **回测线索**：Out-of-sample tests produce an ordered frontier: downside policy yields highest Sharpe; upper-quantile policy yields highest mean return.
- **风险**：Gains are concentrated in periods of high downside-tail dispersion; performance may deteriorate in calm markets.
- **策略价值**：该框架允许投资者根据其对收益分布不同区域的偏好来动态构建组合，为定制化风险管理提供了可行方法。
- **筛选评分**：85
- **原文**：[链接](https://arxiv.org/abs/2510.19271)

---

### 美国大盘股市场影响平方根定律的实证确认

- **收录时间**：2026-06-24 20:18
- **发布时间**：2026-06-24 12:00
- **作者**：Aniket Vasaikar
- **来源**：arXiv q-fin.TR (Trading)
- **分类**：做市 · stock · us
- **频率**：intraday
- **摘要**：该研究利用纳斯达克TotalView-ITCH逐笔订单数据，对苹果公司股票在178个交易日内的市场影响平方根定律进行了实证检验。通过从匿名交易数据中重建元订单，研究将冲击标准化为I/σ_D = c (Q/V_D)^(1/2)，并固定指数为1/2。原始系数c_raw为0.69，偏差修正后c_eff为0.34，条件冲击随Q^(1/2)变化。订单规模分布的尾部指数β=1.54±0.15。模型比较明确偏好平方根形式，优于线性和对数冲击（ΔAIC=22）。交易符号打乱后定向冲击降至随机水平，事件顺序打乱则破坏平方根定律。底层订单流具有长记忆性（γ=0.66），而价格保持扩散性（Hurst指数0.49）。系数在32周滚动校准中保持稳定。
- **要点**：
  - 平方根定律在苹果公司股票上得到实证支持，系数c_raw=0.69。
  - 模型比较显示平方根形式优于线性和对数形式。
  - 订单流长记忆性与价格扩散性同时存在，符合理论预测。
- **回测线索**：Square-root law confirmed on Apple stock; prefactor c_raw=0.69 stable across weekly walk-forward tests.
- **风险**：Metaorder reconstruction from anonymous tape may introduce noise; results may not generalize to other stocks or market conditions.
- **策略价值**：该研究为交易成本建模和最优执行策略提供了基于美国个股的实证基础，有助于量化交易者更准确地估计市场冲击。
- **筛选评分**：85
- **原文**：[链接](https://arxiv.org/abs/2606.24019)

---

### 机器学习分类与投资组合构建：损失函数重要吗？

- **收录时间**：2026-06-24 20:18
- **发布时间**：2026-06-24 12:00
- **作者**：Yang Bai, Kuntara Pukthuanthong
- **来源**：arXiv Quantitative Finance
- **分类**：机器学习 · stock · us
- **摘要**：该研究比较了分类与回归在投资组合构建中的表现，发现分类模型普遍优于回归模型。采用梯度提升树、随机森林和神经网络的堆叠集成模型，分类策略的年化夏普比率为1.83，而回归策略仅为1.11。这种优势在多分类设置、子样本以及扣除交易成本后依然存在。跨期测试表明，在控制回归后分类仍能产生显著的经济alpha，而回归的alpha在控制分类后大幅缩减。结果表明分类能从收益中提取更多有效信息。诊断分析将分类的优势归因于其对收益十分位更清晰和精确的分离。该研究为机器学习在量化投资中的损失函数选择提供了重要依据。
- **要点**：
  - 分类模型比回归模型在投资组合构建中表现更好，夏普比率更高。
  - 堆叠集成模型（梯度提升树+随机森林+神经网络）表现最优。
  - 分类的优势在于更精确地分离收益十分位。
- **回测线索**：Classification models yield higher Sharpe ratios than regression in out-of-sample backtests, with a stacking ensemble achieving Sharpe 1.83 vs 1.11.
- **风险**：Potential overfitting risk if not properly validated; results may depend on data period and market conditions.
- **策略价值**：该研究为量化投资者在选择机器学习损失函数时提供了实证依据，表明分类目标比回归更能提升投资组合表现。
- **筛选评分**：90
- **原文**：[链接](https://arxiv.org/abs/2108.02283)

---

### 预训练Transformer中的资产定价

- **收录时间**：2026-06-24 07:03
- **发布时间**：2026-06-23 12:00
- **作者**：Shanyan Lai
- **来源**：arXiv Quantitative Finance
- **分类**：机器学习 · stock · us
- **频率**：daily
- **摘要**：本文提出了一种创新的Transformer模型SERT，用于美国大盘股定价，并应用于因子投资环境。模型在包含COVID-19全周期的三个时段中，与标准Transformer和仅编码器Transformer进行对比，检验极端市场波动下的适应性。SERT模型在极端波动期间实现了最高的样本外R²，分别为11.94%和11.47%，优于预训练Transformer模型的11.13%和9.72%。基于SERT的趋势跟踪策略在市场冲击中展示了出色的下行风险对冲能力。在静态交易成本场景下，SERT在等权组合中实现了比买入持有基准高47%的Sortino比率，在市值加权组合中高28%。研究发现，Transformer模型能够有效捕捉资产定价因子模型中的时间稀疏模式，特别是在高波动环境下。软最大信号过滤器作为Transformer模型的常见配置，仅消除了模型间差异，并未提升策略绩效。增加注意力头数对模型性能提升不显著，而采用“先层归一化”方法在本文案例中并未增强模型性能。
- **要点**：
  - SERT模型在COVID-19极端波动期间实现11.94%样本外R²，优于其他Transformer变体。
  - 趋势跟踪策略基于SERT在等权组合中Sortino比率比买入持有高47%。
  - 软最大信号过滤器不改善策略绩效，增加注意力头或层归一化顺序影响不显著。
- **回测线索**：Out-of-sample R^2 up to 11.94% during COVID-19; Sortino ratio improvement 47% (equal-weighted) and 28% (value-weighted) over buy-and-hold.
- **风险**：Model complexity may lead to overfitting; transaction costs considered only in static scenario; performance in calm markets not evaluated.
- **策略价值**：该研究表明预训练Transformer能显著提升资产定价和趋势跟踪策略表现，为极端市场下的风险管理和投资组合优化提供新工具。
- **筛选评分**：50
- **原文**：[链接](https://arxiv.org/abs/2505.01575)

---

### 通过Chiarella模型重新审视过度波动之谜

- **收录时间**：2026-06-24 07:03
- **发布时间**：2026-06-23 12:00
- **作者**：Jutta G. Kurth, Adam A. Majewski, Jean-Philippe Bouchaud
- **来源**：arXiv q-fin.TR (Trading)
- **分类**：因子 · multi · global
- **摘要**：本文修正并扩展了Chiarella金融市场模型，以一致地处理任意长期价值漂移。改进了现有的校准方案，使得可以校准单个月度时间序列而非一类时间序列。该技术应用于从1800年至今的四种资产类别（股票指数、债券、商品、货币）的现货价格。校准直接输出所谓的基本价值，从而可以量化这些市场的过度波动程度，发现其很大（如股票指数约为4倍），并与先前估计一致。同时可以确定错误定价的分布，发现许多情况下是双峰的。这两个发现都与有效市场假说强烈矛盾。还详细研究了校准的‘邋遢性’，即参数空间中受数据约束弱的方向。主要结论在不同资产类别间高度一致，并强化了金融市场中期命运由趋势跟随者和基本面投资者之间的拔河决定的假说。
- **要点**：
  - 利用Chiarella模型校准四种资产类别从1800年至今的数据
  - 发现过度波动程度很大，股票指数约4倍
  - 错误定价分布常呈双峰，与有效市场假说矛盾
  - 趋势跟随者与基本面投资者的博弈决定市场中长期走势
- **风险**：Model calibration sloppiness; parameters weakly constrained; results depend on model assumptions.
- **策略价值**：该研究提供了长期跨资产类别的过度波动量化证据，对理解市场非有效性及资产定价具有重要参考价值。
- **筛选评分**：50
- **原文**：[链接](https://arxiv.org/abs/2505.07820)

---

### 运行了三个独立策略，结果发现它们并不独立

- **收录时间**：2026-06-24 07:03
- **发布时间**：2026-06-23 17:29
- **作者**：Thiru_7223
- **来源**：Reddit r/algotrading
- **分类**：综合/其他 · forex · global
- **摘要**：作者在过去几个月构建了三个独立的交易系统，它们有不同的时间框架、逻辑和交易对。作者认为这些策略实现了多样化，并按照不相关风险对每个策略分配了头寸。出于好奇，作者将三条权益曲线并列查看，发现三个策略在完全相同的三天内发生了回撤。这表明不同的入场逻辑并不一定意味着不同的风险暴露，如果它们都对相同的波动率制度做出反应。作者实际上构建了一个穿着三件外衣的策略，却按照三个独立策略进行头寸规模分配。作者仍在寻找在实际交易前测试这种隐藏相关性的方法。
- **要点**：
  - 三个不同时间框架、逻辑和交易对的策略在同一三天内回撤。
  - 不同入场逻辑的风险暴露可能因共同波动率制度而高度相关。
  - 看似分散的投资组合可能实际上是一个单一的大赌注。
- **风险**：Hidden correlation risk: strategies may appear independent but draw down simultaneously due to common volatility regime, leading to underestimated portfolio risk.
- **策略价值**：该经验强调了在策略组合中识别隐藏相关性的重要性，以避免因低估尾部风险而导致严重损失。
- **筛选评分**：55
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1udcdfz/ran_three_independent_strategies_turns_out_they/)

---

### 无模型估值方法的实证分析：对冲缺口、保守性与交易机会

- **收录时间**：2026-06-24 07:03
- **发布时间**：2026-06-23 12:00
- **作者**：Zixing Chen, Yihan Qi, Shanlan Que, Julian Sester, Xiao Zhang
- **来源**：arXiv q-fin.TR (Trading)
- **分类**：期权 · stock · us
- **频率**：daily
- **摘要**：论文研究了无模型估值方法的质量，通过系统评估无模型超对冲策略与衍生品实际收益之间的差异，使用了2018-2022年标普500成分股的历史期权价格。研究发现无模型对冲方法仅比Heston模型等工业标准略保守，且无需模型假设。基于这一发现，构建了一个明确的交易策略，该策略可盈利地应用于金融市场，并具有明确的下行风险控制。统计描述和模型无关性使得策略具有优势。总之，无模型方法在实际中可行且有效。
- **要点**：
  - 无模型对冲方法仅略保守于Heston模型
  - 构建的策略具有下行风险控制
  - 实证基于2018-2022年标普500成分股期权数据
  - 模型无关性降低模型风险
- **回测线索**：Backtested on S&P 500 constituents from 2018-2022, showing profitable trading strategy with downside risk control.
- **风险**：Model-free approach may be conservative; hedging gaps exist but are small relative to industry models.
- **策略价值**：该研究提供了一种无需模型假设的衍生品估值与交易方法，可有效控制下行风险，具有重要实践意义。
- **筛选评分**：60
- **原文**：[链接](https://arxiv.org/abs/2508.16595)

---

### 考虑信息泄漏的LLM预测基准测试：实时预测作为决策时间输入用于宏观因子排序

- **收录时间**：2026-06-23 20:31
- **发布时间**：2026-06-23 12:00
- **作者**：Mao Guan, Qian Chen
- **来源**：arXiv Quantitative Finance
- **分类**：因子 · stock · us
- **摘要**：本文提出一种控制信息泄漏的LLM预测基准测试方法，应用于权益因子排序。使用检索增强的7B开源LLM预测器，仅依赖决策时间信息：滞后FRED宏观变量、近期宏观事件摘要以及克利夫兰联储发布的日常CPI实时预测。该流水线在2023年4月至2026年3月期间，每个月末产生七个美国权益风格因子的排名，中位数月度Spearman秩IC为+0.154。三个不重叠的12个月子窗口均显示正均值，但均值IC统计上不显著（bootstrap 95%置信区间包含零）。在相同决策时间约束下的非LLM基线（如kNN宏观模拟模型）恢复了可比的中位数IC，表明实时通胀信息和宏观相似性检索解释了大部分中位数信号。LLM流水线保留了更高的均值IC和更强的多空配置合理性检验，表明任何边际利益集中于驱动多空组合形成的极端排名。附录中包含36条评论规则和月度案例研究的描述性审计。
- **要点**：
  - LLM预测器内置信息泄漏控制，仅使用决策时可观测的实时数据。
  - 中位数月度IC +0.154，但统计上不显著，非LLM模型表现类似。
  - LLM的边际优势体现在极端排名中，可能改善多空组合构建。
- **回测线索**：Median monthly Spearman IC +0.154, bootstrap CI includes zero; subwindow means all positive.
- **风险**：Information leakage controlled but statistical significance low; marginal benefit may be limited to extreme rankings.
- **策略价值**：为LLM在因子投资中的实际应用提供了泄漏感知评估框架，并揭示了实时宏观信息的重要性。
- **筛选评分**：60
- **原文**：[链接](https://arxiv.org/abs/2606.22719)

---

### 自动化做市商的最优动态费用：针对再平衡损失问题的随机控制方法

- **收录时间**：2026-06-23 20:31
- **发布时间**：2026-06-23 12:00
- **作者**：Farbod Ghasemlu
- **来源**：arXiv q-fin.TR (Trading)
- **分类**：做市 · crypto · global
- **摘要**：本文研究恒定乘积自动化做市商（AMM）中流动性提供者的最优费用政策，允许费用连续调整，采用随机控制方法。作者在Milionis等人（2022）的损失-再平衡（LVR）框架及其扩展到非零费用的基础上，将LP财富相对于连续再平衡基准建模为受控过程，其中费用通过两种对立力量影响：每笔非知情交易增加收入但抑制非知情交易量，同时扩大无套利区间从而降低套利者提取价值的速度。由于费用仅影响相对财富的漂移项而不影响扩散项，LP的期望效用问题简化为遍历控制问题，其解是逐点波动率反馈。作者证明，增长最优费用与LP财富和常数相对风险厌恶无关，在波动率为常数时退化为静态常数，并随瞬时方差严格递增，因此最优费用是顺周期的。当波动率随机时，通过标量遍历Hamilton-Jacobi-Bellman方程和线性Poisson方程刻画最优费用，并用有限差分法求解。进一步证明，对数偏好下最优费用对价格跳跃不变，将其与场所间的竞争模型关联，并通过脉冲控制死区处理Gas成本。校准到流动大型股条件，最优动态费用在每条模拟路径上弱占优于所有静态及波动率相关启发式费用，与最佳静态费用相比，LP增长率改善虽小但一致为正，死区使Gas成本可忽略。
- **要点**：
  - 增长最优费用独立于LP财富和风险厌恶，仅取决于瞬时波动率。
  - 波动率恒定时代为静态，随机波动率时通过HJB方程求解最优动态费用。
  - 动态费用在模拟中一致优于静态和波动率挂钩的启发式策略。
- **回测线索**：Calibration to large-cap conditions shows dynamic fee weakly dominates static fees on simulated paths.
- **风险**：Gas costs, arbitrage extraction, model risk from stochastic volatility assumptions.
- **策略价值**：为AMM流动性提供者提供了理论最优的费用动态调整策略，可显著提升长期增长率。
- **筛选评分**：60
- **原文**：[链接](https://arxiv.org/abs/2606.21769)

---

### 市场解剖：因子模型的身体-尾部检验

- **收录时间**：2026-06-23 20:31
- **发布时间**：2026-06-23 12:00
- **作者**：Useong Shin
- **来源**：arXiv Quantitative Finance
- **分类**：因子 · stock · us
- **频率**：daily
- **摘要**：该论文检验了因子模型是否同时能定价市场整体的内部组成部分。作者构建了CRSP可投资市场组合，并按其规模分为身体（大盘股）和尾部（小盘股）两部分。所有模型均能通过市场整体检验，但q5模型在身体部分产生负alpha，在尾部产生正alpha，两者相互抵消。随机分割样本则消除了这一拒绝现象。研究表明，市场看似被定价可能是因为内部定价误差的抵消。该发现质疑了因子模型定价表面有效性的稳健性。
- **要点**：
  - q5因子模型通过市场整体检验，但在身体和尾部产生相反的alpha
  - 随机分割样本后，系统性的alpha消失
  - 因子模型可能因内部误差抵消而表面定价有效
- **风险**：Factor models may appear to price the market due to internal errors cancelling out; body-tail decomposition reveals model misspecification; results question reliability of factor-based pricing tests.
- **策略价值**：揭示了因子模型看似定价有效但内部存在抵消性错误的风险。
- **筛选评分**：65
- **原文**：[链接](https://arxiv.org/abs/2606.23596)

---

### 通过动态费用缓解集中流动性AMM中的逆向选择：基于代理模型的仿真研究

- **收录时间**：2026-06-23 20:31
- **发布时间**：2026-06-23 12:00
- **作者**：Daniele Maria Di Nosse, Fabrizio Lillo
- **来源**：arXiv q-fin.TR (Trading)
- **分类**：做市 · crypto · global
- **频率**：intraday
- **摘要**：该论文构建了Uniswap v3流动性池的精细代理模型，包含Heston随机波动率、区块传播、Mempool延迟、套利者、MEV搜索者等异构主体。设计了基于波动率和订单流毒性的动态费用方案，以补偿流动性提供者（LP）的逆向选择成本（即损失相对于再平衡策略LVR）。仿真结果表明，动态费用主要通过在价格陈旧风险较高时增加费用收入来提高LP的套期保值利润。当前结果支持动态费用对LVR的补偿作用，而非直接降低LVR。该研究为DeFi做市提供了量化风险管理工具。
- **要点**：
  - 动态费用基于波动率和订单流毒性调整，补偿LP逆向选择损失
  - 仿真表明动态费用增加费用收入，但未显著降低LVR自身
  - 模型重现了真实区块链微观结构，包括Mempool延迟和MEV
- **回测线索**：Agent-based simulation with realistic blockchain microstructure (block propagation, mempool latency).
- **风险**：Model may not capture all real-world blockchain behaviors; dynamic fee complexity could increase implementation risks; results depend on parameter choices.
- **策略价值**：为DeFi流动性提供者提供了量化管理逆向选择风险的新方法。
- **筛选评分**：65
- **原文**：[链接](https://arxiv.org/abs/2606.23070)

---

### 如何在11年回测中权衡夏普比率和年化收益率？

- **收录时间**：2026-06-23 20:31
- **发布时间**：2026-06-23 20:09
- **作者**：ItsmeK1
- **来源**：Reddit r/algotrading
- **分类**：综合/其他 · multi · us
- **频率**：daily
- **摘要**：该帖比较了四种策略的11年回测结果。策略A年化收益11.5%，夏普比率2.37，最大回撤10%。策略B年化12.3%，夏普1.20，回撤11%。策略C年化13.3%，夏普0.70，回撤24%。策略D年化15.4%，夏普0.82，回撤22%。作者倾向于策略A，认为其高夏普比率意味着更稳健的盈利能力和杠杆潜力。也有观点认为，若投资者能承受更大回撤，应选择更高年化收益的策略。讨论强调了夏普比率、年化收益和回撤之间的权衡。实际资产配置需考虑心理承受能力和资金规模。该分析提醒回测结果需要经过稳健性检验。
- **要点**：
  - 策略A夏普2.37，年化11.5%，回撤10%，风险调整后最优
  - 策略D年化最高15.4%，但夏普0.82，回撤22%
  - 高夏普可能表明策略有真实alpha，但需警惕过拟合
- **回测线索**：Eleven-year backtest including transaction costs; comparison based on CAGR, Sharpe, and drawdown.
- **风险**：Potential overfitting; survivorship bias; transaction costs may be underestimated; high Sharpe may not persist out-of-sample.
- **策略价值**：帮助交易者在实际投资决策中平衡风险调整收益与绝对收益。
- **筛选评分**：70
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1udfdlq/how_would_you_trade_off_sharpe_vs_cagr_for_an/)

---

### runchengxie/intraday-trader：日内量化交易项目

- **收录时间**：2026-06-23 20:31
- **发布时间**：2026-06-22 17:03
- **作者**：runchengxie
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · stock · us
- **频率**：intraday
- **摘要**：这是一个日内量化交易项目，涵盖策略开发、历史回测、Alpaca纸交易集成，以及市场数据、交易记录和绩效数据的本地与数据库存储。项目使用Python编写，当前获得0星。它提供了一个完整的日内交易框架，适合在美股市场进行高频或日內策略研究。
- **要点**：
  - 支持Alpaca纸交易，可进行模拟实盘交易。
  - 包含完整的本地和数据库存储方案，便于数据管理。
  - 专注于日内交易，适合短周期策略开发和测试。
- **回测线索**：Includes historical backtesting capability.
- **风险**：日内交易风险高，依赖Alpaca API，可能出现滑点和流动性问题。
- **策略价值**：为日内交易策略的快速开发和测试提供了现成的框架，降低了入门门槛。
- **筛选评分**：80
- **原文**：[链接](https://github.com/runchengxie/intraday-trader)

---

### ashishcj/nifty_100_momentum_features：基于Nifty 100指数的动量因子量化交易框架

- **收录时间**：2026-06-23 20:31
- **发布时间**：2026-06-22 18:22
- **作者**：ashishcj
- **来源**：GitHub Quant Repos
- **分类**：趋势跟踪 · stock · global
- **频率**：daily
- **摘要**：该项目是一个基于印度Nifty 100成分股的系统性量化交易框架。使用ICICI Breeze API获取数据，支持历史数据下载、每日数据更新、策略回测和实时信号扫描。代码使用Python编写，当前获得0星关注。框架专注于动量因子，适用于指数成分股的趋势跟踪策略。
- **要点**：
  - 针对Nifty 100指数成分股，提供完整的回测和实盘交易流程。
  - 依赖ICICI Breeze API获取市场数据，适合印度市场投资者。
  - 采用动量因子策略，属于趋势跟踪类别。
- **回测线索**：Framework supports backtesting strategies on historical data.
- **风险**：India-specific market risks, API dependency, momentum strategy may suffer from sudden reversals.
- **策略价值**：为印度市场的量化投资者提供了一个现成的动量策略框架，可直接用于Nifty 100成分股的回测和实盘。
- **筛选评分**：80
- **原文**：[链接](https://github.com/ashishcj/nifty_100_momentum_features)

---

### 我总结了五种可分散投资组合的另类投资策略

- **收录时间**：2026-06-23 20:31
- **发布时间**：2026-06-23 17:33
- **作者**：Jera_Value
- **来源**：Reddit r/algotrading
- **分类**：综合/其他 · multi · global
- **摘要**：作者延续了之前关于分散投资的讨论，提出了五种另类策略：趋势跟踪、套利（carry）、并购套利、巨灾债券和宏观相对价值。这些策略的收益来源与传统选股不同，能提供真正的分散化。趋势跟踪在趋势持续时获利，套利策略持有无人愿承担的风险，并购套利赌交易完成，巨灾债券承担保险灾难风险，宏观相对价值则押注资产关系的正常化。每种策略都有其独特的风险溢价。文章强调分散化不是拥有更多股票，而是拥有不同的风险敞口。这些策略虽然实施难度大、成本高或带有杠杆，但值得研究。作者提供了详细文章链接，并邀请社区讨论其他可能遗漏的好策略。
- **要点**：
  - 五种策略分别对应不同的风险因子：趋势、流动性、事件、灾难和相对价值。
  - 每种策略都有其独特的收益驱动因素和风险特征。
  - 这些策略通常与传统股票和债券组合相关性低，有助于分散风险。
- **风险**：Some strategies are hard to access, expensive, leveraged, or carry specific risks like deal completion risk or catastrophe risk.
- **策略价值**：了解这些另类策略可以帮助投资者构建更稳健、非传统的投资组合，降低整体波动。
- **筛选评分**：85
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1udcfu1/i_wrote_up_5_alternative_investment_strategies/)

---

### 自营公司算法执行管道搭建经验

- **收录时间**：2026-06-23 07:18
- **发布时间**：2026-06-20 11:07
- **作者**：Flat-Good716
- **来源**：Reddit r/algotrading
- **分类**：综合/其他 · futures · us
- **频率**：intraday
- **摘要**：一位用户分享了其自营交易公司的算法执行管道搭建过程。该管道使用Lucid Trading作为经纪商，底层为Tradovate。交易信号由TradingView的Pine Script生成。Pickmytrades作为webhook连接TradingView和Tradovate。用户之前使用Python连接Alpaca，现在转向期货和自营公司。用户担心从TradingView到Pickmytrades再到Tradovate的警报系统可靠性。NinjaTrader是TradingView的替代方案，但用户不熟悉。整个管道涉及多处费用，包括自营公司、TradingView Pro和PMT。用户希望获得建议和反馈。
- **要点**：
  - 使用Lucid Trading、Tradovate、TradingView和Pickmytrades构建执行管道。
  - 用户从股票转向期货和自营交易。
  - 警报系统可靠性是主要担忧。
- **风险**：管道依赖多个第三方服务，存在连接失败、警报延迟和额外费用风险。
- **策略价值**：为个人交易者搭建自动化期货交易管道提供了实战经验，并突出了多平台集成中的常见问题。
- **筛选评分**：65
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1ualjgw/prop_firm_pipeline_for_algo_execution/)

---

### NIFTY回测引擎

- **收录时间**：2026-06-23 07:18
- **发布时间**：2026-06-23 01:30
- **作者**：Avinash888
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · stock · global
- **摘要**：这是一个针对印度NIFTY指数的Python回测框架。它基于支点（Pivot Point）产生信号，并包含止损/止盈规则。移动平均线（SMA）作为趋势过滤器。还提供了可选的占星过滤器，用于实验性的信号优化。该框架覆盖了30年的NIFTY历史数据。项目代码用Python编写，目前星标为0。
- **要点**：
  - 基于支点信号的量化策略，附带SMA趋势过滤。
  - 包含可选的占星过滤器，属于实验性质。
  - 在30年NIFTY数据上进行回测。
- **回测线索**：在30年的NIFTY数据上进行了回测。
- **风险**：占星过滤器缺乏基本面依据，存在过拟合风险。
- **策略价值**：将传统技术分析与占星因素结合，展示了非常规信号源的可能性，但需警惕过拟合。
- **筛选评分**：85
- **原文**：[链接](https://github.com/Avinash888/Nifty-Backtesting-Engine)

---

### NEPSE强化学习与规则策略交易平台

- **收录时间**：2026-06-23 07:18
- **发布时间**：2026-06-23 01:22
- **作者**：krishna-ji
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · stock · global
- **摘要**：这是一个面向尼泊尔证券交易所（NEPSE）的量化交易研究平台。它包含了7种基于规则的交易策略。使用LightGBM模型进行信号过滤，该模型基于38个特征。还使用了PPO强化学习智能体来优化决策。代码库超过15000行，并包含99个测试。项目主题涵盖算法交易、回测、特征工程、强化学习等。该仓库主要使用Python编写，目前星标为0。
- **要点**：
  - 结合规则基、机器学习和强化学习三种方法。
  - 使用LightGBM对38个特征进行信号过滤。
  - 包含15k+行代码和99个测试。
- **回测线索**：包含99个测试的回测框架，但未报告具体绩效数字。
- **风险**：大量特征和RL可能导致过拟合；NEPSE流动性较低。
- **策略价值**：展示了如何融合多种量化方法于一个小众市场，为低流动性市场提供了可参考的多策略框架。
- **筛选评分**：90
- **原文**：[链接](https://github.com/krishna-ji/nepse-rl-agent-rbs-experiment)

---

### Cornelius-Mulyo/量化交易研究平台

- **收录时间**：2026-06-22 23:20
- **发布时间**：2026-06-22 14:38
- **作者**：Cornelius-Mulyo
- **来源**：GitHub Quant Repos
- **分类**：趋势跟踪 · stock · global
- **频率**：daily
- **摘要**：该项目是一个量化投资组合研究平台，使用Python和PostgreSQL实现。它支持动量策略回测、投资组合优化、风险分析以及有效前沿建模。平台旨在帮助研究不同投资组合配置下的风险收益特征。目前获得0个星标。
- **要点**：
  - 核心功能包括动量策略回测和有效前沿分析。
  - 使用Python和PostgreSQL作为技术栈。
  - 提供投资组合优化和风险分析工具。
- **回测线索**：Focuses on momentum strategy backtesting with portfolio optimization and Efficient Frontier analysis.
- **风险**：Momentum strategies can experience sharp drawdowns during trend reversals; overfitting risk in optimization.
- **策略价值**：该平台为量化投资者提供了一个完整的投资组合研究流程，从策略回测到优化，便于在实践中配置资产。
- **筛选评分**：85
- **原文**：[链接](https://github.com/Cornelius-Mulyo/quant-trading-research-platform)

---

### jagdeepvirdi/ResidualEdge 多策略量化交易系统

- **收录时间**：2026-06-22 23:20
- **发布时间**：2026-06-22 13:14
- **作者**：jagdeepvirdi
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · stock · global
- **频率**：intraday
- **摘要**：该项目是一个针对印度NSE/BSE股票市场的多策略量化研究与交易系统。它包括市场中性纸面策略、实盘资金复利器、日内研究回测器以及AI基础设施投资追踪器，并配有实时监控仪表盘。系统使用Python编写，目前获得0个星标。
- **要点**：
  - 涵盖市场中性、资金复利、日内回测和AI投资追踪等多种策略。
  - 专为印度股票市场设计，使用Python实现。
  - 提供实时监控仪表盘，便于交易跟踪。
- **回测线索**：Includes intraday research backtester and paper strategy backtesting.
- **风险**：Market-neutral strategies may suffer from basis risk and model overfitting; Indian market liquidity can be variable.
- **策略价值**：该系统为印度市场提供了一个完整的量化交易基础设施，从回测到实盘监控，适合希望进入新兴市场的量化交易者。
- **筛选评分**：85
- **原文**：[链接](https://github.com/jagdeepvirdi/ResidualEdge)

---

### 我会为任何发送交易日志的人生成交易分析报告。让我们开启一个线程来比较策略结果

- **收录时间**：2026-06-22 07:05
- **发布时间**：2026-06-22 04:04
- **作者**：JayCreator7
- **来源**：Reddit r/algotrading
- **分类**：综合/其他 · multi · global
- **频率**：daily
- **摘要**：该帖子由Reddit用户/u/JayCreator7发布。作者提供一项服务：接收交易日志CSV文件并生成交易分析报告。日志格式必须包含日期和回报。报告内容包含多个图表和分析指标。目的是鼓励交易者分享日志并比较策略结果。这有助于社区内的策略评估和优化。用户需自行提供交易数据。此服务是免费的社区贡献。报告基于用户数据生成，具有个性化特点。通过比较不同策略的结果，可以促进学习和改进。这是一个协作性的分析工具。注意：结果依赖数据质量和完整性。
- **要点**：
  - 用户需提供包含日期和回报的CSV格式交易日志。
  - 生成包含多个图表的交易分析报告。
  - 目的是促进社区内策略比较和讨论。
  - 作者是/u/JayCreator7。
- **风险**：Report quality depends on user-provided data; potential for overfitting or biased analysis.
- **策略价值**：该服务使交易者能够免费获得专业分析，促进策略透明度和社区协作学习。
- **筛选评分**：55
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1ubzrie/ill_generate_a_trade_analysis_report_for_anyone/)

---

### Clappedbytxger/回测

- **收录时间**：2026-06-22 07:05
- **发布时间**：2026-06-21 03:44
- **作者**：Clappedbytxger
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · multi · global
- **摘要**：这个仓库提供了量化交易研究，包括一个偏差感知的回测框架和一个策略目录。它用Python编写，目前没有星标。框架旨在减少回测中的常见偏差。策略目录包含多种交易策略。用户可以使用该框架进行更可靠的回测。项目还关注策略评估和优化。这是一个开源资源，适合量化研究者。
- **要点**：
  - 偏差感知的回测框架，减少过拟合风险
  - 包含策略目录，提供多种交易策略
  - 使用Python实现，适合量化研究
- **回测线索**：Bias-aware backtesting framework to reduce overfitting.
- **风险**：Backtest bias may still exist despite bias-aware approach.
- **策略价值**：帮助交易者构建更稳健的回测环境，提升策略评估的准确性。
- **筛选评分**：75
- **原文**：[链接](https://github.com/Clappedbytxger/Backtests)

---

### SkyPiggy8/TnT股票分析与EQS

- **收录时间**：2026-06-22 07:05
- **发布时间**：2026-06-21 23:28
- **作者**：SkyPiggy8
- **来源**：GitHub Quant Repos
- **分类**：因子 · stock · cn
- **频率**：daily
- **摘要**：这个仓库提供了针对中国A股市场的量化交易策略和分析。它使用Python编写，集成了EQS系统。目前该项目获得了2个星标。它专注于股票市场的量化分析。工具旨在帮助投资者进行数据驱动的决策。代码包括策略回测和评估。用户可以根据自己的需求进行定制。这是一个开源项目，欢迎贡献。
- **要点**：
  - 针对中国A股市场的量化交易策略与分析
  - 使用Python语言实现并集成EQS
  - 提供股票市场的数据驱动分析工具
- **策略价值**：为中国A股投资者提供实用的量化分析工具，提升投资决策效率。
- **筛选评分**：80
- **原文**：[链接](https://github.com/SkyPiggy8/TnT_stock_analysis_with_EQS)

---

### 将回测与交易日志整合为单一工作流，有人这样做吗？

- **收录时间**：2026-06-21 20:10
- **发布时间**：2026-06-20 05:58
- **作者**：MessPrestigious8035
- **来源**：Reddit r/algotrading
- **分类**：综合/其他 · multi · global
- **摘要**：讨论了一种介于回测器和交易日志之间的工具类别。该工具可以导入实时执行数据，允许用户根据交易手册标记设置，逐笔回放交易，并在同一交易品种上对10年以上的历史数据回测相同的手册。对于系统化交易者而言，样本内回测表现与实时执行之间的差距通常不是策略问题，而是执行层问题。包括滑点、错失成交、过早退出以及在第二个入场信号上的犹豫。单独的回测器无法揭示这些，单独的日志也无法判断底层设置是否具有统计真实性。整合工作流程包括：在历史数据上回测手册获得基准期望，实时交易并针对同一手册记录每次执行，比较实时分布与回测分布。测试显示，纸面交易与实时表现之间60-70%的差距来自执行漂移（过早退出和跳过入场），而非策略失效。难点在于在比较双方拥有相同的手册结构。
- **要点**：
  - 回测与交易日志整合可发现执行漂移，这是纸面交易与实盘表现差距的主要原因。
  - 执行漂移（过早退出、跳过入场）占差距的60-70%，并非策略失效。
  - 需要统一的手册结构用于回测和实时交易，以便准确比较。
- **回测线索**：Backtest playbook on historical data to get baseline expectancy; compare live distribution to backtest distribution to measure execution drift.
- **风险**：Execution drift (early exits, skipped entries) accounts for 60-70% of paper-to-live performance gap; slippage, missed fills, hesitation on second entry signal.
- **策略价值**：该工作流帮助系统化交易者识别并量化执行层的问题，从而缩小回测与实盘之间的绩效差距。
- **筛选评分**：50
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1uaf09r/backtesting_journaling_as_a_single_workflow_does/)

---

### puravi-predicts/quantedge

- **收录时间**：2026-06-21 20:10
- **发布时间**：2026-06-20 17:58
- **作者**：puravi-predicts
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · multi · global
- **摘要**：这是一个模块化的量化交易框架，包含回测管道，使用MLflow跟踪实验，并配有交互式Streamlit仪表盘用于策略评估。该框架支持多种数据源和策略类型，旨在简化量化研究和开发流程。项目语言为Python，尚未有公开的星标。仓库提供了基础的交易策略仿真功能，适合学习和初步测试。整体设计灵活，可扩展性高，但需要用户自行配置策略和数据管道。
- **要点**：
  - 模块化的量化交易框架，集成回测和MLflow跟踪。
  - 提供Streamlit交互式仪表盘进行策略评估。
  - 支持多种数据源和策略类型，灵活可扩展。
- **回测线索**：Includes a backtesting pipeline integrated with MLflow for tracking experiments.
- **策略价值**：该框架为量化开发者提供了一套标准化、可复用的工具链，有助于快速验证交易想法并管理实验记录。
- **筛选评分**：60
- **原文**：[链接](https://github.com/puravi-predicts/quantedge)

---

### 我7个新闻情绪策略全都跑输XBI基准。以下是我方法，请问哪里出了问题？

- **收录时间**：2026-06-21 20:10
- **发布时间**：2026-06-21 17:36
- **作者**：Metathetical_Chemist
- **来源**：Reddit r/algotrading
- **分类**：因子 · stock · us
- **频率**：daily
- **摘要**：该策略基于LLM（DeepSeek/Gemini）对约350只生物科技股的新闻生成情绪评分（0-10分，分财务、技术、监管三个子项）。建立了7个仅做多的纸交易组合，包括综合、各子项、市场分歧、美国/欧洲区域筛选等。入场条件：情绪分>=7，且当日涨幅不超过1.5%。仓位按分数从$1k到$4k不等。出场条件：+20%止盈、-7%硬止损、-8%移动止损、14天时间止损（若不盈利超1%）、或分数降至6以下。运行约一个月后，所有策略收益在+0.9%到-3.3%之间，而XBI上涨约6%。表现最差的策略是综合和市场分歧。作者认为可能的问题包括：在板块已大涨后追多情绪、情绪新闻可能已被定价、以及止损设计导致反复止损。作者疑问：LLM新闻情绪是否作为信号已过时？是否应使用变化率而非情绪水平？是否更适合做空信号？
- **要点**：
  - 基于LLM情绪评分的7个做多策略在生物科技板块均跑输XBI基准。
  - 一个月纸交易中，所有策略收益为平盘至负，而XBI涨约6%。
  - 作者怀疑买入时机滞后，止损设计在波动板块中导致反复亏损。
- **回测线索**：Paper-trading experiment for one month; all strategies underperform XBI by approximately 6-9%.
- **风险**：Long-only bias in a bullish sector; sentiment may be lagging; stop-losses cause whipsaw; signal may be priced in; public news sentiment may not be alpha.
- **策略价值**：该实验揭示了基于公开新闻情绪做多策略在强势板块中的常见陷阱，提醒量化交易者注意信号滞后与策略设计风险。
- **筛选评分**：70
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1ublsph/my_7_newssentiment_strategies_are_all_losing_to_a/)

---

### NiftyOnTheMove：基于Andreas Clenow动量策略的回测框架

- **收录时间**：2026-06-21 20:10
- **发布时间**：2026-06-21 11:49
- **作者**：Suchismit4
- **来源**：GitHub Quant Repos
- **分类**：趋势跟踪 · stock · global
- **频率**：daily
- **摘要**：该仓库提供了一个基于Andreas Clenow动量策略的稳健回测框架。它专门用于模拟、分析和优化印度Nifty500股票的交易。框架采用Python实现，强调现实执行和全面报告。用户可以通过该框架对动量策略进行历史回测和参数优化。代码开源于GitHub，当前获得2颗星。该框架适合研究印度股票市场的动量效应。
- **要点**：
  - 基于Andreas Clenow的动量策略构建回测框架
  - 专注于印度Nifty500股票的交易模拟与优化
  - 支持现实执行和全面报告，使用Python语言
- **回测线索**：框架支持现实执行的回测，包含全面报告和优化功能。
- **风险**：动量策略可能在市场反转或震荡时表现不佳，需注意趋势衰竭风险。
- **策略价值**：该框架为印度股票市场的动量策略提供了一套完整的回测和优化工具，有助于交易者量化评估策略表现。
- **筛选评分**：75
- **原文**：[链接](https://github.com/Suchismit4/NiftyOnTheMove)

---

### 我该继续使用模拟资金还是开始实盘交易？

- **收录时间**：2026-06-21 07:01
- **发布时间**：2026-06-20 16:38
- **作者**：ContrversialIntrovrt
- **来源**：Reddit r/algotrading
- **分类**：综合/其他 · stock · us
- **频率**：daily
- **摘要**：作者在Reddit上分享了自己构建的股票交易策略的测试结果。该策略自4月开始回测，5月22日优化后持续跟踪。作者询问合适的模拟测试周期，担心策略可能在实盘中退化。他提到已检查前瞻偏差和幸存者偏差，想知道还需注意哪些历史模拟偏差。作者怀疑自己的策略是否只是运气好，担心实盘亏损。其他用户建议延长测试期至90-180天，并强调实盘前需充分验证。
- **要点**：
  - 策略从4月开始回测，5月22日优化后跟踪至今；
  - 作者担心策略退化、过拟合和运气成分；
  - 询问合适的模拟测试期（90-180天）及其他历史回测偏差。
- **回测线索**：作者从4月开始回测，5月22日优化后持续跟踪，但担心样本外时间不足（90-180天建议）。
- **风险**：策略退化风险、过拟合、幸存者偏差、前瞻偏差、市场风格切换、运气成分。
- **策略价值**：从模拟交易到实盘交易是量化策略开发的关键一步，需要谨慎评估策略的稳健性和风险。
- **筛选评分**：60
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1uareye/do_i_still_use_paper_money_or_start_live_trading/)

---

### 精准入场模型

- **收录时间**：2026-06-21 07:01
- **发布时间**：2026-06-21 05:25
- **作者**：poplindoing
- **来源**：Reddit r/algotrading
- **分类**：综合/其他 · multi · global
- **频率**：intraday
- **摘要**：这是Reddit上关于精准入场模型的讨论。用户已有的策略基于多信号组合入场，并使用机器学习等退出模型。他们提出是否可以将入场细分为一个独立的模型，通过订单簿、订单流、限价单和分批订单来优化入场时机。用户认为入场优化是一个重要组成部分，能提高胜率。当前退出模型回测良好，但入场过于简单，担心过度过滤导致交易信号减少。讨论焦点在于如何在不损失信号数量的前提下提升入场质量。
- **要点**：
  - 讨论将入场优化作为独立模块
  - 使用订单簿和订单流数据
  - 担心优化入场会减少交易机会
- **回测线索**：用户的退出模型在回测中表现良好，但入场模型较简单，需进一步优化。
- **风险**：精细入场可能增加交易次数和滑点，需平衡频率与胜率；订单簿数据噪声较大。
- **策略价值**：入场优化可显著提升策略绩效，尤其对高频或日内交易者重要。
- **筛选评分**：60
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1ub7zuc/precise_entry_model/)

---

### 量化交易管道

- **收录时间**：2026-06-21 07:01
- **发布时间**：2026-06-20 07:01
- **作者**：Ndima-Mdleleni
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · multi · global
- **频率**：intraday
- **摘要**：这是一个用Python构建的完整量化交易管道。它能获取实时市场数据，计算技术指标，生成买卖信号，并在历史数据上回测策略。最终输出包含夏普比率、最大回撤、胜率和利润因子的性能报告。项目目前星数较少，但功能完整，适合学习和实验。管道设计模块化，便于扩展自定义策略。作者是Ndima-Mdleleni。虽然未指定资产类别，但可适用于股票、加密货币等。管道默认可能使用日线或分钟数据。
- **要点**：
  - 完整的交易流程：数据获取到回测报告
  - 回测指标包括夏普比率和最大回撤
- **回测线索**：回测报告包含夏普比率、最大回撤、胜率和利润因子。
- **风险**：依赖数据质量，可能出现过拟合；实时执行需考虑延迟和滑点。
- **策略价值**：提供了一个开箱即用的量化交易框架，降低了从策略到回测的门槛。
- **筛选评分**：80
- **原文**：[链接](https://github.com/Ndima-Mdleleni/trading-ai)

---

### 量化交易策略集合

- **收录时间**：2026-06-21 07:01
- **发布时间**：2026-06-21 02:07
- **作者**：je-suis-tm
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · multi · global
- **摘要**：这是一个包含多种Python量化交易策略的开源仓库。策略包括VIX计算器、模式识别、商品交易顾问、蒙特卡洛模拟、期权跨式组合、射击之星、伦敦突破、Heikin-Ashi蜡烛图、配对交易、RSI、布林带、抛物线SAR、双推力、Awesome振荡器和MACD。仓库以Python编写，拥有超10000颗星，是学习量化交易的优秀资源。每个策略都有独立的实现，可直接使用或修改。仓库还包含技术分析工具和风险管理组件。作者是je-suis-tm，持续更新策略库。适合从股票到加密货币的多资产类别交易。
- **要点**：
  - 包含15种以上经典量化交易策略
  - Python实现，适合学习和实盘
  - 覆盖趋势、均值回归、期权等多种类型
- **风险**：使用多种策略需注意分散风险和参数优化，避免过度拟合。
- **策略价值**：此仓库提供了一套全面的量化策略模板，可加速个人策略开发与测试。
- **筛选评分**：80
- **原文**：[链接](https://github.com/je-suis-tm/quant-trading)

---

### DCA策略问题

- **收录时间**：2026-06-20 19:54
- **发布时间**：2026-06-20 07:41
- **作者**：Aggressive_Ad1599
- **来源**：Reddit r/algotrading
- **分类**：综合/其他 · stock · us
- **频率**：intraday
- **摘要**：一位交易者发现了一个具有60%胜率和1:1风险回报比的交易优势，并在特定时间执行交易。他引入DCA方法，将风险分成三次入场，使盈利交易的利润翻倍。但一些交易直接达到止盈，未触发DCA，只能获得DCA盈利的三分之一。亏损交易则始终承担全部风险，导致这类直接盈利交易的风险回报比为负。该交易者询问如何弥补这些低风险盈利交易，或这是否是DCA策略的固有缺陷。帖子来自Reddit的algotrading板块，由用户Aggressive_Ad1599提交。
- **要点**：
  - 60%胜率和1:1风险回报比的交易优势基础。
  - DCA将风险分成三次入场，使整体盈利交易利润翻倍。
  - 直接达到止盈的盈利交易仅获得DCA盈利的三分之一，且亏损交易承担全部风险。
  - 此类直接盈利交易的风险回报比为负，需要应对。
- **风险**：DCA策略中，直接达到止盈的交易仅获得三分之一利润，而亏损交易承担全部风险，导致部分交易的风险回报比为负。
- **策略价值**：该问题探讨了DCA策略在提高胜率的同时可能带来的风险回报不均衡，对优化交易管理具有实际意义。
- **筛选评分**：60
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1uahbuk/dca_strategy_question/)

---

### 看起来是赢家，但真的是赢家吗？

- **收录时间**：2026-06-20 19:54
- **发布时间**：2026-06-20 18:04
- **作者**：EaZyRecipeZ
- **来源**：Reddit r/algotrading
- **分类**：均值回归 · stock · us
- **频率**：daily
- **摘要**：该策略是一个纯Python脚本，每天开盘第一秒进行交易，通过平衡ETF组合来操作。没有使用人工智能或机器学习方法。回测中假设无滑点，但作者承认缺乏开盘后30分钟的数据来优化进场时间。回测指标显示夏普比率在2.35到3.36之间，最大回撤从2.39%到24.34%不等，净收益从29.52%到167.82%。不同的配置参数产生了显著不同的结果，暗示可能存在过度拟合。作者在征求社区意见，并考虑将代码开源。该策略强调了简单再平衡策略在回测中的潜力，但需要谨慎评估实盘中的滑点和交易成本。
- **要点**：
  - 每日开盘一次性交易，通过平衡ETF组合实现策略。
  - 回测假设无滑点，夏普比率较高（2.35-3.36）。
  - 不同配置参数下表现差异大，存在过度拟合风险。
  - 作者考虑开源代码并征求改进意见。
- **回测线索**：Backtest shows high Sharpe ratios (2.35-3.36) and net profit (30-168%), but no slippage included. Multiple configurations tested, raising overfitting risk.
- **风险**：No slippage or transaction costs assumed; backtest likely overfitted due to many parameter configurations; performance may not translate to live trading.
- **策略价值**：此案例说明，即使是简单的ETF平衡策略在回测中也可能看似优秀，但必须注意滑点和过度拟合对实盘表现的潜在影响。
- **筛选评分**：70
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1uass5b/looks_like_a_winner_but_is_it_a_winner/)

---

### MarcosACH/quant-strategies

- **收录时间**：2026-06-20 19:54
- **发布时间**：2026-06-19 21:29
- **作者**：MarcosACH
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · multi · global
- **摘要**：A comprehensive framework for developing and backtesting quantitative trading strategies.
Topics: algorithmic-trading, backtesting, backtesting-engine, backtesting-trading-strategies, optuna, optuna-optimization, quantitative-finance, vectorbt
Language: Python
Stars: 1
- **筛选评分**：75
- **原文**：[链接](https://github.com/MarcosACH/quant-strategies)

---

### Project_Aegis

- **收录时间**：2026-06-20 19:54
- **发布时间**：2026-06-20 02:08
- **作者**：Yuyutsu01
- **来源**：GitHub Quant Repos
- **分类**：机器学习 · multi · global
- **摘要**：Project AEGIS（高级执行与梯度提升智能策略）是一个研究级的量化交易框架。它实现了混合元策略架构。标准的强化学习模型在非平稳金融环境中常因噪声信号比过高而表现不佳。AEGIS通过解耦策略与执行来解决这一问题。该框架使用Python编写。旨在提高强化学习在交易中的稳健性。仓库当前获得2颗星。项目仍处于早期研究阶段。它探索了强化学习在量化领域的应用。
- **要点**：
  - 实现混合元策略架构以应对非平稳市场。
  - 解耦策略与执行，降低噪声干扰。
  - 基于强化学习的研究级量化框架。
  - 目前获得2颗星，作者为Yuyutsu01。
- **风险**：强化学习模型在非平稳金融环境中容易过拟合，高噪声信号比可能导致策略失效。
- **策略价值**：该框架为强化学习在量化交易中的实际应用提供了新的解决思路，有助于提高策略在复杂市场环境下的适应性。
- **筛选评分**：70
- **原文**：[链接](https://github.com/Yuyutsu01/Project_Aegis)

---

### 如何发现异常值：一种集成异常检测框架

- **收录时间**：2026-06-20 06:49
- **发布时间**：2026-06-19 12:00
- **作者**：Daniil Peysakhovich, Rafał Sieradzki
- **来源**：arXiv Quantitative Finance
- **分类**：机器学习 · multi · global
- **频率**：daily
- **摘要**：该论文提出了一种集成异常检测框架（EQAF），用于监控投资银行风险计算完整性。框架基于全球主要投资银行的专有信用衍生品数据，涵盖183笔交易、129个交易日。EQAF采用分层无监督架构，结合互补的异常检测方法，实时监控风险计算。通过受控异常注入测试，在八种可操作的真实场景中，集成模型的F1得分达到61-79%，显著优于单个最佳方法（6-66%）。AUC-ROC提升4-6个百分点，证明优势对阈值选择稳健。研究还发现，纯统计方法无法识别“停滞值”异常（即因数据馈送冻结导致的输出与先前观测相同的情况），因此必须加入领域特定的确定性规则。这些发现对巴塞尔III和交易账簿基本审查（FRTB）下的模型风险管理具有直接意义。
- **要点**：
  - 提出集成异常检测框架（EQAF）用于风险计算完整性监控。
  - 在信用衍生品数据上，F1得分达61-79%，优于单一方法。
  - 纯统计方法无法检测停滞值异常，需依赖领域规则。
- **回测线索**：Evaluated using a controlled anomaly-injection protocol with eight operationally realistic scenarios, achieving F1 scores 61-79% and AUC-ROC improvements of 4-6 percentage points over individual methods.
- **风险**：Statistical methods fail to detect stale-value anomalies; domain-specific rules are indispensable. Model risk and potential operational losses if anomalies go undetected.
- **策略价值**：该框架为投资银行提供了一种自动化、可审计的风险模型质量监控工具，有助于满足巴塞尔III和FRTB的监管要求。
- **筛选评分**：50
- **原文**：[链接](https://arxiv.org/abs/2606.20079)

---

### 自动化算法交易XAUUSD系统

- **收录时间**：2026-06-20 06:49
- **发布时间**：2026-06-18 23:43
- **作者**：Ahmed-Eldabea
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · forex · global
- **频率**：intraday
- **摘要**：这是一个基于Python和MetaTrader 5的生产就绪型自动化算法交易系统与量化回测引擎，专门针对XAUUSD（黄金兑美元）设计。该系统利用多时间框架技术策略，并严格执行自营交易公司级别的风险控制措施。系统架构包含多个文件，支持端到端的自动化执行。此外，系统集成了LLM遥测技术用于监控。该仓库旨在提供一个完整的交易框架，从策略研究到实盘执行。代码使用Python编写，目前有0个星标。
- **要点**：
  - 使用Python和MetaTrader 5构建的生产级自动化交易系统。
  - 针对XAUUSD（黄金兑美元）货币对设计。
  - 集成了多时间框架技术策略和严格的风险控制。
  - 包含回测引擎和LLM遥测功能。
- **回测线索**：The repository includes a backtesting engine, but specific performance results are not mentioned.
- **风险**：Prop-firm grade risk controls are implemented, but risks include overfitting and reliance on technical indicators.
- **策略价值**：该系统提供了一个可直接部署的量化交易框架，对于希望快速实现黄金外汇策略自动化的交易者具有实用价值。
- **筛选评分**：60
- **原文**：[链接](https://github.com/Ahmed-Eldabea/Automated-Algorithmic-Trading-XAUUSD)

---

### 多资产回测和蒙特卡洛结果强劲，但疑似过拟合

- **收录时间**：2026-06-20 06:49
- **发布时间**：2026-06-20 03:02
- **作者**：Puzzleheaded_Sun3104
- **来源**：Reddit r/algotrading
- **分类**：综合/其他 · multi · global
- **频率**：intraday
- **摘要**：一位量化交易者分享其策略在多种资产（黄金、白银、指数、外汇、加密货币）上使用相同参数的历史回测表现。策略基于1小时K线，涵盖约50,000根蜡烛，并考虑交易成本。结果显示所有市场盈利稳定，利润因子在2到5之间，胜率35-45%，最大回撤4-12%，年化夏普比率超过1。通过前进测试和蒙特卡洛模拟验证，表现具有韧性。然而，作者对跨市场的一致性感到困惑，怀疑存在过拟合。主要担忧是每市场仅有约100-130笔交易，统计显著性不足。作者寻求社区建议，识别潜在的过拟合形式或进行额外的压力测试。
- **要点**：
  - 同一参数在多个不相关市场（外汇、指数、加密货币）均获强劲回测表现。
  - 标准验证方法（前进测试、蒙特卡洛）未发现明显过拟合迹象。
  - 交易次数较少（每市场100-130笔）是主要统计疑虑。
- **回测线索**：作者报告在多市场使用相同参数获得强劲回测结果：利润因子2-5，胜率35-45%，最大回撤4-12%，夏普比率>1，前进测试和蒙特卡洛显示稳定。
- **风险**：潜在过拟合风险：交易次数有限（每市场100-130笔），跨市场的一致性过于完美，可能隐藏了未检测到的偏差。
- **策略价值**：该案例说明了跨市场一致性策略背后的过拟合风险，即使标准验证方法未发现明显问题。
- **筛选评分**：80
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1uaao3b/strong_multiasset_backtest_and_montecarlo_results/)

---

### tradingstrategy-ai/trading-strategy

- **收录时间**：2026-06-20 06:49
- **发布时间**：2026-06-19 21:49
- **作者**：tradingstrategy-ai
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · crypto · global
- **摘要**：这是一个开源的Python框架，专为去中心化交易所（DEX）的量化金融分析和交易算法设计。它支持以太坊、Arbitrum、Base、Polygon等多条区块链，并集成Uniswap、PancakeSwap等主流DEX。框架提供完整的交易流程，包括数据获取、策略开发、回测和实盘执行。项目在GitHub上获得369颗星，主要语言为Python。它被归类为算法交易、加密货币、量化交易等主题，适合构建交易机器人和执行交易策略。
- **要点**：
  - 支持多条区块链和主流去中心化交易所。
  - 提供从数据到实盘交易的完整框架。
  - Python语言，开源且活跃维护。
- **策略价值**：为去中心化交易所的量化交易提供了开源Python框架，降低了DEX策略开发的门槛。
- **筛选评分**：85
- **原文**：[链接](https://github.com/tradingstrategy-ai/trading-strategy)

---

### 哪个投资组合？因子模型表现对组合构建的依赖

- **收录时间**：2026-06-20 06:49
- **发布时间**：2026-06-19 12:00
- **作者**：Useong Shin
- **来源**：arXiv Quantitative Finance
- **分类**：因子 · stock · us
- **摘要**：该研究考察了因子模型表现如何依赖于测试资产组合的构建方式。作者从广泛的CRSP股票池中构建特征未排序的随机组合，并变化股票选择、初始权重、持有期和再平衡频率。结果显示，不同模型表现排名会因构建方式发生显著变化：买入持有策略下，五因子模型（FF5）和六因子模型（FF6）表现更优；而在日频常数权重下，三因子模型（FF3）最为稳定。尽管q5模型在因子跨度测试中达到最高夏普比率，但在随机组合上留下的定价误差较大且对构建方式敏感。这些差异源于每个模型定价错误向量在构建中获得的特定权重。结论是，测试资产组合的构建方式，特别是动态权重管理，是模型评估中的关键设计选择。
- **要点**：
  - 因子模型表现排名随组合构建方法变化，无普遍最优模型。
  - 买入持有策略偏好包含更多因子的模型如FF5/FF6，日频再平衡则偏好简洁的FF3。
  - q5因子模型在解释截面收益方面最强，但定价误差对组合构建敏感。
- **回测线索**：研究使用CRSP数据，比较不同投资组合构建方法（未排序随机组合、买入持有、日频常数权重）下的因子模型表现，发现排名变化显著。
- **风险**：定价错误的构建特定加权可能导致模型评估偏差。
- **策略价值**：该研究强调了在评估因子模型时，测试资产构建方法（包括动态权重管理）是一个关键设计选择，可能影响模型比较的结论。
- **筛选评分**：90
- **原文**：[链接](https://arxiv.org/abs/2606.19550)

---

### 机器学习预测未来价格分布

- **收录时间**：2026-06-19 21:33
- **发布时间**：2026-06-19 20:46
- **作者**：SquallLionheart
- **来源**：Reddit r/algotrading
- **分类**：机器学习 · stock · us
- **频率**：daily
- **摘要**：作者对从数据中提取可操作情报有浓厚兴趣，但在此领域仍是新手。文章展示了一个K-NN相似性搜索的输出，通过对历史收益进行重采样，模拟了1000条可能的未来价格路径，并计算其中位数。该结果不仅提供了可视化，还生成了量化的元数据特征。这些特征包括：牛市概率0.09、熊市概率0.91、期望收益-0.0254、中位数收益-0.0267、尾部风险-0.0483、波动率预测0.0034、回撤概率0.45和突破概率0.215。作者希望通过这些特征获得可量化的交易信号。他呼吁有更多机器学习经验的人分享如何使用ML数据构建算法交易系统。该帖子展示了从历史数据中学习价格分布的新颖思路。这种方法旨在为交易决策提供概率性依据。
- **要点**：
  - 使用K-NN相似性搜索模拟未来价格路径。
  - 生成了包括概率、期望收益、波动率等量化特征。
  - 当前市场预测偏向熊市，熊市概率91%，期望收益为负。
- **风险**：模型存在过拟合风险，尾部风险预测可能不准确。
- **策略价值**：该方法提供了一种直观的概率框架来评估未来价格走势，有助于量化交易者制定更稳健的仓位管理和风险控制策略。
- **筛选评分**：75
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1ua12ok/ml_for_future_price_distribution/)

---

### 金融市场中的趋势、波动率、相关性和临界现象

- **收录时间**：2026-06-19 21:33
- **发布时间**：2026-06-19 12:00
- **作者**：Sara A. Safari, Christoph Schmidhuber
- **来源**：arXiv Quantitative Finance
- **分类**：趋势跟踪 · multi · global
- **频率**：daily
- **摘要**：该论文基于当前市场趋势预测未来的波动率和相关性。实证发现，在强上涨或下跌趋势中，波动率和相关性会逐日增加，这一效应在下跌趋势中尤为明显。这种关系可以通过当前趋势强度的二次多项式精确量化，从而改进了常见的波动率和相关性均值回复模型。研究结果通过考虑市场趋势提高了市场风险预测的准确性，并支持了最近提出的将金融市场建模为接近临界点的晶格气体的方案。论文为风险管理和市场微观结构提供了新的视角。
- **要点**：
  - 波动率和相关性在强趋势中系统性地上升，下跌趋势中更显著。
  - 用趋势强度的二次多项式可以精确建模该效应，优于传统的均值回复模型。
  - 结果有助于更准确地预测市场风险，并支持金融市场临界点理论。
- **风险**：Model assumes trend persistence; may fail during abrupt reversals or regime changes. Quadratic fit may overextrapolate in extreme trends.
- **策略价值**：该研究将趋势信息直接纳入波动率和相关性预测，为风险管理和衍生产品定价提供了更可靠的量化基础。
- **筛选评分**：85
- **原文**：[链接](https://arxiv.org/abs/2606.20145)

---

### 机器学习增强的Alpha模型

- **收录时间**：2026-06-19 21:33
- **发布时间**：2026-06-19 18:35
- **作者**：Aiden0334
- **来源**：GitHub Quant Repos
- **分类**：机器学习 · futures · us
- **频率**：daily
- **摘要**：该项目开发了一个基于体制的美国股指期货量化交易策略。使用XGBoost模型增强交易信号选择。四年样本外回测结果显示，投资组合夏普比率从0.92提高到1.37。该模型采用滚动窗口验证以避免过拟合。策略根据市场体制调整持仓。代码用Python编写，但未公开具体因子和模型细节。这是一个典型的机器学习在量化交易中的应用案例。
- **要点**：
  - 使用XGBoost模型作为滤波器，提升已有策略表现。
  - 四年样本外回测夏普比率从0.92提升至1.37。
  - 采用滚动窗口验证，增强模型稳健性。
- **回测线索**：四年样本外回测显示，使用机器学习过滤器后，投资组合夏普比率从0.92提升至1.37，采用滚动窗口验证。
- **风险**：机器学习模型可能存在过拟合、市场体制变化导致模型失效、样本外表现可能下降。
- **策略价值**：该案例展示了机器学习可以显著提升传统量化策略的风险调整收益。
- **筛选评分**：95
- **原文**：[链接](https://github.com/Aiden0334/Machine-Learning-Enhanced-Alpha-Models)

---

### sbauwow/schwagent：基于AI的期权交易代理

- **收录时间**：2026-06-19 21:33
- **发布时间**：2026-06-19 20:08
- **作者**：sbauwow
- **来源**：GitHub Quant Repos
- **分类**：期权 · stock · us
- **频率**：intraday
- **摘要**：这是一个使用Charles Schwab API的AI驱动算法交易代理。它支持多种期权策略，包括轮子/theta策略、备兑看涨、铁鹰和垂直价差。该代理集成了量化回测、LLM信号审查和Telegram控制功能。使用Python编写，标有17颗星。该工具旨在通过AI增强期权交易决策。它允许用户通过Telegram远程监控和控制交易。虽然包含回测功能，但未提供具体性能数据。该代理适合有一定经验的期权交易者。
- **要点**：
  - 支持轮子策略、备兑看涨、铁鹰等常见期权策略。
  - 集成LLM进行信号审查，并支持Telegram远程控制。
  - 使用Charles Schwab API进行实盘交易。
- **风险**：AI代理决策可能不可预测、LLM信号可能产生错误、依赖第三方API（Schwab）、期权策略风险（如无限损失风险）。
- **策略价值**：该工具将AI与期权策略自动化结合，降低了手动交易期权策略的复杂性。
- **筛选评分**：95
- **原文**：[链接](https://github.com/sbauwow/schwagent)

---

### 预测市场与期权价格是否匹配？来自Binance和Polymarket的比特币阈值证据

- **收录时间**：2026-06-19 21:33
- **发布时间**：2026-06-19 12:00
- **作者**：Victoria Portnaya
- **来源**：arXiv Quantitative Finance
- **分类**：套利 · crypto · global
- **频率**：intraday
- **摘要**：该论文首次使用期权隐含基准测试加密货币阈值合约的预测市场定价。每小时比较Polymarket的Yes价格与Binance相同标的、行权价和到期日的看涨期权折扣后的风险中性二元价值。2023年9月比特币主合约平均定价差距为5.6个百分点（t=6.46，p<10^{-9}）。合并三个比特币阈值市场得到平均差距6.3个百分点（287个观测值）。差距具有持续性（AR(1)半衰期约4小时），但均值回归，表明信息传递缓慢。横截面回归显示，差距在低期权隐含概率和长到期时最大，符合预测市场的投机需求。delta对冲套利在保守交易成本后仍可盈利。Deribit扩展得到更大差距（11个百分点），以太坊结果混合。结论表明数字市场碎片化导致系统性定价差异。
- **要点**：
  - 预测市场与期权市场对相同比特币阈值合约存在系统性定价差异，平均差距约5.6个百分点。
  - 定价差距具有持续性但均值回归，半衰期约4小时，反映信息传递缓慢。
  - 差距在低概率和长到期时更大，暗示投机需求驱动。
  - delta对冲套利在考虑交易成本后仍可盈利，但统计显著性边际。
- **回测线索**：分析了2023年9月比特币合约的214个每小时观测值，平均定价差距5.6个百分点，delta对冲套利在扣除交易成本后仍可盈利，但统计显著性边际。
- **风险**：统计显著性边际、交易成本可能侵蚀利润、样本期有限、跨平台数据同步问题。
- **策略价值**：该发现揭示了数字金融市场的碎片化会导致经济上相同的支付出现持续定价偏差，为套利策略提供了实证基础。
- **筛选评分**：95
- **原文**：[链接](https://arxiv.org/abs/2606.19517)

---

### 基于梯度的效用短缺风险随机优化

- **收录时间**：2026-06-19 07:31
- **发布时间**：2026-06-18 12:00
- **作者**：Sumedh Gupte, Prashanth L. A., Sanjay P. Bhat
- **来源**：arXiv Quantitative Finance
- **分类**：机器学习 · multi · global
- **摘要**：本文研究了效用短缺风险（UBSR）的估计与优化问题。作者将UBSR扩展到无界随机变量，并涵盖了熵风险、期望分位数风险、风险价值（VaR）和二次风险等特例。在估计方面，推导了样本均值逼近估计器的非渐近误差边界。在优化方面，给出了光滑参数化下UBSR梯度的闭式表达式。提出了梯度估计器并证明了其均方误差边界。将梯度估计器融入随机梯度算法，并推导了强凸、凸和非凸目标下的收敛速率。在金融应用中验证了算法的有效性。
- **要点**：
  - UBSR扩展至无界随机变量，涵盖多种常见风险度量
  - 推导了UBSR的梯度解析表达式
  - 提出随机梯度算法并证明其收敛边界
- **回测线索**：论文通过金融应用实验展示了所提算法的性能。
- **风险**：UBSR对尾部事件敏感，且算法收敛性依赖于凸性假设。
- **策略价值**：为风险管理中的风险度量优化提供了可计算的梯度方法，有望应用于投资组合优化和风险控制。
- **筛选评分**：60
- **原文**：[链接](https://arxiv.org/abs/2506.01101)

---

### 基尼-贝叶斯连接：CAP斜率作为贝叶斯定理，及其在证据权重、Somers' D和校准中的应用

- **收录时间**：2026-06-19 07:31
- **发布时间**：2026-06-18 12:00
- **作者**：Denis Burakov
- **来源**：arXiv Quantitative Finance
- **分类**：因子 · multi · global
- **摘要**：本文建立了累积准确度曲线斜率与贝叶斯定理之间的明确联系。作者指出，标准化的违约概率是经过先验概率缩放的后验概率。证据权重（对数似然比）和基尼系数可以在CAP斜率框架下统一解释。论文展示了准确性比率、Somers' D和基尼系数本质上是相同指标的不同计算方式。通过比较实际结果与模型预测，可以诊断模型校准偏差。文中提供了离散和连续情况下的详细示例。该研究为信用风险评分模型评估提供了理论统一。
- **要点**：
  - CAP斜率等价于贝叶斯定理的累积坐标形式
  - 证据权重和信息价值可统一在CAP斜率几何中
  - 基尼系数、Somers' D和准确性比率是同一数值的三种计算
- **回测线索**：论文通过一个五区间离散示例和核密度连续示例验证了所有推导。
- **风险**：该方法依赖于模型校准质量，不准确的校准可能导致诊断偏差。
- **策略价值**：该理论统一了信用评分中多个常用性能指标，有助于更深入理解模型诊断和校准。
- **筛选评分**：65
- **原文**：[链接](https://arxiv.org/abs/2606.18545)

---

### 需要帮助确定算法中使用的止盈止损模型

- **收录时间**：2026-06-19 07:31
- **发布时间**：2026-06-18 08:58
- **作者**：SpectreIcarus
- **来源**：Reddit r/algotrading
- **分类**：趋势跟踪 · futures · us
- **摘要**：用户在Reddit上寻求关于算法交易中止盈止损模型选择的建议。用户提供了一些策略统计指标，但未透露具体策略细节。用户倾向于使用15%止损和18%止盈的比例，以降低最大回撤。该策略将基于TopstepX API运行，这是一个期货交易平台。用户希望在不暴露交易策略核心的情况下获得模型选择建议。评论中可能包含多种止盈止损方法的讨论。
- **要点**：
  - 用户寻求止盈止损模型选择建议
  - 倾向于15/18%的固定比例以控制回撤
  - 策略计划通过TopstepX API在期货市场执行
- **回测线索**：用户提到了部分统计数据，但未提供具体回测结果。
- **风险**：止盈止损比例可能过于粗糙，需要根据具体策略和市场条件调整。
- **策略价值**：止盈止损模型是算法交易中风险管理的核心，正确选择直接影响策略的收益和回撤表现。
- **筛选评分**：70
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1u8s51y/need_some_help_figuring_out_what_tpsl_model_to/)

---

### factorlab – Laboratório de Fatores Quantitativos

- **收录时间**：2026-06-19 07:31
- **发布时间**：2026-06-19 03:19
- **作者**：Jialei-Ni
- **来源**：GitHub Quant Repos
- **分类**：因子 · stock · us
- **频率**：daily
- **摘要**：factorlab é um projeto pessoal de pesquisa quantitativa focado na construção e teste de estratégias de trading baseadas em fatores. Utiliza indicadores financeiros e a biblioteca Alphalens para análise de fatores e avaliação de desempenho. O projeto é escrito em Python e ainda está em estágio inicial, sem estrelas no GitHub. Ele oferece um ambiente flexível e experimental para explorar comportamentos de sinais e métricas de avaliação.
- **要点**：
  - Foco em estratégias baseadas em fatores com Alphalens.
  - Ambiente experimental para teste de indicadores financeiros.
  - Projeto pessoal, ainda sem estrelas no GitHub.
- **回测线索**：Inclui fluxos de trabalho básicos de backtesting e análise de fatores com Alphalens.
- **风险**：Projeto experimental e pessoal; escalabilidade limitada.
- **策略价值**：Oferece um framework simples e flexível para pesquisadores iniciantes explorarem fatores e backtesting.
- **筛选评分**：85
- **原文**：[链接](https://github.com/Jialei-Ni/factorlab)

---

### AgentQuant: 自主量化交易研究平台

- **收录时间**：2026-06-19 07:31
- **发布时间**：2026-06-19 00:57
- **作者**：OnePunchMonk
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · stock · global
- **摘要**：AgentQuant是一个自主量化交易研究平台。它可以将股票列表转化为完全回测过的策略。该平台使用AI代理、真实市场数据和数学公式。整个过程无需编写任何代码。平台集成了多种工具如yfinance和VectorBT。它支持代理AI、自主代理和金融科技等技术。项目语言为Python，目前在GitHub上有117颗星。该平台旨在降低量化研究的门槛。用户可以专注于策略逻辑而无需技术细节。
- **要点**：
  - 无需编码即可将股票列表转化为回测过的策略
  - 集成AI代理、LangChain、LangGraph等先进技术
  - 支持yfinance和VectorBT进行数据获取和回测
- **回测线索**：Built-in backtesting via VectorBT and AI agents
- **策略价值**：该平台显著降低了量化交易研究的门槛，使非程序员也能快速生成并回测策略。
- **筛选评分**：90
- **原文**：[链接](https://github.com/OnePunchMonk/AgentQuant)

---

### Algoritmo para Mercado de Ações com Estatísticas de Lucro Consistente

- **收录时间**：2026-06-19 07:31
- **发布时间**：2026-06-19 00:56
- **作者**：DarkandBoring
- **来源**：Reddit r/algotrading
- **分类**：综合/其他 · stock · us
- **频率**：intraday
- **摘要**：Este post do Reddit apresenta os resultados de um algoritmo de trading que testa múltiplas estratégias no mercado de ações dos EUA. As estratégias incluem padrões de reversão como 'Double Bottom' e 'Liquidity Sweep', além de indicadores como Stochastic e RSI. A estratégia 'Double Bottom' obteve a maior taxa de acerto (75,7%) e retorno total de +1689,84. O algoritmo é projetado para operar apenas durante o pregão, sem posições overnight, utilizando a API Alpaca SIP. O autor disponibiliza um executável público básico para interessados. Há um risco de overfitting devido ao grande número de estratégias testadas.
- **要点**：
  - Testa 8 estratégias diferentes com dados históricos de ações dos EUA.
  - Estratégia Double Bottom apresenta win rate de 75,7% e retorno total de +1689,84.
  - Opera apenas intraday, sem posições overnight.
  - Risco de overfitting devido à otimização excessiva.
- **回测线索**：Apresenta resultados de backtest para 8 estratégias, com win rates entre 48% e 75,7% e total return de -69.62 a +1689.84.
- **风险**：Risco de overfitting devido a múltiplas estratégias; limitado a ações dos EUA e sem posições overnight.
- **策略价值**：Demonstra a importância de backtest sistemático e validação estatística para estratégias de trading algorítmico.
- **筛选评分**：90
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1u9br5g/stock_market_algo_stats_as_it_consistently_makes/)

---

### Algo-Ankit/AlphaSwarm

- **收录时间**：2026-06-18 20:50
- **发布时间**：2026-06-17 02:15
- **作者**：Algo-Ankit
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · multi · global
- **摘要**：A multi-tenant SaaS platform featuring an LLM-driven strategy compiler, FastAPI control plane, and isolated   Celery, background workers for executing parallel quantitative trading algorithms
Topics: 
Language: Python
Stars: 0
- **筛选评分**：55
- **原文**：[链接](https://github.com/Algo-Ankit/AlphaSwarm)

---

### 用缓和偏斜t分布拟合累积股票收益

- **收录时间**：2026-06-18 20:50
- **发布时间**：2026-06-18 12:00
- **作者**：Siqi Shao, R. A. Serota
- **来源**：arXiv Quantitative Finance
- **分类**：因子 · stock · us
- **频率**：daily
- **摘要**：本文分析了标普500指数多日收益的历史分布，累积天数从20到120天。随着累积天数增加，幂律尾部明显缓和，趋向于有限值。作者采用一个模型产生“有界逆伽马”稳态分布用于随机波动率，进而产生“缓和t分布”用于收益。通过Jones-Faddy对称性破缺机制，得到“缓和偏斜t分布”。该分布能够很好地拟合标普500多日收益分布，并捕捉到正均值和负偏斜的对称性破缺。拟合结果与均值随累积天数的近似线性关系一致，方差（均方实现波动率）更是如此。
- **要点**：
  - 标普500多日收益分布呈现尾部缓和
  - 提出缓和偏斜t分布模型
  - 模型捕捉了正均值和负偏斜特征
- **风险**：The model is fitted to historical S&P500 data and may not generalize to other markets or regimes.
- **策略价值**：更精确的收益分布建模有助于风险管理、期权定价和投资组合优化。
- **筛选评分**：60
- **原文**：[链接](https://arxiv.org/abs/2606.19318)

---

### 限价订单簿在单尺度机制下的二阶近似

- **收录时间**：2026-06-18 20:50
- **发布时间**：2026-06-18 12:00
- **作者**：Ulrich Horst, Dörte Kreher, Konstantins Starovoitovs
- **来源**：arXiv Quantitative Finance
- **分类**：做市 · multi · global
- **频率**：intraday
- **摘要**：本文在单临界尺度下建立了无限维限价订单簿模型的一阶和二阶近似。一阶近似由耦合的ODE-PDE系统给出，二阶近似则由柱形布朗运动驱动的无限维随机演化方程描述。驱动噪声过程表现出非平凡的相关性。作者证明了演化方程有唯一解，并且标准化的限价订单簿模型序列弱收敛于该解。他们还用一个线性化模型对市场数据进行了校准。该模型可用于推导投资组合清算价值的置信区间。
- **要点**：
  - 建立了LOB模型的一阶和二阶近似
  - 二阶近似由随机演化方程描述
  - 模型可校准并用于置信区间计算
- **风险**：The approximations rely on specific scaling assumptions that may not hold in all market conditions.
- **策略价值**：该研究为限价订单簿的动态提供了更精确的数学近似，有助于做市商和算法交易者优化执行策略。
- **筛选评分**：60
- **原文**：[链接](https://arxiv.org/abs/2308.00805)

---

### 量化交易引擎

- **收录时间**：2026-06-18 20:50
- **发布时间**：2026-06-18 04:16
- **作者**：HaoweiChan
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · multi · global
- **摘要**：这是一个与市场无关的量化交易引擎，使用Dash仪表板进行策略开发、回测和实盘交易。引擎基于Python编写，支持多种策略类型。它提供了一个可视化界面，便于用户分析和监控交易表现。该引擎可以用于股票、加密货币等多种资产类别。用户可以根据需要自定义交易逻辑。引擎还具有风险管理和资金管理功能。它旨在帮助交易者快速从回测过渡到实盘。
- **要点**：
  - 支持多种策略类型
  - 提供Dash仪表板
  - 可用于多种资产类别
- **回测线索**：Includes backtesting and live trading capabilities.
- **策略价值**：该引擎提供了一个通用的量化交易平台，简化了从开发到实盘的流程。
- **筛选评分**：60
- **原文**：[链接](https://github.com/HaoweiChan/quant-engine)

---

### 当市场边界弱化时：网络重构和制度依赖的跨资产溢出效应

- **收录时间**：2026-06-18 20:50
- **发布时间**：2026-06-18 12:00
- **作者**：Ruixue Jing, Luis Enrique Correa Rocha
- **来源**：arXiv q-fin.TR (Trading)
- **分类**：综合/其他 · multi · global
- **频率**：daily
- **摘要**：本文研究了加密货币、法定货币和标普500股票在2017年10月至2024年2月期间的整合程度。使用了滚动相关网络、社区结构、市场特定和系统范围的湍流指数以及VAR连接性分析。结果发现跨资产整合是间歇性的，平静时期相对分割，而压力下本地聚类增加、模块分离减弱。社区组成在压力时期变得更加混合。连接性分析显示制度转换改变了传导结构，而非简单地增加溢出幅度。在高湍流状态下，法定货币市场湍流成为主导传导渠道。网络聚类和模块性在传递预测不确定性方面发挥更大作用。网络结构是状态依赖的传导层，而非持久的外生驱动因素。研究强调了制度感知风险监控的必要性。
- **要点**：
  - 跨资产整合只在市场压力时期显著增强，平静时期资产类之间相对分割。
  - 压力下社区结构混合程度增加，模块化分离减弱。
  - 法定货币市场湍流在高波动状态下成为主要传导渠道。
  - 网络结构是状态依赖的，并影响冲击传播而非仅仅是放大。
- **风险**：在压力时期，跨资产耦合增强，可能导致多元化失效；全样本连接性估计可能低估危机时的风险传导。
- **策略价值**：该研究表明，投资者需要根据市场状态调整风险管理策略，因为多元化效应在压力时期可能急剧减弱。
- **筛选评分**：65
- **原文**：[链接](https://arxiv.org/abs/2605.30442)

---

### 如何进一步验证这个交易算法？（内含回测结果）

- **收录时间**：2026-06-18 20:50
- **发布时间**：2026-06-17 23:35
- **作者**：Puzzleheaded_Sun3104
- **来源**：Reddit r/algotrading
- **分类**：趋势跟踪 · multi · global
- **摘要**：该交易系统基于流动性扫描、指数加权移动平均（EWM）波动率机制检测和趋势延续概率。在贵金属（XAUUSD、XAGUSD、XPTUSD）回测中，盈利因子为1.1至1.6，最大回撤为5%至10%。外汇对表现参差不齐，部分盈利，部分接近盈亏平衡。指数（标普500、纳斯达克）整体接近盈亏平衡。加密货币（BTC/ETH）预期为负，最大回撤超过15%。作者仅进行了历史回测，尚未进行蒙特卡洛模拟或向前验证。主要关注点包括验证鲁棒性的下一步、何时认为该策略具有可扩展性，以及贵金属有效而加密货币失效是否暗示结构性优势或过拟合。
- **要点**：
  - 贵金属回测盈利因子1.1-1.6，最大回撤5-10%
  - 加密货币负期望，回撤>15%
  - 尚未进行蒙特卡洛或向前验证
  - 策略基于流动性扫描、EWM波动率和趋势延续
- **回测线索**：贵金属盈利因子1.1-1.6，最大回撤5-10%；加密货币负期望且回撤>15%。
- **风险**：加密货币表现差可能暗示过拟合；需要蒙特卡洛模拟和向前验证；回测数量有限。
- **策略价值**：该案例展示了多资产类别回测中策略表现分化的典型问题，强调需通过更严格的验证方法（如蒙特卡洛、向前测试）来区分真实alpha与过拟合。
- **筛选评分**：80
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1u8dkkb/how_would_you_further_validate_this_trading/)

---

### 发现宝藏，想分享！

- **收录时间**：2026-06-18 20:50
- **发布时间**：2026-06-17 19:25
- **作者**：CustardOk7073
- **来源**：Reddit r/algotrading
- **分类**：综合/其他 · multi · global
- **摘要**：该Reddit帖子分享了一个Youtube视频，揭示了算法交易中寻找真正优势的残酷现实。视频作者测试了131000个策略在不同资产上的表现。只有65个策略通过了前向测试和样本外测试，表现出稳健性和一致性。这些策略能够适应不同的市场环境，并产生合理风险下的良好回报。帖子作者认为这个视频适合让新人了解算法交易的困难。他们提出了一个关键问题：参数调整是为了满足个人偏好还是真实稳健性。帖子邀请观众讨论类似的学习曲线经历。
- **要点**：
  - 测试了131000个策略，仅65个通过严格验证。
  - 视频强调了过拟合和样本外表现的重要性。
  - 讨论了参数调整与策略稳健性之间的冲突。
- **回测线索**：测试了131000个策略，只有65个通过了前向测试和样本外测试，表现出稳健性。
- **风险**：过拟合风险高，大多数策略在样本外失效，需要严格的验证。
- **策略价值**：它提醒算法交易者，真正的交易优势极其罕见，需要严苛的回测和验证，避免过度优化。
- **筛选评分**：85
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1u87hhg/found_this_gem_and_wanted_to_share/)

---

### 德州转型中的电力市场价格形成因果结构映射

- **收录时间**：2026-06-18 07:20
- **发布时间**：2026-06-17 12:00
- **作者**：Shiva Madadkhani, Nils Sturma, Mathias Drton, Svetlana Ikonnikova
- **来源**：arXiv Quantitative Finance
- **分类**：机器学习 · multi · us
- **摘要**：该研究使用因果发现方法分析德州电力批发市场价格的演变。结果推翻了过去认为天然气价格主导市场的观点，发现风力发电已成为日前电价的最大因果驱动因素，其影响超过天然气的三倍。然而，在高峰时段，风能的压价效应正在减弱。风能增长还改变了阻塞成本分布，将其转移至远距离负荷中心。南德州和西德州负荷上升改变了系统价格和区域价差。研究揭示了新型发电和大型负荷的选址、速度和规模对未来电价风险和投资的关键作用。
- **要点**：
  - 风力发电取代天然气成为电价主要驱动因素
  - 风能压价效应在高峰时段减弱
  - 新能源布局改变阻塞成本分布
  - 负荷增长中心转移影响区域电价
- **风险**：市场转型可能导致历史因果关系失效，政策变化和容量投资决策影响未来价格动力。
- **策略价值**：为电力市场参与者和投资者提供了基于因果关系的价格风险新视角，对新能源投资和电网规划有重要参考价值。
- **筛选评分**：50
- **原文**：[链接](https://arxiv.org/abs/2604.14257)

---

### 量化交易研究平台 - 多维度策略评估

- **收录时间**：2026-06-18 07:20
- **发布时间**：2026-06-18 00:27
- **作者**：lguank
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · multi · multi
- **摘要**：该平台是一个基于Python的量化交易研究框架，提供多个用于系统化策略评估的模块。它包含基准归因分析，帮助理解策略相对于基准的收益来源。向前验证模块用于评估策略在样本外数据的稳定性。回撤分析模块提供最大回撤、持续时间等关键指标。分散化诊断工具帮助优化资产配置。平台适用于多资产类别的策略研究。代码公开在GitHub上，供社区使用和改进。
- **要点**：
  - 集成基准归因、向前验证、回撤分析和分散化诊断
  - 支持多种资产类别和市场的策略评估
  - 采用Python编写，开源免费
- **回测线索**：平台支持Walk-Forward验证和回撤分析，但未给出具体策略回测结果。
- **风险**：平台本身无交易风险，但用户开发的策略需谨慎避免过拟合。
- **策略价值**：提供了一个全面的量化策略评估工具箱，帮助研究者避免常见陷阱，提升策略稳健性。
- **筛选评分**：50
- **原文**：[链接](https://github.com/lguank/quantitative-trading-research-platform)

---

### 量化交易回测器 - MA50/MA200策略

- **收录时间**：2026-06-18 07:20
- **发布时间**：2026-06-18 02:29
- **作者**：PhyuSin2026
- **来源**：GitHub Quant Repos
- **分类**：趋势跟踪 · stock · us
- **频率**：daily
- **摘要**：该项目是一个用Python实现的量化交易回测工具，专门针对SPY ETF应用MA50/MA200移动平均线交叉策略。回测旨在评估简单趋势跟踪策略的历史表现。代码实现了买入和卖出信号生成逻辑。回测结果可能用于比较不同市场条件下的策略有效性。该仓库目前处于初始阶段，仅有基本功能。适合初学者学习回测框架。
- **要点**：
  - 使用MA50和MA200移动平均线交叉作为交易信号
  - 回测对象为SPY ETF，属于美国股票市场
  - 采用日频数据进行策略回测
  - 简单趋势跟踪策略，适合入门学习
- **回测线索**：回测展示了简单均线交叉策略，但未提供具体业绩指标。
- **风险**：震荡市场中易产生虚假信号，滞后性可能导致较大回撤。
- **策略价值**：展示了经典均线策略在主流ETF上的实用性，为新手提供了量化回测的入门范例。
- **筛选评分**：55
- **原文**：[链接](https://github.com/PhyuSin2026/Quantitative-Trading-Backtester)

---

### PIVOT：通过可微分的J\"ackel算子桥接Black-Scholes隐含波动率与价格目标

- **收录时间**：2026-06-18 07:20
- **发布时间**：2026-06-17 12:00
- **作者**：Raeid Saqur, Yannick Limmer, Anastasis Kratsios, Blanka Horvath, Hans Buehler
- **来源**：arXiv Quantitative Finance
- **分类**：期权 · stock · us
- **频率**：daily
- **摘要**：本文提出PIVOT，一个可微分层，用于连接Black-Scholes隐含波动率空间和价格空间。它保留了“Let's Be Rational”求解器的前向传递，并通过隐式微分实现后向传递，同时引入门控机制处理低vega区域。在单个H100 GPU上，融合Triton内核达到了17.9亿波动率/秒的计算速度，精度达到机器精度。在SPX数据上，PIVOT增强的目标函数将持有期价格MAE最多降低了43.4%，并在RUT、VIX和NDX上分别实现了40.1%、24.2%和16.7%的价格MAE改善。门控机制被证明是正确性合约而非调节旋钮。
- **要点**：
  - 可微分层连接隐含波动率和价格空间，保留LBR求解器前向传递。
  - 隐式微分后向传递，门控机制处理低vega奇异点。
  - 在SPX上价格MAE降低43.4%，跨资产表现优异。
  - 高性能实现：17.9亿波动率/秒，机器精度。
- **回测线索**：Tested on SPX OptionMetrics data: Pareto-dominated baselines with up to 43.4% reduction in price MAE; cross-asset gains of 40.1% (RUT), 24.2% (VIX), 16.7% (NDX) in price MAE.
- **风险**：Low-vega regime singularity requires careful gating; performance depends on quality of input data; computational overhead compared to non-differentiable methods.
- **策略价值**：PIVOT使得基于梯度的优化可以直接应用于期权定价和波动率曲面建模，有助于提升期权交易策略和风险管理模型的精度。
- **筛选评分**：60
- **原文**：[链接](https://arxiv.org/abs/2606.17065)

---

### 免费数据集：Polymarket 5分钟加密货币涨跌订单簿，逐秒数据（约2680万样本）

- **收录时间**：2026-06-18 07:20
- **发布时间**：2026-06-18 00:55
- **作者**：File-Environmental
- **来源**：Reddit r/algotrading
- **分类**：综合/其他 · crypto · global
- **频率**：intraday
- **摘要**：该数据集记录了Polymarket上5分钟加密货币涨跌市场的订单簿数据，涵盖BTC、ETH、SOL、XRP、DOGE、HYPE、BNB等货币对。数据以每秒频率采集，包含最佳买/卖价、数量以及买方的深度信息。时间范围从2026年3月至5月，总共约2680万个样本。数据格式为Parquet，采用CC0许可协议，可在Hugging Face和Kaggle上获取。作者希望研究者利用该数据集探索订单簿是否能在5分钟时间窗口内领先现货价格。
- **要点**：
  - 覆盖7种加密货币的涨跌市场订单簿数据。
  - 逐秒频率，包含最佳买/卖价及深度。
  - 约2680万样本，2026年3月至5月。
  - 免费公开，CC0许可。
- **风险**：Data limited to March-May 2026; only top-of-book; only for specific crypto pairs; markets may have low liquidity.
- **策略价值**：该数据集为高频预测市场研究提供了宝贵的订单簿数据，有助于探索市场微观结构与短期价格预测。
- **筛选评分**：80
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1u8fsg7/free_dataset_polymarket_5min_crypto_updown_order/)

---

### 25个代码年的前向测试能否赋予交易模型真正的可信度？

- **收录时间**：2026-06-18 07:20
- **发布时间**：2026-06-18 07:17
- **作者**：_WARBUD_
- **来源**：Reddit r/algotrading
- **分类**：综合/其他 · stock · us
- **频率**：daily
- **摘要**：一位交易者分享其交易模型的开发进展，详细描述了多个代码在不同时间区间内的前向测试结果。他们声称模型未经过任何拟合，并询问25个代码年的前向测试是否足以证明模型的可靠性。模型在GME挤压窗口期间实现了58%的胜率和约21%的利润。最近对10个代码各5个月的前向测试平均胜率在53%至58%之间。目前正在进行更大的测试：5个代码各5年，总计25个代码年。他们强调未对原始代码进行任何修改。
- **要点**：
  - 模型在GME事件中取得58%胜率和21%利润。
  - 10个代码各5个月的前向测试平均胜率53-58%。
  - 当前正在进行5个代码各5年的前向测试。
  - 声称未进行任何参数拟合。
- **回测线索**：Forward test results: 58% win rate, ~21% profit on GME during squeeze; recent 10 tickers, 5 months each averaged 53-58% win rate; 25 ticker-year test in progress.
- **风险**：Small sample size; potential survivorship bias; forward test not yet complete; lack of details on edge definitions.
- **策略价值**：该讨论强调了在交易模型开发中，长期、多代码的前向测试对于验证策略稳健性的重要性。
- **筛选评分**：85
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1u8pwb5/does_a_25_tickeryear_forward_test_give_a_trading/)

---

### OwenPetropulos/OPResearch

- **收录时间**：2026-06-17 21:41
- **发布时间**：2026-06-17 06:53
- **作者**：OwenPetropulos
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · multi · global
- **摘要**：这是一个专注于系统化投资策略和应用数据分析的量化金融与经济研究仓库。作者使用Python构建可复现的数据管道，处理市场、基本面及宏观数据，强调信号设计和回测的严谨性。兴趣领域涵盖资产管理、交易以及跨行业的股票研究。仓库以Python为主要编程语言，当前获得0星。
- **要点**：
  - 仓库提供可复现的Python数据管道，整合市场、基本面和宏观数据。
  - 重点在于系统化投资策略的信号设计和严格回测。
  - 涉及资产管理、交易和股票研究等领域。
- **回测线索**：Repository emphasizes backtesting rigor.
- **策略价值**：该仓库为量化研究者提供了一套完整的研究框架和工具，有助于提升策略开发的效率和可靠性。
- **筛选评分**：50
- **原文**：[链接](https://github.com/OwenPetropulos/OPResearch)

---

### 期权定价中计划事件风险的非跨越识别

- **收录时间**：2026-06-17 21:41
- **发布时间**：2026-06-17 12:00
- **作者**：Tenghan Zhong
- **来源**：arXiv Quantitative Finance
- **分类**：期权 · options · us
- **频率**：intraday
- **摘要**：本文提出了一种非跨越识别方法，将计划事件（如FOMC、CPI、非农就业）风险与期权定价中的波动率曲面分离。利用2022年5月至2025年8月的标普500指数期权数据，高斯和混合跳跃模型改善了事件跨越期权的定价误差。对于CPI和FOMC事件的识别最强，而非农就业较弱。污染曲面压力测试表明，若允许事件跨越报价进入无事件曲面，会错误吸收事件溢价。该方法提供了一种在不依赖事件跨越到期日的情况下识别事件风险的途径。
- **要点**：
  - 提出非跨越识别协议，分离事件风险与波动率曲面。
  - 高斯和混合跳跃模型在事件跨越期权定价中表现更好。
  - CPI和FOMC事件识别最强，非农就业较弱。
- **回测线索**：Backtest from May 2022 to August 2025 on SPX options shows that Gaussian and two-component mixture jumps improve held-out event-spanning pricing errors.
- **风险**：Identification is weaker for NFP; contaminated-surface stress test shows risk of absorbing event premia incorrectly. Method relies on clean separation of event and no-event expiries.
- **策略价值**：为期权交易者提供更精确的事件风险定价工具，有助于在宏观数据发布前评估期权溢价。
- **筛选评分**：55
- **原文**：[链接](https://arxiv.org/abs/2606.12872)

---

### 用黄金定价图表验证技术指标优于美元定价图表的算法

- **收录时间**：2026-06-17 21:41
- **发布时间**：2026-06-16 19:21
- **作者**：whoamisri
- **来源**：Reddit r/algotrading
- **分类**：趋势跟踪 · multi · global
- **摘要**：作者构建了一个算法，检验一个假设：以黄金计价的价格图表上的技术指标，优于以美元计价的图表上的指标。作者认为美元图表忽略了货币贬值和通胀，而黄金图表显示真实价值。该算法目前处于测试阶段，结果将发布在X平台上。尚未有公开的回测结果或详细数据。该假设挑战了传统技术分析中以美元为基础的做法。如果成立，可能改变交易者分析资产的方式。风险在于黄金价格本身可能不稳定。
- **要点**：
  - 核心假设：黄金计价图表能剔除货币贬值影响，使技术指标更有效。
  - 算法已建成，但尚无回测结果公布。
  - 结果将在X平台发布，目前信息有限。
- **回测线索**：Results pending; author will post on X.
- **风险**：Thesis assumes gold reflects true value; gold price can also be volatile. Historical outperformance may not persist.
- **策略价值**：如果验证成功，将挑战传统技术分析定价基准，可能为跨境资产分析提供新视角。
- **筛选评分**：60
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1u7apf7/built_an_algorithm_that_tests_a_thesis_i_had/)

---

### 口袋量化引擎

- **收录时间**：2026-06-17 21:41
- **发布时间**：2026-06-17 08:55
- **作者**：earosenfeld
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · stock · us
- **摘要**：这是一个免费数据的量化交易引擎，包含宏观崩盘风险评分、SEC 13F机构信号、基于规则的策略层以及Streamlit仪表盘。该引擎使用Python构建，旨在为散户提供机构级分析工具。宏观崩盘风险评分基于经济指标监测系统性风险。SEC 13F信号跟踪大型基金经理的持仓变化。规则策略层允许用户定义交易逻辑。仪表盘提供实时可视化。目前项目尚未有公开回测结果。数据来源全部免费，但可能影响数据质量。
- **要点**：
  - 集成了宏观风险评分、13F信号和规则策略三个模块。
  - 使用免费数据源，适合个人交易者实验。
  - 无回测结果披露，实际效果未知。
- **风险**：Dependence on free data sources may limit reliability and coverage. No backtest performance reported.
- **策略价值**：为个人交易者提供了整合宏观与机构信号的免费量化工具，降低了量化交易入门门槛。
- **筛选评分**：65
- **原文**：[链接](https://github.com/earosenfeld/pocket-quant)

---

### 基于LLM的多智能体系统用于自动化加密货币投资组合管理

- **收录时间**：2026-06-17 21:41
- **发布时间**：2026-06-17 12:00
- **作者**：Yichen Luo, Yebo Feng, Jiahua Xu, Paolo Tasca, Yang Liu
- **来源**：arXiv q-fin.TR (Trading)
- **分类**：机器学习 · crypto · global
- **频率**：daily
- **摘要**：该论文提出一个多智能体框架，包含三个专门智能体：加密货币智能体、新闻智能体和交易智能体。分别处理市场动态、每周新闻情绪以及信号融合和投资组合执行。评估了四种能力配置：零样本、思维链、检索增强生成和技能增强。在2025年全年回测中，分层（技能）配置实现了133.52%的累积收益和1.502的夏普比率，优于单智能体和深度学习基线。消融研究表明加密货币智能体最为关键，其移除导致累积收益下降42.57个百分点。跨模型比较显示多智能体系统在GPT-4o、GPT-5和Claude Sonnet 4.5下均优于单智能体。每个决策都可追溯到明确的智能体推理，提供了可解释的加密货币投资组合管理方法。
- **要点**：
  - 多智能体系统融合价格、链上数据、新闻和技术指标
  - 分层（技能）配置回测收益133.52%，夏普比率1.502
  - 加密货币智能体最为关键
  - 决策过程可解释
- **回测线索**：52-week backtest over top 15 L1 crypto; best config cumulative return 133.52%, Sharpe 1.502; outperforms baselines.
- **风险**：Dependence on LLM quality; multi-agent complexity; Crypto Agent critical; performance sensitive to configuration.
- **策略价值**：展示了可解释的基于LLM的多智能体系统在加密货币管理中的有效性，克服了深度学习黑箱问题。
- **筛选评分**：70
- **原文**：[链接](https://arxiv.org/abs/2501.00826)

---

### 通过分类器模型的集成强化学习：提升交易策略的风险-收益权衡

- **收录时间**：2026-06-17 21:41
- **发布时间**：2026-06-17 12:00
- **作者**：Zheli Xiong
- **来源**：arXiv Quantitative Finance
- **分类**：机器学习 · multi · global
- **频率**：daily
- **摘要**：本文研究集成强化学习模型在金融交易策略中的应用，使用分类器提升性能。结合A2C、PPO、SAC等强化学习算法与支持向量机、决策树、逻辑回归等传统分类器。评估不同集成方法，并与单一RL模型比较。实验表明集成方法在风险调整收益上通常优于基础模型。但性能对方差阈值、分类器组、RL-智能体对和市场范围敏感。重复实验证实集成选择能提高稳健性，但优势是有条件的。研究强调了RL与分类器结合的价值，适用于交易、机器人等领域。
- **要点**：
  - 集成RL与分类器可改善风险调整收益
  - 性能敏感于多个参数选择
  - 优势有条件，非自动适用于所有数据集
  - 具有跨领域应用潜力
- **回测线索**：Evaluated on financial metrics; performance sensitive to variance threshold, classifier group, RL-agent pair, and market universe.
- **风险**：Ensemble performance conditional on parameters; may not generalize across all datasets; requires careful tuning.
- **策略价值**：提供了一种可解释的强化学习交易策略增强方法，有助于在动态环境中做出更稳健的决策。
- **筛选评分**：75
- **原文**：[链接](https://arxiv.org/abs/2502.17518)

---

### 游戏开发者制作的加密货币交易机器人

- **收录时间**：2026-06-17 21:41
- **发布时间**：2026-06-17 00:46
- **作者**：yaboiq27
- **来源**：Reddit r/algotrading
- **分类**：均值回归 · crypto · global
- **频率**：intraday
- **摘要**：该策略由一位游戏程序员开发，使用基于规则的周期系统。系统结合RSI、斐波那契水平、趋势/成交量/广度过滤器等指标。在4小时K线图上进行长期现货交易。参数通过遗传算法和walk-forward优化。过去5年回测显示训练币种回报504%，未训练币种回报250%。已在模拟交易中运行，即将在树莓派上实盘运行。使用CCXT获取数据和下单，FastAPI监控。策略非机器学习，而是基于规则的循环系统。作者强调进行了多轮测试，防止过拟合。
- **要点**：
  - 游戏程序员开发的加密货币交易机器人
  - 基于RSI、斐波那契和趋势过滤器的规则系统
  - 回测5年504%收益，250%在未见币种上
  - 已模拟交易，准备实盘运行在树莓派上
- **回测线索**：Backtested 504% return on trained coins, 250% on untrained coins; walk-forward optimization including 2022; realistic fees/slippage.
- **风险**：Risk of overfitting due to parameter tuning on historical data; long-only spot limits opportunities; performance may vary live.
- **策略价值**：展示了一个无需机器学习的规则系统也能取得高收益的案例，对业余交易者具有启发意义。
- **筛选评分**：75
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1u7ixpv/game_developer_made_crypto_trading_bot/)

---

### Quantloopp 顶级策略

- **收录时间**：2026-06-17 07:20
- **发布时间**：2026-06-17 05:28
- **作者**：paappraiser
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · multi · global
- **摘要**：该项目收集了来自Hermes Quant自主系统研究的10个顶级量化交易策略。策略使用Python实现，并获得1颗星。这些策略可能涵盖多种交易逻辑，如趋势跟踪、均值回归等。仓库旨在为量化开发者提供经过自动研究验证的冠军策略参考。用户可直接克隆并应用于自己的回测或实盘环境。
- **要点**：
  - 包含10个通过自主系统研究筛选的冠军策略。
  - 策略来源为Hermes Quant研究。
  - 使用Python实现，方便部署。
  - 适合作为量化策略的基准或灵感来源。
- **风险**：策略集合可能包含多种复杂方法，需仔细评估每种策略的风险；历史冠军策略不一定适应未来市场环境。
- **策略价值**：该集合提供了多种策略的现成实现，可加速量化策略研究和对比，尤其适合初学者学习和借鉴。
- **筛选评分**：75
- **原文**：[链接](https://github.com/paappraiser/Quantloopp-Top-stratagies)

---

### 市场情绪分析器2.0

- **收录时间**：2026-06-17 07:20
- **发布时间**：2026-06-16 16:18
- **作者**：VISHESH-53
- **来源**：GitHub Quant Repos
- **分类**：机器学习 · multi · global
- **频率**：daily
- **摘要**：该项目是一个量化交易策略，融合新闻情绪分析、机器学习模型和风险管理回测框架。它使用Python语言实现，旨在通过自动处理新闻数据、提取情绪信号并生成交易决策。策略包含完整的回测模块，帮助评估历史表现。目前仓库获得0星，表明关注度较低。作者为VISHESH-53。该工具适合对新闻驱动交易感兴趣的量化研究者。
- **要点**：
  - 通过新闻情绪驱动交易决策。
  - 集成机器学习模型预测市场方向。
  - 包含风险管理的回测框架。
  - 使用Python实现，易于扩展和定制。
- **风险**：Sentiment data may be noisy or biased; machine learning model risk of overfitting to historical news patterns; requires ongoing data pipeline maintenance.
- **策略价值**：新闻情绪是市场动因之一，该工具提供了一个从数据获取到策略回测的完整流程，适合快速验证情绪因子有效性。
- **筛选评分**：78
- **原文**：[链接](https://github.com/VISHESH-53/market-sentiment-analyzer-2.0)

---

### 超越微笑：混合卷积VAE的加密货币波动率曲面

- **收录时间**：2026-06-17 07:20
- **发布时间**：2026-06-16 12:00
- **作者**：Sadanand Singh, Allam Reddy, Manan Chopra
- **来源**：arXiv Quantitative Finance
- **分类**：机器学习 · crypto · global
- **频率**：intraday
- **摘要**：本文提出一种卷积变分自编码器用于加密货币隐含波动率曲面，结合二次微笑拟合和确定性期限路由规则。模型基于2023年5月至10月Binance期权BTC和ETH的6034个完整每小时曲面数据，在6x7期限-Delta网格上参数化。在10-50%掩码率下，隐藏单元曲面补全RMSE为0.94-1.56波动率点。混合预测器在50%掩码时达到0.83波动率点，比单独微笑拟合（7.00）降低八倍误差，且无额外推理成本。在模拟整期行权价缺失的结构性相关空洞模式下，微笑拟合误差达9.6-13.1点，而学习模型仅1.5-1.9点，表明生成模型是唯一可行的预测器。联合训练BTC和ETH使两个市场分布内模型性能比单一符号模型提升9-27%，表明两大加密货币在观测窗口内共享波动率曲面流形。混合模型在所列行权价上无日历套利和无蝶式套利，而参数微笑拟合在高掩码率下无法实现。训练模型每快照重构误差在无监督情况下识别出10月底ETF预期反弹和2023年8月17日闪崩为高误差时期。所有训练和评估基础设施已开源以支持可重复研究。
- **要点**：
  - 混合模型显著提升波动率曲面填补精度，尤其在高缺失率下优于纯参数方法。
  - 联合训练BTC和ETH发现共享曲面流形，提升跨资产泛化能力。
  - 模型自动检测市场异常事件（如闪崩），无需额外标签。
  - 开源代码和基础设施促进可重复研究。
- **回测线索**：Hybrid predictor achieves 0.83 vol-point RMSE at 50% masking vs 7.00 for smile-only; joint training improves single-symbol performance by 9-27%.
- **风险**：Model may overfit to historical patterns (May-Oct 2023); structural market regime shifts could degrade performance; reliance on Binance options liquidity.
- **策略价值**：该研究为加密货币期权市场提供了高精度、无套利的波动率曲面建模工具，直接支持定价、风险管理和衍生品策略开发。
- **筛选评分**：80
- **原文**：[链接](https://arxiv.org/abs/2606.16961)

---

### 预测美国国债收益率曲线：一种分布鲁棒的机器学习方法用于利率风险管理

- **收录时间**：2026-06-17 07:20
- **发布时间**：2026-06-16 12:00
- **作者**：Jinjun Liu, Ming-Yen Cheng
- **来源**：arXiv Quantitative Finance
- **分类**：因子 · futures · us
- **频率**：daily
- **摘要**：该研究将收益率曲线预测视为分布不确定性下的决策问题，提出一种融合参数因子模型和机器学习的分布鲁棒集成框架。因子增强的动态Nelson-Siegel模型捕捉曲线动态，随机森林建模非线性关系。鲁棒预测组合惩罚尾部风险，提高了各期限的样本外表现。该框架支持基于DV01的利率风险管理，适用于企业、机构和资产负债表决策者。
- **要点**：
  - 结合动态Nelson-Siegel因子模型与随机森林。
  - 分布鲁棒优化处理收益率曲线预测中的分布不确定性。
  - 基于DV01的风险管理，提升样本外预测稳健性。
- **回测线索**：在多个期限上实现了样本外性能提升，具体指标未详细列出。
- **风险**：模型依赖历史数据，极端政策变化可能导致模型失效；分布鲁棒性虽增强稳健性，但不能完全规避尾部风险。
- **策略价值**：该研究为利率风险管理者提供了一种更稳健的收益率曲线预测方法，有助于在不确定环境中优化套保和资产配置决策。
- **筛选评分**：82
- **原文**：[链接](https://arxiv.org/abs/2601.04608)

---

### 耗时6个多月构建并压力测试一套系统性日内期权策略——分享结果、PT1失败及修复，寻求盲点反馈

- **收录时间**：2026-06-17 07:20
- **发布时间**：2026-06-17 03:47
- **作者**：Technical_Sea_5022
- **来源**：Reddit r/algotrading
- **分类**：期权 · stock · us
- **频率**：intraday
- **摘要**：作者开发了一套基于规则、全自动的IWM 0DTE期权日内策略，采用平值期权、每日约2个信号、4层阶梯式止盈（基于ATR）和ATR止损。回测5年（2021-2026）显示胜率55.5%，TP1后到达TP2的概率高达84.9%，使得平均盈利大于平均亏损。逐年独立验证（walk forward）中参数一致，各年表现稳定。策略完全自动化执行，作者不公开信号逻辑，但展示测试过程并寻求反馈。
- **要点**：
  - 5年回测2900个信号，胜率55.5%，TP1后高概率继续。
  - 4层阶梯止盈（1-4倍ATR），平均盈利显著大于亏损。
  - 逐年独立验证，参数未调整，表现一致。
- **回测线索**：5年SIP回测（2021-2026），约2900个信号，胜率55.5%，TP4率24.3%，年化分年验证参数未调整。
- **风险**：0DTE期权时间衰减快；尾部风险；市场极端行情下执行滑点可能影响实际表现。
- **策略价值**：该策略展示了严谨的日内期权策略开发与测试流程，为0DTE期权系统性交易提供了可参考的实证案例。
- **筛选评分**：88
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1u7o1yw/spent_6_months_building_and_stresstesting_a/)

---

### NY Striker v2.2 在MNQ上使用移动止盈锁定利润，在500点清算暴跌前确保盈利日

- **收录时间**：2026-06-17 07:20
- **发布时间**：2026-06-17 06:10
- **作者**：B_Ware321
- **来源**：Reddit r/algotrading
- **分类**：趋势跟踪 · futures · us
- **频率**：intraday
- **摘要**：该策略今日仅在MNQ上触发交易，采用2手入场和不同止盈目标。机器人接近全止盈时移动止损锁定利润，随后市场出现剧烈反向波动并暴跌500点，止损被触发，锁定了约66%的预期利润。若无移动止损，初始止损会被击穿导致最大亏损；若仅移动至保本，则当日收益为零。该案例展示了移动止损在保护回撤缓冲和规避暴跌中的关键作用。策略强调一致性优于贪婪。
- **要点**：
  - 使用移动止盈在暴跌前锁定66%利润。
  - 2手入场，不同止盈目标，无负滑点。
  - 若未移动止损，将遭受最大亏损；仅保本则收益为零。
- **风险**：过早止盈可能错失更大行情，但移动止损有助于保护利润并防止回撤。
- **策略价值**：该案例生动展示了移动止损在保护利润、规避大幅回撤中的实际效果，验证了纪律性风险管理的价值。
- **筛选评分**：90
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1u7rurc/ny_striker_v22_trailing_profits_on_mnq_to_secure/)

---

### 智能交易第一天

- **收录时间**：2026-06-16 23:09
- **发布时间**：2026-06-16 10:22
- **作者**：TastyTrading
- **来源**：Reddit r/algotrading
- **分类**：趋势跟踪 · stock · us
- **频率**：intraday
- **摘要**：用户使用Claude AI、Ruby脚本和Robinhood账户进行智能交易实验。机器人基于第一个1小时K线收盘判断趋势，执行TQQQ的日内动量交易。设置1%止损，随着价格上涨动态调整止损至当日最高价下方1%。为防止隔夜风险，规定在收盘前5分钟平仓。第一笔交易买入后一度盈利0.80%，但隔夜回吐大部分涨幅。目标是锁定0.5%-1%的小幅盈利，追求高胜率。机器人表现将在Thetapal网站的比赛中透明追踪。
- **要点**：
  - 机器人基于第一根1小时K线收盘判断日内动量方向。
  - 设置1%固定止损，并通过跟踪当日最高价动态上移止损。
  - 为避免隔夜风险，强制在收盘前5分钟清仓。
- **风险**：Leverage risk (TQQQ is 3x leveraged ETF), stop loss may not guarantee exit due to gap risk, no backtest validation, reliance on AI model behavior.
- **策略价值**：展示了如何利用AI大模型结合简单规则实现日内动量交易，并通过动态止损和强制日内平仓控制风险。
- **筛选评分**：55
- **原文**：[链接](https://www.reddit.com/r/algotrading/comments/1u70v61/agentic_trading_day_1/)

---

### Alphanume策略实验室

- **收录时间**：2026-06-16 23:09
- **发布时间**：2026-06-16 21:44
- **作者**：alphanume-markets
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · multi · global
- **摘要**：这是一个由Alphanume市场数据API驱动的生产级量化交易研究工具。它提供了一套用于策略开发、回测和执行的框架。仓库使用Python编写，拥有47个星标。该实验室旨在帮助交易者快速将想法转化为可交易的策略，并支持多种数据源和策略类型。目前没有提供具体的回测结果，但框架本身强调生产环境下的可靠性和效率。
- **要点**：
  - 生产级量化交易研究框架，基于Alphanume API。
  - Python语言实现，社区活跃（47星）。
  - 支持多种策略类型和数据源。
- **回测线索**：Designed for production-ready backtesting and research; no specific backtest results provided.
- **策略价值**：为量化交易者提供了一个从研究到生产的完整工具链，降低了策略开发和部署的门槛。
- **筛选评分**：60
- **原文**：[链接](https://github.com/alphanume-markets/Alphanume-Strategy-Lab)

---

### 静态增长-防御风险组合的连续现金覆盖过滤器：慢尾补偿、V型崩溃刹车、滚动验证和最大现金组合

- **收录时间**：2026-06-16 23:09
- **发布时间**：2026-06-16 12:00
- **作者**：Zheli Xiong
- **来源**：arXiv Quantitative Finance
- **分类**：综合/其他 · multi · us
- **频率**：daily
- **摘要**：本文研究了一种模块化现金覆盖规则，用于在固定的50/50增长-防御风险组合与现金之间进行配置。测试了两个独立过滤器：慢尾过滤器（基于补偿、利率逆风、风险溢价压缩等状态）和V型过滤器（基于VIX、利率、信用、回撤和重新入场状态）。每日取两者中较大的现金权重作为最大现金层。在2017-2026年的共同窗口上，最大现金组合实现了18.83%的年化收益率，优于全风险组合的16.62%，并将最大回撤从-33.59%降至-18.05%。滚动窗口外样本测试中，该组合年化收益率为19.35%，最大回撤为-22.05%。2022年后的测试显示，在强劲反弹期间回撤较低但收益率也较低。结果支持现金覆盖作为回撤控制工具，而非独立的收益增强策略。
- **要点**：
  - 慢尾和V型两个过滤器独立生成现金权重，每日取最大值。
  - 最大现金组合在2017-2026年将最大回撤从-33.59%降至-18.05%。
  - 滚动窗口外样本验证了策略的鲁棒性。
- **回测线索**：Walk-forward validation on 2017-2026; max-cash combination improves CAGR and reduces drawdown significantly.
- **风险**：May underperform during strong rallies; fully real-time variable re-screening and multiple-testing adjustments are future work.
- **策略价值**：提供了一种模块化的现金覆盖方法，有效控制投资组合回撤，同时保持较好的收益表现。
- **筛选评分**：65
- **原文**：[链接](https://arxiv.org/abs/2606.09025)

---

### 基于移位数据增强的稳健Transformer一步股票指数预测

- **收录时间**：2026-06-16 23:09
- **发布时间**：2026-06-16 12:00
- **作者**：Tien Thanh Thach
- **来源**：arXiv Quantitative Finance
- **分类**：趋势跟踪 · stock · global
- **摘要**：本文提出了一种改进的Transformer架构，结合移位数据增强（SDA）用于一步股票指数预测。使用带预热的余弦退火学习率调度器。在VN30和S&P 500指数上的实验表明，SDA有效降低了预测误差和运行间变异性，增强了模型对超参数选择的鲁棒性。余弦退火与SDA的组合取得了最佳性能，凸显了数据增强在Transformer金融预测中的重要性，而非单纯增加模型复杂度。该方法为噪声金融环境下的稳健指数预测提供了计算高效的实用方案。
- **要点**：
  - 提出移位数据增强（SDA）技术，有效降低预测误差和运行变异性。
  - 余弦退火学习率调度优于广义逆幂调度。
  - 在VN30和S&P 500指数上验证，SDA组合效果最佳。
- **回测线索**：Outperforms baseline on VN30 and S&P 500 datasets; metrics include forecasting errors and run-to-run variability.
- **风险**：Potential overfitting to historical patterns; limited evaluation on only two indices.
- **策略价值**：提供了一种计算高效且鲁棒的股票指数预测方法，强调了数据增强在金融预测中的关键作用。
- **筛选评分**：65
- **原文**：[链接](https://arxiv.org/abs/2606.15701)

---

### 逆向选择与价格读取下的最优报价

- **收录时间**：2026-06-16 23:09
- **发布时间**：2026-06-16 12:00
- **作者**：Alexander Barzykin, Philippe Bergault, Olivier Guéant, Malo Lemmel
- **来源**：arXiv q-fin.TR (Trading)
- **分类**：做市 · multi · global
- **摘要**：该论文针对做市商在实际交易中面临的两个关键风险——逆向选择和价格读取——提出了一个易于处理的框架。逆向选择源于知情交易者，而价格读取指做市商自身报价可能无意中暴露其库存方向。现有文献对此关注有限，仅停留在简化模型。作者扩展了Ho-Stoll和Avellaneda-Stoikov等经典做市模型，考虑了交易规模分布、客户分层、价格动力学、alpha信号以及内部化与外部化的权衡。新框架使做市商能够更有效地调整报价，以应对信息风险。该研究填补了理论与实践之间的空白，提供了可操作的报价优化方法。
- **要点**：
  - 提出兼顾逆向选择和价格读取风险的做市报价框架
  - 扩展经典做市模型，加入交易规模分布和客户分层等因素
  - 为做市商提供可操作的报价优化策略
- **风险**：面临知情交易者的逆向选择风险；自身报价可能泄露库存方向，被算法利用
- **策略价值**：该框架帮助做市商在实际市场中更精准地管理信息风险，降低报价成本
- **筛选评分**：70
- **原文**：[链接](https://arxiv.org/abs/2508.20225)

---

### 阳光交易还是阴影交易：Hyperliquid上的市场影响与逆向选择

- **收录时间**：2026-06-16 23:09
- **发布时间**：2026-06-16 12:00
- **作者**：Davide Barone, Fabrizio Lillo
- **来源**：arXiv q-fin.TR (Trading)
- **分类**：做市 · crypto · global
- **摘要**：该研究基于Hyperliquid平台（全链上限价订单簿），利用地址级数据重构了430万个隐藏元订单并与46.5万个可见TWAP订单比较。隐藏订单遵循前端加载的U型执行模式，符合瞬时影响最优执行理论，而TWAP订单近乎均匀交易。可见TWAP订单的执行成本低于可比隐藏订单，且永久价格影响更小。与可见TWAP同时执行的隐藏订单会承受更高的永久成本，表明逆向选择成本向非公告者转移。可见TWAP程序能吸引流动性提供：执行期间市场深度增加且订单簿向吸收侧倾斜，且订单规模越大效果越显著。研究实证支持Admati和Pfleiderer（1991）的阳光交易理论。
- **要点**：
  - 可见TWAP订单比隐藏订单执行成本更低、永久影响更小
  - 阳光交易将逆向选择成本转移给非公告方
  - 公开订单能吸引流动性，增加市场深度
- **风险**：阳光交易可能将逆向选择成本转嫁给未公开订单的交易者；流动性提供需谨慎评估信息风险
- **策略价值**：该研究为加密货币市场中的订单披露策略提供了实证依据，有助于交易者优化执行方案
- **筛选评分**：70
- **原文**：[链接](https://arxiv.org/abs/2606.15715)

---

### QuantDinger 量化交易平台

- **收录时间**：2026-06-16 23:09
- **发布时间**：2026-06-16 22:07
- **作者**：brokermr810
- **来源**：GitHub Quant Repos
- **分类**：综合/其他 · multi · global
- **摘要**：该平台是一个基于人工智能的量化交易系统，支持加密货币、股票和外汇报价。它提供回测、实盘交易、市场数据获取和多智能体研究功能。平台使用Python开发，集成了Alpaca、Binance、Coinbase等交易所接口。其核心功能包括vibe交易、交易代理和AI交易策略。平台在GitHub上拥有8101颗星，表明社区活跃度高。该平台旨在为量化交易者提供一站式的开发和执行环境。
- **要点**：
  - 支持加密货币、股票和外汇报价，覆盖多资产类别
  - 集成回测、实盘交易和市场数据功能
  - 使用AI和多智能体技术辅助交易决策
- **回测线索**：内置回测功能，支持历史数据测试策略表现
- **风险**：多资产平台风险分散，但需注意模型过拟合和实时交易的系统风险
- **策略价值**：该平台降低了量化交易的门槛，使个人开发者也能快速搭建和部署AI交易策略
- **筛选评分**：80
- **原文**：[链接](https://github.com/brokermr810/QuantDinger)

---

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
