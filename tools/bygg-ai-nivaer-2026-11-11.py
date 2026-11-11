"""Nivåindelning av AI-banken enligt agent/AI_NIVAINDELNING.md (användarbeslut 2026-11-11).

Sätter E/C/A (`niva`, `poang`) och `traningsniva` för varje delkort, och därefter
huvuduppgiftens värden (högsta nivå, summerade poäng, högsta träningsnivå).
Körs sist i kedjan av AI-byggskript. Idempotent.

Regler i korthet:
- E: känna igen och ta enstaka steg med given regel, korta körningar i små
  labyrinter och träd, h för en ruta, f när g följer en rak väg, kostnad för en
  given väg, minimaxvärden. Träningsnivå 1–2. Banken ska ha många E-uppgifter.
- C: hela körningar som kräver säkerhet (långa BFS/DFS-ordningar med backning,
  A*-spårning med lika-värde-regler), g runt väggar eller genom terräng,
  förklaringar av varför, girig bäst först jämfört med A*. Träningsnivå 3.
- A: allt som gäller alfa–beta-beskärning (användarbeslut), samt att värdera
  heuristiken och generalisera (t.ex. för vilka x roten byter drag).
  Träningsnivå 4; 5 för stora träd (minst 12 löv) eller när både α och β efterfrågas.
"""
import json
import re

BANK = 'uppgifterai.js'
POANG = {'E': '1/0/0', 'C': '0/1/0', 'A': '0/0/1'}
RANK = {'E': 0, 'C': 1, 'A': 2}

# Undantag från grundregeln, per delkort. Motivering i kommentaren.
OVERRIDE = {
    # BFS och DFS: långa ordningar, backning och värdering av sökningens beteende
    '1.01a': ('C', 3),  # hela BFS-ordningen, 13 uttag
    '1.07a': ('C', 3),  # hela DFS-ordningen i 5 × 6 med backning
    '1.08a': ('C', 3),  # påståenden om onåbart mål
    '1.30a': ('C', 3),  # hela BFS-ordningen, 14 uttag
    '1.31a': ('C', 3),  # hela DFS-ordningen med återvändsgränd
    '1.22a': ('C', 3),  # hitta felet i en kötabell
    '1.22c': ('E', 2),  # räkna uttag med rätt BFS
    '1.23c': ('C', 3),  # förklara varför en nod inte läggs in igen
    # g, h och f: C när g måste gå runt väggar eller genom terräng
    '2.01c': ('C', 3),  # D1: g = 5 men Manhattanavståndet från start är 3
    '2.08a': ('C', 3),  # g = 13 men Manhattanavståndet från start är 11
    '2.16b': ('C', 3),  # verklig väg runt väggen
    '2.16c': ('A', 4),  # värdera heuristiken (h underskattar)
    '2.25a': ('C', 3), '2.25b': ('C', 3),  # g och f genom lera
    '2.32a': ('C', 3),  # R nås bara via en omväg
    '2.39a': ('C', 3), '2.39c': ('C', 3),  # g och f genom lera
    # A*-sökning
    '2.02d': ('C', 3),  # antal uttag kräver hela A*-körningen
    '2.09a': ('E', 2),  # girig bäst först: välj lägst h ur tabellen
    '2.19c': ('C', 3),  # förklara varför A* tar ut färre rutor
    '2.33b': ('C', 3),  # kräver hela A*-körningen
    # viktade vägar
    '2.10b': ('E', 2),  # summera kostnaden för tre givna vägar
    '2.30c': ('C', 3),  # förklara skillnaden mellan girig bäst först och A*
    # minimax: allt är E utom resonemang och generalisering
    '3.12c': ('C', 3),  # förklara varför spelet inte når lövet
    '3.07c': ('A', 4),  # för vilka x får B större värde än A
    '3.45a': ('C', 3),  # vad rotvärdet garanterar om MIN gör misstag
    '3.46b': ('C', 3),  # förklara varför MAX inte väljer det högsta lövet
    # värdera heuristiken: när kan A* lita på h
    '2.71a': ('A', 4),  # h får aldrig överskatta
    '2.71b': ('A', 4),  # varför Manhattanavståndet inte överskattar
}

VALUE_Q = re.compile(r'Vilket värde får (roten|[A-Z])\?|Bestäm rotens minimaxvärde')


def leaves(u):
    n = len(re.findall(r'>L\d+<', u['spelIntro']))
    return n or {'3.03': 8}.get(u['id'], 0)


def klass(u, d):
    key = u['id'] + d['etikett']
    if key in OVERRIDE:
        return OVERRIDE[key]
    if u['omr'] == 'alfa_beta':
        n = leaves(u)
        assert n, u['id']
        if VALUE_Q.search(d['fraga']):  # rotvärde eller nodvärde: vanlig minimax
            return ('E', 1) if n <= 7 else ('E', 2) if n <= 9 else ('C', 3)
        both = 'α och β' in d['fraga']
        return ('A', 5) if n >= 12 or both else ('A', 4)
    if u['omr'] == 'minimax':
        return ('E', min(d['traningsniva'], 2))
    if d['niva'] == 'E':
        return ('E', min(d['traningsniva'], 2))
    return ('C', 3)


def main():
    with open(BANK, encoding='utf-8', newline='') as fh:
        src = fh.read()
    i, j = src.index('['), src.rindex(']')
    bank = json.loads(src[i:j + 1])
    used = set()
    for u in bank:
        for d in u['spelDelar']:
            niva, tn = klass(u, d)
            used.add(u['id'] + d['etikett'])
            d['niva'], d['traningsniva'], d['poang'] = niva, tn, POANG[niva]
        nivaer = [d['niva'] for d in u['spelDelar']]
        u['niva'] = max(nivaer, key=RANK.get)
        u['poang'] = '/'.join(str(sum(int(d['poang'].split('/')[k]) for d in u['spelDelar'])) for k in range(3))
        u['traningsniva'] = max(d['traningsniva'] for d in u['spelDelar'])
    assert set(OVERRIDE) <= used, set(OVERRIDE) - used
    with open(BANK, 'w', encoding='utf-8', newline='') as fh:
        fh.write(src[:i] + json.dumps(bank, ensure_ascii=False, indent=2) + src[j + 1:])
    parts = [d for u in bank for d in u['spelDelar']]
    cnt = {k: sum(d['niva'] == k for d in parts) for k in 'ECA'}
    print(f'{len(bank)} uppgifter, {len(parts)} delkort: ' + ', '.join(f'{k} {v}' for k, v in cnt.items()))


if __name__ == '__main__':
    main()
