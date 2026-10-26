# Kunskapsgymmet: deluppgifter i följd (från 2026-10-24)

Användaren tyckte att uppgifter med a), b) och c) blev konstiga i Kunskapsgymmet. Varje delkort
visades som ett eget kort, med samma inledning upprepad, ofta långt ifrån varandra i passet.

## Beslut

- **Uppgiftslabbet och bankerna ändras inte.** Uppgifterna är fortfarande vanliga flerdelsuppgifter
  med `spelDelar`. Delkorten finns kvar som underlag för träningen.
- **Kunskapsgymmet visar hela uppgiften i följd.** När träningen väljer ett delkort startar en kedja
  från uppgiftens första del på elevens nivå: a) → b) → c).
  - Den gemensamma inledningen visas en gång. Den hittas som de block (stycken, figurer, tabeller)
    som alla delkort börjar med.
  - Besvarade delar står kvar ovanför, med elevens svar och ✓ eller ✗.
  - En senare del visar inte block som en tidigare, redan visad del började med. Det gäller till
    exempel b) och c) som beskriver samma kloss när a) har ett eget nivå 1-underlag.
  - Varje del registreras fortfarande på sitt eget delkort (till exempel 3.466b). Nivåer, XP,
    historik och passets räkning fungerar som tidigare.
- **Svårare delar är frivilliga** (användarens val). En del över nivån på det kort som träningen valde
  märks med röd text, "OBS! Svårare nivå", och kan hoppas över med "Hoppa över".
- Kedjan används inte i prov, i lärarens bläddringsläge eller när eleven går tillbaka i passet.

Koden finns i Kunskapsgymmets `index.html`, i funktionerna `kedjaStarta`, `kedjaDelning`,
`kedjaTbody`, `kedjaSpara`, `kedjaNasta` och `kedjaFortsatt` samt i `visaUppgift`, som bröts ut ur
`nextTask`. Den är provad med Ma3 3.466 (flerval och tal) och Fy1 4.173 (nivå 1, 3 och 3, med
"Hoppa över").

## Tillägg 2026-10-26: lärarversionen när delkorten saknar gemensam inledning

I Fy1 har 764 av 1217 flerdelsuppgifter delkort som är skrivna som självständiga kort med egna
inledningar. Kedjan hittade då ingen gemensam inledning och visade varje dels hela text. Samma
situation kom därför i ny formulering i varje del, och läraren rapporterade att det kändes som
samma fråga igen (Fy1 3.93 i felloggen 2026-10-26).

`kedjaLararversion` i Kunskapsgymmet används nu när inga inledande block är gemensamma:

- Uppgiftens `spelIntro` (inledning och figur) visas en gång.
- Varje del visar bara sin korta fråga, `fraga`.
- Villkoret är att `spelIntro` och alla synliga delars `fraga` finns. Det gäller 695 av 764 sådana
  Fy1-uppgifter.
- Bankerna ändras inte. Uppgifter som redan har gemensam inledning, som nästan alla mattekort,
  visas som tidigare.

Provat live med Fy1 3.93. Inledningen och figuren visas en gång. a) står kvar med svar och ✓,
och b) är bara ”Hur lång tid tar det att nå lyftfarten?”.

## Tillägg 2026-10-26 (2): gemensamma meningar och rensade korta frågor

- **`kedjaGemensammaMeningar`** används när varken block eller lärarversion ger en inledning. Om
  alla delkorts första stycke börjar med samma meningar blir de meningarna inledningen, och resten
  av stycket blir delens fråga. Det gäller till exempel Fy1 2.11, 5.544, 5.548 och 9.398, och fler
  uppgifter i andra banker.
- **Andel uppgifter med gemensam inledning efteråt:** Fy1 1152/1217 (före: 453), Fy2 373/384, Ma1
  325/366, Ma2 294/323, Ma3 93/101, Ma4 553/553, Ma5 224/231.
- **Uppgifter som fortfarande saknar inledning** är samlingar av olika övningar, till exempel
  "Omvandla 2,7 g/cm³ till kg/dm³." följt av andra omvandlingar. Där ska varje del visa sin egen
  text. Fy1 8.10 är inte med i träningen (`spel:false`).
- **Korta frågor (`fraga`) i Fy1 som upprepade inledningen:** 89 frågor i 65 uppgifter är
  rensade. Inledande meningar som redan står i `spelIntro` har tagits bort (skripten
  fraga_strip.py och fraga_godkann.py i scratchpad). Alla förslag är genomlästa, och 23 är
  handjusterade där frågan annars blev tvetydig eller fortfarande upprepade inledningen:
  - 2.35 a: "Bestäm A4-arkets area".
  - 8.37 a: "laddaren".
  - 8.445: "torktumlaren" och "datorn".
  - 9.43 a: "Vad betyder det att bananen har aktiviteten 15 Bq?".
  - 9.91 och 9.96: "dosen per timme".
  - 9.20, 9.61 och 9.62: bara "Bestäm massdefekten i u.".
  - 9.66 a: figuren behålls.
- Delkortens egna `t`, facit och svar är oförändrade.
