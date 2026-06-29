import csv
import io

raw_data = """
"Borgvattnet Rahip Evi","Jämtland","İsveç","İsveç'in en bilinen perili evlerinden biri. Ahşap koridorlarında yürürken görünmez varlıkların sizi ittiğini, eşyaların şiddetle fırlatıldığını ve çaresizce ağlayan kadınların seslerini duyarsınız. Buradaki poltergeist enerjisi o kadar agresiftir ki, geceyi burada geçirenlerin aurası adeta fiziksel bir dayak yemiş gibi tükenir.",5
"Frammegården Cadı Evi","Värmland","İsveç","Karanlık ormanların ortasında, cadı avı döneminde yakılan kadınların infaz alanına kurulan bu lanetli ahşap çiftlik. Odalarında yatarken üzerinize çöken o ezici uyku felci (karabasan) hissi ve tavan arasında bitmek bilmeyen o ağır, bedensiz ayak sesleri, toprağın intikam frekansını iliklerinize kadar işletir.",5
"Stortorget (Kan Banyosu Meydanı)","Stockholm","İsveç","1520'deki 'Stockholm Kan Banyosu'nda 82 soylunun başının kesildiği ve kanların sokaklardan nehir gibi aktığı tarihi meydan. Kasım aylarında yağmur yağdığında parke taşlarından kan sızdığı efsanesi anlatılır; meydanın ortasında durduğunuzda yüzlerce yıllık ihanetin ve o paslı, metalik ölüm frekansının göğsünüze oturduğunu hissedersiniz.",4
"Toftaholm Malikanesi","Småland","İsveç","Baronun kızına aşık olan ama kavuşamayacağını anlayınca kendini malikanenin kirişine asan genç Mats'ın melankolik ruhu burayı hiç terk etmemiştir. Gece yarısı kendiliğinden açılan ağır meşe kapılar ve koridorlarda esen o dondurucu, kederli rüzgar, ziyaretçilerin kalbini tarifsiz bir hüzünle sıkar.",4
"Spökslottet (Hayalet Sarayı)","Stockholm","İsveç","Eski sahibi Jacob Knigge'nin şeytanın sürdüğü bir kara arabaya binip kaybolduğuna inanılan, şeytani sembollerle dolu lanetli saray. Aynaların kırıldığı, duvarların içinden müzik seslerinin ve histerik kahkahaların yükseldiği bu yapının aurası, aklın sınırlarını zorlayan yoğun bir okült delilik enerjisi yayar.",5
"Glimmingehus Kalesi","Skåne","İsveç","İskandinavya'nın en iyi korunmuş ama en karanlık Orta Çağ kalelerinden biri. Zifiri karanlık zindanlarından gelen zincir şakırtıları ve kalenin etrafında devriye gezen devasa, kırmızı gözlü cehennem köpekleri (Barghest) efsanesi. Kalenin kalın taş duvarları, savaşın ve izolasyonun o ilkel ve vahşi frekansını hapseder.",4
"Kymlinge Metro İstasyonu","Stockholm","İsveç","İsveç şehir efsanelerinin zirvesi: 'Silverpilen' (Gümüş Ok) adlı hayalet trenin son durağı. Asla tamamlanmamış bu karanlık yeraltı istasyonu için 'Sadece ölüler Kymlinge'de iner' denir. Boş peronlarda yankılanan tren sesleri ve karanlığın içinden size donuk gözlerle bakan yolcu silüetleri, tam bir boyutsal kayboluş hissi yaratır.",5
"Nidingen Feneri","Halland","İsveç","İsveç'in en ölümcül resiflerinin ortasında, binlerce denizcinin sulara gömüldüğü kayalıklarda yükselen izole fener. Fırtınalı gecelerde Kuzey Denizi'nin acımasız dalgalarına karışan boğulma çığlıkları ve ıslak, bedensiz varlıkların kule merdivenlerindeki ağır ayak sesleri; suyun o yutucu, karanlık enerjisini auranıza kazır.",4
"Lund Katedrali Mahzeni","Skåne","İsveç","Yüzlerce yıllık bu devasa katedralin, zifiri karanlık ve buz gibi soğuk olan alt mahzenleri (kripta). Dev Finn efsanesiyle bilinen taş sütunların arasında yürürken, arkanızda sürekli sizi izleyen kadim bir gölgenin varlığını hissedersiniz; buradaki o ağır, ezici dini/gotik frekans nefes almayı bile zorlaştırır.",3
"Häringe Slott (Häringe Şatosu)","Södermanland","İsveç","Karanlık mahzenlerinde asırlar önce duvarlara canlı canlı örülen bir keşişin iniltilerinin duyulduğu aristokratik şato. Odalarda aniden düşen sıcaklık ve gece yarısı koridorlarda beliren 400 yıllık bir çocuğun bedensiz silüeti, şatonun zaman çizgisini sonsuz bir yas döngüsüne kilitlemiştir.",4
"""

reader = csv.reader(io.StringIO(raw_data.strip()))

with open('perili_mekanlar.csv', 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for row in reader:
        if row:
            row.append("")
            writer.writerow(row)

print("İsveç verileri başarıyla eklendi.")
