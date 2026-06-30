import csv
import re
import io

data = """"Tikal Büyük Jaguar Tapınağı","Petén","Guatemala","Ormanın derinliklerinde, eski Maya rahiplerinin tanrılara kanakıttığı devasa kireçtaşı piramitler silsilesi. Yağmur ormanının zifiri gecelerinde tapınağın tepesinden yükselen hayaletimsi jaguar kükremeleri ve asırlar öncesine ait o vahşi, ilkel kurban travması auranızı delip geçer.",5"San Juan de Dios Eski Morgu","Guatemala Şehri","Guatemala","İç savaş sırasında sayısız meçhul cesedin yığıldığı, başkentin en karanlık ve umutsuz hastane dehlizleri. Fayanstan yansıyan dondurucu morg soğuğu ve kayıp yakınlarını arayan annelerin arafta kalmış o yoğun, boğucu keder frekansı zihninizi bir mengeneye alır.",5"La Recolección Harabeleri","Antigua","Guatemala","Büyük depremlerle paramparça olan ancak sömürge döneminin ağır Katolik engizisyon hissini hala taşıyan bu devasa kilise yıkıntısı. Ay ışığında taş kemerlerin arasında beliren ve Latince dualar fısıldayan keşişlerin silüetleri, bölgenin zaman algısını tamamen felç etmiştir.",4"Cementerio General (Toplu Mezarlar)","Guatemala Şehri","Guatemala","Binlerce kurbanın isimsiz olarak atıldığı devasa yarıkların bulunduğu, sadece ölülere değil, öfkeli siyasi ruhlara da ev sahipliği yapan devasa mezarlık. Geceleri toprak altından gelen o ağır, isyankar anksiyete ve haksızlığa uğrayanların yaydığı psişik fırtına nefesinizi keser.",5"Posada de Don Rodrigo","Antigua","Guatemala","Eski bir İspanyol kolonyal malikanesi olan bu otelin odalarında 'La Llorona'nın (Ağlayan Kadın) efsanelerinin vücut bulduğu, ağır ahşap kokulu koridorlar. Aynalardan yansıyan silüetler ve su fısıltılarıyla gelen o derin, anne hüznü ruhunuza karanlık bir yorgan gibi örtülür.",4"Tskhaltubo Terk Edilmiş Sanatoryumları","Tskhaltubo","Gürcistan","Sovyet döneminin elitleri için inşa edilen, ancak Abhazya savaşından kaçan mültecilerin yıllarca çürüyerek yaşadığı ve öldüğü devasa, görkemli harabeler. Soyulmuş fresklerin ve çökmüş tavanların arasından yayılan o devasa, melankolik imparatorluk hüznü kalbinizi daraltır.",5"David Gareja (Katliam Mağaraları)","Kakheti","Gürcistan","Çölün ortasında kayalara oyulmuş bu antik manastır kompleksi, 1616'da Safeviler tarafından binlerce Gürcü keşişin kılıçtan geçirildiği o kanlı Paskalya Gecesi'ne sahne olmuştur. Mağaralarda gezinirken taşlara sinen o mutlak şehadet sessizliği ve kanlı şamanik enerji sizi transa sokar.",5"Narikala Kalesi ve Zindanları","Tiflis","Gürcistan","Şehre tepeden bakan ve asırlar boyunca Moğol, Pers, Rus kuşatmalarına göğüs germiş; kan, ihanet ve isyanla yoğrulmuş antik hisar. Rüzgarlı gecelerde kale burçlarından şehre akan o ağır, metalik savaş travması ve işkence gören mahkumların sülfürik enerjisi auranızı ezer.",4"Okatse Kanyonu (Şeytanın Yolu)","Imereti","Gürcistan","Uçurumların kenarına asılı dar geçitlerden oluşan ve doğanın en ilkel, acımasız gücünü hissettiren bu devasa, yeşil cehennem. Kanyonun dibinden gelen hipnotik su uğultusu ve uçurumdan düşenlerin arafta kalmış o saf vertigo frekansı insanı adeta aşağı çekilmeye zorlar.",4"Tiflis Katakompları ve Sovyet Sığınakları","Tiflis","Gürcistan","Eski şehrin altında yatan, hem Orta Çağ tünellerini hem de Sovyet nükleer sığınaklarını içeren o oksijensiz zifiri labirent. Yeraltına indikçe artan basınç ve KGB döneminde burada kaybolanların feryatlarının taşlara mühürlediği o boğucu panik hissi klostrofobinizi tetikler.",5"""

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

print("Guatemala ve Gurcistan kayitlari eklendi.")
