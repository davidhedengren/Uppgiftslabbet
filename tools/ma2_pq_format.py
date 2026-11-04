"""Formatera granskade lösningsplaner utan att ändra banken."""
import sys,math
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent/"fy1-facit-kap23"))
from render import solution,p,m,inline as I
def st(h,tex='',why=''):return (h,(p(why) if why else '')+(m(tex) if tex else ''))
def num(v):return f'{v:g}'.replace('.', '{,}')
def pq(a,b,v='x'):
 # Arithmetic rendering of explicitly selected p,q; not heuristic task classification.
 half=-a/2;disc=(a/2)**2-b;root=math.sqrt(disc)
 assert root*2==round(root*2)
 aa=num(a);bb=num(b);sub=bb if b>=0 else '('+bb+')'
 tex=rf'\begin{{aligned}}{v}&=-\frac{{{aa}}}2\pm\sqrt{{\left(\frac{{{aa}}}2\right)^2-{sub}}}\\&={num(half)}\pm\sqrt{{{num((a/2)**2)}'+('-'+bb if b>=0 else '+'+num(-b))+rf'}}\\&={num(half)}\pm\sqrt{{{num(disc)}}}\\&={num(half)}\pm {num(root)}\end{{aligned}}'
 return [st('Pq-formeln: '+I(v+r'=-\frac p2\pm\sqrt{(\frac p2)^2-q}'),why='Jämför med '+I(v+'^2+p'+v+'+q=0')+'. Här är '+I('p='+aa)+' och '+I('q='+bb)+'.'),st('Sätt in p och q',tex),st('Beräkna båda rötterna',rf'{v}_1={num(half+root)},\qquad {v}_2={num(half-root)}')]
