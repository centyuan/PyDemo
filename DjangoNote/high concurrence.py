# -*- coding:utf-8 -*-
# Author centyuan
# Date 2019/10/28 11:02

"""
python-django:使用nginx+uwsgi 提供高并发
php：使用nginx+fastcgi 提供高并发
java：使用nginx+tomcat
"""

# 如何再次增加并发量(django)
"""
1:去掉自增主键(ps:因为自增主键的存在写库存在抢锁, 可以利用全局id生成器提前生成id直接写入数据库)
2:换成异步任务去写库(ps:如果数据只是存在mysql中做备份，建议使用异步的方式写入库，先把数据写到缓存下发给用户，之后在利用后台异步任务一点点的写入，例如聊天系统可以这样干)
3:换成更高效的框架或者语言(ps:golang)
nginx+uwsgi
nginx+gunicorn (gunicorn跟uwsgi类似，也是一个高性能的http服务器，它由ruby的unicorn项目移植，是由python编写的)
gunicorn + nginx + gevent(最好方案)

"""
