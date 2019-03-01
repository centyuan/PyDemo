# -*- coding:utf-8 -*-
#初始化字典
dict_data={6:9,10:5,3:11,8:2,7:6}

#1、对字典按键（key）进行排序
#对字典按键（key）进行排序（默认由小到大）
test_data_0=sorted(dict_data.keys())
#输出结果
print(test_data_0) #[3, 6, 7, 8, 10]
test_data_1=sorted(dict_data.items(),key=lambda x:x[0])
#输出结果
print(test_data_1) #[(3, 11), (6, 9), (7, 6), (8, 2), (10, 5)]


#2、对字典按值（value）进行排序
#对字典按值（value）进行排序（默认由小到大）
test_data_2=sorted(dict_data.items(),key=lambda x:x[1])
#输出结果
print(test_data_2) #[('8', 2), ('10', 5), ('7', 6), ('6', 9), ('3', 11)]
test_data_3=sorted(dict_data.items(),key=lambda x:x[1],reverse=True)
#输出结果
print(test_data_3) #[('3', 11), ('6', 9), ('7', 6), ('10', 5), ('8', 2)]