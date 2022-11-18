# 1.使用django-crontab插件来实现定时任务
# 2.使用django-apscheduler
# 3.celery
# 4.自建定时任务

import os
import sys
import time
import datetime
import django
import threading

base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# 将项目路径加入到系统中,导入模型不报错
sys.path.append(base_path)
# 设置环境变量
os.environ['DJANGO_SETTINGS_MODULE'] = 'AntiFraud.settings'
django.setup()


def event_handle():
    # 定时任务
    while 1:
        try:
            local_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f'本地时间:{local_time}')
        except Exception as e:
            print('发生错误，错误信息为：', e)
            continue


def main():
    # 另其一个线程启动定时任务
    try:
        task = threading.Thread(target=event_handle)
        task.start()
    except Exception as e:
        print('异常'+str(e))

if __name__ == '__main__':
    main()