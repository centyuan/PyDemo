#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-3-29 下午6:39
'''
题目描述
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
'''
"""
层次遍历
def traversel(root):
    if root is None:
        return None
    q=[root]
    res=[root.data]
    while q !=[]:
        pop_node=q.pop(0)
        if pop_node.left:
            q.append(pop_node.left)
            res.append(pop_node.left.data)
        if pop_node.right:
            q.append(pop_node.right)
            res.append(pop_node.right.data)
    return res
"""

#1按序获取每一层结点的值
#2将偶数层的值倒序
class Solution:
    def Print(self,pRoot):
        resultArray = []
        if not pRoot:  # 是否为空
            return resultArray
        curLayerNodes = [pRoot]
        isEvenLayer = True#是否需要倒序
        while curLayerNodes:
            curLayerValues = []#这层值取空
            nextLayerNodes = []#这层结点取空
            isEvenLayer = not isEvenLayer
            for node in curLayerNodes:
                curLayerValues.append(node.val)#将该节点值压入
                if node.left:
                    nextLayerNodes.append(node.left)
                if node.right:
                    nextLayerNodes.append(node.right)
            curLayerNodes = nextLayerNodes
            resultArray.append(curLayerValues[::-1]) if isEvenLayer else resultArray.append(curLayerValues)
        return resultArray
