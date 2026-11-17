"""Gemensamt för språkomskrivningen: läsa bank, minimala textersättningar, figurplatshållare."""
import json, re, os

UL = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
FIL = {"fy1": "uppgifter.js", "fy2": "uppgifter2.js", "ma1": "uppgifterma1.js", "ma2": "uppgifterma2.js",
       "mato1": "uppgiftermato1.js", "mato2": "uppgiftermato2.js", "matf1": "uppgiftermatf1.js"}

FIG = re.compile(r"<svg\b.*?</svg>|<table\b.*?</table>|<img\b[^>]*>", re.S)


def lit(s):
    return json.dumps(s, ensure_ascii=False)


class Bank:
    """Läser arrayen och objektens textspann. Ändringar görs som ersättning av strängliteraler
    inne i objektets spann, så att formatet (kompakt eller indraget) bevaras."""

    def __init__(self, kod):
        self.path = os.path.join(UL, FIL[kod])
        self.src = open(self.path, encoding="utf-8", newline="").read()
        dec, i = json.JSONDecoder(), self.src.index("[") + 1
        self.spann, self.arr = {}, []
        while True:
            while self.src[i] in " \t\r\n,":
                i += 1
            if self.src[i] == "]":
                break
            obj, slut = dec.raw_decode(self.src, i)
            self.spann[obj["id"]] = (i, slut)
            self.arr.append(obj)
            i = slut
        self.byte = {}  # id -> ny objekttext
        self.dubbletter = []

    def obj(self, id_):
        s, e = self.spann[id_]
        return json.loads(self.src[s:e])

    def text(self, id_):
        s, e = self.spann[id_]
        return self.src[s:e]

    def ersatt(self, id_, par, tillagg=()):
        """par: [(gammal sträng, ny sträng)], tillagg: [(efter-sträng, nyckel, värde)]
        där nyckel/värde läggs in direkt efter literalen för efter-sträng (som redan bytts)."""
        txt = self.byte.get(id_, self.text(id_))
        for post in par:
            gammal, ny = post[0], post[1]
            nyckel = post[2] if len(post) > 2 else None
            if gammal == ny:
                continue
            g = lit(gammal)
            if nyckel:  # ankra vid fältnamnet, så att t.ex. en likadan ledtråd inte ändras
                rx = re.compile(re.escape(lit(nyckel)) + r"\s*:\s*" + re.escape(g))
                hits = list(rx.finditer(txt))
                if not hits:
                    raise ValueError(f"{id_}: {nyckel} med texten hittades inte: {gammal[:60]}")
                if len(hits) > 1:
                    self.dubbletter.append(f"{id_}: {len(hits)} lika {nyckel}, första ersatt: {gammal[:50]}")
                m = hits[0]
                start = m.end() - len(g)
                txt = txt[:start] + lit(ny) + txt[m.end():]
                continue
            n = txt.count(g)
            if n == 0:
                raise ValueError(f"{id_}: literalen hittades inte: {gammal[:60]}")
            if n > 1:  # t.ex. två delkort med samma fråga: ersätt första förekomsten (dokumentordning)
                self.dubbletter.append(f"{id_}: {n} lika literaler, första ersatt: {gammal[:50]}")
            txt = txt.replace(g, lit(ny), 1)
        for efter, nyckel, varde in tillagg:
            e = lit(efter)
            if txt.count(e) != 1:
                raise ValueError(f"{id_}: ankaret för {nyckel} hittades {txt.count(e)} gånger")
            pos = txt.index(e) + len(e)
            fore = txt[:txt.index(e)]
            m = re.search(r"(\r?\n[ \t]*)\"[^\"]+\":\s*$", fore)
            if m:  # indraget
                ins = f',{m.group(1)}{lit(nyckel)}: {lit(varde)}'
            else:
                ins = f',{lit(nyckel)}:{lit(varde)}'
            txt = txt[:pos] + ins + txt[pos:]
        json.loads(txt)
        self.byte[id_] = txt

    def spara(self):
        src = self.src
        for id_, (s, e) in sorted(self.spann.items(), key=lambda x: -x[1][0]):
            if id_ in self.byte:
                src = src[:s] + self.byte[id_] + src[e:]
        json.loads(src[src.index("["):src.rindex("]") + 1])
        open(self.path, "w", encoding="utf-8", newline="").write(src)
        return len(self.byte)


def till_platshallare(html):
    figs = []

    def ers(m):
        figs.append(m.group(0))
        return f"[F{len(figs)}]"
    return FIG.sub(ers, html or ""), figs


def fran_platshallare(txt, figs, id_=""):
    anv = [int(x) for x in re.findall(r"\[F(\d+)\]", txt)]
    if sorted(anv) != list(range(1, len(figs) + 1)):
        raise ValueError(f"{id_}: figurplatshållare {anv} men originalet har {len(figs)}")
    return re.sub(r"\[F(\d+)\]", lambda m: figs[int(m.group(1)) - 1], txt)


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"<br\s*/?>", "", s or "")).strip()


def li_lista(t):
    m = re.match(r"^(.*?)<ol\b[^>]*>(.*)</ol>(.*)$", t or "", re.S)
    if not m:
        return None
    lis = re.findall(r"<li>(.*?)</li>", m.group(2), re.S)
    return m.group(1), lis, m.group(3)
