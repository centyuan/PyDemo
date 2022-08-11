from multiprocessing.dummy import Pool as ThreadPool  # 线程池
from multiprocessing.pool import ThreadPool  # 线程池，用法无区别，唯一区别这个是线程池

from concurrent.futures import ThreadPoolExecutor  # python原生线程池，这个更主流
# import threadpool  # 线程池，需要 pip install threadpool，很早之前的
