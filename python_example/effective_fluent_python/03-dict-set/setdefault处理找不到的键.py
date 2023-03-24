"""
当字典d[k] 不能找到正确的键的时候，Python 会抛出异常，这个行为符合Python 所信奉的
“快速失败”哲学。也许每个Python 程序员都知道可以用d.get(k, default) 来代替d[k]，
给找不到的键一个默认的返回值

"""
import sys
import re

# [\w] \w+ 都是匹配数字和字母下划线的多个字符
# [\w+]   表示匹配数字、字母、下划线和加号本身字符
WORD_RE = re.compile(r'\w+')
index = {}
# enumerate 对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列
# print(sys.argv[1])
# Q:从索引中获取单词出现的频率信息，并把它们写进对应的列表里
# with open(sys.argv[1],encoding='utf-8') as fp:
with open("zen.txt", encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        # re.finditer和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回
        for match in WORD_RE.finditer(line):
            word = match.group()
            print(match, word)
            column_no = match.start() + 1
            location = (line_no, column_no)
            # occurrences = index.get(word, [])
            # occurrences.append(location)
            # index[word] = occurrences

            # 和上面效果一样,下面比上面少两次键查询
            index.setdefault(word, []).append(location)
        print("______________________")

"""以字母顺序打印出结果"""
print(index)
"""sorted 函数的key= 参数没有调用str.uppper，而是把这个方法的引用传递给sorted 函数，这样在排序的时候，单词会被规范成统一格式"""
for word in sorted(index, key=str.upper):
    print(word, index[word])
