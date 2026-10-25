"""Sammanställ faktisk appinventering. Kör efter konsumentens inventera-nivaer-script."""
import json,sys,collections
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
data=json.loads(Path(sys.argv[1]).read_text());groups={}
for row in data['rows']:
 key=(row['course'],row['key'],tuple(row['ids']))
 if key not in groups:groups[key]=dict(row,tracks=[])
 groups[key]['tracks'].append(row['track'])
rows=list(groups.values())
COURSES={'ma1':'Ma1','ma2':'Ma2','mato1':'Ma3','mato2':'Ma4','matf1':'Ma5','fy1':'Fy1','fy2':'Fy2'}
NOTES={
 ('ma1','Stickprov och urvalsmetoder'):'Jämför två urvalsplaner, tolka bortfall i tabell och resonera om vilka slutsatser som går att dra. Enda nivå-3-kortet är 5.571.',
 ('ma1','Signifikans och felkällor'):'Behöver sammanhängande situationer om skevt urval, mätfel och slutsatser; inte bara namn på felkällor. 5.282 är ensamt på nivå 3.',
 ('ma1','Korrelation och kausalitet'):'Bredda med kontrollgrupper, gemensam bakomliggande faktor och granskning av missvisande diagram. Nu 5.188/203/204.',
 ('ma1','Intervall'):'Kombinera praktiska villkor, tolka gränser i diagram och felsök öppna/slutna intervall. 1.50/52 är nu hela nivå-3-urvalet.',
 ('ma2','Grafisk lösning av ekvationssystem'):'Mer än skärningsavläsning: välj modell, avgör när en skärning är relevant och rekonstruera en linje från villkor. Befintliga 1.225/678/679 har viss variation men är för få.',
 ('ma2','Kvartiler och percentiler'):'Fortsätt med omvända frågor om saknat värde, jämför fördelningar och granska påståenden. 4.363/2024/2027/2079 täcker flera idéer men bara fyra kort.',
 ('ma2','Linjär regression'):'Bredda modellkritik, enhetsbyten, avvikande punkter och val av modell. De fem befintliga korten varierar redan; fler situationer behövs, inte fem kopior.',
 ('ma2','Geometriska begrepp och definitioner'):'Fler resonemang med nödvändiga/tillräckliga egenskaper, egna motexempel och vinkelfigurer. Nu 3.494/495.',
 ('mato1','Naturliga logaritmer'):'Högst prioritet: nivå 3 saknas helt. Lägg till modellval, jämförelse av tillväxt, omvända parameterfrågor och felsökning av ln-regler. Rutinlösning 2.12/44/48 räcker inte som ny nivå 3.',
 ('mato1','Begreppet derivata'):'Tolka enhet, tecken och lokalt förändringstal ur tabell/graf; välj rimlig uppskattning och motivera. Nu bara 2.29/221.',
 ('mato1','Vad säger derivatan om funktionens graf?'):'Utveckla grafmatchning, extremvärden från f′ och jämförelse av förändring. 3.1165/1170/1171 är bra starttyper men för få.',
 ('mato1','Från derivata till funktion'):'Bredda med begynnelsevillkor, grafrekonstruktion och felsökning. Nu består nivå 3 av primitiva funktioner med bråk-/negativa exponenter (3.236/284).',
 ('mato1','Sinussatsen'):'Mer metodval, indirekt mätning och villkor som avgör om en triangel finns; behåll egna tydliga figurer. Nu 4.529/530.',
 ('mato2','Radianbegreppet'):'Mer samband mellan båge, vridning och period. Kalibrera först: 2.576 är vanlig omvandling och bör inte ensam räknas som djupare nivå-3-variation.',
 ('mato2','Polynomdivision'):'Komplettera med restens betydelse, omvänd koefficientfråga och felsökning av division. Nu 4.180/527.',
 ('mato2','De reella talen och imaginära tal'):'Bredda med algebraisk struktur, periodicitet och representationer. Kalibrera först 4.520 (rutinmässiga potenser av i).',
 ('mato2','Derivatan av sin x och cos x'):'Befintliga 2.476/150/477 täcker förenkling, bevis och modell. Fler olika situationer, inte enbart nya koefficienter i sin(ax).',
 ('matf1','Direkta bevis'):'Variera delbarhet, paritet, motexempel och granskning av ogiltiga steg. Fyra kort finns: 2.146/508/708/712.',
 ('matf1','Indirekta bevis'):'Fler val av negation, motsägelse och kontraposition med korta begripliga lösningar. Nu 2.113/718.',
 ('matf1','Vad är en differentialekvation?'):'Mer tolkning av förändringsmodeller, jämvikt och lösningskurvor. Nu 4.329/581/582; använd figurer där de bär resonemanget.',
 ('matf1',"Differentialekvationen y' + ay = 0"):'Variera parameter ur mätdata, modelljämförelse och kontroll av föreslagen lösning. Kontrollera även områdesplacering av 4.358, som har variabel koefficient 3x.',
 ('fy1','Newtons tredje lag'):'Fler situationer med tydligt val av kropp/system, par av krafter och felsökta kraftbilder. Nu 4.462 och 4.496 b.',
 ('fy1','s-t-diagram'):'Fler jämförelser av momentan/medelhastighet, ändrad rörelseriktning och rekonstruktion av rörelse. Nu 3.362/454.',
 ('fy1','Laddning'):'Mer laddningsbevarande, kontakt/jordning i olika ordning och modellval. Nu 8.506/518/521; två av tre rör liknande jordningsförlopp.',
 ('fy1','Seriekoppling'):'Fler felkopplingar, säkerhetsgränser och mätpåverkan med korrekta kretsbilder. Nu fem kort, varav två med liknande kortslutna ljusslingor.',
 ('fy2','Kosmologi'):'Hubblegraf, modellantaganden och jämförelse av observationer. Endast 5.12 på nivå 3; undvik kopior av 1/H₀.',
 ('fy2','Jordens magnetfält'):'Variera komposanter, kompassriktning och kombination av fält från olika källor. Nu 3.14/15/29.',
 ('fy2','Magnituder'):'Jämför skenbar/absolut magnitud, felsök slutsatser och kombinera avstånd med ljusstyrka. Nu fyra nivå-3-kort.',
 ('fy2','Exoplaneter'):'Ljuskurvor, jämförelse av möjliga modeller och osäkerheter. Fyra delkort kommer från bara tre huvuduppgifter; mer innehåll behövs än kortantalet antyder.'
}
def placement(r):
 return (r['course']=='ma1' and r['tracks']==['1a'] and r['name'] in ['Linjära olikheter','Trigonometri i tillämpningar']) or (r['course']=='mato1' and r['tracks']==['1b'] and (r['name'].startswith('Trigonometr') or r['name']=='Absolutbelopp'))
def action(r):
 if placement(r):return 'Spårplacering först'
 if r['levels'][2]<8:return 'P1: fler nivå-3-situationer'
 if r['levels'][2]<16 or r['parents3']<8:return 'P2: bredda nivå 3'
 if r['parents3']<r['levels'][2]/2:return 'Fler skilda huvuduppgifter'
 return 'Ingen mängdbrist på nivå 3 enligt tröskeln'
compact=[]
for r in rows:
 compact.append({k:r[k] for k in ['course','tracks','key','name','chapter','areas','levels','parents12','parents3','familiesLevels','families3','templates3','largestTemplate3','figures3','formats3']}|{'action':action(r),'missingLevel3Families':[f for f,v in r['familiesLevels'].items() if v[2]==0],'level3Ids':[q['id'] for q in r['tasks3']],'note':NOTES.get((r['course'],r['name']))})
metadata={'date':'2026-10-25','masterCommit':'ed183b3','consumerCommit':'08b3156','views':len(data['rows']),'distinctPools':len(rows),'method':'availableTasks + getCards, alla sju banker/spår; identiska fullständiga ID-urval sammanslagna','areas':compact}
(ROOT/'agent/NIVAINVENTERING_2026-10-25.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n')
lines=['# Inventering av nivå 1–2 och nivå 3 – 2026-10-25','',
 'Snapshot efter felloggsleveransen: Uppgiftslabbet `ed183b3`, Kunskapsgymmet `08b3156`. Inkluderar andra sessioners Ma2-omgångar 4–7, statistik/geometri S1–S3, Fy1 omgång 8 och Ma1:s 24 nya kort om oberoende händelser. Inga av dessa omgångar har gjorts om.',
 '', '## Metod och avgränsning','',
 f'Alla {len(data["rows"])} elevsynliga område/spår-vyer har inventerats genom appens egna `availableTasks()`, `expandGameTask()` och `getCards()`. Identiska fullständiga ID-urval på flera spår har slagits ihop: {len(rows)} olika område/spår-urval återstår. Historiska grupper och spel:false räknas inte som vanlig träning. Kapitelblandning räknas inte som nya uppgifter.',
 '', 'Nivå 1 och 2 räknas tillsammans enligt senaste användarbeslutet. Långsiktigt mål: 50–100; under 20 är en tydlig lucka, 20–29 en mindre buffert, 30–49 användbart men under målet. För nivå 3 används arbetsgränserna under 8 (inte ett helt åttapass), 8–15 (begränsad variation över flera pass), minst 16 (rimlig första mängd). Dessa nivå-3-gränser är prioriteringsförslag, inte nya användarregler.',
 '', 'Kort och skilda huvuduppgifter redovisas separat. Delar från samma uppgift är inte oberoende situationer. Delmoment, svarsformer, bilder och återkommande textmönster har inventerats i alla områden. Antal bilder eller ett enda familjenamn bevisar inte kvalitet eller monotoni. Textlikhet är en indikator, inte ett konstaterat fel.',
 '', 'Detta är en heltäckande **innehållsinventering**, inte en ny matematisk facitgranskning av varje uppgift. Manuell innehållsläsning av de prioriterade områdenas nivå-3-frågor ligger bakom förslagen nedan. Några nivåer och placeringar behöver granskas innan nya uppgifter konstrueras.',
 '', '## Sammanställning','', '| Bank | Olika område/spår-urval | Nivå 1–2 <20 | Nivå 1–2 <50 | Nivå 3 <8 | Nivå 3 8–15 | Nivå 3 ≥16 |','|---|---:|---:|---:|---:|---:|---:|']
for c,name in COURSES.items():
 rr=[r for r in rows if r['course']==c]
 v=[len(rr),sum(sum(r['levels'][:2])<20 for r in rr),sum(sum(r['levels'][:2])<50 for r in rr),sum(r['levels'][2]<8 for r in rr),sum(8<=r['levels'][2]<16 for r in rr),sum(r['levels'][2]>=16 for r in rr)]
 lines.append('|'+name+'|'+'|'.join(map(str,v))+'|')
lines+=['','## Beslut om nästa arbete','',
 '1. Kontrollera spåröar före masspåfyllnad: Ma1a linjära olikheter/trigonometri och Ma3b trigonometri/absolutbelopp. Dessa kan ha blivit synliga genom ett fåtal återplacerade repetitionsuppgifter. De ska inte automatiskt byggas ut som om allt tillhörde kursen.',
 '2. Ma1c Proportionalitet hade bara 8.18 och har nu nio nivå-3-kort, men inga nivå-1–2-kort. Kontrollera planering/placering och bygg sedan en riktig bas, eller samla innehållet i rätt befintligt lektionsområde.',
 '3. Prioritera Ma3:s nivå 3: naturliga logaritmer, derivatabegreppet, tolkning av derivatagraf och från derivata till funktion. Därefter Ma1:s statistiska resonemang samt Fy1:s s-t-diagram, tredje lagen och laddning.',
 '4. Ma2: framför allt 2a/2b grafiska ekvationssystem, kvartiler/percentiler och 2b regression. Ma2c har större samlade lektionsområden och får inte användas som bevis på att övriga spår är lika välfyllda.',
 '5. Fyll även Ma4:s polynomdivision/komplexa grunder, Ma5:s bevis/differentialekvationsbegrepp och Fy2:s kosmologi/jordmagnetism/exoplaneter. Anpassa nivå 1–2 till områdets innehåll; gör inte avancerade uppgifter artificiellt enkla genom att ge bort avgörande lösningssteg.',
 '6. Kalibrera före ommärkning: Ma4 2.576 (radianomvandling) och 4.520 (potenser av i) behöver nivåöversyn; höj inte rutinuppgifter för att få fler nivå-3-kort. Ma5 4.358 ligger under y′+ay=0 men har variabel koefficient och behöver placeringskontroll. Inga av dessa har ändrats i denna inventering.',
 '', '### Manuellt analyserade prioriteringar','']
for (c,name),note in NOTES.items():
 rr=next(r for r in rows if r['course']==c and r['name']==name)
 lines.append(f'- **{COURSES[c]} – {name}** ({sum(rr["levels"][:2])} på 1–2, {rr["levels"][2]} på 3): {note}')
lines+=['','## Alla områden','', 'N1–2 = antal spelbara kort tillsammans. H3 = skilda huvuduppgifter bakom nivå-3-korten. F3 = antal delmoment representerade på nivå 3. P1/P2 anger behov enligt mängdtrösklarna; ämnesplan, nivåkalibrering och variation ska alltid bedömas innan konstruktion.']
for c,name in COURSES.items():
 lines+=['', '### '+name,'','| Spår | Område | N1–2 | N3 | H3 | F3 | Bedömning |','|---|---|---:|---:|---:|---:|---|']
 for r in [r for r in rows if r['course']==c]:
  tracks='/'.join(str(t) for t in r['tracks'] if t) or '–'
  lines.append(f'|{tracks}|{r["name"]}|{sum(r["levels"][:2])}|{r["levels"][2]}|{r["parents3"]}|{len(r["families3"])}|{action(r)}|')
lines+=['','## Reproducerbarhet','',
 'Konsumenten: `node tools/inventera-nivaer-2026-10-25.cjs` skriver råsnapshot i /tmp. Master: `python3 tools/analysera-nivaer-2026-10-25.py /tmp/nivainventering-2026-10-25.json` skriver denna rapport och den kompakta JSON-inventeringen. Inga appdata eller rapportstatus skrivs externt.']
(ROOT/'agent/NIVAINVENTERING_2026-10-25.md').write_text('\n'.join(lines)+'\n')
print('Areas:',len(rows),'level 1–2 <20:',sum(sum(r['levels'][:2])<20 for r in rows),'level 3 <8:',sum(r['levels'][2]<8 for r in rows))
