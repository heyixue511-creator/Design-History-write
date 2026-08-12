# Ch17 分析报告：《Contextual Design: Principles and Practice》

## 一、章节定位与功能（行号范围 L4771-L5133）

本章是框架三章之三，也是全书压轴章，作者 Karen Holtzblatt、Hugh Beyer（InContext Enterprises, Inc.，L4775-L4779）。功能：系统阐述**情境设计（Contextual Design）**——从项目设置、田野访谈、数据解释、合并、再设计、用户环境设计到纸原型迭代的"结构化路线图"（L4785、L592），并揭示每一部分背后的组织与人际设计动因（L4787）。

## 二、结构分析

- Introduction（L4781-L4787）
- Background of Contextual Design（L4789-L4804）：历史与演化
- Creating the Project（L4806-L4832）：定义问题、成员、过程
- Understanding the Customer（L4834-L4965）：情境查询、工作模型（context/physical/flow/sequence/artifact）
- Consolidation Across Users（L4967-L5004）：亲和图、工作模型合并、设计室
- Systemic Design（L5006-L5058）：愿景、再设计脚本、分离对话、用户环境设计、纸原型迭代
- Customer-Centered Design in the Organization（L5062-L5088）
- Notes（L5090-L5094）
- References（L5096-L5132）

## 三、内容分析

**背景与演化**：情境设计源于 John Whiteside 向他在 Digital 的可用性团队提出的挑战：开发能带来"产品根本改变"而非小迭代的技术（L4791）。Holtzblatt 回应：根本修正只能来自对客户工作更深入的理解（L4793）。情境查询综合了民族志（理解工作实践）、心理学（缩短研究长过程、管理访谈人际动态）、系统工程（在快速交付约束下看设计含义）；与 Sandra Jones 协作、在 Digital 设计团队中迭代（L4793）。**亲和图**借自日本质量管理"七工具"（Brassard 1989），在 Lou Cohen 质量组中引入（L4793）。CI 首次在 CHI 教程公开命名（Holtzblatt、Jones、Steve Knox，John Bennet 与 Dennis Wixon 支持）（L4795）。Beyer 引入图形化形式主义，发展出**工作模型**与**合并**；因团队卡在 UI 细节，发展出**用户环境（User Environment）形式主义**；纸 mock-up 与对象模型支撑实现过渡（L4797）。

**当前结构**（L4799）：情境查询（收集数据）→ 解释会议+工作建模（单访谈理解）→ 亲和图+工作模型合并（全客户范围与共同模式）→ 再设计（改进工作实践）→ 用户环境设计（从用户视角定系统结构、驱动对象建模）→ 纸 mock-up（与用户测试结构与 UI）。

**创建项目**（L4806-L4832）：定义问题——项目常以过窄陈述开始，须"从原问题陈述向后工作"识别受影响的全部工作实践与相关人员（L4810-L4814）；定义成员——借鉴 TQM（Deming 1982; Ishikawa 1985）的跨职能团队，把市场、可用性、UI 设计、测试、客户放上桌（L4816-L4820）；团队至少一半应是设计者（L4822）；8-12 人以上难管理，须向组织沟通（L4824）；定义过程——清晰过程让团队做真实协作设计，而不是彼此争论流程（L4826-L4830）。

**理解客户**（L4834-L4965）：
- 情境查询：把数据带进工程过程；"客户本身难以说出他们做什么"——workaround 被发明后即被遗忘，日常细节成为第二本能而不可见（L4836）；CI 派个人设计师观察人们工作，交错观察、讨论与重构过去事件（L4840）。
- **五种工作模型**：情境模型（外部影响、文化，驱动"客户愿接受哪些变化"，L4874-L4877）、物理模型（环境如何影响工作、揭示约束与工作策略，L4881-L4886）、流模型（职责/沟通/协调，识别用户角色与通信路径，L4888-L4890）、序列模型（行动序列、意图与触发器，驱动测试用例，L4892-L4932）、制品模型（制品结构/使用/意图，指引新制品结构，L4934-L4963）。

**跨用户合并**（L4967-L5004）：亲和图（每访谈 50-100 笔记，15-20 访谈 1000-2000 笔记；按"亲和性"逐条上墙；禁止"可用性""质量"等熟悉类别，类别名表达用户意图；走墙+贴想法，识别"洞"（数据弱处），L4971-L4977）；工作模型合并（跨客户合成共同结构、保留关键变体；流模型合并示范：识别角色→命名角色→汇总职责→转译通信线；多数团队 10-15 个模型后不再看到新变体，L4979-L4991）；设计室（数据贴墙共享，团队持续返回客户数据；墙上呈现 vs 在线的区别，L4996-L5004）。

**系统设计**（L5006-L5058）：愿景化（跨合并模型头脑风暴替代方案，Pugh 矩阵比较合并最佳部分，L5010）；再设计脚本（角色-步骤-物理/技术变化-概念，统一五种视角展示新工作实践；每步要么被支撑、要么意图被新方式满足、要么因高层意图改变而过时，L5014-L5020）；分离对话（"工作现在如何"vs"工作未来如何"vs"系统结构"三种对话用不同墙区域/模型分开，避免 Joe/Sue 争论式混淆，L5024-L5032）；用户环境设计（系统结构蓝图：地点、功能、工作对象、地点间流动；独立于 UI 与实现；驱动对象模型与 UI 结构；L5036-L5048）；纸原型迭代（先测结构，粗糙度让用户关注结构与功能；迭代让团队保持与客户联系、保持创意，L5050-L5058）。

**组织中的客户中心设计**（L5062-L5088）：情境设计可支撑参与式设计项目（五步：跨职能+客户团队→CI 收集→合并+亲和→头脑风暴再设计→UE 设计+mock-up 测试）（L5066-L5076）；成功将导致组织变革（CACM 1995）；客户访问安排难、营销/工程角色未定、需按组织期望产出文档、需培训新人（L5078-L5088）。

**贯穿原则**（L5060）：客户数据是设计的唯一可靠基础；以具体模型支撑系统思考与干净的设计对话；支持面对面的团队设计并与宿主组织共存。

## 四、逻辑梳理

**Whiteside 挑战（根本改变）→ 情境查询（民族志+心理学+工程）→ 亲和图+工作模型解决"数据太多" → 用户环境解决"系统结构" → 纸原型迭代解决"实现过渡" → 制度化于组织（支撑参与式设计、培训、文档适配）**。逻辑核心：一个为解决产品根本改变而演化的、以客户数据为唯一基石的端到端流程。

## 五、材料使用方式

- **方法自述**：以九年的团队教练经验为证据基础（L4785）。
- **图示**：图 17.1（流程）、17.2（情境模型）、17.3（物理模型）、17.4（流模型）、17.5（序列模型，含"U1 移到更大磁盘"实例）、17.6（制品模型）、17.8（再设计脚本）、用户环境设计表（L5040）。
- **对话反例**：Joe/Sue 争论作为"对话混淆"的教学案例（L5028-L5030）。
- **参考文献**：TQM（Deming 1982; Ishikawa 1985）、亲和图（Brassard 1989）、Pugh（Pugh 1991）、工作建模（Carter 1991）、mock-up（Ehn & Kyng 1991; Kyng 1988）、PICTIVE（Muller 1991）、情境设计相关（Holtzblatt & Jones 1993；Holtzblatt 1994；Beyer 1994）、CACM 特刊（L5098-L5102）。

## 六、论辩与阐述方法

- **演化叙事**：以"每次扩展都由团队需求驱动"的方式叙述方法史（L4797-L4799）。
- **教学式示例**：序列模型、再设计脚本、用户环境设计均以具体实例呈现。
- **反例论证**：Joe/Sue 对话展示"不分离对话"的代价（L5028-L5030）。
- **原则归纳**：结尾以三大原则收束（L5060）。

## 七、语言文风摘录（附行号）

- "a structured, step-by-step roadmap to guide a team from initial project set-up and field interviews through design and the transition to implementation."（L4785）
- "Very little in Contextual Design is totally new. We have adopted and adapted processes developed by others."（L4799）
- "The detail of everyday work becomes second nature and invisible. Customers do not reflect on their work."（L4836）
- "customer data is the only sound basis for design"（L5060）
- "A floor plan allows the architect to see all the parts of a house and how they relate to each other."（L5036）

## 八、实体清单（六类，附行号证据）

### 人物（Person）
| 编号 | 名称 | 身份 | 行号 |
|---|---|---|---|
| P01 | Karen Holtzblatt | 情境设计开发者之一、InContext 联合创始人 | L4775、L416 |
| P02 | Hugh Beyer | 情境设计开发者之一、InContext 联合创始人 | L4777、L420 |
| P03 | John Whiteside | Digital 可用性团队、挑战发起者 | L4791 |
| P04 | Sandra Jones | CI 协作开发者 | L4793 |
| P05 | Steve Knox、John Bennet、Dennis Wixon | CHI 教程支持者 | L4795 |
| P06 | Lou Cohen | Digital 质量组、亲和图引入 | L4793 |

### 著作/作品（Artifact）
| 编号 | 名称 | 说明 | 行号 |
|---|---|---|---|
| A01 | 五种工作模型（context/physical/flow/sequence/artifact） | 工作表示 | L4874-L4963 |
| A02 | 亲和图 | 跨客户问题组织 | L4971 |
| A03 | 合并工作模型 | 市场级工作表示 | L4979 |
| A04 | 再设计脚本 | 图 17.8 | L5018 |
| A05 | 用户环境设计 | 系统结构蓝图 | L5036-L5048 |
| A06 | 纸原型/纸 mock-up | 迭代测试 | L5050-L5058 |

### 概念（Concept）
| 编号 | 名称 | 含义 | 行号 |
|---|---|---|---|
| C01 | Contextual Design | 情境设计（端到端流程） | L4785 |
| C02 | Contextual Inquiry | 情境查询（收集方法） | L4793 |
| C03 | Interpretation session | 解释会议 | L4799、L4973 |
| C04 | Affinity diagram | 亲和图（日本七工具） | L4793、L4971 |
| C05 | Work model consolidation | 工作模型合并 | L4979 |
| C06 | Design room | 设计室 | L4996 |
| C07 | Systemic design | 系统设计（整体工作实践视角） | L4812、L5006 |
| C08 | Redesigned scripts | 再设计脚本 | L5014 |
| C09 | User Environment model | 用户环境模型 | L5036 |
| C10 | Pugh matrix | Pugh 矩阵评估 | L5010 |
| C11 | Cross-functional team | 跨职能团队（TQM 借鉴） | L4816 |
| C12 | Paper mockup / prototyping | 纸原型迭代 | L5050 |

### 机构（Institution）
| 编号 | 名称 | 行号 |
|---|---|---|
| I01 | InContext Enterprises, Inc. | L4779 |
| I02 | Digital Equipment Corporation | L4791 |

### 地点（Place）
| 编号 | 名称 | 行号 |
|---|---|---|
| L01 | 设计室（团队共享空间） | L4996-L5004 |

### 事件（Event）
| 编号 | 名称 | 行号 |
|---|---|---|
| E01 | CHI 教程首次公开 CI（Holtzblatt/Jones/Knox） | L4795 |
| E02 | 九年团队教练过程（方法演化） | L4785 |

## 九、与前后章关联

本章是全书方法论的总纲，把前 14 个案例的分散技术整合为单一流程：Ch1 的行为流、Ch3 的访谈、Ch4 的 CI 用法、Ch11-Ch13 的 CI/情境设计案例、Ch2 的纸面工具都在此获得系统位置。与 Ch15（民族志）、Ch16（参与式设计）构成框架三章，但本章是"最完整、最可执行"的整合框架。主编导言（L590-L594）对本章的定位与内容做了完整预示。
