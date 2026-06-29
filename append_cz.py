import csv
import io

raw_data = """
"Houska Kalesi","Prag (Yakınları)","Çek Cumhuriyeti","Efsaneye göre doğrudan cehenneme açılan dipsiz bir çukuru mühürlemek için inşa edilmiş bu şeytani kale. İkinci Dünya Savaşı'nda Nazilerin karanlık okült deneylerine sahne olan bu yapının altından geceleri kanatlı yaratıkların ve alt boyut varlıklarının duvarları tırmalama sesleri gelir; buradaki aura insanı deliliğin eşiğine getirir.",5
"Sedlec Ossuary (Kemik Kilisesi)","Kutná Hora","Çek Cumhuriyeti","Kara Veba ve savaş kurbanlarından geriye kalan kırk binden fazla insanın kemikleriyle dekore edilmiş bu gotik şapel. Tavandan sarkan kemik avizelerin ve kafataslarından örülmüş duvarların arasında dolaşırken, on binlerce ruhun ölüm enerjisi auranıza yapışır; ölümün o sessiz ve ezici estetiği nefesinizi keser.",5
"Bohnice Psikiyatri Mezarlığı","Prag","Çek Cumhuriyeti","Avrupa'nın en büyük ve en karanlık terk edilmiş tımarhane mezarlığı. Katillerin, delilerin ve intihar edenlerin isimsiz mezarlarına ev sahipliği yapan bu sarmaşık kaplı ormanlık alan, satanik ayinlerin merkezidir. Toprağın altında yatan parçalanmış zihinlerin o kaotik ve ağır anksiyete frekansı, ziyaretçilere fiziksel bir ağırlık olarak çöker.",5
"Špilberk Kalesi Zindanları","Brno","Çek Cumhuriyeti","'Halkların Hapishanesi' olarak bilinen ve Avrupa'nın en ağır işkence merkezlerinden biri olan bu devasa kale zindanı (Kasematlar). Zifiri karanlık hücrelerde zincire vurulan esirlerin o çürümüş ve kırık dökük enerjisi o kadar ağırdır ki, tünellerde ilerlerken oksijenin azaldığını ve karanlığın sizinle nefes aldığını hissedersiniz.",5
"Faust Evi (Faustův dům)","Prag","Çek Cumhuriyeti","Prag'ın kalbinde, yüzyıllar boyunca kara büyücülerin ve simyacıların yaşadığı, şeytanla anlaşmaların yapıldığı efsanevi konak. Duvarlarına sinmiş olan o yoğun simya ve maji enerjisi, binada hala aktif bir okült portalın açık olduğunu gösterir; geceleri boş pencerelerden dışarı sızan tuhaf ışıklar ve fısıltılar insanın aklını zorlar.",4
"Jihlava Yeraltı Dehlizleri","Jihlava","Çek Cumhuriyeti","Avrupa'nın en gizemli yeraltı labirentlerinden biri. Açıklanamayan fosforlu yeşil bir ışık yayan zifiri karanlık koridorlarda yürürken, arkanızdan gelen görünmez ayak sesleri duyarsınız. Yeraltının o boğucu ve izole enerjisi, burada arafta kalmış eski madencilerin ve engizisyon kurbanlarının kederiyle birleşerek sizi yutmak ister.",4
"Zvíkov Kalesi","Güney Bohemya","Çek Cumhuriyeti","Nehirlerin birleştiği noktada yükselen ve Çekya'nın en perili şatolarından biri kabul edilen bu kadim kale. 'Zvíkov'un Şeytanı' olarak bilinen görünmez bir varlığın koridorlarında devriye gezdiği, cihazların anında bozulduğu ve hayvanların girmeyi reddettiği bu alan, son derece agresif ve düşmanca bir frekansa sahiptir.",4
"Daliborka Kulesi (Açlık Zindanı)","Prag","Çek Cumhuriyeti","Prag Kalesi'nin surlarında yer alan ve adını ilk mahkumu Dalibor'dan alan bu korkunç açlık zindanı. Işığın girmediği bu yuvarlak kulede yavaş yavaş açlıktan ölüme terk edilen mahkumların umutsuzluğu taşlara kan gibi işlemiştir. Zindanın dibine baktığınızda, o yavaş ve acı verici ölümün frekansı kalbinizi bir mengene gibi sıkar.",4
"Velhartice Kalesi","Plzeň","Çek Cumhuriyeti","Ölülerin diriltildiği karanlık maji ritüellerine şahitlik etmiş ve Çek folklorunun en korkunç masallarına ilham vermiş bu izole şato. Özellikle avlusunda ve mezarlık bölgesinde hissedilen o devasa negatif enerji alanı (vortex), auranızı anında zayıflatarak sizi derin ve açıklanamaz bir melankoliye sürükler.",4
"Eski Şehir Köprü Kulesi","Prag","Çek Cumhuriyeti","1621'de idam edilen 27 Bohemyalı isyancı soylunun kesik başlarının ibret için yıllarca demir kafeslerde asılı kaldığı bu gotik kule. Karl Köprüsü'nün bu karanlık girişinde, geceleri hala o kanlı infazın öfkesi nabız gibi atar; köprüde esen rüzgara karışan bedensiz iniltiler, intikam arayan aristokrat ruhların enerjisidir.",3
"""

reader = csv.reader(io.StringIO(raw_data.strip()))

with open('perili_mekanlar.csv', 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for row in reader:
        if row:
            row.append("")
            writer.writerow(row)

print("Çek Cumhuriyeti verileri başarıyla eklendi.")
