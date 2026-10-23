# Ma3: andraderivatan, 2026-10-23

Sex nya uppgifter: **3.1201–3.1206**, alla med egna SVG-grafer. Tre på
nivå 1, en på nivå 2 och två på nivå 3. Båda spåren 1b/1c. Området hade
47 huvuduppgifter, varav 25 spelbara och tre uttryckligen på nivå 1.
Nu 53/31/6. Dessa antal avser huvuduppgifter, inte expanderade delkort.

De 47 äldre uppgiftstexterna inventerades för variation. Tidigare beslut
för 3.1173–3.1180 i `PAFYLLNAD_LOGG_2026-10-21.md` bevaras. De nya korten
fyller framför allt luckan mellan enkel andraderivering och mer sammansatt
grafanalys. Inventeringen innebär inte fullständig granskning av äldre facit.

## Samtliga granskade uppgifter och kommentarsförslag

| ID | Nivå | Innehåll och verifierat facit / kommentarsförslag |
|---|---:|---|
| 3.1201 | 1 | Lutningen på f′-grafen ger f″(2)=(0−2)/(3−1)=−1. |
| 3.1202 | 1 | En konstant förstaderivata −4 har andraderivatan 0. Grafens höjd är inte dess lutning. |
| 3.1203 | 1 | En stigande f′-graf ger positiv f″, även när hela f′-grafen ligger under x-axeln. |
| 3.1204 | 2 | f=x³−3x ger f′=3x²−3 och f″=6x. Därför är f″(1)=6, inte punktens y-värde −2. |
| 3.1205 | 3 | Vid x=3 är f′ positiv och dess graf sjunkande. Funktionen ökar samtidigt som dess lutning minskar. |
| 3.1206 | 3 | f″=2 betyder att f′ ökar, men avgör inte dess tecken. Motexemplet f=x²−6x är avtagande för 0<x<2. |

- **Granskad – inget fel:** alla sex efter konstruktionskontrollen.
- **Åtgärdade äldre uppgifter:** inga. Äldre texter, facit och metadata oförändrade.
- **Kvar att utreda i denna omgång:** inget. Detta är inte ett påstående om
  att resten av banken är färdiggranskad.
- Kommentarerna är dokumentation/förslag; inga rapportstatusar eller
  elevmeddelanden ändrades i produktion.

## Pedagogiska beslut

Nivå 1 prövar ett grundsamband mellan f′-grafens lutning och f″. Nivå 2
kräver två deriveringar före insättning. Nivå 3 kombinerar två villkor
eller värderar en slutsats med ett motexempel. Uppgifterna kräver inte
begreppet inflexionspunkt.

Miniräknare tillåts i alla sex; GeoGebra behövs inte för de givna enkla
graferna eller polynomderiveringen. Alla är fristående kort. Figurerna
anger tydligt om de visar f, f′ eller f″. Faciten skiljer konsekvent på
funktionsvärde, förstaderivata och andraderivata. Flervalsalternativen
innehåller relevanta missuppfattningar och har varierad placering av rätt svar.

## Verifiering och filer

- Master: `uppgiftermato1.js`, detta dokument, felmönsterregistret,
  `tools/ma3-andraderivata-2026-10-23.test.js`, cacheversion i `index.html`.
- Konsument: identisk bank, cacheversion och motsvarande `.browser.cjs`.
- Tre testgrupper godkända: oberoende beräkningar, metadata och alla
  faktiskt utritade kurvkoordinater. Föregående förändringskvottest och
  konsumentens `funktionsvansterled-2026-10-22.test.js` godkända.
- 126 kontroller genom den verkliga självrättningen: alla kombinationer
  av flervalsalternativ, alternativa primtecken och f''(x)= framför tal.
  Även felaktiga värden prövade och underkända.
- 12 elevvyer och 12 lärarvyer på 390/1280 px: inga JavaScript-/KaTeX-fel
  eller överflöden. Figurgalleriet och mobilkort visuellt granskade.
- SVG: noll ERROR/WARNING. Sex INFO gäller den vita bakgrundens kantläge.
- Full bankvalidator: 1519 ERROR / 230 WARNING / 1446 INFO före och efter;
  inga nytillkomna fynd. Äldre fynd ligger utanför nykonstruktionen.
- Strukturell diff visar enbart de sex nya objekten; inga gamla ändrades
  eller togs bort. Orelaterade fysikutkast och prototyper är bevarade.
