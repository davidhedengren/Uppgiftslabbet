"""Oberoende kontroll av tangentvärden, tecken, referensprecision och delkort."""
import json, subprocess, math
from pathlib import Path
import sympy as s
ROOT = Path(__file__).resolve().parents[1]
raw = subprocess.check_output(['node', '-e', "const fs=require('fs'),vm=require('vm'),c={window:{}};vm.runInNewContext(fs.readFileSync('uppgiftermatf1.js','utf8'),c);console.log(JSON.stringify(Object.values(c.window).find(Array.isArray)));"], cwd=ROOT, text=True)
parents = {q['id']: q for q in json.loads(raw) if q['omr']=='linjar_approximation'}
assert len(parents)==39
x=s.symbols('x', positive=True)
def tangent(f,a):
    return s.expand(f.subs(x,a)+s.diff(f,x).subs(x,a)*(x-a))
def value(f,a,b):
    return float(tangent(f,a).subs(x,s.Rational(str(b))))
def close(a,b):
    assert math.isclose(a,b,rel_tol=1e-12,abs_tol=1e-12),(a,b)
checks = {
 '3.18':(s.sqrt(x),16,'15.8'), '3.26':(s.sqrt(x),16,'16.3'),
 '3.41':(1/x,2,'2.04'), '3.192':(s.sqrt(x),49,'49.4'),
 '3.42':(x**s.Rational(1,3),27,'27.3'), '3.63':(s.sin(x),0,'.06'),
 '3.64':(s.exp(x),0,'.03'), '3.196':(s.sqrt(x),49,'49.2'),
 '3.99':(s.sqrt(x),25,'25.4'), '3.116':(s.log(x),1,'1.05'),
 '3.118':(s.sqrt(x),4,'4.1'), '3.119':(s.log(x),1,'1.03'),
 '3.120':(s.exp(x),0,'.05'), '3.277':(s.sqrt(x),36,'36.6'),
 '3.279':(x**s.Rational(1,3),8,'8.3'), '3.280':(s.log(x),1,'.97'),
 '3.281':(s.exp(-x),0,'.04'), '3.282':(1/x,1,'1.02'),
 '3.328':(x*x,2,'1.95')}
for id,args in checks.items():close(parents[id]['rättSvar'],value(*args))
for id,v in {'3.278':12+(-3)*(-.1),'3.283':float(s.diff(s.sqrt(x),x).subs(x,9)),
             '3.284':float(tangent(s.log(x),1).subs(x,0)),
             '3.315':float(s.solve(tangent(s.exp(x-1),1)-(5*x-s.Rational(9,2)),x)[0]),
             '3.324':7+3*.1,'3.325':50-2*.5,'3.326':20*.2/100*100,
             '3.327':4+.24/.8}.items():close(parents[id]['rättSvar'],v)
assert tangent(s.cos(x),0)==s.sympify(parents['3.78']['rättSvar'])==1
assert parents['3.78']['svarFormat']=='uttryck'
assert parents['3.283']['svarFormat']=='numeriskt' # Frågan kräver inte bråkform.
assert parents['3.07']['rättSvar'][0]=='3+(x-9)/6'
close(parents['3.07']['rättSvar'][1],value(s.sqrt(x),9,'9.2'))
assert parents['3.65']['rättSvar'][0]=='x-1'
close(parents['3.65']['rättSvar'][1],value(s.log(x),1,'1.08'))
close(parents['3.08']['rättSvar'][0],value(s.log(x),1,'1.04'))
assert parents['3.08']['självrättning']==[True,False]
assert parents['3.43']['självrättning'] is False
for f,a,b in [(s.log(x),1,'1.04'),(s.sqrt(x),9,'9.4')]:
    assert float(s.diff(f,x,2).subs(x,a))<0
    assert value(f,a,b)>float(f.subs(x,s.Rational(b)))
for f,a,answer in zip([x*x,x**3-2*x+3,s.exp(2*x),s.tan(x)], [3,2,0,s.pi/4],
                       [6*x-9,10*x-13,2*x+1,2*x+1-s.pi/2]):
    assert s.simplify(tangent(f,a)-answer)==0
assert parents['3.312']['rättSvar']==['6x-9','10x-13','2x+1','2x+1-pi/2']
for actual,expected in zip(parents['3.313']['rättSvar'],[value((1+x)**3,2,'2.1'),value(x**s.Rational(1,3),8,'8.5')]):close(actual,expected)
for actual,k,h in zip(parents['3.314']['rättSvar'],[50,40,-15,s.Rational(1,3)],[.002,-.002,.004,.009]):close(actual,float(1+k*h))
close(parents['3.286']['rättSvar'][0],value(s.sqrt(x),4,'4.1'))
close(parents['3.286']['rättSvar'][1],(.1/.01)**2)
T=21+8*s.sin(s.pi*(x-8)/24)
close(parents['3.316']['rättSvar'][0],float(s.diff(T,x).subs(x,6)))
close(parents['3.316']['rättSvar'][1],value(T,6,'6.25'))
T=18+80*s.exp(-s.Rational(277,1000)*x)
assert tangent(T,0)==98-s.Rational(554,25)*x
actual=float(T.subs(x,s.Rational(1,2)))
close(parents['3.317']['rättSvar'][1],100*(actual-value(T,0,'.5'))/actual)
assert parents['3.317']['rättSvar'][0]=='98-22.16x'
assert tangent(x**3,0)==0
assert [a['txt'] for a in parents['3.329']['alternativ'] if a['ratt']]==['0']
for id in ['3.192','3.196']:assert parents[id]['tolerans']==.00005
assert parents['3.315']['tolerans']<.0001 # Ska inte godta den icke-linjära ekvationens rot.
cards=0
for q in parents.values():
    assert not q['geogebra']
    assert 'facit-rubrik' in q['s'] and 'facit-svar' in q['s'] and q['ledtrad'],q['id']
    assert '\\prime' not in q['s'].replace('^{\\prime}','').replace('^{\\prime\\prime}','')
    parts=q.get('spelDelar',[]);cards+=len(parts) or 1
    for p in parts:
        assert 'facit-rubrik' in p['s'] and 'facit-svar' in p['s'] and p['ledtrad']
    if q['id']=='3.316':
        assert q['svarEnhet']==['°C/h','°C']
        assert '18,93' in parts[1]['t'] and '1,01' in parts[1]['t']
for id in ['3.07','3.42','3.192','3.196','3.316','3.317']:assert parents[id]['miniräknare']
assert cards==48
print('39 huvuduppgifter / 48 kort: tangentberäkningar, konkavitet, precision, självständiga delkort och verktyg godkända.')
