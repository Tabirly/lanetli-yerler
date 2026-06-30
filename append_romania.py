import csv
import re
import io

data = """"Hoia Baciu Ormanı (Transilvanya'nın Bermuda Şeytan Üçgeni)","Kaloşvar (Cluj-Napoca)","Romanya","Ağaçların kemik gibi büküldüğü, zamanın kaybolduğu ve girenlerin açıklanamaz yanıklarla dışarı kustuğu bu devasa kara orman. Merkeze yaklaştıkça oksijenin çekildiğini hissettiren o ağır, boyutsal (astral) anomali frekansı ve sizi izleyen görünmez 'Gözcüler', aklınızın sınırlarını zorlar.",5"Bran Kalesi (Drakula'nın Şatosu)","Braşov","Romanya","Vlad Tepeş (Kazıklı Voyvoda) efsanesiyle özdeşleşen, sarp kayalıkların üzerine tünemiş bu devasa gotik kale. Geceleri Karpat dağlarından esen dondurucu rüzgarın şatodaki dar, klostrofobik geçitlerden geçerken çıkardığı kurt ulumasını andıran o vampirik ve kanlı ölüm frekansı kalbinizi dondurur.",5"Corvin Kalesi (Hunyadi Şatosu)","Hunedoara","Romanya","Vlad Tepeş'in yıllarca hapsedildiği ve delirdiği iddia edilen, Avrupa'nın en karanlık Orta Çağ kalelerinden biri. Zindanlarında işkenceyle can veren esirlerin feryatları ve taş duvarların arasından sızan o sülfürik, şeytani öfke enerjisi; buranın hala kurban arayan bir astral tuzak olduğunu gösterir.",5"Poenari Kalesi (Gerçek Drakula Kalesi)","Argeş","Romanya","Binlerce esirin elleriyle sarp bir dağın zirvesine inşa ettiği, Vlad Tepeş'in gerçek ve en erişilmez kalesi. Uçurumun kenarında durduğunuzda, intihar ederek kendini aşağı atan Vlad'ın eşinin o trajik çığlığı ve dağın zirvesine mühürlenmiş o saf, kana susamış askeri enerji auranızı ezer.",5"Balta Vrăjitoarelor (Cadılar Gölü)","Boldeşti-Scăeni","Romanya","Hayvanların asla su içmediği, etrafında tek bir canlının yaşamadığı ve dibi olmadığı söylenen bu zifiri karanlık orman göleti. Cadıların asırlardır ritüel yaptığı bu lanetli suda oluşan devasa manyetik vortex ve suyun sizi içine çekmeye çalışan o hipnotik karanlık frekansı iradenizi felç eder.",5"Iulia Hasdeu Şatosu","Câmpina","Romanya","Kızını kaybeden kederli bir babanın, onun ruhuyla iletişim kurmak için tamamen okült (büyüsel) ve spiritüalistik yasalara göre inşa ettiği bu tuhaf şato. Geceleri boş odalarda yankılanan piyano sesleri ve babanın yıllar süren seanslarının yarattığı o yoğun, saplantılı ölüm ötesi iletişim enerjisi havayı ağırlaştırır.",4"Banffy Kalesi","Bonţida","Romanya","Transilvanya'nın 'Versay'ı olarak bilinen ancak savaşlarda yıkılıp Alman hastanesi olarak kullanılan bu lanetli saray. Geceleri harabelerde yankılanan meçhul ayak sesleri ve acı içinde can veren askerlerin duvarlara sinmiş o kaotik ölüm travması; şatonun aurasını kalıcı bir kedere boğmuştur.",4"Chiajna Manastırı Harabeleri","Bükreş","Romanya","18. yüzyılda inşa edilen ancak veba salgını yüzünden hiçbir zaman kutsanamayıp terk edilen bu devasa tuğla harabesi. Veba kurbanlarının toplu mezarı haline gelen bu tapınakta yankılanan devasa çan sesleri (çanı olmamasına rağmen) ve o ağır, sülfürik hastalık enerjisi ziyaretçileri boğar.",4"Rasnov Kalesi","Braşov","Romanya","Karpatların eteklerinde, barbar saldırılarından korunmak için bir dağın zirvesine inşa edilen köylü kalesi. Kalenin merkezinde esir Türk askerlerine kazdırılan ve yıllar süren çaresizliğin sonunda infaz edilen esirlerin feryatlarını barındıran o derin kuyu; saf ve yoğun bir karanlık frekans yayar.",4"Parlamento Sarayı Yeraltı Tünelleri","Bükreş","Romanya","Çavuşesku'nun paranoyasıyla inşa edilen, dünyanın en ağır binasının altındaki o devasa, ışıksız yeraltı şehri. İnşaat sırasında can veren binlerce işçinin duvarların içine gizlenmiş cesetleri ve o megalomanik diktatörlüğün yarattığı boğucu, klostrofobik güç enerjisi ruhunuzu bir mengene gibi sıkar.",5"""

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

print("Romanya kayitlari eklendi.")
