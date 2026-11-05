"""Ma2: felrapporter 2026-11-05 21:56 och liknande uppgifter.

Läraren rapporterade att svar med flera lösningar rättades olika beroende på skrivsätt
(mängdklamrar, kommatecken, "och"). Uppgifterna hade svarstyp "uttryck" med en fritextsträng som
facit ("{-3,0,3}", "x=-2,0,2", "a=2 och b=3"). De får nu ett svarsfält per lösning: en mängd i valfri
ordning (x, x, x) eller ordnade fält med namn (a, b). Kunskapsgymmet godtar då också hela svaret
samlat i ett fält ("x=-3,0,3", "{-3,0,3}", "a=2, b=3", "(4, 7)").
Facit för de omgjorda uppgifterna är omskrivna för hand enligt FACITMALL.
Logg: agent/FELRAPPORTER_2026-11-05_2156.md

  python tools/ma2-felrapporter-2026-11-05-2156.py [--skriv]
"""
import json
import math
import re
import sys
from pathlib import Path

BANK = Path(__file__).resolve().parent.parent / 'uppgifterma2.js'


def li(rub, *h):
    return f'<li><p class="facit-rubrik">{rub}</p>{"".join(h)}</li>'


def p(x):
    return f'<p>{x}</p>'


def m(x):
    return f'<div class="facit-matte">\\[{x}\\]</div>'


def facit(steg, svar):
    return (f'<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">{"".join(steg)}</ol>'
            f'<p class="facit-svar"><strong>Svar:</strong> {svar}</p></div>')


def mangd(varden, etikett):
    n = len(varden)
    return dict(svarstyp='flera_delar', svarsstruktur='mängd', rättSvar=varden, tolerans=[0] * n,
                svarFormat=['numeriskt'] * n, svarEtiketter=[etikett] * n)


def ordnad(varden, etiketter):
    n = len(varden)
    return dict(svarstyp='flera_delar', svarsstruktur='ordnad', rättSvar=varden, tolerans=[0] * n,
                svarFormat=['numeriskt'] * n, svarEtiketter=etiketter)


NOLLPRODUKT = li('Nollproduktmetoden: en produkt är noll när minst en faktor är noll',
                 p('Sätt varje faktor lika med noll.'))

ANDRA = {}
# --- Lösningsmängder i x ---
ANDRA['1.143'] = dict(**mangd([-2, 0, 2], 'x'), s=facit([
    li('Bryt ut den gemensamma faktorn \\(3x\\)', m(r'3x^3-12x=3x(x^2-4)')),
    li('Konjugatregeln: \\(a^2-b^2=(a-b)(a+b)\\)', m(r'x^2-4=(x-2)(x+2)'), m(r'3x(x-2)(x+2)=0')),
    li('Nollproduktmetoden: varje faktor kan vara noll', m(r'3x=0\ \Rightarrow\ x=0'), m(r'x-2=0\ \Rightarrow\ x=2'), m(r'x+2=0\ \Rightarrow\ x=-2'))],
    '\\(x=-2\\), \\(x=0\\) eller \\(x=2\\).'))
for uid, k in [('1.51', 2), ('1.311', 2)]:
    ANDRA[uid] = dict(**mangd([-3, 0, 3], 'x'), s=facit([
        li(f'Bryt ut den gemensamma faktorn \\({k}x\\)', m(rf'{k}x^3-18x={k}x(x^2-9)')),
        li('Konjugatregeln: \\(a^2-b^2=(a-b)(a+b)\\)', m(r'x^2-9=(x-3)(x+3)'), m(rf'{k}x(x-3)(x+3)=0')),
        li('Nollproduktmetoden: varje faktor kan vara noll', m(rf'{k}x=0\ \Rightarrow\ x=0'), m(r'x-3=0\ \Rightarrow\ x=3'), m(r'x+3=0\ \Rightarrow\ x=-3'))],
        '\\(x=-3\\), \\(x=0\\) eller \\(x=3\\).'))
ANDRA['1.311']['ledtrad'] = '<p>Bryt först ut \\(2x\\). Det som blir kvar är en differens av två kvadrater.</p>'
ANDRA['2.160'] = dict(**mangd([-3, 0, 3], 'x'), s=facit([
    li('Bryt ut den gemensamma faktorn \\(x\\)', m(r'x^3-9x=x(x^2-9)')),
    li('Konjugatregeln: \\(a^2-b^2=(a-b)(a+b)\\)', m(r'x(x-3)(x+3)=0')),
    li('Nollproduktmetoden: varje faktor kan vara noll', m(r'x=0'), m(r'x-3=0\ \Rightarrow\ x=3'), m(r'x+3=0\ \Rightarrow\ x=-3'))],
    '\\(x=-3\\), \\(x=0\\) eller \\(x=3\\).'))
# --- Lösningsmängder i k ---
ANDRA['2.62'] = dict(**mangd([-13, -8, -7], 'k'), s=facit([
    li('Rötterna \\(r\\) och \\(s\\): produkten är 12 och summan är \\(-k\\)', m(r'x^2+kx+12=(x-r)(x-s)'), m(r'rs=12\qquad r+s=-k')),
    li('Positiva heltalspar med produkten 12', m(r'(1,12)\quad(2,6)\quad(3,4)')),
    li('Varje par ger ett värde på \\(k=-(r+s)\\)', m(r'k=-13\qquad k=-8\qquad k=-7'))],
    '\\(k=-13\\), \\(k=-8\\) eller \\(k=-7\\).'))
ANDRA['2.451'] = dict(**mangd([7, 8, 13], 'k'), s=facit([
    li('Rötterna \\(r_1\\) och \\(r_2\\): produkten är 12 och summan är \\(k\\)', m(r'x^2-kx+12=(x-r_1)(x-r_2)'), m(r'r_1r_2=12\qquad r_1+r_2=k')),
    li('Positiva heltalspar med produkten 12', m(r'(1,12)\quad(2,6)\quad(3,4)')),
    li('Varje par ger ett värde på \\(k=r_1+r_2\\)', m(r'k=13\qquad k=8\qquad k=7'))],
    '\\(k=7\\), \\(k=8\\) eller \\(k=13\\).'))
# --- Ordnade svar med namn ---
ANDRA['1.116'] = dict(**ordnad([9, -6], ['a', 'b']), s=facit([
    li('Oändligt många lösningar: ekvationerna beskriver samma linje',
       p('Den andra ekvationen måste vara den första multiplicerad med ett tal. Högerledet 21 är 3 gånger 7.')),
    li('Multiplicera den första ekvationen med 3', m(r'3(3x-2y)=3\cdot7\ \Rightarrow\ 9x-6y=21')),
    li('Jämför med \\(ax+by=21\\)', m(r'a=9\qquad b=-6'))],
    '\\(a=9\\) och \\(b=-6\\).'))
ANDRA['1.218'] = dict(**ordnad([2, 3], ['a', 'b']), s=facit([
    li('Oändligt många lösningar: ekvationerna beskriver samma linje',
       p('Den andra ekvationen måste vara den första multiplicerad med ett tal. Högerledet 9 är \\(\\tfrac32\\) gånger 6.')),
    li('Multiplicera den första ekvationen med \\(\\tfrac32\\)', m(r'\tfrac32(ax+2y)=\tfrac32\cdot6'), m(r'\tfrac32ax+3y=9')),
    li('Jämför med \\(3x+by=9\\)', m(r'\tfrac32a=3\ \Rightarrow\ a=2\qquad b=3'))],
    '\\(a=2\\) och \\(b=3\\).'))
ANDRA['2.316'] = dict(**ordnad([1, -6], ['a', 'b']), s=facit([
    li('Toppform med minimipunkten \\((3,1)\\): \\(f(x)=a(x-3)^2+1\\)', m(r'f(x)=a(x^2-6x+9)+1'), m(r'f(x)=ax^2-6ax+9a+1')),
    li('Konstanttermen ska vara 10', m(r'9a+1=10\ \Rightarrow\ a=1')),
    li('Koefficienten för \\(x\\) är \\(b=-6a\\)', m(r'b=-6\cdot1=-6'))],
    '\\(a=1\\) och \\(b=-6\\).'))
ANDRA['1.172'] = dict(**ordnad([3, 0.5], ['x', 'y']), s=facit([
    li('Additionsmetoden: addera ekvationerna så att \\(y\\) försvinner', m(r'(5x+2y)+(3x-2y)=16+8'), m(r'8x=24\ \Rightarrow\ x=3')),
    li('Sätt in \\(x=3\\) i den första ekvationen', m(r'5\cdot3+2y=16\ \Rightarrow\ 2y=1\ \Rightarrow\ y=0{,}5'))],
    '\\(x=3\\) och \\(y=0{,}5\\).'))
ANDRA['1.172']['ledtrad'] = '<p>Addera ekvationerna så att \\(y\\) försvinner.</p>'
ANDRA['2.678'] = dict(**ordnad([5, 4], ['a', 'b']), s=facit([
    li('Potenslagen \\(\\dfrac{x^m}{x^n}=x^{m-n}\\) för varje bas', m(r'\frac{x^{2a}}{x^{a-2}}=x^{2a-(a-2)}=x^{a+2}'), m(r'\frac{y^{b+3}}{y^2}=y^{b+1}')),
    li('Exponenterna ska vara 7 och 5', m(r'a+2=7\ \Rightarrow\ a=5'), m(r'b+1=5\ \Rightarrow\ b=4'))],
    '\\(a=5\\) och \\(b=4\\).'))
# --- 1.115: a) två värden som ska undantas, b) och c) ett värde var ---
ANDRA['1.115'] = dict(
    svarstyp='flera_delar', svarsstruktur='ordnad', rättSvar=[[0, -5], -5, 0], tolerans=[[0, 0], 0, 0],
    svarFormat=[['numeriskt', 'numeriskt'], 'numeriskt', 'numeriskt'],
    svarEtiketter=[['a) a ≠', 'a) a ≠'], 'b) a =', 'c) a ='],
    ledtrad='<p>Systemet har exakt en lösning så länge linjerna har olika lutning. Undersök när koefficienterna för \\(x\\) och \\(y\\) '
            'i de två ekvationerna är proportionella, och pröva sedan de värdena på \\(a\\) ett i taget.</p>',
    t='<p>För vilka värden på \\(a\\) har systemet \\(\\begin{cases}(a+2)x+3y=6\\\\2x+(a+3)y=6\\end{cases}\\)</p>'
      '<p>a) exakt en lösning? Systemet har exakt en lösning för alla \\(a\\) utom två värden. Ange de två värdena.</p>'
      '<p>b) ingen lösning?</p><p>c) oändligt många lösningar?</p>',
    s=facit([
        li('Exakt en lösning så länge linjerna har olika lutning',
           p('Linjerna är parallella eller sammanfaller när koefficienterna för \\(x\\) och \\(y\\) är proportionella:'),
           m(r'\frac{a+2}{2}=\frac{3}{a+3}\ \Rightarrow\ (a+2)(a+3)=6')),
        li('Lös andragradsekvationen', m(r'a^2+5a+6=6\ \Rightarrow\ a(a+5)=0'), m(r'a=0\ \text{eller}\ a=-5'),
           p('a) Exakt en lösning för alla \\(a\\) utom \\(a=0\\) och \\(a=-5\\).')),
        li('Undersök \\(a=-5\\): parallella olika linjer', m(r'-3x+3y=6\iff y=x+2'), m(r'2x-2y=6\iff y=x-3'),
           p('b) Olika linjer med samma lutning skär aldrig varandra: ingen lösning.')),
        li('Undersök \\(a=0\\): samma linje', m(r'2x+3y=6\qquad 2x+3y=6'),
           p('c) Ekvationerna är identiska: oändligt många lösningar.'))],
        'a) alla \\(a\\) utom \\(a=0\\) och \\(a=-5\\), b) \\(a=-5\\), c) \\(a=0\\).'))

# --- Övriga rapporter ---
# 3.282: skriv ut vad V–V betyder
ANDRA['3.282'] = dict(alternativ=[
    {"txt": "Vinkel–vinkel (V–V): två par lika stora vinklar", "ratt": True, "kommentar": "Två par lika stora vinklar räcker för att trianglarna ska vara likformiga."},
    {"txt": "Pythagoras sats", "ratt": False, "kommentar": "Pythagoras sats gäller sidorna i en rätvinklig triangel, inte likformighet."},
    {"txt": "Yttervinkelsatsen", "ratt": False, "kommentar": "Yttervinkelsatsen ger en vinkel i en triangel, men visar inte att två trianglar är likformiga."},
    {"txt": "Mittpunktsformeln", "ratt": False, "kommentar": "Mittpunktsformeln ger mittpunkten på en sträcka i ett koordinatsystem."}],
    s=facit([li('Likformighetsfallet vinkel–vinkel (V–V)',
                p('Två trianglar är likformiga om två vinklar i den ena är lika stora som två vinklar i den andra. Den tredje vinkeln blir då också lika, eftersom vinkelsumman är 180°.'),
                p('Här har trianglarna vinklarna 42°, 63° och 75° båda två.'))],
             'Vinkel–vinkel (V–V).'))
# 4.2127: förklara att andelen gäller för alla normalfördelningar
ANDRA['4.2127'] = dict(t='<p>I ett normalfördelat material har värdena medelvärdet \\(\\mu\\) och standardavvikelsen \\(\\sigma\\). '
                         'Hur stor andel av värdena ligger mer än 1,5 standardavvikelser från medelvärdet, alltså under '
                         '\\(\\mu-1{,}5\\sigma\\) eller över \\(\\mu+1{,}5\\sigma\\)?</p>'
                         '<p>Andelen är densamma för alla normalfördelningar, så du kan räkna med \\(\\mu=0\\) och \\(\\sigma=1\\) i GeoGebra. '
                         '(Svara i procent med en decimal.)</p>')
# 3.2101: skivan hålls parallellt med dörren
ANDRA['3.2101'] = dict(t=None)   # fylls nedan från bankens text
# 3.2140: förtydliga mittpunkterna
ANDRA['3.2140'] = dict(t=None, ledtrad='<p>Randen går mellan sidornas mittpunkter. Hur långa är sidorna i den lilla triangeln vid spetsen jämfört med hela vimpeln?</p>')
# 4.13 b: räkna utan att pröva sig fram
ANDRA['4.13'] = dict()

# ---------------------------------------------------------------- SVG-hjälp
def bage_lucka(svg, grader=6):
    """Bisektrismarkering: två bågar som möts vid bisektrisen får en lucka där, så att de syns som två lika vinklar."""
    arcs = list(re.finditer(r'<path d="M ([\d.]+) ([\d.]+) A ([\d.]+) \3 0 0 0 ([\d.]+) ([\d.]+)"([^>]*)/>', svg))
    byt = {}
    for a1, a2 in zip(arcs, arcs[1:]):
        if a1.group(3) != a2.group(3) or (a1.group(4), a1.group(5)) != (a2.group(1), a2.group(2)):
            continue
        r = float(a1.group(3))
        P1 = (float(a1.group(1)), float(a1.group(2))); P2 = (float(a1.group(4)), float(a1.group(5))); P3 = (float(a2.group(4)), float(a2.group(5)))

        def centrum(A, B):  # centrum för bågen A→B, sweep 0, liten båge
            mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
            dx, dy = B[0] - A[0], B[1] - A[1]; d = math.hypot(dx, dy); h = math.sqrt(max(0, r * r - d * d / 4))
            c1 = (mx - dy / d * h, my + dx / d * h); c2 = (mx + dy / d * h, my - dx / d * h)
            # sweep-flag 0: moturs i skärmens koordinater; välj centrum där korsprodukten stämmer
            for C in (c1, c2):
                cr = (A[0] - C[0]) * (B[1] - C[1]) - (A[1] - C[1]) * (B[0] - C[0])
                if cr < 0:
                    return C
            return c1
        C = centrum(P1, P2)
        vink = lambda P: math.atan2(P[1] - C[1], P[0] - C[0])
        rot = lambda t: (round(C[0] + r * math.cos(t), 1), round(C[1] + r * math.sin(t), 1))
        t1, t2, t3 = vink(P1), vink(P2), vink(P3)
        g = math.radians(grader)
        s12 = 1 if ((t1 - t2 + math.pi) % (2 * math.pi) - math.pi) > 0 else -1
        s32 = 1 if ((t3 - t2 + math.pi) % (2 * math.pi) - math.pi) > 0 else -1
        Q1, Q3 = rot(t2 + s12 * g), rot(t2 + s32 * g)
        byt[a1.group(0)] = f'<path d="M {a1.group(1)} {a1.group(2)} A {a1.group(3)} {a1.group(3)} 0 0 0 {Q1[0]} {Q1[1]}"{a1.group(6)}/>'
        byt[a2.group(0)] = f'<path d="M {Q3[0]} {Q3[1]} A {a2.group(3)} {a2.group(3)} 0 0 0 {a2.group(4)} {a2.group(5)}"{a2.group(6)}/>'
    for a, b in byt.items():
        svg = svg.replace(a, b)
    return svg, len(byt) // 2


def main():
    src = BANK.read_text(encoding='utf-8')
    data = json.loads(src[src.index('['):src.rindex(']') + 1])
    by = {u['id']: u for u in data}
    # 3.2101 och 3.2140: textändringar utifrån befintlig text
    t = by['3.2101']['t']
    gam = 'Ett tunt, 2,3 m långt skivmaterial ska bäras in stående i dörrens plan, alltså snett över öppningen. Går det?'
    assert gam in t, '3.2101'
    ANDRA['3.2101']['t'] = t.replace(gam, 'Ett tunt, 2,3 m långt skivmaterial ska föras rakt igenom öppningen och hela tiden hållas '
                                          'parallellt med dörren, snett från ett hörn till det motsatta. Skivan får alltså inte lutas '
                                          'bakåt genom dörren. Går det?')
    ANDRA['3.2101']['s'] = by['3.2101']['s'].replace('Skivan är för lång för att bäras in stående i dörrens plan.',
                                                       'Skivan är för lång för att föras igenom parallellt med dörren. (Lutar man den bakåt genom dörren går den in, men det tillåter inte uppgiften.)')
    t = by['3.2140']['t']
    gam = 'En rand sys parallellt med basen mellan mittpunkterna på vimpelns två andra sidor.'
    assert gam in t, '3.2140'
    t = t.replace(gam, 'En rand sys parallellt med basen, mellan mittpunkterna på vimpelns två långsidor.')
    # figur: markera mittpunkterna (punkt och lika långa halvor) och märk randen
    t = t.replace('<line x1="145.3" y1="130.0" x2="254.7" y2="130.0" stroke="#2f6fca" stroke-width="3"/>',
                  '<line x1="145.3" y1="130.0" x2="254.7" y2="130.0" stroke="#2f6fca" stroke-width="3"/>'
                  '<g stroke="#172b3a" stroke-width="2"><line x1="166.2" y1="85.4" x2="178.2" y2="93.4"/><line x1="111.6" y1="167.4" x2="123.6" y2="175.4"/>'
                  '<line x1="221.8" y1="93.4" x2="233.8" y2="85.4"/><line x1="276.4" y1="175.4" x2="288.4" y2="167.4"/>'
                  '<line x1="225.2" y1="96.7" x2="237.2" y2="88.7"/><line x1="279.8" y1="178.7" x2="291.8" y2="170.7"/></g>'
                  '<circle cx="145.3" cy="130.0" r="4" fill="#2f6fca"/><circle cx="254.7" cy="130.0" r="4" fill="#2f6fca"/>'
                  '<text x="200.0" y="122.0" font-family="Arial,sans-serif" font-size="13" text-anchor="middle" fill="#2f6fca" stroke="#fff" stroke-width="4" stroke-linejoin="round" paint-order="stroke">rand</text>')
    t = t.replace('aria-label="En triangulär vimpel med kortsidan 36 cm. En rand parallell med kortsidan går mitt emellan spetsen och kortsidan."',
                  'aria-label="En triangulär vimpel med basen 36 cm. Randen går mellan långsidornas mittpunkter; streck visar att båda halvorna av varje långsida är lika långa."')
    assert 'rand</text>' in t
    ANDRA['3.2140']['t'] = t
    # 3.520 och 3.523: lucka i bisektrismarkeringen; 3.523 får beteckningen AC
    for uid in ['3.520', '3.523']:
        nt, n = bage_lucka(by[uid]['t'])
        assert n == 2, (uid, n)
        if uid == '3.523':
            nt = nt.replace('<text x="190.3" y="121.7" font-size="16" fill="#101318" text-anchor="middle" font-family="Arial, sans-serif">2·AC</text>',
                            '<text x="190.3" y="121.7" font-size="16" fill="#101318" text-anchor="middle" font-family="Arial, sans-serif">AB = 2·AC</text>'
                            '<text x="383.0" y="140.0" font-size="16" fill="#101318" text-anchor="start" font-family="Arial, sans-serif">AC</text>')
            assert 'AB = 2·AC' in nt
        ANDRA[uid] = dict(t=nt)
    # 4.13 b: ett steg som räknar ut standardavvikelsen direkt, utan att pröva
    d = next(x for x in by['4.13']['spelDelar'] if x['etikett'] == 'b')
    alt = li('Alternativ: räkna ut \\(\\sigma\\) direkt med InverseNormal',
             p('Du behöver inte pröva olika värden. Skriv <code>(58 - 50) / InverseNormal(0, 1, 0.9)</code> i inmatningsfältet. '
               'InverseNormal(0, 1, 0.9) är hur många standardavvikelser 90:e percentilen ligger över medelvärdet (1.2816), '
               'och 58 − 50 = 8 min är samma avstånd i minuter. GeoGebra visar 6.24. Det engelska kommandonamnet fungerar även i svenska GeoGebra.'))
    ny_b = d['s'].replace('</ol><p class="facit-svar">', alt + '</ol><p class="facit-svar">', 1)
    assert ny_b != d['s']
    ANDRA['4.13']['_delb'] = ny_b
    ANDRA['4.13']['_ledtradb'] = ('<p>Det är inte en gissning: med \\(\\sigma=1\\) visar GeoGebra hur många standardavvikelser 90:e percentilen '
                                  'ligger över medelvärdet, och det antalet är detsamma för alla normalfördelningar. Dela sedan avståndet 58 − 50 '
                                  'med det antalet.</p>')

    # ------------------------------------------------------------ skriv
    byten = 0
    for uid, ny in ANDRA.items():
        u = by[uid]
        for k, v in ny.items():
            if k.startswith('_'):
                continue
            if v is None:
                continue
            u[k] = v
            byten += 1
        if '_delb' in ny:
            d = next(x for x in u['spelDelar'] if x['etikett'] == 'b')
            gammal_b = d['s']
            d['s'] = ny['_delb']; d['ledtrad'] = ny['_ledtradb']
            # Huvudfacit: samma tillägg i del b (huvudfacit innehåller delkortets facit ordagrant).
            assert u['s'].count(gammal_b) == 1, '4.13 huvudfacit'
            u['s'] = u['s'].replace(gammal_b, ny['_delb'])
    # Skriv tillbaka objekt för objekt så att bankens formatering i övrigt bevaras.
    for uid in ANDRA:
        mt = re.search(r'\{\s*"id":\s*"' + re.escape(uid) + r'"', src)
        assert mt, uid
        start = mt.start()
        _, slut = json.JSONDecoder().raw_decode(src, start)
        kompakt = '\n' not in src[start:slut]
        ny = json.dumps(by[uid], ensure_ascii=False) if kompakt else json.dumps(by[uid], ensure_ascii=False, indent=2).replace('\n', '\n  ')
        src = src[:start] + ny + src[slut:]
    json.loads(src[src.index('['):src.rindex(']') + 1])
    print(len(ANDRA), 'uppgifter,', byten, 'fält')
    if '--skriv' in sys.argv:
        BANK.write_text(src, encoding='utf-8', newline='')
        print('skrivet')


main()
