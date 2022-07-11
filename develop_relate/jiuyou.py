import json
import requests
auth_data = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJIWDFqOXRhb2xvdjEzMTQiLCJib2R5Ijp7ImNvdW50cnlDb2RlIjoiKzg2IiwibWVyY2hhbnQiOiJIWDEiLCJvcmlnaW4iOiIyMjIuMjA5LjIwOC4xNjYiLCJyZWdEZXZpY2UiOiJtb2JpbGUiLCJyZWdIb3N0IjoiMTI3LjAuMC4xIiwicmVnSXAiOiIxMjcuMC4wLjEiLCJzdGF0ZSI6Ik5PUk1BTCIsInVzZXJuYW1lIjoiSFgxajl0YW9sb3YxMzE0In0sImJvZHlDbGFzcyI6ImNvbS5wZy5sb2JieS5qOWJjLmF1dGguc2hpcm8uU2hpcm9Vc2VyIiwiZXhwIjoxNjU3NTQ2MDc3MzU4LCJpYXQiOjE2NTc1NDI0NzczNTgsImp0aSI6ImRkNzdiMGUxLTkxYTQtNDdjOC04NWI5LWE1ODYyNTAzNGMwNiIsIm5iZiI6MTY1NzU0MjQ3NzM1OH0.Ry_YrTyVfqRoPvPe67yIRzn7SuSPFq2c6A5P-XGVux8'
wallet_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'authorization':auth_data,
}
to_headers = {
    'accept-language':'cn',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'authorization':auth_data,
    'display-language':'cn',
    'login-name':'HX1j9taolov1314',
    'product-id':'HX1',
    'referer':'https://j9con.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'x-request-domain': 'j9con.com',
    'x-website-code': 'HX1_PC',
    # 'authority': 'j9bcrest.com',
    # 'method': 'POST',
    # 'path': '/api/swap/open/calc/to',
    # 'scheme': 'https',
    # 'host':'j9bcrest.com',
}

wallet_url = 'https://j9bcrest.com/api/customer/wallet'
to_url = 'https://j9bcrest.com/api/swap/open/calc/to'
tran_url = 'https://j9bcrest.com/api/swap/trading-pair/transaction'

to_data = {
    'token':'USDT',
    'value':1,
    'tradeCode':'J9BC_USDT',
}
wall_res = requests.get(wallet_url,headers=wallet_headers)
print('wall_res:',wall_res.text)
print(wall_res.headers)
to_res = requests.post(to_url,headers=to_headers,data=to_data)
print('to_res:',to_res.text)

tran_data ={"fromToken":"USDT","fromValue":1,"slippageTolerance":0.05,"toValue":47.42445508,"tradeCode":"J9BC_USDT"}
tran_res = requests.post(tran_url,data=tran_data,headers=to_headers)
print('tran_res:',tran_res.text)


import httpx
client = httpx.Client(http2=True,verify=False)
to_h = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'authorization': auth_data,
    # ':authority':'j9bcrest.com',
    # ':method':'POST',
    # ':path':'/api/swap/open/calc/to',
    # ':scheme':'https',
    'authority': 'j9bcrest.com',
    'method': 'POST',
    'path': '/api/swap/open/calc/to',
    'scheme': 'https',
}
# response = client.post(to_url,headers=to_headers,data=to_data)
# print(response.text,response.headers)
import requests

import requests
headers = {
    'authority': 'j9bcrest.com',
    'x-request-domain': 'j9con.com',
    'accept-language': 'cn',
    'sec-ch-ua-mobile': '?0',
    'display-language': 'cn',
    'authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJIWDFqOXRhb2xvdjEzMTQiLCJib2R5Ijp7ImNvdW50cnlDb2RlIjoiKzg2IiwibWVyY2hhbnQiOiJIWDEiLCJvcmlnaW4iOiIxMDMuMTk3LjcwLjQ4IiwicmVnRGV2aWNlIjoibW9iaWxlIiwicmVnSG9zdCI6IjEyNy4wLjAuMSIsInJlZ0lwIjoiMTI3LjAuMC4xIiwic3RhdGUiOiJOT1JNQUwiLCJ1c2VybmFtZSI6IkhYMWo5dGFvbG92MTMxNCJ9LCJib2R5Q2xhc3MiOiJjb20ucGcubG9iYnkuajliYy5hdXRoLnNoaXJvLlNoaXJvVXNlciIsImV4cCI6MTY1NzU0NzA4NDI0MiwiaWF0IjoxNjU3NTQzNDg0MjQyLCJqdGkiOiIwYjJjYmZmZS02MWFiLTQxZTktODU1ZC05YTM5MGIyZjQ0ZDMiLCJuYmYiOjE2NTc1NDM0ODQyNDJ9.3YTj1qNJdKGeHg84lmg4Ncjgu0xbMxjjfc_sAGIDSLY',
    'content-type': 'application/json;charset=UTF-8',
    'accept': 'application/json, text/plain, */*',
    'product-id': 'HX1',
    'x-website-code': 'HX1_PC',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'login-name': 'HX1j9taolov1314',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://j9con.com/',
}
new_h = {
    'authority': 'j9bcrest.com',
    'x-request-domain': 'j9con.com',
    'accept-language': 'cn',
    'sec-ch-ua-mobile': '?0',
    'display-language': 'cn',
    'authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJIWDFqOXRhb2xvdjEzMTQiLCJib2R5Ijp7ImNvdW50cnlDb2RlIjoiKzg2IiwibWVyY2hhbnQiOiJIWDEiLCJvcmlnaW4iOiIyMjIuMjA5LjIwOC4xNjYiLCJyZWdEZXZpY2UiOiJtb2JpbGUiLCJyZWdIb3N0IjoiMTI3LjAuMC4xIiwicmVnSXAiOiIxMjcuMC4wLjEiLCJzdGF0ZSI6Ik5PUk1BTCIsInVzZXJuYW1lIjoiSFgxajl0YW9sb3YxMzE0In0sImJvZHlDbGFzcyI6ImNvbS5wZy5sb2JieS5qOWJjLmF1dGguc2hpcm8uU2hpcm9Vc2VyIiwiZXhwIjoxNjU3NTUwNzkzOTE3LCJpYXQiOjE2NTc1NDcxOTM5MTcsImp0aSI6ImQyZTIwZmQzLWNmMDUtNGU5MS05OWQxLTZlYWE4ZWEyZWViYSIsIm5iZiI6MTY1NzU0NzE5MzkxN30.7b-Uosx-atLz4BwXKp96nKDfOldMFvHKeOCRWWyJZ70',
    'product-id': 'HX1',
    'accept': 'application/json, text/plain, */*',
    'x-website-code': 'HX1_PC',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://j9con.com/',
}
json_data = {
    'token': 'J9BC',
    'value': 1,
    'tradeCode': 'J9BC_USDT',
}
response = requests.post('https://j9bcrest.com/api/swap/open/calc/to', headers=new_h, json=json_data)
print('返回',response.text)
val = response.json().get('data').get('value')
print('aa',val)
json_data_1 = {
    'fromToken': 'J9BC',
    'fromValue': 1,
    'slippageTolerance': 0.02,
    'toValue': val,
    'tradeCode': 'J9BC_USDT',
}
print('vaaa',val)
response = requests.post('https://j9bcrest.com/api/swap/trading-pair/transaction', headers=new_h, json=json_data_1)
print('response返回',response.text)
# https://curlconverter.com/
