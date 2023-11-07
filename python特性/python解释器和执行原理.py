
"""
一：解释器
https://zhuanlan.zhihu.com/p/661894167
1.CPython

2.Pyston
  从CPyhton解释器衍生出的分支，实现了性能优化，有可能加速高达30%，由于缺乏兼容的二进制包，需要重新编译
  
3.PyPy
  采用了RPython编写的PyPy是一个专为Python配备的即时JIT编译器，RPython是Python的一个静态类型的子集，不同于CPyton解释器，PyPy对源代码进行编译，生成CPU可直接运行的机器码。
  由于JIT特性，执行速度更快，长时间运行的应用更能从缓冲中受益，大部分的C扩展模块都在PyPy中得到支持,根据官网的基准测试数据，它比CPython实现 的Python要快6倍以上
  由于历史原因，目前pypy中 还保留着GIL，不过正在进行的STM项目试图将PyPy变成没有GIL的Python。
  如果python程序中含有C扩展(非cffi的方式)，JIT的优化效果会大打折扣，甚至比CPython慢（比 Numpy）。
  所以在PyPy中最好用纯Python或使用cffi扩展。 随着STM，Numpy等项目的完善，相信PyPy将会替代CPython。
  详细描述了CPython和PyPy的不同：https://doc.pypy.org/en/latest/cpython_differences.html

4.RustPython
  由Rust编写的Python解释器，RustPython和CPython类似，但可以选择启用JIT编译器
5.Stackless Python
6.Micro Python

性能可以使用Cython或Nuitka将python代码编译成c，再编译成机器码

二：执行原理
python代码真正被CPU运行前，Python先把代码（.py文件）编译成字节码，交给字节码虚拟机，然后虚拟机一条一条执行字节码指令，从而完成程序的执行。

包括以下四个步骤
1.词法分析
2.解析-解析器检查语法和语义规则生成抽象语法树AST
3.编译-编译器会根据AST创建python字节码，这些字节码很基础，和平台无关的指令组成
4.解释-解释器处理字节码

字节码：
  字节码在Python虚拟机程序里对应的是PyCodeObject对象。
  .pyc文件是字节码在磁盘上的表现形式。

 pyc文件：
    PyCodeObject对象的创建时机是模块加载的时候，即import。
  Python test.py会对test.py进行编译成字节码并解释执行，但是不会生成test.pyc。
 如果test.py加载了其他模块，如import util，Python会对util.py进行编译成字节码，生成util.pyc，然后对字节码解释执行。
 如果想生成test.pyc，我们可以使用Python内置模块py_compile来编译。
 加载模块时，如果同时存在.py和.pyc，Python会尝试使用.pyc，如果.pyc的编译时间早于.py的修改时间，则重新编译.py并更新.pyc。
  
 """