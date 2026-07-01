import csv
import re
import io

data = """"Karosta Hapishanesi","Liepaja","Letonya","Çarlık Rusyası ve sonrasında KGB tarafından askeri disiplin cezaevi olarak kullanılan, infazların duvarlarında kurşun delikleri bıraktığı o acımasız ve dondurucu bina. Hücrelerin buz gibi beton zeminlerinde yankılanan asker postallarının sesi ve işkence gören mahkumların yalıtılmış kederi ruhunuzu adeta ezer.",5"KGB Binası (Köşe Ev / Stūra Māja)","Riga","Letonya","Sovyet işgali boyunca on binlerce Letonyalının sorgulandığı, işkence gördüğü ve bodrum katında gizlice infaz edildiği o korkunç 'Köşe Ev'. Kana bulanmış zifiri karanlık hücrelerine indiğinizde, devlet terörünün taşlara mühürlediği o saf ve ezici paranoya frekansı nefesinizi tamamen keser.",5"Pokaiņi Ormanı","Kurzeme","Letonya","Eski Baltık paganlarının ve şamanlarının ritüel yaptığı, devasa yosunlu taş kümeleriyle dolu bu gizemli, yoğun orman. Puslu ağaçların arasında pusula ibrelerinin çıldırdığı bu bölgede gezinirken, doğanın ve kadim şamanların yaydığı o ağır elementer büyü enerjisi sizi tamamen transa çeker.",4"Rundale Sarayı (Beyaz Leydi)","Pilsrundale","Letonya","18. yüzyıldan kalma devasa Barok saray, ancak ihtişamının ardında karanlık intiharları ve gizli cinayetleri barındıran soğuk koridorlara sahip. Geceleri balo salonunun dev aynalarından yansıyan 'Beyaz Leydi'nin silüeti ve keman sesleriyle havaya asılı kalan o aristokrat kederi zihninizi daraltır.",4"Sigulda Kalesi Harabeleri","Sigulda","Letonya","Livonyalı Şövalyeler tarafından inşa edilen ve yüzyıllarca İsveç-Polonya savaşlarında kanla yıkanan Gauja nehri vadisindeki bu gotik harabeler. Sisli gecelerde vadiden yukarı tırmanan ağır çelik zırh sesleri ve kılıçtan geçirilen paganların attığı son feryatlar auranızı sarsar.",4"Ebu Selim Hapishanesi","Trablus","Libya","Kaddafi rejimi sırasında 1996 yılında sadece bir gecede 1200'den fazla siyasi mahkumun vahşice kurşuna dizildiği o dehşet verici zindan. Avlusundaki kumların altına gömülü o devasa katliam travması ve duvarlardan sızan kan dondurucu toplu çaresizlik feryadı insanın aurasını paramparça eder.",5"Leptis Magna Antik Harabeleri","Khoms","Libya","Roma İmparatorluğu'nun Afrika'daki en görkemli şehri olan ancak asırlar boyunca depremler, salgınlar ve çöl kumlarıyla yutulan bu devasa antik metropol. Geceleri amfitiyatroda esen çöl rüzgarı, gladyatörlerin ölüm çığlıklarını ve pagan ritüellerinin o ağır, hipnotik kadim frekansını günümüze taşır.",4"Kaddafi'nin Terk Edilmiş Sarayları","Sirte","Libya","Diktatörlüğün son günlerinde NATO bombardımanıyla enkaza çevrilen ve sonrasında isyancılar tarafından yağmalanan devasa, betonarme saray harabeleri. Yıkık, kurşun deşikli koridorlarda yürürken, kanlı devrimin yaydığı o taze şiddet enerjisi ve sönen bir diktatörlüğün ağır, melankolik frekansı ruhunuza yapışır.",5"Cyrene (Şahat) Antik Mezarlıkları","Şahat","Libya","Eski Yunanlılar tarafından kurulan bu görkemli kentin etrafını saran binlerce devasa kaya mezarının bulunduğu 'Ölüler Şehri' (Nekropol). Issız vadide yeraltına doğru uzanan bu karanlık mezarlara indiğinizde, asırlık Helenistik kederi ve ölüm tanrılarına sunulan kadim adakların çekim gücünü hissedersiniz.",4"Sahra Çölü İkinci Dünya Savaşı Batıkları","Kufra Çölü","Libya","İkinci Dünya Savaşı sırasında yönlerini kaybedip uçsuz bucaksız Libya çölünde kavrularak can veren askerlerin ve uçak enkazlarının (örn: Lady Be Good) bulunduğu ölüm rotası. Oksijensiz sıcağın altında kavrulan metal enkazlarından yükselen o mutlak, sonsuz yalnızlık frekansı ve çöl cinlerinin fısıltısı insanı delirtir.",5"""

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

print("Letonya ve Libya kayitlari eklendi.")
