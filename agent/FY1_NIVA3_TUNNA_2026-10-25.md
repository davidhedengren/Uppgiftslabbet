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
