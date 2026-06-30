import csv
import re
import io

data = """"Rig-e Jenn (Cinler Çölü)","Semnan","İran","İran'ın merkezindeki 'Şeytanın Üçgeni' olarak bilinen ve asırlardır cinlerin (ifritlerin) anavatanı olarak kabul edilen bu ölümcül tuz çölü. Kum fırtınalarının arasından yükselen bedensiz kükremeler ve pusulaları çıldırtan devasa manyetik anomaliler; buraya izinsiz giren kervanların nasıl kaybolduğunu kanıtlar.",5"Yezd Sessizlik Kuleleri (Dakhmeh)","Yezd","İran","Zerdüştlerin binlerce yıl boyunca ölülerini etlerini akbabalara yedirmek için açıkta bıraktıkları devasa ve ıssız kuleler. Çöl rüzgarının kuru kemiklerin arasından süzülürken çıkardığı o tiz ses ve toprağa sinmiş olan o saf, ilkel ölüm frekansı; ölümün buradaki mutlak ve sessiz hakimiyetini hissettirir.",5"Evin Hapishanesi","Tahran","İran","Tarih boyunca siyasi mahkumların zindanlara atıldığı ve akıl almaz işkencelerden geçirildiği bu devasa beton kompleks. Geceleri yankılanan o ağır çaresizlik ve taş duvarlara mühürlenmiş kırık zihinlerin yarattığı kaotik anksiyete; hapishanenin etrafında bile fiziksel bir ağırlık (psişik kalkan) oluşturur.",5"Arg-e Bam (Bam Kalesi)","Kirman","İran","Binlerce yıllık kerpiç mimarisiyle ayakta dururken korkunç bir depremle binlerce insana mezar olan bu devasa antik kale. Yıkıntıların arasında durduğunuzda, saniyeler içinde toprağın altına gömülen o canların ani ölüm paniği ve devasa kederi, göğsünüze sarsıcı bir travma frekansı olarak çöker.",4"Shahr-e Yeri (Ağızsızlar Şehri)","Erdebil","İran","Binlerce yıl öncesine ait, yüzleri olan ama ağızları olmayan yüzlerce tuhaf taş heykelle (megalit) dolu bu antik ve lanetli nekropol. Gece ay ışığı bu sessiz taş ordusunun üzerine vurduğunda, konuşamayan ama sizi izleyen bu varlıkların o ağır, okült (büyüsel) enerjisi zihninizi kör bir paniğe sürükler.",5"Takht-e Soleyman (Süleyman'ın Tahtı)","Batı Azerbaycan","İran","Kadim Zerdüşt ateş tapınaklarının bulunduğu, volkanik ve dipsiz bir gölün etrafına kurulu bu gizemli kompleks. Efsaneye göre Kral Süleyman'ın ifritleri hapsettiği derin kraterlerden (Süleyman'ın Zindanı) geceleri yükselen o kükremeler ve sülfür kokulu ağır astral frekans, insanın iradesini ezer.",4"Alamut Kalesi","Kazvin","İran","Hasan Sabbah'ın sarp dağların zirvesine kurduğu ve Haşhaşilerin (suikastçilerin) zihin kontrolü ve fanatizmle yetiştirildiği o efsanevi 'Kartal Yuvası'. Zirvede esen dondurucu rüzgarların getirdiği o saplantılı, kana susamış tarikat enerjisi ve asırlar önce atılan çığlıkların yankısı, auranızı paramparça eder.",5"Mehdishahr Cinler Kalesi (Ghal'eh Jinn)","Semnan","İran","Yerel halkın geceleri yaklaşmaya bile korktuğu, ifritlerin ve alt boyut varlıklarının mekanı olduğuna inanılan bu terk edilmiş taş kale. Harabelerin içinden gelen açıklanamayan gölgeler ve aniden etrafınızı saran o yoğun, yırtıcı izlenme hissi; buranın insan bilincine kapalı bir portal olduğunu fısıldar.",4"Babak Kalesi","Doğu Azerbaycan","İran","Arap istilasına karşı yıllarca kanlı bir direniş gösteren ve sonunda parçalanarak öldürülen Babak Hürremi'nin sarp dağlardaki kalesi. Sisli kış gecelerinde kaleye giden dar patikalarda, asırlar önceki o korkunç savaşın, kılıç şakırtılarının ve dökülen kanın o paslı, ağır frekansı hala aktif bir şekilde yankılanır.",4"Çoğa Zanbil Zigguratı","Huzistan","İran","Elamlıların devasa tanrılarına adadıkları, binlerce yıllık lanetli ve izole piramit tapınak. Etrafındaki o ezici, kadim sessizlik ve Mezopotamya yeraltı tanrılarının uyuyan enerjisi; basamakları tırmanırken ensenizde eski rahiplerin o donuk fısıltılarını hissetmenize ve aklınızı yitirme noktasına gelmenize sebep olur.",5"""

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

print("İran kayitlari eklendi.")
