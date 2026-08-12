# 第11章：The Data in Design Protocols: The Issue of Data Coding, Data Analysis in the Development of Models of the Design Process —— 分析报告

> 作者：Terry Purcell, John Gero, Helen Edwards and Tom McNeill（University of Sydney）

---

## 一、章节定位与功能

本章的核心贡献是**开发并示范了一套包含27个类别的三层编码方案**，是全书编码系统最丰富、最系统的篇章。Purcell团队将传统的"数据驱动"编码方法与"理论驱动"编码方法相结合——第一层（Level of Abstraction: 0-System / 1-Subsystems / 2-Detail）和第二层（Problem Domain: Function / Structure / Behaviour / Requirements）来自Gero的设计理论，第三层（Strategy: 四大类共20+子类别）来自协议数据的仔细阅读。本章代表了"悉尼设计计算学派"（Gero学派）的方法论取向——通过细致分类来逼近设计认知的结构。

## 二、结构分析

1. **问题意识**：对现有设计协议编码方法的批判性回顾——指出现有研究要么过度依赖简单的几类编码（如Lloyd & Scott的3类=generative/deductive/evaluative），要么在编码方案之间缺乏可比较性。
2. **编码方案的开发过程（Section 1）**：详述编码方案从Gero & McNeill在电子设计领域的早期工作，经过多次迭代修订，到最终应用于Dan协议的演化轨迹。关键发现：Delft实验中的设计师面对的是"新问题"（需要更多问题分析），而此前的电子工程设计实验中设计者已经在日常工作中完成了问题定义——这一差异导致了编码方案的修订。
3. **编码方案的内容描述（Section 2）**：完整呈现三层27类编码：
   - 第一层（Level of Abstraction）：0-System / 1-Subsystems / 2-Detail
   - 第二层（Problem Domain）：F-Function / B-Behaviour / S-Structure / R-Requirements
   - 第三层（Strategy）：四组——问题分析组（propose/analyse/clarify...）、方案提案组（postulate/interpret/modify...）、方案分析组（evaluate/compare/select...）、显性参照组（refer to own activity/refer to knowledge...）
4. **方法与结果示例（Sections 3-4）**：展示将三层编码应用于Dan协议的方法（编码示例见Table 11.2）和结果分析（时间序列分布图）。
5. **附录**：包含Dan协议最终编码样本——为其他研究者提供了编码方案的可验证实例。

## 三、内容分析（核心论题+关键论点案例）

### 核心论题

**如何开发一套既能捕获设计协议的丰富性、又能保持与其他研究可比较性的编码方案？** Purcell团队的回答是：将"数据生成类别"和"理论推导类别"结合在一个多层结构中——理论（Gero的FBS）提供比较性的"骨架"，数据（仔细阅读协议）提供详实性的"血肉"。

### 关键论点

L1101 对现有编码实践的批判："最近在设计协议分析中出现了向外部强加结构（externally derived structure）的转变"——例如Lloyd & Scott仅使用3类编码。虽然这产生了有趣的结果，但"代表了原始协议细节的严重损失"，且不同研究之间"难以比较"。

L1102 **三层编码方案的设计逻辑**：
- 第一层（抽象层级）回答"设计师在哪里？"——是考虑系统整体（用户视角）还是子系统还是细节？
- 第二层（问题域FBS/R）回答"设计师在做什么类型的推理？"——功能性推理 vs. 行为性推理 vs. 结构性推理 vs. 需求修订
- 第三层（策略）回答"设计师此刻在做什么活动？"——分析问题？提案方案？分析方案？显性参照？

L1103 **"多重编码"的方法论选择**：与传统的"每个片段一个编码"不同，Purcell团队允许"同一个片段获得多重编码"——这是受到了"扎根理论"（Glaser & Strauss）的启发，认为单一编码会丢失数据的丰富性。

L1104 **FBS理论作为统一的比较框架**：Gero的Function-Behaviour-Structure框架"论证了设计涉及三个领域中的推理"——功能（设计的目的）、行为（对象在给定条件下的行动/过程）、结构（物理属性）。这一框架在本章中被用作连接不同设计协议分析的"通用语言"——如果不同研究都使用FBS作为第二层编码，则跨研究比较成为可能。

L1105 **时间可视化的重要性**："时间虽然是设计协议分析的重要方面，但过于强调在整个设计会期长度上的变化会掩盖在极短时间尺度上发生的重要现象"——同一片段的多重编码揭示了"同时性"（simultaneity），片段间的关系揭示了"连续性"。

## 四、逻辑梳理

```
现有编码方法要么过于简略（3类）要么不可比较（各自为政）
→ Gero的FBS理论提供了统一的比较骨架（理论支柱）
→ 协议数据的仔细阅读提供了丰富的类别细节（数据驱动）
→ 三层27类编码方案整合了理论深度和实证丰富性
→ 多重编码（同一片段可有多个编码）保留了数据的复杂性
→ 时间序列可视化揭示推理域的切换模式
→ 方法论贡献：一套可复用、可比较、可扩展的编码方案
```

## 五至九节（综合）

L1106 Purcell团队的学术英语——清晰、结构化、以方法论建构为中心，强调编码方案的"可操作性"和"可比较性"。

**原文摘录**（关于现有编码方案的问题）：
> "While this particular experiment and others using this approach have produced interesting results, they represent a severe loss of detail from the original protocol. The second is that the results of the later experiments are difficult to compare to the earlier work and to each other."

L1107 **实体清单**：John Gero（悉尼大学，设计计算和FBS理论创始人）、FBS Framework（功能-行为-结构推理域模型）、Glaser & Strauss的"扎根理论"方法（多重编码的灵感来源）、27类三层编码方案（本章核心方法贡献）、Appendix A（Dan协议最终编码详例=可复用的方法论资源）。

**与前后章关联**：本章与第9章（Takeda et al.）共享FBS概念的基础——但Gero的FBS与Takeda的FBS在定义上有微妙差异（Gero的"Behaviour"更偏向"对象在给定条件下的行动/过程"，Takeda的"Behaviour"更偏向"状态的顺序变化"）。与第2章（Akin & Lin）在"口头-视觉数据关系"上有间接对话——Purcell的编码方案主要用于口头数据，Akin & Lin则关注口头与视觉数据的互补性。与第6章（Baykan）在编码粒度上形成"细vs.粗"的对比——Purcell的27类 vs. Baykan的6种原始信息过程。

---

*分析完成日期：2026-08-04*
