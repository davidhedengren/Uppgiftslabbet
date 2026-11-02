"""Synliggör jämförelsealternativ och förklara vanliga missuppfattningar."""
import json,re
from pathlib import Path
p=Path(__file__).resolve().parent.parent/'uppgifterma1.js';s=p.read_text(encoding='utf8');dec=json.JSONDecoder();pos=s.index('[')+1;changes=[];found=set()
C={
'4.550':[None,'Volym mäts i kubikenheter, exempelvis cm³.','Massa kan exempelvis anges i gram eller kilogram, inte cm².','Längd kan exempelvis anges i cm; cm² är en areaenhet.'],
'5.20':[None,'B+C är udda. Om A också är udda blir summan jämn.','Ett jämnt och ett udda tal har udda summa.','B är jämnt och C udda, så deras summa är udda.'],
'5.44':['Med 6 röda och 4 blå är antalet röda inte dubbelt så stort.','15 är delbart med 3. Hindret är att de 10 återstående fälten inte kan delas i hela grupper om tre.','Då är antalet röda lika stort som antalet blå, inte dubbelt så stort.',None],
'5.81':['Samvariation i sig visar inte att glassförsäljningen orsakar olyckorna.',None,'Att båda ökar samtidigt visar inte att olyckor orsakar glassköp.','Samtidig ökning utesluter inte en gemensam faktor som exempelvis varmt väder.'],
'5.106':['Antalet som svarar gör inte svaren slumpmässigt utvalda; alla tillfrågades.',None,'140 personer svarade inte, så de inkomna svaren täcker inte alla medlemmar.','Bortfall kan snedvrida resultatet om de som inte svarar skiljer sig från dem som svarar.'],
'5.108':['Slumpen kan ge olika andelar i ett enskilt urval, även när alla har chans att väljas.',None,'Utvalda elever kan fortfarande välja att inte svara, vilket ger bortfall.','Att välja lättillgängliga elever kan ge ett systematiskt snett urval.'],
'5.187':['Observationen visar samvariation men bevisar inte orsaken.','Observationen visar att de två variablerna samvarierar i studien.','Observationen fastslår inte orsak eller orsakens riktning.',None]}
while True:
 while s[pos].isspace() or s[pos]==',':pos+=1
 if s[pos]==']':break
 q,end=dec.raw_decode(s,pos);id=q.get('id');chunk=s[pos:end]
 if id in C:
  t=q['t'];assert t.endswith('</p>') and 'alternativ' not in t.lower()
  old='"t": '+json.dumps(t,ensure_ascii=False);new='"t": '+json.dumps(t[:-4]+' Välj ett alternativ.</p>',ensure_ascii=False);assert chunk.count(old)==1;chunk=chunk.replace(old,new,1)
  if id=='5.20':
   old=q['s'];new=old.replace('(1-0,40=0,60)',r'\(1-0{,}40=0{,}60\)');assert new!=old
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
