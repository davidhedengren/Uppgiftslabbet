# Ma3: förändringskvoter, 2026-10-23

Nio nya uppgifter: **2.1176–2.1184**. Fyra på nivå 1, två på nivå 2 och
tre på nivå 3. Båda spåren 1b/1c. Området hade 32 huvuduppgifter, varav
26 spelbara och fyra uttryckligen på nivå 1. Nu 41/35/8. Antalen avser
huvuduppgifter, inte expanderade delkort.

De 32 äldre uppgiftstexterna inventerades för variation, särskilt
2.01, 2.37, 2.518, 2.762, 2.810 och 2.1138–2.1143. Detta är ingen
fullständig omgranskning av dem. De nya uppgifterna kompletterar vanliga
beräkningar från funktionsuttryck med enheter, tabeller, negativa ändringar,
olika långa tidsintervall och omvända problem.

## Samtliga granskade uppgifter och kommentarsförslag

| ID | Nivå | Innehåll och verifierat facit / kommentarsförslag |
|---|---:|---|
| 2.1176 | 1 | Välj rätt kvot ur en tabell: (24−12)/(6−2)=3. Förändringarna måste tas i samma ordning. |
| 2.1177 | 1 | Kostnad i kr delad med körsträcka i km ger kr/km. |
| 2.1178 | 1 | Vattennivån sjunker: (4−10)/(4−1)=−2 cm/min. |
| 2.1179 | 1 | Intervall med längden ett: (8−11)/(8−7)=−3. |
| 2.1180 | 2 | Planta A växer 12/4=3 cm/dygn; B växer 15/6=2,5 cm/dygn. Störst total ökning betyder inte störst hastighet. |
| 2.1181 | 2 | Saknad volym: 38+12·(5−2)=74 liter. 36 liter är bara ökningen. |
| 2.1182 | 3 | Olika långa perioder: (2·3−1·6)/9=0 °C/h. Ett vanligt medelvärde av hastigheterna blir fel. |
| 2.1183 | 3 | Okänd parameter: [(16+4a)−(1+a)]/3=8 ger a=3. |
| 2.1184 | 3 | Okänd slutpunkt: (b²+2b−3)/(b−1)=b+3=8 ger b=5. Villkoret b>1 utesluter den ogiltiga punkten b=1. |

- **Granskad – inget fel:** samtliga nio efter konstruktionskontrollen.
- **Åtgärdade äldre uppgifter:** inga. Inga gamla objekt eller facit ändrades.
- **Konstruktionsjustering:** facit till 2.1181 fick radbrytning efter att
  webbläsartestet påvisat en för lång beräkningsrad på mobil.
- Kommentarerna är dokumentation/förslag; inget skickades till användare
  och inga rapportstatusar ändrades.

## Pedagogik, verktyg och figurer

Nivå 1 prövar ett direkt grundsamband. Nivå 2 kräver jämförelse av två
kvoter eller rekonstruktion av ett slutvärde. Nivå 3 kräver att eleven
bygger ett samband: sammanväger tidsintervall, bestämmer en parameter
eller ett okänt intervall. Alla kort är fristående med pedagogiskt facit
i `facit-v2` och en tydlig slutrad.

Miniräknare tillåts i alla nio. GeoGebra behövs inte: graferna finns redan,
och uppgifterna prövar grundsamband samt enkel algebra. Tre egna SVG-figurer
och fyra smala tabeller. Övriga två är korta begrepps-/algebrafrågor där
en figur bara skulle upprepa texten. Kurvorna följer sina modeller,
tidslinjens perioder har längdförhållandet 1:2. Alla figurer visuellt granskade.

## Verifiering och filer

- Master: `uppgiftermato1.js`, detta dokument, felmönsterregistret,
  `tools/ma3-andringskvoter-2026-10-23.test.js`, cacheversion i `index.html`.
- Konsument: identisk bankkopia, cacheversion och motsvarande `.browser.cjs`.
- Tre automatiska testgrupper: omräkning, metadata och faktiska grafkoordinater.
- 160 kontroller genom faktisk självrättning, inklusive alla kombinationer
  av flervalsalternativ, enheter, negativa tal och a=/b=. Felaktiga svar
  och fel enheter underkänns.
- 18 elevvyer och 18 lärarvyer på 390/1280 px: inga JavaScript-/KaTeX-fel
  eller överflöden efter radbrytningen.
- SVG: noll ERROR/WARNING. Tre INFO gäller avsiktlig vit bakgrund vid kanten.
- Full bankvalidator: 1519 ERROR / 230 WARNING / 1446 INFO före och efter;
  inga nya fynd. De äldre fynden omfattas inte av denna nykonstruktion.
- Strukturell diff: bara nio tillägg, inga ändrade eller borttagna äldre objekt.
  Orelaterade fysikutkast och lokala prototyper ingår inte i leveransen.
