# Ma3-facit i samma form som Ma2 (från 2026-10-23)

Användaren bad om att facit i Ma3 (`uppgiftermato1.js`) ska se ut som i Ma2.
Ma2-facit är en numrerad steglista (`facit-v2 facit-stegvis` med
`ol.facit-steglista`) som avslutas med en egen svarsrad
`<p class="facit-svar"><strong>Svar: …</strong></p>`. Före ändringen saknade
ungefär 1 400 Ma3-facit svarsraden, och ungefär 350 var löpande stycken.

## Vad som ändras

- **Steglista:** facit som bara består av stycken (`<p>`) i en `facit-v2`
  görs om till steglista. Varje stycke blir ett steg. Texten ändras inte.
  En befintlig rad som börjar med "Svar:" blir svarsrad och placeras sist.
- **Förklaring och beräkning i samma steg:** ett block som bara innehåller
  matematik (en ekvation eller beräkning utan förklarande ord) läggs i steget
  före, som i Ma2. Detta gäller också befintliga steglistor där varje ekvation
  låg som ett eget steg, till exempel "Med den kända lutningen får vi" (steg 3)
  och "y−2=2x" (steg 4). Ett facit kan därför få ett enda steg, vilket är vanligt
  i Ma2 (379 facit där).
- **Undantag:** 2.124, 2.129, 2.134, 2.413 och 2.414 har medvetet löpande text
  enligt `MA3_LOGARITMER_2026-10-22.md`, och regressionstestet förbjuder steglista.
  De lämnas orörda.
- **Svarsrad** läggs till där den saknas, och byggs bara ur data som redan finns:
  - självrättande uppgifter: `rättSvar` med enhet och format (grader, procent),
    avrundat efter toleransen; flera delar med etiketter, deluppgifter som a) b) c);
  - flervalsuppgifter: rätt alternativ;
  - manuella uppgifter: sista `\boxed{…}` i facit.
  Manuella uppgifter utan inramat svar lämnas och räknas upp nedan.
- `rättSvar`-uttryck som `(x-1)/2`, `x^(2)` och `<=` skrivs om till LaTeX
  (`\dfrac`, `^{}`, `\le`), med följande regler:
  - `x^3/3` betyder \(\dfrac{x^3}{3}\);
  - bråkexponenter skrivs `x^{3/2}`;
  - `6*sqrt(5)` skrivs \(6\sqrt5\);
  - avslutande nollor tas bort (4,5, inte 4,50);
  - tal med fem eller fler siffror får tusentalsavstånd.
- **Deluppgifter:** när frågan har a), b) … blir svaret "a) …, b) …", även om
  `svarEtiketter` saknas. Ett inramat svar (`\boxed`) används inte som svarsrad
  i uppgifter med deluppgifter, eftersom det bara täcker sista delen.
- **Handskrivna svarsrader** för 13 uppgifter där svaret behöver tolkning,
  till exempel lösningsmängd, extrempunktens karaktär eller storhet:
  1.451, 1.491, 2.29, 2.121, 2.231, 2.282, 2.422, 2.423, 3.27, 3.38, 3.231,
  3.237 och 3.478. Alla är räknade för hand.

## Kontroller per runda

- All text i det gamla facit finns kvar (`facit_kontroll.py`). Enda skillnaden
  utöver svarsraden är att en befintlig svarsrad kan flyttas sist.
- Bara `s`-raden ändras i varje objekt. Från runda 2 byts bara själva
  `s`-strängen i källtexten ut, så att tal som `0.00005` inte skrivs om till `5e-05`.
  Filens indrag och radslut bevaras.
- `node --check`, `git diff --check` och alla tester som läser `uppgiftermato1.js`
  (utom `granska-svg.test.js`, som startar Chrome): 109 av 110 godkända, både före
  och efter. Det enda felet gäller figurbredd i `uppgifter.js` (Fysik 1).
- Visuell kontroll i Kunskapsgymmet: svarsraden visas som svarsruta och
  matematiken renderas av KaTeX.

## Rundor

| Runda | Kapitel | Ändrade facit | Kvar utan svarsrad |
|---|---|---:|---:|
| 1 | Kap 1 | 215 | 87 (manuella utan inramat svar) |
| 2 | Kap 2, och kap 1 grupperas om | 656 (kap 1: 165, kap 2: 491) | kap 1: 87, kap 2: 153 |
| 3 | Kap 3, och 34 svarsrader i kap 1–2 formateras om | 726 | kap 3: 208 |
| 4 | Kap 4, och 5 rader i kap 1–3 | 336 | kap 4: 53 |
| 5 | Kap 1–4: delvis självrättade uppgifter och lösningsmängder | 55 | totalt cirka 450 |

Efter runda 4 har 2 951 av 2 969 Ma3-facit steglista. Svarsrad finns i omkring
2 460 facit, varav några har en svarsrad per deluppgift.

Från runda 4 gäller också följande:

- **Negativa bråk** skrivs \(-\dfrac{3}{2}\).
- **Etiketter med enhet** skrivs \(c=5{,}3\) cm, och `Zmax` skrivs \(Z_{\max}\).
- **Bevisuppgifter** ("Visa att …") får ingen svarsrad, eftersom den bara skulle
  upprepa påståendet. Det gäller 3.149, 3.217, 3.774, 4.197 och 4.207.
  Om uppgiften också frågar efter något annat får den en handskriven
  svarsrad, som 1.212, 3.235 och 4.172.

Regressionstest: `tools/ma3-facit-som-ma2-2026-10-23.test.js` kontrollerar
balanserade steglistor, att svarsraderna saknar rå kalkylatorsyntax, att de
handskrivna svaren stämmer med egen räkning och att undantagen gäller.

## Runda 5

- **Lösningsmängder** skrivs "\(x=30^\circ\) eller \(x=150^\circ\)". Variabeln
  (x, v eller C) hämtas från frågan.
- **Två efterfrågade storheter** ("Bestäm \(\cos v\) och \(\sin v\)") ger etiketterna
  direkt ur frågetexten. Etiketten måste innehålla en bokstav, så att punkter
  som (4;3) aldrig tolkas som etiketter.
- **Delvis självrättade uppgifter** visar "c) se lösningen" för delar som bedöms
  manuellt, så att svarsraden aldrig ser fullständig ut när den inte är det.
- **Nollställen och förbjudna värden** i en del skrivs "\(x=-2\), \(x=0\) och \(x=2\)".
  Andra tallistor utan känd betydelse skrivs för hand: 2.785, 2.793, 2.797,
  2.798, 2.799 och 2.242, alla räknade för hand.

## Kvar

Facit utan svarsrad (kap 1: 87, kap 2: 153, kap 3: 208, kap 4: 53) är främst
resonemangs-, bevis- och tolkningsuppgifter utan entydigt kort svar. De kan få
handskrivna svarsrader i senare rundor, med prioritet för uppgifter som har ett
konkret slutsvar.
