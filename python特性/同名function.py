# -*- coding:utf-8 -*-

def test():
    print("before hello")

def test():
    print("after new hello")

#def gets(datastr,type="耐得住",*args):
#    print(datastr,type)
#    print("before")

def gets(datastr):
    print(datastr,"after")


def gets(datastr,type="耐得住",*args):
    print(datastr,type,"before")
#同名函数后面的会覆盖前面的

if __name__ == '__main__':
    test()
    gets("孤独")
    gets("孤独",type="123456")#持续比较3>2 and 2>2
    print(3>2>2)
#Python2 与 Python3 均不支持复数比较大小
#Python2 支持数字与字符串之间的比较，而 Python3 则不支持
