'use strict';
const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifterma2.js'),'utf8'),c);
const task=n=>c.window.BANKMA2.find(q=>q.id==='3.'+n);
const close=(a,b,eps=.02)=>assert.ok(Math.abs(a-b)<eps,`${a} != ${b}`);
function tags(n,tag){return [...task(n).t.matchAll(new RegExp('<'+tag+'\\b([^>]+)>','g'))].map(m=>Object.fromEntries([...m[1].matchAll(/([\w-]+)="([^"]*)"/g)].map(x=>[x[1],x[2]])));}
function lines(n){return tags(n,'line').map(l=>[[+l.x1,+l.y1],[+l.x2,+l.y2]]);}
const len=l=>Math.hypot(l[1][0]-l[0][0],l[1][1]-l[0][1]);
const mid=l=>[(l[0][0]+l[1][0])/2,(l[0][1]+l[1][1])/2];
function angle(a,o,b){const u=a.map((v,i)=>v-o[i]),v=b.map((x,i)=>x-o[i]);return Math.acos((u[0]*v[0]+u[1]*v[1])/(Math.hypot(...u)*Math.hypot(...v)))*180/Math.PI;}
function distanceToLine(p,l){const u=l[1].map((v,i)=>v-l[0][i]),t=u.reduce((s,v,i)=>s+v*(p[i]-l[0][i]),0)/len(l)**2;return len([p,l[0].map((v,i)=>v+t*u[i])]);}
test('Femton nya självständiga problem har kontrollerade svar och tydliga nivåer',()=>{
 const expected=[Math.sqrt(13**2-12**2),4+3*8/4,84*13/(13+15),8*Math.sqrt(17**2-8**2),(9+12**2/9)/2,90-(180-110)/2,50*(1-(6/10)**2),(14+8)/2*Math.sqrt(10**2-6**2),4*6*Math.sqrt(10**2-6**2)/2,36/2,54/((9+12+15)/2),8*6/2-4*3/2,180-50/2-70/2,(3**2+3**2)/3**2,12*(1-12/(12+18))];
 expected.forEach((v,i)=>{const q=task(540+i);close(q.rättSvar,v,1e-9);assert.equal(q.omr,'geometri_problemlosning');assert.deepEqual(Array.from(q.kurs),['2b','2c']);assert.equal(q.självrättning,true);assert.match(q.t,/<svg/);assert.doesNotMatch(q.s,/facit-steglista|<ol/);assert.equal(q.spelDelar,undefined);});
 assert.equal(task(549).traningsniva,1);for(const n of [540,541,543,545,546,552]){assert.equal(task(n).traningsniva,2);assert.equal(task(n).niva,'E');}
});
test('Cirklarnas radier, kordor, rektangel och höjd följer de givna måtten',()=>{
 let l=lines(540),r=+tags(540,'circle')[0].r;close(len(l[0])/r,24/13);close(len(l[1])/r,1);close(len(l[2])/r,5/13);close(len([mid(l[0]),l[2][1]]),0);
 l=lines(541);const scale=len(l[0])/11,p=[l[1][0][0],l[0][0][1]];close(len([l[0][0],p])/scale,3);close(len([p,l[0][1]])/scale,8);close(len([l[1][0],p])/scale,4);close(len([p,l[1][1]])/scale,6);
 l=lines(543);const k=len(l[0])/8;close(len(l[1])/k,15);close(len(l[4])/k,17);close(+tags(543,'circle')[0].r/k,8.5);close(angle(l[0][0],l[0][1],l[1][1]),90);
 l=lines(544);const k2=len(l[0])/25;close(len(l[3])/k2,12);close(len([l[0][0],l[3][1]])/k2,9);close(angle(l[0][0],l[3][0],l[0][1]),90);
});
test('Bisektrisser och vinkelbågar ligger mellan rätt vinkelben',()=>{
 let l=lines(542);close(angle(l[0][1],l[0][0],l[3][1]),angle(l[3][1],l[0][0],l[2][0]));close(len([l[1][0],l[3][1]])/len(l[1]),13/28);
 l=lines(545);const O=l[0][0],A=l[0][1],B=l[1][1],T=l[3][1];close(angle(A,O,B),110);close(angle(B,A,T),55);close(angle(O,A,T),90);
 // Kontrollera själva x-bågens ändpunkter, oberoende av validatorns val av vinkelben vid A.
 const arc=tags(545,'path').filter(p=>p.d.includes(' A')).at(-1),nums=arc.d.match(/-?\d+(?:\.\d+)?/g).map(Number),start=nums.slice(0,2),end=nums.slice(-2);
 close(distanceToLine(start,[A,B]),0);close(distanceToLine(end,[A,T]),0);close(len([A,start]),50);close(len([A,end]),50);
 l=lines(552);const a=l[0][0],b=l[0][1],cc=l[1][1],I=l[3][1];close(angle(b,a,cc),50);close(angle(a,b,cc),70);close(angle(b,a,I),25);close(angle(I,b,cc),35);close(angle(a,I,b),120);
 l=lines(554);close(angle(l[0][1],l[0][0],l[3][1]),angle(l[3][1],l[0][0],l[2][0]));close(len([l[1][0],l[3][1]])/len(l[1]),.4);close(len([l[0][1],l[4][1]])/len(l[0]),.4);
});
test('Parallella sträckor och mittpunkter ligger på de avsedda sidorna',()=>{
 let l=lines(546);close(len(l[3])/len(l[1]),.6);for(const [pt,side] of [[l[3][0],l[0]],[l[3][1],l[2]]])close(distanceToLine(pt,side),0);
 l=lines(547);const k=len(l[0])/14;close(len(l[2])/k,8);close(len(l[1])/k,10);close(len(l[3])/k,8);
 l=lines(548);const k2=len(l[0])/10;close(len(l[4])/k2,12);close(len(l[5])/k2,16);close(len([mid(l[4]),mid(l[5])]),0);
 l=lines(549);close(len([mid(l[1]),l[3][1]]),0);
 l=lines(551);close(len([mid(l[2]),l[3][0]]),0);close(len([mid(l[1]),l[3][1]]),0);
});
test('Inskrivna cirklar tangerar alla avsedda sidor',()=>{
 let l=lines(550),circle=tags(550,'circle')[0],O=[+circle.cx,+circle.cy],r=+circle.r;close(r/(len(l[0])/9),3);
 for(const side of l.slice(0,3))close(distanceToLine(O,side),r);
 const circles=tags(553,'circle');close((+circles[1].r/+circles[0].r)**2,2);l=lines(553);O=[+circles[0].cx,+circles[0].cy];for(const side of l.slice(0,4)){close(distanceToLine(O,side),+circles[0].r);close(len([O,side[0]]),+circles[1].r);}
});
