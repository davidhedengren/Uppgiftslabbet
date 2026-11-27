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

## Omgång 2: manuell genomläsning område för område

Varje uppgift läses i en kompakt utskrift (text, delkort, svar, enhet, kgInstruktion) och kontrollräknas. Bygger på den
andra sessionens Fy1-revision samma dag (`agent/FY1_REVISION_2026-11-27.md`), som flyttade tabellvärden ur
`spelIntro` och delkort men inte ur huvudtexten `t`.

### Densitet (193 uppgifter, klart) – `tools/fy1-granskning-densitet-2026-11-27.py`

Alla beräkningar stämmer, även A-uppgifterna (2.200, 2.201, 2.290, 2.365–2.377). Ändringar:

- **Tabelldensiteter ur `t` till `kgInstruktion`** (beslutet 2026-11-27 gäller även `t`). 21 uppgifter: 2.117,
  2.122, 2.125, 2.132, 2.143, 2.147, 2.149, 2.150, 2.157, 2.158, 2.162, 2.198, 2.201, 2.202, 2.203, 2.274, 2.277, 2.367,
  2.368, 2.373, 2.375. I 2.367 saknades vattnets och glykolens densitet helt i delkortens instruktion.
- **Står kvar enligt undantagen:** omvandlingsuppgifter där densiteten är uppgiftens tal (2.6, 2.107, 2.108, 2.111,
  2.113), identifiera eller jämföra ämnen (2.24, 2.40, 2.88, 2.92, 2.100, 2.101, 2.104, 2.106, 2.165, 2.169, 2.188),
  värden i en formel eller ett påstående (2.51, 2.116) och uppgiftens egna material (trä, plast, granit, saltvatten,
  ägg, sten, spolarvätska, saft, palladium).
- **”Antag” → ”Anta”:** 2.142, 2.184, 2.195.
- **Tester:** `fysik1-densitet-a-2026-11-18` väntade 36,4 % i 2.200. Facit är 36,1 % med zinkens 7,13 g/cm³
  (formelsamlingen, beslut 2026-11-25), och testet går nu igenom. `felrapporter-2026-11-22-1935` godtar nu
  aluminiumets densitet i `kgInstruktion`.
- 2.85 a (luftens densitet saknades i delkortets instruktion) hade redan rättats av revisionen.

### Medelhastighet (93 uppgifter, klart) – `tools/fy1-granskning-rorelse-2026-11-27.py`

Alla beräkningar stämmer, även ekvationsuppgifterna (2.301, 2.303, 2.315, 2.316) och 2.307, 2.310, 2.317, 2.318,
2.320 och 2.380. Ändringar:

- **Konstanter och tabellvärden till `kgInstruktion`:** ljudets och ljusets fart (3.103), ljusets fart (3.127,
  2.308 b) och jordens radie (3.101).
- **Avrundnings- och svarsinstruktioner** till `kgInstruktion` eller bort: 3.101 a, 2.308 b (”Ange antalet varv.”) och
  3.21 b (”i m”).
- **Lösningsanvisningar och metatext bort:**
  - 3.103: ”Börja med att anta att ljuset inte tar någon tid …”
  - 3.104: ”Antag att s > 0 och v > 0.”
  - 3.229: ”Antag att alla sträckor och farter är positiva …” blir ”Bilen gör inga stopp.”
  - 3.127: ”Antag att signalen går rakt …”
  - 2.297, 2.303, 2.310, 2.315, 2.316, 2.319: ”Ställ upp ett uttryck …” eller ”Ställ upp en ekvation …”
- **2.295, 2.299:** pappersbladets b upprepade situationen med nya ord, och 2.295 sa både ”åker” och ”cyklar”. De har
  fått en ny gemensam inledning, och delkorten är inledning + fråga. I 2.299 b står mellanresultatet 11 934 m i frågan.
- **3.96:** ”Antag” → ”Anta”.
