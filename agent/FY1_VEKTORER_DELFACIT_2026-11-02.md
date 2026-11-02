# Fy1: komponenter i delfacit, 2 november 2026

## Upptäckt och ändring

I uppgift **3.301–3.308 a** skrev lösningen till x-komposanten ut båda krafterna i fullständig vektorform. Därmed visades också de y-komposanter som eleven skulle läsa av och addera i b. Var och en av de åtta a-lösningarna visar nu endast de två x-komposanterna, deras tecken och summan. Hela vektorerna behövs inte för att lösa a. Uppgiftstext, figurer, svar, nivåer, verktygstaggar och helfacit i Uppgiftslabbet är oförändrade.

Matematisk kontroll av \(F_{1x}+F_{2x}\):

| Uppgift | X-komposanter i N | Summa i N |
|---|---:|---:|
| 3.301 | −2 och 2 | 0 |
| 3.302 | −5 och 5 | 0 |
| 3.303 | 4 och −4 | 0 |
| 3.304 | 4 och 2 | 6 |
| 3.305 | 3 och 3 | 6 |
| 3.306 | 1 och −4 | −3 |
| 3.307 | 3 och −1 | 2 |
| 3.308 | −2 och 0 | −2 |

I 3.301 och 3.307 sammanfaller det korrekta x-svaret med y-svaret. Det kan man inte undvika genom att enbart ändra facit; uppgiftsdata har inte ändrats för att dölja ett naturligt sammanfall.

## Liknande granskade uppgifter

- **3.300, 3.309 och 3.312:** granskade – inget motsvarande fel. Deras a-facit behandlar bara x-komposanten.
- **3.311:** granskad – inget motsvarande fel. Delarna efterfrågar fart, tid respektive avdrift; fartlösningen anger inte den senare tiden.
- **3.313:** granskad – inget motsvarande läckage av dolda uppgifter. Senare kortet anger redan hastighetskomponenterna som givna värden; beräkningen i b behöver den y-komposant som efterfrågas där.
- **3.303 b:** granskad – det numeriska svaret råkar vara detsamma som resultantens belopp i c eftersom x-komposanten är noll; detta är en matematisk följd.

En träff i en automatisk siffersökning betyder inte nödvändigtvis svarsläckage. Det kan röra sig om ingångsvärden, nödvändiga mellanled eller samma resultat i olika delar. Denna omgång täcker vektorserien, inte alla uppgifter i banken.

## Test och kommentarsförslag

Riktat banktest kontrollerar de åtta x-summorna och att a-faciten inte skriver ut y-komponenter. Riktigt webbläsarflöde testar alla åtta kedjor på mobil och dator: korrekt x-svar, synlig lösning, fortsatt b och korrekt y-svar. Figuren och lösningen för 3.304 har även kontrollerats visuellt i mobilformat. Tidigare tester för delfacit och kedjor körs igen. Kompletta testsviter körs före push; utfall anges i leveransen.

Förslag till rapportkommentar om denna feltyp: ”Tack! Facit till första delen visar nu endast x-komposanterna, så att du själv kan läsa av y-komposanterna i nästa del.” Ingen rapportstatus eller kommentar har ändrats i appen.

Testutfall: de riktade webbläsar- och banktesterna passerade, liksom tidigare tester för kedjor och heluppgifter. Hela sviten gav 1 062 godkända och 43 sedan tidigare kända SVG-miljöfel i Uppgiftslabbet samt 304 godkända och 10 sedan tidigare kända fel i Kunskapsgymmet.
