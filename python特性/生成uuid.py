
#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-10-18 下午1:33

import uuid

print(uuid.uuid1())
print(uuid.uuid3(uuid.NAMESPACE_DNS,'yuanlin'))
print(uuid.uuid4())
print(uuid.uuid5(uuid.NAMESPACE_DNS,'yuanlin'))


str = "3cfc8d7a-f169-11e9-af5b-58a023321f81"
str_2= "".join(str.split('-'))
print(str_2)
print(len(''.join(str.split('-'))))

"""
uuid1()：这个是根据当前的时间戳和MAC地址生成的，最后的12个字符408d5c985711对应的就是MAC地址，因为是MAC地址，那么唯一性应该不用说了。但是生成后暴露了MAC地址这就很不好了。

uuid3()：里面的namespace和具体的字符串都是我们指定的，然后呢···应该是通过MD5生成的，这个我们也很少用到，莫名其妙的感觉。

uuid4()：这是基于随机数的uuid，既然是随机就有可能真的遇到相同的，但这就像中奖似的，几率超小，因为是随机而且使用还方便，所以使用这个的还是比较多的。

uuid5()：这个看起来和uuid3()貌似并没有什么不同，写法一样，也是由用户来指定namespace和字符串，不过这里用的散列并不是MD5，而是SHA1.
"""


# action = AddSecurityGroupRuleAction()
# action.securityGroupUuid = "19dc0648385c4b1285309fd8a0f24fe0"
# action.rules = [{
#     "type": "Ingress",
#     "startPort": -1,
#     "endPort":-1,
#     "protocol": "ICMP",
#     "allowedCidr": "192.168.1.0/24",
# }]

# from zstack.config import sessionId
# from zstack.zstack_sdk import *
# action.sessionId = sessionId()
# res = action.call()
# action = AddSecurityGroupRuleAction()
# action.securityGroupUuid = "026c2ada94e048af8df044db97a6a6cd"
# action.rules = [{
#     "type": "Ingress",
#     "protocol": "ALL",
#     "allowedCidr": "192.168.10.0/24",
# }]
# action.sessionId = sessionId()
# res = action.call()
# # #{'uuid': '8ecd59868e0d4b6880beaf484d3b8f55', 'securityGroupUuid': 'fd2ceb3fca2848b3bc330735e8ebdab2', 'type': 'Egress', 'ipVersion': 4, 'startPort': 200, 'endPort': 300, 'protocol': 'TCP', 'state': 'Enabled', 'allowedCidr': '192.

# action = DeleteSecurityGroupRuleAction()
# action.ruleUuids = "d59290a1506d41bfabb6628672c4b02b"
# action.sessionId = sessionId()
# res = action.call()

# import requests
# import json
# url = "http://192.168.8.24:8080/zstack/v1/api-jobs/269738af3f5144ea98dc4ca0bbf7ff51"
# response = requests.get(url=url)
# result = json.loads(response.text)
# rules = result.get("inventory").get("rules")
# ruleuuid = ""
# print(rules)
# for rule in rules:
#     if rule.get("startPort")==200 and rule.get("endPort")==300 and rule.get("type")=="Egress":
#         ruleuuid = rule.get("uuid")
# print(ruleuuid)

action = AddSecurityGroupRuleAction()
action.securityGroupUuid = "c97e486e16584adebedf4ff872912e5b"
action.remoteSecurityGroupUuids = ["c97e486e16584adebedf4ff872912e5b"]
ru = {'type': 'Ingress', 'startPort': '520', 'endPort': '1314', 'protocol': 'TCP', 'allowedCidr': '192.168.9.0/24'}
action.rules = [ru]
action.sessionId = sessionId()
res = action.call()

condi=['protocol=TCP', 'type=Ingress', 'startPort=520', 'endPort=1314', 'allow_network=192.168.2.0/24', 'securityGroupUuid=7efe1c0b894d42a49af25d9f9beadf7e']
action = QuerySecurityGroupRuleAction()
action.conditions =['type=Ingress', 'startPort=520', 'endPort=1314', 'protocol=TCP', 'allowedCidr=192.168.10.0/24', 'securityGroupUuid=e17e5bd2a6a74c8a8b89123cf576f0d7']
action.sessionId = sessionId()
res = action.call()