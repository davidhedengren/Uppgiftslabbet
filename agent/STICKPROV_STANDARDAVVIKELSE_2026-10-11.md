# Stickprov, urval och standardavvikelse – 2026-10-11

**177 uppgifter granskade: 41 åtgärdade/förtydligade och 136 granskade utan ändring.** Åtgärdad omfattar även pedagogik, nivå och kortmetadata; det betyder inte att alla 41 hade ett felräknat facit.

## Omfattning

Helbankssökning i sju banker efter stickprov, urval och standardavvikelse. Samtliga 54 ursprungliga uttryckliga stickprovsträffar samt hela ma1-områdena urvalsmetoder/signifikans, hela ma2-standardavvikelse och relaterade frågor. Detta slutmarkerar inte övriga delar av bankerna.

Samtliga sju banker söktes. Träffar på biologisk populationstillväxt, vektorkomponenten s_x och redan givna normalfördelningsparametrar har skilts från statistiska rådatastickprov. Vätskeprovet fy1 #2.175 är genomläst som densitetsuppgift, inte som statistisk Sx-fråga. Fördelning: ma1 128, ma2 47, fy1 1 och matf1 1. Sökningen gav inga ytterligare uttryckliga stickprovsuppgifter i fy2, mato1 eller mato2.

De granskade uppgifterna är manuellt genomlästa för det angivna innehållet. Självrättning och mobil-/datorvisning kontrolleras även automatiskt. Tidigare beslut i FP27/FP28 har lästs; #4.299 d:s 0,55 s, #4.302:s nollspridningsundantag och #4.306:s uttryckliga Sx bevaras. Inga SVG-figurer ändras.

## Viktiga beslut och analoger

- **σx eller Sx:** mätvärden är inte automatiskt en fråga om skattning av en population. σx beskriver hela den givna värdelistan; Sx används här när stickprovet ska uppskatta populationens spridning. Ange målet. Granskade analoger: ma2 #4.05/#4.10/#4.28/#4.46/#4.97/#4.157/#4.306/#5.66/#5.71/#5.94/#5.110. Vid redan givna normalparametrar behövs ingen n−1-omräkning.
- **Precision och fel mått:** #4.299:s tidigare toleranser släppte igenom Sx trots att σx efterfrågades. Detta nya belägg ersätter FP28:s beslut att behålla toleranserna. Fullprecisionsmål och 0,005 används för två decimaler. Kontrollera korrekt avrundning, extra precision, nästa felaktiga avrundning och fel mått. Analoger #4.28/#4.157/#4.302/#5.71/#5.94 samt fy1 #2.175.
- **Hela personer och viktning:** ma1 #5.571:s gamla exakta procentsiffror krävde 19,2 och 12,6 elever. Nu är urvalet 32/28/20 och ja-svaren 20/14/6, totalt 50,0 %. Ovägt medelvärde 47,5 % är fel. Fem kontrollanalogier med giltiga heltalsantal: #5.11/#5.60/#5.99/#5.105/#6.93.
- **Namngivna fält på varje kort:** ma2 #4.241 är ordnad också efter uppdelning. Jämförelser #4.299/#4.302/#5.71/#5.94/#5.110 och ma1 #5.99/#5.571. Rötter ska fortfarande kunna vara oordnade där frågan tillåter det.
- **Målgrupp och faktisk svarstäckning:** ma1 #5.182/#5.221/#5.526/#5.535 anger målgruppen; #5.102 a anger att alla faktiskt svarar. Att alla får en enkät är inte samma sak. Kontrollanalogier #5.09/#5.104/#5.107/#5.108/#5.563/#5.106.
- **Bortfall, självurval och signifikans:** bortfall är uteblivna svar, inte automatiskt bortfallsfel. Självurval behandlas separat. Signifikans är inte sannolikheten att en hypotes är sann och säger inte att skillnaden är stor. Analoger #5.64/#5.106/#5.225/#5.529/#5.533/#5.536 och #5.90/#5.92/#5.93/#5.94/#5.96/#5.98/#5.207/#5.211.
- **Pedagogik och självständighet:** #5.97:s ledtrådar avslöjar inte båda delarnas svar. #4.241 visar kvadratsummornas beräkning och ger a endast relevant information. #4.283/#4.284 får mobilanpassade beräkningar med nödvändiga mellanled kvar. #5.175/#5.179/#5.181/#5.183 får egna förklaringar i stället för en gemensam nyckelidé; fem jämförelser #5.117/#5.176/#5.177/#5.178/#5.530.

## Verifiering

- Master: 40/40 riktade enhetstester inklusive tidigare regressioner. Konsument: 121/121 enhetstester.
- Verkliga svarsfält: 50 oberoende korrekt-/felaktig-svar-kontroller samt 149 facitbaserade kontraktskontroller. De senare testar parsern och fälten, inte facits matematiska riktighet; oberoende beräkningsmodeller och manuell genomläsning används för matematiken.
- 388 kortvisningar på mobil (390 px) och dator (1280 px), med riktig KaTeX: inga råa formelkoder, formel-/tabellöverbredd eller JavaScript-fel. Utvalda mobilkort har också kontrollerats visuellt.
- Tidigare webbläsarregressioner: 86 rättningskontroller, 8 kortfacitvisningar och 58 mobil-/datorvisningar.
- Helbankens strukturella validator ger inga nytillkomna fynd jämfört med baslinjen. Befintliga fynd utanför denna granskning är inte slutmarkerade.
- Reproducerbara skydd: master `tools/stickprov-standardavvikelse.test.js`, konsument `tools/stickprov-standardavvikelse.browser.py` och regressionerna för 16:18/17:49. Browsern gör inga XP- eller databasskrivningar.
- Kommentarerna nedan är förslag att använda i rapportvyn. Ingen rapportstatus eller kommentar har skrivits till Supabase.

## Alla granskade uppgifter

| Kurs | Antal | Granskade ID |
|---|---:|---|
| ma1 | 128 | #5.09, #5.10, #5.11, #5.27, #5.28, #5.29, #5.30, #5.60, #5.61, #5.62, #5.63, #5.64, #5.65, #5.66, #5.90, #5.91, #5.92, #5.93, #5.94, #5.95, #5.96, #5.97, #5.98, #5.99, #5.100, #5.101, #5.102, #5.103, #5.104, #5.105, #5.106, #5.107, #5.108, #5.109, #5.110, #5.111, #5.112, #5.113, #5.114, #5.115, #5.116, #5.117, #5.118, #5.174, #5.175, #5.176, #5.177, #5.178, #5.179, #5.180, #5.181, #5.182, #5.183, #5.206, #5.207, #5.208, #5.209, #5.210, #5.211, #5.212, #5.213, #5.214, #5.215, #5.216, #5.217, #5.218, #5.219, #5.220, #5.221, #5.222, #5.223, #5.224, #5.225, #5.228, #5.280, #5.281, #5.282, #5.283, #5.284, #5.511, #5.514, #5.518, #5.519, #5.520, #5.521, #5.522, #5.523, #5.524, #5.525, #5.526, #5.527, #5.528, #5.529, #5.530, #5.531, #5.532, #5.533, #5.534, #5.535, #5.536, #5.537, #5.538, #5.539, #5.540, #5.541, #5.542, #5.543, #5.544, #5.545, #5.546, #5.547, #5.548, #5.549, #5.550, #5.551, #5.552, #5.553, #5.554, #5.555, #5.563, #5.564, #5.565, #5.566, #5.567, #5.571, #6.40, #6.93, #6.137 |
| ma2 | 47 | #4.04, #4.05, #4.10, #4.14, #4.21, #4.28, #4.35, #4.36, #4.43, #4.46, #4.49, #4.56, #4.65, #4.68, #4.75, #4.84, #4.86, #4.90, #4.93, #4.97, #4.102, #4.106, #4.109, #4.114, #4.121, #4.156, #4.157, #4.173, #4.174, #4.175, #4.195, #4.201, #4.211, #4.212, #4.213, #4.235, #4.236, #4.241, #4.283, #4.284, #4.299, #4.302, #4.306, #5.66, #5.71, #5.94, #5.110 |
| fy1 | 1 | #2.175 |
| matf1 | 1 | #1.103 |

## Åtgärdade och förtydligade – kommentarsförslag

| Kurs/ID | Ändrade fält | Förslag på kommentar |
|---|---|---|
| fy1 #2.175 | rättSvar, tolerans, traningsniva | Vätskeprovet är en densitetsuppgift, inte en Sx-beräkning. Fullprecisionsmål 5142,857… kg med tolerans 5 kg godtar 5140 och extra precision; uppgiften kalibreras till E/nivå 2. |
| ma1 #5.63 | s | Facit skiljer nu tydligt mellan två felkällor: tidpunkten och vilka invånare som nås. Varje felkälla har en egen förbättring. |
| ma1 #5.65 | niva, poang, t, formaga, traningsniva | Population, stickprov och skälet till urval är grundläggande begrepp: E/nivå 2. Frågan säger personer, eftersom urvalet är 15-åringar, inte enbart elever. |
| ma1 #5.91 | s | Facit förklarar gruppstorlekens betydelse genom mindre slumpvariation i medelvärden, utan att ge en sannolikhet för att hypotesen är sann. |
| ma1 #5.97 | ledtrad, spelDelar | Ledtrådarna ger nu en relevant tankefråga för det aktuella kortet i stället för att tala om svaren på båda delarna. Facit är fortfarande falskt respektive sant. |
| ma1 #5.102 | t, s, traningsniva, spelDelar | Del a anger nu att alla faktiskt svarar. Då är ja entydigt; att bara skicka en enkät till alla garanterar inte representativa svar. Grundläggande bedömning är nivå 2. |
| ma1 #5.106 | niva, poang, traningsniva | Grundläggande tolkning av urval eller slumpvariation kalibreras från C till E/nivå 2. Svaret och motiveringen är oförändrade. |
| ma1 #5.174 | t, s | Självurval skiljs nu från bortfall. De elever som själva väljer att svara kan skilja sig från övriga elever. |
| ma1 #5.175 | s | Facit förklarar nu varför vågens återkommande fel på +0,4 kg är systematiskt. Rätt alternativ C är oförändrat. |
| ma1 #5.179 | s | Facit förklarar hur olika avläsningar gör mätvärdet osäkert och skiljer detta från urvalsfel. Rätt alternativ C är oförändrat. |
| ma1 #5.180 | t, s | Uteblivna svar kallas bortfall. Facit skiljer det från bortfallsfel, som uppstår om bortfallet snedvrider resultatet. |
| ma1 #5.181 | s | Facit förklarar att centimetermarkeringar inte ger stöd för fyra decimaler. Rätt alternativ B är oförändrat. |
| ma1 #5.182 | t, s | Målgruppen är nu uttryckligen alla kommuninvånare. Facit förklarar varför den begränsade gruppen kan ge ett snedvridet urval. |
| ma1 #5.183 | s | Facit kopplar de olika instruktionerna till möjlig påverkan på testresultaten. Rätt alternativ B är oförändrat. |
| ma1 #5.215 | niva, poang, traningsniva | Grundläggande tolkning av urval eller slumpvariation kalibreras från C till E/nivå 2. Svaret och motiveringen är oförändrade. |
| ma1 #5.221 | t, s | Målgruppen är nu uttryckligen alla kommuninvånare. Facit förklarar varför den begränsade gruppen kan ge ett snedvridet urval. |
| ma1 #5.228 | niva, poang, traningsniva | Grundläggande tolkning av urval eller slumpvariation kalibreras från C till E/nivå 2. Svaret och motiveringen är oförändrade. |
| ma1 #5.281 | niva, poang, traningsniva | Grundläggande tolkning av urval eller slumpvariation kalibreras från C till E/nivå 2. Svaret och motiveringen är oförändrade. |
| ma1 #5.511 | traningsniva | En direkt begreppsfråga kalibreras till nivå 1. Rätt svar är oförändrat. |
| ma1 #5.525 | traningsniva | En direkt begreppsfråga kalibreras till nivå 1. Rätt svar är oförändrat. |
| ma1 #5.526 | t, s | Målgruppen är nu uttryckligen alla kommuninvånare. Facit förklarar varför den begränsade gruppen kan ge ett snedvridet urval. |
| ma1 #5.527 | traningsniva | En direkt begreppsfråga kalibreras till nivå 1. Rätt svar är oförändrat. |
| ma1 #5.535 | t, s | Målgruppen är nu uttryckligen alla kommuninvånare. Facit förklarar varför den begränsade gruppen kan ge ett snedvridet urval. |
| ma1 #5.544 | t, s | Undersökningarna anges vara oberoende slumpmässiga urval. Facit jämför förändringen med osäkerheten utan en allmän regel om överlappande intervall. |
| ma1 #5.545 | t, s, traningsniva | Signifikans förklaras nu utan att förväxlas med sannolikheten att en verklig skillnad finns. Begreppstolkningen är nivå 2. |
| ma1 #5.547 | t, s | Målgrupp och oberoende slumpmässiga urval anges. Slutsatsen skiljs från en garanti om att inga felkällor finns. |
| ma1 #5.565 | t, s | Den information som behövs om golfklubbens inkomster anges nu i frågan; eleven behöver inte anta en viss grupps ekonomi. |
| ma1 #5.566 | s | Facit lovar inte längre samma urvalssannolikhet för alla elever när antal per skola/program inte anges. |
| ma1 #5.567 | niva, poang, traningsniva | Grundläggande tolkning av urval eller slumpvariation kalibreras från C till E/nivå 2. Svaret och motiveringen är oförändrade. |
| ma1 #5.571 | niva, poang, t, s, traningsniva, rättSvar, tolerans, svarFormat, svarEnhet | Procentsiffrorna i urvalet motsvarar nu hela elever: 20 av 32, 14 av 28 och 6 av 20. Uppskattningen blir 50,0 %. Viktning förklaras med antal ja-svar; uppgiften kalibreras till C/nivå 3 och procentfältet har rätt enhet. |
| ma2 #4.05 | t, spelIntro, spelDelar | Frågan anger nu σx för spridningen i de givna värdena, så att Sx och σx inte ger två olika möjliga facit. |
| ma2 #4.10 | t, s | Frågan anger nu σx för spridningen i de givna värdena, så att Sx och σx inte ger två olika möjliga facit. |
| ma2 #4.28 | t, s, rättSvar, tolerans, spelIntro, spelDelar | σx anges uttryckligen. Fullprecisionsmål √12 och tolerans 0,05 godtar 3,5 samt extra precision men avvisar 3,4 och 3,6. Facit visar beräkningen. |
| ma2 #4.46 | t, s | Frågan anger nu σx för spridningen i de givna värdena, så att Sx och σx inte ger två olika möjliga facit. |
| ma2 #4.97 | t, s | σx anges och slutberäkningen använder oavrundad standardavvikelse. 3 · 3,35 är 10,05, medan 3√11,25 avrundas till 10,06. |
| ma2 #4.157 | t, s, rättSvar, tolerans | σx och två decimaler anges; rättningen använder √(26/5) och √(26/6) med tolerans 0,005, så rätt avrundning och extra precision godtas. |
| ma2 #4.241 | s, ledtrad, spelDelar | Skrivarnas delkort har nu egna namngivna, ordnade svarsfält. A och B kan inte bytas vid rättningen. Facit visar hur kvadratsummorna 8 och 16 fås och varför A har minst spridning. Del a slipper standardavvikelseformeln som bara behövs i b. |
| ma2 #4.283 | s | Facit delar de breda formlerna i läsbara rader och förklarar bidragen inom och mellan klasserna. Medelvärdet 66 och standardavvikelsen 7 är oförändrade. |
| ma2 #4.284 | s | Facit visar kvadratsumman 64, det nya medelvärdet och varför variansen blir oförändrad för 47 eller 53. Beräkningen delas i korta rader för mobil. Svaret är oförändrat. |
| ma2 #4.299 | t, s, rättSvar, tolerans, spelDelar | σx-frågan godkänner inte längre de andra Sx-värdena genom för bred tolerans. Fullprecision och tolerans 0,005 används. Facit fokuserar på efterfrågat mått; tidigare rättad 0,55 s i d bevaras. |
| ma2 #4.302 | t, rättSvar, tolerans, spelDelar | Fullprecisionsmålen √(34/4) och √(34/5) samt tvådecimalstolerans ersätter grova toleranser. σx och det tidigare nollspridningsundantaget bevaras. |

## Granskad – inget fel – kommentarsförslag

| Kurs/ID | Ändrade fält | Förslag på kommentar |
|---|---|---|
| ma1 #5.09 | Inga | Granskad – inget fel: Morgontid är en systematisk avgränsning. Om morgonkunder skiljer sig från andra kunder riskerar urvalet att inte representera hela dagens kundgrupp. Svar: D. |
| ma1 #5.10 | Inga | Granskad – inget fel: a) Urvalet är inte representativt — hälsomedvetna personer är överrepresenterade, vilket snedvrider resultatet b) Social önskvärdhet. Deltagare kan svara det som anses mer accepterat snarare än sanningen, eftersom svaret inte är anonymt c) Systematiskt mätfel (kalibreringsfel). Alla mätningar blir för höga med samma belopp, vilket skiljer sig från slumpmässig mätosäkerhet |
| ma1 #5.11 | Inga | Granskad – inget fel: Båda studierna visar 5 procentenheters skillnad, men i studie X motsvarar några få personer en stor del av varje grupp. Slumpvariation får därför mycket större betydelse där. Med 2 000 personer per grupp blir andelarna normalt stabilare, så samma observerade skillnad ger starkare statistiskt underlag. |
| ma1 #5.27 | Inga | Granskad – inget fel: Nej. En mycket liten skillnad kan vara statistiskt signifikant, särskilt i en stor undersökning. |
| ma1 #5.28 | Inga | Granskad – inget fel: Styrka: urvalet görs enligt en tydlig regel och väljer inte bara personer undersökaren själv föredrar. Svaghet: endast en ingång och en timme täcks. Besökare vid andra tider eller ingångar kan skilja sig. |
| ma1 #5.29 | Inga | Granskad – inget fel: Populationen är hela den grupp undersökningen vill uttala sig om: alla 16–19-åringar i kommunen. Svar: C. |
| ma1 #5.30 | Inga | Granskad – inget fel: a) En ledande fråga. b) Frasen "tycker du inte också" antyder att det förväntade svaret är ja, vilket kan få fler att svara ja än vad de egentligen tycker — svaren blir snedvridna åt det håll frågan pekar c) Till exempel: "Anser du att kommunen bör satsa mer, mindre eller lika mycket pengar på parker som i dag?" |
| ma1 #5.60 | Inga | Granskad – inget fel: Det nya läkemedlet hjälper 45/60 = 75 %, jämfört med 52/80 = 65 %. En observerad skillnad bevisar inte ensam en säker skillnad i effekt. |
| ma1 #5.61 | Inga | Granskad – inget fel: Större stickprov ger normalt mindre slumpmässig variation i skattade andelar, allt annat lika. Svar: C. |
| ma1 #5.62 | Inga | Granskad – inget fel: Att uppskatta träningsmängd ett helt år bakåt är känsligt för att deltagarna inte minns exakt. Svar: D – minnesfel. |
| ma1 #5.64 | Inga | Granskad – inget fel: När många utvalda personer inte svarar kan de svarande skilja sig systematiskt från dem som inte svarar. Svar: A – bortfallsfel. |
| ma1 #5.66 | Inga | Granskad – inget fel: Det slumpade urvalet från elevregistret ger elever från hela skolan möjlighet att bli valda. Självurval på ett socialt konto kan både missa elever och gynna dem som själva vill svara. Svar: B. |
| ma1 #5.90 | Inga | Granskad – inget fel: Statistisk signifikans handlar om hur förenligt resultatet är med slumpvariation under en statistisk nollmodell. Det säger inte automatiskt att skillnaden är stor, praktiskt viktig eller att urvalet är representativt. Svar: D. |
| ma1 #5.92 | Inga | Granskad – inget fel: Två stickprov från samma population får sällan exakt samma medelvärde. En liten observerad skillnad kan därför uppstå genom slumpvariation även om gruppernas bakomliggande populationer inte skiljer sig. |
| ma1 #5.93 | Inga | Granskad – inget fel: Signifikansen kan säga att skillnaden på 2 procentenheter är svår att förklara med enbart slumpvariation bland de svar som faktiskt samlats in . Den tar däremot inte bort självurvalet. Om forumets användare inte representerar hela befolkningen kan resultatet fortfarande vara systematiskt snedvridet. |
| ma1 #5.94 | Inga | Granskad – inget fel: ”Statistiskt signifikant” betyder inte ”stor”. Med ett mycket stort stickprov kan även 0,4 procentenheters skillnad bli statistiskt tydlig, men den praktiska betydelsen kan ändå vara liten. |
| ma1 #5.95 | Inga | Granskad – inget fel: I små stickprov får enskilda observationer stor påverkan och slumpvariation blir större. Svar: C. |
| ma1 #5.96 | Inga | Granskad – inget fel: Med få deltagare kan variationen inom grupperna vara stor i förhållande till antalet observationer. Då blir osäkerheten stor. Svar: Studien kan helt enkelt ha för svagt underlag för att skilja en verklig skillnad från slumpvariation. |
| ma1 #5.98 | Inga | Granskad – inget fel: Nej, informationen räcker inte. Skola A har en större observerad effekt (8 poäng), medan skola B har mycket fler observationer. Båda sakerna kan påverka den statistiska säkerheten. För att bedöma signifikansen behövs också information om exempelvis spridningen i resultaten och hur undersökningen genomfördes. Man kan därför inte avgöra signifikansen enbart från medelvärdesförändringen och antalet elever. |
| ma1 #5.99 | Inga | Granskad – inget fel: Ett urval på 90 av 900 elever är 10 %. Det ger 30, 33 och 27 elever. De tre fälten har namngiven ordning. |
| ma1 #5.100 | Inga | Granskad – inget fel: Genom att dela populationen i relevanta grupper och sedan slumpa inom varje grupp säkerställer man representation samtidigt som urvalet fortfarande bygger på slumpning. Svar: D. |
| ma1 #5.101 | Inga | Granskad – inget fel: Nej. Det ursprungliga urvalet kan vara bra, men olika svarsfrekvens skapar snedvridning på grund av bortfall. Äldre personer riskerar att bli underrepresenterade bland de faktiska svaren. En förbättring är att följa upp grupper med lågt deltagande, använda flera svarssätt och kontrollera hur de svarande fördelar sig jämfört med hela gruppen som undersökningen ska uttala sig om. |
| ma1 #5.103 | Inga | Granskad – inget fel: Med en enda slumpning finns risk att den lilla gruppen 65+ får mycket få deltagare. Genom att välja personer inom varje åldersgrupp säkerställer man att alla viktiga grupper finns representerade och kan jämföras. |
| ma1 #5.104 | Inga | Granskad – inget fel: Urvalsmetoden utesluter elever som går, åker buss eller bil. Därför kan den inte representera hela skolans resvanor. Svar: A. |
| ma1 #5.105 | Inga | Granskad – inget fel: Ett proportionellt urval ger 42, 30 och 18 elever. Därför går det inte samtidigt att kräva minst 25 från varje program med totalt 90 elever. Det är uppgiftens avsedda slutsats. |
| ma1 #5.107 | Inga | Granskad – inget fel: Platsen där urvalet görs gynnar personer som redan ägnar sig åt en fysisk aktivitet. Det kan ge en systematisk överskattning av motionsvanorna. Svar: C. |
| ma1 #5.108 | Inga | Granskad – inget fel: Ett slumpmässigt urval ger alla elever möjlighet att bli valda och minskar systematisk snedvridning. Det garanterar däremot inte att ett enskilt stickprov exakt speglar varje egenskap i populationen. Svar: B. |
| ma1 #5.109 | Inga | Granskad – inget fel: Exempel: • Vilka som väljer att svara: personer som väljer att svara kan ha särskilt starka åsikter. • Utlottningen kan göra att vissa personer svarar främst för tävlingen och kanske inte lika noggrant. QR-koden når dessutom bara personer som faktiskt handlar och får kvitto. |
| ma1 #5.110 | Inga | Granskad – inget fel: Ordet ”utmärkta” värderar kundservicen redan i frågan och kan påverka svaren. Svar: A. |
| ma1 #5.111 | Inga | Granskad – inget fel: Orden ”också” och ”fantastiska” gör frågan ledande. Svar: D. |
| ma1 #5.112 | Inga | Granskad – inget fel: Om en person kan skicka in flera röster får deltagarna olika stor påverkan och resultatet speglar inte längre en röst per person. Svar: C. |
| ma1 #5.113 | Inga | Granskad – inget fel: Mättiden är sannolikt inte representativ för hela veckan. Trafiken kan vara mycket lägre en söndag morgon. En bättre plan är att mäta vid flera tider, veckodagar och gärna under flera veckor . |
| ma1 #5.114 | Inga | Granskad – inget fel: Urvalet är starkt snedvridet: personer som befinner sig vid cykelparkeringar är mycket mer benägna att vara cyklister än kommuninvånare i allmänhet. Ett stort antal svar minskar inte ett systematiskt urvalsfel. Ett bättre upplägg är att slumpa personer från hela målpopulationen, använda flera kontaktvägar och följa upp bortfall. |
| ma1 #5.115 | Inga | Granskad – inget fel: a) Vissa personer kan få större påverkan än andra, så svaren blir inte oberoende bidrag från olika personer. b) Exempelvis unika inloggningar eller engångskoder . |
| ma1 #5.116 | Inga | Granskad – inget fel: Flera saker har ändrats samtidigt: elevgrupperna kan skilja sig, frågorna är andra och provformatet är annat. Svar: Skillnaden kan därför inte säkert kopplas till en enda förklaring. |
| ma1 #5.117 | Inga | Granskad – inget fel: Vågen förskjuter alla mätningar åt samma håll med samma belopp. Svar: D – systematiskt mätfel. |
| ma1 #5.118 | Inga | Granskad – inget fel: De ärenden som tar längst tid har större risk att fortfarande vara öppna och därmed uteslutas. Urvalet av endast avslutade ärenden överrepresenterar snabbare ärenden . Den beräknade genomsnittstiden blir därför sannolikt för låg jämfört med alla kunder. |
| ma1 #5.176 | Inga | Granskad – inget fel: Ordet ”visst” signalerar vilket svar frågeställaren väntar sig, så fler svarar ja än om frågan varit neutral, t.ex. ”Vad tycker du om skolmaten?”. Svar: B : Ledande fråga |
| ma1 #5.177 | Inga | Granskad – inget fel: Elever i idrottsklasser tränar troligen mer än andra elever. Resultatet blir därför för högt om det ska gälla hela skolan. Svar: A : Urvalsfel |
| ma1 #5.178 | Inga | Granskad – inget fel: Att minnas exakt vad man åt för sex månader sedan är svårt och kan ge minnesfel . Svar: C. |
| ma1 #5.206 | Inga | Granskad – inget fel: Allt annat lika ger 2 000 deltagare mindre slumpmässig osäkerhet än 20. Svar: B. |
| ma1 #5.207 | Inga | Granskad – inget fel: Statistisk signifikans säger något om hur starkt stödet är mot att resultatet bara beror på slumpvariation. Den säger inte att skillnaden måste vara stor eller viktig i praktiken. Svar: B – Falskt. |
| ma1 #5.208 | Inga | Granskad – inget fel: Med ett mycket stort stickprov blir den slumpmässiga osäkerheten mindre. Då kan även en liten skillnad bli statistiskt tydlig. Svar: A – Sant. |
| ma1 #5.209 | Inga | Granskad – inget fel: När fler observationer ingår tenderar slumpmässiga variationer att jämna ut sig bättre. Ett större stickprov minskar därför normalt den relativa slumpmässiga osäkerheten. Svar: C. |
| ma1 #5.210 | Inga | Granskad – inget fel: Med små grupper kan en skillnad på 1 procentenhet mycket väl bero på slumpvariation. Svar: B – nej. |
| ma1 #5.211 | Inga | Granskad – inget fel: Statistisk signifikans används för att bedöma om ett observerat resultat är svårt att förklara enbart med slumpvariation under en given nollhypotes. Svar: A – Sant. |
| ma1 #5.212 | Inga | Granskad – inget fel: En skillnad kan vara statistiskt tydlig men ändå så liten att den har liten praktisk betydelse. Begreppen är alltså inte samma sak. Svar: A. |
| ma1 #5.213 | Inga | Granskad – inget fel: Stor spridning inom grupperna gör det svårare att skilja en liten skillnad mellan grupperna från den variation som redan finns i data. Svar: B – Ja. |
| ma1 #5.214 | Inga | Granskad – inget fel: Ett större stickprov kan minska slumpfelet, men det tar inte bort ett systematiskt fel i hur deltagarna valdes. Ett stort snedvridet urval kan fortfarande vara icke-representativt. Svar: B – Falskt. |
| ma1 #5.216 | Inga | Granskad – inget fel: När populationen först delas i relevanta grupper och man sedan gör slumpurval inom varje grupp kallas det stratifierat urval . Svar: D. |
| ma1 #5.217 | Inga | Granskad – inget fel: Om alla individer i populationen faktiskt undersöks är det en totalundersökning , inte ett stickprov. Svar: C. |
| ma1 #5.218 | Inga | Granskad – inget fel: Populationen är hela den grupp som undersökningen vill kunna säga något om. Här är det alla kommuninvånare över 18 år. Svar: C. |
| ma1 #5.219 | Inga | Granskad – inget fel: De 200 personer som faktiskt väljs ut och intervjuas utgör urvalet . Svar: C. |
| ma1 #5.220 | Inga | Granskad – inget fel: Ett slumpmässigt urval från hela elevregistret ger elever från hela skolan möjlighet att väljas och minskar risken för självselektion. Svar: C. |
| ma1 #5.222 | Inga | Granskad – inget fel: Att välja var k:te person efter en startpunkt är ett systematiskt urval . Svar: D. |
| ma1 #5.223 | Inga | Granskad – inget fel: När personer själva bestämmer om de vill gå in och svara får man ett självurval . Sådana deltagare kan skilja sig systematiskt från dem som inte svarar. Svar: C. |
| ma1 #5.224 | Inga | Granskad – inget fel: Ett välgjort stickprov kan ge användbar information om populationen med betydligt mindre tid och kostnad än att undersöka alla. Det eliminerar däremot inte alla felkällor. Svar: B. |
| ma1 #5.225 | Inga | Granskad – inget fel: De utvalda personer som inte lämnar svar utgör undersökningens bortfall . Svar: D. |
| ma1 #5.280 | Inga | Granskad – inget fel: Olika slumpmässiga stickprov innehåller normalt inte exakt samma individer och kan därför ge olika skattningar. Skillnaden 48 % mot 54 % kan alltså bero på slumpvariation. Svar: D. |
| ma1 #5.282 | Inga | Granskad – inget fel: När felmarginalen är proportionell mot 1/√n behöver urvalet bli fyra gånger så stort för att halvera felmarginalen. |
| ma1 #5.283 | Inga | Granskad – inget fel: Ett stort stickprov minskar slumpmässig osäkerhet, men ett snedvridet urval kan fortfarande ge systematiska fel. Storlek ensam garanterar inte representativitet. Svar: A . |
| ma1 #5.284 | Inga | Granskad – inget fel: Större stickprov ger mer information och minskar normalt slumpvariationen. De andra alternativen skapar inte mer data. Svar: A . |
| ma1 #5.514 | Inga | Granskad – inget fel: Exempel: sjuka personer tar mer medicin, men medicinen orsakar inte sjukdomen. Svar: C |
| ma1 #5.518 | Inga | Granskad – inget fel: Stickprovet är den del av populationen som faktiskt undersöks. Svar: D |
| ma1 #5.519 | Inga | Granskad – inget fel: I ett obundet slumpmässigt urval har varje individ samma sannolikhet att komma med. Svar: C |
| ma1 #5.520 | Inga | Granskad – inget fel: Man väljer de som är lätta att nå, vilket kan ge ett skevt urval. Svar: A |
| ma1 #5.521 | Inga | Granskad – inget fel: Ett fast intervall i en lista kallas systematiskt urval. Svar: B |
| ma1 #5.522 | Inga | Granskad – inget fel: I en totalundersökning ingår hela populationen. Svar: B |
| ma1 #5.523 | Inga | Granskad – inget fel: Populationen delas i grupper (strata) och urval görs inom varje grupp. Svar: C |
| ma1 #5.524 | Inga | Granskad – inget fel: Självselektion ger ofta ett urval som inte representerar populationen. Svar: D |
| ma1 #5.528 | Inga | Granskad – inget fel: Slumpning ur hela registret ger alla samma chans att väljas. Svar: B |
| ma1 #5.529 | Inga | Granskad – inget fel: De som valts ut men inte deltar kallas bortfall. Svar: A |
| ma1 #5.530 | Inga | Granskad – inget fel: Frågan antyder vilket svar som förväntas. Svar: B |
| ma1 #5.531 | Inga | Granskad – inget fel: Felet är lika stort och åt samma håll varje gång. Svar: C |
| ma1 #5.532 | Inga | Granskad – inget fel: Reaktionstiden varierar slumpmässigt mellan mätningarna. Svar: A |
| ma1 #5.533 | Inga | Granskad – inget fel: De som inte svarar utgör bortfallet. Svar: D |
| ma1 #5.534 | Inga | Granskad – inget fel: Slumpmässiga fel tar delvis ut varandra när man beräknar medelvärdet av många mätningar. Svar: D |
| ma1 #5.536 | Inga | Granskad – inget fel: Om t.ex. missnöjda svarar oftare än nöjda blir resultatet skevt. Svar: B |
| ma1 #5.537 | Inga | Granskad – inget fel: Man svarar som man tror är socialt accepterat. Svar: C |
| ma1 #5.538 | Inga | Granskad – inget fel: Ett systematiskt fel försvinner inte när man tar medelvärde. Svar: D |
| ma1 #5.539 | Inga | Granskad – inget fel: Avläsningsfel uppstår när mätvärdet läses av felaktigt, t.ex. på grund av parallax. Svar: A |
| ma1 #5.540 | Inga | Granskad – inget fel: Vanor kan skilja sig mellan årstider. Svar: B |
| ma1 #5.541 | Inga | Granskad – inget fel: Tidigare frågor kan påverka hur man svarar på senare frågor. Svar: C |
| ma1 #5.542 | Inga | Granskad – inget fel: Kända felkällor hjälper läsaren att tolka resultatet rätt. Svar: A |
| ma1 #5.543 | Inga | Granskad – inget fel: Ett större stickprov ger säkrare skattningar och därmed mindre felmarginal. Svar: C |
| ma1 #5.546 | Inga | Granskad – inget fel: Felmarginalen beskriver slumpmässig osäkerhet i urvalet, inte alla typer av fel. Svar: C |
| ma1 #5.548 | Inga | Granskad – inget fel: Med mycket stora stickprov kan även små skillnader bli signifikanta. Svar: A |
| ma1 #5.549 | Inga | Granskad – inget fel: Den undre gränsen är 34 − 2,5 = 31,5 %. Svaret 31,5 godkänns. |
| ma1 #5.550 | Inga | Granskad – inget fel: Den övre gränsen är 34 + 2,5 = 36,5 %. Svaret 36,5 godkänns. |
| ma1 #5.551 | Inga | Granskad – inget fel: Intervallet går från 55 % till 61 %, vilket är 6 procentenheter brett. Svar: 6 |
| ma1 #5.552 | Inga | Granskad – inget fel: Avståndet från 12 till både 10,4 och 13,6 är 1,6 procentenheter. |
| ma1 #5.553 | Inga | Granskad – inget fel: För att 1/√n ska halveras måste √n fördubblas, alltså n bli 4 gånger större. Svar: 4 |
| ma1 #5.554 | Inga | Granskad – inget fel: Ett fyra gånger större stickprov halverar felmarginalen från 3 till 1,5 procentenheter. |
| ma1 #5.555 | Inga | Granskad – inget fel: Intervallet 43–51 % innehåller 50 %, så det är inte säkerställt att andelen är under hälften. Svar: Nej |
| ma1 #5.563 | Inga | Granskad – inget fel: De som står först i kön en viss dag är inte slumpmässigt valda. Elever som sällan äter i matsalen kommer inte med alls. Svar: C |
| ma1 #5.564 | Inga | Granskad – inget fel: Det är ett självselekterat urval. De som har starka åsikter ringer oftare än andra, så resultatet blir inte representativt. Svar: A |
| ma1 #6.40 | Inga | Granskad – inget fel: Personer som besöker en viss webbplats – och dessutom väljer att svara – kan skilja sig mycket från hela befolkningen. Svar: B. |
| ma1 #6.93 | Inga | Granskad – inget fel: 18/20 är 90 %. Men stickprovet är mycket litet , och vi vet inte hur personerna valdes. Därför är generaliseringen osäker. |
| ma1 #6.137 | Inga | Granskad – inget fel: 8 är verkligen dubbelt 4, men totalt deltog bara 12 personer. Resultatet kan därför vara mycket känsligt för slumpvariation, och representativiteten beror dessutom på hur personerna valdes. Svar: C. |
| ma2 #4.04 | Inga | Granskad – inget fel: A har mindre spridning och jämnare tider. Lika medeltider betyder att A inte är snabbare i genomsnitt. |
| ma2 #4.14 | Inga | Granskad – inget fel: Standardavvikelsen 5,7 betyder större spridning än 2,1. |
| ma2 #4.21 | Inga | Granskad – inget fel: Omvandlingen 3x − 7 ger medelvärdet 29 och standardavvikelsen 15. Förskjutningen ändrar inte spridningen. |
| ma2 #4.35 | Inga | Granskad – inget fel: B varierar mindre men ligger fel i genomsnitt. Man behöver både läge och spridning för att bedöma vilken maskin som passar bäst. |
| ma2 #4.36 | Inga | Granskad – inget fel: Material A har mindre standardavvikelse och är mer samlat kring sitt medelvärde. |
| ma2 #4.43 | Inga | Granskad – inget fel: Omvandlingen 1,5x − 7 ger medelvärdet 23 och standardavvikelsen 6. |
| ma2 #4.49 | Inga | Granskad – inget fel: Att lägga till 100 till varje värde ändrar inte spridningen. Standardavvikelsen är fortfarande 6. |
| ma2 #4.56 | Inga | Granskad – inget fel: Medelvärdet blir −4·25 + 10 = −90. Standardavvikelsen multipliceras med 4 och blir 12, aldrig negativ. |
| ma2 #4.65 | Inga | Granskad – inget fel: Grupp A har mindre standardavvikelse och är mest samlad. |
| ma2 #4.68 | Inga | Granskad – inget fel: Centimeter till millimeter multiplicerar både medelvärde och standardavvikelse med 10. Svaren är 180 mm och 40 mm. |
| ma2 #4.75 | Inga | Granskad – inget fel: Samma tillägg till alla värden flyttar även medelvärdet. Avstånden till medelvärdet och standardavvikelsen ändras inte. |
| ma2 #4.84 | Inga | Granskad – inget fel: Förhållandet mellan standardavvikelserna är 8/2 = 4. |
| ma2 #4.86 | Inga | Granskad – inget fel: När varje värde multipliceras med 3 blir också standardavvikelsen tre gånger så stor. |
| ma2 #4.90 | Inga | Granskad – inget fel: Medelvärdet ökar från 12 till 17. Standardavvikelsen är fortfarande 3 eftersom alla värden flyttas lika långt. |
| ma2 #4.93 | Inga | Granskad – inget fel: En fördubbling av alla värden fördubblar både medelvärdet och standardavvikelsen. |
| ma2 #4.102 | Inga | Granskad – inget fel: Multiplikation med 0,5 halverar standardavvikelsen från 4 till 2. |
| ma2 #4.106 | Inga | Granskad – inget fel: Den givna normalmodellen har medelvärde 250 och standardavvikelse 30. Andelen över 288 är cirka 10,3 % och 95:e percentilen cirka 299,35. Här beräknas ingen Sx från rådata. |
| ma2 #4.109 | Inga | Granskad – inget fel: 47 = 2μ + 7 ger μ = 20 och 8 = 2σ ger σ = 4. Tillägget 7 ändrar inte spridningen. |
| ma2 #4.114 | Inga | Granskad – inget fel: Medelvärdet ökar med 5 men standardavvikelsen är oförändrad. |
| ma2 #4.121 | Inga | Granskad – inget fel: En mindre standardavvikelse betyder mindre spridning som helhet, inte att varje enskilt värde måste ligga närmare medelvärdet. |
| ma2 #4.156 | Inga | Granskad – inget fel: A har jämnare resultat, men standardavvikelsen ensam bestämmer inte hela fördelningens form. |
| ma2 #4.173 | Inga | Granskad – inget fel: B har större spridning eftersom 4,9 är större än 1,8. |
| ma2 #4.174 | Inga | Granskad – inget fel: Medelvärdet blir 3·35 − 10 = 95 och standardavvikelsen 3·6 = 18. |
| ma2 #4.175 | Inga | Granskad – inget fel: Materialen 0,0,0,3,3 och 0,0,1,1,4 har samma medelvärde 1,2 och standardavvikelse, men olika medianer, 0 och 1. |
| ma2 #4.195 | Inga | Granskad – inget fel: Material A har mindre standardavvikelse och därmed mindre spridning kring medelvärdet. |
| ma2 #4.201 | Inga | Granskad – inget fel: Ett lika stort tillägg till alla värden ändrar inte spridningen. Standardavvikelsen är 3,5. |
| ma2 #4.211 | Inga | Granskad – inget fel: Alla värden flyttas lika långt, så standardavvikelsen är fortfarande 3,5. |
| ma2 #4.212 | Inga | Granskad – inget fel: Standardavvikelsen blir 2,4·5 = 12. |
| ma2 #4.213 | Inga | Granskad – inget fel: Grupp A har mindre standardavvikelse och därmed mindre spridning. |
| ma2 #4.235 | Inga | Granskad – inget fel: Ett lika stort tillägg till alla värden ändrar inte spridningen. Standardavvikelsen är 4,5. |
| ma2 #4.236 | Inga | Granskad – inget fel: Standardavvikelsen blir 2·3,2 = 6,4. |
| ma2 #4.306 | Inga | Granskad – inget fel: Golfresultaten behandlas uttryckligen som ett stickprov: Sx ≈ 3,15 slag. Intervallet är cirka 275,44–281,73; 9 av 12 resultat ligger där, alltså 75 %. Den tidigare rättningen bevaras. |
| ma2 #5.66 | Inga | Granskad – inget fel: Frågan anger σx för de visade värdena. Båda materialen har median 14 och kvartilavstånd 2, men standardavvikelserna är cirka 1,22 och 5,47 minuter. |
| ma2 #5.71 | Inga | Granskad – inget fel: De uttryckliga temperaturstickproven använder Sx och n−1. Båda medelvärdena är 21,00 °C och standardavvikelserna 0,71 respektive 1,41 °C. |
| ma2 #5.94 | Inga | Granskad – inget fel: Temperaturerna är uttryckligen ett stickprov. Medelvärdet är 21,00 °C; kvadratsumman 0,40 delas med 4 och ger Sx ≈ 0,32 °C. |
| ma2 #5.110 | Inga | Granskad – inget fel: Frågan anger σx för gruppernas angivna svar. Båda medelvärdena är 5; standardavvikelserna är cirka 0,63 och 2,00. A har mest samlade svar. |
| matf1 #1.103 | Inga | Granskad – inget fel: Urvalet görs utan återläggning. Exakt en defekt av fyra ger 3·84/495 = 28/55 ≈ 50,9 %. Bråk, decimal och procent godkänns. |
