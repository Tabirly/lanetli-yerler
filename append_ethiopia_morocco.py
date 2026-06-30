import csv
import re
import io

data = """"Fasil Ghebbi Zindanları","Gondar","Etiyopya","Afrika'nın Camelot'u olarak bilinen eski kraliyet şehrinin asırlık, karanlık zindanları. Kralların esirlerini açlıktan ölüme terk ettiği bu taş dehlizlerde gezinirken ensenize çarpan o rutubetli çürümüşlük rüzgarı ve arafta kalmış eski saray muhafızlarının fısıltıları ruhunuzu ezer.",4"Danakil Çöküntüsü (Ateş ve Cin Vadisi)","Afar","Etiyopya","Dünyanın en sıcak ve yaşanılmaz yeri olan, kükürt gölleri ve asit gayzerleriyle kaplı bu zehirli, cehennemi çöl arazisi. Yeraltından fokurdayan sülfürün yaydığı o devasa, zihin büken elementer manyetizma; burayı ateş cinlerinin ve ifritlerin mutlak krallığına çevirmiştir.",5"Harar Jugol Eski Şehir Surları","Harar","Etiyopya","Bin yıllık tarihiyle Afrika'nın en eski İslami merkezlerinden biri olan bu sur içi labirenti. Geceleri dar ve klostrofobik sokaklarda sırtlanların özgürce dolaştığı bu bölgede, karanlık çöktüğünde havaya asılı kalan o yoğun, şamanik Afrika büyüsü ve ataların gözleyen silüetleri sizi transa sokar.",4"Lalibela Kayaya Oyulmuş Kiliseleri","Lalibela","Etiyopya","Efsaneye göre meleklerin yardımıyla tek bir devasa kayanın içi oyularak gece vakti inşa edilen bu muazzam yeraltı tapınak kompleksi. Zifiri karanlık ibadet tünellerinde yankılanan asırlık ilahiler ve taş duvarlara mühürlenmiş o ağır, ezen ve dünyevi olmayan mistik enerji auranızı felç eder.",5"Axum Dikilitaşları ve Antik Mezarlar","Axum","Etiyopya","Ahit Sandığı'nın gizlendiğine inanılan ve devasa antik pagan obelisklerinin (dikilitaş) gökyüzünü yardığı bu binlerce yıllık nekropol. Kralların yeraltı mezarlarına indiğinizde, havada asılı kalan o ezici, kadim krallık laneti ve toprağın yaydığı o ağır tarihsel anksiyete nefesinizi keser.",4"Cara Hapishanesi (Habs Qara)","Meknes","Fas","Meknes şehrinin altına devasa bir labirent olarak inşa edilen, binlerce Hristiyan kölenin gün ışığı görmeden ölene dek çalıştırıldığı ve asla çıkış yolu bulamadığı yeraltı zindanı. Havasız tünellerin sonsuzluğuna bakarken ruhunuzu emen o devasa klostrofobi ve zincir şıkırtıları; burayı mutlak bir cehennem portalı yapar.",5"Chellah Harabeleri (Cin Şehri)","Rabat","Fas","Eski bir Roma yerleşimi üzerine kurulan ve sonradan kraliyet mezarlığına dönüşen, günümüzde doğanın ve leyleklerin yuttuğu bu izole nekropol. Geceleri eski mezar taşlarının arasında gezen Fas cinlerinin (Djinn) ve kara büyü ritüellerinin bıraktığı o ağır, sülfürik dişil frekans iradenizi ele geçirir.",5"Eski Fes (Fes el Bali) Tabakhaneleri","Fes","Fas","Dünyanın en büyük ve en eski Orta Çağ medinasının, binlerce yıldır aynı yöntemle deri tabaklanan o devasa, kan ve asit kokan karanlık arka sokakları. Hayvan ölümlerinin yarattığı o yoğun, ilkel kurban travması ve dar, oksijensiz sokaklara çöken asırlık bedevi lanetleri ruhunuzu yavaş yavaş zehirler.",4"Telouet Kasbah (Glaoui Sarayı)","Yüksek Atlas Dağları","Fas","Atlas Dağları'nın ücra bir tepesinde, eski bir despot kabile liderine ait olan ve içi çürümeye terk edilmiş bu devasa şato harabesi. Duvarlarındaki muazzam işlemelerin zıtlığında, zindanlarında işkence gören isyancıların o kederli ve agresif feryatları taşların arasına siyah bir aura gibi çökmüştür.",4"El Badi Sarayı Zindanları","Marakeş","Fas","Bir zamanlar 'Eşsiz' anlamına gelen devasa bir sarayken tamamen yağmalanıp bir iskelete dönüşen bu devasa kızıl harabe. Sarayın yeraltındaki o karanlık zindan ağından süzülen, ihanetle öldürülmüş sultanların ve esirlerin yaydığı o ağır, boğucu nekromantik enerji ziyaretçilerin kalbini daraltır.",4"""

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

print("Etiyopya ve Fas kayitlari eklendi.")
