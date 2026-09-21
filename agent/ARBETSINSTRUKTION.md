# Arbetsinstruktion för Uppgiftslabbet

Detta dokument är den övergripande instruktionen för agentarbete i Uppgiftslabbet. Det ska läsas före granskning, ändring, synkronisering eller Git-leverans.

Kompletterande regler:

- [PEDAGOGISKA_REGLER.md](PEDAGOGISKA_REGLER.md) – självständig matematisk och pedagogisk bedömning.
- [GIT_OCH_BACKUP.md](GIT_OCH_BACKUP.md) – säkert arbete från flera datorer, synkronisering och framtida backup.
- [KVALITETSKONTROLL.md](KVALITETSKONTROLL.md) – kontroller före och efter ändringar.
- Avsnitt 7 i detta dokument – modellpolicy, kostnadskontroll och eskaleringsordning före delegering.

## 1. Grundprinciper

1. Befintlig metadata och närliggande uppgifter är referensmaterial, inte facit.
2. Varje uppgifts matematiska innehåll ska granskas självständigt.
3. Förmåga, nivå, självrättningsbarhet och tekniskt svarsformat ska bedömas separat.
4. En svår problemlösnings- eller resonemangsuppgift kan vara självrättande om slutsvaret kan representeras entydigt.
5. Tekniska begränsningar i Kunskapsgymmet ska inte i onödan styra formuleringen av en matematiskt bra uppgift.
6. Osäkra eller heuristiska validatorfynd får inte massändras automatiskt.
7. Uppgifts-ID ska bevaras när det är rimligt.
8. Matematiska förändringar ska verifieras och relevanta tester ska köras.
9. Ändra endast det användaren har godkänt. Gör inga närliggande städningar eller massändringar utan uttryckligt uppdrag.
10. Vid osäkerhet som kan påverka matematiskt innehåll eller innebära att en version väljs framför en annan ska agenten stoppa och begära ett redaktionellt beslut.

## 2. Start av varje arbetsomgång

Före redigering:

1. Kontrollera aktuell arbetskatalog, branch, upstream och `git status`.
2. Kör `git fetch` mot relevant remote.
3. Kontrollera om remote innehåller commits som saknas lokalt, om lokalt arbete ligger före remote eller om historiken har divergerat.
4. Läs befintliga lokala ändringar innan nya filer ändras. Bevara pågående, ej committat arbete som ligger utanför uppdraget.
5. Integrera remoteändringar säkert innan redigering om de påverkar arbetet. Skriv aldrig över dem blint.
6. Läs relevanta regler i `agent/` och de filer vars faktiska körbeteende påverkar uppgiften.

## 3. Analys före ändring

För varje berörd uppgift:

1. Lös eller verifiera matematiken självständigt.
2. Bedöm förmåga och nivå utifrån vad eleven faktiskt måste göra.
3. Fastställ lösningsmängd, ordning, enheter, tolerans och om flera representationer kan vara likvärdiga.
4. Bedöm därefter om slutsvaret kan självrättas.
5. Verifiera det tekniska metadataformatet mot Kunskapsgymmets faktiska konsumentkod eller en etablerad, testad kontraktsmodell.
6. Använd liknande uppgifter som jämförelse, aldrig som ensam motivering.

## 4. Ändringsprinciper

- Gör minsta korrekta ändring.
- Bevara uppgiftstext, ID och metadata som inte behöver ändras.
- Skilj på matematisk/pedagogisk korrigering och teknisk anpassning.
- Skriv inte om en bra uppgift enbart för att kringgå en tillfällig teknisk begränsning.
- Ändra inte Uppgiftslabbet och Kunskapsgymmet som två oberoende källor. Följ master- och synkroniseringsreglerna i `GIT_OCH_BACKUP.md`.
- Automatisk korrigering får endast göras när regeln är säker, avgränsad och verifierbar. Heuristiska fynd ska granskas redaktionellt.

## 5. Verifiering och leverans

Efter ändring:

1. Kör kontrollerna i `KVALITETSKONTROLL.md`.
2. Granska diffen och verifiera att endast avsedda objekt och fält har ändrats.
3. Kontrollera på nytt att lokala, orelaterade ändringar är bevarade.
4. Gör ingen commit eller push utan uttryckligt godkännande när arbetsuppdraget kräver ett separat granskningssteg.
5. Precis före en godkänd push ska remote hämtas igen och eventuell samtidig ändring integreras säkert.
6. Rapportera ändrade filer och fält, verifieringar, testresultat, kvarstående osäkerheter samt om commit eller push faktiskt utfördes.

## 6. Källansvar

Uppgiftslabbet är tills vidare master för de sju gemensamma uppgiftsbankerna. Kunskapsgymmet är konsument av dessa banker. En godkänd masterändring får senare synkroniseras, men en bank i Kunskapsgymmet får aldrig skrivas över innan båda repona och deras remotes har jämförts enligt `GIT_OCH_BACKUP.md`.

## 7. Modellbudgetpolicy och kostnadskontroll

### Deterministiskt först

Deterministiska lokala verktyg och tester ska alltid användas framför AI när de kan lösa uppgiften. AI får inte användas för att ersätta en tillgänglig lokal, reproducerbar och tillräcklig kontroll.

Använd lokala verktyg utan modell- eller subagentstart för bland annat:

- filkopiering, filinventering, sökning, parsing och filräkning,
- hashning, kontrollsummor och backup,
- Git-status, branch-, diff-, historik- och remotejämförelser,
- syntaxkontroller, testsuites, validatorer och sammanställning av deras resultat,
- rapportgenerering och annan mekanisk formatering.

Starta inte modellsubagenter för rutinmässig verifiering, testresultat, filinventering, Git-kontroller, hashning eller rapportgenerering. Om en delegeringsmekanism inte erbjuder rätt kostnadsnivå ska uppgiften utföras direkt med deterministiska verktyg, inte delegeras till en dyrare modell.

### Förbud mot automatisk massgranskning

Massgranskning med AI får inte startas utan användarens uttryckliga godkännande. Detta gäller även om varje enskilt fall verkar enkelt eller om modellen är billig.

När en stor mängd innehåller ett litet antal osäkra fall ska den deterministiska delen först avgränsa dessa fall. Eskalera därefter hellre ett litet antal uttryckligen osäkra fall än att låta Sol eller någon annan modell granska hela mängden.

### Tillåtna modellnivåer

1. **Luna eller motsvarande snabb/lätt modell** används sparsamt och endast när uppgiften faktiskt kräver visuell eller språklig bedömning som inte kan göras deterministiskt.
2. **GPT-5.6 Sol** används endast för enskilda, avgränsade fall som kräver avancerat matematiskt, pedagogiskt, visuellt, geometriskt, säkerhetsmässigt eller tekniskt resonemang. Sol får inte användas som standardgranskare för hela mängder.
3. **Astra** får endast användas efter användarens uttryckliga godkännande för det aktuella uppdraget.

### Delegering, eskalering och oberoende granskning

Före varje modell- eller subagentstart ska agenten kunna ange varför deterministiska verktyg inte räcker, varför just den valda modellnivån behövs och hur många fall som ska behandlas.

Eskalera endast osäkra fall och i minsta nödvändiga antal. Börja inte en bred Sol-granskning bara därför att huvudsessionen använder Sol eller därför att ett delegationsverktyg finns tillgängligt.

Oberoende AI-granskningar ska endast göras när en konkret risknivå motiverar kostnaden, exempelvis säkerhetskritisk kod, svår matematik eller en irreversibel operation. De ska inte startas rutinmässigt efter varje teknisk ändring. Vanliga dokumentationsändringar, mekaniska dataändringar och redan deterministiskt verifierade ändringar kräver inte en separat AI-granskare.

### Säkerhetsgrindar

- Deterministiska tester, hashkontroller och andra maskinella verifieringar ska alltid köras oberoende av eventuell modellbedömning.
- En lätt modell får inte ensam godkänna en osäker matematisk ändring, en säkerhetskritisk operation eller en automatisk bankändring.
- Heuristiska fynd får aldrig automatiskt ändra uppgifter eller SVG-figurer, oavsett modell.
- Om osäkerheten inte kan lösas inom den tillåtna modellbudgeten ska agenten stoppa och begära ett redaktionellt beslut i stället för att starta bredare eller dyrare AI-arbete utan godkännande.
