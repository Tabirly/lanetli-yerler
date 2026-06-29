import csv

raw_data = """
"Qız Qalası (Kız Kulesi)","Bakü","Azerbaycan","Hakkında sayısız efsane bulunan, sevmediği biriyle (veya bazı efsanelere göre kendi babasıyla) evlendirilmek istendiği için bir prensesin zirvesinden kendini Hazar'ın karanlık sularına bıraktığı bu kadim yapı. Taş duvarlara asırlardır sinen o çaresiz, melankolik dişil enerji ve intiharın o ağır frekansı, kuleye çıkanların göğsünü görünmez bir mengene gibi sıkar.",4
"Qobustan (Gobustan) Şaman Kayalıkları","Bakü","Azerbaycan","On binlerce yıl öncesinin ilkel şamanik ritüellerine ev sahipliği yapmış bu devasa kaya oymaları alanı. Geceleri çamur volkanlarının topraktan çıkardığı o boğuk, nefes alma benzeri sesler ve rüzgarın kayalara çarparak fısıldadığı kadim dualar, buranın hala doğa ruhları (elementaller) tarafından korunan aktif bir astral portal olduğunu kanıtlar.",5
"Atəşgah (Ateş Tapınağı)","Bakü","Azerbaycan","Tarih boyunca Zerdüştlerin ve Hintli çilekeş rahiplerin sönmeyen ateşe taptığı bu mistik merkez. Kendilerini zincirlere vurarak, aç bırakarak ve fiziksel acı çekerek aydınlanmaya çalışan bu fanatik rahiplerin o kaotik, yakıcı ve ağır çile frekansı, tapınağın avlusunda hala görünmez bir duman gibi asılı durmaktadır.",4
"1139 Gəncə Depremi ve Göygöl","Gəncə","Azerbaycan","1139 yılında meydana gelen ve koca bir şehri yutarak yüz binlerce insanı canlı canlı toprağa gömen devasa depremin yarattığı bu doğa harikası göl. Suyun o pürüzsüz ve muazzam güzelliğinin altında, bir gecede yok olan yüz binlerce insanın toplu kederi ve o ani ölüm travmasının yarattığı karanlık bir su enerjisi yatar.",5
"Əlincə Qalası (Alınca Kalesi)","Nahçıvan","Azerbaycan","Sarp bir dağın zirvesinde, Timur'un acımasız ordularına karşı 14 yıl boyunca direnmiş bu kanlı ve izole savaş kalesi. Kayalıklara sinmiş olan saf savaş, açlık ve vahşet enerjisi o kadar ağırdır ki, gece karanlığında zirvede durduğunuzda kılıç seslerini ve yüzlerce yıl önceki o ölümcül kuşatmanın panik frekansını auranızda hissedersiniz.",5
"Səadət Sarayı (Muhtarov Sarayı)","Bakü","Azerbaycan","Büyük bir aşkla inşa edilen ancak Bolşevik işgali sırasında petrol baronu Murtuza Muhtarov'un evini basan askerleri vurup ardından at üstünde kendi beynine kurşun sıktığı bu ihtişamlı saray. Binanın o görkemli salonlarında hala ani, şiddetli bir ölümün ve yıkılan bir imparatorluğun o paslı, kederli frekansı yankılanmaktadır.",4
"Xınalıq (Kınalık) Dağ Köyü","Quba","Azerbaycan","Kafkas dağlarının bulutları delen zirvelerinde, binlerce yıldır medeniyetten tamamen izole yaşamış, dilleri bile farklı olan bu kadim pagan köyü. Geceleri köyü yutan o yoğun, zifiri sisin içinden dağ ruhlarının fısıltıları duyulur; buradaki ezici izolasyon enerjisi, modern dünyanın zaman çizgisinden tamamen koptuğunuzu hissettirir.",4
"Diri Baba Türbesi","Qobustan","Azerbaycan","Doğrudan sarp bir uçurumun içine oyulmuş bu mistik Sufi türbesi. Efsaneye göre burada inzivaya çekilen ve bedeni hiç çürümeyen (Diri) dervişin aurası mekanı tamamen ele geçirmiştir. Merdivenlerden yukarı çıkarken havada hissettiğiniz o ağır, hipnotik trans enerjisi zihninizi sarsarak sizi başka bir boyuta çeker.",4
"Azıx (Azıh) Mağarası","Xocavənd","Azerbaycan","İnsanlık tarihinin en eski yerleşim yerlerinden biri olan, zifiri karanlık dehlizleriyle bu devasa yeraltı labirenti. Yüz binlerce yıllık o en ilkel korkuların (karanlık korkusu, yırtıcı korkusu) ve hayatta kalma güdüsünün yarattığı o primal (ilksel) enerji, mağaranın derinliklerine adım attığınız anda kalp atışlarınızı hızlandırır.",5
"Bibiheybat Terk Edilmiş Petrol Kuyuları","Bakü","Azerbaycan","Kıyamet sonrası (post-apokaliptik) bir filmi andıran, çürüyen devasa demir pompaların ve siyah petrol birikintilerinin olduğu bu ıssız arazi. Sanayi devrimi sırasında burada acımasız şartlarda çalışırken çıkan yangınlarda kül olan işçilerin o sanayi tipi, toksik kederi ve toprağın kanının emilmesinden doğan o ağır, öfkeli enerji auranızı boğar.",3
"""

import io
reader = csv.reader(io.StringIO(raw_data.strip()))

with open('perili_mekanlar.csv', 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for row in reader:
        if row:
            # Append empty string for resim_url
            row.append("")
            writer.writerow(row)
print("Azerbaycan verileri başarıyla eklendi.")
