# Ch26 分析报告：Emerging Frameworks for Tangible User Interfaces

**作者**：Brygg Ullmer, Hiroshi Ishii（MIT Media Lab / Tangible Media Group）
**所属 Part**：Part VI — Integrating Computation and Real Environments
**在书中位置**：第579–601页

---

## 一、章节定位与功能
### L001
Ch26是**Tangible User Interfaces（有形用户界面）** 领域的奠基性综述。以Urp（城市规划工作台）和mediaBlocks（数字媒体的物理化容器）两个原型为双重核心案例，提出了TUI的交互模型、关键特征、术语学和分类框架。

## 二、结构分析
- 26.1 Introduction + 26.2 Urp（城市规划中的风/影/反射模拟——物理建筑模型+数字投影叠加）
- 26.3 Tangible User Interfaces（定义：通过物理对象来表征和操控数字信息）
- 26.4 Interaction Model（MCRpd模型：Model-Control-Representation——物理+数字的双重表征）
- 26.5 Key Characteristics + 26.6 mediaBlocks（物理块的数字媒体存储/传输概念）
- 26.7 Terminology + 26.8 Coupling Objects with Digital Information（数字绑定的种类/耦合方法/物理表征方法/技术实现）
- 26.9 Interpreting Systems of Objects（空间系统/关系系统/建构系统/混合建构-关系系统）
- 26.10 Application Domains + 26.11 Related Areas + 26.12 Conclusion

## 三、内容分析
### L002 核心论题
图形用户界面（GUI）将交互限制在屏幕的二维像素世界中——**Tangible UI通过将数字信息耦合到可触摸、可操作的物理对象上**——将计算的抽象性变得"可抓取"和可空间操作。交互不发生在"界面"上，而发生在**物理世界的有形表征中**。

### L003 关键论点
1. **MCRpd交互模型**：TUI的交互不同于GUI的MVC（Model-View-Control）——物理表征（physical representation）与数字表征（digital representation）**共存且耦合**——用户通过操作物理对象来同时改变物理和数字世界。
2. **三种耦合系统**：空间系统（物理对象的位置/朝向 = 数字意义）→ 关系系统（物理对象之间的关系 = 数字意义）→ 建构系统（物理对象的组装 = 数字意义）。
3. **mediaBlocks**：数字媒体被封装在可触摸的"块"中——媒体在不同设备间的传输成为物理操作（类似"积木"的插入和拔出的隐喻）。

### L004 原文摘录
> "Tangible interfaces give physical form to digital information, employing physical artifacts both as representations and controls for computational media."
> "The last decade has seen a wave of new research into ways to link the physical and digital worlds."

### L005 关键实体
- **人物**：Brygg Ullmer, Hiroshi Ishii（Tangible Media Group / MIT Media Lab）
- **系统**：Urp（Urban Planning Workbench——城市规划/建筑模拟）, mediaBlocks（数字媒体物理化容器）, metaDESK, Tangible Geospace
- **概念**：Tangible User Interfaces (TUI), MCRpd Model (Model-Control-Representation physical-digital), Spatial/Relational/Constructive Systems, Physical-Digital Coupling, Phicons (Physical Icons)

## 九、关联
- **Ch25 (Streitz/Roomware)**：TUI + Roomware 共享"物理对象作为界面"的核心理念——Roomware关注空间级别的嵌入，TUI关注对象级别的交互
- **Ch23 (Abowd/普适计算)**：TUI是普适计算中"自然界面"的具体交互范型
- **Ch04 (分布式认知)**：TUI的物理-数字耦合是"认知分布"的物质化——认知任务的部分被"卸载"到物理世界中
