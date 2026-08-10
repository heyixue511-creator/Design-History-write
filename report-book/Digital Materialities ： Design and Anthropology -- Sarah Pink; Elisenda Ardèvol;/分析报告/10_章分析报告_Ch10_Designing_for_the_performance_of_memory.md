# 10_章分析报告：Designing for the performance of memory

**作者**：David Carlin
**位置**：Chapter 10，Part Three（Insider Design）
**源文行号**：L1296-L1445

---

## 一、章节定位与功能

本章以Circus Oz（澳大利亚当代马戏团）数字"活档案"（Living Archive）的设计与开发为中心，从作者作为作家/艺术家/马戏团内部人士的独特位置出发，探讨数字档案如何成为"记忆展演的平台"（platform for the performance of memory）。Carlin将Ingold的现象学人类学（"wayfaring"、"storytelling vs classification"）转化为数字档案设计的实践原则，论证数字档案的物质性可以成为一种"关怀的伦理"（ethics of care）的载体。本章在Part Three中与Ch9和Ch11构成"非设计师的内部设计"谱系——Carlin的位置既不同于专业设计者也不同于外部研究者，而是三十年来与马戏团共同生长的"内部人士"。

## 二、结构分析

| 节段 | 起始行 | 核心内容 |
|------|--------|----------|
| Introduction: A Living Archive for a circus | L1300-L1318 | 个人位置：三十年的马戏团关系、"ethics of care"方法论 |
| A knot of stories | L1320-L1334 | Ingold的理论：wayfaring vs classification、storytelling vs taxonomy |
| The performance event and its recording | L1336-L1350 | 第一类事件：performance event——马戏演出及其视频录制的物质性 |
| The memory event (1): Digitizing, Kim and her notes | L1352-L1364 | 第二类事件：digitization as memory event——Kim Baston的注释 |
| The memory event (2): The Barrel of Memories | L1366-L1388 | 社区记忆事件：2011年Spiegeltent的"幸运记忆桶"活动 |
| Designing for the online memory event | L1390-L1421 | 在线平台设计：clip结构、generous interface、用户故事 |
| The performance of memory event | L1423-L1436 | 第三类事件：Memory Booth——表演者观看自己过去表演的影像 |
| Conclusion | L1438-L1440 | 重返Ingold：数字档案如何enable storytelling而非仅仅classification |

## 三、内容分析

### 核心论题
传统的档案是"分类与存储"的场所——"nothing happens to this stuff, in the Archive...It just sits there until it is read, and used, and narrativised"（Steedman 1998, L1334）。数字档案提供了将分类转化为**讲故事**（storytelling）的可能性——将档案变为"the past as present"（Assmann 2008）的**动态、展演性**场所。Carlin提出了一个三层递归的记忆展演框架：performance event（原始表演）→ memory event（与档案记录的遭遇——如Kim的注释、Spiegeltent活动）→ performance of memory event（对memory events的再展演——如Memory Booth）。

### 关键论点与案例

**论点1: "wayfaring"的知识——反对分类，主张故事**
- Ingold (2011): "things do not so much exist as occur...these things are not classified like facts, or tabulated like data, but narrated like stories"（L1328）。
- Ingold的"alongly integrated knowledge of the wayfarer"（L1330）——知识不是垂直分类的也不是水平网络化的，而是"沿路"的。
- Carlin的应用：数字档案的设计应该不是"组织数据"而是"enable storytelling"。

**论点2: 视频记录的"非-人类讲故事者"（nonhuman storyteller）**
- 视频记录既是"forensic value as documentary evidence"，也是"mnemonic prompts"（L1348）。
- 关键张力：距离效应（"this is not the same as the live performance I experienced"）与识别效应（"drawing the viewer into examining their surfaces"）之间的张力——正是这种张力赋予视频记录以"memory-work"的潜能（L1348）。
- "video recordings of performances are nonhuman storytellers, bringing the past to life as if it were going on here and now – and yet clearly inflected with an idiosyncratic and nonhuman (machinic) bias in the telling"（L1350）。

**论点3: 数字化作为"记忆事件"——Kim的注释**
- 关键决策：雇用Kim Baston——不是技术员而是"circus scholar, circus musician and longtime Circus Oz fan"——来操作数字化过程（L1359）。
- 数字化实验室被设置在音乐排练室旁边的小房间——"a door onto the courtyard where company members leave their bicycles"（L1360）——空间位置的"非隔离性"是关键。
- 马戏团成员逐渐"drop by to check out what she was up to"——非正式的观看与评论——"began to embed the reality of the nascent 'living archive' process within...the daily practice of the company"（L1360）。
- Kim的Notes成为档案本身的一部分：注释被整合入在线活档案——"Wayne electrocuted. Musical number. ---- 2 Poles erected. Swirly electronic music, audience clapping along..."（L1362）——一个既是技术记录又是个人回应的"textual memory event"。

**论点4: Barrel of Memories——社区记忆事件的"展演性"**
- 2011年在Circus Oz的Melba Spiegeltent举办的社区活动。
- "Lucky Barrel of Memories Dip"——从桶中抽取乒乓球，每个标有一个马戏节目→在大屏幕上播放对应的新近数字化的视频片段——仿佛奇迹般从"尚未建成的活档案"中召唤出来（L1370-L1371）。
- 分组观看、scrubbing through录像——"new performers discovered the former feats of their older, now-retired colleagues...children watched the younger incarnations of their parents performing for the first time"（L1374-L1384）。
- Gibson (2013): "'record' (re-cord) comes from the same root as cardiac and the French coeur. 'A record well stored and well retrieved...can bring life in its connection to the larger body of present knowledge'"（L1388）。

**论点5: "慷慨的界面"（generous interface）——促进serendipity**
- 受Whitelaw (2012)启发：不提供"搜索框→结果列表"的传统档案界面，而是设计"visualized the video data in patterns"的界面——如按时间分布的展示、按节目类型的网格（L1404-L1405）。
- "These generous interfaces were designed to instantiate new forms of procedural, computational storytelling arising from database structures"（L1404-L1405）。
- 用户被邀请**不留下"评论"而是留下"故事"**——两个提示语："I was there and..." 或 "I wasn't there but..." ——"user stories and videos alike are all different types of story"（L1408-L1409）。

**论点6: Memory Booth——记忆展演事件的"二度递归"**
- 23位前/现任表演者被邀请至RMIT电视演播室→每人为他们各自选择了三段来自活档案的视频→通过提词器观看→同时被拍摄面部反应和声音回应。
- 一位表演者认出了她在某场演出中"a piece of equipment had broken and she had fallen and broken her neck"的精确时刻（L1431）。
- 一位创始成员回忆起早期没有导演时表演者如何"had to develop the skill of seeing their own performance from the outside"（L1431）。
- 展览形式：分屏——一边是活档案的表演视频，一边是表演者**观看和回应该视频**的面孔——"The exhibition attendee is invited to put on headphones so as to be privy to the intimacy of the Memory Booth"（L1432-L1436）。

## 四、逻辑梳理

### 论证链条
**位置定位** → 我不是人类学家也不是设计师——我是作家/艺术家/马戏团内部人士 → **问题重框** → Ingold: 分类vs讲故事——数字档案如何enable 讲故事？ → **三层事件模型** → 1) performance event(原始演出及其视频记录的物质性) → 2) memory event(遭遇档案记录的两个面向：Kim的数字化注释 + Barrel of Memories社区活动) → 3) performance of memory event(Memory Booth的递归展演) → **设计原则外化** → clip结构(transclusion) + generous interface + "stories"而不是"comments" → **回归Ingold** → 数字档案成为"knot of stories"

### 关键因果转折
- 转折1: 传统档案"分类与沉默"→数字档案的"fluid, processual, dynamic"（Featherstone 2006）→使"档案本身成为a knot of stories"成为可能。
- 转折2: 数字化＝乏味的技术劳动→雇用Kim Baston(musician/scholar/fan)将数字化重定义为"记忆事件"——劳动的性质被重新配置。
- 转折3: Barrel of Memories→"再-cord"（bring back to the heart）→社区活动的情感强度验证了视频作为"storytelling devices"的力量。
- 转折4: 在线用户故事的"令人失望"的低参与→Memory Booth作为补偿性的"强记忆事件"——将记忆的展演从分布式线上走向了集中的艺术制作。

## 五、材料使用方式

1. **个人轨迹作为"方法论的内部性"** ：“I have had some association with this circus...for over thirty years, first as a teenage fan, then as a member of their complex and messy extended family...later as a show director, writer and videographer”（L1304-L1306）——这不是"偏见"而是"方法的优势"。
2. **三层事件框架作为叙事组织**：performance/memory/performance of memory——框架是"a designer would a sketch, as a shorthand for thinking"（L1338）。
3. **Ingold的理论作为"设计实践的启发式"** ：不是将Ingold作为"引用权威"来使用，而是将他作为"what kind of archive does a circus want and need?"的设计问题的对话伙伴。
4. **"Kim's Notes"作为档案本体的一部分**：数字化笔记不是"关于"档案的元数据——它**就是档案的一部分**——"Kim's digitizing commentary...has been incorporated into the online Living Archive"（L1364）。
5. **设计决策的透明展示**：clip结构、transclusion、granularity、"act"作为基本单位——展示了设计中的多次选择与被放弃的替代方案。

## 六、论辩与阐述方法

1. **"非学科"的位置作为认识论优势**：Carlin明确声明"neither as an anthropologist nor as a designer"（L1302）——这使他能够在两种学科语言之间自由移动而不受任何一方方法正统的约束。
2. **"ethics of care"作为方法论承诺**：不是"objective detachment"，而是"implicates the observer so that he/she/I cannot maintain a fantasy of detachment"（L1302）。
3. **概念的可视化**：三层事件模型、clip结构、"generous interface"的可视化——将抽象概念化为可想象的空间/时间/界面形式。
4. **从理论到设计的"翻译"展示**：Ingold的"alongly integrated knowledge"→ clip结构（transclusion）+ generous interface（procedural storytelling）+ "stories"（not "comments"）。
5. **词源学作为诗意论证**："platform"、"record"（re-cord = coeur）、"promise"（putting forward）——这些词源学探索不是装饰性的，而是提供了概念发育的种子。

## 七、语言文风

### 原文摘录

**L001 Ingold的wayfaring**
> "For inhabitants, things do not so much exist as occur. Lying at the confluence of actions and responses they are identified not by their intrinsic attributes but by the memories they call up."（L1328）

**L002 视频作为非人讲故事者**
> "video recordings of performances are nonhuman storytellers, bringing the past to life as if it were going on here and now – and yet clearly inflected with an idiosyncratic and nonhuman (in this instance, machinic) bias in the telling"（L1350）

**L003 Re-cord = bring back to the heart**
> "To 'record', Ross Gibson tells us, means to 'bring back to the heart'...'A record well stored and well retrieved...can bring life in its connection to the larger body of present knowledge'"（L1388）

**L004 Memory Booth的递归性**
> "it is memory performed here, memory as a dynamic and complexly mediated flow of stories connecting past, present and future"（L1436）

**L005 档案作为故事**
> "the new digital archive, instead of being fixed and closed to all but the initiated, is...'fluid, processual, dynamic'"（L1333）

**L006 Kim的注释**
> "Wayne electrocuted. Musical number .---- 2 Poles erected. Swirly electronic music, audience clapping along. 10 performers up poles. ----------Missed a bit due to phone call and now I'm completely mystified. Torch song parody."（L1362）

### 文风特征
- 文学性的写作——与全书其他章节的学术写作形成鲜明对比
- 第一人称叙事贯穿全章，且保持高度的"存在感"和"自我质疑"
- 大量使用破折号和插入语——
- 理论引用（Ingold, Barthes, Deleuze & Guattari）与马戏团轶事（"Wayne electrocuted"）并存，不觉得违和
- 对"物"的描写充满感官细节（"the fluttering death-throes of a moth on Virginia Woolf's desk"）——艺术写作者的感性

## 八、实体清单

### L008 人物实体（≥3）
| 编号 | 姓名 | 身份 | 在章中角色 |
|------|------|------|------------|
| P001 | David Carlin | 作家/艺术家/学者 | 作者——三十年来与Circus Oz的多重关系 |
| P002 | Kim Baston | 马戏团学者/音乐家 | 数字化过程的核心人物——"Kim's Notes"的作者 |
| P003 | Tim Ingold | 人类学家 | "wayfaring"/"storytelling vs classification"理论来源 |
| P004 | Tim Coldwell | Circus Oz成员 | Barrel of Memories活动的主持人 |
| P005 | Reuben Stanton | 设计研究者/博士生 | 活档案界面的设计师 |
| P006 | Lukman Iwan | 设计研究者/博士生 | 活档案原型开发 |
| P007 | Ross Gibson | 艺术家/学者 | "re-cord" = coeur的词源学 |
| P008 | Caroline Steedman | 历史学者 | "档案中的沉默"的经典表述 |
| P009 | Mike Featherstone | 社会学家 | 数字档案的"fluid, processual, dynamic"论述 |
| P010 | Mitchell Whitelaw | 数字人文 | "generous interface"概念 |

### L009 著作实体（≥3）
| 编号 | 著作 | 作者 | 年份 | 在章中角色 |
|------|------|------|------|------------|
| B001 | Being Alive: Essays on Movement, Knowledge and Description | Tim Ingold | 2011 | 核心理论框架（wayfaring, storytelling, knot of stories） |
| B002 | Performing Digital: Multiple Perspectives on a Living Archive | Carlin & Vaughan (eds.) | 2015 | 全章的基础——与本书同期的编辑卷 |
| B003 | The Archive and the Repertoire | Diana Taylor | 2003 | archive/repertoire区分 |
| B004 | Camera Lucida | Roland Barthes | 1981 | punctum概念 |
| B005 | A Thousand Plateaus | Deleuze & Guattari | 1980/2004 | "lines of flight"概念 |

### L010 概念实体（≥3）
| 编号 | 概念 | 出处 | 含义 |
|------|------|------|------|
| C001 | Living Archive | Circus Oz project team | 不是存储过去的仓库，而是参与当下文化生产的动态数字平台 |
| C002 | platform for the performance of memory | Carlin | 将过去/记忆/经验的复杂多线程交织展演出来的动态暂存场地 |
| C003 | wayfaring | Ingold | 人类通过在生活世界中的"沿路行走"而获得知识——反对classification |
| C004 | generous interface | Whitelaw | 不是"搜索→结果"的模型，而是可视化数据模式以促进serendipitous discovery |
| C005 | transclusion | Ted Nelson | 通过引用而非复制将数字内容纳入另一个上下文 |
| C006 | performance event / memory event / performance of memory event | Carlin | 三层递归事件模型——记忆展演平台的结构基础 |
| C007 | punctum | Barthes | 摄影中"刺穿/伤害"观看者的某个细节——Carlin将此转化为"ethics of care"的方法论 |

### L011 机构/地点实体（≥3）
| 编号 | 名称 | 类型 | 在章中角色 |
|------|------|------|------------|
| I001 | Circus Oz | 表演艺术公司 | 全章的核心对象——澳大利亚当代马戏团 |
| I002 | RMIT University | 大学 | 项目主持机构——Memory Booth的电视演播室所在地 |
| I003 | Melba Spiegeltent (Melbourne) | 表演/活动场地 | Barrel of Memories社区活动举办地 |
| I004 | AusStage consortium | 学术联盟 | 提供了移动数字化实验室 |
| I005 | Paper Giant (design research company) | 设计公司 | Vault展览的合作制作方 |

### L012 技术/物质实体（≥3）
| 编号 | 名称 | 类型 | 在章中角色 |
|------|------|------|------------|
| T001 | SAMMA video digitization machines | 数字化设备 | 移动实验室的核心硬件 |
| T002 | Circus Oz Living Archive (archive.circusoz.com) | 数字平台 | 全章的设计对象——在线"活档案" |
| T003 | Memory Booth (TV studio + teleprompter) | 录像装置 | 记忆展演事件的"二度递归"技术设置 |
| T004 | Vault: the nonstop performing history of Circus Oz | 展览 | 2014 Melbourne Festival中的展览——Memory Booth视频的展出空间 |
| T005 | 2,000+ hours of performance video | 档案资料 | 跨越37年的演出录像收藏 |

### L013 事件实体（≥3）
| 编号 | 名称 | 时间 | 在章中角色 |
|------|------|------|------------|
| E001 | Circus Oz founding | 1978 | 马戏团创立——档案的起始点 |
| E002 | Barrel of Memories community event at Spiegeltent | 2011.5 | 社区记忆事件——"幸运记忆桶" |
| E003 | Memory Booth filming sessions (RMIT TV studio) | 2014.6 | 23位表演者的记忆展演事件 |
| E004 | Vault exhibition at Melbourne Festival | 2014.10 | Memory Booth视频的公开展出 |
| E005 | Living Archive "soft launch" | 2013 | 在线平台首次公开上线 |

## 九、与前后章关联

- **与Ch1**：Ch1提出"digital materiality as process, as emergent"——Ch10的"活档案"就是这一概念的完整展演——档案不是一个完成的"产品"，而是一个不断展演中的过程（ongoing circulation of stories）。Ch1强调"getting into the middle of it"——Carlin的三十年内部关系就是"在中间"的最极致体现。
- **与Ch5(Pink et al.)**：Ch5的民族志-设计合作跨越四年——Ch10的活档案设计跨越六年——两者共享长期项目的时间性反思。Ch5的"氛围"概念——Ch10的"record=coeur"和记忆事件的"情感强度"——对"感官/情感"的共同关注。
- **与Ch6(Michael)**：Ch6讨论"record"的词源（re-cord = bring back to the heart）——这一概念也在Ch10中通过Gibson的引用被独立激活。Ch6的"事件"概念（Whitehead/Stengers）——Ch10的"performance/memory/performance of memory"三层事件递归模型。
- **与Ch9(Horst)**：Ch9讨论个人如何通过审美实践在长期生活史中保持连续性——Ch10讨论组织如何通过数字档案在长期历史中保持记忆的连续性与生成性——时间性是两章的共同核心维度。
- **与Ch11(McShane et al.)**：Ch10展示了"内部人士"如何领导对自身组织的数字干预——Ch11展示了"公民活动家"如何发起对自身城镇的数字干预——从文化组织（Ch10）到地区基础设施（Ch11）的"insider intervention"谱系。

---
*报告生成日期：2026-08-04*
