"""Visa fyra jämförelseuppgifters alternativ och utveckla ett motexempel."""
import json,re
from pathlib import Path
p=Path(__file__).resolve().parent.parent/'uppgifterma1.js';s=p.read_text(encoding='utf8');dec=json.JSONDecoder();pos=s.index('[')+1;changes=[];found=set()
C={
'1.148':['Produkten av två negativa tal är positiv: (−2)(−6)=12.',None,'Faktorn −2 multipliceras med båda termerna i parentesen.','Man behöver multiplicera −2 med båda termerna; att byta plats rättar inte tecknet.'],
'1.933':['Minst 7 betyder 7 eller större, inte mindre.','x är större än eller lika med 7.','Minst 7 inkluderar 7 och alla större tal.','Minst 7 inkluderar även själva talet 7.'],
'1.939':['Även alla tal som är större än 5 ingår.','Likhetstecknet i ≥ betyder att 5 också ingår.',None,'Tecknet ≥ anger 5 och större tal, inte mindre tal.'],
'2.341':['Startvärdet ensamt visar inte hur snabbt modellerna förändras.','Båda modellerna kan beräknas och jämföras vid samma tidpunkt.','En exponentialmodell ligger inte alltid över en linjär modell; vid start är B lägre än A.',None]}
C['1.933'][1]=None
while True:
 while s[pos].isspace() or s[pos]==',':pos+=1
 if s[pos]==']':break
 q,end=dec.raw_decode(s,pos);id=q.get('id');chunk=s[pos:end]
 if id in C:
  t=q['t'];assert t.endswith('</p>') and 'alternativ' not in t.lower()
  old='"t": '+json.dumps(t,ensure_ascii=False);new='"t": '+json.dumps(t[:-4]+' Välj ett alternativ.</p>',ensure_ascii=False);assert chunk.count(old)==1;chunk=chunk.replace(old,new,1)
  if id=='2.341':
   old=q['s'];needle='<li><p>Därför räcker inte startvärdena för att avgöra ordningen för alla framtida tider.</p></li>'
   new=old.replace(needle,r'<li><p>Pröva exempelvis efter 20 timmar:</p>\[A(20)=20\quad\text{och}\quad B(20)=100\cdot0{,}96^{20}\approx44{,}2.\]<p>Då är B större än A, trots att A började högre. Startvärdena räcker alltså inte för att bestämma ordningen senare.</p></li>');assert new!=old
   oldfield='"s": '+json.dumps(old,ensure_ascii=False);assert chunk.count(oldfield)==1;chunk=chunk.replace(oldfield,'"s": '+json.dumps(new,ensure_ascii=False),1)
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
