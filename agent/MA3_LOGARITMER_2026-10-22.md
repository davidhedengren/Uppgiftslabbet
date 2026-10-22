# Ma3 – naturliga logaritmer, 2026-10-22

Åtta nya uppgifter i `naturliga_logaritmer`, för både 1b och 1c. Före:
24 huvuduppgifter, 20 spelbara. Efter: 32 huvuduppgifter, 28 spelbara.
Området hade framför allt liknande exponentialekvationer. Tillägget tränar
inversa funktioner, definitionsmängd, tecken, logaritmlagar och feltolkningar.
Sju nya kort på nivå 1 och ett på nivå 2. Innehållet hör till kursens
exponentialfunktioner, talet e, naturliga logaritmer och algebra.

## Alla granskade uppgifter

| ID | Utfall och innehåll | Kommentar / verifierat facit |
|---|---|---|
| 2.1150 | Ny, nivå 1: ln som funktionsmaskin | ln x=−2 ger x=e⁻²=1/e². Exakt svar krävs. |
| 2.1151 | Ny, nivå 1: två funktioner efter varandra | e^(ln 8)=8; ln ger exponenten som behövs. |
| 2.1152 | Ny, nivå 1: tecken i ln-grafen | För 0<x<1 är ln x negativt. |
| 2.1153 | Ny, nivå 1: exponent med basen e | ln(e⁴)=4. |
| 2.1154 | Ny, nivå 1: skärning mellan eˣ och y=3 | x=ln 3≈1,10. Uppgiften ber om två decimaler; 1,1 godtas också. |
| 2.1155 | Ny, nivå 1: tillåtna indata | Både 0,5 och 3 fungerar. 0 och −2 har ingen reell naturlig logaritm. |
| 2.1156 | Ny, nivå 1: en enda logaritm | ln 2+ln 7=ln 14. `en_logaritm` kräver den uttryckligen efterfrågade formen. |
| 2.1157 | Ny, nivå 2: felsöka en logaritmlag | ln(2+3)=ln 5, men ln 2+ln 3=ln 6. |
| 2.414 | Åtgärdad ledtråd, pedagogiskt förtydligat facit | Svaret e³ var korrekt. Ledtråden kopplar nu ln till potenser med basen e; den uppmanar inte längre till att isolera en exponentialterm som saknas. |
| 2.124 | Pedagogiskt förtydligande | Svaret ln 12/ln 5 var korrekt. Lösningen visar nu logaritmeringen och divisionen med ln 5. |
| 2.129 | Pedagogiskt förtydligande | Svaret ln 7 var korrekt. Lösningen visar varför ln(eˣ)=x. |
| 2.134 | Pedagogiskt förtydligande | Svaret ln 10/ln 2 var korrekt. Nu syns både divisionen med 4 och logaritmsteget. |
| 2.413 | Kortare, uppgiftsspecifik ledtråd och lösning | Svaret ln 12 var korrekt. Ledtråden handlar direkt om exponenten till e. |
| 2.816 | Granskad – inget fel, oförändrad | Sätt t=eˣ. (t−2)(t−3)=0 ger x=ln 2 eller ln 3; båda rötterna godtas även i omvänd ordning. |

De åtta nya uppgifterna är **Granskad – inget fel** efter konstruktionskontroll.
Äldre svarsfel: inga. Fem äldre uppgifter har fått nya `s`/`ledtrad`; andra
fält är bevarade. Den felaktiga ledtråden i 2.414 följdes upp med fem
jämförelser: 2.124, 2.129, 2.134, 2.413 och 2.816. Kommentarerna ovan är
förslag för dokumentation/återkoppling, inte skickade meddelanden.

## Pedagogik, verktyg och figurer

- Fyra egna SVG-figurer: två funktionsdiagram och två grafer. Övriga frågor
  prövar korta symboliska samband eller definitionsmängd; en extra figur
  skulle upprepa alternativens information eller ge bort metoden.
- 2.1151, 2.1153 och 2.1156 saknar räknare: inverssamband respektive
  symbolisk logaritmlag är själva innehållet. Övriga kort tillåter räknare.
  Inget kort behöver GeoGebra. Konsumentens `raknareTillaten` verifierad.
- Samtliga kort är självständiga; inga resultat från andra frågor behövs.
- Tidigare granskning `MATO1_KALIBRERING_2026-10-08.json` lästes: den tog
  bort generiska förord i dessa fem facit. De nya förklaringarna är
  uppgiftsspecifika och återinför inte sådana förord.
- Förbättrade äldre lösningar behöver ingen figur för de korta algebraiska
  övergångarna. Facit använder förklaring, beräkning och tydlig svarsruta.

## Verifiering

- `tools/ma3-logaritmer-2026-10-22.test.js`: tre testgrupper godkända.
- Konsumentens motsvarande `.browser.cjs`: **182 kontroller** i faktiska
  svarsfält, 28 elevvyer och 28 lärarvyer på 390/1280 px. Alla 15 icke-tomma
  flervalskombinationer prövade i var och en av de tre nya flervalsfrågorna.
- Exakta potenser, 1/e², logaritmkvoter, naturliga vänsterled, decimaltecken,
  efterfrågad precision och rätt respektive fel svar kontrollerade.
  Oförändrad summa/decimaltal underkänns där en enda logaritm efterfrågas.
- Fyra SVG: noll ERROR/WARNING. Fyra INFO avser avsiktlig vit bakgrund vid
  bildkanten. Logaritmkurvans synliga del börjar vid y=−2, utan ritade
  segment utanför figuren. Samtliga figurer visuellt granskade.
- Full bankvalidator: 1539 ERROR, 230 WARNING, 1446 INFO före och efter;
  inga nya fynd. Äldre fynd ligger utanför uppdraget.
- Regressionen ”Uttryckligt logaritmkrav …” i
  `tools/felrapporter-2026-10-16.test.js` är godkänd. Hela den äldre filen
  har ett oberoende kvarstående fel: rapportlistan kräver Ma2 4.142 som
  tagits bort enligt användarbeslut 2026-10-22. Övriga åtta grupper passerar.
  Varken Ma2-banken eller testfilen ändrades här.
- Strukturell diff: åtta tillagda ID:n och endast `s`/`ledtrad` ändrade i
  de fem äldre uppgifterna. Bankkopiorna i båda repona är identiska.

## Kurskort

De tidigare kursnamnen visas nu på egen rad under huvudnamnet med 16 px text.
Mobil/dator samt spårbyte verifierade i båda apparna. Separat push:
Uppgiftslabbet `e0be38a`, Kunskapsgymmet `f7a51c4`.
