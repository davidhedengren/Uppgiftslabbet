# Separata geometriska områden i ma2c – 2026-10-12

Användarbeslut: **Kordasatsen och bisektrissatsen** ska vara ett eget område,
och **Randvinklar och medelpunktsvinklar** ett annat. De ska inte ligga i
det gemensamma områdeskortet ”Cirkelgeometri” i ma2c.

## Ändring

`strukturma2.js` använder två separata `GRUPPMA2`-kort för spår 2c. Det gamla
kortet ”Cirkelgeometri” gäller fortsatt 2b. Kunskapsgymmets `getCards()`
respekterar gruppens valfria `kurs`-lista; grupper utan den listan fungerar
som tidigare. Strukturfilerna är identiska i båda repona.

De befintliga OMR-nycklarna behålls:

- `randvinkel_medelpunkt`: 67 huvuduppgifter, 76 tillgängliga träningskort i 2c.
- `kordasatsen_biskarningssatsen`: 51 huvuduppgifter, 54 tillgängliga träningskort i 2c.

Den gamla stavningen i den andra interna nyckeln behålls för kompatibilitet.
De elevsynliga namnen har korrekt stavning. Delmomenten ligger kvar under rätt
område, inklusive Bisektrissatsen. Befintliga genomgångar filtreras redan på
OMR och visas därför på rätt nya kort; genomgångarnas innehåll har inte ändrats.

## Resultat och uppgiftsinnehåll

Alla uppgifts-ID:n, områdesnycklar och familjer behålls. Därför behövs ingen
migrering av elevernas områdesresultat. Separata kort visar nu respektive områdes
träningsvärde i stället för de två områdenas gemensamma medelvärde. Historik,
nivåresultat, familjeresultat och XP påverkas inte av uppdelningen.

Inga bankobjekt, facit, svårighetsnivåer eller figurer har ändrats. Den
[kompletterande JSON-listan](MA2C_GEOMETRI_OMRADEN_2026-10-12.json) anger samtliga
118 berörda huvuduppgifts-ID:n. Detta är en strukturändring, inte en ny matematisk
eller pedagogisk granskning av dessa uppgifter.

## Verifiering

- `tools/ma2c-geometri-omraden.test.js` i Kunskapsgymmet testar två kort i 2c,
  ett samlat kort i 2b och oförändrad funktion för grupper utan spårbegränsning.
- `tools/ma2c-geometri-omraden.browser.py` testar riktiga områdeskort och
  separata uppgiftspooler, rätt genomgångar, öppning av ett träningspass i varje
  område, bevarade resultat/XP samt växling mellan 2c, 2b och 2a. Ma2a får inga
  av dessa områden. Testet använder en fullständig lokal testprofil och skickar
  inga svar eller databasanrop.
- Mobil (390 px) och dator (1280 px) visar båda nya namn korrekt. Titlarnas
  textrutor ryms; kortets större osynliga klickyta ska inte misstas för textspill.
- Kunskapsgymmets Node-tester: 131/131 godkända. Tidigare geometriregressioner i
  master: 5/5 godkända. Inga JavaScript-fel i webbläsarkontrollen.
- `BANK_VERSION` uppdateras så den nya strukturen laddas. Syntax,
  `git diff --check` och identiska strukturfiler kontrolleras före leverans.
