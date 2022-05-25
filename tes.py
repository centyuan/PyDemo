import cv2






# with open("unpass.txt","r+",encoding="utf-8") as  f:
#
#     for line in f.readlines():
#         print(len(list(line.split("\t"))),line.split('\t'))
#         break
#
#
#
# with open("finish1.txt","r+",encoding="utf-8") as  f:
#
#     for line in f.readlines():
#         print(len(list(line.split("\t"))),line.split('\t'))
#         break

import itertools as its
words = '1234567890'
r = its.product(words,repeat=6)
dic = open("pass.txt", "a")    #保存
for i in r:
    dic.write("".join(i))
    dic.write("".join("\r"))
dic.close()
