# 02_第二章 Design Pattern Languages 分析报告

---

## 一、章节定位与功能

### L### 1.1 章节定位

本章（pp.9-49，约40页）是全书最长的理论性章节，承担"历史资源梳理"和"研究基础铺设"的功能。它位于Ch.1（问题诊断）之后、Ch.3（理论框架构建）之前，是全书论证链中从"现有问题的确认"到"新方案的提出"之间的桥梁。本章也是全书文献引用密度最高的章节——涵盖从1977年（Alexander）到2000年（CHI 2000 Workshop）的几乎所有HCI模式相关文献。

### L### 1.2 核心功能

1. **谱系建构功能**：将模式思想从文艺复兴建筑手稿→Alexander→软件工程→HCI的演进史完整呈现，确立本书的学术合法性。

2. **批判性遗产梳理功能**：不仅罗列历史，更对每一阶段的模式实践进行价值判断——特别是指出软件工程模式的"异化"（丢失了Alexander的使用者赋权精神）以及HCI模式的"更自然的亲缘性"。

3. **需求定义功能**：在分析现有模式集合的基础上，§2.6提出六项跨学科模式语言框架的要求（Requirements），为Ch.3的框架设计提供了"规格说明书"。

4. **共同体地图绘制功能**：详述1997-2000年间CHI、INTERACT、PLoP三大会议系列中的所有相关Workshop和个体研究者的工作——这既是文献综述，也是学术共同体的人际网络图。

---

## 二、结构分析

### L### 2.1 内部结构（六节递进）

```
§2.1 Pattern Languages in Architecture (约13页)
    ├── 文艺复兴溯源: Francesco di Giorgio (1439-1501)
    ├── Alexander的核心理念: Quality Without a Name, Forces, Unfolding
    ├── 两个完整模式实例: STREET CAFE, SITTING WALL
    └── 模式结构分析: 三大部分+隐式排版规则

§2.2 Pattern Languages in Software Engineering (约5页)
    ├── Beck & Cunningham (1987): 第一次软件模式实验 → 实际是UI设计!
    ├── GoF (1995): 模式格式的规范化, 但"不是Alexandrian意义上的模式语言"
    └── Alexander's OOPSLA'96 keynote: 对软件模式的批评

§2.3 Pattern Languages in HCI (约17页)
    ├── Early references (pre-1997): Norman, Apple, Barfield et al.
    ├── CHI'97 Workshop: Activity Patterns vs Design Patterns
    ├── Tidwell (1998): 最全面的HCI模式语言——详细分析
    ├── ChiliPLoP'99: 第一次软件工程+HCI模式共同体直接接触
    ├── INTERACT'99: 用户中心定义+按尺度的分类法
    └── 模式实例: DESCRIPTION AT YOUR FINGERTIPS

§2.4 Pattern Languages in Other Disciplines (约5页)
    ├── 心理学: Barsalou的认知理论解释为什么模式有效
    ├── PSA (Granlund & Lafrenière): 业务领域模式
    └── UPA'99: Alexandrian模式 vs Information模式

§2.5 A Comparison of Central Pattern Collections (约1页)
    └── 对比表: Alexander vs Gamma vs Tidwell

§2.6 Pattern Language Framework Requirements (约3页)
    └── 六项需求规格: 为Ch.3的框架设计制定标准
```

### L### 2.2 结构特征

1. **历史-架构-比较-规范**四段式：§2.1-2.4是历史梳理（纵向），§2.5是横向比较，§2.6是向后看的规范定义——整章形成了一条从"描述过去"到"定义未来"的弧线。

2. **四领域并列**：Architecture → Software Engineering → HCI → Other Disciplines——四节的结构表面上平行，但内在的逻辑关系是"源头→偏离→回归→推广"。

3. **§2.3的嵌套结构**：HCI一节内部自身就是一个微型Ch.2——也有"早期引用→近期研究→会议→模式实例→定义/分类法"的递进。这种"分形"式的结构组织使HCI一节在保持与整章结构一致的同时拥有内部深度。

---

## 三、内容分析（核心论题+关键论点案例）

### L### 3.1 核心论题

本章的论证可以还原为四个递进命题：

1. **溯源性命题**：模式思想是一项具有文艺复兴渊源的设计知识管理传统，Alexander将其系统化为"模式语言"这一强大形式。

2. **偏离性命题**：软件工程虽然借鉴了模式格式，但却丢失了Alexander原初思想中最核心的部分——让使用者/居民能够参与设计并为自己创造美好环境的人本主义精神。

3. **亲缘性命题**：HCI设计比软件设计更自然地接近建筑的处境——因为两者都涉及"人类在环境中的体验质量"和"空间/时间的配置"，而且HCI甚至多了一个时间的维度。

4. **规范性命题**：现有模式集合（包括HCI领域）不能充分满足跨学科交互系统设计的需求，需要一个满足六项要求的新框架。

### L### 3.2 §2.1 建筑模式语言：关键论点

**论点1：模式思想可追溯到文艺复兴时期的设计知识收集传统。**
- 证据：Francesco di Giorgio (1439-1501)的手稿《Tratato I》——以草图+文字解释的形式系统记录建筑设计解决方案——Borchers称之为"第一个设计模式"。
- 意义：将模式思想的历史从Alexander(1970s)上溯至文艺复兴(1480s)，赋予其超越Alexander的学术深度。

**论点2：Alexander的模式具有统一的隐式结构。**
- 通过完整引录和详细分析STREET CAFE（Pattern 88）和SITTING WALL（Pattern 243），Borchers展示Alexander模式的十大组成部分：Name → Ranking → Picture → Context → Problem Statement → Problem Description (with Forces) → Solution → Diagram → References。
- 关键洞察：Alexander通过严格的排版规则（小大写、粗体、三个星号、省略号、"Therefore:"提示词等）实现了结构的显式表达，而无需使用"Context:"、"Solution:"这样的文本标签——"implicit structuring through typography"。

**论点3：Alexander的核心理念是"赋权于使用者"。**
- Alexander认为好环境的好空间模式主要是由居民而非建筑师创造的——模式语言旨在将这些隐性知识显性化，"remind us of what we know already"。
- "the language, and the processes which stem from it, merely release the fundamental order which is native to us"——模式是提示工具而非教条。

### L### 3.3 §2.2 软件工程模式：偏离与批评

**关键论断：第一个软件模式实验实际上涉及UI设计。**
- Beck & Cunningham (1987)的OOPSLA报告——教非程序员用5个模式设计Smalltalk UI——这既是软件模式的起点，也是模式用于HCI的最早实验。Borchers据此指出模式方法从一开始就与UI设计有关联。

**核心批评：GoF模式丢失了Alexander的核心理念。**
- GoF的《Design Patterns》(1995)是"generally regarded as the archetype of a software patterns book"，但Borchers认为它有三重缺陷：
  1. 链接不完整，"the collection...is not complete enough to be a language"
  2. 许多模式不是经验的提炼而是"workarounds to implement object-oriented concepts despite the shortcomings of today's programming languages"
  3. 最关键的是"they are not written with the idea of empowering users to participate in the design process in mind"

**Alexander的审判（OOPSLA'96 Keynote）：**
> "Now, my understanding of what you are doing with patterns... It is a kind of a neat format, and that is fine. The pattern language that we began did have other features, and I don't know whether those have translated into your discipline."

Borchers将这句话放在§2.2末尾，将Alexander的批评用作整节的裁决——"a neat format"（一个漂亮的格式）这个措辞在Borchers笔下获得了反讽的暗示：你们拿走了格式，丢了精神。

### L### 3.4 §2.3 HCI模式：回归本源

**发现1：HCI对模式思想的引用早于软件工程。**
- Norman & Draper (1986), Norman (1988), Apple (1992)都引用了Alexander——而软件工程中第一个广为人知的引用是OOPSLA 1987。
- 这个时间顺序被Borchers用来支撑"模式思想更自然地适用于HCI"的论断。

**发现2：Barfield et al. (1994)的教学实践是关键先例。**
- Utrecht School of the Arts的交互设计课程以模式概念为核心——将模式定义为"three-part rules with context, forces, and configuration"。
- 他们还指出交互设计与建筑的一个关键不同：**时间是一个重要维度**——界面在交互过程中会大幅变化，而建筑基本不变。这个观点被Borchers采纳为Ch.3中时间维度的理论基础。

**核心论断：**
> "The notion of design patterns, as it was intended in architecture, carries over more naturally to user interface design than it does to software design." (p.30)

——这是全书最关键的单句断言之一。它不仅为HCI模式的正当性提供哲学基础，也为Borchers在整个模式共同体中赋予HCI一个"特权地位"：HCI比软件工程更忠于Alexander的原意。

**对Tidwell (1998)的深度分析：**
Borchers对Tidwell的《Common Ground》模式集合给予全书最正面的评价——"the most comprehensive effort in this field"——但也不回避其弱点：
- 正面：50+模式、层级化组织、接近Alexandrian精神、"represents timeless principles of good interaction design"
- 弱点：有些模式尚未详述、"the pattern format is not always kept consistent"、最近未更新

选择GO BACK TO A SAFE PLACE作为引用实例（而非更技术性的模式），暗示Borchers对Tidwell最欣赏的是其"更接近人类体验"的模式。

### L### 3.5 §2.4 其他学科模式：拓展视野

本节的功能是证明"模式可以描述任何领域的知识"——为Ch.4将音乐知识模式化提供先例：
- Casaday (1997): 模式在军事理论、神话学、甚至基础写作（templates）中都有对应物
- Denning & Dargan (1996): Pattern Mapping作为一种跨学科软件设计方法
- Granlund & Lafrenière (1999b): Pattern-Supported Approach (PSA)用于描述业务流程

### L### 3.6 §2.5 比较表

图2.5的对比表是全章唯一跳脱文字叙事的视觉结构——将Alexander, Gamma, Tidwell按Domain, Components, Format, Uniformity四维度排列。结果显示了"a high level of agreement on how a pattern language should be structured"——这为Ch.3的统一格式提供了"共同体已有共识"的合法性。

### L### 3.7 §2.6 六项要求

1. **Cross-discipline readability**：非专业人士也能读懂的散文格式（而非速记列表）
2. **Domain-independent, uniform, well-defined format**：格式在所有领域中一致且被形式化定义
3. **Empirical evidence**：包含已发布的实证研究
4. **Domain-appropriate, design-supporting hierarchy**：层级结构反映该领域的设计过程，从顶向下"展开"
5. **Design dimension coverage**：涵盖该领域所有相关维度（包括空间和时间）
6. **Lifecycle integration**：指定如何将模式语言集成到软件开发生命周期中

Borchers随后用这个要求清单评估Alexander、Gamma和Tidwell的集合——没有任一集合满足全部六项。这个"需求缺口"直接为Ch.3的方案铺路。

---

## 四、逻辑梳理（论证链条+因果转折）

### L### 4.1 整章论证链

```
§2.1: 建筑模式
    Alexander创造了强大的模式语言概念
    + 隐式结构 + 统一格式 + 设计层次
    + 核心理念: 赋权于使用者, QWAN, piecemeal growth
            ↓
§2.2: 软件模式
    借鉴了模式格式(名称、结构、链接)
    BUT 丢失了赋权精神、使用者参与、QWAN的价值关怀
    → 成为一种"工程师写给工程师"的技术工具
            ↓
§2.3: HCI模式
    (a) HCI最早引用模式思想(早于软件工程)
    (b) HCI比软件更接近建筑的处境
         → 都涉及人类在环境中的体验
         → HCI甚至多了时间维度
    (c) 但HCI模式研究仍处于早期阶段
         → 格式不统一、缺乏层级化、无生命周期整合
            ↓
§2.4: 其他领域模式
    模式可以描述任何"设计型"活动
    BUT 有些"模式"缺乏问题和解决方案结构
            ↓
§2.5: 对比表
    Alexander, Gamma, Tidwell 有高度共识的结构元素
            ↓
§2.6: 六项要求
    ≠ 现有任何单一集合都满足
    → 需要一个新的跨学科框架
    → Ch.3将构建此框架
```

### L### 4.2 重要的因果转折

1. **从"描述"到"规范"的转折点**：§2.5对比表——这个看似中立的表格实质上是全章的转向铰链。此前四节是在"描述"三个领域中发生了什么，此后§2.6是在"定义"应该做什么。表格通过展示"已有的共识"和"各自的不足"同时发生，自然导出规范定义的需要。

2. **Alexander的位置变化**：在§2.1中Alexander是"被解释的对象"（历史人物），在§2.2末尾他是"审判者"（对软件模式的批评者），在§2.3中他是"标准制定者"（HCI被论证为更接近其原意），在§2.5-2.6中他是"基准线"（始终满足可读性和统一格式要求，但缺乏实证证据和非空间维度）。Alexander在不同节中的不同角色，折射出Borchers论证策略的灵活性。

3. **"时间"概念的渐进导入**：§2.1中指出Alexander的模式只处理空间（"This simple organizing principle ignores one major dimension: time"的伏笔），§2.3中Barfield et al.提出"interaction is much more dynamic, and context and system of forces often change during the course of interaction"，INTERACT'99 Workshop明确将"physical dimension"区分为spatial, sequence, continuous time——"时间"作为设计维度从"被忽略"到"被注意"到"被正式分类"，逐步上升为Ch.3的核心贡献之一。

---

## 五、材料使用方式

### L### 5.1 引文的层级使用

Borchers使用三种不同性质的引文：

1. **全录式引文（Verbatim Reproduction）**：STREET CAFE（Pattern 88, pp.14-15）和SITTING WALL（Pattern 243, pp.16-17）——两个Alexander模式被几乎完整地转录。这是全书唯一一次大规模转录外部文本。为什么选这两个？STREET CAFE是"大尺度"模式（城市/社区规划级别），SITTING WALL是"小尺度"模式（建筑构件级别），两者合在一起展示了模式语言的层级范围。同时两者都排在"两星"（最高置信度），传递了"真正的好模式是什么样子"的范本。

2. **功能式引用（Functional Citation）**：GoF的《Design Patterns》被引用为"what a widely accepted software pattern collection looks like"——不是在讨论其内容，而是在讨论其"作为模式集合"的性质。

3. **对话式引用（Dialogical Citation）**：Tidwell (1998)的模式GO BACK TO A SAFE PLACE被全文转录并分析其组成部分和优缺点——Borchers在"与Tidwell对话"而非"引用Tidwell"。

### L### 5.2 研讨会的"参与式记录"

§2.3对ChiliPLoP'99和INTERACT'99两次研讨会的描述具有双重性质——既是"第三人称的文献综述"（客观记录），又是"第一人称的参与记忆"（作者本人在场）。这种"自己是文献的一部分"的处境在学术写作中需要技巧性处理——Borchers通过以下策略平衡：

- 在讨论自己参与的部分时使用客观化语言："the workshop turned out..."、"the workshop agreed on..."
- 将自己提出的概念（如INCREMENTAL REVEALING模式、图2.4的分类法）放入"共同体的成果"中讨论，而非单独强调为个人贡献
- 在引用自己的出版物时才使用第一人称："has been described in more detail in [Borchers, 1999]"

### L### 5.3 表格的战略使用

图2.5对比表是全章唯一跳出文字叙事的元素。它在视觉上建立了一个"客观事实"的假象——用表格形式将三个模式集合的比较呈现为无可争议的"数据"。表格中Tidwell一行的Uniformity标记为"+"（好但不是最好），Alexander和Gamma都是"++"（最高分）——这个评级暗示了Borchers对现有HCI模式工作"仍有改善空间"的判断，但以看似客观的表格形式降低了判断的主观感。

---

## 六、论辩与阐述方法

### L### 6.1 系谱学方法（Genealogical Method）

本章最显著的论证策略是建立一条完整的"模式思想系谱"：
```
Francesco di Giorgio (1480)
    → Alexander (1977/1979)
        → Beck & Cunningham (1987) [软件工程分支]
            → GoF (1995)
        → Norman (1986/1988) [HCI分支]
            → Barfield et al. (1994)
                → Bayle et al. (1997)
                    → Tidwell (1998)
                        → Borchers (2001) [← 本书在此]
```

这个系谱不仅证明模式思想的历史合法性，更重要的是——通过追溯HCI分支独立于软件工程分支的发展——为HCI模式的相对自主性（autonomy）提供历史证据。

### L### 6.2 比较-对照方法（Compare-and-Contrast）

本章使用两种层面的比较：
1. **跨领域横向比较**：Architecture vs Software Engineering vs HCI vs Other Disciplines
2. **同领域内纵向比较**：在HCI内部——Norman(1986) vs Barfield(1994) vs Bayle(1997) vs Tidwell(1998) vs INTERACT'99

跨领域比较产生了关于差异性的论断（"HCI比软件更接近建筑"），同领域内比较产生了关于发展趋势的论断（"HCI模式正在成熟但仍有不足"）。

### L### 6.3 辩护式论证（Apologetic Argumentation）

对Alexander在OOPSLA'96上的批评，Borchers的回应策略是**将批评转化为支持HCI模式立场的论据**：

- Alexander批评软件模式只借用了格式 → Borchers说："Exactly! 这正是为什么我们需要一个更忠于Alexander精神的HCI模式方法"
- 软件模式丢失了"under what circumstances is the environment good"的关怀 → Borchers说："这就是HCI模式可以恢复的东西"

这实质上是将Alexander对软件模式的"否定"重新解释为对HCI模式的"潜在肯定"。

### L### 6.4 包容性论证（Inclusiveness Argumentation）

即使Borchers明显倾向于Alexander式的模式方法，他对所有现存方法都保持学术性的尊重：
- 对GoF：承认其巨大的影响力和格式的规范化贡献
- 对Tidwell：详细分析其优点，使批评更具建设性
- 对"Activity Patterns"（CHI'97 Workshop）：承认其在组织模式中的适用性

这种包容性避免了"教条主义"的指责，同时使最终提出的框架呈现为"对现有工作的综合和超越"而非"对现有工作的否定"。

---

## 七、语言文风（原文摘录+L###）

### L### 7.1 整体风格

本章的学术英语在论述性质上介于"历史叙事"和"批判分析"之间：
- 描述历史时：流畅的叙事，倾向于使用较长的段落和过渡语句
- 进行批判时：密集的概念浓缩，频繁使用"However"、"nevertheless"、"whereas"等转折词
- 引用原文时：保留被引文字的原始风格（Alexander的优雅散文、GoF的技术风格、Tidwell的实践导向）

### L### 7.2 代表性原文摘录

#### L### 7.2.1 文艺复兴溯源——一个战略性开场

> "During the renaissance age, architecture, like many other sciences and arts, experienced one of its prime ages. A major key for this revolution was the fact that 'master builders' of that time were beginning to systematically collect, document, and structure architectural design knowledge. A particularly prominent example was master builder Francesco di Giorgio (1439–1501), who led such an effort in Siena. The central ingredient of his documents was the sketch of a successful design solution, supported by textual explanations, which essentially led to a new literary form, the first 'design pattern'." (§2.1, pp.9-10)

这是Borchers为模式思想所做的历史溯源——将"第一个设计模式"定位于1480年的意大利锡耶纳，而非1970年代伯克利的Alexander。这种溯源远远超出了学术综述的需要，其功能在于：
- 将模式思想与文艺复兴的人文主义传统挂钩（而非仅仅是20世纪的系统思维）
- 暗示Alexander不是发明了模式，而是复兴了模式，正如文艺复兴复兴了古典文化
- 为自己的框架赋予超越当代技术话语的历史合法性

"a new literary form"这一措辞将模式描述为一种文学体裁/形式创新——这与全书强调"人类可读性"是一脉相承的。

#### L### 7.2.2 对Alexander模式的排版分析——元层面的细读

> "Alexander's patterns do not contain explicit text tags for each part of each pattern: there is no label saying 'Context:', or 'Solution:'. Though this may seem at first as if this structuring is missing, looking at the patterns more closely reveals that this structural information is communicated implicitly, using very rigid rules of typography." (§2.1, pp.20-21)

这是全书方法论自觉最密集的段落之一。Borchers在这里展示了对"形式的元分析"——不是读模式的内容，而是读模式的排版规则所传达的结构信息。接下来他分析了六条排版规则（小大写→★→照片→省略号→粗体→"Therefore:"→手绘图→星号分隔→省略号引用），将Alexander的视觉排版解构为一个"沟通协议"。

这种分析的学术原创性在于：不是将模式作为一个"文本类型"来接受，而是将其"形式"本身作为分析对象，从中提取可推广的设计原则。这直接为Ch.3中"隐式结构vs显式标签"的讨论提供了分析基础。

#### L### 7.2.3 核心断言——HCI比软件更适合模式

> "The notion of design patterns, as it was intended in architecture, carries over more naturally to user interface design than it does to software design." (§2.3, p.30)

这个句子看似简单，但内含一个精巧的论证结构：
- "as it was intended in architecture"——限定为Alexander原意的模式概念
- "more naturally"——暗示存在一个自然的匹配度，HCI > 软件工程
- 隐含前提：软件的"内部结构"不直接构成"人类体验的环境"——软件工程师在高抽象层次上工作，而HCI设计师为用户创造可直接体验的数字环境

这句话的论证力量依赖于前面12页对Alexander的详细解读——读者已经内化了"什么是Alexander意义上的模式"，所以此时"more naturally"的判断不需要再展开证明。

#### L### 7.2.4 Alexander对软件模式的批评——被征用的权威

> "Now, my understanding of what you are doing with patterns... It is a kind of a neat format, and that is fine. The pattern language that we began did have other features, and I don't know whether those have translated into your discipline. I mean, there was at root behind the whole thing a continuous mode of preoccupation with under what circumstances is the environment good. In our field that means something." (Alexander, OOPSLA'96 keynote, cited on p.26)

Borchers对此引文的处理展现了精心的修辞控制：
1. 完整转录以保持引文力度（而非截取关键句）
2. 引文包含Alexander的犹豫和不完整句（"...It is a kind of a neat format..."）——使批评更具真实性而非攻击性
3. Alexander最后的"In our field that means something"——暗示在你们的领域（软件工程），这种关怀并不自然存在
4. Borchers将这段引文放在§2.2末尾、§2.3开始之前——在结构上充当从"软件模式的偏离"到"HCI模式的回归"的桥梁

#### L### 7.2.5 对Tidwell的平衡评价

> "Tidwell's pattern collection is currently the most promising effort to create an HCI pattern language. While it has a few weaknesses (several of its patterns have not been detailed yet, the pattern format is not always kept consistent, and the collection has not been updated in recent months), it has already served as a frequently quoted example of what an HCI pattern language could look like." (§2.3, p.36)

括号内的三个弱点以从句形式嵌入，不打断主句的赞扬语气——这是一个"赞扬为主、批评为辅"的修辞结构。更值得注意的是，Borchers对Tidwell整体上非常正面——因为Tidwell的集合是最接近Alexander理想（经验驱动的、层级化的、不绑定特定工具包的）的HCI模式集合。这使Tidwell成为Borchers在学术上最亲密的"盟友"和"前驱"。

---

## 八、实体清单（六类每类≥3+L###）

### L### 8.1 人物实体

| 编号 | 姓名 | 出现位置 | 角色 | L### |
|------|------|---------|------|------|
| 1 | Christopher Alexander | §2.1核心 | 建筑模式语言创始人——§2.1以Alexander为中心构建，其两项核心著作和两个完整模式实例构成了该节的血肉 | L###201 |
| 2 | Francesco di Giorgio (1439-1501) | §2.1开头 | 文艺复兴锡耶纳建筑大师——被追溯为"第一个设计模式收集者"，提供超出Alexander的历史深度 | L###202 |
| 3 | Erich Gamma / Richard Helm / Ralph Johnson / John Vlissides | §2.2核心 | "Gang of Four"——1995年《Design Patterns》合著者，代表软件模式运动的最高成就但也代表其限度 | L###203 |
| 4 | Kent Beck / Ward Cunningham | §2.2开头 | OOPSLA 1987最早将模式引入软件工程的报告——值得注意的是这实际上是UI设计实验 | L###204 |
| 5 | Jenifer Tidwell | §2.3核心小节 | 《Common Ground》HCI模式集合的作者——被Borchers视为"目前最有希望的HCI模式努力" | L###205 |
| 6 | Donald A. Norman | §2.3开头 | HCI经典作者——1986年首次在HCI文献中引用Alexander，Borchers据此论证HCI对模式的早期接纳 | L###206 |
| 7 | Lon Barfield et al. | §2.3 | Utrecht School of the Arts的交互设计课程负责人——1994年以模式概念改革课程，Borchers引为重要先例 | L###207 |
| 8 | Tom Erickson | §2.3 | IBM/HCI研究员——推动"交互模式"向人类-人类交互方向发展的关键人物，CHI'97 Workshop核心组织者 | L###208 |
| 9 | Elisabeth Bayle et al. | §2.3 | CHI'97 Workshop报告合著者——首次系统区分模式的五种使用方式（Capture, Generalization, Prescription, Rhetoric, Prediction） | L###209 |
| 10 | Åsa Granlund / Daniel Lafrenière | §2.4 | PSA方法创始人——用模式描述业务流程；提出Alexandrian模式 vs Information模式的关键区分 | L###210 |
| 11 | Peter Denning / Pamela Dargan | §2.4 | 提出"Pattern Mapping"作为跨学科软件设计方法——Borchers引用以支持模式的跨学科价值 | L###211 |
| 12 | George Casaday | §2.4 | 论证模式在军事理论/神话学/写作模板中的普遍对应——Borchers引用以支持"模式可以描述任何领域的知识" | L###212 |
| 13 | Martijn van Welie | §2.3 | HCI模式研究者——其"What's For Dinner?"模式名称被用作"过于隐喻、意义模糊"的反例 | L###213 |
| 14 | Frank Buschmann | (Series Foreword) | Siemens架构师/模式丛书主编——其序言将Borchers与Alexander的"赋权于民"理念对标 | L###214 |

### L### 8.2 文献实体

| 编号 | 文献 | L### |
|------|------|------|
| 1 | Alexander et al. A Pattern Language: Towns, Buildings, Construction (1977) | L###215 |
| 2 | Alexander. The Timeless Way of Building (1979) | L###216 |
| 3 | Alexander et al. The Oregon Experiment (1988) | L###217 |
| 4 | Gamma et al. Design Patterns: Elements of Reusable Object-Oriented Software (1995) | L###218 |
| 5 | Beck & Cunningham. "Using pattern languages for object-oriented programs" (1987) | L###219 |
| 6 | Tidwell. "Interaction design patterns" / Common Ground (1998) | L###220 |
| 7 | Norman & Draper. User-Centered System Design (1986) | L###221 |
| 8 | Norman. The Psychology of Everyday Things (1988) | L###222 |
| 9 | Apple Computer. Macintosh Human Interface Guidelines (1992) | L###223 |
| 10 | Barfield et al. "Interaction design at the Utrecht School of the Arts" (1994) | L###224 |
| 11 | Bayle et al. "Putting it all together: Towards a pattern language for interaction design" (1998) | L###225 |
| 12 | Erickson. "Interaction pattern languages: A lingua franca for interaction design?" (1998) | L###226 |
| 13 | Borchers. "CHI meets PLoP: An interaction patterns workshop" (2000a) | L###227 |
| 14 | Borchers et al. INTERACT'99 & CHI 2000 workshop reports (2001) | L###228 |
| 15 | Granlund & Lafrenière. PSA papers (1999a, 1999b) | L###229 |
| 16 | Denning & Dargan. "Action-centered design" (1996) | L###230 |
| 17 | Casaday. "Notes on a pattern language for interactive usability" (1997) | L###231 |
| 18 | Riehle & Züllighoven. "Tools and Materials" pattern language (1995) | L###232 |
| 19 | Bradac & Fletcher. "A Pattern Language for Developing Form Style Windows" (1998) | L###233 |
| 20 | Rossi et al. Hypermedia navigation patterns (1996, 1997) | L###234 |

### L### 8.3 系统/产品实体

| 编号 | 名称 | L### |
|------|------|------|
| 1 | Mac OS (Balloon Help, Simple Finder) | L###235 |
| 2 | Microsoft Windows (Tool Tips) | L###236 |
| 3 | Netscape Navigator (URL display in status bar) | L###237 |
| 4 | Exploratorium, San Francisco (三段式展品标签) | L###238 |
| 5 | Kai's Power Show (展览化界面的桌面应用) | L###239 |

### L### 8.4 概念实体

| 编号 | 概念 | L### |
|------|------|------|
| 1 | 无名特质 (Quality Without a Name / QWAN) | L###240 |
| 2 | 力 (Forces) | L###241 |
| 3 | 渐次生长 (Piecemeal Growth) | L###242 |
| 4 | 展开过程 (Unfolding Process) | L###243 |
| 5 | 隐式结构 (Implicit Structuring through Typography) | L###244 |
| 6 | 模式语言的链接性 (Context/Reference Links) | L###245 |
| 7 | 交互设计模式 (Interaction Design Pattern) — ChiliPLoP'99定义 | L###246 |
| 8 | 活动模式 vs 设计模式 (Activity Pattern vs Design Pattern) | L###247 |
| 9 | 三层分类法 (Abstraction × Function × Physical Dimension) | L###248 |
| 10 | 按尺度的分类原则 (Scale-based Organizing Principle) | L###249 |
| 11 | 透明度 (Transparency) —— "QWAN的HCI对应物" | L###250 |
| 12 | 跨学科可读性 (Cross-discipline Readability) | L###251 |
| 13 | 信息模式 vs Alexandrian模式 (Information Pattern vs Alexandrian Pattern) | L###252 |
| 14 | 模式映射 (Pattern Mapping) | L###253 |
| 15 | 言语编码 (Verbal Recoding) — Miller (1956) | L###254 |

### L### 8.5 机构/事件实体

| 编号 | 名称 | L### |
|------|------|------|
| 1 | OOPSLA conference (Object-Oriented Programming, Systems, Languages & Applications) | L###255 |
| 2 | PLoP conference series (Pattern Languages of Programming) | L###256 |
| 3 | CHI conference (ACM Conference on Human Factors in Computing Systems) | L###257 |
| 4 | INTERACT conference (IFIP Conference on Human-Computer Interaction) | L###258 |
| 5 | ChiliPLoP conference | L###259 |
| 6 | UPA conference (Usability Professionals' Association) | L###260 |
| 7 | Utrecht School of the Arts (Netherlands) | L###261 |
| 8 | CHI'97 Workshop on HCI Patterns (Atlanta) | L###262 |
| 9 | ChiliPLoP'99 Workshop on Interaction Patterns (Wickenburg, AZ) | L###263 |
| 10 | INTERACT'99 Workshop on HCI Patterns (Edinburgh) | L###264 |
| 11 | CHI 2000 Workshop on Pattern Languages for Interaction Design (The Hague) | L###265 |

### L### 8.6 技术实体

| 编号 | 名称 | L### |
|------|------|------|
| 1 | C++ (GoF模式的实现语言背景) | L###266 |
| 2 | UML (统一建模语言——被提及为软件模式的可能图示方法) | L###267 |
| 3 | Smalltalk (Beck & Cunningham 1987实验所用的编程语言) | L###268 |

---

## 九、与前后章关联

### L### 9.1 与Ch.1的关联

Ch.1 §1.4仅用两句话概括模式语言的起源——Ch.2将此扩展到42页的详述。特别地：
- Ch.1提到模式语言"originated in urban architecture"——Ch.2 §2.1提供了完整的论证和实例
- Ch.1提到"although some of its basic aspects were lost in the process"——Ch.2 §2.2详细论证了"什么被丢失了"（使用者赋权的精神）
- Ch.1提到"extends the notion to HCI"——Ch.2 §2.3提供了已有的HCI模式研究的全景

### L### 9.2 与Ch.3的关联

Ch.2与Ch.3之间是全书最关键的"需求→方案"衔接：
- §2.6的六项要求是Ch.3的"输入规格"——Ch.3构建的框架逐一回应这些要求
- §2.1的"implicit structuring through typography"直接影响了Ch.3中对模式排版规则的讨论
- §2.3中关于"时间维度"的讨论在Ch.3 §3.3中成为独立一节
- §2.3中的三个分类法（抽象层级×功能×物理维度）为Ch.3的模式层级组织原则提供了参考

### L### 9.3 与Ch.4的关联

Ch.2的理论工作在Ch.4中被实例化：
- Alexander的隐式排版规则——Ch.4全文遵循
- Tidwell的GO BACK TO A SAFE PLACE与Ch.4的EASY HANDOVER和CLOSED LOOP有概念亲缘
- §2.3中的DESCRIPTION AT YOUR FINGERTIPS模式在Ch.4的DYNAMIC DESCRIPTOR(H15)中得到完整实现

### L### 9.4 与Ch.5的关联

§2.6的六项要求在Ch.5 §5.1中被用作评估标准。Ch.2中描述的Writer's Workshop评审方法在Ch.5 §5.2中被实际应用（DOMAIN-APPROPRIATE DEVICES的评审）。

---

*本报告根据 Jan Borchers: 《A Pattern Approach to Interaction Design》Chapter 2 (pp.9-49) 细读撰写。*
