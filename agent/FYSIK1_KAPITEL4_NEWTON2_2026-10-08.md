# Fysik 1: Newtons andra lag, 2026-10-08

## Omfattning och arbetssätt

Alla 159 huvuduppgifter i `kap: 4, omr: newton2` har lästs manuellt två gånger. Läsningen omfattar uppgiftstext, lösningsförslag, nivå och samtliga 335 elevkort. Även alla ledtrådar har jämförts med den reviderade frågan. 153 huvuduppgifter och 327 elevkort har ändrats. Uppgifts-ID:n har behållits.

Denna rapport gäller det angivna området. Den innebär inte att hela Fysik 1-banken är färdiggranskad. I kapitel 4 återstår lutande plan, kraftmoment och blandade kraftuppgifter; därefter fortsätter granskningen av senare kapitel och den andra genomgången av hela banken.

## Pedagogik och språk

- Lösningarna visar kraftmodell, enhetsomvandlingar, nödvändiga mellanled och slutsvar utan numrerade lösningssteg.
- Elevkort som visar en ny kraftsituation innehåller den situationens egna förutsättningar. Gamla figurer med fel krafter har tagits bort från berörda kort.
- Varje kort visar de beräkningar som behövs för kortets fråga. I 18 samlade lärarfacit visas 31 identiska inledande beräkningar endast en gång, så att samma acceleration inte räknas om i varje del.
- Formuleringar som ”frilägg” och ”komposant” har ersatts med konkreta instruktioner om att rita krafter eller dela upp en kraft vågrätt och lodrätt där det underlättar frågan eller ledtråden.
- Avrundning anges uttryckligen och toleransen motsvarar den efterfrågade precisionen. Oavrundade mellanvärden används när en tid, sträcka eller kraft räknas vidare.

## Exempel på korrigeringar

- **4.5:** dubbel-escapade formler på elevkort har ersatts med fungerande formler och korta frågor.
- **4.93 d:** kortet innehåller den tidigare saknade fartökningen 900 m/s och har eget fullständigt facit.
- **4.106:** hela kraftberäkningen för de hängande vikterna och snörkraften har skrivits om; en felaktig uppdelning av den tidigare förklaringen har tagits bort.
- **4.206:** uppgiften och kortet gäller en person som hänger i ett räck. Facit behandlar krafterna på personen, med rätt skillnad mellan stöd från en och två händer.
- **4.266:** frågan skiljer mellan bromsarna, vägfriktionen och luftmotståndet. Två överlappande kraftetiketter i lösningsfiguren har flyttats och därefter granskats visuellt.
- **4.559, 4.569, 4.599:** förutsättningarna för vila respektive glidning anges, så att beräkningen inte använder glidfriktion utan att modellen medger rörelse.
- **4.568:** snörets två vågräta delar och den fasta trissans placering beskrivs. Facit visar de tre bromsande krafterna på den undre lådan.
- **4.653 d:** kortet innehåller backens lutning och den konstanta farten. Den gamla drivkraften från den vågräta situationen används inte i backen.
- **4.656 c, 4.659 b–c, 4.662 b, 4.667 c:** gamla avrundade accelerationer har tagits bort ur korttexterna. Kortens lösningar räknar accelerationen från de egna givna värdena.
- **4.650, 4.656, 4.659, 4.662, 4.667, 4.724:** lösningarna visar beräkningarna i de olika rörelsefaserna, inklusive fart vid övergången och extra höjd eller bromssträcka.
- **4.685:** en orimligt lång startacceleration har korrigerats till 5,6 s. Massa, fart och sträcka har räknats om och kontrollerats.
- **4.689:** svar och avrundning stämmer med de två värdesiffror som efterfrågas på korten.
- **4.700, 4.711:** ledtrådarnas felaktiga likheter med avrundade värden har rättats.
- **4.697 och 4.725:** två tidigare nästan likadana kulstötningsuppgifter tränar nu olika obekanta: kraft respektive fart.

## Kalibrering av nivå

Nivån har bedömts efter det arbete eleven faktiskt behöver göra på det enskilda kortet. Antalet nivå 1-kort har ökat från 18 till 36. De består främst av direkt användning av F = ma eller F_g = mg, enkel kraftbalans eller rörelse från vila med given acceleration. Kort med kopplade rörelseekvationer, friktion i flera kontakter eller flera rörelsefaser ligger högre.

| Träningsnivå | Före | Efter |
| --- | ---: | ---: |
| 1 | 18 | 36 |
| 2 | 174 | 165 |
| 3 | 113 | 108 |
| 4 | 22 | 25 |
| 5 | 8 | 1 |

Träningsnivå och betygsnivå bedöms separat. Uppgifter med symboliska härledningar eller längre resonemang kan ha A-innehåll även när träningsnivån är 4.

## Verifiering

- `tools/fysik1-newton2.test.js` räknar alla 135 numeriska huvuduppgifter, med 311 svar, från manuellt avlästa givna värden. Uttrycken hämtar inga tal ur facit eller svarsmetadata.
- Ytterligare 16 uppsättningar kontrollerar förenklade elevkorts egna, ibland avrundade, givna värden.
- Alla 311 oberoende beräknade svar har dessutom provats mot Kunskapsgymmets faktiska självrättning i Chromium: inga fel.
- Hela Fysik 1-banken: 4 977 kort och 32 822 rättningskontroller med rätta svar, alternativa numeriska format, enheter och felaktiga svar: inga fel i kontrollen.
- Formler i uppgifter, facit och kort i båda repona: 24 427 formelförekomster per repo, inga renderingsfel eller presentationsfynd i kontrollen.
- Områdets 50 SVG-figurer har granskats visuellt. Endast lösningsfiguren i 4.266 har ändrade SVG-data; de andra huvudfigurerna är bevarade.
- Testsviter: 114 vanliga tester och 47 SVG-tester i Uppgiftslabbet samt 65 tester i Kunskapsgymmet, samtliga godkända.
- Särskild visuell kontroll av fristående kort på 390 och 1174 pixels bredd: inga formelfel, numrerade lösningslistor eller sidöverflöden.
- Bankvalidatorn ger 0 ERROR, 8 WARNING och 655 INFO. Varnings- och informationsantalen är oförändrade från föregående leverans.
- Uppgiftsbanken synkroniseras från Uppgiftslabbet till Kunskapsgymmet och är identisk byte för byte.

De automatiska kontrollerna kompletterar den manuella läsningen. De kan inte bevisa att varje formulering i hela banken är pedagogiskt färdig.
