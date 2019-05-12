#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-4-11 上午11:20
#python中的变量赋值不需要类型声明

#一：
def f(x, l=[]):
    for i in range(x):
        l.append(i * i)
    print(id(l))
    print(l)


f(2)  # [0,1]
f(3, [3, 2, 1])  # [3,2,1,0,1,4]
f(3)  # [0,1,0,1,4]
f(3)
f(3)

#二：

class Parent(object):
    x = 1


class Child1(Parent):
    pass


class Child2(Parent):
    pass


print(Parent.x, Child1.x, Child2.x)  # 1 1 1
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)  # 1 2 1
Child2.x = 3
print(Parent.x, Child1.x, Child2.x)  # 1 2 3

#三：
def mul():
    return [lambda x: i * x for i in range(4)]


print([m(2) for m in mul()])  # 6 6 6 6

#四：列表去重
list1=[9,4,2,5,8,4,5,3]
new_list=[]
for i in list1:
    if i not in new_list:
        new_list.append(i)
print(new_list)

new_list={}.fromkeys(list1).keys()
print(new_list)

#五：
class Context(object):
      def __enter__(self):
         print("do something before")
         return self
      def __exit__(self,exc_type,exc_val,exc_tb):
         return print("do something after")
      def do_something(self):
         return print("do something")

with Context() as ctx:
      ctx.do_something()

#   python执行with-as 的时候 会调用__enter__方法，然后该函数的返回值传给as后指定的变量，
#   之后会执行with-as 下面的代码块，无论该代码块中出现了什么异常，都会在离开时候执行__exit__
#  __exit__也可以做一些异常的监控和捕获。

#六平衡点问题
#平衡点：比如int[] numbers = {1,3,5,7,8,25,4,20}; 25前面的总和为24，25后面的总和也是24，25这个点就是平衡点；假如一个数组中的元素，其前面的部分等于后面的部分，那么这个点的位序就是平衡点

#要求：返回任何一个平衡点
li = [1,3,5,7,8,25,4,20]
def main():
     i = 0
     length = len(li)
     before = 0
     after = 0
     mark = 0
     balance = 0
     total = sum(li)
     while True:
        balance = i + 1
        if balance + 1 > length -1:
              return -1
        if li[i] == li[balance+1]:
             mark = balance
             return (mark,li[mark])
        else:
             before = before + li[i]
             other = total - before - li[balance]
             if before == other:
                 mark = balance
                 return (mark,li[mark])
        i += 1

if __name__ == "__main__":
    print(main())