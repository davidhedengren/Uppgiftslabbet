"""AI-banken, språksteg 1 (2026-11-23): samma två regler som redan gäller i de andra sju bankerna.

1. ”Välj ett alternativ.” tas bort ur `t`, `spelIntro` och delkortens `t`/`fraga` (stilguiden: Kunskapsgymmet visar
   knappar och papperet visar A–D). ”Välj alla som stämmer.” står kvar, eftersom den säger att flera svar är rätt.
2. Svarsinstruktioner inom parentes sist i ett delkorts fråga, t.ex. ”(Skriv rutorna i ordning, åtskilda med
   kommatecken.)” eller ”(Svara med nodens namn.)”, flyttas till delkortets `kgInstruktion` (användarbeslut
   2026-11-23: sådant behövs bara i Kunskapsgymmet). Kunskapsgymmet lägger `kgInstruktion` sist i texten, så
   eleven ser samma instruktion som förut.

Inga andra fält ändras. Därefter läses varje område för hand (se agent/SPRAKOMSKRIVNING_INSTRUKTION.md).

  python tools/sprak/ai_steg1.py [--skriv]
"""
import copy
import json
import os
import re
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
import bankobjekt as B  # noqa: E402

FIL = os.path.abspath(os.path.join(HERE, '..', '..', 'uppgifterai.js'))
VALJ = re.compile(r'\s*Välj ett alternativ\.')
PAREN = re.compile(r'\s*\(((?:Skriv|Svara|Ange)[^()]*)\)(?=\s*</p>)')


def utan_valj(s):
    if not s:
        return s
    ny = VALJ.sub('', s)
    return re.sub(r'<p>\s*</p>', '', ny)


def med_kg(d, text):
    """Lägg kgInstruktion direkt efter fraga (eller sist i befintlig instruktion)."""
    if d.get('kgInstruktion'):
        if text in d['kgInstruktion']:
            return d
        d['kgInstruktion'] = d['kgInstruktion'].rstrip() + ' ' + text
        return d
    ut = {}
    for k, v in d.items():
        ut[k] = v
        if k == 'fraga':
            ut['kgInstruktion'] = text
    if 'kgInstruktion' not in ut:
        ut['kgInstruktion'] = text
    return ut


def main():
    src, bank = B.las(FIL)
    assert not B.kontrollera_rundresa(FIL)
    nya, n_valj, n_paren = {}, 0, 0
    for u in bank:
        ny = copy.deepcopy(u)
        for k in ('t', 'spelIntro'):
            if ny.get(k):
                n_valj += len(VALJ.findall(ny[k]))
                ny[k] = utan_valj(ny[k])
        delar = []
        for d in ny.get('spelDelar') or []:
            for k in ('t', 'fraga'):
                if d.get(k):
                    n_valj += len(VALJ.findall(d[k]))
                    d[k] = utan_valj(d[k])
            m = PAREN.search(d.get('fraga') or '')
            if m:
                instr = m.group(1).strip()
                d['fraga'] = d['fraga'][:m.start()] + d['fraga'][m.end():]
                d = med_kg(d, instr)
                n_paren += 1
            delar.append(d)
        if delar:
            ny['spelDelar'] = delar
        if ny != u:
            assert set(ny) == set(u), u['id']
            for k in u:
                if k not in ('t', 'spelIntro', 'spelDelar'):
                    assert ny[k] == u[k], (u['id'], k)
            nya[u['id']] = ny
    ny_src = B.ersatt(src, nya)
    ny_bank = json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
    assert [q['id'] for q in ny_bank] == [q['id'] for q in bank]
    rest = [q['id'] for q in ny_bank if 'Välj ett alternativ' in json.dumps(q, ensure_ascii=False).split('"s":')[0]]
    print(f'{len(nya)} uppgifter, {n_valj} ”Välj ett alternativ.” bort, {n_paren} instruktioner till kgInstruktion')
    print('kvar i texterna:', rest[:10])
    if '--skriv' in sys.argv:
        B.skriv(FIL, ny_src)
        print('skrivet')


if __name__ == '__main__':
    main()
