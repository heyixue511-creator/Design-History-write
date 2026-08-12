# NN 专项报告与实体总索引

> 论文：《Replication Protocol Analysis: A Method for the Study of Real-World Design Thinking》（Per Galle & László Béla Kovács）。证据行号以源文件 `_paged.md` 为准（无 `_clean.md` 版本）。

---

# 第一部分 专项报告

## 一、语言与文字风格

1. **语体**：英语学术论文体，主叙述采用第一人称复数"We"（L25、L45、L51、L109、L113、L322），复现协议部分切换为第一人称单数推理独白（L190、L192、L212、L234），形成"论文叙述者"与"协议复现者"两个声音层次。
2. **句式特征**：
   - 长复合句承载复杂限定条件，如 L43 一段内连用"as described below""may not match exactly""seems to apply"多重限定；
   - 定义句密集：RPA（L25）、forward/backward decision（L186）、imagining/reasoning（L99-103）、PDU（L320）；
   - 问句用作论证推进装置："But how?"（L238）、"How can the trees 'unite' groups of buildings? — by playing the role of avenue trees!"（L212，自问自答）。
3. **术语策略**：大量创制/专名化缩写——RPA、DPA（L7、L47）；复合术语——post-hoc rationalization（L43）、deciding THAT/HOW（L308）、that-decision/how-decision（L322）；跨学科借词——modal logic（L268）、abduction（L274）、knowledge elicitation（L111）、figure/ground（L196）。
4. **语气调控**：审慎限定词高频出现——"probably"（L190）、"presumably"（L294）、"we contend"（L113、L322）、"somewhat controversial"（L113）、"as it were"（L314）；同时有明确宣告——"distinct advantages"（L7）、"obviously"（L328）。
5. **OCR 说明**：源文本含 OCR 损伤（L23、L43、L290、L328、L354-364），个别引号与逻辑符号（¬）缺失；语言分析基于可读部分，损伤处已在 00 报告中注明。

## 二、文风与修辞方式

1. **隐喻**：核心隐喻"帆与舵"（sail and rudder，L105）将设计演化（想象）与合理化（推理）的关系具象化，强调二者"交织互依"（L105）；"进入问题之路"（a way in to the problem）借自 Darke 并反复使用（L328、L330）；"削减潜在解的多样性"（reduce the variety of potential solutions）作为贯穿性短语（L328、L330）。
2. **引语镶嵌**：直接引语承载权威论证——Lawson 的两段批评（L43、L87、L93）、Porter 对"理想化设计过程"的定义（L67）、Darke 受访建筑师的"生成性事物"自述（L328）、Eekels 的手段—端相对论（L318）、Gielingh 的 PDU 定义（L320）。
3. **正反论证结构**：先立后破——先承认 DPA "相对真实"（L79），再逐条列 RPA 优势（L81-89）；先引 Darke 主生成器理论，再以观察 B 推广之（L330）；先承认"复现协议绝不能当作真实过程描述"（L79），再论证其研究价值。
4. **自我反驳/边界修辞**：主动设置反例与限度——决策 32a"未留下任何推理痕迹"（L294）；协议作为想象证据"rudimentary"（L306）；主生成器"并非完全自我强加"（L328）。
5. **分层排版修辞**：决策清单（[Decision 3a: ...]）以方括号嵌入协议段落（L192-252），将"原始叙述"与"分析注释"在版面上明确分层；公式（L286-288）以 LaTeX 呈现形式化论证。

## 三、史料使用方式

1. **史料类型**：竞赛一手材料（任务书 L125、方案图 L173-177、竞赛结果刊载 L127）；方法论文献（Lawson L19、Porter L41、Darke L324、Eekels L316、Roozenburg L278）；理论文献（von Wright L276、Gielingh L324）；作者自身工作（L35、L37、L149、L153、L155、L194、L248、L250、L350）。
2. **使用方式**：
   - 任务书被系统转述为五目的+约束清单（L137-169），作为后续论证的"公理库"；
   - 文献以编号上标+页脚全目（L11-350）方式引用，正文给出具体页码（p 226 L43；p 170 L67；p 183、pp 186-187 L328；p 9 L320）；
   - 对历史研究（Darke）采用"重述—对照—推广"三步：详细转述其方法、证据与模型（L328），与案例对照（保存防风林带 vs 树缘场地），再推广结论（L330）；
   - 一手协议材料以"摘录+决策清单注释"方式公开（L186-252），完整版指向工作报告（L194、L340）。
3. **史料批判意识**：指出任务书提及防风林带故主生成器"非完全自我强加"（L328、L358）；说明注 3 是对复现练习的补充说明（L358）。

## 四、阐述方法

1. **方法-案例-应用三段式**：先抽象定义方法（L49-63），再给真实案例（L123-178），最后示范三种分析（L254-330）——以"做给你看"替代"说给你听"。
2. **比较法**：RPA vs DPA 的逐条优势对照（L79-89）；RPA 与 Lawson 第三类方法的同异辨析（L43）；GARM 功能单元/技术解决方案与 that/how 决策的类比与差异（L320-322）。
3. **逻辑形式化**：将自然语言论证（A/B/C 三段，L260-264）翻译为模态逻辑推理模式（L270），并指认其为溯因（L274）；以公式展示"合意¬Q→合意¬P"的否决论证（L286-288）。
4. **案例分析中的归纳**：从协议决策序列归纳观察 A、观察 B（L308-310），再以文献（Eekels、GARM）佐证，最后推广至理论命题（L330）。
5. **多视角并置**：同一协议从合理化（3.2）、知识抽取（3.3）、演化（3.4）三视角分析，展示 RPA 的"一料多用"。

## 五、推演逻辑

1. **总体推演链**：方法论危机（Lawson 批评，L43）→ 化解策略（接受合理化，L45）→ 方法建构（五阶段，L51-63）→ 优势论证（vs DPA，L79-89）→ 边界界定（想象/推理两分，L99-121）→ 案例实证（L123-330）→ 理论推广（L330）→ 贡献总结（L336-342）。
2. **关键推理模式**：
   - 溯因（abduction）：M→E、Required E ⇒ Desirable M（L270-274）——协议中决策辩护的基本形式；
   - 否定式溯因：P→Q、Desirable ¬Q ⇒ Desirable ¬P（L286-288）——后退决策的隐含形式；
   - 类比推理：图底知觉（L196）→ 场地结构再描述；GARM 产品模型 ↔ 设计决策链（L320-322）；
   - 归纳推广：观察 B（单案例）→ 主生成器推广命题（L330）。
3. **推理的诚实标注**：作者明确区分"已确立"与"推测"——"would be going too far"（L266）、"presumably ... quite common"（L294）、"seems to suggest"（L330）、"we contend"（L113、L322）。

## 六、文字风格总评

准确、审慎、结构透明的学术英文；术语密度高但均有定义锚点；论证中主动暴露限度与反例，维持认识论上的谦逊；协议部分文风转为口语化的思考独白（L190-242），与正文的书面体形成鲜明文体对照，强化"原始材料"与"分析文本"的区分。

## 七、术语中英对照表

| 英文术语 | 中文译名 | 行号 |
|---|---|---|
| replication protocol analysis (RPA) | 复现协议分析 | L7、L25 |
| design replication | 设计复现 | L9、L63 |
| replication protocol | 复现协议 | L55、L186 |
| replicator | 复现者 | L51 |
| design protocol analysis (DPA) | 设计协议分析 | L47、L67 |
| protocol analysis | 协议分析（通称） | L67 |
| post-hoc rationalization | 事后合理化 | L43、L45 |
| design thinking | 设计思维 | L7、L99 |
| imagining | 想象 | L93、L101 |
| reasoning | 推理 | L93、L103 |
| design evolution | 设计演化 | L101、L306 |
| design rationalization | 设计合理化 | L103、L256 |
| forward decision | 前进决策 | L186 |
| backward decision | 后退决策 | L186 |
| deciding THAT | 决定"那个"（指定端/目标） | L308 |
| deciding HOW | 决定"怎样"（指定手段） | L308 |
| means / end | 手段 / 端（目的） | L308-318 |
| modal logic | 模态逻辑 | L268 |
| modal operator | 模态算子 | L272 |
| Desirable | 合意的（模态算子） | L270-272 |
| Required | 被要求的（模态算子） | L270-272 |
| abduction / explanatory abduction | 溯因 / 解释性溯因 | L274 |
| primary generator | 主生成器 | L328 |
| generator-conjecture-analysis | 生成—猜想—分析（模型） | L328 |
| analysis-synthesis | 分析—综合（模型） | L328 |
| knowledge elicitation | 知识抽取 | L111、L296 |
| design brief | 设计任务书 | L53、L137 |
| target solution | 目标方案 | L53、L129 |
| figure / ground | 图 / 底 | L196、L362 |
| permeability | 可渗透性 | L224、L298 |
| GARM (General AEC Reference Model) | 通用 AEC 参考模型 | L320、L364 |
| product definition unit (PDU) | 产品定义单元 | L320 |
| functional unit | 功能单元 | L320 |
| technical solution | 技术解决方案 | L320 |
| product model | 产品模型 | L320 |
| decision chain | 决策链 | L316 |
| case study | 案例研究 | L9、L129 |
| site planning | 场地规划 | L7、L129 |
| inference pattern | 推理模式 | L9 |
| windbreak | 防风林带 | L159、L190 |
| shared ownership housing | 共享所有权住房 | L161、L242、L360 |
| low-rise high-density | 低层高密度（住宅） | L139、L161 |

---

# 第二部分 实体总索引

## 一、人物

| 人物 | 身份/角色 | 证据行号 |
|---|---|---|
| Per Galle | 第一作者；丹麦技术大学建筑 CAD 单元；复现者（建筑师出身） | L3、L7、L182 |
| László Béla Kovács | 第二作者；哥本哈根大学计算机科学系 | L5 |
| Lawson（Bryan Lawson） | 设计思维研究权威；四类方法分类与批评者 | L19、L43、L87、L93 |
| Porter, W. L. | 设计复现技术创始人；两项复现案例作者 | L41、L63、L67、L79 |
| Eastman, C. M. | 协议分析早期使用者 | L67、L69 |
| Akin, Ö. | 设计心理学作者；协议分析使用者 | L17、L67、L71 |
| Eckersley, M. | 严谨协议分析研究者 | L67、L73 |
| Schön, D. A. | 协议分析使用者（反思实践传统） | L67、L75 |
| Goldschmidt, G. | 草图辩证法研究者 | L67、L77 |
| Davies, S. P. | DPA 批评者（专家程序员研究） | L87、L95 |
| Darke, J. | 主生成器理论提出者 | L324、L326、L328、L330 |
| Eekels, J. | 决策链理论（端—手段相对论） | L316、L318 |
| Gielingh, W. F. | GARM 模型提出者 | L320、L324 |
| Roozenburg, N. F. M. | 创新设计推理模式研究者 | L274、L278 |
| von Wright, G. H. | 模态逻辑经典作者 | L276 |
| Bentley, I. 等五人 | 《Responsive environments》设计手册作者 | L302 |
| Alexander, C. | 《The timeless way of building》作者 | L11 |
| Cross, N. | 设计方法论编者（Darke 论文重印编者） | L13、L326 |
| Heath, T. | 《Method in architecture》作者 | L15 |
| Brawne, M. | 《From idea to building》作者 | L33 |
| Coyne, R. D. 等五人 | 《Knowledge-based design systems》作者 | L39 |
| Ib V. Nielsen 等六人 | 奥胡斯建筑师集团获奖设计团队成员（Architects MAA） | L356 |

## 二、著作/作品

| 著作/作品 | 类型 | 证据行号 |
|---|---|---|
| 《Replication protocol analysis...》（本文） | 论文 | L1 |
| Lawson《How designers think》(2nd edn) | 专著 | L19 |
| Porter《Notes on the inner logic of designing: Two thought-experiments》(1988) | 论文 | L41、L67 |
| Eastman《On the analysis of intuitive design processes》(1970) | 论文 | L69 |
| Akin《Psychology of architectural design》(1986) | 专著 | L17 |
| Akin《Architects' reasoning with structures and functions》(1993) | 论文 | L71 |
| Eckersley《The form of design processes》(1988) | 论文 | L73 |
| Schön《Designing: rules, types and worlds》(1988) | 论文 | L75 |
| Goldschmidt《The dialectics of sketching》(1991) | 论文 | L77 |
| Davies《Effects of concurrent verbalization...》(1995) | 论文 | L95 |
| Alexander《The timeless way of building》(1979) | 专著 | L11 |
| Cross（编）《Developments in design methodology》(1984) | 编著 | L13、L326 |
| Heath《Method in architecture》(1984) | 专著 | L15 |
| Brawne《From idea to building》(1992) | 专著 | L33 |
| Galle《Issues in architecture》（书评）(1993) | 书评 | L35 |
| Galle & Kovács《The logic of worms》(1992) | 论文 | L37 |
| Galle & Kovács《Introspective observations of sketch design》(1992) | 论文 | L149 |
| Galle & Kovács《The logic of walking》(1993) | 论文 | L153 |
| Galle & Kovács《The logic of plaza space》(1994) | 论文 | L155 |
| Galle & Kovács《Spangsbjerg site planning replicated》(1993) | 工作报告 | L194、L340 |
| Galle《Design rationalization and the logic of design》报告 (1995) | 工作报告 | L248 |
| Galle《Design rationalization and the logic of design: a case study》(in press) | 论文 | L250 |
| Galle《Product modeling for building design》(1994) | 书目报告 | L350 |
| Coyne 等《Knowledge-based design systems》(1990) | 专著 | L39 |
| Esbjerg Kommune《Idé-konkurrence om en bebyggelsesplan i Spangsbjerg》(1985) | 竞赛任务书 | L125 |
| 《Arkitekten》Vol 87 No 17 (1985) | 期刊（竞赛结果） | L127、L348 |
| Bentley 等《Responsive environments. A manual for designers》(1985) | 设计手册 | L302 |
| Eekels《Design processes seen as decision chains》(1983) | 会议论文 | L316 |
| Gielingh《General AEC reference model (GARM)》(1988) | 研究报告 | L324 |
| Darke《The primary generator and the design process》(1979；1984 重印) | 论文 | L324、L326 |
| Roozenburg《On the pattern of reasoning in innovative design》(1993) | 论文 | L278 |
| von Wright《An essay in modal logic》(1951) | 专著 | L276 |

## 三、概念

| 概念 | 简述 | 证据行号 |
|---|---|---|
| RPA | 复现协议分析：五阶段方法 | L7、L25、L51-63 |
| DPA | 设计协议分析：观察式方法 | L47、L67 |
| design replication | 设计复现（Porter 技术） | L9、L63 |
| replication protocol | 复现协议文本 | L55、L186 |
| replicator | 复现者 | L51、L109 |
| post-hoc rationalization | 事后合理化 | L43、L45、L109 |
| imagining / reasoning | 想象/推理两分 | L93、L99-103 |
| design evolution | 设计演化 | L101、L306 |
| design rationalization | 设计合理化 | L103、L256 |
| forward/backward decision | 前进/后退决策 | L186、L188 |
| deciding THAT/HOW | 决定端/决定手段 | L308-310 |
| means/end 链 | 手段—目的链 | L308-318 |
| modal logic | 模态逻辑 | L268 |
| abduction | 溯因推理 | L274 |
| primary generator | 主生成器 | L328、L330 |
| generator-conjecture-analysis | 生成—猜想—分析模型 | L328 |
| analysis-synthesis | 分析—综合模型 | L328 |
| knowledge elicitation | 知识抽取 | L111、L296 |
| figure/ground | 图底 | L196、L362 |
| permeability | 可渗透性 | L224、L298 |
| GARM/PDU | 产品建模框架 | L320-322、L364 |
| functional units / technical solutions | 功能单元/技术解决方案 | L320 |
| design brief | 设计任务书 | L53、L137 |
| target solution | 目标方案 | L53、L129 |
| site planning | 场地规划 | L7、L129 |
| design competition | 设计竞赛 | L7、L125 |
| windbreaks | 防风林带 | L159、L190 |
| shared ownership housing | 共享所有权住房 | L161、L360 |

## 四、机构

| 机构 | 角色 | 证据行号 |
|---|---|---|
| Technical University of Denmark（建筑 CAD 单元/建筑研究所） | 第一作者单位 | L3 |
| University of Copenhagen（计算机科学系） | 第二作者单位 | L5 |
| Esbjerg Kommune（埃斯比约市政府） | 竞赛主办方 | L125、L129 |
| Arkitektgruppen i Århus（奥胡斯建筑师集团） | 一等奖方案作者 | L129、L346 |
| Danske Arkitekters Landsforbund（丹麦建筑师协会） | 竞赛秘书处/刊载方 | L125、L127 |
| Arkitektens Forlag | 图版版权方 | L346 |
| TNO Building and Construction Research（代尔夫特） | GARM 出处 | L324 |
| The American Academy of Arts and Sciences | Porter 复现案例对象 | L63 |
| Oxford University Press / John Wiley / Butterworth / Pion / North-Holland / Addison-Wesley / MIT Press / Architectural Press / Heurista | 文献出版机构（分散出现于参考文献） | L11-350 |

## 五、地点

| 地点 | 角色 | 证据行号 |
|---|---|---|
| Spangsbjerg（丹麦埃斯比约郊外） | 案例场地 | L123、L129 |
| Esbjerg, Denmark | 竞赛城市 | L125、L129 |
| Lyngby, Denmark | 丹麦技术大学所在地 | L3 |
| Copenhagen, Denmark | 哥本哈根大学所在地 | L5 |
| Copley Square, Boston, MA | Porter 复现案例场地 | L63 |
| Delft, Netherlands | GARM 机构所在地 | L324 |
| Zürich（ICED 83 论文集出版地） | 文献地点 | L316 |
| London / Chichester / Reading, MA / Amsterdam / Cambridge, MA | 文献出版地 | L11-350 |

## 六、事件

| 事件 | 简述 | 证据行号 |
|---|---|---|
| 斯庞斯比约场地规划设计竞赛（1985） | 埃斯比约市政府主办；任务书发布；结果刊于《Arkitekten》 | L125、L127 |
| 一等奖授予奥胡斯建筑师集团 | 被选为复现目标方案 | L129 |
| Porter 的两项复现研究 | Copley Square 改造与美国文理科学院大楼 | L63 |
| 斯庞斯比约复现练习 | 第一作者复现，第二作者参与；口头→书面两轮 | L182 |
| 斯庞斯比约项目建成 | 形式略有修改 | L182 |
| Darke 的主生成器访谈研究（1979） | 对建筑师的事后访谈与模型提出 | L328 |

> 注：参与论证的主要实体均已收录；参考文献中的出版地名（伦敦、奇切斯特、剑桥等）按文本出现处计入地点类，但仅作文献信息，不参与论证。
