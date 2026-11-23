# Fy1 densitet: språket efter lärarens korpus och fler A-uppgifter, 23 november 2026

## Uppdrag

Användaren: ”Jag vill att du förbättrar texterna i området densitet i fysik 1. A-uppgifterna är lite konstiga tycker jag,
så titta på alla.” och sedan ”Lägg sedan in fler uppgifter inom densitet på A-nivå, t.ex. lite blandningar osv”.

## Jämförelse med lärarens korpus

Lärarens egna A-uppgifter om densitet (korpusen från OneDrive, `tools/sprak/korpus.py`) är korta och konkreta, till
exempel ”Brons är en blandning av tenn och koppar. Du har … g tenn och vill tillverka brons med densiteten … Hur många
gram koppar behöver du tillsätta?” och frigolitbiten i rödsprit. De saknar:

- antaganden om att metallernas volymer läggs ihop (”Antag att tennets och blyets volymer tillsammans är bitens volym.”);
- modellspråk (”I en förenklad modell”, ”enligt modellen”, ”Modellen tar inte hänsyn till …”);
- metatext (”Avrunda inte.”, ”Ange guldhalten som talvärde i karat.”, ”Utgå från att de angivna måtten … är korrekta.”);
- metodtips och lösningen i frågan (”För att föremålet ska flyta … måste dess medeldensitet vara lägre …”,
  ”För stålet får du antingen räkna …”);
- ”Referensdensiteter i g/cm³: …” (läraren skriver ”Järn har densiteten …”).

## Omskrivning av befintliga uppgifter (72 uppgifter)

Skript: `tools/sprak/omskr/fy1_densitet_2026-11-23.py` (körs med `tools/sprak/apply.py fy1 …`).

- **A-uppgifterna 2.51, 2.90, 2.146, 2.200, 2.202, 2.276, 2.290, 2.365–2.370.** 2.51 a ”Ställ upp ett samband som
  beskriver ringens densitet” heter nu ”Kalla den andel … för x. Visa att ringens densitet kan skrivas ρ = 19,3x +
  8,93(1 − x).” 2.90 b frågar vad det betyder att volymen i verkligheten blir lite mindre. 2.276 är konkret (”Blir kulan
  tyngre eller lättare?”, ”Mellan vilka värden kan massan ligga?”). Antagandet om att volymerna läggs ihop är borttaget
  för metaller och mjölk men kvar för vätskor som etanol, metanol, glycerol och glykol, kortat till ”Anta att vätskornas
  volymer kan adderas.” (låst för 2.90 av `fysik1-densitet-facit-2026-11-04`).
- **Övriga:** ”redan anpassad linje” (2.8, 2.39, 2.171, 2.172, 2.174), ”Avrunda inte.” (sju uppgifter),
  ”Avrunda till hela gram/kilogram/milliliter” till `kgInstruktion` (2.140, 2.141, 2.156, 2.166, 2.196), 2.191:s
  teckeninstruktion till `kgInstruktion`, ”gjort av samma material rakt igenom” (2.112, 2.144, 2.151), referensdensiteter
  som vanliga meningar (2.92, 2.100, 2.101, 2.104, 2.106, 2.169, 2.188), utan sammanhang i 2.96 och 2.97 (nu
  ”Diagrammet visar …”, Wilma och Noah), ”En annan” i 2.99 (Nils), 2.162 utan ”förenklad modell”, 2.165, 2.168 och 2.199
  omskrivna. 2.77:s delkortsinledning stämmer nu med huvudtexten.
- **Facitfel:** 2.369 b hade trasigt decimalkomma i facit (1743{\,}5/0{\,}163), rättat i huvudfacit och delkort.

## Nya A-uppgifter (2.371–2.376), 6 uppgifter och 9 kort

Byggskript: `tools/bygg-fy1-densitet-a-2026-11-23.py` (räknar varje svar och kontrollerar med assert).

| ID | Delmoment | Sammanhang | Svar | Nivå per kort |
|---|---|---|---|---|
| 2.371 | Sammansatta och ihåliga föremål | 12,0 g guld ska bli en legering med densiteten 15,0 g/cm³: a) gram silver, b) karat | 6,2 g, 16 karat | A 5, C 3 |
| 2.372 | Sammansatta och ihåliga föremål | Kung Hierons krona, 1,00 kg, 60,0 cm³ vatten rinner över: a) volym om rent guld, b) gram silver | 51,8 cm³, 189 g | E 2, A 5 |
| 2.373 | Densitet, flytförmåga och modeller | Ägg (1,08) i 400 ml saltvatten (1,20): hur mycket vatten kan hällas i innan ägget sjunker | 600 ml | A 5 |
| 2.374 | Sammansatta och ihåliga föremål | Lättbetong: a) luftandel, b) densitet när 30 % av porerna fylls med vatten | 79 %, 0,74 g/cm³ | C 3, A 5 |
| 2.375 | Densitet, flytförmåga och modeller | Isbit i gränsen mellan fotogen och vatten: andel i vattnet | 59 % | A 5 |
| 2.376 | Sammansatta och ihåliga föremål | Saftkoncentrat (1,30) och vatten ger saft (1,06): delar vatten per del koncentrat | 4 | A 5 |

- Figurer i 2.372 (kärl som rinner över), 2.373 (ägg i saltvatten) och 2.375 (isbit mellan vätskorna). 2.371, 2.374 och
  2.376 har ingen figur, eftersom en bild inte tillför något där.
- Facit följer `FACITMALL.md`: Givet och sökt, formeln i rubriken, insättning, kontroll och svarsrad.
- Delkort börjar med samma inledning. Mellanresultat står i delkortets fråga (6,2 g silver, 79 % luft).
- Miniräknare tillåten, GeoGebra inte (linjära ekvationer).

## Kontroll

- Regressionstest `tools/fysik1-densitet-a-2026-11-23.test.js`. `fysik1-densitet-facit-2026-11-04` räknar nu 190 uppgifter
  och 65 delkort.
- KaTeX: 0 fel i de nya uppgifterna.
- Testsviten jämförd med läget före ändringen: inga nya fel.
