# Enheten i facit, 6 november 2026

## Användarbeslut

”I Uppgiftslabbet vill jag att enheten visas i facit.” Frågetexten ändras inte. Kunskapsgymmet skriver redan ”Svara i …” vid svarsrutan, och Uppgiftslabbet visar uppgiftens `s`. Enheten ska därför stå i facits svarsrad.

## Kontroll

Svepet går igenom 9 641 svarsdelar med `svarEnhet` i alla sju banker. Delkorten har kontrollerats med Kunskapsgymmets `expandGameTask`, så att varje kort får sitt eget facit och sin egen enhet. I huvudfacit kontrolleras varje dels block för sig.

Följande räknas som att enheten finns:

- enheten med ord, till exempel ”kr per timme”, ”bildpunkter per mm”, ”miljoner kronor” och ”R☉”;
- en likvärdig enhet, till exempel N/C för V/m;
- en annan skrivning av samma enhet, till exempel ”kg m/s” och µ eller μ.

Fy1 kapitel 9, där λ står med s⁻¹ men svarsrad saknas, hanteras av en annan session.

## Ändringar (`tools/facit-enhet-svarsrad-2026-11-06.py`)

| Bank | Uppgifter | Ändring |
|---|---|---|
| Ma1 | 0.633, 0.757, 3.543, 1.1320, 1.1330 | Svarsraden får enheten: 16 s, 4,5 MW, 20 %, 6 cm och 6 cm. |
| Ma2 | 2.760, 1.234 a, 3.454 a | Svarsraden får 6 cm, 105 kr och ”Radien är 5 cm”. |
| Ma2 | 3.38, 3.64, 3.264, 3.266, 3.296, 3.317, 3.326 | Koordinatavstånd får ”längdenheter” enligt beslutet 2026-11-05. 3.64 får också närmevärdet √185 ≈ 13,6. |
| Ma2 | 3.346, 3.317, 5.142, 5.157, 1.697, 1.699 | Facit saknade svarsrad. Nu finns en svarsrad med enhet: 70°, 12 Premium-abonnemang, 14 korta och 10 långa besök, 9 cm och 6 cm samt 30 kr och 15 kr. |
| Ma2 | 5.09, 5.25, 5.90, 5.103, 5.169 | Svarsraden namnger enheten: abonnemang, produkter, W, personer. |
| Ma2 | 5.01 | Hela uppgiften är omskriven enligt facitmallen, se nedan. |
| Ma5 | 3.262, 3.264, 3.265, 3.266 | Svarsraden får cm²/s, cm³/s eller cm/s, och exakta svar med π får ett närmevärde. |
| Fy1 | 8.22, 8.24, 8.33, 8.119, 8.159 | Svarsrader med e-notation (”2,2475e-05 N”) skrivs som tiopotens med tre värdesiffror, till exempel 2,25·10⁻⁵ N. Ändringen görs både i huvudfacit och i delkortets facit. |

**Ma2 5.01** (kampanjpaket) hade mycket tunna delkortsfacit, till exempel ”Ekvationssystemet ger 10 Bas”. Delkort c gick inte att lösa utan svaren från a och b, och ledtråden var en allmän mallfras. Nu:

- **Facit:** varje del har rubriker per steg, ekvationssystemet, elimination och en svarsrad med enhet.
- **Inga läckor mellan delarna:** delkort a eliminerar y och delkort b eliminerar x. Ingen av dem visar den andras svar.
- **Delkort c:** frågan anger att 10 Bas-paket och 8 Plus-paket såldes.
- **Ledtråden:** uppmanar till två ekvationer, en för antalet paket och en för faktureringen.

**Radbrytning i mobil:** tre långa pilkedjor i Ma2 3.454 och 5.142 och i Ma1 3.543 blev för breda och har brutits i rader.

**Mer att undersöka:** Fy2 3.54 har enheten, men facit innehåller generiska rader som inte hör till uppgiften, till exempel ”Välj en positiv riktning” och ”Summera alla rörelsemängder med tecken”. Det är felloggens mönster från 2026-11-03 och kan sökas brett.

## Kontroll

- **Verktyget:** det kräver exakt en träff per ändring inom uppgiftens JSON-objekt och återskapar de granskade bankfilerna byte för byte. Talen i facit är kontrollräknade.
- **Svepet efter ändringen:** de kort som återstår har enheten med ord eller i en likvärdig skrivning.
- **Kunskapsgymmets facitkontroll:** `kvFacit` ger 0 fel på 55 ändrade kort och delkort. Rättningen av 5.01 godtar 10, 8 och 119 000 kr och underkänner svar där delarna är förväxlade.
- **Rendering:** alla ändrade facit renderas i 390 px utan KaTeX-fel eller för breda rader.
- **Regressionstest:** `tools/facit-enhet-2026-11-06.test.js` kontrollerar enheterna, att ingen bank har e-notation i någon svarsrad och strukturen i 5.01.
- **Valideraren:** inga nya fel. Fy1 har ett fel som fanns redan före ändringen.
- **Tidigare röda tester:** fyra tester (`ma1-korrelation-begrepp`, `ma1-korrelation-jamforelse`, `ma1-procent-villkor` och `saknat-underlag`) var röda redan före ändringen. Orsaken är `bankBildadresser is not defined` i Uppgiftslabbets visning.
