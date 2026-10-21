# Fysik 1: Mäta med multimeter, 2026-10-21

Användarens önskemål: ett nytt område om att koppla multimetrar. Eleven ser en
multimeter i stil med Mollic MS8201 och ska avgöra:

- uttag: COM, 10A eller µA mA V Ω Hz,
- vredets läge och mätområde,
- var mätaren kopplas in i ett kopplingsschema.

Det nya området `multimeter` ("Mäta med multimeter") ligger i kap 8, efter
"Spänning och resistans". Planeringen saknar en egen multimeterlektion; området
hör till lektionerna om ström, spänning och resistans.

20 nya flervalsuppgifter (`svarstyp:"alternativ"`), 8.530–8.549. Alla har en egen
SVG-figur och en kommentar till varje alternativ. Uttagsfrågorna har två rätta
alternativ (COM + rätt uttag). Kunskapsgymmet kräver att båda markeras.

| ID | Nivå | Delmoment | Innehåll | Rätt svar |
|---|---|---|---|---|
| 8.530 | 1 | Uttag | Spänning över batteri | COM + µA mA V Ω Hz |
| 8.531 | 1 | Uttag | Uttaget som alltid används | COM |
| 8.532 | 2 | Uttag | 0,15 A, noggrannast | COM + µA mA V Ω Hz |
| 8.533 | 2 | Uttag | Elmotor 2 A | COM + 10A |
| 8.534 | 2 | Uttag | Röd sladd i 10A vid spänningsmätning | Flytta röd till µA mA V Ω Hz |
| 8.535 | 3 | Uttag | Okänd ström | Börja med 10A/10 A, gå ned vid behov |
| 8.536 | 1 | Vred | 4,5 V-batteri | V |
| 8.537 | 1 | Vred | Resistans | Ω |
| 8.538 | 2 | Vred | 50 mA | 400 mA |
| 8.539 | 3 | Vred | 1,5 mA, noggrannast | 4000 µA |
| 8.540 | 3 | Vred | Displayen visar OL på 4000 µA | Vrid till 400 mA |
| 8.541 | 2 | Vred | 12 V växelspänning | V + AC med SELECT |
| 8.542 | 1 | Koppla in | Amperemeter | Bryt vid A, i serie |
| 8.543 | 1 | Koppla in | Voltmeter över lampa | A och B |
| 8.544 | 2 | Koppla in | Spänning över L2 i serie | B och C |
| 8.545 | 2 | Koppla in | Ström genom L2 i parallell | Vid R |
| 8.546 | 3 | Koppla in | Amperemeter parallellt | Lampan slocknar, säkringen kan gå |
| 8.547 | 3 | Koppla in | Voltmeter i serie | Lampan lyser inte, visar ≈ batterispänningen |
| 8.548 | 4 (C) | Koppla in | 1,2 A genom L1 | COM + 10A, 10 A, i serie vid Q |
| 8.549 | 3 | Koppla in | Resistans med batteri kvar | Koppla bort batteriet och lossa R |

## Mätarens data

Mätarens data följer förlagan:

- Mätområdena för ström är 4000 µA, 400 mA och 10 A.
- Uttaget µA mA V Ω Hz klarar högst 400 mA.
- SELECT växlar mellan DC och AC.

## Pedagogiska val

- **Vredet ger ingen ledtråd.** Vredet står på OFF i frågor där dess läge annars skulle avslöja svaret (8.531–8.533 och 8.535–8.539, 8.541).
- **Fungerande men sämre val är fel.** Ett val som fungerar men ger sämre noggrannhet räknas som fel när frågan uttryckligen ber om den noggrannaste mätningen (8.532, 8.539), eller när mätområdet är för litet (8.538). Kommentaren förklarar varför.
- **Säkerhetsval.** Vid okänd ström börjar man på 10 A. En amperemeter parallellt kortsluter komponenten. Resistans mäts utan spänningskälla i kretsen.
- **Svarsinstruktionen** står i parentes efter frågan.
- **Verktyg:** miniräknare är tillåten men behövs inte. GeoGebra används inte.

## Verifiering

- Bankvalidator: 0 fel, och inga varningar för de nya ID:na.
- SVG-granskning: inga fynd för de nya uppgifterna. Alla 20 figurer är dessutom granskade visuellt.
- Kunskapsgymmet, lokalt:
  - Området visas efter "Spänning och resistans" med 20 uppgifter och tre delmoment (8, 6 och 6 uppgifter).
  - Alla 20 uppgifter rättas korrekt, både med rätt och med felaktigt val.
  - På mobil (375 px) ryms figuren utan horisontell scroll.
- Test: `tools/fysik1-multimeter-2026-10-21.test.js`.

Kunskapsgymmet har ännu ingen genomgång kopplad till området.
