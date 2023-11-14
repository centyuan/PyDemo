"""
通过使用python内置断点工具调试
python3.7之前,叫pdb,python debugger
python3.7之后,breakpoint作为关键字,作为断点插入
"""
"""
# 1.pdb
    # 非浸入式    
    python -m pdb filename.py   
    # 浸入式修改
    import pdb;pdg.set_trace()

# 2.breakpoint
    breakpoint()
pdb相关命令:
查看源代码:
    l或ll
添加断点
    b
    b lineno行号
    b filename文件名:lineno行号
    b functionname函数名
添加临时断点
    tbreak
    tbreak lineno
    tbreak filename:lineno
    tbreak functionname
清除断点
    cl
    cl filename:lineno
    cl bpnumber断点序号
打印变量
    p 
逐行调试
    s 执行下一行,能够进入函数体
    n 执行下一行,不进入函数体
    r 执行下一行,在函数中会执行到函数返回出
非逐行调试
    c 持续执行下去,直到遇到一个断点
    unt lineno行号 持续执行下去直到指定行
    j lineno行号 直接跳到指定行,被跳过的代码不执行
查看函数参数
    a 
打印变量类型
    whatis 

启动交互式解释器
    interact
打印堆栈信息
    w
退出pdb
    q

"""