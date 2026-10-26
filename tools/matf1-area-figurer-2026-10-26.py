"""Koordinatriktiga SVG till sju individuellt valda integraltillämpningar."""
import math
from html import escape
SPECS={
 '3.51':dict(title='Area mellan linje och parabel',xr=(-1.7,2.7),yr=(-.7,5.5),xt=[-1,0,1,2],yt=[0,2,4],curves=[('y = x + 2',lambda x:x+2,'#1463a6'),('y = x²',lambda x:x*x,'#9d3b13')],regions=[(-1,2,lambda x:x+2,lambda x:x*x)]),
 '3.70':dict(title='Område mellan linjen och axlarna',xr=(-.5,3.7),yr=(-1,7),xt=[0,1,2,3],yt=[0,2,4,6],curves=[('y = 6 − 2x',lambda x:6-2*x,'#1463a6')],regions=[(0,3,lambda x:6-2*x,lambda x:0)]),
 '3.80':dict(title='Geometrisk area på båda sidor om x-axeln',xr=(-2.5,2.5),yr=(-1.7,4),xt=[-2,-1,0,1,2],yt=[-1,0,1,2,3],curves=[('y = x² − 1',lambda x:x*x-1,'#1463a6')],regions=[(-2,-1,lambda x:x*x-1,lambda x:0),(-1,1,lambda x:0,lambda x:x*x-1),(1,2,lambda x:x*x-1,lambda x:0)]),
 '3.103':dict(title='Området mellan y = x och y = x²',xr=(-.15,1.3),yr=(-.15,1.5),xt=[0,.5,1],yt=[0,.5,1],curves=[('y = x',lambda x:x,'#1463a6'),('y = x²',lambda x:x*x,'#9d3b13')],regions=[(0,1,lambda x:x,lambda x:x*x)]),
 '3.288':dict(title='Området mellan en rotkurva och en linje',xr=(-.5,5),yr=(-.4,2.9),xt=[0,1,2,3,4],yt=[0,1,2],domain=(0,5),curves=[('y = √x',lambda x:math.sqrt(x),'#1463a6'),('y = x/2',lambda x:x/2,'#9d3b13')],regions=[(0,4,lambda x:math.sqrt(x),lambda x:x/2)]),
 '3.53':dict(title='Den givna integralens område',xr=(-.25,2.5),yr=(-.15,1.3),xt=[0,1,2],yt=[0,.5,1],domain=(0,2.4),curves=[('y = e⁻ˣ²',lambda x:math.exp(-x*x),'#1463a6')],regions=[(0,2,lambda x:math.exp(-x*x),lambda x:0)]),
 '3.350':dict(title='Temperatur under tolv timmar',xr=(-.8,13.7),yr=(0,27),xt=[0,3,6,9,12],yt=[0,10,20,24],domain=(0,12),xlabel='t (h)',ylabel='T (°C)',curves=[('T(t) = 20 + 4 sin(πt/12)',lambda x:20+4*math.sin(math.pi*x/12),'#1463a6')],regions=[]),
}
def figure(id):
 s=SPECS[id];x0,x1=s['xr'];y0,y1=s['yr'];X=lambda x:64+(x-x0)*440/(x1-x0);Y=lambda y:306-(y-y0)*220/(y1-y0)
 line=lambda x,y,u,v,attrs:f'<line x1="{x:.2f}" y1="{y:.2f}" x2="{u:.2f}" y2="{v:.2f}" {attrs}/>'
 text=lambda x,y,t,extra='':f'<text x="{x:.2f}" y="{y:.2f}" fill="#172b43" font-size="15" {extra}>{escape(str(t))}</text>'
 a=[f'<span class="fig" data-review-area="{id}"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 358" role="img" aria-label="{escape(s["title"])}"><title>{escape(s["title"])}</title><rect width="560" height="358" rx="12" fill="white"/>',text(22,25,s['title'])]
 for j,(label,f,color) in enumerate(s['curves']):
  lx=24+j*250;a.extend([line(lx,51,lx+26,51,f'stroke="{color}" stroke-width="3"'),text(lx+34,56,label)])
 for t in s['xt']:a.append(line(X(t),86,X(t),306,'stroke="#d4deea" stroke-width="1"'))
 for t in s['yt']:a.append(line(64,Y(t),504,Y(t),'stroke="#d4deea" stroke-width="1"'))
 def points(f,l,r):return [(X(l+(r-l)*i/160),Y(f(l+(r-l)*i/160))) for i in range(161)]
 for l,r,f,g in s['regions']:
  ps=points(f,l,r)+list(reversed(points(g,l,r)));a.append('<polygon points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y in ps)+'" fill="#cfe8f2" stroke="none"/>')
 a.extend([line(64,Y(0),516,Y(0),'stroke="#172b43" stroke-width="2"'),line(X(0),312,X(0),76,'stroke="#172b43" stroke-width="2"')])
 a.extend([f'<path d="M 510 {Y(0)-4:.2f} L 516 {Y(0):.2f} L 510 {Y(0)+4:.2f}" fill="none" stroke="#172b43" stroke-width="2"/>',f'<path d="M {X(0)-4:.2f} 82 L {X(0):.2f} 76 L {X(0)+4:.2f} 82" fill="none" stroke="#172b43" stroke-width="2"/>'])
 for t in s['xt']:
  a.extend([line(X(t),Y(0)-3,X(t),Y(0)+3,'stroke="#172b43"'),text(X(t),Y(0)+21,str(t).replace('.',','),'text-anchor="middle"')])
 for t in s['yt']:
  if t!=0:a.extend([line(X(0)-3,Y(t),X(0)+3,Y(t),'stroke="#172b43"'),text(X(0)-10,Y(t)+5,str(t).replace('.',','),'text-anchor="end"')])
 a.extend([text(513,Y(0)+29,s.get('xlabel','x'),'text-anchor="end"'),text(X(0)+12,81,s.get('ylabel','y'))])
 # Kurvorna begränsas till ritytan; dataregionerna ligger helt inom den.
 clip='area-clip-'+id.replace('.','-');a.append(f'<defs><clipPath id="{clip}"><rect x="64" y="86" width="440" height="220"/></clipPath></defs>')
 for label,f,color in s['curves']:
  l,r=s.get('domain',(x0,x1));ps=points(f,l,r);a.append(f'<polyline clip-path="url(#{clip})" points="'+ ' '.join(f'{x:.2f},{y:.2f}' for x,y in ps)+f'" fill="none" stroke="{color}" stroke-width="2.7"/>')
 a.append('</svg></span>');return ''.join(a)
