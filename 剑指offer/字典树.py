#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-9-8 下午7:28
"""
字典树，又称单词查找树，Trie 树，是一种树形结构，是一种哈希树的变种。
典型应用是用于统计，排序和保存大量的字符串（但不仅限于字符串），所以经常被搜索引擎系统用于文本词频统计。
它的优点是：利用字符串的公共前缀来减少查询时间，最大限度地减少无谓的字符串比较，查询效率比哈希树高。
字典树的主要性质
它有 3 个基本性质：

1.根节点不包含字符，除根节点外每一个节点都只包含一个字符；
2.从根节点到某一节点，路径上经过的字符连接起来，为该节点对应的字符串；
3.每个节点的所有子节点包含的字符都不相同
"""

class TrieNode(object):
    def __init__(self):
        self.nodes = dict()
        self.is_leaf = False

    #插入一个字到字典树中 word:str  type hints特性
    def insert(self,word:str):
        curr = self

        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr = curr.nodes[char]
        curr.is_leaf = True

    #插入一列表的字到字典树中
    def insert_many(self,words:[str]):
        for word in  words:
            self.insert(word)

    #在字典树里面查询一个字
    def search(self,word:str):
        curr = self
        for char in word:
            if char not in curr.nodes:
                return  False
            curr = curr.nodes[char]

        return  curr.is_leaf





