import csv
import re
import io

data = """"Lokrum Adası (Lanetli Ada)","Dubrovnik","Hırvatistan","Manastırlarından kovulan Benedikten rahiplerinin adayı terk ederken yaktıkları ters mumlarla toprağa kazıdığı o meşhur ölüm laneti. Adaya gece kalmak için gizlice girenlerin hissettiği o devasa, boğucu lanet enerjisi ve ağaçların arasından süzülen cüppeli, yüzsüz silüetler auranızı anında felç eder.",5"Veliki Tabor Kalesi","Desinić","Hırvatistan","Yasak aşkı yüzünden asilzadeler tarafından kalenin kalın taş duvarları arasına canlı canlı örülen Veronika'nın mekanı. Kış gecelerinde kalede yankılanan hıçkırıklar ve taş duvarlardan sızan o ezici, kederli dişil enerji; yüzyıllardır arafta kalan bu intikam frekansını direkt göğsünüze saplar.",5"Kringa Köyü (Avrupa'nın İlk Vampiri)","İstirya","Hırvatistan","Tarih kayıtlarına geçmiş ilk gerçek vampir vakası olan Jure Grando'nun mezarından kalkıp 16 yıl boyunca dehşet saçtığı bu karanlık yerleşke. Köyün ıssız sokaklarında gece yarısı dolaşırken, eski mezarlığın yaydığı o ilkel (primal), kana susamış okült enerji ve görünmez izleyicilerin baskısı nefesinizi keser.",5"Brestovac Sanatoryumu","Zagreb","Hırvatistan","Medvednica dağının sisli yamaçlarında çürümeye terk edilmiş bu eski verem hastanesi. Sevdiği kadın Ljerka'yı kurtarmak için burayı inşa ettiren doktorun çaresizliği ve acı içinde boğularak can veren binlerce hastanın o ağır, hastalıklı ölüm frekansı; yıkık koğuşlarda yankılanan bedensiz öksürüklerle birleşerek iradenizi emer.",4"Dvigrad (Hayalet Şehir)","Kanfanar","Hırvatistan","Veba ve sıtma salgınlarının vurduğu, 18. yüzyılda tamamen terk edilerek ormanın merhametine bırakılan bu Orta Çağ şehri. Yıkık surların ve boş kilisenin arasında dolaşırken, o toplu çaresizliğin ve devasa izolasyonun yarattığı ölümcül sessizlik, zihninize ağır bir yalnızlık frekansı olarak çöker.",4"Villa Auer","Zagreb","Hırvatistan","Şehrin kalbinde, eski bir mezarlığın tam üzerine inşa edilmiş ve inatçı poltergeist (gürültücü ruh) aktivitesiyle bilinen lanetli konak. Kendiliğinden şiddetle çarpılan kapılar, karanlık pencerelerden dışarı bakan gölgeler ve binanın etrafını saran o agresif, alt boyut karanlığı; buranın doğrudan bir astral portal olduğunu fısıldar.",4"Pazin Mağarası (Yeraltı Geçidi)","Pazin","Hırvatistan","Dante'nin Cehennem'ine bile ilham veren, devasa ve dipsiz bir uçuruma dökülen bu karanlık yeraltı nehri labirenti. Yerin derinliklerinden gelen suyun o hipnotik ve yutucu kükremesi, alt boyut (Hades) varlıklarının çağrısına dönüşerek aklınızın sınırlarını zorlar ve klostrofobik bir dehşet yaratır.",5"Jurjevsko Groblje (Aziz George Mezarlığı)","Zagreb","Hırvatistan","Cadı mahkemelerinden kaçanların ve yoksulların gömüldüğü, asırlık ağaçların mezar taşlarını yuttuğu bu gotik ve terk edilmiş ormanlık alan. Gece çöktüğünde heykellerin arasından süzülen 'Beyazlı Kadın' silüeti ve toprağın o melankolik, eski zaman ölüm enerjisi ziyaretçileri transa sokar.",4"Učka Dağı (Cadıların Zirvesi)","Rijeka","Hırvatistan","Slav mitolojisinin karanlık tanrılarına adakların sunulduğu ve asırlar boyunca yerel cadıların (Mora) toplandığı sarp zirve. Sisin içinden yükselen o devasa, ezici pagan enerjisi ve dağın derinliklerinden gelen açıklanamayan uğultular; buranın insan bilincini büken aktif bir manyetik vortex olduğunu gösterir.",4"Valpovo Kalesi (Prandau-Normann)","Valpovo","Hırvatistan","Efsaneye göre başı kesilerek kuyuya atılan ve asırlar sonra bedeni bulunan genç bir kızın ruhuyla lanetlenmiş bu şato. Kış gecelerinde kalenin avlusunda beliren 'Beyaz Leydi'nin o saf hüzün frekansı ve cinayetin havada asılı kalan paslı enerjisi, ziyaretçilerin göğsüne ağır bir keder oturtur.",3"""

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

print("Hırvatistan kayitlari eklendi.")
