# AI: övningsblad – enklare tabeller, granskning och 24 nya uppgifter, 11 november 2026

## Användarens önskemål

1. Granska uppgifterna för gymnasiekursen AI 1.
2. Fyll på med liknande uppgifter för övningsblad, gärna spelträd i olika
   svårighetsgrad där man bestämmer rotens värde och vilka grenar som kan beskäras.
3. Tabellerna är svåra att fylla i när det står ”…”/”–”. Gör dem enklare.

## Granskning för AI 1

Banken täcker sök- och spelavsnittet väl: köer och stackar, BFS, DFS, girig bäst
först och A* (med g, h och f), kostnader i terräng och grafer samt minimax och
alfa–beta. Uppgifterna har figurer, korta frågor, nivåer från 1 till 4 och
stegvisa facit. Följande har rättats:

- **Tvetydigt ”besöks”.** I BFS och A* betyder ett besök att rutan tas ut ur
  kön (öppna listan), men de äldsta uppgifterna sade bara ”besöks”. 1.01, 1.06,
  1.08, 1.09, 2.02, 2.09, 2.17, 2.19 och 2.28 säger nu ”tas ut ur kön” eller
  ”tas ut ur öppna listan”, som de nyare uppgifterna. DFS-uppgifterna behåller
  ”besöksordning”, där ordet är entydigt.
- 2.09: ”Girig” med stor bokstav mitt i meningen är ändrat till ”girig”.

Bedömt men inte ändrat: 3.04/3.05 c (ange α och β vid varje beskärning) och
2.03 ligger på nivå 4. De passar som utmaning men är inte nödvändiga för grundnivån.

## Tabeller

Celler som eleven ska fylla i var markerade med ”…”, och startraden med ”–”.
Nu är cellerna tomma och rymliga (`min-width:7em; height:2.6em`), så att en
hel kö får plats, och startraden heter **Från början** i alla tabeller med
kolumnen ”Tas ut”. Ändringen görs centralt i
`tools/bygg-ai-pafyllnad3-2026-11-11.py` (`enkla_tabeller`) och gäller alla
uppgifter, även facit.

## Nya uppgifter (24 st)

### Rotvärde och beskärning (alfa–beta), 12 träd

Samma två huvudfrågor i alla, så att de fungerar på ett övningsblad: a) rotens
värde, b) vilka grenar som kan beskäras (löven som aldrig behöver utvärderas).
Den tredje frågan varierar.

| Nivå | ID | Träd | Rot | Beskurna löv | Tredje frågan |
|---|---|---|---:|---|---|
| Lätt | 3.15 | MAX, 2 × 2 | 3 | L4 | drag |
| | 3.16 | MAX, 3 × 2 | 7 | L6 | antal utvärderade löv |
| | 3.17 | MIN, 2 + 3 | 6 | L4, L5 | β i roten före B |
| | 3.18 | MIN, 3 + 2 + 2 | 4 | L7 | värdet i B |
| Medel | 3.19 | MAX, 3 × 3 | 6 | L5, L6, L9 | första beskärningen |
| | 3.20 | MIN, 3 × 3 | 5 | L5, L6, L8, L9 | löv som sparas |
| | 3.21 | MAX, tre nivåer, 8 löv | 7 | L4; grenen till F | varför hela grenen (flerval) |
| | 3.22 | MIN, tre nivåer, negativa värden | −1 | L4; grenen till F | α och β i D |
| Svår | 3.23 | MAX, 12 löv | 6 | L4; grenen till G; L12 | exakta värden och gränser |
| | 3.24 | MIN, 12 löv | 10 | L4; grenarna till G och H | alla beskärningar med α, β |
| | 3.25 | MAX, 14 löv, negativa värden | 4 | grenarna till G och I | α i roten före C |
| | 3.26 | MIN, 14 löv | 3 | L4; grenen till G | värdet i C |

Facit för a) går gren för gren under roten: varje nod får antingen ett exakt
värde eller en gräns (”högst 3”/”minst 9”). Facit för b) förklarar varje
beskärning med α och β i noden där den sker och vem ovanför som aldrig väljer
noden. Lätta träd saknar beskärningar där α = β. 3.26:s drag är inte entydigt
(A och C ger båda 3), så där frågas i stället efter värdet i C.

### Minimax, 4 träd (familjen ”Minimax – träd att lösa”)

3.27 (MIN i roten, 6 löv), 3.28 (MAX, tre nivåer, negativa värden, vägen vid
bästa spel), 3.29 (MIN, tre nivåer, 12 löv) och 3.30 (ojämnt träd med löv på
olika djup, vägen vid bästa spel).

### Övriga områden

| ID | Område | Innehåll |
|---|---|---|
| 1.28 | Kö och stack | Stacken i en tabell; ut B, E, D |
| 1.29 | Kön under sökningen | DFS med stack i ett träd; 8 uttag |
| 1.30 | BFS | 4 × 5, väg med 7 steg; D4 läggs aldrig in |
| 1.31 | DFS | DFS hittar en kortaste väg (7 steg), återvändsgränd A4 |
| 2.31 | Prioritetsköer | Händelserna i en tabell; ut B, D, E |
| 2.32 | g, h och f | Tabell för P, Q, R; R har lägst h men högst f |
| 2.33 | A*-sökning | A* i tabell, alla f = 4; A4 utanför vägen |
| 2.34 | Viktade vägar | Kort väg (9) eller billig väg (8 steg, 8) |

Banken har nu 95 uppgifter: 6–7 i varje område utom alfa–beta (19) och
minimax (11).

## Kontroll

- `tools/ai_speltrad.py`: namngivning, minimax, alfa–beta med anteckningar per
  nod och beskrivning av beskurna grenar. Kontrollerad mot tidigare verifierade
  träd (3.04, 3.09, 3.13).
- `tools/bygg-ai-pafyllnad3-2026-11-11.py`: körs efter de två tidigare
  byggskripten. Hela kedjan ger en identisk fil från den committade versionen.
- `tools/ai-pafyllnad3-2026-11-11.test.js`: egen alfa–beta och minimax i
  JavaScript för alla 16 träd, en kontroll av att figurernas lövvärden är
  samma som de träd som räknas, BFS/DFS/A* för labyrinterna samt tabell- och
  ordvalsreglerna.
- Resultat: 57/57 tester godkända. Validatorn hittar inga nya fynd.
- Webbläsarprov med appens CSS: tabeller, lätta, medelsvåra och svåra träd,
  minimaxträd och övriga nya uppgifter med facit. Inga JS-fel och inget
  horisontellt överflöd. Facit och ledtrådar har lästs igenom. Granskningen är gjord.
