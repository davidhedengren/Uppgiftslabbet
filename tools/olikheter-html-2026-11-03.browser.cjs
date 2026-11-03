'use strict';
const {chromium}=require('playwright'),path=require('node:path'),assert=require('node:assert/strict');
(async()=>{const browser=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']});try{
 const p=await browser.newPage(),errors=[];p.on('pageerror',e=>errors.push(e.message));await p.route('https://*.supabase.co/**',r=>r.abort());await p.route('https://fonts.googleapis.com/**',r=>r.fulfill({body:''}));
 if(process.env.REVIEW_DEPS)await p.route(/^https:\/\/cdn\.jsdelivr\.net\/npm\/(katex|nerdamer)@/,r=>{const m=new URL(r.request().url()).pathname.match(/^\/npm\/(katex|nerdamer)@[^/]+\/(.+)$/);return r.fulfill({path:path.join(process.env.REVIEW_DEPS,m[1],m[2])})});
 await p.goto(process.env.REVIEW_URL);await p.waitForFunction(()=>typeof väljKurs==='function');await p.evaluate(()=>{document.body.classList.remove('password-locked');document.getElementById('passwordGate').hidden=true});
 for(const width of [390,1280]){await p.setViewportSize({width,height:900});for(const [course,id] of [['ma2','2.1091'],['mato1','2.1152']]){
  assert.equal(await p.evaluate(course=>väljKurs(KURSER.find(k=>k.id===course),document.querySelector(`[data-kurs="${course}"]`)),course),true);
  assert.equal(await p.evaluate(({course,id})=>{state.spår=course==='ma2'?'2c':'1c';byggTräd();const q=variantBank().find(q=>q.id===id);if(!q)return false;state.omr=new Set([q.kap+':'+q.omr]);const pos=urval().findIndex(q=>q.id===id);rita(Math.floor(pos/UPPGIFTER_PER_SIDA));return pos>=0},{course,id}),true,id);
  const card=p.locator(`article.kort[data-id="${id}"]`);await card.scrollIntoViewIfNeeded();assert.equal(await card.locator('.ul-alt').count(),4,id);assert.equal(await card.locator('.katex-error').count(),0,id);
  if(id==='2.1091'){await p.waitForFunction(()=>[...document.querySelectorAll('article.kort[data-id="2.1091"] .katex annotation')].some(x=>x.textContent==='0<x<4'));await card.screenshot({path:`/tmp/olikhet21091-after-ul-${width}.png`});const a=await card.locator('.katex annotation').allTextContents();assert.ok(a.includes('0<x<4'),JSON.stringify(a));assert.ok(a.includes('0<x<2'),JSON.stringify(a));}
  await card.locator('.facitknapp').click();assert.equal(await card.locator('.katex-error').count(),0,id+' facit');if(id==='2.1091')assert.ok((await card.locator('.katex annotation').allTextContents()).includes('0<x<4'));
 }}assert.deepEqual(errors,[]);console.log('Lärarkort och facit visar alternativen korrekt på mobil och dator.');
}finally{await browser.close()}})().catch(e=>{console.error(e);process.exitCode=1});
