"""Synliga påståenden om samband, urval och mätningar."""
import json,re
from pathlib import Path
p=Path(__file__).resolve().parent.parent/'uppgifterma1.js';s=p.read_text(encoding='utf8');dec=json.JSONDecoder();pos=s.index('[')+1;changes=[];found=set()
C={
'5.201':['Punkterna följer exakt en stigande linje, vilket är ett tydligt linjärt samband.','Punkterna ligger exakt på linjen, så det linjära sambandet är perfekt.','En stigande linje ger positiv, inte negativ, korrelation.',None],
'5.202':['En fallande linje ger negativ, inte positiv, korrelation.','Punkterna ligger exakt på en fallande linje och har ett tydligt linjärt samband.','Punkterna ligger exakt på linjen, så det linjära sambandet är perfekt.',None],
'5.205':[None,'En negativ linjär korrelation skulle visa en tydlig fallande trend.','En positiv linjär korrelation skulle visa en tydlig stigande trend.','Perfekt positiv korrelation kräver att punkterna ligger exakt på en stigande rät linje.'],
'5.500':['Minustecknet visar att det linjära sambandet är negativt, inte positivt.','Beloppet 0,85 är relativt nära 1 och tyder på ett starkt linjärt samband.',None,'Ett värde nära −1 tyder på ett starkt negativt linjärt samband.'],
'5.567':['Ett större urval blir inte automatiskt representativt om urvalssättet är snett.','Systematiska fel kan kvarstå även när fler personer tillfrågas på samma sätt.',None,'Fler svar kan minska den slumpmässiga osäkerheten, även om snedvridningen kan finnas kvar.'],
'7.05':['Det första intervallet slutar vid 10,1 cm och det andra börjar där; inget mellanrum finns.',None,'Första intervallet slutar vid 10,1 cm och det andra börjar där; de möts bara i den punkten.','Det första intervallet börjar vid 9,9 cm, utanför det andra intervallet.'],
'7.88':[None,'Skillnaden i flöde är 6 liter per minut; tidsskillnaden beror på tankarnas volym.','För samma volym tar det kortare tid med det större flödet 18 liter per minut.','Det är B som tar 1,5 gånger tiden för A, eftersom 18/12=1,5.']}
while True:
 while s[pos].isspace() or s[pos]==',':pos+=1
 if s[pos]==']':break
 q,end=dec.raw_decode(s,pos);id=q.get('id');chunk=s[pos:end]
 if id in C:
  t=q['t'];assert t.endswith('</p>') and 'alternativ' not in t.lower()
  old='"t": '+json.dumps(t,ensure_ascii=False);new='"t": '+json.dumps(t[:-4]+' Välj ett alternativ.</p>',ensure_ascii=False);assert chunk.count(old)==1;chunk=chunk.replace(old,new,1)
  if id=='5.567':
   old=q['alternativ'][2]['txt'];new='Den slumpmässiga osäkerheten kan minska, men det systematiska felet kan finnas kvar.'
   a='"txt": '+json.dumps(old,ensure_ascii=False);assert chunk.count(a)==1;chunk=chunk.replace(a,'"txt": '+json.dumps(new,ensure_ascii=False),1)
   old=q['s'];new=old.replace('Ett större urval minskar den slumpmässiga osäkerheten, men ett systematiskt fel blir inte mindre av att fler tillfrågas på samma sätt.','Ett större urval kan minska den slumpmässiga osäkerheten, men om fler tillfrågas på samma sneda sätt kan ett systematiskt fel kvarstå.').replace('Den slumpmässiga osäkerheten minskar, men det systematiska felet finns kvar.','Den slumpmässiga osäkerheten kan minska, men det systematiska felet kan finnas kvar.');assert new!=old
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
