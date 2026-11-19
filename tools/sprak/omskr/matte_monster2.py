# Matte (alla banker), 2026-11-19, fynd från handgenomläsningen av Ma3c kap 2:
# "Funktionen är \[f(x)=" och "Funktionerna är \(f(x)=…\) och \(g(x)=…\)" → "… ges av …", "På vilka punkter" → "I vilka punkter",
# "parablen" → "parabeln", "+0" sist i ett uttryck (3x^2+0) bort.
# Körs per bank: SPRAKBANK=mato1 python tools/sprak/apply.py mato1 tools/sprak/omskr/matte_monster2.py
import os, sys, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

BANK = os.environ.get('SPRAKBANK', 'mato1')
REGLER = [
    (re.compile(r'(Funktionen|Polynomet) är(\s*</p>\s*<p>\s*|\s*)\\\[([A-Za-z])\(([a-z])\)='),
     lambda m: f'{m.group(1)} \\({m.group(3)}\\) ges av{m.group(2)}\\[{m.group(3)}({m.group(4)})='),
    (re.compile(r'Funktionerna är \\\(([A-Za-z])\(([a-z])\)=(.*?)\\\) och \\\(([A-Za-z])\(([a-z])\)='),
     lambda m: f'Funktionerna \\({m.group(1)}\\) och \\({m.group(4)}\\) ges av \\({m.group(1)}({m.group(2)})={m.group(3)}\\) och \\({m.group(4)}({m.group(5)})='),
    (re.compile(r'Funktionerna är(\s*</p>\s*<p>\s*|\s*)\\\[([A-Za-z])\(([a-z])\)=(.*?),\s*\\qquad\s*([A-Za-z])\('),
     lambda m: f'Funktionerna \\({m.group(2)}\\) och \\({m.group(5)}\\) ges av{m.group(1)}\\[{m.group(2)}({m.group(3)})={m.group(4)},\\qquad {m.group(5)}('),
    (re.compile(r'På vilka punkter'), lambda m: 'I vilka punkter'),
    (re.compile(r'([Pp])arablen'), lambda m: m.group(1) + 'arabeln'),
    (re.compile(r'(?<=en )förenklad ([a-zåäö]+modell)'), lambda m: m.group(1)),
    (re.compile(r'mäts i timme\b'), lambda m: 'mäts i timmar'),
    (re.compile(r'(\^\{?\d+\}?|[a-z}])\+0(?=\\\))'), lambda m: m.group(1)),
]
R = {}
for u in Bank(BANK).arr:
    falt = [u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))]
    e = []
    for x in falt:
        x = re.sub(r'<svg[\s\S]*?</svg>', '', x)
        for rx, f in REGLER:
            for m in rx.finditer(x):
                par = (m.group(0), f(m))
                if par[0] != par[1] and par not in e:
                    e.append(par)
    if e:
        R[u['id']] = {'ers': e}
if __name__ == '__main__' or os.environ.get('VISA'):
    for k, v in R.items():
        for a, b in v['ers']:
            print(k, a[:70], '→', b[:80])
