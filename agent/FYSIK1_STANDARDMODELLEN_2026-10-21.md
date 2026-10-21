# Fysik 1: standardmodellen, 2026-10-21

## Lucka och resultat

Området hade 16 huvuduppgifter och inga figurer. Åtta nya uppgifter ger atom- och kvarkmodeller, antipartiklar, betaomvandlingar och jämförelser av partikelpar. Nu finns **24 uppgifter, varav 8 med figur**. Uppgifterna varierar begrepp och representation, inte bara talvärden.

## Alla nya uppgifter

| ID | Innehåll, korrekt svar och nivå |
|---|---|
| 9.444 | A är elektronen, inte protonen, kärnan eller hela atomen. Nivå 1. |
| 9.445 | Bild B visar neutronens udd. Nivå 1. |
| 9.446 | En d-kvark omvandlas till u vid beta-minus. Nivå 2. |
| 9.447 | Antineutronen är oladdad men består av antikvarkar. Nivå 2. |
| 9.448 | Sju nukleoner à tre kvarkar ger 21; elektroner räknas inte. Nivå 2. |
| 9.449 | Neutronen är oladdad men sammansatt. Nivå 2. |
| 9.450 | Proton i en kärna ger neutron, positron och neutrino. +e bevaras. Nivå 2. |
| 9.451 | C har +e och −e; övriga pars summor är +2e, +e och −e. Nivå 3. |

Två nivå 1, fem nivå 2, en nivå 3. Alla tillåter miniräknare, kräver inte GeoGebra och har självständig fråga, relevant ledtråd, förklarande facit, egen SVG och förklaringar till felalternativen. Antalet i 9.448 är ett exakt diskret antal (`antal_satt`). De sju valfrågornas rätta alternativ ligger på olika platser i bankdata; konsumenten får fortsatt blanda hela alternativobjekt.

## Alla granskade befintliga uppgifter

| ID | Status och färdigt kommentarsförslag |
|---|---|
| GY25-FY1-STD-01 | Granskad – inget fel: Elektronen och kvarken är elementarpartiklar; protonen är sammansatt. |
| GY25-FY1-STD-02 | Åtgärdad: Kvarkladdningarna hämtas nu ur formelsamlingen; uträkningen och slutsatsen +e är bevarade i facit. |
| GY25-FY1-STD-03 | Granskad – inget fel: udd är oladdad men sammansatt. Resonemanget är korrekt. |
| GY25-FY1-STD-04 | Granskad – inget fel: Elektron och neutrino är leptoner, u en kvark och proton en sammansatt partikel. |
| GY25-FY1-STD-05 | Granskad – inget fel: Laddningen bevaras vid beta-minus: 0 = +e − e + 0. Elektronen bildas vid sönderfallet. |
| 9.261 | Åtgärdad: Kvarkladdningar finns i formelsamlingen; protonens laddning +e godkänns oförändrat. |
| 9.262 | Åtgärdad: Kvarkladdningar finns i formelsamlingen; neutronens laddning 0 godkänns oförändrat. |
| 9.263 | Åtgärdad: Tre u-kvarkar ger +2e. Utskriven standardladdning är borttagen ur frågan. |
| 9.264 | Åtgärdad: Antikvarkarnas laddningar ger −e. Standardladdningar och lösningsledning är borttagna ur frågan. |
| 9.265 | Åtgärdad: u och anti-d ger +e. Standardladdningar och lösningsledning är borttagna ur frågan. |
| 9.266 | Granskad – inget fel: Elektronen är en lepton; korrekt alternativ och förklaring. |
| 9.267 | Granskad – inget fel: Protonen är sammansatt och därmed inte en elementarpartikel. |
| 9.268 | Granskad – inget fel: Elektron och positron har samma massa och motsatt laddning. |
| 9.269 | Granskad – inget fel: Upp- och nedkvarkar bygger upp protoner och neutroner. |
| 9.270 | Granskad – inget fel: En baryon innehåller tre kvarkar. |
| 9.329 | Åtgärdad: Båda korten har egna givna baryonladdningar och inga utskrivna kvarkladdningar. Facit förklarar kvarkladdningarna före ekvationen; svar 3 respektive 0. |

Sju äldre frågor har reviderats enligt instruktionen att standardkonstanter ska hittas i formelsamlingen. Laddningarna är kvar i lösningarna. 9.329 har dessutom fått en förklaring av laddningarna före ekvationen; varje delkort har fortfarande egna givna värden. Ingen generell felaktig definition att alla baryoner enbart består av u/d används i den nya frågeinledningen.

De övriga nio befintliga uppgifterna har granskats för innehåll, facit och verktyg. Ingen ändring behövdes för den kontrollen; det är inte en ny fullständig webbläsartestning av alla deras äldre kort. Minst fem jämförelser för standardladdningar och partikelladdning gjordes bland 9.261–9.265 och 9.329 samt GY25-FY1-STD-02. De numeriska svaren är oförändrade.

## Kontrollpunkter och tester

- En neutral partikel är inte nödvändigtvis elementär och inte nödvändigtvis sin egen antipartikel. Neutronen illustrerar båda skillnaderna.
- Varje kvark-/antikvarksladdning och alla fyra partikelparens summor har beräknats separat. Laddning bevaras inklusive den avgivna elektronen/positronen.
- Beta-plus-frågan gäller uttryckligen en proton **i en atomkärna**, inte en fri proton. Bilden är en schematisk reaktion, inte ett påstående om partikelbanor.
- Atommodellerna är uttryckligen förenklade; ledarstrecken i 9.444 pekar på rätt objekt. 9.448 visar tre protoner, fyra neutroner och tre elektroner.
- 114 svarskontroller i riktiga Kunskapsgymmet och 30 kortvyer vid 390/1280 px. Nytt heltalskort, alla sju nya alternativfrågor, fem äldre laddningskort och båda äldre delkorten 9.329 prövade. Även nollsvar och negativa laddningar testade.
- Åtta SVG visuellt kontrollerade. Inga klippta figurtexter, KaTeX-fel, JavaScript-fel eller sidöverflöden.
- `tools/fysik1-standardmodellen-2026-10-21.test.js`, utökat `fysik1-partiklar-medicin.test.js` och test för tunna områden passerar.
- Full bankvalidator före/efter: ERROR 1577, WARNING 227, INFO 1452 oförändrade; inga nya fynd. Äldre fynd utanför området kvarstår.
- Banken synkas identiskt från master till konsumenten efter kontroll av gemensam bas. Cacheversioner uppdateras i båda repona. Inga rapportstatusar eller kommentarer sparas i produktionsdatabasen.
