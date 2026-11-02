'use strict';
const {chromium}=require('playwright'),path=require('node:path'),assert=require('node:assert/strict');
(async()=>{const b=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']});try{
 const p=await b.newPage(),errors=[];p.on('pageerror',e=>errors.push(e.message));await p.route('https://*.supabase.co/**',r=>r.abort());await p.route('https://fonts.googleapis.com/**',r=>r.fulfill({body:''}));
 if(process.env.REVIEW_DEPS)await p.route(/^https:\/\/cdn\.jsdelivr\.net\/npm\/(katex|nerdamer)@/,r=>{const m=new URL(r.request().url()).pathname.match(/^\/npm\/(katex|nerdamer)@[^/]+\/(.+)$/);return r.fulfill({path:path.join(process.env.REVIEW_DEPS,m[1],m[2])})});
 await p.goto(process.env.REVIEW_URL||'http://127.0.0.1:8295');await p.waitForFunction(()=>typeof väljKurs==='function');await p.evaluate(()=>{document.body.classList.remove('password-locked');document.getElementById('passwordGate').hidden=true;});
 assert.equal(await p.evaluate(()=>väljKurs(KURSER.find(k=>k.id==='ma1'),document.querySelector('[data-kurs="ma1"]'))),true);
 for(const width of [390,1280]){await p.setViewportSize({width,height:900});for(const id of ['0.55','0.87','0.256','0.540','0.740','0.744']){
 const found=await p.evaluate(id=>{state.spår='1a';byggTräd();const q=variantBank().find(q=>q.id===id);state.omr=new Set([q.kap+':'+q.omr]);const pos=urval().findIndex(q=>q.id===id);rita(Math.floor(pos/UPPGIFTER_PER_SIDA));return pos>=0},id);assert.equal(found,true,id);
 const card=p.locator(`article.kort[data-id="${id}"]`);await card.scrollIntoViewIfNeeded();const details=await card.evaluate(el=>({alts:el.querySelectorAll('.ul-alt').length,math:el.querySelectorAll('.katex').length,errors:el.querySelectorAll('.katex-error').length,text:el.textContent}));
 assert.equal(details.errors,0,id);assert.equal(details.alts,({'0.267':2,'0.280':2,'0.301':3,'0.309':3}[id]||4),id);
 await card.locator('.facitknapp').click();assert.equal(await card.locator('.katex-error').count(),0,id);
 }}assert.deepEqual(errors,[]);console.log('Alternativ, ruta och facit visas korrekt i Uppgiftslabbet på mobil och dator.');
 }finally{await b.close()}})().catch(e=>{console.error(e);process.exitCode=1});
