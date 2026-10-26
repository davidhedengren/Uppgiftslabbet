"""Manuell områdesrevision: författade lösningar, inte automatiska metodrubriker."""
import json,re,math,importlib.util
from pathlib import Path
from html import escape
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('fields',Path(__file__).with_name('revidera-ma3-facitstruktur-2026-10-25.py'));fields=importlib.util.module_from_spec(spec);spec.loader.exec_module(fields)
D={}
def sol(steps,answer):
 return '<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'+''.join('<li><p class="facit-rubrik">'+escape(h)+'</p>'+b+'</li>' for h,b in steps)+'</ol><p class="facit-svar"><strong>Svar:</strong> '+answer+'</p></div>'
def add(id,hint,steps,answer,**meta):D[id]=dict(s=sol(steps,answer),ledtrad='<p>'+hint+'</p>',**meta)
add('3.07',r'Bestäm kvadratrotens värde och derivata vid 9. Hur långt från 9 ligger talet som ska uppskattas?',[
('Beräkna tangentpunktens höjd och lutning',r'\[f(9)=3,\qquad f^{\prime}(x)=\frac1{2\sqrt x}\]\[f^{\prime}(9)=\frac1{2\cdot3}=\frac16\]'),
('Skriv linjen genom punkten med denna lutning',r'\[L(x)=f(9)+f^{\prime}(9)(x-9)\]\[=3+\frac{x-9}{6}\]'),
('Sätt in 9,2 i linjen',r'\[L(9{,}2)=3+\frac{0{,}2}6=\frac{91}{30}\]\[\approx3{,}03333\]<p>Det är tangentens värde som används för uppskattningen.</p>')],r'\(L(x)=3+(x-9)/6\) och \(\sqrt{9{,}2}\approx3{,}03333\).',rättSvar=['3+(x-9)/6',91/30],tolerans=[None,1e-10],miniräknare=True)
add('3.08',r'Bestäm tangenten vid x = 1. Använd sedan andraderivatans tecken för att bedöma om tangenten ligger över eller under kurvan.',[
('Beräkna logaritmens tangent vid 1',r'\[f(1)=\ln1=0\]\[f^{\prime}(1)=1\]\[L(x)=0+1(x-1)=x-1\]'),
('Uppskatta logaritmen med tangentlinjen',r'\[L(1{,}04)=1{,}04-1=0{,}04\]'),
('Andraderivatan visar att tangenten ligger ovanför',r'\[f^{\prime\prime}(x)=-\frac1{x^2}<0\quad(x>0)\]<p>Lutningen avtar när x ökar. Kurvan böjer därför nedåt, och dess tangent vid 1 ligger ovanför kurvan. Tangentens uppskattning vid 1,04 blir för stor.</p>')],r'\(\ln(1{,}04)\approx0{,}04\). Approximationen är för stor.',traningsniva=4,niva='C',poang='0/3/0')
add('3.18',r'Använd kvadratrotens värde och derivata vid 16. Ändringen i x är negativ.',[
('Beräkna värdet och lutningen vid 16',r'\[f(16)=4\]\[f^{\prime}(16)=\frac1{2\sqrt{16}}=\frac18\]'),
('Använd den negativa ändringen i x',r'\[\Delta x=15{,}8-16=-0{,}2\]\[L(15{,}8)=4+\frac18(-0{,}2)\]\[=4-0{,}025=3{,}975\]')],r'\(\sqrt{15{,}8}\approx3{,}975\).')
add('3.26',r'Bestäm lutningen vid x = 16. Multiplicera den med ändringen från 16 till 16,3.',[
('Utgå från tangentpunkten (16, 4)',r'<p>För \(f(x)=\sqrt x\) gäller</p>\[f(16)=4\]\[f^{\prime}(16)=\frac1{2\sqrt{16}}=\frac18.\]'),
('Lägg tangentens höjdändring till 4',r'\[\Delta x=16{,}3-16=0{,}3\]\[L(16{,}3)=4+\frac18\cdot0{,}3\]\[=4+0{,}0375=4{,}0375\]')],r'\(\sqrt{16{,}3}\approx4{,}0375\).')
add('3.41',r'Använd f(x) = 1/x. Vilket tecken har derivatan vid x = 2?',[
('Beräkna funktionens värde och lutning',r'\[f(2)=\frac12,\qquad f^{\prime}(x)=-\frac1{x^2}\]\[f^{\prime}(2)=-\frac14\]'),
('Minska värdet eftersom tangentens lutning är negativ',r'\[L(2{,}04)=\frac12-\frac14(2{,}04-2)\]\[=0{,}5-0{,}01=0{,}49\]')],r'\(1/2{,}04\approx0{,}49\).')
add('3.192',r'Utgå från √49 och beräkna tangentens lutning där. Avrunda först efter att höjdändringen lagts till.',[
('Beräkna kvadratrotens värde och lutning vid 49',r'\[f(49)=7\]\[f^{\prime}(49)=\frac1{2\cdot7}=\frac1{14}\]'),
('Beräkna tangentens värde efter ändringen 0,4',r'\[L(49{,}4)=7+\frac{0{,}4}{14}\]\[=7{,}028571428\ldots\]'),
('Avrunda till fyra decimaler',r'<p>Femte decimalen är 7, så fjärde decimalen avrundas uppåt.</p>')],r'\(\sqrt{49{,}4}\approx7{,}0286\) med linjär approximation.',tolerans=.00005,miniräknare=True)
add('3.42',r'Skriv kubikroten som x^(1/3). Använd att 27^(1/3) = 3 när derivatans värde beräknas.',[
('Derivera kubikroten och sätt in 27',r'\[f(x)=x^{1/3},\qquad f^{\prime}(x)=\frac1{3x^{2/3}}\]\[f(27)=3\]\[f^{\prime}(27)=\frac1{3\cdot3^2}=\frac1{27}\]'),
('Beräkna tangentens värde vid 27,3',r'\[L(27{,}3)=3+\frac{27{,}3-27}{27}\]\[=3+\frac1{90}=3{,}01111\ldots\]')],r'\(\sqrt[3]{27{,}3}\approx3{,}01111\).',rättSvar=271/90,miniräknare=True)
add('3.43',r'Hur ändras kvadratrotens lutning när x ökar? Koppla det till tangentens läge i förhållande till kurvan.',[
('Undersök hur lutningen förändras',r'\[f^{\prime}(x)=\frac1{2\sqrt x}\]\[f^{\prime\prime}(x)=-\frac1{4x^{3/2}}<0\quad(x>0)\]'),
('Jämför tangentens lutning med kurvans efter x = 9',r'<p>Kurvans lutning avtar. Tangenten fortsätter däremot med samma lutning som vid 9. Mellan 9 och 9,4 ökar därför tangentens höjd mer än kurvans höjd.</p>')],r'Approximationen blir för stor, eftersom tangentlinjen ligger ovanför kurvan.',formaga=['begrepp','resonemang'])
add('3.63',r'Bestäm sinusfunktionens värde och derivata vid noll. Vinkeln anges i radianer.',[
('Beräkna tangentens höjd och lutning vid noll',r'\[f(0)=\sin0=0\]\[f^{\prime}(0)=\cos0=1\]'),
('Sätt in vinkeln i tangentlinjen',r'\[L(x)=0+1(x-0)=x\]\[L(0{,}06)=0{,}06\]')],r'\(\sin(0{,}06)\approx0{,}06\).')
add('3.64',r'Vilka värden har eˣ och dess derivata vid x = 0?',[
('Beräkna värdet och lutningen vid noll',r'<p>Funktionen \(f(x)=e^x\) har derivatan \(f^{\prime}(x)=e^x\). Alltså är</p>\[f(0)=1,\qquad f^{\prime}(0)=1.\]'),
('Sätt in 0,03 i tangentlinjen',r'\[L(x)=1+1(x-0)=1+x\]\[L(0{,}03)=1{,}03\]')],r'\(e^{0{,}03}\approx1{,}03\).')
add('3.65',r'Bestäm funktionsvärdet och lutningen vid x = 1. Sätt sedan in 1,08 i den linje du får.',[
('Beräkna tangentpunktens höjd och lutning',r'\[f(1)=\ln1=0\]\[f^{\prime}(1)=\frac11=1\]'),
('Skriv tangentlinjen genom (1, 0)',r'\[L(x)=0+1(x-1)=x-1\]'),
('Använd linjen för uppskattningen',r'\[L(1{,}08)=1{,}08-1=0{,}08\]')],r'\(L(x)=x-1\) och \(\ln(1{,}08)\approx0{,}08\).')
add('3.78',r'Tangentens lutning är derivatan av cos x vid noll. Vad innebär en tangent med lutningen noll?',[
('Beräkna cosinusfunktionens värde och lutning',r'\[f(0)=\cos0=1\]\[f^{\prime}(0)=-\sin0=0\]'),
('Skriv den vågräta tangentens ekvation',r'\[L(x)=1+0(x-0)=1\]<p>Första ordningens approximation kan vara konstant när lutningen är noll.</p>')],r'\(L(x)=1\).',svarFormat='uttryck',svarstyp='uttryck',rättSvar='1',tolerans=None)
add('3.196',r'Beräkna lutningen vid 49 och multiplicera den med 0,2. Behåll alla siffror tills slutsvaret avrundas.',[
('Beräkna kvadratrotens värde och lutning vid 49',r'\[f(49)=7\]\[f^{\prime}(49)=\frac1{2\cdot7}=\frac1{14}\]'),
('Beräkna tangentens värde vid 49,2',r'\[L(49{,}2)=7+\frac{0{,}2}{14}\]\[=7{,}014285714\ldots\]'),
('Avrunda till fyra decimaler',r'<p>Femte decimalen är 8, så fjärde decimalen avrundas uppåt.</p>')],r'\(\sqrt{49{,}2}\approx7{,}0143\) med linjär approximation.',tolerans=.00005,miniräknare=True)
add('3.99',r'Utgå från kvadratroten ur 25. Tangentens lutning bestäms med derivatan av √x.',[
('Bestäm värdet och lutningen vid 25',r'\[f(25)=5\]\[f^{\prime}(25)=\frac1{2\cdot5}=\frac1{10}\]'),
('Lägg till tangentens ökning',r'\[L(25{,}4)=5+\frac1{10}(25{,}4-25)\]\[=5+0{,}04=5{,}04\]')],r'\(\sqrt{25{,}4}\approx5{,}04\).')
add('3.116',r'Vad är logaritmens värde och lutning vid x = 1? Använd sedan ändringen 0,05.',[
('Bestäm logaritmens tangent vid 1',r'\[f(1)=0,\qquad f^{\prime}(1)=\frac11=1\]\[L(x)=0+1(x-1)=x-1\]'),
('Sätt in 1,05 i linjen',r'\[L(1{,}05)=1{,}05-1=0{,}05\]')],r'\(\ln(1{,}05)\approx0{,}05\).')
add('3.118',r'Beräkna ändringen från 4 till 4,1. Multiplicera den med den givna lutningen och lägg till startvärdet.',[
('Använd den givna tangentens lutning',r'\[\Delta x=4{,}1-4=0{,}1\]\[\Delta y\approx0{,}25\cdot0{,}1=0{,}025\]'),
('Lägg höjdändringen till värdet vid 4',r'\[L(4{,}1)=2+0{,}025=2{,}025\]')],r'\(\sqrt{4{,}1}\approx2{,}025\).')
add('3.119',r'Använd den givna lutningen och ändringen från 1 till 1,03.',[
('Beräkna ändringen i x',r'\[\Delta x=1{,}03-1=0{,}03\]'),
('Låt tangentens lutning ge ändringen i y',r'\[L(1{,}03)=0+1\cdot0{,}03=0{,}03\]')],r'\(\ln(1{,}03)\approx0{,}03\).')
add('3.120',r'Tangentens startvärde och lutning är givna. Hur mycket ökar linjens värde när x ökar från 0 till 0,05?',[
('Beräkna tangentens höjdändring',r'\[\Delta x=0{,}05-0=0{,}05\]\[\Delta y\approx1\cdot0{,}05=0{,}05\]'),
('Addera ändringen till startvärdet 1',r'\[L(0{,}05)=1+0{,}05=1{,}05\]')],r'\(e^{0{,}05}\approx1{,}05\).')
add('3.277',r'Multiplicera ändringen i x med den givna lutningen. Lägg sedan till värdet vid x = 36.',[
('Beräkna tangentens höjdändring',r'\[\Delta x=36{,}6-36=0{,}6\]\[\Delta y\approx\frac1{12}\cdot0{,}6=0{,}05\]'),
('Lägg ökningen till det kända funktionsvärdet',r'\[L(36{,}6)=6+0{,}05=6{,}05\]')],r'\(\sqrt{36{,}6}\approx6{,}05\).')
add('3.278',r'Både ändringen i x och tangentens lutning är negativa. Vilket tecken får deras produkt?',[
('Beräkna ändringen från 5 till 4,9',r'\[\Delta x=4{,}9-5=-0{,}1\]'),
('Multiplicera med den negativa lutningen',r'\[\Delta y\approx(-3)(-0{,}1)=0{,}3\]\[L(4{,}9)=12+0{,}3=12{,}3\]<p>När x minskar på en linje med negativ lutning ökar linjens höjd.</p>')],r'\(f(4{,}9)\approx12{,}3\).')
add('3.279',r'Skriv kubikroten som x^(1/3) och beräkna derivatan vid 8.',[
('Bestäm kubikrotens värde och lutning vid 8',r'\[f(8)=2,\qquad f^{\prime}(x)=\frac1{3x^{2/3}}\]\[f^{\prime}(8)=\frac1{3\cdot2^2}=\frac1{12}\]'),
('Sätt in ändringen 0,3 i tangentsambandet',r'\[L(8{,}3)=2+\frac{8{,}3-8}{12}\]\[=2+0{,}025=2{,}025\]')],r'\(\sqrt[3]{8{,}3}\approx2{,}025\).')
add('3.280',r'Sätt in 0,97 som x-värde i den givna tangentlinjen.',[
('Använd tangentlinjen i stället för logaritmen',r'<p>Den givna linjen är \(L(x)=x-1\).</p>\[L(0{,}97)=0{,}97-1=-0{,}03\]<p>Det negativa värdet är rimligt eftersom logaritmen är negativ när x ligger mellan 0 och 1.</p>')],r'\(\ln(0{,}97)\approx-0{,}03\).')
add('3.281',r'I uttrycket e^(−0,04) är x = 0,04. Sätt in det i den givna linjen y = 1−x.',[
('Sätt in x = 0,04 i tangentlinjen',r'\[L(0{,}04)=1-0{,}04=0{,}96\]<p>Vi använder positivt x = 0,04; minustecknet finns redan i funktionen e⁻ˣ och i tangentens lutning.</p>')],r'\(e^{-0{,}04}\approx0{,}96\).')
add('3.282',r'Använd f(x) = 1/x. Bestäm tangentens värde och lutning vid 1.',[
('Beräkna funktionens värde och derivata',r'\[f(1)=1,\qquad f^{\prime}(x)=-\frac1{x^2}\]\[f^{\prime}(1)=-1\]'),
('Uppskatta förändringen när x ökar med 0,02',r'\[L(1{,}02)=1-1(1{,}02-1)\]\[=1-0{,}02=0{,}98\]')],r'\(1/1{,}02\approx0{,}98\).')
add('3.283',r'Tangentens lutning är derivatan av √x vid x = 9.',[
('Derivera kvadratroten',r'\[f(x)=x^{1/2}\]\[f^{\prime}(x)=\frac1{2\sqrt x}\]'),
('Sätt in tangentpunktens x-värde',r'\[f^{\prime}(9)=\frac1{2\cdot3}=\frac16\]')],r'Lutningen är \(1/6\).')
add('3.284',r'Tangenten går genom kurvans punkt där x = 1. Sätt in punktens koordinater i y = x+c.',[
('Bestäm punkten som tangenten går genom',r'\[x=1,\qquad y=\ln1=0\]<p>Tangenten går alltså genom (1, 0).</p>'),
('Sätt in punkten i den givna linjens ekvation',r'\[0=1+c\quad\Rightarrow\quad c=-1\]')],r'\(c=-1\).')
add('3.286',r'I a används kvadratrotens värde och derivata vid 4. I b ska du jämföra kvadraterna av de två avstånden från 4.',[
('a) Bestäm tangentens lutning vid 4',r'\[f(4)=2,\qquad f^{\prime}(4)=\frac1{2\sqrt4}=\frac14\]'),
('a) Beräkna tangentens värde vid 4,1',r'\[L(4{,}1)=2+\frac14(4{,}1-4)\]\[=2+0{,}025=2{,}025\]'),
('b) Jämför avstånden från tangentpunkten',r'\[h_1=4{,}1-4=0{,}1\]\[h_2=4{,}01-4=0{,}01\]'),
('b) Kvadrera förhållandet eftersom felet följer h²',r'\[\frac{\text{fel}_1}{\text{fel}_2}\approx\frac{0{,}1^2}{0{,}01^2}=100\]<p>Det nya felet är ungefär en hundradel av det första.</p>')],r'a) \(2{,}025\). b) Felet blir ungefär \(100\) gånger mindre.',svarFormat=['numeriskt','numeriskt'],tolerans=[.0005,1e-10],traningsniva=3,niva='C',poang='0/3/0')
add('3.312a',r'Tangenten går genom (3, f(3)) och har lutningen f′(3).',[
('Beräkna höjden och lutningen vid 3',r'\[f(3)=3^2=9\]\[f^{\prime}(x)=2x,\qquad f^{\prime}(3)=6\]'),
('Skriv tangenten och utveckla parentesen',r'\[y=9+6(x-3)\]\[=9+6x-18=6x-9\]')],r'\(y=6x-9\).',traningsniva=2)
add('3.312b',r'Beräkna först både funktionsvärdet och derivatans värde vid 2.',[
('Bestäm tangentpunktens höjd',r'\[f(2)=2^3-2\cdot2+3=7\]'),
('Beräkna tangentens lutning',r'\[f^{\prime}(x)=3x^2-2\]\[f^{\prime}(2)=3\cdot4-2=10\]'),
('Skriv linjen på den efterfrågade formen',r'\[y=7+10(x-2)\]\[=7+10x-20=10x-13\]')],r'\(y=10x-13\).')
add('3.312c',r'Glöm inte kedjeregelns faktor 2 när e^(2x) deriveras.',[
('Bestäm värdet och lutningen vid noll',r'\[f(0)=e^0=1\]\[f^{\prime}(x)=2e^{2x},\qquad f^{\prime}(0)=2\]'),
('Sätt in värdena i tangentens ekvation',r'\[y=1+2(x-0)=2x+1\]')],r'\(y=2x+1\).')
add('3.312d',r'Använd derivatan av tan x och de exakta trigonometriska värdena vid π/4.',[
('Beräkna funktionens värde vid π/4',r'\[f(\pi/4)=\tan(\pi/4)=1\]'),
('Beräkna tangentens lutning',r'\[f^{\prime}(x)=\frac1{\cos^2x}\]\[f^{\prime}(\pi/4)=\frac1{(\sqrt2/2)^2}=2\]'),
('Skriv linjen genom tangentpunkten',r'\[y=1+2\left(x-\frac\pi4\right)\]\[=2x+1-\frac\pi2\]')],r'\(y=2x+1-\pi/2\).')
add('3.313a',r'Välj ett heltal nära 2,1 där både (1+x)³ och derivatan är enkla att beräkna.',[
('Välj tangentpunkten x = 2',r'\[f(2)=(1+2)^3=27\]'),
('Bestäm derivatans värde i samma punkt',r'\[f^{\prime}(x)=3(1+x)^2\]\[f^{\prime}(2)=3\cdot9=27\]'),
('Beräkna tangentens värde vid 2,1',r'\[L(2{,}1)=27+27(2{,}1-2)\]\[=27+2{,}7=29{,}7\]')],r'\(f(2{,}1)\approx29{,}7\).')
add('3.313b',r'Vilken perfekt kub ligger nära 8,5? Beräkna värdet och derivatan där.',[
('Välj tangentpunkten x = 8',r'\[f(8)=2,\qquad f^{\prime}(x)=\frac1{3x^{2/3}}\]\[f^{\prime}(8)=\frac1{3\cdot4}=\frac1{12}\]'),
('Beräkna tangentens värde och avrunda på slutet',r'\[L(8{,}5)=2+\frac{0{,}5}{12}=\frac{49}{24}\]\[=2{,}041666\ldots\approx2{,}042\]')],r'\(\sqrt[3]{8{,}5}\approx2{,}042\).')
add('3.314a',r'Skriv basen som 1 plus en liten ändring. Exponenten är k.',[
('Identifiera ändringen från 1 och exponenten',r'\[1{,}002=1+0{,}002\]\[x=0{,}002,\qquad k=50\]'),
('Använd det givna linjära uttrycket',r'\[1+kx=1+50\cdot0{,}002\]\[=1+0{,}1=1{,}1\]')],r'\(1{,}002^{50}\approx1{,}1\).')
add('3.314b',r'Basen ligger under 1, så ändringen x är negativ.',[
('Skriv basen som 1 plus en negativ ändring',r'\[0{,}998=1-0{,}002\]\[x=-0{,}002,\qquad k=40\]'),
('Sätt in värdena med rätt tecken',r'\[1+kx=1+40(-0{,}002)\]\[=1-0{,}08=0{,}92\]')],r'\(0{,}998^{40}\approx0{,}92\).')
add('3.314c',r'Ändringen från 1 är positiv men exponenten är negativ. Vilket tecken får produkten kx?',[
('Identifiera ändringen och den negativa exponenten',r'\[1{,}004=1+0{,}004\]\[x=0{,}004,\qquad k=-15\]'),
('Beräkna den negativa förändringen',r'\[1+kx=1-15\cdot0{,}004\]\[=1-0{,}06=0{,}94\]')],r'\(1{,}004^{-15}\approx0{,}94\).')
add('3.314d',r'Skriv kubikroten som en potens med exponenten 1/3.',[
('Skriv om roten till en potens',r'\[\sqrt[3]{1{,}009}=(1+0{,}009)^{1/3}\]<p>Alltså är \(x=0{,}009\) och \(k=1/3\).</p>'),
('Använd det givna approximationsuttrycket',r'\[1+kx=1+\frac13\cdot0{,}009\]\[=1+0{,}003=1{,}003\]')],r'\(\sqrt[3]{1{,}009}\approx1{,}003\).')
add('3.315',r'Börja med tangentlinjen till vänsterledet vid x = 1. Lös sedan ekvationen med tangentuttrycket i stället för exponentialfunktionen.',[
('Bestäm tangentens höjd och lutning vid 1',r'<p>Sätt \(f(x)=e^{x-1}\). Då gäller</p>\[f(1)=1,\qquad f^{\prime}(1)=e^0=1.\]'),
('Ersätt vänsterledet med tangentlinjen',r'\[L(x)=1+1(x-1)=x\]<p>Den nya ekvationen blir</p>\[x=5x-4{,}5.\]'),
('Lös den linjära ekvationen',r'\[4x=4{,}5\quad\Rightarrow\quad x=1{,}125\]<p>Detta löser den nya linjära ekvationen och är en uppskattning av en lösning till ursprungsekvationen.</p>')],r'\(x=1{,}125\) i den linjära ekvationen.')
add('3.316a',r'Derivera sinus med kedjeregeln. Argumentet ska räknas i radianer.',[
('Derivera temperaturmodellen med kedjeregeln',r'\[T^{\prime}(t)=8\cdot\frac\pi{24}\cos\frac{\pi(t-8)}{24}\]\[=\frac\pi3\cos\frac{\pi(t-8)}{24}\]'),
('Sätt in t = 6',r'\[\frac{\pi(6-8)}{24}=-\frac\pi{12}\]\[T^{\prime}(6)=\frac\pi3\cos(-\pi/12)\]\[\approx1{,}01151516\]'),
('Avrunda och ange förändring per timme',r'<p>Derivatan anger hur många grader per timme temperaturen ökar just då.</p>')],r'\(T^{\prime}(6)\approx1{,}01\) °C/h.')
add('3.316b',r'Omvandla 15 minuter till timmar. Multiplicera tiden med den givna lutningen och addera starttemperaturen.',[
('Omvandla tiden till samma enhet som lutningen',r'\[\Delta t=\frac{15}{60}=0{,}25\text{ h}\]'),
('Använd de givna tangentvärdena',r'\[\Delta T\approx1{,}01\cdot0{,}25\]\[=0{,}2525\text{ °C}\]\[L(6{,}25)\approx18{,}93+0{,}2525\]\[=19{,}1825\text{ °C}\]'),
('Avrunda temperaturen till en decimal',r'<p>Andra decimalen är 8, så första decimalen avrundas uppåt.</p>')],r'Temperaturen uppskattas till \(19{,}2\) °C klockan 06.15.',traningsniva=2,niva='E',poang='1/0/0')
add('3.317a',r'Bestäm kaffets temperatur och temperaturens derivata vid x = 0.',[
('Beräkna starttemperaturen',r'\[T(0)=18+80e^0=98\]'),
('Beräkna tangentens lutning',r'\[T^{\prime}(x)=-0{,}277\cdot80e^{-0{,}277x}\]\[T^{\prime}(0)=-22{,}16\]'),
('Skriv den linjära approximationen',r'\[L(x)=98-22{,}16(x-0)\]')],r'\(y=98-22{,}16x\).')
add('3.317b',r'Beräkna modellens temperatur och tangentens temperatur vid samma tid. Dividera skillnadens storlek med modellens temperatur.',[
('Beräkna modellens temperatur efter en halv minut',r'\[T(0{,}50)=18+80e^{-0{,}277\cdot0{,}50}\]\[\approx87{,}6530601\text{ °C}\]'),
('Beräkna tangentens uppskattning',r'\[L(0{,}50)=98-22{,}16\cdot0{,}50\]\[=86{,}92\text{ °C}\]'),
('Jämför felet med modellens temperatur',r'<p>Låt ε beteckna det relativa felet.</p>\[\varepsilon=\frac{|T(0{,}50)-L(0{,}50)|}{|T(0{,}50)|}\]\[\approx0{,}0083632003\]<p>Omvandling till procent ger</p>\[\varepsilon\cdot100\%\approx0{,}83632\%.\]')],r'Det relativa felet är cirka \(0{,}8\) %.')
add('3.324',r'Hur mycket ändras avståndet? Multiplicera ändringen med signalens ökning per millimeter.',[
('Beräkna avståndsändringen',r'\[\Delta x=2{,}1-2=0{,}1\text{ mm}\]'),
('Beräkna signalens ökning och lägg till startvärdet',r'\[\Delta U\approx3\cdot0{,}1=0{,}3\text{ V}\]\[U\approx7+0{,}3=7{,}3\text{ V}\]')],r'Signalen uppskattas till \(7{,}3\) V.',svarEnhet='V')
add('3.325',r'Temperaturen minskar. Använd en negativ lutning under den ytterligare halva minuten.',[
('Beräkna hur mycket mer tid som går',r'\[\Delta t=10{,}5-10=0{,}5\text{ min}\]'),
('Lägg temperaturändringen till 50 °C',r'\[\Delta T\approx(-2)\cdot0{,}5=-1\text{ °C}\]\[T\approx50-1=49\text{ °C}\]')],r'Temperaturen uppskattas till \(49\) °C.',svarEnhet='°C')
add('3.326',r'Skriv arean som en funktion av sidan. Använd derivatan för att uppskatta areaökningen och jämför med den ursprungliga arean.',[
('Bestäm areans värde och derivata vid sidan 10 cm',r'\[A(s)=s^2,\quad A(10)=100\text{ cm}^2\]\[A^{\prime}(s)=2s,\quad A^{\prime}(10)=20\]'),
('Uppskatta areaökningen',r'\[\Delta s=10{,}2-10=0{,}2\text{ cm}\]\[\Delta A\approx20\cdot0{,}2=4\text{ cm}^2\]'),
('Jämför ökningen med den ursprungliga arean',r'\[\frac{\Delta A}{A(10)}\cdot100\%\]\[\approx\frac4{100}\cdot100\%=4\%\]')],r'Arean ökar med ungefär \(4\) %. ',svarEnhet='%')
add('3.327',r'Funktionsvärdets ändring är känd. Dividera den med lutningen för att hitta ändringen i x.',[
('Beräkna den önskade höjdändringen',r'\[\Delta y=12{,}24-12=0{,}24\]'),
('Lös ut ändringen i x ur tangentsambandet',r'\[0{,}8\Delta x=0{,}24\]\[\Delta x=\frac{0{,}24}{0{,}8}=0{,}3\]'),
('Lägg ändringen till tangentpunktens x-värde',r'\[x\approx4+0{,}3=4{,}3\]')],r'\(x\approx4{,}3\).')
add('3.328',r'Tangentens lutning är derivatan av x² vid 2. Tänk på att 1,95 ligger till vänster om 2.',[
('Beräkna höjden och lutningen vid 2',r'\[f(2)=4,\qquad f^{\prime}(2)=2\cdot2=4\]'),
('Använd den negativa ändringen i x',r'\[\Delta x=1{,}95-2=-0{,}05\]\[L(1{,}95)=4+4(-0{,}05)=3{,}8\]')],r'\(1{,}95^2\approx3{,}8\) med tangentlinjen.')
add('3.329',r'Beräkna både funktionens värde och dess derivata vid noll. Använd sedan tangentens värde vid 0,2.',[
('Beräkna värdet och lutningen vid noll',r'\[f(0)=0^3=0\]\[f^{\prime}(x)=3x^2,\qquad f^{\prime}(0)=0\]'),
('Skriv och använd den vågräta tangenten',r'\[L(x)=0+0(x-0)=0\]\[L(0{,}2)=0\]'),
('Skilj tangentens värde från funktionens värde',r'<p>Funktionens verkliga värde är \(0{,}2^3=0{,}008\), men frågan gäller tangentens approximation. Tangenten följer inte kurvans böjning. Nära tangentpunkten kan det absoluta felet vara litet samtidigt som det relativa felet är stort.</p>')],r'Den linjära approximationen ger \(0\).')

PART_PARENTS=['3.312','3.313','3.314','3.316','3.317']
def update_object(source,q):
 out=fields.replace_fields(source,q);old=json.loads(source)
 for k,v in q.items():
  if k not in old:out=out.rstrip()[:-1]+',\n    '+json.dumps(k,ensure_ascii=False)+': '+json.dumps(v,ensure_ascii=False)+'\n  }'
 return out

def install():
 path=ROOT/'uppgiftermatf1.js';raw=path.read_text();i=raw.index('[')+1;dec=json.JSONDecoder();edits=[];review=[]
 while True:
  while raw[i].isspace() or raw[i]==',':i+=1
  if raw[i]==']':break
  q,n=dec.raw_decode(raw[i:]);old=json.loads(json.dumps(q));id=q['id']
  if q['omr']=='linjar_approximation':
   q.update(D.get(id,{}))
   if id in PART_PARENTS:
    for p in q['spelDelar']:p.update(D[id+p['etikett']])
   # Räkna från oavrundade referenser. Fri avrundning hanteras redan av konsumenten.
   if id not in ['3.07','3.08','3.43','3.78','3.192','3.196','3.286','3.283','3.329'] and not q.get('spelDelar'):q['tolerans']=1e-10
   if id=='3.08':q['tolerans']=[1e-10,None]
   if id=='3.283':q.update(rättSvar=1/6,svarFormat='numeriskt',svarstyp='numeriskt',tolerans=1e-10)
   if id=='3.65':q['tolerans']=[None,1e-10]
   if id=='3.313':q.update(rättSvar=[29.7,49/24],tolerans=[1e-10,.0005])
   if id=='3.314':q['tolerans']=[1e-10]*4
   if id=='3.316':
    k=math.pi/3*math.cos(math.pi/12);y=21-8*math.sin(math.pi/12)
    q.update(rättSvar=[k,y+k/4],tolerans=[.005,.05],svarEnhet=['°C/h','°C'])
    a,b=q['spelDelar'];b['t']=r'<p>Klockan 06.00 är temperaturen 18,93 °C. Just då ökar den med 1,01 °C per timme.</p><p>Använd linjär approximation för att uppskatta temperaturen klockan 06.15. Svara i °C med en decimal.</p>'
    b['fraga']=r'Använd den givna temperaturen och förändringstakten för att uppskatta temperaturen klockan 06.15. Svara i °C med en decimal.'
   if id=='3.317':
    temp=18+80*math.exp(-.277*.5)
    q.update(rättSvar=['98-22.16x',100*(temp-86.92)/temp],tolerans=[None,.05])
   if id=='3.329':
    for alt,c in zip(q['alternativ'],['Rätt. Både funktionsvärdet och lutningen är noll vid tangentpunkten, så tangenten är y = 0.','Detta är funktionens verkliga värde 0,2³, inte tangentens approximation.','Detta är 0,2². Frågan gäller tangentlinjen till x³ vid noll.','Detta är derivatans värde 3·0,2² vid 0,2. Tangenten ska i stället bestämmas vid noll.']):alt['kommentar']=c
   if id in ['3.328','3.329']:q['typ']='linjär approximation av potensfunktion'
   if q.get('spelDelar'):
    main=[]
    for part in q['spelDelar']:
     s=part['s']
     if id=='3.316' and part['etikett']=='b':
      s=sol([
       ('Beräkna temperaturen vid klockan 06.00',r'\[T(6)=21+8\sin(-\pi/12)\]\[\approx18{,}929448\text{ °C}\]'),
       ('Omvandla tiden och använd tangentens lutning',r'\[\Delta t=15/60=0{,}25\text{ h}\]<p>Lutningen från a används utan mellanavrundning.</p>\[L(6{,}25)=T(6)+T^{\prime}(6)\cdot0{,}25\]\[\approx19{,}182326\text{ °C}\]'),
       ('Avrunda till en decimal',r'<p>Andra decimalen är 8. Temperaturen avrundas därför uppåt.</p>')],r'Temperaturen uppskattas till \(19{,}2\) °C.')
     main.append('<div class="facit-del"><span class="facit-mark">'+part['etikett']+')</span><div class="facit-arbete">'+s+'</div></div>')
    q['s']='<div class="facit-v2">'+''.join(main)+'</div>'
   changes=[k for k in q if q[k]!=old.get(k)];review.append(dict(id=id,changed=changes,parts=[p['etikett'] for p in q.get('spelDelar',[])],level=q['traningsniva']))
   if changes:edits.append((i,i+n,update_object(raw[i:i+n],q)))
  i+=n
 for start,end,new in reversed(edits):raw=raw[:start]+new+raw[end:]
 path.write_text(raw);return review
if __name__=='__main__':
 r=install();print('Granskade',len(r),'ändrade',sum(bool(q['changed']) for q in r))
