# Ma5 handgenomläsning: talteori, talföljder och bevis (2026-11-20).
# Raka citattecken blir svenska ” ”; "Du får använda potenser …" är en svarsinstruktion och flyttas till kgInstruktion.
import os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

POT = ' Du får använda potenser eller upprepa faktorerna.'
R = {}  # 2.79, 2.157, 2.209 behåller POT i texten (felrapportbeslut), se matf1_las6.py
for u in Bank('matf1').arr:
    t = re.sub(r'<[^>]*>', ' ', re.sub(r'<svg[\s\S]*?</svg>', '', u.get('t') or ''))
    for m in re.finditer(r'"([^"<>]{1,120})"', t):
        if '\\' in m.group(0) and not re.search(r'[a-zåäö]', m.group(1)):
            continue
        R.setdefault(u['id'], {'ers': []})['ers'].append((m.group(0), '”' + m.group(1) + '”'))
