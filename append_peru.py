import csv
import re
import io

data = """"Casa Matusita","Lima","Peru","Güney Amerika'nın en tehlikeli ve en meşhur lanetli evi. Sahiplerinin delirdiği, cinayetlerin işlendiği ve şeytani ritüellerin yapıldığı ikinci katına çıkanların ya öldüğü ya da akıl hastanesine kapatıldığı iddia edilir. Evin yanından geçerken bile pencerelerden sızan o kaotik, saf delilik frekansı auranızı bir mengene gibi sıkar.",5"San Francisco Katakompları","Lima","Peru","Yerin metrelerce altına kazılmış ve kemikleri geometrik desenlerle dizilmiş 25.000'den fazla bedeni barındıran zifiri karanlık yeraltı labirenti. Işığın girmediği klostrofobik dehlizlerde ilerlerken, binlerce iskeletin oluşturduğu o devasa ve ağır nekromantik enerji nefesinizi kesecek kadar yoğundur.",5"Chauchilla Mezarlığı","Nazca","Peru","Çölün ortasında, mezar soyguncuları tarafından parçalanmış ve güneşin altında kurumaya terk edilmiş yüzlerce antik Nazca mumyasının bulunduğu bu dehşet verici alan. Gece rüzgarı kurumuş kemiklerin arasından geçerken, saygısızlığa uğrayan ataların o intikamcı ve ilkel (primal) öfkesi ziyaretçileri adeta felç eder.",5"Real Felipe Kalesi","Callao","Peru","İspanyol sömürge döneminin kanlı tarihini taşıyan, korsan saldırılarına ve ağır işkencelere sahne olmuş devasa askeri kale. 'İntihar Zindanı'nda hapsedilenlerin umutsuzluğu taşlara öyle bir kazınmıştır ki; karanlık koridorlarda dolaşırken boğazınızda fiziksel bir düğüm ve ensenizde dondurucu bir nefes hissedersiniz.",5"Presbítero Maestro Mezarlığı","Lima","Peru","Peru'nun en eski anıt mezarlığı olan ve 'Kara Büyü' (Brujería) ritüelleri için geceleri gizlice kullanılan bu gotik nekropol. Zifiri karanlık çöktüğünde mermer lahitlerin arasından yükselen Santería dualarının yarattığı o karanlık astral vortex, arafta kalan sayısız ruhu buraya zincirlemiştir.",4"Gran Hotel Bolívar","Lima","Peru","1920'lerin ihtişamını yansıtan ama sayısız cinayet ve açıklanamayan intihar vakası yüzünden bazı katları tamamen mühürlenmiş olan efsanevi otel. Boş koridorlarında yankılanan 1920'lerin müzikleri ve asansörlerde beliren solgun yüzler; buranın zaman döngüsünde sıkışmış bir ölüm tuzağı olduğunu fısıldar.",4"Q'enqo İnka Tapınağı","Cusco","Peru","İnkaların yeraltı tanrılarına (Pachamama'nın karanlık yüzüne) kanlı kurbanlar sunduğu ve mumyalama işlemlerini yaptığı devasa, mağara içi bir labirent. Taş sunakların üzerinde durduğunuzda, yüzyıllar öncesinin o sert, kurban edilenlerin acısıyla beslenen şamanik enerjisi zihninizi sarsarak ilkel korkularınızı uyandırır.",4"La Casa Encantada","Lunahuaná","Peru","Pasifik Savaşı sırasında Şilili askerlerin yerel bir aileyi vahşice katlederek ele geçirdiği bu izole, lanetli çiftlik evi. Harap halindeki evin ahşap zemininden yükselen ayak sesleri ve o dönemin şiddet dolu işgal frekansı, evin içine adım atan herkesi şiddetli baş ağrılarıyla dışarı kusar.",4"Marcahuasi (Gizemli Taşlar Ormanı)","Huarochirí","Peru","And Dağları'nın 4000 metre yüksekliğinde, devasa yüzlere benzeyen tuhaf kaya oluşumlarıyla dolu bu manyetik bölge. UFO ve boyutlararası kapı (portal) efsanelerinin merkezi olan bu platoda geceler, insan algısını büken aşırı yoğun frekanslarla doludur; burada doğaüstü olan tamamen fizikselleşir.",5"Amazon Belen Cüzzam Kolonisi Harabeleri","Iquitos","Peru","Ormanın derinliklerinde, cüzzam hastalarının toplumdan izole edilip yavaş yavaş çürüyerek ölmeye terk edildiği bu eski yerleşke. Amazon'un yutucu ve nemli karanlığında dolaşırken ağaçların arasından süzülen bedensiz iniltiler ve o ağır, sülfürik hastalık enerjisi, insanı derinden zehirleyen bir korku yaratır.",4"""

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

print("Peru kayitlari eklendi.")
