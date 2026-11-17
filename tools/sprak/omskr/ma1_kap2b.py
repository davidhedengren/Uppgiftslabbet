# Ma1 kapitel 2, del B (grafisk ekvationslösning, jämföra modeller), omskrivet för hand 2026-11-17.
# "Grafen visar hela det område som ska användas i uppgiften." var metatext. Den står kvar som "Figuren visar hela
# grafen." bara där antalet lösningar eller ett intervall beror på att grafen inte fortsätter. "Digitalt verktyg" heter
# GeoGebra eller räknare. Avrundning som rättningen behöver (tät tolerans) ligger i kgInstruktion.
FIG = '<span class="fig">[F1]</span>'
DFIG = '<div class="fig">[F1]</div>'
HELA = 'Figuren visar hela grafen.'
ORDNING = 'Skriv lösningarna i storleksordning, den minsta först.'
EN = 'Avrunda till en decimal.'
TVA = 'Avrunda till två decimaler.'


def p(*s):
    return ''.join(f'<p>{x}</p>' for x in s)


FTG = ('<p>Du ska investera 100 000 kr i ett av två företag.</p><p><strong>A. Sun-Sational Energy:</strong> värdet ökar '
       'med 11 000 kr per år<br><strong>B. Energy Eco-lution:</strong> värdet ökar med 8,5 % per år</p>')
I103 = p(r'Figuren visar grafen till funktionen \(f\).') + FIG
I140 = p(r'Två abonnemang kostar \(A(x)=129+0{,}80x\) och \(B(x)=189+0{,}30x\) kronor, där \(x\) är antalet extra minuter.')
BRYT = p(r'<em>Brytpunkten är \(x=120\) minuter.</em>')
I64 = p(r'Mängden av ett ämne är \(M(t)=300\cdot0{,}90^t\) efter \(t\) tidsenheter.')
I86 = p(r'En population är 500 vid \(t=0\) och 605 vid \(t=2\). Antag en exponentiell modell med samma procentuella '
        'förändring varje tidsenhet.')
I89 = p('En planta är 18 cm hög efter 2 dagar och 42 cm efter 8 dagar. Antag linjär tillväxt.')

R = {
    # ---------------------------------------------------------------- grafisk ekvationslösning
    '2.05': {'t': p('Lös ekvationen f(x) = 4 med hjälp av grafen. Den streckade linjen är y = 4.') + FIG, 'kg': ORDNING},
    '2.27': {'t': p('Lös ekvationen f(x − 2) = 1 med hjälp av grafen.') + FIG +
             p('Grafen visar f för hela definitionsmängden −4 ≤ x ≤ 5.'), 'kg': ORDNING},
    '2.28': {'t': p('Lös ekvationen f(x) = 5 grafiskt.') + FIG},
    '2.52': {'t': p('Grafen består av räta linjesegment. Bestäm alla x som uppfyller f(x) ≥ 2. Ange intervallgränserna exakt '
                    'och förklara varför gränserna ingår.') + FIG + p(HELA)},
    '2.96': {'t': p('Lös ekvationen f(x) = 9 grafiskt. Den streckade linjen är y = 9.') + FIG},
    '2.97': {'t': p('Bestäm alla lösningar till f(x) = g(x). För vilka x är f(x) &lt; g(x)? Förklara hur du läser av det i '
                    'figuren.') + FIG + p('Figuren visar hela graferna.')},
    '2.98': {'t': p('Grafen visar höjden för en boll som kastas från marken vid t = 0. Efter hur många sekunder landar bollen '
                    'igen?') + FIG},
    '2.99': {'t': p('Lös ekvationen f(2x − 1) = 4 med hjälp av grafen.') + FIG, 'kg': ORDNING},
    '2.100': {'t': p('Lös ekvationen f(x) = g(x) grafiskt.') + FIG},
    '2.101': {'t': p('Grafen består av fyra räta linjesegment, och segmentens ändpunkter ingår. För vilka reella p har '
                     'f(x) = p exakt fyra lösningar? Motivera ditt svar och undersök gränsfallen.') + FIG + p(HELA)},
    '2.102': {'t': p('Graferna visar kostnaden för två sätt att hyra. Tiden x är i timmar, och man betalar för den exakta '
                     'tiden, även för delar av en timme. Uppskatta när alternativen kostar lika mycket. Vad kostar de då?') +
              FIG},
    '2.103': {'t': I103 + p('a) Bestäm f(2).<br>b) Lös ekvationen f(x) = 9.'),
              'd': {'a': {'t': I103 + p('Bestäm f(2).')}, 'b': {'t': I103 + p('Lös ekvationen f(x) = 9.'), 'kg': ORDNING}}},
    '2.105': {'t': p('Grafen visar höjden för en scenplattform. Uppskatta hur länge plattformen är minst 4 m över golvet.') +
              FIG},
    '2.136': {'t': p('Lös ekvationen f(x) = g(x) grafiskt.') + FIG},
    '2.137': {'t': p('Grafen består av räta linjesegment, och segmentens ändpunkter ingår. För vilka reella p har '
                     'f(x) = p exakt två lösningar? Motivera ditt svar och undersök alla gränsfall.') + FIG + p(HELA)},
    '2.138': {'t': p('Två funktioner är f(x) = 2x + 1 och g(x) = 8 − x. Uppskatta grafernas skärningspunkt med hjälp av '
                     'figuren.') + FIG,
              'kg': 'Skriv x och y avrundade till en decimal.'},
    '2.139': {'t': p('Grafen består av räta linjesegment. Lös ekvationen f(f(x)) = 3. Visa hur du använder grafen i två steg '
                     'och ange lösningarna exakt.') + FIG + p(HELA)},
    '2.140': {'t': p('Lös ekvationen f(x) = 1 grafiskt.') + FIG},
    '2.141': {'t': p('Bestäm f(1). Bestäm sedan grafiskt alla lösningar till f(x) = 0 och det intervall där f(x) &gt; 0. Ska '
                     'intervallets gränser ingå? Motivera ditt svar.') + FIG + p(HELA)},
    '2.142': {'t': p('Grafen visar vattenmängden W(t) efter t minuter. Efter hur många minuter finns 45 liter kvar?') + FIG},
    '2.143': {'t': p('Figuren visar f(x) = −x + 6 och g(x) = 0,5x. Bestäm x-värdet där funktionerna är lika, både grafiskt '
                     'och algebraiskt.') + FIG},
    '2.144': {'t': p('Lös ekvationen f(x) = 0 grafiskt.') + FIG + p(HELA), 'kg': ORDNING},
    '2.145': {'t': p('Grafen består av räta linjesegment. Lös ekvationen f(f(x)) = 2. Visa hur du använder grafen i två '
                     'steg.') + FIG + p(HELA)},
    '2.242': {'t': p('Grafen visar den körda sträckan s(t) under en resa. Under vilket tidsintervall är s(t) = 120 km?') +
              FIG, 'kg': 'Skriv starttiden först och sedan sluttiden.'},
    '2.261': {'t': p('Grafen visar temperaturen i ett växthus. Efter hur många timmar är temperaturen 18 °C?') + FIG},
    '2.471': {'t': p(r'Lös ekvationen \(f(x)=3\) med hjälp av grafen. Den streckade linjen är \(y=3\).') + FIG, 'kg': ORDNING},
    '2.472': {'t': p(r'Lös ekvationen \(f(x)=3\) med hjälp av grafen. Den streckade linjen är \(y=3\).') + FIG, 'kg': ORDNING},
    '2.473': {'t': p(r'Lös ekvationen \(f(x)=3\) med hjälp av grafen. Den streckade linjen är \(y=3\).') + FIG, 'kg': ORDNING},
    '2.634': {'t': p(r'En cyklist startar med farten 2 m/s och accelererar med 3 m/s². Sträckan efter \(t\) sekunder är '
                     r'\(s(t)=2t+1{,}5t^2\) meter. Grafen visar \(s(t)\) och linjen \(s=20\).') + DFIG +
              p('Hur lång tid tar det att cykla 20 m?'), 'kg': EN},
    '2.635': {'t': p(r'Figuren visar \(y=2^x\) och \(y=x+3\).') + FIG +
              p(r'Ekvationen \(2^x=x+3\) har en positiv lösning. Bestäm den med hjälp av figuren.'), 'kg': EN},
    '2.637': {'t': p(r'Mängden av ett läkemedel i blodet är \(m(t)=400\cdot0{,}8^t\) mg efter \(t\) timmar.') + DFIG +
              p('När har mängden sjunkit till 100 mg?'), 'kg': EN},
    '2.639': {'t': p(r'Lös ekvationen \(3\cdot1{,}5^x=12\) grafiskt i GeoGebra.'), 'kg': TVA},
    '2.641': {'t': p(r'En bil bromsar. Sträckan efter \(t\) sekunder är \(s=20t-2t^2\) meter, och bilen stannar efter 5 s.') +
              DFIG + p(r'Ekvationen \(20t-2t^2=40\) har två lösningar. När har bilen kört 40 m?'), 'kg': EN},
    '2.642': {'t': p(r'Boll A kastas från marken: \(h_A=20t-5t^2\). Samtidigt kastas boll B från en balkong: '
                     r'\(h_B=15+10t-5t^2\).') + DFIG + p('När är bollarna på samma höjd?')},
    '2.643': {'t': p(r'En kula stöts snett uppåt. Höjden över marken är \(h(t)=1{,}8+14t-4{,}91t^2\) meter efter \(t\) '
                     'sekunder. Bestäm grafiskt i GeoGebra när kulan landar.'), 'kg': EN},
    '2.645': {'t': p(r'Figuren visar \(y=2^x\) och \(y=x^2\).') + FIG +
              p(r'Ekvationen \(2^x=x^2\) har lösningarna \(x=2\) och \(x=4\), men också en negativ lösning. Bestäm den med '
                'GeoGebra.'), 'kg': EN},
    '6.12': {'t': p(r'Lös ekvationen \(2^x=35\) med GeoGebra.'), 'kg': TVA},
    '6.32': {'t': p(r'Två modeller är \(A(t)=80\cdot1{,}05^t\) och \(B(t)=140+2t\). Använd GeoGebra för att bestämma när '
                    'modellerna har samma värde.'), 'kg': EN},
    '6.63': {'t': p(r'Lös ekvationen \(2{,}7x+4{,}1=19,5\) med räknare.')},
    '6.64': {'t': I64 + p(r'a) Lös ekvationen \(M(t)=100\) med GeoGebra.<br>b) Efter hur många hela tidsenheter är mängden för '
                          'första gången mindre än 100?'),
             'd': {'a': {'t': I64 + p(r'Lös ekvationen \(M(t)=100\) med GeoGebra.')},
                   'b': {'t': I64 + p('Efter hur många hela tidsenheter är mängden för första gången mindre än 100?')}}},
    '6.65': {'t': p(r'Lös ekvationen \(500\cdot0{,}92^t=300\) med GeoGebra.'), 'kg': TVA},
    '6.66': {'t': p(r'Två modeller är \(A(t)=500+80t\) och \(B(t)=500\cdot1{,}10^t\), \(t\ge0\).') +
             p(r'a) Använd GeoGebra för att bestämma alla tidpunkter \(0\le t\le20\) då modellerna är lika.<br>b) I vilka '
               'intervall är A respektive B störst?')},
    '6.67': {'t': p(r'Använd GeoGebra för att bestämma x-koordinaten för skärningspunkten mellan \(y=2{,}5x+5\) och '
                    r'\(y=23-1{,}1x\).')},
    '6.68': {'t': p(r'En linjär modell är \(L(t)=100+10t\). En exponentiell modell ska ha formen \(E(t)=100(1+p)^t\).') +
             p(r'a) Använd GeoGebra för att bestämma \(p\) så att modellerna har samma värde vid \(t=8\).<br>b) Bestäm alla '
               r'skärningspunkter för \(t\ge0\).<br>c) I vilka intervall är L respektive E störst?')},
    '6.69': {'t': p(r'a) Lös ekvationen \(4{,}5x-7{,}2=23{,}4\) med GeoGebra.<br>b) Bestäm skärningspunkten mellan '
                    r'\(y=2{,}4x+1{,}5\) och \(y=9-1{,}1x\) med GeoGebra.<br>c) Förklara hur du kan kontrollera att svaret i '
                    'a) är rimligt utan GeoGebra.'),
             'd': {'a': {'t': p(r'Lös ekvationen \(4{,}5x-7{,}2=23,4\) med GeoGebra.')},
                   'b': {'t': p(r'Bestäm skärningspunkten mellan \(y=2{,}4x+1{,}5\) och \(y=9-1{,}1x\) med GeoGebra.'),
                         'kg': TVA},
                   'c': {'t': p(r'Ekvationen \(4{,}5x-7{,}2=23,4\) har lösningen \(x=6,8\). Beskriv hur du kan kontrollera '
                                'lösningen utan GeoGebra.')}}},
    '6.70': {'t': p(r'Lös ekvationen \(100\cdot1{,}10^x=50+25x\) för \(0\le x\le20\) med GeoGebra. Hur många lösningar '
                    'finns?')},
    '6.71': {'t': p(r'Lös ekvationen \(120\cdot1{,}06^t=180\) med GeoGebra.'), 'kg': TVA},
    '6.72': {'t': p(r'Lös ekvationen \(4{,}7x-3{,}2=18,9\) med räknare.')},
    # ---------------------------------------------------------------- jämföra modeller
    '2.43': {'t': FTG + p(r'a) Ställ upp en matematisk modell för varje företag, där värdet \(y\) kr beror av tiden \(x\) år.'
                          '<br>b) Beräkna investeringens värde efter 4 år enligt båda modellerna.<br>c) Vilket företag ger '
                          'högst värde efter 4 år?'),
             'd': {'a': {'t': FTG + p(r'Ställ upp en matematisk modell för varje företag, där värdet \(y\) kr beror av tiden '
                                      r'\(x\) år.')},
                   'b': {'t': FTG + p('Beräkna investeringens värde efter 4 år enligt båda modellerna.'),
                         'kg': 'Avrunda till hela hundratal kronor.'},
                   'c': {'t': FTG + p('Vilket företag ger högst värde efter 4 år?'), 'kg': 'Svara A eller B.'}},
             'kg': 'Avrunda värdena i b) till hela hundratal kronor och svara A eller B i c).'},
    '2.341': {'t': p(r'Två modeller beskriver mängden verksam substans, i mg, efter \(x\) timmar:',
                     r'\(A(x)=120-5x\) och \(B(x)=100\cdot0{,}96^x\).',
                     r'Maja säger: ”Eftersom \(A(0)&gt;B(0)\) måste modell A ge störst värde för alla \(x\ge0\).” Vilket '
                     'påstående om hennes slutsats stämmer bäst?')},
    '2.348': {'t': p(r'Två modeller är \(A(x)=5+7x\) och \(B(x)=6\cdot1{,}3^x\), där \(x\) är hela dagar från 0 till 10.',
                     'Viktor säger: ”Eftersom B är större dag 0 och dag 10 måste B vara större hela tiden.” Undersök '
                     'påståendet och ge ett motexempel om det är fel.')},
    '2.532': {'t': p('I modellerna är x antalet år. Vilken av modellerna beskriver en ökning med lika många enheter varje år?')},
    '2.533': {'t': p('I modellerna är x antalet år. Vilken av modellerna beskriver en ökning med lika många procent varje år?')},
    '2.538': {'t': p('Två sparplaner startar med 1000 kr. Plan A ökar med 50 kr per år. Plan B ökar med 8 % per år.',
                     'Beräkna värdet av varje plan efter 3 år.')},
    '2.539': {'t': p('Två sparplaner startar med 5000 kr. Plan A ökar med 400 kr per år. Plan B ökar med 6 % per år.',
                     'Beräkna värdet av varje plan efter 5 år.')},
    '2.540': {'t': p('Två sparplaner startar med 2000 kr. Plan A ökar med 150 kr per år. Plan B ökar med 5 % per år.',
                     'Beräkna värdet av varje plan efter 10 år.')},
    '2.544': {'t': p('Leila använder modellen y = 200 + 15x för hur ett skogsbestånd växer. Vad betyder talet 15?')},
    '6.25': {'t': p('Ett kar innehåller 300 liter vatten. När proppen dras ur rinner det ut 25 liter per minut.') +
             p(r'a) Skriv en modell \(V(t)\) för vattenmängden efter \(t\) minuter.<br>b) Bestäm modellens definitionsmängd '
               r'och förklara varför den inte kan gälla för alla \(t\).<br>c) Jonas använder modellen och får '
               r'\(V(20)=-200\) liter. Förklara vad som har gått fel.')},
    '6.53': {'t': p('En linjär modell beskriver ett träds höjd som att det växer 40 cm varje år för all framtid. Vilken är en '
                    'rimlig begränsning hos modellen?')},
    '6.84': {'t': p('En maskins produktion under de fyra första dagarna är ungefär') + '[F1]' +
             p(r'Ida väljer en linjär modell genom första och sista punkten. Amir väljer \(E(t)=200\cdot1{,}08^t\).') +
             p('a) Bestäm den linjära modellen.<br>b) Jämför prognoserna för dag 10.<br>c) Vilken är den första hela dagen '
               'då modellerna skiljer sig med minst 100 enheter?<br>d) Vilken mer information behövs innan man väljer modell '
               'för prognoser långt fram i tiden?')},
    '6.86': {'t': I86 + p(r'a) Bestäm modellen \(P(t)\).<br>b) Beräkna populationen vid \(t=5\).'),
             'd': {'a': {'t': I86 + p(r'Bestäm modellen \(P(t)\).')},
                   'b': {'t': I86 + p(r'Beräkna populationen vid \(t=5\).')}}},
    '6.88': {'t': p(r'En rektangulär hage byggs mot en lång rak vägg. Bara tre sidor behöver stängsel, och totalt finns 40 m '
                    r'stängsel. Låt de två korta sidorna vara \(x\) meter.') + FIG +
             p(r'a) Visa att arean kan skrivas \(A(x)=x(40-2x)\) och ange en rimlig definitionsmängd.<br>b) Använd GeoGebra '
               'för att bestämma alla bredder som ger en area på minst 150 m².')},
    '6.89': {'t': I89 + p(r'a) Bestäm en modell \(H(t)\).<br>b) Uppskatta höjden efter 15 dagar.'),
             'd': {'a': {'t': I89 + p(r'Bestäm en modell \(H(t)\).')}, 'b': {'t': I89 + p('Uppskatta höjden efter 15 dagar.')}}},
    '6.140': {'t': I140 + p(r'a) För vilket \(x\) kostar abonnemangen lika mycket?<br>b) Vilket abonnemang är billigast för '
                            r'\(x\) mindre än brytpunkten?<br>c) Vilket är billigast för \(x\) större än brytpunkten?'),
              'd': {'a': {'t': I140 + p(r'För vilket \(x\) kostar abonnemangen lika mycket?')},
                    'b': {'t': I140 + p(r'Vilket abonnemang är billigast för \(x\) mindre än brytpunkten?') + BRYT,
                          'kg': 'Svara A eller B.'},
                    'c': {'t': I140 + p(r'Vilket är billigast för \(x\) större än brytpunkten?') + BRYT,
                          'kg': 'Svara A eller B.'}},
              'kg': 'Svara A eller B i b) och c).'},
    '8.19': {'t': p('Två modeller används för mängden material i ett lager. Vilket påstående stämmer med tabellen?') + '[F1]'},
}
