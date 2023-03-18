import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import sessionmaker

ModelBase = declarative_base()  # 元类


# 1.ORM使用模式(先在数据库建好对应表)或使用ModelBase.metadata.create_all(engine)
class User(ModelBase):
    __tablename__ = "auth_user"
    id = Column(Integer, primary_key=True, nullable=True, autoincrement=True)
    date_joined = Column(DateTime)
    username = Column(String(length=30))
    password = Column(String(length=128))


# 2.初始化数据库连接
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/runoob')
# 3.创建表
# ModelBase.metadata.create_all(engine)                                                    
# 4.创建DBsession
DBsession = sessionmaker(bind=engine)
# 5.创建session对象
session = DBsession()
# 6.添加数据
# new_user = User(id=1, date_joined=datetime.datetime.now(), username="袁", password="密码")
# session.add(new_user)  # 添加到session
# session.commit()  # 提交
# session.close()  # 关闭
# 7.查询 session.query(User)返回Query对象
query = session.query(User)
print(query.all())  # 返回查询结果的list,会触发执行SQL查询
print(query.first())  # 返回查询结果一个,会触发执行SQL查询
print(query.get(1))  # 根据primary key查询单个对象
print(query.count())  # 数量
print(query.as_scalar())  # 返回此次查询的SQL语句
print(session.query(User.username).first())  # 值查询username
print(session.query(User.username).all())  # 值查询username
for row in query:
    print(row.id, row.username)
# 排序
for row in query.order_by(User.date_joined):
    print(row.id, row.username)
# 限制条数
for row in session.query(User)[:2]:
    print(row.id)
# 过滤
record = session.query(User).filter(User.username == "李").first()
print(record)
# 更新数据
li_user = session.query(User).filter(User.username == "老李老").first()
li_user.username = "老李老"
session.commit()
print(li_user)
# 删除数据
laoli_user = session.query(User).filter(User.username == "老李老").first()
session.delete(laoli_user)
session.commit()
"""
sqlalchemy两种使用模式
1.SQL表达式语言
2.ORM
"""
