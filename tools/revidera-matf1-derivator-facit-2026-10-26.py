"""Manuellt författad revision av hela repetition_derivator, 27 uppgifter."""
import json, math, re, importlib.util
from pathlib import Path
from html import escape
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('fields',Path(__file__).with_name('revidera-ma3-facitstruktur-2026-10-25.py'));fields=importlib.util.module_from_spec(spec);spec.loader.exec_module(fields)
D={}
def sol(steps,answer):
 return '<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'+''.join('<li><p class="facit-rubrik">'+escape(h)+'</p>'+b+'</li>' for h,b in steps)+'</ol><p class="facit-svar"><strong>Svar:</strong> '+answer+'</p></div>'
def add(id,hint,steps,answer,**meta):D[id]=dict(s=sol(steps,answer),ledtrad='<p>'+hint+'</p>',**meta)
add('3.207',r'Vilket värde har derivatan när tangenten är horisontell? Tänk på att en kvadratekvation kan ha två lösningar.',[
 ('Derivera funktionen',r'\[f^{\prime}(x)=3x^2-9\]'),
 ('Sätt lutningen lika med noll',r'\[3x^2-9=0\]\[3x^2=9\quad\Rightarrow\quad x^2=3\]'),
 ('Ta med både den positiva och den negativa roten',r'\[x=-\sqrt3\quad\text{eller}\quad x=\sqrt3\]<p>Båda ger derivatan 3·3−9=0.</p>')],r'\(x=-\sqrt3\) och \(x=\sqrt3\).',rättSvar=[-math.sqrt(3),math.sqrt(3)],svarFormat=['numeriskt','numeriskt'],tolerans=[1e-10,1e-10],svarsstruktur='mängd',svarEtiketter=['x','x'],miniräknare=True)
add('3.209',r'Jämför grafen till vänsterledet med den vågräta linjen på höjden 8. Läs av skärningens x-koordinat med fler decimaler än slutsvaret ska ha.',[
 ('Välj två grafer att jämföra',r'<p>Skriv in funktionerna i GeoGebra:</p>\[f(x)=xe^x,\qquad g(x)=8\]<p>Använd verktyget för skärning mellan graferna.</p>'),
 ('Läs av och avrunda x-koordinaten',r'\[x\approx1{,}605811996\ldots\]<p>Den fjärde decimalen är 8, så tre decimaler ger 1,606.</p>'),
 ('Kontrollera lösningen och att ingen saknas',r'\[1{,}605811996\,e^{1{,}605811996}\approx8\]<p>För x ≤ 0 är vänsterledet högst noll. För x &gt; 0 är derivatan eˣ(1+x) positiv. Därför finns bara en lösning.</p>')],r'\(x\approx1{,}606\).',tolerans=.0005,niva='E',traningsniva=2,poang='2/0/0',formaga=['procedur'])
add('3.212',r'En horisontell tangent har lutningen noll. Derivera först och lös sedan ekvationen för lutningen.',[
 ('Beräkna tangentens lutning som funktion av x',r'\[f^{\prime}(x)=3x^2-12\]'),
 ('Lös ekvationen för horisontell tangent',r'\[3x^2-12=0\]\[x^2=4\quad\Rightarrow\quad x=\pm2\]')],r'\(x=-2\) och \(x=2\).',svarsstruktur='mängd',svarEtiketter=['x','x'],tolerans=[0,0],miniräknare=True)
add('3.52',r'Låt det högra övre hörnets x-koordinat vara x. Hur kan du skriva bredden och höjden med samma variabel?',[
 ('Beskriv bredd, höjd och tillåtna x-värden',r'<p>Symmetrin ger bredden 2x. Höjden är 9−x².</p>\[0\lt x\lt3\]<p>Utanför detta intervall får vi ingen rektangel med positiv bredd och höjd.</p>'),
 ('Skriv och derivera arean',r'\[A(x)=2x(9-x^2)=18x-2x^3\]\[A^{\prime}(x)=18-6x^2\]'),
 ('Hitta och kontrollera maximum',r'\[18-6x^2=0\quad\Rightarrow\quad x=\sqrt3\]<p>Den negativa roten ligger utanför intervallet. Derivatan är positiv före √3 och negativ efter √3. Arean ökar alltså först och minskar sedan.</p>'),
 ('Beräkna den största arean',r'\[A(\sqrt3)=2\sqrt3(9-3)=12\sqrt3\]\[\approx20{,}7846\]')],r'Den största arean är \(12\sqrt3\approx20{,}8\) areaenheter.',rättSvar=12*math.sqrt(3),svarFormat='numeriskt',svarstyp='numeriskt',tolerans=1e-10,typ='optimering av inskriven rektangel')
add('3.29',r'Lös först ekvationen där derivatan är noll. Undersök sedan derivatans tecken på båda sidor om dessa x-värden.',[
 ('a) Bestäm var derivatan är noll',r'\[3x^2-6=0\]\[x^2=2\quad\Rightarrow\quad x=\pm\sqrt2\]'),
 ('b) Undersök tecknet mellan och utanför nollställena',r'<p>Derivatan 3x²−6 är positiv när x² &gt; 2 och negativ när x² &lt; 2.</p><p>Alltså är derivatan positiv till vänster om −√2 och till höger om √2, men negativ mellan dessa värden.</p>'),
 ('b) Ange de växande intervallen',r'\[x\le-\sqrt2\quad\text{eller}\quad x\ge\sqrt2\]<p>Ändpunkterna kan ingå i de växande intervallen, trots att derivatan är noll just där. Vill man bara ange var derivatan är positiv använder man i stället strikta olikheter.</p>')],r'a) \(x=\pm\sqrt2\). b) Funktionen är växande på \(( -\infty,-\sqrt2]\) och \([\sqrt2,\infty)\).',traningsniva=2,poang='3/0/0')
add('3.227',r'Rita vänsterledet och jämför med höjden 6. Logaritmen begränsar vilka x-värden som är tillåtna.',[
 ('Ange definitionsmängden och välj grafer',r'<p>Logaritmen kräver x &gt; 0. Skriv in följande i GeoGebra och använd skärningsverktyget:</p>\[f(x)=x+\ln x,\qquad g(x)=6\]'),
 ('Läs av lösningen och kontrollera den',r'\[x\approx4{,}496664173\ldots\]\[f(4{,}496664173)\approx6\]'),
 ('Kontrollera att det inte finns fler lösningar',r'\[f^{\prime}(x)=1+\frac1x\gt0\quad(x\gt0)\]<p>Funktionen är strängt växande i hela definitionsmängden och kan därför skära den vågräta linjen högst en gång.</p>')],r'\(x\approx4{,}49666\).',tolerans=1e-10,niva='E',traningsniva=2,poang='2/0/0',formaga=['procedur'])
add('3.54',r'Pröva elevens påstående med ett negativt tal. Kan en kvadratrot bli negativ?',[
 ('Skilj en kvadratrot från lösningarna till en ekvation',r'<p>Symbolen √ anger den icke-negativa kvadratroten. Därför gäller</p>\[\sqrt{x^2}=|x|.\]'),
 ('Visa ett motexempel till elevens påstående',r'\[\sqrt{(-2)^2}=\sqrt4=2\ne-2\]<p>Påståendet √(x²)=x stämmer alltså inte för negativa x.</p>'),
 ('Förklara varför CAS ändå ger två lösningar',r'\[|x|=2\]\[x=-2\quad\text{eller}\quad x=2\]<p>Båda x-värdena ger kvadratroten 2. CAS-resultatet innebär inte att kvadratroten själv kan vara −2.</p>')],r'Eleven blandar ihop \(\sqrt{x^2}=|x|\) med \(\sqrt{x^2}=x\). Det senare gäller bara för \(x\ge0\).')
add('3.74',r'Sätt in närmevärdet i vänsterledet. Kontrollera också ett värde strax under och ett strax över det föreslagna nollstället.',[
 ('Beräkna hur nära noll vänsterledet blir',r'\[f(1{,}521)=1{,}521^3-1{,}521-2\]\[=-0{,}002256239\]<p>Värdet ligger nära noll, vilket stödjer närmevärdet.</p>'),
 ('Kontrollera ett teckenbyte i ett litet intervall',r'\[f(1{,}521)\lt0\]\[f(1{,}522)\approx0{,}00369\gt0\]<p>Polynomfunktionen är kontinuerlig. Det finns därför en rot mellan 1,521 och 1,522.</p>'),
 ('Avgränsa vad kontrollen visar',r'<p>Detta visar att 1,521 ligger nära en rot. Ett teckenbyte mellan enbart 1 och 2 hade gett en mycket grövre kontroll.</p>')],r'Insättning ger ett värde nära noll, och ett teckenbyte mellan 1,521 och 1,522 bekräftar att närmevärdet är rimligt.',geogebra=False)
add('3.83',r'Uttryck först bredd och höjd med samma variabel. När du hittat en stationär punkt behöver du också undersöka om arean ökar eller minskar på var sida.',[
 ('a) Bygg en areafunktion',r'<p>Symmetrin ger bredden 2x och höjden 12−x².</p>\[A(x)=2x(12-x^2)\]\[=24x-2x^3\]\[0\lt x\lt\sqrt{12}\]'),
 ('b) Bestäm den stationära punkten',r'\[A^{\prime}(x)=24-6x^2\]\[24-6x^2=0\quad\Rightarrow\quad x^2=4\]<p>Endast x=2 ligger i det tillåtna intervallet.</p>'),
 ('b) Beräkna arean',r'\[A(2)=2\cdot2(12-2^2)\]\[=4\cdot8=32\]'),
 ('c) Visa att arean är störst där',r'<p>För 0 &lt; x &lt; 2 är A′(x) positiv. För 2 &lt; x &lt; √12 är den negativ. Arean ökar fram till x=2 och minskar därefter, så 32 är det största värdet på hela det tillåtna intervallet.</p>')],r'a) \(A(x)=24x-2x^3\). b) \(32\) areaenheter. c) Derivatan byter tecken från plus till minus vid \(x=2\).',niva='C',traningsniva=3,poang='0/4/0')
add('3.287',r'Jämför uttrycket för tangentens lutning med funktionens uttryck. En heltalsrot kan hjälpa dig att faktorisera tredjegradspolynomet.',[
 ('Översätt villkoret till en ekvation',r'\[f(x)=x^3-2x\]\[f^{\prime}(x)=3x^2-2\]\[3x^2-2=x^3-2x\]\[x^3-3x^2-2x+2=0\]'),
 ('Hitta en rot och faktorisera',r'<p>Ett digitalt verktyg visar en rot nära −1. Insättning ger −1−3+2+2=0, så x+1 är en faktor.</p>\[x^3-3x^2-2x+2\]\[=(x+1)(x^2-4x+2)\]'),
 ('Lös den återstående andragradsekvationen',r'\[x^2-4x+2=0\]\[(x-2)^2=2\]\[x=2\pm\sqrt2\]'),
 ('Samla alla lösningar',r'<p>Faktorn x+1 ger också x=−1. Faktoriseringen visar att inga fler reella lösningar finns.</p>')],r'\(x=-1\), \(x=2-\sqrt2\approx0{,}586\) och \(x=2+\sqrt2\approx3{,}414\).',tolerans=[0,.0005,.0005],svarFormat=['numeriskt']*3)
add('3.330',r'Logaritmens argument är en funktion av x. Vilken extra faktor ger kedjeregeln?',[
 ('Derivera den yttre och inre funktionen',r'\[f^{\prime}(x)=\frac1{1+x^2}\cdot2x\]\[=\frac{2x}{1+x^2}\]'),
 ('Sätt in tangentpunktens x-värde',r'\[f^{\prime}(1)=\frac{2\cdot1}{1+1^2}=1\]')],r'Tangentens lutning är \(1\).')
add('3.331',r'Börja med den första derivatan. Derivera sedan det uttrycket en gång till innan du sätter in 2.',[
 ('Derivera två gånger',r'\[f^{\prime}(x)=3x^2-6x\]\[f^{\prime\prime}(x)=6x-6\]'),
 ('Beräkna andraderivatans värde',r'\[f^{\prime\prime}(2)=6\cdot2-6=6\]')],r'\(f^{\prime\prime}(2)=6\).')
add('3.332',r'Använd produktregeln. Exponentialfaktorn är alltid positiv, så vilken faktor avgör derivatans tecken?',[
 ('Derivera produkten',r'\[f^{\prime}(x)=1\cdot e^{-x}+x(-e^{-x})\]\[=e^{-x}(1-x)\]'),
 ('Hitta den stationära punkten',r'<p>Exponentialfaktorn är aldrig noll. Därför måste den andra faktorn vara noll.</p>\[1-x=0\quad\Rightarrow\quad x=1\]'),
 ('Visa att punkten ger det största värdet',r'<p>För x &lt; 1 är derivatan positiv. För x &gt; 1 är den negativ. Funktionen ökar alltså fram till x=1 och minskar sedan på hela resten av definitionsmängden.</p>')],r'Funktionen har sitt största värde vid \(x=1\).')
add('3.333',r'Översätt den givna tangentlutningen till ett villkor för derivatan. Ta med båda rötterna.',[
 ('Derivera och sätt lutningen till 3',r'\[y^{\prime}=3x^2-3\]\[3x^2-3=3\]'),
 ('Lös ekvationen exakt',r'\[3x^2=6\quad\Rightarrow\quad x^2=2\]\[x=-\sqrt2\quad\text{eller}\quad x=\sqrt2\]')],r'\(x=-\sqrt2\) och \(x=\sqrt2\).',svarsstruktur='mängd',svarEtiketter=['x','x'])
add('3.334',r'Hitta först alla nollställen till derivatan. Använd sedan andraderivatan för att skilja maximum från minimum.',[
 ('Bestäm de stationära punkternas x-värden',r'\[f^{\prime}(x)=3x^2-6x=3x(x-2)\]\[3x(x-2)=0\]\[x=0\quad\text{eller}\quad x=2\]'),
 ('Undersök andraderivatans tecken',r'\[f^{\prime\prime}(x)=6x-6\]\[f^{\prime\prime}(0)=-6\lt0\]<p>Det ger ett lokalt maximum vid x=0. Vid x=2 är andraderivatan 6 &gt; 0, vilket i stället ger ett lokalt minimum.</p>')],r'Den lokala maximipunktens x-koordinat är \(0\).')
add('3.335',r'Behandla a som en konstant när du deriverar. Vad ska derivatans värde vara vid x=2?',[
 ('Derivera med a som konstant',r'\[f^{\prime}(x)=2x+a\]'),
 ('Använd tangentens givna lutning',r'\[f^{\prime}(2)=1\quad\Rightarrow\quad4+a=1\]\[a=1-4=-3\]')],r'\(a=-3\).')
add('3.336',r'Försök skriva uttrycket som en kvadrat minus en konstant. Hur liten kan kvadraten bli?',[
 ('Kvadratkomplettera med x² som variabel',r'\[x^4-8x^2=(x^2-4)^2-16\]<p>Utveckling av kvadraten ger x⁴−8x²+16, så vi måste dra bort 16.</p>'),
 ('Bestäm en nedre gräns som faktiskt nås',r'\[(x^2-4)^2\ge0\]\[f(x)\ge-16\]<p>Likhet fås när x²−4=0, alltså vid x=−2 och x=2.</p>')],r'Det minsta funktionsvärdet är \(-16\).')
add('3.337',r'Vilken lutning har den räta linjen? En parallell tangent ska ha samma lutning.',[
 ('Läs av linjens lutning',r'<p>Linjen y=6x+1 har lutningen 6. Konstanten 1 påverkar inte lutningen.</p>'),
 ('Sätt kurvans derivata lika med denna lutning',r'\[y^{\prime}=2x\]\[2x=6\quad\Rightarrow\quad x=3\]')],r'\(x=3\).')
add('3.338',r'Rita båda leden som funktioner. Vilken av skärningspunkterna har störst x-koordinat?',[
 ('Bestäm båda skärningarna digitalt',r'<p>Skriv in y=eˣ och y=3x i GeoGebra. Skärningsverktyget ger</p>\[x\approx0{,}619061\]\[x\approx1{,}512135\]'),
 ('Välj den större lösningen och avrunda',r'<p>Den större x-koordinaten är 1,512134551… Fjärde decimalen är 1, så tre decimaler ger 1,512.</p>'),
 ('Kontrollera med det oavrundade värdet',r'\[e^{1{,}512134552}\approx4{,}536404\]\[3\cdot1{,}512134552\approx4{,}536404\]')],r'\(x\approx1{,}512\).',niva='E',traningsniva=2,poang='2/0/0')
add('3.339',r'Derivera inom definitionsmängden x>0. Hur ändras derivatans tecken när du passerar dess nollställe?',[
 ('Bestäm var derivatan är noll',r'\[f^{\prime}(x)=\frac1x-\frac12\]\[\frac1x=\frac12\quad\Rightarrow\quad x=2\]'),
 ('Kontrollera hela definitionsmängden',r'<p>För 0 &lt; x &lt; 2 är 1/x &gt; 1/2, så derivatan är positiv. För x &gt; 2 är 1/x &lt; 1/2, så derivatan är negativ.</p><p>Funktionen ökar fram till x=2 och minskar därefter. Därför är detta ett globalt maximum.</p>')],r'Funktionen har sitt största värde vid \(x=2\).')
add('3.340',r'Derivera den yttre kuben och multiplicera med den inre funktionens derivata.',[
 ('Använd kedjeregeln',r'\[f^{\prime}(x)=3(2x+1)^2\cdot2\]\[=6(2x+1)^2\]'),
 ('Sätt in x=1 efter deriveringen',r'\[f^{\prime}(1)=6(2\cdot1+1)^2\]\[=6\cdot9=54\]')],r'\(f^{\prime}(1)=54\).',traningsniva=2,miniräknare=True)
add('3.341',r'Derivatan av en produkt har två termer. Derivera en faktor i taget medan den andra behålls.',[
 ('Använd produktregeln',r'\[f^{\prime}(x)=2xe^x+x^2e^x\]\[=(2x+x^2)e^x\]'),
 ('Sätt in x=1 och behåll exakt värde',r'\[f^{\prime}(1)=(2+1)e=3e\]'),
 ('Avrunda om du väljer decimalsvar',r'\[3e=8{,}154845485\ldots\approx8{,}15\]')],r'\(3e\), eller \(8{,}15\) med två decimaler.',rättSvar=3*math.e)
add('3.342',r'I kvotregeln är ordningen i täljarens subtraktion viktig. Nämnaren ska kvadreras.',[
 ('Derivera täljare och nämnare',r'<p>Täljaren x har derivatan 1. Nämnaren x²+1 har derivatan 2x.</p>'),
 ('Använd kvotregeln',r'\[f^{\prime}(x)=\frac{1\cdot(x^2+1)-x\cdot2x}{(x^2+1)^2}\]\[=\frac{1-x^2}{(x^2+1)^2}\]'),
 ('Sätt in x=0',r'\[f^{\prime}(0)=\frac{1-0^2}{(0^2+1)^2}=1\]')],r'\(f^{\prime}(0)=1\).',miniräknare=True)
add('3.343',r'Derivera båda termerna med kedjeregeln. Kom ihåg minustecknet när cosinus deriveras.',[
 ('Derivera båda trigonometriska termerna',r'\[y^{\prime}=3\cos(3x)-2\sin(2x)\]'),
 ('Använd värdena vid vinkeln noll',r'\[y^{\prime}(0)=3\cos0-2\sin0\]\[=3\cdot1-2\cdot0=3\]')],r'Lutningen är \(3\).',traningsniva=2,miniräknare=True)
add('3.344',r'Läs av funktionsvärdet i tangentpunkten. Bestäm sedan tangentens lutning med två punkter på själva tangentlinjen.',[
 ('Läs av höjden och beräkna tangentens lutning',r'<p>Tangentpunkten ger f(2)=3. Tangenten går också genom (0,2) och (4,4).</p>\[f^{\prime}(2)=\frac{4-2}{4-0}=\frac12\]'),
 ('Använd kedjeregeln för kvadraten',r'\[g^{\prime}(x)=2f(x)f^{\prime}(x)\]'),
 ('Sätt in de två avlästa värdena',r'\[g^{\prime}(2)=2\cdot3\cdot\frac12=3\]')],r'\(g^{\prime}(2)=3\).',niva='C',poang='0/2/0',miniräknare=True)
add('3.345',r'Vilket värde får argumentet 2x när x=1? Använd tangentens lutning vid detta argument och kedjeregelns extra faktor.',[
 ('Derivera den sammansatta funktionen',r'\[h^{\prime}(x)=f^{\prime}(2x)\cdot2\]\[h^{\prime}(1)=2f^{\prime}(2)\]'),
 ('Beräkna tangentens lutning ur figuren',r'<p>Tangenten går genom (0,2) och (4,4).</p>\[f^{\prime}(2)=\frac{4-2}{4-0}=\frac12\]'),
 ('Multiplicera med den inre derivatan',r'\[h^{\prime}(1)=2\cdot\frac12=1\]')],r'\(h^{\prime}(1)=1\).',niva='C',poang='0/2/0',miniräknare=True)
add('3.346',r'Produktregeln använder addition medan kvotregeln använder subtraktion. Var extra noga med g(1), som är negativt.',[
 ('Beräkna produktens derivata',r'\[(fg)^{\prime}=f^{\prime}g+fg^{\prime}\]\[(fg)^{\prime}(1)=3(-1)+2\cdot4\]\[=-3+8=5\]'),
 ('Beräkna kvotens derivata',r'\[\left(\frac fg\right)^{\prime}=\frac{f^{\prime}g-fg^{\prime}}{g^2}\]\[\left(\frac fg\right)^{\prime}(1)=\frac{3(-1)-2\cdot4}{(-1)^2}\]\[=\frac{-3-8}{1}=-11\]')],r'Produktens derivata är \(5\), kvotens derivata är \(-11\).',traningsniva=2,poang='2/0/0',miniräknare=True)

def rectangle_svg(height):
 # Illustrativ rektangel som INTE är maximum. Samma skala i x/y inom respektive axel.
 X=lambda x:240+50*x
 Y=lambda y:255-16*y
 a=1.25;top=height-a*a;extent=math.sqrt(height)
 points=' '.join(f'{X(-extent+2*extent*i/120):.2f},{Y(height-(-extent+2*extent*i/120)**2):.2f}' for i in range(121))
 return f'''<span class="fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 320" width="480" height="320" role="img" aria-label="Rektangel med bas på x-axeln och övre hörn på parabeln y={height}−x². En möjlig rektangel visas; dess bredd är inte bestämd." style="max-width:100%;height:auto" font-family="Arial,sans-serif" font-size="16"><rect x="1" y="1" width="478" height="318" rx="10" fill="white" stroke="#d7e1ec"/><path d="M35 255H450 M240 275V30" fill="none" stroke="#23384c" stroke-width="1.5"/><text x="451" y="248" fill="#23384c">x</text><text x="250" y="28" fill="#23384c">y</text><text x="228" y="275" fill="#23384c">0</text><rect x="{X(-a)}" y="{Y(top)}" width="{100*a}" height="{16*top}" fill="#d6eaf5" fill-opacity=".7" stroke="#087d8e" stroke-width="2"/><polyline points="{points}" fill="none" stroke="#245aab" stroke-width="2.5"/><path d="M{X(-a)} 251v8 M{X(a)} 251v8" stroke="#23384c"/><text x="{X(-a)}" y="280" text-anchor="middle" fill="#23384c">−x</text><text x="{X(a)}" y="280" text-anchor="middle" fill="#23384c">x</text><circle cx="{X(a)}" cy="{Y(top)}" r="4" fill="#b5491d"/><path d="M{X(a)+4} {Y(top)-2}l18 -14" stroke="#b5491d" fill="none"/><text x="{X(a)+24}" y="{Y(top)-17}" fill="#23384c">(x, {height}−x²)</text><text x="85" y="40" fill="#245aab">y = {height} − x²</text><text x="240" y="307" text-anchor="middle" fill="#23384c">En möjlig rektangel</text></svg></span>'''

def install():
 p=ROOT/'uppgiftermatf1.js';raw=p.read_text();dec=json.JSONDecoder();i=raw.index('[')+1;edits=[];ids=[]
 while True:
  while raw[i].isspace() or raw[i]==',':i+=1
  if raw[i]==']':break
  q,n=dec.raw_decode(raw[i:]);old=json.loads(json.dumps(q));id=q['id']
  if q['omr']=='repetition_derivator':
   assert id in D,id;q.update(D[id]);ids.append(id)
   if id=='3.29':q['t']=q['t'].replace('Bestäm de kritiska punkterna.','Bestäm de x-värden där tangenten är horisontell.')
   if id=='3.287':q['t']=q['t'].replace('Använd gärna ett digitalt verktyg och bekräfta exakt.','Du får använda ett digitalt verktyg.')
   if id in ['3.52','3.83']:
    q['t']=re.sub(r'<span class="fig">\s*<svg[\s\S]*?</svg>\s*</span>','',q['t'])+rectangle_svg(9 if id=='3.52' else 12)
   if q!=old:
    source=raw[i:i+n];out=fields.replace_fields(source,q)
    for k,v in q.items():
     if k not in old:out=out.rstrip()[:-1]+',\n    '+json.dumps(k,ensure_ascii=False)+': '+json.dumps(v,ensure_ascii=False)+'\n  }'
    edits.append((i,i+n,out))
  i+=n
 assert len(ids)==27
 for a,b,s in reversed(edits):raw=raw[:a]+s+raw[b:]
 p.write_text(raw);print('27 granskade,',len(edits),'ändrade.')
if __name__=='__main__':install()
