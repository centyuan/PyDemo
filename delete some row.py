# -*- coding:utf-8 -*-
# Author centyuan
# Date 2019/12/2 15:51

import xlrd
import xlwt

sb = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\17501.xls")
sheet1 = sb.sheet_by_name('1')
result_list = []
a = 0
f = open(r"C:\Users\Administrator\Desktop\120.txt", "r", encoding="utf-8")
for line in f:
    print(line.strip())
    result_list.append(line.strip())

workbook = xlwt.Workbook()
new_sheet = workbook.add_sheet('MySheet')
for i in range(17501):
    symbol = True
    value_list = sheet1.row_values(i)
    name = value_list[0]
    if value_list[1] == '电话':
        phone_number = value_list[1]
    else:
        try:
            phone_number = int(float(value_list[1]))
        except Exception as e:
            print("----------异常------------", e)
            phone_number = value_list[1]
    print("******id:%s<>name:%s<>iphone_number:%s" % (i, name, phone_number))
    for item in result_list:
        #print("+++++++++++++++++", item, phone_number, type(item), type(phone_number))
        if str(phone_number) == str(item):
            symbol = False
            a = a + 1
            break
    if symbol:
        new_sheet.write(i, 0, name)
        new_sheet.write(i, 1, phone_number)

workbook.save('new.xls')
f.close()
print("aaaaaaaaaaaaaaaaaaaaaaaaaaa", a)