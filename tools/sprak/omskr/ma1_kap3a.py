# Ma1 kapitel 3, del A (potensregler, potensekvationer, procent, index, förändringsfaktor), omskrivet för hand
# 2026-11-17. "Ange n.", "Ange a och n separat.", definitionen 1 ≤ a < 10 och "(Svara …)" är borttagna; vad som skrivs i
# vilket fält står i kgInstruktion. Avrundning står i kgInstruktion bara där toleransen kräver en viss precision
# (Kunskapsgymmet godtar annars alla korrekt avrundade svar).
FIG = '<span class="fig">[F1]</span>'
EXP = 'Svara med exponenten.'
KN = 'Skriv resultatet som k·xⁿ och ange k och n i var sitt fält.'
AN = 'Skriv talfaktorn a och exponenten n i var sitt fält.'
ORDNING = 'Skriv lösningarna i storleksordning, den minsta först.'
EN = 'Avrunda till en decimal.'
TVA = 'Avrunda till två decimaler.'
MINUS = 'En minskning skrivs som ett negativt tal.'


def p(*s):
    return ''.join(f'<p>{x}</p>' for x in s)


def en(s):
    return f'<div class="spel-en-del">{s}</div>'


def gpf(uttr):
    return {'t': p(f'Beräkna {uttr}. Skriv svaret i grundpotensform.'), 'kg': AN}


def kn(uttr, var):
    return {'t': p(f'Förenkla {uttr} för \\({var}\\ne0\\).'), 'kg': KN.replace('x', var)}


MOMS = p('Momsen på en vara är 25 % av priset utan moms.')
INDEX26 = p('Ett prisindex har basåret 2015 med index 100. År 2025 är index 143.')
KPI73 = p('Mellan två år steg konsumentprisindex från 100 till 137, medan ett löneindex för samma period steg från 100 '
          'till 119.')
Q102 = (p(r'Priset på en produkt förändras med faktorn \(q\), där \(q&gt;1\). Samtidigt förändras antalet sålda produkter '
          r'med faktorn \(1{,}5-0{,}5q\).') + p('Den totala intäkten är oförändrad.'))
POT179 = p('Lös uppgifterna med en potensekvation.')
ELIN = p(r'Elin skriver \(\frac{(x^3)^2}{x^4}=x\).')

R = {
    # ---------------------------------------------------------------- potensregler
    '3.10': {'t': p(r'Skriv \(a^4\cdot a^7\) som en potens av \(a\), där \(a&gt;0\).'), 'kg': EXP},
    '3.11': {'t': p(r'Skriv \(8^6+4^9\) som en potens med basen 2.'), 'kg': EXP},
    '3.12': {'t': p(r'Skriv som en potens med basen 2.') +
             p(r'a) \(2^3\cdot2^4\)<br>b) \(2^5/2^2\)<br>c) \((2^3)^2\cdot2\)'),
             'd': {'a': {'t': p(r'Skriv \(2^3\cdot2^4\) som en potens med basen 2.'), 'kg': EXP},
                   'b': {'t': p(r'Skriv \(2^5/2^2\) som en potens med basen 2.'), 'kg': EXP},
                   'c': {'t': p(r'Skriv \((2^3)^2\cdot2\) som en potens med basen 2.'), 'kg': EXP}},
             'kg': 'Svara med exponenterna.'},
    '3.13': {'t': p(r'Vilket uttryck är lika med \(\frac{16^x+4^{2x}}{4^x}\) för alla reella x?')},
    '3.14': kn(r'\((2b^3)^2\)', 'b'),
    '3.44': {'t': p(r'Skriv som en potens med basen 2.') + p(r'a) \(4^3\)<br>b) \(8^4\)<br>c) \(16^2\)'),
             'd': {'a': {'t': p(r'Skriv \(4^3\) som en potens med basen 2.'), 'kg': EXP},
                   'b': {'t': p(r'Skriv \(8^4\) som en potens med basen 2.'), 'kg': EXP},
                   'c': {'t': p(r'Skriv \(16^2\) som en potens med basen 2.'), 'kg': EXP}},
             'kg': 'Svara med exponenterna.'},
    '3.46': kn(r'\(\frac{10a^6}{2a^2}\)', 'a'),
    '3.48': {'t': p(r'Skriv \(\sqrt{x^6}\cdot x^{-1}\) som en potens av \(x\), där \(x&gt;0\).'), 'kg': EXP},
    '3.50': gpf(r'\((4\cdot10^5)(3\cdot10^{-2})\)'),
    '3.78': gpf(r'\((2\cdot10^3)^3\)'),
    '3.116': {'t': p(r'Tre positiva tal är \(A=2^{30}\), \(B=4^{14}\cdot8\) och \(C=8^{10}/2\).',
                     'Ordna talen från det minsta till det största utan att beräkna dem.'),
              'kg': 'Skriv en bokstav i varje fält, det minsta talet först.'},
    '3.118': {'t': p(r'Vilket tal är störst, \(4^{90}\) eller \(7^{60}\)? Motivera ditt svar utan räknare.')},
    '3.140': {'t': p(r'I uppgifterna är \(a\ne0\).') +
              p(r'a) Skriv \(a^9/a^4\) som en potens av \(a\).<br>b) Beräkna \(a^5/a^5\).<br>c) Skriv \(a^3/a^7\) som en '
                r'potens av \(a\).'),
              'd': {'a': {'t': p(r'Skriv \(a^9/a^4\) som en potens av \(a\), där \(a\ne0\).'), 'kg': EXP},
                    'b': {'t': p(r'Beräkna \(a^5/a^5\), där \(a\ne0\).')},
                    'c': {'t': p(r'Skriv \(a^3/a^7\) som en potens av \(a\), där \(a\ne0\).'), 'kg': EXP}},
              'kg': 'Svara med exponenten i a) och c).'},
    '3.142': {'t': p(r'a) En bakterie är \(2\cdot10^{-6}\) m lång. Skriv längden i meter i decimalform.') +
              p(r'b) 5 000 bakterier, var och en \(2\cdot10^{-6}\) m lång, läggs på rad utan mellanrum. Hur lång blir raden '
                'i meter?') + p('c) En rad bakterier är 0,01 m lång. Hur lång är den i centimeter?'),
              'd': {'a': {'t': p(r'En bakterie är \(2\cdot10^{-6}\) m lång. Skriv längden i meter i decimalform.')}}},
    '3.143': {'t': p(r'Ljuset färdas med farten \(3{,}0\cdot10^8\) m/s. Avståndet mellan solen och jorden är '
                     r'\(1{,}5\cdot10^{11}\) m.') +
              p('a) Hur långt färdas ljuset på en minut? Svara i grundpotensform.<br>b) Hur många minuter tar det för '
                'solljuset att nå jorden?<br>c) Vad innebär det för påståendet att vi ser solen som den såg ut för '
                'ungefär åtta minuter sedan?')},
    '3.145': kn(r'\(\frac{x^3x^{-5}}{x^{-4}}\)', 'x'),
    '3.148': {'t': p(r'Linus skriver \((x^2)^3=x^5\). Förklara felet och skriv rätt svar.')},
    '3.171': {'t': p(r'Jorden har massan \(5{,}97\cdot10^{24}\) kg och månen massan \(7{,}35\cdot10^{22}\) kg.') +
              p('a) Vilken massa är störst? Motivera med talens grundpotensform.<br>b) Hur många gånger så stor är jordens '
                'massa som månens?<br>c) Beräkna summan av massorna och skriv den i grundpotensform.')},
    '3.177': {'t': p(r'Visa utan räknare att \(\frac{2^{158}+2^{158}+2^{158}+2^{158}}{3^{100}}&gt;1\).')},
    '3.180': kn(r'\(\frac{6x^5x^{-2}}{3x^{-1}}\)', 'x'),
    '3.182': {'t': p(r'a) Beräkna \(2^{-3}\).<br>b) Beräkna \(5^{-2}\).<br>c) Beräkna \(10^{-4}\).'),
              'd': {'a': {'t': p(r'Beräkna \(2^{-3}\).'), 'kg': 'Svara exakt med ett bråk.'},
                    'b': {'t': p(r'Beräkna \(5^{-2}\).'), 'kg': 'Svara exakt med ett bråk.'},
                    'c': {'t': p(r'Beräkna \(10^{-4}\).'), 'kg': 'Svara exakt med ett bråk.'}},
              'kg': 'Svara exakt med bråk.'},
    '3.197': {'t': p(r'Skriv \(\frac{x^{11/6}}{x^{5/6}}\) som en potens av \(x\), där \(x&gt;0\).'), 'kg': EXP},
    '3.205': {'t': p('Skriv talet 0,000072 i grundpotensform.'), 'kg': AN},
    '3.208': {'t': p(r'a) Skriv \(a^5/a^8\) som \(1/a^n\), där \(a\ne0\).<br>b) Beräkna \(4^{-1}\cdot4^3\).<br>c) Beräkna '
                     r'\((3^{-2})^{-1}\).'),
              'd': {'a': {'t': p(r'Skriv \(a^5/a^8\) som \(1/a^n\), där \(a\ne0\).'), 'kg': 'Svara med n.'},
                    'b': {'t': p(r'Beräkna \(4^{-1}\cdot4^3\).')},
                    'c': {'t': p(r'Beräkna \((3^{-2})^{-1}\).')}},
              'kg': 'Svara med n i a).'},
    '3.210': {'t': p(r'Theo påstår att \(\sqrt{a^2}=a\) för alla reella a. Vilket påstående stämmer?')},
    '3.212': {'t': ELIN + p('a) Ge den rätta förenklingen och förklara ett möjligt fel i hennes beräkning.<br>b) För vilka '
                            'reella x är hennes likhet ändå sann? Tänk på för vilka x det ursprungliga uttrycket är '
                            'definierat.'),
              'd': {'a': {'t': ELIN + p('Ge den rätta förenklingen och förklara ett möjligt fel i hennes beräkning.')},
                    'b': {'t': ELIN + p('För vilka reella x är hennes likhet ändå sann? Tänk på för vilka x det '
                                        'ursprungliga uttrycket är definierat.')}}},
    '3.214': {'t': p(r'Positiva heltal p och q uppfyller både \((2^p)^q=2^{12}\) och \(2^p\cdot2^q=2^8\). Bestäm p och q.'),
              'kg': 'Skriv det mindre talet först.'},
    '3.404': gpf(r'\((3{,}0\cdot10^5)(4{,}0\cdot10^{-3})\)'),
    '3.405': gpf(r'\(\frac{8{,}4\cdot10^7}{2{,}0\cdot10^3}\)'),
    '3.420': {'t': p(r'Skriv \(2^3\cdot2^4\) som en potens med basen 2.'), 'kg': EXP},
    '3.423': {'t': p(r'Skriv \((a^2)^3\) som en potens med basen a.'), 'kg': EXP},
    # ---------------------------------------------------------------- potensekvationer
    '3.19': {'t': p('En cylindrisk vattentank ska rymma 500 liter och vara 10 dm hög.',
                    'Hur många decimeter ska tankens radie vara?'), 'kg': TVA},
    '3.55': {'t': p(r'Lös ekvationen \(5\cdot3^x=\dfrac{3^{x+2}}{5}\).')},
    '3.123': {'t': p(r'Adam löser \(x^2=144\) och svarar \(x=12\).',
                     'Är lösningen fullständig? Förklara och ange alla lösningar.')},
    '3.179': {'t': POT179 + p('a) En kvadrat har arean 180 cm². Hur lång är sidan?<br>b) En kvadrat har arean 250 cm². Hur '
                              'lång är sidan?<br>c) En kub har volymen 64 cm³. Hur lång är kubens kant?'),
              'd': {'a': {'t': POT179 + p('En kvadrat har arean 180 cm². Hur lång är sidan?'), 'kg': EN},
                    'b': {'t': POT179 + p('En kvadrat har arean 250 cm². Hur lång är sidan?'), 'kg': EN},
                    'c': {'t': POT179 + p('En kub har volymen 64 cm³. Hur lång är kubens kant?')}},
              'kg': 'Avrunda till en decimal där det behövs.'},
    '3.415': {'t': p('En stads befolkning ökade från 12 000 till 15 000 invånare på 10 år, med lika många procent varje år.',
                     'Hur stor var den årliga ökningen i procent?'), 'kg': EN},
    '3.436': {'t': p(r'Lös ekvationen \(x^5=200\).'), 'kg': TVA},
    '3.437': {'t': p(r'Lös ekvationen \(x^3=50\).'), 'kg': TVA},
    '3.438': {'t': p(r'Lös ekvationen \(x^2=81\).'), 'kg': ORDNING},
    '3.439': {'t': p(r'Lös ekvationen \(5x^2=80\).'), 'kg': ORDNING},
    '3.537': {'t': p('Mängden av ett radioaktivt ämne i ett prov har minskat till 30 % av ursprungsmängden på 20 år. Mängden '
                     'minskar med lika många procent varje år.',
                     '<strong>a)</strong> Med hur många procent minskar mängden per år?',
                     '<strong>b)</strong> Hur många år tar det tills hälften av ämnet finns kvar?'),
              'kg': 'Avrunda a) till två decimaler och b) till en decimal.'},
    '3.620': {'t': p('En kubformad låda har volymen 2 744 cm³.') + FIG + p('Hur lång är en kant?')},
    '3.622': {'t': p('Värdet på en tavla fördubblades på 5 år. Värdet ökade med lika många procent varje år.') + FIG +
              p('Hur stor var den årliga ökningen?'), 'kg': EN},
    '3.626': {'t': p('Mängden av ett läkemedel i kroppen halveras på 4 timmar. Mängden minskar med lika många procent varje '
                     'timme.') + FIG + p('Med hur många procent minskar mängden per timme?'), 'kg': EN},
    '3.628': {'t': p('Ett kubformat akvarium ska rymma 125 liter.') + FIG + p('Hur lång ska en kant vara?')},
    '3.631': {'t': p('Ett sparkonto växte från 20 000 kr till 25 000 kr på 4 år, med samma räntesats varje år.') + FIG +
              p('Vilken var räntesatsen per år?'), 'kg': EN},
    # ---------------------------------------------------------------- procent
    '3.20': {'t': p('Elias får 20 % mer pengar att handla för, samtidigt som priset på varan halveras. Hur många procent fler '
                    'varor kan han köpa?')},
    '3.72': {'t': p('Vilka av påståendena är sanna?'), 'kg': 'Välj alla sanna påståenden.'},
    '3.187': {'t': p('Lisa får 2,5 % löneökning och Amir får 4 % löneökning. De får exakt lika många kronor i löneökning. Hur '
                     'förhåller sig deras löner till varandra före höjningen, och vem hade högst lön?'),
              'kg': 'Skriv förhållandet mellan Lisas och Amirs löner, till exempel 3:2, och sedan namnet.'},
    '3.216': {'t': p('En butik vill efter en rea höja priserna tillbaka till exakt den ursprungliga nivån. Under rean var '
                     'rabatten 20 %.') +
              p(r'a) Med hur många procent måste priset höjas efter rean?<br>b) Förklara varför svaret inte är 20 %.<br>c) '
                r'Skriv ett uttryck för hur många procent priset måste höjas efter en rabatt på \(p\) procent.')},
    '3.453': {'t': p('Ett pris höjs från 200 kr till 220 kr. Vilket påstående stämmer?')},
    '3.454': {'t': p('Ett partis stöd ökar från 20 % till 25 %. Vilket påstående stämmer?')},
    '3.541': {'t': p('En butik erbjuder två kampanjer på samma vara:') +
              '<ul><li>Kampanj 1: först 20 % rabatt och sedan ytterligare 25 % rabatt på det nya priset.</li><li>Kampanj 2: '
              '45 % rabatt direkt.</li></ul>' +
              p('Hur många procent dyrare blir varan med kampanj 1 än med kampanj 2?'), 'kg': EN},
    '3.547': {'t': p('En månadslön är 34 750 kr före skatt. Efter skatt betalas 25 466 kr ut. Hur många procent av lönen går '
                     'till skatt?'), 'kg': EN},
    '3.548': {'t': p('En månadslön är 28 000 kr före skatt. Efter skatt betalas 21 560 kr ut. Hur många procent av lönen går '
                     'till skatt?')},
    '3.549': {'t': p('En månadslön är 32 000 kr före skatt. Efter skatt betalas 24 000 kr ut. Hur många procent av lönen går '
                     'till skatt?')},
    '8.01': {'t': p('En ryggsäck kostar 275 kr. Priset sänks med 12 %. Vad kostar den efter sänkningen?')},
    # ---------------------------------------------------------------- index
    '3.25': {'t': p('En indextabell visar:') + '[F1]' + p('En biobiljett kostade 75 kr år 2000.') +
             p('a) Vad skulle den kosta 2025 om priset följt index?<br>b) Det verkliga priset 2025 är 135 kr. Hur många '
               'procent högre är det än det indexjusterade priset?'),
             'd': {'a': {'t': p('En indextabell visar:') + '[F1]' + p('En biobiljett kostade 75 kr år 2000.') +
                              p('Vad skulle den kosta 2025 om priset följt index?')}}},
    '3.26': {'t': INDEX26 + p('a) Hur många procent har prisnivån stigit sedan basåret?<br>b) En vara kostade 250 kr år 2015. '
                              'Vad motsvarar det år 2025 om priset följt index?<br>c) En annan vara kostar 480 kr när index '
                              'är 160. Vad kostade den vid basåret?'),
             'd': {'b': {'t': INDEX26 + p('En vara kostade 250 kr år 2015. Vad motsvarar det år 2025 om priset följt '
                                          'index?')}}},
    '3.27': {'t': p('Du känner priset på en vara år 2008 och vill beräkna motsvarande pris år 2024 med hjälp av en '
                    'indextabell.', 'Vilka indextal behöver du känna till?')},
    '3.73': {'t': KPI73 + p('a) En lön på 24 000 kr följde löneindex. Vad blev den nya lönen?<br>b) Har lönen ökat eller '
                            'minskat i köpkraft? Motivera med en beräkning.<br>c) Hur många procent har köpkraften '
                            'förändrats?'),
             'd': {'c': {'t': KPI73 + p('Hur många procent har köpkraften förändrats?'), 'kg': EN}},
             'kg': 'Avrunda svaret i c) till en decimal.'},
    '3.230': {'t': p('I en indexserie har år A index 100 och år B index 115. Serien baseras om så att år B i stället får index '
                     '100. Vilket index får år A?')},
    '3.535': {'t': p('Konsumentprisindex (KPI) var 106,5 år 2020 och 125,6 år 2023. En persons månadslön var 32 000 kr år 2020 '
                     'och 35 500 kr år 2023.', 'Med hur många procent har reallönen förändrats?'),
              'kg': 'Avrunda till en decimal. ' + MINUS},
    '8.11': {'t': p('Tabellen visar ett prisindex. Hur många procent steg priset från 2023 till 2025?') + '[F1]'},
    '3.634': {'t': p('En biobiljett kostade 110 kr år 2018. Tabellen visar ett prisindex.') + '[F1]' +
              p('Vad borde biljetten kosta år 2025 om priset har följt indexet?')},
    '3.638': {'t': p('En jacka kostar i dag 455 kr när prisindex är 130. Vad kostade den basåret, då index var 100, om priset '
                     'har följt indexet?')},
    '3.641': {'t': p('En hyra följer ett hyresindex.') + '[F1]' + p('Hur stor är hyran i år om den har följt indexet?')},
    '3.642': {'t': p('Saras lön ökade från 28 000 kr till 31 500 kr. Under samma tid steg KPI från 100 till 110.',
                     'Med hur många procent ökade hennes reallön?'), 'kg': EN},
    # ---------------------------------------------------------------- förändringsfaktor
    '3.28': {'t': MOMS + p('a) En verkstadsfaktura är 2 400 kr utan moms. Vad blir priset med moms?<br>b) En cykel kostar '
                           '1 875 kr med moms. Vad kostar den utan moms?<br>c) Hur mycket av de 1 875 kronorna är moms?'),
             'd': {'a': {'t': MOMS + en('En verkstadsfaktura är 2 400 kr utan moms. Vad blir priset med moms?')},
                   'b': {'t': MOMS + en('En cykel kostar 1 875 kr med moms. Vad kostar den utan moms?')},
                   'c': {'t': p('En cykel kostar 1 875 kr med moms. Momsen är 25 % av priset utan moms.',
                                'Hur mycket av de 1 875 kronorna är moms?')}}},
    '3.30': {'t': p('Ett pris minskar från 1 280 kr till 1 088 kr.') +
             p('a) Bestäm förändringsfaktorn och minskningen i procent.<br>b) Med hur många procent måste priset sedan öka '
               'för att komma tillbaka till 1 280 kr?'),
             'd': {'b': {'t': p('Ett pris minskar från 1 280 kr till 1 088 kr.',
                                'Med hur många procent måste priset sedan öka för att komma tillbaka till 1 280 kr?'),
                         'kg': EN}},
             'kg': 'Avrunda svaret i b) till en decimal.'},
    '3.102': {'t': Q102 + p(r'a) Bestäm \(q\). Lös ekvationen grafiskt eller med GeoGebra.<br>b) Tolka de två förändringarna '
                            'i procent.'),
              'd': {'a': {'t': Q102 + p(r'Bestäm \(q\). Lös ekvationen grafiskt eller med GeoGebra.')}}},
    '8.07': {'t': p('En cykelhjälm kostar 720 kr under en rea med 20 % rabatt. Vad var priset före rean?')},
}
