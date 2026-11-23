"""Felrapporter från Kunskapsgymmet 2026-11-23 13:45 (agent/FELRAPPORTER_2026-11-23_1345.md).

- Ma1 5.242 (lärare: "Totalt obegriplig fråga"): ny text med figur, facit enligt FACITMALL, svarFormat heltal.
- Ma2 2.453 (lärare: "Svårt utan räknare"): nollställena är 70 ± √1300, miniräknare tillåten.
- Ma4 1.608 och 1.585 (elev: svara i grader): kgInstruktion om grader på perioder och argument där
  frågan inte har något gradintervall som visar enheten. 1.585 fick "Svara i grader." 2026-11-23 (33796a1).

Körs: python tools/felrapport-2026-11-23-1345.py [--skriv]
"""
import sys, os, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "sprak"))
from sprakverktyg import Bank, lit

SKRIV = "--skriv" in sys.argv

# ---------- Ma1 5.242 ----------
def hjul():
    import math
    cx, cy, r = 80, 84, 62
    farg = ["#f6c945", "#5b8def", "#5b8def", "#5b8def", "#5b8def"]
    delar = []
    for i in range(5):
        a0 = math.radians(-90 + 72 * i)
        a1 = math.radians(-90 + 72 * (i + 1))
        x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        delar.append(f'<path d="M{cx},{cy} L{x0:.1f},{y0:.1f} A{r},{r} 0 0 1 {x1:.1f},{y1:.1f} Z" '
                     f'fill="{farg[i]}" stroke="#ffffff" stroke-width="2"/>')
        am = math.radians(-90 + 72 * i + 36)
        tx, ty = cx + 0.62 * r * math.cos(am), cy + 0.62 * r * math.sin(am) + 5
        namn = "gul" if i == 0 else "blå"
        delar.append(f'<text x="{tx:.1f}" y="{ty:.1f}" text-anchor="middle" font-size="13" '
                     f'font-family="sans-serif" fill="#1b1b1b">{namn}</text>')
    pil = f'<path d="M{cx - 8},{cy - r - 14} L{cx + 8},{cy - r - 14} L{cx},{cy - r + 2} Z" fill="#333333"/>'
    nav = f'<circle cx="{cx}" cy="{cy}" r="5" fill="#333333"/>'
    return ('<svg viewBox="0 0 160 156" width="160" height="156" role="img" '
            'aria-label="Lyckohjul med fem lika stora fält: ett gult och fyra blå." '
            'xmlns="http://www.w3.org/2000/svg">' + "".join(delar) + nav + pil + "</svg>")

T_5242 = ("<p>Ett lyckohjul har 5 lika stora fält. Ett fält är gult och de andra fyra är blå.</p>"
          f'<div class="fig smal">{hjul()}</div>'
          "<p>Du gör ett nytt hjul. Det har samma fem fält och dessutom några nya gula fält. "
          "Alla fält på det nya hjulet är lika stora.</p>"
          "<p>Hur många gula fält måste du lägga till för att sannolikheten att få gult ska bli \\(\\frac{1}{2}\\)?</p>")

S_5242 = ('<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'
          '<li><p class="facit-rubrik">Sannolikhet: \\(P(\\text{gult})=\\dfrac{\\text{antal gula fält}}{\\text{antal fält}}\\)</p>'
          '<p>Lägg till \\(x\\) gula fält. Då finns \\(1+x\\) gula fält av totalt \\(5+x\\) fält:</p>'
          '<div class="facit-matte">\\[P(\\text{gult})=\\frac{1+x}{5+x}\\]</div></li>'
          '<li><p class="facit-rubrik">Sätt sannolikheten lika med \\(\\frac{1}{2}\\)</p>'
          '<div class="facit-matte">\\[\\frac{1+x}{5+x}=\\frac{1}{2}\\]</div>'
          '<p>Multiplicera båda leden med \\(2(5+x)\\):</p>'
          '<div class="facit-matte">\\[2(1+x)=5+x\\]\\[2+2x=5+x\\]\\[x=3\\]</div></li>'
          '<li><p class="facit-rubrik">Kontroll: hälften gula betyder lika många gula som blå</p>'
          '<p>De fyra blå fälten finns kvar. Med 3 nya gula fält blir det 4 gula av 8 fält:</p>'
          '<div class="facit-matte">\\[\\frac{4}{8}=\\frac{1}{2}\\]</div></li>'
          '</ol><p class="facit-svar"><strong>Svar: 3 gula fält.</strong></p></div>')

L_5242 = ("<p>De blå fälten finns kvar på det nya hjulet. Hur många gula fält behövs för att "
          "hälften av alla fält ska vara gula?</p>")

# ---------- Ma4: kgInstruktion om grader ----------
GRADER = {
    "1.608": "Svara i grader.",          # felrapporten: period för sin(2x)
    "1.619": "Svara i grader.",
    "1.622": "Svara i grader.",
    "1.660": "Svara i grader.",
    "1.610": "Ange perioden i grader.",
    "1.611": "Ange perioden i grader.",
    "2.657": "Svara i grader.",
    "2.684": "Svara i grader.",
    "2.702": "Svara i grader.",
    "2.691": "Ange perioden i grader.",
    "2.558": "Svara i grader.",
    "4.482": "Svara i grader.",
    "4.483": "Svara i grader.",
    "4.484": "Svara i grader.",
}


def lagg_till_efter_t(b, id_, nyckel, varde):
    u = b.obj(id_)
    if nyckel in u:
        if u[nyckel] == varde:
            return False
        raise ValueError(f"{id_}: {nyckel} finns redan: {u[nyckel]}")
    b.ersatt(id_, [], [(u["t"], nyckel, varde)])
    return True


def main():
    andrade = {}
    # Ma1
    b = Bank("ma1")
    u = b.obj("5.242")
    b.ersatt("5.242", [(u["t"], T_5242, "t"), (u["s"], S_5242, "s"), (u["ledtrad"], L_5242, "ledtrad"),
                       ("bråk", "heltal", "svarFormat")])
    andrade["ma1"] = (b, ["5.242"])
    # Ma2
    b = Bank("ma2")
    txt = b.text("2.453")
    assert txt.count('"miniräknare":false') == 1, "2.453: miniräknare-flaggan hittades inte"
    b.byte["2.453"] = txt.replace('"miniräknare":false', '"miniräknare":true')
    andrade["ma2"] = (b, ["2.453"])
    # Ma4
    b = Bank("mato2")
    ids = [id_ for id_, kg in GRADER.items() if lagg_till_efter_t(b, id_, "kgInstruktion", kg)]
    andrade["mato2"] = (b, ids)

    for kod, (b, ids) in andrade.items():
        for id_ in ids:
            if id_ in b.byte:
                import json
                json.loads(b.byte[id_])  # giltigt objekt
        print(kod, len(ids), "uppgifter:", ", ".join(ids), "| dubbletter:", b.dubbletter or "-")
        if SKRIV:
            b.spara()
    print("skrivet" if SKRIV else "torrkörning")


if __name__ == "__main__":
    main()
