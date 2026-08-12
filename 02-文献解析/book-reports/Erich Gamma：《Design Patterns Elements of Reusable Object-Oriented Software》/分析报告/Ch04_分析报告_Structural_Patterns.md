# Ch04《Structural Patterns》分析报告

**行号范围**：L3082—L4996（章题 L3082—3084；引言 L3084—3098；Adapter L3100—3367；Bridge L3369—3657；Composite L3659—3950；Decorator L3952—4177；Facade L4179—4392；Flyweight L4394—4653；Proxy L4655—4966；Discussion L4968—4996）
**全书功能**：模式目录第二部分。结构型模式关注"类与对象如何组合成更大结构"；类模式用继承组合接口/实现，对象模式用组合在运行时组装对象。

---

## 一、章节定位与功能

结构型模式回答"如何组装"：类结构模式（多重继承、类版 Adapter）在编译期静态组合，对象结构模式在运行期动态组合（L3086—3088）。本章七个模式覆盖接口适配（Adapter）、抽象/实现分离（Bridge）、整体-部分（Composite）、责任动态添加（Decorator）、子系统门面（Facade）、细粒度共享（Flyweight）、访问代理（Proxy），末节集中比较三组相近模式（L4972—4996）。

---

## 二、结构分析

| 节 | 行号 | 功能 |
|---|---|---|
| 章引言 | L3084—3098 | 界定结构模式范围；预览七模式（Composite/Proxy/Flyweight/Facade/Bridge/Decorator） |
| Adapter | L3100—3367 | 意图：将类接口转换为客户端期望的另一接口（L3102—3104）；别名 Wrapper（L3108）；绘图编辑器 TextView/Shape 示例；类版与对象版 |
| Bridge | L3369—3657 | 意图：将抽象与实现解耦，使二者可独立变化（L3371）；Window/WindowImp 与用户界面库示例 |
| Composite | L3659—3950 | 意图：将对象组合成树形结构以表示整体-部分层次，使客户端统一对待单个与组合对象（L3661—3663）；图形/设备示例 |
| Decorator | L3952—4177 | 意图：动态给对象添加责任，是继承的灵活替代（L3954—3956）；GUI 边框/滚动示例 |
| Facade | L4179—4392 | 意图：为子系统中的一组接口提供统一界面（L4181—4183）；编译器的 Scanner/Parser/ProgramNode/CodeGenerator 示例 |
| Flyweight | L4394—4653 | 意图：通过共享支持大量细粒度对象的高效使用（L4396—4398）；文档编辑器的字符/行/列共享示例 |
| Proxy | L4655—4966 | 意图：为另一对象提供替身或占位符以控制访问（L4657—4659）；文档编辑器图像代理示例 |
| Discussion of Structural Patterns | L4968—4996 | Adapter vs Bridge；Composite vs Decorator vs Proxy |

---

## 三、内容分析

### 1. Adapter（L3100—3367）
- 动机：复用"接口不匹配"的现成类（TextView）于应用（Shape 体系）——不改源码、不让工具箱迁就应用（L3116—3119）。
- 两种形式：类 Adapter（多重继承：继承 Shape 接口 + TextView 实现，L3120）；对象 Adapter（组合 TextView，L3120）。
- 关键点：适配器可补足被适配类缺失的功能（CreateManipulator 提供拖拽动画，L3126—3130）。
- 实现决策：适配程度（接口适配 vs 透明适配）、双向适配器（L3212 附近）。

### 2. Bridge（L3369—3657）
- 动机：一个抽象（Window 概念）可有多个实现（X、PM、Motif 窗口系统），若用继承则子类爆炸（L3379—3399）。
- 关键机制：Abstraction 持有 Implementor 引用，二者接口独立设计（L3419—3443）。
- 后果：接口与实现解耦、可扩展性提升、实现细节对客户端隐藏（L3443 附近）。
- 对比 Adapter：Bridge 是"事先设计"的分离，Adapter 是"事后修补"的适配（L4976—4978）。

### 3. Composite（L3659—3950）
- 动机：绘图编辑器需统一处理基本图形（Line）与组合图形（Picture）（L3667—3675）。
- 关键机制：Component 抽象类统一 Leaf 与 Composite 接口；Composite 递归包含子组件（L3711 附近）。
- 实现注意：子指针管理、组件排序、缓存（L3703 附近）；透明性 vs 安全性之争（L3703 附近）。
- 后果：客户端代码简化、易加新组件类型；代价是接口过度泛化、难以限制子类型（L3699 附近）。

### 4. Decorator（L3952—4177）
- 动机：给 GUI 组件动态加边框/滚动条，避免继承式"每组合一个类"（L3958—3966）。
- 关键机制：Decorator 与 Component 同接口，转发并可在前后附加行为（L3968—3976）。
- 与继承对比：可运行时增减、避免类爆炸；代价是产生大量相似小对象、与标识（identity）相关操作失效（L3978 附近）。
- 注意：与 Composite 结构相似但意图不同（L4984—4988）。

### 5. Facade（L4179—4392）
- 动机：编译器子系统（Scanner/Parser/ProgramNode/CodeGenerator）接口复杂，客户端只需 Compile 一个入口（L4181—4193）。
- 关键机制：Facade 转发请求给子系统对象，子系统不知 Facade 存在（L4215 附近）。
- 后果：屏蔽子系统复杂性、松耦合、不阻止高级用户直用子系统（L4205 附近）。
- 与 Adapter 区别：Facade 定义新接口，Adapter 复用旧接口（L4980）。

### 6. Flyweight（L4394—4653）
- 动机：文档编辑器每字符一对象导致存储爆炸；共享字符对象 + 外部化位置/字体等"外在状态"（L4396—4408）。
- 关键机制：内在状态（可共享，如字符码）与外在状态（由客户端传入，如行/列位置）分离（L4428 附近）；FlyweightFactory 管理共享池（L4428 附近）。
- 后果：大幅节省空间；代价是状态外部化增加运行时开销、逻辑复杂（L4416 附近）。
- 与 Composite 结合：共享叶子（L4456 附近）。

### 7. Proxy（L4655—4966）
- 动机：文档中嵌入大图像——加载代价高，需"按需加载"替身（L4657—4679）。
- 四种常见用途：远程代理、虚代理（延迟加载）、保护代理、智能引用（L4681 附近）。
- 关键机制：Proxy 与 Subject 同接口，持有真实对象引用并转发（L4731 附近）。
- 与 Decorator 区别：Proxy 控制访问、不动态增减责任（L4990—4994）。

### 8. Discussion（L4968—4996）
- **Adapter vs Bridge**：同为间接层+转发，但意图不同——Adapter 解决已存在接口的不兼容（事后），Bridge 是预先设计抽象与实现独立演化（事前）（L4974—4978）。
- **Composite vs Decorator vs Proxy**：三者结构图相似（都递归组合/持引用转发），意图迥异——Composite 关注统一表示，Decorator 关注动态加责任，Proxy 关注访问控制（L4982—4996）；并指出二者可混用（proxy-decorator 混合体，L4996）。

---

## 四、逻辑梳理

本章主线是"**组装方式的四种基本形态**"：
1. **接口层适配**（Adapter）：让不兼容接口协同；
2. **维度分离**（Bridge）：抽象与实现两维独立变化；
3. **结构递归**（Composite）：整体-部分统一对待；
4. **单点包装**（Decorator/Facade/Proxy）：分别包装对象、子系统、访问路径；
5. **共享压缩**（Flyweight）：以共享降存储。

Discussion 以"结构相似≠意图相同"为总命题（L4970），通过三组对比（Adapter/Bridge、Composite/Decorator、Decorator/Proxy）示范如何按意图而非按结构图选模式——这是对 1.7 选型指南的方法论补充。

---

## 五、材料使用方式

1. **领域示例复用**：绘图编辑器（Adapter/Composite/Flyweight）、文档编辑器（Decorator/Flyweight/Proxy）、用户界面库（Bridge）、编译器（Facade）——真实软件领域作为模式动机来源。
2. **结构图+对象图**：每模式 Structure 节配类图，Motivation 配对象图/交互图（图引用散见各节）。
3. **语言相关实现提示**：C++ 的 private inheritance 用于类 Adapter（L3086）、引用计数（Proxy 的 Smart Reference，L4681 附近）、const 正确性（Flyweight 外在状态，L4428 附近）。
4. **对比表格化**：Discussion 用三组对比把"相似模式如何区分"材料化，是全章方法论精华。

---

## 六、论辩与阐述方法

1. **意图优先论**：反复强调"结构相似但意图不同"（L4970、L4984、L4990），把"为什么不用结构图分类"作为核心论证。
2. **成本-收益对称论证**：每个模式 Consequences 同时列收益与代价（如 Decorator 的"大量小对象" L3978 附近、Flyweight 的"外在状态开销" L4416 附近）。
3. **事前后对照**：Adapter 是"设计之后让它工作"，Bridge 是"设计之前让它工作"（L4978）——用时间维度区分模式。
4. **递归与共享的数学化表述**：Composite 的"开放末端的对象数"（L4984）、Flyweight 的"空间效率"（L3092）——用可度量后果支撑论证。

---

## 七、语言文风摘录（附行号）

- "Convert the interface of a class into another interface clients expect."（L3104，Adapter Intent）
- "Decouple an abstraction from its implementation so that the two can vary independently."（L3371 附近，Bridge Intent）
- "Compose objects into tree structures to represent part-whole hierarchies."（L3661—3663 附近，Composite Intent）
- "Attach additional responsibilities to an object dynamically."（L3954 附近，Decorator Intent）
- "Provide a unified interface to a set of interfaces in a subsystem."（L4181—4183 附近，Facade Intent）
- "Use sharing to support large numbers of fine-grained objects efficiently."（L4396—4398 附近，Flyweight Intent）
- "The Adapter pattern makes things work after they're designed; Bridge makes them work before they are."（L4978）

---

## 八、实体清单（六类，附行号证据）

**人物**：作者四人组（以 we 出现）；无外部人物。
**著作/作品**：无外部著作；示例系统：绘图编辑器（L3114）、编译器子系统（L4179 附近）、文档编辑器（L4396 附近）、NEXTSTEP NXProxy（L10181 脚注）。
**概念**：Adapter/Wrapper（L3100—3108）；class adapter/object adapter（L3086、L3120）；Bridge（L3369）；Abstraction/Implementor（L3419 附近）；Composite（L3659）；Component/Leaf（L3711 附近）；Decorator（L3952）；Facade（L4179）；Flyweight（L4394）；intrinsic/extrinsic state（L4428 附近）；FlyweightFactory（L4428 附近）；Proxy（L4655）；remote/virtual/protection/smart-reference proxy（L4681 附近）；multiple inheritance（L3086）。
**机构**：Motif（L3379 附近窗口系统例）；Presentation Manager（L3379 附近）；X Window System（L3379 附近）；NEXTSTEP（L10181 脚注）。
**地点**：无独立地点实体。
**事件**：无历史事件。

---

## 九、与前后章关联

- **承接第 2 章**：Bridge（2.6）、Composite（2.2）、Decorator（2.4）已在 Lexi 中出现，本章给出完整模板与更多实现细节；Flyweight 呼应 2.2 脚注的"Calder 的 glyph 共享"（L10149）。
- **承接第 3 章**：结构模式常与创建模式配合（如 Flyweight 池由工厂管理，L4428 附近；Adapter 可配工厂创建被适配对象）。
- **开启第 5 章**：行为模式处理"对象间的职责分配与通信"，与本章的"静态组装"形成互补；第 5 章引言明确"行为模式描述对象间通信模式"（L5002）。
- **与第 6 章呼应**：L10209 脚注指出 Bridge"分离抽象与实现"也是"封装变化"主题；第 6 章 6.3 的社区讨论承接本章 Discussion 的对比方法论。
