# Ma3c – areasatsen, 2026-10-22

Åtta nya uppgifter, 4.512–4.519, alla med egna SVG-figurer. Området
`areasatsen` växer från 31 till 39 huvuduppgifter. Antalet spelbara
huvuduppgifter med uttrycklig nivå 1 ökar från en till sex.
Fem nya uppgifter är nivå 1, tre är nivå 2. Samtliga är E och hör endast
till 1c-spåret. De 31 äldre uppgifternas innehåll inventerades för variation;
detta är inte en fullständig ny granskning av deras facit eller metadata.

## Alla granskade nya uppgifter och kommentarer

| ID | Nivå / innehåll | Kommentar / verifierat svar |
|---|---|---|
| 4.512 | 1: välja beräkning från figur | Arean är 8·6·sin 50°/2. Vinkeln ligger mellan de kända sidorna. |
| 4.513 | 1: seglets area | 7·12·sin 30°/2=21 m². Även 210000 cm² godtas. |
| 4.514 | 1: ändra en sida | När en av sidorna fördubblas och den andra sidan samt vinkeln bevaras, fördubblas arean. Både 2 och ”dubbelt” godtas. |
| 4.515 | 2: jämföra två trianglar | Samma sidprodukt och sin 60°=sin 120° ger lika stor area. |
| 4.516 | 1: faktor 1/2 i triangelformeln | Diagonalen delar parallellogrammen i två lika stora areor: 58/2=29 cm². |
| 4.517 | 1: avläsa vinkel vid största area | Grafens topp ligger vid 90°. |
| 4.518 | 2: bortskuren triangel | 12·5−8·6·sin 30°/2=60−12=48 cm². |
| 4.519 | 2: först hitta vinkeln mellan sidorna | Toppvinkeln är 180°−75°−75°=30°. Arean är 6·6·sin 30°/2=9 cm². |

Alla åtta: **nya, granskade – inget fel** efter konstruktionskontroll.
Åtgärdade äldre uppgifter: inga. Kommentarerna är förslag för dokumentation
eller återkoppling; inga rapportstatusar eller meddelanden sparas i appen.

## Nivå, verktyg och figurer

- Nivå 1 prövar en direkt beräkning eller ett grundläggande samband.
  Jämförelsen av sinusvärden, subtraktionen av två areor och den föregående
  vinkelberäkningen ligger på nivå 2.
- Miniräknare tillåts på alla kort. Ingen digital ritning eller grafanalys
  behövs, så GeoGebra är inte aktiverat. Lärar- och spelkort är samma
  självständiga uppgift; inga osynliga delresultat behövs.
- Figurerna byggs från de givna sidorna och vinklarna. Trubbig vinkel
  ritas trubbig, och vinkelbågen ligger mellan rätt sidor. I 4.519 är
  toppvinkeln geometriskt 30°, så båda basvinklarna verkligen är 75°.
- Två etiketter som låg nära en sida flyttades efter SVG-kontroll.
  Romerska I/II placerades vid respektive jämförelsetriangel.
- Tidigare FP55 läst: ingen generisk triangel återanvänds med oförenliga
  sidlängder. Alla längder, vinklar och färger är läsbara på vit figuryta.

## Verifiering

- `tools/ma3-areasatsen-2026-10-22.test.js`: tre grupper godkända, inklusive
  oberoende areaberäkningar och mätning av vinklar/sidförhållanden ur
  SVG-polygonernas faktiska koordinater.
- Konsumentens motsvarande browserprov: 122 kontroller av verkliga
  svarsfält, med enhetsbyten, ordet ”dubbelt” och felaktiga svar.
  Alla 15 icke-tomma valkombinationer prövas i båda flervalsfrågorna.
- 16 elevvyer och 16 lärarvyer på 390/1280 px. Inga JavaScript-/KaTeX-fel
  eller överflödande innehåll. Kontroll av konsumentens urval: alla åtta
  finns i 1c och ingen i 1b.
- Åtta figurer visuellt granskade. Slutlig SVG-kontroll: noll ERROR/WARNING.
  Åtta INFO avser vit bakgrund vid kanten och nio INFO avser vinkelbågar
  vars ben ligger i polygoner; vinklarna är kontrollerade separat.
- Full bankvalidator: 1539 ERROR, 230 WARNING, 1446 INFO före/efter.
  Inga nya fynd; äldre fynd utanför denna delomgång kvarstår.
- Endast åtta nya bankobjekt. Äldre uppgifter oförändrade. De två
  bankkopiorna är identiska; pausade lokala fysikutkast ingår inte.
