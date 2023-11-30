"""
collections模块是Python内建的一个集合模块,提供很多有用的集合类和方法

namedtuple: 创建一个命名元组子类的工厂函数
deque: 高效增删改双向队列,实现了在两端快速添加(append)弹出(pop)
defaultdict: 为不存在的key提供一个默认值
OrderedDict: 有序字典
Counter: 计数功能
ChainMap： 类似字典(dict)的容器类，将多个映射集合到一个视图里面
UserDict：
UserList：
UserString：

"""

# 1.namedtuple命名元组
from collections import namedtuple

point = namedtuple("Points", "x y")
p1 = point(2, 2)  # p1类型是point也是tuple类型
# 赋值
p1._make([5, 5])
# 改值
p1._replace(x=10)

# deque双端队列
"""
double-end queue双端队列,支持线程安全,在两端近视 O(1)的插入和删除元素‘
存储数据空间是由一段一段等长的连续空间构成,各段空间不一定连续,deque容器使用数组存储着各个连续空间的首地址
deque容器分段存储结构,提高了在序列两端添加或删除元素的效率，也是该容器迭代器的底层实现变得复杂

底层实现:
{
    iterator start;   // start迭代器，start 迭代器记录着 map 数组中首个连续空间的信息
    iterator finish;  // finish迭代器，finish 迭代器记录着 map 数组中最后一个连续空间的信息
    map map_pointer;  // 指针数组
}

struct __deque_iterator {
    T* cur;      //指向当前正在遍历的元素
    T* first;    //指向当前连续空间的首地址
    T* last;     //指向当前连续空间的尾地址
    map_pointer node; // 指向map数组中存储的指向当前连续空间的指针
}

方法:
append():右端添加元素
appendleft():左端添加元素
extend():
extendleft():
pop():
popleft():
count():统计元素个数
insert(index,obj):指定位置插入元素
rotate():从右侧反转n步，如果n为负数，则从左侧反转
clear():元素全部删除
remove():移除第一次出现的元素，没找到报ValueError
maxlen():deque限定的最大长度,没有返回None,超出长度另一边会被删除
几种对比:https://blog.csdn.net/qq_28304687/article/details/79088491
"""
from collections import deque
