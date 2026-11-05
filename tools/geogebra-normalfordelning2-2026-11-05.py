"""Omgång 2: Sannolikhetskalkylatorns skärmbilder i resterande Ma2-normalfördelningsfacit (5 nov 2026).

* INFOGA: facit med bra befintliga steg. Texten behålls; ett öppningssteg och en inringad bild
  av varje beräkning läggs in i det steg där facit nämner GeoGebras värde.
* SKRIV_OM: tunna facit utan rubriker skrivs om enligt FACITMALL, som i piloten.

  python tools/geogebra-normalfordelning2-2026-11-05.py spec > spec.json
  python tools/geogebra-normalfordelning2-2026-11-05.py bygg <logg.json> [--skriv]
"""
import importlib.util
import json
import re
import sys
from pathlib import Path
from statistics import NormalDist

sys.dont_write_bytecode = True  # skapa ingen __pycache__ i tools/
_s = importlib.util.spec_from_file_location('nf1', Path(__file__).with_name('geogebra-normalfordelning-2026-11-05.py'))
nf1 = importlib.util.module_from_spec(_s)
_s.loader.exec_module(nf1)
sv, g, tex, img, li, facit = nf1.sv, nf1.g, nf1.tex, nf1.img, nf1.li, nf1.facit
BANK = nf1.BANK
MODE = {'vanster': 'Öppet åt vänster', 'intervall': 'Intervall', 'hoger': 'Öppet åt höger'}

# Beräkning: (slug, mu, sigma, läge, a, b, p, sök, kontroll)
#   sök = text i facit-HTML i det steg där bilden ska stå (oftast GeoGebras värde som facit anger)
#   kontroll = (värde, decimaler) som GeoGebras svar avrundat ska ge, eller None
C = lambda *x: x
INFOGA = {
    '4.07': ('plommonens vikt', [C('4-07', 0, 1, 'vanster', None, None, 0.977, 'visas cirka 1,9954', (1.9954, 4))]),
    '4.08': ('testresultaten', [C('4-08-a', 100, 15, 'vanster', None, None, 0.023, 'Skriv 0,023', (70.07, 2)),
                                C('4-08-b', 100, 15, 'vanster', None, None, 0.977, 'Ändra till 0,977', (129.93, 2))]),
    '4.13': ('sluttiderna i terrängloppet', [C('4-13', 50, 1, 'vanster', None, None, 0.90, 'Gränsen blir cirka 51,2816', (51.2816, 4))]),
    '4.19': ('400-meterstiderna', [C('4-19', 0, 1, 'vanster', None, None, 0.841, 'visas cirka 0,9986', (0.9986, 4))]),
    '4.26': ('gösarnas längd', [C('4-26', 49.5, 7, 'hoger', 61, None, None, 'cirka 0,0502', (0.0502, 4))]),
    '4.27': ('produktens vikt', [C('4-27-a', 84, 1, 'hoger', None, None, 0.023, 'Gränsen blir cirka 85,995', (85.995, 3)),
                                 C('4-27-b', 84, 3, 'hoger', 90, None, None, 'cirka 0,0228', (0.0228, 4))]),
    '4.37': ('kanelbullarnas vikt', [C('4-37', 0, 1, 'vanster', None, None, 0.9985, 'visas cirka 2,9677', (2.9677, 4))]),
    '4.38': ('makrillarnas längd', [C('4-38-a', 40, 5, 'vanster', None, None, 0.023, 'visas cirka 30,02', (30.02, 2)),
                                    C('4-38-b', 40, 5, 'vanster', None, None, 0.977, 'visas cirka 49,98', (49.98, 2))]),
    '4.45': ('provresultaten i GeoGebra', [C('4-45-a', 70.6, 12, 'vanster', None, None, 0.90, 'ungefär 86,0', (86.0, 1)),
                                           C('4-45-b', 70.6, 12, 'intervall', 65, 86, None, 'ungefär 0,580', (0.580, 3))]),
    '4.51': ('åldrarna i gruppen', [C('4-51', 0, 1, 'vanster', None, None, 0.977, 'visas cirka 1,9954', (1.9954, 4))]),
    '4.53': ('antalet situps', [C('4-53', 50, 9.4, 'vanster', None, None, 0.90, 'ungefär 62,0', (62.0, 1))]),
    '4.57': ('resultaten på skolans test', [C('4-57-a', 72, 8, 'vanster', None, None, 0.08, 'ungefär 60,8', (60.8, 1)),
                                            C('4-57-b', 72, 8, 'vanster', None, None, 0.88, 'ungefär 81,4', (81.4, 1))]),
    '4.69': ('antalet resenärer', [C('4-69', 0, 1, 'vanster', None, None, 0.841, 'visas cirka 0,9986', (0.9986, 4))]),
    '4.70': ('resultaten bland de 10 % bästa', [C('4-70', 64, 9, 'vanster', None, None, 0.90, 'ungefär 75,5', (75.5, 1))]),
    '4.87': ('detaljernas längd', [C('4-87-a1', 50, 1.8, 'vanster', None, 47, None, 'cirka 0,0956', None),
                                   C('4-87-a2', 50, 1.8, 'hoger', 53, None, None, 'cirka 0,0956', None),
                                   C('4-87-b', 50, 1.8, 'vanster', None, None, 0.05, 'Bestäm gränsen med 5 % till vänster', (47.04, 2)),
                                   C('4-87-c', 50, 1.8, 'hoger', None, None, 0.05, 'Bestäm gränsen med 5 % till höger', (52.96, 2))]),
    '4.95': ('batteriernas körtid', [C('4-95-a', 75, 12.5, 'vanster', None, None, 0.10, 'ungefär 59,0', (59.0, 1)),
                                     C('4-95-b', 75, 12.5, 'vanster', None, None, 0.90, 'ungefär 91,0', (91.0, 1))]),
    '4.104': ('provresultatet', [C('4-104', 0, 12, 'vanster', None, None, 0.80, 'Gränsen blir cirka 10,10', (10.10, 2))]),
    '4.116': ('matematikprovets poäng', [C('4-116-a', 52, 9.4, 'vanster', None, None, 0.10, 'ungefär 40,0', (40.0, 1)),
                                         C('4-116-b', 52, 9.4, 'vanster', None, None, 0.90, 'ungefär 64,0', (64.0, 1))]),
    '4.117': ('monteringstiden', [C('4-117-a', 70, 8, 'vanster', None, None, 0.10, 'ungefär 59,7', (59.7, 1)),
                                  C('4-117-b', 70, 8, 'vanster', None, None, 0.90, 'ungefär 80,3', (80.3, 1))]),
    '4.153': ('provets resultat', [C('4-153-a', 54, 9.4, 'vanster', None, None, 0.10, 'Skriv 0,10', (42.0, 1)),
                                   C('4-153-b', 54, 9.4, 'vanster', None, None, 0.90, 'Ändra sannolikheten till 0,90', (66.0, 1))]),
    '4.176': ('julitemperaturen', [C('4-176-a', 30, 4, 'vanster', None, None, 0.023, 'visas cirka 22,02', (22.02, 2)),
                                   C('4-176-b', 30, 4, 'vanster', None, None, 0.977, 'visas cirka 37,98', (37.98, 2))]),
    '4.177': ('sluttiderna i motionsloppet', [C('4-177-a', 70, 6, 'vanster', None, None, 0.16, 'visas cirka 64,03', (64.03, 2)),
                                              C('4-177-b', 70, 6, 'vanster', None, None, 0.84, 'visas cirka 75,97', (75.97, 2))]),
    '4.178': ('skolornas provresultat', [C('4-178-a', 80, 10, 'hoger', 95, None, None, 'cirka 0,0668', (0.0668, 4)),
                                         C('4-178-b', 76, 14, 'hoger', None, None, 0.0668, 'ungefär 97,0', (97.0, 1))]),
    '4.216': ('påsarna med nötmix', [C('4-216-a', 100, 10, 'vanster', None, None, 0.023, 'visas cirka 80,05', (80.05, 2)),
                                     C('4-216-b', 100, 10, 'vanster', None, None, 0.977, 'visas cirka 119,95', (119.95, 2))]),
    '4.218': ('tackornas vikt', [C('4-218', 60, 8, 'vanster', None, None, 0.90, 'ungefär 70,3', (70.3, 1))]),
    '4.231': ('äggen från hönseriet', [C('4-231-a', 60, 7, 'vanster', None, None, 0.159, 'visas cirka 53,01', (53.01, 2)),
                                       C('4-231-b', 60, 7, 'vanster', None, None, 0.841, 'visas cirka 66,99', (66.99, 2))]),
    '4.260': ('äpplena i partiet', [C('4-260', 160, 1, 'vanster', None, None, 0.84, 'Gränsen blir cirka 160,9945', (160.9945, 4))]),
    '4.261': ('godispåsarnas vikt', [C('4-261', 0, 1, 'vanster', None, None, 0.023, 'visas cirka −1,9954', (-1.9954, 4))]),
    '4.263': ('paketen i lagret', [C('4-263-a', 0, 1, 'vanster', None, None, 0.8413, 'vänsterarea 0,8413', (1.00, 2)),
                                   C('4-263-b', 0, 1, 'vanster', None, None, 0.0227, 'för 0,0227', (-2.00, 2))]),
    '4.285': ('mjölpåsarna efter omställningen', [C('4-285', 0, 1, 'vanster', None, None, 0.0013, 'visas cirka −3,0115', (-3.0115, 4))]),
    '4.287': ('kaffepaketen på linjen', [C('4-287-a', 0, 1, 'vanster', None, None, 0.05, 'Sannolikheten 0,05', (-1.6449, 4)),
                                         C('4-287-b', 0, 1, 'vanster', None, None, 0.99, '0,99 ger', (2.3263, 4))]),
    '4.304': ('de anställdas åldrar', [C('4-304', 0, 1, 'vanster', None, None, 0.977, 'visas cirka 1,9954', (1.9954, 4))]),
    '4.2043': ('männens längd i regionen', [C('4-2043-a', 179, 7, 'vanster', None, None, 0.025, 'Skriv 0,025', (165.28, 2)),
                                            C('4-2043-b', 179, 7, 'vanster', None, None, 0.975, 'Ändra till 0,975', (192.72, 2))]),
    '4.2045': ('skruvarna vid kontrollen', [C('4-2045', 0, 1, 'vanster', None, None, 0.841, 'visas cirka 0,9986', (0.9986, 4))]),
    '4.2046': ('testets resultat', [C('4-2046', 72, 1, 'vanster', None, None, 0.022, 'Gränsen blir cirka 69,986', (69.986, 3))]),
    '4.2049': ('reaktionstiden i testet', [C('4-2049', 0.25, 0.04, 'vanster', None, None, 0.977, 'visas cirka 0,3298', (0.3298, 4))]),
    '4.2051': ('mjölpåsarna på 1 000 g', [C('4-2051', 0, 1, 'vanster', None, None, 0.022, 'visas cirka −2,0141', (-2.0141, 4))]),
    '4.2093': ('kaffepaketen från maskinen', [C('4-2093', 0, 1, 'vanster', None, None, 0.02, 'ungefär −2,0537', (-2.0537, 4))]),
    '4.2094': ('bussresornas restid', [C('4-2094', 0, 1, 'vanster', None, None, 0.90, 'ungefär 1,2816', (1.2816, 4))]),
    '4.2120': ('18-åriga mäns längd', [C('4-2120', 180, 7, 'hoger', 190, None, None, 'cirka 0,0766', (0.0766, 4))]),
    '4.2123': ('reaktionstiden i simulatorn', [C('4-2123', 420, 60, 'vanster', None, None, 0.85, 'cirka 482,2', (482.2, 1))]),
    '4.2125': ('förpackningarnas vikt', [C('4-2125', 500, 8, 'vanster', None, None, 0.05, 'cirka 486,8', (486.8, 1))]),
    '4.2126': ('flaskornas innehåll', [C('4-2126', 0, 1, 'vanster', None, None, 0.01, 'ungefär −2,3263', (-2.3263, 4))]),
    '4.2127': ('ett normalfördelat material', [C('4-2127', 0, 1, 'hoger', 1.5, None, None, 'GeoGebra visar cirka 0,0668', (0.0668, 4))]),
}

# Tunna facit som skrivs om: (namn, enhet, beräkning, rubrik för avläsningen, extra steg/rader, svarstext, kontroll)
SKRIV_OM = {
    '4.523': ('limpornas vikt', 'g', ('4-523', 800, 15, 'hoger', 820, None), 'Läs av andelen limpor över 820 g', 'proc', 'Cirka 9,1 %.', 0.0912),
    '4.526': ('juiceförpackningarnas innehåll', 'ml', ('4-526', 1000, 8, 'intervall', 990, 1010), 'Läs av andelen mellan 990 ml och 1010 ml', 'proc', 'Cirka 78,9 %.', 0.7887),
    '4.530': ('pendlarens restid', 'min', ('4-530', 25, 4, 'hoger', 32, None), 'Läs av sannolikheten för mer än 32 minuter', 'proc', 'Cirka 4,0 %.', 0.0401),
    '4.2087': ('lampornas livslängd', 'timmar', ('4-2087', 8000, 600, 'hoger', 9000, None), 'Läs av andelen lampor över 9 000 timmar', 'proc', 'Cirka 4,8 %.', 0.0478),
    '4.2088': ('cykelresornas tid', 'min', ('4-2088', 23, 2.5, 'vanster', None, 19), 'Läs av andelen resor under 19 min', 'proc', 'Cirka 5,5 %.', 0.0548),
    '4.2089': ('äggen som sorteras', 'g', ('4-2089', 62, 5, 'intervall', 63, 73), 'Läs av andelen ägg i storlek L', 'antal:2500:1017', 'Ungefär 1017 ägg.', 0.4068),
    '4.2091': ('skruvarna från maskinen', 'mm', ('4-2091', 40, 0.3, 'intervall', 39.5, 40.5), 'Läs av andelen godkända skruvar', 'komplement', 'Cirka 9,6 %.', 0.9044),
    '4.2095': ('provpoängen för 240 elever', 'poäng', ('4-2095', 65, 10, 'hoger', 80, None), 'Läs av andelen över 80 poäng', 'antal:240:16', 'Ungefär 16 elever.', 0.0668),
    '4.110': ('potatisarnas vikt', 'g', ('4-110', 120, 15, 'intervall', 105, 135), 'Läs av andelen mellanstora potatisar', 'proc', 'Andelen är cirka 0,683, alltså 68,3 %.', 0.6827),
    '4.217': ('musslornas längd', 'mm', ('4-217', 50, 5, 'vanster', None, 55), 'Läs av sannolikheten att musslan är kortare än 55 mm', 'proc', 'Sannolikheten är cirka 84,1 %.', 0.8413),
}
# 4.58 räknas baklänges: sannolikheten 0,90 till vänster ger viktgränsen.
INV_58 = ('4-58', 500, 20, 'vanster', None, None, 0.90)


def alla_berakningar():
    for uid, (namn, calcs) in INFOGA.items():
        for c in calcs:
            yield c[:7]
    for uid, v in SKRIV_OM.items():
        sl, mu, sigma, mode, a, b = v[2]
        yield (sl, mu, sigma, mode, a, b, None)
    yield INV_58


def forvantat(mu, sigma, mode, a, b, p):
    n = NormalDist(mu, sigma)
    if p is not None:
        return n.inv_cdf(p) if mode == 'vanster' else n.inv_cdf(1 - p)
    return nf1.sannolikhet(mu, sigma, mode, a, b)


def spec():
    jobs = []
    for sl, mu, sigma, mode, a, b, p in alla_berakningar():
        j = {'slug': sl, 'typ': 'normal', 'mu': mu, 'sigma': sigma, 'mode': mode, 'expect': round(forvantat(mu, sigma, mode, a, b, p), 4)}
        for k, v in (('a', a), ('b', b), ('p', p)):
            if v is not None:
                j[k] = v
        jobs.append(j)
    return {'jobs': jobs}


def bildtext(logg, sl, mu, sigma, mode, a, b, p):
    v = logg[sl]['visat']
    if p is not None:
        ind = f'4 sannolikheten {sv(g(p))} efter likhetstecknet'
        ut = f'5 svaret (gränsen blir {v})'
    elif mode == 'intervall':
        ind = f'4 gränserna {sv(g(a))} och {sv(g(b))}'
        ut = f'5 svaret {v}'
    else:
        ind = f'4 gränsen {sv(g(a if mode == "hoger" else b))}'
        ut = f'5 svaret {v}'
    txt = (f'<p>Så ser det ut i GeoGebra: 1 μ = {sv(g(mu))}, 2 σ = {sv(g(sigma))}, 3 knappen '
           f'<strong>{MODE[mode]}</strong>, {ind} och {ut}. GeoGebra skriver decimaltal med punkt.</p>')
    alt = (f'Sannolikhetskalkylatorn med μ = {g(mu)} och σ = {g(sigma)} och knappen {MODE[mode]}. '
           f'Inringat: 1 μ, 2 σ, 3 knappen, 4 indata och 5 svaret {v}.')
    return txt + img(f'geogebra-{sl}.png', alt, 520)


OPPNA_TEXT = ('<p>Gå till geogebra.org/classic. Klicka på menyknappen ☰ uppe till höger, välj <strong>Perspektiv</strong> '
              'och sedan <strong>Sannolikhet</strong>. Kontrollera att det står <strong>Normalfördelning</strong> i listan.</p>')
OPPNA_BILD = img('geogebra-sannolikhet-perspektiv.png', nf1.ALT_OPPNA, 340)
STARTRUBRIK = re.compile(r'^(Öppna|Ange normalfördelningen|Välj normalfördelning|Ställ in|Sannolikhetskalkylatorn)')


def infoga_i(f, uid, logg):
    """Lägg in bilder och ett öppningssteg i ett facit (huvudfacit eller delkort)."""
    namn, calcs = INFOGA[uid]
    lis = [m for m in re.finditer(r'<li>.*?</li>', f)]
    tillagg = {}
    for c in calcs:
        sl, mu, sigma, mode, a, b, p, sok, _ = c
        traff = [m for m in lis if sok in m.group(0)]
        if not traff:
            continue
        tillagg.setdefault(traff[0].start(), []).append(bildtext(logg, sl, mu, sigma, mode, a, b, p))
    if not tillagg:
        return f, 0
    forsta_gg = min([m.start() for m in lis if 'annolikhetskalkylator' in m.group(0)] + list(tillagg))
    ut, pos = [], 0
    for m in lis:
        ut.append(f[pos:m.start()])
        html = m.group(0)
        if m.start() == forsta_gg:
            r = re.match(r'<li><p class="facit-rubrik">(.*?)</p>', html)
            if r and STARTRUBRIK.match(r.group(1)):
                html = html[:r.end()] + OPPNA_TEXT + OPPNA_BILD + html[r.end():]
            else:
                ut.append(li(f'Öppna Sannolikhetskalkylatorn för {namn}', OPPNA_TEXT, OPPNA_BILD))
        if m.start() in tillagg:
            html = html[:-5] + ''.join(tillagg[m.start()]) + '</li>'
        ut.append(html)
        pos = m.end()
    ut.append(f[pos:])
    return ''.join(ut), sum(len(v) for v in tillagg.values())


def visat(svar):
    """Som GeoGebra visar med fyra decimaler: avrunda uppåt vid 5 (−3,01145 → −3,0115)."""
    from decimal import Decimal, ROUND_HALF_UP
    d = Decimal(svar).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)
    t = format(d, 'f').rstrip('0').rstrip('.')
    return '0' if t in ('-0', '') else t


def kolla(logg, sl, varde, dec):
    v = float(logg[sl]['svar'])
    # Tolerans i stället för round(): GeoGebras värde kan ligga exakt mitt emellan (−3,01145).
    assert abs(v - varde) <= 0.5 * 10 ** -dec + 1e-9, (sl, v, varde)


def svarsrad(text):
    return f'<p class="facit-svar"><strong>Svar:</strong> {text}</p>'


def skriv_om(uid, logg, u):
    namn, enhet, (sl, mu, sigma, mode, a, b), rub, extra, svt, ktrl = SKRIV_OM[uid]
    nf1.NAMN[uid] = (namn, enhet)
    nf1.BER[uid] = [(sl, mu, sigma, mode, a, b)]
    kolla(logg, sl, ktrl, 4)
    v = logg[sl]['visat']
    slut, efter = '', []
    if extra == 'proc':
        slut = f'\\[{tex(v)}\\cdot100\\approx{tex(round(float(v) * 100, 1))}\\,\\%\\]'
    elif extra.startswith('antal'):
        _, n, svar_n = extra.split(':')
        efter.append(li(f'Beräkna antalet av {n}', '<p>Resultatet är ett förväntat antal, avrundat till ett heltal.</p>',
                        f'<div class="facit-matte">\\[{tex(v)}\\cdot{n}\\approx{svar_n}\\]</div>'))
    elif extra == 'komplement':
        k = round(1 - float(v), 4)
        efter.append(li('Andelen som kasseras är resten',
                        '<p>Skruvarna utanför intervallet kasseras.</p>',
                        f'<div class="facit-matte">\\[1-{tex(v)}={tex(g(k))}\\approx{tex(round(k * 100, 1))}\\,\\%\\]</div>'))
    forst = []
    if uid == '4.217':
        forst.append(li('55 mm ligger en standardavvikelse över medelvärdet', '<div class="facit-matte">\\[55=50+5=\\mu+\\sigma\\]</div>'))
    return facit(*forst, *nf1.bas(logg, uid, rub, slut), *efter, svarstext=svt)


def skriv_om_58(logg):
    sl, mu, sigma, mode, a, b, p = INV_58
    nf1.NAMN['4.58'] = ('produktens vikt vid sorteringen', 'g')
    kolla(logg, sl, 525.6, 1)
    v = logg[sl]['visat']
    return facit(
        li('10 % över gränsen betyder 90 % under den', '<p>De 10 % tyngsta ligger över gränsen, så 90 % av produkterna väger mindre.</p>'),
        nf1.oppna('4.58'), nf1.parametrar('4.58', mu, sigma),
        li('Välj Öppet åt vänster och skriv sannolikheten 0,90',
           '<p>Klicka på knappen <strong>Öppet åt vänster</strong> (3). Skriv 0,90 i rutan efter likhetstecknet (4) '
           'och tryck Enter. Då räknar GeoGebra ut gränsen.</p>'),
        li('Läs av viktgränsen vid X ≤',
           f'<p>Vid X ≤ (5) står {v}. Gränsen är alltså cirka {sv(round(float(v), 1))} g, och avrundat till hela gram 526 g.</p>',
           bildtext(logg, *INV_58)),
        svarstext='Viktgränsen bör sättas till cirka 526 g.')


def bygg(logg, src):
    data = json.loads(src[src.index('['):src.rindex(']') + 1])
    by = {u['id']: u for u in data}
    byten, rapport = [], {}
    for uid, (namn, calcs) in INFOGA.items():
        u = by[uid]
        for c in calcs:
            if c[8]:
                kolla(logg, c[0], *c[8])
        antal = 0
        for f in [u['s']] + [d['s'] for d in u.get('spelDelar') or []]:
            ny, k = infoga_i(f, uid, logg)
            antal += k
            if ny != f:
                byten.append((f, ny))
        # Varje beräkning ska ha hamnat i minst ett facit.
        for c in calcs:
            assert any(c[7] in f for f in [u['s']] + [d['s'] for d in u.get('spelDelar') or []]), (uid, c[7])
        assert antal >= len(calcs), (uid, antal)
        rapport[uid] = antal
    s87 = [logg['4-87-a1']['svar'], logg['4-87-a2']['svar']]
    assert round(float(s87[0]) + float(s87[1]), 4) == 0.0956, s87
    for uid in SKRIV_OM:
        u = by[uid]
        assert not u.get('spelDelar'), uid
        byten.append((u['s'], skriv_om(uid, logg, u)))
        rapport[uid] = 'omskrivet'
    byten.append((by['4.58']['s'], skriv_om_58(logg)))
    rapport['4.58'] = 'omskrivet'
    for gammal, ny in byten:
        gl = json.dumps(gammal, ensure_ascii=False)
        assert src.count(gl) >= 1, gammal[:60]
        src = src.replace(gl, json.dumps(ny, ensure_ascii=False))
    return src, rapport


def main():
    if sys.argv[1] == 'spec':
        print(json.dumps(spec(), ensure_ascii=False, indent=1))
        return
    logg = json.loads(Path(sys.argv[2]).read_text(encoding='utf-8'))
    # GeoGebra visar fyra decimaler av det exakta värdet. Urklippet ger fem decimaler, så avrunda inte
    # det igen (dubbelavrundning: −2,0537489 → −2,05375 → −2,0538). Räkna i stället exakt och
    # kontrollera mot GeoGebras femdecimalsvärde.
    for sl, mu, sigma, mode, a, b, p in alla_berakningar():
        v = logg[sl]
        exakt = forvantat(mu, sigma, mode, a, b, p)
        assert abs(exakt - float(v['svar'])) <= 0.5e-4 + 1e-9, (sl, exakt, v['svar'])
        v['visat'] = visat(repr(exakt))
    src, rapport = bygg(logg, BANK.read_text(encoding='utf-8'))
    if '--skriv' in sys.argv:
        with open(BANK, 'w', encoding='utf-8', newline='') as f:
            f.write(src)
    print('ok', len(rapport), json.dumps(rapport, ensure_ascii=False))


if __name__ == '__main__':
    main()
