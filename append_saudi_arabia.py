import csv
import re
import io

data = """"Mada'in Saleh (Hegra - Lanetli Şehir)","Al Ula","Suudi Arabistan","Nebatiler döneminden kalma, devasa kayalara oyulmuş bu antik şehir, İslami inanca göre 'kavmi helak olmuş' lanetli bir bölgedir. Çöl gecelerinde devasa anıt mezarların arasında gezinirken, kayalara sinmiş o mutlak, tanrısal gazap frekansı ve asırlık keder enerjisi auranızı felç eder.",5"Irgah (Erga) Terk Edilmiş Hastanesi","Riyad","Suudi Arabistan","Körfez Savaşı sonrasında devasa ekipmanlarıyla birlikte aniden terk edilen ve çöl kumlarının yuttuğu bu karanlık tıp merkezi. Jeneratörleri kapalı olmasına rağmen koridorlarında yanıp sönen ışıklar ve ameliyathanelerden yükselen görünmez feryatlar, buranın ifritler tarafından ele geçirildiğini gösterir.",5"Wadi Al Jinn (Cinler Vadisi)","Medine","Suudi Arabistan","Yerçekimi kanunlarının işlemediği, araçların yokuş yukarı kendiliğinden tırmandığı ve kompasların çıldırdığı o meşhur, manyetik anomali vadisi. Çölden esen sıcak rüzgarla birlikte dağlardan yankılanan o tuhaf, mekanik olmayan sesler ve havaya asılı kalan cin frekansı zihninizi daraltır.",5"Al Balad'ın Terk Edilmiş Evleri","Cidde","Suudi Arabistan","Kızıldeniz kıyısında, asırlardır tüccarlara ev sahipliği yapmış olan ancak dar ve karanlık sokaklarındaki ahşap cumba evlerin (Roshan) çoğunun cin efsaneleri nedeniyle terk edildiği eski şehir. Oksijensiz labirentlerde gezinirken eski taş duvarlara kazınmış o ağır, dişil bedevi lanetleri ensenizde hissedilir.",4"Masmak Kalesi Zindanları","Riyad","Suudi Arabistan","Arap Yarımadası'nın en kanlı kuşatmalarına ve krallık savaşlarına sahne olan bu devasa kerpiç hisar. Kalenin ışık sızmayan zindanlarına indiğinizde, kılıçtan geçirilen savaşçıların toprağa karışan o saf, metalik öfke frekansı ve kapalı alanda biriken klostrofobik travma kalbinizi sıkar.",4"Jabal Al-Qarah (Karanlık Mağaralar)","Al Ahsa","Suudi Arabistan","Yazın buz gibi serin, kışın ise sıcak olan devasa kireçtaşı labirent mağaraları ağı. Doğal tünellerin güneş görmeyen derinliklerine indikçe, çölün karanlık elementallerinin sizi izlediği hissi ve mağara duvarlarının üzerinize doğru kapandığı o yoğun psişik basınç empatları bayıltır.",4"Qasr Al Farid (Yalnız Saray)","Al Ula","Suudi Arabistan","Çölün ortasında, tek ve devasa bir kayanın içine oyulmuş ancak inşaatı asla tamamlanamamış bu dev mezar. Yüzlerce mil çapındaki ıssızlıkta bu dev anıta yaklaştığınızda hissedilen o ağır, boyutsal yalnızlık frekansı ve yarım kalmış ölüm ritüellerinin enerjisi insanı adeta yutar.",4"Rub' al Khali (Boş Çeyrek Çölü)","Güney Arabistan","Suudi Arabistan","Dünyanın en büyük kesintisiz kum çölü olan, binlerce kervanın ve kaşifin iz bırakmadan kaybolduğu o devasa 'Boşluk'. Zifiri gecelerde devasa kum tepelerinin rüzgarla çıkardığı o boğuk uğultular ve çöl ifritlerinin (Marid) yarattığı serap illüzyonları zihninizi doğrudan deliliğe sürükler.",5"Al Hada Dağları (Taif Geçitleri)","Taif","Suudi Arabistan","Sarp dağların yamaçlarında, uçuruma asılı dolambaçlı yollar ve sisli teleferik hatlarıyla kaplı o izole, tekinsiz geçit. Zirvelerden aşağıya çöken o dondurucu sisin içinde kaybolan eski seyyahların feryatları ve uçurumun hipnotik çekim gücü, burayı devasa bir astral tuzağa çevirir.",4"Tarout Kalesi","Qatif","Suudi Arabistan","Binlerce yıl boyunca Pers, Portekiz ve Osmanlı güçlerinin kan döktüğü, adanın merkezindeki sarp bir tepede yükselen o antik hisar. Savaşların şiddetiyle toprağa mühürlenen o ağır, kolektif katliam frekansı ve yıkık burçlarda esen rüzgarın taşıdığı o tarihi hüzün auranızı paramparça eder.",4"""

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

print("Suudi Arabistan kayitlari eklendi.")
