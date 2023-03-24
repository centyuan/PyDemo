#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-5-24 下午3:49
""""
题目描述
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

"""
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def Print(self,pRoot):
        if not pRoot:
            return []
        resultList=[]
        currentLayer=[pRoot]
        while currentLayer:
            curerntList=[]
            nextLayer=[]
            for node in currentLayer:
                curerntList.append(node.val)
                if node.left:
                    nextLayer.append(node.left)
                if node.right:
                    nextLayer.append(node.right)
            currentLayer=nextLayer
            resultList.append(curerntList)
        return resultList

    def Print2(self, pRoot):
        if not pRoot:
            return []
        resultList = []
        curLayer = [pRoot]
        while curLayer:
            curList = []
            nextLayer = []
            for node in curLayer:
                curList.append(node.val)
                if node.left:
                    nextLayer.append(node.left)
                if node.right:
                    nextLayer.append(node.right)
            resultList.append(curList)
            curLayer = nextLayer
        return resultList

