"""Slutredigering av AI-bankens publicerade elevkort och motsvarande pappersfrågor."""

import re
import json
from heapq import heappop, heappush

CELL = re.compile(
    r'<rect (?:data-cell="[A-Z]\d+" )?x="(\d+)" y="(\d+)" width="(?:52|38)" height="(?:52|38)" fill="(#[a-f0-9]+)"[^>]*/>'
)
TERRAIN = {"#d6b98c": 3, "#c4d7ef": 4, "#f4ba88": 5}
WALL = "#334155"
NOTE = "(h(n) är Manhattanavståndet till målet)"
REMOVED = " Varje gång läggs en nods barn in i en datastruktur när noden tas ut."
DIRECTIONS = ((0, -1), (1, 0), (0, 1), (-1, 0))


def weighted(u):
    return any(m[3] in TERRAIN for m in CELL.finditer(u["spelIntro"]))


def distances(grid, start):
    todo = [(0, start)]
    best = {start: 0}
    while todo:
        g, pos = heappop(todo)
        if g != best[pos]:
            continue
        for dx, dy in DIRECTIONS:
            q = pos[0] + dx, pos[1] + dy
            if grid.get(q, WALL) == WALL:
                continue
            cost = g + TERRAIN.get(grid[q], 1)
            if cost < best.get(q, float("inf")):
                best[q] = cost
                heappush(todo, (cost, q))
    return best


def corridors(u, svg):
    if "data-gangar" in svg or u["id"] in ("1.105", "1.106"):
        return svg
    cells = [
        m
        for m in CELL.finditer(svg)
        if m[3] in {*TERRAIN, WALL, "#fff", "#22a05a", "#d94343"}
        and ("data-cell=" in m[0] or 'width="52"' in m[0])
    ]
    if not cells:
        return svg
    x0, y0 = int(cells[0][1]), int(cells[0][2])
    size = int(re.search(r'width="(\d+)"', cells[0][0])[1])

    def coord(m):
        return (int(m[1]) - x0) // size, (int(m[2]) - y0) // size

    grid = {coord(m): m[3] for m in cells}
    # Behåll varje cell som nämns i uppgift, facit, ledtråd eller återkoppling.
    words = re.sub(r"<svg.*?</svg>", "", json.dumps(u, ensure_ascii=False))
    keep = {
        (int(c) - 1, ord(r) - 65) for r, c in re.findall(r"\b([A-Z])(\d+)\b", words)
    }
    for x, y in re.findall(
        r'<rect x="(\d+)" y="(\d+)" width="\d+" height="\d+" fill="#fff3b0"', svg
    ):
        keep.add(((int(x) - x0) // size, (int(y) - y0) // size))
    keep.update(pos for pos, color in grid.items() if color not in ("#fff", WALL))
    # För värdefrågorna kan vi stänga hela rutor om samtliga relevanta avstånd består.
    # För kö- och spårningsfrågor måste även ordningen i sökningen bestå.
    if u["familj"] == "g, h och f för en ruta":
        start = next(k for k in grid if grid[k] == "#22a05a")
        old = distances(grid, start)
        goal = next(k for k in grid if grid[k] == "#d94343")
        from_goal = distances(grid, goal)
        for pos in set(grid) - set(old) - keep:
            if grid[pos] == "#fff":
                grid[pos] = WALL

        def rooms(pos):
            x, y = pos
            return sum(
                all(
                    grid.get((i + dx, j + dy), WALL) != WALL
                    for dx, dy in ((0, 0), (1, 0), (0, 1), (1, 1))
                )
                for i in (x - 1, x)
                for j in (y - 1, y)
            )

        for pos in sorted(set(grid) - keep, key=lambda p: (-rooms(p), p)):
            if grid[pos] != "#fff" or not rooms(pos):
                continue
            grid[pos] = WALL
            new = distances(grid, start)
            to_goal = distances(grid, goal)
            if any(
                new.get(k) != old.get(k) or to_goal.get(k) != from_goal.get(k)
                for k in keep
            ) or set(new) != set(old) - {pos}:
                grid[pos] = "#fff"
            else:
                old = new
    replacements = {
        m[0]: m[0].replace('fill="' + m[3] + '"', 'fill="' + grid[coord(m)] + '"')
        for m in cells
    }
    svg = CELL.sub(lambda m: replacements.get(m[0], m[0]), svg)
    # Rita golvet som gångar med en öppning mitt på varje passerbar sida.
    # Rutcentrum, markerade rutor och avståndet mellan två grannar är oförändrade.
    walls = []
    for m in cells:
        col, row = coord(m)
        if grid[col, row] == WALL:
            continue
        x, y = int(m[1]), int(m[2])
        edge = size // 4
        far = size - edge
        middle = size - 2 * edge
        for dx, dy in ((0, 0), (far, 0), (0, far), (far, far)):
            walls.append(f"M{x + dx} {y + dy}h{edge}v{edge}h-{edge}z")
        for dx, dy, xx, yy, w, h in (
            (0, -1, edge, 0, middle, edge),
            (1, 0, far, edge, edge, middle),
            (0, 1, edge, far, middle, edge),
            (-1, 0, 0, edge, edge, middle),
        ):
            if grid.get((col + dx, row + dy), WALL) == WALL:
                walls.append(f"M{x + xx} {y + yy}h{w}v{h}h-{w}z")
    # En gemensam kontur för väggarnas kanter och hörn.
    return svg.replace(
        "</svg>",
        f'<path data-gangar="1" pointer-events="none" fill="{WALL}" d="{" ".join(walls)}"/></svg>',
    )


INTROS = {
    "Spelträdet söks igenom med minimax.": [
        "Utgå från slutlägena. Vilka värden förs upp genom trädet när båda spelarna använder minimax?",
        "Analysera spelarnas val med minimax. Läs poängen i löven ur MAX:s perspektiv.",
        "Börja i den nedersta förgreningen och arbeta mot roten med minimax.",
    ],
    "Spelträdet söks igenom med alfa–beta-beskärning (vänster gren först).": [
        "Följ alfa–beta från vänster till höger. Håll reda på vilka slutlägen sökningen faktiskt behöver läsa.",
        "Undersök den vänstra grenen först. Fortsätt genom trädet med alfa–beta-beskärning.",
        "Gå igenom dragen från vänster till höger med alfa–beta. Använd gränserna från de drag som redan har prövats.",
    ],
    "Labyrinten söks igenom med BFS (ordning ↑ → ↓ ←).": [
        "Följ kön från den gröna startrutan. BFS prövar grannarna i ordningen ↑ → ↓ ←.",
        "Utgå från start och spåra BFS genom gångarna. Pröva upp, höger, ned och vänster i den ordningen.",
    ],
    "Labyrinten söks igenom med DFS (ordning ↑ → ↓ ←).": [
        "Spåra DFS från start. Vid varje vägval prövas gångarna i ordningen ↑ → ↓ ←.",
        "Följ en gren i taget med DFS. Grannordningen är upp, höger, ned, vänster.",
    ],
    "Maskininlärning delas ofta in i övervakad inlärning (klassificering eller regression), oövervakad inlärning och förstärkningsinlärning.": [
        "Undersök hur träningen går till i varje exempel. Finns det ett känt svar, söker modellen grupper eller får den återkoppling på en handling?",
        "Utgå från materialet som modellen lär sig av. Skilj mellan klassificering, regression, oövervakad inlärning och förstärkningsinlärning.",
        "Jämför uppgifterna nedan. Vilken sorts svar söker man, och vilken information finns tillgänglig under träningen?",
    ],
}
QUESTIONS = {
    "g": [
        "Vilken är den lägsta kostnaden från start till {L}? Ange g({L}).",
        "Följ den billigaste vägen fram till {L}. Vad blir g({L}) där?",
        "Vad kostar det som minst att nå {L} från start? Svara med g({L}).",
    ],
    "h": [
        "Utgå från {L} och räkna avståndet till målet med heuristiken. Vad blir h({L})?",
        "Vilket h-värde får A* för {L}? Ange h({L}).",
        "Vilket avstånd uppskattar heuristiken från {L} till mål? Ange h({L}).",
    ],
    "f": [
        "Vilket prioritetsvärde får {L} i A*? Svara med f({L}).",
        "Lägg ihop vägkostnaden till {L} och heuristiken där. Vad blir f({L})?",
        "När {L} jämförs med andra rutor använder A* ett f-värde. Beräkna f({L}).",
    ],
}


BRIEFS = [
    "På lagrets karta är {L} den sista kontrollpunkten före en hylla. Fyll i de tre värden som A* behöver för kontrollpunkten.",
    "Dammsugaren har två avstånd i sin logg. Det ena gäller vägen från laddaren till {L}, det andra uppskattar hur långt det är kvar. Återskapa loggen för A*.",
    "Musen ser osten genom en springa men måste följa gångarna. Läs kartan ur två perspektiv när A* bedömer {L}.",
    "Spelets kartredigerare visar var leran ligger. Kontrollera hur terrängen påverkar de värden A* sätter på {L}.",
    "En elev räknar fågelvägen från garaget till {L}. Gräsklipparen måste köra runt väggarna. Vilka tal ska egentligen stå i klipparens A*-logg?",
    "Sjukhusets transportrobot kan ta sig fram olika fort på olika underlag. Beräkna vad A* har att gå på när den bedömer {L} på väg till avdelningen.",
    "En drönare flyger bara längs lagergångarna. Beräkna en rad i dess sökprotokoll för A*, från start via kontrollpunkten {L} mot utgången.",
    "Räddningsrobotens operatör ser kartan men inte värdena för {L}. Återskapa beräkningen med A* och kartans inträdeskostnader.",
    "En tränare har markerat {L} på hinderbanan. Använd A* för att skilja den kortaste vägen dit från uppskattningen av återstoden.",
    "Truckens planeringssystem har sparat kartan men tappat siffrorna för {L}. Rekonstruera g, h och f för den rutan med A*.",
    "Maten ska från köket till bordet. För att jämföra gångarna i restaurangen räknar A* ut ett värde för {L}. Ta fram underlaget för jämförelsen.",
    "Inför robotfinalen kontrollerar domaren hur banans olika underlag räknas. Granska A*-värdena för {L}.",
    "Bagagevagnen får bara svänga mellan gångarna på kartan. Visa hur A* skulle bedöma {L} på vägen ut till planet.",
    "Brandrobotens karta anger kostnaden för att köra in i varje typ av ruta. Använd den för att fylla i den saknade raden {L} i A*-loggen.",
    "I växthuset löper gångarna mellan odlingsbäddarna. Bestäm vilka värden A* använder vid {L} när roboten ska fram till plantan.",
    "I parkeringshuset kan två lika långa färdvägar kosta olika mycket. Utred den markerade rutan {L} med A*.",
    "En ny order ska skickas till lagerroboten. Innan den kör vill operatören se vad A* räknar fram för {L}.",
    "Laddstationen är start och hallen är mål. Läs av vad som redan måste köras för att nå {L} och vad A* uppskattar därifrån.",
    "Markeringen {L} sitter i en gång på musens väg till osten. Spåra gångarna från ena hållet och uppskatta avståndet från det andra med A*.",
    "Du testar vägvisningen i ett spel. Kontrollera A* vid {L} innan en spelare släpps in på banan.",
    "Rita med fingret den kortaste körbara vägen från garaget till {L}. Använd sedan kartan för att ta fram värdena för gräsklipparens A*.",
    "På kartan över sjukhuset står bara start, mål och terräng kvar. Beräkna den prioritet som A* skulle ge {L} och delarna som ingår i den.",
    "Utgången ligger på andra sidan hyllorna. Hur ser A*:s beräkning ut för {L} om drönaren utgår från den gröna rutan?",
    "Räddningsledaren behöver skilja kostnaden fram till {L} från uppskattningen av resten av vägen. Använd kartan och A*.",
    "Tänk dig att du står vid {L} på hinderbanan. Titta först tillbaka mot start och sedan mot mål när du tar fram värdena för A*.",
    "Lastkajen är målet. Fyll i truckens planeringsblad för {L} med kostnaden hittills, uppskattningen framåt och A*:s prioritet.",
    "Köket och bordet binds ihop av gångar med räta svängar. Följ A*:s beräkning vid {L} på restaurangens karta.",
    "En tävlingsrobot ska välja bland flera möjliga fortsättningar. Ta fram A*-värdet för {L} utifrån både körkostnaden och avståndet till mål.",
    "Vid incheckningen saknas en rad i bagagevagnens färdplan. Ta fram siffrorna för {L} på samma sätt som A*.",
    "Brandroboten möter underlag med olika kostnad. Analysera {L} från start och från målsidan innan du bestämmer A*:s prioritet.",
]


def revise(u):
    intro = u["spelIntro"]
    new = intro.replace(REMOVED, "")
    ix = int(u["id"].split(".")[1])
    for old, variants in INTROS.items():
        new = new.replace(old, variants[ix % len(variants)])
    for svg in set(re.findall(r"<svg.*?</svg>", new)):
        if "Labyrint" in svg:
            new = new.replace(svg, corridors(u, svg))
    heuristic = "Manhattanavstånd" in new and "h(n)" in new
    if heuristic:
        new = re.sub(
            r" \(h\(n\) = Manhattanavstånd(?: till målet)?, g\(n\) = kortaste vägkostnad från start\)",
            ", där g(n) är den lägsta vägkostnaden från start",
            new,
        )
        new = re.sub(r" \(h\(n\) = Manhattanavstånd(?: till målet)?\)", "", new)
        new = re.sub(
            r"(?:Här är h\(n\) Manhattanavståndet från rutan n till målet och g\(n\) kostnaden|h\(n\) är Manhattanavståndet från rutan n till målet och g\(n\) kostnaden)",
            "g(n) är kostnaden",
            new,
        )
        new = re.sub(
            r",? (?:och|där) h\(n\) är Manhattanavståndet (?:från (?:rutan )?n )?till (?:målet|leveransplatsen)",
            "",
            new,
        )
        new = new.replace(", och den använder Manhattanavståndet som h(n)", "")
        assert "Manhattanavstånd" not in new, u["id"]
    if heuristic and u["kap"] == 2 and 123 <= ix <= 152:
        label = re.search(r"för rutan ([A-Z])", u["spelDelar"][0]["fraga"])[1]
        new = re.sub(
            r"<p>[^<]*A\*[^<]*</p>",
            "<p>" + BRIEFS[ix - 123].format(L=label) + "</p>",
            new,
            count=1,
        )
    assert intro in u["t"] or new == intro, u["id"]
    u["t"] = u["t"].replace(intro, new)
    u["spelIntro"] = new
    for idx, d in enumerate(u["spelDelar"]):
        old = d["fraga"]
        match = re.fullmatch(r"<p>Bestäm ([ghf])\(n\) för rutan ([A-Z])\.</p>", old)
        question = old
        if match and "girig bäst först" not in new:
            k, L = match.groups()
            question = "<p>" + QUESTIONS[k][(ix + idx) % 3].format(L=L) + "</p>"
        paper_question = question
        if heuristic:
            pos = question.find("</p>")
            if pos >= 0:
                question = question[:pos] + " " + NOTE + question[pos:]
            else:
                question += " " + NOTE
        if question != old:
            original = old.removeprefix("<p>").removesuffix("</p>")
            edited = paper_question.removeprefix("<p>").removesuffix("</p>")
            # Pappersbladet har a), b), … och kan ha sina alternativ i följande stycken.
            assert original in u["t"], (u["id"], original)
            u["t"] = u["t"].replace(original, edited, 1)
            d["fraga"] = question
    if heuristic:
        u["t"] += "<p>" + NOTE + "</p>"
