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
