"""Installerar manuellt författade rubriker och flervalskommentarer.
Ingen rubrik härleds automatiskt ur text, nivå eller ID.
"""
import json,re
from html import escape
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
HEADINGS=json.loads(Path(__file__).with_name('ma3-facitstruktur-2026-10-25.rubriker.json').read_text())
COMMENTS=json.loads(Path(__file__).with_name('ma3-facitstruktur-2026-10-25.kommentarer.json').read_text())
EXTRAS=json.loads(Path(__file__).with_name('ma3-facitstruktur-2026-10-25.mellanled.json').read_text())
REWRITES=json.loads(Path(__file__).with_name('ma3-facitstruktur-2026-10-25.omarbetning.json').read_text())
def replace_fields(source,updated):
 """Bevara all orörd formatering och ersätt bara ändrade toppnivåfält."""
 decoder=json.JSONDecoder();i=1;edits=[]
 while True:
  while source[i].isspace() or source[i]==',':i+=1
  if source[i]=='}':break
  key,n=decoder.raw_decode(source[i:]);i+=n
  while source[i].isspace() or source[i]==':':i+=1
  value,n=decoder.raw_decode(source[i:])
  if value!=updated[key]:edits.append((i,i+n,json.dumps(updated[key],ensure_ascii=False)))
  i+=n
 for begin,end,value in reversed(edits):source=source[:begin]+value+source[end:]
 return source
def install():
 path=ROOT/'uppgiftermato1.js';raw=path.read_text();changes=[]
 for id,headings in HEADINGS.items():
  pos=raw.index('"id": "'+id+'"');start=raw.rfind('{',0,pos);q,length=json.JSONDecoder().raw_decode(raw[start:]);before=json.dumps(q,ensure_ascii=False)
  q.update(REWRITES.get(id,{}))
  steps=re.findall(r'<li>([\s\S]*?)</li>',q['s']);assert len(steps)==len(headings),(id,len(steps),len(headings))
  i=iter(enumerate(headings,1))
  def step(m):
   number,heading=next(i)
   body=re.sub(r'^\s*<p class="facit-rubrik">[\s\S]*?</p>','',m.group(1))
   body=re.sub(r'<div data-facit-revision="2026-10-25">[\s\S]*?</div>','',body)
   extra=EXTRAS.get(id,{}).get(str(number))
   if extra:body+='<div data-facit-revision="2026-10-25">'+extra+'</div>'
   return '<li><p class="facit-rubrik">'+escape(heading)+'</p>'+body+'</li>'
  previous=q['s']
  q['s']=re.sub(r'<li>([\s\S]*?)</li>',step,previous)
  if q.get('spelDelar'):
   # Varje del får exakt samma manuella rubriker som motsvarande del i lärarfacitet.
   before_steps=re.findall(r'<li>[\s\S]*?</li>',previous)
   after_steps=re.findall(r'<li>[\s\S]*?</li>',q['s'])
   for part in q['spelDelar']:
    for old,new in zip(before_steps,after_steps):part['s']=part['s'].replace(old,new)
  if id in COMMENTS:
   assert len(q['alternativ'])==len(COMMENTS[id]),id
   for option,comment in zip(q['alternativ'],COMMENTS[id]):option['kommentar']=comment
  if json.dumps(q,ensure_ascii=False)!=before:changes.append(id)
  raw=raw[:start]+replace_fields(raw[start:start+length],q)+raw[start+length:]
 path.write_text(raw);print('Ändrade:',len(changes),changes)
if __name__=='__main__':install()
