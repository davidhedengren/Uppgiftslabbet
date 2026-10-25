# Ma2 sats och bevis: figurer till äldre kort, 2026-10-25

> **Återtaget samma dag (lärarbeslut 2026-10-25, andra beslutet).** Läraren tyckte inte om resultatet och menade att figurerna var tvingade. Figurerna togs bort igen från 34 av de 37 korten nedan och från 7 av S6-korten, och korten återställdes exakt till texten före figurerna. Kvar är 3.236, 3.352 och 3.433 här, och 3.2128 i S6. Där handlar uppgiften om en konkret figur eller beräkning. Efter återtagandet har 27 av 76 kort i `sats_bevis` figur. Resten av dokumentet beskriver den första, återtagna revisionen.

**Lärarbeslut 2026-10-25:** ”alltid hellre figur än utan om det är möjligt och tillför något.” Före revisionen hade 31 av 76 kort i `sats_bevis` figur. Nu har 68 av 76 det.

## Princip

Figuren ska göra resonemanget tydligare utan att peka ut det rätta alternativet.

- **Geometriska påståenden:** formerna med lika långa sidor och räta vinklar markerade. För omvändningar ritas satsens figur, aldrig motexemplet. Rektangeln med lika långa diagonaler ritas, men inte den likbenta parallelltrapetsen.
- **Påståenden om x:** tallinjer med lösningsmängder, till exempel ±4 för \(x^2=16\) och strålar för \(x>4\) och \(x^2>16\).
- **Ekvivalens med en konstant:** grafen till \(y=x^2\) och en vågrät linje, och för \(x^2-6x+c=0\) en parabel med två nollställen jämfört med en som bara nuddar \(x=3\). Värdet på \(c\) går inte att läsa av.
- **Delbarhet:** talremsor med de tal som uppfyller varje villkor.
- **Exempel och bevis:** rutor för fall, där några är provade (✓) och resten oprövade (?), och ett motexempel (✗).
- **Påståendets delar:** schemat ”Om [antagande], så [slutsats]”.

## Kort som fick figur (37)

| Typ | Kort |
|---|---|
| Former | 3.11, 3.21, 3.71, 3.83, 3.136, 3.248, 3.249, 3.251, 3.328, 3.426 |
| Vinklar i trianglar | 3.137, 3.196, 3.231, 3.236, 3.352, 3.429, 3.433 |
| Tallinjer | 3.40, 3.104, 3.106, 3.118, 3.250, 3.281, 3.324, 3.356, 3.506 (även i deluppgift a och c) |
| Grafer | 3.51, 3.105, 3.124, 3.437 |
| Talremsor | 3.107, 3.279, 3.300 |
| Exempel, motexempel och påståendets delar | 3.72, 3.252, 3.304, 3.348 |

## Dokumenterade undantag (8)

- **3.277 och 3.278:** frågar vad symbolerna ⇒ och ⇔ betyder. En pilbild vore själva svaret.
- **3.117:** frågar vad ett bevis är. En bild av en slutledningskedja vore alternativ C.
- **3.207, 3.280, 3.305 och 3.329:** direkta insättningar som \(x=2\Rightarrow x^2=4\). En figur gör dem inte tydligare.
- **3.2130:** felet i ”beviset” för 2 = 1 är ren algebra.
- **3.506 del b:** varje figur av en fyrhörning med två par parallella sidor är antingen en rektangel, som är missvisande, eller själva motexemplet.

## Genomförande och kontroll

- **Genomförande:**
  - Bara textsträngen `t` ändrades, plus `fraga` i deluppgift a och c i 3.506.
  - Ett verktyg delar upp arrayen i objekt med en riktig tokenisering och hittar fältet på kortets egen nivå. Det behövs eftersom de äldre korten är kompakt JSON med olika fältordning.
  - Efteråt jämförs hela banken (3 320 kort) med förväntat resultat. Bara de 39 fälten skiljer sig.
- **Validatorn:** 0 fynd i Ma2 för korten.
  - Fynden som först syntes gällde Fy1-kort i `uppgifter.js` med samma ID, eftersom filtret var för brett.
- **SVG-granskaren:**
  - 0 fynd för tallinjer och talremsor efter att etiketterna gjorts större.
  - Graferna har kvar rutinfynd där etiketter rör rutnätet. I 3.124 ligger 1, 3 och 5 avsiktligt där parablerna skär axeln.
- **Mobil (375 px):**
  - Alla 37 figurer visas, utan överskridning och utan KaTeX-fel, och flervalen rättas som förut.
  - Tallinjernas tal och radnamn gjordes större (15 och 16 px), eftersom de blev för små på mobil.
- **Sidonotering:** de äldre figurerna i 3.232–3.239 visas, men saknar `aria-label`. Det fanns sedan tidigare och ingår inte i den här revisionen.
- **Test:** `tools/ma2-satsbevis-figurer-2026-10-25.test.js` kräver figur på alla kort i området utom de åtta undantagen. Alla `tools/ma2-*.test.js` går igenom.
