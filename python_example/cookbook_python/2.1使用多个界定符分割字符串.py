"""
split():只适应简单的字符串分割,不允许多个分隔符

"""

import re

# 1.
line = 'asdf fjdk; afed, fjek,asdf, foo'
re.split(r'[;,\s]\s*', line)
# \s匹配所有空白符
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# 2.使用()捕获分组:结果会包含分隔符
fields = re.split(r'(;|,|\s)\s*', line)
# fields 包含了分隔符
# ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']

# 3.(?:pattern) 可以不获取匹配结果
fields = re.split(r'(?:;|,|\s)\s*',line)
print(fields)
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
line.startswith()