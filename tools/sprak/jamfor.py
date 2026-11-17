"""Jämför ordförråd och fraser i bankernas uppgiftstexter mot lärarens egen korpus."""
import json, re, math, collections, sys, os, html as H

UL = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
BANKER = {"fy1": "uppgifter.js", "fy2": "uppgifter2.js", "ma1": "uppgifterma1.js", "ma2": "uppgifterma2.js",
          "mato1": "uppgiftermato1.js", "mato2": "uppgiftermato2.js", "matf1": "uppgiftermatf1.js"}


def las_bank(fil):
    s = open(UL + "\\" + fil, encoding="utf-8", newline="").read()
    i = s.index("[")
    arr, _ = json.JSONDecoder().raw_decode(s[i:])
    return arr


def rensa(t):
    t = re.sub(r"<svg.*?</svg>", " ", t, flags=re.S)
    t = re.sub(r"<table.*?</table>", " ", t, flags=re.S)
    t = re.sub(r"\\\(.*?\\\)|\\\[.*?\\\]|\$\$.*?\$\$", " X ", t, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    t = H.unescape(t)
    return re.sub(r"\s+", " ", t).strip()


def ord_(t):
    return re.findall(r"[a-zåäöéü]+", t.lower())


def ngram(ws, n):
    return [" ".join(ws[i:i + n]) for i in range(len(ws) - n + 1)]


if __name__ == "__main__":
    korpus = json.load(open(sys.argv[1], encoding="utf-8"))
    korpus = [k for k in korpus if not k["skapad"].startswith("2026") and "2026" not in k["fil"]]
    ktxt = [p for k in korpus for p in k["text"]]
    bank = {}
    for kod, fil in BANKER.items():
        for u in las_bank(fil):
            bank[(kod, u["id"])] = rensa(u.get("t", ""))
    json.dump({f"{k[0]}|{k[1]}": v for k, v in bank.items()}, open("bank_t.json", "w", encoding="utf-8"),
              ensure_ascii=False)
    res = {}
    for n in (1, 2, 3):
        kc = collections.Counter(g for p in ktxt for g in ngram(ord_(p), n))
        bc = collections.Counter(g for t in bank.values() for g in ngram(ord_(t), n))
        ks, bs = sum(kc.values()), sum(bc.values())
        rad = []
        for g, b in bc.items():
            if b < 25:
                continue
            k = kc.get(g, 0)
            lr = math.log2(((b + .5) / bs) / ((k + .5) / ks))
            rad.append((lr, g, b, k))
        rad.sort(reverse=True)
        res[n] = rad[:250]
        print(f"=== {n}-gram (bank ord {bs}, korpus ord {ks})")
        for lr, g, b, k in rad[:120]:
            print(f"{lr:5.1f} {b:6d} {k:4d}  {g}")
    json.dump(res, open("overrep.json", "w", encoding="utf-8"), ensure_ascii=False)
