"""Ta bort generiska mallfraser ur facit (språkgranskningen, steg ”mallfraser i facit”, 2026-11-20).

Äldre facit har genererade block som står ordagrant i många uppgifter, till exempel
”Tänk så här: Använd en potens- eller logaritmlag i taget och skriv mellanled.”,
”Kontroll och insikt: Sätt tillbaka varje lösning i ursprungsekvationen.” och
”Varför metoden fungerar: Deriveringsregeln väljs utifrån hur funktionen är uppbyggd.”, ofta följda av en
fortsättningsmening i nästa listpunkt. De säger inget om just den uppgiften (FACITMALL: inga allmänna mallfraser).

Urval (beslut per fras, inte per förekomst):
- En listpunkt <li> i ett facit som börjar med etiketten ”Tänk så här:”, ”Kontroll och insikt:” eller
  ”Varför metoden fungerar:” och står ordagrant i minst MIN uppgifter i banken.
- Allmänna råd med etiketten ”Nyckelidé:” eller ”Metod:” som står i ALLMANNA nedan. Övriga ”Nyckelidé”/”Metod”
  anger uppgiftens regel (”Tangens har grundperiod π”) och står kvar.
- Fortsättningsmeningar: en listpunkt som står direkt efter en borttagen etikettpunkt i minst 90 % av sina
  förekomster och själv står i minst MIN uppgifter.
Tomma <ol>-listor tas bort. Ett facit som skulle bli utan uträkning eller svar lämnas orört och rapporteras.

  python tools/sprak/mallfraser.py <bank> [--lista] [--skriv]
"""
import collections
import json
import os
import re
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
import bankobjekt as B  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
FILER = {'ai': 'uppgifterai.js', 'fy1': 'uppgifter.js', 'fy2': 'uppgifter2.js', 'ma1': 'uppgifterma1.js', 'ma2': 'uppgifterma2.js',
         'mato1': 'uppgiftermato1.js', 'mato2': 'uppgiftermato2.js', 'matf1': 'uppgiftermatf1.js'}
MIN = 4
ETIKETTER = ('Tänk så här:', 'Kontroll och insikt:', 'Varför metoden fungerar:')
ALLMANNA = {
    'Nyckelidé: Skriv upp den centrala formeln eller definitionen först och kontrollera därefter varje algebra- eller '
    'beräkningssteg.',
    'Nyckelidé: Bestäm vilken deriveringsregel som behövs innan du börjar förenkla.',
    'Nyckelidé: Identifiera först vad integranden och differentialen betyder i situationen.',
    'Använd lämplig regel från formelbladet.',
}
# Etikettfraser som anger uppgiftens sats eller formel och därför står kvar.
BEHALL = {
    'Tänk så här: Faktorsatsen säger att \\(P(a)=0\\) precis när \\(x-a\\) är en faktor.',
}
LI = re.compile(r'<li>(<p(?: class="[^"]*")?>.*?</p>)</li>')


def text(h):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', h)).strip()


def facitfalt(q):
    yield q, 's'
    for d in q.get('spelDelar') or []:
        yield d, 's'


def analysera(bank):
    """Räkna listpunkter (synlig text) per uppgift och vilken punkt som står före."""
    antal = collections.Counter()
    efter = collections.defaultdict(collections.Counter)   # punkt -> föregående punkt
    for q in bank:
        sett = set()
        for obj, k in facitfalt(q):
            items = [text(x) for x in LI.findall(obj.get(k) or '')]
            for i, it in enumerate(items):
                sett.add(it)
                efter[it][items[i - 1] if i else None] += 1
        antal.update(sett)
    etikett = {it for it, n in antal.items()
               if n >= MIN and (it.startswith(ETIKETTER) or it in ALLMANNA) and it not in BEHALL}
    fortsatt = set()
    for _ in range(3):   # kedjor: etikett, mening, mening
        for it, n in antal.items():
            if n < MIN or it in etikett or it in fortsatt:
                continue
            fore = efter[it]
            tot = sum(fore.values())
            bort = sum(c for p, c in fore.items() if p in etikett or p in fortsatt)
            leder_in = re.search(r'(är|ger|blir|:)$', it) or it.startswith(('Metod:', 'Formel från formelbladet', 'Formelbladet'))
            if tot and bort / tot >= 0.9 and not leder_in and len(it) > 25:
                fortsatt.add(it)
    return etikett, fortsatt, antal


def rensa(f, bort):
    def ersatt(m):
        inre = m.group(1)
        if re.search(r'\\\[|facit-matte|facit-rubrik', inre):
            return m.group(0)
        return '' if text(inre) in bort else m.group(0)
    ny = re.sub(r'<li>(<p(?: class="[^"]*")?>.*?</p>)</li>', ersatt, f)
    ny = re.sub(r'<ol class="facit-steglista" role="list"></ol>', '', ny)
    return ny


def har_innehall(f):
    t = text(f)
    return bool(re.search(r'\\\[|\\\(|Svar|=|\d', f)) and len(t) > 0


def main():
    bank_namn = sys.argv[1]
    fil = os.path.join(ROOT, FILER[bank_namn])
    src, bank = B.las(fil)
    etikett, fortsatt, antal = analysera(bank)
    bort = etikett | fortsatt
    if '--lista' in sys.argv:
        for it in sorted(bort, key=lambda x: -antal[x]):
            print(antal[it], 'E' if it in etikett else 'F', it[:200])
    byten, orort = {}, []   # id -> [(gammal facittext, ny facittext)]
    for q in bank:
        for obj, k in facitfalt(q):
            f = obj.get(k) or ''
            ny = rensa(f, bort)
            if ny == f:
                continue
            if not har_innehall(ny) or len(text(ny)) < 3:
                orort.append(q['id'])
                continue
            byten.setdefault(q['id'], [])
            if (f, ny) not in byten[q['id']]:
                byten[q['id']].append((f, ny))
    print(f'{bank_namn}: {len(bort)} fraser ({len(etikett)} etiketter, {len(fortsatt)} fortsättningar), '
          f'{len(byten)} uppgifter ändras, {len(orort)} facit lämnas orörda: {orort[:20]}')
    if '--skriv' in sys.argv and byten:
        # Byt bara strängliteralerna inom varje berört objekt, så att filens format i övrigt behålls.
        delar, pos = [], 0
        for start, slut, obj in B.spann(src):
            uid = str(obj.get('id'))
            if uid not in byten:
                continue
            bit = src[start:slut]
            for gammal, ny in byten[uid]:
                lit_g = json.dumps(gammal, ensure_ascii=False)
                lit_n = json.dumps(ny, ensure_ascii=False)
                assert lit_g in bit, (uid, 'literal saknas')
                bit = bit.replace(lit_g, lit_n)
            delar += [src[pos:start], bit]
            pos = slut
        delar.append(src[pos:])
        ny_src = ''.join(delar)
        ny_bank = json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
        assert [q['id'] for q in ny_bank] == [q['id'] for q in bank]
        for q, r in zip(ny_bank, bank):
            if q != r:
                assert q['id'] in byten, q['id']
                for obj_n, obj_g in [(q, r)] + list(zip(q.get('spelDelar') or [], r.get('spelDelar') or [])):
                    for k in set(obj_n) | set(obj_g):
                        if k not in ('s', 'spelDelar'):
                            assert obj_n.get(k) == obj_g.get(k), (q['id'], k)
        B.skriv(fil, ny_src)
    return byten


if __name__ == '__main__':
    main()
