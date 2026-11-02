"""Anpassa ledtrådar till den del som eleven arbetar med."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parent.parent
EDITS={
 'uppgifterma2.js':{
  '1.234':{'a':r'<p>Sätt in fem i uttrycket för kostnaden och beräkna värdet.</p>'},
  '1.76':{'a':r'<p>Vilken mängd finns från början och hur ändras mängden varje minut?</p>',
          'b':r'<p>Utgå från startmängden och minskningen per minut. Sätt den återstående mängden lika med 530 liter.</p>'},
  '1.104':{'a':r'<p>Jämför de tre första tabellvärdena. Hur mycket ändras \(y\) när \(x\) ökar med två?</p>',
           'b':r'<p>Använd de tre första tabellvärdena för att bestämma riktningskoefficienten och avläs sedan värdet när \(x=0\).</p>'}},
 'uppgiftermato1.js':{
  '2.20':{'a':r'<p>När du deriverar \(e^{ax}\) multiplicerar du med konstanten \(a\).</p>'}}
}
for filename,edits in EDITS.items():
 p=ROOT/filename;s=p.read_text(encoding='utf8');dec=json.JSONDecoder();pos=s.index('[')+1;changes=[];found=set()
 while True:
  while s[pos].isspace() or s[pos]==',':pos+=1
  if s[pos]==']':break
  q,end=dec.raw_decode(s,pos);id=q.get('id')
  if id in edits:
   chunk=s[pos:end]
   for d in q['spelDelar']:
    label=d.get('etikett')
    if label not in edits[id]:continue
    assert 'ledtrad' not in d,(id,label)
    marker=r'"etikett"\s*:\s*'+re.escape(json.dumps(label))
    assert len(re.findall(marker,chunk))==1,(id,label)
    chunk=re.sub(marker,lambda m:m.group(0)+',\n        "ledtrad": '+json.dumps(edits[id][label],ensure_ascii=False),chunk,count=1)
   if id=='1.104':
    old=json.dumps(q['spelDelar'][0]['s'],ensure_ascii=False)
    new=json.dumps(r'<div class="facit-v2 facit-stegvis"><p>För varje ökning av \(x\) med 2 minskar \(y\) med 4 i de tre första kolumnerna.</p><p>Nästa värde är därför \(-1-4=-5\).</p><p><strong>Svar:</strong> \(-5\).</p></div>',ensure_ascii=False)
    assert chunk.count(old)==1,id
    chunk=chunk.replace(old,new,1)
   parsed=json.loads(chunk)
   for d in parsed['spelDelar']:
    if d.get('etikett') in edits[id]:assert d['ledtrad']==edits[id][d['etikett']]
   changes.append((pos,end,chunk));found.add(id)
  pos=end
 assert found==set(edits),(filename,found)
 for a,b,t in reversed(changes):s=s[:a]+t+s[b:]
 json.loads(s[s.index('['):s.rindex(']')+1]);p.write_text(s,encoding='utf8');print(filename,sorted(found))
