# 量化策略汇总

> 自动生成 · 最后更新：2026-06-19 21:33 · Asia/Shanghai
> 共 74 条策略

## 目录

- [2026-06（74）](#2026-06)

---

## 2026-06

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
