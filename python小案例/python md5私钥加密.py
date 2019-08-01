#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-7-22 下午8:10

from hashlib import  md5

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

