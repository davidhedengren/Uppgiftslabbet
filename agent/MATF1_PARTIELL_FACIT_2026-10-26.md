# Matf1: partiell integration – full områdesgranskning 2026-10-26

**36 huvuduppgifter / 44 träningskort granskade. 33 huvuduppgifter förbättrade, 3 granskade utan fel.** Alla lagrade matematiska slutsvar var korrekta och är oförändrade. Ändringarna gäller lösningarnas pedagogik, ledtrådar, rättningsformat, nivå och verktyg. Detta är en genomgång av ett helt område, inte en färdiggranskning av hela banken.

## Fynd och beslut

- 29 äldre huvudfacit saknade uppgiftsspecifika rubriker eller nödvändiga mellanled. Hela lösningar har skrivits manuellt, inklusive alla 12 delkort i 3.318–3.321. Även 3.356 och 3.357 har fått fler mellanled. 3.01 och 3.02 har fått läsbara formelrader på mobil.
- 3.15 hade en felaktig ledtråd: en partiell integration räcker. Jämförelserna 3.03, 3.135, 3.92, 3.96 och 3.319a använder också en enda partiell integration. De har fått uppgiftsspecifika förklaringar. 3.82 och 3.97 behöver däremot två omgångar.
- 3.318/3.319 a–d frågar efter **alla** primitiva funktioner men använde `primitiv`, som accepterar en enstaka funktion. De använder nu `primitiva`. Tolv andra obestämda integraler (3.34, 3.55, 3.56, 3.58, 3.81, 3.82, 3.90, 3.145, 3.91, 3.92, 3.95, 3.96) har fått samma konsekventa format. Fri konstant får heta exempelvis C eller K och stå först eller sist; 2K+7 går bra. K² och sin(K) ger inte hela familjen och avvisas.
- När **en** primitiv funktion efterfrågas, i 3.125/3.132/3.133/3.135, behålls `primitiv`. I 3.320 a–b behålls `uttryck` eftersom punktvillkoret bestämmer konstanten.
- Rättningskodens tidigare antagande om x gjorde att t kunde behandlas som fri konstant. 3.318c använder t. Konsumenten väljer nu x eller t från facit, avgränsat till de två primitivformaten. Fel t-beroende termer avvisas. Sökning i Matf1/Mato1/Mato2 hittade inget ytterligare t-kort med dessa format. Följdkontrollen omfattar sex tidigare x/exponentialfall samt sex uttrycksfall i x/t och båda formaten.
- Nivå 1 → 2: 3.02, 3.14 och 3.31. Metoden innehåller flera beroende led. 3.92 blir C/nivå 3 i linje med tidigare beslut för 3.03. 3.34 blir nivå 4, jämförbar med 3.01 och 3.132. 3.318 c/d blir E/nivå 2, liksom motsvarande enstegsintegrationer 3.125/3.145/3.30; huvuduppgiften blir E/nivå 2. Övriga nivåer behålls efter genomgång.
- Miniräknare tillåts på alla 44 kort. Nytt för 3.33, 3.57, 3.76, 3.97 samt 3.321 a/b. GeoGebra är avstängt: området tränar uttryckligen metoden partiell integration och integralerna kan lösas symboliskt för hand; CAS skulle ge själva det som prövas. Räkneverktyget behövs inte för exakt metod men vanlig räknare förstör inte den.
- Ingen ny figur behövs till rena symboliska integrationsövningar. Den befintliga areagrafen i 3.357 har kontrollerats: x cos x är icke-negativ på [0,π/2], ändpunkterna ligger på x-axeln och den skuggade arean är π/2−1.

## Alla granskade uppgifter och föreslagna kommentarer

Statusarna nedan är granskningsresultat i repot. Inga elevrapporter har avslutats och inga kommentarer har skickats till elever.

| ID / delar | Status | Kommentar att använda |
|---|---|---|
| #3.01 | Åtgärdad | Svaret var korrekt. De två partiella integrationerna och derivatakontrollen är nu lättare att läsa även på mobil. |
| #3.02 | Åtgärdad | Svaret var korrekt. Formelraderna är tydligare på mobil. Uppgiften ligger nu på nivå 2 eftersom metoden kräver flera beräkningsled. |
| #3.03 | Åtgärdad | Facit visar nu varför logaritmen skrivs som en produkt med 1 och hur den återstående integralen blir x. Alla primitiva funktioner innehåller en fri konstant. |
| #3.125 | Åtgärdad | Facit visar nu hela integrationen och förklarar faktorerna 1/2 och 1/4. En primitiv funktion får väljas med C = 0. |
| #3.14 | Åtgärdad | Facit förklarar nu varför den sista cosinustermen får plustecken. Uppgiften är nivå 2. |
| #3.15 | Åtgärdad | En partiell integration räcker. Den felaktiga ledtråden om flera omgångar är rättad och potensintegrationen visas. |
| #3.30 | Åtgärdad | Facit visar båda faktorerna 1/2 så att termen e^(2x)/4 går att följa. |
| #3.31 | Åtgärdad | Facit visar varför subtraktionen av −cos x ger en positiv integral. Uppgiften är nivå 2. |
| #3.132 | Åtgärdad | Båda partiella integrationerna och insättningen av den andra integralen visas nu. Slutsvaret var korrekt. |
| #3.133 | Åtgärdad | Facit visar båda integrationerna, inklusive tecken och faktorer från argumentet 2x. Slutsvaret var korrekt. |
| #3.33 | Åtgärdad | Den primitiva funktionen härleds nu innan F(1)−F(0) beräknas. Svaret är fortfarande 1. Miniräknare tillåts. |
| #3.34 | Åtgärdad | Facit visar båda integrationerna och hur −2 påverkar hela parentesen. Alla primitiva funktioner kräver en fri konstant. Nivå 4. |
| #3.135 | Åtgärdad | Facit visar hur logaritmens derivata förenklar integranden och varför C = 0 kan väljas när en funktion efterfrågas. |
| #3.55 | Åtgärdad | Facit visar båda faktorerna 1/2 och varför cosinustermen blir positiv. Rättningen hanterar hela familjen av primitiva funktioner. |
| #3.56 | Åtgärdad | Facit förklarar båda minustecknen vid integrering av e^(−x). En fri konstant kan skrivas på olika platser i svaret. |
| #3.57 | Åtgärdad | Facit visar metoden samt F(e) och F(1) separat. Svaret är (e²+1)/4. Miniräknare tillåts. |
| #3.58 | Åtgärdad | Båda integrationerna visas med ett eget mellanresultat J. Rättningen skiljer hela familjen från en enskild primitiv funktion. |
| #3.76 | Åtgärdad | Facit härleder den primitiva funktionen och visar varför F(π)−F(0)=−2. En integral kan vara negativ. Miniräknare tillåts. |
| #3.81 | Åtgärdad | Facit förklarar hur ursprungsintegralen kommer tillbaka och hur ekvationen 2I=eˣ(sin x−cos x) löses. |
| #3.82 | Åtgärdad | Facit visar även den andra integrationen av ln x. Rättningen kräver en fri konstant för hela familjen. |
| #3.90 | Åtgärdad | Facit visar varför två faktorer 1/3 ger 1/9. Ekvivalenta skrivsätt med fri konstant godtas. |
| #3.145 | Åtgärdad | Facit visar nu den efterfrågade derivatakontrollen, där sinustermerna tar ut varandra. Självrättningen kontrollerar slututtrycket; motiveringen läses i lärarvyn. |
| #3.91 | Åtgärdad | Facit förklarar tecknet och båda faktorerna 1/3. Rättningen hanterar hela familjen av primitiva funktioner. |
| #3.92 | Åtgärdad | Facit visar kedjeregeln: derivatan av ln(3x) är 1/x. Uppgiften ligger på nivå 3, liksom den jämförbara logaritmuppgiften 3.03. |
| #3.95 | Åtgärdad | Facit visar den andra integrationen och hur −2 ändrar båda tecknen. Slutsvaret var korrekt. |
| #3.96 | Åtgärdad | Facit visar hur derivatan av ln(2x) förenklas till 1/x. Rättningen hanterar en godtycklig fri konstant. |
| #3.97 | Åtgärdad | Facit visar båda integrationerna och båda gränsvärdena. Svaret är e−2. Miniräknare tillåts. |
| #3.318 a, b, c, d | Åtgärdad | Alla fyra delkort har fullständiga lösningar. En fri konstant krävs när alla primitiva funktioner efterfrågas. t behandlas som integrationsvariabel i c. Samtliga delar är rutinuppgifter på nivå 2. |
| #3.319 a, b, c, d | Åtgärdad | Alla fyra delkort visar metodval och mellanled, särskilt den återkommande integralen i d. En fri konstant krävs i samtliga delar. |
| #3.320 a, b | Åtgärdad | Båda delkorten visar integrationen innan villkoret används. Konstanterna 4 respektive 5 är bestämda och får inte ersättas med en fri konstant. |
| #3.321 a, b | Åtgärdad | Båda delkorten visar primitiv funktion och gränsinsättning separat. De exakta svaren π/4 respektive 8ln(2)/3−7/9 är korrekta. Miniräknare tillåts. |
| #3.353 | Granskad – inget fel | Granskad – inget fel. Derivering av (2x−3)eˣ ger (2x−1)eˣ. Metodval, mellanled och fri konstant framgår. |
| #3.354 | Granskad – inget fel | Granskad – inget fel. Derivering av x⁴ln(x)/4−x⁴/16 ger x³ln(x). Facit och ledtråd visar rätt val av faktorer. |
| #3.355 | Granskad – inget fel | Granskad – inget fel. De två partiella integrationerna och teckenbytet vid subtraktion av J är korrekta och tydliga. |
| #3.356 | Åtgärdad | Facit visar nu vilka faktorer som väljs i båda omgångarna och hela insättningen som ger 5I/4. Slutsvaret var korrekt. |
| #3.357 | Åtgärdad | Facit visar nu hela integrationen och varför integralen motsvarar den skuggade arean. Svaret π/2−1 och figuren är korrekta. |

## Verifiering

- Oberoende symbolisk derivering av samtliga primitiva funktioner samt beräkning av samtliga bestämda integraler: **44 kontroller**. Punktvillkoren i 3.320 kontrollerade separat.
- Faktiska svarsfält: **822 rättningsfall** på mobil och dator, inklusive rätt svar, omformade uttryck, konstantens placering, saknad konstant och felaktiga termer. Alla passerade.
- Efter manuella radbrytningar: **88 elevvyer och 96 lärarvyer**, utan LaTeX-fel eller för breda formelrader. Frågor, ledtrådar och facit renderade; komplexa lösningar och areagraf visuellt kontrollerade.
- Ny regression för x/t och fria konstanter: **144 kontroller**, godkända. Tidigare Ma3-primitivregression: **180 rättningskontroller och 62 vyer**, godkända. Matf1:s 18 senaste uppgifter: befintligt matematiktest godkänt.
- Bankvalidator Matf1: **0 ERROR, 8 WARNING, 67 INFO**. Äldre varningar är inte ett intyg om resten av bankens kvalitet.
- Semantisk diff: endast de 33 redovisade huvuduppgifterna ändrade; inga ändringar av rättSvar, inga borttagna ID:n. Installationsskriptet är idempotent. Master och konsument har identisk bankfil.

Skydd: `tools/matf1-partiell-facit-2026-10-26.test.py`, manuellt författat revisionsskript och mobilradbrytningar. Konsumenten har cases-filen och `tools/primitiv-variabel-2026-10-26.browser.cjs`. Kör revisionsskriptet efter äldre byggare som annars skulle återställa korta facit.
