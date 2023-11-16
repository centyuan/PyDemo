"""
Python中字典是通过hash表来实现的

字典:底层依靠hash table实现(将键通过散列函数转变成了一个列表的索引),
hash冲突解决办法:
1.开放地址法:冲突时去寻找新的空闲的地址(1.线性探测法:加1取模向后查找,2.平方探测法:前后寻找二次探测)
2.再哈希法:同时构造多个不同的哈希函数
3.链地址法:将所有哈希地址相同的记录都链接在同一个链表中
4.建立公共溢出区:将哈希表分为基本表和溢出表,发生冲突的都存放在溢出表
Question: 使用hash获取键的散列值,散列值对数组长度取余,就是存放位置的索引,索引可能相同而冲突?
Answer: 使用开放寻址法解决冲突


字典是否有序?
Python3.5以前:字典是不能保证插入顺序的，底层使用一个二维数组
创建字典: 初始化一个二维数组,8行3列,字典的键值对数量超过当前数组的2/3时，数组会进行扩容
往字典添加一个值: hash(key) & 掩码 或(hash(key)后的值对8取余数)，余数为二维数组的索引，二维数组记录该索引(hash值，key的内存地址,vlaue的内存地址)
取值: hash(key)后的值对8取余数，余数为二维数组的索引

Python3.6后:字典插入有序了，且占用内存空间变小了,底层使用两个一维数组
创建字典: 
indices = [None,None,None,None,None，None，None，None]
entries = 二维数组(hash值，key的内存地址,value的内存地址)
往字典添加一个值: hash后取余后的值为indices上的索引,在该索引上记录entries存值的索引
插入新的数据只在entries后面添加数据,确保了插入的顺序

"""

# 1.c结构体
'''
typedef struct {
    Py_ssize_t me_hash;
    PyObject *me_key;
    PyObject *me_value;
}PyDictEntry;
存储内容有 hash，key，value

'''