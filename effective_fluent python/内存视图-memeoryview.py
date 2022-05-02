from array import  array

"""memoryview 是一个内置类，它能让用户在不复制内容的情况下操作同一个数组的不同切片"""

numbsers = array('h',[-2,-1,0,1,2])
memv = memoryview(numbsers)  # memv里面元素和numbers没有区别
print(memv[0],len(memv))
#   -2, 5
mvmv_oct = memv.cast('B')  # 把memv 里的内容转换成'B' 类型，也就是无符号字符
#   列表的形式查看memv_oct 的内容
print(mvmv_oct.tolist())
#   [254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
mvmv_oct[5] =4
#   把占2 个字节的整数的高位字节改成了4，所以这个有符号整数的值就变成了1024
print(numbsers)
#   array('h', [-2, -1, 1024, 1, 2])
