'use strict';
const CACHE='canyon-guide-v1:'+self.registration.scope;
const FILES=['./','./index.html','./style.css','./app.js','./content.json','./manifest.webmanifest','./icon.svg','./icon-192.png','./icon-512.png','./assets/death.jpg','./assets/grand.jpg','./assets/page.jpg'];
const abs=p=>new URL(p,self.registration.scope).href;
self.addEventListener('install',e=>e.waitUntil(self.skipWaiting()));
self.addEventListener('activate',e=>e.waitUntil((async()=>{await self.clients.claim();})()));
self.addEventListener('message',e=>{
 const reply=x=>e.ports[0]&&e.ports[0].postMessage(x);
 e.waitUntil((async()=>{try{
 if(e.data.type==='DOWNLOAD'){
 const entries=await Promise.all(FILES.map(async p=>{const u=abs(p),r=await fetch(u,{cache:'reload'});if(!r.ok)throw new Error('部分內容下載失敗，請保持連線再試。');return [u,r];}));
 const cache=await caches.open(CACHE);await Promise.all(entries.map(([u,r])=>cache.put(u,r)));reply({ready:true});
 }else if(e.data.type==='STATUS'){
 const cache=await caches.open(CACHE);const found=await Promise.all(FILES.map(p=>cache.match(abs(p))));const content=await cache.match(abs('./content.json'));let revision=null;try{revision=content?(await content.clone().json()).revision:null}catch{}reply({ready:found.every(Boolean),revision});
 }
 }catch(err){reply({error:err.message||'下載失敗，請稍後重試。'});}})());
});
self.addEventListener('fetch',e=>{
 if(e.request.method!=='GET'||new URL(e.request.url).origin!==self.location.origin)return;
 e.respondWith((async()=>{
 try{const r=await fetch(e.request);if(r.ok)return r;throw new Error('unavailable');}
 catch{const cache=await caches.open(CACHE);const hit=await cache.match(e.request,{ignoreSearch:true});if(hit)return hit;if(e.request.mode==='navigate'){const shell=await cache.match(abs('./index.html'));if(shell)return shell;}return new Response('尚未下載此內容。請連線後先下載離線導覽。',{status:503,headers:{'Content-Type':'text/plain;charset=utf-8'}});}
 })());
});
