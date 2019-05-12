# -*- coding:utf-8 -*-
#item for item in list_a if item not in list_b.
# 如果将它分为三个部分，可能会更清楚：
#
#     接受 item ；
#     来自 for item in list ;
#     火警的警铃在哪里? item not in list_b
#
# 列表理解语法的原因是因为它反映了扩展的版本：
#
# for item in list: # 2.
#  if item not in list_b: # 3.
#  new_list.append(item) # 1.
#
# 而且，你也不一定只需要 item，例如：
#
# new = [x ** 2 for x in old if not x % 2]
#
# 将创建一个 new 列表，其中包含 old 中所有偶数的平方。
