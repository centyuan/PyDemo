"""
堆 (heap) 是一种经过排序的完全二叉树，其中任一非叶子节点的值均不大于（或不小于）其左孩子和右孩子节点的值。

最大堆 根结点的键值是所有堆结点键值中最大者。

最小堆 根结点的键值是所有堆结点键值中最小者。
"""


class heap(object):

    def __init__(self):
        # 初始化一个空堆，使用数组来在存放堆元素，节省存储
        self.data_list = []

    def get_parent_index(self, index):
        # 返回父节点的下标
        if index == 0 or index > len(self.data_list) - 1:
            return None
        else:
            return (index - 1) >> 1  # 二进制形式右移1位

    def swap(self, index_a, index_b):
        # 交换数组中两个元素
        self.data_list[index_a], self.data_list[index_b] = self.data_list[index_b], self.data_list[index_a]

    def insert(self, data):
        # 先把元素放在最后，然后从后往前依次堆化
        # 这里以大顶堆为例，如果插入元素比父节点大，则交换，直到最后
        self.data_list.append(data)
        index = len(self.data_list) - 1
        parent = self.get_parent_index(index)
        # 循环，直到该元素成为堆顶，或小于父节点（对于大顶堆)
        while parent is not None and self.data_list[parent] < self.data_list[index]:
            # 交换操作
            self.swap(parent, index)
            index = parent
            parent = self.get_parent_index(parent)

    def removeMax(self):
        # 删除堆顶元素，然后将最后一个元素放在堆顶，再从上往下依次堆化d
        remove_data = self.data_list[0]
        self.data_list[0] = self.data_list[-1]
        del self.data_list[-1]

        # 堆化
        self.heapify(0)
        return remove_data

    def heapify(self, index):
        # 从上往下堆化，从index 开始堆化操作 (大顶堆)
        total_index = len(self.data_list) - 1
        while True:
            maxvalue_index = index
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
