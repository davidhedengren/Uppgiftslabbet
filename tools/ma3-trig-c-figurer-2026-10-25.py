"""SVG-hjälpare: geometri och etiketter; uppgifterna skrivs individuellt."""
import math,html
sin=lambda d:math.sin(math.radians(d))
cos=lambda d:math.cos(math.radians(d))
asin=lambda x:math.degrees(math.asin(x))
acos=lambda x:math.degrees(math.acos(x))
def txt(x,y,s,size=18,color='#172e46'):
 return f'<text x="{x:.3f}" y="{y:.3f}" text-anchor="middle" dominant-baseline="middle" font-family="Arial,sans-serif" font-size="{size}" fill="{color}">{html.escape(str(s))}</text>'
def svg(title,body,height=380):
 return f'<span class="fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 {height}" style="width:100%;max-width:520px" role="img" aria-label="{html.escape(title)}"><title>{html.escape(title)}</title><rect width="520" height="{height}" fill="white" rx="10"/>{body}</svg></span>'
def arc(P,U,V,label,r=22):
 u=(U[0]-P[0],U[1]-P[1]);v=(V[0]-P[0],V[1]-P[1]);lu=math.hypot(*u);lv=math.hypot(*v);u=tuple(x/lu for x in u);v=tuple(x/lv for x in v)
 angle=math.degrees(math.acos(max(-1,min(1,sum(a*b for a,b in zip(u,v))))));cross=u[0]*v[1]-u[1]*v[0]
 start=(P[0]+r*u[0],P[1]+r*u[1]);end=(P[0]+r*v[0],P[1]+r*v[1]);d=(u[0]+v[0],u[1]+v[1]);l=math.hypot(*d);distance=max(45,19/max(.15,math.sin(math.radians(angle/2))))
 s=f'<path data-angle-arc="{angle:.9f}" data-center="{P[0]:.6f},{P[1]:.6f}" d="M{start[0]:.6f} {start[1]:.6f} A{r} {r} 0 0 {1 if cross>0 else 0} {end[0]:.6f} {end[1]:.6f}" fill="none" stroke="#087f8c" stroke-width="2"/>'
 return s+txt(P[0]+distance*d[0]/l,P[1]+distance*d[1]/l,label,17,'#087f8c')
def triangle(A,B,a=10,title='Triangel ABC',sides=None,angles=None,altitude=False,bisector=None,extra='',externalB=None,median=False):
 C=180-A-B;assert min(A,B,C)>0
 b=a*sin(B)/sin(A);c=a*sin(C)/sin(A)
 raw=[(0,0),(c,0),(b*cos(A),b*sin(A))]
 xmin=min(x for x,y in raw);xmax=max(x for x,y in raw);ymax=max(y for x,y in raw)
 # Vid trubbig B ligger höjdfoten till höger om basen; skalningen omfattar även foten.
 scale=min(340/(xmax-xmin),210/ymax);cx=(xmin+xmax)/2
 xy=lambda P:(260+(P[0]-cx)*scale,285-P[1]*scale)
 pts=list(map(xy,raw));body='<polygon data-geometry="triangle" data-angles="'+','.join(map(str,[A,B,C]))+'" data-lengths="'+','.join(map(str,[c,a,b]))+'" points="'+' '.join(f'{x:.6f},{y:.6f}' for x,y in pts)+'" fill="#edf6fb" stroke="#096c9a" stroke-width="2.5"/>'
 # Fria hörnnamn ligger utanför vinklarna.
 for i,P in enumerate(pts):
  u=(pts[(i+1)%3][0]-P[0],pts[(i+1)%3][1]-P[1]);v=(pts[(i+2)%3][0]-P[0],pts[(i+2)%3][1]-P[1]);lu=math.hypot(*u);lv=math.hypot(*v);d=(u[0]/lu+v[0]/lv,u[1]/lu+v[1]/lv);ld=math.hypot(*d)
  body+=txt(P[0]-25*d[0]/ld,P[1]-25*d[1]/ld,'ABC'[i],18)
 for key,label in (sides or {}).items():
  i,j={'a':(1,2),'b':(2,0),'c':(0,1)}[key];P,Q=pts[i],pts[j];dx=Q[0]-P[0];dy=Q[1]-P[1];l=math.hypot(dx,dy);off=max(29,4.8*len(str(label))*abs(dy/l)+9*abs(dx/l)+12) if key!='c' else (61 if bisector is not None or median or altitude else 33)
  body+=txt((P[0]+Q[0])/2-dy/l*off,(P[1]+Q[1])/2+dx/l*off,label,18)
 for i,label in (angles or {}).items():body+=arc(pts[i],pts[(i+1)%3],pts[(i+2)%3],label)
 if altitude:
  H=xy((raw[2][0],0));P=pts[2];body+=f'<path data-altitude="true" d="M{P[0]} {P[1]}L{H[0]} {H[1]}" stroke="#a15320" stroke-width="2" stroke-dasharray="6 5" fill="none"/>'
  if H[0]<pts[0][0] or H[0]>pts[1][0]:body+=f'<path d="M{min(H[0],pts[0][0])} {H[1]}H{(H[0]+22 if H[0]>pts[1][0] else pts[1][0])}" stroke="#8796a5" stroke-width="1.5" fill="none"/>'
  body+=f'<path d="M{H[0]+10} {H[1]}v-10h-10" fill="none" stroke="#a15320" stroke-width="1.5"/>'+txt(H[0],H[1]+23,'H',17)
 if bisector is not None:
  if bisector==2:
   D=(c*b/(a+b),0)
  elif bisector==1:
   # AD/DC = AB/BC = c/a.
   D=(raw[2][0]*c/(a+c),raw[2][1]*c/(a+c))
  elif bisector==0:
   D=((raw[1][0]*b+raw[2][0]*c)/(b+c),raw[2][1]*c/(b+c))
  else:raise ValueError('unsupported vertex')
  P=pts[bisector];Q=xy(D);body+=f'<path data-bisector="{bisector}" d="M{P[0]} {P[1]}L{Q[0]} {Q[1]}" stroke="#a15320" stroke-width="2" stroke-dasharray="6 5" fill="none"/>'
  body+=txt(Q[0]+(-22 if bisector==1 else (24 if bisector==0 else 0)),Q[1]+(0 if bisector in [0,1] else 24),'D',17)
 if median:
  P=pts[2];Q=((pts[0][0]+pts[1][0])/2,pts[0][1]);body+=f'<path data-median="true" d="M{P[0]} {P[1]}L{Q[0]} {Q[1]}" stroke="#a15320" stroke-width="2" stroke-dasharray="6 5" fill="none"/>'+txt(Q[0],Q[1]+23,'M',17)
 if externalB:
  P=pts[1];body+=f'<path d="M{P[0]} {P[1]}h75" stroke="#8796a5" stroke-width="1.5" fill="none"/>'+arc(P,(P[0]+75,P[1]),pts[2],externalB)
 if extra:body+=txt(260,365,extra,16)
 return svg(title,body,400 if bisector else 390)
