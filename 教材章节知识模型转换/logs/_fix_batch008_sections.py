# -*- coding: utf-8 -*-
"""修正 BATCH-008 中通配节号(x)为具体小节号。"""
import json
from pathlib import Path

ROOT = Path(r"D:\Design-history-知识库\教材章节知识模型转换\11_语义复核批次\BATCH-008-CH07-GOODDESIGN\review_data")

# 按 maps 数组下标(0-based)给出目标节号
FIXES = {
    "B0401": {
        7: ("5.2", None),    # role_consume_modernity -> 5.2 美国大众消费体系
        8: ("5.5", None),    # role_professionalise_commercial_design -> 5.5 工业设计职业的形成
        9: ("9.1", None),    # role_postwar_consumer_society -> 9.1 丰裕社会与消费公民
        10: ("9.1", None),   # role_brand_consumer_culture -> 9.1 消费文化理论谱系
        11: ("11.2", None),  # role_critique_modernism -> 11.2 波普与日常商品
        12: ("11.5", None),  # role_postmodern_design_practice -> 11.5 孟菲斯及对象的叙事化
        13: ("11.7", "11.x"),  # role_japanese_postmodern_path -> 11.7 后现代的全球传播与边界；边界文本中的 11.x 一并替换
    },
    "B0415": {
        11: ("12.1", None),  # design_as_political_and_social_responsibility -> 12.1 从职业伦理到社会批判
    },
}

for sid, idx_map in FIXES.items():
    path = ROOT / f"{sid}_review.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    for idx, (new_sec, old_sec_in_text) in idx_map.items():
        row = data["maps"][idx]
        old = row[0]
        assert old.endswith(".x"), f"{sid} 条目{idx}: 节号 {old} 不是通配"
        assert not new_sec.endswith(".x")
        row[0] = new_sec
        if old_sec_in_text:
            for j in (3, 4):  # accepted_claim / evidence_boundary 中的通配节号文本
                row[j] = row[j].replace(old_sec_in_text, new_sec)
        print(f"{sid} 条目{idx}: {old} -> {new_sec}")
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{sid}: 已写回")
