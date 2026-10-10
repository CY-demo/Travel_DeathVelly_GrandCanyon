"""Anonymized first-hand connections; no personal calendar dates."""
from extensions import section

def render_rides(slug):
 titles={'katmai':'Katmai：兩次出發，才成功到 Brooks Camp','kenai-fjords':'Seward：火車下車後怎麼接船','denali':'Denali：車站、飯店、飛行與巴士怎麼接'}
 if slug not in titles:return ''
 s='<section id="our-connections"><div class="section-title"><p class="eyebrow">OUR JOURNEY / CONNECTION DETAILS</p><h2>'+titles[slug]+'</h2><p>從報到、轉乘到回程，這些是我們這趟旅行的搭乘經驗。班次與接駁會依季節和訂位而變動。</p></div>'
 if slug=='katmai':
  s+=section('第一次：Katmai Air 原訂的四段航空交通',[
   '原安排為飯店接駁到機場，再依序搭乘 Anchorage → King Salmon → Brooks Camp。報到地點、飯店接送時間及行李限制依確認通知；不要把小飛機基地當成 Anchorage 主航廈。',
   '<strong>08:00：</strong>Anchorage → King Salmon。<br><strong>10:00：</strong>King Salmon → Brooks Camp。<br><strong>16:30：</strong>Brooks Camp → King Salmon。<br><strong>17:30：</strong>King Salmon → Anchorage。',
   '以上四個時間都是當時原訂的各段出發時間，不是抵達時間，也不是現在可直接照訂的班表。King Salmon 與 Brooks Camp 之間的轉乘需由業者協調；實際落地與園內可用時間要扣掉轉乘、報到及安全說明。'])
  s+=section('實際發生：起飛後折返，當天下午改走 Anchorage',[
   '飛機確實起飛，但 King Salmon／航線低能見度與天氣狀況使這次航程原機返回 Anchorage，因此第一次沒有到 Brooks Camp。業者當時可退款，但後續幾天幾乎沒有空位；退款不等於隔天一定能補飛。',
   '回城後把彈性活動移到下午：Alaska Public Lands Information Center、NPS 資訊與蓋章，以及 Ship Creek／William Jack Hernandez Hatchery 一帶看鮭魚。市區行程讓等待新航班的一天仍有事情可做。',
   '同時聯絡其他 air taxi 詢問空位，最後找到隔天可出發的另一家業者。這次臨時換公司的成功經驗，不代表天氣不好時換一家就一定能飛；每家仍要自行判斷航線與天候。'])
  s+=section('第二次：隔天換業者，成功進 Brooks Camp',[
   '隔天早上搭另一家小飛機成功進入 Brooks Camp。這段沒有足夠資料確認業者名稱、精確起飛時間及是否經 King Salmon，因此不把前一天 Katmai Air 的轉乘時間套用到第二天。',
   '<strong>落地 → Bear School → 存放食物與有氣味用品 → Lower River → 詢問 ranger 當日熊況 → Brooks Falls Trail → Riffles → Brooks Falls Platform → 回程再看 Lower River。</strong>',
   '先快速看 Lower River，向 ranger 問「今天熊主要在哪裡？」再走往瀑布方向。若其他區域已看到熊，就把時間留給當下的觀察，不執著在瀑布平台排很久。步道通行及平台使用仍依現場指示。',
   '當天選擇不吃 buffet，自備簡單食物，把時間留給看熊。食物需按規定寄存，只在指定可用餐區域吃，不能一路邊走邊吃。',
   '這次保守估計看見約五隻不同的熊，包括母熊與幼熊、河裡覓食及吃鮭魚的熊；Lower River 與瀑布附近都有觀察機會。沒有看到期待中很多熊同時在瀑布抓魚的畫面，因此下次會優先考慮七月中旬。熊的數量與位置不是行程保證。'])
  s+=section('回程與租車：實際做了什麼，照排前要留意什麼',[
   '<strong>約 17:00 多：</strong>回到 Anchorage，接著到機場租車，再往 Copper Center 移動，當晚住當地。租車櫃檯取車與小飛機降落地點之間還需另算交通及辦理手續時間；這次沒有留下精確接駁與抵達飯店時間。',
   '這是我們實際走過、但很緊湊的一段，不適合當作每天都能照做的保證。看熊返程若延誤，應調整公路段或留 Anchorage 休息；若希望玩得從容，可以另留一天給公路移動。',
   '最有用的準備是保留一至兩個可移動日、先存幾家業者聯絡方式，並確認租車與住宿的變更／取消條件。不要等天氣取消後才發現後面所有安排都不能動。'])
 elif slug=='kenai-fjords':
  s+=section('去程：Coastal Classic → 船公司接駁 → 中午遊船',[
   '<strong>06:45：</strong>從 Anchorage 搭 Coastal Classic。<strong>11:20：</strong>抵達 Seward，下車後直接找船公司接駁車；不要先離開車站自行逛街。<strong>約 11:35：</strong>到小船碼頭櫃檯 check-in。<strong>12:00：</strong>5.5 小時 Kenai Fjords 遊船出發。',
   '這次透過 Alaska Railroad 搭配 day trip，讓火車、遊船與接駁接在一起。船公司與接駁車識別、集合位置、登船截止時間，仍要在預訂時確認。',
   '完成必要報到後，曾利用空檔快訪附近的 Kenai Fjords 遊客中心，來回約十分鐘，非常趕；回港時已無法再安排同樣的參觀。先問清登船期限，有足夠空檔才去，不能把十分鐘當成每個人都能做到的保證。'])
  s+=section('回程與搭乘心得',[
   '遊船約 17:30 回港，接著盡快搭安排好的接駁回 Seward 車站；當時規劃最晚約 17:50 開始移動，銜接 <strong>18:00</strong> 回 Anchorage 的列車，<strong>22:15</strong> 抵達。這個銜接很緊，請讓套裝業者確認安排，不把火車會等候當成保證。',
   'Anchorage ↔ Seward 與 Anchorage ↔ Denali 的景觀鐵路本身就很值得，個人推薦 GoldStar 觀景車廂。領票時可以詢問景觀側座位，但座位需求不一定能滿足。餐飲與行李服務要依實際票種確認。'])
 else:
  s+=section('北上當天：Denali Star → 飯店接駁 → Fly Denali',[
   '<strong>當時約 07:45</strong> 到 Anchorage 車站報到，<strong>08:20</strong> 搭 Denali Star 北上，<strong>15:40</strong> 抵達 Denali。給後續旅客的建議仍是依鐵路報到規定提早到場，不把這次較短的報到空檔當標準。',
   '<strong>約 15:55：</strong>搭 飯店專屬接駁車往 Denali 園區入口飯店，<strong>約 16:15：</strong>入住。這是我們當時的住宿與接駁組合，不代表任何火車票都包含這間飯店接送。',
   '<strong>約 17:30：</strong>Fly Denali 業者派車從飯店接往 Healy，接近傍晚六點的冰川飛行／著陸體驗；記得帶太陽眼鏡。<strong>約 20:00：</strong>接駁回飯店後吃晚餐。這次體驗很推薦；Ruth Glacier 與 Wrangell–St. Elias 的 Root Glacier 是不同地點。'])
  s+=section('園區日：飯店接 Tundra 團，下午再用公園接駁',[
   '我們拿到的是 <strong>06:00</strong> 從 Denali 園區入口飯店 接送的 Tundra Wilderness Tour。這只是當次時刻；營運季每天有團，要提前報名，實際出發時間於出發前 48 小時公布／確認。規劃時仍預留約 5–5.5 小時及接送餘裕。',
   '午間回遊客中心用餐，下午從 Denali Visitor Center 的 Sled Dog Shuttle 站排隊，接 <strong>14:00</strong> 雪橇犬示範；看完後再按當天 Savage River 接駁班次決定是否走河谷步道。若 Tundra 團較晚出發，就要刪減下午安排。',
   '當晚另加了七點多的 Cabin Nite 晚餐劇場，覺得很有趣。要同時安排河谷步道與晚餐秀，先核對末班接駁及劇場報到時間，不要只看活動開始時刻。'])
  s+=section('南下回程：退房、行李與火車分開處理',[
   '<strong>約 09:30：</strong>退房，請飯店協助安排寄放／送往火車站的行李，並明確確認服務。<strong>約 10:00：</strong>往遊客中心活動。<strong>當時約 12:00：</strong>回 Denali 車站報到；<strong>12:30</strong> 搭南下列車，<strong>20:00</strong> 回 Anchorage。',
   'Alaska Railroad 一起訂的住宿與交通套裝，應在訂購時確認 Anchorage 清晨飯店接送、Denali 車站接送、行李運送及公園入口接駁。飯店通常有接駁，不代表每一段都隨到隨搭，也不代表行李會自動跟人送到下一站。'])
 return s+'</section>'
