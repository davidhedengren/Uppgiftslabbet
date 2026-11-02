"""Rätta koordinataxlar och granskningsfynd i Ma3."""
from pathlib import Path
import json,re,math
P=Path(__file__).resolve().parent.parent/'uppgiftermato1.js'
s=P.read_text(encoding='utf8');dec=json.JSONDecoder();pos=s.index('[')+1;edits=[];found=set()
axes={'3.1201':'200.667','3.1202':'76.0','3.1203':'89.6','3.1204':'161.0','3.1205':'200.667'}
trig={'4.104':6*math.sin(math.radians(68)),'4.102':30*math.tan(math.radians(38)),'4.114':120*math.sin(math.radians(35)),'4.118':18*math.sin(math.radians(52))+1.5}
decimaler={'4.485':34.0,'4.486':16.3}
targets=set(axes)|set(trig)|set(decimaler)|{'3.1233','3.1206'}
while True:
 while s[pos].isspace() or s[pos]==',':pos+=1
 if s[pos]==']':break
 q,end=dec.raw_decode(s,pos);id=q.get('id')
 if id in targets:
  chunk=s[pos:end]
  if id in axes:
   old=q['t'];new=old; y=axes[id];yn=float(y)
   bottom='<path d="M60 280L443 280" fill="none" stroke="#243447" stroke-width="2"/>'
   assert new.count(bottom)==1;new=new.replace(bottom,'',1)
   axis=f'<path d="M60 {y}L430 {y}" fill="none" stroke="#243447" stroke-width="2"/>'
   replacement=f'<path d="M60 {y}L443 {y} M435 {yn-4:g}L443 {y}L435 {yn+4:g}" fill="none" stroke="#243447" stroke-width="2"/>'
   assert new.count(axis)==1,(id,axis);new=new.replace(axis,replacement,1)
   # Delstreck och siffror hör till nollaxeln, inte till diagrammets underkant.
   pat=r'<text x="([\d.]+)" y="302" font-family="Arial,sans-serif" font-size="16" text-anchor="middle" fill="#243447">([^<]+)</text>'
   labels=list(re.finditer(pat,new));assert len(labels)==5,id
   def tick(m):
    x=float(m.group(1));return f'<path d="M{x:g} {yn-4:g}V{yn+4:g}" stroke="#243447" stroke-width="1.2"/><text x="{m.group(1)}" y="{yn+21:g}" font-family="Arial,sans-serif" font-size="16" text-anchor="middle" fill="#243447">{m.group(2)}</text>'
   new=re.sub(pat,tick,new)
   xtext='<text x="430" y="329" font-family="Arial,sans-serif" font-size="17" text-anchor="end" fill="#243447">x</text>'
   assert xtext in new;new=new.replace(xtext,f'<text x="449" y="{yn+5:g}" font-family="Arial,sans-serif" font-size="17" text-anchor="start" fill="#243447">x</text>',1)
   if id=='3.1204':
    left='<path d="M60 280L60 32" fill="none" stroke="#243447" stroke-width="2"/>'
    assert left in new;new=new.replace(left,'',1)
    new,n=re.subn(r'(<text x=")49(" y="[0-9.]+" font-family="Arial,sans-serif" font-size="16" text-anchor="end")',r'\g<1>234\g<2>',new);assert n==7,(id,n)
    new,n=re.subn(r'<text x="234" y="166(?:\.0)?"[^>]*>0</text>','',new);assert n==1,(id,n)
    new=new.replace('<text x="60" y="23" font-family="Arial,sans-serif" font-size="17" text-anchor="start" fill="#243447">f(x)</text>','<text x="245" y="23" font-family="Arial,sans-serif" font-size="17" text-anchor="start" fill="#243447">f(x)</text>',1)
   oldenc=json.dumps(old,ensure_ascii=False);assert chunk.count(oldenc)==1;chunk=chunk.replace(oldenc,json.dumps(new,ensure_ascii=False),1)
  if id in trig:
   exact=trig[id]
   def repl(key,value):
    nonlocal_dummy=None
    global chunk
    pat=r'("'+re.escape(key)+r'"\s*:\s*)'+re.escape(json.dumps(q[key],ensure_ascii=False))
    chunk,n=re.subn(pat,lambda m:m.group(1)+json.dumps(value,ensure_ascii=False),chunk,count=1);assert n==1,(id,key)
   repl('rättSvar',exact);repl('tolerans',1e-9)
   assert 'svarFormat' not in q and 'svarEnhet' not in q
   idx=chunk.rfind('}');chunk=chunk[:idx].rstrip()+',\n    "svarFormat": "numeriskt",\n    "svarEnhet": "m"\n  '+chunk[idx:]
  if id in decimaler:
   for key,value in [('rättSvar',decimaler[id]),('tolerans',0)]:
    pat=r'("'+re.escape(key)+r'"\s*:\s*)'+re.escape(json.dumps(q[key],ensure_ascii=False))
    chunk,n=re.subn(pat,lambda m:m.group(1)+json.dumps(value,ensure_ascii=False),chunk,count=1);assert n==1,(id,key)
   assert 'svarFormat' not in q
   idx=chunk.rfind('}');chunk=chunk[:idx].rstrip()+',\n    "svarFormat": "numeriskt"\n  '+chunk[idx:]
  if id=='3.1206':
   old=json.dumps(q['s'],ensure_ascii=False)
   new=(r'<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list"><li>'
    r'<p class="facit-rubrik">En positiv andraderivata betyder att lutningen ökar</p>'
    r'<p>Den säger inte att lutningen redan är positiv. Välj till exempel \(f(x)=x^2-6x\).</p>'
    r'\[f^{\prime\prime}(x)=2\]'
    r'<p>Förstaderivatan är ändå negativ på hela intervallet \(0&lt;x&lt;2\):</p>'
    r'\[f^{\prime}(x)=2x-6&lt;0\]'
    r'</li></ol><p class="facit-svar"><strong>Svar:</strong> Nej. Funktionen kan vara avtagande även när dess lutning ökar.</p></div>')
   assert chunk.count(old)==1;chunk=chunk.replace(old,json.dumps(new,ensure_ascii=False),1)
  if id=='3.1233':
   pat=r'("traningsniva"\s*:\s*)3\b';chunk,n=re.subn(pat,r'\g<1>4',chunk,count=1);assert n==1
  parsed=json.loads(chunk);assert parsed['id']==id;edits.append((pos,end,chunk));found.add(id)
 pos=end
assert found==targets,(found,targets)
for a,b,c in reversed(edits):s=s[:a]+c+s[b:]
json.loads(s[s.index('['):s.rindex(']')+1]);P.write_text(s,encoding='utf8');print('Ändrade',', '.join(sorted(found)))
