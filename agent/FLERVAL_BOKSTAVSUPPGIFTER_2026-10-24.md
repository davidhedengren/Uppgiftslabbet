# Bokstavsuppgifter blir blandningsbara flervalskort (från 2026-10-24)

Användaren ville att Kunskapsgymmet ska blanda svarsalternativen. Appen blandar redan
alternativen i riktiga flervalskort (`svarstyp: "alternativ"`, funktionen `altOrdna` i
Kunskapsgymmets `index.html`). Men många uppgifter hade alternativen hårdkodade i frågetexten
("A: …<br>B: …" eller "**A** höger, **B** vänster …") och eleven skrev en bokstav
(`svarstyp` `val` eller `kort_text`, `rättSvar` `"B"`). De kunde inte blandas.

## Omvandling

Skript i sessionens scratchpad: `bokstav_om.py` (val av uppgifter och ny text) och
`ersatt_falt.py` (byter bara de berörda fälten i källtexten).

- Stycket med alternativen tas bort ur `t`, liksom "(Svara A, B eller C.)" och
  "Svara med bokstaven".
- `alternativ` får innehållet som text i ursprunglig ordning. Rätt alternativ markeras
  `ratt: true`. `svarstyp` blir `alternativ`, `rättSvar` och `tolerans` blir `null`, och
  `svarFormat`, `svarEnhet` och `svarVardesiffror` tas bort.
- Facits svarsrad "Svar: B", "Svar: Alternativ B (vänster)" eller "Svar: **C**" blir
  "Svar: <innehållet>". Resten av facit ändras inte.
- Uppgifter hoppas över och lämnas till handgranskning när bokstäverna används på annat
  sätt: i frågan (till exempel "vagn A och B"), i ledtråden eller i facit ("I A minskar …"),
  när svarsraden har en annan form eller när uppgiften har delkort.

Ändring i appen: alternativ som bara är bokstäver som syftar på figurens delar ("A", "Bild B")
blandas inte, eftersom deras ordning inte är någon ledtråd.

## Rundor

| Runda | Bank | Omgjorda | Hoppade (handgranskas) |
|---|---|---:|---:|
| 1 | Fy2 (`uppgifter2.js`) | 75 | 14 |

Testet `tools/felrapporter-2026-10-22-1541.test.js` jämför nu kraftriktningen i 3.161–3.172
med rätt alternativs text i stället för bokstaven.
