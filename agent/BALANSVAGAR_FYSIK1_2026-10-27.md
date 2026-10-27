# Fy1 kap 4 moment: balansvågar (Albert och Isaac), 2026-10-27

Användaren bad om uppgifter i stil med en lärares provfråga: ”förklara varför
Isaacs våg fungerar bättre än Alberts”. Frågan prövar förståelse av vridmoment.
Den ska ha hög nivå och figurer och prövas från flera håll: välja våg, förklara
och räkna. Självrättningen bygger på alternativ vars kommentarer tar upp vanliga
fallgropar.

## Modell

Bommen är lätt, och skålarna hänger fritt i bommens ändar på avståndet L från
bommens mitt. Vridpunkten P sitter avståndet h ovanför bommens mitt, och staven
mellan dem är vinkelrät mot bommen. När bommen lutar vinkeln θ är momentarmarna

- höger: L cos θ − h sin θ
- vänster: L cos θ + h sin θ

om höger sida är nedåt. Jämvikten ger tan θ = (m_H − m_V)·L / ((m_H + m_V)·h).

- h > 0 (Isaac): den sänkta sidan får kortare arm. Bommen stannar vid en
  lutning som visar vilken sida som är tyngst.
- h = 0 (Albert): armarna är lika långa i alla lägen. Vid olika massor tippar
  bommen till lodrätt läge, och vid lika massor blir den kvar i varje läge.
- h < 0: jämvikten är instabil.

## Kort

| ID | Typ | Nivå | Prövar |
|---|---|---|---|
| 4.902 | flerval | 2 | Vilken skål är tyngst hos Isaacs våg i stilla läge |
| 4.903 | flerval | 3 | Vilken våg som kan jämföra två föremål, och varför |
| 4.904 | flerval | 3 | Albert, 50 g mot 51 g: bommen tippar till lodrätt |
| 4.905 | flerval | 4 | Albert, lika massor, bommen lutar 20°: den blir kvar |
| 4.906 | flerval | 5 | Vridpunkt ovanför, i och under bommen: stabil, indifferent, instabil |
| 4.907 | resonemang | 5 | Lärarens fråga: förklara Albert mot Isaac (Idé/Verklighet-figur), manuell rättning |
| 4.908 | deluppgifter | 4, 4, 5 | Momentarmar 14,25 och 15,29 cm vid 10°, och massan 107 g |
| 4.909 | flerval | 5 | Hur vågen blir känsligare: minska h, men inte till noll |

Alla kort har en egen SVG-figur. Bommen är blå, vridpunkten är en blå prick och
massorna är orangea. I 4.906 visas vågarna i bredd, i 4.907 har raderna
etiketterna Idé/Verklighet, och 4.908 är ritad i skala. Figurerna har
kontrollerats för överlapp.

## Självrättning för 4.908

Appen godtar n − 2 till n + 2 värdesiffror vid korrekt avrundning. Med
`svarVardesiffror` 3 godtogs 100 g i del c (107 avrundat till en värdesiffra),
och det är just felsvaret ”lika massor”. Därför är `svarVardesiffror` 4 på alla
tre delarna, i linje med de givna mellanresultaten 15,29 och 14,25. Kontrollen
i webbläsaren gav följande:

- Del a: 14,25, 14,3 och 14 godtas. 15, 15,00 och 14,77 (glömd stav) underkänns.
- Del b: 15,29 och 15,3 godtas. 14,25 underkänns.
- Del c: 107, 107,3 och 110 godtas. 100, 100,0 och 93,2 (omvänd kvot) underkänns.

Känd begränsning: i del b godtas 15, eftersom 15,29 avrundat till två
värdesiffror blir 15. Felsvaret L = 15 cm fångas redan i del a och del c.

Delkorten visar `spelIntro` med figur och sedan sin fråga (`fraga`). Del c
anger momentarmarna, så kortet går att lösa utan a och b.

## Tester

- `tools/fy1-balansvagar-2026-10-27.test.js`: figurer, kommentarer, ett rätt
  alternativ per flervalskort, rätt alternativ mot momentmodellen och en
  oberoende beräkning av 4.908 (bland annat att viloläget för 107,3 g blir 10°).
- `tools/fysik1-moment.test.js`: 48 numeriska momentuppgifter (tidigare 47) och
  83 kontrollerade slutsvar (tidigare 80).
