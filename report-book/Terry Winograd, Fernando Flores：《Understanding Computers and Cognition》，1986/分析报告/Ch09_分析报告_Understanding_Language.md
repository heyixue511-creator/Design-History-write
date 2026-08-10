# Ch09 分析报告：Understanding Language（理解语言）

## 一、章节定位与功能

- **行号范围**：L1794–L2088（含 9.1 Artificial intelligence and language understanding L1805–L1855；9.2 The problem of background L1856–L1920；9.3 Understanding as pattern recognition L1921–L1991；9.4 What does it mean to understand? L1992–L2088）
- **定位**：Part II 的纵深章——把第 8 章"计算机不能智能"的论证落实到自然语言处理。
- **功能**：逐例分析从机器翻译到 SHRDLU、ELIZA、SAM、BORIS 的程序，论证"计算机不能理解语言"，并阐明"理解"是承诺性谓词。

## 二、结构分析

1. **9.1 AI 与语言理解**（L1805–L1855）：机器翻译失败→AI 转向"表征+推理"范式；SHRDLU 对话实例；理性主义语言理解模型的三假设。
2. **9.2 背景问题**（L1856–L1920）：字面意义/背景分离不可维持；"bachelor"定义失败；对说话者/听者心理状态建模的扩展及其任意性。
3. **9.3 理解作为模式识别**（L1921–L1991）：框架/脚本/模式/原型；Minsky 框架理论；默认值与缺省推理；非单调逻辑、资源受限推理；框架方案的两类结局与失明局限。
4. **9.4 "理解"意味着什么**（L1992–L2088）：从"时钟程序"到 ELIZA 到 SAM/BORIS 到 Macbeth 类比程序逐级考察；"理解即承诺"结论；对实际应用的缓和立场。

## 三、内容分析

- **三假设模型**（L1813–L1823）：自然语言句子对应世界事实；可建形式表征系统（对应+推理）；"理解"即表征的操纵。
- **SHRDLU**（L1828–L1854）：完整对话样例（L1832–L1844）；指代消解与对话结构推理；但用 ad hoc 方式处理对话知识。
- **bachelor 案例**（L1881–L1884）：无任何长度的"核对清单"能覆盖"独身者"的适用条件；"问题在每个陈述背后"（Gadamer，L1884）。
- **框架理论**（L1921–L1954）：Minsky 框架引文（L1926–L1933）；房间视觉框架例（L1934–L1935）；Schank 记忆/类比引文（L1948–L1951）；"框架方案从诠释学方向接近意义"（L1952–L1953）但未解决背景问题。
- **缺省与非单调推理的困境**（L1961–L1971）：何时算"典型"无法判定；规则细化即不再是缺省。
- **资源受限推理**（L1972–L1978）：有限处理后的跳跃结论；"绕过逻辑"（Minsky，L1976）；形式规则相对于系统结构。
- **两类框架程序**（L1985–L1989）：只对特定例子有效，或与普通程序等价；框架不逃脱失明。
- **程序四连**（L1996–L2054）：时钟程序（L1997–L1999）→模式匹配（L2000–L2004）→ELIZA/DOCTOR（L2004–L2008）→脚本 SAM（L2009–L2014）；各程序"理解"宣称的有限性。
- **BORIS 与 Macbeth 类比程序**（L2033–L2054）：M-SEX、M-ADULTERY、TAU-RED-HANDED 等"剧本动物园"；Macbeth 的微型表征列表（L2041–L2052）——"人类宽度"只是微型世界幻觉。
- **理解即承诺**（L2057–L2079）：说"X 理解 Y"即承认 X 进入理解所蕴涵的承诺；计算机不能承诺，故程序是媒介而非理解者（L2068–L2071）。
- **TEIRESIAS 与元知识**（L2072–L2075）：元表征同样有限；Hofstadter 的"怪圈"直觉未被支持（L2075–L2076）。
- **实际应用缓和**（L2080–L2088）：批判"理解"的常见理解，但不谴责技术本身；用户须认识到两点——语言结构被操纵但未被理解、响应体现特定表征及其失明。

## 四、逻辑梳理

机器翻译失败促使 AI 转向表征+推理（9.1）→ 但字面意义论因背景不可分离而崩溃（9.2）→ 框架/模式识别试图用预存结构解释输入，仍未解决"何为典型/相关"的背景问题（9.3）→ 对实际程序的考察表明"理解"只能按承诺来理解，而计算机无承诺能力（9.4）。

## 五、材料使用方式

- **程序实证**：SHRDLU 对话全文（L1832–L1844）、ELIZA 模式（L2004–L2008）、SAM 脚本（L2009–L2014）、BORIS 结构（L2036–L2038）、Macbeth 表征（L2041–L2052）。
- **哲学引文**：Searle（L948–L951 于第 5 章）、Gadamer《Philosophical Hermeneutics》（L1870–L1873）、Minsky（L1926–L1933、L1976）、Schank（L1948–L1951）、Weizenbaum《Computer Power and Human Reason》（L1862–L1863、L2007–L2008）、McCarthy（L1865–L1867）、Hofstadter《Gödel, Escher, Bach》（L2075）、Fodor（L1826）。
- **个人回顾**：Winograd 引自己的《When will computers understand people?》（L1897–L1898）。
- **Newsweek 报道**（L1993）、Schank-Riesbeck 声明（L1993、L2014）。

## 六、论辩与阐述方法

- **程序阶梯法**：从最简单的时钟程序逐级上升至 BORIS，每级都证明"扩大模式集合不改变本质"。
- **微型世界揭露**：反复揭示程序看起来"宽"实则"窄"（L2030–L2054）。
- **承诺语义学收束**：以"理解=承诺"判据作最终裁决。
- **平衡叙述**：9.4 明确"不是对技术工作的谴责"（L2081–L2082）。

## 七、语言文风摘录（附行号）

- "Our position, in accord with the preceding chapters, is that computers cannot understand language."（L1800）
- "When we squeeze out the role of interpretation, we are left not with the essence of meaning, but with the shell."（L1876）
- "Understanding is not a fixed relationship between a representation and the things represented, but is a commitment to carry out a dialog within the full horizons of both speaker and hearer…"（L2079）
- "The apparent human breadth of the program is like that of ELIZA."（L2038）
- "…we are engaging in a particularly dangerous form of blindness if we see the computer—rather than the people who program it——as doing the understanding."（L2071）

## 八、实体清单（附行号证据）

**人物**：Weizenbaum（L1862、L2007）、McCarthy（L1865–L1866）、Gadamer（L1870–L1874）、Minsky（L1926、L1976）、Schank（L1948–L1951）、Riesbeck（L1993、L2014）、Hofstadter（L2075）、Fodor（L1826）、Moore（L1922）、Newell（L1922）、Bobrow（L1922）、Norman（L1922）、Winston（L1922 提及 prototypes）、Winograd（L1828、L1897）。

**著作/作品**：Winograd《Understanding Natural Language》（L1828、L3291）、Weizenbaum《Computer Power and Human Reason》（L1862–L1863、L2007–L2008、L3289）、McCarthy《An unreasonable book》（L1865–L1866、L3218）、Minsky《A framework for representing knowledge》（L1926–L1933、L3222）、Schank《Language and memory》（L1948–L1951、L3257）、Schank & Abelson《Scripts Plans Goals and Understanding》（L1922、L3258–L3259）、Schank & Riesbeck《Inside Computer Understanding》（L1993、L2014、L3260）、Moore & Newell（beta structures，L1922）、Bobrow & Norman（schemas，L1922）、Bobrow & Winograd（prototypes，L1922）、Hofstadter《Gödel, Escher, Bach》（L2075、L3164）、Fodor《Methodological solipsism…》（L1826、L3116–L3117）、Gadamer《Philosophical Hermeneutics》（L1870–L1873）、Winograd《When will computers understand people?》（L1897–L1898、L3292）。

**概念**：机器翻译（machine translation，L1806）、自然语言理解（language understanding，L1805）、字面意义（literal meaning，L1861）、背景（background，L1856–L1920）、框架（frame，L1922、L1926–L1933）、脚本（script，L1922、L2009–L2014）、模式（schema，L1922）、原型（prototype，L1922、L1937–L1945）、缺省（default，L1961–L1964）、非单调推理（non-monotonic reasoning，L1964）、资源受限推理（resource-limited reasoning，L1972–L1978）、微型世界（microworld，L2030）、元知识（meta-knowledge，L2072–L2073）、理解即承诺（understanding as commitment，L2057–L2079）、意向立场（L2061）。

**机构**：Cognitive Systems, Inc.（第 10 章广告，L2141 于第 10 章）。

**地点**：无。

**事件**：1960 年代中期机器翻译失败（L1805–L1807）。

## 九、与前后章关联

- **前承第 5、8 章**：9.4 依赖第 5 章承诺理论与第 8 章"心理谓词预设自主行动者"（L2057–L2061）。
- **后承第 10 章**：9.4 末指明实际应用在第 10 章考察（L2083）。
- **后承第 12 章**：9.4 的"媒介"观在第 12.3 系统域讨论中延续（L2979–L2982）。
