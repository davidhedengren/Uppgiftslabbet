# Fy2 kap 5: HR-diagram, magnituder och parallax – 2026-10-23

Läraren bad om ”bra uppgifter om HR-diagram och avståndsmätning”, fokuserade på det som ingår i kursen:

- bestämma absolut magnitud ur HR-diagram;
- tolka diagram;
- parallax och luminositet.

Variation var viktig, och HR-diagrammen skulle se professionella ut, med verkliga stjärnor utprickade.

## Nya kort 5.400–5.446 (47 st)

| Område | Före (nivå 1) | Efter (nivå 1) | Innehåll |
|---|---|---|---|
| farg_ljusstyrka (HR-diagram) | 0 | 17 | läsa M, T och L ur diagram; varmast, vit dvärg, störst och minst radie, spektralklass, färg, typ av stjärna; luminositetsförhållande; M för en huvudseriestjärna ur bandet; namngivna stjärnor (Sirius B, Rigel, Betelgeuse, Aldebaran, Sirius A och B, Proxima) |
| magnituder | 2 | 8 | ljusast på himlen (tabell), M på 10 pc, 5 mag = ×100, avståndsmodul, vilken ligger längst bort, blotta ögat; nivå 2–3: M och m ur avstånd, L jämfört med solen, avstånd med HR-diagram plus apparent magnitud |
| avstandsmatning | 9 | 17 | avstånd och parallax, vilken vinkel som är parallaxen (figur), halverad parallax, parsec till ljusår, Gaia i millibågsekunder, ljusets gångtid, avståndskvadratlagen; nivå 2: förskjutning mellan januari och juli (halva skiftet), parsec i AE, varför galaxer kräver andra metoder |
| stjarnornas_utveckling | 4 | 8 | Wiens lag, pil mot röd jätte, solens slutstadium, kortast livslängd, radie ur L och T |

### HR-diagrammen

- **Bakgrund:** mörk bakgrund, temperaturaxel med logaritmisk skala (varmast till vänster) och spektralklasserna O B A F G K M i färgband.
- **Axlar:** absolut magnitud med en rutlinje per magnitud, eller luminositet i \(L_\odot\) med en rutlinje per tiopotens.
- **Verkliga stjärnor:** omkring 80 verkliga stjärnor är utprickade med ungefärliga katalogvärden för yttemperatur och absolut magnitud. Där ingår närbelägna röda dvärgar, solliknande stjärnor, A-stjärnor, jättar, superjättar och vita dvärgar. Prickarna är färgade efter temperatur, och en bildtext talar om att de är verkliga stjärnor.
- **Etiketter:** områdesetiketterna (huvudserien, jättar, superjättar, vita dvärgar) och stjärnnamnen har vit bakgrund.
- **Uppgiftsstjärnor:** stjärnorna A–F är fiktiva och placerade på rutlinjer, så att avläsningen blir entydig.

### Fysikregler

- Inga formler eller konstanter står i frågorna. Svarsinstruktionen står i parentes.
- Avläsningar ur diagram rättas med tolerans. Beräkningar använder värdesiffror.
- Solens absoluta magnitud är 4,74, som i bankens övriga kort.

## Kunskapsgymmet

Enhetstabellen har nu parsec, ljusår och AE, med prefix som kpc. Därmed godtas till exempel ”1 kpc” och ”3 300 ljusår” för 1 000 pc. Testet är `tools/astronomiska-enheter-2026-10-23.test.js`. Rättningen är prövad med 61 svar i webbläsaren.

## Verifiering

- **Validator:** inga nya fynd.
- **SVG-granskning:** 0 fynd för 5.400–5.446.
- **Test:** `tools/fy2-astronomi-hr-parallax-2026-10-23.test.js` räknar om facit och kontrollerar radieordningen med Stefan–Boltzmanns lag, både för bokstavsstjärnorna och de verkliga stjärnorna. Det kontrollerar också att inga formler står i frågorna.

## Omgång 2: äldre kort görs om och kombinationsuppgifter läggs till

### Äldre kort (56 ändrade)

- **Automatisk rättning:** 25 självrättade kort rättas nu automatiskt, med tal, ordsvar eller flerval. Uppdelade kort fick fält per delkort, där resonemangsdelar blev flerval enligt mönstret i Fy1 8.11. Exempel:
  - 5.28: tabellen med åtta tomma rutor;
  - 5.43: rangordningen blev flerval;
  - 5.53: cepheiden svaras i Mpc och km/s;
  - 5.23: parallaxen om 100 år räknas om exakt;
  - 5.54: dubbelstjärnan har två luminositeter, två våglängder och flerval.
- **Träningsnivå:** 42 kort saknade nivå och fick en.
- **Formler ur frågorna:** formler som inte påverkar svaret är borttagna, till exempel ”Absolut magnitud: M = m + 5 − 5 lg r”, Wiens och Stefan–Boltzmanns lagar och Wiens konstant. Formeln P = P☉·10^(−0,4M + 1,932) är kvar i 5.356–5.368. Den bygger på M☉ = 4,83 i stället för 4,74, och att ta bort den skulle ändra facit.
- **Svarsinstruktioner** finns nu i 5.349–5.355 och 5.385. Delkortens mellanresultat (”Avståndet är 3,63 pc.”) ligger nu i egna stycken.
- **Facit:** irrelevant text om kärnreaktioner är borttagen i 5.8, 5.315 och 6.51.

### Nya kort 5.447–5.463 (17 st, nivå 1–5)

- **Kedjor på nivå 4–5:**
  - Arcturus: parallax → d → M → L → R;
  - Wiens lag och L → R;
  - vit dvärg: parallax och m → M → L → R;
  - hela kedjan från strålningsmaximum, parallax och m;
  - huvudseriepassning: ett diagram över en stjärnhop med apparent magnitud jämfört med standardhuvudserien.
- **Nivå 2–3:**
  - luminositet ur flöde;
  - solens intensitet vid Mars, med skalenlig figur;
  - radie ur ett avläst HR-diagram;
  - samma L med olika T;
  - radiekvot i en hop;
  - luminositetskvot i en dubbelstjärna;
  - Sirius jämfört med Polstjärnan;
  - Sirius på 10 pc;
  - absolut magnitud ur L;
  - den kosmiska avståndsstegen;
  - vilken stjärna har störst luminositet (tabell).
- **Tolerans:** svar som beror på solens värden har en tolerans som även godtar M☉ = 4,83 och T☉ = 5 778 K. Det kontrolleras i testet.

### Kunskapsgymmet

- Bågsekunder (″, ”bågsekunder”) och bågminuter (′) är nu enheter.
- ”Lika långt” och ”samma avstånd” godtas som ordsvaret ”lika”.
- Rättningen är prövad med 59 svar.

**Verifiering:**
- Testet `tools/fy2-astronomi-omgjorda-2026-10-23.test.js` kontrollerar att inga självrättade kort finns kvar, att inga formler står i frågorna och att facit stämmer.
- Validatorn ger inga nya fynd och SVG-granskningen 0 fynd.

**Lärdom:** en annan session pushade `uppgifter2.js` medan arbetet pågick. Eftersom alla ändringar var skriptade kunde de köras om på den nya versionen.
