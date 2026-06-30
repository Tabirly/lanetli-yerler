import csv
import re
import io

data = """"Bhangarh Kalesi","Rajasthan","Hindistan","Hindistan'ın yasal olarak gece girilmesi yasaklanan tek yeri. Saplantılı bir kara büyücünün (Tantrik) ölüm döşeğindeki lanetiyle bir gecede harabeye dönen bu antik şehirde; güneş battıktan sonra uyanan o ezici, şeytani frekans ve yıkıntıların arasından gelen bedensiz çığlıklar auranızı paramparça eder.",5"Kuldhara Hayalet Köyü","Rajasthan","Hindistan","Acımasız bir vezirin zulmünden kaçan binlerce köylünün kara bir büyüyle lanetleyerek bir gecede tamamen terk ettiği bu izole yerleşke. Kuruyan kuyuların ve dökülen taş evlerin arasında dolaşırken, toprağa kazınmış o saf öfke ve kimsesizlik enerjisi göğsünüze ağır bir yumru gibi oturur.",5"Dumas Sahili (Cesetler Kumsalı)","Gucerat","Hindistan","Asırlar boyunca binlerce Hindu'nun cesedinin açık ateşte yakıldığı ve küllerinin karıştığı bu kapkara kumlu sahil. Geceleri okyanusun uğultusuna karışan fısıltılar ve aniden etrafınızı saran görünmez varlıkların o ağır, yanık et kokulu astral frekansı ziyaretçileri dehşete düşürür.",5"Shaniwar Wada","Pune","Hindistan","Kendi sarayında, amcasının emriyle suikastçılar tarafından vahşice parçalanarak öldürülen genç prens Narayanrao'nun kanlı mekanı. Dolunaylı gecelerde sarayın bahçesinde 'Amca, beni kurtar!' diye feryat eden o kederli çocuk çığlıkları ve ihanetin havada asılı kalan o paslı enerjisi kalbinizi sızlatır.",4"Dow Hill Ormanları","Kurseong","Hindistan","Himalayaların eteklerinde, zifiri bir sisin içine hapsolmuş bu ormanlık alan ve Viktorya dönemi okulları. Yüksek intihar oranlarıyla bilinen ormanın derinliklerinde dolaşan başsız bir çocuğun silüeti ve ağaçların sizi izlediğini hissettiren o ilkel, yutucu doğa enerjisi iradenizi felç eder.",4"Agrasen Ki Baoli","Yeni Delhi","Hindistan","Yerin metrelerce altına inen, yüzlerce asırlık basamağıyla bu devasa ve klostrofobik su kuyusu. Efsaneye göre kuyunun dibindeki zifiri 'siyah su', zayıf zihinleri hipnotize ederek intihara çağırırdı; merdivenlerden aşağı indikçe o boğucu ve karanlık çekim kuvvetinin auranızı emdiğini fiziksel olarak hissedersiniz.",4"Mukesh Mills (Terk Edilmiş Fabrika)","Mumbai","Hindistan","1980'lerde feci bir yangınla tamamen kül olan ve bir daha asla açılamayan devasa tekstil fabrikası. İçeride yanarak can veren işçilerin o kaotik ölüm korkusu duvarlara sinmiştir; çekim yapmak için buraya gelen ekiplerin aniden ele geçirilme (possession) vakaları yaşaması, buranın şeytani bir portala dönüştüğünü gösterir.",5"Güney Park Sokağı Mezarlığı","Kalküta","Hindistan","Şehrin kalabalığının ortasında, tropik bitkilerin ve sarmaşıkların yuttuğu devasa piramit ve gotik anıt mezarlarla dolu bu İngiliz sömürge mezarlığı. Tropik sıtmadan ve savaşlardan kırılan aristokratların yattığı bu alanda, gece bastırdığında heykellerin arasından süzülen o koyu, kederli sömürge frekansı zihninizi bulandırır.",4"Sanjay Van Ormanı","Yeni Delhi","Hindistan","Metropolün göbeğinde yer alan ama güneş battığı anda devasa bir astral mezarlığa dönüşen bu zifiri orman. İçinde eski Sufi azizlerinin türbeleri bulunan bu alanda, ağaçların arasından süzülen beyaz giyimli kadınların ve aniden düşen sıcaklığın yarattığı o ağır boyutsal enerji, ziyaretçileri panik içinde kaçırtır.",4"Lothian Mezarlığı","Yeni Delhi","Hindistan","Sevdiği kadın tarafından reddedilince kafasına kurşun sıkarak intihar eden İngiliz general Sir Nicholas'ın başsız ruhunun dolaştığı, 200 yıllık bu harabe mezarlık. Asırlık ağaçların kökleriyle parçalanmış mezar taşlarının arasında, aşkın ve ölümün o saplantılı, kanlı frekansı arafta kalmış ruhların ağıtlarına karışır.",4"""

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

print("Hindistan kayitlari eklendi.")
