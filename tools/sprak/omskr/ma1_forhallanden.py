# Ma1 förhållanden (omr forhallanden), omskrivet för hand 2026-11-17.
# "(Svara i …)" är borttaget, "sammanlagt" heter "totalt" och konstlade formuleringar är skrivna om.
FIG = '<span class="fig">[F1]</span>'


def p(*s):
    return ''.join(f'<p>{x}</p>' for x in s)


R = {
    '0.789': {'t': p('Förhållandet mellan röda och blå pärlor är 5:8. Det finns 52 pärlor totalt. Hur många är röda?')},
    '0.825': {'t': p('En lastbils framaxel får bära högst 7 500 kg och bakaxeln högst 15 500 kg. Skriv förhållandet mellan '
                     'den största tillåtna vikten på framaxeln och på bakaxeln i enklaste form.')},
    '0.829': {'t': p('I en fruktskål är förhållandet äpplen : päron = 2 : 3. Sex päron byts ut mot sex äpplen. Då blir '
                     'förhållandet 4 : 3. Hur många frukter finns i skålen?')},
    '0.1142': {'t': p('Cement och sand blandas i volymförhållandet 1:3. Blandningen ska bli 14 liter. Hur många liter sand '
                      'behövs?')},
    '0.1143': {'t': p('Saftkoncentrat och vatten blandas i förhållandet 1:4. Det ska bli 15 liter saft. Hur många liter vatten '
                      'behövs?')},
    '0.1144': {'t': p('Vit och blå färg blandas i förhållandet 2:3. Det ska bli 20 liter färg. Hur många liter blå färg '
                      'behövs?')},
    '0.1221': {'t': p('72 kr ska delas mellan Ella och Omar i förhållandet 4 : 5.') + FIG + p('Hur många kronor får Omar?')},
    '0.1222': {'t': p('Saft ska blandas med vatten i förhållandet 1 : 5. Du har 3 dl saft.') + FIG +
               p('Hur många dl vatten ska du använda?')},
    '0.1224': {'t': p('En målare blandar vit, gul och röd färg i förhållandet 1 : 2 : 5. Blandningen ska bli 16 liter.') + FIG +
               p('Hur många liter röd färg behövs?')},
    '0.1226': {'t': p('En bioduk har formatet 21 : 9, alltså bredd : höjd. Duken är 84 dm bred.') + FIG +
               p('Hur många decimeter hög är duken?')},
    '0.1227': {'t': p('I en klass med 30 elever är förhållandet tjejer : killar = 3 : 2. Sedan börjar 5 nya killar i klassen.',
                      'Vilket är det nya förhållandet tjejer : killar?'), 'kg': 'Svara på formen a:b.'},
    '0.1229': {'t': p('Mässing består av koppar och zink i förhållandet 3 : 2. Hur många kilogram zink finns i 8 kg mässing?')},
}
