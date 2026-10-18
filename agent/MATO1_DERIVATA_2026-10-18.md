# Mato1: derivator, delomgång 2 – 2026-10-18

24 huvuduppgifter ändras. 36 befintliga delkort får uppgiftsspecifika förklaringar i både masterfacit och konsumentkort. Hela banken är inte färdiggranskad.

## Ändringar
- **2.08**: Uttalat avrundningskrav, fullprecisionsmål och tolerans för två decimaler.
- **2.44**: Uttalat avrundningskrav, fullprecisionsmål och tolerans för två decimaler.
- **2.48**: Uttalat avrundningskrav, fullprecisionsmål och tolerans för två decimaler.
- **2.52**: Uttalat avrundningskrav, fullprecisionsmål och tolerans för två decimaler.
- **2.509**: Precisionskrav och avrundning samordnade; samband förklarat utan falsk exakt likhet eller facit i ledtråden.
- **2.510**: Precisionskrav och avrundning samordnade; samband förklarat utan falsk exakt likhet eller facit i ledtråden.
- **2.511**: Precisionskrav och avrundning samordnade; samband förklarat utan falsk exakt likhet eller facit i ledtråden.
- **2.512**: Precisionskrav och avrundning samordnade; samband förklarat utan falsk exakt likhet eller facit i ledtråden.
- **2.547**: Sekantfigur saknade korrekt skala och kontakt med kurvan. Ny skalenlig figur, fullständig logaritmlösning och precisionskontrakt.
- **3.1149**: Efterfrågad tolkning/motivering får manuell komplettering; numeriska svar fortsätter självrättas.
- **2.753**: Efterfrågad tolkning/motivering får manuell komplettering; numeriska svar fortsätter självrättas.
- **3.1079**: Exakt dubblett av 2.753 ersatt med omvänd användning av derivatasambandet; enkel E-variant på nivå 2.
- **2.14**: Tre fristående delkort och helfacit får korta uppgiftsspecifika regel- och insättningsförklaringar. Felriktad ledtråd rättas där den fanns. Facitvärden och verktygsval bevarade.
- **2.18**: Tre fristående delkort och helfacit får korta uppgiftsspecifika regel- och insättningsförklaringar. Felriktad ledtråd rättas där den fanns. Facitvärden och verktygsval bevarade.
- **2.22**: Tre fristående delkort och helfacit får korta uppgiftsspecifika regel- och insättningsförklaringar. Felriktad ledtråd rättas där den fanns. Facitvärden och verktygsval bevarade.
- **2.26**: Tre fristående delkort och helfacit får korta uppgiftsspecifika regel- och insättningsförklaringar. Felriktad ledtråd rättas där den fanns. Facitvärden och verktygsval bevarade.
- **2.207**: Tre fristående delkort och helfacit får korta uppgiftsspecifika regel- och insättningsförklaringar. Felriktad ledtråd rättas där den fanns. Facitvärden och verktygsval bevarade.
- **2.210**: Tre fristående delkort och helfacit får korta uppgiftsspecifika regel- och insättningsförklaringar. Felriktad ledtråd rättas där den fanns. Facitvärden och verktygsval bevarade.
- **2.248**: Tre fristående delkort och helfacit får korta uppgiftsspecifika regel- och insättningsförklaringar. Felriktad ledtråd rättas där den fanns. Facitvärden och verktygsval bevarade.
- **2.301**: Tre fristående delkort och helfacit får korta uppgiftsspecifika regel- och insättningsförklaringar. Felriktad ledtråd rättas där den fanns. Facitvärden och verktygsval bevarade.
- **2.302**: Tre fristående delkort och helfacit får korta uppgiftsspecifika regel- och insättningsförklaringar. Felriktad ledtråd rättas där den fanns. Facitvärden och verktygsval bevarade.
- **2.303**: Tre fristående delkort och helfacit får korta uppgiftsspecifika regel- och insättningsförklaringar. Felriktad ledtråd rättas där den fanns. Facitvärden och verktygsval bevarade.
- **2.304**: Tre fristående delkort och helfacit får korta uppgiftsspecifika regel- och insättningsförklaringar. Felriktad ledtråd rättas där den fanns. Facitvärden och verktygsval bevarade.
- **2.202**: Rättar sista kvarvarande potensmodell-ledtråden i Mato1 och ersätter orelaterat råd om ekvationsrötter med deriveringsförklaringar för tre delkort.

## Pedagogiska och tekniska beslut
Miniräknare/GeoGebra är kontrollerade för alla ändrade uppgifter. Numeriska logaritmer behåller miniräknare; algebraisk derivering kräver inte CAS. 2.210, 2.753 och den nya varianten 3.1079 klaras med små tal och behåller miniräknare avstängd. 3.1079 ändras avsiktligt från en exakt dubblett till omvänd användning av m′=−0,2m; träningsnivå 2 bevaras.
2.753 behåller tidigare korrekt svar −2 g/h och enhet från FP54; den efterfrågade tolkningen markeras nu som manuell komplettering. 3.1149 behåller båda korrekta rötterna och kräver motivering.
Tolv liknande derivatauppgifter med tre delar vardera jämförda och lösningarna lästa. Potensregeln kontrollerad termvis, inklusive negativa och halva exponenter. Fyra exponentialekvationer och fyra basomskrivningar jämförda; numeriska mål verifierade med ursprungliga samband.
Inga rapportstatusar i databasen ändrade. Tidigare 66-uppgiftersomgång bevarad.

## Verifiering
416 mastertester och 178 konsumenttester. 88 webbläsarkontroller av korrekta/felaktiga svar och 96 kortvyer på mobil/dator, utan fel. Separata granska-svg CLI-suiten undantagen på grund av tidigare miljötimeout; den nya sekantfiguren granskas i appen och punkterna verifieras matematiskt.
Validatorn ger inga nya ERROR/WARNING; en INFO-grupp om tre liknande exponentialekvationer får uppdaterad text efter precisionskravet.
