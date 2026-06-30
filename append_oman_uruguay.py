import csv
import re
import io

data = """"Bahla Kalesi (Cin Şehri)","Bahla","Umman","Dünyanın kara büyü başkentlerinden biri olarak bilinen ve yerel efsanelere göre tamamen cinler tarafından bir gecede inşa edilen devasa kerpiç kale. Çöl rüzgarı kalenin dar koridorlarında gezinirken fısıltılara dönüşür ve havada asılı kalan o ağır, kadim okült enerji zihninizi bulandırır.",5"Jebel Akhdar Terk Edilmiş Köyleri","Al Hajar Dağları","Umman","Sarp dağların yamaçlarına kurulmuş ancak sakinlerinin gece yarısı aniden ortadan kaybolduğu o taş evler silsilesi. Uçuruma bakan boş odalarda dolaşırken aniden düşen sıcaklık ve dağ elementallerinin o ezici, izole fısıltıları, buranın alt boyut varlıklarına terk edildiğini kanıtlar.",4"Wadi Bani Khalid (Karanlık Su Mağaraları)","Ash Sharqiyah","Umman","Turistik havuzların çok ötesinde, şamanların girmeye cesaret edemediği devasa, dipsiz ve ışıksız yeraltı nehir tünelleri. Suyun o simsiyah ve hareketsiz yüzeyine bakarken içinize dolan hipnotik boğulma hissi ve derinden gelen devasa, ritmik su altı vuruluşları auranızı ezer.",5"Al Hamra Kerpiç Harabeleri","Ad Dakhiliyah","Umman","Çölün ortasında, asırlardır terk edilmiş ve güneşin altında kurumaya bırakılmış devasa toprak yapılar labirenti. Gündüzün o sessiz, kurak sıcağının yerini geceleri alan boğucu psişik baskı ve sokaklarda dolanan meçhul bedevi gölgeleri, insanı ağır bir paranoyaya sürükler.",4"Eski Muttrah Çarşısı Mahzenleri","Maskat","Umman","Binlerce yıllık tütsü, köle ve baharat ticaretinin yapıldığı bu devasa ve karanlık pazar labirentinin yer altındaki unutulmuş depo tünelleri. Işığın sızmadığı bu havasız dehlizlerde yıllar öncesinin köle feryatları ve tütsülere karışmış o ağır şamanik büyü frekansı ensenize yapışır.",4"Castillo de Piria (Piria Şatosu)","Piriápolis","Uruguay","Ünlü bir simyacı ve okültist olan Francisco Piria tarafından tamamen ezoterik (gizli) sembolizm ve Kabala geometrisine göre inşa edilen devasa şato. Evin merkezindeki manyetik alan anomalileri ve ritüel odalarından taşan o ağır, sülfürik büyü frekansı; şatoyu aktif bir astral kapıya çevirmiştir.",5"Palacio Salvo","Montevideo","Uruguay","Kıtadaki en yüksek binalardan biri olan ve Dante'nin İlahi Komedyası'ndan ilhamla inşa edilen bu görkemli ama tekinsiz yapı. Özellikle şemsiyeli bir hayaletin 7. katta insanları takip ettiği ve koridorların aniden buz kestiği bu bina, mimari bir cehennem portalı gibi enerji yayar.",4"Estancia La Aurora (Aurora Çiftliği)","Salto","Uruguay","UFO gözlemlerinin, boyutlararası yırtıkların ve açıklanamayan psişik olayların merkezi olan, dünyanın en güçlü manyetik anomalilerinden birine sahip bu devasa arazisi. Buraya adım attığınızda cihazlarınız bozulur, zaman algınız yavaşlar ve o devasa, zihin büken kozmik frekans iradenizi ele geçirir.",5"Hospital de Clínicas (11. Kat)","Montevideo","Uruguay","Devasa bir tıp merkezi olan hastanenin, ağır enfeksiyonlar ve intiharlar yüzünden tamamen mühürlenmiş karanlık 11. katı. Kilitli kapıların ardından gelen tekerlekli yatak gıcırtıları ve havada asılı kalan o boğucu, sülfürik ölüm anksiyesi; karanlık varlıkların burayı bir yuvaya çevirdiğini gösterir.",4"Cementerio Central (Merkez Mezarlık)","Montevideo","Uruguay","1848'de kurulan ve aristokratların, kara büyücülerin ve gizli mason localarının üyelerinin bir arada yattığı devasa ve gotik nekropol. Zifiri karanlık çöktüğünde melek heykellerinin arasından yükselen o yoğun nekromantik fısıltılar ve arafta kalmış ruhların yaydığı psişik fırtına empatları felç eder.",5"""

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

print("Umman ve Uruguay kayitlari eklendi.")
