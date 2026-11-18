# Fy1 densitet: blandningsuppgifter på A-nivå, 18 november 2026

## Uppdrag

Felrapport från Uppgiftslabbet 2026-11-18 11:38, Fysik 1 #2.51 (taggen *Fel nivå / poäng*, nivå C (0/3/0)).
Lärarens kommentar: ”Detta är nog mer A-nivå, lägg även till fler uppgifter av denna typen på A-nivå.”
Användaren: ”fyll på med lite tuffare densitetsuppgifter och flytta alla av denna typ till A-nivå”.

**Beslut:** Uppgifter där eleven ska bestämma hur mycket det finns av två ämnen (eller ett okänt ämnes densitet) ur
blandningens densitet räknas som A-uppgifter i Fy1. Eleven måste själv ställa upp ett samband med en obekant i
båda delarna, till exempel \(\rho=x\rho_1+(1-x)\rho_2\) eller \(V=m_1/\rho_1+m_2/\rho_2\). Framåtriktade uppgifter
(blandningens densitet ur kända mängder, som 2.18, 2.53, 2.142, 2.145, 2.189, 2.197 och 2.198) och uppgifter där
bara en del saknas och fås genom subtraktion (2.196, 2.201) är oförändrade på E/C.

## Befintliga uppgifter som flyttats till A

Bara `niva`, `poang` och `traningsniva` är ändrade. Text, facit och självrättning är oförändrade.

| ID | Innehåll | Före | Efter |
|---|---|---|---|
| 2.51 | Guldring: samband och guldets volymandel | C (0/3/0), nivå 4 | A (0/0/3), nivå 5 |
| 2.90 | Vatten och etanol till given massa och volym, och varför volymerna inte adderas exakt | C (0/3/0), nivå 4 | A (0/1/2), nivå 5. Resonemanget i b ger C-poäng. |
| 2.146 | Aluminium och koppar: kopparens volym ur medeldensiteten | C (0/2/0), nivå 4 | A (0/0/2), nivå 4 |
| 2.200 | Mässing: zinkhalt i massprocent ur massa och volym | C (0/2/0), nivå 4 | A (0/0/2), nivå 5 |
| 2.202 | Glycerol och metanol: volym metanol för en given densitet | C (0/2/0), nivå 4 | A (0/0/2), nivå 4 |

2.146 och 2.202 behåller träningsnivå 4. Totalvolymen respektive glycerolvolymen är given, så ekvationen blir kortare.

## Nya A-uppgifter (2.365–2.370), 6 uppgifter och 9 kort

| ID | Delmoment | Sammanhang | Svar | Nivå per kort |
|---|---|---|---|---|
| 2.365 | Sammansatta och ihåliga föremål | Lödtenn i mätglas: volymen läses av i figuren, och tennets massprocent ska bestämmas | 56 % | A, 5 |
| 2.366 | Sammansatta och ihåliga föremål | Mjölk: a) fettets volymandel ur densiteten 1,031 g/cm³, b) fetthalten i massprocent | 3,5 %, 3,1 % | A 5, C 3 |
| 2.367 | Sammansatta och ihåliga föremål | Kylarvätska: a) glykolhalt ur densiteten, b) hur mycket som ska tappas ur och ersättas med ren glykol för 50 % | 36 %, 1,3 liter | A 4, A 5 |
| 2.368 | Densitet, flytförmåga och modeller | Isbit med infrusen sten som svävar i vatten: stenens massa | 15,4 g | A, 5 |
| 2.369 | Sammansatta och ihåliga föremål | Jordens kärna i en tvåskiktsmodell: a) kärnans volymandel, b) kärnans densitet | 16,3 %, 1,1·10⁴ kg/m³ | C 3, A 5 |
| 2.370 | Densitet, flytförmåga och modeller | Fiskeflöte av balsaträ med blyvikt som ska flyta med 80 % under ytan: blyviktens massa | 7,8 g | A, 5 |

- **Figurer:** alla sex har en egen färgsatt SVG-figur i frågan (mätglas före och efter, mjölkglas med fettdroppar, vatten,
  glykol och kylsystem, isbit med sten i vatten, genomskärning av jorden, flöte med 80 %-markering). Figurerna har vit
  bakgrund och fasta färger som övriga Fy1-figurer.
- **Facit** följer `FACITMALL.md`: Givet och sökt, formeln i rubriken (\(m=\rho V\), \(V=m/\rho\), klotets volym,
  nedsänkt andel), insättning och svarsrad som stämmer med `rättSvar` och `svarVardesiffror`. Flera facit har en kontroll.
- **Delkort** börjar med samma inledning och figur. Ett behövt mellanresultat står i delkortets fråga (3,48 %, 36,4 % och
  16,3 %), aldrig i huvudtexten. Med de avrundade mellanresultaten blir slutsvaret detsamma.
- **Verktyg:** miniräknare tillåten, GeoGebra inte (linjära ekvationer).
- **Precision:** `svarVardesiffror` efter de minst noggranna givna värdena. Facit lagras oavrundat.

## Kontroll

- Byggskript: `tools/bygg-fy1-densitet-a-2026-11-18.py` räknar varje svar och kontrollerar med assert. Det flyttar också de
  fem befintliga uppgifterna till A genom att byta bara de tre raderna.
- Regressionstest: `tools/fysik1-densitet-a-2026-11-18.test.js` räknar om svaren oberoende och kontrollerar nivåer,
  facitformat, figurer, självbärande delkort och svarsrader. `fysik1-densitet-facit-2026-11-04.test.js` räknar nu med
  184 uppgifter och 59 delkort.
- Rendering: alla facit, ledtrådar och delkort är renderade med KaTeX i 390 px utan fel och utan för breda rader och
  genomlästa som bilder.
- SVG-granskning: inga ERROR eller WARNING för de nya figurerna. Etiketten för kärnans radie flyttades in i kärnan efter en
  varning. Det som återstår är INFO om att bakgrundsrektangeln ligger mot kanten, vilket är avsiktligt.
- Valideraren: Fy1 har 0 fel, 10 varningar och 761 INFO, alltså samma antal som före ändringen.
- Fy1-testerna (151 filer) ger samma resultat som före ändringen. 14 filer var röda redan innan och berörs inte.
- **Kunskapsgymmet är inte synkat i denna session**, eftersom sessionen inte fick behörighet till det repot. Kopiera
  `uppgifter.js` till Kunskapsgymmet, kontrollera med `cmp` och höj `BANK_VERSION`.
