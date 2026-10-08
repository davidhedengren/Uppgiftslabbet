# Fysik 1: formuleringar och nivåkalibrering, 2026-10-08

Banken innehåller 3681 originaluppgifter och 5847 kort efter delning. Den här omgången ändrar **360 originaluppgifter**, **325 visade frågetexter**, **68 kortfacit** och **275 kortnivåer**. ID:n, E/C/A, poäng och befintliga SVG-figurer har bevarats. Endast svaren till 5.386 ändras.

## Granskningens omfattning

Alla 720 ursprungliga nivå 1-kort har lästs. I de prioriterade momenten har samtliga 787 ursprungliga nivå 1–2-kort lästs, inklusive närliggande gas- och lyftkraftsuppgifter. Överlappningen ger **1275 olika kort**. Dessutom har 115 kort lästs efter en sökning genom hela banken efter hänvisningar till andra delar, krångliga ord och långa texter på nivå 1–2. Ytterligare 61 kortare prioriterade kort på nivå 3–4 har lästs med fokus på nivå och saknade värden. Totalt är **1451 olika kort** dokumenterade som lästa. Utvalda högre kort har också kontrollerats när ett språk- eller fysikproblem framkommit. Detta är ingen fullständig semantisk granskning av samtliga nivå 2–5-kort i hela Fysik 1. De högre nivåerna utanför urvalet återstår.

Kalibreringen bygger på vad eleven faktiskt måste göra på det visade kortet och reglerna i PEDAGOGISKA_REGLER.md. Provfilerna har inte ingått i analysen.

## Nivåprinciper

- Nivå 1: grundbegrepp, avläsning eller ett direkt samband med enkla tal. En enkel energi- eller lyftkraftsformel kan också höra hit.
- Nivå 2: något mer krävande rutinuppgifter, exempelvis enhetsomvandling tillsammans med beräkning, procent, proportion eller flera beroende steg. De kan fortfarande vara E.
- Nivå 3: kombination av rörelsemängd och energi eller stötar där flera kroppar och riktningar behöver samordnas.

| Ändring | Kort |
|---|---:|
| 1 → 2 | 206 |
| 1 → 3 | 2 |
| 2 → 1 | 40 |
| 2 → 3 | 10 |
| 3 → 1 | 1 |
| 3 → 2 | 16 |

Nivåer har både höjts och sänkts. Direkta frågor om kraft, area, effekt, rörelsemängd och tid har flyttats till nivå 1 där de tidigare låg för högt. Nivån för hela originaluppgiften och den för ett förenklat delkort kan skilja sig åt.

## Bekräftade innehållsproblem

- **5.386:** Golvets impuls var förväxlad med ändringen i bollens rörelsemängd. Tyngdkraften verkar samtidigt under golvkontakten. Rätt golvimpuls är 8,99568 Ns och rätt medelkraft 449,784 N. Kort b anger 9,0 Ns och ger cirka 450 N, inom svarstoleransen. Huvudfacit, båda kortfaciten och självrättningssvaren har rättats.
- **8.465 b:** Batteriets 90 Ah saknades på delkortet. Kapaciteten och tiden 24 h står nu på samma kort. Facit förklarar varför Ah delat med timmar ger A.
- **5.515 d:** Handens massa och fart saknades när kortet visades separat. Massan 7,0 kg och farten 10,0 m/s står nu tillsammans med bromssträckan 2,00 cm.
- **5.514 b, 6.483 b, 5.600 d:** Bilens massa, isens massa respektive solpanelernas årsproduktion saknades på separata kort. Dessa uppgifter anges nu direkt på respektive kort. Solpanelernas kostnadsmodell anger också oförändrad årsproduktion och elpris.
- **6.486:** Pråmens lodräta sidor, konstanta tvärsnitt och oförändrade massa anges; utan formvillkoret kan det nya djupgåendet inte bestämmas från det gamla.
- **5.412, 5.423, 5.427:** Farten efter ett kast eller skott mäts nu uttryckligen i förhållande till marken, vattnet eller rymdskeppet. De förtydligade referenserna motsvarar den fysik som tidigare facit räknade på.
- **4.681, 4.678, 4.687, 4.689:** Konstant kraft eller acceleration anges där tiden räknas fram. Bollens glidmodell anger också att rotation bortses från.
- **4.700:** Det generella påståendet att människor tål 30g har tagits bort; 30g är nu en given bromsacceleration i modellen.
- **5.397, 5.399, 5.400, 3.368:** Vila vid fallstart och konstant acceleration under de beräkningar som kräver det anges uttryckligen. Delkort visar bara relevanta givna värden.
- **6.436, 6.437, 6.438, 6.444, 6.464:** Tryckökning, tryckminskning och absoluttryck skiljs åt. Kvicksilverytornas nivåer beskrivs tydligt så att tecknet i tryckberäkningen kan avgöras.

## Språk och facit

Överflödiga materialdata och senare deluppgifters siffror har tagits bort från berörda kort. Återkommande generella impulsrubriker har tagits bort från frågetexten. Exempelvis ”isotermt”, ”friläggningsdiagram” och ”smältentalpi” har ersatts med enklare uttryck i de kontrollerade uppgifterna. Nödvändiga fysikbegrepp, riktningar, nollnivåer och villkor har behållits.

68 kortfacit har förbättrats med metodförklaring, relevanta enhetsomvandlingar och tydligt slutsvar. Förändrade delkortsfacit har förts in även i huvudfacit när originaluppgiftens delstruktur tillåter det.

## Verifiering

- 284 numeriska kontroller för 251 olika kort, jämförda med lagrade svar och toleranser. Kontrollerna är redovisade i JSON-filen.
- 58 mastertester och 54 konsumenttester godkända. Fyra nya regressionsfall täcker golvimpulsen, saknade givna data, hastighetsreferenser och separata friktions-, is- och solpanelskort.
- Chromium: 3493 formler i de 360 ändrade uppgifterna renderas utan fel i båda apparna.
- Kunskapsgymmets faktiska självrättning godkänner facitsvar med och utan enhet för samtliga 2503 nuvarande nivå 1–2-kort och de 783 korten från berörda originaluppgifter. Även alla 284 beräknade kontrollsvar godkänns.
- Ytterligare 47 SVG-tester godkända. SVG-validatorn visar 0 ERROR i Fysik 1, samt 344 WARNING och 332 INFO för befintliga figurer. De oförändrade bankerna Fysik 2 och Ma5 har tillsammans 74 ERROR i den fullständiga figurrapporten; dessa ligger utanför denna Fysik 1-omgång.
- Mobil- och datorvisning kontrollerad för 5.386, 8.465 och 6.430.
- Bankvalidatorn har 0 ERROR, 8 WARNING och 655 INFO både före och efter ändringen. Inga nya fel eller varningar har tillkommit.
- JavaScript-syntax, antal uppgifter, ID:n, oförändrade E/C/A-poäng, figurer, strukturerad objektdiff och byte-identisk banksynk kontrollerade.

## Ändrade originaluppgifter

Fullständiga kortnivåer, numeriska kontroller och lästa kort finns i [FYSIK1_KALIBRERING_2026-10-08.json](FYSIK1_KALIBRERING_2026-10-08.json). Fälten nedan gäller originalobjektet; ändringar på ett delkort ligger i `spelDelar`.

| ID | Moment | Ändrade fält |
|---|---|---|
| 2.239 | matnogg | traningsniva |
| 2.240 | matnogg | traningsniva |
| 2.29 | enheter | spelDelar |
| 2.257 | matnogg | traningsniva |
| 2.58 | enheter | traningsniva, spelDelar |
| 2.107 | densitet | traningsniva |
| 2.108 | densitet | traningsniva |
| 2.111 | densitet | traningsniva |
| 2.113 | densitet | traningsniva |
| 2.115 | densitet | traningsniva |
| 2.118 | densitet | traningsniva |
| 3.28 | konstacc | t, traningsniva, spelIntro, spelDelar |
| 3.165 | konstacc | traningsniva, spelDelar |
| 4.323 | fjadrar | traningsniva |
| 4.45 | lutande_plan | spelDelar |
| 4.51 | moment | spelDelar |
| 4.61 | moment | spelDelar |
| 4.85 | newton2 | spelDelar |
| 4.400 | newton1 | t |
| 4.401 | newton1 | t |
| 4.402 | newton2 | t |
| 4.403 | arkimedes | t |
| 4.404 | newton1 | t |
| 4.406 | normalkraft | t |
| 4.408 | newton1 | t |
| 4.410 | newton2 | t |
| 4.411 | newton2 | t |
| 4.151 | blandat_kraft | spelDelar |
| 4.434 | blandat_kraft | traningsniva |
| 4.333 | arbete | traningsniva |
| 4.187 | tyngdkraft | spelDelar |
| 4.190 | tyngdkraft | spelDelar |
| 4.412 | normalkraft | t |
| 4.414 | newton1 | t |
| 4.208 | tyngdkraft | spelDelar |
| 4.241 | newton1 | spelDelar |
| 4.517 | friktion | spelDelar |
| 4.519 | friktion | spelDelar |
| 4.520 | friktion | t, traningsniva |
| 4.521 | friktion | t, traningsniva |
| 4.526 | friktion | spelDelar, traningsniva |
| 4.527 | friktion | t, s, spelIntro, spelDelar |
| 4.530 | friktion | spelDelar |
| 4.545 | friktion | spelDelar |
| 4.547 | friktion | spelDelar |
| 4.576 | friktion | spelDelar |
| 4.577 | friktion | spelDelar, traningsniva |
| 4.298 | newton2 | spelDelar |
| 4.559 | newton2 | spelDelar |
| 4.562 | newton2 | spelDelar |
| 4.565 | newton2 | spelDelar |
| 4.572 | newton2 | spelDelar |
| 4.678 | newton2 | t, spelIntro, spelDelar |
| 4.679 | newton2 | spelDelar |
| 4.681 | newton2 | t, spelIntro, spelDelar |
| 4.685 | newton2 | t, spelIntro, spelDelar |
| 4.687 | newton2 | t, spelIntro, spelDelar |
| 4.688 | newton2 | t |
| 4.689 | newton2 | t, spelIntro, spelDelar |
| 4.690 | newton2 | t |
| 4.692 | newton2 | t |
| 4.700 | newton2 | t, spelIntro, spelDelar |
| 4.714 | newton2 | spelDelar |
| 4.715 | newton2 | spelDelar |
| 4.716 | newton2 | spelDelar |
| 4.717 | newton2 | spelDelar |
| 4.720 | newton2 | spelDelar |
| 5.4 | arbete | spelDelar |
| 5.11 | arbete | spelDelar |
| 5.14 | kollisioner | spelDelar |
| 5.16 | rorelsemangd | spelDelar |
| 5.279 | rorelsemangd | traningsniva |
| 5.312 | rorelsemangd | traningsniva |
| 5.20 | arbete | spelDelar |
| 5.21 | effekt | spelDelar |
| 5.32 | rorelsemangd | spelDelar |
| 5.280 | rorelsemangd | traningsniva |
| 5.313 | rorelsemangd | traningsniva |
| 5.42 | effekt | spelDelar |
| 5.45 | arbete | spelDelar |
| 5.46 | arbete | spelDelar |
| 5.52 | rorelseenergi | spelDelar |
| 5.57 | arbete | spelDelar |
| 5.65 | arbete | spelDelar |
| 5.67 | arbete | spelDelar |
| 5.71 | arbete | spelDelar |
| 5.72 | arbete | spelDelar |
| 5.262 | effekt | traningsniva |
| 5.77 | effekt | spelDelar |
| 5.82 | rorelsemangd | spelDelar |
| 5.95 | blandat_energi | spelDelar |
| 5.108 | blandat_energi | spelDelar |
| 5.115 | blandat_energi | spelDelar |
| 5.117 | blandat_energi | spelDelar |
| 5.125 | blandat_energi | spelDelar |
| 5.131 | blandat_energi | spelDelar |
| 5.140 | effekt | spelDelar |
| 5.147 | effekt | spelDelar |
| 5.149 | effekt | spelDelar |
| 5.157 | rorelsemangd | spelDelar |
| 5.161 | rorelsemangd | spelDelar |
| 5.162 | rorelsemangd | spelDelar |
| 5.170 | blandat_energi | spelDelar |
| 6.2 | tryck | spelDelar |
| 6.6 | arkimedes | spelDelar |
| 6.8 | vatsketryck | spelDelar |
| 6.304 | vatsketryck | t |
| 6.15 | arkimedes | spelDelar |
| 6.16 | arkimedes | spelDelar |
| 6.17 | arkimedes | t, spelDelar |
| 6.32 | vatsketryck | spelDelar |
| 6.42 | tryck | spelDelar |
| 6.46 | arkimedes | spelDelar |
| 6.51 | tryck | spelDelar |
| 6.55 | tryck | spelDelar |
| 6.69 | vatsketryck | t |
| 6.70 | vatsketryck | spelDelar |
| 6.71 | arkimedes | spelDelar |
| 6.72 | arkimedes | spelDelar |
| 6.74 | arkimedes | spelDelar |
| 6.76 | arkimedes | spelDelar |
| 6.82 | gaslagen | traningsniva |
| 6.83 | gaslagen | spelDelar |
| 6.299 | tryck | traningsniva |
| 6.298 | tryck | traningsniva |
| 6.244 | tryck | traningsniva |
| 6.101 | vatsketryck | spelDelar |
| 6.104 | vatsketryck | spelDelar |
| 6.105 | vatsketryck | t |
| 6.107 | vatsketryck | spelDelar |
| 6.112 | arkimedes | t |
| 6.113 | arkimedes | spelDelar |
| 6.114 | arkimedes | spelDelar |
| 6.117 | arkimedes | spelDelar |
| 6.126 | gaslagen | spelDelar |
| 6.133 | vatsketryck | spelDelar |
| 7.64 | varme | traningsniva |
| 7.65 | varme | traningsniva |
| 7.85 | fasandring | t |
| 7.87 | fasandring | t |
| 7.88 | fasandring | t |
| 7.66 | varme | traningsniva |
| 7.67 | varme | traningsniva |
| 7.89 | fasandring | t |
| 7.94 | fasandring | t |
| 7.95 | fasandring | t |
| 7.97 | fasandring | t |
| 7.98 | fasandring | t |
| 7.51 | fasandring | t, traningsniva |
| 7.54 | fasandring | t |
| 8.207 | kopplingar | t, traningsniva |
| 8.257 | potential | traningsniva |
| 8.321 | falt | traningsniva |
| 8.322 | falt | traningsniva |
| 8.216 | kopplingar | t, traningsniva |
| 8.245 | parallellkoppling | traningsniva |
| 8.26 | strom | t, traningsniva |
| 8.247 | parallellkoppling | traningsniva |
| 8.109 | kopplingar | traningsniva |
| 6.141 | gaslagen | t, traningsniva |
| 6.144 | gaslagen | t |
| 4.309 | moment | traningsniva |
| 6.336 | gaslagen | traningsniva |
| 8.413 | kretsar | traningsniva |
| 8.416 | kretsar | spelDelar |
| 8.439 | kretsar | traningsniva |
| 8.473 | kretsar | spelDelar |
| 9.100 | karnreaktioner | traningsniva |
| 4.671 | newton1 | spelDelar |
| 4.672 | newton1 | spelDelar |
| 5.368 | rorelsemangd | t, spelIntro, spelDelar |
| 5.369 | rorelsemangd | t, traningsniva |
| 5.370 | rorelsemangd | t, s, spelIntro, spelDelar |
| 5.371 | rorelsemangd | t, spelIntro, spelDelar |
| 5.372 | rorelsemangd | t |
| 5.373 | rorelsemangd | t, spelIntro, spelDelar |
| 5.374 | rorelsemangd | t |
| 5.375 | rorelsemangd | t, s, traningsniva |
| 5.376 | rorelsemangd | t, s, traningsniva |
| 5.377 | rorelsemangd | t, traningsniva |
| 5.378 | rorelsemangd | t, traningsniva |
| 5.379 | rorelsemangd | t |
| 5.380 | rorelsemangd | t, spelIntro, spelDelar |
| 5.381 | rorelsemangd | t, spelIntro, spelDelar |
| 5.382 | rorelsemangd | t, spelIntro, spelDelar |
| 5.383 | rorelsemangd | t |
| 5.384 | rorelsemangd | t, s, spelIntro, spelDelar |
| 5.385 | rorelsemangd | t |
| 5.386 | rorelsemangd | t, s, rättSvar, spelIntro, spelDelar |
| 5.387 | rorelsemangd | t, spelIntro, spelDelar |
| 5.388 | rorelsemangd | t, spelIntro, spelDelar |
| 5.389 | rorelsemangd | t, s, traningsniva |
| 5.390 | rorelsemangd | t |
| 5.391 | rorelsemangd | t, s, traningsniva |
| 5.392 | rorelsemangd | t, spelIntro, spelDelar |
| 5.393 | rorelsemangd | t |
| 5.394 | rorelsemangd | t, ledtrad |
| 5.395 | rorelsemangd | t, spelIntro, spelDelar |
| 5.397 | rorelsemangd | t, s, spelIntro, spelDelar |
| 5.398 | rorelsemangd | t, spelIntro, spelDelar |
| 5.399 | rorelsemangd | t, s, spelIntro, spelDelar |
| 5.400 | rorelsemangd | t, s, spelIntro, spelDelar |
| 7.137 | varme | spelDelar, traningsniva |
| 7.139 | varme | spelDelar |
| 7.140 | varme | spelDelar |
| 7.144 | varme | spelDelar |
| 7.150 | varme | spelDelar |
| 7.132 | fasandring | t |
| 7.134 | fasandring | t |
| 7.190 | fasandring | spelDelar, traningsniva |
| 7.193 | fasandring | traningsniva |
| 8.402 | kopplingar | spelDelar |
| 8.445 | kopplingar | spelDelar |
| 8.446 | kopplingar | spelDelar |
| 5.189 | arbete | spelDelar |
| 5.209 | rorelseenergi | spelDelar |
| 6.345 | gaslagen | t |
| 6.291 | tryck | t |
| 6.202 | gaslagen | spelDelar |
| 2.291 | medelhastighet | spelDelar |
| 2.295 | medelhastighet | spelDelar |
| 2.305 | medelhastighet | spelDelar |
| 3.271 | acceleration | traningsniva |
| 3.375 | konstacc | spelDelar |
| 3.380 | konstacc | spelDelar |
| 3.381 | konstacc | spelDelar |
| 3.392 | konstacc | spelDelar |
| 3.393 | konstacc | spelDelar, traningsniva |
| 3.394 | konstacc | spelDelar |
| 3.398 | konstacc | spelDelar |
| 3.279 | acceleration | traningsniva |
| 3.368 | acceleration | spelDelar |
| 5.228 | rorelseenergi | spelDelar |
| 5.233 | arbete | traningsniva |
| 2.282 | densitet | traningsniva |
| 2.283 | densitet | traningsniva |
| 5.551 | effekt | s, spelDelar |
| 5.556 | effekt | s, spelDelar |
| 5.560 | effekt | t |
| 5.562 | effekt | spelDelar |
| 5.563 | effekt | spelDelar |
| 5.573 | effekt | spelDelar |
| 5.588 | effekt | s, spelDelar |
| 5.600 | effekt | t, s, spelDelar |
| 5.346 | arbete | traningsniva |
| 5.347 | arbete | traningsniva |
| 5.476 | rorelseenergi | s, spelDelar |
| 5.477 | rorelseenergi | spelDelar |
| 5.480 | rorelseenergi | spelDelar |
| 5.481 | rorelseenergi | spelDelar |
| 5.503 | rorelseenergi | spelDelar |
| 5.505 | rorelseenergi | s, spelDelar |
| 5.509 | rorelseenergi | spelDelar |
| 5.510 | rorelseenergi | t, spelIntro, spelDelar |
| 5.511 | rorelseenergi | s, spelDelar |
| 5.514 | rorelseenergi | s, spelDelar |
| 5.515 | rorelseenergi | s, spelDelar |
| 5.546 | rorelseenergi | spelDelar |
| 9.394 | nuklider | spelDelar |
| 9.395 | nuklider | spelDelar |
| 9.407 | fission | spelDelar |
| 9.410 | fission | spelDelar |
| 9.411 | fission | spelDelar |
| 9.345 | aktivitet | s, spelDelar |
| 9.365 | straldoser | s, spelDelar |
| 9.373 | straldoser | spelDelar |
| 9.374 | straldoser | spelDelar |
| 9.380 | straldoser | s, spelDelar |
| 9.385 | straldoser | spelDelar |
| 6.315 | arkimedes | t |
| 6.319 | arkimedes | t |
| 6.317 | arkimedes | traningsniva |
| 6.318 | arkimedes | traningsniva |
| 6.323 | arkimedes | traningsniva |
| 6.329 | arkimedes | traningsniva |
| 6.332 | gaslagen | traningsniva |
| 6.333 | gaslagen | traningsniva |
| 6.335 | gaslagen | traningsniva |
| 6.337 | gaslagen | traningsniva |
| 6.338 | gaslagen | traningsniva |
| 6.342 | gaslagen | t |
| 6.344 | gaslagen | t |
| 6.352 | tryck | traningsniva |
| 6.419 | tryck | s, spelDelar |
| 6.421 | tryck | spelDelar |
| 6.422 | tryck | spelDelar, traningsniva |
| 6.423 | tryck | spelDelar |
| 6.430 | tryck | s, spelDelar |
| 6.431 | tryck | t, traningsniva |
| 6.436 | vatsketryck | spelDelar |
| 6.437 | vatsketryck | s, spelDelar |
| 6.438 | vatsketryck | t, s, ledtrad |
| 6.439 | vatsketryck | spelDelar |
| 6.442 | vatsketryck | s, spelDelar |
| 6.444 | vatsketryck | s, spelDelar |
| 6.454 | vatsketryck | s, spelDelar |
| 6.457 | vatsketryck | s, spelDelar |
| 6.463 | vatsketryck | s, spelDelar |
| 6.464 | vatsketryck | spelDelar |
| 6.358 | arkimedes | traningsniva |
| 6.361 | arkimedes | t |
| 6.466 | arkimedes | s, spelDelar |
| 6.469 | arkimedes | t, spelIntro, spelDelar |
| 6.470 | arkimedes | s, spelDelar |
| 6.471 | arkimedes | t |
| 6.474 | arkimedes | t, spelIntro, spelDelar |
| 6.482 | arkimedes | s, spelDelar |
| 6.483 | arkimedes | s, spelDelar |
| 6.486 | arkimedes | t, s, ledtrad, traningsniva |
| 6.487 | arkimedes | s, spelDelar |
| 6.490 | arkimedes | spelDelar |
| 6.505 | arkimedes | spelDelar |
| 6.508 | arkimedes | s, spelDelar |
| 6.544 | gaslagen | s, spelDelar |
| 4.647 | normalkraft | spelDelar |
| 4.579 | lutande_plan | spelDelar |
| 4.584 | lutande_plan | spelDelar |
| 4.585 | lutande_plan | spelDelar |
| 4.587 | lutande_plan | traningsniva |
| 4.590 | lutande_plan | spelDelar |
| 4.623 | lutande_plan | spelDelar |
| 4.624 | lutande_plan | spelDelar, traningsniva |
| 4.625 | lutande_plan | spelDelar |
| 8.378 | strom | traningsniva |
| 8.464 | strom | spelDelar |
| 8.465 | strom | s, spelDelar |
| 8.466 | strom | t, traningsniva |
| 9.415 | fusion | spelDelar |
| 9.420 | fusion | spelDelar |
| 9.298 | medicinska_metoder | t, traningsniva |
| 9.304 | em_stralning | traningsniva |
| 5.497 | arbete | spelDelar, traningsniva |
| 5.499 | arbete | spelDelar |
| 5.520 | arbete | spelDelar |
| 5.523 | arbete | s, spelDelar |
| 5.525 | arbete | s, spelDelar, traningsniva |
| 5.528 | arbete | s, spelDelar |
| 5.530 | arbete | spelDelar |
| 5.532 | arbete | spelDelar |
| 5.533 | arbete | spelDelar |
| 5.535 | arbete | spelDelar |
| 5.401 | kollisioner | s, traningsniva |
| 5.402 | kollisioner | traningsniva |
| 5.403 | kollisioner | traningsniva |
| 5.405 | kollisioner | s, spelDelar, traningsniva |
| 5.406 | kollisioner | traningsniva |
| 5.411 | kollisioner | s, traningsniva |
| 5.412 | kollisioner | t, s, spelIntro, spelDelar, traningsniva |
| 5.423 | kollisioner | t, s, spelIntro, spelDelar |
| 5.426 | kollisioner | spelDelar, traningsniva |
| 5.427 | kollisioner | t, s, ledtrad, traningsniva |
| 5.434 | kollisioner | spelDelar |
| 5.435 | kollisioner | s, traningsniva |
| 5.438 | kollisioner | spelDelar |
| 5.440 | kollisioner | s, spelDelar |
| 5.447 | kollisioner | spelDelar |
| 5.461 | kollisioner | t, s, spelIntro, spelDelar, traningsniva |
| 5.462 | kollisioner | t, ledtrad |
| 5.463 | kollisioner | t |
| 5.470 | kollisioner | spelDelar |
