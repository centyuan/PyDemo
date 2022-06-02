# -*- coding:utf-8 -*-
# Author centyuan
# Date 2019/11/26 13:52
import xlrd
# rb = xlrd.open_workbook("四季周转1000.xlsx")
rb = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\四季周转1000.xlsx")
print(rb.sheet_names())
sheet1 = rb.sheet_by_name('Sheet1')
print(sheet1.nrows)
print(sheet1.ncols)
print(sheet1.row(0))
value = sheet1.row_values(0)
print("value",value)
name = value[0].split()[0]
number = value[0].split()[1]
