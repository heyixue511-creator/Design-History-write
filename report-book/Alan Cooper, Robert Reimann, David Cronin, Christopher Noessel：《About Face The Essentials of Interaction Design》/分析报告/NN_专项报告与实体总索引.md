# NN 专项报告与实体总索引

---

## 专项报告一：核心方法论链——从研究到交付的完整逻辑

### 1.1 Goal-Directed Design 方法论链全景

```
定性研究 (CH 2)
  → Persona 构建 (CH 3)
    → 情境场景与需求定义 (CH 4)
      → 交互框架设计 (CH 5, 9)
        → 细节设计与控件选择 (CH 5, 21)
          → 可用性验证 (CH 5)
            → 开发支持 (CH 5, 6)
```

### 1.2 每个阶段的输入-输出-关键决策

| 阶段 | 输入 | 关键决策 | 输出 | 核心章节 |
|------|------|----------|------|----------|
| 研究 | 项目目标、初始假设 | 研究范围、方法选择、访谈对象 | 行为数据、观察记录 | CH 2 |
| 建模 | 定性数据 | Persona 类型分配、Primary 确定 | Persona 集合、领域模型 | CH 3 |
| 需求 | Persona、目标 | "魔法" vs 现实的取舍 | 数据/功能/情境需求 | CH 4 |
| 框架 | 设计需求 | 姿态选择、功能分组、导航结构 | 交互/视觉/服务框架 | CH 5, 9 |
| 细化 | 框架、原则、模式 | 控件选择、错误策略、视觉层次 | 详细设计规格 | CH 5, 7-17, 21 |
| 支持 | 设计规格 | 实现可行性反馈、设计调整 | 最终产品 | CH 5, 6 |

---

## 专项报告二：概念地图——全书核心概念关系网络

### 2.1 核心概念聚类

**Cluster 1: 用户理解**
- Persona（CH 3）
- 目标（Goals）——体验目标/最终目标/人生目标（CH 3）
- 心智模型（Mental Model）（CH 1）
- 行为变量（Behavioral Variables）（CH 2, 3）

**Cluster 2: 设计过程**
- Goal-Directed Design 六阶段（CH 1）
- 情境场景（Context Scenario）（CH 4）
- 关键路径场景（Key Path Scenario）（CH 5）
- 验证场景（Validation Scenario）（CH 5）
- 矩形草图（Rectangle Sketch）（CH 5）

**Cluster 3: 设计品质**
- 设计价值观（Design Values）——伦理/目标导向/务实/优雅/无害（CH 7）
- 数字礼仪（Digital Etiquette）（CH 8）
- 心流（Flow）（CH 11）
- Excise——附加工作（CH 12）
- 优雅（Elegance）（CH 7）

**Cluster 4: 交互模式**
- 实现模型/心智模型/表现模型（CH 1）
- 姿态（Posture）——独占/暂时/后台/辅助（CH 9）
- 隐喻/习惯用法/示能性（CH 13）
- 直接操纵（Direct Manipulation）（CH 11）

**Cluster 5: 设计质量保障**
- 错误预防——Poka-Yoke（CH 15）
- 撤销（Undo）（CH 15）
- 视觉层次（Visual Hierarchy）（CH 17）
- 格式塔原则（CH 17）
- 可用性测试——形成性/总结性（CH 5）

**Cluster 6: 团队与组织**
- 生成者/综合者（Generator/Synthesizer）（CH 6）
- 15 分钟规则（CH 6）
- 敏捷协作（CH 6）
- 设计技能层级（CH 6）

### 2.2 核心概念跨章节引用热力图

| 概念 | CH1 | CH2 | CH3 | CH4 | CH5 | CH6 | CH7 | CH8 | CH9 | CH10 | CH11 | CH12 | CH13 | CH14 | CH15 | CH16 | CH17 | CH18 | CH19 | CH20 | CH21 |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|------|------|------|------|------|------|------|------|------|------|------|
| Persona | ● | ○ | ●●● | ●●● | ●● | ○ | ○ | ○ | ○ | ● | ○ | ○ | ○ | ○ | ○ | ● | ○ | ○ | ○ | ○ | ○ |
| 目标 | ●● | ○ | ●●● | ●● | ● | ○ | ● | ○ | ○ | ○ | ○ | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| 表现模型 | ●●● | ○ | ○ | ○ | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ●● | ●● | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| Excise | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ● | ○ | ●●● | ● | ● | ● | ○ | ○ | ● | ● | ● | ●● |
| 心流 | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ● | ○ | ● | ●●● | ●● | ○ | ○ | ● | ○ | ○ | ○ | ○ | ○ | ○ |
| 姿态 | ○ | ○ | ○ | ○ | ●● | ○ | ○ | ○ | ●●● | ○ | ● | ○ | ○ | ○ | ○ | ○ | ○ | ●● | ●● | ● | ○ |
| 错误预防 | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ●●● | ○ | ○ | ○ | ○ | ○ | ● |
| 视觉层次 | ○ | ○ | ○ | ○ | ● | ○ | ○ | ○ | ○ | ○ | ○ | ● | ○ | ○ | ○ | ○ | ●●● | ○ | ○ | ○ | ● |

● = 核心讨论  ○ = 提及或应用  ●●● = 该概念的定义和核心讨论所在章

---

## 专项报告三：关键争议与学派对话

### 3.1 Persona vs JTBD（Jobs-to-be-Done）

| 维度 | Persona 方法（Cooper） | JTBD 方法（Christensen） |
|------|----------------------|--------------------------|
| 核心问题 | "谁在使用？" | "用户想完成什么工作？" |
| 分析单元 | 人（用户原型） | 任务/工作（需要完成的事） |
| 数据来源 | 定性人种志研究 | 用户行为观察 + 购买决策分析 |
| 优势 | 丰富的同理心、团队共情 | 聚焦于功能优先级、更简单 |
| 弱点 | 维护成本高、可能过度聚焦"人" | 可能丢失"人"的丰富语境 |
| 互补方式 | Persona 提供"谁"，JTBD 提供"要做什么" | 结合使用 |

### 3.2 Goal-Directed Design vs Lean UX

| 维度 | Goal-Directed Design | Lean UX |
|------|---------------------|---------|
| 节奏 | 前期深度研究 → 设计 → 验证 | 快速假设 → 实验 → 迭代 |
| 研究深度 | 深（人种志访谈） | 浅（快速验证） |
| 输出物 | 详尽的 Persona、场景、需求文档 | 低保真原型、持续更新的假设 |
| 最佳场景 | 全新产品、复杂领域 | 已有产品的持续优化 |
| 主要风险 | 分析瘫痪（Analysis Paralysis） | 局部最优（Local Optimization） |
| 平衡建议 | 用 Persona Hypothesis 启动，Lean 方式迭代验证 | |

### 3.3 隐喻 vs 习惯用法（本书内部的核心辩证）

| 维度 | 隐喻立场 | 习惯用法立场（Cooper 立场） |
|------|----------|---------------------------|
| 设计基础 | 类比熟悉事物 | 建立可学习的约定 |
| 学习成本 | 理论上更低（"直觉"） | 需要学习，但学后极低 |
| 创新空间 | 受物理世界限制 | 可以利用数字媒介的全部可能性 |
| 适合阶段 | 概念探索 | 交互实现 |
| 风险 | 拟物主义、功能受限 | 过度依赖已有约定、难以创新 |
| Cooper 的平衡 | 概念层用隐喻，交互层用习惯用法 | |

### 3.4 可用性测试的角色之争

| 立场 | 代表 | 观点 |
|------|------|------|
| 测试驱动设计 | 部分可用性专家 | 通过反复测试迭代优化设计 |
| 设计驱动测试 | Cooper | 测试验证设计，而非替代设计。测试告诉你什么坏了，不告诉你该建什么 |

---

## 专项报告四：跨时代检验——2014 vs 2026

### 4.1 已过时的内容（需结合新文献更新）

| 内容 | 原章节 | 过时原因 | 替代参考 |
|------|--------|----------|----------|
| 桌面为主的平台视角 | CH 18 | 移动优先已成为主流 | Wroblewski《Mobile First》 |
| iPhone 2007 的革命叙事 | CH 19 | 移动设计已进入"后iPhone"时代 | Apple HIG、Material Design 最新版 |
| 传统 Web 2.0 架构 | CH 20 | SPA、PWA、Jamstack 改变了Web应用 | React/Vue 设计系统文档 |
| 无 AI/ML 考量 | 全书 | AI 驱动的交互已无处不在 | Google PAIR、Microsoft HAX 工具包 |
| 无语音/VUI 设计 | 全书 | 语音助手已普及 | Pearl《The Voice in the Machine》 |
| 无 Design System 概念 | CH 17, 21 | 组件化设计系统已成行业标准 | Kholmatova《Design Systems》 |
| 无隐私设计 | CH 7, 8 | GDPR、CCPA 改变了数据设计的约束 | 隐私设计（Privacy by Design）文献 |

### 4.2 仍然有效的核心洞见（历久弥新）

| 洞见 | 原章节 | 在当前的价值 |
|------|--------|-------------|
| 目标 > 任务 | CH 1, 3 | AI 代理时代比 2014 年更相关 |
| Persona 作为沟通工具 | CH 3 | 在远程协作时代更显重要 |
| 数字礼仪 | CH 8 | AI 助手的伦理基础设施 |
| Excise | CH 12 | 自动化浪潮中的设计北极星 |
| 习惯用法 > 隐喻 | CH 13 | 触屏手势和语音指令的学习性基础 |
| 撤销 > 确认对话框 | CH 15 | 仍未被充分实践的黄金原则 |
| 表现模型 ≠ 实现模型 | CH 1, 14 | 解释 AI 可解释性问题的框架 |

---

## 专项报告五：作者思想谱系

### 5.1 四位作者的贡献分布

| 作者 | 主要贡献领域 | 对应章节 |
|------|-------------|----------|
| **Alan Cooper** | 方法论创始人、Persona 概念、设计价值观 | CH 1, 3, 7, 13 的核心思想 |
| **Robert Reimann** | 设计原则体系、设计研究流程 | CH 2, 7, 8, 10-12 的大量内容 |
| **David Cronin** | 企业级设计实践、设计团队协作 | CH 5, 6, 9 |
| **Christopher Noessel** | 第四版新增内容、服务设计、敏捷协作 | CH 5（服务框架）、CH 6（敏捷）、CH 8（AI 伦理更新） |

### 5.2 Cooper 的思想谱系

```
Victor Papanek (设计伦理)
  → Alan Cooper (交互设计方法论)
    ├─→ Persona 方法 → Grudin & Pruitt (微软实践)
    ├─→ 目标导向设计 → 设计思维运动
    ├─→ Cooper 公司实践 → 美国交互设计行业
    └─→ About Face 系列 → 全球交互设计教育

Don Norman (认知心理学 + 情感设计)
  → Cooper 的三层目标模型 (体验/最终/人生)

Clifford Nass & Byron Reeves (Media Equation)
  → Cooper 的数字礼仪概念

Csikszentmihalyi (心流理论)
  → Cooper 的心流与编排 (CH 11)
```

---

## 六、实体总索引

### 6.1 人物索引

| 人名 | 英文名 | 出现章节 | 贡献/关联 |
|------|--------|----------|-----------|
| 艾伦·库珀 | Alan Cooper | 全书 | 第一作者、方法论创始人 |
| 罗伯特·雷曼 | Robert Reimann | 全书 | 第二作者、设计原则体系 |
| 大卫·克罗宁 | David Cronin | 全书 | 第三作者、企业设计实践 |
| 克里斯托弗·诺塞尔 | Christopher Noessel | 全书 | 第四作者、第四版更新 |
| 唐·诺曼 | Don Norman | CH 1, 3, 13 | 情感设计、认知处理三层理论 |
| 维克多·帕帕奈克 | Victor Papanek | CH 1, 7 | 设计伦理、设计定义 |
| 克利福德·纳斯 | Clifford Nass | CH 8 | Media Equation、人机社交互动 |
| 拜伦·里夫斯 | Byron Reeves | CH 8 | Media Equation |
| 米哈里·契克森米哈赖 | Mihaly Csikszentmihalyi | CH 11 | 心流理论 |
| 雅各布·尼尔森 | Jakob Nielsen | CH 5 | 可用性工程、形成性/总结性评估 |
| 金·古德温 | Kim Goodwin | CH 2, 3, 5, 6 | 设计研究方法、Persona 实践 |
| 拉里·康斯坦丁 | Larry Constantine | CH 3 | 用户角色模型 |
| 露西·洛克伍德 | Lucy Lockwood | CH 3 | 用户角色模型 |
| 休·杜伯利 | Hugh Dubberly | CH 7 | 设计价值观制定者之一 |
| 布伦达·劳雷尔 | Brenda Laurel | CH 4 | 叙事与交互设计 |
| 唐纳德·舍恩 | Donald Schön | CH 2 | 反思性实践 |
| 史蒂文·平克 | Steven Pinker | CH 2 | 认知科学、自我认知局限 |
| J.J. 吉布森 | J.J. Gibson | CH 13 | 示能性概念 |
| 乔治·莱考夫 | George Lakoff | CH 13 | 隐喻的认知语言学 |
| 马克·约翰逊 | Mark Johnson | CH 13 | 隐喻的认知语言学 |
| 比尔·巴克斯顿 | Bill Buxton | CH 4, 11 | 草图用户体验 |
| 杰夫·拉斯金 | Jef Raskin | CH 10, 12, 13, 14 | 人性化界面 |
| 爱德华·塔夫特 | Edward Tufte | CH 12, 17 | 视觉信息设计 |
| 彼得·莫维尔 | Peter Morville | CH 20 | 信息架构 |
| 路易斯·罗森菲尔德 | Louis Rosenfeld | CH 20 | 信息架构 |
| 史蒂夫·克鲁格 | Steve Krug | CH 10, 12, 20 | Web 可用性 |
| 杰西·詹姆斯·加勒特 | Jesse James Garrett | 前言/引言 | 用户体验要素 |
| 克莱顿·克里斯滕森 | Clayton Christensen | CH 3 | Jobs-to-be-Done 理论 |

### 6.2 关键术语索引

| 中文术语 | 英文术语 | 定义章节 | 核心应用章节 |
|----------|----------|----------|-------------|
| 目标导向设计 | Goal-Directed Design | CH 1 | CH 1-6 |
| 人物模型 | Persona | CH 3 | CH 3-5, 16 |
| 实现模型 | Implementation Model | CH 1 | CH 1, 14 |
| 心智模型 | Mental Model | CH 1 | CH 1, 4 |
| 表现模型 | Represented Model | CH 1 | CH 1, 13, 14 |
| 附加工作 | Excise | CH 12 | CH 12, 14, 15, 21 |
| 数字礼仪 | Digital Etiquette | CH 8 | CH 8, 11, 15 |
| 姿态 | Posture | CH 9 | CH 9, 18-20 |
| 心流 | Flow | CH 11 | CH 11, 12 |
| 习惯用法 | Idiom | CH 13 | CH 13, 21 |
| 隐喻 | Metaphor | CH 13 | CH 1, 13 |
| 示能性 | Affordance | CH 13 | CH 13, 21 |
| 情境场景 | Context Scenario | CH 4 | CH 4, 5 |
| 关键路径场景 | Key Path Scenario | CH 5 | CH 5 |
| 验证场景 | Validation Scenario | CH 5 | CH 5 |
| Poka-Yoke | Poka-Yoke | CH 15 | CH 15 |
| 撤销 | Undo | CH 15 | CH 15 |
| 视觉层次 | Visual Hierarchy | CH 17 | CH 17 |
| 生成者-综合者 | Generator-Synthesizer | CH 6 | CH 6 |
| 响应式设计 | Responsive Design | CH 20 | CH 19, 20 |

### 6.3 组织与产品索引

| 名称 | 出现章节 | 关联内容 |
|------|----------|----------|
| Cooper（设计咨询公司） | CH 6 | 团队协作模式的实践来源 |
| Xerox PARC / Alto | CH 18 | 桌面界面的历史源头 |
| Apple / iPhone | CH 1, 9, 19 | 移动交互的范式转变 |
| Microsoft / Windows / Office | CH 1, 5, 12, 14, 18 | 正反案例 |
| Google / Android / Gmail / Docs | CH 12, 14, 19, 20 | 良好设计的案例 |
| Adobe Photoshop | CH 5, 9, 10, 18 | 独占型应用的设计典范 |
| Facebook | 多处引用 | 社交交互分析 |
| Dropbox | CH 1 | 危险操作位置的反例 |

### 6.4 关键著作索引

| 著作 | 作者 | 关联章节 | 核心论点 |
|------|------|----------|----------|
| *The Design of Everyday Things* | Norman | CH 1, 13, 15 | 示能性、错误、强制函数 |
| *Emotional Design* | Norman | CH 3 | 三层认知处理（visceral/behavioral/reflective） |
| *The Media Equation* | Nass & Reeves | CH 8 | 人机互动 = 人际互动 |
| *Flow* | Csikszentmihalyi | CH 11 | 心流理论 |
| *Contextual Design* | Beyer & Holtzblatt | CH 2, 3 | 情境调查、用户建模 |
| *Designing for the Digital Age* | Goodwin | CH 2-6 | 设计研究和 Persona 操作指南 |
| *The Humane Interface* | Raskin | CH 10, 12, 13, 14 | 模态、Excise、文件系统批判 |
| *Sketching User Experiences* | Buxton | CH 4, 11 | 设计草图与叙事 |
| *Don't Make Me Think* | Krug | CH 10, 12, 20 | Web 可用性 |
| *The Elements of User Experience* | Garrett | 引言 | 用户体验五层模型 |
| *Design for the Real World* | Papanek | CH 1, 7 | 设计伦理 |
| *Metaphors We Live By* | Lakoff & Johnson | CH 13 | 隐喻的认知基础 |
| *Information Architecture* | Morville & Rosenfeld | CH 20 | Web 信息架构 |

---

## 七、文件索引

### 7.1 本分析报告目录完整文件列表

```
分析报告/
├── 00_整体分析报告.md
├── CH01_分析报告_A Design Process for Digital Products.md
├── CH02_分析报告_Understanding the Problem Design Research.md
├── CH03_分析报告_Modeling Users Personas and Goals.md
├── CH04_分析报告_Setting the Vision Scenarios and Design Requirements.md
├── CH05_分析报告_Designing the Product Framework and Refinement.md
├── CH06_分析报告_Creative Teamwork.md
├── CH07_分析报告_A Basis for Good Product Behavior.md
├── CH08_分析报告_Digital Etiquette.md
├── CH09_分析报告_Platform and Posture.md
├── CH10_分析报告_Optimizing for Intermediates.md
├── CH11_分析报告_Orchestration and Flow.md
├── CH12_分析报告_Reducing Work and Eliminating Excise.md
├── CH13_分析报告_Metaphors Idioms and Affordances.md
├── CH14_分析报告_Rethinking Data Entry Storage and Retrieval.md
├── CH15_分析报告_Preventing Errors and Informing Decisions.md
├── CH16_分析报告_Designing for Different Needs.md
├── CH17_分析报告_Integrating Visual Design.md
├── CH18_分析报告_Designing for the Desktop.md
├── CH19_分析报告_Designing for Mobile and Other Devices.md
├── CH20_分析报告_Designing for the Web.md
├── CH21_分析报告_Design Details Controls and Dialogs.md
└── NN_专项报告与实体总索引.md
```

### 7.2 原书结构对照

```
About Face 4th Edition
├── Part I: Goal-Directed Design
│   ├── CH 1: A Design Process for Digital Products
│   ├── CH 2: Understanding the Problem: Design Research
│   ├── CH 3: Modeling Users: Personas and Goals
│   ├── CH 4: Setting the Vision: Scenarios and Design Requirements
│   ├── CH 5: Designing the Product: Framework and Design Refinement
│   └── CH 6: Creative Teamwork
├── Part II: Designing Behavior and Form
│   ├── CH 7: A Basis for Good Product Behavior
│   ├── CH 8: Digital Etiquette
│   ├── CH 9: Platform and Posture
│   ├── CH 10: Optimizing for Intermediates
│   ├── CH 11: Orchestration and Flow
│   ├── CH 12: Reducing Work and Eliminating Excise
│   ├── CH 13: Metaphors, Idioms, and Affordances
│   ├── CH 14: Rethinking Data Entry, Storage, and Retrieval
│   ├── CH 15: Preventing Errors and Informing Decisions
│   ├── CH 16: Designing for Different Needs
│   └── CH 17: Integrating Visual Design
└── Part III: Interaction Details
    ├── CH 18: Designing for the Desktop
    ├── CH 19: Designing for Mobile and Other Devices
    ├── CH 20: Designing for the Web
    └── CH 21: Design Details: Controls and Dialogs
```

---

*索引生成日期：2026-08-04*
*基于《About Face: The Essentials of Interaction Design》第四版全文及其分析报告系统*
