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
- **Svarsrad** läggs till där den saknas, och byggs bara ur data som redan finns:
  - självrättande uppgifter: `rättSvar` med enhet och format (grader, procent),
    avrundat efter toleransen; flera delar med etiketter, deluppgifter som a) b) c);
  - flervalsuppgifter: rätt alternativ;
  - manuella uppgifter: sista `\boxed{…}` i facit.
  Manuella uppgifter utan inramat svar lämnas och räknas upp nedan.
- `rättSvar`-uttryck som `(x-1)/2`, `x^(2)` och `<=` skrivs om till LaTeX
  (`\dfrac`, `^{}`, `\le`).

## Kontroller per runda

- All text i det gamla facit finns kvar (`facit_kontroll.py`). Enda skillnaden
  utöver svarsraden är att en befintlig svarsrad kan flyttas sist.
- Bara `s`-raden ändras i varje objekt. Filens indrag och radslut bevaras.
- `node --check`, `git diff --check` och alla tester som läser `uppgiftermato1.js`
  (utom `granska-svg.test.js`, som startar Chrome): 109 av 110 godkända, både före
  och efter. Det enda felet gäller figurbredd i `uppgifter.js` (Fysik 1).
- Visuell kontroll i Kunskapsgymmet: svarsraden visas som svarsruta och
  matematiken renderas av KaTeX.

## Rundor

| Runda | Kapitel | Ändrade facit | Kvar utan svarsrad |
|---|---|---:|---:|
| 1 | Kap 1 | 215 | 87 (manuella utan inramat svar) |
