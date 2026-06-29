import csv
import io

raw_data = """
"Capela dos Ossos (Kemikler Şapeli)","Évora","Portekiz","'Biz burada yatan kemikler, sizinkileri bekliyoruz' yazısıyla ziyaretçileri karşılayan, beş binden fazla insanın iskeletinden inşa edilmiş bu klostrofobik şapel. Duvarlara dokunduğunuzda ölümün o soğuk, kaçınılmaz gerçeği ve arafta kalmış binlerce ruhun yarattığı ağır ölüm frekansı nefesinizi keser.",5
"Quinta das Lágrimas (Gözyaşı Malikânesi)","Coimbra","Portekiz","Kraliyetin karanlık bir suikastına kurban giden Inês de Castro'nun vahşice öldürüldüğü bu tarihi bahçe. Efsaneye göre kırmızı kayalardaki lekeler hala onun kanıdır; suyun kenarında durduğunuzda asırlar öncesinin o yoğun, haksız ölüm kederi ve ihanet enerjisi göğsünüze bir mengene gibi oturur.",4
"Valongo Sanatoryumu","Valongo","Portekiz","Beyaz Veba (Verem) kurbanlarının tecrit edildiği ve binlercesinin acı içinde can verdiği bu devasa çürüyen kompleks. Ormanın derinliklerindeki bu harabeye çöken zifiri karanlıkta, duvarlardan gelen boğuk öksürük krizlerini ve nefessiz kalarak ölenlerin o boğucu hastalık enerjisini tüm hücrelerinizde hissedersiniz.",5
"Sintra Dağları (Karanlık Orman)","Sintra","Portekiz","Dışarıdan bir masal diyarını andıran ama geceleri pagan ayinlerine, masonik ritüellere ve boyut kapılarına ev sahipliği yapan bu sisli dağ. Özellikle Initiation Well (İnisiyasyon Kuyusu) etrafında durduğunuzda, yeraltı dünyasının o hipnotik çekim gücü ve kadim okült frekanslar zihninizi tamamen transa sokar.",5
"Beau-Séjour Sarayı","Lizbon","Portekiz","Glória Baronu'nun ruhu tarafından sahiplenilmiş bu görkemli 19. yüzyıl sarayı. Boş koridorlarında kendiliğinden çalan çanlar, görünmez ellerin savurduğu eşyalar ve aniden bastıran dondurucu hava dalgaları; buranın sadece bir bina değil, Baron'un inatçı ve dışlayıcı enerjisiyle mühürlenmiş aktif bir poltergeist alanı olduğunu gösterir.",4
"Castelo de Almourol (Tapınakçı Kalesi)","Vila Nova da Barquinha","Portekiz","Tejo Nehri'nin ortasında sisli bir adacığa inşa edilen bu izole Tapınak Şövalyeleri kalesi. Karanlık sularla çevrili bu yapının taşlarında, asırlar önce ihanete uğrayan şövalyelerin ve nehirde kaybolanların o melankolik, ağır sır frekansı yatar; gece adaya yaklaşanları görünmez bir zırh şakırtısı karşılar.",4
"Teatro Lethes","Faro","Portekiz","Eski bir Cizvit kolejinin kalıntıları üzerine kurulan ve sahnede intihar eden bir balerinin lanetini taşıyan tiyatro. Gösteri bittikten sonra boşalan salonda yankılanan görünmez ayak sesleri ve sahnede biriken o koyu, kederli intihar enerjisi, sanatın ve ölümün en karanlık dansını auranıza kazır.",3
"Peniche Kalesi (Zindanları)","Peniche","Portekiz","Okyanusun acımasız dalgalarının dövdüğü bu sarp kale, uzun yıllar boyunca siyasi mahkumların ağır işkencelerden geçirildiği bir tecrit merkeziydi. Zifiri karanlık izolasyon hücrelerinde durduğunuzda, aklını yitiren mahkumların o paslı çaresizliği ve okyanus rüzgarına karışan iniltileri kalbinizi sızlatır.",4
"Palacete Marques Gomes","Vila Nova de Gaia","Portekiz","Uzun yıllar terk edilmiş halde kalan ve sayısız EVP (Elektronik Ses Fenomeni) kaydına konu olan bu lanetli malikane. Paranormal araştırmacıların girmeye çekindiği bu yapının çökmüş salonlarında, şeytani fısıltılar ve aniden cihazların pillerini emen o aç, alt boyut frekansı insanı derinden sarsar.",4
"Caramulo Sanatoryumu","Caramulo","Portekiz","Avrupa'nın bir dönem en büyük sağlık kompleksi olan ama bugün dağların zirvesinde bir hayalet şehri andıran devasa harabe. Çürüyen yatakhanelerde ve sonsuz gibi görünen koridorlarda esen dondurucu dağ rüzgarı, burada can veren binlerce kırık ruhun veda edememiş yas enerjisini direkt olarak ruhunuza aktarır.",4
"""

reader = csv.reader(io.StringIO(raw_data.strip()))

with open('perili_mekanlar.csv', 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for row in reader:
        if row:
            row.append("")
            writer.writerow(row)

print("Portekiz verileri başarıyla eklendi.")
