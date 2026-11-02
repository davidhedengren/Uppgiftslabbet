"""Förklara grundvinklar, tecken och period i trigonometriska ekvationer."""
from pathlib import Path
import json
P=Path(__file__).resolve().parent.parent/'uppgiftermato2.js'
D={
'1.16':[
r'<p>Sinus är noll vid \(0^\circ\) och \(180^\circ\). Därefter upprepas nollställena med \(180^\circ\) mellanrum.</p><p><strong>Svar:</strong> \(x=180^\circ n\), där \(n\in\mathbb Z\).</p>',
r'<p>Cosinus är \(-1\) vid \(180^\circ\). Cosinus har perioden \(360^\circ\).</p><p><strong>Svar:</strong> \(x=180^\circ+360^\circ n\), där \(n\in\mathbb Z\).</p>',
r'<p>Vi har \(\tan60^\circ=\sqrt3\). Tangens har perioden \(180^\circ\).</p><p><strong>Svar:</strong> \(x=60^\circ+180^\circ n\), där \(n\in\mathbb Z\).</p>',
r'<p>Sinus är \(1/2\) vid \(30^\circ\) och \(150^\circ\) under ett varv. Sinus har perioden \(360^\circ\).</p><p><strong>Svar:</strong> \(x=30^\circ+360^\circ n\) eller \(x=150^\circ+360^\circ n\), där \(n\in\mathbb Z\).</p>'],
'1.132':[
r'<p>Referensvinkeln är \(30^\circ\) eftersom \(\sin30^\circ=1/2\). Sinus är positiv i första och andra kvadranten.</p><p><strong>Svar:</strong> \(x=30^\circ\) eller \(150^\circ\).</p>',
r'<p>Referensvinkeln är \(45^\circ\) eftersom \(\cos45^\circ=\sqrt2/2\). Cosinus är negativ i andra och tredje kvadranten.</p><p><strong>Svar:</strong> \(x=135^\circ\) eller \(225^\circ\).</p>',
r'<p>Referensvinkeln är \(45^\circ\) eftersom \(\tan45^\circ=1\). Tangens är negativ i andra och fjärde kvadranten.</p><p><strong>Svar:</strong> \(x=135^\circ\) eller \(315^\circ\).</p>'],
'1.299':[
r'<p>Dividera med 3: \(\sin x=1/2\). Referensvinkeln är \(30^\circ\), och sinus är positiv i första och andra kvadranten.</p><p><strong>Svar:</strong> \(x=30^\circ\) eller \(150^\circ\).</p>',
r'<p>Flytta över \(\sqrt3\) och dividera med 2: \(\cos x=-\sqrt3/2\). Referensvinkeln är \(30^\circ\), och cosinus är negativ i andra och tredje kvadranten.</p><p><strong>Svar:</strong> \(x=150^\circ\) eller \(210^\circ\).</p>',
r'<p>Referensvinkeln är \(45^\circ\) eftersom \(\tan45^\circ=1\). Tangens är negativ i andra och fjärde kvadranten.</p><p><strong>Svar:</strong> \(x=135^\circ\) eller \(315^\circ\).</p>',
r'<p>Dividera med 4 och ta hänsyn till båda tecknen: \(\cos^2x=1/4\), alltså \(\cos x=\pm1/2\). Referensvinkeln är \(60^\circ\), och båda tecknen ger en lösning i varje kvadrant.</p><p><strong>Svar:</strong> \(x=60^\circ,\ 120^\circ,\ 240^\circ\) eller \(300^\circ\).</p>']}
D['1.68']=[
 r'<p>En produkt är noll när minst en faktor är noll. Alltså \(\sin x=0\) eller \(\cos x=0\). Tillsammans ger nollställena en vinkel var \(90^\circ\).</p><p><strong>Svar:</strong> \(x=90^\circ n\), där \(n\in\mathbb Z\).</p>',
 r'<p>Ta hänsyn till båda tecknen: \(\sin x=\pm\sqrt3/2\). Referensvinkeln är \(60^\circ\); båda tecknen ger vinklar i alla fyra kvadranter.</p><p><strong>Svar:</strong> \(x=60^\circ+180^\circ n\) eller \(x=120^\circ+180^\circ n\), där \(n\in\mathbb Z\).</p>',
 r'<p>Flytta över 1 och dividera med 2: \(\cos^2x=1/2\), så \(\cos x=\pm\sqrt2/2\). Referensvinkeln är \(45^\circ\).</p><p><strong>Svar:</strong> \(x=45^\circ+90^\circ n\), där \(n\in\mathbb Z\).</p>',
 r'<p>En produkt är noll när minst en faktor är noll: \(\sin x=0\) eller \(\cos x=1/2\). Det ger \(180^\circ n\) respektive vinklarna \(60^\circ\) och \(300^\circ\) med perioden \(360^\circ\).</p><p><strong>Svar:</strong> \(x=180^\circ n\), \(x=60^\circ+360^\circ n\) eller \(x=300^\circ+360^\circ n\), där \(n\in\mathbb Z\).</p>']
D['1.69']=[
 D['1.16'][0],
 r'<p>Cosinus är noll vid \(90^\circ\) och \(270^\circ\). Nollställena upprepas med \(180^\circ\) mellanrum.</p><p><strong>Svar:</strong> \(x=90^\circ+180^\circ n\), där \(n\in\mathbb Z\).</p>',
 D['1.16'][2],
 r'<p>Cosinus är \(1\) vid \(0^\circ\) och upprepas efter varje helt varv.</p><p><strong>Svar:</strong> \(x=360^\circ n\), där \(n\in\mathbb Z\).</p>']
def content(s):return '<div class="facit-v2 facit-stegvis"><p class="facit-rubrik"><strong>Bestäm vinklarna</strong></p>'+s+'</div>'
s=P.read_text(encoding='utf8');dec=json.JSONDecoder();pos=s.index('[')+1;changes=[];found=set()
while True:
 while s[pos].isspace() or s[pos]==',':pos+=1
 if s[pos]==']':break
 q,end=dec.raw_decode(s,pos);id=q.get('id')
 if id in D:
  ds=q['spelDelar'];vals=D[id];assert len(ds)==len(vals)
  chunk=s[pos:end];old=json.dumps(q['s'],ensure_ascii=False)
  parent='<div class="facit-v2 facit-stegvis">'+''.join('<div class="facit-del"><span class="facit-mark">'+chr(97+i)+')</span><div class="facit-arbete">'+content(v)+'</div></div>' for i,v in enumerate(vals))+'</div>'
  assert chunk.count(old)==1;chunk=chunk.replace(old,json.dumps(parent,ensure_ascii=False),1)
  for d,v in zip(ds,vals):
   old=json.dumps(d['s'],ensure_ascii=False);assert chunk.count(old)==1,(id,d.get('etikett'));chunk=chunk.replace(old,json.dumps(content(v),ensure_ascii=False),1)
  json.loads(chunk);changes.append((pos,end,chunk));found.add(id)
 pos=end
assert found==set(D)
for a,b,c in reversed(changes):s=s[:a]+c+s[b:]
json.loads(s[s.index('['):s.rindex(']')+1]);P.write_text(s,encoding='utf8');print('Ändrade',', '.join(sorted(found)))
