# Ma1: nivå 3, omgång B, 2026-10-25

Den här omgången fortsätter påfyllningen i de områden som har få kort på nivå 3. Räkningen gäller spelbara kort med exakt `traningsniva` 3.

| Område | Kort på nivå 3 före |
|---|---|
| prefix | 3 |
| linjära olikheter | 3 |
| linjära ekvationer | 3 |
| vektorer | 3 |
| mätning | 3 |
| överslag | 3 |
| kostnadsberäkningar | 3 |
| yrkesformler | 3 |

## Nya kort (35 st, alla på nivå 3 med C-poäng och arbetsinsats 2)

| Område | ID | Innehåll |
|---|---|---|
| prefix (5) | 0.1261–0.1265 | Foton på en hårddisk (TB/MB). Virus i rad på 1 mm (nm). Transistorer på en chipyta, där prefixet kvadreras. Vindkraftverkets årsproduktion (MWh→GWh). Nedladdningstid (GB och Mbit/s). |
| linjära olikheter (5) | 1.1557–1.1561 | När ett rörligt abonnemang är billigast. Olikhet med parentes och teckenbyte (intervallsvar). Felsökning av Oskars division med −2 (flerval). När ett årskort lönar sig. Dubbel olikhet (intervallsvar). |
| linjära ekvationer (5) | 1.1562–1.1566 | Två parenteser med minustecken. Åldersproblem. Ekvation med decimaler. Vilken ekvation som saknar lösning (flerval). Blandning av två kaffesorter. |
| vektorer (4, 1c) | 4.820–4.823 | Slutpunkt ur startpunkt och vektor. Vilka vektorer som är lika (rutnätsfigur, flerval). Tre punkter på en linje (k i AC = k·AB). Avstånd efter två förflyttningar. |
| mätning (4, 1a) | 7.781–7.784 | Fylla en pool. En stålbalks massa. Dropp som pågår (flöde och rest). Medelfart i m/s och km/h. |
| överslag (4, 1a) | 7.785–7.788 | Största möjliga area med avrundade mått. Rimligt överslag för en beställning (flerval). Färgburkar till ett rum. Hjärtslag under ett år. |
| kostnadsberäkningar (4, 1a) | 7.789–7.792 | Moms efter rabatt. Offert för ett snickeriarbete. Inköpspris baklänges ur påslag och moms. När en kaffemaskin har betalat sig. |
| yrkesformler (4, 1a) | 7.793–7.796 | Ström från två apparater (P = UI). Spädning av en lösning. Takets lutning i procent. Dosering per kilo och minut. |

Kurstaggarna följer områdena:

- Vektorer har bara 1c.
- Kap 7 har bara 1a.
- Övriga områden har 1a, 1b och 1c.

Ekvationskorten 1.1562 och 1.1564 har ”(Svara exakt.)”. Utan den texten godkände avrundningsregeln 6 för 5,5 och 4 för 3,5. Olikhetskorten med intervallsvar har ingen miniräknare. Det har inte heller grafkortet, flervalskorten om ekvationer och överslag eller de exakta ekvationerna.

## Kontroll

- Facit räknades separat i byggskriptet och räknas om igen i `tools/ma1-niva3-omgang-b-2026-10-25.test.js`, som passerar 2 av 2.
- Inget nytt kort har samma facit som ett annat kort i området. Fyra tal byttes före infogningen.
- Validatorn för Ma1 ger 201 fynd både före och efter ändringen.
- SVG-granskaren ger 0 fynd för vektorfiguren.
- Självrättningen i Kunskapsgymmet testades i webbläsaren med 74 svar och sedan 6 svar efter ändringen till exakt svar. Alla gav väntat resultat.
  - Ett avvikande fall är att 0,25 godkänns för lutningen 25 %. Det är samma tal, och svarsenheten är %.
