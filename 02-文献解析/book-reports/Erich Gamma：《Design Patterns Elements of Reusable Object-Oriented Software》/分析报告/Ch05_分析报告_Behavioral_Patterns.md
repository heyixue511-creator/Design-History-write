# Ch05《Behavioral Patterns》分析报告

**行号范围**：L4998—L8160（章题 L4998—5000；引言 L5000—5012；Chain of Responsibility L5014—5280；Command L5282—5539；Interpreter L5541—5931；Iterator L5933—6347；Mediator L6349—6583；Memento L6585—6822；Observer L6824—7106；State L7108—7340；Strategy L7342—7594；Template Method L7596—7744；Visitor L7746—8083；Discussion L8085—8160）
**全书功能**：模式目录第三部分，也是最大的一部分。行为模式关注"算法与对象间职责分配"，不仅描述对象/类模式，还描述它们之间的通信模式（L5002）。十一章模式按"封装变化"主题组织，Discussion 从五个视角横向比较。

---

## 一、章节定位与功能

行为模式处理"控制流"问题：把复杂、难以在运行时追踪的控制流显性化为对象间的通信模式（L5002）。两个类模式（Template Method、Interpreter）用继承分配行为；九个对象模式用组合。本章 Discussion 是全书的模式比较方法论总汇：封装变化（L8087—8103）、对象作为参数（L8105—8109）、通信的封装 vs 分发（L8111—8121）、发送者-接收者解耦（L8123—8150）、总结（L8152—8160）。

---

## 二、结构分析

| 节 | 行号 | 功能 |
|---|---|---|
| 章引言 | L5000—5012 | 界定行为模式；预览 11 模式；MVC 中的 Observer 例 |
| Chain of Responsibility | L5014—5280 | 意图：解耦请求发送者与接收者，多个对象依次获得处理机会（L5016—5018）；GUI 上下文帮助示例 |
| Command | L5282—5539 | 意图：将请求封装为对象，支持参数化、排队、记录与撤销（L5284—5286）；菜单/工具按钮示例 |
| Interpreter | L5541—5931 | 意图：为语言定义文法表示与解释器（L5543 附近）；布尔表达式语言示例 |
| Iterator | L5933—6347 | 意图：提供顺序访问聚合元素的方法而不暴露内部表示（L5935 附近）；List/Traversal 示例 |
| Mediator | L6349—6583 | 意图：定义中介对象封装一组对象的交互方式（L6351 附近）；对话框 FontDialogDirector 示例 |
| Memento | L6585—6822 | 意图：在不破坏封装的前提下捕获并外部化对象内部状态（L6587 附近）；可撤销图形编辑器示例 |
| Observer | L6824—7106 | 意图：定义一对多依赖，主体变化时通知所有依赖者（L6826 附近）；MVC 分离示例 |
| State | L7108—7340 | 意图：对象内部状态改变时行为随之改变（L7110 附近）；TCP 连接状态示例 |
| Strategy | L7342—7594 | 意图：定义算法族并封装，使算法可互换（L7344 附近）；排版/换行策略示例 |
| Template Method | L7596—7744 | 意图：在操作中定义算法骨架，把部分步骤延迟到子类（L7598 附近）；应用框架步骤示例 |
| Visitor | L7746—8083 | 意图：表示作用于对象结构元素的操作，允许不修改元素类而定义新操作（L7748 附近）；编译器的节点访问示例 |
| Discussion of Behavioral Patterns | L8085—8160 | 五视角比较：封装变化、对象作参数、通信封装/分发、发送者-接收者解耦、总结 |

---

## 三、内容分析

### 1. Chain of Responsibility（L5014—5280）
- 动机：GUI 上下文帮助——按钮→对话框→应用，帮助请求沿对象链传递直到被处理（L5022—5034）。
- 关键机制：请求沿链转发，接收者隐式（L5032）；链可运行时组装。
- 实现：后继链的建立（构造器/引用）、请求表示（L5044 附近）。
- 后果：降低耦合、增强职责分配灵活性；代价是请求可能无人处理（L5038 附近）。

### 2. Command（L5282—5539）
- 动机：菜单项/工具按钮需以统一方式触发任意操作并支持撤销（L5286—5294）。
- 关键机制：Execute/Unexecute；命令对象参数化发送者；宏命令（L5306 附近）。
- 实现：撤销的存储策略、C++ 函数指针退化用法（L5318 附近）。
- 后果：解耦发送者-接收者、可组合命令、易扩展新命令；代价是类数量增加（L5310 附近）。

### 3. Interpreter（L5541—5931）
- 动机：布尔表达式语言需解析与求值（L5543 附近）。
- 关键机制：文法规则→类层次（NonterminalExpression/TerminalExpression），解释器是树上的操作（L5549 附近）。
- 实现：语法树的构建（L5565 附近）、共享终结符（Flyweight 结合，L5565 附近）。
- 后果：易扩展文法、易实现；代价是文法复杂时类爆炸（L5553 附近）。
- 作者提醒：仅在文法简单、效率非关键时使用（L5553 附近）。

### 4. Iterator（L5933—6347）
- 动机：聚合对象（List）需多种遍历方式而不暴露内部结构（L5937 附近）。
- 关键机制：外部迭代器 vs 内部迭代器（L5937 附近）；多遍历并发（L5973 附近）。
- 实现：健壮迭代器（结构变化处理，L5973 附近）、C++ 模板化（L5973 附近）。
- 后果：支持多种遍历、统一聚合接口、可并发多遍历；代价是迭代器与聚合耦合、遍历中修改结构有风险（L5965 附近）。
- 相关：与 Composite、Flyweight、Memento（游标）相关（L10191 脚注）。

### 5. Mediator（L6349—6583）
- 动机：对话框中的组件（按钮/列表）相互依赖会导致紧耦合——引入中介者集中交互（L6351—6363）。
- 关键机制：Colleague 只认识 Mediator；Mediator 路由请求（L6379 附近）。
- 实现：中介者的通信协议简化（L6391 附近）。
- 后果：减少子类化、集中控制流；代价是中介者可能变成"上帝对象"（L6383 附近）。

### 6. Memento（L6585—6822）
- 动机：图形编辑器的撤销需保存对象状态而不破坏封装（L6587—6595）。
- 关键机制：Originator 生成 Memento 并可用其恢复；Caretaker 保存但不读内部（L6603 附近）。
- 实现：C++ 友元、Memento 接口宽窄（L6615 附近）。
- 后果：封装保持、恢复简单；代价是 Memento 存储开销、Caretaker 需管理生命周期（L6607 附近）。

### 7. Observer（L6824—7106）
- 动机：MVC——模型变化时所有视图自动更新（L6826—6838）。
- 关键机制：Subject 维护 Observer 列表并通知；推送 vs 拉取模型（L6850 附近）。
- 实现：目标一致性、避免特定通知顺序依赖、C++ 中删除观察者（L6874 附近）。
- 后果：抽象耦合、支持广播通信；代价是意外更新、更新成本不可知（L6856 附近）。
- 与 Mediator 对比：Observer 分发通信，Mediator 集中通信（L8113—8115）。

### 8. State（L7108—7340）
- 动机：TCP 连接的状态机行为——每个状态的行为封装为 State 子类（L7110—7118）。
- 关键机制：Context 委托给当前 State 对象；状态转移=换 State 对象（L7126 附近）。
- 实现：谁定义转移（Context vs State）、表驱动 vs 类层次（L7150 附近）。
- 后果：状态行为局部化、转移显式化；代价是状态类数量（L7142 附近）。
- 与 Strategy 区分：State 封装状态相关行为，Strategy 封装算法（L7336 附近）。

### 9. Strategy（L7342—7594）
- 动机：排版算法的族（简单/TeX 换行）可互换（L7344—7352）。
- 关键机制：Context 持有 Strategy 引用，委托算法；策略间数据传递（L7362 附近）。
- 实现：策略参数化、默认策略（L7382 附近）。
- 后果：替代继承、消除条件语句、算法族可复用；代价是客户端需了解策略差异（L7374 附近）。

### 10. Template Method（L7596—7744）
- 动机：应用框架的算法骨架（打开文档/构建应用）固定，步骤由子类实现（L7598—7606）。
- 关键机制：模板方法调用抽象/钩子操作；子类只填具体步骤（L7614 附近）。
- 实现：最小化原语操作数、命名约定（L7630 附近）。
- 后果：复用骨架、控制反转；代价是子类需理解骨架结构（L7626 附近）。
- 与 Factory Method/Strategy 相关（L7740 附近）。

### 11. Visitor（L7746—8083）
- 动机：编译器需对语法树做多种操作（类型检查、代码生成、格式化），不愿每加一操作就改所有节点类（L7748—7756）。
- 关键机制：Accept/Visit 双重分派；每个元素类一个 Visit 操作（L7772 附近）。
- 实现：双分派机制、C++ 无内建双分派（L7786 附近）。
- 后果：操作集中、易加新操作；代价是加新元素类须改所有 Visitor（L7780 附近）。
- 适用判据：结构稳定而操作多变时最合适（L1676 与本章重复）。

### 12. Discussion（L8085—8160）
- **封装变化**（L8087—8103）：Strategy/State/Mediator/Iterator 均封装易变方面。
- **对象作参数**（L8105—8109）：Visitor 是 Accept 的参数；Command/Memento 是"魔法令牌"。
- **通信封装 vs 分发**（L8111—8121）：Observer 分发 vs Mediator 集中；Observer 更易复用、Mediator 更易理解。
- **发送者-接收者解耦**（L8123—8150）：Command（一对一绑定对象）、Observer（一对多信号）、Mediator（集中路由）、Chain of Responsibility（隐式链）四种解耦各有取舍。
- **总结**（L8152—8160）：行为模式互补强化；模式级组合（而非类级）带来"协同"（synergy）。

---

## 四、逻辑梳理

本章按"职责如何分配"组织论证：
1. **请求传递**（Chain of Responsibility）：谁处理请求——沿链隐式分配；
2. **请求封装**（Command）：请求何时、如何执行——对象化；
3. **语言表示**（Interpreter）：文法如何表示与求值——类层次；
4. **访问抽象**（Iterator）：如何遍历——外部化；
5. **交互集中**（Mediator）：对象间如何通信——中介；
6. **状态外部化**（Memento）：状态如何保存——备忘录；
7. **依赖传播**（Observer）：变化如何通知——订阅；
8. **状态行为**（State）：行为如何随状态变——状态对象；
9. **算法族**（Strategy）：算法如何互换——策略对象；
10. **骨架复用**（Template Method）：步骤如何延迟——模板；
11. **操作扩展**（Visitor）：操作如何加——双分派。

Discussion 的五视角构成一条"从变化点到通信形态"的收束论证：先问"什么在变"（封装变化），再问"对象以何种角色参与"（参数/令牌），再问"通信集中还是分发"，最后落到"解耦的四种形态"（L8123—8150），并以模式组合的协同作结（L8152—8160）。

---

## 五、材料使用方式

1. **领域示例**：GUI 帮助（Chain of Responsibility）、菜单命令（Command）、布尔表达式（Interpreter）、聚合遍历（Iterator）、对话框（Mediator）、图形撤销（Memento）、MVC（Observer）、TCP 连接（State，L10201 脚注基于 Lynch & Rose）、排版（Strategy）、应用框架（Template Method）、编译器（Visitor）。
2. **MVC 复用**：Observer 直接以 MVC 为经典例证（L6826—6838、L5010），与第 1 章 1.2 呼应。
3. **代码示例**：每模式含 C++ 示例代码，Smalltalk 对照（如 Observer 的 message 参数化 L8121、Interpreter 的 Smalltalk 实现差异）。
4. **学术引证**：脚注引用 Booch 的内外迭代器术语（L10189）、Lynch & Rose 的 TCP 协议（L10201）、CLOS 多重分派（L10207）。

---

## 六、论辩与阐述方法

1. **对比式定义**：State vs Strategy（L7336 附近）、Observer vs Mediator（L8113—8115）、Command vs Memento（L8109）、外部 vs 内部迭代器（L10189）——用相邻模式互证边界。
2. **代价对称**：每个 Consequences 平衡收益与代价（如 Visitor 的"易加操作 vs 难加元素"L7780 附近）。
3. **适用判据前置**：Interpreter 明确"何时不该用"（L5553 附近）、Visitor 明确"哪个层次变化更频繁"（L1676、L7780 附近）——把模式选择理性化。
4. **解耦谱系**：Discussion 用"解耦的四种形态"（Command/Observer/Mediator/Chain of Responsibility）构建一个连续谱系，展示同一目标的不同权衡。

---

## 七、语言文风摘录（附行号）

- "Behavioral patterns are concerned with algorithms and the assignment of responsibilities between objects."（L5002）
- "Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request."（L5018）
- "Encapsulating variation is a theme of many behavioral patterns."（L8089）
- "The Observer pattern promotes partitioning and loose coupling…"（L8117）
- "…it's easier to understand the flow of communication in Mediator than in Observer."（L8119）
- "Composition at the pattern level rather than the class or object levels lets us achieve the same synergy with greater ease."（L8158—8160）

---

## 八、实体清单（六类，附行号证据）

**人物**：作者四人组（以 we 出现）；Booch（L10189 脚注）；Lynch、Rose（L10201 脚注）；Calder（L10149 脚注，Flyweight 语境）。
**著作/作品**：无独立外部著作；示例系统：MVC（L5010、L6826）；TCP 连接协议（L10201）；编译器（L7748 附近）；布尔表达式语言（L5543 附近）。
**概念**：behavioral pattern（L5000）；Chain of Responsibility（L5014）；implicit receiver（L5032）；Command（L5282）；macro command（L5306 附近）；Interpreter（L5541）；grammar class hierarchy（L5004）；Iterator（L5933）；external/internal iterator（L5937 附近、L10189）；robust iterator（L5973 附近）；Mediator（L6349）；Colleague（L6379 附近）；Memento（L6585）；Originator/Caretaker（L6603 附近）；Observer（L6824）；Subject/Observer（L6850 附近）；push/pull model（L6850 附近）；State（L7108）；Context（L7126 附近）；Strategy（L7342）；Template Method（L7596）；hook operation（L7614 附近）；Visitor（L7746）；Accept/Visit（L7772 附近）；double dispatch（L7786 附近、L10207）；encapsulating variation（L8089）；magic token（L8109）。
**机构**：C++、Smalltalk、CLOS（L10207 脚注）、Dylan（L10199 脚注）。
**地点**：无独立地点实体（会议地点出现在文献引注）。
**事件**：无历史事件。

---

## 九、与前后章关联

- **承接第 1—2 章**：MVC 从 1.2 的"三个模式的解剖"（L439—465）到 5.7 的完整 Observer 模板形成闭环；2.7 Command、2.8 Iterator/Visitor 在目录章获得完整展开；1.6 的"依赖具体操作"（L812—814）由 Chain of Responsibility/Command 回应。
- **与第 3—4 章交叉**：Interpreter 结合 Flyweight（L5565 附近）；Iterator 结合 Composite 与 Memento（L10191 脚注）；State 可用 Singleton 实现（L10203 脚注）——模式间组合证据贯穿目录章。
- **开启第 6 章**：Discussion 的"模式级组合协同"（L8158—8160）直接引出第 6 章"最好的设计将许多模式嵌合交织"（L8288）；"封装变化"主题在 6.3 被再次概括（L10209 脚注）。
