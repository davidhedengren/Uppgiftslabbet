"""Lista kvarvarande förbjudna mönster (samma som sprak-2026-11-17.test.js) i ett kapitel eller område.
Användning: python tools/sprak/kvar.py fy1 3            (kapitel 3)
            python tools/sprak/kvar.py fy1 omr:konstacc  (ett område)"""
import sys, json, re, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sprakverktyg import Bank

F = [r'[Vv]älj ett alternativ', r'[Mm]arkera det korrekta', r'\(Svara ', r'[Ss]vara med (tre|två|en) (värdesiffr|decimal)',
     r'\b(?:[Ee]n|[Ee]tt|[Tt]vå|[Tt]re) (?:[a-zåäö]+ )?[a-zåäö]+ på [\d ,]+ ?(kg|g|ton)\b', r'\b[Vv]ågrät|\b[Ll]odrät',
     r'från vila', r'positiva? riktning', r'med tecken|[Aa]nge tecken', r'[Rr]äkna (bara )?på ', r'[Ss]ammanlagd',
     r'[Bb]ortse från andra krafters', r'[Ee]ndast .{0,40} verkar|[Bb]ara .{0,40} verkar', r'utan tecken|\bentydigt\b']


def synlig(h):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', re.sub(r'<svg.*?</svg>|<table.*?</table>', '', h or '', flags=re.S)))


kod, val = sys.argv[1], sys.argv[2]
b = Bank(kod)
n = 0
for u in b.arr:
    if val.startswith('omr:'):
        if u.get('omr') != val[4:]:
            continue
    elif str(u.get('kap')) != val:
        continue
    sett = set()
    for t in [u.get('t'), u.get('spelIntro')] + [x for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))]:
        v = synlig(t)
        for rx in F:
            for m in re.finditer(rx, v):
                s0 = v.rfind('.', 0, m.start()) + 1
                s1 = v.find('.', m.end())
                mening = v[s0:(s1 + 1 if s1 >= 0 else len(v))].strip()
                if mening not in sett:
                    sett.add(mening)
                    n += 1
                    print(u['id'], u.get('omr'), '|', mening[:220])
print('totalt', n)
