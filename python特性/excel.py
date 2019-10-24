# -*- coding:utf-8 -*-
import xlrd
import xlwt

pabook=xlwt.Workbook(encoding='utf-8')
pasheet=pabook.add_sheet('记录')
pasheet.write(2,2,label='你说房间爱减肥方法')
pabook.save('信息.xls')
fruits = ['banana', 'apple', 'mango','hiann','sfjaj','ajdfa','fahdjkfh']
for index in range(len(fruits)):
    print
    '当前水果 :', fruits[index]

print(len(fruits))
