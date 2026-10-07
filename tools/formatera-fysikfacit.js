/* Formatering av befintliga matematik- och fysiklösningar i en DOM-miljö.
 * Ändrar bara presentation: okänd matematisk syntax lämnas orörd.
 * struktureraFacit kontrollerar att ursprunglig text kan återvinnas.
 * Kör inte en bankändring utan den fulla innehålls- och konsumentkontrollen.
 */
/* Konservativ typografisk översättning. Okänd text lämnas som text. */
function facitMatte(raw){
  const greek={ρ:'\\rho',θ:'\\theta',α:'\\alpha',β:'\\beta',γ:'\\gamma',λ:'\\lambda',μ:'\\mu',π:'\\pi',η:'\\eta',τ:'\\tau',Δ:'\\Delta',Σ:'\\Sigma',ω:'\\omega',ε:'\\varepsilon',φ:'\\varphi'};
  const sup={'⁰':'0','¹':'1','²':'2','³':'3','⁴':'4','⁵':'5','⁶':'6','⁷':'7','⁸':'8','⁹':'9','⁻':'-','⁺':'+'};
  const sub={'₀':'0','₁':'1','₂':'2','₃':'3','₄':'4','₅':'5','₆':'6','₇':'7','₈':'8','₉':'9','ₙ':'n','ₓ':'x'};
  let s=raw.trim().replace(/[.。]$/,'').trim();
  if(!/[=≈]/.test(s)||/[<>]/.test(s)||s.includes('\\'))return null;
  let unit='';
  const u=s.match(/\s+(°C|°|%|(?:[kMGTmunµμc]?)(?:kg|g|m|s|N|J|W|Pa|bar|K|V|A|C|Ω|Bq|Gy|Sv|eV|u|liter|l|h|min)(?:[²³]|\^(?:2|3))?(?:[·/](?:kg|m|s|K|mol|år|h|min)(?:[²³]|\^(?:2|3))?)*)([.]?)$/);
  // Ett g efter en variabel är tyngdaccelerationen, inte en gram-enhet.
  if(u&&/[0-9⁰¹²³⁴⁵⁶⁷⁸⁹)]$/.test(s.slice(0,u.index).trim())){unit=u[1];s=s.slice(0,u.index).trim();}
  const tokens=[];
  for(let i=0;i<s.length;){
    if(/\s/.test(s[i])){i++;continue;}
    const r=s.slice(i);let m;
    if(m=r.match(/^(?:\d{1,3}(?:[ \u00a0]\d{3})+|\d+)(?:[.,]\d+)?(?:[eE][+-]?\d+)?/)){tokens.push({type:'atom',tex:m[0].replace(/,/g,'{,}').replace(/[ \u00a0]/g,'\\,').replace(/[eE]([+-]?\d+)$/,'\\cdot10^{$1}'),raw:m[0],numeric:true});i+=m[0].length;continue;}
    if(m=r.match(/^(sin|cos|tan|ln|lg|log)(?![a-zåäö_])/)){tokens.push({type:'fn',tex:'\\'+m[0],raw:m[0]});i+=m[0].length;continue;}
    if(m=r.match(/^[A-Za-zρθαβγλμπητωεφΔΣ](?:[₀-₉ₙₓ]+|_[A-Za-zåäöÅÄÖ0-9]+)?/)){
      let symbol=m[0],base=symbol[0],suffix=symbol.slice(1),tex=greek[base]||base;
      if(suffix.startsWith('_'))tex+='_{\\mathrm{'+suffix.slice(1)+'}}';
      else if(suffix)tex+='_{'+[...suffix].map(x=>sub[x]).join('')+'}';
      tokens.push({type:'atom',tex,raw:symbol,numeric:false});i+=symbol.length;continue;
    }
    if(m=r.match(/^[⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺]+/)){tokens.push({type:'sup',tex:[...m[0]].map(x=>sup[x]).join(''),raw:m[0]});i+=m[0].length;continue;}
    if(s[i]==='°'){tokens.push({type:'sup',tex:'\\circ',raw:'°'});i++;continue;}
    const c=s[i],op={'−':'-','–':'-','·':'*','×':'*','*':'*','≈':'approx','=':'=', '+':'+','-':'-','/':'/','(':'(',')':')','[':'(',']':')','^':'^','√':'sqrt','|':'|'}[c];
    if(!op)return null;tokens.push({type:'op',tex:op,raw:c});i++;
  }
  // Prosa och okända ord får aldrig tolkas som variabelprodukter.
  const variableRuns=s.match(/[A-Za-zåäöÅÄÖ]{3,}/g)||[];
  for(const word of variableRuns){
    if(['sin','cos','tan','ln','lg','log'].includes(word))continue;
    if(new RegExp('_'+word+'(?:$|[^A-Za-zåäöÅÄÖ])').test(s))continue;
    if(['mgh','mghf','COP'].includes(word))continue;
    return null;
  }
  let at=0;
  function atom(){
    const t=tokens[at++];if(!t)throw 0;
    let n;
    if(t.type==='atom')n={tex:t.tex,numeric:t.numeric,group:false};
    else if(t.tex==='('){const a=expr(0);if(tokens[at++]?.tex!==')')throw 0;n={tex:'\\left('+a.tex+'\\right)',numeric:false,group:true,inside:a.tex};}
    else if(t.tex==='+'||t.tex==='-'){const a=atom();n={tex:t.tex+a.tex,numeric:a.numeric,group:false};}
    else if(t.tex==='sqrt'){const a=atom();n={tex:'\\sqrt{'+(a.group?a.inside:a.tex)+'}',numeric:false,group:false};}
    else if(t.type==='fn'){const a=atom();n={tex:t.tex+' '+a.tex,numeric:false,group:false};}
    else throw 0;
    if(tokens[at]?.type==='sup'){n.tex+='^{'+tokens[at++].tex+'}';n.numeric=false;}
    if(tokens[at]?.tex==='^'){at++;const p=atom();n.tex+='^{'+(p.group?p.inside:p.tex)+'}';n.numeric=false;}
    return n;
  }
  function expr(min){
    let left=atom();
    while(at<tokens.length){
      const t=tokens[at];if(t.tex===')'||t.tex==='='||t.tex==='approx')break;
      const implicit=t.type==='atom'||t.type==='fn'||t.tex==='('||t.tex==='sqrt';
      const op=implicit?'implicit':t.tex,prec=op==='+'||op==='-'?1:2;
      if(!['+','-','*','/','implicit'].includes(op)||prec<min)break;
      if(!implicit)at++;
      const right=expr(prec+1);
      if(op==='/')left={tex:'\\frac{'+left.tex+'}{'+(right.group?right.inside:right.tex)+'}',numeric:false,group:false};
      else left={tex:left.tex+(op==='implicit'?' ':op==='*'?'\\cdot ':op)+right.tex,numeric:false,group:false};
    }
    return left;
  }
  try{
    const parts=[expr(0).tex];let relations=0;
    while(at<tokens.length){const t=tokens[at++];if(!['=','approx'].includes(t.tex))return null;parts.push(t.tex==='='?'=':'\\approx ');parts.push(expr(0).tex);relations++;}
    if(!relations)return null;
    let tex=parts.join('');
    if(unit){
      let ut=unit.replace(/²/g,'^2').replace(/³/g,'^3').replace(/µ|μ/g,'\\mu ').replace(/Ω/g,'\\Omega').replace(/·/g,'\\,');
      tex+='\\, '+(unit==='%'?'\\%':unit==='°'?'{}^\\circ':unit==='°C'?'{}^\\circ\\mathrm{C}':'\\mathrm{'+ut+'}');
    }
    return tex;
  }catch(_){return null;}
}
if(typeof module!=='undefined')module.exports={facitMatte};

function facitAvslutandeMatte(html){
 const match=html.match(/^([\s\S]+?)\\\(([^]*?)\\\)\s*([.,;:]?)\s*$/);
 if(!match||/\\[()[\]]/.test(match[1]+match[2])||!/[=≈]|\\(?:Rightarrow|implies)/.test(match[2]))return null;
 return {prefix:match[1].trim(),tex:match[2],suffix:match[3]};
}

function struktureraFacit(source){
 if(/class=["'][^"']*\bfacit-stegvis\b/.test(source))return {html:source,ledger:[],unconverted:[],preserved:true};
 const protectedSvg=[];
 source=source.replace(/<svg\b[\s\S]*?<\/svg>/gi,s=>{protectedSvg.push(s);return '<span data-facit-figur="'+(protectedSvg.length-1)+'"></span>';});
 const root=document.createElement('div');root.innerHTML=source;
 const ledger=[],unconverted=[];
 const plainHtml=h=>{const d=document.createElement('div');d.innerHTML=h;return d.textContent;};
 const escape=s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
 function chunks(html){
  const stash=[];
  const protect=s=>{stash.push(s);return '\uE000'+(stash.length-1)+'\uE001';};
  let tmp=html.replace(/\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\]|<strong\b[^>]*>[\s\S]*?<\/strong>|<em\b[^>]*>[\s\S]*?<\/em>|<[^>]*>/gi,protect);
  tmp=tmp.replace(/([.!?])\s+(?=[A-ZÅÄÖÄÖΔρ0-9−√\uE000])|\s+(?=[a-h]\)\s)/g,'$1\uE002');
  tmp=tmp.replace(/(\uE001),\s+(?=\uE000)/g,'$1,\uE002');
  return tmp.split('\uE002').filter(s=>s.trim()).map(s=>s.replace(/\uE000(\d+)\uE001/g,(_,n)=>stash[+n]).trim());
 }
 function formula(html){
  const raw=plainHtml(html).trim();
  // Redan skriven matematik: flytta fristående beräkningar till egen rad.
  const tex=html.match(/^\s*\\\(([\s\S]+)\\\)\s*([.,;:]?)\s*$/);
  if(tex&&!/\\[()[\]]/.test(tex[1])&&/[=≈^_]|\\(?:frac|dfrac|sqrt|cdot)/.test(tex[1]))return '<div class="facit-matte">\\['+tex[1]+'\\]'+tex[2]+'</div>';
  // En förklaring med en enda avslutande beräkning hålls i samma steg.
  const trailing=facitAvslutandeMatte(html);
  if(trailing){
   return '<div class="facit-berakning"><p>'+trailing.prefix+'</p><div class="facit-matte">\\['+trailing.tex+'\\]'+trailing.suffix+'</div></div>';
  }
  if(/<[^>]*>/.test(html)||html.includes('\\'))return null;
  // Endast en helt igenkänd formel eller ett formelslut efter förklaringen.
  const starts=[0];for(const m of raw.matchAll(/\s+/g))starts.push(m.index+m[0].length);
  for(const from of starts){
   const candidate=raw.slice(from),tex=facitMatte(candidate);if(!tex)continue;
   const math='\\['+tex+'\\]';ledger.push({before:candidate,after:math});
   const prefix=raw.slice(0,from).trim();
   return '<div class="facit-berakning">'+(prefix?'<p class="facit-metod">'+escape(prefix)+'</p>':'')+'<div class="facit-matte">'+math+'</div></div>';
  }
  if(/[=≈]/.test(raw))unconverted.push(raw);
  return null;
 }
 function answer(html){return /^(?:\s*<[^>]+>)*\s*(?:Svar\s*:|Svaret (?:är|blir)|Rätt svar\s*:)/i.test(html)||/^\s*<strong\b[^>]*>[^<]+<\/strong>\s*$/.test(html);}
 function inlineNotation(html){
  const stash=[];
  let text=html.replace(/\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\]|<[^>]*>/g,s=>{stash.push(s);return '\uE000'+(stash.length-1)+'\uE001';});
  text=text.replace(/\b([A-Za-z]|mgh|COP)_([A-Za-zåäöÅÄÖ0-9]+)\b/g,(raw,base,sub)=>{
   const math='\\('+base+'_{\\mathrm{'+sub+'}}\\)';ledger.push({before:raw,after:math});return math;
  });
  return text.replace(/\uE000(\d+)\uE001/g,(_,i)=>stash[+i]);
 }
 function paragraph(p){
  if(p.classList.contains('facit-svar')||answer(p.innerHTML)){
   const d=document.createElement('p');d.className='facit-svar';d.innerHTML=p.innerHTML;return [d];
  }
  const out=[];
  for(let h of chunks(p.innerHTML)){
   if(answer(h)){
    const d=document.createElement('p');d.className='facit-svar';d.innerHTML=h;out.push(d);continue;
   }
   const f=formula(h);
   if(f){const holder=document.createElement('div');holder.innerHTML=f;out.push(...holder.children);}
   else {const d=document.createElement('p');d.className=p.className;d.innerHTML=inlineNotation(h);out.push(d);}
  }
  return out;
 }
 // Formatera stycken innan listorna ordnas. Inline-markering och figurer bevaras.
 for(const p of [...root.querySelectorAll('p')]){
  if(p.closest('.facit-matte'))continue;
  p.innerHTML=p.innerHTML.replace(/<(strong|b)>\s*([a-h])\)\s*<\/\1>/gi,'$2) ');
  if(p.classList.contains('facit-svar')||answer(p.innerHTML)){p.replaceWith(...paragraph(p));continue;}
  const segments=chunks(p.innerHTML),nodes=[];let body=null;
  for(const html of segments){
   const m=html.match(/^\s*([a-h])\)\s*([\s\S]*)$/),part=document.createElement('p');part.className=p.className;
   if(m){
    const group=document.createElement('div');group.className='facit-del';
    const mark=document.createElement('span');mark.className='facit-mark';mark.textContent=m[1]+')';
    body=document.createElement('div');body.className='facit-arbete';part.innerHTML=m[2];body.append(...paragraph(part));group.append(mark,body);nodes.push(group);
   }else{part.innerHTML=html;const content=paragraph(part);if(body)body.append(...content);else nodes.push(...content);}
  }
  if(p.classList.contains('facit-svar')||answer(p.innerHTML))p.replaceWith(...paragraph(p));else p.replaceWith(...nodes);
 }
 // Numrera verkliga innehållsblock; svar står för sig utanför räknestegen.
 function organize(parent){
  for(const el of [...parent.children]){
   if(el.matches('svg,span[data-facit-figur],.facit-matte,.facit-svar,.facit-berakning'))continue;
   if(el.tagName==='DIV'||el.tagName==='LI'||el.tagName==='OL'||el.tagName==='UL')organize(el);
  }
  if(!parent.matches('div,li')||parent.matches('.facit-matte,.facit-del,.facit-svar'))return;
  if(parent.classList.contains('facit-arbete')&&/^\d/.test(parent.parentElement.querySelector(':scope > .facit-mark')?.textContent||''))return;
  let list=null;
  for(const node of [...parent.childNodes]){
   if(node.nodeType===3&&!node.textContent.trim())continue;
   if(node.nodeType===1&&node.matches('p:not(.facit-svar),.facit-matte,.facit-berakning')){
    if(!list){list=document.createElement('ol');list.className='facit-steglista';list.setAttribute('role','list');parent.insertBefore(list,node);}
    const previous=list.lastElementChild;
    if(node.matches('.facit-matte')&&previous?.lastElementChild?.matches('p')&&/:\s*$/.test(previous.lastElementChild.textContent)){
     previous.append(node);continue;
    }
    const item=document.createElement('li');item.append(node);list.append(item);
   }else list=null;
  }
 }
 organize(root);
 let holder;
 if(root.children.length===1&&root.firstElementChild.matches('.facit-v2'))holder=root.firstElementChild;
 else{holder=document.createElement('div');holder.className='facit-v2';holder.append(...root.childNodes);root.append(holder);}
 holder.classList.add('facit-stegvis');
 let output=root.innerHTML.replace(/\sclass=""/g,'');
 for(let i=0;i<protectedSvg.length;i++)output=output.replace('<span data-facit-figur="'+i+'"></span>',protectedSvg[i]);
 // Kontrollerbar garanti: inget ursprungligt resonemang eller tal tappas bort.
 let reverted=output;
 for(const r of ledger)reverted=reverted.replace(r.after,r.before);
 const canonical=s=>plainHtml(s).replace(/\\[()[\]]/g,'').replace(/\s/g,'');
 const original=source.replace(/<span data-facit-figur="(\d+)"><\/span>/g,(_,i)=>protectedSvg[+i]);
 return {html:output,ledger,unconverted,preserved:canonical(original)===canonical(reverted),before:canonical(original),after:canonical(reverted)};
}

if(typeof module!=="undefined")Object.assign(module.exports,{struktureraFacit,facitAvslutandeMatte});
