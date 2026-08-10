# 第六章分析报告：Methods for Protocol Analysis（协议分析方法）

## L### 一、章节定位与功能

### L### 定位
第六章是全书从"理论"转向"技术"的操作性章节。前五章建立了口头报告作为数据的理论合法性（一至三章）和推论方法论（四至五章），第六章则将这一切转化为可执行的操作规程——如何实际地对口头协议进行编码和分析。

### L### 功能
本章承担四重功能：(1) 历史回顾——从Watson(1920)到Newell & Simon(1972)的协议分析方法演变；(2) 方法展示——介绍基于信息加工模型的协议分析基本技术（词汇定义、分段、编码、聚合）；(3) 方法论讨论——探讨编码中的关键问题（上下文使用、信度、效度）；(4) 自动化编码的介绍——PAS和SAPA系统。

### L### 战略意义
第六章是本书对"如何实际做协议分析"的最系统回答。它将前五章的抽象理论原则转化为具体的操作规程——编码者面对一份协议时，第一步做什么、第二步做什么、在什么情况下使用上下文、如何评估编码质量。

---

## L### 二、结构分析

### L### 表层结构
本章共5节，形成"历史→技术→方法论→自动化→总结"的递进：
- 6.1 Early Protocol Analysis —— 早期协议分析（手写笔记时代）
- 6.2 Introduction to Techniques of Protocol Analysis —— 协议分析技术导论
- 6.3 Methodological Issues —— 方法论议题（编码上下文、信度、效度）
- 6.4 Reliability and Validity of Encoding —— 编码的信度和效度
- 6.5 Effective Protocol Analysis Procedures —— 有效的协议分析程序

### L### 深层结构
论证以"三层编码"为主线：
1. **基础层**：词汇定义和分段——从协议中提取编码词汇，识别同义词和规范表达。
2. **编码层**：语句编码——三种编码策略（浅层/深层/基于产生式系统），讨论上下文使用的利弊权衡。
3. **聚合层**：从语句到模式——通过"情节"（episodes）、"解题步骤"或"宏观操作"聚合编码结果。

---

## L### 三、内容分析（核心论题+关键论点案例）

### L### 核心论题
**论题一：编码的理论预设不可避免但可控制。** 协议分析建立在四个基本假设之上（搜寻求解、操作应用、口头化对应STM、信息=操作输入/输出），但这些假设是"弱假设"——广泛兼容于多种信息加工理论。

### L### 核心论题
**论题二：编码的上下文使用是信度与信息保留之间的权衡。** "The use of context in coding protocols involves a tradeoff. On the one hand, interpreting protocol statements in terms of context permits a much larger part of the semantic content of the protocol to be retained... On the other hand, when context is used in interpretation, the evidence provided by each statement is no longer wholly independent."

### L### 关键论点
1. **词汇编码的节俭性**：对于结构良好的问题解决任务，一个小型词汇表（数十到数百个词项关系）足以覆盖超过90%的协议语言。河内塔协议约2000词，词汇量仅约165个不同词。

2. **同义词替换的风险**：将"smallest disk"替换为"Disk 1"虽然在编码上是可靠的简约操作，但可能丢失关于被试知觉编码的信息——"smallest disk"这一表述本身提供了关于被试如何表征信息的重要线索。

3. **上下文使用的程度分层**：三层编码策略的上下文依赖程度依次递增——
   - 浅层编码（如河内塔协议的Move(3;A,C)编码）：几乎不需上下文。
   - 深层编码（如Bhaskar & Simon 1977的SAPA系统）：需要识别语句所属的"行动"类别。
   - 产生式系统编码（如Newell & Simon 1972的密码算术协议）：需以整个产生式系统为上下文。

4. **自动化=完美的一致性和明确的假设**：自动化编码（PAS系统）的最大优势是——"Reliability is perfect ... and the robustness of the encoding to changes in the underlying vocabulary and rules can be tested directly."

5. **跨编码者信度可达到.8-.9**：在理解任务的编码者手中，基于上下文的编码可以达到高信度。

### L### 关键案例
1. **河内塔协议的Move/Goal/Plan编码**（Figure 6-1）：展示如何将"l'll place 3 from A to C"编码为"Move(3;A,C)"，以及如何通过"so"和"because"等话语标记区分推理链。
2. **密码算术协议的深层产生式编码**（Figure 6-2）：展示Newell & Simon如何以整个产生式系统为上下文进行最深层编码。
3. **SAPA系统的"行动"编码**：选择系统、注意关键词、写出能量方程、修订方程等——编码词汇从任务分析中推导。
4. **聚合技术的对比**：情节聚合（将非问题性的子目标处理为宏操作）、解题步骤聚合（区分专家"前进式"和新手"后退式"推理路径）。

---

## L### 四、逻辑梳理（论证链条+因果转折）

### L### 论证链条
1. **历史背景**（6.1）：磁带录音机普及前的协议分析方法受限于实时手写笔记——不可靠、不可重复分析。
2. **技术确立**（6.2）：基于四个弱假设，建立协议分析的标准流程：定义编码词汇→扫描未覆盖的语句→补充词汇→分段→编码→聚合。
3. **方法论深化**（6.3-6.4）：讨论编码中的核心问题——
   - 上下文的使用程度
   - 编码者间信度（.8-.9可达成）
   - 编码效度（协议与理论的一致性始终是整体系列假设的一致性检验）
4. **自动化方案**（6.4）：PAS和SAPA系统——前者全自动，后者半自动交互式支持编码者。
5. **实践总结**（6.5）：提出有效协议分析的"最佳实践"建议。

### L### 因果转折
- **关键转折1**（约1945年）：磁带录音机的普及使逐字转录成为可能——"The practice of transcribing the tapes literally into typewritten form developed rapidly"——这是协议分析方法论的根本转折点。
- **关键转折2**（约1956年）：计算机模拟认知过程的出现——模型开始做出关于"什么信息被处理"的明确声称，可与协议直接比较。
- **关键转折3**：从"编码者信度"到"全系统一致性"——认识到协议编码从来不是在检验一个孤立的假设，而是在检验一整体系列假设（问题空间定义+推理规则+行为理论）的相互一致性。

---

## L### 五、材料使用方式

### L### 材料类型
1. **历史研究**：Watson (1920)、Duncker (1926, 1945)、de Groot (1965)——展示录音前时代的协议分析方法。
2. **当代编码研究**：Newell & Simon (1972)的密码算术协议、Anzai & Simon (1979)的河内塔协议、Bhaskar & Simon (1977)的SAPA系统。
3. **方法论反思**：关于上下文使用、信度评估的讨论。
4. **技术系统**：PAS-I/II（Newell & Waterman）、SAPA（Bhaskar & Simon）。

### L### 使用策略
- **历史进化叙事**："早期无法录音→录音普及→逐字转录→计算机模拟→自动化编码"——以技术进步驱动方法进化。
- **"良好实践"示范**：以河内塔和密码算术协议的编码为范例，展示"如何做"。
- **"利弊权衡"框架**：不提供绝对规则（"绝不使用上下文"），而是提供权衡框架（"在什么情况下使用多少上下文"）。

### L### 材料整合方式
本章大量"引用"前五章中已经介绍过的研究，但以方法论的视角重新组装——不是关注这些研究"发现了什么"，而是关注它们"如何分析协议"。

---

## L### 六、论辩与阐述方法

### L### 主要论辩策略
1. **"弱假设"策略（延续第一章）**：编码方法的四个基本假设被明确标注为"weak postulates"——它们兼容广泛的理论变体。
2. **"展示优于讲述"策略**：以大量编码实例（Figure 6-1, 6-2）而非抽象描述来说明编码方法。
3. **"元方法论"策略**：不仅讨论"如何编码"，还讨论"为什么这样编码是合理的"——将方法论本身作为反思的对象。
4. **"技术中性"策略**：同时介绍手工编码、半自动编码（SAPA）和全自动编码（PAS），不偏好任何一种，而是讨论各自适用的情境。

### L### 辅助阐述方法
- **编码实例展示**：以河内塔协议的逐句编码展示分段和编码过程。
- **比较表**：对比不同编码层级的上下文依赖程度。
- **技术史叙事**：从Watson到Newell & Simon的方法进化。

---

## L### 七、语言文风（原文摘录+L###）

### L### 总体风格
操作手册体——清晰、条理化、以"如何做"为导向。与前几章的理论辩论体形成鲜明对比。然而，本章的"操作手册"风格中始终保持着方法论反思的深度——作者不仅告诉读者"做什么"，还告诉读者"为什么这样做是合理的"。

### L### 关键原文摘录
1. "The major theoretical assumptions that underlie these methods are ... [four assumptions] ... The first two of these four assumptions can be viewed as weak postulates about the problem-solving process."——编码方法的理论基础。
2. "A good rule of thumb for protocols of any considerable length is that the number of different words will be between five and ten per cent of the length of the text."——关于协议词汇量的经验法则。
3. "The use of context in coding protocols involves a tradeoff."——关于上下文使用的核心权衡。
4. "Notice that the test is really simultaneously a test of the mutual consistency of the problem space definitions, the inference rules for encoding, and the theory of the subject's behavior."——关于编码效度的元方法论反思。
5. "Readers who have had actual experience in encoding verbal protocols will not underestimate the importance of this last point."——关于半自动化编码工具减轻编码者疲劳的实用价值的诚实承认。

### L### 文风特征
- **精确的指令性语言**：使用了大量的"may be defined as"、"should be kept as narrow as possible"等规范表述。
- **经验法则的提供**："a small vocabulary (in the dozens and hundreds, not thousands) ... is sufficient to code more than ninety per cent of the language"。
- **实用主义的诚实**：不追求完美编码，而是讨论在什么条件下达到"足够好"的编码。
- **元认知意识**：频繁反思"我们现在在做什么、为什么这样做"。

---

## L### 八、实体清单（六类，每类≥3+L###）

### L### 人物实体
1. **Allen Newell**——与Simon合作开发了密码算术和逻辑问题的协议分析方法、Problem Behavior Graph和PAS系统。
2. **John B. Watson (1920)**——进行了有文献记载的最早的"想出声"协议分析。
3. **Adriaan de Groot (1965)**——使用Selz (1913)的框架编码国际象棋选手的TA协议，重建了被试的搜索树。
4. **R. Bhaskar**——与Simon合作开发了SAPA（半自动化协议分析）系统。
5. **Donald Waterman**——与Newell合作开发了PAS-I和PAS-II全自动化协议分析系统。
6. **Y. Anzai**——与Simon合作发表了河内塔协议的详细编码分析。

### L### 著作/文献实体
1. **Newell & Simon (1972) "Human Problem Solving"**——提供了协议编码的最详尽范例（密码算术协议第165-183页）。
2. **de Groot (1965) "Thought and Choice in Chess"**——早期协议分析的经典，使用Selz的框架编码国际象棋思维。
3. **Duncker (1926, 1945) "On Problem Solving"**——早期协议分析的奠基之作，对20多个问题的协议进行了功能编码。
4. **Newell & Waterman (1971, 1973) PAS-I / PAS-II**——全自动化协议分析系统的文档。
5. **Bhaskar & Simon (1977) SAPA系统**——半自动化协议分析系统，特别针对热力学问题。
6. **Zipf (1949) / Yule (1924)**——作者引用其等级-频率定律来说明协议词汇的分布特征。

### L### 理论/模型实体
1. **编码方法的四个基本假设**——搜寻求解、操作应用、口头化对应STM、信息=操作I/O。
2. **编码的三层策略**——浅层（基于局部信息）、深层（基于任务分析中的"行动"类别）、产生式层级（基于完整产生式系统）。
3. **上下文-独立性权衡模型**——上下文越多→语义保留越多→但证据独立性越低。
4. **问题行为图（Problem Behavior Graph）**——Newell & Simon的核心分析工具，将协议映射为知识状态序列。
5. **情节聚合理论（Episoding Theory）**——非问题性子目标被压缩为宏操作，用于协议的高层概览。
6. **Zipf定律在协议中的应用**——约一半的词汇只出现一次，对编码的节俭性是严重阻碍。

### L### 概念/术语实体
1. **Segmentation（分段）**——将协议切分为与语句对应的独立分析单元。
2. **Canonical Recording（规范转写）**——通过同义词定义为协议建立简化的标准表达形式。
3. **Encoding Vocabulary（编码词汇）**——从任务分析和协议中提取的用于编码的术语集合。
4. **Macro-Operator（宏操作）**——经过良好练习的子目标达成过程被打包成的单一操作。
5. **Anaphoric Reference（回指引用）**——代词和描述性命名，需要上下文消歧。
6. **Inter-Coder Reliability（编码者间信度）**——不同编码者独立编码同一协议的一致性程度。

### L### 实验/研究实体
1. **Anzai & Simon (1979)的河内塔协议编码**——展示从第一试次（低度格式化的评估性语句）到第四试次（高度格式化的Goal/Plan/Move语句）的变化。
2. **Newell & Simon (1972)的密码算术协议深层编码**——Figure 6-2展示了产生式系统层级的编码。
3. **Bhaskar & Simon (1977)的SAPA系统应用于热力学问题解决**。
4. **Simon & Simon (1978)的物理问题解决中的专家-新手比较**——区分"前进式"和"后退式"推理。
5. **Watson (1920)的"想出声"分析**——有文献记载的最早案例。
6. **De Groot (1965)的国际象棋协议分析**——展示了在不完全记录条件下仍能重构搜索树的可能。

### L### 机构/工具实体
1. **PAS-I / PAS-II（Protocol Analysis System）**——Newell & Waterman开发的全自动化协议分析系统。
2. **SAPA（Semi-Automated Protocol Analysis）**——Bhaskar & Simon开发的半自动化交互式协议分析程序。
3. **Tape Recorder（约1945年普及）**——使逐字转录成为可能，是协议分析方法论革命的技术基础。
4. **Computer Simulation Programs**——用于生成可与协议直接比较的"程序轨迹"。
5. **Production System Formalism（产生式系统形式化方法）**——Newell & Simon的编码框架。
6. **First Order Predicate Calculus（一阶谓词演算）**——在某些形式化编码中被用作表示工具。
7. **MPAS（Mini Protocol Analysis System）**——第六章6.4节介绍的第三种协议分析系统（正文L4858起"## Mini Protocol Analysis System"一节，原书索引第291-293页）：一个交互式计算机编码程序，核心思想是控制编码者编码每个协议段时可用的信息——从多个协议随机抽样分段呈现，使编码者无法推断当前段与先前段的关系，从而满足编码独立性标准；上下文可按需逐步扩展并记录用量。【校对修正】原报告仅列PAS与SAPA，遗漏MPAS，现补充。

---

## L### 九、与前后章关联

### L### 与第五章的关联
第五章的口头化六假设模型为本章的编码方法提供了理论依据。本章的四个基本假设是第五章六假设在编码实践层面的操作化。

### L### 与第七章的关联
本章是"方法"章，第七章是"实例"章——第七章用大量具体案例展示本章描述的方法在实际协议分析中如何应用。两章构成"方法-实例"对。

### L### 与第四章的关联
第四章对"低层编码vs高层编码"的比较性评价在第六章被转化为具体的编码建议——"retain, as fully as possible, the content of the protocol (low-level encoding)"。

### L### 与前三章的关联
第一至三章建立了口头报告作为数据的合法性，第六章则将这一合法性转化为操作规程——如果口头报告是合法数据（前三章），那么它是"如何"被加工的（第六章）。

### L### 跨章论证线索
本章体现出本书的一个核心理念：**协议分析的编码方法应与信息加工理论融贯一致。** 编码不是在"理论中性"的环境中进行，而是以"尽可能弱但充分的理论假设"为指导。这一理念从第一章的"最弱理论策略"开始，到第六章的"编码四假设"被具体实施。
