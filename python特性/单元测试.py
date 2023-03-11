"""
python中单元测试方法:
unittest(内置)
nose
pytest(基于unittest)
"""

import pytest
import requests

"""
pytest:
1.文件名必须以test_.py开始或结尾
2.测试函数以test开头
3.测试类必须以Test开头,不能带有构造方法,__init__
4.断言使用assert 
运行:
1.pytest 按照用例规则自动去匹配
2.pytest 文件名 
3.pytest 文件名::类名::方法名或文件名:函数名
4. if __name__ == "__main__":
     pytest.main(["-s"])
@pytest.mark.smoke:自己标记运行时候使用-m参数来运行部分测试用例
@pytest.mark.skip:跳过测试用例
@pytest.mark.skipif:带条件跳过测试用例
"""


# 1.函数测试
@pytest.mark.p0
def test_mark01():
    print("函数级别的mark_p0")


@pytest.mark.p1
def test_mark02():
    print("函数级别的mark_p1")


@pytest.mark.p2
def test_mark03():
    print("函数级别的mark_p2")


data = [
    ({"city": '上海', "key": "331eab8f3481f37868378fcdc76cb7cd", 'result': "查询成功!"}),

    ({"city": "上海", "key": "331eab8f3481f37868378fcdc76cb7c", 'result': "错误的请求KEY"}),

    ({"city": "上", "key": "331eab8f3481f37868378fcdc76cb7cd", 'result': "暂不支持该城市"})]


# 2.类测试
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
    # @pytest.mark.parametrize("data", data)
    @pytest.mark.smoke
    def test_01(self, data):
        data = {"city": '上海', "key": "331eab8f3481f37868378fcdc76cb7cd", 'result': "查询成功!"}
        r = TestCase.weather(city=data['city'], key=data['key'])
        assert r['reason'] == data['result']
