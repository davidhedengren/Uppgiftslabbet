"""Matematik, tecken, riktningsfält och metadata för de 28 grunduppgifterna."""
import json,subprocess,re,math,xml.etree.ElementTree as E
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
raw=subprocess.check_output(['node','-e',"const fs=require('fs'),vm=require('vm'),c={window:{}};vm.runInNewContext(fs.readFileSync('uppgiftermatf1.js','utf8'),c);console.log(JSON.stringify(Object.values(c.window).find(Array.isArray)));"],cwd=ROOT,text=True)
q={v['id']:v for v in json.loads(raw) if v['omr']=='vad_ar_diffekv'};seen=set();x,y=s.symbols('x y',real=True)
def val(id,v):assert q[id]['rättSvar']==v,(id,v);seen.add(id)
val('4.326',s.solve(2*y-6,y)[0]);val('4.328',3*4**2-4);val('4.329',s.solve(y*(1-y/160),y))
val('4.346',float(s.solve(5-2*y,y)[0]));val('4.158',s.solve(y*(4-y),y));val('4.351',4**2-3)
val('4.319',max(s.solve(x*x-4,x)));val('4.518',[0,4,s.solve(s.diff(y*(4-y),y),y)[0]])
val('4.577',2);val('4.579',s.solve(s.Rational(1,2)*(4-y),y)[0]);val('4.580',1+2);val('4.583',2)
val('4.88','T');assert q['4.88']['svarFormat']=='kort_text'
val('4.46',['ja','nej','ja','nej']);assert len(q['4.46']['spelDelar'])==4
for p in q['4.46']['spelDelar']:assert p['ledtrad'] and 'facit-rubrik' in p['s']
for id,L,k in [('4.330',5,-3),('4.582',3,-2)]:
 assert k*((L+1)-L)<0 and k*((L-1)-L)>0;seen.add(id)
assert (-160)*(-1)>0;seen.add('4.16')
assert 4*(10-4)>0 and 12*(10-12)<0;seen.add('4.90')
assert -s.Rational(1,5)*(25-15)<0 and -s.Rational(1,5)*(10-15)>0;seen.add('4.159')
for id,L in [('4.66',500),('4.91',200),('4.123',400),('4.344',180),('4.581',4)]:
 f=y*(L-y)
 assert s.solve(f,y)==[0,L]
 assert f.subs(y,-1)<0 and f.subs(y,L/2)>0 and f.subs(y,L+1)<0;seen.add(id)
seen.add('4.15');assert 'inhomogen' in q['4.15']['s']
f=s.Rational(8,3)*s.cos(x);assert s.simplify(s.diff(f,x,2)+4*f-8*s.cos(x))==0;seen.add('4.44')
assert [a['ratt'] for a in q['4.578']['alternativ']]==[True,False,False,False];seen.add('4.578')
assert [a['ratt'] for a in q['4.581']['alternativ']]==[True,False,False,False]
assert [a['ratt'] for a in q['4.582']['alternativ']]==[True,False,False]
assert [a['ratt'] for a in q['4.584']['alternativ']]==[True,False,False,False]
assert -s.Rational(1,10)*(80-20)<0 and -s.Rational(1,10)*(20-20)==0;seen.add('4.584')
assert seen==set(q) and len(q)==28
assert '<svg' not in q['4.123']['t'] and '<svg' in q['4.123']['s']
assert 'P = 400' in q['4.123']['s'] and 'y = 400' not in q['4.123']['s']
# Kontrollera de faktiska streckens lutningar mot rätt axelskalor, inte bara deras tecken.
ns='{http://www.w3.org/2000/svg}'
for id,lims,fun in [('4.578',(-3,3,-3,3),lambda x,y:x),('4.579',(0,6,0,7),lambda x,y:.5*(4-y)),('4.581',(0,10,0,6),lambda x,y:.25*y*(4-y)),('4.582',(0,5,0,6),lambda x,y:-2*(y-3))]:
 svg=E.fromstring(re.search(r'<svg[\s\S]*?</svg>',q[id]['t'])[0]);xmin,xmax,ymin,ymax=lims;sx=344/(xmax-xmin);sy=270/(ymax-ymin)
 strokes=[e for e in svg.iter(ns+'line') if e.get('stroke')=='#5b7fa8'];assert len(strokes)>100
 for e in strokes:
  x1,y1,x2,y2=[float(e.get(k)) for k in ['x1','y1','x2','y2']]
  cx=((x1+x2)/2-40)/sx+xmin;cy=(286-(y1+y2)/2)/sy+ymin;rate=fun(cx,cy)
  assert abs((y2-y1)+rate*(x2-x1)*sy/sx)<.5,(id,rate,e.attrib)
 if id=='4.581':
  curve=svg.find(ns+'polyline');assert curve is not None
  for xy in curve.get('points').split():
   px,py=map(float,xy.split(','));vx=(px-40)/sx;vy=(286-py)/sy
   assert abs(vy-4/(1+3*math.exp(-vx)))<.5/sy # Mindre än en halv bildpunkt.
for id,v in q.items():
 assert v['miniräknare'] and not v['geogebra'] and 'facit-rubrik' in v['s'] and 'facit-svar' in v['s'],id
 for k in ['t','s','ledtrad']:
  for mathblock in re.findall(r'\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\]',v[k]):assert '<' not in mathblock and '>' not in mathblock,(id,k)
for id in ['4.329','4.158']:assert q[id]['svarsstruktur']=='mängd' and q[id]['spel']
for id in ['4.330','4.15','4.16','4.44','4.66','4.90','4.91','4.123','4.344','4.159']:assert q[id]['spel'] is False
print('28 grunduppgifter: algebra, tecken, fem SVG-figurer, fyra delkort och metadata OK.')
