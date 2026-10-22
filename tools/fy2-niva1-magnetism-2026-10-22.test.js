'use strict';
/* Påfyllnad 2026-10-22: 56 kort på nivå 1 i Fy2 kap 3 (3.460–3.515). */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifter2.js'),'utf8'),c);
const nya=c.window.BANK2.filter(t=>{const [k,n]=t.id.split('.').map(Number);return k===3&&n>=460&&n<=515;});
const get=id=>nya.find(t=>t.id===id);
const MU0=4e-7*Math.PI,QE=1.602176634e-19,ME=9.1093837e-31,MP=1.67262192e-27;
const utanSvg=h=>h.replace(/<svg[\s\S]*?<\/svg>/g,'');

test('56 kort på nivå 1, åtta per område, i fysikformat',()=>{
  assert.equal(nya.length,56);const per={};
  for(const t of nya){per[t.omr]=(per[t.omr]||0)+1;
    assert.equal(t.traningsniva,1,t.id);assert.equal(t.miniräknare,true,t.id);assert.match(t.poang,/^\(\d\/\d\/\d\)$/,t.id);assert.match(t.t,/<svg/,t.id);
    assert.doesNotMatch(utanSvg(t.t),/4\\?\s?π\s?·?\s?10|1,602|9,109|1,67\d|μ_?0\s*=|\\mu_0=/,t.id);
    if(t.svarstyp==='alternativ')assert.equal(t.alternativ.filter(a=>a.ratt).length,1,t.id);
    if(t.svarVardesiffror!=null){assert.ok(t.svarEnhet,t.id);assert.doesNotMatch(utanSvg(t.t),/decimal|avrund|värdesiffr/i,t.id);}
  }
  assert.deepEqual(per,{magnetism:8,orsted:8,spolar:8,laddade_partiklar:8,induktion:8,induktion_ledare:8,jordens_magnetfalt:8});
});

test('Facit räknas om',()=>{
  const Bl=(I,a)=>MU0*I/(2*Math.PI*a),Bs=(N,I,l)=>MU0*N*I/l,deg=Math.PI/180;
  const fall={'3.460':0.25*4*0.5,'3.461':0.08*2.5*0.2,'3.462':0.12/(3*0.4),'3.463':0.06/(0.3*0.1),'3.466':2*0.3,
    '3.468':Bl(10,0.05),'3.469':Bl(3,0.02),'3.472':2e-5*2*Math.PI*0.1/MU0,'3.473':Bl(200,10),
    '3.476':Bs(500,2,0.25),'3.477':Bs(1200,0.5,0.4),'3.480':4e-3*0.3/(MU0*800),'3.481':MU0*3000*1.5,
    '3.484':QE*2e6*0.05,'3.485':QE*3e5*0.2,'3.486':MP*1e6/(QE*0.5),'3.487':ME*5e6/(QE*2e-3),'3.490':4e4/0.02,
    '3.492':0.4*0.05,'3.493':0.3*0.01,'3.494':200*3e-3/0.1,'3.495':0.02/0.5,'3.499':50*0.4*0.02/0.2,
    '3.500':0.5*0.2*3,'3.501':4.5e-5*30*250,'3.502':0.12/(0.4*0.15),'3.503':0.6/3,'3.505':2*0.25,'3.506':0.8,
    '3.508':50*Math.cos(70*deg),'3.509':50*Math.sin(70*deg),'3.510':Math.hypot(18,48),'3.511':Math.atan(3)/deg};
  for(const [id,v] of Object.entries(fall)){const t=get(id);assert.ok(t,id);assert.ok(Math.abs(t.rättSvar-v)<=Math.abs(v)*1e-9+1e-15,`${id}: ${t.rättSvar} ≠ ${v}`);}
});

test('Riktningsfacit följer högerhandsregeln',()=>{
  const ratt=id=>get(id).alternativ.find(a=>a.ratt).txt;
  const kors=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
  const namn={'1,0,0':'åt höger','-1,0,0':'åt vänster','0,1,0':'uppåt','0,-1,0':'nedåt','0,0,1':'ut ur pappret','0,0,-1':'in i pappret'};
  const r=(I,B)=>namn[kors(I,B).map(x=>x+0).join(',')];
  assert.equal(ratt('3.464'),r([1,0,0],[0,0,-1]));   // ström höger, fält in
  assert.equal(ratt('3.467'),r([0,-1,0],[0,0,1]));   // ström ned, fält ut
  assert.equal(ratt('3.491'),r([0,1,0],[0,0,1]));    // positiv laddning uppåt, fält ut
});
