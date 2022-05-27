import cv2


#
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "HOST": "192.168.8.243",
#         "PORT": 3306,
#         "USER":"root",
#         "PASSWORD": "Isoon@qzmp",
#         "NAME": "actual2",
#     }
# }

#
# i =1
# with open("unpass.txt","r+",encoding="utf-8") as  f:
#
#     for line in f.readlines():
#         print(len(list(line.split("\t"))),line.split('\t'))
#         i +=1
#         if i >10:
#             break
#
#
# i=1
# with open("finish1.txt","r+",encoding="utf-8") as  f:
#
#     for line in f.readlines():
#         print(len(list(line.split("\t"))),line.split('\t'))
#         i +=1
#         if i >10:
#             break

str1 = "a89788071	顏熙德	15/11/2004 10:04:26	a89788071	M	24/2/1966 00:00:00	9	406	中正路188之180號	02-67890123	web@pchome.com.tw			6	4	5	4	D146643032					11/11/2004 21:28:45"
print(len(list(str1.split("\t"))))

# from zstack.config import sessionId
# from zstack.zstack_sdk import *
# action = AttachFirewallRuleSetToL3Action()
# action.vpcFirewallUuid = "c8cc24eb83cb40049d2841a104a149a5"#  zf.fuuid
# action.forward = "in"
# action.ruleSetUuid = "05eb2ab00b5341eaa8cd875b21d8b5bb"
# action.sessionId = sessionId()
# action.l3Uuid = "a6701f68b3804573bf470bcbba74c2ce" # zf.l3uuid
# res = action.call()
# print(res)


# c8cc24eb83cb40049d2841a104a149a5 in 05eb2ab00b5341eaa8cd875b21d8b5bb a6701f68b3804573bf470bcbba74c2ce
# import requests
# import json
# url = "http://192.168.8.24:8080/zstack/v1/api-jobs/8731c21494b34e6ca9fd1d1d180e1020"
# response = requests.get(url)
# result = json.loads(response.text)
# print(result)
# if result.get('error'):
#     res = action.call()
#
# # 2.加载新的防火墙规则集
# time.sleep(0.2)
# new_rule = info.get("new_rule")
# action_c = AttachFirewallRuleSetToL3Action()
# action_c.vpcFirewallUuid = zf.fuuid
# action_c.forward = new_rule.get("type")
# action_c.ruleSetUuid = new_rule.get("rulesetUuid")
# action_c.sessionId = sessionId()
# # l3uuid = zf.l3uuid
# print("更新防火墙规则uuuuuuuuuuuuuuu", zf.fuuid, new_rule.get("target_network"), ruleset.target_network)
# if new_rule.get("target_network") == ruleset.target_network:
#     action_c.l3Uuid = zf.l3uuid
#     res = action.call()
#     print("绑定新的防火墙规则集cc", action.vpcFirewallUuid, action.forward, action.ruleSetUuid, action.l3Uuid, res)
#     # if request_location(res):
    #     response = requests.get(res.get("location"))
    #     result = json.loads(response.text)
    #     print(result)
    #     if result.get('error'):
    #         res = action.call()

