'use strict';
const {chromium}=require('playwright'),path=require('node:path'),assert=require('node:assert/strict');
(async()=>{const b=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']});try{
 const p=await b.newPage({viewport:{width:1280,height:900}}),errors=[];p.on('pageerror',e=>errors.push(e.message));await p.route('https://*.supabase.co/**',r=>r.abort());await p.route('https://fonts.googleapis.com/**',r=>r.fulfill({body:''}));
 if(process.env.REVIEW_DEPS)await p.route(/^https:\/\/cdn\.jsdelivr\.net\/npm\/(katex|nerdamer)@/,r=>{const m=new URL(r.request().url()).pathname.match(/^\/npm\/(katex|nerdamer)@[^/]+\/(.+)$/);return r.fulfill({path:path.join(process.env.REVIEW_DEPS,m[1],m[2])})});
 await p.goto(process.env.REVIEW_URL||'http://127.0.0.1:8223');await p.waitForFunction(()=>typeof väljKurs==='function');
 await p.evaluate(()=>{document.body.classList.remove('password-locked');document.getElementById('passwordGate').hidden=true;});
 assert.equal(await p.evaluate(async()=>väljKurs(KURSER.find(k=>k.id==='mato2'),document.querySelector('[data-kurs="mato2"]'))),true);
 for(const id of ['1.20','1.38','1.41','1.145']){
  const found=await p.evaluate(id=>{state.spår='2c';byggTräd();const q=variantBank().find(q=>q.id===id);state.omr=new Set([q.kap+':'+q.omr]);const pos=urval().findIndex(q=>q.id===id);rita(Math.floor(pos/UPPGIFTER_PER_SIDA));return pos>=0},id);assert.equal(found,true,id);
  const card=p.locator(`article.kort[data-id="${id}"]`);await card.scrollIntoViewIfNeeded();await card.locator('.facitknapp').click({timeout:5000});const txt=await card.innerText();assert.match(txt,/Svar:/,id);assert.doesNotMatch(txt,/ekvivalenskedja|periodiciteten|Vid olikheter/,id);assert.equal(await card.locator('.katex-error').count(),0,id);
  if(id==='1.38')await card.screenshot({path:'/tmp/ma4-trig-labbet.png'});
 }
 assert.deepEqual(errors,[]);console.log('Fyra helfacit visas utan KaTeX-fel i Uppgiftslabbet.');
 }finally{await b.close()}})().catch(e=>{console.error(e);process.exitCode=1});
