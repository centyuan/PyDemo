"""

https://zhuanlan.zhihu.com/p/374308042
第一种:
from django.core.cache import cache
cache.set('name','yyy',60*60)
cache.get('name')                     # 取值
cache.set("foo", "bar", timeout=22)   # 设置过期时间
cache.ttl('foo')                      # 获取过期时间
cache.persist('foo')                  # 让一个值永久在
cache.keys('foo_*')                   # 返回所有匹配的值
cache.iter_keyd('foo_*')              # 返回匹配值的迭代器
cache.delete_pattern('foo_*')         # 返回删掉的键的数量 支持全局通配符


with cache.lock("somekey"):           # 使用 python 上下文管理器分配锁的例子
    do_some_thing()

https://django-redis-chs.readthedocs.io/zh_CN/latest/
第二种: get_redis_connection 原生用法
from django_redis import get_redis_connection
redis_conn = get_redis_connection('default')
redis_conn.setex(key,time,value)  # key 过期时间 value
redis_conn.set('name','yyy')
redis_conn.expire('name',60*60)
redis_conn.delete('name')
redis_conn.get('name')
redis_conn.ttl('name')
# 设置过期时间
conn.set(key,json.dumps(value),ex=60)


第三种 import redis
import redis
r = redis.StrictRedis(host='localhost',port=6379,db=0)
# decode_responses 将redis取出来的字节改成字符串
r = redis.Redis(host='localhost',port=6379,decode_responses=True)
pool = redis.ConnectionPool(host='localhost',db=3)
r = redis.Redis(connection_pool=pool)
r.keys('foo*') # 模糊匹配

"""

