import json,re,sys,random,html as H
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from jamfor import BANKER,las_bank
def rå(t):
  t=re.sub(r'<svg.*?</svg>',' [SVG] ',t,flags=re.S); t=re.sub(r'<table.*?</table>',' [TABELL] ',t,flags=re.S)
  t=re.sub(r'<[^>]+>',' ',t); return re.sub(r'\s+',' ',H.unescape(t)).strip()
ALLA={}
def ladda():
  if not ALLA:
    for kod,fil in BANKER.items():
      for u in las_bank(fil): ALLA[(kod,u['id'])]=u
  return ALLA
if __name__=='__main__':
  pat=re.compile(sys.argv[1]); n=int(sys.argv[2]); kod=sys.argv[3] if len(sys.argv)>3 else None
  A=ladda(); hits=[(k,rå(u.get('t',''))) for k,u in A.items() if (not kod or k[0]==kod) and pat.search(rå(u.get('t','')))]
  random.seed(3); print(len(hits),'träffar')
  for k,t in random.sample(hits,min(n,len(hits))): print(f'- {k[0]} {k[1]}: {t[:420]}')
