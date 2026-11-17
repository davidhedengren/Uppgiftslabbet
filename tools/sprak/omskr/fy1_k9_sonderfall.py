# Fy1 kap 9: sönderfall och medicinska metoder, genomläsning 2026-11-17.
# Texterna lät i huvudsak naturliga. Ändrat: modellmeningar, upprepade instruktioner och "försumma".


def p(*s):
    return ''.join(f'<p>{x}</p>' for x in s)


R = {
    '9.3': {'ers': [('Räkna bara med radioaktivt sönderfall.', 'Bortse från att kroppen gör sig av med jod på andra sätt.')]},
    '9.504': {'ers': [('Hur stor är aktiviteten efter 12 h, om man bara räknar med det radioaktiva sönderfallet?',
                       'Hur stor är aktiviteten efter 12 h? Bortse från att kroppen gör sig av med ämnet på andra sätt.')]},
    '9.28': {'ers': [('De två bortförselkonstanterna adderas.', 'Båda processerna pågår samtidigt.')]},
    '9.560': {'ers': [('Försumma dotterkärnans rekyl.', 'Bortse från att dotterkärnan börjar röra sig.')]},
    '9.47': {
        't': p('Stabila lätta kärnor har ungefär lika många protoner och neutroner. Avgör om kärnan sönderfaller med beta-minus eller beta-plus, och ange dotterkärnan.',
               'a) Kol-11 har 6 protoner och 5 neutroner.', 'b) Kol-14 har 6 protoner och 8 neutroner.',
               'c) Fosfor-32 har 15 protoner och 17 neutroner.', 'd) Syre-15 har 8 protoner och 7 neutroner.'),
        'intro': p('Stabila lätta kärnor har ungefär lika många protoner och neutroner. Avgör om kärnan sönderfaller med beta-minus eller beta-plus.')},
}
