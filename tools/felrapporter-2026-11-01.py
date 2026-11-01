"""Avgränsade ändringar för felloggen den 1 november 2026."""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
def update(filename, edits):
    path = ROOT / filename
    raw = path.read_text(encoding='utf8')
    bank = json.loads(raw[raw.index('['):raw.rindex(']')+1])
    # Top-level decoder finds object boundaries even in compact appended data.
    decoder=json.JSONDecoder(); pos=raw.index('[')+1; replacements=[]; found=set()
    while True:
        while raw[pos].isspace() or raw[pos]==',': pos+=1
        if raw[pos]==']': break
        obj,length=decoder.raw_decode(raw[pos:]); ident=obj.get('id')
        if ident in edits:
            old=json.loads(json.dumps(obj,ensure_ascii=False));edits[ident](obj)
            if old!=obj: replacements.append((pos,pos+length,json.dumps(obj,ensure_ascii=False,separators=(',',':'))))
            found.add(ident)
        pos+=length
    assert found==set(edits),(filename,found,set(edits))
    for start,end,value in reversed(replacements): raw=raw[:start]+value+raw[end:]
    json.loads(raw[raw.index('['):raw.rindex(']')+1])
    path.write_text(raw,encoding='utf8')

def prime(q):
    for key in ('t','s'):
        q[key]=q[key].replace(r'f\prime(2)',r'f^{\prime}(2)')
def axes(q):
    s=q['t']
    for v in ('<path d="M60 280L443 280" fill="none" stroke="#243447" stroke-width="2"/>','<path d="M60 280L60 32" fill="none" stroke="#243447" stroke-width="2"/>'):
        assert v in s;s=s.replace(v,'')
    s=s.replace('<text x="430" y="329" font-family="Arial,sans-serif" font-size="17" text-anchor="end" fill="#243447">x</text>','<text x="440" y="155" font-family="Arial,sans-serif" font-size="17" text-anchor="start" fill="#243447">x</text>')
    s=s.replace('<text x="60" y="23" font-family="Arial,sans-serif" font-size="17" text-anchor="start" fill="#243447">y</text>','<text x="226" y="35" font-family="Arial,sans-serif" font-size="17" text-anchor="start" fill="#243447">y</text>')
    q['t']=s
def histogram(q):
    s=q['t']; piece='<path d="M97.0 42L97.0 280" fill="none" stroke="#243447" stroke-width="2"/>'
    assert piece in s;q['t']=s.replace(piece,'')
def unitcircle(q):
    assert 'currentColor' in q['t'];q['t']=q['t'].replace('currentColor','#243447')
def domain(q):
    q['rättSvar'][1]='x≠2';q['svarFormat'][1]='definitionsmangd_utom'
    q['spelDelar'][0]['s']='<p>Faktorisera täljaren: \\(x^2-4=(x-2)(x+2)\\). För \\(x\\ne2\\) kan vi förkorta med \\(x-2\\).</p><p><strong>Svar:</strong> \\(R(x)=x+2\\).</p>'
    q['spelDelar'][1]['s']='<p>Nämnaren är noll för \\(x=2\\), och uttrycket är definierat för alla andra reella tal.</p><p><strong>Svar:</strong> \\(x\\ne2\\).</p>'
    q['spelDelar'][2]['s']='<p>Sätt in \\(x=3\\) i uttrycket: \\(R(3)=(3^2-4)/(3-2)=5\\).</p><p><strong>Svar:</strong> 5.</p>'
def interval(q):
    q['rättSvar']='[-9,6]';q['svarFormat']='intervall'
def domain98(q):
    q['rättSvar'][1]='x≠3';q['svarFormat'][1]='definitionsmangd_utom'
    q['spelDelar'][0]['s']='<p>Faktorisera täljaren: \\(x^2-9=(x-3)(x+3)\\). För \\(x\\ne3\\) kan vi förkorta med \\(x-3\\).</p><p><strong>Svar:</strong> \\(R(x)=x+3\\).</p>'
    q['spelDelar'][1]['s']='<p>Nämnaren är noll för \\(x=3\\), och uttrycket är definierat för alla andra reella tal.</p><p><strong>Svar:</strong> \\(x\\ne3\\).</p>'
    q['spelDelar'][2]['s']='<p>Sätt in \\(x=5\\) i uttrycket: \\(R(5)=(5^2-9)/(5-3)=8\\).</p><p><strong>Svar:</strong> 8.</p>'
def domainexcluded(q):
    if q['id']=='1.135': q['t']=q['t'].replace('ange fullständig definitionsmängd','ange alla x-värden som inte ingår i definitionsmängden')
    else: q['t']=q['t'].replace('Ange definitionsmängden.','Ange alla x-värden som inte ingår i definitionsmängden.')
def midpoint(q):
    q['t']=q['t'].replace('Bestäm mittpunkten på sträckan mellan','Bestäm mittpunkten på sträckan mellan').replace('</p><div class="fig smal">',' Ange koordinaterna som (x, y).</p><div class="fig smal">',1)
    q['svarFormat']='punkt'
def vectors(q):
    q['t']='<p>Beräkna vektorn \\(-3\\cdot(-2,-4)\\).</p>'
    q['s']=q['s'].replace(r'\begin{pmatrix}6\\12\end{pmatrix}',r'(6,12)')
def leak(q):
    q['spelDelar'][0]['s']='<p>Funktionen växer där derivatan är positiv. Grafen ligger över x-axeln för \\(-2&lt;x&lt;1\\) och för \\(x&gt;4\\).</p><p><strong>Svar:</strong> \\((-2,1)\\) och \\((4,\\infty)\\).</p>'
    q['spelDelar'][1]['s']='<p>Funktionen avtar där derivatan är negativ. Grafen ligger under x-axeln för \\(x&lt;-2\\) och för \\(1&lt;x&lt;4\\).</p><p><strong>Svar:</strong> \\((-\\infty,-2)\\) och \\((1,4)\\).</p>'
def angles(q):
    q['t']=q['t'].replace('Bestäm den vinkel som ger största möjliga tvärsnittsarea och ange även arean.','Bestäm den vinkel i radianer som ger största möjliga tvärsnittsarea och ange även arean.')
    q['s']=q['s'].replace('Vinkeln är cirka \\(68{,}5^\\circ\\) och största arean cirka','Vinkeln är cirka \\(1{,}196\\) rad och största arean cirka')
def carddeck(q):
    q['t']=q['t'].replace('med 52 kort.', 'med 52 kort. Kortleken har fyra färger med 13 kort i varje färg.')
def midpointx(q):
    q['t']=q['t'].replace('Bestäm mittpunkten mellan','Mittpunkten ligger mellan').replace('Ange mittpunktens x-koordinat.','Bestäm mittpunktens x-koordinat.')
def rounding(q):
    q['t']=q['t'].replace('Hur stor är höjdskillnaden mellan linans ändar?','Hur stor är höjdskillnaden mellan linans ändar? Svara med en decimal.')
    q['tolerans']=0.05

if not sys.argv[1:] or 'mato1' in sys.argv: update('uppgiftermato1.js',{'1.66':lambda q:q.update(traningsniva=4),'1.216':lambda q:q.update(traningsniva=5),'1.866':prime,'1.907':axes,'1.895':histogram,'4.470':unitcircle,'1.93':domain,'2.221':interval})
if 'interval' in sys.argv: update('uppgiftermato1.js',{'2.221':interval})
if 'domain' in sys.argv: update('uppgiftermato1.js',{'1.93':domain})
if not sys.argv[1:] or 'domainextra' in sys.argv: update('uppgiftermato1.js',{'1.98':domain98,'1.135':domainexcluded,'1.211':domainexcluded})
if not sys.argv[1:] or 'cirklar' in sys.argv: update('uppgiftermato1.js',{i:unitcircle for i in ('4.429','4.434','4.442','4.465','4.466','4.469','4.471','4.472')})
if not sys.argv[1:] or 'ma1' in sys.argv: update('uppgifterma1.js',{'5.411':carddeck,'4.514':vectors,'4.50':rounding})
if not sys.argv[1:] or 'ma2' in sys.argv: update('uppgifterma2.js',{'3.295':midpointx,'3.263':midpoint})
if not sys.argv[1:] or 'mato2' in sys.argv: update('uppgiftermato2.js',{'2.106':leak,'2.269':angles})
print('De valda bankändringarna har skrivits.')
