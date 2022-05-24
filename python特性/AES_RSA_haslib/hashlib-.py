import hashlib

da = "望太微兮穆穆"
# 1.
print(hashlib.md5(da.encode('utf8')).hexdigest())
print(hashlib.sha1(da.encode('utf8')).hexdigest())
print(hashlib.sha224(da.encode('utf8')).hexdigest())
print(hashlib.sha256(da.encode('utf8')).hexdigest())
print(hashlib.sha384(da.encode('utf8')).hexdigest())
print(hashlib.sha512(da.encode('utf8')).hexdigest())
print(hashlib.md5(da.encode()))

# 2.
m = hashlib.md5()
m.update(da.encode('utf-8'))
print(m.hexdigest())

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
