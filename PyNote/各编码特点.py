# 1.URL编码,以%开头
import json
from urllib import parse

ss = "http://www.baidu.com"
print(parse.quote(ss))  # 编码:http%3A//www.baidu.com
# print(parse.unquote()) 解码

# 2.Unicode,以&#(&#X为Unicode 16进制)
# &#20170;&#20599;

# 3.UTF-8,以\u开头
e = '\u89e3\u6790\u5305\u5f02\u5e38'
# 显示为中文
print("\u89e3\u6790\u5305\u5f02\u5e38")  # 解析包异常
# 显示为中文
result = e.encode("utf-8").decode()

# 4.base64 编码,以=结尾
