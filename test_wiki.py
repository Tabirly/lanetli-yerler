import json
import urllib.request
import urllib.parse
import urllib.error

def test():
    try:
        url = "https://tr.wikipedia.org/w/api.php?action=query&titles=Aokigahara&prop=pageimages&format=json&pithumbsize=800"
        req = urllib.request.Request(url, headers={'User-Agent': 'LanetliYerlerBot/1.0 (test@example.com)'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode('utf-8'))
            print("TR Aokigahara:", json.dumps(data, indent=2))
    except urllib.error.HTTPError as e:
        print("HTTP Error:", e.code)

    try:
        url = "https://en.wikipedia.org/w/api.php?action=query&titles=Aokigahara&prop=pageimages&format=json&pithumbsize=800"
        req = urllib.request.Request(url, headers={'User-Agent': 'LanetliYerlerBot/1.0 (test@example.com)'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode('utf-8'))
            print("EN Aokigahara:", json.dumps(data, indent=2))
    except urllib.error.HTTPError as e:
        print("HTTP Error:", e.code)

test()
