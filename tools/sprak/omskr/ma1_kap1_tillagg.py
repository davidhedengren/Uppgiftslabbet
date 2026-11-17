# Ma1 kapitel 1, tillägg 2026-11-17: precisionskrav som språktestet hittade. Facit är avrundat till en decimal med
# liten tolerans, så kravet behövs i rättningen. Det står nu i kgInstruktion i stället för i frågan.
EN = 'Svara med en decimal.'


def p(*s):
    return ''.join(f'<p>{x}</p>' for x in s)


INTRO_103 = 'En cylinder har volymen \\(V=\\pi r^2h\\). Volymen är 500 cm³ och diametern är 8,0 cm.'

R = {
    '1.99': {'t': p('Två koner har samma volym. Volymen ges av \\(V=\\frac{\\pi r^2h}{3}\\). Den andra konens radie är 20 % '
                    'större än den förstas.', 'Hur många procent mindre måste den andra konens höjd vara?'), 'kg': EN},
    '1.103': {'t': f'<p>{INTRO_103}</p>\n<p>a) Bestäm höjden.<br>b) Radien ökas sedan med 25 % medan höjden är oförändrad. '
                    'Hur många procent ökar volymen?</p>',
              'd': {'a': {'t': p(INTRO_103, 'Bestäm höjden.'), 'kg': EN}}},
    '1.443': {'t': p('Kroppsmasseindex beräknas med \\(BMI=\\dfrac{m}{l^2}\\), där \\(m\\) är massan i kilogram och \\(l\\) längden '
                     'i meter.', 'Beräkna BMI för en person som väger 68 kg och är 1,75 m lång.'), 'kg': EN},
    '1.444': {'t': p('En cirkels omkrets är \\(O=2\\pi r\\).', 'Beräkna omkretsen av en cirkel med radien 6,5 cm.'), 'kg': EN},
    '1.1025': {'t': p('Klockan är exakt 3.00. Minutvisaren står då på 12 och timvisaren på 3.',
                      'Hur många minuter senare täcker minutvisaren timvisaren för första gången?'), 'kg': EN},
    '1.1029': {'t': p('Klockan är exakt 2.00.', 'Hur många minuter senare bildar tim- och minutvisaren för första gången en rät '
                      'vinkel?'), 'kg': EN},
}
