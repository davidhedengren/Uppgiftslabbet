# Fy1: manuell granskning av densitet, rörelse och krafter, 2026-11-27

I en tidigare chatt föreslogs och gjordes ändringar i Fy1 (lokala commits d4bd27e och 4f62f87). De nådde aldrig GitHub,
eftersom pushen misslyckades i den miljön, och patcharna följde inte med. Ändringarna är gjorda om här, varje uppgift är
kontrollerad mot banken, och de fem rörelseuppgifter som chatten inte namngav är identifierade på nytt. Skriptet är
`tools/fy1-granskning-2026-11-27.py`.

| Uppgift | Fynd | Ändring |
|---|---|---|
| 2.17 c | ”Bestäm densiteten.” efter ”Bestäm densiteten i g/cm³”. Facit begär kg/m³ (288/240 = 1,2 g/cm³ = 1 200 kg/m³). | ”Ange rätblockets densitet i kg/m³.” |
| 2.26 d | Som ovan (1 050/125 = 8,4 g/cm³ = 8 400 kg/m³). | ”Ange kubens densitet i kg/m³.” |
| 2.161 b | Som ovan (5 600/5 000 = 1,12 g/cm³ = 1 120 kg/m³). | ”Ange glykolens densitet i kg/m³.” |
| 2.379 | ”vågrätt” i stället för stilguidens ”horisontellt”. | ”flyter/ligger horisontellt”. `sprak-2026-11-17` går nu igenom. |
| 3.14 | ”Sedan har den den konstanta accelerationen …” | ”Den accelererar sedan konstant med 3,0 m/s² i 4,0 s.” |
| 3.158 | ”Därefter håller den den farten.” | ”Därefter fortsätter bilen med samma fart.” |
| 3.64, 3.120, 3.124, 3.155 | Facit använder tidlösa formeln eller medelfart gånger tid, alltså konstant acceleration, men frågan sa det inte. Utan villkoret går bara en medelacceleration att bestämma. | ”Räkna med att accelerationen är konstant (under inbromsningen).” Tomma `<p></p>` och inledande mellanslag i styckena är borta. |
| 4.368 | ”En satellit är 400 km över ytan.” Tyngdlösheten beror på att satelliten faller fritt. | ”En satellit kretsar runt jorden på 400 km höjd.” |

Andra rörelseuppgifter där facit förutsätter konstant acceleration är redan tydliga. Det gäller till exempel
”accelererar med …”, ”bromsar med …”, ”bromsar jämnt” (3.278), ”samma retardation” (3.206), fritt fall och diagram. I
3.253 är antagandet självt det som prövas.

Svar, facit och rättning är oförändrade. Kontroll:

- Kedjornas delkort börjar fortfarande med inledningen.
- 3.120 och 2.17 är renderade i Kunskapsgymmet.
- `sprak-2026-11-17` går igenom. Densitetstesterna och `fysik1-kapitel3` har samma kända fel som före ändringen.

Granskningen av hela urvalet (193 densitets-, 460 rörelse- och 1 020 kraftuppgifter) är inte slutförd. Det här är
de fynd som hittills är bekräftade.
