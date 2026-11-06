"""Enheten ska synas i facit (användarbeslut 2026-11-06).

Svarsrader som saknade svarets enhet får den, facit utan svarsrad får en, och fem Fy1-svarsrader
med e-notation (2,2475e-05 N) skrivs som tiopotens. Varje ändring sker inom uppgiftens eget
JSON-objekt och kräver exakt en träff. Svaren är kontrollräknade (se agent/FACIT_ENHET_2026-11-06.md).

  python tools/facit-enhet-svarsrad-2026-11-06.py [--skriv]
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SV = '<p class="facit-svar"><strong>Svar:</strong> '

ANDRINGAR = {
    'uppgifterma1.js': [
        ('0.633', SV + '16</p>', SV + '16 s</p>'),
        ('0.757', SV + '<strong>4,5</strong></p>', SV + '4,5 MW</p>'),
        ('3.543', SV + r'\(p=20\)</p>', SV + r'\(p=20\), alltså 20 %</p>'),
        ('1.1320', SV + r'\(x=6\)</p>', SV + r'\(x=6\), alltså 6 cm</p>'),
        ('1.1330', SV + r'\(x=6\)</p>', SV + r'\(x=6\), alltså 6 cm</p>'),
    ],
    'uppgifterma2.js': [
        ('1.234', '<p class="facit-svar"><strong>105</strong></p>', SV + '105 kr</p>'),
        ('2.760', SV + r'\(x=6\)</p>', SV + r'\(x=6\), alltså 6 cm</p>'),
        ('3.38', r'<strong>\(AB=10\).</strong>', r'<strong>\(AB=10\) längdenheter.</strong>'),
        ('3.64', r'Medianens längd är \(\sqrt{185}\).', r'Medianens längd är \(\sqrt{185}\approx13{,}6\) längdenheter.'),
        ('3.264', '<strong>Svar: 5.</strong>', '<strong>Svar: 5 längdenheter.</strong>'),
        ('3.266', '<strong>Svar: 10.</strong>', '<strong>Svar: 10 längdenheter.</strong>'),
        ('3.296', '<p class="facit-svar"><strong>6</strong></p>', SV + '6 längdenheter</p>'),
        ('3.317', r'\[5-(-2)=7\].</div></div></li></ol></div>',
         r'\[5-(-2)=7\].</div></div></li></ol>' + SV + '7 längdenheter</p></div>'),
        ('3.326', r'\(5\). Elin adderade', r'\(5\) längdenheter. Elin adderade'),
        ('3.346', r'\[120-50=70\].</div></li></ol></div>',
         r'\[120-50=70\].</div></li></ol>' + SV + r'\(70^\circ\)</p></div>'),
        ('5.01', '10 Bas och 8 Plus.', '10 Bas-paket och 8 Plus-paket.'),
        ('5.142', r'y=12.\]</p></li></ol></div>', r'y=12.\]</p></li></ol>' + SV + '12 Premium-abonnemang</p></div>'),
        ('5.09', '210 Bas och 210 Premium.', '210 Bas-abonnemang och 210 Premium-abonnemang.'),
        ('5.25', 'Påståendet stämmer inte. Exakt hälften var typ B.',
         'Påståendet stämmer inte. 250 produkter var typ A och 250 produkter typ B, alltså exakt hälften.'),
        ('5.90', 'största värdet är 64 vid', 'största värdet är 64 W vid'),
        ('5.103', '250 yngre och 250 äldre.', '250 yngre och 250 äldre personer.'),
        ('5.157', r'Det ger \(x=14\) och \(y=10\).</p></li></ol></div>',
         r'Det ger \(x=14\) och \(y=10\).</p></li></ol>' + SV + '14 korta och 10 långa besök</p></div>'),
        ('5.169', 'A: 120, B: 180.', 'Grupp A: 120 personer, grupp B: 180 personer.'),
        ('1.697', r'\(l=9\).</p></div>', r'\(l=9\).</p>' + SV + 'Längden är 9 cm och bredden 6 cm.</p></div>'),
        ('1.699', r'\(k=60-30=30\).</p></div>', r'\(k=60-30=30\).</p>' + SV + 'Ett kaffe kostar 30 kr och en bulle 15 kr.</p></div>'),
    ],
    'uppgiftermatf1.js': [
        ('3.262', SV + '-6</p>', SV + r'\(-6\ \mathrm{cm^2/s}\)</p>'),
        ('3.264', SV + r'\(11520\pi\)</p>', SV + r'\(11520\pi\approx36\,191\ \mathrm{cm^3/s}\)</p>'),
        ('3.265', SV + r'\(\frac{12}{\pi}\)</p>', SV + r'\(\frac{12}{\pi}\approx3{,}82\ \mathrm{cm/s}\)</p>'),
        ('3.266', SV + r'\(1680\pi\)</p>', SV + r'\(1680\pi\approx5\,278\ \mathrm{cm^3/s}\)</p>'),
    ],
    'uppgifter.js': [
        ('8.22', r'\(2{,}3072e-24\,\mathrm{N}\)', r'\(2{,}31\cdot10^{-24}\,\mathrm{N}\)', 'alla'),
        ('8.24', r'\(8{,}74028e-05\,\mathrm{N}\)', r'\(8{,}74\cdot10^{-5}\,\mathrm{N}\)', 'alla'),
        ('8.33', r'\(8{,}42812e-05\,\mathrm{N}\)', r'\(8{,}43\cdot10^{-5}\,\mathrm{N}\)', 'alla'),
        ('8.119', r'\(2{,}2475e-05\,\mathrm{N}\)', r'\(2{,}25\cdot10^{-5}\,\mathrm{N}\)', 'alla'),
        ('8.159', r'\(4{,}21406e-05\,\mathrm{N}\)', r'\(4{,}21\cdot10^{-5}\,\mathrm{N}\)', 'alla'),
    ],
}

# Kontrollräkning av de tal som skrivs in i facit.
import math
assert math.isclose(11520 * math.pi, 36191.147, rel_tol=1e-6) and round(12 / math.pi, 2) == 3.82
assert round(1680 * math.pi) == 5278 and round(math.sqrt(185), 1) == 13.6
assert math.isclose(4 * math.pi * 24 ** 2 * 5, 11520 * math.pi) and math.isclose(2 * math.pi * 6 * 20 * 7, 1680 * math.pi)
assert math.isclose(2 * 5 * -0.6, -6) and 30 * 14 + 45 * 10 == 870 and 100 * 18 + 150 * 12 == 3600


# Ma2 3.454 a: delkortets facit saknade svarsrad.



# Långa pilkedjor som var för breda i mobil bryts i rader.
ANDRINGAR['uppgifterma2.js'] += [
    ('3.454', r'\[(8+r)^2=r^2+12^2\quad\Longrightarrow\quad64+16r+r^2=r^2+144\quad\Longrightarrow\quad16r=80\quad\Longrightarrow\quad r=5.\]',
     r'\[\begin{aligned}(8+r)^2&=r^2+12^2\\64+16r+r^2&=r^2+144\\16r&=80\\r&=5\end{aligned}\]', 'alla'),
    ('5.142', r'\[100(30-y)+150y=3600\Rightarrow50y=600\Rightarrow y=12.\]',
     r'\[\begin{aligned}100(30-y)+150y&=3600\\3000+50y&=3600\\50y&=600\\y&=12\end{aligned}\]'),
]
ANDRINGAR['uppgifterma1.js'].append(
    ('3.543', r'(1+x)(1-x)=0{,}96\;\Leftrightarrow\;1-x^2=0{,}96\;\Leftrightarrow\;x^2=0{,}04.',
     r'\begin{aligned}(1+x)(1-x)&=0{,}96\\1-x^2&=0{,}96\\x^2&=0{,}04\end{aligned}'))

# Ma2 3.454 a: delkortets facit saknade svarsrad (efter radbrytningen ovan).
ANDRINGAR['uppgifterma2.js'].append(
    ('3.454', r'r&=5\end{aligned}\]</p></li></ol></div>', r'r&=5\end{aligned}\]</p></li></ol>' + SV + 'Radien är 5 cm.</p></div>'))


def li(rubrik, *delar):
    return f'<li><p class="facit-rubrik">{rubrik}</p>{"".join(delar)}</li>'


def matte(x):
    return f'<div class="facit-matte">\\[{x}\\]</div>'


def facit(steg, svar):
    return ('<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">' + ''.join(steg)
            + '</ol>' + SV + svar + '</p></div>')


SYSTEM = li('Två villkor: antalet paket och faktureringen',
            r'<p>Låt \(x\) vara antalet Bas-paket och \(y\) antalet Plus-paket.</p>',
            matte(r'\begin{cases}x+y=18\\8000x+12000y=176000\end{cases}'))
ELIM_Y = li(r'Eliminera \(y\): multiplicera den första ekvationen med 12 000',
            matte(r'12000x+12000y=216000'),
            '<p>Subtrahera den andra ekvationen från den nya:</p>',
            matte(r'\begin{aligned}4000x&=40000\\x&=10\end{aligned}'))
ELIM_X = li(r'Eliminera \(x\): multiplicera den första ekvationen med 8 000',
            matte(r'8000x+8000y=144000'),
            '<p>Subtrahera den nya ekvationen från den andra:</p>',
            matte(r'\begin{aligned}4000y&=32000\\y&=8\end{aligned}'))
KOSTNAD = li('Rörliga kostnader: antal paket gånger kostnad per paket',
             matte(r'\begin{aligned}&10\cdot2500+8\cdot4000\\&=25000+32000=57000\ \text{kr}\end{aligned}'))
KVAR = li('Dra bort de rörliga kostnaderna från faktureringen', matte(r'176000-57000=119000\ \text{kr}'))
assert 10 + 8 == 18 and 8000 * 10 + 12000 * 8 == 176000 and 10 * 2500 + 8 * 4000 == 57000


def skriv_om_5_01(q):
    huvud_a = facit([SYSTEM, ELIM_Y,
                     li(r'Antalet Plus-paket: \(y=18-x\)', matte(r'y=18-10=8')),
                     li('Kontroll i faktureringen', matte(r'\begin{aligned}&8000\cdot10+12000\cdot8\\&=80000+96000=176000\end{aligned}'))],
                    '10 Bas-paket och 8 Plus-paket.')
    huvud_b = facit([KOSTNAD, KVAR], '119 000 kr återstår.')
    q['s'] = ('<div class="facit-v2 facit-stegvis">'
              f'<div class="facit-del"><span class="facit-mark">a)</span><div class="facit-arbete">{huvud_a}</div></div>'
              f'<div class="facit-del"><span class="facit-mark">b)</span><div class="facit-arbete">{huvud_b}</div></div></div>')
    q['ledtrad'] = ('<p>Ställ upp två ekvationer: en för hur många paket som såldes och en för hur mycket '
                    'faktureringen blev.</p>')
    a, b, c = q['spelDelar']
    a['s'] = facit([SYSTEM, ELIM_Y], '10 Bas-paket.')
    b['s'] = facit([SYSTEM, ELIM_X], '8 Plus-paket.')
    c['fraga'] = '<p>Det såldes 10 Bas-paket och 8 Plus-paket. Hur mycket återstår av faktureringen efter de rörliga kostnaderna?</p>'
    c['s'] = facit([KOSTNAD, KVAR], '119 000 kr.')


OBJEKT = {'uppgifterma2.js': {'5.01': skriv_om_5_01}}


def omrade(src, uid):
    """Exakt start och slut för uppgiftens JSON-objekt i bankfilen."""
    dec = json.JSONDecoder()
    pos = src.index('[') + 1
    while True:
        while src[pos] in ' \t\r\n,':
            pos += 1
        if src[pos] == ']':
            raise KeyError(uid)
        obj, slut = dec.raw_decode(src, pos)
        if obj.get('id') == uid:
            return pos, slut
        pos = slut


def main():
    for fil, lista in ANDRINGAR.items():
        p = ROOT / fil
        src = p.read_text(encoding='utf-8')
        for uid, gammal, ny, *alla in lista:
            a, b = omrade(src, uid)
            g, n = json.dumps(gammal, ensure_ascii=False)[1:-1], json.dumps(ny, ensure_ascii=False)[1:-1]
            del_ = src[a:b]
            # 'alla': samma rad står i huvudfacit och i delkortets facit och ändras på båda ställena.
            assert del_.count(g) == 1 or (alla and del_.count(g) >= 1), (fil, uid, del_.count(g), gammal)
            src = src[:a] + del_.replace(g, n) + src[b:]
        for uid, funk in OBJEKT.get(fil, {}).items():
            a, b = omrade(src, uid)
            q = json.loads(src[a:b])
            assert json.dumps(q, ensure_ascii=False, separators=(',', ':')) == src[a:b], uid
            funk(q)
            src = src[:a] + json.dumps(q, ensure_ascii=False, separators=(',', ':')) + src[b:]
        json.loads(src[src.index('['):src.rindex(']') + 1])
        print(fil, len(lista), 'ändringar')
        if '--skriv' in sys.argv:
            with open(p, 'w', encoding='utf-8', newline='') as fh:
                fh.write(src)


if __name__ == '__main__':
    main()
