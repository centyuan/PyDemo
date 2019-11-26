# -*- coding:utf-8 -*-
# Author centyuan
# Date 2019/11/26 13:13
import xlrd

rb = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\四季周转1000.xlsx")
sheet1 = rb.sheet_by_name('Sheet1')

sqli = "insert into dede_diyform1_source (ren, dz, dkqxian, dkje, dkytu, day) values ('%s', '%s', '%s', '%s', '%s', '%s');"

f = open("./c.sql", 'w', encoding="utf-8")

for i in range(909):
    try:
        value = sheet1.row_values(i)
        ren = value[0].split()[0]  # 姓名
        dz = value[0].split()[1]  # 手机号
        dkqxian = "1月"
        dkje = "%s千" % (str(str(value[2]).split()[0])[0])
        dkytu = "个人贷款"
        day = "20191126"
        sql = sqli%(ren, dz, dkqxian, dkje, dkytu, day)
        f.writelines(sql)
    except:
        continue

f.close()
