"""Felrapporter från Kunskapsgymmet 2026-11-23 18:07 (agent/FELRAPPORTER_2026-11-23_1807.md).

- Fy1 3.63 (lärare: "konstig bild. cyklisten syns inte"): ny figur med cyklist på cykel, ritad i
  tools/bygg-fy1-kap3-figurer-2026-11-19.py (funktionen cyklist).
- Fy1 2.18 (lärare: "Ändra zinks densitet till 7,13 som vår formelsamling"): zink 7,13 g/cm³ i alla
  Fy1-uppgifter som använder zinkens densitet (2.18, 2.40, 2.156, 2.200), med nya svar och facit.

Körs: python tools/felrapporter-2026-11-23-1807.py [--skriv]
"""
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "sprak"))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True
from sprakverktyg import Bank  # noqa: E402

SKRIV = "--skriv" in sys.argv

spec = importlib.util.spec_from_file_location("k3", os.path.join(HERE, "bygg-fy1-kap3-figurer-2026-11-19.py"))
K3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(K3)


def bara_svg(s):
    return s[s.index("<svg"):s.rindex("</svg>") + 6]


def byt(s, par):
    for gammal, ny in par:
        assert gammal in s or gammal in dict(ZN), gammal
        s = s.replace(gammal, ny)
    assert s != "" and "7,14" not in s and "7{,}14" not in s
    return s


ZN = [("7,14", "7,13"), ("7{,}14", "7{,}13")]


def main():
    b = Bank("fy1")

    # ---------- 3.63: ny figur ----------
    u = b.obj("3.63")
    gammal = re.search(r"<svg.*?</svg>", u["t"], re.S).group(0)
    ny_t = u["t"].replace(gammal, bara_svg(K3.F["3.63"]))
    b.ersatt("3.63", [(u["t"], ny_t, "t")])

    # ---------- 2.18 ----------
    u = b.obj("2.18")
    s = byt(u["s"], ZN + [("14{,}0056", "14{,}0252"), ("\\approx8{,}26\\ ", "\\approx8{,}25\\ "),
                          ("\\(8{,}26\\ \\mathrm{g/cm^3}\\)", "\\(8{,}25\\ \\mathrm{g/cm^3}\\)")])
    b.ersatt("2.18", [(u["s"], s, "s"), (u["kgInstruktion"], byt(u["kgInstruktion"], ZN), "kgInstruktion")])
    txt = b.byte["2.18"]
    assert re.search(r'"rättSvar":\s*8\.258313253012048,', txt)
    b.byte["2.18"] = re.sub(r'("rättSvar":\s*)8\.258313253012048,', r'\g<1>' + repr(300 / (200 / 8.96 + 100 / 7.13)) + ',', txt)

    # ---------- 2.40 (bara jämförelsen i d) ----------
    u = b.obj("2.40")
    b.ersatt("2.40", [(u["t"], byt(u["t"], ZN), "t"), (u["s"], byt(u["s"], ZN), "s")])

    # ---------- 2.156: 0,65 m³ zink ----------
    u = b.obj("2.156")
    s = byt(u["s"], ZN + [("7140", "7130"), ("=4641\\ \\mathrm{kg}", "=4634{,}5\\ \\mathrm{kg}"),
                          ("<strong>Svar:</strong> \\(4641\\ \\mathrm{kg}\\)",
                           "<strong>Svar:</strong> \\(4635\\ \\mathrm{kg}\\)")])
    b.ersatt("2.156", [(u["s"], s, "s"), (u["kgInstruktion"], byt(u["kgInstruktion"], ZN), "kgInstruktion")])
    txt = b.byte["2.156"]
    # 0,65 · 7130 = 4634,5 kg: både 4634 och 4635 godtas efter avrundning till hela kilogram
    assert re.search(r'"rättSvar":\s*4641,', txt) and re.search(r'"tolerans":\s*0,', txt)
    txt = re.sub(r'("rättSvar":\s*)4641,', r'\g<1>4634.5,', txt)
    b.byte["2.156"] = re.sub(r'("tolerans":\s*)0,', r'\g<1>0.5,', txt, count=1)

    # ---------- 2.200: zinkens andel i mässing ----------
    u = b.obj("2.200")
    x = (100 - 820 / 8.96) / (1 / 7.13 - 1 / 8.96)
    assert abs(x - 296.109) < 0.001
    s = byt(u["s"], ZN + [("1{,}82x+5854{,}8&=6397{,}44", "1{,}83x+5846{,}6&=6388{,}48"),
                          ("x&=\\frac{542{,}64}{1{,}82}\\approx298{,}154", "x&=\\frac{541{,}88}{1{,}83}\\approx296{,}109"),
                          ("\\frac{542{,}64/1{,}82}{820}\\cdot100\\,\\%\\approx36{,}36\\,\\%",
                           "\\frac{541{,}88/1{,}83}{820}\\cdot100\\,\\%\\approx36{,}11\\,\\%"),
                          ("\\(36{,}4\\,\\%\\)", "\\(36{,}1\\,\\%\\)")])
    b.ersatt("2.200", [(u["s"], s, "s"), (u["kgInstruktion"], byt(u["kgInstruktion"], ZN), "kgInstruktion")])
    txt = b.byte["2.200"]
    assert re.search(r'"rättSvar":\s*36\.4,', txt)
    b.byte["2.200"] = re.sub(r'("rättSvar":\s*)36\.4,', r'\g<1>36.1,', txt)

    for id_ in b.byte:
        assert "7,14" not in b.byte[id_] and "7{,}14" not in b.byte[id_], id_
    print("ändrade:", ", ".join(b.byte), "| dubbletter:", b.dubbletter or "-")
    if SKRIV:
        b.spara()
    print("skrivet" if SKRIV else "torrkörning")


if __name__ == "__main__":
    main()
