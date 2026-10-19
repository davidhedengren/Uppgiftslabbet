# Mato1: primitiva funktioner med villkor – 2026-10-19

49 uppgifter i området lästa med fråga, lösning, ledtråd och metadata. Dessutom två följdfynd i andra områden: totalt 51 granskade huvuduppgifter, 19 ändrade och 32 oförändrade. Hela Mato1 är inte färdiggranskad.

## Ändringar
- **3.22**: Generisk ledtråd ersatt med uppgiftens konkreta villkor.
- **3.28**: Generisk ledtråd ersatt med uppgiftens konkreta villkor.
- **3.34**: Generisk ledtråd ersatt med uppgiftens konkreta villkor.
- **3.154**: Generisk ledtråd ersatt med uppgiftens konkreta villkor.
- **3.166**: Generisk ledtråd ersatt med uppgiftens konkreta villkor.
- **3.186**: Ledtråden gällde potensintegrering trots att inget funktionsuttryck ges.
- **3.220**: De båda extremvärdena är lokala; polynomet har inga globala extremvärden.
- **3.310**: Generisk ledtråd ersatt med uppgiftens konkreta villkor.
- **3.313**: Globalt minimum finns inte för kubiken. Villkor och lösning preciseras till lokalt minimum.
- **3.354**: Generisk ledtråd ersatt med uppgiftens konkreta villkor.
- **3.422**: Ledtrådens obekanta notation F_C ersatt med uppgiftens F.
- **3.898**: Riktning och tidsenhet saknades. Förklarar skillnaden mellan förflyttning och avstånd från startlinjen.
- **3.899**: Tidens enhet uttalad och volymberäkningen förklarad.
- **3.944**: Närliggande tankuppgift varierad: bestäm startvolym från slutvolym i stället för ytterligare talbyte i framåträkning.
- **3.1011**: Fullprecisionsmål och halv hundradels tolerans i stället för avrundat mål med hel hundradels tolerans.
- **3.1074**: Lång sammanhängande formel delas i läsbara mellanled. Tidigare variationsbeslut och svar 6 bevaras.
- **3.1147**: Exakt bråksvar i stället för tolerans som godkände avrundade svar. Kortare lösningsrader. C/4 efter sammansatt men standardmässig tangentanalys.
- **3.1100**: Följdfynd: samma saknade riktning och tidsenhet som 3.898. Korrekt svar bevarat.
- **3.1014**: Följdfynd: samma saknade riktning och tidsenhet som 3.898. Korrekt svar bevarat.

## Utan ändring
3.81, 3.88, 3.158, 3.170, 3.212, 3.224, 3.240, 3.281, 3.311, 3.312, 3.314, 3.353, 3.418, 3.423, 3.615, 3.616, 3.619, 3.641, 3.741, 3.800, 3.813, 3.825, 3.832, 3.861, 3.862, 3.874, 3.875, 3.945, 3.1010, 3.1012, 3.1013, 3.1156.

## Bedömning
Primitiva funktioner kontrollerade genom termvis derivering och insättning av givna värden. Alla befintliga matematiska slutsvar i området stämmer; i 3.313 var det själva existensvillkoret som var felaktigt formulerat. 3.220 förtydligas av samma skäl. 3.944 ändrar avsiktligt frågeriktning och därmed svar från 29 till 20 liter för större variation. 3.1011 bevarar rätt avrundat svar 5,72 men använder nu full precision och tolerans 0,005. 3.1147 kräver 4/3 eller ekvivalent exakt uttryck; 1,333 underkänns.

3.1147 bedöms C/nivå 4: eleven kombinerar integration, derivatans nollställe och tangentvillkoret, men behöver ingen generell parameteranalys eller ny strategi på A-nivå. Övriga nivåer bevaras efter kontroll. Nivå 1 finns i 3.825 och 3.1156; rutinuppgifter med integration plus villkor behåller nivå 2.

Verktyg: inga flaggor ändrade. Enkla småtalskort utan räknare kräver bara huvudräkning; övriga tillåter miniräknare. GeoGebra behövs inte eftersom symbolisk integration och tolkning av villkor prövas. Området har inga separata spelDelar; samtliga faktiska kort renderas i browser-testet.

De befintliga figurerna i 3.353 och 3.354 stämmer med x²+3 respektive x³+1 och punkterna (1,4)/(1,2), och har granskats visuellt. Ingen ny figur tillför avgörande information i de korta algebraiska villkorsuppgifterna. Bilens riktning beskrivs uttryckligen; tankens enkla inflöde förklaras i lösningen.

Liknande fall: 3.338, 3.364, 3.719, 3.43, 3.49, 3.93, 3.257, 3.06, 3.12, 3.30, 3.60, 3.66. Jämförelser är inte fullständig granskning av deras områden. FP54/55/58:s avrundningsprinciper används. FP60:s skillnad mellan givna data och dolda antaganden följs. 3.1074:s tidigare variation enligt MATO1_KALIBRERING_2026-10-08 bevaras.

## Verifiering
Riktiga svarsfält testas med korrekta och felaktiga svar, ekvivalenta uttryck, enhetsbyte och exakt/avrundat svar. Samtliga 51 uppgifter renderas på 390 och 1280 px. Kontroll av JavaScript, KaTeX, sidbredd, intern formelklippning, SVG-etiketter och verktygsflaggor. 428 mastertester och 178 konsumenttester passerar; 56 faktiska svarskontroller och 102 kortvyer passerar utan fynd. Separata granska-svg CLI-suiten undantagen på grund av tidigare miljötimeout; figurernas rendering kontrolleras i appen.

Master/konsument jämförda före synk. Inga rapportstatusar ändrade i databasen.
