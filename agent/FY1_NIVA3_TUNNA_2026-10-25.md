# Fy1: nivå 3 i tunna områden, 2026-10-25

**Lärarbeslut:**

- Fyll inte medicinska metoder, standardmodellen eller strålning möter materia. Där görs få uppgifter.
- Fyll övriga tunna områden ett i taget, och pusha efter varje område.
- Uppgifterna ska vara varierade och ingå i kursen, utan svåra eller krångliga formuleringar. Stilen ska likna de befintliga korten.
- Facit görs enligt instruktionen, och figurer används där de passar.

Läget mättes med appens nivålogik efter dagens övriga omgångar. Antal kort på nivå 3:

| Område | Kort på nivå 3 |
|---|---|
| em_stralning | 4 |
| enheter | 5 |
| tyngdkraft | 5 |
| falt | 5 |
| strom | 7 |
| parallellkoppling | 7 |
| potential | 7 |
| sonderfall | 7 |

Varje område kontrolleras i `tools/fysik1-niva3-tunna-2026-10-25.test.js` (nivå, format, facitkrav och dubblettfacit). Numeriska kort i kap 9 läggs också till i strålnings- och kärnfysiktesternas listor.

## 1. Elektromagnetisk strålning (em_stralning): 6 kort, 9.576–9.581

Tre av de fyra befintliga nivå 3-korten var varianter av ”fotoner per sekund”. De nya korten har andra frågetyper:

| ID | Innehåll |
|---|---|
| 9.576 | Energin i en mol fotoner |
| 9.577 | Hur mycket kortare våglängden blir när radiostationen byter frekvens |
| 9.578 | Ljuseffekt ur antalet fotoner (baklänges) |
| 9.579 | Vilken sorts strålning en foton på 5,0 eV är (flerval efter beräkning) |
| 9.580 | Energiintervallet för synligt ljus |
| 9.581 | Hur många gånger större energi en foton av blått ljus har än en mobilfoton |

Konstanterna är desamma som i strålningstestet (h = 6,63·10⁻³⁴ J·s, c = 3,00·10⁸ m/s). Ingen figur, eftersom det inte tillförde något.

Facitgranskningen gjordes före infogningen:

- Facit och ledtråd renderades och lästes igenom.
- Alla facit har metodtext och svarsrad.
- 9 långa räkneled radbröts för mobil.

Kontroller:

- Validatorn ger 788 fynd både före och efter ändringen.
- Självrättningen testades i Kunskapsgymmet med 20 svar, och alla gav väntat resultat.

## Lärarbeslut: konstanter slås upp i formelsamlingen

Läraren beslutade att naturkonstanter inte ska stå i uppgifterna. Svar räknade med c = 2,998·10⁸ ska också godkännas. Regeln står nu i `CLAUDE.md`.

Dagens fysikkort söktes igenom:

- **Konstanter i frågan:** 9.526, 9.527, 9.532, 8.650 och den nya 9.576. De togs bort.
- **Konstanter i ledtråden:** 8.638, 9.537, 9.539 och 9.542. Ledtrådarna formulerades om.
- **Toleranser:** alla kort med c eller h räknades om med formelsamlingens värden (6,626·10⁻³⁴ och 2,998·10⁸).
  - Bara 9.539 underkände då ett korrekt avrundat svar (496 mot facit 497 nm), så toleransen vidgades till 1 nm.

Testet kontrollerar att inga naturkonstanter står kvar i frågor eller ledtrådar.

## 2. Måttenheter och prefix (enheter): 6 kort, 2.359–2.364

| ID | Innehåll |
|---|---|
| 2.359 | Tvärsnittsarean av ett hårstrå i mm² (prefix i kvadrat) |
| 2.360 | Hur långt ljuset färdas på en nanosekund (c slås upp) |
| 2.361 | Volym och kantlängd för en guldkub ur densiteten |
| 2.362 | En laddares energi i kJ och kWh |
| 2.363 | Ungefär antalet sandkorn i en liter (storleksordning) |
| 2.364 | Löparens fart ur tempot i min per km |

Kontroller:

- Facit renderades och lästes igenom, och alla räkneled ryms på mobil.
- Validatorn ger 788 fynd både före och efter ändringen.
- Självrättningen testades med 29 svar, inklusive de rättade konstantkorten. Alla gav väntat resultat.

## 3. Tyngdkraft: 5 kort, 4.897–4.901

| ID | Innehåll |
|---|---|
| 4.897 | Vilken planet det är, ur en mätning (flerval, jämför med formelsamlingen) |
| 4.898 | Lastbilens massa ur tyngdkraften 0,15 MN, i ton |
| 4.899 | Tyngden av en hink med vatten (densiteten ingår) |
| 4.900 | Vilken låda som har störst tyngd, 12 kg på månen eller 2,0 kg på jorden (flerval efter beräkning) |
| 4.901 | Kraftmätarens mätområde på jorden och på månen |

g-värden står inte i frågorna. Toleranserna godtar både 9,81 och 9,82 m/s² samt 1,62 och 1,63 m/s².

De numeriska korten har lagts till i tyngdkraftslistan i `fysik1-kapitel4.test.js`. Antalet i `fysik1-tyngdkraft-variation-2026-10-21` är nu 46 kort, varav 44 spelbara.

Kontroller:

- Facit renderades och lästes igenom, och 3 räkneled radbröts.
- Validatorn ger 788 fynd både före och efter ändringen.
- Självrättningen testades med 13 svar, och alla gav väntat resultat.
