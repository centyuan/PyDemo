#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-9-6 下午8:29

class Node:
    def __init__(self,data):
        self.data = data #表示对应的元素值
        self.next = None #表示下一个链接的lian点

#单链表
class Linked_List:
    def __init__(self,head=None): #默认参数
        self.head =head

    def append(self,node):
        #将头结点指向临时变量
        current =self.head
        #头结点存在时
        if self.head:
            #循环遍历到链表最后一个元素
            while current.next:
                current =current.next
            current.next = node
        #头结点不存在时
        else:
            self.head = node

    def is_empty(self):
        """
        判断链表是否为空
        :return:
        """
        return  bool(self.head)

    def insert(self,position,node):
        if position <0 or position>self.get_length():
            raise  IndexError('insert插入时，key超出了范围')
        temp = self.head
        #遍历找到position位置
        if position == 0:
            node.next = temp
            self.head = node
        i = 0
        while i < position:
            pre ,temp =temp,temp.next
            i +=1
        pre.next =node
        node.next =temp

    def remove(self,position):
        if position < 0 or position > self.get_length():
            raise IndexError("删除元素的索引超出了链表的范围")
        i = 0
        temp =self.head
        while temp:
            if position ==0:
                self.head = temp.next
                temp.next =None #从链表中删除这个结点
                return
            pre ,temp = temp,temp.next #遍历
            i +=1
            if i == position:
                pre.next = temp.next
                temp.next = None #从链表中删除这个结点
                return

    def get_length(self):
        """
        返回链表的长度
        :return:
        """
        temp = self.head

        length = 0
        while temp:
            length +=1
            temp = temp.next
        return length

    def print_list(self):
        """
        遍历链表，并将元素依次打印出来
        :return:
        """
        print("linked_list:")
        temp =self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def reverse(self):
        """
        将链表反转
        :return:
        """
        prev = None
        current =self.head
        while current:
            next_node = current.next #记录下一个结点

            current.next = prev #将现在结点的next->上一个结点
            prev = current     #prev向前移动1
            current =next_node #current也向前移动1
        self.head = prev

    def initlist(self,data_list):
        """
        将列表转化为链表
        :param data_list:
        :return:
        """
        #创建头结点
        self.head =Node(data_list[0])
        temp = self.head
        #循环为每个创建结点，建立链表
        for data in data_list[1:]:
            node = Node(data)
            temp.next = node
            temp = temp.next

#双向链表

class Node(object):
    def __init__(self,item):
        self.data = item
        self.next = None
        self.prev = None

class DLinkList(object):
    def __init__(self):
        self._head =None

    def is_empty(self):
        #判断链表是否为空
        return  self._head == None

    def get_length(self):
        #返回链表长度
        cur = self._head
        count = 0
        while cur:
            count +=1
            cur = cur.next
        return count

    def travel(self):
        #遍历链表
        cur = self._head
        while cur:
            print(cur.data)
            cur = cur.next

    def add(self,item):
        #头部插入数据
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

    def append(self,item):
        #尾部插入数据
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            #循环到链表尾部的结点位置
            cur = self._head
            while cur.next:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def search(self,item):
        #查找元素是否存在
        cur = self._head
        while cur:
            if cur.data == item:
                return  True
            cur = cur.next
        return False

    def insert(self,pos,item):
        #在指定位置添加节点
        #在头部插入
       if pos <=0:
           self.add(item)
        #在尾部插入
       elif pos > (self.get_length()-1):
           self.append(item)

       else:
           node = Node(item)
           cur = self._head
           count = 0
           #移动到指定位置的前一个位置
           while count < (pos-1):
               count +=1
               cur =cur.next
           node.prev = cur
           node.next = cur.next
           cur.next.prev = node
           cur.next = node

    def remove(self,item):
        #删除元素
        if self.is_empty():
            return
        else:
            cur = self._head
            if cur.data == item:
                if cur.next:
                    cur.next.prev = None
                    self._head = cur.next
                else:
                    self._head = None
            while cur:
                if cur.data == item:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    break
                cur = cur.next

#例子1:
#给定两个值，如果这两个值都在单链表的链点中，即交换这两个链点在单链表的位置。
"""
Sulotion:
要交换的d1,d2，在声明D1,D2
d1=D1,d2=D2,再改变索引的位置

"""
class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None

    def print_list(self):  # 遍历链表，并将元素依次打印出来
        print("linked_list:")
        temp = self.head
        new_list = []
        while temp is not None:
            new_list.append(temp.data)
            temp = temp.next
        print(new_list)

    def insert(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def swapNodes(self,d1,d2):
        prevD1 = None
        prevD2 = None
        if d1 == d2:
            return
        else:
            D1 = self.head
            #循环判断不相等时，相等就跳出循环
            while D1 and D1.data != d1:
                prevD1 = D1
                D1 = D1.next
            D2 = self.head
            while D2 and D2.data != d2:
                prevD2 = D2
                D2 = D2.next
            #1.如果都没有找到
            if not D1 or not D2:
                return
            #2.交换pre
            if prevD1:
                prevD1.next = D2
            else:
                self.head = D2
            if prevD2:
                prevD2.next = D1
            else:
                self.head = D1
            #3.交换next
            temp = D1.next
            D1.next = D2.next
            D2.next = temp

if __name__ == '__main__':
    list = Linkedlist()
    list.insert(5)
    list.insert(4)
    list.insert(3)
    list.insert(2)
    list.insert(1)
    list.print_list()
    list.swapNodes(1, 4)
    print("After swapping")
    list.print_list()