# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/29 14:46

cars = ['Audi', 'BMW', 'Ford', 'Tesla', 'Volvo']

cars_dict = dict(enumerate(cars))
cars_dict1 = dict.fromkeys(cars)
print(cars_dict)
# {0: 'Audi', 1: 'BMW', q 2: 'Ford', 3: 'Tesla', 4: 'Volvo'}
print(cars_dict1)
# {'Audi': None, 'BMW': None, 'Ford': None, 'Tesla': None, 'Volvo': None}
ddd = [(0, 'Spring',1), (1, 'Summer',2), (2, 'Fall',3), (3, 'Winter',4)]
for k,v,i in ddd:
    print(k,v,i)