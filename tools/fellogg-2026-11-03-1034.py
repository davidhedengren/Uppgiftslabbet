"""Nivåkalibrera Ma1 1.1311 och förklara hur ekvationen ställs upp."""
import json
from pathlib import Path

p = Path(__file__).resolve().parent.parent / 'uppgifterma1.js'
s = p.read_text(encoding='utf8')
dec = json.JSONDecoder()
pos = s.index('[') + 1
while True:
    while s[pos].isspace() or s[pos] == ',': pos += 1
    assert s[pos] != ']', 'Uppgiften saknas'
    q, end = dec.raw_decode(s, pos)
    if q.get('id') == '1.1311': break
    pos = end
assert q['traningsniva'] == 1 and q['rättSvar'] == -2
chunk = s[pos:end]
solution = ('<div class="facit-v2 facit-stegvis">'
            '<p class="facit-rubrik"><strong>Ställ uttrycken lika</strong></p>'
            '<p>Uttrycken har samma värde när \\(2x+9=5x+15\\).</p>'
            '<p class="facit-rubrik"><strong>Samla termerna</strong></p>'
            '<p>Subtrahera \\(2x\\) och sedan 15 från båda leden:</p>'
            '<div class="facit-matte">\\[9=3x+15\\quad\\Rightarrow\\quad -6=3x.\\]</div>'
            '<p>Dividera båda leden med 3: \\(x=-2\\).</p>'
            '<p>Kontroll: båda uttrycken blir 5 när \\(x=-2\\).</p>'
            '<p class="facit-svar"><strong>Svar:</strong> \\(x=-2\\).</p></div>')
for key, val in [('s', solution), ('traningsniva', 2)]:
    old = '"' + key + '": ' + json.dumps(q[key], ensure_ascii=False)
    new = '"' + key + '": ' + json.dumps(val, ensure_ascii=False)
    assert chunk.count(old) == 1, key
    chunk = chunk.replace(old, new, 1)
assert json.loads(chunk)['id'] == '1.1311'
s = s[:pos] + chunk + s[end:]
json.loads(s[s.index('['):s.rindex(']')+1])
p.write_text(s, encoding='utf8')
print('Ma1 1.1311: nivå 2 och förtydligat facit')
