# method-1
# 使用dir()函数查看对象的属性列表，如果只有__iter__()函数则是可迭代的，如果__iter__()和__next__()函数都有则是迭代器。

lst = ['Today is Wednesday', 'Tomorrow is Thursday', 'The day after tomorrow is Friday']
it = lst.__iter__()
print(dir(lst))
print(dir(it))

# method-2
# 使用isinstance() 函数来判断一个对象是否是一个已知的类型
from collections import Iterator,Iterable
print(isinstance(lst, Iterable))  #
print(isinstance(it, Iterator))  #


# 案例 删除字典value为空的键值对
data_info = {
    'account': 1,
    'remark': 2,
    'sort': '',
    'weight': '',

}
# 下面报错data_info.keys()返回迭代器，在迭代器遍历时候不能删除
for key in data_info.keys():
    if not data_info.get(key):
        del data_info[key]