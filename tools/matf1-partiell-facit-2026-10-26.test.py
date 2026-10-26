"""Oberoende derivator/gränser och bevarade kontrakt för hela området."""
import json,subprocess,re
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
raw=subprocess.check_output(['node','-e',"const fs=require('fs'),vm=require('vm'),c={window:{}};vm.runInNewContext(fs.readFileSync('uppgiftermatf1.js','utf8'),c);console.log(JSON.stringify(Object.values(c.window).find(Array.isArray)));"],cwd=ROOT,text=True)
bank=json.loads(raw);parents=[q for q in bank if q['omr']=='partiell_integration'];assert len(parents)==36
cards={}
for q in parents:
 assert q['miniräknare'] and not q['geogebra'],q['id']
 assert 'facit-rubrik' in q['s'] and 'facit-svar' in q['s'],q['id']
 if q.get('spelDelar'):
  for i,p in enumerate(q['spelDelar']):
   card={**q,**p,'id':q['id']+p['etikett'],'svarFormat':q['svarFormat'][i]}
   cards[card['id']]=card
   assert p['s'] in q['s'],card['id']
 else:cards[q['id']]=q
assert len(cards)==44
x,t=s.symbols('x t',positive=True);ns=dict(s=s,x=x,t=t,exp=s.exp,log=s.log,sin=s.sin,cos=s.cos)
checks=json.loads(Path(__file__).with_name('matf1-partiell-facit-2026-10-26.matematik.json').read_text())
assert {r['id'] for r in checks}==set(cards)
for r in checks:
 q=cards[r['id']];assert q['ledtrad'] and 'facit-rubrik' in q['s']
 f=eval(r['integrand'],ns)
 if 'primitive' in r:
  F=eval(r['primitive'],ns);v=ns[r['variable']]
  assert s.simplify(s.diff(F,v)-f)==0,r['id']
  if r['id']=='3.320a':assert F.subs(x,0)==2
  elif r['id']=='3.320b':assert F.subs(x,0)==3
  elif r['id'] in ['3.125','3.132','3.133','3.135']:assert q['svarFormat']=='primitiv'
  else:assert q['svarFormat']=='primitiva',r['id']
 else:
  a,b=[s.sympify(v) for v in r['bounds']]
  assert s.simplify(s.integrate(f,(x,a,b))-s.sympify(r['value']))==0,r['id']
assert 'mer än en gång' not in cards['3.15']['ledtrad']
assert cards['3.318c']['svarFormat']=='primitiva'
assert all(q['traningsniva']>=2 for q in cards.values())
print('36 huvuduppgifter / 44 kort: derivator, gränser, villkor, svarsformat och verktyg kontrollerade.')
