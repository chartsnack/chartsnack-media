// YouTube Studio upload helpers (2026-11-17). Paste into the Studio tab (videos/short page) once per page load.
window.requestAnimationFrame = cb => setTimeout(()=>cb(performance.now()),16); window.cancelAnimationFrame = id => clearTimeout(id); window.sleep=ms=>new Promise(r=>setTimeout(r,ms));
window.ytOpen=async(url)=>{ [...document.querySelectorAll('tp-yt-paper-item')].find(e=>e.innerText.trim()=='Videos hochladen').click(); await sleep(2500);
 let inp; for(let i=0;i<20&&!(inp=document.querySelector('ytcp-uploads-file-picker input[type=file], input[type=file]'));i++) await sleep(500);
 const b=await (await fetch(url,{cache:'no-store'})).blob(); const f=new File([b],url.split('/').pop(),{type:'video/mp4'}); const dt=new DataTransfer(); dt.items.add(f);
 inp.files=dt.files; inp.dispatchEvent(new Event('change',{bubbles:true})); return b.size;};
window.setTB=(el,txt)=>{el.focus(); getSelection().selectAllChildren(el); document.execCommand('insertText',false,txt);};
window.ytDetails=async(title,desc)=>{ let tb; for(let i=0;i<30;i++){tb=document.querySelectorAll('ytcp-uploads-dialog #textbox'); if(tb.length>=2)break; await sleep(500);}
 setTB(tb[0],title); await sleep(300); setTB(tb[1],desc); await sleep(500);
 document.querySelectorAll('ytcp-social-suggestions-dropdown tp-yt-paper-dialog').forEach(d=>d.close&&d.close());
 document.querySelector('tp-yt-paper-radio-button[name=VIDEO_MADE_FOR_KIDS_NOT_MFK]').click(); await sleep(300);
 document.querySelector('ytcp-uploads-dialog #toggle-button')?.click(); await sleep(1000); return [tb[0].innerText];};
window.ytDate=async(value)=>{ const dpkr=document.querySelector('ytcp-date-picker'); const pin=dpkr.querySelector('tp-yt-paper-input'); const inp=pin.querySelector('input')||dpkr.querySelector('input');
 inp.value=value; if(pin) pin.value=value; dpkr.onDateTextChange({target:pin||inp, detail:{value}}); dpkr.onFormSubmit(new Event('submit')); await sleep(800);};
window.ytFocusTime=()=>{const ins=[...document.querySelectorAll('ytcp-datetime-picker input')].filter(i=>/:/.test(i.value)); const i=ins[0]; i.focus(); i.select(); return i.value;};
window.ytToSched=async(date)=>{const dl=document.querySelector('ytcp-uploads-dialog'); for(let i=0;i<3;i++){dl.querySelector('#next-button').click(); await sleep(1500);}
 dl.querySelector('#second-container-expand-button').click(); await sleep(1200); dl.querySelector('#datepicker-trigger')?.click(); await sleep(1000);
 await ytDate(date); return [ytFocusTime(), dl.querySelector('#datepicker-trigger')?.innerText];};
window.ytCloseShare=async()=>{ const b=[...document.querySelectorAll('ytcp-button, button')].filter(b=>b.offsetParent&&/^Schließen$/.test(b.innerText.trim())); b.forEach(x=>x.click()); await sleep(1500); return b.length;};
window.ytDone=async()=>{const dl=document.querySelector('ytcp-uploads-dialog'); let ok=false; for(let i=0;i<35;i++){const b=dl.querySelector('#done-button'); if(b&&!b.hasAttribute('disabled')&&b.getAttribute('aria-disabled')!=='true'){b.click(); ok=true; break;} if(/Upload-Limit/.test(document.body.innerText)) return 'LIMIT'; await sleep(1000);} await sleep(4000);
 const n=await ytCloseShare(); return [ok, n];};
// ytUp(NN, title, desc, 'dd.mm.yyyy') -> then computer type "12:00" + Return in the focused time field -> ytFinish('12:00','dd.mm.yyyy')
window.ytUp=async(n,title,desc,date)=>{ await ytCloseShare(); [...document.querySelectorAll('ytcp-button')].find(b=>b.innerText.trim()=='Erstellen').click(); await sleep(1000);
 const sz=await ytOpen(`https://raw.githubusercontent.com/chartsnack/chartsnack-media/main/queue/ep${n}.mp4`);
 const r=await ytDetails(title,desc); const y=document.querySelector('tp-yt-paper-radio-button[name=VIDEO_HAS_ALTERED_CONTENT_YES]'); y.click(); await sleep(500);
 const ai=y.getAttribute('aria-checked'); const s=await ytToSched(date); return [sz, r[0], ai, s];};
window.ytFinish=async(tm,dt)=>{await sleep(600); const v=[[...document.querySelectorAll('ytcp-datetime-picker input')].map(i=>i.value)[0], document.querySelector('ytcp-uploads-dialog #datepicker-trigger')?.innerText]; if(v[0]!=tm||v[1]!=dt) return ['MISMATCH',v]; return [v, await ytDone()];};
window.ytIds=()=>[...document.querySelectorAll('ytcp-video-row')].slice(0,14).map(r=>(r.querySelector('a[href*="/video/"]')?.getAttribute('href')||'').split('/')[2]+' '+r.innerText.replace(/\s+/g,' ').slice(5,40)+' '+(r.innerText.match(/Geplant|Öffentlich|Privat|Entwurf/)||[''])[0]);
'ok'
