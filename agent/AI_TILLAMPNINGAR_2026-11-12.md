# AI-banken: C-uppgifter med AI-tillämpningar (2026-11-12)

Användaren ville ha fler C-uppgifter med verklighetsförankring, kopplade till AI-tillämpningar i
stället för abstrakta träd. Tio förslag godkändes (”kör”), och alla tio ligger nu i Uppgiftslabbet
och i Kunskapsgymmet (`tools/bygg-ai-tillampningar-2026-11-12.py`).

| Uppgift | Tillämpning | Område | Det eleven gör |
|---|---|---|---|
| 1.107 | Vänner i flera led i ett socialt nätverk | BFS | vänners vänner, kortaste kedjan, BFS-kedjan, varför BFS ger kortast |
| 1.108 | Räddningsrobot i ett rasat hus | DFS (BFS jämfört med DFS) | vilket rum BFS och DFS hittar först, och vilken sökning som passar |
| 2.117 | Navigeringsapp i en stad | A* | f med lika värden, hela uttagsordningen med uppdaterat f, varför inte den raka gatan |
| 2.118 | Plockrobot i ett lager | A* | uttag med BFS (27) och A* (11), varför A* sparar tid och batteri |
| 2.119 | Leveransdrönare och flygförbudszoner | g, h och f | g runt zonen (8) mot h (3), skillnaden mellan g och h |
| 2.120 | Reseplanerare i kollektivtrafiken | viktade vägar | girig bäst först (21 min) mot A* (12 min), varför väntan vid bytet missas |
| 2.121 | Åttapusslet | heuristiken h | h = brickor på fel plats för fem lägen, A*:s val, varför h inte överskattar |
| 2.122 | Triage på en akutmottagning | prioritetskö | behandlingsordning, väntetid 58 min, svält och en bättre regel (A) |
| 3.79 | Luffarschack | minimax | nodvärde, datorns drag och varför den blockerar i stället för att försöka vinna |
| 3.80 | Schackdator med tidsgräns | alfa–beta | stödfrågor om beskärning, antal bedömningar i två ordningar, varför slagdrag först |

- **Papper och Kunskapsgymmet:** förklaringsfrågorna (”Varför …?”) är öppna frågor i
  uppgiftstexten och huvudfacit. I Kunskapsgymmet är de flerval, och varje felaktigt alternativ är
  ett vanligt missförstånd med en kommentar. Alla uppgifter går att rätta automatiskt.
- **Nivåer:** varje uppgift har minst ett C-delkort. 2.122d (föreslå en regel mot svält) och 3.80d
  (alfa–beta i en ny ordning) är A.
- **Figurer:** egna SVG-figurer för spelplanen i luffarschack och åttapusslets brädor (två rader
  för mobil). Kartor och nätverk ritas med de befintliga graffigurerna, och triage som tabell.
- **Granskning:** facit, ledtrådar och figurer har lästs igenom i 390 px. Nodnamnen i
  luffarschackets spelträd fick mer luft, och svarsraden i 2.121b anger läge för varje h.
- **Test:** `tools/ai-tillampningar-2026-11-12.test.js` räknar om alla svar med egen kod (BFS, A*,
  girig bäst först, h och verkligt antal drag i åttapusslet, triagesimulering, luffarschack och
  alfa–beta). Testet kontrollerar också att förklaringsfrågorna saknar alternativ på papper.
- Kunskapsgymmet: 868 delkort, 2 659 rättningskontroller, inga fel.
