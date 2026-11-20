"""Originalteckningar för kraftkapitlet. Kör utan argument för kontroll, med --skriv för inläggning."""
from html import escape
from math import hypot
from pathlib import Path
import hashlib
import json
import re
import sys

import bankobjekt

INK = '#253e49'
TEAL = '#126779'
RUST = '#a44224'
PALE = '#d8e7e7'
STEEL = '#92acb2'
WOOD = '#dcac70'
GROUND = '#8c9d9f'
SKIN = '#dca77f'


def path(d, fill='none', stroke=INK, width=2):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{width}" stroke-linejoin="round" stroke-linecap="round"/>'


def rect(x, y, w, h, fill, radius=0, stroke=INK, width=2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>'


def dot(x, y, radius, fill, stroke=INK, width=1.5):
    return f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>'


def label(x, y, value, anchor='middle', color=INK, size=17):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Arial, sans-serif" font-size="{size}" font-weight="600" fill="{color}">{escape(value)}</text>'


def arrow(x, y, endx, endy, color):
    dx, dy = endx-x, endy-y
    length = hypot(dx, dy)
    ux, uy = dx/length, dy/length
    bx, by = endx-10*ux, endy-10*uy
    return (path(f'M{x} {y} L{bx:.2f} {by:.2f}', stroke=color, width=3.4)
            + path(f'M{endx} {endy} L{bx-4.8*uy:.2f} {by+4.8*ux:.2f} L{bx+4.8*uy:.2f} {by-4.8*ux:.2f} Z',color,'none'))


def measure(x1, x2, y, name):
    return (path(f'M{x1} {y} H{x2} M{x1} {y-5} v10 M{x2} {y-5} v10',stroke=GROUND,width=1.5)
            + label((x1+x2)/2, y-7, name,size=16))


def guide(x, top, bottom):
    return f'<path d="M{x} {top} V{bottom}" stroke="{GROUND}" stroke-width="1" stroke-dasharray="3 4"/>'


def wheel(x, y, radius):
    return dot(x,y,radius,INK)+dot(x,y,radius*.56,'#c8d5d6',INK,1.5)+dot(x,y,radius*.2,INK,INK,1)


def ground(y=142):
    return path(f'M18 {y} H462',stroke=GROUND,width=1.5)


def frame(uid, h, description, art):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 {h}" width="480" height="{h}" '
            f'role="img" aria-label="{escape(description,quote=True)}" data-figur="kraft-{uid}" style="max-width:100%;height:auto"><title>{escape(description)}</title>'
            f'<rect width="480" height="{h}" fill="#fff"/>{art}</svg>')


def cart():
    return (ground()+wheel(196,130,11)+wheel(282,130,11)
            +path('M190 118 H286 L280 126 H196 Z',STEEL)
            +path('M164 77 H313 L307 116 Q306 119 302 119 H176 Q171 119 170 115 Z','#96c2c4')
            +rect(163,72,152,8,'#e7efeb',2)
            +path('M173 96 H309 M186 81 L189 114 M290 81 L287 114',stroke=TEAL,width=1.4)
            +dot(185,86,2.2,INK)+dot(292,86,2.2,INK))


def box(taped):
    if taped:
        return (ground()+rect(177,70,126,71,'#d5a673',2)
                +path('M177 70 L191 59 H315 L303 70 Z','#e8c99c')
                +path('M303 70 L315 59 V130 L303 141 Z','#bd8e63')
                +path('M230 70 L243 59 H263 L250 70 V88 L245 85 L241 88 L236 85 L230 88 Z','#f4dfb5','#967750',1)
                +path('M187 131 H213 M187 126 H200',stroke='#916d48',width=1.4))
    return (ground()+rect(169,66,142,75,'#d8b488',2)
            +path('M178 74 H302 V132 H178 Z M178 92 H302 M178 111 H302',stroke='#96774f',width=1)
            +path('M177 125 L293 73 H303 V80 L187 132 H177 Z','#e6c9a0')
            +''.join(dot(x,y,1.9,'#785f41','none') for x in (175,305) for y in (73,134)))


def sled():
    return (path('M18 142 Q85 140 140 142 T260 142 T365 142 T462 142',stroke='#7696a2',width=1.5)
            +path('M181 117 L194 136 M272 117 L285 136 M197 135 L264 116',stroke=INK,width=4)
            +path('M162 137 H285 Q308 137 317 117',stroke=INK,width=6)
            +path('M162 136 H285 Q306 136 315 117',stroke='#8daad0',width=2)
            +rect(165,105,134,11,WOOD,4)
            +path('M173 104 L184 98 H299 Q304 98 300 103 L295 106', '#ebca96')
            +path('M185 101 H291',stroke='#ad7743',width=1.3)
            +path('M293 104 L313 87 h7 M293 110 L313 117 h7',stroke='#95744b',width=2))


def rope():
    art=path('M170 101 Q240 99 310 101',stroke='#71573b',width=12)
    art+=path('M170 100 Q240 98 310 100',stroke='#e1bb83',width=8)
    art+=''.join(path(f'M{x} 97 l5 7',stroke='#98764e',width=1.6) for x in range(173,307,9))
    return art+path('M237 94 H246 L244 109 L252 126 L244 123 L240 128 L235 110 Z','#bf653c')


def boat():
    return (path('M17 135 Q33 131 49 135 T81 135 T113 135 T145 135 T177 135 T209 135 T241 135 T273 135 T305 135 T337 135 T369 135 T401 135 T433 135 T463 135',stroke='#789da9',width=1.6)
            +path('M177 102 L174 92 H166 L164 118 L171 126 H177 Z','#50666b')
            +path('M189 101 L204 81 H227 L237 65 H253 L271 95 L299 98 L321 92 Q315 115 286 129 H197 Q183 123 178 105 Z','#567d87')
            +path('M181 103 Q245 110 317 97 L312 106 Q240 117 185 110 Z','#ebf0e9',INK,1)
            +path('M212 97 L218 84 H231 L238 69 H251 L265 95 Z','#d5e9e8')
            +path('M244 71 L246 96 M207 98 H282',stroke=INK,width=2)
            +dot(276,116,3,'#d2dfdb')+dot(289,114,3,'#d2dfdb'))


def ball():
    return (ground()+dot(240,99,42,'#f7f5e9',INK,2.5)
            +path('M233 84 L252 83 L259 99 L246 111 L229 102 Z','#344f57')
            +path('M219 63 L231 58 L239 59 L237 67 L223 72 Z M274 76 L281 92 L278 103 L270 96 L268 83 Z M254 126 L268 121 L267 132 L252 139 L246 136 Z M200 92 L209 93 L214 106 L209 117 L201 113 Z','#344f57')
            +path('M223 72 L218 80 L233 84 M237 67 L252 83 M259 99 L270 96 M246 111 L254 126 M229 102 L214 106 M218 80 L209 93 M209 117 L221 131 L246 136',stroke='#667d7d',width=1.3))


def shopping_cart():
    art=(ground()+wheel(206,134,7)+wheel(281,134,7)
         +path('M168 65 H184 L203 118 H285 M204 118 L199 127 H285',stroke='#3d6167',width=4)
         +path('M187 78 L306 75 L296 108 L200 114 Z','#d3e4e2'))
    for x in range(201,294,13):
        art+=path(f'M{x} 80 l3 28',stroke='#6d9094',width=1)
    return art+path('M194 91 L300 87 M197 103 L298 97',stroke='#6d9094',width=1.4)+rect(162,60,24,7,TEAL,3)


# (belopp, riktning, kraftens läge, etikett). Pilar i en bild använder samma kraftskala.
SCENES = {
    913:(cart,[(30,1,'in-left','30 N'),(20,-1,'in-right','20 N')]),
    914:(cart,[(30,1,'in-left','30 N'),(20,1,'out-right','20 N')]),
    915:(cart,[(20,1,'in-left','20 N'),(40,1,'in-left','40 N'),(30,-1,'in-right','30 N')]),
    916:(cart,[(30,1,'in-left','30 N'),(30,-1,'in-right','30 N')]),
    917:(cart,[(20,-1,'out-left','20 N'),(20,-1,'out-left','20 N'),(40,1,'out-right','40 N')]),
    918:(lambda:box(False),[(120,1,'in-left','Ali 120 N'),(50,-1,'in-right','Bea 50 N'),(45,-1,'surface','friktion 45 N')]),
    919:(sled,[(60,1,'out-right','60 N'),(45,1,'out-right','45 N'),(75,-1,'surface','friktion 75 N')]),
    920:(rope,[(90,-1,'out-left','vänster lag 90 N'),(90,1,'out-right','höger lag 90 N')]),
    921:(boat,[(90,1,'out-right','motor 90 N'),(55,-1,'surface','vatten 55 N'),(20,-1,'out-left','vind 20 N')]),
    922:(ball,[(35,1,'in-left','Sara 35 N'),(50,-1,'in-right','Tim 50 N')]),
    923:(shopping_cart,[(25,1,'in-left','25 N'),(15,1,'in-left','15 N'),(10,-1,'surface','friktion 10 N')]),
    924:(lambda:box(True),[(80,-1,'out-left','Emil 80 N'),(50,1,'out-right','Lisa 50 N'),(30,1,'out-right','Omar 30 N')]),
}


def horizontal(number):
    draw, forces = SCENES[number]
    art = draw()
    descriptions = []
    scale = 126 / max(force[0] for force in forces)
    left, right = {920: (170, 310), 922: (198, 282), 923: (177, 307),
                   924: (176, 313)}.get(number, (168, 313))
    counts = {}
    for n, sign, place, name in forces:
        side = place.split('-')[-1]
        counts[side] = counts.get(side, 0) + 1
        shared = sum(force[2].endswith(side) for force in forces) > 1
        y = (77 if counts[side] == 1 else 112) if shared else 100
        width = n * scale
        contact = left if side == 'left' else right
        if number == 919 and side == 'right':
            y, contact = (87 if counts[side] == 1 else 117), 320
        if number == 923 and side == 'left':
            contact = 188 if counts[side] == 1 else 200
        x = contact - sign * width if place.startswith('in') else contact
        caption_y = y - 11
        if place == 'surface':
            x, y, caption_y = 241, 142, 169
        if number == 921:
            x, y, caption_y = {90: (168 - width, 120, 109), 55: (283, 129, 166),
                               20: (237, 65, 50)}[n]
        color = TEAL if sign == 1 else RUST
        middle = x + sign * width / 2
        if number in (918, 924) and side == 'right':
            middle = max(middle, 359)
        art += '<g class="kraftpil">' + arrow(x, y, x + sign * width, y, color) + '</g>'
        art += label(middle, caption_y, name, color=color)
        direction = 'höger' if sign == 1 else 'vänster'
        descriptions.append(f'{name} åt {direction}')
    description = 'Vågräta krafter: ' + ', '.join(descriptions) + '.'
    return frame('4.'+str(number),185,description,art)


def wheelbarrow(number):
    art=ground(173)
    art+=wheel(70,142,30)+dot(70,142,16,'#c9d8d9')
    for dx,dy in [(13,0),(7,12),(-7,12),(-13,0),(-7,-12),(7,-12)]:
        art+=path(f'M70 142 l{dx} {dy}',stroke='#728a91',width=1.5)
    art+=path('M73 142 Q105 132 139 120 L254 110 L410 76',stroke=INK,width=7)
    art+=path('M167 121 L204 154 L232 113',stroke='#698287',width=4)
    art+=path('M106 88 Q131 78 145 74 Q161 57 175 62 Q188 52 200 59 Q219 58 240 74 L265 78 L268 90 Z','#c6a579')
    art+=path('M91 82 Q152 90 278 77 L250 111 Q244 117 232 119 L151 127 Q133 128 125 119 Z','#78a8a8')
    art+=path('M91 81 Q151 89 279 76',stroke=INK,width=5)
    art+=path('M132 104 Q164 110 245 98',stroke='#d7e8e3',width=2)
    art+=path('M398 79 L430 72',stroke=INK,width=9)+dot(70,142,4,'#f1e9d4')
    xload=195 if number!=75 else 210
    art+=dot(xload,78,4,RUST)
    if number==302:
        art+=arrow(xload,78,xload,146,RUST)+label(207,148,'Fg, last','start',RUST,15)
        art+=dot(157.5,115,3,INK)+arrow(157.5,115,157.5,132,TEAL)+label(155,153,'Fg, kärra','middle',TEAL,15)
    else:
        art+=path(f'M{xload} 72 l12 -25 h14',stroke=GROUND,width=1.4)+label(xload+22,39,'lastens tyngdpunkt',size=16)
    if number!=11:
        art+=arrow(420,75,420,48 if number==302 else 24,TEAL)+label(410,47 if number==302 else 26,'Fh' if number==302 else 'händerna','end',TEAL,16)
    art+=guide(70,176,255 if number==302 else 226)+guide(420,84,255 if number==302 else 226)
    if number==302:
        art+=guide(157.5,161,194)+measure(70,157.5,194,'0,35 m')
    y=222 if number==302 else 193
    art+=guide(xload,143 if number==302 else 130,y)+measure(70,xload,y,'x = ?' if number==75 else '0,50 m')
    art+=measure(70,420,y+31,'1,4 m')
    desc={11:'Skottkärra. Lastens tyngdpunkt ligger 0,50 m och handtagen 1,4 m bakom hjulaxeln.',
          75:'Skottkärra med en last. Lastens avstånd bakom hjulaxeln söks. Händerna lyfter 1,4 m bakom axeln.',
          302:'Skottkärra. Kärrans tyngd verkar 0,35 m bakom axeln, lastens 0,50 m bakom. Händerna lyfter 1,4 m bakom axeln.'}
    return frame(f'4.{number}',y+49,desc[number],art)


def cyclist():
    art=ground(171)
    for x in (143,322):
        art+=dot(x,132,38,'white',INK,5)+dot(x,132,33,'none',STEEL,1.3)
        for dx,dy in [(32,0),(22,22),(0,32),(-22,22)]:
            art+=path(f'M{x-dx} {132-dy} l{2*dx} {2*dy}',stroke='#adbdbe',width=1)
    art+=path('M143 132 L183 76 L215 132 Z M183 76 L292 80 L215 132 M322 132 L289 67 L299 60',stroke=TEAL,width=5)
    art+=path('M179 77 L173 64 M160 63 H184 M289 67 L281 60 H296 Q306 60 302 68',stroke=INK,width=4)
    art+=dot(215,132,7,'#d6e1df')+path('M215 132 l13 9 h9',stroke=INK,width=3)
    art+=path('M185 56 Q197 52 207 60 L238 85 Q244 91 239 99 L217 131 L206 126 L220 96 L186 80 Q174 73 177 63 Z','#526974')
    art+=path('M208 125 L217 128 L225 137 Q224 140 214 138 L202 133 Z',INK)
    art+=path('M185 55 Q197 32 222 23 Q234 21 245 32 L249 44 Q226 49 212 69 L181 67 Z','#b76b47')
    art+=path('M242 37 L255 60 L282 60 Q290 59 291 64 L282 67 L252 67 Q247 66 243 61 L230 44 Z',SKIN)
    art+=path('M235 32 L245 48 L233 56 L222 40 Z','#c17b55')
    art+=path('M236 31 L243 22 Q249 10 260 17 Q267 20 265 29 L268 34 L262 35 Q259 43 253 39 L246 35 L243 40 Z',SKIN)
    art+=path('M240 24 Q238 11 251 9 Q264 8 269 20 L263 22 L241 27 Z','#477b81')+path('M248 14 l8 -2 M253 18 l9 -2',stroke=PALE,width=2)
    return frame('4.411',188,'En cyklist rullar åt höger på plan väg med fötterna på pedalerna.',art)


def parachute(number):
    art=path('M92 71 Q101 27 152 19 Q219 7 289 19 Q335 25 354 67 Q336 55 321 71 Q302 54 278 72 Q251 54 224 72 Q198 55 173 73 Q148 56 125 73 Q109 60 92 71 Z','#cc8858')
    art+=path('M125 73 Q139 34 168 22 Q146 42 148 62 M173 73 Q187 33 204 17 M224 72 Q226 44 224 16 M278 72 Q266 32 252 18 M321 71 Q302 38 282 21',stroke='#805f46',width=1.4)
    art+=path('M93 71 L202 155 M125 73 L202 155 M173 73 L205 156 M278 72 L236 154 M321 71 L236 154 M354 67 L238 155',stroke='#68848c',width=1.5)
    art+=path('M201 154 L211 166 M237 154 L230 167',stroke=INK,width=3)
    art+=path('M213 155 Q217 151 225 154 L231 165 L229 185 L214 186 L208 165 Z','#638f94')
    art+=path('M211 164 L201 155 L198 144 M229 163 L238 153 L241 143',stroke=INK,width=5)
    art+=path('M217 185 L214 201 L206 209 M225 185 L231 197 L226 209',stroke=INK,width=7)
    art+=dot(220,145,9,SKIN)+path('M210 145 Q208 134 219 134 Q230 134 230 143 L222 143 L218 147 Z','#456f78')
    art+=path('M213 156 L228 178 M226 155 L214 177 M212 178 H230',stroke='#253e49',width=2.4)
    if number==136:
        art+=arrow(386,119,386,176,TEAL)+label(399,151,'v','start',TEAL)
    return frame(f'4.{number}',222,'Hoppare under öppen fallskärm. Linorna från skärmen är fästa i personens sele.'+(' Hastigheten är riktad nedåt.' if number==136 else ''),art)


def wall_contact(number):
    block = number == 146
    art = rect(293, 20, 31, 140, '#e8edeb', 0, 'none')
    for y in range(36, 155, 16):
        art += path(f'M294 {y} l13 -13', stroke='#acbdba', width=1.3)
    art += path('M293 20 V160', stroke=INK, width=2.5)
    if block:
        art += rect(205, 51, 87, 81, WOOD, 1)
        art += path('M211 60 q13 -2 28 0 M258 124 q12 -2 23 -1',
                    stroke='#b38655', width=1.3)
        art = '<g transform="translate(480 0) scale(-1 1)">' + art + '</g>'
        art += label(231, 99, '2,0 kg')
        art += dot(275, 92, 4.5, TEAL, 'white', 1.5)
        art += path('M279 89 L303 66 H321', stroke=TEAL, width=1.4)
        art += label(326, 71, 'Här trycker', 'start', size=16)
        art += label(326, 90, 'handen', 'start', size=16)
        desc = 'En kloss på 2,0 kg ligger mot väggen till vänster. En punkt mitt på klossens högra sida visar var handen trycker.'
    else:
        art += rect(245, 42, 47, 101, TEAL, 3)
        art += path('M250 46 H286 Q283 89 286 139 H250 Z', '#f4ead4', INK, 1)
        art += path('M255 49 V134 M260 49 V133 M278 51 V135', stroke='#cbbfa7', width=1)
        art += arrow(126, 92, 244, 92, RUST)
        art += label(185, 79, '30 N', color=RUST, size=19)
        desc = 'Boken står mot väggen till höger. En vågrät pil märkt 30 N pekar åt höger mot bokens vänstra sida.'
    return frame(f'4.{number}', 181, desc, art)


def books():
    art=path('M58 135 H420 V146 H58 Z','#d6b48d')+path('M76 146 v15 M402 146 v15',stroke=INK,width=5)
    for x,y,w,h,cover,value in [(128,92,219,43,'#59868b','1,2 kg'),(147,56,183,36,'#b86a48','0,80 kg')]:
        art+=rect(x,y,w,h,cover,3)+path(f'M{x+13} {y+4} h{w-16} q-4 {h/2-4} 0 {h-8} H{x+13} Z','#f4ead4',INK,1.1)
        for k in (9,h-10):
            art+=path(f'M{x+w-34} {y+k} h26',stroke='#b6a98b',width=1)
        art+=path(f'M{x+8} {y+3} v{h-6}',stroke='#d4d7bc',width=1.2)+label(x+w/2,y+h/2+6,value)
    return frame('4.478',172,'Två inbundna böcker vilar på bordet. Den övre väger 0,80 kg och den undre 1,2 kg.',art)


def astronaut():
    art=path('M49 49 Q49 31 67 31 H99 M49 49 V152 Q49 171 69 171 H113 M431 51 V145',stroke='#b4c6c9',width=2)
    art+=rect(110,65,36,73,'#819a9d',7)+rect(112,75,12,44,'#d6e1dd',3)
    art+=path('M133 111 Q146 104 166 115 L171 136 L153 154 L137 162 L126 153 L145 136 L128 135 L112 149 L94 146 L93 136 L112 132 L125 113 Z','#d4ded9')
    art+=path('M94 133 L110 141 L104 153 L83 149 Q80 145 85 140 Z M129 152 L139 161 L133 173 L115 171 Q110 166 118 161 Z','#607b81')
    art+=path('M137 66 Q158 58 173 73 L174 115 Q157 126 132 116 L126 94 Q125 76 137 66 Z','#ebefe7')
    art+=path('M131 105 l40 3 M134 113 l34 3',stroke='#839c9e',width=2)
    art+=rect(144,81,20,16,'#73959a',3)+dot(159,85,2.1,'#eec17e','none')
    art+=dot(151,53,23,'#e1e9e3')+path('M136 48 Q150 35 166 43 Q176 50 166 61 Q150 69 138 59 Z','#345963')
    art+=path('M143 48 Q151 43 160 45',stroke='#abc8c6',width=2)
    art+=path('M171 76 Q177 69 184 76 L196 88 L222 85 L230 97 L196 104 Q191 105 186 101 L172 92 Q166 87 171 76 Z','#e3e9e2')
    art+=path('M210 87 l4 14 M216 86 l4 14',stroke='#779298',width=2)
    art+=path('M222 86 Q228 83 236 86 L247 89 L248 102 L225 98 Z','#a7bdb8')
    art+=rect(248,77,73,54,'#ce8958',5)+path('M270 77 V68 Q270 63 276 63 H294 Q300 63 300 69 V77',stroke=INK,width=4)
    art+=path('M249 92 H320 M254 124 H315',stroke='#946347',width=1.8)+rect(260,88,7,10,PALE,1)+rect(302,88,7,10,PALE,1)
    art+=arrow(249,50,313,50,TEAL)+label(281,38,'45 N',color=TEAL)+label(284,155,'15 kg')+label(152,198,'astronaut 90 kg')
    return frame('4.464',212,'En fritt svävande astronaut på 90 kg knuffar en verktygslåda på 15 kg åt höger med 45 N.',art)


def skater(x, height, mirrored, coat):
    # Skridskoskären och händerna har fasta kontaktpunkter i den lokala kroppen.
    outfit=(path('M-9 -68 L10 -67 L16 -42 L9 -12 H-1 L3 -43 L-4 -49 L-13 -29 L-27 -12 L-35 -18 L-23 -38 Z','#526673')
            +path('M-36 -18 L-25 -12 L-25 -8 H-47 Q-47 -13 -41 -14 Z M-1 -15 H10 L18 -8 H-4 Z',INK)
            +path('M-47 -3 h25 q4 0 5 -3 M-5 -3 h23 q5 0 6 -4',stroke='#627d86',width=2)
            +path('M-40 -8 v5 M-27 -8 v5 M0 -8 v5 M12 -8 v5',stroke=INK,width=1.6)
            +path('M-8 -109 Q6 -115 15 -101 L20 -78 L10 -64 L-14 -67 L-10 -84 Z',coat)
            +path('M8 -103 Q14 -108 20 -99 L31 -88 L52 -85 L51 -75 L28 -78 Q24 -78 20 -82 L6 -94 Z',coat)
            +path('M49 -86 Q57 -88 63 -81 Q63 -77 58 -76 L49 -76 Z',SKIN)
            +path('M-2 -116 Q-2 -127 9 -127 Q18 -126 18 -117 L22 -112 L17 -110 Q16 -104 11 -104 L5 -106 L1 -101 L-5 -107 Z',SKIN)
            +path('M-5 -118 Q-6 -129 3 -133 Q14 -137 20 -123 L19 -119 L2 -117 L-4 -113 Z',coat))
    scale=height/134
    return f'<g transform="translate({x} 173) scale({-scale if mirrored else scale:.3f} {scale:.3f})">{outfit}</g>'


def skaters():
    # Händerna möts vid x=233, i gemensam höjd. Strecket är isens yta.
    art=path('M27 172 H450 M89 181 h66 M290 179 h48',stroke='#92b2bb',width=1.5)
    art+=skater(171,134,False,'#649596')+skater(295,134,True,'#c17a55')
    art+=arrow(233,92,303,92,RUST)+label(234,58,'150 N',color=RUST)
    art+=label(152,204,'50 kg')+label(307,204,'75 kg')
    return frame('4.463',216,'Två skridskoåkare möts hand mot hand. Eleven på 50 kg trycker eleven på 75 kg åt höger med kraften 150 N.',art)


def elevator(number):
    has_scale=number in (39,115,202,217)
    art=path('M194 9 V29 M208 9 V29 M246 9 V29',stroke='#71878d',width=2)
    art+=rect(107,28,220,161,PALE,7)+rect(115,35,204,145,'#f4f6f2',3)
    art+=path('M126 163 V48 H307 V163 M115 180 L126 166 H307 L319 180',stroke='#aec1c1',width=1.3)
    art+=rect(132,69,10,26,'#c5d4cf',2,INK,1)+dot(137,77,1.8,'#536e74','none')+dot(137,86,1.8,'#536e74','none')
    if has_scale:
        art+=path('M182 171 L191 165 H251 L255 172 V178 H182 Z','#607b82')+path('M190 171 H245',stroke='#becfc9',width=1)
    offset=0 if has_scale else 7
    person=(path('M202 112 H230 L232 136 L235 163 L226 165 L218 133 L214 130 L211 161 L201 163 L201 137 Z','#526573')
            +path('M201 159 H211 L212 169 H194 Q192 164 201 162 Z M226 159 L235 158 L239 164 L245 167 L244 170 H226 Z',INK)
            +path('M199 83 Q207 76 218 77 Q228 77 231 86 L230 118 Q219 122 200 117 Z','#679898')
            +path('M200 84 Q195 84 194 93 L191 116 L198 119 L205 96 M227 84 L233 87 L238 111 L234 115 L226 101', '#79a6a3')
            +path('M191 114 L198 116 L197 125 Q192 129 190 122 Z M232 113 L238 109 L240 119 Q239 124 235 122 Z',SKIN)
            +path('M207 72 L208 80 Q215 84 219 78 L219 71 Z',SKIN)
            +path('M205 57 Q211 49 222 57 L222 64 L225 68 L221 70 Q220 78 211 75 L207 71 Z',SKIN)
            +path('M203 60 Q201 49 212 48 Q223 47 224 56 L220 60 L211 59 L209 66 L204 64 Z',INK))
    art+=f'<g transform="translate(0 {offset})">{person}</g>'
    motion={199:('a',True),804:('v',True),805:('a',True),806:('a',False)}
    if number in motion:
        sym,up=motion[number]
        art+=arrow(361,133 if up else 74,361,74 if up else 133,TEAL)+label(377,105,sym,'start',TEAL,20)
    if number in (39,115,202,217):
        text={39:'60 kg',115:'65 kg',202:'62 kg',217:'68 kg'}[number]
        art+=label(260,84,text,'start',size=15)
        art+=path('M252 172 L280 206 H293',stroke=GROUND,width=1.5)
        art+=label(299,211,'75 kg' if number==217 else 'våg','start',size=16)
    if number==217:art+=label(367,130,'a = ?',color=TEAL)
    captions={39:'En person på 60 kg står på en våg i en hiss.',115:'En person på 65 kg står på en kraftmätande våg i hissen.',199:'Personen står på hissgolvet medan hissen accelererar uppåt.',202:'En person på 62 kg står på en våg i hissen.',217:'Personen väger 68 kg och hissvågen visar 75 kg. Accelerationen söks.',804:'Hissen och personen rör sig uppåt med konstant fart.',805:'Hissen med personen accelererar uppåt.',806:'Hissen med personen accelererar nedåt.'}
    return frame(f'4.{number}',226 if has_scale else 202,captions[number],art)


def illustrations():
    figures={f'4.{n}':horizontal(n) for n in SCENES}
    figures.update({f'4.{n}':wheelbarrow(n) for n in (11,75,302)})
    figures.update({f'4.{n}':parachute(n) for n in (136,413,422)})
    figures.update({f'4.{n}':elevator(n) for n in (39,115,199,202,217,804,805,806)})
    figures.update({
        '4.146':wall_contact(146),'4.411':cyclist(),'4.463':skaters(),
        '4.464':astronaut(),'4.478':books(),'4.816':wall_contact(816),
    })
    return figures

# Fingeravtrycken avgränsar vilka äldre original som får ersättas.
ORIGINAL = {
    "4.11": "a0942de5856dfd20",
    "4.39": "941450d12cfbdd22",
    "4.75": "aad73dbd0127751b",
    "4.115": "8f385edf16924862",
    "4.136": "be59f979085b2995",
    "4.146": "cfec04c21d315bbb",
    "4.411": "fa656c7e4d6ba4a5",
    "4.413": "5eb5f36240c10a35",
    "4.199": "3339954575f2a7e5",
    "4.202": "31898c1153d61a51",
    "4.217": "90b78c6a2077046b",
    "4.422": "5eb5f36240c10a35",
    "4.302": "2add5bcf1857196c",
    "4.463": "19893958f2ed393a",
    "4.464": "6d95cb07ba762329",
    "4.478": "11b516a02e866b56",
    "4.804": "dbc807954811f0a7",
    "4.805": "74ace9c42aa77653",
    "4.806": "4de8081b01db7307",
    "4.816": "499e09b88c575c77",
    "4.913": "1d81b8be9019add1",
    "4.914": "d62bc959bda72522",
    "4.915": "daa6fb42542769dd",
    "4.916": "04659f14327680f1",
    "4.917": "902073793f7f4462",
    "4.918": "24d3ef271b944bf6",
    "4.919": "67ab2844735948f6",
    "4.920": "be8d9f60ee6b88c7",
    "4.921": "775f58529f3282ad",
    "4.922": "fedaf491503f8f93",
    "4.923": "7461439fee0c7ace",
    "4.924": "15f83147073af22b",
}


def main():
    file=Path(__file__).resolve().parents[1]/'uppgifter.js'
    src,bank=bankobjekt.las(file)
    figures=illustrations()
    assert set(figures)==set(ORIGINAL)
    assert set(figures) <= {task['id'] for task in bank}
    changed={}
    replacements={}
    for task in bank:
        uid=task['id']
        if uid not in figures:
            continue
        images=re.findall(r'<svg\b.*?</svg>|<img\b[^>]*>',task['t'],re.S)
        assert len(images)==1,uid
        old,=images
        new=figures[uid]
        if old==new:
            continue
        if not (hashlib.sha256(old.encode()).hexdigest()[:16]==ORIGINAL[uid] or f'data-figur="kraft-{uid}"' in old):
            raise ValueError(f'{uid}: figuren har ändrats sedan granskningen')
        for obj in [task,*task.get('spelDelar',[])]:
            for field in ('t','spelIntro'):
                if field in obj:
                    obj[field]=obj[field].replace(old,new)
        changed[uid]=task
        replacements[uid]=(old,new)
    if changed and '--skriv' in sys.argv:
        parts=[]
        cursor=0
        for start,end,original in bankobjekt.spann(src):
            uid=original['id']
            if uid not in changed:
                continue
            old,new=replacements[uid]
            old,new=(json.dumps(s,ensure_ascii=False)[1:-1] for s in (old,new))
            block=src[start:end].replace(old,new)
            assert json.loads(block)==changed[uid],uid
            parts.extend([src[cursor:start],block])
            cursor=end
        bankobjekt.skriv(file,''.join(parts)+src[cursor:])
    print(f'{len(figures)} illustrationer, {len(changed)} att uppdatera.')


if __name__=='__main__':
    main()
