import csv
import json
import re

rows = list(csv.DictReader(open('perili_mekanlar.csv', encoding='utf-8')))
js_str = json.dumps(json.dumps(rows, ensure_ascii=False))
txt = open('../Lanetli Yerler.txt', encoding='utf-8').read()

import re
pattern = re.compile(r'const csvData = ".*?";')
txt = pattern.sub(lambda m: 'const csvData = ' + js_str + ';', txt)

open('../Lanetli Yerler.txt', 'w', encoding='utf-8').write(txt)
print("Updated successfully")
