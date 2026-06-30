import csv
import re
import io

data = """"Diplomat Hotel (Terk Edilmiş Rahipler Zindanı)","Baguio City","Filipinler","İkinci Dünya Savaşı sırasında Japon ordusunun karargah ve işkence merkezi olarak kullandığı, rahiplerin ve sivillerin başlarının kesildiği bu devasa beton harabe. Geceleri çöken yoğun sisin içinde yankılanan çaresiz çığlıklar ve kesik başlı hayaletlerin kederli, ağır travmatik frekansı ziyaretçileri dehşete düşürür.",5"Clark Hava Üssü Hastanesi","Angeles City","Filipinler","Vietnam Savaşı sırasında binlerce ağır yaralı ve travmatize Amerikan askerinin öldüğü, sonradan terk edilen bu çürümüş hastane. Paslı koridorlarda gezinirken duyulan görünmez sedye tekerleklerinin gıcırtısı ve ölüm döşeğindeki askerlerin o sülfürik, ağır savaş anksiyetesi auranızı bir mengene gibi sıkar.",5"Manila Film Merkezi","Pasay City","Filipinler","1981'deki inşaatı sırasında iskelenin çökmesiyle yüzlerce işçinin canlı canlı çimentoya gömüldüğü ve projenin durmaması için cesetlerin üzerine beton dökülen lanetli yapı. Binanın karanlık salonlarında hala betonun içinden gelen tırmalama sesleri ve hapsolmuş ruhların o ezici, klostrofobik öfkesi binayı esir almıştır.",5"Ozone Disco Harabesi","Quezon City","Filipinler","1996 yılında kapıların içe açılması yüzünden sıkışan 162 gencin yanarak can verdiği o korkunç diskonun kapkara iskeleti. Harabeye yaklaştığınızda hala burnunuza gelen o psişik yanık et kokusu ve duvarlara kazınmış çaresiz el izlerinden yayılan saf ölüm paniği zihninizi felç eder.",5"Malinta Tüneli","Corregidor Adası","Filipinler","Manila Körfezi'ndeki bu stratejik adanın altında, İkinci Dünya Savaşı'nda Japon askerlerinin topluca intihar ettiği o devasa ve havasız tünel ağı. Zifiri karanlığın içinde ilerlerken mağara duvarlarından sızan o mutlak, fanatik intihar enerjisi ve görünmez ellerin dokunuşları empatları nefessiz bırakır.",4"Eski Gazze Tünelleri ve Katakompları","Gazze","Filistin","Binlerce yıldır savaşların, kuşatmaların ve yıkımların altında katman katman biriken o devasa, havasız yeraltı labirentleri. Işığın sızmadığı dehlizlerde asırlardır biriken o yoğun savaş travması, dökülen kanların toprağa işleyen sülfürik kederi ve arafta kalmış kayıp sivil ruhların ezici ağırlığı nefesinizi keser.",5"Tel es-Sultan (Antik Eriha) Harabeleri","Eriha","Filistin","Dünyanın en eski ve en alçak şehirlerinden biri olan, savaş ve lanetlerle yerle bir edilen bu on bin yıllık antik toz çölü. Güneşin kavurucu sıcağında bile harabelerin arasında esen o soğuk, kadim okült ölüm rüzgarı; asırlar öncesindeki yıkım ve kıyımların hafızasını zihninize kazır.",4"Qumran Mağaraları (Ölü Deniz Kıyıları)","Batı Şeria","Filistin","Ölü Deniz Yazmaları'nın bulunduğu, çöl sıcağının kuruttuğu bu izole, derin yeraltı mağaraları. Tuzlu, ölü denizin yaydığı o ağır, dünyevi olmayan mineral frekansıyla birleşen bu mağaralardaki münzevi yalnızlık ve binlerce yıllık sessiz ezoterik bekleyiş, zaman algınızı tamamen yok eder.",4"Sebastia (Samiriye) Antik Harabeleri","Nablus","Filistin","Romalılardan ve antik krallıklardan kalma devasa sütunların ve yıkık tapınakların rüzgarda aşındığı bu terk edilmiş kadim tepe. Geceleri antik mezarların arasından yükselen o yoğun, kraliyet kanıyla karışık melankolik pagan frekansı ve görünmez tapınak bekçilerinin adımları tüyler ürperticidir.",4"Hebron (El-Halil) Eski Şehir Zindanları","Batı Şeria","Filistin","Binlerce yıllık din savaşlarına, katliamlara ve kuşatmalara tanıklık etmiş bu dar, taş sokakların altındaki karanlık ve unutulmuş sığınaklar. Duvarlara kazınmış asırlık acılar, nesiller boyu aktarılan o saf travmatik öfke ve kapalı mekanlara sinen o sülfürik çatışma enerjisi kalbinizi daraltır.",5"""

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

print("Filipinler ve Filistin kayitlari eklendi.")
