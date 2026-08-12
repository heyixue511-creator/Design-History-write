# Ch04 分析报告：《Changing the Rules: A Pragmatic Approach to Product Development》

## 一、章节定位与功能（行号范围 L1298-L1720）

本章是第二个主题簇"FOCUS ON THE DEVELOPMENT PROCESS / DESIGN PROCESS"（L472-L476）的首篇，作者为 Dennis R. Wixon、Christine M. Pietras、Paul K. Huntwork、Douglas W. Muzzey（Digital Equipment Corporation，L1302-L1310）。功能：示范**田野研究、量化调查、全面质量管理、原型测试如何整合进一个完整的用户中心设计流程**（TeamLinks for Macintosh 产品），并系统总结"如何改变规则"的组织经验。它是编者（Wixon 本人）的直接作品，是全书中"流程整合"论述最完整的章节。

## 二、结构分析

- Executive Summary（L1312-L1314）
- Background（L1316-L1398）：产品概述、设计过程、跨职能团队环境
- What We Did（L1419-L1488）：找到客户需求/据此设计/与客户细化
- What We Learned（L1490-L1636）：推翻旧假设的四大教训 + 惊喜点 + 原型细化
- Response from Customers（L1638-L1651）
- Reflections（L1653-L1671）：六条方法论经验
- Acknowledgments（L1673-L1679）
- References（L1681-L1719）

## 三、内容分析

**产品与背景**：TeamLinks 让 Windows PC 与 Macintosh 集成进企业级网络，基于 Digital 的 ALL-IN-1 IOS、邮件、文件共享、工作流等网络服务（L1322）。TeamLinks for Windows 于 1992 年春夏推出后，需立即为 Macintosh 提供核心服务（邮件、ad-hoc 工作流、归档），时间窗口 6-9 个月（L1324）。

**设计过程**：五步通用流程（产品概念定义、产品能力决策、用户界面设计、实现、测试）+ 用户全程参与 + 迭代（L1338-L1350）。Table 4.1 给出每步的具体方法：Contextual Inquiry/基于工作的访谈、客户调查+Vector Comparative Analysis、Contextual Inquiry/制品走查、UI 原型测试、生产工作测试（L1357）。

**三原则（L1367-L1373）**：找到客户需要什么；据此设计；与客户一起细化。

**方法库**：
- **田野研究**：直接接触用户的早期设计价值（Gould et al. 1991; Grudin 1991）（L1395）；
- **量化研究**：决策阶段的系统客观依据（Gilb 1988）（L1397）；
- **植根设计（Grounded Design）**：设计植根于客户数据而非猜测（L1399）；
- **需求拉动（Demand Pull）**、**客户驱动设计**、**设计隐喻**（L1403-L1409）；
- **迭代需求与原型**（L1413-L1417）。

**执行细节**：
- **跨职能团队**：产品经理、工程师（含兄弟产品）、客户经理、支持人员、客户人员、市场/人因/图形/出版/竞品分析专家（L1425）；
- **客户伙伴**：美国政府承包商、制造业、制药业、银行业四个重度使用 PC 的行业（L1430）；
- **Contextual Inquiry 训练**：三原则 context/partnership/focus（Holtzblatt & Jones 1990）（L1434）；
- **客户调查**：需求层级问卷、100 分分配法（L1436-L1448）；
- **客户日（Customer Day）**、**竞争基准测试**、**交叉验证**（L1450-L1454）；
- **VCA**：加权平均滚动得分的向量比较工具，Digital 为替代 QFD 而开发（L1456）。

**四大教训（推翻旧假设）**：
1. 不建整合信息管理器，ALL-IN-1 文件柜应作为 Mac 文件系统的扩展（L1503-L1512）；
2. 不做大而整合的应用，不建新 X.400 邮件客户端，改用既有组件+工作流（L1516-L1531）；
3. 时间管理必须做——两位伙伴将其列为最高优先级（L1535-L1541）；
4. 不能把 Windows 版移植到 Mac——"Build a real Mac product"（L1545-L1557）。

**惊喜点（Delighters）**：按钮栏（Button Bar）出乎意料地受喜爱（L1563）；工作流自动化是新兴机会（L1565-L1569）。

**原型细化**：四轮原型（Table 4.2，L1488）：UI 外观→UI+有限功能→可用工作流+基本邮件→完整功能。以邮件隐喻重新设计路由窗口（L1588-L1603）、术语审查（Table 4.4：Template/Original/Carbon Copy/Routing Copy，L1616）、跨组件一致性与统一图形（L1618-L1627）、文件柜扩展设计（L1629-L1636）。

**客户反馈**：政府承包商、制造业、制药、政府机构的原话好评（L1642-L1651）。

**六条方法论经验**（L1655-L1667）：
1. 组织/流程因素决定方法成败，管理必须是完整支持者；
2. 方法省钱省时——"若没有此流程，我们会花 18 个月和 200 万美元做出无竞争力的产品"（L1659）；
3. 方法互补，互相提供支撑性发现；
4. 开放式方法应早、聚焦问题方法应后；
5. 单一协调人是关键（Pietras）；
6. 无法单独核算可用性工作的成本-收益，因为它是流程的组成部分。

## 四、逻辑梳理

**高层目标（满足市场/交付可用方案/适应环境约束）→ 设计伙伴关系 + 五步迭代流程 → 田野与量化并用的需求发现（VCA 决策）→ 田野数据推翻四大初始假设 → 以原型迭代确认细化（邮件隐喻、术语、一致性）→ 客户验收 → 提炼六条方法论经验**。

## 五、材料使用方式

- **一手材料**：客户伙伴关系中的访谈、调查问卷、VCA 数据、四轮原型测试记录、制品走查（客户表单/文档）、客户反馈原话。
- **表格化呈现**：Table 4.1（方法映射）、4.2（原型轮次）、4.3（原设计与修订设计对比）、4.4（术语对照）。
- **参考文献**：设计流程（Good 1985；Ohno 1988；Sanders 1992）、隐喻（Lakoff & Johnson 1980；Halasz & Moran 1982；Pepper 1966）、软件工程史（Naur & Randall 1969；Womack & Roos 1990）、Contextual Inquiry（Holtzblatt & Jones 1990；Wixon & Jones 1996）。

## 六、论辩与阐述方法

- **对比论证**：1969 年"软件危机"的层级化软件工程模型 vs. 跨职能团队（Deming 管理法）的新产品开发（L1363）；旧式组织=文档传递+延误，跨职能=共享愿景+快速（L1377-L1386）；原设计 vs. 修订设计（Table 4.3）。
- **实证决策论证**：每次设计转向都以客户原话+VCA 数据为依据（如 L1523-L1527、L1539）。
- **成效论证**：以交付时间、资源、"delighter"、客户原话等多元证据收束。

## 七、语言文风摘录（附行号）

- "Find out what the customer needs. / Design the product based on what you learn. / Refine your product with your customers."（L1369-L1373）
- "Without this process we would have spent 18 months and 2 million dollars producing a noncompetitive product."（L1659）
- "Open-ended methods should come early; methods oriented around specific questions should come later."（L1663）
- "Document management should look and work like the Mac."（L1507）

## 八、实体清单（六类，附行号证据）

### 人物（Person）
| 编号 | 名称 | 身份 | 行号 |
|---|---|---|---|
| P01 | Dennis R. Wixon | Digital 可用性项目经理 | L1302、L364 |
| P02 | Christine M. Pietras | 人因顾问、UI 协调人 | L1304、L366 |
| P03 | Paul K. Huntwork | Digital 咨询工程师 | L1306、L368 |
| P04 | Douglas W. Muzzey | 开发经理（TeamLinks 赞助人） | L1308、L370 |

### 著作/作品（Artifact）
| 编号 | 名称 | 说明 | 行号 |
|---|---|---|---|
| A01 | TeamLinks for Macintosh | 目标产品（邮件/工作流/归档/会议） | L1314、L1322 |
| A02 | ALL-IN-1 IOS | Digital 综合办公系统 | L1322 |
| A03 | DEC MAILworks for Macintosh | 既有 X.400 邮件客户端 | L1527-L1529 |
| A04 | VCA（Vector Comparative Analysis） | 向量比较工具 | L1456 |
| A05 | TeamLinks Routing | 工作流路由产品 | L1569 |
| A06 | Table 4.4 术语表（Template/Original/Carbon Copy/Routing Copy） | 修订术语 | L1616 |

### 概念（Concept）
| 编号 | 名称 | 含义 | 行号 |
|---|---|---|---|
| C01 | Design partnership | 设计伙伴关系 | L1336 |
| C02 | Cross-functional team | 跨职能团队 | L1363、L1425 |
| C03 | Grounded design | 植根设计 | L1399 |
| C04 | Demand pull | 需求拉动 | L1405 |
| C05 | Design metaphor | 设计隐喻（桌面隐喻） | L1409 |
| C06 | Delighters | 惊喜点 | L1559 |
| C07 | Artifact walkthrough | 制品走查 | L1485 |
| C08 | Software crisis | 软件危机（1969 与当代） | L1363-L1365 |

### 机构（Institution）
| 编号 | 名称 | 行号 |
|---|---|---|
| I01 | Digital Equipment Corporation | L1310 |
| I02 | Apple（Apple Developers Conference、AOCE） | L1507、L1636 |

### 地点（Place）
| 编号 | 名称 | 行号 |
|---|---|---|
| L01 | 客户伙伴所在地（四行业） | L1430 |

### 事件（Event）
| 编号 | 名称 | 行号 |
|---|---|---|
| E01 | TeamLinks for Macintosh 开发（1992 末-1993 初） | L1314 |
| E02 | 四轮原型周期 | L1483-L1488 |
| E03 | 客户日 | L1450 |
| E04 | Apple Developers Conference | L1507 |

## 九、与前后章关联

本章直接呼应 Ch5（Delta 方法也强调"把可用性整合进既有流程"）；与 Ch7（组织考虑）共同构成"组织/流程"轴线；其 Contextual Inquiry 用法被 Ch11/Ch12/Ch13 作为参照。VCA 的量化决策路径与 Ch2 的"质性+量化"组合主张互补。本文原载《Digital Technical Journal》1993 年秋季刊（L1679），是全书最具"流程整合"示范性的章节。
