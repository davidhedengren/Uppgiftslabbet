"""Förtydliga fem begreppsfrågor och visa deras alternativ."""
import json,re
from pathlib import Path
p=Path(__file__).resolve().parent.parent/'uppgifterma1.js';s=p.read_text(encoding='utf8');dec=json.JSONDecoder();pos=s.index('[')+1;changes=[];found=set()
C={
'1.121':['Tecknet ≤ betyder att 50 ingår i intervallet.','−20 ingår inte eftersom tecknet där är strikt mindre än.','−20 ingår inte, men 50 ingår eftersom tecknet där är ≤.',None],
'1.907':['3² betyder 3·3=9, medan 2·3=6.','2·3=6, men 3² betyder 3·3=9.','3² är 9, men 2·3 är 6 och inte 9.',None],
'2.236':['När x ökar med 3 ändras y med −3·3=−9.','En negativ riktningskoefficient betyder att y minskar när x ökar.','När x ökar med 3 minskar y med 9, inte med 1.',None],
'2.287':[None,'Punktens x-koordinat är −1 och y-koordinaten är 3; de har bytt plats.','När x är −1 är funktionsvärdet 3, inte −3.','Punkten ger information om x=−1, inte om x=1.'],
'2.319':['Tidpunkten när volymen når 0 ingår: modellen gäller tills behållaren är tom.','Efter 16 minuter skulle modellen ge negativ volym och gäller därför inte längre.',None,'96 är startvolymen i liter. Behållaren töms på 96/6=16 minuter.']}
while True:
 while s[pos].isspace() or s[pos]==',':pos+=1
 if s[pos]==']':break
 q,end=dec.raw_decode(s,pos);id=q.get('id');chunk=s[pos:end]
 if id in C:
  t=q['t'];assert t.endswith('</p>') and 'alternativ' not in t.lower()
  if id=='1.121':t=t.replace('Vilken beskrivning stämmer?','Temperaturen T mäts i °C. Vilken beskrivning stämmer?')
  if id=='2.319':t=t.replace('och gäller tills behållaren är tom.','och gäller tills behållaren är tom. Här är t tiden i minuter efter att tömningen börjar.')
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
