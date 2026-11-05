"""Ma2: GeoGebra-skärmbilder i resten av statistikfacit med Envariabelanalys (5 november 2026, steg 2).

Fortsättning på agent/MA2_STATISTIK_GEOGEBRA_STEGBILDER_2026-11-05.md. Samma arbetsgång och bildstil
(tools/geogebra-skarmbilder.js): kalkylblad → skriv in och markera → Envariabelanalys → Σx → läs av.
Bilderna tas här i riktiga GeoGebra Classic på geogebra.org (GGB_WEBB=1). Frekvenstabeller skrivs med
värdena i kolumn A och antalen i kolumn B. Svarsraderna behålls; uppgiftens egna steg (resonemang,
beräkning av x och liknande) behålls där de anges med K(...). Ingen formel för standardavvikelsen.

  python tools/ma2-geogebra-skarmbilder-steg2-2026-11-05.py spec > spec.json
  python tools/ma2-geogebra-skarmbilder-steg2-2026-11-05.py bygg <logg.json> [--skriv]
Logg: agent/MA2_STATISTIK_GEOGEBRA_SKARMBILDER_2026-11-05.md
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BANK = ROOT / 'uppgifterma2.js'
ALLA = ['n', 'Medel', 'σ', 's', 'Σx', 'Σx²', 'Min', 'Q1', 'Median', 'Q3', 'Max']

# ---------------- datamängder ----------------
DS = {}


def D(slug, values, beskr, freq=None, lista=None):
    DS[slug] = dict(values=values, beskr=beskr, freq=freq, lista=lista, crops={}, stolp=False)


def g(x):
    return ('%g' % x).replace('-', '−').replace('.', ',')


def talrad(v):
    t = [g(x) for x in v]
    return t[0] if len(t) == 1 else '; '.join(t)


# ---------------- steg ----------------
class Steg:
    def __init__(self, typ, **k):
        self.typ, self.k = typ, k


def B(ds, rub=None): return Steg('block', ds=ds, sigma=True, rub=rub or {})
def Bn(ds, rub=None): return Steg('block', ds=ds, sigma=False, rub=rub or {})
def A(ds, rub, text=None): return Steg('igen', ds=ds, rub=rub, text=text)
def R(ds, rows, show=None, rub=None, extra=''): return Steg('las', ds=ds, rows=rows, show=show, rub=rub, extra=extra)
def RD(ds, kind, show=None, enh=''): return Steg('diff', ds=ds, kind=kind, show=show, enh=enh)
def ST(ds, enh='', extra=''): return Steg('stolp', ds=ds, enh=enh, extra=extra)
def K(*i): return Steg('behall', i=i)
def Kr(i, rub): return Steg('behall', i=(i,), rub=rub)   # behåll steget men med egen rubrik
def N(rub, html): return Steg('ny', rub=rub, html=html)


T = {}   # id -> {etikett|None: [steg] | 'behall'}


def U(uid, **delar):
    T[uid] = {(None if k == '_' else k): v for k, v in delar.items()}


# ---------------- HTML ----------------
def li(rubrik, *delar):
    return f'<li><p class="facit-rubrik">{rubrik}</p>{"".join(delar)}</li>'


def img(fil, alt, maxw):
    return (f'<span class="fig"><img src="bilder/{fil}" alt="{alt}" loading="lazy" '
            f'style="width:100%;max-width:{maxw}px;height:auto"/></span>')


def sv(x):
    return x.replace('-', '−').replace('.', ',')


def punktnot(*vals):
    v = [x for x in vals if '.' in x]
    return f'<p>GeoGebra skriver decimaltal med punkt: {v[0]} betyder {sv(v[0])}.</p>' if v else ''


def cropnamn(rows, show):
    namn = '-'.join(r.lower().replace('σ', 'sigma').replace('²', '2') for r in rows)
    return namn + ('-dold' + str(len(show)) if show else '')


def registrera(ds, rows, show):
    namn = cropnamn(rows, show)
    DS[ds]['crops'][namn] = {'name': namn, 'frame': rows, **({'show': show} if show else {})}
    return f'geogebra-{ds}-{namn}.png'


PERSPEKTIV = li('Öppna kalkylbladet i GeoGebra Classic',
                '<p>Gå till geogebra.org/classic. Klicka på menyknappen ☰ uppe till höger, välj <strong>Perspektiv</strong> '
                'och sedan <strong>Kalkylblad</strong>.</p>',
                img('geogebra-kalkylblad-perspektiv.png', 'GeoGebra Classic med menyn öppen. Inringat: 1 menyknappen, 2 Perspektiv, 3 Kalkylblad.', 340))
MENY = li('Välj Envariabelanalys under stapeldiagramknappen',
          '<p>Klicka på stapeldiagramknappen, den andra knappen i verktygsraden (1), och välj <strong>Envariabelanalys</strong> (2). '
          'Ett analysfönster med ett histogram öppnas.</p>',
          img('geogebra-envariabelanalys-meny.png', 'Menyn under stapeldiagramknappen med Envariabelanalys inringad.', 420))


def extra_text(v):
    t = ''
    if any(x != int(x) for x in v):
        t += ' Decimaltal kan skrivas med komma eller punkt; GeoGebra visar dem med punkt.'
    if any(x < 0 for x in v):
        t += ' Ett negativt tal skrivs med minustecken före, till exempel -3.'
    return t


def data_steg(ds, rub=None, text=None):
    d = DS[ds]
    v, f, n = d['values'], d['freq'], len(d['values'])
    if f:
        rub = rub or f'Skriv {d["beskr"]} i kolumn A och antalen i kolumn B'
        body = (text or ('<p>Klicka i cell A1, skriv det första värdet och tryck Enter. Då hamnar du i cellen under. '
                         f'Skriv på samma sätt värdena {d["lista"] or talrad(v)} i kolumn A.{extra_text(v)} '
                         f'Skriv sedan i kolumn B hur många gånger varje värde förekommer, på samma rad: {talrad(f)}.</p>')
                + f'<p>Dra med musen från A1 till B{n} så att båda kolumnerna blir blå. När två kolumner är markerade '
                  'räknar GeoGebra talen i kolumn B som antal (frekvenser).</p>')
        alt = f'Kalkylbladet med värdena {talrad(v)} i kolumn A och antalen {talrad(f)} i kolumn B. A1–B{n} är markerade och stapeldiagramknappen är inringad.'
        return li(rub, body, img(f'geogebra-{ds}-data.png', alt, 420))
    rub = rub or f'Skriv {d["beskr"]} i A1–A{n} och markera dem'
    body = (text or ('<p>Klicka i cell A1, skriv det första värdet och tryck Enter. Då hamnar du i cellen under. '
                     f'Skriv på samma sätt alla värden: {d["lista"] or talrad(v)}.{extra_text(v)}</p>')) \
        + f'<p>Dra sedan med musen från A1 till A{n} så att cellerna blir blå.</p>'
    alt = f'Kalkylbladet med värdena {talrad(v)} i A1–A{n}. Cellerna är markerade och stapeldiagramknappen är inringad.'
    return li(rub, body, img(f'geogebra-{ds}-data.png', alt, 330))


def sigma_steg(ds):
    return li('Klicka på Σx för att visa statistiken',
              '<p>Knappen Σx sitter uppe till höger i analysfönstret. Då visas en tabell med statistiska mått till vänster om diagrammet.</p>',
              img(f'geogebra-{ds}-analys.png', f'Analysfönstret med {"diagram" if DS[ds]["freq"] else "histogram"} över {DS[ds]["beskr"]}. Knappen Σx uppe till höger är inringad.', 560))


def las_text(st, rows):
    v = [st[r] for r in rows]
    if len(rows) == 1:
        t = f'<p>På raden {rows[0]} står {v[0]}.</p>'
    else:
        t = '<p>' + ', '.join(f'på raden {r} står {st[r]}' for r in rows[:-1]) + f' och på raden {rows[-1]} står {v[-1]}.</p>'
        t = t[:3] + t[3].upper() + t[4:]
    t += punktnot(*v)
    if 's' in rows:
        t += '<p>Raden s är stickprovsstandardavvikelsen Sx.' + ('' if 'σ' in rows else ' Raden σ är ett annat mått och används inte här.') + '</p>'
    return t


STANDARDRUBRIK = {
    ('s',): 'Läs av raden s, som är Sx', ('Medel', 's'): 'Läs av raderna Medel och s', ('Medel',): 'Läs av medelvärdet på raden Medel',
    ('Median',): 'Läs av medianen på raden Median', ('Q1',): 'Läs av nedre kvartilen på raden Q1', ('Q3',): 'Läs av övre kvartilen på raden Q3',
}


def bygg_steg(steg, logg, gamla, sett, delnamn, main):
    ut = []
    for s in steg:
        k = s.k
        if s.typ == 'block':
            ds = k['ds']
            if main and ds in sett:
                ut.append(li(f'Använd analysen av {DS[ds]["beskr"]} från {sett[ds]})',
                             f'<p>Värdena är redan inskrivna och analyserade med Envariabelanalys i {sett[ds]}).</p>'))
                continue
            if main and delnamn:
                sett.setdefault(ds, delnamn)
            r = k['rub']   # egna rubriker där ett område kräver unika rubriker (lådagram)
            byt = lambda html, ny: html if not ny else re.sub(r'(<p class="facit-rubrik">).*?(</p>)', lambda mm: mm.group(1) + ny + mm.group(2), html, count=1)
            b_ = DS[ds]['beskr']
            ut += [byt(PERSPEKTIV, r.get('p') or f'Öppna ett kalkylblad i GeoGebra för {b_}'), data_steg(ds),
                   byt(MENY, r.get('m') or f'Analysera {b_} med Envariabelanalys')] + \
                ([byt(sigma_steg(ds), r.get('s') or f'Visa statistiken för {b_} med Σx')] if k['sigma'] else [])
        elif s.typ == 'igen':
            ds = k['ds']
            d = DS[ds]
            txt = k['text'] or (f'<p>Ta bort de gamla värdena och skriv {talrad(d["values"])} i kolumn A'
                                + (f' och antalen {talrad(d["freq"])} i kolumn B' if d['freq'] else '') + '.</p>')
            ut.append(li(k['rub'], txt + '<p>Markera de nya cellerna, välj Envariabelanalys och klicka på Σx på samma sätt som ovan.</p>',
                         img(f'geogebra-{ds}-data.png', f'Kalkylbladet med {d["beskr"]} markerade.', 420 if d['freq'] else 330)))
        elif s.typ == 'las':
            ds, rows = k['ds'], k['rows']
            st = logg[ds]['stats']
            fil = registrera(ds, rows, k['show'])
            b_ = DS[ds]['beskr']
            rub = k['rub'] or {('s',): f'Läs av raden s (Sx) för {b_}', ('Medel', 's'): f'Läs av Medel och s för {b_}',
                               ('Medel',): f'Läs av medelvärdet för {b_} på raden Medel', ('Median',): f'Läs av medianen för {b_} på raden Median',
                               ('Q1',): f'Läs av nedre kvartilen för {b_} på raden Q1', ('Q3',): f'Läs av övre kvartilen för {b_} på raden Q3'}.get(tuple(rows)) \
                or ('Läs av raderna ' + ', '.join(rows[:-1]) + ' och ' + rows[-1] + f' för {b_}')
            alt = 'Statistikpanelen med ' + ' och '.join(f'{r} = {st[r]}' for r in rows) + ' inringat.'
            ut.append(li(rub, las_text(st, rows) + k['extra'], img(fil, alt, 340)))
        elif s.typ == 'diff':
            ds = k['ds']
            st = logg[ds]['stats']
            dr = ['Min', 'Max'] if k['kind'] == 'range' else ['Q1', 'Q3']
            fil = registrera(ds, dr, k['show'])
            lo, hi = st[dr[0]], st[dr[1]]
            diff = round(float(hi) - float(lo), 10)
            lo_p = f'({sv(lo)})' if float(lo) < 0 else sv(lo)
            b_ = DS[ds]['beskr']
            rub, namn = ((f'Variationsbredden för {b_}: ' + r'\(\text{Max}-\text{Min}\)', 'Variationsbredden') if dr[0] == 'Min'
                         else (f'Kvartilavståndet för {b_}: ' + r'\(Q_3-Q_1\)', 'Kvartilavståndet'))
            mat = f'{sv(hi)}-{lo_p}={g(diff)}'.replace(',', '{,}')
            ut.append(li(rub, f'<p>Läs av raderna {dr[0]} och {dr[1]}: {dr[0]} = {lo} och {dr[1]} = {hi}.</p>' + punktnot(lo, hi)
                         + f'<div class="facit-matte">\\[{mat}\\]</div><p>{namn} är {g(diff)}{" " + k["enh"] if k["enh"] else ""}.</p>',
                         img(fil, f'Statistikpanelen med raderna {dr[0]} = {lo} och {dr[1]} = {hi} inringade.', 340)))
        elif s.typ == 'stolp':
            ds = k['ds']
            d = DS[ds]
            d['stolp'] = True
            c = Counter()
            for x, n in zip(d['values'], d['freq'] or [1] * len(d['values'])):
                c[x] += n
            top = max(c.values())
            modes = sorted(x for x in c if c[x] == top)
            e = (' ' + k['enh']) if k['enh'] else ''
            if len(modes) == 1:
                txt = f'<p>Den högsta stapeln står vid {g(modes[0])}{e}. Det värdet förekommer {top} gånger, fler gånger än något annat värde.</p>'
            else:
                txt = (f'<p>Staplarna vid {" och ".join(g(m) for m in modes)}{e} är lika höga och högst. Båda värdena förekommer '
                       f'{top} gånger, så det finns två typvärden.</p>')
            ut.append(li(f'Hitta typvärdet för {d["beskr"]} i Stolpdiagram',
                         '<p>Klicka på listan där det står Histogram, uppe till vänster i analysfönstret, och välj <strong>Stolpdiagram</strong>. '
                         'Varje stapel visar hur många gånger ett värde förekommer.</p>' + txt + k['extra'],
                         img(f'geogebra-{ds}-stolp.png', f'Stolpdiagram över {d["beskr"]}. Den högsta stapeln är inringad.', 560)))
        elif s.typ == 'behall':
            for i in k['i']:
                g_ = gamla[i]
                if k.get('rub'):
                    g_ = re.sub(r'(<p class="facit-rubrik">).*?(</p>)', lambda mm: mm.group(1) + k['rub'] + mm.group(2), g_, count=1)
                ut.append(g_)
        elif s.typ == 'ny':
            ut.append(li(k['rub'], k['html']))
    return ''.join(ut)


# ---------------- uppgifterna ----------------
SX = ['n', 'Medel', 'σ', 's', 'Σx', 'Σx²']   # visa bara dessa när senare delar frågar efter Min/Q1/Median/Q3/Max
MED = ['n', 'Median']

D('4-05-1', [8, 10, 12, 14], 'material 1')
D('4-05-2', [9, 10, 11, 12], 'material 2')
U('4.05', a='behall', b=[B('4-05-1'), R('4-05-1', ['s'], rub='Material 1: läs av raden s'),
                       A('4-05-2', 'Material 2: skriv 9, 10, 11 och 12 i A1–A4'), R('4-05-2', ['s'], rub='Material 2: läs av raden s'),
                       N('Minst s betyder minst standardavvikelse', '<p>Material 2 har mindre värde på raden s än material 1.</p>')])

D('4-10-a', [0, 0, 0, 3, 3], 'material A')
D('4-10-b', [0, 0, 1, 1, 4], 'material B')
JMF = N('Samma medelvärde och standardavvikelse, olika median', '<p>Båda materialen har medelvärdet 1,2 och s ≈ 1,64, men medianen är 0 i A och 1 i B.</p>')
U('4.10', _=[B('4-10-a'), R('4-10-a', ['Medel', 's', 'Median'], rub='Material A: läs av Medel, s och Median'),
             A('4-10-b', 'Material B: skriv 0, 0, 1, 1 och 4 i A1–A5'), R('4-10-b', ['Medel', 's', 'Median'], rub='Material B: läs av Medel, s och Median'), JMF])
U('4.175', _=[K(0), B('4-10-a'), R('4-10-a', ['Medel', 's', 'Median'], rub='Material A: läs av Medel, s och Median'),
              A('4-10-b', 'Material B: skriv 0, 0, 1, 1 och 4 i A1–A5'), R('4-10-b', ['Medel', 's', 'Median'], rub='Material B: läs av Medel, s och Median'), JMF])

D('4-11', [6, 8, 9, 9, 11, 17], 'talen')
U('4.11', a=[B('4-11'), R('4-11', ['Medel'], show=['n', 'Medel'])], b=[B('4-11'), R('4-11', ['Median'])])
U('4.28', a=[B('4-11'), R('4-11', ['Medel'], show=['n', 'Medel'])], b=[B('4-11'), R('4-11', ['s'])])

D('4-14-alla', [6, 8, 9, 10, 11, 24], 'de sex prickvärdena')
D('4-14-utan24', [6, 8, 9, 10, 11], 'värdena utan 24')
U('4.14', _=[B('4-14-alla'), R('4-14-alla', ['s'], rub='Läs av raden s för alla sex värden'),
             A('4-14-utan24', 'Ta bort 24 och analysera de fem andra värdena', '<p>Radera 24 i A6 så att 6, 8, 9, 10 och 11 står kvar i A1–A5.</p>'),
             R('4-14-utan24', ['s'], rub='Läs av raden s utan 24'),
             N('Pröva att ta bort de andra värdena', '<p>Tar man bort något av de andra värdena i stället blir s mellan 6,58 och 7,20, alltså större än med alla sex. 24 ligger längst från de andra.</p>')])

D('4-41', [5, 7, 8, 10, 10, 14], 'lästiderna')
U('4.41', a=[B('4-41'), R('4-41', ['Medel'], show=['n', 'Medel'])], b=[B('4-41'), R('4-41', ['Median'])])

D('4-46-a', [12, 16, 18, 21, 23], 'de fem värdena')
D('4-46-b', [12, 16, 18, 21, 23, 18], 'de sex värdena med 18')
U('4.46', a=[B('4-46-a'), R('4-46-a', ['Medel', 's'])],
     b=[A('4-46-b', 'Skriv 18 i A6 och analysera alla sex värdena', '<p>Behåll värdena från a) och skriv 18 i A6.</p>'), R('4-46-b', ['s'])],
     c='behall')

D('4-61', [4, 6, 6, 7, 9, 10, 14], 'de sju talen')
U('4.61', a=[B('4-61'), R('4-61', ['Medel'], show=['n', 'Medel'])], b=[B('4-61'), R('4-61', ['Median'])], c=[Bn('4-61'), ST('4-61')])

D('4-97-x', [2, 5, 8, 11], 'de ursprungliga värdena')
D('4-97-y', [-2, -11, -20, -29], 'de omvandlade värdena')
U('4.97', a=[B('4-97-x'), R('4-97-x', ['Medel', 's'], rub='Före omvandlingen: läs av Medel och s'), K(1),
             A('4-97-y', 'Analysera de omvandlade värdena −2, −11, −20 och −29'), R('4-97-y', ['Medel', 's'], rub='Efter omvandlingen: läs av Medel och s')],
     b='behall')

D('4-157-fore', [7, 9, 10, 10, 14], 'de fem givna värdena')
D('4-157-efter', [7, 9, 10, 10, 14, 10], 'alla sex värdena')
U('4.157', a='behall', b=[B('4-157-fore'), R('4-157-fore', ['s'], rub='Före: läs av raden s för de fem talen'),
                         A('4-157-efter', 'Lägg till det sjätte värdet 10 och analysera igen', '<p>Skriv 10 i A6.</p>'),
                         R('4-157-efter', ['s'], rub='Efter: läs av raden s för de sex talen'),
                         Kr(-1, 'Det sjätte värdet ligger på medelvärdet, så Sx minskar')])

D('4-174-a', [24.3, 24.6, 24.1, 24.5, 24.4, 24.7], 'linjalmätningarna')
D('4-174-b', [24.40, 24.46, 24.43, 24.48, 24.41, 24.45], 'skjutmåttsmätningarna', lista='24,40; 24,46; 24,43; 24,48; 24,41; 24,45')
U('4.174', _=[B('4-174-a'), R('4-174-a', ['s'], rub='Linjalen (A): läs av raden s'),
              A('4-174-b', 'Skjutmåttet (B): skriv de sex mätningarna i A1–A6'), R('4-174-b', ['s'], rub='Skjutmåttet (B): läs av raden s'), K(-1)])

D('4-212-x', [2, 2, 2, 7, 7, 12, 12, 12], 'material X')
D('4-212-y', [2, 6, 7, 7, 7, 7, 8, 12], 'material Y')
U('4.212', _=[K(0, 1), B('4-212-x'), R('4-212-x', ['s'], rub='Kontroll: läs av raden s för X'),
              A('4-212-y', 'Analysera Y på samma sätt', '<p>Prickarna i Y ger 2, 6, 7, 7, 7, 7, 8 och 12. Skriv dem i A1–A8 i stället.</p>'),
              R('4-212-y', ['s'], rub='Läs av raden s för Y')])

D('4-235-fel', [5.2, 5.6, 4.9, 5.8, 55, 5.1, 5.4, 5.0], 'de åtta hoppen med det felskrivna värdet', lista='5,2; 5,6; 4,9; 5,8; 55; 5,1; 5,4; 5,0')
D('4-235-ratt', [5.2, 5.6, 4.9, 5.8, 5.5, 5.1, 5.4, 5.0], 'de rättade hoppen')
U('4.235', _=[B('4-235-fel'), R('4-235-fel', ['s'], rub='Med felet: läs av raden s'),
              A('4-235-ratt', 'Rätta 55 till 5,5 och analysera igen', '<p>Skriv 5,5 i A5 i stället för 55.</p>'),
              R('4-235-ratt', ['s'], rub='Efter rättningen: läs av raden s'), K(-1)])

D('4-241-a', [-2, 0, 0, 0, 2], 'skrivare A:s avvikelser')
D('4-241-b', [-2, -2, 0, 2, 2], 'skrivare B:s avvikelser')
U('4.241',
  a=[B('4-241-a'), R('4-241-a', ['Medel', 'Min', 'Max'], show=['n', 'Medel', 'Min', 'Max'], rub='Skrivare A: läs av Medel, Min och Max'),
     A('4-241-b', 'Skrivare B: skriv −2, −2, 0, 2 och 2 i A1–A5'),
     R('4-241-b', ['Medel', 'Min', 'Max'], show=['n', 'Medel', 'Min', 'Max'], rub='Skrivare B: läs av Medel, Min och Max'), K(-1)],
  b=[B('4-241-a'), R('4-241-a', ['s'], rub='Skrivare A: läs av raden s'), A('4-241-b', 'Skrivare B: skriv −2, −2, 0, 2 och 2 i A1–A5'),
     R('4-241-b', ['s'], rub='Skrivare B: läs av raden s'), K(-1)])

D('4-283', [58, 60, 60, 62, 68, 70, 70, 72], 'alla åtta elevernas poäng')
U('4.283', _=[B('4-283'), R('4-283', ['Medel', 's'])])

D('4-284-0', [44, 48, 48, 52, 52, 52, 52, 52], 'ursprungsmaterialet')
D('4-284-1', [44, 48, 48, 52, 52, 52, 52, 52, 46.79], 'materialet med 46,79')
D('4-284-2', [44, 48, 48, 52, 52, 52, 52, 52, 50], 'materialet med 50')
D('4-284-3', [44, 48, 48, 52, 52, 52, 52, 52, 53.21], 'materialet med 53,21')
U('4.284', _=[B('4-284-0'), R('4-284-0', ['s'], rub='Ursprungsmaterialet: läs av raden s'),
              A('4-284-1', 'Prova 46,79 som nionde värde', '<p>Skriv 46,79 i A9.</p>'), R('4-284-1', ['s'], rub='Med 46,79: läs av raden s'),
              A('4-284-2', 'Prova 50 som nionde värde', '<p>Skriv 50 i A9 i stället.</p>'), R('4-284-2', ['s'], rub='Med 50: läs av raden s'),
              A('4-284-3', 'Prova 53,21 som nionde värde', '<p>Skriv 53,21 i A9 i stället.</p>'), R('4-284-3', ['s'], rub='Med 53,21: läs av raden s'),
              N('Jämför avrundat till två decimaler', '<p>Ursprungsmaterialet och kandidaterna 46,79 och 53,21 ger alla 3,02. Med 50 blir det 2,83.</p>')])

D('4-299-alva', [31.2, 30.8, 31.5, 30.9, 31.1, 31.0], 'Alvas tider', lista='31,2; 30,8; 31,5; 30,9; 31,1; 31,0')
D('4-299-bea', [30.4, 31.9, 30.6, 32.0, 30.5, 31.1], 'Beas tider', lista='30,4; 31,9; 30,6; 32,0; 30,5; 31,1')
D('4-299-bea5', [30.4, 31.9, 30.6, 30.5, 31.1], 'Beas tider utan 32,0 s')
U('4.299',
  a=[B('4-299-alva'), R('4-299-alva', ['Medel'], show=['n', 'Medel'], rub='Alva: läs av raden Medel'),
     A('4-299-bea', 'Bea: skriv hennes sex tider i A1–A6'), R('4-299-bea', ['Medel'], show=['n', 'Medel'], rub='Bea: läs av raden Medel'), K(-1)],
  b=[B('4-299-alva'), R('4-299-alva', ['s'], rub='Alva: läs av raden s'), A('4-299-bea', 'Bea: skriv hennes sex tider i A1–A6'),
     R('4-299-bea', ['s'], rub='Bea: läs av raden s')],
  c='behall',
  d=[B('4-299-bea5'), R('4-299-bea5', ['s'], rub='Beas fem lopp: läs av raden s'), K(-1)])

D('4-302-a', [4, 7, 9, 12], 'de fyra talen')
D('4-302-b', [4, 7, 9, 12, 8], 'de fem talen')
U('4.302', a=[B('4-302-a'), R('4-302-a', ['Medel', 's'])],
     b=[B('4-302-b'), R('4-302-b', ['Medel', 's'], rub='Läs av raderna Medel och s för de fem talen'), K(-1)])

D('4-303', [0, 4, 2, 1, 3, 2, 2, 1, 4, 8], 'skidortens temperaturer')
U('4.303', _=[B('4-303'), R('4-303', ['Medel', 'Min', 'Median', 'Max'], rub='Läs av Min, Max, Median och Medel'),
              N(r'Variationsbredden: \(\text{Max}-\text{Min}\)', r'<div class="facit-matte">\[8-0=8\]</div><p>Medelvärdet 2.7 skrivs 2,7.</p>')])

D('5-41', [7, 8, 8, 9, 9, 10, 10, 10, 11, 11, 12, 12, 13, 14, 14, 16], 'de sexton tiderna')
U('5.41', a=[B('5-41'), R('5-41', ['Median'], show=MED)], b=[B('5-41'), R('5-41', ['Q1'], show=['n', 'Q1', 'Median'])],
     c=[B('5-41'), R('5-41', ['Q3'], show=['n', 'Q1', 'Median', 'Q3'])], d=[B('5-41'), RD('5-41', 'iqr', enh='min')])

D('5-66-a', [12, 13, 13, 14, 14, 15, 15, 16], 'dag A:s tider')
D('5-66-b', [12, 13, 13, 14, 14, 15, 15, 30], 'dag B:s tider')
U('5.66', a=[B('5-66-a'), R('5-66-a', ['Q1', 'Median', 'Q3'], show=['n', 'Min', 'Q1', 'Median', 'Q3', 'Max'], rub='Dag A: läs av Q1, Median och Q3'),
             A('5-66-b', 'Dag B: skriv dag B:s tider i A1–A8'),
             R('5-66-b', ['Q1', 'Median', 'Q3'], show=['n', 'Min', 'Q1', 'Median', 'Q3', 'Max'], rub='Dag B: läs av Q1, Median och Q3'),
             N(r'Kvartilavståndet: \(Q_3-Q_1\)', r'<div class="facit-matte">\[15-13=2\]</div><p>Samma för båda dagarna.</p>')],
     b=[N('Använd analyserna från a)', '<p>Båda dagarnas värden är redan analyserade. Läs nu av raden s.</p>'),
        R('5-66-a', ['s'], rub='Dag A: läs av raden s'), R('5-66-b', ['s'], rub='Dag B: läs av raden s')],
     c='behall')

D('5-71-a', [20.0, 21.0, 22.0, 21.0, 21.0], 'rum A:s temperaturer', lista='20,0; 21,0; 22,0; 21,0; 21,0')
D('5-71-b', [19.0, 21.0, 23.0, 21.0, 21.0], 'rum B:s temperaturer', lista='19,0; 21,0; 23,0; 21,0; 21,0')
U('5.71', _=[B('5-71-a'), R('5-71-a', ['Medel', 's'], rub='Rum A: läs av Medel och s'), A('5-71-b', 'Rum B: skriv dess fem temperaturer i A1–A5'),
             R('5-71-b', ['Medel', 's'], rub='Rum B: läs av Medel och s'), K(-1)])

D('5-94', [20.8, 21.2, 21.0, 21.4, 20.6], 'rumstemperaturerna', lista='20,8; 21,2; 21,0; 21,4; 20,6')
U('5.94', _=[B('5-94'), R('5-94', ['Medel', 's'])])

D('5-110-a', [4, 5, 5, 6, 5], 'grupp A:s svar')
D('5-110-b', [2, 4, 5, 6, 8], 'grupp B:s svar')
U('5.110', _=[B('5-110-a'), R('5-110-a', ['Medel', 's'], rub='Grupp A: läs av Medel och s'), A('5-110-b', 'Grupp B: skriv 2, 4, 5, 6 och 8 i A1–A5'),
              R('5-110-b', ['Medel', 's'], rub='Grupp B: läs av Medel och s'), K(-1)])

D('4-310', [4, 8, 6, 10, 7], 'väntetiderna vid hållplatsen')
U('4.310', _=[B('4-310'), R('4-310', ['Median'])])

D('4-311', [0, 1, 2, 3], 'antalet böcker', freq=[4, 8, 6, 2])
U('4.311', a=[B('4-311'), R('4-311', ['Median'], show=MED)], b=[B('4-311'), R('4-311', ['Medel'])])

D('4-317', [2, 2, 4, 4, 4, 6, 6, 6, 6, 8], 'elevernas väntetider')
U('4.317', _=[B('4-317'), R('4-317', ['Median'])])

D('4-322', [2, 4, 4, 4, 6], 'antalet serieböcker')
D('4-323', [0, 0, 1, 1, 1, 2], 'målen i de sex matcherna')
D('4-324', [-4, -2, 0, -2, 3], 'morgontemperaturerna')
D('4-325', [14, 8, 12, 8, 18], 'verkstadsbesöken')
D('4-326', [36, 37, 38, 39, 40], 'skostorlekarna', freq=[1, 3, 5, 2, 1])
for uid, e in [('4.322', ''), ('4.323', ''), ('4.324', '°C'), ('4.325', ''), ('4.326', '')]:
    s_ = uid.replace('.', '-')
    U(uid, a=[B(s_), R(s_, ['Medel'], show=['n', 'Medel'])], b=[B(s_), R(s_, ['Median'])],
      c=[Bn(s_), ST(s_, e, '<p>Det är fem personer som har skostorlek 38.</p>' if uid == '4.326' else '')])

# Serien 4.343–4.347 (a median, b typvärde, c Medel och s, d variationsbredd eller resonemang)
D('4-343', [19.8, 20, 20, 20.1, 20.4], 'skruvlängderna')
D('4-344', [2, 2, 2, 2, 2], 'paketvikterna')
D('4-345', [1, 2, 3, 4, 5], 'betygen', freq=[1, 2, 1, 2, 1])
D('4-347', [20, 20, 30, 30, 40, 400], 'gåvorna')
for uid, e, d_ in [('4.343', 'mm', 'range'), ('4.344', 'kg', 'range'), ('4.345', '', 'range'), ('4.347', 'kr', None)]:
    s_ = uid.replace('.', '-')
    # 4.347: staplarna vid 20–40 blir bara streck när 400 finns med, så typvärdet läses inte av i stolpdiagrammet där.
    U(uid, a=[B(s_), R(s_, ['Median'], show=MED)], b='behall' if uid == '4.347' else [Bn(s_), ST(s_, e)],
      c=[B(s_), R(s_, ['Medel', 's'], show=SX if d_ else None)] + ([K(-1)] if uid == '4.344' else []),
      d=[B(s_), RD(s_, d_, enh=e)] if d_ else 'behall')

D('4-346-a', [18, 20, 20, 20, 22], 'maskin A:s längder')
D('4-346-b', [16, 20, 20, 20, 24], 'maskin B:s längder')
U('4.346', a=[B('4-346-a'), R('4-346-a', ['Medel', 's'])], b=[B('4-346-b'), R('4-346-b', ['Medel', 's'])],
     c=[B('4-346-a'), R('4-346-a', ['s'], rub='Maskin A: läs av raden s'), A('4-346-b', 'Maskin B: skriv 16, 20, 20, 20 och 24 i A1–A5'),
        R('4-346-b', ['s'], rub='Maskin B: läs av raden s'),
        N('Minst s betyder minst spridning', '<p>Maskin A har mindre värde på raden s än maskin B.</p>')])

D('4-348-a', [2, 4, 4, 6, 9], 'A-värdena')
D('4-348-b', [7, 9, 9, 11, 14], 'B-värdena')
U('4.348', a=[B('4-348-a'), R('4-348-a', ['Medel', 's'], show=SX)], b=[B('4-348-b'), R('4-348-b', ['Medel', 's'], show=SX)], c='behall')

D('4-349-a', [1, 3, 3, 4, 9], 'sträckorna A')
D('4-349-b', [2, 6, 6, 8, 18], 'sträckorna B')
U('4.349', a=[B('4-349-a'), R('4-349-a', ['Medel', 's'])], b=[B('4-349-b'), R('4-349-b', ['Medel', 's'])],
     c=[B('4-349-a'), R('4-349-a', ['s'], rub='A: läs av raden s'), A('4-349-b', 'B: skriv 2, 6, 6, 8 och 18 i A1–A5'),
        R('4-349-b', ['s'], rub='B: läs av raden s'), K(-1)])

D('4-350-a', [0, 1, 2, 3, 4], 'poängen i grupp A', freq=[1, 1, 6, 1, 1])
D('4-350-b', [0, 1, 2, 3, 4], 'poängen i grupp B', freq=[3, 1, 2, 1, 3])
U('4.350', a=[B('4-350-a'), R('4-350-a', ['Medel', 's'])], b=[B('4-350-b'), R('4-350-b', ['Medel', 's'])],
     c=[B('4-350-a'), R('4-350-a', ['s'], rub='Grupp A: läs av raden s'),
        A('4-350-b', 'Grupp B: byt antalen i kolumn B', '<p>Behåll poängen 0–4 i kolumn A och skriv grupp B:s antal 3, 1, 2, 1 och 3 i kolumn B.</p>'),
        R('4-350-b', ['s'], rub='Grupp B: läs av raden s'),
        N('Störst s betyder störst standardavvikelse', '<p>Grupp B har större värde på raden s. Många i B har 0 eller 4 poäng, långt från medelvärdet 2.</p>')])

D('4-351', [10, 20, 30, 40, 50], 'antalet sålda lotter', freq=[2, 3, 1, 1, 1])
U('4.351', a=[B('4-351'), R('4-351', ['Medel', 's'], show=SX)], b=[B('4-351'), R('4-351', ['Median'], show=['n', 'Min', 'Median', 'Max'])],
     c=[Bn('4-351'), ST('4-351')], d=[B('4-351'), RD('4-351', 'iqr')], e='behall')

D('4-360', [2, 4, 7, 10, 14], 'de fem talen')
U('4.360', _=[K(0, 1), B('4-360', {'p': 'Öppna ett kalkylblad i GeoGebra för lådagrammets fem tal', 'm': 'Analysera de fem talen med Envariabelanalys',
                                    's': 'Visa statistiken för de fem talen med Σx'}), R('4-360', ['Medel'])])

D('4-361-a', [0, 2, 4, 6, 8, 10, 12, 14, 16], 'material A')
D('4-361-b', [0, 1, 5, 7, 8, 11, 11, 15, 16], 'material B')
U('4.361', a=[B('4-361-a', {'p': 'Öppna ett kalkylblad i GeoGebra för material A och B', 'm': 'Analysera material A med Envariabelanalys',
                             's': 'Visa statistiken för material A med Σx'}), R('4-361-a', ['Medel'], show=['n', 'Medel'], rub='Material A: läs av raden Medel'),
             A('4-361-b', 'Material B: skriv dess nio värden i A1–A9'), R('4-361-b', ['Medel'], show=['n', 'Medel'], rub='Material B: läs av raden Medel'),
             N('Avrunda till två decimaler', '<p>8 blir 8,00 och 8.2222 blir 8,22.</p>')],
     b='behall')

D('4-362-utan4', [1, 2, 3, 5, 6, 7, 8, 9, 10, 12], 'talen utan 4')
D('4-362-utan5', [1, 2, 3, 4, 6, 7, 8, 9, 10, 12], 'talen utan 5')
# Med tio tal ger GeoGebras Q1 och Q3 medianerna i halvorna med fem tal, alltså uppgiftens konvention.
U('4.362', _=[K(0, 1), B('4-362-utan4', {'p': 'Öppna ett kalkylblad i GeoGebra för talen utan 4', 'm': 'Analysera talen utan 4 med Envariabelanalys',
                                       's': 'Visa statistiken för talen utan 4 med Σx'}),
              R('4-362-utan4', ['Min', 'Q1', 'Median', 'Q3', 'Max'], rub='Utan 4: läs av lådagrammets fem värden'),
              A('4-362-utan5', 'Byt 5 mot 4 och analysera igen', '<p>Skriv 4 i stället för 5 i A4, så att listan blir 1, 2, 3, 4, 6, 7, 8, 9, 10 och 12.</p>'),
              R('4-362-utan5', ['Min', 'Q1', 'Median', 'Q3', 'Max'], rub='Utan 5: läs av lådagrammets fem värden'),
              N('Båda listorna ger samma lådagram', '<p>I båda fallen är Min = 1, Q1 = 3, Median = 6,5, Q3 = 9 och Max = 12, som i figuren. Q1 och Q3 är medianerna i de fem lägsta och de fem högsta talen: deras medianer är 3 respektive 9.</p>')])
D('4-364', [6.5, 7, 7.5, 8, 8.5], 'pH-värdena', freq=[4, 8, 10, 6, 2])
U('4.364', a=[B('4-364'), R('4-364', ['Median'], show=MED)], b=[Bn('4-364'), ST('4-364')],
     c=[B('4-364'), R('4-364', ['Medel', 's'], show=SX)], d=[B('4-364'), RD('4-364', 'iqr')])

D('4-365', [45, 55, 65, 75], 'lådornas mittpunkter', freq=[4, 10, 12, 4])
D('4-366', [2.5, 7.5, 12.5, 17.5], 'väntetidernas mittpunkter', freq=[6, 14, 8, 2])
U('4.365', a=[Kr(0, 'Ersätt lådviktsintervallen med sina mittpunkter'), B('4-365'), R('4-365', ['Medel', 's'])], b='behall')
U('4.366', a=[Kr(0, 'Ersätt väntetidsintervallen med sina mittpunkter'), B('4-366'), R('4-366', ['Medel', 's'], show=SX)], b='behall')

D('4-371-a', [4, 6, 6, 9, 10], 'de fem mätvärdena')
D('4-371-b', [4, 6, 6, 9, 10, 6, 8], 'alla sju värdena')
U('4.371', a=[B('4-371-a'), R('4-371-a', ['Medel', 's'])],
     b=[B('4-371-a'), R('4-371-a', ['s'], rub='Före: läs av raden s'),
        A('4-371-b', 'Lägg till 6 och 8 och analysera igen', '<p>Skriv 6 i A6 och 8 i A7.</p>'), R('4-371-b', ['s'], rub='Efter: läs av raden s'), K(-1)])

D('4-373', [120, 150, 210], 'biljettpriserna', freq=[5, 10, 5])
U('4.373', a=[B('4-373'), R('4-373', ['Medel', 's'], show=SX)], b=[B('4-373'), R('4-373', ['Median'])], c=[Bn('4-373'), ST('4-373', 'kr')])

D('4-384-a', [9, 10, 10, 10, 10, 10, 10, 11], 'diagram A:s värden')
D('4-384-b', [7, 8, 9, 10, 10, 11, 12, 13], 'diagram B:s värden')
D('4-384-c', [4, 5, 8, 10, 10, 12, 15, 16], 'diagram C:s värden')
U('4.384', _=[K(0), B('4-384-a'), R('4-384-a', ['s'], rub='Diagram A: läs av raden s'),
              A('4-384-b', 'Diagram B: skriv 7, 8, 9, 10, 10, 11, 12 och 13 i A1–A8'), R('4-384-b', ['s'], rub='Diagram B: läs av raden s'),
              A('4-384-c', 'Diagram C: skriv 4, 5, 8, 10, 10, 12, 15 och 16 i A1–A8'), R('4-384-c', ['s'], rub='Diagram C: läs av raden s')])

D('4-385', [22, 25, 27, 28, 29, 30, 30, 31, 32, 33, 35, 38], 'de tolv provresultaten')
U('4.385', _=[K(0), B('4-385'), R('4-385', ['s'], rub='Kontrollera uppskattningen: läs av raden s')])

D('4-386-8', [12, 13, 14, 14, 15, 15, 16, 17], 'de åtta blå värdena')
D('4-386-9', [12, 13, 14, 14, 15, 15, 16, 17, 31], 'alla nio värdena')
U('4.386', _=[B('4-386-8'), R('4-386-8', ['Medel', 's'], rub='Före tillägget: läs av Medel och s'),
              A('4-386-9', 'Lägg till den röda pricken 31 och analysera igen', '<p>Skriv 31 i A9.</p>'),
              R('4-386-9', ['Medel', 's'], rub='Efter tillägget: läs av Medel och s'),
              N('Ett värde långt från de andra ökar spridningen kraftigt', '<p>Medelvärdet ökar från 14,5 till ungefär 16,33, och s ökar från ungefär 1,60 till ungefär 5,70.</p>')])

D('4-387-p', [40, 45, 50, 55, 60], 'mittpunkterna i P', freq=[4, 10, 22, 10, 4])
D('4-387-q', [25, 35, 45, 55, 65, 75], 'mittpunkterna i Q', freq=[6, 8, 9, 9, 8, 6])
U('4.387', _=[K(0), B('4-387-p'), R('4-387-p', ['s'], rub='Histogram P: läs av raden s'),
              A('4-387-q', 'Histogram Q: skriv mittpunkterna och antalen', '<p>Skriv 25, 35, 45, 55, 65 och 75 i kolumn A och antalen 6, 8, 9, 9, 8 och 6 i kolumn B.</p>'),
              R('4-387-q', ['s'], rub='Histogram Q: läs av raden s'), K(-1)])

D('4-388', [7, 7, 7, 7, 7, 7], 'sömntiderna')
U('4.388', _=[K(0), B('4-388'), R('4-388', ['s'], rub='Kontrollera: läs av raden s')])

D('4-389-7', [11, 13, 14, 15, 16, 17, 19], 'de sju blå värdena')
D('4-389-8', [11, 13, 14, 15, 16, 17, 19, 15], 'alla åtta värdena')
U('4.389', _=[B('4-389-7'), R('4-389-7', ['Medel', 's'], rub='De sju blå värdena: läs av Medel och s'),
              A('4-389-8', 'Lägg till den röda pricken 15 och analysera igen', '<p>Skriv 15 i A8.</p>'),
              R('4-389-8', ['Medel', 's'], rub='Alla åtta värdena: läs av Medel och s'),
              Kr(-1, 'Den röda pricken ligger på medelvärdet 15, så Sx minskar lite')])

D('4-390-a', [14, 16, 15, 17, 18, 16, 15, 17, 16, 16], 'stad A:s temperaturer')
D('4-390-b', [9, 14, 20, 12, 22, 18, 11, 21, 17, 16], 'stad B:s temperaturer')
U('4.390', _=[B('4-390-a'), R('4-390-a', ['s'], rub='Stad A: läs av raden s'), A('4-390-b', 'Stad B: skriv de tio temperaturerna i A1–A10'),
              R('4-390-b', ['s'], rub='Stad B: läs av raden s')])

D('4-391', [48, 52, 55, 57, 58, 60, 61, 62, 63, 65, 70, 75], 'pulsvärdena')
U('4.391', _=[B('4-391'), R('4-391', ['Medel', 's']), K(1, 2)])

D('4-392-a', [72, 75, 70, 79, 68, 74, 81, 69], 'spelare A:s slag')
D('4-392-b', [75, 76, 74, 77, 75, 76, 74, 77], 'spelare B:s slag')
U('4.392', _=[B('4-392-a'), R('4-392-a', ['s'], rub='Spelare A: läs av raden s'), A('4-392-b', 'Spelare B: skriv de åtta rundorna i A1–A8'),
              R('4-392-b', ['s'], rub='Spelare B: läs av raden s'), K(-1)])

D('4-393', [498.2, 501.5, 503.1, 497.4, 500.8, 495.9, 502.6, 499.0, 504.2, 497.3], 'kaffepaketens vikter',
  lista='498,2; 501,5; 503,1; 497,4; 500,8; 495,9; 502,6; 499,0; 504,2; 497,3')
U('4.393', _=[B('4-393'), R('4-393', ['s']), K(-1)])

D('4-454-ali', [9, 8, 10, 9, 7, 9], 'Alis poäng')
D('4-454-bo', [10, 6, 10, 9, 7, 10], 'Bos poäng')
U('4.454', _=[B('4-454-ali'), R('4-454-ali', ['s'], rub='Ali: läs av raden s'), A('4-454-bo', 'Bo: skriv hans sex poäng i A1–A6'),
              R('4-454-bo', ['s'], rub='Bo: läs av raden s'), K(-1)])

D('4-458-8', [2, 4, 8], 'talen 2, 4 och 8')
D('4-458-971', [2, 4, 9.71], 'talen 2, 4 och 9,71')
D('4-458-11', [2, 4, 11], 'talen 2, 4 och 11')
U('4.458', _=[B('4-458-8'), R('4-458-8', ['s'], rub='Med x = 8: läs av raden s'),
              A('4-458-971', 'Prova x = 9,71', '<p>Skriv 9,71 i A3 i stället.</p>'), R('4-458-971', ['s'], rub='Med x = 9,71: läs av raden s'),
              A('4-458-11', 'Prova x = 11', '<p>Skriv 11 i A3 i stället.</p>'), R('4-458-11', ['s'], rub='Med x = 11: läs av raden s'),
              N('Vilket förslag ger ungefär 4?', '<p>Bara 9,71 ger s = 4,00 avrundat till två decimaler.</p>')])

D('4-461-a', [1, 5, 5, 5, 9], 'A-materialet')
D('4-461-b', [1, 1, 5, 9, 9], 'B-materialet')
U('4.461', _=[B('4-461-a'), R('4-461-a', ['s'], rub='Material A: läs av raden s'), A('4-461-b', 'Material B: skriv 1, 1, 5, 9 och 9 i A1–A5'),
              R('4-461-b', ['s'], rub='Material B: läs av raden s'), K(-1)])

D('4-463', [2, 4, 6, 8], 'talen 2, 4, 6 och 8')
U('4.463', _=[B('4-463'), R('4-463', ['σ', 's'], rub='Jämför raderna σ och s',
                              extra='<p>Raden s visar Sx: 2.582, alltså 2,58. Lisa läste av raden σ (2.2361, alltså 2,24), som är ett annat mått.</p>')])

D('4-2015', [0, 1, 2, 3, 4], 'fotbollslagets mål', freq=[3, 5, 6, 4, 2])
D('4-2016', [0, 1, 2, 3, 4], 'innebandylagets mål', freq=[3, 5, 6, 4, 2])
U('4.2015', _=[Bn('4-2015'), ST('4-2015', 'mål')])
U('4.2016', _=[B('4-2016'), R('4-2016', ['Medel'])])

# 4.343–4.347 fick skärmbilder i steg 1 (commit 64658e2, geogebra-statistik-serie2-2026-11-05.py) och lämnas orörda här.
for _uid in ['4.343', '4.344', '4.345', '4.346', '4.347']:
    T.pop(_uid)
for _ds in ['4-343', '4-344', '4-345', '4-347', '4-346-a', '4-346-b']:
    DS.pop(_ds)


# ---------------- bank ----------------
def las_bank():
    src = BANK.read_text(encoding='utf-8')
    i, j = src.index('['), src.rindex(']') + 1
    return src, json.loads(src[i:j])


def delblock(s):
    start = '<div class="facit-v2 facit-stegvis">'
    kropp = s[len(start):-len('</div>')]
    ut = []
    for b in re.split(r'(?=<div class="facit-del"><span class="facit-mark">)', kropp):
        if not b:
            continue
        m = re.match(r'<div class="facit-del"><span class="facit-mark">([a-z])\)</span><div class="facit-arbete">(.*)</div></div>$', b, re.S)
        assert m, b[:100]
        ut.append((m.group(1), m.group(2)))
    return ut


def montera(par):
    return '<div class="facit-v2 facit-stegvis">' + ''.join(
        f'<div class="facit-del"><span class="facit-mark">{m})</span><div class="facit-arbete">{inner}</div></div>' for m, inner in par) + '</div>'


def svarsrad(fac):
    return ''.join(re.findall(r'<p class="facit-svar">.*?</p>', fac, re.S))


def steglista(fac):
    return re.findall(r'<li>.*?</li>', fac, re.S)


def lista(steg, svar):
    return f'<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">{steg}</ol>{svar}</div>'


def bygg(logg):
    src, data = las_bank()
    by = {u['id']: u for u in data}
    byten = []
    bara = [a for a in sys.argv if re.fullmatch(r'\d+\.\d+', a)]   # t.ex. "bygg logg.json 4.362 --skriv"
    for uid, delar in T.items():
        if bara and uid not in bara:
            continue
        u = by[uid]
        harDel = bool(u.get('spelDelar'))
        if None in delar:                     # ett enda facit
            ny = lista(bygg_steg(delar[None], logg, steglista(u['s']), {}, None, True), svarsrad(u['s']))
            byten.append((u['s'], ny))
            continue
        if 'facit-del' not in u['s']:
            # Huvudfacit utan delmarkeringar (4.11, 4.28, 4.41, 4.61, 5.41) förblir en sammanhängande lista:
            # en gemensam inmatning och analys, därefter avläsningarna för varje del och den gamla svarsraden.
            sett, steg_html = {}, ''
            for d in u['spelDelar']:
                st = delar.get(d['etikett'], 'behall')
                assert st != 'behall', uid
                steg_html += bygg_steg(st, logg, steglista(d['s']), sett, d['etikett'], True)
            steg_html = re.sub(r'<li><p class="facit-rubrik">Använd analysen av [^<]* från [a-z]\)</p>.*?</li>', '', steg_html, flags=re.S)
            byten.append((u['s'], lista(steg_html, svarsrad(u['s']))))
            for d in u['spelDelar']:
                byten.append((d['s'], lista(bygg_steg(delar[d['etikett']], logg, steglista(d['s']), {}, d['etikett'], False), svarsrad(d['s']))))
            continue
        main_par = delblock(u['s'])
        sett, nya_main = {}, []
        for m, inner in main_par:
            if delar.get(m, 'behall') == 'behall':
                nya_main.append((m, inner))
                continue
            nya_main.append((m, lista(bygg_steg(delar[m], logg, steglista(inner), sett, m, True), svarsrad(inner))))
        byten.append((u['s'], montera(nya_main)))
        if harDel:
            for d in u['spelDelar']:
                st = delar.get(d['etikett'], 'behall')
                if st == 'behall':
                    continue
                byten.append((d['s'], lista(bygg_steg(st, logg, steglista(d['s']), {}, d['etikett'], False), svarsrad(d['s']))))
    for gammal, ny in byten:
        gj = json.dumps(gammal, ensure_ascii=False)
        assert src.count(gj) == 1, (src.count(gj), gammal[:100])
        src = src.replace(gj, json.dumps(ny, ensure_ascii=False))
    return src, byten


def spec(logg_fake=True):
    # Kör en torrbyggnad med påhittade panelvärden för att registrera alla bildutsnitt.
    falsk = {s: {'stats': {k: '1' for k in ALLA}} for s in DS}
    bygg(falsk)
    jobs = []
    for s, d in DS.items():
        j = {'slug': s, 'values': d['values'], 'stats': list(d['crops'].values())}
        if d['freq']:
            j['freq'] = d['freq']
        if d['stolp']:
            j['stolp'] = True
        jobs.append(j)
    return {'jobs': jobs}


if __name__ == '__main__':
    if sys.argv[1] == 'spec':
        print(json.dumps(spec(), ensure_ascii=False, indent=1))
    elif sys.argv[1] == 'bygg':
        logg = json.loads(Path(sys.argv[2]).read_text(encoding='utf-8'))
        ny, byten = bygg(logg)
        print('ok', len(T), 'uppgifter,', len(byten), 'facit')
        if '--skriv' in sys.argv:
            with open(BANK, 'w', encoding='utf-8', newline='') as f:
                f.write(ny)
            print('skrivet')
