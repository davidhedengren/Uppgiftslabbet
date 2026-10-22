# Ma3 – exponentialfunktion och derivata, 2026-10-22

Sju nya uppgifter, 2.1158–2.1164, i `derivata_exponential` för 1b och 1c.
Området växer från 24 till 31 huvuduppgifter. Antalet spelbara huvuduppgifter
med uttrycklig nivå 1 ökar från två till sju. Tillägget innehåller fem på
nivå 1, en på nivå 2 och en på nivå 3.

## Alla granskade nya uppgifter

| ID | Nivå / innehåll | Kommentar / verifierat facit |
|---|---|---|
| 2.1158 | 1: samband i tabell | k=10/4=20/8=30/12=2,5. Raderna visar värden i punkter, inte påhittade jämna x-steg. |
| 2.1159 | 1: avtagande graf | I P är f=5. Sambandet f′=−0,4f ger lutningen −2. |
| 2.1160 | 1: mängd och förändringshastighet | M′=−0,2·50=−10 g/min. Minustecknet anger att mängden minskar. Även −600 g/h godtas. |
| 2.1161 | 1: proportionalitet | När f fördubblas fördubblas även 0,08f och därmed derivatan. |
| 2.1162 | 2: gemensamt funktionsvärde, olika lutning | Vid x=0 är f′=1,2 och g′=3. Grafen till g har större lutning. |
| 2.1163 | 3: tillagd konstant | f=4+3e²ˣ ger f′=6e²ˣ=2(f−4). Derivatan är inte 2f. |
| 2.1164 | 1: diagram med f och f′ på axlarna | Den markerade punkten ger k=f′/f=−2/4=−0,5. |

Alla sju är **nya, granskade – inget fel** efter konstruktionskontroll.
Åtgärdade äldre uppgifter: inga. Kommentarerna ovan är förslag och har inte
skickats till någon eller lagts in som rapportstatus i appen.

## Variation, nivå och figurer

- Fyra SVG-figurer: avtagande exponentialkurva, mängd i en lösning,
  jämförelse mellan två exponentialkurvor och ett diagram över f′ mot f.
  Därutöver en lodrät tabell och två korta begreppsfrågor. En extra figur
  i de senare skulle inte bidra utöver de givna symboliska sambanden.
- De enklaste korten ger proportionalitetssambandet och prövar ett enda
  grundsamband. 2.1162 kräver två deriveringar och en jämförelse (nivå 2).
  Att identifiera exponentialdelen efter en vertikal förskjutning i 2.1163
  kräver mer självständigt algebra-/begreppsarbete (nivå 3/C).
- Miniräknare tillåts på alla kort. Ingen digital grafanalys behövs för
  att läsa av de givna figurerna, så GeoGebra krävs inte och är inte aktiverat.
- Figurerna är beräknade från de faktiska funktionerna. I 2.1159 ligger P
  på 10e^(−0,4x) vid x=ln(2)/0,4. I 2.1162 används exakt 6e^(0,2x)
  respektive 6e^(0,5x). Den sista bilden har uttryckligen f(x), inte x,
  på vågräta axeln; facit använder en avläsning som eleven kan göra.
- Tidigare FP58/FP60 lästa. Facit visar regel, relevant insättning eller
  avläsning. Dolda funktionsuttryck behövs inte för att förstå lösningarna.
- Innehållet i de 24 äldre uppgifterna inventerades för variation. Det
  motsvarar inte en fullständig ny granskning av deras facit och rättning.

## Verifiering

- Två testgrupper i `tools/ma3-exponential-2026-10-22.test.js` godkända:
  oberoende beräkningar, numerisk derivatakontroll, tabell-/grafrelationer,
  metadata, nivå, enhet och verktyg.
- Konsumentens `tools/ma3-exponential-2026-10-22.browser.cjs`: 130 kontroller
  i riktiga svarsfält. Alla 15 icke-tomma valkombinationer i var och en av
  tre flervalsfrågor prövas. Korrekt och fel tecken, bråk/decimaler,
  vänsterled och enhetsbyten kontrolleras.
- 14 elevvyer och 14 lärarvyer på 390/1280 px. Inga JavaScript-fel,
  KaTeX-fel eller överflödande innehåll. Figurer visuellt granskade.
- Grafbeteckningarna P, f och g flyttades bort från rutnätslinjer efter
  SVG-kontrollen. Slutlig geometrikontroll: noll ERROR/WARNING och fyra
  INFO om den avsiktliga vita bakgrunden vid bildkanten.
- Full bankvalidator före/efter: 1539 ERROR, 230 WARNING, 1446 INFO;
  inga nya fynd. Äldre fynd utanför denna delomgång kvarstår.
- Endast sju nya bankobjekt; befintliga uppgifter oförändrade. Bankerna
  i båda repona är identiska. Pausade lokala fysikutkast ingår inte.
