# Fy1 kap 9: kärnreaktioner, genomläsning 2026-11-17.
# Ändrat: precisionskrav i frågan, krystade massuppräkningar ("före och efter är … respektive … och …"),
# dubblerad fråga i 9.76, saknad punkt i 9.195/9.196 och svarsordning som bara rättningen behöver.


def p(*s):
    return ''.join(f'<p>{x}</p>' for x in s)


R = {
    '9.10': {'ers': [('b) Bestäm produkternas totala massa i u med sex decimaler.', 'b) Hur stor är produkternas totala massa?'),
                     ('Bestäm produkternas totala massa i u med sex decimaler.', 'Hur stor är produkternas totala massa?')]},
    '9.76': {'t': p('Polonium-210 alfasönderfaller. Atommassorna är 209,982874 u för polonium-210, 205,974465 u för bly-206 och 4,002603 u för helium-4.',
                    'a) Bestäm frigjord energi i MeV.', 'b) Skriv reaktionsformeln.'),
             'intro': p('Polonium-210 alfasönderfaller. Atommassorna är 209,982874 u för polonium-210, 205,974465 u för bly-206 och 4,002603 u för helium-4.'),
             'd': {'a': {'t': p('Polonium-210 alfasönderfaller. Atommassorna är 209,982874 u för polonium-210, 205,974465 u för bly-206 och 4,002603 u för helium-4.', 'Bestäm frigjord energi i MeV.')}}},
    '9.109': {'t': p('Torium-232 alfasönderfaller till radium-228. Atommassorna är 232,038056 u för torium-232, 228,031071 u för radium-228 och 4,002603 u för helium-4. Hur mycket energi frigörs?')},
    '9.115': {'t': p('Americium-241 alfasönderfaller till neptunium-237. Atommassorna är 241,056829 u för americium-241, 237,048173 u för neptunium-237 och 4,002603 u för helium-4. Hur mycket energi frigörs?')},
    'KG-FY1-ALFA-03': {'t': p('En kärna alfasönderfaller. Moderatomen har massan 238,050788 u. Dotteratomen och heliumatomen har massorna 234,043601 u och 4,002602 u. Hur mycket energi frigörs?')},
    '9.116': {'ers': [('Bestäm poloniumatomens massa i u med fem decimaler.', 'Hur stor massa har poloniumatomen?')]},
    '9.117': {'ers': [('Bestäm protaktiniumatomens massa i u med fem decimaler.', 'Hur stor massa har protaktiniumatomen?')]},
    '9.195': {'ers': [(r'x n\) Hur många', r'x n.\) Hur många')]},
    '9.196': {'ers': [(r'x n\) Hur många', r'x n.\) Hur många')]},
    '9.52': {'ers': [('Från början har kärnan masstalet A och Z antal protoner.', 'Från början har kärnan masstalet A och atomnumret Z.'),
                     ('Kärnan genomgår totalt 4n stycken sönderfall', 'Kärnan genomgår totalt 4n sönderfall')]},
    'KG-FY1-ALFA-04': {'t': p('Uran-238 med atomnummer 92 blir bly-206 med atomnummer 82 genom en serie alfa- och beta-minus-sönderfall. Hur många sönderfall av varje sort sker?'),
                       'd': {'a': {'f': 'Uran-238 med atomnummer 92 blir bly-206 med atomnummer 82 genom alfa- och beta-minus-sönderfall. Hur många alfasönderfall och hur många beta-minus-sönderfall sker?',
                                   'kg': 'Svara först med antalet alfasönderfall och sedan med antalet beta-minus-sönderfall.'}}},
    '9.111': {'ers': [('Bestäm produkternas farter i m/s, först alfapartikeln och sedan urankärnan.', 'Vilka farter får alfapartikeln och urankärnan?'),
                      ('Bestäm deras farter i m/s, först alfapartikeln och sedan urankärnan.', 'Vilka farter får de?')],
              'd': {'e': {'kg': 'Svara först med alfapartikelns fart och sedan med urankärnans.'}}},
}
# Punkten ska stå efter formeln, inte i den.
for _i in ('9.195', '9.196'):
    R[_i] = {'ers': [(r'x n.\) Hur många', r'x n\). Hur många')]}
