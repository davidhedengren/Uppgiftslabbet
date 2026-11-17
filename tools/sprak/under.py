import json,math,collections,re,sys
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from jamfor import ord_,ngram
k=json.load(open('korpus.json',encoding='utf-8'))
k=[x for x in k if not x['skapad'].startswith('2026') and '2026' not in x['fil']]
kt=[p for x in k for p in x['text']]
bt=list(json.load(open('bank_t.json',encoding='utf-8')).values())
for n in (1,2,3):
  kc=collections.Counter(g for p in kt for g in ngram(ord_(p),n))
  bc=collections.Counter(g for t in bt for g in ngram(ord_(t),n))
  ks,bs=sum(kc.values()),sum(bc.values())
  r=[]
  for g,c in kc.items():
    if c<12 or 'x' in g.split():continue
    b=bc.get(g,0); r.append((math.log2(((c+.5)/ks)/((b+.5)/bs)),g,c,b))
  r.sort(reverse=True)
  print('=== under',n)
  print('\n'.join(f'{a:4.1f} {c:4d} {b:5d} {g}' for a,g,c,b in r[:90]))
