from concurrent.futures import ThreadPoolExecutor
import asyncio
import os
import requests

ex = ThreadPoolExecutor(2)
asyncio.get_event_loop().set_default_executor(ex)

async def down_one(loop,url):
    name = os.path.basename(url)
    print("down_one:start{}".format(name))
    result = await loop.run_in_executor(None,requests.get,url)
    print('down_one:middle{}'.format(name))
    if result.status_code==200:
        with open(name,"wb") as fp:
              r = await loop.run_in_executor(None,fp)
              print("down_one:r={}".format(r))
    print("downone:endxx {}".format(name))
    return "ok {}".format(name)

async def deal(loop):
    ts = []
    for i in range(1, 20):
        name = str(i) + ".mp3"
        path = "http://mp3-d.xxx.com:9090/有声书/闪婚剩女" + "/" + name
        ts.append(asyncio.ensure_future(down_one(loop, path)))
    print("deal: middle")
    result = await asyncio.gather(*ts)
    print("deal:end")
    return result
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        result = loop.run_until_complete(deal(loop))
        print("main:result = {}".format(result))
    finally:
        loop.close()
    print("main end")
