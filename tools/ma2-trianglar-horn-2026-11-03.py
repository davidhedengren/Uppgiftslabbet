"""Märk motsvarande hörn i två likformighetsfigurer."""
import json
from pathlib import Path

path=Path(__file__).resolve().parent.parent/'uppgifterma2.js';source=path.read_text(encoding='utf8');dec=json.JSONDecoder();pos=source.index('[')+1;changes=[];seen=set()
labels={
 '3.692':[('B',16,207),('A',183,207),('C',137,60),('Q',206,207),('P',403,207),('R',348,36)],
 '3.695':[('A',70,107),('B',28,231),('C',168,231),('X',258,54),('Y',197,231),('Z',412,231)],
}
while True:
    while source[pos].isspace() or source[pos]==',':pos+=1
    if source[pos]==']':break
    q,end=dec.raw_decode(source,pos);ident=q.get('id')
    if ident in labels:
        texts=''.join(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="16" font-style="italic" text-anchor="middle" fill="#172b3a">{name}</text>' for name,x,y in labels[ident])
        assert q['t'].count('</svg>')==1
        t=q['t'].replace('</svg>',texts+'</svg>')
        if ident=='3.695':
            old='Vilken sida i \\(XYZ\\) motsvarar sidan \\(BC\\)?'
            assert old in t;t=t.replace(old,old+' Välj ett alternativ.',1)
        chunk=source[pos:end];old='"t": '+json.dumps(q['t'],ensure_ascii=False);assert chunk.count(old)==1;chunk=chunk.replace(old,'"t": '+json.dumps(t,ensure_ascii=False),1);assert json.loads(chunk)['id']==ident
        changes.append((pos,end,chunk));seen.add(ident)
    pos=end
assert seen==set(labels)
for a,b,c in reversed(changes):source=source[:a]+c+source[b:]
json.loads(source[source.index('['):source.rindex(']')+1]);path.write_text(source,encoding='utf8');print('Ändrade:',', '.join(sorted(seen)))
