# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/23 23:47
"""
该方法将通过递归的方式将列表的嵌套展开为单个列表
"""


# 1
def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret


def deep_flatten(lst):
    result = []
    result.extend(spread(list(map(lambda x: deep_flatten(x) if type(x) == list else x, lst))))
    return result


result = deep_flatten([[1, 2, 4], [4, 5, [4, 4]], [6], [7, 8], ['a', 'b']])  # [1,2,3,4,5]
print(result)

# 2 只能两层
l = [[1, 2, 4], [4, 5, [4, 4]], [6], [7, 8], ['a', 'b']]
flat_list = [item for sublist in l for item in sublist]
print(flat_list)
