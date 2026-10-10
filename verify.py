from pathlib import Path
from urllib.parse import urlsplit,unquote
from html.parser import HTMLParser
import json
class Doc(HTMLParser):
 def __init__(self,s):
  super().__init__();self.elements=[];self.feed(s)
 def handle_starttag(self,tag,attrs):self.elements.append((tag,dict(attrs)))
 def ids(self):return [a['id'] for t,a in self.elements if 'id' in a]
root=Path(__file__).parent/'dist'
pages=list(root.rglob('*.html'));assert len(pages)==12
for p in pages:
 s=p.read_text();doc=Doc(s)
 assert any(t=='meta' and a.get('name')=='viewport' for t,a in doc.elements)
 assert any(t=='h1' for t,a in doc.elements)
 assert len(doc.ids())==len(set(doc.ids()))
 for tag,a in doc.elements:
  if tag=='img':assert a.get('alt') and a.get('width') and a.get('height')
  for attr in ['href','src']:
   if attr not in a:continue
   link=a[attr];u=urlsplit(link)
   if u.scheme or u.netloc:continue
   target=(p.parent/unquote(u.path)).resolve() if u.path else p
   if target.is_dir():target=target/'index.html'
   assert target.is_relative_to(root.resolve()),(p,link)
   assert target.exists(),(p,link)
   if u.fragment and target.suffix=='.html':assert u.fragment in Doc(target.read_text()).ids(),(p,link)
 assert 'app.notion.com' not in s
 assert not any(x in s for x in ['原筆記','原始筆記','筆記提到','原路線'])
 assert not __import__('re').search(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',s)

for p in (root/'assets').glob('*.jpg'):assert p.read_bytes().startswith(b'\xff\xd8')
assert len(json.loads((root/'parks.json').read_text()))==6
print('PASS: 12 pages, local assets and anchors, 6 park entries, mobile viewport, and private itinerary markers.')
from itinerary import DAYS
assert len(DAYS)==9
kenai=(root/'parks/kenai-fjords/index.html').read_text()
denali=(root/'parks/denali/index.html').read_text()
assert '12:00–17:30' in kenai
assert '提前報名' in denali and '48 小時' in denali
for d in DAYS:
 s=(root/d['page']/'index.html').read_text()
 assert f'id="day-{d["n"]}"' in s
manifest=json.loads((root/'assets/spots/manifest.json').read_text())
assert len(manifest)>=12
for entry in manifest.values():
 assert (root/'assets/spots'/entry['file']).exists()
sw=(root/'sw.js').read_text()
assert './days/anchorage/' in sw
for entry in manifest.values():assert './assets/spots/'+entry['file'] in sw
print('PASS: nine complete day routes, selected noon sailing, Denali advance-booking instructions, spot photos, offline assets.')
