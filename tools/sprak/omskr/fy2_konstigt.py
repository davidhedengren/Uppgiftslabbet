"""Fy2: konstiga formuleringar som granskaren tools/sprak/konstigt.py hittade (2026-11-23).
Körs med tools/sprak/delkort_hela.py (R) och tools/sprak/byt_falt.py (BYT).

- 4.439: ”fyra maximum av första ordningen”, inledning som slutade mitt i en mening och delkort som bara var
  vinklar.
- 4.510: v_n = v_1/n behövs inte i uppgiften och är borttagen.
- GY25-FY2-EXP-03: ”plottas … mot” och ”diagrammet” utan diagram.
- 6.344: ”i ett tv-rör rör sig”.
"""

R = {
    '4.439': {'intro': 'Ljuset från en lampa går genom ett gitter med 9 800 ritsor/cm. I första ordningen syns fyra '
                       'ljusa linjer.', 'ol': True,
              'd': {'a': 'Bestäm våglängden för linjen vid 28,8°.', 'b': 'Bestäm våglängden för linjen vid 36,7°.',
                    'c': 'Bestäm våglängden för linjen vid 38,6°.', 'd': 'Bestäm våglängden för linjen vid 41,2°.'}},
}

BYT = {
    '4.510': [('\\(v_n=\\dfrac{v_1}{n}\\) och \\(E_n', '\\(E_n'),
              (' och \\(v_1=\\dfrac{e^2}{2\\varepsilon_0h}\\).', '.'),
              ('I Bohrs modell för väte är \\(r_n=n^2r_1\\), \\(E_n',
               'I Bohrs modell för väte är \\(r_n=n^2r_1\\) och \\(E_n')],
    'GY25-FY2-EXP-03': [('I ett försök med fotoelektrisk effekt plottas stoppspänningen \\(U_s\\) mot frekvensen '
                         '\\(f\\). Förklara vilken modell som bör anpassas och hur Plancks konstant kan bestämmas ur '
                         'diagrammet.',
                         'I ett försök med fotoelektrisk effekt mäter man stoppspänningen \\(U_s\\) för ljus med olika '
                         'frekvens \\(f\\) och ritar \\(U_s\\) som funktion av \\(f\\) i ett diagram. Vilken sorts '
                         'kurva bör anpassas till mätpunkterna? Förklara hur Plancks konstant kan bestämmas ur '
                         'diagrammet.')],
    '6.344': [('En elektron i ett tv-rör rör sig med farten', 'En elektron i ett gammalt tv-rör har farten')],
    '5.15': [('<div class="fig"></div>', '')],   # tom figurruta
}
R['4.498'] = {'intro': 'En laser med effekten 10 W har strålens diameter 4,0 mm. När strålen når månen är diametern '
                       '85 km.', 'ol': True,
              'd': {'a': 'Beräkna intensiteten när strålen lämnar lasern.',
                    'b': 'Beräkna intensiteten när strålen träffar månen.'}}
