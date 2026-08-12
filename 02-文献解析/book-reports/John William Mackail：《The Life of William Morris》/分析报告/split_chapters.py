import re, os

src = 'F:/Design-history-知识元/00-book/John William Mackail：《The Life of William Morris》.md'
outdir = 'F:/Design-history-知识元/report/John William Mackail：《The Life of William Morris》/分析报告/chapters'
os.makedirs(outdir, exist_ok=True)

with open(src, 'r', encoding='utf-8-sig') as f:
    content = f.read()

lines = content.split('\n')
preface_line = lines[8] if len(lines) > 8 else ''
vol1_line = lines[10] if len(lines) > 10 else ''
vol2_line = lines[12] if len(lines) > 12 else ''

# Extract preface
pm = re.match(r'^# Preface To First Edition (.*)', preface_line)
if pm:
    with open(os.path.join(outdir, '00_Preface.txt'), 'w', encoding='utf-8') as f:
        f.write(pm.group(1))
    print(f'Preface: {len(pm.group(1))} chars')

# Use exact chapter markers from grep output
vol1_markers = [
    ('I',   r'## I\. Walthamstow, Woodford, And Marlborough'),
    ('II',  r'## II\. Oxford'),
    ('III', r'## III\. The Brotherhood'),
    ('IV',  r'# IV\. Red Lion Square'),
    ('V',   r'# V\. Red House'),
    ('VI',  r'## VI\. The Earthly Paradise'),
    ('VII', r'## VII\. Morris And Kelmscott'),
    ('VIII',r'# VIII\. Journey To Iceland'),
    ('IX',  r'# IX\. Love Is Enough'),
    ('X',   r'# X\. Period Of Dyeing'),
    ('XI',  r'# XI\. The Society For Protection Of Ancient Buildings'),
]

vol2_markers = [
    ('XII',   r'# XII\. London And Kelmscott'),
    ('XIII',  r'# XIII\. Merton Abbey'),
    ('XIV',   r'# XIV\. Concentration'),
    ('XV',    r'# XV\. The Democratic Federation'),
    ('XVI',   r'# XVI\. The Socialist League'),
    ('XVII',  r'# XVII\. The Odyssey'),
    ('XVIII', r'# XVIII\. Signs Of Change'),
    ('XIX',   r'# XIX\. Passive Socialism'),
    ('XX',    r'# XX\. Printing, Romance-Writing'),
    ('XXI',   r'# XXI\. Last Years'),
    ('XXII',  r'# XXII\. Ilicet'),
]

chapter_titles = {
    'I': 'Walthamstow, Woodford, And Marlborough',
    'II': 'Oxford',
    'III': 'The Brotherhood',
    'IV': 'Red Lion Square: The Oxford Union: The Defence Of Guenevere',
    'V': 'Red House: Formation Of The Firm: The Fall Of Troy',
    'VI': 'The Earthly Paradise',
    'VII': 'Morris And Kelmscott',
    'VIII': 'Journey To Iceland',
    'IX': 'Love Is Enough: Period Of Illuminations: Dissolution Of The Firm',
    'X': 'Period Of Dyeing: The Aeneids: Sigurd The Volsung',
    'XI': 'The Society For Protection Of Ancient Buildings: The Eastern Question Association: Period Of Textiles',
    'XII': 'London And Kelmscott: Theories Of Art And Life',
    'XIII': 'Merton Abbey',
    'XIV': 'Concentration',
    'XV': 'The Democratic Federation',
    'XVI': 'The Socialist League',
    'XVII': 'The Odyssey: John Ball: Trafalgar Square',
    'XVIII': 'Signs Of Change: The Arts And Crafts: Return To Romance',
    'XIX': 'Passive Socialism: Foundation Of The Kelmscott Press',
    'XX': 'Printing, Romance-Writing, Translation, And Criticism: Final Attitude Towards Art And History',
    'XXI': 'Last Years: The Kelmscott Chaucer',
    'XXII': 'Ilicet',
}

def split_vol(vol_text, markers):
    # Find positions of all markers
    positions = []
    for num, pattern in markers:
        m = re.search(pattern, vol_text)
        if m:
            positions.append((num, m.start()))
            print(f'  Found Ch{num} at position {m.start()}')
        else:
            print(f'  MISSING Ch{num}')

    # Sort by position
    positions.sort(key=lambda x: x[1])

    results = []
    for i, (num, start) in enumerate(positions):
        if i + 1 < len(positions):
            end = positions[i+1][1]
        else:
            end = len(vol_text)
        ch_text = vol_text[start:end].strip()

        # Remove the heading line (everything up to the year range or first sentence)
        # Pattern: "## I. Walthamstow, Woodford, And Marlborough 1834-1852 " or "# IV. Red Lion Square: The Oxford Union..."
        ch_text = re.sub(r'^(#{1,2} [IVX]+\. [^\d]*\d{4}[–\-]\d{4}\s*)', '', ch_text, count=1)
        # If no year range found, just remove heading without years
        ch_text = re.sub(r'^(#{1,2} [IVX]+\.[A-Za-z, &;:\-]+(?:\d{4}[–\-]\d{4})?\s*)', '', ch_text, count=1)

        title = chapter_titles.get(num, f'Chapter {num}')
        safe_title = title[:60].replace(":","-").replace(" ","_").replace(",","").replace(";","")
        fname = f'Ch{num}_{safe_title}.txt'
        filepath = os.path.join(outdir, fname)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(ch_text)
        print(f'  -> Ch{num}: {len(ch_text)} chars')
        results.append((num, title, len(ch_text), filepath))
    return results

print('=== Volume I ===')
r1 = split_vol(vol1_line, vol1_markers)
print('=== Volume II ===')
r2 = split_vol(vol2_line, vol2_markers)

print('\nDone!')
