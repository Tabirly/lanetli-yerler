import csv
import re
import io

data = """"Al-Salam Terk Edilmiş Sarayı","Kuveyt Şehri","Kuveyt","Irak işgali sırasında bombalanarak enkaza dönen ve içi cesetlerle dolan bu eski devasa kraliyet sarayı. Kömürleşmiş ve kurşun delikleriyle dolu mermer koridorlarda yürürken, duvarlara sinen o ezici savaş travması ve işkence gören askerlerin arafta kalan o boğuk çığlıkları zihninizi sarar.",5"Failaka Adası Savaş Harabeleri","Basra Körfezi","Kuveyt","Körfez Savaşı sırasında ağır bombardıman yiyen ve halkı tamamen sürülen, delik deşik binalarla dolu o hayalet ada. Terk edilmiş okullarda ve evlerde gezinirken esen tuzlu rüzgarın taşıdığı o devasa, melankolik kitlesel ölüm frekansı kalbinizi dondurur.",5"Mutla Geçidi (Ölüm Yolu)","Jahra","Kuveyt","Körfez Savaşı'nda geri çekilen binlerce Irak askerinin müttefik uçakları tarafından bombalanarak kömürleştiği o korkunç çöl otoyolu. Geceleri asfalttan yansıyan o saf, katıksız kitlesel yanma anksiyetesi ve ufukta beliren meçhul askeri silüetler auranızı paramparça eder.",5"Eski İngiliz Hristiyan Mezarlığı","Kuveyt Şehri","Kuveyt","Körfezin sert ikliminde çürüyüp gitmiş eski sömürgecilerin, diplomatların ve koloni kurbanlarının gömülü olduğu kapalı ve tekinsiz nekropol. Kum fırtınalarının yıprattığı kırık haçların arasında dolaşırken, o derin sömürge hırsı ve yalıtılmış ölüm kederi nefesinizi keser.",4"Jleeb Al-Shuyoukh (Karanlık Çöplükler)","Kuveyt Şehri","Kuveyt","Kaçak işçilerin, insan kaçakçılarının ve mafyaların kontrol ettiği, devletin bile giremediği o devasa ve derme çatma, kaotik gecekondu bölgesi. Oksijensiz, çöp ve kanalizasyon kokan dar sokaklarda vahşice işlenen cinayetlerin yaydığı o ağır, boğucu alt-astral karanlık frekansı empatları zehirler.",4"Yodok Toplama Kampı (Kamp 15)","Güney Hamgyong","Kuzey Kore","Yüz binlerce muhalifin açlıktan kırıldığı, madenlerde ölene dek çalıştırıldığı ve canlı canlı gömüldüğü, dünyadaki cehennemin fiziksel karşılığı. Karlarla kaplı dağların arasına gizlenmiş bu ölüm vadisinden yükselen o mutlak, sonsuz işkence ve çaresizlik enerjisi insan ruhunu anında ezer geçer.",5"Ryugyong Oteli (Kıyamet Gökdeleni)","Pyongyang","Kuzey Kore","Şehrin ortasında devasa, sivri bir piramit gibi yükselen ancak onlarca yıl boyunca içi tamamen boş ve çürümeye terk edilmiş beton ucubesi gökdelen. Asansörsüz zifiri karanlık şaftlarında ve kapkaranlık devasa boşluğunda yankılanan o ağır totaliter delilik ve hipnotik boyut anomalisi zihninizi yutar.",5"Kijong-dong (Sahte Sınır Köyü)","Kuzey Kore DMZ","Kuzey Kore","Güney Kore'yi etkilemek için sınıra inşa edilen, içi tamamen boş devasa beton binalardan ve hoparlörlerden yükselen propaganda marşlarından ibaret olan 'Hayalet Köy'. Kimsenin yaşamadığı sahte binaların boş pencerelerinden size doğru akan o distopik, mekanik ve ruhsuz karanlık frekans tüyler ürperticidir.",4"Kaesong Gizli Zindanları","Kaesong","Kuzey Kore","Sınır hattına yakın, devletin 'buharlaştırdığı' muhaliflerin tutulduğu ve gün yüzü görmeden asitle eritildiği iddia edilen yeraltı sorgu labirentleri. Zifiri karanlık yeraltı hücrelerine mühürlenmiş o vahşi devlet terörü ve insan bedeninin tamamen hiçliğe karışma korkusu kalbinize bıçak gibi saplanır.",5"Chongjin Ölüm Mahalleleri","Kuzey Hamgyong","Kuzey Kore","1990'lardaki devasa 'Arduous March' kıtlığında sokaklarında yüz binlerce insanın açlıktan yığılıp can verdiği o gri, paslı ağır sanayi şehri. Terk edilmiş dondurucu fabrikaların ve paslı vinçlerin etrafına çöken o devasa, sessiz ve kitlesel açlık kederi auranızı adeta soğurur.",5"""

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

print("Kuveyt ve Kuzey Kore kayitlari eklendi.")
