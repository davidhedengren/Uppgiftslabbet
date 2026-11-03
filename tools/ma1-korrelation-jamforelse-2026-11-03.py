"""Gör tre jämförelser av linjär korrelation entydiga och begripliga."""
import json
import re
from pathlib import Path

path = Path(__file__).resolve().parent.parent / 'uppgifterma1.js'
source = path.read_text(encoding='utf8')
decoder = json.JSONDecoder()
position = source.index('[') + 1
changes = []
seen = set()
revisions = {
    '5.07': {
        't_prefix': ('Vilket av punktdiagrammen visar den starkaste positiva korrelationen?',
                     'Vilket av punktdiagrammen visar den starkaste positiva korrelationen? Välj ett alternativ.'),
        's': '<div class="facit-v2 facit-stegvis"><p class="facit-rubrik"><strong>Jämför punktmolnen</strong></p><p>I A ligger alla punkter på en stigande rät linje. Korrelationen är därför perfekt positiv.</p><p>Även B visar en stigande tendens, men punkterna ligger inte på en rät linje. Korrelationen i B är därför svagare än i A.</p><p class="facit-svar"><strong>Svar:</strong> Diagram A.</p></div>',
        'kommentarer': [None, 'A är perfekt positivt linjärt, medan punkterna i B inte ligger på en rät linje.', 'A är perfekt positivt linjärt. B stiger också, men är inte perfekt linjärt.', 'Punkterna i båda diagrammen visar en stigande tendens.']},
    '5.25': {
        't': '<p>För två variabler är korrelationskoefficienten \\(r=-0{,}93\\). Beskriv det linjära sambandet. Välj ett alternativ.</p>',
        's': '<div class="facit-v2 facit-stegvis"><p class="facit-rubrik"><strong>Tolka tecknet och styrkan</strong></p><p>Minustecknet visar att sambandet är negativt: när den ena variabeln ökar tenderar den andra att minska.</p><p>Talet ligger nära \\(-1\\), så det linjära sambandet är starkt.</p><p class="facit-svar"><strong>Svar:</strong> Stark negativ korrelation.</p></div>',
        'ledtrad': '<p>Vad betyder minustecknet? Hur nära ligger talet \\(-1\\)?</p>',
        'kommentarer': ['Minustecknet visar att sambandet är negativt.', None, 'Värdet ligger nära −1 och visar ett starkt negativt linjärt samband.', 'Värdet ligger nära −1, så det linjära sambandet är starkt.']},
    '5.69': {
        't': '<p>Två punktdiagram visar båda en fallande trend. I diagram A ligger alla punkter exakt på en fallande rät linje. I diagram B ligger punkterna inte på en och samma räta linje.</p><p>Vilket diagram har starkast negativ linjär korrelation? Välj ett alternativ.</p>',
        's': '<div class="facit-v2 facit-stegvis"><p class="facit-rubrik"><strong>Jämför med en perfekt linje</strong></p><p>Alla punkter i A ligger på en fallande rät linje. Därför är korrelationen där \\(r=-1\\), alltså perfekt negativ.</p><p>B har en fallande trend, men punkterna ligger inte på en och samma linje. Korrelationen är därför inte perfekt negativ och är svagare än i A.</p><p class="facit-svar"><strong>Svar:</strong> Diagram A.</p></div>',
        'ledtrad': '<p>Vad är korrelationen när alla punkter ligger exakt på en fallande rät linje?</p>',
        'kommentarer': [None, 'A har perfekt negativ korrelation. B:s punkter ligger inte på en och samma räta linje.', 'A är perfekt negativt linjärt medan B inte är det.', 'Båda är negativa, men A är perfekt negativt linjärt och B är det inte.']},
}

while True:
    while source[position].isspace() or source[position] == ',':
        position += 1
    if source[position] == ']':
        break
    question, end = decoder.raw_decode(source, position)
    ident = question.get('id')
    chunk = source[position:end]
    if ident in revisions:
        revision = revisions[ident]
        for key in ('t', 's', 'ledtrad'):
            if key not in revision:
                continue
            old = '"' + key + '": ' + json.dumps(question[key], ensure_ascii=False)
            assert chunk.count(old) == 1, (ident, key)
            chunk = chunk.replace(old, '"' + key + '": ' + json.dumps(revision[key], ensure_ascii=False), 1)
        if 't_prefix' in revision:
            old, new = revision['t_prefix']
            assert chunk.count(old) == 1
            chunk = chunk.replace(old, new, 1)
        if ident == '5.07':
            # Diagramrubrikerna ska förbli läsbara när SVG-bilden krymps på mobil.
            assert chunk.count('font-size=\\"12\\"') == 2
            chunk = chunk.replace('font-size=\\"12\\"', 'font-size=\\"24\\"')
        assert sum(bool(a['ratt']) for a in question['alternativ']) == 1
        for alternative, comment in zip(question['alternativ'], revision['kommentarer'], strict=True):
            if alternative['ratt']:
                assert comment is None
                continue
            assert comment and 'kommentar' not in alternative
            pattern = r'"txt"\s*:\s*' + re.escape(json.dumps(alternative['txt'], ensure_ascii=False)) + r'\s*,\s*"ratt"\s*:\s*false'
            chunk, count = re.subn(pattern, lambda match: match.group(0) + ', "kommentar": ' + json.dumps(comment, ensure_ascii=False), chunk, count=1)
            assert count == 1, (ident, alternative['txt'])
        assert json.loads(chunk)['id'] == ident
        changes.append((position, end, chunk))
        seen.add(ident)
    position = end
assert seen == set(revisions)
for start, end, chunk in reversed(changes):
    source = source[:start] + chunk + source[end:]
json.loads(source[source.index('['):source.rindex(']') + 1])
path.write_text(source, encoding='utf8')
print('Ändrade:', ', '.join(sorted(seen)))
