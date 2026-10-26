"""Manuell genomgång av alla 28 uppgifter i vad_ar_diffekv."""
import json,re,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('base',ROOT/'tools/revidera-matf1-forsta-facit-2026-10-26.py');base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
D={}
def add(id,hint,steps,answer,**meta):D[id]=dict(s=base.solution(steps,answer),ledtrad='<p>'+hint+'</p>',miniräknare=True,**meta)
add('4.326',r'Vad är derivatan av en funktion som har samma värde överallt?',[
 ('Sätt derivatan till noll',r'\[0=2y-6\]'),
 ('Bestäm och kontrollera konstanten',r'\[2y=6\quad\Rightarrow\quad y=3\]<p>Derivatan av 3 är 0 och högerledet blir 2·3−6=0.</p>')],r'\(y(x)=3\).')
add('4.328',r'Lutningen är derivatan. Använd det givna x-värdet direkt i högerledet.',[
 ('Sätt in x=4 i uttrycket för lutningen',r'\[y^{\prime}=3\cdot4^2-4\]\[=3\cdot16-4=44\]'),
 ('Tolka varför svaret gäller alla lösningskurvor',r'<p>Högerledet beror bara på x. Därför har alla lösningskurvor samma lutning 44 när x=4.</p>')],r'Lutningen är 44.')
add('4.329',r'En jämvikt innebär att populationen inte ändras. Använd nollproduktmetoden på högerledet.',[
 ('Sätt förändringshastigheten till noll',r'\[0{,}20P(1-P/160)=0\]'),
 ('Låt en faktor i taget vara noll',r'<p>Faktorn 0,20 är inte noll. Därför krävs</p>\[P=0\quad\text{eller}\quad 1-P/160=0\]\[P=0\quad\text{eller}\quad P=160\]'),
 ('Kontrollera båda jämvikterna',r'<p>Vid P=0 är första faktorn noll. Vid P=160 är parentesen noll. I båda fallen blir P′=0.</p>')],r'\(P=0\) och \(P=160\).',niva='E',poang='2/0/0',traningsniva=2,spel=True,svarstyp='flera_delar',rättSvar=[0,160],självrättning=[True,True],svarFormat=['numeriskt','numeriskt'],tolerans=[0,0],svarsstruktur='mängd')
add('4.330',r'Undersök tecknet på derivatan strax över och strax under jämvikten. Leder förändringen tillbaka mot 5?',[
 ('Undersök en lösning ovanför 5',r'<p>Om y är större än 5 är y−5 positivt. Då är −3(y−5) negativt, så y minskar mot 5.</p>'),
 ('Undersök en lösning under 5',r'<p>Om y är mindre än 5 är y−5 negativt. Då är y′ positivt, så y ökar mot 5.</p>'),
 ('Sammanfatta rörelsen från båda sidor',r'<p>Små avvikelser minskar: lösningarna går tillbaka mot jämvikten när x ökar.</p>')],r'Ja, \(y=5\) är en stabil jämvikt.',traningsniva=3)
add('4.15',r'Titta efter den högsta derivatan. Undersök sedan om ett fristående högerled återstår när alla y-termer står till vänster.',[
 ('Läs av den högsta derivatan',r'<p>y″ är en andraderivata och är den högsta derivatan i ekvationen. Ordningen är därför 2.</p>'),
 ('Undersök det fristående högerledet',r'<p>Alla y-termer står till vänster, men högerledet är 4eˣ och inte 0. Den linjära ekvationen är därför inhomogen.</p>')],r'Andra ordningen och inhomogen.',formaga=['begrepp'],spel=False)
add('4.88',r'Vilken storhet är det som deriveras i ekvationen?',[
 ('Identifiera funktionen vars derivata förekommer',r'<p>T′ är derivatan av T. Det är alltså T som beror på den oberoende variabeln, vanligtvis tiden i denna temperaturmodell.</p>')],r'Den beroende variabeln är T.',svarFormat='kort_text',svarstyp='text')
add('4.16',r'Vilket tecken har temperaturskillnaden när föremålet är kallare än ugnen? Vilket tecken har derivatan när föremålet värms?',[
 ('Bestäm tecknet på temperaturskillnaden',r'\[T-180=20-180\]\[=-160\lt0\]'),
 ('Använd att temperaturen stiger',r'<p>Uppvärmning betyder T′ &gt; 0. En negativ temperaturskillnad måste alltså multipliceras med ett negativt k för att produkten ska bli positiv.</p>')],r'\(k\lt0\).',niva='E',poang='2/0/0',traningsniva=2,spel=False)
add('4.44',r'Båda ekvationerna har samma homogena del. Vilken extra funktion behövs för att vänsterledet ska bli det andra högerledet?',[
 ('Lös ekvationen med högerledet noll',r'\[r^2+4=0\quad\Rightarrow\quad r=\pm2i\]\[y_h=C_1\cos2x+C_2\sin2x\]'),
 ('Bestäm en del som ger högerledet 8 cos x',r'<p>Pröva yₚ=A cos x. Då är yₚ″=−A cos x.</p>\[y_p^{\prime\prime}+4y_p=3A\cos x\]\[3A=8\quad\Rightarrow\quad A=8/3\]'),
 ('Jämför de två lösningsfamiljerna',r'<p>Den homogena ekvationen har bara yₕ. Den inhomogena får dessutom en bestämd partikulärdel:</p>\[y=y_h+\frac83\cos x\]<p>De två fria konstanterna finns kvar i yₕ. Högerledet bestämmer den extra termen.</p>')],r'Första familjen är \(y_h\); den andra är \(y_h+(8/3)\cos x\).',spel=False)
add('4.66',r'Populationen är positiv. Då avgör den andra faktorn om högerledet är positivt eller negativt.',[
 ('Undersök positiva populationer under 500',r'<p>När 0 &lt; P &lt; 500 är både P och 500−P positiva. Därför är P′ positivt och populationen växer.</p>'),
 ('Undersök populationer över 500',r'<p>När P &gt; 500 är P positivt men 500−P negativt. Då är P′ negativt och populationen minskar.</p>'),
 ('Kontrollera gränsen mellan fallen',r'<p>Vid P=500 är P′=0: populationen är konstant.</p>')],r'Växer för \(0\lt P\lt500\), minskar för \(P\gt500\) och är konstant vid \(P=500\).',niva='E',poang='2/0/0',traningsniva=2,spel=False)
add('4.90',r'Sätt in varje y-värde. Ett positivt högerled betyder positiv derivata.',[
 ('Beräkna tecknet vid y=4',r'\[y^{\prime}=4(10-4)=24\gt0\]'),
 ('Beräkna tecknet vid y=12',r'\[y^{\prime}=12(10-12)=-24\lt0\]')],r'Positiv vid y=4 och negativ vid y=12.',spel=False,formaga=['begrepp','procedur'])
add('4.91',r'Hitta först var produkten är noll. Jämför sedan derivatans tecken strax på varje sida om dessa värden.',[
 ('Bestäm jämvikterna med nollproduktmetoden',r'\[0{,}01y(200-y)=0\]\[y=0\quad\text{eller}\quad y=200\]'),
 ('Undersök tecknen på de tre intervallen',r'<p>För y &lt; 0 är produkten negativ. För 0 &lt; y &lt; 200 är den positiv. För y &gt; 200 är den negativ.</p>'),
 ('Avgör om lösningarna går mot eller bort från jämvikten',r'<p>Nära 0 går lösningarna bort från 0: negativa värden minskar och små positiva värden ökar. Nära 200 ökar värden under 200 och minskar värden över 200.</p>')],r'\(y=0\) är instabil och \(y=200\) är stabil.',traningsniva=3,spel=False)
add('4.123',r'Bestäm först var förändringshastigheten är noll. Gör sedan en teckenanalys och följ riktningen från startvärdet.',[
 ('a) Bestäm de konstanta populationerna',r'\[0{,}5P(1-P/400)=0\]\[P=0\quad\text{eller}\quad P=400\]'),
 ('b) Undersök när populationen växer och minskar',r'<p>För 0 &lt; P &lt; 400 är båda faktorerna positiva: P′ &gt; 0 och populationen växer. För P &gt; 400 är parentesen negativ: P′ &lt; 0 och populationen minskar.</p>'),
 ('c) Följ riktningen nära jämvikterna',r'<p>Små positiva populationer växer bort från 0, så P=0 är instabil. Populationer strax under 400 ökar och populationer strax över 400 minskar. Därför är P=400 stabil.</p>'),
 ('Följ populationen som börjar vid 50',r'<p>Startvärdet ligger mellan 0 och 400. Populationen växer, men tillväxthastigheten går mot noll när P närmar sig 400. Den närmar sig 400 utan att passera jämviktslösningen.</p>')],r'a) 0 och 400. b) Växer mellan 0 och 400; minskar över 400. c) 0 är instabil, 400 stabil. Från 50 växer populationen mot 400.',niva='C',poang='2/2/0',traningsniva=3,formaga=['procedur','begrepp','resonemang'])
add('4.344',r'En jämvikt har derivatan noll. Mellan jämvikterna kan du avgöra tecknet faktor för faktor.',[
 ('Bestäm jämvikterna',r'\[0{,}12P(1-P/180)=0\]\[P=0\quad\text{eller}\quad P=180\]'),
 ('Undersök intervallet 0 < P < 180',r'<p>P är positivt och P/180 är mindre än 1. Därför är också 1−P/180 positivt. Hela produkten blir positiv.</p>')],r'Jämvikter: \(P=0\) och \(P=180\). För \(0\lt P\lt180\) är \(P^{\prime}\gt0\).',niva='E',poang='3/0/0',traningsniva=2)
add('4.346',r'Vilket värde på y gör att förändringshastigheten är noll?',[
 ('Använd att en konstant har derivatan noll',r'\[0=5-2y\]'),
 ('Lös och kontrollera',r'\[2y=5\quad\Rightarrow\quad y=2{,}5\]\[5-2\cdot2{,}5=0\]')],r'\(y(x)=2{,}5\).',traningsniva=1)
add('4.158',r'En konstant lösning har derivatan noll. När kan produkten i högerledet vara noll?',[
 ('Sätt derivatan till noll',r'\[y(4-y)=0\]'),
 ('Använd nollproduktmetoden',r'\[y=0\quad\text{eller}\quad4-y=0\]\[y=0\quad\text{eller}\quad y=4\]'),
 ('Kontrollera båda konstantfunktionerna',r'<p>Vid både y=0 och y=4 blir en faktor noll. Derivatan och högerledet är alltså båda noll.</p>')],r'\(y=0\) och \(y=4\).',spel=True,självrättning=[True,True],svarstyp='flera_delar',rättSvar=[0,4],tolerans=[0,0],svarFormat=['numeriskt','numeriskt'],svarsstruktur='mängd',formaga=['procedur','begrepp'])
add('4.159',r'Sätt in temperaturen i högerledet. Derivatans tecken visar om temperaturen stiger eller sjunker.',[
 ('Undersök temperaturen 25',r'\[T^{\prime}=-0{,}2(25-15)=-2\lt0\]<p>Temperaturen sjunker.</p>'),
 ('Undersök temperaturen 10',r'\[T^{\prime}=-0{,}2(10-15)=1\gt0\]<p>Temperaturen stiger.</p>'),
 ('Jämför riktningen i båda fallen',r'<p>Båda temperaturerna rör sig mot jämvikten 15.</p>')],r'Sjunkande vid 25 och stigande vid 10.',spel=False,formaga=['begrepp','procedur'])
add('4.351',r'Derivatan ger lutningen direkt; du behöver inte bestämma hela lösningsfunktionen.',[
 ('Använd x=4 i differentialekvationen',r'\[y^{\prime}=4^2-3=16-3=13\]'),
 ('Tolka lutningen',r'<p>Alla lösningskurvor har lutningen 13 vid x=4, eftersom högerledet inte beror på y.</p>')],r'Lutningen är 13.',traningsniva=1)
add('4.319',r'En horisontell tangent har derivatan noll. Kom ihåg vilket av x-värdena som efterfrågas.',[
 ('Sätt lutningen till noll',r'\[x^2-4=0\quad\Rightarrow\quad x^2=4\]'),
 ('Välj det positiva x-värdet',r'\[x=-2\quad\text{eller}\quad x=2\]<p>Frågan gäller det positiva värdet, alltså x=2.</p>')],r'\(x=2\).',niva='E',poang='2/0/0')
add('4.518',r'Undersök högerledet som en andragradsfunktion av y. Dess nollställen och maximipunkt svarar på olika delar av frågan.',[
 ('Bestäm de konstanta lösningarna',r'\[y(4-y)=0\]\[y=0\quad\text{eller}\quad y=4\]'),
 ('Skriv tillväxthastigheten på kvadratkompletterad form',r'\[g(y)=4y-y^2\]\[=4-(y-2)^2\]'),
 ('Skilj populationen från tillväxthastigheten',r'<p>En kvadrat är minst 0, så g är störst när y=2. Då är tillväxthastigheten g(2)=4, men frågan söker populationsvärdet 2.</p>')],r'Konstanta lösningar: 0 och 4. Snabbast tillväxt vid \(y=2\).',niva='C',poang='1/2/0',traningsniva=3,svarFormat=['numeriskt','numeriskt','numeriskt'])
add('4.577',r'Vilken är den högsta derivatan som förekommer?',[
 ('Identifiera den högsta derivatan',r'<p>y″ är andraderivatan. Ingen högre derivata finns i ekvationen, så ordningen är 2.</p>')],r'Andra ordningen.')
add('4.578',r'Jämför streck i samma kolumn och i samma rad. Var är lutningen noll?',[
 ('Undersök vad lutningen beror på',r'<p>I en lodrät kolumn har alla streck samma lutning. Höjden y ändrar alltså inte lutningen; det gör x.</p>'),
 ('Jämför tecknen till vänster och höger',r'<p>Vid x=0 är strecken vågräta. Till höger stiger de och till vänster faller de. Det stämmer med y′=x.</p>')],r'\(y^{\prime}=x\).')
add('4.579',r'En konstant lösning har vågräta tangenter. Använd både ekvationen och riktningsfältet.',[
 ('Sätt derivatan till noll',r'\[0{,}5(4-y)=0\]\[4-y=0\quad\Rightarrow\quad y=4\]'),
 ('Kontrollera i riktningsfältet',r'<p>Längs y=4 är alla streck vågräta, så en lösning kan vara kvar på den nivån.</p>')],r'\(y(x)=4\).')
add('4.580',r'Lutningen är y′. Sätt in båda koordinaterna i högerledet.',[
 ('Använd punkten (1,2)',r'\[y^{\prime}=x+y=1+2=3\]')],r'Lutningen är 3.')
add('4.581',r'Vilket tecken har produkten mellan jämvikterna? Jämför med hur den ritade kurvan utvecklas.',[
 ('Undersök tecknet från startvärdet 1',r'<p>Mellan y=0 och y=4 är båda faktorerna y och 4−y positiva. Därför växer lösningen som börjar vid 1.</p>'),
 ('Undersök vad som händer nära 4',r'<p>När y närmar sig 4 går faktorn 4−y mot noll. Lutningen går därför mot noll och kurvan planar ut mot jämvikten y=4.</p>')],r'Lösningen växer och närmar sig \(y=4\).',traningsniva=2)
add('4.582',r'Vilket tecken har derivatan ovanför respektive under den streckade linjen?',[
 ('Undersök lösningar över y=3',r'<p>y−3 är positivt, så y′=−2(y−3) är negativt. Lösningarna minskar mot 3.</p>'),
 ('Undersök lösningar under y=3',r'<p>y−3 är negativt, så y′ är positivt. Lösningarna ökar mot 3.</p>'),
 ('Sammanfatta stabiliteten',r'<p>På båda sidor rör sig lösningarna mot jämvikten när x ökar.</p>')],r'Ja, jämvikten är stabil.',traningsniva=2)
add('4.583',r'Derivera den givna funktionen och sätt in i båda leden. Likheten ska gälla för alla x.',[
 ('Derivera och sätt in y=x²',r'\[y^{\prime}=2x\]\[x\cdot2x=a x^2\]'),
 ('Jämför koefficienterna',r'<p>2x²=ax² ska gälla för alla x. Vid till exempel x=1 får vi a=2. Med a=2 stämmer likheten även vid alla andra x, inklusive x=0.</p>')],r'\(a=2\).')
add('4.584',r'Hastigheten uttrycks med en derivata. Vilket tecken behövs när teet är varmare än rummet?',[
 ('Beskriv temperaturskillnaden',r'<p>Skillnaden mellan teet och rummet är T−20. Ändringshastigheten har storleken 0,1 gånger denna skillnad när teet är varmare.</p>'),
 ('Välj tecknet som ger avsvalning',r'<p>När T &gt; 20 ska T′ vara negativt. Därför behövs ett minustecken:</p>\[T^{\prime}=-0{,}1(T-20)\]'),
 ('Kontrollera jämvikten',r'<p>Vid T=20 blir derivatan noll: temperaturen slutar ändras när teet har samma temperatur som rummet.</p>')],r'\(T^{\prime}=-0{,}1(T-20)\).',niva='E',poang='2/0/0',traningsniva=2)
PARTS=[]
for label,title,body,ans,hint in [
 ('a','Identifiera funktionen och derivatan',r'<p>Här finns den okända funktionen y och dess derivata y′. Sambandet är därför en differentialekvation.</p>','ja','Vilka symboler beskriver funktionen och dess förändring?'),
 ('b','Undersök om någon derivata förekommer',r'<p>2x+5=11 är en algebraisk ekvation för ett tal x. Den innehåller ingen derivata.</p>','nej','Vad skiljer en algebraisk ekvation från en differentialekvation?'),
 ('c','Känn igen andraderivatan',r'<p>y″ är en derivata av den okända funktionen y. En differentialekvation kan innehålla både första och högre derivator.</p>','ja','Vad betyder de två primtecknen?'),
 ('d','Skilj en given funktion från en differentialekvation',r'<p>f(x)=x² anger direkt vilken funktion f är. Det finns ingen derivata i sambandet.</p>','nej','Innehåller sambandet en derivata eller anger det bara funktionen?')]:
 PARTS.append(dict(s=base.solution([(title,body)],ans.capitalize()+'.'),ledtrad='<p>'+hint+'</p>',miniräknare=True,geogebra=False,traningsniva=1))
D['4.46']=dict(s=''.join('<h4>'+str(chr(97+i))+')</h4>'+p['s'] for i,p in enumerate(PARTS)),miniräknare=True)

def install():
 p=ROOT/'uppgiftermatf1.js';raw=p.read_text();dec=json.JSONDecoder();i=raw.index('[')+1;edits=[];seen=[]
 while True:
  while raw[i].isspace() or raw[i]==',':i+=1
  if raw[i]==']':break
  q,n=dec.raw_decode(raw[i:]);old=json.loads(json.dumps(q));id=q['id']
  if q['omr']=='vad_ar_diffekv':
   seen.append(id);q.update(D[id])
   if id=='4.344':q['t']=q['t'].replace('P<180',r'P\lt180')
   if id=='4.46':
    for part,updates in zip(q['spelDelar'],PARTS):part.update(updates)
   if id=='4.123':
    # Bilden gav tidigare bort hela teckenanalysen. Behåll den som förklaring i facit.
    match=re.search(r'<span class="fig">(<svg[\s\S]*?</svg>)</span>',q['t'])
    if match:
     svg=match.group(1);q['t']=q['t'].replace(match.group(0),'')
    else:
     match=re.search(r'<svg[\s\S]*?</svg>',old['s']);assert match;svg=match.group(0)
    svg=svg.replace('y&#8242;', 'P&#8242;').replace('x="140" y="-6"', 'x="155" y="20"').replace('>y</text>', '>P</text>').replace('y lika','P lika').replace('y =','P =').replace('y′','P′').replace("y’","P′").replace("y'","P′").replace('#999','#526173').replace('#888','#526173')
    q['s']+='<span class="fig">'+svg+'</span>'
   if id=='4.88':q['t']=r'<p>I differentialekvationen \(T^{\prime}=-0{,}2(T-20)\), vilken storhet är den beroende variabeln? Svara med dess bokstav.</p>'
   if q!=old:
    out=base.fields.replace_fields(raw[i:i+n],q)
    for k,v in q.items():
     if k not in old:out=out.rstrip()[:-1]+',\n    '+json.dumps(k,ensure_ascii=False)+': '+json.dumps(v,ensure_ascii=False)+'\n  }'
    edits.append((i,i+n,out))
  i+=n
 assert len(seen)==28 and set(seen)==set(D)
 for a,b,s in reversed(edits):raw=raw[:a]+s+raw[b:]
 p.write_text(raw);print('28 granskade,',len(edits),'ändrade.')
if __name__=='__main__':install()
