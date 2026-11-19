# Fy1 kapitel 3: fler figurer, 19 november 2026

## Uppdrag

Fortsättning på kapitel 2 (`FY1_KAP2_FIGURER_2026-11-18.md`). Användaren: ”fortsätt” efter att kapitel 2 blev klart.
Samma önskemål gäller: fler figurer, snygga och med färg, inte generiska och inte där de inte tillför något.

Kapitel 3 hade 458 uppgifter, och 233 saknade figur:

| Område | Uppgifter | Utan figur före | Läge |
|---|---:|---:|---|
| acceleration | 48 | 44 | 11 figurer tillagda 2026-11-19 |
| konstacc | 136 | 100 | 16 figurer tillagda 2026-11-19 |
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

## Urval i konstacc

Alla 100 uppgifter utan figur lästes. Figur lades till i 16 uppgifter med en enda situation: sten kastad nedåt från en
bro (3.30), reaktions- och bromssträcka för en cyklist (3.63), hiss i tre faser (3.68), mutter som lossnar i en hiss
(3.86), kast uppåt från 1,5 m (3.118), backhoppets ansats (3.124), linjal som mäter reaktionstid (3.162), två bollar som
möts (3.170), bil mot hinder (3.172), två vagnar på parallella banor (3.177), bil mot trafikljus (3.378), golfputt
(3.379), två bilar i kö (3.391), kast uppåt från ett tak (3.400), raket med motor på och av (3.406) och vägen A–B–C
(3.387). I 3.400 och 3.387 står figuren efter det stycke som beskriver situationen (`EFTER`). Delkort a i 3.387 har en
egen kortare text och får ingen figur.

Utan figur: enstegsuppgifter (3.273–3.278), uppgifter med bokstäver i stället för tal (3.153, 3.187, 3.189, 3.254,
3.255), tabelluppgifter (3.65, 3.83, 3.167) och samlingsuppgifter där varje delkort har en egen situation
(3.43, 3.90, 3.369, 3.370, 3.373, 3.380–3.386, 3.392–3.409 utom de valda).

## Kontroll

- Byggskript: `tools/bygg-fy1-kap3-figurer-2026-11-19.py`. Regressionstest: `tools/fysik1-kap3-figurer-2026-11-19.test.js`.
- Figurerna är granskade som bilder och med `tools/granska-svg.js`. Inga krockar eller klippta etiketter återstår.
- Hela testsviten ger samma resultat som före ändringen.
- **Kunskapsgymmet är inte synkat i denna session.**
