---
title: Python @property详解
categories: 
   - Python从入门到放弃
tags: 
   - Python
---
### Python @property详解

Python的装饰器,用来修饰方法,使调用方法变成读取属性

#### 作用：

使用@property装饰器来创建**只读属性**，@property装饰器会将**方法**转换为相同名称的**只读属性**,可以与所定义的属性配合使用，这样可以防止属性被修改

#### 使用方式:

##### 1.不带装饰器

    语法:class property([fget[, fset[, fdel[, doc]]]])

##### 参数

    fget -- 获取属性值的函数

    fset -- 设置属性值的函数

    fdel -- 删除属性值函数

    doc -- 属性描述信息

```
class test(object):
	def __init(self):
        self.__num = 0
    def getNum(self):
        return self.__num
   	def setNum(self,value):
        self.__num = value
    def delNum(self):
        del self.__num
    num = property(getNum,setNum,delNum)
    # num = proper
print('test.num:', test.num)
test.num = 20
print('test.num:', test.num)
>>test.num: <property object at 0x000001E183216728>
>>test.num: 20
```

##### 2.使用装饰器

```python
class test(object):
  def __init__(self):
      self.__num=0
  @property
  def num(self):
  	return self.__num
 	@num.setter
  def num(self.value):
      # 类型检查
  	if not isinstance(value,int):
          raise TypeError("Expected a string")
       self.__num = value
  @num.deleter
  def num(self):
      del self.__num
print('test_2.num:', test_2.num)
test.num = 90
print('test_2.num:', test_2.num)
print("判断是否有对应属性:",hasattr(test,"num"))
>>test.num: <property object at 0x0000016AD4B8E2C8>
>>test.num: 90
>>判断是否有对应属性: True

```

### hasattr() getattr() getattr() setattr()

**hasattr():函数用于判断是否包含对应的属性**

```
语法：
　　hasattr(object,name)
参数：
　　object--对象
　　name--字符串，属性名
返回值：
　　如果对象有该属性返回True，否则返回False
```

**getattr():函数用于返回一个对象属性值**

```
语法：
　　getattr(object,name,default)
参数：
　　object--对象
　　name--字符串，对象属性
　　default--默认返回值，如果不提供该参数，在没有对于属性时，将触发AttributeError。
返回值：
　　返回对象属性值
```

**setattr():函数用于设置属性值，该属性必须存在**

```
语法：
　　setattr(object,name,value)
 参数：
　　object--对象
　　name--字符串，对象属性
　　value--属性值
返回值：
　　无
```

**delattr():函数用于删除属性**

```
delattr(x,'foobar)相当于del x.foobar
语法：
　　setattr(object,name)
参数：
　　object--对象
　　name--必须是对象的属性
返回值：
　　无
```
