# Ma3b/3c – deriveringsregler, 2026-10-22

Elva nya uppgifter, 2.1165–2.1175: sex på träningsnivå 1, två på nivå 2
och tre på nivå 3. Åtta har egna SVG-figurer och en har en tabell.
Området växer från 61 till 72 huvuduppgifter. Antalet spelbara
huvuduppgifter med uttrycklig nivå 1 ökar från en till sju. Äldre
avstängda huvuduppgifter räknas inte som tillgänglig mängdträning.

## Alla granskade nya uppgifter och förslag på kommentarer

| ID | Nivå | Innehåll och verifierat svar / kommentar |
|---|---|---|
| 2.1165 | 1 | Konstant funktion: f=7 har derivatan 0. Vågrät graf. |
| 2.1166 | 1 | Linjär funktion: f=−3x+5 har derivatan −3. Avtagande graf. |
| 2.1167 | 1 | Kvadratens area A=x² har derivatan 2x. Figur med sidmått. |
| 2.1168 | 1 | Felsökning: derivatan av 4x³ är 12x²; exponenten måste minska. |
| 2.1169 | 1 | x² och x²+4 har samma derivata. Två kurvor med tydliga etiketter. |
| 2.1170 | 1 | Tabell: f′(−2)=3·(−2)²=12. Även hela detta svarsvänsterled godtas nu. |
| 2.1171 | 2 | Okänd koefficient: derivatan av ax² ska vara 6x, alltså a=3. |
| 2.1172 | 2 | Rektangel: utveckla x(x+4) innan derivering; A′=2x+4. |
| 2.1173 | 3 | Tangenten ger lutningen 4 och f(1)=2. För f=x²+ax+b blir a=2, b=−1. Namngivna fält. |
| 2.1174 | 3 | Två vagnar: derivera sträckfunktionerna och lös 3t²=12t. Tiderna är 0 s och 4 s, i valfri ordning. |
| 2.1175 | 3 | Ett andragradspolynom kan inte vara lika med sin linjära derivata för alla x. Enstaka sammanfallande värden räcker inte. |

Alla elva är **nya, granskade – inget fel** efter konstruktionskontrollen.
I 2.1170 upptäcktes ett gemensamt rättningsfel som åtgärdas i appen.
Tre figurplaceringar förbättrades under kontrollen; detta är inga öppna fel.

## Åtgärdad självrättning och fem äldre jämförelser

`hogerled` kände inte igen negativa argument: `f'(-2)=12` avvisades
trots att `12` godkändes. Nu kan ett funktionsnamn följt av ett signerat
tal och primtecken vara svarsetikett. Detta utvidgar inte stödet till
godtyckliga vänsterled som `x-2=12`. Felaktiga tal ska fortfarande nekas.

| ID | Bedömning och ändring | Förslag på kommentar |
|---|---|---|
| 2.34 | Facit 0 korrekt. Negativt argument får nu stå i svarsetiketten. Miniräknare tillåts. | Åtgärdad självrättning: f′(−1)=0 godtas. Facit var korrekt. |
| 2.142 | Facit 11 korrekt. Samma rättningsändring och verktygsjustering. | Åtgärdad självrättning: f′(−1)=11 godtas, även med tangentbordets vanliga apostrof. |
| 2.177 | Facit 60 korrekt. Samma rättningsändring och verktygsjustering. | Åtgärdad självrättning: f′(−2)=60 godtas. Facit var korrekt. |
| 2.30 | Granskad – inget fel i facit/rättning: f′(2)=19. Endast miniräknare ändrad. | Derivatan är 6x²−5, vilket ger 19 vid x=2. Miniräknare tillåts nu. |
| 2.38 | Granskad – inget fel i facit/rättning: f′(3)=22. Endast miniräknare ändrad. | Derivatan är 6x+4, vilket ger 22 vid x=3. Miniräknare tillåts nu. |

Dessa fem kontroller gäller derivatavärde, svarsinmatning och verktyg,
inte en fullständig omarbetning av deras äldre presentation. Historiken
i `MATO1_KALIBRERING_2026-10-08.json` lästes; dess nivå- och facitbeslut
bevaras. Miniräknaren tar inte bort det som prövas: att derivera och
sätta in rätt x-värde. Därför tillåts den enligt den senare verktygspolicyn.
Inga rapportstatusar eller kommentarer har skickats till användare.

## Nivå, variation och verktyg

- Nivå 1: en grundregel, avläsning av en konstant lutning eller insättning
  i en redan given derivata. Nivå 2: en mellanberäkning eller koefficientjämförelse.
- Nivå 3: koppla tangentens lutning till både derivata och punktvillkor;
  välja hastighetsmodeller och lösa en ekvation med två rötter; respektive
  resonera om likhet för alla x genom polynomgrader. Nivån bygger på
  tankearbetet, inte på stora tal. Dessa tre är C, övriga E.
- Miniräknare tillåts på alla nya kort. Ingen numerisk grafanalys eller
  avancerad symbolhantering behövs. Givna figurer kan läsas direkt, och
  GeoGebra skulle ersätta själva deriveringsmomentet. GeoGebra är därför av.
- Endast tangenten visas i 2.1173. En fullständig funktionskurva skulle
  göra konstanttermen möjlig att läsa av i stället för att bestämma den.
- Sträckgraferna i 2.1174 visar sträcka, inte hastighet. Kurvorna får
  därför inte användas för att jämföra hastighet via samma höjd.
- Alla kort är fristående och har korta sammanhängande facit med de
  avgörande beräkningarna. Inga osynliga tidigare delresultat krävs.

## Kontroller

- Mastertest `tools/ma3-deriveringsregler-2026-10-22.test.js`: fem grupper,
  oberoende numerisk derivering, tangentvillkor, båda tidslösningarna,
  metadata och kontroll av de nya nivå 3-grafernas faktiska SVG-koordinater.
- Konsumentens motsvarande browserprov: 178 rättningskontroller, inklusive
  fem äldre jämförelser, felaktiga svar, ordnade/oordnade fält, enheter och
  alla 15 icke-tomma valkombinationer i de tre flervalsfrågorna.
- 22 elevvyer och 22 lärarvyer på 390/1280 px: inga JavaScript-/KaTeX-fel
  eller överflödande innehåll. Figurer och nivå 3-facit visuellt kontrollerade.
- SVG-kontroll: noll ERROR/WARNING, åtta INFO för den avsiktligt
  heltäckande vita bakgrundens placering vid bildkanten.
- Nytt konsumenttest `tools/funktionsvansterled-2026-10-22.test.js`:
  tre grupper för signerade funktionsargument och felaktiga vänsterled.
  Befintligt `tools/brakuttryck.test.js`: sju grupper godkända.
- Full bankvalidator före/efter: 1539 ERROR, 230 WARNING, 1446 INFO.
  Inga nya fynd. Äldre orelaterade fynd kvarstår.
- Båda bankkopiorna synkas och cacheversionerna höjs. Inga uppgifter tas
  bort. Pausade fysikutkast ingår inte i denna leverans.
