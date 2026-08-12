# 05_原子证据卡

## 目录用途

本目录将教材关键命题拆为可核验的最小事实、引文、对象、事件和数字单元。一张原子证据卡对应"一个可核验的最小主张"，不是来源卡（03）的重复，也不是命题矩阵（06）的整段命题。

追溯链统一为：

> 教材句子 → 教材命题 → 原子证据卡 → 分析报告定位 → 原始文献／对象

## 卡结构（依据 `schemas/atomic-evidence.schema.json`）

| 字段 | 必填 | 说明 |
|---|---|---|
| evidence_id | ✓ | 全局唯一编号：`EV-{章}{序号}`，如 `EV-0501` |
| claim | ✓ | 原子主张：只含一个可核验事实／引文／对象／事件／数字 |
| source_id | ✓ | 来源资产ID（B/P开头） |
| source_location | ✓ | 分析报告定位或clean行号；V3/V4时写版本＋页码 |
| source_class | ✓ | P0—P4 |
| verification_level | ✓ | V0—V4 |
| section_ids | ✓ | 适用教材章／节（可多个） |
| textbook_function | 可选 | 教材功能：核心命题／案例／反例／方法／争议 |
| supports | 可选 | 可支持的教材命题 |
| does_not_support | 可选 | 不能支持的外推 |
| time_boundary | 可选 | 时间边界 |
| geographic_boundary | 可选 | 地理边界 |
| counterevidence | 可选 | 反例或争议 |
| status | ✓ | candidate／accepted／rejected／needs_original_check |

## 规则

1. **原子性**：每卡只写一个最小主张；"命题矩阵行"须拆分为多张卡后方可入本目录。
2. **层级匹配**：P4（分析报告）定位只能产生 candidate 卡；accepted 卡必须能回查到 clean 原文行号或原始对象。
3. **升级路径**：V2 → V3（完整原文核验）→ V4（版本＋页码＋上下文）按项目说明第3.2节执行；本目录随升级更新 `verification_level` 与 `source_location`。
4. **去重**：同一引文、对象、档案或数字全库只计一张卡（共享P0组规则，见各章去重总表）。
5. **文件组织**：每章一个 JSON 文件（`CH00_原子证据卡.json` … `CH99_原子证据卡.json`），按 evidence_id 升序排列；`_candidates/` 存放脚本生成的待审候选卡。

## 生成与核验

- 候选卡可由 `scripts/build_atomic_evidence_candidates.py` 从已复核映射的 A 级行批量提取（status=candidate，仅作拆分素材）。
- 人工精选卡：从各章矩阵 A 级命题＋来源卡 `original_spot_checks` 拆分，须标注行号或报告定位后方可标 accepted。
