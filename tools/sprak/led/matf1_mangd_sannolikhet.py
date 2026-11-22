# Ma5 mängdlära, Venndiagram och kombinatorisk sannolikhet: egna ledtrådar (2026-11-22).
SNITT = r"Snittet \(A\cap B\) är de element som finns i båda mängderna, och unionen \(A\cup B\) de som finns i minst en av dem."
DIFF = r"\(A\setminus B\) är de element i A som inte finns i B."
KOMPL = r"Komplementet är de element i grundmängden som inte finns i mängden."
LISTA = r"Gå igenom talen ett i taget och kontrollera om de uppfyller villkoret. Se upp med om gränserna ingår."
TVA = r"\(|A\cup B|=|A|+|B|-|A\cap B|\), eftersom snittet annars räknas två gånger."
TRE = r"För tre mängder: \(|A\cup B\cup C|=|A|+|B|+|C|-|A\cap B|-|A\cap C|-|B\cap C|+|A\cap B\cap C|\)."
EXAKT_EN = r"Exakt en av mängderna är unionen minus snittet. Rita gärna ett Venndiagram och fyll i snittet först."
UTAN = r"Antalet i A men inte i B är \(|A|-|A\cap B|\)."
INGEN = r"Dra bort dem som inte tillhör någon mängd från hela gruppen. Då har du \(|A\cup B|\), och sedan ger formeln snittet."
OMR = r"Gå igenom området del för del: ligger det i A, i B, i C, eller utanför? Använd snitt, union, differens och komplement."
KARD = r"Kardinaltalet är antalet element i mängden."
LIKA = r"Sannolikheten är antalet gynnsamma urval delat med antalet möjliga urval. Räkna båda med \(\binom nk\)."
BIN = r"Binomialfördelningen: \(P(X=k)=\binom nk p^k(1-p)^{n-k}\)."
MINST1 = r"Använd komplementet: P(minst en) = 1 − P(ingen)."
L = {
    # ---------- mängdlära ----------
    '1.01': r"Skriv villkoret efter ett lodrätt streck: \(\{x\in\mathbb R\mid\ldots\}\).",
    '1.02': r"\(|n|<4\) betyder att n ligger strikt mellan −4 och 4.",
    '1.03': r"Lista elementen inom klammerparenteser. Finns det några heltal strikt mellan 1 och 2?",
    '1.111': r"Skriv villkoret efter ett lodrätt streck, till exempel med \(n=2k\).",
    '1.112': LISTA, '1.145': r"Skriv \(\{x\in\mathbb Z\mid\ldots\}\) med olikheten efter strecket.",
    '1.482': LISTA,
    '1.483': r"\(A\subset B\) betyder att varje element i A också finns i B.",
    '1.484': KARD, '1.564': KARD, '1.572': r"Den tomma mängden har inga element.",
    '1.574': r"\(A\subset B\) betyder att varje element i A också finns i B.",
    '1.13': OMR, '1.165': OMR,
    # ---------- mängdoperationer ----------
    '1.04': SNITT, '1.06': SNITT + r" Snittet med den tomma mängden är tomt.",
    '1.08': SNITT + " " + KOMPL + " " + DIFF,
    '1.10': r"Bestäm \(A\cup B\) och \(A\cap B\) först, och ta sedan bort snittet från unionen.",
    '1.113': SNITT, '1.114': DIFF + " " + KOMPL,
    '1.146': r"Bestäm \(A\cup B\) och \(A\cap B\) först, och ta sedan bort snittet från unionen.",
    '1.478': SNITT, '1.479': SNITT, '1.480': DIFF,
    '1.568': SNITT, '1.569': SNITT, '1.570': DIFF, '1.571': KOMPL,
    # ---------- Venndiagram ----------
    '1.310': UTAN, '1.320': UTAN, '1.330': UTAN,
    '1.05': r"Läs av antalen i de områden som ingår. \(A\setminus B\) är den del av A som ligger utanför B.",
    '1.312': TRE, '1.322': TRE,
    '1.07': OMR, '1.09': OMR, '1.12': OMR, '1.14': OMR, '1.46': OMR, '1.162': OMR,
    '1.163': OMR + r" Ett område kan ofta skrivas både med differens och med snitt och komplement.",
    '1.115': r"Läs av antalen i varje område och addera de områden som efterfrågas.",
    '1.147': TRE + r" De som inte talar något språk är de som blir kvar av 80.",
    '1.161': r"Läs av vilka element som ligger i varje område.",
    '1.167': r"|A| är summan av alla områden inne i A. Sätt summan lika med 45 och lös ut x.",
    '1.333': TVA,
    '1.170': r"Bestäm \(A\setminus B\) och \(B\setminus A\) och slå ihop dem.",
    '1.335': TVA,
    '1.336': INGEN, '1.348': INGEN, '1.360': INGEN, '1.206': INGEN,
    '1.17': TVA, '1.174': TVA, '1.205': TVA, '1.365': TVA,
    '1.337': EXAKT_EN, '1.349': EXAKT_EN, '1.367': EXAKT_EN, '1.56': EXAKT_EN, '1.175': EXAKT_EN,
    '1.338': TRE, '1.350': TRE, '1.368': TRE, '1.47': TRE, '1.177': TRE,
    '1.18': TRE + r" Unionen är hela gruppen minus de 7 som inte deltar. Lös ut x.",
    '1.339': TRE + r" Lös ut trippelsnittet.", '1.351': TRE + r" Lös ut trippelsnittet.", '1.369': TRE + r" Lös ut trippelsnittet.",
    '1.57': r"De som ligger i exakt två mängder är de parvisa snitten minus de som ligger i alla tre, en gång för varje snitt.",
    '1.166': r"Läs av antalen i diagrammet. Exakt två mängder är de tre områden där två cirklar överlappar utan den tredje.",
    '1.178': TVA + r" Lös ut snittet.",
    '1.207': EXAKT_EN + r" De som inte provar någon är de som blir kvar av 110.",
    '1.485': TVA,
    '1.563': KARD, '1.573': r"Lista heltalen från −1 till 3 och räkna dem.",
    # ---------- kombinatorisk sannolikhet ----------
    '1.35': LIKA + r" För minst 3 rätt delar du upp i 3, 4 och 5 rätt.",
    '1.102': LIKA + r" Om A och B båda väljs ska bara två till väljas bland de övriga åtta.",
    '1.103': LIKA + r" Exakt en defekt betyder 1 av 3 defekta och 3 av 9 hela.",
    '1.104': LIKA, '1.105': LIKA, '1.109': LIKA + r" Exakt 4 rätt betyder 4 av de 6 vinnarnumren och 2 av de 24 övriga.",
    '1.444': MINST1.replace('minst en', 'båda färgerna').replace('ingen', 'bara en färg') + r" Räkna sannolikheten för bara röda och bara blå.",
    '1.128': LIKA, '1.159': LIKA, '1.197': LIKA, '1.198': LIKA, '1.199': LIKA,
    '1.200': LIKA + r" Om Alex väljs ska två till väljas bland de övriga nio.",
    '1.201': LIKA, '1.203': LIKA,
    '1.226': r"Dela upp efter om hjärter kung är med eller inte, och räkna varje fall för sig.",
    '1.548': BIN, '1.549': BIN, '1.550': BIN, '1.556': BIN, '1.557': BIN,
    '1.558': r"Varje kast ger ingen etta med sannolikheten 5/6. Kasten är oberoende.",
    '1.560': LIKA, '1.561': LIKA, '1.562': LIKA,
    '1.679': {'b': BIN + r" Sannolikheten för krona är 1/2."},
    '1.681': {'b': r"Med återläggning är dragningarna oberoende. Multiplicera sannolikheterna för varje dragning."},
    '1.691': MINST1 + r" Ingen av första märket betyder att alla fyra är av det andra.",
    '1.695': {'b': MINST1 + r" Räkna sannolikheten att inget kort är en kung."},
    '1.700': {'b': r"Räkna de gynnsamma utfallen bland de 36. För minst en fyra kan du använda komplementet."},
    '1.703': MINST1 + r" För en tärning är P(ingen sexa) \(=(5/6)^4\), och för två tärningar är P(ingen dubbelsexa) \(=(35/36)^{24}\).",
    '1.707': r"Två skor: hur många av de 11 återstående skorna passar ihop med den första? Fyra skor: räkna sannolikheten att inget par bildas och använd komplementet.",
    '1.708': MINST1 + r" Sannolikheten att alla har olika födelsedag är \(\frac{366}{366}\cdot\frac{365}{366}\cdot\frac{364}{366}\cdots\).",
    '1.714': {'a': BIN + r" Här är \(n=10\) och \(p=1/6\)."},
    '1.717': {'b': MINST1 + r" Varje pil missar med sannolikheten 0,2."},
    '1.719': {'a': BIN + r" Minst 4 givare: räkna komplementet, alltså 0–3 givare."},
    '1.720': {'b': BIN + r" Alla flickor betyder att ingen är pojke."},
    '1.724': {'c': MINST1 + r" Varje person blir sjösjuk med sannolikheten 0,25."},
    '1.726': {'c': BIN + r" Här är \(n=25\) och \(p=0{,}95\)."},
    '1.728': {'b': BIN + r" Här är \(n=13\) och \(p=1/3\)."},
}
