---
title: Python项目中日志处理
categories:
  - Python从入门到放弃
tags:
  - Logging
---

#### logging

>logging是Python内置的标准模块，可以设置输出日志等级，时间，其他信息(进程ID,进程名词,线程ID,线程名称)
>
>参考:
>
>[Python的日志记录工具](https://docs.python.org/zh-cn/3/library/logging.html)
>
>[Python日志指南](https://docs.python.org/zh-cn/3/howto/logging.html)



##### 输出到控制台

```
import logging 

logging.basicConfig(
	level=logging.DEBUG,
	format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s:%(message)s"
)
logging.info("this is a loggging info message")
logging.debug("this is a loggging debug message")
logging.warning("this is loggging a warning message")
logging.error("this is an loggging error message")
logging.critical("this is a loggging critical message")


------------------------------------------------------------------------------------------------------------
logging.DEBUG：DEBUG以上的日志会输出
format常用格式说明:
%(levelno)s: 日志级别
%(levelname)s: 日志级别名词
%(pathname)s: 执行程序的路径,就是sys.argv[0]
%(funcName)s: 当前函数
%(lineno)d: 当前行号
%(asctime)s: 时间
%(thread)d: 线程ID
%(threadName)s: 线程名称
%(process)d: 进程ID
%(message)s: 日志信息
```



##### 输出到文件

```
import logging 

# 1.创建一个logger
logger = logging.getLogger()

# 2.创建一个handler，用于日志写入文件
log_file = "logging-test.log"
fh = logging.FileHandler(log_file)
fh.setLevel(logging.DEBUG)

# 3.定义handler输出格式
log_formatter = logging.Formatter( "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(log_formatter)

# 4.将logger添加到handler里面
logger.addHandler(fh)

logger.info("Finish")

```



##### 输出到ES

>三种方案:
>
>​	flume+kafka+spark准实时写入ES
>
>​	logging+CMRESHanlder实时写入ES
>
>​	通过python elasticsearch包

```
from cmreslogging.handlers import CMRESHandler  # noqa: E402

logger = logging.getLogger("ES_log")
logger.setLevel(logging.INFO)
# ES handler 
cm_handler = CMRESHandler( 
	hosts=[{"host": "localhost", "port": 9200}],
    es_index_name="log_index",
    auth_type=CMRESHandler.AuthType.NO_AUTH,)
    
logger.addHandler(cm_handler)
logger.info("ES日志")

```



##### logging项目中使用

```
import os
import logging
from logging.handlers import RotatingFileHandler  # noqa: E402

class Logger:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self,
             log_path:str = None, 
             log_name: str = "application.log", 
             log_level=logging.DEBUG,
             To_console = True,
             To_file = False,
             To_ES = False,
             ROTA = False,
             ):
        if not log_path:
            log_path = os.getcwd() + os.sep + "logs"+os.sep # os.sep 路径分隔符(Linux使用/,window使用\)

      
        log_formatter = logging.Formatter(
            fmt="[%(asctime)s.%(msecs)03d][%(levelname)s][%(filename)s][%(lineno)d] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        self.logger = logging.getLogger()
        self.logger.setLevel(log_level)

        # 1.console流handler 输出到sys.stdout,sys.stderr输出到控制台
        if To_console:
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(log_formatter)
            self.logger.addHandler(stream_handler)
        
        # 2.文件
        if To_file:
            #self.logger = logging.getLogger(log_path)
            if ROTA: # RotatingFileHandler 循环日志文件
                rota_log = log_path+"rotate_"+log_name
                if not os.path.exists(rota_log):
                    os.makedirs(rota_log)
                rotate_handler = RotatingFileHandler(rota_log, maxBytes=1024 * 1024 * 50, backupCount=5)
                # maxBytes 最大字节数,backupCount 超过最大字节数保留5个
                self.logger.addHandler(rotate_handler)
            else:
                log_file = log_path+log_name
                if not os.path.exists(log_file):
                    os.makedirs(log_file)
                fh = logging.FileHandler(log_file)
                fh.setFormatter(log_formatter)
                self.logger.addHandler(fh)
        # TimedRotatingFileHandler 定时生成新日志文件

        # 3. ES
        if To_ES:
            cm_handler = CMRESHandler(
                hosts=[{"host": "localhost", "port": 9200}],
                es_index_name="log_index",
                auth_type=CMRESHandler.AuthType.NO_AUTH,
            )
            cm_handler.setFormatter(log_formatter)
            self.logger.addHandler(cm_handler)

    
     

    def get_logger(self):
        return self.logger


logger = Logger().get_logger()
logger.info("日志")

```

>**RotatingFileHandler:**
>
>自带的日志处理器,将日志写入到指定的文件中，并控制文件大小和数量,实现日志轮转(及备份旧日志并创建新的日志)
>
>```
>from logging.handlers import RotatingFileHandler
>RotatingFileHandler(filename, mode='a', maxBytes=0, backupCount=0, encoding=None, delay=False)
>
>filename: 指定日志的文件路径和名称
>model: 模式,可选值为 ‘a’ 或 ‘w’,追加或覆盖
>maxBytes: 单个日志文件调度最大大小(单位:字节),当日志文件达到该大小时，会自动备份旧日志并创建新的日志文件。默认值为 0，表示不限制日志文件大小。
>backupCount: 备份文件数量,当生成的日志文件数量超过该数目时，会自动删除旧的备份日志文件。默认值为 0，表示不备份
>encoding: 日志文件的编码格式,默认为None,表示使用系统编码
>delay: True(延时打开文件,即在第一次写入日志时才打开日志文件),False(表示在初始化时即打开日志文件。默认值为 False)
>
>为maxBytes指定了>0的值，则mode指定为w是没有意义的，RotatingFileHandler初始化时会自动将mode强制改为a
>```
>
>**TimedRotatingFileHandler:**
>
>与RotatingFileHandler类似,按照时间对文件进行切割，例如每天或每个小时生成一个新的日志文件
>
>```
>from logging.handlers import TimedRotatingFileHandler
>
>TimedRotatingFileHandler(filename, when='h', interval=1, backupCount=0, encoding=None, delay=False, utc=False, atTime=None)
>
>filename: 指定日志文件的路径和名称
>when: 日志轮转的时间间隔，可选值为 ‘S’、‘M’、‘H’、‘D’、‘W’ 和 ‘midnight’，分别表示秒、分、时、天、周和每天的午夜；默认值为 ‘midnight’，即每天的午夜轮转，值不区分大小
>internal: 时间间隔的数量，默认为 1；例如，当 when=‘D’ 且 interval=7 时，表示每周轮转一次
>backupCount: 备份文件数目；当生成的日志文件数量超过该数目时，会自动删除旧的备份日志文件；默认值为 0，表示不备份
>encoding: 日志文件的编码格式，默认为 None，表示使用系统默认编码
>delay: 可选值为 True 和 False；当为 True 时，表示延时打开文件，即在第一次写入日志时才打开日志文件；当为 False 时，表示在初始化时即打开日志文件；默认值为 False
>utc：是否使用 UTC 时间，默认为 False，表示使用本地时间
>atTime：用来设置轮转时间，格式为 ‘%H:%M:%S’，默认为午夜 12 点；需要注意的是该参数仅在when为W/midnight时有效
>```



##### 异步线程写日志

>独立开启线程，将待写的日志信息异步放入队列，做到日志输出不影响主流程性能
>
>参考:
>
>[异步线程写日志](https://www.cnblogs.com/yindianhaidao/p/13201074.html)

#### [logru](https://github.com/Delgan/loguru)

>支持Python3.5以上，日志格式输出更加优雅简洁,配置将半结构化和彩色化的输出记录到标准错误，可以使用装饰器对**异常进行追溯**
>
>参考:
>
>[logru docs](https://loguru.readthedocs.io/en/stable/overview.html)
>
>[logru doc汉化](https://www.cnblogs.com/struggleMan/p/17510494.html#%E5%BC%82%E6%AD%A5%E7%BA%BF%E7%A8%8B%E5%AE%89%E5%85%A8%E5%A4%9A%E8%BF%9B%E7%A8%8B%E5%AE%89%E5%85%A8)
>
>



#### [logbook](https://github.com/getlogbook/logbook)

>自称是 Python 标准库`logging`模块的酷炫替代品，其目的是让日志记录变得有趣
>
>参考：
>
>[Logbook docs](https://logbook.readthedocs.io/en/stable/)