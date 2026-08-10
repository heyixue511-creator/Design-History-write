# NN_专项报告与实体总索引

---

## 第一部分：专项报告

### 专项一：全书76个模式总表

全书13章共覆盖76个交互设计模式。以下按章节排列：

| 编号 | 章节 | 模式名称 | 所属领域 | 核心功能 | 关键关联模式 |
|------|------|----------|----------|----------|--------------|
| 001 | Ch1 | Scroll | Composition | Viewport外的信息访问 | Vertical/Infinite List, Infinite Area |
| 002 | Ch1 | Annunciator Row | Composition | 硬件状态指示(radio/power/input) | Notifications, Titles |
| 003 | Ch1 | Notifications | Composition | 视觉/触觉/听觉警报 | Tones, Haptic Output, LED |
| 004 | Ch1 | Titles | Composition | 页面/元素标签 | Ordered Data, Tooltip |
| 005 | Ch1 | Revealable Menu | Composition | 可触发展开的隐藏菜单 | Fixed Menu, Pop-Up |
| 006 | Ch1 | Fixed Menu | Composition | 固定停靠的持续可见菜单 | Revealable Menu, Tabs |
| 007 | Ch1 | Home & Idle Screens | Composition | 设备/应用默认状态屏幕 | Lock Screen, Timeout |
| 008 | Ch1 | Lock Screen | Composition | 安全休眠锁定屏幕 | Sign On, Timeout |
| 009 | Ch1 | Interstitial Screen | Composition | 启动/加载过渡屏幕 | Wait Indicator |
| 010 | Ch1 | Advertising | Composition | 应用内广告集成 | — |
| 011 | Ch2 | Vertical List | Display | 单列垂直列表 | Scroll, Infinite List |
| 012 | Ch2 | Infinite List | Display | 动态加载无边列表 | Vertical List, Scroll |
| 013 | Ch2 | Thumbnail List | Display | 带缩略图的增强列表 | Vertical List, Grid |
| 014 | Ch2 | Fisheye List | Display | 焦点放大-周边缩小列表 | Vertical List, Carousel |
| 015 | Ch2 | Carousel | Display | 3D旋转项目排列 | Film Strip, Fisheye List |
| 016 | Ch2 | Grid | Display | 行列矩阵展示 | Thumbnail List, Sort & Filter |
| 017 | Ch2 | Film Strip | Display | 水平排列横向滚动 | Carousel, Slideshow |
| 018 | Ch2 | Slideshow | Display | 时间/操作驱动的单项目切换 | Film Strip, Carousel |
| 019 | Ch2 | Infinite Area | Display | 大型空间数据(地图)展示 | Zoom & Scale, Location Jump |
| 020 | Ch2 | Select List | Display | 可选择列表(展示+交互) | Vertical List, Form Selections |
| 021 | Ch3 | Confirmation | Control | 模态确认对话框 | Pop-Up, Exit Guard |
| 022 | Ch3 | Sign On | Control | 身份验证与授权 | Lock Screen, Timeout |
| 023 | Ch3 | Exit Guard | Control | 退出保护(灾难性数据丢失) | Confirmation, Cancel Protection |
| 024 | Ch3 | Cancel Protection | Control | 取消保护(高恢复成本数据) | Exit Guard, Confirmation |
| 025 | Ch3 | Timeout | Control | 不活跃超时自动退出/锁定 | Sign On, Lock Screen |
| 026 | Ch4 | Windowshade | Revealing | 同一页面上展开额外信息 | Pop-Up, Hierarchical List |
| 027 | Ch4 | Pop-Up | Revealing | 浮层覆盖展示控件/信息 | Windowshade, Confirmation |
| 028 | Ch4 | Hierarchical List | Revealing | 逐层深入的列表导航 | Drilldown (Link/Button), Vertical List |
| 029 | Ch4 | Returned Results | Revealing | 搜索结果的列表展示 | Search Within, Sort & Filter |
| 030 | Ch5 | Tabs | Lateral | 水平选项卡切换 | Pagination, Fixed Menu |
| 031 | Ch5 | Peel Away | Lateral | "剥离"揭示下层内容 | Simulated 3D Effects, Windowshade |
| 032 | Ch5 | Simulated 3D Effects | Lateral | 3D透视/旋转传达空间关系 | Peel Away, Carousel |
| 033 | Ch5 | Pagination | Lateral | 分页导航 | Tabs, Location Within |
| 034 | Ch5 | Location Within | Lateral | "我在哪里"的位置指示 | Tabs, Ordered Data |
| 035 | Ch6 | Link | Drilldown | 文本内导航触发器 | Button, Icon, Indicator |
| 036 | Ch6 | Button | Drilldown | 明确操作的触发器 | Link, Icon, Press-and-Hold |
| 037 | Ch6 | Indicator | Drilldown | 图形化的"可深入"提示 | Icon, Link, Annotation |
| 038 | Ch6 | Icon | Drilldown | 紧凑图形化触发器 | Indicator, Button, Accesskeys |
| 039 | Ch6 | Stack of Items | Drilldown | "卡片堆"展开机制 | Peel Away, Carousel |
| 040 | Ch6 | Annotation | Drilldown | 数据上的标注触发器 | Indicator, Tooltip |
| 041 | Ch7 | Ordered Data | Labels | 数值数据标签化 | Titles, Sort & Filter |
| 042 | Ch7 | Tooltip | Labels | 上下文相关的短暂解释 | Pop-Up, Annotation |
| 043 | Ch7 | Avatar | Labels | 用户视觉标识 | Icon, Thumbnail List |
| 044 | Ch7 | Wait Indicator | Labels | 加载/处理中的状态反馈 | Interstitial Screen, Reload/Synch/Stop |
| 045 | Ch7 | Reload/Synch/Stop | Labels | 数据刷新过程控制 | Wait Indicator, Tones |
| 046 | Ch8 | Zoom & Scale | Info Controls | 缩放改变细节层级 | Location Jump, Infinite Area |
| 047 | Ch8 | Location Jump | Info Controls | 索引/标记跳转到数据集位置 | Zoom & Scale, Search Within |
| 048 | Ch8 | Search Within | Info Controls | 数据集内搜索 | Returned Results, Autocomplete |
| 049 | Ch8 | Sort & Filter | Info Controls | 排序+过滤改变组织方式 | Ordered Data, Search Within |
| 050 | Ch9 | Keyboards & Keypads | Text Input | 硬件/软件键盘 | Pen Input, Mode Switches |
| 051 | Ch9 | Pen Input | Text Input | 手写笔识别和手势输入 | Keyboards & Keypads, Input Areas |
| 052 | Ch9 | Mode Switches | Text Input | 输入模式切换 | Input Method Indicator, Keyboards |
| 053 | Ch9 | Input Method Indicator | Text Input | 输入法状态可视化 | Mode Switches, Tooltip |
| 054 | Ch9 | Autocomplete & Prediction | Text Input | 预测性文本辅助输入 | Search Within, Keyboards & Keypads |
| 055 | Ch10 | Directional Entry | Interactive | 五向/方向键定向输入 | Focus & Cursors, Scroll |
| 056 | Ch10 | Press-and-Hold | Interactive | 长按触发次级功能 | Button, Pop-Up |
| 057 | Ch10 | Focus & Cursors | Interactive | 聚焦元素的视觉指示 | Directional Entry, Scroll |
| 058 | Ch10 | Other Hardware Keys | Interactive | 专用硬件按键(音量/相机) | Accesskeys, Dialer |
| 059 | Ch10 | Accesskeys | Interactive | 硬件按键→屏幕功能一对映 | Other Hardware Keys, Keyboards |
| 060 | Ch10 | Dialer | Interactive | 电话拨号特殊交互 | Keyboards & Keypads, Other Hardware Keys |
| 061 | Ch10 | On-Screen Gestures | Interactive | 屏幕触控手势 | Kinesthetic Gestures, Press-and-Hold |
| 062 | Ch10 | Kinesthetic Gestures | Interactive | 设备运动输入(倾斜/摇晃) | On-Screen Gestures, Orientation |
| 063 | Ch10 | Remote Gestures | Interactive | 远离设备的手势控制 | On-Screen Gestures, Kinesthetic Gestures |
| 064 | Ch11 | Input Areas | Input | 输入区域尺寸和布局 | Keyboards & Keypads, Form Selections |
| 065 | Ch11 | Form Selections | Input | 选项选择机制 | Select List, Ordered Data |
| 066 | Ch11 | Mechanical Style Controls | Input | 物理隐喻控件(slider/switch) | Form Selections, On-Screen Gestures |
| 067 | Ch11 | Clear Entry | Input | 清除输入数据 | Confirmation, Cancel Protection |
| 068 | Ch12 | Tones | Audio | 非语音听觉信号 | Notifications, Haptic Output |
| 069 | Ch12 | Voice Input | Audio | 语音识别输入 | Voice Readback, Keyboards & Keypads |
| 070 | Ch12 | Voice Readback | Audio | 系统朗读信息(TTS) | Voice Input, Voice Notifications |
| 071 | Ch12 | Voice Notifications | Audio | 语音播报通知 | Voice Readback, Notifications |
| 072 | Ch12 | Haptic Output | Audio | 振动触觉反馈 | Tones, LED |
| 073 | Ch13 | LED | Screens | 低功耗硬件指示灯 | Haptic Output, Tones |
| 074 | Ch13 | Display Brightness Controls | Screens | 自动/手动亮度管理 | Orientation, Annunciator Row |
| 075 | Ch13 | Orientation | Screens | 屏幕方向自动检测切换 | Kinesthetic Gestures, Zoom & Scale |
| 076 | Ch13 | Location | Screens | 多源定位(GPS/WiFi/Cell) | Location Jump, Zoom & Scale |

---

### 专项二：全书理论框架依赖关系图

```
                     Christopher Alexander (Pattern Language, Preface)
                                |
                ┌───────────────┼───────────────┐
                |               |               |
        Donald Norman      Colin Ware      Paul Fitts
        (Interaction       (Information    (Fitts's Law,
        Model, Ch4/10)     Entities,       Ch11/Appendix D)
                           Ch2)
                |               |               |
        ┌───────┼───────┐   Hierarchy vs.    Touch Target
        |       |       |   Faceting         Sizing
    Mental   Mapping  Affordances  |               |
    Model                         |               |
        |               ┌───────┴───────┐       |
    Wayfinding      Morville's IA    Lynch's     |
    (Ch5)           Rules (Ch2)    Wayfinding    |
                                (Ch2/Ch5/Part I)
                                            |
                        ┌───────────────────┼───────────────────┐
                        |                   |                   |
                Gestalt Principles    Human Factors       Distributed
                (Part I/Ch1/Ch2)  (Appendix D:        Cognition
                                   Eye/Hearing/Touch/  (Payette 2008,
                                   Visual Angle/       Ch3)
                                   Rods & Cones)
                                            |
                        八条移动设计原则 (Preface)
                                            |
                            76个交互设计模式 (Ch1-13)
```

---

### 专项三：叙事结构分析

本书的一个标志性特征是在每章开篇使用叙事引入。以下是各章的叙事类型分布：

| 章节 | 叙事类型 | 叙事内容 | 修辞功能 |
|------|----------|----------|----------|
| Ch1 | 历史叙事 | Gutenberg/Bi Sheng印刷史 | 建立"排版原则是有历史根基的"权威感 |
| Ch2 | 认知叙事 | 十字路口信息过滤 | 建立"信息过载-信号过滤"的认知模型 |
| Ch3 | 社会叙事 | 电影院Lady Gaga铃声 | 建立"错误是可以预防的"共情 |
| Ch4 | 隐喻叙事 | 魔术师从帽子变出兔子 | 建立"设计不应像魔术一样让人猜测"的立场 |
| Ch5 | 日常叙事 | 桌面文件整理 | 建立"横向分类"的物理世界类比 |
| Ch6 | 焦虑叙事 | 低油量指示灯 | 建立"信息深度成为生存需要"的紧迫感 |
| Ch7 | 个人叙事 | 澳大利亚文化适应 | 建立"标签理解是跨文化问题"的第一人称证据 |
| Ch8 | 对比叙事 | Weilers V1 vs V2 (商场寻路) | 建立"信息控件决定体验成败"的对比证据 |
| Ch9 | 历史叙事 | QWERTY vs Dvorak键盘 | 建立"用户习惯>技术效率"的核心原则 |
| Ch10 | 悬念叙事 | 万圣节怪物按门铃 | 建立"好的交互控件应普遍可用"的门铃案例 |
| Ch11 | 幽默叙事 | "The Wheels on the Bus"改编 | 建立"输入者是多群体的"的轻松观察 |
| Ch12 | 地方叙事 | KU "Big Tooter"蒸汽哨声 | 建立"听觉信号可以持久且可靠"的历史证据 |
| Ch13 | 情感叙事 | Motorola StarTAC初恋 | 建立"设备是情感对象，但设计不为我"的认识论 |
| Preface | 方法论叙事 | 作者的10年研究历程 | 建立"这些模式不是编造的，是研究出来的"可信度 |

---

## 第二部分：实体总索引

### 2.1 人物实体总索引

| 编号 | 名称 | 首次出现位置 | 角色/贡献 | 跨章出现次数 |
|------|------|--------------|-----------|--------------|
| H01 | Steven Hoober | Preface | 第一作者 | 13+(全书) |
| H02 | Eric Berkman | Preface | 第二作者 | 13+(全书) |
| H03 | Christopher Alexander | Preface | Pattern Language创始人 | 2 |
| H04 | Donald Norman | Ch4 | Interaction Model (mental model, mapping, affordance, feedback) | 5+ |
| H05 | Colin Ware | Ch2 | Information entities/relationships/attributes | 2 |
| H06 | Peter Morville | Ch2 | Information Architecture principles | 2 |
| H07 | Kevin Lynch | Part I Intro | Wayfinding theory (Paths/Edges/Nodes/Landmarks/Districts) | 2 |
| H08 | Paul Fitts | Ch11/App D | Fitts's Law | 2 |
| H09 | Johannes Gutenberg | Ch1 | 欧洲活字印刷术 | 1 |
| H10 | Bi Sheng (毕昇) | Ch1 | 中国活字印刷术(11世纪) | 1 |
| H11 | Christopher Latham Sholes | Ch9 | QWERTY键盘发明者 | 1 |
| H12 | James Densmore | Ch9 | Sholes的投资人 | 1 |
| H13 | August Dvorak | Ch9 | Dvorak Simplified Keyboard | 1 |
| H14 | Mary Treseler | Preface | O'Reilly编辑 | 1 |
| H15 | Jennifer Tidwell | Preface | 技术评审(Designing Interfaces作者) | 1 |
| H16 | Dan Saffer | Preface | 技术评审(Designing Gestural Interfaces作者) | 1 |
| H17 | Josh Clark | Preface | 技术评审 | 1 |
| H18 | Bill Scott | Preface | 技术评审 | 1 |
| H19 | Christian Crumlish | Preface | 技术评审 | 1 |
| H20 | Frank Strong | Ch12 | KU校长(1912) | 1 |
| H21 | Luke Wroblewski | (间接) | Mobile First方法论 | 1 |

### 2.2 组织与机构总索引

| 编号 | 名称 | 类型 | 首次出现 |
|------|------|------|----------|
| O01 | O'Reilly Media | 出版社 | Preface |
| O02 | Digital Eskimo | 设计机构(Eric Berkman) | Preface |
| O03 | 4ourth Mobile | 设计机构(Steven Hoober) | Preface |
| O04 | Safari Books Online | 数字图书馆 | Preface |
| O05 | Mobile Marketing Association (MMA) | 行业标准组织 | Ch1 |
| O06 | Human Factors Society | 学术标准组织 | App D |
| O07 | University of Kansas | 大学 | Ch12 |
| O08 | University of Washington | 大学 | Ch9 |
| O09 | Bell System | 电信公司 | App A |
| O10 | E. Remington and Sons | 打字机制造商 | Ch9 |
| O11 | FCC (Federal Communications Commission) | 监管机构 | App A |
| O12 | Australian Communications and Media Authority | 监管机构 | Ch7 |
| O13 | US Navy Department / Procurement Division | 政府机构 | Ch9 |
| O14 | Surplus Exchange (Kansas City) | 电子回收机构 | Preface |
| O15 | Build-A-Bear Workshop | 零售企业(叙事) | Ch8 |

### 2.3 理论与框架总索引

| 编号 | 名称 | 核心命题 | 源章节 | 被引章节 |
|------|------|----------|--------|----------|
| T01 | Pattern Language | 模式是语言组成，非stencil | Preface | 全书 |
| T02 | Four Eras of Mobile | Voice→Paging→Network→General Computing | Preface | — |
| T03 | Five Mobile Characteristics | Small/Portable/Connected/Interactive/Contextually aware | Preface | Ch13, Ch8 |
| T04 | Eight Design Principles | Respect Data; Personal; Lives Precedence; All Contexts; Sensors; User Tasks; Consistency; Respect Information | Preface | 全书(每个Antipattern) |
| T05 | Common vs. Best Practice | 常见≠最佳 | Preface | 全书 |
| T06 | User-Centric Execution | Never walk away + Goals for everyone + OO principles + Polymorphism | Preface | — |
| T07 | Ware's Data Model | Entities/Relationships/Attributes | Ch2 | Ch2, Ch4 |
| T08 | Information Classification | Nominal/Ordinal/Ratio/Interval/Alphabetical/Geographical/Topical/Task/Audience/Social/Metaphor | Ch2 | Ch2, Ch5 |
| T09 | Hierarchy vs. Faceting | 信息架构的两种基本组织方式 | Ch2 | Ch5, Ch6 |
| T10 | Morville's IA Rules | Mutually exclusive categories / balance breadth-depth / max 2-3 levels | Ch2 | Ch6 |
| T11 | Norman's Interaction Model | Mental Model + Visibility (Mapping/Affordance/Constraints/Feedback) | Ch4 | Ch4, Ch10 |
| T12 | Distributed Cognition | Cognition is embodied, situated, distributed | Ch3 | Ch3 |
| T13 | Gestalt Principles | Closure/Continuity/Figure-Ground/Proximity/Relative Size/Similarity/Symmetry | Part I | Ch1, Ch2 |
| T14 | Wayfinding Theory | Paths/Edges/Nodes/Landmarks/Districts | Part I | Ch5 |
| T15 | Visual Hierarchy | Position→Size→Shape→Contrast→Color→Form | Part I | Ch1 |
| T16 | Fitts's Law | MT = a + b log2(D/W+1) | Ch11/App D | Ch11, App D |
| T17 | Visual Perception Model | Features→Patterns→Objects (3 stages) | App D | App D |
| T18 | Visual Angle Formula | VA = (3438)(length)/distance | App D | App C, Ch13 |
| T19 | Leaky Bucket Model | 人脑如漏桶，感觉输入被过滤 | App D | Ch3, App D |
| T20 | Transient Disability Framework | 永久残疾+临时环境限制=共性Accessibility | Ch12 | Ch12, Ch13 |

### 2.4 技术与模式总索引

见"专项一：全书76个模式总表"。

### 2.5 设备与平台总索引

| 编号 | 名称 | 类型 | 首次出现 |
|------|------|------|----------|
| D01 | Motorola StarTAC (1997) | Feature Phone (2G) | Ch13 |
| D02 | iPhone | Smartphone (touch) | Ch4 |
| D03 | Android devices | Smartphone (touch) | — |
| D04 | Feature phones (generic) | Feature Phone | Preface |
| D05 | iPad / Tablets | Tablet | Preface, Ch1 |
| D06 | eReaders | eReader | Preface |
| D07 | Nintendo DS | Portable Game | Preface |
| D08 | Xbox Kinect | Game Console (Remote Gestures) | Preface, Ch10 |
| D09 | Wii | Game Console (Kinesthetic) | Preface |
| D10 | Windows Tablet PC | Tablet PC (反例) | Preface |
| D11 | GPS navigation devices | Portable Navigation | Preface, Ch2 |
| D12 | Kiosks | Fixed Interactive Terminal | Preface, Ch3 |
| D13 | 5-way pad devices | Scroll-and-Select | Ch1, Ch10 |
| D14 | Capacitive touch devices | Touch | Ch1, Ch11 |
| D15 | ATM | Kiosk | Ch3 |
| D16 | Multitouch interactive table | Large Touch | Ch8 |

### 2.6 事件与时代总索引

| 编号 | 名称 | 时间 | 源章节 |
|------|------|------|--------|
| E01 | 中国雕版印刷 | 7世纪 | Ch1 |
| E02 | 毕昇活字印刷 | 11世纪 | Ch1 |
| E03 | Gutenberg印刷术革命 | 1440年 | Ch1 |
| E04 | QWERTY专利出售 | 1873年 | Ch9 |
| E05 | Remington No. 2发布(大小写) | 1878年 | Ch9 |
| E06 | Big Tooter首次使用 | 1912年3月25日 | Ch12 |
| E07 | Dvorak DSK专利 | 1936年 | Ch9 |
| E08 | US Navy Dvorak测试 | 1944年 | Ch9 |
| E09 | Bell MTS移动电话启动 | 1946年 | App A |
| E10 | IMTS改进版本启动 | 1963年 | App A |
| E11 | Christopher Alexander's Pattern Language出版 | 1970s | Preface |
| E12 | Donald Norman's "The Design of Everyday Things" | 1988 | Ch4 |
| E13 | 作者第一台手机(StarTAC) | 1997年 | Ch13 |
| E14 | Mobile First运动兴起 | 2009-2011 | Preface |
| E15 | 数字电视转频释放频谱 | 2009-2011 | App A |
| E16 | 本书第一版出版 | 2011年11月 | Preface |
| E17 | 澳大利亚FNN编号制度 | 当代 | Ch7 |
| E18 | 作者Eric Berkman移居澳大利亚 | 当代 | Ch7 |
| E19 | Weiler家族商场寻路(V1/V2叙事) | 虚构 | Ch8 |
| E20 | Halloween trick-or-treat叙事 | 虚构 | Ch10 |
| E21 | "Wheels on the Bus"改编叙事 | 虚构 | Ch11 |

---

## 第三部分：交叉引用索引

### 3.1 被引用最多的模式(Top 10跨章引用)

| 排名 | 模式名称 | 被引用次数(估计) | 引用其的章节 |
|------|----------|-----------------|-------------|
| 1 | Scroll | 15+ | Ch1, Ch2, Ch5, Ch8, Ch10, Ch11... |
| 2 | Pop-Up | 10+ | Ch3, Ch4, Ch6, Ch7, Ch8, Ch11... |
| 3 | Vertical List | 10+ | Ch1, Ch2, Ch4, Ch6, Ch7... |
| 4 | Confirmation | 8+ | Ch3, Ch4, Ch11, Ch12... |
| 5 | Notifications | 8+ | Ch1, Ch7, Ch12, Ch13... |
| 6 | Tabs | 7+ | Ch1, Ch5, Ch6, Ch8... |
| 7 | Input Areas | 6+ | Ch9, Ch10, Ch11... |
| 8 | On-Screen Gestures | 6+ | Ch8, Ch10, Ch11, Ch13... |
| 9 | Autocomplete & Prediction | 5+ | Ch8, Ch9, Ch11... |
| 10 | Orientation | 5+ | Ch10, Ch12, Ch13... |

### 3.2 章节间最强关联对

| 关联对 | 关联强度 | 关联性质 |
|--------|----------|----------|
| Ch5 (Lateral Access) ↔ Ch6 (Drilldown) | 最强 | 横向-纵向导航互补 |
| Ch2 (Display) ↔ Ch8 (Info Controls) | 极强 | 信息展示-信息控制 |
| Ch4 (Revealing) ↔ Ch6 (Drilldown) | 极强 | 揭示机制-导航触发 |
| Ch9 (Text Input) ↔ Ch11 (Input & Selection) | 极强 | 文本输入-表单接收 |
| Ch3 (Control) ↔ Ch4 (Revealing) | 强 | Confirmation的Pop-Up载体 |
| Ch10 (Interactive) ↔ Ch12 (Audio) | 强 | 手势反馈-Haptic反馈 |
| Ch12 (Audio) ↔ Ch13 (Screens) | 强 | 非视觉通道-LED/亮度 |
| Ch1 (Composition) ↔ Ch5 (Lateral) | 强 | 页面容器-导航菜单 |
| Ch7 (Labels) ↔ Ch11 (Input) | 中强 | 标签化-表单标签 |
| App D (Human Factors) ↔ All Ch1-13 | 基础 | 科学的生理/认知基础 |

---

## 第四部分：报告清单

| 文件编号 | 文件名 | 覆盖内容 | 状态 |
|----------|--------|----------|------|
| 00 | 00_整体分析报告.md | 全书总纲 | 已完成 |
| 01 | 01_Preface_分析报告.md | Preface + Part I Intro | 已完成 |
| 02 | 02_Chapter01_Composition_分析报告.md | Ch1: 10 patterns | 已完成 |
| 03 | 03_Chapter02_Display of Information_分析报告.md | Ch2: 10 patterns | 已完成 |
| 04 | 04_Chapter03_Control and Confirmation_分析报告.md | Ch3: 5 patterns | 已完成 |
| 05 | 05_Chapter04_Revealing More Information_分析报告.md | Ch4: 4 patterns | 已完成 |
| 06 | 06_Chapter05_Lateral Access_分析报告.md | Ch5: 5 patterns | 已完成 |
| 07 | 07_Chapter06_Drilldown_分析报告.md | Ch6: 6 patterns | 已完成 |
| 08 | 08_Chapter07_Labels and Indicators_分析报告.md | Ch7: 5 patterns | 已完成 |
| 09 | 09_Chapter08_Information Controls_分析报告.md | Ch8: 4 patterns | 已完成 |
| 10 | 10_Chapter09_Text and Character Input_分析报告.md | Ch9: 5 patterns | 已完成 |
| 11 | 11_Chapter10_General Interactive Controls_分析报告.md | Ch10: 9 patterns | 已完成 |
| 12 | 12_Chapter11_Input and Selection_分析报告.md | Ch11: 4 patterns | 已完成 |
| 13 | 13_Chapter12_Audio and Vibration_分析报告.md | Ch12: 5 patterns | 已完成 |
| 14 | 14_Chapter13_Screens Lights and Sensors_分析报告.md | Ch13: 4 patterns | 已完成 |
| 15 | 15_AppendixA_Mobile Radiotelephony_分析报告.md | App A | 已完成 |
| 16 | 16_AppendixB_Design Templates and UI Guidelines_分析报告.md | App B | 已完成 |
| 17 | 17_AppendixC_Mobile Typography_分析报告.md | App C | 已完成 |
| 18 | 18_AppendixD_Human Factors_分析报告.md | App D | 已完成 |
| NN | NN_专项报告与实体总索引.md | 四个专项+全局实体索引 | 已完成 |

共计：1份总报告 + 1份Preface报告 + 13份章节报告 + 4份附录报告 + 1份专项索引报告 = **20份报告**

---

*本报告是《Designing Mobile Interfaces》分析报告系列的总索引文件，包含四个专项报告(模式总表/理论框架依赖/叙事结构/交叉引用)和全局实体总索引(人物/组织/理论/模式/设备/事件六类)。*
*报告语言：中文。L###为段落级编号。如需检索某具体模式的各章分析，请使用文件名编号(00-NN)配合L###交叉引用。*
