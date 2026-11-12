"""AI-banken 2026-11-12: efterbearbetning av alla uppgifter (användarbeslut 2026-11-12).

1. Delkortens facit listar kommentarerna till flervalsalternativen. Tidigare stod de med
   bokstav (”A: …, B: …”), men Kunskapsgymmet blandar alternativen, så bokstaven stämde ofta
   inte med knappen eleven ser. I delkortens facit (`spelDelar[].s`, visas bara i
   Kunskapsgymmet) står nu själva alternativet i stället för bokstaven. Huvudfacit `s`, som
   Uppgiftslabbet visar på papper, behåller bokstäverna; där stämmer de med A–D i `t`.
2. Alternativ som bara är ett namn (”B”) krockar på papper med bokstäverna A–D (”A. B”,
   ”B. G”). De skrivs som ”Noden B”, eller ”Rutan P” när uppgiften handlar om rutor, i
   alternativ, svar, uppgiftstext och facit (huvudfacit bara inom delens eget avsnitt).

Körs efter bygg-ai-omgruppering-2026-11-11.py och före bygg-ai-nivaer-2026-11-11.py. Idempotent.
"""
import json
import re

BANK = 'uppgifterai.js'
AVVIKELSER = []
# Delkort där alternativet inte är en nod eller ruta utan till exempel ett uttag.
ORD_UNDANTAG = {'1.22a': 'Efter uttaget av'}
LI = re.compile(r'<li><strong>([A-Z]):</strong> (.*?)</li>')


def utan_punkt(t):
    return t[:-1] if t.endswith('.') else t


def facit_med_text(d):
    """Byt ”A:” mot alternativets text i delkortets kommentarlista."""
    alts = d.get('alternativ') or []
    if not alts:
        return 0
    m = re.search(r'<ul>((?:<li>.*?</li>)+)</ul></div>$', d['s'])
    if not m:
        return 0
    rader = LI.findall(m.group(1))
    if not rader:
        return 0  # redan omskriven
    assert len(rader) == len(alts), d['fraga']
    ny = ''
    for (bokstav, komm), a in zip(rader, alts):
        assert ord(bokstav) - 65 == alts.index(a) and komm == a['kommentar'], (d['fraga'], bokstav)
        ny += f'<li><strong>{utan_punkt(a["txt"])}:</strong> {komm}</li>'
    d['s'] = d['s'][:m.start(1)] + ny + d['s'][m.end(1):]
    return 1


def ord_for(u):
    """”Rutan” när uppgiften handlar om rutor i en labyrint eller öppna listans rutor, annars ”Noden”."""
    return 'Rutan' if re.search(r'data-cell|\bruto?r?n?\b|rutor', u['spelIntro']) else 'Noden'


def del_avsnitt(s, et):
    """Start och slut för delens avsnitt i huvudfacit (facit-del med märket et))."""
    m = re.search(rf'<span class="facit-mark">{et}\)</span>', s)
    if not m:
        return None
    nxt = s.find('<div class="facit-del">', m.end())
    return m.start(), (nxt if nxt >= 0 else len(s))


def ensam_bokstav(u, d):
    """Alternativ som är ett ensamt namn får prefixet ”Noden” eller ”Rutan”. Returnerar antal ändrade."""
    alts = d.get('alternativ') or []
    if not alts or not any(re.fullmatch(r'[A-Z]', a['txt']) for a in alts):
        return 0
    ordet = ORD_UNDANTAG.get(u['id'] + d['etikett'], ord_for(u))
    gammalt = d['rättSvar']
    n = 0
    for a in alts:
        if re.fullmatch(r'[A-Z]', a['txt']):
            gammal, ny = a['txt'], f'{ordet} {a["txt"]}'
            # Alternativlistan i uppgiftstexten (papper), bara i delens egen lista
            u['t'] = re.sub(rf'(<p class="ul-alt"><strong>[A-Z]\.</strong> ){gammal}(</p>)', rf'\g<1>{ny}\g<2>', u['t'])
            a['txt'] = ny
            n += 1
    ratt = [a['txt'] for a in alts if a['ratt']]
    d['rättSvar'] = ratt[0] if len(ratt) == 1 else ratt
    if isinstance(gammalt, str) and re.fullmatch(r'[A-Z]', gammalt):
        gam, nyr = f'<strong>Svar:</strong> {gammalt}.</p>', f'<strong>Svar:</strong> {ordet} {gammalt}.</p>'
        if d['s'].count(gam) != 1:
            AVVIKELSER.append(u['id'] + d['etikett'])  # svarsraden är skriven i ord
        else:
            d['s'] = d['s'].replace(gam, nyr)
            av = del_avsnitt(u['s'], d['etikett'])
            if av:
                a0, a1 = av
                seg = u['s'][a0:a1]
                assert seg.count(gam) == 1, (u['id'], d['etikett'], 'huvudfacit')
                u['s'] = u['s'][:a0] + seg.replace(gam, nyr) + u['s'][a1:]
    return n


def main():
    with open(BANK, encoding='utf-8', newline='') as fh:
        src = fh.read()
    i, j = src.index('['), src.rindex(']')
    bank = json.loads(src[i:j + 1])
    nf = nb = 0
    for u in bank:
        for k, d in enumerate(u['spelDelar']):
            nb += ensam_bokstav(u, d)
            nf += facit_med_text(d)
            if isinstance(u.get('rättSvar'), list) and len(u['rättSvar']) == len(u['spelDelar']):
                u['rättSvar'][k] = d['rättSvar']
    with open(BANK, 'w', encoding='utf-8', newline='') as fh:
        fh.write(src[:i] + json.dumps(bank, ensure_ascii=False, indent=2) + src[j + 1:])
    print('svarsrad i ord:', AVVIKELSER)
    print(f'{nf} delfacit fick alternativens text i stället för bokstav, {nb} alternativ fick prefixet ”Noden”')


if __name__ == '__main__':
    main()
