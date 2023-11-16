"""
在于 lambda 表达式中的 x 是一个自由变量，在运行时绑定值，而不
是定义时就绑定，这跟函数的默认值参数定义是不同的。因此，在调用这个 lambda 表
达式的时候，x 的值是执行时的值

"""
# 1.函数执行时，捕获到值
x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y
print(a(10))  # 30
print(b(10))  # 30

# 2. 函数定义时捕获值(使用默认参数)
x1 = 10
a1 = lambda y, x=x1: x + y
x1 = 20
b1 = lambda y, x=x1: x + y
print(a1(10))  # 20
print(b1(10))  # 30