# Ma2: fler uppgifter där standardavvikelsen bestäms – 2026-10-22

Användaren påpekade att många uppgifter i området Standardavvikelse egentligen handlar om andra mått, till exempel variationsbredd. Användaren bad om fler uppgifter där standardavvikelsen ska bestämmas, och om flervalsfrågor om vad standardavvikelse innebär.

## Kartläggning

Området `standardavvikelse` hade 81 uppgifter, som blir 171 kort i Kunskapsgymmet. Bara **91 kort** handlar om standardavvikelse eller spridning. De andra 80 gäller:

- median (24),
- typvärde (21),
- variationsbredd (14),
- enbart medelvärde (11),
- kvartilavstånd (8),
- övrigt (2).

De kommer främst från de flerdelade uppgifterna 4.328–4.345, där delarna a, b och d om median, typvärde och variationsbredd eller kvartilavstånd blir egna kort i området. Det är **inte ändrat** i denna omgång. Ett förslag finns sist.

## Nya uppgifter (4.450–4.464)

ID-blocket valdes med marginal, eftersom en parallell påfyllnadssession tar ID i följd i kapitel 4.

| ID | Typ | Nivå/tn | Facit |
|---|---|---|---|
| 4.450 | Sx för 4, 6, 8 | E/1 | 2 |
| 4.451 | Sx ur prickdiagram (läxtid, figur) | E/2 | 1,51 h |
| 4.452 | Sx för stegräknare, tabell med decimaltal | E/2 | 1,8 |
| 4.453 | Sx ur frekvenstabell, skostorlekar (n = 15) | E/2 | 1,18 |
| 4.454 | Två bågskyttar med samma medelvärde: Sx för båda | E/2 | 1,03; 1,75 |
| 4.455 | Sx ur stolpdiagram, mål per match (figur) | E/2 | 1,16 |
| 4.456 | Sx för förbättringar (före − efter) | C/3 | 0,31 s |
| 4.457 | Bestäm x ur medelvärdet och därefter Sx | C/3 | 13; 4 |
| 4.458 | Bestäm x så att Sx = 4 | A/5 | 9,71 |
| 4.459 | Medelvärde och Sx för äggvikter | E/2 | 61,4 g; 2,7 g |
| 4.460 | Flerval: vad standardavvikelsen beskriver (figur med avvikelser i facit) | E/1 | – |
| 4.461 | Flerval: samma variationsbredd men olika standardavvikelse | E/2 | B |
| 4.462 | Flerval: varför standardavvikelse ger bättre bild än variationsbredd | E/2 | – |
| 4.463 | Flerval: Lisa delade med n i stället för n − 1 | C/3 | – |
| 4.464 | Flerval: tolka Sx = 2 min för väntetider | E/1 | – |

Beräkningsuppgifterna följer Sx-regeln: Sx och n − 1 står i frågan, och både GeoGebra och miniräknare är tillåtna. Flervalsfrågorna kompletterar den andra sessionens konceptfrågor 4.384–4.395 utan att upprepa dem.

Det befintliga testet `statistik-sx-2026-10-14` förbjuder σx i Ma2-uppgifter. Därför är 4.463 formulerad som "delat med n i stället för n − 1", utan symbolen σx.

## Verifiering

- Det nya testet `tools/ma2-standardavvikelse-sx-2026-10-22.test.js` räknar om varje Sx ur den data som visas, även tabeller och frekvenser. Det kontrollerar också avrundningsmarginaler och verktygsflaggor. Två dataset byttes vid kontrollen, eftersom Sx låg för nära en avrundningsgräns.
- Statistik- och Ma2-testerna: 97 tester passerar. Validatorn för Ma2 ger samma fynd före och efter.
- Kunskapsgymmet: 26 rättningsfall med rätt och fel svar, i angiven precision och med enhet, fungerar. Varje flervalsfråga har exakt ett rätt alternativ. GeoGebra och miniräknare finns på beräkningskorten. Alla 15 uppgifter syns i 2a, 2b och 2c och visas på 375 px utan KaTeX-fel eller överbredd.

## Förslag, inte genomfört

De flerdelade uppgifterna 4.328–4.345 kan behållas hela i Uppgiftslabbet. I Kunskapsgymmet kan de bara visa Sx-kortet, eftersom `spelDelar` får vara en delmängd av läraruppgiftens delar. Median-, typvärdes- och variationsbreddsdelarna skulle då inte längre dyka upp i standardavvikelseområdet. Det kräver användarens beslut.
