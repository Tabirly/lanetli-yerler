import csv
import re
import io

data = """"Greyfriars Kirkyard (Mackenzie Poltergeist)","Edinburgh","İskoçya","Tarihin en agresif ve fiziksel zarar veren poltergeist vakalarından birine ev sahipliği yapan bu ürkütücü gotik mezarlık. Covenanters Hapishanesi'nin kalıntılarında uyanan 'Kanlı Mackenzie'nin şeytani enerjisi, gece yarısı demir kapıların ardına geçenlerin vücutlarında açıklanamayan yanıklar, tırnak izleri ve ağır baygınlıklar yaratır.",5"Mary King's Close","Edinburgh","İskoçya","Veba salgını sırasında hastalıklı insanların diri diri tuğlalarla örülerek ölüme terk edildiği, yerin metrelerce altındaki bu zifiri karanlık labirent sokaklar. Oksijensiz dehlizlerde ilerlerken, veba kurbanlarının o umutsuz, çürümüş ölüm frekansı ve karanlıkta beliren çocuk silüetleri iradenizi adeta ezip geçer.",5"Glamis Kalesi","Angus","İskoçya","Shakespeare'in Macbeth'ine ilham veren ve 'Gizli Oda' efsanesiyle bilinen, İskoçya'nın en karanlık sırlarını barındıran şatosu. Duvarların ardına diri diri gömülen asilzadelerin çığlıkları ve gece yarısı koridorlarda sürüklenen zincir sesleri; kalenin kadim, vampirik ve aristokratik lanetinin hala kan aradığını gösterir.",5"Culloden Muharebe Alanı","Inverness","İskoçya","1746'da binlerce İskoç klan savaşçısının (Jacobite) bir saatten kısa sürede acımasızca katledildiği, kana doymuş devasa bozkır. Sisli kış sabahlarında ovanın üzerinde yankılanan o kaotik savaş çığlıkları ve dökülen kanın yarattığı devasa, paslı travma frekansı empatları anında dizlerinin üzerine çöktürür.",5"Overtoun Köprüsü (Ölüm Köprüsü)","West Dunbartonshire","İskoçya","1950'lerden beri yüzlerce köpeğin açıklanamaz bir dürtüyle kendilerini 15 metrelik uçurumdan atarak intihar ettiği bu gotik ve gizemli taş köprü. Vadiye hakim olan ve Kelt mitolojisinde 'İnce Yer' (boyutların kesiştiği nokta) olarak bilinen bu alanın yaydığı o hipnotik, yutucu karanlık frekans zihninizi bulandırır.",5"Edinburgh Kalesi (Zindanlar)","Edinburgh","İskoçya","Sönmüş bir volkanın üzerine kurulu olan ve asırlar boyunca cadıların yakıldığı, esirlerin işkenceyle parçalandığı bu devasa askeri kale. Zifiri karanlık zindanlarda kaybolan hayalet gaydacı çocuğun o melankolik müziği ve işkence odalarının taşlarına sinmiş olan o saf acı enerjisi nefes almanızı engeller.",4"Glencoe Vadisi (Katliam Vadisi)","Highlands","İskoçya","1692'de gece yarısı misafirperverlik kurallarının vahşice ihlal edilip MacDonald klanının uykularında doğrandığı o devasa, izole ve sarp dağ geçidi. Vadinin kasvetli, ağır sisinde yankılanan kadın ve çocuk çığlıkları; ihanetin doğaya nasıl kazındığını ve toprağın bu kanı asla affetmediğini kanıtlar.",4"Stirling Kalesi","Stirling","İskoçya","Tarihin en kanlı kuşatmalarına sahne olmuş bu antik kalede dolaşan 'Yeşil Kadın'ın uğursuz silüeti. Efsaneye göre onun belirmesi ölümün ve felaketin habercisidir; kalenin soğuk rüzgarına karışan kılıç şakırtıları ve savaşın o agresif, erkeksi ölüm frekansı ziyaretçileri sürekli tetikte tutar.",4"St Andrews Katedrali Harabeleri","Fife","İskoçya","Kuzey Denizi'nin hırçın dalgalarına bakan, Orta Çağ'ın en büyük ama şu an en yıkık tapınaklarından biri. 'Beyazlı Hanım'ın ve katledilen keşişlerin hayaletlerinin dolaştığı bu devasa harabelerin arasında esen tuzlu rüzgar, arafta kalan dini bir fanatizmin o ağır ve yargılayıcı enerjisini taşır.",4"Borthwick Kalesi","Midlothian","İskoçya","Mary Stuart'ın (İskoç Kraliçesi) sığındığı ve sonrasında kanlı kuşatmalara uğrayan bu devasa ve klostrofobik ikiz kuleli şato. 'Kırmızı Oda'da şeytani ritüeller yapan eski lordun yarattığı o karanlık astral portal ve duvarlardan sızan o sülfürik kötülük frekansı, ziyaretçilere fiziksel bir bulantı verir.",4"""

# Split by fixing the missing newline before a quote after a number
formatted_data = re.sub(r'(\d)"', r'\1\n"', data)

reader = csv.reader(io.StringIO(formatted_data))
with open('perili_mekanlar.csv', 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for row in reader:
        # Avoid empty lines
        if not row:
            continue
        if len(row) == 5:
            row.append('') # resim_url
        writer.writerow(row)

print("İskocya kayitlari eklendi.")
