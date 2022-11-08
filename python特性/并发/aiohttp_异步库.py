import asyncio
import aiohttp

"""https://zhuanlan.zhihu.com/p/59621713"""

urls = [
    'http://www.163.com/',
    'http://www.sina.com.cn/',
    'https://www.hupu.com/',
    'http://www.csdn.net/'
]

async def get_http_data(url):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as res:
                global count
                count += 1
                print(count, res.status,res.text())
    return res.headers

async def main(url):
    """
    主调度函数
    :param u:
    :return:
    """
    res = await get_http_data(url)
    return res

if __name__ == '__main__':
    count = 0
    semaphore = asyncio.Semaphore(500)
    loop = asyncio.get_event_loop()
    tasks = [main(i) for i in urls]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    print(tasks)



"""
问题：ValueError:too many file descriptors in select()
原因分析：使用aiohttp时，python内部会使用select()，操作系统对文件描述符最大数量有限制，
linux为1024个，windows为509个
解决方案：限制并发数量（一般500），若并发的量不大可不作限制
1.如windows下使用loop = asyncio.ProactorEventLoop() 

限制并发数量方法(此方法也可用来作为异步爬虫的限速方法（反反爬）)


"""