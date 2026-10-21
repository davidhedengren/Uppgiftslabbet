# Fysik 1: variation i värmeöverföring, 2026-10-21

## Lucka och resultat

Användaren prioriterar områden med liten faktisk variation. Värme hade 121 uppgifter, men endast sex i familjen **Värmeledning och strålning**. De var främst två enkla begreppsval och fyra större beräknings-/resonemangsuppgifter. Sex nya figurkort kompletterar experimenttolkning, strömning, vakuum, temperaturkurvor, energiflöde och termisk jämvikt. Familjen har nu **12 uppgifter**, området **127**, och 17 uppgifter med figur i stället för 11. Inga områden eller familjer har skapats eller flyttats.

## Alla nya uppgifter

| ID | Innehåll, korrekt svar och nivå |
|---|---|
| 7.225 | A: aluminium leder värme snabbare än plast. Nivå 1. |
| 7.226 | Värmeströmning/konvektion: rörligt vatten för med sig energi. Nivå 1. |
| 7.227 | Värmestrålning kan överföra energi genom ett tomrum. Nivå 1. |
| 7.228 | Lika vattenmassor svalnar 30 respektive 15 grader: A avger dubbelt så mycket energi. Nivå 2. |
| 7.229 | 1200 J in minus 300 J reflekterat ger 900 J absorberat. Nivå 1. |
| 7.230 | Samma temperatur innebär att ingen av kopparbitarna värmer den andra, trots olika massa. Nivå 1. |

Fem nivå 1 och en nivå 2. Varje kort tränar en annan situation/representation; inga talvarianter av en gemensam mall. Alla tillåter miniräknare. Färdiga figurer och enkel avläsning kräver inga GeoGebra-funktioner. Alla kort är självständiga och självrättande, med relevant ledtråd, förklarande facit utan numrerade lösningssteg och svarsinstruktion i slutparentes. Inga standardkonstanter eller färdiga lösningsformler skrivs i frågan.

## Alla granskade befintliga jämförelser – Granskad – inget fel

Jämförelserna gäller fysik, facit och verktyg inom det berörda innehållet. Det är inte en ny fullständig språk-/UX-granskning av alla äldre värmekort. Inga äldre bankobjekt har ändrats.

| ID | Färdigt kommentarsförslag |
|---|---|
| 7.2 | Granskad – inget fel: 18 graders skillnad ger 427,5 W genom väggar och 388,8 W genom fönster. Energin under 5040 h är 4114,152 kWh och bytet sparar 1224,72 kr i modellen. |
| 7.8 | Granskad – inget fel: De givna materialdata ger 70,35 J från en liter luft och 292600 J från en liter vatten. Samma temperatur innebär inte samma energimängd. |
| 7.11 | Granskad – inget fel: Järn och trä har samma temperatur efter lång tid i frysen. Järn leder värme från handen snabbare och känns därför kallare. |
| 7.17 | Granskad – inget fel: Tvärsnittsarea/klotyta ger 1361/4 = 340,25 W/m²; 70 procent absorberat blir 238,175 W/m². |
| 7.18 | Granskad – inget fel: Fönstrets 22 graders temperaturskillnad ger 63,36 W och 126,72 kWh. Bytet minskar energin med 42,24 kWh. De efterfrågade avrundningarna stämmer. |
| 7.128 | Granskad – inget fel: Strålning kan färdas genom tomrum. Värmeledning och strömmande luft kräver materia. |

**Åtgärdade befintliga uppgifter:** inga. **Nya:** 7.225–7.230. **Granskad – inget fel:** samtliga sex ovan. **Kvar att utreda:** inget i de nya korten. Inga rapportstatusar, elevkommentarer eller andra produktionsdata skrivs.

## Pedagogiska och fysikaliska kontroller

- 7.225: lika långa/tjocka stavar med samma starttemperatur i samma vatten. Stavarna står genom vattenytan och går inte genom kärlväggen. Smöret finns vid den andra änden. Frågan gäller värmeledningens hastighet, inte ett garanterat smältförlopp med okända värmeförluster.
- 7.226: pilarna visar vatten som strömmar runt, inte ljus- eller kraftpilar. Energin följer med vattnet. Fackordet konvektion förklaras med det svenska värmeströmning.
- 7.227: inga material förbinder de två ytorna genom mellanrummet. Vakuum stoppar inte strålning. Ett tomrum innebär alltså inte fullständig värmeisolering.
- 7.228: samma massa och samma ämne gör att c och m tar ut sig. Det är **temperatursänkningarna** 70−40 och 70−55 som jämförs, inte sluttemperaturerna. Diagrammet har läsbara femgraderslinjer, tydliga ändpunkter och både heldragen/streckad kurva. `svarFormat: multipel` gör att även **dubbelt** godtas.
- 7.229: ingen strålning passerar plattan. Av lampans 1200 J reflekteras 300 J och absorberas 900 J. Detta är absorberad strålningsenergi, inte ett påstående om hela plattans temperaturändring eller all dess övriga energiomsättning.
- 7.230: lika temperatur ger termisk jämvikt även vid olika massa och olika inre energi. Felalternativen skiljer dessa begrepp åt och har egna förklaringar.

## Tester och leverans

- Nytt `tools/fysik1-varmeoverforing-variation-2026-10-21.test.js`: oberoende energiberäkningar, temperaturdifferenser, metadata, unika figurer och entydiga alternativ. Rätta alternativ ligger på fyra olika platser i källdata; hela alternativen får blandas av konsumenten.
- Äldre `fysik1-varme.test.js` bevarar samtliga 102 beräkningsmodeller och 138 kontroller av numeriska facit. Endast det förväntade antalet uppgifter uppdateras från 121 till 127. De två nya numeriska korten kontrolleras i det nya testet. Formelsamlingstestet passerar också.
- **56 svarskontroller och 12 kortvyer** i Kunskapsgymmet vid 390/1280 px. Alla alternativ prövade; 2/dubbelt/2 gånger och J/kJ fungerar. Fel kvot, fel energibelopp och felalternativ avvisas.
- Samtliga sex SVG visuellt granskade. Inga klippta texter, KaTeX-/JavaScript-fel, sidöverflöden eller överfulla displayformler.
- SVG-validatorns oförändrade DOM-/geometrifunktioner körda genom Playwright: 0 ERROR, 0 WARNING, 6 INFO. INFO avser avsiktliga vita bakgrunder vid viewBox-kanten, inte avklippta etiketter.
- Full bankvalidator före/efter: ERROR 1577, WARNING 227, INFO 1450 oförändrat; inga nya fynd. Äldre fynd utanför omgången kvarstår.
- Gemensam bankbas verifierad före identisk synk till Kunskapsgymmet; cacheversioner uppdateras i båda apparna. Orelaterade prototyper och Python-cache bevaras.
