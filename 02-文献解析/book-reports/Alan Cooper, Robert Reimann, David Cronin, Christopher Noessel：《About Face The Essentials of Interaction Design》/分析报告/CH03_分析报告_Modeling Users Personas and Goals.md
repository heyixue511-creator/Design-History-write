# CH 03 分析报告：Modeling Users: Personas and Goals（用户建模：人物模型与目标）

---

### 一、章节概述

本章是全书的"心脏"。Cooper 团队在此完整呈现了 Persona（人物模型）方法的理论依据、构建流程和实践指南。章节首先论证了 Persona 在克服"弹性用户"、"自我指涉设计"和"边缘情况"三大设计陷阱中的关键作用，随后系统阐述了 Persona 的八大构建步骤，并将 Don Norman 的三层认知处理理论与用户目标分类进行了创造性整合——提出了体验目标、最终目标、人生目标的三层目标框架。本章还讨论了非用户目标（客户目标、商业目标、技术目标）的平衡问题，以及 Persona 与其他用户模型（角色模型、市场细分）的本质区别。

---

### 二、核心概念与术语

| 术语 | 英文 | 定义 |
|------|------|------|
| 人物模型 | Persona | 基于研究数据合成的复合用户原型 |
| 弹性用户 | Elastic User | 缺乏明确定义时被不同利益相关者随意拉伸的模糊用户概念 |
| 自我指涉设计 | Self-Referential Design | 设计师/开发者将自己的目标投射到产品设计 |
| 边缘情况 | Edge Case | 可能发生但通常不会发生的情况，不应驱动设计 |
| 行为变量 | Behavioral Variable | 用以区分用户行为模式的多维度特征轴 |
| 体验目标 | Experience Goal | 用户在使用产品时希望获得的感受（对应 visceral 层） |
| 最终目标 | End Goal | 用户使用产品的动机——完成任务或达成状态（对应 behavioral 层） |
| 人生目标 | Life Goal | 超越具体产品的深层个人愿望（对应 reflective 层） |
| 主要人物模型 | Primary Persona | 产品的核心设计目标用户，每个界面只能有一个 |
| 次要人物模型 | Secondary Persona | 基本满意主要人物模型设计但有额外特定需求的用户 |
| 补充人物模型 | Supplemental Persona | 需求完全被主要+次要人物模型覆盖的用户 |
| 客户人物模型 | Customer Persona | 购买决策者而非终端用户的建模 |
| 被服务人物模型 | Served Persona | 非使用者但受产品使用影响的人 |
| 负面人物模型 | Negative Persona | 明确定义产品不为谁设计 |

---

### 三、关键论点与分析

**论点 1：为一个人设计 = 为所有人设计**

这是 Cooper 方法中最具争议也最深刻的洞见。逻辑上，为满足多样化用户，似乎应设计尽可能广泛的功能。但 Cooper 的论证是反向的：当你试图取悦所有人时，你实际上没有取悦任何人。聚焦于一个具体的 Primary Persona 的设计决策在各个 Persona 之间形成张力，这种张力恰好产生了有灵魂的设计——而非妥协的"平均"设计。

**论点 2：三大设计陷阱源于"用户"一词的空泛**

- **弹性用户**：当你说"用户需要 X"，实际上你指的是"我认为用户需要 X"，每个人都在定义自己的用户。
- **自我指涉设计**：开发者为自己设计功能。
- **边缘情况**：罕见的极端场景被当作设计驱动，使日常使用变得复杂。

Persona 通过提供一个具体的、有名字的、有照片的、有行为细节的"人"，使以上三个问题在团队沟通中自然消解。

**论点 3：目标 > 任务（深化）**

CH 1 提出目标优于任务，本章通过 Norman 的三层理论将其操作化：
- **体验目标**：感觉聪明、有掌控感、有趣（visceral）
- **最终目标**：完成报表、联系家人（behavioral）
- **人生目标**：成为受尊敬的专业人士、过上美好的生活（reflective）

只有最终目标被满足是不够的——用户可能在完成任务的过程中因为糟糕的体验而弃用产品。

**论点 4：Persona 必须有动机**

Persona 如果只有人口统计特征（年龄、收入、地点）而没有行为动机（目标），就只是市场细分而非设计工具。

**论点 5：每个界面只有一个 Primary Persona**

这是 Cooper 方法中最严格的原则之一。一个产品可以有多个界面，每个界面服务于不同的 Primary Persona，但同一界面不可能同时为两个不同 Primary Persona 优化。

---

### 四、方法论与工具

**Persona 构建八步法**：

1. **按角色分组访谈对象**：基于 Persona Hypothesis 的组织
2. **识别行为变量**：列出区分用户行为的维度
3. **将访谈对象映射到行为变量**：创建行为映射矩阵
4. **识别显著行为模式**：在映射中寻找聚类（Cluster）
5. **合成特征并定义目标**：从行为聚类推导 Persona 属性和三种目标
6. **检查完整性和冗余**：确保 Persona 集合覆盖用户谱系但不过度重叠
7. **指定 Persona 类型**：分为 Primary/Secondary/Supplemental/Customer/Served/Negative
8. **扩展属性与行为描述**：撰写叙事、选择照片

**Persona 叙事的要求**：
- 是对研究数据的综合，而非虚构
- 包含具体的、可感知的行为描述
- 照片使其"真实"，增强团队的共情
- 长度适中：一到两页

**其他设计模型**：
- **工作流模型**（Workflow Models）：信息流和决策过程
- **制品模型**（Artifact Models）：用户使用的工具和表格
- **物理模型**（Physical Models）：用户的工作/生活环境布局

---

### 五、案例与实践应用

**Persona 如何避免设计陷阱**：

- **弹性用户 → Persona**：当 PM 说"用户需要导出功能"时，设计师可以问："Vivian（Primary Persona）需要这个吗？她是会计师，通常直接在系统内完成所有分析，不需要导出。"
- **自我指涉设计 → Persona**：当开发者想添加一个命令行快捷方式时，可以问："我们的 Primary Persona 是护士 Cheryl，她会用命令行吗？"
- **边缘情况 → Persona**：当讨论一个极少发生的操作是否符合 Persona 的日常使用模式时，Persona 提供判断基准。

**临时 Persona（Provisional Persona）的适用场景**：

当资源不足以支持完整的定性研究时，可以使用基于现有知识的临时 Persona，但需明确标注为"临时"，并在条件允许时用研究数据验证和修正。

**组织 Persona**：

Cooper 团队发现，将 Persona 的概念应用于组织本身也有价值——描述一个组织的"行为模式"（如创新程度、技术采用速度、预算决策方式）。

---

### 六、与其他章节的关联

- **CH 2**：研究数据 → Persona 构建的输入
- **CH 4**：Persona → 情境场景的"演员"
- **CH 5**：Persona → 关键路径场景的设计对象
- **CH 7**：设计原则 → 在 Persona 语境下应用
- **CH 8**：数字礼仪 → 对特定 Persona 如何表现礼貌
- **CH 16**：Persona 方法如何服务于特殊需求用户

本章是 Part I 的核心枢纽，将"研究"转化为"设计方向"。

---

### 七、学术评价与反思

**优点**：

- 八步法将抽象的"理解用户"转化为可操作、可复现的流程
- 六种 Persona 分类（Primary/Secondary/Supplemental/Customer/Served/Negative）为团队协作提供了清晰的优先级排序机制
- 将 Norman 情感设计理论融入交互设计方法的尝试具有开创性
- Persona 叙事 + 照片的组合在团队沟通中的效果有实证支持

**局限与争议**：

- **"Primary Persona 唯一性"原则**：在多元用户场景（如社交媒体平台）中，这一原则可能过于严格
- **Persona 疲劳**：长期维护 Persona 文档的团队动力衰减问题
- **数据驱动 Persona 的挑战**：行为分析（Analytics）产生的大规模定量数据如何与定性 Persona 整合
- **Job-to-be-Done 框架的竞争**：Clayton Christensen 的 JTBD 框架关注"用户想要完成的工作"而非"用户是谁"，在某些场景更具操作性
- **文化与种族偏见**：Persona 的合成过程中可能无意识地复制研究者偏见的风险

---

### 八、关键引文与数据

- "To create a product that must satisfy a diverse audience of users, logic might tell you to make its functionality as broad as possible to accommodate the most people. This logic is wrong."
- "Personas are user models that are represented as specific, individual human beings."
- "Goals motivate usage patterns."
- "A product can have only one primary persona per interface."
- "Stereotypes are, in most respects, the antithesis of well-developed personas."

---

### 九、延伸阅读与参考

1. Norman, D. *Emotional Design* (2005) —— 三层认知处理理论的完整论述
2. Goodwin, K. *Designing for the Digital Age* (2009) —— Persona 构建的详细操作指南
3. Grudin, J. & Pruitt, J. —— Persona 在微软的应用实践
4. Constantine, L. & Lockwood, L. *Software for Use* (1999) —— 用户角色模型
5. Christensen, C. *Competing Against Luck* (2016) —— JTBD 理论的竞争性视角
6. Holtzblatt, K. & Beyer, H. *Contextual Design* —— 工作流、制品和物理模型

---

*报告日期：2026-08-04 | 基于第四版 CH 3 全文分析*
