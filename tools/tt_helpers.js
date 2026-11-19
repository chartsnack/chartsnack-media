// TikTok Studio upload helpers (2026-11-17). Paste into https://www.tiktok.com/tiktokstudio/upload after every page load.
// Flow: ttInject(cloudinaryUrl); ttCaption('text + emoji '); computer "type" each hashtag + space (7 tags);
//       ttSched('yyyy-mm-dd','hh','mm') -> verify; ttPlan() -> usually 'dialog-cancelled' (check still running);
//       next call: ttWaitOk() (check finishes within seconds AFTER the first Planen click) -> verify inputs -> ttPlan() -> '/tiktokstudio/content'.
window.requestAnimationFrame = cb => setTimeout(()=>cb(performance.now()),16); window.cancelAnimationFrame = id => clearTimeout(id); window.sleep=ms=>new Promise(r=>setTimeout(r,ms));
window.ttInject=async(url)=>{let inp; for(let i=0;i<30&&!(inp=document.querySelector('input[type=file]'));i++) await sleep(500); const b=await (await fetch(url)).blob(); const dt=new DataTransfer(); dt.items.add(new File([b],url.split('/').pop(),{type:'video/mp4'})); inp.files=dt.files; inp.dispatchEvent(new Event('change',{bubbles:true})); return b.size;};
window.ttCaption=async(txt)=>{let el; for(let i=0;i<40&&!(el=document.querySelector('[contenteditable=true]'));i++) await sleep(500); await sleep(1500); el.focus(); document.execCommand('selectAll'); document.execCommand('delete'); document.execCommand('insertText',false,txt); const r=document.createRange(); r.selectNodeContents(el); r.collapse(false); const s=getSelection(); s.removeAllRanges(); s.addRange(r); return el.innerText;};
window.ttSched=async(ymd,hh,mm)=>{ const ins=()=>[...document.querySelectorAll('input')];
 const lab=[...document.querySelectorAll('label, span, div')].filter(e=>e.children.length<3&&e.innerText?.trim()=='Zeitplan'); lab[0]?.click(); await sleep(1500);
 [...document.querySelectorAll('button')].find(b=>b.innerText.trim()=='Erlauben')?.click(); await sleep(800);
 const di=ins().find(i=>/^\d{4}-\d{2}-\d{2}$/.test(i.value)); di.click(); await sleep(800);
 const dd=+ymd.split('-')[2];
 for(let k=0;k<3;k++){ const tgt=[...document.querySelectorAll('span.day.valid')].find(s=>+s.innerText.trim()===dd); if(tgt){tgt.click(); break;} await sleep(500);}
 await sleep(800);
 const ti=ins().find(i=>/^\d{2}:\d{2}$/.test(i.value)); ti.click(); await sleep(1000);
 const pick=async(idx,val)=>{const list=document.querySelectorAll('.tiktok-timepicker-option-list')[idx]; const o=[...list.children].find(c=>c.innerText.trim()===val); o.scrollIntoView({block:'center'}); await sleep(200); (o.querySelector('*')||o).click(); await sleep(600);};
 await pick(0,hh); await pick(1,mm); await sleep(1500);
 return ins().filter(i=>/\d{4}-\d{2}-\d{2}|\d{2}:\d{2}/.test(i.value)).map(i=>i.value);};
window.ttPlan=async()=>{ for(let i=0;i<30;i++){ const b=[...document.querySelectorAll('button')].find(b=>b.innerText.trim()=='Planen'); if(b&&!b.disabled&&b.getAttribute('aria-disabled')!=='true'){ b.click(); break;} await sleep(1000);} await sleep(4000);
 const t=document.body.innerText; if(/Weiter und veröffentlichen/.test(t)){[...document.querySelectorAll('button')].find(b=>b.innerText.trim()=='Abbrechen')?.click(); return 'dialog-cancelled';} return location.pathname;};
window.ttWaitOk=async()=>{for(let i=0;i<20;i++){ if(/Keine Probleme gefunden/.test(document.body.innerText)) return true; await sleep(2000);} return false;};
'ok'
// --- direct publishing (since 2026-11-19): after caption + hashtags call ttPost(); if it returns 'check-dialog', call ttWaitOk() and ttPost() again.
window.ttPost=async()=>{ for(let i=0;i<30;i++){ const b=[...document.querySelectorAll('button')].find(b=>b.innerText.trim()=='Veröffentlichen'); if(b&&!b.disabled&&b.getAttribute('aria-disabled')!=='true'){ b.click(); break;} await sleep(1000);} await sleep(4000);
 const t=document.body.innerText; if(/Weiter und veröffentlichen/.test(t)){ const j=[...document.querySelectorAll('button')].find(b=>b.innerText.trim()=='Jetzt veröffentlichen'); if(j){ j.click(); await sleep(5000); return 'posted-now:'+location.pathname;} [...document.querySelectorAll('button')].find(b=>b.innerText.trim()=='Abbrechen')?.click(); return 'check-dialog';} return location.pathname;};
