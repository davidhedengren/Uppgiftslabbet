# Ma2: normalfördelning med verkliga sammanhang – 2026-10-22

Användaren önskade mer text och verkliga exempel i normalfördelningsuppgifterna, i stället för bara ”normalfördelning, standardavvikelse, medelvärde”. Eleverna ska också få se exempel på normalfördelat material. Alla 88 uppgifter i `normalfordelat_material` och `normalfordelning_digitala_verktyg` gicks igenom, och varje facit räknades om.

## Omskrivna uppgifter (51)

Tal, facit, toleranser, nivåer och verktygsflaggor är oförändrade. Bara texten i `t`, `spelIntro` och delkortens `fraga`/`t` har ändrats. I 4.178 har även en rad i facit ändrats, eftersom grupperna nu heter skolor. Exempel på de nya sammanhangen:

| ID | Sammanhang |
|---|---|
| 4.06, 4.181 | blodtryck (mmHg) |
| 4.07, 4.37, 4.99, 4.110, 4.231 | plommon, bullar, äpplen, potatis och ägg (g) |
| 4.08 | normerat test (100 / 15) |
| 4.19, 4.177, 4.13 | löptider |
| 4.26 | gösens längd och maxmått på 61 cm; delkortens egna texter är omskrivna |
| 4.39, 4.196, 4.215, 4.216 | russin, chokladknappar, tändstickor och nötmix |
| 4.44 | födelsevikt hos kattungar (`svarEnhet` "observationer" → "kattungar") |
| 4.50, 4.214 | mankhöjd och vingbredd |
| 4.53 | situps |
| 4.66 | att hålla andan |
| 4.81 | vilopuls |
| 4.95 | körtid för batterier i elsparkcyklar |
| 4.106 | lystid för ficklampor |
| 4.117 | monteringstid |
| 4.122, 4.256 | fartkamera och trafikmätning (km/h) |
| 4.123 | busstid |
| 4.152 | dusch (liter) |
| 4.176 | maxtemperatur i juli |
| 4.217 | blåmusslor |
| 4.218 | fårtackor |
| 4.251, 4.252 | kycklingar och 11-åringars längd; tidigare bara ”Bestäm a/b” |
| 4.45, 4.57, 4.72, 4.116, 4.151, 4.178, 4.232, 4.237 | prov- och testresultat |
| 4.87 | kassation av detaljer (`spelIntro`) |

- **Delkort:** `spelIntro` av typen ”Normalfördelning: μ = …, σ = …” har ersatts med sammanhanget. Delkort som 4.215 b (”Bestäm den övre gränsen.”) är nu självbärande.
- **Beteckningar:** μ och σ skrivs ut bredvid orden i de uppgifter som tidigare använde beteckningarna. Testet `statistik-sx-2026-10-14` kräver σ i 4.06.
- **Nya figurer:** 4.07, 4.19, 4.37, 4.39, 4.69 och 4.232 saknade figur. De har nu en normalfördelningskurva som bara visar de givna gränserna. Kurvan avslöjar alltså inte σ.
- **Svarsenheter:** inga nya `svarEnhet` har lagts till. En enhet byter mobilens siffertangentbord mot texttangentbordet, och svar med enhet godtas ändå. Det är kontrollerat med `delSvarRatt`.
- **Validator:** inga nya fynd. Fem varningar om textkloner försvann: 4.19/4.37, 4.72/4.231, 4.177/4.197, 4.196/4.214 och 4.215/4.216.
- **Kontrollerat utan ändring:** 4.298 b. Facit 3,3 kor följer formelbladets 2,2 %. Toleransen 0,4 godtar både 3 och 3,4.

## Nya uppgifter: känna igen normalfördelat material (4.475–4.479)

| ID | Nivå/tn | Innehåll |
|---|---|---|
| 4.475 | E/1 | Fyra histogram (snett, två toppar, klockform, jämnt): vilket är troligen normalfördelat? |
| 4.476 | E/1 | Vilken storhet är troligen normalfördelad (längd, lön, tärning, ålder)? Ren begreppsfråga utan figur, eftersom alternativen är texter. |
| 4.477 | E/2 | Histogram över 200 pojkars längd: andel mellan 165 och 175 cm (66 %) |
| 4.478 | C/3 | Samma histogram: jämför 66 % och 94 % med 68 % och 95 % (Sx ≈ 5,4 cm ur klassmitterna) |
| 4.479 | C/3 | Snett histogram över telefonköns väntetider. Normalfördelningen ger cirka 7 % negativa tider (GeoGebra). |

## Användarens beställning: 4.480 (standardavvikelse, E/1)

Ett prickdiagram visar en klass IQ-resultat, 24 elever mellan 93 och 107. Natalie, med IQ 140, börjar i klassen. Frågan är vilket spridningsmått som påverkas minst.

| Mått | Före | Efter |
|---|---|---|
| Kvartilavstånd (Ma2-konvention) | 4 | 4,5 |
| Variationsbredd | 14 | 47 |
| Sx | 3,2 | 8,6 |

Facit är kvartilavståndet.

## Verifiering

- **Test:** `tools/ma2-normalfordelning-sammanhang-2026-10-22.test.js` kontrollerar följande:
  - facit är oförändrat i de 51 uppgifterna;
  - inga kontextlösa inledningar finns kvar;
  - de nya figurerna finns;
  - histogramandelar, Sx och andelen negativa väntetider räknas om ur figurernas data;
  - 4.480 räknas om ur prickarnas lägen.
- **Hela sviten:** 595 av 603 tester godkända. De 8 felen (fysik kapitel 3, fysikprosa och felrapporter 2026-10-16) finns redan i HEAD och gäller inte Ma2.
- **Kunskapsgymmet:** 194 tester godkända. Rättning med och utan enhet fungerar, och de 35 berörda korten ger inga KaTeX-fel och ingen överbredd vid 375 px.
