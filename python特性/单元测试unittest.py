"""
python中单元测试方法:
unittest(内置)
nose
pytest(基于unittest)
"""
# 1. basic 函数测试
def func(x):
    return x+1
def 
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
    @pytest.mark.parametrize("data", data)
    def test_01(self, data):
        r = TestCase.weather(city=data['city'], key=data['key'])
        assert r['reason'] == data['result']


if __name__ == '__main__':
    pass
