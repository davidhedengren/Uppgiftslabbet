"""Skydda olikhetstecken i uppgiftstext som renderas som HTML."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
for filename, ident in [('uppgifterma2.js', '2.1091'), ('uppgiftermato1.js', '2.1152')]:
    path = ROOT / filename
    source = path.read_text(encoding='utf8')
    decoder = json.JSONDecoder()
    position = source.index('[') + 1
    while True:
        while source[position].isspace() or source[position] == ',':
            position += 1
        if source[position] == ']':
            raise AssertionError((filename, ident))
        q, end = decoder.raw_decode(source, position)
        if q.get('id') == ident:
            break
        position = end
    chunk = source[position:end]
    if filename == 'uppgifterma2.js':
        old = 'För vilka \\(x\\) ligger bågen ovanför marken, alltså \\(h(x)>0\\)?'
        # Frågetexten innehåller JSON-kodade backslashar i originalfilen.
        encoded_old = json.dumps(old, ensure_ascii=False)[1:-1]
        assert chunk.count(encoded_old) == 1
        chunk = chunk.replace(encoded_old, encoded_old + ' Välj ett alternativ.', 1)
        for old, new, expected in [('0<x<4', '0&lt;x&lt;4', 2), ('0<x<2', '0&lt;x&lt;2', 1), ('x<0', 'x&lt;0', 1)]:
            assert chunk.count(old) == expected, (old, chunk.count(old))
            chunk = chunk.replace(old, new)
    else:
        old = 'För 0<x<1 är ln x mindre än 0.'
        assert chunk.count(old) == 1
        chunk = chunk.replace(old, 'För 0 &lt; x &lt; 1 är ln x mindre än 0.', 1)
    assert json.loads(chunk)['id'] == ident
    source = source[:position] + chunk + source[end:]
    json.loads(source[source.index('['):source.rindex(']') + 1])
    path.write_text(source, encoding='utf8')
    print(filename, ident)
