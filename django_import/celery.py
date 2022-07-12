from celery import Celery

app = Celery('hello',broker='amqp://guest@localhost//')

@app.task
def hello():
    return "hello world"

# 调用方式
result = hello.delay()
hello.apply_async()
# 检测是否处理完毕 True False
result.ready()
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
