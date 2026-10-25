# Ma1 digital ekvationslösning: kaströrelser, parabler och exponentialfunktioner, 2026-10-25

Läraren vill att grafisk lösning också ska innehålla svårare funktioner, till exempel kaströrelser med \(s=v_0t+\frac{at^2}{2}\) och exponentialfunktioner.

**Lärarbeslut om placering:**
- Sådana uppgifter hör till digitala hjälpmedel.
- I Ma2:s `grafisk_losning_ekvationssystem` ska bara linjära ekvationssystem finnas.

Korten ligger därför i Ma1 `grafisk_ekvationslosning` (”Grafisk och digital ekvationslösning”), i delmomentet ”Ekvationslösning med digitalt verktyg”. Dit flyttades tidigare korten från det gamla området `digital_ekvationslosning`. Inga kort i Ma2:s ekvationssystem är icke-linjära, vilket testet kontrollerar.

## Nya kort (14, 2.632–2.645): 2 på nivå 1, 7 på nivå 2 och 5 på nivå 3

| Nivå | Innehåll |
|---|---|
| 1 | Kastad boll på höjden 15 m (graf och streckad linje), \(x^2=x+6\) ur figur |
| 2 | Tid ur \(s=2t+1{,}5t^2\) (graf), \(2^x=x+3\) (figur), när exponentiell tillväxt går om linjär (graf), läkemedel \(400\cdot0{,}8^t=100\) (graf), \(x^2-3=2x+5\) (figur), \(3\cdot1{,}5^x=12\) med digitalt verktyg, varför \(h(t)=25\) har två lösningar (flerval) |
| 3 | Bromssträcka där bara en av två lösningar är rimlig, två kast från olika höjd, landningstid för en kula (\(h=1{,}8+14t-4{,}91t^2\)), två exponentiella sparkonton, den negativa lösningen till \(2^x=x^2\) |

- Alla kort har GeoGebra och miniräknare tillåtna, och kurstaggarna är 1a, 1b och 1c.
- Decimalsvar har precisionen i parentes och toleransen ett halvt avrundningssteg.
- Elva figurer finns: grafer med sammanhang, streckade nivålinjer och två kurvor i samma koordinatsystem.

## Kontroll

- Inget nytt kort har samma facit som ett annat kort i området. Tre kort fick nya tal eller en ny fråga, eftersom området redan har många små heltalssvar.
- Validatorn för Ma1 ger inga nya fynd (201 före och efter). SVG-granskaren ger 0 fynd efter att tre etiketter flyttats.
- `tools/ma1-digital-ekvationslosning-2026-10-25.test.js` ger 2/2 pass. Testet räknar om rötterna med bisektion och kontrollerar placeringen.
- Självrättningen i Kunskapsgymmet testades i webbläsaren med 26 svar, och alla gav väntat resultat. Testet täckte bland annat:
  - att för grov avrundning underkänns;
  - båda minustecknen;
  - lösningar i valfri ordning;
  - att den orimliga lösningen 7,2 s underkänns.
- Infogningsskriptet tål nu tomma rader före `];` i bankfilen. En annan session hade lagt till en sådan rad.
