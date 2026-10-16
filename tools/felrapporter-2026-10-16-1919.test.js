'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const root=path.join(__dirname,'..'),c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(root,'uppgiftermato1.js'),'utf8'),c);const bank=c.window.BANKMATO1,q=id=>bank.find(x=>x.id===id),plain=x=>JSON.parse(JSON.stringify(x));
const report=JSON.parse(fs.readFileSync(path.join(root,'agent/FELRAPPORTER_2026-10-16_1919.json'),'utf8'));
test('Rapporter och minst fem relevanta jämförelser har kommentarer och verktygsbeslut',()=>{
 assert.equal(report.rapporter.length,4);assert.equal(report.granskade.length,28);assert.equal(report.bankAndrade.length,21);
 assert.equal(report.atgardade.length,25);assert.equal(report.granskad_inga_fel.length,3);
 for(const group of Object.values(report.jamforelsegrupper))assert.ok(group.length>=6);
 for(const id of report.granskade){const row=report.poster.find(x=>x.id===id);assert.ok(row.kommentar);assert.ok(row.kontroll);assert.equal(typeof q(id)['miniräknare'],'boolean');if(q(id).geogebra)assert.ok(q(id)['miniräknare']);}
});
test('Alla rötter är korrekta och ska kunna ges i valfri ordning',()=>{
 const equations={'2.530':x=>30*x-(3*x*x-33),'2.531':x=>3*x*x-.88-5,'2.576':x=>24*x-(3*x*x-27),'2.416':x=>3*x*x-12,'2.42':x=>3*x*x-6*x-9,'2.182':x=>3*x*x-12*x+9,'2.422':x=>5*x**4-5,'2.423':x=>3*x*x-6*x};
 for(const [id,f] of Object.entries(equations)){assert.equal(q(id).svarsstruktur,'mängd');for(const x of q(id).rättSvar)assert.ok(Math.abs(f(x))<1e-8,id);}
 assert.equal(q('2.530').traningsniva,3);
});
test('Modeller definierar tiden och använder rätt tids- och svarsenheter',()=>{
 assert.match(q('2.571').t,/minuter/);assert.match(q('2.571').t,/°C/);assert.equal(q('2.571').svarEnhet,'%');assert.ok(Math.abs(q('2.571').rättSvar-100*(1-Math.exp(-.039)))<.005);
 const t=q('2.321').rättSvar;assert.ok(Math.abs(96*Math.exp(.08*t)-150)<1e-9);assert.equal(Math.round(t*10)/10,5.6);assert.equal(q('2.321').svarEnhet,'år');assert.equal(q('2.321').geogebra,true);
 assert.match(q('2.537').t,/minuter/);assert.match(q('3.655').t,/timmar/);assert.equal(q('3.655').svarEnhet,'bakterier/h');
 assert.match(q('3.656').t,/tiden i år/);assert.ok(Math.abs(q('3.656').rättSvar-100*Math.exp(.5))<1e-9);assert.equal(q('3.656').svarEnhet,'individer/år');
 assert.equal(q('2.753').svarEnhet,'g/h');assert.equal(q('2.757').svarEnhet,'bakterier/h');
});
test('Exakt eller tre decimaler använder halv avrundningsenhet och rätt matematik',()=>{
 const expected={'1.579':Math.sqrt(3),'2.810':Math.sqrt(7),'4.474':3*Math.sqrt(3)/2};
 for(const [id,v] of Object.entries(expected)){assert.ok(Math.abs(q(id).rättSvar-v)<1e-12);assert.equal(q(id).tolerans,.0005);}
 assert.deepEqual(plain(q('2.816').rättSvar),['ln(2)','ln(3)']);assert.deepEqual(plain(q('2.816').svarFormat),['uttryck','uttryck']);
 const [x,min]=q('2.826').rättSvar;assert.ok(Math.abs(x-Math.log(2))<1e-12);assert.equal(min,-4);assert.ok(Math.abs(Math.exp(2*x)-4*Math.exp(x)-min)<1e-12);assert.equal(q('2.826')['miniräknare'],true);assert.equal(q('2.826').traningsniva,4);
 for(const z of q('1.586').rättSvar)assert.ok(Math.abs(2*z*z+12*z+7)<1e-10);
 assert.deepEqual(plain(q('2.823').rättSvar),[4.7,11/3]);
});
