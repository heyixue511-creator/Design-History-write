# 第7章 Evaluation（评估）分析报告

## 一、章节定位与功能

本章是Part II的收束章，对应交互设计三阶段中的"评估"阶段。其功能是：为交互设计师提供从"Quick and Dirty"到"科学实验"的完整评估方法谱系，使设计师能够判断——"我设计的这东西到底好不好？"

本章开篇即宣言："Evaluation is about humility."（评估关乎谦卑）——这是对全书设计哲学的方法论表达。

## 二、结构分析

本章分为十二节，呈现从"非正式→正式→移动特殊性→综合"的递进结构：

1. **7.1 Introduction**：谦卑宣言 + 用户会做你没想到的事（配图：意外使用场景）。

2. **7.2 Classifying evaluation**：三维分类——谁来评（用户/专家/无人）、在哪评（实验室/田野/混合）、什么结果（轶事/定性/定量）。

3. **7.3 'Quick And Dirty'**：非正式、快速、宽泛反馈——"brain-damage check"。

4. **7.4 Conceptual model extraction**：用户如何理解全新的界面——HP数码相机图标案例（"摩天大楼模式"→"凌乱的叠放"）。

5. **7.5 Direct observation**：出声思维（Erikson & Simon）→听天由命的问题→建设性互动→编码表→自动日志→不干扰实验。

6. **7.6 Interviews**：访谈作为观察的补充——"人们非常不擅长解释和分解他们如何完成某个任务"。

7. **7.7 Questionnaires**：问卷——QUIS标准量表、Likert量表、语义差异量表、多选题、可靠性/有效性警告。

8. **7.8 Non-user methods**：启发式评估（Nielsen十项原则）、认知走查、GOMS/KLM（无用户评估）。

9. **7.9 Experimental evaluation**：假设→变量→实验设计（组间/组内/混合）→统计分析。

10. **7.10 Considering context**：移动评估的三重情境——物理的、技术的、社会的。

11. **7.11 Complementary evaluation**：互补评估——实验室+田野=完整图景。

12. **7.12 Conclusion**：移动系统评估仍是"开放问题"——"no one is completely sure what a 'correct' evaluation of a mobile system really is."

## 三、内容分析（核心论题+关键论点案例）

### 核心论题

**论题一：评估=谦卑的实践**
L### "Evaluation is about humility. No matter how good you think your design ideas are, there will always be something you didn't consider."

**论题二：没有一种评估方法足以单独评估移动系统**
L### "both types of testing are essential for mobile systems" ——实验室评估预测性能，情境评估揭示真实世界的问题。

**论题三：移动评估仍是开放问题**
L### 引用Abowd和Mynatt（2000）、Banavar和Bernstein（2002）——移动系统评估"需要更多关注"。

**论题四："五个用户就够了"被滥用**
L### Nielsen的五用户规则适用于启发式评估，不适用于科学实验——"5 people are sufficient to reveal the majority of problems in a given interface"但实验需要"many more than five users"。

**论题五：情境不仅指物理环境**
L### 三重情境框架——物理的（噪音、光线）、技术的（网络、设备）、社会的（有人在场、文化规范）——每种都需要不同的评估策略。

### 关键案例

L### **HP数码相机图标**（7.4）：一个图标被用户理解为"拍摩天大楼的模式"——实际上是"已拍摄照片数（叠放）"。最终解决方案："凌乱的叠放"（messy stack）——明确触发了"照片叠"的正确心智模型。

L### **Brewster的声音增强实验**（7.11）：实验室中声音增强提高了按钮选择准确性 → 户外行走中仍然有效但数据输入量减少32% → 证明：(a)实验室可以预测情境表现 (b)情境测试提供实验室无法替代的额外信息。

L### **"74次按键"用户**（Box 7.2）：在新菜单实验中，一位用户弃用快速访问系统，坚持用下箭头滚动——某次需74次按键。"他回答使用下箭头不需要思考该按哪个键——虽然按键更多，但保证能到达目标。"

L### **WiFi vs 蜂窝网络原型**（7.10.2）：一个系统在WiFi上崩溃了——因为WiFi带宽太高，设备来不及处理数据包——而在蜂窝网络（更低带宽）上反而正常运行。

L### **课堂SMS系统**（7.10.2）：学生最初愿意付费发SMS，但成本考虑导致使用迅速下降——技术方案可行但经济模式不可持续。

### 关键方法框架

L### **Nielsen十项启发式原则**（7.8.1）：系统状态可见性、系统与真实世界的匹配、用户控制与自由、一致性与标准、错误预防、识别而非回忆、灵活高效使用、审美与极简设计、错误诊断与恢复、帮助与文档。

L### **实验设计**（7.9）：假设→零假设→自变量/因变量→组间/组内设计→学习效应/疲劳效应→统计分析。

L### **三重情境框架**（7.10）：Physical context（噪音、光线、温度）、Technological context（网络带宽、外部设备）、Social context（他人在场、文化规范）。

## 四、逻辑梳理（论证链条+因果转折）

**主论证链**：
评估是必需的(humility) → 根据原型保真度和发展阶段选择方法 → 从Quick and Dirty到科学实验 → 移动系统需要实验室+情境"双轨"评估 → 移动评估方法论仍在演化中

**因果转折点**：
L### 转折一：从"出声思维=自然行为"到"出声思维=尴尬且容易忘记"——Erikson & Simon理论的实际困难导致"建设性互动"（两人协作）的提出。
L### 转折二：从"实验室评估替代情境评估"到"实验室评估+情境评估互补"——Brewster实验提供了实证基础。
L### 转折三：从"Nielsen的五用户规则"到"这规则只适用于启发式评估"——对被滥用的流行观念的纠正。
L### 转折四：从"人类可以被建模"到"GOMS/KLM只适用于有限情境"——认知建模的边界自觉。

**方法论困难**：
测量"unobtrusiveness"或"ambient awareness"这类属性极难量化——"how do you measure attributes like 'unobtrusiveness'?"

## 五、材料使用方式

1. **个人经验叙事**：
L### Box 7.2的"74次按键用户"——"At the end of the experiment, we interviewed the user and asked why they had adopted this strategy."
L### WiFi崩溃故事——"one system we tested using this technique failed because the bandwidth was too high!"

2. **教科书式框架**：以"谁/在哪/什么结果"三维对每项评估技术进行统一分类描述——形成一致的信息结构。

3. **实证研究引用**：
L### Brewster（2002）的声音增强研究——作为"实验室+情境互补"的核心证据。
L### Beck et al.（2003）——114篇移动HCI论文中仅50篇有评估内容。
L### Milgram（1974）——权威服从实验，作为用户偏见的极端警示。

4. **心理学经典参考**：
L### Hawthorne效应（Western Electric实验）
L### Halo效应（Thorndike, 1920）
L### Milgram实验（1974）

5. **标准量表引用**：QUIS（Maryland）、Gary Perlman的问卷库——为读者提供可直接使用的评估工具。

6. **技术工具**：Remote Display Control for PocketPC（Microsoft免费下载）、Noldus的Mobile Device Camera、Observer软件、EVA系统——具体的技术细节服务于实际操作。

## 六、论辩与阐述方法

1. **谦卑宣言**："Evaluation is about humility"——以一个抽象价值开启技术性章节，将评估从"技术步骤"提升为"伦理态度"。

2. **病理案例示范**：7.5节开篇描绘了一个灾难性的观察会话——用户乱按、原型崩溃、观察者走神、受试者失去信心——以"反面教材"的方式引出良好观察实践的每个要素。

3. **伦理嵌入**：伦理讨论不放在章节末尾的"免责声明"区，而是嵌入7.5.3和7.5.4的方法讨论核心——"How to not bias the experiment"和"Happy users"两节包含了完整的伦理实践指南。

4. **统计去神秘化**："If you're starting to get nervous about these statistical terms . . . please don't worry"——以安抚而非威吓的方式引入统计概念。

5. **开放问题诚实化**：以Abowd & Mynatt + Banavar & Bernstein的双重引用结尾——"no one is completely sure what a 'correct' evaluation of a mobile system really is"——与研究领域的不确定性共存的学术诚实。

## 七、语言文风（原文摘录+L###）

L### 文风特征：

L### 典型摘录1（谦卑宣言——伦理驱动）：
> "Evaluation is about humility. No matter how good you think your design ideas are, there will always be something you didn't consider – users are just so ingenious at doing what you didn't expect them to do."

L### 典型摘录2（病理叙事——焦虑制造）：
> "You start to think about how to change the interface and are startled by a sudden noise as the computer crashes. What happened? How did the user do that? You were so lost in thought you didn't notice what happened. Now you are angry with yourself and the user for crashing your prototype."

L### 典型摘录3（开车类比——身体感受）：
> "The next time you drive your car, speak aloud the driving decisions and maneuvers you're making as if to a driving instructor in the seat beside you. . . As you start to speak, you're very self-conscious. It's embarrassing to be telling the world these mundane thoughts."

L### 典型摘录4（学术诚实——方法论谦卑）：
> "So don't be put off that you may not be doing the 'correct' sort of evaluation; for the time being, no one is completely sure what a 'correct' evaluation of a mobile system really is."

**文风总结**：本章是全书中最"教学化"的一章——清晰的结构、大量实操细节、标准化方法描述。但"谦卑"的主题贯穿始终，使技术性讨论保持着人性温度。开车类比、Milgram实验、74次按键用户——这些故事性元素将"枯燥"的评估方法论变得生动。

## 八、实体清单（六类每类≥3+L###）

### 人物实体（≥3）
L### Jakob Nielsen——十项启发式原则、五用户规则、Alertbox专栏
L### Ben Shneiderman——CHARM网站、实验评估方法
L### Stephen Brewster——声音增强移动研究、实验室+情境互补证据
L### Stanley Milgram——权威服从实验（1974）
L### K. Anders Ericsson / Herbert Simon——出声思维方法（think-aloud protocol）
L### Jurek Kirakowski——问卷设计讨论（ucc.ie）
L### Gary Perlman——问卷资源网站（acm.org）
L### Abowd & Mynatt (2000)——移动评估"开放问题"声明
L### Banavar & Bernstein (2002)——普适计算应用评估方法需求
L### Wendy Mackay——EVA注释系统（1989）
L### Susan Dray——参与者同意书模板

### 技术/产品实体（≥3）
L### QUIS——Questionnaire for User Interaction Satisfaction
L### Remote Display Control for PocketPC——Microsoft无线屏幕镜像
L### Mobile Device Camera——Noldus定制摄像设备
L### Observer——Noldus数据分析软件
L### EVA——Mackay的早期视频注释实验系统（1989）
L### Theme——PatternVision的AI模式发现软件
L### GOMS (Goals, Operators, Methods, Selectors)——认知建模
L### KLM (Keystroke Level Model)——简化的按键级模型
L### scan converter——屏幕-视频信号转换器

### 机构/组织实体（≥3）
L### University of Maryland HCI Lab——QUIS
L### Noldus——Observer、Mobile Device Camera
L### Dray & Associates——参与者同意书模板、Tablet PC评估
L### HP——数码相机图标案例
L### PatternVision——Theme软件
L### University of Cape Town——作者所在机构，多个实验

### 概念/术语实体（≥3）
L### think-aloud protocol——出声思维协议
L### constructive interaction——建设性互动（双人协作出声思维）
L### Hawthorne Effect——被观察改变行为的效应
L### Halo Effect——光环效应（Thorndike, 1920）
L### heuristic evaluation——启发式评估
L### cognitive walkthrough——认知走查
L### contextual walkthrough——情境走查（Po, 2003）
L### coding sheet——编码表
L### null hypothesis——零假设
L### dependent variable / independent variable——因变量/自变量
L### between-groups / within-groups design——组间/组内实验设计
L### learning effect / ordering effect——学习效应/顺序效应
L### Likert scale——李克特量表
L### semantic differential scale——语义差异量表
L### reliability and validity——信度与效度
L### conceptual model extraction——概念模型提取
L### context awareness——情境意识
L### longitudinal study——纵向研究
L### complementary evaluation——互补评估

### 文献/理论实体（≥3）
L### Nielsen, 1994——十项启发式原则
L### Nielsen and Mack, 1994——评估方法经典文集
L### Erikson and Simon, 1985——出声思维协议
L### Brewster, 2002——声音增强移动评估
L### Beck et al., 2003——114篇移动HCI论文评估元分析
L### Milgram, 1974——权威服从实验
L### Card et al., 1983——GOMS模型
L### Preece et al., 2002——交互设计教科书（评估方法）
L### Shneiderman, 1998——实验评估方法
L### Dey, 2001——情境定义
L### Jameson, 2001——用户与情境的互补建模
L### Po, 2003——情境走查
L### Vetere et al., 2003——移动CSCW启发式
L### Smith and Mosier, 1986——944项评估的基础
L### Nunez, 2002——连接主义认知模型与虚拟环境
L### Thorndike, 1920——Halo Effect
L### Howell, 2001——统计方法入门

### 关键数据实体（≥3）
L### 114篇移动HCI论文：仅50篇（44%）有评估内容（1996-2002, Beck et al.）
L### Brewster实验：户外行走中数据输入减少32%
L### 944项评估：最早的系统桌面评估（Smith & Mosier, 1986）
L### Nielsen十项启发式原则
L### 五用户规则：Nielsen称五人足以发现大部分问题
L### 10人/条件：组间实验设计的经验法则（Dix et al.）
L### 74次按键：不使用快捷方式的用户单次选择所需最大按键数
L### Milgram：参与者"电击"他人的权威服从实验

## 九、与前后章关联

**与第4章的关联**：
L### 第4.5节"评估"是第7章的概览——第4章提到的用户测试、专家评估、KSPC、启发式评估在第7章全部展开。
L### 第4章的"谦卑"态度在这里被明确命名为"evaluation is about humility"。

**与第5章的关联**：
L### 第5章的"自然观察"方法在第7章被重新定位为"Quick and Dirty"评估。
L### 第5章的纵向民族志挑战在第7章获得评估方法层面的解决方案（语音日记、Remote Display Control）。
L### 第5章的人种志方法与第7章的科学实验形成方法论的两极。

**与第6章的关联**：
L### 第6章的原型在不同保真度阶段对应第7章不同评估方法——低保真→Quick and Dirty，功能原型→启发式评估/实验。
L### 第6章的"纵向原型健壮性"要求直接导向第7章的纵向评估讨论。

**与Part III（第8-11章）的关联**：
L### 第7章的实验设计方法在第8章B+Tree菜单研究中得到完整应用——假设→零假设→自变量/因变量→被试→任务→模拟→步骤。
L### 第7章的"情境评估"理念在第10章SDAZ浏览器和第11章发展中国家部署中得到实践。
L### 第7章Box 7.2的"74次按键用户"直接来自第8章的菜单研究。

**逻辑定位总结**：第7章是Part II的最后一章，完成"理解→创制→评价"三元循环。它同时是全书中最"不完整"的一章——作者反复强调移动评估方法论仍在演化中，这种"开放问题"的诚实姿态既反映了该领域的真实状态，也为读者的创造性贡献留出了空间。
