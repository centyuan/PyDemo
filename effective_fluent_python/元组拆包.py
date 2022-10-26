"""
元组拆包可以应用到任何可迭代对象上，唯一的硬性要求是，被可迭代对象
中的元素数量必须要跟接受这些元素的元组的空档数一致。除非我们用* 来
表示忽略多余的元素
"""
# 元组拆包
# 1:(分别赋值)
city, year, pop, chg, area = ('Tokyou', 2003, 32450, 0.66, 8014)

# 2:
traveler_ids = [('USA', '31157633'), ('BRA', 'CE232234'), ('ESP', 'XDA23222')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

# 多余元素赋值给占位符 _
for country, _ in traveler_ids:
    print(country)

# 3: a,b=b,a # 很优雅的写法

# 4:* 运算符把一个可迭代对象拆开作为函数的参数
# divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组
divmod(20, 8)
t = (20, 8)
quotiment, remainder = divmod(*t)

# 5:平行赋值(python3中)
a, b, *args = range(5)
# (0,1,[2,3,4])
a, *body, c, d = range(5)
# (0,[1,2],3,4)

# 6:嵌套元组拆包获取经度
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),  # ➊
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))
