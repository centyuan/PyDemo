from memory_profiler import profile
import time
"""
memory_profiler：是按每行代码查看内存占用的工具
"""

@profile
def readiso():
    start_time = time.time()
    count = 0
    with open('60960684_p0.png', 'rb') as f:
        f.seek(0, 2)
        total = f.tell()
        f.seek(count)
        res = f.read(count + 1024*1024*10)
        count += 1024*1024*10
        print(f'{count}/{total}')
    end_time = time.time()
    print('cost time:', end_time-start_time)


readiso()
