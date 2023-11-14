import hashlib

# da = "望太微兮穆穆"
da = "https://www.yedanrongqi.com.cn"
da = "94:83:c4:1b:6e:9e"
# 1.基本操作
print('hhh:', hashlib.md5(da.encode('utf8')).hexdigest(), len(hashlib.md5(da.encode('utf8')).hexdigest()))
print(hashlib.sha1(da.encode('utf8')).hexdigest())
print(hashlib.sha224(da.encode('utf8')).hexdigest())
print(hashlib.sha256(da.encode('utf8')).hexdigest())
print(hashlib.sha384(da.encode('utf8')).hexdigest())
print(hashlib.sha512(da.encode('utf8')).hexdigest())
print(hashlib.md5(da.encode()))

# 2.
m = hashlib.md5()
m.update(da.encode('utf-8'))
print("2:", m.hexdigest())
ms = "8bcfaaac9ccc3768596b72ba34d5dc77"
if ms == m.hexdigest():
    print(len(ms))
# 3

from hashlib import md5


def md5_sign(dict_map, key):
    """md5加密算法"""
    d = sorted(dict_map.items(), key=lambda x: x[0])
    list_l = []
    for i in range(len(d)):
        k, v = d[i]
        if i == 0:
            str1 = k + "=" + v
            list_l.append(str1)
        else:
            str2 = "&" + str(k) + "=" + str(v)
            list_l.append(str2)
    content = ''.join([str(i) for i in list_l])
    con = content + "&key={}".format(key)
    m = md5()
    m.update(con.encode(encoding='UTF-8'))
    sign = m.hexdigest()
    return sign.upper(), content


with open('s.txt', 'rb') as fd:
    data = fd.read()
    hs = hashlib.md5(data).hexdigest()
    print(hs)

# 4.base64编码
import base64

encode_str = base64.b64encode("centyuan.com".encode("utf-8"))  # 参数为byte,先使用encode
print(encode_str.decode("utf-8"))  # Y2VudHl1YW4uY29t

