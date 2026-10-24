# Ma1 omgång B: träddiagram, beroende händelser och svårare sannolikhet, 2026-10-24

Uppdrag: fortsätta med variation och figurer i Ma1. Läraren gav fyra önskemål för omgången:

- Träddiagrammen ska vara snyggare, med raka grenar som eleverna är vana vid.
- De ska gå nedåt, inte vara liggande.
- De ska gärna vara färgglada.
- Vid beroende händelser ska några uppgifter gå ut på att fylla i en sannolikhet i en gren.

Läraren bad också om svårare uppgifter i stil med `Extrauppgifter Sannolikhet.pdf` (Ma1c, kap 5, OneDrive).

## Träddiagram

Alla träd i Ma1 kom från en äldre generator med krokiga grenar. De har ritats om som stående träd med:

- roten överst och raka, färgade grenar nedåt;
- utfallen i färgade bubblor;
- sannolikheterna i vita rutor vid grenarna;
- ljusa färgband per gren från roten;
- produkterna i rutor under löven.

Tal, luckor (”?”) och aria-texter är oförändrade.

- **Uppgifter i Ma1:** 5.02 (med delkort a och b), 5.16, 5.21, 5.123 (a–c), 5.124, 5.155 och 5.157 (a–c). Totalt 15 figurer.
- **5.124:** trädet var redan rakt men liggande och har ritats om i samma stil.
- **Kunskapsgymmet:** genomgången `ma1-grund-5-05` (”Använda träddiagram”) i `typuppgifter-ma1.js` har fått samma träd. Vägarna sen–i tid och i tid–sen är markerade med gul överstrykning. Den slutliga figuren sätts i `trad.steg[0].figur` i justeringsblocket i slutet av filen.

Generatorn ligger i scratchpad-skriptet `tradlib.py` (`rita(struktur, aria)`, `tolka_gammalt(svg)`).

## Nya kort (59)

| Område | ID | Antal | Innehåll |
|---|---|---|---|
| beroende_handelser | 5.600–5.615 | 16 | Se nedan |
| sannolikhet_flera_steg | 5.616–5.617 | 2 | Lyckohjul med okänd sannolikhet x i trädet (ekvation, nivå 5) och tre straffskyttar, ”ett eller två mål” via komplement |
| komplementhandelse | 5.618–5.619 | 2 | Väntat antal elever med minst ett rätt i en gissad frågesport och fyra oberoende brandlarm |
| genomsnittlig_forandring | 3.600–3.612 | 13 | Stapel- och linjediagram, tabell, jämförelse av två företag, två olika procentsatser (7,9 % och inte 8 %), ±20 %, återhämtning efter ett fall |
| brakform | 0.1200–0.1213 | 14 | Pajer, pizza, rutnät, tallinjer, stänger att jämföra, chokladkaka, vattentank och triangel |
| kvadratrotter | 4.750–4.761 | 12 | Kvadrater med area, tallinje med √30, rätvinkliga trianglar (ramp, mobilskärm), cirkel med given area |

Korten i beroende_handelser består av:

- sex kort där eleven fyller i en saknad gren, både i första och andra dragningen;
- ett kort där eleven hittar felet i en elevs träd;
- ett kort där eleven avgör hur många röda kulor som fanns från början;
- produkter i trädet, vägar som adderas och ”vilken fråga besvarar 3/7 · 2/6?”;
- tre kort på nivå 4: med eller utan återläggning i procentenheter, lotter med minst en vinst och lagkaptener med minst en kille.

Kort som liknade befintliga kort fick nya tal eller sammanhang. Inget nytt kort har samma facit som ett annat kort i sitt område.

## Kontroll

- Validatorn ger inga nya fynd: 201 fynd före och efter, sedan en dubblett av ”0,45 som bråk” ersattes.
- SVG-granskaren ger 0 fynd för de nya och omritade figurerna.
- `tools/ma1-omgang-b-trad-2026-10-24.test.js` ger 3/3 pass.
- Testerna som fallerade redan före ändringen gör det fortfarande och påverkas inte. Det gäller felrapporter-2026-10-13, felrapporter-2026-10-16, fysik1-kapitel3, ma1-uttryck-med-parenteser, ma1-verktyg-2026-10-15 och svg-bredd-2026-10-21.
- Självrättningen i Kunskapsgymmet testades i webbläsaren med 77 svar, bland annat:
  - bråk som förlängts eller skrivits i decimalform (”10/16”, ”0,625”);
  - procent med och utan %-tecken;
  - sannolikheter som ”30 %”, ”3/10” och ”0,3”;
  - felaktiga svar.

  Alla gav väntat resultat.
- Kunskapsgymmets testsvit ger 258 pass.
