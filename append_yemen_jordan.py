import csv
import re
import io

data = """"Barhout Kuyusu (Cehennem Kuyusu)","Al Mahrah","Yemen","Çölün ortasında, dibi görünmeyen devasa ve karanlık bir obruk. Yerel efsanelere göre 'Cinlerin Zindanı' olan ve kafir ruhların hapsedildiği bu çukurdan yükselen o zehirli, sülfürik koku ve aşağıdan geldiği iddia edilen boğuk iniltiler; yeraltının o korkunç, ilkel öfkesini yüzeye taşır.",5"Şibam (Çölün Manhattan'ı) Harabeleri","Hadhramaut","Yemen","Çölün ortasında, asırlık devasa kerpiç gökdelenlerden oluşan ve geceleri karanlığa gömülen bu kadim hayalet şehir. Boş ve rüzgarlı dar sokaklarında yankılanan kabile savaşlarının çığlıkları ve o boğucu, kurak kum frekansı; zamanın burada kumların altına gömülüp çürüdüğünü hissettirir.",4"Socotra Adası (Ejderha Kanı Ormanı)","Socotra","Yemen","Dünyanın geri kalanından tamamen izole edilmiş, uzaylımsı bitki örtüsüyle kaplı olan ve ağaçlarının gövdelerinden kan kırmızısı bir reçine akan bu mistik ada. Eski büyücülerin sırlarını saklayan bu adaya adım attığınızda, doğanın yaydığı o devasa, telepatik ve dışlayıcı enerji aklınızı bulandırır.",4"Ghumdan Sarayı Harabeleri","Sana'a","Yemen","İslam öncesi dönemin en efsanevi saraylarından biri olan ve cinlerin yardımıyla inşa edildiğine inanılan devasa yapı. Savaşlarla yıkılan ve efsanesi kana bulanan bu harabelerde esen gece rüzgarı, asırlar önce yaşamış kâhinlerin fısıltılarını taşıyarak insanı şiddetli bir paranoyaya sürükler.",4"Marib Antik Barajı ve Tapınakları","Marib","Yemen","Saba Melikesi'nin krallığının kalbi olan ve devasa bir selle yerle bir edilen bu antik harabeler. Kumların altından çıkarılan eski güneş tapınaklarında, sular altında kalıp boğulan binlerce insanın kederi ve o ani kıyamet travması; alanı hala aktif bir karanlık astral portala dönüştürmektedir.",5"Petra (Cinlerin Şehri)","Ma'an","Ürdün","Kızıl kayalara oyulmuş, dünyanın en görkemli ama bir o kadar da nekromantik antik şehri. Gündüzleri turist dolu olsa da gece çöktüğünde uyanan Nebati krallarının ruhları ve yerel Bedevilerin girmeye korktuğu 'Cin Blokları'; etrafa devasa, ağır ve kan dondurucu bir mezar frekansı yayar.",5"Kerak Kalesi","Karak","Ürdün","Haçlı Seferleri döneminde, kana susamış Reynald de Châtillon'un esirlerini surlardan aşağı canlı canlı attırdığı bu devasa askeri kale. Zindanların karanlık taş duvarlarına sinmiş olan o çaresiz düşüş korkusu ve işkence travması, günümüzde bile empatları nefessiz bırakarak diz çöktürür.",5"Lut Gölü (Ölüdeniz) ve Sodom Kalıntıları","Ölüdeniz","Ürdün","İlahi bir gazapla yeryüzünden silinen Sodom ve Gomora şehirlerinin sular altında kaldığına inanılan, dünyanın en alçak ve ölü noktası. Hiçbir canlının yaşamadığı o yoğun tuzlu suyun yüzeyinden yayılan ve gökyüzünü bile karartan o ağır, sülfürik yargılanma enerjisi ruhunuzu adeta ezer.",5"Machaeurus (İnfaz Kalesi)","Madaba","Ürdün","Vaftizci Yahya'nın hapsedilip kafasının kesildiği, Ölüdeniz'e bakan o sarp ve ıssız tepe kalesi. Yıkıntılar arasında durduğunuzda, tarihin en meşhur infazlarından birinin yarattığı o ani, keskin kan kokusu ve arafta kalan o ezici masumiyet frekansı boğazınızda fiziksel bir düğüm oluşturur.",4"Quseir Amra (Çöl Kalesi)","Zarqa","Ürdün","Çölün ortasında, Emevi halifelerinin gizli zevkleri ve yasak eğlenceleri için kullandıkları bu izole edilmiş taş köşk. Duvarlarını süsleyen ve İslam sanatında nadir görülen çıplak fresklerin arasında gezinirken; asırlar önceki günahların, zehirlenmelerin ve karanlık suikastlerin o sinsice fısıldayan enerjisi bedeninizi sarar.",4"""

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

print("Yemen ve Urdun kayitlari eklendi.")
