# Inventering av hela banken – 2026-10-26

**21475 huvuduppgifter** i sju kurser är inventerade automatiskt. Detta är inte en manuell kvalitetskontroll. Korta lösningar kan räcka för enkla frågor. Fysik ska ha sammanhängande lösningar, inte matematikens numrerade stegrubriker.

107 delkort utan egna facit och sex uppgifter utan ledtråd har åtgärdats i [rundans logg](FACIT_DELKORT_2026-10-26.md). De tidigare 158 Ma3-faciten finns i [Ma3-loggen](MA3_FACITSTRUKTUR_2026-10-25.md). Därefter har hela området partiell integration i Matf1 granskats: [36 huvuduppgifter / 44 kort](MATF1_PARTIELL_FACIT_2026-10-26.md), varav 33 förbättrades och tre var utan fel. Därefter har [linjär approximation i Matf1](MATF1_LINJAR_FACIT_2026-10-26.md) granskats: 39 huvuduppgifter / 48 kort, samtliga förbättrade. Även [derivatrepetition i Matf1](MATF1_DERIVATOR_FACIT_2026-10-26.md) är nu genomgången: 27 huvuduppgifter, samtliga förbättrade. Även [verifiering av differentialekvationer](MATF1_VERIFIERING_FACIT_2026-10-26.md) är genomgången: 29 huvuduppgifter, samtliga förbättrade. Därefter har [första ordningens homogena och inhomogena ekvationer](MATF1_FORSTA_FACIT_2026-10-26.md) granskats: 68 huvuduppgifter, 51 förbättrade och 17 utan fel. Totalt **410 huvuduppgifter granskade och 390 bearbetade i dessa sju rundor**.

| Kurs | Huvuduppgifter | Huvud- och delobjekt | Facit under 150 tecken (söksignal) | Saknar egen lösning | Saknar ledtråd |
|---|---:|---:|---:|---:|---:|
| ma1 | 4674 | 5630 | 3717 | 0 | 0 |
| ma2 | 3362 | 4231 | 1993 | 0 | 0 |
| mato1 | 3276 | 3540 | 1546 | 0 | 0 |
| mato2 | 2251 | 4023 | 1731 | 0 | 0 |
| matf1 | 1703 | 2306 | 668 | 0 | 0 |
| fy1 | 4444 | 7857 | 2508 | 0 | 0 |
| fy2 | 1765 | 2739 | 1221 | 0 | 0 |

## Kvarstående arbete

Fortsätt manuellt område för område med äldre facit som bara anger tal eller hoppar över modell/insättning. Prioritera korta lösningar på nivå 3–5, därefter rutinkort. Kontrollera alla huvud- och delkort, ledtrådar, rättning, verktyg och mobilvisning. Rubriker ska skrivas individuellt, aldrig genereras automatiskt.

Uppgifter utan manuell granskningslogg är fortfarande ogranskade i denna helbanksgenomgång. Många återstår. Noll saknade fält betyder inte att alla facit är pedagogiskt färdiga. Kör om `tools/inventera-facit-2026-10-26.cjs` efter varje runda och håll inventering skild från manuell granskningsstatus.
