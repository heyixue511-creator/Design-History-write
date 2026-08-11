#!/usr/bin/env python3
"""Build the auditable first-pass textbook knowledge-model assets.

This script performs mechanical full-file reading, inventory, outline parsing,
duplicate detection, and similarity-based routing. It never promotes a machine
candidate to an accepted textbook reference.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path
from typing import Iterable


KB_ROOT = Path(r"D:\Design-history-知识库")
BOOK_REPORT = KB_ROOT / "report-book"
PAPER_REPORT = KB_ROOT / "report-paper"
BOOK_CLEAN = KB_ROOT / "00-book_clean"
PAPER_CLEAN = KB_ROOT / "00-paper_clean"
OUTLINE = KB_ROOT / "教材总纲-现当代设计史（设计学理论专业）.md"
DEFAULT_OUTPUT = KB_ROOT / "教材章节知识模型转换"

CHINESE_NUMERALS = {
    "一": 1,
    "二": 2,
    "三": 3,
    "四": 4,
    "五": 5,
    "六": 6,
    "七": 7,
    "八": 8,
    "九": 9,
    "十": 10,
    "十一": 11,
    "十二": 12,
    "十三": 13,
    "十四": 14,
    "十五": 15,
    "十六": 16,
}

STOP_FEATURES = {
    "设计",
    "历史",
    "现代",
    "当代",
    "本章",
    "章节",
    "问题",
    "核心",
    "材料",
    "研究",
    "分析",
    "关系",
    "方法",
    "如何",
    "以及",
    "通过",
    "形成",
    "进入",
    "the",
    "and",
    "design",
    "history",
}


@dataclass
class Section:
    section_id: str
    chapter_id: str
    chapter_title: str
    title: str
    description: str
    core_question: str
    core_thesis: str

    @property
    def query(self) -> str:
        return " ".join(
            [
                self.chapter_title,
                self.title,
                self.description,
                self.core_question,
                self.core_thesis,
            ]
        )


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def ensure_dirs(output: Path) -> dict[str, Path]:
    dirs = {
        "inventory": output / "01_语料清单",
        "outline": output / "02_总纲知识结构化",
        "source_cards": output / "03_来源清单与来源卡",
        "mapping": output / "04_文献—章节映射",
        "evidence": output / "05_原子证据卡",
        "matrix": output / "06_核心命题—证据矩阵",
        "entities": output / "07_实体与关系网络",
        "causal": output / "08_历史机制链与争议矩阵",
        "packages": output / "09_章节写作包",
        "gaps": output / "10_证据缺口与审计",
        "logs": output / "logs",
    }
    for directory in dirs.values():
        directory.mkdir(parents=True, exist_ok=True)
    return dirs


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_bytes_text(path: Path) -> tuple[bytes, str]:
    data = path.read_bytes()
    for encoding in ("utf-8-sig", "utf-8", "utf-16"):
        try:
            return data, data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return data, data.decode("utf-8", errors="replace")


def normalize_name(value: str) -> str:
    value = value.lower()
    value = re.sub(r"(?:_paged)?_clean$", "", value)
    value = re.sub(r"\.(?:md|txt)$", "", value)
    return re.sub(r"[^0-9a-z\u4e00-\u9fff]+", "", value)


def match_clean_file(folder_name: str, clean_files: list[Path]) -> tuple[Path | None, float]:
    target = normalize_name(folder_name)
    exact = [p for p in clean_files if normalize_name(p.stem) == target]
    if exact:
        return exact[0], 1.0
    prefix = [
        p
        for p in clean_files
        if normalize_name(p.stem).startswith(target) or target.startswith(normalize_name(p.stem))
    ]
    if prefix:
        prefix.sort(key=lambda p: abs(len(normalize_name(p.stem)) - len(target)))
        return prefix[0], 0.95
    best_path: Path | None = None
    best_score = 0.0
    for path in clean_files:
        score = SequenceMatcher(None, target, normalize_name(path.stem)).ratio()
        if score > best_score:
            best_score = score
            best_path = path
    if best_score >= 0.72:
        return best_path, round(best_score, 4)
    return None, round(best_score, 4)


def classify_report_file(relative: Path) -> str:
    name = relative.name
    parent = relative.parent.name
    if relative.parent == Path(".") and name == "分析报告.md":
        return "legacy_root_report"
    if parent == "分析报告":
        if name == "00_整体分析报告.md":
            return "overall_report"
        if "专项报告与实体总索引" in name:
            return "special_entity_index"
        return "chapter_or_full_report"
    if parent == "知识涌现分析":
        if name.startswith("00_"):
            return "emergence_method_or_overview"
        if name.startswith("01_"):
            return "emergence_semantic_units"
        if name.startswith("02_"):
            return "emergence_link_network"
        if name.startswith("03_"):
            return "emergence_computation"
        if name.startswith("04_"):
            return "emergence_discovery"
        return "emergence_variant"
    return "other"


def material_type(corpus: str, folder_name: str) -> str:
    if corpus == "book":
        return "book_or_book_length_source"
    lowered = folder_name.lower()
    if "review" in lowered or "书评" in folder_name:
        return "book_review"
    if "call for" in lowered or "征稿" in folder_name:
        return "call_for_papers"
    if "publisher" in lowered or "blurb" in lowered or "书介" in folder_name:
        return "publisher_or_web_description"
    return "paper_or_other_research_source_unverified"


def extract_heading_content(block_lines: list[str], heading: str) -> str:
    capture = False
    collected: list[str] = []
    for line in block_lines:
        if line.startswith("### "):
            if capture:
                break
            capture = line.strip() == f"### {heading}"
            continue
        if capture and line.strip() and not line.strip().startswith("---"):
            collected.append(line.strip())
    return " ".join(collected)


def chapter_id_from_title(title: str) -> str:
    if title.startswith("导论"):
        return "CH00"
    if title.startswith("结语"):
        return "CH99"
    match = re.match(r"第([一二三四五六七八九十]+)章", title)
    if not match:
        return "CHXX"
    number = CHINESE_NUMERALS.get(match.group(1))
    return f"CH{number:02d}" if number is not None else "CHXX"


def parse_outline(path: Path) -> tuple[list[dict], list[Section]]:
    text = path.read_text(encoding="utf-8-sig")
    lines = text.splitlines()
    starts: list[tuple[int, str]] = []
    for idx, line in enumerate(lines):
        if re.match(r"^## (?:导论|第[一二三四五六七八九十]+章|结语)", line):
            starts.append((idx, line[3:].strip()))
    chapters: list[dict] = []
    sections: list[Section] = []
    section_re = re.compile(
        r"^\d+\.\s+\*\*((?:\d{1,2})\.(?:\d{1,2}))\s+([^*]+)\*\*(?:[：:]\s*(.*))?$"
    )
    for pos, (start, title) in enumerate(starts):
        end = starts[pos + 1][0] if pos + 1 < len(starts) else len(lines)
        block = lines[start:end]
        chapter_id = chapter_id_from_title(title)
        core_question = extract_heading_content(block, "核心问题")
        core_thesis = extract_heading_content(block, "核心论点")
        chapter_sections: list[dict] = []
        for line_idx, line in enumerate(block):
            match = section_re.match(line.strip())
            if not match:
                continue
            section_id, section_title, description = match.groups()
            description = (description or "").strip()
            if not description:
                for following in block[line_idx + 1 :]:
                    stripped = following.strip()
                    if not stripped:
                        continue
                    if stripped.startswith("### ") or section_re.match(stripped):
                        break
                    description = stripped
                    break
            item = Section(
                section_id=section_id,
                chapter_id=chapter_id,
                chapter_title=title,
                title=section_title.strip(),
                description=description,
                core_question=core_question,
                core_thesis=core_thesis,
            )
            sections.append(item)
            chapter_sections.append(
                {
                    "section_id": section_id,
                    "title": item.title,
                    "description": item.description,
                }
            )
        if not chapter_sections and chapter_id == "CH99":
            item = Section(
                section_id="C.0",
                chapter_id=chapter_id,
                chapter_title=title,
                title="结语综合",
                description="从正典转向关系、责任、证据与可能性的全书回收",
                core_question=core_question,
                core_thesis=core_thesis,
            )
            sections.append(item)
            chapter_sections.append(
                {"section_id": item.section_id, "title": item.title, "description": item.description}
            )
        chapters.append(
            {
                "chapter_id": chapter_id,
                "title": title,
                "core_question": core_question,
                "core_thesis": core_thesis,
                "sections": chapter_sections,
            }
        )
    return chapters, sections


def write_outline_assets(dirs: dict[str, Path], chapters: list[dict], sections: list[Section]) -> None:
    (dirs["outline"] / "章节树.json").write_text(
        json.dumps({"generated_at": utc_now(), "chapters": chapters}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    with (dirs["outline"] / "章节需求总表.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            ["chapter_id", "chapter_title", "section_id", "section_title", "description", "core_question", "core_thesis"]
        )
        for section in sections:
            writer.writerow(
                [
                    section.chapter_id,
                    section.chapter_title,
                    section.section_id,
                    section.title,
                    section.description,
                    section.core_question,
                    section.core_thesis,
                ]
            )
    for chapter in chapters:
        lines = [
            f"# {chapter['chapter_id']} {chapter['title']}",
            "",
            "## 核心问题",
            "",
            chapter["core_question"] or "待从总纲补充。",
            "",
            "## 核心论点",
            "",
            chapter["core_thesis"] or "待从总纲补充。",
            "",
            "## 小节需求",
            "",
            "| 节ID | 标题 | 总纲说明 | 正式文献状态 |",
            "|---|---|---|---|",
        ]
        for section in chapter["sections"]:
            lines.append(
                f"| {section['section_id']} | {section['title']} | {section['description']} | 尚未完成语义复核 |"
            )
        lines.extend(
            [
                "",
                "## 建模状态",
                "",
                "本文件由总纲机械解析生成。核心命题、关系链、反例和证据准入将在逐来源语义复核后补充。",
            ]
        )
        safe_name = re.sub(r"[<>:\"/\\|?*]", "_", f"{chapter['chapter_id']}_{chapter['title']}")
        (dirs["outline"] / f"{safe_name}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def query_features(text: str) -> Counter[str]:
    features: Counter[str] = Counter()
    lowered = text.lower()
    for token in re.findall(r"[a-z][a-z0-9_-]{2,}", lowered):
        if token not in STOP_FEATURES:
            features[token] += 1
    for run in re.findall(r"[\u4e00-\u9fff]+", lowered):
        for size in (2, 3):
            for idx in range(0, len(run) - size + 1):
                token = run[idx : idx + size]
                if token not in STOP_FEATURES:
                    features[token] += 1
    return features


def weighted_section_query(section: Section) -> Counter[str]:
    """Build a section-first routing query without erasing chapter context.

    Section title and description identify the actual textbook node. Chapter
    title, core question, and thesis are retained only as background signals so
    one general-history source does not dominate every section in a chapter.
    """
    weighted: Counter[str] = Counter()
    fields = (
        (section.title, 6.0),
        (section.description, 5.0),
        (section.chapter_title, 2.0),
        (section.core_question, 0.5),
        (section.core_thesis, 0.5),
    )
    for text, weight in fields:
        weighted.update({feature: count * weight for feature, count in query_features(text).items()})
    return weighted


def document_features(text: str, allowed: set[str]) -> Counter[str]:
    features: Counter[str] = Counter()
    lowered = text.lower()
    for token in re.findall(r"[a-z][a-z0-9_-]{2,}", lowered):
        if token in allowed:
            features[token] += 1
    for run in re.findall(r"[\u4e00-\u9fff]+", lowered):
        for size in (2, 3):
            for idx in range(0, len(run) - size + 1):
                token = run[idx : idx + size]
                if token in allowed:
                    features[token] += 1
    return features


def file_weight(category: str) -> float:
    return {
        "overall_report": 3.0,
        "chapter_or_full_report": 2.0,
        "special_entity_index": 2.0,
        "emergence_discovery": 1.5,
        "emergence_semantic_units": 1.2,
        "emergence_link_network": 1.0,
        "emergence_computation": 0.8,
        "emergence_method_or_overview": 0.5,
        "emergence_variant": 1.0,
        "legacy_root_report": 0.5,
        "other": 0.3,
    }.get(category, 0.5)


def weighted_cosine(document: Counter[str], query: Counter[str], idf: dict[str, float]) -> float:
    dot = 0.0
    doc_norm = 0.0
    query_norm = 0.0
    keys = set(query)
    for feature in keys:
        weight = idf.get(feature, 1.0)
        dv = math.log1p(document.get(feature, 0.0)) * weight
        qv = math.log1p(query[feature]) * weight
        dot += dv * qv
        doc_norm += dv * dv
        query_norm += qv * qv
    if not doc_norm or not query_norm:
        return 0.0
    return dot / math.sqrt(doc_norm * query_norm)


def write_csv(path: Path, fieldnames: list[str], rows: Iterable[dict]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def build_inventory_and_profiles(
    dirs: dict[str, Path], sections: list[Section]
) -> tuple[list[dict], list[dict], list[Counter[str]], list[dict]]:
    clean_by_corpus = {
        "book": sorted(BOOK_CLEAN.glob("*.md"), key=lambda p: p.name.casefold()),
        "paper": sorted(PAPER_CLEAN.glob("*.md"), key=lambda p: p.name.casefold()),
    }
    report_by_corpus = {"book": BOOK_REPORT, "paper": PAPER_REPORT}
    query_vectors = [weighted_section_query(section) for section in sections]
    allowed_features = set().union(*(set(vector) for vector in query_vectors))
    sources: list[dict] = []
    file_rows: list[dict] = []
    document_vectors: list[Counter[str]] = []
    structure_exceptions: list[dict] = []
    source_counter = {"book": 0, "paper": 0}

    for corpus in ("book", "paper"):
        root = report_by_corpus[corpus]
        for folder in sorted((p for p in root.iterdir() if p.is_dir()), key=lambda p: p.name.casefold()):
            source_counter[corpus] += 1
            source_id = f"{'B' if corpus == 'book' else 'P'}{source_counter[corpus]:04d}"
            clean_path, match_confidence = match_clean_file(folder.name, clean_by_corpus[corpus])
            clean_hash = None
            if clean_path:
                clean_hash = hashlib.sha256(clean_path.read_bytes()).hexdigest()
            report_files = sorted((p for p in folder.rglob("*") if p.is_file()), key=lambda p: str(p).casefold())
            vector: Counter[str] = Counter()
            vector.update({k: v * 5.0 for k, v in document_features(folder.name, allowed_features).items()})
            file_records: list[dict] = []
            categories: Counter[str] = Counter()
            total_chars = 0
            total_lines = 0
            replacement_chars = 0
            for path in report_files:
                relative = path.relative_to(folder)
                category = classify_report_file(relative)
                categories[category] += 1
                data, text = read_bytes_text(path)
                sha = sha256_bytes(data)
                line_count = text.count("\n") + (1 if text else 0)
                heading_count = sum(1 for line in text.splitlines() if re.match(r"^#{1,6}\s", line))
                replacements = text.count("\ufffd")
                total_chars += len(text)
                total_lines += line_count
                replacement_chars += replacements
                features = document_features(text, allowed_features)
                weight = file_weight(category)
                for feature, count in features.items():
                    vector[feature] += count * weight
                record = {
                    "source_id": source_id,
                    "corpus": corpus,
                    "source_folder": folder.name,
                    "relative_path": str(relative),
                    "category": category,
                    "size_bytes": len(data),
                    "sha256": sha,
                    "characters": len(text),
                    "physical_lines": line_count,
                    "markdown_headings": heading_count,
                    "replacement_characters": replacements,
                    "machine_read_status": "complete",
                    "semantic_review_status": "pending",
                }
                file_records.append(record)
                file_rows.append(record)

            has_overall = categories["overall_report"] == 1
            has_special = categories["special_entity_index"] >= 1
            emergence_count = sum(
                count for key, count in categories.items() if key.startswith("emergence_")
            )
            notes: list[str] = []
            if not has_overall:
                notes.append("missing_overall_report")
            if not has_special:
                notes.append("missing_special_entity_index")
            if emergence_count != 5:
                notes.append(f"emergence_file_count={emergence_count}")
            if clean_path is None:
                notes.append("clean_source_not_matched")
            if replacement_chars:
                notes.append(f"replacement_characters={replacement_chars}")
            if notes:
                structure_exceptions.append(
                    {"source_id": source_id, "corpus": corpus, "folder_name": folder.name, "notes": ";".join(notes)}
                )
            source = {
                "source_id": source_id,
                "corpus": corpus,
                "folder_name": folder.name,
                "material_type": material_type(corpus, folder.name),
                "clean_source_path": str(clean_path) if clean_path else None,
                "clean_match_confidence": match_confidence,
                "clean_source_sha256": clean_hash,
                "duplicate_group": None,
                "report_structure": {
                    "file_count": len(report_files),
                    "categories": dict(categories),
                    "has_overall_report": has_overall,
                    "has_special_entity_index": has_special,
                    "emergence_file_count": emergence_count,
                    "total_characters": total_chars,
                    "total_physical_lines": total_lines,
                    "replacement_characters": replacement_chars,
                },
                "files": file_records,
                "candidate_sections": [],
                "review_status": "machine_read_complete",
                "evidence_level": "V2",
                "notes": notes,
            }
            sources.append(source)
            document_vectors.append(vector)

    hashes: dict[str, list[int]] = defaultdict(list)
    for idx, source in enumerate(sources):
        if source["clean_source_sha256"]:
            hashes[source["clean_source_sha256"]].append(idx)
    duplicate_rows: list[dict] = []
    group_no = 0
    for sha, indices in sorted(hashes.items()):
        if len(indices) < 2:
            continue
        group_no += 1
        group_id = f"DUP{group_no:04d}"
        for idx in indices:
            sources[idx]["duplicate_group"] = group_id
            duplicate_rows.append(
                {
                    "duplicate_group": group_id,
                    "sha256": sha,
                    "source_id": sources[idx]["source_id"],
                    "corpus": sources[idx]["corpus"],
                    "folder_name": sources[idx]["folder_name"],
                    "clean_source_path": sources[idx]["clean_source_path"],
                }
            )

    write_csv(
        dirs["inventory"] / "文件读取台账.csv",
        [
            "source_id",
            "corpus",
            "source_folder",
            "relative_path",
            "category",
            "size_bytes",
            "sha256",
            "characters",
            "physical_lines",
            "markdown_headings",
            "replacement_characters",
            "machine_read_status",
            "semantic_review_status",
        ],
        file_rows,
    )
    write_csv(
        dirs["inventory"] / "重复原文组.csv",
        ["duplicate_group", "sha256", "source_id", "corpus", "folder_name", "clean_source_path"],
        duplicate_rows,
    )
    write_csv(
        dirs["inventory"] / "结构异常与待核清单.csv",
        ["source_id", "corpus", "folder_name", "notes"],
        structure_exceptions,
    )
    return sources, file_rows, document_vectors, query_vectors


def build_candidates(
    dirs: dict[str, Path], sources: list[dict], document_vectors: list[Counter[str]], sections: list[Section], query_vectors: list[Counter[str]]
) -> tuple[list[dict], list[dict]]:
    source_count = len(sources)
    document_frequency: Counter[str] = Counter()
    for vector in document_vectors:
        for feature in vector:
            document_frequency[feature] += 1
    idf = {
        feature: math.log((source_count + 1) / (frequency + 1)) + 1.0
        for feature, frequency in document_frequency.items()
    }
    all_scores: list[list[float]] = []
    source_to_section: list[dict] = []
    for source, vector in zip(sources, document_vectors):
        scores = [weighted_cosine(vector, query, idf) for query in query_vectors]
        all_scores.append(scores)
        ranked = sorted(range(len(scores)), key=lambda idx: scores[idx], reverse=True)[:8]
        candidates: list[dict] = []
        for rank, section_idx in enumerate(ranked, 1):
            section = sections[section_idx]
            score = scores[section_idx]
            if score >= 0.35:
                band = "strong_machine_candidate"
            elif score >= 0.20:
                band = "machine_candidate"
            elif score >= 0.08:
                band = "weak_machine_candidate"
            else:
                band = "unmatched_needs_manual_review"
            row = {
                "source_id": source["source_id"],
                "corpus": source["corpus"],
                "folder_name": source["folder_name"],
                "rank": rank,
                "section_id": section.section_id,
                "chapter_id": section.chapter_id,
                "chapter_title": section.chapter_title,
                "section_title": section.title,
                "similarity_score": round(score, 6),
                "candidate_band": band,
                "mapping_grade": "UNREVIEWED",
                "status": "candidate_needs_review",
                "rationale": "字符n-gram与英文术语相似度生成；尚未完成语义、版本和证据权限复核。",
            }
            source_to_section.append(row)
            candidates.append(
                {
                    "rank": rank,
                    "section_id": section.section_id,
                    "score": round(score, 6),
                    "candidate_band": band,
                    "status": "candidate_needs_review",
                }
            )
        source["candidate_sections"] = candidates

    section_to_source: list[dict] = []
    for section_idx, section in enumerate(sections):
        ranked_sources = sorted(
            range(len(sources)), key=lambda idx: all_scores[idx][section_idx], reverse=True
        )[:30]
        for rank, source_idx in enumerate(ranked_sources, 1):
            source = sources[source_idx]
            section_to_source.append(
                {
                    "section_id": section.section_id,
                    "chapter_id": section.chapter_id,
                    "chapter_title": section.chapter_title,
                    "section_title": section.title,
                    "rank": rank,
                    "source_id": source["source_id"],
                    "corpus": source["corpus"],
                    "folder_name": source["folder_name"],
                    "similarity_score": round(all_scores[source_idx][section_idx], 6),
                    "mapping_grade": "UNREVIEWED",
                    "status": "candidate_needs_review",
                }
            )

    write_csv(
        dirs["mapping"] / "机器候选_来源到章节.csv",
        [
            "source_id",
            "corpus",
            "folder_name",
            "rank",
            "section_id",
            "chapter_id",
            "chapter_title",
            "section_title",
            "similarity_score",
            "candidate_band",
            "mapping_grade",
            "status",
            "rationale",
        ],
        source_to_section,
    )
    write_csv(
        dirs["mapping"] / "机器候选_章节到来源.csv",
        [
            "section_id",
            "chapter_id",
            "chapter_title",
            "section_title",
            "rank",
            "source_id",
            "corpus",
            "folder_name",
            "similarity_score",
            "mapping_grade",
            "status",
        ],
        section_to_source,
    )
    return source_to_section, section_to_source


def write_source_assets(dirs: dict[str, Path], sources: list[dict]) -> None:
    with (dirs["source_cards"] / "来源资产总表.jsonl").open("w", encoding="utf-8") as handle:
        for source in sources:
            handle.write(json.dumps(source, ensure_ascii=False) + "\n")
    rows = []
    for source in sources:
        structure = source["report_structure"]
        rows.append(
            {
                "source_id": source["source_id"],
                "corpus": source["corpus"],
                "folder_name": source["folder_name"],
                "material_type": source["material_type"],
                "clean_source_path": source["clean_source_path"],
                "clean_match_confidence": source["clean_match_confidence"],
                "duplicate_group": source["duplicate_group"],
                "report_file_count": structure["file_count"],
                "report_characters": structure["total_characters"],
                "report_lines": structure["total_physical_lines"],
                "review_status": source["review_status"],
                "evidence_level": source["evidence_level"],
                "notes": ";".join(source["notes"]),
            }
        )
    write_csv(
        dirs["source_cards"] / "来源资产总表.csv",
        [
            "source_id",
            "corpus",
            "folder_name",
            "material_type",
            "clean_source_path",
            "clean_match_confidence",
            "duplicate_group",
            "report_file_count",
            "report_characters",
            "report_lines",
            "review_status",
            "evidence_level",
            "notes",
        ],
        rows,
    )


def write_chapter_candidate_indexes(dirs: dict[str, Path], sections: list[Section], section_rows: list[dict]) -> None:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in section_rows:
        grouped[row["section_id"]].append(row)
    chapters: dict[str, list[Section]] = defaultdict(list)
    for section in sections:
        chapters[section.chapter_id].append(section)
    for chapter_id, chapter_sections in chapters.items():
        title = chapter_sections[0].chapter_title
        lines = [
            f"# {chapter_id} {title}：机器候选来源",
            "",
            "> 本文件仅用于路由。所有条目均为`UNREVIEWED`，不得直接写入正式参考文献或教材正文。",
            "",
        ]
        for section in chapter_sections:
            lines.extend(
                [
                    f"## {section.section_id} {section.title}",
                    "",
                    f"总纲说明：{section.description}",
                    "",
                    "| 排名 | 来源ID | 类型 | 相似度 | 来源目录 |",
                    "|---:|---|---|---:|---|",
                ]
            )
            for row in grouped.get(section.section_id, []):
                folder = row["folder_name"].replace("|", "／")
                lines.append(
                    f"| {row['rank']} | {row['source_id']} | {row['corpus']} | {row['similarity_score']:.6f} | {folder} |"
                )
            lines.append("")
        safe_title = re.sub(r"[<>:\"/\\|?*]", "_", title)
        (dirs["mapping"] / f"{chapter_id}_{safe_title}_机器候选.md").write_text(
            "\n".join(lines) + "\n", encoding="utf-8"
        )


def write_summary(
    dirs: dict[str, Path], sources: list[dict], file_rows: list[dict], sections: list[Section], source_rows: list[dict]
) -> None:
    corpus_counts = Counter(source["corpus"] for source in sources)
    category_counts = Counter(row["category"] for row in file_rows)
    candidate_bands = Counter(row["candidate_band"] for row in source_rows)
    duplicate_sources = sum(1 for source in sources if source["duplicate_group"])
    summary = {
        "generated_at": utc_now(),
        "source_directories": len(sources),
        "book_directories": corpus_counts["book"],
        "paper_directories": corpus_counts["paper"],
        "report_files_machine_read": len(file_rows),
        "report_characters_machine_read": sum(row["characters"] for row in file_rows),
        "outline_sections": len(sections),
        "machine_candidate_rows": len(source_rows),
        "duplicate_group_members": duplicate_sources,
        "file_categories": dict(category_counts),
        "candidate_bands": dict(candidate_bands),
        "semantic_review_complete_sources": 0,
        "warning": "机器读取完成不等于语义复核完成；候选映射不得直接用作正式参考文献索引。",
    }
    (dirs["logs"] / "initial-build-summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    lines = [
        "# 第一轮建模生成报告",
        "",
        f"- 生成时间：{summary['generated_at']}",
        f"- 来源目录：{summary['source_directories']}（书籍{summary['book_directories']}；论文库来源{summary['paper_directories']}）",
        f"- 完成机器读取的报告文件：{summary['report_files_machine_read']}",
        f"- 机器读取字符数：{summary['report_characters_machine_read']:,}",
        f"- 教材章／节节点：{summary['outline_sections']}",
        f"- 来源→章节候选记录：{summary['machine_candidate_rows']}",
        f"- 进入重复组的来源：{summary['duplicate_group_members']}",
        "",
        "## 状态边界",
        "",
        "本轮已完成逐文件机械读取、哈希、结构识别和候选路由；尚未完成589个来源的逐项语义复核。所有候选映射均为`UNREVIEWED`，不能直接用于正文或出版参考文献。",
        "",
        "## 下一步",
        "",
        "按来源批次读取整体、逐章、专项和知识涌现内容，填写来源卡中的支持命题、不能外推、争议、章节角色和A—D／X等级；随后抽取V2原子证据卡并对承担核心论点的材料返回原文核验。",
    ]
    (dirs["logs"] / "第一轮建模生成报告.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    output = args.output.resolve()
    dirs = ensure_dirs(output)
    chapters, sections = parse_outline(OUTLINE)
    write_outline_assets(dirs, chapters, sections)
    sources, file_rows, document_vectors, query_vectors = build_inventory_and_profiles(dirs, sections)
    source_rows, section_rows = build_candidates(
        dirs, sources, document_vectors, sections, query_vectors
    )
    write_source_assets(dirs, sources)
    write_chapter_candidate_indexes(dirs, sections, section_rows)
    write_summary(dirs, sources, file_rows, sections, source_rows)
    print(
        json.dumps(
            {
                "output": str(output),
                "sources": len(sources),
                "files_read": len(file_rows),
                "sections": len(sections),
                "candidate_rows": len(source_rows),
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
