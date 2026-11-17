# Ma1 negativa tal (omr negativa_tal), omskrivet för hand 2026-11-17.
# "Välj ett alternativ." och "Svara i …" är borttagna, "en elev" har fått namn och "sammanlagd" heter "total".
# 0.62 behåller "och skriver −7 · (−5) = 35" (lärarens felrapport 2026-11-10).


def p(*s):
    return ''.join(f'<p>{x}</p>' for x in s)


R = {
    '0.62': {'t': p('Hugo räknar \\(-4-3\\cdot(-5)\\) från vänster och skriver \\(-7\\cdot(-5)=35\\). Vad är det viktigaste '
                    'felet?')},
    '0.77': {'t': p('Vilken beskrivning visar hur man beräknar −6 + (−4) på en tallinje?')},
    '0.80': {'t': p('Vilket påstående om 7 − (−3) stämmer?')},
    '0.86': {'t': p('Vilken av divisionerna går inte att utföra?')},
    '0.92': {'t': p('Vilket påstående om uttrycken \\(-2^2\\) och \\((-2)^2\\) stämmer?')},
    '0.98': {'t': p('För två tal gäller att a &lt; b &lt; 0. Vilken ordning gäller alltid?')},
    '0.107': {'t': p('Jonna säger: ”0 ÷ (−4) och (−4) ÷ 0 blir båda 0.” Har hon rätt? Använd sambandet mellan '
                     'multiplikation och division när du förklarar.')},
    '0.134': {'t': p('Temperaturen sjunker 8 grader och är då −3 °C. Vilken temperatur var det innan?')},
    '0.140': {'t': p('Antalet varor i ett lager ändras med \\(-18\\) första dagen, \\(+27\\) andra dagen och \\(-14\\) tredje '
                     'dagen.', 'Hur stor är den totala förändringen?')},
    '0.322': {'t': p('Vilket uttryck har värdet −16?')},
    '0.406': {'t': p('Efter en insättning på 500 kr är saldot på kontot 150 kr. Vad var saldot före insättningen?')},
    '0.864': {'t': p('I golf anger man resultatet i förhållande till ”par”. Emma går första rundan på \\(-3\\), alltså tre '
                     'slag under par, och andra rundan på \\(+5\\). Vilket är hennes totala resultat i förhållande till par?')},
    '0.879': {'t': p('Vilket av uttrycken har störst värde när \\(a=-3\\)?')},
}
