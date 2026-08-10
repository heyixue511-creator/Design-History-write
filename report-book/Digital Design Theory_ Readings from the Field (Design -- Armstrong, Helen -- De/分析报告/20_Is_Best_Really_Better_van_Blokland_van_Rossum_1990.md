# 20 Is Best Really Better — Erik van Blokland & Just van Rossum (LettError) | 1990

作者：Erik van Blokland & Just van Rossum (LettError设计二人组) | 出处：Emigre 18 (1990) | 文本类型：字体设计宣言/技术实验报告

## L001 一、章节定位与功能

LettError的"Is Best Really Better"在Section Two中定位于**数字字体的"后完美"宣言**——是对现代主义"追求最高品质"信条的讽刺性颠覆。其功能为：(1) 以RandomFont技术（随机扰动每个字符轮廓上的点）证明"不完美"可以在数字字体中产生生命力(vitality)；(2) 将字体从"固定的物体"重新定义为"可变的数据"——数字字体的每一次输出可以是不同的；(3) 以幽默/反讽的方式提出大量"病毒字体""自毁字体""字体流感"等恶作剧式的未来场景，挑战字体行业的正统商业逻辑。

## L002 二、结构分析

论文结构为**批判→实验→推演**。(a) 批判：技术上最完美的印刷品反而变得"绝对无聊"——"The quality of a printed product, the high resolution of its typefaces, the perfect printing are not necessarily what makes for good design or clear communication."(b) 实验：Beowolf RandomFont——"Random technology...is about letting the rasterizer behave randomly within the boundaries of legibility."——每次输出时字符轮廓点随机扰动，因此每个字符每次打印都不同。(c) 推演：一系列恶作剧式的"未来字体"方案——病毒字体（自传播字体）、酸奶字体（文件会变质）、磨损字体、智能字体（根据天气条件改变对比度）、自我破坏字体（常用字逐渐磨损）。

## L003 三、内容分析

**核心论题**："Quality"（品质/完美）不是好设计或清晰传达的必要条件——甚至可能妨碍它。数字技术使我们能够重新获得活字印刷时代因经济/技术因素而丧失的活力(vitality)。

**关键论点**：(1) **历史批判(L003-1)**："The developments in typeface design, typesetting, and printing have always been aimed at the improvement of 'quality.'...Unfortunately, the results have too often become absolutely boring."(2) **RandomFont定义(L003-2)**："Instead of re-creating a fixed outline or bitmap, the RandomFont redefines its outlines every time they are called for. Thus, each character will be different each time it is printed."(3) **去物质化(L003-3)**："Through our experience with traditional typesetting methods, we have come to expect that the individual letterforms of a particular typeface should always look the same. This notion is the result of a technical process, not the other way around."——"始终相同"是技术条件的结果，不是字体本体论的要求。(4) **识别不依赖重复(L003-4)**："Recognition does not come from simple repetition of the same form but is something much more intelligent, something that happens in our minds."——认知心理学论证：识别声音时即使感冒变音也能听出是谁，字体的可识别性不依赖完全相同的重复。

## L004 四、逻辑梳理

**论证逻辑链**：品质追求的历史悖论（追求完美→无聊）→数字字体的去物质化（字体从固定对象变为数据/指令）→RandomFont实验（每次输出不同的随机扰动字符）→本体论结论（字体的同一性只是技术偶然性的结果，不是设计必然性）→恶作剧式的未来推演（如果字体不再是固定的，会有什么可能？）→文化政治的暗流（对"字体工业标准化"的讽刺性瓦解）。

## L005-L007（合并）

**材料使用**：以自身技术实验(Beowolf)为核心材料，以幽默的未来场景构想为论证扩展。

**阐述方法**："实验性证明+讽刺性想象"——通过技术实验证明可能性，通过夸张的幽默想象揭示更广泛的含义。病毒字体、酸奶字体等构想虽然恶作剧，但深刻地揭示了"代码=法律"（code is law）的数字世界本体特征。

> **原文摘录L007-1**："This notion is the result of a technical process, not the other way around."

> **原文摘录L007-2**："Recognition does not come from simple repetition of the same form but is something much more intelligent, something that happens in our minds."

## L008 八、实体清单

### L008-1 人物：Erik van Blokland, Just van Rossum (LettError二人组), Erik Spiekermann(FontFont字体库/FontShop创始人/Beowolf发行者), Donald Knuth(Metafont/被LettError友好提及为"first"), Gutenberg(提及/历史参照)

### L008-2 概念：RandomFont/Beowolf（随机字体技术）, Dematerialization of Type（字体的去物质化/从物理对象到数据指令）, Programming-Assisted Design（编程辅助设计/设计师设置参数计算机随机变化）, Virus Font（病毒字体/恶作剧未来构想）, Recognition ≠ Repetition（识别不等于重复）

### L008-3 技术/工具：PostScript, Linotronic, LaserWriter, FontFont Library, The Hague Royal Academy of Art

### L008-4 出版物：Emigre 18(1990), LettError Magazine(仅出版一期即包含RandomFont概念), FontFont Library (FontShop)

## L009 九、与前后章关联

**与前章(Kay)**：Kay论证"你必须会写媒介才能有素养"——LettError正是Kay理念的字体设计版实现：不是使用现有字体工具，而是使用PostScript编程来创造新类型的字体。

**与后章(Maeda, Fry/Reas)**：LettError的"编程辅助设计"——设计师设定参数，计算机在界限内随机变化——是Maeda"Design by Numbers"和Fry/Reas Processing中"参数化生成"理念的早期字体设计实践。Beowolf的随机扰动直接预示了Conditional Design(第28章)的"受控涌现"方法论。病毒字体的幽默想象在Faste(第32章)的"后人类"焦虑中获得了严肃的回响——"自传播代码"从玩笑变为可能的现实。
