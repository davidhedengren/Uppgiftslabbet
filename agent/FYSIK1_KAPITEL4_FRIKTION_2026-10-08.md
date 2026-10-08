# Fysik 1: manuell friktionsgranskning

Samtliga 88 huvuduppgifter och deras 138 kort har lästs manuellt, både före revideringen och i en andra full läsning efteråt. 81 huvudposter har ändrats. Loggen i JSON anger ändrade fält per uppgift. Huvudfrågor, lösningar och fristående kort ingår i granskningen.

## Innehåll och pedagogik

- 4.534 b saknade sträckan som behövdes för att bestämma farten. Kortet anger nu 25 m och lösningen beräknar själv accelerationen innan farten beräknas.
- 4.535 och 4.541 visar hela förloppet: kraftsumma, acceleration, sträcka under drivning, fart när drivningen upphör, retardation, bromssträcka och total sträcka. Beräkningarna använder oavrundade mellanvärden. Numrerade steg används inte.
- Vilofriktion och glidfriktion skiljs åt. I 4.516 anger frågan att samma friktionstal gäller i båda fallen och att släden börjar i vila. Lösningen jämför dragkraften med glidgränsen innan den väljer friktionskraft.
- 4.555 anger att klossen glider uppåt; därmed är friktionen nedåt. Den gamla texten angav inte rörelseriktningen. Normalkraft, friktion, tyngdkraft och uppåtriktad kraft beräknas i lösningen.
- 4.529 frågar efter retardationen vid den angivna farten när luftmotståndet beror på farten. Det står att farten i luftmotståndsformeln anges i m/s.
- 4.547 beskriver motståndsmodellen för en gräsklippare och härleder kraften som krävs när farten ökar. Kort c använder ursprungliga mätvärden och räknar ut motståndstalet; det får inte längre ett avrundat tal som ger ett annat svar än huvuduppgiften.
- Fristående kort räknar om tidigare mellanresultat när de behövs, bland annat i 4.527, 4.543, 4.549 och 4.551. Inga lösningar hänvisar till ett osynligt svar i a.
- Felaktiga formelsymboler där N eller g hamnat i indexet på μ har rättats i 4.57, 4.122 och 4.449.
- Nivå 1 består av enkla direktberäkningar och grafavläsningar. Rutinberäkningar ligger på nivå 2; flera kraftbalanser eller hela rörelseförlopp får högre nivå. Exempelvis flyttas 4.523–4.524 från nivå 2 till 3, medan 4.499 och 4.563 flyttas ned från tidigare överhöga nivåer.
- Frågor anger svarsenhet och avrundning där det behövs. Toleranserna följer kravet och godkänner också de oavrundade fysikaliska värdena. 4.577 b ger det exakta svaret 67,5 N i stället för ett oförklarat heltalsfacit.
- Deluppgifter visas på egna rader. Dubblerade ritinstruktioner och onödig information i kort har tagits bort. Det missvisande lodräta kraftdiagrammet används inte längre i det fristående vågräta dragkortet 4.44 b.

## Kontroller

- Samtliga 70 numeriska huvuduppgifter, 120 svar: oberoende beräkningar från transkriberade givna värden i `tools/fysik1-kapitel4.test.js`. Alla svar ligger inom avsedd avrundningstolerans.
- 130 riktade kontroller med Kunskapsgymmets riktiga självrättning: alla 120 oavrundade fysikaliska svar samt tio kontroller av rätta och felaktiga avrundade svar. Alla passerar.
- Hela kursens 4977 aktiva kort: 32822 kontroller av facit, enheter och felaktiga svar, inklusive halva och dubbla tal, noll och fel tecken. Inga fel eller KaTeX-fel.
- Samtliga frågor, lösningar, ledtrådar och kort renderade i båda apparna utan KaTeX-fel eller numrerade fysiksteglistor.
- Alla områdets 29 SVG-figurer granskade visuellt. Kort för 4.534 b, 4.535 c, 4.516 b och 4.555 b kontrollerade visuellt i mobil- och skrivbordsbredd.
- 110 tester i Uppgiftslabbet utöver SVG-sviten och 65 tester i Kunskapsgymmet passerar. SVG-innehållet i huvuduppgifterna är oförändrat från föregående testade bankversion.
- Bankvalidatorn ger 0 ERROR, 8 WARNING och 655 INFO.

Banken är byteidentisk i båda apparna. Kapitel 4 har nu 365 manuellt granskade huvuduppgifter. Newtons andra lag, lutande plan, moment och blandade kraftuppgifter återstår i kapitlet. Därefter återstår kapitel 5–9 och en andra helhetsrunda. Automatiska kontroller av hela kursen ersätter inte den manuella granskningen.
