# Fy1 kap 9: fission och fusion, genomläsning 2026-11-17.
# Ändrat: huvudtexter som upprepade alla data i varje deluppgift, modellformuleringar, konstanter i frågan
# och precisionskrav. Övriga texter lät naturliga.


def p(*s):
    return ''.join(f'<p>{x}</p>' for x in s)


R = {
    '9.46': {'ers': [('Räkna i denna modell med samma effekt under 4,6 miljarder år.', 'Antag att solen har strålat med samma effekt i 4,6 miljarder år.'),
                     ('I en modell omvandlar solen', 'Solen omvandlar')]},
    '9.409': {'t': p('När uran-235 klyvs helt frigörs energin 1,0·10¹⁴ J. Varje klyvning ger 200 MeV och en uranatom har massan 235,04 u.',
                     'a) Hur många kg uran klyvs?', 'b) Hur stor massa omvandlas till energi?'),
              'intro': p('När uran-235 klyvs helt frigörs energin 1,0·10¹⁴ J. Varje klyvning ger 200 MeV och en uranatom har massan 235,04 u.')},
    '9.410': {'t': p('En reaktor ger 1 400 MW el och dubbelt så stor effekt i värme till omgivningen under ett helt år. En villa använder 5 000 kWh per år. En uran-235-atom har massan 235,04 u och varje klyvning ger 200 MeV. Bränslet innehåller 3,0 % uran-235. Ett år är 3,156·10⁷ s.',
                     'a) Ungefär hur många villors årsbehov motsvarar elenergin?', 'b) Hur mycket energi frigörs totalt i reaktorn under ett år?',
                     'c) Hur många kg uran-235 klyvs under ett år?', 'd) Hur många kg bränsle går åt under ett år?')},
    '9.411': {'t': p('En uranreserv innehåller 4,4·10⁶ ton naturligt uran, varav 0,700 % är uran-235. En uran-235-atom har massan 235,04 u och varje klyvning ger 200 MeV. Ett år är 3,156·10⁷ s.',
                     'a) Hur många kg uran-235 finns i reserven?', 'b) Hur mycket energi frigörs om allt uran-235 klyvs?',
                     'c) Hela världens energianvändning motsvarar ungefär den konstanta effekten 1,5·10¹³ W. Hur många år skulle energin räcka?'),
              'intro': p('En uranreserv innehåller 4,4·10⁶ ton naturligt uran, varav 0,700 % är uran-235. En uran-235-atom har massan 235,04 u och varje klyvning ger 200 MeV. Ett år är 3,156·10⁷ s.')},
    '9.564': {'ers': [(' (1 u = 1,6605·10⁻²⁷ kg)', '')]},
    '9.468': {'ers': [('omvandlas sammanlagt 2,0 mg massa', 'omvandlas 2,0 mg massa')]},
    '9.290': {'ers': [('Bestäm massminskningen i u med sex decimaler.', 'Hur mycket minskar massan?')]},
}
