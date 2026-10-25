# Ma2 kap 3 geometri, omgång S4: yttervinkelsatsen, begrepp och likformighetsbevis, 2026-10-25

Fortsättning på serien S (se `MA2_GEOMETRI_S2_2026-10-25.md`). Inventeringen efter S3 visade att `yttervinkelsatsen`, `geometriska_begrepp_definitioner` och `bevis_likformighet` hade 29–31 kort på nivå 1–2. Det gällde särskilt nivå 2, med 5–8 kort per område. Nästa lediga ID:n i serien S är **3.2096** och **4.2112**.

## Nya kort (43, 3.2053–3.2095)

| Område | Antal | Nivå 1/2/3 | Figurer | Innehåll |
|---|---:|---|---:|---|
| `yttervinkelsatsen` | 15 | 4/9/2 | 11 | Skylt, motstående vinkel, yttervinkel och intilliggande vinkel, likbent triangel, ekvation, deltriangel, förhållandet 2 : 3, resonemang om storlek, toppvinkel ur yttervinkel, ett steg i beviset (likbelägna vinklar), sväng i en vägkorsning, summan av yttervinklarna, tredje yttervinkeln, satsen två gånger |
| `geometriska_begrepp_definitioner` | 14 | 5/7/2 | 6 | Vinkel vid parallella linjer, parallelltrapets, höjd, regelbunden sexhörning, klassificera triangel, femhörningens vinkelsumma, likbelägna vinklar och vertikalvinklar med algebra, komplementvinkel, samband mellan fyrhörningar (flera rätt), knäck mellan parallella linjer, bisektriser till sidovinklar, antal hörn, vinkeln BIC |
| `bevis_likformighet` | 14 | 3/8/3 | 9 | SVS-fallet, höjden mot hypotenusan, katet ur hypotenusans delar, gemensam vinkel (vilka hörn som motsvarar varandra), längd ur gemensam vinkel, hålkamera, brist i ett bevis, diagonaler i parallelltrapets, areaskala, korsande stag, vilka villkor som räcker (flera rätt), vinklar vid förstoring, motsvarande sida, vinkel vid höjden |

- **Nivåer:** 12 kort på nivå 1, 24 på nivå 2 och 7 på nivå 3.
- **Kursspår:** `yttervinkelsatsen` har 2a, 2b och 2c. De två andra områdena har 2b och 2c, som i strukturen.
- **Figurer:** 26 figurer ritade ur verkliga koordinater.
  - Hålkameran är en skiss som är märkt ”inte skalenlig”, men strålarna går exakt genom hålet.
  - Textkort om definitioner och vinkelsummor saknar figur, eftersom en figur där inte tillför något eller skulle visa lösningsidén, som triangeluppdelningen i femhörningen.
- **Verktyg:** miniräknare är tillåten och GeoGebra nekas. Uppgifterna prövar satser och resonemang, inte beräkningar.

## Kontroll

- **Facit:** alla facit räknades om oberoende. Två krockar med äldre kort och en saknad precisionsfras rättades:
  - 3.2057 hade 108 (krock med 3.499) och har nu toppvinkeln 28°, vilket ger 104°;
  - 3.2087 fick ”med en decimal”.
- **Figurgeometri:** alla vinkelbågar i 17 figurer mättes ur SVG-koordinaterna och stämmer med etiketterna inom 0,6°. Regressionstestet gör samma kontroll.
- **Etiketter:**
  - P i 3.2067 flyttades bort från vinkelbågen.
  - Etiketten 9 cm i 3.2086 togs bort, eftersom D ligger på AB och etiketten var tvetydig. AB anges i texten.
  - Gradetiketterna i 3.2079 och de algebraiska etiketterna i 3.2074 och 3.2076 flyttades från linjerna.
- **SVG-granskaren:** inga verkliga fel kvar. De kvarvarande fynden är heuristiska:
  - `ANGLE_ARC_REVIEW`;
  - bågriktning där vinkelbenen fortsätter förbi spetsen, som i knäckfiguren 3.2078;
  - punktnamn som rör linjer.
- **Validatorn:** inga fynd för de nya korten.
- **Självrättning i Kunskapsgymmet:** 115 kontroller. Rätt svar godtas med och utan enhet (°, cm, cm², m). Fel svar och fel flerval avvisas.
- **Mobil (375 px):** ingen överskridning och inga KaTeX-fel i frågor eller facit.
- **Samordning:** remote hade fått omgång 7 och 9 i Ma2 kap 1–2 från den andra sessionen. S4 lades in på nytt ovanpå den nya banken, och krockkontrollen kördes om.
- **Test:** `tools/ma2-geometri-s4-2026-10-25.test.js` ger 5/5, och alla `tools/ma2-*.test.js` går igenom.
