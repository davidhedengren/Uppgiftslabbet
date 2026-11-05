'use strict';
/* Styr GeoGebra Classic (svenska) i en dold Chrome via Chrome DevTools Protocol, utan externa paket.
   Används för att ta riktiga skärmbilder till statistikfacit (agent/MA2_STATISTIK_GEOGEBRA_*.md).
   Kräver Chrome i C:\Program Files\Google\Chrome\Application\ och Node 22+ (inbyggd WebSocket). */
const {spawn}=require('node:child_process');
const fs=require('node:fs'),path=require('node:path');
const CHROME='C:/Program Files/Google/Chrome/Application/chrome.exe';
const vila=ms=>new Promise(r=>setTimeout(r,ms));

async function starta({port=9333,profil,bredd=1100,hojd=640,skala=2}={}){
  const proc=spawn(CHROME,[`--headless=new`,`--remote-debugging-port=${port}`,`--user-data-dir=${profil}`,
    '--lang=sv','--no-first-run','--no-default-browser-check','--disable-extensions',`--window-size=${bredd},${hojd}`,'about:blank'],{stdio:'ignore'});
  let lista=null;
  for(let i=0;i<60 && !lista;i++){ try{ lista=await (await fetch(`http://127.0.0.1:${port}/json/list`)).json(); }catch(_){ await vila(250); } }
  const sida=lista.find(x=>x.type==='page');
  const ws=new WebSocket(sida.webSocketDebuggerUrl);
  await new Promise((ok,fel)=>{ ws.onopen=ok; ws.onerror=fel; });
  let nr=0; const vantar=new Map();
  ws.onmessage=e=>{ const m=JSON.parse(e.data); if(m.id&&vantar.has(m.id)){ const {ok,fel}=vantar.get(m.id); vantar.delete(m.id); m.error?fel(new Error(JSON.stringify(m.error))):ok(m.result); } };
  const send=(method,params={})=>new Promise((ok,fel)=>{ const id=++nr; vantar.set(id,{ok,fel}); ws.send(JSON.stringify({id,method,params})); });
  await send('Page.enable'); await send('Runtime.enable');
  await send('Emulation.setDeviceMetricsOverride',{width:bredd,height:hojd,deviceScaleFactor:skala,mobile:false});
  const evaluate=async(expr)=>{ const r=await send('Runtime.evaluate',{expression:expr,awaitPromise:true,returnByValue:true}); if(r.exceptionDetails) throw new Error(r.exceptionDetails.exception?.description||r.exceptionDetails.text); return r.result.value; };
  const mus=async(typ,x,y,extra={})=>send('Input.dispatchMouseEvent',{type:typ,x,y,button:'left',clickCount:1,...extra});
  const klick=async(x,y,mod=0)=>{ await mus('mouseMoved',x,y,{modifiers:mod}); await mus('mousePressed',x,y,{modifiers:mod}); await mus('mouseReleased',x,y,{modifiers:mod}); await vila(250); };
  const dra=async(x1,y1,x2,y2)=>{ await mus('mouseMoved',x1,y1); await mus('mousePressed',x1,y1); for(let i=1;i<=8;i++) await mus('mouseMoved',x1+(x2-x1)*i/8,y1+(y2-y1)*i/8,{buttons:1}); await mus('mouseReleased',x2,y2); await vila(300); };
  const hjul=async(x,y,dx,dy)=>{ await send('Input.dispatchMouseEvent',{type:'mouseWheel',x,y,deltaX:dx,deltaY:dy}); await vila(300); };
  const tangent=async(key,code,vk)=>{ for(const type of ['keyDown','keyUp']) await send('Input.dispatchKeyEvent',{type,key,code,windowsVirtualKeyCode:vk}); await vila(150); };
  const bild=async(fil,clip)=>{ const r=await send('Page.captureScreenshot',{format:'png',...(clip?{clip:{...clip,scale:1}}:{}),captureBeyondViewport:false}); fs.writeFileSync(fil,Buffer.from(r.data,'base64')); return fil; };
  const ga=async(url)=>{ await send('Page.navigate',{url}); await vila(1500); };
  const stang=async()=>{ try{ ws.close(); }catch(_){} proc.kill(); await vila(300); };
  return {send,evaluate,klick,dra,hjul,tangent,bild,ga,stang,vila,bredd,hojd};
}
module.exports={starta,vila};
