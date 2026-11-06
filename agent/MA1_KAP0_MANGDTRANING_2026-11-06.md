# Ma1 kapitel 0: mängdträning och felrapport 2026-11-06 08:31

Underlag: `felrapporter/Felrapporter UL 2026-11-06 0831.txt` (0.02, 0.125, 0.62) och användarens önskan:

> Det är viktigt med mängdträning i "kapitel 0" här. inte konstigt formulerade, men vanliga beräkningar som de kan
> träna på. ibland bara en uppgift ibland a) b) osv med varierande antal deluppgifter, och gärna då a) enklast,
> b) lite svårare och c) svårast osv.

## Felrapporterna

| ID | Rapport | Åtgärd |
|---|---|---|
| 0.125 | ”byt strikt mot ’mellan’ med fetstil … Gör detta i hela banken” | Frågan lyder nu ”ligger **mellan** −4 och 3”. Facitrubriken heter ”Mellan betyder att ändpunkterna inte räknas”. Samma byte är gjort i hela Ma1-banken. ”Strikt mellan” blev fetstilt **mellan** i frågor (0.76) och vanligt ”mellan” i facit (0.76, 0.591, 1.449, 0.1134, 0.1135). Övriga ”strikt” i Ma1 är omskrivna med vardagliga ord: 0.112 och 0.118 (ledtrådar), 0.558, 1.118, 1.226, 3.02 och 7.138 (facit), 1.121 (alternativkommentar) samt 2.214 (fråga och ledtråd: ”i första kvadranten och inte på någon av axlarna”). Ma1-banken innehåller inte längre ordet. ”Strikt växande” i Ma3–Ma5 är kvar, eftersom det är kursbegrepp där. |
| 0.62 | Elevexemplet ska vara ”… och skriver −7·(−5)” | Frågan lyder nu ”…från vänster och skriver \(-7\cdot(-5)=35\)”. Alternativen och facit (”Eleven räknade −4 − 3 först”) passar fortfarande. |
| 0.02 | ”Alla behöver inte vara a) b) c). Variera lite … gärna med ökad svårighetsgrad.” | 0.02 har nu fyra delar i stigande svårighet: a) −8+5 (nivå 1), b) 6−14+9 (2), c) −3−7+12 (2), d) −5−(−9)+(−6) (3). Det nya `rättSvar` är [−3, 1, 2, −2] och poängen 4/0/0. Varje del har egen träningsnivå, ledtråd och facit. Kommentaren gäller banken som helhet, och därför följer all ny mängdträning nedan samma princip. |

## Ny mängdträning: 86 uppgifter, 208 kort (#0.1302–0.1387)

Uppgifterna är vanliga beräkningar utan textproblem. Antalet delar varierar: 24 uppgifter har en del, 23 har två, 18 har tre och 21 har fyra. Inom en uppgift ökar svårigheten från a) till d), och varje delkort har en egen `traningsniva`. Nivåfördelningen över korten är 52 på nivå 1, 100 på nivå 2, 51 på nivå 3 och 5 på nivå 4.

| ID | Område (familj) | Innehåll | Kort per nivå |
|---|---|---|---|
| 0.1302–0.1317 | negativa_tal | ± med negativa tal, ·/÷ med teckenregler, potenser \((-6)^2\) och \(-6^2\), blandade räknesätt | 10 / 18 / 11 / 1 |
| 0.1318–0.1329 | tal_rakneordning | prioriteringsregler, parenteser, potenser, ÷ och · från vänster | 5 / 14 / 7 / 1 |
| 0.1330–0.1342 | brakrakning | ± med lika och olika nämnare, negativa bråk, heltal och bråk, · och ÷ | 5 / 16 / 8 / 1 |
| 0.1343–0.1352 | decimaltal_positionssystem | ±, ·, ÷ med decimaltal, ·/÷ 10, 100, 1000 (utan räknare) | 8 / 10 / 5 / 1 |
| 0.1353–0.1362 | enhetsbyten | längd, massa, tid, volym, area | 6 / 13 / 6 / 1 |
| 0.1363–0.1372 | andelar | procent av, andel i procent, procent ↔ decimalform | 7 / 11 / 5 / 0 |
| 0.1373–0.1376 | brakform | förkorta så långt som möjligt | 3 / 5 / 2 |
| 0.1377–0.1380 | avrundning | heltal, decimaler, tiotal–tusental (även 9,95 → 10,0) | 4 / 4 / 2 |
| 0.1381–0.1383 | prefix | k, c, m, µ, M, G | 2 / 3 / 2 |
| 0.1384–0.1387 | tiopotenser_prefix | decimalform ↔ grundpotensform | 2 / 6 / 3 |

### Beslut

- **Miniräknare av** på alla, även procent. Talen är valda så att varje steg går i huvudet. Det som tränas är själva proceduren, till exempel teckenregler, prioritering, gemensam nämnare och decimaltecknets plats, och den proceduren tar en räknare bort (minnesregeln: enstegsuppgifter och sådant fx-991 gör direkt ska lösas utan räknare). Det skiljer sig från talrutinen 2026-11-05, där procentkorten tillät räknare.
- **Svarsformat:**
  - Heltalsräkning: `numeriskt`.
  - Decimaltal, enheter, procent, prefix och avrundning: `decimalform`. Formatet kräver målenheten om eleven skriver en enhet.
  - Bråkräkning: `bråk`. Likvärdiga bråk godtas, som i 2026-11-05.
  - Förkortning: `forkortat_brak`. Ett oförkortat svar underkänns, eftersom förkortningen är det som tränas.
  - Grundpotensform: `grundpotensform`.
  - Procent har `svarEnhet` `%`, så både ”25” och ”25 %” godtas.
- **Facit** följer FACITMALL med en numrerad steglista och ett steg per räkneoperation. Rubriken namnger regeln och visar uppgiftens egna tal, till exempel ”Multiplikation före subtraktion: \(4\cdot(-3)=-12\) (olika tecken ger minus)” och ”I parentesen, potensen först: \(2^3=2\cdot2\cdot2=8\)”. Efter varje steg visas det kvarvarande uttrycket, och sist kommer en svarsrad. Ingen rubrik är en mallfras utan tal; testet kontrollerar det.
- **Ledtrådar** pekar på första tankesteget i just den delen och avslöjar inte svaret. Exempel: ”Börja på \(-6\) på tallinjen och gå 4 steg åt höger”, ”Vilken räkneoperation ska göras först: division eller subtraktion?”, ”Står minustecknet innanför eller utanför potensen?” och ”Vilken är den minsta nämnare som både 6 och 8 går jämnt upp i?”. Huvudkortet visar delarnas ledtrådar efter varandra, märkta a), b) och så vidare.
- **Inga figurer.** Rena räkneuttryck blir inte tydligare av en bild.
- **Validatorn** gav 2 INFO om liknande textmall (0.1328 mot 0.23 och 0.1371 mot 0.1106–0.1108). Likheten är avsiktlig mängdträning, på samma sätt som 2026-11-05.

## Verifiering

- Byggskriptet `tools/bygg-ma1-kap0-mangdtraning-2026-11-06.py` räknar med Fraction och Decimal.
- Regressionstestet `tools/ma1-kap0-mangdtraning-2026-11-06.test.js` räknar om alla 208 svar direkt ur den fråga eleven ser, utan att använda byggaren. Det kontrollerar också:
  - stigande träningsnivå a → d;
  - egen ledtråd och eget facit per del;
  - att varje facitrubrik innehåller uppgiftens tal;
  - rättelserna 0.02, 0.62 och 0.125;
  - att Ma1-banken inte innehåller ”strikt”.
- I Kunskapsgymmet kontrollerar `tools/ma1-kap0-mangdtraning-2026-11-06.test.js` med appens riktiga `expandGameTask` och `delSvarRatt` att:
  - alla 208 kort godtar facit med decimalkomma, decimalpunkt och enhet;
  - fel värde, fel tecken, fel täljare och oförkortat bråk underkänns, liksom decimalform där grundpotensform krävs.
- I headless Chrome kördes appens `kvFacit` på 89 uppgifter och 214 kort: 0 fel.
- Alla frågor, ledtrådar och facit renderades med MathJax i 390 px bredd. Den bredaste formeln är 246 px. Tvåbråksrader och långa prefixrader delades före leverans. Facit för bland annat 0.1315 och 0.1335 har lästs i skärmbild.
- Granskningen av facit, ledtrådar och svarsrad mot `rättSvar` är gjord för alla nya kort. Efter genomläsningen rättades:
  - parentes runt negativt första tal;
  - talordning i 0.1328;
  - specifika rubriker för bråk och decimaltal;
  - avrundningens nollor (4,00);
  - 1 h = 60 min, som först räknades fram som 59,999…;
  - dubbletter av samma svar i förkortningsuppgifterna.
