'use strict';
const $=s=>document.querySelector(s);
let data, activeDay, allExpanded=false;
const CONTENT_REVISION='2026-10-09-lounge-locations';
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function renderTable(t){return t?`<div class="table-scroll" tabindex="0" role="region" aria-label="${esc(t.caption)}"><table><caption>${esc(t.caption)}</caption><thead><tr>${t.headers.map(h=>`<th scope="col">${esc(h)}</th>`).join('')}</tr></thead><tbody>${t.rows.map(r=>`<tr>${r.map((v,i)=>i===0?`<th scope="row">${esc(v)}</th>`:`<td>${esc(v)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`:''}
function save(k,v){try{localStorage.setItem('canyon-'+k,v)}catch{}}
function read(k){try{return localStorage.getItem('canyon-'+k)}catch{return null}}
function goDay(id,restore){
 activeDay=data.days.find(d=>d.id===id)||data.days[0];allExpanded=false;
 $('#expandAll').textContent='展開全部介紹';
 $('#days').innerHTML=data.days.map(d=>`<button class="day-tab" data-day="${d.id}" aria-pressed="${d.id===activeDay.id}"><small>${esc(d.label)}</small><strong>${esc(d.title)}</strong></button>`).join('');
 $('#days').querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{location.hash=b.dataset.day}));
 $('#dayHero').classList.toggle('day-hero--text',!activeDay.image);
 $('#dayHero').innerHTML=`${activeDay.image?`<img src="${esc(activeDay.image)}" alt="${esc(activeDay.title)}真實景觀照片">`:''}<div class="hero-text"><p class="eyebrow" style="color:#efb974">${esc(activeDay.label)} · ${activeDay.chapters.length} 個閱讀章節</p><h2>${esc(activeDay.subtitle)}</h2><p>${esc(activeDay.summary)}</p><p class="timing">${esc(activeDay.timing)}</p></div>`;
 const airport=activeDay.kind==='airport';
 $('#expandAll').hidden=airport;
 $('#chapterHeading').textContent=activeDay.title+(airport?' · 位置':' · 分站介紹');
 $('#sectionLabel').textContent=airport?'貴賓室位置':'逐站探索地景';
 $('#readingNote').textContent=airport?'各貴賓室所在的登機區與鄰近登機門。':'每站都有詳細介紹、觀察重點與簡單走法。參考停留時間不等於當天保證。';
 $('#chapterNav').innerHTML=activeDay.chapters.map((c,i)=>`<a class="chapter-link" href="#${activeDay.id}/${c.id}" data-id="${c.id}"><span>${String(i+1).padStart(2,'0')}</span>${esc(c.title)}</a>`).join('');
 $('#chapters').innerHTML=activeDay.chapters.map((c,i)=>airport?`<article class="chapter" id="${c.id}"><h3>${esc(c.title)}</h3><p class="english">${esc(c.en)}</p><p class="lead" style="white-space:pre-line">${esc(c.lead)}</p></article>`:`<article class="chapter" id="${c.id}"><div class="chapter-top"><div><p class="eyebrow">${String(i+1).padStart(2,'0')} · ${esc(activeDay.title)}</p><h3>${esc(c.title)}</h3><p class="english">${esc(c.en)}</p></div></div><span class="badge ${/協調|替換|爭取|提醒/.test(c.status)?'conditional':''}">${esc(c.status)}</span><span class="time">${esc(c.time)}</span><p class="lead">${esc(c.lead)}</p>${renderTable(c.table)}<details ${i===0?'open':''}><summary>${esc(activeDay.detailLabel||'詳細介紹與形成故事')}</summary><div class="script">${c.paras.map(p=>`<p>${esc(p)}</p>`).join('')}</div></details><div class="observe"><strong>${esc(activeDay.lookLabel||'現場看什麼')}</strong><br>${esc(c.look)}</div><p class="walk"><strong>${esc(activeDay.walkLabel||'簡單走走與行程提醒')}</strong><br>${esc(c.walk)}</p><div class="refs">${c.sources.map(k=>`<a href="${esc(data.sources[k][1])}" target="_blank" rel="noopener">${esc(data.sources[k][0])}</a>`).join('')}</div></article>`).join('');
 save('day',activeDay.id);
 if(!restore) window.scrollTo({top:0,behavior:'instant'});
}
function route(){
 const [day,chapter]=location.hash.slice(1).split('/');
 if(!activeDay||day!==activeDay.id) goDay(day||read('day')||'death',!!chapter);
 if(chapter){const el=document.getElementById(chapter);if(el){const details=el.querySelector('details');if(details)details.open=true;requestAnimationFrame(()=>el.scrollIntoView({block:'start'}));save('chapter',day+'/'+chapter);document.querySelectorAll('.chapter-link').forEach(a=>a.classList.toggle('active',a.dataset.id===chapter));}}
}
$('#font').addEventListener('click',()=>{const on=document.body.classList.toggle('large');$('#font').setAttribute('aria-pressed',on);$('#font').textContent=on?'標準字':'大字';save('large',String(on));});
if(read('large')==='true'){$('#font').click()}
$('#helpOpen').onclick=()=>{$('#help').showModal();checkCache();};
$('#helpClose').onclick=()=>$('#help').close();
$('#help').addEventListener('click',e=>{if(e.target===$('#help')){const r=e.target.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)e.target.close();}});
$('#expandAll').onclick=()=>{allExpanded=!allExpanded;$('#chapters').querySelectorAll('details').forEach(d=>d.open=allExpanded);$('#expandAll').textContent=allExpanded?'收合詳細介紹':'展開全部介紹';};
function network(){$('#network').textContent=navigator.onLine?'已連線':'離線閱讀';}
window.addEventListener('online',network);window.addEventListener('offline',network);network();
let registration;
async function worker(){
 if(!('serviceWorker' in navigator))throw new Error('此瀏覽器不支援離線儲存，請改用Safari或Chrome。');
 registration=registration||await navigator.serviceWorker.register('./sw.js');
 return navigator.serviceWorker.ready;
}
function tellWorker(type){return new Promise(async(resolve,reject)=>{try{const reg=await worker();const channel=new MessageChannel();const timer=setTimeout(()=>reject(new Error('下載較久或網路不穩，請保持連線再試一次。')),90000);channel.port1.onmessage=e=>{clearTimeout(timer);e.data.error?reject(new Error(e.data.error)):resolve(e.data)};reg.active.postMessage({type},[channel.port2]);}catch(e){reject(e)}})}
async function checkCache(){try{const r=await tellWorker('STATUS');$('#offlineStatus').textContent=r.ready?(r.revision===CONTENT_REVISION?'行程文字、照片與 LAS 貴賓室資訊已儲存於此裝置。出發前請做飛航測試。':'已儲存較早版本；請重新下載以更新內容。'):'尚未完整儲存。請在有網路時下載。';}catch(e){$('#offlineStatus').textContent=e.message;}}
$('#download').onclick=async()=>{const b=$('#download');b.disabled=true;b.textContent='正在下載…';$('#offlineStatus').textContent='正在儲存全部行程、照片與 LAS 貴賓室資訊。';try{await tellWorker('DOWNLOAD');await checkCache();b.textContent='重新下載／更新內容';}catch(e){$('#offlineStatus').textContent=e.message;b.textContent='重試下載';}finally{b.disabled=false}};
fetch('./content.json').then(r=>{if(!r.ok)throw new Error('內容暫時無法載入');return r.json()}).then(d=>{data=d;route();window.addEventListener('hashchange',route);$('#sourceLinks').innerHTML=Object.values(data.sources).map(([name,url])=>`<a href="${esc(url)}" target="_blank" rel="noopener">${esc(name)}</a>`).join('');worker().catch(()=>{});}).catch(e=>{$('#chapters').innerHTML=`<p role="alert">${esc(e.message)}。首次使用需要網路；若已下載，請使用原本儲存的瀏覽器開啟。<button onclick="location.reload()">重新載入</button></p>`});
