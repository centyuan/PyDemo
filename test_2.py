import requests
import json
headers = {

    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",

}
url = "https://599.com/live/"
url_1 = "https://599.com/live/wcbf.html"
url_2 = "https://api.599.com/footballapi/core/matchlist/v1/result?lang=zh&timeZone=8&date=2022-05-30&platform=pc$version=666&appType=3&st=1653880709136&sign=02c37a30aa28ab88cd2c3c0e4c3078d299"

cookies = {
    "Hm_lvt_b8167d9d4d6b87ad4f016f6096a48019":"1653875311",
    "acw_tc":"0bca393616538791082863117e014a1a59458500457353e6d9094f4f481c97",
    "Hm_lpvt_b8167d9d4d6b87ad4f016f6096a48019":"1653880709",
}

re = requests.get(url_2,headers=headers,cookies=cookies)
print(re.text)
da = json.loads(re.text)
# for it in da.get("finishFilter"):
#     print(it)
# print("-----------------------")
for it in da.get("current").get("match"):
    print(it)
    break