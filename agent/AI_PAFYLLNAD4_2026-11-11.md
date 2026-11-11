# AI: 30 nya självrättande uppgifter, mest E-nivå, 11 november 2026

Fortsatt påfyllnad mot målet 50–100 kort på träningsnivå 1–2 per område.
Uppgifterna följer Kunskapsgymmets format (tal eller ett rätt alternativ per
del, se AI_KUNSKAPSGYMMET_2026-11-11.md) och nivåindelningen i
AI_NIVAINDELNING.md. A*-sökning hade minst E-kort och fick flest nya uppgifter.

## Nya uppgifter

| Område | ID | Innehåll |
|---|---|---|
| Kö och stack | 1.44, 1.45 | Ångra-knappen som stack; skrivarkö |
| Kön under sökningen | 1.46–1.48 | BFS-kö efter två uttag; stacken när målet hittas; robotens kö i ett lager |
| BFS | 1.49–1.51 | Robotens sökning; BFS med flera vägar; mål i en ficka |
| DFS | 1.52–1.54 | DFS genom smal gång (kortaste: ja); lång omväg (kortaste: nej); höger gren först |
| A*-sökning | 2.54–2.58 | Tredje uttaget; lägst f bland grannar; girig två steg; öppna listan; två rutor med givet g |
| g, h och f | 2.59–2.61 | h och f med givet g; närmast målet enligt h; g runt lång vägg (C) |
| Viktade vägar | 2.62–2.64 | Tre vägar i graf; två vägar runt is; den billiga omvägen (C) |
| Prioritetsköer | 2.65, 2.66 | Akutmottagning; andra uttaget ur A*:s kö |
| Minimax | 3.37–3.39 | Nodvärde, rotvärde och drag; lövet där spelet slutar |
| Alfa–beta | 3.40–3.42 | Rotvärde (E/C) och beskärning (A): antal exakta barn, sista lövet, α före sista barnet |

Nya sammanhang: robot i lager, ångra-knapp, skrivarkö och akutmottagning.
Nya frågeformer: vilka rutor som ligger i öppna listan, vilket löv spelet slutar
i, hur många av rotens barn som får exakt värde och vilket löv som utvärderas sist.

Lika värden: där lika h kan uppstå (2.56) anges regeln i uppgiften. Övriga
designer valdes så att lägsta f eller h är entydigt.

Alternativkommentarerna är utbyggda i hela banken. Inga kommentarer på 15 tecken
eller färre finns kvar, och varje kommentar säger varför alternativet är rätt
eller fel.

## Fördelning efter omgången

162 uppgifter, 431 delkort: 303 E (70 %), 76 C och 52 A. Kort på träningsnivå 1–2
per område: köer och stackar 27, kön under sökningen 29, BFS 35, DFS 34,
prioritetsköer 31, g/h/f 26, A*-sökning 25, viktade vägar 31, minimax 47 och
alfa–beta 18 (där är de flesta korten A-nivå enligt beslut).

## Kontroll

- Byggskript: `tools/bygg-ai-pafyllnad4-2026-11-11.py`. Det körs efter
  `bygg-ai-e-uppgifter-2026-11-11.py` och före `bygg-ai-nivaer-2026-11-11.py`.
  Hela kedjan med sju skript ger en identisk fil.
- Test: `tools/ai-pafyllnad4-2026-11-11.test.js` räknar om alla svar i
  JavaScript. 75/75 AI-tester godkända. Validatorn hittar inga nya fynd.
- Webbläsarprov med appens CSS. Facit och ledtrådar har lästs igenom. Granskningen är gjord.
