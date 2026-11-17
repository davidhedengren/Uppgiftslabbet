# Fy1 kap 9: aktivitet och halveringstid, genomläsning 2026-11-17.
# Texterna lät i huvudsak som lärarens prov. Ändrat: omvänd ordföljd i frågan, "modell"-meningar,
# formel i frågan (9.11 c), "1 halveringstider", tal utan tiopotens, "Räkna med/bara med" och
# enhetsprefix i frågan (kBq, GBq), som Kunskapsgymmet visar via svarEnhet.
R = {
    '9.121': {'ers': [('Efter två halveringstider, vilken aktivitet återstår?', 'Vilken aktivitet återstår efter två halveringstider?')]},
    '9.130': {'ers': [('Efter en halveringstid återstår vilken aktivitet?', 'Vilken aktivitet återstår efter en halveringstid?')]},
    '9.11': {'ers': [('Den matematiska sönderfallsmodellen är A(t) = A₀·2^(−t/T). Varför når kurvan aldrig exakt noll?',
                      'Aktiviteten halveras under varje halveringstid. Varför når kurvan aldrig exakt noll?'),
                     ('c) Varför når den matematiska kurvan aldrig exakt noll?', 'c) Varför når kurvan aldrig exakt noll?')]},
    '9.38': {'ers': [('Bestäm tid (min), andel kvar (%) och aktivitet (Bq) efter', 'Bestäm tiden, andelen kvar och aktiviteten efter'),
                     ('Bestäm tiden i minuter, andelen kvar i procent och aktiviteten i Bq efter', 'Bestäm tiden, andelen kvar och aktiviteten efter'),
                     ('efter 1 halveringstider', 'efter 1 halveringstid')]},
    '9.29': {'ers': [('Bestäm aktiviteten. Ett år är 3,156·10⁷ s.', 'Ett år är 3,156·10⁷ s. Bestäm aktiviteten.')]},
    '9.335': {'ers': [('Bestäm sönderfallskonstanten i s⁻¹. Ett år är 3,156·10⁷ s.', 'Ett år är 3,156·10⁷ s. Bestäm sönderfallskonstanten i s⁻¹.')]},
    '9.338': {'ers': [('Bestäm aktiviteten. Ett år är 3,156·10⁷ s.', 'Ett år är 3,156·10⁷ s. Bestäm aktiviteten.'),
                      ('Hur många uran-238-kärnor finns i mineralet? Ett år är 3,156·10⁷ s.', 'Ett år är 3,156·10⁷ s. Hur många uran-238-kärnor finns i mineralet?')]},
    '9.43': {'ers': [('Hur många sönderfall sker i genomsnitt under ett år? Ett år är 3,156·10⁷ s.', 'Ett år är 3,156·10⁷ s. Hur många sönderfall sker i genomsnitt under ett år?')]},
    '9.423': {'ers': [('Hur många kol-14-kärnor finns i provet? Ett år är 3,156·10⁷ s.', 'Ett år är 3,156·10⁷ s. Hur många kol-14-kärnor finns i provet?')]},
    '9.346': {'ers': [('Vår matematiska modell för ett vismut-210-prov är A(t) = A₀·2^(−t/T), där A₀ = 0,37 GBq och T = 5,01 dygn. Vilken aktivitet ger modellen efter 365 dygn?',
                       'Ett vismut-210-prov har aktiviteten 0,37 GBq. Halveringstiden är 5,01 dygn. Vilken aktivitet har provet efter 365 dygn?')]},
    '9.348': {'ers': [('Från början är antalet Sr-90-kärnor dividerat med antalet Cs-134-kärnor 0,0078. Vad blir samma kvot efter 15 år?',
                       'Från början är kvoten mellan antalet Sr-90-kärnor och antalet Cs-134-kärnor 0,0078. Vad är kvoten efter 15 år?')]},
    '9.427': {'ers': [('I en modell finns lika många U-235- och U-238-kärnor från början.', 'Antag att det från början fanns lika många U-235- och U-238-kärnor.'),
                      ('I dag är antalet U-235-kärnor dividerat med antalet U-238-kärnor 0,0072. Hur lång tid har gått enligt modellen?',
                       'I dag är kvoten mellan antalet U-235-kärnor och antalet U-238-kärnor 0,0072. Hur lång tid har gått?')]},
    '9.359': {'ers': [('4468000000,0 år', '4,468·10⁹ år'),
                      ('Bestäm värmeeffekten i W om all frigjord energi blir värme.', 'Hur stor blir värmeeffekten om all frigjord energi blir värme?'),
                      ('Bestäm värmeeffekten i W om all denna energi blir värme.', 'Hur stor blir värmeeffekten om all denna energi blir värme?')]},
    '9.360': {'ers': [('Bestäm värmeeffekten i W om all frigjord energi blir värme.', 'Hur stor blir värmeeffekten om all frigjord energi blir värme?'),
                      ('Bestäm värmeeffekten i W om all denna energi blir värme.', 'Hur stor blir värmeeffekten om all denna energi blir värme?')]},
    '9.351': {'ers': [('Räkna med konstant fart.', 'Antag att farten är konstant.')]},
    '9.357': {'ers': [('Räkna bara med dessa två isotoper.', 'Antag att provet bara innehåller dessa två isotoper.')]},
}
for _i in ('9.41', '9.79', '9.81', '9.86', '9.30'):
    R.setdefault(_i, {'ers': []})['ers'] += [(' i kBq.', '.'), (' i GBq.', '.')]
