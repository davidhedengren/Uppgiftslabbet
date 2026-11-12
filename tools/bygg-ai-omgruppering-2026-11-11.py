"""AI-banken 2026-11-11: ny indelning i oinformerad och informerad sökning.

Användarbeslut 2026-11-11:
- Kapitel 1 ”Oinformerad sökning”: köer och stackar samt BFS och DFS i labyrinter,
  träd och grafer. Kortet ”Kön under sökningen” (ko_sokning) upphör; dess uppgifter
  hör nu till BFS eller DFS beroende på algoritm.
- Kapitel 2 ”Informerad sökning”: prioritetsköer, heuristik och g, h, f, girig bäst
  först och A*, viktade vägar.
- Kapitel 3 (spelträd) behåller sina två kort men får två delmoment per kort.

Varje uppgift hade tidigare ett eget delmoment (`familj`). Enligt strukturregeln
(moment = kort, delmoment = 2–5 per kort) samlas de nu i 2 delmoment per kort.
Gamla värden sparas i `omrTidigare` och `familjTidigare`, så att Kunskapsgymmets
migreraFamiljer() flyttar elevernas resultat.

Strukturfilen strukturai.js skrivs här. Körs efter bygg-ai-mangdtraning-2026-11-12.py och
före nivåskriptet. Idempotent.
"""
import json

BANK = 'uppgifterai.js'
STRUKTUR = 'strukturai.js'

KAPITEL = {'1': 'Oinformerad sökning', '2': 'Informerad sökning', '3': 'Spelträd och beskärning'}
OMRADEN = {
    '1': {'ko_stack': 'Köer och stackar', 'bfs': 'Bredden först (BFS)', 'dfs': 'Djupet först (DFS)'},
    '2': {'prioritetsko': 'Prioritetsköer', 'astar_varden': 'Heuristik och f-värden',
          'astar_sokning': 'Girig bäst först och A*', 'viktade_vagar': 'Viktade vägar'},
    '3': {'minimax': 'Minimax', 'alfa_beta': 'Alfa–beta-beskärning'},
}

# delmoment: (område, uppgifter)
DELMOMENT = {
    'Kö och stack steg för steg': ('ko_stack', '1.77 1.78 1.79 1.80 1.81 1.82 1.03 1.10 1.11 1.12 1.21 1.28 1.32 1.33 1.34'),
    'Kö, stack och sökning i teorin': ('ko_stack', '1.97 1.98 1.20 1.44 1.45 1.55 1.56 1.58 1.59 1.60'),
    'BFS i labyrinter': ('bfs', '1.83 1.84 1.85 1.86 1.01 1.06 1.08 1.13 1.15 1.16 1.24 1.25 1.30 1.37 1.38 1.39 1.40 '
                                '1.48 1.49 1.50 1.51 1.57 1.61'),
    'BFS i träd och grafer': ('bfs', '1.91 1.92 1.93 1.04 1.09 1.14 1.22 1.23 1.35 1.46 1.64 1.65 1.66 1.67 1.68 1.69 1.70'),
    'DFS i labyrinter': ('dfs', '1.100 1.101 1.102 1.103 1.99 1.87 1.88 1.89 1.90 1.02 1.07 1.17 1.18 1.19 1.27 1.31 1.41 1.43 1.52 1.53 1.62 1.63'),
    'DFS i träd och grafer': ('dfs', '1.94 1.95 1.96 1.05 1.26 1.29 1.36 1.42 1.47 1.54 1.71 1.72 1.73 1.74 1.75 1.76'),
    'Uttag ur en prioritetskö': ('prioritetsko', '2.88 2.89 2.90 2.91 2.04 2.12 2.23 2.24 2.31 2.35 2.65 2.82 2.83 2.84'),
    'Prioritetskön i girig bäst först och A*': ('prioritetsko', '2.104 2.105 2.05 2.13 2.14 2.36 2.37 2.66 2.72 2.85 2.86 2.87'),
    'Heuristiken h': ('astar_varden', '2.106 2.15 2.16 2.49 2.60 2.68 2.71 2.78 2.79 2.80 2.81'),
    'g, h och f för en ruta': ('astar_varden', '2.92 2.93 2.94 2.95 2.01 2.06 2.07 2.08 2.25 2.26 2.32 2.38 2.39 2.40 '
                                               '2.50 2.51 2.59 2.61 2.67'),
    'A* steg för steg': ('astar_sokning', '2.109 2.110 2.111 2.112 2.96 2.97 2.98 2.99 2.02 2.17 2.18 2.28 2.33 2.41 2.43 2.47 2.54 2.55 2.57 '
                                          '2.58 2.74 2.76'),
    'Girig bäst först jämfört med A*': ('astar_sokning', '2.108 2.09 2.19 2.27 2.42 2.48 2.56 2.69 2.70 2.75'),
    'Vägkostnad i labyrinter': ('viktade_vagar', '2.113 2.114 2.115 2.116 2.100 2.101 2.102 2.103 2.03 2.10 2.11 2.22 2.29 2.34 2.44 2.53 2.63 2.64'),
    'Billigaste väg i grafer': ('viktade_vagar', '2.107 2.20 2.21 2.30 2.45 2.46 2.52 2.62 2.73 2.77'),
    # Kapitel 3 (fortsättning 2026-11-11): två delmoment per kort i stället för ett per uppgift.
    'Minimaxvärden och bästa drag': ('minimax', '3.62 3.63 3.64 3.65 3.01 3.02 3.06 3.08 3.27 3.28 3.29 3.30 3.31 3.32 3.33 3.37 '
                                                '3.38 3.39 3.47 3.48 3.49 3.51 3.53 3.55'),
    'Tolka och resonera om minimax': ('minimax', '3.07 3.11 3.12 3.43 3.44 3.45 3.46 3.50 3.52 3.54'),
    'Beskärningens idé': ('alfa_beta', '3.66 3.67 3.68 3.69 3.10 3.14 3.56 3.57 3.58 3.59 3.60 3.61'),
    'Rotvärde och beskurna löv': ('alfa_beta', '3.70 3.71 3.72 3.03 3.04 3.05 3.09 3.13 3.15 3.16 3.17 3.18 3.19 3.20 3.21 '
                                               '3.22 3.23 3.24 3.25 3.26 3.34 3.35 3.36 3.40 3.41 3.42'),
}


def struktur_js():
    def obj(d, ind):
        rader = [f'{" " * (ind + 2)}{json.dumps(k, ensure_ascii=False)}: {v}' for k, v in d.items()]
        return '{\n' + ',\n'.join(rader) + '\n' + ' ' * ind + '}'
    kap = obj({k: json.dumps(v, ensure_ascii=False) for k, v in KAPITEL.items()}, 0)
    omr = obj({k: obj({o: json.dumps(n, ensure_ascii=False) for o, n in v.items()}, 2)
               for k, v in OMRADEN.items()}, 0)
    return f'window.KAPNAMNAI = {kap};\nwindow.OMRAI = {omr};\n'


def main():
    with open(BANK, encoding='utf-8', newline='') as fh:
        src = fh.read()
    i, j = src.index('['), src.rindex(']')
    bank = json.loads(src[i:j + 1])
    plats = {}
    for fam, (omr, ids) in DELMOMENT.items():
        for id_ in ids.split():
            assert id_ not in plats, id_
            plats[id_] = (omr, fam)
    kap_for = {o: int(k) for k, v in OMRADEN.items() for o in v}
    flyttade, n = 0, 0
    for u in bank:
        assert u['id'] in plats, u['id'] + ' saknar plats'
        omr, fam = plats.pop(u['id'])
        assert kap_for[omr] == u['kap'], u['id']
        n += 1
        if u['omr'] != omr:
            u.setdefault('omrTidigare', u['omr'])
            u['omr'] = omr
            flyttade += 1
        if u['familj'] != fam:
            u.setdefault('familjTidigare', u['familj'])
            u['familj'] = fam
    assert not plats, sorted(plats)
    # Fast ordning efter kapitel och nummer. Flera äldre byggskript lägger sina uppgifter sist
    # vid omkörning, så utan sortering beror ordningen på vilken fil kedjan startar från.
    bank.sort(key=lambda u: (u['kap'], int(u['id'].split('.')[1])))
    with open(BANK, 'w', encoding='utf-8', newline='') as fh:
        fh.write(src[:i] + json.dumps(bank, ensure_ascii=False, indent=2) + src[j + 1:])
    with open(STRUKTUR, 'w', encoding='utf-8', newline='') as fh:
        fh.write(struktur_js())
    print(f'{n} uppgifter placerade, {flyttade} bytte område')


if __name__ == '__main__':
    main()
