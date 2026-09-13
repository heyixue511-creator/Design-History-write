# 处理记录契约

数据任务按 processing/<ref_id>/ 保存 chunks.md、semantics.md 与 coverage.md；由模型阅读、判断后写入 Markdown，复用等价现行记录时保留这些语义。

## 段落记录
chunk_id 为稳定记录 ID；ref_id 与 sources 对应。
source_path、source_sha256、line_start、line_end 必填，行范围针对指定版本、从 1 起算且包含首尾。
text 保存该范围的原文；heading_path、parent_chunk_id、context_chunk_ids 表达结构和必要上下文。
page_label 仅在原文或原件明确标注时填写。
重新切段不静默复用失效定位：标明新旧关系，使依赖单元需复核。

## 语义记录
analysis_id、chunk_id、entities、candidate_claims、issues。
entities 保留原词、候选规范名、类型和别名依据；不因同名就合并人物或概念。
candidate_claims 每项记录主语、谓语、宾语、归属、否定、模态、时间、地点、条件及证据范围。
否定可独立编码，但展示时不得丢失：“甲—未采用—乙”不能显示成“甲—采用—乙”。
引用某人的观点不等于本文作者赞同该观点。

## 覆盖记录
ref_id、输入文件与哈希、processed_ranges、pending_ranges、excluded_ranges（含理由）、issues、status。
范围针对每个文件记录；有意义的未覆盖正文或 pending 不得标为 complete。
状态区分 pending / partial / complete / blocked；进度记录续作位置与原因，不复制全文。
