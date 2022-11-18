# -*- coding:utf-8 -*-
# Author centyuan
# Date 2019/10/31 10:31
"""
https://blog.csdn.net/zcl_love_wx/article/details/81983267
数据库锁一般可以分为两类，一个是悲观锁，一个是乐观锁。

乐观锁一般是指用户自己实现的一种锁机制，假设认为数据一般情况下不会造成冲突，所以在数据进行提交更新的时候，才会正式对数据的冲突与否进行检测，如果发现冲突了，则让返回用户错误的信息，让用户决定如何去做。乐观锁的实现方式一般包括使用版本号和时间戳。

悲观锁一般就是我们通常说的数据库锁机制，以下讨论都是基于悲观锁。

悲观锁主要表锁、行锁、页锁。在MyISAM中只用到表锁，不会有死锁的问题，锁的开销也很小，但是相应的并发能力很差。innodb实现了行级锁和表锁，锁的粒度变小了，并发能力变强，但是相应的锁的开销变大，很有可能出现死锁。同时inodb需要协调这两种锁，算法也变得复杂。InnoDB行锁是通过给索引上的索引项加锁来实现的，只有通过索引条件检索数据，InnoDB才使用行级锁，否则，InnoDB将使用表锁。

表锁和行锁都分为共享锁和排他锁（独占锁），而更新锁是为了解决行锁升级（共享锁升级为独占锁）的死锁问题。

innodb中表锁和行锁一起用，所以为了提高效率才会有意向锁（解决行锁和表锁的冲突，意向共享锁和意向排他锁）。

'''
表锁：
实现逻辑简单,开销小,加锁 释放锁快，能避免死锁问题
粒度大所以并发小

行锁：myIsam不支持,Innodb,NDBCluster支持
逻辑复杂，开销大，加锁慢，容易出现死锁

行锁:通过给索引上的索引项加锁来实现的,只有通过索引条件检索数据，InnoDB才使用行级锁，否则，InnoDB将使用表锁

意向锁(表级锁定)：让表锁行锁共存
发现某些行资源被排他锁锁占用时，
1.需要一个共享锁，那么就在表上面添加一个意向共享锁
2.需要一个排他锁，则先在表上面添加一个意向排他锁
意向共享锁可以存着多个，意向排他锁只能一个

###  在同一个SQL session里，如果已经获取了一个表的锁定，则对没有锁的表不能进行任何操作，否则会报错。

'''


"""

# 乐观锁实现(适合读取操作频繁的)
# 1:原生语句
# update tb_goodsinfo set stock=5 where id=1 and stock=10;
# 2：django
# GoodsInfo.objects.filter(id=1, stock=10).update(stock=5)


# 悲观锁实现(适合写入修改操作频繁的)
# 行级锁
# 使用select_for_update(nowait=False, skip_locked=False)
# Entry.objects.select_for_update().filter(author=request.user)
# select_for_update与select_related时，相关对象也被锁定,select_for_update具有“of”选项，用于显式地声明要锁定查询中的哪些表
# 加互斥锁，由于mysql在查询时自动加的是共享锁，所以我们可以手动加上互斥锁。create、update、delete操作时，mysql自动加行级互斥锁
# (ps:注意必须用在事务里面,所有的匹配行将被锁定,直到事务结束.这意味着可以通过锁防止数据被其他事务修改)

"""
　　一般情况下如果其他事物锁定了相关行,那么本查询将被阻塞,直到锁被释放.如果这不想要使查询阻塞的话,
   使用select_for_update(nowait=True).如果其他事物持有冲突的锁,互斥锁,那么查询将引发DatabaseError异常.
   你也可以使用select_for_update(skip_locked=True)忽略锁定的行. nowait和skip_locked是互斥的,
   同时设置会导致ValueError.目前,postgresql,oracle和mysql数据库后端支持select_for_update().
   但是,Mysql不支持nowait和skip_locked参数.
   使用不支持这些选项的数据库后端(如MySQL)将nowait=True或skip_locked = True转换为select_for_update() 
   将导致抛出DatabaseError异常,这可以防止代码意外终止.
"""
# 表级锁
# https://zhuanlan.zhihu.com/p/151767128
# class LockingManager(models.Manager):
#     def lock(self):
#         cursor = connection.cursor()
#         table = self.model._meta.db_table
#         cursor.execute(f"LOCK TABLES {table} WRITE")
#
#     def unlock(self):
#         cursor = connection.cursor()
#         table = self.model._meta.db_table
#         cursor.execute("UNLOCK TABLES")
# objects = LockingManager()
# 加表锁：
# User.objects.lock()
# 解表锁：
# User.objects.unlock()


# http://t.zoukankan.com/sundawei7-p-11656505.html
# django事务开启方式
# 1：全局开启(ps:，常用的事务处理方式是将每个请求都包裹在一个事务中。这个功能使用起来非常简单，
# 你只需要将它的配置项ATOMIC_REQUESTS设置为True。它是这样工作的：当有请求过来时，Django会在调用视图方法前开启一个事务。
# 如果请求却正确处理并正确返回了结果，Django就会提交该事务。否则，Django会回滚该事务)
# @transaction.non_atomic_requests 可以取消全局的事务开启（不推荐）
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'mxshop',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#         'USER': 'root',
#         'PASSWORD': '123',
#         'OPTIONS': {
#             "init_command": "SET default_storage_engine='INNODB'",
# 　　　　　　　#'init_command': "SET sql_mode='STRICT_TRANS_TABLES'", #配置开启严格sql模式
#         }
#         "ATOMIC_REQUESTS": True, #全局开启事务，绑定的是http请求响应整个过程        "AUTOCOMMIT":False, #全局取消自动提交，慎用
#     }，　　'other':{　　　　'ENGINE': 'django.db.backends.mysql',             ......　　} #还可以配置其他数据库
# }

# 2：局部使用事务
# @transaction.atomic 函数装饰器
# with transaction.atomic(): 上下文管理器
# 一旦把atomic代码块放到try/except中，完整性错误就会被自然的处理掉了
# 需要捕获异常添加一个嵌套的atomic来做
# 嵌套 函数的事务嵌套上下文管理器的事务，上下文管理器的事务嵌套上下文管理器的事务
from django.db import transaction


@transaction.atomic
def viewfunc(request):
    sid = transaction.savepoint()  # 创建保存点
    if True:
        transaction.savepoint_commit(sid)  # 提交保存点
    else:
        transaction.savepoint_rollback(sid)  # 回滚保存点

    transaction.commit()  # 手动提交事务，默认是自动提交的，也就是说如果你没有设置取消自动提交，
    # 那么这句话不用写，如果你配置了那个AUTOCOMMIT=False，那么就需要自己手动进行提交。
