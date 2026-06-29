import csv
import io

raw_data = """
"Vardø Cadı İnfaz Alanı (Steilneset)","Vardø","Norveç","Kutup dairesinin dondurucu soğuğunda, 17. yüzyılda Avrupa'nın en acımasız cadı avlarının yapıldığı ve 91 kişinin diri diri yakıldığı bu lanetli kıyı. Rüzgarın uğultusuna karışan o tarifsiz yanık et kokusu ve haksız yere katledilenlerin toprağa sinen saf öfkesi, buraya adım atanların aurasını adeta buz gibi bir bıçakla keser.",5
"Lier Akıl Hastanesi","Viken","Norveç","1980'lerde karanlık sırlarıyla terk edilen, hastalara yasadışı LSD deneylerinin ve vahşi lobotomilerin uygulandığı devasa çürüyen kompleks. Duvarları dökülen koğuşlarda yürürken, aklını yitirmiş hastaların göğsünüze binen o ezici anksiyetesini ve koridorlardan süzülen bedensiz, histerik gölgeleri tüm çakralarınızda hissedersiniz.",5
"Hotel Union Øye (Mavi Oda)","Ørsta","Norveç","Sarp dağlar ve fiyortlar arasına gizlenmiş bu asırlık otelin 'Mavi Oda'sı (Blårommet), yasak bir aşkın karanlık sonuna şahitlik etmiştir. İntihar eden genç Linda'nın arafta kalan kederli ruhu odanın içinde hapsolmuştur. Gece yarısı koridorda yankılanan ayak sesleri ve havayı aniden dolduran o boğucu, buz gibi intihar enerjisi ziyaretçilerin aurasını dondurur.",4
"Nidaros Katedrali Mahzeni","Trondheim","Norveç","Kuzey Avrupa'nın en görkemli ama bir o kadar da karanlık gotik yapısı. Güneş battığında katedralin derinliklerinden gelen ve boynunda kanlı bir yara iziyle dolaşan 'Gözleri Oyuk Keşiş'in silüeti, buradaki kutsal enerjinin aslında arafta kalmış çok daha karanlık bir okült titreşimle iç içe geçtiğini kanıtlar.",4
"Pyramiden Hayalet Kasabası","Svalbard","Norveç","Kuzey Kutbu'nun acımasız ıssızlığında, bir gecede terk edilip zamanın 1998'de donup kaldığı bu devasa Sovyet maden şehri. Yılın büyük bir kısmını zifiri karanlıkta geçiren bu buzul kentinde dolaşırken, binaların boş pencerelerinden sizi izleyen o devasa yalnızlık ve soğuk ölüm enerjisi zihninizi felç eder.",5
"Nes Kilise Harabeleri","Viken","Norveç","Karanlık bir ormanın kalbinde yer alan, 1800'lerde karanlık varlıklarla anlaştığı söylenen ve kendi çocuklarını öldürdükten sonra sunak arkasına gömülen rahip Finckenhagen'in lanetli harabesi. Geceleri çöken o ağır, bataklık benzeri enerji ve aniden arkanızda beliren uzun siyah gölgeler iradenizi ele geçirmek ister.",4
"Dalen Hotel (Oda 17)","Telemark","Norveç","Sarp dağların arasında, ejderha başı oymalarıyla süslü bu devasa gotik ahşap otel. Bebeğini öldürüp intihar eden 'İngiliz Kadın' Miss Greenfield'ın kederli ruhu 17 numaralı odada kilitli kalmıştır. Geceleri boş beşiğin sallanma sesi ve havayı aniden dolduran o boğucu, soğuk yas frekansı ziyaretçileri dehşete düşürür.",4
"Fredriksten Kalesi","Halden","Norveç","İsveç Kralı XII. Karl'ın vurularak öldürüldüğü ve yüzlerce askerin kanının aktığı sarp sınır kalesi. Surlarda devriye gezen beyazlı kadın ('Hvite Dame') silüeti ve gece yarısı aniden yükselen bedensiz savaş naraları, toprağın o paslı ve şiddet dolu savaş travmasını hala aktif bir şekilde kustuğunu gösterir.",3
"Bærums Verk Demirhanesi","Viken","Norveç","Yüzyıllar önce köle gibi çalıştırılan işçilerin kanı ve teriyle dönen bu tarihi sanayi bölgesi. Gece çöktüğünde eski fırınların etrafında yeşil elbiseli Anna Krefting'in kontrolcü ruhu dolaşır; o dondurucu nehir rüzgarına karışan örs sesleri, zamanın kırıldığını ve sanayi devriminin o ağır, isli enerjisinin auranızı boğduğunu hissettirir.",3
"Munkholmen (Keşiş Adası)","Trondheim","Norveç","Trondheim fiyordunun ortasında; bir zamanlar idam alanı, manastır ve en azılı suçluların hapsedildiği bir zindan adası. Kıyılarına vuran okyanus dalgalarına karışan kesik başların ağıtları ve adanın üzerindeki o ezici tecrit enerjisi, buraya ayak basanların nefesini kesen karanlık bir ruhsal karantina alanı yaratır.",4
"""

reader = csv.reader(io.StringIO(raw_data.strip()))

with open('perili_mekanlar.csv', 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for row in reader:
        if row:
            row.append("")
            writer.writerow(row)

print("Norveç verileri başarıyla eklendi.")
