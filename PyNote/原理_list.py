
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