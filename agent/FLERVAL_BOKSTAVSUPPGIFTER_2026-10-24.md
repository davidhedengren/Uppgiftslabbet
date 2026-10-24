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
| 2 | Ma3 (`uppgiftermato1.js`) | 59 | 12 |
| 3 | Ma4 (`uppgiftermato2.js`) och Ma5 (`uppgiftermatf1.js`) | 16 + 14 | 7 + 15 |
| 4 | Ma1 (`uppgifterma1.js`) | 471 | 116 |

Testet `tools/felrapporter-2026-10-22-1541.test.js` jämför nu kraftriktningen i 3.161–3.172
med rätt alternativs text i stället för bokstaven.

Rättelse efter runda 1: när facit redan skrev ut svaret efter bokstaven ("Svar: A, infraljud.")
blev innehållet dubblerat. 2.301 och 5.324 (Fy2) samt 1.539 och 3.636 (Ma3) är rättade, och
skriptet tar nu bara bort bokstaven i sådana fall. `mato1-granskning-2026-10-18.test.js` jämför
1.539 med rätt alternativs text.

`felrapporter-2026-10-13-2127.test.js` läser bokstaven för Ma5 2.305, 2.541, 2.572 och 2.577 ur platsen i bankens alternativlista när kortet är ett flervalskort (banken behåller ursprunglig ordning; appen blandar).

Rättelse i runda 4: svarsrader med formen "Svar: B – regn." eller "Svar: A: ungefär 30 miljoner"
fick först alternativtexten före det korta svaret ("Regn.– regn."). I 45 Ma1-uppgifter är nu det
korta svaret efter tankstrecket eller kolonet svaret ("Svar: Regn.", "Svar: Ungefär 30 miljoner").
Regressionstestet letar efter sådana rester i alla omgjorda banker.

| 5 | Ma3, Ma4, Ma5 och Ma1: fler svarsformer ("<b>Svar: B</b>", "Rätt svar: A.", "B är rätt.", "Svar: B – självurval.") | 4 + 3 + 12 + 24 | ca 125 kvar totalt |

Runda 5 uppdaterade felrapporter-2026-10-13-2127, felrapporter-2026-10-19-2044 (granskningsspåret jämförs utan de omvandlade fälten för 2.407 och 2.408) och stickprov-standardavvikelse.
| 6 | Handgranskade: bokstäverna är namn i uppgiften ("Lån A", "System B", kompassuppgifterna i Fy2). Fy1 3.442, Ma1 7.185 och 3.256 omskrivna för hand | 11 + 1 + 1 + 34 + 1 | |

Runda 6 uppdaterade fy2-figurer-2026-10-23, fysik1-acceleration-2026-10-21 och felrapporter-2026-10-12-0958 så att de jämför rätt alternativs text.
