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
| 7 | Facit förklarade alternativen med bokstäver ("A ger 76, B ger 25"). Bokstäverna byttes mot alternativets innehåll (formler som de står, text inom citattecken); 1.121 och 2.343 (Ma1) som namnuppgifter | 24 + 4 + 3 | |

I runda 7 rättades också ett fel i det ursprungliga facit för Ma3 1.449: det sade "Endast D uppfyller detta" fast rätt svar är E, \(4x^3+2x^2\). Ma1 0.402 sade "I alternativens ordning blir talen A: …", vilket inte stämmer när alternativen blandas, och visar nu bara talen. `ma1-uttryck-med-parenteser.test.js` jämför 1.1150 och 1.1151 med alternativens text.
| 8 | Handgranskade med en specifikation per uppgift (bokstav_spec.py): alternativ i egna stycken eller efter radbrytning, "Svara A eller B" mellan två namngivna saker (blir t.ex. "Butik A"/"Butik B"), figurer med bokstäver (blir bokstavsknappar som inte blandas) och svarsrader som "**C.** För …" | 5 + 2 + 1 + 2 + 32 (+ 5 tolkade automatiskt) | |

Runda 8 uppdaterade fysik1-densitet-2026-10-21, felrapporter-2026-10-21-1300 och tunna-omraden-2026-10-21.
| 9 | Ma3 3.466 och 3.470: deluppgift a) var ett bokstavsflerval i en flerdelsuppgift. Uppgifterna fick delkort där a) är ett flervalskort som appen blandar och b) ett numeriskt kort | 2 | |

## Medvetet kvar

11 flerdelsuppgifter där bokstaven är namnet på det man väljer, inte platsen i en lista, och därför inte kan avslöja något: Ma1 1.197, 1.469, 3.111, 3.116, 3.125, 3.173, 7.17 och 7.224 (abonnemang, sparformer eller tal som heter A, B och C), Ma2 1.267 (tabell A eller B) och 4.297 (para ihop histogram med lådagram A–C). Dessutom Fy2 5.24, där delkortet redan frågar efter en namngiven stjärna.
