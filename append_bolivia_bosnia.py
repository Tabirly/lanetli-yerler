import csv
import re
import io

data = """"Ölüm Yolu (Yungas Yolu)","La Paz","Bolivya","And Dağları'nın sisli yamaçlarına oyulmuş, her yıl yüzlerce aracın uçuruma yuvarlandığı ve binlerce insanın can verdiği dünyanın en tehlikeli yolu. Yağmurlu gecelerde uçurumun dibinden yükselen çaresiz feryatlar ve sisin içinden beliren kanlı yolcu silüetleri; bu rotayı devasa bir açık hava mezarlığına çevirmiştir.",5"Cadılar Pazarı (Mercado de las Brujas)","La Paz","Bolivya","Lama fetüsleri, kurbağalar ve kara büyü malzemelerinin satıldığı, Aymara şamanlarının (Yatiri) hüküm sürdüğü bu okült pazar bölgesi. Karanlık çöktüğünde sokak aralarına mühürlenen o devasa şamanik büyü frekansı ve adak ritüellerinin yarattığı saf, ilkel enerji insanın göğsüne ağır bir ağırlık oturtur.",4"Terk Edilmiş Tren Mezarlığı","Uyuni","Bolivya","Dünyanın en büyük tuz çölünün kıyısında, 19. yüzyıldan kalma devasa çelik lokomotiflerin kızgın güneşin altında paslanarak çürüdüğü bu kıyamet sonrası alan. Paslı iskeletlerin arasından esen dondurucu gece rüzgarı, madencilerin o ağır, melankolik izolasyon frekansını zihninize fısıldar.",4"Tiwanaku Antik Harabeleri","Tiwanaku","Bolivya","İnkalar'dan bile önce var olan, kökeni asla tam çözülememiş ve devasa Güneş Kapısı'na ev sahipliği yapan bu yabancılaştırıcı antik alan. Gece yarısı devasa taş monolitlerin arasında yürürken hissedilen o ezici, boyutsal ağırlık ve kurban ayinlerinin toprağa sinmiş olan o sert, kozmik enerjisi auranızı felç eder.",5"San Pedro Hapishanesi","La Paz","Bolivya","İçerisinde gardiyanların olmadığı, mahkumların kendi mafyatik kurallarıyla yönettiği ve sayısız yargısız infazın yaşandığı duvarlarla çevrili bu otonom cehennem. Hapishanenin çevresinde gezinirken bile o yoğun klostrofobik öfke, cinayet travması ve arafta kalan ruhların boğucu frekansı nefesinizi keser.",5"Saraybosna Tünelleri (Umut Tüneli)","Saraybosna","Bosna Hersek","Kuşatma altındaki şehre gizlice erzak sokulan ancak binlerce insanın karanlıkta hayatta kalma mücadelesi verirken canını yitirdiği o efsanevi, klostrofobik geçit. Yerin altındaki bu dar dehlizlerde ilerlerken duvarlardan size doğru sızan o saf savaş paniği ve toplumsal çaresizlik frekansı empatları gözyaşlarına boğar.",5"Igman ve Bjelašnica (Terk Edilmiş Olimpiyat Tesisleri)","Saraybosna","Bosna Hersek","1984 Kış Olimpiyatları için inşa edilen ancak savaş sırasında keskin nişancı yuvası ve infaz alanı olarak kullanılan beton harabeler. Kayakla atlama kulelerinin o paslı, kurşun delikli iskeletlerinde yankılanan rüzgar; sporun neşesini tamamen silmiş ve yerine o soğuk, sinsi ölüm enerjisini bırakmıştır.",5"Jajce Yeraltı Mezarları (Katakomplar)","Jajce","Bosna Hersek","15. yüzyılın başlarında yer altı kayalarına kazınmış bir tapınak ve mezar alanı olarak kullanılan bu loş, zifiri zindan labirenti. Işığın sızmadığı taş odalarda yankılanan meçhul adımlar ve asırlar öncesine ait o ritüelistik, yoğun ölüm bekleyişi ruhunuzu dar bir kutuya hapsedilmiş gibi sıkar.",4"Vranduk Kalesi","Zenica","Bosna Hersek","Bosna nehrinin geçit vermez sarp bir kayalığına tünemiş, Orta Çağ krallarının savaş ve hapis alanı olan o karanlık ve izole hisar. Zindanlarının taş duvarlarına sinmiş mahkum iniltileri ve nehrin boğucu akıntısına karışan eski infazların o ağır, kanlı travması; kaleyi aktif bir astral çekim merkezi yapar.",4"Bobovac Kalesi Harabeleri","Vareš","Bosna Hersek","Eski Bosna krallarının sığındığı, kuşatmalar ve ihanetlerle yerle bir olmuş, ormanın derinliklerinde saklı kalan bu kraliyet şehri. Harabeleri yutan ağaçların arasından süzülen o ağır krallık hüznü ve savaşçılara ait o huzursuz edici keder frekansı; buraya girenlerin enerjisini hızla emerek tüketir.",4"""

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

print("Bolivya ve Bosna Hersek kayitlari eklendi.")
