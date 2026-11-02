"""Återställ underlag och förtydliga figurtillhörighet i två deluppgifter."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent

def rewrite(filename,id,changes):
 p=ROOT/filename;raw=p.read_text(encoding='utf8');decoder=json.JSONDecoder();pos=raw.index('[')+1
 while True:
  while raw[pos].isspace() or raw[pos]==',':pos+=1
  if raw[pos]==']':raise ValueError(id)
  q,end=decoder.raw_decode(raw,pos)
  if q.get('id')==id:break
  pos=end
 segment=raw[pos:end];m=re.search(r'"spelDelar"\s*:\s*\[',segment);assert m
 n=m.end();parts=[]
 while True:
  while segment[n].isspace() or segment[n]==',':n+=1
  if segment[n]==']':break
  part,stop=decoder.raw_decode(segment,n);parts.append((part,n,stop));n=stop
 for i,key,new in sorted(changes(q),reverse=True):
  part,start,stop=parts[i];d=segment[start:stop];field=re.search(r'"'+re.escape(key)+r'"\s*:\s*',d);assert field
  _,v_end=decoder.raw_decode(d,field.end());d=d[:field.end()]+json.dumps(new,ensure_ascii=False)+d[v_end:]
  segment=segment[:start]+d+segment[stop:]
 raw=raw[:pos]+segment+raw[end:];json.loads(raw[raw.index('['):raw.rindex(']')+1]);p.write_text(raw,encoding='utf8')

def table(q):
 m=re.search(r'<table\b.*?</table>',q['t'],re.S);assert m
 intro='<p>Tabellen visar några värden för funktionen \\(f\\).</p>'+m.group()
 return [(0,'t',intro+'<p>Bestäm \\(f(2)\\).</p>'),
         (1,'t',intro+'<p>Vilket \\(x\\)-värde ger \\(f(x)=1\\)?</p>'),
         (2,'t',intro+'<p>Vilken punkt på grafen motsvarar \\(f(-3)=6\\)? Ange x- och y-koordinat.</p>')]

def caption(q):
 old=q['spelDelar'][0]['fraga'];assert '<span class="fig">' in old
 return [(0,'fraga',old.replace('<span class="fig">','<p>Figuren hör till del a.</p><span class="fig">',1))]

rewrite('uppgifterma2.js','2.436',table)
rewrite('uppgiftermato2.js','3.116',caption)
