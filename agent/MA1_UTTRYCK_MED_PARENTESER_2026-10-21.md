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

## Omgång 2: 25 uppgifter till (#1.1159–1.1183)

Användaren bad om 25 uppgifter till med god variation, gärna med figur. Inga uppgifter fick ha samma värden eller likvärdiga uttryck. Delmomentet har nu 48 uppgifter.

| ID | Innehåll | Figur | Nivå/tn | Svar |
|---|---|---|---|---|
| 1.1159 | Rabatt: areamodell 3(2x+7) | ja | E/1 | 6x+21 m² |
| 1.1160 | Regelbunden sexhörning, sida 2r−3 | ja | E/1 | 12r−18 cm |
| 1.1161 | Rektangelns omkrets 2(3t−2)+2(t+5) | ja | E/2 | 8t+6 cm |
| 1.1162 | List i fyra delar, stapelmodell 3(2z−5)+7 | ja | E/2 | 6z−8 cm |
| 1.1163 | Staket mot husvägg 2(w+1)+(3w−4) | ja | E/2 | 5w−2 m |
| 1.1164 | Skylt av två rektanglar 6(p−1)+4(2p+3) | ja | E/2 | 14p+6 dm² |
| 1.1165 | Omkretsskillnad rektangel/kvadrat | ja | C/3 | 2x+2 cm |
| 1.1166 | Tre varv runt en bana 3(2(2d+15)+2d) | ja | C/3 | 18d+90 m |
| 1.1167 | Okänd sida när omkretsen är 6(x+4) | ja | C/4 | 2x+7 cm |
| 1.1168 | ½(8x+6) | – | E/2 | 4x+3 |
| 1.1169 | 0,2(15n+40) | – | E/2 | 3n+8 |
| 1.1170 | −2(3p−q+4), tre termer | – | E/2 | −6p+2q−8 |
| 1.1171 | 12−(5w−3+2w) | – | E/2 | 15−7w |
| 1.1172 | 6(x+□)=6x−30 | – | E/2 | −5 |
| 1.1173 | □(5−2n)=−15+6n | – | E/2 | −3 |
| 1.1174 | Flerval: vilket är inte lika med 6−3(x−2)? | – | E/2 | D |
| 1.1175 | Felanalys: −(6y−4)+2y | – | E/2 | A |
| 1.1176 | Värdet av 4(3−n)+3(2n−1) för n=−5 | – | E/2 | −1 |
| 1.1177 | A=5(2c+3), B=2(5c−1): konstant skillnad | – | C/3 | 17 |
| 1.1178 | Frågesport 5r−2(20−r) | – | E/2 | 7r−40 |
| 1.1179 | Rea på tröjor och byxor | – | E/2 | 5p+200 kr |
| 1.1180 | Nästlad 15−2(4−(x−3)) | – | C/3 | 2x+1 |
| 1.1181 | Bestäm C så att A+B+C=0 | – | C/3 | −5x−7 |
| 1.1182 | □(2x−□)=6x−15 | – | C/3 | 3 och 5 |
| 1.1183 | a så att 4(ax−3)−3(2x−a) inte beror på x | – | A/4 | a=1,5; −7,5 |

**Variation:**
- Nio uppgifter har figur: areamodell, sexhörning, rektangel, stapelmodell, staket mot vägg, sammansatt skylt, jämförelse av omkretsar, löparbana och omvänd omkretsuppgift.
- Variablerna är x, r, t, z, w, p, d, n, q, c och y.
- Faktorerna är heltal, ett bråk (½) och ett decimaltal (0,2). Parenteserna har två eller tre termer, och en uppgift har nästlade parenteser.

**Dubblettkontroll:**
- Skript: alla uttryck med parentes i frågetexterna jämfördes mot hela Ma1-banken, och alla facituttryck i kapitel 1 likaså. Det gav 0 träffar efter två justeringar. 1.1165 fick kvadratsidan x+2, eftersom 2x−2 och 2x−6 redan fanns som delfacit i 1.151 och 1.14. 1.1172 fick talen 6 och −30, eftersom facit −4 fanns i 1.1152.
- Testet kräver nu att inga två uppgifter i delmomentet har samma facit.

**Verifiering:**
- Numerisk ekvivalens kontrolleras i byggskriptet och i testet, som nu täcker alla 48 uppgifter.
- 57 rättningsfall i Kunskapsgymmets riktiga kod fungerar, till exempel att 3/2 och −15/2 godtas i 1.1183.
- Alla 25 kort visas på 375 px utan KaTeX-fel eller överbredd.
- Figurerna är kontrollerade med getBBox: ingen text hamnar vid kanten och inget krockar med text eller linjer. De är också granskade visuellt.
- Validatorn för Ma1 ger 0 ERROR, 17 WARNING och 181 INFO, samma som före.
- Testerna: 51 i master och 180 i Kunskapsgymmet. De 3991 tidigare objekten är oförändrade, och banken har nu 4016 objekt.
- I Kunskapsgymmet ändras utöver banken bara BANK_VERSION (`2026-10-21-ma1-parenteser-2`).
