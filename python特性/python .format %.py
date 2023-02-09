# ！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan

# 1.%
# 打印字符串
print("his name is %s" % ("centyuan"))
# 打印整数
print("He is %d years old" % (25))
# 打印浮点数
print("His height is %f m" % (1.83))
# 打印浮点数（指定保留小数点位数）
print("His height is %.2f m" % (1.83))
# .指定占位符宽度
print("Name:%10s Age:%8d Height:%8.2f" % ("Aviad", 25, 1.83))
# 2。format
"{} {}".format("hello", "world")  # 不设置指定位置，按默认顺序
# 'hello world'
"{1} {0} {1}".format("hello", "world")  # 设置指定位置
# 'world hello world'
# 3.格式化 f''    python3.6 后的版本支持
name = 'Tom'
age = 20
print(f'姓名是：{name},年龄是：{age}')
