import csv

img_map = {
    'Kaya Köy': 'images/kaya-koy-hayalet-köy-1.jpg, images/kaya-koy-hayalet-köy-2.jpg, images/kaya-koy-hayalet-köy-3.png',
    'Büyükada Yetimhanesi': 'images/buyukada-yetimhanesi-1.jpg, images/buyukada-yetimhanesi-2.jpg',
    'Aokigahara Ormanı': 'images/aokigahara -ormani-1.jpg, images/aokigahara -ormani-2.jpg'
}

with open('perili_mekanlar.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    updated = False
    for k, v in img_map.items():
        if k in line:
            # We assume resim_url is the last column
            # If line doesn't end with a comma, or if we just want to replace the end:
            parts = line.strip().rsplit(',', 1)
            # If the last part is empty (i.e. no image), or we want to overwrite it
            if len(parts) > 1:
                new_lines.append(parts[0] + ',"' + v + '"\n')
                updated = True
                break
    if not updated:
        new_lines.append(line)

with open('perili_mekanlar.csv', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Images updated successfully.")
