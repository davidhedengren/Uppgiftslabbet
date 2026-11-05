"""Specifikation och facitbygge för GeoGebra-skärmbilder i Ma2-statistik (5 nov 2026).

Serien 4.328–4.342 har fyra delkort: a) median, b) typvärde, c) medel och Sx,
d) variationsbredd eller kvartilavstånd. Data och mått är kontrollerade mot
GeoGebras egen statistikpanel (se loggfilen som generatorn skriver).

  python tools/geogebra-statistik-serie-2026-11-05.py spec  > spec.json
  python tools/geogebra-statistik-serie-2026-11-05.py bygg <logg.json>
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BANK = ROOT / 'uppgifterma2.js'

# id -> (beskrivning av värdena i rubriken, enhet i svarstext eller '')
# Beskrivningarna är skrivna för hand utifrån varje uppgifts inledning.
SERIE = {
    '4.328': ('de sex kundernas väntetider', 'min'),
    '4.329': ('elevernas antal syskon', ''),
    '4.330': ('bussarnas förseningar', 'min'),
    '4.331': ('antalet pennor i de sex askarna', ''),
    '4.332': ('batteriernas drifttider', 'h'),
    '4.333': ('deltagarnas quizpoäng', ''),
    '4.334': ('de fem plantornas längder', 'cm'),
    '4.335': ('påsarnas vikter', 'g'),
    '4.336': ('medlemmarnas antal träningspass', ''),
    '4.337': ('de tio besökarnas boklån', ''),
    '4.338': ('delarnas avvikelser', 'mm'),
    '4.339': ('löparnas tider', 's'),
    '4.340': ('koppvolymerna', 'ml'),
    '4.341': ('hundarnas åldrar', 'år'),
    '4.342': ('skärmtiderna', 'h'),
}

ALLA = ['n', 'Medel', 'σ', 's', 'Σx', 'Σx²', 'Min', 'Q1', 'Median', 'Q3', 'Max']


def las_bank():
    src = BANK.read_text(encoding='utf-8')
    i, j = src.index('['), src.rindex(']') + 1
    return src, i, j, json.loads(src[i:j])


def slug(uid):
    return uid.replace('.', '-')


def varden(u):
    lista = set()
    for d in u['spelDelar']:
        lista.update(re.findall(r'Skriv värdena (.*?) i kolumn A', d['s']))
    assert len(lista) == 1, (u['id'], lista)
    txt = lista.pop()
    return txt, [float(v.replace(',', '.').replace('−', '-')) for v in txt.split('; ')]


def d_rader(u):
    r = re.search(r'facit-rubrik">Beräkna (variationsbredden|kvartilavståndet)', u['spelDelar'][3]['s']).group(1)
    return ['Min', 'Max'] if r == 'variationsbredden' else ['Q1', 'Q3']


def spec():
    _, _, _, data = las_bank()
    by = {u['id']: u for u in data}
    jobs = []
    for uid in SERIE:
        u = by[uid]
        _, vals = varden(u)
        dr = d_rader(u)
        jobs.append({
            'slug': slug(uid),
            'values': [int(v) if v == int(v) else v for v in vals],
            'stolp': True,
            'stats': [
                {'name': 'median', 'frame': ['Median'], 'show': ['n', 'Median']},
                {'name': 'medel-s', 'frame': ['Medel', 's'], 'show': [r for r in ALLA if r not in dr]},
                {'name': '-'.join(dr).lower(), 'frame': dr},
            ],
        })
    return {'jobs': jobs}


BILD = 'bilder/'


def img(fil, alt, maxw):
    return (f'<span class="fig"><img src="{BILD}{fil}" alt="{alt}" '
            f'style="width:100%;max-width:{maxw}px;height:auto"/></span>')


def sv(x):
    """GeoGebras visning (punkt, bindestreck) -> svensk skrivning."""
    return x.replace('-', '−').replace('.', ',')


def num(x):
    return float(x.replace(',', '.').replace('−', '-'))


def punktnot(*vals):
    v = [x for x in vals if '.' in x]
    if not v:
        return ''
    return (f'<p>GeoGebra skriver decimaltal med punkt: {v[0]} betyder {sv(v[0])}.</p>')


def enh(e):
    return f' {e}' if e else ''


def li(rubrik, *delar):
    return f'<li><p class="facit-rubrik">{rubrik}</p>{"".join(delar)}</li>'


def svarsrad(fac):
    m = re.search(r'<p class="facit-svar">.*?</p>', fac)
    return m.group(0)


def svarstal(fac):
    t = re.sub(r'<[^>]+>', '', svarsrad(fac))
    return [num(x) for x in re.findall(r'−?\d+(?:,\d+)?', t)]


def gg_block(uid, beskr, listtxt, n, vals, med_sigma, skriv=None):
    sl = slug(uid)
    neg = any(v < 0 for v in vals)
    dec = any(v != int(v) for v in vals)
    extra = ''
    if dec:
        extra += ' Decimaltal kan skrivas med komma eller punkt; GeoGebra visar dem med punkt.'
    if neg:
        extra += ' Ett negativt tal skrivs med minustecken före, till exempel -3.'
    steg = [
        li('Öppna kalkylbladet i GeoGebra Classic',
           '<p>Gå till geogebra.org/classic. Klicka på menyknappen ☰ uppe till höger, '
           'välj <strong>Perspektiv</strong> och sedan <strong>Kalkylblad</strong>.</p>',
           img('geogebra-kalkylblad-perspektiv.png',
               'GeoGebra Classic med menyn öppen. Inringat: 1 menyknappen, 2 Perspektiv, 3 Kalkylblad.', 340)),
        li(f'Skriv {beskr} i A1–A{n} och markera dem',
           f'<p>Klicka i cell A1, skriv det första värdet och tryck Enter. Då hamnar du i cellen under. '
           + (skriv or f'Skriv på samma sätt alla värden: {listtxt}.') + f'{extra}</p>'
           f'<p>Dra sedan med musen från A1 till A{n} så att cellerna blir blå.</p>',
           img(f'geogebra-{sl}-data.png',
               f'Kalkylbladet med värdena {listtxt} i A1–A{n}. Cellerna är markerade och stapeldiagramknappen är inringad.', 330)),
        li('Välj Envariabelanalys under stapeldiagramknappen',
           '<p>Klicka på stapeldiagramknappen, den andra knappen i verktygsraden (1), och välj '
           '<strong>Envariabelanalys</strong> (2). Ett analysfönster med ett histogram öppnas.</p>',
           img('geogebra-envariabelanalys-meny.png',
               'Menyn under stapeldiagramknappen med Envariabelanalys inringad.', 420)),
    ]
    if med_sigma:
        steg.append(li('Klicka på Σx för att visa statistiken',
                       '<p>Knappen Σx sitter uppe till höger i analysfönstret. Då visas en tabell med '
                       'statistiska mått till vänster om diagrammet.</p>',
                       img(f'geogebra-{sl}-analys.png',
                           f'Analysfönstret med histogram över {beskr}. Knappen Σx uppe till höger är inringad.', 480)))
    return ''.join(steg)


def bygg_serie(logg):
    src, i, j, data = las_bank()
    by = {u['id']: u for u in data}
    rapport, byten = [], []
    for uid, (beskr, e) in SERIE.items():
        u = by[uid]
        sl = slug(uid)
        st = logg[sl]['stats']
        listtxt, vals = varden(u)
        n = len(vals)
        assert int(st['n']) == n
        dr = d_rader(u)
        delar = u['spelDelar']
        assert [d['etikett'] for d in delar] == ['a', 'b', 'c', 'd']
        orig_main = '<div class="facit-v2 facit-stegvis">' + ''.join(
            '<div class="facit-del"><span class="facit-mark">%s)</span><div class="facit-arbete">%s</div></div>'
            % (d['etikett'], d['s']) for d in delar) + '</div>'
        assert u['s'] == orig_main, uid
        svar = {d['etikett']: svarsrad(d['s']) for d in delar}
        tal = {d['etikett']: svarstal(d['s']) for d in delar}

        # a) median
        med = st['Median']
        assert abs(num(med) - tal['a'][0]) < 1e-9, (uid, med, tal['a'])
        las_a = li('Läs av medianen på raden Median',
                   f'<p>På raden Median står {med}{", alltså " + sv(med) if "." in med else ""}{enh(e)}.</p>',
                   img(f'geogebra-{sl}-median.png', f'Statistikpanelen med raden Median = {med} inringad.', 340))
        # b) typvärde
        from collections import Counter
        c = Counter(vals); top = max(c.values()); modes = [v for v in c if c[v] == top]
        assert len(modes) == 1 and abs(modes[0] - tal['b'][0]) < 1e-9, (uid, modes, tal['b'])
        typ = sv(('%g' % modes[0]))
        las_b = li('Byt till Stolpdiagram och hitta den högsta stapeln',
                   '<p>Klicka på listan där det står Histogram, uppe till vänster i analysfönstret, och välj '
                   '<strong>Stolpdiagram</strong>. Varje stapel visar hur många gånger ett värde förekommer.</p>'
                   f'<p>Den högsta stapeln står vid {typ}{enh(e)}. Det värdet förekommer {top} gånger, '
                   'fler gånger än något annat värde.</p>',
                   img(f'geogebra-{sl}-stolp.png',
                       f'Stolpdiagram över {beskr}. Den högsta stapeln, vid {typ}, är inringad.', 560))
        # c) medel och s
        m, s_ = st['Medel'], st['s']
        assert abs(num(m) - tal['c'][0]) < 1e-9, (uid, m, tal['c'])
        dec = len(re.sub(r'<[^>]+>', '', svar['c']).split('≈')[1].strip().split(' ')[0].split(',')[1].rstrip('.'))
        assert round(num(s_), dec) == round(tal['c'][1], dec), (uid, s_, tal['c'])
        las_c = li('Läs av raderna Medel och s',
                   f'<p>På raden Medel står {m} och på raden s står {s_}.</p>'
                   + punktnot(m, s_) +
                   '<p>Raden s är stickprovsstandardavvikelsen Sx. Raden σ är ett annat mått och används inte här.</p>',
                   img(f'geogebra-{sl}-medel-s.png',
                       f'Statistikpanelen med raderna Medel = {m} och s = {s_} inringade.', 340))
        # d) variationsbredd eller kvartilavstånd
        lo, hi = st[dr[0]], st[dr[1]]
        diff = round(num(hi) - num(lo), 10)
        assert abs(diff - tal['d'][0]) < 1e-9, (uid, lo, hi, tal['d'])
        lo_s, hi_s, diff_s = sv(lo), sv(hi), sv('%g' % diff)
        lo_p = f'({lo_s})' if num(lo) < 0 else lo_s
        if dr == ['Min', 'Max']:
            rub = r'Variationsbredden: \(\text{Max}-\text{Min}\)'
            namn = 'Variationsbredden'
        else:
            rub = r'Kvartilavståndet: \(Q_3-Q_1\)'
            namn = 'Kvartilavståndet'
        las_d = li(rub,
                   f'<p>Läs av raderna {dr[0]} och {dr[1]}: {dr[0]} = {lo} och {dr[1]} = {hi}.</p>'
                   + punktnot(lo, hi) +
                   f'<div class="facit-matte">\\[{hi_s.replace(",", "{,}")}-{lo_p.replace(",", "{,}")}={diff_s.replace(",", "{,}")}\\]</div>'
                   f'<p>{namn} är {diff_s}{enh(e)}.</p>',
                   img(f'geogebra-{sl}-{"-".join(dr).lower()}.png',
                       f'Statistikpanelen med raderna {dr[0]} = {lo} och {dr[1]} = {hi} inringade.', 340))

        def fac(steg):
            return f'<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">{steg}</ol>'
        full = gg_block(uid, beskr, listtxt, n, vals, True)
        utan_sigma = gg_block(uid, beskr, listtxt, n, vals, False)
        nya = {
            'a': fac(full + las_a) + svar['a'] + '</div>',
            'b': fac(utan_sigma + las_b) + svar['b'] + '</div>',
            'c': fac(full + las_c) + svar['c'] + '</div>',
            'd': fac(full + las_d) + svar['d'] + '</div>',
        }
        samma = li('Använd analysfönstret från a)',
                   f'<p>Värdena är redan inskrivna i A1–A{n} och analyserade med Envariabelanalys i a).</p>')
        huvud = {
            'a': nya['a'],
            'b': fac(samma + las_b) + svar['b'] + '</div>',
            'c': fac(samma + las_c) + svar['c'] + '</div>',
            'd': fac(samma + las_d) + svar['d'] + '</div>',
        }
        for d in delar:
            byten.append((d['s'], nya[d['etikett']]))
        byten.append((u['s'], '<div class="facit-v2 facit-stegvis">' + ''.join(
            '<div class="facit-del"><span class="facit-mark">%s)</span><div class="facit-arbete">%s</div></div>'
            % (k, huvud[k]) for k in 'abcd') + '</div>'))
        rapport.append(uid)
    return byt(src, byten), rapport


def byt(src, byten):
    # Byt bara de ändrade strängarna så att bankfilens formatering bevaras.
    for gammal, ny in byten:
        g = json.dumps(gammal, ensure_ascii=False)
        assert src.count(g) == 1, g[:80]
        src = src.replace(g, json.dumps(ny, ensure_ascii=False))
    return src


# Uppgifter med ett facit och ett datamaterial. "behall" = antal inledande steg
# i det gamla facit som är uppgiftens egen matematik och ska stå kvar.
ENKLA = {
    '4.450': dict(vals=[4, 6, 8], beskr='talen 4, 6 och 8', e='', behall=0, rader=['s']),
    '4.452': dict(vals=[6.2, 8.5, 7.1, 9.8, 5.4, 10.3, 7.7], beskr='Majas sju stegtal', e='tusen steg', behall=0, rader=['s'],
                  lista='6,2; 8,5; 7,1; 9,8; 5,4; 10,3; 7,7'),
    '4.453': dict(vals=[38] * 3 + [39] * 4 + [40] * 5 + [41] * 2 + [42], beskr='de 15 skostorlekarna', e='', behall=0, rader=['s'],
                  skriv='Varje medlem är ett värde, så skostorlekarna skrivs så många gånger som tabellen anger: '
                        '38 tre gånger, 39 fyra gånger, 40 fem gånger, 41 två gånger och 42 en gång. Det blir 15 värden.'),
    '4.457': dict(vals=[5, 9, 13], beskr='talen 5, 9 och 13', e='', behall=1, rader=['s']),
    '4.459': dict(vals=[62, 57, 65, 61, 59, 63, 60, 64], beskr='de åtta äggvikterna', e='g', behall=0, rader=['Medel', 's']),
    '6.09': dict(vals=[4, 6, 6, 8], beskr='de fyra väntetiderna', e='min', behall=0, rader=['s']),
    '4.451': dict(vals=[2, 3, 3, 4, 4, 4, 5, 7], beskr='de åtta läxtiderna', e='h', behall=1, rader=['s']),
    '4.455': dict(vals=[0] * 4 + [1] * 6 + [2] * 3 + [3, 4], beskr='målen i de 15 matcherna', e='', behall=1, rader=['s'],
                  skriv='Varje match är ett värde: 0 fyra gånger, 1 sex gånger, 2 tre gånger, 3 en gång och 4 en gång. Det blir 15 värden.'),
    '4.456': dict(vals=[0.4, 0.7, 0.2, 0.8, 0.9, 0.2], beskr='de sex förbättringarna', e='s', behall=1, rader=['s'],
                  lista='0,4; 0,7; 0,2; 0,8; 0,9; 0,2'),
}


def fmt_lista(vals):
    t = ['%g' % v for v in vals]
    return sv(', '.join(t[:-1]) + ' och ' + t[-1]) if len(t) > 1 else sv(t[0])


def spec_enkla():
    jobs = []
    for uid, c in ENKLA.items():
        jobs.append({'slug': slug(uid), 'values': c['vals'],
                     'stats': [{'name': '-'.join(c['rader']).lower().replace('medel', 'medel'), 'frame': c['rader']}]})
    return {'jobs': jobs}


def bygg_enkla(logg, src):
    _, _, _, data = las_bank()
    by = {u['id']: u for u in data}
    byten, rapport = [], []
    for uid, c in ENKLA.items():
        u = by[uid]
        sl = slug(uid)
        st = logg[sl]['stats']
        vals = c['vals']
        n = len(vals)
        assert int(st['n']) == n, uid
        gamla = re.findall(r'<li>.*?</li>', u['s'])
        svar = svarsrad(u['s'])
        # Svarsraden ska stämma med GeoGebras värden avrundade som i svaret.
        tokens = re.findall(r'−?\d+(?:,\d+)?', re.sub(r'<[^>]+>', '', svar))[-len(c['rader']):]
        for r, t in zip(c['rader'], tokens):
            dec = len(t.split(',')[1]) if ',' in t else 0
            assert round(num(st[r]), dec) == num(t), (uid, r, st[r], t)
        listtxt = c.get('lista') or fmt_lista(vals)
        block = gg_block(uid, c['beskr'], listtxt, n, vals, True, skriv=c.get('skriv'))
        v = [st[r] for r in c['rader']]
        if c['rader'] == ['s']:
            rub = 'Läs av raden s, som är Sx'
            las = f'<p>På raden s står {v[0]}.</p>'
        else:
            rub = 'Läs av raderna Medel och s'
            las = f'<p>På raden Medel står {v[0]} och på raden s står {v[1]}.</p>'
        las += punktnot(*v)
        las += '<p>Raden s är stickprovsstandardavvikelsen Sx. Raden σ är ett annat mått och används inte här.</p>'
        alt = ' och '.join(f'{r} = {st[r]}' for r in c['rader'])
        las_li = li(rub, las, img(f'geogebra-{sl}-{"-".join(c["rader"]).lower()}.png',
                                  f'Statistikpanelen för {c["beskr"]} med {alt} inringat.', 340))
        ny = ('<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'
              + ''.join(gamla[:c['behall']]) + block + las_li + '</ol>' + svar + '</div>')
        byten.append((u['s'], ny))
        rapport.append(uid)
    return byt(src, byten), rapport


if __name__ == '__main__':
    if sys.argv[1] == 'spec':
        print(json.dumps(spec(), ensure_ascii=False, indent=1))
    elif sys.argv[1] == 'spec-enkla':
        print(json.dumps(spec_enkla(), ensure_ascii=False, indent=1))
    elif sys.argv[1] == 'bygg-enkla':
        logg = json.loads(Path(sys.argv[2]).read_text(encoding='utf-8'))
        ny, rapport = bygg_enkla(logg, BANK.read_text(encoding='utf-8'))
        if '--skriv' in sys.argv:
            with open(BANK, 'w', encoding='utf-8', newline='') as f:
                f.write(ny)
        print('ok', len(rapport), ' '.join(rapport))
    elif sys.argv[1] == 'bygg':
        logg = json.loads(Path(sys.argv[2]).read_text(encoding='utf-8'))
        ny, rapport = bygg_serie(logg)
        if '--skriv' in sys.argv:
            with open(BANK, 'w', encoding='utf-8', newline='') as f:
                f.write(ny)
        print('ok', len(rapport), ' '.join(rapport))
