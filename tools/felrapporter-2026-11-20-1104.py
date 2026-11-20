"""Felrapport 2026-11-20 11:04, Ma3c 1.1103: ”snarare nivå 3. ändra detta i alla liknande när det är många termer i
parentesen osv”. Lärarens bedömning är E (2/0/0), så bara träningsnivån ändras från 2 till 3.

Regel: att sätta in ett uttryck (x+h, a+h, 2+h, 2−h, 2a) i en funktion med flera termer där kvadreringsregeln behövs
är träningsnivå 3. Linjära funktioner (1.1101, 1.1129, 1.1130) och en enda kvadratterm (1.1131 x², 1.1132 3x²)
står kvar, liksom numeriska differenskvoter (2.25, 2.1126, 2.1148).

  python tools/felrapporter-2026-11-20-1104.py [--skriv]
"""
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).parent))
import bankobjekt as B  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
IDS = ['1.235', '1.1102', '1.1103', '1.1117', '1.1133', '1.1134', '1.1135', '1.1136', '1.1137', '1.1141', '1.1142',
       '1.1144']


def main():
    src, bank = B.las(ROOT / 'uppgiftermato1.js')
    Q = {q['id']: q for q in bank}
    nya = {}
    for i in IDS:
        q = json.loads(json.dumps(Q[i]))
        assert q['niva'] == 'E' and q['traningsniva'] == 2 and not q.get('spelDelar'), i
        q['traningsniva'] = 3
        q['arbetsinsats'] = max(q.get('arbetsinsats', 2), 2)
        nya[i] = q
    assert not B.kontrollera_rundresa(ROOT / 'uppgiftermato1.js', set(nya))
    ny = B.ersatt(src, nya)
    nb = json.loads(ny[ny.index('['):ny.rindex(']') + 1])
    andr = [q['id'] for q, r in zip(nb, bank) if q != r]
    assert sorted(andr) == sorted(IDS), andr
    print(andr)
    if '--skriv' in sys.argv:
        B.skriv(ROOT / 'uppgiftermato1.js', ny)


if __name__ == '__main__':
    main()
