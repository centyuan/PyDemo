# 1.if else

# 2.for else:1.for顺利遍历完后执行else,2.中间有break则跳过else
for i in range(5):
    print("for:", i)
    # break
else:
    print("for else")
# 3.while else:条件为False执行else(有break退出,else也不执行)
number = 1
# number = 6
while number < 5:
    print("while:", number)
    number += 1
    # break
else:
    print("while else")


# 4.try except else:没有异常发生,else被执行
# 总结:在所有情况下,如果异常,或return,break,continue导致控制权跳到外面,else也会被跳过

