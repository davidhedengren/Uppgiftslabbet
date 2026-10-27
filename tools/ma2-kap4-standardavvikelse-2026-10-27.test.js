'use strict';
/* Ma2 kap 4 etapp 4: standardavvikelse (2026-10-27). Facit enligt Ma1 #1.116 med kortspecifika rubriker.
   4a: de 29 korten med delar (4.328–4.351, 4.364–4.366, 4.371, 4.372). Beräkningarna byggdes ur datan och kontrolleras här
   mot rättSvar: kvadratsumma, Sx med n − 1 och svarsrad. Tecknet i 4.338 (”2−−0,5”) är rättat. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const L=c.window.BANKMA2.filter(q=>q.omr==='standardavvikelse'&&q.kap===4),get=id=>L.find(q=>q.id===id);
const ren=s=>(s||'').replace(/<svg[\s\S]*?<\/svg>/g,' ').replace(/<[^>]+>/g,' ').replace(/\s+/g,' ').trim();
const rubriker=s=>[...(s||'').matchAll(/class="facit-rubrik">([\s\S]*?)<\/p>/g)].map(m=>ren(m[1]));
function facit(namn,s){assert.match(s,/facit-svar/,`${namn}: svarsrad`);const st=(s.match(/<li>/g)||[]).length+(s.match(/class="facit-stycke"/g)||[]).length,r=rubriker(s);assert.ok(st>0&&r.length>=st,`${namn}: ${st} steg men ${r.length} rubriker`);}
const ETAPP4A=['4.328','4.329','4.330','4.331','4.332','4.333','4.334','4.335','4.336','4.337','4.338','4.339','4.340','4.341','4.342','4.343','4.344','4.345','4.346','4.347','4.348','4.349','4.350','4.351','4.364','4.365','4.366','4.371','4.372'];
const tal=x=>Array.isArray(x)?x.flatMap(tal):typeof x==='number'?[x]:[];
test('4a: facit med rubrik per steg och delkort med eget facit och ledtråd',()=>{
  for(const id of ETAPP4A){const q=get(id);facit(id,q.s);for(const d of q.spelDelar||[]){facit(id+d.etikett,d.s);assert.ok(ren(d.ledtrad).length>10,id+d.etikett);}}
});
test('4a: svarsraderna innehåller alla tal i rättSvar',()=>{
  for(const id of ETAPP4A){const q=get(id),svar=[...q.s.matchAll(/facit-svar"><strong>Svar:<\/strong> ([^<]*)</g)].map(m=>m[1]).join(' ; '),f=(svar.match(/−?\d+(?:,\d+)?/g)||[]).map(x=>+x.replace('−','-').replace(',','.'));
    for(const t of tal(JSON.parse(JSON.stringify(q.rättSvar))))assert.ok(f.some(x=>Math.abs(x-t)<=0.051),`${id}: ${t} saknas i ”${svar}”`);}
});
test('4a: varje Sx i facit är kvadratsumman delad med n − 1',()=>{
  for(const id of ETAPP4A){const s=get(id).s;for(const m of s.matchAll(/S_x=\\sqrt\{\\frac\{([\d\\,{}]+)\}\{(\d+)-1\}\}(?:\\approx|=)([\d{},]+)/g)){
    const num=x=>+x.replace(/\\,/g,'').replace('{,}','.');assert.ok(Math.abs(Math.sqrt(num(m[1])/(+m[2]-1))-num(m[3]))<0.006,`${id}: √(${m[1]}/${m[2]}−1) ≠ ${m[3]}`);}}
  assert.doesNotMatch(get('4.338').s,/--|−−/);assert.match(get('4.338').s,/2-\(-0\{,\}5\)=2\{,\}5/);
});
test('4a: rubriker och huvudledtrådar delas inte mellan korten',()=>{
  const rub={},led={};for(const id of ETAPP4A){const q=get(id);(led[q.ledtrad]=led[q.ledtrad]||[]).push(id);for(const r of new Set([q.s,...(q.spelDelar||[]).map(d=>d.s)].flatMap(rubriker)))(rub[r]=rub[r]||new Set()).add(id);}
  assert.deepEqual(Object.entries(rub).filter(([,v])=>v.size>1).map(([r,v])=>r+': '+[...v]),[]);assert.deepEqual(Object.values(led).filter(v=>v.length>1),[]);
});
