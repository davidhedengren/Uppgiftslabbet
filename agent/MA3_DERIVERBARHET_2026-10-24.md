# Ma3 – deriverbarhet, 24 oktober 2026

Området växer från 16 till 24 uppgifter. Åtta handskrivna nya uppgifter på
nivå 1–4, varav fem med egna SVG-grafer. Dessutom rättas #3.1191. Detta är
en avgränsad påfyllnad, inte en garanti om hela bankens kvalitet.

## Samtliga nya uppgifter

| ID | Nivå | Variation och kontrollerat svar |
| --- | --- | --- |
| 3.1207 | 1 | Konstant vattennivå i graf: h′(2) = 0 cm/h. |
| 3.1208 | 2 | Derivata på en rak del av en graf som har ett hörn på annan plats: f′(1) = −2. |
| 3.1209 | 1 | Vad följer säkert av f′(3) = −4? Kontinuitet vid x = 3, inte ett visst funktionsvärde. |
| 3.1210 | 3 | Kvadrerat absolutbelopp: |x−1|² = (x−1)² och f′(1) = 0. |
| 3.1211 | 3 | x|x| är deriverbar vid 0 trots absolutbeloppet. Differenskvoten |h| går mot 0. |
| 3.1212 | 3 | Ett parameterproblem utan lösning: kontinuitet kräver a = 4, lika lutningar a = 2. |
| 3.1213 | 4 | Kombinerar skarvens höjd, lutning och ett ytterligare punktvillkor: a = 5/3, b = −1/3, c = 1/3. |
| 3.1214 | 3 | Granska ett falskt bevis: symmetrisk differenskvot 0 för |x| innebär inte derivata 0. |

Miniräknare tillåts i samtliga. GeoGebra behövs inte: figurerna är givna och
frågorna prövar begrepp eller enkla exakta villkor, inte digital grafanalys.
Tre abstrakta frågor har ingen figur: en illustration skulle inte tillföra
nödvändig information eller skulle avslöja parameterlösningen.

## Åtgärdad: #3.1191

**Felorsak:** fyra differenskvoter för h = ±0,1 och ±0,01 behandlades som
bevis för olika ensidiga gränsvärden. Det följer inte av ändligt många prover.
Som oberoende kontroll kan q(h) = (300000h³−3330h+11)/22 användas:
q(−0,1) = q(−0,01) = 2 och q(0,01) = q(0,1) = −1, men funktionen
f(1+h) = hq(h) är ett polynom och har f′(1) = 1/2. Den gamla tabellen
kunde alltså även komma från en deriverbar funktion.

**Ändring:** tabellen anger nu uttryckligen vad kvoten närmar sig när h går
mot 0 från vardera sidan. Då är det befintliga rätta alternativet entydigt:
f är inte deriverbar vid x = 1. Vertikal tabell, omarbetat kort facit och
miniräknare tillåten. ID, svarsalternativ, nivå och ämnesområde bevaras.

**Kommentarsförslag:** ”Uppgiften anger nu gränsvärdena från båda sidor.
De är 2 respektive −1, så derivatan finns inte. Den tidigare tabellen med
bara fyra provvärden räckte inte för att dra den slutsatsen.”

## Fem jämförelser: Granskad – inget fel

Avgränsad kontroll av samma felorsak, beräkning och facit. Ingen ny fullständig
browsergranskning av dessa äldre uppgifter eller omklassning av deras nivå.

| ID | Kontrollerad beräkning och förslag på kommentar |
| --- | --- |
| 2.17 | ”Granskad – inget fel: (5,41−4,61)/0,2 = 4 används uttryckligen som approximation.” |
| 2.246 | ”Granskad – inget fel: accelerationen uppskattas till (20,50−19,50)/0,2 = 5 m/s².” |
| 2.386 | ”Granskad – inget fel: (5,04−5)/0,01 = 4 är en uppskattning, inte ett bevis för derivatan.” |
| 2.658 | ”Granskad – inget fel: den symmetriska kvoten (4,41−3,61)/0,2 = 4 efterfrågas som uppskattning.” |
| 2.659 | ”Granskad – inget fel: (9,0601−8,9401)/0,02 = 6 används som uppskattning.” |

## Verifiering

- Exakta identiteter, ensidiga gränsvärden och parametersystem kontrollerade
  med Sympy. Facit har också räknats igenom manuellt.
- Nya `tools/ma3-deriverbarhet-2026-10-24.test.js` och befintliga regressioner
  för kontinuitet, Ma3-facit och Ma3/Ma4-figurer godkända.
- Gemensamt browserprov för båda dagens områden: 278 svarskontroller,
  34 visningar vid 390/1280 px. Exakta bråk, funktionsprefix, enheter,
  ordnade fält, felaktiga svar och alternativa val ingår.
- Båda spåren verifierade i båda apparna. Inga KaTeX-/JavaScript-fel.
- Tre för långa facitrader upptäcktes på mobil och delades upp före leverans.
- Alla fem nya grafer visuellt granskade. Sekantetiketten flyttades från
  rutnätet efter geometrikontrollen. SVG: inga ERROR/WARNING; endast INFO
  för den avsiktligt kantfyllande vita bakgrunden.
- Bankvalidatorn har inga fynd för omgångens nio berörda objekt. Repots
  tidigare totalsiffror är oförändrade: 1483 ERROR, 230 WARNING, 1445 INFO.
- Objektdiff: exakt åtta nya objekt och endast #3.1191 ändrat bland äldre.
- Författarkälla: `tools/bygg-ma3-deriverbarhet-2026-10-24.py` med figurhjälpare
  från kontinuitetsomgången. Browserharness med båda områdenas namn finns i
  respektive repo. Ingen rapportstatus har ändrats i databasen.
