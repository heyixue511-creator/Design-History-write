# 知识单元与跨文献扩散契约

以下是执行数据任务的最小字段规范，不是已经完成的知识数据。

## 存储
knowledge/entities.md：规范实体、别名、类型、语境与辨识依据。
knowledge/units/<ref_id>.md：主谓宾知识单元；由指定 ref_id 首次提取的单元可引用多条出处。
knowledge/links.md：跨文献单元关系。
knowledge/coverage.md：清单快照、逐文献状态、扩散检索记录与续作断点。
使用可阅读的 Markdown 单元卡与关系表，模型逐项分析后写入，不由程序机械生成。
跨文件引用使用稳定 ID，不用展示文本作唯一键；已确认索引可按规模分片，入口只存索引路径。

## 知识单元

| 字段 | 含义 |
| --- | --- |
| unit_id | 稳定命题 ID |
| subject / predicate / object | 主语、明确关系、宾语；展示时包含否定，实体可带 entity_id |
| qualifiers | 时间、空间、条件、范围、否定、模态；原文未定者保持未知 |
| attribution | 谁的判断、谁在引用谁；匿名或不明必须如实标记 |
| claim_kind | source_statement / author_interpretation / paraphrase / cross_source_inference |
| evidence | 至少一项 ref_id、chunk_id、source_path、source_sha256、line_start、line_end；引文应短且必要 |
| status | candidate / checked_against_md / needs_original / disputed / superseded |
| premise_unit_ids | 综合推论必填，不能只列书名充当前提 |
| inference_note | 推论方法、适用边界、替代解释；非推论可为空 |
| issues | 尚不能确认的具体问题 |

checked_against_md 只表示与给定 MD 核对，不声称史实或 PDF 原件已经完全核验。
外部世界中的因果与“某作者认为存在因果”必须可区分。
同一句有多个关系时分别记录，并用共同上下文保持联系。

## 跨文献关系

link_id、from_unit_id、relation、to_unit_id、supporting_ref_ids、evidence、rationale、status。
relation 使用明确词义：supports、complements、contradicts、context_differs、same_source、topic_related。
方向：supports 为支持者 → 被支持命题；contradicts 等对称关系保持单一去重记录，不强赋因果方向。
这些是命题间的分析关系，不混入历史对象之间的因果三元组。
至少两个不同 ref_id 只是跨文献最低条件；同源转引用 same_source，不当独立互证。
合并同义单元后，出处仍完整保留；知识单元的唯一来源归属不等于它只能有一条证据。

## 全库覆盖
保存 bibliography_snapshot（真实路径、版本或哈希及 ref_id 集合），逐 ref_id 分列：
source_status、processing_status、extraction_status、diffusion_status、issues、resume_at。
每次扩散记录种子单元、检索键/别名、实际检索 ref_id 范围和索引版本、命中候选、接受/拒绝依据及未解决候选。
无关联仅指记录的检索方法与快照下未发现，不能宣称永久无关。
全清单逐条已核对且可用材料全部完成预定检索与候选核验，才能称该轮范围覆盖完成。
有缺源、未处理或待核项时输出已完成数量与缺口；不能靠把状态统一改成 complete 获得完成率。

## 语义验收情景
- 原文“作者甲引乙反对方案丙”：不得提取“甲—赞成—丙”。
- 两书同引一份宣言：可作同源关系，不计两份独立实施证据。
- 甲未采用乙：否定保留在展示和字段中。
- A→B 与 B→C：不自动创建 A→C 因果知识。
- 原文哈希变化：旧定位和相关推论需复核，不静默沿用。
