# Fy1 (2026-11-20): raka citattecken i uppgiftstexten blir svenska ” ” (samma regel som matf1_las3.py).
import os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

POT = None
R = {}
for u in Bank('fy1').arr:
    t = re.sub(r'<[^>]*>', ' ', re.sub(r'<svg[\s\S]*?</svg>', '', u.get('t') or ''))
    for m in re.finditer(r'"([^"<>]{1,120})"', t):
        if '\\' in m.group(0) and not re.search(r'[a-zåäö]', m.group(1)):
            continue
        R.setdefault(u['id'], {'ers': []})['ers'].append((m.group(0), '”' + m.group(1) + '”'))
