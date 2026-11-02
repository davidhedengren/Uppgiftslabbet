# Ledtrådar per del, 2 november 2026

Kunskapsgymmet ärver huvuduppgiftens ledtråd när en del saknar egen. Det är ofta lämpligt, men kan ge hjälp om en annan del och i vissa fall avslöja resultat innan eleven kommer dit. Genomgången sökte i alla sju bankerna efter ärvda ledtrådar och möjliga direkta numeriska läckor; sådana textsökningar bevisar inte att alla ledtrådar är lämpliga.

## Ändrade uppgifter

- **Ma2 1.104 a/b:** tidigare angav den gemensamma ledtråden både \(k=-2\) och \(m=3\) redan under a, medan b frågar efter hela formeln. I a får eleven hjälp att jämföra förändringarna, i b att använda dem och avläsa startvärdet. Eleven räknar själv ut båda koefficienterna. Även a-facit skrev tidigare ut hela formeln; nu räknar det vidare med tabellens konstanta förändring och anger inte b-svaret.
- **Ma2 1.76 a/b:** ledtråden i a angav startvärdet och förändringen som behövs för att skriva modellen. Nu ställer den en fråga om dem. Ledtråden i b vägleder om hur mängden 530 liter används.
- **Ma2 1.234 a:** den gemensamma ledtråden förklarade konstanttermens betydelse trots att det efterfrågas i b. Den nya a-ledtråden handlar bara om att beräkna \(K(5)\); b behåller sin egen ledtråd.
- **Ma3 2.20 a:** den gemensamma ledtråden handlade om tangentens ekvation och passade b, men a frågar efter derivatan. a får nu en separat ledtråd om derivatan av exponentialfunktionen. b behåller tangentledtråden.

I övrigt är uppgiftstexter, facit, svar, nivåer och verktygstaggar oförändrade.

## Jämförda uppgifter utan ändring

**Ma2 1.02, 1.123, 1.138 och 1.81 samt Matf1 1.15** har granskats. Deras gemensamma ledtrådar förklarar metod eller begrepp och skriver inte ut nästa dels specifika svar. I 1.138 är talet 200 uttryckligen givet i b; ledtråden hänvisar endast till metoden. Ledtråden i Matf1 1.15 skiljer tal från mängd utan att ge ett ja/nej-svar.

## Test och rapportkommentar

Riktade banktester kontrollerar ledtrådarnas innehåll. Webbläsartest öppnar alla fyra uppgifter på mobil och dator, visar ledtråden i vardera delen och provar de rätta svaren, inklusive flervalsdelen i 1.234. Tidigare regressionsfall för delkedjor, heluppgifter och vektorer körs också. Hela `tools/*.test.js` körs i båda repona; se leveransen för de tidigare kända testfelen.

Förslag till en rapport om fel ledtråd: ”Tack! Vi har anpassat ledtråden till den aktuella deluppgiften så att den hjälper utan att avslöja ett senare delsvar.” Inga rapportstatusar eller kommentarer har sparats i appen.

Testutfall: samtliga riktade tester passerade. Den kompletta sviten gav 1 064 godkända och 43 tidigare kända SVG-miljöfel i Uppgiftslabbet samt 304 godkända och 10 tidigare kända fel i Kunskapsgymmet. Ett äldre kursinnehållstest fångade ett olämpligt begrepp i ett första utkast till Ma3-ledtråden; formuleringen ändrades och testet passerar nu.
