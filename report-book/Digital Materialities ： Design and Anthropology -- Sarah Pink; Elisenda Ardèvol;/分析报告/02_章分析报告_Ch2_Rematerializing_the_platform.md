# 02_章分析报告：Rematerializing the platform: Emulation and the digital–material

**作者**：Paul Dourish
**位置**：Chapter 2，Part One（Expectations）
**源文行号**：L326-L462

---

## 一、章节定位与功能

本章通过计算机仿真（emulation）这一技术案例，从计算机科学内部论证"数字本身即是物质的"这一全书核心命题。Dourish挑战了"虚拟性"（virtuality）话语中隐含的"去物质化"假设，提出仿真实践所揭示的恰恰是一种"再物质化"（rematerialization）过程——虚拟计算机的构建需要精确复制原机器的硬件缺陷、时序特征和输入输出特性。本章在全书中的功能是**技术本体论的深层奠基**：以计算机科学家的"内部视角"为全书铺陈数字物质性的技术基础。

## 二、结构分析

| 节段 | 起始行 | 核心内容 |
|------|--------|----------|
| Introduction | L330-L346 | 提出"虚拟时代"话语遮蔽了数字的物质性 |
| The digital–material | L348-L383 | 以Python程序和数字系统的"欠规范性"论证数字的物质性 |
| Emulation | L385-L398 | 介绍仿真概念：从Turing机到Amiga/Warhol案例 |
| Problems of materiality in virtual computers | L399-L445 | 三个维度分析仿真中的物质性问题 |
| -- Instructions and representations | L403-L413 | 指令作为"物"而非纯粹数学形式，PDP-10虫子案例 |
| -- Timing | L415-L433 | 模拟时序问题：CRT扫描、垂直消隐期的物质性 |
| -- Input and output | L435-L445 | 输入输出的非Turing可计算性 |
| Virtualization and rematerialization | L447-L457 | 结论：仿真揭示虚拟化实为再物质化 |
| Acknowledgements | L459-L460 | — |

## 三、内容分析

### 核心论题
"虚拟性"是数字性的核心话语策略，而计算机仿真——作为"双重虚拟"——恰恰暴露了虚拟性的不可维持性。Dourish的核心命题是：**"virtualization is better seen as rematerialization"**（L396），即每次虚拟化操作本质上是在新的物质基础上重新实现数字体验。

### 关键论点与案例

**论点1：计算机程序的"欠规范性"（underspecification）构成数字的物质性**
- 以图2.1的Python程序为例：程序并不"标注"（notate）处理器速度、内存容量、网络特征和最大可表示数等所有影响执行的条件。
- "The materialities of digital systems lie...in this gap between what is denoted and what is expressed, or between the specification and the execution"（L379）
- "the experience that is the result of the program's execution is radically underspecified by that program"（L379）

**论点2：仿真不是简单的"寻找等价指令"**
- PDP-10克隆的经典案例：研究者Ed Fiala发现了PDP-10浮点运算中的bug，在克隆机中"修复"了它们，但随后发现部分软件恰好依赖这些bug才能运行。
- "Fiala was asked to program the bugs back into his implementation, so that it would be wrong, but in the same way as the PDP-10"（L412）
- 论旨："what needs to be reproduced and reenacted is the entire mechanism into which those instructions fit"（L412）

**论点3：仿真需要再现非数字元素**
- CRT显示器的"垂直消隐期"（vertical blanking interval）成为早期游戏编程的关键约束（Montford & Bogost的Racing the Beam）。
- "the production of the virtual 'guest' computer means the reproduction not only of the digital elements of the original machine, but also thoroughly non-digital components"（L433）

**论点4：实际计算机"多于"也"少于"Turing机**
- 少于：实际计算机没有无限存储。
- 多于：实际计算机可以播放音乐、连接网络——这些输入输出功能在数学上超出Turing可计算性的范畴。
- "A real 'Turing machine' wouldn't sell very well in the marketplace"（L443）

### Andy Warhol Amiga案例
2003年，Warhol博物馆与CMU合作，通过Amiga仿真器恢复了Warhol在1980年代用Commodore Amiga创作的数字艺术作品——原始硬件已不可得，但仿真器使得软件可以"不加修改地"在当代PC上运行（L387-L388）。

## 四、逻辑梳理

### 论证链条
**问题提出**："虚拟时代"话语默认虚拟/物质二分 → **反驳**：学界从基础设施、组织理论、设计实践三个角度强调物质性，但这些批评"leave the duality between materiality and virtuality intact"（L340）→ **论证转折**："the digital is itself material"（L343）→ **方法选择**：以仿真——"双重虚拟"——作为"particular fruitful perspective"（L447）→ **三重经验论证**：(1)指令的物质性(PDP-10虫子)→(2)时序的物质性(CRT扫描、垂直消隐期)→(3)输入输出的物质性(非Turing可计算性)→**结论**："in practice, the problems of virtuality become particularly visible"（L384），仿真不是从物质到虚拟的迁移，而是"a new material foundation for digital experience"（L395）。

### 关键因果转折
- 转折1：从"学者强调物质性"到"但他们保留二分法"——引出本章的独特贡献。
- 转折2：PDP-10案例中"修复bug→破坏了软件→重新引入bug"的因果反转，强有力地展示物质性不可消除。
- 转折3：从"数字元素"到"CRT的模拟（analog）特性"——物质性从数字内部扩展到非数字外围。

## 五、材料使用方式

1. **计算机科学内部史作为论证资源**：Turing (1936) 的"通用机"论文、Xerox PARC历史、PDP-10克隆轶事——这些不是"外部批判"而是"内部揭示"。
2. **个人编程史的经验调用**："On my Mac laptop, I can run cbm, an emulator of the Commodore PET 2001, the first computer I ever used"（L391）——将自传经验用作方法论证据。
3. **数学论证与工程实践的对照**：Church-Turing论题定义了可计算函数，但实际计算机"are both more than and less than Turing-equivalent machines"（L441）。
4. **案例的递进性组织**：从简单程序→PDP-10→CRT时序→音乐播放——案例复杂度逐步升级，论证的物质性维度逐步拓宽。

## 六、论辩与阐述方法

1. **"insider critique"策略**：Dourish作为计算机科学教授，从学科内部进行批判，避免外部批判者常见的简化。
2. **从日常Intuition出发的逐步复杂化**：以"数字作为表征系统"这一常识为起点，逐步揭示表征的不完整性。
3. **技术细节的"精读"**：对指令集、时序、CRT垂直消隐期等技术细节进行细致展开，以此展示"物質性在细节中"。
4. **悖论性修辞**："this is a case that is twice virtual"（L384）——以仿真作为"双重虚拟"的极端案例来反证虚拟性本身的不可维持。
5. **个人经历的"温和侵入"**：在严谨的技术讨论中插入个人计算机使用史，打破客观性幻觉。

## 七、语言文风

### 原文摘录

**L001 核心隐喻**
> "I want here to use the case of emulators to examine virtualization as rematerialization – not as a move away from the material to create a domain of the virtual, but rather a new material foundation for digital experience."（L395-L396）

**L002 PDP-10经典案例**
> "Investigation revealed that some software was failing because it depended on the very bugs that Fiala had corrected. With software compatibility as a key requirement for the new computer, only one solution was possible; Fiala was asked to program the bugs back into his implementation, so that it would be wrong, but in the same way as the PDP-10."（L411-L412）

**L003 程序的不完整性**
> "A computer program may be a precise series of instructions, and yet the experience that is the result of the program's execution is radically underspecified by that program."（L379）

**L004 虚拟性的不可维持**
> "The denial of materiality that is at the centre of the rhetoric of virtuality could be maintained only if the specification were complete: if a program really were an adequate account of what will happen in execution..."（L381）

**L005 物质性的"顽固"侵入**
> "a further intrusion of the obstreperously non-virtual"（L433）

### 文风特征
- 精湛的技术精确性与人文反思性的结合——Dourish的写作同时面向计算机科学家和社会科学家
- 善于用简短的技术轶事（PDP-10虫子）承载深度理论寓意
- 使用日常技术经验为桥梁（"On my Mac laptop I can run..."）
- 句子结构清晰、层次分明，大量使用"not simply...but rather..."的对比结构
- 语言中带有机智感：如"further intrusion of the obstreperously non-virtual"

## 八、实体清单

### L008 人物实体（≥3）
| 编号 | 姓名 | 学科/身份 | 在章中角色 |
|------|------|-----------|------------|
| P001 | Alan Turing | 数学/计算机科学 | "通用机"概念奠基者，1936论文被引为仿真理论基础 |
| P002 | Andy Warhol | 艺术家 | Amiga数字艺术作品案例主角 |
| P003 | Ed Fiala | 计算机研究员 | PDP-10克隆中"修复"又"重新引入"bug的关键人物 |
| P004 | Cory Arcangel | 艺术家 | 2003年Warhol数字作品恢复项目的合作艺术家 |
| P005 | Butler Lampson | 计算机科学家 | Xerox Alto设计师，CRT显示时序优化的轶事来源 |
| P006 | Michael Hiltzig | 科技史作者 | 提供PDP-10克隆历史的记录者 |
| P007 | David Hilbert | 数学家 | 1928年提出Entscheidungsproblem，催生Turing的工作 |

### L009 著作实体（≥3）
| 编号 | 著作 | 作者 | 年份 | 在章中角色 |
|------|------|------|------|------------|
| B001 | On Computable Numbers | Alan Turing | 1936 | 计算机科学奠基论文 |
| B002 | Racing the Beam | Montford & Bogost | 2009 | Atari VCS编程与CRT扫描时序的详细分析 |
| B003 | Dealers of Lightning | Michael Hiltzig | 1999 | XOR PARC历史，PDP-10克隆轶事来源 |
| B004 | Divining a Digital Future | Dourish & Bell | 2011 | ubicomp的"mess"讨论 |

### L010 概念实体（≥3）
| 编号 | 概念 | 出处/提出者 | 含义 |
|------|------|-------------|------|
| C001 | rematerialization | Dourish | 虚拟化不是去物质化，而是在新物质基础上重新实现 |
| C002 | underspecification | Dourish | 程序规范与实际执行之间的"间隙"，数字物质性所在 |
| C003 | Turing-equivalent machine | Turing | 可计算任何可计算函数的理论机器 |
| C004 | emulation | 计算机科学 | 用一台计算机（host）在软件中模拟另一台（guest） |
| C005 | vertical blanking interval | 显示技术 | CRT扫描电子束从右下角回到左上角的间隙 |
| C006 | notation vs enaction | Dourish | 标注（程序文本）与执行（实际运行）之间的差异/滑动 |

### L011 机构/地点实体（≥3）
| 编号 | 名称 | 类型 | 在章中角色 |
|------|------|------|------------|
| I001 | Xerox PARC | 研究中心 | PDP-10克隆发生地，HCI诞生地 |
| I002 | Carnegie Mellon University | 大学 | 2003年Warhol Amiga图像恢复项目合作伙伴 |
| I003 | Andy Warhol Museum | 博物馆 | 保存Warhol Amiga软盘的机构 |
| I004 | UC Irvine | 大学 | Dourish所在机构 |

### L012 技术/物质实体（≥3）
| 编号 | 名称 | 类型 | 在章中角色 |
|------|------|------|------------|
| T001 | PDP-10 | 计算机 | DEC大型机，Xerox PARC克隆目标 |
| T002 | Commodore Amiga | 计算机 | Warhol使用的早期多媒体个人计算机 |
| T003 | CRT (Cathode Ray Tube) | 显示技术 | 其扫描物理特性构成仿真时序难题 |
| T004 | MOS 6502 processor | 处理器 | Apple II使用的CPU，用于展示指令与时机的不标注性 |
| T005 | Xerox Alto | 计算机 | 首个GUI工作站，66%处理时间用于显示管理 |
| T006 | Python programming language | 编程语言 | 图2.1中用于展示"程序标注的不完整性" |

### L013 事件实体（≥3）
| 编号 | 名称 | 时间 | 在章中角色 |
|------|------|------|------------|
| E001 | Warhol Amiga artwork recovery | 2003 | 通过仿真恢复Warhol已失的数字艺术 |
| E002 | Apple PowerPC-to-Intel transition (Rosetta) | 2006 | 商业仿真器案例 |
| E003 | PDP-10 clone at Xerox PARC | 1970s | 经典仿真/克隆困境案例 |

## 九、与前后章关联

- **与Ch1**：Ch1声称"the digital is itself material"——Ch2以仿真技术实践为此提供最技术性的经验论证。
- **与Ch3(Lanzeni)**：Ch2揭示"虚拟性"话语的物质盲点——Ch3展示"智能"全球想象如何遮蔽地方的物质实践。两章共同构成Part One对"期望"（Expectations）的批判审视。
- **与Ch4(Strengers)**：Ch2展示"再物质化"——Ch4展示智能家居从乌托邦愿景到日常物质实践的"再落地"。时序上的类比：Ch2的"仿真≠复制原机器"对应Ch4的"技术脚本≠日常使用"。
- **与Ch8(Mueller)**：Ch2援引Dourish自己的"embodied interaction"理论传统——Ch8将身体视为数字物质性本身，进一步推进"数字的物质性"命题。

---
*报告生成日期：2026-08-04*
