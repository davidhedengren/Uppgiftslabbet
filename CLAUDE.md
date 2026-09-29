# Uppgiftslabbet – instruktioner för Claude

Claude är agenten som underhåller Uppgiftslabbet och Kunskapsgymmet. Innan du granskar, ändrar, synkroniserar eller levererar något i detta repo **ska** du läsa och följa:

1. `agent/ARBETSINSTRUKTION.md` – övergripande arbetsgång och modellbudget
2. `agent/INNEHALLSREGLER.md` – kontrollkedja för uppgifter, facit, ledtrådar, Kunskapsgymmet-kort och SVG
3. `agent/PEDAGOGISKA_REGLER.md` – förmåga, nivå, självrättning och svarsformat
4. `agent/KVALITETSKONTROLL.md` – checklistor före och efter ändring
5. `agent/GIT_OCH_BACKUP.md` – Git från flera datorer, banksynkronisering och backup

Reglerna i `agent/` gäller Claude på samma sätt som de gällde Hermes.

## Kärnregler (gäller även innan dokumenten ovan har lästs)

- Kör `git status`, `git fetch origin --prune` och jämför med upstream före redigering. Användaren laddar ofta upp filer via GitHubs webb och arbetar från flera datorer.
- Använd aldrig force push. Gör ingen commit eller push utan användarens godkännande.
- Uppgiftslabbet är master för de sju gemensamma bankerna. Kunskapsgymmet får bara synkade kopior, aldrig egna manuella ändringar.
- Bevara ID:n och radera aldrig uppgifter eller filer utan uttryckligt godkännande.
- Befintlig metadata och facit är referensmaterial, inte facit. Räkna själv.
- Heuristiska fynd får aldrig massändras.
- Ändra bara det användaren har bett om.

## Modellbudget för Claude

Inled varje nytt arbete med ”För det här jobbet föreslår jag …” (Sonnet eller Opus) med en kort motivering. Byt inte modell mitt i en lång session, eftersom det kräver en dyr omläsning utan cache. Föreslå i stället att användaren startar en ny session med rätt modell för jobbet. Sonnet räcker för mekaniskt och deterministiskt arbete. Opus behövs för svår matematik- och fysikgranskning, pedagogiska bedömningar, geometriskt SVG-arbete och komplex kod.

Avsnitt 7 i ARBETSINSTRUKTION (Luna/Sol/Astra) översätts så här: använd deterministiska verktyg först, starta inga subagenter för rutinkontroller, och fråga användaren innan en bred AI-granskning av många uppgifter.

## Miljö på datorn `Hedav`

- Repona ligger i `C:\Users\Hedav\code\Uppgiftslabbet` och `C:\Users\Hedav\code\kunskapsgymmet`.
- **Node.js finns inte** och får inte installeras (IT-policy). `tools/*.js` och `node --check` kan därför inte köras direkt. Använd i stället parsning i den inbyggda webbläsaren eller PowerShell, och redovisa att Node-testerna inte har körts.
- Backupsystemet i `GIT_OCH_BACKUP.md` finns på den andra datorn (`C:\Users\david\...`), inte här.
