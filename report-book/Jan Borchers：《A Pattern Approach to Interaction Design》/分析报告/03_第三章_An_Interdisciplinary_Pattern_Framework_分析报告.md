# 03_第三章 An Interdisciplinary Pattern Framework 分析报告

---

## 一、章节定位与功能

### L### 1.1 章节定位

本章（pp.51-73，约23页）是全书的理论核心，承担"框架构建"功能。它位于Ch.2（历史综述+需求规格）之后、Ch.4（三套实例模式语言）之前，是全书的"概念发动机"——后续所有章节均以本章定义的概念框架为工作基础。

在全书六章中，本章的理论密度最高——包含形式数学模型、软件生命周期嵌入、时间维度理论化、以及10个模式成分的跨领域规范——而且这一切在仅23页内完成。

### L### 1.2 核心功能

1. **形式化功能（Formalization）**：以数学集合论符号为模式语言和模式本身提供了领域无关的严格定义。$PL = (\wp, \Re)$和$P = \{n, r, i, p, f_1...f_i, e_1...e_j, s, d\}$不是装饰性的数学化——它们同时服务于理论精确性（消除歧义）、跨领域适用性（不绑定任何特定领域术语）、以及计算机工具支持（PET工具的数据模型基础）。

2. **过程嵌入功能（Process Integration）**：将模式语言框架嵌入Nielsen (1993)的可用性工程生命周期的全部11个阶段，论证了模式如何在每一阶段发挥作用——从"了解用户"（第一阶段）到"收集现场反馈"（第十一阶段）。这是将模式从"静态知识库"转化为"动态过程工具"的关键步骤。

3. **时间维度理论化（Temporal Dimension）**：明确指出Alexander纯粹基于"空间大小"的层级组织原则不足以处理交互设计——因为交互设计的产品（用户界面）在交互过程中会发生实质变化。解决方案：将层级排序原则从"空间大小"扩展为"时空范围"。

4. **成分规范功能（Component Specification）**：对模式十大组成部分逐一进行跨领域（HCI/软件工程/应用领域）的需求分析和规范定义——确保三个领域的模式格式真正"统一"而非仅仅是"格式相同"。

---

## 二、结构分析

### L### 2.1 内部结构

```
§3.1 A Formal Model of Pattern Languages (约2页)
    ├── PL = (℘, ℜ) — 模式语言作为有向无环图
    ├── P = {n, r, i, p, f₁...fᵢ, e₁...eⱼ, s, d} — 模式作为有序集合
    └── 10个成分的初步定义 + 形式vs文本的张力

§3.2 Pattern Languages in the Software Lifecycle (约10页)
    ├── 图3.1: 三种模式语言的分工图
    ├── §3.2.1: Nielsen的可用性工程生命周期(11阶段)
    └── §3.2.2: 三套模式语言在11个阶段的具体使用方式

§3.3 Time in Patterns (约3页)
    ├── 问题: Alexander的空间层级忽略时间
    ├── 方案: 将"空间大小"→"时空范围"
    └── 结构暗示: 时间被放在层级的顶层(任务>对话>UI对象)

§3.4 Patterns and Their Components in Detail (约8页)
    ├── 3.4.1 Name (命名规则+跨学科可理解性)
    ├── 3.4.2 Ranking (两星评级制)
    ├── 3.4.3 Illustration (媒体选择取决于领域)
    ├── 3.4.4 Problem and Forces (对立力量概念)
    ├── 3.4.5 Examples (归纳法: 例子→概括)
    ├── 3.4.6 Solution (建设性而非描述性)
    ├── 3.4.7 Diagram (示意图 vs 插图)
    └── 3.4.8 Context and References (设计过程引导)
```

### L### 2.2 结构特征

1. **从抽象到具体**：§3.1给出纯形式定义→§3.2将其嵌入具体过程→§3.3处理一个抽象维度（时间）→§3.4逐个成分具体化——从最高抽象下降到最具体层面。

2. **形式-文本双重性**：§3.1既给出了严格的数学定义，又立即声明"for actual presentation, patterns are not represented as formulae, but rather as written texts"——这一声明缓解了数学化可能导致的"可读性"焦虑，同时保留了形式化的精确性优势。

3. **生命周期嵌入作为论证核心**：§3.2是本章最长的子节——不仅因为11个阶段的逐一解释需要篇幅，更因为"嵌入生命周期"是Borchers框架区别于此前的所有模式集合（Alexander, Gamma, Tidwell均未提供此类嵌入）的关键差异点。

---

## 三、内容分析（核心论题+关键论点案例）

### L### 3.1 核心论题

本章的核心论题可归纳为：

> 一个跨学科的模式语言框架——应用于HCI、软件工程和应用领域——可以通过**形式的图论定义、生命周期的过程嵌入、时间维度的纳入**和**十个组成部分的跨领域规范**而被严格构建，从而为交互系统设计过程提供统一的经验表达和沟通工具。

### L### 3.2 §3.1 形式模型：关键论点和细节

**定义1：模式语言**
> $PL = (\wp, \Re)$ — 模式语言是一个有向无环图，节点 $\wp = \{P_1, \ldots, P_n\}$ 为模式，边 $\Re = \{R_1, \ldots, R_m\}$ 为引用关系。

- "有向无环"（DAG）的性质保证了层次结构的严格性——不能出现循环引用，确保"从大到小"的展开方向是单向的。

**定义2：模式**
> $P = \{n, r, i, p, f_1 \ldots f_i, e_1 \ldots e_j, s, d\}$ — 每个模式由名称(n)、评级(r)、插图(i)、问题(p)、力(f₁...fᵢ)、例子(e₁...eⱼ)、解决方案(s)和图(d)组成。

**定义3：Context和References作为双向关系**
> context = 指向该模式的入边集合，references = 从该模式发出的出边集合

- 这个定义澄清了一个常被误解的点：context和references在Alexander的实践中并非严格的"双向链接"（"the graph of links that point downwards...is different from the graph of those that point upwards"）——但Borchers强调Alexander更重视"教学品质"甚于"数学精确性"。

**关键声明**：
> "This formal definition helps to clarify the structure of patterns and pattern languages...It is also useful as a model to implement computerized tools that support authoring or browsing pattern languages. For actual presentation, however, patterns are not represented as formulae, but rather as written texts."

这个声明揭示了Borchers的方法论立场——在"严格性"和"可读性"之间，他追求"以形式化保证内部一致性，以自然语言保证外部交流性"的双轨策略。

### L### 3.3 §3.2 生命周期嵌入：11阶段的模式应用

Borchers将三套模式语言嵌入Nielsen的11个阶段的详细映射：

| 阶段 | 阶段名称 | HCI模式 | 软件模式 | 应用领域模式 |
|------|---------|---------|---------|------------|
| 1 | Know the user | — | — | **核心**：用模式格式记录用户任务 |
| 2 | Competitive analysis | 从竞争产品中抽取HCI模式 | (不可获得) | — |
| 3 | Setting usability goals | 可用性目标→高层HCI模式的forces | — | — |
| 4 | Parallel design | 外部HCI模式→设计指南 | — | — |
| 5 | Participatory design | HCI模式→用户理解设计师的价值观 | — | **核心**：领域专家借领域模式参与讨论 |
| 6 | Coordinated design | HCI模式词汇→界面一致性 | — | — |
| 7 | Guidelines & heuristic analysis | 模式→改进形式的指南 | — | — |
| 8 | Prototyping | HCI设计师理解软件架构约束 | **核心**：软件模式→HCI设计师理解技术 | — |
| 9 | Empirical testing | 识别问题→链接到可应用的HCI模式 | — | 领域模式→构造现实测试场景 |
| 10 | Iterative design | 模式→建设性的设计方案建议 | 软件模式→信息化的设计选项 | — |
| 11 | Collect field feedback | HCI模式→指出替代方案 | — | 领域模式→用户与设计师的共同词汇 |

**关键洞察**：
- 领域模式在阶段5（参与式设计）中发挥最大的跨学科价值——设计师通过领域模式学习用户的专业术语，用户通过模式格式理解设计师的工作方式
- 阶段10（迭代设计）中的"HCI模式→建设性的"（constructive）vs"设计指南→描述性的"（descriptive）——这是全书最精炼的模式vs指南对比

### L### 3.4 §3.3 时间维度

**核心论点**：
> "This simple organizing principle [of spatial size] ignores one major dimension: time. This works reasonably well for architecture, as the artefacts created (buildings, streets, etc.) do not change themselves substantially over time. ... This approach does not work for HCI, software engineering, and many other application domains, because the artefacts they create do change substantially over time, following the tasks they support."

**解决方案**：
- "put time at the top of the hierarchy, according to the large-scale notion of tasks"——在HCI中，设计师首先考虑"完整任务是什么"，然后细化"每个交互步骤的设计"，最后才是"每个UI对象的布局"。
- 这样做使层级排序原则从"空间大小"扩展为"时空范围"。

### L### 3.5 §3.4 成分详解——十个模式组成部分的跨领域规范

每个子节遵循"通用定义→HCI特殊要求→软件工程特殊要求→应用领域特殊要求"的结构：

| 成分 | 关键洞见 | 跨领域差异 |
|------|---------|-----------|
| **Name** (3.4.1) | 名称是"the only thing that is remembered literally"——两词最佳，四词上限 | 应用领域模式可使用领域术语；HCI/软件模式应避免不可译的行话 |
| **Ranking** (3.4.2) | 采用Alexander的0/★/★★三档 | 所有领域相同 |
| **Illustration** (3.4.3) | "sensitizing the reader"——功能是感性唤起而非信息传达 | 建筑=照片；HCI=屏幕截图/视频(需包含时间)；软件=对象交互图；音乐=音频 |
| **Problem & Forces** (3.4.4) | "this part is often the most difficult one to write"；Forces必须是对立的 | 建筑=物理/社会力；HCI=认知/社会/经济；软件=技术力(如内存vs速度)；应用领域=可能难以表达为对立力 |
| **Examples** (3.4.5) | 双重功能：引导新手+给专家提供实证 | 选择该领域广泛已知的系统 |
| **Solution** (3.4.6) | "the central message"——"a succinct form (usually not more than a few short sentences)" | HCI=心理/时空规则；软件=架构/实现建议；应用领域=领域工作方式 |
| **Diagram** (3.4.7) | "more concise and schematic than the illustration"——专业人员的快速理解工具 | 建筑=手绘；HCI=手绘+故事板(时间)；软件=UML(但需考虑可读性)；音乐=乐谱 |
| **Context & References** (3.4.8) | "the added value that turns a loose collection of patterns into a pattern language" | 排序原则取决于领域：建筑=空间大小；HCI=时空范围(任务→对话→组件→原语)；软件=架构→组件→实现 |

---

## 四、逻辑梳理（论证链条+因果转折）

### L### 4.1 整章论证链

```
Ch.2 → 六项要求 (问题空间)
            │
            ▼
§3.1: 形式定义 (解决方案的"骨架")
    ├── PL = (℘, ℜ) — 模式语言的数学本质
    └── P = {n, r, i, p, f, e, s, d} — 模式的数学本质
            │
            ▼
§3.2: 过程嵌入 (骨架的"运动方式")
    ├── 三个模式语言的分工 (HCI/软件/应用领域)
    └── 在11个生命周期阶段的具体操作
            │
            ▼
§3.3: 时间维度 (运动中的一个关键方向)
    └── 将排序原则从"空间大小"扩展为"时空范围"
            │
            ▼
§3.4: 成分详解 (骨架的"血肉")
    └── 十个成分的跨领域规范
            │
            ▼
Ch.4 → 实例化证明
```

### L### 4.2 关键因果转折

1. **从"形式"到"过程"的跳跃**：§3.1定义的是静态结构（图），§3.2描述的是动态过程（生命周期）。两者之间的逻辑连接是隐含的——Borchers没有正式论证"为什么一个图论模型能够映射到可用性工程生命周期"，而是通过实际映射来证明其可行性。这是一种"通过实践来论证"而非"通过逻辑来论证"的策略。

2. **"时间"作为独立概念的介入**：§3.3中时间的讨论虽然被放在了§3.2（生命周期）和§3.4（成分详解）之间，但其内容实质上是§3.4.8（Context and References中关于排序原则的讨论）的前置扩展。这个位置安排暗示了"时间"在Borchers框架中的双重角色：(a)作为层级排序原则的维度，(b)作为个别模式内容的维度（在§3.4.3的Illustration和§3.4.7的Diagram中讨论）。

3. **"Force"作为质量控制点**：§3.4.4将能否表达为对立力（opposing forces）作为判断某领域知识是否适合模式化的"试金石"——"existing efforts...often fail at expressing their problems using opposing forces. This usually indicates that the solutions presented are not really design-oriented patterns...but rather activity patterns"。这是一个方法论上的关键判断：不是所有经验都可以模式化，只有涉及"冲突力量的平衡"的设计性知识才适合。

---

## 五、材料使用方式

### L### 5.1 对Nielsen (1993)的"框架化"使用

Nielsen的可用性工程生命周期是§3.2的基本框架——但Borchers不是在"引用"Nielsen，而是在"改写"Nielsen。Nielsen的原著11个阶段有更详细的子阶段和更偏向"评估"的重心，Borchers将其改写为"模式使用指南"——每个阶段被重述为一组"在这个阶段，模式语言可以用来做X"的操作性指令。这种使用方式使Nielsen的模型成为"模式框架的载体"而非"独立的理论资源"。

### L### 5.2 图3.1和图3.2的视觉论证

- **图3.1**（p.55）：三套模式语言的分工图——以连接三个圈（HCI / Application Domain / Software Engineering）的用户界面设计师作为"relay person"。这个图不仅传达信息，更在视觉上重新分配了传统开发中的角色——"software engineers usually create the software design on their own, and often even do the user interface design...users are hardly involved"→新模式将"responsibilities shifted further to the left"。
- **图3.2**（p.56）：三套模式语言的具体层次结构——以少数模式实例代表各自的语言。这是在Ch.4大量模式出现之前的"预告"——读者在看到图的这一刻还不知道每个模式的具体内容，但可以预见即将到来的大规模模式展开。

### L### 5.3 音乐和建筑的类比

Borchers频繁使用音乐术语来描述模式的层级组织——例如"coarse...changes are applied before finer-grained adjustments"（§3.4.8）。这种语言选择暗示了作者的两个知识来源在写作中的自然渗透：一方面是第4章将以音乐作为应用领域，一方面是Alexander的建筑话语（"coarse/fine-grained"是建筑设计的经典区分）。

### L### 5.4 对Dix et al. (1998)的策略性引用

> "Probably 90% of the value of any interface design technique is that it forces the designer to remember that someone (and in particular someone else) will use the system under construction." (cited on p.56)

这个引文被放置在§3.2开头——它的功能是降低读者对"将模式框架嵌入具体生命周期模型"这一建议的抵触。Dix的"90%"说法暗示：具体的生命周期模型的选择并不如看起来那么关键——重要的是有某种过程能让你记住用户。这就为Borchers选择Nielsen的具体模型（而非其他可能的模型）做了学术上的"解围"。

---

## 六、论辩与阐述方法

### L### 6.1 形式化-去形式化的双重策略

Borchers在§3.1中引入了形式化的数学定义，但紧接着又"去形式化"——声明形式定义用于计算机工具而非人类读者。这是对两个潜在批评的同时防御：
- 对"过度形式化"的批评者：我已经声明这个定义只用于计算机工具，实际模式是以人类可读的散文呈现的
- 对"缺乏理论严格性"的批评者：我提供了形式的数学定义，比任何软性的描述更精确

### L### 6.2 过程嵌入中的演绎论证

§3.2.2对11个生命周期阶段的逐一展开采用的是一种统一的论证格式：
```
在第X阶段, [需要完成某种设计活动]
    → HCI/软件/应用领域模式 [可以以某种方式提供支持]
    → 举例说明 [具体如何支持]
```
这产生了一种"覆盖性"（exhaustiveness）的效果——读者感到框架已经考虑到开发过程的所有关键节点。

### L### 6.3 "反模式"的引入作为一种谦逊姿态

在§3.2.2的阶段10（迭代设计）中，Borchers提到了anti-patterns：
> "There is, however, the notion of anti-patterns, which document particularly bad solutions that people often implement due to lack of better knowledge."

这不是一个中心论点，但在修辞上具有重要性——它表明Borchers意识到模式方法不是万能的（有些设计决策记录的是"失败"而非"成功"），从而避免了方法论上的傲慢。

### L### 6.4 对Alexander的修正而非否定

在§3.3中，Borchers指出Alexander的空间层级排序忽略了时间维度——但他的措辞是"expanded into"（扩展为）而非"replaced by"（替代为）。这种措辞选择将自己定位为"Alexander的扩展者"而非"Alexander的反对者"——保持了学术谱系上的连续性。

---

## 七、语言文风（原文摘录+L###）

### L### 7.1 整体风格

本章的英文是全书最"重"的——学术性和形式化程度最高。但它巧妙地通过两种手段缓解了密集度：
1. 图表的视觉呼吸（图3.1, 3.2以及生命周期的分点列表）
2. 模式成分详解中使用具体例子（如"WHAT'S FOR DINNER?"的命名批评）打破抽象论述

### L### 7.2 代表性原文摘录

#### L### 7.2.1 形式定义——数学精确性

> "1. A pattern language is a directed acyclic graph $PL = (\wp, \Re)$ with nodes $\wp = \{P_1, \ldots, P_n\}$ and edges $\Re = \{R_1, \ldots, R_m\}$.
> 2. Each node $P \in \wp$ represents a pattern.
> 3. For two nodes $P, Q \in \wp$, we say that P references Q if and only if there is a directed edge $R \in \Re$ leading from $P$ to $Q$.
> 4. The set of edges pointing away from a node $P \in \wp$ is called its references, and the set of edges pointing to it is called its context.
> 5. Each node $P \in \wp$ is itself a set $P = \{n, r, i, p, f_1 \ldots f_i, e_1 \ldots e_j, s, d\}$..." (§3.1, pp.52-53)

这段形式定义在全书的散文中显得突出——它是全书唯一使用这种严格数学表述的段落。它的功能不仅是提供精确的语义，更是建立了"理论框架可以是严格科学的"的认知。在HCI领域（通常以实证研究和设计实践为方法论基础），这种形式化姿态本身就是一个声明。

#### L### 7.2.2 图论的形式与文本的优先性——双重声明

> "This formal definition helps to clarify the structure of patterns and pattern languages, and gives a domain-independent description of the structure of a pattern language. It is also useful as a model to implement computerized tools that support authoring or browsing pattern languages. For actual presentation, however, patterns are not represented as formulae, but rather as written texts, to make them easy to read and understand even for people from other professions." (§3.1, pp.53-54)

"however"之后的句子是整个形式化论辩的关键转折——它建立了Borchers认识论立场的核心：理论严格性服务于实际可读性，而不是相反。这种"形式服务于人"的立场是全书试图在"工程严谨"和"人文关怀"之间取得平衡的缩影。

#### L### 7.2.3 名称选择——从ENTRY PROCESS到ENTRANCE TRANSITION

> "Alexander [1979, p. 267] gives an example of how his group improved a pattern name over several iterations. ... From an initial name ENTRY PROCESS (much too vague), via HOUSE STREET RELATIONSHIP (not defining the relationship), and FRONT DOOR INDIRECTLY REACHED FROM STREET (still not defining the place to create), they arrived at a final name that actually captures the idea that a concrete space, the 'transition', needs to be created: ENTRANCE TRANSITION." (§3.4.1, p.65)

这个命名迭代过程不仅是关于命名的，更是关于模式设计本身的隐喻——从"模糊的动词"到"具体的名词"，这个过程最好地展示了什么是"把一种感觉转化为一个可操作的设计指令"。Borchers在这里让Alexander自己展示"如何做好模式"——通过引用的过程本身教育读者。

#### L### 7.2.4 Forces的试金石功能

> "The existing efforts that have been presented in section 2.4 to carry the pattern idea over to the application domain often fail at expressing their problems using opposing forces. This usually indicates that the solutions presented are not really design-oriented patterns balancing conflicting design goals, but rather activity patterns that just describe existing work practice without validating it." (§3.4.4, p.69)

这是全书最接近"方法论宣言"的段落之一。它建立了一个明确的区分标准（"能否表达为对立力"）来划分"真正的设计模式"和"仅仅是活动描述"。这个标准对Borchers自己的后续工作也有约束力——在第4章中，所有11个音乐模式都必须通过"forces"的检验。

#### L### 7.2.5 HCI中的设计序列与空间+时间层级

> "HCI actually uses a similar design sequence with time as an added dimension, especially when following the ideas of user-centred design and iterative prototyping as outlined in the usability engineering lifecycle: after task analysis, which in the pattern framework creates the application domain pattern language, the user interface is designed in an iterative process. The first designs are crude prototypes, paper sketches, or storyboards that deal with the overall structure of the interaction. Only in subsequent iterations, those designs are refined, user interface objects identified until final prototypes deal with small-scale issues of graphical layout etc." (§3.4.8, pp.72-73)

这是"展开过程"（unfolding）在HCI中的具体化——它论证了HCI设计过程本身遵循"从粗到细"的层级化顺序，因此模式语言的层级化组织原则（大尺度模式→小尺度模式）与HCI设计过程的自然流程是"同构的"。

---

## 八、实体清单（六类每类≥3+L###）

### L### 8.1 人物实体

| 编号 | 姓名 | 出现位置 | 角色 | L### |
|------|------|---------|------|------|
| 1 | Jakob Nielsen | §3.2.1核心 | 可用性工程生命周期模型(1993)的作者——其11阶段模型是§3.2的组织骨架 | L###301 |
| 2 | Christopher Alexander | §3.1, §3.3, §3.4多处 | 建筑模式语言创始人——在命名、排序、隐式结构等多处被引用为指导权威 | L###302 |
| 3 | Hermann Hesse | 章首引语 | "The Glass Bead Game" (Magister Ludi)——其关于"跨学科通用语言"的构想被用作本书跨学科框架的文学隐喻 | L###303 |
| 4 | Donald A. Norman | §3.4.4 (Gestalt), §3.4.8 | 提供"natural mappings"概念和"labeling"批评——被借用来支持命名和forces的讨论 | L###304 |
| 5 | Alan Dix et al. | §3.2开头 | "90% of the value"著名断言——被用来缓解对框架嵌入特定生命周期模型的顾虑 | L###305 |
| 6 | Martijn van Welie | §3.4.1 | "WHAT'S FOR DINNER?"——被用作模式名称"过度隐喻化"的反面案例 | L###306 |
| 7 | Wolfgang Köhler | §3.4.4 | Gestalt心理学创始人——其理论被用作HCI中"空间力"的理论基础 | L###307 |
| 8 | George A. Miller | §3.4.4 (隐含) | 认知心理学——"7±2"和"verbal recoding"概念隐含着影响了forces和name的讨论 | L###308 |

### L### 8.2 文献实体

| 编号 | 文献 | L### |
|------|------|------|
| 1 | Nielsen. Usability Engineering (1993) | L###309 |
| 2 | Alexander. The Timeless Way of Building (1979) | L###310 |
| 3 | Alexander et al. A Pattern Language (1977) | L###311 |
| 4 | Dix et al. Human-Computer Interaction, 2nd ed. (1998) | L###312 |
| 5 | Gamma et al. Design Patterns (1995) | L###313 |
| 6 | Borchers. "A pattern approach to interaction design" (DIS 2000) | L###314 |
| 7 | Borchers et al. INTERACT'99 & CHI 2000 workshop reports | L###315 |
| 8 | Tidwell. Common Ground (1998) | L###316 |
| 9 | Norman. The Psychology of Everyday Things (1988) | L###317 |
| 10 | Hesse. The Glass Bead Game (Magister Ludi) | L###318 |

### L### 8.3 系统/产品实体

| 编号 | 名称 | L### |
|------|------|------|
| 1 | WorldBeat (图3.2中作为模式语言层级图的核心示例) | L###319 |
| 2 | Mac OS (Simple Finder, Balloon Help) | L###320 |
| 3 | PET (Pattern Editing Tool, 在§3.1中被预先提及) | L###321 |

### L### 8.4 概念实体

| 编号 | 概念 | L### |
|------|------|------|
| 1 | 形式模式语言定义 $PL = (\wp, \Re)$ | L###322 |
| 2 | 形式模式定义 $P = \{n, r, i, p, f_1...f_i, e_1...e_j, s, d\}$ | L###323 |
| 3 | 可用性工程生命周期 (Usability Engineering Lifecycle) | L###324 |
| 4 | 时间作为设计维度 (Time as Design Dimension) | L###325 |
| 5 | 跨学科"接力人"角色 (Relay Person) — 图3.1 | L###326 |
| 6 | 对立力量 (Opposing Forces) | L###327 |
| 7 | 模式命名规则 (两词最佳，四词上限) | L###328 |
| 8 | 两级评级制 (0/★/★★) | L###329 |
| 9 | 归纳式写作 (Inductive Style): 例子→方案 | L###330 |
| 10 | 结构设计原理 (Structural/Post-hoc Design Rationale) | L###331 |
| 11 | 过程设计原理 (Process Design Rationale) | L###332 |
| 12 | 反模式 (Anti-Patterns) | L###333 |
| 13 | 空间+时间排序原则 | L###334 |
| 14 | 设计过程同构性 (Design Process Isomorphism) | L###335 |

### L### 8.5 机构实体

无本章专属的重大机构实体。

### L### 8.6 技术实体

| 编号 | 名称 | L### |
|------|------|------|
| 1 | UML (Unified Modeling Language — 在Diagram讨论中被提及) | L###336 |
| 2 | MIDI (在应用领域Diagram的讨论中隐含) | L###337 |
| 3 | XML (在§3.1中作为PET工具基础被预先暗示，详见Ch.5) | L###338 |

---

## 九、与前后章关联

### L### 9.1 与Ch.2的关联

- §2.1的隐式排版分析 → §3.4中每个成分的详细规范（将"Alexander做了什么"转换为"你应该怎么做"）
- §2.5的对比表 → §3.1的形式定义（从"观察到的共识"上升到"规定的形式结构"）
- §2.6的六项要求 → §3.1-§3.4的逐一满足（框架→格式统一；层级→设计过程支持；etc.）
- §2.3中交互设计的时间讨论 → §3.3（从"注意到问题"到"提出系统方案"）

### L### 9.2 与Ch.4的关联

本章定义的每一个概念都在Ch.4中得到直接实例化：
- §3.1的$PL=(\wp, \Re)$ → Ch.4的三个模式语言图（图4.2, 4.14, 4.37）
- §3.1的$P=\{n, r, i, p, f, e, s, d\}$ → Ch.4的每个模式严格按此结构书写
- §3.4.3的Illustration媒体选择 → Ch.4中音乐模式使用乐谱和唱片封面、HCI模式使用屏幕截图和展品照片
- §3.4.8的"时空范围"排序 → Ch.4中HCI模式从ATTRACT-ENGAGE-DELIVER（全局任务）到ONE INPUT DEVICE（具体设备）的层级

### L### 9.3 与Ch.5的关联

- §3.1的形式模型 → Ch.5 §5.8中PET工具的超文本数据模型基础
- §3.2的生命周期嵌入 → Ch.5 §5.5中展示模式如何在后续项目的不同阶段被实际使用
- §3.4的10个成分规范 → Ch.5 §5.2中Peer Review针对具体模式（DOMAIN-APPROPRIATE DEVICES）的格式评估
- §3.3的时间维度 → Ch.5 §5.1中作为"Design dimension coverage"要求被满足的证据

---

*本报告根据 Jan Borchers: 《A Pattern Approach to Interaction Design》Chapter 3 (pp.51-73) 细读撰写。*
