'''
all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
元素除了是 0、空、None、False 外都算 True。

'''


class Solution:

    def isSubsequence(self, s, t):
        t = iter(t)

        return all(c in t for c in s)


t = 'to be or not to be'
s = 'to be or'
t = iter(t)

# str = 'abcdefg'
# st = iter(str)
# if 'a' in st:
#     print('a') #输出:a
# if 'b' in st:
#     print('b') #输出:b
# if 'f' in st:
#     print('f')
#     print(next(st)) #输出: f g

gene = (c in t for c in s)  # 生成器
while True:
    try:
        print(next(gene))
    except StopIteration:
        break
