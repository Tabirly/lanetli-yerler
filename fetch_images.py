import csv
import json
import os
import urllib.request
import urllib.parse
import re

# Dosya yolları
base_dir = r"C:\Users\User\Desktop\Lanetli Yerler\lanetli-yerler"
csv_path = os.path.join(base_dir, "perili_mekanlar.csv")
temp_csv_path = os.path.join(base_dir, "perili_mekanlar_temp.csv")
img_dir = os.path.join(base_dir, "images")

if not os.path.exists(img_dir):
    os.makedirs(img_dir)

def fetch_wiki_image(title):
    try:
        # TR Wikipedia
        url_tr = f"https://tr.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(title)}&prop=pageimages&format=json&pithumbsize=800&origin=*"
        req_tr = urllib.request.Request(url_tr, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req_tr, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            pages = data.get("query", {}).get("pages", {})
            if pages:
                page = list(pages.values())[0]
                if "thumbnail" in page and "source" in page["thumbnail"]:
                    return page["thumbnail"]["source"]

        # EN Wikipedia fallback
        url_en = f"https://en.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(title)}&prop=pageimages&format=json&pithumbsize=800&origin=*"
        req_en = urllib.request.Request(url_en, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req_en, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            pages = data.get("query", {}).get("pages", {})
            if pages:
                page = list(pages.values())[0]
                if "thumbnail" in page and "source" in page["thumbnail"]:
                    return page["thumbnail"]["source"]
    except Exception as e:
        print(f"[{title}] API error: {e}")
    return None

def sanitize_filename(name):
    # Geçersiz karakterleri temizle
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    name = name.strip().replace(' ', '_').lower()
    return name

def download_image(url, filename):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as response:
            with open(filename, 'wb') as f:
                f.write(response.read())
        return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False

with open(csv_path, 'r', encoding='utf-8') as f_in, open(temp_csv_path, 'w', encoding='utf-8', newline='') as f_out:
    reader = csv.DictReader(f_in)
    fieldnames = reader.fieldnames
    if "resim_url" not in fieldnames:
        fieldnames.append("resim_url")
    
    writer = csv.DictWriter(f_out, fieldnames=fieldnames)
    writer.writeheader()
    
    count = 0
    for row in reader:
        count += 1
        ad = row['ad']
        
        # Eğer zaten bir resmi varsa atla (Script yarım kalırsa diye)
        if row.get('resim_url') and row['resim_url'].startswith('images/'):
            writer.writerow(row)
            continue
            
        print(f"[{count}] İşleniyor: {ad}")
        img_url = fetch_wiki_image(ad)
        
        resim_kayit_yolu = ""
        if img_url:
            safe_name = sanitize_filename(ad) + ".jpg"
            local_path = os.path.join(img_dir, safe_name)
            
            if os.path.exists(local_path) or download_image(img_url, local_path):
                # Başarılı ise csv'ye yaz
                resim_kayit_yolu = f"images/{safe_name}"
            else:
                print(f"  -> Resim indirilemedi: {img_url}")
        else:
            print(f"  -> Wikipedia'da resim bulunamadı.")
            
        row['resim_url'] = resim_kayit_yolu
        writer.writerow(row)

# Dosyayı değiştir
os.replace(temp_csv_path, csv_path)
print("Bitti! Tüm resimler indirildi ve CSV güncellendi.")
