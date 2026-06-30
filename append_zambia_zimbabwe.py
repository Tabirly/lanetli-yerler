import csv
import re
import io

data = """"Victoria Şelalesi (Mosi-oa-Tunya) Cin Havuzları","Livingstone","Zambiya","'Gürleyen Duman'ın zifiri derinliklerinde yer alan ve yerel şamanlara göre öfkeli su cinlerinin (Mamba Muntu) yaşadığı ölümcül kayalıklar. Su buharının içinde aniden beliren boğulmuş insan silüetleri ve şelalenin o yutucu, kükreyen enerjisi aklınızı çelip sizi uçuruma doğru hipnotize eder.",5"Shiwa Ngandu Malikanesi","Chinsali","Zambiya","Afrika'nın ıssız ormanlarının kalbine İngiliz asilzadesi Sir Stewart Gore-Browne tarafından inşa edilmiş bu devasa sömürge dönemi malikanesi. Sahiplerinin kederli hayaletlerinin ve sömürülen yerlilerin arafta kalmış o yoğun, ağır psişik enerjisinin dolaştığı boş koridorlar, insanı derin bir klostrofobiye sokar.",4"Kabwe Kurşun Madeni (Broken Hill)","Kabwe","Zambiya","Dünyanın en zehirli şehirlerinden birinde, on binlerce işçinin ölümüne ve sakat kalmasına yol açan devasa açık maden çukurları. Terk edilmiş şaftların etrafında gezinirken, toprağı bile zehirleyen o saf sülfürik acı frekansı ve hastalıktan kırılan madencilerin boğuk öksürük sesleri auranızı ezer.",5"Kariba Barajı (Nyaminyami'nin Gazabı)","Kariba","Zambiya","İnşaatı sırasında yerel Tonga halkının sular altında kalan kutsal vadileri ve nehir tanrısı Nyaminyami'nin lanetiyle bağdaştırılan devasa yapı. Betonun içine gömülen onlarca işçinin feryatları ve nehir tanrısının barajı yıkmaya çalışan o devasa, elementer dişil öfkesi havada statik bir elektrik yaratır.",5"Zambezi Nehri Ölüm Girdapları","Zambezi Bölgesi","Zambiya","Asırlar boyunca köle ticaretinde kaçakçıların teknelerinin battığı ve sayısız bedenin timsahlara yem olduğu bu zifiri akıntılar. Gece nehir kıyısında durduğunuzda, zincirlerle boğulan kölelerin o çaresiz, boğuk çığlıkları ve suyun o karanlık, yutucu astral çekim gücü ruhunuzu daraltır.",4"Büyük Zimbabve Harabeleri","Masvingo","Zimbabve","Afrika kıtasının Sahra altındaki en büyük antik taş şehri olan ve kralların ruhlarının (Mhondoro) hala koruduğu bu devasa labirent. Ay ışığında taş duvarların arasından yükselen görünmez şamanların ritmik fısıltıları ve o ilkel, saf kıta enerjisi; buraya izinsiz girenlerin zihinlerini şiddetli bir transa zorlar.",5"Bvumba Dağları (Leopard Rock)","Mutare","Zimbabve","Sislerle kaplı bu mistik zirvelerde dolaşan yalnız ruhlar ve 'Beyazlı Kadın' efsanelerinin merkezi. Şiddetli rüzgarların arasında açıklanamayan feryatların yankılandığı ve dağ elementallerinin insanı ormanın derinliklerine, geri dönüşü olmayan bir izolasyona çektiği o ağır, melankolik frekans.",4"Matobo Tepeleri","Bulawayo","Zimbabve","Binlerce yıllık kaya resimleriyle dolu olan ve hem kadim kralların hem de sömürgeci Cecil Rhodes'un mezarını barındıran devasa granit tepe. Yerli halkın 'Ruhların Oturduğu Yer' (Malindidzimu) dediği bu alanda, gece uyanan devasa atalar enerjisi ve sömürgecilerin çatışan auraları zihinsel bir fırtına koparır.",5"Chinhoyi Mağaraları (Sessiz Havuz)","Chinhoyi","Zimbabve","19. yüzyılda Nguni akıncılarının yerel kabileleri katlederek yüzlerce insanı dibi görünmeyen kobalt mavisi havuzlara diri diri attığı bu karanlık dehliz. Yeraltı suyunun o buz gibi, pürüzsüz yüzeyine bakarken derinlerden gelen boğuk iniltiler ve katliamın o sessiz ama ezici travması empatları nefessiz bırakır.",5"Bulawayo Eski Tren İstasyonu ve Mezarlığı","Bulawayo","Zimbabve","Afrika'nın sömürge demiryolu ağının kalbi olan ve kanlı savaşlar, hastalıklar yüzünden sayısız ölüme sahne olan bu paslı sanayi kalıntısı. Geceleri kullanılmayan raylarda ilerleyen hayalet buharlı tren sesleri ve savaşta can veren askerlerin o kederli, ağır frekansı burayı aktif bir astral istasyona çevirmiştir.",4"""

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

print("Zambiya ve Zimbabve kayitlari eklendi.")
