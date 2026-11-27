# Fy1-revision 2026-11-27: felrapporter, densiteter och deluppgiftskedjor

Användaren: ”Fortsätt revidera språket och uppgifterna i fysik 1. Det är många som är lite konstiga. Börja med dessa
felrapporter och gör sedan liknande ändringar i alla uppgifter, samt det som står i instruktionerna.” Dessutom:
”rullgång” ska skrivas om till rulltrappa, rullband eller liknande.

Skript: `tools/sprak/fy1_revision_2026-11-27.py <steg> [--skriv]` med stegen `rapporter`, `grammatik`, `densitet`, `tabell`,
`kedja`, `figur` och `kg_tillbaka` (körs i den ordningen; `densitet` och `kedja` kan köras om och ändrar då inget). Handskrivna kedjefrågor:
`tools/sprak/omskr/fy1_kedjor_2026-11-27.py`. Test: `tools/fy1-revision-2026-11-27.test.js`.

## Felrapporter 2026-11-27 09:54

| Uppgift | Rapport | Åtgärd |
|---|---|---|
| 2.110 | Konstigt formulerad | ”Vilken volym har 206 g av havsvattnet?” (ett fristående kort som tappat sitt sammanhang) → ”Hur stor volym har 206 g havsvatten?”. Ledtråden om ”deras sammanlagda massa” omskriven. Densiteten står i `kgInstruktion`. |
| 2.84 | ”berätta inte densiteterna, detta ska eleverna slå upp” | Aluminiums densitet borttagen ur Kunskapsgymmets inledning och delkort; den står bara i `kgInstruktion`. Ledtrådarna sa ”varje kubikcentimeter har massan 2,70 g” och är omskrivna. Gäller hela Fy1, se nedan. |
| 2.82 | ”ta bort bortse från möblernas och personernas …” | Förbehållet borttaget överallt. ”Avrunda till hela kilogram.” borttaget; precisionen ligger i `svarVardesiffror` (3). Luftens densitet står kvar (gas, beror på temperaturen). |
| 2.55 b | ”a) och b) är samma?” | Delkortet hade tappat enheten: ”Bestäm densiteten.” → ”Ange densiteten i kg/m³.” Enheten är här själva uppgiften (omvandlingen). |
| 2.52 c | ”frågan kommer igen i c) men inte b)” | c hade en egen inledning med 30 kg, så kedjan visade hela situationen igen. Nu börjar alla tre delkort likadant och c frågar ”Hur stor blir radien om klotet i stället ska ha massan 30 kg?”. Samma fel fanns i många uppgifter, se kedjor nedan. |
| 3.72 | ”formulera om” | ”Bestäm kvoten mellan falltiden vid 1,62 m/s² och falltiden vid 9,82 m/s².” → ”En sten släpps från samma höjd på jorden och på månen. Hur många gånger längre tid tar fallet på månen? Bortse från luftmotståndet.” Tyngdaccelerationerna slås upp; 2,45–2,48 godtas via `svarTabell` (1,6/1,63 och 9,81 m/s²). |

Rullgång → rullband: 3.234 och 2.318 (”Ett 90 m långt rullband”, ”Ett rullband på en flygplats rör sig med
0,65 m/s.”). I 3.234 ersattes metatexten ”Anta konstanta gångfarter, omedelbar vändning och L > 0, v > u ≥ 0.” med
”Rullbandets fart u mäts relativt golvet och personens fart v relativt rullbandet. Vändningen tar ingen tid.”

Grammatik: 7.149 ”Antag att en kropp med massan 65 kg effekten 200 W och bildar ingen ny värme.” → ”En kropp med
massan 65 kg avger värme med effekten 200 W men bildar ingen ny värme.” 6.454 ”… i röret vara högst …” → ”får vara
högst”.

## Densiteter: aldrig i frågetexterna, bara i kgInstruktion

Felrapporten om 2.84 (”berätta inte densiteterna”) gällde att densiteten stod i själva frågetexten i Kunskapsgymmet
(inledningen och delkorten), inte bara i instruktionen. Användarens förtydligande samma dag: ”i uppgiftslabbet ska
det inte vara med några densiteter som finns i formelsamlingen, men i kunskapsgymmet kan de stå för att det ska bli
rätt med rättningen, men då finns det ju en egen del i koden.” Den delen är `kgInstruktion`, som bara Kunskapsgymmet
visar, sist under frågan. Beslutet från 2026-11-23 gäller alltså och förtydligas:

- Tabelldensiteter för vatten, havsvatten, is, metaller, kvicksilver och etanol är borttagna ur alla frågetexter:
  `spelIntro`, delkortens `t` och `fraga`, och där de fanns kvar ur `t` (6.255, 6.309, 6.33, 6.440, 6.494). Formerna
  var bland annat ”Vattnets densitet är 998 kg/m³.”, ”Densitet: vatten 1 000 kg/m³, is 917 kg/m³.”, ”i vatten med
  densiteten 998 kg/m³”, ”En järnkula med radien 3,0 cm och densiteten 7870 kg/m³”, ”Materialets densitet är 11340
  kg/m³.” och ”Lufttrycket är 101,3 kPa och vattnets densitet 998 kg/m³”.
- Värdena står i stället i `kgInstruktion` som egna meningar (”Blyets densitet är 11,3 g/cm³.”), på uppgiften och på
  varje delkort som hade värdet, så att ett ensamt delkort också har det (steget `kg_tillbaka`, 298 uppgifter).
- Blandade meningar behåller den andra uppgiften i texten eller instruktionen: ”Kopparns resistivitet är 1,7·10⁻⁸
  Ωm.”, ”Oljans densitet är 850 kg/m³.”, ”Plasten har densiteten 1,20 g/cm³.”
- Står kvar i texten: gasernas densitet (luft, helium, vätgas), uppgifternas egna data (trä, olja, plast, saltvatten
  1030 kg/m³) och undantagen i `t` från 2026-11-23 där eleven ska identifiera ämnet. Facit är oförändrat.
- Rättningen är oförändrad (`svarTabell` som före ändringen). 3.72 har nya `svarTabell` för tyngdaccelerationen,
  som nu slås upp: 2,45–2,48 godtas.

## Deluppgiftskedjor: alla delkort börjar med samma inledning

Kunskapsgymmets kedja (a → b → c) visar bara det som skiljer en dels text från de föregående. När en del hade en
egen, förkortad inledning (ofta a på träningsnivå 1) eller ett ändrat tal i inledningen visades hela situationen
igen, och två delar kunde se likadana ut (2.52, 2.55). 242 uppgifter är omgjorda så att varje delkort är
`spelIntro` + delens fråga:

- Omkring 150 automatiskt: varje mening i delens egen inledning stod ordagrant i `spelIntro`.
- Resten genomlästa för hand (lista `BEHALL` där frågorna behålls, `KEDJA` med 163 nya frågor i 89 uppgifter) där det som ändras står i frågan (”I en annan krock bromsas samma bil
  från 14 m/s till stillastående på 0,20 m. Hur stor är bromskraften då?”, ”Massorna byter plats: …”,
  ”Personen drar i stället rakt uppåt i lådan med 40 N.”), behövda mellanresultat står i frågan (”Accelerationen
  är 2,29 m/s². Hur stor är kraften i snöret till den hängande vikten?”) och två delar med samma fråga har fått
  olika frågor (”före studsen”/”efter studsen”, ”den första vagnens”/”den andra vagnens”). Villkoren i
  inledningen (friktion, luftmotstånd) kontrollerades mot facit för delar som tidigare hade egen text.
- Överhoppade: uppgifter utan gemensam inledning eller där inledningen bara är ett förbehåll (”Bortse från
  luftmotståndet.”, ”Beräkna följande.”), med fristående delar som visas hela, som avsett (bland annat 6.26, 9.63,
  5.476, 7.140).

Kvar för en senare omgång: ett sextiotal uppgifter där delens fråga själv upprepar inledningens data (till exempel
8.13 b ”Ett batteri med ems 1,5 V och inre resistans 0,60 Ω kopplas till …”). Kontrollera med kedjesimuleringen i
`fy1_revision_2026-11-27.py` (`visas_igen`).

Delar med ändrat kraftläge behåller sin egen text utan inledningens kraftbild (`EGEN_TEXT`: 4.31 c och d, 4.53 d,
4.88 d, 4.98 c, 4.206 c, 4.237 d), eftersom ett ensamt delkort annars visar en kraftbild som motsäger frågan (beslut
som skyddas av `fysik1-newton2` och `fysik1-kapitel4`). Kedjan visar ändå bara det som skiljer sig.

Äldre tester som låste regeln att delkort på nivå 1–2 bara visar sina egna data är uppdaterade, med kommentar:
`felrapporter-2026-10-11-1131`, `-10-11-1902`, `-10-22`, `-11-22-1935`, `fysik-felrapporter-2026-10-08`,
`fysik1-densitet-2026-10-22`, `fysik1-temperatur`, `fysik1-tryck`.

Delkort med en egen figur som visar delens ändrade situation har kvar den efter frågan (steget `figur`): 4.251 b
(m = ?), 3.311 c (simmarens drift), 4.245 c (0,10 m), 3.93 c (78 m/s). Övriga egna figurer var förenklade varianter
av inledningens figur.

## Kontroll

- `tools/fy1-revision-2026-11-27.test.js` (felrapporterna, rullband, inga tabelldensiteter i frågetexterna men i
  `kgInstruktion`, kedjorna, grammatiken).
- Alla `tools/*.test.js` som läser `uppgifter.js` jämförda med läget före ändringen.
- Andra sessionens commit d9c8312 (figurer, inledningar i 4.747, 4.647, 6.88, 6.530, 6.538, 7.139) hämtades först;
  stegen kördes om ovanpå och gav samma resultat som före hämtningen för alla övriga uppgifter.

## Omgång 2 samma dag: alla tabellvärden bara i kgInstruktion

Samma princip som för densiteterna gäller alla formelsamlingsvärden. Steget `tabell` flyttar dem ur Kunskapsgymmets
frågetexter (`spelIntro`, delkortens `t` och `fraga`) till `kgInstruktion` på uppgiften respektive delkortet: 77
uppgifter, främst vattnets och isens specifika värmekapacitet, smält- och ångbildningsvärme (”Isens smältvärme är
334 kJ/kg.”), ljudets fart i luft och vatten, kopparns resistivitet, g på månen och Mars, kol-14:s halveringstid och
gasernas densitet. Igenkänningen är `tabell_till_kg.rensa_t` från 2026-11-23, som bara flyttar värden som stämmer
med tabellvärdet; uppgiftens egna data står kvar (2.312: ljudfarten 1304 m/s i ett material).

Dessutom: 7.117 ”0,200 kg is vid 0 °C har smält till 65 %.” → ”Av 0,200 kg is vid 0 °C har 65 % smält.” och 9.216
flervalsstammen ”Två isotoper av samma grundämne skiljer sig åt i...” → ”Vad skiljer två isotoper av samma grundämne
åt?”. En sökning efter fler fristående kort som tappat sitt sammanhang (som 2.110) gav inga fler.

Metatext: ”med ett digitalt verktyg” → ”med GeoGebra” i 6.190 och 2.46 (båda har `geogebra: true`). Rubriken
”Fördjupning: …” i 8.294 och 8.439–8.444 står kvar trots stilguiden, eftersom fellogg 2026-11-11 uttryckligen
märker dem som fördjupning (`fellogg-fy1-2026-11-11.test.js`); fråga användaren om de ska bort.
