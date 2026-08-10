# NN_专项报告与实体总索引

---

## 专项报告一：设计模式方法论在本书中的演变与应用

### 1.1 方法论源头与演变

《Designing Interfaces》的模式方法论直接追溯至两条脉络：

**建筑学脉络**：Christopher Alexander 的《A Pattern Language》(1977) 和《The Timeless Way of Building》(1979)。Alexander 建立了一个250模式的、多层级的完整模式语言，其核心理念是模式捕捉了使空间"宜居"（habitable）的结构性和行为性特征。

**软件工程脉络**：Gamma, Helm, Johnson, Vlissides 的《Design Patterns》(1994)。该书将模式概念引入面向对象软件设计，深刻改变了商业软件架构的实践。但 Tidwell 指出，软件模式"使软件对编写者更宜居——而非使用者"。

Tidwell 的贡献在于**将模式方法从软件架构迁移到用户界面设计**——第一版（2005）是最早的UI模式集合之一，第二版（2010）在竞品涌现的背景下进行了更新和扩展。

### 1.2 本书模式的定义特征

Tidwell 在本版中明确界定了模式的特征：

1. **具体的，非一般的**：模式填补高层原则与底层UI语法之间的空白
2. **跨平台有效**：最佳模式不限于单一平台或习语，"有些在印刷和交互系统中都有效"
3. **产品，非流程**：模式是可能的解决方案，不是关于如何找到解决方案的建议
4. **建议，非要求**：设计师可以根据设计语境和用户需求接受或拒绝
5. **元素之间的关系，非单一元素**："文本字段不是模式。但文本字段和旁边帮助文本之间的空间关系可能是模式。"
6. **适应每个设计语境**：模式实例化时，设计师应根据情况调整

### 1.3 与完整模式语言的距离

Tidwell 坦承本书"远不是完整"的模式语言。与 Alexander 的250模式多层语言相比，本书约124个模式显得规模有限。但她认为"至少它足够简洁，易于管理和使用"。

### 1.4 第二版的模式演变

第二版对模式集进行了大规模的重构：
- **新增**：Ch9（社交媒体）、Ch10（移动设计）整章；Fat Menus, Sitemap Footer, Hover Tools, Password Strength Meter, Data Spotlight, Radial Table 等新模式
- **移除**：Extras on Demand, Intriguing Branches, Global Navigation, Illustrated Choices, Color-Coded Sections 等已被广泛接受或不再常用的模式
- **移除整章**："Builders and Editors"章（读者反馈价值最低）
- **重构**：Ch5 从三章中提取列表相关内容；Card Stack → Module Tabs, Closable Panels → Collapsible Panels
- **新增关联**：每个模式末尾增加"In other libraries"部分

---

## 专项报告二：全书跨章模式网络分析

### 2.1 核心"安全网"模式链

```
Safe Exploration (Ch1)
  → Escape Hatch (Ch3) — 空间导航的安全网
  → Multi-Level Undo (Ch6) — 操作的安全网
  → Cancelability (Ch6) — 时间的安全网
  → Same-Page Error Messages (Ch8) — 输入的安全网
```

这五个模式形成了一个跨越4章的"安全网"体系，是本书最核心的设计理念之一。

### 2.2 "新手→专家"渐进路径

```
Clear Entry Points (Ch3) — 引导首次用户
  → Wizard (Ch2) — 步骤化引导
    → Good Defaults (Ch8) — 减轻决策负担
      → Multi-Level Help (Ch2) — 多层级帮助
        → Smart Menu Items (Ch6) — 适应使用模式
          → Macros + Command History (Ch6) — 专家工具
```

### 2.3 "列表→详情"三模式网络

```
Two-Panel Selector ←→ One-Window Drilldown ←→ List Inlay
      (Ch5)                (Ch5)                 (Ch5)
        ↑                     ↑                     ↑
  Picture Manager        Mobile Design         Accordion
      (Ch2)                (Ch10)               (Ch4)
```

### 2.4 "数据探索"交互链

```
Overview Plus Detail → Zoom/Pan → Sort → Filter → Data Brushing → Datatips
     (Ch7)            (Ch7)      (Ch7)   (Ch7)       (Ch7)         (Ch7)
```

### 2.5 "内容→分发→反馈"社交循环

```
Editorial Mix → Timing Strategy → Social Links → Sharing Widget → Content Leaderboard
   (Ch9)           (Ch9)             (Ch9)          (Ch9)            (Ch9)
      ↑                                                               ↓
      └──────────── 反馈驱动下一轮内容生产 ←─────────────────────────┘
```

---

## 专项报告三：第二版与第一版的变更分析

### 3.1 时代背景变化

- **Web 设计主导**：大多数UI设计师现在在Web上工作，而不是桌面应用
- **移动设计成熟**：iPhone 和其他智能设备普及
- **社交媒体主流化**：博客、Twitter、Facebook、评论区、论坛
- **模式方法被广泛接受**：多个其他UI相关模式集合涌现

### 3.2 结构变化

| 变化类型 | 具体内容 |
|---------|---------|
| 新增章节 | Ch9 Using Social Media, Ch10 Going Mobile |
| 移除章节 | "Builders and Editors"（原第8章） |
| 重构章节 | Ch5 Lists（从原Ch2, Ch7等多章抽取） |
| 重写导论 | Ch2 (IA), Ch3 (Navigation), Ch4 (Page Layout) |
| 更新示例 | 几乎所有模式都有新截图 |

### 3.3 内容变化

- "几乎每个模式至少有一个新的图片示例"
- "许多模式有'In other libraries'部分"
- Row Striping 更新了实验研究结果
- 多个模式重命名以适应行业术语演变

### 3.4 有意留白

- 搜索模式（有专门的模式库覆盖）
- 一般社交界面（Designing Social Interfaces 覆盖）
- 手势界面（Designing Gestural Interfaces 覆盖）
- 移动设计的深度
- 动画过渡类型
- 帮助技术

---

## 实体总索引

### A. 全书模式总索引（按字母顺序）

| 序号 | 模式名 | 章节 | 中文译名 | 功能分类 |
|------|--------|------|---------|---------|
| 1 | Accordion | Ch4 | 手风琴面板 | 页面布局 |
| 2 | Action Panel | Ch6 | 动作面板 | 动作命令 |
| 3 | Alphabet Scroller | Ch5 | 字母索引滚动条 | 列表 |
| 4 | Alternative Views | Ch2 | 替代视图 | IA/结构 |
| 5 | Animated Transition | Ch3 | 动画过渡 | 导航 |
| 6 | Annotated Scrollbar | Ch3 | 注释滚动条 | 导航 |
| 7 | Autocompletion | Ch8 | 自动补全 | 表单 |
| 8 | Borders That Echo Fonts | Ch11 | 与字体呼应的边框 | 视觉 |
| 9 | Bottom Navigation | Ch10 | 底部导航 | 移动 |
| 10 | Breadcrumbs | Ch3 | 面包屑 | 导航 |
| 11 | Button Groups | Ch6 | 按钮组 | 动作命令 |
| 12 | Cancelability | Ch6 | 可取消性 | 动作命令 |
| 13 | Canvas Plus Palette | Ch2 | 画布+调色板 | IA/结构 |
| 14 | Carousel | Ch5 | 轮播 | 列表 |
| 15 | Cascading Lists | Ch5 | 级联列表 | 列表 |
| 16 | Center Stage | Ch4 | 中央舞台 | 页面布局 |
| 17 | Changes in Midstream | Ch1 | 中途改变 | 用户行为 |
| 18 | Clear Entry Points | Ch3 | 清晰入口点 | 导航 |
| 19 | Collapsible Panels | Ch4 | 可折叠面板 | 页面布局 |
| 20 | Command History | Ch6 | 命令历史 | 动作命令 |
| 21 | Content Leaderboard | Ch9 | 内容排行榜 | 社交 |
| 22 | Contrasting Font Weights | Ch11 | 对比字体粗细 | 视觉 |
| 23 | Conversation Starters | Ch9 | 对话启动器 | 社交 |
| 24 | Corner Treatments | Ch11 | 角处理 | 视觉 |
| 25 | Dashboard | Ch2 | 仪表盘 | IA/结构 |
| 26 | Data Brushing | Ch7 | 数据刷选 | 信息图形 |
| 27 | Data Spotlight | Ch7 | 数据聚光灯 | 信息图形 |
| 28 | Datatips | Ch7 | 数据提示 | 信息图形 |
| 29 | Deep Background | Ch11 | 深层背景 | 视觉 |
| 30 | Deep-linked State | Ch3 | 深度链接状态 | 导航 |
| 31 | Deferred Choices | Ch1 | 推迟选择 | 用户行为 |
| 32 | Diagonal Balance | Ch4 | 对角平衡 | 页面布局 |
| 33 | Dropdown Chooser | Ch8 | 下拉选择器 | 表单 |
| 34 | Dynamic Queries | Ch7 | 动态查询 | 信息图形 |
| 35 | Editorial Mix | Ch9 | 编辑混合 | 社交 |
| 36 | Escape Hatch | Ch3 | 逃逸舱口 | 导航 |
| 37 | Fat Menus | Ch3 | 胖菜单 | 导航 |
| 38 | Feature, Search, and Browse | Ch2 | 推荐·搜索·浏览 | IA/结构 |
| 39 | Few Hues, Many Values | Ch11 | 少色调·多明度 | 视觉 |
| 40 | Fill-in-the-Blanks | Ch8 | 填空式 | 表单 |
| 41 | Filmstrip | Ch10 | 胶片式 | 移动 |
| 42 | Forgiving Format | Ch8 | 宽容格式 | 表单 |
| 43 | Generous Borders | Ch10 | 宽大边距 | 移动 |
| 44 | Good Defaults | Ch8 | 良好默认值 | 表单 |
| 45 | Grid of Equals | Ch4 | 等分网格 | 页面布局 |
| 46 | Habituation | Ch1 | 习惯化 | 用户行为 |
| 47 | Hairlines | Ch11 | 极细线条 | 视觉 |
| 48 | Hover Tools | Ch6 | 悬停工具 | 动作命令 |
| 49 | Incremental Construction | Ch1 | 渐进构建 | 用户行为 |
| 50 | Infinite List | Ch10 | 无限列表 | 移动 |
| 51 | Input Hints | Ch8 | 输入提示 | 表单 |
| 52 | Input Prompt | Ch8 | 输入占位符 | 表单 |
| 53 | Instant Gratification | Ch1 | 即时满足 | 用户行为 |
| 54 | Inverted Nano-pyramid | Ch9 | 倒置纳米金字塔 | 社交 |
| 55 | Jump to Item | Ch5 | 跳转到项目 | 列表 |
| 56 | Keyboard Only | Ch1 | 键盘独占 | 用户行为 |
| 57 | Liquid Layout | Ch4 | 液态布局 | 页面布局 |
| 58 | List Builder | Ch8 | 列表构建器 | 表单 |
| 59 | List Inlay | Ch5 | 列表内嵌 | 列表 |
| 60 | Loading Indicators | Ch10 | 加载指示器 | 移动 |
| 61 | Local Zooming | Ch7 | 局部缩放 | 信息图形 |
| 62 | Macros | Ch6 | 宏 | 动作命令 |
| 63 | Many Workspaces | Ch2 | 多工作区 | IA/结构 |
| 64 | Menu Page | Ch3 | 菜单页面 | 导航 |
| 65 | Microbreaks | Ch1 | 微休息 | 用户行为 |
| 66 | Modal Panel | Ch3 | 模态面板 | 导航 |
| 67 | Module Tabs | Ch4 | 模块标签 | 页面布局 |
| 68 | Movable Panels | Ch4 | 可移动面板 | 页面布局 |
| 69 | Multi-Level Help | Ch2 | 多层级帮助 | IA/结构 |
| 70 | Multi-Level Undo | Ch6 | 多级撤销 | 动作命令 |
| 71 | Multi-Y Graph | Ch7 | 多Y轴图 | 信息图形 |
| 72 | New-Item Row | Ch5 | 新项目行 | 列表 |
| 73 | News Box | Ch9 | 新闻盒子 | 社交 |
| 74 | News Stream | Ch2 | 新闻流 | IA/结构 |
| 75 | One-Window Drilldown | Ch5 | 单窗下钻 | 列表 |
| 76 | Other People's Advice | Ch1 | 他人建议 | 用户行为 |
| 77 | Overview Plus Detail | Ch7 | 概览+详图 | 信息图形 |
| 78 | Pagination | Ch5 | 分页 | 列表 |
| 79 | Password Strength Meter | Ch8 | 密码强度指示器 | 表单 |
| 80 | Personal Recommendations | Ch1 | 个人推荐 | 用户行为 |
| 81 | Personal Voices | Ch9 | 个人之声 | 社交 |
| 82 | Picture Manager | Ch2 | 图片管理器 | IA/结构 |
| 83 | Preview | Ch6 | 预览 | 动作命令 |
| 84 | Progress Indicator | Ch6 | 进度指示器 | 动作命令 |
| 85 | Prominent "Done" Button | Ch6 | 突出"完成"按钮 | 动作命令 |
| 86 | Prospective Memory | Ch1 | 前瞻记忆 | 用户行为 |
| 87 | Pyramid | Ch3 | 金字塔导航 | 导航 |
| 88 | Radial Table | Ch7 | 径向表格 | 信息图形 |
| 89 | Recent Chatter | Ch9 | 最近聊天 | 社交 |
| 90 | Repost and Comment | Ch9 | 转发与评论 | 社交 |
| 91 | Responsive Disclosure | Ch4 | 响应式展开 | 页面布局 |
| 92 | Responsive Enabling | Ch4 | 响应式启用 | 页面布局 |
| 93 | Richly Connected Apps | Ch10 | 深度连接的应用 | 移动 |
| 94 | Right/Left Alignment | Ch4 | 左右对齐 | 页面布局 |
| 95 | Row Striping | Ch5 | 行条纹 | 列表 |
| 96 | Safe Exploration | Ch1 | 安全探索 | 用户行为 |
| 97 | Same-Page Error Messages | Ch8 | 同页错误消息 | 表单 |
| 98 | Satisficing | Ch1 | 满意即可 | 用户行为 |
| 99 | Sequence Map | Ch3 | 序列地图 | 导航 |
| 100 | Settings Editor | Ch2 | 设置编辑器 | IA/结构 |
| 101 | Sharing Widget | Ch9 | 分享小工具 | 社交 |
| 102 | Sign-in Tools | Ch3 | 登录工具 | 导航 |
| 103 | Sitemap Footer | Ch3 | 网站地图页脚 | 导航 |
| 104 | Skins and Themes | Ch11 | 皮肤与主题 | 视觉 |
| 105 | Small Multiples | Ch7 | 小倍数图 | 信息图形 |
| 106 | Smart Menu Items | Ch6 | 智能菜单项 | 动作命令 |
| 107 | Social Links | Ch9 | 社交链接 | 社交 |
| 108 | Sortable Table | Ch7 | 可排序表格 | 信息图形 |
| 109 | Spatial Memory | Ch1 | 空间记忆 | 用户行为 |
| 110 | Specialized Streams | Ch9 | 专用信息流 | 社交 |
| 111 | Streamlined Branding | Ch10 | 精简品牌 | 移动 |
| 112 | Streamlined Repetition | Ch1 | 流线化重复 | 用户行为 |
| 113 | Structured Format | Ch8 | 结构化格式 | 表单 |
| 114 | Text Clear Button | Ch10 | 文本清除按钮 | 移动 |
| 115 | Thumbnail Grid | Ch5 | 缩略图网格 | 列表 |
| 116 | Thumbnail-and-Text List | Ch10 | 缩略图+文本列表 | 移动 |
| 117 | Timing Strategy | Ch9 | 时机策略 | 社交 |
| 118 | Titled Sections | Ch4 | 标题分区 | 页面布局 |
| 119 | Touch Tools | Ch10 | 触屏工具 | 移动 |
| 120 | Tree Table | Ch5 | 树形表格 | 列表 |
| 121 | Treemap | Ch7 | 树图 | 信息图形 |
| 122 | Two-Panel Selector | Ch5 | 双面板选择器 | 列表 |
| 123 | Vertical Stack | Ch10 | 垂直堆叠 | 移动 |
| 124 | Visual Framework | Ch4 | 视觉框架 | 页面布局 |
| 125 | Wizard | Ch2 | 向导 | IA/结构 |

**总计：125个模式**（含Ch1的14个行为模式）

### B. 全书关键人物总索引

| 人物 | 角色/贡献 | 出现章节 |
|------|----------|---------|
| Jenifer Tidwell | 本书作者 | 全书 |
| Christopher Alexander | 建筑模式语言创始人 | Preface |
| Herbert Simon | Satisficing概念提出者 | Ch1 |
| Mihaly Csikszentmihalyi | 心流理论创立者 | Ch1 |
| Jef Raskin | "直觉=熟悉"提出者 | Preface |
| Donald Norman | 交互设计权威，正面情感研究 | Ch11 |
| Steve Krug | Don't Make Me Think作者 | Ch1 |
| Bill Scott | Designing Web Interfaces合著者 | Ch2, Ch4 |
| Theresa Neil | RIA应用结构三类型提出者 | Ch2 |
| Erin Malone | Designing Social Interfaces合著者 | Ch9 |
| Christian Crumlish | Designing Social Interfaces合著者 | Ch9 |
| Dan Saffer | Designing Gestural Interfaces作者 | Ch10 |
| Brian Fling | Mobile Design and Development作者 | Ch10 |
| Martijn van Welie | Welie.com模式库创始人 | 多章 |
| Stephen Few | Information Dashboard Design作者 | Ch2 |
| Edward Tufte | 信息可视化权威（间接引用） | Ch7 |
| Ben Shneiderman | Treemap发明者 | Ch7 |
| Gamma, Helm, Johnson, Vlissides | GoF设计模式作者 | Preface, Ch6 |

### C. 全书关键文献总索引

| 文献 | 作者 | 年份 | 关联章节 |
|------|------|------|---------|
| A Pattern Language | Christopher Alexander et al. | 1977 | Preface |
| The Timeless Way of Building | Christopher Alexander | 1979 | Preface |
| Design Patterns: Elements of Reusable O-O Software | Gamma et al. | 1994 | Preface, Ch6 |
| Designing Web Interfaces | Bill Scott, Theresa Neil | 2009 | Ch2, Ch4 |
| Designing Social Interfaces | Erin Malone, Christian Crumlish | 2009 | Ch9 |
| Designing Gestural Interfaces | Dan Saffer | 2008 | Ch10 |
| Mobile Design and Development | Brian Fling | 2009 | Ch10 |
| Information Dashboard Design | Stephen Few | 2006 | Ch2 |
| Don't Make Me Think | Steve Krug | 2000 | Ch1 |
| Emotional Design | Donald Norman | 2004 | Ch11 |
| The Visual Display of Quantitative Information | Edward Tufte | 1983 | Ch7 |
| Information Visualization: Perception for Design | Colin Ware | 2004 | Ch7 |
| Welie.com Interaction Design Patterns | Martijn van Welie | - | 多章 |
| Yahoo! Design Pattern Library | Yahoo! | - | 多章 |
| CSS Zen Garden | Dave Shea | - | Ch11 |

### D. 全书核心概念总索引

| 概念 | 定义简述 | 首现章节 |
|------|---------|---------|
| Design Pattern（设计模式） | 跨平台可复用的界面设计最佳实践 | Preface |
| Information Architecture（信息架构） | 组织信息空间的艺术 | Ch2 |
| Visual Hierarchy（视觉层次） | 通过大小/颜色/位置区分重要性 | Ch4 |
| Affordance（可供性） | 对象通过视觉线索暗示可操作性 | Ch6 |
| Satisficing（满意即可） | 接受"足够好"而非"最佳" | Ch1 |
| Flow（心流） | 完全沉浸的活动状态 | Ch1 |
| Habituation（习惯化） | 频繁动作变成无需意识的反射 | Ch1 |
| Spatial Memory（空间记忆） | 通过位置而非名称回忆对象 | Ch1 |
| Gestalt Principles（格式塔原则） | 邻近性/相似性/连续性/闭合性 | Ch4 |
| Preattentive Variables（前注意变量） | 在意识注意前传达信息的视觉特征 | Ch7 |
| Focus Plus Context（焦点+语境） | 信息可视化核心mantra | Ch7 |
| Navigational Cost（导航成本） | 页面跳转的认知负荷 | Ch3 |
| Idiom（习语） | 可识别的界面类型或风格 | Preface |
| Guild of Patterns（模式行会） | 多个模式相互支持的有机组合 | Ch2 |
| Reentrance（可重入性） | 支持中途退出并在之后从原处继续 | Ch1 |

---

## 分析报告文件清单

| 文件名 | 内容 |
|--------|------|
| 00_整体分析报告.md | 全书总体分析（定位、结构、内容、逻辑、材料、论辩、文风、实体、跨章关联） |
| 01_第1章分析报告_What_Users_Do.md | Ch1：用户行为模式（14个行为模式） |
| 02_第2章分析报告_Organizing_the_Content.md | Ch2：信息架构与应用结构（10个模式） |
| 03_第3章分析报告_Getting_Around.md | Ch3：导航、路标与路径寻找（13个模式） |
| 04_第4章分析报告_Organizing_the_Page.md | Ch4：页面元素布局（13个模式） |
| 05_第5章分析报告_Lists_of_Things.md | Ch5：列表呈现（12个模式） |
| 06_第6章分析报告_Doing_Things.md | Ch6：动作与命令（11个模式） |
| 07_第7章分析报告_Showing_Complex_Data.md | Ch7：信息图形（11个模式） |
| 08_第8章分析报告_Getting_Input_from_Users.md | Ch8：表单与控件（11个模式）【校对修正：原误作10个】 |
| 09_第9章分析报告_Using_Social_Media.md | Ch9：社交媒体（12个模式） |
| 10_第10章分析报告_Going_Mobile.md | Ch10：移动设计（11个模式） |
| 11_第11章分析报告_Making_It_Look_Good.md | Ch11：视觉风格与美学（7个模式） |
| NN_专项报告与实体总索引.md | 本文件：方法论分析+跨章网络+版次变更+实体总索引 |

---

*分析完成日期：2026-08-05*
*总报告数：13份（1份整体报告 + 11份章节报告 + 1份专项报告与索引）*
*每章报告九节结构：一/定位功能 二/结构分析 三/内容分析 四/逻辑梳理 五/材料使用 六/论辩方法 七/语言文风 八/实体清单 九/章间关联*
