import csv
import re
import io

data = """"A'ali Tümülüsleri (Antik Mezarlar)","A'ali","Bahreyn","Tarih öncesi Dilmun uygarlığına ait, çölün ortasında kilometrelerce uzanan binlerce antik tepe mezarı. Güneş battığında bu devasa nekropolden yayılan o kadim, ağır ve yeraltına çeken ölüm frekansı; asırlar öncesinin pagan ritüellerini ve kanlı adaklarını adeta havaya kazımıştır.",5"Barbar Tapınağı Harabeleri","Diraz","Bahreyn","Eski Sümer su tanrısı Enki'ye adanmış ve yerin altına doğru katman katman inen bu kadim, lanetli tapınak kompleksi. Yeraltı su kaynaklarının hala fokurdadığı bu ritüel alanında gezinirken, antik kurban ayinlerinin o vahşi ve ilkel sülfürik enerjisi empatları bayıltacak kadar yoğundur.",5"Hayat Ağacı (Tree of Life) Çölü","Jebel Dukhan","Bahreyn","Suyun olmadığı çorak bir çölün ortasında, yüzlerce yıldır yeşil kalan ama etrafında sürekli paranormal aktivitelerin ve cin efsanelerinin döndüğü devasa yalnız ağaç. Geceleri ağacın dallarından yayılan o yoğun manyetik çekim ve kumların arasında beliren meçhul silüetler, buranın bir çöl portalı olduğunu kanıtlar.",4"Eski Muharrak Sokakları","Muharrak","Bahreyn","Bir zamanlar inci ticaretiyle zenginleşen ama deniz kazalarında veya kölelik şartlarında ölenlerin lanetiyle terk edilen eski, labirent gibi tüccar evleri. Oksijensiz ve rutubetli dar sokaklarda yankılanan, boğulmuş inci dalgıçlarının feryatları ve o yoğun, kederli su frekansı ruhunuzu daraltır.",4"Khamis Camii Harabeleri","Manama","Bahreyn","Bölgenin en eski İslami yapılarından biri olan ancak ikiz minarelerinin etrafında asırlardır karanlık gölgelerin dolaştığı bu antik harabe. Çöl rüzgarının eski taşlar arasında çıkardığı uğultu ve arafta kalmış eski savaşçıların o ağır, melankolik frekansı; zaman algınızı tamamen bozar.",3"Panam Nagar (Hayalet Şehir)","Narayanganj","Bangladeş","Bengal'in altın çağında zengin Hindu tüccarlar tarafından inşa edilen ancak kanlı dini çatışmalarla tamamen terk edilen bu devasa ve gotik harabe şehir. Sarmaşıkların yuttuğu kırmızı tuğlalı malikanelerde yankılanan ayak sesleri ve o ani, travmatik katliam frekansı şehrin aurasını kalıcı olarak zehirlemiştir.",5"Lalbagh Kalesi (Mühürlü Dehlizler)","Dakka","Bangladeş","Babür İmparatorluğu'ndan kalma ve inşaatı asla bitirilemeyen bu kanlı saray kompleksinin zifiri karanlık yeraltı geçitleri. Askerlerin ve atların bile girip kaybolduğu efsanevi tünellere yaklaştığınızda, yerin altından sızan o boğucu karanlık ve görünmez varlıkların ağır psişik baskısı nefesinizi keser.",5"Foy's Lake Ormanları","Chittagong","Bangladeş","Görünüşte huzurlu bir göl olan ancak etrafındaki sık ormanlarda 'Beyazlı Kadın'ın (Shankhachurni) ve boğulmuş ruhların dolaştığı o yutucu, nemli karanlık. Geceleri gölün yüzeyinden yayılan o soğuk, hipnotik çekim gücü ve ormandan gelen açıklanamayan feryatlar, zihninizi intihara doğru sürükleyen bir girdaptır.",4"Ghilachhari (Kanlı Vadi)","Chittagong Hill Tracts","Bangladeş","Yıllarca süren gerilla savaşlarına ve kabile katliamlarına sahne olan, ormanın derinliklerindeki bu sisli ve lanetli vadi. Ağaçların arasına sinmiş olan ve toprağın adeta kusmaya çalıştığı o saf şiddet, barut kokusu ve masumların arafta kalmış çaresizlik frekansı; bedeninize giren fiziksel bir acı yaratır.",5"Bogra Nawab Sarayı (Terk Edilmiş)","Bogra","Bangladeş","Geçmişteki zengin Bengal aristokrasisinin çöküşünü simgeleyen, içi dökülmüş, devasa ve yalnız malikane. Eski sahiplerinin intiharlarına ve cinayetlere sahne olan sarayın boş salonlarında yankılanan eski müzik sesleri ve o ağır, sülfürik keder enerjisi; buranın bir zaman döngüsü tuzağı olduğunu hissettirir.",4"""

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

print("Bahreyn ve Banglades kayitlari eklendi.")
