# Ch05 分析报告：《The Delta Method: A Way to Introduce Usability》

## 一、章节定位与功能（行号范围 L1721-L2022）

本章是第二主题簇"FOCUS ON THE DEVELOPMENT PROCESS"（L472-L474）的第二篇，作者 Martin Rantzer（Ericsson Infocom Consultants AB，L1723-L1725）。功能：介绍**Delta 方法**——一种把既有可用性工具与实践组装为可用性流程、补充传统系统开发早期阶段的框架，并展示它如何在客户组织（Telia NM）中通过试点项目落地（L1729-L1733）。它是全书"如何把可用性引入企业"的北欧视角代表。

## 二、结构分析

- Executive Summary（L1727-L1733）
- Background（L1735-L1743）：Ericsson Infocom 与林雪平大学联合开发背景
- The Development of the Delta Method（L1745-L1758）：三阶段开发
- The Method Purpose（L1760-L1783）：用户界面扩展定义、客户/用户区分
- The Structure of the Design Group（L1785-L1789）
- The Role of Delta in the System Design Process（L1791-L1820）：集成与 Telia NM 案例
- The Delta Method—In Theory and Practice（L1822-L1985）：六项活动理论与实务对照
- Summary（L1987-L2003）
- Acknowledgments（L2005-L2011）
- References（L2013-L2021）

## 三、内容分析

**开发背景**：Ericsson Infocom 是爱立信旗下咨询公司，约 500 人（L1737）。1992 年开发启动时公司内无人有人因/可用性经验（L1741）；由一名资深技术传播者发起——他受够了交付前被叫去"用文档补救可用性问题"（L1741）。开发由 Ericsson Infocom 与林雪平大学联合进行，获瑞典国家工业与技术发展委员会（NUTEK）支持，属 ITYP 计划（L1739）。

**三阶段开发**（L1747）：方法构思（method inception）→ 现场研究（field studies，商业试点项目）→ 基于经验的修订。开发者"以身作则"（live as we preach）：方法本身基于未来用户（系统开发者和技术传播者）的经验与需求开发（L1747）。

**方法目的**：
- **扩展用户界面**：用户界面 = 服务（functions）+ 图形呈现 + 使能信息（user documentation）三部分（L1766-L1774）；与 Lewis & Reiman 的"extended user interface"类似（L1774）。
- **区分客户与用户**：客户想要稳健、廉价、易维护；用户想要简单、快、支撑任务（L1781）。

**设计组结构**：系统设计师 + 技术传播者，二者均专精界面设计；可配语言学/心理学/人因/认知科学专家（L1787）。

**与系统设计流程的关系**：Delta 是补充方法而非完整方法，支撑需求分析与初始设计阶段（L1793）。集成须贴合组织既有文档与项目管理结构（L1802-L1804）。

**Telia NM 案例**：Telia AB 是瑞典最大最老的电话公司（L1808）；Telia NM 中心采购式开发（L1810）。Delta 被选为其质量系统中的"可用性指令"方法（L1812-L1814）；"Directions for Use"需并行开发（L1816-L1818）；关键文件是需求规范——"把可用性变成与功能需求同等的需求"（L1820）。

**六项活动（理论与实务对照）**：
1. **系统定义（System Definition）**：高层抽象分析，三类用户需求草稿；三阶段：Preparations/System Definition/System Description（L1835-L1843）。实务：两天异地会议，8 人组，产出 Information Matrix（L1847-L1849）。
2. **用户与任务分析**：问卷+访谈；用户分析（L1855-L1859）：问卷发 51 份回收 35 份（L1865）；任务分析（L1869-L1880）：action graph（行动图）+ playback 验证。实务：12 次访谈、动作图合并为"super graphs"（L1884-L1888）。
3. **设计准备（Design Preparations）**：场景 + 用户画像 + 设计建议（L1894-L1896）。实务中"未产出详细场景被证明是最大失误"（L1902）。
4. **概念设计（Conceptual Design）**：服务结构抽象设计，概念模型/隐喻/使能信息三问（L1918-L1928）。实务：两次设计工作坊（第二次更好，用 UED 记号+亲和图，L1935-L1937）。
5. **制定可用性目标（Formulating Usability Goals）**：基于现状/竞品/场景的测试用例+可用性规范（L1941-L1943）。实务：12 个可用性目标，用户参与迭代改进（L1951）。
6. **原型设计（Prototype Design）**：纸原型→计算机原型迭代（L1955-L1959）。实务：纸原型需内部试测，"远未准备好"（L1965）；计算机原型引入"会说话的活书"（talking book）角色（L1969）。
7. **可用性测试（Usability Tests）**：按测试用例、用户代表参与（L1973-L1975）。实务：纸原型 4 名高级用户、计算机原型 6 名用户（L1979-L1983）。

**总结**（L1987-L2003）：大学-工业联合是知识转移良方；inception-pilot-revision 开发法有效；方法"看起来好"很重要（L1995）；必须紧贴既有文档/项目管理制度（L1997）；可用性需求须与功能需求同等方式描述、测试、执行（L1999）；客户代表参与必要，非典型用户常能看到超出现状的方案（L2001）；未来应更重视场景开发（L2003）。

## 四、逻辑梳理

**发起动因（交付前补救可用性）→ 大学-工业联合三阶段开发（构思→试点→修订）→ 扩展用户界面观 → 六活动流程（定义→分析→准备→概念→目标→原型→测试）→ Telia NM 落地（质量系统+需求规范）→ 经验总结（制度化、需求同等化、场景）**。

## 五、材料使用方式

- **一手材料**：试点项目（Telia NM 本地无人交换机的监控管理软件，L1824）过程中的问卷、访谈、动作图、原型测试记录；研究者作为系统开发者嵌入团队的质性观察（L1751）。
- **文档材料**：The Delta Method Handbook（L1758、L2015）、Carlshamre 的博士论文《A Collaborative Approach to Usability Engineering》（L1758、L2011）、Telia 的 GMMS 界面设计指南（L2021）。
- **对照结构**："In Theory"与"In Real Life"逐活动对照，是全书独有的编排手法（L1833-L1985）。

## 六、论辩与阐述方法

- **实践检验理论**：每个活动都同时给出方法与实际经历，"theory and practice"对照使方法论陈述具有证伪性。
- **历史叙述**：开发三阶段以叙事展开（L1745-L1758）。
- **边界自陈**：坦承"试错"细节——首次工作坊失败（L1935）、动作图未产出（L1902）、纸原型不合格（L1965）。

## 七、语言文风摘录（附行号）

- "In an effort to live as we preach, the Delta Method was developed based on the experiences and needs of its future users."（L1747）
- "The only way to introduce a new concept in the development is to make usability a requirement with the same status as functional requirements."（L1820）
- "It might seem silly, but it is very important to have a method that looks good."（L1995）
- "Optional requirements and usability activities will be overlooked when the deadlines of the project are creeping closer."（L1999）

## 八、实体清单（六类，附行号证据）

### 人物（Person）
| 编号 | 名称 | 身份 | 行号 |
|---|---|---|---|
| P01 | Martin Rantzer | Ericsson 系统开发者、Delta 方法开发与集成负责人 | L1723、L372 |
| P02 | Pär Carlshamre | 林雪平大学研究者、博士论文作者 | L1758、L2011 |
| P03 | Cecilia Bretzner、Ulf Idesten、Anders Möller、Göran Sandström | Ericsson Infocom Delta 组成员 | L2009 |
| P04 | Jonas Löwgren、Karin Mårdsjö | 林雪平大学研究者 | L2009 |

### 著作/作品（Artifact）
| 编号 | 名称 | 说明 | 行号 |
|---|---|---|---|
| A01 | The Delta Method Handbook | 方法手册 | L1758、L2015 |
| A02 | "Delta within Telia NM: Directions for Use" | 集成使用指令 | L1816 |
| A03 | Information Matrix | 系统定义产出矩阵 | L1849 |
| A04 | Action Graph / Super Graphs | 任务分析图 | L1875-L1888 |
| A05 | Usability Instruction | Telia 质量系统内的可用性指令 | L1812-L1814 |

### 概念（Concept）
| 编号 | 名称 | 含义 | 行号 |
|---|---|---|---|
| C01 | Delta Method | 可用性工程框架 | L1729 |
| C02 | Extended user interface | 扩展用户界面（服务+呈现+使能信息） | L1766-L1774 |
| C03 | Customer vs. user | 客户与用户的区分 | L1781 |
| C04 | Action graph | 行动图 | L1875 |
| C05 | Scenario | 场景 | L1894、L1906-L1914 |
| C06 | Usability goals + test specification | 可用性目标与测试规范 | L1941-L1943 |

### 机构（Institution）
| 编号 | 名称 | 行号 |
|---|---|---|
| I01 | Ericsson Infocom Consultants AB | L1737 |
| I02 | Linköping University | L1739 |
| I03 | NUTEK（瑞典国家工业与技术发展委员会） | L1739 |
| I04 | Telia AB / Telia NM | L1808-L1810 |
| I05 | Telia Research（分包商） | L1824 |

### 地点（Place）
| 编号 | 名称 | 行号 |
|---|---|---|
| L01 | 瑞典（Ericsson 四个办公地） | L1737 |
| L02 | 林雪平（Linköping） | L1739 |

### 事件（Event）
| 编号 | 名称 | 行号 |
|---|---|---|
| E01 | Delta 方法开发启动（1992） | L1741 |
| E02 | 试点项目（Telia NM 交换机监控系统） | L1824 |
| E03 | 系统定义异地两天会议（8 人） | L1847 |
| E04 | 12 次任务分析访谈 | L1884 |

## 九、与前后章关联

本章与 Ch4 都讨论"把用户输入整合进开发流程"，但 Ch4 是在既有用户中心流程中嵌入多种方法，本章是把可用性作为**独立可销售/可集成的方法产品**引入组织。与 Ch16（参与式设计）共享北欧背景（斯堪的纳维亚），但与参与式设计的"工人优先"政治承诺不同，Delta 更多是工程-咨询导向。其"可用性需求必须与功能需求同等"的主张与 Ch13 的"需求文档"生成逻辑呼应。
