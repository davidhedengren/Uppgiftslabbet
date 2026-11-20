# Ma3c Funktioner: varierade uppgifter utan ”diskret funktion”, 20 november 2026

Användaren, med en skärmbild av fyra nästan likadana uppgifter (”En diskret funktion har värdena f(1)=…, f(2)=… och
f(3)=…. Bestäm f(1)+f(2)+f(3).”): ”Detta ser inte bra ut, variera dessa och ta bort begreppet diskret funktion.”

**Beslut:** Begreppet ”diskret funktion” används inte i uppgifter, facit eller ledtrådar i Ma1 och Ma3c. Skriv i
stället vad det betyder i sammanhanget, till exempel ”kan bara anta heltalsvärden” eller ”man kan bara köpa ett helt
antal”.

| ID | Före | Efter | Svar |
|---|---|---|---|
| 1.545 | f(1)+f(2)+f(3) med givna värden | Sålda lotter tre dagar, tabell, summa | 45 |
| 1.546 | samma typ | Solrosplantans höjd vecka för vecka, graf med punkter, tillväxt h(3) − h(1) | 25 cm |
| 1.551 | samma typ | Biljettpris per antal zoner, tabell, vilket n ger k(n) = 48 | 3 |
| 1.552 | samma typ | Två bowlinghallar, A(n) = 60 + 45n och B(n) = 70n, jämför för n = 4 | 40 kr |
| 1.453 | ”Vilken situation beskrivs bäst med en diskret funktion?” (NP Ma3c ht 2012) | ”I vilken av situationerna kan den oberoende variabeln bara anta heltalsvärden?” Samma alternativ och rätt svar | – |

Ordet är också borttaget ur facit i 1.175, 1.457, 3.120 och 3.737 (Ma3c) och ur ledtrådarna i Ma1 2.85. Nivå,
träningsnivå och `spel` är oförändrade. Kvar: Fy1 3.38 har ordet bara i det interna fältet `typ`, och Ma5 2.470
skriver ”diskret modell” om en rekursionsformel.

Kontroll: `tools/ma3c-funktioner-utan-diskret-2026-11-20.py` (skript) och `.test.js` (skydd). Kunskapsgymmets rättning
är prövad (45, 25 cm, 0,25 m, 3 zoner, 40 kr godtas). Renderat i 390 px. Valideraren: Ma3c 0 fel, 48 varningar,
190 INFO (före 191). Hela testsviten oförändrad.
