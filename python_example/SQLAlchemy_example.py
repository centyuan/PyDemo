"""
sqlalchemy两种使用模式
1.SQL表达式语言
2.ORM

https://www.cnblogs.com/ChangAn223/p/11277468.html
https://www.cnblogs.com/ybjourney/p/11876595.html
https://juejin.cn/post/6844904164141580302

"""
# 一:orm基本使用方法
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import sessionmaker
ModelBase = declarative_base()  # 创建元类
engine = create_engine()      # 创建引擎
ModelBase.metadata.create_all(engine)  # 在表结构迁移到数据库

# 1.ORM使用模式(先在数据库建好对应表)或使用ModelBase.metadata.create_all(engine)
class User(ModelBase):
    __tablename__ = "auth_user"
    id = Column(Integer, primary_key=True, nullable=True, autoincrement=True)
    date_joined = Column(DateTime)
    username = Column(String(length=30))
    password = Column(String(length=128))


# 2.初始化数据库连接:创建一个数据库引擎方便session建立会话
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/runoob',
                       echo=True,
                       pool_size=100,
                       pool_recycle=3600, # 一个小时
                       pool_pre_ping=True,

                       )
'''
pool_size:连接池大小
pool_recycle:指定时间内回收连接,必须小于mysql wait_timeout
pool_pre_ping:每次从连接池取走一个连接,都会向数据库请求select 1,测试查询语句来判断服务器是否正常运行。当该连接出现 disconnect 的情况时，该连接连同pool中的其它连接都会被回收。

'''
# 3.创建表
# ModelBase.metadata.create_all(engine)
# 4.创建DBsession工厂并关联engine,应该全局声名以确保每个session都可以使用该Engine连接资源
DBsession = sessionmaker(bind=engine,autoflush=False,autocommit=False)
'''
autoflush:True 自动预提交,查询之前把当前变更提交到数据库内存,还没写入数据库摁键,之后就可以查询出来,flush之后还是可以rollback
autocommit:True 则所有操作都是一个单独的事物并自动提交,然后在开启一个新事务,所以不能rollback了

'''
# 5.创建session对象,连接池会分配一个connection,当调用session.close(),将连接归还给连接池而不会关闭连接
session = DBsession()
# 6.添加数据
# new_user = User(id=1, date_joined=datetime.datetime.now(), username="袁", password="密码")
# session.add(new_user)  # 添加到session
# session.commit()       # 提交
# session.close()        # 关闭
# session.rollbackk()    # 回滚
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
for row in  session.query(User)[:2]:
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

# 二:进阶说明
"""
session对象包含了三个重要部分(采用了弱引用机制):
    1.标识映射(Identity Map)
    2.对象的状态/状态跟踪
    3.事物
一般使用上下文封装session工厂
from contextlib import contextmanager

@contextmanager
def session_maker(session=session):
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise 
    finally:
        session.close()

session_factory = scoped_session(sessionmaker(bind=engine))
session不是线程安全的,且在并发场景下,同一个线程没必要多次获取session,可以使用scoped_session,在同一个线程,返回同一个session对象,注意多线程还是不同对象
scoped_session本质上是实现了一个"线程级"的单例模式,使用了threading.local()实现


"""