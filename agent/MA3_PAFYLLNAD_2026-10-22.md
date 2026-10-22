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
