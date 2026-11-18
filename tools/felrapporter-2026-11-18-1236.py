"""Felrapporter från Kunskapsgymmet 2026-11-18 12:36. Se agent/FELRAPPORTER_2026-11-18_1236.md.

Fy1  3.196 c  ”otydlig”: tydligare situation (vagn på rak bana, figur med riktningar) och tabell i stället för
              ”Hastigheterna är -5, -8, -11 m/s.” i alla sex delar. Svaren är oförändrade.
Fy1  3.651, 3.652 läraren: kraftuppgifter ligger fel i ”Hastighet som vektor”. Alla 66 kraftuppgifter i området
              `vektorer` flyttas till `kraftvektorer` (kap 4, ”Vektorer”) med omrTidigare/familjTidigare.
Ma4  1.319 a  svaret ska få anges både med π och som decimaltal i cm. Samma ändring i cirkelsektorns övriga
              längd- och areasvar med π där frågan inte kräver exakt svar: 1.118, 1.124, 1.167, 1.306, 1.324.
Ma4  1.424   formelbladet skriver cos 45° = 1/√2. Facit visar båda formerna.
Ma1  2.306 c läraren: svårt att förklara. Konkret fråga om ordningen och ett facit utan ”kommutativ”; c-kortet är
              självbärande.
Ma1  1.87    parentes runt 2a + 3 underkändes. Frågan anger formen 4(b − 2)(…) och svaret rättas som uttryck.

  python tools/felrapporter-2026-11-18-1236.py [--skriv]
"""
import json
import math
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).parent))
import bankobjekt as B  # noqa: E402
import a_uppgifter_hjalp as H  # noqa: E402
from a_uppgifter_hjalp import svg, tt, linje, pil, rekt, cirkel, BLA, ORA, GRA, INK  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
SKRIV = '--skriv' in sys.argv


def byt(text, gammal, ny, n=1):
    assert text.count(gammal) == n, (gammal, text.count(gammal))
    return text.replace(gammal, ny)


# ================================================================ Fy1
def fy1(bank):
    Q = {q['id']: q for q in bank}
    nya = {}

    # ---- 3.196: vagn på rak bana, tabell per del
    q = json.loads(json.dumps(Q['3.196']))
    data = [(-20, -15, -10), (2, 4, 6), (-5, -8, -11), (12, 8, 4), (5, 0, -5), (-11, -8, -5)]
    assert q['rättSvar'] == [(c - a) / 2 for a, _, c in data]
    tal = lambda v: str(v).replace('-', '−')

    def fig():
        b = linje(20, 92, 420, 92, INK, 2.5)
        for x in range(40, 420, 40):
            b += linje(x, 92, x - 8, 102, GRA, 1.2)
        b += rekt(180, 46, 80, 34, '#f2c48d', INK, 2, 5) + cirkel(198, 84, 9, INK, '#fff', 2) + cirkel(242, 84, 9, INK, '#fff', 2)
        b += pil(270, 30, 390, 30, BLA, 3) + tt(330, 22, 'positiv hastighet', 14, 'middle', BLA, True)
        b += pil(170, 30, 50, 30, ORA, 3) + tt(110, 22, 'negativ hastighet', 14, 'middle', ORA, True)
        return svg(440, 116, b, 'En vagn på en rak, horisontell bana. Hastighet åt höger är positiv och hastighet åt vänster negativ.')

    intro = ('<p>En vagn rullar fram och tillbaka på en rak bana. Hastigheter åt höger räknas positiva och hastigheter åt '
             'vänster negativa.</p>' + fig())
    fraga = '<p>Hur stor är vagnens medelacceleration mellan 0 s och 2 s?</p>'

    def tabell(v):
        return ('<table class="data"><tr><th>t (s)</th><th>0</th><th>1</th><th>2</th></tr>'
                f'<tr><th>v (m/s)</th><td>{tal(v[0])}</td><td>{tal(v[1])}</td><td>{tal(v[2])}</td></tr></table>')

    q['t'] = (intro + '<p>Tabellen visar vagnens hastighet v (m/s) vid tre tidpunkter i sex olika försök, a–f. Hur stor är '
              'medelaccelerationen mellan 0 s och 2 s i varje försök?</p>'
              '<table class="data"><tr><th>Försök</th><th>t = 0 s</th><th>t = 1 s</th><th>t = 2 s</th></tr>'
              + ''.join(f'<tr><th>{e})</th><td>{tal(v[0])}</td><td>{tal(v[1])}</td><td>{tal(v[2])}</td></tr>'
                        for e, v in zip('abcdef', data)) + '</table>')
    q['spelIntro'] = intro
    for d, v in zip(q['spelDelar'], data):
        d['fraga'] = tabell(v) + fraga
        d['t'] = intro + d['fraga']
    nya['3.196'] = q

    # ---- kraftuppgifter i "Hastighet som vektor" -> kraftvektorer
    flytt = []
    for q0 in bank:
        if q0['omr'] != 'vektorer':
            continue
        text = re.sub('<[^>]+>', ' ', re.sub(r'<svg[\s\S]*?</svg>', '', q0['t']))
        enh = json.dumps(q0.get('svarEnhet'), ensure_ascii=False)
        if re.search(r'kraft|\bN\b|newton', text, re.I) or '"N"' in enh:
            flytt.append(q0['id'])
    assert len(flytt) == 66 and {'3.651', '3.652'} <= set(flytt), len(flytt)
    for uid in flytt:
        q = json.loads(json.dumps(Q[uid]))
        if q['familj'] == 'Dela upp vektorer i komposanter':
            fam, nyckel = 'Komposantuppdelning', 'kraftvektorer__komposantuppdelning'
        else:
            assert q['familj'] == 'Addera vektorer', uid
            if q.get('trigonometri'):
                fam, nyckel = 'Resultantbestämning med trigonometri', 'kraftvektorer__resultantbestamning_med_trigonometri'
            else:
                fam, nyckel = 'Resultantbestämning utan trigonometri', 'kraftvektorer__resultantbestamning_utan_trigonometri'
        q['omrTidigare'] = list(q.get('omrTidigare') or []) + ['vektorer']
        q['familjTidigare'] = list(q.get('familjTidigare') or []) + [q['familj']]
        if q.get('familjNyckel') and not q.get('familjNyckelTidigare'):
            q['familjNyckelTidigare'] = q['familjNyckel']
        q['omr'], q['kap'], q['familj'], q['familjNyckel'] = 'kraftvektorer', 4, fam, nyckel
        nya[uid] = q
    return nya, flytt


# ================================================================ Ma4 (mato2)
PI = {  # id: {delindex: (uttryck, värde, decimaltext)}
    '1.319': {0: ('2*pi', 2 * math.pi), 1: ('5*pi', 5 * math.pi), 2: ('15*pi/2', 15 * math.pi / 2)},
    '1.324': {0: ('49*pi/12', 49 * math.pi / 12), 1: ('49*pi/4', 49 * math.pi / 4), 2: ('49*pi/3', 49 * math.pi / 3)},
    '1.118': {1: ('4*pi', 4 * math.pi), 2: ('12*pi', 12 * math.pi)},
    '1.124': {0: ('4*pi', 4 * math.pi), 1: ('12*pi', 12 * math.pi)},
    '1.167': {0: ('10*pi', 10 * math.pi), 1: ('60*pi', 60 * math.pi)},
    '1.306': {0: ('5*pi/3', 5 * math.pi / 3), 1: ('10*pi', 10 * math.pi), 3: ('6*pi', 6 * math.pi)},
}
# Facittext: det exakta slutsvaret får ett närmevärde (tre värdesiffror) i huvudfacit och delkortens facit.
SBYT = {
    '1.319': [(r'\(2\pi\)', r'\(2\pi\approx6{,}28\)'), (r'\(5\pi\)', r'\(5\pi\approx15{,}7\)'),
              (r'\(15\pi/2\)', r'\(15\pi/2\approx23{,}6\)')],
    '1.324': [(r'\(49\pi/12\)', r'\(49\pi/12\approx12{,}8\)'), (r'\(49\pi/4\)', r'\(49\pi/4\approx38{,}5\)'),
              (r'\(49\pi/3\)', r'\(49\pi/3\approx51{,}3\)')],
    '1.118': [(r'\(4\pi\)', r'\(4\pi\approx12{,}6\)'), (r'\(12\pi\)', r'\(12\pi\approx37{,}7\)'),
              (r'\boxed{4\pi}', r'\boxed{4\pi\approx12{,}6}'), (r'\boxed{12\pi}', r'\boxed{12\pi\approx37{,}7}')],
    '1.124': [(r'\boxed{4\pi\text{ cm}}', r'\boxed{4\pi\approx12{,}6\text{ cm}}'),
              (r'\boxed{12\pi\text{ cm}^2}', r'\boxed{12\pi\approx37{,}7\text{ cm}^2}'),
              (r'\(4\pi\)', r'\(4\pi\approx12{,}6\)'), (r'\(12\pi\)', r'\(12\pi\approx37{,}7\)')],
    '1.167': [(r'\(10\pi\)', r'\(10\pi\approx31{,}4\)'), (r'\(60\pi\)', r'\(60\pi\approx188\)')],
    '1.306': [(r'\(5\pi/3\)', r'\(5\pi/3\approx5{,}24\)'), (r'\(10\pi\)', r'\(10\pi\approx31{,}4\)'),
              (r'\(6\pi\)', r'\(6\pi\approx18{,}8\)')],
}


def facitfalt(q):
    """Alla facittexter i uppgiften: huvudfacit och delkortens facit."""
    yield q, 's'
    for d in q.get('spelDelar') or []:
        yield d, 's'


def mato2(bank):
    Q = {q['id']: q for q in bank}
    nya = {}
    for uid, delar in PI.items():
        q = json.loads(json.dumps(Q[uid]))
        n = len(q['rättSvar'])
        tol = list(q['tolerans']) if isinstance(q.get('tolerans'), list) else [q.get('tolerans')] * n
        for i, (uttr, varde) in delar.items():
            assert q['rättSvar'][i] == uttr and q['svarFormat'][i] == 'uttryck', (uid, i)
            assert not re.search('exakt', q['t'] + json.dumps(q.get('spelDelar'), ensure_ascii=False), re.I), uid
            q['rättSvar'][i], q['svarFormat'][i], tol[i] = varde, 'numeriskt', 1e-9
        q['tolerans'] = tol
        for gammal, ny in SBYT[uid]:
            antal = sum(obj[f].count(gammal) for obj, f in facitfalt(q))
            assert antal >= 1, (uid, gammal)
            for obj, f in facitfalt(q):
                obj[f] = obj[f].replace(gammal, ny)
        nya[uid] = q

    q = json.loads(json.dumps(Q['1.424']))
    s = q['s']
    s = byt(s, r'<p class="facit-rubrik">Standardvärdet \(\cos45^\circ=\tfrac{\sqrt2}{2}\)</p>',
            r'<p class="facit-rubrik">Formelbladet: \(\cos45^\circ=\tfrac{1}{\sqrt2}\)</p>')
    s = byt(s, r'<div class="facit-matte">\[\cos(2v)=\cos45^\circ=\frac{\sqrt2}{2}\]</div>',
            r'<div class="facit-matte">\[\cos(2v)=\cos45^\circ=\frac{1}{\sqrt2}\]</div>'
            r'<p>Formelbladet skriver \(\tfrac{1}{\sqrt2}\). Förläng med \(\sqrt2\) så får du den andra vanliga formen:</p>'
            r'<div class="facit-matte">\[\frac{1}{\sqrt2}=\frac{1\cdot\sqrt2}{\sqrt2\cdot\sqrt2}=\frac{\sqrt2}{2}\]</div>')
    s = byt(s, r'<strong>Svar:</strong> \(\frac{\sqrt2}{2}\)</p>',
            r'<strong>Svar:</strong> \(\frac{1}{\sqrt2}\), som också kan skrivas \(\frac{\sqrt2}{2}\).</p>')
    q['s'] = s
    assert q['rättSvar'] == 'sqrt(2)/2' and q['svarFormat'] == 'uttryck'
    nya['1.424'] = q
    return nya


# ================================================================ Ma1
def ma1(bank):
    Q = {q['id']: q for q in bank}
    nya = {}
    f = lambda x: 3 * x - 5
    g = lambda x: 2 * x + 4
    assert (f(g(3)), g(f(3))) == (25, 12)

    q = json.loads(json.dumps(Q['2.306']))
    fun = r'<p>Funktionerna är \(f(x)=3x-5\) och \(g(x)=2x+4\).</p>'
    c_fraga = (r'I a) räknar du först ut \(g(3)\) och sätter in svaret i \(f\). I b) är det tvärtom. '
               r'Förklara med hjälp av uträkningarna varför svaren blir olika.')
    c_kort = (r'Julia räknar ut att \(f(g(3))=25\) men att \(g(f(3))=12\). Förklara med hjälp av uträkningarna varför '
              r'svaren blir olika.')
    q['t'] = byt(q['t'], r'c) Förklara varför svaren inte behöver bli lika.</p>', 'c) ' + c_fraga + '</p>')

    def li(rubrik, *delar):
        return f'<li><p class="facit-rubrik">{rubrik}</p>{"".join(delar)}</li>'

    mt = lambda x: f'<div class="facit-matte">\\[{x}\\]</div>'
    p = lambda x: f'<p>{x}</p>'
    fac = lambda steg, svar: ('<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">' + ''.join(steg)
                              + f'</ol><p class="facit-svar"><strong>Svar:</strong> {svar}</p></div>')
    sa = fac([li(r'Den inre funktionen räknas först: \(g(3)\)', mt(r'g(3)=2\cdot3+4=10')),
              li(r'Sätt in 10 i \(f\)', mt(r'f(g(3))=f(10)=3\cdot10-5=25'))], r'\(f(g(3))=25\)')
    sb = fac([li(r'Den inre funktionen räknas först: \(f(3)\)', mt(r'f(3)=3\cdot3-5=4')),
              li(r'Sätt in 4 i \(g\)', mt(r'g(f(3))=g(4)=2\cdot4+4=12'))], r'\(g(f(3))=12\)')
    sc = fac([li(r'I \(f(g(3))\) räknas \(g\) först', mt(r'g(3)=10\quad\Rightarrow\quad f(10)=25'),
                 p(r'Det tal som \(f\) får är 10.')),
              li(r'I \(g(f(3))\) räknas \(f\) först', mt(r'f(3)=4\quad\Rightarrow\quad g(4)=12'),
                 p(r'Det tal som \(g\) får är 4.')),
              li('Ordningen avgör vilket tal som sätts in i den andra funktionen',
                 p(r'Funktionerna gör olika saker med ett tal: \(f\) multiplicerar med 3 och drar bort 5, medan \(g\) '
                   r'multiplicerar med 2 och lägger till 4. När ordningen byts får den andra funktionen ett annat tal, '
                   r'och den behandlar det på ett annat sätt. Därför blir slutresultaten olika.'))],
             'Den funktion som räknas först bestämmer vilket tal den andra funktionen får. Eftersom \\(f\\) och \\(g\\) '
             'räknar på olika sätt blir \\(f(g(3))\\) och \\(g(f(3))\\) olika.')
    q['s'] = ('<div class="facit-v2 facit-stegvis">' + ''.join(
        f'<div class="facit-del"><span class="facit-mark">{e})</span><div class="facit-arbete">{x[len("<div class=\"facit-v2 facit-stegvis\">"):-len("</div>")]}</div></div>'
        for e, x in zip('abc', (sa, sb, sc))) + '</div>')
    da, db, dc = q['spelDelar']
    da['s'], db['s'] = sa, sb
    dc['t'] = byt(dc['t'], '<p>Förklara varför svaren inte behöver bli lika.</p>', '<p>' + c_kort + '</p>')
    assert dc['t'].startswith(fun)
    dc['s'] = sc
    dc['ledtrad'] = ('<p>Skriv ut båda uträkningarna steg för steg. Vilket tal sätts in i \\(f\\) i den ena, och vilket tal '
                     'sätts in i \\(g\\) i den andra?</p>')
    nya['2.306'] = q

    q = json.loads(json.dumps(Q['1.87']))
    assert q['rättSvar'] == '2a+3' and q['svarFormat'] == 'förenklat_polynom'
    q['t'] = (r'<p>Skriv uttrycket \(8a(b-2)+12(b-2)\) på formen \(4(b-2)\cdot(\ \ldots\ )\). '
              r'Vad ska stå i den sista parentesen?</p>')
    q['s'] = fac([li(r'Bryt ut den gemensamma faktorn \(b-2\)', mt(r'8a(b-2)+12(b-2)=(b-2)(8a+12)')),
                  li(r'Bryt ut 4 ur \(8a+12\)', mt(r'8a+12=4(2a+3)')),
                  li(r'Skriv på formen \(4(b-2)\cdot(\ \ldots\ )\)', mt(r'(b-2)\cdot4(2a+3)=4(b-2)(2a+3)'))],
                 r'\(2a+3\)')
    q['svarFormat'] = 'uttryck'
    nya['1.87'] = q
    return nya


def main():
    andrade = {}
    for fil, funk in (('uppgifter.js', fy1), ('uppgiftermato2.js', mato2), ('uppgifterma1.js', ma1)):
        src, bank = B.las(ROOT / fil)
        ut = funk(bank)
        nya, flytt = ut if isinstance(ut, tuple) else (ut, None)
        assert not B.kontrollera_rundresa(ROOT / fil, set(nya)), fil
        ny_src = B.ersatt(src, nya)
        ny_bank = json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
        assert len(ny_bank) == len(bank) and [q['id'] for q in ny_bank] == [q['id'] for q in bank]
        andr = [q['id'] for q, r in zip(ny_bank, bank) if q != r]
        assert sorted(andr) == sorted(nya), (fil, set(andr) ^ set(nya))
        andrade[fil] = andr
        print(fil, len(andr), andr if len(andr) < 12 else andr[:6] + ['…'])
        if flytt:
            print('  flyttade till kraftvektorer:', len(flytt))
        if SKRIV:
            B.skriv(ROOT / fil, ny_src)
    return andrade


if __name__ == '__main__':
    main()
