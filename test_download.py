import urllib.request
import ssl

url = "https://upload.wikimedia.org/wikipedia/commons/7/78/SalemWitchcraftTrial.jpg"
try:
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(url, headers={'User-Agent': 'LanetliYerlerBot/1.0 (test@example.com)'})
    with urllib.request.urlopen(req, timeout=10, context=ctx) as response:
        print("Success! Downloaded", len(response.read()), "bytes")
except Exception as e:
    print("Download failed:", e)
