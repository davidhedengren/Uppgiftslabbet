# Facitmall: inventering av alla sju banker, 2026-11-04

## Slutsats och prioritering

Samtliga **21 582 huvuduppgifter och 30 442 huvud-/delfacit** har strukturskannats mot `FACITMALL.md`, baslinje `1ff40ce`. Detta är inte en manuell matematisk granskning av hela banken. Huvuduppgifter och explicita delkort räknas var för sig, inklusive läraruppgifter som inte visas i gymmet.

Störst samlad strukturavvikelse finns i **Fysik 1**, följt av **Ma4**. Fysik 1 saknar ofta både steglista och namngivna formelrubriker. Ma4 har ofta en steglista men saknar en avslutande svarsruta. Ma5 har också relativt många facit utan steglista. Övriga banker behöver framför allt uppgiftsspecifika rubriker och samlade lösningssteg; Fy2:s nästan 100 % rubrikavvikelse betyder alltså inte att nästan alla lösningar är matematiskt fel.

| Bank | Huvuduppgifter | Huvud-/delfacit | Utan steglista | Utan nya rubrikklassen | Utan svarsruta |
|---|---:|---:|---:|---:|---:|
| Fysik 1 | 4495 | 7911 | 5987 (76%) | 5986 (76%) | 3070 (39%) |
| Fysik 2 | 1765 | 2739 | 229 (8%) | 2727 (100%) | 113 (4%) |
| Matematik 1 | 4730 | 5690 | 461 (8%) | 4946 (87%) | 1793 (32%) |
| Matematik 2 | 3362 | 4231 | 421 (10%) | 2818 (67%) | 636 (15%) |
| Ma3 / fortsättning nivå 1 | 3276 | 3540 | 90 (3%) | 3208 (91%) | 606 (17%) |
| Ma4 / fortsättning nivå 2 | 2251 | 4023 | 369 (9%) | 3850 (96%) | 3060 (76%) |
| Ma5 / fördjupning nivå 1 | 1703 | 2308 | 775 (34%) | 1883 (82%) | 481 (21%) |

## Var granskningen bör fortsätta

1. **Fy1 kopplingar:** 338 huvud-/delfacit, samtliga saknar nya steglistan och rubrikklassen vid inventeringen. 180 är kortare än 150 text-/TeX-tecken. Delområdet **Blandade kopplingar, 26 huvuduppgifter och 37 delkort**, har nu granskats manuellt och åtgärdats i denna omgång. Nästa tydliga delområde är Elektrisk effekt och energi (80 huvuduppgifter). Ems/inre resistans har 48 och effekt/verkningsgrad med inre resistans 14.
2. **Ma4 komplexa tal, konjugat och räknesätt:** 271 facit; 264 utan rubrikklass och 239 utan svarsruta. Prioritera fullständiga svar efter varje del och förklara varför konjugatet används.
3. **Ma4 primitiva funktioner:** 270 facit; 263 utan rubrikklass och 234 utan svarsruta. Granska integrationskonstant, mellanled och kontroll genom derivering.
4. **Fy1 aktivitet och stråldoser:** 190 respektive 125 facit, samtliga utan nya steglistan. Nästan alla saknar svarsruta. Prioritera fysikalisk tolkning, enhetsbyten och skillnaden mellan storheterna.
5. **Ma1 funktionsbegreppet:** 203 facit; 201 utan rubrikklass och 101 utan svarsruta. 165 korta facit bör granskas mot vad frågan faktiskt kräver.

Fy1 kraftavsnittet har också omfattande mallavvikelser men bearbetas redan i den parallella sessionen. Denna omgång lämnar dess innehåll till den pågående genomgången.

## Vad indikatorerna betyder

- Steglista, rubrik och svarsruta avser klassnamnen `facit-steglista`, `facit-rubrik` och `facit-svar` i den beslutade mallen. Avvikelse är inte samma sak som felaktigt slutsvar.
- Kort text är endast en prioriteringssignal. En enkel begreppsfråga kan ha ett fullgott kort facit. Ingen text ändras automatiskt från längdmåttet.
- Ett facit med alla tre klasserna kan ändå ha brister. Formler, mellanled, delindelning, ledtrådar, figurer och rättningsnycklar måste granskas manuellt.
- Exempel från varje bank har lästs: många äldre mallar har löpande text i numrerade listor men saknar specifika rubriker. Att bara byta CSS-klass skulle inte lösa den pedagogiska bristen.

Reproducerbar inventering: `node tools/inventera-facitmall-2026-11-04.cjs`. JSON-filen intill denna rapport innehåller utgångsvärden för alla områden. [Manuell första omgång och kommentarslista](FY1_BLANDADE_KOPPLINGAR_FACIT_2026-11-04.md).
