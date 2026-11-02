"""Ersätt ovidkommande malltext med uträkningar för exakta trigonometriska värden."""
from pathlib import Path
import json
P=Path(__file__).resolve().parent.parent/'uppgiftermato2.js'
# Vinkeluppdelningen och rätt formel anges; därefter sätts standardvärden in.
FORM={
 'sin75':(r'\sin75^\circ=\sin(45^\circ+30^\circ)',r'\sin45^\circ\cos30^\circ+\cos45^\circ\sin30^\circ',r'\frac{\sqrt2}{2}\cdot\frac{\sqrt3}{2}+\frac{\sqrt2}{2}\cdot\frac12',r'\frac{\sqrt6+\sqrt2}{4}'),
 'cos75':(r'\cos75^\circ=\cos(45^\circ+30^\circ)',r'\cos45^\circ\cos30^\circ-\sin45^\circ\sin30^\circ',r'\frac{\sqrt2}{2}\cdot\frac{\sqrt3}{2}-\frac{\sqrt2}{2}\cdot\frac12',r'\frac{\sqrt6-\sqrt2}{4}'),
 'sin15':(r'\sin15^\circ=\sin(45^\circ-30^\circ)',r'\sin45^\circ\cos30^\circ-\cos45^\circ\sin30^\circ',r'\frac{\sqrt2}{2}\cdot\frac{\sqrt3}{2}-\frac{\sqrt2}{2}\cdot\frac12',r'\frac{\sqrt6-\sqrt2}{4}'),
 'cos15':(r'\cos15^\circ=\cos(45^\circ-30^\circ)',r'\cos45^\circ\cos30^\circ+\sin45^\circ\sin30^\circ',r'\frac{\sqrt2}{2}\cdot\frac{\sqrt3}{2}+\frac{\sqrt2}{2}\cdot\frac12',r'\frac{\sqrt6+\sqrt2}{4}'),
 'cos105':(r'\cos105^\circ=\cos(60^\circ+45^\circ)',r'\cos60^\circ\cos45^\circ-\sin60^\circ\sin45^\circ',r'\frac12\cdot\frac{\sqrt2}{2}-\frac{\sqrt3}{2}\cdot\frac{\sqrt2}{2}',r'\frac{\sqrt2-\sqrt6}{4}')}
SYMBOL={
 'sinxplus30':(r'\sin(x+30^\circ)',r'\sin x\cos30^\circ+\cos x\sin30^\circ',r'\frac{\sqrt3}{2}\sin x+\frac12\cos x'),
 'sinxminus45':(r'\sin(x-45^\circ)',r'\sin x\cos45^\circ-\cos x\sin45^\circ',r'\frac{\sqrt2}{2}\sin x-\frac{\sqrt2}{2}\cos x'),
 'cosxplus60':(r'\cos(x+60^\circ)',r'\cos x\cos60^\circ-\sin x\sin60^\circ',r'\frac12\cos x-\frac{\sqrt3}{2}\sin x'),
 'cosxminus30':(r'\cos(x-30^\circ)',r'\cos x\cos30^\circ+\sin x\sin30^\circ',r'\frac{\sqrt3}{2}\cos x+\frac12\sin x')}
IDS={'1.20':['sinxplus30','sinxminus45','cosxplus60','cosxminus30'],'1.38':['sin75','cos75','sin15','cos15'],'1.41':['sin75','cos15','cos105'],'1.145':['sin75','cos15','cos105']}
def terms(expr):
 for i,c in enumerate(expr):
  if c in '+-':return expr[:i],expr[i:]
 raise ValueError(expr)
def content(key):
 if key in SYMBOL:
  start,form,result=SYMBOL[key];f1,f2=terms(form);r1,r2=terms(result)
  return (r'<p class="facit-rubrik"><strong>Använd formeln och sätt in standardvärden</strong></p>'
   +r'<p>Använd additions- eller subtraktionsformeln och sätt sedan in de exakta värdena.</p>'
   +r'\[\begin{aligned}'+start+r'&='+f1+r'\\&\quad '+f2+r'\\&='+r1+r'\\&\quad '+r2+r'\end{aligned}\]'
   +r'<p><strong>Svar:</strong> \('+result+r'\).</p>')
 split,form,sub,result=FORM[key];f1,f2=terms(form);s1,s2=terms(sub)
 return (r'<p class="facit-rubrik"><strong>Välj standardvinklar och använd formeln</strong></p>'
  +r'<p>Skriv vinkeln som en summa eller differens och använd additions- eller subtraktionsformeln.</p>'
  +r'\['+split+r'\]'
  +r'\[\begin{aligned}&='+f1+r'\\&\quad '+f2+r'\\&='+s1+r'\\&\quad '+s2+r'\\&='+result+r'\end{aligned}\]'
  +r'<p><strong>Svar:</strong> \('+result+r'\).</p>')

s=P.read_text(encoding='utf8');dec=json.JSONDecoder();pos=s.index('[')+1;changes=[];found=set()
while True:
 while s[pos].isspace() or s[pos]==',':pos+=1
 if s[pos]==']':break
 q,end=dec.raw_decode(s,pos);id=q.get('id')
 if id in IDS:
  keys=IDS[id];assert len(q['spelDelar'])==len(keys)
  chunk=s[pos:end];old=json.dumps(q['s'],ensure_ascii=False)
  parent='<div class="facit-v2 facit-stegvis">'+''.join('<div class="facit-del"><span class="facit-mark">'+chr(97+i)+')</span><div class="facit-arbete">'+content(k)+'</div></div>' for i,k in enumerate(keys))+'</div>'
  assert chunk.count(old)==1;chunk=chunk.replace(old,json.dumps(parent,ensure_ascii=False),1)
  for d,k in zip(q['spelDelar'],keys):
   old=json.dumps(d['s'],ensure_ascii=False);new=json.dumps('<div class="facit-v2 facit-stegvis">'+content(k)+'</div>',ensure_ascii=False)
   assert chunk.count(old)==1,(id,d.get('etikett'));chunk=chunk.replace(old,new,1)
  parsed=json.loads(chunk);assert len(parsed['spelDelar'])==len(keys);changes.append((pos,end,chunk));found.add(id)
 pos=end
assert found==set(IDS),found
for a,b,c in reversed(changes):s=s[:a]+c+s[b:]
json.loads(s[s.index('['):s.rindex(']')+1]);P.write_text(s,encoding='utf8');print('Ändrade',', '.join(sorted(found)))
