"""
　defaultdict：处理找不到的键的一个选择
"""
import sys
import re
import collections

WORD_RE = re.compile(r'\w+')
"""
　1.dd['new-key'] 找不到 键 new-key
  2.调用list() 来建立一个新列表
  3.把这个新列表作为值，'new-key' 作为它的键，放到dd中
  4.返回这个列表的引用
"""

WORD_RE = re.compile(r'\w+')
index = collections.defaultdict(list)
with open("zen.txt", encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            #defaultdict 里的default_factory 只会在__getitem__ 里被调用即index[word]
            index[word].append(location)

for word in sorted(index,key=str.upper):
    print(word,index[word])

