#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-6-4 上午9:29
import time
#一
print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))
#二
words = input('Please input the words you want to say!:')
for item in words.split():
    print('\n'.join([''.join([(item[(x-y) % len(item)] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(12, -12, -1)]))
    time.sleep(1.5);
#三
words=input('Please input the words you want to say')
for item in words.split():
    lettelist=[]
    for y in range(12,-12,-1):
        list_X=[]
        letters=''
        for x in range(-30,30):
            #公式
            expression=((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
            if expression <=0:
                letters +=item[(x-y)%len(item)]
            else:
                letters +=' '
        list_X.append(letters)
        lettelist +=list_X
    print('\n'.join(lettelist))
    time.sleep(1.5)


