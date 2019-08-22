#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-8-12 下午11:06

from urllib.parse import parse_qs

test_str = 'red=5&blue=0&green='
my_value = parse_qs(test_str,keep_blank_values=True)
print(my_value)


#---before 5
