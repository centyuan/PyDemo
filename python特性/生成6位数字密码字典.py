import itertools as its

# words = "abcdefghijklmnopqrstuvwxyz1234567890"
words = '1234567890'
r = its.product(words,repeat=6)
dic = open("pass.txt", "a")    #保存
for i in r:
    dic.write("".join(i))
    dic.write("".join("\r"))
dic.close()

