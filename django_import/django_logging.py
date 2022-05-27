"""
https://zhuanlan.zhihu.com/p/133864368
https://www.cnblogs.com/lxc123/p/14391429.html
https://docs.djangoproject.com/zh-hans/2.0/topics/logging/

logging 结构包括Loggers、Handlers、Filters 和 Formatters

Logger:记录器,是日志系统的入口,
1.向应用程序公开几种方法（logger.debug(),logger.info(),logger.warning(),logger.error(),logger.critical(),logger.log(),logger.exception()），以便运行时记录消息
2.根据传递给 Logger 的消息的严重性，确定消息是否需要处理
3.将需要处理的消息传递给所有感兴趣的处理器 Handler
DEBUG：排查故障时使用的低级别系统信息，通常开发时使用
INFO：一般的系统信息，并不算问题
WARNING：描述系统发生小问题的信息，但通常不影响功能
ERROR：描述系统发生大问题的信息，可能会导致功能不正常
CRITICAL：描述系统发生严重问题的信息，应用程序有崩溃的风险

Handlers:处理器,决定如何处理Logger中的每一条记录,如把消息输出到控制台，文件，Email中,
    Handler 也有级别的概念。如果一条日志记录的级别不匹配或者低于 Handler 的日志级别，则会被 Handler 忽略

Filters:过滤器,在日志记录从 Logger 传到 Handler 的过程中，使用 Filter 来做额外的控制。例如，只允许某个特定来源的 ERROR 消息输出

Formaters:格式化器，主要功能是确定最终输出的形式和内容。

"""

"""实现方式"""
import os
# 1.文件开头 import logging
import logging

logging.basicConfig(
    format='%(asctime)s - %(pathname)s[%(lineno)d] - %(levelname)s: %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)

def my_view(request, arg1, arg):

    if True:
        # Log an error message
        logger.error('Something went wrong!')

# 2. 自定义类
settings = ""
class CommonLog(object):
    """
    日志记录
    """
    def __init__(self, logger, logname='web-log'):
        self.logname = os.path.join(settings.LOGS_DIR, '%s' % logname)
        self.logger = logger
        self.logger.setLevel(logging.DEBUG)
        self.logger.propagate = False
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', '%Y-%m-%d %H:%M:%S')

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.handlers.TimedRotatingFileHandler(self.logname, when='MIDNIGHT', interval=1, encoding='utf-8')
        # fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')
        fh.suffix = '%Y-%m-%d.log'
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)
# 3.django 中间件
# 中间件日志代码一共分三个部分，分别是：Filters 代码，middleware 代码，settings 配置
import json,threading,socket
MiddlewareMixin= ""

local = threading.local()


class RequestLogFilter(logging.Filter):
    """
    日志过滤器
    """

    def filter(self, record):
        record.sip = getattr(local, 'sip', 'none')
        record.dip = getattr(local, 'dip', 'none')
        record.body = getattr(local, 'body', 'none')
        record.path = getattr(local, 'path', 'none')
        record.method = getattr(local, 'method', 'none')
        record.username = getattr(local, 'username', 'none')
        record.status_code = getattr(local, 'status_code', 'none')
        record.reason_phrase = getattr(local, 'reason_phrase', 'none')

        return True


class RequestLogMiddleware(MiddlewareMixin):
    """
    将request的信息记录在当前的请求线程上。
    """

    def __init__(self, get_response=None):
        self.get_response = get_response
        self.apiLogger = logging.getLogger('web.log')

    def __call__(self, request):

        try:
            body = json.loads(request.body)
        except Exception:
            body = dict()

        if request.method == 'GET':
            body.update(dict(request.GET))
        else:
            body.update(dict(request.POST))

        local.body = body
        local.path = request.path
        local.method = request.method
        local.username = request.user
        local.sip = request.META.get('REMOTE_ADDR', '')
        local.dip = socket.gethostbyname(socket.gethostname())

        response = self.get_response(request)
        local.status_code = response.status_code
        local.reason_phrase = response.reason_phrase
        self.apiLogger.info('system-auto')

        return response

"================================================"
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
      # 自定义中间件添加在最后
    'lib.log_middleware.RequestLogMiddleware'
]

LOGGING = {
    # 版本
    'version': 1,
    # 是否禁止默认配置的记录器
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '{"time": "%(asctime)s", "level": "%(levelname)s", "method": "%(method)s", "username": "%(username)s", "sip": "%(sip)s", "dip": "%(dip)s", "path": "%(path)s", "status_code": "%(status_code)s", "reason_phrase": "%(reason_phrase)s", "func": "%(module)s.%(funcName)s:%(lineno)d",  "message": "%(message)s"}',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    # 过滤器
    'filters': {
        'request_info': {'()': 'lib.log_middleware.RequestLogFilter'},
    },
    'handlers': {
        # 标准输出
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        # 自定义 handlers，输出到文件
        'restful_api': {
            'level': 'DEBUG',
            # 时间滚动切分
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOGS_DIR, 'web-log.log'),
            'formatter': 'standard',
            # 调用过滤器
            'filters': ['request_info'],
            # 每天凌晨切分
            'when': 'MIDNIGHT',
            # 保存 30 天
            'backupCount': 30,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False
        },
        'web.log': {
            'handlers': ['restful_api'],
            'level': 'INFO',
            # 此记录器处理过的消息就不再让 django 记录器再次处理了
            'propagate': False
        },
    }
}