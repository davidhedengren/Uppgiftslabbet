# Fy2: nivå 2–3 i kosmologi, exoplaneter, stjärnor, avstånd, magnituder och jordens magnetfält, 2026-10-25

Enligt appens nivåräkning i `NIVAINVENTERING_2026-10-25` hade flera Fy2-områden få kort på nivå 3:

| Område | Kort på nivå 3 | Kort på nivå 1–2 |
|---|---|---|
| kosmologi | 1 | 29 |
| jordens magnetfält | 3 | — |
| exoplaneter | 4 | — |
| magnituder | 4 | — |
| stjärnornas utveckling | 6 | — |
| avståndsmätning | 6 | — |

Fy2-banken saknar ofta `traningsniva`, och appen härleder då nivån ur poängen. En rå räkning av `traningsniva` ger därför fel bild för Fy2.

**Lärarbeslut under arbetet:** ”Skippa astronomin helt just nu.” Läraren lade sedan till: ”Har du gjort bra uppgifter där får du gärna lägga in dem innan du skippar resten.” De astronomikort som redan var byggda och kontrollerade har lagts in. Inga fler astronomikort görs tills vidare.

## Nya kort (29 st: 7 på nivå 2 och 22 på nivå 3)

| Område | ID | Innehåll |
|---|---|---|
| kosmologi (6) | 5.464–5.469 | H₀ ur ett Hubblediagram (figur, nivå 2). Avstånd ur z (nivå 2). Rödförskjuten vätelinje ger z, fart och avstånd. Rödförskjutning ur skalfaktor. ”Är vi i centrum?” (flerval, nivå 2). Avstånd och fart ur ljusets restid. |
| jordens_magnetfalt (6) | 3.538–3.543 | Inklination ur komposanter (nivå 2). Ström ur en kompassnåls utslag (figur). Kraft på en kraftledning (bara den lodräta komposanten verkar). Inducerad spänning i en bilaxel. Kompass nära magnetiska polen (flerval, nivå 2). Proton från solvinden i jordfältet. |
| exoplaneter (6) | 5.470–5.475 | Transitdjup (nivå 2). Omloppstid med Keplers tredje lag (nivå 2). Period och radie ur en ljuskurva (figur). Avstånd ur transitperioden. Banfart ur en radialhastighetskurva (figur). Vad som krävs för planetens densitet (flerval). |
| stjarnornas_utveckling (3) | 5.476–5.478 | Radie ur strålningsmaximum och luminositet. Solens massförlust per sekund och på 10 miljarder år. Betelgeuses radie i solradier och AU. |
| avstandsmatning (4) | 5.479–5.482 | Avståndsintervall ur en osäker Gaia-parallax. En galax diameter ur synvinkeln. Solens synvinkel från Mars. Resa till Proxima Centauri. |
| magnituder (4) | 5.483–5.486 | Sammanlagd magnitud för en dubbelstjärna. Hur långt bort en stjärna syns med blotta ögat. Magnitud och flöde när avståndet ändras. Supernova av typ Ia som standardljus, kombinerad med Hubbles lag. |

Astronomireglerna från 2026-10-23 följs:

- AU används, aldrig AE.
- Ordet ”bolometrisk” förekommer inte.
- Inga solvärden eller konstanter från formelsamlingen står i frågan.
- Svar som beror på solens värden godtar T☉ 5 772–5 800 K och L☉ 3,83–3,85·10²⁶ W.

## Kontroll

- Facit räknas om i `tools/fy2-niva3-astro-magnetfalt-2026-10-25.test.js`, som passerar 2 av 2. Alla `tools/fy2*.test.js` passerar, 47 av 47.
- Inget nytt kort har samma facit som ett annat kort i området. Transitkortet fick radien 0,13 i stället för 0,12.
- Validatorn för `uppgifter2.js` ger 1514 fynd både före och efter ändringen.
- SVG-granskaren ger 0 varningar efter två ändringar:
  - Hubblediagrammets punkt heter P, och koordinaterna står i texten.
  - Kompassens etiketter flyttades.
- Självrättningen i Kunskapsgymmet testades med 82 svar. Testet täckte enheter med prefix (mV, kpc, Mpc), dygn, AU, ljusår, grader, tiopotenser, fel ordning och fel storleksordning. Alla gav väntat resultat.
