"""Manuellt skrivna lösningar. Ingen rubrik eller förklaring genereras ur gamla facit."""
import json,re,importlib.util
from pathlib import Path
from html import escape
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('fields',Path(__file__).with_name('revidera-ma3-facitstruktur-2026-10-25.py')); fields=importlib.util.module_from_spec(spec);spec.loader.exec_module(fields)
def sol(steps,answer):
 return '<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'+''.join('<li><p class="facit-rubrik">'+escape(title)+'</p>'+body+'</li>' for title,body in steps)+'</ol><p class="facit-svar"><strong>Svar:</strong> '+answer+'</p></div>'
DATA={}
def add(id,hint,steps,answer):DATA[id]={'ledtrad':'<p>'+hint+'</p>','s':sol(steps,answer)}
add('3.03',r'Skriv \(\ln x\) som \(1\cdot\ln x\). Vilken faktor bör deriveras?',[
('Skriv logaritmen som en produkt med 1',r'<p>Välj \(u=\ln x\) och \(v\prime=1\). Då är \(u\prime=1/x\) och \(v=x\), för \(x>0\).</p>'),
('Produkten i den nya integralen blir 1',r'\[\int u v\prime\,dx=uv-\int u\prime v\,dx\]\[\int\ln x\,dx=x\ln x-\int\frac1x\cdot x\,dx\]\[=x\ln x-\int1\,dx\]'),
('Integrera konstanten och ta med alla primitiva funktioner',r'<p>En primitiv funktion till 1 är x. En godtycklig konstant C ger hela familjen.</p>')],r'\(F(x)=x\ln x-x+C\), för \(x>0\).')
add('3.125',r'Låt x deriveras. Vilken faktor behövs när du integrerar \(\sin(2x)\)?',[
('Derivera x och integrera sinusfaktorn',r'<p>Välj \(u=x\), \(u\prime=1\), \(v\prime=\sin(2x)\) och \(v=-\cos(2x)/2\).</p>'),
('Sätt in faktorerna i partiell integration',r'\[\int x\sin(2x)\,dx\]\[=-\frac{x\cos(2x)}2+\frac12\int\cos(2x)\,dx\]'),
('Integrera cosinus och välj en konstant',r'<p>Den sista integralen är \(\sin(2x)/2\). Faktoren 1/2 framför den ger därför 1/4. Eftersom en primitiv funktion efterfrågas kan vi välja C = 0.</p>')],r'\(F(x)=-x\cos(2x)/2+\sin(2x)/4\).')
add('3.14',r'Derivera x och integrera cos x. Tänk på tecknet när den återstående sinusfunktionen integreras.',[
('Välj faktorer så att x försvinner vid derivering',r'<p>Med \(u=x\) och \(v\prime=\cos x\) blir \(u\prime=1\) och \(v=\sin x\).</p>'),
('Använd partiell integration på produkten',r'\[\int x\cos x\,dx=x\sin x-\int\sin x\,dx\]'),
('Det sista minustecknet ger plus cosinus',r'<p>En primitiv funktion till sin x är −cos x. Därför ger subtraktionen \(-(-\cos x)=\cos x\).</p>')],r'\(F(x)=x\sin x+\cos x+C\).')
add('3.15',r'Låt logaritmen deriveras och x² integreras. Vad blir produkten i den återstående integralen?',[
('Derivera logaritmen och integrera x²',r'<p>Välj \(u=\ln x\), \(u\prime=1/x\), \(v\prime=x^2\) och \(v=x^3/3\).</p>'),
('Förkorta produkten i den nya integralen',r'\[\int x^2\ln x\,dx\]\[=\frac{x^3\ln x}{3}-\int\frac1x\cdot\frac{x^3}3\,dx\]\[=\frac{x^3\ln x}{3}-\frac13\int x^2\,dx\]'),
('Integrera potensen med faktorn 1/3 kvar',r'\[\frac13\int x^2\,dx=\frac13\cdot\frac{x^3}3=\frac{x^3}9\]<p>En enda partiell integration räcker; därefter används potensregeln.</p>')],r'\(F(x)=x^3\ln x/3-x^3/9+C\), för \(x>0\).')
add('3.30',r'Välj x som faktorn som deriveras. Kom ihåg den inre derivatan 2 när exponentialfunktionen integreras.',[
('Integrera exponentialfunktionen med rätt faktor',r'<p>Välj \(u=x\), \(u\prime=1\), \(v\prime=e^{2x}\) och \(v=e^{2x}/2\).</p>'),
('Använd partiell integration och integrera en gång till',r'\[\int xe^{2x}\,dx=\frac{xe^{2x}}2-\frac12\int e^{2x}\,dx\]\[=\frac{xe^{2x}}2-\frac12\cdot\frac{e^{2x}}2+C\]')],r'\(F(x)=xe^{2x}/2-e^{2x}/4+C\).')
add('3.31',r'Välj x som faktorn som deriveras. En primitiv funktion till sin x har ett minustecken.',[
('Derivera x och integrera sin x',r'<p>Välj \(u=x\), \(u\prime=1\), \(v\prime=\sin x\) och \(v=-\cos x\).</p>'),
('Subtraktionen av v ger en positiv integral',r'\[\int x\sin x\,dx=-x\cos x+\int\cos x\,dx\]'),
('Integrera cosinus och lägg till konstanten',r'<p>En primitiv funktion till cos x är sin x. Konstanten C får vara vilket reellt tal som helst.</p>')],r'\(F(x)=-x\cos x+\sin x+C\).')
add('3.132',r'Derivera x² i första omgången. Den återstående produkten med x kräver en andra partiell integration.',[
('Minska polynomets grad från 2 till 1',r'<p>Välj \(u=x^2\), \(u\prime=2x\) och \(v=e^{2x}/2\).</p>\[\int x^2e^{2x}\,dx=\frac{x^2e^{2x}}2-J\]<p>Här är \(J=\int xe^{2x}\,dx\).</p>'),
('Beräkna J genom att derivera x',r'<p>Välj nu \(u=x\), \(u\prime=1\) och \(v=e^{2x}/2\).</p>\[J=\frac{xe^{2x}}2-\frac12\int e^{2x}\,dx\]\[=\frac{xe^{2x}}2-\frac{e^{2x}}4\]'),
('Subtrahera J och samla exponentialfaktorn',r'\[F(x)=\frac{x^2e^{2x}}2-\frac{xe^{2x}}2+\frac{e^{2x}}4\]<p>Vi väljer integrationskonstanten noll eftersom en primitiv funktion räcker.</p>')],r'\(F(x)=e^{2x}(2x^2-2x+1)/4\).')
add('3.133',r'Derivera x² och integrera sin(2x). Integrera sedan den nya produkten partiellt en gång till.',[
('Den första omgången lämnar x cos(2x)',r'<p>Välj \(u=x^2\), \(u\prime=2x\) och \(v=-\cos(2x)/2\).</p>\[\int x^2\sin(2x)\,dx=-\frac{x^2\cos(2x)}2+J\]<p>Här är \(J=\int x\cos(2x)\,dx\).</p>'),
('Integrera produkten i J partiellt',r'<p>Välj \(u=x\), \(u\prime=1\) och \(v=\sin(2x)/2\).</p>\[J=\frac{x\sin(2x)}2-\frac12\int\sin(2x)\,dx\]\[=\frac{x\sin(2x)}2+\frac{\cos(2x)}4\]'),
('Sätt in J och välj konstanten noll',r'<p>De två termerna i J ska adderas till det första resultatet. Vi söker en primitiv funktion, så C = 0 går bra.</p>')],r'\(F(x)=-x^2\cos(2x)/2+x\sin(2x)/2+\cos(2x)/4\).')
add('3.33',r'Integrera produkten partiellt med x som faktorn som deriveras. Beräkna sedan F(1)−F(0).',[
('Bestäm en primitiv funktion till xeˣ',r'<p>Med \(u=x\), \(u\prime=1\) och \(v=e^x\) ger partiell integration</p>\[F(x)=xe^x-\int e^x\,dx=(x-1)e^x.\]'),
('Beräkna värdet vid båda gränserna',r'\[F(1)=(1-1)e=0\]\[F(0)=(0-1)e^0=-1\]'),
('Subtrahera värdet vid den undre gränsen',r'\[\int_0^1xe^x\,dx=F(1)-F(0)\]\[=0-(-1)=1\]')],r'Integralen är \(1\).')
add('3.34',r'Derivera x² i första omgången och x i den andra. Exponentialfunktionen behåller sin form.',[
('Den första integrationen ger en produkt med x',r'<p>Välj \(u=x^2\), \(u\prime=2x\) och \(v=e^x\).</p>\[I=\int x^2e^x\,dx=x^2e^x-2J\]<p>Här är \(J=\int xe^x\,dx\).</p>'),
('Beräkna J med en andra partiell integration',r'<p>Med \(u=x\), \(u\prime=1\) och \(v=e^x\) får vi</p>\[J=xe^x-\int e^x\,dx=xe^x-e^x.\]'),
('Multiplicera hela J med −2',r'\[I=x^2e^x-2(xe^x-e^x)+C\]\[=e^x(x^2-2x+2)+C\]')],r'\(e^x(x^2-2x+2)+C\).')
add('3.135',r'Låt ln x deriveras och x integreras. Förenkla den nya integrandens potens.',[
('Derivera logaritmen i produkten',r'<p>För \(x>0\) väljer vi \(u=\ln x\), \(u\prime=1/x\), \(v\prime=x\) och \(v=x^2/2\).</p>'),
('Förenkla den återstående integralen',r'\[\int x\ln x\,dx=\frac{x^2\ln x}2-\frac12\int x\,dx\]\[=\frac{x^2\ln x}2-\frac{x^2}4+C\]'),
('Välj en av de primitiva funktionerna',r'<p>Frågan efterfrågar en primitiv funktion. Vi väljer C = 0.</p>')],r'\(F(x)=x^2\ln x/2-x^2/4\), för \(x>0\).')
add('3.55',r'Låt x deriveras. Ta hänsyn till faktorn 2 i cosinusfunktionens argument vid båda integreringarna.',[
('Derivera x och integrera cos(2x)',r'<p>Välj \(u=x\), \(u\prime=1\) och \(v=\sin(2x)/2\).</p>\[\int x\cos(2x)\,dx\]\[=\frac{x\sin(2x)}2-\frac12\int\sin(2x)\,dx\]'),
('Integrera sinus med rätt tecken och faktor',r'<p>En primitiv funktion till \(\sin(2x)\) är \(-\cos(2x)/2\). Multiplikation med −1/2 ger därför \(+\cos(2x)/4\).</p>')],r'\(x\sin(2x)/2+\cos(2x)/4+C\).')
add('3.56',r'Derivera x. Kontrollera minustecknet i en primitiv funktion till e⁻ˣ.',[
('Integrera exponentialfunktionen med minustecken',r'<p>Välj \(u=x\), \(u\prime=1\) och \(v=-e^{-x}\).</p>\[\int xe^{-x}\,dx=-xe^{-x}+\int e^{-x}\,dx\]'),
('Samla termerna med e⁻ˣ',r'\[=-xe^{-x}-e^{-x}+C\]\[=-(x+1)e^{-x}+C\]')],r'\(-(x+1)e^{-x}+C\).')
add('3.57',r'Låt logaritmen deriveras när du bestämmer en primitiv funktion. Vid gränserna gäller ln e = 1 och ln 1 = 0.',[
('Integrera produkten genom att derivera logaritmen',r'<p>Välj \(u=\ln x\), \(u\prime=1/x\) och \(v=x^2/2\).</p>\[F(x)=\frac{x^2\ln x}2-\frac12\int x\,dx\]\[=\frac{x^2\ln x}2-\frac{x^2}4\]'),
('Sätt in e och 1 var för sig',r'\[F(e)=\frac{e^2}2-\frac{e^2}4=\frac{e^2}4\]\[F(1)=0-\frac14=-\frac14\]'),
('Subtrahera det negativa värdet vid 1',r'\[\int_1^e x\ln x\,dx=\frac{e^2}4-\left(-\frac14\right)\]')],r'\((e^2+1)/4\).')
add('3.58',r'Derivera x² i första omgången och x i den andra. Håll reda på minustecknet när sinus integreras.',[
('Den första omgången ger x cos x',r'<p>Välj \(u=x^2\), \(u\prime=2x\) och \(v=-\cos x\).</p>\[I=\int x^2\sin x\,dx=-x^2\cos x+2J\]<p>Här är \(J=\int x\cos x\,dx\).</p>'),
('Beräkna J med en andra partiell integration',r'<p>Välj \(u=x\), \(u\prime=1\) och \(v=\sin x\).</p>\[J=x\sin x-\int\sin x\,dx\]\[=x\sin x+\cos x\]'),
('Sätt in hela J och multiplicera med 2',r'\[I=-x^2\cos x+2(x\sin x+\cos x)+C\]')],r'\(-x^2\cos x+2x\sin x+2\cos x+C\).')
add('3.76',r'Bestäm en primitiv funktion till produkten. Använd sedan sinus- och cosinusvärdena vid 0 och π.',[
('Derivera x när produkten integreras',r'<p>Välj \(u=x\), \(u\prime=1\) och \(v=\sin x\).</p>\[F(x)=x\sin x-\int\sin x\,dx\]\[=x\sin x+\cos x\]'),
('Beräkna värdet vid båda gränserna',r'\[F(\pi)=\pi\cdot0+(-1)=-1\]\[F(0)=0\cdot0+1=1\]'),
('Subtrahera den undre gränsens värde',r'\[\int_0^\pi x\cos x\,dx=-1-1=-2\]<p>Detta är en integral med tecken, inte summan av områdenas areor.</p>')],r'Integralen är \(-2\).')
add('3.81',r'Kalla integralen I. Integrera partiellt två gånger och samla sedan I-termerna i samma led.',[
('Koppla sinusintegralen till en cosinusintegral',r'<p>Välj \(u=\sin x\), \(u\prime=\cos x\) och \(v=e^x\). Skriv \(J=\int e^x\cos x\,dx\).</p>\[I=e^x\sin x-J\]'),
('Integrera J så att I kommer tillbaka',r'<p>Välj \(u=\cos x\), \(u\prime=-\sin x\) och \(v=e^x\).</p>\[J=e^x\cos x+I\]'),
('Sätt in J och lös ekvationen för I',r'\[I=e^x\sin x-e^x\cos x-I\]\[2I=e^x(\sin x-\cos x)\]<p>Vi har räknat fram en primitiv funktion. Lägg till en godtycklig konstant för hela familjen.</p>')],r'\(e^x(\sin x-\cos x)/2+C\).')
add('3.82',r'Skriv uttrycket som 1·(ln x)² och derivera logaritmens kvadrat. Därefter återstår integralen av ln x.',[
('Derivera logaritmens kvadrat med kedjeregeln',r'<p>Välj \(u=(\ln x)^2\), \(u\prime=2\ln x/x\) och \(v=x\).</p>\[I=x(\ln x)^2-2J\]<p>Här är \(J=\int\ln x\,dx\).</p>'),
('Integrera den återstående logaritmen',r'<p>Med \(u=\ln x\), \(u\prime=1/x\) och \(v=x\) får vi</p>\[J=x\ln x-\int1\,dx=x\ln x-x.\]'),
('Multiplicera båda termerna i J med −2',r'\[I=x(\ln x)^2-2(x\ln x-x)+C\]')],r'\(x(\ln x)^2-2x\ln x+2x+C\), för \(x>0\).')
add('3.90',r'Låt x deriveras. En integrering av e³ˣ ger faktorn 1/3, och exponentialfunktionen behöver integreras två gånger.',[
('Derivera x och integrera e³ˣ',r'<p>Välj \(u=x\), \(u\prime=1\) och \(v=e^{3x}/3\).</p>\[\int xe^{3x}\,dx=\frac{xe^{3x}}3-\frac13\int e^{3x}\,dx\]'),
('Behåll båda faktorerna 1/3',r'\[=\frac{xe^{3x}}3-\frac13\cdot\frac{e^{3x}}3+C\]')],r'\(e^{3x}(x/3-1/9)+C\).')
add('3.145',r'Derivera x och integrera cos(3x). Använd produktregeln när du sedan kontrollerar resultatet.',[
('Integrera produkten genom att derivera x',r'<p>Välj \(u=x\), \(u\prime=1\) och \(v=\sin(3x)/3\).</p>\[F(x)=\frac{x\sin(3x)}3-\frac13\int\sin(3x)\,dx\]\[=\frac{x\sin(3x)}3+\frac{\cos(3x)}9+C\]'),
('Derivera och se att sinustermerna tar ut varandra',r'\[F\prime(x)=\frac{\sin(3x)}3+x\cos(3x)-\frac{\sin(3x)}3\]\[=x\cos(3x)\]')],r'\(F(x)=x\sin(3x)/3+\cos(3x)/9+C\). Kontrollen ger den ursprungliga integranden.')
add('3.91',r'Derivera x. Kontrollera både tecknet och faktorn 1/3 när sinus- och cosinusfunktionerna integreras.',[
('Derivera x och integrera sin(3x)',r'<p>Välj \(u=x\), \(u\prime=1\) och \(v=-\cos(3x)/3\).</p>\[\int x\sin(3x)\,dx\]\[=-\frac{x\cos(3x)}3+\frac13\int\cos(3x)\,dx\]'),
('Integrera cosinus med ytterligare en faktor 1/3',r'\[=-\frac{x\cos(3x)}3+\frac13\cdot\frac{\sin(3x)}3+C\]')],r'\(-x\cos(3x)/3+\sin(3x)/9+C\).')
add('3.92',r'Skriv ln(3x) som en produkt med 1. Vad blir derivatan av ln(3x) när kedjeregeln används?',[
('Derivera logaritmen med kedjeregeln',r'<p>Välj \(u=\ln(3x)\) och \(v\prime=1\). Då är</p>\[u\prime=\frac{3}{3x}=\frac1x,\qquad v=x.\]'),
('Integranden som återstår är 1',r'\[\int\ln(3x)\,dx=x\ln(3x)-\int\frac1x\cdot x\,dx\]\[=x\ln(3x)-x+C\]')],r'\(x\ln(3x)-x+C\), för \(x>0\).')
add('3.95',r'Derivera x² i första omgången. I nästa omgång ska du integrera x sin x.',[
('Derivera x² och integrera cosinus',r'<p>Välj \(u=x^2\), \(u\prime=2x\) och \(v=\sin x\).</p>\[I=\int x^2\cos x\,dx=x^2\sin x-2J\]<p>Här är \(J=\int x\sin x\,dx\).</p>'),
('Beräkna J genom en andra partiell integration',r'<p>Välj \(u=x\), \(u\prime=1\) och \(v=-\cos x\).</p>\[J=-x\cos x+\int\cos x\,dx\]\[=-x\cos x+\sin x\]'),
('Låt faktorn −2 påverka båda termerna',r'\[I=x^2\sin x-2(-x\cos x+\sin x)+C\]')],r'\(x^2\sin x+2x\cos x-2\sin x+C\).')
add('3.96',r'Derivera ln(2x) med kedjeregeln och integrera x. Förenkla produkten i den nya integralen.',[
('Derivera logaritmen och integrera x',r'<p>Välj \(u=\ln(2x)\) och \(v\prime=x\). Då är \(u\prime=2/(2x)=1/x\) och \(v=x^2/2\).</p>'),
('Förenkla och integrera den återstående potensen',r'\[\int x\ln(2x)\,dx\]\[=\frac{x^2\ln(2x)}2-\frac12\int x\,dx\]\[=\frac{x^2\ln(2x)}2-\frac{x^2}4+C\]')],r'\(x^2\ln(2x)/2-x^2/4+C\), för \(x>0\).')
add('3.97',r'Börja med att derivera (ln x)² och integrera faktorn 1. Integrera därefter ln x och sätt in båda gränserna.',[
('Minska logaritmens exponent med partiell integration',r'<p>Välj \(u=(\ln x)^2\), \(u\prime=2\ln x/x\) och \(v=x\).</p>\[F(x)=x(\ln x)^2-2\int\ln x\,dx\]'),
('Beräkna logaritmens primitiva funktion',r'<p>Partiell integration med \(u=\ln x\) och \(v=x\) ger</p>\[\int\ln x\,dx=x\ln x-\int1\,dx=x\ln x-x.\]\[F(x)=x(\ln x)^2-2x\ln x+2x\]'),
('Sätt in gränserna och ta differensen',r'\[F(e)=e\cdot1^2-2e\cdot1+2e=e\]\[F(1)=1\cdot0^2-2\cdot1\cdot0+2=2\]\[\int_1^e(\ln x)^2\,dx=F(e)-F(1)=e-2\]')],r'\(e-2\).')
add('3.318a',r'Låt 2x vara faktorn som deriveras. Vad blir dess derivata?',[
('Derivera 2x och integrera eˣ',r'<p>Välj \(u=2x\), \(u\prime=2\) och \(v=e^x\).</p>\[\int2xe^x\,dx=2xe^x-2\int e^x\,dx\]'),
('Integrera eˣ och samla termerna',r'\[=2xe^x-2e^x+C\]\[=2(x-1)e^x+C\]')],r'\(2(x-1)e^x+C\).')
add('3.318b',r'Låt x+1 deriveras. Kontrollera minustecknet i en primitiv funktion till sin x.',[
('Derivera x+1 och integrera sinus',r'<p>Välj \(u=x+1\), \(u\prime=1\) och \(v=-\cos x\).</p>\[\int(x+1)\sin x\,dx\]\[=-(x+1)\cos x+\int\cos x\,dx\]'),
('Integrera den återstående cosinusfunktionen',r'<p>En primitiv funktion till cos x är sin x. Lägg till en godtycklig konstant.</p>')],r'\(-(x+1)\cos x+\sin x+C\).')
add('3.318c',r'Derivera t och integrera cos(3t). Ta hänsyn till den inre derivatan 3.',[
('Använd t som integrationsvariabel',r'<p>Välj \(u=t\), \(u\prime=1\) och \(v=\sin(3t)/3\).</p>\[\int t\cos(3t)\,dt\]\[=\frac{t\sin(3t)}3-\frac13\int\sin(3t)\,dt\]'),
('Integrera sinus med rätt tecken',r'<p>En primitiv funktion till \(\sin(3t)\) är \(-\cos(3t)/3\). Produkten av de två negativa faktorerna ger plus.</p>')],r'\(t\sin(3t)/3+\cos(3t)/9+C\).')
add('3.318d',r'Derivera x och integrera e⁻²ˣ. Kontrollera både minustecknet och faktorn 1/2.',[
('Derivera x och integrera exponentialfunktionen',r'<p>Välj \(u=x\), \(u\prime=1\) och \(v=-e^{-2x}/2\).</p>\[\int xe^{-2x}\,dx\]\[=-\frac{xe^{-2x}}2+\frac12\int e^{-2x}\,dx\]'),
('Integrera exponentialfunktionen en gång till',r'\[=-\frac{xe^{-2x}}2-\frac{e^{-2x}}4+C\]')],r'\(-xe^{-2x}/2-e^{-2x}/4+C\).')
add('3.319a',r'Låt ln x deriveras och x integreras. Förenkla sedan den nya integranden.',[
('Derivera logaritmen i produkten',r'<p>För \(x>0\) väljer vi \(u=\ln x\), \(u\prime=1/x\) och \(v=x^2/2\).</p>'),
('Integrera den återstående potensen',r'\[\int x\ln x\,dx=\frac{x^2\ln x}2-\frac12\int x\,dx\]\[=\frac{x^2\ln x}2-\frac{x^2}4+C\]')],r'\(x^2\ln x/2-x^2/4+C\), för \(x>0\).')
# Samma integrand som 3.58, men ett eget fristående facit på delkortet.
DATA['3.319b']=dict(DATA['3.58'])
add('3.319c',r'Skriv integranden som ln x · x⁻². Derivera logaritmen och integrera potensen.',[
('Integrera x⁻² med potensregeln',r'<p>För \(x>0\) väljer vi \(u=\ln x\), \(u\prime=1/x\), \(v\prime=x^{-2}\) och \(v=-1/x\).</p>'),
('Förenkla produkten efter partiell integration',r'\[\int\frac{\ln x}{x^2}\,dx=-\frac{\ln x}{x}+\int\frac1{x^2}\,dx\]'),
('Integrera x⁻² en gång till',r'\[\int x^{-2}\,dx=-x^{-1}+C\]')],r'\(-\ln x/x-1/x+C\), för \(x>0\).')
add('3.319d',r'Integrera partiellt två gånger. Samla den återkommande integralen i samma led.',[
('Koppla cosinusintegralen till sinusintegralen',r'<p>Sätt \(I=\int e^x\cos x\,dx\). Välj \(u=\cos x\), \(u\prime=-\sin x\) och \(v=e^x\).</p>\[I=e^x\cos x+J\]<p>Här är \(J=\int e^x\sin x\,dx\).</p>'),
('Integrera J så att I återkommer',r'<p>Med \(u=\sin x\), \(u\prime=\cos x\) och \(v=e^x\) får vi</p>\[J=e^x\sin x-I.\]'),
('Sätt in J och samla I-termerna',r'\[I=e^x\cos x+e^x\sin x-I\]\[2I=e^x(\cos x+\sin x)\]<p>Dividera med 2 och lägg till en godtycklig konstant.</p>')],r'\(e^x(\cos x+\sin x)/2+C\).')
add('3.320a',r'Bestäm först en primitiv funktion med en fri konstant. Sätt sedan in x = 0 i hela uttrycket.',[
('Integrera produkten genom att derivera x+2',r'<p>Välj \(u=x+2\), \(u\prime=1\) och \(v=-\cos x\).</p>\[F(x)=-(x+2)\cos x+\int\cos x\,dx\]\[=-(x+2)\cos x+\sin x+C\]'),
('Bestäm konstanten ur F(0) = 2',r'\[F(0)=-2\cdot1+0+C=2\]\[-2+C=2\quad\Rightarrow\quad C=4\]')],r'\(F(x)=-(x+2)\cos x+\sin x+4\).')
add('3.320b',r'Derivera 2x och integrera e⁻ˣ. Använd därefter punktvillkoret för att bestämma konstanten.',[
('Integrera produkten med rätt minustecken',r'<p>Välj \(u=2x\), \(u\prime=2\) och \(v=-e^{-x}\).</p>\[F(x)=-2xe^{-x}+2\int e^{-x}\,dx\]\[=-2xe^{-x}-2e^{-x}+C\]'),
('Bestäm konstanten ur F(0) = 3',r'\[F(0)=0-2\cdot1+C=3\]\[-2+C=3\quad\Rightarrow\quad C=5\]')],r'\(F(x)=-2xe^{-x}-2e^{-x}+5\).')
add('3.321a',r'Derivera x och integrera sin(2x). Sätt sedan in π/2 och 0 i den primitiva funktionen.',[
('Bestäm en primitiv funktion med partiell integration',r'<p>Välj \(u=x\), \(u\prime=1\) och \(v=-\cos(2x)/2\).</p>\[F(x)=-\frac{x\cos(2x)}2+\frac12\int\cos(2x)\,dx\]\[=-\frac{x\cos(2x)}2+\frac{\sin(2x)}4\]'),
('Beräkna värdet vid båda gränserna',r'\[F(\pi/2)=-\frac{(\pi/2)(-1)}2+0=\frac\pi4\]\[F(0)=0+0=0\]'),
('Ta differensen mellan gränsvärdena',r'\[\int_0^{\pi/2}x\sin(2x)\,dx=\frac\pi4-0\]')],r'\(\pi/4\).')
add('3.321b',r'Låt ln x deriveras. Beräkna sedan F(2) och F(1) separat innan du subtraherar.',[
('Derivera logaritmen och integrera x²',r'<p>Välj \(u=\ln x\), \(u\prime=1/x\) och \(v=x^3/3\).</p>\[F(x)=\frac{x^3\ln x}3-\frac13\int x^2\,dx\]\[=\frac{x^3\ln x}3-\frac{x^3}9\]'),
('Sätt in de två integrationsgränserna',r'\[F(2)=\frac{8\ln2}3-\frac89\]\[F(1)=0-\frac19=-\frac19\]'),
('Subtrahera och samla bråken',r'\[F(2)-F(1)=\frac{8\ln2}3-\frac89+\frac19\]\[=\frac{8\ln2}3-\frac79\]')],r'\(8\ln(2)/3-7/9\).')
# Fördjupa även två nyare facit där valet av faktorer saknades.
add('3.356',r'Efter två partiella integrationer kommer ursprungsintegralen tillbaka. Sätt in det andra sambandet i det första.',[
('Koppla sinusintegralen till cosinusintegralen',r'<p>Sätt \(I=\int e^{2x}\sin x\,dx\). Välj \(u=\sin x\), \(u\prime=\cos x\) och \(v=e^{2x}/2\).</p>\[I=\frac{e^{2x}\sin x}2-\frac J2\]<p>Här är \(J=\int e^{2x}\cos x\,dx\).</p>'),
('Integrera J så att I kommer tillbaka',r'<p>Välj \(u=\cos x\), \(u\prime=-\sin x\) och \(v=e^{2x}/2\).</p>\[J=\frac{e^{2x}\cos x}2+\frac I2\]'),
('Sätt in hela uttrycket för J',r'\[I=\frac{e^{2x}\sin x}2-\frac{e^{2x}\cos x}4-\frac I4\]\[\frac54I=\frac{e^{2x}\sin x}2-\frac{e^{2x}\cos x}4\]<p>Multiplicera båda leden med 4/5. Lägg sedan till den fria konstanten.</p>')],r'\(F(x)=e^{2x}(2\sin x-\cos x)/5+C\).')
add('3.357',r'Kontrollera funktionens tecken i det skuggade intervallet. Bestäm sedan en primitiv funktion och sätt in gränserna.',[
('Den skuggade arean är en positiv integral',r'<p>För \(0\le x\le\pi/2\) är både x och cos x icke-negativa. Arean är därför integralen av x cos x över detta intervall.</p>'),
('Derivera x när produkten integreras',r'<p>Välj \(u=x\), \(u\prime=1\) och \(v=\sin x\).</p>\[F(x)=x\sin x-\int\sin x\,dx\]\[=x\sin x+\cos x\]'),
('Ta värdet vid π/2 minus värdet vid noll',r'\[F(\pi/2)=\frac\pi2\cdot1+0=\frac\pi2\]\[F(0)=0\cdot0+1=1\]\[A=F(\pi/2)-F(0)=\frac\pi2-1\]')],r'\(\pi/2-1\) areaenheter.')
FAMILY_IDS=['3.34','3.55','3.56','3.58','3.81','3.82','3.90','3.145','3.91','3.92','3.95','3.96']
def install():
 path=ROOT/'uppgiftermatf1.js';raw=path.read_text();i=raw.index('[')+1;dec=json.JSONDecoder();edits=[];review=[]
 while True:
  while raw[i].isspace() or raw[i]==',':i+=1
  if raw[i]==']':break
  q,n=dec.raw_decode(raw[i:]);old=json.loads(json.dumps(q));id=q['id']
  if q['omr']=='partiell_integration':
   q.update(DATA.get(id,{}))
   if id in FAMILY_IDS:q['svarFormat']='primitiva'
   if id in ['3.318','3.319']:
    q['svarFormat']=['primitiva']*4
   if q.get('spelDelar'):
    for part in q['spelDelar']:part.update(DATA[id+part['etikett']])
    q['s']='<div class="facit-v2">'+''.join('<div class="facit-del"><span class="facit-mark">'+p['etikett']+')</span><div class="facit-arbete">'+p['s']+'</div></div>' for p in q['spelDelar'])+'</div>'
   # Nivå 1 är ett direkt grundsamband; partiell integration kräver flera led.
   if id in ['3.02','3.14','3.31']:q['traningsniva']=2
   if id=='3.92':q.update(traningsniva=3,niva='C',poang='0/2/0')
   if id=='3.34':q['traningsniva']=4
   if id=='3.318':
    q.update(traningsniva=2,niva='E',poang='4/0/0')
    for part in q['spelDelar']:part.update(traningsniva=2,niva='E',poang='1/0/0')
   # Vanlig räknare tar inte bort valet av metod; CAS skulle göra det.
   q['miniräknare']=True
   # Behåll tidigare förklaringar, men bryt för långa formler i de två gamla referenserna.
   if id=='3.01':
    q['s']=q['s'].replace(r'\[\frac{d}{dx}\left[-e^{-2x}\left(\frac{x^2}{2}+\frac{x}{2}+\frac14\right)\right]=e^{-2x}\left(x^2+x+\frac12-x-\frac12\right)=x^2e^{-2x}.\]',r'<p>Sätt \(P(x)=x^2/2+x/2+1/4\). Produktregeln ger</p>\[(-e^{-2x}P(x))\prime=e^{-2x}(2P(x)-P\prime(x)).\]\[2P(x)-P\prime(x)\]\[=x^2+x+\frac12-(x+\frac12)=x^2.\]<p>Derivatan är alltså \(x^2e^{-2x}\).</p>')
   if id=='3.02':q['s']=q['s'].replace(r'\[\int xe^x\,dx=xe^x-\int e^x\,dx=xe^x-e^x+C.\]',r'\[\int xe^x\,dx=xe^x-\int e^x\,dx\]\[=xe^x-e^x+C.\]')
   mobile=json.loads(Path(__file__).with_name('matf1-partiell-facit-2026-10-26.mobil.json').read_text())
   for target in [q,*q.get('spelDelar',[])]:
    for before,after in mobile.items():target['s']=target['s'].replace(r'\['+before+r'\]',r'\['+after+r'\]')
   changes=[k for k in q if q[k]!=old.get(k)]
   review.append({'id':id,'parts':[p['etikett'] for p in q.get('spelDelar',[])],'changed':changes,'status':'Åtgärdad' if changes else 'Granskad – inget fel','level':q['traningsniva']})
   if changes:edits.append((i,i+n,fields.replace_fields(raw[i:i+n],q)))
  i+=n
 for start,end,new in reversed(edits):raw=raw[:start]+new+raw[end:]
 path.write_text(raw)
 return review
if __name__=='__main__':
 report=install();print('Granskade',len(report),'ändrade',sum(bool(q['changed']) for q in report));
 # Logga första körningens ändringar, inte tomma skillnader vid återkörning.
 if any(q['changed'] for q in report):(ROOT/'agent/MATF1_PARTIELL_FACIT_2026-10-26.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
