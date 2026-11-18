# Fy1 kapitel 2: fler figurer, 18 november 2026

## Uppdrag

Användaren 2026-11-18, efter att ha sett figurerna i densitetsuppgifterna 2.365–2.370: ”ändra sedan bilderna i hela detta
kapitel, så det är fler med figur, snygga med lite färger, men inte generiska och inte när det inte tillför något. men
uppgifterna är lite ’tråkiga’ utan figurer ibland. och ibland är det också svårt att tolka uppgiften. De du gjorde nu hade
riktigt bra bilder så mer sånt där det går.”

Kapitel 2 i Fy1 (`uppgifter.js`, kap 2) hade 407 uppgifter, och 292 av dem saknade figur:

| Område | Uppgifter | Med figur före | Läge |
|---|---:|---:|---|
| densitet | 184 | 75 | 27 figurer tillagda 2026-11-18 |
| medelhastighet | 92 | 22 | ej påbörjat |
| matnogg | 68 | 12 | ej påbörjat |
| enheter | 63 | 6 | ej påbörjat |

## Urval i densitet

Alla 109 uppgifter utan figur lästes. En figur lades till där den gör uppgiften lättare att tolka eller roligare:

- **Inre struktur som är svår att föreställa sig:** ihåliga föremål (2.37, 2.77), kula med kärna och skal (2.275, 2.277),
  ihålig kula som svävar (2.290), rör (2.179), kabel i tvärsnitt (2.181), kub med borrat hål (2.180), stav av tre metaller (2.203).
- **Mätsituationer:** mätglas före och efter (2.165, 2.285), sten med luftbubblor (2.114), mätglas på våg (2.188), flaska som
  vägs tre gånger (2.190), bägare på våg med två vätskor (2.196), mätglas med okänd höjd (2.192).
- **Flytande föremål med given andel under ytan:** block (2.144), föremål i okänd vätska (2.151) och träbit (2.289). Vattnet
  ritas genomskinligt över den nedsänkta delen.
- **Föremål och rum med mått:** järnstång (2.163), lektionssal (2.166), falltorn (2.168), oljefat (2.182), stålplåt (2.162),
  bassäng (2.167).
- **Vardagliga förlopp:** majskorn som poppas (2.86), vattenflaska i frys (2.87).

Ingen figur lades till i rena enhetsbyten, i enstegsuppgifter där figuren bara skulle upprepa ett tal, eller där figuren
skulle avslöja svaret. Exempel: 2.149 och 2.150 frågar hur stor del av stocken eller isbiten som är under eller över ytan,
och en skalenlig figur skulle visa svaret.

## Regler för figurerna

- Varje figur är ritad för sin uppgift, med verkliga färger för materialen (koppar, aluminium, guld, järn, trä, vatten).
  Vit bakgrund och fasta färger, som övriga Fy1-figurer, så att de fungerar i mörkt läge.
- Okända storheter markeras med ?, till exempel r = ? och h = ?. Föremål med okänd storlek ritas inte skalenligt.
- Givna värden i figuren är desamma som i texten.
- Figuren läggs efter första stycket i frågan, sist i `spelIntro` och efter första stycket i varje delkort. Inga andra fält
  ändras. Byggskriptet kontrollerar det för varje uppgift.

## Kontroll

- Byggskript: `tools/bygg-fy1-densitet-figurer-2026-11-18.py`.
- Regressionstest: `tools/fysik1-kap2-figurer-2026-11-18.test.js`.
- Rendering: alla 27 uppgifter är renderade i 390 px och granskade som bilder. Etiketter som klipptes eller krockade är flyttade.
- SVG-granskning (`tools/granska-svg.js`, Chrome headless shell med `--no-sandbox`): inga ERROR och inga krockar mellan text
  och geometri. Det som återstår är varningar om ”vinkelbågar”, vilket är ellipsbågar i cylindrar och fatets ringar, och
  INFO om att bakgrundsrektangeln ligger mot kanten. Båda är falsklarm.
- Fy1-testerna (151 filer) ger samma resultat som före ändringen.
- **Kunskapsgymmet är inte synkat i denna session** (ingen behörighet till repot).

## Fortsättning

Nästa steg är medelhastighet, där figurer passar för vägar, kartor, sträckor med olika fart och tidslinjer. Därefter
mätnoggrannhet (mätinstrument med skala, linjal, skjutmått, termometer) och sist enheter, där figurer sällan tillför något.
