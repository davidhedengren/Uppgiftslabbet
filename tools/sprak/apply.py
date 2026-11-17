"""För in handskrivna omskrivningar. Användning: python tools/sprak/apply.py fy1 tools/sprak/omskr/fy1_rorelsemangd.py [--skriv]
Omskrivningsfilen definierar R = {id: post}. En post kan ha:
  t      hela nya huvudtexten (Uppgiftslabbet), med [F1].. för originalets figurer
  fore, li, efter   ny text före listan, nya li-texter i ordning, ny text efter (behåller <ol …>-taggen)
  intro  ny spelIntro (figurer [F1].. ur originalets spelIntro)
  kg     kgInstruktion för huvuduppgiften (visas bara i Kunskapsgymmet)
  d      {etikett: {f, t, kg}} för delkort. Ett [I+F]-kort får t = intro + <p>f</p> om t saknas.
Om huvudtexten var INTRO + lista av frågor byggs den om från intro och delarnas f om t/li saknas."""
import sys, re, json, importlib.util, html as H
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from sprakverktyg import Bank, till_platshallare, fran_platshallare, norm, li_lista, lit

FORBJUDET = [r"[Vv]älj ett alternativ", r"[Mm]arkera det korrekta", r"\(Svara ", r"[Ss]vara med (tre|två|en) ",
             r"\b(?:[a-zåäö]+) på [\d ,]+ ?(?:kg|g|ton)\b", r"\b[Vv]ågrät", r"\b[Ll]odrät", r"från vila",
             r"positiva? riktning", r"med tecken", r"[Aa]nge tecken", r"krafters impuls", r"[Rr]äkna (bara )?på",
             r"[Ss]ammanlagd", r"[Bb]ortse från andra", r"[Rr]äkna bara med", r"[Ee]ndast .* verkar",
             r"[Bb]ara .* verkar", r"utan tecken", r"\bentydigt\b", r"[Mm]arkera"]


def synlig(h):
    h, _ = till_platshallare(h)
    return re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", h)))


def tal(h):
    s = synlig(h).replace(" ", " ")
    s = re.sub(r"(?<=\d) (?=\d{3}\b)", "", s)
    return sorted(re.findall(r"\d+(?:,\d+)?", s))


def jamfor(id_, falt, gammal, ny, varn):
    a, b = tal(gammal), tal(ny)
    sa, sb = list(a), list(b)
    for x in a:
        if x in sb:
            sb.remove(x); sa.remove(x)
    if sa or sb:
        varn.append(f"{id_} {falt}: tal borta {sa} nya {sb}")
    for rx in FORBJUDET:
        m = re.search(rx, synlig(ny))
        if m:
            varn.append(f"{id_} {falt}: mönster «{m.group(0)}»")


def main():
    kod, fil = sys.argv[1], sys.argv[2]
    skriv = "--skriv" in sys.argv
    spec = importlib.util.spec_from_file_location("omskr", fil)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    b = Bank(kod)
    varn, antal = [], 0
    for id_, p in mod.R.items():
        u = b.obj(id_)
        par, till = [], []

        def lagg(obj, ankare, nyckel, varde):
            """Lägg till nyckel, eller byt värdet om nyckeln redan finns (gör omkörning idempotent)."""
            if nyckel in obj:
                if obj[nyckel] != varde:
                    if not isinstance(obj[nyckel], str):
                        raise ValueError(f"{id_}: {nyckel} finns redan med annat värde")
                    par.append((obj[nyckel], varde, nyckel))
            else:
                till.append((ankare, nyckel, varde))
        t0, intro0 = u.get("t", ""), u.get("spelIntro")
        delar = u.get("spelDelar") or []
        ll = li_lista(t0)
        var_lista = (intro0 is not None and ll and norm(ll[0]) == norm(intro0) and len(ll[1]) == len(delar)
                     and all(norm(x) == norm(d.get("fraga")) for x, d in zip(ll[1], delar)) and not ll[2].strip())
        # ers: handskrivna delsträngsbyten [(gammal, ny)] i t, spelIntro och delkortens t/fraga.
        # Används när bara en mening ska bort eller skrivas om. Varje byte måste träffa minst en gång.
        if p.get("ers"):
            u2 = json.loads(json.dumps(u))
            for a, c in p["ers"]:
                traff = 0
                for obj, key in [(u2, "t"), (u2, "spelIntro")] + [(d, k) for d in (u2.get("spelDelar") or []) for k in ("t", "fraga")]:
                    if isinstance(obj.get(key), str) and a in obj[key]:
                        obj[key] = obj[key].replace(a, c); traff += 1
                if not traff:
                    finns = any(isinstance(o.get(k), str) and c and c in o[k] for o, k in [(u2, "t"), (u2, "spelIntro")] + [(d, kk) for d in (u2.get("spelDelar") or []) for kk in ("t", "fraga")])
                    if not finns and c:
                        raise ValueError(f"{id_}: ers hittade inte «{a[:50]}»")
            p = dict(p)
            if u2.get("t") != u.get("t") and "t" not in p and "li" not in p and "fore" not in p:
                p["t"] = till_platshallare(u2["t"])[0]
            if u2.get("spelIntro") != u.get("spelIntro") and "intro" not in p:
                p["intro"] = till_platshallare(u2["spelIntro"])[0]
            dd = dict(p.get("d") or {})
            for i, (d0, d2) in enumerate(zip(u.get("spelDelar") or [], u2.get("spelDelar") or [])):
                et = d0.get("etikett") or chr(97 + i)
                q = dict(dd.get(et) or {})
                if d2.get("t") != d0.get("t") and "t" not in q:
                    q["t"] = till_platshallare(d2["t"])[0]
                if d2.get("fraga") != d0.get("fraga") and "f" not in q:
                    q["f"] = d2["fraga"]
                    # Egen t som inte innehöll den bytta frasen: behåll den (annars kräver delkortet t).
                    if d0.get("t") and "t" not in q and not (intro0 is not None and norm(d0["t"]) == norm(intro0 + "<p>" + (d0.get("fraga") or "") + "</p>")):
                        q["t"] = till_platshallare(d2["t"])[0]
                if q:
                    dd[et] = q
            p["d"] = dd
        # spelIntro
        intro1 = intro0
        if "intro" in p:
            intro1 = fran_platshallare(p["intro"], till_platshallare(intro0)[1], id_ + " intro")
            jamfor(id_, "intro", intro0, intro1, varn)
            par.append((intro0, intro1, "spelIntro"))
        # delkort
        nya_f = {}
        for i, d in enumerate(delar):
            et = d.get("etikett") or chr(97 + i)
            q = (p.get("d") or {}).get(et)
            if not q:
                if "intro" in p and d.get("t") and intro0 is not None and norm(d["t"]) == norm(intro0 + "<p>" + (d.get("fraga") or "") + "</p>"):
                    par.append((d["t"], intro1 + "<p>" + d["fraga"] + "</p>", "t"))
                continue
            f0, dt0 = d.get("fraga"), d.get("t")
            f1 = q.get("f", f0)
            nya_f[i] = f1
            if "t" in q:
                dt1 = fran_platshallare(q["t"], till_platshallare(dt0)[1], f"{id_}{et}")
            elif dt0 and intro0 is not None and norm(dt0) == norm(intro0 + "<p>" + (f0 or "") + "</p>"):
                dt1 = intro1 + "<p>" + f1 + "</p>"
            elif dt0 and "f" in q:
                raise ValueError(f"{id_}{et}: delkortet har egen t, ange t")
            else:
                dt1 = dt0
            if dt0 is not None:
                jamfor(id_, f"del {et}", dt0, dt1, varn)
            par += [(dt0, dt1, "t")] if dt0 is not None else []
            par += [(f0, f1, "fraga")] if f0 is not None else []
            if q.get("kg"):
                lagg(d, dt1 if dt0 is not None else f1, "kgInstruktion", q["kg"])
        # huvudtext
        figs = till_platshallare(t0)[1]
        if "t" in p:
            t1 = fran_platshallare(p["t"], figs, id_)
        elif "li" in p or "fore" in p:
            fore, lis, efter = ll
            nfore = p.get("fore", fore)
            nlis = p.get("li", lis)
            if len(nlis) != len(lis):
                raise ValueError(f"{id_}: {len(lis)} li i originalet")
            olm = re.search(r"<ol[^>]*>", t0).group(0)
            t1 = nfore + olm + "".join(f"<li>{x}</li>" for x in nlis) + "</ol>" + p.get("efter", efter)
            antal_f = len(re.findall(r"\[F\d+\]", t1))
            if antal_f:
                t1 = fran_platshallare(t1, figs, id_)
        elif var_lista and ("intro" in p or nya_f):
            olm = re.search(r"<ol[^>]*>", t0).group(0)
            fr = [nya_f.get(i, d.get("fraga")) for i, d in enumerate(delar)]
            t1 = intro1 + olm + "".join(f"<li>{x}</li>" for x in fr) + "</ol>"
        else:
            t1 = t0
        if t1 != t0:
            jamfor(id_, "t", t0, t1, varn)
            par.insert(0, (t0, t1, "t"))
        if p.get("kg"):
            lagg(u, t1, "kgInstruktion", p["kg"])
        # Uppgiftslabbet skriver bara ut flervalsalternativen om texten nämner "alternativ/markera/…"
        # eller om visaAlternativ är true (altVisas i index.html). Sätt flaggan när ordet försvinner.
        ALT = re.compile(r"alternativ|markera|kryssa|ringa in", re.I)
        if u.get("alternativ") and ALT.search(t0) and not ALT.search(t1) and u.get("visaAlternativ") is not True:
            lagg(u, t1, "visaAlternativ", True)
        for nyckel, varde in (p.get("extra") or {}).items():
            lagg(u, t1, nyckel, varde)
        # facitjustering när pappersfrågan ändrats (sbyt: [(gammal delsträng, ny delsträng)] i huvudfacit s)
        if p.get("sbyt"):
            s0 = u["s"]; s1 = s0
            for a, c in p["sbyt"]:
                if s1.count(a) == 0 and c in s1:
                    continue  # redan gjort (omkörning)
                if s1.count(a) != 1:
                    raise ValueError(f"{id_}: sbyt hittades {s1.count(a)} gånger")
                s1 = s1.replace(a, c)
            if s1 != s0:
                par.append((s0, s1, "s"))
                varn.append(f"{id_}: huvudfacit justerat")
        # ordna så att längre strängar ersätts först (undviker delsträngskrockar i literalerna)
        b.ersatt(id_, par, till)
        antal += 1
    varn += b.dubbletter
    for v in varn:
        print("VARNING", v)
    print(antal, "uppgifter klara", "(skrivet)" if skriv else "(torrkörning)")
    if skriv:
        print(b.spara(), "objekt skrivna")


if __name__ == "__main__":
    main()
