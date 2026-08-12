# NN_专项报告与实体总索引

---

# 第一部分：专项报告

---

## 专项报告一：全书方法论深度分析

### L### 一、方法论谱系定位

Borchers的《A Pattern Approach to Interaction Design》在方法论上处于一个独特的交叉位置：

```
方法论谱系
├── 实证主义传统 (Positivism)
│   └── 定量评估数据 (Ch.5 §5.4: user survey μ=2.08)
│   └── 教学实验 (Ch.5 §5.6: controlled-ish evaluation)
│
├── 解释学传统 (Hermeneutics)
│   └── Alexander的"Quality Without a Name" ← 不可量化的价值维度
│   └── 模式作为"阐释性框架"而非"算法指令"
│
├── 设计研究传统 (Design Research)
│   └── Research through Design: WorldBeat是"通过设计来研究"的典范
│   └── 模式语言作为设计知识的形式化表达
│
└── 形式主义传统 (Formalism)
    └── PL = (℘, ℜ) ← 图论的严格定义
    └── P = {n, r, i, p, f, e, s, d} ← 集合论的模式定义
```

这种**四重方法论混合**使本书区别于HCI领域的典型学术著作：
- 大多数HCI研究偏向单一方法论——要么是定量的实验研究，要么是定性的设计案例研究
- 大多数模式文献偏向实用主义——提供模式但不提供形式的或评估的严密性
- Borchers的独特在于：**同时使用四种方法论而不让它们相互冲突**

### L### 二、核心方法论概念

#### 1. "通过设计来研究" (Research through Design / RtD)

本书的核心方法论是RtD——不是"先研究再设计"，也不是"先设计再评估研究"，而是"设计行为本身就是研究行为"：
- WorldBeat的系统设计 → 产生了HCI、软件和音乐三套模式语言
- Interactive Fugue的设计 → 验证了模式的可转移性（从Blues到Fugue）
- PET的设计 → 验证了形式模式模型的工具化可行性

RtD在本书中的体现是：**设计产出（系统）和知识产出（模式）是从同一过程中同时涌现的**——设计的每一步都是"这个解决方案可以推广吗？"的追问。

#### 2. "回溯性设计原理" (Post-hoc Design Rationale)

在Ch.3 §3.2.2中，Borchers提出模式是"结构设计原理"（structural/post-hoc design rationale）的理想载体——这与"过程设计原理"（process design rationale，记录设计过程中每个决策的演变）形成对比。

本书自身的方法论实践体现了这一点：模式语言不是从第一原理推导出来的"最优方案"，而是从已经完成的成功项目中**回溯性地提取**的：WorldBeat (1996)先存在，模式 (2001出版)后提取。

#### 3. "形式的二重性" (Duality of Formalism)

Borchers在形式化（$PL = (\wp, \Re)$）和人类可读性（散文格式而非公式）之间建立了一种二元共存：
- 形式的底层：数学定义确保了语义精确，可用于计算机工具
- 文本的表层：散文模式确保了人类可读，可用于跨学科沟通

这种二重性不是折中——它是一种深思熟虑的认识论立场："可操作"（形式化）和"可传播"（文本化）不应相互排斥。

#### 4. "自我指涉性" (Self-Referentiality)

本书在不同层面展现了自我指涉：
- PET工具使用DYNAMIC DESCRIPTOR模式来设计其自己的UI
- 本书自身的论证结构（问题→历史→框架→实例→验证→总结）映射了它所倡导的设计过程（需求→资源→方案→原型→评估→交付）
- 模式语言的层级排列（大→小）映射了本书的章节排列（总览→具体模式）

### L### 三、方法论的优势与局限

**优势**：
1. **系统性的经验捕捉**：比纯粹的"设计指南"更结构化，比纯粹的"案例研究"更可推广
2. **多维度的验证**：Ch.5从七个维度评估，避免了单一方法的偏见
3. **理论与实践的统一**：形式模型和散文模式在同一框架中共存

**局限**：
1. **缺乏对照实验**：没有A/B测试证明"使用模式的设计过程"优于"不使用模式的设计过程"
2. **作者即设计者**：所有系统都是Borchers自己或他的学生设计的——存在"自我验证"的循环风险
3. **样本偏倚**：所有案例都来自"交互式音乐展览"这一狭窄领域——框架在其他领域的通用性尚未证伪

### L### 四、方法论在知识元体系中的位置

在"设计历史与知识元"框架中，本书的方法论提供了：
1. **一种"设计知识形式化"的可操作方法**：10个模式成分 × 跨领域统一格式
2. **一种"设计经验累积"的组织原则**：模式语言的层级展开结构使新经验可以被增量式地添加
3. **一种"跨学科沟通"的媒介模型**：模式作为"lingua franca"——既不偏向任一学科，又可以被所有学科理解

---

## 专项报告二：全书核心价值判断

### L### 一、学术原创性评估

**极高原创性的贡献**：
1. **应用领域模式语言**：将音乐理论表达为设计模式——这是Borchers最独特的原创概念
2. **形式的模式语言数学模型**：$PL = (\wp, \Re)$在HCI模式文献中无先例
3. **时间维度的理论化**：将模式层级排序从Alexander的纯粹"空间大小"扩展为"时空范围"
4. **可用性工程生命周期嵌入**：在Nielsen的11阶段模型中逐阶段展示模式的使用——此前无任何模式集合提供如此详细的"操作手册"

**高度综合性的贡献**：
5. **HCI模式的语言**：17个交互式展览模式——是当时该子领域最完备的模式集合
6. **穷尽性文献综述**：追溯了从Norman(1986)到CHI 2000的完整HCI模式研究史
7. **模式的跨学科统一格式**：将Alexander/Gamma/Tidwell的格式传统整合为统一规范

**具有先见之明的贡献**：
8. **PET工具设计**：2001年提出的基于XML的跨平台模式编辑工具——这种思路与后来的Wiki模式和协作式在线知识库是同一方向

### L### 二、历史影响评估

本书出版后的历史验证了Borchers的判断：
- HCI设计模式确实在2000年代初期"gained momentum"——Tidwell的《Designing Interfaces》(2005)将模式方法带入主流HCI实践；Yahoo! Design Pattern Library (2006)等工业界项目采纳了模式方法；van Welie的Web Design Patterns持续发展
- 交互式展览领域的模式——如ATTRACT-ENGAGE-DELIVER模型——被广泛采纳到博物馆学和公共交互设计领域
- 模式的XML定义思路在后续的Pattern Language Markup Language (PLML)等工作中得到发展

### L### 三、在"设计历史-知识元"中的价值

本书在知识元体系中的节点价值：

1. **作为"桥梁文献"**：连接了建筑模式思想（Alexander, 1970s）→ 软件模式技术（GoF, 1990s）→ HCI模式方法（Borchers et al., 2000s）

2. **作为"实例矿床"**：32个完整的模式（11音乐+17 HCI+4软件）为后续研究提供了可直接引用的高质量模式实例

3. **作为"学科奠基文献"**：在HCI设计模式这一子领域，本书起到了类似GoF在软件模式领域的作用——尽管HCI的多样性使得后续没有出现单一的"权威"模式集合，但本书为该领域提供了理论深度和方法论严格性

4. **作为"方法论模型"**：如何将一个设计实践领域（交互式展览设计）中的隐性知识转化为显性的、可传播的、可教学的形式化知识——这一方法论过程本身是跨领域的

---

## 专项报告三：全书逻辑网络图

### L### 全书的"超文本结构"——论证弧与回环

```
┌──────────────────────────────────────────────────────────┐
│                       全书超文本图                         │
│                                                          │
│    ┌──────┐     ┌──────┐     ┌──────┐                    │
│    │Preface│────▶│Ch.1  │────▶│Ch.2  │                    │
│    │宣告方案│     │问题诊断│     │历史资源│                    │
│    └──────┘     └──────┘     └──┬───┘                    │
│                                 │                         │
│                    六项要求 (§2.6)                          │
│                                 │                         │
│                                 ▼                         │
│                           ┌──────────┐                    │
│                           │  Ch.3    │                    │
│                           │ 理论框架  │                    │
│                           └────┬─────┘                    │
│                                │                          │
│              ┌─────────────────┼─────────────────┐        │
│              ▼                 ▼                 ▼        │
│        ┌──────────┐    ┌──────────┐     ┌──────────┐     │
│        │音乐模式11│    │HCI模式17 │     │软件模式4 │     │
│        │  (§4.1)  │    │  (§4.2)  │     │  (§4.3)  │     │
│        └──────────┘    └──────────┘     └──────────┘     │
│              │                 │                 │        │
│              └─────────────────┼─────────────────┘        │
│                                │                          │
│                                ▼                          │
│                    ┌──────────────────────┐               │
│                    │       Ch.5           │               │
│                    │    七维度评估         │               │
│                    └──────────┬───────────┘               │
│                               │                           │
│                               ▼                           │
│                         ┌──────────┐                      │
│                         │  Ch.6    │                      │
│                         │ 总结展望  │                      │
│                         └──────────┘                      │
│                                                          │
│  论证弧: 宣告 → 诊断 → 历史 → 框架 → 实例 → 验证 → 收束  │
│  回环1: §2.6六项要求 → Ch.3框架 → §5.1对照验证          │
│  回环2: Ch.4 H11 → §5.2同行评审 → 模式改进               │
│  回环3: Ch.4实例 → §5.5重用 → 模式改进                   │
│  回环4: Ch.3形式模型 → §5.8 PET设计 → 工具化             │
└──────────────────────────────────────────────────────────┘
```

---

# 第二部分：全书实体总索引

以下索引汇总了七份分析报告（00_整体分析报告 + 01-06六章分析报告）中的全部L###编码实体，按六种实体类型和L###编号排序。

---

## 一、人物实体索引（按L###编号排序）

| L### | 姓名 | 身份 | 主要出现章节 |
|------|------|------|------------|
| L###001 | Christopher Alexander | 建筑师/模式语言创始人 | Ch.2, Ch.3, Ch.6 |
| L###002 | Erich Gamma / Richard Helm / Ralph Johnson / John Vlissides (GoF) | 软件模式作者 | Ch.2 |
| L###003 | Jenifer Tidwell | HCI模式研究者 | Ch.2, Ch.4 |
| L###004 | Donald A. Norman | 认知科学家/HCI先驱 | Ch.1, Ch.2, Ch.3, Ch.4 |
| L###005 | Jakob Nielsen | 可用性工程专家 | Ch.1, Ch.3, Ch.4 |
| L###006 | Frank Buschmann | Siemens架构师/丛书序作者 | 00, Ch.2 |
| L###007 | Hiroshi Ishii / Brygg Ullmer | MIT Media Lab / Tangible Bits | Ch.4 |
| L###008 | Francesco di Giorgio (1439-1501) | 文艺复兴建筑大师 | Ch.2 |
| L###009 | Kent Beck / Ward Cunningham | OOPSLA 1987软件模式先驱 | Ch.2 |
| L###010 | Tom Erickson | IBM/HCI研究员 | Ch.2 |
| L###101 | Ben Shneiderman | HCI教科书作者 | Ch.1 |
| L###102 | Donald A. Norman (重复) | 见L###004 | — |
| L###103 | Scott Kim | "disciplines are like cultures"概念提出者 | Ch.1 |
| L###104 | Brad A. Myers / Mary Beth Rosson | UI开发投入调查(45%/50%) | Ch.1 |
| L###105 | Robin Jeffries et al. | HCI设计师ROI研究(3-4倍) | Ch.1 |
| L###106 | Jakob Nielsen (重复) | 见L###005 | — |
| L###107 | Thomas K. Landauer | 《The Trouble with Computers》 | Ch.1 |
| L###201 | Christopher Alexander (重复) | 见L###001 | — |
| L###202 | Francesco di Giorgio (重复) | 见L###008 | — |
| L###203 | GoF (重复) | 见L###002 | — |
| L###204 | Kent Beck / Ward Cunningham (重复) | 见L###009 | — |
| L###205 | Jenifer Tidwell (重复) | 见L###003 | — |
| L###206 | Donald A. Norman (重复) | 见L###004 | — |
| L###207 | Lon Barfield et al. | Utrecht交互设计课程改革者 | Ch.2 |
| L###208 | Tom Erickson (重复) | 见L###010 | — |
| L###209 | Elisabeth Bayle et al. | CHI'97 Workshop报告 | Ch.2 |
| L###210 | Åsa Granlund / Daniel Lafrenière | PSA方法创始人 | Ch.2 |
| L###211 | Peter Denning / Pamela Dargan | Pattern Mapping概念 | Ch.2 |
| L###212 | George Casaday | 模式普遍性论证 | Ch.2 |
| L###213 | Martijn van Welie | HCI模式研究者/XML模式格式 | Ch.2, Ch.3, Ch.5 |
| L###214 | Frank Buschmann (重复) | 见L###006 | — |
| L###301 | Jakob Nielsen (重复) | 见L###005 | — |
| L###302 | Christopher Alexander (重复) | 见L###001 | — |
| L###303 | Hermann Hesse | 《玻璃珠游戏》作者 | Ch.3 |
| L###304 | Donald A. Norman (重复) | 见L###004 | — |
| L###305 | Alan Dix et al. | "90% of the value"断言 | Ch.3 |
| L###306 | Martijn van Welie (重复) | 见L###213 | — |
| L###307 | Wolfgang Köhler | Gestalt心理学创始人 | Ch.3 |
| L###308 | George A. Miller | "7±2"规则/Verval Recoding | Ch.3 |
| L###401 | J.W. von Goethe | Faust作者 | Ch.4 |
| L###402 | Louis Armstrong | 爵士音乐家 | Ch.4 |
| L###403 | John Coltrane / Jimmy Garrison | 爵士音乐家 | Ch.4 |
| L###404 | Donald A. Norman (重复) | 见L###004 | — |
| L###405 | Hiroshi Ishii / Brygg Ullmer (重复) | 见L###007 | — |
| L###406 | John Ruskin | 19世纪英国作家 | Ch.2, Ch.4 |
| L###407 | George Gershwin | 作曲家 | Ch.4 |
| L###408 | Ben Shneiderman (重复) | 见L###101 | — |
| L###409 | Jakob Nielsen (重复) | 见L###005 | — |
| L###410 | Bill Hailey | Rock Around The Clock | Ch.4 |
| L###501 | Austin Henderson | Rivendel Consulting / Pattern Reviewer | Ch.5 |
| L###502 | Karri-Pekka Laakso | University of Helsinki / Pattern Reviewer | Ch.5 |
| L###503 | Victor Lombardi | Razorfish / Pattern Reviewer | Ch.5 |
| L###504 | Carol Strohecker | MERL / Pattern Reviewer | Ch.5 |
| L###505 | Yongmei Wu | Darmstadt UT / Pattern Reviewer | Ch.5 |
| L###506 | Max Mühlhäuser | Borchers的导师和合作者 | Ch.5 |
| L###507 | Matthias Dannenberg | Interactive Fugue硕士论文 | Ch.5 |
| L###508 | Martijn van Welie (重复) | 见L###213 | — |
| L###601 | J.W. von Goethe (重复) | 见L###401 | — |
| L###602 | Christopher Alexander (重复) | 见L###001 | — |
| L###603 | Jan Borchers | 本书作者 | Ch.6 |

---

## 二、文献实体索引

| L### | 文献 | 首次出现章节 |
|------|------|------------|
| L###011 | Alexander et al. A Pattern Language (1977) | 00 |
| L###012 | Alexander. The Timeless Way of Building (1979) | 00 |
| L###013 | Gamma et al. Design Patterns (1995) | 00 |
| L###014 | Tidwell. Common Ground / Interaction Design Patterns (1998) | 00 |
| L###015 | Nielsen. Usability Engineering (1993) | 00 |
| L###016 | Norman. The Psychology of Everyday Things (1988) | 00 |
| L###017 | Norman & Draper. User-Centered System Design (1986) | 00 |
| L###018 | Apple Computer. Macintosh HIG (1992) | 00 |
| L###019 | Barfield et al. "Interaction design at the Utrecht School" (1994) | 00 |
| L###020 | Miller. "The Magical Number Seven" (1956) | 00 |
| L###108 | Helander et al. Handbook of HCI (1997) | Ch.1 |
| L###109 | ACM SIGCHI. Curricula for HCI (1992) | Ch.1 |
| L###110 | Shneiderman. Designing the User Interface, 3rd ed. (1998) | Ch.1 |
| L###111 | Tognazzini. TOG on Interface (1992) | Ch.1 |
| L###112 | Myers & Rosson. "Survey on UI programming" (1992) | Ch.1 |
| L###113 | Apple Computer. Macintosh HIG (1992) — 重复 | Ch.1 |
| L###114 | Kim. "Interdisciplinary cooperation" (1990) | Ch.1 |
| L###115 | Norman & Draper (1986) — 重复 | Ch.1 |
| L###116 | Tedeschi. "Good website design" NYT (1999) | Ch.1 |
| L###117 | Muller et al. "Participatory practices" (1997) | Ch.1 |
| L###215 | Alexander et al. A Pattern Language (1977) — 重复 | Ch.2 |
| L###216 | Alexander. The Timeless Way of Building (1979) — 重复 | Ch.2 |
| L###217 | Alexander et al. The Oregon Experiment (1988) | Ch.2 |
| L###218 | Gamma et al. Design Patterns (1995) — 重复 | Ch.2 |
| L###219 | Beck & Cunningham. "Using pattern languages..." (1987) | Ch.2 |
| L###220 | Tidwell. Common Ground (1998) — 重复 | Ch.2 |
| L###221 | Norman & Draper (1986) — 重复 | Ch.2 |
| L###222 | Norman. Psychology of Everyday Things (1988) — 重复 | Ch.2 |
| L###223 | Apple. Macintosh HIG (1992) — 重复 | Ch.2 |
| L###224 | Barfield et al. (1994) — 重复 | Ch.2 |
| L###225 | Bayle et al. "Putting it all together" (1998) | Ch.2 |
| L###226 | Erickson. "Lingua franca for interaction design?" (1998) | Ch.2 |
| L###227 | Borchers. "CHI meets PLoP" (2000a) | Ch.2 |
| L###228 | Borchers et al. INTERACT'99 & CHI 2000 reports (2001) | Ch.2 |
| L###229 | Granlund & Lafrenière. PSA papers (1999a,b) | Ch.2 |
| L###230 | Denning & Dargan. "Action-centered design" (1996) | Ch.2 |
| L###231 | Casaday. "Notes on a pattern language..." (1997) | Ch.2 |
| L###232 | Riehle & Züllighoven. "Tools and Materials" (1995) | Ch.2 |
| L###233 | Bradac & Fletcher. "Form Style Windows" (1998) | Ch.2 |
| L###234 | Rossi et al. Hypermedia navigation patterns (1996, 1997) | Ch.2 |
| L###309 | Nielsen. Usability Engineering (1993) — 重复 | Ch.3 |
| L###310 | Alexander. Timeless Way (1979) — 重复 | Ch.3 |
| L###311 | Alexander et al. Pattern Language (1977) — 重复 | Ch.3 |
| L###312 | Dix et al. HCI, 2nd ed. (1998) | Ch.3 |
| L###313 | Gamma et al. Design Patterns (1995) — 重复 | Ch.3 |
| L###314 | Borchers. "A pattern approach..." DIS 2000 | Ch.3 |
| L###315 | Borchers et al. INTERACT'99 & CHI 2000 reports — 重复 | Ch.3 |
| L###316 | Tidwell. Common Ground (1998) — 重复 | Ch.3 |
| L###317 | Norman. POET (1988) — 重复 | Ch.3 |
| L###318 | Hesse. The Glass Bead Game | Ch.3 |
| L###411 | Alexander et al. Pattern Language (1977) — 重复 | Ch.4 |
| L###412 | Tidwell. Common Ground (1998) — 重复 | Ch.4 |
| L###413 | Norman. POET (1988) — 重复 | Ch.4 |
| L###414 | Ishii & Ullmer. "Tangible Bits" CHI 1997 | Ch.4 |
| L###415 | Underkoffler & Ishii. "Urp" CHI 1999 | Ch.4 |
| L###416 | Miller. "Blues" in Berendt (1978) | Ch.4 |
| L###417 | Binkowski. Musik Um Uns (1988) | Ch.4 |
| L###418 | Akkerman. "Professional keyboard studies" (2000) | Ch.4 |
| L###419 | Borchers. "WorldBeat" CHI 1997 | Ch.4 |
| L###420 | Borchers & Mühlhäuser. IEEE Multimedia 1998 | Ch.4 |
| L###421 | Borchers et al. "Getting it across" 1995 | Ch.4 |
| L###422 | Streitz et al. "i-LAND" CHI 1999 | Ch.4 |
| L###423 | Shneiderman. Designing UI 3rd ed. (1998) — 重复 | Ch.4 |
| L###424 | Lee, Garnett & Wessel. ICMC 1992 | Ch.4 |
| L###425 | Fels et al. "MusiKalscope" ICMCS 1997 | Ch.4 |
| L###509 | Borchers. "WorldBeat" CHI 1997 — 重复 | Ch.5 |
| L###510 | Borchers & Mühlhäuser. IEEE Multimedia 1998 — 重复 | Ch.5 |
| L###511 | Borchers. "CHI meets PLoP" (2000a) — 重复 | Ch.5 |
| L###512 | Borchers et al. CHI 2000 Workshop report | Ch.5 |
| L###513 | Borchers et al. INTERACT'99 Workshop report | Ch.5 |
| L###514 | Tidwell. Common Ground (1998) — 重复 | Ch.5 |
| L###515 | Nielsen. Usability Engineering (1993) — 重复 | Ch.5 |
| L###516 | Dannenberg. "Die Interaktive Fuge" (1999) | Ch.5 |
| L###517 | van Welie. CHI 2000 Workshop position paper | Ch.5 |
| L###518 | Ishii & Ullmer. "Tangible Bits" (1997) — 重复 | Ch.5 |
| L###519 | Underkoffler & Ishii. "Urp" (1999) — 重复 | Ch.5 |
| L###520 | Streitz et al. "i-LAND" (1999) — 重复 | Ch.5 |
| L###521 | Norman. POET (1988) — 重复 | Ch.5 |
| L###522 | Lee, Garnett & Wessel. ICMC 1992 — 重复 | Ch.5 |
| L###523 | Zellweger et al. "Fluid documents" CHI 2000 | Ch.5 |
| L###604 | Borchers. "CHI meets PLoP" (2000a) — 重复 | Ch.6 |
| L###605 | Borchers. DIS 2000 — 重复 | Ch.6 |
| L###606 | Borchers & Mühlhäuser. IEEE Multimedia 1998 — 重复 | Ch.6 |

---

## 三、系统/产品实体索引

| L### | 名称 | 类型 |
|------|------|------|
| L###021 | WorldBeat | 交互式音乐展览 |
| L###022 | Interactive Fugue | 交互式音乐展览 |
| L###023 | Personal Orchestra | 交互式音乐展览 |
| L###024 | Virtual Vienna | VR城市导览 |
| L###025 | PET (Pattern Editing Tool) | 软件工具原型 |
| L###026 | Urp (MIT Media Lab) | 城市规划工作台 |
| L###027 | CAVE (Ars Electronica Center) | VR装置 |
| L###028 | DynaWall / i-LAND | 交互式白板 |
| L###029 | Kai's Power Show | 桌面展示软件 |
| L###030 | Mac OS / Microsoft Windows | 桌面操作系统 |
| L###118 | Microsoft Windows NT | 操作系统 |
| L###119 | IBM website | 网站 |
| L###120 | Macintosh OS | 操作系统 |
| L###235 | Mac OS (Balloon Help, Simple Finder) | 操作系统功能 |
| L###236 | Microsoft Windows (Tool Tips) | 操作系统功能 |
| L###237 | Netscape Navigator | 网络浏览器 |
| L###238 | Exploratorium (San Francisco) | 科学博物馆展览系统 |
| L###239 | Kai's Power Show | 桌面应用 |
| L###319 | WorldBeat | 交互式展览 |
| L###320 | Mac OS | 操作系统 |
| L###321 | PET | 软件工具 |
| L###426 | WorldBeat | 交互式展览 |
| L###427 | Interactive Fugue | 交互式展览 |
| L###428 | Personal Orchestra | 交互式展览 |
| L###429 | Virtual Vienna | VR导览 |
| L###430 | Urp | 城市规划工作台 |
| L###431 | CAVE (AEC) | VR装置 |
| L###432 | DynaWall / i-LAND | 交互式白板 |
| L###433 | Brain Opera (MIT) | 交互式展览 |
| L###434 | Kai's Power Show | 桌面应用 |
| L###435 | Mac OS | 操作系统 |
| L###436 | Microsoft Windows | 操作系统 |
| L###437 | Studio Vision Pro (Opcode) | 数字音频软件 |
| L###438 | MusiKalscope | 音乐交互系统 |
| L###439 | "Fin-Fin" dolphin exhibit (TMD) | 博物馆展品(负面案例) |
| L###440 | Exploratorium | 科学博物馆 |
| L###524 | WorldBeat | 交互式展览 |
| L###525 | Interactive Fugue | 交互式展览 |
| L###526 | Personal Orchestra | 交互式展览 |
| L###527 | Virtual Vienna | VR导览 |
| L###528 | PET | 软件工具原型 |
| L###529 | WorldBeat MDP component | 软件模块 |
| L###530 | Apple Power Macintosh 8500/120 | 计算机 |
| L###531 | Buchla Lightning II | MIDI控制器 |
| L###532 | MAX (Opcode) | 编程环境 |
| L###533 | Urp | 工作台 |
| L###607 | WorldBeat | 交互式展览 |
| L###608 | Personal Orchestra | 交互式展览 |
| L###609 | Interactive Fugue | 交互式展览 |
| L###610 | Virtual Vienna | VR导览 |
| L###611 | PET | 软件工具 |

---

## 四、概念/术语实体索引

| L### | 中文 | 英文原文 | 首次出现章节 |
|------|------|---------|------------|
| L###031 | 模式语言 | Pattern Language | 00 |
| L###032 | 设计模式 | Design Pattern | 00 |
| L###033 | 力 | Forces | 00 |
| L###034 | 无名特质 | Quality Without a Name (QWAN) | 00 |
| L###035 | 跨学科模式框架 | Interdisciplinary Pattern Framework | 00 |
| L###036 | 渐次生长 | Piecemeal Growth | 00 |
| L###037 | 可用性工程生命周期 | Usability Engineering Lifecycle | 00 |
| L###038 | 展开过程 | Unfolding Process | 00 |
| L###039 | 交互式展览 | Interactive Exhibit / Actibit | 00 |
| L###040 | 应用领域模式 | Application Domain Pattern | 00 |
| L###041 | 隐式结构 | Implicit Structuring | 00 |
| L###042 | 反模式 | Anti-Pattern | 00 |
| L###043 | 设计原理 | Design Rationale | 00 |
| L###044 | 交互设计模式定义 | Interaction Design Pattern (ChiliPLoP'99) | 00 |
| L###121 | 人机交互 | Human-Computer Interaction (HCI) | Ch.1 |
| L###122 | 以用户为中心的设计 | User-Centred Design | Ch.1 |
| L###123 | 参与式设计 | Participatory Design | Ch.1 |
| L###124 | 企业记忆 | Corporate Memory | Ch.1 |
| L###125 | 设计指南 | Design Guidelines | Ch.1 |
| L###126 | 设计模式 | Design Pattern | Ch.1 |
| L###127 | 模式语言 | Pattern Language | Ch.1 |
| L###128 | 抽象指南vs具体指南 | Abstract vs Concrete Guidelines | Ch.1 |
| L###129 | 跨学科设计 | Interdisciplinary Design | Ch.1 |
| L###130 | 设计原理 | Design Rationale | Ch.1 |
| L###240 | QWAN | Quality Without a Name | Ch.2 |
| L###241 | 力 | Forces | Ch.2 |
| L###242 | 渐次生长 | Piecemeal Growth | Ch.2 |
| L###243 | 展开过程 | Unfolding Process | Ch.2 |
| L###244 | 隐式结构 | Implicit Structuring | Ch.2 |
| L###245 | 链接性 | Context/Reference Links | Ch.2 |
| L###246 | 交互设计模式 | Interaction Design Pattern | Ch.2 |
| L###247 | 活动模式vs设计模式 | Activity vs Design Pattern | Ch.2 |
| L###248 | 三层分类法 | Abstraction×Function×Physical Dimension | Ch.2 |
| L###249 | 按尺度的分类原则 | Scale-based Organizing Principle | Ch.2 |
| L###250 | 透明度 | Transparency | Ch.2 |
| L###251 | 跨学科可读性 | Cross-discipline Readability | Ch.2 |
| L###252 | 信息模式vs Alexandrian模式 | Information vs Alexandrian Pattern | Ch.2 |
| L###253 | 模式映射 | Pattern Mapping | Ch.2 |
| L###254 | 言语编码 | Verbal Recoding | Ch.2 |
| L###322 | 形式模式语言定义 | Formal PL = (℘, ℜ) | Ch.3 |
| L###323 | 形式模式定义 | Formal P = {n,r,i,p,f,e,s,d} | Ch.3 |
| L###324 | 可用性工程生命周期 | Usability Engineering Lifecycle | Ch.3 |
| L###325 | 时间作为设计维度 | Time as Design Dimension | Ch.3 |
| L###326 | 接力人角色 | Relay Person | Ch.3 |
| L###327 | 对立力量 | Opposing Forces | Ch.3 |
| L###328 | 命名规则 | Pattern Naming Rules | Ch.3 |
| L###329 | 两级评级制 | Two-star Ranking | Ch.3 |
| L###330 | 归纳式写作 | Inductive Style | Ch.3 |
| L###331 | 结构设计原理 | Structural/Post-hoc Design Rationale | Ch.3 |
| L###332 | 过程设计原理 | Process Design Rationale | Ch.3 |
| L###333 | 反模式 | Anti-Patterns | Ch.3 |
| L###334 | 空间+时间排序原则 | Space+Time Ordering | Ch.3 |
| L###335 | 设计过程同构性 | Design Process Isomorphism | Ch.3 |
| L###441 | 吸引-参与-传达 | Attract-Engage-Deliver | Ch.4 |
| L###442 | 吸引空间 | Attraction Space | Ch.4 |
| L###443 | 渐增揭示 | Incremental Revealing | Ch.4 |
| L###444 | 扁平窄树 | Flat and Narrow Tree | Ch.4 |
| L###445 | 闭环 | Closed Loop | Ch.4 |
| L###446 | 增强现实 | Augmented Reality | Ch.4 |
| L###447 | 领域适切设备 | Domain-Appropriate Devices | Ch.4 |
| L###448 | 渐进式帮助 | Dynamic Descriptor | Ch.4 |
| L###449 | 即时信息 | Information Just in Time | Ch.4 |
| L###450 | 隐藏硬件 | Invisible Hardware | Ch.4 |
| L###451 | 单一输入设备 | One Input Device | Ch.4 |
| L###452 | 五声音阶 | Pentatonic Scale | Ch.4 |
| L###453 | 蓝音 | Blue Notes | Ch.4 |
| L###454 | 三连音律动 | Triplet Groove | Ch.4 |
| L###455 | 分支变换器链 | Branching Transformer Chain | Ch.4 |
| L###456 | 节奏变换器 | Metric Transformer | Ch.4 |
| L###457 | 即兴辅助器 | Improvisation Helper | Ch.4 |
| L###458 | 音乐事件 | Musical Events | Ch.4 |
| L###459 | Kiosk四分类 | Information/Advertising/Service/Entertainment | Ch.4 |
| L###460 | 合作体验 | Cooperative Experience | Ch.4 |
| L###534 | Writer's Workshop | 模式同行评审方法 | Ch.5 |
| L###535 | 多点三角测量 | Multi-point Triangulation | Ch.5 |
| L###536 | 超文本模式模型 | Hypertext Pattern Model | Ch.5 |
| L###537 | 模式内容块 | Pattern Content Block | Ch.5 |
| L###538 | 跨平台工具设计 | Cross-platform Tool Design | Ch.5 |
| L###539 | 教学有效性 | Didactic Usefulness | Ch.5 |
| L###540 | 企业记忆 | Corporate Memory | Ch.5 |
| L###541 | 可转移性 | Transferability | Ch.5 |
| L###542 | 通用MIDI | General MIDI | Ch.5 |
| L###543 | 手势识别 | Gesture Recognition | Ch.5 |
| L###612 | 跨学科模式框架 | Interdisciplinary Pattern Framework | Ch.6 |
| L###613 | HCI设计模式 | HCI Design Patterns | Ch.6 |
| L###614 | 应用领域模式语言 | Application Domain Pattern Language | Ch.6 |
| L###615 | 领域无关的形式定义 | Domain-independent Formal Definition | Ch.6 |
| L###616 | 可用性工程生命周期 | Usability Engineering Lifecycle | Ch.6 |
| L###617 | 企业记忆 | Corporate Memory | Ch.6 |
| L###618 | 设计原理 | Design Rationale | Ch.6 |
| L###619 | 无名特质 | QWAN | Ch.6 |
| L###620 | IFIP HCI模式任务组 | IFIP TG for HCI Design Patterns | Ch.6 |
| L###621 | 超文本模式模型 | Hypertext Pattern Model | Ch.6 |

---

## 五、机构/地点实体索引

| L### | 名称 | 类型 |
|------|------|------|
| L###045 | Ars Electronica Center (AEC), Linz | 科技艺术博物馆 |
| L###046 | HOUSE OF MUSIC VIENNA | 音乐博物馆 |
| L###047 | Stanford University | 大学 |
| L###048 | University of Linz | 大学 |
| L###049 | University of Darmstadt / University of Ulm | 大学 |
| L###050 | Techniek Museum Delft | 科技博物馆 |
| L###051 | MIT Media Lab | 研究机构 |
| L###052 | Utrecht School of the Arts | 艺术学院 |
| L###053 | Exploratorium, San Francisco | 科学博物馆 |
| L###054 | IFIP (International Federation for Information Processing) | 国际学术组织 |
| L###131 | ACM SIGCHI | 学术组织 |
| L###132 | Apple Computer | 公司 |
| L###133 | IBM | 公司 |
| L###255 | OOPSLA conference | 学术会议 |
| L###256 | PLoP conference series | 学术会议系列 |
| L###257 | CHI conference | 学术会议 |
| L###258 | INTERACT conference | 学术会议 |
| L###259 | ChiliPLoP conference | 学术会议 |
| L###260 | UPA conference | 行业会议 |
| L###261 | Utrecht School of the Arts | 艺术学院 |
| L###262 | CHI'97 Workshop (Atlanta) | 学术研讨会 |
| L###263 | ChiliPLoP'99 Workshop (Wickenburg, AZ) | 学术研讨会 |
| L###264 | INTERACT'99 Workshop (Edinburgh) | 学术研讨会 |
| L###265 | CHI 2000 Workshop (The Hague) | 学术研讨会 |
| L###461 | Ars Electronica Center, Linz | 博物馆 |
| L###462 | HOUSE OF MUSIC VIENNA | 博物馆 |
| L###463 | MIT Media Lab | 研究机构 |
| L###464 | Techniek Museum Delft | 博物馆 |
| L###465 | Exploratorium, San Francisco | 博物馆 |
| L###466 | GMD-IPSI | 研究机构 |
| L###467 | Vienna Philharmonic Orchestra | 艺术团体 |
| L###544 | Ars Electronica Center, Linz | 博物馆 |
| L###545 | HOUSE OF MUSIC VIENNA | 博物馆 |
| L###546 | Techniek Museum Delft | 博物馆 |
| L###547 | University of Linz | 大学 |
| L###548 | University of Ulm | 大学 |
| L###549 | University of Darmstadt | 大学 |
| L###550 | MIT Media Lab | 研究机构 |
| L###551 | IFIP | 学术组织 |
| L###622 | IFIP (TG for HCI Design Patterns) | 学术组织 |
| L###623 | British HCI Group | 学术组织 |
| L###624 | Stanford University | 大学 |

---

## 六、技术/硬件实体索引

| L### | 名称 | 类型 |
|------|------|------|
| L###055 | Buchla Lightning II | 红外线MIDI控制器 |
| L###056 | MIDI (Musical Instruments Digital Interface) | 数字音乐协议 |
| L###057 | MAX (Opcode Inc.) | 多媒体编程环境 |
| L###058 | NaviPad | 定制3D控制器 |
| L###059 | Apple Power Macintosh 8500/120 | 计算机硬件 |
| L###060 | Roland pitch-to-MIDI converter | 音频-MIDI转换器 |
| L###061 | General MIDI (GM) Sound Module | 音源标准 |
| L###062 | XML / Java (for PET) | 标记语言+编程语言 |
| L###063 | VR Head-Mounted Display (HMD) | VR头戴显示器(反例) |
| L###134 | World-Wide Web | 网络 |
| L###135 | E-commerce platforms | 电商平台 |
| L###136 | Public information terminals (kiosks) | 公共信息终端 |
| L###266 | C++ | 编程语言 |
| L###267 | UML | 建模语言 |
| L###268 | Smalltalk | 编程语言 |
| L###336 | UML | 建模语言 |
| L###337 | MIDI | 数字音乐协议 |
| L###338 | XML | 标记语言 |
| L###468 | Buchla Lightning II | 红外线MIDI控制器 |
| L###469 | MIDI protocol | 数字音乐协议 |
| L###470 | MAX (Opcode) | 编程环境 |
| L###471 | NaviPad | 定制3D控制器 |
| L###472 | Roland pitch-to-MIDI converter | 音频转换器 |
| L###473 | Apple Power Macintosh 8500/120 | 计算机 |
| L###474 | General MIDI (GM) | 音源标准 |
| L###475 | VR HMD | VR头戴显示器(反例) |
| L###552 | MIDI | 数字音乐协议 |
| L###553 | XML | 标记语言 |
| L###554 | Java Applet | 编程技术 |
| L###555 | General MIDI (GM) | 音源标准 |
| L###556 | Roland pitch-to-MIDI converter | 音频转换器 |
| L###557 | URL-based pattern addressing | 寻址机制 |

---

# 第三部分：报告文件清单

| 文件名 | 对应内容 | 页数估算 |
|--------|---------|---------|
| 00_整体分析报告.md | 全书总体分析 | ~30页 |
| 01_第一章_Introduction_分析报告.md | Ch.1 (pp.1-7) | ~25页 |
| 02_第二章_Design_Pattern_Languages_分析报告.md | Ch.2 (pp.9-49) | ~40页 |
| 03_第三章_An_Interdisciplinary_Pattern_Framework_分析报告.md | Ch.3 (pp.51-73) | ~35页 |
| 04_第四章_A_Pattern_Language_for_Interactive_Music_Exhibits_分析报告.md | Ch.4 (pp.75-168) | ~45页 |
| 05_第五章_Evaluation_and_Tool_Support_分析报告.md | Ch.5 (pp.169-201) | ~35页 |
| 06_第六章_Summary_and_Further_Research_分析报告.md | Ch.6 (pp.203-208) | ~20页 |
| NN_专项报告与实体总索引.md | 专项报告+全书实体索引 | ~40页 |

所有报告均以中文撰写，均标记L###编码，均遵循九节结构（00和NN另有特殊结构）。

---

*本索引根据七份分析报告中的全部L###实体汇总编制。每份分析报告内有该章节专属的实体清单，本索引为全书的统一检索入口。*
