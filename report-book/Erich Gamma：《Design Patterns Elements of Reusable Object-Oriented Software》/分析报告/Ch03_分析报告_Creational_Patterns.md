# Ch03《Creational Patterns》分析报告

**行号范围**：L1702—L3080（章题 L1704—1706；引言 L1706—1819；Abstract Factory L1821—2074；Builder L2076—2332；Factory Method L2334—2607；Prototype L2609—2851；Singleton L2853—3054；Discussion L3056—3080）
**全书功能**：模式目录第一部分。创建型模式抽象实例化过程，使系统独立于对象的创建、组合与表示方式；五个模式共用"迷宫游戏"统一示例，便于对比。

---

## 一、章节定位与功能

创建型模式解决"系统如何知道创建哪些具体类、如何创建、由谁创建、何时创建"的问题（L1712）。类创建型模式（Factory Method）用继承改变被实例化的类；对象创建型模式（其余四个）把实例化委托给另一对象（L1708）。本章以"创建迷宫"为统一动机：硬编码 `new Room/Wall/Door` 的 CreateMaze 函数"问题不在大小而在不灵活"（L1803），五种模式分别给出去除具体类显式引用的途径（L1809—1819）。

---

## 二、结构分析

| 节 | 行号 | 功能 |
|---|---|---|
| 章引言（迷宫示例） | L1706—1819 | 定义创建型模式的主题；MapSite/Room/Wall/Door/Maze/MazeGame 基础类；CreateMaze 的硬编码问题；五种模式的解决路径预告 |
| Abstract Factory | L1821—2074 | 意图：创建相关产品族而不指定具体类（L1823—1825）；迷宫/外观示例；MazeFactory、BombedMazeFactory、EnchantedMazeFactory |
| Builder | L2076—2332 | 意图：将复杂对象的构建与表示分离（L2078）；MazeBuilder、StandardMazeBuilder、CountingMazeBuilder；RTF 阅读器示例 |
| Factory Method | L2334—2607 | 意图：定义创建对象的接口，让子类决定实例化哪个类（L2336—2338）；MazeGame 的 MakeMaze；文档应用框架示例 |
| Prototype | L2609—2851 | 意图：以原型实例指定待创建对象种类，复制原型创建新对象（L2611）；MazePrototypeFactory；图形编辑器 GraphicTool 示例 |
| Singleton | L2853—3054 | 意图：保证一个类只有一个实例并提供全局访问点（L2855—2857）；迷宫单例；注册表变体 |
| Discussion of Creational Patterns | L3056—3080 | 两种参数化方式对比（子类化 vs 工厂对象）；图形编辑器三方案权衡；进化路径（Factory Method→其他） |

---

## 三、内容分析

### 1. 统一示例的价值（L1706—1819）
迷宫示例的"组件类可变"问题（普通迷宫→魔法迷宫：DoorNeedingSpell、EnchantedRoom，L1807）为五个模式提供同一动机：如何让 CreateMaze 不硬编码具体类。四个模式给出四条不同途径（虚拟函数、工厂参数、构建器参数、原型参数，L1811—1817），Singleton 则解决"每游戏一个迷宫"的全局访问（L1819）——这是全书最清晰的"同题异构"教学结构。

### 2. Abstract Factory（L1821—2074）
- 动机：外观（Look-and-Feel）系统需创建相关 widget 族（L1831—1843）。
- 关键机制：抽象工厂接口声明每个产品的创建操作（L1857—1861），具体工厂返回具体产品；客户端只与抽象产品接口交互。
- 实现要点：工厂作为 Singleton（L1903 附近）、产品用 Prototype 创建（L1903 附近）、可扩展工厂（L1903 附近）。
- 后果：隔离具体类、易于交换产品族、难以支持新产品种类（L1891 附近）。
- 示例：MazeFactory/BombedMazeFactory/EnchantedMazeFactory（L1946—2064）。

### 3. Builder（L2076—2332）
- 动机：RTF 阅读器——同一格式转换过程需生成多种表示（文本、ASCII、TeX 控件，L2082—2096）。
- 关键机制：Director 调用 Builder 的逐步构建操作（BuildWall/BuildDoor…）；Builder 与 Director 分离使"构建过程"与"表示"独立变化（L2108—2146）。
- 对比 Abstract Factory：工厂立即返回产品，Builder 分步构建复杂产品（L2146 附近）。
- 示例：StandardMazeBuilder 追踪房间位置、CountingMazeBuilder 计数（L2174—2314）。

### 4. Factory Method（L2334—2607）
- 动机：文档应用框架——Application/ Document 框架需创建具体 Document 子类，框架不知道具体类（L2344—2358）。
- 关键机制：Creator 用抽象工厂操作（CreateDocument）延迟实例化，ConcreteCreator 覆盖之（L2368—2398）。
- 实现：参数化工厂方法（L2422 附近）、C++ 模板化变体（L2422 附近）、"钩子"（L2422 附近）。
- 后果：消除对具体类的耦合，代价是需子类化 Creator（L2398 附近）。
- 示例：MazeGame::MakeMaze 返回 Maze 组件（L2525—2589）；MyDocument 应用。

### 5. Prototype（L2609—2851）
- 动机：图形编辑器——用调色板中的图形原型创建新图形，避免为每种图形建工厂类（L2615—2631）。
- 关键机制：原型实现 Clone/复制自身；客户端以原型为参数请求新产品（L2641—2663）。
- 实现：C++ 深浅拷贝问题（L2687 附近）、原型注册表（L2687 附近）、Clone 与初始化解耦（L2687 附近）。
- 后果：运行时增减产品类、减少子类数、可动态配置；代价是每个类实现 Clone、复制语义复杂（L2663 附近）。
- 示例：MazePrototypeFactory 以原型参数化（L2709—2837）；GraphicTool 的 NewGraphic（L2709 附近）。

### 6. Singleton（L2853—3054）
- 动机：需要全局唯一实例且不允许客户端自由构造（打印机池、文件系统等，L2859—2865）。
- 关键机制：静态 Instance() 操作 + 私有构造；经典 C++ 实现用静态实例 + 返回引用（L2996 附近）。
- 实现变体：线程安全与延迟初始化之争（L2905 附近）、子类化单例、注册表式单例（L2905 附近）。
- 后果：受控访问唯一实例、减少全局变量、可细粒度控制实例数（L2891 附近）；批评点：多线程与测试困难（L2891 附近）。
- 示例：MazeFactory 单例化（L3002—3046）。

### 7. Discussion（L3056—3080）
- 参数化系统的两条路：子类化创建者（Factory Method）vs 引入工厂对象（Abstract Factory/Builder/Prototype）（L3058—3060）。
- 图形编辑器三方案权衡：Factory Method 最易起步但子类增殖；Abstract Factory 需同等大的工厂层次；Prototype 只需 Clone 最省类（L3062—3076）。
- 进化路径：设计常从 Factory Method 起步，随灵活性需求演化到其他三模式（L3080）。

---

## 四、逻辑梳理

本章论证主线是"**同一问题、五条解法**"的比较逻辑：
1. 先确立问题：创建对象的硬编码导致对具体类的依赖（L1803—1809）；
2. 逐模式展开：每个模式回答"谁创建、何时创建、如何换产品"，并在 13 节模板内给出动机→机制→实现→权衡；
3. 末节横向比较：类机制（继承）vs 对象机制（委托/组合）两条参数化路线（L3058），给出选择判据与进化路径（L3080）。

模式间的关系网络（Related Patterns 节）：Builder 可用其他创建模式实现组件（L2328 附近）；Prototype 可用 Singleton（L2847 附近）；Abstract Factory 常实现为 Singleton（L2070 附近）；Factory Method 是 Template Method 的特例（L2599 附近）。

---

## 五、材料使用方式

1. **统一迷宫示例**：同一领域（迷宫构建）贯穿五模式，材料复用最大化，使差异（五条创建途径）成为对比焦点（L1706—1819、L1809—1819）。
2. **第二领域示例**：每个模式另有独立动机故事——外观系统（Abstract Factory，L1831）、RTF 阅读器（Builder，L2082）、文档框架（Factory Method，L2344）、图形编辑器（Prototype，L2615）、全局唯一对象（Singleton，L2859）。
3. **C++ 代码全量示例**：每个模式含可运行风格代码（如 CreateMaze L1785—1801、MazeGame::MakeMaze L2525 附近），Smalltalk 要点散见（L1732 方向符号）。
4. **实现细节清单**：Implementation 节枚举语言相关陷阱（C++ 深浅拷贝 L2687 附近、静态初始化顺序 L2905 附近），材料服务于"可操作性"。

---

## 六、论辩与阐述方法

1. **同题异构对比法**：五模式共享动机，差异即论点——作者借此说明"选择哪种创建模式取决于变化维度"（产品族 vs 构建步骤 vs 子类 vs 原型 vs 唯一性）。
2. **参数化维度论证**：Discussion 把选择问题归结为"以什么为参数"（类 vs 工厂对象 vs 构建器 vs 原型），并以图形编辑器三方案的成本收益表收束（L3062—3076）。
3. **权衡话语**：每个模式的 Consequences 都给出收益/代价对（如 Prototype 的"运行时灵活 vs 复制语义复杂"，L2663 附近）。
4. **进化叙事**：L3080 提出"Factory Method→Abstract Factory/Prototype/Builder"的演化路径，把模式选择从静态分类转为动态设计过程。

---

## 七、语言文风摘录（附行号）

- "Creational design patterns abstract the instantiation process."（L1708）
- "The real problem with this member function isn't its size but its inflexibility."（L1803）
- "It hard-codes the maze layout."（L1803）
- "The creational patterns show how to make this design more flexible, not necessarily smaller."（L1805）
- "This approach is an example of the Factory Method (107) pattern."（L1811）
- "Often, designs start out using Factory Method and evolve toward the other creational patterns…"（L3080）

---

## 八、实体清单（六类，附行号证据）

**人物**：Erich Gamma、Richard Helm、Ralph Johnson、John Vlissides（作者，全章以 we 出现）；Knuth（Knu84 在 Builder 示例 TeX 提及语境）。
**著作/作品**：无独立外部著作（示例系统为虚构）；RTF 阅读器示例（L2082）。
**概念**：creational pattern（L1706）；class/object creational pattern（L1708）；Abstract Factory（L1821）；product family（L1185 前章、本章 L1861 附近）；Builder（L2076）；Director（L2108 附近）；Factory Method（L2334）；Creator/ConcreteCreator（L2368 附近）；Prototype（L2609）；Clone（L2641 附近）；Singleton（L2853）；Instance 操作（L2879 附近）；parameterization（L3058）；maze 组件类 MapSite/Room/Wall/Door/Maze/MazeGame（L1734—1779）；EnchantedRoom/DoorNeedingSpell（L1807）。
**机构**：C++（示例语言）；Smalltalk（L1732）；Motif（外观示例语境，L1831 附近）。
**地点**：无独立地点实体。
**事件**：无历史事件（示例均为虚构设计场景）。

---

## 九、与前后章关联

- **承接第 1—2 章**：Factory Method 是 1.6"创建对象间接化"（L808—810）的实现；Abstract Factory 已在 2.5 以 GUIFactory 亮相（L1183），本章给出完整模板；Singleton 在 2.5 被提及管理 guiFactory（L1161）。
- **开启第 4 章**：创建型模式与结构型模式的互补（创建对象 vs 组装对象）在 Discussion 后自然过渡；第 4 章引言（L3084—3088）从"组合接口/实现"接续。
- **与第 6 章呼应**：L10209 脚注指出 Abstract Factory/Builder/Prototype "都封装关于对象如何被创建的知识"——这正是 6.3 讨论的"封装变化"主题在创建型上的体现。
