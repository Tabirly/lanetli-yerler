import csv
import re
import io

data = """"Larnach Kalesi","Dunedin","Yeni Zelanda","Yeni Zelanda'nın tek kalesi olan ve sahiplerinin ardı ardına trajik intiharlarla yok olduğu bu Viktorya dönemi malikanesi. Geceleri balo salonunda yankılanan fısıltılar ve 'Leydi Kate'in o ezici, melankolik hayaleti; kalenin asırlık, karanlık bir hüznün merkez üssü olduğunu ziyaretçilerin göğsüne ağır bir taş gibi oturtur.",5"Napier Hapishanesi","Napier","Yeni Zelanda","Ülkenin en eski hapishanesinde, sayısız idamın gerçekleştiği o kanlı ve rutubetli zindanlar. İnfaz avlusunda durduğunuzda, boynu kırılan mahkumların o saplantılı ölüm paniği ve havada asılı kalan paslı kan frekansı, zihinsel kalkanlarınızı bir anda parçalayan agresif bir poltergeist aktivitesi yaratır.",5"Kingseat Psikiyatri Hastanesi","Karaka","Yeni Zelanda","Zamanında yüzlerce personelin ve hastanın korkunç şartlar altında intihar ettiği, çürümeye terk edilmiş devasa bir tımarhane kompleksi. Yıkık koğuşların içinde dolaşırken, aklını yitirenlerin o histerik çığlıkları ve duvarlara sinmiş olan o saf delilik enerjisi, auranızı fiziksel olarak sarsar.",5"Spirits Bay (Kapowairua)","Northland","Yeni Zelanda","Maori mitolojisinde ölenlerin ruhlarının öte aleme (Hawaiki) geçiş yaptığı, okyanusun kıyısındaki bu devasa ve ıssız kutsal kumsal. Fırtınalı gecelerde dalgaların sesine karışan bedensiz ağıtlar ve toprağın o yutucu, ilkel çekim gücü, insanın kendi yaşam enerjisinin çekildiğini hissetmesine sebep olur.",5"Seacliff Akıl Hastanesi Harabeleri","Otago","Yeni Zelanda","1942'de çıkan korkunç bir yangında kilitli koğuşlarda diri diri yanan 37 kadın hastanın feci şekilde can verdiği bu gotik harabe. Ormanın yuttuğu taş yıkıntıların arasında hala yankılanan o çaresiz feryatlar ve ateşin yarattığı saf dehşet frekansı empatları anında nefessiz bırakır.",4"St. James Tiyatrosu","Wellington","Yeni Zelanda","Sahneden düşerek ölen Rus balerin 'Yuri' ve intihar eden müzisyenlerin ruhlarına ev sahipliği yapan bu ihtişamlı ama karanlık tiyatro. Seyircisiz salonda kendiliğinden yankılanan koro sesleri ve sahneden size doğru süzülen o soğuk, dramatik ölüm frekansı buranın bir astral sahne olduğunu gösterir.",4"Vulcan Oteli","St Bathans","Yeni Zelanda","Eski bir altın madeni kasabasında, boğularak öldürülen 'Rose' isimli hayat kadınının öfkesiyle lanetlenmiş tarihi pub. Özellikle erkek misafirlerin odalarında uyurken hissettikleri o boğucu baskı ve agresif dişil öfke enerjisi, geçmişteki vahşetin arafta kilitli kaldığını fısıldar.",4"Carlile Evi","Auckland","Yeni Zelanda","Geçmişte bir yetimhane olan ve 43 çocuğun yanarak feci şekilde can verdiği iddia edilen, duvarları isli ve yıkık dökük bu lanetli köşk. Boş pencerelerden bakan çocuk silüetleri ve içeride aniden düşen dondurucu sıcaklık, o korkunç yangının travmasını sonsuz bir döngüye sokmuştur.",4"Waitomo Parıltılı Mağaraları (Lanetli Bölgeler)","Waikato","Yeni Zelanda","Turistik rotaların dışında kalan ve kadim Maori şamanlarının büyüyle mühürlediği zifiri karanlık yeraltı dehlizleri. Yerin derinliklerinde ilerlerken suyun çıkardığı o hipnotik ses ve yeraltı elementallerinin zihninizi bulandıran karanlık çağrısı, insanı klostrofobik bir paniğe sürükler.",4"Waipukurau Terkedilmiş Hastanesi","Hawke's Bay","Yeni Zelanda","Çürüyen ameliyathaneleri ve paslı tıbbi aletleriyle zamanın durduğu, devasa ve ıssız bir hastane kompleksi. Koridorların sonundan size doğru yaklaşan açıklanamayan adım sesleri ve morg bölgesine sinmiş o ağır, sülfürik hastalık enerjisi; buranın alt boyut varlıkları için bir yuvaya dönüştüğünü kanıtlar.",4"""

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

print("Yeni Zelanda kayitlari eklendi.")
