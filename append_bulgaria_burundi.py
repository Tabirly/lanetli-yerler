import csv
import re
import io

data = """"Buzludzha Anıtı (Terk Edilmiş UFO Komünizm Binası)","Kazanlak","Bulgaristan","Balkan dağlarının dondurucu zirvesine kondurulmuş, terk edilmiş ve UFO'ya benzeyen bu devasa Sovyet anıtı. Çürüyen devasa salonun içinde uluyan rüzgar, arafta kalmış eski rejimin megalomanik ama ölü enerjisini taşır; bu gri beton canavarın içinde durduğunuzda zaman algınız tamamen donar.",5"Şeytanın Boğazı Mağarası (Dyavolsko Garlo)","Rodop Dağları","Bulgaristan","Mitolojiye göre Orpheus'un yeraltı dünyasına, Hades'e indiği o dipsiz ve devasa mağara. Mağaranın içine dökülen dev şelalenin yarattığı o sağır edici karanlık ve asla geri yüzeye çıkmayan nesnelerin efsanesi; insan zihnini doğrudan yeraltının o ezici, hipnotik karanlığına çeker.",5"Tsarichina Kazı Alanı (Lanetli Çukur)","Sofya","Bulgaristan","1990'larda Bulgar ordusunun 'dünya dışı varlıklar ve kadim bir varlık' bulmak için gizlice kazdığı ancak toplu psişik krizler yüzünden alelacele betonla mühürlediği bu kara nokta. Bölgenin toprağından yayılan o devasa, zihin büken manyetik radyasyon ve duyulduğu iddia edilen telepatik çığlıklar auranızı felç eder.",5"Baba Vida Kalesi","Vidin","Bulgaristan","Tuna Nehri'nin kıyısında, Orta Çağ zindanlarında sayısız işkencenin yaşandığı ve idam edilen esirlerin feryatlarını barındıran bu soğuk taş kale. Suyun rutubetiyle karışan o paslı kan kokusu ve karanlık dehlizlerde beliren 'Beyazlı Kadın'ın kederli silüeti, burayı aktif bir acı portalına çevirir.",4"Asen Kalesi Harabeleri","Asenovgrad","Bulgaristan","Sarp kayalıkların üzerine inşa edilen ve Haçlı seferlerinden bu yana kanlı kuşatmalara sahne olan bu devasa uçurum kalesi. Geceleri rüzgarın yıkık kilise çanlarında çıkardığı o uğursuz çınlama ve savaşlarda uçurumdan atılan askerlerin o ani düşüş paniği, ziyaretçilerin göğsüne ağır bir ağırlık oturtur.",4"Kibira Ulusal Parkı (Ölüm Ormanı)","Cibitoke","Burundi","Ruanda-Burundi iç savaşları sırasında binlerce insanın vahşice katledildiği, ormanın derinliklerine gömüldüğü bu devasa, geçit vermez yeşil cehennem. Ormanın zifiri karanlığında gezinirken ağaçların arasından sızan o saf şiddet ve kan kokulu katliam frekansı empatları nefessiz bırakır.",5"Rusizi Nehri Timsah Kıyıları (Gustave'in Suları)","Bujumbura","Burundi","Yüzlerce insanı yediği iddia edilen devasa efsanevi timsah 'Gustave' ve savaş döneminde nehre atılan sayısız cesedin yarattığı lanetli akıntılar. Suyun o karanlık ve pürüzsüz yüzeyine bakarken derinlerden yükselen boğulma iniltileri ve ilkel, yırtıcı su elementallerinin fısıltısı zihninizi daraltır.",5"Terk Edilmiş Belçika Koloni Harabeleri","Bujumbura Kırsalı","Burundi","Ormanın yavaş yavaş geri aldığı, sömürge döneminin o acımasız ve kanlı kırbaç izlerini taşıyan yıkık malikaneler. İşkenceyle çalıştırılan yerlilerin arafta kalmış o yoğun, kederli sömürü frekansı ve boş pencerelerden size bakan meçhul gölgeler; burayı yutucu bir siyah girdaba çevirmiştir.",4"Gishora Davul Barınağı (Kanlı Ayin Alanı)","Gitega","Burundi","Eskiden kralların ve savaşçıların gücünü göstermek için düşman kanıyla yıkandığı iddia edilen, kadim davulların ritimlerine ev sahipliği yapan bu alan. Gece rüzgarına karışan ve insanın kalp atışını kontrol eden o hayalet davul sesleri, saf Afrika mistisizminin en karanlık, zihin büken halini yansıtır.",4"Ruvubu Bataklıkları (Kayıp Ruhlar Bölgesi)","Ruyigi","Burundi","Ülkenin en büyük ve en izole nehir deltası; hem kaçak avcıların hem de isyancıların cesetlerini yutan o devasa ve sessiz çamur kapanı. Sisli sabahlarda bataklığın üzerinden yükselen fosforik ışıklar ve balçığa çekilen ruhların feryatları, bu doğa harikasını ölümcül bir astral tuzağa dönüştürür.",4"""

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

print("Bulgaristan ve Burundi kayitlari eklendi.")
