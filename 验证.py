# # import pymysql
# #
# # # 1.连接数据库
# # db = pymysql.connect(host="localhost", user="root", passwd="123456", db="ccstc")
# # # 2.创建一个cursor游标对象
# # cursor = db.cursor()
# # # 3.execute()执行sql
# # sql_ = "select id,username from users_userinfo where  id< ?and id> ?"
# # # sql_ = "select id,username from users_userinfo where  id< :id1and id>:id2"
# # cursor.execute(sql_,(14,20))
# # # cursor.execute(sql_,{"id1":14,"id2":20})
# # # 4.获取所有记录列表
# # results = cursor.fetchall()
# # for row in results:
# #     print(row[1])
# #
# #
# # import mysql.connector
# # connection = mysql.connector.connect(host='localhost',
# #                              database='python_db',
# #                              user='pynative',
# #                              password='pynative@#29')
# #
# # # this will retun MySQLCursorPrepared object
# # cursor = connection.cursor(prepared=True)
# import re
#
#
# def filter_format(phone=None, email=None):
#     phone_pat = r"^(((13[0-9]{1})|(14[0-9]{1})|(15[0-9]{1})|(16[0-9]{1})|(17[0-9]{1})|(19[0-9]{1})|(18[0-9]{1}))+\d{8})$"
#     email_pat = r"\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}"
#     ph, em = True, True
#     if not re.match(phone_pat, phone):
#         ph = False
#     if not re.match(email_pat, email):
#         em = False
#     return ph, em
#
#
# if __name__ == '__main__':
#     phone = "13985856325"
#     email = '375319412@qq.com'
#     print(filter_format(phone,email))



