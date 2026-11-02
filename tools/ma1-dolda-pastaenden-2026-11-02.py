"""Visa avsedda påståenden och förklara felaktiga alternativ."""
import json,re
from pathlib import Path
p=Path(__file__).resolve().parent.parent/'uppgifterma1.js';s=p.read_text(encoding='utf8');dec=json.JSONDecoder();pos=s.index('[')+1;changes=[];found=set()
C={
'0.55':['Tiondelssiffran i 0,073 är 0. Siffran 7 bidrar med 0,07.','Entalssiffran är 0. Siffran 7 står två platser efter kommatecknet.','Tusendelssiffran är 3. Siffran 7 står på hundradelsplatsen.',None],
'0.87':[None,'Multiplikation med ett positivt tal mindre än 1 gör ett positivt tal mindre.','Produkten är mindre än båda talen och ligger därför inte mellan dem.','Båda faktorerna är mindre än 1, så produkten är mindre än även det mindre talet.'],
'0.256':['Parentesen ska räknas först. Felet kommer när 3 och 2 adderas före multiplikationen.','Parentesen räknas först. Efter den ska 8 multipliceras med 3 före additionen.',None,'Uttrycket i parentesen ska beräknas först; det första felet kommer därefter.'],
'0.540':[None,'Varje meter motsvarar 100 cm, så areans talvärde multipliceras med 100·100.','Kvadraten ändras inte när enheten byts. Talvärdet för arean ökar 100·100 gånger.','Själva arean är oförändrad; bara enheten och talvärdet ändras.'],
'0.740':[None,'Faktorn 4,1 är större än 1, så produkten är större än 38,5.','Antalet decimaler visar inte att storleken är rimlig. Ett överslag ger cirka 160.','38·41 motsvarar inte 38,5·4,1; den andra faktorn är ungefär 4, inte 40.'],
'0.744':['Eftersom 0,52 är mindre än 1 är produkten mindre än 810, men ungefär hälften av 810.',None,'Produkten ska visserligen vara mindre än 810, men den bör vara ungefär hälften av 810.','52·81 ≈ 4 200 bortser från decimalfaktorn; 0,52 är ungefär en halv.']}
while True:
 while s[pos].isspace() or s[pos]==',':pos+=1
 if s[pos]==']':break
 q,end=dec.raw_decode(s,pos);id=q.get('id');chunk=s[pos:end]
 if id in C:
  t=q['t'];assert t.endswith('</p>') and 'alternativ' not in t.lower()
  if id=='0.540':t=t.replace('Vilket påstående beskriver arean rätt?','Arean anges därefter i kvadratcentimeter i stället för kvadratmeter. Vilket påstående beskriver arean rätt?')
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
