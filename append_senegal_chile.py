import csv
import re
import io

data = """"Gorée Adası (Köle Evi / Maison des Esclaves)","Dakar","Senegal","Yüzyıllar boyunca milyonlarca Afrikalının zincirlenerek tutulduğu ve okyanusa açılan 'Dönüşü Olmayan Kapı'dan geçirildiği o tarihi işkence merkezi. Kilitli, penceresiz dar zindanların zeminine sinmiş olan o devasa kitlesel kölelik hüznü ve koparılan ailelerin duvarlarda yankılanan feryadı auranızı ezer.",5"Fadiouth Adası (Kemik ve Kabuk Adası)","Fadiouth","Senegal","Tamamı milyonlarca deniz kabuğundan oluşan ve asırlardır hem Müslümanların hem de Hristiyanların yan yana gömüldüğü bu tuhaf, beyaz nekropol ada. Ay ışığında kabukların üzerinde yürürken çıkan o kırılma sesleri ve adanın yaydığı o yoğun, ezoterik Afrika atalar kültü frekansı insanı transa sokar.",4"Terk Edilmiş Rufisque İstasyonu","Dakar","Senegal","Fransız sömürge döneminin en işlek ancak günümüzde tamamen paslanmış ve çürümeye terk edilmiş olan o eski sömürge tren istasyonu. Gece rüzgarının paslı raylarda çıkardığı mekanik ıslıklar ve sömürgecilerin hastalık yüzünden kırıldığı o ağır, melankolik sıtma frekansı nefesinizi keser.",4"Niokolo-Koba Ormanları (Ruhlar Bölgesi)","Tambacounda","Senegal","Balta girmez ormanların derinliklerinde yer alan, yerel halkın cinler ve kadim orman ruhları tarafından korunduğuna inandığı geniş ve tehlikeli savana. Güneş battığında ormanın derinliklerinden gelen o ilkel, açıklanamayan fısıltılar ve ağaç köklerine mühürlenmiş o vahşi, şamanik titreşim zihninizi daraltır.",4"Dakar Katedrali Yeraltı Dehlizleri","Dakar","Senegal","Görkemli katedralin altında, sömürge dönemi boyunca sarı hummadan ölen sayısız Katolik rahip ve misyonerin gömüldüğü o rutubetli yeraltı mahzenleri. Oksijensiz dehlizlerde gezinirken eski haçların yaydığı o ağır, dini melankoli ve Afrika'nın acımasız sıcağında eriyenlerin kederi kalbinizi sıkar.",4"Humberstone Hayalet Kasabası","Atacama Çölü","Şili","Dünyanın en kurak çölünün ortasında, İngiliz maden patronlarının köle gibi çalıştırdığı binlerce işçinin kavrularak öldüğü ve aniden terk edilen devasa sanayi şehri. Paslı makinelerin arasında esen dondurucu gece rüzgarı ve açık mezarlardan yükselen o saf, sülfürik sömürü ve çaresizlik anksiyetesi sizi felç eder.",5"Dawson Adası Zindanları","Tierra del Fuego","Şili","Pinochet diktatörlüğü sırasında, Antarktika'ya yakın bu donmuş ve izole adada kurulan acımasız siyasi toplama kampı. Dondurucu fırtınalara karışan işkence çığlıkları ve kutup soğuğunda tel örgülere asılarak can veren muhaliflerin o mutlak, yalıtılmış ölüm kederi ruhunuzu dondurur.",5"Estadio Nacional (Ulusal Stadyum)","Santiago","Şili","1973 darbesinde binlerce insanın tutuklandığı, sorgulandığı ve koridorlarında kurşuna dizildiği o devasa, kanlı spor kompleksi. Boş tribünlere baktığınızda o çimlerin altına kazınmış olan ezici devlet terörü, elektroşok odalarından sızan o ölümcül travma ve kayıpların feryadı auranızı paramparça eder.",5"Chiloé Adası (Caleuche Hayalet Gemisi)","Chiloé","Şili","Karanlık denizcilik efsanelerinin, kara büyücülerin (brujos) ve deniz kurbanlarının ruhlarını taşıyan 'Caleuche' adlı devasa hayalet geminin görüldüğü o sisli takımadalar. Okyanusun zifiri gecelerinde suların altından gelen o ritmik, şeytani müzik sesleri ve boğulmuş denizcilerin yaydığı soğuk manyetizma zihninizi yutar.",4"Palacio Cousiño (Hayaletli Malikane)","Santiago","Şili","19. yüzyılda gümüş ve kömür baronları tarafından inşa edilen ancak arka arkaya gelen trajik intiharlar ve çocuk ölümleriyle lanetlenen o lüks, gotik saray. Kadife kaplı karanlık odalarda havaya asılı kalan o ağır, aristokratik melankoli ve devasa aynalardan sizi izleyen o buz gibi gölgeler nefesinizi keser.",4"""

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

print("Senegal ve Sili kayitlari eklendi.")
