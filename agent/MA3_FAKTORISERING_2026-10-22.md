# Ma3 – faktorisering, 2026-10-22

Sex nya uppgifter i `faktorisera_polynom`, kapitel 1, för både 1b och 1c.
Före: 22 huvuduppgifter, varav 21 spelbara och tre på nivå 1.
Efter: 28 huvuduppgifter, varav 27 spelbara och sju på nivå 1.
De nya uppgifterna har fyra olika areabilder, en saknad koefficient och
en gemensam parentes. Det ger fler representationer av faktorisering än
de huvudsakligen symboliska uppgifterna i området.

## Alla granskade nya uppgifter

| ID | Nivå och innehåll | Kommentar / verifierat facit |
|---|---|---|
| 1.874 | 1: rektangel med två delar | 3x+12=3(x+4). Den gemensamma höjden är 3. |
| 1.875 | 1: kvadrat och rektangel | x²+5x=x(x+5). Den gemensamma höjden är x. |
| 1.876 | 1: utskuret kvadratiskt hörn | x²−16=(x−4)(x+4), med x>4 i geometrin. |
| 1.877 | 2: saknad koefficient | (x−3)(x+5)=x²+2x−15. Talet i rutan är 5. |
| 1.878 | 1: kvadrat uppdelad i fyra områden | x²+6x+9=(x+3)². Figuren visar delarna x², 3x, 3x och 9. |
| 1.879 | 2: gemensam parentes | 2(x+1)+x(x+1)=(x+1)(x+2). |

Samtliga sex är **nya, granskade – inget fel** efter konstruktionskontroll.
Inga äldre uppgifter ändrades i denna omgång. Kommentarerna ovan är förslag
för dokumentation och återkoppling; inga rapporter har avslutats i appen.

Inför konstruktionen inventerades de 22 befintliga uppgifternas innehåll:
1.06, 1.21, 1.36, 1.41, 1.46, 1.51, 1.113, 1.116, 1.155, 1.215,
1.282, 1.580, 1.818, 1.819 och 1.842–1.849. Den inventeringen avsåg
variation och luckor, inte en fullständig kontroll av deras självrättning.

## Pedagogik och verktyg

- Fyra egna SVG-figurer, visuellt granskade. De två rent algebraiska
  frågorna har ingen extra bild som bara skulle upprepa uttrycket.
- Samtliga uppgifter är självständiga. Nivå 1 innebär ett grundläggande
  faktoriseringssamband; koefficientjämförelse och gruppering ligger på nivå 2.
- Miniräknare tillåts på alla sex. En vanlig miniräknare gör inte själva
  den symboliska faktoriseringen. GeoGebra behövs inte.
- `svarFormat: faktoriserat` används där faktorform uttryckligen efterfrågas.
  Ordningen mellan faktorer och likvärdiga teckenbyten får variera.
  En utvecklad summa är däremot inte den efterfrågade svarformen.
- Facit förklarar det aktuella sambandet och visar beräkningen före svarsrutan.

## Verifiering

- `tools/ma3-faktorisering-2026-10-22.test.js`: två testgrupper godkända,
  med oberoende identitetskontroller och metadata-/formatkontroller.
- Konsumentens motsvarande `.browser.cjs`: **56 kontroller** av faktiska
  svarsfält, 12 elevvyer och 12 lärarvyer på 390 respektive 1280 px.
  Inga JavaScript-/renderingsfel eller överflödande innehåll hittades.
- Omordnade faktorer, naturligt vänsterled och likvärdiga teckenbyten
  godtas. Felaktiga faktorer och utvecklade summor underkänns. Varje
  alternativ i flervalsfrågan har provats. Verktygsbehörigheten kontrollerad.
- Fyra SVG: noll ERROR/WARNING; fyra INFO gäller vit bakgrund vid bildkanten.
- Full bankvalidator: 1539 ERROR, 230 WARNING, 1446 INFO före och efter.
  Inga nya fynd; befintliga fynd är inte åtgärdade genom denna påfyllnad.
- Strukturell diff kontrollerad: endast sex nya ID:n. De två bankkopiorna
  är identiska. Separata, pågående fysikändringar ingår inte i leveransen.
