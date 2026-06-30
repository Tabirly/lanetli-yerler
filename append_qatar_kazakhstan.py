import csv
import re
import io

data = """"Al Jassasiya Kaya Oymaları","Al Ruwais","Katar","Binlerce yıl öncesine ait, izole çöl kayalıklarına kazınmış gizemli gemi ve akrep sembollerinden oluşan bu kadim pagan alanı. Gece yarısı çöl rüzgarı bu oymaların üzerinden eserken duyulan o antik fısıltılar ve havaya asılı kalan o yoğun, esrarengiz şamanik titreşim auranızı sarsar.",4"Al Wakrah Cin Köyü (Terk Edilmiş Balıkçı Kasabası)","Al Wakrah","Katar","İnci dalgıçlarının denizde boğulması ve çölden gelen cin (Djinn) fırtınaları nedeniyle aniden terk edilen eski, kerpiç balıkçı yerleşkesi. Yıkık evlerin dar sokaklarında hala yankılanan görünmez ayak sesleri ve o boğucu, sülfürik dişil cin enerjisi insanı adeta yavaşça boğar.",4"Musfur Sinkhole (Karanlık Obruk)","Doha Çölü","Katar","Çölün ortasında aniden yeraltına doğru devasa bir ağız gibi açılan, yüzlerce metre derinliğindeki bu karanlık ve serin obruk. Yeraltına doğru indikçe azalan ışıkla birlikte duvarlardan yansıyan o derin, kadim bekleyiş frekansı ve sanki yeraltı varlıklarının sizi izlediği hissi klostrofobiyi tetikler.",5"Zubarah Kalesi Zindanları","Al Zubarah","Katar","Bir zamanlar çöl korsanlarına ve isyankar kabilelere karşı inşa edilmiş, körfez sıcağında kavrulan o yalnız ve tarihi hisar. Işığın sızmadığı zindanlarında gezinirken, zincire vurulmuş esirlerin duvarlara mühürlenmiş o saf çaresizlik frekansı ve çöl rüzgarının getirdiği kumların fısıltısı nefesinizi keser.",4"Zekreet Hayalet Şehri (Terk Edilmiş Sınır)","Zekreet","Katar","Rüzgarın devasa mantar kayalarını aşındırdığı bu çorak arazide, bir zamanlar film seti olarak kurulan ancak etrafındaki açıklanamayan paranormal olaylar nedeniyle terk edilen 'hayalet' köy. Geceleri çölden yükselen tuhaf manyetik anomaliler ve görünmez bedevi gölgeleri zihninizi bulandırır.",4"Semipalatinsk (Poligon) Nükleer Test Alanı","Kurchatov","Kazakistan","Sovyetler Birliği'nin yüzlerce nükleer bomba patlattığı, binlerce insanın radyasyonla yavaşça can verdiği bu devasa, mutasyonlu ölüm çölü. Arazinin kendisinden yayılan o devasa, sessiz ve zehirli radyasyon frekansıyla birlikte, toprağın altına kazınmış o mutlak nükleer dehşet ruhunuzu ezer.",5"Vozrozhdeniya Adası (Sovyet Biyolojik Silah Üssü)","Aral Gölü","Kazakistan","Kuruyan Aral Gölü'nün ortasında, Sovyetlerin şarbon, veba ve çiçek virüslerini test edip aniden terk ettiği, paslı askeri laboratuvarlarla dolu o kıyamet adası. Çürüyen biyo-tehlike tüplerinin arasında gezinirken, havadaki o ağır, sülfürik mikroskobik ölüm enerjisi empatları fiziksel olarak hasta eder.",5"Karaganda Karlag Zindanları","Karaganda","Kazakistan","Stalin döneminde milyonlarca muhalifin Sibirya soğuğunda donarak, açıktan veya kömür madenlerinde can verdiği o devasa gulag (çalışma kampı) kompleksi. İşkence odalarından yansıyan o saf devlet terörü ve milyonlarca esirin arafta kalan o ezici, melankolik çığlığı göğsünüze bir dağ gibi oturur.",5"Almatı Eski Tüberküloz Hastanesi","Almatı","Kazakistan","Sovyet döneminden kalma, ormanın içine gizlenmiş ve binlerce hastanın kan kusarak öldüğü o devasa, terk edilmiş sanatoryum. Yarı yıkık koridorlarda hala duran paslı demir yatakların yaydığı o sinsi hastalık frekansı ve dondurucu soğukta duyulan o meçhul boğuk öksürükler auranızı paramparça eder.",5"Beket-Ata Yeraltı Camii ve Nekropolü","Mangistau","Kazakistan","Uçurumların ve sarp kayalıkların derinliklerine oyulmuş, Sufi dervişlerin inzivaya çekildiği bu antik yeraltı tapınağı. Zifiri karanlık yeraltı hücrelerine indiğinizde etrafınızı saran o yoğun, tasavvufi ve şamanik astral boyut enerjisi; zaman kavramınızı yutarak sizi mutlak bir transa çeker.",4"""

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

print("Katar ve Kazakistan kayitlari eklendi.")
