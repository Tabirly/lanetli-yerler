import os
import csv
import pickle
import time
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/blogger']
BLOG_ID = '2621008100567662305'

CRED_PATH = r'C:\Users\User\.gemini\antigravity\scratch\blogger_seo_sync\credentials.json'
TOKEN_PATH = r'C:\Users\User\.gemini\antigravity\scratch\blogger_seo_sync\token.pickle'
CSV_PATH = 'perili_mekanlar.csv'

def get_blogger_service():
    creds = None
    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH, 'rb') as token:
            creds = pickle.load(token)
            
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CRED_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, 'wb') as token:
            pickle.dump(creds, token)
            
    return build('blogger', 'v3', credentials=creds)

def determine_category(name, story):
    text = (name + " " + story).lower()
    
    if any(k in text for k in ['kale', 'şato', 'sato']):
        return 'Perili Kaleler'
    elif any(k in text for k in ['orman', 'koruluk', 'ağaç', 'agac']):
        return 'Perili Ormanlar'
    elif any(k in text for k in ['köy', 'kasaba', 'koy']):
        return 'Terkedilmiş Köyler'
    elif any(k in text for k in ['hastane', 'tımarhane', 'sanatoryum', 'akıl', 'klinik']):
        return 'Perili Hastaneler'
    elif any(k in text for k in ['ev', 'köşk', 'malikane', 'konak', 'yalı']):
        return 'Lanetli Evler ve Köşkler'
    elif any(k in text for k in ['ada']):
        return 'Lanetli Adalar'
    elif any(k in text for k in ['otel', 'motel', 'pansiyon']):
        return 'Perili Oteller'
    elif any(k in text for k in ['mezarlık', 'kript', 'türbe', 'mezar']):
        return 'Perili Mezarlıklar'
    elif any(k in text for k in ['zindan', 'hapishane', 'cezaevi']):
        return 'Perili Hapishaneler'
    else:
        return 'Diğer Gizemli Mekanlar'

def generate_html(row, category):
    img_url = "https://via.placeholder.com/800x400.png?text=Gorsel+Yakinda"
    
    html = f"""
<div class="haunted-place-post" 
     data-city="{row['sehir']}" 
     data-country="{row['ulke']}" 
     data-rating="{row['puan']}" 
     data-category="{category}">
     
  <div class="place-header" style="text-align: center; margin-bottom: 20px;">
      <img src="{img_url}" alt="{row['ad']}" style="max-width:100%; border-radius:12px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
  </div>
  
  <div class="place-meta" style="background: #f8f9fa; padding: 15px; border-radius: 8px; margin-bottom: 20px; border-left: 4px solid #d9534f;">
    <p style="margin: 5px 0;"><strong>📍 Konum:</strong> {row['sehir']}, {row['ulke']}</p>
    <p style="margin: 5px 0;"><strong>⭐ Puan:</strong> {row['puan']} / 5</p>
    <p style="margin: 5px 0;"><strong>🏷️ Kategori:</strong> {category}</p>
  </div>
  
  <div class="place-story">
    <h3>Mekanın Hikayesi</h3>
    <p style="line-height: 1.6; font-size: 16px;">{row['hikaye']}</p>
  </div>
  
</div>
"""
    return html

def fetch_existing_titles(service):
    titles = set()
    request = service.posts().list(blogId=BLOG_ID, maxResults=500, fetchBodies=False, status='DRAFT')
    while request is not None:
        response = request.execute()
        if 'items' in response:
            for post in response['items']:
                titles.add(post.get('title', ''))
        request = service.posts().list_next(request, response)
    return titles

def import_to_blogger(test_mode=True):
    service = get_blogger_service()
    
    print("Mevcut yazilar kontrol ediliyor (kopya olusmamasi icin)...")
    existing_titles = fetch_existing_titles(service)
    print(f"{len(existing_titles)} adet yazi bulundu.")
    
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        
    print(f"Toplam {len(rows)} mekan bulundu.")
    
    limit = 2 if test_mode else len(rows)
    count = 0
    added_count = 0
    
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    
    for row in rows:
        if count >= limit:
            break
            
        if row['ad'] in existing_titles:
            print(f"ATLANDI (Zaten var): {row['ad']}")
            count += 1
            continue
            
        category = determine_category(row['ad'], row['hikaye'])
        html_content = generate_html(row, category)
        
        post_body = {
            "title": row['ad'],
            "content": html_content,
            "labels": ["Lanetli Yerler", category]
        }
        
        max_retries = 5
        for attempt in range(max_retries):
            try:
                # Insert as DRAFT
                request = service.posts().insert(blogId=BLOG_ID, body=post_body, isDraft=True)
                response = request.execute()
                print(f"[{count+1}/{limit}] BASARILI: {row['ad']} (Kategori: {category})")
                added_count += 1
                time.sleep(2) # Prevent rate limiting (increased to 2 seconds)
                break # Success, break retry loop
            except Exception as e:
                err_msg = str(e)
                print(f"HATA olustu ({row['ad']}), Deneme {attempt+1}: {err_msg[:100]}...")
                if "429" in err_msg or "rateLimitExceeded" in err_msg or "quota" in err_msg.lower():
                    sleep_time = (2 ** attempt) * 10
                    print(f"Rate limit aşıldı. {sleep_time} saniye bekleniyor...")
                    time.sleep(sleep_time)
                else:
                    break # Not a rate limit error, don't retry
        count += 1
        
    print(f"\nIslem tamamlandi. {added_count} yeni yazi eklendi.")

if __name__ == "__main__":
    print("Tum kayitlar yukleniyor...")
    import_to_blogger(test_mode=False)
    print("\nTum islemler tamamlandi.")
