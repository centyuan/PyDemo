# _*_ coding:utf-8 _*_
# @Author : centyuan
# @Time : 2022/3/18 11:14
"""
1、object #公用方法
2、_object #半保护
                 #被看作是“protect”，意思是只有类对象和子类对象自己能访问到这些变量，
                  在模块或类外不可以使用，不能用’from module import *’导入。
                #__object 是为了避免与子类的方法名称冲突， 对于该标识符描述的方法，父
                  类的方法不能轻易地被子类的方法覆盖，他们的名字实际上是
                  _classname__methodname。
3、_ _ object  #全私有，全保护
                       #私有成员“private”，意思是只有类对象自己能访问，连子类对象也不能访
                          问到这个数据，不能用’from module import *’导入。
4、_ _ object_ _     #内建方法，用户不要这样定义
"""