'use strict';
/* Ma2 kap 4 etapp 3: lådagram (2026-10-27). Facit enligt Ma1 #1.116 med kortspecifika rubriker, nya läsbara lådagram för
   mallkorten (4.03, 4.12, 4.18, 4.42, 4.67, 4.88) och de gamla småfigurerna (4.82, 4.108, 4.209, 4.210),
   rättade exempelmaterial i 4.82 och 4.165 (de gav fel Q3) och kommentarer till alla flervalsalternativ. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const L=c.window.BANKMA2.filter(q=>q.omr==='ladagram'&&q.kap===4),get=id=>L.find(q=>q.id===id);
const ren=s=>(s||'').replace(/<svg[\s\S]*?<\/svg>/g,' ').replace(/<[^>]+>/g,' ').replace(/\s+/g,' ').trim();
const rubriker=s=>[...(s||'').matchAll(/class="facit-rubrik">([\s\S]*?)<\/p>/g)].map(m=>ren(m[1]));
function facit(namn,s){assert.match(s,/facit-svar/,`${namn}: svarsrad`);const st=(s.match(/<li>/g)||[]).length+(s.match(/class="facit-stycke"/g)||[]).length,r=rubriker(s);assert.ok(st>0&&r.length>=st,`${namn}: ${st} steg men ${r.length} rubriker`);}
const at=(t,n)=>+t.match(new RegExp(`\\s${n}="([-\\d.]+)"`))[1];
// Läser femtalssammanfattningen ur ett lådagram ritat med lådans rect och tjockt medianstreck (stroke-width 3).
function femtal(svg){const ax=[...svg.matchAll(/<text\b([^>]*)>(-?[\d,]+)<\/text>/g)].map(m=>({x:at(m[1],'x'),y:at(m[1],'y'),v:+m[2].replace(',','.')}));
  const y0=Math.max(...ax.map(t=>t.y)),tick=ax.filter(t=>t.y===y0),a=tick[0],b=tick[tick.length-1],val=x=>+(a.v+(x-a.x)/(b.x-a.x)*(b.v-a.v)).toFixed(2);
  return [...svg.matchAll(/<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="26"/g)].map(r=>{const x=+r[1],y=+r[2]+13,w=+r[3];
    const caps=[...svg.matchAll(/<line x1="([\d.]+)" y1="([\d.]+)" x2="\1" y2="([\d.]+)" stroke="[^"]+" stroke-width="2"\/>/g)].filter(l=>+l[2]===y-9).map(l=>+l[1]);
    const med=[...svg.matchAll(/<line x1="([\d.]+)" y1="([\d.]+)" x2="\1" y2="[\d.]+" stroke="[^"]+" stroke-width="3"\/>/g)].find(l=>+l[2]===y-13);
    return [Math.min(...caps),x,+med[1],x+w,Math.max(...caps)].map(val);});}
test('Facit med rubrik per steg, delkort med eget facit och ledtråd, inga delade rubriker eller ledtrådar',()=>{
  assert.ok(L.length>=75);const rub={},led={};
  for(const q of L){facit(q.id,q.s);(led[q.ledtrad]=led[q.ledtrad]||[]).push(q.id);
    for(const d of q.spelDelar||[]){facit(q.id+d.etikett,d.s);assert.ok(ren(d.ledtrad).length>10,q.id+d.etikett);}
    for(const r of new Set([q.s,...(q.spelDelar||[]).map(d=>d.s)].flatMap(rubriker)))(rub[r]=rub[r]||new Set()).add(q.id);}
  assert.deepEqual(Object.entries(rub).filter(([,v])=>v.size>1).map(([r])=>r),[]);assert.deepEqual(Object.values(led).filter(v=>v.length>1),[]);
  for(const q of L.filter(q=>q.alternativ))for(const a of q.alternativ)assert.ok((a.kommentar||'').length>8,`${q.id}: ${a.txt}`);
});
test('De omritade lådagrammen visar värdena som facit använder',()=>{
  const F={'4.03':[[6,10,14,20,24]],'4.12':[[6,11,15,19,25]],'4.18':[[12,16,20,27,31]],'4.42':[[10,14,17,22,28]],'4.67':[[4,8,12,18,24]],'4.88':[[4,7,10,14,19]],
    '4.82':[[2,4,6,9,11]],'4.108':[[4,6,7,9,12],[3,5,7,10,11]],'4.209':[[3,7,10,15,19]],'4.210':[[2,6,10,14,18]]};
  for(const[id,v]of Object.entries(F)){const q=get(id),svg=q.t.match(/<svg[\s\S]*?<\/svg>/)[0];assert.deepEqual(femtal(svg),v,id);assert.doesNotMatch(svg,/IBM Plex Mono/,id);
    if(q.spelIntro)assert.ok(q.spelIntro.includes(svg),id+' intro');}
  assert.deepEqual(JSON.parse(JSON.stringify([get('4.03').rättSvar,get('4.12').rättSvar,get('4.18').rättSvar,get('4.42').rättSvar,get('4.67').rättSvar,get('4.88').rättSvar])),[[14,10,18],[15,8,19],[20,19,11],[14,22,8],[12,20],[10,7]]);
  const b={};for(const id of ['4.209','4.210'])b[get(id).t.match(/<svg[\s\S]*?<\/svg>/)[0].replace(/aria-label="[^"]*"/,'')]=id;assert.equal(Object.keys(b).length,2,'4.209 och 4.210 har olika figurer');
});
test('Exempelmaterialen i 4.82 och 4.165 ger de angivna kvartilerna',()=>{
  const md=a=>(a[(a.length-1)>>1]+a[a.length>>1])/2,fem=v=>[v[0],md(v.slice(0,4)),v[4],md(v.slice(5)),v[8]];
  assert.deepEqual(fem([2,3,5,5,6,7,8,10,11]),[2,4,6,9,11]);assert.match(get('4.82').s,/2,3,5,5,6,7,8,10,11/);
  assert.deepEqual(fem([2,4,6,7,8,9,10,12,18]),[2,5,8,11,18]);assert.match(get('4.165').s,/2,4,6,7,8,9,10,12,18/);
});
