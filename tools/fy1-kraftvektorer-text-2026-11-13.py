"""Fy1 Vektorer (kraftvektorer), användarens önskemål 2026-11-13:
- punkter och vektorer skrivs (30, 20) i stället för (30; 20);
- facitrubriken ”Kraftresultant längs en linje” heter ”Resulterande kraft”;
- ”Addera sedan med tecken” och ”summan av alla krafter med tecken” skrivs om till
  ”adderar du … (tänk på tecknen)”.
Ändrar bara uppgifter med omr = kraftvektorer, direkt i texten så att filens format bevaras. Idempotent.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bankpatch  # noqa: E402

FIL = 'uppgifter.js'
BYTEN = [
    ('Kraftresultant längs en linje: \\\\(F_R', 'Resulterande kraft: \\\\(F_R'),
    ('Addera sedan med tecken.', 'Sedan adderar du alla krafter (tänk på tecknen).'),
    ('Resultanten är summan av alla krafter med tecken.', 'Resultanten får du genom att addera alla krafter (tänk på tecknen).'),
]
# (30;\ 20) i LaTeX, i filen JSON-kodat som (30;\\ 20), blir (30,\,20).
PUNKT = re.compile(r'\((-?\d+);\\\\ (-?\d+)\)')


def main():
    src = open(FIL, encoding='utf-8').read()
    ids = [u['id'] for u in json.loads(src[src.index('['):src.rindex(']') + 1]) if u.get('omr') == 'kraftvektorer']
    antal = {k: 0 for k, _ in BYTEN}
    punkter = 0
    for uid in ids:
        start, slut, _, _ = bankpatch.hitta(src, uid)
        bit = src[start:slut]
        for gammal, ny in BYTEN:
            antal[gammal] += bit.count(gammal)
            bit = bit.replace(gammal, ny)
        bit, n = PUNKT.subn(r'(\1,\\\\,\2)', bit)
        punkter += n
        src = src[:start] + bit + src[slut:]
    bank = json.loads(src[src.index('['):src.rindex(']') + 1])
    for u in bank:
        if u.get('omr') == 'kraftvektorer':
            j = json.dumps(u, ensure_ascii=False)
            assert not re.search(r'\d;\\\\ ', j), u['id']
            assert 'längs en linje:' not in j and 'Addera sedan med tecken' not in j, u['id']
    with open(FIL, 'w', encoding='utf-8', newline='') as fh:
        fh.write(src)
    print(len(ids), 'uppgifter;', antal, '; punkter:', punkter)


if __name__ == '__main__':
    main()
