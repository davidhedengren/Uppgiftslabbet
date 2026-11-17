# Ma1 kapitel 2, del C (linjära funktioner, räta linjens ekvation, bestämma linjär funktion, exponential- och
# potensfunktioner), omskrivet för hand 2026-11-17. "(Svara …)", "Endast svar krävs." och "Välj ett alternativ." är
# borttagna. "Anta" heter "Antag". Avrundning står i kgInstruktion bara där facit är avrundat med tät tolerans.
FIG = '<span class="fig">[F1]</span>'
EN = 'Avrunda till en decimal.'
TVA = 'Avrunda till två decimaler.'
TRE = 'Avrunda till tre decimaler.'


def p(*s):
    return ''.join(f'<p>{x}</p>' for x in s)


def en(s):
    return f'<div class="spel-en-del">{s}</div>'


I29 = p('En trafikskola tar en fast avgift på 1 800 kr och 620 kr per körlektion.')
I41 = p(r'Arean av en cirkel ges av potensfunktionen \(A=\pi r^2\).')
I166 = p('En behållare innehåller 84 liter efter 3 minuter och 60 liter efter 7 minuter. Antag att volymen förändras '
         'linjärt.')
I188 = p('Efter en injektion finns 80 mg av ett läkemedel i kroppen. Mängden minskar med 25 % per timme.')
I190 = p(r'Antalet bakterier i en odling är \(y=2\,000\cdot1{,}4^x\), där \(x\) är antalet timmar efter försökets början.')
I256 = p('Antalet registrerade användare för en tjänst var 48 tusen år 2018 och 63 tusen år 2023. Antag en linjär '
         'utveckling.')
I420 = p(r'En exponentialfunktion har formen \(f(x)=100\cdot b^x\) och \(f(3)=64\).')
F254B = r'Kostnaden är \(K(x)=16x+55\) kronor. Vad betyder \(k\) och \(m\)?'

R = {
    # ---------------------------------------------------------------- linjära funktioner
    '2.29': {'t': I29 + p(r'a) Skriv kostnadsfunktionen \(K(x)\), där \(x\) är antalet körlektioner.<br>b) Sara har betalat '
                          r'9 240 kr totalt. Hur många lektioner har hon tagit?<br>c) Vad betyder funktionens k- och m-värde?'),
             'd': {'a': {'t': I29 + p(r'Skriv kostnadsfunktionen \(K(x)\), där \(x\) är antalet körlektioner.')},
                   'b': {'t': I29 + p('Sara har betalat 9 240 kr totalt. Hur många lektioner har hon tagit?')},
                   'c': {'t': I29 + p('Vad betyder funktionens k- och m-värde?')}}},
    '2.106': {'t': p('Vilken av funktionerna är linjär?')},
    '2.152': {'t': p(r'Funktionen \(f\) ges av \(f(x)=-4x+19\). Beräkna \(f(8)-f(3)\).')},
    '2.236': {'t': p(r'En linjär funktion har riktningskoefficienten \(k=-3\). Vilken beskrivning stämmer?')},
    '2.254': {'li': [r'Skriv en linjär funktion \(K(x)\) för kostnaden i kronor när man åker \(x\) km.',
                     r'Vad betyder \(k\) och \(m\) i funktionen?'],
              'd': {'b': {'f': F254B, 't': p('En taxi kostar 55 kr i startavgift och 16 kr per kilometer.') + p(F254B)}}},
    '2.256': {'t': I256 + p('a) Uppskatta antalet användare år 2027.<br>b) Ange en tydlig begränsning hos uppskattningen.'),
              'd': {'a': {'t': I256 + p('Uppskatta antalet användare år 2027.')},
                    'b': {'t': I256 + p('Ange en tydlig begränsning hos uppskattningen.')}}},
    '2.329': {'t': p(r'Hanna säger att \(m=2{,}4\) i funktionen \(y=2{,}4x-3\), eftersom 2,4 står först. Vilket påstående '
                     'stämmer?')},
    '2.410': {'t': p(r'Det kostar \(C(x)\) kr att hyra en släpvagn i \(x\) timmar, där \(C(x)=75+12x\). Vad betyder talet 12?')},
    '2.437': {'t': p(r'Det kostar \(K(t)=250+90t\) kronor att hyra en släpvagn i \(t\) timmar.',
                     'Hur mycket ökar kostnaden för varje extra timme?')},
    '8.10': {'t': p(r'Ett abonnemang kostar 90 kr per månad plus 12 kr för varje extra gigabyte. Vilken modell ger '
                    r'månadskostnaden \(K\) för \(x\) extra gigabyte?')},
    # ---------------------------------------------------------------- räta linjens ekvation, bestämma linjär funktion
    '2.117': {'t': p(r'Skriv ekvationen \(2x+y=6\) på formen \(y=kx+m\). Vilka värden har \(k\) och \(m\)?')},
    '2.166': {'t': I166 + p(r'a) Bestäm en modell \(V(t)\).<br>b) Vad betyder riktningskoefficienten?<br>c) När är '
                            'behållaren tom enligt modellen? I vilket tidsintervall är det då rimligt att använda modellen?'),
              'd': {'a': {'t': I166 + p(r'Bestäm en modell \(V(t)\).')},
                    'b': {'t': I166 + p('Vad betyder riktningskoefficienten?')},
                    'c': {'t': I166 + p('När är behållaren tom enligt modellen? I vilket tidsintervall är det då rimligt '
                                        'att använda modellen?') +
                          p(r'<em>Du kan använda modellen \(V(t)=102-6t\).</em>')}}},
    '2.170': {'t': p('En taxiresa kostar 45 kr i startavgift. En resa på 5 km kostar totalt 125 kr. Antag att priset är en '
                     'linjär funktion av sträckan.', r'Bestäm kostnadsfunktionen \(K(x)\).')},
    '2.173': {'t': p(r'En planta är 18 cm hög efter 4 dagar och 33 cm efter 14 dagar. Antag linjär tillväxt. Bestäm '
                     r'\(h(x)\).')},
    '2.221': {'t': p(r'En linje går genom \((0,-4)\) och \((5,6)\). Kevin skriver \(y=2x+4\).',
                     'Förklara hans fel och ange linjens rätta ekvation.')},
    '2.621': {'t': p('Grafen visar en rät linje.') + FIG + p(r'Bestäm linjens riktningskoefficient \(k\).'),
              'kg': 'Svara i decimalform.'},
    '2.627': {'t': p('Grafen visar kostnaden för ett gymkort beroende på antal månader.') + FIG +
              p('Hur stor är startavgiften?')},
    '2.628': {'t': p(r'Linjen går genom punkterna \((-2,\ 7)\) och \((4,\ -2)\).') + FIG + p(r'Bestäm \(k\).'),
              'kg': 'Svara i decimalform.'},
    '8.15': {'t': p('En förening betalar en fast avgift och samma pris per deltagare för en aktivitet. Tabellen visar två '
                    'bokningar. Vad är priset per deltagare?') + '[F1]'},
    # ---------------------------------------------------------------- exponentialfunktioner
    '2.36': {'t': p(r'En population beskrivs av \(P(t)=480\cdot1{,}06^t\).') +
             p('a) Vad betyder talen 480 och 1,06?<br>b) Efter hur många hela år är populationen första gången större än '
               '700? Använd GeoGebra.'),
             'd': {'a': {'t': p(r'En population beskrivs av \(P(t)=480\cdot1{,}06^t\).') +
                              p('Vad betyder talen 480 och 1,06?')},
                   'b': {'t': p(r'En population beskrivs av \(P(t)=480\cdot1{,}06^t\).') +
                              p('Efter hur många hela år är populationen första gången större än 700? Använd GeoGebra.')}}},
    '2.37': {'t': p(r'a) Vilket startvärde har \(y=400\cdot1{,}06^x\)?<br>b) Vilken förändringsfaktor har '
                    r'\(y=400\cdot1{,}06^x\)?<br>c) Ökar eller minskar \(y=250\cdot0{,}88^x\), och med hur många procent per '
                    'steg?'),
             'd': {'a': {'t': p(r'Vilket startvärde har \(y=400\cdot1{,}06^x\)?')},
                   'b': {'t': p(r'Vilken förändringsfaktor har \(y=400\cdot1{,}06^x\)?')},
                   'c': {'t': p(r'Ökar eller minskar \(y=250\cdot0{,}88^x\), och med hur många procent per steg?')}}},
    '2.187': {'t': p(r'Värdet på en maskin är \(V(x)=85\,000\cdot0{,}82^x\) kr efter \(x\) år. Med hur många procent minskar '
                     'värdet varje år?')},
    '2.188': {'t': I188 + p(r'a) Skriv en formel för mängden \(M(t)\) mg efter \(t\) timmar.<br>b) Beräkna mängden efter 4 '
                            'timmar.<br>c) Efter hur många hela timmar är mängden för första gången under 20 mg?'),
              'd': {'a': {'t': I188 + p(r'Skriv en formel för mängden \(M(t)\) mg efter \(t\) timmar.')},
                    'b': {'t': I188 + p('Beräkna mängden efter 4 timmar.'), 'kg': EN},
                    'c': {'t': I188 + p('Efter hur många hela timmar är mängden för första gången under 20 mg?')}},
              'kg': 'Avrunda svaret i b) till en decimal.'},
    '2.190': {'t': I190 + p('a) Hur många bakterier fanns från början?<br>b) Med hur många procent ökar antalet varje timme?'
                            '<br>c) Beräkna antalet bakterier efter 4 timmar.'),
              'd': {'a': {'t': I190 + p('Hur många bakterier fanns från början?')},
                    'b': {'t': I190 + p('Med hur många procent ökar antalet varje timme?')},
                    'c': {'t': I190 + p('Beräkna antalet bakterier efter 4 timmar.'), 'kg': 'Avrunda till två värdesiffror.'}},
              'kg': 'Avrunda svaret i c) till två värdesiffror.'},
    '2.373': {'t': p(r'En population är 500 när \(t=0\) och 550 när \(t=1\). Antag exponentiell utveckling. Bestäm '
                     'förändringsfaktorn.')},
    '2.374': {'t': p(r'En mängd är 200 vid \(t=0\) och 288 vid \(t=2\). Utvecklingen är exponentiell.',
                     'Nils säger: ”Mängden har ökat 44 % på två steg, alltså är ökningen 22 % per steg.” Förklara varför han '
                     'har fel och bestäm den rätta procentuella ökningen per steg.')},
    '2.417': {'t': p(r'En exponentialfunktion ges av \(f(x)=3\cdot1{,}2^x\).', r'Beräkna \(f(4)\).'), 'kg': TRE},
    '2.418': {'t': p(r'En exponentialfunktion ges av \(f(x)=80\cdot0{,}85^x\).', r'Beräkna \(f(3)\).')},
    '2.420': {'t': I420 + p(r'a) Bestäm förändringsfaktorn \(b\).<br>b) Hur stor är den procentuella förändringen per steg?'),
              'd': {'a': {'t': I420 + p(r'Bestäm förändringsfaktorn \(b\).'), 'kg': TRE},
                    'b': {'t': I420 + p('Hur stor är den procentuella förändringen per steg?'), 'kg': EN}},
              'kg': 'Avrunda förändringsfaktorn till tre decimaler och den procentuella förändringen till en decimal.'},
    '2.451': {'t': p('Ett värde ökar först med 30 % och minskar sedan med 30 %.',
                     'Bestäm den totala förändringsfaktorn och den totala procentuella förändringen.')},
    '2.452': {'t': p('Ett kapital på 24 000 kr sätts in på ett konto med räntesatsen 2,5 % per år.',
                     'Hur mycket finns på kontot efter 8 år?')},
    '2.523': {'t': p(r'Ett sparkonto växer enligt \(y=5\,000\cdot1{,}04^x\). Beräkna y när x = 3.')},
    # ---------------------------------------------------------------- potensfunktioner
    '2.41': {'t': I41 + p(r'a) Beräkna arean när \(r=5\) cm.<br>b) Bestäm radien när arean är 200 cm².<br>c) Hur många '
                          'gånger större blir arean om radien fördubblas?'),
             'd': {'a': {'t': I41 + en(r'Beräkna arean när \(r=5\) cm.'), 'kg': EN},
                   'b': {'t': I41 + en('Bestäm radien när arean är 200 cm².'), 'kg': TVA},
                   'c': {'t': I41 + en('Hur många gånger större blir arean om radien fördubblas?')}},
             'kg': 'Avrunda arean till en decimal och radien till två decimaler.'},
    '2.350': {'t': p(r'Funktionen \(f\) ges av \(f(x)=2x^{2}\). Beräkna \(f(3)\).')},
    '2.351': {'t': p(r'Funktionen \(f\) ges av \(f(x)=3x^2\). Hur många gånger större är \(f(4)\) än \(f(2)\)?')},
    '2.352': {'t': p(r'Funktionen \(f\) ges av \(f(x)=0{,}5x^{2}\). Beräkna \(f(6)\).')},
    '2.353': {'t': p(r'Funktionen \(f\) ges av \(f(x)=4x^{0{,}5}\). Beräkna \(f(16)\).')},
    '2.354': {'t': p(r'Funktionen \(f\) ges av \(f(x)=2x^{-1}\). Beräkna \(f(8)\).')},
    '2.355': {'t': p(r'Funktionen \(f\) ges av \(f(x)=5x^3\). Bestäm det positiva \(x\)-värde som ger \(f(x)=40\).')},
    '2.356': {'t': p(r'Tilde beräknar \(f(4)\) för \(f(x)=1{,}5x^2\) och skriver \(1{,}5\cdot4=6\).',
                     r'Förklara felet och beräkna rätt värde på \(f(4)\).')},
    '2.357': {'t': p(r'Funktionen \(f\) ges av \(f(x)=12x^{-1}\). Bestäm det positiva \(x\)-värde som ger \(f(x)=3\).')},
    '2.358': {'t': p(r'En potensfunktion har formen \(f(x)=ax^2\) och går genom punkten \((3,40)\). Bestäm \(a\).'),
              'kg': TVA},
    '2.455': {'t': p('Luftmotståndet på ett fordon är proportionellt mot kvadraten på farten.',
                     'Farten ökar från 70 km/h till 105 km/h. Med hur många procent ökar luftmotståndet?')},
    '2.530': {'t': p(r'Arean av en cirkel är \(A(r)=\pi r^2\). Beräkna arean då r = 5 cm.')},
    '2.545': {'t': p('Bromssträckan för en bil är proportionell mot kvadraten på hastigheten. Vid 50 km/h är bromssträckan '
                     '14 m.', 'Vid vilken hastighet blir bromssträckan dubbelt så lång?'), 'kg': EN},
    '2.546': {'t': p(r'I sagan om Gulliver är invånarna i Lilliput \(\frac1{12}\) så långa som Gulliver i alla riktningar.',
                     '<strong>a)</strong> Antag att matbehovet är proportionellt mot kroppens volym. Hur många '
                     'lilliputportioner behöver Gulliver per dag?',
                     '<strong>b)</strong> Biologer menar att värmeförlusten, och därmed matbehovet, snarare beror på '
                     'kroppens yta. Hur många portioner blir det då?')},
    '2.600': {'t': p(r'Grafen visar funktionen \(y=0{,}5x^2\).') + FIG + p(r'Vilket värde har \(y\) när \(x=5\)?')},
    '2.602': {'t': p(r'Grafen visar en funktion av typen \(f(x)=ax^2\).') + FIG + p(r'Bestäm \(a\).')},
    '2.603': {'t': p(r'Tiden \(T\) sekunder för en pendelsvängning fram och tillbaka kan beräknas med \(T=2L^{0{,}5}\), där '
                     r'\(L\) är pendelns längd i meter.') + FIG +
              p('Hur lång tid tar en svängning för en pendel med längden 1,44 m?')},
    '2.604': {'t': p('Två kubformade lådor av samma material är likformiga. Den stora har tre gånger så lång kant som den '
                     'lilla.') + FIG + p('Hur många gånger tyngre är den stora lådan om massan är proportionell mot '
                                         'volymen?')},
    '2.605': {'t': p(r'Bromssträckan för en bil kan beräknas med \(s=0{,}006v^2\), där \(s\) är i meter och \(v\) i km/h.') +
              FIG + p('Hur lång är bromssträckan vid 90 km/h?')},
    '2.606': {'t': p(r'En potensfunktion \(y=Cx^n\) går genom punkterna \((1,\ 5)\) och \((2,\ 40)\).') + FIG +
              p(r'Bestäm \(y\) när \(x=3\).')},
    '2.608': {'t': p('En pizzeria säljer pizzor med diametern 30 cm och 40 cm.') + FIG +
              p('Hur många gånger större area har den stora pizzan?'), 'kg': TVA},
    '2.609': {'t': p(r'Effekten från ett vindkraftverk är proportionell mot vindhastigheten upphöjd till 3: \(P=kv^3\).') +
              FIG + p('Vinden ökar från 6 m/s till 9 m/s. Hur många gånger större blir effekten?')},
    '2.610': {'t': p(r'Funktionen \(f(x)=60x^{-1}\) beskriver hur lång tid i minuter det tar att fylla en tank med \(x\) '
                     r'slangar. Beräkna \(f(8)\).')},
    '2.611': {'t': p(r'Ett djurs energibehov per dygn kan uppskattas med \(P=70m^{0{,}75}\), där \(P\) är i kcal och \(m\) är '
                     'massan i kg.') + FIG + p('Hur stort är energibehovet för en hund som väger 16 kg?')},
}
