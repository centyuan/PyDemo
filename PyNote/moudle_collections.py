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
from collections import deque
