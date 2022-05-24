#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-4-6 下午9:25
"""
_zap=12c8557d-e38e-4e2d-9c25-74787c86901e; d_c0="AGDkJL24GQ-PTvsL_Mj6FtQbwZki7ByELcs=|1552204187"; q_c1=cd553a0df4bb40f6a0b8699b865c608b|1552204189000|1552204189000; __gads=ID=894f7e707e297a98:T=1553668216:S=ALNI_MaPRnvsjxuOOOXT95J1B1NBxcR8ew; tgw_l7_route=7bacb9af7224ed68945ce419f4dea76d; _xsrf=oNpnAsEQwSFDBVtvacZ5Nx7LNYORYEjo; capsion_ticket="2|1:0|10:1554556989|14:capsion_ticket|44:YzRkNzdkOTU3Y2QyNGEyOWE5OThkYTU0ZjgwYWY1Nzg=|3290d123c445e2967e2363b6716a56cf1216e82b0926631b335762962e91df50"; z_c0="2|1:0|10:1554556997|4:z_c0|92:Mi4xRkM1MUFnQUFBQUFBWU9Ra3ZiZ1pEeVlBQUFCZ0FsVk5SZmFWWFFCaDBzVFBiYlllMWN4ZzBaSm5rTERDQ3RkM3p3|f574abaf07285719c04b3209b87c293b76388238ed7bb0c96c38fbf867b3f556"; tst=r

"""
import requests
import re
import urllib3
headers={
    'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/2010',
    'Cookie':'_zap=12c8557d-e38e-4e2d-9c25-74787c86901e; d_c0="AGDkJL24GQ-PTvsL_Mj6FtQbwZki7ByELcs=|1552204187"; q_c1=cd553a0df4bb40f6a0b8699b865c608b|1552204189000|1552204189000; __gads=ID=894f7e707e297a98:T=1553668216:S=ALNI_MaPRnvsjxuOOOXT95J1B1NBxcR8ew; tgw_l7_route=7bacb9af7224ed68945ce419f4dea76d; _xsrf=oNpnAsEQwSFDBVtvacZ5Nx7LNYORYEjo; capsion_ticket="2|1:0|10:1554556989|14:capsion_ticket|44:YzRkNzdkOTU3Y2QyNGEyOWE5OThkYTU0ZjgwYWY1Nzg=|3290d123c445e2967e2363b6716a56cf1216e82b0926631b335762962e91df50"; z_c0="2|1:0|10:1554556997|4:z_c0|92:Mi4xRkM1MUFnQUFBQUFBWU9Ra3ZiZ1pEeVlBQUFCZ0FsVk5SZmFWWFFCaDBzVFBiYlllMWN4ZzBaSm5rTERDQ3RkM3p3|f574abaf07285719c04b3209b87c293b76388238ed7bb0c96c38fbf867b3f556"; tst=r',

}
session=requests.Session()
response=session.get('https://www.zhihu.com/people/centyuan/',headers=headers)
print(response.text)

