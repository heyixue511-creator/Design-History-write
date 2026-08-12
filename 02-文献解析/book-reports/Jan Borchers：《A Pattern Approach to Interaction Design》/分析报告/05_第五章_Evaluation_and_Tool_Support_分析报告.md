# 05_第五章 Evaluation and Tool Support 分析报告

---

## 一、章节定位与功能

### L### 1.1 章节定位

本章（pp.169-201，约33页）是全书的多维度评估章，承担"证明框架有效"的功能。它位于Ch.4（三套实例模式语言）之后、Ch.6（总结与展望）之前，是全书论证链的收束环节——不再提出新的理论或模式，而是对前面四章建构的理论+实例体系进行全面验证。

### L### 1.2 核心功能

1. **需求验证功能（§5.1）**：对照Ch.2 §2.6的六项初始要求，逐一确认框架是否满足。

2. **同行验证功能（§5.2）**：完整转录DOMAIN-APPROPRIATE DEVICES (H11)的Writer's Workshop同行评审过程及其改进——这是学术共同体对框架的直接质量检验。

3. **共识对齐功能（§5.3）**：将本书的模式格式与CHI 2000 Workshop的定义进行逐项对比，证明其与该领域最新共同体共识高度吻合。

4. **系统验证功能（§5.4）**：提供WorldBeat系统的完整技术描述和定量/定性评估数据——证明基于模式方法设计的系统确实成功。

5. **重用性验证（§5.5）**：通过三个后续项目（Interactive Fugue, Personal Orchestra, Virtual Vienna）证明模式语言的可转移性和迭代改进性。

6. **教学验证功能（§5.6）**：通过一项正式的教学实验（32名大一CS学生）证明模式方法在教育中的有效性。

7. **出版验证功能（§5.7）**：简要提及两大国际出版社的出版意向——以业界背书加强可信度。

8. **工具验证功能（§5.8）**：展示PET (Pattern Editing Tool)的设计，证明框架的形式化定义可以转化为实用的软件工具。

**这七个/八个维度的评估密度在全书中是独特的——没有任何其他章节对一个论点进行如此多维度的攻击。**

---

## 二、结构分析

### L### 2.1 内部结构

```
§5.1 Comparison With Framework Requirements (约2页)
    └── 六项要求逐一对照 → 结论：基本满足全部

§5.2 Pattern Peer Review (约8页)
    ├── 评审方法背景 (Writer's Workshop)
    ├── 完整转录DOMAIN-APPROPRIATE DEVICES原始文本
    ├── 评审过程转录
    │   ├── 5.2.1 Summary (三句总结)
    │   ├── 5.2.2 Positive Formal Aspects (7条正面)
    │   ├── 5.2.3 Positive Contents Aspects (8条正面)
    │   ├── 5.2.4 Format Improvement Suggestions (3条建议)
    │   ├── 5.2.5 Contents Improvement Suggestions (8条建议)
    │   └── 5.2.6 Conclusion: Main Advantages
    └── 回应: 标记*的建议原因 → 已改进

§5.3 Comparison With CHI 2000 Workshop Results (约1页)
    └── 本书格式与Workshop共识对比 → 几乎完全吻合

§5.4 Evaluation of a Resulting System: WorldBeat (约8页)
    ├── 5.4.1 Project Background (AEC/KnowledgeNet)
    ├── 5.4.2 System Features (6个模块)
    ├── 5.4.3 Implementation (技术架构详述)
    ├── 5.4.4 Usage Scenario (交互隐喻)
    └── 5.4.5 Evaluation (四类评估 + 定量数据)

§5.5 Reusing Patterns (约4页)
    ├── 5.5.1 The Interactive Fugue
    └── 5.5.2 Personal Orchestra and Virtual Vienna

§5.6 Study of Didactic Usefulness (约3页)
    └── 教学实验: 32名大一学生, 2周后评估

§5.7 Publishing Peer Review (约半页)
    └── 两大出版社的出版意向

§5.8 PET: A Pattern Editing Tool (约7页)
    ├── 形式模型的超文本化
    ├── Target Group + Tasks and Scenarios
    ├── Design: Features and Constraints
    ├── Design: Architecture (XML + Java)
    └── Storyboard of Sample Implementation
```

### L### 2.2 结构特征：七重论证的平行布局

Ch.5的结构不支持"线性递进"逻辑，而是七个平行评估维度的并列——每个小节都可以独立阅读和理解。这种并行结构的论证优势是：即使某个评估维度被质疑，其他六个维度仍能支撑框架的有效性。这是一种"多点防御"的论证策略。

---

## 三、内容分析（核心论题+关键论点案例）

### L### 3.1 核心论题

本章的核心论题是：

> Ch.3-4提出的跨学科模式框架经过七个维度的验证——需求对照、同行评审、共同体共识对齐、系统实证、重用性检验、教学有效性研究和工具可行性设计——被证明是有效的、可转移的、可教学的，并且可以扩展为计算机化的支持工具。

### L### 3.2 §5.1 需求验证

| 要求 | 满足方式 | 评估 |
|------|---------|------|
| Domain-independent, uniform, well-defined format | Ch.3的形式定义 + Ch.4三套语言统一格式 | ✓ |
| Empirical evidence | 多个模式已包含实证研究(如H15 DYNAMIC DESCRIPTOR引用Zellweger et al. 2000) | 部分: "Not all example patterns contain references...yet" |
| Domain-appropriate, design-supporting hierarchy | 三套模式语言均遵循"从整体到细节"的层级 | ✓ |
| Design dimension coverage | 时间和空间均被融入层级和模式内容 | ✓ |
| Lifecycle integration | §3.2将框架嵌入Nielsen的11阶段生命周期模型 | ✓ |
| Cross-discipline readability | 模式用散文写就，最小化行话，有非专业者可理解的例子 | ✓ |

关键的自评："unlike any of the previously existing efforts, the framework and sample pattern languages presented in this text basically fulfil all of the initial requirements"——这可能是全书最明确的"贡献声明"。

### L### 3.3 §5.2 同行评审：对DOMAIN-APPROPRIATE DEVICES的评审

**评审委员会**：5位HCI模式领域的研究者（Austin Henderson, Karri-Pekka Laakso, Victor Lombardi, Carol Strohecker, Yongmei Wu）。

**形式方面的正面评价**（7条）：
- 布局"looks exactly like Alexander's patterns"→有助于熟悉Alexander格式的读者快速定位
- 问题和解决方案以粗体突出，容易找到
- 页面尺寸和列长适合阅读
- 标题和照片有效引入模式
- 评级帮助读者判断有效性
- **隐式结构格式（排版而非显式标签）被一致好评**："repeated labels would be unaesthetic and boring"
- 插图频繁且分布均匀

**内容方面的正面评价**（8条）：
- WorldBeat照片非常合适
- URL链接到示例的"主页"是好主意
- 汽车座椅例子选得特别好："The car seat example is very well chosen"
- 解决方案包括"intuitive, efficient, and enjoyable"作为系统目标
- 解决方案措辞优秀
- 包含与其他模式的链接

**改进建议**（11条）——关键的三条：
1. "References suggest trying to map most interactions to the single input device...this may not always be appropriate" → 回应：这个模式来自描述交互式展览的更大语言，在该上下文中合理
2. "Title could be more specific" → 已在成书中保留原名
3. "Is the pattern about both input and output devices?" → 在成书中扩展为涵盖输入和输出设备
4. "Leave out the notion of 'modern' interactive systems...makes the pattern more timeless" → 已被采纳——成书中删除了"modern"

**评审的自我反思**：Borchers在脚注(*)中解释了某些批评的来源——"this pattern was taken from a larger language"——指出评审者没有看到模式在其他模式中的位置，导致了一些不适用于完整语言上下文的批评。

### L### 3.4 §5.3 共识对齐：CHI 2000 Workshop对比

CHI 2000 Workshop定义了HCI设计模式的11个组成部分：name, ranking, sensitizing example, context, problem statement, evidence, solution, sketch, references, synopsis, credits。

Borchers的框架包含了其中10个——只缺少(synopsis（被图形化的模式层级图取代）和credits（因为模式是本书的一部分所以作者自动可知）。"both this definition and the list of pattern constituents very much confirm the validity of the approach and format used in this book"。

### L### 3.5 §5.4 WorldBeat的实证评估

**定量数据**：
- 用户满意度：μ = 2.08（1=最好, 5=最差），σ = 1.12（n = 104）
- Top 3最受欢迎展品：第3名（13.5%），仅排在两个"百万美元VR"之后
- 硬件成本：约US$15,000（与百万美元VR形成鲜明对比）
- 获奖：1998 Multimedia Transfer Award（从160个参赛项目中选出9个）

**定性数据**：
- "continuous observation"显示红外线指挥棒导航和演奏"posed no problems"
- Musical Design Patterns组件是"the most attractive component"
- 用户"enjoyed 'jamming' with a blues band without playing wrong notes"
- Groove概念的教学效果："visitors quickly grasped the concept of groove in jazz, by playing with the on-screen groove slider for a few seconds"

**最后一句话特别关键**——它不仅评估了系统的娱乐价值，还评估了其作为"教学工具"的有效性，这与模式方法所声称的"支持培训和教育"功能直接相关。

### L### 3.6 §5.5 模式重用

**Interactive Fugue**：
- 重用15个已有HCI模式 + 新增多个模式
- 创造了16个新的"Fugue作曲模式"——**证明了应用领域模式方法的可转移性**（从Blues到古典Fugue）
- 音乐专家"was quick to understand the pattern format, agreed to its general appropriateness for this field"
- 使用了GoF的FAÇADE模式——证明了跨"流派"的模式互操作性

**Personal Orchestra / Virtual Vienna**：
- 最关键的论证来自一次设计会议：
  > "the customer suggested that several exhibits with standard monitors be installed instead of one exhibit with a large projection."
  > "after pointing out that this idea would violate several of the HCI design patterns...particularly IMMERSIVE DISPLAY (H13) and COOPERATIVE EXPERIENCE (H3), the idea was withdrawn"
- 这个会议场景证明模式在真实商业谈判中有效——不是学术装饰，而是可操作的决策工具
- "During meetings and written communication...being able to point to the HCI patterns saved significant time"

### L### 3.7 §5.6 教学验证

**实验设计**：
- 对象：32名大一CS本科生（其中n_0 = 32，在模式问题上n = 26作答）
- 时间线：一堂90分钟的课→学生花15分钟研究Tidwell的模式集合→2周后在不预告的情况下进行问卷调查
- 问题设计：记忆测试+三个5分制Likert量表

**结果**：
| 指标 | μ | σ | 解读 |
|------|---|---|------|
| 记住的模式数量 | 1.73 | 1.65 | "quite promising"——仅接触15分钟+2周间隔 |
| 模式对理解HCI的有用性 | 1.96 | 0.65 | 第二好成绩，高度共识 |
| 模式对当前项目的有用性 | 2.23 | 0.89 | 略差但仍为第二好，共识度降低 |
| 未来项目中重用的信心 | 1.94 | 0.81 | 第二好成绩，较高共识 |

**研究的诚实性**：Borchers指出几个局限——
- 未进行期末考试复习"may have spent more time trying to remember"
- 标准差大（σ=1.65）反映有些学生一个模式都没写出来
- 对当前项目的有用性评估较低（μ=2.23）——可能是学生刚刚完成了原型，而模式是在事后才被介绍的

### L### 3.8 §5.8 PET工具设计

**从形式模型到超文本**：
- 模式语言 = 有向图，模式 = 节点，引用关系 = 有向边 → 直接映射到超文本
- 每个模式节点 = 内容块序列（名称、评级、插图...），每个内容块 = 多媒体容器（文本/图像/音频/视频）

**设计过程使用模式自身**：PET的图形化概览页面使用DYNAMIC DESCRIPTOR模式来设计——鼠标悬停在模式图上弹出解决方案摘要。这展示了"用模式来设计模式工具"的递归性——是全书最巧妙的自我指涉（self-reference）之一。

**约束条件**：基于XML的开放标准（无需特定平台安装）、基于URL的可寻址性、内容块的分离创作（不强制使用单一编辑器）。

---

## 四、逻辑梳理（论证链条+因果转折）

### L### 4.1 七条平行论证线

```
§5.1: 需求对照
    Ch.2六项要求 → Ch.3框架 → 对照验证
    结论: 全部基本满足 (唯一未完全满足: 所有模式都有实证证据)
        ┐
§5.2: 同行评审    ├─ "共同体/外部认可"类
§5.3: 共识对齐    ┘
        ┐
§5.4: 系统实证    ├─ "实践结果"类
§5.5: 重用性检验  ┘
        ┐
§5.6: 教学实验    ├─ "教育+传播"类
§5.7: 出版认可    ┘
        ┐
§5.8: 工具设计    └─ "可扩展性"类
```

所有七条线汇合为一个总体结论：**这个框架在多个维度上都是有效的**。

### L### 4.2 关键论证亮点

**用"自己设计的行为"做证据**：在§5.5.2的会议上，Borchers用自己写的HCI模式来否决客户的建议并成功——这展示了一种"模式的内化"：模式不仅是写下来给别人用的文档，而且是内化到设计直觉中的思维工具。"being able to point to the HCI patterns"暗示了模式已经从书面文档变成了一种可即时调用的论证资源。

**谦虚与自信的平衡**：自评"basically fulfil all of the initial requirements"中的"basically"和对实证证据"Not all...yet"的承认——表明Borchers知道框架仍在发展中。而又宣称"unlike any of the previously existing efforts"——确立了相对的优越性。这是一种"有自知之明的领先者"的修辞姿态。

---

## 五、材料使用方式

### L### 5.1 "实践→文本"的倒置

大多数章节是先有文本、后有实践——Ch.5的材料使用方式是**先有实践、后有文本**：
- WorldBeat系统在1996年建成（早于本书5年）→ Ch.5提供了其评估数据
- Writer's Workshop在CHI 2000举行（本书出版前1年）→ Ch.5转录其过程
- 教学实验在1999年夏季进行 → Ch.5提供其问卷结果

这种时间顺序使Ch.5不是"预测性的理论论证"而是"回顾性的经验总结"——增强了证据的可信度。

### L### 5.2 多媒体数据的无法复制

§5.4.5指出更多细节"is also available online on the actibits home page"——这承认了纸本书籍在展示交互系统方面的固有限制。与Ch.4中的静态照片和屏幕截图不同，WorldBeat的真实交互体验必须通过视频或实地体验才能充分理解。Borchers通过提供URL承认了这一局限性而非试图用文字弥补。

### L### 5.3 同行评审转录的透明性策略

§5.2完整转录了评审过程的正面和负面评论（而非选择性地摘录）——这与通常学术写作中"选择性引用同行认可"的做法不同。这种透明性达到了双重效果：
1. 证明框架的不足可以被发现和改进（"科学可证伪性"的展示）
2. 通过展示改进过程证明框架的"适应性"

---

## 六、论辩与阐述方法

### L### 6.1 多点三角测量（Multi-point Triangulation）

Ch.5的核心论辩方法是**多点三角测量**——从多个独立的评估来源获取证据（需求对照、同行评审、用户调查、重用案例、教学实验、出版反馈），所有来源指向同一个结论（框架有效）。任何一个来源单独的论证力可能有限，但合在一起形成了几乎不可质疑的证据网络。

### L### 6.2 定量与定性的混合

- 定量数据：μ = 2.08 (WorldBeat满意度)；学习实验的四个均值
- 定性数据：观察到的用户行为（"nobody cared that the keyboard constantly changes"）；会议中的对话场景；评审者的口头评论

这种混合使论证既不被指责为"只有印象"（有定量支撑），也不被指责为"只有数字"（有故事提供意义）。

### L### 6.3 自引管理的策略

本书中Borchers大量自引——但总是在适当的地方标注：
- 自己的出版物以方括号[Borchers, 1997]等引用
- 自己组织的研讨会以"co-organized by the author"标识
- 自己的网站以[H:Borchers99]等HCI Patterns Home Page引用标记

这种自引的透明管理避免了"自我推广"的印象，而创造了"这是一个长期研究项目的成果总结"的效果。

### L### 6.4 Case Study vs. Controlled Experiment的张力

§5.4 (WorldBeat)是一个案例研究——没有对照组，没有随机分配，无法证明因果关系。§5.6 (教学实验)则是一个受控实验的近似——有前/后测，有量化评分。Borchers不试图将案例研究包装为实验——§5.4被标记为"Evaluation"而非"Experiment"，使用的是观测和调查数据而非因果推断。这种诚实的方法论标签避免了过度声称，但也暴露了HCI设计方法论研究的一个固有问题：很难在实验室中真正测试"一个框架是否改善了设计过程"。

---

## 七、语言文风（原文摘录+L###）

### L### 7.1 整体风格

Ch.5的文风介于Ch.1-3的"正式学术"和Ch.4的"模式散文"之间——在§5.1-5.3（理论评估）中偏向正式，在§5.4-5.6（实证报告）中偏向叙事，在§5.8（工具设计）中偏向工程技术写作。这种"一个章节中三种声音"的切换反映了一个方法论理念：不同种类的论证需要不同的文体。

### L### 7.2 代表性原文摘录

#### L### 7.2.1 需求验证的自评

> "In all, unlike any of the previously existing efforts, the framework and sample pattern languages presented in this text basically fulfil all of the initial requirements. Improvements in various aspects are of course still possible." (§5.1, p.170)

这个段落的修辞结构值得拆解：
- "In all" = 总结信号
- "unlike any of the previously existing efforts" = 相对优越性声明（对比的基准是Ch.2分析过的全部现有模式集合）
- "basically" = 谦虚的限定（承认不是100%完美）
- "Improvements...are of course still possible" = 结束时的科学谦卑——一个"当然"（of course）将不完美转化为"科学的常态"而非"框架的缺陷"

#### L### 7.2.2 同行评审中的元评论

> "(\*) The comments marked with asterisks arise because this pattern was taken from a larger language, because the reviewers did not know that this language particularly addresses interactive exhibits, and because the text contains a detailed description of WorldBeat elsewhere." (§5.2.5, p.178)

这个括号注释展示了Borchers对同行评审过程的元认知——他不仅接受评审意见，而且分析了**为什么**某些评审意见会产生。这是方法论自觉的高水平表现：在评审中看到评审过程本身的限制。

#### L### 7.2.3 直观的用户观察叙述

> "It also showed that modelling musical concepts as 'patterns', by turning them into software objects with an appropriate user interface, helped visitors greatly to understand those principles. For example, it was frequently observed that visitors quickly grasped the concept of groove in jazz, by playing with the on-screen groove slider for a few seconds. It usually takes the author much longer to explain this concept to musical amateurs without the help of such an interactive tool." (§5.4.5, pp.187-188)

这个段落是全章论证的"真北"——它揭示了为什么模式框架不仅仅是沟通工具，更是**让用户参与到概念中**的媒介。"playing with the on-screen groove slider for a few seconds" vs."much longer to explain...without the help of such an interactive tool"——这个对比表明，当模式概念被转化为交互式软件对象时，它们成为了一种新的教学媒介。

#### L### 7.2.4 设计会议中的模式使用——一个完整的论证场景

> "As an example, at one of these meetings for Virtual Vienna, the customer suggested that several exhibits with standard monitors be installed instead of one exhibit with a large projection. The idea was to lower the cost for display hardware and increase visitor throughput. However, after pointing out that this idea would violate several of the HCI design patterns presented, particularly IMMERSIVE DISPLAY (H13) and COOPERATIVE EXPERIENCE (H3), the idea was withdrawn in favour of the single larger exhibit." (§5.5.2, p.192)

这个场景值得作为"模式如何在实际中工作"的教科书级例子来分析：
1. 客户提出一个基于成本逻辑的建议（多个小显示器 → 降低成本）
2. Borchers不反驳"成本"论点，而是引入了**设计质量**维度（模式13+HCI模式3）
3. 客户自愿撤回建议——不是因为"Borchers说了算"，而是因为模式名称唤起了已经在会议上讨论过并达成共识的设计原则
4. "Sound on this system was also made optional..."——随后还进行了基于ATTRACTION SPACE (H2)的进一步设计决策

这是一个完整的"模式在行动"的微型案例。

#### L### 7.2.5 教学实验的结论

> "In all, these results indicate that a pattern approach in HCI education is useful and convincing. Through the structured combination of widely known examples with generalized recommendations, even first-year undergraduates can quickly relate to this format, and find it useful and worth considering for their further projects." (§5.6, p.195)

"even first-year undergraduates"的措辞强调了模式的"低门槛"——如果连大一学生都能在15分钟内理解并使用模式，那么任何设计团队成员也都能。这是一种"能力门槛"的论证策略。

---

## 八、实体清单（六类每类≥3+L###）

### L### 8.1 人物实体

| 编号 | 姓名 | 出现位置 | 角色 | L### |
|------|------|---------|------|------|
| 1 | Austin Henderson | §5.2 | Rivendel Consulting — Writer's Workshop评审者之一，提供了关键的格式肯定("looks exactly like Alexander's patterns") | L###501 |
| 2 | Karri-Pekka Laakso | §5.2 | University of Helsinki — 评审者，指出评级帮助读者判断有效性 | L###502 |
| 3 | Victor Lombardi | §5.2 | Razorfish, New York — 评审者，提供了最详细的正面和建设性评论 | L###503 |
| 4 | Carol Strohecker | §5.2 | MERL (Mitsubishi Electric Research Lab) — 评审者，关注插图和手绘图的对应关系 | L###504 |
| 5 | Yongmei Wu | §5.2 | Darmstadt University of Technology — 评审者，提供了总结性陈述 | L###505 |
| 6 | Max Mühlhäuser | §5.4 | 作者在Darmstadt的导师和合作者 — "The Conference/Classroom of the Future"项目的领导 | L###506 |
| 7 | Matthias Dannenberg | §5.5 | University of Ulm硕士生 — Interactive Fugue项目的执行者，撰写了以模式方法为基础的硕士论文 | L###507 |
| 8 | Martijn van Welie | §5.8 | HCI模式研究者 — 开发了第一个面向UI设计模式的XML结构定义，Borchers在其基础上改进 | L###508 |

### L### 8.2 文献实体

| 编号 | 文献 | L### |
|------|------|------|
| 1 | Borchers. "WorldBeat: Designing a baton-based interface..." (CHI 1997) | L###509 |
| 2 | Borchers & Mühlhäuser. "Design patterns for interactive musical systems" (IEEE Multimedia 1998) | L###510 |
| 3 | Borchers. "CHI meets PLoP" (SIGCHI Bulletin 2000a) | L###511 |
| 4 | Borchers et al. CHI 2000 Workshop report | L###512 |
| 5 | Borchers et al. INTERACT'99 Workshop report | L###513 |
| 6 | Tidwell. "Interaction Design Patterns" / Common Ground (1998) | L###514 |
| 7 | Nielsen. Usability Engineering (1993) | L###515 |
| 8 | Dannenberg. "Die Interaktive Fuge" (Master's Thesis, University of Ulm, 1999) | L###516 |
| 9 | van Welie. "A structure for usability based patterns" (CHI 2000 Workshop position paper) | L###517 |
| 10 | Ishii & Ullmer. "Tangible Bits" (CHI 1997) | L###518 |
| 11 | Underkoffler & Ishii. "Urp" (CHI 1999) | L###519 |
| 12 | Streitz et al. "i-LAND" (CHI 1999) | L###520 |
| 13 | Norman. The Psychology of Everyday Things (1988) | L###521 |
| 14 | Lee, Garnett & Wessel. "An adaptive conductor follower" (ICMC 1992) | L###522 |
| 15 | Zellweger et al. "The impact of fluid documents" (CHI 2000) | L###523 |

### L### 8.3 系统/产品实体

| 编号 | 名称 | L### |
|------|------|------|
| 1 | WorldBeat (评估对象) | L###524 |
| 2 | Interactive Fugue (模式重用的首个验证案例) | L###525 |
| 3 | Personal Orchestra (模式在商业项目中的使用案例) | L###526 |
| 4 | Virtual Vienna (设计会议中使用模式的案例) | L###527 |
| 5 | PET (Pattern Editing Tool — 原型设计) | L###528 |
| 6 | WorldBeat Musical Design Patterns组件 (groove slider的用户观察) | L###529 |
| 7 | Apple Power Macintosh 8500/120 (WorldBeat的计算机平台) | L###530 |
| 8 | Buchla Lightning II (红外线空间MIDI控制器) | L###531 |
| 9 | MAX (Opcode Inc.) (WorldBeat的软件开发平台) | L###532 |
| 10 | Urp / Tangible Bits (MIT Media Lab) | L###533 |

### L### 8.4 概念实体

| 编号 | 概念 | L### |
|------|------|------|
| 1 | Writer's Workshop (模式评审的同行方法) | L###534 |
| 2 | 多点三角测量 (Multi-point Triangulation) — 本章暗含的方法论策略 | L###535 |
| 3 | 超文本模式模型 (Hypertext Pattern Model — PL = (℘, ℜ) → 超文本数据结构) | L###536 |
| 4 | 模式内容块 (Pattern Content Block) — 多媒体容器概念 | L###537 |
| 5 | 跨平台工具设计 (Cross-platform Tool Design — XML + Java Applet) | L###538 |
| 6 | 教学有效性 (Didactic Usefulness) | L###539 |
| 7 | 企业记忆 (Corporate Memory) — 在§5.5中通过模式重用实际验证 | L###540 |
| 8 | 可转移性 (Transferability — 从Blues到Fugue的领域模式迁移) | L###541 |
| 9 | 通用MIDI (General MIDI) | L###542 |
| 10 | 手势识别 (Gesture Recognition — Lightning II内置) | L###543 |

### L### 8.5 机构实体

| 编号 | 名称 | L### |
|------|------|------|
| 1 | Ars Electronica Center (AEC), Linz — WorldBeat的安装和评估地 | L###544 |
| 2 | HOUSE OF MUSIC VIENNA (Haus der Musik Wien) | L###545 |
| 3 | Techniek Museum Delft (WorldBeat 1998年展出地) | L###546 |
| 4 | University of Linz (Telecooperation Research Group) | L###547 |
| 5 | University of Ulm (Interactive Fugue项目所在地) | L###548 |
| 6 | University of Darmstadt (Borchers的德国研究基地之一) | L###549 |
| 7 | MIT Media Lab | L###550 |
| 8 | IFIP (International Federation of Information Processing) — HCI Design Patterns Task Group, 2000年成立 | L###551 |

### L### 8.6 技术实体

| 编号 | 名称 | L### |
|------|------|------|
| 1 | MIDI (Musical Instruments Digital Interface) | L###552 |
| 2 | XML (Extensible Markup Language — PET的数据格式基础) | L###553 |
| 3 | Java Applet (PET的图形化界面技术) | L###554 |
| 4 | General MIDI (GM) Sound Module (Lightning基座中内置) | L###555 |
| 5 | Roland pitch-to-MIDI converter | L###556 |
| 6 | URL-based pattern addressing (PET的寻址机制) | L###557 |

---

## 九、与前后章关联

### L### 9.1 与Ch.4的关联

- Ch.4的DOMAIN-APPROPRIATE DEVICES (H11) → §5.2的完整同行评审 → 展示了"模式写完后发生了什么"的完整生命周期
- Ch.4的HCI模式语言 → §5.5的重用案例 → 15个模式被Interactive Fugue使用，各模式被Personal Orchestra/Virtual Vienna的设计会议使用
- Ch.4的音乐模式M9 (TRIPLET GROOVE) → §5.4.5的用户观察 → "在几秒内理解groove概念"——模式M9转化为交互式软件对象的效果

### L### 9.2 与Ch.3的关联

- Ch.3 §3.1的形式模型 → §5.8的超文本模型 → 从数学定义到软件数据结构
- Ch.3 §3.2的生命周期嵌入 → §5.5中模式在设计会议的不同阶段被使用
- Ch.3 §3.4的十个成分定义 → §5.2的同行评审针对具体成分（格式、内容、名称等）
- Ch.3 §3.3的时间维度 → §5.1中确认"Design dimension coverage"满足要求

### L### 9.3 与Ch.2的关联

- Ch.2 §2.6的六项需求 → §5.1的逐一对照
- Ch.2 §2.3的CHI 2000 Workshop → §5.3的格式对比
- Ch.2 §2.1的Writer's Workshop方法 → §5.2的实践应用
- Ch.2分析过的Alexander/Gamma/Tidwell集合 → §5.1中被用作not满足全部需求的反例

### L### 9.4 与Ch.6的关系

Ch.5是最后一次详细的论证——Ch.6只是简短的总结。这反映了一个写作理念：**论证在Ch.5完成后实质上已经结束了**，Ch.6只是形式上收尾。这种安排与大多数学术著作（总结章往往是长篇大论）形成对比——Borchers选择在论证密度最高点收束，然后以极简的方式告别。

---

*本报告根据 Jan Borchers: 《A Pattern Approach to Interaction Design》Chapter 5 (pp.169-201) 细读撰写。*
