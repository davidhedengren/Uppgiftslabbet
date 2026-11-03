"""Rätta facit om skalning och förtydliga två korrelationsuppgifter."""
import json
import re
from pathlib import Path

path = Path(__file__).resolve().parent.parent / 'uppgifterma1.js'
source = path.read_text(encoding='utf8')
decoder = json.JSONDecoder()
position = source.index('[') + 1
changes = []
seen = set()
updates = {
    '5.197': {
        't': '<p>Ett punktmoln har en tydligt stigande trend, men punkterna ligger inte alla på en rät linje. En elev säger: ”Eftersom punkterna är utspridda finns ingen korrelation.” Vilken bedömning är bäst? Välj ett alternativ.</p>',
        's': '<div class="facit-v2 facit-stegvis"><p class="facit-rubrik"><strong>Skilj på riktning och styrka</strong></p><p>Den stigande trenden visar positiv korrelation. Korrelation kan finnas även om punkterna inte ligger exakt på en rät linje.</p><p>Eftersom punkterna inte alla ligger på en rät linje är sambandet inte perfekt linjärt.</p><p class="facit-svar"><strong>Svar:</strong> Trenden visar positiv korrelation, men sambandet är inte perfekt linjärt.</p></div>',
        'ledtrad': '<p>Vad säger den stigande trenden om riktningen? Måste alla punkter ligga på en rät linje för att det ska finnas korrelation?</p>',
        'correct': 'Trenden visar positiv korrelation, men sambandet är inte perfekt linjärt.',
        'comments': ['Korrelation kan finnas även om punkterna är utspridda kring en trend.', 'Ett perfekt linjärt samband kräver att alla punkter ligger på en rät linje.', 'Den stigande trenden visar positiv, inte negativ, korrelation.', None]},
    '5.678': {
        'replace': [('har korrelationskoefficienterna 0,97, −0,75 och 0,02, men i blandad ordning.', 'har korrelationskoefficienterna 0,97, −0,75 och 0,02 avrundade till två decimaler, men i blandad ordning.'), ('Vilken parning stämmer?', 'Vilken parning stämmer? Välj ett alternativ.'), ('font-size=\\"15\\"', 'font-size=\\"20\\"')],
        's_replace': [('ingen trend alls', 'ingen tydlig linjär trend'), ('ingen stigande eller fallande trend', 'ingen tydlig stigande eller fallande trend')],
        'ledtrad': '<p>Tecknet visar om den linjära trenden stiger eller faller. Ett värde nära 1 eller −1 visar ett starkt linjärt samband.</p>'},
    '5.681': {
        's': '<div class="facit-v2 facit-stegvis"><p class="facit-rubrik"><strong>Undersök vad enhetsbytet gör</strong></p><p>Varje längd delas med 100 och varje vikt multipliceras med 1 000. Båda variablerna ändras alltså med positiva skalningsfaktorer. Punkterna kan se mer utdragna eller hoptryckta ut i ett diagram, men sambandet och dess riktning ändras inte.</p><p>Om varje avvikelse från medelvärdet delas med variabelns standardavvikelse försvinner de positiva skalningsfaktorerna. Därför är den linjära korrelationskoefficienten oförändrad.</p><p class="facit-svar"><strong>Svar:</strong> \\(r=0{,}72\\).</p></div>',
        'ledtrad': '<p>Alla längder delas med 100 och alla vikter multipliceras med 1 000. Ändrar positiva enhetsbyten korrelationskoefficienten?</p>'},
}
while True:
    while source[position].isspace() or source[position] == ',':
        position += 1
    if source[position] == ']':
        break
    question, end = decoder.raw_decode(source, position)
    ident = question.get('id')
    chunk = source[position:end]
    if ident in updates:
        revision = updates[ident]
        for key in ('t', 's', 'ledtrad'):
            if key not in revision:
                continue
            old = '"' + key + '": ' + json.dumps(question[key], ensure_ascii=False)
            assert chunk.count(old) == 1, (ident, key)
            chunk = chunk.replace(old, '"' + key + '": ' + json.dumps(revision[key], ensure_ascii=False), 1)
        for old, new in revision.get('replace', []):
            count = 3 if old.startswith('font-size=') else 1
            assert chunk.count(old) == count, (ident, old, chunk.count(old))
            chunk = chunk.replace(old, new)
        for old, new in revision.get('s_replace', []):
            assert chunk.count(old) == 1, (ident, old)
            chunk = chunk.replace(old, new)
        if 'correct' in revision:
            old = question['alternativ'][-1]['txt']
            assert question['alternativ'][-1]['ratt'] is True
            encoded = '"txt": ' + json.dumps(old, ensure_ascii=False)
            assert chunk.count(encoded) == 1
            chunk = chunk.replace(encoded, '"txt": ' + json.dumps(revision['correct'], ensure_ascii=False), 1)
            for alternative, comment in zip(question['alternativ'], revision['comments'], strict=True):
                if alternative['ratt']:
                    assert comment is None
                    continue
                assert comment and 'kommentar' not in alternative
                pattern = r'"txt"\s*:\s*' + re.escape(json.dumps(alternative['txt'], ensure_ascii=False)) + r'\s*,\s*"ratt"\s*:\s*false'
                chunk, count = re.subn(pattern, lambda match: match.group(0) + ', "kommentar": ' + json.dumps(comment, ensure_ascii=False), chunk, count=1)
                assert count == 1
        assert json.loads(chunk)['id'] == ident
        changes.append((position, end, chunk))
        seen.add(ident)
    position = end
assert seen == set(updates)
for start, end, chunk in reversed(changes):
    source = source[:start] + chunk + source[end:]
json.loads(source[source.index('['):source.rindex(']') + 1])
path.write_text(source, encoding='utf8')
print('Ändrade:', ', '.join(sorted(seen)))
