# Ma3 – kontinuitet, 24 oktober 2026

Åtta nya handskrivna uppgifter i ordinarie `kontinuitet`, kapitel 1, spår 1b/1c.
Området växer från 48 till 56 uppgifter. Urvalet kompletterar många befintliga
parameterfrågor med graf- och tabelltolkning samt modeller. Detta är en
påfyllnadsomgång, inte ett påstående att hela området är felfritt.

## Alla nya och granskade uppgifter

| ID | Nivå | Innehåll och kontrollerat svar |
| --- | --- | --- |
| 1.925 | 1 | Vattennivå med ett hörn i grafen. Kontinuerlig trots ändrad lutning. |
| 1.926 | 1 | Avgiftens hopp i en trappgraf: 35−20 = 15 kr. |
| 1.927 | 2 | Tabell med angivna ensidiga gränsvärden och funktionsvärden. Kontinuerlig endast vid x = 3. |
| 1.928 | 2 | Kan ett hopp lagas genom att bara ändra f(1)? Nej, vänster- och högergränsvärdena är 2 respektive 4. |
| 1.929 | 2 | Temperaturmodell utan hopp: 28 = 29+k, alltså k = −1. |
| 1.930 | 3 | Skilja ett borttagbart hål från en asymptot: x = 1 och f(1) = −2. Namngivna ordnade svarsfält. |
| 1.931 | 3 | Kontinuerlig temperatur med två teckenbyten: minst två skilda tidpunkter med 0 °C. |
| 1.932 | 3 | Två skarvar: b = 2 och 3a+b = 8, alltså a = 2. |

Samtliga har kontrollerade facit och ledtrådar. Miniräknare tillåts; GeoGebra
behövs inte för de givna figurerna och enkla algebraiska villkoren. Tre egna
SVG-grafer och två tabeller; de tre rena algebrafrågorna får tydligt satta
uttryck i stället för dekorativa bilder. Lösningarna visar centrala mellanled
med en tydlig svarsrad i Ma2-stil. Fyra alternativ används när det finns fyra
rimliga val, inte med irrelevanta utfyllnadsalternativ.

## Åtgärdade äldre uppgifter

Inga äldre uppgifter ändrade i denna omgång. Inga rapportstatusar ändrade.
Ett separat fynd i deriverbarhet #3.1191 tas i nästa omgång: ändligt många
observerade differenskvoter bevisar inte ett gränsvärde.

## Granskad – inget fel (avgränsad kontroll av matematik och facit)

| ID | Egen kontroll och förslag på kommentar |
| --- | --- |
| 1.59 | ”Granskad – inget fel: delarna möts när 5 = 1+c, alltså c = 4.” |
| 1.64 | ”Granskad – inget fel: delarna möts när −1 = 1+c, alltså c = −2.” |
| 1.151 | ”Granskad – inget fel: en kontinuerlig funktion som går från −2 till 5 måste passera 1.” |
| 1.160 | ”Granskad – inget fel: gränsvärdet och funktionsvärdet måste även vara lika.” |
| 1.820 | ”Granskad – inget fel: linjen har inget hål eller hopp vid x = 1.” |
| 1.821 | ”Granskad – inget fel: grafen hoppar från 2 till 3 vid x = 1.” |

Jämförelseuppgifterna har inte genomgått en ny fullständig browserprovning.
Ingen tidigare rättning eller nivåbedömning för dessa ersätts här.

## Verifiering

- Åtta nya objekt; alla gamla bankobjekt oförändrade.
- `tools/ma3-kontinuitet-2026-10-24.test.js`, föregående rationella-regression,
  Ma3-facitregression och bankvalidatorns tester godkända.
- 84 faktiska svarskontroller i Kunskapsgymmet vid 390/1280 px: även felaktiga
  svar, omkastade ordnade fält, enhet och samtliga kombinationer av alternativ.
- 16 kortvisningar utan KaTeX-fel, JavaScript-fel eller sid-/formelöverflöde.
- Uppgiftslabbet: nya frågor hittas och visas i ordinarie område på båda spår.
- Tre SVG:er visuellt och geometriskt granskade. Inga ERROR/WARNING; tre INFO
  om avsiktlig vit bakgrund som går till viewBox-kanten.
- Inga validatorfynd för de åtta nya uppgifterna.
- Författarkälla: `tools/bygg-ma3-kontinuitet-2026-10-24.py`.
- Browserharness: `tools/ma3-kontinuitet-deriverbarhet-2026-10-24.browser.cjs`
  i respektive repo. Nästa omgång lägger till sina ID:n i samma kontroll.
