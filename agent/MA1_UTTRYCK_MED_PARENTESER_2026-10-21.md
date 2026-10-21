# Ma1: delmomentet Uttryck med parenteser – 2026-10-21

Användaren ville ha ett nytt delmoment i Ma1, under **Skriva och förenkla uttryck** (`forenkla_uttryck`). Där ska eleverna träna på att multiplicera in positiva och negativa tal i parenteser och hantera minustecken framför parenteser. Delmomentet ska ha korrekt taggade uppgifter med god variation.

Det nya delmomentet (`familj`) heter **Uttryck med parenteser**. Det har **23 nya uppgifter, #1.1136–1.1158**, för Ma1a, 1b och 1c. Uppgifterna ger 24 kort, eftersom #1.1156 delas i a/b. Kunskapsgymmet har också fått en genomgång, `ma1-grund-1-02p`, ”Förenkla uttryck med parenteser”, med träningsknapp till delmomentet.

Området hade tidigare två delmoment: Förenkla uttryck (29) och Uttryck i resonemang och problem (26). Delmomentet *Multiplicera in i en parentes* finns redan under `multiplicera_uttryck` (Multiplikation av uttryck) och är oförändrat. Det nya delmomentet har en egen progression med kombinationer av flera parenteser, felanalys, sammanhang, figur och okända koefficienter. De enklaste korten liknar ändå några befintliga uppgifter i det delmomentet, till exempel 1.410 och 1.1039.

## Progression

| ID | Uppgift | Nivå/träningsnivå | Svar |
|---|---|---|---|
| 1.1136 | \(4(x+5)\), areamodell i facit | E/1 | \(4x+20\) |
| 1.1137 | \(6(a-2)\) | E/1 | \(6a-12\) |
| 1.1138 | \(3x+(2x-7)\), plustecken framför | E/1 | \(5x-7\) |
| 1.1139 | \(5(1-2x)\) | E/1 | \(5-10x\) |
| 1.1140 | \(-(4-3m)\) | E/2 | \(3m-4\) |
| 1.1141 | \(-3(x+4)\) | E/2 | \(-3x-12\) |
| 1.1142 | \(-5(2a-3)\), minus gånger minus | E/2 | \(-10a+15\) |
| 1.1143 | \(10-(4-x)\) | E/2 | \(x+6\) |
| 1.1144 | \(3(2x-1)+4\) | E/2 | \(6x+1\) |
| 1.1145 | \(5y-2(y-6)\) | E/2 | \(3y+12\) |
| 1.1146 | \(2(x+3)-(x-5)\) | E/2 | \(x+11\) |
| 1.1147 | \(-(3x-2)-(x+4)\) | E/2 | \(-4x-2\) |
| 1.1148 | \(4(a+2b)-3(a-b)\), två variabler | E/2 | \(a+11b\) |
| 1.1149 | \(-2(x-1)-3(1-x)\) | E/2 | \(x-1\) |
| 1.1150 | Flerval: vilket uttryck är lika med \(-2(x-3)\)? | E/2 | C |
| 1.1151 | Felanalys: \(7-2(x-3)\) | E/2 | B |
| 1.1152 | Bestäm \(a\): \(a(2x-3)=-8x+12\) | E/2 | \(-4\) |
| 1.1153 | Konsertbiljetter, växel \(500-3(x+15)\) | E/2 | \(455-3x\) kr |
| 1.1154 | Figur: rektangel med bortklippt hörn | E/2 | \(3x+17\) cm² |
| 1.1155 | Nästlad parentes \(2(3x-(x+4))\) | C/3 | \(4x-8\) |
| 1.1156 | \(3(x+4)-2(x+6)\) a) förenkla b) värdet för \(x=2026\) | C (a E/2, b C/3) | \(x\); 2026 |
| 1.1157 | Saknat tal: \(4(x+3)-\square(x-2)=x+18\) | C/3 | 3 |
| 1.1158 | Bestäm \(a,b\): \(a(x+2)-b(x-1)=5x+4\) | A/5 | \(a=3\), \(b=-2\) |

Nivå 1 innehåller bara en positiv faktor eller ett plustecken framför parentesen. Nivå 2 tillkommer när ett tecken måste bytas, när faktorn är negativ eller när två parenteser kombineras. Fler rutinsteg har inte ensamma fått höja E till C (se INNEHALLSREGLER 3.10). C används när eleven måste välja ordning i nästlade parenteser, se att förenklingen gör en beräkning onödig eller bestämma en okänd faktor genom att jämföra koefficienter. A-uppgiften kräver en egen strategi, till exempel att välja \(x\)-värden som nollställer en parentes.

## Verktyg, svar och figurer

- **Miniräknare:** `miniräknare:false` och `geogebra:false` på alla uppgifter och kort. Motivering: det som tränas är teckenreglerna vid multiplikation, till exempel \((-5)\cdot(-3)\). Räknaren skulle ta över just den delen, och övriga tal är små. Det avviker från de flesta äldre uppgifter i området, som har räknare tillåten. Avvikelsen är medveten och följer regel 3 i PEDAGOGISKA_REGLER, ”Verktygsval i varje granskning”.
- **Svarsformat:** `förenklat_polynom` på alla förenklingar. Termerna får stå i valfri ordning och skrivas med unicode-minus eller ”·”. Svar som behåller en parentes eller har osamlade termer underkänns. 1.1153 och 1.1154 godtar enhet (kr respektive cm²). 1.1158 har två ordnade fält, a och b.
- **Flervalsfrågor:** 1.1150 och 1.1151 följer mönstret i 1.213, med svarstyp `val` och alternativ ”A: …”.
- **Figurer:** 1.1136 har en areamodell i facit. 1.1154 har en måttsatt figur i uppgiften som är skalenlig för \(x=7\) (30 px/cm). De rent symboliska förenklingarna har ingen figur, eftersom en figur inte tillför något för teckenhanteringen. Areamodellen visar idén en gång.

## Verifiering

- Numerisk ekvivalens mellan frågans uttryck och facit för slumpade värden, både i byggskriptet och i nytt test `tools/ma1-uttryck-med-parenteser.test.js` (4 tester). Testet kontrollerar också metadata, verktyg, nivåspridning, flerval, okända koefficienter och figurens mått.
- Master: 51 ma1-, deluppgifts- och validatortester passerar. Kunskapsgymmet: 180 tester passerar.
- Bankvalidator Ma1: 0 ERROR, 17 WARNING och 181 INFO, både före och efter. Inga fynd gäller de nya ID:na.
- Kunskapsgymmets riktiga rättning: 55 fall via `delSvarRatt`. Rätt svar i valfri termordning, med unicode-minus, ”·” och enhet godkänns. Teckenfel, ofullständig multiplikation, kvarvarande parentes, osamlade termer och omkastade a/b underkänns. Flervalens alternativ läses korrekt av `valAlternativ`.
- Kort på 375 px: alla 24 kort med visat facit har inga KaTeX-fel och ingen överbredd. Korten syns i 1a, 1b och 1c (24 vardera) och räknarknappen är inaktiv. Genomgången kopplas till delmomentet på kortet `forenkla_uttryck`.
- SVG: båda figurerna kontrollerade med getBBox. Ingen text hamnar utanför eller krockar med text eller måttlinjer. Figurerna är också granskade visuellt.
- Strukturerad jämförelse: de 3968 tidigare Ma1-objekten är oförändrade, och banken har nu 3991 objekt med unika ID:n. Bankkopiorna är identiska. I Kunskapsgymmet ändras utöver banken bara `typuppgifter-ma1.js` (en ny genomgång) och `BANK_VERSION` (`2026-10-21-ma1-parenteser`).
