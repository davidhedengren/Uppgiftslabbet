"""Oberoende integralberäkningar, delkort och figurkoordinater för 29 uppgifter."""
import json,subprocess,re,math,xml.etree.ElementTree as E,importlib.util
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
raw=subprocess.check_output(['node','-e',"const fs=require('fs'),vm=require('vm'),c={window:{}};vm.runInNewContext(fs.readFileSync('uppgiftermatf1.js','utf8'),c);console.log(JSON.stringify(Object.values(c.window).find(Array.isArray)));"],cwd=ROOT,text=True)
q={v['id']:v for v in json.loads(raw) if v['omr']=='integraler_area'};seen=set();x,a,k,t=s.symbols('x a k t',real=True)
def val(id,v):
 target=s.sympify(q[id]['rättSvar']);assert abs(float(target-v))<1e-12,(id,target,v);seen.add(id)
def integ(f,l,r):return s.integrate(f,(x,l,r))
val('3.12',s.solve(integ(a*x-x*x,0,a)-s.Rational(9,2),a)[0])
val('3.22',-integ(x*x-4*x+3,1,3));val('3.28',integ(4-x,1,3))
val('3.206',integ(x*x,0,4));val('3.208',integ(4*x*x,0,4)/4)
assert integ(2*x,0,s.sqrt(2))==2 and s.diff(integ(2*x,0,t),t)==2*t;seen.add('3.210')
val('3.49',integ(4-x*x,-2,2));val('3.50',integ(x*x,0,3)/3)
assert s.solve(x*x-x-2,x)==[-1,2];val('3.51',integ(x+2-x*x,-1,2))
val('3.70',integ(6-2*x,0,3));val('3.71',integ(x**3+4,-2,2));val('3.219',integ(x**3,0,4)/4)
val('3.73',max(s.solve(integ(2*x,0,a)-25,a)))
val('3.80',integ(x*x-1,-2,-1)+integ(1-x*x,-1,1)+integ(x*x-1,1,2))
val('3.224',max(s.solve(integ(4*x,0,t)-5,t)))
assert abs(float(integ(s.exp(-x*x),0,2))-.8821)<.00005;seen.add('3.53')
assert 'momentan' in q['3.75']['s'] and '3,7 °C/min' in q['3.75']['s'];seen.add('3.75')
assert s.solve(x*x-2*x,x)==[0,2]
assert q['3.84']['spelDelar'][0]['rättSvar']==['(0,0)','(2,4)']
assert q['3.84']['spelDelar'][0]['svarsstruktur']=='mängd'
assert abs(q['3.84']['spelDelar'][1]['rättSvar']-float(integ(2*x-x*x,0,2)))<1e-14;seen.add('3.84')
val('3.102',integ(2*x+1,0,3)/3);val('3.103',integ(x-x*x,0,1))
val('3.104',s.solve(integ(k*x-x*x,0,k)-s.Rational(4,3),k)[0])
val('3.285',max(s.solve(integ(x*x,0,a)/a-12,a)))
assert s.solve(s.sqrt(x)-x/2,x)==[0,4];val('3.288',integ(s.sqrt(x)-x/2,0,4))
val('3.347',integ(s.exp(x),0,s.log(3)));val('3.348',integ(3*x*x,0,2))
val('3.349',integ(s.sin(x),0,s.pi));val('3.350',integ(20+4*s.sin(s.pi*x/12),0,12)/12)
val('3.351',sum((u+v)/2 for u,v in zip([2,3,5],[3,5,8])));val('3.352',integ(1/x,1,s.E))
assert seen==set(q) and len(q)==29
for id,v in q.items():
 assert 'facit-rubrik' in v['s'] and 'facit-svar' in v['s'] and v['ledtrad'],id
 assert v['miniräknare'] and not v['geogebra'],id
 assert v['traningsniva'] in range(1,6)
 for field in ['t','s','ledtrad']:
  for formula in re.findall(r'\\\((.*?)\\\)|\\\[(.*?)\\\]',v[field],re.S):assert '<' not in ''.join(formula),(id,field)
for id in ['3.49','3.51','3.103']:assert q[id]['svarFormat']=='numeriskt' and q[id]['tolerans']==0
assert q['3.288']['svarFormat']=='bråk' and q['3.224']['svarFormat']=='uttryck'
assert q['3.350']['rättSvar']!=22.5 and q['3.350']['tolerans']==.05
for id in ['3.50','3.102','3.103']:assert q[id]['självrättning'] is True and q[id]['spel'] is True
for id in ['3.210','3.53','3.75']:assert q[id]['spel'] is False
# Läs de faktiska SVG-punkterna och jämför med de matematiska funktionerna.
spec=importlib.util.spec_from_file_location('figs',ROOT/'tools/matf1-area-figurer-2026-10-26.py');figs=importlib.util.module_from_spec(spec);spec.loader.exec_module(figs)
for id,cfg in figs.SPECS.items():
 svg=E.fromstring(re.search(r'<svg[\s\S]*?</svg>',q[id]['t'])[0]);ns={'s':'http://www.w3.org/2000/svg'}
 lines=svg.findall('s:polyline',ns);assert len(lines)==len(cfg['curves'])
 x0,x1=cfg['xr'];y0,y1=cfg['yr']
 for line,(_,f,_) in zip(lines,cfg['curves']):
  ps=[tuple(map(float,p.split(','))) for p in line.get('points').split()]
  lo,hi=cfg.get('domain',cfg['xr'])
  for i,(px,py) in enumerate(ps):
   xv=lo+(hi-lo)*i/(len(ps)-1)
   assert abs(px-(64+(xv-x0)*440/(x1-x0)))<.006
   assert abs(py-(306-(f(xv)-y0)*220/(y1-y0)))<.006
 for polygon in svg.findall('s:polygon',ns):
  ps=[tuple(map(float,p.split(','))) for p in polygon.get('points').split()]
  assert all(63.99<=px<=504.01 and 85.99<=py<=306.01 for px,py in ps)
print('29 uppgifter: oberoende integraler, exakta/numeriska mål, delkort och sju figurgeometrier OK.')
