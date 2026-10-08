# Fysik 1: lutande plan, 2026-10-08

## Omfattning

Samtliga 95 huvuduppgifter och 136 elevkort i kapitel 4, området `lutande_plan`, har lästs manuellt två gånger. Även alla ledtrådar och svarsalternativ har lästs mot den reviderade frågan. 93 huvuduppgifter och 134 kort har ändrats. ID:n är bevarade. JSON-rapporten anger ändrade fält för varje ID.

Denna rapport gäller detta område. Hela Fysik 1-banken är ännu inte färdiggranskad. Härnäst återstår kraftmoment och blandade kraftuppgifter i kapitel 4, därefter senare kapitel och en andra genomgång av hela banken.

## Revidering

Lösningarna förklarar kraftbalansen, visar insatta värden och de mellanled som behövs för svaret, utan numrerade lösningssteg. Begreppen vilofriktion och glidfriktion används med rätt förutsättningar. Rullande föremål behandlas med en uttrycklig modell för motstånd och hjulens massa. I två uppgifter har skateboard ersatts med pulka, så att modellen för glidfriktion passar situationen.

- **4.610 c:** den saknade startfarten 3,0 m/s finns nu på kortet. Lösningen visar retardationen uppför, stoppsträckan, tiden uppför, accelerationen nedför och tiden tillbaka. Kortet kräver inga tidigare kort.
- **4.583 b–c, 4.586 b, 4.604 b, 4.629 b:** kortens egna givna värden, lösningar och rättning har jämförts. Avrundning i ett tidigare kort ska inte göra ett korrekt svar fel i nästa kort.
- **4.631 b:** den gamla avrundade massan har tagits bort. Kortet innehåller hela kraftsituationen och visar hur massan bestäms innan normalkraften beräknas.
- **4.616 b och 4.635 b:** onödiga data från det tidigare försöket har tagits bort. Frågan beskriver den situation som eleven faktiskt ska lösa.
- **4.67, 4.114, 4.125:** facit visar normalkraften, tyngdkraftens del längs planet och friktionens gräns. Den friktion som behövs för vila skiljs från största möjliga friktion.
- **4.47, 4.124:** felaktiga numeriska slutsiffror har korrigerats. Övriga numeriska facit har också jämförts med självständiga beräkningar.
- **4.590:** den faktiskt använda bromskraften delad med normalkraften beskrivs som en kvot, inte automatiskt som däckens största möjliga friktionstal.
- **4.407 och 4.417:** lådan i bilden har flyttats så att dess undersida ligger på rampen. Friktionspilen i 4.417 har gjorts tydligare. Tyngdkraftens etikett i 4.222 har flyttats från bildens bottenlinje.

Numeriska frågor anger den efterfrågade avrundningen. Metadata behåller de oavrundade fysiska värdena och en tolerans som tillåter korrekt avrundade svar. Felaktiga exakta likheter med avrundade resultat har ersatts med ungefär lika med.

## Nivå

Nivå 1 består av en direkt tyngdkraftsberäkning och två enkla frågor om krafternas riktning eller normalkraftens förändring. Direkt uppdelning av en given kraft och en enkel kraftbalans ligger på nivå 2. Friktion tillsammans med rörelseberäkningar ligger vanligen på nivå 3. Flera rörelsefaser, två obekanta kopplade kraftbalanser eller mer avancerade resonemang ligger högre. Träningsnivå och betygsnivå bedöms separat.

| Träningsnivå | Före | Efter |
| --- | ---: | ---: |
| 1 | 3 | 3 |
| 2 | 61 | 46 |
| 3 | 57 | 71 |
| 4 | 10 | 13 |
| 5 | 5 | 3 |

## Verifiering

- `tools/fysik1-lutande-plan.test.js`: samtliga 72 numeriska huvuduppgifter, med 113 svar, räknas från manuellt avlästa givna värden. Dessutom kontrolleras fem uppsättningar egna kortdata och facits numeriska slutsvar.
- Kunskapsgymmets faktiska rättning i Chromium: 124 oberoende beräknade svar, inklusive kortens egna avrundade givna värden, godkända.
- Hela Fysik 1-banken: 4 977 kort och 32 822 kontroller av rätta svar, numeriska format, enheter och felaktiga svar, utan fel i kontrollen.
- Full formelrendering i båda repona: 23 823 formelförekomster per repo, inga renderingsfel eller presentationsfynd.
- Områdets samtliga 21 SVG-figurer granskade visuellt. Fyra SVG-fält i tre uppgifter är ändrade och har granskats igen efter ändringen.
- 118 vanliga tester och 47 SVG-tester i Uppgiftslabbet samt 65 tester i Kunskapsgymmet: godkända.
- Samtliga 136 elevkort och 95 läraruppgifter har kontrollerats för för breda displayformler vid 390 pixels bredd. Breda beräkningar har fått radbrytningar eller tydligt beräknade mellanvärden. Inga displayformler kräver sidscrollning i kontrollen. Utvalda fristående kort har också granskats visuellt på mobil och dator.
- Bankvalidator: 0 ERROR, 8 WARNING, 655 INFO, oförändrade fyndantal.
- Bankfilerna i Uppgiftslabbet och Kunskapsgymmet är identiska byte för byte. Inga uppgifter utanför området har ändrats i denna leverans.

De automatiska kontrollerna kompletterar den manuella analysen och bevisar inte att hela banken saknar pedagogiska fel.
