const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),path=require('path'),vm=require('vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter2.js'),'utf8'),c);const bank=c.window.BANK2,q=id=>bank.find(q=>q.id===id),close=(a,b)=>assert.ok(Math.abs(a-b)<=Math.abs(b)*1e-8,`${a} != ${b}`);
const ids=['5.30','5.35','5.41','5.42','5.48','5.31','5.32','5.33','5.34','5.39'];
test('Magnituder, stjärneffekt och fem liknande modeller räknas självständigt',()=>{
 const sun=3.828e26,T=5772;
 close(q('5.30').rättSvar[0],100**((4.74-.58)/5));close(q('5.30').rättSvar[1],sun*100**((4.74-.58)/5));
 close(q('5.31').rättSvar,4.74-2.5*Math.log10(6.89e23/sun));
 for(const [id,r,t] of [['5.32',3.4,12000],['5.39',2.05,6530]]){const L=r*r*(t/T)**4;close(q(id).rättSvar[0],L);close(q(id).rättSvar[1],4.74-2.5*Math.log10(L));}
 close(q('5.33').rättSvar,Math.sqrt(100**((4.74+3.55)/5))*(T/21000)**2);
 close(q('5.34').rättSvar,T*(100**((4.74+6.93)/5)/203**2)**.25);
 for(const [i,r,t,m] of [[0,2.8,10300,1.58],[1,8.8,4700,1.14]]){const L=r*r*(t/T)**4,M=4.74-2.5*Math.log10(L),d=10**((m-M+5)/5);[L,M,d].forEach((v,j)=>close(q('5.35').rättSvar[j][i],v));}
});
test('Teleskopets fotonantal följer effekt dividerad med fotonenergi',()=>{
 const d=1/.01925,M=4.36+5-5*Math.log10(d),T=2.898e-3/632e-9,Lrel=100**((4.74-M)/5),I=Lrel*3.828e26/(4*Math.PI*(d*3.086e16)**2),P=I*Math.PI*3**2,E=6.626e-34*3e8/632e-9;
 [d,M,T,Lrel,I,P/E].forEach((v,i)=>close(q('5.42').rättSvar[i],v));
 const s=q('5.42').spelDelar[5].s;for(const word of ['Parallaxen','magnitud','effekt','sfär','foton'])assert.match(s,new RegExp(word,'i'));for(const f of ['A&=','P&=','E&=','\\frac{N}{t}'])assert.ok(s.includes(f));
});
test('Kalibrering, språk och hjälpmedel fungerar även på fristående delkort',()=>{
 for(const id of ids)for(const d of [q(id),...(q(id).spelDelar||[])]){assert.equal(d.miniräknare,true,id);assert.equal(d.geogebra,false,id);assert.ok(d.traningsniva>=1&&d.traningsniva<=5,id);assert.doesNotMatch(d.t+d.s,/bolometr|enfärgsmodell|facit-steglista/i);assert.match(d.s,/facit-svar/);}
 assert.equal(q('5.30').spelDelar[1].traningsniva,5);assert.equal(q('5.35').spelDelar[1].traningsniva,5);assert.equal(q('5.42').spelDelar[5].traningsniva,5);assert.equal(q('5.42').spelDelar[0].traningsniva,2);assert.equal(q('5.42').spelDelar[2].traningsniva,2);
 for(const id of ['5.32','5.39'])assert.match(q(id).spelDelar[1].s,/5772/);
 for(const d of q('5.35').spelDelar){assert.deepEqual(Array.from(d.svarEtiketter),['A','B']);assert.equal(d.svarsstruktur,'ordnad');}
});
test('Två omgjorda begreppskort skiljer absolut från skenbar magnitud',()=>{
 assert.equal(q('5.41').traningsniva,1);assert.equal(q('5.48').traningsniva,2);
 assert.equal(q('5.41').alternativ.find(a=>a.ratt).txt,'Stjärna A.');assert.match(q('5.48').alternativ.find(a=>a.ratt).txt,/Sirius.*avstånden/);
 for(const id of ['5.41','5.48'])assert.equal(q(id).alternativ.filter(a=>a.ratt).length,1);
});
