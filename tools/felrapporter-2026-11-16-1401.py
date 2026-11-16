"""Felrapporter 2026-11-16 14:01 (Ma5 4.174, 4.469; Ma1 4.529). Logg: agent/FELRAPPORTER_2026-11-16_1401.md

  python tools/felrapporter-2026-11-16-1401.py [--skriv]
"""
import io, json, os, sys

ROT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROT, 'tools'))


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


def main():
    # ---------- Ma5 4.469: "Hur mycket mindre" var tvetydigt (skillnad eller kvot?); generisk ledtråd och metodtext
    m5 = Bank('uppgiftermatf1.js')
    u = m5.get('4.469')
    gammal_t = u['t']
    assert 'Hur mycket mindre blir felet ungefär?' in gammal_t, gammal_t
    u['t'] = gammal_t.replace('Hur mycket mindre blir felet ungefär?',
                              'Hur många gånger mindre blir felet när steglängden halveras? (Svara med kvoten mellan felen.)')
    u['t'] = u['t'].replace('h=0,2', 'h=0{,}2').replace('h=0,1', 'h=0{,}1')
    u['ledtrad'] = (r"<p>För \(y'=y\) ger varje steg i Eulers metod \(y_{n+1}=y_n+h\cdot y_n=(1+h)\,y_n\). "
                    r"Hur många steg behövs till \(x=1\) med respektive steglängd?</p>")
    u['s'] = facit(
        steg(r"Eulers metod för \(y'=y\): \(y_{n+1}=(1+h)\,y_n\)",
             '<p>Varje steg multiplicerar med \\(1+h\\). Till \\(x=1\\) behövs \\(1/h\\) steg, så \\(y(1)\\approx(1+h)^{1/h}\\).</p>'),
        steg(r'Steglängd \(h=0{,}2\): fem steg',
             r'y(1)\approx1{,}2^5=2{,}488320',
             r'\text{fel}=e-2{,}488320\approx0{,}229962'),
        steg(r'Steglängd \(h=0{,}1\): tio steg',
             r'y(1)\approx1{,}1^{10}\approx2{,}593742',
             r'\text{fel}=e-2{,}593742\approx0{,}124540'),
        steg(r'Hur många gånger mindre: kvoten mellan felen',
             r'\frac{0{,}229962}{0{,}124540}\approx1{,}85',
             '<p>Felet blir ungefär hälften så stort när steglängden halveras. Det stämmer med att felet i Eulers metod är ungefär proportionellt mot \\(h\\).</p>'),
        svar='Ungefär 1,85 gånger mindre.')
    m5.put('4.469', u)

    # ---------- Ma5 4.174 och 4.582: stabilitet hos jämviktslösningar ligger utanför kursen (lärarrapport) -> bara i Uppgiftslabbet
    for id_ in ('4.174', '4.582'):
        u = m5.get(id_)
        assert 'stabil' in (u['t'] + u['s']).lower(), id_
        u['spel'] = False
        m5.put(id_, u)

    # ---------- Ma1 4.529: höjden ritades utanför trapetsen
    m1 = Bank('uppgifterma1.js')
    u = m1.get('4.529')
    gammal = ('<line x1="300.0" y1="60.0" x2="300.0" y2="153.0" stroke="#c2410c" stroke-width="1.5" stroke-dasharray="5 4"/>'
              '<rect x="302.0" y="99.0" width="48.6" height="18" rx="3" fill="#fff"/>'
              '<text x="306.0" y="112.0" font-family="Arial,sans-serif" font-size="14" text-anchor="start" fill="#c2410c" font-weight="bold">0,6 m</text>')
    ny = ('<line x1="242.0" y1="60.0" x2="242.0" y2="153.0" stroke="#c2410c" stroke-width="1.5" stroke-dasharray="5 4"/>'
          '<polyline points="234.0,60.0 234.0,68.0 242.0,68.0" fill="none" stroke="#c2410c" stroke-width="1.3"/>'
          '<rect x="180.0" y="99.0" width="54.0" height="18" rx="3" fill="#fff"/>'
          '<text x="230.0" y="112.0" font-family="Arial,sans-serif" font-size="14" text-anchor="end" fill="#c2410c" font-weight="bold">0,6 m</text>')
    assert u['t'].count(gammal) == 1
    u['t'] = u['t'].replace(gammal, ny)
    m1.put('4.529', u)

    if '--skriv' in sys.argv:
        m5.spara(); m1.spara(); print('skrivet')
    else:
        print('torrkörning ok')


if __name__ == '__main__':
    main()
