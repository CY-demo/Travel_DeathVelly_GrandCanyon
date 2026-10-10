'use strict';
const scriptURL=new URL(document.currentScript.src);
const base=new URL('./',scriptURL);
const font=document.getElementById('font');
function setLarge(on){document.body.classList.toggle('large',on);font.setAttribute('aria-pressed',String(on));font.textContent=on?'標準字':'大字';}
try{setLarge(localStorage.getItem('alaska-large')==='true')}catch{}
font.addEventListener('click',()=>{const on=!document.body.classList.contains('large');setLarge(on);try{localStorage.setItem('alaska-large',on)}catch{}});
const expand=document.getElementById('expand');
if(expand)expand.addEventListener('click',()=>{const details=[...document.querySelectorAll('.chapter details')];const open=details.some(d=>!d.open);details.forEach(d=>d.open=open);expand.textContent=open?'收合詳細介紹':'展開詳細介紹';});
let ready;
function worker(){if(!('serviceWorker' in navigator))return Promise.reject(new Error('此瀏覽器不支援離線下載。'));return ready||(ready=navigator.serviceWorker.register(new URL('sw.js',base),{scope:base.pathname}).then(()=>navigator.serviceWorker.ready));}
worker().catch(()=>{});
document.getElementById('offline').addEventListener('click',async()=>{
 const button=document.getElementById('offline'),status=document.getElementById('offline-status');button.disabled=true;button.textContent='下載中…';status.textContent='正在儲存全部公園介紹與照片。';
 try{const reg=await worker();await new Promise((resolve,reject)=>{const channel=new MessageChannel(),timer=setTimeout(()=>reject(new Error('下載逾時，請保持連線再試一次。')),90000);channel.port1.onmessage=e=>{clearTimeout(timer);e.data.ok?resolve():reject(new Error(e.data.error))};reg.active.postMessage({type:'DOWNLOAD'},[channel.port2]);});button.textContent='已儲存 ✓';status.textContent='此裝置已儲存導覽與照片。請先用飛航模式測試；更新後可再下載，外部連結仍需網路。';}
 catch(e){button.textContent='重試離線下載';status.textContent=e.message;}
 finally{button.disabled=false;}
});
