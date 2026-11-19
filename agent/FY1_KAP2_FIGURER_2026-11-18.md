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
| medelhastighet | 92 | 22 | 15 figurer tillagda 2026-11-18 |
| matnogg | 68 | 12 | 11 figurer tillagda 2026-11-18 |
| enheter | 63 | 6 | 5 figurer tillagda 2026-11-18 |

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

## Urval i medelhastighet

Alla 70 uppgifter utan figur lästes. Figur lades till i 15 uppgifter med en enda situation där bilden hjälper tolkningen:
backen upp och ner (3.9), förflyttning och fart på en rak gång (3.51), två bilar med olika fart på halva sträckan (3.97),
båt med och mot strömmen (3.125), eko från en klippvägg (3.130), splittider på löparbanan (3.133), rullgång dit och
tillbaka (3.234), blixt och åska (3.103), resa med stopp (3.236), sträcka i bråkdelar (3.235), satellitbana (3.101),
cykeltur till affären (2.296), ljud genom järn och luft (2.304), båtrace med två delsträckor (2.313) och boj med ubåt
(2.320). Byggskript: `tools/bygg-fy1-kap2-figurer-2026-11-18.py`.

Utan figur: enhetsbyten och enstegsuppgifter (till exempel 3.102, 3.256–3.262), uppgifter som redan har en tabell
(3.19, 2.344, 2.350) och samlingsuppgifter där varje delkort har ett eget scenario (2.291–2.295, 2.297–2.319 utom de
valda). En gemensam figur skulle där bara passa en av delarna.

## Urval i mätnoggrannhet

Alla 56 uppgifter utan figur lästes. Figur lades till där mätsituationen är det svåra att föreställa sig: vågens display
(2.234), ett ark i skjutmått mot en bunt med 500 ark (2.15), pendel med tidtagarur (2.243), personvåg med fel (2.245),
lägen på en mätlinje (2.251), cylinder med osäkra mått (2.255), termometer i is och kokande vatten (2.258), tråd lindad
40 varv på en penna (2.269), bägare på våg före och efter avdunstning (2.49), granstam med omkrets och längd (2.45) och
skiva mätt med diameter eller på rutpapper (2.271).

Utan figur: frågor om värdesiffror och avrundning, rena beräkningar med ± och uppgifter där ett ritat intervall skulle
visa svaret, till exempel avrundningsgränserna i 2.236 och 2.237 och om referensvärdet ligger inom intervallet i 2.261.
2.30 och 2.46 har redan en tabell.

## Urval i enheter

Alla 57 uppgifter utan figur lästes. De flesta är rena omvandlingar, där en figur inte tillför något. Figur lades till där
skalan är svår att föreställa sig: solsystemsmodell (2.11), mobilskärmens bildpunkter (2.12), A4-ark mot fotbollsplan
(2.35), kamerasensorns bildpunkter (2.223) och sandkorn i en liter (2.363). Delkorten i 2.11, 2.12 b och 2.35 har egna,
avskalade texter med bara de data kortet behöver. De får därför ingen figur, som annars skulle visa tal kortet inte
behöver (`KORT` i byggskriptet). 2.34 (”0,75 m² = 75 cm²”) fick ingen figur, eftersom en ruta med 100 × 100 cm skulle
ge bort förklaringen som efterfrågas.

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
- **Kunskapsgymmet är synkat 2026-11-19** (commit b3b7c8e, `uppgifter.js` identisk med `cmp`, `BANK_VERSION` 2026-11-19-fy1-figurer-kap2-4). Kunskapsgymmets rättning är prövad med `tools/kg-sjalvrattning-kontroll.cjs`: 1.319 a godtar 2pi, 2π, 6,28 och 6,3, 1.424 godtar 1/√2 och √2/2, och 1.87 godtar (2a+3).

## Läge

Hela kapitel 2 är genomgånget 2026-11-18: 58 nya figurer (densitet 27, medelhastighet 15, mätnoggrannhet 11, enheter 5).
