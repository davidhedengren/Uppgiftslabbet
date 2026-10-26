"""Manuellt författade lösningar till ytterligare 16 huvuduppgifter."""
import json,re,math,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('first',Path(__file__).with_name('revidera-ma2-delfacit-2026-10-26.py'));first=importlib.util.module_from_spec(spec);spec.loader.exec_module(first)
# Varje tuple innehåller en specifik ledtråd, manuella steg och svarsrad.
D={
'2.370':[
(r'<p>Sätt in x-värdet i den givna modellen och gör multiplikationen före additionen.</p>', [('Sätt in 6 i regressionsmodellen',r'\[y=1{,}52\cdot6+1{,}3\]\[=9{,}12+1{,}3=10{,}42\]')],r'Modellvärdet är \(10{,}42\).'),
(r'<p>I en linjär modell beskriver koefficienten framför x förändringen per x-enhet.</p>', [('Koefficienten framför x anger ökningen per steg',r'<p>När x ökar med 1 förändras termen 1,52x med 1,52. Konstanten 1,3 ändras inte. Därför ökar y med 1,52 för varje x-enhet.</p>')],r'Ökningen är \(1{,}52\) per x-enhet.')],
'2.389':[
(r'<p>Skriv en linjär funktion med en okänd konstantterm. Vad säger den givna ökningen om lutningen?</p>', [('Ökningen per x-enhet ger lutningen 3',r'\[f(x)=3x+m\]'),('Använd värdet vid x = 2 för att bestämma m',r'\[7=3\cdot2+m\]\[m=7-6=1\]')],r'\(f(x)=3x+1\).'),
(r'<p>I f(2x) ska hela argumentet 2x ersätta x i funktionsuttrycket.</p>', [('Skriv ut båda leden med funktionsformeln',r'\[f(2x)=3\cdot2x+1=6x+1\]\[f(x)+15=3x+1+15\]\[=3x+16\]'),('Samla x-termerna och lös den linjära ekvationen',r'\[6x+1=3x+16\]\[3x=15\quad\Rightarrow\quad x=5\]')],r'\(x=5\).')],
'2.390':[
(r'<p>Använd parenteser när du sätter in det negativa talet. Skilj mellan kvadraten och termen med minustecken.</p>', [('Ersätt varje x med −2',r'\[g(-2)=2(-2)^2-(-2)+4\]'),('Kvadraten och minus ett negativt tal är positiva',r'\[g(-2)=2\cdot4+2+4=14\]')],r'\(g(-2)=14\).'),
(r'<p>Sätt in 1 i varje term i funktionsuttrycket.</p>', [('Beräkna funktionsvärdet vid x = 1',r'\[g(1)=2\cdot1^2-1+4\]\[=2-1+4=5\]')],r'\(g(1)=5\).')],
'2.426':[
(r'<p>Multiplicera först x-värdet med −4 och lägg sedan till 9.</p>', [('Sätt in x = 2 i den linjära funktionen',r'\[f(2)=-4\cdot2+9=-8+9=1\]')],r'\(f(2)=1\).'),
(r'<p>Vad blir produkten av två negativa tal?</p>', [('Ersätt x med −1 och håll reda på tecknen',r'\[f(-1)=-4\cdot(-1)+9\]\[=4+9=13\]')],r'\(f(-1)=13\).'),
(r'<p>Här är funktionsvärdet känt. Sätt uttrycket för f(x) lika med 5.</p>', [('Skriv ekvationen för det givna funktionsvärdet',r'\[-4x+9=5\]'),('Subtrahera 9 och dividera med −4',r'\[-4x=-4\quad\Rightarrow\quad x=1\]')],r'\(x=1\).')],
'2.428':[
(r'<p>Leta upp 3 bland x-värdena och läs sedan det tillhörande funktionsvärdet.</p>', [('Läs värdet som hör till x = 3',r'<p>I kolumnen där x = 3 står funktionsvärdet −1. Därför är f(3) = −1.</p>')],r'\(f(3)=-1\).'),
(r'<p>Leta den här gången efter 4 bland funktionsvärdena och läs det tillhörande x-värdet.</p>', [('Läs argumentet som hör till funktionsvärdet 4',r'<p>Funktionsvärdet 4 står i kolumnen där x = 0. Det innebär f(0) = 4.</p>')],r'\(x=0\).'),
(r'<p>Värdet inne i parentesen är indata. Talet efter likhetstecknet är funktionens utdata.</p>', [('Placera argumentet 5 i parentesen och värdet 6 efter likhetstecknet',r'<p>Med funktionssymbolen f skrivs sambandet</p>\[f(5)=6.\]')],r'\(f(5)=6\).')],
'2.433':[
(r'<p>Sätt parentes kring −2. Vilket tecken får produkten av −3 och −2?</p>', [('Sätt in −2 och beräkna tecknen',r'\[f(-2)=5-3(-2)\]\[=5+6=11\]')],r'\(f(-2)=11\).'),
(r'<p>Beräkna multiplikationen innan du subtraherar från 5.</p>', [('Sätt in 4 i funktionsuttrycket',r'\[f(4)=5-3\cdot4=5-12=-7\]')],r'\(f(4)=-7\).'),
(r'<p>Du söker indata, inte utdata. Sätt funktionsuttrycket lika med det givna värdet 2.</p>', [('Skriv ekvationen och subtrahera 5',r'\[5-3x=2\]\[-3x=-3\]'),('Dividera båda leden med −3',r'\[x=1\]<p>Kontroll: f(1) = 5 − 3 = 2.</p>')],r'\(x=1\).')],
'2.444':[
(r'<p>Vilken rot upphäver att ett tal är upphöjt till 3?</p>', [('Ta kubikroten eftersom x är basen',r'\[x^3=50\quad\Rightarrow\quad x=\sqrt[3]{50}\]'),('Avrunda rotens värde till en decimal',r'\[x\approx3{,}6840\approx3{,}7\]')],r'\(x\approx3{,}7\).'),
(r'<p>Här står x i exponenten. Använd en logaritm för att få ner exponenten.</p>', [('Logaritmera båda leden',r'\[\lg(3^x)=\lg50\]\[x\lg3=\lg50\]'),('Dividera med lg 3 och avrunda',r'\[x=\frac{\lg50}{\lg3}\approx3{,}5609\]')],r'\(x\approx3{,}6\).')],
'2.445':[
(r'<p>Undersök om det okända talet står i basen eller i exponenten.</p>', [('I x³ är det basen som är okänd',r'<p>Exponentens värde är det fasta talet 3. Därför är x³ = 20 en potensekvation. Den löses genom att ta kubikroten:</p>\[x=\sqrt[3]{20}.\]')],r'Potensekvation.'),
(r'<p>Vilken del av potensen 3 upphöjt till x innehåller det okända talet?</p>', [('I 3ˣ är det exponenten som är okänd',r'<p>Basen är det fasta talet 3. Därför är 3ˣ = 20 en exponentialekvation. Med logaritmer får man</p>\[x\lg3=\lg20\]\[x=\frac{\lg20}{\lg3}.\]')],r'Exponentialekvation.')],
'2.459':[
(r'<p>Vilken förändringsfaktor motsvarar en ökning med 4 %? Startvärdet multipliceras med den faktorn en gång per år.</p>', [('Ökningen med 4 % ger förändringsfaktorn 1,04',r'\[a=1+\frac4{100}=1{,}04\]'),('Multiplicera startvärdet med faktorn t gånger',r'<p>Låt t vara antalet år från start.</p>\[V(t)=8000\cdot1{,}04^t\]')],r'\(V(t)=8000\cdot1{,}04^t\) kr.'),
(r'<p>Förändringsfaktorn används en gång för varje år. Hur många gånger ska den därför multipliceras med sig själv?</p>', [('Beräkna fem års upprepad procentuell ökning',r'\[V(5)=8000\cdot1{,}04^5\]\[V(5)\approx9733{,}2232\text{ kr}\]'),('Avrunda beloppet till hela kronor',r'<p>Decimaldelen är mindre än 0,5, så beloppet avrundas till 9 733 kr.</p>')],r'\(9733\) kr.')],
'2.460':[
(r'<p>Kvoten mellan slutvärdet och startvärdet beskriver två tidsenheters förändring. Hur får du faktorn för en enda tidsenhet?</p>', [('Två tidsenheter motsvarar förändringsfaktorn i kvadrat',r'\[a^2=\frac{972}{1200}=0{,}81\]'),('Välj den positiva roten för en förändringsfaktor',r'\[a=\sqrt{0{,}81}=0{,}9\]')],r'Förändringsfaktorn är \(0{,}9\).'),
(r'<p>Använd startvärdet och den givna förändringsfaktorn i exponentialmodellens form.</p>', [('Startvärdet multipliceras med förändringsfaktorn en gång per tidsenhet',r'<p>Vid t = 0 är mängden 1 200. Varje tidsenhet återstår 90 % av föregående mängd.</p>\[N(t)=1200\cdot0{,}9^t\]'),('Kontrollera modellen efter två tidsenheter',r'\[N(2)=1200\cdot0{,}9^2\]\[=1200\cdot0{,}81=972\]')],r'\(N(t)=1200\cdot0{,}9^t\).')],
'2.461':[
(r'<p>Startvärdet är värdet vid t = 0. Vad blir förändringsfaktorn upphöjd till noll?</p>', [('Sätt t = 0 i modellen',r'\[P(0)=850\cdot1{,}04^0\]\[=850\cdot1=850\]')],r'Startvärdet är \(850\).'),
(r'<p>En faktor på 1 motsvarar oförändrat värde. Hur mycket större än 1 är den givna faktorn?</p>', [('Översätt förändringsfaktorn till procentuell ökning',r'\[(1{,}04-1)\cdot100\,\%=4\,\%\]')],r'Ökningen är \(4\,\%\) per tidsenhet.')],
'2.462':[
(r'<p>Punkten med x = 1 ger faktorn framför potensen. Jämför sedan vad som händer med y när x fördubblas.</p>', [('Värdet vid x = 1 ger a = 5',r'\[5=a\cdot1^n=a\]'),('Fördubblingen av x ger exponenten n',r'\[20=5\cdot2^n\]\[2^n=4\quad\Rightarrow\quad n=2\]'),('Kontrollera med den tredje givna punkten',r'\[5\cdot4^2=80\]<p>Även den tredje punkten följer modellen.</p>')],r'\(y=5x^2\).'),
(r'<p>Sätt in det givna x-värdet i modellen och beräkna kvadraten först.</p>', [('Beräkna tabellvärdet vid x = 8',r'\[y=5\cdot8^2=5\cdot64=320\]')],r'Tabellvärdet ska vara \(320\).')],
'2.463':[
(r'<p>Dividera massorna med varandra. Då försvinner konstanten C och bara skalförhållandet och exponenten återstår.</p>', [('Kvoten mellan massorna ger en ekvation för exponenten',r'\[\frac{144}{18}=\frac{C\cdot4^a}{C\cdot2^a}\]\[8=\left(\frac42\right)^a=2^a\]'),('Jämför med en känd potens av 2',r'\[8=2^3\quad\Rightarrow\quad a=3\]')],r'\(a=3\).'),
(r'<p>Sätt in den givna massan och längdskalan i modellen med exponenten 3.</p>', [('Använd massan vid längdskalan 2',r'\[18=C\cdot2^3=8C\]'),('Dividera med 8 för att bestämma C',r'\[C=\frac{18}{8}=2{,}25\]')],r'\(C=2{,}25\).'),
(r'<p>Sätt massan lika med 80 och isolera s³. Vilken rot behövs för att få s?</p>', [('Sätt in massan i den givna modellen',r'\[2{,}25s^3=80\]\[s^3=\frac{80}{2{,}25}\]'),('Ta kubikroten och avrunda längdskalan',r'\[s=\sqrt[3]{\frac{80}{2{,}25}}\approx3{,}2883\]')],r'\(s\approx3{,}29\).')],
'2.464':[
(r'<p>Beräkna först 2 upphöjt till 3 och multiplicera sedan med koefficienten.</p>', [('Sätt in x = 2 i potensfunktionen',r'\[f(2)=2{,}5\cdot2^3\]\[=2{,}5\cdot8=20\]')],r'\(f(2)=20\).'),
(r'<p>Jämför uttrycken när argumentet är x respektive 2x. Hur påverkas en tredje potens av fördubblingen?</p>', [('Fördubblingen blir en faktor i tredje potens',r'<p>För en potensfunktion f(x) = kx³ gäller</p>\[f(2x)=k(2x)^3=8kx^3\]\[=8f(x).\]<p>Koefficienten k påverkar inte förändringsfaktorn.</p>')],r'Funktionsvärdet multipliceras med \(8\).')],
'2.493':[
(r'<p>En positiv bas upphöjd till noll är 1. Använd det i uttrycket för f(0).</p>', [('Beräkna potensen vid x = 0',r'\[f(0)=3\cdot1{,}5^0=3\cdot1=3\]')],r'\(f(0)=3\).'),
(r'<p>Jämför förändringsfaktorn med 1. Blir ett positivt värde större eller mindre när det multipliceras med faktorn?</p>', [('Faktorn 1,5 gör värdet större för varje steg',r'<p>Startvärdet är positivt och förändringsfaktorn 1,5 är större än 1. Därför ökar f(x) när x ökar.</p>')],r'Funktionen är växande.')],
'2.495':[
(r'<p>Vad blir potensen när exponenten är noll?</p>', [('Sätt in x = 0 i exponentialfunktionen',r'\[g(0)=8\cdot0{,}75^0=8\cdot1=8\]')],r'\(g(0)=8\).'),
(r'<p>Förändringsfaktorn talar om vilken andel som återstår. Jämför med hela det ursprungliga värdet.</p>', [('Dra den återstående andelen från 100 %',r'<p>Faktorn 0,75 innebär att 75 % återstår.</p>\[100\,\%-75\,\%=25\,\%\]')],r'Minskningen är \(25\,\%\).'),
(r'<p>Jämför förändringsfaktorn med 0 och 1. Vad händer när ett positivt värde multipliceras med den?</p>', [('En faktor mellan 0 och 1 gör de positiva värdena mindre',r'<p>Startvärdet är positivt och \(0\lt0{,}75\lt1\). Varje steg till höger ger därför ett mindre funktionsvärde.</p>')],r'Funktionen är avtagande.')]
}
def install():
 p=ROOT/'uppgifterma2.js';raw=p.read_text()
 for id,parts in D.items():
  pos=re.search(r'"id"\s*:\s*"'+re.escape(id)+'"',raw).start();start=raw.rfind('{',0,pos);q,n=json.JSONDecoder().raw_decode(raw[start:]);assert len(parts)==len(q['spelDelar'])
  for part,(hint,steps,answer) in zip(q['spelDelar'],parts):part['ledtrad']=hint;part['s']=first.solution(steps,answer)
  q['ledtrad']=parts[0][0]
  q['s']='<div class="facit-v2 facit-stegvis">'+''.join('<div class="facit-del"><span class="facit-mark">'+part['etikett']+')</span><div class="facit-arbete">'+part['s']+'</div></div>' for part in q['spelDelar'])+'</div>'
  if id=='2.390':q['s']+='<p>Jämförelse: g(−2) = 14 är större än g(1) = 5.</p>'
  if id=='2.444':q['s']+='<p>I a) är basen okänd och vi använder en rot. I b) är exponenten okänd och vi använder logaritmer.</p>'
  if id=='2.428':
   q['svarFormat'][2]='text';q['rättSvar'][2]='f(5)=6 eller 6=f(5)'
   table=re.search(r'<table[\s\S]*?</table>',q['t']).group()
   q['spelDelar'][0]['t']='<p>Tabellen visar värden för funktionen f.</p>'+table+'<p>Bestäm f(3).</p>'
   q['spelDelar'][1]['t']='<p>Tabellen visar värden för funktionen f.</p>'+table+'<p>Vilket x-värde ger f(x) = 4?</p>'
  if id=='2.459':
   q['spelDelar'][0]['t']=r'<p>En summa på 8 000 kr ökar med 4 % per år. Skriv en modell \(V(t)\), där t är antalet år från start och V(t) värdet i kronor.</p>'
   q['rättSvar'][1]=8000*1.04**5;q['tolerans'][1]=.5;q['spelDelar'][1]['svarEnhet']='kr'
  if id=='2.460':q['spelDelar'][1]['t']=r'<p>Startvärdet är 1200 och förändringsfaktorn per tidsenhet är 0,9. Skriv modellen \(N(t)\), där t är antalet tidsenheter från start.</p>'
  if id=='2.463':q['rättSvar'][2]=(80/2.25)**(1/3);q['tolerans'][2]=.005
  raw=raw[:start]+first.fields.replace_fields(raw[start:start+n],q)+raw[start+n:]
 p.write_text(raw)
if __name__=='__main__':install();print(len(D),'huvuduppgifter,',sum(map(len,D.values())),'delfacit omarbetade.')
