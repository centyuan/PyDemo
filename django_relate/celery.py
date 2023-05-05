"""
celery:Producer/Beat->Broker(消息代理)->worker(任务消费者)->backend(存储结果)
Producer:调用celery提供的Api/函数/装饰器产生任务交给任务队列处理
Beat:读取配置文件,将里面任务周期性发送给任务队列处理
Broker:消息中间件(通常是消息队列或数据库:RabbitMQ/Redis),接受生产者任务发送过来的任务消息,存进队列再按序分发给worker
Worker:执行任务的消费者(通常在多台服务器运行)(空闲的worker去拉去消息)
Backend:任务处理完保存状态信息和结果
"""

# 一:定义任务
from celery import Celery

app = Celery('hello', broker='amqp://guest@localhost//')


@app.task
def hello():
    return "hello world"


# 调用方式
result = hello.delay()
result = hello.apply_async()
# 检测是否处理完毕 True False
result.ready()
result.result()  # 获取结果
"""
#1. worker 
nohup celery -A CTFServer worker -B -l info --logfile=./celery.log

#2. beat 
celeyr -A proj beat 
celery -A proj beat -s /home/celery/var/run/celerybeat-schedule
celery -A FZ_Platform worker -B -l info -c 10 -D --logfile=celery.log -p gevent
-B:代表celery -A proj beat 
-c:协程数量
-D:后台运行
-p:实现并发的方式(perfork(默认多进程),eventlet,gevent)

#3.任务调用
# 方法一：delay方法
task_name.delay(args1, args2, kwargs=value_1, kwargs2=value_2)
​
# 方法二： apply_async方法，与delay类似，但支持更多参数
task.apply_async(args=[arg1, arg2], kwargs={key:value, key:value})
countdown=5:等待一段时间执行
eta=now+timedelta(second=10):任务开始的时间
expires=60:任务超时时间

#4.flower Monitor
https://docs.celeryq.dev/en/master/userguide/monitoring.html
pip install flower
celery -A proj flower 或celery -A proj flower --port=5555
open http://localhost:5555

#5.curses Monitor
celery -A proj events 



"""
# 二:
from celery import Task


class BaseTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print('异步任务执行成功时，回调')
        return super(BaseTask, self).on_success(retval, task_id, args, kwargs)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('异步任务失败时，回调发出警告')
        return super(BaseTask, self).on_failure(exc, task_id, args, kwargs, einfo)

    """
`   def after_return
    # 异步任务尝试重试时，会执行这个回调方法
    def after_return
    # 异步任务执行成功，并且return了一些内容，会执行这个回调方法。
    def update_state
    # 可以手动调用这个方法来更新任务状态。
    def send_error_email
    # 异步任务执行失败时，并且配置了send_error_emails=True时，会执行这个回调方法。
    """


"""
@celery_app.task(base=BaseTask):
def send_email(x):
    print('执行异步发送邮件{}'.format(x))
    return {'message':'成功'}
"""
# 三:@task or @shared_task
"""
@app.task装饰器:定义我们的异步任务时，那么这个任务依赖于根据项目名myproject生成的Celery实例。
@shared_task
进行Django开发时为了保证每个app的可重用性，我们经常会在每个app文件夹下编写异步任务，这些任务并不依赖于具体的Django项目名。
使用@shared_task 装饰器能让我们避免对某个项目名对应Celery实例的依赖，使app的可移植性更强
"""
# 四:bind=True 绑定任务 ignore_result=True忽略结果(存储结果耗费时间和资源)
# 绑定任务意味着任务函数的第一个参数总是任务实例本身(self)
"""
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)
@task(bind=True)
def add(self, x, y):
    logger.info(self.request.id)
"""

# 五:避免任务同步启动(并发执行)工作单元池被耗尽的话这将会导致死锁。
# 将不同的任务签名链接起来创建一个任务链，三个子任务按顺序执行。警告：不建议同步执行子任务
# chain = first_task | second_task | thread_task


# 六:事务中的celery 任务
"""
from django.db.transaction import on_commit
def create_article(request):
    article = Article.objects.create()
    # on_commit 所有事务提交成功后启动任务。
    on_commit(lambda :task.delay(article.pk))
"""

# 七:任务重试机制
"""
@app.task(bind=True,max_retries=5,default_retry_delay=30*60,time_limit=1800)
def add(self,x,y):
    try:
        something_raising()
    except Exception as exc:
        # default_retry_delay重试前会等待给定的时间,coutdown可以覆盖
        raise self.retry(exc=exc, countdown=60)
bind=True:第一个参数为self
max_retries=5:最大重试次数
default_retry_delay=30*60:重试时间
time_limit:任务超时
"""

# 八:定时任务
# https://blog.csdn.net/captain5339/article/details/125400254
from celery.schedules import crontab

# 绑定时区，防止定时任务时间有误
app.conf.enable_utc = False
app.conf.timezone = "Asia/Shanghai"
# 下面的设置就是关于调度器beat的设置,
# CELERYBEAT_SCHEDULE = {}
app.conf.beat_schedule = {
    'periodic_deletion': {
        'task': 'match.end_match.timing_del_match_resources',
        'schedule': crontab(hour=0, minute=30),
        'args': (4, 5)
    },
    'match_end_remove_tempapply': {
        'task': 'policy.task.match_end_remove_tempapply',
        'schedule': crontab('*/10'),  # 每十分钟执行一次
        # timedelta 可以精确到秒
        # 'schedule':timedleta(seconds=30)  # 每三十秒执行一次
    },

}

# 九:定义任务队列
# https://www.cnblogs.com/chaolumeng/p/12318989.html
from kombu import Queue, Exchange

CELERY_QUEUES = (
    Queue('default', exchange=Exchange('default'), routing_key='default'),
    Queue('app_task', exchange=Exchange('app_task'), routing_key='app_task')
)
CELERY_ROUTES = {
    'match_end_remove_tempapply': {'queue': 'app_task', 'routing_key': 'app_task'},
    'periodic_deletion': {'queue': 'default', 'routing_key': 'default'},
}

# celery -A CTFServer worker -B -l info --logfile=celery.log -Q 队列名(启动worker来消费指定队列的任务)
# 十:常见问题 https://zhuanlan.zhihu.com/p/351328752
# 任务过期时间,celery任务执行结果的超时时间
CELERY_TASK_RESULT_EXPIRES = 60 * 20
# 规定任务完成的时间
CELERY_TASK_TIME_LIMIT = 5  # 在5s内完成任务，否则执行该任务的worker将被杀死，任务移交给父进程
# celery worker的并发数，默认是服务器的内核数目,也是命令行-c参数指定的数目
CELERYD_CONCURRENCY = 4
# 每个worker执行了多少任务就会死掉，默认是无限的:防止内存泄露和worker僵死
CELERYD_MAX_TASKS_PER_CHILD = 40
# 防止死锁
CELERYD_FORCE = True
# 表示Worker在任务执行完后才向Broker发送acks:处理异常,一个任务可能会多次执行
CELERY_ACKS_LATE = True
# 十一:注意事项 https://zhuanlan.zhihu.com/p/130934654
# 1.默认"不公平"任务分配:禁用任务队列预取机制(会将任务成批发送给指定worker)
# -O fair
# 2.引用数据库数据(可能数据在任务执行前被修改)
# 3.不在任务中使用数据库事务
# 4.给任务指定了一个很长的countdown或一个eta
# 5.ACKS行为:celery的默认行为是立即确认任务(通过@shared_task的acks_late为具体任务确定"延迟确认",而不是全局配置)


# redis celery kombu版本问题
# celery==4.4.2
# redis==3.4.3
# kombu==4.6.8

# celery==5.2.7
# redis==4.3.4
# kombu==5.2.4
