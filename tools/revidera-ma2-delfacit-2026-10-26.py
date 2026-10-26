"""Sex manuellt omarbetade huvuduppgifter med 13 självständiga delfacit."""
import json,math,importlib.util,re
from pathlib import Path
from html import escape
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('fields',Path(__file__).with_name('revidera-ma3-facitstruktur-2026-10-25.py'));fields=importlib.util.module_from_spec(spec);spec.loader.exec_module(fields)
def solution(steps,answer):
 return '<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'+''.join('<li><p class="facit-rubrik">'+escape(title)+'</p>'+body+'</li>' for title,body in steps)+'</ol><p class="facit-svar"><strong>Svar:</strong> '+answer+'</p></div>'
def part(label,question,hint,steps,answer,**metadata):return dict(etikett=label,fraga=question,ledtrad=hint,s=solution(steps,answer),**metadata)
PARTS={
'2.261':[
part('a',r'<p>Bestäm startvärdet \(C\). (Svara med två decimaler.)</p>',r'<p>Dividera de två funktionsvärdena för att få ett uttryck för förändringen under tre tidsenheter. Hur backar du sedan två tidsenheter från M(2)?</p>',[
('Kvoten visar förändringen under tre tidsenheter',r'\[\frac{M(5)}{M(2)}=\frac{Ca^5}{Ca^2}=a^3\]\[a^3=\frac{121{,}5}{45}=2{,}7\]'),
('Backa två tidsenheter från det kända värdet 45',r'<p>Två tidsenheters förändring motsvarar \(a^2=(a^3)^{2/3}\). Därför gäller</p>\[45=C\cdot2{,}7^{2/3}\]\[C=\frac{45}{2{,}7^{2/3}}\approx23{,}207944\]')],r'\(C\approx23{,}21\).',traningsniva=3,arbetsinsats=2),
part('b',r'<p>Bestäm förändringsfaktorn \(a\). (Svara med tre decimaler.)</p>',r'<p>Hur många tidsenheter skiljer det mellan de två givna värdena? Kvoten mellan värdena motsvarar förändringen under hela den tiden.</p>',[
('Dividera värdena så att startvärdet försvinner',r'\[\frac{121{,}5}{45}=a^{5-2}=a^3\]\[a^3=2{,}7\]'),
('Ta kubikroten för att få förändringen per tidsenhet',r'\[a=\sqrt[3]{2{,}7}\approx1{,}39247665\]<p>Avrunda först nu till tre decimaler. Fjärde decimalen är 4.</p>')],r'\(a\approx1{,}392\).',traningsniva=3,arbetsinsats=1),
part('c',r'<p>Modellen kan också skrivas \(M(t)=45\cdot2{,}7^{(t-2)/3}\). När når mängden värdet 200? (Svara med två decimaler.)</p>',r'<p>Sätt modellens värde lika med 200. Dividera med 45 och använd en logaritm för att lösa ut exponenten.</p>',[
('Sätt in det efterfrågade värdet i modellen',r'\[45\cdot2{,}7^{(t-2)/3}=200\]\[2{,}7^{(t-2)/3}=\frac{200}{45}\]'),
('Logaritmera för att få ner exponenten',r'\[\frac{t-2}{3}\lg2{,}7=\lg\frac{200}{45}\]'),
('Lös ut t och avrunda först på slutet',r'\[t=2+3\frac{\lg(200/45)}{\lg2{,}7}\]\[t\approx6{,}5053679\]')],r'\(t\approx6{,}51\) tidsenheter.',traningsniva=3,arbetsinsats=2)
],
'2.330':[
part('a',r'<p>Bestäm funktionen på faktoriserad form.</p>',r'<p>Vilka faktorer blir noll vid x = 1 respektive x = 7? Använd sedan det givna funktionsvärdet för att bestämma faktorn framför.</p>',[
('Nollställena bestämmer två faktorer',r'\[f(x)=a(x-1)(x-7)\]'),
('Punkten med x = 3 bestämmer faktorn a',r'\[-16=a(3-1)(3-7)=-8a\]\[a=2\]')],r'\(f(x)=2(x-1)(x-7)\).',traningsniva=3,arbetsinsats=2),
part('b',r'<p>Funktionen är \(f(x)=2(x-1)(x-7)\). Bestäm dess minsta värde.</p>',r'<p>Symmetrilinjen ligger mitt emellan nollställena. Vad blir funktionsvärdet där?</p>',[
('Symmetrilinjen ligger mitt emellan nollställena',r'\[x=\frac{1+7}{2}=4\]<p>Koefficienten framför x² är positiv. Parabeln öppnar därför uppåt och har sitt minimum på symmetrilinjen.</p>'),
('Beräkna funktionsvärdet på symmetrilinjen',r'\[f(4)=2(4-1)(4-7)\]\[=2\cdot3\cdot(-3)=-18\]')],r'Minsta värdet är \(-18\).',traningsniva=2,arbetsinsats=1)
],
'2.333':[
part('a',r'<p>Bestäm funktionen på toppform.</p>',r'<p>Toppformen skrivs med avståndet till symmetrilinjen. Punkten (5, 9) bestämmer sedan faktorn framför kvadraten.</p>',[
('Minimipunkten ger förskjutningarna i toppformen',r'\[f(x)=a(x-2)^2-9\]'),
('Använd den andra punkten för att bestämma a',r'\[9=a(5-2)^2-9\]\[18=9a\quad\Rightarrow\quad a=2\]')],r'\(f(x)=2(x-2)^2-9\).',traningsniva=3,arbetsinsats=2),
part('b',r'<p>Funktionen är \(f(x)=2(x-2)^2-9\). Bestäm nollställena. (Svara med två decimaler.)</p>',r'<p>Sätt f(x) = 0 och isolera kvadraten. Kom ihåg båda tecknen när du tar kvadratroten.</p>',[
('Vid nollställena är funktionsvärdet noll',r'\[2(x-2)^2-9=0\]\[(x-2)^2=\frac92\]'),
('Båda rötterna ligger lika långt från symmetrilinjen',r'\[x=2\pm\sqrt{\frac92}\]\[x_1\approx-0{,}1213203\]\[x_2\approx4{,}1213203\]')],r'\(x\approx-0{,}12\) och \(x\approx4{,}12\).',traningsniva=3,arbetsinsats=2)
],
'2.336':[
part('a',r'<p>Teckna areafunktionen \(A(x)\).</p>',r'<p>Kalla den andra sidan y och skriv en ekvation för hela omkretsen. Arean är produkten av de två sidlängderna.</p>',[
('Omkretsen bestämmer den andra sidlängden',r'\[2x+2y=120\]\[x+y=60\quad\Rightarrow\quad y=60-x\]'),
('Multiplicera rektangelns två sidlängder',r'\[A(x)=x(60-x)=-x^2+60x\]<p>Båda sidorna måste vara positiva, alltså \(0\lt x\lt60\).</p>')],r'\(A(x)=-x^2+60x\) m², för \(0\lt x\lt60\).',traningsniva=2,arbetsinsats=2),
part('b',r'<p>Areafunktionen är \(A(x)=-x^2+60x\), där \(0\lt x\lt60\). Bestäm den största möjliga arean. (Svara i m².)</p>',r'<p>Parabeln öppnar nedåt. Bestäm var dess symmetrilinje ligger och beräkna arean där.</p>',[
('Nollställena ger parabelns symmetrilinje',r'<p>Uttrycket \(x(60-x)\) är noll vid x = 0 och x = 60. Symmetrilinjen ligger mitt emellan:</p>\[x=\frac{0+60}{2}=30\]'),
('Kontrollera att toppen ger en tillåten maximal area',r'<p>Koefficienten framför x² är negativ, så toppen är ett maximum. Värdet x = 30 ligger i det tillåtna intervallet.</p>\[A(30)=-30^2+60\cdot30\]\[=-900+1800=900\]')],r'Största arean är \(900\) m².',traningsniva=3,arbetsinsats=2)
],
'2.347':[
part('a',r'<p>Bestäm potensfunktionen.</p>',r'<p>Vad blir en potens av 1? Använd den första punkten till C och den andra till exponenten.</p>',[
('Punkten med x = 1 ger konstanten C',r'\[5=C\cdot1^a=C\]'),
('Den andra punkten ger en ekvation för exponenten',r'\[40=5\cdot4^a\]\[4^a=8\]'),
('Skriv båda leden som potenser av 2',r'\[(2^2)^a=2^3\]\[2a=3\quad\Rightarrow\quad a=\frac32\]')],r'\(f(x)=5x^{3/2}\).',traningsniva=3,arbetsinsats=2),
part('b',r'<p>Potensfunktionen är \(f(x)=5x^{3/2}\). Bestäm \(f(9)\).</p>',r'<p>Exponentens nämnare 2 innebär en kvadratrot. Beräkna potensen innan du multiplicerar med 5.</p>',[
('Sätt in 9 som funktionens argument',r'\[f(9)=5\cdot9^{3/2}\]'),
('Beräkna potensen och multiplicera med 5',r'\[9^{3/2}=(\sqrt9)^3=3^3=27\]\[f(9)=5\cdot27=135\]')],r'\(f(9)=135\).',traningsniva=2,arbetsinsats=1)
],
'2.354':[
part('a',r'<p>Bestäm modellen.</p>',r'<p>Dividera funktionsvärdena för att få bort faktorn a. Vad blir förhållandet mellan x-värdena?</p>',[
('De två punkterna ger varsin ekvation',r'\[18=a\cdot2^n,\quad288=a\cdot8^n\]'),
('Kvoten mellan ekvationerna bestämmer exponenten',r'\[\frac{288}{18}=\left(\frac82\right)^n\]\[16=4^n\quad\Rightarrow\quad n=2\]'),
('Använd det första värdet för att bestämma a',r'\[18=a\cdot2^2=4a\]\[a=\frac{18}{4}=4{,}5\]')],r'\(f(x)=4{,}5x^2\).',traningsniva=3,arbetsinsats=2),
part('b',r'<p>Modellen är \(f(x)=4{,}5x^2\). Bestäm det positiva x-värdet som ger \(f(x)=72\).</p>',r'<p>Sätt modellens värde lika med 72. Isolera x² och använd sedan villkoret att x ska vara positivt.</p>',[
('Sätt funktionsvärdet lika med 72',r'\[4{,}5x^2=72\]\[x^2=\frac{72}{4{,}5}=16\]'),
('Välj roten som uppfyller frågans villkor',r'<p>Ekvationen har rötterna −4 och 4. Endast 4 är positiv.</p>\[f(4)=4{,}5\cdot16=72\]')],r'\(x=4\).',traningsniva=2,arbetsinsats=1)
]}
MAIN_QUESTIONS={
'2.261':r'<p>a) Bestäm startvärdet C. (Svara med två decimaler.)</p><p>b) Bestäm förändringsfaktorn a. (Svara med tre decimaler.)</p><p>c) När når modellen värdet 200? (Svara med två decimaler.)</p>',
'2.330':r'<p>a) Bestäm funktionen på faktoriserad form.</p><p>b) Bestäm funktionens minsta värde.</p>',
'2.333':r'<p>a) Bestäm funktionen på toppform.</p><p>b) Bestäm nollställena. (Svara med två decimaler.)</p>',
'2.336':r'<p>a) Teckna areafunktionen \(A(x)\).</p><p>b) Bestäm den största möjliga arean. (Svara i m².)</p>',
'2.347':r'<p>a) Bestäm potensfunktionen.</p><p>b) Bestäm \(f(9)\).</p>',
'2.354':r'<p>a) Bestäm modellen.</p><p>b) Bestäm det positiva x-värdet som ger \(f(x)=72\).</p>'
}
def install():
 p=ROOT/'uppgifterma2.js';raw=p.read_text()
 for id,parts in PARTS.items():
  pos=re.search(r'"id"\s*:\s*"'+re.escape(id)+'"',raw).start();start=raw.rfind('{',0,pos);q,n=json.JSONDecoder().raw_decode(raw[start:])
  q['spelDelar']=parts
  q['s']='<div class="facit-v2 facit-stegvis">'+''.join('<div class="facit-del"><span class="facit-mark">'+part['etikett']+')</span><div class="facit-arbete">'+part['s']+'</div></div>' for part in parts)+'</div>'
  q['ledtrad']=parts[0]['ledtrad']
  q['t']=q['spelIntro']+MAIN_QUESTIONS[id]
  # Självständiga delkort får hela situationen, med givna mellanresultat där de behövs.
  for part in parts:part['t']=q['spelIntro']+part['fraga']
  if id=='2.261':
   a=2.7**(1/3);q['rättSvar']=[45/a**2,a,2+3*math.log(200/45)/math.log(2.7)];q['tolerans']=[.005,.0005,.005]
  if id=='2.354':
   for field in ['t','spelIntro']:q[field]=q[field].replace(r'y=ax^n',r'f(x)=ax^n')
   for part in parts:part['t']=part['t'].replace(r'y=ax^n',r'f(x)=ax^n')
  raw=raw[:start]+fields.replace_fields(raw[start:start+n],q)+raw[start+n:]
 p.write_text(raw)
if __name__=='__main__':install();print('6 huvudfacit och 13 delfacit manuellt omarbetade.')
