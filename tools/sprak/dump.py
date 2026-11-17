"""Skriv ut ett områdes uppgifter i läsbar form för omskrivning för hand.
Användning: python tools/sprak/dump.py fy1 kollisioner [rorelsemangd ...] > ut.txt"""
import sys, json
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from sprakverktyg import Bank, till_platshallare, norm, li_lista

kod, omraden = sys.argv[1], set(sys.argv[2:])
b = Bank(kod)
for u in b.arr:
    if u.get("omr") not in omraden:
        continue
    t, _ = till_platshallare(u.get("t", ""))
    huvud = f"### {u['id']} | {u.get('typ','')} | svar={json.dumps(u.get('rättSvar'),ensure_ascii=False)} enh={json.dumps(u.get('svarEnhet'),ensure_ascii=False)}"
    if u.get("alternativ"):
        huvud += " | ALT=" + " / ".join(str(a.get("txt", a))[:40] for a in u["alternativ"])
    if u.get("kgInstruktion"):
        huvud += " | KG=" + u["kgInstruktion"]
    print(huvud)
    intro = u.get("spelIntro")
    delar = u.get("spelDelar") or []
    ll = li_lista(u.get("t", ""))
    if intro is not None and ll and norm(ll[0]) == norm(intro) and len(ll[1]) == len(delar) \
            and all(norm(a) == norm(d.get("fraga")) for a, d in zip(ll[1], delar)) and not ll[2].strip():
        print("T = INTRO + lista av fragor")
    else:
        print("T:", t)
    if intro is not None:
        print("INTRO:", till_platshallare(intro)[0])
    for d in delar:
        dt = d.get("t") or ""
        f = d.get("fraga") or ""
        if intro is not None and norm(dt) == norm(intro + "<p>" + f + "</p>"):
            print(f"  {d.get('etikett')}: [I+F] F: {f}")
        else:
            print(f"  {d.get('etikett')}: T: {till_platshallare(dt)[0]}  || F: {f}")
    print()
