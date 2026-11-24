# Figurer och kort som ser professionella ut, 2026-11-24

Användaren: ”nu fortsätter vi förbättra språk och uppgifter. Det måste se snyggt och professionellt ut. t.ex. korten
ska se bra ut, bilder ska se bra ut osv.”

Arbetssätt: riktiga Kunskapsgymmet-kort renderades i mobilbredd (390 px) med Playwright, både fråga och facit, och
SVG-granskningen (`tools/granska-svg.js`) kördes för alla banker före och efter. Fynden nedan är systematiska och
åtgärdades deterministiskt; enskilda figurer kontrollerades visuellt.

## Kunskapsgymmet (index.html, egna filer)

| Fel i mobil | Orsak | Åtgärd |
|---|---|---|
| Svarsrutorna i kort med flera svar stack ut 3 px utanför kortet | rutnätets kolumn var `auto` och tog rutans naturliga bredd | `.ainputs` och `.apart` har `grid-template-columns:minmax(0,1fr)` |
| Knappen GeoGebra klipptes i högerkanten | formelblad, miniräknare och GeoGebra fick inte plats på en rad | `.hm-grupp` radbryts (`flex-wrap:wrap`) under 640 px |
| Cirka 430 Fy1/Fy2-figurer visades i Times | figurerna anger `font-family="IBM Plex Mono"`, som Uppgiftslabbet laddar men inte Kunskapsgymmet | IBM Plex Mono 400–600 laddas från Google Fonts, som i Uppgiftslabbet |
| Deluppgifter visades som 1. 2. 3. (`<ol>`, 275 listor) eller a. b. c. (`<ol type="a">`, cirka 2 000), medan svarsrutor och facit heter a), b), c) | webbläsarens standardlistor | listor i frågetexten (`.tbody`, inte facits steglistor) visas som a), b), c) med samma räknare som Uppgiftslabbet |
| Facit hade bara cirka 200 px textbredd, och längre formelrader fick rullas | delbokstaven och stegnumret låg i var sin indragen kolumn | under 520 px står delbokstaven över delens lösning, steglistans indrag är 32 px och lösningsrutans kant 14 px |
| AI-bankens spelträd klipptes (högra halvan syntes inte) | figurerna har `min-width:420px` i en rullbar ruta, utan synlig rullning | under 520 px sätts `min-width:0` för dessa figurer; hela trädet syns och kan förstoras med nypzoom. Bankens byggskript ändras inte. |

## Bankerna (master i Uppgiftslabbet)

- `tools/sprak/omskr/mellanslag_delbokstav_2026-11-24.py`: ”<strong>a)</strong>Bestäm” fick mellanslag (Fy1 281
  ställen i 116 uppgifter, Fy2 2). Korten visade ”a)Bestäm”.
- `tools/svg-rattningar-2026-11-24.py`:
  - Gemena SVG-attribut (viewbox, preserveaspectratio, markerwidth, refx …) har rätt skiftläge (cirka 340 figurförekomster i
    Fy2, Ma1, Ma3c och Ma4). En HTML-tolkare hade skrivit om dem. Webbläsaren rättar dem i HTML men inte när figuren
    tolkas som XML, där innehållet hamnade helt utanför bilden (54 av granskningens 72 ERROR).
  - Fy1 9.434: ett tidigare skript hade bytt bindestreck mot typografiskt minus i attribut (`dy="−6" font−size`), så
    10⁻¹⁰ visades som ”10−10”.
  - Ma3c 1.911: ”<” i figurens titel skrivs `&lt;`.
  - Ma5 4.84, 4.109, 4.110: riktningsfältens rad y = −1 och x-axelns tal låg under bildens kant. Ramen flyttas
    (4.84, 4.109: y = 45–363; 4.110: y = −6–316).
- `tools/svg-textstorlek-2026-11-24.cjs`: läsbar figurtext i mobil. Före: cirka 1 900 figurer hade median under 10 px
  i ett 320 px brett kort, 459 under 8 px. Verktyget mäter textens verkliga storlek i Chromium, skalar alla
  font-size med k = 10,5 / median (högst 1,5) och kör SVG-granskningens analys före och efter. Ändringen behålls bara
  om inget fynd av typen text–text, text–geometri, text utanför bilden, punktetikett, måttetikett, gradetikett eller
  kantklippning blir fler; annars provas halva förstoringen och sist lämnas figuren. Bara font-size ändras, aldrig
  koordinater.

  | Bank | figurer | för liten text | förstorade | lämnade av spärren |
  |---|---:|---:|---:|---:|
  | Fy1 | 1 878 | 539 | 408 | 131 |
  | Fy2 | 697 | 156 | 89 | 67 |
  | Ma1 | 654 | 244 | 170 | 74 |
  | Ma2 | 1 126 | 355 | 220 | 134 |
  | Ma3c | 939 | 329 | 284 | 45 |
  | Ma4 | 465 | 296 | 197 | 99 |
  | Ma5 | 187 | 25 | 17 | 8 |

  Ma2 3.14 återställdes efter förstoringen, eftersom `ma2-kap3-overlapp-2026-10-27` (en linje genom etiketten
  ”1,80 m”) är strängare än spärren. AI-banken förstorades inte: den byggs av sina byggskript och ändras i en annan
  session.

Stickprov före/efter i 320 px (Fy1, Ma2, Ma4, Ma5) visade större text utan nya överlapp.

## Granskningen före och efter

ERROR 72 → 2 (kvar: Ma4 2.624, där en kurvgren avsiktligt ligger under bildens kant, och en Ma5-figur som rättades
efter körningen). TEXT_PARTIALLY_OUTSIDE_VIEWBOX 23 → 7, OBJECT_PARTIALLY_OUTSIDE_VIEWBOX 306 → 294. Små ökningar
(EDGE_CLIPPING +7, vinkelbågar +2) kommer från figurer som granskningen först nu kan tolka efter att viewBox rättats.

## Kvar att göra

- 558 figurer med liten text klarade inte spärren och behöver ritas om för hand (lista i planfilen, `#lamnade`).
- AI-bankens figurer: liten text i mobil (min-width borttagen), bör åtgärdas i byggskripten.
- Ma5 4.110: lösningen startar i (0, 3), men riktningsfältet visar bara y ≤ 2.
