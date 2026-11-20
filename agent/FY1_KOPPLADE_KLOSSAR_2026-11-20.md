# Fy1: kopplade klossar med snören och trissor, 20 november 2026

## Uppdrag

Användaren laddade upp lärarens häfte ”Färdighetsträning – Newtons andra lag” (skannad PDF från 2016, 15 uppgifter,
facit och lösning av exempel 2 och 6):

> När du är klar vill jag att du gör detta häfte lite snyggare. En glowup helt enkelt. Uppdatera bilderna med lite
> snyggare färger och kanske skuggningar, se till så facit är rätt och layouten blir bättre helt enkelt. Sedan vill
> jag att du lägger in dessa uppgifter i uppgiftslabbet/kunskapsgymmet och lägger till fler liknande. Men där vill jag
> att varje fråga är fristående, så då måste det stå t.ex. ”en kloss med massan…” osv, inte att den förväntas att man
> sett de tidigare. Lägg till på olika nivåer.

## Häftet

- `material/fysik1/Fardighetstraning_Newtons_andra_lag.pdf` (6 sidor A4) och `.html`, byggda med
  `tools/bygg-hafte-newton2-2026-11-20.py --deps=<mapp med katex/package>`.
- Sida 1: rubrikband, rutan ”Så här gör du” (frilägg, positiv riktning, \(F_{\text{res}}=ma\) för varje kloss, lös
  ekvationssystemet), givna värden (F = 10 N, m = 1,0 kg, g = 9,82 m/s²), ”Högre nivå” (lös algebraiskt först), uppgift
  1–4 och rutan ”Bra att veta”. Sida 2–3: uppgift 5–15. Sida 4: facit. Sida 5–6: lösning av exempel 2 och 6.
- Figurerna ritas om med `tools/newton2_klossar.py`: klossar med färgtoning och skugga, bord i trä med ben, trissor
  i metall, streckat golv, röd dragkraft och friktionsyta där det finns friktion. Snörena märks \(S_1\), \(S_2\) i
  kedjans ordning när det finns fler än ett. Uppgift 13 ritas som originalet, med ett snöre över ett bord och en
  trissa i varje hörn.
- Exemplen har färgade friläggningar (\(F_N\), \(F_g\), \(S\), \(F\)) och ekvationssystem med numrerade ekvationer.
  Felskrivningen ”\(F=\tfrac{10}{3}\) N” i exempel 2 är rättad till \(S\).
- Facit visar för varje uppgift accelerationen och snörkrafterna med två värdesiffror och det algebraiska uttrycket.

### Facit i originalhäftet

Facit räknades om med g = 9,82 m/s². Det gamla facit blandade g = 9,82 och g = 10 och hade räknefel. Bara uppgift 1, 2
och 6 stämde helt.

| Nr | Gammalt facit | Rätt |
|---|---|---|
| 3 | a = 1,7; S₁ = 1,7; S₂ = 5,1 N | S₂ = 5,0 N (3m·a = F/2) |
| 4 | a = 8,0 | 9,0 m/s² ((10 − 1,0)/1,0) |
| 5 | a = 1,3; S = 3,3 | a = 2,3 m/s² |
| 7 | a = 1,3; S₁ = 2,9; S₂ = 17 | a = 7,0 m/s²; S₁ = 17 N; S₂ = 11 N |
| 8 | S = 6,6 | 6,5 N |
| 9 | a = 6,7; S₁ = 13; S₂ = 10 | a = 6,5 m/s²; S₂ = 9,8 N (g = 10 användes) |
| 10 | a = 1,7; S₁ = 5,1; S₂ = 8,3 | a = 1,6 m/s²; S₁ = 4,9 N; S₂ = 8,2 N |
| 11 | a = 6,0; S = 8,0 | a = 6,2 m/s²; S = 7,2 N |
| 12 | S₁ = 10; S₂ = 4,0 | S₁ = 9,0 N; S₂ = 3,6 N |
| 13 | a = 5,0 | 4,9 m/s² |
| 14 | S₂ = 40 N | 20 N (= 2mg) |
| 15 | a = 2,2; S₁ = 24; S₂ = 37 | a = 0,65 m/s²; S₁ = 21 N; S₂ = 28 N |

## Bankuppgifter: Fy1 newton2, nytt delmoment ”Kopplade klossar med snören och trissor”

26 uppgifter och 53 delkort (`tools/bygg-fy1-kopplade-klossar-2026-11-20.py`). Uppgifterna är fristående: varje text
anger massorna i kg, krafterna, friktionen och hur snörena går, och varje uppgift har en egen figur. Häftets m och F
är ersatta med 1,0 kg och 10 N.

| ID | Innehåll | Nivå per kort |
|---|---|---|
| 4.979–4.993 | Häftets uppgift 1–15 | se nedan |
| 4.994 | Leksakståg, bara accelerationen | E2 |
| 4.995 | Kraften i dragkroken på en släpvagn, given acceleration | E1 |
| 4.996 | Kran lyfter balk som accelererar uppåt | E2 |
| 4.997 | Labbvagn och hängande vikt, bara accelerationen | E2 |
| 4.998 | Hink med murbruk och motvikt över trissa | C3, C3 |
| 4.999 | Låda med glidfriktionstal och hängande vikt | C4, C3 |
| 4.1000 | Okänd hängande massa ur uppmätt acceleration | C4 |
| 4.1001 | Algebraiskt: m och 3m över trissa (svar g/2 och 3mg/2, format `uttryck`) | A4, A5 |
| 4.1002 | Vilken massa ger accelerationen 1,5 m/s² (två trissor och friktion) | A5 |
| 4.1003 | Acceleration och fart när vikten når golvet | C3, C4 |
| 4.1004 | Dragkraften ur två kända snörkrafter och en okänd massa | A5 |

Häftets uppgifter: 4.979 E1, 4.980 E2/C3, 4.981 E2/C3/C3, 4.982 E2, 4.983 C3/C3, 4.984 E2/C3, 4.985 C3/C4/C4,
4.986 E2/C3, 4.987 C3/C4/C4, 4.988 E2/C3/C3, 4.989 C3/C3, 4.990 C4/C4/C4, 4.991 E2/C3, 4.992 C3/C4/C4,
4.993 C4/C4/C4. Accelerationen i enkla system utan friktion (skillnad i tyngd delat med total massa) är E2. Totalt
12 kort på träningsnivå 1–2.

- **Facit** följer `FACITMALL.md`: Givet och sökt med positiv riktning, rubriker med \(F_{\text{res}}=m_{\text{tot}}a\)
  eller \(F_{\text{res}}=ma\) för en namngiven kloss, insättning och svarsrad med två värdesiffror. Delarna om
  snörkrafter börjar med en friläggning av just den kloss som används (figur med färgade kraftpilar).
- **Delkort** börjar med samma inledning och figur. Delar om snörkrafter får accelerationen med fyra värdesiffror i
  frågan, och delfacit säger ”Accelerationen är given”. Inget delfacit avslöjar en senare del.
- **Rättning:** `svarVardesiffror` 2 och `svarEnhet` m/s², N, kg eller m/s. Fullt värde lagras i `rättSvar`.
  Miniräknare tillåten, GeoGebra inte (linjära ekvationer).
- **g** står inte i frågorna. Eleverna använder formelsamlingens värde.

## Kontroll

- Svaren räknas om oberoende i `tools/fy1-kopplade-klossar-2026-11-20.test.js`. Byggskriptet till häftet jämför
  modellens svar med en separat kontrollräkning.
- Kunskapsgymmets rättning (`tools/kg-sjalvrattning-kontroll.cjs`, 67 kort): rätta svar med och utan enhet, kN, g,
  ”g/2”, ”0,5g”, ”3mg/2” och ”1,5mg” godtas; det gamla facitets felvärden underkänns.
- Valideraren: Fy1 0 fel, 10 varningar, 754 INFO, samma som före (26 fler uppgifter).
- SVG-granskning: inga ERROR eller WARNING för de nya figurerna efter att avståndet mellan hängande klossar ökades.
- Alla 26 uppgifter och häftets sidor är renderade och granskade som bilder (390 px respektive A4).
- `fysik1-newton2.test.js` låste antalet newton2-uppgifter till 136; det nya delmomentet räknas där bort och testas
  i det nya testet.
