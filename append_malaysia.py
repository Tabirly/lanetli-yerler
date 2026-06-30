import csv
import re
import io

data = """"Highland Towers (Yıkık Kuleler)","Selangor","Malezya","1993 heyelanında yıkılan ve onlarca kişinin diri diri toprağa gömüldüğü lüks apartman kompleksi. Doğa tarafından yutulan bu beton enkazında dolaşırken, boğularak can verenlerin feryatları ve alt boyut varlıklarının (Pontianak) o ağır, yırtıcı enerjisi auranızı bir mengene gibi sıkar.",5"Penang Savaş Müzesi (Hayalet Tepe)","Penang","Malezya","İkinci Dünya Savaşı'nda Japon ordusunun acımasız bir işkence ve infaz kampına dönüştürdüğü (Bukit Hantu) bu eski kale. Giyotinle baş kesilenlerin ve açlıktan ölen esirlerin o paslı kan frekansı duvarlara öylesine sinmiştir ki, gece karanlığında ensenizde celladın nefesini hissedersiniz.",5"Karak Otoyolu","Pahang","Malezya","Malezya'nın en ölümcül ve şeytani enerjili dağ geçidi. Gece yarısı zifiri karanlıkta sürücülere musallat olan sürücüsüz sarı bir araba ve kayıp çocuk silüetleri; bu yolun aslında doğrudan yeraltı elementallerine ve kana susamış orman cinlerine açılan aktif bir astral portal olduğunu gösterir.",5"Mona Fandey'in Evi (Kara Büyü Evi)","Pahang","Malezya","90'larda bir politikacıyı kara büyü (bomoh) ritüeliyle parçalara ayıran ünlü cadı/şarkıcı Mona Fandey'in lanetli evi. Toprağa sinmiş olan o saf, şeytani (demonic) büyü enerjisi ve evin etrafını saran o saldırgan, dışlayıcı karanlık frekans, içeri girmeye çalışanların aurasını anında bıçaklar.",5"Villa Nabila","Johor Bahru","Malezya","Johor Bahru'da yer alan ve tüm ailenin vahşice katledildiği efsanesiyle bilinen, ormanın yuttuğu bu devasa malikane. Terk edilmiş koridorlarında yürürken, duvarların içinden gelen boğuk çocuk çığlıkları ve aniden cihazların pillerini emen o aç, karanlık zeka zihninizi felç eder.",4"Pudu Hapishanesi (Pudu Jail)","Kuala Lumpur","Malezya","On binlerce azılı suçlunun hapsedildiği, karanlık ve nemli hücrelerinde sayısız infazın gerçekleştirildiği bu devasa beton cehennem. İdam odasının bulunduğu blokta durduğunuzda, boynu kırılan mahkumların o saf nefret ve can havli frekansı göğsünüze kurşun gibi oturur.",5"Kellie'nin Kalesi (Kellie's Castle)","Perak","Malezya","İskoç bir kauçuk baronunun eşi için yaptırdığı ancak salgın hastalıklar ve ani ölümüyle yarım kalan bu gizemli Hint-Gotik şatosu. Zifiri karanlık gizli tünellerinde ve boş salonlarında yankılanan bedensiz ayak sesleri, zamanın o melankolik ölüm anında sonsuz bir döngüye girdiğini fısıldar.",4"First World Hotel (21. Kat)","Pahang","Malezya","Genting Highlands'te bulunan ve kumar borcu yüzünden intihar edenlerin kederiyle zehirlenmiş devasa bir astral araf. Özellikle 21. katın o boğucu koridorlarında asılı kalan ölüm korkusu ve asansör boşluklarından süzülen şekilsiz gölgeler, insanın yaşama sevincini yavaş yavaş emer.",4"Bukit Tunku (Kenny Hills)","Kuala Lumpur","Malezya","Kuala Lumpur'un göbeğinde yer alan ancak devasa ağaçların güneş ışığını engellediği bu elit ama ürkütücü ormanlık bölge. Terk edilmiş lüks konakların boş pencerelerinden sizi izleyen görünmez gözler ve gece yarısı aniden bastıran o dondurucu, boğucu yalnızlık enerjisi zihinsel kalkanlarınızı sarsar.",4"Mimaland Terk Edilmiş Tema Parkı","Selangor","Malezya","Ormanın derinliklerinde, vahşi doğanın ve karanlık orman ruhlarının tamamen geri aldığı bu devasa eski eğlence parkı. Çürüyen dinozor maketlerinin ve boş havuzların arasında dolaşırken, eski kahkahaların yerine doğanın o ilkel, yutucu ve tekinsiz sessizliğinin aklınızı zorladığını hissedersiniz.",3"""

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

print("Malezya kayitlari eklendi.")
