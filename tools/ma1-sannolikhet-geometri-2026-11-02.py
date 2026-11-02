"""Visa sju alternativa jämförelser och förklara deras felval."""
import json,re
from pathlib import Path
p=Path(__file__).resolve().parent.parent/'uppgifterma1.js';s=p.read_text(encoding='utf8');dec=json.JSONDecoder();pos=s.index('[')+1;changes=[];found=set()
C={
'4.47':[None,'cos 25° är lika med sin 65°, inte sin 25°.','Tangens har inte samma komplementvinkelrelation som sinus och cosinus.','sin 65° är lika med cos 25°, inte sin 25°.'],
'4.402':['Olikheten visar bara att sidorna kan bilda en triangel, inte att den är rätvinklig.',None,'Summan 31 visar inte att Pythagoras sats gäller.','Skillnaden 1 mellan två sidor visar inte att Pythagoras sats gäller.'],
'5.192':['Två variabler kan samvariera utan att den ena orsakar den andra.','Korrelation betyder samvariation; orsak betyder att en förändring påverkar en annan.',None],
'5.212':[None,'Statistisk signifikans och hur stor effekten är i praktiken är olika saker.'],
'5.245':[None,'20·0,33=6,6, men antalet röda kulor måste vara ett heltal.','20·0,36=7,2, men antalet röda kulor måste vara ett heltal.','20·0,37=7,4, men antalet röda kulor måste vara ett heltal.'],
'5.416':['1 är en möjlig sannolikhet och innebär att händelsen är säker.','0,99 är mellan 0 och 1 och är därför en möjlig sannolikhet.','0 är en möjlig sannolikhet och innebär att händelsen är omöjlig.',None],
'5.539':[None,'Detta är bortfall i en undersökning, inte felavläsning av en skala.','Ett för litet urval gäller vilka som undersöks, inte avläsningen.','En ledande fråga kan påverka svaren, men är inte ett avläsningsfel.']}
while True:
 while s[pos].isspace() or s[pos]==',':pos+=1
 if s[pos]==']':break
 q,end=dec.raw_decode(s,pos);id=q.get('id');chunk=s[pos:end]
 if id in C:
  t=q['t'];assert t.endswith('</p>') and 'alternativ' not in t.lower()
  if id=='5.192':t=t.replace('Vilket påstående är korrekt?','Vilket påstående om samband och orsak är korrekt?')
  if id=='5.212':t=t.replace('Vilket påstående är bäst?','Vilket påstående om statistisk signifikans och praktisk betydelse är bäst?')
  old='"t": '+json.dumps(q['t'],ensure_ascii=False);new='"t": '+json.dumps(t[:-4]+' Välj ett alternativ.</p>',ensure_ascii=False);assert chunk.count(old)==1;chunk=chunk.replace(old,new,1)
  if id=='5.539':
   old=q['s'];new=old.replace('t.ex. på grund av parallax','t.ex. när man ser skalan snett');assert new!=old
   a='"s": '+json.dumps(old,ensure_ascii=False);assert chunk.count(a)==1;chunk=chunk.replace(a,'"s": '+json.dumps(new,ensure_ascii=False),1)
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
