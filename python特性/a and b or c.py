# -*- coding:utf-8 -*-

val1=1
val2=3
intval=1

print("a if b>1 else c:" ,val1 if intval >1 else val2)
print("a and b or c:",intval>1 and val1 or val2)
vax=val1 if intval >1 else val2
print(vax)
print(type(vax))
# "a and b or c" 这是 Python 里经常用到的很方便的一个表达式，被用的很频繁。
#
# intval > 1 and val1 or val2
# 如果 intval > 1 表达式为真返回 val1 否则返回 val2 (其中vla1必须为真)
# 但这只是其中一种逻辑。
# (intval > 1 and val1) or val2
# 如上：如果 val1 是逻辑否，那么就会返回 val2 ，当你就是想返回一个逻辑否的值时，比如 (0,[],{},False,''),那么这个表达式就不能这么用了。
#
# 应该用：
#
# val1 if intval > 1 else val2
itms=[1,2,3,4,5,6]
#item for item in items:
#and 有一个为假就为假，全为真为真
#or 有一个为真为真，全为假为假