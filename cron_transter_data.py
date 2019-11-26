# -*- coding:utf-8 -*-
# Author centyuan
# Date 2019/11/26 14:55
import time
import MySQLdb
import random

if __name__ == '__main__':
    while 1:
        conn = MySQLdb.connect(
            host='154.221.20.205',
            port=3306,
            user='danye1',
            passwd='danye1',
            db='danye1',
        )
        cur = conn.cursor()
        sql = '''
        INSERT into dede_diyform1 (ren, dz, sszf, dkje, dkytu, sjian, day, datasource) 
        SELECT ren, dz, sszf, dkje, dkytu, sjian, day, datasource from dede_diyform1_source where sjian <= NOW() and inuse=0 ORDER BY sjian DESC LIMIT 1;
        update dede_diyform1_source set inuse=1 where inuse=0 AND dz in(SELECT dz from dede_diyform1);
        '''
        cur.execute(sql)
        cur.close()
        conn.commit()
        time.sleep(random.randint(1,300))
        conn.close()
