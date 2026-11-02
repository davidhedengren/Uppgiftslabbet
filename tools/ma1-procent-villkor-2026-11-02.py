"""Synliga påståenden och nödvändiga villkor i sju Ma1-uppgifter."""
import json,re
from pathlib import Path
p=Path(__file__).resolve().parent.parent/'uppgifterma1.js';s=p.read_text(encoding='utf8');dec=json.JSONDecoder();pos=s.index('[')+1;changes=[];found=set()
C={
'1.82':[None,'Multiplicera även −3 med −2: 5x−3x+6=2x+6.','Den konstanta termen är 6, eftersom −3 gånger −2 är 6.','Den konstanta termen är +6, inte −2.'],
'3.210':['Kvadratroten är aldrig negativ. För negativa a är √(a²)=−a.','Exempelvis a=2 ger √(2²)=2, så likheten gäller för fler än noll.','För negativa a är roten positiv medan a är negativt; de är inte lika.',None],
'3.411':['7 % årlig minskning ger faktorn 0,93⁶, ungefär 64,7 %, inte 65 %.','A lämnar cirka 64,7 % och B lämnar 65 %; de har bytt plats.','0,93⁶ är cirka 0,647. B är därför bara något högre än A.',None],
'3.453':['Procentenheter används för skillnaden mellan två procentsatser, inte mellan två priser.','Ökningen är 20 kr av 200 kr, alltså 20/200=10 %.','Ökningen är 20 kr, men det är 10 % av det ursprungliga priset 200 kr.',None],
'3.454':['Skillnaden mellan procentsatserna är 25−20=5 procentenheter.','Fem procentenheter är inte samma som 5 % relativ ökning; 5/20=25 %.','125 % är det nya stödets andel av det gamla; den relativa ökningen är 25 %.',None],
'3.512':['Årliga procentuella förändringar multipliceras: 1,10³ är ungefär 1,33.','30 % gäller för hela perioden. Samma årliga procentsats ger faktorn ³√1,30.','Förändringsfaktorer multipliceras mellan åren, så procenttalen kan inte bara delas.',None],
'3.526':['Samma räntesats ger samma procentuella ökning för båda kontona.','Med positiv ränta växer också skillnaden mellan kontona; den blir större än 5 000 kr.',None,'Samma räntesats ger dubbelt så stor ränteökning i kronor på det dubbelt så stora beloppet.']}
while True:
 while s[pos].isspace() or s[pos]==',':pos+=1
 if s[pos]==']':break
 q,end=dec.raw_decode(s,pos);id=q.get('id');chunk=s[pos:end]
 if id in C:
  t=q['t'];assert t.endswith('</p>') and 'alternativ' not in t.lower()
  if id=='3.411':t=t.replace('Två modeller beskriver en minskning under sex år.','Två modeller utgår från samma positiva startvärde och beskriver en minskning under sex år.')
  if id=='3.512':t=t.replace('den genomsnittliga ökningen är 10 % per år.','ökningen är 10 % per år om den är lika stor i procent varje år.')
  if id=='3.526':t=t.replace('Två konton har samma räntesats.','Två konton har samma positiva räntesats. Räntan läggs till kontona varje år.').replace('utan uttag?','utan insättningar eller uttag?')
  old='"t": '+json.dumps(q['t'],ensure_ascii=False);new='"t": '+json.dumps(t[:-4]+' Välj ett alternativ.</p>',ensure_ascii=False);assert chunk.count(old)==1;chunk=chunk.replace(old,new,1)
  assert len(q['alternativ'])==len(C[id]) and sum(a['ratt'] for a in q['alternativ'])==1
  for alt,text in zip(q['alternativ'],C[id]):
   if alt['ratt']:assert text is None;continue
   assert text and 'kommentar' not in alt
   pattern=r'"txt"\s*:\s*'+re.escape(json.dumps(alt['txt'],ensure_ascii=False))+r'\s*,\s*"ratt"\s*:\s*false'
   chunk,n=re.subn(pattern,lambda m:m.group(0)+', "kommentar": '+json.dumps(text,ensure_ascii=False),chunk,count=1);assert n==1,(id,alt['txt'])
  assert json.loads(chunk)['id']==id;changes.append((pos,end,chunk));found.add(id)
 pos=end
assert found==set(C)
for a,b,c in reversed(changes):s=s[:a]+c+s[b:]
json.loads(s[s.index('['):s.rindex(']')+1]);p.write_text(s,encoding='utf8');print('Ändrade:',', '.join(sorted(found)))
