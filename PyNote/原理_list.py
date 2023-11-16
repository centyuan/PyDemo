
"""
Python的列表是一种动态数组,数组中每个元素都一个指向存储真实数据的指针
扩容时会重新分配一块更大的内存空间,并将原来的值复制到新内存空间,这种实现方式使列表的随机访问非常高效
但在插入和删除元素时需要移动大量的数据，效率较低

"""

# 1.C结构体
'''
typedef struct {
    PyObejct_VAR_HEAD
    PyObject **ob_item;
    Py_ssize_t allocated;
}PyListObject;

ob_item:指向列表对象的指针数组
allocated:申请内存的槽的个数(通常分配的槽的大小大于列表的大小,为了避免每次列表添加元素的时候调用分配内存的函数扩容)

append:追加元素的操作平均复杂度为  O(1)
insert:插入操作平均复杂度为 O(n)
pop：取出最后一个的平均复杂度为 O(1)
remove: 删除指定元素的复杂度为 O(n)

'''
# 2.元组和list区别
'''
元组c结构体:
typedef struct {
    PyObject_VAR_HEAD
    PyObject *ob_item[1];
}PyTupleObject;

区别:
列表是动态的，属于可变序列，可以使用[append](https://link.zhihu.com/?target=https%3A//www.olzz.com/tag/append/)()、[extend](https://link.zhihu.com/?target=https%3A//www.olzz.com/tag/extend/)()、[insert](https://link.zhihu.com/?target=https%3A//www.olzz.com/tag/insert/)()、remove()和pop()等方法实现添加和[修改列表](https://link.zhihu.com/?target=https%3A//www.olzz.com/tag/xiugailiebiao/)元素，

元组是静态的，属于不可变序列，无法增加、删除、修改元素，除非整体替换

元组比列表更轻量:
1.元组占用空间更小(空的小16字节，列表是动态数组，会额外预留一部分空间，元组空间大小固定)
2.元组初始化速度快5倍(python -m timeit "x=(1,2,3)" 和 python -m timeit "x=[1,2,3]")
3.元组的访问速度快2倍
4.元组可以在字典中作为键
5.元组底层也是数组，但是做了优化(为了避免效率,避免频繁调用系统函数free,malloc向系统释放申请空间,tuple源文件中定义了一个free_list,所有申请过的，小于一定大小的元组，
在释放的时候会被放进这个 `free_list` 中以供下次使用。也就是说，如果以后需要再去创建同样的 `tuple`，Python 就可以直接从缓存中载入)
static PyTupleObject *free_list[PyTuple_MAXSAVESIZE];
'''
