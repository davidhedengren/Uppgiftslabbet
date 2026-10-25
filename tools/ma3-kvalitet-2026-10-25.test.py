"""Oberoende matematikkontroll av granskade bankfacit. Kräver sympy."""
import json, math, re
from pathlib import Path
import sympy as s
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor
root=Path(__file__).resolve().parents[1]
raw=(root/'uppgiftermato1.js').read_text()
bank=json.loads(raw[raw.index('['):raw.rindex(']')+1]);q={v['id']:v for v in bank}
x=s.Symbol('x',positive=True);a,C=s.symbols('a C')
def expr(value):
 value=str(value).split('=')[-1].replace('ln2','ln(2)').replace('xsqrt','x*sqrt')
 return parse_expr(value,local_dict={'x':x,'a':a,'C':C,'e':s.E,'sqrt':s.sqrt,'ln':s.log},transformations=standard_transformations+(implicit_multiplication_application,convert_xor))
def answer(id):return expr(q[id]['rättSvar'])
# Derivator räknas från funktionerna i frågan, oberoende av facitets mellanled.
for id,f in {'2.02':2*x**4-3*x**3+5*x,'2.10':5*x**3-2*s.sqrt(x),'2.212':x**s.Rational(3,2)+6/x,'2.250':x**s.Rational(3,2)-7/x+1/s.sqrt(x),'2.539':a*x**2-4/x,'2.1167':x*x}.items():
 assert s.simplify(answer(id)-s.diff(f,x))==0,id
# Här kontrolleras bankens faktiska uttryck genom derivering.
for id,f in {'3.134':s.sqrt(x),'3.138':x**s.Rational(3,2),'3.142':x**-2,'3.146':3*x+2*s.exp(x),'3.150':3*2**x+x*x,'3.162':x**3,'3.174':s.sqrt(x),'3.236':4/x**2+3*s.sqrt(x),'3.283':16*x**3+2*x,'3.284':5*x**s.Rational(3,2)-2/x**3,'3.82':6*x*x-4/x**2,'3.1217':(x*x-1)**2/x**2,'3.1218':(x+1)**2/s.sqrt(x),'3.1220':(s.exp(x)-2)**2}.items():
 assert s.simplify(s.diff(answer(id),x)-f)==0,id
assert answer('3.162').subs(x,2)==7
assert answer('3.174').subs(x,4)==10
F=2*x**3-x*x+C
assert q['3.1063']['rättSvar']==F.subs(x,2)-F.subs(x,1)
assert q['3.1057']['rättSvar']==7+3
for id,want in {'3.921':math.e-1,'3.1052':7-math.e,'3.1011':math.e+3,'3.1016':2*3**2+10,'3.1106':2*1+1,'2.740':9,'3.182':6/3,'3.194':3**2}.items():
 assert abs(q[id]['rättSvar']-want)<1e-12,id
for id in ['3.921','3.1052','3.1011']:
 value=q[id]['rättSvar'];rounded=round(value,2);tol=q[id]['tolerans']
 assert abs(value-rounded)<=tol
 assert all(abs(value-wrong)>tol for wrong in [rounded-.01,rounded+.01])
# Tangenten ska verkligen gå genom den givna punkten och beröra kurvan.
tx,ty=q['2.812']['rättSvar'];assert ty==math.sqrt(tx)
assert (ty-0)/(tx+4)==1/(2*math.sqrt(tx))
assert q['2.825']['rättSvar']==[2,4]
assert s.diff(x+4/x,x).subs(x,2)==0 and s.diff(x+4/x,x,2).subs(x,2)>0
# Ökande behöver inte betyda strikt positiv derivata i varje punkt.
assert s.diff(x**3,x).subs(x,0)==0
assert '≥' in q['3.198']['s'] and '≤' in q['3.198']['s']
assert 'samma intervall' in q['3.178']['t']
for first,second in [('2.605','2.740'),('2.585','2.744'),('3.1011','3.921'),('3.1011','3.1052'),('3.1012','3.1063'),('3.1015','3.1057')]:
 assert q[first]['t']!=q[second]['t']
changes=json.loads((root/'agent/MA3_KVALITET_2026-10-25.andringar.json').read_text())
for id in changes:
 task=q[id];assert task['geogebra'] is not True or task['miniräknare'] is True,id
 assert not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]',task['t']+task['s']),id
for id,level in {'3.182':2,'3.194':2,'3.283':2,'3.551':2,'3.617':2,'3.727':2,'2.812':3,'2.825':3,'3.58':3}.items():
 assert q[id]['traningsniva']==level,id
assert q['3.1106']['svarEnhet']=='m/s'
print('Oberoende matematik, avrundning, nivåbeslut och metadata: godkända.')
