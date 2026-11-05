"""Ma2: regression och korrelation med GeoGebra-skärmbilder i facit (5 november 2026).

Bilderna tas med tools/geogebra-regression-bilder.js (Tvåvariabels regressionsanalys i GeoGebra Classic på
geogebra.org). Facit följer FACITMALL och samma stil som envariabelfacit: kalkylblad → skriv x i kolumn A och
y i kolumn B → Tvåvariabels regressionsanalys → välj modell, läs av ekvationen (och r med Σx) → uppgiftens
egna steg → svarsrad. Rubriker och texter är skrivna för hand per uppgift.

  python tools/ma2-geogebra-regression-2026-11-05.py [--skriv]
Logg: agent/MA2_REGRESSION_GEOGEBRA_BILDER_2026-11-05.md
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BANK = ROOT / 'uppgifterma2.js'


def li(rubrik, *delar):
    return f'<li><p class="facit-rubrik">{rubrik}</p>{"".join(delar)}</li>'


def p(x):
    return f'<p>{x}</p>'


def matte(x):
    return f'<div class="facit-matte">\\[{x}\\]</div>'


def img(fil, alt, maxw):
    return (f'<span class="fig"><img src="bilder/{fil}" alt="{alt}" loading="lazy" '
            f'style="width:100%;max-width:{maxw}px;height:auto"/></span>')


def lista(steg, svar):
    return (f'<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">{"".join(steg)}</ol>'
            f'<p class="facit-svar"><strong>Svar:</strong> {svar}</p></div>')


def tal(v):
    return '; '.join(('%g' % x).replace('.', ',') for x in v)


# slug -> (x, y, beskrivning i rubriker, vad x och y är)
DS = {
    '4-138': ([1, 2, 3, 4, 5], [7, 10, 12, 15, 17], 'tabellens x- och y-värden', 'x', 'y'),
    '4-139': ([1, 2, 3, 4, 5], [12, 15, 17, 21, 24], 'de fem mätpunkterna', 'x', 'y'),
    '4-141-a': ([1, 2, 3, 4, 5], [3, 5, 7, 9, 20], 'alla fem mätpunkterna', 'x', 'y'),
    '4-141-b': ([1, 2, 3, 4], [3, 5, 7, 9], 'de fyra första mätpunkterna', 'x', 'y'),
    '4-146': ([1, 2, 3, 4, 5], [48, 54, 61, 67, 70], 'träningstimmarna och resultaten', 'timmarna', 'resultaten'),
    '2-773': ([0, 1, 2, 3, 4, 5, 6], [52.1, 55.8, 60.2, 63.7, 68.1, 71.6, 76.0], 'valpens längder', 'veckorna', 'längderna'),
    '4-400': ([2, 3, 4, 5, 6, 7, 8], [14.2, 16.1, 18.5, 20.1, 22.4, 24.6, 26.3], 'tabellens sju mätpunkter', 'x', 'y'),
    '4-2098': ([0, 1, 2, 3, 4], [24.5, 26.0, 27.8, 29.1, 30.9], 'kaffepriserna', 'åren efter 2019', 'priserna'),
    '4-383': ([12.0, 14.5, 17.2, 19.8, 22.4, 25.1, 27.6, 30.3], [14.1, 16.4, 19.3, 21.7, 24.6, 27.0, 29.8, 32.0], 'termometrarnas värden',
              'termometer A', 'termometer B'),
    '4-2107': ([36, 37, 39, 40, 41, 43, 44, 45], [160, 171, 166, 178, 172, 185, 177, 188], 'skostorlekarna och längderna', 'skostorlekarna', 'längderna'),
    '4-2129': ([2, 4, 5, 7, 8, 10, 12], [11, 15, 13, 20, 17, 22, 25], 'pluggtimmarna och poängen', 'timmarna', 'poängen'),
    '2-372-p': ([1, 2, 3, 4, 5], [6.1, 9.9, 16.2, 25.8, 41.3], 'tabellens värden', 'x', 'y'),
    '2-372-e': ([1, 2, 3, 4, 5], [6.1, 9.9, 16.2, 25.8, 41.3], 'tabellens värden', 'x', 'y'),
}
# Ekvationen och r som GeoGebra visar (avlästa i skärmbilderna, kontrollerade mot AnpassaLinje och en egen beräkning).
EKV = {
    '4-138': 'y = 2.5x + 4.7', '4-139': 'y = 3x + 8.8', '4-141-a': 'y = 3.8x − 2.6', '4-141-b': 'y = 2x + 1', '4-146': 'y = 5.7x + 42.9',
    '2-773': 'y = 3.9714x + 52.0143', '4-400': 'y = 2.0429x + 10.1', '4-2098': 'y = 1.59x + 24.48',
}
R = {'4-383': '0.9996', '4-2107': '0.8602', '4-2129': '0.9471'}

PERSP_IMG = img('geogebra-kalkylblad-perspektiv.png', 'GeoGebra Classic med menyn öppen. Inringat: 1 menyknappen, 2 Perspektiv, 3 Kalkylblad.', 340)


def block(ds, rub_las, las_txt, modell='Linjär'):
    x, y, beskr, xn, yn = DS[ds]
    n = len(x)
    dec = ' Decimaltal kan skrivas med komma eller punkt; GeoGebra visar dem med punkt.' if any(v != int(v) for v in x + y) else ''
    return [
        li(f'Öppna ett kalkylblad i GeoGebra för {beskr}',
           p('Gå till geogebra.org/classic. Klicka på menyknappen ☰ uppe till höger, välj <strong>Perspektiv</strong> och sedan <strong>Kalkylblad</strong>.'),
           PERSP_IMG),
        li(f'Skriv {beskr} i kolumnerna A och B och markera dem',
           p(f'Skriv {xn} i kolumn A: {tal(x)}. Skriv {yn} i kolumn B på samma rader: {tal(y)}.{dec}'),
           p(f'Dra sedan med musen från A1 till B{n} så att båda kolumnerna blir blå. Kolumn A blir x och kolumn B blir y.'),
           img(f'geogebra-{ds}-data.png', f'Kalkylbladet med x-värdena {tal(x)} i kolumn A och y-värdena {tal(y)} i kolumn B. A1–B{n} är markerade och stapeldiagramknappen är inringad.', 380)),
        li(f'Analysera {beskr} med Tvåvariabels regressionsanalys',
           p('Klicka på stapeldiagramknappen, den andra knappen i verktygsraden (1), och välj <strong>Tvåvariabels regressionsanalys</strong> (2). '
             'Ett spridningsdiagram med punkterna öppnas.'),
           img('geogebra-tvavariabel-meny.png', 'Menyn under stapeldiagramknappen med Tvåvariabels regressionsanalys inringad.', 470)),
        li(rub_las, las_txt,
           img(f'geogebra-{ds}-regression.png', f'Analysfönstret för {beskr} med modellen {modell}. Regressionsmodellen, ekvationen, knappen Σx och raderna är inringade.', 690),
           # Förstorat utsnitt så att ekvationen (eller r) går att läsa på mobil.
           img(f'geogebra-{ds}-r.png', f'Statistikpanelen för {beskr} med raden r inringad.', 420) if ds in R else
           img(f'geogebra-{ds}-ekvation.png', f'Listan Regressionsmodell med {modell} och ekvationen för {beskr} inringade.', 640)),
    ]


def linjar_text(ds):
    return p(f'Välj <strong>Linjär</strong> i listan Regressionsmodell under diagrammet (1). Då ritas regressionslinjen bland punkterna, '
             f'och ekvationen visas bredvid listan (2): {EKV[ds]}.') + p('GeoGebra skriver decimaltal med punkt.' if '.' in EKV[ds] else '')


def r_text(ds):
    return (p('Välj <strong>Linjär</strong> i listan Regressionsmodell under diagrammet (1) och klicka på Σx uppe till höger (3). '
              f'Då visas statistik till vänster. På raden r (4) står {R[ds]}.')
            + p(f'GeoGebra skriver decimaltal med punkt: {R[ds]} betyder {R[ds].replace(".", ",")}.'))


U = {}   # id -> {None|etikett: html}  ('main' för huvudfacit med delar)


def bygg_innehall():
    U.clear()
    # 4.138
    las = lambda: block('4-138', 'Välj Linjär och läs av modellen för tabellens värden', linjar_text('4-138'))
    ins = li('Sätt in x = 6 i modellen y = 2,5x + 4,7', matte(r'y=2{,}5\cdot6+4{,}7=19{,}7'))
    U['4.138'] = {
        None: lista(las() + [ins], 'Modellen är \\(y\\approx2{,}5x+4{,}7\\). När \\(x=6\\) ger den \\(y\\approx19{,}7\\).'),
        'a': lista(las() + [li('Lutningen k är talet framför x', p('I y = 2.5x + 4.7 står 2.5 framför x.'))], '\\(k=2{,}5\\).'),
        'b': lista(las() + [li('Skärningen m är konstanttermen', p('I y = 2.5x + 4.7 är konstanttermen 4.7, alltså där linjen skär y-axeln.'))], '\\(m=4{,}7\\).'),
        'c': lista(las() + [ins], '\\(y\\approx19{,}7\\).'),
    }
    # 4.139
    las = lambda: block('4-139', 'Välj Linjär och läs av modellen för de fem mätpunkterna', linjar_text('4-139'))
    U['4.139'] = {
        None: lista(las(), '\\(y\\approx3{,}00x+8{,}80\\).'),
        'a': lista(las() + [li('Koefficienten a står framför x', p('Med två decimaler blir a = 3,00.'))], '\\(a\\approx3{,}00\\).'),
        'b': lista(las() + [li('Konstanten b är konstanttermen', p('Med två decimaler blir b = 8,80.'))], '\\(b\\approx8{,}80\\).'),
    }
    # 4.141 a och b (c står kvar)
    U['4.141'] = {
        'main:a': lista(block('4-141-a', 'Välj Linjär och läs av modellen för alla fem punkterna', linjar_text('4-141-a')),
                        '\\(y\\approx3{,}8x-2{,}6\\).'),
        'main:b': lista(block('4-141-b', 'Välj Linjär och läs av modellen utan punkten (5, 20)', linjar_text('4-141-b')
                              + p('De fyra punkterna ligger exakt på linjen.')), '\\(y=2x+1\\).'),
    }
    # 4.146 a
    U['4.146'] = {
        'main:a': lista(block('4-146', 'Välj Linjär och läs av modellen för träningsdatan', linjar_text('4-146')), '\\(y\\approx5{,}7x+42{,}9\\).'),
    }
    # 2.773
    U['2.773'] = {None: lista(block('2-773', 'Välj Linjär och läs av modellen för valpens längd', linjar_text('2-773'))
                              + [li('Avrunda k och m till en decimal', matte(r'k\approx3{,}97\approx4{,}0\qquad m\approx52{,}01\approx52{,}0'),
                                    p('Valpen växer med ungefär 4,0 cm per vecka enligt modellen.'))],
                              '\\(k\\approx4{,}0\\) och \\(m\\approx52{,}0\\).')}
    # 4.400
    U['4.400'] = {None: lista(block('4-400', 'Välj Linjär och läs av riktningskoefficienten för de sju punkterna', linjar_text('4-400'))
                              + [li('Riktningskoefficienten k står framför x', p('2.0429 avrundat till två decimaler är 2,04. y ökar med ungefär 2 när x ökar med 1.'))],
                              '\\(k\\approx2{,}04\\).')}
    # 4.2098
    U['4.2098'] = {None: lista(block('4-2098', 'Välj Linjär och läs av modellen för kaffepriserna', linjar_text('4-2098'))
                               + [li('Lutningen är prisökningen per år', p('Talet framför x anger hur många kronor priset ökar per år enligt modellen.'))],
                               '1,59 kr per år.')}
    # 4.383 a
    U['4.383'] = {'main:a': lista(block('4-383', 'Läs av korrelationskoefficienten r för termometrarna', r_text('4-383')),
                                  '\\(r\\approx1{,}00\\).')}
    U['4.383']['a'] = U['4.383']['main:a']
    # 4.2107 och 4.2129
    U['4.2107'] = {None: lista(block('4-2107', 'Läs av r för skostorlek och längd', r_text('4-2107'))
                               + [li('Tolka r för skostorlek och längd', p('r är positivt och nära 1: längre personer har oftast större skor, men sambandet är inte perfekt.'))],
                               '\\(r\\approx0{,}86\\).')}
    U['4.2129'] = {None: lista(block('4-2129', 'Läs av r för pluggtid och poäng', r_text('4-2129'))
                               + [li('Tolka r för pluggtid och poäng', p('Ett starkt positivt samband i den här gruppen: de som pluggade mer fick oftast fler poäng.'))],
                               '\\(r\\approx0{,}95\\).')}
    # 2.372: andragradsmodell och exponentialmodell jämförs i GeoGebra
    steg = [li('Växande ökningar räcker inte för att välja modell',
               p('Både en andragradsfunktion och en exponentialfunktion ger ökningar som växer. Kvoterna mellan efterföljande y-värden är '
                 'ungefär 1,62; 1,64; 1,59 och 1,60. De är jämnare än differenserna, och det talar för en exponentialmodell.'),
               matte(r'\frac{9{,}9}{6{,}1}\approx1{,}62\qquad\frac{16{,}2}{9{,}9}\approx1{,}64'),
               matte(r'\frac{25{,}8}{16{,}2}\approx1{,}59\qquad\frac{41{,}3}{25{,}8}\approx1{,}60'))]
    steg += block('2-372-p', 'Välj Polynom av grad 2 och läs av andragradsmodellen',
                  p('Välj <strong>Polynom</strong> i listan Regressionsmodell (1) och grad 2 i listan bredvid. '
                    'GeoGebra visar y = 1.9071x² − 2.8129x + 7.32 (2) och ritar kurvan bland punkterna.'), 'Polynom av grad 2')
    steg.append(li('Byt till Exponentiell C•a^x och läs av exponentialmodellen',
                   p('Välj <strong>Exponentiell C•a^x</strong> i samma lista. GeoGebra visar y = 3.8058 · 1.6133^x. '
                     'Förändringsfaktorn 1.6133 stämmer med kvoterna ovan.'),
                   img('geogebra-2-372-e-ekvation.png', 'Listan Regressionsmodell med Exponentiell C•a^x och ekvationen y = 3.8058 · 1.6133^x inringade.', 640)))
    steg.append(li('Jämför hur modellerna följer punkterna',
                   p('Titta på båda kurvorna tillsammans med punkterna och se om avvikelserna följer något mönster. Båda följer punkterna bra, '
                     'men bara exponentialmodellen förklarar att y ökar med nästan samma faktor i varje steg.')))
    U['2.372'] = {None: lista(steg, 'Exponentialmodellen har den starkare motiveringen.')}


def byt_del(s, mark, nytt):
    """Byter innehållet i delen mark) i ett huvudfacit. Slutet hittas genom att räkna div-nivåer,
    så att text efter delarna (äldre facit har en svarsrad sist) står kvar."""
    start = f'<div class="facit-del"><span class="facit-mark">{mark})</span><div class="facit-arbete">'
    assert s.count(start) == 1, mark
    i = s.index(start) + len(start)
    djup, k = 1, i
    while djup:
        o, c = s.find('<div', k), s.find('</div>', k)
        if o != -1 and o < c:
            djup, k = djup + 1, o + 4
        else:
            djup, k = djup - 1, c + 6
    slut = k - 6   # början av </div> som stänger facit-arbete
    return s[:i] + nytt + s[slut:]


def main():
    bygg_innehall()
    src = BANK.read_text(encoding='utf-8')
    data = json.loads(src[src.index('['):src.rindex(']') + 1])
    by = {u['id']: u for u in data}
    byten = []
    for uid, d in U.items():
        u = by[uid]
        if None in d:
            byten.append((u['s'], d[None]))
        hd = {k[5:]: v for k, v in d.items() if k and k.startswith('main:')}
        if hd:
            ny = u['s']
            for m, v in hd.items():
                ny = byt_del(ny, m, v)
            # 4.146: den allmänna GeoGebra-beskrivningen sist ersätts av stegen med bilder i a).
            ny = re.sub(r'<ol class="facit-steglista" role="list"><li><p><strong>GeoGebra:</strong>.*?</ol>(?=</div>$)', '', ny, flags=re.S)
            byten.append((u['s'], ny))
        for dd in u.get('spelDelar') or []:
            if dd['etikett'] in d:
                byten.append((dd['s'], d[dd['etikett']]))
    for g, n in byten:
        gj = json.dumps(g, ensure_ascii=False)
        assert src.count(gj) == 1, (src.count(gj), g[:80])
        src = src.replace(gj, json.dumps(n, ensure_ascii=False))
    print(len(U), 'uppgifter,', len(byten), 'facit')
    if '--skriv' in sys.argv:
        with open(BANK, 'w', encoding='utf-8', newline='') as f:
            f.write(src)
        print('skrivet')


if __name__ == '__main__':
    main()
