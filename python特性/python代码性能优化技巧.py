from time import time

"""一:改进算法,选择合适的数据结构,优化时间复杂度"""

# 1.使用dict查找元素而不是list,或者set(list)
"""
dict使用了hash table，因此查找操作时间复杂度为O(1),
list实际是个数组,O(n)
"""
t = time()
list_demo = ['a', 'b', 'is', 'python', 'jason', 'hello', 'phone', 'test', 'apple', 'ind', 'var', 'bana']
# list_demo = dict.fromkeys(list,True)
filter = []
for i in range(1000000):
    for find in ['is', 'hat', 'new', 'list', 'old', '.']:
        if find not in list_demo:
            filter.append(find)
print('花费时间:', time() - t)

# 2.使用set求交集而不是list
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 34, 53, 42, 44]
listb = [2, 4, 6, 9, 23]
intersection = []
# 使用list
for i in range(100):
    for a in lista:
        for b in listb:
            if a == b:
                intersection.append(a)
# 使用set
for i in range(100):
    list(set(lista) & set(listb))

# 3.字符串优化
# (使用join而不是+)
# (字符串可以使用正则表达式或者内置函数来处理时候,选择内置函数，如str.startswith)

# 4.使用列表解析(要比在循环中重新构建一个新的 list 更为高效),推导式或生成器表达式


# 5.合理使用copy,deepcopy(deepcopy使用递归复制,慢一个数量级)

# 6.在循环开始之前:设置一个局部变量保存一个函数的全局引用(或其他模块)(字典查询在大量调用时会降低性能)
# python访问一个变量,函数或模块时步骤:1.查找本地变量locals(),2.查找全局变量globals(),3.查找__builtin__模块对象(实际上在模块对象的locals()查找)
# 7.其他
# xrange代替range(python3：range代替xrange)
# 使用局部变量,避免global，局部变量比全局变量快
# is运算符比==速度快,能用is情况尽量使用
# if done is not None 比 if done !=None快,if done is True比if done ==True快一倍
# (交换变量值:a,b=b,a)
# while 1比while True快(后者可读性强，True是一个全局变量而非关键字)
# 内建函数通常较快,add(a,b)优于a+b
# 优化循环:循环外能做的事放在循环外面
# 优化包含多个判断(对于and，应该把满足条件少的放在前面，对于or，把满足条件多的放在前面)ps:充分利用Lazy-evaluation
# 使用最佳的反序列化方式(eval,cPickle,json) json比cPickel快3倍,比eval快20倍
"""
终级大杀器：PyPy PyPy是用RPython(CPython的子集)实现的Python，根据官网的基准测试数据，它比CPython实现 的Python要快6倍以上。
快的原因是使用了Just‑in‑Time(JIT)编译器，即动态编译器，与静态编译 器(如gcc,javac等)不同，它是利用程序运行的过程的数据进行优化。
由于历史原因，目前pypy中 还保留着GIL，不过正在进行的STM项目试图将PyPy变成没有GIL的Python。
如果python程序中含有C扩展(非cffi的方式)，JIT的优化效果会大打折扣，甚至比CPython慢（比 Numpy）。
所以在PyPy中最好用纯Python或使用cffi扩展。 随着STM，Numpy等项目的完善，相信PyPy将会替代CPython。
"""