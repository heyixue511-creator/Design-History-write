# 04_第四章 A Pattern Language for Interactive Music Exhibits 分析报告

---

## 一、章节定位与功能

### L### 1.1 章节定位

本章（pp.75-168，约93页）是全书篇幅最大的一章，承担"实例证明"功能。它位于Ch.3（理论框架构建）之后、Ch.5（多维度评估）之前。在全书结构中，本章是连接理论（Ch.1-3）和实践验证（Ch.5）的枢纽——它展示了Ch.3定义的形式框架如何在实际设计项目中"填充血肉"。

本章也是全书从"论证"模式转向"展示"模式的转折点——Ch.1-3是"关于模式"的论述（discourse about patterns），Ch.4是"模式本身"的呈现（patterns themselves）。

### L### 1.2 核心功能

1. **实例证明功能（Proof by Example）**：通过三套完整的模式语言（Music 11个 + HCI 17个 + Software 4个）证明Ch.3的跨学科模式框架的可行性和统一性。

2. **设计资源功能（Design Resource）**：HCI模式语言（17个模式）本身就是一个可直接用于交互式展览/公共信息亭设计的知识库——"The HCI pattern language should be useful to many readers in its own right"。

3. **跨界示范功能（Cross-Domain Demonstration）**：通过展示同一个形式框架如何同时应用于三个截然不同的领域（Blues音乐理论、交互设计、软件架构），证明框架的"领域无关性"。

4. **模板功能（Template Function）**：为未来的模式作者提供"如何以Alexandrian格式写模式"的范本——排版规则（小大写名称→星级→照片→省略号→粗体问题→"Therefore:"→粗体方案→手绘图→星号分隔→小模式引用）被严格遵循。

---

## 二、结构分析

### L### 2.1 顶层结构

```
Chapter 4
├── 章首引言 (Goethe: Faust) + 项目背景简介
├── §4.1 Musical Pattern Language (11个模式, M1-M11)
├── §4.2 HCI Pattern Language (17个模式, H1-H17)
└── §4.3 Software Pattern Language (4个模式, S1-S4)
```

### L### 2.2 §4.1 音乐模式语言内部结构

音乐模式的排序原则：**从"大尺度"到"小尺度"的时空范围 + 和声/旋律/节奏分组**

```
M1  BLUES STYLE              ← 全局: 选择Blues作为音乐风格
    ↓
M2  COMBO INSTRUMENTATION    ← 大尺度: 乐队编制
    ↓
M3  SOLO & COMPING *         ← 中尺度: 角色分配
    ↓
M4  TWELVE-BAR PROGRESSION * ← 和声组: 和弦进行
    ↓
M5  SIXTH AND SEVENTH CHORDS  ← 和声组: 和弦类型
    ↓
M6  CHORD TRANSITIONS         ← 和声组: 和弦过渡
    ↓
M7  PENTATONIC SCALE **       ← 旋律组: 音阶材料
    ↓
M8  BLUE NOTES **             ← 旋律组: 特殊音
    ↓
M9  TRIPLET GROOVE **         ← 节奏组: 摇摆感
    ↓
M10 WALKING BASS *            ← 节奏组: 低音线
    ↓
M11 BLUES TEMPO               ← 最具体: 速度
```

排序逻辑：从"选择什么风格"（最抽象）→"用什么乐器"→"什么和弦"→"什么音"→"什么节奏"→"多快"（最具体）。同时，M4-M6是和声维度，M7-M8是旋律维度，M9-M11是节奏维度。

### L### 2.3 §4.2 HCI模式语言内部结构

HCI模式的排序原则：**任务级→交互级→界面级→设备级**（按时空范围从大到小）

```
H1  ATTRACT-ENGAGE-DELIVER *     ← 整体交互模型
    ↓
H2  ATTRACTION SPACE *           ← 环境中的可见性
    ↓
H3  COOPERATIVE EXPERIENCE **     ← 多人共享体验
    ↓
H4  EASY HANDOVER *              ← 用户交接
    ↓
H5  SIMPLE IMPRESSION *           ← 系统整体印象
    ↓
H6  INCREMENTAL REVEALING **      ← 信息展开策略
    ↓
H7  FLAT AND NARROW TREE *        ← 导航结构设计
    ↓
H8  AUGMENTED REALITY *           ← 替代导航范式
    ↓
H9  CLOSED LOOP *                 ← 交互单元的闭环
    ↓
H10 LANGUAGE INDEPENDENCE         ← 国际化
    ↓
H11 DOMAIN-APPROPRIATE DEVICES *  ← 输入设备选择
    ↓
H12 INNOVATIVE APPEARANCE *       ← 外观吸引力
    ↓
H13 IMMERSIVE DISPLAY *           ← 显示规模
    ↓
H14 INVISIBLE HARDWARE *          ← 隐藏技术
    ↓
H15 DYNAMIC DESCRIPTOR **         ← 即时帮助
    ↓
H16 INFORMATION JUST IN TIME **   ← 使用说明的时机
    ↓
H17 ONE INPUT DEVICE *            ← 输入设备数量
```

### L### 2.4 §4.3 软件模式语言内部结构

```
S1 BRANCHING TRANSFORMER CHAIN   ← 整体架构: 数据流处理链
    ↓
S2 METRIC TRANSFORMER *          ← 子系统: 节奏变换
    ↓
S3 IMPROVISATION HELPER **       ← 子系统: 即兴辅助
    ↓
S4 MUSICAL EVENTS *              ← 基础: 数据表示格式
```

### L### 2.5 三个模式语言的规模安排

| 语言 | 模式数量 | 评级分布 | 功能 |
|------|---------|---------|------|
| 音乐 | 11个 | **×3, *×3, 无×5 | 捕捉应用领域知识——解释Blues的"设计空间" |
| HCI | 17个 | **×4, *×11, 无×2 | 捕捉交互设计经验——解释如何设计交互式展览 |
| 软件 | 4个 | **×1, *×2, 无×1 | 捕捉软件架构经验——解释如何构建交互音乐系统 |

数量差异不是因为"软件模式不重要"，而是因为(a)软件模式已有GoF等大量文献，Borchers只补充领域特定的那些；(b)HCI是本书的核心关注；(c)音乐模式是为了证明"领域知识可以模式化"的概念。

---

## 三、内容分析（核心论题+关键论点案例）

### L### 3.1 核心论题

本章的核心论题是：

> Ch.3定义的跨学科模式框架具有真正的跨领域实用性——同一套形式（Name, Ranking, Illustration, Context, Problem, Forces, Examples, Solution, Diagram, References）和同一套排版规则（Alexander的隐式结构）可以有效地表达三个截然不同领域（音乐理论、交互设计、软件架构）的设计知识，而且产生的模式语言具有内在的一致性和设计导向性（从大到小的展开层级）。

### L### 3.2 音乐模式语言分析（§4.1）

**核心论证：应用领域（如音乐）中的知识具有"设计"性质，可以用模式形式表达。**

**最精选的模式：M7 PENTATONIC SCALE （两星）**

- 问题："Just using the notes of the simple triad chords...is too simple for improvisation. But using all notes in the chromatic scale equally would remove the harmonic context completely."
- 力："too simple for improvisation" vs "would remove harmonic context" ——在"过于简单"和"失去和声语境"之间寻找平衡
- 解决方案：使用五声音阶（prime, second, third, fifth, sixth）作为即兴的"优先音集"
- 例子：Gershwin的"Nice Work If You Can Get It"的主旋律恰好使用G大调五声音阶(G, A, B, D, E)
- 意义：这是一个"设计问题"——给定一个即兴任务和某种材料的限制，什么是"最优"的音符选择？它不是"正确vs错误"的问题，而是"在这个约束下，什么方案工作得最好"

**最精彩的forces：M8 BLUE NOTES （两星）**

- 力1："The pure pentatonic scale does not create enough musical tension"（太协和=缺乏表现力）
- 力2："But not all other notes can be used to enrich the scale"（随意加音=破坏Blues风格）
- 力3：非洲音乐中使用的某些音"lie between the flat and natural notes...have no direct correspondence in the chromatic scale"（物理上无法在固定音高乐器上精确演奏）
- 解决方案：使用降3/降5/降7的中间音高，在无法精确演奏时"frequently sliding from the lower to the upper note"
- 意义：这展示了forces的丰富性——不仅是两股力的对抗，而是**三股力**的复杂平衡（张力不足vs风格破坏vs物理限制）。

### L### 3.3 HCI模式语言分析（§4.2）

**核心论证：交互式展览设计中的反复出现的成功解决方案可以被系统地捕获为模式语言。**

**关键模式1：H1 ATTRACT-ENGAGE-DELIVER （一星）——全语言的"根模式"**

- 定义了交互式展览的整体交互模型：吸引(Attract)→参与(Engage)→传达(Deliver)
- 灵感来源：Exploratorium的三段式展品标签（"To do and notice" / "What's going on?" / "So What?"）
- 这是时空范围最大的HCI模式——它定义了整个交互过程的叙事弧
- 引用关系：指向H2(ATTRACTION SPACE), H6(INCREMENTAL REVEALING), H9(CLOSED LOOP)三个子模式分别处理三阶段

**关键模式2：H6 INCREMENTAL REVEALING （两星）——全书评级最高的四个HCI模式之一**

- 问题：系统如果一开始看起来复杂→吓跑用户；但如果太简单→用户很快觉得无聊
- 解决方案：初始只展示简洁的功能概览→只有当用户表现出兴趣时才逐步揭示更深的内容
- 例子：Mac OS Finder只显示顶层文件夹→点击后展开子层级；WorldBeat主菜单只显示组件图标→鼠标靠近时出现说明→点击后进入功能页
- 两个揭示阶段：1) DYNAMIC DESCRIPTOR（鼠标悬停显示简述）2) 进入组件页（详情+交互）

**关键模式3：H11 DOMAIN-APPROPRIATE DEVICES （一星）——全书最受关注的模式之一**

- 核心主张：选择与系统应用领域中的真实物体相似的输入/输出设备
- 两个强有力的例子：
  1. Norman的汽车座椅调节器——形状就是微型座椅
  2. WorldBeat的红外线指挥棒——像指挥棒/木琴槌，而非键盘+鼠标
- 曾经包含在Ch.5的同行评审中（Writer's Workshop at CHI 2000），评审后改进

**关键模式4：H15 DYNAMIC DESCRIPTOR （两星）**

- 这个模式将Tidwell的SHORT DESCRIPTION和INTERACT'99 Workshop的DESCRIPTION AT YOUR FINGERTIPS整合并针对"展览场景"做了调整——因为展览的典型用户是"首次+单次"用户，所以描述需要自动激活（而非像Mac OS Balloon Help那样需要手动开启）
- 体现了一个关键的方法论原则：通用模式在应用到特定场景时需要适配

**关键模式5：H16 INFORMATION JUST IN TIME （两星）**

- 问题：展览用户不阅读长说明，更不记忆它们
- 观察证据："We noticed users usually only stopping to read when they actually did not know how to continue"
- 解决方案：延迟使用说明到用户"卡住"的那一刻——"no more than three sentences with twelve words each"——15个词的硬性上限
- 这是"经验驱动的模式"的最佳范例——方案直接来自对用户行为的观察，而非抽象推导

### L### 3.4 软件模式语言分析（§4.3）

**核心论证：交互音乐系统中有领域特定的软件架构模式——它们不需要UML图来表达，使用清晰文字+简单关系图即可让非工程师理解。**

**关键模式：S2 METRIC TRANSFORMER （一星）**

这个模式是全书最复杂的单个模式——占用了约4页篇幅。它定义了一个包含六个协作对象的子系统：

- **Creator**：提供音乐"原材料"（乐谱）
- **Metronome**：提供"原始节奏"（均匀拍子）
- **Modulator**：定义节奏变异（此处封装了groove的数学模型）
- **Customizer**：让用户在实时中调整Modulator参数（UI对象）
- **Timer**：将Metronome的基础拍子按照Modulator的变异进行调整
- **Player**：将Creator的音乐材料按Timer的调制拍子输出

这个模式的价值在于展示了"语义概念"（groove/"swing"的感觉）如何被转化为一个交互式软件架构——用户通过屏幕上的滑块（Customizer）调整groove百分比（67%=典型swing），实时听到效果变化。这比阅读关于"swing"的文字解释高效得多——"It usually takes the author much longer to explain this concept to musical amateurs without the help of such an interactive tool"。

**关键模式：S3 IMPROVISATION HELPER （两星）**

这个模式定义了另一个多对象协作架构：
- **Accompanist**：提供伴奏
- **HarmonicAnalyser**：实时确定当前和声（例如"现在是Fm7"）
- **InputAnalyser**：读取用户的即兴输入（例如指挥棒的下击手势位置→音高）
- **Corrector**：将用户输入映射到当前和声允许的最接近音符
- **SupportAdaptor**：让用户调整"协助"程度（从"完全自动纠正"到"无辅助=全音阶键盘"）

这个模式产生了"从未弹过乐器的人可以走到系统前开始即兴——而且不错一个音"的惊人用户体验。

---

## 四、逻辑梳理（论证链条+因果转折）

### L### 4.1 三套模式语言的论证分工

```
音乐模式语言 (M1-M11)
    ├── 功能: 证明→应用领域知识可以模式化
    ├── 读者: HCI设计师+软件工程师 (学习应用领域的"语言")
    └── 论证: "看, 音乐理论中的设计决策和建筑设计遵循相同的模式结构"

HCI模式语言 (H1-H17)
    ├── 功能: 证明→交互设计经验可以模式化+提供直接可用的设计知识
    ├── 读者: 所有三方 (核心)
    └── 论证: "看, 这些模式可以在你的下一个交互式展览项目中使用"

软件模式语言 (S1-S4)
    ├── 功能: 证明→领域特定的软件架构也可以模式化
    ├── 读者: HCI设计师 (理解技术约束) + 软件工程师 (复用解决方案)
    └── 论证: "看, 即使是技术性的软件架构也可以用人类可读的模式表达"
```

### L### 4.2 模式间的引用网络

模式间的context/reference链接构成了"展开路径"：

```
M1 BLUES STYLE
    → M2 COMBO INSTRUMENTATION (乐队组成)
    → M4 TWELVE-BAR PROGRESSION (和声框架)
    → M7 PENTATONIC SCALE (旋律材料)
    → M9 TRIPLET GROOVE (节奏感觉)

H1 ATTRACT-ENGAGE-DELIVER
    → H2 ATTRACTION SPACE (吸引阶段)
    → H6 INCREMENTAL REVEALING (参与阶段)
    → H9 CLOSED LOOP (传达阶段=闭环)

H2 ATTRACTION SPACE
    → H12 INNOVATIVE APPEARANCE (靠什么吸引)
    → H5 SIMPLE IMPRESSION (不要太复杂吓跑人)
    → H11 DOMAIN-APPROPRIATE DEVICES (用领域相关的物品)

S1 BRANCHING TRANSFORMER CHAIN (总架构)
    → S2 METRIC TRANSFORMER (节奏处理)
    → S3 IMPROVISATION HELPER (即兴辅助)
    → S4 MUSICAL EVENTS (数据基础)
```

这些引用网络确保了单个模式不是孤立的——每个模式都有"从哪里来"（context）和"往哪里去"（references）的明确轨迹。

### L### 4.3 跨语言的链接

存在一些跨语言的隐含链接：
- M9 TRIPLET GROOVE → S2 METRIC TRANSFORMER（音乐概念→软件实现）
- M7 PENTATONIC SCALE + M8 BLUE NOTES → S3 IMPROVISATION HELPER（音乐素材→即兴纠正的基础）
- H11 DOMAIN-APPROPRIATE DEVICES（的WorldBeat例子）→ M1-M11（因为选用音乐领域的设备，所以需要音乐领域的模式知识）

---

## 五、材料使用方式

### L### 5.1 排版作为论证工具

本章最显著的材料使用特征是**排版规则的精确遵守**——每个模式严格遵循Alexander的隐式结构规范：

1. **小大写名称**（如"BLUES STYLE"）：在视觉上建立模式的"标题性"
2. **星级评分**（★/★★/无星）：在名称后的第一视觉线索
3. **照片/插图**：作为"sensitizing image"——例如M1使用黑人铁路工人的历史照片而非乐谱
4. **省略号开头（"..."）**：context——"你从哪里来"
5. **三个分隔符号**（在本书中以菱形/星号呈现）：将模式分为三大部分
6. **粗体问题**：在分隔符后即刻出现
7. **正文讨论**：详述forces和例子
8. **"Therefore:"**（独占一行）：解决方案的前导词——全书最具辨识度的排版元素
9. **粗体方案**：紧随"Therefore:"
10. **手绘图**：方案的视觉化
11. **三个分隔符**：第二部分结束
12. **小模式引用（"..."开头）**：references——"你可以往哪里去"

这种排版使用本身就是对Ch.3 §3.4和Ch.2 §2.1中理论分析的**实践验证**——它证明了"隐式结构"确实可以被精确复制并应用于新的领域。

### L### 5.2 图像的战略使用

- **历史照片**（M1: 铁路工人, M2: Louis Armstrong's Hot Five）：将音乐模式锚定在真实历史和文化实践中——不是抽象的"音乐理论"，而是"真实的人在做真实的音乐"
- **乐谱片段**（M4, M5, M7）：向音乐专业人士传递精确信息
- **手绘示意图**（每个模式）：模仿Alexander的风格——传达"这是一个草图/概念"而非"这是一个精确蓝图"
- **展品照片**（WorldBeat, CAVE, DynaWall）：将HCI模式锚定在真实的展览系统中
- **软件架构图**（S1, S2, S3）：以文字标注的方块+箭头图——刻意不使用UML，保持对非工程师的可读性

### L### 5.3 WorldBeat作为贯穿案例的统一功能

三个模式语言的几乎所有例子都来自同一组项目——WorldBeat(1996), Interactive Fugue(1999), Personal Orchestra(2000), Virtual Vienna(2000)。这种以一个核心项目贯穿的做法创造了一种"纵向的案例深度"——读者可以通过四个视角（应用领域、交互、软件、评估）反复观察同一个系统，获得对其设计本质的立体理解。

---

## 六、论辩与阐述方法

### L### 6.1 "展示而非讲述"（Show, Don't Tell）

Ch.1-3在"论证"模式方法的可行性——Ch.4的策略是"直接展示"三套模式语言。Borchers在章首引言中的Goethe诗句表达了这一策略的自觉性："Der Worte sind genug gewechselt, Laßt mich auch endlich Taten sehn!"（言辞已足够，让我看到行动！）。

### L### 6.2 模式内的归纳式论证

每个模式内部遵循一个相同的论证弧：
```
具体现象/问题 → 具体例子(已知系统) → 从例子中抽象出通用方案
```
这是**归纳法**（inductive）而非**演绎法**（deductive）。Borchers在Ch.3 §3.4.5中明确主张："to make a pattern as understandable as possible, it is better to use an inductive than a deductive style"。Ch.4严格执行了这一方法论——每个模式都是从"你看这个系统/这个录音/这个场景"出发，逐步上升到"所以你应该这样做"。

### L### 6.3 观众的双重性策略

每个模式同时服务于两个观众群体：
- **领域外读者**：通过具体例子理解概念
- **领域内读者**：通过已经知道的事实验证模式的有效性

例如M7 PENTATONIC SCALE——音乐外行通过五声音阶的概念开阔视野，音乐内行看到"Nice Work If You Can Get It"的例子会想"对！那个旋律确实是五声音阶！"——从而产生"模式确实捕捉了我已经知道但未曾明确表述的东西"的认同感。

### L### 6.4 评级系统的修辞功能

两星（**）vs 一星（*）vs 无星的区分为每个模式附加了一个"置信度元数据"：
- **模式的作者都不完全确定**→读者感到是被引入一个"进行中的研究"而非"教条式规章"
- **四星级的HCI模式**（H3, H6, H15, H16）被标记为最高置信度→间接指出了作者认为"最经得起考验"的设计原则
- **无星的音乐模式**（M1, M2等）→暗示音乐领域模式的工作仍在早期，"the true invariant of the pattern still has to be found"

---

## 七、语言文风（原文摘录+L###）

### L### 7.1 整体风格

本章的英文文风与Ch.1-3截然不同——从"论述性的学术英语"切换为"描述性的模式散文"。这种切换是方法论上的需要：模式应该是"人类可读的散文"（Ch.3 §3.1的要求），而不是学术论文。

### L### 7.2 代表性原文摘录

#### L### 7.2.1 模式的"声音"——一种特殊的第二人称

> "You are searching for a musical style to play, sing, and improvise in, probably together with other players, without having formally rehearsed anything together." (M1 BLUES STYLE, Context)

所有模式的Context部分都使用"you"来直接与读者对话——这是从Alexander那里继承的核心文体特征。它不是学术的第二人称（"one might consider..."），而是教程式的、对话式的"You"——仿佛一位有经验的设计师在手把手地指导你。这种声音在学术写作中极为罕见，但在模式文学中是标准配置。

#### L### 7.2.2 从观察到方案——INFORMATION JUST IN TIME

> "We noticed users usually only stopping to read when they actually did not know how to continue, and were actively looking for help. We also frequently observed that WorldBeat users did not read longer texts explaining what to do, until those texts were redesigned to be even more succinct, clear, and constructive, as shown in the opening picture." (H16, Problem Description)

这个段落展示了"设计叙事"的力量——不是抽象的"用户不阅读长文本"，而是"我们注意到用户在某个确切的行为时刻才停止并阅读"。第一人称"We"的使用赋予这一观察以目击证人的可信度，转换成一个可以在你自己的项目中使用的具体规则（"≤3句, ≤12词/句"）。

#### L### 7.2.3 跨领域共鸣——音乐模式中的"设计"语言

> "The bass needs more note material than what is included in the current harmony chord. But adding arbitrary notes with large intervals between them leads to a loss of continuity and harmonic context in the music perceived." (M10 WALKING BASS, Problem)

注意这里使用的"设计"语汇——"needs more...than"（需求分析）、"adding...leads to a loss of"（副作用/代价）。即使主题是音乐理论，使用的却是设计思考的框架——这表明Borchers确实成功地将音乐理论"转译"为了设计语言。如果这一段用纯粹的音乐理论术语写（例如"根音在强拍上，弱拍填充和弦音和经过音"），非音乐家根本无法理解——但用设计术语写，任何人都能理解其中的trade-off逻辑。

#### L### 7.2.4 "Therefore:"——全书最标志性的一个词

在每个模式的Solution之前，独占一行的"Therefore:"是全书最具辨识度的排版/修辞元素：

> "Therefore:
> Use the blues style to start playing together with others. Make sure that its simple basic harmonic form is known by everybody, and agree on tempo, key choice, choruses, and introduction and endings." (M1 BLUES STYLE, Solution)

"Therefore:"执行了四个功能：(1)标记"方案即将到来"；(2)暗示前面的所有讨论逻辑上导致了这一结论；(3)以排版空白为方案创建呼吸空间；(4)将模式从"描述"切换到"指导"的模式。"Therefore:"之前的文字是"这是问题和背景"，之后的文字是"这是你应该做的"。

#### L### 7.2.5 最令人印象深刻的方案——IMPROVISATION HELPER的"魔法"

> "The result is quite fascinating: people who have never before played an instrument can walk up to the system and start improvising to a blues band—without playing wrong notes!" (S3 IMPROVISATION HELPER, Examples)

这是全书最热情的措辞——"quite fascinating"不是学术用语，而是设计者的真实兴奋。而破折号后的"without playing wrong notes!"是一个感叹号——全书唯一使用感叹号的句子之一。这种由内而发的热情打破了学术文体的常规克制，但它出现在模式内部（允许更灵活的语调），不会破坏全书的严肃性。

---

## 八、实体清单（六类每类≥3+L###）

### L### 8.1 人物实体

| 编号 | 姓名 | 出现位置 | 角色 | L### |
|------|------|---------|------|------|
| 1 | J.W. von Goethe | 章首引语 | "Faust"诗句——"Der Worte sind genug gewechselt, Laßt mich auch endlich Taten sehn!" | L###401 |
| 2 | Louis Armstrong | M2插图 | Hot Five爵士组合——作为COMBO INSTRUMENTATION的视觉例证 | L###402 |
| 3 | John Coltrane / Jimmy Garrison | M3插图 | 萨克斯手与贝斯手——SOLO & COMPING的摄影例证 | L###403 |
| 4 | Donald A. Norman | H11, H14 | 汽车座椅调节器(natural mappings)和电影放映机→录像机(hidden complexity)的经典例证 | L###404 |
| 5 | Hiroshi Ishii / Brygg Ullmer | H11 | Tangible Bits概念和Urp城市规划工作台——DOMAIN-APPROPRIATE DEVICES的核心当代例证 | L###405 |
| 6 | John Ruskin | §2.1引用, SITTING WALL引用 | 19世纪英国作家——描述了理想的花园矮墙（可坐、可聊天、可跳过的"Christian fence"） | L###406 |
| 7 | George Gershwin | M7 | "Nice Work If You Can Get It"的旋律恰好是全音阶五声音阶 | L###407 |
| 8 | Ben Shneiderman | H9, H16 | "八金律"——"design dialogs to yield closure"和"see and choose instead of remember and type in"被引用 | L###408 |
| 9 | Jakob Nielsen | H17 | 可用性启发式——"Simple and Natural Dialogue"被引用 | L###409 |
| 10 | Bill Hailey | M4 | "Rock Around The Clock"的副歌使用12小节Blues进行 | L###410 |

### L### 8.2 文献实体

| 编号 | 文献 | L### |
|------|------|------|
| 1 | Alexander et al. A Pattern Language (1977) — 模式格式和排版规则的直接来源 | L###411 |
| 2 | Tidwell. Common Ground / Interaction Design Patterns (1998) — H7, H9, H15等多处被引用 | L###412 |
| 3 | Norman. The Psychology of Everyday Things (1988) — H11, H14的经典例证来源 | L###413 |
| 4 | Ishii & Ullmer. "Tangible Bits" (CHI 1997) — H11的核心当代例证 | L###414 |
| 5 | Underkoffler & Ishii. "Urp" (CHI 1999) — H11的补充例证 | L###415 |
| 6 | Miller. "Blues" in Berendt (1978) — M4的和声分析来源 | L###416 |
| 7 | Binkowski. Musik Um Uns (1988) — M7/M8的非洲音乐根源来源 | L###417 |
| 8 | Akkerman. "Professional keyboard studies" (2000) — M10的Walking Bass规则来源 | L###418 |
| 9 | Borchers. "WorldBeat" (CHI 1997) — 全书最频繁的自引 | L###419 |
| 10 | Borchers & Mühlhäuser. "Design patterns for interactive musical systems" (IEEE Multimedia 1998) | L###420 |
| 11 | Borchers et al. "Getting it across: Layout issues for kiosk systems" (1995) — kiosk四分类 | L###421 |
| 12 | Streitz et al. "i-LAND" (CHI 1999) — DynaWall = AUGMENTED REALITY核心例证 | L###422 |
| 13 | Shneiderman. Designing the User Interface, 3rd ed. (1998) — H9, H16的理论资源 | L###423 |
| 14 | Lee, Garnett & Wessel. "An adaptive conductor follower" (ICMC 1992) — Virtual Baton算法来源 | L###424 |
| 15 | Fels et al. "MusiKalscope" (ICMCS 1997) — S3 IMPROVISATION HELPER的独立实现案例 | L###425 |

### L### 8.3 系统/产品实体

| 编号 | 名称 | L### |
|------|------|------|
| 1 | WorldBeat (全章贯穿案例) | L###426 |
| 2 | Interactive Fugue | L###427 |
| 3 | Personal Orchestra | L###428 |
| 4 | Virtual Vienna | L###429 |
| 5 | Urp (MIT Media Lab Urban Planning Workbench) | L###430 |
| 6 | CAVE (Ars Electronica Center) | L###431 |
| 7 | DynaWall / i-LAND (GMD-IPSI) | L###432 |
| 8 | Brain Opera (MIT Media Lab) | L###433 |
| 9 | Kai's Power Show | L###434 |
| 10 | Mac OS (Finder, Balloon Help, Simple Finder) | L###435 |
| 11 | Microsoft Windows (Tool Tips) | L###436 |
| 12 | Studio Vision Pro (Opcode Inc.) | L###437 |
| 13 | MusiKalscope (Fels et al.) | L###438 |
| 14 | "Fin-Fin"海豚展品 (Techniek Museum Delft — 负面案例) | L###439 |
| 15 | Exploratorium, San Francisco (三段式展品标签系统) | L###440 |

### L### 8.4 概念实体

| 编号 | 概念 | L### |
|------|------|------|
| 1 | 吸引-参与-传达三阶段模型 (Attract-Engage-Deliver) | L###441 |
| 2 | 吸引空间 (Attraction Space) | L###442 |
| 3 | 渐增揭示 (Incremental Revealing) | L###443 |
| 4 | 扁平窄树 (Flat and Narrow Tree — 深度≤5, 每层≤7) | L###444 |
| 5 | 闭环 (Closed Loop — 2-4分钟交互单元) | L###445 |
| 6 | 增强现实 (Augmented Reality — 在真实环境上附加数字层) | L###446 |
| 7 | 领域适切设备 (Domain-Appropriate Devices) | L###447 |
| 8 | 渐进式帮助 (Dynamic Descriptor — 自动激活的悬停说明) | L###448 |
| 9 | 即时信息 (Information Just in Time — ≤3句, ≤12词/句) | L###449 |
| 10 | 隐藏硬件 (Invisible Hardware) | L###450 |
| 11 | 单一输入设备 (One Input Device) | L###451 |
| 12 | 五声音阶 (Pentatonic Scale — 即兴的首选音集) | L###452 |
| 13 | 蓝音 (Blue Notes — 介于钢琴键之间的音) | L###453 |
| 14 | 三连音律动 (Triplet Groove — 摇摆感的数学模型) | L###454 |
| 15 | 分支变换器链 (Branching Transformer Chain — 信号处理的架构模式) | L###455 |
| 16 | 节奏变换器 (Metric Transformer — 6对象协作的节奏处理子系统) | L###456 |
| 17 | 即兴辅助器 (Improvisation Helper — 实时和声纠正系统) | L###457 |
| 18 | 音乐事件 (Musical Events — MIDI式的离散音符表示) | L###458 |
| 19 | Kiosk系统四分类 (Information/Advertising/Service/Entertainment) | L###459 |
| 20 | 合作体验 (Cooperative Experience — 2人同时使用+5+旁观者) | L###460 |

### L### 8.5 机构实体

| 编号 | 名称 | L### |
|------|------|------|
| 1 | Ars Electronica Center, Linz | L###461 |
| 2 | HOUSE OF MUSIC VIENNA (Haus der Musik Wien) | L###462 |
| 3 | MIT Media Lab | L###463 |
| 4 | Techniek Museum Delft | L###464 |
| 5 | Exploratorium, San Francisco | L###465 |
| 6 | GMD-IPSI (DynaWall/i-LAND项目所在地) | L###466 |
| 7 | Vienna Philharmonic Orchestra | L###467 |

### L### 8.6 技术实体

| 编号 | 名称 | L### |
|------|------|------|
| 1 | Buchla Lightning II 红外线指挥棒 | L###468 |
| 2 | MIDI (Musical Instruments Digital Interface) 协议 | L###469 |
| 3 | MAX 多媒体编程环境 (Opcode Inc.) | L###470 |
| 4 | NaviPad (Virtual Vienna的定制3D导航控制器) | L###471 |
| 5 | Roland pitch-to-MIDI converter | L###472 |
| 6 | Apple Power Macintosh 8500/120 | L###473 |
| 7 | General MIDI (GM) 音源 | L###474 |
| 8 | VR头戴显示器 (HMD — 在IMMERSIVE DISPLAY中作为反例) | L###475 |

---

## 九、与前后章关联

### L### 9.1 与Ch.3的关联

本章是对Ch.3的完整实例化：
- Ch.3 §3.1的 $PL=(\wp, \Re)$ → 本章每套模式语言开头都有一张展示链接关系的模式语言图
- Ch.3 §3.1的 $P=\{n, r, i, p, f, e, s, d\}$ → 每个模式严格包含所有十个成分
- Ch.3 §3.3的时空排序 → HCI模式从ATTRACT-ENGAGE-DELIVER（整体任务）到ONE INPUT DEVICE（具体设备）
- Ch.3 §3.4.1的名称规则 → 所有模式名控制在2-4词（如"ATTRACTION SPACE"而非"THE DESIGN OF THE SPACE AROUND THE EXHIBIT THAT ATTRACTS VISITORS"）
- Ch.3 §3.4.3的跨领域媒体选择 → 音乐模式使用乐谱/录音，HCI模式使用照片/截图，软件模式使用架构图

### L### 9.2 与Ch.2的关联

- Ch.2 §2.1的隐式排版规则 → 本章120%实现（排版比Alexander原著更加一致）
- Ch.2 §2.3 Tidwell的GO BACK TO A SAFE PLACE → 本章的EASY HANDOVER(H4)和CLOSED LOOP(H9)有概念亲缘
- Ch.2 §2.3 DESCRIPTION AT YOUR FINGERTIPS → 本章的DYNAMIC DESCRIPTOR(H15)是其交互式展览场景下的适配版
- Ch.2 §2.3的INTERACT'99分类法(scale-based) → 本章HCI模式的层级组织正是按"规模"分类

### L### 9.3 与Ch.5的关联

- 本章的DOMAIN-APPROPRIATE DEVICES (H11) → Ch.5 §5.2中对其进行了Writer's Workshop同行评审
- 本章重复引用的WorldBeat系统 → Ch.5 §5.4提供了完整的技术架构和评估数据
- 提及的Interactive Fugue → Ch.5 §5.5.1详细描述了模式在后续项目中的重用
- 提及的Personal Orchestra / Virtual Vienna → Ch.5 §5.5.2详述了一个使用模式名称进行设计沟通的会议实例（客户建议多个小显示器→因违反IMMERSIVE DISPLAY和COOPERATIVE EXPERIENCE而被否决）
- 本章的音乐模式（M9 TRIPLET GROOVE的groove滑块）→ Ch.5 §5.4.5显示这帮助游客在几秒内理解groove概念

---

*本报告根据 Jan Borchers: 《A Pattern Approach to Interaction Design》Chapter 4 (pp.75-168) 细读撰写。*
