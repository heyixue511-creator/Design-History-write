# 第6章 Prototypes（原型）分析报告

## 一、章节定位与功能

本章是Part II中的"原型方法论章"，对应交互设计三阶段中的"开发原型设计"阶段。其核心功能是：将从第5章用户研究中获得的理解和洞察转化为可被评估、讨论和迭代的具体形式。

Scott Jenson的名言"fail fast"（快速失败）是本章的哲学座右铭——原型是让设计"足够多次失败以最终成功"的工具。

## 二、结构分析

本章分为八节，呈现从"低"到"高"再到"收束"的递进结构：

1. **6.1 Introduction**：确立"fail fast"的原型哲学——"No matter how good the designer, it is unlikely that their first design will fulfill all the varied user, engineering and esthetic requirements."

2. **6.2 What is a prototype?**：解构"原型"概念——对程序员是预发布软件，对艺术家是铅笔草图。核心定义：让设计想法尽快被表达的任何东西。

3. **6.3 Different prototypes for different purposes**：低保真vs高保真谱系——取决于用户感知而非实现细节。

4. **6.4 Low-fidelity**：自检原型（Jeff Hawkin的木块PalmPilot）、团队交流（白板+Post-it）、交互原型（故事板→PowerPoint→Wizard of Oz）、用户赋权（PICTIVE、实地角色扮演）。

5. **6.5 Higher-fidelity**：水平vs垂直原型、PC端vs通用移动平台vs专用平台、Handspring Treo的Buck、Nam和Lee的投影原型。

6. **6.6 Finishing the process**：演进式vs革命式原型——代码可以保留还是必须丢弃？

7. **6.7 Issues in prototyping**：移动原型的特殊挑战——硬件软件整合、纵向研究的健壮性要求。

8. **6.8 A final note on development**：设计是收敛的过程。

## 三、内容分析（核心论题+关键论点案例）

### 核心论题

**论题一：原型=快速失败，以加速成功**
L### "Prototyping is a way to 'fail fast', his rationale being that if we fail enough times, then eventually we will get it right." 这是本章最核心的认识论立场。

**论题二：低保真原型对移动设计尤其重要**
L### Jeff Hawkin的"木块便携"、纸板VR游戏、聚苯乙烯"计算机"和纸板"传感器"——这些案例共同论证：低保真不只是"简陋替代品"，而是让非技术利益相关者参与设计的民主化工具。

**论题三：移动原型的硬件-软件整合挑战远大于桌面系统**
L### 桌面原型可以假设标准I/O，但移动设备专有硬件（滚轮、触控笔、倾角传感器）与软件高度耦合——硬件迭代周期远长于软件。

**论题四：原型不仅是"展示给他人"——首先是"展示给自己"**
L### 作者以自身的菜单设计经历作为"反面教材"：三个月的编程浪费，因为跳过了纸面草图的自我检查阶段——"it seemed like a good idea at the time."

**论题五：纵向研究对移动原型提出健壮性要求**
L### 一项研究持续超过一年（Petersen et al., 2002）——原型的可靠性必须足以支撑长时段日常使用。

### 关键案例

L### **Jeff Hawkin的木块**（6.4.1）：PalmPilot的设计者将一块木头放在衬衫口袋中作为设备代用品——"Sounds crazy, but it worked for him."

L### **纸板VR游戏**（6.4.4）：使用笔、纸、塑料人偶来预演VR游戏设计——"Playing in cardboard allows us to decide whether the idea has any merit before taking it to the rest of the team."

L### **B+Tree菜单原型**（6.5.1）：Java applet+互动照片——不可见按钮覆盖在扫描的实体按钮照片上。说明：纸面原型在这里无效，因为Wizard of Oz无法跟上交互速度。

L### **Treo的Buck**（6.5.2）：Handspring团队将Treo键盘连接到笔记本电脑——通用测试平台，捕获了否则不可能发现的小键盘交互问题。

L### **Peephole的"Heath-Robinson"方案**（6.5.2）：用电缆将PDA连接到桌面鼠标来模拟空间位置跟踪——"The design appears somewhat 'Heath-Robinson', but allowed the researcher to gage the effectiveness of the interplay between the software and hardware."

L### **滑雪教练定位设备**（6.5.2）：寒冷天气导致电池寿命不足——这是实验室中永远不会发现的field finding。

L### **Tablet PC的"Version 1.0 = 原型"策略**（6.5.2）：Dray & Associates将完整成品先只发给47名评估者——第一个公开发售的实际上是第二个版本。

## 四、逻辑梳理（论证链条+因果转折）

**主论证链**：
设计想法需要被表达(why prototype) → 从最低保真开始(self-check) → 与团队沟通(shared surface) → 交互测试(scenario/storyboard) → 用户参与(PD) → 决定测试什么(horizontal vs vertical) → 选择合适的平台(PC→general mobile→specialist) → 纵向部署(longitudinal use) → 收敛到最终设计

**因果转折点**：
L### 转折一：从"原型=粗糙版软件"到"原型=使设计可被审查的任何东西"——概念的彻底扩展。
L### 转折二：从"原型给别人看"到"原型先给自己看"——自我检查(self-checking)的独立一节，强调设计者的内部对话。
L### 转折三：从"低保真=低价值"到"纸板是VR的必需品"——通过极端案例颠覆价值判断。
L### 转折四：从"在PC上开发然后移植"到"可能需要从移动端开始写代码"——作者自己项目的教训：Java→J2SE→Linux→失败→.NET重写。

**学习效应警示**：
学习效应不仅影响实验设计(第7章)，也影响原型开发——过早的代码投入可能导致对半成熟设计的"过早承诺"。

## 五、材料使用方式

1. **个人叙事**：作者在多处使用第一人称讲述自己的失败经历——"I am guilty of this myself, and wasted about three months of programming time..."——建立教学中的"共犯"关系。

2. **工业界案例**：
L### Treo的Buck：Handspring/Palm团队的定制测试硬件
L### Apple Newton→PalmPilot：Jeff Hawkin的个人原型策略
L### Dray & Associates的Tablet PC"Version 1.0"策略

3. **可视化辅助**：大量原型实物照片（纸面草图、Post-it白板、故事板、纸板VR游戏、PocketPC模拟器截图、Buck装置、投影原型），使抽象的原型概念具体化。

4. **概念对比表**：低保真vs高保真、水平vs垂直、演进式vs革命式——读者可以快速对照决策。

5. **学术引用**：
L### Fallman的"sketching"理论（第4章已介绍）
L### Landay和Myers的SILK系统
L### Nielsen的"scenario-based prototyping"

6. **婚前课程类比**：作者用自己婚前辅导课上的"描述-绘画"练习来说明口头描述视觉设计的困难——个人生活经验被用作设计教学工具。

## 六、论辩与阐述方法

1. **共情式失败叙事**：作者的"三个月浪费"不仅仅是在说"原型很重要"，而是在说"我也犯过这个错误"——降低说教感。

2. **极端案例论证**："连VR都可以用纸板做原型"——如果最技术密集的领域都可以用低保真，那任何领域都可以。

3. **婚礼类比**：私下场合的个人经验被公开并转化为教学工具——增加文本的亲近感和人性化。

4. **平台作为分析维度**：PC→通用移动平台→专用平台→Version 1.0——四个递进的保真级别，各有其适用场景和陷阱。

5. **"pitfalls"显式列出**：PC端开发的五项陷阱（键盘、鼠标、便携性、怪硬件、性能）以编号列表呈现——这是工业实践经验的直接转移。

## 七、语言文风（原文摘录+L###）

L### 文风特征：本章是全书中最"自传体"色彩的一章，第一人称叙事密度最高。

L### 典型摘录1（个人失败叙事——幽默的自嘲）：
> "I am guilty of this myself, and wasted about three months of programming time when developing the ideas for the new menu structure discussed in Chapter 8. In my rush to create a functioning handset, I glossed over design considerations and made some arbitrary decisions. . . Again, it seemed like a good idea at the time."

L### 典型摘录2（婚前课程类比——私人经验的公开化）：
> "Just before we were married, my wife and I went on a course to help us prepare for married life. One exercise we undertook required one of us to describe an image and the other to sketch it based on the verbal instructions. It was one of the hardest things we've ever had to do – speech is the wrong medium to convey visual information."

L### 典型摘录3（纸板VR——挑衅性的宣言）：
> "When we started using cardboard and paper, the rest of the team were very skeptical about the value of such an approach – virtual reality is a technology-heavy research area. Once they saw how quickly we could refine ideas and empower non-technologists to contribute to the discussion, they realized that cardboard is an essential component in virtual reality."

L### 典型摘录4（API教训——技术细节中的幽默）：
> "Eventually, after a month of tinkering and the purchase of a 1 Gb memory card, the application ran (very slowly)."

**文风总结**：高度个人化，失败叙事真诚，技术细节中嵌入自嘲幽默。与第4章的理论化、第5章的叙事化不同，第6章是"工匠经验谈"——一个做了很多错误选择的设计者告诉你什么不该做。

## 八、实体清单（六类每类≥3+L###）

### 人物实体（≥3）
L### Jeff Hawkin——PalmPilot发明者，木块原型传奇
L### Scott Jenson——"fail fast"名言来源
L### Daniel Fallman——"sketching as archetypal design activity"
L### Jakob Nielsen——scenario-based prototyping，水平/垂直原型区分
L### Alan Cooper——《The Inmates are Running the Asylum》，关于过早承诺代码的警示
L### Susan Dray——Tablet PC原型策略（Dray & Associates）
L### James Landay——SILK系统（与Myers合作）
L### Jason Pascoe——非洲野生动物追踪系统

### 技术/产品实体（≥3）
L### PalmPilot——Jeff Hawkin的木块原型故事
L### Apple Newton——PDA市场的著名失败
L### Handspring Treo + "Buck"——硬件软件整合的原型策略
L### Peephole系统的"鼠标电缆"方案——Heath-Robinson式原型
L### PocketPC模拟器——Visual Studio开发环境
L### Griffin PowerMate——替代滚轮的USB设备
L### HP iPAQ 5550——通用移动原型平台（400MHz XScale, 128Mb RAM）
L### B+Tree菜单原型——Java applet+交互照片
L### 纸板VR游戏——笔、纸、塑料人偶
L### PICTIVE——参与式设计工具包

### 机构/组织实体（≥3）
L### Handspring——Treo开发者
L### Palm——PalmPilot和操作系统
L### Microsoft——PocketPC/Windows Mobile/.NET Compact Framework
L### Sun——Java/J2ME
L### Symbian——移动操作系统
L### Noldus——Observer软件、移动设备摄像设备

### 概念/术语实体（≥3）
L### low-fidelity vs high-fidelity prototypes——低保真vs高保真原型
L### horizontal vs vertical prototypes——水平vs垂直原型
L### evolutionary vs revolutionary prototyping——演进式vs革命式原型
L### "fail fast"——快速失败哲学
L### self-checking——自我检查原型
L### Wizard of Oz——人模拟计算机的原型技术
L### PICTIVE——Plastic Interface for Collaborative Technology Initiatives through Video Exploration
L### storyboarding——故事板（从电影行业借用的概念）
L### participatory design——参与式设计
L### live-action role playing——实地角色扮演
L### software emulator——软件模拟器
L### scan converter——混合视频信号的转换器
L### J2SE vs J2ME vs .NET Compact Framework——移动开发平台的对比

### 文献/理论实体（≥3）
L### Bergman and Haitani, 2000——PalmPilot设计故事（木块原型）
L### Fallman, 2003——设计作为"sketching"
L### Nielsen, 1993——scenario-based prototyping, 水平/垂直原型
L### Landay and Myers, 1995——SILK系统
L### Gould et al., 1983——Wizard of Oz（"listening typewriter"）
L### Nam and Lee, 2003——投影原型系统
L### Pering, 2002——Treo的Buck
L### Yee, 2003——Peephole空间跟踪
L### Dray and Siegel, 2002——Tablet PC原型策略
L### Petersen et al., 2002——一年纵向研究
L### Liu and Khooshabeh, 2003——Wizard of Oz疲劳效应

### 关键数据实体（≥3）
L### Jeff Hawkin：衬衫口袋中的木块—>PalmPilot
L### KPSC对比：multi-tap (2.03), T9 (1.01), QWERTY (1), 预测+触笔 (0.50)
L### 一年：Petersen等人的纵向研究时长
L### 47名评估者：Dray的Tablet PC原型策略
L### 三个月浪费：作者在菜单项目上的编程投入
L### 1Gb内存卡：作者在失败的Java移植中购买的额外硬件
L### 10000+词/天：Wizard of Oz无法跟上的交互速度

## 九、与前后章关联

**与第4章的关联**：
L### 第4.4节"原型设计"是第6章的"目录"——第4章提到的低保真/高保真、水平/垂直、纸面原型/Wizard of Oz、PICTIVE等概念在本章都得到系统展开。
L### 第4章的Fallman"设计即sketching"理论在本章被嵌入到具体原型策略中。

**与第5章的关联**：
L### 第5章的用户研究产出（Personas, Scenarios, 任务分析）是第6章原型设计的输入——Scenarios用于驱动交互原型的storyboarding。
L### 第5章的"实地角色扮演"方法在本章被归入"低保真原型"的类别。

**与第7章的关联**：
L### 第6章讨论的原型在第7章成为评估的对象——原型的保真度决定适用的评估方法（纸面→Quick and Dirty，功能原型→实验评估，纵向部署→Diary Study）。
L### 第6.5节的"纵向原型"要求直接导向第7章的纵向评估讨论。

**与第8章的关联**：
L### 第6.5.1节直接引用第8章的B+Tree菜单作为"需要非纸面原型"的案例。
L### 第6.5.2节的"interactive photograph"（Java applet原型）就是第8章菜单评估的实际工具。

**与第10章的关联**：
L### 第6章讨论的"无法用纸面原型"的移动交互（高速交互、视觉浏览）在第10章的SDAZ浏览器案例中得到验证——需要功能性原型。

**逻辑定位总结**：第6章是连接"用户理解"与"设计评估"的桥梁——原型是将洞察转化为可测试形式的关键转化环节。它在全书中是"创制"阶段的理论阐述，作者的"工匠叙事"风格使这一章成为全书中最具实践操作性的章节之一。
