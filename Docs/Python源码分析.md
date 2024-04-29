---
title: Python源码分析
categories:
    - Python从入门到放弃
tags:
    - Python
---



#### 相关资料

>[Python源码剖析](https://juejin.cn/post/7031139112321024031)
>
>[Python源码](https://fasionchan.com/python-source/preface/intra/)
>
>[Cpython-github](https://github.com/python/cpython)
>
>[Your Guide to the CPython Source Code](https://realpython.com/cpython-source-code-guide/)
>
>[CPyUG](https://groups.google.com/g/python-cn)



#### 主要内容

##### 编译Python

>1 Python总体架构
>2 Python源代码的组织
>3 Windows环境下编译Python
>4 Unix/Linux环境下编译Python
>5 修改Python源代码
>6 通往Python之路
>7 一些注意事项

##### Python内建对象

###### Python中的整数对象

>1 初识PyIntObject对象
>2 PyIntObject对象的创建和维护
>3 Hack PyIntObject

###### Python中的字符串对象

>1 PyStringObject与PyString_Type
>2 创建PyStringObject对象
>3 字符串对象的intern机制
>4 字符缓冲池
>5 PyStringObject效率相关问题
>6 Hack PyStringObject

###### Python中List对象

>1 PyListObject对象
>2 PyListObject对象的创建与维护
>3 PyListObject对象缓冲池
>4 Hack PyListObject

###### Python中的Dict对象

>1 散列表概述
>2 PyDictObject
>3 PyDictObject的创建和维护
>4 PyDictObject对象缓冲池
>5 Hack PyDictObject

###### Python模拟

>1 Small Python
>2 对象机制
>3 解释过程
>4 交互式环境



##### Python虚拟机

###### Python的编译结果---Code对象与pyc文件

>1 Python程序的执行过程
>2 Python编译器的编译结果——PyCodeObject对象
>3 Pyc文件的生成
>4 Python的字节码
>5 解析pyc文件

##### Python虚拟机框架

>1 Python虚拟机中的执行环境
>2 名字、作用域和名字空间
>3 Python虚拟机的运行框架
>4 Python运行时环境初探

###### Python虚拟机中的一般表达式

>1 简单内建对象的创建
>2 复杂内建对象的创建
>3 其他一般表达式

###### Python虚拟机中的控制流

>1 Python虚拟机中的if控制流
>2 Python虚拟机中的for循环控制流
>3 Python虚拟机中的while循环控制结构
>4 Python虚拟机中的异常控制流

###### Python虚拟机中的函数机制

>1 PyFunctionObject对象
>2 无参函数调用
>3 函数执行时的名字空间
>4 函数参数的实现
>5 函数中局部变量的访问
>6 嵌套函数、闭包与decorator

###### Python虚拟机中的类机制

>1 Python中的对象模型
>2 从type对象到class对象
>3 用户自定义class
>4 从class对象到instance对象
>5 访问instance对象中的属性
>6 千变万化的descriptor

###### Python运行环境初始化

>1 线程环境初始化
>2 系统module初始化
>3 激活Python虚拟机

###### Python模块的动态加载机制

>1 import前奏曲
>2 Python中import机制的黑盒探测
>3 import机制的实现
>4 Python中的import操作
>5 与module有关的名字空间问题

###### Python多线程机制

>1 GIL与线程调度
>2 初见Python Thread
>3 Python线程的创建
>4 Python线程的调度
>5 Python子线程的销毁
>6 Python线程的用户级互斥与同步
>7 高级线程库——threading

###### Python的内存管理机制

>1 内存管理架构
>2 小块空间的内存池
>3 循环引用的垃圾收集
>4 Python中的垃圾收集