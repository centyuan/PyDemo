"""
python中单元测试方法:
unittest(内置)
nose
pytest(基于unittest)
"""

import pytest
import requests

data = [
    ({"city": '上海', "key": "331eab8f3481f37868378fcdc76cb7cd", 'result': "查询成功!"}),

    ({"city": "上海", "key": "331eab8f3481f37868378fcdc76cb7c", 'result': "错误的请求KEY"}),

    ({"city": "上", "key": "331eab8f3481f37868378fcdc76cb7cd", 'result': "暂不支持该城市"})]


class TestCase:

    def weather(self, city, key):
        # 查询天气接口参数
        url = 'http://apis.juhe.cn/simpleWeather/query'
        data = {
            'city': city,
            'key': key
        }
        return requests.post(url, data=data).json()

    def idCard(self, card_no, key):
        data = {
            "cardno": card_no,
            "key": key
        }
        return requests.post("http://apis.juhe.cn/idcard/index", data=data).json()

    # 单元测试

    def test_01(self,data):
        pass


if __name__ == '__main__':
    d = {"city": "上海", "key": "331eab8f3481f37868378fcdc76cb7cd", 'result': "暂不支持该城市"}
    d_card = {
        "cardno": "130428197411155947",  # 身份证信息通过Faker随机创建
        "key": "f40a75704fac353952a6534a18f9f437"}
    c = TestCase()
    result = c.weather(city=d["city"], key=d["key"])
    print(result)
    result = c.idCard(card_no=d_card["cardno"], key=d["key"])
    print(result)
