# 03_Functional Patterns

## 一、章节定位与功能

本章是 Part 1 中"模式"主题的第一部分，聚焦于功能模式（functional patterns）。其核心功能是：论证为什么功能模式应该在设计过程早期被定义，并提供一套具体的工具和技术来实现这一目标。与第4章（感知模式）形成对照和互补——如果说第4章关注"界面的形容词"，本章关注的是"界面的名词和动词"。

## 二、结构分析

1. **定义与导入**（L621-633）：定义功能模式及其与用户行为的关系，以食谱网站为例说明模块如何组合以达成共享目的。
2. **核心论证段**（L634-665）：通过 FutureLearn 三年间核心功能模式的演变，论证"模式可以演变，但行为保持稳定"——这是本章最重要的理论贡献。
3. **方法工具箱**（L666-783）：六种定义功能模式的技术：
   - 创建模式地图（pattern map）：将模块映射到用户旅程
   - 进行界面审计（interface inventory）：基于 Brad Frost 的方法
   - 将模式视为动作（view patterns as actions）：用动词替代名词来描述模式
   - 绘制模式结构（draw pattern's structure）：定义核心内容元素和层次
   - 将模式置于尺度上（place patterns on a scale）：建立视觉音量比较
   - 将内容视为假设（treat content as a hypothesis）：以目的驱动而非内容驱动来设计模块

## 三、内容分析（核心论题+关键论点与案例）

**核心论题**：功能模式是界面的"行为骨架"。定义功能模式的关键不是定义其外观，而是理解其目的——即它被设计来鼓励或促成的用户行为。模式的视觉呈现、交互和内容可以变化，但其核心行为目的相对稳定。

**关键论点**：
1. 功能模式是"界面的有形构建块，其目的是促成或鼓励某些用户行为"。（L625-627）
2. 核心功能模式的行为目的在长期演化中保持稳定，尽管其视觉设计和交互可以发生巨大变化。（L638-665）
3. 当模式没有被定义和共享时，团队成员会不断重新创建模式来完成类似目标，最终导致模式泛滥——"30种不同的产品展示和弹出菜单"。（L661-663）
4. 用动词而不是名词来描述模式：与其叫它"Image header"或"Course banner"，不如关注它做了什么——"Promote a course"、"Discover a course"。（L702-710）
5. 将内容视为假设而非已知资产：先定义模式的目的，然后测试内容是否符合该假设；如果内容始终不合适，要么重新定义目的，要么重新设计模式，要么使用另一个模式。（L759-775）
6. 模块的鲁棒性取决于是否从目的和结构出发来设计——如果被内容"牵着走"，模块就会变得脆弱。（L776-781）

**关键案例**：
- FutureLearn 课程进度模块：三年间视觉样式几经变化，但核心目的（导航课程内容、显示进度）不变。（L640-648）
- FutureLearn 讨论线程：布局和交互多次迭代，但核心目的（促使用户对话和学习）不变。（L650-653）
- FutureLearn 课程列表：从少量项目变为更大规模的筛选展示，但目的（帮助用户发现和加入课程）不变。（L655-658）
- Billboard 命名案例：从"Image header"到"Billboard"，用动词/行动命名来拓展模式的使用场景。（L704-710）
- 社交信息流统一案例：四种不同的评论/回复/通知模块通过绘制结构发现可以统一为一个"Feed item"模式。（L732-744）
- 脆弱模块案例：标题文案过长导致标签被推到可视区域外，因为模块设计过于依赖特定内容。（L776-781）

## 四、逻辑梳理（论证链条+因果转折）

**论证链条**：

功能模式是什么？→ 它们被设计来促成用户行为 → **问题**：为什么要早期定义？→ 因为不定义会导致模式重复和碎片化 → **论证**：FutureLearn 三年的演变显示，核心模式的行为目的高度稳定（视觉变、行为不变）→ 那么如何定义功能模式？→ 六种技术构成工具包 → 所有技术都围绕一个核心原则：从目的出发，连接模式与行为 → 最终目标：让模式更鲁棒、减少重复、便于测试。

**关键转折**：
- L634："But do the core functional patterns really change that much?"——以提问方式引入一个反直觉的发现：虽然界面三年变化巨大，但核心行为稳定。
- L660-661："Perhaps this was inevitable. Or could some of those duplications have been prevented?"——从描述问题转向探索解决方案。
- L728："It's just a sketch or a wireframe. I do that all the time anyway. But it's a bit different."——预判读者可能的质疑并加以回应。

## 五、材料使用方式

1. **历时性案例追踪**：FutureLearn 三年间同一模块的视觉演变截图（L642-658）是最有说服力的经验材料——四组 Before/After 对比，每组展示视觉变化与行为不变的张力。
2. **Brad Frost 方法论引用**：界面审计（Interface Inventory）直接借用 Frost 的方法，但加以改造——赋予了"目的导向"的新维度。
3. **图表演示**：模式结构图（content structure sketches）用视觉化方式将"先定义结构再设计外观"的理念落地。
4. **失败案例**：FutureLearn 的多版本社交信息流、脆弱模块案例，以教训佐证论点。
5. **Tom Osborne 音量指南的再度引用**：将第1章的理论概念应用于实际工作方法。

## 六、论辩与阐述方法

1. **先实例后抽象**：不从理论开始，而是以 FutureLearn 的视觉演变图为切入点，让读者先看到"变化"与"不变"的具象对比。
2. **工具箱格式**：六种技术被呈现为独立的、可单独使用的方法片段，降低了实践的进入门槛。
3. **预判式反驳**："It's just a sketch or a wireframe. I do that all the time anyway. But it's a bit different."（L728）——回应可能的读者质疑。
4. **悖论引入**：L759 开篇即以"paradox"一词点明内容优先设计与模块灵活性之间的张力，然后以"将内容视为假设"的概念化解。
5. **行动导向的语言**：每项技术都表现为一个动词短语（"Create a pattern map"、"Conduct an interface inventory"），强化"这是可做之事"的实践感。

## 七、语言文风（原文摘录+L###行号）

> "Functional patterns are the tangible building blocks of the interface. Their purpose is to enable or encourage certain user behaviors."（L625-627）

> "Patterns are the physical embodiment of the behaviors we're trying to encourage or enable through the interface."（L664）

> "When a pattern is not defined and shared in the team, you start recreating it to accomplish similar goals: another promotional module, another news feed, another set of sharing links, another dropdown."（L662）

> "To understand the purpose of a pattern, try focusing on what it does rather than what you think it is."（L702）

> "Here's a paradox. We're expected to design content-first, but at the same time we're expected to build modules in a way that can fit any kind of content. A way to do this is not necessarily by starting with content, but with the purpose."（L759）

**文风特征**：本章是最具实践操作感的章节。大量使用祈使句（"Try...", "Start by...", "Think about..."），语调是一步步手把手教学的风格。对自己的失败经历坦诚展示（L660-663, L776-781），拉近与读者的距离。

## 八、实体清单（六类）

### 人物（≥3）
- Brad Frost：界面审计（Interface Inventory）方法和 Atomic Design 的提出者。（L685）
- （无明显其他独立人物，主要引用自身团队实践）

### 著作（≥3）
- （本章无显著著作引用）

### 概念（≥3）
- Functional Patterns（功能模式）（L625-627）
- Pattern Map（模式地图）（L672-681）
- Interface Inventory（界面审计）（L683-698）
- Content Structure（内容结构）（L711-744）
- Visual Loudness Scale（视觉音量尺度）（L746-756）
- Content as Hypothesis（内容即假设）（L757-775）
- View Patterns as Actions（将模式视为动作）（L700-710）

### 机构（≥3）
- FutureLearn（贯穿全章）
- Open University（FutureLearn的创办方）（L638）

### 地点（≥3）
- London, UK：FutureLearn所在城市，但未在正文中显式提及

### 事件（≥3）
- FutureLearn 成立（2013）：由Open University创办（L638）
- FutureLearn 三年间的四次界面设计迭代（L640-658）

## 九、与前后章的关联

本章与第1章（Design Systems）和Introduction中关于"功能模式是界面的名词/动词"的论述直接衔接（L272-274）。与第2章（Design Principles）的关联在于：原则通过模式的选择和执行得以物化（如Medium的"Direction over Choice"原则体现在极简编辑器中）。与第4章（Perceptual Patterns）形成对照和互补——本章末尾（L787）明确指出"如果功能模式是界面中的物体，那么感知模式更像是风格——它们描述这些物体是什么样的以及给人的感觉"。与第8章（Systemizing Functional Patterns）前后呼应——本章提供理论基础，第8章提供更具体的系统化操作流程。
