# Fysik 1: medelhastighet och medelfart, 2026-10-21

Mätnoggrannhet hoppas över enligt användarens uttryckliga beslut. Nästa område
är medelhastighet i kapitel 2. Befintliga uppgiftstexter inventerades för att
undvika fler rena talbyten; de 76 befintliga uppgifterna är inte samtliga
manuellt fullgranskade i denna omgång.

## Nya uppgifter – samtliga granskade

| ID | Innehåll | Nivå | Svar |
|---|---|---:|---|
| 2.335 | Avläs positionsändringen när grafen inte börjar i origo | 2 | 2 m/s |
| 2.336 | Medelfart för en promenad inklusive paus | 2 | 1,25 m/s |
| 2.337 | Medelhastighet efter vändning, positiv riktning angiven | 2 | +1 m/s |
| 2.338 | Medelfart från positionsdiagram med paus och återfärd | 2 | 1,6 m/s |
| 2.339 | Använd skillnaden mellan två passertider | 2 | 10 m/s |
| 2.340 | Tidsavstånd mellan paketens framkanter vid en sensor | 2 | 20 s |
| 2.341 | Hela tåget ska passera en bro | 3 | 20 s |
| 2.342 | Drönarens längsta avstånd med mättid och olika farter | 4 | 1 296 m |

Alla åtta har egna SVG-figurer, uppgiftsspecifika ledtrådar, förklarande facit
och självbärande kort. Miniräknare är tillåten; GeoGebra behövs inte för
avläsning av dessa givna diagram. Inga standardkonstanter eller formelledningar
har lagts till i frågorna. Nivå 2 avser flera enkla beroende moment; nivå 3
kräver att tågets egen längd räknas med; nivå 4 kräver en tidsbudget och ekvation.
Områdets enkla nivå 1-uppgifter finns kvar, bland annat 3.102 och 3.259.

2.338 begär uttryckligen en decimal. Skälet är att 1,6 m/s annars får avrundas
till 2 m/s enligt användarens regel om fri avrundning. Just 2 m/s är också
resultatet om pausen utelämnas. Preciseringen gör att uppgiften kan pröva
om eleven faktiskt räknar hela tiden. Övriga nya uppgifter saknar krav på
antal decimaler; inget nytt generellt precisionskrav införs i parsern.

## Befintliga uppgifter som granskats och förbättrats

| ID | Ändring | Föreslagen kommentar |
|---|---|---|
| 3.126 | t: enheten i parentes efter frågan | Enheten står nu samlat efter frågan. Medelfarten är fortfarande 120 km/h. |
| 3.259 | t: enheten i parentes efter frågan | Frågan anger tydligt att farten ska uttryckas i km/h. Svaret är 36 km/h. |
| 3.260 | t och rättSvar: samlad instruktion, fullprecision i maskinfacit | Svaret 13,9 m/s och det oavrundade värdet 50/3,6 godkänns. Instruktionen står efter frågan. |
| 3.262 | t och rättSvar: samlad instruktion, fullprecision i maskinfacit | Svaret 4,3 m/s och det oavrundade värdet 650/150 godkänns. Instruktionen står efter frågan. |

Dessa är förtydliganden och precisionstillämpningar; inget nytt matematiskt
fel har konstaterats i deras tidigare elevfacit. Toleranserna för 3.260 och
3.262 var redan 0,05 och behålls. Nivåer, verktyg och lösningsmetoder behålls
efter kontroll. Före/efter finns i `FYSIK1_MEDELHASTIGHET_2026-10-21_ANDRINGAR.json`.

## Granskad – inget fel

- **3.102:** 660 m på 30 s ger 22 m/s. Direkt samband, nivå 1 och miniräknare
  tillåten. Kommentar: ”Granskad – inget fel: 660/30 = 22 m/s.”

Inga rapportstatusar ändras och inga kommentarer skickas till elever.
Samtliga manuellt granskade ID:n i omgången är de åtta nya och fem befintliga
i tabellerna/listan ovan. Andra äldre bankobjekt är oförändrade.

## Kontroller

- Oberoende numeriska beräkningar av alla nya svar samt tidskontroll för drönaren.
- Bankvalidator före/efter: inga nya fynd.
- SVG-validator och visuell kontroll av alla åtta figurer. Grafetiketter fick
  extra marginal; tåg- och brolängder är proportionerliga. Inga kvarvarande
  ERROR/WARNING. INFO för vit bakgrund vid viewBox-kanten är väntad.
- Faktisk självrättning, enheter, tecken och både riktiga/felaktiga svar prövas
  med `tools/fysik1-medelhastighet-2026-10-21.browser.cjs` i konsumenten, vid
  390 och 1280 px. Ingen XP eller elevdata skrivs.
- `tools/fysik1-medelhastighet-2026-10-21.test.js` skyddar beräkningar,
  diagrammens koordinater och metadata. Föregående densitetstester körs också.
- Masterbanken synkas identiskt till Kunskapsgymmet och BANK_VERSION uppdateras.

Slutresultat: **84 rättningskontroller och 26 kort-/lösningsvisningar**
passerar utan upptäckta renderings- eller layoutfel. Åtta uppgifter tillagda,
fyra befintliga förtydligade, en befintlig granskad utan ändring.
