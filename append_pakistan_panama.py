import csv
import re
import io

data = """"Mohenjo-Daro (Ölüler Tepesi)","Sindh","Pakistan","İndus Vadisi'nin binlerce yıl önce aniden ve gizemli bir şekilde yok olan devasa, kapkaranlık antik şehri. Harabelerin arasında esen çöl rüzgarı, şehrin sokaklarına kazınmış o kadim, kıyamet benzeri ölüm anını ve sokaklarda yığılı kalan binlerce iskeletin donuk enerjisini auranıza kazır.",5"Koh-i-Chiltan Dağları (Kırk Çocuk Zirvesi)","Belucistan","Pakistan","Efsaneye göre dağda ölüme terk edilen kırk çocuğun ruhu tarafından ele geçirilen ve dağcıların yönlerini kaybettiği ıssız zirveler. Zifiri karanlık gecelerde vadilerden yankılanan o görünmez çocuk ağlamaları ve dağın insanı içine çeken o ağır, çekici karanlık frekansı zihninizi bulandırır.",5"Karsaz Yolu (Hayalet Gelin)","Karaçi","Pakistan","Geceleri aniden ortaya çıkan ve gözleri olmayan 'Kırmızı Gelin' silüetiyle ünlenen, sayısız ölümcül trafik kazasının yaşandığı o tekinsiz asfalt yol. Arabanın arka koltuğuna çöken o dondurucu ani soğuk ve asfaltın altından gelen o ağır ölüm bekleyişi sürücüleri deliliğe sürükler.",4"Sheikhupura Kalesi Harabeleri","Pencap","Pakistan","Babür İmparatorluğu'nun en görkemli dönemlerinde inşa edilen ancak sonrasında haremin karanlık entrikalarına ve cinayetlerine sahne olan bu devasa hisar. Zindanlarından ve yıkık avlularından yayılan o yoğun, sülfürik saray zehirlenmesi frekansı ve arafta kalan prenseslerin görünmez feryatları nefesinizi keser.",4"Hawkes Bay Sahili","Karaçi","Pakistan","Dolunay gecelerinde kara büyü (Kala Jadu) ayinlerinin yapıldığı ve denizin altından gizemli varlıkların (Djinn) çıktığına inanılan uzun kumsal. Okyanusun uğultusuna karışan davul sesleri ve kumların altında hissedilen o ağır, boyutsal astral anomali insanı tamamen felç eder.",4"Coiba Adası Zindanları","Coiba Ulusal Parkı","Panama","Panama diktatörlüğü boyunca en vahşi cinayetlerin, 'kaybedilenlerin' (Los Desaparecidos) ve korkunç orman işkencelerinin merkezi olan bu devasa cezaevi adası. Ormanın nemli ve çürük kokusuna karışan mahkum feryatları ve hücre duvarlarına kanla kazınmış o saf, katıksız devlet terörü kalbinizi dondurur.",5"Panama Kanalı (Culebra Kesimi)","Panama Kanalı","Panama","Dünyanın en büyük mühendislik harikası inşa edilirken 25.000'den fazla işçinin sarı humma, sıtma ve toprak kaymalarıyla can verdiği o devasa kanal yarığı. Gemiler geçerken suyun derinliklerinden yükselen o ağır, kitlesel kurban frekansı ve sulara gömülmüş işçilerin toplu çaresizliği auranızı ezer.",5"Darién Boşluğu (Ölüm Ormanı)","Darién","Panama","Güney ile Kuzey Amerika'yı birbirinden ayıran, binlerce kaçağın ve gezginin iz bırakmadan kaybolduğu dünyanın en ölümcül ve karanlık cangılı. Sık ağaçların arasında gezinirken sizi izleyen o gizemli orman varlıkları ve bataklıklarda boğulanların havaya yaydığı o ilkel hayatta kalma paniği zihninizi daraltır.",5"Gorgas Hastanesi (Eski Sarı Humma Koğuşları)","Ancon Tepesi","Panama","Kanal inşaatı sırasında binlerce insanın sarı hummadan kan kusarak can verdiği ve cesetlerin trenlerle morglara taşındığı bu eski, sömürge dönemi hastanesi. Terk edilmiş koğuşlarında hala hissedilen o sinsi, ateşli hastalık frekansı ve kapalı kapılar ardından gelen o görünmez ölüm öksürükleri ruhunuzu dondurur.",4"Casco Viejo Terk Edilmiş Malikaneleri","Panama Şehri","Panama","Korsan Henry Morgan'ın yağmalarıyla ve İspanyol sömürgesinin ağır engizisyon acılarıyla yoğrulmuş eski şehrin çürümeye yüz tutmuş karanlık binaları. Arnavut kaldırımlı sokaklarda yankılanan korsan çizmelerinin sesi ve yıkık malikanelerden taşan o ağır, melankolik kolonist travma zaman algınızı yok eder.",4"""

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

print("Pakistan ve Panama kayitlari eklendi.")
