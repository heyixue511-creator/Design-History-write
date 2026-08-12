# 06_第六章分析报告：Action-Centered Design（行动中心设计）

**作者**：Peter Denning（George Mason 大学计算机科学系主任，前 ACM 主席）和 Pamela Dargan（高级软件工程师）
**附 Profile 6**：Business-Process Mapping（业务流程映射）

---

## 一、章节定位与功能

本章代表了全书从"计算机科学内部"发起的对传统软件工程方法的批判性重构。Denning 是 ACM 前主席和计算机科学教育的核心人物，他与其合作者 Dargan 从内部批判软件工程，提出"行动中心设计"（action-centered design）作为替代范式。

L### 定位要素
- **范式转换功能**：从未自设计或艺术领域，而是自计算机科学内部发起对软件工程的根本性批判——"The standard engineering design process produces a fundamental blindness to the domains of action in which the customers of software systems live and work"
- **方法论提案功能**：提出"software architecture"（软件架构）作为新的学科名称，以"action-centered design"为其核心实践——将 Christopher Alexander 的建筑模式语言引入软件设计
- **桥梁功能**：连接了本书的设计话语（前五章）与软件工程的工程技术话语——为两种语言之间的翻译提供了概念工具

核心论断：
> "We propose a broader interpretation of design that is based on observing the repetitive actions of people in a domain and connecting those action-processes to supportive software technologies."

---

## 二、结构分析

本章由四个递进部分组成，每部分都以"问题诊断→替代方案"的对比结构展开。

**第一部分：现状批判——软件工程的失败**
- 1979 年美国政府问责局数据：9 个国防部软件项目——2% 交付并被使用、25% 从未交付、50% 交付但从未使用
- 软件工程"unwittingly created an illusion"——以为将需求转换为系统的严格流程是可靠设计的关键
- 揭示软件工程的三条核心假设及其局限

**第二部分：两种设计范式的对比**
- 软件工程（product-centered）：结果 = 产品 ← 规格说明 ← 几乎无需与客户接触
- 人本设计（human-centered）：结果 = 满意的客户 ← 持续协作 ← 持续沟通
- 引入成功软件包（Quicken, MeetingMaker, Topic, Macintosh UI）设计师的调查结果——他们"did not pay much attention to standard software-engineering methodology"

**第三部分：行动中心设计与领域本体论**
- 引入 Alexander 的"模式语言"（pattern language）作为类比
- 提出"领域本体论"（ontology of the domain）作为软件架构师的核心工作对象
- 六类基本模式：
  1. 语言区分（linguistic distinctions）
  2. 言语行为（speech acts）
  3. 标准实践（standard practices）
  4. 就手工具（ready-to-hand tools）
  5. 故障（breakdowns）
  6. 持续关切（ongoing concerns）

**第四部分：业务流程映射**
- 业务流程作为行动协调的分析层次——高于物质过程和信息过程
- ActionWorkflow 环路模型：请求→协商→执行→完成

**附 Profile 6：Business-Process Mapping**（Denning & Winograd 撰写，详述工作流映射方法，包括 ActionWorkflow 环路的四个阶段和其在组织分析中的应用）

L### 结构特征
以"失败→研究成功反例→提出替代方案"的三段论展开——核心转折发生在对成功设计师的调查研究结果："the internal structure of their code is ugly and is not well modularized"——成功的软件并不遵循软件工程教科书的原则。

---

## 三、内容分析：核心论题与关键论点/案例

**核心论题 1：软件工程的根本性盲目**
Denning & Dargan 的核心批判是：标准工程设计过程产生了"对客户生活和工作的行动领域的根本性盲目"（"a fundamental blindness to the domains of action"）。这不是方法的失效，而是方法本身的结构性缺陷——它把设计框定为"从规格中推导系统"的过程，从而必然地忽视了实际的使用情境。

**核心论题 2：人本设计的替代性假设**
- 好设计的结果 = 满意的客户（而非符合规格的产品）
- 设计过程 = 设计师与客户的协作（而非从规格的单向推导）
- 设计师与客户处于持续沟通中（而非仅在需求阶段和交付时接触）

**核心论题 3：行动中心设计——领域本体论**
以 Alexander 的建筑模式语言为模型，提出软件的"领域本体论"：
- 不是关注"系统做什么"（功能），而是关注"人在做什么"（行动）
- 六类模式涵盖了从语言、行为、实践到工具和故障的完整行动生态
- 软件架构师的工作 = 绘制这个本体论 → 将其表达为模式语言 → 协调建造者的工作

**核心论题 4：言语行为作为行动协调的基础**
"S speech acts such as 'I request,' 'I promise,' 'I have completed the task,' and 'I am satisfied' are important because they are the motivating force for action." 这一论断将 Winograd & Flores (1987) 的语言-行动视角引入软件设计方法论。

**关键案例**：
- 1979 年美国政府问责局数据——软件失败的量化证据
- Quicken / MeetingMaker / Topic / Macintosh 设计师调查——成功的秘诀是"study the nature of the actions"而非遵循软件工程方法论
- 个人金融的领域本体论——语言区分（支票、账本、银行…）、言语行为（pay, deposit, withdraw…）、标准实践（每月付账单、对账…）、就手工具（笔、计算器、税表…）——一个完整的示例
- ActionWorkflow 环路的四阶段——作为业务过程映射的基本单位

L### 核心论点关键词
- Action-centered design（行动中心设计）
- Ontology of the domain（领域本体论）
- Pattern language（模式语言）
- Speech acts（言语行为）
- Software architecture（软件架构）
- Fundamental blindness（根本性盲目）
- Customer satisfaction（客户满意）vs. specification conformance（规格符合）

---

## 四、逻辑梳理：论证链条与因果转折

**论证链条**：
```
[证据呈现] 软件项目失败率惊人（1979 GAO 数据）
    ↓
[原因诊断] 软件工程的基本假设（产品中心、规格驱动、客户远距）→ "根本性盲目"
    ↓
[替代方案提出] 人本设计的三条替代假设
    ↓
[经验验证] 成功设计师的调查：不遵循软件工程，而是研究用户的行动模式
    ↓
[方法论建构] 领域本体论 → 模式语言 → 架构蓝图
    ↓  （借鉴Alexander的建筑模式语言 + Winograd & Flores的语言-行动理论）
[工具配套] 业务流程映射（ActionWorkflow环路）作为分析行动的实用工具
    ↓
[学科提案] "software architecture"作为软件工程与设计的统一学科
```

**关键因果转折**：
- 从"软件工程是正确方法但执行不力"到"软件工程的方法本身就是问题"——这是一个决定性的诊断转折。"The software crisis is usually seen as a breakdown in the application of this methodology...The shortcoming is not due to a lack of effort...The problem is of a different kind"
- 从"从规格中推导系统"到"从观察行动中推导系统"——不是改进旧方法，而是转向新的出发点
- 从"软件工程"到"软件架构"——借用建筑领域的 prestige 来赋予新的方法论以学科合法性

**内在张力**：
- Denning & Dargan 强调"formal method"的价值——他们的领域本体论是高度结构化的——这与 Kelley (Ch.8) 的"design is messy"和 Schön (Ch.9) 的"design is a conversation"存在张力
- 他们试图通过"architecture"（建筑）的类比同时吸引工程派（需要系统方法）和设计派（需要关注人的行动）——这种双栖策略既有整合力，也有内部矛盾

---

## 五、材料使用方式

**政府数据**：1979 年 GAO 报告——提供软件失败的量化证据——具有"客观权威"的修辞效果。

**成功案例调查**：对 Quicken、MeetingMaker、Synchronize、Topic、Macintosh 设计者的访谈——从"成功的设计师实际上做了什么"出发，而非从理论出发——这是一种"实践导向的归纳"策略。

**建筑理论类比**：Christopher Alexander 的"A Pattern Language"——将建筑领域的"模式"概念映射到软件的"行动模式"——为软件的"本体论"提供成熟的参考框架。

**语言-行动理论**：Winograd & Flores (1987)、Searle (1969)——为"speech acts as motivators of action"提供哲学基础。

**学术文献引用**：Bohem（瀑布模型和螺旋模型）、Floyd（人本设计）、Neumann（计算机风险）——将论证置于计算机科学的学术传统之中。

L### 材料运用的特点
- 本章是学术性最强的一章——使用了"方法论回顾+经验调查+理论建构"的典型学术论文结构
- 成功设计师引语的直接引用（"the internal structure of their code is ugly and is not well modularized"）是本章最具冲击力的经验证据

---

## 六、论辩与阐述方法

**1. 经验归纳法**：通过调查成功设计师的实践，归纳出共同模式——"There was a surprising level of unanimity in their answers"——以经验共识对抗理论正统。

**2. 对立框架法**：以三组对立指标对比两种范式（结果：产品 vs. 客户 → 过程：推导 vs. 协作 → 关系：远距 vs. 持续）——清晰的结构对比使论证一目了然。

**3. 案例示范法**：用个人金融领域完整地展示六类模式的具体内容——将抽象的"领域本体论"转化为可操作的清单。

**4. 类比授权**："The field of architecture is rich in useful analogies and practices"——通过建筑（更成熟的设计领域）的类比为软件设计的提案背书。

**5. 谦虚修辞**："We propose this interpretation not as a final answer, but as a preliminary step—an opening for a new direction"——以开放性的姿态避免教条主义的印象。

**6. 数据引用**：GAO 数字（2%/25%/50%）以量化证据打开讨论——数字的精确性建立了批判的可信度。

---

## 七、语言文风：附原文摘录 + L### 标注

本章语言是全书最具"学术论文"风格的一章——术语密集、定义明确、论证结构清晰。

**代表摘录 1**（根本性批判）：
> "The standard engineering design process produces a fundamental blindness to the domains of action in which the customers of software systems live and work. The connection between measurable aspects of the software and the satisfaction of those customers is, at best, tenuous."
L### 特征："fundamental blindness"不是修辞夸张而是诊断性的概念——"根本性盲目"的意思是：这不是方法的偶然失败，而是方法的结构性特征

**代表摘录 2**（成功设计师的反直觉发现）：
> "All the designers said that they did not pay much attention to standard software-engineering methodology. Several said that the internal structure of their code is ugly and is not well modularized. When fixing bugs, they made patches; when the system got too patchy, they declared the next version and redesigned the software completely."
L### 特征：以直接引语方式呈现反直觉发现——"ugly code"作为成功产品的特征——动摇"良好工程设计=产品成功"的假设

**代表摘录 3**（行动中心设计的定义）：
> "A discipline of software design must train its practitioners to be skilled observers of the domain of action in which a particular community of people engage, so that the designers can produce software that assists people in performing those actions more effectively."
L### 特征：定义中的动词——"observe"（观察）、"assist"（协助）——将设计师定位为"行动域的观察者和协助者"而非"系统的设计者"

**代表摘录 4**（言语行为的重要性）：
> "Speech acts...are important because they are the motivating force for action. Without them, no task would be declared, initiated, or completed, and no one would know whether anyone else was satisfied."
L### 特征：以否定条件句（"Without them"）反向论证言语行为的基础性——言语行为不是系统的附属功能，而是行动的起点

L### 整体文风评价
本章的学术严谨性使其成为全书中最适合用于教学和课程设计的章节。但极高的术语密度和理论抽象度也可能使其对非学术读者（尤其是非计算机背景的设计师）不够亲切——这恰好反映了"两个世界"（计算机科学与设计实践）之间的沟通挑战。

---

## 八、实体清单：六类每类≥3项 + L### 标注

#### 1. 人物
| 编号 | 名称 | L### 说明 |
|------|------|-----------|
| P01 | Peter Denning | ACM 前主席，"Denning report" 作者。L### 从"计算机科学内部"发起对软件工程的批判，具有特殊的学科政治意义 |
| P02 | Pamela Dargan | 高级软件工程师。L### 近二十年的软件开发经验——为理论提案提供实践锚点 |
| P03 | Christopher Alexander | 建筑模式语言理论家。L### "A Pattern Language"——本章方法论蓝图的核心类比来源 |
| P04 | Peter Neumann | 计算机风险研究者。L### GAO 数据的引用来源——"Computer-Related Risks" |
| P05 | John Searle | 言语行为理论哲学家。L### "speech acts"概念的理论源头 |
| P06 | Terry Winograd | 本书主编。L### "Understanding Computers and Cognition" (1987, with Flores)——语言-行动视角的来源 |

#### 2. 组织/公司
| 编号 | 名称 | L### 说明 |
|------|------|-----------|
| O01 | Intuit (Quicken) | L### 个人财务管理软件的生产者——成功设计师访谈的核心案例之一 |
| O02 | On Technologies (MeetingMaker) / Crosswind Technologies (Synchronize) | L### 日程和会议管理软件——另一个成功案例 |
| O03 | Verity (Topic) | L### 文档检索系统——成功案例之一 |
| O04 | Action Technologies, Inc. | L### ActionWorkflow 方法论和工具的商业化企业——Profile 6 的核心 |
| O05 | ACM (Association for Computing Machinery) | L### Denning 曾担任主席——他本人的机构身份增加了批判的内部合法性 |

#### 3. 产品/系统
| 编号 | 名称 | L### 说明 |
|------|------|-----------|
| S01 | Quicken | Intuit 的个人理财软件。L### "study the nature of actions"的成功范例 |
| S02 | MeetingMaker / Synchronize | L### 会议日程系统——作为"理解协作行动"的案例 |
| S03 | Topic (Verity) | L### 基于文本内容的文档检索——作为"理解信息检索行动"的案例 |
| S04 | ActionWorkflow Analyst | L### Action Technologies 的工作流映射工具——作为"制图"的实例 |

#### 4. 概念/理论
| 编号 | 名称 | L### 说明 |
|------|------|-----------|
| C01 | Action-Centered Design（行动中心设计） | L### 本章核心提案——以观察人类重复行动并将其与软件技术连接为基础的学科实践 |
| C02 | Ontology of the Domain（领域本体论） | L### "a conceptual framework for interpreting the world in terms of recurrent actions"——六类模式构成 |
| C03 | Pattern Language（模式语言） | L### 源自 Alexander——"patterns are not objects...but relationships among simpler patterns and the environment" |
| C04 | Speech Acts（言语行为） | L### Searle → Winograd & Flores——"the motivating force for action" |
| C05 | ActionWorkflow Loop（行动工作流环路） | L### request → negotiation → performance → completion——业务过程的基本单位 |
| C06 | Fundamental Blindness（根本性盲目） | L### 本章对软件工程的核心诊断——方法本身的结构性缺陷 |

#### 5. 事件
| 编号 | 名称 | L### 说明 |
|------|------|-----------|
| E01 | 1979 年 GAO 软件项目审查 | L### 2% 成功 / 25% 未交付 / 50% 未使用——软件工程失败的经典量化证据 |
| E02 | Denning & Dargan 的成功设计师调查 | L### 访谈软件获奖产品的设计师——"surprising level of unanimity"——本章核心经验证据 |
| E03 | "Denning report" (1989) | L### Denning 领导的计算机科学课程修订——他本人的学科改革背景 |

#### 6. 文献/文本
| 编号 | 名称 | L### 说明 |
|------|------|-----------|
| B01 | Denning & Dargan, "A discipline of software architecture" (interactions, 1994) | L### 本章的前身——更学术化的版本 |
| B02 | Alexander, A Pattern Language (1977) / The Timeless Way of Building (1979) | L### 模式语言——本章的方法论类比来源 |
| B03 | Winograd & Flores, Understanding Computers and Cognition (1987) | L### 语言-行动视角——本章"ontology of domain"和"speech acts"的理论来源 |
| B04 | Neumann, Computer-Related Risks (1995) | L### GAO 数据的引述来源 |
| B05 | Medina-Mora et al., "The ActionWorkflow approach" (1993) | L### Profile 6 的核心参考文献——工作流环路的技术描述 |

---

## 九、与前后章关联

**与 Ch.5 (Saffo) 的关系**：
- 互补：Saffo 从外部（市场/消费者）问"设计为谁"，Denning & Dargan 从内部（方法）问"设计基于什么"——两章分别回答了设计的前提条件的"外"和"内"

**与 Ch.7 (Brown & Duguid) 的关系**：
- 深层呼应：Denning & Dargan 的"标准实践"和"就手工具"概念与 Brown & Duguid 的"border resources"和"genre"概念——两者都强调设计需要理解用户实际使用中的常规和资源
- 区别：Ch.6 偏重"结构化地描述行动"（本体论），Ch.7 偏重"理解行动如何在文化意义中生成"（社会文化语境）

**与 Ch.9 (Schön) 的关系**：
- 隐性对话：Schön 强调设计的不可预测性和反思性——Denning & Dargan 的方法论提案（领域本体论 + 行动工作流环路）有可能被误解为一种新的"系统化"——但作者以"preliminary step"的谦虚姿态避免了这种误解

**与 Ch.14 (Kuhn) 的关系**：
- 补充：Kuhn 讨论的是工作场所中计算机系统对工人的社会政治影响——Denning & Dargan 的"行动中心设计"如果被认真执行，应该能够避免 Kuhn 所描述的 TTS/HELP/Big Bank 中的设计失败
- 区别：Ch.6 偏重方法论，Ch.14 偏重伦理和政治

**与 Profile 6 (Business-Process Mapping) 的关系**：
- 直接配套：Profile 6 提供了 Ch.6 所倡导的方法论的具体工具描述——ActionWorkflow 环路的四个阶段、工作流映射的三层分析（material/information/business processes）

---

*分析完成时间：2026-08-04*
