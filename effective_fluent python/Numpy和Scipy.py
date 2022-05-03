import numpy

a = numpy.arange((12))
print(a,type(a),a.shape)
#   [ 0  1  2  3  4  5  6  7  8  9 10 11] <class 'numpy.ndarray'> (12,)
a.shape=3,4
print(a)    # 3横4竖
a.transpose()  # 转置行列交换 4横3竖