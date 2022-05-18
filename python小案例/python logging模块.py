# -*- coding:utf-8 -*-
# Author centyuan
# Date 2019/11/20 11:16

import logging
logging.debug(u"苍井空")
logging.info(u"麻生希")
logging.warning(u"小泽玛利亚") # 默认生成的root logger的level是logging.WARNING,低于该级别的就不输出了
logging.error(u"桃谷绘里香")
logging.critical(u"泷泽萝拉")

# 1.日志输出到控制台
import logging  # 引入logging模块
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  # logging.basicConfig函数对日志的输出格式及方式做相关配置
# logging.basicConfig函数进行配置了日志级别和日志内容输出格式；因为级别为DEBUG
# 所以会将DEBUG级别以上的信息都输出显示再控制台上。
logging.info('this is a loggging info message')
logging.debug('this is a loggging debug message')
logging.warning('this is loggging a warning message')
logging.error('this is an loggging error message')
logging.critical('this is a loggging critical message')


# 2.日志输出到文件
import logging
# 1 创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
log_path = ''
log_file = log_path + 'logging_test.log'
# 2 创建一个handler，用于写入日志文件
fh = logging.FileHandler(log_file)
fh.setLevel(logging.DEBUG)  # 设置日志级别
# 3 定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)  # 设置Formatter
# 4 将logger添加到handler里面
logger.addHandler(fh)  # 添加一个Handler logger.removeHanlder() 删除一个handler
# 5 traceback模块被用于跟踪异常返回信息，可以在logging中记录下traceback，

try:
    open("sklearn.txt","rb")
    raise ValueError("错误")
except Exception as e:
    # 下面三种方式三选一，推荐使用第一种
    logging.exception("Exception occurred")
    logging.error("Exception occurred", exc_info=True)
    logging.log(level=logging.DEBUG, msg="Exception occurred", exc_info=True)
    """
    当发生异常时，直接使用无参数的 debug()、info()、warning()、error()、critical() 方法并不能记录异常信息，
    需要设置 exc_info 参数为 True 才可以，或者使用 exception() 方法，还可以使用 log() 方法，
    但还要设置日志级别和 exc_info 参数。"""

logger.info("Finish")

"""
6、format常用格式说明
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