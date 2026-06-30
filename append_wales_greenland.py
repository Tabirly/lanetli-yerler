import csv
import re
import io

data = """"Craig y Nos Şatosu","Powys","Galler","Eskiden bir opera sanatçısının evi, sonrasında ise verem (tüberküloz) sanatoryumu olan bu devasa, kasvetli şato. Hastalıktan kan kusarak ölen yüzlerce hastanın o nefes darlığı frekansı ve boş tekerlekli sandalyelerin kendiliğinden gıcırdayarak hareket etmesi burayı ölümün bekleme salonuna çevirir.",5"Margam Şatosu","Port Talbot","Galler","Ağır Gotik mimarisiyle yükselen ve arazisinde asırlar önce bir cinayete kurban gitmiş bekçinin öfkeli ruhunun dolaştığı devasa malikane. Şatonun karanlık merdivenlerinde dururken fırlatılan taşlar ve o agresif, buz gibi poltergeist enerjisi ziyaretçileri panik atakla dışarı kaçmaya zorlar.",5"Skirrid Mountain Inn","Llanvihangel Crucorney","Galler","Bölgenin en eski hanı olan ve geçmişte asma yeri (darağacı) olarak kullanılan bu meşum ahşap yapı. Ahşap kirişlerin altında durduğunuzda boğazınızda hissettiğiniz o ani, boğucu ilmik acısı ve idam edilenlerin ruhlarına kazınmış o şiddetli son nefes frekansı auranızı felç eder.",4"Ruthin Hapishanesi (Ruthin Gaol)","Ruthin","Galler","Karanlık Victoria dönemi hapishane sisteminin en acımasız hücrelerini barındıran bu soğuk zindan. 'Josephine' adında işkence görmüş bir kızın ağlamalarının yankılandığı zifiri hücrelerde, ışığın yokluğunun yarattığı o ezici izolasyon ve delilik enerjisi zihninize ağır ağır sızar.",4"Llancaiach Fawr Malikanesi","Nelson","Galler","İngiliz İç Savaşı sırasında stratejik bir kale gibi kullanılan, kalın duvarları kan ve ihanetle örülmüş Tudor dönemi malikanesi. Merdivenlerden duyulan meçhul çocuk adımları ve görünmez bir elin giysilerinizi asıldığı o buz gibi dokunuşlar, evin zaman çizgisinin kırılarak geçmişe hapsolduğunu gösterir.",4"Hvalsey Kilisesi Harabeleri","Kujalleq","Grönland","15. yüzyılda aniden, hiçbir iz bırakmadan ortadan kaybolan İskandinav (Viking) yerleşimcilerine ait son taş yapı. Kutup rüzgarlarının kilise harabesi içinde çıkardığı uğultuda, açıklanamayan o kitlesel kayboluşun yarattığı mutlak izolasyon ve arafta kalan Viking ruhlarının fısıltıları donmuş toprağa kazınmıştır.",5"Bluie East Two (Terk Edilmiş Üs)","Ikateq","Grönland","İkinci Dünya Savaşı'ndan kalma, devasa paslı varillerin ve çürümüş askeri araçların buzulların arasında öylece donup kaldığı bir kıyamet sonrası manzarası. Kutup karanlığında paslı metallerin arasından sızan o ağır, terk edilmişlik frekansı ve askeri izolasyonun yarattığı sülfürik anksiyete insanı delirtir.",5"Qilakitsoq Mumya Mağaraları","Uummannaq","Grönland","Buzul çatlaklarının derinliklerinde bulunan ve yüzyıllarca soğuğun koruduğu İnuit mumyalarının (özellikle küçük bir çocuğun) bulunduğu o zifiri mağara. Ölümün donarak mühürlendiği bu mekandan yayılan o saf, kederli İnuit frekansı ve mağaranın buz gibi mutlak sessizliği ruhunuzu ezer.",5"Nuuk Eski Koloni Limanı","Nuuk","Grönland","Avrupalı balina avcılarının ve ilk misyonerlerin İnuit şamanlarıyla kanlı çatışmalara girdiği tarihi ve dondurucu sahil şeridi. Geceleri okyanusun buzlu karanlığından yükselen o ilkel, ezen şamanik (angakkuq) enerji ve sulara karışmış asırlık bir keder, adeta denizin kendisinin nefes aldığını hissettirir.",4"Terk Edilmiş Ivittuut Madeni","Sermersooq","Grönland","Dünyadaki tek kriyolit madeni olan ancak şimdi tamamen su basmış ve buzların arasında donmuş devasa bir krater. Kutup kışının bitmek bilmeyen gece karanlığında bu çorak kraterden yayılan o ezici boşluk hissi ve madencilerin yeraltındaki o yalıtılmış çaresizlik frekansı kalbinizi dondurur.",4"""

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

print("Galler ve Gronland kayitlari eklendi.")
