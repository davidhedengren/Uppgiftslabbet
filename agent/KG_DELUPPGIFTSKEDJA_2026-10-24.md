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
