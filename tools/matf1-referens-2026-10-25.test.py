"""Oberoende kontroll av de nya uppgifterna. Kräver SymPy."""
import json,math,itertools,re
from pathlib import Path
import sympy as s
from sympy.parsing.sympy_parser import parse_expr,standard_transformations,convert_xor
root=Path(__file__).resolve().parents[1];raw=(root/'uppgiftermatf1.js').read_text()
bank=json.loads(raw[raw.index('['):raw.rindex(']')+1]);q={v['id']:v for v in bank}
ids=[f'1.{i}' for i in range(802,809)]+[f'2.{i}' for i in range(720,726)]+[f'3.{i}' for i in range(353,358)]
assert len(q)==len(bank),'Dubblerade ID:n'
x=s.Symbol('x',positive=True);C=s.Symbol('C');n=s.Symbol('n',integer=True,positive=True)
def parse(v):return parse_expr(str(v),local_dict={'x':x,'n':n,'C':C,'e':s.E,'pi':s.pi,'ln':s.log},transformations=standard_transformations+(convert_xor,))
for id,f in {'3.353':(2*x-1)*s.exp(x),'3.354':x**3*s.log(x),'3.355':x*x*s.cos(2*x),'3.356':s.exp(2*x)*s.sin(x)}.items():
 assert s.simplify(s.diff(parse(q[id]['rättSvar']),x)-f)==0,id
 assert q[id]['svarFormat']=='primitiva'
assert parse(q['3.357']['rättSvar'])==s.integrate(x*s.cos(x),(x,0,s.pi/2))
expected={'1.802':math.comb(10,7),'1.803':sum(abs(p.index('A')-p.index('B'))==1 for p in itertools.permutations('ABCDEFG')),'1.807':sum(c[1]==8 for c in itertools.combinations(range(1,41),4)),'1.808':next(i for i in range(10) if math.factorial(i)==120),'2.720':47%6,'2.721':next(a for a in range(20,51) if a%5==2 and a%7==4),'2.722':(-79)%13,'2.723':(17+pow(7,123,24))%24,'2.724':pow(14,37,9),'2.725':(pow(23,42,10)+pow(17,43,10))%10}
assert [a for a in range(20,51) if a%5==2 and a%7==4]==[32]
for id,want in expected.items():assert q[id]['rättSvar']==want,(id,want)
for id,f in {'1.804':s.factorial(n+2)/s.factorial(n),'1.805':(s.factorial(n+1)-3*s.factorial(n))/s.factorial(n),'1.806':(s.factorial(n+2)+s.factorial(n+1))/s.factorial(n)}.items():
 assert s.simplify(parse(q[id]['rättSvar'])-s.simplify(f))==0,id
for id in ids:
 t=q[id];assert t['spel'] and t['självrättning'] and not t.get('alternativ')
 assert t['t'] and t['ledtrad'] and 'facit-svar' in t['s']
 assert not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]',t['t']+t['s'])
 assert not t['geogebra'] or t['miniräknare']
 assert 1<=t['traningsniva']<=5
for id in ['1.803','1.807','2.723','3.357']:assert '<svg' in q[id]['t']
for id in ['1.802','1.803','1.807','1.808']:assert q[id]['svarFormat']=='antal_satt' and q[id]['tolerans']==0
print('18 uppgifter: symbolisk matematik, brute force-räkning, modulo, metadata och facit godkända.')
