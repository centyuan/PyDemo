"""
https://zhuanlan.zhihu.com/p/374308042
# 一.cache
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
# 二. get_redis_connection 原生用法
# settings配置和连接池
CACHES = {
    'default':{
        'BACKEND':'django_redis.cache.RedisCache',
        'LOCATION':'redis://127.0.0.1:6379/3',
        'OPTIONS':{
            'CONNECTION_POOL_KWARGS':{"max_connections": 100}
        }
    }
}
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


# 三. import redis
import redis
# 1.StrictRedis
r = redis.StrictRedis(host='localhost',port=6379,db=0)
# 2.Redis decode_responses 将redis取出来的字节改成字符串
r = redis.Redis(host='localhost',port=6379,decode_responses=True)
# 3. 连接池
pool = redis.ConnectionPool(host='localhost',db=3)
r = redis.Redis(connection_pool=pool)
r.keys('foo*') # 模糊匹配
# 4.使用管道pipline
# redis默认在执行每次请求都会创建（连接池申请连接）和断开（归还连接池）一次连接操作，如果想要在一次请求中指定多个命令，则可以使用pipline实现一次请求指定多个命令，并且默认情况下一次pipline 是原子性操作
pool = redis.ConnectionPool(host='localhost',db=3)
r = redis.Redis(connection_pool=pool)
pipe = r.pipline() # 创建管道
pipe.set('name','yuan').set('sex','man')
pipe.set('role','sb')
pipe.incr('num')

"""
# 四.库存秒杀案例
"""
三个问题
1.连接超时？使用连接池
2.并发问题? 乐观锁,使用事务watch multi
3.库存遗留? 乐观锁造成库存遗留,(并发多个人乐观锁,发现版本号不一样,都不执行了)lua封装多个命令实现秒杀逻辑
"""
import redis
from redis import WatchError
from concurrent.futures import ProcessPoolExecutor
pool = redis.ConnectionPool(host='localhost',db=3)

r = redis.Redis(host='127.0.0.1', port=6379,connection_pool=pool)
# from django_redis import get_redis_connection
# r = get_redis_connection("default")

def decr_stock():
    # 1.循环直到减库存操作完成
    # 2.库存充足,操作成功,返回True
    # 3.库存不足,操作失败,返回False
    # 4.所有操作用管道
    with r.pipeline() as pipe:
        while 1:
            try:
                # 1.watch库存键, 监视一个(或多个) key ，如果在事务执行之前这个(或这些) key 被其他命令所改动，那么事务将被打断。
                pipe.watch('stock_count')
                count = int(pipe.get('stock_count'))
                if count > 0:
                    # 有库存
                    # 2.开始事务
                    pipe.multi()
                    # 3.命令入队(命令入队时失败,其他命令都不执行)
                    pipe.decr('stock_count')
                    # 4.执行事务 discard取消事务
                    # execute返回命令执行结果列表, 这里只有一个decr返回当前值
                    print(pipe.execute()[0])
                    return True
                else:
                    # 无库存
                    pipe.unwatch()
                    pipe.execute()
                    return False
                    # exec命令或discard命令先被执行了的话，就不需要再执行unwatch了

            except WatchError as e:
                print(e)
                # 5.取消 WATCH 命令对所有 key 的监视
                pipe.unwatch()
                pipe.execute()


def worker():
    while 1:
        if not decr_stock():
            # 没有库存就退出
            break


# 1.设置库存 begin
r.set('stock_coutn', 100)
# 2.多进程模拟多客户端
with ProcessPoolExecutor(max_workers=4) as pool:
    for _ in range(10):
        pool.submit(worker)