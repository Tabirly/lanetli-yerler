import csv
import re
import io

data = """"El Helicoide","Karakas","Venezuela","Dünyanın en büyük helezonik yapılarından biri olarak alışveriş merkezi için tasarlanan ancak sonradan istihbarat ve işkence merkezine dönüşen devasa beton zindan. Yeraltı hücrelerinde ışık görmeden hapsedilen siyasi mahkumların acı dolu feryatları ve betonun içine işleyen o boğucu, kaotik delilik frekansı burayı modern bir cehenneme çevirmiştir.",5"San Carlos de la Barra Kalesi","Maracaibo","Venezuela","Korsan saldırılarından korunmak için inşa edilen ve asırlar boyunca kanlı kuşatmalara, vahşi işkencelere sahne olan bu sarp askeri kale. Zindanların karanlık sularla dolduğu dehlizlerde gezinirken, zincire vurulup boğulan mahkumların o paslı, nefes kesen intikam enerjisi auranızı sarsar.",5"Museo Sacro (Gizli Mezarlık)","Karakas","Venezuela","Eski bir kilise ve veba mezarlığının üzerine inşa edilmiş, ölümün ve dinin iç içe geçtiği bu gotik ve ürkütücü müze. Yeraltı mezarlarının (katakomp) bulunduğu alt katlardan süzülen o ağır, nekromantik enerji ve karanlıkta fısıldayan görünmez rahiplerin silüetleri insanı derin bir paniğe sokar.",5"Casa de los Celis","Valencia","Venezuela","Bağımsızlık savaşı sırasında hastane olarak kullanılan ve savaşın en kanlı ampütasyonlarına, ölümlerine sahne olan bu eski kolonyal malikane. Gece yarısı odalarında yankılanan asker iniltileri ve binanın ahşap zeminine kazınmış o saf, travmatik savaş frekansı ziyaretçilere fiziksel bir ağırlık çökertir.",4"Hospital Vargas (Terk Edilmiş Koğuşlar)","Karakas","Venezuela","Başkentin en eski hastanelerinden birinin yıllardır kapalı ve çürümeye terk edilmiş olan psikiyatri ve morg bölümleri. Karanlık, fayanslı koridorlarda yankılanan meçhul adımlar ve o ağır, sülfürik ölüm/hastalık enerjisi, buranın astral alt boyut varlıkları için bir yuva olduğunu fısıldar.",4"Castillo de San Carlos Borromeo","Pampatar (Margarita Adası)","Venezuela","Karayip korsanlarının defalarca yağmalayıp kılıçtan geçirdiği ve adanın o masmavi sularına kan karıştıran tarihi sahil kalesi. Kaledeki dar ve havasız 'Hüzün Odası'nda durduğunuzda, esirlerin o çaresiz yalnızlık frekansı ve kanlı korsan saldırılarının arafta kalmış kaosu ruhunuzu daraltır.",4"Cuartel San Carlos (San Carlos Kışlası)","Karakas","Venezuela","Onlarca yıl siyasi isyancıların hapsedilip acımasızca sorgulandığı, isyanların kanla bastırıldığı devasa askeri hapishane. Boş hücrelerin arasında gezerken ensenizde hissettiğiniz soğuk baskı ve haksızlığa uğrayanların duvarlara sinmiş o ilkel öfkesi; burayı aktif bir negatif enerji girdabına dönüştürür.",4"Cerro El Ávila (Kayıp Ruhlar Dağı)","Karakas","Venezuela","Şehre tepeden bakan ve sisli ormanlarında sayısız insanın kaybolduğu, doğaüstü olayların ve UFO gözlemlerinin merkezi olan devasa dağ. Ormanın derinliklerine girdiğinizde aniden yön duygunuzu kaybettiren o yoğun manyetik anomali ve ağaçların arasından izleyen 'Gözcüler'in fısıltıları zihninizi ezer.",5"Hacienda La Trinidad Harabeleri","Karakas","Venezuela","Geçmişte kölelerin zorla çalıştırıldığı ve şiddet gördüğü, doğanın yavaş yavaş geri aldığı bu sömürge dönemi çiftlik kalıntıları. Gece rüzgarıyla kırbaç seslerini andıran uğultuların yankılandığı bu alanda, toprağa kanla yazılmış olan o devasa, kederli sömürü frekansı her nefeste göğsünüzü sıkar.",4"Hotel Cervantes","Karakas","Venezuela","1930'ların ihtişamlı günlerinden geriye sadece açıklanamayan cinayetlerin ve intiharların kaldığı, bazı katları gizlice mühürlenmiş bu eski otel. Asansörlerin kendiliğinden açıldığı, boş aynalarda silüetlerin belirdiği bu yapının içine hapsolmuş o zaman dışı, melankolik karanlık zihninizi yavaş yavaş zehirler.",4"""

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

print("Venezuela kayitlari eklendi.")
