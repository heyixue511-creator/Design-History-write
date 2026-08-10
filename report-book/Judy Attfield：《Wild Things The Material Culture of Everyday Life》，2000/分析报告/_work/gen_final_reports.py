# -*- coding: utf-8 -*-
"""Generate 00_Overall Report and NN_Special Reports & Entity Index"""
import os

OUT = 'F:/Design-history-知识元/report/Judy Attfield：《Wild Things The Material Culture of Everyday Life》，2000/分析报告'
os.makedirs(OUT, exist_ok=True)

def write_report(filename, content):
    path = os.path.join(OUT, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Written: {path}')

# =============================================================================
# 00_整体分析报告
# =============================================================================
def gen_overall():
    report = """# Judy Attfield《Wild Things: The Material Culture of Everyday Life》(2000) 整体分析报告

**全书信息**
- 作者：Judy Attfield (1937-2006)
- 初版：2000年（Berg Publishers）
- 再版：2020年（Bloomsbury Visual Arts，含Claudia Marina 2020版前言及Jo Turney后记）
- 丛书：Radical Thinkers in Design
- 全书结构：Introduction + 3 Parts (9 Chapters) + Conclusion + Afterword + Bibliography + Index
- 总规模：约550,000字符 / 约685条引用
- 插图：19幅

---

## 一、全书定位与核心贡献

### 1.1 学科定位

《Wild Things》是20世纪末物质文化研究（Material Culture Studies）与设计史（Design History）交汇的里程碑式著作。它既是一部设计史的方法论宣言，也是一部日常物质文化的理论专著，更是一部对现代性条件下人与物关系的深刻哲学反思。

在学科版图上，该书占据了三个"之间"的位置：
- **设计史与人类学之间**：借用Appadurai、Miller等人类学家的理论工具来分析设计物
- **生产研究与消费研究之间**：拒绝生产/消费的二分法，关注物在全部"社会生命"中的意义流动
- **学术分析与日常经验之间**：始终保持理论话语与日常生活经验的可通达性

### 1.2 核心贡献

**L000.1.2.1 概念贡献**：Attfield创造了一系列具有持久影响力的分析概念：
- "有态度的物"（things with attitude）：重新定义设计
- "小写设计"（design in the lower case）：日常的非专业设计实践
- "反设计"（undesign）：未经专业设计过程的日常物品
- "投机建造商的本土风格"（spec builder's vernacular）：无名的建筑风格
- "合理的家具"（reasonable furniture）：复制品的一种特殊本真性
- "织理性"（textility）：从"文本性"转向织物物质性的理论概念

**L000.1.2.2 方法论贡献**：
- 建立了"后学科"（post-disciplinary）的跨学科研究范式
- 为案例研究（case study）方法提供了系统的理论辩护
- 展示了如何将微观物质分析（如梳妆台台面）与宏观社会诊断（如郊区化、现代化进程）相连接
- 开创了"从物出发"（thing-centred）而非"从文本出发"的研究路径

**L000.1.2.3 政治贡献**：
- 挑战了现代主义"好设计/坏设计"的精英主义二分法
- 为日常物质实践（DIY、复制品消费、郊区生活）提供了文化合法性
- 揭示了"品味"论述中隐含的阶级和性别政治
- 将消费者重新定义为创造性的"使用者/制作者"而非被动的"接受者"

---

## 二、全书结构分析

### 2.1 宏观结构：三部曲+框架

```
Front Matter (Preface + 2020 Preface)
    ↓
Introduction: The material culture of everyday life
    ↓
Part I: THINGS (概念奠基)
    Ch1: The meaning of design — Things with attitude
    Ch2: The meaning of things — Design in the lower case
    Ch3: Things and the dynamics of social change
    ↓
Part II: THEMES (主题展开)
    Ch4: Continuity — Authenticity and reproduction
    Ch5: Change — The ephemeral materiality of identity
    Ch6: Containment — The ecology of personal possessions
    ↓
Part III: CONTEXTS (语境整合)
    Ch7: Space — Where things take place
    Ch8: Time — Bringing things to life
    Ch9: The body — The threshold between nature and culture
    ↓
Conclusion + Afterword (Jo Turney)
```

### 2.2 结构逻辑

全书呈现了精密的四层递进结构：

**第一层（Part I）：概念奠基**——"设计是什么？物是什么？物如何在社会中运作？"
**第二层（Part II）：主题展开**——三个核心动力学（本真性/短暂性/容纳）的个案深描
**第三层（Part III）：语境整合**——将主题置于空间、时间、身体三个基础语境中
**第四层（Conclusion/Afterword）**：反思与展望

每一层内部也遵循精密的对称结构：
- Part I：设计（Ch1）→ 物（Ch2）→ 社会变迁（Ch3）[从主体到客体到动力学]
- Part II：持续性（Ch4）→ 变化（Ch5）→ 容纳（Ch6）[时间性对子→空间性综合]
- Part III：空间（Ch7）→ 时间（Ch8）→ 身体（Ch9）[从宏观到微观的语境收束]

### 2.3 章节规模与引用密度

| 章节 | 字符数 | 引用数 | 节段数 | 特点 |
|------|--------|--------|--------|------|
| Introduction | 16,341 | 10 | — | 方法论宣言 |
| Ch1 | 68,275 | 87 | 5 | 学科史+概念重构 |
| Ch2 | 53,697 | 88 | 4 | 日常物的理论化 |
| Ch3 | 44,705 | 56 | 6 | 三大主题预告（最短但密度最高） |
| Ch4 | 47,303 | 56 | 7 | 家具行业的深度案例 |
| Ch5 | 61,831 | 69 | 6 | 精神分析+情感维度 |
| Ch6 | 45,759 | 55 | 7 | 梳妆台的微观研究 |
| Ch7 | 66,159 | 96 | 6 | 引用最密集（空间） |
| Ch8 | 47,185 | 64 | 5 | 哲学密度最高（时间） |
| Ch9 | 47,476 | 65 | 6 | 终章，从具身到离身 |

---

## 三、全书核心论题体系

### 3.1 第一级论题：物与人

全书最根本的理论命题是：物不是社会关系的被动"反映"或"表征"，而是社会关系的"物理表达"（physical articulation）和"积极中介"（active mediator）。物在"做"（doing）事物，而不仅仅是"意味"（meaning）事物。

### 3.2 第二级论题：设计与日常

设计不是专业设计师的专属活动，而是贯穿整个人类物质实践的普遍过程。专业设计（"大写设计"）只是这种普遍过程的一小部分——被命名、被记录、被博物馆收藏的那一小部分。占物质文化绝大多数的"小写设计"（日常的、无名的、不被记录的）才构成了人类生活世界的物质基础。

### 3.3 第三级论题：现代性与物

在现代性条件下，物与人的关系发生了三重转变：
1. **从附着到流通**：物不再是固定的家传之物，而是在市场中不断流转的商品
2. **从持久到短暂**：时尚、更新、废弃——短暂性成为物的常态而非例外
3. **从具身到离身**：身体与物的亲密关系日益被功能性使用关系所取代

### 3.4 第四级论题：身份与物质化

身份（identity）不是一个纯粹心理或社会的过程，而是需要通过物来"物质化"（materialize）的。不同类别的物以不同的方式参与身份建构：
- 家具复制品→通过"连续的传统"建构身份
- 时尚服饰→通过"持续的变化"建构身份
- 个人梳妆台→通过"容纳与排列"建构身份
- 郊区住宅→通过"空间的改造与个性化"建构身份

---

## 四、全书论证方法体系

### 4.1 跨学科理论拼贴

Attfield的理论资源跨越了至少七个学科领域：
- **设计史**：Adrian Forty, Marcia Pointon
- **人类学**：Arjun Appadurai, Daniel Miller, Brian Spooner
- **社会学**：Anthony Giddens, Georg Simmel, Pierre Bourdieu, David Harvey
- **精神分析**：Donald Winnicott, Jay Greenberg
- **哲学**：Martin Heidegger, Henri Lefebvre, Roland Barthes, Bruno Latour
- **文化研究**：Dick Hebdige, Raymond Williams
- **女性主义**：Carolyn Steedman, Juliet Ash, Beverley Gordon

### 4.2 案例驱动的理论建构

全书使用的主要案例：
| 章节 | 核心案例 | 案例时间跨度 | 分析方法 |
|------|----------|-------------|---------|
| Ch1 | V&A博物馆命名史 | 1851-1909 | 制度谱系学 |
| Ch2 | Kaffe Fassett编织+Brinton地毯 | 1981-82 | 设计/手工艺边界分析 |
| Ch4 | J. Clarke & Sons家具公司 | 20世纪（三代） | 行业微观史 |
| Ch5 | Pat Kirkham母亲的外套 | 个人记忆 | 情感现象学 |
| Ch6 | Mrs Winter的梳妆台（1951购入） | 1951-1986 | 物质文化厚描 |
| Ch7 | Cockfosters郊区化 | 1933-1982 | 空间社会史 |
| Ch8 | 遗产博物馆+"新古物主义" | 20世纪末 | 文化诊断 |

### 4.3 概念翻转为核心的修辞策略

Attfield最青睐的论证方法是"概念翻转"——将一个既有概念的常识含义翻转过来：
- "复制品"不是"假货"，而是"诚实的本真性"的承载者
- "短暂性"不是缺陷，而是现代身份建构的条件
- "日常"不是平庸，而是文化的根基
- "杂物"（clutter）不是混乱，而是个人生态系统的丰富性
- "郊区"不是庸俗，而是另一种现代性

---

## 五、全书逻辑线索图

```
起点：设计史学科的局限性
  ↓
翻转：设计→物质文化中的"物"
  ↓
扩展：设计师→所有日常使用者
  ↓
主题化：物如何承载意义？
  ├─ 本真性（通过持久/复制）
  ├─ 短暂性（通过变化/时尚）
  └─ 容纳（通过收集/排列）
  ↓
语境化：这些意义在什么条件中运作？
  ├─ 空间（从梳妆台到郊区）
  ├─ 时间（从记忆到遗产）
  └─ 身体（从具身到离身）
  ↓
终点：在"离身"的数字时代，人与物的关系将何去何从？
```

---

## 六、全书学术谱系与对话关系

### 6.1 继承与发展

- **从Appadurai继承**："物的社会生命"和"价值体制"概念，但将其从人类学"礼物交换"语境扩展到现代消费社会
- **从Winnicott继承**："过渡性客体"概念，但将其从儿童发展心理学扩展到成人物质文化实践
- **从Lefebvre继承**："日常生活的批判"议程，但将其从法兰克福学派的批判传统重新定向为物质文化的分析框架

### 6.2 批判与超越

- **批判"好设计"传统**（Pevsner, Read等）：以"好设计/坏设计"二分法筛选研究对象的做法是精英主义的，忽视了使用者的能动性
- **批判法兰克福学派**（Adorno, Horkheimer）：将消费等同于"被动接受"的理论简化了人与物的复杂关系
- **批判Bourdieu式的品味社会学**：将"日常"等同于"低品味"是对日常生活的误解
- **超越符号学/再现论**（Barthes）：物不仅是"可读的"符号，更是"可触的"物质实在

---

## 七、全书语言文风总评

### 7.1 总体特征

Attfield的学术写作具有以下可辨识的风格特征：
- **精确与通达的平衡**：长句密集但逻辑清晰，从句嵌套控制在2-3层
- **第一人称的学术在场**：明确使用"I"和"this book"建立作者立场的清晰性
- **概念创新与日常语言的双重性**：新概念（textility, undesigned, spec builder's vernacular）与日常引用（"part of the furniture"）共存
- **感性与理性的切换**：在个人回忆/电影场景（感性）和理论分析（理性）之间快速切换
- **温和但坚定的批评**：对既有学术传统的批评语气克制但立场明确

### 7.2 修辞标帜

- **破折号使用**：全书大量使用em-dash（——）实现句内转折/解释，构成Attfield文风的视觉特征
- **括号中的注释**：常用括号进行概念的精确定义和自我修正（如"the everyday (lower case intended)"）
- **文学/流行文化引用**：Eliot诗歌、Poe小说、Lou Reed歌词、Kubrick电影——学术论证中穿插文化引用
- **双关使用**："personal effects"、"part of the furniture"、"bringing things to life"——日常词组的学术化

---

## 八、全书实体总览

### 8.1 人物实体分布

全书引用/讨论的学者和人物超过200位，包括：
- **哲学家**：Heidegger, Lefebvre, Barthes, Bataille, Wittgenstein
- **社会学家**：Giddens, Bourdieu, Simmel, Harvey
- **人类学家**：Appadurai, Miller, Spooner
- **精神分析师**：Winnicott, Greenberg
- **设计史家**：Forty, Pointon, Breward
- **女性主义学者**：Steedman, Kirkham, Ash, Gordon, Warwick
- **艺术家/设计师**：Cummings, Boontje, Starck, Fassett, Gehry

### 8.2 核心概念体系

全书原创/重新定义的核心概念约15个，形成互相关联的概念网络：
things with attitude → design in the lower case → undesigned → spec builder's vernacular → reasonable furniture → textility → personal effects → containment → ephemeral materiality → authenticity paradox → embodiment/disembodiment

### 8.3 核心物理对象

全书分析的物理对象涵盖六个尺度层级：
- **身体尺度**：化妆品、服饰、假肢
- **家具尺度**：椅子、梳妆台、复制品家具
- **房间尺度**：卧室套件、厨房
- **建筑尺度**：半独立式住宅、半木结构山墙
- **社区尺度**：Cockfosters郊区
- **城市尺度**：伦敦地铁Piccadilly线

### 8.4 核心空间场所

- **博物馆/机构**：V&A Museum, ICA, British Museum, Design Museum, Crafts Council, National Trust
- **生产场所**：Clarkes工场, Brinton地毯工厂
- **居住场所**：Mrs Winter的卧室, No. 7 Hays Gardens, Harlow New Town
- **消费/文化场所**：遗产博物馆, 购物中心, 主题公园
- **学术场所**：Futures会议, "Getting Real"研讨会, Material Memories会议

### 8.5 核心事件/展览

- 1851年大博览会 → V&A博物馆的制度起源
- 1933年 Piccadilly线延伸至Cockfosters → 郊区化关键节点
- 1982年 Cockfosters田野调查 → 核心经验研究
- 1996年 "Getting Real"研讨会 → 物质性研究的学术聚集
- 1999年 Stealing Beauty展览 → 当代设计实践的展示
- 1999年 Material Memories会议 → 物质记忆研究的兴起

### 8.6 核心文献引用

全书引用文献超过200部，覆盖面极广。最具构建性功能的引用包括：
- Appadurai (1986) The Social Life of Things
- Winnicott (1971) Playing and Reality
- Heidegger (1927) Being and Time
- Lefebvre (1947-81) Critique of Everyday Life
- Forty (1986) Objects of Desire
- Miller (1987) Material Culture and Mass Consumption
- Lowenthal (1985) The Past is a Foreign Country

---

## 九、全书评价与当代意义

### 9.1 学术价值

《Wild Things》在以下方面具有长久的学术价值：
1. **方法论示范**：展示了如何将哲学理论（Heidegger）、精神分析（Winnicott）、人类学（Appadurai）整合为物质文化的分析工具
2. **概念创新**：创造了一系列至今仍被广泛使用的分析概念
3. **政治介入**：为"被忽视的"日常物质实践提供了学术合法性
4. **跨学科桥梁**：在设计史、人类学、社会学、文化研究之间建立了有效的对话

### 9.2 历史局限

从2026年的视角回溯：
1. **数字化/虚拟化讨论不足**：2000年出版时尚处于数字时代前夜，对虚拟物的讨论仅在第九章有所暗示
2. **非西方视角有限**：案例主要集中在英国，对非西方物质文化的分析较为薄弱
3. **可持续性/生态维度缺失**：2000年的学术语境尚未将生态危机置于中心位置，"物的废弃与循环"没有得到充分关注

### 9.3 当代意义

在2026年的物质文化语境中，《Wild Things》的洞见依然具有强烈相关性：
- "离身"（disembodiment）的趋势在20多年后的数字/社交媒体时代进一步加速
- "小写设计"的概念在maker movement、开源设计的时代获得新的生命
- "容纳"（containment）的生态学视角为理解"极简主义vs.囤积"的当代焦虑提供了分析工具
- 全书对"日常"的理论化依然是抵抗"spectacular design"文化霸权的有力武器

---
*报告生成日期：2026-08-05*
*本报告基于对《Wild Things》全9章及Introduction的逐章深度分析生成*
"""
    write_report('00_整体分析报告.md', report)

# =============================================================================
# NN_专项报告与实体总索引
# =============================================================================
def gen_special():
    report = """# Judy Attfield《Wild Things》(2000) 专项报告与实体总索引

## 专项报告一：全书方法论体系

### 一、后学科研究范式

Attfield在Introduction中明确宣布本书是"unashamedly hybrid"的——这一自我定位构成了全书的方法论总纲。所谓"后学科"（post-disciplinary）不是"反学科"（anti-disciplinary），而是在充分掌握各学科传统方法后，有意识地跨越学科边界进行研究。

**L000.S1.1 跨学科拼贴的原则**：
1. **以问题为中心而非以学科为中心**：研究问题（"物如何在日常生活中承载意义？"）决定方法选择，而非相反
2. **理论作为工具箱**：不同理论不是竞争的"真理"，而是互补的分析工具
3. **案例的优先性**：理论服务于案例，而非案例服务于理论

### 二、案例研究方法的理论辩护（Chapter 3第五节）

Attfield为案例研究方法提供了系统的理论辩护：

**L000.S1.2.1 微观-宏观关系的再思考**：
- "普遍性"不能通过抽象的理论推导获得，只能通过对"具体性"的深度分析来逼近
- 案例研究不是"微观的"——它通过在特定情境中揭示的关系网络来连接微观与宏观

**L000.S1.2.2 案例选择的标准**：
- 信息丰富性（information-richness）而非统计代表性
- 典型案例（typical case）：Clarkes（行业标准的代表）
- 关键案例（critical case）：Mrs Winter（理论预期的反例）
- 极端案例（extreme case）：Cockfosters（郊区化过程的极端例证）

### 三、概念翻转法的系统运用

Attfield最具辨识度的方法论特征是对既有概念的"翻转"操作：

| 既有概念（常识含义） | 翻转后的含义 | 所在章节 |
|---------------------|-------------|---------|
| 复制品=假货/低劣 | 复制品=诚实的本真性 | Ch4 |
| 短暂=无价值 | 短暂=现代身份的条件 | Ch5 |
| 日常=平庸/无趣 | 日常=文化的根基 | Ch2 |
| 杂物=混乱 | 杂物=个人生态的丰富性 | Ch6 |
| 郊区=庸俗/保守 | 郊区=另一种现代性 | Ch7 |
| 设计=专业活动 | 设计=普通人的日常实践 | Ch1 |

---

## 专项报告二：全书理论对话关系图

### 一、对话谱系

```
                    物质文化研究
                         │
        ┌────────────────┼────────────────┐
        │                │                │
   人类学路线          设计史路线        精神分析路线
   (Appadurai,        (Forty,           (Winnicott,
    Miller,            Pointon,          Greenberg)
    Spooner)           Breward)              │
        │                │                │
        └────────────────┼────────────────┘
                         │
                    Attfield的
                  "后学科"综合
                         │
        ┌────────────────┼────────────────┐
        │                │                │
   社会学转向        哲学转向          政治转向
   (Giddens,         (Heidegger,       ( feminism,
    Bourdieu,         Lefebvre,          class analysis,
    Harvey,           Barthes,           post-colonial)
    Simmel)           Latour)
```

### 二、关键理论接受的修正

| 理论来源 | 原始语境 | Attfield的修正/扩展 |
|---------|---------|-------------------|
| Appadurai的"物的社会生命" | 人类学的礼物/商品交换 | 扩展到现代消费社会的所有物 |
| Winnicott的"过渡性客体" | 儿童发展心理学 | 扩展到成人物质文化实践 |
| Lefebvre的"日常生活批判" | 马克思主义哲学 | 重新定向为物质文化分析框架 |
| Heidegger的"存在时间" | 存在主义哲学 | 与物质文化的经验分析对接 |
| Lévi-Strauss的"bricolage" | 结构主义人类学 | 重新定向为DIY/消费实践分析 |

---

## 专项报告三：全书叙事策略与修辞分析

### 一、宏观叙事结构

全书可以被读作一部"学术教育小说"（academic Bildungsroman）：从设计史学科的"童年"（Ch1对设计史学史的追溯）出发，经历了一系列"冒险"（Part II的案例深描），最终抵达一个开放的"成年"反思（Ch9的"离身"诊断和BBC节目的伦理讨论）。

### 二、开篇与收束的修辞对称

- **开篇（Introduction）**："This is a contradictory project..."——以"矛盾的"作为全书第一个自我描述词，预设了全书的辩证基调
- **收束（Ch9结尾）**：BBC Radio 4中"choice, mind and feelings"——以"何为人"的伦理问题收束，将全书的物质文化分析引向一个更深层的人类学追问

### 三、情感节奏的调控

全书各章的情感密度呈现出有意识的波动：
- Ch1-3（Part I）：情感中性，以概念辨析为主
- Ch4：中等情感密度，行业故事带来叙事性
- Ch5：最高情感密度——以个人丧母回忆开篇
- Ch6：中高情感密度——电影场景和梳妆台轶事
- Ch7-8：中低情感密度——空间和时间分析
- Ch9：中高情感密度——以跨性别歌曲和生命伦理讨论收束

### 四、插图系统的功能

全书19幅插图不是装饰性的，而是论证的有机组成部分：
- **作为证据**：图17（No. 7 Hays Gardens）、图18（1939年Cockfosters航拍）——田野考察的视觉记录
- **作为反讽**：图2（"Designer" cheddar cheese）——对"设计"概念的视觉讽刺
- **作为对照**：图13（1938年好品味的梳妆台）vs. 图15（Mrs Winter的"非实用型"梳妆台）——好设计/消费者选择的对立
- **作为论证**：图4（El Ultimo Grito的设计宣言）——设计实践者自己的话语

---

## 实体总索引

### 一、核心人物索引（全书出现≥2次的重要人物）

| 编号 | 姓名 | 领域 | 出现章节 | 功能 |
|------|------|------|---------|------|
| P001 | Arjun Appadurai | 人类学 | Intro, Ch1, Ch3 | 物的社会生命/价值体制理论 |
| P002 | Daniel Miller | 人类学 | Intro, Ch5, Ch8 | 物质文化与消费理论 |
| P003 | Donald Winnicott | 精神分析 | Ch3, Ch5 | 过渡性客体理论 |
| P004 | Adrian Forty | 设计史 | Ch1 | 设计史方法论批判 |
| P005 | Anthony Giddens | 社会学 | Ch6, Ch7 | 本体安全/隐私理论 |
| P006 | Henri Lefebvre | 哲学/社会学 | Ch2 | 日常生活批判 |
| P007 | Martin Heidegger | 哲学 | Ch8 | 存在时间 |
| P008 | Roland Barthes | 符号学/文论 | Ch1 | 神话学/物之意义 |
| P009 | Bruno Latour | STS | Ch1 | 行动者网络理论 |
| P010 | Pierre Bourdieu | 社会学 | Ch2 | 品味/区隔 |
| P011 | Georg Simmel | 社会学 | Ch3, Ch5 | 时尚/现代性 |
| P012 | David Harvey | 地理学 | Ch3, Ch8 | 时空压缩 |
| P013 | Brian Spooner | 人类学 | Ch3, Ch4 | 本真性的人类学分析 |
| P014 | David Lowenthal | 历史学/地理学 | Ch4, Ch8 | 过去/遗产文化 |
| P015 | Dick Hebdige | 文化研究 | Ch3 | 亚文化/现代性隐喻 |
| P016 | Raymond Williams | 文化理论 | Ch7 | 城市/乡村 |
| P017 | Carolyn Steedman | 历史学 | Ch5 | 童年/物品/记忆 |
| P018 | Pat Kirkham | 设计史 | Ch5 | 母亲外套的情感案例 |
| P019 | Christopher Breward | 时尚史 | Ch5 | 时尚文化史 |
| P020 | Juliet Ash | 女性主义 | Ch5 | 服饰与性别 |
| P021 | Beverley Gordon | 物质文化 | Ch9 | 女性与物 |
| P022 | Alexandra Warwick | 文化研究 | Ch9 | 身体/时尚 |
| P023 | Pasi Falk | 社会学 | Ch9 | 具身消费 |
| P024 | Georges Bataille | 哲学 | Ch9 | 身体/耗费 |
| P025 | Jane Graves | 学者 | Ch6, Ch8 | 研讨会组织者 |
| P026 | T. S. Eliot | 文学 | Ch8 | Prufrock诗句引用 |
| P027 | Neil Cummings | 当代艺术 | Ch1 | 降落伞装置 |
| P028 | Tord Boontje | 设计 | Ch1 | Rough and Ready Chair |
| P029 | Kaffe Fassett | 设计/手工艺 | Ch2 | 编织艺术 |
| P030 | Mike Leigh | 电影 | Ch6 | Secrets and Lies |

### 二、核心概念索引

| 编号 | 概念（中文） | 概念（原文） | 首现章节 | 原创性 |
|------|------------|-------------|---------|--------|
| C001 | 有态度的物 | things with attitude | Ch1 | 重新定义 |
| C002 | 小写设计 | design in the lower case | Ch2 | 原创 |
| C003 | 反设计 | undesigned | Ch2 | 原创 |
| C004 | 本真性 | authenticity | Ch3-4 | 重新理论化 |
| C005 | 短暂的物质性 | ephemeral materiality | Ch3, Ch5 | 原创 |
| C006 | 容纳 | containment | Ch3, Ch6 | 重新理论化 |
| C007 | 过渡性客体 | transitional object | Ch5 | 概念扩展 |
| C008 | 织理性 | textility | Ch5 | 原创 |
| C009 | 合理的家具 | reasonable furniture | Ch4 | 原创 |
| C010 | 投机建造商的本土风格 | spec builder's vernacular | Ch7 | 原创 |
| C011 | 平凡的安置 | installation of the commonplace | Ch3, Ch6 | 原创 |
| C012 | 具身/离身 | embodiment/disembodiment | Ch9 | 重新框架化 |
| C013 | 个人效应 | personal effects | Ch5 | 双关概念的学术化 |
| C014 | 新古物主义 | new antiquarianism | Ch8 | 原创 |
| C015 | 价值体制 | regimes of value | Ch1 | 借用（Appadurai） |
| C016 | 后学科 | post-disciplinary | Intro | 原创方法论定位 |

### 三、核心物理对象索引

| 编号 | 对象 | 类型 | 所在章节 | 分析功能 |
|------|------|------|---------|---------|
| O001 | 椅子（chair） | 家具 | Ch1 | 人造物vs.自然物的界定 |
| O002 | Cummings的降落伞 | 装置艺术 | Ch1 | 反驳再现理论 |
| O003 | DIY鸡尾酒柜（1959） | 家庭自制家具 | Ch2 | 日常设计实践 |
| O004 | Clarkes复制品家具 | 家具 | Ch4 | 本真性的悖论 |
| O005 | Kirkham母亲的外套 | 服饰 | Ch5 | 情感/身份的物化 |
| O006 | Mrs Winter的梳妆台（1951） | 家具 | Ch6 | 容纳实践的核心案例 |
| O007 | 半独立式住宅 | 建筑类型 | Ch7 | 投机建造商的本土风格 |
| O008 | Piccadilly线地铁 | 交通设施 | Ch7 | 郊区化的物质驱动力 |
| O009 | 咖啡勺 | 日常餐具 | Ch8 | 存在时间的物质化 |
| O010 | 假肢/假体 | 医疗器械 | Ch9 | 具身/离身的双重性 |
| O011 | 化妆品 | 身体修饰品 | Ch6, Ch9 | 具身/阶级/性别的交汇 |
| O012 | 时尚服饰 | 衣着 | Ch5, Ch9 | 短暂性的物化载体 |
| O013 | 家庭照片 | 图像/物品 | Ch8 | 记忆的物质化 |
| O014 | 儿童安抚毯 | 过渡性客体 | Ch5 | Winnicott理论的原初对象 |
| O015 | 遗产博物馆复制品 | 展示物 | Ch8 | "过去"的可触摸体验 |
| O016 | Buddha雕像 | 家庭装饰品 | Ch9 | 全书结尾的个人叙事参照物 |

### 四、核心空间/场所索引

| 编号 | 场所 | 类型 | 所在章节 | 分析功能 |
|------|------|------|---------|---------|
| S001 | Victoria and Albert Museum | 博物馆 | Ch1 | 设计史制度化的关键场所 |
| S002 | ICA London | 展览空间 | Ch1-2 | 当代设计实践的展示场所 |
| S003 | Brinton地毯工厂（Kidderminster） | 工业场所 | Ch2 | 设计师/制作者共存的空间 |
| S004 | Clarkes公司工场 | 生产场所 | Ch4 | 家族企业生产实践 |
| S005 | Mrs Winter的卧室 | 私人空间 | Ch6 | 梳妆台个案的具体场所 |
| S006 | Cockfosters | 伦敦郊区 | Ch7 | 核心案例研究场所 |
| S007 | Harlow New Town | 战后新城 | Ch6-7 | Mrs Winter搬入地 |
| S008 | No. 7 Hays Gardens | 具体住宅 | Ch7 | 半木结构山墙+双层玻璃的案例 |
| S009 | 遗产博物馆（Heritage Museum） | 博物馆类型 | Ch8 | "过去"的物质化体验场所 |
| S010 | National Trust物业 | 遗产机构 | Ch8 | 英国"过去"的机构化管理者 |
| S011 | 购物中心/主题公园 | 消费空间 | Ch2-3 | 当代视觉/消费文化的空间 |
| S012 | 矿村（pit village） | 社区空间 | Ch5 | Kirkham母亲外套的原初社会空间 |
| S013 | Crafts Council | 机构 | Ch2 | 手工艺制度化 |
| S014 | London Underground (Piccadilly Line) | 交通系统 | Ch7 | 城市/郊区的空间连接 |

### 五、核心事件/展览索引

| 编号 | 事件/展览 | 时间 | 所在章节 | 功能 |
|------|----------|------|---------|------|
| E001 | Great Exhibition | 1851 | Ch1 | V&A的制度起源 |
| E002 | V&A命名从"Manufactures"到"Art Museum" | 1857-1909 | Ch1 | 科学/艺术制度分离 |
| E003 | Piccadilly线延伸至Cockfosters | 1933 | Ch7 | 郊区化关键基础设施事件 |
| E004 | Mrs Winter购买卧室套件 | 1951 | Ch6 | 消费者选择的个案时间节点 |
| E005 | Cockfosters田野调查 | 1982 | Ch7 | Attfield的核心经验研究 |
| E006 | Eva Londos拍摄Mrs Winter梳妆台 | 1986 | Ch6 | 人类学田野记录 |
| E007 | Futures会议（Hebdige闭幕演讲） | 约1991 | Ch3 | 设计史学术共同体反思 |
| E008 | "Getting Real"研讨会 | 1996年2月 | Ch6 | Clutter主题跨学科讨论 |
| E009 | Material Memories会议 | 约1990s | Ch8 | 物质记忆研究兴起 |
| E010 | Stealing Beauty展览（ICA） | 1999 | Ch1-2 | 当代设计实践展示 |
| E011 | Abracadabra展览（Tate） | 1999年7月 | Ch1-2 | 当代艺术身份危机 |
| E012 | 《Eyes Wide Shut》上映 | 1999 | Ch5 | 身份/面具关系的大众文化案例 |
| E013 | BBC Radio 4讨论"创造人造生命" | 1999年12月10日 | Ch9 | 全书收束的文化事件 |

### 六、核心文献索引（最具构建性功能的前20部）

| 编号 | 文献 | 作者 | 年份 | 所在章节 | 功能 |
|------|------|------|------|---------|------|
| T001 | The Social Life of Things | Arjun Appadurai | 1986 | Ch1, Ch3 | 价值体制/物的社会生命 |
| T002 | Objects of Desire | Adrian Forty | 1986 | Ch1 | 设计史方法论 |
| T003 | Playing and Reality | Donald Winnicott | 1971 | Ch3, Ch5 | 过渡性客体 |
| T004 | Being and Time | Martin Heidegger | 1927 | Ch8 | 存在时间 |
| T005 | Critique of Everyday Life | Henri Lefebvre | 1947-81 | Ch2 | 日常生活批判 |
| T006 | Mythologies | Roland Barthes | 1957 | Ch1 | 物之意义分析 |
| T007 | Material Culture and Mass Consumption | Daniel Miller | 1987 | Ch5 | 消费/物质文化 |
| T008 | The Past is a Foreign Country | David Lowenthal | 1985 | Ch4, Ch8 | 过去/遗产文化 |
| T009 | The Condition of Postmodernity | David Harvey | 1989 | Ch3, Ch8 | 时空压缩 |
| T010 | Distinction | Pierre Bourdieu | 1979 | Ch2 | 品味/区隔 |
| T011 | The Consuming Body | Pasi Falk | 1994 | Ch9 | 具身消费 |
| T012 | Landscape for a Good Woman | Carolyn Steedman | 1986 | Ch5 | 童年/物品/记忆 |
| T013 | The Culture of Fashion | Christopher Breward | 1995 | Ch5 | 时尚文化史 |
| T014 | The World of Consumption | Fine & Leopold | 1993 | Ch1 | 消费/生产互动 |
| T015 | Taste and Power | Leora Auslander | 1996 | Ch1 | 品味政治学 |
| T016 | The Meaning of Things | Csikszentmihalyi & Rochberg-Halton | 1981 | Ch6 | 家庭物意义 |
| T017 | The Constitution of Society | Anthony Giddens | 1984 | Ch7 | 结构化理论 |
| T018 | English Furniture, Decoration, Woodwork and Allied Arts | T. A. Strange | 1900 | Ch4 | 家具本真性的历史建构 |
| T019 | The Things We See: Indoors and Out | Alan Jarvis | 1946 | Ch6 | 好品味话语的历史文献 |
| T020 | Philosophical Investigations | Ludwig Wittgenstein | 1953 | Ch1 | 日常语言哲学 |

---

## 附录：全书章节快速索引

| 章节编号 | 中文标题 | 核心概念 | 核心案例 | 字符数 |
|---------|---------|---------|---------|--------|
| Intro | 导论：日常生活的物质文化 | post-disciplinary, hybridity | — | 16,341 |
| Ch1 | 设计的意义——有态度的物 | things with attitude, regimes of value | V&A博物馆, Cummings降落伞 | 68,275 |
| Ch2 | 物的意义——小写设计 | design in the lower case, undesigned, the everyday | Kaffe Fassett编织, Utility Chic | 53,697 |
| Ch3 | 物与社会变迁的动力 | authenticity, ephemerality, containment | (预告Ch4-6主题) | 44,705 |
| Ch4 | 连续性——本真性与复制的悖论 | reasonable furniture, authenticity paradox | Clarkes家具公司 | 47,303 |
| Ch5 | 变化——身份的短暂物质性 | transitional object, textility, personal effects | Kirkham母亲外套 | 61,831 |
| Ch6 | 容纳——个人财物的生态学 | containment, clutter, dressing practices | Mrs Winter梳妆台 | 45,759 |
| Ch7 | 空间——物之所在 | spec builder's vernacular, bricolage, house vs. home | Cockfosters郊区化 | 66,159 |
| Ch8 | 时间——赋予物以生命 | existential time, new antiquarianism, material memories | 遗产博物馆, 咖啡勺 | 47,185 |
| Ch9 | 身体——自然与文化之间的门槛 | embodiment/disembodiment, prosthesis, gendered object | 假体, 时尚身体 | 47,476 |
| Conc | 结论 | — | Lou Reed, BBC讨论 | 3,958 |
| Afterword | 后记（Jo Turney） | 2000-2020的变迁 | — | 20,404 |

---
*报告生成日期：2026-08-05*
*本索引涵盖全书Introduction + 9章 + Conclusion + Afterword的完整实体范围*
"""
    write_report('NN_专项报告与实体总索引.md', report)

# Execute
gen_overall()
gen_special()
print("Final reports generated successfully!")
