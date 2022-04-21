l=['a','b','c','d','e','f']

#enumerate()返回的是一个enumerate对象,利用它可以同时获得index和value
d = dict(enumerate(l))
print(d.get(3))