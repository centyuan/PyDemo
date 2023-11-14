import sqlite3
import re


def printcookie(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    # c.execute('select host,name,value from moz_cookies')
    # 列出所有表名
    # sql_ = "select name from sqlite_master where type='table' order by name"
    sql_ = "select host,name,value from moz_cookies"
    c.execute(sql_)
    for row in c:
        host = str(row[0])
        name = str(row[1])
        value = str(row[2])
        print('[+] Host:{},cookie:{},value:{}'.format(host,name,value))

    # print(c.fetchall())

    # for row in c:
    #     host = str(row[0])
    #     name = str(row[1])
    #     value = str(row[2])
    #     print('[+] Host: ' + host + ', Cookie: ' + name + ', Value: ' + value)

def printGoogle(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    sql_ = "select url from moz_places,moz_historyvisits where visit_count>0 and moz_places.id==moz_historyvisits.place_id;"
    c.execute(sql_)
    print('Found Google')
    for row in c:
        url = str(row[0])
        # date = str(row[1])
        if 'google' in url.lower():
            r = re.findall(r'q=.*\&',url)
            if r:
                search = r[0].split('&')[0]
                search = search.replace('q=','').replace('+','')
                print('[+]'+'-Searched For:'+search)


def main():
    db = 'C:/Users/rainbow/AppData/Roaming/Mozilla/Firefox/Profiles/w75400ak.default-release/cookies.sqlite'
    new_db = 'C:/Users/rainbow/AppData/Roaming/Mozilla/Firefox/Profiles/w75400ak.default-release/places.sqlite'
    printcookie(db)
    printGoogle(new_db)

if __name__ == '__main__':
    main()