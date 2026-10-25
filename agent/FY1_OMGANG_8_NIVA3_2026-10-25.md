# Fy1 omgång 8: nivå 3 i a-t-diagram, tyngdkraft, ström och parallellkoppling, 2026-10-25

En genomgång av Fy1 visade att flera områden som undervisats nyligen hade mycket få kort på nivå 3:

| Område | Kort på nivå 3 |
|---|---|
| `tyngdkraft` | 1 |
| `strom` | 4 |
| `parallellkoppling` | 4 |
| `at_diagram` | 5 |

Syntesområdena `blandat_energi` och `blandat_kraft` har få kort på nivå 1–2, men det är avsiktligt. Deras tester låser dessutom exakta antal och facittexter, så de lämnades orörda.

## Nya kort (25): 18 på nivå 3 och 7 på nivå 2

ID: 3.733–3.738, 4.885–4.890 och 8.636–8.648.

| Område | Antal | Innehåll |
|---|---|---|
| `at_diagram` | 6 | Sträcka genom tre faser, läge när rörelsen vänder (negativ starthastighet), triangulärt a-t-diagram, tid till en viss fart i två faser, vilket a-t-diagram som hör till en v-t-graf (flerval), hissens färdsträcka. 4 figurer. |
| `tyngdkraft` | 6 | Tyngd på jorden ur tyngd på månen, största massan man kan lyfta på månen, g ur två mätningar, samma tyngd på olika himlakroppar, balansvåg och fjädervåg (flerval), minskad tyngd på Mars |
| `strom` | 6 | Laddningstid för ett mobilbatteri, ström ur Q-t-graf, elektroner per minut, laddning ur I-t-graf med lutande del, ström i en förgreningspunkt, elektroner i en blixt. 2 figurer. |
| `parallellkoppling` | 7 | Vilken resistor som ska parallellkopplas, en lampa går sönder, resistans ur grenströmmar, tre parallella resistorer, fler parallella lampor (flerval), antal apparater innan säkringen löser ut, amperemeter i huvudledningen (kretsfigur) |

- Fysikformatet följs: nivå 3 har C och (0/1/0), miniräknare är tillåten, precisionen anges i parentes efter frågan, svarsrutan används och lösningen skrivs i styckeform.
- Rätt alternativ står inte först i flervalskorten.
- Rättelse under granskningen: kretsfiguren var först ritad med en obruten övre ledning. Den hade kortslutit de parallella grenarna. Huvudledningen går nu bara till förgreningspunkterna, som är markerade med prickar. Ledningarna är också uppdelade i separata banor, så att granskaren inte läser in en linje genom amperemetern.

## Kontroll

- Inget nytt kort har samma facit som ett annat kort i området. Sju kort fick nya tal.
- Facit avrundas till 12 värdesiffror när korten byggs, så att flyttalsrester som 2,0999… inte hamnar i banken.
- Validatorn för Fy1 ger inga nya fynd, med 788 fynd före och efter. SVG-granskaren ger 0 fynd för de 7 figurerna.
- Kontrollistorna i `fysik1-kapitel3` (at_diagram) och `fysik1-kapitel4` (tyngdkraft) är utökade med oberoende uträkningar. Antalskontrollen i `fysik1-tyngdkraft-variation-2026-10-21` är höjd till 41 kort, varav 39 med spel.
- Det nya testet `tools/fysik1-omgang-8-niva3-2026-10-25.test.js` ger 2/2 pass. Det kontrollerar bland annat att kretsfiguren inte kortsluter grenarna.
- Självrättningen i Kunskapsgymmet testades i webbläsaren med 46 svar, och alla gav väntat resultat. Testet täckte bland annat:
  - enheter som kN, N, mA och Ω;
  - grundpotenser;
  - att fel tecken och för grov avrundning underkänns.
- Hela testsviten ger samma 11 fel som före omgången.
