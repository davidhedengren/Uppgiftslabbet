"""Avgränsad manuell granskning av sju alternativberoende Ma1-uppgifter."""
import json,re
from pathlib import Path
p=Path(__file__).resolve().parent.parent/'uppgifterma1.js';s=p.read_text(encoding='utf8');dec=json.JSONDecoder();pos=s.index('[')+1;changes=[];found=set()
comments={
'0.51':['Noll dividerat med ett tal skilt från noll är 0.','Produkten av ett tal och 0 är 0.',None,'Att addera 0 ändrar inte talet; värdet är 3/5.'],
'0.264':['Parentesen blir 19 och hela uttrycket 19·4 = 76.','Multiplikationen görs först: 20−3+8 = 25.',None,'Räkna från vänster: 20−3+2−4 = 15.'],
'0.267':['Multiplicera först: 6+2·5 = 16. Jämför med det andra uttryckets värde 40.',None],
'0.280':[None,'Räkna parentesen först: 24÷(6·2) = 2. Det andra uttrycket är 8.'],
'0.301':[None,'Bråket har rätt värde, men täljare och nämnare kan båda delas med 7.','Bråket har rätt värde, men täljare och nämnare kan båda delas med 2.'],
'0.309':[None,'Gemensam nämnare ger 4/9 = 44/99 och 5/11 = 45/99, så det första är mindre.','Gemensam nämnare ger 44/99 och 45/99. De är inte lika stora.'],
'0.404':['Skriv 0,7 som 0,70: det är större än 0,65.','Skriv 0,35 som 0,350: 0,305 är mindre.','Skriv 1,10 som 1,100: 1,099 är mindre.', 'Skriv 2,8 som 2,80: 2,08 är mindre.']}
# Rätt alternativ har ingen felkommentar.
comments['0.404'][2]=None
while True:
 while s[pos].isspace() or s[pos]==',':pos+=1
 if s[pos]==']':break
 q,end=dec.raw_decode(s,pos);id=q.get('id');chunk=s[pos:end]
 if id in comments:
  assert q['t'].endswith('</p>') and 'alternativ' not in q['t'].lower()
  old='"t": '+json.dumps(q['t'],ensure_ascii=False);new='"t": '+json.dumps(q['t'][:-4]+' Välj ett alternativ.</p>',ensure_ascii=False);assert chunk.count(old)==1;chunk=chunk.replace(old,new,1)
  assert len(q['alternativ'])==len(comments[id]);assert sum(a['ratt'] for a in q['alternativ'])==1
  for alt,text in zip(q['alternativ'],comments[id]):
   if alt['ratt']:assert text is None;continue
   assert text and 'kommentar' not in alt
   pattern=r'"txt"\s*:\s*'+re.escape(json.dumps(alt['txt'],ensure_ascii=False))+r'\s*,\s*"ratt"\s*:\s*false'
   chunk,n=re.subn(pattern,lambda m:m.group(0)+', "kommentar": '+json.dumps(text,ensure_ascii=False),chunk,count=1);assert n==1,(id,alt['txt'])
  assert json.loads(chunk)['id']==id;changes.append((pos,end,chunk));found.add(id)
 pos=end
assert found==set(comments)
for a,b,c in reversed(changes):s=s[:a]+c+s[b:]
json.loads(s[s.index('['):s.rindex(']')+1]);p.write_text(s,encoding='utf8');print('Ändrade:',', '.join(sorted(found)))
