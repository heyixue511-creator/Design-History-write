# 第9章：Analysis of Design Protocol by Functional Evolution Process Model —— 分析报告

> 作者：Hideaki Takeda¹, Masaharu Yoshioka², Tetsuo Tomiyama² and Yoshiki Shimomura³（¹Nara Institute of Science and Technology, ²University of Tokyo, ³Mita Industrial Co. Ltd.）

---

## 一、章节定位与功能

本章是全书中最具**人工智能和知识工程**色彩的研究。四位日本研究者使用自创的FBS（功能-行为-状态）建模和FEP（功能演化过程）模型来分析团队协议——目标不是解释设计行为的认知机制，而是**验证FBS/FEP作为一个知识建模框架能否充分表示设计过程中的功能推理**。本章的核心功能地位可概括为：它是全书的"AI/知识工程分析极"——代表了将设计协议分析视为"知识抽取"（knowledge elicitation）而非"认知研究"的研究范式。

## 二、结构分析

1. **功能-行为-状态建模（Section 1）**：系统阐述FBS框架的核心概念——区分三个表示层次（功能/行为/状态），定义功能为"通过对行为的利用性识别而被抽象的行为描述"（a description of behaviour abstracted through the recognition of that behaviour for utilization），区分"功能体"（function body=动词如'move''carry'）与"功能修饰语"（functional modifier=副词如'precisely''firmly'）——功能修饰语的关键特性：它有满足度（degree of satisfaction），可以比较两个对象——"一个功能有与其功能修饰语一样多的评价标准。"
2. **功能演化过程（Section 2）**：提出四种功能关系类型：(1)Decompose（分解）——功能A分解为子功能B、C；(2)Be-caused-by（被引起）——功能B是功能A的必要条件，由行为层面的因果关系支持；(3)Be-reinforced-by（被强化）——功能B被推荐存在以使功能A更好地实现其功能性（B不是A的必要条件）；(4)Decompose-modifiers（修饰语分解）——一个修饰语可以被分解为更细的修饰语。
3. **协议数据分析（Section 3）**：使用团队协议（至1:49）的数据，按照FBS/FEP框架提取功能、功能修饰语、行为和结构，并构建了功能演化图（Functional Evolution Graph）。
4. **总结（Section 4）**：肯定FBS/FEP模型在表示设计过程功能推理方面的有效性。

## 三、内容分析（核心论题+关键论点案例）

### 核心论题

**功能在设计过程中是如何演化的？能否用一个形式化模型来捕捉这一演化过程？** 本章的回答通过FBS/FEP的双层建模实现——功能不是静态的标签，而是在设计过程中通过分解、因果链接和强化关系不断细化、拓展和收敛的动态网络。

### 关键论点

L901 **功能与行为的区分**——这是一个核心的理论澄清：行为可以从对象和环境的状态直接推导（由物理定律支配），而功能还与设计师对对象的感知有关。汽车的例子：同一行为（移动）可被不同人识别为不同的功能（"移动"/"运载"/"围合"）。功能是"通过利用性识别而被抽象的行为描述。"

L902 **功能修饰语（functional modifier）的关键性**：功能修饰语不是功能的"装饰"或"次要属性"——"功能修饰语是表征一个功能如何被实现的评价标准。"FBS的一个重要创新是将修饰语提升为与功能体同等重要的分析对象——一个功能有"与其功能修饰语一样多的评价标准。"

L903 **"be-reinforced-by"关系的独特贡献**：这是FEP模型中最具原创性的关系类型——它捕捉的不是必要因果链接，而是"推荐性的"强化关系："功能B不是功能A的必要条件，因为A可以没有B而存在。但有了B，A将更好地完成其功能性。"这一类型的关系无法从纯行为因果中推导——它只能从功能评价中产生。

L904 **功能演化图的可视化**：Figure 9.3展示了一个"称重秤"设计项目的功能演化图——节点代表功能和功能修饰语，边代表decompose/be-caused-by/be-reinforced-by关系。这一可视化方法为理解设计过程的功能推理结构提供了强大的认知工具。

L905 **协议分析中的启发式提取**：作者坦承从协议中提取FBS元素"不是一个纯语法操作，而是一个依赖于上下文的启发式操作"——使用语法信息作为发现功能/行为/结构类型的"提示"（如动词=功能的指标）。这一方法论诚实性值得注意。

## 四、逻辑梳理

```
功能是设计的核心概念但其定义模糊（问题意识）
→ FBS区分了功能/行为/状态三个表示层次（概念澄清）
→ 功能通过四种关系类型在时间中演化（FEP模型）
→ 团队协议数据被用于测试FBS/FEP的解释力（实证应用）
→ 功能演化图展示了功能的逐步细化过程（可视化结果）
→ FBS/FEP模型能够充分表示设计过程中的功能推理（验证结论）
```

## 五至七节（综合）

L906 AI/知识工程领域的学术英语——形式化、系统化、使用Lisp-like符号表示，包含大量的图表和形式定义。

**原文摘录**：
> "Function is not only related to the state of objects and their environment but also related to the perception of the object by designers."

L907 "perception"（感知）一词是关键——它将功能从客观的物理属性中拉出，锚定在设计师的主观识别中。这一理论立场与Schön的"反思性实践"和Dorst & Dijkhuis（第12章）的"建构主义"范式有潜在的亲和性。

## 八、实体清单（精简）

L908 **FBS (Function-Behaviour-Structure) Modelling**：三层对象表示框架——"状态"=实体+属性+关系，"行为"=对象状态的顺序变化（由物理定律支配），"功能"=通过对行为的利用性识别而被抽象的行为描述。

L909 **Functional Evolution Process (FEP)**：功能在时间中的演化过程——通过decompose、be-caused-by、be-reinforced-by和decompose-modifiers四种关系运作。

L910 **Aspect（方面）**：FBS的基本分析单元——由术语定义、实体（结构）和规则（物理定律）组成的集合。设计涉及多个方面（从刚性体动力学等"良好定义"的方面到可制造性等"模糊定义"的方面）。

L911 **Functional Evolution Graph（功能演化图）**：FEP的可视化表示——以节点（功能+修饰语）和边（四种关系类型）构成的依赖图。可用于定性仿真（"What-if?"和"How-to?"问题）。

L912 **Lisp-like Representation**：功能的形式化表示——(function-body subjective objective1 ...)，例如(carry/fasten device backpack bicycle)。

## 九、与前后章关联

本章与第8章（Ullman et al.）在"对象-关系"模型上有理论近缘性——Ullman的"对象-关系-属性-值"和Takeda的"功能-行为-状态"共享对设计的"结构化表示"兴趣，但层次不同（Ullman偏产品物理结构，Takeda偏功能推理）。与第12章（Dorst & Dijkhuis）的"范式比较"形成认识论对话——FBS/FEP属于Simon式的"理性问题解决"范式，而Dorst & Dijkhuis质疑的正是这个范式的完备性。与第11章（Purcell et al.）的FBS编码方案有直接的方法论对应——第11章也使用"功能/行为/结构"作为编码类别，但用于不同的分析目的（描述推理域vs.建模功能演化）。

---

*分析完成日期：2026-08-04*
