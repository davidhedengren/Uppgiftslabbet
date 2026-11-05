# Ma2: GeoGebra-skärmbilder i resten av envariabelfacit (5 november 2026, steg 2)

Fortsättning på [MA2_STATISTIK_GEOGEBRA_STEGBILDER_2026-11-05.md](MA2_STATISTIK_GEOGEBRA_STEGBILDER_2026-11-05.md). Den andra sessionen har gjort:

- 4.328–4.347, 4.450–4.459 och 6.09 med samma arbetsgång;
- normalfördelningsfacit med Sannolikhetskalkylatorn.

## Uppdrag

Användaren vill att statistikuppgifter där standardavvikelsen bestäms löses med GeoGebra, inte för hand med formeln. Facit ska ha skärmdumpar så att eleven ser *hur* man gör i GeoGebra. Användaren bad sedan om skärmbilder i alla statistikuppgifter som saknar dem.

Beslutet från samma dag gäller också: Ma2-eleverna ska inte behöva kunna formeln för standardavvikelse.

## Verktyg

- **`tools/geogebra-cdp-playwright.js`** (ny): ett litet ersättningslager för den del av Playwright som `tools/geogebra-skarmbilder.js` använder. Det är byggt direkt på Chrome DevTools Protocol, eftersom Playwright och det lokala GeoGebra-paketet inte finns på datorn `Hedav`.
- **`tools/geogebra-skarmbilder.js`**:
  - Med `GGB_WEBB=1` körs riktiga GeoGebra Classic från `geogebra.org/classic?lang=sv`.
  - Kakbannern avböjs (”Reject all”), och tipsrutan ”Nybörjare?” döljs i bilderna.
  - Kalkylbladets celler ritas på webben på en canvas, så cellernas läge anges med uppmätta mått.
  - Nytt fält `freq`: värdena skrivs i kolumn A och antalen i kolumn B, och sedan markeras A1–Bn. GeoGebra räknar då kolumn B som frekvenser. Kontrollen av n och Σx tar hänsyn till frekvenserna.
- **`tools/ma2-geogebra-skarmbilder-steg2-2026-11-05.py`** (ny): datamängder och facitsteg per uppgift. `spec` skapar bildspecen och `bygg <logg> --skriv` skriver facit.
  - Arbetsgången och rubrikerna följer steg 1, och rubrikerna nämner uppgiftens data, till exempel ”Analysera skidortens temperaturer med Envariabelanalys”.
  - Typvärdet läses i Stolpdiagram, och variationsbredd och kvartilavstånd som Max − Min respektive \(Q_3-Q_1\).
  - Har en uppgift två material eller före/efter, får det andra materialet ett eget inmatningssteg och en egen panelbild.
  - Svarsraderna behålls, och uppgiftens egna steg står kvar (x, omvandling, tolkning).
  - I delkort döljs panelrader som besvarar senare delar.
  - 4.11, 4.28, 4.41, 4.61 och 5.41 har kvar ett sammanhängande huvudfacit utan delmarkeringar.

## Uppgifter (60)

- **Lägesmått:** 4.11, 4.41, 4.61, 4.303, 4.310, 4.311, 4.317, 4.322–4.326, 4.2015, 4.2016 och 5.41.
- **Standardavvikelse:** 4.05, 4.10, 4.14, 4.28, 4.46, 4.97, 4.157, 4.174, 4.175, 4.212, 4.235, 4.241, 4.283, 4.284, 4.299, 4.302, 4.348–4.351, 4.364–4.366, 4.371, 4.373, 4.384–4.393, 4.454, 4.458, 4.461, 4.463, 5.66, 5.71, 5.94 och 5.110.
- **Lådagram:** 4.360 och 4.361 a.

Delar som inte bygger på data i GeoGebra står kvar oförändrade, till exempel 4.46 c, 4.97 b, 4.157 a, 4.299 c, 4.348 c, 4.351 e, 4.361 b, 4.365 b, 4.366 b och 5.66 c.

Figurdata har lästs ur SVG-koordinaterna och stämmer med tidigare facit:

- 4.212: X = 2, 2, 2, 7, 7, 12, 12, 12 och Y = 2, 6, 7, 7, 7, 7, 8, 12.
- 4.384: A = 9, 10×6, 11; B = 7, 8, 9, 10, 10, 11, 12, 13; C = 4, 5, 8, 10, 10, 12, 15, 16.
- 4.385: 22, 25, 27, 28, 29, 30, 30, 31, 32, 33, 35, 38.

Svar, `rättSvar`, toleranser, frågor, ledtrådar och verktygsflaggor är oförändrade. 4.212, 4.384 och 4.385 behåller `geogebra: false`, eftersom GeoGebra bara används som kontroll där. Facit innehåller ingen formel för standardavvikelsen.

I 4.284 stod tidigare att kandidaten 50 ger 2,96. GeoGebra visar s = 2,8284, och facit säger nu 2,83. Svaret (46,79 och 53,21) är oförändrat.

## Kontroll

- **Värden:**
  - Varje avläst panelvärde (logg från GeoGebra) har jämförts med svarsraden. Alla stämmer.
  - Kvartilerna i 5.41, 5.66, 4.351 och 4.364 ger samma kvartilavstånd som facit.
  - 4.347 b läses inte av i stolpdiagram, eftersom staplarna vid 20–40 bara blir streck när 400 finns med. Den uppgiften gjordes senare i steg 1.
- **Rendering:** facit renderades i 390 px med Uppgiftslabbets CSS. Inga KaTeX-fel, trasiga bilder eller för breda element. Utvalda facit granskades visuellt.
- **Tester:**
  - `tools/ma2-geogebra-skarmbilder-steg2-2026-11-05.test.js` (nytt) passerar, liksom statistik-, lägesmått-, lådagrams- och formeltesterna.
  - Tre tester misslyckas på samma sätt som före ändringen: `ma2-geogebra-sx-jamforelse`, `ma2-kap4-standardavvikelse` (4.343–4.347, 4.102/4.114 och 4.338) och `ma2-statistik-diagram`.
  - `granska-uppgifter.js` ger samma fynd som före ändringen.
- **Bilder:** 286 nya bilder på i genomsnitt cirka 18 kB, komprimerade med `tools/geogebra-skarmbilder-komprimera.py`.
