#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-8-13 下午8:09

#用列表推导来取代map和filter
a = [1,2,3,4,5,6,7,8]
squares = [x**2 for x in a] #列表推导
squares = map(lambda x:x**2,a)


#计算那些可以为2整除的数
even_squares = [x**2 for x in a if x%2==0]
  #使用filter也能达到同样的效果
alt = map(lambda x:x**2,filter(lambda x:x%2==0,a))


#字典(dict)与集(set)也有和列表类似的推导机制.
clile_ranks = {'ghost':1,'habanero':2,'cayenne':3}
rank_dict = {rank:name for name,rank in clile_ranks.items()} #字典
clile_len_set = {len(name) for name in rank_dict.values()} #集合
print(rank_dict)
print(clile_len_set)


#不要使用含有两个以上表达式的列表推导,太复杂会很难理解
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat = [x for row in matrix for x in row]
#flat1 = [x for x in row for row in matrix] 错误
print(flat)

squared = [[x**2 for x in row] for row in matrix] #可以理解为嵌套处理
print(squared)

#列表表达式支持多个if条件
a = [1,2,3,4,5,6,7,8,9,10]
b = [x for x in a if x>4 if x%2 ==0] #默认是and模式
c = [x for x in a if x>4 and x%2 ==0]

filtered = [[x for x in row if x%3==0]for row in matrix if sum(row)>=10]







