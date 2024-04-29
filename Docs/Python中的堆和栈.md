---
title: Python中的堆和栈
categories: 
   - Python从入门到放弃
tags: 
   - Python
---
### 1.堆和栈

堆(Heap)和栈(stack)一般有两层含义:

```text
(1)**数据结构中**,表示两种数据结构
(2)**操作系统中**,两种内存管理方式(系统对进程占用的内存空间的管理方式)
```

##### 1.1数据结构

**栈**:

```text
是一种操作受限的线性表,只能在一端(栈顶)插入/删除的操作,简称先进后出(First In Last Out)FILO。

分为顺序表/链式表,底层分别由数组/链表实现,区别在于数组地址连续,链表地址不连续。
```

**堆:**

```text
是一种满足父子节点关系(所有节点不大于或不小于其父节点)的完全二叉树,这一特性使其成为优先队列实现的基础。

分为大顶堆(根节点最大)/小顶堆(根节点最小),底层存储一般用数组实现。
```

##### 1.2操作系统

```text
(1).栈:**由操作系统分配释放**,程序运行时自动拥有的小块内存(在编译期有编译器决定大小)用于存储函数调用栈/局部变量等,且栈在内存中由高地址向低地址增长,所以栈的空间有限(window默认1MB,Linux默认10MB),一旦局部变量申请过多/函数调用太深(递归未终止),会导致栈溢出,操作系统会直接将程序杀掉,操作方式类似数据结构中的栈。
(2).堆:**由程序员分配释放**,若未释放,程序结束时由操作系统释放。
```

##### 1.3区别

```text
- 管理方式不同:栈由操作系统分配释放,堆需要手动申请释放(容易产生内存泄露)
- 空间大小不同:每个进程拥有的栈远远小于堆大小
- 分配方式不同:堆是按需申请,动态分配,速度较慢,容易产生内存碎片,栈(静态分配/动态分配:由操作系统完成,和堆动态分 配不同),速度较快.

使用栈:(像是去饭馆吃饭,只管点菜付钱,方便快捷,但是自由度小)

使用堆:(自己动手做饭,自由度大,想吃什么做什么,但是比较麻烦)
```

### 2.堆的代码实现

```python
class heap:
    def __init__(self,index):
        """初始化一个空堆,采用数组存放"""
        self.data = []
    def get_parent_index(self,index)
 		"""返回父节点下标"""
        if index ==0 or index >len(self.data)-1:
            return None
       	else:
            return (index-1)>>1  #二进制左移1位
	def sawp(self,index_a,index_b):
        """交换数组中两个元素"""
        self.data[index_a],self.data[index_b] = self.data[index_b],self.data[index_a]
    def insert(self,d):
        # 先把元素放入数组末尾,在进行上浮或下沉找到对应位置,以大顶堆为例,
        self.data.append(d)
        index = len(self.data)-1
        parent = self.get_parent_index(index)
         # 循环，直到该元素成为堆顶，或小于父节点（对于大顶堆)
        while parent is not None and self.data[parent] < self.data[index]:
            # 交換
            self.swap(parent,index)
            index = parent
            parent = self.get_parent_index(parent)
   
    def removeMax(self):
        """刪除栈顶元素"""
        remove_data = self.data[0]
        self.data[0]=self.data[-1]
        del self.data[-1]
        # 堆化
       	self.heapify(0)
        return remove_data
  
   	def heapify(self,index):
        """从上往下堆化,从index开始堆化"""
        total_index = len(self.data)-1
        while 1:
            max_value_index = index
            if 2 * index + 1 <= total_index and self.data_list[2 * index + 1] > self.data_list[maxvalue_index]:
                maxvalue_index = 2 * index + 1
            if 2 * index + 2 <= total_index and self.data_list[2 * index + 2] > self.data_list[maxvalue_index]:
                maxvalue_index = 2 * index + 2
            if maxvalue_index == index:
                break
            self.swap(index, maxvalue_index)
            index = maxvalue_index

    
"""
请将 元素 1-10 放进堆，并展示建堆情况，及删除堆顶元素情况
实例如下：

建堆: [10, 9, 6, 7, 8, 2, 5, 1, 4, 3]

删除堆顶元素： [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
"""
if __name__ == "__main__":
    myheap = heap()
    for i in range(10):
        myheap.insert(i + 1)
    print('建堆:', myheap.data_list)
    print("删除堆顶元素：", [myheap.removeMax() for _ in range(10)])
```

### 3.heapq常用方法

```python
"""
python中只有最小堆,没有最大堆,(可以在插入元素取反,弹出也取反实现最大堆)
"""
import heapq 
# 一:创建堆
#1.定义空列表,使用heapq.heqppush(item)将元素加入到堆
heap =[]
heapq.heappush(heap,3)
#2.使用heapq.heapify(list)将列表转为堆结
heap = [3,0,9,1]
heapq.heapify(heap) # [0, 1, 9, 3]
# 二:插入元素
num = 3
heapq.heappush(heap,num)
# 三:刪除并返回堆顶元素
heapq.heappop(heap,num)
# 四:查询堆中最小的n个元素
n = 3
heap =[1,3,5,7,2,4,6,8]
print(heapq.nsmallest(n,heap))
print(heapq.nlargeest(n,heap)) # 最大
# 五:合并两个有序列表
array_a = [6,9,10,14,18]
array_b = [3,5,13,19,20]
array_merge = heapq.merge(array_a,array_b) # 返回一个生成器
print(list(array_merge))
# [3, 5, 6, 9, 10, 13, 14, 18, 19, 20]
```

### 4.常用场景

- 实现优先级队列

```python
import heapq 
class PriorityQueue:
	def __init__(self):
        self._queue = []
        self._index = 0 
    def push(self,item,priority):
        # 默认由小到大,对priority取负
        # 存放元组
        heapq.heappush(self._queue,(-proority,self._index,item))
        self._index +=1
    
    def pop(self):
        return heapq.heappop(self._queue)[]
  
queue = PriorityQueue()
q.push("小米",1)
q.push("iphone",2)
q.push("ThinkPad",3)
q.push("Dell",4)
q.pop()
# Dell
```

- 合并两个有序数组:采用heapq.merge
- 获取k个最小值
