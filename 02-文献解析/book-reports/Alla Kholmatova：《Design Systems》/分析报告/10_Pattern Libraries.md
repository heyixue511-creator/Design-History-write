# 10_Pattern Libraries

## 一、章节定位与功能

本章是全书的收束实操章节，聚焦于设计系统的核心工具——模式库（Pattern Library）。但与前九章建立的核心观点一致，作者的立场是：模式库本身不是系统，而是支持和传播系统的工具。本章的功能是提供一套建立多学科共享、持久可维护的模式库的实用策略，涵盖内容获取、组织方式、文档化规范、工作流程和工具选择。

## 二、结构分析

1. **导入与定位**（L2677-2705）：重申"模式库不等于设计系统"，并引入一个关键前提——多学科（multi-disciplinary）的模式库比单学科的模式库更具韧性和持久性。以 Sipgate 的教训佐证：技术复杂度阻碍了设计师参与，导致模式重复。
2. **内容优先**（L2707-2722）：提出以 Google Docs 作为 MVP 模式库的起点——先有内容（定义好的模式及其目的），再考虑网站的设计和构建。
3. **组织方式**（L2723-2796）：三大类组织策略——感知模式的抽象化（从各种系统中提取的命名对比表）、功能模式的四种组织方式（字母序、层级式、按目的/结构）、FutureLearn 的两年试错历程和 Shopify Polaris 的可用性测试。
4. **模式文档化**（L2797-2954）：
   - 功能模式文档化：名称、目的、示例、变体（各附正反例证）。
   - 感知模式文档化：不只记录构建块，更要记录使用方法；交叉引用样式；展示元素之间的关系（比例、层次、密度等）。
5. **工作流程**（L2955-3013）：新模式添加的流程和标准、团队角色与责任、策展人（Curator）vs. 生产者（Producer）两种模式。
6. **系统多面的一致性**（L3013-3026）：代码、设计文件和模式库——同一系统的三个"面"——应遵循相同的命名、结构和目的理解。
7. **工具**（L3027-3059）：保持模式库与代码同步的工具概览（KSS、Pattern Lab、Fractal）、保持设计文件与模式库同步的工具（Abstract、Craft、UXPin、Brand.ai、Lingo）。
8. **未来展望**（L3061-3066）：多学科协作工具、从模式库自动生成设计文件——"设计系统让我们有更多时间和精力解决更大、更有意义的问题"。

## 三、内容分析（核心论题+关键论点与案例）

**核心论题**：一个有效的模式库是多学科的、以内容（模式的目的和定义）为先的、组织方式与用户思维模型匹配的、工具服务于工作流程而非反过来被工具所困的。模式库的建设是一个持续迭代的过程——"这项工作永远不会完成"。

**关键论点**：
1. 多学科参与是模式库持久性的关键——Sipgate 的教训：仅由开发者维护的模式库必然导致设计师脱离系统。（L2691-2701）
2. 先有内容，再有平台——Google Docs 文件夹就是 MVP 模式库。过早纠结于工具和网站设计会拖慢进度。（L2709-2722）
3. 原子设计（Atomic Design）不一定适合每个团队"开箱即用"——FutureLearn 曾花太多时间争论某元素是"分子"还是"有机体"，最终简化为两个层级。（L2767-2771）
4. 模式的分类方式应基于使用者（设计师、开发者、内容策略师等）的思维模型——如 Shopify Polaris 通过卡片分类和可用性测试来决定分类。（L2787-2791）
5. 好的文档化应使模式的"目的"一目了然——Sipgate 的两个版本的模式描述对比："Use Showcase to present multiple types of information with a media file"（太泛）vs. "Fact Grid is a shortlist of facts...Use Fact Grid to give the reader an immediate impression about the upcoming content"（具体、可想象）。（L2829-2835）
6. 感知模式的文档化不能止于构建块（色板、字号表），必须展示使用方法和元素之间的关系。（L2896-2953）
7. 系统和工具应该适应团队的自然工作流程，而非相反。（L3063）
8. "这项工作永远不会完成"——这是所有有效模式库团队的最高频表述。（L2795-2796）

**关键案例**：
- Sipgate 的单学科陷阱：技术复杂度阻止了设计师参与，导致设计师在 Photoshop 中从头创建页面，将模式适配工作全压在开发者身上——"导致了无数的 if 语句、例外和重复模式"。（L2693-2700）
- WeWork Plasma 的 Google Docs MVP：快速记录所有核心模式及其定义，而非被构建和设计限制所阻碍。（L2717-2721）
- 九家公司对"感知模式 vs. 功能模式"的命名对比表——展示了术语的多样性以及"components"（组件）作为功能模式通用命名的事实。（L2735-2737）
- 原子设计变体对比表：8个不同系统对层级分类的命名方式——从 Atomic Design（5层）到 WeWork Plasma（2层），说明了灵活性的必要。（L2773-2774）
- FutureLearn 的两年组织方式试错：从一长列表→原子设计层级→按页面角色（"intro"、"outro"、"hero"、"bridge"）→最终按目的分类（"推广模块"、"学习进度模块"、"社交模块"等）。（L2779-2785）
- Shopify Polaris 的多学科思维模型研究——"设计师倾向于按结构思考，开发者默认按功能，内容策略师两者结合"。（L2789-2791）
- Sipgate "Showcase" → "Fact Grid" 的目的描述改进。（L2829-2835）
- Marvel 的自我文档化示例——Popover 组件在示例中自带说明性 UI 文案。（L2846-2849）
- FutureLearn "Billboard" 的失败示例——呈现方式完全没传达出"这是一块醒目的推广元素"。（L2851-2855）
- Carbon 的变体对比：日期选择器的每个变体类型清晰说明了使用场景。（L2871-2873）
- GOV.UK 的颜色色板——不仅列出色值，更指定了文本、链接、背景等角色的使用规则。（L2900-2904）
- Shopify Polaris 的 Do/Don't 格式——"蓝色不应用于按钮"的显式规则。（L2906-2908）
- FutureLearn 交互状态网格——将所有交互状态放在一个网格中，使跨元素的统一规则成为可能。（L2923-2927）
- FutureLearn 的密度三级法——"宽敞"、"常规"、"紧凑"——将排版对比度与间距的关系可视化。（L2939-2951）
- Nordnet 的三步提交流程：提交→团队讨论→文档化并推送到 Craft Library。（L2963-2968）
- Atlassian 的"perpetually slightly off-sync"哲学——拥抱模式库与代码永远不会完美同步的事实，设计能处理这些不完美的系统。（L3041-3042）
- Amy Thibodeau/Shopify 的"合作伙伴而非警察"理念——设计系统团队应该尽早与产品团队合作，而非最后批准或否决。（L3009-3011）

## 四、逻辑梳理（论证链条+因果转折）

**论证链条**：

模式库是什么？（重温第1章定义）→ 为什么需要多学科参与？（Sipgate 教训）→ 从哪里开始？（先有内容，Google Docs= MVP）→ 内容如何组织？（感知模式抽象化 + 功能模式四种方法）→ 如何文档化？（从名称/目的/示例/变体的基本四要素开始）→ 如何管理持续贡献？（工作流程+标准）→ 工具如何支持？（概览但不深究）→ 回归核心：模式库、代码和设计文件是同一系统的三个面 → 最终展望：工具将适应多学科工作流程，解放设计师和开发者去解决更大的问题。

**关键转折**：
- L2709："Looking back, at FutureLearn we spent far too much time researching tools and working out what the pattern library should look like."——以反思开篇，立即确立"工具不是起点"的论点。
- L2715-2716："Second, a folder in Google Docs is like an MVP pattern library — the team can start using it as a reference right away."——将"完美"延迟到"可用"之后，体现了务实的迭代主义。
- L2767-2768："At FutureLearn we struggled to find a use for 'templates' and 'pages.'"——坦承"原子设计不完全适合我们"，鼓励读者根据自己的需求调整方法论。
- L2795-2796："The phrase I hear the most from all the teams with effective patterns libraries is that their 'work is never done'."——将"未完成"从缺点重新框架为有效系统的常态特征。
- L2953："Perhaps the next generation of pattern libraries can show them in more connected ways."——以建设性批判结束文档化部分，为未来的发展指出方向。
- L3041-3042："Our design language, as any language, is constantly evolving...We embrace this fact and design a system which can deal with these imperfections."——Jürgen Spangl 的引述将"永远不同步"的焦虑转化为"拥抱演化"的积极态度。
- L3065-3066："Design systems free our time and energy to solve bigger and more meaningful problems, like understanding our users better and making design languages more inclusive."——以充满希望和意义的展望结束全章，将整本书的技术性讨论升华到人文关怀的层面。

## 五、材料使用方式

1. **对比表格的密集使用**：三张大型对比表——九家公司的感知模式/功能模式命名对比（L2735-2737）、原子设计层级变体对比（L2773-2774）、模式组织方式的系统差异（L2773-2774）。表格是最有效的"一眼看清差异"的工具。
2. **Sipgate 故事的再引用**：开篇再次使用 Sipgate 的教训，但这次从"多学科参与"的角度切入——展示了同一案例的多维解读可能性。
3. **截图的正反例证**：Marvel 的好示例 vs. FutureLearn Billboard 的差示例——在文档化讨论中提供了可直接对比的视觉证据。
4. **工具全景图**：从 KSS（最简单）到 Fractal、Pattern Lab，再到 Abstract、Craft、Brand.ai、Lingo、UXPin——提供了从轻到重的工具连续谱。
5. **实践者的直接引述**：来自 Atlassian（Jürgen Spangl）、Shopify（Amy Thibodeau、Selene Hinkley）、Sipgate（Mathias Wegener）的多学科观点——用不同角色的声音为"多学科"论点提供多重证据。

## 六、论辩与阐述方法

1. **"MVP 思维"的实践化**：将软件开发的 MVP 概念创造性应用于模式库建设——"一个 Google Docs 文件夹就是你的 MVP 模式库"。
2. **正反案例并置**：总是呈现好示例和差示例（Sipgate 的两个描述版本、Marvel vs. FutureLearn 的示例质量），让"好"和"差"的具体含义可视化。
3. **演化叙事**：FutureLearn 的两年组织方式试错（L2779-2785）和 Shopify Polaris 的持续用户研究（L2787-2791）都以"我们尝试了X→发现Y问题→转向了Z"的叙事结构呈现，比直接给结论更有说服力。
4. **"我们还在学习中"的谦逊语调**：多次出现"we found..."、"we struggled with..."、"after trial and error..."——拒绝了"专家给出正确答案"的权威姿态，代之以"同行分享经验"的协作姿态。
5. **未来主义收尾**：以工具演化和社会意义的展望结束，跳出前九章的方法论框架，赋予全书一个情感上令人振奋的结尾。

## 七、语言文风（原文摘录+L###行号）

> "Looking back, at FutureLearn we spent far too much time researching tools and working out what the pattern library should look like."（L2709）

> "It was often left to developers to fit the design with the existing patterns, who had to tweak them until they fit. This led to numerous if-statements, exceptions and duplicate patterns." ——Mathias Wegener（L2695-2697）

> "The phrase I hear the most from all the teams with effective patterns libraries is that their 'work is never done'."（L2795-2796）

> "We want to collaborate with teams as early as possible when they're thinking about developing new patterns and components. Our relationship with product teams should be a partnership, rather than a situation where someone goes away and does a bunch of work and then we either approve or veto it." ——Amy Thibodeau, Shopify（L3009-3011）

> "It's always slightly off-sync. If it's too perfect, it's not going to work. Our design language, as any language, is constantly evolving." ——Jürgen Spangl, Atlassian（L3041-3042）

> "Design systems free our time and energy to solve bigger and more meaningful problems, like understanding our users better and making design languages more inclusive."（L3065-3066）

**文风特征**：本章是全书的"务实终章"——语调介于轻松反思和实用指导之间。大量引用实践者的直接引述（Atlassian、Shopify、Sipgate、Carbon），让不同的声音共同演奏"多学科合作"这一主题。最后的未来展望（L3065-3066）以诗意的乐观主义结束，与全书开篇的"问题陈述"形成完整的叙事弧线。

## 八、实体清单（六类）

### 人物（≥3）
- Brad Frost：Atomic Design 方法论创始人。（L2759）
- Dave Olsen：Pattern Lab 联合创作者。（L3035）
- Brian Muenzenmeyer：Pattern Lab 联合创作者。（L3035）
- Mark Perkins：Fractal 工具创作者。（L3037）
- Mathias Wegener：Sipgate 前端开发者。（L2699）
- Andrew Couldwell：WeWork Plasma 设计系统的记录者。（L2717）
- Jürgen Spangl：Atlassian 设计主管。（L3041-3042）
- Amy Thibodeau：Shopify UX 主管。（L3009-3011）
- Selene Hinkley：Shopify Polaris 内容策略师。（L2789-2791）
- Vitaly Friedman：Smashing Magazine 主编。（L2892）
- Nathan Curtis：模块化设计顾问。（本章多项间接引用）
- Ross Malpass：Nordnet 原子设计工作流程的记录者。（L3127脚注, L3131脚注）

### 著作（≥3）
- Brad Frost：《Atomic Design》（L2759）
- Vitaly Friedman："Taking The Pattern Library To The Next Level"（L2892）
- Ross Malpass："Super easy Atomic Design documentation with Sketch app" 和 "An Atomic workflow for design & development at Nordnet"（L3127, L3131脚注）

### 概念（≥3）
- MVP Pattern Library（最小可行模式库）（L2715）
- Atomic Design（原子设计：Atoms→Molecules→Organisms→Templates→Pages）（L2759-2771）
- Hierarchical Organization（层级式组织方式）（L2755-2776）
- Purpose-Based Organization（基于目的的组织方式）（L2777-2785）
- Pattern Documentation（模式文档化：Name/Purpose/Example/Variants四要素）（L2803-2815）
- Living Pattern Library（活的模式库）（L2857）
- Variants（变体）（L2863-2879）
- Curator vs. Producer Model（策展人 vs. 生产者模型）（L2999-3006）
- Source of Truth（"真相之源"——模式库作为权威参考）（L3055-3059）
- Cross-Referencing Styles（样式的交叉引用）（L2915-2921）
- Density and Contrast in Layout（排版密度与对比度的关系）（L2937-2951）
- Submission Template and Process（模式提交模板与流程）（L2961-2977）
- Criteria for Adding Patterns（添加模式的标准：每次新增 vs. 第二次使用再添加 vs. 基于潜在复用）（L2977-2991）

### 机构（≥3）
- FutureLearn（贯穿全章）
- Sipgate（L2693-2700, L2829-2835）
- WeWork（Plasma 设计系统）（L2717-2721）
- Airbnb（L2735表格）
- Atlassian（L2735表格, L2876-2878, L3041-3042）
- BBC（GEL）（L2735表格）
- IBM（Carbon）（L2735表格, L2819-2821, L2859-2861, L2871-2873, L2919-2921）
- Lonely Planet（Rizzo）（L2735表格, L2747-2751）
- Marvel（L2735表格, L2846-2849）
- Office Fabric（L2735表格, L2867-2869）
- Salesforce（Lightning Design System）（L2735表格）
- Shopify（Polaris）（L2735表格, L2787-2791, L2906-2908, L3009-3011）
- GE（Predix）（L2773表格）
- Nordnet（L2963-2968）
- Shyp（L2973）
- Eurostar（GLU）（L2761-2763）
- GOV.UK（L2900-2904）
- US Government（Web Standards）（L2910-2912）
- OpenTable（L2934）
- Sky（Toolkit）（L2884-2886, L2747）
- Clearleft（ClearFractal）（L2773表格）

### 地点（≥3）
（本章无显著地点实体）

### 事件（≥3）
- Sipgate 新建模式库及"Fact Grid"描述方式的改进（L2829-2835）
- FutureLearn 两年的模式库组织方式试错过程（L2779-2785）
- Shopify Polaris 通过卡片分类和可用性测试决定模式分类方式（L2787-2791）
- Atlassian 两阶段冲刺法建立 ADG（L1930-1931, Ch7回引）

## 九、与前后章的关联

本章是全书的"汇聚点"——前面九章建立的所有概念和流程最终落到了"如何建立一个模式库来承载它们"这个实操问题上。与第1章首尾呼应：第1章指出"模式库不等于设计系统"（L327），本章以这个观点开篇（L2679），并用整章的篇幅说明"如何让模式库有效服务于设计系统"。与第5章（共享语言）和第7章（规划）密切关联：本章中关于组织方式、多学科参与、知识分享的内容，是第5章共享语言实践和第7章文化建设策略在工具层面的具体实现。与第8章和第9章的关联最直接：这两章系统化的成果（定义好的功能模式/感知模式及其目的、命名、结构、变体）是本章模式库的"内容"。与 Conclusion 的关联：本章结尾（L3065-3066）的展望——"让我们有更多时间和精力解决更大、更有意义的问题"——与结论章（Conclusion）中关于模式语言伦理责任的论述形成情感和思想的闭环。
