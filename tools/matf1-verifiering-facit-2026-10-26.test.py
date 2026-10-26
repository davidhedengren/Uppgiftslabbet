"""Oberoende symboliska kontroller av alla 29 verifieringsuppgifter."""
import json, subprocess
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
raw=subprocess.check_output(['node','-e',"const fs=require('fs'),vm=require('vm'),c={window:{}};vm.runInNewContext(fs.readFileSync('uppgiftermatf1.js','utf8'),c);console.log(JSON.stringify(Object.values(c.window).find(Array.isArray)));"],cwd=ROOT,text=True)
q={v['id']:v for v in json.loads(raw) if v['omr']=='verifiering'}
x,C,D,k,a,b=s.symbols('x C D k a b',real=True)
checked=set()
def zero(id,expr):
 assert s.simplify(expr)==0,(id,expr)
 checked.add(id)
def answer(id,value):
 actual=q[id]['rättSvar']
 if isinstance(value,(list,tuple)):
  assert len(actual)==len(value)
  for u,v in zip(actual,value):assert abs(float(u)-float(v))<1e-12,(id,u,v)
 else:assert abs(float(actual)-float(value))<1e-12,(id,actual,value)
 checked.add(id)
def d(f,n=1):return s.diff(f,x,n)
for id,f,A,B,H in [
 ('4.14',4*s.exp(-2*x),0,2,0),('4.327',C*s.exp(2*x),0,-2,0),
 ('4.36',2*s.exp(x)+3,1,-1,-3),('4.64',s.sin(3*x),1,9,0),
 ('4.89',4+2*s.exp(-3*x),0,3,12),('4.144',C*s.exp(-2*x)+5,0,2,10)]:
 zero(id,(d(f,2) if A else d(f))+B*f-H)
f=x*s.exp(x);zero('4.161',d(f,2)-2*d(f)+f)
for id,rate,offset in [('4.160',-2,3),('4.72',-5,3)]:
 f=C*s.exp(rate*x)+offset;zero(id,d(f)-rate*(f-offset))
for id,f,A,B in [('4.76',(C+D*x)*s.exp(4*x),-8,16),('4.78',s.exp(2*x)*(C*s.cos(3*x)+D*s.sin(3*x)),-4,13)]:
 zero(id,d(f,2)+A*d(f)+B*f)
 # Two independent solutions: the family contains the full order-two solution space.
 zero(id,d(f,2)+A*d(f)+B*f)
 u=f.subs({C:1,D:0});v=f.subs({C:0,D:1});assert s.simplify(u*d(v)-v*d(u))!=0
f=5*s.exp(-x/5);answer('4.320',s.simplify(d(f)/f));answer('4.321',3*4)
f=s.exp(2*x)+C*s.exp(-x);answer('4.514',s.simplify((d(f)+f)/s.exp(2*x)))
f=(C+D*x)*s.exp(2*x);sol=s.solve([f.subs(x,0)-1,d(f).subs(x,0)-3],[C,D]);answer('4.522',[sol[C],sol[D]])
f=C*s.exp(-3*x)+2;answer('4.569',s.simplify(d(f)+3*f))
f=5*s.exp(k*x);answer('4.570',s.solve(s.simplify((d(f)-4*f)/f),k)[0])
answer('4.571',s.diff(x*x+C,x,2))
f=C*s.exp(x)+x;pol=s.Poly(s.expand(d(f)-f),x);answer('4.572',pol.all_coeffs())
answer('4.573',2*3+1)
f=(C+D*x)*s.exp(x);res=s.expand((d(f,2)+a*d(f)+b*f)/s.exp(x));sol=s.solve(s.Poly(res,x,C,D).coeffs(),[a,b]);answer('4.574',[sol[a],sol[b]])
f=s.cos(k*x);res=(d(f,2)+25*f).subs(x,0);answer('4.575',max(s.solve(res,k)))
f=3*s.exp(-2*x)+4;sol=s.solve([s.expand((d(f)+a*f-b)*s.exp(2*x)).subs(x,0),s.expand((d(f)+a*f-b)*s.exp(2*x)).subs(x,1)],[a,b]);answer('4.576',[sol[a],sol[b]])
for id,funcs,operator in [
 ('4.585',[2*s.exp(-x),2*s.exp(x),x+2],lambda f:d(f)+f),
 ('4.587',[x*x,3*x*x,x*x+1,x**3],lambda f:x*d(f)-2*f),
 ('4.588',[s.sin(3*x),s.cos(3*x),s.exp(3*x),s.sin(9*x)],lambda f:d(f,2)+9*f)]:
 assert [s.simplify(operator(f))==0 for f in funcs]==[o['ratt'] for o in q[id]['alternativ']]
 checked.add(id)
f=10-8*s.exp(-x/2);zero('4.586',f.subs(x,0)-2);assert d(f).subs(x,0)==s.Rational(6-2,1-0)
answer('4.586',d(f).subs(x,0)/(10-f.subs(x,0)))
f=C*s.exp(2*x)-1;answer('4.589',s.solve(f.subs(x,0)-3,C)[0])
f=s.exp(k*x);answer('4.590',s.solve(s.simplify((d(f,2)-d(f)-6*f)/f),k))
assert q['4.590']['svarsstruktur']=='mängd'
assert checked==set(q) and len(q)==29
assert sum(v.get('spel') is False for v in q.values())==7
for id,v in q.items():
 assert v['miniräknare'] is True and not v['geogebra'],id
 assert 'facit-rubrik' in v['s'] and 'facit-svar' in v['s'] and v['ledtrad'],id
 assert r'y\prime' not in v['s'],id
print('29 uppgifter: symbolisk matematik, svar, alternativ, bedömningsform och verktyg OK.')
