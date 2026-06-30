import csv
import re
import io

data = """"Ebu Gureyb Hapishanesi","Bağdat","Irak","İnsanlık tarihinin en karanlık işkence merkezlerinden biri. Duvarlarına sinen yoğun acı, öfke ve çaresizlik enerjisi; burayı ziyaret edenlerin üzerinde tarifi imkansız bir ağırlık ve görünmez bir baskı hissi bırakır.",5"Babil Harabeleri","Babil","Irak","Mezopotamya'nın kalbi. Kadim kralların lanetli mirasları ve savaşın yıkımı altında kalan bu topraklar, gece çöktüğünde antik ruhların fısıltılarıyla dolar; burada zaman algısı bir anda parçalanır.",4"Ur Zigguratı","Zikar","Irak","Sümerlerin Ay Tanrısı Nanna'ya adanmış bu devasa yapı, insanlığın ilk kadim astral portallarından biridir. Yüzlerce yılın getirdiği o sessiz, görkemli ama bir o kadar da ürkütücü enerji, ziyaretçilerin ruhunu görünmez bir güçle sarsar.",4"Musul (Nineveh) Harabeleri","Musul","Irak","Antik Asur imparatorluğunun başkenti ve savaşın en çok vurduğu noktalardan biri. Antik tarih ile modern yıkımın iç içe geçtiği bu topraklarda, havada asılı kalan o kolektif keder ve barut kokusu ziyaretçiyi adeta boğar.",5"Güney Irak Bataklıkları (Ahwar)","Basra","Irak","İfritlerin ve kadim su cinlerinin (Mared) hüküm sürdüğü bu izole bataklıklar. Geceleri sazlıkların arasından gelen boğuk sesler ve suyun içine çekme eğilimindeki o hipnotik, karanlık enerji; buraya girenlerin ruhunu yavaş yavaş kendi içine hapseder.",4"Taq Kasra (Ctesiphon)","Bağdat (Yakınları)","Irak","Sasani İmparatorluğu'nun devasa kemeri. Zamanın ve savaşların yıktığı bu yapıda, eski Pers krallarının ve savaşçıların ruhları hala nöbet tutmaktadır. Geceleri rüzgarın taşıdığı antik ağıtlar auranızı dondurur.",3"El-Faw Sarayı (Overlook)","Bağdat","Irak","Saddam döneminden kalma, savaşın tüm izlerini taşıyan devasa ve tekinsiz saray. Terk edilmiş koridorlarında dolanan gölgeler ve savaşın aniden kestiği hayatların yarattığı ağır anksiyete, burayı ziyaret edenleri hızla uzaklaşmaya zorlar.",4"Dicle Nehir Kıyısı (Bağdat)","Bağdat","Irak","Nehrin asırlar boyunca aldığı canlar ve kadim efsanelere göre suyun altına çekilen ruhlar. Geceleri Dicle'nin kıyısında duyulan boğuk iniltiler ve suyun o yutucu karanlık frekansı, en deneyimli kişilerin bile zihinsel kalkanlarını zayıflatır.",3"Samarra (Al-Askari Türbesi Çevresi)","Samarra","Irak","Bombalanan ve yıkılan tarihi dokunun ardında, ağır bir travma ve manevi huzursuzluk yatar. Bölge genelinde ziyaretçilerin rapor ettiği ani soğukluklar ve görünmez varlıkların izleme hissi, buradaki astral karantinanın hala devam ettiğini gösterir.",4"Bağdat'ın Terkedilmiş Köşkleri","Bağdat","Irak","Sömürge ve kraliyet döneminden kalma, savaşlar sırasında bir gecede terk edilmiş, içi mobilyalarla dolu köşkler. Hiç dokunulmamış eşyaların arasında esen rüzgar, arafta kalmış eski sakinlerin kederli fısıltılarını taşır.",4"""

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

print("Irak kayitlari eklendi.")
