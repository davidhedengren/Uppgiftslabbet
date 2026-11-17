"""Räkna kandidatmönster per 10 000 ord i bank (t) och lärarkorpus."""
import json, re, collections, sys
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from jamfor import ord_

M = {
    # flerval och svarsinstruktioner
    "Välj ett alternativ": r"[Vv]älj ett alternativ",
    "Markera det korrekta alternativet": r"[Mm]arkera det korrekta alternativet",
    "Vilket alternativ": r"[Vv]ilket alternativ",
    "Du kan svara med": r"[Dd]u kan svara med",
    "Skriv svaret som ett vanligt tal": r"vanligt tal, inte i tiopotensform",
    "(Svara i …)": r"\(Svara i [^)]{1,15}\)",
    "Svara i … (utan parentes)": r"(?<!\()Svara i ",
    "Svara med ett ord/tal": r"[Ss]vara med (ett|en) (ord|tal|heltal)",
    "Avrunda till …": r"[Aa]vrunda (till|vid)",
    # fysikens konstruktioner
    "<sak> på <tal> kg": r"\b(?:[a-zåäö]+) på [\d ,]+ ?(?:kg|g|ton|N|J|W|V|Ω|A|nC|µC|C)\b",
    "med massan": r"med massan",
    "som väger": r"som väger|väger [\d]",
    "vågrät/lodrät": r"\b(vågrät|lodrät)",
    "horisontell/vertikal": r"\b(horisontell|vertikal)",
    "från vila": r"från vila",
    "från stillastående/stillastående": r"stillastående|från stillhet|i vila",
    "positiv riktning/räknas som positiv": r"positiva? riktning|räknas som positiv",
    "med tecken": r"med tecken",
    "andra krafters impuls / den korta stöten": r"krafters impuls|den korta stöten",
    "Behandla … som / i en förenklad modell": r"Behandla [^.]* som|förenklad modell|[Mm]odellera?s? ",
    "formel i frågan (X-lag:/-ekvationen:)": r"(lag|ekvationen|formeln|samband(et)?)\s*:\s",
    # allmän AI-prosa
    "tankstreck – eller —": r" [–—] ",
    "kolon mitt i fråga": r"[a-zåäö] ?: [A-ZÅÄÖa-zåäö]",
    "Anta/Antag att": r"\bAnta(g)? att",
    "Antag att": r"\bAntag att",
    "Anta att": r"\bAnta att",
    "Bortse från": r"[Bb]ortse från",
    "En elev säger/påstår/menar": r"[Ee]n elev (säger|påstår|menar|tänker|hävdar|skriver)",
    "Bedöm/Avgör om påståendet": r"(Bedöm|Avgör om) påståendet",
    "respektive": r"respektive",
    "exakt (ord)": r"\bexakt\b",
    "sammanlagda/sammanlagt": r"sammanlag",
    "i stället": r"i stället",
    "Hur stor/Hur stort": r"\bHur stor",
    "Beräkna": r"\bBeräkna\b",
    "Bestäm": r"\bBestäm\b",
    "Hur mycket": r"\bHur mycket",
    "Vilken/Vilket/Vilka": r"\bVilk(en|et|a)\b",
    "Motivera": r"[Mm]otivera",
    "Förklara": r"[Ff]örklara",
    "Visa att": r"\bVisa att",
    "figuren nedan / se figur": r"[Ff]iguren nedan|[Ss]e figur|figuren nedan",
    "figuren visar / i figuren": r"[Ff]iguren visar|[Ii] figuren",
    "Tabellen visar": r"[Tt]abellen visar",
    "digitalt verktyg": r"digitalt? verktyg",
    "skall": r"\bskall\b",
    "ungefär": r"\bungefär\b",
    "rimlig": r"\brimlig",
    "detaljer/uppsättning/scenario": r"\b(uppsättning|scenario|scenariot)\b",
    "Två tal …: X och X": r": X (och|,) X",
}

def raknare(texter):
    tot = sum(len(ord_(t)) for t in texter)
    c = {}
    for n, rx in M.items():
        r = re.compile(rx)
        c[n] = sum(len(r.findall(t)) for t in texter)
    return tot, c

if __name__ == "__main__":
    k = json.load(open('korpus.json', encoding='utf-8'))
    k = [x for x in k if not x['skapad'].startswith('2026') and '2026' not in x['fil']]
    kt = [p for x in k for p in x['text']]
    b = json.load(open('bank_t.json', encoding='utf-8'))
    bt = list(b.values())
    kw, kc = raknare(kt)
    bw, bc = raknare(bt)
    print(f"{'mönster':45s} {'bank':>6s} {'/10k':>6s} {'korpus':>6s} {'/10k':>6s}")
    for n in M:
        print(f"{n:45s} {bc[n]:6d} {bc[n]/bw*1e4:6.1f} {kc[n]:6d} {kc[n]/kw*1e4:6.1f}")
