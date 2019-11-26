# -*- coding:utf-8 -*-
# Author centyuan
# Date 2019/11/26 13:35
import MySQLdb
conn = MySQLdb.connect(
    host='154.221.20.205',
    port=3306,
    user='danye1',
    passwd='danye1',
    db='danye1',
)

cur = conn.cursor()
sqli = "insert into dede_diyform1_source (ren, dz, dkqxian, dkje, dkytu, day) values (%s, %s, %s, %s, %s, %s,)"
cur.executemany(sqli,[

])

cur.close()
conn.commit()
conn.close()