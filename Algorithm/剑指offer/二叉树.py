# ！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-9-7 下午10:24

# 满二叉树：树中除了叶子节点，每个节点都有两个子节点
# 完全二叉树：在满二叉树上，最后一层的叶子节点均在最左边
# 完美二叉树：在完全二叉树上，树的叶子节点均在最后一层(也就是一个完美的三角形)

# 二叉搜索树(二叉查找树，二叉排序树)：对于树中任何节点，如果其左子节点不为空，那么该节点的value值永远 >= 其左子节点；
# 如果其右子节点不为空，那么该节点的value值永远 <= 其右子节点

# 平衡二叉树定义(AVL)：它或者是一颗空树，
# 或者具有以下性质的二叉排序树：它的左子树和右子树的深度之差(平衡因子)的绝对值不超过1，且它的左子树和右子树都是一颗平衡二叉树。
# 条件一：它必须是二叉查找树。
# 条件二：每个节点的左子树和右子树的高度差小于等于1。
# 高度相差太大，会让二叉排序树操作的时间复杂度升级为O(n)

# 红黑树是一个平衡二叉查找树:
# 1.根节点是黑色，叶子节点是不存储数据的黑色空节点
# 2.任何相邻的两个节点不能同时为红色
# 3.任意节点到其可到达的叶子节点间包含相同数量的黑色节点
"""
红黑树是一种特化的AVL树
"""

"""
def delete()
    先获取待删除节点 item 的父节点。
        如果父节点不为空，判断 item 的左右子树：
            如果左子树为空，那么判断 item 是父节点的左孩子，还是右孩子；
                如果是左孩子，将父节点的左指针指向 item 的右子树，反之将父节点的右指针指向 item 的右子树。
            如果右子树为空，那么判断 item 是父节点的左孩子，还是右孩子；
                如果是左孩子，将父节点的左指针指向 item 的左子树，反之将父节点的右指针指向 item 的左子树。
            如果左右子树均不为空，寻找右子树中的最左叶子节点 x ，将 x 替代要删除的节点。
        删除成功，返回 True。
        删除失败, 返回 False。
"""


class Node(object):
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.item)  # print一个Node类时会打印__str__的返回值


class Tree(object):
    def __init__(self):
        self.root = Node('root')

    # 添加
    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]
            while True:
                pop_node = q.pop(0)
                if pop_node.left is None:  # 左子树为空，添加到左子树
                    pop_node.left = node
                elif pop_node.right is None:  # 右子树为空，添加到右子树
                    pop_node.right = node
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)

    # 找到item的父节点
    def get_parent(self, item):
        if self.root.item == item:
            return None  # 根节点没有父节点
        temp = [self.root]
        while temp:
            pop_node = temp.pop(0)
            if pop_node.left and pop_node.left.item == item:
                return pop_node
            if pop_node.right and pop_node.right.item == item:
                return pop_node

            if pop_node.left:
                temp.append(pop_node.left)
            if pop_node.right:
                temp.append(pop_node.right)
        return None

    # 删除
    def delete(self, item):
        if self.root is None:  # 如果根为空，就什么也不做
            return False
        parent = self.get_parent(item)
        if parent:
            del_node = parent.left if parent.left.item == item else parent.right  # 待删除节点
            if del_node.left is None:
                if parent.left.item == item:
                    parent.left = del_node.right
                else:
                    parent.right = del_node.right
                del del_node
                return True
            elif del_node.right is None:
                if parent.left.item == item:
                    parent.left = del_node.left
                else:
                    parent.right = del_node.left
                del del_node
                return True
            else:  # 左右子树都不为空,需要寻找后继节点
                tmp_pre = del_node
                tmp_next = del_node.right
                if tmp_next.left is None:
                    # 替代
                    tmp_pre.right = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right

                else:
                    while tmp_next.left:  # 让tmp指向右子树的最后一个叶子
                        tmp_pre = tmp_next
                        tmp_next = tmp_next.left
                    # 替代
                    tmp_pre.left = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                if parent.left.item == item:
                    parent.left = tmp_next
                else:
                    parent.right = tmp_next
                del del_node
                return True
        else:
            return False


