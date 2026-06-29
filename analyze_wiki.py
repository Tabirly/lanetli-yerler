import csv
import json
import urllib.request
import urllib.parse
import re

def search_wiki(query, lang):
    clean_query = re.sub(r'\(.*?\)', '', query).strip()
    url = f"https://{lang}.wikipedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(clean_query)}&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'LanetliYerlerBot/1.0 (test@example.com)'})
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode('utf-8'))
            results = data.get('query', {}).get('search', [])
            return len(results) > 0
    except Exception as e:
        return False

total = 0
any_found = 0
not_found_list = []

try:
    with open('perili_mekanlar.csv', 'r', encoding='utf-8') as f:
        reader = list(csv.DictReader(f))
        total = len(reader)
        for row in reader:
            name = row['ad']
            
            found_tr = search_wiki(name, 'tr')
            if found_tr:
                any_found += 1
            else:
                found_en = search_wiki(name, 'en')
                if found_en:
                    any_found += 1
                else:
                    not_found_list.append(name)
except Exception as e:
    with open('wiki_results.txt', 'w', encoding='utf-8') as out:
        out.write(f"ERROR: {str(e)}\n")
    import sys
    sys.exit(1)

with open('wiki_results.txt', 'w', encoding='utf-8') as out:
    out.write(f"Toplam: {total}\n")
    out.write(f"Bulunan: {any_found}\n")
    out.write(f"Ozgur: {total - any_found}\n")
    out.write(f"Ozgurluk Orani: %{((total - any_found) / total) * 100:.2f}\n")
    for n in not_found_list[:10]:
        out.write(f"- {n}\n")
