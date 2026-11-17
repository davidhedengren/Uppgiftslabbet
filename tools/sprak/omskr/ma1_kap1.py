# Ma1 kapitel 1 (algebra, ekvationer och olikheter), omskrivet för hand 2026-11-17.
# Alla områden i kapitlet ligger i den här filen. De flesta uppgifter låter redan som lärarens egna och är
# oförändrade. Här tas "(Svara …)", "Välj ett alternativ." och "Ange …" bort, "en elev" får namn och
# "Anta" heter "Antag". Hur flera svar skrivs in står i kgInstruktion.
FIG = '<span class="fig">[F1]</span>'
SMAL = '<span class="fig smal">[F1]</span>'
ORDNING = 'Skriv talen i storleksordning, det minsta först.'


def p(*s):
    return ''.join(f'<p>{x}</p>' for x in s)


R = {
    # ---------------------------------------------------------------- formler
    '1.04': {'t': p('Omkretsen av en cirkel är \\(C=2\\pi r\\). Hur stor är radien om omkretsen är 25 cm?'),
             'kg': 'Avrunda till en decimal.'},
    '1.34': {'t': p('En bil som kör s km och använder F liter bensin har förbrukningen \\(c=100F/s\\) liter per 100 km. '
                    'Bil A använder 18 liter på 240 km och bil B 14 liter på 200 km. Hur många liter mindre bensin använder '
                    'bil B än bil A på en resa som är 600 km?')},
    '1.39': {'t': p('Temperaturen i en ugn beskrivs av formeln T = 208 − 0,7t, där t är tiden i minuter. Vid ett tillfälle är '
                    'temperaturen 187 °C. Vilken temperatur ger formeln tio minuter senare?')},
    '1.167': {'t': p('Formeln \\(y=ax+b\\), där \\(a\\ne0\\), ska lösas ut med avseende på \\(x\\). Albin påstår att lösningen är') +
              p('\\(x=\\frac ya-b.\\)') + p('För vilka värden på \\(a\\) och \\(b\\) stämmer Albins formel för alla värden på \\(y\\)?')},
    '1.209': {'t': p('En rektangel har arean A = lb. Kalle skriver b = A − l. Hur kan man kontrollera att Kalle har fel?')},
    '1.440': {'t': p('Formeln \\(y=kx+m\\) ska användas för att bestämma \\(x\\) när \\(y\\) är känt. Vad gäller om \\(k=0\\)?')},
    '1.442': {'t': p('Arean av en parallelltrapets är \\(A=(a+b)h/2\\). Antag att A, b och h är positiva. Lös ut a. När blir även '
                     'a positiv? Förklara vad gränsfallet betyder.')},
    '1.1050': {'t': p('Arean av en triangel är \\(A=\\frac{b\\cdot h}{2}\\). Beräkna arean då b = 8 cm och h = 5 cm.')},
    '1.1052': {'t': p('Omkretsen av en rektangel är \\(O=2l+2b\\). Beräkna omkretsen då l = 7,5 m och b = 4 m.')},
    '1.1053': {'t': p('Sträckan ges av \\(s=v\\cdot t\\). En bil kör med farten 80 km/h i 2,5 h. Hur lång sträcka kör bilen?')},
    '1.1054': {'t': p('För sträcka, fart och tid gäller \\(s=v\\cdot t\\). En cyklist cyklar 36 km på 1,5 h. Vilken medelfart har '
                      'cyklisten?')},
    '1.1055': {'t': p('Priset för en taxiresa är \\(K=50+15s\\) kr, där s är antalet kilometer. En resa kostade 230 kr. Hur lång var '
                      'resan?')},
    # ---------------------------------------------------------------- förenkla uttryck
    '1.11': {'t': p('En grupp köper fyra smörgåsar för x kr styck och tre drycker för 22 kr styck. Med en kupong får de 10 kr '
                    'rabatt per smörgås, men ingen rabatt på dryckerna. Skriv ett förenklat uttryck för vad de betalar totalt.')},
    '1.72': {'t': p('Två uttryck är A = 7x + 4 − 3x + 2 och B = 4x + 9. Vilket tal d gör att A + d = B för alla x?')},
    '1.142': {'t': p('Rektangeln har längden \\(x+4\\) cm och bredden \\(x\\) cm. Skriv ett förenklat uttryck för omkretsen.') + SMAL},
    '1.201': {'t': p('Elvira vill att \\(3(px-2)-2(x+p)=10x-14\\) ska gälla för alla x. Hon testar x = 0, får p = 4 och säger att '
                     'det bevisar att likheten gäller. Har hon rätt? Fungerar p = 4 ändå? Hur många olika x-värden behöver man '
                     'pröva för att bevisa att två uttryck av formen ax + b och cx + d är lika för alla x?')},
    '1.223': {'t': p('Max skriver 5x + 2 + 4x − 7 = 9x + 9. Vilket fel har han gjort?')},
    '1.402': {'t': p('En rektangel har längden x + 3 cm och bredden x cm. En annan rektangel har längden x + 5 cm och bredden '
                     'x − 2 cm. Antag att x &gt; 2. Har rektanglarna samma omkrets för alla tillåtna x? Förklara varför villkoret '
                     'x &gt; 2 behövs.')},
    '1.431': {'t': p('Alva är \\(x\\) år. Bea är 4 år äldre än Alva.',
                     'Skriv ett förenklat uttryck för hur gamla de är tillsammans om 3 år.')},
    '1.433': {'t': p('Summan av tre heltal som följer på varandra är alltid delbar med 3. Agnes gissar att summan av fyra heltal '
                     'som följer på varandra därför alltid är delbar med 4. Undersök båda påståendena med algebra och förklara '
                     'varför de skiljer sig.')},
    '1.462': {'t': p('Jämför uttrycken \\(3(x+2)\\) och \\(3x+2\\).',
                     'Det första uttrycket är alltid lika mycket större än det andra, vilket värde \\(x\\) än har. '
                     '<strong>Hur stor är skillnaden?</strong>')},
    # ---------------------------------------------------------------- multiplicera uttryck
    '1.19': {'t': p('Jamal skriver 4(x + 3) = 4x + 3. Vilken förklaring visar vad som är fel?')},
    '1.21': {'t': p('En rektangel har bredden 4 cm och längden x + 5 cm, där x &gt; 0. Majken skriver att arean är 4x + 5 cm². '
                    'Hur många cm² för liten blir hennes area?')},
    '1.23': {'t': p('Bestäm k så att \\(6(2a-3)-ka\\) har samma värde för alla a. Vilket är det värdet?'),
             'kg': 'Skriv k först och sedan uttryckets värde.'},
    '1.82': {'t': p('Vilket påstående om \\(5x-3(x-2)\\) stämmer för alla x?')},
    '1.148': {'t': p('Nora skriver −2(x − 6) = −2x − 12. Vilket påstående stämmer?')},
    '1.154': {'t': p('En kvadrat har sidan x + 2 cm, där x &gt; 0. Isak skriver att omkretsen är 4x + 2 cm. För vilket x är hans '
                     'omkrets hälften av den verkliga?')},
    '1.196': {'t': p('Lova utvecklar k(2x − 1) till 10x − 1. Finns det något tal k som gör detta rätt för alla x? Motivera ditt '
                     'svar utan att bara pröva enstaka x-värden.')},
    '1.413': {'t': p('Bestäm talen a och b så att \\(-2(4y-7)=ay+b\\) gäller för alla y.'), 'kg': 'Skriv a och b i var sitt fält.'},
    '1.966': {'t': p('Sam faktoriserar −3x + 6 som −3(x + 2). Hur kan man kontrollera att det är fel?')},
    '1.967': {'t': p('Mira skriver x² + x = x · x. Hur mycket större är vänsterledet än högerledet när x = 7?')},
    # ---------------------------------------------------------------- faktorisering
    '1.26': {'t': p('Antag att x &gt; −4. Rektangeln har arean \\(6x+24\\) cm² och ena sidan är 6 cm. Skriv ett förenklat uttryck '
                    'för den andra sidan.') + SMAL},
    '1.27': {'t': p('Bryt ut 3x ur 12x² − 9x.'), 'kg': 'Skriv bara det som står i parentesen.'},
    '1.87': {'t': p('Uttrycket \\(8a(b-2)+12(b-2)\\) ska skrivas som 4(b − 2) gånger en faktor utan parenteser. Vilken är faktorn?')},
    '1.89': {'t': p('Leila skriver') + p('\\(24x^2y+18xy^2=6xy(4x+3y).\\)') +
             p('Är faktoriseringen rätt, och är uttrycket faktoriserat så långt som möjligt? Motivera ditt svar.')},
    '1.258': {'t': p('Sixten bryter ut 3 ur 18x + 30 och får 3(6x + 10). Är svaret rätt? Har han brutit ut den största gemensamma '
                     'faktorn? Förklara skillnaden mellan de två frågorna.')},
    '1.261': {'t': p('Bryt ut en faktor ur −14x² + 21x så att den första termen i parentesen blir 2x.'),
              'kg': 'Skriv faktorn och det som står i parentesen i var sitt fält.'},
    '1.437': {'t': p('Lös ekvationen 6x² = 9x genom att först bryta ut den största gemensamma faktorn ur 6x² − 9x.'),
              'kg': 'Skriv faktorn med positiv talfaktor, sedan det som står i parentesen och sist lösningarna, den minsta först.'},
    # ---------------------------------------------------------------- intervall
    '1.54': {'t': p('Bilen får stå på en parkering längre än 0 timmar men högst 12 timmar. Beskriv alla tillåtna tider t med '
                    'olikhetstecken.')},
    '1.118': {'t': p('Vilka två av talen −2, 0, 5 och 7 uppfyller \\(-2&lt;x\\le5\\)?'), 'kg': ORDNING},
    '1.121': {'t': p('En givare fungerar när \\(-20&lt;T\\le50\\), där T är temperaturen i °C. Vilken beskrivning stämmer?')},
    '1.122': {'t': p('Ett transportband får gå med hastigheten \\(30\\le v\\le70\\) meter per minut. Vilken är den största '
                     'tillåtna hastigheten?')},
    '1.123': {'t': p('En våg ger tillförlitliga mätningar för \\(80\\le m\\le600\\) gram. Hampus påstår: ”Om en massa inte kan '
                     'mätas tillförlitligt så är den större än 600 gram.” Har han rätt? Beskriv alla positiva massor utanför '
                     'mätområdet.')},
    '1.227': {'t': p('Lisa skriver att motsatsen till \\(-3\\le x&lt;5\\) är \\(-3&gt;x\\ge5\\). Förklara vad som är fel och '
                     'beskriv de tal som inte uppfyller det första villkoret.')},
    '1.229': {'t': p('Viggo säger: ”Intervallet \\(0\\le x\\le12\\) innehåller 13 tal.” När stämmer påståendet och när stämmer det '
                     'inte?')},
    '1.232': {'t': p('Vilka två heltal uppfyller \\(1{,}5\\le x&lt;3{,}5\\)?'), 'kg': ORDNING},
    '1.932': {'t': p('Vilka av talen 1, 2, 3, 4 och 5 är större än 3?'), 'kg': ORDNING},
    '1.933': {'t': p('Vilken beskrivning betyder att x är minst 7?')},
    '1.939': {'t': p('Du har fått lösningen \\(x\\ge5\\) till en olikhet. Vilket påstående beskriver lösningen?')},
    '1.1067': {'t': p('Vilket av talen tillhör intervallet \\(2&lt;x\\le5\\)?')},
    # ---------------------------------------------------------------- linjära olikheter
    '1.59': {'t': p('Vilka tre av talen 1, 2, 3, 4 och 5 uppfyller inte \\(3x-2&gt;7\\)?'), 'kg': ORDNING},
    '1.60': {'t': p('Mira har fått 12 och 17 poäng på två prov. På det tredje provet kan hon få ett helt antal poäng mellan 0 och 30. '
                    'Medelvärdet för de tre proven ska vara minst 15 men mindre än 18. Vilken är den lägsta och den högsta '
                    'poäng hon kan få på det tredje provet?'), 'kg': 'Skriv den lägsta poängen först.'},
    '1.66': {'t': p('Elsa löser \\(-3x&lt;12\\) och skriver \\(x&lt;-4\\). Förklara vad som är fel. Vilka x uppfyller olikheten? '
                    'Ge ett tal som visar att Elsas svar inte kan stämma.')},
    '1.132': {'t': p('Aktivitet A kostar 90 + 6x kr och aktivitet B kostar 30 + 9x kr, där x är antalet deltagare. A ska vara '
                     'billigare än B, och båda priserna ska vara högst 270 kr. Hur många deltagare kan det som minst och som '
                     'mest vara?'), 'kg': 'Skriv det minsta antalet först.'},
    '1.245': {'t': p('Oliver påstår att lösningen till \\(6-2(3x+1)&gt;-8\\) är x &lt; 2. Han testar x = 0 och säger att testet '
                     'bevisar svaret. Bedöm både hans svar och hans motivering.')},
    '1.247': {'t': p('Tindra får x ≤ 3 som lösning till \\(3-4(x-1)\\ge2x-11\\). Sedan skriver hon att det största tillåtna talet '
                     'är 2, eftersom ”gränsen aldrig räknas”. Bedöm båda delarna av hennes lösning.')},
    '1.951': {'t': p('Utgå från en sann olikhet a &lt; b. Malte säger: ”Om båda talen kvadreras är a² &lt; b² fortfarande sant.” '
                     'Undersök påståendet när båda talen är positiva, när båda är negativa och när de har olika tecken. När är '
                     'a² mindre än, lika med eller större än b²?')},
    '1.956': {'t': p('Rut prövar x = 6 i \\(2x+1&gt;9\\) och säger sedan att lösningen är x = 6. Vad visar hennes prövning? '
                     'Bestäm alla lösningar.')},
    '1.958': {'t': p('Arvid säger att det minsta talet som uppfyller x &gt; 2 är 2,1. Har han rätt om x är ett heltal? Har han rätt '
                     'om x får vara vilket tal som helst?')},
    # ---------------------------------------------------------------- linjära ekvationer
    '1.113': {'t': p('Klara skriver 4(x − 3) = 20 och sedan 4x − 3 = 20. Vad ska det stå i stället för 4x − 3?')},
    '1.200': {'t': p('Daniel löser 3x + 6 = 18 genom att skriva x + 2 = 6. Vilken förklaring stämmer?')},
    '1.274': {'t': p('Lovisa vill lösa 3x + 5 = 3x + 8. Vilken slutsats stämmer?')},
    '1.1520': {'t': p('Vågen är i jämvikt. Alla paket väger lika mycket, \\(x\\) kg.') + FIG + p('Hur mycket väger ett paket?')},
    '1.1521': {'t': p('Rektangeln har omkretsen 34 cm.') + FIG + p('Hur lång är sidan \\(x\\)?')},
    '1.1522': {'t': p('Vinklarna i triangeln är \\(x\\), \\(2x\\) och 60°.') + FIG + p('Hur stor är vinkeln \\(x\\)?')},
    '1.1523': {'t': p('Det finns paket på båda sidor av vågen, och den väger jämnt. Varje orange paket väger \\(x\\) kg.') + FIG +
               p('Hur mycket väger ett paket?')},
    '1.1525': {'t': p('Ett gym tar 250 kr i startavgift och 99 kr per månad. Emma har betalat 1 834 kr totalt. Hur många månader '
                      'har hon varit medlem?')},
    '1.1528': {'t': p('Elias löser en ekvation så här:') + FIG + p('Vilket steg är fel?')},
    '1.1529': {'t': p('Mamma är tre gånger så gammal som Liv. Tillsammans är de 68 år. Hur gammal är Liv?')},
    '1.1530': {'t': p('En rektangel är 5 cm längre än den är bred. Omkretsen är 90 cm.') + FIG + p('Hur bred är rektangeln?')},
    '1.1562': {'t': p('Lös ekvationen \\(3(2x-1)-4(x-3)=20\\).')},
    '1.1564': {'t': p('Lös ekvationen \\(0{,}6(x+5)=0{,}2x+4{,}4\\).')},
    # ---------------------------------------------------------------- ekvationer, problemlösning
    '1.202': {'t': p('En rektangels omkrets är 46 cm. Linn påstår att sidorna kan vara 9 cm och 14 cm. Adam föreslår 8 cm och 15 cm. '
                     'Hur många av förslagen har rätt omkrets?')},
    '1.469': {'t': p('Abonnemang A kostar 99 + 0,80x kr och B kostar 179 + 0,30x kr, där x är samtalstiden i minuter. Man betalar '
                     'också för delar av minuter. Du har 220 kr. Vilket abonnemang ger längst samtalstid, och hur många minuter '
                     'blir det?'), 'kg': 'Skriv A eller B i det första fältet och antalet minuter i det andra.'},
    '1.471': {'t': p('En låda innehåller 26 mynt, enkronor och femkronor. Vilket av beloppen 78 kr, 79 kr, 80 kr och 81 kr kan '
                     'mynten vara värda tillsammans?')},
    '1.474': {'t': p('Två bilar startar samtidigt från två orter som ligger 300 km från varandra och kör mot varandra. Den ena '
                     'håller farten 80 km/h och den andra 100 km/h.', 'Efter hur många timmar möts de?'),
              'kg': 'Svara med två decimaler.'},
    '1.478': {'t': p('En båt kör 24 km medströms på 2 timmar och samma sträcka tillbaka, motströms, på 3 timmar.',
                     'Båtens fart i vattnet och strömmens fart är desamma under båda resorna. Hur fort går båten i stilla '
                     'vatten, och hur fort rör sig strömmen?'), 'kg': 'Skriv båtens fart först.'},
    '1.972': {'t': p('En rektangel har omkretsen 50 cm. Längden är 15 cm.', 'Hur bred är rektangeln?')},
    '1.974': {'t': p('En taxiresa kostar 45 kr i grundavgift plus 14 kr per kilometer. En resa kostade 283 kr.',
                     'Hur många kilometer var resan?')},
    '1.977': {'t': p('I en likbent triangel är den tredje vinkeln 40°.', 'Hur stor är var och en av de två lika stora vinklarna?')},
    '1.979': {'t': p('Tre vänner delar lika på en restaurangnota. Dessutom lägger var och en till 20 kr i dricks. Var och en betalar '
                     'då 145 kr.', 'Hur mycket var notan utan dricks?')},
    '1.984': {'t': p('En rektangel är 4 cm längre än den är bred. Omkretsen är 64 cm.', 'Hur stor är rektangelns area?')},
    '1.987': {'t': p('Elavtal A kostar 39 kr per månad plus 1,20 kr per kWh. Elavtal B kostar 99 kr per månad plus 0,95 kr per kWh.',
                     'Vid hur många kWh per månad kostar avtalen lika mycket?')},
    '1.988': {'t': p('Ett tåg kör 30 km/h fortare än en buss. Tåget behöver 2 timmar och bussen 3 timmar för samma sträcka.',
                     'Hur lång är sträckan?')},
    '1.995': {'t': p('Ett rep som är 12 m långt delas i tre bitar. Den andra biten är 1,5 m längre än den första, och den tredje är '
                     'dubbelt så lång som den första.', 'Hur lång är den längsta biten?')},
    '1.1013': {'t': p('Jobb A ger 24 000 kr i månadslön. Jobb B ger 18 000 kr i grundlön plus 6 % av det du säljer för under '
                      'månaden.', 'Hur mycket måste du sälja för under en månad för att jobben ska ge lika mycket?')},
    '1.1018': {'t': p('Två tåg är 415 km från varandra och kör mot varandra. Det ena kör 110 km/h och startar 30 minuter före det '
                      'andra, som kör 130 km/h.', 'Hur långt från sin startpunkt har det långsammare tåget kört när tågen möts?')},
    '1.1026': {'t': p('Sofia cyklar till skolan. Om hon håller 15 km/h kommer hon 10 minuter för sent. Om hon håller 20 km/h kommer '
                      'hon 5 minuter för tidigt.', 'Hur lång är vägen till skolan?')},
    '1.1027': {'t': p('En båt åker 24 km uppströms på 3 timmar. Samma sträcka nedströms tar 2 timmar. Båtens fart i stilla vatten '
                      'är densamma hela tiden.', 'Hur fort rör sig strömmen?')},
    '1.1679': {'t': p('Två elevföreningar har tillsammans 5 000 kr i sina kassor. Musikföreningen använder 25 % av sina pengar till '
                      'en spelning. Samtidigt får filmföreningen ett bidrag på 600 kr. Därefter har föreningarna lika mycket '
                      'pengar.', 'Hur mycket pengar hade musikföreningen från början?') + '[F1]'},
    '1.1680': {'t': p('En jacka kostar 240 kr mer än en väska före rabatterna. På rean är rabatten 20 % på jackan och 10 % på väskan. '
                      'När båda köps får kunden dessutom dra av en kupong på 150 kr från den rabatterade summan. Kunden betalar '
                      '1 164 kr.', 'Vad kostade jackan före rabatterna?') + '[F1]'},
    '1.1681': {'t': p('En rektangulär hage delas i två med ett stängsel tvärs över bredden. Längden är 4 m längre än dubbla bredden. '
                      'I ytterkanten finns en grind som är 2 m bred och som inte behöver något stängsel. Mellanstängslet har '
                      'ingen grind.', 'Totalt används 90 m stängsel, mellanstängslet inräknat. Hur lång är hela hagen?') + '[F1]'},
    '1.1683': {'t': p('Nora startar kl. 09.00 och cyklar med farten 15 km/h. Efter 30 minuter stannar hon i 10 minuter och fortsätter '
                      'sedan i samma fart. Sam startar kl. 09.20 från samma plats och följer samma väg med farten 24 km/h utan '
                      'paus.', 'Hur många minuter efter kl. 09.00 hinner Sam ikapp Nora första gången?') + '[F1]'},
    '8.04': {'t': p('En verkstad köper två likadana förvaringslådor. Frakten är 35 kr och hela beställningen kostar 185 kr. Vad '
                    'kostar en låda?')},
    # ---------------------------------------------------------------- ekvationer med bråk och parenteser
    '1.1095': {'t': p('Theo löser \\(\\frac{x}{3}+2=5\\) genom att multiplicera båda leden med 3 och skriver \\(x+2=15\\). Vad är '
                      'fel?')},
    '1.1113': {'t': p('En pool kan fyllas med en stor slang på 6 timmar eller med en liten slang på 9 timmar.',
                      'Hur många timmar tar det om båda slangarna används samtidigt?')},
    '1.1194': {'t': p('Elin löser ekvationen \\(3(x-2)=12\\) så här:') +
               p('Steg 1: \\(3x-2=12\\)<br>Steg 2: \\(3x=14\\)<br>Steg 3: \\(x=\\dfrac{14}{3}\\)') + p('Vilket steg är fel?')},
    '1.1396': {'t': p('En rektangel förlängs åt höger utan att höjden ändras. Den tillagda ytan är 56 cm². Längderna i figuren är i '
                      'cm.') + FIG + p('Bestäm \\(x\\).')},
    '1.1399': {'t': p('Talet \\(a\\) ska väljas så att de två ekvationerna får samma lösning \\(x\\).') +
               '\\[3(x-2)-2(1-x)=a+4\\]\\[2\\bigl(3-(x-1)\\bigr)=x+2a\\]' + p('Bestäm \\(a\\). Svara exakt.')},
    '1.1400': {'t': p('Ekvationen är') +
               '\\[\\begin{aligned}&\\frac23\\left(3x-\\frac{x-2}{4}\\right)\\\\&\\quad-\\frac12\\left(x-\\frac{2x+1}{3}\\right)=\\frac{x+5}{2}.\\end{aligned}\\]' +
               p('Bara talet 5 i högerledet ska bytas ut, så att lösningen x blir precis 1 mindre än förut. Vilket tal ska stå '
                 'i stället för 5? Svara exakt.')},
    # ---------------------------------------------------------------- algebraiska uttryck och mönster
    '1.907': {'t': p('Vilket påstående om x² och 2x stämmer när x = 3?')},
    '1.1549': {'t': p('Ali är \\(a\\) år. Bea är 4 år äldre än Ali. Cem är dubbelt så gammal som Bea. Skriv ett förenklat uttryck för '
                      'hur gamla de är tillsammans.')},
    '1.1500': {'t': p('Figurerna är byggda av prickar.') + FIG + p('Hur många prickar har figur 4?')},
    '1.1501': {'t': p('Husen byggs av tändstickor. Hus som står bredvid varandra delar vägg.') + FIG +
               p('Hur många tändstickor behövs till figur 4?')},
    '1.1502': {'t': p('Tabellen visar ett mönster.') + '[F1]' + p('Hur många har figur 6?')},
    '1.1504': {'t': p('Talföljden 1, 3, 9, 27, … fortsätter på samma sätt. Vilket är nästa tal?')},
    '1.1505': {'t': p('Vilket tal saknas i talföljden 3, 7, __, 15, 19?')},
    '1.1506': {'t': p('Prickarna bildar trianglar.') + FIG + p('Hur många prickar har figur 5?')},
    '1.1507': {'t': p('Kvadratiska bord ställs i en rad. Figuren visar hur många som får plats.') + FIG +
               p('Hur många personer får plats vid 10 bord i rad?')},
    '1.1508': {'t': p('En gång läggs med plattor. Figur n har \\(4n+2\\) plattor. Vilket nummer har den figur som har 50 plattor?')},
    '1.1509': {'t': p('Trianglar läggs i en rad av tändstickor. Trianglar som ligger bredvid varandra delar en sticka.') + FIG +
               p('Figur n har n trianglar. Hur många stickor behövs till figur 25?')},
    '1.1510': {'t': p('Ett staket byggs i sektioner. Mellan två stolpar sitter två brädor.') + FIG +
               p('Hur många stolpar behövs för ett staket med 9 sektioner?')},
    '1.1511': {'t': p('Ett pärlband följer mönstret röd, blå, blå, röd, blå, blå, …') + FIG + p('Vilken färg har pärla nummer 50?')},
    '1.1512': {'t': p('Antalet stickor i figur n är \\(7n+3\\). Hur många stickor tillkommer för varje ny figur?')},
    '1.1516': {'t': p('Ett ljus är 30 cm långt och blir 1,5 cm kortare varje timme. Hur långt är ljuset efter 8 timmar?')},
}
