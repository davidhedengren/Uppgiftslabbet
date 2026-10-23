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
