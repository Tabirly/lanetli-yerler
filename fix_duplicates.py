import csv
import re
import io

def normalize(name):
    # Remove punctuation and lowercase
    name = re.sub(r'[^\w\s]', '', name.lower())
    # Remove common words
    words_to_remove = ['eski', 'terk', 'edilmis', 'harabeleri', 'zindanlari', 'kalesi', 'ormani', 'mezarligi', 'hastanesi', 'sanatoryumu', 'evi']
    words = [w for w in name.split() if w not in words_to_remove]
    return ' '.join(words)

records = []
seen = set()
dup_count = 0

# Read and deduplicate
with open('perili_mekanlar.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) > 0:
            name = row[0]
            norm_name = normalize(name)
            if norm_name in seen:
                dup_count += 1
            else:
                seen.add(norm_name)
                records.append(row)

# The new locations to add in place of the 3 duplicates
new_data = """"Centralia (Yanan Hayalet Kasaba)","Centralia, Pennsylvania","Amerika Birleşik Devletleri","1962'den beri yeraltındaki kömür madenlerinde sönmeden yanan ve koca bir kasabayı ölümcül karbonmonoksit gazıyla yutan 'Sessiz Tepe' (Silent Hill) ilhamlı hayalet şehir. Çatlamış asfalttan tüten zehirli dumanlar ve toprağın altından gelen o cehennem ateşi uğultusu sizi yutar.",5"St. Louis Mezarlığı No. 1","New Orleans, Louisiana","Amerika Birleşik Devletleri","New Orleans'ın en ünlü ve en perili Voodoo mezarlığı. Kraliçe Marie Laveau'nun da gömülü olduğu, bataklık suyu seviyesi nedeniyle yer üstüne inşa edilmiş bu devasa lahit şehrinde gezinirken, arkanızdan gelen karanlık ayak sesleri ve o ağır, bataklık vodoo titreşimi zihninizi daraltır.",5"Sorrel-Weed Evi","Savannah, Georgia","Amerika Birleşik Devletleri","Amerika'nın en perili şehirlerinden biri olan Savannah'da, cinayetler ve intiharlarla sarsılan ve kölelerin en ağır eziyetleri gördüğü devasa antebellum malikane. Titreşen gaz lambalarının altında havaya asılı kalan o mutlak güney melankolisi ve görünmez ellerin dokunuşları kanınızı dondurur.",5"""

formatted_data = re.sub(r'(\d)"', r'\1\n"', new_data)

new_reader = csv.reader(io.StringIO(formatted_data))
for row in new_reader:
    if row:
        if len(row) == 5:
            row.append('') # resim_url
        records.append(row)

# Write back
with open('perili_mekanlar.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for row in records:
        writer.writerow(row)

print(f"Bitti! {dup_count} adet cift kayit kaldirildi ve yerine 3 adet yeni ABD mekani eklendi. Toplam mekan sayisi su an {len(records) - 1} (1 baslik + 1000 mekan).")
