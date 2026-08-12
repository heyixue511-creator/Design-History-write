# NN_专项报告与实体总索引

## 专项报告一：全书概念网络图

### 概念层级结构

```
Level 0: SOFTWARE（软件）
  └─ Level 1: Cultural Software（文化软件）
       └─ Level 2: Media Software（媒介软件）
            ├─ 模拟媒介技术（Simulations of prior media）
            └─ 原生计算媒介（Born-digital computational media）

Level 1: Computer Metamedium（计算机元媒介）
  ├─ 已有媒介的模拟（Simulations of existing media）
  │    └─ 含"新属性"的添加（New properties added）
  ├─ 全新计算媒介（New computational media）
  │    ├─ 超文本/超媒体（Hypertext/Hypermedia）
  │    ├─ 可导航3D空间（Navigable 3D space）
  │    ├─ GIS（Geographic Information Systems）
  │    ├─ 社交媒体（Social media）
  │    └─ 其他（etc.）
  └─ 杂交媒介（Hybrid media）
       └─ "深层可混合性"（Deep remixability）

Level 1: 软件技术双分类
  ├─ 第一方案（按数据形态）
  │    ├─ Media-specific techniques（媒介特定技术）
  │    └─ Media-independent techniques（媒介独立技术）
  └─ 第二方案（按历史谱系）
       ├─ 模拟旧工具的技术（Simulations）
       └─ "数字原生"技术（Born-digital）

Level 2: Medium = Algorithms + a Data Structure
  ├─ 数据结构（Data Structures）
  │    ├─ 位图（Bitmap）
  │    ├─ 矢量图（Vector）
  │    ├─ 3D多边形模型（Polygonal 3D model）
  │    ├─ 3D NURBS模型（NURBS model）
  │    ├─ ASCII文本
  │    ├─ HTML
  │    ├─ XML
  │    ├─ 音频格式
  │    ├─ 视频格式
  │    └─ KML等
  └─ 算法/工具/命令（Algorithms/Tools/Commands）
       ├─ 模拟型（Simulation — brush, filter, camera pan...）
       └─ 原生型（Native — constraint satisfaction, particle systems...）
```

### 核心论证链

```
Kay的元媒介概念（1977）
  → 永久可扩展性（软件≠硬件固化的物理媒介）
      → 数据结构标准化（多种物理材料→少数数据结构）
          → 杂交化可能（不同媒介技术在同一数据结构上相遇）
              → 深层可混合性（不仅混合内容，更混合技术基因）
                  → 新媒介物种（增殖→传统"媒介"概念失效）
                      → 进化"物种模型"替代分类"媒介模型"
```

## 专项报告二：人物谱系表

| 编号 | 姓名 | 生卒/活跃期 | 身份 | 核心贡献 | 出现章节 |
|------|------|-----------|------|----------|----------|
| L060 | Alan Kay | 1940- | 计算机科学家 | Dynabook构想；Smalltalk；"元媒介"概念 | 导论/第1/2/3/4/5/结论 |
| L061 | J.C.R. Licklider | 1915-1990 | 心理学家/计算机科学家 | "人机共生"理念；ARPANET推动者 | 导论/第1章 |
| L062 | Ivan Sutherland | 1938- | 计算机科学家 | Sketchpad（1962）；交互式图形奠基人 | 导论/第1/2章 |

【校对修正】原表写"Sketchpad（1963）；首个VR系统"：源文件对Sketchpad年份统一用1962（源文件第492行），且源文件未提及Sutherland的VR头戴显示器（"首个VR系统"属外部知识、源文件无对应内容），已删除并统一为1962，与时间线一致。
| L063 | Douglas Engelbart | 1925-2013 | 工程师/发明家 | NLS系统；鼠标；视窗；"视控"概念 | 导论/第1/2章 |
| L064 | Ted Nelson | 1937-2024 | 信息技术先驱 | "超文本""超媒体"术语；Xanadu项目 | 导论/第1/2/3章 |
| L065 | Nicholas Negroponte | 1943- | 建筑师/计算机科学家 | MIT Media Lab创始人；*Being Digital* | 导论/第1/3章 |
| L066 | Marshall McLuhan | 1911-1980 | 媒介理论家 | *Understanding Media*；"媒介即讯息" | 导论/第1/5章 |
| L101 | Adele Goldberg | 1945- | 计算机科学家 | 1977年与Kay合著"Personal Dynamic Media" | 第1/2/3/4章 |
| L102 | Ivan Sutherland | 见L062 | | | |
| L105 | Jerome Bruner | 1915-2016 | 认知心理学家 | enactive/iconic/symbolic三重心智理论 | 第1/4章 |
| L107 | Alvy Ray Smith | 1943- | 计算机图形学先驱 | SuperPaint；区分"paint program"与"paint system" | 第1章 |
| L108 | Richard Shoup | 1943-2015 | 计算机科学家 | SuperPaint主要开发者 | 第1章 |
| L109 | Marshall McLuhan | 见L066 | | | |
| L113 | Larry Tesler | 1945-2020 | 计算机科学家 | 在Xerox PARC实现cut/copy/paste通用命令 | 第1/2章 |
| L202 | Gotthold Lessing | 1729-1781 | 哲学家/艺术批评家 | *Laocoon*——诗歌与绘画的区分 | 第2章 |
| L203 | Clement Greenberg | 1909-1994 | 艺术批评家 | 现代主义绘画"平面性"独特性 | 第2章 |
| L205 | George Lakoff | 1941- | 认知语言学家 | 概念隐喻理论 | 第2章 |
| L206 | Thomas Porter & Tom Duff | 1950s- | 计算机科学家 | 1984年数字合成论文；RGB+Alpha通道 | 第2章 |
| L207 | John & Thomas Knoll | 1960s- | 软件工程师 | Photoshop最初开发者 | 第2章 |
| L208 | Martin Wattenberg | 1970- | 数据可视化艺术家 | 音乐/文本/网络结构可视化 | 第2章 |
| L304 | Masaki Fujihata | 1956- | 媒体艺术家 | *Field-Work*系列——GPS+视频+3D空间 | 第3章 |
| L302 | Joachim Sauter | 1959-2021 | 媒体艺术家/设计师 | Art+Com创始人——*Invisible Shape* | 第3章 |
| L400 | Niklaus Wirth | 1934-2024 | 计算机科学家 | *Algorithms+Data Structures=Programs* | 第4章 |
| L402 | Howard Gardner | 1943- | 心理学家 | 多元智能理论（1983） | 第4章 |
| L501 | Jeremy Blake | 1971-2007 | 数字影像艺术家 | *Sodium Fox*；*Winchester Trilogy* | 第5章 |
| L502 | Takeshi Murata | 1974- | 数字影像艺术家 | *Untitled (Pink Dot)* | 第5章 |
| L503 | Ann Lislegaard | 1962- | 艺术家 | *Crystal World*；*Bellona* | 第5章 |
| L507 | Imaginary Forces | 1996- | 设计公司 | *Mad Men*片头；运动图形产业定义者 | 第5章 |
| L508 | Psyop | 2001- | 动画/视觉特效公司 | 超风格化商业广告 | 第5章 |
| L510 | Gregg Lynn | 1964- | 建筑师 | 粒子系统生成建筑形态；"blob"建筑 | 第5章 |
| L603 | Michelangelo Antonioni | 1912-2007 | 电影导演 | *Blowup*——照片放大揭示隐藏真相 | 结论 |

## 专项报告三：时间线——文化软件发展的关键节点

```
1945    Vannevar Bush, "As We May Think" —— Memex构想
1947    Giedion, *Mechanization Takes Command*
1948    Shannon, *A Mathematical Theory of Communication*
1949    MIT Lincoln Laboratory开始交互式计算机工作
1950s   数字图像处理的军事起源（侦察照片分析）
1960    Spacewar游戏（TX-2计算机）
1962    Sutherland完成Sketchpad（MIT博士论文）
1965    Nelson,"A File Structure for the Complex... "——超文本宣言
1968    Engelbart "母亲之所有演示" —— NLS系统
1970    Kay加入Xerox PARC
1972-3  Shoup开发SuperPaint
1974-5  Tesler在PARC实现cut/copy/paste通用命令
1975    Wirth,*Algorithms Plus Data Structure Equals Programs*
1977    Kay & Goldberg,"Personal Dynamic Media" —— "元媒介"定义
1978-9  Aspen Movie Map（Architecture Machine Group, MIT）
1981    Xerox Star发布（首个商业GUI）
1982    *Star Trek II* —— Porter & Duff数字合成的前身
1984    Apple Macintosh发布；Porter & Duff SIGGRAPH论文
1985    Macromedia Director（原VideoWorks）发布；PageMaker发布
1987    Illustrator发布；HyperCard发布
1989    Photoshop 1.0发布
1990    World Wide Web原型完成（Tim Berners-Lee）
1991    QuickTime 1.0发布（Apple）
1992    JPEG格式开始广泛使用
1993    After Effects 1.0发布 —— "天鹅绒革命"起点
1994    Photoshop 3.0加入图层功能
1999    AE 4.0 + Photoshop 5.5 + Final Cut Pro —— 互操作性范式完成
2004    Flickr上线；Mappr mashup（Stamen Design）
2005    Google Earth发布；YouTube上线
2006    Facebook向公众开放；Twitter上线
2007    iPhone发布；Google Street View上线
2010    iPad发布；HTML5标准推进
2013    Manovich,*Software Takes Command*出版
```

## 专项报告四：软件产品家族谱系

### 图像编辑
```
SuperPaint (Shoup, PARC, 1972-3)
  → Paint (Smith, 1975-6)
    → Digital Darkroom (1987, "plug-in"术语起源)
      → Photoshop (Knoll兄弟, ILM/Adobe, 1989-)
        ├─ Photoshop CS4 (2008)
        ├─ Photoshop CS5.5 (2011)
        └─ Photoshop Touch for iPad
```

### 视频/运动图形
```
Harry (Quantel, 1986) / Flame/Inferno (Discreet Logic, 1992)
  → After Effects (Adobe, 1993-)
      ├─ AE 4.0 (1999, Premiere导入)
      └─ 竞争对手: Motion (Apple), Combustion (Autodesk), Nuke
```

### 3D建模/动画
```
Sketchpad (Sutherland, 1963)
  → Wavefront / Alias (1984-)
      → Alias|Wavefront (1995, SGI并购合并)
        → Maya (Autodesk, 2006-)
  3ds Max (Autodesk)
  LightWave 3D
  Blender (开源)
```

### 办公/生产
```
NLS (Engelbart, 1968)
  → Xerox Star (1981)
    → MacWrite/MacPaint (1984)
      → Word (1984) / PowerPoint / Excel
      → Google Docs (2006-)
```

### GIS/空间媒体
```
GIS专业系统（1970s-）
  → ArcGIS
    → Earth Viewer (Keyhole, 2001)
      → Google Earth (2005-)
      → Google Maps (2005-)
      → Bing Maps (Microsoft)
```

## 专项报告五：全书实体总索引

### 人物实体索引（按拼音排序）

| 编号 | 姓名 | 英文名 | 核心身份 |
|------|------|--------|----------|
| L212 | Bill Atkinson | Bill Atkinson | HyperCard开发者 |
| L209 | Ben Fry | Ben Fry | Processing共同开发者；信息可视化 |
| L203 | Clement Greenberg | Clement Greenberg | 现代主义艺术批评家 |
| L063 | Douglas Engelbart | Douglas Engelbart | 鼠标/视窗/视控发明人 |
| L602 | DJ Spooky | Paul Miller | 电子音乐家 |
| L404 | Eleanor Rosch | Eleanor Rosch | 原型理论心理学家 |
| L511 | Foreign Office Architects | FOA | 建筑事务所 |
| L205 | George Lakoff | George Lakoff | 认知语言学家 |
| L202 | Gotthold Lessing | Gotthold Lessing | 哲学家；*Laocoon*作者 |
| L510 | Gregg Lynn | Gregg Lynn | 建筑师；"blob"建筑 |
| L402 | Howard Gardner | Howard Gardner | 多元智能理论 |
| L062 | Ivan Sutherland | Ivan Sutherland | Sketchpad发明人 |
（注：人物谱系表中该行已据源文件统一为“Sketchpad（1962）”，删除“首个VR系统”（源文件无此内容，属外部知识）。【校对修正】）
| L061 | J.C.R. Licklider | J.C.R. Licklider | "人机共生"先驱 |
| L064 | Ted Nelson | Ted Nelson | 超文本/超媒体概念创造者 |
| L501 | Jeremy Blake | Jeremy Blake | 数字影像艺术家 |
| L105 | Jerome Bruner | Jerome Bruner | 认知心理学家 |
| L302 | Joachim Sauter | Joachim Sauter | Art+Com创始人 |
| L207 | John & Thomas Knoll | Knoll brothers | Photoshop开发者 |
| L207 | John Knoll | John Knoll | ILM特效监督；Photoshop共同开发者 |
| L606 | 已删除 | （原L606为DJ Spooky重复条目，与L602重复且与07结论报告L606=Google+冲突，已删除。【校对修正】） | |
| L403 | Louis Menand | Louis Menand | 历史学家；达尔文转向的解释 |
| L066 | Marshall McLuhan | Marshall McLuhan | 媒介理论家 |
| L208 | Martin Wattenberg | Martin Wattenberg | 数据可视化艺术家 |
| L304 | Masaki Fujihata | Masaki Fujihata | 日本媒体艺术家 |
| L065 | Nicholas Negroponte | Nicholas Negroponte | MIT Media Lab创始人 |
| L400 | Niklaus Wirth | Niklaus Wirth | 计算机科学家 |
| L068 | Noah Wardrip-Fruin | Noah Wardrip-Fruin | *Expressive Processing*作者 |
| L108 | Richard Shoup | Richard Shoup | SuperPaint开发者 |
| L502 | Takeshi Murata | Takeshi Murata | 数字影像艺术家 |
| L206 | Thomas Porter & Tom Duff | Porter & Duff | 数字合成概念定义者 |
| L500 | Trish & Chris Meyer | Meyer夫妇 | After Effects教科书作者 |
| L406 | Wassily Kandinsky | Wassily Kandinsky | 抽象艺术先驱 |
| L512 | Zaha Hadid | Zaha Hadid | 建筑师 |

### 软件产品实体索引（按类型）

**图像与图形**：Photoshop, Illustrator, GIMP, Inkscape, Painter, SuperPaint, Paint, Digital Darkroom, Paintbox（Quantel）, iPhoto, Picasa, Aperture

**视频与运动图形**：After Effects, Final Cut, Premiere, Flame, Inferno, Smoke, Lustre, Harry, Henry, Hal, Mirage, Motion, Combustion, Flash（Macromedia/Adobe）

**3D建模与动画**：Maya, 3ds Max, Blender, LightWave 3D, Alias, Wavefront, SketchUp, AutoCAD, Revit

**文本与办公**：Microsoft Word, PowerPoint, Excel, Google Docs, OpenOffice, Pages, MacWrite, WordPerfect

**多媒体与Web**：Macromedia Director, QuickTime, HyperCard, Dreamweaver, Flash, WordPress, Blogger, Firefox, Chrome

**音频**：Pro Tools, Audacity, GarageBand, Max/MSP, PD (Pure Data)

**GIS与地图**：Google Earth, Google Maps, ArcGIS, Bing Maps

**编程环境与语言**：Smalltalk, Processing, Java, JavaScript, Python, PHP, ActionScript, C++

### 概念实体索引（按英文首字母）

| 英文 | 中文 | 编号 |
|------|------|------|
| amplification | 放大效应 | L541 |
| API | 应用程序编程接口 | L321 |
| computer metamedium | 计算机元媒介 | L125 |
| constraint satisfaction | 约束满足 | L130 |
| continuity turn | 连续性转向 | L540 |
| convergence | 融合 | L319 |
| crossover effect | 交叉效应 | L542 |
| cultural software | 文化软件 | L082 |
| data structure | 数据结构 | L418 |
| deep remixability | 深层可混合性 | L537 |
| digital compositing | 数字合成 | L231 |
| digital image processing | 数字图像处理 | L235 |
| Dynabook | Dynabook | L124 |
| file format | 文件格式 | L420 |
| GIS layers | GIS图层 | L232 |
| media hybridization | 媒介杂交化 | L316 |
| media species | 媒介物种 | L318 |
| media-independent techniques | 媒介独立技术 | L228 |
| media-specific techniques | 媒介特定技术 | L229 |
| Medium=Algorithms+Data Structure | 媒介=算法+数据结构 | L419 |
| metamedium | 元媒介 | L081 |
| motion graphics | 运动图形 | L536 |
| multimedia vs. hybrid media | 多媒体vs.杂交媒介 | L317 |
| parameters | 参数化 | L421 |
| permanent extendibility | 永久可扩展性 | L128 |
| remediation | 再媒介化 | L084 |
| software epistemology | 软件认识论 | L615 |
| software performance | 软件表演 | L085 |
| software studies | 软件研究 | L083 |
| universal commands | 通用命令 | L237 |
| variable form | 可变形式 | L539 |
| Velvet Revolution | 天鹅绒革命 | L535 |
| view control | 视控 | L126 |

### 机构实体索引

| 英文 | 中文 | 编号 |
|------|------|------|
| Adobe Systems | Adobe系统公司 | L080 |
| Apple Inc. | 苹果公司 | L079 |
| Architecture Machine Group (MIT) | 建筑机器小组 | L312 |
| Art+Com | Art+Com | L313 |
| Autodesk | Autodesk | L530 |
| BBC | BBC | L417 |
| Calit2 (UCSD) | 加州电信与信息技术研究院 | L078 |
| Europeana | 欧洲数字图书馆 | L416 |
| Google | 谷歌 | L611 |
| ILM (Industrial Light and Magic) | 工业光魔 | L222 |
| Imaginary Forces | Imaginary Forces | L527 |
| Keyhole, Inc. | Keyhole公司 | L314 |
| MIT Lincoln Laboratory | MIT林肯实验室 | L120 |
| MIT Media Lab | MIT媒体实验室 | L077 |
| Psyop | Psyop | L528 |
| Quantel | Quantel | L531 |
| Research Center for Augmenting Human Intellect (SRI) | SRI增强人类智力研究中心 | L121 |
| Stamen Design | Stamen设计 | L315 |
| University of Utah | 犹他大学 | L123 |
| Xerox PARC | 施乐帕洛阿尔托研究中心 | L076 |

### 论著/文献实体索引

| 编号 | 作者/标题 | 年份 |
|------|----------|------|
| L133 | Kay & Goldberg, "Personal Dynamic Media" | 1977 |
| L134 | Sutherland, *Sketchpad: A Man-Machine Graphical Communication System* | 1963 |
| L135 | Nelson, "A File Structure for the Complex, the Changing, and the Indeterminate" | 1965 |
| L087 | Bolter & Grusin, *Remediation: Understanding New Media* | 2000 |
| L088 | McLuhan, *Understanding Media* | 1964 |
| L089 | Giedion, *Mechanization Takes Command* | 1947 |
| L090 | Rheingold, *Tools for Thought* | 1985 |
| L091 | Wardrip-Fruin & Montfort (eds.), *New Media Reader* | 2003 |
| L092 | Shannon, *A Mathematical Theory of Communication* | 1948 |
| L138 | Bruner, *Toward a Theory of Instruction* | 1966 |
| L238 | Porter & Duff, "Compositing Digital Images" (SIGGRAPH) | 1984 |
| L239 | Wirth, *Algorithms Plus Data Structure Equals Programs* | 1975 |
| L240 | Lessing, *Laocoon: An Essay on the Limits of Painting and Poetry* | 1766 |
| L241 | Greenberg, "Modernist Painting" | 1960 |
| L243 | Morville, *Ambient Findability* | 2005 |
| L244 | Smith et al., "Designing the Star User Interface" (*Byte*) | 1982 |
| L324 | Darwin, *On the Origin of Species* | 1859 |
| L325 | Moretti, *Graphs, Maps, Trees: Abstract Models for Literary History* | 2007 |
| L428 | Wirth, *Algorithms Plus Data Structure Equals Programs* | 1975 |
| L546 | Huyssen, *After the Great Divide* | 1986 |
| L547 | Meyer & Meyer, *Creating Motion Graphics* | 2000 |
| L549 | Bordwell & Thompson, *Film Art* | （多版） |
| L622 | Lyotard, *The Postmodern Condition* | 1979 |

### 事件实体索引（按时间排序）

| 编号 | 年份 | 事件 |
|------|------|------|
| L140 | 1962 | Sketchpad完成 |
| L093/L139 | 1968 | Engelbart的"母亲之所有演示" |
| L141 | 1977 | Kay & Goldberg发表"Personal Dynamic Media" |
| L327 | 1978-9 | Aspen Movie Map项目 |
| L434 | 1981 | Xerox Star发布 |
| L094/L142 | 1984 | Apple Macintosh发布 |
| L246 | 1984 | Porter & Duff在SIGGRAPH发表数字合成论文 |
| L554 | 1986 | Quantel Harry发布 |
| L247 | 1994 | Photoshop 3.0加入图层 |
| L248/L328 | 1991 | QuickTime 1.0发布 |
| L551 | 1993 | After Effects 1.0发布 |
| L552 | 1999 | AE 4.0 + PS 5.5 + FCP——互操作性范式完成 |
| L329 | 2004 | Mappr发布 |
| L330/L558 | 2005 | Google Earth首次发布 |
| L556 | 2005 | Common "Go" MV发布 |
| L555 | 2002 | Yokohama International Port Terminal建成 |
| L557 | 2007 | *Mad Men*片头发布 |
| L097 | 2007 | iPhone发布 |
| L331 | 2007 | Google Street View发布 |
| L627 | 2008 | HIPerSpace超级可视化计算机上线 |

【校对修正】原索引此处编号误用L625：L625在07结论报告中为“1977年Kay和Goldberg发表‘Personal Dynamic Media’”，2008年HIPerSpace在07结论报告中编号为L627，已统一为L627。另：时间线中1966“Sutherland首个VR头戴显示器”条目已删除（源文件无此内容，属外部知识）。
| L249 | 2010 | iPad首发 |
| L628 | 2011 | Google+ Circles / Facebook Subscribe推出 |

## 报告使用说明

本系列分析报告共含9份文件：

1. **00_整体分析报告.md** —— 全书宏观分析
2. **01_导论分析报告.md** —— 导论逐章分析
3. **02_第一章分析报告_Alan Kay的通用媒体机器.md**
4. **03_第二章分析报告_理解元媒介.md**
5. **04_第三章分析报告_杂交化.md**
6. **05_第四章分析报告_软进化.md**
7. **06_第五章分析报告_媒体设计.md**
8. **07_结论分析报告.md**
9. **NN_专项报告与实体总索引.md**（本文件）

每份报告均含九节：一、章节定位与功能 / 二、结构分析 / 三、内容分析（核心论题+关键论点案例）/ 四、逻辑梳理（论证链条+因果转折）/ 五、材料使用方式 / 六、论辩与阐述方法 / 七、语言文风（原文摘录+L###标注）/ 八、实体清单（六类每类≥3，带L###编号）/ 九、与前后章关联。

实体编号体系L###贯穿所有报告，确保索引一致性。NN文件提供跨报告的横向索引，包含概念网络图、人物谱系表、关键节点时间线、软件产品家族谱系、以及六类实体的完整索引。
