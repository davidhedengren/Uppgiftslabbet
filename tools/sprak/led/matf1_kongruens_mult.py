# Ma5 kongruens och multiplikations- och additionsprincipen: egna ledtrådar (2026-11-22).
MULT = r"Multiplikationsprincipen: multiplicera antalet val i varje steg."
REST = r"Dela med modulen och se vad som blir kvar. Resten ska ligga mellan 0 och modulen minus 1."
BYT = r"Byt varje tal mot dess rest modulo talet först. Räkna sedan med de små resterna."
DEF = r"\(a\equiv b\pmod m\) betyder att \(a-b\) är delbart med m, alltså att a och b ger samma rest vid division med m."


def pot(bas, mod, frag=''):
    return (rf"Beräkna de första potenserna av {bas} modulo {mod} tills resten upprepar sig. "
            rf"Använd sedan mönstret för den stora exponenten.{frag}")


SLUT = r"Slutsiffran är resten modulo 10. Undersök slutsiffrorna i de första potenserna och leta efter ett mönster."
L = {
    # ---------- multiplikations- och additionsprincipen ----------
    '1.171': r"Räkna talen delbara med 3 och med 5 och dra bort dem som är delbara med båda, alltså med 15.",
    '1.172': r"Använd inklusion och exklusion för tre mängder: addera de enskilda, dra bort parvisa snitt och lägg tillbaka trippelsnittet.",
    '1.377': MULT, '1.379': MULT, '1.381': MULT,
    '1.23': MULT, '1.24': MULT + r" Varje position har 10 möjligheter.", '1.25': MULT,
    '1.67': r"Det finns bara n möjliga rester vid division med n. Vad säger lådprincipen om \(n+1\) tal?",
    '1.387': MULT + r" Första siffran har 8 val och varje övrig plats 7.",
    '1.389': MULT + r" Första siffran har 8 val och varje övrig plats 8.",
    '1.39': MULT + r" Läs villkoret för den första bokstaven noga.",
    '1.52': MULT + r" Bokstäverna ska vara olika, så andra bokstaven har ett val mindre.",
    '1.53': MULT,
    '1.54': r"Räkna alla kombinationer och dra bort de förbjudna med chokladbotten.",
    '1.55': r"Första fältet har 5 val. Varje följande fält får inte ha samma färg som fältet bredvid.",
    '1.117': MULT,
    '1.118': MULT,
    '1.130': MULT,
    '1.131': MULT + r" Första siffran har 9 val.",
    '1.132': r"Paketen är av två olika slag. Räkna varje slag med multiplikationsprincipen och addera.",
    '1.148': MULT,
    '1.149': MULT + r" Bokstäverna och siffrorna ska vara olika, så antalet val minskar för varje steg.",
    '1.229': r"Räkna alla sätt att fördela uppgifterna och dra bort dem där någon elev blir utan, med inklusion och exklusion.",
    '1.494': MULT, '1.495': MULT, '1.496': MULT, '1.497': MULT, '1.498': MULT, '1.499': MULT,
    '1.500': MULT + r" Varje kast har 2 utfall.", '1.501': MULT + r" Varje fråga har 2 svar.", '1.502': MULT, '1.503': MULT,
    '1.575': r"Alla fem siffror ska användas en gång, så antalet är \(5!\).",
    '1.576': MULT + r" Varje position har 5 möjligheter.",
    '1.577': r"Ett udda tal måste sluta på en udda siffra. Hur många sådana finns? Fyll sedan de andra platserna.",
    '1.578': MULT + r" Varje position har 29 möjligheter.",
    '1.579': MULT + r" Antalet val minskar med en för varje bokstav.",
    '1.580': MULT,
    '1.581': MULT + r" Jämför antalet koder med antalet skåp.",
    '1.582': MULT + r" Varje fråga har 4 möjligheter.",
    '1.583': MULT + r" Första siffran har 8 val.",
    '1.584': MULT + r" Första siffran har 9 val.",
    '1.585': MULT,
    '1.586': r"Man väljer antingen det ena eller det andra, så antalen ska adderas.",
    '1.730': MULT,
    '1.733': r"Utan upprepning minskar antalet val för varje siffra. Med upprepning har varje position 5 möjligheter.",
    '1.738': MULT + r" Jämför antalet bokstäver i de två fallen.",
    '1.743': r"Mynten kan ordnas på \(4!\) sätt. Varje mynt kan dessutom ligga på 2 sätt.",
    # ---------- kongruens ----------
    '2.387': pot(2, 7),
    '2.19': REST, '2.20': BYT, '2.21': DEF + r" Lägg till eller dra bort multiplar av 9.", '2.22': BYT, '2.23': REST,
    '2.25': DEF, '2.64': REST, '2.87': REST, '2.88': DEF, '2.89': DEF + r" Dra bort 7 tills talet blir negativt.",
    '2.118': DEF + r" Lägg till multiplar av 6.",
    '2.27': BYT, '2.29': BYT + r" För potenserna letar du efter ett mönster i resterna.",
    '2.30': SLUT, '2.121': SLUT,
    '2.57': pot(3, 7) + r" Gör likadant med 5 och addera resterna.",
    '2.65': BYT, '2.90': BYT, '2.91': pot(2, 3), '2.92': BYT,
    '2.93': SLUT,
    '2.119': BYT + r" Om resten blir negativ lägger du till 5.",
    '2.120': r"\(3^2\equiv-1\) och \(4\equiv-1\pmod5\). Vad blir då \(3^{50}\) och \(4^{50}\)?",
    '2.137': r"Lägg till multiplar av 7 till −23 tills du får ett tal mellan 0 och 6.",
    '2.195': REST, '2.196': BYT, '2.197': BYT + r" Byt först 17 mot dess rest.",
    '2.200': r"De två sista siffrorna är resten modulo 100. Beräkna \(3^{10}\) först och kvadrera sedan.",
    '2.318': BYT + r" Byt först 7 mot dess rest.", '2.319': r"\(23\equiv-1\pmod8\). Vad blir då \(23^7\)?",
    '2.320': BYT + r" Byt först 2026 mot dess rest modulo 11.",
    '2.525': REST, '2.526': REST, '2.527': REST, '2.528': REST,
    '2.529': BYT, '2.530': BYT, '2.531': BYT, '2.532': BYT, '2.533': BYT, '2.534': BYT,
    '2.557': REST, '2.558': REST, '2.559': pot(2, 6), '2.560': pot(3, 7),
    '2.561': SLUT, '2.562': SLUT,
    '2.563': BYT, '2.564': BYT, '2.565': BYT,
    '2.566': r"Talet minus 1 ska vara delbart med 3, 5 och 7. Vilket är det minsta sådana tal som är större än 0?",
    '2.567': pot(10, 7),
    '2.568': r"\(10\equiv1\pmod9\). Vad blir då \(10^4\)?",
}
