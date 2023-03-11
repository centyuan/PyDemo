"""
Django中单元测试方法是django.test.TestCase(在unittest.TestCase基础上封装)
python manage.py test # 执行整个项目的单元测试
python manage.py test account # 只执行account模块
python manage.py test cccount.tests.XXXTestCase # 只执行某一个测试类
"""

from django.test import TestCase
class AccountRegister(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    sex = models.IntergerField(max_length=10)
    register_time = models.DatetimeField()


# 1.model单元测试
class AccountTestCase(TestCase):
    def setUp(self):
        """初始数据"""
        self.account = AccountRegister.objects.create(
            username="test",
            password="root",
            sex=1,
            register_time="2023-03-11 12:00:00",
        )

    def test_account_model(self):
        """测试方法一"""
        self.assertEqual(self.account.register_time, "2023-03-11 12:00:00")


# 2.接口单元测试
# from rest_framework.test import APITransactionTestCase, RequestsClient
class XXXTestCase(APITransactionTestCase):

    def setUp(self) -> None:
        """
        初始化数据
        """
        # 如果接口需要认证，则设置Token
        self.token = 'your_token'
        self.client = RequestsClient()
        self.client.headers.update({'X-TOKEN': self.token})
        self.BASE_URL = 'http://127.0.0.1:8000'

    def test_delete_xxx(self):
        id = "test_id"
        api = '/test/{}/'.format(id)  # 你的接口
        response = self.client.delete(self.BASE_URL + api)
        resp = response.json()
        self.assertEqual(resp['code'], 200)  # 根据情况断言返回结果
        self.assertEqual(resp['message'], 'ok')
