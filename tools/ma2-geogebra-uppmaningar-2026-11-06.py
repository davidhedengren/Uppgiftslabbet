"""Ma2: inga uppmaningar att använda GeoGebra i frågetexterna, i någon del av banken (2026-11-06).

Följer felrapporten 10:00 (tools/ma2-felrapporter-2026-11-06-1000.py, området normalfordelning_digitala_verktyg).
Läraren: "Ja, du kan ta bort uppmaningen där också. Om geogebra-taggen är på så får de själva förstå att de ska
använda geogebra."

Bara frågetexter ändras (t, spelIntro och delkortens t/fraga), och bara i uppgifter med geogebra: true.
Facit och ledtrådar får fortfarande visa GeoGebra-metoden. Följande behålls eftersom GeoGebra där är själva ämnet
eller situationen: "En elev ritar … i GeoGebra", "GeoGebra visar …", "Beskriv hur du i GeoGebra skulle …",
"hur bör GeoGebra användas …", "för in … i GeoGebra", "analyserar … i GeoGebra", "… ritas i GeoGebra",
"GeoGebra har anpassat …".
Logg: agent/FELRAPPORTER_2026-11-06_1000.md (avsnittet om resten av Ma2)

  python tools/ma2-geogebra-uppmaningar-2026-11-06.py [--skriv]
"""
import json
import re
import sys
from pathlib import Path

BANK = Path(__file__).resolve().parent.parent / 'uppgifterma2.js'
REGLER = [
    # särfall först
    (r'Använd GeoGebra för talen ', 'Talen är '),                        # 4.28
    (r'Använd GeoGebra för att uppskatta', 'Uppskatta'),                 # 4.44
    (r'Använd GeoGebra och ange', 'Ange'),                               # 4.05
    (r'Använd GeoGebra och jämför', 'Jämför'),                           # 4.458
    (r'Använd Sx i GeoGebra', 'Använd Sx'),                              # måttet Sx behövs, verktyget inte
    (r'<p>Använd GeoGebra\.</p>', ''),                                   # 5.127: eget stycke
    (r' Använd GeoGebra\.', ''),
    (r'Använd GeoGebra\. ', ''),                                         # i början av ett delkort
    (r' med hjälp av GeoGebra', ''),
    (r' med GeoGebra', ''),
]
BEHALL = re.compile(r'ritar [^.]* i GeoGebra|GeoGebra visar|I GeoGebra syns|ritas i GeoGebra|Beskriv hur du i GeoGebra|'
                    r'hur bör GeoGebra användas|för in [^.]* i GeoGebra|analyserar [^.]* i GeoGebra|GeoGebra har anpassat|'
                    r'GeoGebra anpassar|Vilka värden ska du skriva in i GeoGebras|I GeoGebra har någon|'
                    r'hur man kan (?:göra|bestämma detta) i GeoGebra')


def tvatta(text):
    for monster, ny in REGLER:
        text = re.sub(monster, ny, text)
    return text


def synlig(html):
    return re.sub('<[^>]+>', ' ', re.sub(r'<svg.*?</svg>', ' ', html or '', flags=re.S))


def main():
    src = open(BANK, encoding='utf-8', newline='').read()
    data = json.loads(src[src.index('['):src.rindex(']') + 1])
    andrade, kvar = [], []
    for u in data:
        falt = [('t', u)] + ([('spelIntro', u)] if u.get('spelIntro') else []) + [
            (k, d) for d in u.get('spelDelar') or [] for k in ('t', 'fraga') if d.get(k)]
        bytt = []
        if u.get('geogebra'):
            for k, obj in falt:
                ny = tvatta(obj[k])
                if ny != obj[k]:
                    bytt.append((obj[k], ny))
                    obj[k] = ny
        for k, obj in falt:
            for m in re.finditer(r'[^.?!]*GeoGebra[^.?!]*', synlig(obj[k])):
                if not BEHALL.search(m.group(0)):
                    kvar.append((u['id'], m.group(0).strip()))
        if bytt:
            andrade.append((u, bytt))
    # Objektens lägen i filen: läs arrayen objekt för objekt (id står inte alltid först i objektet).
    dec, spann, i = json.JSONDecoder(), {}, src.index('[') + 1
    while True:
        while src[i] in ' \t\r\n,':
            i += 1
        if src[i] == ']':
            break
        obj, slut = dec.raw_decode(src, i)
        spann[obj['id']] = (i, slut)
        i = slut
    for u, bytt in sorted(andrade, key=lambda x: -spann[x[0]['id']][0]):   # bakifrån, så att lägena gäller
        start, slut = spann[u['id']]
        ny = src[start:slut]
        for fore, efter in bytt:
            f, e = json.dumps(fore, ensure_ascii=False)[1:-1], json.dumps(efter, ensure_ascii=False)[1:-1]
            assert f in ny, u['id']
            ny = ny.replace(f, e)
        src = src[:start] + ny + src[slut:]
    for u, bytt in andrade:
        for fore, efter in bytt:
            print(u['id'], u['omr'], '|', re.sub(r'\s+', ' ', synlig(efter))[-200:])
    for i, s_ in kvar:
        print('KVAR', i, '|', s_[:200])
    print(len(andrade), 'uppgifter ändrade,', len(kvar), 'kvar att granska')
    json.loads(src[src.index('['):src.rindex(']') + 1])
    if '--skriv' in sys.argv:
        assert not kvar
        open(BANK, 'w', encoding='utf-8', newline='').write(src)
        print('skrivet')


if __name__ == '__main__':
    main()
