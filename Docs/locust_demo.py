import time
from locust import HttpUser, task, between, events
import urllib3
from locust.contrib.fasthttp import FastHttpLocust
urllib3.disable_warnings()


@events.test_start.add_listener
def on_test_start(**kwargs):
    print('===测试最开始提示===')


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    print('===测试结束了提示===')


class TestTask(HttpUser):
    wait_time = between(1, 5)
    # host = 'https://www.baidu.com'

    def on_start(self):
        print('这是SETUP，每次实例化User前都会执行！')

    @task(1)
    def getBaidu(self):
        self.client.get(url="/", verify=False)

    def on_stop(self):
        print('这是TEARDOWN，每次销毁User实例时都会执行！')


if __name__ == "__main__":
    import os

    os.system("locust -f locust_demo.py --host=http://192.168.8.243:8001/api/scene/all_type")
