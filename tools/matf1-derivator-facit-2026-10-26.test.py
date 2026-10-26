"""Oberoende matematik, precision och figurer för 27 derivatuppgifter."""
import json,subprocess,math,re,xml.etree.ElementTree as ET
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
raw=subprocess.check_output(['node','-e',"const fs=require('fs'),vm=require('vm'),c={window:{}};vm.runInNewContext(fs.readFileSync('uppgiftermatf1.js','utf8'),c);console.log(JSON.stringify(Object.values(c.window).find(Array.isArray)));"],cwd=ROOT,text=True)
bank=json.loads(raw);q={v['id']:v for v in bank if v['omr']=='repetition_derivator'}
assert len(q)==27
x,a=s.symbols('x a',real=True)
def close(actual,expected):assert math.isclose(actual,float(expected),abs_tol=1e-12,rel_tol=1e-12),(actual,expected)
def roots(id,f,derivative_target=0):
    expected=sorted([float(v) for v in s.solve(s.diff(f,x)-derivative_target,x)])
    actual=sorted(float(s.sympify(str(v).replace('sqrt','sqrt'))) for v in q[id]['rättSvar'])
    assert len(actual)==len(expected)
    for av,ev in zip(actual,expected):close(av,ev)
    assert q[id]['svarsstruktur']=='mängd'
roots('3.207',x**3-9*x+4);roots('3.212',x**3-12*x+4);roots('3.333',x**3-3*x,3)
for id,expr,start in [('3.209',x*s.exp(x)-8,1.6),('3.227',x+s.log(x)-6,4.5),('3.338',s.exp(x)-3*x,1.5)]:
    close(q[id]['rättSvar'],s.nsolve(expr,start,prec=40))
    assert q[id]['geogebra'] and q[id]['miniräknare']
    assert q[id]['traningsniva']==2
assert q['3.209']['tolerans']==q['3.338']['tolerans']==.0005
for id,H in [('3.52',9),('3.83',12)]:
    A=2*x*(H-x*x);critical=s.sqrt(s.Rational(H,3))
    assert s.diff(A,x).subs(x,critical)==0
    assert s.diff(A,x).subs(x,critical/2)>0
    assert s.diff(A,x).subs(x,(critical+s.sqrt(H))/2)<0
    if id=='3.52':close(q[id]['rättSvar'],A.subs(x,critical))
    else:assert A.subs(x,critical)==32
    svg=ET.fromstring(re.search(r'<svg[\s\S]*?</svg>',q[id]['t']).group())
    ns={'s':'http://www.w3.org/2000/svg'}
    rect=svg.findall('s:rect',ns)[1];point=svg.find('s:circle',ns)
    rx=(float(point.get('cx'))-240)/50
    ry=(255-float(point.get('cy')))/16
    close(ry,H-rx*rx);close(float(rect.get('width'))/50,2*rx)
    close(float(rect.get('height'))/16,ry)
    assert not math.isclose(rx,float(critical)) # Figuren får inte visa maxlösningen.
    for xy in svg.find('s:polyline',ns).get('points').split():
        px,py=map(float,xy.split(','));fx=(px-240)/50;fy=(255-py)/16
        assert abs(fy-(H-fx*fx))<.002
f=x**3-6*x
assert s.solve(s.diff(f,x),x)==[-s.sqrt(2),s.sqrt(2)]
assert [s.sign(s.diff(f,x).subs(x,v)) for v in [-2,0,2]]==[1,-1,1]
assert 'absolutbelopp' not in q['3.29']['ledtrad']
assert 'kritiska punkterna' not in q['3.29']['t']
assert '\\le-\\sqrt2' in q['3.29']['s'] and '\\ge\\sqrt2' in q['3.29']['s']
assert s.sqrt(s.Integer(-2)**2)==2 # 3.54: motexempel och båda ekvationsrötterna.
assert s.solve(s.Abs(x)-2,x)==[-2,2]
p=x**3-x-2
assert p.subs(x,s.Rational(1521,1000))==s.Rational(-2256239,10**9)
assert p.subs(x,s.Rational(1522,1000))==s.Rational(3688648,10**9)
f=x**3-2*x;expected=sorted(float(v) for v in s.solve(f-s.diff(f,x),x))
for av,ev in zip(sorted(q['3.287']['rättSvar']),expected):close(av,ev)
assert s.expand((x+1)*(x*x-4*x+2))==f-s.diff(f,x)
functions={
 '3.330':(s.log(1+x*x),1,1),'3.331':(x**3-3*x*x,2,2),
 '3.340':((2*x+1)**3,1,1),'3.341':(x*x*s.exp(x),1,1),
 '3.342':(x/(x*x+1),0,1),'3.343':(s.sin(3*x)+s.cos(2*x),0,1)}
for id,(f,point,order) in functions.items():close(q[id]['rättSvar'],s.diff(f,x,order).subs(x,point))
f=x*s.exp(-x)
close(q['3.332']['rättSvar'],s.solve(s.diff(f,x),x)[0]);assert s.diff(f,x).subs(x,0)>0 and s.diff(f,x).subs(x,2)<0
f=x**3-3*x*x;assert s.diff(f,x).subs(x,0)==0 and s.diff(f,x,2).subs(x,0)<0;close(q['3.334']['rättSvar'],0)
close(q['3.335']['rättSvar'],s.solve(s.diff(x*x+a*x,x).subs(x,2)-1,a)[0])
assert s.expand((x*x-4)**2-16)==x**4-8*x*x;close(q['3.336']['rättSvar'],-16)
close(q['3.337']['rättSvar'],s.solve(s.diff(x*x,x)-6,x)[0])
f=s.log(x)-x/2;close(q['3.339']['rättSvar'],s.solve(s.diff(f,x),x)[0]);assert s.diff(f,x).subs(x,1)>0 and s.diff(f,x).subs(x,3)<0
# Värden och lutning från grafen samt tabellvärdena kontrolleras oberoende.
m=s.Rational(4-2,4-0)
close(q['3.344']['rättSvar'],2*3*m);close(q['3.345']['rättSvar'],2*m)
for id in ['3.344','3.345']:
    svg=ET.fromstring(re.search(r'<svg[\s\S]*?</svg>',q[id]['t']).group())
    circles=svg.findall('{http://www.w3.org/2000/svg}circle')
    for c,(px,py) in zip(circles,[(2,3),(0,2),(4,4)]):
        assert abs((float(c.get('cx'))-98)/50-px)<.002
        assert abs((258.571428571-float(c.get('cy')))/(276/7)-py)<.002
assert q['3.346']['rättSvar']==[3*(-1)+2*4,(3*(-1)-2*4)/(-1)**2]
assert q['3.346']['svarsstruktur']=='ordnad'
assert {id for id,v in q.items() if v.get('spel') is False}=={'3.29','3.54','3.74','3.83'}
assert {id for id,v in q.items() if v['geogebra']}=={'3.209','3.227','3.287','3.338'}
for id,v in q.items():
    assert v['miniräknare'] and v['ledtrad'] and 'facit-rubrik' in v['s'] and 'facit-svar' in v['s'],id
    assert v['traningsniva']>=2
print('27 uppgifter: derivator, rötter, maxima, tecken, numeriska referenser, verktyg och fyra SVG-figurer godkända.')
