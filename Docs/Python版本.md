#### 前言

>[Python](https://so.csdn.net/so/search?q=Python&spm=1001.2101.3001.7020) 的版本主要分为 `2.×` 、 `3.×` 两个系列。
>
>- Python3 计划每年发布一个新的子版本，每次只增加两三种新语法



##### Python 3.0

>2008 年发布: https://www.python.org/download/releases/3.0/
>
>- **统一的字符串类型**：`str`类型包含Unicode字符，`bytes`类型用于二进制数据。
>- **print函数**：将`print`语句改成了函数，强制使用括号 `print()`
>- **除法操作**：整数除法返回浮点数（即 `/` 操作符），使用 `//` 表示整除
>- **移除老旧特性**：如 `<>` 比较操作符（使用 `!=` 代替）、`old-style classes` 等。
>- **迭代器行为的一些变化**：如 `range()`返回range对象而非列表。

##### Python 3.1

>2009年发布: https://www.python.org/download/releases/3.1/
>
>- **性能增强**：比如 `OrderedDict`、`io`模块性能提升。
>- **新增`math`和`cmath`函数**：如 `math.factorial()`。
>- **字符串格式化**：新增 `str.format()` 的增强机制。
>- **其他改进**：如`functools.lru_cache` 和 `collections.Counter`。

##### Python 3.2

>2011年发布:https://www.python.org/downloads/release/python-320/
>
>- **新增 `lzma` 模块**：支持 `.xz` 格式压缩
>- **相对导入增强**：简化了包结构和导入机制。
>- **性能提升和 bug 修复**。
>- **concurrent.futures**：新增的标准库模块，用于并发编程。

##### Python 3.3

>2012年发布: https://www.python.org/downloads/release/python-330/
>
>- **虚拟环境**：内置 `venv` 模块，用于创建虚拟环境
>- **新的语法**：如 `yield from` 表达式。
>- **性能提升**：如 `key-sharing dictionaries` 优化了内存使用。
>- **新的错误处理**：如新的 `ChainMap` 容器类型和`faulthandler`模块。

##### Python 3.4

>2014 年发布：https://www.python.org/downloads/release/python-340/
>
>- **asyncio**：引入了 `asyncio` 模块，用于异步编程
>- **Pathlib**：引入了 `pathlib` 模块，用于面向对象的文件系统路径操作。
>- **标准库改进**：如 `enum` 模块、`statistics` 模块（提供了求平均值、中位数、方差等运算的函数）、新增的 `tracemalloc` 内存分析工具。
>- **pip**：`将 `pip` 集成到标准库中。

##### Python 3.5

>2015 年发布：https://www.python.org/downloads/release/python-350/
>
>- 迭代拆包符*,字典拆包符**
>- 增加语法: 百分号 `%` 来格式化字符串
>- 增加关键字 `async`、`await` ，用于定义协程
>- 增加语法: 类型注释(type annotations)
>- 增加标准款typing：定义了一些类型，用于类型注释
>- 增加标准款zipapp: 将 Python 脚本打包成可执行的归档文件，扩展名为 .pyz

##### Python 3.6

>2016 年发布：https://www.python.org/downloads/release/python-360/
>
>- dict底层结构改变,dict按插入有序
>- 增加语法:数字中插入下划线，提高可读性
>- **增加语法:f-string**
>- **增加标准库secrets**,用于生成安全的随机数(random生成的随机数可能被预测)
>- **Async Generators & Comprehensions**：支持异步生成器和异步推导式。
>- **小数支持增强**：如 `decimal` 模块的性能优化。

##### Python 3.7

>2018 年发布：https://www.python.org/downloads/release/python-370/
>
>- **数据类**：`dataclasses` 模块新增，用于自动生成特殊方法的简便类定义。
>- **时间函数的高精度**：如新的 `time` 模块函数提供更高的时间精度。
>- **决定性显存器**：CPython 实现引入了隐式的 **slots** 限制。
>- **Async/Await**：异步和等候的改进和语法变化（如移除旧的 `@coroutine` 修饰方式）。

##### Python 3.8

>2019年发布: https://www.python.org/downloads/release/python-380/
>
>- **:= 运算符**：引入 “海象操作符” 允许在表达式中进行赋值。
>- **位置参数**：允许参数限定为仅限于位置的写法，用做函数定义增强(定义函数时，在正斜杆 / 之前的参数都会被视作位置参数)。
>- **字典合并**：增加了字典的多个合并拼接写法。
>- **f-string 插入变量的值**: 
>- 语言的一些性能提升和优化：删除了 GIL（全局解释器锁）对于多线程的限制。

##### Python 3.9

>2020年发布: https://www.python.org/downloads/release/python-390/
>
>**whatnews**: https://docs.python.org/zh-cn/3.9/whatsnew/3.9.html
>
>- **字典操作** : dict 类增加合并运算符 `|`、更新运算符 `|=`
>- **Type hinting 的改进**：增加了支持更多类型的语法，例如 Union 以及 Literal 类型
>- **简化了异常和错误处理机制**：引入了新的异常处理语法，使得代码可读性和可维护性更好

##### Python 3.10

>2021 年发布：https://www.python.org/downloads/release/python-3100/
>
>- **match 语法**: match-case 模式匹配
>- **更加友好的错误提示**
>- **类型联合**：用 `|` 运算符连接多个类型，表示 Union 类型
>-  在对大型网络包进行序列化/反序列化的时候提高了性能。

##### Python 3.11 

>2022年发布: https://www.python.org/downloads/release/python-3110/
>
>- CPython 解释器优化了加载模块、调用函数等操作，使得 Python3.11 比 Python3.10 的启动速度、运行速度快了 10%~60% 。
>
>- `typing.Self`: 类型提示可以使用self
>
>- typing.TypedDict,typing.NotRequired,typing.Required
>
>- 异常处理改进
>  ```
>  1.多异常处理,增加了标准异常类型 BaseExceptionGroup、ExceptionGroup ，用于将多个异常打包为一组。异常组只能用语法 except* 捕捉
>  2.Zero-cost异常:  
>  ```



##### Python 3.12

> 2023 年发布：https://www.python.org/downloads/release/python-3120/
>
>**解释器隔离**：在一个Python进程可以有多个解释器,一定程度缓解了GIL带来的问题
>`在 3.12 版本当中可以创建子解释器，可以为每个子解释器单独创建一个 GIL，这样就可以让 Python 充分利用多核的性能。目前在 CPython3.12 当中只能够通过 C 扩展 API 创建，在 Python 层面当中还不能够使用，预计在 CPython3.13 当中能够直接在 Python 层面进行调用`
>
>- **f-string增加了几种语法**
>- 简化泛型语法
>- 支持 Linux `perf` 探查器在跟踪中报告 Python 函数名称
