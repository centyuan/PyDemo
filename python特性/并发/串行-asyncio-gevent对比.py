import time
import asyncio
import gevent
from gevent import monkey

# 定义个函数模拟耗时io处理
def read(url):
    print('open url:', url)
    time.sleep(5)
    return f'url:{url}'


urls = ['https://www.bilibili.com/', 'https://www.mgtv.com/']
# 1.普通顺序执行
start_time = time.time()
for url in urls:
    read(url)
print('顺序执行time cost:', time.time() - start_time)

# 2.使用gevent
# 加monkey patch才可以不然还是顺序执行
monkey.patch_all(thread=False)  # thread=False使多线程不阻塞
start_time = time.time()
gevent.joinall([
    gevent.spawn(read, url) for url in urls
])
print('gevent执行time cost:', time.time() - start_time)


# 3.asyncio
async def read(url):
    print('open url:', url)
    await asyncio.sleep(5)
    return f'url:{url}'

start_time = time.time()
loop = asyncio.get_event_loop()
tasks = [read(url) for url in urls]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
print('asyncio执行time cost:',time.time()-start_time)