import csv
import re
import io

data = """"Fort St. Angelo (Gri Kadın'ın Zindanı)","Birgu","Malta","Büyük Malta Kuşatması'nda binlerce bedenin parçalandığı bu kanlı kale. Zindanlarında hapsedilen ve trajik bir şekilde katledilen 'Gri Kadın'ın araftaki ruhu, taş duvarlardan sızan yoğun bir çaresizlik enerjisi yayar; gece nöbetçileri asırlardır kılıç şakırtıları ve boğuk feryatlar duyduklarını rapor eder.",5
"Lazzaretto (Veba Hastanesi)","Manoel Adası","Malta","Yüzyıllar boyunca veba kurbanlarının tecrit edilerek çürümeye terk edildiği, okyanus rüzgarlarına açık bu devasa karantina merkezi. Yıkık dökük koridorlarında yürürken, hastalığın o genzi yakan sülfürik enerjisi ve binlerce kişinin can çekiştiği ölüm yataklarından yükselen kolektif acı, auranızı adeta zehirler.",5
"St. Paul Katakompları","Rabat","Malta","Romalıların ve erken dönem Hıristiyanların kullandığı, yerin metrelerce altına inen bu klostrofobik, zifiri karanlık ölüm labirenti. On binlerce iskeletin yattığı bu daracık kaya oyuklarında ilerlerken, yeraltının o boğucu, ezici frekansını hisseder ve karanlığın içinden gelen antik fısıltılarla aklınızın sınırlarını zorlarsınız.",5
"Mdina Sokakları (Sessiz Şehir)","Mdina","Malta","Geceleri sokak lambalarının aydınlatamadığı bu dar ve kadim labirentlerde, kafası kesilmiş eski şövalyelerin ve 'Beyazlı Kadın'ın ağır, melankolik frekansı dolaşır. Şehrin o ezici, taş duvarlara sinmiş mutlak sessizliği, insanın kendi kalp atışlarını bile dehşet verici bir yankıya dönüştürür.",4
"Villa Sans Souci","Marsaxlokk","Malta","Malta'nın en ürkütücü ve tekinsiz terk edilmiş malikanelerinden biri. İçeri adım atar atmaz dışarıdaki tüm seslerin kesildiği, havanın aniden buz kestiği ve boğucu bir psişik ağırlığın göğse oturduğu iddia edilir. Evi mesken tutan karanlık alt boyut varlıklarının fısıltıları, insan iradesini sıfırlayan bir dehşet saçar.",5
"Fort Manoel (Kara Şövalye)","Gzira","Malta","İkinci Dünya Savaşı'nda ağır bombardımana tutulan bu tarihi kalede, tam zırhlı ve yüzsüz bir 'Kara Şövalye'nin nöbet tuttuğu anlatılır. Tapınak şövalyelerinin ezoterik ritüellerinden arta kalan o baskın, eril ve düşmanca frekans, kaleye izinsiz girenlerin zihinsel kalkanlarını saniyeler içinde parçalar.",4
"Verdala Sarayı (Mavi Kadın)","Siggiewi","Malta","Görkemli Malta Şövalyeleri'nin sarayı olan bu yapı, istenmeyen bir evlilikten kaçarken balkondan atlayıp ölen 'Mavili Kadın'ın hüzünlü silüetine ev sahipliği yapar. Geceleri boş aynalarda beliren o yoğun dişil keder ve sarayın ıssız salonlarında yankılanan ayak sesleri, zamanın o intihar anında kilitlendiğini gösterir.",4
"Splendid Hotel","Valletta","Malta","Eski günlerinde Strait Sokağı'nın genelevlerinden biri olan ve acımasız bir cinayete kurban giden bir kadının ruhunun hapsolduğu bu terk edilmiş otel. Boş odalarda kendi kendine fırlatılan eşyalar ve havada asılı kalan o paslı kan kokusu, buradaki poltergeist aktivitesinin son derece agresif ve kin dolu olduğunu kanıtlar.",4
"Fort St. Elmo","Valletta","Malta","Osmanlı kuşatmasında neredeyse her santiminin kanla sulandığı, binlerce şövalyenin ve askerin katledildiği bu devasa savunma kalesi. Savaşın o primal, kaotik vahşet frekansı surların içine hapsolmuştur; gece rüzgarı denizden estiğinde, top seslerine karışan bedensiz ağıtlar insanı psikolojik bir komaya sokar.",4
"Telgħa t'Alla u Ommu (Lanetli Yokuş)","Naxxar","Malta","Malta'nın en gizemli ve ölümcül kazalarına sahne olan bu tepe yolu. Geceleri aniden yola fırlayan genç bir kız silüetinin veya dikiz aynasında beliren gölgelerin, sürücüleri yoldan çıkarmaya çalıştığı bilinir. Yoldaki o karanlık, yırtıcı ve kurban isteyen elemental enerji bölge halkını dehşete düşürür.",3"""

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

print("Malta kayitlari eklendi.")
