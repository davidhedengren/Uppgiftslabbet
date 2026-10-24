# Ma1: variation och figurer i geometri och mönster, 2026-10-24

Uppdrag: förbättra uppgifterna i Kunskapsgymmet område för område, med början i Ma1. Varje område ska ha varierade uppgifter, gärna med figurer som gör frågan tydligare. Prioriteringen bygger på en variationsanalys per område: antal kort, kort på nivå 1, andel med figur, andel flerval och hur många kort som delar textmall.

## Nya kort (65)

| Område | ID | Antal | Med figur |
|---|---|---|---|
| volym | 4.700–4.716 | 17 | 15 |
| omkrets_area | 4.717–4.733 | 17 | 14 |
| monster_samband | 1.1500–1.1516 | 17 | 9 |
| skala_likformighet | 7.700–7.713 | 14 | 8 |

- **Figurer:**
  - snedprojicerade rätblock, kuber byggda av enhetskuber, en utvikt kub, cylindrar, koner, klot, prismor och ett hus med sadeltak;
  - plana figurer med mått, rutnät och fyra figurer att jämföra;
  - prick-, tändstickor-, bord-, staket- och pärlbandsmönster;
  - en karta med skalstock, en förstoring med linjal och likformiga figurer.
- **Representationer:** text, figur, tabell och flerval (11 kort), samt svar som tal, färg (kort_text) och skala (`svarFormat: "skala"`).
- **Inga dubblettfacit:** inget nytt kort har samma facit som ett annat kort i sitt område. Vid krock ändrades talen, till exempel 4.711 (takhöjd 1,5 m), 4.716 (säck om 30 l) och 7.701 (myra 4 cm).
- **Nära kopior undveks:** sammanhangen ändrades när ett befintligt kort redan hade samma sammanhang:
  - grushög i stället för glasstrut;
  - vattentank i stället för fotboll;
  - låda utan lock i stället för present;
  - chokladkartong i stället för tält;
  - pallkrage i stället för sandlåda;
  - husgavel i stället för L-rum.

## Figurer till äldre kort (22)

Texten är oförändrad, med ett undantag som anges nedan. En figur har lagts in före frågan i 4.527, 4.528, 4.529, 4.530, 4.537, 4.540, 4.541, 4.544, 4.545, 4.547, 4.548, 4.570, 4.582, 4.583, 4.587, 4.594, 6.416, 1.1103, 1.1106, 7.544, 7.545 och 7.546.

I 7.545 rättades även ”5 m långt och 3 m brett” till ”5 m lång och 3 m bred”. Facit ändrades inte.

## SVG

Ellipsbågar i cylindrar, koner, halvcirklar och löparbanan ritas med kubiska Bézierkurvor i stället för `A`-kommandon. Annars tolkar `granska-svg` dem som vinkelbågar (ANGLE_ARC_*). Efter ändringen återstår bara ett INFO-fynd (EDGE_CLIPPING) bland de 68 figurerna.

## Kontroll

- Validatorn ger inga nya fynd i Ma1, med 201 fynd både före och efter.
- `tools/ma1-geometri-variation-2026-10-24.test.js` ger 4/4 pass.
- Testerna som fallerade redan före ändringen gör det fortfarande och påverkas inte av den här ändringen. Det gäller felrapporter-2026-10-13, felrapporter-2026-10-16, fysik1-kapitel3, ma1-uttryck-med-parenteser, ma1-verktyg-2026-10-15 och svg-bredd-2026-10-21.
- Självrättningen i Kunskapsgymmet testades i webbläsaren med 63 svar, både rätta och felaktiga, bland annat med enhet, avrundade svar, ”1 : 50” och ”Blå”. Alla gav väntat resultat.
- Kunskapsgymmets testsvit ger 258 pass.

## Nästa steg

Gå vidare med Ma1 i omgång B:

- genomsnittlig_forandring: 0 % figurer och många upprepade mallar;
- beroende_handelser: träddiagram;
- brakform;
- kvadratrotter.

Därefter kommer proportionalitet_yrke, potensekvationer, potensfunktioner, index och upprepade_forandringar. Sedan Ma2 och uppåt.
