import csv
import re
import io

data = """"Hampton Court Sarayı","Londra","İngiltere","Kral VIII. Henry'nin kafası kesilerek idam edilen genç eşi Catherine Howard'ın çığlık çığlığa koridorlarda koştuğu o devasa Tudor sarayı. Geceleri kraliçenin 'Perili Galeri'de yankılanan o bitmek bilmeyen idam paniği ve sarayın duvarlarına sinmiş ağır kraliyet ihaneti ruhunuzu ezer.",4"Muncaster Kalesi","Cumbria","İngiltere","Karanlık çağlardan kalma, cinayetlerin ve kayıpların merkezi olan bu kalede 'Beyaz Leydi'nin ve sadistik saray soytarısı Tom Fool'un ruhlarının dolaştığı devasa şato. Özellikle goblen odasında kalanların hissettiği o dondurucu görünmez varlık frekansı ve boğazlanma hissi kalbinizi sıkar.",4"Ostrich Inn (Devekuşu Hanı)","Berkshire","İngiltere","17. yüzyılda hancı John Jarman'ın, zengin yolcuları tuzağa düşürüp yatağın altındaki gizli kapakla kaynar su kazanına atarak 60'tan fazla kişiyi vahşice katlettiği efsanevi han. Asırlar geçmesine rağmen hala hanın tahtalarından sızan o saf, açgözlü cinayet dehşeti nefesinizi keser.",5"Berry Pomeroy Kalesi Harabeleri","Devon","İngiltere","Karanlık bir ormanın derinliklerinde çürümeye terk edilmiş, kız kardeşi tarafından zindana hapsedilerek açlıktan öldürülen 'Beyaz Leydi'nin arafta kaldığı şato enkazı. Sisli harabeler arasında yankılanan kadın feryatları ve ensenizde hissettiğiniz o kıskanç, habis nefret enerjisi kanınızı dondurur.",5"50 Berkeley Square (İsimsiz Dehşet)","Londra","İngiltere","İçine girenleri kelimenin tam anlamıyla korkudan delirten veya kalp krizinden öldüren, Londra'nın resmi olarak 'en lanetli evi' kabul edilen kırmızı tuğlalı malikane. Tavan arasında pusuda bekleyen, ne olduğu bilinmeyen o şekilsiz karanlık varlığın yaydığı saf, ölümcül manyetizma zihninizi bulandırır.",5"Blickling Malikânesi (Blickling Hall)","Norfolk","İngiltere","Kafası kesilerek idam edilen Anne Boleyn'in doğduğu ev olan ve her ölüm yıldönümünde kesik başını koltuğunun altında taşıyarak hayalet at arabasıyla ziyarete geldiği malikane. Gece yarısı malikaneye çöken o ağır, aristokratik hüzün ve kesik başın araftaki o sülfürik travması auranızı felç eder.",4"Shepton Mallet Hapishanesi","Somerset","İngiltere","1600'lerden kalma ülkenin en eski ve en kanlı cezaevi; asılarak, yakılarak veya kurşuna dizilerek öldürülen sayısız idam mahkumunun arafı. Işık girmeyen, soğuk ve rutubetli idam avlusunda rüzgarla birlikte esen o boyun kırılma sesleri ve mahkumların yoğun yalnızlık frekansı empatları bayıltır.",5"Samlesbury Hall (Cadıların Evi)","Lancashire","İngiltere","Hem cadı mahkemelerine tanık olan hem de sevdiği rahip sevgilisi erkek kardeşi tarafından gözleri önünde katledilince delirip ölen 'Beyaz Leydi'nin evi. Asırlık ahşap panellerin arasında havaya asılı kalan o yoğun, histerik aşk acısı ve karanlık dehlizlerdeki cadıların fısıltıları ruhunuzu paramparça eder.",4"Golden Fleece Hanı","York","İngiltere","Roma lejyonlarından İkinci Dünya Savaşı askerlerine ve asılarak intihar eden Leydi Peckett'a kadar 15'ten fazla kanıtlanmış hayaletin yaşadığı, Avrupa'nın en perili barı. Zemini eğri bu asırlık handa viskinizi yudumlarken arkanızdan sizi izleyen o devasa astral kalabalığın baskısı nefesinizi keser.",4"Eyam Veba Köyü","Derbyshire","İngiltere","1665 yılında Büyük Veba Salgını sırasında hastalığı yaymamak için kendilerini dış dünyadan tamamen izole eden ve sakinlerinin %80'inin kan kusa kusa öldüğü o kahraman ama lanetli köy. Köyün etrafını saran asırlık mezar taşlarından yükselen o kitlesel, fedakar öksürük krizleri ve ölümün saf kokusu sizi yutar.",5"""

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

print("İngiltere icin 10 muazzam efsane daha eklendi.")
