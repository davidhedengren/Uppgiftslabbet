# Ma1 kapitel 3, del B (upprepade förändringar, genomsnittlig förändring, ränta, amortering), omskrivet för hand
# 2026-11-17. "(Svara i kr.)", "Avrunda till hela kronor." och "Svara med en decimal." är borttagna ur frågan. Där
# toleransen kräver en viss precision står avrundningen i kgInstruktion. Negativa procentsvar förklaras i kgInstruktion
# som "En minskning skrivs som ett negativt tal." (aldrig "med tecken").
FIG = '<span class="fig">[F1]</span>'
EN = 'Avrunda till en decimal.'
TVA = 'Avrunda till två decimaler.'
TRE = 'Avrunda till tre decimaler.'
DEC = 'Svara i decimalform.'
MINUS = 'En minskning skrivs som ett negativt tal.'
# felrapporter-2026-10-12-0958 låser att eleven får veta att svaret avrundas till hela kronor (toleransen är 0,5).
HELA = 'Avrunda till hela kronor.'


def p(*s):
    return ''.join(f'<p>{x}</p>' for x in s)


def en(s):
    return f'<div class="spel-en-del">{s}</div>'


def okn(fore, fraga):
    return {'t': p(fore, fraga), 'kg': EN}


TRAD = p('Ett träd bär 40 frukter ett år och 46 nästa år. I en modell fortsätter antalet att öka med samma procent varje '
         'år.')
NOOR = p('Vid köp av en bostad betalar Noor 99 000 kr i kontantinsats. Det motsvarar 18 % av priset.')
SPAR40 = p('Du sätter in 12 000 kr på ett sparkonto med 2,4 % ränta per år. Räntan läggs till kapitalet varje år. Inga andra '
           'insättningar eller uttag görs.')
HYRA = p('En hyra är 8 200 kr i månaden. Hyran höjs med 2,8 % varje år.')
STROM = p('En strömningstjänst kostade 89 kr i månaden. Priset har därefter höjts med 15 % tre gånger, ett år i taget.')
FOND = p('Du placerar 18 000 kr i en fond som ökar med 9,5 % per år.')
EL = p('Elpriset i ett område var 1,45 kr/kWh. Under vintern steg priset med 12 %, och till våren sjönk det med 8 % från '
       'den nya nivån.')
FAKT = p(r'<em>Du kan använda den totala förändringsfaktorn \(1{,}0304\).</em>')

R = {
    # ---------------------------------------------------------------- upprepade förändringar
    '3.06': {'t': p('En rektangels längd ökar med 12 % samtidigt som bredden minskar med 12 %. Hur många procent förändras '
                    'arean? Visa med en generell beräkning.'), 'kg': MINUS},
    '3.34': {'t': TRAD + p('a) Med hur många procent ökade antalet frukter från 40 till 46?') +
             p('b) Hur många frukter ger modellen fem år efter det år då trädet bar 46 frukter?'),
             'd': {'b': {'t': TRAD + p('Hur många frukter ger modellen fem år efter det år då trädet bar 46 frukter?'),
                         'kg': 'Avrunda till ett heltal.'}},
             'kg': 'Avrunda svaret i b) till ett heltal.'},
    '3.58': {'t': p('Ett pris höjs först med 10 % och sänks sedan med 10 %. Är priset tillbaka på samma nivå? Hur många '
                    'procent har priset förändrats totalt? Motivera ditt svar.'), 'kg': MINUS},
    '3.61': {'t': p(r'Ett värde ökar först med \(p\) %, ökar sedan med samma \(p\) % en gång till och minskar därefter med '
                    r'\(p\) %.') + p('Efter de tre förändringarna är värdet totalt 15,2 % större än från början.') +
             p(r'Bestäm alla möjliga \(p\) mellan 0 % och 100 %. Använd GeoGebra och förklara varför det finns mer än en '
               'lösning.')},
    '3.63': {'t': p('En befolkning ökar från 820 miljoner till 1,64 miljarder på 130 år. Antag att ökningen är lika många '
                    'procent varje år.', 'Hur stor är den genomsnittliga årliga ökningen i procent?'), 'kg': TRE},
    '3.162': {'t': STROM + p('a) Skriv ett uttryck för priset efter de tre höjningarna.<br>b) Beräkna priset.<br>c) Hur många '
                             'procent har priset totalt ökat?'),
              'd': {'b': {'t': STROM + p('Beräkna priset.') + p(r'<em>Du kan använda uttrycket \(89\cdot1{,}15^3\).</em>'),
                          'kg': TVA},
                    'c': {'t': STROM + p('Hur många procent har priset totalt ökat?') +
                          p('<em>Du kan använda att priset efter de tre höjningarna är cirka 135,36 kr.</em>'), 'kg': EN}},
              'kg': 'Avrunda priset till två decimaler och den procentuella ökningen till en decimal.'},
    '3.167': {'t': FOND + p('a) Hur mycket är fonden värd efter 8 år?<br>b) Efter hur många hela år har värdet passerat '
                            '30 000 kr?'),
              'd': {'a': {'t': FOND + p('Hur mycket är fonden värd efter 8 år?'), 'kg': 'Avrunda till hela kronor.'}},
              'kg': 'Avrunda svaret i a) till hela kronor.'},
    '3.168': {'t': p('En hyra ökar med 3,5 % per år. Hur många procent har hyran ökat totalt efter 6 år?')},
    '3.189': {'t': EL + p('a) Bestäm den totala förändringsfaktorn.<br>b) Hur många procent har priset förändrats totalt?'
                          '<br>c) Vad är priset efter båda förändringarna?'),
              'd': {'c': {'t': EL + p('Vad är priset efter båda förändringarna?') + FAKT, 'kg': TVA}},
              'kg': 'Avrunda priset i c) till två decimaler.'},
    '3.190': {'t': p('En jacka kostar 1 200 kr. Först sänks priset med 25 %. Därefter sänks det nya priset med 40 %.',
                     'Wilma säger att den totala rabatten är 65 %. Hur stor är den totala rabatten i procent? Har hon rätt? '
                     'Förklara.')},
    '3.199': {'t': p('Ett pris höjs först med 20 %. Därefter sänks det så att slutpriset blir exakt samma som '
                     'ursprungspriset.', 'Hur stor måste den andra procentuella förändringen vara?'),
              'kg': 'Avrunda till en decimal. En sänkning skrivs som ett negativt tal.'},
    '3.219': {'t': p('Under 22 handelsdagar förändras en aktie så här:',
                     '+1,2 % under 10 dagar<br>+2,5 % under 6 dagar<br>−1,8 % under 4 dagar<br>−2,0 % under 2 dagar.',
                     'Hur många procent har aktiens värde förändrats totalt? Använd förändringsfaktorer.'), 'kg': EN},
    '3.489': {'t': p('En sparsumma på 5 000 kr växer med 3 % per år.', 'Hur mycket är sparsumman värd efter 4 år?')},
    '3.490': {'t': p('Ett fordon värt 18 000 kr minskar i värde med 10 % per år.', 'Vad är fordonet värt efter 3 år?')},
    '3.491': {'t': p('En hyra på 2 000 kr höjs med 5 % per år.', 'Hur stor är hyran efter 2 år?')},
    '3.492': {'t': p('En maskin värd 64 000 kr minskar i värde med 25 % per år.', 'Vad är maskinen värd efter 2 år?')},
    '3.493': {'t': p('En befolkning på 12 000 ökar med 2 % per år.', 'Hur stor är befolkningen efter 5 år?')},
    '3.494': okn('Ett värde ökar med 6 % per år i 3 år.', 'Hur många procent är den totala ökningen?'),
    '3.495': okn('Ett värde ökar med 4 % per år i 5 år.', 'Hur många procent är den totala ökningen?'),
    '3.496': okn('Ett värde minskar med 8 % per år i 2 år.', 'Hur många procent är den totala minskningen?'),
    '3.497': okn('Ett värde ökar med 12 % per år i 2 år.', 'Hur många procent är den totala ökningen?'),
    '8.06': {'t': p('Den lagrade energin i ett batteri minskar med 4 % varje timme. Från början är energin 850 Wh. Hur mycket '
                    'återstår efter tre timmar?')},
    '3.644': {'t': p('En jacka är nedsatt i två steg.') + FIG + p('Vad kostar jackan i kassan?')},
    '3.646': {'t': p('Tidslinjen visar hur priset på en vara förändrades.') + FIG + p('Vad kostar varan efter tre år?'),
              'kg': EN},
    '3.647': {'t': p('Ett sparkonto växer med 4 % per år.') + FIG + p('Hur stort är saldot efter 6 år?')},
    '3.649': {'t': p('En skuld på 5 000 kr växer med 2 % per månad om ingenting betalas. Hur stor är skulden efter ett år?')},
    '3.651': {'t': p('En vara sänks först med 15 % och höjs sedan med 10 %. Nu kostar den 935 kr. Vad kostade den från '
                     'början?')},
    '3.652': {'t': p('Antalet invånare i en by minskar med 3 % per år.') + FIG +
              p('Hur många invånare finns det efter 5 år?')},
    '3.653': {'t': p('Tabellen visar hur ett belopp växer med 7 % per år.') + '[F1]' +
              p('Efter hur många hela år har beloppet fördubblats för första gången?')},
    # ---------------------------------------------------------------- genomsnittlig förändring
    '3.07': {'t': p('En bil köps för 260 000 kr och säljs 5 år senare för 178 000 kr. Antag att värdet minskar med lika många '
                    'procent varje år.', 'Hur stor är den genomsnittliga årliga minskningen i procent?'), 'kg': EN},
    '3.38': {'t': NOOR + p('a) Vad kostar bostaden?<br>b) Fyra år senare säljs den för 680 000 kr. Antag att värdet har ökat '
                           'med lika många procent varje år. Hur stor är den årliga ökningen i procent?'),
             'd': {'b': {'t': p('En bostad köps för 550 000 kr och säljs fyra år senare för 680 000 kr. Antag att värdet har '
                                'ökat med lika många procent varje år.', 'Hur stor är den årliga ökningen i procent?'),
                         'kg': TVA}},
             'kg': 'Avrunda svaret i b) till två decimaler.'},
    '3.65': {'t': p('Ett värde ökar med totalt 50 % på fem år. Antag att ökningen är lika många procent varje år. Hur stor är '
                    'den genomsnittliga årliga ökningen i procent?')},
    '3.104': {'t': p('En investering växer från 10 000 kr till 12 100 kr på två år. Antag att ökningen är lika många procent '
                     'varje år. Hur stor är den årliga ökningen?')},
    '3.105': {'t': p('Värdet på en fond ökar totalt med 30 % på sex år. Antag att ökningen är lika många procent varje år. '
                     'Hur stor är den årliga ökningen i procent?')},
    '3.130': {'t': p('Värdet på en tillgång ökar från 50 000 kr till 60 500 kr på två år. Antag att ökningen är lika många '
                     'procent varje år.', 'Hur stor är den årliga ökningen?')},
    '3.133': {'t': p(r'Ett värde förändras under fem år. Under de två första åren är den årliga ökningen \(p\) %. Under de tre '
                     r'sista åren är den årliga ökningen \((p-4)\) %.') +
              p('Över hela femårsperioden är den genomsnittliga årliga ökningen exakt 6 %.') +
              p(r'Bestäm \(p\). Använd GeoGebra och kontrollera att svaret är rimligt.'), 'kg': TVA},
    '3.134': {'t': p('En bils värde minskar från 250 000 kr till 170 000 kr på sex år. Antag att värdet minskar med lika många '
                     'procent varje år. Hur stor är den genomsnittliga årliga minskningen i procent?')},
    '3.138': {'t': p('En bil minskar i värde från 300 000 kr till 192 000 kr på fyra år. Antag att värdet minskar med lika '
                     'många procent varje år. Hur stor är den årliga minskningen i procent?')},
    '3.139': {'t': p(r'Ett värde ökar med \(p\) % per år under de två första åren. Under de följande tre åren minskar värdet '
                     r'med \(p/2\) % per år.') + p('Efter fem år är värdet totalt 4 % större än från början.') +
              p(r'Bestäm alla möjliga \(p\) mellan 0 % och 50 %. Använd GeoGebra och förklara varför det kan finnas två '
                'lösningar.')},
    '3.403': {'t': p('Ett värde minskar från 1 000 till 512 på tre år med samma procentuella minskning varje år.',
                     'Leo räknar ut den totala minskningen, 48,8 %, och delar med 3. Bestäm den rätta årliga minskningen och '
                     'förklara varför hans metod inte fungerar.')},
    '3.408': {'t': p('En storhet minskar från 1000 till 810 på 2 år. Antag att den minskar med lika många procent varje år.',
                     'Hur stor är den genomsnittliga årliga minskningen i procent?')},
    '3.409': {'t': p('En storhet minskar från 2400 till 1680 på 4 år. Antag att den minskar med lika många procent varje år.',
                     'Hur stor är den genomsnittliga årliga minskningen i procent?'), 'kg': TVA},
    '3.410': {'t': p('Ett värde minskar från 500 till 320 på fem år med samma procentuella minskning varje år.',
                     r'Moa säger: ”Den totala minskningen är 36 %, så den årliga minskningen är \(36/5=7{,}2\%\).” Vilken '
                     'bedömning av hennes resonemang stämmer?')},
    '3.411': {'t': p('Två modeller utgår från samma positiva startvärde och beskriver en minskning under sex år.',
                     'Modell A minskar med 7 % per år. Modell B minskar med totalt 35 % under hela sexårsperioden.',
                     'Vilket påstående jämför modellerna korrekt?')},
    '3.503': okn('Ett värde ökade från 50 000 till 65 000 på 5 år.', 'Hur stor var den genomsnittliga årliga ökningen i '
                 'procent?'),
    '3.504': okn('Ett värde ökade från 120 till 150 på 3 år.', 'Hur stor var den genomsnittliga årliga ökningen i procent?'),
    '3.505': okn('Ett värde minskade från 8000 till 6000 på 4 år.', 'Hur stor var den genomsnittliga årliga minskningen i '
                 'procent?'),
    '3.506': okn('Ett värde ökade från 2,4 till 3,1 på 6 år.', 'Hur stor var den genomsnittliga årliga ökningen i procent?'),
    '3.507': okn('Ett värde minskade från 900 till 700 på 5 år.', 'Hur stor var den genomsnittliga årliga minskningen i '
                 'procent?'),
    '3.508': okn('Ett värde ökade från 15 000 till 21 000 på 8 år.', 'Hur stor var den genomsnittliga årliga ökningen i '
                 'procent?'),
    '3.509': okn('Ett värde ökade i genomsnitt med 5 % per år under 4 år.', 'Hur många procent ökade värdet totalt?'),
    '3.510': okn('Ett värde ökade i genomsnitt med 3 % per år under 10 år.', 'Hur många procent ökade värdet totalt?'),
    '3.511': okn('Ett värde minskade i genomsnitt med 6 % per år under 3 år.', 'Hur många procent minskade värdet totalt?'),
    '3.512': {'t': p('Ett värde ökade med totalt 30 % på 3 år. Ellen säger att ökningen är 10 % per år om den är lika stor i '
                     'procent varje år. Vilket påstående stämmer?')},
    '3.544': {'t': p('En fond ökade med 50 % ett år och minskade med 50 % året därpå. Max säger att fonden ”i genomsnitt har '
                     'gått med 0 % per år”.', 'Hur stor är den verkliga genomsnittliga procentuella förändringen per år?'),
              'kg': 'Avrunda till en decimal. ' + MINUS},
    '3.600': {'t': p('Diagrammet visar antalet invånare i en ort. Antalet ökade med samma procent varje år.') + FIG +
              p('Bestäm den årliga förändringsfaktorn.'), 'kg': DEC},
    '3.601': {'t': p('Priset på en begagnad cykel sjönk från 6 400 kr till 4 900 kr på två år, med samma procentuella '
                     'minskning varje år.') + FIG + p('Med hur många procent sjönk priset varje år?')},
    '3.603': {'t': p('Antalet besökare på ett museum ökade totalt med 26,25 % på fyra år. Ökningen var lika stor i procent '
                     'varje år.', 'Hur stor var ökningen per år?')},
    '3.605': {'t': p('En kommun hade 12 000 invånare år 2014 och 15 000 invånare år 2024.') + FIG +
              p('Hur stor var den genomsnittliga årliga ökningen?'), 'kg': EN},
    '3.606': {'t': p('En bil kostar 240 000 kr som ny. Värdet minskar i genomsnitt med 15 % per år.') + FIG +
              p('Vad är bilen värd efter 3 år?')},
    '3.607': {'t': p('Ett hus ökade i värde med 12 % det första året och med 4 % det andra året.') + FIG +
              p('Hur stor var den genomsnittliga årliga ökningen?'), 'kg': EN},
    '3.609': {'t': p('Tabellen visar hur många som följer ett konto i sociala medier. Antalet ökade med samma procent varje '
                     'månad.') + '[F1]' + p('Bestäm förändringsfaktorn per månad.'), 'kg': DEC},
    '3.610': {'t': p('En aktie föll med 20 % under ett år. Under de två följande åren steg den med samma procent varje år och '
                     'var då tillbaka på sitt ursprungliga värde.') + FIG +
              p('Hur stor var den årliga ökningen under de två sista åren?'), 'kg': EN},
    '3.612': {'t': p('Lönerna i ett yrke ökade från 26 000 kr till 31 000 kr per månad på sex år.') + FIG +
              p('Hur stor var den genomsnittliga årliga ökningen?'), 'kg': EN},
    # ---------------------------------------------------------------- ränta
    '3.39': {'t': p('Efter tre år med 5,5 % årlig ränta finns 16 439,38 kr på ett konto. Inga insättningar eller uttag har '
                    'gjorts. Hur stort var startkapitalet?'), 'kg': HELA},
    '3.40': {'t': SPAR40 + p('a) Skriv förändringsfaktorn för ett år.') + p('b) Skriv ett uttryck för kapitalet efter 5 år.') +
             p('c) Beräkna kapitalet efter 5 år.'),
             'd': {'c': {'t': SPAR40 + p('Beräkna kapitalet efter 5 år.'), 'kg': TVA}},
             'kg': 'Avrunda svaret i c) till två decimaler.'},
    '3.80': {'t': p('20 000 kr sätts in på ett konto. Första året är räntan 2,0 %. Direkt efter första årets ränta sätts '
                    'ytterligare 5 000 kr in. Det andra året är räntan okänd. Tredje året är räntan 4,0 %. Efter tre år finns '
                    '27 208,48 kr. Hur hög var räntan i procent under det andra året?')},
    '3.81': {'t': p('Du sätter in 5 000 kr på ett konto med 4 % ränta. Hur stor blir räntan första året?')},
    '3.82': {'t': p('Ett kapital ökar med 5 % första året. Under de följande två åren är den årliga räntan samma procentsats. '
                    'Efter tre år har kapitalet totalt ökat med 21,275 %.',
                    'Hur hög var årsräntan under vart och ett av de två sista åren?'), 'kg': TVA},
    '3.85': {'t': p('Ett sparkapital på 18 000 kr får 3 % ränta under ett år. Hur stor är räntan i kronor?')},
    '3.87': {'t': p('20 000 kr står på ett konto med 2 % ränta. Hur stor är räntan under det andra året om inga pengar sätts in '
                    'eller tas ut?')},
    '3.88': {'t': HYRA + p('a) Skriv förändringsfaktorn för ett år.<br>b) Vad blir hyran efter 3 år?<br>c) Hur mycket mer '
                           'betalar man per månad efter 3 år jämfört med i dag?'),
             'd': {'b': {'t': HYRA + p('Vad blir hyran efter 3 år?'), 'kg': TVA},
                   'c': {'t': p('En hyra är 8 200 kr i månaden och höjs med 2,8 % varje år.',
                                'Hur mycket mer betalar man per månad efter 3 år jämfört med i dag?'), 'kg': TVA}},
             'kg': 'Avrunda b) och c) till två decimaler.'},
    '3.89': {'t': p('Du sätter in 12 000 kr på ett konto. Efter det första året får du 384 kr i ränta. Vilken var årsräntan i '
                    'procent?')},
    '3.112': {'t': p('Ett amorteringsfritt lån är 900 000 kr och årsräntan 4,0 %. Hur mycket betalas i ränta per månad?')},
    '3.126': {'t': p('10 000 kr växer till 11 255,09 kr på fyra år med samma ränta varje år. Hur hög är årsräntan i '
                     'procent?')},
    '3.203': {'t': p('10 000 kr växer med 2,5 % ränta per år. Hur mycket finns efter 5 år?'), 'kg': HELA},
    '3.217': {'t': p('8 000 kr sätts in på ett konto med 3 % årlig ränta. Hur mycket finns på kontot efter två år om inga uttag '
                     'görs?'), 'kg': HELA},
    '3.223': {'t': p('7 500 kr står på ett konto med 1,8 % årlig ränta. Hur mycket finns efter två år om räntan läggs till '
                     'kapitalet varje år?'), 'kg': HELA},
    '3.518': {'t': p('10 000 kr sätts in på ett konto med räntan 3 % per år. Räntan läggs till kapitalet varje år. Hur mycket '
                     'finns på kontot efter 5 år?'), 'kg': HELA},
    '3.519': {'t': p('25 000 kr sätts in på ett konto med räntan 2 % per år. Räntan läggs till kapitalet varje år. Hur mycket '
                     'finns på kontot efter 10 år?'), 'kg': HELA},
    '3.520': {'t': p('4000 kr sätts in på ett konto med räntan 4,5 % per år. Räntan läggs till kapitalet varje år. Hur mycket '
                     'finns på kontot efter 3 år?'), 'kg': HELA},
    '3.521': {'t': p('60 000 kr sätts in på ett konto med räntan 1,5 % per år. Räntan läggs till kapitalet varje år. Hur mycket '
                     'finns på kontot efter 8 år?')},
    '3.522': {'t': p('20 000 kr sätts in till räntan 4 % per år. Hur mycket ränta har insättningen gett totalt efter 3 år?')},
    '3.523': {'t': p('7500 kr sätts in till räntan 2 % per år. Hur mycket ränta har insättningen gett totalt efter 6 år?')},
    '3.524': {'t': p('150 000 kr sätts in till räntan 3,5 % per år. Hur mycket ränta har insättningen gett totalt efter 4 '
                     'år?')},
    '3.526': {'t': p('Två konton har samma positiva räntesats. Räntan läggs till kontona varje år. Konto A har 5 000 kr och '
                     'konto B har 10 000 kr. Vilket påstående stämmer efter 10 år utan insättningar eller uttag?')},
    '3.542': {'t': p('Du sätter in 50 000 kr i 5 år.') +
              '<ul><li>Bank A ger 3,6 % ränta per år, med ränta på ränta en gång per år.</li><li>Bank B ger 0,3 % ränta per '
              'månad, med ränta på ränta varje månad.</li></ul>' +
              p('Hur många kronor mer får du i den bättre banken efter 5 år?')},
    '3.671': {'t': p('Ett utdrag från ett sparkonto.') + FIG + p('Hur mycket ränta får man efter ett år?')},
    '3.673': {'t': p('Tabellen visar ett konto med ränta på ränta.') + '[F1]' + p('Vilket saldo ska stå efter år 3?'),
              'kg': TVA},
    '3.674': {'t': p('8 000 kr sätts in på ett konto med 5 % ränta per år. Grafen visar hur saldot växer.') + FIG +
              p('Hur mycket finns på kontot efter 10 år?')},
    '3.676': {'t': p('Ett bolån på 300 000 kr har årsräntan 4,2 %. Hur stor är räntan per månad om skulden är oförändrad?')},
    '3.679': {'t': p('Efter ett år med 2,5 % ränta finns 8 200 kr på ett konto. Inga insättningar eller uttag har gjorts. Hur '
                     'mycket sattes in?')},
    '3.681': {'t': p('Du sätter in 10 000 kr på ett konto i början av år 1 och ytterligare 10 000 kr i början av år 2. Räntan '
                     'är 3 % per år med ränta på ränta. Hur mycket finns på kontot i slutet av år 2?')},
    # ---------------------------------------------------------------- amortering
    '3.93': {'t': p('Ett lån på 90 000 kr amorteras med 7 500 kr per månad. Månadsräntan är 0,6 %. Hur mycket betalas totalt '
                    'under de tre första månaderna?')},
    '3.127': {'t': p('Ett lån på 120 000 kr återbetalas med 1 350 kr per månad i 10 år.',
                     'a) Hur mycket betalas totalt?', 'b) Hur mycket mer betalas än lånebeloppet?',
                     'c) Första månadens ränta är 780 kr. Hur många procent av första betalningen är ränta?'),
              'd': {'a': {'t': p('Ett lån återbetalas med 1 350 kr per månad i 10 år.', 'Hur mycket betalas totalt?')},
                    'b': {'t': p('Ett lån på 120 000 kr återbetalas med 1 350 kr per månad i 10 år.',
                                 'Hur mycket mer betalas än lånebeloppet?')},
                    'c': {'t': p('Den första månadsbetalningen på ett lån är 1 350 kr. Av den är 780 kr ränta.',
                                 'Hur många procent av betalningen är ränta?'), 'kg': EN}},
              'kg': 'Avrunda svaret i c) till en decimal.'},
    '3.660': {'t': p('Diagrammet visar skulden på ett lån med rak amortering i slutet av varje år.') + FIG +
              p('Hur stor är amorteringen per år?')},
    '3.662': {'t': p('Tabellen är en del av en amorteringsplan. Månadsräntan är 0,5 %.') + '[F1]' +
              p('Hur stor är räntan i månad 2?')},
    '3.663': {'t': p('Ett lån på 30 000 kr amorteras med 2 500 kr per månad. Månadsräntan är 1 %. Diagrammet visar de fyra '
                     'första betalningarna.') + FIG + p('Hur mycket ska betalas totalt i månad 3?')},
    '3.664': {'t': p('Ett lån på 200 000 kr amorteras med 20 000 kr i slutet av varje år. Räntan är 3 % per år. Hur stor är '
                     'räntan för år 2?')},
    '3.666': {'t': p('Ett lån på 24 000 kr amorteras med 4 000 kr per månad. Månadsräntan är 1 %. Hur mycket betalas i ränta '
                     'totalt?')},
    '3.667': {'t': p('En tv kan köpas på två sätt.') + FIG + p('Hur mycket dyrare blir tv:n med avbetalning?')},
    '3.669': {'t': p('Ett lån på 90 000 kr amorteras med 7 500 kr per kvartal. Hur stor är skulden efter två år?')},
    '3.670': {'t': p('Ett lån på 60 000 kr betalas av med rak amortering på 12 månader. Månadsräntan är 1 %. Hur mycket betalas '
                     'i ränta totalt?')},
}
