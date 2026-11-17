"""Felrapporter 2026-11-17 09:08 (Ma1 1.100, Fy1 8.2 och liknande ensamma a-uppgifter).
Logg: agent/FELRAPPORTER_2026-11-17_0908.md

  python tools/felrapporter-2026-11-17-0908.py [--skriv]
"""
import io, json, os, re, sys

ROT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Bank:
    """Objekt på översta nivån i arrayen; bara ändrade objekt skrivs om (indrag 2, objektets egna radslut)."""
    def __init__(self, fil):
        self.fil = os.path.join(ROT, fil)
        self.src = io.open(self.fil, encoding='utf-8', newline='').read()
        self.nl = '\r\n' if '\r\n' in self.src else '\n'

    def _spann(self, id_):
        dec, i = json.JSONDecoder(), self.src.index('[') + 1
        while True:
            while self.src[i] in ' \t\r\n,':
                i += 1
            obj, slut = dec.raw_decode(self.src, i)
            if obj.get('id') == id_:
                rad = self.src.rfind('\n', 0, i) + 1
                return i, slut, self.src[rad:i]
            i = slut

    def get(self, id_):
        s, e, _ = self._spann(id_)
        return json.loads(self.src[s:e])

    def put(self, id_, obj):
        s, e, ind = self._spann(id_)
        if ind.strip():  # kompakt bank (t.ex. Ma2): hela arrayen på en rad
            txt = json.dumps(obj, ensure_ascii=False, separators=(',', ':'))
        else:
            txt = json.dumps(obj, ensure_ascii=False, indent=2).replace('\n', self.nl + ind)
        self.src = self.src[:s] + txt + self.src[e:]

    def spara(self):
        json.loads(self.src[self.src.index('['):self.src.rindex(']') + 1])
        io.open(self.fil, 'w', encoding='utf-8', newline='').write(self.src)


def steg(rubrik, *delar):
    inn = ''.join(d if d.startswith('<') else f'<div class="facit-matte">\\[{d}\\]</div>' for d in delar)
    return f'<li><p class="facit-rubrik">{rubrik}</p>{inn}</li>'


def facit(*st, svar):
    return (f'<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">{"".join(st)}</ol>'
            f'<p class="facit-svar"><strong>Svar:</strong> {svar}</p></div>')


# Uppgifter som bara har en del men ändå markerar den "a)" (lärarkommentar till Fy1 8.2:
# "Står en a-uppgift när det inte finns fler deluppgifter").
ENSAMMA_A = {
    'uppgifter.js': ['2.226', '2.227', '8.2', '9.55', 'KG-FY1-ALFA-04', '9.402'],
    'uppgifterma2.js': ['3.393', '3.394', '3.395', '3.397', '3.399', '3.400'],
}

DEL_START = '<div class="facit-v2 facit-stegvis"><div class="facit-del"><span class="facit-mark">a)</span><div class="facit-arbete">'
STRONG_START = '<div class="facit-v2"><p><strong>a)</strong></p><div class="facit-v2">'


def ta_bort_ensamt_a(u):
    t = u['t']
    assert not re.search(r'(^|>|\s)[b-e]\)', t), u['id']
    assert t.count('<p>a) ') == 1, u['id']
    u['t'] = t.replace('<p>a) ', '<p>', 1)
    s = u['s']
    if s.startswith(DEL_START):
        assert s.count('facit-mark') == 1 and s.endswith('</div></div></div>'), u['id']
        s = '<div class="facit-v2 facit-stegvis">' + s[len(DEL_START):-len('</div></div>')]
    elif s.startswith(STRONG_START):
        assert s.count('<strong>a)</strong>') == 1 and s.endswith('</div></div>'), u['id']
        s = '<div class="facit-v2">' + s[len(STRONG_START):-len('</div>')]
    assert not re.search(r'facit-mark">a\)|<strong>a\)</strong>', s), u['id']
    u['s'] = s
    for d in u.get('spelDelar') or []:
        assert not re.search(r'(^|>)a\) ', (d.get('t') or '') + (d.get('fraga') or '')), u['id']
    return u


def main():
    banker = {}
    for fil, ids in ENSAMMA_A.items():
        b = banker[fil] = Bank(fil)
        for id_ in ids:
            b.put(id_, ta_bort_ensamt_a(b.get(id_)))

    # ---------- Ma1 1.100: basarean behövs inte, sätt in talen direkt i V = lbh
    m1 = banker['uppgifterma1.js'] = Bank('uppgifterma1.js')
    u = m1.get('1.100')
    assert 'Basarean' in u['s'] and u['rättSvar'] == 5
    u['ledtrad'] = r'<p>Sätt in volymen, längden och bredden i formeln \(V=lbh\). Vilken ekvation får du för \(h\)?</p>'
    u['s'] = facit(
        steg(r'Sätt in de kända värdena i formeln \(V=lbh\)',
             r'120=6\cdot4\cdot h'),
        steg('Multiplicera ihop de kända faktorerna',
             r'120=24h'),
        steg(r'Dela båda leden med 24 för att få \(h\) ensamt',
             r'h=\frac{120}{24}=5'),
        steg('Kontroll: sätt in höjden i formeln',
             r'6\cdot4\cdot5=120\ \mathrm{cm^3}'),
        svar='Höjden är 5 cm.')
    m1.put('1.100', u)

    if '--skriv' in sys.argv:
        for b in banker.values():
            b.spara()
        print('skrivet')
    else:
        print('torrkörning ok')


if __name__ == '__main__':
    main()
