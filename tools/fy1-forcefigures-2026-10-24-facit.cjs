// Only manually confirmed overwide equations. Values and derivations are preserved.
const fs=require('fs'),path=require('path');const R=String.raw;
const rows=[
['4.20',R`x=\frac{6{,}0}{61{,}375}=0{,}097759\ldots\,\mathrm{m}\approx9{,}78\,\mathrm{cm}`,[R`x=\frac{6{,}0}{61{,}375}=0{,}097759\ldots\,\mathrm{m}`,R`x\approx9{,}78\,\mathrm{cm}`]],
['4.93',R`a=\frac{0{,}090}{500}=0{,}00018\,\mathrm{m/s^2}=0{,}18\,\mathrm{mm/s^2}`,[R`a=\frac{0{,}090}{500}=0{,}00018\,\mathrm{m/s^2}`,R`a=0{,}18\,\mathrm{mm/s^2}`]],
['4.100',R`N-mg=ma\quad\Rightarrow\quad N=m(g+a)`,[R`N-mg=ma`,R`N=m(g+a)`]],
['4.100',R`N-mg=ma_h\quad\Rightarrow\quad N=m(g+a_h)`,[R`N-mg=ma_h`,R`N=m(g+a_h)`]],
['4.110',R`m_{\mathrm{tot}}=(40+20+20)\ \mathrm t=80\ \mathrm t=8{,}0\cdot10^4\ \mathrm{kg}`,[R`m_{\mathrm{tot}}=(40+20+20)\ \mathrm t`,R`m_{\mathrm{tot}}=80\ \mathrm t=8{,}0\cdot10^4\ \mathrm{kg}`]],
['4.110',R`F_1=(20\,000+20\,000)0{,}60=24\,000\ \mathrm N=24\ \mathrm{kN}`,[R`F_1=(20\,000+20\,000)0{,}60`,R`F_1=24\,000\ \mathrm N=24\ \mathrm{kN}`]],
['4.110',R`F_2=20\,000\cdot0{,}60=12\,000\ \mathrm N=12\ \mathrm{kN}`,[R`F_2=20\,000\cdot0{,}60`,R`F_2=12\,000\ \mathrm N=12\ \mathrm{kN}`]],
['4.146',R`f-mg=0\Rightarrow f=2{,}0\cdot9{,}82=19{,}64\ \mathrm N\approx19{,}6\ \mathrm N`,[R`f-mg=0`,R`f=2{,}0\cdot9{,}82=19{,}64\ \mathrm N`,R`f\approx19{,}6\ \mathrm N`]],
['4.171',R`F_g=mg=0{,}0050\cdot9{,}82=0{,}0491\ \mathrm N=49{,}1\ \mathrm{mN}`,[R`F_g=mg=0{,}0050\cdot9{,}82`,R`F_g=0{,}0491\ \mathrm N=49{,}1\ \mathrm{mN}`]],
['4.179',R`f_k=18\ \mathrm N,\qquad\mu_k=\frac{18}{49{,}1}\approx0{,}367`,[R`f_k=18\ \mathrm N`,R`\mu_k=\frac{18}{49{,}1}\approx0{,}367`]],
['4.199',R`N-mg=ma\Rightarrow N=m(g+a)&gt;mg`,[R`N-mg=ma`,R`N=m(g+a)&gt;mg`]],
['4.206',R`F-mg=ma\quad\Rightarrow\quad F=638{,}3+52=690{,}3\,\mathrm N`,[R`F-mg=ma`,R`F=638{,}3+52=690{,}3\,\mathrm N`]],
['4.237',R`F=F_g+ma=785{,}6+48=833{,}6\,\mathrm N`,[R`F=F_g+ma`,R`F=785{,}6+48=833{,}6\,\mathrm N`]],
['4.258',R`N+S\sin30^\circ=mg\Rightarrow N=mg-S\sin30^\circ&lt;mg`,[R`N+S\sin30^\circ=mg`,R`N=mg-S\sin30^\circ&lt;mg`]],
['4.260',R`S_1\cos35^\circ=mg\Rightarrow S_1=\frac{mg}{\cos35^\circ}&gt;mg`,[R`S_1\cos35^\circ=mg`,R`S_1=\frac{mg}{\cos35^\circ}&gt;mg`]],
['4.302',R`F_H=\frac{9{,}82(60\cdot0{,}50+15\cdot0{,}35)}{1{,}4}\approx247\,\mathrm N`,[R`F_H=\frac{9{,}82(60\cdot0{,}50+15\cdot0{,}35)}{1{,}4}`,R`F_H\approx247\,\mathrm N`]],
['4.872',R`300\cdot2{,}0=400\cdot x\quad\Rightarrow\quad x=\frac{600}{400}=1{,}5\ \mathrm m`,[R`300\cdot2{,}0=400\cdot x`,R`x=\frac{600}{400}=1{,}5\ \mathrm m`]]
];
let p=path.join(__dirname,'../uppgifter.js'),s=fs.readFileSync(p,'utf8');for(const[id,before,after]of rows){const re=new RegExp('\\n([ \\t]*)\\{\\n[ \\t]*"id": "'+id.replace('.','\\.')+'"'),h=re.exec(s);if(!h)throw Error(id);let start=h.index+1,end=s.indexOf('\n'+h[1]+'}',start)+h[1].length+2,raw=s.slice(start,end);const from=JSON.stringify(R`\[${before}\]`).slice(1,-1),to=JSON.stringify(after.map(x=>R`\[${x}\]`).join('')).slice(1,-1);if(!raw.includes(from)&&!raw.includes(to))throw Error('Formula missing '+id);s=s.slice(0,start)+raw.split(from).join(to)+s.slice(end);}fs.writeFileSync(p,s);
console.log('Mobilanpassade facit:',new Set(rows.map(r=>r[0])).size);
