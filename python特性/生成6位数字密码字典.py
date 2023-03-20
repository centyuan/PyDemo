import itertools as its

# words = "abcdefghijklmnopqrstuvwxyz1234567890"
words = '1234567890'
dict_f = {"f" + str(i): open("pass" + str(i) + ".txt", "a") for i in range(0, 10)}
r = its.product(words, repeat=6)
for item in r:
    f = None
    for i in range(0, 10):
        if int(item[0]) == i:
            f = dict_f["f" + str(i)]
            break
    if f:
        f.write("".join(item))
        f.write("".join("\r"))
    else:
        break
