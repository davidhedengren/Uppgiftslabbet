import json,re,collections
k=json.load(open('korpus.json',encoding='utf-8'))
k=[x for x in k if not x['skapad'].startswith('2026') and '2026' not in x['fil']]
kt=[p for x in k for p in x['text'] if len(p)>25 and not re.search(r'poäng|betyg|Hjälpmedel|kriterier|Max',p)]
bt=list(json.load(open('bank_t.json',encoding='utf-8')).values())
def meningar(ts):
  out=[]
  for t in ts:
    for m in re.split(r'(?<=[.?!])\s+',t):
      m=m.strip()
      if len(m)>3: out.append(m)
  return out
km,bm=meningar(kt),meningar(bt)
import statistics as st
print('medel ord/mening korpus',st.mean(len(m.split()) for m in km),'bank',st.mean(len(m.split()) for m in bm))
print('frågemeningar (?) andel korpus',sum(m.endswith('?') for m in km)/len(km),'bank',sum(m.endswith('?') for m in bm)/len(bm))
def start(ms,n=2): return collections.Counter(' '.join(m.split()[:n]) for m in ms)
kc,bc=start(km),start(bm)
print('== vanligaste meningsstarter korpus (per 1000 meningar) vs bank')
for g,c in kc.most_common(60): print(f'{c/len(km)*1000:5.1f} {bc.get(g,0)/len(bm)*1000:5.1f}  {g}')
print('== bank')
for g,c in bc.most_common(60): print(f'{kc.get(g,0)/len(km)*1000:5.1f} {c/len(bm)*1000:5.1f}  {g}')
