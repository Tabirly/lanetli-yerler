import csv
import re
import io

data = """"Predjama Şatosu","Postojna","Slovenya","Dünyanın en büyük mağara şatosu olan ve sarp bir uçurumun içine oyulan bu efsanevi yapı. 15. yüzyılda kalede kuşatılan ve tuvaletteyken gülleyle vurularak öldürülen zalim baron Erazem'in hayaleti; mağaranın rutubetli dehlizlerinde yankılanan kılıç sesleri ve o derin, yeraltı izolasyonunun getirdiği ezici basınçla ziyaretçileri dehşete düşürür.",5"Bogenšperk Kalesi","Šmartno pri Litiji","Slovenya","17. yüzyılda ünlü bir bilim adamı ve büyücü olan Johann Weikhard von Valvasor'un okült deneyler yaptığı bu devasa Orta Çağ kalesi. Kalenin gizli mahzenlerinde yapılan kadim simya ritüellerinin bıraktığı o ağır, sülfürik büyü frekansı; gece yarısı kütüphane koridorlarında beliren gölgelerle birleşerek zihninizi sarsar.",4"Celje Eski Kalesi (Stari Grad)","Celje","Slovenya","Slovenya'nın en büyük kalelerinden biri olan ve trajik aşk cinayetleriyle lanetlenmiş sarp harabe. Zehirlenerek öldürülen güzel Veronika'nın çaresiz çığlıkları kış gecelerinde surlarda yankılanırken; kalenin kanlı tarihine kazınmış o saplantılı ve ihanet dolu dişil enerji empatları anında gözyaşlarına boğar.",4"Hrastovec Şatosu","Lenart","Slovenya","Bir zamanlar Avrupa'nın en acımasız cadı mahkemelerine ev sahipliği yapmış ve sonrasında akıl hastanesi olarak kullanılmış bu karanlık şato. İşkenceyle yakılan cadıların o saf, ilkel öfkesi ile hastaların histerik deliliği birleşerek; şatonun aurasını insan iradesini büken, devasa ve kaotik bir siyah vortex'e dönüştürmüştür.",5"Teharje Toplama Kampı Bölgesi","Celje","Slovenya","İkinci Dünya Savaşı sonrası binlerce insanın yargısız infazla kurşuna dizilip toplu mezarlara gömüldüğü bu kanlı arazi. Toprağın altında yatan ihanetin ve toplu ölüm korkusunun yarattığı o ağır, çürümüş enerji, alana adım atanların göğsüne kurşun gibi oturarak devasa bir anksiyete atağına sebep olur.",5"Ptuj Şatosu","Ptuj","Slovenya","Slovenya'nın en eski şehri Ptuj'da bulunan ve antik Roma ritüellerinden bu yana pagan enerjiler taşıyan kale. Duvarların ardında işkence gören Osmanlı esirlerinin ve Orta Çağ mahkumlarının o boğuk, klostrofobik iniltileri; kalenin asırlık silah deposunda aniden düşen sıcaklıkla birlikte bedeninizi dondurur.",4"Ljubljana Kalesi Zindanları","Ljubljana","Slovenya","Şehre tepeden bakan, yüzyıllar boyunca hapishane ve işkence merkezi olarak kullanılan bu tarihi sembol. Yerin altındaki zifiri karanlık hücrelerde yıllarca ışık görmeden çürüyen esirlerin o ağır, melankolik delilik frekansı ve taşlardan sızan rutubetli ölüm kokusu nefesinizi keser.",4"Rihemberk Kalesi (Branik)","Nova Gorica","Slovenya","Vadiye hakim bir tepede yükselen, İkinci Dünya Savaşı'nda partizanlar tarafından kısmen havaya uçurulmuş bu heybetli harabe. Kalenin yıkık avlusunda dolaşan 'Beyazlı Kadın'ın kederli silüeti ve savaşın yarattığı o ani, travmatik yıkım enerjisi; buranın zaman çizgisinde bir yırtık oluşturduğunu hissettirir.",4"Štanjel Kalesi","Komen","Slovenya","Karst bölgesinin sarp tepelerinde yer alan ve savaşların yıkıcı aurasını taşıyan bu gotik yerleşke. Gece rüzgarlarının taş sokaklarda çıkardığı uğultu, asırlar önce vebadan ve savaştan kırılan köylülerin feryatlarını taklit ederek; arafta kalmış o ağır çaresizlik frekansını doğrudan ruhunuza fısıldar.",3"Kamen Kalesi Harabeleri","Begunje na Gorenjskem","Slovenya","Alplerin sarp bir geçidini koruyan ve 18. yüzyılda terk edilerek ormanın merhametine bırakılan bu yalnız kale. Sisli kış günlerinde kalenin devasa taş duvarları arasında esen dondurucu rüzgar ve o mutlak, yutucu ıssızlık; doğa elementallerinin burayı insanlardan kalıcı olarak geri aldığını gösterir.",4"""

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

print("Slovenya kayitlari eklendi.")
