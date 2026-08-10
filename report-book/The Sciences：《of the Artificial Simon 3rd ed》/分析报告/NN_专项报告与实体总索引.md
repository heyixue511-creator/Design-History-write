# NN 专项报告与实体总索引

> 本书：Herbert A. Simon, *The Sciences of the Artificial*, 3rd ed. (MIT Press, 1996)。分析基准：`00-book\The Sciences：《of the Artificial Simon 3rd ed》.md`（4197 行）。证据行号为该文件实际行号。

---

# 第一部分 专项报告

## 一、语言总貌

1. **英语学术散文，第一人称主导**：全书以"我"的视角推进论证，兼具讲座语气与书面论文体。典型句式："I should like to...";"Let me...";"It is the thesis of this chapter that..."（L1428）；"I shall argue..."（L2477）。
2. **跨学科术语并置**：经济学（utility, Pareto optimality）、心理学（chunk, short-term memory）、计算机科学（program, symbol system, heuristic search）、系统科学（feedback, hierarchy, near decomposability）术语相互翻译，形成统一语汇（L433、L872、L2332）。
3. **格言与荷兰谚语开篇**：章首以斯台文荷兰文题辞"Wonder, en is gheen wonder"（L186—L188）确立"奇妙而非不可解"的基调；全书常引拉丁语性质格言与英语俗语（L311）。
4. **数学公式与图示的叙事化处理**：数学以 LaTeX 形式保留（密码算术 L762、热矩阵 L2342），图与表格作为论证证据（图1—图7）。
5. **白话与学术平衡**：说理中插入日常经验（"telephone directory constants" L884、厨柜空空的童谣 L2465），使抽象概念可感。

## 二、文风特征

1. **比喻密度高**：蚂蚁路径（L725—L739）、钟表匠（L2228—L2232）、干草堆找针（L1512）、雪片般的城市（L537）、长暗厅（L1908）、油画（L1980）、心理橱窗购物（L1996）、空中吊钩—摩天楼（L361—L363）、点击保险箱（L2296）。
2. **让步—限定—推进的三段式**：如 L203（承认夸大再辩护）、L1058（先承认并行感官再限定串行符号处理）、L1120（先给数字再说不必认真）。
3. **设问驱动结构**：各章以问题句开启小节或推进论证："How can a simulation ever tell us anything that we do not already know?"（L337）；"What is a good strategy in this game?"（L1640）；"Who is the client?"（L1846）。
4. **对偶与对称**：自然/人工、内/外环境、状态描述/过程描述、实质理性/程序理性、优化/满意化——以二元对照组织思想（L223、L2471—L2475、L453）。
5. **反讽与警句**："The marvel is not that markets optimize (they don't) but that they often clear."（L533）；"Modal logics can be shown to exist in the same way that giraffes can namely, by exhibiting some of them."（L1456）。

## 三、修辞方式

| 修辞类型 | 例 | 证据行号 |
| --- | --- | --- |
| 比喻/类比 | 蚂蚁→人；钟表匠→演化；雪花→城市 | L725—L739、L2228、L537 |
| 反诘 | "If we can go to the Moon, why can't we...?" | L1748 |
| 设问 | "How can a simulation ever tell us anything...?" | L337 |
| 让步 | "I shall plead guilty to overstatement, while protesting..." | L203 |
| 讽刺 | 模态逻辑"像长颈鹿一样存在" | L1456 |
| 格言引用 | 撒缪尔·约翰逊的跳舞狗 | L533 |
| 平行结构 | "飞机与鸟、海豚与金枪鱼、重力钟与电池钟" | L265 |
| 类比推演 | 自然选择之于生物=理性之于人类行为科学 | L263 |

## 四、史料使用方式

1. **作为论据的史料**：心理学实验史（Ebbinghaus 1880 年代 L856、Hull-Hovland 1930 年代 L860）、经济思想史（Cournot 19 世纪中叶 L581）、控制论史（Wiener 二战期 L2080）、突变论史（1968 L2104）。
2. **作为案例的史料**：18 世纪航海时钟（L241）、马歇尔计划（1948 L1770）、美国宪法（1787 L1754）、匹兹堡重建（约 1940 年代 L1974）、东欧经济转轨（1990 L543）。
3. **作为引文的史料**：专利文本（L281—L295）、联邦党人文集第 55 篇（L1758）、Skinner（L912—L914）、Smuts（L2052—L2054）、Euclid（L2473）。
4. **作为数据的史料**：参数估计（8 秒/组块、7 组块、50,000 组块）跨文献汇算（L856—L886、L1120）。
5. **处理原则**：作者区分"经验证据"与"投机推断"，对后者明示边界（L1120、L2258、L2320）。

## 五、阐述方法

1. **主题—变奏式组织**：序言自陈全书如"赋格曲"（L138），概念先在各章主题中呈现，后在后续章节复现深化（如"界面"在第1、2、5、8章反复）。
2. **自底向上与自上而下并用**：既有从简单参数到复杂表现的归纳（第3、4章），也有从总纲到例证的演绎（第1、8章）。
3. **思想实验方法**：蚂蚁自动化设计（L735）、点击保险箱（L2296）、64 符号矩阵缩写（L2449）。
4. **程序即理论**：把"可运行程序"作为精确理论陈述（EPAM、GPS、BACON），用"程序能否复现人类行为"检验命题（L435、L1710—L1712）。
5. **课程清单法**：第5、6章分别以设计课程七主题/社会设计六主题收束（L1682—L1708、L2016—L2032），将理论转为可教知识。

## 六、推演逻辑特征

1. **以"内/外环境"为公理式二分**：全书多数论证从该二分出发（L245—L253）。
2. **经验—先验混合**：参数恒常性作为经验概括（L858），层级优势作为先验+计算论证（L2228—L2260）。
3. **可计算性论证**：用复杂度量级（10!、10^120、N!、100^10）论证可行性边界（L767、L1490、L1506、L2296）。
4. **反事实推演**："如果环境不同，人工物可能完全不同"（L146）。
5. **边界声明**：对不确定处明确标注（L2108—L2110、L2160）。

## 七、术语中英对照表

| 英文术语 | 中文译名 | 主要证据行号 |
| --- | --- | --- |
| artificial / artificiality | 人工的/人工性 | L213—L215 |
| inner/outer environment | 内环境/外环境 | L245—L253 |
| interface | 界面 | L247 |
| functional explanation | 功能解释 | L255—L269 |
| substantive rationality | 实质理性 | L453 |
| procedural rationality | 程序理性 | L453 |
| bounded rationality | 有限理性 | L152、L649 |
| satisficing | 满意化 | L491—L493、L1502 |
| aspiration levels | 抱负水平 | L501—L503 |
| physical symbol system | 物理符号系统 | L415—L433 |
| chunk | 组块 | L872 |
| short-term memory (STM) | 短时记忆 | L830 |
| long-term memory (LTM) | 长时记忆 | L1108—L1110 |
| production system | 产生式系统 | L1288—L1306 |
| heuristic search | 启发式搜索 | L479、L2298 |
| means-ends analysis | 手段—目的分析 | L1524—L1532 |
| design | 设计 | L1412 |
| optimization | 最优化 | L1466 |
| representation | 表征/表示 | L1634—L1680 |
| state description | 状态描述 | L2471—L2475 |
| process description | 过程描述 | L2471—L2475 |
| hierarchy / hierarchic system | 层级/层级系统 | L2190 |
| near decomposability | 近可分解性 | L2330—L2336 |
| complexity | 复杂性 | L2180—L2182 |
| emergence | 涌现 | L2056—L2064 |
| holism | 整体论 | L2052 |
| reductionism | 还原论 | L2056 |
| cybernetics | 控制论 | L2080 |
| chaos / strange attractor | 混沌/奇异吸引子 | L2114—L2128 |
| catastrophe theory | 突变论 | L2102 |
| genetic algorithms | 遗传算法 | L2146—L2154 |
| cellular automata | 元胞自动机 | L2156—L2160 |
| template | 模板 | L964、L2495 |
| docility | 可教化性 | L671 |
| empty world hypothesis | 空世界假说 | L2465 |
| goal-driven / stimulus-driven | 目标驱动/刺激驱动 | L1304 |
| rational expectations | 理性预期 | L593 |
| transaction costs | 交易成本 | L615 |
| externalities | 外部性 | L635 |
| identification | 认同 | L657 |
| organization-&-market economy | 组织-&-市场经济 | L515—L517 |
| invisible hand | 看不见的手 | L519—L521 |
| Pareto optimality | 帕累托最优 | L531 |
| General Problem Solver (GPS) | 通用问题求解器 | L1532 |

---

# 第二部分 实体总索引

> 收录参与论证的主要实体，按六类分表；行号为其在正文中的主要出现位置（部分兼附人名索引页码行 L2537—L2549 供检索）。

## 一、人物

| 人物 | 身份/贡献 | 证据行号 |
| --- | --- | --- |
| Herbert A. Simon | 作者 | L5 |
| Allen Newell | 合作者、献词对象 | L91—L93、L164、L1302 |
| Simon Stevin | 荷兰物理学家，斜面定律 | L182—L193 |
| Aristotle | 哲学家，《物理学》 | L203 |
| Isaac Newton | 物理学家 | L180、L1382 |
| Karl Taylor Compton | Compton 讲座主办者 | L140、L160、L1432 |
| H. Rowan Gaither | Gaither 讲座主办者 | L142、L160 |
| Lee W. Gregg | 合作者 | L166 |
| A. W. Phillips | Moniac 水力学模型 | L333 |
| John von Neumann | 计算机理论、博弈论、元胞自动机 | L381、L583、L1464、L2158 |
| Charles Babbage | 计算器 Mill/Store | L393 |
| Milton Friedman | 经济学家 | L495 |
| Oscar Lange | 市场社会主义 | L541 |
| Friederich von Hayek | 市场秩序理论 | L547 |
| Augustin Cournot | 双头垄断理论 | L581 |
| Oskar Morgenstern | 博弈论 | L583 |
| Roy Radner | 博弈论、满意解 | L587 |
| George Katona | 预期形成研究 | L603 |
| Kenneth Arrow | 一般均衡 | L531、L1464 |
| Gerard Debreu | 一般均衡 | L531 |
| Leo Hurwicz | 一般均衡 | L531 |
| R. R. Nelson / S. G. Winter | 演化经济学 | L705—L709 |
| O. E. Williamson | 新制度经济学 | L607—L615 相关 |
| Grey Walter | 机电"乌龟" | L735 |
| Hermann Ebbinghaus | 记忆实验 | L856—L858 |
| Carl I. Hovland / Clark Hull | 学习实验 | L860—L862 |
| S. S. Stevens | 实验心理学手册 | L862 |
| J. A. McGeoch | 学习心理学 | L864 |
| B. R. Bugelski | 学习参数 | L864 |
| George A. Miller | 神奇数字七 | L882 |
| N. C. Waugh / D. A. Norman | 短时记忆实验 | L888 |
| Roger N. Shepard | 图片识别 | L890 |
| Donald F. Dansereau | 心算实验 | L900 |
| B. F. Skinner | 行为主义 | L912 |
| Adriaan D. de Groot | 棋局知觉 | L932 |
| Alfred Marshall | 新古典经济学 | L976 |
| Noam Chomsky | 生成语言学 | L986 |
| L. Stephen Coles | 语义消歧程序 | L1008 |
| Laurent Siklóssy | 语言学习程序 | L1022 |
| I. A. Richards | "Language through Pictures" | L1022 |
| Immanuel Kant | 哲学家 | L1042 |
| Benjamin Lee Whorf | 语言相对论 | L1042 |
| Bobby Fischer / Judit Polgar | 国际象棋天才 | L1138 |
| Mozart | 作曲家 | L1138—L1140 |
| Gordon Novak | ISAAC 程序 | L1218 |
| David Neves | 从例子学习程序 | L1338 |
| John R. Anderson | 认知导师 | L1340—L1350 |
| Yuichiro Anzai | 学做程序 | L1344 |
| P. Langley / G. L. Bradshaw / J. M. Zytkow | BACON 与发现研究 | L1362—L1370 |
| Marvin L. Manheim | 公路选址设计 | L1570 |
| Ivan Sutherland | SKETCHPAD | L1664 |
| John Grason | 户型平面系统 | L1666 |
| Karl R. Popper（非正文人物，见人名索引） | 哲学 | L2537（索引） |
| Mies van der Rohe | 建筑师 | L1862 |
| Oscar Wilde / J. M. W. Turner | 文学/绘画 | L1938 |
| Vannevar Bush | "无尽边疆" | L2014 |
| Gary Becker / George Stigler | 效用资本论 | L1992 |
| Plato | 哲学家 | L1746、L2479 |
| Sir Thomas More | 乌托邦 | L1746 |
| Karl Marx | 乌托邦/革命 | L1746 |
| Alexander the Great / Philip | 帝国 | L2316 |
| T. E. Lawrence | 阿拉伯起义 | L2318 |
| J. C. Smuts | 整体论 | L2052 |
| Norbert Wiener | 控制论 | L2080 |
| R. Thom | 突变论 | L2104 |
| Henri Poincaré | 动力系统 | L2114 |
| E. N. Lorenz | 天气混沌 | L2116 |
| John Holland | 遗传算法 | L2148 |
| Stanislaw Ulam / Arthur Burks / Christopher Langton | 元胞自动机 | L2158 |
| W. M. Elsasser | 《生物学的物理基础》 | L2439 |
| James Madison / Alexander Hamilton / John Jay | 《联邦党人文集》 | L1758、L140（索引） |
| Samuel Johnson | 文人 | L533 |
| Galileo | 落体定律 | L2467 |
| Euclid | 几何学 | L2473 |
| F. P. Ramsey / B. de Finetti / A. Wald / J. Neyman / L. J. Savage | 决策理论 | L1464 |
| Dahlberg | 水力经济模型 | L331 |
| Frederic Bartlett | 记忆研究 | L842 |
| Darwin | 演化论 | L539、L681、L2417 |
| Lamarck | 演化论（拉马克式转移） | L709 |
| Adam Smith（概念性） | 看不见的手 | L519—L521 |

## 二、著作/作品

| 著作/作品 | 说明 | 证据行号 |
| --- | --- | --- |
| The Sciences of the Artificial | 本书 | L3 |
| Administrative Behavior | 西蒙行政理论 | L152 |
| Models of Man | 西蒙文集 | L152 |
| Unified Theories of Cognition | Newell 遗著 | L126 |
| The Theory of Games and Economic Behavior | von Neumann & Morgenstern | L583 |
| Human Problem Solving | Newell & Simon | L1302 |
| Scientific Discovery | Langley, Simon, Bradshaw, Zytkow | L1370 |
| Principles of Economics | Marshall | L976 |
| Science and Human Behavior | Skinner | L912 |
| Psychology of Human Learning | McGeoch | L864 |
| The Federalist | 美国宪法辩护文集 | L1758 |
| Physics | 亚里士多德 | L203 |
| Meno | 柏拉图 | L2479 |
| "Holism"（Encyclopaedia Britannica） | Smuts 条目 | L2052、L2062 |
| The Physical Foundation of Biology | Elsasser | L2439 |
| The Clockwork Orange | 电影 | L1870 |
| 1919 Motor Controller Patent | 电机控制器专利 | L279—L295 |
| Club of Rome Report | 罗马俱乐部报告 | L1824—L1828 |
| "Language through Pictures" | Richards 系列教材 | L1022 |
| "The Magical Number Seven" | Miller 论文 | L882 |
| EPAM（程序） | 记忆模拟 | L872—L874 |
| GPS（程序） | 通用问题求解器 | L1532 |
| BACON / AM / DENDRAL / MECHEM | 发现程序 | L1358—L1374 |
| UNDERSTAND / ISAAC | 理解程序 | L1198—L1240 |
| SKETCHPAD | 交互图形系统 | L1664 |
| MATER | 象棋杀棋程序 | L1594 |

## 三、概念

| 概念 | 证据行号 |
| --- | --- |
| artificiality / artificial | L144、L213—L215 |
| inner environment / outer environment | L245—L253 |
| interface | L247 |
| functional explanation | L255—L269 |
| adaptation | L231、L259 |
| homeostasis | L267、L2046 |
| task environment | L307 |
| simulation | L319—L369 |
| skyhook-skyscraper | L361—L363 |
| physical symbol system | L415—L433 |
| intelligence as computation | L431—L435 |
| substantive/procedural rationality | L453 |
| satisficing | L491—L493、L1502 |
| aspiration levels | L501—L503 |
| organization-&-market economy | L515—L517 |
| invisible hand | L519—L521 |
| Pareto optimality | L531 |
| transaction costs | L615 |
| externalities | L635 |
| identification | L657—L675 |
| docility | L671 |
| generator and test | L679—L681 |
| local/global maxima | L691—L693 |
| chunk | L872 |
| short-term memory / long-term memory | L830—L832、L1108—L1110 |
| list structures | L970 |
| mind's eye | L972—L974 |
| recognition / intuition | L1118—L1128 |
| template / retrieval structure | L964、L874 |
| semantically rich domains | L1090 |
| production system | L1288—L1306 |
| learning from examples | L1308—L1344 |
| discovery processes | L1346—L1376 |
| representation change | L1378—L1390 |
| design | L1412 |
| science of design | L1426—L1438 |
| imperative/declarative logic | L1442—L1480 |
| optimization | L1466—L1496 |
| means-ends analysis | L1524—L1532 |
| generator-test cycle | L1606—L1612 |
| style | L1620—L1626 |
| representation | L1634—L1680 |
| social planning | L1744 |
| organization as representation | L1768—L1778 |
| limiting resource | L1782—L1790 |
| discounting the future | L1918—L1926 |
| designing without final goals | L1966—L1998 |
| bounded rationality | L152、L1756、L2020 |
| holism / reductionism | L2050—L2076 |
| emergence | L2056—L2064 |
| cybernetics | L2080 |
| general systems theory | L2088 |
| catastrophe theory | L2102—L2110 |
| chaos | L2112—L2142 |
| strange attractor | L2126—L2128 |
| genetic algorithms | L2146—L2154 |
| cellular automata | L2156—L2160 |
| hierarchy | L2190—L2196 |
| near decomposability | L2328—L2407 |
| empty world hypothesis | L2465 |
| state description / process description | L2471—L2483 |
| ontogeny recapitulates phylogeny | L2507 |
| rational expectations | L593—L601 |
| Prisoners' Dilemma | L585—L587 |
| negative entropy | L2080 |

## 四、机构

| 机构 | 说明 | 证据行号 |
| --- | --- | --- |
| The MIT Press | 出版者 | L7 |
| Massachusetts Institute of Technology | 讲座主办/研究基地 | L140、L369、L986 |
| University of California, Berkeley | 讲座主办 | L142、L174 |
| Carnegie Mellon University | 作者单位/设计研究中心 | L369、L1006、L1428—L1436 |
| Carnegie-Mellon | 同上（旧称） | L172 |
| National Institute of Mental Health | 心理研究资助 | L170 |
| Public Health Service | 资助 | L170 |
| Advanced Research Projects Agency | 设计研究资助 | L172 |
| Carnegie Corporation / Ford Foundation / Alfred P. Sloan Foundation | 资助方 | L172 |
| NASA | 登月组织 | L1750 |
| Economic Cooperation Administration (ECA) | 马歇尔计划执行机构 | L1770—L1778 |
| National Academy of Sciences | 排放标准委员会 | L1800 |
| U.S. State Department | 通信拥堵案例 | L1782 |
| Illinois Institute of Technology | Mies 任教 | L1862 |
| Library of Congress | 记忆类比 | L1258 |
| Psychology Institute, Chinese Academy of Sciences | 中国代数课程 | L1340—L1342 |
| Santa Fe Institute | 人工生命会议 | L2170 |
| European Union / Common Market | ECA 后果 | L1778 |
| Encyclopaedia Britannica | Smuts 条目 | L2062 |

## 五、地点

| 地点 | 语境 | 证据行号 |
| --- | --- | --- |
| Phoenix / Boston | 日晷使用 | L241 |
| Arctic | 白毛动物/冬季 | L241、L259 |
| Pittsburgh | 出租车司机/重建 | L1084、L1974—L1976 |
| East Bay | 出租车司机 | L1084 |
| Himalayan villages | 茶道问题 | L1176 |
| California / Mt. Whitney / Nob Hill | 局部/全局最大 | L691—L693 |
| Singapore / New York | 蝴蝶效应 | L2116 |
| Rheinland / Mainz / Ebersheim / Woerstadt / Partenheim | 家谱搜索 | L1910 |
| Poland | Lange 市场社会主义 | L541 |
| Bosnia / Sri Lanka | 不确定性例 | L557 |
| Oklahoma City | 反政府炸弹 | L1900 |
| Tennessee Valley / Indus / Nile / Egypt | 流域开发 | L1746 |
| Troy | 历史之光 | L1912 |
| London / Thames | Turner 画雾 | L1938 |
| America / France / Russia / China | 革命 | L1746 |
| China | 代数课程 | L1340—L1342 |
| Shippingport | 原子能电站 | L357 |
| Scythian / Indian frontiers | 亚历山大边疆 | L2318 |
| Persia | 帝国子系统 | L2316 |

## 六、事件

| 事件 | 说明 | 证据行号 |
| --- | --- | --- |
| 1968 Compton 讲座（MIT） | 成书第一来源 | L140 |
| 1980 Gaither 讲座（Berkeley） | 成书第二来源 | L142 |
| 1969 第一版出版 | 设计科学影响起点 | L176、L1428 |
| 1981 第二版修订 | 版本史 | L120 |
| 1996 第三版出版 | 本书版本 | L51、L134 |
| 1962 年《美国哲学会会刊》刊文 | 第8章前身 | L162 |
| 18 世纪航海时钟研制 | 环境塑形设计 | L241 |
| 大萧条 | 达赫伯格模型语境 | L331 |
| 第二次世界大战 | 控制论/东欧经济 | L333、L541、L2080 |
| 1944 年《博弈论与经济行为》出版 | 博弈论里程碑 | L583 |
| 1956 年 MIT 会议 | 转换语言学与信息加工心理学诞生 | L986 |
| 1948 年马歇尔计划 | ECA 案例 | L1770 |
| 1990 年东欧经济崩溃 | 计划—市场之争 | L543 |
| 郁金香狂热 | 投机泡沫 | L565 |
| 美国独立/宪法 200 周年 | 社会设计案例 | L1754 |
| 登月 | 技术设计成功 | L1750—L1752 |
| 匹兹堡金三角重建 | 无最终目标设计 | L1974—L1976 |
| 1963 年字母序列发现程序 | 发现研究起点 | L1356 |
| 1968 年突变论登场 | 突变论史 | L2104 |
| 1970 年代末混沌实验证据 | 混沌研究 | L2116 |
| 俄克拉荷马城爆炸 | 反政府情绪 | L1900 |
| 罗马俱乐部报告 | 预测批判 | L1824—L1828 |
| 英制→公制转换 | 局部最大例 | L699 |
