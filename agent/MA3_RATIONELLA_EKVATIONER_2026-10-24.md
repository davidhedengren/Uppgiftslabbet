# Ma3 – rationella ekvationer, 24 oktober 2026

Åtta nya handskrivna uppgifter, #1.933–1.940. Området växer från 47 till 55
uppgifter. Samtliga hör till kapitel 1 och båda spåren 1b/1c. Påfyllnaden
varierar sättet att använda rationella ekvationer, inte bara koefficienterna.

## Alla nya och granskade uppgifter

| ID | Nivå | Innehåll och kontrollerat svar |
| --- | --- | --- |
| 1.933 | 1 | Läsa av skärningen mellan 6/x och 2 i given graf: x = 3. |
| 1.934 | 1 | Dela en kostnad med belopp per person: 360/60 = 6 personer. |
| 1.935 | 2 | Lika täljare men oförenliga nämnare: 5 = −10 efter omformning, ingen lösning. |
| 1.936 | 2 | Välja korrekt rad efter multiplikation av varje term med 6x: 6+2x = 3x. |
| 1.937 | 3 | En pump saknar känd fylltid: 1/4−1/12 = 1/6, alltså 6 timmar ensam. |
| 1.938 | 3 | Fyra extra deltagare sänker kostnaden per person med 50 kr: 12 personer från början. Den negativa roten −16 är orimlig som antal. |
| 1.939 | 3 | Area och omkrets ger x+24/x = 10. Båda sidvalen 4 och 6 cm godtas i valfri ordning. |
| 1.940 | 3 | Parameter som ger fler än en lösning: a = 4, då alla x utom 2 fungerar. |

Tre egna SVG-figurer (skärningsgraf, pumpar, rektangel) och två tabeller.
Miniräknare tillåts för alla uppgifter. Ingen behöver GeoGebra: grafen är
redan ritad, övriga frågor prövar modeller och exakt algebra. De tre rena
algebra-/felsökningsfrågorna saknar figur eftersom en sådan inte förtydligar
metoden. Facit visar beräkningar och avslutas med svar; långa rader är delade
för mobilvisning.

## Åtgärdade äldre uppgifter

Inga äldre uppgifter ändrade i denna omgång. Inga rapportstatusar ändrade.
Den gamla tabellfrågan som rättades i föregående omgång är dokumenterad i
[deriverbarhetsloggen](MA3_DERIVERBARHET_2026-10-24.md).

## Granskad – inget fel

Avgränsad kontroll av matematik, otillåtna värden och facit i fem närliggande
uppgifter. Detta innebär inte ny fullständig browser-/nivågranskning av dem.

| ID | Egen kontroll och förslag på kommentar |
| --- | --- |
| 1.13 | ”Granskad – inget fel: ekvationen ger x(x−3) = 0 och båda lösningarna 0 och 3 är tillåtna.” |
| 1.150 | ”Granskad – inget fel: vänsterledet är 1 för alla tillåtna x och kan därför inte bli 3.” |
| 1.508 | ”Granskad – inget fel: kandidaten x = 2 gör nämnaren noll, så ekvationen saknar lösning.” |
| 1.535 | ”Granskad – inget fel: x = −2 är tillåtet och gör täljaren noll. x = 2 är förbjudet.” |
| 1.536 | ”Granskad – inget fel: den enda kandidaten är det förbjudna värdet x = 3.” |

## Verifiering

- Egen lösning för samtliga. Exakta rötter och parameteridentiteter även
  verifierade med Sympy; positiva antal och sidlängder kontrollerade separat.
- `tools/ma3-rationella-ekvationer-2026-10-24.test.js` godkänt tillsammans
  med regressionerna för kontinuitet, deriverbarhet, Ma3-facit och validatorn.
- 106 verkliga svarskontroller i Kunskapsgymmet: båda skärmstorlekarna
  390/1280 px, alternativa svar, enheter inklusive timmar/h, fel enhet,
  omkastade sidlängder och samtliga alternativkombinationer.
- 16 kortvisningar utan överflöde, KaTeX-fel eller JavaScript-fel efter att
  den sista långa facitraden delats upp.
- Uppgiftslabbet: alla åtta visas i rätt ordinarie område på båda spår.
- Tre figurer visuellt och geometriskt granskade: inga ERROR/WARNING,
  endast tre INFO om vit bakgrund vid viewBox-kanten.
- Inga validatorfynd för de åtta nya objekten. Hela repots baslinje oförändrad:
  1483 ERROR, 230 WARNING, 1445 INFO. Dessa äldre fynd är inte lösta här.
- Objektdiff bekräftar att inga äldre bankobjekt ändrats. Båda bankkopiorna
  är identiska. Orelaterade Fy1-utkast lämnas utanför leveransen.
- Författarkälla och regression: `bygg-ma3-rationella-ekvationer-2026-10-24.py`
  respektive `ma3-rationella-ekvationer-2026-10-24.test.js` under `tools/`.
  Browserharness med samma områdesnamn/datum finns i respektive repo.
