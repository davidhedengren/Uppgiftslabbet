const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifterma1.js'),'utf8'),c);
const bank=c.window.BANKMA1,ids=Array.from({length:15},(_,i)=>'1.'+(1386+i)),get=id=>bank.find(q=>q.id===id);
test('Femton självständiga kort på nivå 3–5 med alla Ma1-spår och rätt verktyg',()=>{
 const count={};for(const id of ids){const q=get(id);assert.ok(q,id);assert.equal(q.omr,'ekv_parenteser');assert.deepEqual([...q.kurs],['1a','1b','1c']);assert.equal(q.miniräknare,true);assert.equal(q.geogebra,false);assert.equal(q.spel,true);assert.equal(q.självrättning,true);assert.equal(q.tolerans,0);assert.match(q.s,/facit-svar/);count[q.traningsniva]=(count[q.traningsniva]||0)+1;}
 assert.deepEqual(count,{3:6,4:6,5:3});assert.equal(new Set(bank.map(q=>q.id)).size,bank.length);
});
test('Tio rutinuppgifter: insättning och oberoende linjära koefficienter',()=>{
 // f = vänsterled minus högerled, skrivet från frågan; m och b härledda separat.
 const cases=[
  [1386,x=>5*(2*x-3)-2*(3*x+4)-(3*(x-5)+1),1,-9],
  [1387,x=>7-3*(2-(x-4))-2*(x+1),1,-13],
  [1388,x=>(2*x-1)/3-(x+4)/2-(x-5)/4,-1/12,-13/12],
  [1389,x=>.4*(5*x-2)-.6*(x+1)-.5*(2*x+3),.4,-2.9],
  [1390,x=>4*(3-x)-(2*(5-(x+1))+3*x),-5,4],
  [1391,x=>3*(x-2)/4-(5*(x+1)/6-2),-1/12,-1/3],
  [1392,x=>2*(3*x-(x-4))-3*(x-2*(x+1))-(5*(x+2)-6),2,10],
  [1393,x=>(3*(2*x-1)-2*(x+4))/5-(2*(x-3)+1)/3,2/15,-8/15],
  [1394,x=>(x+4)*(x-2)-(x+1)*(x-3)-17,4,-22],
  [1395,x=>3*(2*x-1)/4-(5-2*(x+3))/6-(x+7)/3,1.5,-35/12]
 ];
 const numeric=v=>typeof v==='number'?v:Number(v.split('/')[0])/Number(v.split('/')[1]);
 for(const [id,f,m,b] of cases){const q=get('1.'+id),ans=numeric(q.rättSvar);for(const x of [-7,-1,0,1,6])assert.ok(Math.abs(f(x)-(m*x+b))<1e-10,id);assert.ok(Math.abs(f(ans))<1e-10,id);assert.ok(Math.abs(ans+b/m)<1e-10,id);assert.ok(Math.abs(f(ans+1))>1e-3,id+' rejects neighbour');}
});
test('Figurens area och den felaktiga elevlösningen ger korrekta villkor',()=>{
 const x=get('1.1396').rättSvar;assert.ok(x>1);assert.equal((x+6)*(x+2)-(x-1)*(x+2),56);assert.equal(get('1.1396').svarEnhet,'cm');assert.match(get('1.1396').t,/<svg/);
 const k=18,wrong=2,correct=get('1.1397').rättSvar;assert.equal(2*(2*wrong+2),3*(wrong-4)+k);assert.notEqual(2*(3*wrong-(wrong+2)),3*(wrong-4)+k);assert.equal(2*(3*correct-(correct+2)),3*(correct-4)+k);
});
test('Avancerade parameterfall: identitet, samma rot och förskjuten lösning',()=>{
 const a=5,b=get('1.1398').rättSvar;assert.equal(2*a+4,a+9);assert.equal(-6*a+4,-2*a-18+b);
 for(const x of [-3,0,1,7])assert.equal(2*a*(x-3)+4*(x+1),(a+9)*(x-2)+b);
 const x=32/13,p=4/13;assert.ok(Math.abs(3*(x-2)-2*(1-x)-(p+4))<1e-12);assert.ok(Math.abs(2*(3-(x-1))-(x+2*p))<1e-12);assert.equal(get('1.1399').rättSvar,'4/13');
 const L=x=>(2/3)*(3*x-(x-2)/4)-(1/2)*(x-(2*x+1)/3);
 for(const x of [-3,0,4])assert.ok(Math.abs(L(x)-(10*x+3)/6)<1e-12);
 assert.ok(Math.abs(L(12/7)-(12/7+5)/2)<1e-12);assert.ok(Math.abs(L(5/7)-(5/7+8/3)/2)<1e-12);assert.equal(get('1.1400').rättSvar,'8/3');
 for(const id of ['1.1395','1.1399','1.1400'])assert.equal(get(id).svarFormat,'bråk');
});
