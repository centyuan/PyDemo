### 一.四舍五入

# 1.round
"""
round(80.23456,2) # 80.23 返回无点数的四舍六入
python3中:round如果距离两边一样远，会保留到偶数的一边。比如round(0.5)和round(-0.5)都会保留到0，而round(1.5)会保留到2。 
python2中:round如果距离两端一样远，则保留到离0远的一边。所以round(0.5)会近似到1，而round(-0.5)会近似到-1
浮点数精度问题
round(2.675, 2) 的结果，不论我们从python2还是3来看，结果都应该是2.68的，结果它偏偏是2.67，为什么？
机器中浮点数不一定精确表达,因为换算成一串1和0后可能是无限位数的,机器已经做了截断处理，
那么在机器中保存的2.675这个数字就比实际数字要小那么一点点。这一点点就导致了它离2.67要更近一点点
"""

# 2.math.ceil(x)将数字x向上舍入到最接近的整数
"""
math.floor(x)将数字向下舍入到最接近的整数
"""  
# 3.decimal.Decimal(传入字符串数字) 浮点数不准确
"""
decimal.Decimal(str_num).quantize(decimal.Decimal("0.01"),rouding="ROUND_HALF_UP")
保留小数方式:
  ROUND_CEILING   总是趋向正无穷大方向取值
  ROUND_FLOOR     总是趋向负无穷大方向取值
  ROUND_DOWN      总是趋向0方向取值
  ROUND_UP        总是趋向0反方向取值
  ROUND_HALF_UP    四舍五入
  ROUND_HALF_DOWN   大于等于5向0方向取整,
  ROUND_HALF_EVEN   四舍六入双五
  ROUND_05UP        最后一位是0/5,
"""
# 4."%.2f"%float(str_num) 四舍五入