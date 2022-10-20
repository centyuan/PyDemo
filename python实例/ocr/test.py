# from DecryptLogin import login
#
# # the instanced client
# client = login.Client()
# # the instanced weibo
# weibo = client.weibo(reload_history=True)
# # use the login function to login in weibo
# infos_return, session = weibo.login('me', 'pass', 'scanqr')
from collections import defaultdict

print(dict.fromkeys(range(1,9)))  # {'a': None, 'b': None}
see =['' for i in range(1,9)]
print(dict([(i,'') for i in range(1,9)]))

dict4 = defaultdict(list)
for k,v in dict4.items():
    print(',',k,v)