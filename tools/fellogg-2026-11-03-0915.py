"""Åtgärda verifierade fel och otydligheter i felloggen 2026-11-03 09:15."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

triangles = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 250" role="img" aria-label="Två likformiga trianglar ABC och DEF. AB är 6 centimeter, AC 8 centimeter, DE 9 centimeter och DF är obekant." style="width:100%;max-width:480px"><rect x="1" y="1" width="478" height="248" rx="10" fill="#fff" stroke="#dce4ed"/><g fill="#d9ecf2" fill-opacity=".35" stroke="#172b3a" stroke-width="2.4" stroke-linejoin="round"><polygon points="50,220 140,220 80,103.8105"/><polygon points="220,220 355,220 265,45.7158"/></g><g font-family="Arial,sans-serif" font-size="17" fill="#172b3a" font-style="italic"><text x="32" y="233">A</text><text x="143" y="233">B</text><text x="76" y="94">C</text><text x="202" y="233">D</text><text x="359" y="233">E</text><text x="260" y="36">F</text></g><g font-family="Arial,sans-serif" font-size="17" fill="#216d87" font-weight="bold" text-anchor="middle"><text x="95" y="213">6</text><text x="48" y="160">8</text><text x="287.5" y="213">9</text><text x="218" y="132">?</text></g></svg>'''
ship = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 390 245" role="img" aria-label="Fartyget seglar 18 kilometer österut, sedan 25 kilometer 60 grader norr om öst. En streckad linje förenar start och slut." style="width:100%;max-width:390px"><rect x="1" y="1" width="388" height="243" rx="8" fill="#fff" stroke="#e4e3e6"/><line x1="48" y1="198" x2="183" y2="198" stroke="#2a5d9e" stroke-width="4"/><line x1="183" y1="198" x2="276.75" y2="35.62" stroke="#0f6b4f" stroke-width="4"/><line x1="48" y1="198" x2="276.75" y2="35.62" stroke="#b43123" stroke-width="2" stroke-dasharray="6 4"/><line x1="183" y1="198" x2="238" y2="198" stroke="#64748b" stroke-width="1.5" stroke-dasharray="5 4"/><path d="M213 198 A30 30 0 0 0 198 172.02" fill="none" stroke="#2b2527" stroke-width="1.6"/><g font-family="Arial,sans-serif" font-size="14"><text x="101" y="220" fill="#2a5d9e">18 km</text><text x="241" y="108" fill="#0f6b4f">25 km</text><text x="215" y="176" fill="#172b3a">60°</text><text x="241" y="205" fill="#475569">öst</text><text x="34" y="187" fill="#172b3a">start</text><text x="282" y="36" fill="#172b3a">slut</text></g></svg>'''

solutions = [
    '<p>Derivera varje term för sig: derivatan av \\(\\sin x\\) är \\(\\cos x\\), och derivatan av \\(\\cos x\\) är \\(-\\sin x\\).</p><p class="facit-svar"><strong>Svar:</strong> \\(f\'(x)=4\\cos x+3\\sin x\\).</p>',
    '<p>Skriv först \\(\\tan x=\\dfrac{\\sin x}{\\cos x}\\). Med kvotregeln får vi</p><div class="facit-matte">\\[g\'(x)=\\frac{\\cos x\\cdot\\cos x-\\sin x\\cdot(-\\sin x)}{\\cos^2 x}=\\frac{\\cos^2x+\\sin^2x}{\\cos^2x}.\\]</div><p>Eftersom \\(\\cos^2x+\\sin^2x=1\\) förenklas täljaren till 1. Här krävs \\(\\cos x\\ne0\\), precis som för tangens.</p><p class="facit-svar"><strong>Svar:</strong> \\(g\'(x)=\\dfrac{1}{\\cos^2x}\\).</p>',
    '<p>Använd kedjeregeln. Den inre funktionen \\(2x\\) har derivatan 2 och derivatan av cosinus är minus sinus.</p><div class="facit-matte">\\[h\'(x)=5\\cdot(-\\sin(2x))\\cdot2=-10\\sin(2x).\\]</div><p class="facit-svar"><strong>Svar:</strong> \\(h\'(x)=-10\\sin(2x)\\).</p>',
    '<p>Använd kedjeregeln för båda termerna: derivatorna av de inre funktionerna är 3 respektive 4.</p><div class="facit-matte">\\[p\'(x)=2\\cdot3\\cos(3x)+4\\sin(4x)=6\\cos(3x)+4\\sin(4x).\\]</div><p class="facit-svar"><strong>Svar:</strong> \\(p\'(x)=6\\cos(3x)+4\\sin(4x)\\).</p>',
]
solutions = ['<div class="facit-v2 facit-stegvis">'+s+'</div>' for s in solutions]

def alter(q, file):
    ident = q['id']
    if file == 'uppgifterma2.js' and ident == '3.691':
        q['t'], n = re.subn(r'<svg\b[\s\S]*?</svg>', lambda _: triangles, q['t'], count=1); assert n == 1
    elif file == 'uppgifterma2.js' and ident == '4.514':
        marks = ''.join(f'<line x1="{30+380*i/35:.1f}" y1="110" x2="{30+380*i/35:.1f}" y2="114" stroke="#475569" stroke-width="1"/>' for i in range(1,35) if i % 5)
        guide = '<line x1="203.7" y1="82" x2="203.7" y2="110" stroke="#c2410c" stroke-width="1.3" stroke-dasharray="3 3"/>'
        anchor = '<line x1="30.0" y1="110.0" x2="410.0" y2="110.0"'
        assert q['t'].count(anchor)==1
        q['t'] = q['t'].replace(anchor, guide + marks + anchor).replace('font-size="13"', 'font-size="16"')
    elif file == 'uppgifterma2.js' and ident == '6.10':
        q['ledtrad'] = '<p>Hur långt från medelvärdet ligger gränserna? I en normalfördelning ligger ungefär 68 % inom en standardavvikelse från medelvärdet.</p>'
        q['s'] = '<div class="facit-v2 facit-stegvis"><p class="facit-rubrik"><strong>Jämför gränserna med standardavvikelsen</strong></p><p>56 = 60 − 4 och 64 = 60 + 4. Intervallet sträcker sig alltså en standardavvikelse åt vardera hållet från medelvärdet.</p><p>I en normalfördelning ligger ungefär 68 % inom en standardavvikelse från medelvärdet. Regeln kan användas här utan grafritare.</p><p class="facit-svar"><strong>Svar:</strong> Ungefär 68 %.</p></div>'
    elif file == 'uppgifterma2.js' and ident == '3.2064':
        old = 'Hur många grader svänger bilisten i \\(C\\)? (Svara i grader.)'
        new = 'Hur många grader svänger bilisten i \\(C\\)? Med svängen menas vinkeln mellan riktningen rakt fram och vägen mot \\(B\\). Svara i grader.'
        assert old in q['t']; q['t'] = q['t'].replace(old,new)
    elif file == 'uppgifterma1.js' and ident == '5.554':
        q['t'] = q['t'].replace('Ungefär hur stor blir felmarginalen med 4 000 personer?', 'Ungefär hur stor blir felmarginalen med 4 000 personer? Svara i procentenheter.')
        q['s'] = '<div class="facit-v2 facit-stegvis"><p class="facit-rubrik"><strong>Jämför stickprovens storlek</strong></p><p>4 000 är fyra gånger så många som 1 000. Roten ur 4 är 2, så felmarginalen halveras.</p><div class="facit-matte">\\[3/2=1{,}5\\]</div><p class="facit-svar"><strong>Svar:</strong> 1,5 procentenheter.</p></div>'
        q['ledtrad'] = '<p>Hur många gånger större är stickprovet? Hur påverkas felmarginalen av roten ur den faktorn?</p>'
    elif file == 'uppgifterma1.js' and ident == '5.97':
        q['t'] = q['t'].replace('Avgör om påståendena är rimliga.', 'Avgör om påståendena är sanna eller falska.')
        explanations = ['Inte signifikant betyder inte att grupperna måste vara exakt lika; undersökningen kan vara för osäker för att påvisa en verklig skillnad.', 'En skillnad kan vara liten men ändå statistiskt signifikant om den statistiska osäkerheten är tillräckligt liten.']
        for i, d in enumerate(q['spelDelar']):
            d['t'] = d['t'].replace('Avgör om påståendena är rimliga.', 'Är påståendet sant eller falskt? Välj ett alternativ.')
            d['s'] = '<div class="facit-v2 facit-stegvis"><p>'+explanations[i]+'</p><p class="facit-svar"><strong>Svar:</strong> '+('Falskt' if i==0 else 'Sant')+'.</p></div>'
            d['alternativ'] = [{'txt':'Sant','ratt':i==1,'kommentar':explanations[i]}, {'txt':'Falskt','ratt':i==0,'kommentar':explanations[i]}]
        q['s'] = '<div class="facit-v2 facit-stegvis"><p><strong>a) Falskt.</strong> '+explanations[0]+'</p><p><strong>b) Sant.</strong> '+explanations[1]+'</p></div>'
    elif file == 'uppgiftermato1.js' and ident == '4.23':
        q['t'], n = re.subn(r'<svg\b[\s\S]*?</svg>', lambda _: ship, q['t'], count=1); assert n == 1
    elif file == 'uppgiftermato1.js' and ident == '4.274':
        q['rättSvar'] = 1066.5348094534763
        q['s'] = '<div class="facit-v2 facit-stegvis"><p class="facit-rubrik"><strong>Använd areasatsen</strong></p><p>Två sidor och vinkeln mellan dem är kända, så \\(T=ab\\sin C/2\\).</p><div class="facit-matte">\\[T=\\frac{42\\cdot57\\cdot\\sin63^\\circ}{2}\\approx1066{,}5348\\ \\mathrm{m}^2.\\]</div><p class="facit-svar"><strong>Svar:</strong> cirka 1 066,5 m².</p></div>'
    elif file == 'uppgiftermato1.js' and ident == '4.548':
        q['traningsniva'] = 4
    elif file == 'uppgiftermato2.js' and ident == '2.17':
        q['s'] = '<div class="facit-v2 facit-stegvis">'+''.join('<p><strong>'+chr(97+i)+')</strong></p>'+s for i,s in enumerate(solutions))+'</div>'
        q['ledtrad'] = '<p>Derivera sinus och cosinus termvis. För tangens kan du skriva tan x = sin x / cos x och använda kvotregeln; använd kedjeregeln när vinkeln innehåller en faktor.</p>'
        for d,s in zip(q['spelDelar'],solutions,strict=True): d['s']=s
    else: raise AssertionError((file,ident))

targets={'uppgifterma2.js':{'3.691','4.514','6.10','3.2064'},'uppgifterma1.js':{'5.554','5.97'},'uppgiftermato1.js':{'4.23','4.274','4.548'},'uppgiftermato2.js':{'2.17'}}
for file, ids in targets.items():
    p=ROOT/file; source=p.read_text(encoding='utf8'); dec=json.JSONDecoder(); position=source.index('[')+1; changes=[]; seen=set()
    while True:
        while source[position].isspace() or source[position]==',': position+=1
        if source[position]==']': break
        q,end=dec.raw_decode(source,position)
        if q.get('id') in ids:
            alter(q,file); encoded=json.dumps(q,ensure_ascii=False,indent=2).replace('\n','\n  ');changes.append((position,end,encoded));seen.add(q['id'])
        position=end
    assert seen==ids,(file,seen,ids)
    for a,b,c in reversed(changes):source=source[:a]+c+source[b:]
    json.loads(source[source.index('['):source.rindex(']')+1]);p.write_text(source,encoding='utf8');print(file,', '.join(sorted(seen)))
