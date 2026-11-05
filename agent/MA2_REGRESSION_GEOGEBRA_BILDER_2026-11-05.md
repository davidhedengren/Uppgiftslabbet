# Ma2: regression och korrelation med GeoGebra-skärmbilder (5 november 2026)

Fortsättning på [MA2_STATISTIK_GEOGEBRA_SKARMBILDER_2026-11-05.md](MA2_STATISTIK_GEOGEBRA_SKARMBILDER_2026-11-05.md). Användaren vill ha skärmbilder från GeoGebra i alla statistikuppgifter som saknar dem.

## Verktyg

- **`tools/geogebra-regression-bilder.js`** (ny) kör riktiga GeoGebra Classic på svenska (geogebra.org) via `tools/geogebra-cdp-playwright.js`. Bildstilen är densamma som i övriga statistikfacit.
- Arbetsgången: x i kolumn A och y i kolumn B → markera A1–Bn → stapeldiagramknappen → *Tvåvariabels regressionsanalys* → välj modell i listan *Regressionsmodell* → Σx.
- Bilderna per datamängd:
  - `-data.png`: markeringen och knappen.
  - `-regression.png`: modellen, ekvationen, Σx och vid behov raden r inringade.
  - Den gemensamma bilden `geogebra-tvavariabel-meny.png`.
- Som kontroll beräknar GeoGebra samma linje med kommandot AnpassaLinje (FitLine), oberoende av visningen. Ett jobb som hänger avbryts efter fyra minuter.
- **`tools/ma2-geogebra-regression-2026-11-05.py`** (ny) skriver facit. Rubriker och texter är skrivna för hand per uppgift.

## Uppgifter

| Uppgift | Ändring |
|---|---|
| 4.138 (+ delkort a–c) | Linjär regression med bilder. Delkorten hade bara en formelrad och har nu steglista och svarsrad. c sätter in x = 6. |
| 4.139 (+ a, b) | Linjär regression, y = 3x + 8.8. Delkorten har nu steglista och svarsrad. |
| 4.141 a och b | Regression med alla fem punkter respektive de fyra första. c (resonemanget) och svarsraden står kvar. |
| 4.146 a | Regression med bilder. b och c står kvar. Den allmänna GeoGebra-beskrivningen sist är borttagen, eftersom a nu visar stegen. |
| 2.773, 4.400, 4.2098 | Linjär regression med bilder, avrundning och tolkning av lutningen. |
| 4.383 a (+ delkort a) | r med Σx: 0.9996, alltså 1,00. b och c står kvar. |
| 4.2107, 4.2129 | r med Σx (0.8602 och 0.9471) och tolkning. |
| 2.372 | Kvoterna mellan y-värdena följs av två bilder: Polynom av grad 2 (y = 1.9071x² − 2.8129x + 7.32) och Exponentiell C•a^x (y = 3.8058 · 1.6133^x). Förändringsfaktorn 1,6133 stämmer med kvoterna. |

Svar, `rättSvar` och toleranser är oförändrade. 2.371 saknar data och är kvar som resonemang. 4.381 kräver att ett okänt värde varieras och har inte fått bilder i den här omgången.

Varje regressionssteg har också ett förstorat utsnitt (-ekvation.png eller -r.png) som går att läsa på mobil. I delkorten 4.138 a och b syns hela ekvationen i bilden. Det beror på att k och m läses av i samma fönster.

## Kontroll

- **Ekvationer och r:**
  - De har lästs av i varje bild och jämförts med AnpassaLinje, med en egen minsta kvadrat-beräkning och med `rättSvar`.
  - En tidig körning visade y = 3x + 8.7 för 4.139. Det var en tillfällig visning, eftersom både AnpassaLinje och en ny körning ger 3x + 8.8. Bilden är tagen om.
- **Test:** `tools/ma2-geogebra-regression-2026-11-05.test.js`.
