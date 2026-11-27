"""Pedagogiska vägval och förklaringar beräknade från elevens faktiska karta."""

import json
import re
from functools import cache
from pathlib import Path
from xml.etree import ElementTree as ET

import ai_sokalgoritmer as A


@cache
def kartval():
    return json.loads(
        Path(__file__).with_name("ai-labyrintval.json").read_text(encoding="utf-8")
    )


def vald_karta(id_):
    fall = kartval()[id_]
    return fall["rows"], [(ord(k[0]) - 65, int(k[1:]) - 1) for k in fall["markers"]]


def las_karta(svg):
    figur = ET.fromstring(svg)
    plattor = [e for e in figur if e.get("rx") == "4" and e.get("stroke") == "#1d2743"]
    sida = int(plattor[0].get("width"))
    x0, y0 = (
        min(int(e.get("x")) for e in plattor),
        min(int(e.get("y")) for e in plattor),
    )

    def position(e):
        return (int(e.get("y")) - y0) // sida, (int(e.get("x")) - x0) // sida

    farger = {
        "#334155": "#",
        "#fff": ".",
        "#bfdbfe": ".",
        "#22a05a": "S",
        "#d94343": "G",
        "#d6b98c": "3",
        "#c4d7ef": "4",
        "#f4ba88": "5",
    }
    celler = {position(e): farger[e.get("fill")] for e in plattor}
    bokstaver = {}
    for e in figur:
        if not e.tag.endswith("}text") or not e.text or position(e) not in celler:
            continue
        if e.text.isdigit():
            celler[position(e)] = e.text
        elif re.fullmatch("[A-Z]", e.text):
            bokstaver[e.text] = position(e)
    rader, kolumner = max(r for r, c in celler) + 1, max(c for r, c in celler) + 1
    return [
        "".join(celler[r, c] for c in range(kolumner)) for r in range(rader)
    ], bokstaver


def vagval(p, q):
    for i, (a, b) in enumerate(zip(p, q)):
        if a != b:
            return tuple(map(A.cname, (p[i - 1], a, b)))
    return None


def sokbredd(rows, id_):
    start, goal = A.parse(rows)
    b, d = A.bfs(rows), A.dfs(rows)
    nb, nd = len(b["order"]), len(d["order"])
    lb, ld = len(b["path"]) - 1, len(d["path"]) - 1
    if id_ in ("1.105", "1.106"):
        avstand = A.dist_all(rows, start)
        lager = [sum(v == n for v in avstand.values()) for n in range(lb + 1)]
        return (
            "Rita en ring runt alla rutor på samma avstånd från start. Hur ändras ringarnas storlek på andra sidan mitten?",
            f"Från {A.cname(start)} till {A.cname(goal)} innehåller avståndslagren {', '.join(map(str, lager))} rutor. "
            "Fram till mitten växer nästa lager. Efter mitten begränsar rutnätets kanter hur många nya rutor kön kan få.",
        )
    if id_ in ("1.18", "1.99"):
        omvand = A.dfs(rows, order=A.STD[::-1])
        forgrening = vagval(d["path"], omvand["path"])
        extra = (
            f" Vägarna delar sig vid {forgrening[0]} och fortsätter till {forgrening[1]} respektive {forgrening[2]}."
            if forgrening
            else ""
        )
        return (
            "Pröva att vända DFS grannordning från ↑ → ↓ ← till ← ↓ → ↑. Påverkas besöksordningen, vägen eller båda?",
            f"Med ↑ → ↓ ← besöker DFS {nd} rutor och hittar en väg på {ld} steg. Med ← ↓ → ↑ blir det {len(omvand['order'])} besök och {len(omvand['path']) - 1} steg.{extra}",
        )
    forgrening = vagval(b["path"], d["path"])
    for i, (x, y) in enumerate(zip(b["order"], d["order"]), 1):
        if x != y:
            bryt = f"Vid besök {i} tar BFS ut {A.cname(x)} ur kön medan DFS besöker {A.cname(y)}."
            break
    else:
        bryt = "Metoderna följer samma besöksordning tills den första når målet."
    if forgrening:
        plats, bval, dval = forgrening
        fraga = f"Följ vägarna från {plats}. Vilken gren ingår i BFS-vägen och vilken ingår i DFS-vägen?"
        skillnad = f"BFS-vägen fortsätter genom {bval}, DFS-vägen genom {dval}."
    elif nd != nb:
        fraga = "För bok över rutorna fram till mål med BFS och DFS. Vilken metod undersöker färre rutor när båda prövar ↑ → ↓ ←?"
        skillnad = bryt
    else:
        fraga = "Markera rutorna som undersöks och ringa sedan in själva vägen. Hur mycket arbete gör sökningarna utanför vägen?"
        skillnad = f"BFS tar ut {nb - lb - 1} rutor utanför sin slutliga väg. För DFS är antalet {nd - ld - 1}."
    return (
        fraga,
        f"{skillnad} BFS tar ut {nb} rutor och hittar en väg på {lb} steg. DFS besöker {nd} rutor och hittar en väg på {ld} steg. Start och mål ingår i båda antalen.",
    )


def prioriteter(rows, algoritm):
    start, goal = A.parse(rows)
    kostnad, oppna = {start: 0}, {start}
    for n in algoritm(rows)["order"]:
        yield n, {c: kostnad[c] for c in oppna}
        oppna.remove(n)
        for c in A.neigh(rows, n):
            alt = kostnad[n] + A.cost(rows, c)
            if c not in kostnad or (algoritm is A.astar and alt < kostnad[c]):
                oppna.add(c)
                kostnad[c] = alt


def exempel(u, rows, mark):
    start, goal = A.parse(rows)
    id_, familj = u["id"], u["familj"]
    h = lambda c: A.manhattan(c, goal)
    if familj in ("BFS i labyrinter", "DFS i labyrinter") and id_ != "1.104":
        return sokbredd(rows, id_)
    if id_ in kartval() and 173 <= int(id_.split(".")[1]) <= 188:
        kandidater = set(mark.values())
        tidigare = None
        for n, oppna in prioriteter(rows, A.greedy):
            if set(oppna) == kandidater:
                namn = {c: b for b, c in mark.items()}
                vinnare = min(oppna, key=lambda c: (oppna[c] + h(c), h(c), A.cname(c)))
                if len(oppna) == 2:
                    return (
                        f"Följ girig bäst först tills {A.cname(tidigare)} har tagits ut och dess grannar har lagts in. Vad händer om du byter från girig bäst först till A* just där?",
                        f"Med den givna listan väljer girig bäst först {namn[n]} ({A.cname(n)}) med h({namn[n]}) = {h(n)}. A* väljer {namn[vinnare]} ({A.cname(vinnare)}) med f({namn[vinnare]}) = {oppna[vinnare]} + {h(vinnare)} = {oppna[vinnare] + h(vinnare)}. Den andra kandidatens f-värde är {oppna[n] + h(n)}.",
                    )
                return (
                    f"Spåra girig bäst först tills grannarna till {A.cname(tidigare)} har lagts in. Hur rangordnas de tre kandidater som då ligger öppna?",
                    "I ordning efter h-värde ligger "
                    + ", ".join(
                        f"{namn[c]} ({A.cname(c)}, h = {h(c)})"
                        for c in sorted(oppna, key=h)
                    )
                    + f". Nästa uttag blir {A.cname(n)}.",
                )
            tidigare = n
        raise ValueError(f"{id_}: kandidaterna förekommer aldrig samtidigt")
    a, g = A.astar(rows), A.greedy(rows)
    pa, pg = a["path"], g["path"]
    ca, cg = A.path_cost(rows, pa), g["cost"]
    la, lg = len(pa) - 1, len(pg) - 1
    kostkarta = any(ch.isdigit() for row in rows for ch in row)
    if ca < cg and (kostkarta or familj != "g, h och f för en ruta"):
        gren, av, gv = vagval(pa, pg)
        ordval = (
            "räkna både steg och kostnad" if kostkarta else "räkna stegen till målet"
        )
        return (
            f"Följ de två vägarna från {gren} och {ordval}. Vilken fortsättning får girig bäst först respektive A*?",
            f"Vid {gren} går den väg som girig bäst först hittar genom {gv}. Den har {lg} steg och kostar {cg}. A*:s väg går genom {av}, har {la} steg och kostar {ca}.",
        )
    if kostkarta:
        # En lokaliserad kostnad visar vad en enskild terrängruta gör med ett vägval.
        terrang = [
            (r, c)
            for r, row in enumerate(rows)
            for c, ch in enumerate(row)
            if ch.isdigit()
        ]
        for c in sorted(terrang, key=lambda c: (c not in pg, c)):
            r, k = c
            vanliga = rows.copy()
            vanliga[r] = rows[r][:k] + "." + rows[r][k + 1 :]
            billig, _ = A.ucs_grid(vanliga)
            if billig < ca:
                return (
                    f"Pröva att göra {A.cname(c)} till en vanlig gångruta. Hur förändras den lägsta möjliga kostnaden till mål?",
                    f"Det kostar {A.cost(rows, c)} att gå in i {A.cname(c)}. Med kartans terräng är lägsta kostnaden {ca}. När just den rutan kostar 1 blir lägsta kostnaden {billig}.",
                )
        vana = A.bfs(rows)["path"]
        terr = next((c for c in vana[1:] if A.cost(rows, c) > 1), terrang[0])
        via = A.bfs(rows, start=start, goal=terr)["path"]
        return (
            f"Summera priset på färden från start till {A.cname(terr)} längs en väg med så få steg som möjligt. Hur mycket av kostnaden kommer från terrängen?",
            f"En sådan väg är {' → '.join(map(A.cname, via))}. Den har {len(via) - 1} steg och kostar {A.path_cost(rows, via)}. Att gå in i {A.cname(terr)} kostar {A.cost(rows, terr)}.",
        )
    if mark and familj in ("g, h och f för en ruta", "Heuristiken h"):
        avstand = A.dist_all(rows, goal)
        ds = A.dist_all(rows, start)
        namn, c = max(
            mark.items(),
            key=lambda x: (
                avstand[x[1]] - h(x[1]),
                ds[x[1]] - A.manhattan(start, x[1]),
            ),
        )
        rest = avstand[c]
        if len(mark) > 1 and familj == "g, h och f för en ruta":
            kandidater = sorted(mark.items(), key=lambda x: (h(x[1]), x[0]))
            par = next(
                (
                    (i, j)
                    for i in kandidater
                    for j in kandidater
                    if h(i[1]) < h(j[1]) and ds[i[1]] + h(i[1]) >= ds[j[1]] + h(j[1])
                ),
                None,
            )
            if par:
                (x, px), (y, py) = par
                return (
                    f"Jämför {x} och {y} som tänkbara nästa rutor. Räcker det att välja den som ser ut att ligga närmast målet?",
                    f"{x} har h({x}) = {h(px)} och f({x}) = {ds[px]} + {h(px)} = {ds[px] + h(px)}. För {y} blir h({y}) = {h(py)} och f({y}) = {ds[py]} + {h(py)} = {ds[py] + h(py)}. "
                    + (
                        f"Girig bäst först föredrar {x}. Med dessa vägkostnader ger A* företräde åt {y}."
                        if ds[px] + h(px) > ds[py] + h(py)
                        else f"Girig bäst först väljer {x}. A* får lika f-värden och behöver då regeln om lägst h."
                    ),
                )
        if ds[c] > A.manhattan(start, c) and int(id_.split(".")[1]) % 2 == 0:
            rak = A.manhattan(start, c)
            return (
                f"Rita vägen från start till {namn} ({A.cname(c)}). Var på vägen tvingar en vägg dig att lämna den raka rutvägen?",
                f"Utan väggar skulle {rak} steg räcka. En kortaste gångväg är {' → '.join(map(A.cname, A.bfs(rows, goal=c)['path']))}. Den har {ds[c]} steg, alltså {ds[c] - rak} extra.",
            )
        return (
            f"Stanna vid {namn} ({A.cname(c)}). Uppskatta först hur långt det är kvar och följ sedan en kortaste gångväg till målet.",
            f"Från {A.cname(c)} ger rad- och kolumnskillnaden h({namn}) = {h(c)}. En kortaste fortsättning är {' → '.join(map(A.cname, A.bfs(rows, start=c, goal=goal)['path']))}, alltså {rest} steg. "
            + (
                f"Väggarna gör vägen {rest - h(c)} steg längre än uppskattningen."
                if rest > h(c)
                else "Här går det att nå målet utan ett enda steg bort från det, så uppskattningen är exakt."
            ),
        )
    for v, oppna in prioriteter(rows, A.astar):
        for w in sorted(oppna):
            if w != v and oppna[v] + h(v) == oppna[w] + h(w) and h(v) < h(w):
                return (
                    f"Jämför {A.cname(v)} och {A.cname(w)} när båda ligger öppna. Vilken regel avgör nästa uttag med A*?",
                    f"Båda har f-värdet {oppna[v] + h(v)}. {A.cname(v)} har h-värdet {h(v)} och {A.cname(w)} har {h(w)}. Regeln om lägst h vid lika f ger uttaget {A.cname(v)}.",
                )
    return (
        "Jämför hur mycket av kartan BFS och A* söker igenom på väg till mål. Markera gärna de rutor som bara BFS tar ut.",
        f"På den här kartan tar BFS ut {len(A.bfs(rows)['order'])} rutor och A* tar ut {len(a['order'])}. En kortaste väg har {la} steg. I jämförelsen räknas både start och mål.",
    )


def vagbild(rows, jamfor_djup):
    """Två kartor med samma orientering. På sökkartorna syns även besök utanför vägen."""
    start, mal = A.parse(rows)
    par = (
        (("BFS", A.bfs(rows)), ("DFS", A.dfs(rows)))
        if jamfor_djup
        else (("Girig bäst först", A.greedy(rows)), ("A*", A.astar(rows)))
    )
    bredd, hojd = len(rows[0]) * 22 + 22, len(rows) * 22 + 22
    block = []
    for metod, sokning in par:
        path = sokning["path"]
        besok = set(sokning["order"])
        steg = len(path) - 1
        matt = (
            f"{len(besok)} undersökta rutor"
            if jamfor_djup
            else f"kostnad {A.path_cost(rows, path)}"
        )
        titel = f"{metod} · {steg} steg · {matt}"
        lager = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {bredd} {hojd}" style="display:block;width:100%;height:auto" role="img" aria-label="{titel}"><title>{titel}</title>'
        ]
        siffror = []
        for c in range(len(rows[0])):
            lager.append(
                f'<text x="{29 + 22 * c}" y="12" text-anchor="middle" font-size="10">{c + 1}</text>'
            )
        for r, row in enumerate(rows):
            lager.append(
                f'<text x="8" y="{33 + r * 22}" text-anchor="middle" font-size="10">{chr(65 + r)}</text>'
            )
            for c, ch in enumerate(row):
                x, y = 18 + c * 22, 18 + r * 22
                fyll = {
                    "#": "#334155",
                    "3": "#d6b98c",
                    "4": "#c4d7ef",
                    "5": "#f4ba88",
                }.get(ch, "#fff")
                if jamfor_djup and (r, c) in besok:
                    fyll = "#cde8ed"
                if (r, c) in (start, mal):
                    fyll = "#22a05a" if (r, c) == start else "#d94343"
                lager.append(
                    f'<rect x="{x}" y="{y}" width="21" height="21" rx="2" fill="{fyll}" stroke="#64748b" stroke-width=".65"/>'
                )
                if ch.isdigit():
                    siffror.append(
                        f'<text x="{x + 17}" y="{y + 8}" text-anchor="middle" font-size="8" font-weight="bold">{ch}</text>'
                    )
        punkter = " ".join(f"{28 + c * 22},{28 + r * 22}" for r, c in path)
        lager.append(
            f'<polyline points="{punkter}" fill="none" stroke="#183659" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>'
        )
        block.append(
            '<div style="flex:1 1 155px;max-width:235px"><strong style="display:block">'
            + metod
            + f'</strong><span style="display:block">{steg} steg · {matt}</span>'
            + "".join(lager + siffror)
            + "</svg></div>"
        )
    led = (
        "Den mörka linjen visar vägen till mål. Ljusblå rutor undersöktes under sökningen."
        if jamfor_djup
        else "Den mörka linjen visar vägen till mål. Siffrorna anger kostnaden för att gå in i terrängrutorna."
    )
    return (
        '<figure class="labyrintvagar" style="margin:0.65em 0;color:#162438;background:#fff;padding:0.6em"><div style="display:flex;flex-wrap:wrap;gap:1em">'
        + "".join(block)
        + "</div><figcaption>"
        + led
        + "</figcaption></figure>"
    )


def tillampning(u):
    intro = u["spelIntro"]
    if "Labyrint med" not in intro:
        return
    svg = re.search(r"<svg.*?</svg>", intro)[0]
    rows, mark = las_karta(svg)
    fraga, svar = exempel(u, rows, mark)
    # Tillämpningen visas i facit, där eleven först kan pröva den på samma karta.
    # Native details fungerar även i fristående HTML. Pappersfacit har svaret utskrivet.
    fokus = fraga
    if u["id"] in kartval() and u["familj"] == "Heuristiken h":
        fokus += " Vid lika h väljs den ruta som kommer först i bokstavsordning."
    elif (
        any(ch.isdigit() for row in rows for ch in row) and "girig bäst först" in fraga
    ):
        fokus += " Girig bäst först sorterar efter h och därefter rutnamn. A* sorterar efter f, sedan h och sist rutnamn."
    prompt = '<p class="labyrintfokus">Att fundera på. ' + fokus + "</p>"
    gammal = re.sub(r'<p class="labyrintfokus">.*?</p>', "", intro)
    nytt = gammal + prompt
    assert intro in u["t"], u["id"]
    u["t"] = u["t"].replace(intro, nytt, 1)
    u["spelIntro"] = nytt
    inledning = '<p class="labyrintprov"><strong>Pröva på kartan.</strong> '
    deltext = (
        inledning
        + fraga
        + '</p><details class="labyrintforklaring"><summary>Visa förklaring</summary><p>'
        + svar
        + "</p></details>"
    )
    papper = inledning + fraga + '</p><p class="labyrintforklaring">' + svar + "</p>"

    djup = u["id"] in kartval() and u["kap"] == 1
    kost = any(ch.isdigit() for row in rows for ch in row)
    bild = (
        vagbild(rows, djup)
        if djup or (kost and A.greedy(rows)["cost"] > A.ucs_grid(rows)[0])
        else ""
    )

    def placera(html, block):
        html = re.sub(r'<figure class="labyrintvagar".*?</figure>', "", html)
        html = re.sub(
            r'<p class="labyrintprov">.*?</p>(?:<details class="labyrintforklaring">.*?</details>|<p class="labyrintforklaring">.*?</p>)',
            "",
            html,
        )
        svar = list(re.finditer(r'<p class="facit-svar">.*?</p>', html))
        assert svar, u["id"]
        pos = svar[-1].end()
        return html[:pos] + block + html[pos:]

    for d in u["spelDelar"]:
        text = (
            deltext.replace("</details>", bild + "</details>")
            if d is u["spelDelar"][-1]
            else deltext
        )
        d["s"] = placera(d["s"], text)
    u["s"] = placera(u["s"], papper + bild)
