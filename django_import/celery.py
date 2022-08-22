# 一:定义任务
from celery import Celery

app = Celery('hello', broker='amqp://guest@localhost//')


@app.task
def hello():
    return "hello world"


# 调用方式
result = hello.delay()
hello.apply_async()
# 检测是否处理完毕 True False
result.ready()
result.result()  # 获取结果
"""
# worker 
nohup celery -A CTFServer worker -B -l info --logfile=./celery.log

# flower Monitor
https://docs.celeryq.dev/en/master/userguide/monitoring.html
pip install flower
celery -A proj flower 或celery -A proj flower --port=5555
open http://localhost:5555

# curses Monitor
celery -A proj events 

#beat 
celeyr -A proj beat 
celery -A proj beat -s /home/celery/var/run/celerybeat-schedule
celery -A FZ_Platform worker -B -l info -c 10
-B代表celery -A proj beat 
#任务调用
# 方法一：delay方法
task_name.delay(args1, args2, kwargs=value_1, kwargs2=value_2)
​
# 方法二： apply_async方法，与delay类似，但支持更多参数
task.apply_async(args=[arg1, arg2], kwargs={key:value, key:value})


https://blog.csdn.net/captain5339/article/details/125400254
https://www.jianshu.com/p/1840035cb510
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
@app.task(bind=True,default_retry_delay=30*60)
def add(self,x,y):
    try:
        something_raising()
    except Exception as exc:
        # default_retry_delay重试前会等待给定的时间,coutdown可以覆盖
        raise self.retry(exc=exc, countdown=60)
"""