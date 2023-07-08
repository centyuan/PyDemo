import itertools as its

# words = "abcdefghijklmnopqrstuvwxyz1234567890"
words = '1234567890'
dict_f = {"f" + str(i): open("pass" + str(i) + ".txt", "a") for i in range(0, 10)}
r = its.product(words, repeat=6)
for item in r:
    f = dict_f["f" + str(item[0])]
    f.write("".join(item))
    f.write("".join("\r"))

