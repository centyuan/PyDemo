# import time
# import requests
# import hashlib
# import json
# from decimal import Decimal
# import uuid
# import decimal
#
#
#
# server = "http://api.wg08.vip/api/"
# Token = "b7027c340a0c4073aa1560b152f42531"
# md5_key = "b4a75235"
# headers = {
#     "content-type": "application/json"
# }
#
#
# class DecimalEncoder(json.JSONEncoder):
#
#     def default(self, o):
#
#         if isinstance(o, decimal.Decimal):
#             return float(o)
#
#         super(DecimalEncoder, self).default(o)
#
#
# def get_sign(sign_dict,key):
#     sign_str = sign_dict['Token']+sign_dict['GameCode']+sign_dict['PlayerName']+sign_dict['PlayerPassword']+sign_dict['TimeSapn']+key
#     return hashlib.md5(sign_str.encode('utf8')).hexdigest()
#
# #检查登录或者注册
# def checkorcreategameaccout(account):
#
#     params = {
#         'Token':Token,
#         #'GameCode':'AG',
#         #'GameCode':'BG',
#         #'GameCode':'GB',
#         'GameCode':'KY',
#         'PlayerName':"xj" + str(account),
#         'PlayerPassword':'123456',
#         'TimeSapn':time.strftime("%Y%m%d%H%M%S"), #格式20180624180521
#         #'Sign':'7E8CF53828DB3E00109F5E8C2E4F67A9'
#     }
#     sign= get_sign(params,md5_key)
#     params['Sign'] = sign
#     url = server+"Register"
#     result = requests.post(url,data=json.dumps(params), headers=headers)
#     outcome = json.loads(result.text)
#     if outcome['StatusCdoe'] == 1:
#         return True
#     else:
#         return False
#
# def forwardgame(account,playcode,mh5):
#     sign_data = {
#         'Token':Token,
#         #'GameCode':'AG',
#         #'GameCode':'BG',
#         #'GameCode':'GB',
#         'GameCode':'KY',
#         'PlayerName':"xj" + str(account),
#         'PlayerPassword':'123456',
#         'TimeSapn':time.strftime("%Y%m%d%H%M%S"),
#         #'Sign':'sign',
#     }
#     post_data = {
#         "GameName":playcode,
#         'UserIp':'127.0.0.1',
#         'DeviceType':0,
#     }
#     sign_data['Sign'] = get_sign(sign_data,md5_key)
#     params = dict(sign_data,**post_data)
#     url = server+"Login"
#     result = requests.post(url, data=json.dumps(params), headers=headers)
#     outcome = json.loads(result.text)
#     print('----',params)
#     print('----',outcome)
#     if outcome['StatusCdoe'] == 1:
#         return outcome['PayUrl']
#     else:
#         return False
#
#
# def preparetransfercredit(account, money, in_or_out="IN"):
#     seq = str(uuid.uuid1())
#     billno = "".join(seq.split('-'))
#     # billno = 'B9992054603AA450F81879FF68F89435' #uuid格式
#     sign_data = {
#         'Token': Token,
#         'GameCode': 'AG',
#         'PlayerName': "xj" + str(account),
#         'PlayerPassword': '123456',
#         'TimeSapn': time.strftime("%Y%m%d%H%M%S"),
#         # 'Sign':'sign',
#     }
#     sign_data['Sign'] = get_sign(sign_data, md5_key)
#     post_data = {
#         "TranType": in_or_out,
#         "Money": str(money),
#         "OrderNo": billno,
#     }
#     params = dict(sign_data, **post_data)
#     url = server + "Transfer"
#     result = requests.post(url, data=json.dumps(params,cls=DecimalEncoder),headers=headers)
#     outcome = json.loads(result.text)
#     print('-----',params)
#     print('-----',outcome)
#     if outcome['StatusCdoe'] == '1':
#         return True, True
#
#     elif outcome['StatusCdoe'] == '307':
#         return "余额不足", False
#     else:
#         return outcome["Message"], False
#
#
# #会员登入
# def gologin(account,money,ip,playcode,platform):
#     #登录先注册
#     if checkorcreategameaccout(account):
#         # 如果存在金额，则先进行转账，再跳转
#         if Decimal(money) > Decimal("0"):
#             upfen(account, money)
#         if platform is None:
#             mh5 = 'y'
#         else:
#             mh5 = None
#         return forwardgame(account, playcode, mh5), True
#     else:
#         return '用户出错', False
#
#
#
# #上分
# def upfen(account, money):
#     if checkorcreategameaccout(account):
#         return preparetransfercredit(account, money, in_or_out="IN")
#     else:
#         return '用户出错', False
#
# #下分
# def downfen(account, money):
#     if checkorcreategameaccout(account):
#         return preparetransfercredit(account, money, in_or_out="OUT")
#     else:
#         return '用户出错', False
#
#
# #查询余额
# def querybalance(account):
#     if checkorcreategameaccout(account):
#         params = {
#             'Token': Token,
#             'GameCode': 'KY',
#             'PlayerName': "xj" + str(account),
#             'PlayerPassword': '123456',
#             'TimeSapn': time.strftime("%Y%m%d%H%M%S"),  # 格式20180624180521
#             # 'Sign':'7E8CF53828DB3E00109F5E8C2E4F67A9'
#         }
#         params['Sign'] = get_sign(params,md5_key)
#         url = server + "QueryBalance"
#         result = requests.post(url,data=json.dumps(params),headers=headers)
#         outcome = json.loads(result.text)
#         print('------',params)
#         print(outcome)
#         if outcome['StatusCdoe'] == 1:
#             return Decimal(outcome['Balance']),True
#         else:
#             return outcome['Message'],False
#
#     else:
#         return "用户出错",False
#
#
#
#
# if __name__ == "__main__":
#     #BG AG UG V-G MX GBC
#     #gologin(account,money,ip,playcode,platform):
#
#     gologin('xj16191','0','127.0.0.1','GameName','0')
#     #forwardgame('zzzxxx88','AG','')
#     #upfen("xj16191",10)
#     #downfen('zzzxxx88',10)
#     querybalance('16191')
#
#
# #
# # {
# #     "currency": "CNY",
# #     "balance": "47.000",
# #     "promotion_commission": "0.000",
# #     "freeze_balance": "0.000",
# #     "update_time": "2019-10-23T10:53:32.742487",
# #     "team_promotion_income": 0,
# #     "transfer_balance": 47.0,
# #     "kybalance": "8.000",
# #     "agbalance": "25.100"
# # }