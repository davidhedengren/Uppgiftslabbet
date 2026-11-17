# Ma1 bråkräkning (omr brakrakning), omskrivet för hand 2026-11-17.
# "Ange ett exakt värde." står inte längre i frågan. I Kunskapsgymmet säger kgInstruktion att svaret ska vara ett
# bråk. "Välj ett alternativ.", "(Svara …)" och "Ange a och b separat." är borttagna, och "en elev" har fått namn.
# Drillserierna 0.1266–0.1289 ("Beräkna … Svara exakt.") låter som lärarens egna övningsblad och är oförändrade.
BRAK = 'Svara exakt med ett bråk eller ett heltal.'
TN = 'Skriv täljaren och nämnaren i var sitt fält.'
FIG = '<span class="fig">[F1]</span>'


def p(*s):
    return ''.join(f'<p>{x}</p>' for x in s)


def ber(uttr):
    return {'t': p(f'Beräkna \\({uttr}\\).'), 'kg': BRAK}


def berd(uttr):
    """Uttrycket står på egen rad i originalet."""
    return {'t': p('Beräkna.') + p(f'\\[{uttr}\\]'), 'kg': BRAK}


R = {
    '0.15': ber('\\frac38+\\frac28'),
    '0.18': ber('\\frac12+\\frac13'),
    '0.21': ber('\\frac7{12}+\\frac5{18}-\\frac19'),
    '0.24': ber('\\frac9{14}-\\frac27+\\frac5{21}'),
    '0.39': ber('\\frac34\\cdot\\frac89'),
    '0.42': ber('\\frac23\\div\\frac45'),
    '0.45': ber('\\frac7{12}\\cdot\\frac{18}{35}\\cdot\\frac{10}{9}'),
    '0.51': {'t': p('Vilken av beräkningarna går inte att utföra?')},
    '0.57': ber('\\frac34-\\frac23\\cdot\\frac38'),
    '0.60': {'t': p('Lukas skriver \\(\\frac12+\\frac13=\\frac25\\). Hur ska han göra i stället?')},
    '0.66': {'t': p('Hur stora är \\(\\frac34\\cdot\\frac25\\) och \\(\\frac34\\div\\frac25\\) jämfört med \\(\\frac34\\)? '
                    'Svara utan att räkna ut värdena.')},
    '0.75': ber('2+\\frac34-\\frac56'),
    '0.78': ber('\\frac92-\\frac74-\\frac58'),
    '0.87': {'t': p('Två positiva tal x och y är båda mindre än 1. Vilket påstående gäller alltid?')},
    '0.90': {'t': p('Beräkna.') + '<div class="deluppgifter" style="display:grid;gap:0.85rem;margin:0.8rem 0;">'
             '<div>a) \\(-\\frac34+\\frac56-\\frac18\\)</div><div>b) \\(\\frac7{12}-(-\\frac5{18})-\\frac14\\)</div>'
             '<div>c) \\(-\\frac23\\cdot\\frac9{10}+\\frac15\\)</div></div>',
             'd': {'a': {'t': p('Beräkna.') + p('\\(-\\frac34+\\frac56-\\frac18\\)'), 'kg': BRAK},
                   'b': {'t': p('Beräkna.') + p('\\(\\frac7{12}-(-\\frac5{18})-\\frac14\\)'), 'kg': BRAK},
                   'c': {'t': p('Beräkna.') + p('\\(-\\frac23\\cdot\\frac9{10}+\\frac15\\)'), 'kg': BRAK}}},
    '0.96': {'t': p('Två positiva bråk är båda mindre än 1, och täljare och nämnare är positiva heltal. Nils adderar '
                    'täljarna för sig och nämnarna för sig. Hur förhåller sig hans resultat till de två bråken?')},
    '0.120': ber('-\\frac34+\\frac56'),
    '0.135': {'t': p('Låt a, b, c och d vara positiva heltal. Sofia påstår att \\(\\frac{a}{b}+\\frac{c}{d}=\\frac{a+c}{b+d}\\).',
                     'Visa med ett exempel att regeln inte stämmer, och förklara hur man adderar bråk.')},
    '0.150': {'t': p('Beräkna först \\(\\frac34-\\frac25\\). Dividera sedan resultatet med \\(1-\\frac7{10}\\).'), 'kg': BRAK},
    '0.151': {'t': p('Ett recept innehåller \\(\\frac34\\) liter mjölk till 6 portioner. Du har \\(\\frac{17}{8}\\) liter mjölk, '
                     'och det finns tillräckligt av allt annat.',
                     'Hur många <strong>hela</strong> portioner kan du som mest laga?')},
    '0.152': {'t': p('Erik ska dividera \\(\\frac56\\) med \\(\\frac{10}{9}\\). Han multiplicerar i stället \\(\\frac56\\) '
                     'med \\(\\frac{10}{9}\\) och får \\(\\frac{25}{27}\\).', 'Förklara vad som är fel och beräkna rätt svar.')},
    '0.153': {'t': p('Två positiva bråk har summan 1. Det ena är \\(\\frac7{15}\\). Båda bråken ska skrivas med samma nämnare. '
                     'Nämnaren ska vara ett heltal större än 100, men så liten som möjligt. Vilken blir nämnaren, och vilka '
                     'blir täljarna?'),
              'kg': 'Skriv nämnaren först, sedan täljaren till 7/15 och sist den andra täljaren.'},
    '0.292': berd('\\frac12+\\frac34\\cdot\\frac23'),
    '0.293': berd('(\\frac12+\\frac14)\\cdot\\frac23'),
    '0.294': berd('\\frac35-\\frac12\\cdot\\frac25'),
    '0.295': berd('(\\frac56-\\frac13)\\div\\frac12'),
    '0.296': berd('1-\\frac34\\div\\frac32'),
    '0.297': berd('\\frac23+(\\frac12)^2'),
    '0.298': berd('(\\frac34-\\frac14)^2\\cdot4'),
    '0.299': berd('(\\frac12+\\frac13)\\div\\frac56'),
    '0.300': {'t': p('Förkorta \\(\\frac{42}{63}\\) så långt som möjligt.'), 'kg': TN},
    '0.301': {'t': p('Vilket av bråken är \\(\\frac{56}{98}\\) förkortat så långt som möjligt?')},
    '0.303': {'t': p('Förkorta \\(\\frac{54}{90}\\) så långt som möjligt.'), 'kg': TN},
    '0.304': {'t': p('Förkorta \\(\\frac{120}{168}\\) så långt som möjligt.'), 'kg': TN},
    '0.305': {'t': p('Vilket av bråken är störst?')},
    '0.308': {'t': p('Skriv bråken \\(\\frac34\\), \\(\\frac5{12}\\) och \\(\\frac23\\) i storleksordning. Börja med det minsta.')},
    '0.309': {'t': p('Vilket påstående stämmer? Svara utan att skriva bråken i decimalform.')},
    '0.1242': {'t': p('Stapeln är delad i 12 lika stora delar. Den blå delen är \\(\\frac13\\) och den orange delen är '
                      '\\(\\frac14\\).') + FIG + p('Beräkna \\(\\frac13+\\frac14\\).'), 'kg': BRAK},
    '0.1243': {'t': p('Hälften av en pizza finns kvar. Du äter \\(\\frac13\\) av det som finns kvar.') + FIG +
               p('Hur stor del av hela pizzan äter du?'), 'kg': BRAK},
    '0.1244': {'t': p('Beräkna \\(1-\\frac25\\).') + FIG, 'kg': BRAK},
    '0.1245': {'t': p('Ett recept innehåller \\(\\frac23\\) dl socker. Du ska göra 4 satser. Hur mycket socker behövs?'),
               'kg': BRAK},
    '0.1246': {'t': p('Hur många flaskor som rymmer \\(\\frac34\\) liter kan fyllas med 6 liter vatten?')},
    '0.1247': {'t': p('Figuren visar \\(\\frac34\\) (blå ram) och \\(\\frac25\\) (orange ram) av samma kvadrat.') + FIG +
               p('Beräkna \\(\\frac34\\cdot\\frac25\\).'), 'kg': BRAK},
    '0.1249': {'t': p('En vattentank är fylld till \\(\\frac38\\). Efter att 15 liter fyllts på är den fylld till '
                      '\\(\\frac34\\).') + FIG + p('Hur många liter rymmer tanken?')},
    '0.1250': {'t': p('Ali äter \\(\\frac27\\) av en kaka. Bea äter sedan \\(\\frac15\\) av det som är kvar. Hur stor del av '
                      'hela kakan finns kvar?'), 'kg': BRAK},
}
