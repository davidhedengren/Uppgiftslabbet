'use strict';
const {chromium}=require('playwright'),path=require('node:path'),assert=require('node:assert/strict');
(async()=>{const b=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']});try{
 const p=await b.newPage(),errors=[];p.on('pageerror',e=>errors.push(e.message));await p.route('https://*.supabase.co/**',r=>r.abort());await p.route('https://fonts.googleapis.com/**',r=>r.fulfill({body:''}));
 if(process.env.REVIEW_DEPS)await p.route(/^https:\/\/cdn\.jsdelivr\.net\/npm\/(katex|nerdamer)@/,r=>{const m=new URL(r.request().url()).pathname.match(/^\/npm\/(katex|nerdamer)@[^/]+\/(.+)$/);return r.fulfill({path:path.join(process.env.REVIEW_DEPS,m[1],m[2])})});
 await p.goto(process.env.REVIEW_URL);await p.waitForFunction(()=>typeof väljKurs==='function');await p.evaluate(()=>{document.body.classList.remove('password-locked');document.getElementById('passwordGate').hidden=true});assert.equal(await p.evaluate(()=>väljKurs(KURSER.find(k=>k.id==='ma2'),document.querySelector('[data-kurs="ma2"]'))),true);
 for(const width of [390,1280]){await p.setViewportSize({width,height:900});for(const [id,names] of [['3.692','ABCPQR'],['3.695','ABCXYZ']]){
  assert.equal(await p.evaluate(id=>{state.spår='2c';byggTräd();const q=variantBank().find(q=>q.id===id);if(!q)return false;state.omr=new Set([q.kap+':'+q.omr]);const pos=urval().findIndex(q=>q.id===id);rita(Math.floor(pos/UPPGIFTER_PER_SIDA));return pos>=0},id),true,id);
  const card=p.locator(`article.kort[data-id="${id}"]`);await card.scrollIntoViewIfNeeded();const texts=await card.locator('svg text').allTextContents();for(const n of names)assert.ok(texts.includes(n),id+' '+n);if(id==='3.695')assert.equal(await card.locator('.ul-alt').count(),4);await card.locator('.facitknapp').click();assert.equal(await card.locator('.katex-error').count(),0,id);
 }}assert.deepEqual(errors,[]);console.log('Båda lärarkorten visar hörn och facit på mobil och dator.');
}finally{await b.close()}})().catch(e=>{console.error(e);process.exitCode=1});
