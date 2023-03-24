"""
你可能有大量的代码，由不同的人来分散地维护。每个部分被组织为文件目录，如一个包。
如下:
foo-package/
    spam/
        blah.py

bar-package/
    spam/
        grok.py

# 在这里工作的机制被称为“包命名空间”的一个特征
关键是确保顶级目录中没有 __init__.py 文件来作为共同的命名空
间。缺失 __init__.py 文件使得在导入包的时候会发生有趣的事情：这并没有产生错
误，解释器创建了一个由所有包含匹配包名的目录组成的列表。特殊的包命名空间模块
被创建，只读的目录列表副本被存储在其 __path__ 变量中。
"""


# 删除了__init__.py，两个都有共同的命名空间spam
import sys

sys.path.extend(['foo-package', 'bar-package'])
# 可以这样导入
# import spam.blah
# import spam.grok
