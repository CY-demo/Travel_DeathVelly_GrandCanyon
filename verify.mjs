import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
const root=new URL('./dist/',import.meta.url);
const data=JSON.parse(fs.readFileSync(new URL('content.json',root)));
assert.equal(data.days.length,4);
assert.equal(data.days.flatMap(d=>d.chapters).length,30);
for(const d of data.days){
 if(d.image) assert(fs.existsSync(new URL(d.image,root)));
 for(const c of d.chapters) for(const source of c.sources) assert(data.sources[source]);
}
const manifest=JSON.parse(fs.readFileSync(new URL('manifest.webmanifest',root)));
for(const key of ['id','start_url','scope']) assert.equal(manifest[key],'./');
const html=fs.readFileSync(new URL('index.html',root),'utf8');
const app=fs.readFileSync(new URL('app.js',root),'utf8');
for(const m of app.matchAll(/\$\('#([A-Za-z]+)'\)/g)) assert(html.includes(`id="${m[1]}"`));
for(const base of ['https://cy-demo.github.io/Travel_DeathVelly_GrandCanyon/','https://example.test/']){
 let online=true;const handlers={},stored=new Map();
 const cache={async put(k,v){stored.set(k,v.clone())},async match(k){return stored.get(typeof k==='string'?k:k.url)?.clone()}};
 const ctx={URL,Response,Promise,console,caches:{open:async()=>cache},fetch:async req=>{
  if(!online)throw new Error('offline');
  const u=typeof req==='string'?req:req.url;
  assert(u.startsWith(base));
  const path=u.slice(base.length)||'index.html';
  const f=new URL(path,root);
  return fs.existsSync(f)?new Response(fs.readFileSync(f)):new Response('',{status:404});
 },self:{registration:{scope:base},location:{origin:new URL(base).origin},clients:{claim:async()=>{}},skipWaiting:async()=>{},addEventListener:(k,fn)=>handlers[k]=fn}};
 vm.createContext(ctx);vm.runInContext(fs.readFileSync(new URL('sw.js',root),'utf8'),ctx);
 async function message(type){let result,done;handlers.message({data:{type},ports:[{postMessage:r=>result=r}],waitUntil:p=>done=p});await done;return result}
 assert.equal((await message('STATUS')).ready,false);
 assert.equal((await message('DOWNLOAD')).ready,true);
 assert.equal((await message('STATUS')).revision,data.revision);
 online=false;
 for(const path of ['', 'index.html','content.json','assets/grand.jpg']){
  let response;handlers.fetch({request:{url:base+path,method:'GET',mode:path?'cors':'navigate'},respondWith:p=>response=p});
  assert.equal((await response).status,200);
 }
}
console.log('PASS: 30 chapters, sources, DOM IDs, relative manifest, offline download and reading at root and GitHub Pages subpath.');
