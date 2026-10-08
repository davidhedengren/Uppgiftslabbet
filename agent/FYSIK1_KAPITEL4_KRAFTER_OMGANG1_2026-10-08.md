# Fysik 1: kapitel 4, första kraftomgången

277 huvuduppgifter och deras 409 kort (inklusive odelade uppgifter) har lästs manuellt: tyngdkraft, normalkraft, Newtons första och tredje lag, fjädrar och gravitation. Alla huvudfrågor, huvudfacit och fristående kort har lästs. Reviderade beräkningar, fristående kort och huvuduppgifternas motsvarande data har kontrollerats igen. Detta är en delomgång i kapitel 4. Friktion, Newtons andra lag, lutande plan, moment och blandade kraftuppgifter återstår för kapitlets fullständiga manuella genomgång.

227 huvudposter har ändrats. JSON-loggen anger ändrade fält för varje post. Endast Fysik 1-banken ändras och banken är byteidentisk i båda apparna.

## Viktigaste rättningarna

- Gravitationsfacit 4.9 saknade kvadraten på planetens radie. 4.379 och 4.385 saknade kvadraten på avståndet till den andra massan. 4.348 och 4.354 hade fel uppställda avståndskvoter. Formler och beräkningar har rättats, även i fristående kort.
- Blykloten i 4.746 skulle överlappa vid det gamla centrumavståndet. Avståndet ändras från 4,50 till 45,0 cm och den uppmätta kraften från 7,51 · 10⁻⁹ till 7,51 · 10⁻¹¹ N. Uppgiften ger samma avsedda gravitationskonstant och använder en möjlig geometri.
- 4.502 blandade ihop statisk friktion med glidfriktion. Det felaktiga påståendet om att friktionen alltid ändras proportionellt mot normalkraften har tagits bort.
- Reaktion, bromsning och acceleration skiljs åt i hissuppgifter. Vågens utslag följer den angivna modellen. Fjäderuppgifter anger vid behov att vikten är stilla i förhållande till hissen.
- Fristående fjäder- och kraftkort redovisar beräkning av fjäderkonstant, repkraft eller kraftkomposanter när dessa behövs. Inga svar måste hämtas från a), exempelvis 4.63 d, 4.181 d, 4.671 b–c och 3.334–3.344 b.
- 4.494 frågade tidigare efter acceleration utifrån en medelkraft. Frågan gäller nu uttryckligen medelacceleration. Onödiga uppgifter om kulans massa tas bort.
- Avrundningskrav och svarstoleranser hänger ihop. Korrekta oavrundade värden godkänns också. Enkla direktberäkningar och grafavläsningar placeras på nivå 1; rutinberäkningar på nivå 2; längre kraftbalanser behåller högre nivå.
- Varje deluppgift har en egen rad. Facit använder förklarande stycken och beräkningar, utan numrerade steglistor. Likhetstecken mellan avrundade och exakta värden har rättats där de identifierats.
- 152 SVG-figurer i dessa områdens huvudfrågor och facit har granskats visuellt. Överlappande kraftnamn i 4.133, 4.142 och 4.150 har flyttats och kontrollerats igen. Ett missvisande nedåtriktat kraftdiagram tas bort från det fristående uppåtdragningskortet 4.98 c.

- Självrättningen i Kunskapsgymmet avrundade mycket små tal till noll via algebrabiblioteket. Numeriska uttryck beräknas nu med den strikta räknarparsern och jämförs på talens egen skala. I 4.736 b godkänns 3,6 · 10⁻⁴⁷ N och det oavrundade värdet, medan halva kraften och noll underkänns. Regressionstest omfattar både rätta och felaktiga små tal.

## Verifiering

- Alla 180 numeriska huvuduppgifter i de sex områdena: 317 svar kontrollerade med oberoende transkriberade givna värden i `tools/fysik1-kapitel4.test.js`. Beräkningarna hämtar inte värden från facittexten.
- Hela Fysik 1: 4977 aktiva kort kontrollerade med Kunskapsgymmets verkliga självrättning. 32822 kontroller inklusive negativa svar på talens egen skala (halvt, dubbelt, noll och motsatt tecken), utan fel eller KaTeX-fel. Separat passerar 19 riktade kontroller av avrundning, enheter och mycket små tal. Kortens frågor och facit har även kontrollerats visuellt i mobil- och skrivbordsbredd.
- Alla frågor, lösningar, ledtrådar och deluppgifter renderade i båda apparna: 25296 matematikuttryck per app, inga KaTeX-fel eller numrerade fysiksteglistor.
- 108 tester i Uppgiftslabbet utöver SVG-sviten och 65 tester i Kunskapsgymmet passerar. SVG-sviten gav 46 godkända tester; testet för 4.133 uppdaterades efter att dess etikettöverlappning rättats och passerade separat.
- Bankvalidatorn: 0 ERROR, 8 WARNING och 655 INFO. Dubblettvarningarna gäller tidigare dokumenterade diagramuppgifter vars olika figurer utelämnas ur textjämförelsen.

Automatiska gröna kontroller är inte ett påstående om att alla kursens uppgifter är pedagogiskt färdiggranskade. Fortsätt med de återstående kraftområdena, kapitel 5–9 och en andra helhetsrunda.
