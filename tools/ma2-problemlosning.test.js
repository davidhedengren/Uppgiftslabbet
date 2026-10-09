'use strict';
const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};
for(const file of ['strukturma2.js','uppgifterma2.js'])vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..',file),'utf8'),c);
const task=id=>c.window.BANKMA2.find(q=>q.id===id);
test('Geometrisk problemlösning kombinerar korrekta vinklar, längder och areor',()=>{
  const height=Math.sqrt(10**2-6**2);
  const models=[
    ['3.531',Math.sqrt(10**2-6**2)],
    ['3.532',180-(180-40-60)-40/2],
    ['3.533',8*(Math.sqrt(10**2-8**2)/2)/2],
    ['3.534',Math.sqrt(13**2-((14**2-(15**2-13**2))/(2*14))**2)],
    ['3.535',Math.hypot(6,8)*6/(6+8)],
    ['3.536',8*6/(6+14)],
    ['3.537',(180-2*35)/2],
    ['3.538',12*height/4],
    ['3.539',180/2],
    ['3.478',10*9/2*(8/(8+4))**2],
    ['3.484',6**2/Math.hypot(6,8)],
    ['3.485',12*8/(12+8)],
    ['3.486',2+6*(1/.8)],
  ];
  for(const [id,value] of models)assert.ok(Math.abs(task(id).rättSvar-value)<1e-10,id);
  assert.equal(task('3.479').rättSvar,'\\(24\\sqrt{2}\\)');
  assert.equal(12/2*Math.sqrt(8*4),24*Math.sqrt(2));
  const fraction=Math.hypot(3,4)/(Math.hypot(3,4)+Math.hypot(12,-9));
  assert.equal(task('3.530').rättSvar,`(${3+fraction*(12-3)},${4+fraction*(-9-4)})`);
});
test('Maxarean i 3.538 gäller hela det möjliga höjdintervallet',()=>{
  for(let i=0;i<=800;i++){
    const h=i/100,area=h*(12-1.5*h);
    assert.ok(area<=task('3.538').rättSvar+1e-10);
    assert.ok(Math.abs(area-(-1.5*(h-4)**2+24))<1e-10);
  }
});
test('Blandad geometri har egen struktur, en enkel ingång och nivåer 1–5',()=>{
  assert.equal(c.window.OMRMA2[3].geometri_problemlosning,'Problemlösning');
  assert.deepEqual(Array.from(c.window.SPARMA2[3].geometri_problemlosning),['2b','2c']);
  const group=c.window.GRUPPMA2[3].find(g=>g.id==='geometri_problemlosning');
  assert.equal(group.namn,'Problemlösning');
  const qs=c.window.BANKMA2.filter(q=>q.omr==='geometri_problemlosning');
  assert.equal(qs.length,15);
  assert.deepEqual([...new Set(qs.map(q=>q.traningsniva))].sort(),[1,2,3,4,5]);
  for(const q of qs){assert.doesNotMatch(q.s,/facit-steglista/,q.id);assert.match(q.t,/<svg/,q.id);}
});
