# 第2章 分析报告：时间图像——面向时间数据的可视化表征（Images of time）

**作者**：Christian Tominski, Wolfgang Aigner, Silvia Miksch, Heidrun Schumann
**所属部分**：Part 1 历史视角（Historical perspectives）
**原书页码**：232-?

---

## 一、章节概述

本章系统阐述了面向时间数据（time-oriented data）的可视化表征的理论基础、设计原则和实现技术。作者团队来自信息可视化与视觉分析领域，提出了从时间概念化（conceptualizing time）到数据映射（mapping time and data）再到具体技术实现的完整框架。本章的核心创新是TimeViz Browser——一个交互式的可视化技术分类浏览器，收录了超过100种面向时间数据的可视化技术。

本章与第1章形成"历史-当代"的完整叙事弧：第1章追溯18世纪时间可视化的起源，本章将叙事延续到计算机时代的动态、交互式可视化。

---

## 二、核心论点

1. **时间的多面性**：时间并非简单的线性序列，而是具有时间原语（instants vs. intervals）、时间排列（linear vs. cyclic）等多重面向，可视化设计必须充分考虑这些特性。

2. **静态与动态表征的互补性**：静态表征（时间映射到空间）适合概览和趋势检测；动态表征（时间映射到物理时间）适合传达总体动态。两者各有优劣，应配合使用。

3. **可视化流水线模型**：Haber和McNabb（1990）的filtering-mapping-rendering三阶段模型是理解可视化设计过程的核心框架，其中mapping阶段决定可视化的表达力和有效性。

4. **视觉变量的数据适应性**：Bertin（1983）定义的七种视觉变量（位置、尺寸、值、纹理、颜色、方向、形状）对不同尺度数据（定量/定序/定类）具有不同适配度。

---

## 三、关键概念

| 概念 | 英文 | 释义 |
|------|------|------|
| 时间原语 | Time primitives | 时刻（instant）与时段（interval） |
| 时间排列 | Time arrangement | 线性（linear）与循环（cyclic）两种时间隐喻 |
| 参照框架 | Frame of reference | 抽象数据 vs. 空间数据 |
| 视觉变量 | Visual variables | Bertin定义的编码数据的七种视觉属性 |
| 地平线图 | Horizon graphs | 通过切片、分层和双色调伪彩色压缩显示多变量时间序列 |
| 火花线 | Sparklines | 可嵌入文本的词级微型图表 |
| 循环图 | Cycle plots | 同时展示季节性成分和趋势成分 |
| 规划线 | PlanningLines | 用字形表示具有时间不确定性的区间数据 |
| 时空轨迹墙 | Trajectory Wall | 在地图上方以3D带状堆叠显示时空运动轨迹 |
| 视觉分析 | Visual Analytics | 整合可视化、交互和分析方法的跨学科研究领域 |

---

## 四、方法论分析

本章采用系统性的概念分析法（conceptual analysis）与设计研究（design research）相结合的方法：

1. **概念分解**：将"时间"这一复杂现象分解为可操作的设计维度（原语、排列、尺度、视点、粒度等）。

2. **分类框架构建**：基于对100+可视化技术的分析，建立多维分类体系（数据面：参照框架×变量数；时间面：排列×原语；可视化面：映射×维度）。

3. **设计工具开发**：将分类框架实现为TimeViz Browser这一可交互的实用工具，体现了"研究即工具"的设计科学理念。

4. **历史谱系法**：将当代技术置于从10世纪行星运动图到Playfair统计图的历史脉络中。

---

## 五、案例研究/技术示例

本章展示了多种当代可视化技术：

1. **Horizon Graphs（Reijner 2008）**：通过切片分层和双色调伪彩色处理，在有限空间内高效展示大量时间序列变量。

2. **Cycle Plots（Cleveland 1993）**：将循环模式（如星期几）分离为独立的面板行，使趋势和季节效应同时可见。

3. **Enhanced Interactive Spiral（Tominski & Schumann 2008）**：沿螺旋线布局时间序列数据，通过交互式调整周期长度探测循环模式。

4. **PlanningLines（Aigner et al. 2005）**：用特殊字形（由两端帽和双条组成）表示最早/最晚开始、最早/最晚结束、最小/最大持续时间。

5. **Trajectory Wall（Tominski et al. 2012）**：将时空轨迹以3D带状堆叠在地图上方，配合循环时间径向显示进行交互式空间查询。

6. **Gapminder/Trendalyzer**：Hans Rosling的动画散点图，以VCR式控件操作时间轴。

---

## 六、理论贡献

1. **建立时间可视化的系统分类学**：将时间的多面性（6个设计维度）与数据的特性（3个关键面）整合为一个可操作的概念框架，为信息设计师提供了"选择正确可视化技术"的决策依据。

2. **桥接感知理论与可视化实践**：将Bertin的视觉变量理论和Mackinlay的排序框架应用于时间数据领域，明确了不同数据类型对应的最佳视觉编码方式。

3. **提出"可视化调查"（visual survey）的概念**：TimeViz Browser以视觉化的方式组织可视化技术本身——这是一种"元可视化"的方法论创新。

4. **为视觉分析（Visual Analytics）奠定概念基础**：明确指出了整合自动化分析与人类感知的必要性。

---

## 七、实践启示

1. **数据与问题分析先行**：任何可视化设计项目的第一步都应是识别数据的性质（时刻vs.时段、线性vs.循环、抽象vs.空间），然后选择或设计匹配的可视化形式。

2. **动画需要交互控制**：动态可视化虽然直观，但可能导致信息过载——必须配备慢放、快进、回放等交互控件。

3. **静态与动态互补**：静态视图提供概览（"一帧之中"），动态视图传达过程——最佳实践是两者结合。

4. **工具赋能**：TimeViz Browser展示了如何通过工具降低信息设计师在技术选型时的认知负担。

---

## 八、批判性评述

**优势**：
- 概念框架清晰、系统性强
- 理论与实践紧密结合，有工具落地
- 历史视野与现代技术并重

**局限**：
- 对可视化技术的评估主要依赖设计合理性而非严格的用户实验数据
- TimeViz Browser的分类维度虽全面，但未涵盖美学和情感因素
- 对非西方文化中的时间概念（如循环时间观在东亚文化中的主导地位）着墨甚少

---

## 九、跨章节关联

- **与第1章（Boyd Davis）**的直接对话：第1章提供历史谱系，本章提供当代发展和分类框架
- **与第3章（Playfair）**的技术继承：Playfair发明的折线图、柱状图、饼图至今仍是时间可视化最常用的基本形式
- **与第14章（Weber, 交互式信息图形）**的衔接：本章聚焦于时间维度，第14章更广泛地讨论交互性
- **与第21章（Tversky, 图表）**的认知基础：Tversky讨论图表认知的心理学基础，为本章的技术分类提供认知科学支撑
- **与第22章（Lowe, 动画图表）**的深化：Lowe深入讨论动画在教育材料中的应用，是本章动态表征讨论的延伸
- **与第28章（Dyson, 研究方法）**的方法论呼应：Dyson讨论信息设计的研究方法，本章的TimeViz Browser可视为一种研究工具的实现

---

## L### 参考文献（精选）

L001 Bertin, J. (1983). *Semiology of graphics*. University of Wisconsin Press.
L002 Aigner, W., Miksch, S., Schumann, H., & Tominski, C. (2011). *Visualization of time-oriented data*. Springer.
L003 Tufte, E.R. (1983). *The visual display of quantitative information*. Graphics Press.
L004 Cleveland, W.S. (1993). *Visualizing data*. Hobart Press.
L005 Mackinlay, J. (1986). 'Automating the design of graphical presentations.' *ACM Transactions on Graphics*, 5(2), 110–141.
L006 Haber, R.B. & McNabb, D.A. (1990). 'Visualization idioms.' In *Visualization in scientific computing*, 74–93. IEEE.
L007 Reijner, H. (2008). 'The development of the horizon graph.' *VisWeek Workshop*.
L008 Tominski, C. & Schumann, H. (2008). 'Enhanced interactive spiral display.' *SIGRAD 2008*.
L009 Playfair, W. (1786/1801). *The commercial and political atlas*. London.
L010 Rosenberg, D. & Grafton, A. (2010). *Cartographies of time*. Princeton Architectural Press.
