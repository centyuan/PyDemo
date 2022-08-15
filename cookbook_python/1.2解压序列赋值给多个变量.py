"""
解压

"""
# 1.可变长元组
records = [
    ('foo',1,2),
    ('bar','hello'),
    ('foo',3,4),
]
for tag,*args in records:
    print(tag,args)

# 2. 解压元素丢弃
record = ('ACME',800,123,45,(12,18,2022))
name,*_,(*_,year) = record

# 3.解压后实现递归:来求和运算
items = [2,10,9,7,18,3]
def sum_(items):
    head,*tail =items
    return head + sum_(tail) if tail else head
print(sum_(items))