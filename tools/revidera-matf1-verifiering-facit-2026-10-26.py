"""Manuellt författade lösningar till områdets 29 uppgifter, inte mallrubriker."""
import json,re,importlib.util
from pathlib import Path
from html import escape
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('fields',Path(__file__).with_name('revidera-ma3-facitstruktur-2026-10-25.py'));fields=importlib.util.module_from_spec(spec);spec.loader.exec_module(fields)
D={}
def add(id,hint,steps,answer,**meta):
 s='<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'+''.join('<li><p class="facit-rubrik">'+escape(h)+'</p>'+b+'</li>' for h,b in steps)+'</ol><p class="facit-svar"><strong>Svar:</strong> '+answer+'</p></div>'
 D[id]=dict(s=s,ledtrad='<p>'+hint+'</p>',**meta)
add('4.14',r'Derivera funktionen med kedjeregeln. Vad blir summan av derivatan och två gånger funktionen?',[
 ('Derivera den föreslagna lösningen',r'\[y^{\prime}=4(-2)e^{-2x}=-8e^{-2x}\]'),
 ('Sätt in i differentialekvationens vänsterled',r'\[y^{\prime}+2y=-8e^{-2x}+2\cdot4e^{-2x}\]\[=-8e^{-2x}+8e^{-2x}=0\]')],r'Ja. Vänsterledet blir 0 för alla x, så \(y=4e^{-2x}\) löser ekvationen.',traningsniva=2,formaga=['procedur','begrepp'])
add('4.327',r'C är en konstant när du deriverar. Jämför sedan derivatan med högerledet i ekvationen.',[
 ('Derivera med C som konstant',r'\[y=Ce^{2x}\quad\Rightarrow\quad y^{\prime}=2Ce^{2x}\]'),
 ('Beräkna högerledet med samma funktion',r'\[2y=2Ce^{2x}\]<p>Detta är samma uttryck som derivatan. Vi behövde inte välja något särskilt värde på C; även C=0 fungerar.</p>')],r'\(y=Ce^{2x}\) löser \(y^{\prime}=2y\) för varje konstant C.')
add('4.36',r'Derivera två gånger. Behåll parentesen runt hela y-uttrycket när du subtraherar y.',[
 ('Beräkna båda derivatorna',r'\[y^{\prime}=2e^x,\qquad y^{\prime\prime}=2e^x\]<p>Den konstanta termen 3 försvinner vid derivering.</p>'),
 ('Subtrahera hela funktionen',r'\[y^{\prime\prime}-y=2e^x-(2e^x+3)\]\[=2e^x-2e^x-3=-3\]')],r'Ja. Vänsterledet blir −3 för alla x, precis som ekvationen kräver.',formaga=['procedur','begrepp'])
add('4.64',r'Kedjeregeln ger en faktor 3 vid varje derivering. Vilket tecken får den andra derivatan?',[
 ('Derivera sinus två gånger',r'\[y^{\prime}=3\cos(3x)\]\[y^{\prime\prime}=3(-\sin(3x))\cdot3\]\[=-9\sin(3x)\]'),
 ('Sätt in funktionen och andraderivatan',r'\[y^{\prime\prime}+9y\]\[=-9\sin(3x)+9\sin(3x)\]\[=0\]')],r'\(y=\sin(3x)\) löser ekvationen för alla x.',formaga=['procedur','begrepp'])
add('4.89',r'Derivera exponentialtermen. Multiplicera sedan båda termerna i y med 3 innan du summerar.',[
 ('Beräkna derivatan',r'\[y^{\prime}=2(-3)e^{-3x}=-6e^{-3x}\]'),
 ('Sätt in hela y-uttrycket',r'\[y^{\prime}+3y\]\[=-6e^{-3x}+3(4+2e^{-3x})\]\[=-6e^{-3x}+12+6e^{-3x}=12\]')],r'Ja. Vänsterledet är 12 för alla x.',formaga=['procedur','begrepp'])
add('4.160',r'Derivera lösningsfamiljen. Hur kan du ersätta exponentialtermen med ett uttryck som innehåller y?',[
 ('Isolera exponentialtermen och derivera',r'\[y-3=Ce^{-2x}\]\[y^{\prime}=-2Ce^{-2x}\]'),
 ('Eliminera konstanten C ur sambandet',r'<p>Ersätt Ce⁻²ˣ med y−3:</p>\[y^{\prime}=-2(y-3)=-2y+6\]'),
 ('Kontrollera att hela lösningsfamiljen blir den givna',r'<p>Sätt z=y−3. Ekvationen blir z′=−2z, vars allmänna lösning är z=Ce⁻²ˣ. Därmed får vi precis y=Ce⁻²ˣ+3.</p>')],r'Till exempel \(y^{\prime}=-2y+6\), ekvivalent med \(y^{\prime}+2y=6\).')
add('4.161',r'Använd produktregeln vid båda deriveringarna. Bryt sedan ut exponentialfaktorn efter insättning.',[
 ('Beräkna första derivatan med produktregeln',r'\[y^{\prime}=e^x+xe^x=(x+1)e^x\]'),
 ('Använd produktregeln en gång till',r'\[y^{\prime\prime}=e^x+(x+1)e^x\]\[=(x+2)e^x\]'),
 ('Sätt in och samla termerna',r'\[y^{\prime\prime}-2y^{\prime}+y\]\[=(x+2)e^x-2(x+1)e^x+xe^x\]\[=[x+2-2(x+1)+x]e^x\]\[=(x+2-2x-2+x)e^x=0\]')],r'\(y=xe^x\) löser differentialekvationen för alla x.',niva='E',poang='3/0/0',traningsniva=2,formaga=['procedur','begrepp'])
add('4.320',r'Använd kedjeregeln för exponentialfunktionen. Vilken faktor multipliceras hela y-uttrycket med?',[
 ('Derivera funktionen',r'\[y^{\prime}=5(-0{,}2)e^{-0{,}2x}\]\[=-0{,}2\,(5e^{-0{,}2x})\]'),
 ('Jämför med ky',r'\[y^{\prime}=-0{,}2y\]<p>Faktorn framför y är därför k=−0,2.</p>')],r'\(k=-0{,}2\).',niva='E',poang='2/0/0',miniräknare=True)
add('4.321',r'Differentialekvationen gäller även vid x=0. Använd det givna funktionsvärdet där.',[
 ('Sätt in startvärdet direkt',r'\[y^{\prime}(0)=3y(0)=3\cdot4=12\]<p>Du behöver inte bestämma hela funktionen y(x).</p>')],r'\(y^{\prime}(0)=12\).',niva='E',poang='1/0/0',miniräknare=True)
add('4.72',r'Derivera familjen och använd ursprungsuttrycket för att få bort C. Skriv sedan svaret på den efterfrågade formen.',[
 ('Derivera och skriv om exponentialtermen',r'\[y^{\prime}=-5Ce^{-5x}\]\[Ce^{-5x}=y-3\]'),
 ('Ersätt exponentialtermen och utveckla parentesen',r'\[y^{\prime}=-5(y-3)=-5y+15\]'),
 ('Kontrollera lösningsfamiljen',r'<p>Ekvationen kan skrivas (y−3)′=−5(y−3). Därför är y−3=Ce⁻⁵ˣ, vilket ger den efterfrågade familjen.</p>')],r'\(y^{\prime}=-5y+15\), alltså \(a=-5\) och \(b=15\).')
add('4.144',r'Derivera först. Räkna sedan ut högerledet separat med parentes runt hela funktionen.',[
 ('Beräkna vänsterledet',r'\[y^{\prime}=-2Ce^{-2x}\]'),
 ('Beräkna högerledet',r'\[-2y+10\]\[=-2(Ce^{-2x}+5)+10\]\[=-2Ce^{-2x}-10+10\]\[=-2Ce^{-2x}\]'),
 ('Jämför uttrycken för alla C',r'<p>Båda leden är −2Ce⁻²ˣ. Likheten gäller för varje x och varje konstant C, även C=0.</p>')],r'Alla funktioner \(y=Ce^{-2x}+5\) löser differentialekvationen.')
add('4.76',r'Vilken typ av karakteristisk rot ger både en exponentialterm och x gånger samma exponentialterm?',[
 ('Läs av den karakteristiska dubbelroten',r'<p>Lösningsfamiljen innehåller både e⁴ˣ och xe⁴ˣ. Det motsvarar en dubbelrot r=4.</p>'),
 ('Bygg det karakteristiska polynomet',r'\[(r-4)^2=r^2-8r+16\]'),
 ('Översätt polynomet till en differentialekvation',r'<p>r² motsvarar y″, r motsvarar y′ och konstanttermen multiplicerar y.</p>\[y^{\prime\prime}-8y^{\prime}+16y=0\]<p>Dubbelroten 4 ger den allmänna lösningen (C₁+C₂x)e⁴ˣ, precis som i frågan.</p>')],r'Till exempel \(y^{\prime\prime}-8y^{\prime}+16y=0\).')
add('4.78',r'Vilken realdel och vilken imaginärdel av de karakteristiska rötterna motsvarar exponentialfaktorn respektive svängningen?',[
 ('Läs av de två komplexa rötterna',r'<p>Faktorn e²ˣ ger realdelen 2. Sinus och cosinus med argumentet 3x ger imaginärdelarna ±3.</p>\[r=2+3i\quad\text{och}\quad r=2-3i\]'),
 ('Multiplicera rotfaktorerna',r'\[(r-2-3i)(r-2+3i)\]\[=(r-2)^2-(3i)^2\]\[=(r-2)^2+9=r^2-4r+13\]'),
 ('Skriv differentialekvationen',r'\[y^{\prime\prime}-4y^{\prime}+13y=0\]<p>Dess två karakteristiska rötter ger exakt den lösningsfamilj som står i frågan.</p>')],r'Till exempel \(y^{\prime\prime}-4y^{\prime}+13y=0\).')
add('4.514',r'Derivera båda exponentialtermerna. Vilka termer tar ut varandra när y adderas?',[
 ('Derivera med C som konstant',r'\[y^{\prime}=2e^{2x}-Ce^{-x}\]'),
 ('Addera hela funktionen y',r'\[y^{\prime}+y\]\[=2e^{2x}-Ce^{-x}+e^{2x}+Ce^{-x}\]\[=3e^{2x}\]'),
 ('Jämför faktorerna framför e²ˣ',r'\[3e^{2x}=ae^{2x}\]<p>Exponentialfaktorn är aldrig noll. Division med den ger a=3.</p>')],r'\(a=3\).',svarFormat='numeriskt',tolerans=0)
add('4.522',r'Använd först villkoret för y(0). Derivera sedan produkten för att kunna använda villkoret för y′(0).',[
 ('Använd funktionsvärdet vid noll',r'\[y(0)=(C_1+C_2\cdot0)e^0=C_1\]\[C_1=1\]'),
 ('Derivera produkten',r'\[y^{\prime}=C_2e^{2x}+2(C_1+C_2x)e^{2x}\]'),
 ('Använd lutningen vid noll',r'\[y^{\prime}(0)=C_2+2C_1=3\]\[C_2+2=3\quad\Rightarrow\quad C_2=1\]'),
 ('Kontrollera de två villkoren',r'<p>Funktionen blir y=(1+x)e²ˣ. Då är y(0)=1 och y′(x)=(3+2x)e²ˣ, så y′(0)=3.</p>')],r'\(C_1=1\) och \(C_2=1\).',niva='E',traningsniva=2,poang='3/0/0',svarFormat=['numeriskt','numeriskt'],tolerans=[0,0])
add('4.569',r'Derivera med C som konstant. Multiplicera sedan hela y-uttrycket med 3.',[
 ('Derivera funktionen',r'\[y^{\prime}=-3Ce^{-3x}\]'),
 ('Sätt in i vänsterledet',r'\[y^{\prime}+3y\]\[=-3Ce^{-3x}+3(Ce^{-3x}+2)\]\[=-3Ce^{-3x}+3Ce^{-3x}+6=6\]')],r'\(a=6\).')
add('4.570',r'Kedjeregeln ger en faktor k. Jämför med högerledet och förkorta den gemensamma exponentialfaktorn.',[
 ('Derivera och sätt in',r'\[y^{\prime}=5ke^{kx},\qquad4y=20e^{kx}\]\[5ke^{kx}=20e^{kx}\]'),
 ('Dividera med en faktor som aldrig är noll',r'<p>Eftersom 5eᵏˣ &gt; 0 får vi dividera båda leden med den faktorn.</p>\[k=4\]')],r'\(k=4\).')
add('4.571',r'Derivera x² och den konstanta termen var för sig. Jämför sedan koefficienten framför x.',[
 ('Derivera och jämför för alla x',r'\[y^{\prime}=2x+0=2x\]<p>Detta ska vara ax för alla x. Koefficienterna måste därför vara lika.</p>')],r'\(a=2\).')
add('4.572',r'Var noga med minustecknet framför hela y när du bildar y′−y.',[
 ('Beräkna derivatan',r'\[y^{\prime}=Ce^x+1\]'),
 ('Subtrahera funktionen och samla termerna',r'\[y^{\prime}-y=Ce^x+1-(Ce^x+x)\]\[=Ce^x+1-Ce^x-x=-x+1\]'),
 ('Jämför med ax+b',r'<p>Koefficienten framför x är −1 och konstanttermen är 1. Likheten ska gälla för alla x.</p>')],r'\(a=-1\) och \(b=1\).',niva='E',traningsniva=2,poang='2/0/0')
add('4.573',r'Sätt in x=0 i differentialekvationen och använd det givna värdet på y(0).',[
 ('Beräkna derivatan direkt från sambandet',r'\[y^{\prime}(0)=2y(0)+1\]\[=2\cdot3+1=7\]<p>Hela lösningen y(x) behöver inte bestämmas.</p>')],r'\(y^{\prime}(0)=7\).')
add('4.574',r'Använd produktregeln två gånger. Efter insättning ska uttrycket bli noll oavsett hur C och D väljs.',[
 ('Derivera två gånger',r'\[y^{\prime}=De^x+(C+Dx)e^x\]\[=(C+D+Dx)e^x\]\[y^{\prime\prime}=De^x+(C+D+Dx)e^x\]\[=(C+2D+Dx)e^x\]'),
 ('Sätt in och dividera med eˣ',r'\[C+2D+Dx\]\[{}+a(C+D+Dx)\]\[{}+b(C+Dx)=0\]<p>Samla koefficienterna:</p>\[(1+a+b)(C+Dx)\]\[{}+(2+a)D=0\]'),
 ('Använd att C och D får väljas fritt',r'<p>C=1 och D=0 ger 1+a+b=0. Med det villkoret återstår (2+a)D=0. Eftersom även D=1 ska fungera får vi 2+a=0.</p>\[a=-2,\qquad1-2+b=0\]\[b=1\]'),
 ('Kontrollera hela familjen',r'<p>När a=−2 och b=1 är båda koefficienterna i det samlade uttrycket noll. Därför gäller ekvationen för alla C, D och x.</p>')],r'\(a=-2\) och \(b=1\).')
add('4.575',r'Använd kedjeregeln vid båda deriveringarna. Ekvationen ska gälla för alla x, inte bara där cosinus råkar vara noll.',[
 ('Derivera cosinus två gånger',r'\[y^{\prime}=-k\sin(kx)\]\[y^{\prime\prime}=-k^2\cos(kx)\]'),
 ('Sätt in och jämför koefficienterna',r'\[y^{\prime\prime}+25y=(25-k^2)\cos(kx)\]<p>För att detta ska vara noll för alla x måste 25−k²=0. Till exempel är cosinusfaktorn 1 vid x=0.</p>'),
 ('Använd villkoret på k',r'\[k^2=25\quad\Rightarrow\quad k=\pm5\]<p>Eftersom k &gt; 0 väljer vi den positiva roten.</p>')],r'\(k=5\).')
add('4.576',r'Efter insättning ska vänsterledet vara samma konstant för alla x. Vad måste då hända med exponentialtermen?',[
 ('Derivera och sätt in funktionen',r'\[y^{\prime}=-6e^{-2x}\]\[y^{\prime}+ay\]\[=-6e^{-2x}+a(3e^{-2x}+4)\]\[=(-6+3a)e^{-2x}+4a\]'),
 ('Ta bort beroendet av x',r'<p>Exponentialtermen varierar med x. Dess koefficient måste därför vara noll när hela uttrycket ska vara konstant.</p>\[-6+3a=0\quad\Rightarrow\quad a=2\]'),
 ('Beräkna den återstående konstanten',r'\[b=4a=4\cdot2=8\]')],r'\(a=2\) och \(b=8\).')
add('4.585',r'Använd startvärdet i differentialekvationen. Ska lösningen först öka eller minska?',[
 ('Bestäm lutningen i startpunkten',r'\[y^{\prime}(0)=-y(0)=-2\]<p>Alla kurvor går genom (0,2), men bara A har negativ lutning där. B och C ökar och kan därför inte vara lösningen.</p>'),
 ('Kontrollera den valda kurvan',r'<p>A är kurvan y=2e⁻ˣ.</p>\[y^{\prime}=-2e^{-x}=-y\]\[y(0)=2e^0=2\]<p>Både differentialekvationen och startvillkoret stämmer.</p>')],r'Kurva A.')
add('4.586',r'Beräkna tangentens lutning från de två markerade punkterna. Använd den som y′(0) i ekvationen.',[
 ('Bestäm lutningen i startpunkten',r'\[y^{\prime}(0)=\frac{6-2}{1-0}=4\]'),
 ('Sätt in lutningen och funktionsvärdet',r'\[4=k(10-2)=8k\]'),
 ('Lös ekvationen för k',r'\[k=\frac48=0{,}5\]')],r'\(k=0{,}5\).',traningsniva=2,poang='2/0/0',formaga=['procedur','begrepp'])
add('4.587',r'Kontrollera varje funktion genom att derivera och jämföra leden. Likheten måste gälla för alla x.',[
 ('Pröva y=x²',r'\[y^{\prime}=2x\]\[xy^{\prime}=2x^2=2y\]<p>Funktionen löser ekvationen.</p>'),
 ('Pröva y=3x²',r'\[y^{\prime}=6x\]\[xy^{\prime}=6x^2=2y\]<p>Även denna funktion löser ekvationen.</p>'),
 ('Pröva y=x²+1',r'\[xy^{\prime}=2x^2,\qquad2y=2x^2+2\]<p>Leden skiljer sig med 2. Funktionen löser inte ekvationen.</p>'),
 ('Pröva y=x³',r'\[xy^{\prime}=3x^3,\qquad2y=2x^3\]<p>Likheten gäller bara vid x=0, inte på ett helt intervall. Funktionen är därför inte en lösning.</p>')],r'\(y=x^2\) och \(y=3x^2\).',traningsniva=2,poang='2/0/0')
add('4.588',r'Derivera varje förslag två gånger. Kontrollera både tecknet och faktorn framför den ursprungliga funktionen.',[
 ('Pröva sinus med argumentet 3x',r'\[y^{\prime}=3\cos(3x)\]\[y^{\prime\prime}=-9\sin(3x)=-9y\]<p>Detta förslag stämmer.</p>'),
 ('Pröva cosinus med argumentet 3x',r'\[y^{\prime}=-3\sin(3x)\]\[y^{\prime\prime}=-9\cos(3x)=-9y\]<p>Även detta förslag stämmer.</p>'),
 ('Pröva exponentialfunktionen',r'\[y^{\prime}=3e^{3x},\qquad y^{\prime\prime}=9e^{3x}\]<p>Det ger 9y, med fel tecken.</p>'),
 ('Pröva sinus med argumentet 9x',r'\[y^{\prime}=9\cos(9x)\]\[y^{\prime\prime}=-81\sin(9x)=-81y\]<p>Här blir faktorn −81, inte −9.</p>')],r'\(y=\sin(3x)\) och \(y=\cos(3x)\).')
add('4.589',r'Vad blir exponentialfaktorn vid x=0? Använd sedan det givna startvärdet.',[
 ('Använd startvillkoret',r'\[y(0)=Ce^0-1=C-1\]\[C-1=3\quad\Rightarrow\quad C=4\]'),
 ('Kontrollera startvärdet',r'\[4e^0-1=4-1=3\]<p>Det är redan givet att familjen löser differentialekvationen. Det som återstod var att välja rätt C.</p>')],r'\(C=4\).')
add('4.590',r'Derivera exponentialfunktionen två gånger. Faktorn eᵏˣ är aldrig noll, vilket gör att du kan förkorta den.',[
 ('Beräkna derivatorna',r'\[y^{\prime}=ke^{kx},\qquad y^{\prime\prime}=k^2e^{kx}\]'),
 ('Sätt in och bryt ut exponentialfaktorn',r'\[y^{\prime\prime}-y^{\prime}-6y\]\[=k^2e^{kx}-ke^{kx}-6e^{kx}\]\[=(k^2-k-6)e^{kx}\]'),
 ('Lös ekvationen för k',r'<p>Eftersom eᵏˣ aldrig är noll måste</p>\[k^2-k-6=0\]\[(k-3)(k+2)=0\]'),
 ('Kontrollera båda värdena',r'\[3^2-3-6=0\]\[(-2)^2-(-2)-6=0\]<p>Båda värdena ger noll för alla x i den ursprungliga differentialekvationen.</p>')],r'\(k=-2\) eller \(k=3\).',traningsniva=2,poang='2/0/0',formaga=['procedur','begrepp'])

def install():
 p=ROOT/'uppgiftermatf1.js';raw=p.read_text();dec=json.JSONDecoder();i=raw.index('[')+1;edits=[];ids=[]
 while True:
  while raw[i].isspace() or raw[i]==',':i+=1
  if raw[i]==']':break
  q,n=dec.raw_decode(raw[i:]);old=json.loads(json.dumps(q));id=q['id']
  if q['omr']=='verifiering':
   assert id in D,id;q.update(D[id]);ids.append(id)
   if id=='4.160':q['t']=q['t'].replace('en första ordningens differentialekvation','en differentialekvation av formen \\(y^{\\prime}=ay+b\\), med konstanta a och b,')
   if id=='4.76':q['t']=r'<p>Ställ upp en homogen differentialekvation av andra ordningen med konstanta koefficienter vars allmänna lösning är \\(y=(C_1+C_2x)e^{4x}\\).</p>'.replace('\\\\','\\')
   if id=='4.78':q['t']=q['t'].replace('en homogen differentialekvation med konstantkoefficienter','en homogen differentialekvation av andra ordningen med konstanta koefficienter')
   if id=='4.587':q['alternativ'][3]['kommentar']='Leden blir 3x³ och 2x³. De är bara lika vid x=0, inte på ett helt intervall.'
   if q!=old:
    source=raw[i:i+n];out=fields.replace_fields(source,q)
    for k,v in q.items():
     if k not in old:out=out.rstrip()[:-1]+',\n    '+json.dumps(k,ensure_ascii=False)+': '+json.dumps(v,ensure_ascii=False)+'\n  }'
    edits.append((i,i+n,out))
  i+=n
 assert len(ids)==29
 for a,b,s in reversed(edits):raw=raw[:a]+s+raw[b:]
 p.write_text(raw);print('29 granskade,',len(edits),'ändrade.')
if __name__=='__main__':install()
