import csv
import re
import io

data = """"Rose Hall Malikanesi (Beyaz Cadı'nın Evi)","Montego Bay","Jamaika","Annie Palmer adındaki 'Beyaz Cadı'nın üç kocasını ve sayısız köleyi vahşice katlettiği efsanevi sömürge malikanesi. Voodoo ayinlerinin izlerini taşıyan kanlı yatak odalarında gezinirken, duvarlara kazınmış olan o ezici Afrika büyüsü (Obeah) ve işkence gören kölelerin ağır keder frekansı zihninize saldırır.",5"Batık Korsan Şehri (Port Royal)","Kingston Körfezi","Jamaika","17. yüzyılda 'Dünyanın En Günahkar Şehri' olarak bilinen ve devasa bir depremle sulara gömülen o lanetli korsan başkenti. Geceleri okyanusun altından kilise çanlarının çaldığı duyulan bu körfezde, boğulan on binlerce insanın ve korsanların arafta kalan o karanlık, sülfürik enerjisi denizi zehirler.",5"Edinburgh Kalesi (Lewis Hutchinson'ın Evi)","St. Ann","Jamaika","Jamaika'nın ilk kaydedilen seri katili olan ve zevk için yolcuları vurup cesetlerini bir obruğa atan Lewis Hutchinson'ın izole kalesi. Harabelerin altında uzanan ve cesetlerin atıldığı o devasa karanlık obruğun (sinkhole) yanına yaklaştığınızda, o saf psikopatik şiddet frekansı nefesinizi keser.",4"Martha Brae Nehri (Cadı Suları)","Trelawny","Jamaika","İspanyol işgalcilere altınların yerini söylememek için nehrin yatağını büyüyle değiştirerek onlarla birlikte boğulan Taino cadısı Martha Brae'nin lanetli suları. Zifiri karanlık ormanın içinden akan bu sessiz nehirde, suların altından gelen o intikamcı, elementer Voodoo çekimi empatları adeta içine çeker.",4"Spanish Town Eski Zindanları","Spanish Town","Jamaika","Adanın eski başkenti olan ve sömürgecilerin köleleri hapsettiği, hastalıktan kırılan o rutubetli, eski İspanyol zindanları. Yüzlerce yıldır tuğlalara sinmiş olan sarı humma acısı ve zincire vurulanların duvarlardan yankılanan o ağır, melankolik çaresizlik frekansı kalbinize oturur.",4"Tuol Sleng Soykırım Müzesi (S-21 Hapishanesi)","Phnom Penh","Kamboçya","Kızıl Kmerler döneminde bir liseden ölüm kampına dönüştürülen ve 20.000'den fazla insanın akıl almaz işkencelerle katledildiği o kanlı binalar. Hücrelerin zeminindeki o silinmeyen kan lekelerinden fışkıran mutlak dehşet ve devasa, saf travmatik anksiyete, içeri girenlerin aurasını fiziksel olarak yırtar.",5"Choeung Ek (Ölüm Tarlaları)","Phnom Penh","Kamboçya","Yağmur yağdıkça toprağın altından hala insan kemiklerinin ve elbiselerin yüzeye çıktığı devasa ve sessiz toplu mezar alanları. Milyonlarca masumun acımasızca katledildiği bu ölüm arazisinde esen rüzgar bile ağıt gibi uğuldar; o ezici soykırım frekansı zamanı ve mekanı tamamen yok eder.",5"Bokor Hill Station","Kampot","Kamboçya","Ormanın derinliklerinde, sarp bir tepede yer alan ve sislerin arasından hayalet gibi beliren devasa, terk edilmiş bir Fransız koloni kasabası ve kumarhanesi. İnşaatında binlerce işçinin öldüğü ve Kızıl Kmerlerin siper olarak kullandığı bu çürümüş beton canavar, ağır bir komünist/emperyalist çatışma laneti saçar.",5"Angkor Wat Orman Dehlizleri","Siem Reap","Kamboçya","Binlerce yıllık, devasa ağaç köklerinin tapınakları yuttuğu bu görkemli ama karanlık Angkor kompleksi. Gündüzün turistik kalabalığı çekildiğinde, eski Khmer krallarının kurban ayinlerinin yapıldığı gizli dehlizlere çöken o kadim, yoğun Asya okültizmi ve orman cinlerinin fısıltısı insanı delirtir.",4"Kampong Chhnang (Terk Edilmiş Üs)","Kampong Chhnang","Kamboçya","Kızıl Kmerlerin on binlerce köleyi ölümüne çalıştırarak inşa ettiği ancak devrilmeleriyle aniden terk edilen devasa, izole havaalanı ve tünel sistemi. Beton pistin etrafını saran ormanın sessizliği ve toprağın altına gömülü isimsiz işçilerin o mutlak, çaresiz izolasyon frekansı zihninizi daraltır.",4"""

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

print("Jamaika ve Kambocya kayitlari eklendi.")
