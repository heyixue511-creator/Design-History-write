# -*- coding: utf-8 -*-
"""
Generate all analysis reports for Judy Attfield's "Wild Things" (2000).
Outputs 11 reports: 00_整体分析报告 + 01-09 per-chapter + NN_专项报告与实体总索引
"""
import re, os, json

BASE = os.path.dirname(os.path.abspath(__file__))
WORK = BASE  # same directory
OUT = os.path.join(os.path.dirname(BASE))  # report directory itself

CHAPTER_NAMES = {
    'intro_book': 'Introduction: The material culture of everyday life',
    'ch01': 'Chapter 1: The meaning of design: Things with attitude',
    'ch02': 'Chapter 2: The meaning of things: Design in the lower case',
    'ch03': 'Chapter 3: Things and the dynamics of social change',
    'ch04': 'Chapter 4: Continuity: Authenticity and the paradoxical nature of reproduction',
    'ch05': 'Chapter 5: Change: The ephemeral materiality of identity',
    'ch06': 'Chapter 6: Containment: The ecology of personal possessions',
    'ch07': 'Chapter 7: Space: Where things take place',
    'ch08': 'Chapter 8: Time: Bringing things to life',
    'ch09': 'Chapter 9: The body: The threshold between nature and culture',
}

# Chinese chapter titles
CN_TITLES = {
    'intro_book': '导论：日常生活的物质文化',
    'ch01': '第一章：设计的意义——有态度的物',
    'ch02': '第二章：物的意义——小写设计',
    'ch03': '第三章：物与社会变迁的动力',
    'ch04': '第四章：连续性——本真性与复制的悖论本质',
    'ch05': '第五章：变化——身份的短暂物质性',
    'ch06': '第六章：容纳——个人财物的生态学',
    'ch07': '第七章：空间——物之所在',
    'ch08': '第八章：时间——赋予物以生命',
    'ch09': '第九章：身体——自然与文化之间的门槛',
}

def read_chapter(name):
    fpath = os.path.join(WORK, f'{name}.txt')
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            return f.read()
    return ''

def extract_sections(content):
    """Extract ## level sections from chapter content"""
    sections = []
    pattern = r'##\s+(.+?)(?=\s*<sup>|\.\s+[A-Z]|$)'
    for m in re.finditer(pattern, content):
        title = m.group(1).strip()
        start = m.start()
        sections.append({'title': title, 'start': start})
    return sections

def extract_quotes(content, min_len=30, max_len=400):
    """Extract quoted phrases using Unicode smart quotes"""
    quotes = re.findall(r'‘([^’]{' + str(min_len) + ',' + str(max_len) + r'}?)’', content)
    return [q.strip() for q in quotes if len(q.strip()) > min_len]

def extract_people(content):
    """Extract likely person names"""
    # Find patterns like "First Last" (proper nouns)
    names = set()
    # People often cited with full names before citations
    pattern = r'(?:^|[.;])\s+([A-Z][a-z]+(?:\s+(?:van\s+|de\s+|la\s+)?[A-Z][a-z]+)+)'
    for m in re.finditer(pattern, content):
        name = m.group(1).strip()
        # Filter out common non-person terms
        skip_words = ['The ', 'This ', 'These ', 'That ', 'Those ', 'There ', 'Part ', 'Chapter ',
                      'However ', 'Although ', 'Nevertheless ', 'Furthermore ', 'Moreover ',
                      'British ', 'French ', 'American ', 'English ', 'First World War',
                      'Christmas Gifts', 'Band Aid', 'Berlin Wall', 'Buenos Aires']
        if len(name) > 8 and not any(name.startswith(w) for w in skip_words):
            names.add(name)
    return sorted(names)

def extract_objects(content):
    """Extract mentioned physical objects/artefacts"""
    objects = set()
    # Common object patterns in the text
    obj_patterns = [
        r'(?:the|a|an)\s+([a-z]+\s(?:chair|table|desk|bed|sofa|cabinet|dressing\s+table|wardrobe|sideboard|chest|furniture|house|home|car|radio|computer|telephone|television|cloth|dress|garment|costume|knife|fork|spoon|tool|machine|appliance|device|gadget|ornament|vase|picture|painting|carpet|curtain|lamp|light|mirror|clock|watch))',
    ]
    for pat in obj_patterns:
        for m in re.finditer(pat, content, re.IGNORECASE):
            objects.add(m.group(1).strip().lower())
    return sorted(objects)

def extract_theories(content):
    """Extract theoretical concepts and frameworks"""
    # Find capitalized multi-word concepts
    theories = set()
    # Academic theories often capitalized
    pattern = r'([A-Z][a-z]+(?:\s+(?:[A-Z][a-z]+|of|and|the|in|to|as|for)){2,})'
    for m in re.finditer(pattern, content):
        phrase = m.group(1).strip()
        if 10 < len(phrase) < 200:
            theories.add(phrase)
    return sorted(theories)

def extract_citation_count(content):
    return len(re.findall(r'<sup>\d+</sup>', content))

def extract_numbered_sections(content):
    """Extract sections with explicit numbering or clear section breaks"""
    # Find sentences that start sections (after a period, followed by a capital letter and section-like language)
    return []

def get_chapter_overview(ch_name):
    """Get chapter overview data"""
    content = read_chapter(ch_name)
    sections = extract_sections(content)
    quotes = extract_quotes(content)
    citation_count = extract_citation_count(content)

    # Get first and last few sentences
    first_500 = content[:500]
    last_500 = content[-500:]

    return {
        'name': ch_name,
        'en_title': CHAPTER_NAMES.get(ch_name, ch_name),
        'cn_title': CN_TITLES.get(ch_name, ch_name),
        'char_count': len(content),
        'section_count': len(sections),
        'sections': sections,
        'citation_count': citation_count,
        'quote_count': len(quotes),
        'sample_quotes': quotes[:20],
        'first_500': first_500,
        'last_500': last_500,
    }

# Run extraction on all chapters
if __name__ == '__main__':
    all_data = {}
    for ch_name in ['ch01', 'ch02', 'ch03', 'ch04', 'ch05', 'ch06', 'ch07', 'ch08', 'ch09']:
        data = get_chapter_overview(ch_name)
        all_data[ch_name] = data
        print(f"{data['cn_title']}: {data['char_count']} chars, {data['section_count']} sections, {data['citation_count']} citations, {data['quote_count']} quotes")

    # Save as JSON for reference
    with open(os.path.join(WORK, 'extracted_data.json'), 'w', encoding='utf-8') as f:
        # Convert to serializable format
        json.dump({k: {kk: vv for kk, vv in v.items() if kk != 'sample_quotes'} for k, v in all_data.items()}, f, ensure_ascii=False, indent=2)

    print("\nData extraction complete!")
