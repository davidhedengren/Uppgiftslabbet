"""Felrapport Ma2 2026-11-06 10:00 (4.2122, 4.2123, 4.2124, 4.2126).

Läraren: "Ta bort 'använd geogebra' och gör det i alla uppgifter här. de ska inse det själva."
I området normalfordelning_digitala_verktyg stryks uppmaningar om att använda GeoGebra ur frågetexterna:
t, spelIntro och delkortens t. Frågor där GeoGebra är själva ämnet behålls, till exempel "Vilka värden ska du
skriva in i GeoGebras sannolikhetskalkylator", "I GeoGebra har någon räknat ut" och "Beskriv också hur man kan
göra i GeoGebra". Facit och ledtrådar ändras inte (metoden får stå där), och inte heller geogebra-flaggan.
Logg: agent/FELRAPPORTER_2026-11-06_1000.md

  python tools/ma2-felrapporter-2026-11-06-1000.py [--skriv]
"""
import json
import re
import sys
from pathlib import Path

BANK = Path(__file__).resolve().parent.parent / 'uppgifterma2.js'
OMR = 'normalfordelning_digitala_verktyg'
REGLER = [
    (r' Använd GeoGebra\.', ''),
    (r'Använd GeoGebra och svara', 'Svara'),
    (r'Använd GeoGebra och bestäm', 'Bestäm'),
    (r'Använd GeoGebras [Ss]annolikhetskalkylator och bestäm', 'Bestäm'),
    (r'Använd GeoGebras [Ss]annolikhetskalkylator för att bestämma', 'Bestäm'),
    (r'Bestäm med GeoGebra ', 'Bestäm '),
    (r'(percentilen) med GeoGebra([.,])', r'\1\2'),
    (r'Uppskatta standardavvikelsen med hjälp av GeoGebra', 'Uppskatta standardavvikelsen'),
    # 4.27 b) och dess delkort
    (r'Kontrollera uppskattningen med GeoGebras Sannolikhetskalkylator\.',
     'Kontrollera uppskattningen genom att beräkna hur många procent av produkterna som väger mer än 90,0 g.'),
    (r'Kontrollera med GeoGebra: hur många procent ligger över 90 om μ=84 och σ=3\?',
     'Hur många procent av produkterna väger mer än 90,0 g om standardavvikelsen är 3,0 g?'),
    # 4.2127
    (r'\(\\sigma=1\\\) i GeoGebra\.', r'(\\sigma=1\\).'),
]
# GeoGebra som ämne i frågan: behålls
BEHALL = re.compile(r'Vilka värden ska du skriva in i GeoGebras|I GeoGebra har någon|hur man kan (?:göra|bestämma detta) i GeoGebra')


KVAR = []


def tvatta(text):
    for monster, ny in REGLER:
        text = re.sub(monster, ny, text)
    return text


def main():
    src = open(BANK, encoding='utf-8', newline='').read()
    data = json.loads(src[src.index('['):src.rindex(']') + 1])
    andrade = []
    for u in [x for x in data if x.get('omr') == OMR]:
        # delkort har antingen eget t eller en fråga som visas efter spelIntro
        falt = [('t', u)] + ([('spelIntro', u)] if u.get('spelIntro') else []) + [
            (k, d) for d in u.get('spelDelar') or [] for k in ('t', 'fraga') if d.get(k)]
        bytt = []
        for k, obj in falt:
            ny = tvatta(obj[k])
            if ny != obj[k]:
                bytt.append((obj[k], ny))
                obj[k] = ny
        rest = [re.sub('<[^>]+>', ' ', obj[k]) for k, obj in falt]
        kvar = [s for s in rest if re.search('geogebra', s, re.I) and not BEHALL.search(s)]
        for s in kvar:
            print('KVAR', u['id'], '|', s[:220])
        KVAR.extend(kvar)
        if bytt:
            andrade.append((u, bytt))
    nl = '\r\n' if '\r\n' in src else '\n'
    for u, bytt in andrade:
        m = re.search(r'\{\s*"id":\s*"' + re.escape(u['id']) + r'"', src)
        _, slut = json.JSONDecoder().raw_decode(src, m.start())
        gammal = src[m.start():slut]
        ny = gammal
        for fore, efter in bytt:
            f, e = json.dumps(fore, ensure_ascii=False)[1:-1], json.dumps(efter, ensure_ascii=False)[1:-1]
            assert f in ny, u['id']
            ny = ny.replace(f, e)
        src = src[:m.start()] + ny + src[slut:]
        for fore, efter in bytt:
            print(u['id'], '|', re.sub('<[^>]+>|<svg.*', ' ', efter)[:170])
    print(len(andrade), 'uppgifter ändrade')
    json.loads(src[src.index('['):src.rindex(']') + 1])
    assert not KVAR, f'{len(KVAR)} uppmaningar kvar'
    if '--skriv' in sys.argv:
        open(BANK, 'w', encoding='utf-8', newline='').write(src)
        print('skrivet')


if __name__ == '__main__':
    main()
