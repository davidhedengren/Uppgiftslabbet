'use strict';
/* Ma2 kap 3: överlappskontroll av alla 593 figurer (2026-10-27).
   granska-svg.js mätte figurerna i Chrome. En striktare regel, där en mörk linje går genom textens kärna eller en text klipps,
   gav 112 figurer före och 23 efter. De 23 är axeltal med vit kant och fem uppmätta falsklarm, se agent/MA2_KAP3_REVISION_2026-10-25.md.
   Testet kontrollerar de flyttade etiketterna med en ungefärlig textruta (teckenbredd 0,58 · font-size) mot raka linjer,
   och att axeltal som skärs av en graf har vit kant och ritas sist. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const B=c.window.BANKMA2,get=id=>{const q=B.find(x=>x.id===id);assert.ok(q,id);return q;};
const figurer=q=>[...new Set([q.t,q.spelIntro,q.s,...(q.spelDelar||[]).flatMap(d=>[d.t,d.fraga,d.s])].filter(s=>typeof s==='string').flatMap(s=>s.match(/<svg[\s\S]*?<\/svg>/g)||[]))];
const innehall=t=>t.replace(/^<text[^>]*>|<\/text>$/g,'').replace(/<[^>]+>/g,'').replace(/&amp;/g,'&').trim();
const attr=(tag,n)=>{const m=tag.match(new RegExp(`\\s${n}="([^"]*)"`));return m?m[1]:null;};
const texter=svg=>[...svg.matchAll(/<text\b[\s\S]*?<\/text>/g)].map(m=>({raw:m[0],i:m.index,tag:m[0].match(/<text\b[^>]*>/)[0],txt:innehall(m[0])}));
const lum=h=>{if(!h||!/^#[0-9a-f]{6}$/i.test(h))return 0;const v=[1,3,5].map(i=>parseInt(h.slice(i,i+2),16)/255);return 0.2126*v[0]+0.7152*v[1]+0.0722*v[2];};
function strackor(svg){const ut=[];
  for(const m of svg.matchAll(/<(line|polyline|polygon|path)\b[^>]*>/g)){const tag=m[0],st=attr(tag,'stroke');if(!st||st==='none'||lum(st)>0.8||/transform=/.test(tag))continue;
    let p=[];
    if(m[1]==='line')p=[[+attr(tag,'x1'),+attr(tag,'y1')],[+attr(tag,'x2'),+attr(tag,'y2')]];
    else if(m[1]==='path'){const d=attr(tag,'d')||'';if(!/^[\sMLHVZ\d.,-]+$/.test(d))continue;let x=0,y=0,s=null;
      for(const[,k,a]of d.matchAll(/([MLHVZ])([^MLHVZ]*)/g)){const n=(a.match(/-?[\d.]+/g)||[]).map(Number);
        if(k==='M'||k==='L')for(let i=0;i+1<n.length;i+=2){x=n[i];y=n[i+1];if(k==='M'&&i===0&&p.length){ut.push(p);p=[];}p.push([x,y]);if(!s)s=[x,y];}
        else if(k==='H'){x=n[0];p.push([x,y]);}else if(k==='V'){y=n[0];p.push([x,y]);}else if(k==='Z'&&s)p.push(s);}}
    else{p=(attr(tag,'points')||'').trim().split(/[\s,]+/).map(Number).reduce((a,v,i)=>(i%2?a[a.length-1].push(v):a.push([v]),a),[]);if(m[1]==='polygon'&&p.length)p.push(p[0]);}
    if(p.length>1)ut.push(p);}
  return ut;}
function karna(t){const fs=+(attr(t.tag,'font-size')||16),x=+attr(t.tag,'x'),y=+attr(t.tag,'y'),w=t.txt.length*0.58*fs,a=attr(t.tag,'text-anchor')||'start';
  const x0=a==='middle'?x-w/2:a==='end'?x-w:x;return{x:x0+0.1*w,y:y-0.62*fs,w:0.8*w,h:0.54*fs};}
function skar(p,q,b){let t0=0,t1=1;const dx=q[0]-p[0],dy=q[1]-p[1];
  for(const[pp,qq]of[[-dx,p[0]-b.x],[dx,b.x+b.w-p[0]],[-dy,p[1]-b.y],[dy,b.y+b.h-p[1]]]){
    if(pp===0){if(qq<0)return false;}else{const r=qq/pp;if(pp<0){if(r>t1)return false;if(r>t0)t0=r;}else{if(r<t0)return false;if(r<t1)t1=r;}}}return true;}
const FLYTTADE=[['3.13','A'],['3.14','1,80 m'],['3.25','A'],['3.34','9 m'],['3.53','y = x'],['3.58','A'],['3.77','C'],['3.82','A'],['3.100','7,2 cm'],['3.166','3'],['3.175','A'],['3.205','A'],['3.209','C'],['3.226','x'],['3.229','32°'],['3.230','75°'],['3.232','4x'],['3.232','5x'],['3.235','68°'],['3.237','x−12°'],['3.271','U'],['3.275','C'],['3.390','(x + 12)°'],['3.394','C'],['3.395','C'],['3.402','C'],['3.408','C'],['3.433','B'],['3.460','55 tum'],['3.2020','3,0 m'],['3.2058','2x + 12'],['3.2074','3x + 12'],['3.2074','5x − 20'],['3.2076','2x + 15'],['3.2081','I'],['3.2098','60 cm'],['3.2098','90 cm'],['3.2133','2x + 20°'],['3.2158','?'],['3.2160','30 cm'],['3.2162','115°'],['3.2162','v'],['3.2163','M'],['3.2173','P'],['3.315','P'],['3.520','BC = 20 cm'],['3.521','BC = 9 cm'],['3.529','BC = 20 cm'],['3.607','D'],['3.607','2'],['3.112','A(-2,1)'],['3.291','D']];
test('Flyttade etiketter: ingen rak linje genom textens kärna',()=>{
  for(const[id,txt]of FLYTTADE){let n=0;
    for(const svg of figurer(get(id))){const S=strackor(svg);
      for(const t of texter(svg).filter(t=>t.txt===txt)){n++;const k=karna(t);
        for(const p of S)for(let i=1;i<p.length;i++)assert.ok(!skar(p[i-1],p[i],k),`${id}: ”${txt}” korsas av en linje`);}}
    assert.ok(n>0,`${id}: ”${txt}” saknas`);}
});
const HALO=[['3.05','7'],['3.24','2'],['3.45','−1'],['3.45','2'],['3.54','4'],['3.58','1'],['3.64','6'],['3.75','−3'],['3.75','−4'],['3.82','-1'],['3.112','1'],['3.135','1'],['3.183','3'],['3.183','4'],['3.205','1'],['3.205','3'],['3.289','4'],['3.317','3'],['3.319','−3'],['3.319','5'],['3.342','0'],['3.362','−2'],['3.2113','2'],['3.184','−1']];
test('Axeltal som skärs av en graf har vit kant och ritas efter linjerna',()=>{
  for(const[id,txt]of HALO){const svg=figurer(get(id))[0],sist=Math.max(...['<line','<polyline','<polygon','<path'].map(s=>svg.lastIndexOf(s)));
    assert.ok(texter(svg).some(t=>t.txt===txt&&/paint-order="stroke"/.test(t.tag)&&/stroke="#fff"/.test(t.tag)&&t.i>sist),`${id}: axeltalet ${txt}`);}
});
test('Handflyttade figurer',()=>{
  const pos=(id,txt,f=0)=>{const t=texter(figurer(get(id))[f]).find(t=>t.txt===txt);assert.ok(t,`${id} ${txt}`);return{x:+attr(t.tag,'x'),y:+attr(t.tag,'y')};};
  for(const[id,bc]of[['3.520','BC = 20 cm'],['3.521','BC = 9 cm'],['3.529','BC = 20 cm']])assert.ok(Math.abs(pos(id,bc).x-pos(id,'D').x)>50,`${id}: BC-etiketten under D`);
  assert.ok(pos('3.607','D').y-pos('3.607','2').y>25,'3.607: 2 och D staplade');
  assert.ok(pos('3.121','föremål 1,80 m').y<60&&pos('3.121','3,0 m').x===125,'3.121');assert.match(figurer(get('3.121'))[0],/M65 256v12M185 256v12M65 262H185/);
  assert.match(figurer(get('3.2102'))[0],/viewBox="0 0 432 230"/);assert.match(figurer(get('3.458'))[0],/viewBox="0 0 300 250"/);
  assert.match(figurer(get('3.2157'))[0],/x2="200.0" y2="71.0"/,'3.2157: minutvisaren täcker inte 12');
  assert.ok(pos('3.2160','30 cm').y<49,'3.2160: radieetiketten ovanför hjulet');
});
