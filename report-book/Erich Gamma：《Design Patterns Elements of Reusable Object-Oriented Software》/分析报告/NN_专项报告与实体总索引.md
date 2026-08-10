# 专项报告与实体总索引

## 第一部分：专项报告

---

### 一、语言特征

本书以**现代英语技术写作**为主体，呈现以下特征：

1. **教学性第一人称复数**：全书以"we"统一作者与读者视角，设计过程被表述为共同推进的探索（如"Let's consider…"L1213、"We'll define…"L1034）。这是"设计演练"文体的标志。
2. **祈使与条件句结合**：适用性与实现节大量使用祈使（"Use the Adapter pattern when…"L3134）与条件（"if you want to…"）句式，把知识编码为可操作规则。
3. **术语名物化**：模式名、参与者名以专有名词形式出现（Composite、Decorator、Originator…），正文、目录、索引、脚注之间以页码交叉引用形成严密的指称网络（如"Composite (163)"L686）。
4. **句子结构**：长句为主但信息密度高；定义性句子常以"X is a Y that…"模板出现（如"Delegation is a way of making composition as powerful for reuse as inheritance"L738）。

### 二、文风特征

1. **先破后立**：每章/每节先展示问题或错误方案，再给出模式方案（第 2 章最典型：L1066 继承爆炸→L1072 透明封装）。
2. **类比启发**：用非软件领域经验建立直观——文学情节模式（L403）、生态系统 vs 分类学（L780）、音乐记谱（第 1 章思想源）、建筑模式语言（L8242—8266）。
3. **权衡话语**：反复使用"trade-off"（L1026、L1438）、"on the other hand"（L866、L918），避免绝对化断言。
4. **清单式呈现**：编号列表承载核心结构（七个设计问题 L934—948、八种重设计成因 L808—842、四重价值 L8178—8224）。

### 三、修辞方式

1. **对比对照**：全书最核心修辞——类继承 vs 接口继承（L670）、白盒 vs 黑盒（L714—716）、继承 vs 组合 vs 泛型（L760—774）、Observer vs Mediator（L8111—8121）、Adapter vs Bridge（L4972—4978）、Composite vs Decorator vs Proxy（L4982—4996）。
2. **设问自答**：以问题引出论述（"What is it?"L399、"How can existing and unrelated classes like TextView work…?"L3118、"Can We Use an Abstract Factory?"L1191）。
3. **反例论证**：先证伪替代方案（type test 代码"pretty ugly"L1583、函数参数化三缺陷 L1369—1375、交集/并集接口 L1215—1217）。
4. **权威引证**：以文献支撑论点（Sny86"继承破坏封装"L720、Knu84 TeX L1048、Foote 三阶段 L8212、Alexander 引语 L8290）。

### 四、史料使用方式

1. **第一手内部史料**：成书史（L8228—8236）基于作者亲历（博士论文、OOPSLA/ECOOP 会议、命名演化）。
2. **真实系统样本**：MVC（L439—465）、Doc 编辑器（L10145 脚注）、ET++（L8719 文献）、NEXTSTEP NXProxy（L10181 脚注）、TCP 协议（L10201 脚注）——以既有系统作为模式存在的证据。
3. **文献网络**：正文引证缩略（Sny86、Knu84 等），完整信息集中于 Bibliography（L8665—8859，约百条），形成"正文—文献"双层证据结构。
4. **社区史实**：OOPSLA '91 工作坊、PLoP 1994（L8270）——把本书嵌入正在形成的学术运动叙事。

### 五、阐述方法

1. **问题-约束-方案-模式**四段式（第 2 章标准流程，L932—950 确立）。
2. **统一示例对照法**：迷宫（创建型 L1706—1819）、绘图编辑器（结构型）、编译器（Facade/Visitor）——同一领域内多模式对比。
3. **模板化描述**：13 节固定模板（L473—523）保证 23 个模式可比较、可检索。
4. **从结构到意图**：Discussion 教导读者"结构相似≠意图相同"（L4970），以意图而非图式选模式。

### 六、推演逻辑

1. **归纳-命名**：从系统实践中归纳重复结构→命名→模板化（L401、L8232—8238）。
2. **原则-实例双向印证**：两条原则（L704、L730）由案例归纳得出，又被全书 23 个模式反复印证。
3. **变化维度分析**：以"什么应可变"（Table 1.2，L894—896）为轴，把每个模式定位到具体变化维度。
4. **权衡-比较决策**：模式选择被理性化为"在哪些维度牺牲什么"的权衡问题（L3062—3076、L8123—8150）。

### 七、术语中英对照表

| 英文术语 | 中文译名 | 证据行号 |
|---|---|---|
| design pattern | 设计模式 | L401 |
| abstract class | 抽象类 | L658 |
| abstract operation | 抽象操作 | L658 |
| interface inheritance / subtyping | 接口继承 / 子类型化 | L680 |
| class inheritance | 类继承 | L680 |
| white-box reuse | 白盒复用 | L714 |
| black-box reuse | 黑盒复用 | L716 |
| object composition | 对象组合 | L716 |
| delegation | 委托 | L736 |
| parameterized types / generics / templates | 参数化类型 / 泛型 / 模板 | L760—762 |
| aggregation | 聚合 | L782 |
| acquaintance | 相识（关联） | L784 |
| abstract coupling | 抽象耦合 | L830 |
| framework | 框架 | L858 |
| toolkit | 工具箱 | L854 |
| refactoring | 重构 | L8210 |
| intent | 意图 | L477 |
| applicability | 适用性 | L489 |
| participants | 参与者 | L497 |
| collaborations | 协作 | L501 |
| consequences | 后果 | L505 |
| encapsulation | 封装 | L720 |
| polymorphism | 多态 | L692 |
| recursive composition | 递归组合 | L972 |
| transparent enclosure | 透明封装 | L1072 |
| double dispatch | 双重分派 | L1585、L10207 |
| creational / structural / behavioral | 创建型 / 结构型 / 行为型 | L581—591 |
| white-box / black-box | 白盒 / 黑盒 | L714—716 |
| encapsulation of variation | 封装变化 | L8089 |

---

## 第二部分：实体总索引

### 一、人物

| 实体 | 身份 | 证据行号 |
|---|---|---|
| Erich Gamma | 作者，目录发起人 | L8228 |
| Richard Helm | 作者 | L8228 |
| Ralph Johnson | 作者 | L8228 |
| John Vlissides | 作者 | L8228 |
| Grady Booch | 序言作者 | L349 |
| Christopher Alexander | 建筑师，模式语言创始人 | L8242、L8290 |
| Bruce Anderson | OOPSLA '91 工作坊主持 | L8270 |
| Donald Knuth | 《计算机程序设计艺术》作者 | L8272 |
| James Coplien | 《Advanced C++》作者 | L8274 |
| Kent Beck | Smalltalk 模式专栏作者 | L8276 |
| Peter Coad | 分析模式收集者 | L8276 |
| Brian Foote | 软件生命周期三阶段提出者 | L8212 |
| Calder | Doc 编辑器作者，glyph 术语首创 | L10145、L10149 |
| Lynch / Rose | TCP 连接协议描述者 | L10201 |
| Stan Lippman | 评语作者（C++ Report） | L233 |
| Tom DeMarco | 评语作者（IEEE Software） | L237 |
| Sanjiv Gossain | 评语作者（JOOP） | L241 |
| Larry O'Brien | 评语作者（Software Development） | L245 |
| Steve Bilow | 评语作者（JOOP） | L249 |

### 二、著作/作品

| 实体 | 类型 | 证据行号 |
|---|---|---|
| A Pattern Language（Alexander 等 1977） | 建筑模式著作 | L8671、L8242 |
| The Art of Computer Programming（Knuth） | 算法目录 | L8272 |
| Graphics Gems 系列 | 图形算法目录 | L8272 |
| Advanced C++: Programming Styles and Idioms（Coplien） | C++ 惯用法著作 | L8274 |
| The Annotated C++ Reference Manual（Ellis & Stroustrup） | C++ 语言参考 | L8721 |
| Object-Oriented Analysis and Design with Applications（Booch） | OOAD 方法著作 | L8683 |
| Smalltalk Report 专栏（Beck） | 模式专栏 | L8276 |
| Doc（Calder） | 文本编辑器应用 | L10145 |
| NEXTSTEP General Reference（Addison-Wesley） | 平台参考 | L8667 |
| ET++SwapsManager 论文（Eggenschwiler & Gamma） | 金融框架报告 | L8719 |

### 三、概念（23 个模式 + 核心机制）

| 实体 | 证据行号 |
|---|---|
| Abstract Factory | L1821 |
| Builder | L2076 |
| Factory Method | L2334 |
| Prototype | L2609 |
| Singleton | L2853 |
| Adapter（Wrapper） | L3100、L3108 |
| Bridge | L3369 |
| Composite | L3659 |
| Decorator | L3952 |
| Facade | L4179 |
| Flyweight | L4394 |
| Proxy | L4655 |
| Chain of Responsibility | L5014 |
| Command | L5282 |
| Interpreter | L5541 |
| Iterator | L5933 |
| Mediator | L6349 |
| Memento | L6585 |
| Observer | L6824 |
| State | L7108 |
| Strategy | L7342 |
| Template Method | L7596 |
| Visitor | L7746 |
| design pattern | L401 |
| interface / implementation inheritance | L670—684 |
| white-box / black-box reuse | L714—716 |
| delegation | L736 |
| aggregation / acquaintance | L782—792 |
| abstract coupling | L830 |
| framework / toolkit / application | L846—884 |
| refactoring | L8210 |
| double dispatch | L1585、L10207 |
| glyph | L987、L10149 |
| transparent enclosure | L1072 |
| recursive composition | L972 |
| encapsulate the concept that varies | L892、L8089 |
| program to an interface | L704 |
| favor object composition | L730 |
| pattern language | L8244 |
| MVC（Model-View-Controller） | L439 |

### 四、机构

| 实体 | 证据行号 |
|---|---|
| Addison-Wesley | L53、L8667 |
| OOPSLA（会议） | L8228、L8270 |
| ECOOP（会议） | L8228 |
| PLoP / Pattern Languages of Programs | L8270 |
| ACM（出版/会议方） | L8689、L8725 |
| IEEE | L8677 |
| USENIX | L8717 |
| X Window System | L1257 |
| Presentation Manager | L1128、L1269 |
| Motif | L1128 |
| Macintosh | L1189 |
| Windows（窗口系统） | L1189 |
| NEXTSTEP | L10181 |
| Smalltalk（语言/社区） | L678 |
| C++（语言） | L678 |

### 五、地点

| 实体 | 证据行号 |
|---|---|
| Reading, MA（Addison-Wesley 所在地） | L8667 |
| Kaiserslautern（ECOOP '93 所在地） | L8679 |
| Bologna（ECOOP '94 所在地） | L8681 |
| Ottawa（OOPSLA '90 所在地） | L8689 |
| Vancouver（OOPSLA '92 所在地） | L8701 |
| Paris（TOOLS '90 所在地） | L8669 |
| Portland（USENIX C++ '92 所在地） | L8717 |
| Snowbird（UIST '90 所在地） | L8699 |
| Boston（Graphics Gems II 出版地） | L8675 |
| New York（A Pattern Language 出版地） | L8671 |

### 六、事件

| 实体 | 证据行号 |
|---|---|
| OOPSLA '91（目录成为独立项目） | L8228 |
| OOPSLA '92（Ralph Johnson 加入） | L8228 |
| ECOOP '93（摘要获接纳） | L8228 |
| 1994 年 8 月第一届 PLoP 会议 | L8270 |
| OOPSLA '91 软件架构手册工作坊（Bruce Anderson 主持） | L8270 |
| 目录命名演化（Wrapper→Decorator 等） | L8230 |
| Smalltalk MVC 的形成 | L439—465 |
| 软件生命周期三阶段（原型/扩张/巩固） | L8212—8218 |
