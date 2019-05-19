#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-5-17 下午3:30
import  xlwt

xlwt_testfile=xlwt.Workbook()#新建一个excel文件
table=xlwt_testfile.add_sheet('sheet name')#新建一个sheet
#对一个单元格重复操作，会引发错误，建议file.add_sheet('sheet name',cell_overwrite_ok=true)添加参数
table.write(0,0,'testdata')
xlwt_testfile.save('xlwt_test.xls')