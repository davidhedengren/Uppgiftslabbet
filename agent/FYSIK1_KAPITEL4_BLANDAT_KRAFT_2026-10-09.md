# Fysik 1: blandade kraftuppgifter, 2026-10-09

## Omfattning

Samtliga 53 huvuduppgifter och 101 elevkort i kapitel 4, området `blandat_kraft`, har lästs manuellt två gånger. Frågor, lösningsförslag och ledtrådar har jämförts. Samtliga huvuduppgifter har reviderats. ID:n är bevarade. JSON-rapporten anger ändrade fält per ID.

Den manuella granskningen av kapitel 2–4 omfattar nu 1 430 huvuduppgifter. Hela Fysik 1-banken är fortfarande under granskning. Nästa område är arbete i kapitel 5, därefter övriga områden och en andra genomgång av hela banken.

## Revidering

Texter beskriver den situation som ska lösas och anger tydligt vad svaret avser. Facit visar insatta värden, enheter och de beräkningar som behövs. Konstant acceleration skiljs från en varierande fjäderkraft. Kraftsumma, dragkraft och friktion hålls isär. Deluppgifterna står på separata rader, utan numrerade lösningssteg.

- **4.153 och 4.286:** accelerationsformeln är rättad från den felaktiga skrivningen Δv/Δ · t till Δv/Δt.
- **4.160 b och e:** de fristående korten innehåller egna data och hänvisar inte till ”de första fyra delarna”. Lösningen räknar på släpet utan att blanda in bilens massa.
- **4.153, 4.155, 4.158, 4.159, 4.167, 4.169 och 4.281:** onödiga massor, kraftdata eller uppgifter för andra delar har tagits bort från enklare kort. Ledtrådarna passar kortets egna data.
- **4.164 b och 4.201 c:** två upprepade fart–sträcka-beräkningar har varierats till frågor om tid. Enheter, rättningsvärden och lösningar följer frågan.
- **4.201, 4.225 c och 4.281 d:** enkla kort ger accelerationen eller kraftsumman direkt och kräver endast en insättning. De kan besvaras utan tidigare kort.
- **4.278, 4.279 och 4.277:** lösningarna visar acceleration, fart och sträcka i varje rörelsefas samt hur nästa fas börjar. I huvudfacit visas gemensamma beräkningar en gång; fristående kort behåller hela sin egen härledning.
- **4.284:** varje kort visar de två kraftbalanserna och hur accelerationen beräknas. Tid och slutfart använder ett oavrundat värde.
- **4.282:** paketets förflyttning i rummet skiljs från glidsträckan i förhållande till bandet. Lösningen beräknar bandets och paketets sträckor innan skillnaden tas.
- **4.439:** härledningen visar hur snörkraften bestäms och varför lika friktionstal tar ut sig. Villkoret för positiv snörkraft förklaras.
- **4.167:** ”dynamometer” har ersatts med ”kraftmätare”, även i figuren.

Numeriska frågor anger tre värdesiffror. Rättningen använder oavrundade fysiska värden och tolerans för den angivna avrundningen. Exakta likheter och avrundade resultat skrivs med rätt tecken.

## Nivå

Nivå 1 har en enda direkt beräkning med givna värden och en given formel. Nivå 2 omfattar en enkel kraftbalans, hastighetsändring, medelfart eller enhetsomvandling. Kombinationer av kraftbalans och rörelse ligger vanligen på nivå 3. Flera rörelsefaser och kopplade kroppar med efterföljande rörelse ligger högre. Träningsnivå och betygsnivå bedöms separat.

| Träningsnivå | Före | Efter |
| --- | ---: | ---: |
| 1 | 0 | 7 |
| 2 | 22 | 39 |
| 3 | 63 | 42 |
| 4 | 14 | 12 |
| 5 | 2 | 1 |

## Verifiering

- `tools/fysik1-blandade-krafter.test.js`: samtliga 36 numeriska huvuduppgifter med 84 svar räknas från manuellt avlästa givna värden. Alla 84 numeriska slutsvar i kortens facit jämförs med dessa beräkningar. De reviderade tidsfrågornas enheter och flera beroenden mellan kort kontrolleras separat.
- Kunskapsgymmets faktiska rättning i Chromium: 87 självständigt beräknade svar godkända, inklusive tre kort med egna förenklade givna värden.
- Hela Fysik 1-banken: 4 977 kort och 32 822 kontroller av rätta svar, format, enheter och felaktiga svar, utan fel i kontrollen.
- Full formelrendering i båda repona: 23 878 formelförekomster per repo, inga renderingsfel eller presentationsfynd.
- Alla 25 figurförekomster granskade visuellt. Den ändrade etiketten i 4.167 är granskad igen efter ändringen.
- 125 vanliga tester och 47 SVG-tester i Uppgiftslabbet samt 65 tester i Kunskapsgymmet: godkända.
- Samtliga 101 elevkort och 53 läraruppgifter har kontrollerats för för breda displayformler vid 390 pixels bredd, med appens text- och facitklasser. Inga displayformler kräver sidscrollning. Utvalda fristående kort har granskats visuellt på mobil och dator, utan horisontellt överflöde.
- Bankvalidator: 0 ERROR, 8 WARNING, 730 INFO. Varningsantalet är oförändrat.
- Bankfilerna är identiska byte för byte. Inga uppgifter utanför området har ändrats i denna leverans.

Kontrollerna kompletterar den manuella analysen och bevisar inte att hela banken saknar pedagogiska fel.
