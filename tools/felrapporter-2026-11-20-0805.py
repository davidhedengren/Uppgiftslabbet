"""Felrapporter från Kunskapsgymmet 2026-11-20 08:05. Se agent/FELRAPPORTER_2026-11-20_0805.md.

Ma1  0.825     15/31 är samma förhållande som 15:31. Kunskapsgymmet godtar a/b för alla förhållanden a:b
               (kort_text); facit visar bråkformen.
Ma1  0.1383, 0.1362 d  grundpotensform underkändes (formatet decimalform). Enhets- och prefixbyten får formatet
               omvandling: målenheten krävs fortfarande, men talet får skrivas i grundpotensform.
Ma1  0.1004    ”tungvrickare”: ordningen för avrundningen skrivs ut (Emma avrundar först, kassan avrundar summan).
Ma4  1.156 a   perioden i radianer. Samma förtydligande i 14 liknande periodfrågor i kurvor_radianer.
Ma4  1.672     toleransen 0,001 godtog 2,829. Nu 0,0005, så att bara korrekt avrundade tre decimaler godtas.
Ma4  2.685     axelnamnet t (min) låg på kurvan. Figuren breddas och facit får tydligare rubriker.
Ma2  3.143     sidlängderna rättas i valfri ordning, liksom 3.140, 3.141, 3.187 och Ma3c 4.119.
Fy2  2.164     måtten ritas utanför bassängen.

  python tools/felrapporter-2026-11-20-0805.py [--skriv]
"""
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).parent))
import bankobjekt as B  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
SKRIV = '--skriv' in sys.argv


def byt(text, gammal, ny, n=1):
    assert text.count(gammal) == n, (gammal, text.count(gammal))
    return text.replace(gammal, ny)


def kopia(q):
    return json.loads(json.dumps(q))


def steg(rubrik, *innehall):
    return '<li><p class="facit-rubrik">' + rubrik + '</p>' + ''.join(innehall) + '</li>'


def matte(x):
    return '<div class="facit-matte">\\[' + x + '\\]</div>'


def facit(*stegen, svar):
    return ('<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">' + ''.join(stegen)
            + '</ol><p class="facit-svar"><strong>Svar:</strong> ' + svar + '</p></div>')


# ================================================================ Ma1
FORMKRAV = re.compile(r'vanligt tal|utan potens|tiopotens|grundpotens|decimalform', re.I)


def ma1(bank):
    Q = {q['id']: q for q in bank}
    nya = {}

    # ---- 0.825: förhållandet kan skrivas som bråk. Rättningen (a/b mot a:b) ligger i Kunskapsgymmets kort_text.
    q = kopia(Q['0.825'])
    assert q['rättSvar'] == '15:31' and 7500 * 31 == 15500 * 15
    nya['0.825'] = q

    q = nya['0.825']
    q['s'] = byt(q['s'], '<div class="facit-matte">\\[7500:15500=15:31\\].</div></li>',
                 '<div class="facit-matte">\\[7500:15500=15:31\\].</div></li>'
                 '<li><p>Förhållandet kan också skrivas som bråket \\(\\tfrac{15}{31}\\).</p></li>')

    # ---- enhets- och prefixbyten: grundpotensform godtas
    omv = []
    for q0 in bank:
        f = q0.get('svarFormat')
        fs = f if isinstance(f, list) else [f]
        if q0['omr'] not in ('prefix', 'enhetsbyten') or 'decimalform' not in fs:
            continue
        texter = [q0['t'], q0.get('kgInstruktion') or ''] + [
            (d.get('t') or '') + (d.get('fraga') or '') + (d.get('kgInstruktion') or '') for d in q0.get('spelDelar') or []]
        if any(FORMKRAV.search(re.sub(r'<[^>]+>', ' ', x)) for x in texter):
            print('  behåller decimalform (formkrav i texten):', q0['id'])
            continue
        q = kopia(nya.get(q0['id'], q0))
        q['svarFormat'] = ['omvandling' if x == 'decimalform' else x for x in f] if isinstance(f, list) else 'omvandling'
        nya[q['id']] = q
        omv.append(q['id'])
    assert '0.1383' in omv and '0.1362' in omv
    print('  omvandling:', len(omv))

    # ---- 0.1004: ordningen för avrundningen
    q = kopia(Q['0.1004'])
    assert q['rättSvar'] == 1
    priser = [12.45, 8.49, 23.50, 6.45, 9.48]
    emma = sum(int(p + 0.5) for p in priser)
    kassa = round(sum(priser), 2)
    assert (emma, kassa, round(kassa) - emma) == (59, 60.37, 1)
    q['t'] = ('<p>Emma köper fem varor som kostar 12,45 kr, 8,49 kr, 23,50 kr, 6,45 kr och 9,48 kr. Hon avrundar '
              'först varje pris till hela kronor och lägger sedan ihop de avrundade priserna. Kassan lägger i stället '
              'ihop de exakta priserna och avrundar summan till hela kronor.</p>'
              '<p>Hur många kronor skiljer det mellan Emmas summa och kassans summa?</p>')
    q['s'] = facit(
        steg('Emma avrundar varje pris först',
             '<p>12,45 → 12, 8,49 → 8, 23,50 → 24, 6,45 → 6 och 9,48 → 9.</p>',
             matte('12+8+24+6+9=59\\ \\text{kr}')),
        steg('Kassan lägger ihop de exakta priserna och avrundar summan',
             matte('\\begin{aligned}&12{,}45+8{,}49+23{,}50+6{,}45+9{,}48\\\\&=60{,}37\\approx60\\ \\text{kr}\\end{aligned}')),
        steg('Jämför summorna',
             matte('60-59=1\\ \\text{kr}'),
             '<p>Emma avrundar fyra av priserna nedåt och bara 23,50 kr uppåt. Därför blir hennes summa för liten.</p>'),
        svar='1 kr')
    nya['0.1004'] = q
    return nya


# ================================================================ Ma4
RADIANER = {
    '1.30': [('a) perioden<br>', 'a) perioden i radianer<br>'), ('del:a', '<p>perioden</p>', '<p>perioden i radianer</p>')],
    '1.73': [('a) perioden<br>', 'a) perioden i radianer<br>'), ('del:a', '<p>perioden</p>', '<p>perioden i radianer</p>')],
    '1.136': [('b) perioden<br>', 'b) perioden i radianer<br>'), ('del:b', '<p>perioden</p>', '<p>perioden i radianer</p>')],
    '1.291': [('b) perioden<br>', 'b) perioden i radianer<br>'), ('del:b', '<p>perioden</p>', '<p>perioden i radianer</p>')],
    '1.297': [('b) perioden<br>', 'b) perioden i radianer<br>'), ('del:b', '<p>perioden</p>', '<p>perioden i radianer</p>')],
    '1.154': [('a) bestäm perioden,<br>', 'a) bestäm perioden i radianer,<br>'),
              ('del:a', '<p>bestäm perioden,</p>', '<p>bestäm perioden i radianer,</p>')],
    '1.155': [('a) perioden för', 'a) perioden i radianer för'), ('b) perioden för', 'b) perioden i radianer för'),
              ('del:a', '<p>perioden för', '<p>perioden i radianer för'),
              ('del:b', '<p>perioden för', '<p>perioden i radianer för')],
    '1.156': [('a) Ange funktionens period.<br>', 'a) Ange funktionens period i radianer.<br>'),
              ('del:a', '<p>Ange funktionens period.</p>', '<p>Ange funktionens period i radianer.</p>')],
    '1.157': [('a) Ange funktionens period.<br>', 'a) Ange funktionens period i radianer.<br>'),
              ('del:a', '<p>Ange funktionens period.</p>', '<p>Ange funktionens period i radianer.</p>')],
    '1.158': [('a) Ange funktionens period.<br>', 'a) Ange funktionens period i radianer.<br>'),
              ('del:a', '<p>Ange funktionens period.</p>', '<p>Ange funktionens period i radianer.</p>')],
    '1.159': [('a) Ange funktionens period.<br>', 'a) Ange funktionens period i radianer.<br>'),
              ('del:a', '<p>Ange funktionens period.</p>', '<p>Ange funktionens period i radianer.</p>')],
    '1.151': [('<p>är given.</p>', '<p>är given, där \\(x\\) är i radianer.</p>'),
              ('intro', '<p>är given.</p>', '<p>är given, där \\(x\\) är i radianer.</p>')],
    '1.518': [('Bestäm amplitud och period.</p>', 'Bestäm amplitud och period. Ange perioden i radianer.</p>')],
    '1.522': [('Bestäm perioden för', 'Bestäm perioden i radianer för')],
    '1.524': [('Bestäm perioden.</p>', 'Bestäm perioden i radianer.</p>')],
}


def fig_2685(svg):
    """Bredda figuren så att axelnamnet t (min) står till höger om pilen i stället för på kurvan."""
    svg = byt(svg, 'viewBox="0 0 460 300"', 'viewBox="0 0 510 300"')
    svg = byt(svg, 'max-width:460px', 'max-width:510px')
    svg = byt(svg, '<rect x="1" y="1" width="458" height="298"', '<rect x="1" y="1" width="508" height="298"')
    svg = byt(svg, '<text x="450.0" y="249.0" font-family="Arial,sans-serif" font-size="15" text-anchor="end"',
              '<text x="458.0" y="263.0" font-family="Arial,sans-serif" font-size="15" text-anchor="start"')
    return svg


def mato2(bank):
    Q = {q['id']: q for q in bank}
    nya = {}
    for i, byten in RADIANER.items():
        q = kopia(Q[i])
        assert q['omr'] == 'kurvor_radianer' and 'radian' not in q['t'], i
        for b in byten:
            if len(b) == 2:
                q['t'] = byt(q['t'], *b)
            elif b[0] == 'intro':
                q['spelIntro'] = byt(q['spelIntro'], b[1], b[2])
            else:
                d = next(d for d in q['spelDelar'] if d['etikett'] == b[0][4:])
                falt = 'fraga' if 'fraga' in d else 't'
                d[falt] = byt(d[falt], b[1], b[2])
        nya[i] = q

    # ---- 1.156: facit med periodformeln och minsta värdet uträknat
    q = nya['1.156']
    assert q['rättSvar'] == ['pi', -1]
    fa = [steg('Perioden för \\(\\cos(kx)\\): \\(T=\\dfrac{2\\pi}{k}\\)',
               '<p>Här är \\(k=2\\), eftersom funktionen innehåller \\(\\cos(2x)\\).</p>',
               matte('T=\\frac{2\\pi}{2}=\\pi'),
               '<p>I grader skulle det motsvara 180°, men här räknas \\(x\\) i radianer.</p>')]
    fb = [steg('Cosinus är som minst \\(-1\\)',
               '<p>Funktionen är minst när \\(\\cos(2x)=-1\\).</p>',
               matte('f_{\\min}=2+3\\cdot(-1)=-1'))]

    def del_facit(stegen, svar):
        return ('<div class="facit-v2 facit-stegvis"><div class="spel-en-del"><ol class="facit-steglista" role="list">'
                + ''.join(stegen) + '</ol><p class="facit-svar"><strong>Svar:</strong> ' + svar + '</p></div></div>')

    def huvud_del(mark, stegen, svar):
        return ('<div class="facit-del"><span class="facit-mark">' + mark + ')</span><div class="facit-arbete">'
                '<ol class="facit-steglista" role="list">' + ''.join(stegen) + '</ol><p class="facit-svar"><strong>'
                'Svar:</strong> ' + svar + '</p></div></div>')

    q['s'] = ('<div class="facit-v2 facit-stegvis">' + huvud_del('a', fa, '\\(\\pi\\)')
              + huvud_del('b', fb, '\\(-1\\)') + '</div>')
    q['spelDelar'][0]['s'] = del_facit(fa, '\\(\\pi\\)')
    q['spelDelar'][1]['s'] = del_facit(fb, '\\(-1\\)')
    q['ledtrad'] = ('<p>a) Hur mycket måste \\(x\\) öka för att \\(2x\\) ska öka med ett helt varv, \\(2\\pi\\)?</p>'
                    '<p>b) Vilket är det minsta värde som \\(\\cos(2x)\\) kan få?</p>')

    # ---- 1.672: bara korrekt avrundade tre decimaler
    q = kopia(Q['1.672'])
    assert abs(q['rättSvar'] - 2 * 2 ** 0.5) < 1e-12 and q['tolerans'] == 0.001
    q['tolerans'] = 0.0005
    assert abs(2.828 - q['rättSvar']) <= 0.0005 < abs(2.829 - q['rättSvar'])
    nya['1.672'] = q

    # ---- 2.685: axelnamnet och facitrubrikerna
    q = kopia(Q['2.685'])
    gammal = re.search(r'<svg[\s\S]*?</svg>', q['t']).group(0)
    q['t'] = q['t'].replace(gammal, fig_2685(gammal))
    q['s'] = facit(
        steg('Gondolen är längst ned vid \\(t=0\\) och nästa gång vid \\(t=6\\)',
             '<p>Ett varv är klart när gondolen är tillbaka längst ned.</p>'),
        steg('Ett varv är en period: tiden mellan två lägsta punkter',
             matte('T=6-0=6\\ \\text{min}')),
        steg('Kontroll med de högsta punkterna',
             '<p>Gondolen är högst upp vid \\(t=3\\) och \\(t=9\\).</p>', matte('9-3=6\\ \\text{min}')),
        svar='6 min')
    nya['2.685'] = q
    return nya


# ================================================================ Ma2 och Ma3c
def mangd(bank, ids):
    Q = {q['id']: q for q in bank}
    nya = {}
    for i in ids:
        q = kopia(Q[i])
        assert isinstance(q['rättSvar'], list) and len(q['rättSvar']) == 2 and not q.get('svarsstruktur'), i
        assert not q.get('spelDelar') and not q.get('svarEtiketter'), i
        q['svarsstruktur'] = 'mängd'
        nya[i] = q
    return nya


def ma2(bank):
    return mangd(bank, ['3.140', '3.141', '3.143', '3.187'])


def mato1(bank):
    return mangd(bank, ['4.119'])


# ================================================================ Fy2
F = 'font-family="IBM Plex Mono"'


def fig_2164():
    """Vågbassäng med mätlinje. Måtten 0,50 m, 2,0 m och 3,0 m ritas utanför bassängen."""
    s1, s2, yk = 150, 370, 224          # källornas mitt
    m, p, ym = 260, 260 + 220 / 3 / 2, 82  # 220 px = 3,0 m, alltså 0,50 m = 36,67 px
    g = []
    a = g.append
    a('<rect x="60" y="56" width="400" height="200" rx="8" fill="#FAFAFB" stroke="#D5D2D7" stroke-width="1.4"/>')
    a(f'<line x1="82" y1="{ym}" x2="448" y2="{ym}" stroke="#5C575E" stroke-width="1.7"/>')
    a(f'<text x="445" y="{ym - 8}" text-anchor="end" {F} font-size="9.5" fill="#5C575E">mätlinje</text>')
    a(f'<line x1="{m}" y1="{ym}" x2="{m}" y2="{yk}" stroke="#9A959C" stroke-width="1.2" stroke-dasharray="5 5"/>')
    for x, namn, ankare, dx in ((s1, 'S₁', 'end', -24), (s2, 'S₂', 'start', 24)):
        a(f'<g transform="translate({x} {yk})"><rect x="-17" y="-24" width="34" height="48" rx="3" fill="#EDEEF1" '
          'stroke="#2B2527" stroke-width="2"/><circle cx="0" cy="-7" r="8" fill="#C9CCD2" stroke="#2B2527" '
          'stroke-width="1.5"/><circle cx="0" cy="12" r="4" fill="#C9CCD2" stroke="#2B2527" stroke-width="1.3"/>'
          f'<text x="{dx}" y="4" text-anchor="{ankare}" {F} font-size="11" font-weight="600" fill="#2B2527">{namn}'
          '</text></g>')
    a(f'<line x1="{s1}" y1="{yk}" x2="{p:.2f}" y2="{ym}" stroke="#B43123" stroke-width="1.8" stroke-dasharray="6 4"/>')
    a(f'<line x1="{s2}" y1="{yk}" x2="{p:.2f}" y2="{ym}" stroke="#2A5D9E" stroke-width="1.8" stroke-dasharray="6 4"/>')
    a(f'<text x="196" y="163" {F} font-size="10" font-weight="600" fill="#B43123">r₂</text>')
    a(f'<text x="341" y="145" {F} font-size="10" font-weight="600" fill="#2A5D9E">r₁</text>')
    a(f'<circle cx="{m}" cy="{ym}" r="5" fill="#2B2527"/>')
    a(f'<text x="{m - 10}" y="{ym - 9}" text-anchor="end" {F} font-size="11" font-weight="700" fill="#2B2527">M</text>')
    a(f'<circle cx="{p:.2f}" cy="{ym}" r="5" fill="#B43123"/>')
    a(f'<text x="{p + 10:.2f}" y="{ym - 9}" {F} font-size="11" font-weight="700" fill="#B43123">P</text>')
    tunn = 'stroke="#9A959C" stroke-width="0.9" stroke-dasharray="3 3"'
    # 0,50 m ovanför bassängen
    a(f'<line x1="{m}" y1="34" x2="{m}" y2="{ym - 6}" {tunn}/><line x1="{p:.2f}" y1="34" x2="{p:.2f}" y2="{ym - 6}" {tunn}/>')
    a(f'<line x1="{m}" y1="40" x2="{p:.2f}" y2="40" stroke="#B43123" stroke-width="1.2"/>')
    a(f'<line x1="{m}" y1="35" x2="{m}" y2="45" stroke="#B43123" stroke-width="1.2"/>'
      f'<line x1="{p:.2f}" y1="35" x2="{p:.2f}" y2="45" stroke="#B43123" stroke-width="1.2"/>')
    a(f'<text x="{(m + p) / 2:.2f}" y="28" text-anchor="middle" {F} font-size="10" font-weight="600" '
      'fill="#B43123">0,50 m</text>')
    # 2,0 m till vänster om bassängen
    a(f'<line x1="36" y1="{ym}" x2="80" y2="{ym}" {tunn}/><line x1="36" y1="{yk}" x2="80" y2="{yk}" {tunn}/>')
    a(f'<line x1="42" y1="{ym}" x2="42" y2="{yk}" stroke="#5C575E" stroke-width="1.2"/>')
    a(f'<line x1="37" y1="{ym}" x2="47" y2="{ym}" stroke="#5C575E" stroke-width="1.2"/>'
      f'<line x1="37" y1="{yk}" x2="47" y2="{yk}" stroke="#5C575E" stroke-width="1.2"/>')
    a(f'<text x="36" y="{(ym + yk) / 2 + 4:.0f}" text-anchor="end" {F} font-size="10" font-weight="600" '
      'fill="#5C575E">2,0 m</text>')
    # 3,0 m under bassängen
    a(f'<line x1="{s1}" y1="{yk + 28}" x2="{s1}" y2="279" {tunn}/><line x1="{s2}" y1="{yk + 28}" x2="{s2}" y2="279" {tunn}/>')
    a(f'<line x1="{s1}" y1="274" x2="{s2}" y2="274" stroke="#5C575E" stroke-width="1.2"/>')
    a(f'<line x1="{s1}" y1="269" x2="{s1}" y2="279" stroke="#5C575E" stroke-width="1.2"/>'
      f'<line x1="{s2}" y1="269" x2="{s2}" y2="279" stroke="#5C575E" stroke-width="1.2"/>')
    a(f'<text x="{(s1 + s2) / 2:.0f}" y="292" text-anchor="middle" {F} font-size="10" font-weight="600" '
      'fill="#5C575E">3,0 m</text>')
    titel = 'Mätlinje i en vågbassäng framför två vågkällor; punkten P ligger 0,50 meter från M.'
    return ('<svg viewBox="0 0 475 300" width="620" height="392" preserveAspectRatio="xMidYMid meet" role="img" '
            f'aria-label="{titel}" xmlns="http://www.w3.org/2000/svg"><title>{titel}</title>' + ''.join(g) + '</svg>')


def fy2(bank):
    q = kopia(next(q for q in bank if q['id'] == '2.164'))
    gammal = re.findall(r'<svg[\s\S]*?</svg>', q['t'])
    assert len(gammal) == 1 and '2 m</text>' in gammal[0]
    for k in ('s', 'spelIntro', 'ledtrad'):
        assert '<svg' not in (q.get(k) or ''), k
    q['t'] = q['t'].replace(gammal[0], fig_2164())
    # Kontroll: P minimum. r1 till den närmaste källan, r2 till den bortre.
    r1, r2 = (2 ** 2 + 1 ** 2) ** 0.5, (2 ** 2 + 2 ** 2) ** 0.5
    assert abs((r2 - r1) - 1.18 / 2) < 0.01
    return {'2.164': q}


def ersatt_kompakt(src, nya):
    """Ma2 har både kompakta objekt ({"id":"3.140",...} på en rad) och indragna. Kompakta objekt skrivs kompakt igen."""
    dec = json.JSONDecoder()
    kvar = {}
    for uid, obj in nya.items():
        nyckel = '{"id":"' + uid + '"'
        if src.count(nyckel) != 1:
            kvar[uid] = obj
            continue
        i = src.index(nyckel)
        gammal, slut = dec.raw_decode(src, i)
        if src[i:slut] == json.dumps(gammal, ensure_ascii=False, separators=(',', ':')):
            src = src[:i] + json.dumps(obj, ensure_ascii=False, separators=(',', ':')) + src[slut:]
            continue
        # Talformat som 1e-9 skrivs annorlunda av Python. Bara nya nycklar läggs då till sist i objektet.
        assert all(obj[k] == v for k, v in gammal.items()) and set(gammal) <= set(obj), uid
        tillagg = ''.join(',' + json.dumps(k, ensure_ascii=False) + ':' + json.dumps(obj[k], ensure_ascii=False)
                          for k in obj if k not in gammal)
        assert src[slut - 1] == '}'
        src = src[:slut - 1] + tillagg + src[slut - 1:]
    return B.ersatt(src, kvar) if kvar else src


def main():
    andrade = {}
    for fil, funk in (('uppgifterma1.js', ma1), ('uppgiftermato2.js', mato2), ('uppgifterma2.js', ma2),
                      ('uppgiftermato1.js', mato1), ('uppgifter2.js', fy2)):
        src, bank = B.las(ROOT / fil)
        nya = funk(bank)
        ny_src = ersatt_kompakt(src, nya)
        ny_bank = json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
        assert [q['id'] for q in ny_bank] == [q['id'] for q in bank]
        andr = [q['id'] for q, r in zip(ny_bank, bank) if q != r]
        assert sorted(andr) == sorted(nya), (fil, set(andr) ^ set(nya))
        andrade[fil] = andr
        print(fil, len(andr), andr if len(andr) < 12 else andr[:6] + ['…'])
        if SKRIV:
            B.skriv(ROOT / fil, ny_src)
    return andrade


if __name__ == '__main__':
    main()
