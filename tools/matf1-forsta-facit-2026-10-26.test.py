"""Oberoende algebra, funktionskontroller och avrundning för 68 uppgifter."""
import json,re,subprocess,math
from pathlib import Path
import sympy as s
from sympy.parsing.sympy_parser import parse_expr,standard_transformations,implicit_multiplication_application,convert_xor
ROOT=Path(__file__).resolve().parents[1]
raw=subprocess.check_output(['node','-e',"const fs=require('fs'),vm=require('vm'),c={window:{}};vm.runInNewContext(fs.readFileSync('uppgiftermatf1.js','utf8'),c);console.log(JSON.stringify(Object.values(c.window).find(Array.isArray)));"],cwd=ROOT,text=True)
Q={v['id']:v for v in json.loads(raw) if v['omr'] in ['homogena_forsta','inhomogena_forsta']};seen=set()
x,t,C=s.symbols('x t C',real=True)
def parse(v):
 v=str(v).removeprefix('y=').replace(r'\frac{x}{3}','(x/3)').replace(r'\frac19','(1/9)').replace(r'\frac12','(1/2)')
 v=v.replace('{','(').replace('}',')')
 return parse_expr(v,local_dict={'x':x,'t':t,'C':C,'e':s.E,'ln':s.log},transformations=standard_transformations+(implicit_multiplication_application,convert_xor))
def ode(id,rate,source=0,initial=None):
 f=parse(Q[id]['rättSvar']);assert s.simplify(s.diff(f,x)-rate*f-source)==0,(id,f)
 if initial:
  at,value=initial;assert s.simplify(f.subs(x,at)-value)==0,(id,f)
  assert Q[id]['svarFormat']=='uttryck'
 else:
  assert Q[id]['svarFormat']=='diffekv_losning',id
  assert C in f.free_symbols and s.diff(f,C)!=0 and s.diff(f,C,2)==0,id
 seen.add(id)
for id,k,src,init in [
 ('4.48',2,0,(0,5)),('4.03',3,0,None),('4.358',3*x,0,None),('4.50',-s.Rational(1,2),0,(0,12)),
 ('4.67',-4,0,None),('4.68',s.Rational(3,10),0,(0,7)),('4.124',2,0,(0,3)),('4.125',-s.Rational(1,2),0,(0,8)),
 ('4.362',-2,5,None),('4.09',3,-x,None),('4.21',2,s.exp(3*x),None),('4.51',-2,6,None),('4.71',-2,10,(0,1)),
 ('4.94',-2,8,None),('4.95',-3,6,(0,5)),('4.142',2,8,None),('4.143',s.Rational(1,2),-3,None),('4.145',2,4*x-1,None),
 ('4.107',-1,4,(0,10)),('4.126',1,4,(0,2)),('4.168',-1,3,(0,5)),('4.612',6,0,None),('4.618',-2,10,None),
 ('4.622',-2,10,(0,5)),('4.623',-1,4,(0,0))]:ode(id,k,src,init)
def answer(id,expected):
 actual=Q[id]['rättSvar'];actual=actual if isinstance(actual,list) else [actual];expected=expected if isinstance(expected,list) else [expected]
 assert len(actual)==len(expected)
 for a,e in zip(actual,expected):assert abs(float(parse(a))-float(e))<1e-10,(id,a,e)
 seen.add(id)
for id,val in {
 '4.69':s.log(s.Rational(18,12))/5,'4.120':10/s.E**2,'4.396':2*s.E,'4.397':6+4*s.exp(-6),'4.399':[6,s.log(2)],
 '4.515':5730*s.log(s.Rational(10,3))/s.log(2),'4.516':50*s.exp(-s.Rational(6,5)),
 '4.520':[s.log(2)/20,20*s.log(1000)/s.log(2)],'4.556':2*s.log(s.Rational(20,14))/s.log(s.Rational(17,14)),
 '4.557':200*s.Rational(5,2)**3,'4.558':[14*s.exp(s.Rational(35,100)),s.log(s.Rational(122,14))/7],
 '4.559':s.log(200)/48,'4.560':s.log(2)/s.Rational(55,10),'4.517':5*s.log(s.Rational(7,2))/s.log(s.Rational(7,5)),
 '4.521':[20,20*s.log(4)],'4.591':6/2,'4.592':[-2,-2],'4.593':6/(2+1),'4.594':s.Rational(98,10)/s.Rational(1,2),
 '4.596':s.log(3),'4.597':[-s.Rational(1,2),2],'4.606':s.Rational(3,10),'4.608':3,'4.609':s.Rational(1,2)*4,
 '4.611':100*s.exp(-s.Rational(1,2)),'4.613':3*(s.Rational(6,3))**3,'4.614':10/s.E,'4.615':10*s.log(2),
 '4.616':s.log(3),'4.617':18/3,'4.620':6-2*1,'4.621':[5,10],'4.624':[2,1],'4.625':5/(-2+1),
 '4.627':s.Rational(1,2)*10,'4.628':3-3*s.exp(-2)}.items():answer(id,val)
f=parse(Q['4.554']['rättSvar'][0]);assert s.simplify(s.diff(f,t)-s.Rational(5,100)*f)==0 and f.subs(t,0)==1500
assert abs(float(f.subs(t,7))-Q['4.554']['rättSvar'][1])<1e-10;seen.add('4.554')
assert Q['4.607']['rättSvar']=="y'=0.02y";seen.add('4.607')
for id,funcs,op in [
 ('4.605',[5*s.exp(x),s.exp(x/5),s.exp(5*x),x**5],lambda f:s.diff(f,x)-5*f),
 ('4.610',[2*s.exp(s.Rational(6,10)*x),s.Integer(2),2*s.exp(-s.Rational(6,10)*x)],lambda f:s.diff(f,x)+s.Rational(6,10)*f),
 ('4.595',[2+2*s.exp(-x),2-2*s.exp(-x),4*s.exp(-x)],lambda f:s.diff(f,x)-(2-f)) ,
 ('4.619',[4*x,s.exp(-x),s.Integer(4),4*s.exp(-x)],lambda f:s.diff(f,x)+f-4)]:
 expected=[s.simplify(op(f))==0 and (id!='4.595' or f.subs(x,0)==4) for f in funcs]
 assert expected==[a['ratt'] for a in Q[id]['alternativ']],id;seen.add(id)
assert [o['ratt'] for o in Q['4.626']['alternativ']]==[False,True,False,False]
for c in [-1,1]:assert s.diff(abs(c)*s.exp(2*x),x)>0
seen.add('4.626')
assert seen==set(Q) and len(Q)==68
for id,q in Q.items():
 assert q['miniräknare'] and not q['geogebra'],id
 assert 'facit-rubrik' in q['s'] and 'facit-svar' in q['s'],id
 for p in q.get('spelDelar',[]):assert 'facit-rubrik' in p['s'] and p['ledtrad'],id
for id,tol in [('4.515',5),('4.516',.005),('4.556',.05),('4.559',.0005),('4.560',.0005),('4.517',.05)]:assert Q[id]['tolerans']==tol
assert all(Q[id]['tolerans']==0 for id in ['4.69','4.120','4.396','4.397','4.557'])
assert 'begynnelsevillkoren' not in Q['4.396']['ledtrad']
assert 'C får också vara 0' in Q['4.358']['s']
assert '1500e' in Q['4.554']['spelDelar'][1]['t']
print('68 uppgifter: lösningar, startvillkor, fria konstanter, numeriska mål, alternativ och delkort OK.')
