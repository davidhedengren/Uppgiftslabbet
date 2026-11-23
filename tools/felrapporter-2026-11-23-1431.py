"""Felrapporter 2026-11-23 14:31 (AI-banken). Se agent/FELRAPPORTER_2026-11-23_1431.md.

AI 3.01 a  Läraren: alla uppgifter i området minimax ska vara fristående kort i Kunskapsgymmet, inte a) → b) → c)
           i samma kort. Alla uppgifter i området får kgFristaendeDelar: true. Kunskapsgymmet visar då varje delkort
           som ett eget kort (kedjaSyskon i index.html). Pappersversionen i Uppgiftslabbet behåller a), b), c).
AI 3.79 c  Läraren: ”del C var konstig. Ta bort den.” Del c tas bort i text, facit, delkort och svarsfält.
           Uppgiften blir E (2/0/0), träningsnivå 2.

  python tools/felrapporter-2026-11-23-1431.py [--skriv]
"""
import copy
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).parent))
import bankobjekt as B  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
FIL = ROOT / 'uppgifterai.js'
SKRIV = '--skriv' in sys.argv


def byt(text, gammal, ny):
    assert text.count(gammal) == 1, (gammal[:60], text.count(gammal))
    return text.replace(gammal, ny)


def utan_c_379(q):
    q = copy.deepcopy(q)
    assert [d['etikett'] for d in q['spelDelar']] == ['a', 'b', 'c']
    q['t'] = byt(q['t'], '<p>c) Datorn väljer ett drag som bara leder till oavgjort, värdet 0. '
                         'Varför försöker den inte vinna i stället?</p>', '')
    s = q['s']
    i = s.index('<div class="facit-del"><span class="facit-mark">c)</span>')
    assert s.endswith('</div></div></div></div>')
    q['s'] = s[:i] + '</div>'          # behåll den yttre facit-v2-diven
    q['spelDelar'] = q['spelDelar'][:2]
    for k in ('rättSvar', 'tolerans', 'svarFormat', 'svarEnhet', 'svarEtiketter'):
        assert len(q[k]) == 3, k
        q[k] = q[k][:2]
    q['niva'], q['poang'], q['traningsniva'], q['arbetsinsats'] = 'E', '2/0/0', 2, 1
    q['formaga'] = ['procedur']   # resonemanget hörde till del c
    return q


def main():
    src, bank = B.las(FIL)
    nya = {}
    for q in bank:
        if q.get('omr') != 'minimax':
            continue
        n = utan_c_379(q) if q['id'] == '3.79' else copy.deepcopy(q)
        if len(n.get('spelDelar') or []) >= 2:
            n['kgFristaendeDelar'] = True
        if n != q:
            nya[q['id']] = n
    assert B.kontrollera_rundresa(FIL, set(nya)) == [], 'rundresan ändrar formatet'
    ut = B.ersatt(src, nya)
    print(len(nya), 'uppgifter ändrade:', ' '.join(sorted(nya, key=lambda x: [int(p) for p in x.split('.')])))
    if SKRIV:
        B.skriv(FIL, ut)
        print('skrivet')
    else:
        print('torrkörning')


if __name__ == '__main__':
    main()
