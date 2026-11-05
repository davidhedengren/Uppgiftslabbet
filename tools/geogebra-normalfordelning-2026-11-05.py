"""GeoGebra-skärmbilder i Ma2-facit för normalfördelning (Sannolikhetskalkylatorn), 5 nov 2026.

Varje beräkning körs i riktig GeoGebra Classic (svenska) av tools/geogebra-skarmbilder.js.
Byggaren kontrollerar att facit använder samma värde som GeoGebra visar.

  python tools/geogebra-normalfordelning-2026-11-05.py spec > spec.json
  python tools/geogebra-normalfordelning-2026-11-05.py bygg <logg.json> [--skriv]
"""
import json
import re
import sys
from pathlib import Path
from statistics import NormalDist

ROOT = Path(__file__).resolve().parent.parent
BANK = ROOT / 'uppgifterma2.js'
BILD = 'bilder/'


def sv(x):
    return str(x).replace('-', '−').replace('.', ',')


def tex(x):
    return sv(x).replace(',', '{,}')


def img(fil, alt, maxw):
    return (f'<span class="fig"><img src="{BILD}{fil}" alt="{alt}" '
            f'style="width:100%;max-width:{maxw}px;height:auto"/></span>')


def li(rubrik, *delar):
    return f'<li><p class="facit-rubrik">{rubrik}</p>{"".join(delar)}</li>'


def g(x):
    return ('%g' % x)


# Beräkningar: (slug, mu, sigma, läge, a, b). Läge: vanster = P(X ≤ b), intervall = P(a ≤ X ≤ b),
# hoger = P(X ≥ a). Värden och lägen är avlästa ur respektive uppgift för hand.
BER = {
    '4.44': [('4-44', 100, 12, 'intervall', 88, 124)],
    '4.81': [('4-81', 72, 8, 'intervall', 65, 80)],
    '4.2086': [('4-2086', 58, 4, 'intervall', 55, 62)],
    '4.2121': [('4-2121', 100, 15, 'intervall', 85, 120)],
    '4.257': [('4-257', 5.9, 0.05, 'intervall', 5.85, 6.05)],
    '4.2092': [('4-2092-a', 250, 4, 'intervall', 242, 258), ('4-2092-b', 252, 3, 'intervall', 242, 258)],
    '4.89': [('4-89', 50, 8, 'vanster', None, 62)],
    '4.100': [('4-100', 100, 15, 'vanster', None, 120)],
    '4.123': [('4-123', 50, 8, 'vanster', None, 60)],
    '4.124': [('4-124', 12, 3, 'vanster', None, 15)],
    '4.152': [('4-152', 40, 5, 'vanster', None, 45)],
    '4.237': [('4-237', 50, 10, 'vanster', None, 60)],
    '4.522': [('4-522', 150, 20, 'vanster', None, 175)],
    '4.524': [('4-524', 167, 6, 'vanster', None, 160)],
    '4.525': [('4-525', 200, 4, 'vanster', None, 195)],
    '4.527': [('4-527', 9, 0.6, 'vanster', None, 8.5)],
    '4.2122': [('4-2122', 165, 18, 'vanster', None, 140)],
    '4.2124': [('4-2124', 3.2, 0.6, 'vanster', None, 2)],
}


# Vad fördelningen beskriver och enheten, skrivet för hand per uppgift (ger uppgiftsspecifika rubriker).
NAMN = {
    '4.44': ('kattungarnas födelsevikt', 'g'), '4.81': ('vilopulsen', 'slag/min'),
    '4.2086': ('hundarnas mankhöjd', 'cm'), '4.2121': ('logiktestets resultat', ''),
    '4.257': ('skruvarnas diameter', 'mm'), '4.2092': ('påsarnas vikt', 'g'),
    '4.89': ('bladens längd', 'mm'), '4.100': ('solrosornas höjd', 'cm'), '4.123': ('bussens restid', 'min'),
    '4.124': ('väntetiden', 'min'), '4.152': ('vattnet per dusch', 'liter'), '4.237': ('provpoängen', 'poäng'),
    '4.522': ('äpplenas vikt', 'g'), '4.524': ('kvinnornas längd', 'cm'), '4.525': ('kaffet i muggarna', 'ml'),
    '4.527': ('löptiderna på 60 m', 's'), '4.2122': ('äpplenas vikt vid must', 'g'),
    '4.2124': ('batteriernas livslängd', 'år'),
}


def sannolikhet(mu, sigma, mode, a, b):
    n = NormalDist(mu, sigma)
    if mode == 'vanster':
        return n.cdf(b)
    if mode == 'hoger':
        return 1 - n.cdf(a)
    return n.cdf(b) - n.cdf(a)


def spec():
    jobs = []
    for calcs in BER.values():
        for sl, mu, sigma, mode, a, b in calcs:
            j = {'slug': sl, 'typ': 'normal', 'mu': mu, 'sigma': sigma, 'mode': mode,
                 'expect': round(sannolikhet(mu, sigma, mode, a, b), 4)}
            if a is not None:
                j['a'] = a
            if b is not None:
                j['b'] = b
            jobs.append(j)
    return {'jobs': jobs}


ALT_OPPNA = 'GeoGebra Classic med menyn öppen. Inringat: 1 menyknappen, 2 Perspektiv, 3 Sannolikhet.'


def oppna(uid):
    return li(f'Öppna Sannolikhetskalkylatorn för {NAMN[uid][0]}',
              '<p>Gå till geogebra.org/classic. Klicka på menyknappen ☰ uppe till höger, välj '
              '<strong>Perspektiv</strong> och sedan <strong>Sannolikhet</strong>. Kontrollera att det står '
              '<strong>Normalfördelning</strong> i listan.</p>',
              img('geogebra-sannolikhet-perspektiv.png', ALT_OPPNA, 340))


def parametrar(uid, mu, sigma, rubrik=None):
    dec = ' Decimaltal kan skrivas med komma eller punkt.' if (mu != int(mu) or sigma != int(sigma)) else ''
    return li(rubrik or f'Ange {NAMN[uid][0]}: μ = {sv(g(mu))} och σ = {sv(g(sigma))}',
              f'<p>Klicka i rutan efter μ (1), skriv {sv(g(mu))} och tryck Enter. Gör sedan likadant i rutan '
              f'efter σ (2) med {sv(g(sigma))}.{dec}</p>')


def lage(uid, mode, a, b):
    e = f' {NAMN[uid][1]}' if NAMN[uid][1] else ''
    if mode == 'vanster':
        return li(f'Välj Öppet åt vänster och skriv gränsen {sv(g(b))}{e}',
                  '<p>Klicka på knappen <strong>Öppet åt vänster</strong> (3), den första av de fyra knapparna. '
                  f'Skriv {sv(g(b))} i rutan efter X ≤ (4) och tryck Enter. Då räknas andelen under {sv(g(b))} ut.</p>')
    if mode == 'intervall':
        return li(f'Välj Intervall och skriv gränserna {sv(g(a))}{e} och {sv(g(b))}{e}',
                  '<p>Klicka på knappen <strong>Intervall</strong> (3), den andra av de fyra knapparna. '
                  f'Skriv {sv(g(a))} i den vänstra rutan och {sv(g(b))} i den högra (4). Tryck Enter efter varje tal.</p>')
    return li(f'Välj Öppet åt höger och skriv gränsen {sv(g(a))}{e}',
              '<p>Klicka på knappen <strong>Öppet åt höger</strong> (3), den sista av de fyra knapparna. '
              f'Skriv {sv(g(a))} i rutan före ≤ X (4) och tryck Enter.</p>')


def avlas(logg, sl, mu, sigma, mode, a, b, rubrik, slut=''):
    v = logg[sl]['visat']
    if mode == 'vanster':
        omr = f'P(X ≤ {sv(g(b))})'
        kurva = f'Det skuggade området under kurvan, till vänster om {sv(g(b))}, visar samma andel.'
    elif mode == 'intervall':
        omr = f'P({sv(g(a))} ≤ X ≤ {sv(g(b))})'
        kurva = f'Det skuggade området mellan {sv(g(a))} och {sv(g(b))} visar samma andel.'
    else:
        omr = f'P(X ≥ {sv(g(a))})'
        kurva = f'Det skuggade området till höger om {sv(g(a))} visar samma andel.'
    alt = (f'Sannolikhetskalkylatorn med μ = {g(mu)} och σ = {g(sigma)}. Inringat: 1 μ, 2 σ, 3 knappen för '
           f'området, 4 gränsen och 5 svaret {v}.')
    return li(rubrik,
              f'<p>Efter likhetstecknet (5) står {v}. GeoGebra skriver decimaltal med punkt, så {omr} ≈ {sv(v)}. '
              f'{kurva}</p>', slut,
              img(f'geogebra-{sl}.png', alt, 520))


def svar(text):
    return f'<p class="facit-svar"><strong>Svar:</strong> {text}</p>'


def facit(*steg, svarstext):
    return ('<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'
            + ''.join(steg) + '</ol>' + svar(svarstext) + '</div>')


def gamla_li(s):
    return re.findall(r'<li>.*?</li>', s)


def bas(logg, uid, rubrik, slut=''):
    sl, mu, sigma, mode, a, b = BER[uid][0]
    return [oppna(uid), parametrar(uid, mu, sigma), lage(uid, mode, a, b), avlas(logg, sl, mu, sigma, mode, a, b, rubrik, slut)]


def kolla(logg, sl, varde, dec):
    """Facits värde (avrundat till dec decimaler) ska stämma med GeoGebras."""
    v = float(logg[sl]['svar'])
    assert round(v, dec) == round(varde, dec), (sl, v, varde)


def bygg_alla(logg, data):
    by = {u['id']: u for u in data}
    ny = {}

    def proc(v, d=1):
        return f'\\[{tex(v)}\\cdot100\\approx{tex(round(float(v) * 100, d))}\\,\\%\\]'

    # Intervall
    u = by['4.44']; kolla(logg, '4-44', 0.8186, 4)
    ny['4.44'] = facit(*bas(logg, '4.44', 'Läs av andelen mellan 88 g och 124 g'), gamla_li(u['s'])[2],
                       svarstext='Cirka 655 kattungar.')
    kolla(logg, '4-81', 0.6506, 4)
    ny['4.81'] = facit(*bas(logg, '4.81', 'Läs av sannolikheten och skriv den i procent',
                            proc(logg['4-81']['visat'])), svarstext='Sannolikheten är cirka 65,1 %.')
    kolla(logg, '4-2086', 0.6147, 4)
    ny['4.2086'] = facit(*bas(logg, '4.2086', 'Läs av andelen och skriv den i procent',
                              proc(logg['4-2086']['visat'])),
                         svarstext='Cirka 61,5 % av hundarna har en mankhöjd mellan 55 och 62 cm.')
    kolla(logg, '4-2121', 0.7501, 4)
    ny['4.2121'] = facit(*bas(logg, '4.2121', 'Läs av andelen mellan 85 och 120',
                              proc(logg['4-2121']['visat'])), svarstext='Cirka 75,0 %.')
    u = by['4.257']; kolla(logg, '4-257', 0.84, 2)
    gl = gamla_li(u['s'])
    sl, mu, sigma, mode, a, b = BER['4.257'][0]
    ny['4.257'] = facit(gl[0], oppna('4.257'),
                        parametrar('4.257', mu, sigma, 'Pröva medelvärdet μ = 5,90 med σ = 0,05'), lage('4.257', mode, a, b),
                        avlas(logg, sl, mu, sigma, mode, a, b, 'Kontrollera att andelen blir ungefär 84 %',
                              '<p>Medelvärdet 5,90 mm ger alltså rätt andel mellan 5,85 mm och 6,05 mm.</p>'),
                        gl[2], svarstext='Det minsta medelvärdet är ungefär 5,90 mm.')
    u = by['4.2092']; kolla(logg, '4-2092-a', 0.9545, 4); kolla(logg, '4-2092-b', 0.9768, 4)
    gl = gamla_li(u['s'])
    A, B = BER['4.2092']
    ny['4.2092'] = facit(oppna('4.2092'),
                         parametrar('4.2092', A[1], A[2], 'Maskin A: skriv in μ = 250 och σ = 4'), lage('4.2092', *A[3:]),
                         avlas(logg, *A, 'Läs av andelen godkända påsar för maskin A'),
                         parametrar('4.2092', B[1], B[2], 'Maskin B: ändra till μ = 252 och σ = 3'),
                         li('Behåll Intervall och gränserna 242 och 258',
                            '<p>Knappen Intervall (3) och gränserna (4) är kvar sedan maskin A. Tryck Enter om '
                            'svaret inte uppdateras.</p>'),
                         avlas(logg, *B, 'Läs av andelen godkända påsar för maskin B'),
                         gl[2], svarstext='Cirka 2,2 procentenheter lägre för maskin B.')
    # Öppet åt vänster
    for uid, sl, tal, rub, svt in [
        ('4.89', '4-89', 0.9332, 'Läs av andelen kortare än 62 mm', 'Cirka 93,3 % av bladen är kortare än 62 mm.'),
        ('4.152', '4-152', 0.8413, 'Läs av andelen under 45 liter', 'Cirka 84,1 % av duscharna använde mindre än 45 liter.'),
        ('4.237', '4-237', 0.8413, 'Läs av andelen under 60 poäng', 'Cirka 84,1 % fick mindre än 60 poäng.'),
        ('4.522', '4-522', 0.8944, 'Läs av andelen äpplen under 175 g', 'Cirka 89,4 %.'),
        ('4.524', '4-524', 0.1217, 'Läs av andelen kortare än 160 cm', 'Cirka 12,2 %.'),
        ('4.525', '4-525', 0.1056, 'Läs av andelen muggar under 195 ml', 'Cirka 10,6 %.'),
        ('4.527', '4-527', 0.2023, 'Läs av andelen tider under 8,5 s', 'Cirka 20,2 %.'),
    ]:
        kolla(logg, sl, tal, 4)
        ny[uid] = facit(*bas(logg, uid, rub, proc(logg[sl]['visat'])), svarstext=svt)
    for uid, sl, tal, rub, svt in [
        ('4.100', '4-100', 0.909, 'Läs av andelen lägre än 120 cm', 'Andelen är cirka 0,909.'),
        ('4.123', '4-123', 0.894, 'Läs av andelen resor under 60 min', 'Andelen är cirka 0,894.'),
    ]:
        kolla(logg, sl, tal, 3)
        v = logg[sl]['visat']
        ny[uid] = facit(*bas(logg, uid, rub, f'<p>Med tre decimaler blir det {sv(round(float(v), 3))}.</p>'),
                        svarstext=svt)
    # 4.124: formelbladet och GeoGebra
    kolla(logg, '4-124', 0.841, 3)
    ny['4.124'] = facit(
        li('15 minuter ligger en standardavvikelse över medelvärdet', '<div class="facit-matte">\\[15=12+3=\\mu+\\sigma\\]</div>'),
        li('Formelbladets normalfördelning: 50 % + 34,1 %',
           '<p>Till vänster om medelvärdet ligger 50 %. Enligt figuren på formelbladet ligger 34,1 % mellan '
           '\\(\\mu\\) och \\(\\mu+\\sigma\\).</p><div class="facit-matte">\\[50\\,\\%+34{,}1\\,\\%=84{,}1\\,\\%\\]</div>'),
        *bas(logg, '4.124', 'Läs av sannolikheten i GeoGebra',
             f'<p>Det stämmer med formelbladet: {sv(logg["4-124"]["visat"])} ≈ 84,1 %.</p>'),
        svarstext='Sannolikheten är ungefär 84,1 %.')
    # Antal
    kolla(logg, '4-2122', 0.0824, 4)
    ny['4.2122'] = facit(*bas(logg, '4.2122', 'Läs av andelen under 140 g och beräkna antalet',
                              '<div class="facit-matte">\\[0{,}0824\\cdot500\\approx41\\]</div>'),
                         svarstext='Ungefär 41 äpplen.')
    kolla(logg, '4-2124', 0.0228, 4)
    ny['4.2124'] = facit(*bas(logg, '4.2124', 'Läs av andelen före garantitidens slut'),
                         li('Beräkna det förväntade antalet',
                            '<p>Resultatet är en uppskattning, inte ett exakt antal framtida batteribyten.</p>'
                            '<div class="facit-matte">\\[0{,}0228\\cdot4000\\approx91\\]</div>'),
                         svarstext='Ungefär 91 batterier.')
    return ny


def main():
    if sys.argv[1] == 'spec':
        print(json.dumps(spec(), ensure_ascii=False, indent=1))
        return
    logg = json.loads(Path(sys.argv[2]).read_text(encoding='utf-8'))
    src = BANK.read_text(encoding='utf-8')
    data = json.loads(src[src.index('['):src.rindex(']') + 1])
    by = {u['id']: u for u in data}
    ny = bygg_alla(logg, data)
    for uid, s in ny.items():
        u = by[uid]
        assert not u.get('spelDelar'), uid  # piloten gäller bara uppgifter utan delkort
        gl = json.dumps(u['s'], ensure_ascii=False)
        assert src.count(gl) == 1, uid
        src = src.replace(gl, json.dumps(s, ensure_ascii=False))
    if '--skriv' in sys.argv:
        with open(BANK, 'w', encoding='utf-8', newline='') as f:
            f.write(src)
    print('ok', len(ny), ' '.join(ny))


if __name__ == '__main__':
    main()
