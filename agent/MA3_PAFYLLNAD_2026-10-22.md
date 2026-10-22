# Matematik 3: varierad påfyllnad, 2026-10-22

## Omgång 1 – tangent, sekant och gränsvärde

Efter inventering prioriterades `tangent_sekant`: 24 huvuduppgifter, varav
20 spelbara och två uttryckligen på träningsnivå 1 före tillägget.
Antalen avser huvuduppgifter, inte expanderade delkort. Området hör till
tolkning av förändringshastighet och derivata i Matematik – fortsättning
nivå 1b/1c (tidigare Ma3b/Ma3c). Nu 30 huvuduppgifter, 26 spelbara.

Alla nya uppgifter är granskade avseende matematik, facit, metadata, språk,
självrättning och SVG. Befintliga uppgifter har inte ändrats.

| ID | Variation | Nivå | Oberoende verifierat facit / kommentarsförslag |
|---|---|---:|---|
| 1.862 | Böjd kurva men vågrät sekant | 1 | Samma y-värde i ändpunkterna ger (5−5)/(5−1)=0. |
| 1.863 | Negativ tangentlutning och olika axelskalor | 1 | (0−6)/(4−0)=−1,5. Minustecknet visar att linjen sjunker. |
| 1.864 | Vattenmängd, tid och genomsnittlig ökning | 1 | (100−40)/(6−2)=15 liter/minut. |
| 1.865 | En tangent som korsar kurvan | 3 | För x³/4 är derivatan 3x²/4. I origo är lutningen 0; korsningen hindrar inte tangens. |
| 1.866 | Läs lutningen ur tangentens ekvation | 1 | Koefficienten 0,8 är f′(2); 1,4 är linjens skärning med y-axeln. |
| 1.867 | Beräkna en okänd koordinat från sekantlutning | 2 | y=2+2·(4−1)=8. Y-skala saknas avsiktligt så eleven beräknar värdet. |

- **Åtgärdade äldre uppgifter:** inga. Detta är nykonstruktion.
- **Granskad – inget fel:** samtliga sex nya uppgifter efter konstruktionskontroll.
  Kommentarsförslagen i tabellen är dokumentation, inte skickad återkoppling.
- **Jämförelseunderlag för variation:** områdets 24 äldre uppgiftstexter,
  särskilt 1.49, 1.54, 1.566–1.573 och 1.826–1.833. Dessa har bara inventerats
  avseende innehåll/representation, inte fullständigt kvalitetsgranskats här.
- **Verktyg:** miniräknare tillåten i alla sex; aritmetiken är inte målet.
  GeoGebra behövs inte för dessa givna grafer och grundsamband. Alla är
  fristående kort för båda spåren. Inga tidigare resultat behövs.
- **Facit:** kort förklaring, relevant beräkning och tydlig slutrad i
  `facit-v2`/`facit-svar`. Figurerna är egna och matematiskt konstruerade.

### Verifiering

- `tools/ma3-tangenter-2026-10-22.test.js`: omräkning, metadata och kontrakt.
- Konsumentens `tools/ma3-tangenter-2026-10-22.browser.cjs`: 54 svarskontroller,
  12 elevvyer och 12 lärarvyer på 390/1280 px. Inga JS-/KaTeX-fel eller
  horisontella överflöden. Samtliga flervalsalternativ prövade.
- Inga dolda avrundningskrav: −2 godtas som korrekt heltalsavrundning av
  −1,5 enligt användarens beslut. Testet skiljer detta från felaktiga −3.
- SVG-geometrikontroll: noll ERROR/WARNING; sex INFO gäller avsiktlig vit
  bakgrund vid viewBox-kanten. Punktetiketter flyttades efter kontroll.
- Full bankvalidator före/efter: 1539 ERROR, 230 WARNING, 1446 INFO i båda;
  **inga tillkommande fynd**. Äldre fynd ligger utanför denna avgränsning.
- Strukturell diff: endast 1.862–1.867 tillagda; tidigare objekt oförändrade.

## Kursnamn

Separat leverans i båda apparna: gamla kursnamn inom parentes. Översikten
visar Ma1a/Ma1b/Ma1c, Ma2a/Ma2b/Ma2c, Ma3b/Ma3c, Ma4, Ma5, Fy1 och Fy2.
Valt matematikspår visar sitt eget tidigare kursnamn. Kurs-ID och sparade
resultat ändras inte. Lokal webbläsarkontroll på mobil/dator och byte mellan
Ma3b/Ma3c godkända. Commits: Uppgiftslabbet `5b854bb`, Kunskapsgymmet `6ebc5f7`.

## Omgång 2 – derivatans definition

Före: 21 huvuduppgifter, 20 spelbara, två uttryckligen på träningsnivå 1.
Efter: 27 huvuduppgifter, 26 spelbara. Fyra nya på nivå 1, en på nivå 2,
en på nivå 3. Samtliga för 1b/1c. Området hör till derivatans definition
och tolkning, ett centralt grundmoment i Matematik 3.

| ID | Innehåll | Nivå | Facit / kommentarsförslag |
|---|---|---:|---|
| 2.1144 | Tolka h i en graf | 1 | h=4,2−4=0,2; h är ändringen, inte den andra x-koordinaten. |
| 2.1145 | Punkten flyttas till vänster | 1 | h=4,7−5=−0,3. Ett h får vara negativt. |
| 2.1146 | Konstant funktion med definitionen | 1 | (7−7)/h=0 för h≠0. Gränsvärdet och derivatan är 0. |
| 2.1147 | Välja rätt differenskvot | 2 | [2(1+h)²−2]/h; både funktionsvärdena och ändringen i x behövs. |
| 2.1148 | Tabell med h från båda håll | 1 | Kvoten närmar sig 2,5. Tabellen ger en uppskattning, inte ett bevis. |
| 2.1149 | Gränsvärde trots odefinierad kvot vid h=0 | 3 | Kvoten är 2+h för h≠0, så derivatan är 2. Ett hål hindrar inte gränsvärdet. |

Alla sex nya uppgifter är granskade: **Granskad – inget fel** efter
konstruktionskontrollen. Inga äldre uppgifter åtgärdade. Kommentarerna är
förslag/dokumentation; inga rapportstatusar ändrades i produktion.

Områdets 21 äldre uppgiftstexter inventerades för variation, särskilt
2.800–2.809 och 2.1124–2.1131; detta var ingen fullständig omgranskning av dem.
Nya uppgifter kompletterar vanliga beräkningar med definitionens byggstenar.
Alla kort är fristående. Miniräknare tillåten; GeoGebra behövs inte.
2.1148 använder en vertikal tabell som fungerar på mobil. En extra graf
skulle upprepa samma information, så den uppgiften har ingen SVG.

Verifiering: `tools/ma3-definition-2026-10-22.test.js` samt konsumentens
motsvarande `.browser.cjs`. 56 kontroller i riktiga svarsfält, alla alternativ,
12 elevvyer och 12 lärarvyer, 390/1280 px. Inga JS-/KaTeX-fel eller överflöden.
SVG: noll ERROR/WARNING, fem INFO om den vita bakgrundens avsiktliga kantläge.
Etiketter och axeltal flyttades för bättre marginaler. Full validator:
1539 ERROR / 230 WARNING / 1446 INFO före och efter; inga nya fynd.
Enbart 2.1144–2.1149 tillagda, tidigare uppgifter oförändrade.

## Omgång 3 – polynombegrepp, grad och koefficienter

Inventeringen visade 23 huvuduppgifter, varav 20 spelbara. Efter påfyllnad:
29 huvuduppgifter, 26 spelbara. Begreppet polynom ingår i områdets algebra
för både 1b och 1c. Nytt innehåll prövar samma grundbegrepp med flera
representationer, i stället för sex nästan identiska uttryck.

| ID | Variation | Nivå | Facit / kommentarsförslag |
|---|---|---:|---|
| 1.868 | Konstantterm i vertikal värdetabell | 1 | c=p(0)=−3. Termerna med x försvinner vid x=0. |
| 1.869 | Grad för en rektangels areapolynom | 2 | (x+4)(x+1)=x²+5x+4, alltså grad 2. |
| 1.870 | Cirkelyta och π som koefficient | 1 | πx² är ett polynom; koefficienten behöver inte vara ett heltal. |
| 1.871 | Konstantterm som skärning med y-axeln | 1 | d=p(0)=−2. |
| 1.872 | Gradtal efter att termer tagit ut varandra | 2 | 3x⁴−3x⁴=0, kvar är x³+2x² och graden är 3. |
| 1.873 | Ledande koefficient i en lådas volym | 2 | x·2x·(x+1)=2x³+2x²; koefficienten är 2. |

Alla sex är fullständigt konstruktionsgranskade: **Granskad – inget fel**.
Inga äldre uppgifter åtgärdade och inga kommentarer skickade till användare.
Jämförelseunderlaget för variation var de 23 tidigare uppgiftstexterna,
bland annat 1.125, 1.449, 1.463, 1.531, 1.560 och 1.834–1.841; detta
innebär inte en fullständig omgranskning av de äldre uppgifterna.

Tre nivå 1 och tre nivå 2. Area, volym och förenkling kräver flera tankeled
och ligger därför på nivå 2. Miniräknare tillåten; GeoGebra behövs inte och
symboliska verktyg skulle ta över det begrepp som prövas. Alla kort är
fristående. Fyra egna SVG-figurer. 1.868 har tabell; 1.872 har bara ett
kort uttryck eftersom en figur inte tillför något till termförenklingen.

Kontroller: `tools/ma3-polynom-2026-10-22.test.js` samt konsumentens
motsvarande `.browser.cjs`: 42 svarskontroller, 12 elevvyer och 12 lärarvyer
på mobil/dator, inga fel eller överflöden. Även `c=-3` och `d=-2` godtas.
SVG: noll ERROR/WARNING, fyra INFO om vit bakgrund vid viewBox-kanten.
Full bankvalidator oförändrad (1539 ERROR, 230 WARNING, 1446 INFO).
Strukturell diff visar endast de sex nya ID:na 1.868–1.873.
