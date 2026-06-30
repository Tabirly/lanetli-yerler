import csv
import re
import io

data = """"Ogrodzieniec Kalesi","Silezya","Polonya","Tarihin en büyük büyücülerinden biri olan ve ruhunu şeytana sattığına inanılan soylu Stanislaw Warszycki'nin mekanı. Dolunay gecelerinde kalenin harabelerinde beliren ve boynunda alevli bir zincir taşıyan devasa 'Kara Köpek'in yarattığı o cehennemvari, sülfürik frekans aklınızı başınızdan alır.",5"Reszel Kalesi (Cadı Zindanları)","Warmia-Masuria","Polonya","1811 yılında Avrupa'da yasal olarak yakılan son cadı olan Barbara Zdunk'un hapsedildiği ve işkence gördüğü bu ağır taş kale. Zindanların karanlık dehlizlerinde yankılanan yanık et kokusu ve haksız yere alevlere atılan bir kadının o saf, ilkel öfkesi; buranın aurasını kalıcı olarak zehirlemiştir.",5"Krzywy Las (Çarpık Orman)","Gryfino","Polonya","Ağaçların gövdelerinin doğaya aykırı bir şekilde, adeta acı çekercesine 90 derece büküldüğü bu son derece tekinsiz çam ormanı. Ormanın derinliklerine girdiğinizde aniden kesilen kuş sesleri ve cihazların enerjisini emen o devasa, sessiz ve boyutsal (astral) anomali frekansı sizi derinden huzursuz eder.",4"Dunajec Kalesi (Niedzica)","Küçük Polonya","Polonya","İnka prensesi Umina'nın, İspanyol suikastçiler tarafından hançerlenerek öldürüldüğü bu sarp uçurum kalesi. Geceleri kalede dolaşan ve hala kayıp İnka altınını arayan 'Beyazlı İnka Prensesi'nin hayaleti ile yüzyılların ihanet enerjisi, taş duvarların arasında ağır bir keder girdabı oluşturur.",4"Czocha Kalesi","Aşağı Silezya","Polonya","İkinci Dünya Savaşı sırasında Nazi okült (kara büyü) birimlerinin gizli deneyler yaptığı bu devasa ve gotik şato. Kalenin gizli geçitlerinde ve yeraltı mahzenlerinde hala aktif olan o karanlık, ritüelistik enerji ve duvarların arkasından gelen boğuk iniltiler, buranın şeytani bir kapı olduğunu fısıldar.",5"Krzyżtopór Şatosu Harabeleri","Świętokrzyskie","Polonya","Okült sembolizm ve astrolojiye göre kusursuzca inşa edilen ancak savaşlarda yerle bir olan devasa saray harabesi. Duvarlarındaki gizli kabalistik mühürlerin yaydığı o ağır, ezoterik çekim gücü ve geceleri harabelerde beliren siyahlı şövalyenin yarattığı psişik baskı, en deneyimli ruhları bile ürkütür.",4"Zofiówka Sanatoryumu","Otwock","Polonya","İkinci Dünya Savaşı'nda Nazilerin Lebensborn programı ve acımasız ötanazi (T4) cinayetleri için kullandığı bu terk edilmiş psikiyatri hastanesi. Yıkık koğuşlarda yankılanan ve aniden zihninize saplanan çaresizlik çığlıkları ile buraya hapsolmuş masum ruhların yaydığı o ezici ölümcül anksiyete, insanı nefessiz bırakır.",5"Babia Góra (Cadılar Dağı)","Beskids","Polonya","Polonya mitolojisinde cadıların Şabat (Sabbath) için toplandığı ve etrafında açıklanamayan uçak kazalarının yaşandığı bu uğursuz zirve. Dağa tırmanırken aniden düşen sıcaklık, sisin içinden size doğru fısıldayan görünmez varlıklar ve o ilkel (primal), kaotik pagan enerjisi iradenizi felç eder.",4"Wieliczka Tuz Madeni (Mühürlü Katmanlar)","Wieliczka","Polonya","Turistik alanların çok altındaki, zifiri karanlık ve terkedilmiş derin dehlizlerde yer alan bu devasa yeraltı labirenti. Işığın asla ulaşmadığı o klostrofobik derinliklerde, maden göçüklerinde can veren işçilerin feryatları ve yeraltı elementallerinin (Skarbnik) insanı deliliğe sürükleyen hipnotik fısıltıları yankılanır.",4"Kórnik Şatosu","Büyük Polonya","Polonya","Beyaz bir elbise içinde asırlardır portresinden çıkarak kalede dolaştığına inanılan 'Beyaz Leydi' Teofila'nın mekanı. Kış geceleri şatonun bahçesinde ona eşlik eden meçhul bir siyah atlının toynak sesleri ve havada asılı kalan o saplantılı, aristokratik ölüm frekansı; buradaki zamanı adeta dondurmuştur.",3"""

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

print("Polonya kayitlari eklendi.")
