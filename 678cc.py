from freeproxy import freeproxy
import requests
proxy_sources = ['jiangxianli', 'taiyanghttp']
fp_client = freeproxy.FreeProxy(proxy_sources=proxy_sources)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}


data = {
    "uri":"/personal/insertNewMemberBankInfo",
    "token":"1d7eed3debf84f9b961bf81ee7b89d53",
    "paramData":{
    "bankAccountName": "刘木生",
    "bankAddress": "usdt",
    "bankCardNo": "TNMvyPR68ji1Qvwskb9FL2Bc4SAwrVj1p4",
    "defaultFlg": True,
    "siteCode": "jeroy",
    "typeCode": "USDT",
    "typeName": "USDT美金账户",
    "value": "TRC20",
    "verifyPhoneInput": "",
    "withdrawalPassword": "4b82ba17481acc7ad9fec620bd960b80",
    }
}

url = "https://www.67874.cc/wap/personal/insertNewMemberBankInfo"

response = fp_client.get('http://httpbin.org/get', headers=headers)
print(response.text)

