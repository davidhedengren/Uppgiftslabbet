"""Ma1, trigonometri i tillämpningar."""

DEC = 'Avrunda till en decimal.'
TORN = '<p>Från en punkt på plan mark är vinkeln upp till toppen av ett torn 28°. När du mäter från en punkt 30 m närmare tornet är vinkeln 41°. Båda vinklarna mäts från marknivå.</p>'
AVSTAND = 'Hur långt är det från den närmare punkten till tornets fot?'
HOJD = 'Hur högt är tornet?'

def byt(fore, efter, kg=None):
    post = {'ers': [(fore, efter)]}
    if kg:
        post['kg'] = kg
    return post

def avrundning():
    return byt(' Svara med en decimal.', '', DEC)

R = {
    '4.17': byt('den vågräta sträckan', 'den horisontella sträckan'),
    '4.18': byt('Från en punkt 14 m från en flaggstång är elevationsvinkeln 27°. Hur hög är stången? Ögonhöjd försummas.', 'Från marknivå, 14 m från en flaggstångs fot, är vinkeln upp till toppen 27°. Hur hög är flaggstången?'),
    '4.31': byt('Från strandkanten ser du toppen av en mast på andra sidan en kanal med elevationsvinkeln 52°. Du går 18 m rakt bakåt och vinkeln blir 33°. Marken är plan.', 'En mast står precis vid stranden på andra sidan en kanal. Rakt mittemot masten är vinkeln upp till toppen 52°. Från en punkt 18 m längre bort på samma linje är vinkeln 33°. Båda vinklarna mäts från marknivå på samma höjd som mastens fot.'),
    '4.33': {'t': '<p>En väg lutar 12°. Mätt horisontellt är avståndet mellan vägsträckans ändpunkter 40 m. Hur lång är sträckan längs vägen?</p>'},
    '4.40': byt('Två observationspunkter ligger 25 m från varandra. Elevationsvinkeln till ett torn är 31° från den bortre punkten och 47° från den närmare.', 'Två punkter på plan mark ligger på samma räta linje fram till ett torn. Avståndet mellan punkterna är 25 m. Från den bortre punkten är vinkeln upp till tornets topp 31° och från den närmare är den 47°.'),
    '4.62': byt('En fiskare använder två spön från samma plats. På det ena har 12 m mer lina släppts ut. Vinklarna mellan vattenytan och linorna är 38° och 24°. Båda betena går på samma djup. Spöspetsen är 1,0 m över vattnet.', 'En fiskare håller två spön med spetsarna 1,0 m över vattenytan. Båda linorna är sträckta och betena ligger på samma djup. Den kortare linan bildar vinkeln 38° med vattenytan. Den andra linan är 12 m längre och bildar vinkeln 24°.'),
    '4.63': {'t': '<p>En takkant ligger 5,5 m över plan mark. Från en punkt på marken är vinkeln upp till takkanten 34°. Hur långt är det från punkten till marken rakt under takkanten?</p>'},
    '4.64': {'ers': [('två rätvinkliga trianglar med gemensam lodrät sida', 'två rätvinkliga trianglar med en gemensam vertikal sida'), ('Hur mycket längre omkrets har den stora triangeln än den lilla?', 'Hur stor är skillnaden mellan trianglarnas omkretsar?')]},
    '4.65': {'ers': [('monteras liggande på golvet och sedan resas upp? Motivera.', 'monteras liggande på rygg på golvet och sedan resas upp? Motivera ditt svar.'), ('När skåpet står med botten mot väggen är överkanten 3,2 cm från väggen. Anta att skåpet står vinkelrätt mot golvet. Bestäm vinkeln mellan vägg och golv.', 'Skåpet står nu vinkelrätt mot golvet, med bakre nederkanten mot väggen. Det kortaste avståndet från skåpets bakre överkant till väggen är 3,2 cm. Hur stor är den spetsiga vinkeln mellan väggen och golvet?')]},
    '4.66': {'t': '<p>En 3,6 m lång stege lutar mot en vägg och bildar vinkeln 74° med marken. Hur högt upp på väggen når stegen?</p>'},
    '4.67': {'ers': [('Ett tak anges med lutningsförhållandet 1:2,5, dvs. det stiger', 'Ett tak har lutningen 1:2,5. Det stiger'), ('Motivera.', 'Motivera ditt svar.')]},
    '4.68': {'t': '<p>Från punkt A på plan mark är vinkeln upp till ett torns topp 28°. När du går 35 m rakt mot tornet kommer du till punkt B, där vinkeln är 41°. Vinklarna mäts från marknivå.</p><p>Hur högt är tornet?</p>'},
    '4.167': {'t': TORN + '<p>a) ' + AVSTAND + '<br>b) ' + HOJD + '</p>', 'd': {'a': {'t': TORN + '<p>' + AVSTAND + '</p>', 'kg': DEC}, 'b': {'t': TORN + '<p>' + HOJD + '</p><p><em>Du kan använda att avståndet från den närmare punkten till tornets fot är cirka 47,2 m.</em></p>', 'kg': DEC}}},
    '4.168': byt('Ett borrhål ska nå lodrätt djup 140 m och borras 12° från lodlinjen.', 'Ett borrhål ska nå en punkt 140 m under markytan. Hålet borras i en rak linje som bildar vinkeln 12° med lodlinjen.'),
    '4.170': {'ers': [('Två fiskelinor har samma lodräta sträcka från spöspets till bete.', 'Två spöspetsar hålls på samma höjd och betena ligger lika djupt. Båda linorna är sträckta.'), ('Vilken ekvation modellerar situationen korrekt?', 'Vilken av ekvationerna beskriver linorna?')], 'extra': {'visaAlternativ': True}},
    '4.180': byt('I cirkeln är \\(O\\) centrum. Den lodräta linjen är vinkelrät mot den vågräta sträckan. Den vågräta sträckan är 5,4 cm och vinkeln vid cirkelpunkten är 21°.', r'Cirkeln har medelpunkten \(O\). Den horisontella sträckan är 5,4 cm och bildar rät vinkel med den vertikala linjen. Vinkeln vid cirkelns kant är 21°.'),
    '4.182': byt(' Avrunda till två decimaler.', '', 'Avrunda till två decimaler.'),
    '4.230': byt('Den horisontella sträckan är 6,0 m. Hur lång är rampen? Avrunda till en decimal.', 'Avståndet mellan rampens ändar är 6,0 m mätt längs marken. Hur lång är rampen?', DEC),
    '4.231': byt('Hur lång är vajern? Avrunda till en decimal.', 'Hur lång är vajern från markfästet till masten?', DEC),
    '4.232': byt('Hur lång är stigen? Avrunda till närmaste meter.', 'Hur lång är stigen?', 'Avrunda till närmaste meter.'),
    '4.233': {'t': '<p>Du mäter från marknivå 25 m från foten av ett torn. Vinkeln upp till toppen är 41°. Hur högt är tornet?</p>', 'kg': DEC},
    '4.234': byt('Hur långt är det horisontella avståndet från stolpens fot till linans fästpunkt i marken? Avrunda till en decimal.', 'Hur långt från stolpens fot är linan fäst i marken?', DEC),
    '4.443': avrundning(),
    '4.444': avrundning(),
    '4.445': avrundning(),
    '4.446': byt('Hur lång måste rampen minst vara, mätt längs rampen? Svara med en decimal.', 'Vilken är den kortaste ramp som klarar kravet?', DEC),
    '4.447': byt('Handen är vid marken. Hur högt flyger draken? Svara med en decimal.', 'Linans nedre ände är fäst vid marken. Hur högt flyger draken?', DEC),
    '4.448': {'ers': [('Takfotens vågräta avstånd till nocken', 'Det horisontella avståndet från takfoten till nocken'), (' Svara med en decimal.', '')], 'kg': DEC},
    '4.449': {'ers': [('på en vågrät sträcka', 'på en horisontell sträcka'), (' Svara med en decimal.', '')], 'kg': DEC},
    '4.450': byt('Från en 25 m hög utsiktsplats syns en båt. Linjen till båten bildar vinkeln 12° med horisontalplanet. Hur långt från utsiktsplatsens fot är båten? Svara i hela meter.', 'Du ser en båt från en utsiktsplats 25 m över vattnet. Siktlinjen till båten lutar 12° nedåt från horisontalplanet. Hur långt är det horisontellt från utsiktsplatsen till båten?', 'Avrunda till närmaste meter.'),
    '4.451': avrundning(),
    '4.452': byt('Hur högt har det kommit när det har flugit 5 000 m längs sin bana? Svara i hela meter.', 'Hur mycket har flygplanets höjd ökat när det har flugit 5 000 m längs sin bana?', 'Avrunda till närmaste meter.'),
    '4.453': {'t': '<p>En av de spetsiga vinklarna i en rätvinklig triangel är 38°. Hur stor är den andra spetsiga vinkeln?</p>'},
    '4.454': avrundning(),
    '4.573': {'ers': [('Båten ror 200 m', 'Du ror 200 m'), (' Svara i hela meter.', '')], 'kg': 'Avrunda till närmaste meter.'},
    '4.584': byt(' Svara i meter med en decimal.', '', DEC),
    '8.12': byt('Hur stor är höjdskillnaden mellan rampens ändar? (Svara i m.)', 'Hur stor är höjdskillnaden mellan rampens ändar?'),
}
