/* Lokala panelinställningar. Inga konto- eller dokumentdata ändras. */
(()=>{
  'use strict';
  const yta=document.querySelector('.arbetsyta');
  if(!yta)return;
  const key='ul-panelbredder-v1',desktop=matchMedia('(min-width:961px)');
  const min={vanster:200,hoger:260},max={vanster:360,hoger:520},mittMin=380;
  let val={},drag=null;
  try{
    const sparat=JSON.parse(localStorage.getItem(key));
    for(const sida of ['vanster','hoger']){
      if(Number.isFinite(sparat?.[sida]))val[sida]=Math.max(min[sida],Math.min(max[sida],sparat[sida]));
    }
  }catch(_){}
  const handtag={};
  const standard=()=>{
    const css=getComputedStyle(yta);
    return {vanster:parseFloat(css.getPropertyValue('--vanster-standard')),hoger:parseFloat(css.getPropertyValue('--hoger-standard'))};
  };
  function bredder(){
    return {vanster:yta.querySelector('.vänster').getBoundingClientRect().width,hoger:yta.querySelector('.höger').getBoundingClientRect().width};
  }
  function spara(){try{localStorage.setItem(key,JSON.stringify(val));}catch(_){}}
  function rita(){
    if(!desktop.matches||yta.hidden||!yta.clientWidth)return;
    const def=standard(),w=yta.clientWidth;
    // Behåll önskade bredder vid tillfälligt mindre fönster, men skydda mitten.
    let l=Math.max(min.vanster,Math.min(max.vanster,val.vanster??def.vanster));
    let r=Math.max(min.hoger,Math.min(max.hoger,val.hoger??def.hoger));
    const over=Math.max(0,l+r+mittMin-w);
    const krymp=Math.min(over,r-min.hoger);
    r-=krymp;l-=Math.min(over-krymp,l-min.vanster);
    yta.style.setProperty('--panel-vanster',l+'px');
    yta.style.setProperty('--panel-hoger',r+'px');
    for(const [sida,bredd,annan] of [['vanster',l,r],['hoger',r,l]]){
      handtag[sida].setAttribute('aria-valuenow',Math.round(bredd));
      handtag[sida].setAttribute('aria-valuemax',Math.floor(Math.min(max[sida],w-annan-mittMin)));
      handtag[sida].setAttribute('aria-valuetext',Math.round(bredd)+' pixlar');
    }
  }
  function andra(sida,bredd){
    const b=bredder(),annan=sida==='vanster'?'hoger':'vanster';
    // Ändra bara den valda sidan under dragning.
    val[annan]=b[annan];
    val[sida]=Math.max(min[sida],Math.min(max[sida],yta.clientWidth-b[annan]-mittMin,bredd));
    rita();
  }
  function avsluta(){
    if(!drag)return;
    const {el,id}=drag;drag=null;
    if(el.hasPointerCapture(id))el.releasePointerCapture(id);
    document.body.classList.remove('panelbredd-dras');spara();
  }
  for(const [sida,selector,namn] of [['vanster','.vänster','områdespanelen'],['hoger','.höger','provpanelen']]){
    const panel=yta.querySelector(selector),el=document.createElement('div');
    panel.id=panel.id||'panel-'+sida;
    el.className='panelavdelare';el.dataset.sida=sida;el.tabIndex=0;
    el.setAttribute('role','separator');el.setAttribute('aria-orientation','vertical');
    el.setAttribute('aria-label','Ändra bredd på '+namn);
    el.setAttribute('aria-controls',panel.id);el.setAttribute('aria-valuemin',min[sida]);
    el.title='Dra för att ändra bredd. Dubbelklicka för standardbredd. Du kan också använda piltangenterna eller Home.';
    handtag[sida]=el;yta.append(el);
    el.addEventListener('pointerdown',e=>{
      if(e.button!==0||!e.isPrimary||!desktop.matches)return;
      e.preventDefault();el.focus();
      drag={el,id:e.pointerId,x:e.clientX,start:bredder()[sida]};
      el.setPointerCapture(e.pointerId);document.body.classList.add('panelbredd-dras');
    });
    el.addEventListener('pointermove',e=>{
      if(!drag||drag.el!==el||drag.id!==e.pointerId)return;
      andra(sida,drag.start+(e.clientX-drag.x)*(sida==='vanster'?1:-1));
    });
    for(const event of ['pointerup','pointercancel','lostpointercapture'])el.addEventListener(event,avsluta);
    const aterstall=()=>{delete val[sida];rita();spara();};
    el.addEventListener('dblclick',aterstall);
    el.addEventListener('keydown',e=>{
      if(e.key==='Home'){e.preventDefault();aterstall();}
      else if(e.key==='ArrowLeft'||e.key==='ArrowRight'){
        e.preventDefault();
        andra(sida,bredder()[sida]+(e.key==='ArrowRight'?1:-1)*(sida==='vanster'?1:-1)*(e.shiftKey?40:10));spara();
      }
    });
  }
  window.addEventListener('blur',avsluta);
  desktop.addEventListener('change',()=>{avsluta();rita();});
  new ResizeObserver(rita).observe(yta);
  rita();
})();
