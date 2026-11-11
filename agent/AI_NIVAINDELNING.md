# Nivåindelning av AI-uppgifter (E, C, A och träningsnivå)

Användarbeslut 2026-11-11. Gäller AI-banken (`uppgifterai.js`) och alla nya eller
omarbetade AI-uppgifter. Reglerna verkställs av `tools/bygg-ai-nivaer-2026-11-11.py`
och skyddas av `tools/ai-nivaer-2026-11-11.test.js`.

## Styrdokument

Ämnet artificiell intelligens, nivå 1 (Gy25, ARTI1000X). Betygskriterierna och
det centrala innehållet är desamma som för den äldre kursen Artificiell
intelligens 1 (ARTART01, SKOLFS 2023:136).
Två betygskriterier gäller sök- och spelavsnittet:

| | E | C | A |
|---|---|---|---|
| Kunskaper om AI, dess tillämpningar, tekniker och beståndsdelar | godtagbara | goda | mycket goda |
| Använder AI för att lösa **enkla problem** | med viss säkerhet | med säkerhet | med god säkerhet |

Tolkning:

- Problemen är ”enkla” på alla tre nivåerna. Progressionen ligger i **säkerhet**
  (rätt utan fel även i längre körningar och specialfall) och i **djup** (från att
  känna igen principen, via att förklara varför, till att värdera och generalisera).
- Sökning ingår på nivå 1 som ”översikt av tekniker … däribland sökning” och
  ”enklare … användning av spelagent”. Formuleringarna ”styrkor och svagheter …
  inom sökning” och ”algoritmer … spelagent” hör till nivå 2. Detaljerad
  algoritmspårning är därför fördjupning, och den mest krävande delen placeras på A.
- Skolverkets kommentarmaterial (Gy25) gick inte att läsa (inloggning krävdes
  2026-11-11). Komplettera tolkningen om det blir tillgängligt.

## Nivåerna

**E – känna igen principen och ta enstaka steg med given regel** (träningsnivå 1–2).
Exempel:

- köer, stackar och prioritetsköer: in, ut, nästa uttag, vad som ligger kvar;
- BFS och DFS i små labyrinter och träd: grannar, nästa uttag, k:e uttaget,
  antal steg, avstånd från start, kort kötabell, kort besöksordning;
- h för en ruta; f när g är givet eller när g följer en rak väg utan omväg;
  välja lägst h eller lägst f ur en tabell; A*:s eller girig sökningens första steg;
- kostnaden för en given väg, och billigaste väg i en liten graf eller labyrint;
- minimax: nodvärden, rotens värde, rotens drag och vägen vid bästa spel,
  även i tre nivåer och med negativa värden;
- rotens värde i ett alfa–beta-träd med högst 9 löv (vanlig minimax).

**C – genomföra en hel körning säkert och förklara varför** (träningsnivå 3).
Exempel:

- långa BFS/DFS-ordningar (cirka 10 uttag eller fler) och DFS med backning;
  påståenden om sökningens beteende (onåbart mål, grannordningens betydelse);
- g som måste gå runt väggar eller genom terräng, och därmed också f för den rutan;
- A*-spårning med regler för lika värden, antal uttag, öppna listan;
- girig bäst först jämfört med A*; förklara varför den ena hittar en billigare väg;
- förklaringar av typen ”varför läggs C bara in en gång”, ”varför når spelet inte lövet 7”;
- rotens eller en nods värde i stora alfa–beta-träd (minst 12 löv).

**A – alfa–beta-beskärning, värdering och generalisering** (träningsnivå 4–5).

- **Allt som gäller alfa–beta-beskärning är A** (användarbeslut): vilka löv eller
  grenar som beskärs, antal utvärderade löv, α och β, var den första beskärningen
  sker, varför en gren kan beskäras och hur ordningen påverkar beskärningen.
  Träningsnivå 5 för träd med minst 12 löv och när både α och β efterfrågas,
  annars 4.
- Värdera heuristiken, till exempel påståenden om att h underskattar.
- Generalisera, till exempel ”för vilka x byter roten drag”.

## Regler för metadata

- Bedöm **varje delkort för sig**. Ett kort som ger ett mellanresultat, till
  exempel ”g för P är 7”, kan vara E även om hela uppgiften är C.
- `niva` och `poang` per delkort: E = `1/0/0`, C = `0/1/0`, A = `0/0/1`.
- `traningsniva`: E = 1 eller 2, C = 3, A = 4 eller 5. Nivå 1 är ett enda steg
  med en tydlig regel, och nivå 2 är några beroende steg eller en liten tabell.
- Huvuduppgiften får den högsta delnivån, summerade poäng och den högsta träningsnivån.
- **Många E-uppgifter** (användarbeslut). Sikta på minst 55–60 % E bland
  delkorten i banken, och på E i de flesta kort om köer, stackar, BFS, DFS,
  prioritetsköer och minimax. När ett område får för få E-kort, fyll på med
  korta E-uppgifter i stället för att sänka nivån på C- och A-kort.
- Avgör nivån utifrån vad eleven faktiskt måste göra, inte utifrån
  rättningsformatet. Ett flervalskort om beskärning är fortfarande A.
- Nya undantag läggs in i `OVERRIDE` i nivåskriptet, med en kort motivering per delkort.

## Fördelning efter omklassningen 2026-11-11

132 uppgifter och 358 delkort: 245 E (68 %), 67 C (19 %) och 46 A (13 %).
80 delkort bytte nivå. Bland annat blev alfa–beta-beskärningen A, f med g runt
väggar (2.01c, 2.08) C, och minimaxträden E utom resonemangsfrågan 3.12c (C)
och generaliseringen 3.07c (A). Sju nya E-uppgifter lades till (2.47–2.53) i de
områden som hade fått mest C: A*-sökning, g/h/f och viktade vägar.

Byggordning: `bygg-ai-pafyllnad-2026-11-11.py` → `…pafyllnad2…` → `…pafyllnad3…` →
`bygg-ai-kunskapsgymmet-2026-11-11.py` → `bygg-ai-e-uppgifter-2026-11-11.py` →
`bygg-ai-pafyllnad4-2026-11-11.py` → `bygg-ai-pafyllnad5-2026-11-11.py` → `bygg-ai-pafyllnad6-2026-11-11.py` → `bygg-ai-sjalvrattning-2026-11-11.py` → `bygg-ai-pafyllnad7-2026-11-11.py` → `bygg-ai-pafyllnad8-2026-11-11.py` → `bygg-ai-omgruppering-2026-11-11.py` → `bygg-ai-nivaer-2026-11-11.py`. Nya byggskript läggs in före nivåskriptet. Kedjan ger en identisk fil från den committade versionen.

Tillägg 2026-11-11 (teorifrågor): att känna igen ett begrepp, till exempel
”vilken datastruktur använder BFS”, är E. Att förklara varför är C, till exempel
”varför väljer MAX inte det högsta lövet” eller ”varför är h mindre än det
verkliga avståndet”. Att värdera en heuristik, till exempel ”h får aldrig
överskatta”, är A. Minimaxfrågor om vad rotvärdet garanterar är C.

Tillägg 2026-11-11 (beskärning på E–C-nivå, användarbeslut): fullständig
alfa–beta-spårning är fortfarande A. Det gäller att själv följa α och β, att hitta
alla beskärningar, djupa beskärningar och α/β-värden. **Beskärning med stöd är C**:
träd i två nivåer, ett givet mellanvärde (till exempel ”A har värdet 5, B:s första löv
är 3”) och ett enda beslut (”kan B bli större än 3?”, ”vilket löv kan hoppas över?”,
”hur påverkar ordningen?”). **Begreppsfrågor om vad beskärning är** (”ändrar beskärning
rotens värde?”) är E. De äldre beskärningsuppgifterna 3.03–3.42 är oförändrat A.
Gäller 3.56–3.61. Minimaxfrågor där eleven tolkar eller jämför värden, till exempel
vad rotvärdet −1 betyder eller två drag med samma värde, är C.
