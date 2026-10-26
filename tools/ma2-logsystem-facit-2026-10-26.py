import json,re,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('first',Path(__file__).with_name('revidera-ma2-delfacit-2026-10-26.py'));m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
D={
'2.636':m.solution([
('Produktlagen omvandlar den första ekvationen',r'\[\lg x+\lg y=\lg(xy)=2\]\[xy=10^2=100\]'),
('Kvotlagen ger förhållandet mellan x och y',r'\[\lg x-\lg y=\lg\frac xy=\lg4\]\[\frac xy=4\quad\Rightarrow\quad x=4y\]'),
('Sätt in x = 4y i produkten och välj positiv rot',r'\[4y\cdot y=100\]\[y^2=25\]<p>Eftersom y måste vara positivt väljer vi y = 5. Då blir x = 4 · 5 = 20.</p>'),
('Kontrollera både produkten och kvoten',r'\[20\cdot5=100,\qquad\frac{20}{5}=4\]<p>Båda talen är positiva, så logaritmerna är definierade och båda ursprungliga ekvationerna stämmer.</p>')],r'\(x=20\) och \(y=5\).'),
'2.637':m.solution([
('Byt variabler så att logaritmerna blir u och v',r'<p>Sätt u = lg x och v = lg y. Systemet blir</p>\[u+v=2,\qquad u^2+v^2=5.\]'),
('Sätt v = 2 − u i ekvationen med kvadrater',r'\[u^2+(2-u)^2=5\]\[2u^2-4u-1=0\]\[u^2-2u-\frac12=0\]'),
('Kvadratkomplettera och behåll båda rötterna',r'\[(u-1)^2=\frac32\]\[u=1\pm\frac{\sqrt6}{2}\]<p>Eftersom v = 2 − u får v motsatt tecken framför rottermen.</p>'),
('Gå tillbaka från logaritmer till positiva x och y',r'<p>För den första lösningen är</p>\[x_1=10^{1+\sqrt6/2}\]\[y_1=10^{1-\sqrt6/2}.\]<p>Den andra lösningen fås genom att byta plats på dessa två värden. Båda är positiva eftersom de är potenser av 10.</p>'),
('Kontrollera summan och kvadratsumman av logaritmerna',r'<p>Sätt r = √6/2, så att r² = 3/2. Då är logaritmerna 1 + r och 1 − r:</p>\[(1+r)+(1-r)=2\]\[(1+r)^2+(1-r)^2\]\[=2+2r^2=2+3=5.\]')],r'\((x,y)=(10^{1+\sqrt6/2},\,10^{1-\sqrt6/2})\) eller paret i omvänd ordning.')}
p=ROOT/'uppgifterma2.js';raw=p.read_text()
for id,solution in D.items():
 pos=re.search(r'"id"\s*:\s*"'+re.escape(id)+'"',raw).start();start=raw.rfind('{',0,pos);q,n=json.JSONDecoder().raw_decode(raw[start:]);q['s']=solution;q['svarstyp']='resonemang';q['rättSvar']=None
 raw=raw[:start]+json.dumps(q,ensure_ascii=False)+raw[start+n:]
p.write_text(raw)
