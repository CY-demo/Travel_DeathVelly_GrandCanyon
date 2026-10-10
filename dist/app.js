'use strict';
const scriptURL=new URL(document.currentScript.src),base=new URL('./',scriptURL);
const english=document.documentElement.lang==='en';
const t=(zh,en)=>english?en:zh;
const font=document.getElementById('font');
function setLarge(on){document.body.classList.toggle('large',on);font.setAttribute('aria-pressed',String(on));font.textContent=on?t('標準字','Standard text'):t('大字','Larger text');}
try{setLarge(localStorage.getItem('alaska-large')==='true')}catch{}
font.addEventListener('click',()=>{const on=!document.body.classList.contains('large');setLarge(on);try{localStorage.setItem('alaska-large',on)}catch{}});
// Preserve the current section when switching language, with usable HTML links as fallback.
function languageLinks(){document.querySelectorAll('.language-switch a').forEach(a=>{const u=new URL(a.href);u.hash=location.hash;a.href=u.href;});}
languageLinks();addEventListener('hashchange',languageLinks);
const expand=document.getElementById('expand');
if(expand)expand.addEventListener('click',()=>{const details=[...document.querySelectorAll('.chapter details')];const open=details.some(d=>!d.open);details.forEach(d=>d.open=open);expand.textContent=open?t('收合詳細介紹','Collapse detailed guides'):t('展開詳細介紹','Expand detailed guides');});
let ready;
function worker(){if(!('serviceWorker' in navigator))return Promise.reject(new Error(t('此瀏覽器不支援離線下載。','This browser does not support offline downloads.')));return ready||(ready=navigator.serviceWorker.register(new URL('sw.js',base),{scope:base.pathname}).then(()=>navigator.serviceWorker.ready));}
worker().catch(()=>{});
document.getElementById('offline').addEventListener('click',async()=>{
 const button=document.getElementById('offline'),status=document.getElementById('offline-status');button.disabled=true;button.textContent=t('下載中…','Saving…');status.textContent=t('正在儲存中英文導覽與照片。','Saving both languages and photos.');
 try{const reg=await worker();await new Promise((resolve,reject)=>{const channel=new MessageChannel(),timer=setTimeout(()=>reject(new Error(t('下載逾時，請保持連線再試一次。','Download timed out. Stay online and try again.'))),90000);channel.port1.onmessage=e=>{clearTimeout(timer);e.data.ok?resolve():reject(new Error(t('部分檔案未下載完成，請重新嘗試。','Some files could not be saved. Please try again.')))};reg.active.postMessage({type:'DOWNLOAD'},[channel.port2]);});button.textContent=t('已儲存 ✓','Saved ✓');status.textContent=t('此裝置已儲存中英文導覽與照片。可先用飛航模式測試；外部連結仍需網路。','Both languages and photos are saved on this device. Test in airplane mode; external links still need internet access.');}
 catch(e){button.textContent=t('重試離線下載','Retry offline download');status.textContent=e.message;}
 finally{button.disabled=false;}
});
