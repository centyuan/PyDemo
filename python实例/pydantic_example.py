"""
pydantic库是python中用于数据接口定义检查与设置管理的库
"""
import json

from pydantic import BaseModel, Field, validator, ValidationError
from typing import Dict, List, Sequence, Set, Tuple, Optional, Union


# 一.基本使用
# 1.schema基本定义方法
class Person(BaseModel):
    name: str
    age: int = 19
    birth: int = 19


# 2.schema实例方法
p1 = Person(name="Tom")
p2 = Person(**{"name": "Tom"})
p3 = Person.copy(p2)
# 解析数据
print("解析数据对象:", Person.parse_obj(obj={"name": "username"}))
print("解析数据对象:", Person.parse_raw('{"name":"username"}'))
print("解析数据:", p3.parse_obj(obj={"name": "username"}))  # 解析obj
print("解析数据:", p3.parse_raw('{"name":"username"}'))  # 解析字符串
# 3.错误传参报错
try:
    # p4 = Person(person="Tom")  # 没有person参数
    # p4 = Person(name="张三", age="三",brith="sha")
    p4 = Person(name="张三", birth="三")
# 捕获ValidationError
except ValidationError as e:
    info = e.json()
    print(json.loads(info)[0].get("loc"))
    # print(e.json())
# 4.额外的参数会被过滤
p5 = Person(name="Tom", age="10", gender="man")
print(p5.json())
# 5.数据类型自动转换
p6 = Person(name=321)
print(p6.json())  # {"name": "321"}

# 二:基本数据类型
from enum import Enum


# 枚举类型
class Gender(str, Enum):
    man = "man"
    women = "women"


class demo(BaseModel):
    a: int
    b: float
    c: str
    d: bool
    e: List[int]  # 整数列表
    f: Dict[str, int]  # 字典型
    g: Set[int]  # 集合
    h: Tuple[str, int]  # 元组
    j: Gender
    age: Optional[int]  # 可选数据类型,参数不是必须的,默认值为None
    gender: str = "man"  # 定义默认值(一般性操作)
    gen = "man"  # 也可以直接定义默认值
    time: Union[int, str]  # 允许多种数据类型(2020,"2020":字符串和数字都可以传入)
    username: str = Field(alias="user_name")  # 传入参数定义别名
    person: List[Person]  # schema 嵌套


# 三 数据类型检查(通过validator和config实现更复杂的数据类型检查)
class Password(BaseModel):
    password: str

    @validator("password")
    def password_rule(cls, password):
        def is_valid(password):
            if len(password) < 6 or len(password) > 20:
                return False
            return True

        if not is_valid(password):
            raise ValueError("password is invalid")

    # 对类中某一个基本类型同一格式要求
    class Config:
        min_anystr_length = 6  # 令Password类中所有字符串长度不小于6
        max_anystr_length = 20  # 令Password类中所有字符串长度不大于6
