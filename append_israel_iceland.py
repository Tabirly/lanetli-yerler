import csv
import re
import io

data = """"Kudüs Yeraltı Tünelleri ve Katakompları","Kudüs","İsrail","Üç semavi dinin de en kanlı din savaşlarını ve kuşatmalarını yaşadığı, eski şehrin altındaki o devasa, havasız dehlizler. Haçlı kılıçlarından kaçanların yığıldığı bu taş tünellerde ilerlerken, binlerce yıllık dini fanatizmin, dökülen kanların ve esir feryatlarının yarattığı o ezici, kadim enerji nefesinizi keser.",5"Masada Kalesi","Ölü Deniz","İsrail","Romalıların kuşatmasına karşı direnen ve teslim olmamak için 900'den fazla Yahudi isyancının topluca intihar ettiği, sarp bir kayalığın zirvesindeki devasa kale. Çölün o ölümcül sıcağında harabeler arasında gezerken, o toplu intihar anının yarattığı saf, fanatik ve kederli okült frekans ruhunuzu daraltır.",5"Akka (Acre) Eski Zindanları","Akka","İsrail","Tapınak Şövalyeleri'nin, Osmanlıların ve İngiliz sömürgesinin acımasız işkencelerine sahne olan, Akdeniz kıyısındaki o rutubetli yeraltı kalesi. Taş duvarlarına zincirlenmiş mahkumların iniltileriyle karışan deniz dalgalarının sesi ve zifiri karanlıktaki o ağır, kanlı haçlı frekansı auranızı felç eder.",4"Safed (Tzfat) Kabala Mezarlıkları","Safed","İsrail","Asırlardır Kabala ustalarının ve mistiklerin gömüldüğü, dar sokaklarla ulaşılan bu kadim, ezoterik dağ nekropolü. Gece yarısı mezar taşları arasında hissedilen o devasa boyutlararası manyetizma ve görünmez varlıkların (dybbuk) fısıltıları, buranın alt astral alemlere açılan aktif bir portal olduğunu kanıtlar.",5"Megiddo (Armageddon) Harabeleri","Kuzey İsrail","İsrail","İncil'de kıyamet savaşının (Armageddon) kopacağı yer olarak kehanet edilen, üzerinde sayısız antik savaşın yaşandığı kanlı tepe. Harabelerin altındaki gizli su tünellerinde yürürken, asırlarca dökülen kanların toprağa işlediği o yutucu, kıyamet anksiyetesi ve saf şiddet frekansı empatları paniğe sürükler.",4"Dimmuborgir (Kara Şatolar)","Mývatn","İzlanda","Lavların soğuyarak devasa, gotik şatolar ve kapkara heykeller oluşturduğu, efsaneye göre Elflerin ve ölümcül Trollerin (Yule Lads) yaşadığı o karanlık labirent. Buz gibi rüzgarların lav kayalıklarında çıkardığı şeytani ıslıklar ve ortamın o ağır, dışlayıcı elementer büyüsü zihninize ağır bir sis gibi çöker.",5"Höfði Evi (Höfdi House)","Reykjavik","İzlanda","Soğuk Savaş'ı bitiren zirveye ev sahipliği yapan ancak asıl şöhretini içinde yaşayan ve sürekli eşyaları fırlatan meşhur 'Beyazlı Kadın' hayaletiyle kazanan bu ahşap ev. Odanın içinde aniden dondurucu bir soğuğun belirmesi ve ensenizde kilitlenen o buz gibi, kederli poltergeist enerjisi tüyler ürperticidir.",4"Hekla Yanardağı (Cehennem Kapısı)","Güney İzlanda","İzlanda","Orta Çağ boyunca Avrupa'da 'Cehenneme açılan kapı' olarak bilinen ve cadıların lanetli ruhlarla buluştuğuna inanılan aktif volkan. Zirvesindeki zehirli sülfür gazlarının arasında yankılanan o derin yeraltı homurtuları ve magmanın yaydığı o devasa, ilkel yıkım frekansı auranızı doğrudan deler geçer.",5"Lagarfljót Gölü","Egilsstaðir","İzlanda","Efsanevi devasa 'solucan canavarının' yaşadığına inanılan, buzlu ve dipsiz karanlık göl. Sisin gölün pürüzsüz ve kara yüzeyini kapladığı anlarda suyun altından gelen o ağır, ritmik boyutsal titreşim ve gölün insanı içine çeken o hipnotik, boğucu enerjisi sizi tamamen felç eder.",4"Djúpalónssandur Kara Kum Plajı","Snæfellsnes","İzlanda","Geçmişteki sayısız gemi kazasının ve boğularak ölen balıkçıların parçalanmış gemi enkazlarının sergilendiği, zifiri siyah kumlarla kaplı ıssız sahil. Okyanusun devasa dalgalarıyla birlikte karaya vuran o ağır, sülfürik denizci kederi ve hayaletimsi feryatlar; bu plajı bir açık hava nekropolüne çevirir.",4"""

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

print("İsrail ve İzlanda kayitlari eklendi.")
