"""Åtgärda verifierade fel i Ma1-felloggen 2026-11-04."""
import json, re
from pathlib import Path

p=Path(__file__).resolve().parent.parent/'uppgifterma1.js';source=p.read_text(encoding='utf8');dec=json.JSONDecoder();pos=source.index('[')+1;changes=[];seen=set()
ids={'7.789','7.435','7.434','7.178','7.123','7.147','7.161','7.142','5.607','2.27','2.05'}
def axis(t,xaxis,yaxis,xtick_y):
    # Behåll kurvor och rutnät; flytta etiketterna intill respektive axel.
    svg=re.search(r'<svg\b[\s\S]*?</svg>',t);assert svg
    g=svg.group(0)
    g,n=re.subn(r'(<text x=")55(" y="[\d.]+" text-anchor="end" font-family="sans-serif" font-size="12">)(-?\d+)(</text>)',lambda m:f'{m[1]}{xaxis-10:.3f}{m[2]}{m[3]}{m[4]}',g)
    assert n>=5,n
    if xtick_y is not None:
        g,n=re.subn(r'(<text x="[\d.]+" y=")288(" text-anchor="middle" font-family="sans-serif" font-size="12">)(-?\d+)(</text>)',lambda m:f'{m[1]}{xtick_y:.3f}{m[2]}{m[3]}{m[4]}',g);assert n==10,n
        # Origo får bara en nolla, placerad vid x-axeln.
        g,n=re.subn(r'<text x="'+f'{xaxis-10:.3f}'+r'" y="'+f'{yaxis+4:.3f}'+r'" text-anchor="end" font-family="sans-serif" font-size="12">0</text>','',g);assert n==1,n
        g=g.replace('<text x="435" y="313"','<text x="435" y="213"')
    g=g.replace('<text x="18" y="23"',f'<text x="{xaxis+10:.3f}" y="35"')
    return t[:svg.start()]+g+t[svg.end():]

def edit(q):
    id=q['id']
    if id=='7.789':
        q['t']='<p>En cykel kostar 2 250 kr inklusive 25 % moms. Butiken ger 20 % rabatt på priset.</p><p>Hur många kronor av det rabatterade priset är moms? Svara i kronor.</p>'
    elif id=='7.435':
        q['t']='<p>Gör ett överslag: 6 070 kr ska delas lika på 11 personer. Avrunda till 6 000 kr och 10 personer. Ungefär hur mycket får var och en?</p>'
        q['s']='<div class="facit-v2 facit-stegvis"><p>Avrunda 6 070 kr till 6 000 kr och 11 personer till 10 personer:</p><div class="facit-matte">\\[6\\,000/10=600\\ \\text{kr}.\\]</div><p class="facit-svar"><strong>Svar:</strong> cirka 600 kr per person.</p></div>'
        q['ledtrad']='<p>Dela det avrundade beloppet 6 000 kr mellan 10 personer.</p>';q['rättSvar']=600
    elif id=='7.434':
        assert '100 k r' in q['s'];q['s']=q['s'].replace('100 k r','100\\,\\text{kr}')
    elif id=='7.178':
        q['rättSvar']=25;q['tolerans']=5
        q['s']='<div class="facit-v2 facit-stegvis"><p class="facit-rubrik"><strong>Omvandla och avrunda</strong></p><p>398 km är 39,8 mil. Avrunda exempelvis till 40 mil och 0,6 liter per mil.</p><div class="facit-matte">\\[40\\cdot0{,}6=24\\ \\text{liter}.\\]</div><p>Andra rimliga avrundningar kan ge andra närliggande svar. Som överslag godtas värden från 20 till 30 liter.</p><p class="facit-svar"><strong>Exempel på svar:</strong> cirka 24 liter.</p></div>'
    elif id=='7.123':
        q['t']=q['t'].replace('Hur stor andel av tiden måste flödet ha varit aktivt om givaren är korrekt?', 'Hur stor andel av tiden måste flödet ha varit aktivt om givaren är korrekt? Svara i procent.')
        q['spelDelar'][0]['t']=q['spelDelar'][0]['t'].replace('Hur stor andel av tiden måste flödet ha varit aktivt om givaren är korrekt?', 'Hur stor andel av tiden måste flödet ha varit aktivt om givaren är korrekt? Svara i procent.')
        q['svarEnhet']=['%','L/s'];q['svarFormat']=['numeriskt','numeriskt'];q['rättSvar'][0]=7500/0.85/13200*100
        q['spelDelar'][0]['s']='<div class="facit-v2 facit-stegvis"><p>Omvandla först tiden och volymen: 3 h 40 min = 13 200 s och 7,50 m³ = 7 500 L.</p><p>Den aktiva tiden är</p><div class="facit-matte">\\[7\\,500/0{,}85\\approx8\\,823{,}5\\ \\text{s}.\\]</div><p>Andelen aktiv tid är \\(8\\,823{,}5/13\\,200\\approx0{,}6684\\), alltså ungefär 66,8 %.</p><p class="facit-svar"><strong>Svar:</strong> cirka 66,8 %.</p></div>'
    elif id=='7.147':
        q['t']=q['t'].replace('Efter exakt 5 schemalagda timmar','Efter 5 schemalagda timmar')
        q['rättSvar']=5+1365/306;q['svarEnhet']='h';q['svarFormat']='numeriskt'
    elif id=='7.161':
        q['t']=q['t'].replace('Bestäm koncentrationen.', 'Bestäm koncentrationen. Svara i procent.');q['svarEnhet']='%'
    elif id=='7.142':
        q['t']=q['t'].replace('Mängderna är proportionella.</p>', 'Mängderna är proportionella. Svara i gram.</p>')
        q['rättSvar']=[150,2250,1500];q['svarEnhet']=['g','g','g']
        for d in q['spelDelar']:
            d['t']=d['t'].replace('Mängderna är proportionella.</p>', 'Mängderna är proportionella. Svara i gram.</p>')
            d['ledtrad']='<p>Beräkna först hur många gram som behövs till en portion.</p>'
        for d,n,m in zip(q['spelDelar'],[1,15,10],[150,2250,1500],strict=True):
            detail='En portion kräver \\(900/6=150\\) g.' if n==1 else f'En portion kräver \\\\(900/6=150\\\\) g. Till {n} portioner behövs \\\\(150\\\\cdot{n}={m}\\\\) g.'
            # Bygg med en enda LaTeX-avgränsare i den lagrade strängen.
            detail=detail.replace('\\\\','\\')
            d['s']='<div class="facit-v2 facit-stegvis"><p>'+detail+'</p><p class="facit-svar"><strong>Svar:</strong> '+str(m)+' g.</p></div>'
    elif id=='5.607':
        q['t']=q['t'].replace('Hur många röda kulor fanns i påsen från början?', 'Använd sannolikheterna från båda dragningarna. Hur många röda kulor fanns i påsen från början?')
        q['s']='<div class="facit-v2 facit-stegvis"><p class="facit-rubrik"><strong>Använd sannolikheter från båda dragningarna</strong></p><p>Låt \\(N\\) vara antalet kulor och \\(r\\) antalet röda från början. Av första grenen får vi \\(r/N=5/9\\).</p><p>Efter att en blå kula dragits finns fortfarande \\(r\\) röda kulor, men totalt \\(N-1\\) kulor. Trädet visar då \\(r/(N-1)=5/8\\).</p><p>Därför är \\(r=5N/9=5(N-1)/8\\). Lös ekvationen:</p><div class="facit-matte">\\[8N=9(N-1)\\quad\\Rightarrow\\quad N=9,\\quad r=5.\\]</div><p>Enbart sannolikheten \\(5/9\\) i första dragningen hade inte räckt för att bestämma antalet kulor.</p><p class="facit-svar"><strong>Svar:</strong> 5 röda kulor.</p></div>'
        q['ledtrad']='<p>Använd både sannolikheten för röd kula först och sannolikheten för röd kula efter att en blå dragits.</p>'
    elif id=='2.27':q['t']=axis(q['t'],229.444,222.8,242)
    elif id=='2.05':q['t']=axis(q['t'],188.333,268,None)
    else:raise AssertionError(id)

while True:
    while source[pos].isspace() or source[pos]==',':pos+=1
    if source[pos]==']':break
    q,end=dec.raw_decode(source,pos)
    if q.get('id') in ids:
        edit(q);changes.append((pos,end,json.dumps(q,ensure_ascii=False,indent=2).replace('\n','\n  ')));seen.add(q['id'])
    pos=end
assert seen==ids,(seen,ids)
for a,b,c in reversed(changes):source=source[:a]+c+source[b:]
json.loads(source[source.index('['):source.rindex(']')+1]);p.write_text(source,encoding='utf8');print('Ändrade:',', '.join(sorted(seen)))
