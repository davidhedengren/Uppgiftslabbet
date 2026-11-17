# Fy1 kap 9: stråldoser, genomläsning 2026-11-17.
# Ändrat: "Räkna med …" (blir "Antag att …" eller ett vanligt påstående), "I en modell", "den" i stället för "dosen per timme", semikolon och enhet i frågan där Kunskapsgymmet
# visar den.
R = {
    # "Samma vävnad" behålls (fysik1-straldoser låser det: båda doserna träffar samma vävnad). Återställer en
    # tidigare körning som skrev "En vävnad".
    '9.89': {'ers': [('En vävnad får 1,5 mGy', 'Samma vävnad får 1,5 mGy'),
                     ('Gamma, neutroner och alfa har i en uppgift viktfaktorerna', 'Gamma, neutroner och alfa har viktfaktorerna')]},
    '9.178': {'ers': [('En vävnad får gammastrålning vid två undersökningar.', 'Samma vävnad får gammastrålning vid två undersökningar.')]},
    '9.186': {'ers': [('En vävnad får', 'Samma vävnad får')]},
    '9.189': {'ers': [('En vävnad får', 'Samma vävnad får')]},
    '9.15': {'ers': [('Lungvävnaden får', 'Samma lungvävnad får')]},
    '9.94': {'ers': [('Räkna med bakgrundsdosen 2,4 mSv per år och 365 dygn per år.', 'Bakgrundsdosen är 2,4 mSv per år. Ett år är 365 dygn.'),
                     ('Räkna med en bakgrundsdos på 2,4 mSv per år.', 'Bakgrundsdosen är 2,4 mSv per år.')]},
    '9.98': {'ers': [('Räkna med bakgrundsdosen 2,4 mSv per år och 365 dygn per år.', 'Bakgrundsdosen är 2,4 mSv per år. Ett år är 365 dygn.'),
                     ('Räkna med en bakgrundsdos på 2,4 mSv per år.', 'Bakgrundsdosen är 2,4 mSv per år.')]},
    '9.96': {'ers': [(' i µSv/h.', '.')]},
    '9.366': {'ers': [('Räkna med viktfaktorn 3,0.', 'Viktfaktorn är 3,0.')]},
    '9.371': {'ers': [('Räkna med viktfaktorn 1.', 'Viktfaktorn är 1.')]},
    '9.381': {'ers': [('Räkna med viktfaktorn 10.', 'Viktfaktorn är 10.')]},
    '9.385': {'ers': [('Räkna med viktfaktorn 14.', 'Viktfaktorn är 14.'),
                      ('Hur stor absorberad dos krävs i Gy?', 'Hur stor absorberad dos krävs?'),
                      ('b) Bestäm absorberad energi i J.', 'b) Bestäm den absorberade energin.')]},
    '9.367': {'ers': [('I en modell får 1 kg vävnad', 'Antag att 1 kg vävnad får'),
                      ('Räkna bara med dess egna sönderfall.', 'Bortse från sönderfallen hos dotterkärnorna.')]},
    '9.384': {'ers': [('I en modell får 2 kg vävnad', 'Antag att 2 kg vävnad får'),
                      ('Räkna bara med dess egna sönderfall.', 'Bortse från sönderfallen hos dotterkärnorna.')]},
    '9.368': {'ers': [('Räkna med konstant aktivitet under tiden.', 'Antag att aktiviteten är konstant.')]},
    '9.379': {'ers': [('Räkna med konstant aktivitet under tiden.', 'Antag att aktiviteten är konstant.')]},
    '9.375': {'ers': [('Räkna med konstant aktivitet.', 'Antag att aktiviteten är konstant.')]},
    '9.387': {'ers': [('Räkna med att varje sönderfall i genomsnitt ger 1,4 MeV som tas upp av kroppen.', 'Varje sönderfall ger i genomsnitt 1,4 MeV som tas upp av kroppen.'),
                      ('Räkna med konstant aktivitet under tiden.', 'Antag att aktiviteten är konstant.')]},
    '9.378': {'ers': [('Räkna med en gammafoton på 1,25 MeV per sönderfall.', 'Varje sönderfall ger en gammafoton på 1,25 MeV.')]},
    '9.380': {'ers': [('absorberar 1,7 J; den andra har massan 0,15 kg.', 'absorberar 1,7 J. Den andra har massan 0,15 kg.')]},
}
# "den" syftar på dosen per timme; skriv ut det.
DEN = {'9.91': ['b', 'p'], '9.96': ['b', 'p'], '9.169': ['h'], '9.171': ['h'], '9.175': ['h'], '9.374': ['p']}
FRAS = {'b': ('Bestäm den på ', 'Bestäm dosen per timme på '),
        'p': ('På vilket avstånd är den ', 'På vilket avstånd är dosen per timme '),
        'h': ('Hur stor är den på avståndet', 'Hur stor är dosen per timme på avståndet')}
for _i, _f in DEN.items():
    R.setdefault(_i, {'ers': []})['ers'] += [FRAS[x] for x in _f]
