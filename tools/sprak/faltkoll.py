import json,sys
def load(p):
    s=open(p,encoding='utf-8').read(); i=s.index('['); return {u['id']:u for u in json.JSONDecoder().raw_decode(s[i:])[0]}
a=load(sys.argv[1]); b=load(sys.argv[2]); undantag=set(sys.argv[3:])
TILLATNA={'t','spelIntro','kgInstruktion','visaAlternativ','s'}
n=0
for id_,u in b.items():
    v=a.get(id_)
    if v is None: print('ny',id_); continue
    for k in set(u)|set(v):
        if k=='spelDelar': continue
        if u.get(k)!=v.get(k):
            if k not in TILLATNA: print(id_,k); n+=1
            elif k=='s' and id_ not in undantag: print('S ÄNDRAD',id_); n+=1
    if len(u.get('spelDelar') or [])!=len(v.get('spelDelar') or []): print(id_,'antal delar'); n+=1
    for i,(d1,d0) in enumerate(zip(u.get('spelDelar') or [],v.get('spelDelar') or [])):
        for k in set(d1)|set(d0):
            if d1.get(k)!=d0.get(k) and k not in ('t','fraga','kgInstruktion'): print(id_,'del',i,k); n+=1
print('avvikelser:',n)
