# Fysik 1: varierade rutinuppgifter om effekt, 2026-10-21

## Avgränsning och variation

Efter användarens styrning avbryts den fortsatta utbyggnaden av kärnfysik/elektromagnetisk strålning. Fokus ligger på rutinuppgifter i andra områden. Effekt hade redan 110 uppgifter, men bara två figurer och många formelinsättningar. Sex nya uppgifter kompletterar **sättet att träna**, inte bara antalet: arbetsdiagram, jämförelsetabell, energiflöde, två effektlägen, omvänd dragkraft och verkliga mätarställningar. Nu 116 uppgifter och 8 med figur.

## Alla nya uppgifter

| ID | Innehåll, korrekt svar och nivå |
|---|---|
| 5.623 | 500 W från 3 kJ på 6 s i ett arbetsdiagram. Nivå 1. |
| 5.624 | A ger 500 W och B 300 W; störst arbete behöver inte ge störst effekt. Nivå 2. |
| 5.625 | 600 J nyttigt av 800 J tillfört ger 75 %. Energiflöde med 200 J värme. Nivå 1. |
| 5.626 | Två effektlägen ger 0,04 + 0,02 = 0,06 kWh. Nivå 2. |
| 5.627 | 60 W vid 0,50 m/s ger dragkraften 120 N. Kraft och rörelse åt vänster. Nivå 1. |
| 5.628 | Mätarökning 0,3 kWh på 0,25 h ger 1,2 kW. Startvärdet ska dras bort. Nivå 2. |

Tre nivå 1 och tre nivå 2. Rutinuppgifterna kräver inga härledningar. Nivå 1 har ett direkt samband och lättlästa data. Nivå 2 kombinerar jämförelser, tidsdelar eller två avläsningar. Alla kort är självständiga och självrättande; ingen del behöver data från ett annat kort. Befintliga familjer återanvänds. Miniräknare tillåts; avläsning av färdiga diagram kräver inga GeoGebra-funktioner. Svarsinstruktioner står i parentes och konstanter/formelledningar ges inte i frågorna.

## Granskade jämförelseuppgifter – inget fel i den avgränsade kontrollen

Sex äldre uppgifter jämfördes för fysik, facit och verktyg. Detta är inte en ny fullständig text-/webbläsargranskning av alla 110 äldre uppgifter. Inga befintliga bankobjekt har ändrats.

| ID | Färdigt kommentarsförslag |
|---|---|
| 5.251 | Granskad – inget fel: 15000 J på 20 s ger 750 W. Facit förklarar joule per sekund. |
| 5.254 | Granskad – inget fel: 500 W i 10 s och 1000 W i 30 s ger 35 kJ och 875 W över hela tiden. Tidsviktningen förklaras. |
| 5.261 | Granskad – inget fel: 600 N längs rörelsen vid 2,0 m/s ger 1200 W. |
| 5.325 | Granskad – inget fel: 0,75 av 800 W ger 600 W nyttig effekt. |
| 5.264 | Granskad – inget fel: 1053/1300 = 81 % och 1620/0,81 = 2000 W. Det separata b-kortet anger sin egen verkningsgrad. |
| 5.270 | Granskad – inget fel: 260 W under totalt 67,5 h ger 17,55 kWh, korrekt avrundat till 17,6 kWh. |

**Åtgärdade befintliga uppgifter:** inga. **Nya uppgifter:** samtliga sex ovan. **Nya felrapporter:** inga i denna omgång. **Kvar att utreda:** inget i de sex nya korten.

## Kontrollpunkter

- 5.623: arbete i kJ omvandlas till J innan effekten anges i W.
- 5.624: jämför arbete per sekund. B har större arbete men lägre medeleffekt.
- 5.625: nämnaren är tillförd energi, inte värmen. Energierna balanserar: 600 + 200 = 800 J.
- 5.626: låg effekt pågår fyra minuter, inte sex. Tider i minuter omvandlas till timmar för kWh.
- 5.627: en vinsch till vänster drar lådan åt vänster. Både hastighets- och kraftpilens spetsar pekar åt vänster. Därmed är den överförda mekaniska effekten positiv. Förväxla inte en SVG-banans ritordning med pilspetsens faktiska riktning.
- 5.628: använd ändringen i mätarställning, inte hela slutvärdet. 15 minuter är 0,25 h.

## Verifiering och leverans

- Oberoende formler i nytt test `tools/fysik1-effekt-variation-2026-10-21.test.js` och utökat `tools/fysik1-effekt.test.js`. Det äldre fullständighetskravet omfattar nu 95 numeriska uppgifter och 180 numeriska facitsvar; inga gamla fall eller krav tas bort. `energi-kombinatorik.test.js` passerar också.
- 64 svarskontroller i Kunskapsgymmet, alla alternativ samt olika giltiga enheter och felmetoder; 12 kortvyer vid 390/1280 px. W/kW, N/kN, procent/andel och kWh/Wh/J fungerar.
- Alla sex SVG visuellt granskade i slutlig version. Inga klippta texter, KaTeX-/JavaScript-fel eller sidöverflöden. Kraft- och hastighetspilarnas spetsar kontrolleras även särskilt i regressionstestet.
- Full bankvalidator: ERROR 1577, WARNING 227, INFO 1452 före och efter; inga nya fynd. Äldre fynd utanför omgången kvarstår.
- Gemensam bankbas jämförd före identisk synk. Cacheversion uppdaterad i båda apparna. Ingen ändring av rapportstatus eller elevdata i databasen.
