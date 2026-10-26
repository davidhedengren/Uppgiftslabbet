# Första ordningens differentialekvationer – manuell granskning 2026-10-26

**68 huvuduppgifter granskade: 51 förbättrade, 17 granskade utan fel.** Hela områdena homogena första ordningen (33) och inhomogena första ordningen (35), inklusive fyra fristående delkort. 70 elevkort efter delning. Ingen rapportstatus ändras och inga kommentarer skickas. Fortfarande inte en manuell slutgranskning av hela banken.

## Viktiga fynd

- Elva äldre allmänna lösningar hade `uttryck` i stället för `diffekv_losning`: 4.03/358/67/362/09/21/51/94/142/143/145. Samma matematiska familj ska accepteras med exempelvis K eller 2A i stället för C. En enskild lösning eller en familj med fel partikulärdel räcker inte. FP73:s parser bevaras; dess användning utökas till de missade förstaordningsuppgifterna. 4.612/618 är jämförelsefall som redan var rätt taggade.
- I 4.94/95 var beskrivningen ”proportionell mot y” fel: det är avvikelsen från jämvikten som är proportionell. 4.67:s ledtråd påstod att negativ k alltid ger en avtagande funktion, vilket inte stämmer när C är negativt. 4.358 tar nu med nollösningen efter separationens division med y. Placeringen av den variabelkoefficientekvationen behålls i detta breda förstaordningsområde, men nivån ändras till C/3.
- Generisk text om flera begynnelsevillkor och kontroll av y′ togs bort där endast ett startvillkor finns. Jämfört bland annat 4.48/50/68/396/397/107/124/125/126/168. Varje facit är individuellt författat med relevant beräkning och slutsvar.
- Numeriska referenser använder full precision. Ingen dold exaktform i 4.120, som nu accepterar 10/e² och korrekta decimaler. Fria avrundningar i 4.69/120/396/397 får inte en godtyckligt bred grundtolerans. 4.557 har exakt antal och avvisar fel heltal. Explicita avrundningskrav har halvt sista avrundningssteg; särskilt 4.515/516/520/556/558/559/560/517/521.
- 4.399 frågar bara efter entydiga C och k. Den får två märkta, ordnade numeriska svarsfält i stället för manuell bedömning. Ingen motiveringsuppgift har gjorts automatisk.
- 4.554/558 har individuella delfacit utan andra delens slutsvar. B-kortet i 4.554 får den modell som behövs för insättningen. Gemensamma inledningar bevaras; behövt resultat placeras i delfrågan enligt senaste instruktionen. 4.521 skiljer uttryckligen kg från minuter.

## Nivåer, verktyg och figurer

4.48 är nivå 1 eftersom familjen är given. 4.124/125/120 och de berörda 4.554/558-korten är nivå 2. 4.69/399/397/516/592/596 är E/nivå 2: rutinberäkningar blir inte C för att de innehåller flera steg. 4.358/515/520/556/517/521/597 är C/nivå 3, med variabelseparation, parameterbestämning eller tolkning av flera samband; de tidigare A/4–5-etiketterna var för höga. Övriga nivåer behålls efter genomgång.

Alla 68 tillåter vanlig miniräknare. GeoGebra är avstängt eftersom symbolisk metod eller avläsning av redan givna grafer prövas och ingen digital lösare behövs. Modelluppgifter med logaritmer kan räknas med vanlig miniräknare. Befintliga figurer bevaras och granskas mot ekvationer, tangenter och startvärden. Symboliska uppgifter får ingen dekorativ figur.

## Granskade ID:n och föreslagna kommentarer

| ID | Status | Kommentar |
|---|---|---|
| #4.48 | Åtgärdad | Facit använder den redan givna familjen direkt. Nivå 1; inga onödiga råd om att lösa ekvationen på nytt. |
| #4.03 | Åtgärdad | Facit visar varför exponentialfamiljen fungerar för alla C. Fria konstanter får heta exempelvis K. |
| #4.358 | Åtgärdad | Separationen och integreringen visas. Nollösningen tas med trots divisionen med y. C/nivå 3 och familjerättning. |
| #4.50 | Åtgärdad | Startvärdet används uttryckligen och båda villkoren kontrolleras. |
| #4.67 | Åtgärdad | Ledtråden påstår inte längre att alla lösningar avtar: negativa C ger växande funktioner mot noll. Familjerättning. |
| #4.68 | Åtgärdad | Facit visar varför C=7 och kontrollerar derivatan. |
| #4.69 | Åtgärdad | Fullprecision för k och korrekt fri avrundning. Lösningen visar båda mätvärdena och logaritmsteget. E/nivå 2. |
| #4.362 | Åtgärdad | Facit visar hur avvikelsen från jämvikten ger den homogena ekvationen. Alternativa namn på fria konstanten godtas. |
| #4.120 | Åtgärdad | Numeriskt format godtar både exakt 10/e² och korrekta decimalavrundningar. Nivå 2. |
| #4.09 | Åtgärdad | Facit utvecklar den linjära ansatsen och bestämmer båda koefficienterna. Rättningen jämför hela lösningsfamiljen. |
| #4.21 | Åtgärdad | Facit visar derivatan av ansatsen, koefficientjämförelsen och summan av lösningsdelarna. Familjerättning. |
| #4.51 | Åtgärdad | Facit bestämmer båda lösningsdelarna och kontrollerar insättningen. Familjerättning. |
| #4.71 | Åtgärdad | Facit visar varför jämvikten är 5 innan startvillkoret används. |
| #4.94 | Åtgärdad | Den missvisande förklaringen om proportionalitet mot y ersätts: det är avvikelsen från jämvikten som är proportionell. Familjerättning. |
| #4.95 | Åtgärdad | Facit beskriver avvikelsen från jämvikten och använder startvärdet utan att ledtråden ger bort jämviktsvärdet. |
| #4.142 | Åtgärdad | Facit visar minustecknet när den konstanta partikulärlösningen bestäms. Familjerättning. |
| #4.143 | Åtgärdad | Facit visar jämvikten och förklarar att positiva exponenten ger ökande avstånd från den. Familjerättning. |
| #4.145 | Åtgärdad | Båda koefficientvillkoren i den linjära ansatsen visas. Familjerättning. |
| #4.396 | Åtgärdad | Ett startvillkor används utan irrelevant text om flera villkor. Fullprecision och fri avrundning ersätter bred tolerans. |
| #4.397 | Åtgärdad | Facit visar C=4 och värdet vid x=2. Fri avrundning med fullprecision; rutinuppgiften är E/nivå 2. |
| #4.399 | Åtgärdad | Två märkta svarsfält för C och k ger robust självrättning av den entydiga beräkningen. E/nivå 2. |
| #4.107 | Åtgärdad | Facit visar den konstanta delen och det enda startvillkoret, utan generiska instruktioner för högre ordning. |
| #4.124 | Åtgärdad | Facit visar lösningsfamilj, startvillkor och kontroll. Nivå 2 för två beroende steg. |
| #4.125 | Åtgärdad | Facit visar hur startvärdet bestämmer C och kontrollerar tecknet i derivatan. Nivå 2. |
| #4.515 | Åtgärdad | Halveringstid, logaritmer och rimlighetskontroll visas. Toleransen avvisar angränsande felaktiga tiotalsavrundningar. C/nivå 3. |
| #4.516 | Åtgärdad | Facit visar startvillkoret före insättningen. E/nivå 2; 15,06 godtas och 15,05/15,07 avvisas. |
| #4.520 | Åtgärdad | Facit använder exakt k i nästa beräkning. Enheter och precisionsgränser för båda fälten är uttryckliga. C/nivå 3. |
| #4.554 | Åtgärdad | Båda delarna har egna steg och ledtrådar. B-kortet får modellen det behöver; fullprecision används vid avrundning till hundratal. Nivå 2. |
| #4.556 | Åtgärdad | Facit visar logaritmsteget och att tiden räknas från eldningens början. Fullprecision, snävare tolerans och C/nivå 3. |
| #4.557 | Åtgärdad | Facit förklarar de tre åttatimmarsperioderna. Det exakta antalet är 3 125; närliggande felaktiga heltal godtas inte. |
| #4.558 | Åtgärdad | Egna facit för båda delarna. Fullprecision används före heltals-/decimalavrundning. A-kortet är nivå 2. |
| #4.559 | Åtgärdad | Facit visar tidsintervallet 48 år och logaritmsteget. Fullprecision, tre decimaler och enheten per år. |
| #4.560 | Åtgärdad | Facit visar hur starttrycket förkortas och varför k är positivt. Fullprecision och enheten per km. |
| #4.126 | Åtgärdad | Facit visar hur −4 och sedan C=6 bestäms och kontrollerar lösningen. |
| #4.168 | Åtgärdad | Facit förklarar avvikelsen från jämvikten, startvillkoret och riktningen mot 3. |
| #4.517 | Åtgärdad | Facit visar temperaturskillnaderna och använder oavrundat k. C/nivå 3; rätt tiondelsavrundning godtas. |
| #4.521 | Åtgärdad | Frågan skiljer kg från minuter. Facit visar jämvikten, startvillkoret och tiden till 15 kg. C/nivå 3. |
| #4.591 | Åtgärdad | Facit kopplar jämvikten till nivån som kurvorna närmar sig. Figuren behålls. |
| #4.592 | Åtgärdad | Facit visar minustecknet framför hela ansatsen och båda koefficientvillkoren. E/nivå 2. |
| #4.593 | Åtgärdad | Kedjeregel och koefficientjämförelse visas före slutsvaret. |
| #4.594 | Åtgärdad | Facit visar beräkningen av gränshastigheten och kontrollerar den mot grafen och derivatans tecken. |
| #4.595 | Åtgärdad | Startvärde och jämviktsnivå används var för sig för att välja rätt kurva, följt av kontroll. |
| #4.596 | Åtgärdad | Facit visar lösningen med startvillkor och logaritmsteget. Fullprecision och E/nivå 2. |
| #4.597 | Åtgärdad | Facit kopplar tangentens lutning och jämviktsnivån till två separata parametervillkor. C/nivå 3. |
| #4.605 | Granskad – inget fel | Granskad – inget fel: frågan, lösningen, ledtråden, nivån och självrättningen stämmer. Befintligt facit behålls. |
| #4.606 | Åtgärdad | Den långa deriveringsraden delas i två meningsfulla steg för mobilvisning. |
| #4.607 | Granskad – inget fel | Granskad – inget fel: frågan, lösningen, ledtråden, nivån och självrättningen stämmer. Befintligt facit behålls. |
| #4.608 | Granskad – inget fel | Granskad – inget fel: frågan, lösningen, ledtråden, nivån och självrättningen stämmer. Befintligt facit behålls. |
| #4.609 | Granskad – inget fel | Granskad – inget fel: frågan, lösningen, ledtråden, nivån och självrättningen stämmer. Befintligt facit behålls. |
| #4.610 | Granskad – inget fel | Granskad – inget fel: frågan, lösningen, ledtråden, nivån och självrättningen stämmer. Befintligt facit behålls. |
| #4.611 | Åtgärdad | Andel och procent behandlas i separata steg. Fullprecision används vid avrundningen. |
| #4.612 | Granskad – inget fel | Granskad – inget fel: frågan, lösningen, ledtråden, nivån och självrättningen stämmer. Befintligt facit behålls. |
| #4.613 | Granskad – inget fel | Granskad – inget fel: frågan, lösningen, ledtråden, nivån och självrättningen stämmer. Befintligt facit behålls. |
| #4.614 | Åtgärdad | Facit visar varför C=10/e och hur det ger y(0). Fullprecision används vid rättning. |
| #4.615 | Åtgärdad | Facit visar halveringsvillkor, förkortning och logaritmer. Fullprecision används vid rättning. |
| #4.616 | Granskad – inget fel | Granskad – inget fel: frågan, lösningen, ledtråden, nivån och självrättningen stämmer. Befintligt facit behålls. |
| #4.617 | Granskad – inget fel | Granskad – inget fel: frågan, lösningen, ledtråden, nivån och självrättningen stämmer. Befintligt facit behålls. |
| #4.618 | Granskad – inget fel | Granskad – inget fel: frågan, lösningen, ledtråden, nivån och självrättningen stämmer. Befintligt facit behålls. |
| #4.619 | Granskad – inget fel | Granskad – inget fel: frågan, lösningen, ledtråden, nivån och självrättningen stämmer. Befintligt facit behålls. |
| #4.620 | Granskad – inget fel | Granskad – inget fel: frågan, lösningen, ledtråden, nivån och självrättningen stämmer. Befintligt facit behålls. |
| #4.621 | Granskad – inget fel | Granskad – inget fel: frågan, lösningen, ledtråden, nivån och självrättningen stämmer. Befintligt facit behålls. |
| #4.622 | Åtgärdad | Facit prövar den konstanta lösningen direkt i båda villkoren. |
| #4.623 | Åtgärdad | Facit visar jämvikten, familjen och hur startvärdet bestämmer konstanten. |
| #4.624 | Granskad – inget fel | Granskad – inget fel: frågan, lösningen, ledtråden, nivån och självrättningen stämmer. Befintligt facit behålls. |
| #4.625 | Granskad – inget fel | Granskad – inget fel: frågan, lösningen, ledtråden, nivån och självrättningen stämmer. Befintligt facit behålls. |
| #4.626 | Granskad – inget fel | Granskad – inget fel: frågan, lösningen, ledtråden, nivån och självrättningen stämmer. Befintligt facit behålls. |
| #4.627 | Granskad – inget fel | Granskad – inget fel: frågan, lösningen, ledtråden, nivån och självrättningen stämmer. Befintligt facit behålls. |
| #4.628 | Åtgärdad | Facit härleder båda lösningsdelarna före insättning. Fullprecision används vid tvådecimalerssvaret. |

## Kontroller

- Oberoende SymPy-kontroll av alla 68: funktioner, derivator, startvillkor, numeriska referenser, flervalsalternativ och verktyg.
- Tidigare `ma5-diffekv-2026-10-24.test.js`: sju tester godkända utan försvagade kontroller.
- Chromium: 710 rättningsfall i huvudkörningen och 44 riktade delkortskontroller godkända. 140 elevvyer och 144 lärarvyer på 390/1280 px. Fyra för långa formelrader upptäcktes och delades upp. Alla nio SVG-figurer visuellt granskade; 4.591:s ledtråd hänvisar inte längre till en horisontell kurva som inte är utritad.

Reproduktion: `tools/revidera-matf1-forsta-facit-2026-10-26.py`, `tools/matf1-forsta-facit-2026-10-26.test.py`, konsumentens `matf1-forsta-facit-2026-10-26.cases.json` samt det gemensamma browserharneset. Äldre byggare får inte återställa korta facit eller uttrycksformat för allmänna lösningar.

Helbanksvalidator: Matf1 0 ERROR, 8 WARNING, 67 INFO. Äldre fel i andra banker redovisas i helbanksinventeringen och åtgärdas inte blint här.

Slutlig omrendering: 140 elevvyer och 144 lärarvyer utan LaTeX-fel, horisontellt sidöverflöde eller för breda formelrader.
