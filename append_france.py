import csv

raw_data = """
"Paris Yeraltı Mezarları (Katakomplar)","Paris","Fransa","Işıklar şehrinin altında yatan altı milyondan fazla iskeletin oluşturduğu bu devasa ölüm labirenti. Klostrofobik tünellerde ilerlerken, kafataslarının boş göz çukurlarından size sızan o ezici ve kolektif karanlık, ruhunuzu emer. Işıkların ötesine geçildiğinde duyulan bedensiz fısıltılar ve zihni ele geçiren kaybolma hissi tam bir astral kabustur.",5
"Oradour-sur-Glane (Şehitler Köyü)","Nouvelle-Aquitaine","Fransa","Nazi askerleri tarafından 1944'te kadın ve çocukların kilisede diri diri yakıldığı, erkeklerin kurşuna dizildiği ve o günden beri dokunulmadan bırakılan bu hayalet kasaba. Yıkık evlerin ve yanmış arabaların arasında dolaşırken, havada asılı kalan o devasa travma ve haksız ölüm frekansı insanın göğsünü paramparça eder.",5
"Château de Fougeret","Vienne","Fransa","Fransa'nın paranormal aktivitesi en yüksek ve en agresif şatolarından biri. Ziyaretçilerin fiziksel saldırıya uğradığı, eşyaların havada uçuştuğu ve odalarda görünmez varlıkların ağır nefeslerinin duyulduğu bu mekanda, öte alem perdesi tamamen yırtılmıştır; buradaki poltergeist enerjisi kalkanlarınızı anında deler.",5
"Montségur Kalesi","Occitanie","Fransa","Sarp bir dağın zirvesinde yer alan ve 1244'te yüzlerce Kathar müridinin engizisyon tarafından dağın eteklerinde diri diri yakıldığı bu trajedi merkezi. Zirvedeki yıkıntıların arasında esen rüzgar, alevlerin içinde can verenlerin feryatlarını taşır; dağın o acımasız ve fanatik ölüm enerjisi ziyaretçileri transa sokar.",5
"Père Lachaise Mezarlığı","Paris","Fransa","Dünyanın en ünlü ve en gotik mezarlığı. Devasa anıt mezarların ve karga sürülerinin hüküm sürdüğü bu alanda, özellikle karanlık çöktüğünde yapılan okült ve satanik ritüellerin enerjisi uyanır. Heykellerin arasından süzülen şekilsiz gölgeler ve o melankolik, aristokratik ölüm frekansı zihni yavaş yavaş zehirler.",4
"Château de Puymartin","Dordogne","Fransa","Kocası tarafından kuledeki küçük bir odaya hapsedilen ve 15 yıl boyunca orada delirerek ölen Thérèse de Saint-Clar'ın ruhu tarafından sahiplenilmiştir. Geceleri şatonun koridorlarında dolaşan 'Beyazlı Kadın'ın o kederli ve saplantılı dişil enerjisi, kuleye adım atanların nefesini kesen bir ağırlık yaratır.",4
"Versailles Sarayı (Petit Trianon)","Versay","Fransa","Marie Antoinette'in kaçış alanı olan bu saray bahçesinde, zaman anomalileri (Moberly-Jourdain olayı) yaşandığı iddia edilir. Geceleri bahçede dolaşırken aniden etrafın 18. yüzyıl frekansına geçmesi, havada beliren giyotin travmasının ve o aristokratik kibrin boğucu enerjisi, ziyaretçileri boyutsal bir girdaba çeker.",4
"Brocéliande Ormanı","Bretanya","Fransa","Kral Arthur efsanelerine ve karanlık Kelt büyülerine ev sahipliği yapan bu kadim, zifiri orman. Peri vadisi ve dönüşü olmayan yolların bulunduğu bu ağaçlık alanda, doğa elementallerinin ve eski druidlerin bıraktığı o vahşi, primal maji aktiftir; orman geceleri dışarıdan gelen herkesi yutmak isteyen bir bilince bürünür.",4
"Château de Châteaubriant","Loire-Atlantique","Fransa","Kıskanç kocası tarafından kanı yavaşça akıtılarak katledilen Françoise de Foix'nın kanlı mirası. Efsaneye göre her yıl cinayet gününde şatonun merdivenlerinde küçük kan havuzları belirir. Zindanlardan ve odalardan yayılan o paslı kan kokusu ve ihanetin kederli frekansı, kaleyi adeta bir astral hapishaneye çevirmiştir.",4
"Gouffre de Padirac (Şeytanın Çukuru)","Lot","Fransa","Efsaneye göre doğrudan Lucifer'in toprağa vurarak açtığı devasa ve karanlık bir yeraltı uçurumu. Güneş ışığının ulaşamadığı metrelerce derinlikteki yeraltı nehirlerinde sandalla ilerlerken, yeraltı dünyasının o ezici, klostrofobik ve hipnotik enerjisi sizi sonsuz bir karanlığa çekmek ister.",4
"""

import io
reader = csv.reader(io.StringIO(raw_data.strip()))

with open('perili_mekanlar.csv', 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for row in reader:
        if row:
            # Append empty string for resim_url
            row.append("")
            writer.writerow(row)
print("Başarıyla eklendi.")
