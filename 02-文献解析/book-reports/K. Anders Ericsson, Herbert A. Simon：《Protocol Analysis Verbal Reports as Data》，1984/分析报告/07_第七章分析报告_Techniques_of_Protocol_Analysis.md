# 第七章分析报告：Techniques of Protocol Analysis Examples（协议分析技术实例）

## L### 一、章节定位与功能

### L### 定位
第七章是全书的方法论"展示厅"——第六章建立了协议分析的理论和方法框架，第七章则通过一系列具体实例展示这些方法在实际协议分析中如何被应用。从非正式分析到形式化预测，从简单任务（心算加法）到复杂任务（河内塔、TOH同构问题），本章提供了从"初学者水平"到"专家水平"的完整技术谱系。

### L### 功能
本章承担三重功能：(1) 教学功能——以具体协议为例逐步展示分析过程（阅读→释义→推论）；(2) 验证功能——通过实例证明第六章所描述的方法确实能够生成对口头报告数据的非平凡预测；(3) 拓展功能——展示协议分析不仅用于"理解"认知过程，还可用于"检验"竞争性理论。

### L### 战略意义
第七章是全书论证的"经验闭环"——它回到第一章提出的"从口头数据中推论认知过程"这一核心目标，并以一系列成功实例证明：这一目标是可达成的。

---

## L### 二、结构分析

### L### 表层结构
本章共7节：
- 7.1 Informal Protocol Analysis —— 非正式协议分析
- 7.2 Using a Theory for Protocol Prediction —— 使用理论进行协议预测
- 7.3 Characteristics of Generated Information: Representations —— 生成信息的特征：表征
- 7.4 Sequences of Heeded Information —— 被注意信息的序列
- 7.5 Processes With Alternative Realizations —— 有多种实现方式的过程
- 7.6 Reliability of Verbal Reports —— 口头报告的信度
- 7.7 Concluding Remarks and Future Directions —— 总结与未来方向

### L### 深层结构
论证以"分析深度递进"为主轴：
1. **非正式分析**（7.1-7.2）：以最小理论承诺分析协议——仅区分"阅读""释义""推论"三层过程。
2. **表征推论**（7.3）：从协议中推论被试使用的内部表征——Eight Puzzle和TOH同构问题。
3. **序列预测**（7.4）：从过程模型中预测被注意信息的序列并与协议匹配。
4. **多实现过程**（7.5）：讨论同一任务可被不同策略实现时如何分析协议。
5. **信度评估**（7.6）：审查口头报告本身的信度以及协议编码的信度。
6. **展望**（7.7）：对协议分析未来发展的讨论。

---

## L### 三、内容分析（核心论题+关键论点案例）

### L### 核心论题
**论题一：即使是最低理论承诺的分析也能从协议中提取有意义的过程信息。** 7.1节展示了仅通过区分"阅读"（Read）、"释义"（Paraphrase）和"推论"（Inference）三层过程，就能对Ohlsson (1980)的三项系列任务协议进行有意义的结构分析——"Read process accounts for almost a third of the protocol segments, 17 out of 56."

### L### 核心论题
**论题二：协议分析可以区分不同表征和策略。** 7.3节展示了如何从协议中推论被试使用的内部表征——Eight Puzzle中被试几乎只注意线性序列1-2-3-4-5-6-7-8中的邻接关系（而非同样有用的列关系），以及TOH同构问题中被试使用"移动"表征还是"改变"表征。

### L### 关键论点
1. **"and/then"推理标记**：在序列任务协议中，"and"和"then"的话语标记可靠地指示了推理过程——"and"标记前提的联结，"then"标记推论的引出。

2. **H1 vs H2的区分力**：在心算加法例子中，两个竞争性假设（从左到右累加vs从右到左累加）预测了完全不同的中间结果集合。一个被试的协议匹配H1的6个预测中的6个——"The chances that such a close match with H1 could be produced by chance are less than one in a trillion."

3. **表征可以从两类协议语句中推论**：对"移动"的描述（"So the small globe goes over to the guy with the medium-sized globe"→移动表征）和对"状态"的描述（"The small monster has the large"→基于怪物的列表表征）。

4. **产生式系统与协议的直接比对**：对河内塔的两种策略（目标递归策略vs知觉策略），产生式系统模型预测了不同的信息序列。被试的协议与他们被训练使用的策略高度一致。

5. **协议预测的"不完全性容忍"**：即使口头化是不完全的，H1仍然优于H2——因为H1预测的数字集合在协议中出现的比例远高于H2。

### L### 关键案例
1. **Ohlsson (1980)的三项系列任务协议**（7.1）：以"阅读/释义/推论"三层分类分析56个协议段，展示"and/then"标记的推理功能。
2. **心算加法的H1-H2竞争性检验**（7.4）：两个模型预测了几乎不相交的中间结果集合，协议数据清晰地支持H1。
3. **Eight Puzzle的表征分析**（7.3）：从274个"意图"段和132个"认知"段中推论出被试的线性序列表征——目标配置被表征为1-2-3-4-5-6-7-8序列，而非3×3矩阵。
4. **TOH同构问题（Monster Problems）**（7.3）：被试使用的表征可由其对移动和状态的描述推断——两个编码者独立判断的完全一致验证了这一方法。
5. **河内塔的策略对照**（7.4）：目标递归策略的被试按照[Goal → Test → State → Action]序列口头化，而知觉策略的被试按照[Biggest → Goal → State]序列口头化。

---

## L### 四、逻辑梳理（论证链条+因果转折）

### L### 论证链条
1. **从零开始**（7.1）：不预设理论框架，仅以"阅读/释义/推论"三级分类分析协议→证明即使是最粗糙的分析也能提取过程信息。
2. **引入理论**（7.2-7.3）：当有理论可用时，理论允许两类预测——弱预测（信息类型，不预测顺序）和强预测（信息序列）。
3. **从协议中推论表征**（7.3）：Eight Puzzle→被试使用线性序列表征；TOH同构→被试使用与问题措辞一致的"移动"或"改变"表征。
4. **从模型中预测序列**（7.4）：心算加法→H1预测的中间结果集与协议匹配；河内塔→产生式系统模型的预测与被试实际口头化高度一致。
5. **处理个体差异**（7.5）：同一任务可被不同策略实现，协议分析的任务是在个体协议中识别策略签名。
6. **信度评估**（7.6）：口头报告的重测信度和编码者间信度。
7. **未来方向**（7.7）：探索协议分析与其他方法（眼动、脑成像）的结合。

### L### 因果转折
- **关键转折1**（7.1→7.2）：从"无理论"的非正式分析到"有理论"的预测性分析——前者是探索性的，后者是检验性的。
- **关键转折2**（7.3）：从"协议陈述了什么"到"协议陈述的方式揭示表征"——不仅是信息的内容，信息的措辞本身也提供关于表征的线索。
- **关键转折3**（7.4-7.5）：从"一个任务一个正确策略"到"一个任务多种可行策略"——协议分析的任务从"验证唯一正确模型"转向"识别个体使用的策略"。

---

## L### 五、材料使用方式

### L### 材料类型
1. **完整协议转录**：Ohlsson (1980)的三项系列任务协议（56段）、心算加法的三份协议、河内塔协议。
2. **协议编码数据**：心算加法的中间结果集合、Eight Puzzle的意图和认知频次统计（Figure 7-2）、TOH同构问题中移动和状态的措辞分析。
3. **产生式系统模型**：河内塔的目标递归策略和知觉策略的产生式系统。
4. **信度数据**：重测信度、编码者间信度。
5. **附录材料**：TA指令示例（本章附录）。

### L### 使用策略
- **"逐步放大"策略**：从协议的最粗粒度分析（Read/Paraphrase/Inference）开始，逐渐放大到细粒度分析（产生式系统层级）。
- **"竞争性假设检验"策略**：同时构造两个（或多个）竞争性过程模型，让协议数据在它们之间做出裁决。
- **"完形展示"策略**：不仅展示分析结果，还展示完整的原始协议和数据，使读者可以独立进行判断。

### L### 材料整合方式
本章的材料呈现具有强烈的"教学"特征——每个方法都先展示"原始协议"，再展示"编码过程"，最后展示"分析结果"。这种"逐步展示"的呈现方式与前几章的"整合论述"形成对比。

---

## L### 六、论辩与阐述方法

### L### 主要论辩策略
1. **"存在性证明"策略**：通过对多个不同任务的成功协议分析，证明"协议分析方法是有效的"不是一个空洞的主张。
2. **"敏感性展示"策略**：心算加法例子特别展示了协议的敏感性——H1与H2预测的数字集合仅有一个共同元素（44），协议数据可以清晰地选择H1。
3. **"收敛性验证"策略**：通过两种不同的语句类型（移动描述vs状态描述）得出相同的表征推论——"The analyses of moves and of states always yielded the same representation."
4. **"弱预测的力量"策略**：在心算加法中，即使弱预测（不预测顺序，只预测数字集合）也有足够的区分力来选择模型。

### L### 辅助阐述方法
- **完整协议转录**：Ohlsson协议的全56段转录——允许读者独立分析。
- **编码对照表**：心算加法的原始协议与编码结果并排呈现。
- **产生式系统轨迹**：用产生式系统的"程序轨迹"格式展示模型预测——可直接与协议编码比对。
- **图示**：Eight Puzzle的邻接关系图（Figure 7-2）直观展示哪些关系被不注意。

---

## L### 七、语言文风（原文摘录+L###）

### L### 总体风格
演示性学术写作——作者以一个熟练工匠的姿态，带领读者"走过"一个个协议分析的实例。语气从前面几章的理论论辩转向"让我展示给你看"的实践演示。

### L### 关键原文摘录
1. "The chances that such a close match with H1 could be produced by chance are less than one in a trillion."——关于H1-H2选择的统计说服力。
2. "A verbalization may be a literal copy of information that is presented or has been memorized previously."——非正式分析中"Read"过程的定义。
3. "The analyses of moves and of states always yielded the same representation, and there were no disagreements between the two encoders."——TOH同构问题分析中的收敛性验证。
4. "The most striking finding about intentions is that subjects define goals in terms of only a few tiles (or one)."——Eight Puzzle分析的关键发现。
5. "Ignoring sequence (the weakest model, H2), it can be predicted that all the verbalized two-digit numbers will belong to the following set."——弱预测方法论的清晰陈述。

### L### 文风特征
- **教学性**：大量的"Let us see how we can..."、"We will employ a sequential decision process..."等引导性表述。
- **数据透明度**：提供完整的原始协议数据，而非仅提供编码结果。
- **"工具箱"意识**：不同方法适用于不同情况——非正式分析用于探索、弱预测用于快速筛选、强预测用于严格检验。
- **数学精确性与非形式洞察的平衡**：既给出"one in a trillion"的概率计算，也不回避"there is no clear indication as to how the inference was arrived at"的不确定性。

---

## L### 八、实体清单（六类，每类≥3+L###）

### L### 人物实体
1. **Stellan Ohlsson (1980)**——其三项系列任务协议在本章被作为非正式分析的范例。
2. **Y. Anzai**——与Simon合作发表河内塔协议分析的编码研究。
3. **John R. Hayes**——与Simon合作开发UNDERSTAND模型，预测被试对TOH同构问题的表征。
4. **David Neves (1977)**——训练被试使用不同策略解决河内塔，为本研究的策略对照分析提供数据。
5. **K. Anders Ericsson (1975b)**——其Eight Puzzle研究提供了本章关于表征推论的核心数据。
6. **John R. Anderson (1976)**——提出STM不是独立存储而是LTM的当前激活部分的替代理论。

### L### 著作/文献实体
1. **Ohlsson (1980)博士论文**——三项系列任务协议的数据来源，包含完整的协议转录和深入的过程模型分析。
2. **Simon & Hayes (1976) "The understanding process: Problem isomorphs"**——UNDERSTAND模型的原始论文，预测TOH同构问题的表征。【校对修正】原标题误写为 "Understanding complex task instructions"，源文件参考文献（L8268-8270）实际标题为 "The understanding process: Problem isomorphs"（Cognitive Psychology, 1976, 8, 165-190）。
3. **Hayes & Simon (1974) "Understanding written problem instructions"**——UNDERSTAND模型的前身。
4. **Ericsson (1975b) "Problem-solving behaviour with the Eight Puzzle IV: Process in terms of sequences of moves"**——Eight Puzzle协议的数据来源。【校对修正】原报告标题误写为 "Protocol analysis and the Eight Puzzle"，源文件参考文献（L6955-6959）实际标题为 "Problem-solving behaviour with the Eight Puzzle IV: Process in terms of sequences of moves"（Reports from the Department of Psychology, No. 448, University of Stockholm, 1975）。
5. **Anzai & Simon (1979) "The theory of learning by doing"**——河内塔协议编码的发表论文。
6. **Simon (1975) "The functional equivalence of problem solving skills"**——河内塔策略的产生式系统理论分析。

### L### 理论/模型实体
1. **非正式分析三层分类（Read/Paraphrase/Inference）**——以最小理论承诺区分协议段的生成过程类型。
2. **弱预测策略（Weak Prediction Strategy）**——预测信息类型但非序列，适合信息不完全口头化的情况。
3. **强预测策略（Strong Prediction Strategy）**——预测唯一或有限的信息序列，适合口头化较完整的情况。
4. **UNDERSTAND模型**——Simon & Hayes (1976)的问题理解模型，预测被试如何将文本指令转化为内部表征。
5. **目标递归策略vs知觉策略**——Simon (1975)对河内塔的两种策略的产生式系统模型。
6. **"and/then"推理标记假设**——话语标记"and"指示前提联结，"then"指示推论引出。

### L### 概念/术语实体
1. **Move Representation vs. Change Representation**——TOH同构问题的两种可能内部表征。
2. **Linear Sequence Representation (1-2-3-...-8)**——Eight Puzzle中被试实际使用的表征。
3. **Weak vs. Strong Predictions**——弱预测=信息类型；强预测=信息序列。
4. **Strategy Signature（策略签名）**——不同策略在协议中留下的可识别痕迹。
5. **Informal Protocol Analysis**——以最小理论承诺进行的探索性协议分析。
6. **Competing Hypothesis Testing**——构造两个（或多个）竞争模型以协议数据裁决。

### L### 实验/研究实体
1. **Ohlsson (1980)的三项系列任务协议分析**——47条信息单元整合为单一线性排序。
2. **心算加法的H1-H2竞争性检验**——H1（左→右累加）完胜H2（右→左累加）。
3. **Ericsson (1975b)的Eight Puzzle表征分析**——从406个协议段中推论出线性序列表征。
4. **Simon & Hayes (1976)的TOH同构问题（Monster Problems）**——"移动"版vs"改变"版对表征的影响。
5. **Neves (1977)的河内塔策略训练研究**——目标递归策略vs知觉策略的协议对照。
6. **心算乘法的过程模型预测与协议匹配**（7.5）——包含策略选择、进位处理和错误模式。

### L### 机构/工具实体
1. **UNDERSTAND Program**——实现Simon & Hayes (1976)模型的计算机程序。
2. **Production System Simulator**——用于生成与协议比对的过程轨迹。
3. **Eight Puzzle (3×3滑动积木)**——Ericsson (1975b)使用的实验材料。
4. **Tower of Hanoi (4-disk version)**——Neves (1977)和Anzai & Simon (1979)使用的实验材料。
5. **Transition Net（转换网络）**——在心算乘法模型中表示过程流程。
6. **Regression Analysis Tools**——用于检验延迟预测的准确性。

---

## L### 九、与前后章关联

### L### 与第六章的关联
第六章提供了协议分析的"方法手册"，第七章提供了"方法演示"——每一个第六章中描述的技术（分段、编码、聚合、模型比对）在第七章都有对应的实例展示。两章共同构成全书的"方法-实例"双子星结构。

### L### 与第五章的关联
第五章的口头化过程模型为第七章的协议分析提供了理论解释——当我们说"and/then"标记指示推理过程时，其理论依据是第五章的"口头化直接反映STM内容结构"假设。

### L### 与第四章的关联
第四章提出的相关性/一致性/记忆三标准和"基于任务分析的编码"方法在第七章的心算加法、Eight Puzzle和TOH同构问题分析中得到了系统实施。

### L### 与第二章的关联
第二章关于"不同指令导致不同效应"的发现——在第七章关于TA指令措辞的讨论中得到回响（附录中的TA指令示例）。

### L### 与全书的关联
第七章以一系列成功的协议分析实例完成了全书的论证闭环——从第一章宣告"口头报告可作为数据"，到第七章展示"口头报告确实被成功用作数据"。全书从一个承诺（"我们能这样做"）开始，以一系列证据（"我们确实这样做了"）结束。

### L### 跨章论证线索
第七章的每一个实例都展示了同一个核心原则：**协议分析的成功依赖于分析者对被分析任务的结构有透彻的理解。** 无论分析多么"非正式"，任务分析始终是协议分析的出发点。这一原则从第一章的Coombs数据加工框架开始，贯穿第四、五、六章，在第七章的实践中得到最终实现。
