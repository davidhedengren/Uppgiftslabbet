"""Felrapport 2026-11-25 10:47, Fy1 2.258 (lärare: ”Jätte konstig uppgift”).

Uppgiften var rätt räknad men krånglig: modellspråk (”sensorns visning ändras linjärt mellan kalibreringspunkterna”,
”Antag att isens temperatur är exakt 0 °C och det kokande vattnets exakt 100 °C vid kalibreringen”), en
svarsinstruktion i texten (”Ange svaret med en decimal.”, mot beslutet om rena uppgifter 2026-11-23) och frågan före
figuren. Texten skrivs om enkelt och konkret: termometern visar 99,8 grader där den verkliga skillnaden är 100 grader,
och felet fördelar sig jämnt längs skalan. Ledtråden får vardagliga ord i stället för ”kalibreringsavläsningarna”, och
facit får steget ”Givet och sökt” enligt FACITMALL. Tal, figur och svar (50,0 °C) är oförändrade.

  python tools/felrapporter-2026-11-25-1047.py [--skriv]
"""
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
FIL = os.path.join(ROOT, 'uppgifter.js')

NY_T_FORE = ('<p>En termometer visar 0,8 °C i smältande is och 100,6 °C i kokande vatten, där den borde visa 0 °C '
             'och 100 °C. Mellan de två punkterna visar den alltså 99,8 grader för en verklig skillnad på 100 grader. '
             'Felet fördelar sig jämnt längs hela skalan.</p>')
NY_T_FRAGA = '<p>Vilken är den verkliga temperaturen när termometern visar 50,7 °C?</p>'
NY_LEDTRAD = ('<p>Hur många grader över 0,8 °C ligger 50,7 °C? Hur stor andel är det av de 99,8 grader som motsvarar '
              '100 verkliga grader?</p>')
NY_S = ('<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'
        '<li><p class="facit-rubrik">Givet och sökt</p>'
        '<div class="facit-matte">\\[\\begin{aligned}&u_0=0{,}8\\ ^\\circ\\mathrm C\\ \\text{(visas vid 0 °C)}\\\\'
        '&u_{100}=100{,}6\\ ^\\circ\\mathrm C\\ \\text{(visas vid 100 °C)}\\\\&u=50{,}7\\ ^\\circ\\mathrm C\\end{aligned}\\]</div>'
        '<p>Sökt: den verkliga temperaturen \\(T\\).</p></li>'
        '<li><p class="facit-rubrik">Termometerns grader är lika stora längs skalan: '
        '\\(T=\\frac{u-u_0}{u_{100}-u_0}\\cdot100\\ ^\\circ\\mathrm C\\)</p>'
        '<p>Mellan is och kokande vatten visar termometern \\(100{,}6-0{,}8=99{,}8\\) grader för 100 verkliga grader. '
        'Avläsningen ligger \\(50{,}7-0{,}8=49{,}9\\) grader över isens avläsning.</p></li>'
        '<li><p class="facit-rubrik">Sätt in avläsningarna</p>'
        '<div class="facit-matte">\\[T=\\frac{49{,}9}{99{,}8}\\cdot100\\ ^\\circ\\mathrm C=50{,}0\\ ^\\circ\\mathrm C\\]</div></li>'
        '</ol><p class="facit-svar"><strong>Svar:</strong> \\(50{,}0\\ ^\\circ\\mathrm C\\).</p></div>')


def lit(v):
    return json.dumps(v, ensure_ascii=False)


def main():
    src = open(FIL, encoding='utf-8', newline='').read()
    bank = json.loads(src[src.index('['):src.rindex(']') + 1])
    q = next(x for x in bank if x['id'] == '2.258')
    figur = re.search(r'<span class="fig">[\s\S]*?</svg></span>', q['t'])
    assert figur, 'figuren saknas'
    ny_t = NY_T_FORE + figur.group(0) + NY_T_FRAGA
    assert abs((50.7 - 0.8) / (100.6 - 0.8) * 100 - q['rättSvar']) < 1e-9
    ny = src
    for falt, varde in (('t', ny_t), ('s', NY_S), ('ledtrad', NY_LEDTRAD)):
        a = lit(q[falt])
        assert ny.count(a) == 1, falt
        ny = ny.replace(a, lit(varde))
    efter = json.loads(ny[ny.index('['):ny.rindex(']') + 1])
    andr = [(x['id'], sorted(k for k in set(x) | set(y) if x.get(k) != y.get(k))) for x, y in zip(bank, efter) if x != y]
    assert andr == [('2.258', ['ledtrad', 's', 't'])], andr
    print(andr)
    if '--skriv' in sys.argv:
        with open(FIL, 'w', encoding='utf-8', newline='') as fh:
            fh.write(ny)


if __name__ == '__main__':
    main()
