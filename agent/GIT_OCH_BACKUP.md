# Git och backup

## Grundregel

GitHub är gemensam synkroniseringspunkt när Uppgiftslabbet eller Kunskapsgymmet bearbetas från flera datorer. Lokal disk är en arbetskopia, inte automatiskt den senaste sanningen.

Använd aldrig force push. Skriv aldrig över nyare GitHub-innehåll enbart därför att den lokala filen är annorlunda.

## Före varje arbetsomgång

Kör minst:

```bash
git status --short --branch
git branch --show-current
git remote -v
git fetch origin --prune
git rev-list --left-right --count HEAD...@{upstream}
```

Kontrollera därefter:

- lokala, ej committade ändringar,
- ospårade filer,
- om lokal branch ligger före eller efter upstream,
- om lokal och remote har divergerat,
- om remoteändringarna berör samma filer eller uppgifter som det planerade arbetet.

Om remote ligger före och arbetskopian är ren kan en fast-forward-integration användas, exempelvis `git pull --ff-only`. Om arbetskopian innehåller lokala ändringar eller historiken har divergerat ska ändringarna först analyseras och säkras. Använd inte reset, checkout eller annan destruktiv åtgärd för att få en ren arbetskopia utan uttryckligt godkännande.

## Samtidiga ändringar

Om lokal och remote har ändrat olika saker ska båda ändringsmängderna integreras. Merge eller rebase får bara väljas efter att branchens läge, lokala ändringar och projektets leveranssätt har kontrollerats.

Vid verklig innehållskonflikt får agenten aldrig godtyckligt välja lokal eller remote version. Konflikten ska beskrivas konkret och lämnas för redaktionellt eller tekniskt beslut om korrekt kombination inte kan härledas säkert.

Efter merge eller rebase ska relevanta tester köras igen och den resulterande diffen granskas.

## Före commit

- Kör relevanta tester och validatorer.
- Granska `git diff` och `git diff --check`.
- Kontrollera att endast avsedda filer ingår.
- Kontrollera att tillfälliga filer, lokala experiment, hemligheter och orelaterade ändringar inte stagats.
- Bevara pågående lokala ändringar som inte tillhör leveransen.

## Precis före push

Kör åter:

```bash
git fetch origin --prune
git rev-list --left-right --count HEAD...@{upstream}
```

Om remote har förändrats under arbetet ska förändringen analyseras och integreras före push. Kör därefter relevanta tester igen. Använd aldrig `--force` eller `--force-with-lease` för detta projekt utan ett separat, uttryckligt beslut som ändrar denna regel.

Efter push ska remote läsas tillbaka och jämföras med lokal branch innan synkronisering rapporteras som klar.

## Uppgiftslabbet och Kunskapsgymmet

Uppgiftslabbet är tills vidare master för de sju gemensamma uppgiftsbankerna. Kunskapsgymmet ska konsumera godkända masterversioner; agenten får inte självständigt redigera två kopior av samma uppgift så att de divergerar.

Före framtida banksynkronisering:

1. Kontrollera status i båda repona.
2. Kör `git fetch` i båda repona.
3. Jämför lokal branch mot respektive upstream.
4. Jämför den berörda banken mellan repona.
5. Kontrollera särskilt om Kunskapsgymmets kopia innehåller ändringar som saknas i Uppgiftslabbet.
6. Integrera unika, giltiga ändringar i master eller begär beslut; skriv inte över dem blint.
7. Synkronisera först därefter den godkända masterversionen till Kunskapsgymmet.
8. Kör tester och verifiera diffen i båda repona innan separata commits eller pushar godkänns.

En lyckad filkopiering är inte i sig bevis på korrekt synkronisering.

## Lokalt backupsystem

Backupsystemet är fristående från båda Git-repona och körs utan Hermes eller annan AI.

- Script: `C:\Users\david\Documents\Agenten\LocalBackup\scripts\Backup-AgentProjects.ps1`
- Backuprot: `C:\Users\david\Documents\Agenten\LocalBackup\archives`
- Loggar: `C:\Users\david\Documents\Agenten\LocalBackup\logs`
- Källor:
  - `C:\Users\david\Documents\Agenten\GitHub\Uppgiftslabbet`
  - `C:\Users\david\Documents\Agenten\GitHub\kunskapsgymmet`

Varje lyckad körning skapar en katalog med tidsstämpeln `yyyyMMdd_HHmmss`. Katalogen innehåller:

- ett ZIP-arkiv med båda projekten och deras `.git`-metadata,
- `manifest.json` med källor, arkivets storlek och SHA-256 samt kontrollsummor för centrala filer,
- `verification.json` med resultat från återställningskontrollen,
- `VERIFIED.ok`, som endast skapas efter lyckad full extraktion och kontroll av centrala filer.

`LATEST_VERIFIED.txt` pekar på den senast verifierade backupen. Pågående och misslyckade körningar hålls separerade i `.inprogress` respektive `.failed` och ersätter inte den senaste fungerande backupen.

Scriptet exkluderar genererbara cache- och byggkataloger såsom `node_modules`, cachekataloger, `tmp`, `temp`, `__pycache__`, `dist` och `build`. Arbetskopiornas övriga innehåll, inklusive ospårade och ej committade filer samt `.git`, ingår.

### Manuell körning

```powershell
powershell.exe -NoProfile -NonInteractive -ExecutionPolicy Bypass `
  -File "C:\Users\david\Documents\Agenten\LocalBackup\scripts\Backup-AgentProjects.ps1" `
  -BackupType ManualTest
```

Exitkod `0` betyder att arkivet skapades, kunde extraheras och klarade kontrollen. Annan exitkod betyder fel; detaljer skrivs till månadsloggen i loggkatalogen.

### Retention

Minst de 12 senaste verifierade backuperna behålls. Gallring körs först efter att den nya backupen har verifierats och flyttats till sin slutliga katalog. Endast äldre kataloger som innehåller `VERIFIED.ok` får raderas automatiskt. Den senaste verifierade backupen skyddas uttryckligen från radering. Misslyckade eller ofullständiga körningar omfattas inte av automatisk retention och ska granskas separat.

### Schemaläggning i Windows

Windows Task Scheduler-uppgiften heter `AgentProjects-WeeklyBackup` och körs varje söndag klockan 03:00 lokal tid. Åtgärden är:

```text
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -NonInteractive -ExecutionPolicy Bypass -File "C:\Users\david\Documents\Agenten\LocalBackup\scripts\Backup-AgentProjects.ps1" -BackupType Scheduled
```

Uppgiften använder ingen AI-tjänst. Den är inställd att starta så snart som möjligt efter en missad tid, väcka datorn för körningen, tillåta körning på batteri och förhindra parallella instanser. Den körs med användaren `david` i interaktivt läge; om användaren är helt utloggad kan körningen därför vänta tills en interaktiv session finns.

### Återställningsförfarande

Återställ alltid först till en separat katalog. Extrahera aldrig direkt över ett befintligt repo.

1. Välj en tidsstämplad backupkatalog som innehåller `VERIFIED.ok`.
2. Läs `manifest.json` och notera `ArchiveName` samt `ArchiveSha256`.
3. Kontrollera arkivets SHA-256:

   ```powershell
   (Get-FileHash -Algorithm SHA256 -LiteralPath "SÖKVÄG_TILL_ARKIV.zip").Hash
   ```

   Värdet ska vara identiskt med `ArchiveSha256` i manifestet.

4. Skapa en tom återställningskatalog utanför båda aktiva repona, exempelvis:

   ```powershell
   New-Item -ItemType Directory -Path "C:\Users\david\Documents\Agenten\LocalBackup\restore-test" -Force
   ```

5. Extrahera arkivet med Windows inbyggda `tar.exe`:

   ```powershell
   & "C:\Windows\System32\tar.exe" -xf "SÖKVÄG_TILL_ARKIV.zip" `
     -C "C:\Users\david\Documents\Agenten\LocalBackup\restore-test"
   ```

6. Kontrollera att följande minst finns i den extraherade kopian:

   - `Uppgiftslabbet\uppgifterma2.js`
   - `Uppgiftslabbet\.git\HEAD`
   - `Uppgiftslabbet\agent\GIT_OCH_BACKUP.md`
   - `kunskapsgymmet\index.html`
   - `kunskapsgymmet\uppgifterma2.js`
   - `kunskapsgymmet\.git\HEAD`

7. Jämför vid behov dessa filers SHA-256 med `RequiredFiles` i `manifest.json`. `verification.json` från backuptillfället ska dessutom visa `Verified: true`, `ArchiveReadable: true`, `FullExtractionSucceeded: true` och `Match: true` för samtliga centrala filer.
8. Öppna de återställda repona från den separata katalogen och kör läsande Git-kontroller, exempelvis `git status` och `git log`, innan någon aktiv arbetskopia ersätts.
9. Om en aktiv arbetskopia måste ersättas: stäng program som använder den, byt först namn på den befintliga katalogen och flytta sedan in den verifierade återställningen. Radera inte den tidigare katalogen förrän den återställda kopian har kontrollerats.
10. Kör projektens relevanta tester efter en faktisk återställning.

En återställning ska avbrytas om arkivhashen inte stämmer, arkivet inte kan extraheras, en central fil saknas eller kontrollsummorna skiljer sig.
