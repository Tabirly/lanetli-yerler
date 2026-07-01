import csv
import re
import io

data = """"Vila Algarve (PIDE Gizli Polis Zindanları)","Maputo","Mozambik","Portekiz sömürge döneminde gizli polis teşkilatının (PIDE) acımasız sorgu ve işkence merkezi olarak kullandığı, şu an çürümeye yüz tutmuş tarihi malikane. Yıkık, fayanslı koridorlarında yankılanan mahkum feryatları ve o kan dondurucu devlet terörü frekansı, binanın duvarlarından adeta zehir gibi sızar.",5"Grande Hotel Beira (Kıyamet Oteli)","Beira","Mozambik","Afrika'nın en lüks otellerinden biri olarak inşa edilen ancak iç savaş sırasında binlerce mültecinin sığındığı, asansör şaftlarının toplu mezarlara dönüştüğü devasa bir beton harabesi. Karanlık ve su basmış dehlizlerinde gezinirken, çaresizliğin ve kitlesel arafın yaydığı o ağır, çürük travma auranızı paramparça eder.",5"Fort São Sebastião Zindanları","Mozambik Adası","Mozambik","Hint Okyanusu'nun en eski Portekiz kalelerinden biri olan ve asırlar boyunca on binlerce Afrikalı kölenin zincirlere vurularak gemilere bindirilmeyi beklediği o karanlık hisar. Işık girmeyen zindanlarda okyanus dalgalarına karışan zincir sesleri ve yalıtılmış köle hüznü nefesinizi tamamen keser.",5"Gorongosa İç Savaş Ormanları","Sofala","Mozambik","Kanlı iç savaş boyunca vahşi hayvanların katledildiği, mayınlarla döşenen ve binlerce isyancının ormanın derinliklerinde can verdiği geniş doğal yaşam alanı. Ağaçların arasında esen rüzgarın taşıdığı o ilkel hayatta kalma anksiyetesi ve toprak altındaki o ağır, sülfürik savaş laneti empatları zehirler.",4"Mozambik Adası Sömürge Harabeleri","Nampula","Mozambik","Asırlar boyunca Arap, Hint ve Portekizli köle tüccarlarının merkezi olan ve günümüzde suların aşındırdığı taş binalardan oluşan bu efsanevi ada. Gece dar sokaklara çöken sise eşlik eden meçhul ağlamalar ve denizin altından gelen o karanlık Voodoo/Muti titreşimleri insanı adeta yutar.",4"Narayanhiti Kraliyet Sarayı (Katliam Odaları)","Katmandu","Nepal","2001 yılında Veliaht Prens'in tüm kraliyet ailesini otomatik silahlarla tarayarak katlettiği ve ardından intihar ettiği o görkemli ama lanetli saray. Katliamın gerçekleştiği salonun yıkılmasına rağmen, araziye tamamen mühürlenmiş o mutlak hanedan dehşeti ve ihanet frekansı zihninizi daraltır.",5"Pashupatinath Ölü Yakma Ghatları","Katmandu","Nepal","Bagmati Nehri'nin kıyısında, binlerce yıldır durmaksızın Hintu cenaze ritüellerinin (ölü yakma) yapıldığı bu devasa ve kutsal tapınak kompleksi. Gece yarısı yükselen ağır insan eti dumanları, yanan ateşlerin çıkardığı çıtırtılar ve etrafa yayılan o devasa, geçiş boyutundaki ruhani manyetizma sizi sarsar.",5"Everest Dağı (Gökkuşağı Vadisi)","Khumbu Bölgesi","Nepal","Dünyanın zirvesinde, 'Ölüm Bölgesi' olarak bilinen ve donarak ölen 200'den fazla dağcının renkli ceketleriyle yattığı, asla çürümeyen bedenlerin olduğu o buzlu cehennem. Oksijensiz 8000 metrede fırtınanın çıkardığı o şeytani ıslık ve donarak ölmenin yaydığı o katıksız, beyaz uyuşukluk hissi ruhunuzu dondurur.",5"Bagh Bhairab Tapınağı","Kirtipur","Nepal","Kaplan formundaki yırtıcı tanrı Bhairab'a adanmış olan ve tapınağın çevresinin kılıçlarla bezendiği bu antik ve kanlı ritüel merkezi. Geceleri kurban edilen hayvanların toprağa işleyen saf, ilkel terörü ve tapınaktan yansıyan o ezici, kaplan gibi vahşi astral enerji auranızı adeta pençeler.",4"Gokarna Şamanik Ormanları","Katmandu Vadisi","Nepal","Eski Hindu ve Budist şamanlarının tantrik ayinler gerçekleştirdiği ve aydınlanma ararken deliren keşişlerin ruhlarının hapsolduğuna inanılan o gizemli ve yoğun orman. Sislerin arasından gelen o boğuk çan sesleri ve ağaç köklerine sinmiş olan o ağır, dünyevi olmayan ezoterik çekim gücü insanı deliliğe sürükler.",4"""

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

print("Mozambik ve Nepal kayitlari eklendi.")
