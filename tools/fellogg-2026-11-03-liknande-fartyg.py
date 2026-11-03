"""Rätta liknande skeva vinklar och längdförhållanden i fartygsfigurer."""
import ast
import json
import re
from pathlib import Path

root=Path(__file__).resolve().parent.parent
module=ast.parse((root/'tools/fellogg-2026-11-03-0915.py').read_text(encoding='utf8'))
ship=next(ast.literal_eval(node.value) for node in module.body if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='ship' for t in node.targets))
forty='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 390 245" role="img" aria-label="Fartyget seglar 18 kilometer österut och sedan 25 kilometer 40 grader norr om öst. En streckad linje förenar start och slut." style="width:100%;max-width:390px"><rect x="1" y="1" width="388" height="243" rx="8" fill="#fff" stroke="#e4e3e6"/><line x1="48" y1="198" x2="183" y2="198" stroke="#2a5d9e" stroke-width="4"/><line x1="183" y1="198" x2="326.63" y2="77.48" stroke="#0f6b4f" stroke-width="4"/><line x1="48" y1="198" x2="326.63" y2="77.48" stroke="#b43123" stroke-width="2" stroke-dasharray="6 4"/><line x1="183" y1="198" x2="238" y2="198" stroke="#64748b" stroke-width="1.5" stroke-dasharray="5 4"/><path d="M213 198 A30 30 0 0 0 205.98 178.72" fill="none" stroke="#2b2527" stroke-width="1.6"/><g font-family="Arial,sans-serif" font-size="14"><text x="101" y="220" fill="#2a5d9e">18 km</text><text x="246" y="164" fill="#0f6b4f">25 km</text><text x="216" y="181" fill="#172b3a">40°</text><text x="241" y="205" fill="#475569">öst</text><text x="34" y="187" fill="#172b3a">start</text><text x="331" y="76" fill="#172b3a">slut</text></g></svg>'''
p=root/'uppgiftermato1.js';source=p.read_text(encoding='utf8');dec=json.JSONDecoder();pos=source.index('[')+1;changes=[];seen=set()
while True:
    while source[pos].isspace() or source[pos]==',':pos+=1
    if source[pos]==']':break
    q,end=dec.raw_decode(source,pos);ident=q.get('id')
    if ident in {'4.108','4.249'}:
        q['t'],n=re.subn(r'<svg\b[\s\S]*?</svg>',lambda _:ship if ident=='4.108' else forty,q['t'],count=1);assert n==1
        if ident=='4.249':
            q['s']='<div class="facit-v2 facit-stegvis"><p class="facit-rubrik"><strong>Bestäm triangelns vinkel</strong></p><p>Vinkeln mellan den fortsatta riktningen österut och den andra sträckan är 40°. Triangelns inre vinkel vid vändpunkten blir därför \\(180^\\circ-40^\\circ=140^\\circ\\).</p><p class="facit-rubrik"><strong>Använd cosinussatsen</strong></p><div class="facit-matte">\\[d^2=18^2+25^2-2\\cdot18\\cdot25\\cos140^\\circ\\]</div><p>Ta den positiva roten för att få avståndet.</p><div class="facit-matte">\\[d\\approx40{,}5\\ \\mathrm{km}\\]</div><p class="facit-svar"><strong>Svar:</strong> Cirka 40,5 km.</p></div>'
        changes.append((pos,end,json.dumps(q,ensure_ascii=False,indent=2).replace('\n','\n  ')));seen.add(ident)
    pos=end
assert seen=={'4.108','4.249'}
for a,b,c in reversed(changes):source=source[:a]+c+source[b:]
json.loads(source[source.index('['):source.rindex(']')+1]);p.write_text(source,encoding='utf8');print('Ändrade:',', '.join(sorted(seen)))
