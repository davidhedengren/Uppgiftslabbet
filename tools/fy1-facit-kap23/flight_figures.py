"""Handritade flygplansfigurer för felloggen 2026-11-04, inga ändrade svar."""
import re
from render import byid, save

# En sidovy: svepta vingar och stjärtplan, rundad nos, motor och landningsställ.
AIRCRAFT='''<g data-figure="aircraft-side-profile" stroke="#24374b" stroke-width="1.8" stroke-linejoin="round">
<path d="M80 100 L44 20 Q43 16 48 16 L64 16 Q68 16 70 20 L127 101 Z" fill="#245b85"/>
<path d="M64 28 L94 78 L81 77 L56 28 Z" fill="#70b5d6" stroke="none"/>
<path d="M205 103 L161 70 L177 69 L263 104 Z" fill="#c2d5e1"/>
<path d="M39 100 Q52 91 77 91 L302 91 Q335 91 352 99 Q372 106 383 119 Q386 124 377 127 Q341 138 293 140 L123 140 Q79 140 50 121 L30 107 Q26 103 39 100 Z" fill="#f7fafc"/>
<path d="M57 120 Q87 134 126 134 L293 134 Q344 134 377 125 Q353 139 293 140 L123 140 Q79 140 57 126 Z" fill="#c2d5e1" stroke="none"/>
<path d="M81 119 L302 119 Q348 119 373 121" fill="none" stroke="#3986ad" stroke-width="3"/>
<path d="M334 98 Q347 100 354 104 L367 114 L347 113 Z" fill="#24374b"/>
<path d="M330 98 L337 113 L321 112 L318 98 Z" fill="#24374b"/>
<rect x="103" y="98" width="11" height="30" rx="3" fill="none" stroke="#738b9b" stroke-width="1"/>
<rect x="292" y="98" width="11" height="30" rx="3" fill="none" stroke="#738b9b" stroke-width="1"/>
'''+''.join(f'<rect x="{x}" y="103" width="7" height="8" rx="3" fill="#304e67" stroke="none"/>' for x in range(124,285,15))+'''
<path d="M187 137 L187 165 M181 166 L195 166 M337 134 L337 166 M337 157 L327 148" fill="none" stroke-width="3"/>
<g fill="#24374b"><circle cx="182" cy="171" r="7"/><circle cx="195" cy="171" r="7"/><circle cx="337" cy="171" r="7"/></g>
<g fill="#a4b8c6" stroke="none"><circle cx="182" cy="171" r="2.5"/><circle cx="195" cy="171" r="2.5"/><circle cx="337" cy="171" r="2.5"/></g>
<path d="M214 128 L233 153 L249 153 L247 126" fill="#a7bfce"/>
<path d="M220 148 Q212 149 211 158 Q210 169 220 171 L255 170 Q264 166 263 156 Q261 148 254 147 Z" fill="#d3e2eb"/>
<ellipse cx="256" cy="159" rx="7" ry="11" fill="#59758a"/><ellipse cx="258" cy="159" rx="3.8" ry="7" fill="#24374b" stroke="none"/>
<path d="M204 121 L126 158 Q125 160 130 160 L157 160 L270 125 Z" fill="#dae7ee"/>
<path d="M144 154 L241 126" fill="none" stroke="#8faaba" stroke-width="1"/>
<path d="M74 107 L24 128 L44 132 L121 112 Z" fill="#bed4e2"/>
</g>'''

def scene(distance=None,acc=None,speed=None):
    labels=['Flygplan på en rak startbana, sett från sidan']
    if distance: labels.append('sträcka '+distance+' meter')
    if acc: labels.append('acceleration '+acc+' meter per sekundkvadrat')
    if speed: labels.append('lyftfart '+speed+' meter per sekund')
    title='. '.join(labels)+'.'
    s=f'<svg xmlns="http://www.w3.org/2000/svg" width="720" height="330" viewBox="0 0 720 330" style="display:block;width:720px;max-width:100%;height:auto;margin:12px auto;background:#fff;border-radius:10px" role="img" aria-label="{title}"><title>{title}</title>'
    s+='<rect x="1" y="1" width="718" height="328" rx="10" fill="#f4f9fc" stroke="#ccdbe5"/>'
    s+='<path d="M26 242 H694 V273 H26 Z" fill="#dce5eb"/><path d="M26 242 H694" stroke="#354b5e" stroke-width="2"/><path d="M36 260 H684" stroke="#fff" stroke-width="3" stroke-dasharray="28 22"/>'
    s+='<g transform="translate(180 64)">'+AIRCRAFT+'</g>'
    s+='<g font-family="Arial,sans-serif" font-size="21" fill="#172e43">'
    if acc:s+=f'<text x="394" y="38" text-anchor="middle">a = {acc} m/s²</text><path d="M308 53 H470 M460 47 L472 53 L460 59" fill="none" stroke="#245b85" stroke-width="2.5"/>'
    else:s+='<text x="394" y="38" text-anchor="middle">Rörelseriktning</text><path d="M308 53 H470 M460 47 L472 53 L460 59" fill="none" stroke="#245b85" stroke-width="2.5"/>'
    if speed:s+=f'<text x="602" y="109" text-anchor="middle">{speed} m/s</text><path d="M560 126 H645 M636 120 L648 126 L636 132" fill="none" stroke="#245b85" stroke-width="2.5"/>'
    s+='<text x="80" y="200" text-anchor="middle">Start</text><text x="80" y="228" text-anchor="middle">v₀ = 0</text>'
    if distance:s+=f'<path d="M80 278 V304 M652 278 V304 M80 291 H652" fill="none" stroke="#5c7081" stroke-width="1.5"/><text x="366" y="319" text-anchor="middle">{distance} m</text>'
    else:s+='<text x="366" y="310" text-anchor="middle">Startbana</text>'
    return s+'</g></svg>'

def replace_svg(text,svg):
    if '<svg' in text:return re.sub(r'<svg\b[\s\S]*?</svg>',lambda m:svg,text)
    pos=text.index('</p>')+4
    return text[:pos]+svg+text[pos:]

q=byid['3.73']
for key in ['t','spelIntro']:q[key]=replace_svg(q[key],scene('800',acc='2,5'))
for d,fig in zip(q['spelDelar'],[scene(acc='2,5',speed='65'),scene(acc='2,5',speed='65'),scene('800',acc='2,5'),scene('800',speed='65')]):d['t']=replace_svg(d['t'],fig)
q=byid['3.93']
for key in ['t','spelIntro']:q[key]=replace_svg(q[key],scene('1156',speed='68')).replace('och rullar 1156 m','och rullar 1156 m med konstant acceleration').replace('och rullar med konstant acceleration 1156 m','och rullar 1156 m med konstant acceleration')
for d,fig in zip(q['spelDelar'],[scene('1156',speed='68'),scene(acc='2,0',speed='68'),scene(acc='2,0',speed='78')]):
    d['t']=replace_svg(d['t'],fig).replace('och rullar 1156 m','och rullar 1156 m med konstant acceleration').replace('och rullar med konstant acceleration 1156 m','och rullar 1156 m med konstant acceleration').replace('accelererar med 2,0','accelererar med konstant acceleration 2,0')
q=byid['3.88']
def fix(value):
    if isinstance(value,str):return value.replace('Räkna med konstant acceleration. Räkna med konstant acceleration.', 'Räkna med konstant acceleration.').replace('M163 140 L174 132 L189 132 L181 140 L189 148 L174 148 Z','M189 140 L178 132 L163 132 L171 140 L163 148 L178 148 Z').replace('Pilen startar från vila och lämnar bågen med farten 55 m/s.','Pilen startar från vila och lämnar bågen med farten 55 m/s. Räkna med konstant acceleration.').replace('Räkna med konstant acceleration. Räkna med konstant acceleration.', 'Räkna med konstant acceleration.')
    if isinstance(value,list):return [fix(x) for x in value]
    if isinstance(value,dict):return {k:fix(v) for k,v in value.items()}
    return value
q.update(fix(q))
save()
