"""Gör sex alternativberoende modell- och uttrycksfrågor självständiga."""
import json,re
from pathlib import Path
p=Path(__file__).resolve().parent.parent/'uppgifterma1.js';s=p.read_text(encoding='utf8');dec=json.JSONDecoder();pos=s.index('[')+1;changes=[];found=set()
C={
'1.1067':['Gränsen 2 ingår inte eftersom olikheten kräver att x är större än 2.','5,5 är större än den övre gränsen 5.','1,9 är mindre än den undre gränsen 2.',None],
'2.15':[None,'Ett tillåtet x-värde måste ha exakt ett y-värde för att sambandet ska vara en funktion.'],
'2.106':['Variabeln står i exponenten, så detta är en exponentialfunktion.',None,'Uttrycket innehåller x² och är därför en andragradsfunktion.'],
'2.532':[None,'Faktorn 1,3 innebär en ökning med samma procenttal, inte samma antal, varje år.','När x ökar lika mycket förändras x² inte med samma antal varje gång.','Faktorn 0,7 ger en minskning, inte en ökning.'],
'2.533':['Modellen minskar med 8 enheter per år i stället för att öka med en fast procent.','Uttrycket är linjärt och motsvarar inte en positiv startmängd som ökar med en fast faktor.',None,'Modellen ökar med 8 enheter per år, inte med samma procenttal.'],
'3.13':[None,'Täljaren är 2·4^(2x); dividera även med 4^x.','Här saknas divisionen med 4^x, som ger exponenten x.','Vid division subtraheras exponenterna, de adderas inte.']}
while True:
 while s[pos].isspace() or s[pos]==',':pos+=1
 if s[pos]==']':break
 q,end=dec.raw_decode(s,pos);id=q.get('id');chunk=s[pos:end]
 if id in C:
  t=q['t'];assert t.endswith('</p>') and 'alternativ' not in t.lower()
  if id=='2.15':t=r'<p>Vad krävs för att en relation ska beskriva \(y\) som en funktion av \(x\)?</p>'
  if id in {'2.532','2.533'}:t=t.replace('<p>','<p>Här är x antalet år. ',1)
  old='"t": '+json.dumps(q['t'],ensure_ascii=False);new='"t": '+json.dumps(t[:-4]+' Välj ett alternativ.</p>',ensure_ascii=False);assert chunk.count(old)==1;chunk=chunk.replace(old,new,1)
  if id=='2.15':
   old=json.dumps(q['alternativ'][0]['txt'],ensure_ascii=False);new=json.dumps(r'varje tillåtet \(x\)-värde får exakt ett \(y\)-värde',ensure_ascii=False);assert chunk.count(old)==1;chunk=chunk.replace(old,new,1)
  if id=='2.106':
   old=q['s'];new=old.replace(r'\(f(x)=5x-2\)</strong>',r'\(f(x)=5x-2\)');assert old!=new
   needle='"s": '+json.dumps(old,ensure_ascii=False);assert chunk.count(needle)==1;chunk=chunk.replace(needle,'"s": '+json.dumps(new,ensure_ascii=False),1)
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
