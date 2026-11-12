"""AI-banken: lärarens felrapporter 2026-11-12 18:41 i kapitel 1 (sökning).

- 1.14 b: ”Fortsätt tabellen tills målet tas ut. (Svara med noderna i den ordning de tas ut efter dem som
  redan står i tabellen.)” var otydligt. Frågan säger nu rakt ut vad som ska skrivas: i vilken ordning
  resten av noderna tas ut, efter S och A, fram till och med målet. Svaret är oförändrat (B, C, D, E, F).
- 1.60: ”grannordning” förklaras i inledningen: den ordning som grannarna till en ruta prövas i, med ett
  exempel. Samma förklaring läggs in i 1.18 och 1.99, som använder ordet i inledningen.

Kapitel 4 rättas i bygg-ai-maskininlarning-2026-11-12.py, ai_ml_modeller.py och ai_ml.py.
Körs efter bygg-ai-efterbearbetning-2026-11-12.py och före bygg-ai-nivaer-2026-11-11.py. Idempotent.
"""
import json

BANK = 'uppgifterai.js'

GRANN = ('Grannordningen är den ordning som grannarna till en ruta prövas i. ↑ → ↓ ← betyder att rutan ovanför '
         'prövas först, sedan rutan till höger, rutan nedanför och sist rutan till vänster.')

B_GAMMAL = 'Fortsätt tabellen tills målet tas ut.'
B_NY = 'S och A är redan uttagna. I vilken ordning tas resten av noderna ut, fram till och med målet F?'
B_KORT_GAMMAL = (f'<p>{B_GAMMAL} (Svara med noderna i den ordning de tas ut efter dem som redan står i tabellen.)</p>')
B_KORT_NY = f'<p>{B_NY} (Skriv noderna i ordning, åtskilda med kommatecken.)</p>'


def ersatt(text, gammal, ny, falt):
    """Byter en gång. Redan bytt text lämnas (idempotent)."""
    if ny in text:
        return text
    assert text.count(gammal) == 1, (falt, gammal)
    return text.replace(gammal, ny)


def main():
    with open(BANK, encoding='utf-8', newline='') as fh:
        src = fh.read()
    i, j = src.index('['), src.rindex(']')
    bank = json.loads(src[i:j + 1])
    d = {u['id']: u for u in bank}

    u = d['1.14']
    b = next(k for k in u['spelDelar'] if k['etikett'] == 'b')
    assert b['rättSvar'] == 'B, C, D, E, F' and b['svarFormat'] == 'namnordning'
    b['fraga'] = ersatt(b['fraga'], B_KORT_GAMMAL, B_KORT_NY, '1.14b')
    u['t'] = ersatt(u['t'], f'<p>b) {B_GAMMAL}</p>', f'<p>b) {B_NY}</p>', '1.14 t')

    for id_, mening in [('1.60', 'Frågorna handlar om vad grannordningen betyder för BFS och DFS.'),
                        ('1.18', 'Labyrinten söks igenom med DFS två gånger, med olika grannordning.'),
                        ('1.99', 'Labyrinten söks igenom med DFS två gånger, med två olika grannordningar.')]:
        u = d[id_]
        for falt in ('t', 'spelIntro'):
            u[falt] = ersatt(u[falt], f'<p>{mening}</p>', f'<p>{mening} {GRANN}</p>', f'{id_} {falt}')

    with open(BANK, 'w', encoding='utf-8', newline='') as fh:
        fh.write(src[:i] + json.dumps(bank, ensure_ascii=False, indent=2) + src[j + 1:])
    print('1.14 b, 1.60, 1.18 och 1.99 rättade')


if __name__ == '__main__':
    main()
