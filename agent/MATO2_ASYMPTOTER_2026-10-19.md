# Mato2: asymptoter, extrempunkter och ledtrådar, 2026-10-19

Sex uppgifter granskade och förbättrade: **2.14, 2.264, 2.267, 2.103,
2.486 och 2.488**. Granskad – inget fel: inga helt oförändrade uppgifter i
omgången. De tre sistnämndas matematiska facit var korrekta; ändringarna där
gäller ledtråd/svarsinstruktion. Tidigare rättningar FP64–67 bevaras.

## Åtgärder och färdiga kommentarsförslag

| ID | Kommentar |
|---|---|
| 2.14 | Åtgärdad: lösningen förklarar teckenbytet, maximipunkten och båda gränsbeteendena. En egen graf visar hur skissen ska se ut. Skiss och resonemang är fortsatt lärarbedömda. |
| 2.264 | Åtgärdad: asymptoter och extrempunkter har tydligt märkta svarsfält och självrättning. Lösningen förklarar teckenbytena och varför reella nollställen saknas. En graf är tillagd i b-lösningen. |
| 2.267 | Åtgärdad: självrättning är tillagd för asymptoter och extrempunkter. b-kortet visar omskrivningen av funktionen utan att förutsätta a-lösningen. Maximi- och minimipunkt förklaras med derivatans tecken. |
| 2.103 | Åtgärdad: den generiska ledtråden om polynomdivision är ersatt med en ledtråd om ln 1, gränsen vid 0 och derivatans tecken. Facit var korrekt och bevaras. |
| 2.486 | Åtgärdad: frågan säger nu att svaret ska vara uppåt eller nedåt. Ledtråden handlar om andraderivatan. Det korrekta svaret nedåt är oförändrat. |
| 2.488 | Åtgärdad: ledtråden pekar nu på produktregeln, teckenbytet och funktionsvärdet. Det korrekta exakta svaret 1/e är oförändrat. |

## Oberoende matematisk kontroll

- 2.14: f′(x)=1/x−1/2. Den är positiv på (0,2) och negativ på (2,∞).
  Maximum är (2,ln2−1). Både gränsvärdet vid 0 från höger och vid ∞ är −∞.
  Maxvärdet är negativt, så hela grafen ligger under x-axeln.
- 2.264: f′(x)=2−4/(x+1)² ger x=−1±√2. Vid vänstra roten byter
  derivatan plus→minus, vid högra minus→plus. y-värdena är −3±4√2.
  Asymptoter: x=−1, y=2x−1. Nollställen skulle kräva 2x²+x+3=0,
  vars diskriminant −23 är negativ.
- 2.267: x²+1=(x−2)(x+2)+5 ger f=x+2+5/(x−2). Asymptoterna är
  x=2 och y=x+2. f′=1−5/(x−2)² ger x=2±√5 och y=4±2√5.
  Vänster punkt är lokalt maximum, höger lokalt minimum.
- 2.103: (1,0), lodrät asymptot x=0, växande eftersom 1/x>0.
- 2.486: f″=−1/x²<0 på x>0, alltså konkav nedåt.
- 2.488: f′=e^(−x)(1−x) byter plus→minus vid 1. f(0)=0 och
  gränsvärdet vid ∞ är 0, så globalt maxvärde är f(1)=1/e.

## Kort, nivå, verktyg och figurer

2.264/267:s asymptotkort frågar efter a och g(x) i x=a respektive y=g(x).
Det ger enkla, märkta numeriska/uttrycksfält. Både med och utan x=/y= fungerar.
Extrempunkterna använder fyra ordnade fält: maximum x/y, minimum x/y.
Fullprecisionsvärden och halv tusendels tolerans följer begärda tre decimaler.
Rotuttryck godtas också. Fel tecken, fel avrundning och omkastade punkter
underkänns. 2.264 c frågar ja/nej och godtar nej.

2.264 a höjs från nivå 1 till E/nivå 2: två asymptottyper kräver mer än
ett direkt grundsteg. Övriga nivåer bevaras: 2.267 a E/2, båda b C/3,
2.14 C/3, 2.103 E/2, 2.486 C/3, 2.488 C/3. De längre b-kortens arbetsinsats
höjs till 2. Nya granskningen följer fem liknande fall i FP67 och granskar
sex ytterligare uppgifter inom samma område.

2.14/103 förblir spel:false och utan självrättning. Browserprovet renderar
dem endast som kontroll, det gör dem inte till tillgängliga träningskort.
Räknare/GeoGebra bevaras för grafanalysen i 2.14/103/264/267. 2.486 tillåter
räknare men inte GeoGebra. 2.488 kräver inget numeriskt räknande; exakt
analys sker fortsatt utan räknare/GeoGebra. Kontroll gäller även delkort.

Tre nya lösningsgrafer ritas från originalfunktionerna. Bruten kurvritning
vid asymptoter undviker falska förbindelser mellan grenarna. Inga figurer i
a-facit avslöjar b-svaren. 2.103 har redan ett graderat skissrutnät. 2.486/488
behåller sina analytiska lösningar utan ytterligare graf.

## Verifiering

- 48 faktiska svarskontroller samt 34 elev-/lärarvisningar vid 390/1280 px
  passerar, utan JavaScriptfel, KaTeXfel eller klippta formler.
- Nya grafer granskade visuellt. SVG-analys av samtliga fem kopior ger inga fynd.
- Oberoende tester kontrollerar koordinater mot originalfunktionerna,
  derivatans tecken på båda sidor och metadata för ordnade svar.
- Sju relevanta testfiler passerar, inklusive tidigare FP59/64–67.
- Bankvalidator: 72 befintliga fynd före/efter, inga nya.
- ID:n och övriga bankobjekt bevaras. Före/efter sparas i motsvarande JSON.

Inga produktionsrapporter avslutade och inga elevkommentarer skickade.
