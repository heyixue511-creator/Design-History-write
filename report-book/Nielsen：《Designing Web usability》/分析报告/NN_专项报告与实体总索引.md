# 《Designing Web Usability》专项报告与实体总索引

## L0 本索引说明

本文件为《Designing Web Usability: The Practice of Simplicity》分析报告体系的**专项报告索引**与**全书实体总索引**。所有实体按其唯一编号（L###）统一编排，每种实体标注其出现章节和简要说明。专项报告部分提供跨章节主题的深度分析。

---

# 第一部分：专项报告

## ZX1 专项报告一：Nielsen论证方法论研究

### L1 Nielsen的论证武器库

Jakob Nielsen在本书中运用了极为丰富的论证方法，可归纳为以下十种核心策略：

| 序号 | 方法 | 典型应用 | 代表性章节 |
|:---|:---|:---|:---|
| 1 | 用户测试数据引用 | "79%扫描"、"42%/26%成功率" | Ch1, Ch3, Ch4 |
| 2 | 经济成本计算 | 坏标题=$5,000浪费 | Ch3 |
| 3 | 受控实验对比 | Nebraska文本五种写法 | Ch3 |
| 4 | 真实网站截图批评 | MapQuest, Pathfinder, Hertz | Ch2, Ch3 |
| 5 | 时间序列追踪 | MapQuest 1997→1999 | Ch2 |
| 6 | 反例-正例对照 | "Click Here"→信息性锚文本 | Ch2 |
| 7 | 类比论证 | 17楼商店、戏剧服装、互联网之链 | Ch1, Ch3, Ch8 |
| 8 | 隐喻贯穿 | HOME-RUN、副总裁按钮 | Ch4, Ch9 |
| 9 | 权威引用 | Tufte, Metcalfe, Norman | Ch2, Ch8 |
| 10 | 匿名用户原话 | "70 emails and 50 voicemails a day" | Ch3 |

### L2 论证风格的三层结构

Nielsen的说服策略遵循经典修辞学三分法：
- **Ethos（人格威信）**：400+用户观察、Sun Microsystems杰出工程师、Nielsen Norman Group创始人、38项美国专利。
- **Pathos（情感诉求）**：制造紧迫感（"你的竞争对手只需一次点击"）、道德召唤（"Let's design a world that will be good for us"）。
- **Logos（理性论证）**：数据驱动（百分比、像素计数、成本计算）、逻辑链条（从元命题到具体推论）。

### L3 数字的修辞力量

Nielsen对数字的使用是其文风的标志性特征：
- **精确数字**：480,000像素、25%阅读速度差异、$5,000/标题。
- **比例数字**：79%扫描、42%成功率、124%提升。
- **预测数字**：10亿用户（2010）、2亿站点（2005）、500亿页面（2005）。
- **对比数字**：6倍屏幕差异（GUI）vs.100倍（Web）、20K vs.2M页（Sun）。

## ZX2 专项报告二：全书核心概念体系图谱

### L1 概念层级

```
L0: 元概念 — Simplicity（简洁性）
    │
    ├── L1: 用户行为规律
    │   ├── 扫描而非阅读（79%）
    │   ├── 信息觅食（Information Foraging）
    │   ├── 注意力经济（Attention Economy）
    │   └── 用户控制导航（The User Controls Navigation）
    │
    ├── L1: 设计方法论
    │   ├── 可用性工程（Usability Engineering）
    │   ├── 折扣可用性工程（Discount Usability Engineering）
    │   ├── 渐进删除测试（Remove One at a Time）
    │   └── 设计达尔文主义（Design Darwinism）
    │
    ├── L1: 技术原则
    │   ├── 意义与表现分离
    │   ├── 跨平台不可预测性（WYSIWYG Is Dead）
    │   ├── Data Ink vs. Chart Junk
    │   └── ALT属性与语义HTML
    │
    ├── L1: 架构原则
    │   ├── 用户中心结构（vs.公司中心结构）
    │   ├── 导航三问（Where am I? / Where have I been? / Where can I go?）
    │   ├── 主页三功能（目录+新闻+搜索）
    │   └── 广度优于深度
    │
    └── L1: 综合框架
        ├── HOME-RUN（七要素）
        ├── 超越现实（Better Than Reality）
        └── Metcalfe's Law（网络价值=n²）
```

### L2 概念之间的关系

| 上游概念 | 下游概念 | 关系类型 |
|:---|:---|:---|
| 简洁性 | 所有具体设计建议 | 元原则→派生规则 |
| 注意力经济 | 扫描行为、50%文本规则 | 理论→行为解释→设计规则 |
| Metcalfe's Law | 用户选择权、竞争门槛 | 技术规律→商业逻辑 |
| 信息觅食 | 可扫描性、链接设计 | 行为理论→设计原则 |
| 反Mac界面 | 信息家电、浏览器死亡 | 理论预测→产品形态 |

## ZX3 专项报告三：Nielsen预测的验证（1999→2026）

### L1 已验证的预测

| 预测内容 | 预测时间 | 实际发生 | 准确度 |
|:---|:---|:---|:---|
| 10亿Web用户 | 约2010 | 2010年约20亿互联网用户 | 偏高 |
| 2007年屏幕可读性达纸张水平 | 2007 | Kindle(2007)/Retina(2010) | 接近 |
| 信息家电兴起 | 2000-2005 | iPhone(2007)/智能手机爆发 | 延迟但正确 |
| CSS成为标准 | 进行中 | CSS 2.1(2011)/CSS3 | 正确 |
| 北美用户比例下降至50%以下 | 2000-2005 | 2000年代中期确实发生 | 正确 |
| 移动作为第三杀手应用 | 2000s | 智能手机革命 | 正确 |
| 远程工作改变地产价值 | 数十年 | COVID-19加速(2020) | 正确 |
| 隐私成为奢侈品 | 数十年 | 数字排毒运动、隐私付费 | 正确 |
| 传统全职就业变化 | 数十年 | 零工经济(Gig Economy) | 正确 |

### L2 未被验证或部分验证的预测

| 预测内容 | 预测时间 | 实际 | 分析 |
|:---|:---|:---|:---|
| 书籍在2007年消亡 | 2007 | 纸质书仍存在 | 技术→文化转型慢于预期 |
| 浏览器死亡 | 2000s | Chrome(2008)反而让浏览器更重要 | 移动端部分正确 |
| 汤加王国成为最富国家 | 数十年 | 未发生 | 推测性预测 |
| 美国邮政被解散 | 数十年 | 仍在运营 | 低估制度惯性 |
| 反Mac界面成为主流 | 10-20年 | iOS/Android有反Mac元素但不完全 | 部分验证 |

### L3 被低估的趋势

| 未充分预见 | 当前现实 | 影响评估 |
|:---|:---|:---|
| 搜索引擎的进化 | Google语义搜索、AI搜索引擎 | 搜索建议已过时 |
| 社交媒体 | Facebook/Twitter/TikTok | 完全缺失 |
| 移动优先设计 | 移动端流量超桌面 | 仍以桌面为中心 |
| 响应式设计 | 2010年Ethan Marcotte提出 | 接近但未明确提出 |
| AI与机器学习 | ChatGPT等生成式AI | 完全未预见 |
| 应用商店生态 | iOS App Store(2008) | 未预见 |

---

# 第二部分：实体总索引

## S1 人物实体索引（按姓氏字母序）

| L### | 姓名 | 身份/角色 | 出现章节 | 关键贡献/关联 |
|:---|:---|:---|:---|:---|
| L803 | Bob Metcalfe | 以太网发明者 | Ch4, Ch8 | Metcalfe's Law（网络价值=n²） |
| L207 | Bruce Tognazzini | Apple前UI专家 | Ch2 | GUI设计传统 |
| L909 | Charles Dickens | 文学家 | Ch9 | "最好/最坏的时代"引用 |
| L108 | Donald A. Norman | Nielsen Norman Group联合创始人 | Ch1, Ch8 | "The Invisible Computer" |
| L801 | Don Gentner | Sun Microsystems研究员 | Ch8 | 反Mac界面合作者 |
| L206 | Edward Tufte | 数据可视化权威 | Ch2 | Data Ink / Chart Junk |
| L802 | Donald A. Norman(重复) | — | Ch8 | 见L108 |
| L804 | Bill Gates | 微软创始人 | Ch6, Ch8 | 书网站可访问性丑闻；Encarta 2020预测 |
| L107 | Jakob Nielsen | 作者 | 全书 | 第一人称叙述者 |
| L408 | Jared Spool | 可用性研究者 | Ch4 | 42%成功率研究 |
| L301 | John Morkes | 合作研究者 | Ch3 | Nebraska文本实验 |
| L409 | Mark Hurst | 合作研究者 | Ch4 | 26%成功率研究 |
| L302 | Mike Tucker | Baxter HR VP | Ch3 | Baxter欢迎页案例 |
| L805 | Rich Gold | Xerox PARC艺术家 | Ch8 | "Drawing a Computer" |
| L108 | Steve Outing | 新闻技术专栏作家 | Ch2, Ch3 | "Stop the Presses!"专栏 |
| L109 | 400名被测用户 | 可用性测试参与者 | Ch1 | 全书实证基础 |
| L910 | 8900名Forrester受访者 | 调查样本 | Ch9 | 复访驱动因素数据 |

## S2 网站/公司实体索引（按名称字母序）

| L### | 名称 | URL | 出现章节 | 上下文 |
|:---|:---|:---|:---|:---|
| L403 | Apple Store | — | Ch4 | 假期关闭主页反例 |
| L401 | BatteryPlanet | www.batteryplanet.com | Ch4 | 主页误导性第一印象 |
| L304 | Baxter | — | Ch3 | Web招聘写作案例 |
| L305 | DisCopyLabs | www.discopylabs.com | Ch3 | 拼写错误反例 |
| L404 | Expedia | — | Ch4 | 搜索入口正例 |
| L306 | Hertz | www.hertz.com | Ch3 | 保险信息扫描案例 |
| L307 | IBM ThinkPad | — | Ch3 | 产品描述模糊反例 |
| L201 | MapQuest | www.mapquest.com | Ch2 | 屏幕空间经典分析 |
| L205 | Mercedes-Benz | — | Ch2 | 概念车联网案例 |
| L308 | Nebraska tourism | — | Ch3 | 文本写法受控实验 |
| L202 | Pathfinder | www.pathfinder.com | Ch2 | 密度过高反例 |
| L203 | Quote.com | www.quote.com | Ch2 | 字体问题案例 |
| L905 | RiteAid | www.riteaid.com | Ch9 | 邮件可用性反例 |
| L402 | Saturn | — | Ch4 | 神秘问号图标 |
| L405 | Serco | www.serco.com | Ch4 | 主页过度简洁 |
| L501 | Sun Microsystems | — | Ch5 | 20K外部/2M内部页 |
| L701 | Yahoo! | — | Ch7 | 多国本地化案例 |
| L702 | Yahoo! Germany | — | Ch7 | 德国版对比 |
| L204 | ZDNet | www.zdnet.com | Ch2 | 链接分析 |
| L406 | Cosmopolitan | www.cosmomag.com | Ch4, Ch9 | 主页=杂志封面 |
| L907 | Cubeland | www.cubeland.com | Ch9 | Windows 98风格主页 |

## S3 技术标准/协议/格式索引

| L### | 名称 | 类别 | 出现章节 | 说明 |
|:---|:---|:---|:---|:---|
| L605 | ALT attribute | HTML属性 | Ch2, Ch3, Ch6 | 图像替代文本 |
| L209 | HTML | 标记语言 | Ch1, Ch2, Ch6 | 意义编码的基础 |
| L210 | CSS (Style Sheets) | 样式语言 | Ch2 | 分离意义与表现 |
| L211 | HTTP Keep-Alive | 网络协议 | Ch2 | 加速页面加载 |
| L212 | `<NOFRAMES>` | HTML标签 | Ch2 | 框架降级 |
| L310 | GIF/JPEG/PNG | 图像格式 | Ch3 | 图像优化 |
| L311 | Streaming video | 媒体技术 | Ch3 | 流媒体vs.可下载 |
| L312 | Plug-ins | 浏览器扩展 | Ch3 | 多媒体依赖 |
| L711 | HTML int'l characters | 字符编码 | Ch7 | ü, é, ø支持 |
| L607 | Screen readers | 辅助技术 | Ch6 | 盲人用户工具 |
| L608 | `<H1>`-`<H6>` | HTML标题 | Ch3, Ch6 | 页面结构标记 |
| L414 | Archival URLs | URL设计 | Ch4 | URL持久性 |

## S4 设计原则/方法论/法则索引

| L### | 名称 | 类别 | 出现章节 | 核心表述 |
|:---|:---|:---|:---|:---|
| L815 | Simplicity Principle | 元原则 | 全书 | Simplicity always wins over complexity |
| L214 | Data Ink / Chart Junk | 视觉原则 | Ch2 | 去除一切非必要视觉元素 |
| L215 | "Remove one at a time" | 方法论 | Ch2 | 渐进删除测试 |
| L216 | 50%/80% content rule | 设计规则 | Ch2 | 内容占页面50%-80% |
| L217 | WYSIWYG is dead | 设计哲学 | Ch2 | 放弃像素级控制 |
| L313 | 50% text rule | 写作规则 | Ch3 | 文本量为印刷品50% |
| L314 | Scannability | 写作原则 | Ch3 | 为扫描而写 |
| L315 | Information Foraging | 行为理论 | Ch3 | 用户如觅食般浏览信息 |
| L316 | Attention Economy | 经济概念 | Ch3 | 用户注意力是最稀缺资源 |
| L419 | Design Creationism vs. Darwinism | 设计哲学 | Ch4 | 一次性设计vs.持续演化 |
| L420 | The Vice-Presidential Button | 讽刺概念 | Ch4 | 组织中心主义结构 |
| L421 | User-Centered Structure | 结构原则 | Ch4 | 结构匹配用户任务 |
| L422 | Navigation三问 | 导航框架 | Ch4 | 我在哪/去过哪/能去哪 |
| L507 | Employee-centered design | 设计原则 | Ch5 | 内联网以员工为中心 |
| L508 | Average vs. Marginal Costs | 经济分析 | Ch5 | 生产力ROI计算 |
| L620 | Encode meaning, not appearance | HTML哲学 | Ch6 | 标记意义而非外观 |
| L621 | Relative font sizes | 可访问性 | Ch6 | 相对而非绝对字体 |
| L622 | Staged accessibility | 实施策略 | Ch6 | 分阶段合规 |
| L623 | High contrast | 可访问性 | Ch6 | 前景/背景高对比 |
| L901 | HOME-RUN | 综合框架 | Ch9 | 七要素设计模型 |
| L912 | Repeat traffic as metric | 度量原则 | Ch9 | 复访是唯一成功标准 |
| L914 | Go beyond reality | 设计哲学 | Ch9 | 超越物理世界限制 |

## S5 学术/理论概念索引

| L### | 名称 | 学科领域 | 出现章节 | 说明 |
|:---|:---|:---|:---|:---|
| L113 | Web usability | 人机交互 | Ch1 | 全书核心主题 |
| L806 | Metcalfe's Law | 网络理论 | Ch4, Ch8 | 网络价值随节点数平方增长 |
| L807 | Anti-Mac User Interface | 界面设计 | Ch8 | 反转Macintosh设计原则 |
| L808 | The Invisible Computer | 普适计算 | Ch8 | Norman的概念 |
| L317 | 25% slower screen reading | 人因工程 | Ch3 | 屏幕阅读速度研究 |
| L319 | 300 dpi screen readability | 显示技术 | Ch3 | 高分辨率屏幕可读性 |
| L116 | Usability engineering | 软件工程 | Ch1 | 可用性工程方法论 |
| L506 | Directory/Search/News | 信息架构 | Ch5 | 内联网三大基础设施 |

## S6 组织/机构索引

| L### | 名称 | 类型 | 出现章节 | 角色 |
|:---|:---|:---|:---|:---|
| L119 | Nielsen Norman Group | 咨询公司 | Ch1 | 作者公司 |
| L120 | Sun Microsystems | 技术公司 | Ch1, Ch5 | 作者前雇主 |
| L121 | IBM User Interface Institute | 研究机构 | Ch1 | 作者前雇主 |
| L601 | W3C/WAI | 标准组织 | Ch6 | Web可访问性标准 |
| L602 | Trace Center | 研究机构 | Ch6 | 辅助技术信息 |
| L603 | NCAM | 媒体组织 | Ch6 | Web Access Symbol |
| L604 | IBM | 技术公司 | Ch6 | Home Page Reader |
| L423 | Forrester Research | 市场研究 | Ch4, Ch9 | 用户调查数据 |
| L814 | Xerox PARC | 研究机构 | Ch8 | GUI发源地 |
| L815 | Carnegie Mellon HomeNet | 学术研究 | Ch8 | 家庭互联网使用研究 |

---

# 第三部分：各章分析报告索引

| 序号 | 文件名 | 章节 | 核心分析焦点 |
|:---|:---|:---|:---|
| 00 | 00_整体分析报告.md | 全书 | 全书结构、论证体系、方法论、历史坐标 |
| 01 | 01_Preface_前言分析报告.md | Preface | 媒介选择论证、两卷本策略、书籍消亡预测 |
| 02 | 02_Ch1_引言分析报告.md | Ch1 Introduction | 付费时序倒置、六类根本错误、工程vs.艺术 |
| 03 | 03_Ch2_页面设计分析报告.md | Ch2 Page Design | 屏幕空间审计、跨平台、链接设计、框架批判 |
| 04 | 04_Ch3_内容设计分析报告.md | Ch3 Content Design | Web写作实验、扫描行为、注意力经济 |
| 05 | 05_Ch4_网站设计分析报告.md | Ch4 Site Design | 导航三问、主页设计、搜索、URL、副总裁按钮 |
| 06 | 06_Ch5_内部网设计分析报告.md | Ch5 Intranet Design | Intranet/Internet/Extranet三界分异 |
| 07 | 07_Ch6_可访问性分析报告.md | Ch6 Accessibility | 五类残疾、ALT属性、搜索引擎=盲用户 |
| 08 | 08_Ch7_国际化使用分析报告.md | Ch7 International Use | I18N vs. L10N、域名策略、国际用户测试 |
| 09 | 09_Ch8_未来预测分析报告.md | Ch8 Future Predictions | 反Mac界面、Metcalfe's Law、信息家电、长期预测 |
| 10 | 10_Ch9_结论分析报告.md | Ch9 Conclusion | HOME-RUN模型、超越现实、鼠标投票 |

---

# 第四部分：实体编号体系说明

## L### 编号规则

- **L0xx**：前言（Preface）实体
- **L1xx**：第一章（Introduction）实体
- **L2xx**：第二章（Page Design）实体
- **L3xx**：第三章（Content Design）实体
- **L4xx**：第四章（Site Design）实体
- **L5xx**：第五章（Intranet Design）实体
- **L6xx**：第六章（Accessibility）实体
- **L7xx**：第七章（International Use）实体
- **L8xx**：第八章（Future Predictions）实体
- **L9xx**：第九章（Conclusion）实体

## 实体分类代码

| 首数字后第二位 | 实体类别 |
|:---|:---|
| x0x | 人物 |
| x1x | 网站/公司/产品 |
| x2x | 技术标准/协议/格式 |
| x3x | 设计原则/方法论 |
| x4x | 学术/理论概念 |
| x5x | 组织/机构 |
| x6x | 书籍/出版物 |
| x7x | 其他（跨类别或未归类） |

---

*索引编制日期：2026年8月*
*涵盖范围：《Designing Web Usability》全书（Preface至Chapter 9）及其完整分析报告体系*
