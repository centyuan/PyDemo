# -*- coding:utf-8 -*-
# Author centyuan
# Date 2019/11/20 11:16



"""
format常用格式说明
%(levelno)s: 打印日志级别的数值
%(levelname)s: 打印日志级别名称
%(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
%(filename)s: 打印当前执行程序名
%(funcName)s: 打印日志的当前函数
%(lineno)d: 打印日志的当前行号
%(asctime)s: 打印日志的时间
%(thread)d: 打印线程ID
%(threadName)s: 打印线程名称
%(process)d: 打印进程ID
%(message)s: 打印日志信息

"""

# 1.日志输出到控制台
import logging
import os

# logging.basicConfig函数进行配置了日志级别和日志内容输出格式；因为级别为DEBUG
# 所以会将DEBUG级别以上的信息都输出显示再控制台上。
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s",
)  

logging.info("this is a loggging info message")
logging.debug("this is a loggging debug message")
logging.warning("this is loggging a warning message")
logging.error("this is an loggging error message")
logging.critical("this is a loggging critical message")

# 2.日志输出到文件
import logging  # noqa: E402

# 1 创建一个logger
logger = logging.getLogger()
# logger.setLevel(logging.INFO)


# 2 创建一个handler，用于写入日志文件
fh = logging.FileHandler("logging_test.log")
fh.setLevel(logging.DEBUG)  # 设置日志级别

# 3 定义handler的输出格式
log_formatter = logging.Formatter(
    "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"
)
fh.setFormatter(log_formatter)  # 设置Formatter

# 4 将logger添加到handler里面
logger.addHandler(fh)  # 添加一个Handler logger.removeHanlder() 删除一个handler

# 5 traceback模块被用于跟踪异常返回信息，可以在logging中记录下traceback，

try:
    open("sklearn.txt", "rb")
    raise ValueError("错误")
except Exception:
    # 下面三种方式三选一，推荐使用第一种
    logging.exception("Exception occurred")
    logging.error("Exception occurred", exc_info=True)
    logging.log(level=logging.DEBUG, msg="Exception occurred", exc_info=True)
    """
    当发生异常时，直接使用无参数的 debug()、info()、warning()、error()、critical() 方法并不能记录异常信息，
    需要设置 exc_info 参数为 True 才可以，或者使用 exception() 方法，还可以使用 log() 方法，
    但还要设置日志级别和 exc_info 参数。"""

logger.info("Finish")


# 3. logging项目使用
from logging.handlers import RotatingFileHandler  # noqa: E402


class Logger:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self,
             log_path:str = None, 
             log_name: str = "access.log", 
             log_level = logging.DEBUG,
             To_console = True,
             To_file = False,
             To_ES = False,
             ROTA = False,
             ):
        if not log_path:
            log_path = os.getcwd() + os.sep + "logs"+os.sep # os.sep 路径分隔符(Linux使用/,window使用\)

      
        log_formatter = logging.Formatter(
            fmt=" %(asctime)s.%(msecs)03d  |  %(levelname)s  |  %(filename)s |  %(lineno)d  |  %(message)s",
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


# 4.日志写入ES
"""
三种方案
flume+kafka+spark准实时写入ES
logging+CMRESHanlder实时写入ES
通过python elasticsearch包
"""
from cmreslogging.handlers import CMRESHandler  # noqa: E402

cm_handler = CMRESHandler(
    hosts=[{"host": "localhost", "port": 9200}],
    es_index_name="log_index",
    auth_type=CMRESHandler.AuthType.NO_AUTH,
)
logger = logging.getLogger("ES_log")
logger.setLevel(logging.INFO)
logger.addHandler(cm_handler)
logger.info("ES日志")

# 5. loguru
