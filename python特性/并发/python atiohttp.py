"""
aiohttp:Async HTTP client/server for asyncio and Python
用于异步和Python的异步HTTP客户端/服务器
"""
import asyncio
import aiohttp


# 1.get，post请求及参数
async def get_http_data(url, timeout=aiohttp.ClientTimeout(total=30)):
    # 1.创建一个ClientSession对象
    # data = {'key':'value'}
    # headers = {'content-type':'image/gif'}
    # cookeis = {'cookies':'working'}
    # url = 'http://httpbin.org/post'
    params = {'name': 'yuan'}
    # timeout 超时设置
    async with aiohttp.ClientSession(timeout=timeout) as session:
        # 2.发送请求
        # async with session.post(url,data=data,headers=headers,cookeis=cookeis) as res:
        async with session.get(url, params=params) as res:
            # 3.await 异步等待返回结果
            print(res.status)
            print(await res.text())
            return await res.text()


loop = asyncio.get_event_loop()
task = loop.create_task(get_http_data('http://httpbin.org/get'))
loop.run_until_complete(task)


# 2. 流式响应内容（Streaming Response Content）

async def get_streaming_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            print('res.content:',res.content)
            print('await res.conten.read():',res.content.read())
            with open('test.txt','wb') as f:
                while 1:
                    chunk = await res.content.read()
                    if not chunk:
                        break
                    f.write(chunk)

loop = asyncio.get_event_loop()
task = loop.create_task(get_streaming_data('https://api.github.com/events'))
loop.run_until_complete(task)