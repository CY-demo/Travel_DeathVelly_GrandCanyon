"""Public alternatives; indicative timing, never a confirmed booking."""
def section(title, paragraphs):
 return '<article class="chapter"><h3>'+title+'</h3>'+''.join('<p>'+p+'</p>' for p in paragraphs)+'</article>'
def sources(items):
 return '<div class="refs">'+''.join(f'<a href="{url}" target="_blank" rel="noopener">{label} ↗</a>' for label,url in items)+'</div>'
def render_extensions(slug):
 if slug not in ('katmai','wrangell-st-elias'):return ''
 body='<section id="alternatives"><div class="section-title"><p class="eyebrow">STAY LONGER / OTHER WAYS TO GO</p><h2>其他可行玩法：把時間留在當地</h2><p>以下是替代安排，不是九日路線已包含的行程。時間為規劃示例；住宿、交通與導覽須分別確認。</p></div>'
 if slug=='katmai':
  body+=section('Brooks Camp 露營，或 Brooks Lodge 住一晚',[
   '<strong>營地預訂與客房抽籤是兩件事。</strong>Brooks Camp 營地透過 Recreation.gov 分批開放預訂；Brooks Lodge 客房才採抽籤。以 2026 年為例，營地依入住月份分成 1 月 7 日、2 月 7 日、3 月 7 日開放；未來年度要查新公告，不要直接套用。',
   'Brooks Lodge 的 2027 年住宿抽籤已結束，可向業者詢問取消釋出的房間；2028 年住宿申請預計於 2026 年 12 月 1–30 日受理。若選露營，先取得營位，再確認往返交通，避免只有機票卻沒有合法過夜地點。',
   '<strong>裝備可以事先租，但不要抵達才賭庫存。</strong>當地 Trading Post 有租借與露營服務，公開價目未完整列出帳篷、睡袋、睡墊整套供應；請先逐項確認。也可在 Anchorage 的 Alaska Outdoor Gear Rental 預訂露營裝備，再確認航空行李限重、尺寸與燃料攜帶規定。',
   '住營地多了清晨與傍晚觀察機會，也少了當天急著離開的壓力；代價是自己處理露營與食物收納。營地有指定食物儲放與炊事區，電圍籬並不代表熊絕對不會進入。'])
  body+=section('水上飛機與船：都是從 King Salmon 接近 Brooks Camp',[
   '<strong>飛機：</strong>Anchorage → King Salmon，再轉水上飛機到 Brooks Camp，第二段飛行約 20 分鐘。日遊套裝與露營交通票不同，訂票時說明要過夜、裝備件數與回程日期。',
   '<strong>船：</strong>先飛到 King Salmon，陸路接駁約 15–20 分鐘到 Lake Camp，再橫越 Naknek Lake；天候良好時船程約 45 分鐘。這不是從 Anchorage 一路搭船過來，也不能保證較便宜或不受天氣影響。',
   '飛機會受能見度與天候影響，船也會受風浪影響。先核對 King Salmon 航班與接駁能否銜接；回到 Anchorage 後保留緩衝，再搭不可錯過的長程航班。'])
  body+=section('看熊季節怎麼挑？',[
   '<strong>7 月：</strong>以 Brooks Falls 鮭魚洄游、熊在瀑布附近捕魚的經典場景為目標，通常是優先考慮月份；人潮也多，平台可能需要輪候，不能保證看到跳魚或特定熊。',
   '<strong>9 月：</strong>熊可能在河流較下游覓食，適合接受不同場景、想看秋色的人。不要只盯著瀑布平台；先確認當年 Lodge、接駁與導覽的營運截止日。',
   '<strong>6 月與 8 月：</strong>不是完全沒有熊，但 Brooks Falls 的集中程度較不穩定。若日期固定，可比較 Katmai 其他沿海看熊導覽，並向業者問清楚實際落點；沿海行程不等於 Brooks Camp。'])
  body+=section('可照著規劃：Brooks Camp 兩天一夜',[
   '<strong>前一晚：</strong>抵達 King Salmon 住宿，先處理補給及隔日接駁，減少同日跨段延誤。',
   '<strong>第 1 天上午：</strong>搭預約的水上飛機或船抵達，完成熊安全說明、營地報到；中午安頓與用餐。<strong>下午：</strong>依現場通行及平台輪候情況看熊，傍晚回營地或 Lodge。',
   '<strong>第 2 天上午：</strong>再次看熊、收營與整理行李；按已確認的班次離開。下午是否能接上 King Salmon → Anchorage，需由接駁與航空時刻共同決定。想少趕一點可改三天兩夜。',
   '放進九日路線時，可用 Day 6–7 改為 Katmai 過夜，另安排 King Salmon 前一晚或交通緩衝；這會占用原本公路段，不能原封不動保留所有後續景點。'])
  body+=sources([('NPS 營地預訂','https://www.nps.gov/katm/planyourvisit/campingbcdv.htm'),('Brooks Lodge 抽籤','https://katmailand.com/brooks-lodge-lottery/'),('Trading Post 服務','https://katmailand.com/rates-and-services/trading-post/'),('Anchorage 裝備租借','https://www.alaskaoutdoorgearrental.com/camping'),('水上飛機交通','https://katmaiair.com/bear-viewing/flights-to-brooks-lodge-brooks-camp/'),('水上接駁訂位注意','https://katmaiwatertaxi.com/booking-considerations/'),('阿拉斯加魚類與野生動物部：看熊季節','https://www.newsrelease.adfg.alaska.gov/index.cfm?adfg=bearviewing.katmai')])
 else:
  body+=section('從遊客中心再往內走：McCarthy 與 Kennecott',[
   'Copper Center 的公園遊客中心適合公路旅行順訪；若想走上 Root Glacier，目的地應改為 McCarthy／Kennecott。這是更深入園區的另一段旅程，需要另外安排交通、住宿與導覽。',
   '<strong>坐車進去：</strong>經 Chitina 轉入約 59 英里的 McCarthy Road 碎石路。租車前取得車行對這條路的明確許可；抵達 Kennicott River 人行橋附近停車，步行過橋，再確認往 McCarthy／Kennecott 的當地接駁。一般自駕不等於可以直接開到 Kennecott 飯店門口。',
   '<strong>坐小飛機進去：</strong>Wrangell Mountain Air 有 Chitina → McCarthy 的季節性定期航班，約 30 分鐘，通常夏季營運。單買交通機票不代表包含飯店接送、冰川導覽或觀光飛行；也可比較業者整合的飛入一日行程。',
   '空中觀景與交通飛行也不同：想在園區落地散步，訂購時要確認降落地點與停留時間；只買 flightseeing 不一定會到鎮上。'])
  body+=section('Root Glacier：冰川健行，或技術型攀冰',[
   '<strong>冰川健行：</strong>先沿山徑接近冰川，再穿上冰爪，在導遊帶領下看冰面、融水與冰河地形。這不是平坦的短程觀景步道；St. Elias Alpine Guides 的半日路線列為中等難度，接近冰川的步程約 2.5 英里，末段有陡坡與鬆石，需評估體力。',
   '<strong>技術型攀冰：</strong>使用繩索、冰斧、頭盔等裝備攀爬冰壁，是另一種活動；報名前確認體能與年齡條件。單純想體驗踏上冰川，選 guided glacier hike 就好。',
   '<strong>裝備不一定需要自己買。</strong>該業者冰川健行包含冰爪，技術攀冰提供相應技術裝備；但其現行 FAQ 不提供一般旅客單獨租冰爪。不能把過去租借價當成現在人人都能便宜租到整套裝備。鞋子、防雨衣及保暖層仍要看預訂清單準備。',
   'Root Glacier 位於 Wrangell–St. Elias；Denali 飛行行程常看的 Ruth Glacier 是另一座冰川，不能互換名稱。'])
  body+=section('建議住當地：自駕三天兩夜，飛入可縮短',[
   '<strong>第 1 天：</strong>早上從 Copper Center／Chitina 方向出發，為碎石路、拍照與過橋接駁留半天以上；下午抵達 McCarthy 或 Kennecott 入住、確認翌日導覽集合地點。',
   '<strong>第 2 天：</strong>上午參加預訂的 Root Glacier 半日健行，下午依回程時間與體力安排 Kennecott 建築群；磨坊內部導覽需另外確認預訂。晚上再住當地，不趕著長途回 Anchorage。',
   '<strong>第 3 天：</strong>上午離開，下午接公路行程；若要加 Matanuska 冰川健行，另留一整天最從容。九日行程原本只有 Day 8 遊客中心，改成這個版本通常至少多留兩天。',
   '<strong>飛入兩天一夜：</strong>第 1 天飛到 McCarthy、接駁入住及參觀鎮區；第 2 天安排冰川導覽後飛出。必須先讓業者確認導覽結束能銜接航班；若時間不合，改兩晚或購買已配好交通的日遊套裝。住宿 McCarthy／Kennecott 比住 Copper Center 更適合一早集合。'])
  body+='<p><a class="cta" href="../../nearby/matanuska/">延伸：Matanuska 冰川觀景與冰面健行 →</a></p>'
  body+=sources([('NPS：McCarthy Road 與 Kennecott 交通','https://www.nps.gov/wrst/planyourvisit/directions-mccarthy-rd-and-kennecott.htm'),('Chitina–McCarthy 飛行','https://www.wrangellmountainair.com/mccarthy-chitina'),('Root Glacier 半日健行','https://www.steliasguides.com/trips/half-day-glacier-hike/'),('裝備與租借 FAQ','https://www.steliasguides.com/faqs/'),('技術攀冰','https://www.steliasguides.com/trips/ice-climbing/')])
 return body+'<p class="fine">資訊核對：2026 年 10 月。季節班次、預訂辦法與裝備服務請以出發年度公告為準。</p></section>'

def matanuska_body():
 return '''<nav class="breadcrumbs"><a href="../../index.html">國家公園總覽</a>／<a href="../../routes/alaska/">阿拉斯加行程</a>／Matanuska</nav><section class="park-hero"><div><img src="../../assets/spots/matanuska.jpg" alt="Matanuska 冰川與山谷景觀；觀景不等於踏上冰面" width="1200" height="750"><p class="fine">冰川景觀照片；健行路線會依冰況調整。</p></div><div class="hero-copy"><p class="eyebrow">NEARBY EXPLORATIONS / GLACIER WALK</p><h1>Matanuska 冰川<br>遠眺，或真正走上冰面。</h1><p>州立休憩區的短程觀景，與有導遊的冰川健行，是兩種不同安排。這裡不是國家公園。</p></div></section>'''+section('怎麼選：公路順遊，還是一整天冰川體驗？',[
  '<strong>州立休憩區觀景：</strong>Matanuska Glacier State Recreation Site 適合回程停留、走森林步道及看冰川山谷；這裡沒有直接通往冰面的入口。曾在這一帶看過野生 moose，但動物出現不能保證。',
  '<strong>冰面健行：</strong>另訂冰川導覽，從業者指定入口報到，穿戴其提供的防滑裝備後跟團上冰。冰面並非平坦步道，需能在不平地形行走；可先告知長輩體能，請業者建議合適路線。不要把觀景停車點當作導覽集合地點。'])+section('交通選項與裝備',[
  '<strong>自行開車：</strong>向 Matanuska Glacier Adventures 等業者預約，確認集合入口、報到時間、費用包含項目與冰上活動長度。該業者提供含裝備及相關費用的導覽，仍需自己穿合適鞋子及保暖防雨衣物。',
  '<strong>Anchorage 接送一日團：</strong>例如 Greatland Adventures 的夏季行程約 8 小時，通常約 07:30–08:00 開始接送，包含冰川導覽、冰上裝備、午餐與點心水。飯店接送範圍及租屋住址能否接送需先確認。',
  '冰洞、藍冰與融水地形會隨季節及冰況改變，不能把照片中的冰洞視為一定能進入的景點。'])+section('一日時間示例：從 Anchorage 出發',[
  '<strong>07:30–08:00：</strong>按確認通知候車。<strong>上午：</strong>沿 Glenn Highway 前往冰川，完成報到、裝備及安全說明。<strong>中午至下午：</strong>依當日安排健行與用餐。<strong>約 15:30–16:00：</strong>以 8 小時團估算回 Anchorage；實際以業者路況與導覽安排為準。',
  '原九日行程的 Day 8 保留州立休憩區短走即可；想加冰面健行，最清楚的方式是新增一個完整活動日，再把離境日順延。若要直接排在 Copper Center 回程，先確認導覽時段、車程及集合入口，並縮減其他停留或住附近一晚。'])+sources([('州立休憩區與步道','https://dnr.alaska.gov/parks/aspunits/matsu/matsuglsrs.htm'),('自行抵達的冰川導覽','https://www.matanuskaglacieradventures.us/guided-glaciers-tours/'),('Anchorage 接送夏季一日團','https://www.greatlandadventures.com/matanuska-glacier-summer-tour/')])+'<p class="fine">資訊核對：2026 年 10 月。以上為規劃參考，非已確認出團時間。</p>'
