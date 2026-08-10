# Ch02《A Case Study: Designing a Document Editor》分析报告

**行号范围**：L920—L1700（章题 L920—922；2.1 L932；2.2 L952；2.3 L1018；2.4 L1058；2.5 L1110；2.6 L1187；2.7 L1333；2.8 L1434；2.9 Summary L1678）
**全书功能**：全书唯一的贯穿案例章。以 WYSIWYG 文档编辑器 Lexi 的七个设计问题为纲，逐一引出八个设计模式（Composite、Strategy、Decorator、Abstract Factory、Bridge、Command、Iterator、Visitor），示范"模式如何在一个真实系统中协作"。作者明言其设计基于 Calder 的 Doc 文本编辑应用（L10145 脚注）。

---

## 一、章节定位与功能

第 2 章是全书方法论的中枢：把第 1 章的抽象原则（面向接口编程、优先组合、封装变化）落实为一次完整的设计演练。七个问题（文档结构、格式化、界面修饰、多外观标准、多窗口系统、用户操作、拼写检查与断字）对应八个模式，且每个问题的解决都遵循同一套路：**陈述目标与约束→分析备选方案→选定方案→点出对应模式**。

---

## 二、结构分析

| 节 | 行号 | 功能 |
|---|---|---|
| 2.1 Design Problems | L932—950 | 列举七个设计问题，说明每个问题的目标/约束/模式对应关系 |
| 2.2 Document Structure | L952—1016 | 递归组合表示文档；Glyph 抽象类（Draw/Bounds/Intersects/子结构接口）；引出 Composite |
| 2.3 Formatting | L1018—1056 | 封装格式化算法；Compositor/Composition 分离；引出 Strategy |
| 2.4 Embellishing the User Interface | L1058—1108 | 透明封装；MonoGlyph（Border/Scroller）；引出 Decorator |
| 2.5 Supporting Multiple Look-and-Feel Standards | L1110—1185 | 抽象对象创建；GUIFactory/产品类；引出 Abstract Factory |
| 2.6 Supporting Multiple Window Systems | L1187—1331 | Window/WindowImp 双层次；WindowSystemFactory 配置；引出 Bridge |
| 2.7 User Operations | L1333—1432 | 请求封装为 Command 对象；撤销/重做与命令历史；引出 Command |
| 2.8 Spelling Checking and Hyphenation | L1434—1676 | 访问与遍历封装（Iterator）；分析与遍历分离；Accept/Visit 双重分派；引出 Visitor |
| 2.9 Summary | L1678—1700 | 总结八个模式并扩展到其他应用域 |

---

## 三、内容分析

### 2.2 文档结构：递归组合与 Glyph
- 七个问题之首（L936）：内部表示影响编辑/格式化/显示/分析全部环节。
- 关键约束：文本与图形统一对待、单元素与组元素统一对待（L966—968）。
- 递归组合（L972—985）：字符→行→列→页的逐层嵌套；每个元素一个对象。
- Glyph 抽象类（L987—1012）：三类责任——绘制（Draw）、空间（Bounds/Intersects）、结构（Insert/Remove/Child/Parent）。
- 结论：Composite 模式（L1014—1016）。

### 2.3 格式化：算法封装
- 格式化=断行（L1022）；质量/速度权衡、速度/存储权衡（L1026）。
- Compositor（算法）与 Composition（上下文）分离（L1032—1050）：SimpleCompositor、TeXCompositor（L1048）。
- 结论：Strategy 模式（L1052—1056）；"接口要足够通用以支持算法族"是关键（L1056）。

### 2.4 界面修饰：透明封装
- 继承式装饰导致"每种子类组合一个类"的爆炸（BorderedComposition、ScrollableComposition、BorderedScrollableComposition…L1066）。
- 透明封装 = 单子组合 + 兼容接口（L1072）；MonoGlyph 转发全部请求（L1076—1086）；Border::Draw 先调父类再画边框（L1088—1092）。
- 结论：Decorator 模式（L1106—1108），"embellishment"广义化。

### 2.5 多外观标准：抽象创建
- 约束：不能在代码里硬编码 `new MotifScrollBar`（L1132、L1140）；要能整体替换 widget 族（L1134）。
- GUIFactory 抽象类 + MotifFactory/PMFactory 等具体工厂（L1136—1160）；工厂实例来源任意（全局/静态/局部），可用 Singleton 管理（L1161）。
- 结论：Abstract Factory 模式（L1183—1185），强调"产品族"区别于其他创建模式。

### 2.6 多窗口系统：抽象与实现分离
- 为何不能用 Abstract Factory？厂商类层次不兼容、无共同抽象产品类（L1195）；且不能自建窗口系统（L1197）。
- 交集/并集两种极端接口哲学均不可行（L1215—1217）；取"流行特性"中间路线。
- Window（应用视角）与 WindowImp（系统视角）双层次（L1234—1240）；WindowImp 子类（XWindowImp、PMWindowImp，L1257—1290）；WindowSystemFactory 配置 `_imp`（L1296—1323）。
- 结论：Bridge 模式（L1325—1331）：两个可独立演化的层次协作。

### 2.7 用户操作：请求对象化
- 需求：多界面访问同一操作、撤销/重做、不限层数（L1351—1355）。
- 不能为每个请求建 MenuItem 子类（类数爆炸，L1365—1367）；参数化函数有三大缺陷（无撤销、难存状态、难扩展，L1369—1375）。
- Command 抽象类 + Execute（L1381）；Unexecute 撤销（L1394）；Reversible 运行时判断可撤销性（L1398）；命令历史与"present"指针（L1400—1426）。
- 结论：Command 模式（L1428—1432）。

### 2.8 拼写检查与断字：遍历与分析的分离
- 两部分难题：访问散布信息（遍历）与执行分析（L1442）。
- 遍历封装：把遍历机制从 Glyph 接口中移出（整数索引会偏向特定数据结构，L1454—1456）；Iterator 抽象类 + ArrayIterator/ListIterator/PreorderIterator/NullIterator（L1487—1542）。
- 结论一：Iterator 模式（L1544—1546）。
- 分析封装：拒绝 type test/downcast（L1569—1583）；CheckMe(SpellingChecker&) 双重分派（L1587—1593）；推广为 Accept(Visitor&)（L1664）。
- 结论二：Visitor 模式（L1672—1676），并指出其适用判据："哪个类层次变化更频繁"（L1676）。

### 2.9 Summary
八个模式清单（L1680—1696）；扩展到金融投资组合（Composite）、编译器寄存器分配（Strategy）、GUI（Decorator+Command）（L1698）。

---

## 四、逻辑梳理

本章有一条主论证链："**表示（2.2）→ 布局（2.3）→ 修饰（2.4）→ 外观（2.5）→ 平台（2.6）→ 交互（2.7）→ 分析（2.8）**"，从文档内核逐层向外到用户与分析功能，每个环节都因"某方面需要独立变化"而引出模式：

- 结构需任意嵌套 → Composite（组合变化）
- 算法需可替换 → Strategy（算法变化）
- 责任需动态增减 → Decorator（责任变化）
- 产品族需整体切换 → Abstract Factory（产品族变化）
- 实现平台需隐藏 → Bridge（实现变化）
- 请求需可撤销可排队 → Command（请求变化）
- 遍历需多形态 → Iterator（访问变化）
- 分析需开放扩展 → Visitor（操作变化）

这正是第 1 章"为变化而设计"（L798）与"封装变化的概念"的实战展开，八个模式对应 Table 1.2 中的八种可变方面。

---

## 五、材料使用方式

1. **单一贯穿案例**：Lexi 从零设计，问题、约束、C++ 代码与对象图全部自洽，构成"完整设计叙事"而非孤立示例。
2. **代码即证据**：每节配真实风格 C++ 代码（Glyph 接口 L995、MonoGlyph::Draw L1083、Window::DrawRect L1251、Command 历史 L1400 区、PreorderIterator L1512—1540、CheckMe L1591），代码承担论证功能。
3. **反例驱动**：先演示错误方案（继承装饰爆炸 L1066、硬编码构造 L1132、type test L1569—1583、遍历枚举 L1479），再引入模式——"先破后立"在第 2 章成为固定修辞。
4. **脚注学术溯源**：Lexi 基于 Calder 的 Doc（L10145）；glyph 术语由 Calder 首创（L10149）；MVC 客户实为事件分发器（L10161）。

---

## 六、论辩与阐述方法

1. **约束—方案匹配法**：每个问题先列目标与约束（L958—970 等），方案必须逐一满足，模式因此显得"被设计逼出来"而非强加。
2. **方案比较表**：如 2.6 的"交集 vs 并集"哲学（L1215—1217）、2.7 的"函数 vs 对象参数化"（L1369—1377）。
3. **可运行时变化论证**：反复强调"运行时可改"（换 compositor L1050、换装饰顺序 L1100—1102、换 WindowImp L1232、撤销/重做 L1400—1426），把动态性作为模式价值的核心证据。
4. **模式名即时点题**：每节结尾以小标题"XX Pattern"收束，形成"问题→解决→命名"的教学节奏。

---

## 七、语言文风摘录（附行号）

- "A document is ultimately just an arrangement of basic graphical elements…"（L954）
- "We can treat text and graphics uniformly…"（L983）
- "…we shouldn't use inheritance to add them to the user interface."（L1060）
- "Clients generally can't tell whether they're dealing with the component or its enclosure."（L1072）
- "What varies is the window system implementation."（L1232）
- "Here we have another example of encapsulating the concept that varies, in this case a request."（L1377）
- "This code is pretty ugly."（L1583，指 type-test 代码）

---

## 八、实体清单（六类，附行号证据）

**人物**：Calder（L10145、L10149 脚注）；作者四人组（以 we 贯穿）；Knu84（TeX，L1048 文献引注）。
**著作/作品**：Doc 文本编辑器（L10145）；TeX 排版算法（L1048）。
**概念**：Lexi（L924）；WYSIWYG（L924）；Glyph（L987）；recursive composition（L972）；Composite pattern（L1014）；Compositor/Composition（L1032）；Strategy pattern（L1052）；transparent enclosure（L1062）；MonoGlyph（L1074）；Decorator pattern（L1106）；GUIFactory（L1150）；Abstract Factory pattern（L1183）；Window/WindowImp（L1234）；WindowSystemFactory（L1300）；Bridge pattern（L1325）；Command/Unexecute/Reversible（L1381—1398）；command history（L1400）；Iterator/NullIterator/PreorderIterator（L1487—1510）；Visitor/Accept（L1653—1664）；discretionary glyph（L1666—1668）。
**机构**：Motif（L1128）；Presentation Manager（L1128）；X Window System（L1257）；Macintosh（L1189）；Windows（L1189）；C++（示例语言）。
**地点**：无独立地点实体（窗口系统名含平台属性）。
**事件**：无历史事件（本章为虚构设计演练，引 Calder 的 Doc 为现实参照）。

---

## 九、与前后章关联

- **承接第 1 章**：把 1.6 的原则与 Table 1.2 的可变方面逐一实例化；"先破后立"与"封装变化"话语直接继承（L1377 与 L1232 同构）。
- **开启第 3—5 章**：八个模式在目录章中均以完整 13 节模板重述；第 2 章提供了它们的"第一遍阅读场景"，目录章则提供"第二遍系统学习"。例如 2.2 明确指示"现在正是转向 Composite (163) 研读的时机"（L1016）。
- **与第 6 章呼应**：2.9 的"模式组合"思想（L1698）在第 6 章 6.5 被 Alexander 的"密度"引语升华（L8290）。
