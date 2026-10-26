"""Individuellt granskade lösningar: integraler, areor och funktionsmedelvärden."""
import json,re,math,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('base',ROOT/'tools/revidera-matf1-forsta-facit-2026-10-26.py');base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
specfig=importlib.util.spec_from_file_location('figs',ROOT/'tools/matf1-area-figurer-2026-10-26.py');figs=importlib.util.module_from_spec(specfig);specfig.loader.exec_module(figs)
D={}
def add(id,hint,steps,answer,**meta):
 D[id]=dict(s=base.solution(steps,answer),ledtrad='<p>'+hint+'</p>',miniräknare=True,geogebra=False,**meta)
add('3.12',r'Börja med nollställena uttryckta med a. Mellan dem är funktionen positiv. Hur beror integralen på a?',[
 ('Bestäm områdets gränser',r'\[ax-x^2=x(a-x)=0\]<p>Nollställena är 0 och a. Eftersom a är positivt ligger grafen över x-axeln mellan dem.</p>'),
 ('Beräkna arean med a kvar i uttrycket',r'\[A=\int_0^a(ax-x^2)\,dx\]\[=\left[\frac{ax^2}{2}-\frac{x^3}{3}\right]_0^a\]\[=\frac{a^3}{2}-\frac{a^3}{3}=\frac{a^3}{6}\]'),
 ('Använd den givna arean',r'\[\frac{a^3}{6}=\frac92\quad\Rightarrow\quad a^3=27\]\[a=3\]<p>Kontroll: 3³/6=27/6=9/2.</p>')],r'\(a=3\).',typ='parameter från integralvillkor')
add('3.22',r'Bestäm områdets gränser. Vilket tecken får integralen när grafen ligger under x-axeln?',[
 ('Hitta nollställena',r'\[x^2-4x+3=0\]\[(x-1)(x-3)=0\]<p>Gränserna är x=1 och x=3. Funktionen är negativ mellan dem.</p>'),
 ('Integrera och sätt in båda gränserna',r'\[F(x)=\frac{x^3}{3}-2x^2+3x\]\[F(3)=9-18+9=0\]\[F(1)=\frac13-2+3=\frac43\]\[\int_1^3(x^2-4x+3)\,dx=0-\frac43\]'),
 ('Gör den geometriska arean positiv',r'\[A=-\left(-\frac43\right)=\frac43\]')],r'\(\frac43\) areaenheter.')
add('3.28',r'Området är en trapets. Du kan använda ändpunkternas höjder eller integrera linjens funktion.',[
 ('Bestäm trapetsens höjder och bredd',r'\[f(1)=4-1=3\]\[f(3)=4-3=1\]<p>Bredden i x-led är 3−1=2.</p>'),
 ('Beräkna trapetsens area',r'\[A=\frac{3+1}{2}\cdot2=4\]'),
 ('Kontrollera med en integral',r'\[\int_1^3(4-x)\,dx=\left[4x-\frac{x^2}{2}\right]_1^3\]\[=(12-9/2)-(4-1/2)=4\]')],r'4 areaenheter.')
add('3.206',r'Hitta en primitiv funktion till x² och sätt in de två integrationsgränserna.',[
 ('Integrera potensfunktionen',r'\[\int x^2\,dx=\frac{x^3}{3}+C\]'),
 ('Subtrahera värdet vid den undre gränsen',r'\[\int_0^4x^2\,dx=\left[\frac{x^3}{3}\right]_0^4\]\[=\frac{4^3}{3}-\frac{0^3}{3}=\frac{64}{3}\]')],r'\(\frac{64}{3}\).')
add('3.208',r'Ett funktionsmedelvärde är integralens värde delat med intervallets längd.',[
 ('Beräkna integralen över hela intervallet',r'\[\int_0^4 4x^2\,dx=\left[\frac{4x^3}{3}\right]_0^4\]\[=\frac{4\cdot64}{3}-0=\frac{256}{3}\]'),
 ('Dividera med intervallets längd',r'\[f_{\text{medel}}=\frac{1}{4-0}\cdot\frac{256}{3}\]\[=\frac{64}{3}\]')],r'\(\frac{64}{3}\).')
add('3.210',r'Beräkna först A(t). Undersök därefter om funktionen kan anta samma värde vid två positiva t.',[
 ('Uttryck integralen som en funktion av t',r'\[A(t)=\left[x^2\right]_0^t=t^2\]'),
 ('Lös ekvationen och använd t:s tecken',r'\[t^2=2\quad\Rightarrow\quad t=\pm\sqrt2\]<p>Villkoret t positivt lämnar bara t=√2.</p>'),
 ('Motivera att ingen annan positiv lösning finns',r'\[A^{\prime}(t)=2t\gt0\quad\text{för }t\gt0\]<p>A är strikt växande för positiva t och kan därför inte få värdet 2 mer än en gång.</p>')],r'\(t=\sqrt2\), den enda positiva lösningen.')
add('3.49',r'Bestäm nollställena. Parabeln är symmetrisk kring y-axeln, vilket kan förenkla beräkningen.',[
 ('Bestäm integrationsgränserna',r'\[4-x^2=0\quad\Rightarrow\quad x=\pm2\]<p>Grafen ligger ovanför x-axeln mellan dessa punkter.</p>'),
 ('Beräkna halva arean',r'\[\int_0^2(4-x^2)\,dx=\left[4x-\frac{x^3}{3}\right]_0^2\]\[=8-\frac83=\frac{16}{3}\]'),
 ('Använd symmetrin',r'\[A=2\cdot\frac{16}{3}=\frac{32}{3}\approx10{,}67\]')],r'\(\frac{32}{3}\approx10{,}67\) areaenheter.',svarstyp='numeriskt',svarFormat='numeriskt',rättSvar=32/3,tolerans=0,traningsniva=2)
add('3.50',r'Beräkna integralen och dividera sedan med intervallets längd. Medelvärdet är inte samma sak som värdet i intervallets mitt.',[
 ('Beräkna integralens värde',r'\[\int_0^3x^2\,dx=\left[\frac{x^3}{3}\right]_0^3=9\]'),
 ('Fördela integralvärdet över intervallet',r'\[f_{\text{medel}}=\frac{9}{3-0}=3\]<p>Som jämförelse är f(1,5)=2,25. För en böjd graf behöver mittpunktens funktionsvärde inte vara medelvärdet.</p>')],r'Medelvärdet är 3.',svarstyp='numeriskt',svarFormat='numeriskt',rättSvar=3,tolerans=0,självrättning=True,spel=True,traningsniva=2)
add('3.51',r'Lös ekvationen där kurvorna möts. Integrera därefter den övre funktionens värde minus den undres.',[
 ('Bestäm skärningspunkternas x-värden',r'\[x^2=x+2\]\[(x-2)(x+1)=0\]<p>Gränserna är −1 och 2. Linjen ligger över parabeln mellan dem, till exempel ger x=0 värdena 2 respektive 0.</p>'),
 ('Integrera höjdskillnaden',r'\[A=\int_{-1}^2(x+2-x^2)\,dx\]\[F(x)=\frac{x^2}{2}+2x-\frac{x^3}{3}\]'),
 ('Sätt in båda gränserna',r'\[F(2)=2+4-\frac83=\frac{10}{3}\]\[F(-1)=\frac12-2+\frac13=-\frac76\]\[A=\frac{10}{3}-\left(-\frac76\right)=\frac92\]')],r'\(\frac92=4{,}5\) areaenheter.',svarstyp='numeriskt',svarFormat='numeriskt',rättSvar=4.5,tolerans=0,niva='C',poang='0/2/0',traningsniva=3)
add('3.70',r'Var skär linjen de två koordinataxlarna? Vilken geometrisk figur avgränsar de?',[
 ('Bestäm axelskärningarna',r'<p>Vid x=0 är y=6. Vid y=0 gäller</p>\[6-2x=0\quad\Rightarrow\quad x=3\]'),
 ('Beräkna triangelns area',r'<p>Den rätvinkliga triangeln har basen 3 och höjden 6.</p>\[A=\frac{3\cdot6}{2}=9\]')],r'9 areaenheter.')
add('3.71',r'Integrera term för term. Var noga med minustecknet framför värdet vid den undre gränsen.',[
 ('Bestäm en primitiv funktion',r'\[F(x)=\frac{x^4}{4}+4x\]'),
 ('Beräkna ändpunktsvärdena',r'\[F(2)=\frac{16}{4}+8=12\]\[F(-2)=\frac{16}{4}-8=-4\]'),
 ('Subtrahera det undre värdet',r'\[\int_{-2}^2(x^3+4)\,dx\]\[=12-(-4)=16\]<p>Kontroll: x³ är udda och dess bidrag tar ut varandra på det symmetriska intervallet. Konstanten 4 ger 4·4=16.</p>')],r'16.',traningsniva=2)
add('3.219',r'Integralens värde ska delas med intervallets längd för att ge ett medelvärde.',[
 ('Beräkna integralen',r'\[\int_0^4x^3\,dx=\left[\frac{x^4}{4}\right]_0^4\]\[=\frac{256}{4}-0=64\]'),
 ('Dividera med längden 4',r'\[f_{\text{medel}}=\frac{64}{4-0}=16\]')],r'16.',traningsniva=2,tolerans=0)
add('3.73',r'Integrera först med a som övre gräns. Vilken av ekvationens lösningar är positiv?',[
 ('Uttryck integralen med a',r'\[\int_0^a2x\,dx=\left[x^2\right]_0^a=a^2\]'),
 ('Lös villkoret och välj positiv rot',r'\[a^2=25\quad\Rightarrow\quad a=\pm5\]<p>Eftersom a ska vara positivt väljer vi a=5.</p>')],r'\(a=5\).',niva='E',poang='2/0/0')
add('3.80',r'Bestäm var grafen byter sida om x-axeln. Dela upp arean där och använd gärna symmetrin.',[
 ('Dela vid nollställena',r'\[x^2-1=0\quad\Rightarrow\quad x=\pm1\]<p>Grafen ligger under x-axeln mellan −1 och 1, men över den på de två yttre delarna.</p>'),
 ('Beräkna arean under x-axeln',r'\[A_{\text{mitt}}=\int_{-1}^1(1-x^2)\,dx\]\[=\left[x-\frac{x^3}{3}\right]_{-1}^1\]\[=\frac23-\left(-\frac23\right)=\frac43\]'),
 ('Beräkna de två lika stora yttre areorna',r'\[A_{\text{yttre}}=2\int_1^2(x^2-1)\,dx\]\[=2\left[\frac{x^3}{3}-x\right]_1^2\]\[=2\left(\frac23-\left(-\frac23\right)\right)=\frac83\]'),
 ('Addera positiva areor',r'\[A=\frac43+\frac83=4\]<p>Den vanliga integralen över hela intervallet skulle dra bort mittarean och ger därför inte den geometriska arean.</p>')],r'4 areaenheter.')
add('3.224',r'Beräkna integralen med t kvar som gräns. Använd sedan kravet att t är positivt.',[
 ('Integrera och använd areavillkoret',r'\[\int_0^t4x\,dx=\left[2x^2\right]_0^t=2t^2\]\[2t^2=5\quad\Rightarrow\quad t^2=\frac52\]'),
 ('Ta den positiva roten',r'\[t=\sqrt{\frac52}=\frac{\sqrt{10}}2\]<p>Den negativa roten uppfyller inte villkoret t positivt.</p>')],r'\(t=\frac{\sqrt{10}}2\).',traningsniva=2)
add('3.53',r'Vilket geometriskt område hör till en bestämd integral när funktionen är positiv?',[
 ('Identifiera grafen och gränserna',r'<p>Funktionen e⁻ˣ² är positiv. Integralen gäller området under grafen y=e⁻ˣ², ovanför x-axeln, från x=0 till x=2.</p>'),
 ('Tolka talet som en area',r'<p>Eftersom grafen ligger ovanför x-axeln är integralvärdet också områdets geometriska area. Värdet är redan givet och behöver inte beräknas igen.</p>')],r'Området under \(y=e^{-x^2}\) mellan x=0 och x=2 har arean cirka 0,8821 areaenheter.')
add('3.75',r'En derivata anger förändring per tidsenhet i ett visst ögonblick. Tolka både tecknet och enheten.',[
 ('Tolka argumentet och minustecknet',r'<p>f′(2) beskriver förändringen vid tiden t=2 minuter. Minustecknet betyder att temperaturen sjunker.</p>'),
 ('Tolka storleken med rätt enhet',r'<p>Förändringshastigheten är då cirka 3,7 °C per minut nedåt. Det är en momentan hastighet, inte temperaturändringen under hela de två första minuterna.</p>')],r'Efter 2 minuter sjunker temperaturen med cirka 3,7 °C/min just då.')
A84=base.solution([
 ('Sätt kurvornas värden lika',r'\[x^2=2x\quad\Rightarrow\quad x(x-2)=0\]<p>Alltså är x=0 eller x=2.</p>'),
 ('Beräkna de tillhörande y-värdena',r'\[y(0)=0,\qquad y(2)=2\cdot2=4\]')],r'\((0,0)\) och \((2,4)\).')
B84=base.solution([
 ('Bestäm gränserna och övre kurvan',r'<p>Kurvorna möts vid x=0 och x=2. Mellan dem är 2x−x²=x(2−x) positivt, så linjen ligger över parabeln.</p>'),
 ('Integrera skillnaden',r'\[A=\int_0^2(2x-x^2)\,dx\]\[=\left[x^2-\frac{x^3}{3}\right]_0^2\]'),
 ('Sätt in gränserna',r'\[A=\left(4-\frac83\right)-0=\frac43\]')],r'\(\frac43\approx1{,}33\) areaenheter.')
add('3.84',r'Börja med skärningspunkterna. Integrera sedan skillnaden mellan den övre och den undre kurvan.',[],r'Se respektive del.')
D['3.84']['s']='<h4>a) Skärningspunkter</h4>'+A84+'<h4>b) Area</h4>'+B84
add('3.102',r'För en linjär funktion ändras värdet jämnt mellan ändpunkterna. Du kan också använda integralens medelvärdesformel.',[
 ('Bestäm värdena i intervallets ändpunkter',r'\[f(0)=1,\qquad f(3)=7\]'),
 ('Ta medelvärdet av ändpunkterna',r'<p>Eftersom funktionen är linjär är funktionsmedelvärdet</p>\[\frac{1+7}{2}=4\]'),
 ('Kontrollera med integralen',r'\[\frac13\int_0^3(2x+1)\,dx=\frac13\left[x^2+x\right]_0^3\]\[=\frac{12}{3}=4\]')],r'4.',svarstyp='numeriskt',svarFormat='numeriskt',rättSvar=4,tolerans=0,självrättning=True,spel=True)
add('3.103',r'Vilken av funktionerna har störst värde mellan 0 och 1? Integrera skillnaden.',[
 ('Välj övre minus undre funktion',r'<p>För x mellan 0 och 1 är x minst lika stort som x². Områdets höjd är därför x−x².</p>'),
 ('Integrera höjdskillnaden',r'\[A=\int_0^1(x-x^2)\,dx\]\[=\left[\frac{x^2}{2}-\frac{x^3}{3}\right]_0^1\]\[=\frac12-\frac13=\frac16\]')],r'\(\frac16\approx0{,}167\) areaenheter.',svarstyp='numeriskt',svarFormat='numeriskt',rättSvar=1/6,tolerans=0,självrättning=True,spel=True,traningsniva=2)
add('3.104',r'Låt k vara kvar när du bestämmer skärningspunkter och area. Sätt sedan areauttrycket lika med det givna värdet.',[
 ('Bestäm gränserna med k',r'\[x^2=kx\quad\Rightarrow\quad x(x-k)=0\]<p>Gränserna är 0 och k. Linjen ligger över parabeln mellan dem eftersom k är positivt.</p>'),
 ('Uttryck arean som en funktion av k',r'\[A=\int_0^k(kx-x^2)\,dx\]\[=\left[\frac{kx^2}{2}-\frac{x^3}{3}\right]_0^k\]\[=\frac{k^3}{2}-\frac{k^3}{3}=\frac{k^3}{6}\]'),
 ('Använd areavillkoret',r'\[\frac{k^3}{6}=\frac43\quad\Rightarrow\quad k^3=8\]\[k=2\]')],r'\(k=2\).',traningsniva=3)
add('3.285',r'Både integralens övre gräns och intervallets längd beror på a.',[
 ('Beräkna medelvärdet med a kvar',r'\[f_{\text{medel}}=\frac1a\int_0^a x^2\,dx\]\[=\frac1a\left[\frac{x^3}{3}\right]_0^a=\frac{a^2}{3}\]'),
 ('Använd det givna medelvärdet',r'\[\frac{a^2}{3}=12\quad\Rightarrow\quad a^2=36\]<p>a är positivt, så a=6. Kontroll: integralen är 72 och 72/6=12.</p>')],r'\(a=6\).',niva='C',poang='0/2/0',traningsniva=3,svarFormat='numeriskt')
add('3.288',r'Bestäm skärningspunkterna. Skriv rotfunktionen som en potens när du integrerar.',[
 ('Bestäm gränserna',r'\[\sqrt x=\frac x2\]<p>Båda leden är icke-negativa för x≥0, så vi kan kvadrera:</p>\[x=\frac{x^2}{4}\quad\Rightarrow\quad x(x-4)=0\]<p>x=0 och x=4 uppfyller även den ursprungliga ekvationen.</p>'),
 ('Integrera övre minus undre kurva',r'<p>Rotkurvan ligger över linjen mellan skärningspunkterna.</p>\[A=\int_0^4\left(x^{1/2}-\frac x2\right)\,dx\]\[=\left[\frac23x^{3/2}-\frac{x^2}{4}\right]_0^4\]'),
 ('Beräkna det exakta värdet',r'\[A=\frac23\cdot8-\frac{16}{4}-0\]\[=\frac{16}{3}-4=\frac43\]')],r'\(\frac43\) areaenheter.',niva='C',poang='0/3/0',traningsniva=3,svarstyp='bråk',svarFormat='bråk',rättSvar='4/3',tolerans=0)
add('3.347',r'Vilken funktion har derivatan eˣ? Använd sedan sambandet mellan exponentialfunktionen och ln.',[
 ('Integrera exponentialfunktionen',r'\[\int_0^{\ln3}e^x\,dx=\left[e^x\right]_0^{\ln3}\]'),
 ('Använd de exakta ändpunktsvärdena',r'\[e^{\ln3}-e^0=3-1=2\]')],r'2.')
add('3.348',r'Sträckan fås genom att summera hastigheten över tiden med en integral.',[
 ('Välj tidsintervall och integrand',r'<p>Under de första två sekunderna går t från 0 till 2. Hastigheten är icke-negativ, så integralen ger tillryggalagd sträcka.</p>\[s=\int_0^2 3t^2\,dt\]'),
 ('Integrera och sätt in tiderna',r'\[s=\left[t^3\right]_0^2=2^3-0^3=8\]<p>Enheten blir (m/s)·s=m.</p>')],r'8 m.',traningsniva=2)
add('3.349',r'Sinus är icke-negativ på intervallet. Vilken funktion har derivatan sin x?',[
 ('Skriv arean som en integral',r'<p>Grafen ligger över x-axeln mellan 0 och π, så</p>\[A=\int_0^\pi\sin x\,dx\]'),
 ('Integrera och använd cosinusvärdena',r'\[A=\left[-\cos x\right]_0^\pi\]\[=-\cos\pi-(-\cos0)\]\[=-(-1)-(-1)=2\]')],r'2 areaenheter.')
add('3.350',r'Dividera temperaturens integral med tidsintervallets längd. Tänk på den inre derivatan när du integrerar sinusuttrycket.',[
 ('Skriv medelvärdesintegralen',r'\[T_{\text{medel}}=\frac1{12}\int_0^{12}T(t)\,dt\]<p>Intervallets längd är 12 timmar. Vi integrerar hela det givna temperaturuttrycket.</p>'),
 ('Bestäm en primitiv funktion',r'\[F(t)=20t-\frac{48}{\pi}\cos\frac{\pi t}{12}\]<p>Faktorn 12/π kompenserar för den inre derivatan π/12.</p>'),
 ('Beräkna integralens värde',r'\[F(12)=240+\frac{48}{\pi}\]\[F(0)=-\frac{48}{\pi}\]\[F(12)-F(0)=240+\frac{96}{\pi}\]'),
 ('Dividera med 12 och avrunda sist',r'\[T_{\text{medel}}=20+\frac8\pi\]\[\approx22{,}54648\ ^\circ\mathrm C\]')],r'Medeltemperaturen är cirka 22,5 °C.',rättSvar=20+8/math.pi,tolerans=.05,traningsniva=3,niva='C',poang='0/2/0')
add('3.351',r'Beräkna en trapets för varje intilliggande par i tabellen. Alla trapetser har bredden 1.',[
 ('Dela upp intervallet i tre trapetser',r'<p>För en trapets är arean bredden gånger medelvärdet av de två funktionsvärdena.</p>'),
 ('Beräkna bidragen från tabellen',r'\[A_1=1\cdot\frac{2+3}{2}=2{,}5\]\[A_2=1\cdot\frac{3+5}{2}=4\]\[A_3=1\cdot\frac{5+8}{2}=6{,}5\]'),
 ('Addera uppskattningarna',r'\[\int_0^3 f(x)\,dx\approx2{,}5+4+6{,}5\]\[=13\]<p>Det är en approximation eftersom vi ersätter grafen med räta sträckor mellan tabellpunkterna.</p>')],r'Integralen uppskattas till 13.')
add('3.352',r'Vilken funktion har derivatan 1/x för positiva x? Använd de exakta logaritmvärdena vid gränserna.',[
 ('Integrera på det positiva intervallet',r'\[\int_1^e\frac1x\,dx=\left[\ln x\right]_1^e\]'),
 ('Sätt in gränserna',r'\[\ln e-\ln1=1-0=1\]')],r'1.')

def install():
 p=ROOT/'uppgiftermatf1.js';raw=p.read_text();dec=json.JSONDecoder();i=raw.index('[')+1;edits=[];seen=[]
 while i<len(raw):
  while i<len(raw) and (raw[i].isspace() or raw[i]==','):i+=1
  if raw[i]!= '{':break
  q,n=dec.raw_decode(raw[i:]);old=json.loads(json.dumps(q));id=q['id']
  if id in D:
   seen.append(id);q.update(D[id])
   q['t']=q['t'].replace('t>0',r't\gt0').replace('k>0',r'k\gt0').replace('a&gt;0',r'a\gt0')
   if id in figs.SPECS:
    q['t']=re.sub(r'<span class="fig" data-review-area="[^"]+">[\s\S]*?</svg></span>', '', q['t'])+figs.figure(id)
   if id=='3.84':
    q['spelDelning']='deluppgifter'
    q['t']=re.sub(r'<text[^>]*>\(2, 4\)</text>', '', q['t'])
    intro=q['t'].split('<ol type="a">')[0]
    q['spelIntro']=intro
    q['spelDelar']=[dict(etikett='a',fraga='Bestäm skärningspunkterna.',t=intro+'<p>Bestäm skärningspunkterna.</p>',s=A84,ledtrad='<p>Lös ekvationen där funktionerna har samma värde. Beräkna sedan tillhörande y-värden.</p>',svarstyp='flera_delar',rättSvar=['(0,0)','(2,4)'],svarFormat=['punkt','punkt'],självrättning=[True,True],svarsstruktur='mängd',svarEtiketter=['Skärningspunkt','Skärningspunkt'],miniräknare=True,geogebra=False,niva='E',poang='2/0/0',traningsniva=2),dict(etikett='b',fraga='Beräkna områdets area.',t=intro+'<p>Beräkna områdets area.</p>',s=B84,ledtrad='<p>Bestäm kurvornas skärningspunkter och integrera övre funktion minus undre funktion mellan dem.</p>',svarstyp='numeriskt',rättSvar=4/3,svarFormat='numeriskt',självrättning=True,tolerans=0,miniräknare=True,geogebra=False,niva='E',poang='2/0/0',traningsniva=2)]
    q['svarFormat']=[['punkt','punkt'],'numeriskt'];q['rättSvar']=[['(0,0)','(2,4)'],4/3]
   if q!=old:
    out=base.fields.replace_fields(raw[i:i+n],q)
    for k,v in q.items():
     if k not in old:out=out.rstrip()[:-1]+',\n    '+json.dumps(k,ensure_ascii=False)+': '+json.dumps(v,ensure_ascii=False)+'\n  }'
    edits.append((i,i+n,out))
  i+=n
 assert set(seen)==set(D) and len(seen)==29
 for a,b,s in reversed(edits):raw=raw[:a]+s+raw[b:]
 p.write_text(raw);print('29 granskade,',len(edits),'ändrade.')
if __name__=='__main__':install()
