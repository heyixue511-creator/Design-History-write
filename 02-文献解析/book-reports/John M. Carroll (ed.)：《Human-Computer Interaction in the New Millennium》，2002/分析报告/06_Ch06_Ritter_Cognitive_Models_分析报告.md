# Ch06 分析报告：User Interface Evaluation: How Cognitive Models Can Help

**作者**：Frank E. Ritter, Gordon D. Baxter, Gary Jones, Richard M. Young
**所属 Part**：Part II — Usability Engineering Methods and Concepts
**在书中位置**：第125–147页

---

## 一、章节定位与功能

### L001
Ch06 提出将认知模型（cognitive models）作为"替代用户"（surrogate users）直接与界面交互的技术架构。核心创新是**CMIMS（Cognitive Model Interface Management System）**——将用户界面管理系统（UIMS）扩展为支持认知模型"看"（Sim-eye）和"操作"（Sim-hand）界面的平台。

---

## 二、结构分析

| 节 | 核心 |
|---|---|
| 6.1 Synergy between Cognitive Modeling and HCI | 认知模型对HCI的三种贡献（设计比较/智能助手/替代用户）；互动任务对模型的三大好处 |
| 6.2 Route to Supporting Models as Users | CMIMS架构：Sim-eye+Sim-hand+通信机制；功能模型（fovea+parafovea+periphery） |
| 6.3 Example Cognitive Models | 三个案例：ATC模型（Garnet+Soar）、Tower of Nottingham（Garnet+ACT-R）、电子战任务（SLGMS+Soar）+ 相关系统综述（APEX/Driver-Soar/EPIC/ACT-R/PM） |
| 6.4 Cognitive Models as Users in the New Millennium | 对模型的启示（交互知识、视觉搜索成本）；对界面的启示（what-if评估、嵌入式助手） |

---

## 三、内容分析

### L002 核心论题
认知模型可以通过统一的"模拟眼和手"（Sim-eye & Sim-hand）接口获得与人类用户相同的界面访问权限，从而用作自动化可用性评估工具。

### L003 关键论点
1. "Models as users has been envisioned before but has not yet been widely applied." ——为认知模型提供"真实"界面访问是尚未兑现的承诺。
2. "Including a theory of interaction has both provided models with more capabilities and also constrained the speed and abilities." ——加上感知-动作的约束实际上使模型更"像人"而非更弱。
3. "The importance of perception in task performance was confirmed." ——三个案例中模型花费约一半时间在交互（视觉搜索+动作执行）上——暗示HCI常年低估了感知-动作成本。

### L004 关键案例
1. **简化ATC模型**（6.3.1）：Soar模型通过Garnet UIMS中的Sim-eye导航空管显示——模型必须主动搜索信息（飞机的航向/速度/位置），而非"全知"地"在知道一切"。发现：周边视觉（periphery）对简单搜索至关重要。
2. **Tower of Nottingham**（6.3.2）：ACT-R模型在Garnet中操控积木块——Sim-eye和Sim-hand的图形化表征使模型者可以观察模型的"行为"。模型花费约一半时间在交互上。
3. **电子战任务模型**（6.3.3）：SLGMS UIMS中的Sim-eye+Sim-hand在两周内实现——证明了跨UIMS的可移植性。

---

## 四、逻辑梳理

### L005
CMIMS的必要性 ← 认知模型需要与真实界面交互 ← 传统建模语言内模拟任务的局限（静态+模型者内建任务状态） ← 解决方案：将Sim-eye+Sim-hand嵌入UIMS ← 实证验证：三个跨架构跨UIMS的案例 ← 未来：更准确的嵌入式助手+what-if设计评估。

---

## 五、材料使用
自我研究案例为主（三个自建系统）+ 相关系统综述（APEX/MIDAS/Driver-Soar/EPIC/ACT-R/PM作为"相关工作"被详细比较）。

## 六、论辩方法
技术架构展示（Figure 6.1的CMIMS概念图是关键"视觉论证"）+ 跨架构验证（Soar+ACT-R两个认知架构均成功使用CMIMS）→ "普遍性"论证。

## 七、语言文风

### L006 原文摘录
> "Models as users has been envisioned before but has not yet been widely applied."
> "The model spent approximately half of its time interacting with the simulation."
> "Authors of interface design tools and of UIMSs should include support for cognitive models as users."

## 八、实体清单

| 类别 | 实体 |
|---|---|
| 人物 | Ritter, Baxter, Jones, Young; Kieras & Meyer (EPIC); Byrne (ACT-R/PM); Newell (Soar) |
| 概念 | CMIMS, Sim-eye, Sim-hand, Cognitive Architecture, Peripheral Vision in Models |
| 系统 | Garnet UIMS, SLGMS, Soar, ACT-R, EPIC, APEX, MIDAS, ACT-R/PM |
| 方法 | GOMS家族, Cognitive Modeling Process, Functional Model of Vision |

## 九、与前后章关联

- **Ch05**：Ch05使用GOMS进行"人类"策略分析；Ch06将GOMS的建模逻辑扩展到"机器模拟人"——互为表里。
- **Ch07 (Vicente)**：Ch06关注"模拟个体用户的认知"；Ch07要求HCI关注"工作者对意外事件的适应"——后者暗示了CMIMS为"规范化任务"建模的固有局限。
- **Ch10 (Myers et al.)**：Ch06对UIMS的依赖直接连接Ch10对用户界面软件工具历史的全面综述。

---

**报告生成日期**：2026-08-05
**L###标记**：L001–L006
