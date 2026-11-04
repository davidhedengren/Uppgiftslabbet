"""Small, deterministic scientific SVGs for the reviewed battery models."""
from html import escape

def graph(kind):
    w,h=540,370
    x0,x1,y0,y1=65,500,310,42
    xmax=3 if kind=='power' else (4.2 if kind=='short' else 1.8)
    ymax=1.2 if kind=='power' else 1.8
    X=lambda x:x0+(x1-x0)*x/xmax
    Y=lambda y:y0-(y0-y1)*y/ymax
    def text(x,y,s,anchor='middle',color='#20384d'):
        return f'<text x="{x:.2f}" y="{y:.2f}" text-anchor="{anchor}" font-family="Arial,sans-serif" font-size="18" fill="{color}" paint-order="stroke" stroke="white" stroke-width="4" stroke-linejoin="round">{escape(s)}</text>'
    def line(a,b,c,d,color='#d5dee6',dash=''):
        return f'<line x1="{a:.2f}" y1="{b:.2f}" x2="{c:.2f}" y2="{d:.2f}" stroke="{color}" stroke-width="1.5"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'
    caption='Effekten i den yttre resistorn' if kind=='power' else 'Polspänning som funktion av ström'
    s=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{caption}" style="width:100%;max-width:540px"><rect width="540" height="370" fill="white"/>'
    xticks=[.6,1.2,1.8,2.4,3] if kind=='power' else ([1,2,3,4] if kind=='short' else [.3,.6,.9,1.2,1.5,1.8])
    yticks=[.2,.4,.6,.8,1,1.2] if kind=='power' else [.3,.6,.9,1.2,1.5,1.8]
    fmt=lambda n:f'{n:g}'.replace('.',',')
    for x in xticks:s+=line(X(x),y0,X(x),y1)+text(X(x),y0+26,fmt(x))
    for y in yticks:s+=line(x0,Y(y),x1,Y(y))+text(x0-12,Y(y)+6,fmt(y),'end')
    s+=line(x0,y0,x1+8,y0,'#20384d')+line(x0,y0,x0,y1-10,'#20384d')
    s+=text(x0-12,y0+24,'0','end')+text(x0,y1-18,'P (W)' if kind=='power' else 'U (V)','middle')+text(x1,y0+53,'R (Ω)' if kind=='power' else 'I (A)','end')
    f=(lambda x:1.5**2*x/(x+.6)**2) if kind=='power' else (lambda x:1.52-.4*x)
    end=xmax if kind!='short' else 3.8
    points=' '.join(f'{X(end*i/180):.2f},{Y(f(end*i/180)):.2f}' for i in range(181))
    s+=f'<polyline points="{points}" fill="none" stroke="#1464a0" stroke-width="3"/>'
    if kind=='line':
        for x,y in [(0.25,1.42),(.6,1.28),(1.05,1.10),(1.5,.92)]:s+=f'<circle cx="{X(x):.2f}" cy="{Y(y):.2f}" r="5" fill="#bd4b24"/>'
        s+=text(480,70,'Mätpunkter','end','#bd4b24')+text(480,96,'Anpassad linje','end','#1464a0')
    if kind=='power':
        x,y=.6,f(.6)
        s+=line(X(x),y0,X(x),Y(y),'#bd4b24','5 4')+f'<circle cx="{X(x):.2f}" cy="{Y(y):.2f}" r="5" fill="#bd4b24"/>'
        s+=text(X(x)+18,Y(y)-18,'Maximum vid R = 0,60 Ω','start','#bd4b24')
    if kind=='short':
        s+=f'<circle cx="{X(3.8):.2f}" cy="{y0}" r="5" fill="#bd4b24"/>'
        s+=line(X(3.8),y0-70,X(3.8),y0-9,'#bd4b24','5 4')+text(X(3.8)-6,y0-80,'I = 3,8 A','end','#bd4b24')
    return '<span class="fig">'+s+'</svg></span>'
