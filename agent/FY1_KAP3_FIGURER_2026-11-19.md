# Fy1 kapitel 3: fler figurer, 19 november 2026

## Uppdrag

Fortsättning på kapitel 2 (`FY1_KAP2_FIGURER_2026-11-18.md`). Användaren: ”fortsätt” efter att kapitel 2 blev klart.
Samma önskemål gäller: fler figurer, snygga och med färg, inte generiska och inte där de inte tillför något.

Kapitel 3 hade 458 uppgifter, och 233 saknade figur:

| Område | Uppgifter | Utan figur före | Läge |
|---|---:|---:|---|
| acceleration | 48 | 44 | 11 figurer tillagda 2026-11-19 |
| konstacc | 136 | 100 | ej påbörjat |
| vektorer | 101 | 58 | ej påbörjat |
| st_diagram | 54 | 12 | ej påbörjat |
| vt_diagram | 68 | 12 | ej påbörjat |
| at_diagram | 51 | 7 | ej påbörjat |

## Regler

Samma som i kapitel 2: varje figur är ritad för sin uppgift, med vit bakgrund och fasta färger. Okända storheter
markeras med ?, och figuren visar inget svar. Figuren läggs efter första stycket i frågan, sist i `spelIntro` och efter
första stycket i varje delkort. Delkort med egna, avskalade texter får figuren bara när de har samma data (`KORT` i
byggskriptet). Inga andra fält ändras.

Särskilt för kapitel 3: **riktningsval skrivs inte i figuren.** Efter språkomskrivningen står ”Höger räknas som positiv
riktning.” och liknande bara i `kgInstruktion`, eftersom lärarens prov inte skriver det på papper. Figurerna visar
därför hastigheter som pilar med storlek, eller med tecken när tecknet står i texten (till exempel +12 m/s och −12 m/s
i 3.223), men aldrig ordet ”positiv”. Testet kontrollerar det.

## Urval i acceleration

Alla 44 uppgifter utan figur lästes. Figur lades till där riktningen byts eller där flera föremål är inblandade:
telefon i mjukt skydd (3.213), bil före och efter kollision (3.214), basketboll som studsar (3.215), tennisboll mot
racket (3.216), klubbhuvud och boll (3.217), två testvagnar (3.218, bara huvudfrågan eftersom delkorten handlar om en
vagn var), cyklist som passerar markeringen åt båda hållen (3.223), två motorcyklar med motsatta accelerationer
(3.226), vagn på lutande plan (3.210), bil som hinns ikapp (3.360) och planet i elliptisk bana (3.203).

Utan figur: enstegsberäkningar (3.190, 3.270–3.279), tabelluppgifter och uppgifter där varje delkort har en egen
rörelse (3.151, 3.192, 3.198, 3.368), samt 3.207, där ett a–t-diagram skulle visa lösningen.

## Kontroll

- Byggskript: `tools/bygg-fy1-kap3-figurer-2026-11-19.py`. Regressionstest: `tools/fysik1-kap3-figurer-2026-11-19.test.js`.
- Figurerna är granskade som bilder och med `tools/granska-svg.js`. Inga krockar eller klippta etiketter återstår.
- Hela testsviten ger samma resultat som före ändringen.
- **Kunskapsgymmet är inte synkat i denna session.**
