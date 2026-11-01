"""Skriv avgränsade delfacit utan att ändra heluppgiftens facit."""
from pathlib import Path
import json,re

ROOT=Path(__file__).resolve().parent.parent
facit={
'uppgiftermato2.js':{
 '2.117':{0:r"""<div class="facit-v2"><p>Produktregeln ger \(f'(x)=ae^x+(ax+b)e^x\). För \(x=0\) är alltså \(f'(0)=a+b\), medan \(f(0)=b\).</p><p>Subtrahera de givna funktionsvärdena:</p>\[a=f'(0)-f(0)=5-2=3.\]<p><strong>Svar:</strong> \(a=3\).</p></div>"""},
 '2.229':{0:r"""<div class="facit-v2"><p>Villkoret \(f(1)=4\) ger \(a+b=8\). Med kvotregeln får vi \(f'(x)=(a-b)/(x+1)^2\), så \(f'(1)=3\) ger \(a-b=12\).</p><p>Addera de två ekvationerna:</p>\[2a=8+12=20.\]<p><strong>Svar:</strong> \(a=10\).</p></div>"""},
 '2.101':{0:r"""<div class="facit-v2"><p>Skriv \(h(x)=(1+x^2)^{1/2}\). Kedjeregeln ger</p>\[h'(x)=\frac12(1+x^2)^{-1/2}\cdot2x=\frac{x}{\sqrt{1+x^2}}.\]<p><strong>Svar:</strong> \(h'(x)=\dfrac{x}{\sqrt{1+x^2}}\).</p></div>"""},
 '2.42':{0:r"""<div class="facit-v2"><p>Funktionen växer där grafen för derivatan ligger över x-axeln och avtar där den ligger under.</p><p>Grafen ligger över axeln för \(x&lt;-1\) och \(x&gt;2\), och under axeln för \(-1&lt;x&lt;2\).</p><p><strong>Svar:</strong> Växande på \((-\infty,-1)\) och \((2,\infty)\); avtagande på \((-1,2)\).</p></div>"""},
 '2.77':{0:r"""<div class="facit-v2"><p>Funktionen växer där grafen för derivatan ligger över x-axeln och avtar där den ligger under.</p><p>Grafen ligger över axeln för \(x&lt;-1\) och \(x&gt;3\), och under axeln för \(-1&lt;x&lt;3\).</p><p><strong>Svar:</strong> Växande på \((-\infty,-1)\) och \((3,\infty)\); avtagande på \((-1,3)\).</p></div>"""},
 '2.158':{
  0:r"""<div class="facit-v2"><p>Derivera en gång och sedan en gång till:</p>\[f'(x)=4x^3-8x,\qquad f''(x)=12x^2-8.\]<p><strong>Svar:</strong> \(f''(x)=12x^2-8\).</p></div>""",
  1:r"""<div class="facit-v2"><p>Andraderivatan är \(f''(x)=12x^2-8\). Den är positiv när \(12x^2&gt;8\), alltså när \(x^2&gt;2/3\), och negativ när \(x^2&lt;2/3\).</p><p><strong>Svar:</strong> \(f''(x)&gt;0\) för \(|x|&gt;\sqrt{2/3}\) och \(f''(x)&lt;0\) för \(|x|&lt;\sqrt{2/3}\).</p></div>"""},
 '2.253':{
  0:r"""<div class="facit-v2"><p>Derivatan \((x-1)(x-4)\) är positiv när båda faktorerna har samma tecken. Det gäller när båda är negativa eller båda positiva.</p><p><strong>Svar:</strong> \(f\) växer för \(x&lt;1\) och för \(x&gt;4\).</p></div>""",
  1:r"""<div class="facit-v2"><p>Derivatan är noll när någon faktor är noll:</p>\[(x-1)(x-4)=0\quad\Rightarrow\quad x=1\ \text{eller}\ x=4.\]<p>Derivatan byter tecken vid båda värdena, så båda ger extrempunkter.</p><p><strong>Svar:</strong> \(x=1\) och \(x=4\).</p></div>"""},
 '3.113':{0:r"""<div class="facit-v2"><p>Ett tvärsnitt vinkelrätt mot x-axeln blir en cirkelskiva med radien \(r=x^2\). Tvärsnittsarean är därför \(\pi r^2=\pi x^4\).</p><p><strong>Svar:</strong> \(V=\pi\displaystyle\int_0^3 x^4\,dx\).</p></div>"""},
 '4.04':{0:r"""<div class="facit-v2"><p>Vid multiplikation multipliceras absolutbeloppen och argumenten adderas. Här är beloppet \(2\cdot3=6\) och argumentet \(30^\circ+(-45^\circ)=-15^\circ\).</p><p><strong>Svar:</strong> \(z_1z_2=6(\cos(-15^\circ)+i\sin(-15^\circ))\).</p></div>"""},
 '4.327':{0:r"""<div class="facit-v2"><p>Ekvationen har sex rötter med samma absolutbelopp. Deras argument är jämnt fördelade med ett vinkelsteg på \(2\pi/6=\pi/3\), så punkterna ligger jämnt fördelade på en cirkel.</p><p><strong>Svar:</strong> En regelbunden sexhörning.</p></div>"""},
},
'uppgifterma2.js':{
 '1.313':{0:r"""<div class="facit-v2"><p>Låt en tom låda väga \(l\) kg och en bok \(b\) kg. Vägningarna ger \(3l+24b=15\) och \(5l+40b=25\). Båda förenklas till samma villkor \(l+8b=5\), så de bestämmer inte vikterna entydigt.</p><p>Två möjliga par \((l,b)\) är \((1{,}8;0{,}4)\) och \((2{,}6;0{,}3)\). Båda uppfyller villkoret och har positiva vikter.</p><p><strong>Svar:</strong> Nej, vägningarna räcker inte.</p></div>"""},
 '3.462':{1:r"""<div class="facit-v2"><p>Pythagoras sats ger \((a-d)^2+a^2=(a+d)^2\), vilket förenklas till \(a=4d\). Hypotenusan är då \(a+d=5d\).</p><p>Omkretsen är \((a-d)+a+(a+d)=3a=12d\). Eftersom den är 36 cm får vi \(d=3\) cm.</p><p><strong>Svar:</strong> Hypotenusan är \(5d=15\) cm.</p></div>"""},
},
'uppgifter.js':{
 '3.80':{1:r"""<div class="facit-v2"><p>Vid konstant acceleration från vila är sträckan arean av en triangel i hastighetsdiagrammet:</p>\[s=\frac{vt}{2}.\]<p>Lös ut slutfarten och sätt in värdena:</p>\[v=\frac{2s}{t}=\frac{2\cdot24}{4}=12\,\mathrm{m/s}.\]<p><strong>Svar:</strong> 12 m/s.</p></div>"""},
}}

def spans(raw):
    decoder=json.JSONDecoder();pos=raw.index('[')+1
    while True:
        while raw[pos].isspace() or raw[pos]==',':pos+=1
        if raw[pos]==']':break
        obj,end=decoder.raw_decode(raw,pos);yield obj,pos,end;pos=end

for filename,edits in facit.items():
    p=ROOT/filename;raw=p.read_text(encoding='utf8');changes=[];found=set()
    for q,start,end in spans(raw):
        if q.get('id') not in edits:continue
        part_edits=edits[q['id']];obj=raw[start:end]
        match=re.search(r'"spelDelar"\s*:\s*\[',obj);assert match,q['id']
        pos=match.end();dec=json.JSONDecoder();parts=[]
        while True:
            while obj[pos].isspace() or obj[pos]==',':pos+=1
            if obj[pos]==']':break
            d,e=dec.raw_decode(obj,pos);parts.append((d,pos,e));pos=e
        for idx,new in sorted(part_edits.items(),reverse=True):
            if filename!='uppgifter.js':
                rubrik={'2.117':'Jämför funktionsvärdet och derivatan','2.229':'Lös ut den sökta parametern',
                        '2.101':'Använd kedjeregeln','2.42':'Läs derivatans tecken','2.77':'Läs derivatans tecken',
                        '2.158':'Undersök andraderivatan','2.253':'Undersök derivatans tecken',
                        '3.113':'Ställ upp volymintegralen','4.04':'Multiplicera belopp och addera argument',
                        '4.327':'Undersök rötternas placering','1.313':'Jämför vägningarna',
                        '3.462':'Använd Pythagoras sats och omkretsen'}[q['id']]
                new=new.replace('<div class="facit-v2">','<div class="facit-v2 facit-stegvis"><p class="facit-rubrik"><strong>'+rubrik+'</strong></p>',1)
            d,a,b=parts[idx];seg=obj[a:b];m=re.search(r'"s"\s*:\s*',seg);assert m,(q['id'],idx)
            value_end=dec.raw_decode(seg,m.end())[1]
            seg=seg[:m.end()]+json.dumps(new,ensure_ascii=False)+seg[value_end:]
            obj=obj[:a]+seg+obj[b:]
        changes.append((start,end,obj));found.add(q['id'])
    assert found==set(edits),(filename,found,set(edits))
    for start,end,new in reversed(changes):raw=raw[:start]+new+raw[end:]
    json.loads(raw[raw.index('['):raw.rindex(']')+1]);p.write_text(raw,encoding='utf8')
    print(filename,', '.join(sorted(found)))
