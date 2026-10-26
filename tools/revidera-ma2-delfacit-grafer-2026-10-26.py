"""23 grafuppgifter: manuellt författade 57 delfacit efter visuell grafkontroll."""
import json,re,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('first',Path(__file__).with_name('revidera-ma2-delfacit-2026-10-26.py'));first=importlib.util.module_from_spec(spec);spec.loader.exec_module(first)
# Rubrik, förklaring/beräkning, svarsrad och ledtråd är skrivna för varje enskild del.
D={
'2.385':[
('Sök grafens båda skärningar med höjden 3',r'<p>Följ den vågräta nivån y = 3. Den skär vänstra grenen vid x = −2 och högra grenen vid x = 2. Det är dessa argument som ger funktionsvärdet 3.</p>',r'\(a=-2\) och \(a=2\).','Utgå från höjden 3 på y-axeln. Finns det mer än en punkt på grafen på den höjden?'),
('Låt x + 1 vara argumentet som läses av i grafen',r'<p>Funktionsvärdet är 3 vid argumenten −2 och 2. Därför måste</p>\[x+1=-2\quad\text{eller}\quad x+1=2.\]<p>Subtrahera 1 i båda ekvationerna.</p>\[x=-3\quad\text{eller}\quad x=1\]',r'\(x=-3\) och \(x=1\).','Läs först vilka argument som ger höjden 3. Hela uttrycket x + 1 ska vara lika med något av dem.')],
'2.387':[
('Läs höjden vid tiden 3 sekunder',r'<p>Vid t = 3 ligger grafen på höjden 5. Det betyder att föremålet befinner sig 5 meter högt 3 sekunder efter start.</p>',r'Höjden är \(5\) m efter \(3\) s.','Tiden läses längs den vågräta axeln och höjden längs den lodräta. Följ tiden 3 upp till kurvan.'),
('Läs båda tiderna då kurvan har höjden 3 meter',r'<p>Den vågräta nivån H = 3 skär kurvan en gång på väg upp och en gång på väg ner. Avläsningen ger t = 1 och t = 5.</p>',r'\(t=1\) s och \(t=5\) s.','Följ höjden 3 meter vågrätt genom grafen. Kurvan kan nå samma höjd vid mer än en tid.')],
'2.393':[
('Läs grafens höjd när x = 3',r'<p>Följ x = 3 upp till parabeln. Skärningspunkten har y-koordinaten 5, alltså f(3) = 5.</p>',r'\(f(3)=5\).','Börja vid 3 på x-axeln och läs höjden där du träffar grafen.'),
('Sök alla argument som ger den givna höjden 5',r'<p>Den vågräta linjen y = 5 skär parabeln vid x = −1 och x = 3. Båda uppfyller ekvationen.</p>',r'\(x=-1\) och \(x=3\).','Sök båda skärningarna med samma vågräta nivå. Parabelns två sidor kan ge två lösningar.'),
('Sätt x + 2 lika med argumenten på höjden 5',r'<p>Grafen har höjden 5 vid argumenten −1 och 3. Därför gäller</p>\[x+2=-1\quad\text{eller}\quad x+2=3.\]<p>Subtraktion av 2 ger x = −3 respektive x = 1.</p>',r'\(x=-3\) och \(x=1\).','Vilka argument ger funktionsvärdet 5? Sätt sedan hela uttrycket x + 2 lika med dem.')],
'2.395':[
('Läs argumentet som ger höjden 2 och dra sedan bort 1',r'<p>Grafen ger f(2) = 2. För att f(x + 1) ska bli 2 behöver därför argumentet x + 1 vara 2.</p>\[x+1=2\quad\Rightarrow\quad x=1\]',r'\(x=1\).','Bestäm först vilket argument som ger värdet 2. Argumentet här är x + 1.'),
('Sätt argumentet 2x lika med grafens nollställe',r'<p>Grafen skär x-axeln vid argumentet 4. Därför gäller</p>\[2x=4\quad\Rightarrow\quad x=2.\]',r'\(x=2\).','Läs först var grafen har höjden noll. Det avlästa värdet är 2x, inte x.')],
'2.397':[
('Läs funktionsvärdet vid x = 2',r'<p>Vid x = 2 ligger linjen på höjden 3. Därför är f(2) = 3.</p>',r'\(f(2)=3\).','Följ x = 2 lodrätt till linjen och läs y-koordinaten.'),
('Sätt det givna inre värdet i den yttre funktionen',r'<p>Det är g som ska användas på värdet 3.</p>\[g(f(2))=g(3)=2\cdot3-3=3\]',r'\(g(f(2))=3\).','Börja med den innersta funktionen. Det givna värdet ska sedan sättas in som argument till g.'),
('Läs först vilket argument till f som ger 4',r'<p>Grafen visar f(3) = 4. Alltså måste g(x) = 3.</p>\[2x-3=3\]\[2x=6\quad\Rightarrow\quad x=3\]',r'\(x=3\).','Läs vilket argument till f som ger höjden 4. Hela g(x) måste vara lika med det argumentet.')],
'2.401':[
('Använd formeln vid x = 4',r'\[f(4)=4^2+2=16+2=18\]',r'\(f(4)=18\).','Funktionsformeln gäller även utanför den del av grafen som visas.'),
('Sätt funktionsvärdet till 18 och behåll båda rötterna',r'\[x^2+2=18\]\[x^2=16\]<p>Både −4 och 4 har kvadraten 16.</p>',r'\(x=-4\) och \(x=4\).','Sätt formeln lika med 18. Kom ihåg att både positiva och negativa tal kan ha samma kvadrat.')],
'2.402':[
('Läs skärningen med y-axeln',r'<p>x = 0 ligger på y-axeln. Där skär linjen vid y = 4, så f(0) = 4.</p>',r'\(f(0)=4\).','Var ligger x = 0 i koordinatsystemet?'),
('Läs linjens höjd vid x = 2',r'<p>Vid x = 2 ligger grafen på x-axeln. Höjden är därför noll.</p>',r'\(f(2)=0\).','Följ x = 2 till linjen. Vilken y-koordinat har en punkt på x-axeln?'),
('Sök x-koordinaten på höjden 6',r'<p>Den vågräta nivån y = 6 skär linjen vid x = −1. Ekvationen efterfrågar x-koordinaten, inte höjden.</p>',r'\(x=-1\).','Börja vid 6 på y-axeln, gå vågrätt till linjen och läs sedan x.')],
'2.404':[
('Läs grafens lägsta punkt vid x = 1',r'<p>V-formens spets ligger i punkten (1, 1). Därför är f(1) = 1.</p>',r'\(f(1)=1\).','Läs höjden vid den givna x-koordinaten 1.'),
('Läs den högra grenens höjd vid x = 4',r'<p>Vid x = 4 träffar vi grafen på höjden y = 4. Alltså är f(4) = 4.</p>',r'\(f(4)=4\).','Följ x = 4 lodrätt till den högra grenen.'),
('Sök höjden 3 på båda sidor av spetsen',r'<p>Nivån y = 3 skär vänstra grenen vid x = −1 och högra grenen vid x = 3.</p>',r'\(x=-1\) och \(x=3\).','Kontrollera båda grenarna när du söker argumenten till ett givet funktionsvärde.')],
'2.411':[
('Läs två funktionsvärden och subtrahera i rätt ordning',r'<p>Grafen visar f(2) = 2,5 och f(0) = 1,5. Därför blir</p>\[f(2)-f(0)=2{,}5-1{,}5=1.\]',r'Skillnaden är \(1\).','Läs först av varje funktionsvärde för sig. Subtrahera sedan i den ordning som står i frågan.'),
('Läs argumentet där grafen har höjden 2',r'<p>Kurvan når y = 2 vid x = 1. Den är nästan vågrät där men sammanfaller inte med nivån över ett intervall.</p>',r'\(x=1\).','Följ nivån y = 2 till kurvan och läs den vågräta koordinaten.')],
'2.413':[
('Beräkna det inre värdet och använd det som nytt argument',r'\[f(0)=0^2-1=-1\]\[f(f(0))=f(-1)\]\[=(-1)^2-1=0\]',r'\(f(f(0))=0\).','Arbeta inifrån och ut. Resultatet från den första funktionsberäkningen blir argument i nästa.'),
('Använd formeln två gånger',r'\[f(2)=2^2-1=3\]\[f(f(2))=f(3)=3^2-1=8\]<p>Formeln behövs eftersom det andra argumentet, 3, ligger utanför den visade grafens intervall.</p>',r'\(f(f(2))=8\).','Beräkna först f(2). Du kan sedan behöva formeln eftersom nästa argument ligger utanför bildens intervall.')],
'2.414':[
('Läs den högra parabelgrenens höjd vid x = 2',r'<p>Vid x = 2 har grafen y-koordinaten 3. Därför är f(2) = 3.</p>',r'\(f(2)=3\).','Följ x = 2 upp till parabeln.'),
('Läs den vänstra parabelgrenens höjd vid x = −2',r'<p>Vid x = −2 har grafen y-koordinaten 3. Därför är f(−2) = 3.</p>',r'\(f(-2)=3\).','Läs av på den vänstra sidan av y-axeln.'),
('Nollställena är skärningarna med x-axeln',r'<p>Höjden noll motsvarar x-axeln. Parabeln skär den vid x = −1 och x = 1.</p>',r'\(x=-1\) och \(x=1\).','Sök alla punkter på grafen med y-koordinaten noll.')],
'2.416':[
('Läs linjens höjd vid x = 2',r'<p>Vid x = 2 ligger linjen på höjden 4. Därför är f(2) = 4.</p>',r'\(f(2)=4\).','Börja på x-axeln vid 2 och läs sedan höjden på linjen.'),
('Läs linjens höjd vid x = −3',r'<p>Vid x = −3 ligger grafen en enhet under x-axeln, på höjden −1.</p>',r'\(f(-3)=-1\).','Funktionsvärdet kan vara negativt när linjen ligger under x-axeln.'),
('Sök argumentet som ger höjden 5',r'<p>Linjen når y = 5 vid x = 3. Ekvationen f(x) = 5 har därför lösningen x = 3.</p>',r'\(x=3\).','Börja vid höjden 5, gå till linjen och läs sedan x-koordinaten.')],
'2.419':[
('Beräkna de två funktionsvärdena innan de subtraheras',r'\[f(1)=2\cdot1-1=1\]\[g(1)=-1+5=4\]\[f(1)-g(1)=1-4=-3\]',r'Skillnaden är \(-3\).','Beräkna f(1) och g(1) var för sig. Ordningen i subtraktionen är viktig.'),
('Sätt de två linjernas uttryck lika',r'\[2x-1=-x+5\]\[3x=6\quad\Rightarrow\quad x=2\]<p>Det stämmer med x-koordinaten för grafernas skärningspunkt.</p>',r'\(x=2\).','Linjerna har samma funktionsvärde i sin skärningspunkt.'),
('Ersätt argumentet i f innan du ställer upp ekvationen',r'\[f(x+1)=2(x+1)-1\]\[=2x+1\]\[2x+1=-x+5\]\[3x=4\quad\Rightarrow\quad x=\frac43\]',r'\(x=4/3\).','Hela x + 1 ersätter x i f. Sätt sedan det nya uttrycket lika med g(x).')],
'2.420':[
('Läs punkten på grafen där x = 1',r'<p>Linjen går genom punkten (1, 1). Alltså är f(1) = 1.</p>',r'\(f(1)=1\).','Läs höjden där grafen passerar x = 1.'),
('Använd formeln för ett argument utanför bilden',r'\[f(4)=2\cdot4-1=8-1=7\]',r'\(f(4)=7\).','Grafbilden visar bara en del av funktionen. Funktionsuttrycket går fortfarande att använda.')],
'2.421':[
('Läs av båda höjderna och beräkna skillnaden',r'<p>Grafen visar f(2) = 6 och f(−1) = 1,5.</p>\[f(2)-f(-1)=6-1{,}5=4{,}5\]',r'Skillnaden är \(4{,}5\).','Notera rutnätets skala och läs varje funktionsvärde separat.'),
('Argumentet x + 2 ska ge höjden 2,5',r'<p>Kurvan har värdet 2,5 vid argumentet 1. Därför gäller</p>\[x+2=1\quad\Rightarrow\quad x=-1.\]',r'\(x=-1\).','Läs argumentet som ger höjden 2,5. Det avlästa talet motsvarar x + 2.')],
'2.425':[
('Läs grafens höjd på y-axeln',r'<p>Vid x = 0 ligger grafen i punkten (0, 2). Därför är f(0) = 2.</p>',r'\(f(0)=2\).','x = 0 motsvarar y-axeln.'),
('Läs den högra toppens höjd',r'<p>Vid x = 2 når grafen höjden 5. Det ger f(2) = 5.</p>',r'\(f(2)=5\).','Gå från x = 2 till grafen och läs y-värdet.'),
('Kontrollera alla linjestycken på höjden 5',r'<p>Nivån y = 5 når endast den högra toppen, vars x-koordinat är 2. Inget annat linjestycke når den höjden.</p>',r'\(x=2\).','Följ samma vågräta höjd genom hela den visade grafen, inte bara ett linjestycke.')],
'2.427':[
('Läs linjens y-koordinat vid x = 2',r'<p>Linjen går genom (2, 4), så f(2) = 4.</p>',r'\(f(2)=4\).','Läs y-värdet som hör till x = 2.'),
('Läs linjen till vänster om y-axeln',r'<p>Vid x = −3 ligger punkten på y = −1, vilket ger f(−3) = −1.</p>',r'\(f(-3)=-1\).','Leta upp −3 på x-axeln och följ den lodräta riktningen till linjen.'),
('Sök x-koordinaten vid funktionsvärdet 5',r'<p>Linjen skär nivån y = 5 vid x = 3. Här är det argumentet som efterfrågas.</p>',r'\(x=3\).','Börja med y-värdet när ekvationen anger f(x).')],
'2.429':[
('Läs V-formens spets vid x = 1',r'<p>Spetsen ligger på höjden 1. Alltså är f(1) = 1.</p>',r'\(f(1)=1\).','Hitta den punkt på grafen som har x-koordinaten 1.'),
('Läs båda skärningarna med y = 3',r'<p>Grafens två grenar skär höjden 3 vid x = −1 respektive x = 3.</p>',r'\(x=-1\) och \(x=3\).','Samma funktionsvärde kan förekomma på båda sidor av spetsen.')],
'2.430':[
('Läs grafens höjd vid x = 1',r'<p>Linjen går genom punkten (1, 2). Därför är f(1) = 2.</p>',r'\(f(1)=2\).','Gå från x = 1 till linjen och läs höjden.'),
('Beräkna värdet med formeln även utanför bildens intervall',r'\[f(4)=3\cdot4-1=12-1=11\]',r'\(f(4)=11\).','Använd funktionsformeln när punkten inte finns med i den visade delen av grafen.')],
'2.431':[
('Läs kurvans skärning med y-axeln',r'<p>Vid x = 0 är kurvans höjd 1. Alltså är f(0) = 1.</p>',r'\(f(0)=1\).','x = 0 ligger på den lodräta axeln.'),
('Läs kurvans höjd vid x = 2',r'<p>Vid x = 2 passerar kurvan höjden 3, så f(2) = 3.</p>',r'\(f(2)=3\).','Följ x = 2 upp till kurvan och sedan vågrätt mot y-axeln.')],
'2.434':[
('Läs kurvans höjd vid x = −1',r'<p>Punkten på kurvan har koordinaterna (−1, 1). Därför är f(−1) = 1.</p>',r'\(f(-1)=1\).','Utgå från −1 på x-axeln.'),
('Läs kurvans höjd vid x = 1',r'<p>Kurvan passerar punkten (1, 3), vilket ger f(1) = 3.</p>',r'\(f(1)=3\).','Läs den lodräta koordinaten där kurvan passerar x = 1.'),
('Sök argumentet på höjden 2',r'<p>Kurvan passerar nivån y = 2 vid x = 0. Det är där ekvationen f(x) = 2 är uppfylld.</p>',r'\(x=0\).','När funktionsvärdet är givet börjar du med en vågrät nivå i koordinatsystemet.')],
'2.437':[
('Läs den vänstra grenens höjd vid x = −2',r'<p>Vid x = −2 har parabeln höjden 4. Därför är f(−2) = 4.</p>',r'\(f(-2)=4\).','Gå till den vänstra parabelgrenen vid x = −2.'),
('Läs parabelns lägsta punkt vid x = 0',r'<p>Parabelns lägsta punkt ligger i origo (0, 0). Därför är f(0) = 0.</p>',r'\(f(0)=0\).','Origo har både x-koordinaten och y-koordinaten noll.'),
('Höjden 4 nås på båda sidor om y-axeln',r'<p>Nivån y = 4 skär parabeln vid x = −2 och x = 2. Båda är lösningar.</p>',r'\(x=-2\) och \(x=2\).','Kontrollera både den vänstra och högra grenen när du söker alla lösningar.')],
'2.439':[
('Läs linjens skärning med y-axeln',r'<p>Linjen skär y-axeln vid y = 1. Därför är f(0) = 1.</p>',r'\(f(0)=1\).','Var i koordinatsystemet ligger alla punkter med x = 0?'),
('Läs argumentet som ger höjden 3',r'<p>Linjen når y = 3 vid x = −1. Därför löser x = −1 ekvationen.</p>',r'\(x=-1\).','Gå vågrätt från höjden 3 till linjen och läs x-koordinaten.')]
}
def install():
 p=ROOT/'uppgifterma2.js';raw=p.read_text()
 for id,rows in D.items():
  pos=re.search(r'"id"\s*:\s*"'+re.escape(id)+'"',raw).start();start=raw.rfind('{',0,pos);q,n=json.JSONDecoder().raw_decode(raw[start:]);assert len(rows)==len(q['spelDelar'])
  for part,(title,body,answer,hint) in zip(q['spelDelar'],rows):part['s']=first.solution([(title,body)],answer);part['ledtrad']='<p>'+hint+'</p>'
  q['ledtrad']='<p>'+rows[0][3]+'</p>'
  q['s']='<div class="facit-v2 facit-stegvis">'+''.join('<div class="facit-del"><span class="facit-mark">'+part['etikett']+')</span><div class="facit-arbete">'+part['s']+'</div></div>' for part in q['spelDelar'])+'</div>'
  if id=='2.395':q['s']+='<p>c) Läs först vilket argument som ger det efterfrågade funktionsvärdet. Sätt uttrycket inne i parentesen lika med argumentet och lös ekvationen.</p>'
  if id=='2.413':q['s']+='<p>c) Formeln behövs eftersom det andra argumentet är 3 och grafbilden bara visar −2 ≤ x ≤ 2.</p>'
  if id=='2.387':
   for part in q['spelDelar']:part['t']='<p>Grafen visar höjden H(t) i meter, t sekunder efter start.</p>'+part['t'] if not part['t'].startswith('<p>Grafen visar höjden') else part['t']
   q['spelDelar'][0].update({'rättSvar':5,'svarFormat':'numeriskt','svarEnhet':'m','självrättning':True})
   q['spelDelar'][1]['svarEnhet']='s'
  if id=='2.393':q['spelDelar'][1]['t']=q['spelDelar'][1]['t'].replace('<p>Bestäm alla',r'<p>Det är givet att \(f(3)=5\). Bestäm alla') if 'Det är givet' not in q['spelDelar'][1]['t'] else q['spelDelar'][1]['t']
  if id=='2.397':q['spelDelar'][1]['t']=q['spelDelar'][1]['t'].replace('<p>Bestäm',r'<p>Det är givet att \(f(2)=3\). Bestäm') if 'Det är givet' not in q['spelDelar'][1]['t'] else q['spelDelar'][1]['t']
  raw=raw[:start]+first.fields.replace_fields(raw[start:start+n],q)+raw[start+n:]
 p.write_text(raw)
if __name__=='__main__':install();print(len(D),'huvuduppgifter,',sum(map(len,D.values())),'delfacit omarbetade.')
