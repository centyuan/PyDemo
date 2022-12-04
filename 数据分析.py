import numpy as np

# 创建数组
array_ = np.array([1, 2, 3, 4])
# 维度数量  几行几列  总个数(n*m)  类型 每个元素的大小(单位为字节)
print('数组属性:', array_.ndim, array_.shape, array_.size, array_.dtype, array_.itemsize)
# reshape调整维度,不改变原来的值
b = np.arange(20)
a = b.reshape((4, 5))
print('ab:', a, b)
# numpy.resize(a,new_shape)

# print(array_[1]  # 取索引和切片
# 用于复制 =是直接引用
b = np.array(array_)
print(type(array_))
print(np.array(range(10)))

# 数组里类型不一一样，转为最后一个的类型
print(np.array([1, 2, 3, '4']))
# dtype 转换类型
print(np.array([1, 2, 3, 4], dtype='float'))

# 创建二维数组
print(np.array([
    [1, 2, 3],
    ('1', '2', '3')]
))

# 创建二维数组,个数不一样
# print(np.array([
#     [1, 2, 3],
#     ('1', '2', '3', '4')]
# ))

# 创建区间数组
print(np.arange(1, 5))

# 浮点不准确影响值
print(np.arange(0.1, 0.4, 0.1))
# [0.1 0.2 0.3 0.4]


# 等差数列 numpy.linspace
# 0-4 9个值
# retstep:True显示间距默认不显示并显示步长,默认为False
# endpoint:默认为True包含4
print(np.linspace(0, 4, 9, retstep=True, endpoint=True))

# 等比数列
# base 对log的底数
# 2的0次方到2的9次方分成10分
print(np.logspace(0, 9, 10, base=2))
print(np.logspace(1, 5, 3, base=2))

# 切片
a = [0, 1, 2, 3, 4, 5, 6, 7]
print(a[2:7:1])
# 切片并修改值
a = np.arange(10)
a[7:9] = 200
print('切片并修改值\n', a)

# 二维切片 使用省略号
# 取所有行的，第一列
# array_[...,1]
# 取所有行的,第一列及以后
# array_[...,1:]
# 取1,2行,1,2列
# array_[1:3,1:3]
# array_[1,2] == array_[1][2]


# 练习题:创建8X8的国际象棋棋盘矩阵
# 全为0
Z = np.zeros((8, 8), dtype=int)
Z[1::2, ::2] = 1
Z[::2, 1::2] = 1
print('打印矩阵')
print(Z)

# 布尔索引
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
# 筛选大于6的一维数组
print(x[x > 6])
# 筛选条件为多个 $和 |或
print(x[(x > 4) & (x < 9)])
print(x[(x < 4) | (x > 9)])
# 练习题:找出奇数并改为-1

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
x[x % 2 == 1] = -1
print(x)

# True False筛选
row_ = np.array([False, True, True])
column_ = np.array([True, False, True, False])
a_3_4 = np.arange(12).reshape(3, 4)
# 只要2,3行
print('True False筛选\n', a_3_4[row_])
print(a_3_4[[1, 2], :])
# 所要行，只要1,3列
print('True False筛选\n', a_3_4[:, column_])
print(a_3_4[:, [0, 2]])
# 先选第一行和最后一行,在选0,2,3列
print(a_3_4[[0, -1], :][:, [0, 2, 3]])

# numpy广播机制
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
# 维数相同
c = a * b
print('numpy广播机制\n', c)  # [ 10  40  90 160]
# 维数不同,小的维度会横向或纵向上重复变成维度相同
# 判断是否能运算：相同,1,空


# 求平均值
m_ = np.arange(20).reshape((4, 5))
print('求平均值\n', m_.mean())
# 求每列平均值
print(m_.mean(axis=0))
# 求每行平均值
print(m_.mean(axis=1))

# 中位数
# 奇数个取中间一个,偶数个取中间两个平均值
ar1 = np.array([1, 3, 5, 6, 8])
print('中位数\n', np.median(ar1))

# 求标准差
# (是一组数据平均分散程度及离散程度的一种度量，较大标准差:代表大部分数值和平均值之间差异较大,较小标准差:代表这些数值交接近平均值)
# 用于稳定性指标:标准差有计量单位,方差没有计量单位
c = np.array([95,85,75,65,55,45])
d = np.array([73,72,71,69,68,67])
print('求标准差\n',np.std(c),np.std(d))
print('方差表示数据离散程度\n',c.var())
# 每个-平均数在平方后求和/总单位数 在开平方
print(np.sqrt(np.sum((c-np.mean(c))**2)/c.size))


# 求最大最小值
max1 = np.array([1,4,10,9,5])
print('求最大值,最小值\n',max1.max(),max1.min())
max1 = np.arange(20).reshape((4,5))
print('求某行最大\n',max1.max(axis=0))
print('求某列最大\n',max1.max(axis=1))

# 求和
print(np.sum(max1))

# 求加权平均值
# 各数字乘以权重求和/总的单位数
# np.average()

# 练习:求该学科综合成绩(求加权平均)

ming = np.array([80,90,95])  # 平时,期中,期末 权重:0.2,0.3,0.5
gang = np.array([95,90,80])
print('求加权平均值\n',np.average(ming,weights=[0.2,0.3,0.5]))


# 标准差不合适时候表示离散程度大小的时候:使用变异系数
# 股票
stat_info = np.array([
    [110.93,16.46,0.2376,0.0573],
    [-0.013,31.01,0.1188,0.0836],
    [8.94,26.67,0.0565,0.0676],
    [17.24,19.53,0.1512,0.0433],
    [43.86,-10.14,0.097,0.0421],
    [-15.34,13.04,0.0902,0.0732],
    [-20.82,23.37,0.0582,0.1091],
])
# 1.计算各自的平均值
stat_mean = np.mean(stat_info,axis=0)
print('股票平均值:',stat_mean)
# 2.计算标准差
stat_std = np.std(stat_info,axis=0)
print('股票标准差:',stat_std)
# 3.变异系数 = 原始数据标准差/原始数据平均值
# 变异系数:几组数据测量尺度相差太大,或数据量纲不同,用标准差毕竟不合适,可以使用变异系数(可以消除测量尺度和量纲的影响)
print('股票变异系数:',stat_std/stat_mean)


# 结构化数据类型
teacher = np.dtype([('name',np.str,2),('age','i1'),('salary','f4')])

b = np.array([('张老师',29,8789.50),
              ('邓老师',30,7856.90),
              ],dtype=teacher)
print('结构化数据类型:',b)
print('只取name,age:',b['name'],b['age'])

# 读取普通文件
